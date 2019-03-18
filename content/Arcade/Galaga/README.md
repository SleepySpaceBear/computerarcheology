![Galaga](Galaga.jpg)

>>> deploy:<br>
>>>   CPU1.md
>>>   CPU2.md
>>>   CPU3.md
>>>   CPU1Fix.md
>>>   +Galaga.jpg
>>>   +galaga1.jpg
>>>   +galaga2.jpg
>>>   Journal.md

# Galaga No-fire Cheat

A snazzier version of this material was published in Circuit Cellar magazine. The editors did a wonderful job cleaning up my writing mess: 
[Debugging Commercial Code: A Quick Fix for Galaga Code in Circuit Cellar magazine November 2005](http://www.cc-webshop.com/Circuit-Cellar-Issue-184-November-2005-PDF-FI-2005-184.htm).

* [CPU1 (Main Game Controller)](CPU1.md)
* [CPU2 Game Helper](CPU2.md)
* [CPU3 Sound Processor](CPU3.md)

## Cheat Instructions

In the early 80's my Uncle Mike told me about a bug in the arcade game Galaga. If you know the secret, and if you are willing to wait 15 minutes, you can make the bees 
stop firing at you.

His instructions went something like this: on the first stage, let all the bees form up on the screen and then kill all of the bees except the one on the bottom left. 
Dodge that bee as it continues to attack, and eventually (about fifteen minutes later) it will stop firing. Kill it and none of the bees will fire for the rest of the game.

Galaga is still popular. I run into it in theatres and grocery stores and on retro-game pacs for other console systems. I rarely take the time to play out the cheat now. 
But the questions always nagged for the past decades. Was the cheat purposefully added to the code as a backdoor for players in-the-know? Or is the cheat a glitch in the 
software -- an unexpected side effect that persisted over several releases of the game ROMs? If the cheat is a glitch, what is wrong with the code? Is there another 
sequence of actions to get to the disabled state faster?

Time for the answers!

## The Dig Site 

Namco created Galaga (licensed to Midway) in 1981 as a sequel to Galaxian. The Galaga machine contains three Z-80 processors that share the load of playing the game. Each of 
the Galaga CPUs has its own ROM space. CPU1, the game boss, contains 16K of code while the other 2 slave-processors contain only 4K of code each. All three CPUs share the same 
RAM and I/O area. An 8K chunk of RAM is mapped into the exact center of the address space. This tiny RAM serves as video memory and general-purpose storage for all three CPUs. 
A hardware device mapped into the top of the RAM area controls the display of 64 sprites. The device reads sprite bitmaps from a special set of ROMs (12K total). Another special 
device, mapped just above RAM, generates the moving star-field behind the video display. All other I/O functions (joysticks, DIP switches, coin counters, etc) are controlled 
by a dedicated I/O processor mapped into the shared address space below RAM.

## Breaking Ground 

We will follow the code through the entire life cycle of a bee-shot. First, we will isolate and explore the segment of code that initiates a bee shot (we will call it the 
InitiateBeeShot routine). Next we will isolate and explore the segment of code that moves a bee shot on the screen (the MoveBeeFire routine). Finally, we will isolate and 
explore the segment of code that removes a bee shot from active play -- the RemoveBeeShot routine. By tracing the interactions of these three code segments, we should be able to unearth the reasons that the cheat works.

With an average of three bytes per instruction, 24K of Z80 code disassembles into roughly 8000 lines of assembler source. We are faced with over 136 pages of cryptic code 
listings. Where should we begin? Should we start with one of the smaller CPU2 and CPU3 listings or jump into the meat of the code, the 16K listing of CPU1?

We can do a little preliminary commenting in all three files based on what we know about the Z80 hardware. We know, for instance, that the first instruction executed is at 0000. 
We also know that NMI (non-maskable) interrupts cause the processor to call address 0066.

The first 7*8=56 bytes of each ROM are reserved for 7, 8-byte interrupt handlers. Hardware devices can request a call to any one of these 7 handlers by signaling an IRQ 
(non-maskable interrupt request) and placing the desired vector number on the data bus. An 8-byte interrupt service routine cannot do much; usually, a jump is made from the 
service area to a longer routine elsewhere in the ROM.

Galaga uses a simpler hardware interrupt strategy called Mode 1, which causes all IRQ requests to vector to the last handler at 0038 (the 7th handler). Thus we expect to find 
an interrupt handler routine at 0038 in the code.

CPU3 is dedicated to sound ... I doubt it contributes to the cheat. The CPU2 code is much smaller. I'll start there. Not long after startup, CPU2 goes into an infinite loop. 
Everything it does is interrupt driven with commands from CPU1.

As part of our dig, we will be making changes to the ROM images and observing the results when played in the MAME emulator. Note, however, that the initialization code performs 
a checksum to insure that the ROM is not corrupted. If we make changes to the code then the checksum will change and the game will halt at power up. Changing the byte 
at 0594 to FF defeats the checksum process. The CPU reports the checksum is good no matter what it calculates.

## CPU2 

### Command Vectoring 

The first part of the interrupt service routine is rather boring just bumping several timers. But the end of the routine is interesting. The code below shows how the interrupt 
handler vectors out to individual commands.

```plainCode
055D: 21 3B 00        LD      HL,$003B            ; Jump table
0560: 79              LD      A,C                 ; Command
0561: CB 27           SLA     A                   ; *2
0563: 85              ADD     A,L                 ; Offset into table
0564: 6F              LD      L,A                 ; Set HL to table point
0565: 5E              LD      E,(HL)              ; Get LSB
0566: 23              INC     HL                  ; Bump
0567: 56              LD      D,(HL)              ; Get MSB
0568: EB              EX      DE,HL               ; HL to DE
0569: C5              PUSH    BC                  ; Preserve BC (B=flag,C=command)
056A: CD 34 00        CALL    $0034               ; Vector to command
056D: C1              POP     BC                  ; Restore BC
...
0034: E9              JP      (HL)                ; Jump to routine pointed to by HL
```

The interrupt handler processes a list of commands supplied in shared memory by CPU1. The above code fetches a two-byte address for each command from a table at 003B and 
essentially performs a CALL to that address. The code below shows the contents of the jump table in memory at 003B.

```plainCode
; Jump table for commands
003B: BE 05       ;RET
003D: BF 05       ;     Commenting this disables the drawing of the Blue bees and the Big Bees
003F: D3 08       ;     Commenting this disables all enemies. They don't appear on the screen and the levels progress automatically upwards.
0041: BE 05       ; RET
0043: F5 06       ;     Commenting this disables player fire. The bullet appears but stays in place at the bottom. Collisions with it do not explode.
0045: EE 05       ;     Commenting this disables player collision detection. Bullets and bees pass under the player undetected.
0047: BE 05       ; RET
0049: CA 0E       ; ??Expansion check? Commenting seemed to have no effect.
```

The Z80 is a little-endian machine; the address bytes are stored LSB first. Command0 begins in ROM at 05BE. Note that the instruction at this location is simply a return. 
Command0 does nothing, and neither do commands 3 and 6. Why are these in the table? Are they placeholders for future expansion? Are they remnants of functionality that got 
left out?

Whenever you find a jump table like this in a ROM you are disassembling, you are in a great position to get a lot of information by patching. If we change the table at 0045 
to read BE05, we change the normal operation of this command to a do-nothing. By observing the behavior of the modified code in MAME, we can get a feel for what the command 
is doing. When we "patch out" Command5, we find that the player becomes invulnerable; bees and bee shots pass right through the player! Want to see what the upper levels look 
like? Make this patch.

When we patch out Command4, we see that the player shots appear at the bottom of the screen but never move upwards. Bees that fly into the motionless bullets do not explode. 
We can assume that Command4 is in charge of moving the player's fire and performing collision detection on the bees.

Command2 is a rather lengthy routine. It processes all moving bees in the game. If we patch out this command, CPU1 assumes that each level is complete as soon as it begins, 
and the game progresses from stage to stage rapidly.

Discovering the functions of these commands allows us to break up the ROM file into a several more manageable pieces. We are still looking for the code that initiates and 
manages bee shots, but we don't expect to find it in the Command5 code (in fact, the cheat still works with the collision-detection turned off). We also don't expect the cheat in Command4.

Command02 uses another vector table (stored at 0920) to reference 17 subcommands. Patching these out and playing the emulator hints a little at their use. If we patch out 
subcommand04, for instance, the bees appear on the screen but never leave their initial circles. The two lines of bees enter two tight circles and spin there 
forever (or until they are shot).

Command0D gets called to split a blue bee into three special bees in the later stages. Command09 takes effect when there are fewer than six bees on the screen. This subcommand 
is the continuous-attack pattern characteristic of play at the end of a stage.

### InitiateBeeShot 

I found the initiate bee shot routine by patching around in subcommand 5.

```plainCode
; Initiate bee shot
0D54: DD 35 0E        DEC     (IX+$0E)            ; Enough time ellapsed between shots?
0D57: C2 FA 0D        JP      NZ,$0DFA            ; No ... skip shooting.
0D5A: DD CB 0F 3E     SRL     (IX+$0F)            ; Another delay component ...
0D5E: D2 F4 0D        JP      NC,$0DF4            ; Too soon to drop another.
0D61: DD 7E 01        LD      A,(IX+$01)          ; Y coordinate
0D64: FE 4C           CP      $4C                 ; Don't fire if ...
0D66: DA F4 0D        JP      C,$0DF4             ; ... too close to the bottom.
0D69: 3A 15 90        LD      A,($9015)           ; Fighter ...
0D6C: A7              AND     A                   ; ... capture sequence?
0D6D: CA F4 0D        JP      Z,$0DF4             ; Yes ... no shooting
0D70: 3A AD 92        LD      A,($92AD)           ; After user ...
0D73: A7              AND     A                   ; ... explosion?
0D74: C2 F4 0D        JP      NZ,$0DF4            ; Yes ... skip shooting
0D77: EB              EX      DE,HL               ; Hold HL
0D78: 21 68 88        LD      HL,$8868            ; Shot pointers
0D7B: 06 08           LD      B,$08               ; 8 shots
0D7D: 7E              LD      A,(HL)              ; Get shot info
0D7E: FE 80           CP      $80                 ; Shot active?
0D80: 28 06           JR      Z,$D88              ; No -- use it
0D82: 2C              INC     L                   ; Try ...
0D83: 2C              INC     L                   ; ... next slot.
0D84: 10 F7           DJNZ    $D7D                ; Try all slots
0D86: 18 6C           JR      $DF4                ; None available ... reload 0E for this bee and do next bee
;
; While the cheat is in effect, all shots end up not
; finding a slot. All slots are taken. The question is ...
; ... why and what does it have to do with Movement9?
;
; Initialize shot
0D88: 36 06           LD      (HL),$06            ; First byte no longer 0x80
0D8A: 26 9B           LD      H,$9B               ;
...
0DDA: 7D              LD      A,L                 ; Get calculated X velocity
0DDB: FE 60           CP      $60                 ; X velocity too great?
0DDD: 38 02           JR      C,$DE1              ; No -- keep it
0DDF: 3E 60           LD      A,$60               ; Set max X velocity
0DE1: 47              LD      B,A                 ; Hold in B
0DE2: F1              POP     AF                  ;
0DE3: CB 18           RR      B                   ; X velocity divided by 2
0DE5: E1              POP     HL                  ; Restore 88xx pointer
0DE6: 7D              LD      A,L                 ; Add 8 bytes ...
0DE7: C6 08           ADD     A,$08               ; ... to LSB ...
0DE9: E6 0F           AND     $0F                 ; ... and Make it 0-15
0DEB: 21 B0 92        LD      HL,$92B0            ; Read by CPU1 while moving shots
0DEE: 85              ADD     A,L                 ; Add in new ...
0DEF: 6F              LD      L,A                 ; ... LSB offset.
0DF0: 70              LD      (HL),B              ; Set X velocity
0DF1: 23              INC     HL                  ; Point to Y velocity
0DF2: 36 00           LD      (HL),$00            ; Set Y velocity to 0 (not used by CPU1)
0DF4: 3A E2 92        LD      A,($92E2)           ; Reload ....
0DF7: DD 77 0E        LD      (IX+$0E),A          ; ... shot delay counter.
; Next bee
0DFA: 21 89 92        LD      HL,$9289            ; Counter
0DFD: 35              DEC     (HL)                ; All done?
0DFE: C8              RET     Z                   ; Yes ... out
0DFF: 11 14 00        LD      DE,$0014            ; Point to next ...
0E02: DD 19           ADD     IX,DE               ; ... structure
0E04: C3 E4 08        JP      $08E4               ; Continue with next bee.
```

While patching and exploring the movement subcommands of Command02, we glimpse a strange series of checks beginning at 0D54. These checks are protecting a segment of 
ode beginning at 0D7D. If all the conditions are not just right, the routine is skipped. We can quickly figure out what this special routine does by patching the code 
to ensure that it is ALWAYS skipped. When we NOP-out the two bytes at 0D84, we remove the only entry point into the routine. When we play the resulting images, we find 
that the bees do not fire at all! We have stumbled onto the code that initiates the bee shot.

To save space, the panel only shows a part of the routine. Bee shots are kept in another data structure. Two-byte flags beginning in RAM at 8868 mark a shot 
data-structure as being empty (first byte equals 80) or containing a bee shot (first byte 06). The code at 0D88 sets the shot structure to the "taken" state. Next, the 
shot inherits its X,Y coordinates from the parent bee. Then the code calculates the X velocity needed to send the shot towards the player.

The check at 0DDB keeps the X velocity to a reasonable value. If a bee is far to the player's left or right, the shot never gets enough horizontal velocity to be a 
threat. Change the byte at 0DDD to 18 and you change the instruction from a conditional jump to a jump always. Play the game, and you will see that no matter where the 
bee is, its shot can now reach you! This is an example of patching the logic flow.

Making patches to the logic flow is a powerful digging technique. We can patch the logic of the checks at 0D54 to see what conditions prevent a bee from firing. For 
instance, when we NOP-out the conditional jump at 0D66, the bees fire when they are too close to the bottom of the screen.

Notice that coming into this segment of code, IX points to a chunk of memory describing the firing bee. Each moving bee has one of these descriptors. Byte 0 and 1 are 
the X and Y coordinate of the bee respectively. Bye 0E is used as a delay between shots by the same bee. This prevents a bee from firing a rapid succession of shots.

Note the loop at 0D7D. This code looks for an empty data structure to put the shot in. There are only eight possible bee bullets allowed on the screen at once; if 
all are taken, no other shots are created.

Ah ha! Could this be the problem when the cheat is going on? Could it be that for some reason all the slots are remaining "taken" and the game can't find any available 
structures to create new shots?

### Shot Slot Instrumentation 

The below shows what we'll call an "instrument" -- a section of code that is inserted into normal play to collect data. Remember that the graphics screen is memory mapped. 
Writing to the screen memory causes a character to appear on the screen. This snippet of code displays the status of all eight shots on the graphics screen with a line of 
eight characters. We can place the instrument in place of Command05 (the player-collision-detection command). Now when the game calls for player collision detection, the 
status of the shot slots is updated on the screen. We can see how the shot structures are handled by playing the resulting images.

```plainCode
; This file patches the CPU2 code to show the status of the
; shot-slots on the screen.

;##$CPU Z80
;##$OriginalBinary 3600E.BIN
;##$PatchOutput c:\mame\roms\galagamw\

; Patch the initialization routine to skip looking up the checksum
;
0593: 3E FF     LD     A,$FF          ; Prevent checksum error

; Patch over the "Command 5:Player Collision Detection"
; Instead of checking, update the slots and return no-collision
;
05EE: 3A 68 88  LD    A,($8868)       ; From shot flag ...
05F1: 32 00 81  LD    ($8100),A       ; ... to screen
05F4: 3A 6A 88  LD    A,($886A)
05F7: 32 01 81  LD    ($8101),A       ; Brute force all flags
05FA: 3A 6C 88  LD    A,($886C)
05FD: 32 02 81  LD    ($8102),A
0600: 3A 6E 88  LD    A,($886E)
0603: 32 03 81  LD    ($8103),A
0606: 3A 70 88  LD    A,($8870)
0609: 32 04 81  LD    ($8104),A
060C: 3A 72 88  LD    A,($8872)
060F: 32 05 81  LD    ($8105),A
0612: 3A 74 88  LD    A,($8874)
0615: 32 06 81  LD    ($8106),A
0618: 3A 76 88  LD    A,($8876)
061B: 32 07 81  LD    ($8107),A 
061E: C9        RET                   ; No collision 
```

When we play the game, our hypothesis is proven. Initially, the screen shows a line of 0's (evidently character 80) when the slots are empty. When a bee fires, the 0's 
change to 6's. As the shots vanish off the bottom of the screen, the 6's turn back to 0's.

As that lone, left bee continues to dive, it occasionally drops a shot that never gets removed from the slot. Slowly, all the slots begin to fill up with invisible shots 
until 15 minutes later when they are all corrupt and the bee stops firing. The slots remain "taken" for the remainder of the game. The pictures below show how the instrument 
looks on the game screen. Note in the first screen shot that the first two shot structures are filled by the two shots moving towards the player. In the second screen-shot, 
all the shot structures are filled, yet there are no visible shots.

![](galaga1.jpg)
![](galaga2.jpg)

We now have at least part of the answer. Occasionally a shot structure is given a corrupted shot which never gets removed. Over time, all of the structures get corrupted and 
the bees can't fire. So where is the code that removes the shots? I suspect we will find it coupled to the code that moves the shot, but where? We don't even know which CPU's 
code to look at, but we can find out with a clever patch!

Let's patch an infinite loop at the bottom of the InitiateBeeShot routine -- say at 0DF4. As soon as a shot is initiated, CPU2 will come to a halt. When we play the game, we 
find that the bees act normally until the first shot was fired. Then every bee freezes -- as expected (CPU2 is in charge of moving the bees). We can still move our ship left 
and right; that must be controlled by CPU1. And what of the single shot that gets initiated? Interestingly, the bullet continues down the screen normally. Bee fire must also be 
controlled by CPU1, which is where our dig continues.

## CPU1 Game Controller 

### Interrupt Vectors 

We start with CPU1 just as we did before -- with the RST handles in the first 56 bytes of the ROM. As the code below shows, we find pretty much what we found in CPU2; there is 
a multiply routine and some buffer fillers. The initialization code squeezed in two instructions before jumping elsewhere. The interrupt handler at 0038 jumps away too. But 
notice the instruction just after the ISR at 003B. This might be the heart of a jump vector system, and we know from CPU2 how informative that can be.

```plainCode
0000: 3E 10           LD      A,$10               ; Send command ...
0002: 32 00 71        LD      ($7100),A           ; ... to IO processor
0005: C3 C4 02        JP      $02C4               ; Continue
;======================================================================
; Add A*2 to HL.
; If A=0, add 0x100 to HL
0008: 87              ADD     A,A                 ; A*2
0009: 30 05           JR      NC,$10              ; Not a special
000B: 24              INC     H                   ; Else HL+=0x100
000C: C3 10 00        JP      $0010               ; Continue
000F: FF              RST     $38                 ; Filler
;======================================================================
; Add A to HL
0010: 85              ADD     A,L                 ; Add offset to HL ...
0011: 6F              LD      L,A                 ; ... LSB
0012: D0              RET     NC                  ; No overflow
0013: 24              INC     H                   ; Else add in overvlow
0014: C9              RET                         ; Out
0015: FF              RST     $38                 ; Filler
0016: FF              RST     $38                 ; Filler
0017: FF              RST     $38                 ; Filler
;======================================================================
; Fill buffer with value in A HL = pointer B = length
0018: 77              LD      (HL),A              ; Fill byte in buffer
0019: 23              INC     HL                  ; Next byte
001A: 10 FC           DJNZ    $18                 ; Do until done
001C: C9              RET                         ; Done
001D: FF              RST     $38                 ; Filler
001E: FF              RST     $38                 ; Filler
001F: FF              RST     $38                 ; Filler
;======================================================================
; Subtract 0x20 from DE
; Subtracting 20 moves to the right one character on the screen
0020: 7B              LD      A,E                 ; LSB
0021: D6 20           SUB     $20                 ; Subtract 0x20
0023: 5F              LD      E,A                 ; Back to LSB
0024: D0              RET     NC                  ; No overflow
0025: 15              DEC     D                   ; Else borrow
0026: C9              RET                         ; Done
0027: FF              RST     $38                 ; Filler
;======================================================================
; Clear 0xF0 bytes starting at 9100 (bee space)
0028: 21 00 91        LD      HL,$9100            ; Bee space
002B: 06 F0           LD      B,$F0               ; Count
002D: AF              XOR     A                   ; Clear value
002E: DF              RST     $18                 ; Clear the bee buffer
002F: C9              RET                         ; Done
;======================================================================
0030: 37              SCF                         ; Set carry flag
0031: 08              EX      AF,AF'              ; Switch register bank
0032: C3 B5 13        JP      $13B5               ;
0035: FF              RST     $38                 ; Filler
0036: FF              RST     $38                 ; Filler
0037: FF              RST     $38                 ; Filler
;======================================================================
; Interrupt comes here
0038: C3 37 02        JP      $0237               ; Revector interrupt

;======================================================================
003B: E9              JP      (HL)                ; Indirection to HL
```

If we use the search capability in our text editor, we find that this instruction is CALLed from only one place -- 028E which is deep within the interrupt handler. CPU1 
must be using interrupt timing to perform command processing just like CPU2. The code below shows the jump table vector from the interrupt handler. You'll note that the 
jump table is located at 0096 in ROM. We can use our patching technique to uncover the workings of the individual routines.

### Checksum 

```plainCode
0280: 47              LD      B,A                 ;
0281: 21 96 00        LD      HL,$0096            ; Jump table
0284: 79              LD      A,C                 ;
0285: CB 27           SLA     A                   ;
0287: 85              ADD     A,L                 ;
0288: 6F              LD      L,A                 ;
0289: 5E              LD      E,(HL)              ;
028A: 23              INC     HL                  ;
028B: 56              LD      D,(HL)              ;
028C: EB              EX      DE,HL               ;
028D: C5              PUSH    BC                  ;
028E: CD 3B 00        CALL    $003B               ; Redirection to HL
```

But first, we must tackle another problem. Remember that CPU2 performs a checksum on its local ROM and communicates the results through a shared memory location. CPU1 
also performs the same check on its own ROMs -- probably near the point where the information is fetched from the other two CPUs. CPU2 wrote its checksum to 
location 9100. If we search CPU1 for a read of location 9100, we uncover the following section of code.

```plainCode
3568: CD 21 35        CALL    $3521               ; Checksum ROM 1
356B: 34              INC     (HL)                ;
356C: 0E 00           LD      C,$00               ;
356E: CD 21 35        CALL    $3521               ; Checksum ROM 2
3571: 34              INC     (HL)                ;
3572: 0E 00           LD      C,$00               ;
3574: CD 21 35        CALL    $3521               ; Checksum ROM 3
3577: 34              INC     (HL)                ;
3578: 0E 00           LD      C,$00               ;
357A: CD 21 35        CALL    $3521               ; Checksum ROM 4
357D: 36 FF           LD      (HL),$FF            ;
357F: 3A 00 91        LD      A,($9100)           ; CPU2 ROMs
3582: 32 30 68        LD      ($6830),A           ; Watchdog reset
3585: A7              AND     A                   ; Wait ...
3586: 28 F7           JR      Z,$357F             ; ... For CPU 2
3588: 3C              INC     A                   ; OK?
3589: 28 07           JR      Z,$3592             ; Yes ... move on to CPU3
358B: 3D              DEC     A                   ; Restore error
358C: 32 02 91        LD      ($9102),A           ; Save error code
358F: C3 35 35        JP      $3535               ; Print ROM/RAM report
3592: 3A 01 91        LD      A,($9101)           ; CPU3 ROMs
3595: 32 30 68        LD      ($6830),A           ; Watchdog reset
3598: A7              AND     A                   ; Wait ...
3599: 28 F7           JR      Z,$3592             ; ... For CPU 3
359B: 3C              INC     A                   ; OK?
359C: 28 17           JR      Z,$35B5             ; Yes ... continue
359E: 3D              DEC     A                   ; Restore error
359F: 32 02 91        LD      ($9102),A           ; Save error code
35A2: C3 35 35        JP      $3535               ; Print ROM/RAM report
```

First CPU1 checks its own four ROM chips. Then it waits for results from CPU2 and CPU3 in turn. The local checksum can be disabled by NOPing out the calls to 3521 
at each of the four places.

### Command Vectoring 

Now we can patch out the individual commands and observe the results. The code below shows the jump table from 0096. There are 32 commands in the table, but a number 
of the entries point to an RET instruction. These commands do absolutely nothing. By changing other entries to point to the same RET (at 083A) we can discover the 
functionality of the disabled command.

```plainCode
; Play functions called from ISR
0096: 3A 08       ;00:RET
0098: 3B 08       ;01:Draw player
009A: B2 17       ;02:?
009C: 00 17       ;03:? 
009E: 86 1A       ;04:?
00A0: 6A 08       ;05:?
00A2: 3A 08       ;06:RET
00A4: 3A 08       ;07:RET
00A6: 24 29       ;08:No bees come out on screen
00A8: EC 1D       ;09:No bees come out on screen
00AA: 9E 2A       ;0A:Explosion sequence for dead bee
00AC: B9 1D       ;0B:Bees freeze when shot and when entering block formation
00AE: EB 23       ;0C:Bees freak out when they leave their initial spin
00B0: AA 1E       ;0D:MOVE BEE FIRE
00B2: 38 1D       ;0E:?
00B4: 48 09       ;0F:Bees never leave the block formation
00B6: 6B 1B       ;10:Start attack patterns 
00B8: B2 19       ;11:Pause game for "Fighter Captured" and handle fighter to top
00BA: 7C 1D       ;12:?
00BC: 3A 08       ;13:RET
00BE: 8B 1F       ;14:Move player left or right
00C0: 0A 1F       ;15:Initiate player fire
00C2: 3A 08       ;16:RET
00C4: D8 1D       ;17:?Display icon and STAGE message at start of wave?
00C6: 30 22       ;18:Initiate tractor beam
00C8: D9 21       ;19:?More of tractor beam?
00CA: 3A 08       ;1A:RET
00CC: 3A 08       ;1B:RET
00CE: F2 20       ;1C:Fighter becomes "captured"
00D0: 00 20       ;1D:Coordinate free-fighter sequence
00D2: 3A 08       ;1E:RET
00D4: 8A 09       ;1F:Process inputs (coins)
```

When we disable Command14, we can't move the ship left or right. When we disable Command 15, we cannot fire a shot. When we comment out Command0D, the bee fire 
appears on the screen but does not move. We have found the MoveBeeFire code as shown below.

### MoveBeeFire Function 

```plainCode
; PLAY COMMAND 0D (Move Bee Fire)
1EAA: 3A A0 92        LD      A,($92A0)           ;
1EAD: E6 01           AND     $01                 ;
1EAF: C6 02           ADD     A,$02               ;
1EB1: 47              LD      B,A                 ;
1EB2: 3A 15 92        LD      A,($9215)           ; 0 = shots move up
1EB5: A7              AND     A                   ;
1EB6: 78              LD      A,B                 ;
1EB7: 28 02           JR      Z,$1EBB             ; Jump if 9215 is zero
1EB9: ED 44           NEG                         ; Shots moving down!
1EBB: DD 67           LD      IXH,A               ;
1EBD: 2E 68           LD      L,$68               ; Offset to fire space
1EBF: 11 B0 92        LD      DE,$92B0            ; X and Y velocity
1EC2: DD 2E 08        LD      IXL,$08             ; Eight shots to do
;
; Loop Here
1EC5: 26 8B           LD      H,$8B               ; Sprite color code
1EC7: 7E              LD      A,(HL)              ; Get sprite color
1EC8: FE 30           CP      $30                 ; Sprite color of a bee shot?
1ECA: 20 39           JR      NZ,$1F05            ; Not 30 - skip moving it
;
1ECC: 26 93           LD      H,$93               ; Sprite position
1ECE: 7E              LD      A,(HL)              ; Get position
1ECF: A7              AND     A                   ; Set flags
1ED0: 28 33           JR      Z,$1F05             ; If it is 0, skip moving it
;
1ED2: EB              EX      DE,HL               ;
1ED3: 46              LD      B,(HL)              ; Get X velocity
1ED4: 78              LD      A,B                 ;
1ED5: E6 7E           AND     $7E                 ;
1ED7: 2C              INC     L                   ;
1ED8: 86              ADD     A,(HL)              ;
1ED9: 4F              LD      C,A                 ;
1EDA: E6 1F           AND     $1F                 ;
1EDC: 77              LD      (HL),A              ;
1EDD: 2C              INC     L                   ;
1EDE: 79              LD      A,C                 ;
1EDF: 07              RLCA                        ;
1EE0: 07              RLCA                        ;
1EE1: 07              RLCA                        ;
1EE2: E6 07           AND     $07                 ;
1EE4: CB 78           BIT     7,B                 ; Left or right?
1EE6: 28 02           JR      Z,$1EEA             ; Right -- keep it
1EE8: ED 44           NEG                         ; Shots move to left
1EEA: EB              EX      DE,HL               ;
1EEB: 86              ADD     A,(HL)              ; Offset X coordinate
1EEC: 77              LD      (HL),A              ; New X coordinate
1EED: 2C              INC     L                   ; Y coordinate
1EEE: 7E              LD      A,(HL)              ; Get Y coordinate
1EEF: DD 84           ADD     A,IXH               ; Offset Y coordinate
1EF1: 77              LD      (HL),A              ; New Y coordinate
```

The interesting part of this routine is that it does not access the 8868 flags that CPU2 uses to spot a free shot structure. This routine simply looks at the 
coordinates and velocity of the shot sprites. Notice the check at 1ECC. If the X coordinate of the sprite is 0, the shot is ignored. Why?

It turns out to be a hardware thing. The hardware always draws all 64 sprites including the 8 bee shots. If a sprite has an X coordinate of 0, it is drawn off 
the screen to the left. This is how sprites are made inactive. When the MoveBeeFire routine sees an X coordinate of 0, it assumes the shot sprite is not being 
used and does not move it.

### RemoveBeeShot Function 

The frustrating part of this routine is that it only moves a shot -- it does not remove it from play. Some other part of the code is putting the value of 80 
into the shot structure. We'll use the search capability of our source editor to search for the #80 operand and identify every place where the value is stored 
into memory. We NOP these spots out (there are a number of them) one at a time and play the game to see which one is freeing the shot.

It turns out to be the instruction at 2588. When we comment out this set, the bee shots "wrap" from the bottom of the screen back to the top over and over again. 
The code below shows the RemoveBeeShot routine.

```plainCode
; Jump04,07:
; Remove item if Y coordinate is too close to bottom or top of screen.
255B: 26 93           LD      H,$93               ; Coordinates
255D: 6B              LD      L,E                 ;
255E: CB FD           SET     7,L                 ; ?
2560: 7E              LD      A,(HL)              ; {13} [00] Get X coordinate
2561: FE F4           CP      $F4                 ; => F4 ?
2563: 30 1A           JR      NC,$257F            ; Yes ... Remove from duty
2565: 2C              INC     L                   ; Point to Y
2566: 4E              LD      C,(HL)              ; {4A} [74] Get Y coordinate
2567: 26 9B           LD      H,$9B               ; This gets set as a special in the movement code
2569: 7E              LD      A,(HL)              ; {01} [00]
256A: 2D              DEC     L                   ; Restore pointer
256B: 0F              RRCA                        ; {C=1} [C=0]
256C: 79              LD      A,C                 ; {4A} [74] Y coordinate
256D: 1F              RRA                         ; {A5}
256E: FE 0B           CP      $0B                 ; If Y coordinate is too close to top of screen ...
2570: 38 0D           JR      C,$257F             ; ... remove it (Y< 0B).
2572: FE A5           CP      $A5                 ; If Y coordinate is too close to bottom of screen ...
2574: 30 09           JR      NC,$257F            ; ... remove it (Y>= A5).
2576: 1A              LD      A,(DE)              ; Get type
2577: FE 06           CP      $06                 ; Bee shot?
2579: C2 22 24        JP      NZ,$2422            ; Not a bee shot ... do something and next
257C: C3 24 24        JP      $2424               ; Do next
; Remove item from active duty
257F: CB BD           RES     7,L                 ;
2581: 1A              LD      A,(DE)              ; Type
2582: FE 03           CP      $03                 ;
2584: 28 0A           JR      Z,$2590             ;
2586: 3E 80           LD      A,$80               ; Flag free slot
2588: 12              LD      (DE),A              ; Here it is -- shots are erased here.
2589: 26 93           LD      H,$93               ; Free ...
258B: 36 00           LD      (HL),$00            ; ... sprite
258D: C3 24 24        JP      $2424               ; Do next
```

Actually, this code is part of a larger block of code -- the Command0C from the jump table. This is a huge routine that uses another jump table to perform 
several subcommands. One of these subcommands (subcommand06) removes score indications from the screen after they have been displayed for a couple of seconds. 
Subcommand04 (the RemoveBeeShot routine) removes sprites from play whose coordinates are too far off the top or bottom. The routine is used to remove both bees 
and shots that are leaving the screen. Most importantly, the routine only looks at the Y coordinate of the shot to determine removal.

## Testing a Hypothesis 

Here is the life cycle of a bee bullet. CPU2 initiates the shot and establishes the sprite coordinates. CPU1 moves all sprites whose X coordinates are not 0. CPU1 
also removes shots whose Y coordinates fall off the bottom of the screen. The slot is then available for another shot, and the cycle repeats.

But what happens if CPU2 drops a shot with X = 0? The movement routine would ignore it and the Y coordinate would never change. Thus the removal routine would never 
remove the shot, and the bullet would become "hung" in space off the left side of the screen where it would remain forever.

I feel confident that we have found the problem. Shots are being dropped at X=0; these shots are being ignored and never freed. What is the sequence to get to 
the cheat?

## The Sequence 

There are four bees on the very edges of the enemy rack. Two bees stick out on the bottom left and two on the bottom right. Normally all the bees stay well inside 
the bounds of the screen. However, when there are only six bees left in play a special attack pattern kicks in (Movement subcommand 09 in CPU2). This takes the bees 
out to the sides in wide, sweeping, diving arcs.

The bees on the far edges leave the screen and sweep out to X=0 (the bees on the right "wrap around" to 0). Note that only two bees are in the diving pattern at a 
time. The others are fixed in the rack. Every now and then (on average once every two minutes) a shot is initiated by one of these two bees at X=0. After about 15 minutes, 
all eight bee shot sprites become corrupted and no other shot can be made for the duration of the game.

Note that any dive, even the very first one, can snag a shot slot during the "end game" thus making the game a little easier. A normal player (one who doesn't wait around 
at the end of each level) might get very lucky and clog up three or four slots in the first few levels. I wonder how many high scores were aided by clogged slots.

## The Fix 

Of course our work is not really complete here until we actually FIX the software bug! The fix is rather straight forward. The InitiateBeeShot (in CPU2) must be modified 
to keep a shot from being dropped at X=0. One way is to increment the X coordinate to 1 if it is ever 0.

Space in the CPU2 ROM is tight, but there are eight bytes of empty space beginning at 0EC1. If we could re-assemble the CPU2 code, we could insert the extra code and 
recompile the whole thing. A patch takes up a bit more space since we have to put in a jump (3 bytes) to get out of the normal flow, and then we have to put in a jump 
(3 more bytes) back to the original flow. Our patch must also include the 3 bytes of code we overwrote in the original flow with our jump. In other words, our patch is 
going to need more space than the eight empty bytes we have identified. We'll have to over-write some existing functionality.

The Command7 routine at 0ECA in CPU2 reads bit 6 from the second set of DIP switches. The instruction manual says that this is the "Automatic Rack Advance" switch, which 
is normally off. Command7 simply returns when it sees the switch is off. That leaves a section of ROM available after the conditional jump. We can put our patch (shown below) 
in that area. When we test it in the emulator, we find that the "no shooting" cheat is corrected.

```plainCode
; This file patches the CPU2 code to fix the galaga-cheat. It makes
; sure a shot is never fired at X=0.
;
; Patch the initialization routine to skip looking up the checksum
;
0593: 3E FF     LD     A,$FF          ; Prevent checksum error

; There isn't room in-line for the fix, so jump out to a different
; area where we do have room to write code.
;
0D95: C3 D0 0E  JP     $ED0           ; Jump out to patch

; If X==0 then X=1
0ED0: A7        AND    A              ; Is the X coordinate 0?
0ED1: C2 D5 0E  JP     NZ,$ED5        ; No ... use it
0ED4: 3C        INC    A              ; Otherwise set it to 1
;
0ED5: 77        LD     (HL),A         ; Original 3 bytes ...
0ED6: 1C        INC    E              ; ... from ...
0ED7: 2C        INC    L              ; ... 0D95
0ED8: C3 98 0D  JP     $D98           ; Continue regular flow
```

## Updates 

Thanks to [Joe Zbiciak](http://spatula-city.org/~im14u2c/) for pointing out that the Z80 is a "little-endian" machine because it stores the LSB of a two byte value first. 
I had incorrectly called it a "big-endian". Thanks Joe.

Dan asked me to further define the cheat-sequence: which bees are involved and when the slots become taken. I turned on the slot-status instrumentation and tried lots of 
combinations. I discovered any of the four edge bees can clog a slot, but they only dive two at a time and only when there are less than seven bees on the screen. Thanks Dan.

Vecoven Frederic has disassembled the Galaga sound processor. See his awesome work here: [Vecoven Frederic -- Galaga Sound](http://www.vecoven.com/elec/galaga/galaga.html).

Thanks to Dan Price for correcting an odd phrasing.
