![Haunted House 1st Floor](HauntedHouse.jpg)

# Haunted House First Floor

>>> cpu Z80

>>> binary 42E9:Code1.bin

>>> memoryTable ram 
[RAM Usage](RAMUse1.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

# Start

```code
Start: 
42E9: C3 5E 43   JP      $435E           ; Skip over load-second-floor
     
; The second-floor of the game is a completely separate program that loads
; at $435E over the first floor code. Obviously this loading code must
; remain resident.

42EC: CD F8 01   CALL    $01F8           ; Turn off the tape drive
42EF: 21 41 43   LD      HL,$4341        ; "CHECKSUM[CR]"
42F2: CD D0 45   CALL    $45D0           ; Print message
```

# Script Command 17

 Script command 17 jumps here to load second floor

```code
ScriptCommand17: 
; LoadSecondFloorFromTape()
42F5: 31 FE 4F   LD      SP,$4FFE        ; Reset sack at top of RAM
42F8: 21 4A 43   LD      HL,$434A        ; "READY CASSETTE[CR]"
42FB: CD D0 45   CALL    $45D0           ; Print message
42FE: CD EE 45   CALL    $45EE           ; Get a key
4301: FE 0D      CP      $0D             ; Enter?
4303: C2 FE 42   JP      NZ,$42FE        ; No ... wait for player to press enter
4306: CD 93 02   CALL    $0293           ; Find the cassette header
4309: CD 35 02   CALL    $0235           ; Get one byte from the tape
430C: FE 55      CP      $55             ; Start of data?
430E: 20 F9      JR      NZ,$4309        ; No ... keep reading
;
4310: 06 06      LD      B,$06           ; Six bytes 
4312: 7E         LD      A,(HL)          ; ??? This is never used. Killing time?
4313: 23         INC     HL              ; Bump HL (??? This may be where the asterisk is going to print in model 1 routine)
4314: 10 FC      DJNZ    $4312           ; Keep going to add 6 to HL
4316: CD 2C 02   CALL    $022C           ; (Model I only) Blinks right asterisk during tape load operations
4319: CD 35 02   CALL    $0235           ; Get one byte from the tape
431C: FE 78      CP      $78             ; End of load?
431E: CA 5B 43   JP      Z,$435B         ; If yes then stop the cassette and start 2nd floor
4321: FE 3C      CP      $3C             ; Starting-point marker?
4323: 20 F4      JR      NZ,$4319        ; If no then go back and wait for the starting-point marker
4325: CD 35 02   CALL    $0235           ; Get count byte from the tape
4328: 47         LD      B,A             ; Count to B for DJNZ
4329: CD 14 03   CALL    $0314           ; Reads two byte destination from tape to HL register
432C: 85         ADD     A,L             ; COUNT + LSB ...
432D: 4F         LD      C,A             ; ... is expected checksum
432E: CD 35 02   CALL    $0235           ; Read one byte from tape
4331: 77         LD      (HL),A          ; Store in buffer
4332: 23         INC     HL              ; Bump buffer pointer
4333: 81         ADD     A,C             ; Add to ...
4334: 4F         LD      C,A             ; ... running checksum
4335: 10 F7      DJNZ    $432E           ; All B bytes read? No ... go back for them all
4337: CD 35 02   CALL    $0235           ; Get the final checksum byte from the tape
433A: B9         CP      C               ; Does our checksum match?
433B: CA 16 43   JP      Z,$4316         ; If yes then keep loading till end
433E: C3 EC 42   JP      $42EC           ; Do checksum error and try loading again
;     
; CHECKSUM[CR]
4341: 43 48 45 43 4B 53 55 4D 00

; READY CASSETTE[CR]                   
434A: 52 45 41 44 59 20 43 41 53 53 45 54 54 45 00
                 
4359: 00 00
                     
435B: CD F8 01   CALL    $01F8           ; Stop the cassette and fall into loaded second floor code

; First Floor starts here (the second floor loads here too)

435E: 31 B8 46   LD      SP,$46B8        ; Small stack space
4361: 3E 0E      LD      A,$0E           ; ??? Maybe ...
4363: CD 33 00   CALL    $0033           ; ... ??? clear the screen?
4366: 21 83 46   LD      HL,$4683        ; "HAUNTED HOUSE!!"
4369: CD D0 45   CALL    $45D0           ; Print welcome message
436C: CD EE 45   CALL    $45EE           ; Wait for the user to press a key

436F: 3E 10      LD      A,$10           ; Starting room is ...
4371: 32 E2 48   LD      ($48E2),A       ; ... 16 (OUTIDE OF HOUSE)
4374: CD 2D 49   CALL    $492D           ; Print the room description
;
4377: 97         SUB     A,A             ; A=0
4378: 32 7B 46   LD      ($467B),A       ; Clear noun (object within reach)
437B: 32 7C 46   LD      ($467C),A       ; Clear verb (throw, north, rub, etc)
437E: 32 7D 46   LD      ($467D),A       ; Grammar type (verb, verb+nounInReach, verb+nounInPack)
4381: CD 2F 44   CALL    $442F           ; Get user input line and parse
4384: 3A E2 48   LD      A,($48E2)       ; Room number
4387: 21 7F 47   LD      HL,$477F        ; Room descriptors
438A: CD C6 43   CALL    $43C6           ; Get 4 bytes for room
438D: 23         INC     HL              ; Skip over ...
438E: 23         INC     HL              ; ... to room's script pointer
438F: 7E         LD      A,(HL)          ; Script ...
4390: 23         INC     HL              ; ... pointer ...
4391: 66         LD      H,(HL)          ; ... to ...
4392: 6F         LD      L,A             ; ... HL
4393: CD D8 43   CALL    $43D8           ; Process the room script
4396: C2 A8 43   JP      NZ,$43A8        ; ZF clear ... script was successful. Move on.
4399: 21 F2 4A   LD      HL,$4AF2        ; General script
439C: CD D8 43   CALL    $43D8           ; Process the script
439F: C2 A8 43   JP      NZ,$43A8        ; ZF clear ... script was successful. Move on.
43A2: 21 0C 4F   LD      HL,$4F0C        ; Simply "NO"
43A5: CD AE 45   CALL    $45AE           ; Print "NO"
; Removed call to "after every command"
43A8: C3 77 43   JP      $4377           ; Back to get user input
```
         
# Get Object Info

```code
GetObjectInfo:  
; Return ZF set if found in desired location
; Return HL points to object location structure
43AB: 21 C8 48   LD      HL,$48C8        ; Object location table
43AE: CD BC 43   CALL    $43BC           ; A has object number ... two byte offset into table
43B1: 7E         LD      A,(HL)          ; Get location
43B2: E6 80      AND     $80             ; Is object contained by another
43B4: 23         INC     HL              ; Parent object (if any)
43B5: 7E         LD      A,(HL)          ; Get the parent object (if any ... does not affect ZF)
43B6: C2 AB 43   JP      NZ,$43AB        ; Bit is set ... find where the parent is
43B9: 2B         DEC     HL              ; HL back to start of object location
43BA: BB         CP      E               ; Is this object in the desired location?
43BB: C9         RET                     ; Done

; HL = HL + (A-1)*2
43BC: D5         PUSH    DE              ; Will be mangling this
43BD: EB         EX      DE,HL           ; HL to DE for a moment
43BE: 6F         LD      L,A             ; A - 1 ...
43BF: 2D         DEC     L               ; ... to ...
43C0: 26 00      LD      H,$00           ; ... HL
43C2: 29         ADD     HL,HL           ; Times 2
43C3: 19         ADD     HL,DE           ; Offset to HL
43C4: D1         POP     DE              ; Restore DE
43C5: C9         RET                     ; Done

; HL = HL + (A-1)*4
43C6: D5         PUSH    DE              ; Will be mangling this
43C7: EB         EX      DE,HL           ; HL to DE for a moment
43C8: 6F         LD      L,A             ; A - 1 ...
43C9: 2D         DEC     L               ; ... to ...
43CA: 26 00      LD      H,$00           ; ... HL
43CC: 29         ADD     HL,HL           ; Times 2
43CD: 29         ADD     HL,HL           ; Times 4
43CE: 19         ADD     HL,DE           ; Offset to HL
43CF: D1         POP     DE              ; Restore DE
43D0: C9         RET                     ; Done

; Set object's location
43D1: CD AB 43   CALL    $43AB           ; Find object
43D4: 23         INC     HL              ; Point to location
43D5: 73         LD      (HL),E          ; Change location
43D6: 2B         DEC     HL              ; Back to start of object
43D7: C9         RET                     ; Done
```

# Process Room Script

```code
; Process the user input against the script for a room
ProcessRoomScript: 
43D8: 7E         LD      A,(HL)          ; Next command to run
43D9: A7         AND     A               ; Zero means ...
43DA: C8         RET     Z               ; ... end of the list
43DB: FE FF      CP      $FF             ; If we get to an FF then ALWAYS ...
43DD: CA E4 43   JP      Z,$43E4         ; ... process the command (kind of like an ELSE)
43E0: 3A 7C 46   LD      A,($467C)       ; Verb word
43E3: BE         CP      (HL)            ; Does it match?
43E4: 23         INC     HL              ; Next byte
43E5: CA EF 43   JP      Z,$43EF         ; Yes ... go do it
43E8: 4E         LD      C,(HL)          ; Get length of command
43E9: 06 00      LD      B,$00           ; MSB is zero
43EB: 09         ADD     HL,BC           ; Skip to next command
43EC: C3 D8 43   JP      $43D8           ; Back to process next command
;
43EF: CD F6 43   CALL    $43F6           ; Run the command
43F2: C0         RET     NZ              ; Not zero if the command passed
43F3: C3 D8 43   JP      $43D8           ; The command failed ... keep running the list of commands
```

# Run Script

```code
RunScript: 
43F6: E5         PUSH    HL              ; Make room for the end point (and hold the current value)
43F7: 4E         LD      C,(HL)          ; Get the length of the script (length INCLUDES the length byte)
43F8: 06 00      LD      B,$00           ; MSB is 0
43FA: 09         ADD     HL,BC           ; This is where the script ends
43FB: E3         EX      (SP),HL         ; Put the end pointer on the stack (and restore the current value)
43FC: 23         INC     HL              ; The actual script command
;
```

# Run Script Command

```code
;
RunScriptCommand: 
43FD: 7E         LD      A,(HL)          ; Get the script command
43FE: 23         INC     HL              ; Point to first parameter
43FF: E5         PUSH    HL              ; Current script location
4400: 21 FD 48   LD      HL,$48FD        ; Jump table of commands
4403: CD BC 43   CALL    $43BC           ; Offset A-1 into commands table
4406: 7E         LD      A,(HL)          ; Get LSB
4407: 23         INC     HL              ; Point to MSB
4408: 66         LD      H,(HL)          ; Get MSB
4409: 6F         LD      L,A             ; LSB to HL
440A: E9         JP      (HL)            ; Jump to the command
```

# Script Command PASS

```code
ScriptCommandPASS:       
440B: E1         POP     HL              ; Current script pointer
440C: D1         POP     DE              ; Where we should end
440D: 7C         LD      A,H             ; MSB ...
440E: BA         CP      D               ; ... the same?
440F: C2 1A 44   JP      NZ,$441A        ; No ... keep processing
4412: 7D         LD      A,L             ; LSB ...
4413: BB         CP      E               ; ... the same?
4414: C2 1A 44   JP      NZ,$441A        ; No ... keep processing
4417: F6 01      OR      $01             ; Clear Zero Flag (PASS)
4419: C9         RET                     ; Return
441A: D5         PUSH    DE              ; Put end back on the stack
441B: C3 FD 43   JP      $43FD           ; Keep running commands
```

# Script Command FAIL

```code
ScriptCommandFAIL: 
441E: E1         POP     HL              ; Pop the current script pointer
441F: E1         POP     HL              ; Pop the ending spot
4420: AF         XOR     A               ; Set Zero Flag (FAIL)
4421: C9         RET                     ; Done
```

# Script Command 06

```code
ScriptCommand06: 
; SubscriptAbortAllIfPass(...)
; Run the subscript. If the subscript passes then abort the current script and
; all parent scripts. If the subscript fails then continue on to the next command.
;
; How does this abort all current scripts, you ask?
; 43F6 only has two callers: the primary caller and the code here at 4423. The RET
; at 442E returns either to that primary caller or to 4426. The code at 4426 keeps
; the zero flag clear which continues to call return for subscripts eventually
; getting back to the primary caller.
4422: E1         POP     HL              ; Current script pointer
4423: CD F6 43   CALL    $43F6           ; Run the list of commands
4426: E5         PUSH    HL              ; Points passed the list just executed
4427: CA 0B 44   JP      Z,$440B         ; Subscript failed ... but keep going in current script
; The subscript failed. Bail out (with a PASS)
442A: E1         POP     HL              ; Current script pointer
442B: E1         POP     HL              ; End of script
442C: F6 01      OR      $01             ; Clear Zero Flag (PASS)
442E: C9         RET					 ; Done
```
           
# Parse User Input

```code          
ParseUserInput: 
442F: CD 05 46   CALL    $4605           ; Prompt and read line
4432: CD DA 44   CALL    $44DA           ; Parse the input string
4435: 2A AC 45   LD      HL,($45AC)      ; Pointer to noun data
4438: 3A AA 45   LD      A,($45AA)       ; Number of bytes ...
443B: 47         LD      B,A             ; ... in noun data
443C: 3A 7D 46   LD      A,($467D)       ; Grammar type
443F: FE 03      CP      $03             ; Value 3 means nothing in buffer
4441: CA 2F 44   JP      Z,$442F         ; Ignore blank lines
4444: 3A 7B 46   LD      A,($467B)       ; Noun number
4447: A7         AND     A               ; Was there a noun on the input line?
4448: C2 6A 44   JP      NZ,$446A        ; Yes ... check for verb-noun things
444B: 3A 7C 46   LD      A,($467C)       ; Verb
444E: A7         AND     A               ; Did we have a verb?
444F: C2 5B 44   JP      NZ,$445B        ; Yes ... check for verb-only things
;
; Something was typed, but no noun or verb were decoded
4452: 21 A7 4F   LD      HL,$4FA7        ; I_DON'T_UNDERSTAND.[CR]
4455: CD AE 45   CALL    $45AE           ; Print the error
4458: C3 2F 44   JP      $442F           ; Back to the top
;
445B: 3A 7D 46   LD      A,($467D)       ; Grammar type
445E: FE C0      CP      $C0             ; Is the verb nounless?
4460: C8         RET     Z               ; Yes ... done (we don't have a noun)
;
; We have a verb that expected a noun, but no noun was given
4461: 21 7F 4D   LD      HL,$4D7F        ; WHAT?[CR]
4464: CD AE 45   CALL    $45AE           ; Print error (verb expected noun)
4467: C3 2F 44   JP      $442F           ; Back to top of input loop
;
; We have a verb and a noun
446A: 22 AC 45   LD      ($45AC),HL      ; Pointer into noun data
446D: 3A D9 44   LD      A,($44D9)       ; Did we have ...
4470: A7         AND     A               ; ... lone noun last parse?
4471: C2 C6 44   JP      NZ,$44C6        ; Yes ... use that now
;
4474: 7E         LD      A,(HL)          ; Next word-for-object value
4475: 23         INC     HL              ; Bump ...
4476: 22 AC 45   LD      ($45AC),HL      ; ... word-data pointer
4479: 1E FF      LD      E,$FF           ; Look in backpack first
447B: C5         PUSH    BC              ; Hold
447C: CD AB 43   CALL    $43AB           ; Find object
447F: C1         POP     BC              ; Restore
4480: CA BE 44   JP      Z,$44BE         ; Found object. Use it.
4483: 3A 7D 46   LD      A,($467D)       ; Grammar type
4486: FE 40      CP      $40             ; 01 ... noun must be in pack
4488: CA 9C 44   JP      Z,$449C         ; Validate noun
448B: 2A AC 45   LD      HL,($45AC)      ; Pointer to noun data
448E: 2B         DEC     HL              ;
448F: 3A E2 48   LD      A,($48E2)       ; Current room
4492: 5F         LD      E,A             ; For find
4493: 7E         LD      A,(HL)          ; Back up data pointer
4494: C5         PUSH    BC              ; Hold
4495: CD AB 43   CALL    $43AB           ; Do find
4498: C1         POP     BC              ; Restore
4499: CA BE 44   JP      Z,$44BE         ; Object is in room. Use it.
;
449C: 2A AC 45   LD      HL,($45AC)      ; Noun data
449F: 05         DEC     B               ; All tried?
44A0: C2 74 44   JP      NZ,$4474        ; No ... try next word
44A3: 3A 7D 46   LD      A,($467D)       ; Grammar type
44A6: FE 40      CP      $40             ; 01 ... noun must be in pack
44A8: C2 B1 44   JP      NZ,$44B1        ; Could be pack or room
44AB: 21 72 4F   LD      HL,$4F72        ; YOU_AREN'T_CARRYING_IT.[CR]
44AE: C3 B4 44   JP      $44B4           ; Print and out
44B1: 21 84 4F   LD      HL,$4F84        ; THERE'S_NOT_ONE_HERE.[CR]
44B4: CD AE 45   CALL    $45AE           ; Print error
44B7: 97         SUB     A,A             ; This noun doesn't ...
44B8: 32 7B 46   LD      ($467B),A       ; ... count
44BB: C3 2F 44   JP      $442F           ; Back to top of input loop
;
44BE: 2A AC 45   LD      HL,($45AC)      ; Noun data
44C1: 2B         DEC     HL              ; Back to word pointer
44C2: 7E         LD      A,(HL)          ; Get the for-object value
44C3: 32 7B 46   LD      ($467B),A       ; Hold the value
;
44C6: 3A 7C 46   LD      A,($467C)       ; Verb
44C9: A7         AND     A               ; Was there a verb?
44CA: C0         RET     NZ              ; Yes ... got what we need
44CB: 21 94 4F   LD      HL,$4F94        ; WHAT_SHOULD_I_DO_WITH_IT?[CR]
44CE: CD AE 45   CALL    $45AE           ; Print message
44D1: 3E 01      LD      A,$01           ; Flag that we have a lone ...
44D3: 32 D9 44   LD      ($44D9),A       ; ... noun
44D6: C3 2F 44   JP      $442F           ; Back to the top of input loop
           
44D9: 00 ; 1 if there was a lone object last input             

; Parse the input line
ParseInputLine: 
44DA: 21 5A 46   LD      HL,$465A        ; Start of the input
44DD: 97         SUB     A,A             ; Make a zero
44DE: 32 AB 45   LD      ($45AB),A       ; Nothing in buffer to start with
44E1: 32 7D 46   LD      ($467D),A       ; Grammar type
;
44E4: 11 4B 4A   LD      DE,$4A4B        ; Command table
44E7: EB         EX      DE,HL           ; Next word to HL 
44E8: 22 7F 46   LD      ($467F),HL      ; Pointer to next word to check
44EB: EB         EX      DE,HL           ; Back to DE
; Skip spaces before a word
44EC: 7E         LD      A,(HL)          ; Next character from input buffer
44ED: FE 20      CP      $20             ; A space?
44EF: C2 F6 44   JP      NZ,$44F6        ; No ... decode this input
44F2: 23         INC     HL              ; It is a space, skip over it
44F3: C3 EC 44   JP      $44EC           ; And keep trying
;
44F6: A7         AND     A               ; Reached the end ...
44F7: CA 81 45   JP      Z,$4581         ; ... of the line
44FA: 3E 01      LD      A,$01           ; Flag that something ...
44FC: 32 AB 45   LD      ($45AB),A       ; ... is in the buffer
44FF: E5         PUSH    HL              ; Hold start of word
4500: 1A         LD      A,(DE)          ; Have we reached ...
4501: A7         AND     A               ; ... the end of the command table?
4502: CA 8C 45   JP      Z,$458C         ; Yes ... give error
4505: 32 82 46   LD      ($4682),A       ; Store word data
4508: E6 07      AND     $07             ; Size of text ...
450A: 4F         LD      C,A             ; ... to C
450B: 32 81 46   LD      ($4681),A       ; Text count
450E: 3A 82 46   LD      A,($4682)       ; Word data again
4511: E6 38      AND     $38             ; Mask 0_111_000
4513: 0F         RRCA                    ; Get ...
4514: 0F         RRCA                    ; ... number of ...
4515: 0F         RRCA                    ; ... data bytes
4516: 47         LD      B,A             ; To B
4517: EB         EX      DE,HL           ; Update ...
4518: 22 7F 46   LD      ($467F),HL      ; ... command table ...
451B: EB         EX      DE,HL           ; ... pointer
451C: 13         INC     DE              ; Next in word text
451D: 1A         LD      A,(DE)          ; Character from table
451E: BE         CP      (HL)            ; Same as user input?
451F: C2 73 45   JP      NZ,$4573        ; No ... not this word
4522: 23         INC     HL              ; Next character ...
4523: 13         INC     DE              ; ... to try
4524: 0D         DEC     C               ; Tried all in the table?
4525: C2 1D 45   JP      NZ,$451D        ; No ... keep looking
4528: 3A 81 46   LD      A,($4681)       ; Text count
452B: FE 04      CP      $04             ; Four (or more)?
452D: CA 3A 45   JP      Z,$453A         ; Yes ... we need to ignore extras
4530: 7E         LD      A,(HL)          ; Next in buffer
4531: FE 20      CP      $20             ; Word ended correctly in the buffer?
4533: CA 48 45   JP      Z,$4548         ; Yes ... this is our word
4536: A7         AND     A               ; Word ended correctly at end of buffer?
4537: C2 78 45   JP      NZ,$4578        ; No ... not our word
;Skip to end of word
453A: 7E         LD      A,(HL)          ; Next character in buffer
453B: FE 20      CP      $20             ; A space?
453D: CA 48 45   JP      Z,$4548         ; Yes ... word matched
4540: A7         AND     A               ; End of buffer?
4541: CA 48 45   JP      Z,$4548         ; Yes ... word matched
4544: 23         INC     HL              ; Next in input buffer
4545: C3 3A 45   JP      $453A           ; Skip to end of the word
; Word matched
4548: 3A 82 46   LD      A,($4682)       ; Word data
454B: E6 C0      AND     $C0             ; Top two bits ... word type
454D: CA 5A 45   JP      Z,$455A         ; Word is a noun
4550: 32 7D 46   LD      ($467D),A       ; Store grammar type
4553: 1A         LD      A,(DE)          ; Get word number
4554: 32 7C 46   LD      ($467C),A       ; Store verb
4557: C3 6B 45   JP      $456B           ; Check for more to parse
;Word is a noun
455A: 1A         LD      A,(DE)          ; Noun number from the word's data
455B: 32 7B 46   LD      ($467B),A       ; Hold word number
455E: EB         EX      DE,HL           ; Store ...
455F: 22 AC 45   LD      ($45AC),HL      ; ... pointer to noun data
4562: EB         EX      DE,HL           ; Restore pointers
4563: 78         LD      A,B             ; Number of data bytes
4564: 32 AA 45   LD      ($45AA),A       ; Hold this for later
4567: 97         SUB     A,A             ; No longer remember ...
4568: 32 D9 44   LD      ($44D9),A       ; ... a past lone object

456B: 7E         LD      A,(HL)          ; Next from buffer
456C: FE 20      CP      $20             ; Is it a space
456E: D1         POP     DE              ; Restore command table pointer
456F: CA E4 44   JP      Z,$44E4         ; Yes ... more input. Parse next word.
4572: C9         RET                     ; That's all the input we need
; Word doesn't match
4573: 13         INC     DE              ; Skip ...
4574: 0D         DEC     C               ; ... to end of word text ...
4575: C2 73 45   JP      NZ,$4573        ; ... in table
4578: 13         INC     DE              ; Skip to end ...
4579: 05         DEC     B               ; ... of data ...
457A: C2 78 45   JP      NZ,$4578        ; ... bytes
457D: E1         POP     HL              ; Back to start of word
457E: C3 EC 44   JP      $44EC           ; Try next word in command table

; End of input
4581: 3A AB 45   LD      A,($45AB)       ; Something in ...
4584: A7         AND     A               ; ... the buffer?
4585: C0         RET     NZ              ; Yes ... done
4586: 3E 03      LD      A,$03           ; Grammar type 3 means ...
4588: 32 7D 46   LD      ($467D),A       ; ... nothing in buffer
458B: C9         RET                     ; Done

; Skip leading space in front of token and then skip to next token.
; If there is another token go back and decode. Otherwise return.
458C: E1         POP     HL              ; Start of word
458D: 97         SUB     A,A             ; Clear ...  
458E: 32 7C 46   LD      ($467C),A       ; ... verb ...
4591: 32 7B 46   LD      ($467B),A       ; ... and noun
4594: 7E         LD      A,(HL)          ; Next character
4595: FE 20      CP      $20             ; A space?
4597: C2 9E 45   JP      NZ,$459E        ; No ... out of loop
459A: 23         INC     HL              ; Next in input
459B: C3 94 45   JP      $4594           ; Skip spaces
;
459E: 7E         LD      A,(HL)          ; Next in buffer          
459F: A7         AND     A               ; End of buffer?
45A0: C8         RET     Z               ; Yes ... out
45A1: FE 20      CP      $20             ; Space?
45A3: CA E4 44   JP      Z,$44E4         ; Restart at top of command list
45A6: 23         INC     HL              ; Next input
45A7: C3 9E 45   JP      $459E           ; Keep looking

; RAM used in parsing input
45AA: 00       ; Number of data bytes in noun       
45AB: 00       ; 0 if decode is empty, 1 if something was decoded               
45AC: 00 00    ; Pointer to noun data            
```

# Print Packed

```code
PrintPacked: 
; Unpack a message (or multiple packed message) and print.
; HL is pointer to message   
45AE: 7E         LD      A,(HL)          ; Get the length
45AF: A7         AND     A               ; None ... 
45B0: C8         RET     Z               ; ... out
45B1: 23         INC     HL              ; Skip over length
45B2: 11 5A 46   LD      DE,$465A        ; Buffer
45B5: CD B9 46   CALL    $46B9           ; Unpack and print
45B8: 7E         LD      A,(HL)          ; Get terminator
45B9: A7         AND     A               ; Zero ...
45BA: CA E7 45   JP      Z,$45E7         ; ... print carriage return and out
45BD: FE 01      CP      $01             ; Leave alone?
45BF: C8         RET     Z               ; Yes ... we are done
45C0: 47         LD      B,A             ; To position for print
45C1: E5         PUSH    HL              ; Hold HL
45C2: CD FF 45   CALL    $45FF           ; Print the character
45C5: E1         POP     HL              ; Restore HL
45C6: 7E         LD      A,(HL)          ; Get next byte from unpacked
45C7: FE 0A      CP      $0A             ; Mark for another packing?
45C9: 23         INC     HL              ; 
45CA: CA AE 45   JP      Z,$45AE         ; Yes ... start again
45CD: C3 B8 45   JP      $45B8           ; No ... continue this packing
```
    
# Print Message

```code
; HL points to message terminated by
;  - 0 : add a CR on the end and return
;  - 1 : no CR on the end and return
; Return with B holding last character (if any) sent to ROM routine.
;
PrintMessage: 
45D0: 7E         LD      A,(HL)          ; Get next character from message
45D1: A7         AND     A               ; End of message (with CR)?
45D2: CA E7 45   JP      Z,$45E7         ; Yes ... print CR and return
45D5: FE 01      CP      $01             ; End of message (no CR)?
45D7: C8         RET     Z               ; Yes ... done
45D8: FE 40      CP      $40             ; Skip over character?
45DA: CA E3 45   JP      Z,$45E3         ; Yes ... just advance cursor
45DD: 47         LD      B,A             ; Character to B
45DE: E5         PUSH    HL              ; Hold message pointer
45DF: CD FF 45   CALL    $45FF           ; Print character
45E2: E1         POP     HL              ; Increment ...
45E3: 23         INC     HL              ; ... message pointer
45E4: C3 D0 45   JP      $45D0           ; Next character in message
;           
45E7: 06 0D      LD      B,$0D           ; CR character
45E9: 78         LD      A,B             ; To A
45EA: CD FF 45   CALL    $45FF           ; Print character
45ED: C9         RET                  
```
   
# Wait For Key

```code
WaitForKey: 
45EE: D5         PUSH    DE              ; Hold DE
45EF: 3A 7E 46   LD      A,($467E)       ; Bump ...
45F2: 3C         INC     A               ; ... some ...
45F3: 32 7E 46   LD      ($467E),A       ; ... ??? counter
45F6: CD 2B 00   CALL    $002B           ; Get a key
45F9: A7         AND     A               ; Keep waiting ...
45FA: CA EF 45   JP      Z,$45EF         ; ... if nothing pressed
45FD: D1         POP     DE              ; Restore DE
45FE: C9         RET                     ; Return key in A
```

# PrintChar

```code
PrintChar:       
45FF: D5         PUSH    DE              ; Hold DE
4600: CD 33 00   CALL    $0033           ; Print the character
4603: D1         POP     DE              ; Restore DE
4604: C9         RET                     ; Done
```

# PromptAndReadLine

```code
PromptAndReadLine: 
4605: 06 3A      LD      B,$3A           ; ":" for prompt
4607: 78         LD      A,B             ; To A for printing
4608: CD FF 45   CALL    $45FF           ; Print the prompt
460B: 21 5A 46   LD      HL,$465A        ; Input buffer
460E: 0E 00      LD      C,$00           ; Size of input buffer (starts empty)
;
4610: E5         PUSH    HL              ; Hold ...
4611: C5         PUSH    BC              ; ... most ...
4612: D5         PUSH    DE              ; ... everything
4613: CD EE 45   CALL    $45EE           ; Wait for a key
4616: D1         POP     DE              ; ... restore ...
4617: C1         POP     BC              ; ... most ...
4618: E1         POP     HL              ; ... everything
4619: 47         LD      B,A             ; Key to B
461A: FE 08      CP      $08             ; A backspace?
461C: CA 41 46   JP      Z,$4641         ; Yes ... go handle that
461F: 77         LD      (HL),A          ; Put character in buffer
4620: CD FF 45   CALL    $45FF           ; Send the character to the screen
4623: FE 0D      CP      $0D             ; Was it ENTER?
4625: CA 57 46   JP      Z,$4657         ; Yes ... we have our line
4628: 0C         INC     C               ; Bump the input count
4629: 23         INC     HL              ; Bump the pointer in the buffer
462A: 11 7A 46   LD      DE,$467A        ; End of buffer (32 bytes long)
462D: 7C         LD      A,H             ; Compare ...
462E: BA         CP      D               ; ... MSB
462F: DA 10 46   JP      C,$4610         ; Not the same ... still room for more
4632: 7D         LD      A,L             ; Compare ...
4633: BB         CP      E               ; ... LSB
4634: DA 10 46   JP      C,$4610         ; Not the same ... still room for more
4637: 06 08      LD      B,$08           ; No more room. Take the last ...
4639: 78         LD      A,B             ; ... character ...
463A: CD FF 45   CALL    $45FF           ; ... off the screen
463D: 2B         DEC     HL              ; And reject the character from our buffer
463E: C3 10 46   JP      $4610           ; Back for more input (better be backspaces)
; Backspace
4641: 2B         DEC     HL              ; Back up our pointer
4642: 3E 46      LD      A,$46           ; Compare MSB to ...
4644: BC         CP      H               ; ... start of buffer
4645: DA 4E 46   JP      C,$464E         ; Not the same. We can take it.
4648: 7D         LD      A,L             ; Compare LSB to ...
4649: FE 5A      CP      $5A             ; ... start of buffer
464B: DA 0B 46   JP      C,$460B         ; Nothing left to remove. Ignore this.
464E: 3E 08      LD      A,$08           ; Backspace ...
4650: 47         LD      B,A             ; ... to ...
4651: CD FF 45   CALL    $45FF           ; ... screen
4654: C3 10 46   JP      $4610           ; Back to input loop
; Enter
4657: 36 00      LD      (HL),$00        ; Put a zero on the end of the buffer        
4659: C9         RET                     ; Done
```

# Input Buffer

```code
; Input buffer (with some uninitialized leftover data!)
InputBuffer: 
; 32 bytes
;     -- F  6  -- -- E  _  I  P  _  S  I  G  N  -- --
465A: 15 46 36 00 C9 45 20 49 50 20 53 49 47 4E 00 00
;     G  -- -- (  &  -- <  _  -- -- -- /  /  -- -- .         
466A: 47 FE 78 28 26 FE 3C 20 F5 CD 82 47 47 CD 9C 46
        
467A: 00

; Used in input parsing
467B: 00    ; Noun
467C: 00    ; Verb
467D: 00    ; Grammar type
467E: 00    ; Input loop counter (never used)
467F: 00 00 ; Pointer to next word while parsing                      
4681: 00    ; Character counter in word text                  
4682: 00    ; Current word data   
  
; "HAUNTED HOUSE!![CR]"             
4683: 48 41 55 4E 54 45 44 20 48 4F 55 53 45 21 21 00
       
; Uninitialized stack space with some leftover data in it!
; This might be interesting stuff?
StackRAM: 
4693: 15 40 0D 02 C0 3F 80 04 DD 03 1D 40 15 40 D4 4D 
46A3: 5E 0D 08 46 5F 46 FA 48 97 4A FA 48 FA 48 26 44                
46B3: FE 48 F2 43 93   
; Stack points here at beginning    
46B8: 00 
```

# Unpack Message

```code
UnpackMessage: 
; TODO: Decode this. I have a program created by translating this to Java.
; It works, but it would be nice to understand the math here.
46B9: 32 7B 47   LD      ($477B),A       ;
46BC: 3E 01      LD      A,$01           ;
46BE: 32 7E 47   LD      ($477E),A       ;
46C1: C3 CB 46   JP      $46CB           ;     
46C4: 32 7B 47   LD      ($477B),A       ;
46C7: 97         SUB     A,A             ;  
46C8: 32 7E 47   LD      ($477E),A       ;
46CB: E5         PUSH    HL              ;
46CC: 06 03      LD      B,$03           ;
46CE: E1         POP     HL              ;
46CF: 7E         LD      A,(HL)          ;
46D0: 23         INC     HL              ;
46D1: 4E         LD      C,(HL)          ;
46D2: 23         INC     HL              ;
46D3: E5         PUSH    HL              ;
46D4: 61         LD      H,C             ;
46D5: 6F         LD      L,A             ;
46D6: 13         INC     DE              ;
46D7: 13         INC     DE              ;
46D8: EB         EX      DE,HL           ;   
46D9: E5         PUSH    HL              ;
46DA: C5         PUSH    BC              ;
46DB: 21 28 00   LD      HL,$0028        ; Number of characters in map
46DE: 22 7C 47   LD      ($477C),HL      ; 
46E1: 21 11 47   LD      HL,$4711        ;
46E4: 36 11      LD      (HL),$11        ; 17 passes
46E6: 01 00 00   LD      BC,$0000        ;
46E9: C5         PUSH    BC              ;
46EA: 7B         LD      A,E             ;
46EB: 17         RLA                     ;
46EC: 5F         LD      E,A             ;
46ED: 7A         LD      A,D             ;
46EE: 17         RLA                     ;
46EF: 57         LD      D,A             ;
46F0: 35         DEC     (HL)            ;
46F1: E1         POP     HL              ;
46F2: CA 12 47   JP      Z,$4712         ;
46F5: 3E 00      LD      A,$00           ;
46F7: CE 00      ADC     A,$00           ; 
46F9: 29         ADD     HL,HL           ;
46FA: 44         LD      B,H             ;
46FB: 85         ADD     A,L             ;
46FC: 2A 7C 47   LD      HL,($477C)      ;
46FF: 95         SUB     A,L             ;  
4700: 4F         LD      C,A             ;
4701: 78         LD      A,B             ;
4702: 9C         SBC     A,H             ; 
4703: 47         LD      B,A             ;
4704: C5         PUSH    BC              ;
4705: D2 0A 47   JP      NC,$470A        ;
4708: 09         ADD     HL,BC           ;
4709: E3         EX      (SP),HL         ;
470A: 21 11 47   LD      HL,$4711        ;
470D: 3F         CCF                     ;
470E: C3 EA 46   JP      $46EA           ;
4711: 00                                 ;
4712: 01 53 47   LD      BC,$4753        ; Character compression map
4715: 09         ADD     HL,BC           ; Offset into table
4716: 7E         LD      A,(HL)          ; Get the character value
4717: C1         POP     BC              ; Restore BC
4718: E1         POP     HL              ; Restore pointer to buffer
4719: 77         LD      (HL),A          ; Replace the character with the decoded value
471A: 2B         DEC     HL              ; Next character (moving left)
471B: 05         DEC     B               ; All done?
471C: C2 D9 46   JP      NZ,$46D9        ; No ... keep decoding
471F: 3A 7E 47   LD      A,($477E)       ;
4722: A7         AND     A               ;
4723: CA 3B 47   JP      Z,$473B         ;
4726: E5         PUSH    HL              ;
4727: C5         PUSH    BC              ;
4728: D5         PUSH    DE              ;
4729: 1E 03      LD      E,$03           ;
472B: 23         INC     HL              ;
472C: 46         LD      B,(HL)          ;
472D: E5         PUSH    HL              ;
472E: 78         LD      A,B             ;
472F: CD FF 45   CALL    $45FF           ; Print character
4732: E1         POP     HL              ;
4733: 23         INC     HL              ;
4734: 1D         DEC     E               ;
4735: C2 2C 47   JP      NZ,$472C        ;
4738: D1         POP     DE              ;
4739: C1         POP     BC              ;
473A: E1         POP     HL              ;
473B: EB         EX      DE,HL           ;
473C: 13         INC     DE              ;
473D: 3A 7E 47   LD      A,($477E)       ;
4740: A7         AND     A               ;
4741: C2 47 47   JP      NZ,$4747        ;
4744: 13         INC     DE              ;
4745: 13         INC     DE              ;
4746: 13         INC     DE              ;
4747: 3A 7B 47   LD      A,($477B)       ;
474A: 3D         DEC     A               ;
474B: 32 7B 47   LD      ($477B),A       ;
474E: C2 CC 46   JP      NZ,$46CC        ;
4751: E1         POP     HL              ;
4752: C9         RET                     ;
```

# Character Table

```code
; Character compression table
CharTable: 
4753: 3F 21 32 20 22 27 3C 3E 2F 30 33                 ; ?!2_"'<>/03
475E: 41 42 43 44 45 46 47 48 49 4A 4B 4C 4D 4E 4F 50  ; ABCDEFGHIJKLMNOP       
476E: 51 52 53 54 55 56 57 58 59 5A 2D 2C 2E           ; QRSTUVWXYZ-,.
 
477B: 00 ; RAM used by unpack 
477C: 00 ; RAM used by unpack
477D: 00 ; RAM used by unpack
477E: 00 ; RAM used by unpack
```
    
# Room Information

```code
RoomInformation: 
; First two: description
; Second two: room script
477F: 90 4C BF 47 ; 1 FORYER.
4783: 96 4C CC 47 ; 2 LIVING ROOM.
4787: A0 4C EC 47 ; 3 DINING ROOM.
478B: AA 4C F5 47 ; 4 KITCHEN.
478F: B2 4C 16 48 ; 5 BREAKFAST ROOM.
4793: BE 4C 1F 48 ; 6 SERVANTS QUARTERS.
4797: BE 4C 2F 48 ; 7 SERVANTS QUARTERS.
479B: CC 4C 3D 48 ; 8 DEN.
479F: D1 4C 46 48 ; 9 EAST END OF THE HALL.
47A3: E1 4C 53 48 ; 10 WEST END OF THE HALL.
47A7: F1 4C 74 48 ; 11 GREEN BEDROOM. THERE'S A PANEL ON THE WEST WALL.
47AB: 13 4D 7D 48 ; 12 SECRET PASSAGE.
47AF: 1F 4D 86 48 ; 13 BLUE BEDROOM. THERE'S A PANEL ON THE EAST WALL.
47B3: 41 4D 8F 48 ; 14 MASTER BEDROOM.
47B7: 4D 4D A3 48 ; 15 LIBRARY. THERE IS A HOLE IN THE CEILING.
47BB: 6B 4D B9 48 ; 16 OUTSIDE OF THE HOUSE.
```
     
# Room Scripts

```code
RoomScripts: 
; Commands 1 FORYER
; This room just has directional changes.
                  ; "Room_1"   : {
                  ;     "Description" : "YOU_ARE_AT_THE_FORYER.[CR]",
47BF: 02 03 01 02 ;     "E"    : ["GoToRoom(2)"],
47C3: 03 03 01 08 ;     "S"    : ["GoToRoom(8)"],
47C7: 04 03 01 09 ;     "W"    : ["GoToRoom(9)"]
47CB: 00          ; },
 
; Commands 2 LIVING ROOM
; You can safely go EAST or WEST. You can also issue a GET command. If you enter any other
; command and the KNIFE is in the room then you die. Note that you can't pick up the KNIFE
; unless you have the PAPER.
;
; This KNIFE behavior is part of the LIVING ROOM script. Anywhere else the KNIFE is just an
; ordinary, non-dangerous object.
;
                  ; "Room_2"   : {
                  ;     "Description" : "YOU_ARE_AT_THE_LIVING_ROOM.[CR]",
47CC: 02 03 01 03 ;     "E"    : ["GoToRoom(3)"],
47D0: 04 03 01 01 ;     "W"    : ["GoToRoom(1)"],
47D4: 06 0E 06 0B ;     "GET"  : ["SubscriptAbortAllIfPass", [                               
47D8: 0A 06       ;                   "AssertNounIs(KNIFE)",
47DA: 06 04       ;                   "SubscriptAbortAllIfPass", [           
47DC: 02 01       ;                       "AssertIsInPack(PAPER)",
47DE: 0E          ;                       "MoveNounToPack()"],
47DF: 04 B6 4F    ;                   "Print(THE_KNIFE_FLOATS_OUT_OF_YOUR_REACH.[CR])"],              
47E2: 0E          ;               "MoveNounToPack()"],
47E3: FF 07 10 06 ;     "*"    : ["AssertIsInRoom(KNIFE)",                       
47E7: 04 10 4F    ;               "Print(SUDDENLY_THE_KNIFE_WHOOSHES_DOWN_AND_SLITS_YOUR_THROAT!__YOU_AREDEAD.[CR])",           
47EA: 07          ;               "EndlessLoop()"]                  
47EB: 00          ; },
                     
; Commands 3 DINING ROOM
; This room just has directional changes.
;
                  ; "Room_3"   : {
                  ;     "Description" : "YOU_ARE_AT_THE_DINING_ROOM.[CR]",
47EC: 03 03 01 04 ;     "S"    : ["GoToRoom(4)"],  
47F0: 04 03 01 02 ;     "W"    : ["GoToRoom(2)"]
47F4: 00          ; },

; Commands 4 KITCHEN  
; The ARMOR is an invisible object in this room (it has no description). If you have the KNIFE in your pack then
; it runs off (out of game-play). If you don't have the knife and the ARMOR is in the room then it prevents you
; from going SOUTH.
;
                  ; "Room_4"   : {
                  ;     "Description" : "YOU_ARE_AT_THE_KITCHEN.[CR]",
47F5: 01 03 01 03 ;     "N"    : ["GoToRoom(3)"],             
47F9: 04 03 01 08 ;     "W"    : ["GoToRoom(8)"],
47FD: 03 17 06 13 ;     "S"    : ["SubscriptAbortAllIfPass", [           
4801: 10 08       ;                   "AssertObjectIsInRoom(object8)",
4803: 06 0B       ;                   "SubscriptAbortAllIfPass", [           
4805: 02 06       ;                       "AssertObjectIsInPack(KNIFE)",
4807: 0D 08 00    ;                       "MoveObjectToRoom(8,0)",                     
480A: 04 4E 4E    ;                       "Print(A_SUIT_OF_ARMOUR_HERE_FLEES_WHEN_IT_SPOTS_YOUR_KNIFE[CR])",          
480D: 01 05       ;                       "GoToRoom(5)"],
480F: 04 73 4E    ;                   "Print(YOUR_ARE_AT_THE_BREAKFAST_ROOM.__AN_ANIMATED_SUIT_OF_ARMOUR_____THROWS_YOU_OUT![CR])",      
4812: 05          ;                   "PrintRoomDescription()"],             
4813: 01 05       ;               "GoToRoom(5)"
4815: 00          ; },     

; Commands 5 BREAKFAST ROOM   
; This room just has directional changes.
;
                  ; "Room_5"   : {
                  ;     "Description" : "YOU_ARE_AT_THE_BREAKFAST_ROOM.[CR]",
4816: 01 03 01 04 ;     "N"    : ["GoToRoom(4)"],
481A: 02 03 01 06 ;     "E"    : ["GoToRoom(6)"],
481E: 00          ; },

; Commands 6 SERVANTS QUARTERS
; This room has the empty CABINET. If you open the CABINET you get the message.
;
                  ; "Room_6"   : {
                  ;     "Description" : "YOU_ARE_AT_THE_SERVANTS_QUARTERS.[CR]",
481F: 01 03 01 07 ;     "N"    : ["GoToRoom(7)"],
4823: 04 03 01 05 ;     "W"    : ["GoToRoom(5)"],
4827: 05 06 0A 09 ;     "OPEN" : ["AssertNounIs(CABINET)",
482B: 04 AA 4E    ;               "Print(IT'S_EMPTY.[CR])"]        
482E: 00          ; },

; Commands 7 SERVANTS QUARTERS  
; This room has the same description as Room_6 ... very sneaky. This room has the
; CABINET WITH KEY in it. Whenever you open this CABINET the KEY appears in the 
; room. If the key is already in your pack or dropped in some other room then it
; magically moves here.
;
                  ; "Room_7"   : {
                  ;     "Description" : "YOU_ARE_AT_THE_SERVANTS_QUARTERS.[CR]",                   
482F: 03 03 01 06 ;     "S"    : ["GoToRoom(6)"],
4833: 05 08 0A 0B ;     "OPEN" : ["AssertNounIs(CABINETKEY)",               
4837: 08 03       ;               "MoveObjectToCurrentRoom(KEY)",
4839: 04 FC 4E    ;               "Print(THERE_IS_A_KEY_IN_IT.[CR])"]
483C: 00          ; },

; Commands 8 DEN   
; This room just has directional changes.
;
                  ; "Room_8"   : {   
                  ;     "Description" : "YOU_ARE_AT_THE_DEN.[CR]",
483D: 01 03 01 01 ;     "N"    : ["GoToRoom(1)"], 
4841: 02 03 01 04 ;     "E"    : ["GoToRoom(4)"]
4845: 00          ; },

; Commands 9 EAST END OF THE HALL
; This room just has directional changes.
;
                  ; "Room_9"   : {   
                  ;     "Description" : "YOU_ARE_AT_THE_EAST_END_OF_THE_HALL.[CR]",
4846: 01 03 01 0B ;     "N"    : ["GoToRoom(11)"],           
484A: 02 03 01 01 ;     "E"    : ["GoToRoom(1)"], 
484E: 04 03 01 0A ;     "W"    : ["GoToRoom(10)"], 
4852: 00          ; },

; Commands 10 WEST END OF THE HALL      
; You can OPEN DOOR or go S to the LIBRARY -- but only if you have the KEY in the pack. Otherwise you
; get an error message.
;
                  ; "Room_10"  : {     
                  ;     "Description" : "YOU_ARE_AT_THE_WEST_END_OF_THE_HALL.[CR]",
4853: 01 03 01 0D ;     "N"    : ["GoToRoom(13)"],            
4857: 02 03 01 09 ;     "E"    : ["GoToRoom(9)"],
485B: 03 0A 06 05 ;     "S"    : ["SubscriptAbortAllIfPass", [        
485F: 02 03       ;                   "AssertObjectIsIPack(KEY)", 
4861: 01 0E       ;                   "GoToRoom(15)"],
4863: 04 B4 4E    ;               "Print(YOU'LL_NEED_A_KEY_TO_GET_THROUGH_THAT_DOOR.[CR])"],     
4866: 05 0C 0A 05 ;     "OPEN" : ["AssertInputNounIs(DOOR)",       
486A: 06 05       ;               "SubscriptAbortAllIfPass", [       
486C: 02 03       ;                   "AssertObjectIsInPack(KEY)",
486E: 01 0E       ;                   "GoToRoom(15)"],
4870: 04 B4 4E    ;               "Print(YOU'LL_NEED_A_KEY_TO_GET_THROUGH_THAT_DOOR.[CR])"]    
4873: 00          ; },

; Commands 11 GREEN BEDROOM. THERE'S A PANEL ON THE WEST WALL     
; This room just has directional changes. 
;
                  ; "Room_11"  : {  
                  ;     "Description" : "YOU_ARE_AT_THE_GREEN_BEDROOM._THERE'S_A_PANEL_ON_THE_WEST_WALL.[CR]",
4874: 03 03 01 09 ;     "S"    : ["GoToRoom(9)"],
4878: 0E 03 01 0C ;     "PANE" : ["GoToRoom(12)"]
487C: 00          ; },

; Commands 12 SECRET PASSAGE
; This room just has directional changes.
;
                  ; "Room_12"  : { 
                  ;     "Description" : "YOU_ARE_AT_THE_SECRET_PASSAGE.[CR]",
487D: 02 03 01 0B ;     "E"    : ["GoToRoom(11)"],
4881: 04 03 01 0D ;     "W"    : ["GoToRoom(13)"],
4885: 00          ; },

; Commands 13 BLUE BEDROOM. THERE'S A PANEL ON THE EAST WALL
                  ; "Room_13"  : { 
                  ;     "Description" : "YOU_ARE_AT_THE_BLUE_BEDROOM.__THERE'S_A_PANEL_ON_THE_WEST_WALL.[CR]",
4886: 03 03 01 0A ;     "S"    : ["GoToRoom(10)"],
488A: 0E 03 01 0C ;     "PANE" : ["GoToRoom(12)"]
488E: 00          ; },

; Commands 14 MASTER BEDROOM
; The YES command takes you east at any time (even if you haven't seen the "are you sure?"). The E command
; always prints a "are you sure?" message. The NO command prints "a wise decision", but it isn't really.
; Very sneaky game.
;
                     ; "Room_14"  : { 
                     ;     "Description" : "YOU_ARE_AT_THE_MASTER_BEDROOM.[CR]",
488F: 01 03 01 0A    ;     "N"    : ["GoToRoom(11)"],  
4893: 02 04 04 D3 4E ;     "E"    : ["Print(ARE_YOU_JUST_GOING_TO_WALK_RIGHT_THROUGH_THAT_RAGING_FIRE?[CR])"],  
4898: 12 04 0C       ;     "YES"  : ["PrintOK()",
489B: 01 0F          ;               "GoToRoom(15)"],
489D: 13 04 04 D0 4F ;     "NO"   : ["Print(A_WISE_DECISION.[CR])"]    
48A2: 00                           

; Commands 15 LIBRARY. THERE IS A HOLE IN THE CEILING
; If you DROP the ROPE in this room then the ROPE object goes out of game-play and the ROPE TO CEILING is
; moved to this room. If the ROPE TO CEILING is in this room then the CLIMB command loads the second floor
; from tape.
;
                     ; "Room_15"  : { 
                     ;     "Description" : "YOU_ARE_AT_THE_LIBRARY._THERE IS A HOLE IN THE CEILING.[CR]",
48A3: 04 03 01 0E    ;     "W"    : ["GoToRoom(13)"],
48A7: 07 0B 0A 07    ;     "DROP" : ["AssertInputNounIs(ROPE)",                
48AB: 0D 07 00       ;               "MoveObjectToRoom(ROPE,0)"                                    
48AE: 08 0C          ;               "MoveObjectToCurrentRoom(ROPECEILING)",               
48B0: 04 40 4F       ;               "Print(INSTANTLY_THE_ROPE_UNWINDS_AND_LEVITATES_TO_THE_HOLE_IN_THE_____CEILING![CR])"],         
48B3: 0F 04 10 0C    ;     "CLIM" : ["AssertObjectIsInRoom(ROPECEILING)",  
48B7: 11             ;               "LoadSecondFloorFromTape"]
48B8: 00             ; },

; Commands 16 OUTSIDE OF THE HOUSE
; There is a DOOR here, but you can't open it. You have to use the PLUGH command to "poof" inside the house.
; Be sure to pick up the PAPER here or you can't get the KNIFE later. The PAPER has a message you can
; READ, but that is handled by the general script (later).
;
                     ; "Room_16"  : { 
                     ;     "Description" : "YOU_ARE_AT_THE_OUTSIDE_OF_THE_HOUSE.[CR]",
48B9: 0A 06 04 23 4E ; "PLUG" : ["Print(YOU_MATERIALIZE_INSIDE_THE_DOOR.[CR])", 
48BE: 01 01          ;           "GoToRoom(1)"],
48C0: 05 06 0A 02    ; "OPEN" : ["AssertInputNounIs(DOOR)"
48C4: 04 3B 4E       ;           "Print(THE_DOOR_CAN'T_BE_OPENED.[CR])"]
48C7: 00             ; }      
```

# Object Info

```code
ObjectInfo: 
;
; The format of the two bytes are:
;
; MC------ RRRRRRRR
;
; M - if set, the second byte is an object number (container). if clear, the second byte 
;     is a room number (containment is not used in this game). Containment is not used
;     in this game. Maybe this is part of an earlier general purpose engine.
; C - if set, object can be picked up ("+" objects in the list below).
;
; RRRRRRRR - Second byte is the object's location (containing object or room number).
;
48C8: 40 10 ;  1 PAPER       +(OUTSIDE OF THE HOUSE)
48CA: 00 10 ;  2 DOOR         (OUTSIDE OF THE HOUSE)
48CC: 40 00 ;  3 KEY         +(Starts out of play)                
48CE: 00 0E ;  4 FIRE         ()
48D0: 00 0A ;  5 LOCKEDDOOR   ()           
48D2: 40 02 ;  6 KNIFE       +()        
48D4: 40 0C ;  7 ROPE        +()            
48D6: 00 04 ;  8 ARMOR        ()             
48D8: 00 06 ;  9 CABINET      ()
48DA: 40 04 ; 10 BUCKET      +()            
48DC: 00 07 ; 11 CABINETKEY   ()                      
48DE: 00 00 ; 12 ROPECEILING  ()                          
48E0: 40 02 ; 13 SCROLL      +()  
 
48E2: 10 ; Current room number (OUTSIDE OF THE HOUSE)
```

# Object Descriptions

```code 
ObjectDescriptions: 
; Object descriptions. Two strings: first is "in room" description. Second
; is a shorter "inventory" description.
48E3: 35 4B ;  1 PAPER            
48E5: 64 4B ;  2 DOOR       
48E7: 77 4B ;  3 KEY
48E9: 87 4B ;  4 FIRE
48EB: A5 4B ;  5 LOCKEDDOOR
48ED: BD 4B ;  6 KNIFE
48EF: E5 4B ;  7 ROPE
48F1: CB 47 ;  8 (no description for the suit of armor)            
48F3: F8 4B ;  9 CABINET
48F5: 0F 4C ; 10 BUCKET
48F7: F8 4B ; 11 CABINETKEY
48F9: 32 4C ; 12 ROPECEILING
48FB: 5F 4C ; 13 SCROLL
```

# Script Commands

```code
ScriptCommands: 
48FD: 1F 49 ;  1 GoToRoom(room)
48FF: 67 49 ;  2 AssertObjectIsInPack(object)
4901: 76 49 ;  3 AssertObjectIsInRoomOrPack(object)
4903: AF 49 ;  4 PrintMessage(message)
4905: 27 49 ;  5 PrintRoomDescription()
4907: 22 44 ;  6 SubscriptAbortAllIfPass[...]
4909: 48 4A ;  7 EndlessLoop()
490B: BC 49 ;  8 MoveObjectToCurrentRoom(object)
490D: CB 49 ;  9 PrintInventory()
490F: F5 49 ; 10 AssertInputNounIs(object)
4911: 03 4A ; 11 GetObjectFromRoom(object)
4913: 2A 4A ; 12 PrintOK()
4915: 33 4A ; 13 MoveObjectToRoom(object,room)     
4917: 9A 49 ; 14 GetNounToPack()
4919: 23 4A ; 15 DropNounToRoom()
491B: 89 49 ; 16 AssertObjectIsInRoom(object)
491D: F5 42 ; 17 LoadSecondFloorFromTape()
```

# Script Command 01

```code
ScriptCommand01: 
; GoToRoom(room)
491F: E1         POP     HL              ; Pointer to script  
4920: 46         LD      B,(HL)          ; Get the room number from the script          
4921: 23         INC     HL              ; Next byte in script
4922: E5         PUSH    HL              ; New pointer into script
4923: 78         LD      A,B             ; Room number to A
4924: 32 E2 48   LD      ($48E2),A       ; Change rooms
```

# Script Command 05

```code
ScriptCommand05: 
; PrintRoomDescription()
4927: CD 2D 49   CALL    $492D           ; Print the room description
492A: C3 0B 44   JP      $440B           ; ScriptCommandPASS
```

# DescribeRoom

```code
DescribeRoom: 
; DescribeCurrentRoom()
492D: 21 84 4C   LD      HL,$4C84        ; "YOU ARE AT THE " message
4930: CD AE 45   CALL    $45AE           ; Print the message
4933: 3A E2 48   LD      A,($48E2)       ; Room number
4936: 21 7F 47   LD      HL,$477F        ; Room descriptions
4939: CD C6 43   CALL    $43C6           ; 4-byte offset
493C: 7E         LD      A,(HL)          ; Get ...
493D: 23         INC     HL              ; ... LSB ...
493E: 66         LD      H,(HL)          ; ... and ...
493F: 6F         LD      L,A             ; ... MSB
4940: CD AE 45   CALL    $45AE           ; Print the description
4943: 06 00      LD      B,$00           ; B runs the object numbers
4945: 04         INC     B               ; Next object (1 on first pass)
4946: 3A E2 48   LD      A,($48E2)       ; Room number
4949: 5F         LD      E,A             ; To E for find
494A: 78         LD      A,B             ; Object number for find
494B: FE 0E      CP      $0E             ; All objects (1 through 13) checked?
494D: D0         RET     NC              ; Yes ... done here
494E: CD AB 43   CALL    $43AB           ; Get object if in this room
4951: C2 45 49   JP      NZ,$4945        ; Object is not in room ... skip it
4954: 78         LD      A,B             ; Object number
4955: 21 E3 48   LD      HL,$48E3        ; Object descriptions
4958: CD BC 43   CALL    $43BC           ; 2-byte offset
495B: 7E         LD      A,(HL)          ; Get ...
495C: 23         INC     HL              ; ... LSB ...
495D: 66         LD      H,(HL)          ; ... and ...
495E: 6F         LD      L,A             ; ... MSB
495F: C5         PUSH    BC              ; Hang on to object number
4960: CD AE 45   CALL    $45AE           ; Print description
4963: C1         POP     BC              ; Restore object number
4964: C3 45 49   JP      $4945           ; Keep checking objects
```

# Script Command 02

```code
ScriptCommand02: 
; AssertObjectInPack(object)
4967: E1         POP     HL              ; Script pointer
4968: 7E         LD      A,(HL)          ; Get object number
4969: 23         INC     HL              ; New script ...
496A: E5         PUSH    HL              ; ... pointer
496B: 1E FF      LD      E,$FF           ; Backpack value
496D: CD AB 43   CALL    $43AB           ; Get object info
4970: CA 0B 44   JP      Z,$440B         ; ScriptCommandPASS
4973: C3 1E 44   JP      $441E           ; ScriptCommandFAIL
```

# Script Command 03

```code
ScriptCommand03: 
; AssertObjectIsInRoomOrPack(object) 
4976: E1         POP     HL              ; Script pointer
4977: 46         LD      B,(HL)          ; Get object number
4978: 23         INC     HL              ; New script ...
4979: E5         PUSH    HL              ; ... pointer
497A: 3A E2 48   LD      A,($48E2)       ; Current room ...
497D: 5F         LD      E,A             ; ... to E for find
497E: 78         LD      A,B             ; Object number for find
497F: CD AB 43   CALL    $43AB           ; Look for the object in current room
4982: CA 0B 44   JP      Z,$440B         ; Found it ... ScriptCommandPASS
4985: 78         LD      A,B             ; Object number again
4986: C3 6B 49   JP      $496B           ; Continue checking the pack
```

# Script Command 16

```code
ScriptCommand16: 
; AssertObjectIsInRoom(object)
4989: E1         POP     HL              ; Script pointer
498A: 3A E2 48   LD      A,($48E2)       ; Room number ...
498D: 5F         LD      E,A             ; ... to E for find
498E: 7E         LD      A,(HL)          ; Get object number
498F: 23         INC     HL              ; New script ...
4990: E5         PUSH    HL              ; ... pointer
4991: CD AB 43   CALL    $43AB           ; Find the object
4994: CA 0B 44   JP      Z,$440B         ; Found it in room ... ScriptCommandPASS
4997: C3 1E 44   JP      $441E           ; ScriptCommandFAIL
```

# Script Command 14

```code
ScriptCommand14: 
; GetNounToPack()
499A: 3A 7B 46   LD      A,($467B)       ; Input Noun
499D: 1E FF      LD      E,$FF           ; Is object already ...
499F: CD AB 43   CALL    $43AB           ; ... in backpack?
49A2: C2 A8 49   JP      NZ,$49A8        ; No ... do the get
49A5: C3 2A 4A   JP      $4A2A           ; Print OK and PASS
;
49A8: 3A 7B 46   LD      A,($467B)       ; User input ...
49AB: 47         LD      B,A             ; ... noun
49AC: C3 08 4A   JP      $4A08           ; Get object from room
```

# Script Command 04

```code
ScriptCommand04: 
; PrintMessage(message)
49AF: E1         POP     HL              ; Get script pointer
49B0: 5E         LD      E,(HL)          ; Get ...
49B1: 23         INC     HL              ; ... message pointer ...
49B2: 56         LD      D,(HL)          ; ... from ...
49B3: 23         INC     HL              ; ... script
49B4: E5         PUSH    HL              ; New script pointer
49B5: EB         EX      DE,HL           ; Message pointer to HL
49B6: CD AE 45   CALL    $45AE           ; Unpack and print
49B9: C3 0B 44   JP      $440B           ; ScriptCommandPASS
```

# Script Command 08

```code
ScriptCommand08: 
; MoveObjectToCurrentRoom(object)
49BC: E1         POP     HL              ; Get script pointer
49BD: 46         LD      B,(HL)          ; Get the object number
49BE: 23         INC     HL              ; New script ...
49BF: E5         PUSH    HL              ; ... pointer
;
49C0: 3A E2 48   LD      A,($48E2)       ; Current Room number
49C3: 5F         LD      E,A             ; To E
49C4: 78         LD      A,B             ; Object number to A
49C5: CD D1 43   CALL    $43D1           ; Move object
49C8: C3 2A 4A   JP      $4A2A           ; Print OK and PASS
```

# Script Command 09

```code
ScriptCommand09: 
; PrintInventory()
49CB: 06 00      LD      B,$00           ; B runs the object numbers
49CD: 1E FF      LD      E,$FF           ; Location = backpack
49CF: 04         INC     B               ; Next object (1 on first pass)
49D0: 78         LD      A,B             ; Have we ...
49D1: FE 0E      CP      $0E             ; ... done all objects (1 - 13) ?
49D3: D2 0B 44   JP      NC,$440B        ; Yes ... ScriptCommandPASS
49D6: CD AB 43   CALL    $43AB           ; Find the object
49D9: C2 CD 49   JP      NZ,$49CD        ; Not in the pack ... skip it
49DC: 78         LD      A,B             ; Object number
49DD: 21 E3 48   LD      HL,$48E3        ; Object descriptions
49E0: CD BC 43   CALL    $43BC           ; 2-byte offset
49E3: 7E         LD      A,(HL)          ; Get ...
49E4: 23         INC     HL              ; ... LSB ...
49E5: 66         LD      H,(HL)          ; ... and ...
49E6: 6F         LD      L,A             ; ... MSB
49E7: 7E         LD      A,(HL)          ; Skip ...
49E8: 23         INC     HL              ; ... to ...
49E9: A7         AND     A               ; ... short ...
49EA: C2 E7 49   JP      NZ,$49E7        ; ... description
49ED: C5         PUSH    BC              ; Hold object number
49EE: CD AE 45   CALL    $45AE           ; Print the description
49F1: C1         POP     BC              ; Restore object number
49F2: C3 CD 49   JP      $49CD           ; Keep going
```

# Script Command 10

```code
ScriptCommand10: 
; AssertInputNounIs(object)
49F5: E1         POP     HL              ; Script pointer
49F6: 46         LD      B,(HL)          ; Get object number
49F7: 23         INC     HL              ; New ...
49F8: E5         PUSH    HL              ; ... script pointer
49F9: 3A 7B 46   LD      A,($467B)       ; Input noun
49FC: B8         CP      B               ; Are they the same
49FD: C2 1E 44   JP      NZ,$441E        ; No ... ScriptCommandFAIL
4A00: C3 0B 44   JP      $440B           ; Yes ... ScriptCommandPASS
```

# Script Command 11

```code
ScriptCommand11: 
; GetObjectFromRoom(object)
4A03: E1         POP     HL              ; Script pointer
4A04: 46         LD      B,(HL)          ; Get object
4A05: 23         INC     HL              ; New ...
4A06: E5         PUSH    HL              ; ... script pointer
4A07: 78         LD      A,B             ; Object number to A for the find
;
4A08: CD AB 43   CALL    $43AB           ; Find the object
4A0B: 7E         LD      A,(HL)          ; Get the flags
4A0C: E6 40      AND     $40             ; Can the user pick it up?
4A0E: C2 1A 4A   JP      NZ,$4A1A        ; Yes ... move to pack
4A11: 21 85 4D   LD      HL,$4D85        ; "DON'T BE RIDICULOUS"
4A14: CD AE 45   CALL    $45AE           ; Print error message
4A17: C3 0B 44   JP      $440B           ; ScriptCommandPASS (was handled here)
;
4A1A: 78         LD      A,B             ; Object number
4A1B: 1E FF      LD      E,$FF           ; Location is backpack
4A1D: CD D1 43   CALL    $43D1           ; Move the object
4A20: C3 2A 4A   JP      $4A2A           ; Print OK and PASS
```

# Script Command 15

```code
ScriptCommand15: 
; DropNounToCurrentRoom()
4A23: 3A 7B 46   LD      A,($467B)       ; User input
4A26: 47         LD      B,A             ; To B
4A27: C3 C0 49   JP      $49C0           ; Drop the object in the current room
```

# Script Command 12

```code
ScriptCommand12: 
; PrintOK
4A2A: 21 7B 4D   LD      HL,$4D7B        ; "OK"
4A2D: CD AE 45   CALL    $45AE           ; Print OK
4A30: C3 0B 44   JP      $440B           ; ScriptCommandPASS
```

# Script Command 13

```code
ScriptCommand13: 
; MoveObjectToRoom(object,room)
4A33: E1         POP     HL              ; Script pointer
4A34: 7E         LD      A,(HL)          ; Get object
4A35: 23         INC     HL              ; Next
4A36: 5E         LD      E,(HL)          ; Get room number
4A37: 23         INC     HL              ; New ...
4A38: E5         PUSH    HL              ; ... object pointer
4A39: 21 C8 48   LD      HL,$48C8        ; Object descriptor
4A3C: CD BC 43   CALL    $43BC           ; 2 byte offset
4A3F: 7E         LD      A,(HL)          ; Clear the ...
4A40: E6 7F      AND     $7F             ; ... contained-by ...
4A42: 77         LD      (HL),A          ; ... flag
4A43: 23         INC     HL              ; Next
4A44: 73         LD      (HL),E          ; Set the room number
4A45: C3 0B 44   JP      $440B           ; ScriptCommandPASS
```

# Script Command 07

```code        
ScriptCommand07: 
; EndlessLoop()
4A48: C3 48 4A   JP      $4A48           ; Infinite loop
```

# Command Table

```code
CommandTable:             
; aa_bbb_ccc
; aa is grammar type:
;   00 This word is a noun
;   01 This verb requires a noun in the pack (POUR WATER)
;   10 This verb requires a noun in the room or pack (OPEN DOOR)
;   11 This verb requires nothing more
; bbb = number of data bytes       
; ccc = word text size
;                              FIRST FLOOR WORDS
4A4B: 0B 4B 45 59 03         ; 00_001_011  KEY   03            
4A50: 0C 50 41 50 45 01      ; 00_001_100  PAPE  01 
4A56: 14 44 4F 4F 52 02 05   ; 00_010_100  DOOR  02 05 ; Noun for object 2 and 5               
4A5D: 0C 46 49 52 45 04      ; 00_001_100  FIRE  04              
4A63: 0C 4B 4E 49 46 06      ; 00_001_100  KNIF  06
4A69: 14 52 4F 50 45 07 0C   ; 00_010_100  ROPE  07 0C ; For 7 and C                
4A70: 0C 41 52 4D 4F 08      ; 00_001_100  ARMO  08          
4A76: 14 43 41 42 49 09 0B   ; 00_010_100  CABI  09 0B ; For 9 and B               
4A7D: 0C 57 41 54 45 0A      ; 00_001_100  WATE  0A         
4A83: 0C 42 55 43 4B 0A      ; 00_001_100  BUCK  0A          
4A89: 0C 53 43 52 4F 0D      ; 00_001_100  SCRO  0D
;               
4A8F: C9 4E 01               ; 11_001_001  N     01
4A92: C9 45 02               ; 11_001_001  E     02         
4A95: C9 53 03               ; 11_001_001  S     03             
4A98: C9 57 04               ; 11_001_001  W     04              
4A9B: CC 43 4C 49 4D 0F      ; 11_001_100  CLIM  0F                    
4AA1: CC 51 55 49 54 0B      ; 11_001_100  QUIT  0B          
4AA7: CC 49 4E 56 45 0C      ; 11_001_100  INVE  0C              
4AAD: CC 4C 4F 4F 4B 0D      ; 11_001_100  LOOK  0D              
4AB3: 4C 44 52 4F 50 07      ; 01_001_100  DROP  07                   
4AB9: 4C 50 4F 55 52 08      ; 01_001_100  POUR  08        
4ABF: 8B 47 45 54 06         ; 10_001_011  GET   06
4AC4: 8C 4F 50 45 4E 05      ; 10_001_100  OPEN  05              
4ACA: 4C 44 52 49 4E 10      ; 01_001_100  DRIN  10
4AD0: 8C 53 4D 41 53 11      ; 10_001_100  SMAS  11
4AD6: CB 59 45 53 12         ; 11_001_011  YES   12       
4ADB: CA 4E 4F 13            ; 11_001_010  NO    13           
4ADF: 4C 52 45 41 44 09      ; 01_001_100  READ  09        
4AE5: CC 50 41 4E 45 0E      ; 11_001_100  PANE  0E
4AEB: CC 50 4C 55 47 0A      ; 11_001_100  PLUG  0A         
4AF1: 00                     ; end of list
```

# General Script

```code 
GeneralScript:                     
; When you enter a command, the game tries your input against the script of the current room.
; If that script fails then this general script runs to handle common things like GET and DROP
; along with some other things:
;  - Unhandled directions simply reprint the room description
;  - GET, DROP, LOOK, QUIT, and INVENTORY do what you would expect (unless the room
;    script has already handled these words).
;  - POUR, SMASH, and PLUGH print messages.
;  - You can READ the PAPER or SCROLL if they are present (in your pack or in the room).
;  - DRINK the water and you die.
;                    ; {
4AF2: 01 02 05       ;  "N"    : ["PrintRoomDescription()"],
4AF5: 02 02 05       ;  "E"    : ["PrintRoomDescription()"],                
4AF8: 03 02 05       ;  "S"    : ["PrintRoomDescription()"],              
4AFB: 04 02 05       ;  "W"    : ["PrintRoomDescription()"],                   
4AFE: 06 02 0E       ;  "GET"  : ["GetNounToPack()"],
4B01: 07 02 0F       ;  "DROP" : ["DropNounToRoom()"],                    
4B04: 0D 02 05       ;  "LOOK" : ["PrintRoomDescription()"],         
4B07: 0B 02 07       ;  "QUIT" : ["EndlessLoop()"],             
4B0A: 0C 02 09       ;  "INVE" : ["PrintInventory()"],  
4B0D: 08 06 0A 0A    ;  "POUR" : ["AssertInputNounIs(BUCKET)",  
4B11: 04 95 4D       ;            "Print(THE_GROUND_IS_WET.__THE_BUCKET_MAGICALLY_REFILLS![CR])"],                 
4B14: 09 06 0A 01    ;  "READ" : ["AssertInputNounIs(PAPER)", 
4B18: 04 B8 4D       ;            "Print(IT_SAYS,_"MAGIC_WORD_-_PLUGH."[CR])"],                 
4B1B: 09 06 0A 0D    ;  "READ" : ["AssertInputNounIs(SCROLL)",                  
4B1F: 04 DD 4F       ;            "Print(IT_SAYS,_"THERE_IS_ESCAPE_FROM_THE_SECOND_FLOOR!"[CR])"],          
4B22: 10 07 0A 0A    ;  "DRIN" : ["AssertInputNounIs(BUCKET)",                
4B26: 04 CE 4D       ;            "Print(YOU_FEEL_SICK.__IN_FACT,_YOU_JUST_DIED.__IT_WAS_POSION![CR])",          
4B29: 07             ;            "EndlessLoop()"],                
4B2A: 11 04 04 F5 4D ;  "SMAS" : ["OUCH!__YOU_HURT_YOUR_HAND.[CR]"],                  
4B2F: 0A 04 04 09 4E ;  "PLUG" : ["Print(SORRY,_ONLY_ONE_PLUGH_PER_CUSTOMER.[CR])"]               
4B34: 00             ; }            
```

# Compressed Text

```code
CompressedText: 

; How much was saved? There are 04CB bytes from here down. The compression isn't perfect. There are uncompressed
; characters and terminators. But ideally you could get 04CB/2*3 = 72F characters. That would be an additional 
; 612 bytes. The "uncompressor" is 154 bytes. That's a pretty good tradeoff.

; THERE_IS_A_CRUMPLED_PIECE_OF_PAPER_ON_THE_GROUND.[CR]
4B35: 10 5F BE 5B B1 4B 7B 45 45 EF B3 FF A5 12 58 25 
4B45: 79 51 5E 92 64 DF 48 91 AF 96 96 DB 72 B9 6E 8E 
4B55: C5 2E 00 

; CRUMPLED_PAPER[CR]
4B58: 04 BF 55 E6 93 F3 5F 52 A4 45 52 00 

; THE_FRONT_DOOR_IS_CLOSED.[CR]
4B64: 08 5F BE 5C 15 1E A0 09 15 A3 A0 4B 7B C9 54 A6 
4B74: B7 2E 00 

; A_KEY_IS_HERE.[CR]
4B77: 04 4D 45 3B 63 4B 7B F4 72 45 2E 00 

; KEY[CR]
4B83: 01 BB 85 00 

; A_WALL_OF_RAGING_FIRE_BLOCKS_THE_WAY_EAST.[CR]
4B87: 0E 59 45 46 48 B8 16 2B 17 50 6D C8 6A 2F 7B B6 
4B97: 14 5D 9E D6 B5 DB 72 1B D0 23 15 17 BA 00 

; A_LOCKED_DOOR_BARS_THE_WAY_SOUTH.[CR]
4BA5: 0B 4E 45 5D 9E F3 5F 81 5B 84 AF 3D 49 82 17 59 
4BB5: 5E 3B 4A 47 B9 77 BE 00 

; A_KNIFE_IS_LEVITATING_IN_THE_MIDDLE_OF_THE_ROOM.[CR]
4BBD: 10 4D 45 08 99 4B 5E CE B5 D3 62 56 BD 91 7A D0 
4BCD: 15 82 17 4F 5E FE 78 DB 8B C3 9E 5F BE 39 17 FF 
4BDD: 9F 00 

; KNIFE[CR]
4BDF: 01 13 87 46 45 00 

; A_ROPE_IS_NEARBY.[CR]
4BE5: 05 54 45 5F A0 D5 15 8F 16 2C 49 59 2E 00 

; ROPE[CR]
4BF3: 01 02 B3 45 00 

; THERE_IS_A_CABINET_ON_ONE_WALL.[CR]
4BF8: 0A 5F BE 5B B1 4B 7B 45 45 B3 46 76 98 C0 16 C0 
4C08: 16 59 5E 46 48 2E 00 

; A_BUCKET_OF_WATER_IS_ON_THE_FLOOR.[CR]
4C0F: 0B 44 45 DD C3 73 62 C3 9E 16 D0 23 62 4B 7B 03 
4C1F: A0 5F BE 56 15 44 A0 2E 00 

; WATER_BUCKET[CR]
4C28: 04 16 D0 23 62 E5 4F B6 85 00 

; A_ROPE_IS_STRETCHING_FROM_THE_GROUND_TO_THE_HOLE_IN_THE_CEILING.[CR]
4C32: 15 54 45 5F A0 D5 15 66 17 76 B1 23 54 AB 98 79 
4C42: 68 56 90 DB 72 B9 6E 8E C5 89 17 82 17 4A 5E BF 
4C52: 9F D0 15 82 17 45 5E CE 60 91 7A 2E 00 

; THERE_IS_A_MYSTERIOUS_SCROLL_ON_THE_GROUND.[CR]
4C5F: 0E 5F BE 5B B1 4B 7B 4F 45 66 DF 33 62 35 A1 55 
4C6F: 17 FE B2 11 8A 96 96 DB 72 B9 6E 8E C5 2E 00 

; SCROLL[CR]
4C7E: 02 64 B7 C6 9F 00 

; YOU_ARE_AT_THE_
4C84: 05 C7 DE 94 14 43 5E 16 BC DB 72 01 

; FOYER.[CR]
4C90: 02 0B 68 47 62 00 

; LIVING_ROOM.[CR]
4C96: 04 98 8C 91 7A 39 17 FF 9F 00 

; DINING_ROOM.[CR]
4CA0: 04 90 5A 91 7A 39 17 FF 9F 00 

; KITCHEN.[CR]
4CAA: 02 56 86 1F 54 4E 2E 00 

; BREAKFAST_ROOM.[CR]
4CB2: 05 6F 4F 18 48 66 49 39 17 FF 9F 00 

; SERVANTS_QUARTERS.[CR]
4CBE: 06 B4 B7 D0 C9 0B C0 A3 AD BF B3 AF B3 00 

; DEN.[CR]
4CCC: 01 F0 59 2E 00 

; EAST_END_OF_THE_HALL.[CR]
4CD1: 07 95 5F 07 BC 33 98 C3 9E 5F BE 9B 15 17 8D 00 

; WEST_END_OF_THE_HALL.[CR]
4CE1: 07 B5 D0 07 BC 33 98 C3 9E 5F BE 9B 15 17 8D 00 

; GREEN_BEDROOM._THERE'S_A_PANEL_ON_THE_WEST_WALL.[CR]
4CF1: 10 AF 6E 83 61 66 4D 01 B3 DB 95 5F BE 5D B1 C3 
4D01: B5 DB 16 6E 98 C0 16 82 17 59 5E 66 62 F3 17 17 
4D11: 8D 00 

; SECRET_PASSAGE.[CR]
4D13: 05 A5 B7 76 B1 DB 16 D3 B9 BF 6C 00 

; BLUE_BEDROOM.__THERE'S_A_PANEL_ON_THE_EAST_WALL.[CR]
4D1F: 10 8F 4E 44 5E 0C 60 3F A0 3B F4 5F BE 5D B1 C3 
4D2F: B5 DB 16 6E 98 C0 16 82 17 47 5E 66 49 F3 17 17 
4D3F: 8D 00 

; MASTER_BEDROOM.[CR]
4D41: 05 95 91 F4 BD AF 14 F9 5B FF 9F 00 

; LIBRARY.__THERE_IS_A_HOLE_IN_THE_CEILING.[CR]
4D4D: 0D 84 8C D4 B0 DB E0 82 17 2F 62 D5 15 7B 14 7E 
4D5D: 74 4B 5E 96 96 DB 72 AB 53 90 8C 47 2E 00 

; OUTSIDE_OF_THE_HOUSE.[CR]
4D6B: 07 36 A1 46 B8 51 5E 96 64 DB 72 87 74 BF B7 00 



; OK_[CR]
4D7B: 01 8B 9F 00 

; WHAT?[CR]
4D7F: 01 1B D1 54 3F 00 

; DON'T_BE_RIDICULOUS![CR]
4D85: 06 80 5B F3 23 5B 4D 06 B2 E7 78 87 8D 53 21 00 

; THE_GROUND_IS_WET.__THE_BUCKET_MAGICALLY_REFILLS![CR]
4D95: 10 5F BE 84 15 30 A1 0B 58 D9 B5 97 62 56 13 DB 
4DA5: 72 E5 4F B6 85 63 16 45 6D 46 48 54 DB 53 60 0D 
4DB5: 8D 21 00 

; IT_SAYS,_"MAGIC_WORD_-_PLUGH."[CR]
4DB8: 0A 73 7B 1B B7 33 BB A3 1C 45 6D 01 18 33 B1 D2 
4DC8: E7 69 8E 9C 76 00 

; YOU_FEEL_SICK.__IN_FACT,_YOU_JUST_DIED.__IT_WAS_POSION![CR]
4DCE: 12 C7 DE 4F 15 33 61 45 B8 5B 89 D0 15 4B 15 16 
4DDE: 56 51 18 4C C2 66 C6 03 15 17 60 4B 13 19 BC 4B 
4DEE: 49 85 A6 C0 7A 21 00 

; OUCH!__YOU_HURT_YOUR_HAND.[CR]
4DF5: 08 25 A1 AB 70 51 18 4A C2 3E C6 51 18 23 C6 50 
4E05: 72 44 2E 00 

; SORRY,_ONLY_ONE_PLUGH_PER_CUSTOMER.[CR]
4E09: 0B 44 B9 9E B4 C0 16 FB 8E 0F A0 E6 16 7A C4 DF 
4E19: 16 85 AF 66 C6 E7 9F 52 2E 00 

; YOU_MATERIALIZE_INSIDE_THE_DOOR.[CR]
4E23: 0A C7 DE 63 16 F4 BD 8E 78 6F 7C D0 15 46 B8 56 
4E33: 5E DB 72 81 5B 52 2E 00 

; THE_DOOR_CAN'T_BE_OPENED.[CR]
4E3B: 08 5F BE 09 15 A3 A0 10 53 F3 23 5B 4D 5F A0 66 
4E4B: 98 2E 00 

; A_SUIT_OF_ARMOUR_HERE_FLEES_WHEN_IT_SPOTS_YOUR_KNIFE[CR]
4E4E: 11 55 45 D6 C4 B8 16 94 14 C7 93 8A AF 2F 62 56 
4E5E: 15 35 60 FA 17 83 61 73 7B 69 B9 0B C0 C7 DE 8D 
4E6E: AF 08 99 45 00 

; YOUR_ARE_AT_THE_BREAKFAST_ROOM.__AN_ANIMATED_SUIT_OF_ARMOUR_____THROWS_YOU_OUT![CR]
4E73: 1A C7 DE 83 AF 5B B1 73 49 5F BE BC 14 8D 5F D5 
4E83: 65 14 BC 3F A0 3B F4 83 48 93 48 96 91 F3 5F 2B 
4E93: BA 11 BC 83 64 B1 B2 23 C6 3B 13 82 17 09 B3 DB 
4EA3: B5 1B A1 36 A1 21 00 

; IT'S_EMPTY.[CR]
4EAA: 03 75 7B C7 B5 EE 93 59 2E 00 

; YOU'LL_NEED_A_KEY_TO_GET_THROUGH_THAT_DOOR.[CR]
4EB4: 0E C7 DE C6 22 8F 16 F3 5F 4D 45 3B 63 6B BF B6 
4EC4: 6C 82 17 07 B3 13 6D 5B BE 06 BC 44 A0 2E 00 

; ARE_YOU_JUST_GOING_TO_WALK_RIGHT_THROUGH_THAT_RAGING_FIRE?[CR]
4ED3: 13 2F 49 51 18 4C C2 66 C6 81 15 91 7A 89 17 F3 
4EE3: 17 CB 8C 09 B2 33 75 6C BE 29 A1 16 71 56 72 2B 
4EF3: 17 50 6D C8 6A 2F 7B 3F 00 

; THERE_IS_A_KEY_IN_IT.[CR]
4EFC: 07 5F BE 5B B1 4B 7B 4D 45 3B 63 83 7A 97 7B 00 

; NO.[CR]
4F0C: 01 0F 9A 00 

; SUDDENLY_THE_KNIFE_WHOOSHES_DOWN_AND_SLITS_YOUR_THROAT!__YOU_AREDEAD.[CR]
4F10: 17 26 BA F0 59 FB 8E 5F BE 20 16 4F 79 FA 17 45 
4F20: A0 F5 72 09 15 03 D2 8E 48 5E 17 8D 7B 51 18 23 
4F30: C6 6C BE 16 9E BB 06 C7 DE 94 14 FF 5F 17 47 00 

; INSTANTLY_THE_ROPE_UNWINDS_AND_LEVITATES_TO_THE_HOLE_IN_THE_____CEILING![CR]
4F40: 18 9D 7A 50 BD 13 BF 82 17 54 5E 5F A0 B0 17 50 
4F50: D1 0B 5C 8E 48 3F 16 16 CB 7F 49 D6 B5 D6 9C DB 
4F60: 72 7E 74 4B 5E 96 96 DB 72 3B 13 D7 14 43 7A A9 
4F70: 98 00 

; YOU_AREN'T_CARRYING_IT.[CR]
4F72: 07 C7 DE 94 14 85 61 05 BC 3C 49 D0 DD CB 6A 54 
4F82: 2E 00 

; THERE'S_NOT_ONE_HERE.[CR]
4F84: 07 5F BE 5D B1 D0 B5 F3 A0 0F A0 9F 15 7F B1 00 

; WHAT_SHOULD_I_DO_WITH_IT?[CR]
4F94: 08 1B D1 15 BC 87 74 B3 8B 46 77 D9 9C 82 7B D6 
4FA4: 15 3F 00 

; I_DON'T_UNDERSTAND.[CR]
4FA7: 06 46 77 05 A0 17 BC 3F 98 A6 B3 8E 48 2E 00 

; THE_KNIFE_FLOATS_OUT_OF_YOUR_REACH.[CR]
4FB6: 0B 5F BE 20 16 4F 79 56 15 16 9E D1 B5 73 C6 C3 
4FC6: 9E C7 DE 94 AF 85 5F 48 2E 00 

; A_WISE_DECISION.[CR]
4FD0: 05 59 45 57 7B FF 14 55 54 C0 7A 2E 00 

; IT_SAYS,_"THERE_IS_ESCAPE_FROM_THE_SECOND_FLOOR!"[CR]
4FDD: 10 73 7B 1B B7 33 BB C2 1D 2F 62 D5 15 35 15 12 
4FED: 53 48 5E FF B2 82 17 55 5E E1 5F 33 98 89 67 A1 
4FFD: A0 22 00 
```