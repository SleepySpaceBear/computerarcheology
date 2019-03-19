![Haunted House 2nd Floor](HauntedHouse.jpg)

# Haunted House Second Floor

>>> cpu Z80

>>> memoryTable ram 
[RAM Usage](RAMUse2.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

# Start

```code
Start: 
; The code executes here after loading from tape.

435E: 31 B9 46   LD      SP,$46B9        ; Small stack space
4361: 3E 0E      LD      A,$0E           ; ??? Clear ...
4363: CD 33 00   CALL    $0033           ; ... the screen
4366: 3E 01      LD      A,$01           ; Starting room is ...
4368: 32 2F 49   LD      ($492F),A       ; ... 1 (???)
436B: 21 69 4E   LD      HL,$4E69        ; YOU_DROP_EVERYTHING_YOU_HAD_TO_CLIMB_THE_ROPE.__YOU_REACH_THE___SECOND_FLOOR.[CR]
436E: CD B3 45   CALL    $45B3           ; Print message
4371: CD 7C 49   CALL    $497C           ; Print room description
;
4374: 97         SUB     A,A             ; Make a zero
4375: 32 80 46   LD      ($4680),A       ; Clear noun
4378: 32 81 46   LD      ($4681),A       ; Clear verb
437B: 32 82 46   LD      ($4682),A       ; Clear grammar
437E: CD 2F 44   CALL    $442F           ; ParseUserInput
4381: 3A 2F 49   LD      A,($492F)       ; Current room
4384: 21 82 47   LD      HL,$4782        ; Room descriptors
4387: CD C6 43   CALL    $43C6           ; Get 4 bytes for room
438A: 23         INC     HL              ; Skip over ...
438B: 23         INC     HL              ; ... to room's script pointer
438C: 7E         LD      A,(HL)          ; Script ...
438D: 23         INC     HL              ; ... pointer ...
438E: 66         LD      H,(HL)          ; ... to ...
438F: 6F         LD      L,A             ; ... HL
4390: CD D8 43   CALL    $43D8           ; Process the room script
4393: C2 A5 43   JP      NZ,$43A5        ; ZF clear ... script was successful. Move on.
4396: 21 1A 4B   LD      HL,$4B1A        ; General script
4399: CD D8 43   CALL    $43D8           ; Process the script
439C: C2 A5 43   JP      NZ,$43A5        ; ZF clear ... script was successful. Move on
439F: 21 F0 4D   LD      HL,$4DF0        ; "NO"
43A2: CD B3 45   CALL    $45B3           ; Print packed error message
;
; This is a RET statement. The PYRAMID code uses this to process after-every-command things.
; This wasted call was removed from the first floor code ... maybe as part of a byte-squeeze
; effort.
43A5: CD 6D 49   CALL    $496D           ; Do nothing (after every command)
;
43A8: C3 74 43   JP      $4374           ; Back to top of input loop
```

# Get Object Info

```code
GetObjectInfo:  
; Return ZF set if found in desired location
; Return HL points to object location structure
43AB: 21 15 49   LD      HL,$4915        ; Object location table
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
43E0: 3A 81 46   LD      A,($4681)       ; Verb word
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
RunScriptCommand: 
43FD: 7E         LD      A,(HL)          ; Get the script command
43FE: 23         INC     HL              ; Point to first parameter
43FF: E5         PUSH    HL              ; Current script location
4400: 21 4D 49   LD      HL,$494D        ; Jump table of commands; Jump table of commands
4403: CD BC 43   CALL    $43BC           ; Offset A-1 into commands table
4406: 7E         LD      A,(HL)          ; Get LSB
4407: 23         INC     HL              ; Point to MSB
4408: 66         LD      H,(HL)          ; Get MSB
4409: 6F         LD      L,A             ; LSB to HL
440A: E9         JP      (HL)            ; Jump to the command

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
442E: C9         RET                     ; Done
```

# Parse User Input

```code                     
ParseUserInput: 
442F: CD 0A 46   CALL    $460A           ; Prompt and read line
4432: CD DA 44   CALL    $44DA           ; Parse the input string
4435: 2A AF 45   LD      HL,($45AF)      ; Pointer to noun data
4438: 3A AD 45   LD      A,($45AD)       ; Number of bytes ...
443B: 47         LD      B,A             ; ... in noun data
443C: 3A 82 46   LD      A,($4682)       ; Grammar type
443F: FE 03      CP      $03             ; Value 3 means nothing in buffer
4441: CA 2F 44   JP      Z,$442F         ; Ignore blank lines
4444: 3A 80 46   LD      A,($4680)       ; Noun number
4447: A7         AND     A               ; Was there a noun on the input line?
4448: C2 6A 44   JP      NZ,$446A        ; Yes ... check for verb-noun things
444B: 3A 81 46   LD      A,($4681)       ; Verb
444E: A7         AND     A               ; Did we have a verb?
444F: C2 5B 44   JP      NZ,$445B        ; Yes ... check for verb-only things
;
; Something was typed, but no noun or verb were decoded
4452: 21 5A 4E   LD      HL,$4E5A        ; I_DON'T_UNDERSTAND.[CR]
4455: CD B3 45   CALL    $45B3           ; Print the error
4458: C3 2F 44   JP      $442F           ; Back to the top
;
445B: 3A 82 46   LD      A,($4682)       ; Grammar type
445E: FE C0      CP      $C0             ; Is the verb nounless?
4460: C8         RET     Z               ; Yes ... done (we don't have a noun)
;
; We have a verb that expected a noun, but no noun was given
4461: 21 0B 4C   LD      HL,$4C0B        ; WHAT?[CR]
4464: CD B3 45   CALL    $45B3           ; Print error (verb expected noun)
4467: C3 2F 44   JP      $442F; Back to top of input loop
;
; We have a verb and a noun
446A: 22 AF 45   LD      ($45AF),HL      ; Pointer into noun data
446D: 3A D9 44   LD      A,($44D9)       ; Did we have ...
4470: A7         AND     A               ; ... lone noun last parse?
4471: C2 C6 44   JP      NZ,$44C6        ; Yes ... use that now
;
4474: 7E         LD      A,(HL)          ; Next word-for-object value
4475: 23         INC     HL              ; Bump ...
4476: 22 AF 45   LD      ($45AF),HL      ; ... word-data pointer
4479: 1E FF      LD      E,$FF           ; Look in backpack first
447B: C5         PUSH    BC              ; Hold
447C: CD AB 43   CALL    $43AB           ; Find object
447F: C1         POP     BC              ; Restore
4480: CA BE 44   JP      Z,$44BE         ; Found object. Use it.
4483: 3A 82 46   LD      A,($4682)       ; Grammar type
4486: FE 40      CP      $40             ; 01 ... noun must be in pack
4488: CA 9C 44   JP      Z,$449C         ; Validate noun
448B: 2A AF 45   LD      HL,($45AF)      ; Pointer to noun data
448E: 2B         DEC     HL              ;
448F: 3A 2F 49   LD      A,($492F)       ; Current room
4492: 5F         LD      E,A             ; For find
4493: 7E         LD      A,(HL)          ; Back up data pointer
4494: C5         PUSH    BC              ; Hold
4495: CD AB 43   CALL    $43AB           ; Do find
4498: C1         POP     BC              ; Restore
4499: CA BE 44   JP      Z,$44BE         ; Object is in room. Use it.
;
449C: 2A AF 45   LD      HL,($45AF)      ; Noun data
449F: 05         DEC     B               ; All tried?
44A0: C2 74 44   JP      NZ,$4474        ; No ... try next word
44A3: 3A 82 46   LD      A,($4682)       ; Grammar type
44A6: FE 40      CP      $40             ; 01 ... noun must be in pack
44A8: C2 B1 44   JP      NZ,$44B1        ; Could be pack or room
44AB: 21 1F 4E   LD      HL,$4E1F        ; YOU_AREN'T_CARRYING_IT.[CR]
44AE: C3 B4 44   JP      $44B4           ; Print and out
44B1: 21 31 4E   LD      HL,$4E31        ; THERE'S_NOT_ONE_HERE.[CR]
44B4: CD B3 45   CALL    $45B3           ; Print error
44B7: 97         SUB     A               ; This noun doesn't ...
44B8: 32 80 46   LD      ($4680),A       ; ... count
44BB: C3 2F 44   JP      $442F           ; Back to top of input loop
;
44BE: 2A AF 45   LD      HL,($45AF)      ; Noun data
44C1: 2B         DEC     HL              ; Back to word pointer
44C2: 7E         LD      A,(HL)          ; Get the for-object value
44C3: 32 80 46   LD      ($4680),A       ; Hold the value
; Hold the value
;
44C6: 3A 81 46   LD      A,($4681)       ; Verb
44C9: A7         AND     A               ; Was there a verb?
44CA: C0         RET     NZ              ; Yes ... got what we need
44CB: 21 41 4E   LD      HL,$4E41        ; WHAT_SHOULD_I_DO_WITH_IT?[CR]
44CE: CD B3 45   CALL    $45B3           ; Print message
44D1: 3E 01      LD      A,$01           ; Flag that we have a lone ...
44D3: 32 D9 44   LD      ($44D9),A       ; ... noun
44D6: C3 2F 44   JP      $442F           ; Back to the top of input loop
           
44D9: 00 ; 1 if there was a lone object last input; 1 if there was a lone object last input             

; Parse the input line
ParseInputLine: 
44DA: 21 5F 46   LD      HL,$465F        ; Start of the input
44DD: 97         SUB     A               ; Make a zero
44DE: 32 AE 45   LD      ($45AE),A       ; Nothing in buffer to start with
44E1: 32 82 46   LD      ($4682),A       ; Grammar type
;
44E4: 11 9A 4A   LD      DE,$4A9A        ; Command table
44E7: EB         EX      DE,HL           ; Next word to HL 
44E8: 22 88 46   LD      ($4688),HL      ; Pointer to next word to check
44EB: EB         EX      DE,HL           ; Back to DE
; Skip spaces before a word
44EC: 7E         LD      A,(HL)          ; Next character from input buffer
44ED: FE 20      CP      $20             ; A space?
44EF: C2 F6 44   JP      NZ,$44F6        ; No ... decode this input
44F2: 23         INC     HL              ; It is a space, skip over it
44F3: C3 EC 44   JP      $44EC           ; And keep trying

; Slightly different code here than first floor code. This next
; line is removed from first floor. It is never used here either.
; This strengthens my belief that the 1st floor code went through
; a squeezing exercise to get bytes.
;
44F6: 22 8A 46   LD      ($468A),HL    ; Hold on to pointer (never read)
;
44F9: A7         AND     A               ; Reached the end ...
44FA: CA 84 45   JP      Z,$4584         ; ... of the line
44FD: 3E 01      LD      A,$01           ; Flag that something ...
44FF: 32 AE 45   LD      ($45AE),A       ; ... is in the buffer
4502: E5         PUSH    HL              ; Hold start of word
4503: 1A         LD      A,(DE)          ; Have we reached ...
4504: A7         AND     A               ; ... the end of the command table?
4505: CA 8F 45   JP      Z,$458F         ; Yes ... give error
4508: 32 90 46   LD      ($4690),A       ; Store word data
450B: E6 07      AND     $07             ; Size of text ...
450D: 4F         LD      C,A             ; ... to C
450E: 32 8C 46   LD      ($468C),A       ; Text count
4511: 3A 90 46   LD      A,($4690)       ; Word data again
4514: E6 38      AND     $38             ; Mask 0_111_000
4516: 0F         RRCA                    ; Get ...
4517: 0F         RRCA                    ; ... number of ...
4518: 0F         RRCA                    ; ... data bytes
4519: 47         LD      B,A             ; To B
451A: EB         EX      DE,HL           ; Update ...
451B: 22 88 46   LD      ($4688),HL      ; ... command table ...
451E: EB         EX      DE,HL           ; ... pointer
451F: 13         INC     DE              ; Next in word text
4520: 1A         LD      A,(DE)          ; Character from table
4521: BE         CP      (HL)            ; Same as user input?
4522: C2 76 45   JP      NZ,$4576        ; No ... not this word
4525: 23         INC     HL              ; Next character ...
4526: 13         INC     DE              ; ... to try
4527: 0D         DEC     C               ; Tried all in the table?
4528: C2 20 45   JP      NZ,$4520        ; No ... keep looking
452B: 3A 8C 46   LD      A,($468C)       ; Text count
452E: FE 04      CP      $04             ; Four (or more)?
4530: CA 3D 45   JP      Z,$453D         ; Yes ... we need to ignore extras
4533: 7E         LD      A,(HL)          ; Next in buffer
4534: FE 20      CP      $20             ; Word ended correctly in the buffer?
4536: CA 4B 45   JP      Z,$454B         ; Yes ... this is our word
4539: A7         AND     A               ; Word ended correctly at end of buffer?
453A: C2 7B 45   JP      NZ,$457B        ; No ... not our word
;Skip to end of word
453D: 7E         LD      A,(HL)          ; Next character in buffer
453E: FE 20      CP      $20             ; A space?
4540: CA 4B 45   JP      Z,$454B         ; Yes ... word matched
4543: A7         AND     A               ; End of buffer?
4544: CA 4B 45   JP      Z,$454B         ; Yes ... word matched
4547: 23         INC     HL              ; Next in input buffer
4548: C3 3D 45   JP      $453D           ; Skip to end of the word
; Word matched
454B: 3A 90 46   LD      A,($4690)       ; Word data
454E: E6 C0      AND     $C0             ; Top two bits ... word type
4550: CA 5D 45   JP      Z,$455D         ; Word is a noun
4553: 32 82 46   LD      ($4682),A       ; Store grammar type
4556: 1A         LD      A,(DE)          ; Get word number
4557: 32 81 46   LD      ($4681),A       ; Store verb
455A: C3 6E 45   JP      $456E           ; Check for more to parse
;Word is a noun
455D: 1A         LD      A,(DE)          ; Noun number from the word's data
455E: 32 80 46   LD      ($4680),A       ; Hold word number
4561: EB         EX      DE,HL           ; Store ...
4562: 22 AF 45   LD      ($45AF),HL      ; ... pointer to noun data
4565: EB         EX      DE,HL           ; Restore pointers
4566: 78         LD      A,B             ; Number of data bytes
4567: 32 AD 45   LD      ($45AD),A       ; Hold this for later
456A: 97         SUB     A               ; No longer remember ...
456B: 32 D9 44   LD      ($44D9),A       ; ... a past lone object

456E: 7E         LD      A,(HL)          ; Next from buffer
456F: FE 20      CP      $20             ; Is it a space
4571: D1         POP     DE              ; Restore command table pointer
4572: CA E4 44   JP      Z,$44E4         ; Yes ... more input. Parse next word.
4575: C9         RET                     ; That's all the input we need
; Word doesn't match
4576: 13         INC     DE              ; Skip ...
4577: 0D         DEC     C               ; ... to end of word text ...
4578: C2 76 45   JP      NZ,$4576        ; ... in table
457B: 13         INC     DE              ; Skip to end ...
457C: 05         DEC     B               ; ... of data ...
457D: C2 7B 45   JP      NZ,$457B        ; ... bytes
4580: E1         POP     HL              ; Back to start of word
4581: C3 EC 44   JP      $44EC           ; Try next word in command table

; End of input
4584: 3A AE 45   LD      A,($45AE)       ; Something in ...
4587: A7         AND     A               ; ... the buffer?
4588: C0         RET     NZ              ; Yes ... done
4589: 3E 03      LD      A,$03           ; Grammar type 3 means ...
458B: 32 82 46   LD      ($4682),A       ; ... nothing in buffer
458E: C9         RET                     ; Done

; Skip leading space in front of token and then skip to next token.
; If there is another token go back and decode. Otherwise return.
458F: E1         POP     HL              ; Start of word
4590: 97         SUB     A               ; Clear ...  
4591: 32 81 46   LD      ($4681),A       ; ... verb ...
4594: 32 80 46   LD      ($4680),A       ; ... and noun
4597: 7E         LD      A,(HL)          ; Next character
4598: FE 20      CP      $20             ; A space?
459A: C2 A1 45   JP      NZ,$45A1        ; No ... out of loop
459D: 23         INC     HL              ; Next in input
459E: C3 97 45   JP      $4597           ; Skip spaces
;
45A1: 7E         LD      A,(HL)          ; Next in buffer          
45A2: A7         AND     A               ; End of buffer?
45A3: C8         RET     Z               ; Yes ... out
45A4: FE 20      CP      $20             ; Space?
45A6: CA E4 44   JP      Z,$44E4         ; Restart at top of command list
45A9: 23         INC     HL              ; Next input
45AA: C3 A1 45   JP      $45A1           ; Keep looking

; RAM used in parsing input
45AD: 00       ; Number of data bytes in noun
45AE: 00       ; 0 if decode is empty, 1 if something was decoded               
45AF: 00 00    ; Pointer to noun data            
45B1: 00 00             
```

# Print Packed

```code
PrintPacked: 
; Unpack a message (or multiple packed message) and print.
; HL is pointer to message   
45B3: 7E         LD      A,(HL)          ; Get the length
45B4: A7         AND     A               ; None ... 
45B5: C8         RET     Z               ; ... out
45B6: 23         INC     HL              ; Skip over length
45B7: 11 5F 46   LD      DE,$465F        ; Buffer
45BA: CD BC 46   CALL    $46BC           ; Unpack and print
45BD: 7E         LD      A,(HL)          ; Get terminator
45BE: A7         AND     A               ; Zero ...
45BF: CA EC 45   JP      Z,$45EC         ; ... print carriage return and out
45C2: FE 01      CP      $01             ; Leave alone?
45C4: C8         RET     Z               ; Yes ... we are done
45C5: 47         LD      B,A             ; To position for print
45C6: E5         PUSH    HL              ; Hold HL
45C7: CD 04 46   CALL    $4604           ; Print the character
45CA: E1         POP     HL              ; Restore HL
45CB: 7E         LD      A,(HL)          ; Get next byte from unpacked
45CC: FE 0A      CP      $0A             ; Mark for another packing?
45CE: 23         INC     HL              ; 
45CF: CA B3 45   JP      Z,$45B3         ; Yes ... start again
45D2: C3 BD 45   JP      $45BD           ; No ... continue this packing
```
 
# Print Message

```code   
; HL points to message terminated by
;  - 0 : add a CR on the end and return
;  - 1 : no CR on the end and return
; Return with B holding last character (if any) sent to ROM routine.
;
PrintMessage: 
45D5: 7E         LD      A,(HL)          ; Get next character from message
45D6: A7         AND     A               ; End of message (with CR)?
45D7: CA EC 45   JP      Z,$45EC         ; Yes ... print CR and return
45DA: FE 01      CP      $01             ; End of message (no CR)?
45DC: C8         RET     Z               ; Yes ... done
45DD: FE 40      CP      $40             ; Skip over character?
45DF: CA E8 45   JP      Z,$45E8         ; Yes ... just advance cursor
45E2: 47         LD      B,A             ; Character to B
45E3: E5         PUSH    HL              ; Hold message pointer
45E4: CD 04 46   CALL    $4604           ; Print character
45E7: E1         POP     HL              ; Increment ...
45E8: 23         INC     HL              ; ... message pointer
45E9: C3 D5 45   JP      $45D5           ; Next character in message
;           
45EC: 06 0D      LD      B,$0D           ; CR character
45EE: 78         LD      A,B             ; To A
45EF: CD 04 46   CALL    $4604           ; Print character
45F2: C9         RET                     
```

# Wait For Key

```code   
WaitForKey: 
45F3: D5         PUSH    DE              ; Hold DE
45F4: 3A 83 46   LD      A,($4683)       ; Bump ...
45F7: 3C         INC     A               ; ... some ...
45F8: 32 83 46   LD      ($4683),A       ; ... ??? counter
45FB: CD 2B 00   CALL    $002B           ; Get a key
45FE: A7         AND     A               ; Keep waiting ...
45FF: CA F4 45   JP      Z,$45F4         ; ... if nothing pressed
4602: D1         POP     DE              ; Restore DE
4603: C9         RET                     ; Return key in A
```

# PrintChar

```code
PrintChar:       
4604: D5         PUSH    DE              ; Hold DE
4605: CD 33 00   CALL    $0033           ; Print the character
4608: D1         POP     DE              ; Restore DE
4609: C9         RET; Done
```

# Prompt And Read Line

```code
PromptAndReadLine: 
460A: 06 3A      LD      B,$3A           ; ":" for prompt
460C: 78         LD      A,B             ; To A for printing
460D: CD 04 46   CALL    $4604           ; Print the prompt
4610: 21 5F 46   LD      HL,$465F        ; Input buffer
4613: 0E 00      LD      C,$00           ; Size of input buffer (starts empty)
;
4615: E5         PUSH    HL              ; Hold ...
4616: C5         PUSH    BC              ; ... most ...
4617: D5         PUSH    DE              ; ... everything
4618: CD F3 45   CALL    $45F3           ; Wait for a key
461B: D1         POP     DE              ; ... restore ...
461C: C1         POP     BC              ; ... most ...
461D: E1         POP     HL              ; ... everything
461E: 47         LD      B,A             ; Key to B
461F: FE 08      CP      $08             ; A backspace?
4621: CA 46 46   JP      Z,$4646         ; Yes ... go handle that
4624: 77         LD      (HL),A          ; Put character in buffer
4625: CD 04 46   CALL    $4604           ; Send the character to the screen
4628: FE 0D      CP      $0D             ; Was it ENTER?
462A: CA 5C 46   JP      Z,$465C         ; Yes ... we have our line
462D: 0C         INC     C               ; Bump the input count
462E: 23         INC     HL              ; Bump the pointer in the buffer
462F: 11 7F 46   LD      DE,$467F        ; End of buffer (32 bytes long)
4632: 7C         LD      A,H             ; Compare ...
4633: BA         CP      D               ; ... MSB
4634: DA 15 46   JP      C,$4615         ; Not the same ... still room for more
4637: 7D         LD      A,L             ; Compare ...
4638: BB         CP      E               ; ... LSB
4639: DA 15 46   JP      C,$4615         ; Not the same ... still room for more
463C: 06 08      LD      B,$08           ; No more room. Take the last ...
463E: 78         LD      A,B             ; ... character ...
463F: CD 04 46   CALL    $4604           ; ... off the screen
4642: 2B         DEC     HL              ; And reject the character from our buffer
4643: C3 15 46   JP      $4615           ; Back for more input (better be backspaces)
; Backspace
4646: 2B         DEC     HL              ; Back up our pointer
4647: 3E 46      LD      A,$46           ; Compare MSB to ...
4649: BC         CP      H               ; ... start of buffer
464A: DA 53 46   JP      C,$4653         ; Not the same. We can take it.
464D: 7D         LD      A,L             ; Compare LSB to ...
464E: FE 5F      CP      $5F             ; ... start of buffer
4650: DA 10 46   JP      C,$4610         ; Nothing left to remove. Ignore this.
4653: 3E 08      LD      A,$08           ; Backspace ...
4655: 47         LD      B,A             ; ... to ...
4656: CD 04 46   CALL    $4604           ; ... screen
4659: C3 15 46   JP      $4615           ; Back to input loop
; Enter
465C: 36 00      LD      (HL),$00        ; Put a zero on the end of the buffer        
465E: C9         RET                     ; Done
```

# Input Buffer

```code
; Input buffer (with some uninitialized leftover data!)
InputBuffer: 
; 32 bytes
465F: 45 20 49 50 20 53 49 47 4E 00 00 47 FE 78 28 26
466F: FE 3C 20 F5 CD 82 47 47 CD 9C 46 00 00 00 00 00               
467F: 00    

; Used in input parsing           
4680: 00    ; Noun             
4681: 00    ; Verb              
4682: 00    ; Grammar type             
4683: 00    ; Input loop counter (never used)                 
4684: 00 00 ; Pointer to next word while parsing                 
4686: 00    ; Character counter in word text               
4687: 00    ; Current word data 
4688: 00 00 ;
468A: 00 00 ; Input buffer pointer (never used)
    
; Uninitialized stack space with some leftover data in it!
; This might be interesting stuff?
StackRAM: 
468C: 00 00 00 00 00 21 00 15 40 0D 02 C0             
4698: 3F 80 04 DD 03 1D 40 15 40 D4 4D 5E 0D 08 46 5F                   
46A8: 46 FA 48 97 4A FA 48 FA 48 26 44 FE 48 F2 43 93 
46B8: 00                            
; Stack points here at beginning
46B9: 00
                         
46BA: 00 00 ; Not used   
```

# Unpack Message

```code
UnpackMessage: 
; TODO: Decode this. I have a program created by translating this to Java.
; It works, but it would be nice to understand the math here.
46BC: 32 7E 47   LD      ($477E),A       ;
46BF: 3E 01      LD      A,$01           ;
46C1: 32 81 47   LD      ($4781),A       ;
46C4: C3 CE 46   JP      $46CE           ;     
46C7: 32 7E 47   LD      ($477E),A       ;
46CA: 97         SUB     A               ;  
46CB: 32 81 47   LD      ($4781),A       ;
46CE: E5         PUSH    HL              ;
46CF: 06 03      LD      B,$03           ;
46D1: E1         POP     HL              ;
46D2: 7E         LD      A,(HL)          ;
46D3: 23         INC     HL              ;
46D4: 4E         LD      C,(HL)          ;
46D5: 23         INC     HL              ;
46D6: E5         PUSH    HL              ;
46D7: 61         LD      H,C             ;
46D8: 6F         LD      L,A             ;
46D9: 13         INC     DE              ;
46DA: 13         INC     DE              ;
46DB: EB         EX      DE,HL           ;   
46DC: E5         PUSH    HL              ;
46DD: C5         PUSH    BC              ;
46DE: 21 28 00   LD      HL,$0028        ; Number of characters in map
46E1: 22 7F 47   LD      ($477F),HL      ; 
46E4: 21 14 47   LD      HL,$4714        ;
46E7: 36 11      LD      (HL),$11        ; 17 passes
46E9: 01 00 00   LD      BC,$0000        ;
46EC: C5         PUSH    BC              ;
46ED: 7B         LD      A,E             ;
46EE: 17         RLA                     ;
46EF: 5F         LD      E,A             ;
46F0: 7A         LD      A,D             ;
46F1: 17         RLA                     ;
46F2: 57         LD      D,A             ;
46F3: 35         DEC     (HL)            ;
46F4: E1         POP     HL              ;
46F5: CA 15 47   JP      Z,$4715         ;
46F8: 3E 00      LD      A,$00           ;
46FA: CE 00      ADC     $00             ; 
46FC: 29         ADD     HL,HL           ;
46FD: 44         LD      B,H             ;
46FE: 85         ADD     A,L             ;
46FF: 2A 7F 47   LD      HL,($477F)      ;
4702: 95         SUB     L               ;  
4703: 4F         LD      C,A             ;
4704: 78         LD      A,B             ;
4705: 9C         SBC     H               ; 
4706: 47         LD      B,A             ;
4707: C5         PUSH    BC              ;
4708: D2 0D 47   JP      NC,$470D        ;
470B: 09         ADD     HL,BC           ;
470C: E3         EX      (SP),HL         ;
470D: 21 14 47   LD      HL,$4714        ;
4710: 3F         CCF                     ;
4711: C3 ED 46   JP      $46ED           ;
4714: 00                                 ;
4715: 01 56 47   LD      BC,$4756        ; Character compression map
4718: 09         ADD     HL,BC           ; Offset into table
4719: 7E         LD      A,(HL)          ; Get the character value
471A: C1         POP     BC              ; Restore BC
471B: E1         POP     HL              ; Restore pointer to buffer
471C: 77         LD      (HL),A          ; Replace the character with the decoded value
471D: 2B         DEC     HL              ; Next character (moving left)
471E: 05         DEC     B               ; All done?
471F: C2 DC 46   JP      NZ,$46DC        ; No ... keep decoding
4722: 3A 81 47   LD      A,($4781)       ;
4725: A7         AND     A               ;
4726: CA 3E 47   JP      Z,$473E         ;
4729: E5         PUSH    HL              ;
472A: C5         PUSH    BC              ;
472B: D5         PUSH    DE              ;
472C: 1E 03      LD      E,$03           ;
472E: 23         INC     HL              ;
472F: 46         LD      B,(HL)          ;
4730: E5         PUSH    HL              ;
4731: 78         LD      A,B             ;
4732: CD 04 46   CALL    $4604           ; Print character
4735: E1         POP     HL              ;
4736: 23         INC     HL              ;
4737: 1D         DEC     E               ;
4738: C2 2F 47   JP      NZ,$472F        ;
473B: D1         POP     DE              ;
473C: C1         POP     BC              ;
473D: E1         POP     HL              ;
473E: EB         EX      DE,HL           ;
473F: 13         INC     DE              ;
4740: 3A 81 47   LD      A,($4781)       ;
4743: A7         AND     A               ;
4744: C2 4A 47   JP      NZ,$474A        ;
4747: 13         INC     DE              ;
4748: 13         INC     DE              ;
4749: 13         INC     DE              ;
474A: 3A 7E 47   LD      A,($477E)       ;
474D: 3D         DEC     A               ;
474E: 32 7E 47   LD      ($477E),A       ;
4751: C2 CF 46   JP      NZ,$46CF        ;
4754: E1         POP     HL              ;
4755: C9         RET                     ;
```

# Character Table

```code
; Character compression table
CharTable:                 
4756: 3F 21 32 20 22 27 3C 3E 2F 30 33                 ; ?!2_"'<>/03
4761: 41 42 43 44 45 46 47 48 49 4A 4B 4C 4D 4E 4F 50  ; ABCDEFGHIJKLMNOP                    
4771: 51 52 53 54 55 56 57 58 59 5A 2D 2C 2E           ; QRSTUVWXYZ-,.
 
477E: 00 ; RAM used by unpack        
477F: 00 ; RAM used by unpack                
4780: 00 ; RAM used by unpack                    
4781: 00 ; RAM used by unpack
```

# Room Information

```code
RoomInformation: 
; First two: description (most rooms look the same)
; Second two: room script                     
4782: E6 4B A2 47 ; 1 DIMLY_LIT_ROOM.__THERE_IS_A_HOLE_IN_THE_FLOOR.[CR]   
4786: DA 4B B5 47 ; 2 DIMLY_LIT_ROOM.[CR]      
478A: DA 4B EF 47 ; 3 DIMLY_LIT_ROOM.[CR]         
478E: DA 4B 29 48 ; 4 DIMLY_LIT_ROOM.[CR]        
4792: DA 4B 67 48 ; 5 DIMLY_LIT_ROOM.[CR]              
4796: DA 4B A0 48 ; 6 DIMLY_LIT_ROOM.[CR]            
479A: DA 4B B9 48 ; 7 DIMLY_LIT_ROOM.[CR]              
479E: DA 4B CE 48 ; 8 DIMLY_LIT_ROOM.[CR]     
    
; TODO a word here on duplicate words.
```

# Room Scripts

```code
RoomScripts: 
; Commands 1
; All of these rooms look the same except for this first one you start in
; on the second floor. In this room there is a hole in the floor, but climbing
; down will kill you.
; 
                     ; "Room_1"   : {
                     ;     "Description" : "YOU_ARE_IN_A_DIMLY_LIT_ROOM.__THERE_IS_A_HOLE_IN_THE_FLOOR.[CR]",
47A2: 02 03 01 02    ;     "E"    : ["GoToRoom(2)"],
47A6: 03 03 01 03    ;     "S"    : ["GoToRoom(3)"],
47AA: 04 03 01 04    ;     "W"    : ["GoToRoom(4)"],
47AE: 0F 05 04 F4 4D ;     "CLIM" : ["Print(YOU_FALL_THROUGH_THE_HOLE_AND_BREAK_YOUR_NECK.__YOU_ARE_DEAD.[CR])",
47B3: 07             ;               "EndlessLoop()"]
47B4: 00             ; },

; Commands 2 
; If you HIT the sword you get a message that you hurt your hand.
;
; This room either has GHOST1 (living) or GHOST5 (dead).
; If GHOST1 (living) is in the room:
;   You can KILL the GHOST if you have the sword. GHOST1 is moved out of play and GHOST5 is moved to this room.
;   If you KILL GHOST without the sword you get a warning about your "BARE HANDS".
; If GHOST5 (dead) is in the room:
;   Any KILL command results in "THE POOR THING'S ALREADY DEAD". Bring the sign back to this room with the
;   dead ghost and KILL SIGN.
;
; There is only one exit from this room, but the scripts will print "THE GHOST WILL NOT LET YOU PASS!" if
; it is alive and you go in any invalid direction. This is a little trickery to make you think the ghost
; is actually blocking you, when really there is nowhere to go.
;
                  ; "Room_2"   : {
                  ;     "Description" : "YOU_ARE_IN_A_DIMLY_LIT_ROOM.[CR]",                   
47B5: 11 06 0A 09 ;     "KILL" : ["AssertNounIs(SWORD)",       
47B9: 04 91 4C    ;               "Print(OUCH!__YOU_HURT_YOUR_HAND.[CR])"],        
47BC: 04 03 01 01 ;     "W"    : ["GoToRoom(1)"],
47C0: 11 18 06 13 ;     "KILL" : ["SubscriptAbortAllIfPass", [            
47C4: 10 01       ;                   "AssertObjectIsInRoom(GHOST1)"
47C6: 06 0C       ;                   "SubscriptAbortAllIfPass", [   
47C8: 02 09       ;                       "AssertObjectIsInPack(SWORD)",
47CA: 0D 01 00    ;                       "MoveObjectToRoom(GHOST1,0)",
47CD: 0D 05 02    ;                       "MoveObjectToRoom(GHOST5,2)",         
47D0: 04 11 4C    ;                       "Print(YOUR_MAGIC_SWORD_ENABLES_YOU_TO_KILL_THE_GHOST![CR])"]
47D3: 04 43 4C    ;                   "Print(YOU_CAN'T_KILL_A_GHOST_WITH_YOUR_BARE_HANDS.[CR])"]
47D6: 04 63 4C    ;               "Print(THE_POOR_THING'S_ALREADY_DEAD.[CR])"],
47D9: 01 06 10 01 ;     "N"    : ["AssertObjectIsInRoom(GHOST1)",
47DD: 04 79 4C    ;               "Print(THE_GHOST_WILL_NOT_LET_YOU_PASS![CR])"],      
47E0: 02 06 10 01 ;     "E"    : ["AssertObjectIsInRoom(GHOST1)",
47E4: 04 79 4C    ;               "Print(THE_GHOST_WILL_NOT_LET_YOU_PASS![CR]))"],
47E7: 03 06 10 01 ;     "S"    : ["AssertObjectIsInRoom(GHOST1)",
47EB: 04 79 4C    ;               "Print(THE_GHOST_WILL_NOT_LET_YOU_PASS![CR]))"]
47EE: 00          ; },                  

; Commands 3
; If you HIT the sword you get a message that you hurt your hand.
;
; This room either has GHOST2 (living) or GHOST6 (dead).
; If GHOST2 (living) is in the room:
;   If you KILL GHOST without the sword you get a warning about your "BARE HANDS".
;   You can KILL the GHOST if you have the sword. GHOST2 is moved out of play and GHOST6 is moved to this room.
; If GHOST6 (dead) is in the room:
;   Any KILL command results in "THE POOR THING'S ALREADY DEAD". Bring the sign back to this room with the
;   dead ghost and KILL SIGN.
;
; There is only one exit from this room, but the scripts will print "THE GHOST WILL NOT LET YOU PASS!" if
; it is alive and you go in any invalid direction. This is a little trickery to make you think the ghost
; is actually blocking you, when really there is nowhere to go.
; 
                  ; "Room_3"   : {
                  ;     "Description" : "YOU_ARE_IN_A_DIMLY_LIT_ROOM.[CR]",
47EF: 11 06 0A 09 ;     "KILL" : ["AssertNounIs(SWORD)",                 
47F3: 04 91 4C    ;               "Print(OUCH!__YOU_HURT_YOUR_HAND.[CR])"],                 
47F6: 01 03 01 01 ;     "N"    : ["GoToRoom(1)"],
47FA: 11 18 06 13 ;     "KILL" : ["SubscriptAbortAllIfPass", [             
47FE: 10 02       ;                   "AssertObjectIsInRoom(GHOST2)"      
4800: 06 0C       ;                   "SubscriptAbortAllIfPass", [          
4802: 02 09       ;                       "AssertObjectIsInPack(SWORD)",         
4804: 0D 02 00    ;                       "MoveObjectToRoom(GHOST2,0)",                       
4807: 0D 06 03    ;                       "MoveObjectToRoom(GHOST6,2)",          
480A: 04 11 4C    ;                       "Print(YOUR_MAGIC_SWORD_ENABLES_YOU_TO_KILL_THE_GHOST![CR])"]
480D: 04 43 4C    ;                   "Print(YOU_CAN'T_KILL_A_GHOST_WITH_YOUR_BARE_HANDS.[CR])"]        
4810: 04 63 4C    ;               "Print(THE_POOR_THING'S_ALREADY_DEAD.[CR])"],        
4813: 02 06 10 02 ;     "E"    : ["AssertObjectIsInRoom(GHOST2)",          
4817: 04 79 4C    ;               "Print(THE_GHOST_WILL_NOT_LET_YOU_PASS![CR])"],             
481A: 03 06 10 02 ;     "S"    : ["AssertObjectIsInRoom(GHOST2)",           
481E: 04 79 4C    ;               "Print(THE_GHOST_WILL_NOT_LET_YOU_PASS![CR])"],            
4821: 04 06 10 02 ;     "W"    : ["AssertObjectIsInRoom(GHOST2)", 
4825: 04 79 4C    ;               "Print(THE_GHOST_WILL_NOT_LET_YOU_PASS![CR])"],         
4828: 00

; Commands 4 
; If you HIT the sword you get a message that you hurt your hand.
;
; This room either has GHOST3 (living) or GHOST7 (dead).
; If GHOST3 (living) is in the room:
;   If you KILL GHOST without the sword you get a warning about your "BARE HANDS".
;   You can KILL the GHOST if you have the sword. GHOST3 is moved out of play and GHOST7 is moved to this room.
; If GHOST7 (dead) is in the room:
;   Any KILL command results in "THE POOR THING'S ALREADY DEAD". Bring the sign back to this room with the
;   dead ghost and KILL SIGN.
;
; There are two exits from this room. You can go East any time, but this time the ghost does block your
; passage. Once you kill the ghost you can go West.
;
                  ; "Room_4"   : {
                  ;     "Description" : "YOU_ARE_IN_A_DIMLY_LIT_ROOM.[CR]",                     
4829: 11 06 0A 09 ;     "KILL" : ["AssertNounIs(SWORD)",              
482D: 04 91 4C    ;               "Print(OUCH!__YOU_HURT_YOUR_HAND.[CR])"],               
4830: 02 03 01 01 ;     "E"    : ["GoToRoom(1)"], 
4834: 11 18 06 13 ;     "KILL" : ["SubscriptAbortAllIfPass", [               
4838: 10 03       ;                   "AssertObjectIsInRoom(GHOST3)"     
483A: 06 0C       ;                   "SubscriptAbortAllIfPass", [         
483C: 02 09       ;                       "AssertObjectIsInPack(SWORD)",        
483E: 0D 03 00    ;                       "MoveObjectToRoom(GHOST3,0)",                       
4841: 0D 07 04    ;                       "MoveObjectToRoom(GHOST7,2)",             
4844: 04 11 4C    ;                       "Print(YOUR_MAGIC_SWORD_ENABLES_YOU_TO_KILL_THE_GHOST![CR])"]
4847: 04 43 4C    ;                   "Print(YOU_CAN'T_KILL_A_GHOST_WITH_YOUR_BARE_HANDS.[CR])"]             
484A: 04 63 4C    ;               "Print(THE_POOR_THING'S_ALREADY_DEAD.[CR])"],               
484D: 01 06 10 03 ;     "N"    : ["AssertObjectIsInRoom(GHOST3)",                
4851: 04 79 4C    ;               "Print(THE_GHOST_WILL_NOT_LET_YOU_PASS![CR])"],                 
4854: 03 06 10 03 ;     "S"    : ["AssertObjectIsInRoom(GHOST3)",                  
4858: 04 79 4C    ;               "Print(THE_GHOST_WILL_NOT_LET_YOU_PASS![CR])"],             
485B: 04 06 10 03 ;     "W"    : ["AssertObjectIsInRoom(GHOST3)",                  
485F: 04 79 4C    ;               "Print(THE_GHOST_WILL_NOT_LET_YOU_PASS![CR])"],          
4862: 04 03 01 05 ;     "W"    : ["GoToRoom(5)"]
4866: 00          ; },

; Commands 5
; If you HIT the sword you get a message that you hurt your hand.
;
; This room has GHOST4 (living) in it. Like the others, there is a "dead" version GHOST8 of it. But there
; is no way to kill this ghost. You can "KILL" it with or without the SWORD. Either way you just
; get a message.
;
; You can always go East back the way you came. If you have the SWORD in your pack on if it is on the
; floor then the ghost blocks your other movements. You can go North if you drop the sword in a previous
; room. South and West leave you in the current room.
;
                  ; "Room_5"   : {
                  ;     "Description" : "YOU_ARE_IN_A_DIMLY_LIT_ROOM.[CR]",
4867: 11 06 0A 09 ;     "KILL" : ["AssertNounIs(SWORD)",             
486B: 04 91 4C    ;               "Print(OUCH!__YOU_HURT_YOUR_HAND.[CR])"],                
486E: 02 03 01 04 ;     "E"    : ["GoToRoom(4)"],
4872: 11 0B 06 06 ;     "KILL" : ["SubscriptAbortAllIfPass", [             
4876: 02 09       ;                   "AssertObjectIsInPack(SWORD)",         
4878: 04 BF 4C    ;                   "Print(THE_GHOST_IS_IMMUNE_TO_YOUR_ATTACK![CR])"],                
487B: 04 43 4C    ;               "Print(YOU_CAN'T_KILL_A_GHOST_WITH_YOUR_BARE_HANDS.[CR])"],          
487E: 01 0A 06 06 ;     "N"    : ["SubscriptAbortAllIfPass", [ 
4882: 03 09       ;                   "AssertObjectIsInRoomOrPack(SWORD)"
4884: 04 79 4C    ;                   "Print(THE_GHOST_WILL_NOT_LET_YOU_PASS![CR])"],            
4887: 01 06       ;               "GoToRoom(6)"],
4889: 03 0A 06 06 ;     "S"    : ["SubscriptAbortAllIfPass", [          
488D: 03 09       ;                   "AssertObjectIsInRoomOrPack(SWORD)",          
488F: 04 79 4C    ;                   "Print(THE_GHOST_WILL_NOT_LET_YOU_PASS![CR])"],               
4892: 01 05       ;               "GoToRoom(5)"],
4894: 04 0A 06 06 ;     "W"    : ["SubscriptAbortAllIfPass", [          
4898: 03 09       ;                   "AssertObjectIsInRoomOrPack(SWORD)",       
489A: 04 79 4C    ;                   "Print(THE_GHOST_WILL_NOT_LET_YOU_PASS![CR])"],                  
489D: 01 05       ;               "GoToRoom(5)"] 
489F: 00          ; },     

; Commands 6 
; This room has a live GHOST11 that has no dead version. It doesn't block you. You can't kill it.
; It's just scenery.
;
; This room also intercepts all KILL commands. If you KILL SWORD you get the standard
; "HURT YOUR HAND". If you KILL any other object you get the "GHOST WITH BARE HANDS"
; message. Of course, you can't bring the SWORD to this room so you'll never get the
; "HURT" message. Try bringing the SIGN to this room and KILL SIGN!
; 
                     ; "Room_6"   : {
                     ;     "Description" : "YOU_ARE_IN_A_DIMLY_LIT_ROOM.[CR]",  
48A0: 11 06 0A 09    ;     "KILL" : ["AssertNounIs(SWORD)",          
48A4: 04 91 4C       ;               "Print(OUCH!__YOU_HURT_YOUR_HAND.[CR])"],             
48A7: 02 03 01 04    ;     "E"    : ["GoToRoom(4)"],
48AB: 03 03 01 05    ;     "S"    : ["GoToRoom(5)"],
48AF: 04 03 01 07    ;     "W"    : ["GoToRoom(7)"],
48B3: 11 04 04 43 4C ;     "KILL" : ["Print(YOU_CAN'T_KILL_A_GHOST_WITH_YOUR_BARE_HANDS.[CR]))"]                   
48B8: 00             ; },     

; Commands 7 
; This room has a live GHOST12 that has no dead version. It doesn't block you. You can't kill it.
; It's just scenery.
;
; This room also intercepts all KILL commands. If you KILL SWORD you get the standard
; "HURT YOUR HAND". If you KILL any other object you get the "GHOST WITH BARE HANDS"
; message. Of course, you can't bring the SWORD to this room so you'll never get the
; "HURT" message. Try bringing the SIGN to this room and KILL SIGN!
;
                     ; "Room_7"   : {
                     ;     "Description" : "YOU_ARE_IN_A_DIMLY_LIT_ROOM.[CR]",      
48B9: 11 06 0A 09    ;     "KILL" : ["AssertNounIs(SWORD)",         
48BD: 04 91 4C       ;               "Print(OUCH!__YOU_HURT_YOUR_HAND.[CR])"],             
48C0: 02 03 01 06    ;     "E"    : ["GoToRoom(6)"],
48C4: 03 03 01 08    ;     "S"    : ["GoToRoom(8)"],
48C8: 11 04 04 43 4C ;     "KILL" : ["Print(YOU_CAN'T_KILL_A_GHOST_WITH_YOUR_BARE_HANDS.[CR]))"]                
48CD: 00             ; },              

; Commands 8 
; When you READ SIGN from anywhere the exit object is moved to this room. This is handled in
; the general script.
;
; You can always go back North.
;
; Every other direction is the end of the game. If you are holding the SIGN then you die. If you have not
; READ SIGN then you die. If you have READ SIGN then the exit object is here and you escape.
;
                  ; "Room_8"   : {
                  ;     "Description" : "YOU_ARE_IN_A_DIMLY_LIT_ROOM.[CR]",
48CE: 01 03 01 07 ;     "N"    : ["GoToRoom(7)"],                       
48D2: 02 15 06 07 ;     "E"    : ["SubscriptAbortAllIfPass", [          
48D6: 02 0A       ;                   "AssertObjectIsInPack(SIGN)",   
48D8: 04 56 4D    ;                   "Print(YOU_FALL_THROUGH_A_TRAP_DOOR_TO_YOUR_DEATH![CR])",            
48DB: 07          ;                   "EndlessLoop()"],                       
48DC: 06 07       ;               "SubscriptAbortAllIfPass", [
48DE: 10 0D       ;                   "AssertObjectIsInRoom(EXIT)"
48E0: 04 75 4D    ;                   "Print(YOU_WALK_THROUGH_A_DOOR_AND_FIND_YOURSELF_ON_A_BALCONY.__YOU____CLIMB_DOWN_A_TREE_AND_ESCAPE_TO_SAFETY!__CONGRATULATIONS!_______YOU_MADE_IT![CR])",              
48E3: 07          ;                   "EndlessLoop()"],              
48E4: 04 56 4D    ;               "Print(YOU_FALL_THROUGH_A_TRAP_DOOR_TO_YOUR_DEATH![CR])",             
48E7: 07          ;               "EndlessLoop()"],    
48E8: 03 15 06 07 ;     "S"    : ["SubscriptAbortAllIfPass", [           
48EC: 02 0A       ;                   "AssertObjectIsInPack(SIGN)",       
48EE: 04 56 4D    ;                   "Print(YOU_FALL_THROUGH_A_TRAP_DOOR_TO_YOUR_DEATH![CR])",              
48F1: 07          ;                   "EndlessLoop()"],                 
48F2: 06 07       ;               "SubscriptAbortAllIfPass", [   
48F4: 10 0D       ;                   "AssertObjectIsInRoom(EXIT)"     
48F6: 04 75 4D    ;                   "Print(YOU_WALK_THROUGH_A_DOOR_AND_FIND_YOURSELF_ON_A_BALCONY.__YOU____CLIMB_DOWN_A_TREE_AND_ESCAPE_TO_SAFETY!__CONGRATULATIONS!_______YOU_MADE_IT![CR])",                             
48F9: 07          ;                   "EndlessLoop()"],                  
48FA: 04 56 4D    ;               "Print(YOU_FALL_THROUGH_A_TRAP_DOOR_TO_YOUR_DEATH![CR])",            
48FD: 07          ;                   "EndlessLoop()"],                  
48FE: 04 15 06 07 ;     "W"    : ["SubscriptAbortAllIfPass", [              
4902: 02 0A       ;                   "AssertObjectIsInPack(SIGN)",      
4904: 04 56 4D    ;                   "Print(YOU_FALL_THROUGH_A_TRAP_DOOR_TO_YOUR_DEATH![CR])",                
4907: 07          ;                   "EndlessLoop()"],                 
4908: 06 07       ;               "SubscriptAbortAllIfPass", [         
490A: 10 0D       ;                   "AssertObjectIsInRoom(EXIT)"         
490C: 04 75 4D    ;                   "Print(YOU_WALK_THROUGH_A_DOOR_AND_FIND_YOURSELF_ON_A_BALCONY.__YOU____CLIMB_DOWN_A_TREE_AND_ESCAPE_TO_SAFETY!__CONGRATULATIONS!_______YOU_MADE_IT![CR])",             
490F: 07          ;                   "EndlessLoop()"],              
4910: 04 56 4D    ;               "Print(YOU_FALL_THROUGH_A_TRAP_DOOR_TO_YOUR_DEATH![CR])",               
4913: 07          ;                   "EndlessLoop()"]                         
4914: 00          ; } 
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
4915: 00 02 ;  1 GHOST1 (live)              (Room 2)
4917: 00 03 ;  2 GHOST2 (live)              (Room 3)  
4919: 00 04 ;  3 GHOST3 (live)              (Room 4)        
491B: 00 05 ;  4 GHOST4 (live)              (Room 5)   
491D: 00 00 ;  5 GHOST5 (dead)              (out of play)            
491F: 00 00 ;  6 GHOST6 (dead)              (out of play)         
4921: 00 00 ;  7 GHOST7 (dead)              (out of play)              
4923: 00 00 ;  8 GHOST8 (dead)              (out of play)             
4925: 40 01 ;  9 SWORD                     +(Room 1)
4927: 40 08 ; 10 SIGN                      +(Room 8)
4929: 00 06 ; 11 GHOST 11 (not killable)    (Room 6)
492B: 00 07 ; 12 GHOST 12 (not killable)    (Room 7)       
492D: 40 00 ; 13 (open exit marker)        +(out of play) ; ?? Why is this pick-up-able?

492F: 01 ; Current room number (room with hole in the floor)

4930: 00 00 00     
```

# Object Descriptions

```code
ObjectDescriptions: 
; Object descriptions. Two strings: first is "in room" description. Second
; is a shorter "inventory" description.                           
4933: 51 4B ;  1 GHOST1 (live)  
4935: 51 4B ;  2 GHOST2 (live)              
4937: 51 4B ;  3 GHOST3 (live)                 
4939: 51 4B ;  4 GHOST4 (live)                   
493B: 62 4B ;  5 GHOST5 (dead)                  
493D: 62 4B ;  6 GHOST6 (dead)                 
493F: 62 4B ;  7 GHOST7 (dead)               
4941: 62 4B ;  8 GHOST8 (dead)                
4943: 80 4B ;  9 SWORD                
4945: A4 4B ; 10 SIGN              
4947: 51 4B ; 11 GHOST 11 (live)                
4949: 51 4B ; 12 GHOST 12 (live)               
494B: 15 49 ; 13 (open exit marker no description)    
```
 
# Script Commands

```code
ScriptCommands:           
494D: 6E 49 ;  1 GoToRoom(room)        
494F: B6 49 ;  2 AssertObjectIsInPack(object)           
4951: C5 49 ;  3 AssertObjectIsInRoomOrPack(object)         
4953: FE 49 ;  4 PrintMessage(message)          
4955: 76 49 ;  5 PrintRoomDescription()          
4957: 22 44 ;  6 SubscriptAbortAllIfPass[...]
4959: 97 4A ;  7 EndlessLoop()          
495B: 0B 4A ;  8 MoveObjectToCurrentRoom(object)         
495D: 1A 4A ;  9 PrintInventory()          
495F: 44 4A ; 10 AssertInputNounIs(object)           
4961: 52 4A ; 11 GetObjectFromRoom(object)           
4963: 79 4A ; 12 PrintOK()           
4965: 82 4A ; 13 MoveObjectToRoom(object,room)             
4967: E9 49 ; 14 GetNounToPack()           
4969: 72 4A ; 15 DropNounToRoom()            
496B: D8 49 ; 16 AssertObjectIsInRoom(object)
             
496D: C9         RET  ; Run-after-every-command comes here (and does nothing)
```

# Script Command 01

```code                     
ScriptCommand01: 
; GoToRoom(room)
496E: E1         POP     HL              ; Pointer to script
496F: 46         LD      B,(HL)          ; Get the room number from the script 
4970: 23         INC     HL              ; Next byte in script
4971: E5         PUSH    HL              ; New pointer into script
4972: 78         LD      A,B             ; Room number to A
4973: 32 2F 49   LD      ($492F),A       ; Change rooms
```

# Script Command 05

```code
ScriptCommand05: 
; PrintRoomDescription()   
4976: CD 7C 49   CALL    $497C           ; Print the room description
4979: C3 0B 44   JP      $440B           ; ScriptCommandPASS
```

# Describe Room

```code
DescribeRoom: 
; DescribeCurrentRoom()
497C: 21 CF 4B   LD      HL,$4BCF        ; "YOU ARE AT THE " message
497F: CD B3 45   CALL    $45B3           ; Print the message
4982: 3A 2F 49   LD      A,($492F)       ; Room number
4985: 21 82 47   LD      HL,$4782        ; Room descriptions
4988: CD C6 43   CALL    $43C6           ; 4-byte offset
498B: 7E         LD      A,(HL)          ; Get ...
498C: 23         INC     HL              ; ... LSB ...
498D: 66         LD      H,(HL)          ; ... and ...
498E: 6F         LD      L,A             ; ... MSB
498F: CD B3 45   CALL    $45B3           ; Print the description
4992: 06 00      LD      B,$00           ; B runs the object numbers
4994: 04         INC     B               ; Next object (1 on first pass)
4995: 3A 2F 49   LD      A,($492F)       ; Room number
4998: 5F         LD      E,A             ; To E for find
4999: 78         LD      A,B             ; Object number for find
499A: FE 0D      CP      $0D             ; All objects (1 through 13) checked?
499C: D0         RET     NC              ; Yes ... done here
499D: CD AB 43   CALL    $43AB           ; Get object if in this room
49A0: C2 94 49   JP      NZ,$4994        ; Object is not in room ... skip it
49A3: 78         LD      A,B             ; Object number
49A4: 21 33 49   LD      HL,$4933        ; Object descriptions
49A7: CD BC 43   CALL    $43BC           ; 2-byte offset
49AA: 7E         LD      A,(HL)          ; Get ...
49AB: 23         INC     HL              ; ... LSB ...
49AC: 66         LD      H,(HL)          ; ... and ...
49AD: 6F         LD      L,A             ; ... MSB
49AE: C5         PUSH    BC              ; Hang on to object number
49AF: CD B3 45   CALL    $45B3           ; Print description
49B2: C1         POP     BC              ; Restore object number
49B3: C3 94 49   JP      $4994           ; Keep checking objects
```

# Script Command 02 

```code
ScriptCommand02: 
; AssertObjectInPack(object)
49B6: E1         POP     HL              ; Script pointer
49B7: 7E         LD      A,(HL)          ; Get object number
49B8: 23         INC     HL              ; New script ...
49B9: E5         PUSH    HL              ; ... pointer
49BA: 1E FF      LD      E,$FF           ; Backpack value
49BC: CD AB 43   CALL    $43AB           ; Get object info
49BF: CA 0B 44   JP      Z,$440B         ; ScriptCommandPASS
49C2: C3 1E 44   JP      $441E           ; ScriptCommandFAIL
```

# Script Command 03

```code
ScriptCommand03: 
; AssertObjectIsInRoomOrPack(object) 
49C5: E1         POP     HL              ; Script pointer
49C6: 46         LD      B,(HL)          ; Get object number
49C7: 23         INC     HL              ; New script ...
49C8: E5         PUSH    HL              ; ... pointer
49C9: 3A 2F 49   LD      A,($492F)       ; Current room ...
49CC: 5F         LD      E,A             ; ... to E for find
49CD: 78         LD      A,B             ; Object number for find
49CE: CD AB 43   CALL    $43AB           ; Look for the object in current room
49D1: CA 0B 44   JP      Z,$440B         ; Found it ... ScriptCommandPASS
49D4: 78         LD      A,B             ; Object number again
49D5: C3 BA 49   JP      $49BA           ; Continue checking the pack
```

# Script Command 16

```code
ScriptCommand16: 
; AssertObjectIsInRoom(object)
49D8: E1         POP     HL              ; Script pointer
49D9: 3A 2F 49   LD      A,($492F)       ; Room number ...
49DC: 5F         LD      E,A             ; ... to E for find
49DD: 7E         LD      A,(HL)          ; Get object number
49DE: 23         INC     HL              ; New script ...
49DF: E5         PUSH    HL              ; ... pointer
49E0: CD AB 43   CALL    $43AB           ; Find the object
49E3: CA 0B 44   JP      Z,$440B         ; Found it in room ... ScriptCommandPASS
49E6: C3 1E 44   JP      $441E           ; ScriptCommandFAIL
```

# Script Command 14

```code
ScriptCommand14: 
; GetNounToPack()
49E9: 3A 80 46   LD      A,($4680)       ; Input Noun
49EC: 1E FF      LD      E,$FF           ; Is object already ...
49EE: CD AB 43   CALL    $43AB           ; ... in backpack?
49F1: C2 F7 49   JP      NZ,$49F7        ; No ... do the get
49F4: C3 79 4A   JP      $4A79           ; Print OK and PASS
;
49F7: 3A 80 46   LD      A,($4680)       ; User input ...
49FA: 47         LD      B,A             ; ... noun
49FB: C3 57 4A   JP      $4A57           ; Get object from room
```

# Script Command 04

```code
ScriptCommand04: 
; PrintMessage(message)
49FE: E1         POP     HL              ; Get script pointer
49FF: 5E         LD      E,(HL)          ; Get ...
4A00: 23         INC     HL              ; ... message pointer ...
4A01: 56         LD      D,(HL)          ; ... from ...
4A02: 23         INC     HL              ; ... script
4A03: E5         PUSH    HL              ; New script pointer
4A04: EB         EX      DE,HL           ; Message pointer to HL
4A05: CD B3 45   CALL    $45B3           ; Unpack and print
4A08: C3 0B 44   JP      $440B           ; ScriptCommandPASS
```

# Script Command 08

```code
ScriptCommand08: 
; MoveObjectToCurrentRoom(object)
4A0B: E1         POP     HL              ; Get script pointer
4A0C: 46         LD      B,(HL)          ; Get the object number
4A0D: 23         INC     HL              ; New script ...
4A0E: E5         PUSH    HL              ; ... pointer
;
4A0F: 3A 2F 49   LD      A,($492F)       ; Current Room number
4A12: 5F         LD      E,A             ; To E
4A13: 78         LD      A,B             ; Object number to A
4A14: CD D1 43   CALL    $43D1           ; Move object
4A17: C3 79 4A   JP      $4A79           ; Print OK and PASS
```

# Script Command 09

```code
ScriptCommand09: 
; PrintInventory()
4A1A: 06 00      LD      B,$00           ; B runs the object numbers
4A1C: 1E FF      LD      E,$FF           ; Location = backpack
4A1E: 04         INC     B               ; Next object (1 on first pass)
4A1F: 78         LD      A,B             ; Have we ...
4A20: FE 0D      CP      $0D             ; ... done all objects (1 - 13) ?
4A22: D2 0B 44   JP      NC,$440B        ; Yes ... ScriptCommandPASS
4A25: CD AB 43   CALL    $43AB           ; Find the object
4A28: C2 1C 4A   JP      NZ,$4A1C        ; Not in the pack ... skip it
4A2B: 78         LD      A,B             ; Object number
4A2C: 21 33 49   LD      HL,$4933        ; Object descriptions
4A2F: CD BC 43   CALL    $43BC           ; 2-byte offset
4A32: 7E         LD      A,(HL)          ; Get ...
4A33: 23         INC     HL              ; ... LSB ...
4A34: 66         LD      H,(HL)          ; ... and ...
4A35: 6F         LD      L,A             ; ... MSB
4A36: 7E         LD      A,(HL)          ; Skip ...
4A37: 23         INC     HL              ; ... to ...
4A38: A7         AND     A               ; ... short ...
4A39: C2 36 4A   JP      NZ,$4A36        ; ... description
4A3C: C5         PUSH    BC              ; Hold object number
4A3D: CD B3 45   CALL    $45B3           ; Print the description
4A40: C1         POP     BC              ; Restore object number
4A41: C3 1C 4A   JP      $4A1C           ; Keep going
```

# Script Command 10

```code
ScriptCommand10: 
; AssertInputNounIs(object)
4A44: E1         POP     HL              ; Script pointer
4A45: 46         LD      B,(HL)          ; Get object number
4A46: 23         INC     HL              ; New ...
4A47: E5         PUSH    HL              ; ... script pointer
4A48: 3A 80 46   LD      A,($4680)       ; Input noun
4A4B: B8         CP      B               ; Are they the same
4A4C: C2 1E 44   JP      NZ,$441E        ; No ... ScriptCommandFAIL
4A4F: C3 0B 44   JP      $440B           ; Yes ... ScriptCommandPASS
```

# Script Command 11

```code
ScriptCommand11: 
; GetObjectFromRoom(object)
4A52: E1         POP     HL              ; Script pointer
4A53: 46         LD      B,(HL)          ; Get object
4A54: 23         INC     HL              ; New ...
4A55: E5         PUSH    HL              ; ... script pointer
4A56: 78         LD      A,B             ; Object number to A for the find
;
4A57: CD AB 43   CALL    $43AB           ; Find the object
4A5A: 7E         LD      A,(HL)          ; Get the flags
4A5B: E6 40      AND     $40             ; Can the user pick it up?
4A5D: C2 69 4A   JP      NZ,$4A69        ; Yes ... move to pack
4A60: 21 33 4C   LD      HL,$4C33        ; "DON'T BE RIDICULOUS"
4A63: CD B3 45   CALL    $45B3           ; Print error message
4A66: C3 0B 44   JP      $440B           ; ScriptCommandPASS (was handled here)
;
4A69: 78         LD      A,B             ; Object number
4A6A: 1E FF      LD      E,$FF           ; Location is backpack
4A6C: CD D1 43   CALL    $43D1           ; Move the object
4A6F: C3 79 4A   JP      $4A79; Print OK and PASS
```

# Script Command 15

```code
ScriptCommand15: 
; DropNounToCurrentRoom()
4A72: 3A 80 46   LD      A,($4680)       ; User input
4A75: 47         LD      B,A             ; To B
4A76: C3 0F 4A   JP      $4A0F           ; Drop the object in the current room
```

# Script Command 12

```code
ScriptCommand12: 
; PrintOK
4A79: 21 07 4C   LD      HL,$4C07        ; "OK"
4A7C: CD B3 45   CALL    $45B3           ; Print OK
4A7F: C3 0B 44   JP      $440B           ; ScriptCommandPASS
```

# Script Command 13

```code
ScriptCommand13: 
; MoveObjectToRoom(object,room)
4A82: E1         POP     HL              ; Script pointer
4A83: 7E         LD      A,(HL)          ; Get object
4A84: 23         INC     HL              ; Next
4A85: 5E         LD      E,(HL)          ; Get room number
4A86: 23         INC     HL              ; New ...
4A87: E5         PUSH    HL              ; ... object pointer
4A88: 21 15 49   LD      HL,$4915        ; Object descriptor
4A8B: CD BC 43   CALL    $43BC           ; 2 byte offset
4A8E: 7E         LD      A,(HL)          ; Clear the ...
4A8F: E6 7F      AND     $7F             ; ... contained-by ...
4A91: 77         LD      (HL),A          ; ... flag
4A92: 23         INC     HL              ; Next
4A93: 73         LD      (HL),E          ; Set the room number
4A94: C3 0B 44   JP      $440B           ; ScriptCommandPASS
```

# Script Command 07

```code        
ScriptCommand07: 
; EndlessLoop()
4A97: C3 97 4A   JP      $4A97  ; Infinite loop
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
;                                            SECOND FLOOR WORDS
4A9A: 0C 53 49 47 4E 0A                    ; 00_001_100  SIGN  0A
4AA0: 0C 53 57 4F 52 09                    ; 00_001_100  SWOR  09
4AA6: 3C 47 48 4F 53 01 02 03 04 05 06 07  ; 00_111_100  GHOS  01 02 03 04 05 06 07
;
4AB2: C9 4E 01                             ; 11_001_001  N     01
4AB5: C9 45 02                             ; 11_001_001  E     02
4AB8: C9 53 03                             ; 11_001_001  S     03
4ABB: C9 57 04                             ; 11_001_001  W     04
4ABE: CC 43 4C 49 4D 0F                    ; 11_001_100  CLIM  0F ; CLIMB and JUMP are the same thing
4AC4: CC 4A 55 4D 50 0F                    ; 11_001_100  JUMP  0F
4ACA: CC 51 55 49 54 0B                    ; 11_001_100  QUIT  0B
4AD0: CC 49 4E 56 45 0C                    ; 11_001_100  INVE  0C
4AD6: CC 4C 4F 4F 4B 0D                    ; 11_001_100  LOOK  0D
4ADC: 4C 44 52 4F 50 07                    ; 01_001_100  DROP  07
4AE2: 8B 47 45 54 06                       ; 10_001_011  GET   06
4AE7: 8C 4F 50 45 4E 05                    ; 10_001_100  OPEN  05
4AED: 8C 53 4D 41 53 11                    ; 10_001_100  SMAS  11 ; SMASH, HIT, ATTACK, and KILL are the same thing
4AF3: CB 48 49 54 11                       ; 11_001_011  HIT   11
4AF8: CC 41 54 54 41 11                    ; 11_001_100  ATTA  11
4AFE: CC 4B 49 4C 4C 11                    ; 11_001_100  KILL  11
4B04: CB 59 45 53 12                       ; 11_001_011  YES   12
4B09: CA 4E 4F 13                          ; 11_001_010  NO    13
4B0D: 4C 52 45 41 44 09                    ; 01_001_100  READ  09
4B13: CC 50 4C 55 47 0A                    ; 11_001_100  PLUG  0A
4B19: 00                                   ; end of list
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
;  - KILL and PLUGH print a message.
;  - You can READ the SIGN or SWORD to get a message. Note that you MUST read the sign to open the exit.  
;
;                    ; {                   
4B1A: 01 02 05       ;  "N"    : ["PrintRoomDescription()"],  
4B1D: 02 02 05       ;  "E"    : ["PrintRoomDescription()"],            
4B20: 03 02 05       ;  "S"    : ["PrintRoomDescription()"],          
4B23: 04 02 05       ;  "W"    : ["PrintRoomDescription()"],               
4B26: 06 02 0E       ;  "GET"  : ["GetNounToPack()"], 
4B29: 07 02 0F       ;  "DROP" : ["DropNounToRoom()"],               
4B2C: 0D 02 05       ;  "LOOK" : ["PrintRoomDescription()"],           
4B2F: 0B 02 07       ;  "QUIT" : ["EndlessLoop()"],                    
4B32: 0C 02  09      ;  "INVE" : ["PrintInventory()"],                  
4B35: 09 09 0A 0A    ;  "READ" : ["AssertInputNounIs(SIGN)",                 
4B39: 0D 0D 08       ;            "MoveObjectToRoom(8)", 
4B3C: 04 D9 4C       ;            "Print(THE_SIGN_SAYS,_______________________________________________________"THERE_ARE_THREE_EXITS_FROM_THIS_ROOM.__ONLY_ONE_IS_TRUE...______YOU_MUST_KNOW,_BUT_NOT_BE_BURDENED_BY,_THIS_CLUE!"[CR])"],   
4B3F: 0A 04 04 A5 4C ;  "PLUG" : ["Print(SORRY,_ONLY_ONE_PLUGH_PER_CUSTOMER.[CR])"],                  
4B44: 11 04 04 91 4C ;  "KILL" : ["Print(; OUCH!__YOU_HURT_YOUR_HAND.[CR])"],                     
4B49: 09 06 0A 09    ;  "READ" : ["AssertInputNounIs(SWORD)",             
4B4D: 04 D5 4D       ;            "Print(AN_INSCRIPTION_READS,_"GHOST_KILLER."[CR])"]            
4B50: 00             ; }
```

# Compressed Text

```code                     
CompressedText: 

; THERE_IS_A_GHOST_HERE.[CR]
4B51: 07 5F BE 5B B1 4B 7B 49 45 85 74 0A BC 2F 62 2E 
4B61: 00 

; THE_BODY_OF_A_DEAD_GHOST_IS_ON_THE_FLOOR.[CR]
4B62: 0D 5F BE B9 14 FB 5C C3 9E 46 45 86 5F 7A 15 E6 
4B72: A0 D5 15 C0 16 82 17 48 5E 81 8D 52 2E 00 

; THERE_IS_A_MAGIC_SWORD_ON_THE_FLOOR.[CR]
4B80: 0C 5F BE 5B B1 4B 7B 4F 45 7B 47 D5 51 44 D2 11 
4B90: 58 96 96 DB 72 89 67 C7 A0 00 

; MAGIC_SWORD[CR]
4B9A: 03 89 91 CB 78 81 BA 52 44 00 

; THERE_IS_A_RUSTY_OLD_SIGN_LAYING_ON_THE_GROUND.[CR]
4BA4: 0F 5F BE 5B B1 4B 7B 54 45 66 C6 51 DB B3 8B 49 
4BB4: B8 8E 96 4B 4A AB 98 03 A0 5F BE 84 15 30 A1 44 
4BC4: 2E 00 

; RUSTY_SIGN[CR]
4BC6: 03 F5 B3 FB C0 49 B8 4E 00 

; YOU_ARE_IN_A 
4BCF: 04 C7 DE 94 14 4B 5E 83 96 20 01 

; DIMLY_LIT_ROOM.[CR]
4BDA: 05 8F 5A FB 8E 96 8C 39 17 FF 9F 00 

; DIMLY_LIT_ROOM.__THERE_IS_A_HOLE_IN_THE_FLOOR.[CR]
4BE6: 0F 8F 5A FB 8E 96 8C 39 17 FF 9F 56 13 F4 72 4B 
4BF6: 5E C3 B5 A9 15 DB 8B 83 7A 5F BE 56 15 44 A0 2E 
4C06: 00 

; OK_[CR]
4C07: 01 8B 9F 00 

; WHAT?[CR]
4C0B: 01 1B D1 54 3F 00 

; YOUR_MAGIC_SWORD_ENABLES_YOU_TO_KILL_THE_GHOST![CR]
4C11: 0F C7 DE 8F AF 7B 47 D5 51 44 D2 07 58 C4 97 F5 
4C21: 8B 51 18 56 C2 CD 9C 46 7A 82 17 49 5E 85 74 54 
4C31: 21 00 

; DON'T_BE_RIDICULOUS![CR]
4C33: 06 80 5B F3 23 5B 4D 06 B2 E7 78 87 8D 53 21 00 

; YOU_CAN'T_KILL_A_GHOST_WITH_YOUR_BARE_HANDS.[CR]
4C43: 0E C7 DE D3 14 E6 96 1B 16 F3 8C 49 45 85 74 19 
4C53: BC 82 7B 51 18 23 C6 D4 4C 4A 5E 8E 48 53 2E 00 

; THE_POOR_THING'S_ALREADY_DEAD.[CR]
4C63: 0A 5F BE E9 16 A3 A0 63 BE AD 98 C3 B5 EF 8D 13 
4C73: 47 FF 14 17 47 00 

; THE_GHOST_WILL_NOT_LET_YOU_PASS![CR]
4C79: 0A 5F BE 7A 15 E6 A0 FB 17 F3 8C 06 9A 3F 16 1B 
4C89: BC 1B A1 55 A4 53 21 00 

; OUCH!__YOU_HURT_YOUR_HAND.[CR]
4C91: 08 25 A1 AB 70 51 18 4A C2 3E C6 51 18 23 C6 50 
4CA1: 72 44 2E 00 

; SORRY,_ONLY_ONE_PLUGH_PER_CUSTOMER.[CR]
4CA5: 0B 44 B9 9E B4 C0 16 FB 8E 0F A0 E6 16 7A C4 DF 
4CB5: 16 85 AF 66 C6 E7 9F 52 2E 00 

; THE_GHOST_IS_IMMUNE_TO_YOUR_ATTACK![CR]
4CBF: 0B 5F BE 7A 15 E6 A0 D5 15 CF 15 B0 94 56 5E DB 
4CCF: 9C 34 A1 96 14 45 BD 4B 21 00 

; THE_SIGN_SAYS,_______________________________________________________"THERE_ARE_THREE_EXITS_FROM_THIS_ROOM.__ONLY_ONE_IS_TRUE...______YOU_MUST_KNOW,_BUT_NOT_BE_BURDENED_BY,_THIS_CLUE!"[CR]
4CD9: 3D 5F BE 5B 17 03 6E 1B B7 33 BB 3B 13 3B 13 3B 
4CE9: 13 3B 13 3B 13 3B 13 3B 13 3B 13 3B 13 3B 13 3B 
4CF9: 13 3B 13 3B 13 3B 13 3B 13 3B 13 3B 13 3B 13 C2 
4D09: 1D 2F 62 94 14 56 5E EF 74 47 5E 96 D7 C8 B5 FF 
4D19: B2 82 17 4B 7B 01 B3 DB 95 C0 16 FB 8E 0F A0 D5 
4D29: 15 8C 17 3F C4 DB F9 3B 13 5B 13 1B A1 B5 94 0D 
4D39: BC 09 9A 04 EE 73 C6 06 9A AF 14 BF 14 3F B1 66 
4D49: 98 C3 14 16 EE 95 73 DE 14 19 C4 22 00 

; YOU_FALL_THROUGH_A_TRAP_DOOR_TO_YOUR_DEATH![CR]
4D56: 0E C7 DE 4B 15 F3 8C 6C BE 29 A1 03 71 8C 17 D3 
4D66: 48 81 5B 96 AF DB 9C 34 A1 FF 14 82 49 21 00 

; YOU_WALK_THROUGH_A_DOOR_AND_FIND_YOURSELF_ON_A_BALCONY.__YOU____CLIMB_DOWN_A_TREE_AND_ESCAPE_TO_SAFETY!__CONGRATULATIONS!_______YOU_MADE_IT![CR]
4D75: 2E C7 DE F3 17 CB 8C 6C BE 29 A1 03 71 09 15 A3 
4D85: A0 8E 48 53 15 33 98 C7 DE 97 B3 03 8C 03 A0 44 
4D95: 45 3D 48 23 A0 3B F4 C7 DE 3B 13 DE 14 64 7A 09 
4DA5: 15 03 D2 56 45 67 B1 90 14 07 58 53 B7 DB A4 6B 
4DB5: BF 08 B7 93 62 BB 06 40 55 AB 6E 6E C0 83 49 1D 
4DC5: A0 BB 06 3B 13 5B 13 1B A1 86 91 4B 5E 54 21 00 

; AN_INSCRIPTION_READS,_"GHOST_KILLER."[CR]
4DD5: 0C 83 48 9D 7A B3 55 43 A7 03 A0 63 B1 2E 5C 71 
4DE5: 13 85 74 0D BC 46 7A 47 62 22 00 

; NO.[CR]
4DF0: 01 0F 9A 00 

; YOU_FALL_THROUGH_THE_HOLE_AND_BREAK_YOUR_NECK.__YOU_ARE_DEAD.[CR]
4DF4: 14 C7 DE 4B 15 F3 8C 6C BE 29 A1 16 71 DB 72 7E 
4E04: 74 43 5E 33 98 6F 4F 0B 48 C7 DE 90 AF DD 5F 3B 
4E14: F4 C7 DE 94 14 46 5E 86 5F 2E 00 

; YOU_AREN'T_CARRYING_IT.[CR]
4E1F: 07 C7 DE 94 14 85 61 05 BC 3C 49 D0 DD CB 6A 54 
4E2F: 2E 00 

; THERE'S_NOT_ONE_HERE.[CR]
4E31: 07 5F BE 5D B1 D0 B5 F3 A0 0F A0 9F 15 7F B1 00 

; WHAT_DO_YOU_WANT_ME_TO_DO_WITH_IT?[CR]
4E41: 0B 1B D1 06 BC DB 9C 1B A1 10 D0 0F BC 56 5E C6 
4E51: 9C D9 9C 82 7B D6 15 3F 00 

; I_DON'T_UNDERSTAND.[CR]
4E5A: 06 46 77 05 A0 17 BC 3F 98 A6 B3 8E 48 2E 00 

; YOU_DROP_EVERYTHING_YOU_HAD_TO_CLIMB_THE_ROPE.__YOU_REACH_THE___SECOND_FLOOR.[CR]
4E69: 19 C7 DE 0C 15 53 A0 CF 62 96 B4 90 73 DB 6A 1B 
4E79: A1 46 72 89 17 DE 14 64 7A 82 17 54 5E 5F A0 3B 
4E89: F4 C7 DE 2F 17 DA 46 82 17 3B 5E 57 17 40 55 08 
4E99: 58 81 8D 52 2E 00 
```
      