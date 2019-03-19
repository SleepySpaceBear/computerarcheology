![TRS-80 Pyramid](TRS80Pyramid.jpg)

# Pyramid

>>> cpu Z80

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

# Start

```code
Start: 

4300: 31 BF 47   LD      SP,$47BF        ; Small stack space
4303: 3E 0E      LD      A,$0E           ; Clear ....
4305: CD 33 00   CALL    $0033           ; ... the screen
4308: 21 82 47   LD      HL,$4782        ; "WELCOME TO PYRAMID!!"
430B: CD D0 45   CALL    $45D0           ; Print the message
430E: CD EE 45   CALL    $45EE           ; Wait for a key

4311: 3E 01      LD      A,$01           ; Starting room is ...
4313: 32 3F 50   LD      ($503F),A       ; ... room 1
4316: CD 45 52   CALL    $5245           ; Print room description

4319: 97         SUB     A               ; A=0
431A: 32 7B 46   LD      ($467B),A       ; Clear noun (object within reach)
431D: 32 7C 46   LD      ($467C),A       ; Clear verb (throw, north, rub, etc)
4320: 32 7D 46   LD      ($467D),A       ; Grammar type (verb, verb+nounInReach, verb+nounInPack)
4323: CD CF 43   CALL    $43CF           ; Get user input line and parse
4326: 3A 3F 50   LD      A,($503F)       ; Room number
4329: 21 88 48   LD      HL,$4888        ; Room descriptors
432C: CD 6B 43   CALL    $436B           ; Get 4 bytes for room
432F: 23         INC     HL              ; Skip over ...
4330: 23         INC     HL              ; ... to room's script pointer
4331: 7E         LD      A,(HL)          ; Script ...
4332: 23         INC     HL              ; ... pointer ...
4333: 66         LD      H,(HL)          ; ... to ...
4334: 6F         LD      L,A             ; ... HL
4335: CD 7D 43   CALL    $437D           ; Process the room script
4338: C2 4A 43   JP      NZ,$434A        ; ZF clear ... script was successful. Move on.
433B: 21 B0 59   LD      HL,$59B0        ; General script
433E: CD 7D 43   CALL    $437D           ; Process the script
4341: C2 4A 43   JP      NZ,$434A        ; Process the script
4344: 21 71 74   LD      HL,$7471        ; General fail message
4347: CD AE 45   CALL    $45AE           ; Print message
434A: CD D9 50   CALL    $50D9           ; After every turn
434D: C3 19 43   JP      $4319           ; Back to get user input
```

# Get Object Info

```code
GetObjectInfo:  
; Return ZF set if found in desired location
; Return HL points to object location structure
4350: 21 E7 4F   LD      HL,$4FE7        
4353: CD 61 43   CALL    $4361           
4356: 7E         LD      A,(HL)          
4357: E6 80      AND     $80             
4359: 23         INC     HL              
435A: 7E         LD      A,(HL)          
435B: C2 50 43   JP      NZ,$4350        
435E: 2B         DEC     HL              
435F: BB         CP      E               
4360: C9         RET                     

; HL = HL + (A-1)*2
4361: D5         PUSH    DE              
4362: EB         EX      DE,HL           
4363: 6F         LD      L,A             
4364: 2D         DEC     L               
4365: 26 00      LD      H,$00           
4367: 29         ADD     HL,HL           
4368: 19         ADD     HL,DE           
4369: D1         POP     DE              
436A: C9         RET                     

; HL = HL + (A-1)*4
436B: D5         PUSH    DE              
436C: EB         EX      DE,HL           
436D: 6F         LD      L,A             
436E: 2D         DEC     L               
436F: 26 00      LD      H,$00           
4371: 29         ADD     HL,HL           
4372: 29         ADD     HL,HL           
4373: 19         ADD     HL,DE           
4374: D1         POP     DE              
4375: C9         RET                     

; Set object's location
4376: CD 50 43   CALL    $4350           
4379: 23         INC     HL              
437A: 73         LD      (HL),E          
437B: 2B         DEC     HL              
437C: C9         RET                     
```

# Process Room Script

```code
; Process the user input against the script for a room
ProcessRoomScript: 
437D: 7E         LD      A,(HL)          
437E: A7         AND     A               
437F: C8         RET     Z               
4380: 3A 7C 46   LD      A,($467C)       
4383: BE         CP      (HL)            
4384: 23         INC     HL              
4385: CA 8F 43   JP      Z,$438F         
4388: 4E         LD      C,(HL)          
4389: 06 00      LD      B,$00           
438B: 09         ADD     HL,BC           
438C: C3 7D 43   JP      $437D           
438F: CD 96 43   CALL    $4396           
4392: C0         RET     NZ              
4393: C3 7D 43   JP      $437D           
```

# Run Script

```code
RunScript: 
4396: E5         PUSH    HL              
4397: 4E         LD      C,(HL)          
4398: 06 00      LD      B,$00           
439A: 09         ADD     HL,BC           
439B: E3         EX      (SP),HL         
439C: 23         INC     HL
;              
RunScriptCommand: 
439D: 7E         LD      A,(HL)          
439E: 23         INC     HL              
439F: E5         PUSH    HL              
43A0: 21 9F 50   LD      HL,$509F        
43A3: CD 61 43   CALL    $4361           
43A6: 7E         LD      A,(HL)          
43A7: 23         INC     HL              
43A8: 66         LD      H,(HL)          
43A9: 6F         LD      L,A             
43AA: E9         JP      (HL)            
```

# Script Command PASS

```code
ScriptCommandPASS:     
43AB: E1         POP     HL              
43AC: D1         POP     DE              
43AD: 7C         LD      A,H             
43AE: BA         CP      D               
43AF: C2 BA 43   JP      NZ,$43BA        
43B2: 7D         LD      A,L             
43B3: BB         CP      E               
43B4: C2 BA 43   JP      NZ,$43BA        
43B7: F6 01      OR      $01             
43B9: C9         RET                     
43BA: D5         PUSH    DE              
43BB: C3 9D 43   JP      $439D           
```

# Script Command FAIL

```code
ScriptCommandFAIL: 
43BE: E1         POP     HL              
43BF: E1         POP     HL              
43C0: AF         XOR     A               
43C1: C9         RET                     
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
43C2: E1         POP     HL              
43C3: CD 96 43   CALL    $4396           
43C6: E5         PUSH    HL              
43C7: CA AB 43   JP      Z,$43AB         
; The subscript failed. Bail out (with a PASS)
43CA: E1         POP     HL              
43CB: E1         POP     HL              
43CC: F6 01      OR      $01             
43CE: C9         RET                     
```

# Parse User Input

```code
ParseUserInput: 
43CF: CD 05 46   CALL    $4605           
43D2: CD A2 44   CALL    $44A2           
43D5: 2A AA 45   LD      HL,($45AA)      
43D8: 3A A8 45   LD      A,($45A8)       
43DB: 47         LD      B,A             
43DC: 3A 7D 46   LD      A,($467D)       
43DF: FE 03      CP      $03             
43E1: CA CF 43   JP      Z,$43CF         
43E4: 3A 7B 46   LD      A,($467B)       
43E7: A7         AND     A               
43E8: C2 1C 44   JP      NZ,$441C        
43EB: 3A 7C 46   LD      A,($467C)       
43EE: A7         AND     A               
43EF: C2 0D 44   JP      NZ,$440D        
43F2: 3A 7E 46   LD      A,($467E)       
43F5: 3C         INC     A               
43F6: E6 03      AND     $03             
43F8: 32 7E 46   LD      ($467E),A       
43FB: 21 7F 46   LD      HL,$467F        
43FE: 07         RLCA                    
43FF: 4F         LD      C,A             
4400: 06 00      LD      B,$00           
4402: 09         ADD     HL,BC           
4403: 7E         LD      A,(HL)          
4404: 23         INC     HL              
4405: 66         LD      H,(HL)          
4406: 6F         LD      L,A             
4407: CD D0 45   CALL    $45D0           
440A: C3 CF 43   JP      $43CF           
440D: 3A 7D 46   LD      A,($467D)       
4410: FE C0      CP      $C0             
4412: C8         RET     Z               
4413: 21 FD 46   LD      HL,$46FD        
4416: CD D0 45   CALL    $45D0           
4419: C3 CF 43   JP      $43CF           
441C: 22 AA 45   LD      ($45AA),HL      
441F: 3A A1 44   LD      A,($44A1)       
4422: A7         AND     A               
4423: C2 8E 44   JP      NZ,$448E        
4426: 7E         LD      A,(HL)          
4427: 23         INC     HL              
4428: 22 AA 45   LD      ($45AA),HL      
442B: 1E FF      LD      E,$FF           
442D: C5         PUSH    BC              
442E: CD 50 43   CALL    $4350           
4431: C1         POP     BC              
4432: CA 86 44   JP      Z,$4486         
4435: 3A 7D 46   LD      A,($467D)       
4438: FE 40      CP      $40             
443A: CA 4E 44   JP      Z,$444E         
443D: 2A AA 45   LD      HL,($45AA)      
4440: 2B         DEC     HL              
4441: 3A 3F 50   LD      A,($503F)       
4444: 5F         LD      E,A             
4445: 7E         LD      A,(HL)          
4446: C5         PUSH    BC              
4447: CD 50 43   CALL    $4350           
444A: C1         POP     BC              
444B: CA 86 44   JP      Z,$4486         
444E: 2A AA 45   LD      HL,($45AA)      
4451: 05         DEC     B               
4452: C2 26 44   JP      NZ,$4426        
4455: 3A 7D 46   LD      A,($467D)       
4458: FE 40      CP      $40             
445A: C2 63 44   JP      NZ,$4463        
445D: 21 98 46   LD      HL,$4698        
4460: C3 7C 44   JP      $447C           
4463: 21 87 46   LD      HL,$4687        
4466: CD D0 45   CALL    $45D0           
4469: 3E 01      LD      A,$01           
446B: 32 FB 46   LD      ($46FB),A       
446E: 21 D3 46   LD      HL,$46D3        
4471: CD D0 45   CALL    $45D0           
4474: 3E 3F      LD      A,$3F           
4476: 32 FB 46   LD      ($46FB),A       
4479: 21 91 46   LD      HL,$4691        
447C: CD D0 45   CALL    $45D0           
447F: 97         SUB     A               
4480: 32 7B 46   LD      ($467B),A       
4483: C3 CF 43   JP      $43CF           
4486: 2A AA 45   LD      HL,($45AA)      
4489: 2B         DEC     HL              
448A: 7E         LD      A,(HL)          
448B: 32 7B 46   LD      ($467B),A       
448E: 3A 7C 46   LD      A,($467C)       
4491: A7         AND     A               
4492: C0         RET     NZ              
4493: 21 B0 46   LD      HL,$46B0        
4496: CD D0 45   CALL    $45D0           
4499: 3E 01      LD      A,$01           
449B: 32 A1 44   LD      ($44A1),A       
449E: C3 CF 43   JP      $43CF
           
44A1: 00 ; 1 if there was a lone object last input 
                   
44A2: 21 5A 46   LD      HL,$465A        
44A5: 97         SUB     A               
44A6: 32 A9 45   LD      ($45A9),A       
44A9: 32 7D 46   LD      ($467D),A       
44AC: 11 CE 56   LD      DE,$56CE        
44AF: EB         EX      DE,HL           
44B0: 22 79 47   LD      ($4779),HL      
44B3: EB         EX      DE,HL           
44B4: 7E         LD      A,(HL)          
44B5: FE 20      CP      $20             
44B7: C2 BE 44   JP      NZ,$44BE        
44BA: 23         INC     HL              
44BB: C3 B4 44   JP      $44B4           
44BE: 22 7B 47   LD      ($477B),HL      
44C1: A7         AND     A               
44C2: CA 5C 45   JP      Z,$455C         
44C5: 3E 01      LD      A,$01           
44C7: 32 A9 45   LD      ($45A9),A       
44CA: E5         PUSH    HL              
44CB: 1A         LD      A,(DE)          
44CC: A7         AND     A               
44CD: CA 67 45   JP      Z,$4567         
44D0: 32 81 47   LD      ($4781),A       
44D3: E6 07      AND     $07             
44D5: 4F         LD      C,A             
44D6: 32 7D 47   LD      ($477D),A       
44D9: 3A 81 47   LD      A,($4781)       
44DC: E6 38      AND     $38             
44DE: 0F         RRCA                    
44DF: 0F         RRCA                    
44E0: 0F         RRCA                    
44E1: 47         LD      B,A             
44E2: EB         EX      DE,HL           
44E3: 22 79 47   LD      ($4779),HL      
44E6: EB         EX      DE,HL           
44E7: 13         INC     DE              
44E8: 1A         LD      A,(DE)          
44E9: BE         CP      (HL)            
44EA: C2 4E 45   JP      NZ,$454E        
44ED: 23         INC     HL              
44EE: 13         INC     DE              
44EF: 0D         DEC     C               
44F0: C2 E8 44   JP      NZ,$44E8        
44F3: 3A 7D 47   LD      A,($477D)       
44F6: FE 06      CP      $06             
44F8: CA 05 45   JP      Z,$4505         
44FB: 7E         LD      A,(HL)          
44FC: FE 20      CP      $20             
44FE: CA 13 45   JP      Z,$4513         
4501: A7         AND     A               
4502: C2 53 45   JP      NZ,$4553        
4505: 7E         LD      A,(HL)          
4506: FE 20      CP      $20             
4508: CA 13 45   JP      Z,$4513         
450B: A7         AND     A               
450C: CA 13 45   JP      Z,$4513         
450F: 23         INC     HL              
4510: C3 05 45   JP      $4505           
4513: 3A 81 47   LD      A,($4781)       
4516: E6 C0      AND     $C0             
4518: CA 2D 45   JP      Z,$452D         
451B: 32 7D 46   LD      ($467D),A       
451E: 1A         LD      A,(DE)          
451F: 32 7C 46   LD      ($467C),A       
4522: E5         PUSH    HL              
4523: 21 FD 46   LD      HL,$46FD        
4526: CD 85 45   CALL    $4585           
4529: E1         POP     HL              
452A: C3 46 45   JP      $4546           
452D: 1A         LD      A,(DE)          
452E: 32 7B 46   LD      ($467B),A       
4531: EB         EX      DE,HL           
4532: 22 AA 45   LD      ($45AA),HL      
4535: EB         EX      DE,HL           
4536: 78         LD      A,B             
4537: 32 A8 45   LD      ($45A8),A       
453A: 97         SUB     A               
453B: 32 A1 44   LD      ($44A1),A       
453E: E5         PUSH    HL              
453F: 21 D3 46   LD      HL,$46D3        
4542: CD 85 45   CALL    $4585           
4545: E1         POP     HL              
4546: 7E         LD      A,(HL)          
4547: FE 20      CP      $20             
4549: D1         POP     DE              
454A: CA AC 44   JP      Z,$44AC         
454D: C9         RET                     
454E: 13         INC     DE              
454F: 0D         DEC     C               
4550: C2 4E 45   JP      NZ,$454E        
4553: 13         INC     DE              
4554: 05         DEC     B               
4555: C2 53 45   JP      NZ,$4553        
4558: E1         POP     HL              
4559: C3 B4 44   JP      $44B4           
455C: 3A A9 45   LD      A,($45A9)       
455F: A7         AND     A               
4560: C0         RET     NZ              
4561: 3E 03      LD      A,$03           
4563: 32 7D 46   LD      ($467D),A       
4566: C9         RET                     
4567: E1         POP     HL              
4568: 97         SUB     A               
4569: 32 7C 46   LD      ($467C),A       
456C: 32 7B 46   LD      ($467B),A       
456F: 7E         LD      A,(HL)          
4570: FE 20      CP      $20             
4572: C2 79 45   JP      NZ,$4579        
4575: 23         INC     HL              
4576: C3 6F 45   JP      $456F           
4579: 7E         LD      A,(HL)          
457A: A7         AND     A               
457B: C8         RET     Z               
457C: FE 20      CP      $20             
457E: CA AC 44   JP      Z,$44AC         
4581: 23         INC     HL              
4582: C3 79 45   JP      $4579           
4585: EB         EX      DE,HL           
4586: 2A 7B 47   LD      HL,($477B)      
4589: 06 28      LD      B,$28           
458B: 7E         LD      A,(HL)          
458C: A7         AND     A               
458D: CA 9F 45   JP      Z,$459F         
4590: FE 20      CP      $20             
4592: CA 9F 45   JP      Z,$459F         
4595: 12         LD      (DE),A          
4596: 23         INC     HL              
4597: 13         INC     DE              
4598: 05         DEC     B               
4599: 78         LD      A,B             
459A: FE 01      CP      $01             
459C: C2 8B 45   JP      NZ,$458B        
459F: 3E 40      LD      A,$40           
45A1: 12         LD      (DE),A          
45A2: 13         INC     DE              
45A3: 05         DEC     B               
45A4: C2 9F 45   JP      NZ,$459F        
45A7: C9         RET                     

; RAM used in parsing input
45A8: 00             
45A9: 00                  
45AA: 00                   
45AB: 00                   
45AC: 00                   
45AD: 00 
```

# Print Packed

```code
PrintPacked: 
; Unpack a message (or multiple packed message) and print.
; HL is pointer to message                        
45AE: 7E         LD      A,(HL)          
45AF: A7         AND     A               
45B0: C8         RET     Z               
45B1: 23         INC     HL              
45B2: 11 5A 46   LD      DE,$465A        
45B5: CD C2 47   CALL    $47C2           
45B8: 7E         LD      A,(HL)          
45B9: A7         AND     A               
45BA: CA E7 45   JP      Z,$45E7         
45BD: FE 01      CP      $01             
45BF: C8         RET     Z               
45C0: 47         LD      B,A             
45C1: E5         PUSH    HL              
45C2: CD FF 45   CALL    $45FF           
45C5: E1         POP     HL              
45C6: 7E         LD      A,(HL)          
45C7: FE 0A      CP      $0A             
45C9: 23         INC     HL              
45CA: CA AE 45   JP      Z,$45AE         
45CD: C3 B8 45   JP      $45B8           

; HL points to message terminated by
;  - 0 : add a CR on the end and return
;  - 1 : no CR on the end and return
; Return with B holding last character (if any) sent to ROM routine.
;
45D0: 7E         LD      A,(HL)          
45D1: A7         AND     A               
45D2: CA E7 45   JP      Z,$45E7         
45D5: FE 01      CP      $01             
45D7: C8         RET     Z               
45D8: FE 40      CP      $40             
45DA: CA E3 45   JP      Z,$45E3         
45DD: 47         LD      B,A             
45DE: E5         PUSH    HL              
45DF: CD FF 45   CALL    $45FF           
45E2: E1         POP     HL              
45E3: 23         INC     HL              
45E4: C3 D0 45   JP      $45D0           
45E7: 06 0D      LD      B,$0D           
45E9: 78         LD      A,B             
45EA: CD FF 45   CALL    $45FF           
45ED: C9         RET                     
```

# Wait for Key

```code
WaitForKey: 
45EE: D5         PUSH    DE              
45EF: 3A 74 47   LD      A,($4774)       
45F2: 3C         INC     A               
45F3: 32 74 47   LD      ($4774),A       
45F6: CD 2B 00   CALL    $002B           
45F9: A7         AND     A               
45FA: CA EF 45   JP      Z,$45EF         
45FD: D1         POP     DE              
45FE: C9         RET                     
```

# Print Char

```code
PrintChar:    
45FF: D5         PUSH    DE              
4600: CD 33 00   CALL    $0033           
4603: D1         POP     DE              
4604: C9         RET                     
```

# Prompt And Read Line

```code
PromptAndReadLine: 
4605: 06 3A      LD      B,$3A           
4607: 78         LD      A,B             
4608: CD FF 45   CALL    $45FF           
460B: 21 5A 46   LD      HL,$465A        
460E: 0E 00      LD      C,$00           
;
4610: E5         PUSH    HL              
4611: C5         PUSH    BC              
4612: D5         PUSH    DE              
4613: CD EE 45   CALL    $45EE           
4616: D1         POP     DE              
4617: C1         POP     BC              
4618: E1         POP     HL              
4619: 47         LD      B,A             
461A: FE 08      CP      $08             
461C: CA 41 46   JP      Z,$4641         
461F: 77         LD      (HL),A          
4620: CD FF 45   CALL    $45FF           
4623: FE 0D      CP      $0D             
4625: CA 57 46   JP      Z,$4657         
4628: 0C         INC     C               
4629: 23         INC     HL              
462A: 11 7A 46   LD      DE,$467A        
462D: 7C         LD      A,H             
462E: BA         CP      D               
462F: DA 10 46   JP      C,$4610         
4632: 7D         LD      A,L             
4633: BB         CP      E               
4634: DA 10 46   JP      C,$4610         
4637: 06 08      LD      B,$08           
4639: 78         LD      A,B             
463A: CD FF 45   CALL    $45FF           
463D: 2B         DEC     HL              
463E: C3 10 46   JP      $4610           
4641: 2B         DEC     HL              
4642: 3E 46      LD      A,$46           
4644: BC         CP      H               
4645: DA 4E 46   JP      C,$464E         
4648: 7D         LD      A,L             
4649: FE 5A      CP      $5A             
464B: DA 0B 46   JP      C,$460B         
464E: 3E 08      LD      A,$08           
4650: 47         LD      B,A             
4651: CD FF 45   CALL    $45FF           
4654: C3 10 46   JP      $4610           
4657: 36 00      LD      (HL),$00        
4659: C9         RET                     
```

# Input Buffer

```code
; Input buffer (with some uninitialized leftover data!)
InputBuffer: 
;      A  N T  _  M  E  _  T  O  _  D  O  _  W  I  T
465A: 41 4E 54 20 4D 45 20 54 4F 20 44 4F 20 57 49 54             
;     H  _  T  H  E  _  ,  A  CR -- 0  0  0  0  _  _
466A: 48 20 54 48 45 20 2C 41 0D 12 30 30 30 30 20 20    

; Used in input parsing
467A: 00                   
467B: 00                    
467C: 00                   
467D: 00                    
467E: 00                   
;
467F: 25 47           
4681: 2C 47         
4683: 44 47       
4685: 58 47

; I_SEE_NO_
4687: 49 20 53 45 45 20 4E 4F 20 01

; _HERE.[CR]
4691: 20 48 45 52 45 2E 00

; YOU_AREN'T_CARRYING_IT.[CR]
4698: 59 4F 55 20 41 52 45 4E 27 54 20 43 41 52 52 59 49 4E 47 20 49 54 2E 00

; WHAT_DO_YOU_WANT_ME_TO_DO_WITH_THE_
46B0: 57 48 41 54 20 44 4F 20 59 4F 55 20 57 41 4E 54 20 4D 45 20 54 4F 20 44 4F 20 57 49 54 48 20 54
46D0: 48 45 20 
; 40 byte buffer for unknown noun word
46D3: 4F 57 20 54 48 41 54 20 57 4F 
46DD: 52 44 2E 00 49 20 44 4F 4E 27                
46E7: 54 20 55 4E 44 45 52 53 54 41            
46F1: 4E 44 2E 00 49 20 44 4F 4E 27
; "?"                   
46FB: 3F 00                 

; 40 byte buffer for unknown verb
46FD: 4B 4E 4F 57 20 57 48 41 54 20 
4707: 59 4F 55 20 4D 45 41 4E 2E 00
4711: 00 00 00 00 00 00 00 00 00 00                     
471B: 00 00 00 00 57 45 4C 43 4F 4D             

;" WHAT?",0
4725: 20 57 48 41 54 3F 00                  

; "I DON'T KNOW THAT WORD.",0
472C: 49 20 44 4F 4E 27 54 20 4B 4E 4F 57 20 54 48 41 54 20 57 4F 52 44 2E 00 

; "I DON'T UNDERSTAND.",0          
4744: 49 20 44 4F 4E 27 54 20 55 4E 44 45 52 53 54 41 4E 44 2E 00 
 
; "I DON'T KNOW WHAT YOU MEAN.",0          
4758: 49 20 44 4F 4E 27 54 20 4B 4E 4F 57 20 57 48 41 54 20 59 4F 55 20 4D 45 41 4E 2E 00  
          
4774: 00                    
4775: 00                              
4776: 00                              
4777: 00                              
4778: 00                              
4779: 00                              
477A: 00                              
477B: 00                              
477C: 00                              
477D: 00                              
477E: 00                              
477F: 00                              
4780: 00                              
4781: 00                              

; "WELCOME TO PYRAMID!!",0
4782: 57 45 4C 43 4F 4D 45 20 54 4F 20 50 59 52 41 4D 49 44 21 21 00 
        
4797: E1         POP     HL              
4798: CA B8 47   JP      Z,$47B8         
479B: 3E 00      LD      A,$00           
479D: CE 00      ADC     $00             
479F: 29         ADD     HL,HL           
47A0: 44         LD      B,H             
47A1: 85         ADD     A,L             
47A2: 2A 22 48   LD      HL,($4822)      
47A5: 95         SUB     L               
47A6: 4F         LD      C,A             
47A7: 78         LD      A,B             
47A8: 9C         SBC     H               
47A9: 47         LD      B,A             
47AA: C5         PUSH    BC              
47AB: D2 B0 47   JP      NC,$47B0        
47AE: 09         ADD     HL,BC           
47AF: E3         EX      (SP),HL         
47B0: 21 B7 47   LD      HL,$47B7        
47B3: 3F         CCF                     
47B4: C3 90 47   JP      $4790           
47B7: 00         NOP                     
47B8: 01 F9 47   LD      BC,$47F9        
47BB: 09         ADD     HL,BC           
47BC: 7E         LD      A,(HL)          
47BD: C1         POP     BC              
47BE: E1         POP     HL              
47BF: 00         NOP                     
47C0: 00         NOP                     
47C1: 00         NOP                     
47C2: 32 84 48   LD      ($4884),A       
47C5: 3E 01      LD      A,$01           
47C7: 32 87 48   LD      ($4887),A       
47CA: C3 D4 47   JP      $47D4           
47CD: 32 84 48   LD      ($4884),A       
47D0: 97         SUB     A               
47D1: 32 87 48   LD      ($4887),A       
47D4: E5         PUSH    HL              
47D5: 06 03      LD      B,$03           
47D7: E1         POP     HL              
47D8: 7E         LD      A,(HL)          
47D9: 23         INC     HL              
47DA: 4E         LD      C,(HL)          
47DB: 23         INC     HL              
47DC: E5         PUSH    HL              
47DD: 61         LD      H,C             
47DE: 6F         LD      L,A             
47DF: 13         INC     DE              
47E0: 13         INC     DE              
47E1: EB         EX      DE,HL           
47E2: E5         PUSH    HL              
47E3: C5         PUSH    BC              
47E4: 21 28 00   LD      HL,$0028        
47E7: 22 85 48   LD      ($4885),HL      
47EA: 21 1A 48   LD      HL,$481A        
47ED: 36 11      LD      (HL),$11        
47EF: 01 00 00   LD      BC,$0000        
47F2: C5         PUSH    BC              
47F3: 7B         LD      A,E             
47F4: 17         RLA                     
47F5: 5F         LD      E,A             
47F6: 7A         LD      A,D             
47F7: 17         RLA                     
47F8: 57         LD      D,A             
47F9: 35         DEC     (HL)            
47FA: E1         POP     HL              
47FB: CA 1B 48   JP      Z,$481B         
47FE: 3E 00      LD      A,$00           
4800: CE 00      ADC     $00             
4802: 29         ADD     HL,HL           
4803: 44         LD      B,H             
4804: 85         ADD     A,L             
4805: 2A 85 48   LD      HL,($4885)      
4808: 95         SUB     L               
4809: 4F         LD      C,A             
480A: 78         LD      A,B             
480B: 9C         SBC     H               
480C: 47         LD      B,A             
480D: C5         PUSH    BC              
480E: D2 13 48   JP      NC,$4813        
4811: 09         ADD     HL,BC           
4812: E3         EX      (SP),HL         
4813: 21 1A 48   LD      HL,$481A        
4816: 3F         CCF                     
4817: C3 F3 47   JP      $47F3           
481A: 00         NOP                     
481B: 01 5C 48   LD      BC,$485C        
481E: 09         ADD     HL,BC           
481F: 7E         LD      A,(HL)          
4820: C1         POP     BC              
4821: E1         POP     HL              
4822: 77         LD      (HL),A          
4823: 2B         DEC     HL              
4824: 05         DEC     B               
4825: C2 E2 47   JP      NZ,$47E2        
4828: 3A 87 48   LD      A,($4887)       
482B: A7         AND     A               
482C: CA 44 48   JP      Z,$4844         
482F: E5         PUSH    HL              
4830: C5         PUSH    BC              
4831: D5         PUSH    DE              
4832: 1E 03      LD      E,$03           
4834: 23         INC     HL              
4835: 46         LD      B,(HL)          
4836: E5         PUSH    HL              
4837: 78         LD      A,B             
4838: CD FF 45   CALL    $45FF           
483B: E1         POP     HL              
483C: 23         INC     HL              
483D: 1D         DEC     E               
483E: C2 35 48   JP      NZ,$4835        
4841: D1         POP     DE              
4842: C1         POP     BC              
4843: E1         POP     HL              
4844: EB         EX      DE,HL           
4845: 13         INC     DE              
4846: 3A 87 48   LD      A,($4887)       
4849: A7         AND     A               
484A: C2 50 48   JP      NZ,$4850        
484D: 13         INC     DE              
484E: 13         INC     DE              
484F: 13         INC     DE              
4850: 3A 84 48   LD      A,($4884)       
4853: 3D         DEC     A               
4854: 32 84 48   LD      ($4884),A       
4857: C2 D5 47   JP      NZ,$47D5        
485A: E1         POP     HL              
485B: C9         RET         
```
 
# Character Table

```code
; Character compression table
CharTable:            
485C: 3F 21 32 20 22 27 3C 3E 2F 30 33                 ; ?!2_"'<>/03 
4867: 41 42 43 44 45 46 47 48 49 4A 4B 4C 4D 4E 4F 50  ; ABCDEFGHIJKLMNOP
4877: 51 52 53 54 55 56 57 58 59 5A 2D 2C 2E           ; QRSTUVWXYZ-,.

; RAM used by unpack
4884: 00           
4885: 00                    
4886: 00                    
4887: 00
```
     
# Room Table

 Each entry is 4 bytes. The first word is the packed room description. 
 The second word is the room's command script.

```code
RoomTable:
;
; 81 rooms numbered starting at 1
;      Description   Script                
4888: DB 5B CC 49
488C: 10 5C E1 49
4890: 57 5C F2 49
4894: 57 5C 03 4A
4898: 57 5C 14 4A
489C: 57 5C 25 4A
48A0: 68 5C 36 4A
48A4: E2 5C 47 4A
48A8: 28 5D 58 4A
48AC: 7D 5D 69 4A
48B0: A0 5D 7E 4A
48B4: 1E 5E 87 4A
48B8: 8E 5E 9D 4A
48BC: 69 5F C8 4A
48C0: AB 5F D1 4A
48C4: 08 60 0D 4B
48C8: 3C 60 48 4B
48CC: 55 60 51 4B
48D0: 85 60 90 4B
48D4: F1 60 A9 4B
48D8: 5F 61 BE 4B
48DC: AC 61 C7 4B
48E0: D8 61 D8 4B
48E4: E0 61 E1 4B
48E8: 18 62 F2 4B
48EC: 58 62 07 4C
48F0: B0 62 14 4C
48F4: C8 62 21 4C
48F8: C8 62 36 4C
48FC: C8 62 47 4C
4900: C8 62 60 4C
4904: C8 62 69 4C
4908: C8 62 76 4C
490C: C8 62 87 4C
4910: C8 62 98 4C
4914: C8 62 B1 4C
4918: C8 62 C2 4C
491C: C8 62 CB 4C
4920: C8 62 DC 4C
4924: C8 62 E9 4C
4928: C8 62 F6 4C
492C: D8 61 03 4D
4930: D8 61 08 4D
4934: D8 61 0D 4D
4938: D8 61 12 4D
493C: D8 61 17 4D
4940: D8 61 1C 4D
4944: D8 61 21 4D
4948: D8 61 26 4D
494C: D8 61 2B 4D
4950: D8 61 30 4D
4954: EA 62 41 4D
4958: D8 61 56 4D
495C: 49 63 5B 4D
4960: A6 63 68 4D
4964: DA 63 75 4D
4968: 1F 64 93 4D
496C: 7A 64 9C 4D
4970: 0A 65 B1 4D
4974: A1 65 BE 4D
4978: D5 65 06 4E
497C: 82 66 21 4E
4980: E0 66 2A 4E
4984: 07 67 33 4E
4988: 29 67 3C 4E
498C: 89 67 65 4E
4990: 00 00 00 00
4994: D2 6B 3B 4F
4998: 00 00 00 00
499C: B1 6B 32 4F
49A0: 5C 6B 25 4F
49A4: 25 68 6E 4E
49A8: 82 68 77 4E
49AC: 00 00 00 00
49B0: 00 00 00 00
49B4: F6 68 86 4E
49B8: F3 6A 0E 4F
49BC: 3F 69 9B 4E
49C0: 21 6A A8 4E
49C4: 4B 6A B1 4E
49C8: 9D 6A BE 4E

  
49CC: 01 03 01   LD      BC,$0103        
49CF: 02         LD      (BC),A          
49D0: 02         LD      (BC),A          
49D1: 03         INC     BC              
49D2: 01 03 03   LD      BC,$0303        
49D5: 03         INC     BC              
49D6: 01 04 04   LD      BC,$0404        
49D9: 03         INC     BC              
49DA: 01 05 0B   LD      BC,$0B05        
49DD: 03         INC     BC              
49DE: 01 02 00   LD      BC,$0002        

49E1: 03         INC     BC              
49E2: 03         INC     BC              
49E3: 01 01 0A   LD      BC,$0A01        
49E6: 03         INC     BC              
49E7: 01 07 0C   LD      BC,$0C07        
49EA: 03         INC     BC              
49EB: 01 01 12   LD      BC,$1201        
49EE: 03         INC     BC              
49EF: 01 1A 00   LD      BC,$001A        
49F2: 01 03 01   LD      BC,$0103        
49F5: 06 02      LD      B,$02           
49F7: 03         INC     BC              
49F8: 01 03 03   LD      BC,$0303        
49FB: 03         INC     BC              
49FC: 01 04 04   LD      BC,$0404        
49FF: 03         INC     BC              
4A00: 01 01 00   LD      BC,$0001        
4A03: 01 03 01   LD      BC,$0103        
4A06: 01 02 03   LD      BC,$0302        
4A09: 01 03 03   LD      BC,$0303        
4A0C: 03         INC     BC              
4A0D: 01 04 04   LD      BC,$0404        
4A10: 03         INC     BC              
4A11: 01 05 00   LD      BC,$0005        
4A14: 01 03 01   LD      BC,$0103        
4A17: 06 02      LD      B,$02           
4A19: 03         INC     BC              
4A1A: 01 01 03   LD      BC,$0301        
4A1D: 03         INC     BC              
4A1E: 01 04 04   LD      BC,$0404        
4A21: 03         INC     BC              
4A22: 01 05 00   LD      BC,$0005        
4A25: 01 03 01   LD      BC,$0103        
4A28: 06 02      LD      B,$02           
4A2A: 03         INC     BC              
4A2B: 01 03 03   LD      BC,$0303        
4A2E: 03         INC     BC              
4A2F: 01 01 04   LD      BC,$0401        
4A32: 03         INC     BC              
4A33: 01 05 00   LD      BC,$0005        
4A36: 09         ADD     HL,BC           
4A37: 03         INC     BC              
4A38: 01 02 0C   LD      BC,$0C02        
4A3B: 03         INC     BC              
4A3C: 01 02 04   LD      BC,$0402        
4A3F: 03         INC     BC              
4A40: 01 08 0B   LD      BC,$0B08        
4A43: 03         INC     BC              
4A44: 01 08 00   LD      BC,$0008        
4A47: 02         LD      (BC),A          
4A48: 03         INC     BC              
4A49: 01 07 0C   LD      BC,$0C07        
4A4C: 03         INC     BC              
4A4D: 01 07 04   LD      BC,$0407        
4A50: 03         INC     BC              
4A51: 01 09 0B   LD      BC,$0B09        
4A54: 03         INC     BC              
4A55: 01 09 00   LD      BC,$0009        
4A58: 02         LD      (BC),A          
4A59: 03         INC     BC              
4A5A: 01 08 0B   LD      BC,$0B08        
4A5D: 03         INC     BC              
4A5E: 01 0A 09   LD      BC,$090A        
4A61: 03         INC     BC              
4A62: 01 0A 04   LD      BC,$040A        
4A65: 03         INC     BC              
4A66: 01 0A 00   LD      BC,$000A        
4A69: 0A         LD      A,(BC)          
4A6A: 03         INC     BC              
4A6B: 01 09 02   LD      BC,$0209        
4A6E: 03         INC     BC              
4A6F: 01 09 0B   LD      BC,$0B09        
4A72: 03         INC     BC              
4A73: 01 0B 04   LD      BC,$040B        
4A76: 03         INC     BC              
4A77: 01 0B 09   LD      BC,$090B        
4A7A: 03         INC     BC              
4A7B: 01 0B 00   LD      BC,$000B        
4A7E: 02         LD      (BC),A          
4A7F: 03         INC     BC              
4A80: 01 0A 04   LD      BC,$040A        
4A83: 03         INC     BC              
4A84: 01 0C 00   LD      BC,$000C        
4A87: 02         LD      (BC),A          
4A88: 03         INC     BC              
4A89: 01 0B 0A   LD      BC,$0A0B        
4A8C: 0B         DEC     BC              
4A8D: 07         RLCA                    
4A8E: 07         RLCA                    
4A8F: 02         LD      (BC),A          
4A90: 25         DEC     H               
4A91: 04         INC     B               
4A92: 71         LD      (HL),C          
4A93: 71         LD      (HL),C          
4A94: 05         DEC     B               
4A95: 01 0D 04   LD      BC,$040D        
4A98: 04         INC     B               
4A99: 04         INC     B               
4A9A: 96         SUB     (HL)            
4A9B: 71         LD      (HL),C          
4A9C: 00         NOP                     
4A9D: 03         INC     BC              
4A9E: 03         INC     BC              
4A9F: 01 0E 04   LD      BC,$040E        
4AA2: 03         INC     BC              
4AA3: 01 0F 0A   LD      BC,$0A0F        
4AA6: 03         INC     BC              
4AA7: 01 10 01   LD      BC,$0110        
4AAA: 03         INC     BC              
4AAB: 01 10 09   LD      BC,$0910        
4AAE: 0A         LD      A,(BC)          
4AAF: 07         RLCA                    
4AB0: 06 02      LD      B,$02           
4AB2: 25         DEC     H               
4AB3: 04         INC     B               
4AB4: B6         OR      (HL)            
4AB5: 71         LD      (HL),C          
4AB6: 01 0C 02   LD      BC,$020C        
4AB9: 0A         LD      A,(BC)          
4ABA: 07         RLCA                    
4ABB: 06 02      LD      B,$02           
4ABD: 25         DEC     H               
4ABE: 04         INC     B               
4ABF: B6         OR      (HL)            
4AC0: 71         LD      (HL),C          
4AC1: 01 0C 20   LD      BC,$200C        
4AC4: 03         INC     BC              
4AC5: 01 1A 00   LD      BC,$001A        
4AC8: 0C         INC     C               
4AC9: 03         INC     BC              
4ACA: 01 0D 01   LD      BC,$010D        
4ACD: 03         INC     BC              
4ACE: 01 0D 00   LD      BC,$000D        
4AD1: 02         LD      (BC),A          
4AD2: 03         INC     BC              
4AD3: 01 0D 10   LD      BC,$100D        
4AD6: 0C         INC     C               
4AD7: 07         RLCA                    
4AD8: 06 03      LD      B,$03           
4ADA: 01 04 C8   LD      BC,$C804        
4ADD: 71         LD      (HL),C          
4ADE: 04         INC     B               
4ADF: FA 71 05   JP      M,$0571         
4AE2: 04         INC     B               
4AE3: 0A         LD      A,(BC)          
4AE4: 07         RLCA                    
4AE5: 05         DEC     B               
4AE6: 03         INC     BC              
4AE7: 01 01 12   LD      BC,$1201        
4AEA: 04         INC     B               
4AEB: 09         ADD     HL,BC           
4AEC: 72         LD      (HL),D          
4AED: 0D         DEC     C               
4AEE: 05         DEC     B               
4AEF: 03         INC     BC              
4AF0: 01 01 12   LD      BC,$1201        
4AF3: 23         INC     HL              
4AF4: 18 11      JR      $4B07           
4AF6: 11 07 0C   LD      DE,$0C07        
4AF9: 03         INC     BC              
4AFA: 01 15 01   LD      BC,$0115        
4AFD: 00         NOP                     
4AFE: 15         DEC     D               
4AFF: 02         LD      (BC),A          
4B00: 00         NOP                     
4B01: 04         INC     B               
4B02: DE 7B      SBC     $7B             
4B04: 18 01      JR      $4B07           
4B06: 15         DEC     D               
4B07: 02         LD      (BC),A          
4B08: 12         LD      (DE),A          
4B09: 04         INC     B               
4B0A: F5         PUSH    AF              
4B0B: 7B         LD      A,E             
4B0C: 00         NOP                     
4B0D: 09         ADD     HL,BC           
4B0E: 03         INC     BC              
4B0F: 01 0D 02   LD      BC,$020D        
4B12: 03         INC     BC              
4B13: 01 0D 03   LD      BC,$030D        
4B16: 0A         LD      A,(BC)          
4B17: 07         RLCA                    
4B18: 06 03      LD      B,$03           
4B1A: 0B         DEC     BC              
4B1B: 04         INC     B               
4B1C: 27         DAA                     
4B1D: 72         LD      (HL),D          
4B1E: 01 11 01   LD      BC,$0111        
4B21: 0A         LD      A,(BC)          
4B22: 07         RLCA                    
4B23: 06 03      LD      B,$03           
4B25: 0B         DEC     BC              
4B26: 04         INC     B               
4B27: 27         DAA                     
4B28: 72         LD      (HL),D          
4B29: 01 19 04   LD      BC,$0419        
4B2C: 0A         LD      A,(BC)          
4B2D: 07         RLCA                    
4B2E: 06 03      LD      B,$03           
4B30: 0B         DEC     BC              
4B31: 04         INC     B               
4B32: 27         DAA                     
4B33: 72         LD      (HL),D          
4B34: 01 18 26   LD      BC,$2618        
4B37: 10 11      DJNZ    $4B4A           
4B39: 14         INC     D               
4B3A: 03         INC     BC              
4B3B: 0B         DEC     BC              
4B3C: 15         DEC     D               
4B3D: 0B         DEC     BC              
4B3E: 00         NOP                     
4B3F: 18 13      JR      $4B54           
4B41: 15         DEC     D               
4B42: 14         INC     D               
4B43: 00         NOP                     
4B44: 04         INC     B               
4B45: A1         AND     C               
4B46: 7C         LD      A,H             
4B47: 00         NOP                     
4B48: 01 03 01   LD      BC,$0103        
4B4B: 10 0C      DJNZ    $4B59           
4B4D: 03         INC     BC              
4B4E: 01 10 00   LD      BC,$0010        
4B51: 10 0C      DJNZ    $4B5F           
4B53: 07         RLCA                    
4B54: 06 03      LD      B,$03           
4B56: 02         LD      (BC),A          
4B57: 04         INC     B               
4B58: C8         RET     Z               
4B59: 71         LD      (HL),C          
4B5A: 04         INC     B               
4B5B: FA 71 05   JP      M,$0571         
4B5E: 02         LD      (BC),A          
4B5F: 0A         LD      A,(BC)          
4B60: 07         RLCA                    
4B61: 05         DEC     B               
4B62: 03         INC     BC              
4B63: 02         LD      (BC),A          
4B64: 01 0F 04   LD      BC,$040F        
4B67: 09         ADD     HL,BC           
4B68: 72         LD      (HL),D          
4B69: 01 06 04   LD      BC,$0406        
4B6C: 3D         DEC     A               
4B6D: 72         LD      (HL),D          
4B6E: 01 13 0D   LD      BC,$0D13        
4B71: 05         DEC     B               
4B72: 03         INC     BC              
4B73: 02         LD      (BC),A          
4B74: 01 0F 23   LD      BC,$230F        
4B77: 18 11      JR      $4B8A           
4B79: 11 07 0C   LD      DE,$0C07        
4B7C: 03         INC     BC              
4B7D: 02         LD      (BC),A          
4B7E: 15         DEC     D               
4B7F: 02         LD      (BC),A          
4B80: 00         NOP                     
4B81: 15         DEC     D               
4B82: 01 00 04   LD      BC,$0400        
4B85: DE 7B      SBC     $7B             
4B87: 18 02      JR      $4B8B           
4B89: 15         DEC     D               
4B8A: 01 0F 04   LD      BC,$040F        
4B8D: F5         PUSH    AF              
4B8E: 7B         LD      A,E             
4B8F: 00         NOP                     
4B90: 03         INC     BC              
4B91: 03         INC     BC              
4B92: 01 1C 09   LD      BC,$091C        
4B95: 03         INC     BC              
4B96: 01 1C 11   LD      BC,$111C        
4B99: 03         INC     BC              
4B9A: 01 1C 02   LD      BC,$021C        
4B9D: 03         INC     BC              
4B9E: 01 12 01   LD      BC,$0112        
4BA1: 03         INC     BC              
4BA2: 01 12 04   LD      BC,$0412        
4BA5: 03         INC     BC              
4BA6: 01 14 00   LD      BC,$0014        
4BA9: 02         LD      (BC),A          
4BAA: 03         INC     BC              
4BAB: 01 13 09   LD      BC,$0913        
4BAE: 03         INC     BC              
4BAF: 01 13 04   LD      BC,$0413        
4BB2: 03         INC     BC              
4BB3: 01 15 01   LD      BC,$0115        
4BB6: 03         INC     BC              
4BB7: 01 16 0A   LD      BC,$0A16        
4BBA: 03         INC     BC              
4BBB: 01 16 00   LD      BC,$0016        
4BBE: 02         LD      (BC),A          
4BBF: 03         INC     BC              
4BC0: 01 14 01   LD      BC,$0114        
4BC3: 03         INC     BC              
4BC4: 01 16 00   LD      BC,$0016        
4BC7: 04         INC     B               
4BC8: 03         INC     BC              
4BC9: 01 14 01   LD      BC,$0114        
4BCC: 03         INC     BC              
4BCD: 01 17 02   LD      BC,$0217        
4BD0: 03         INC     BC              
4BD1: 01 18 03   LD      BC,$0318        
4BD4: 03         INC     BC              
4BD5: 01 15 00   LD      BC,$0015        
4BD8: 03         INC     BC              
4BD9: 03         INC     BC              
4BDA: 01 16 0C   LD      BC,$0C16        
4BDD: 03         INC     BC              
4BDE: 01 16 00   LD      BC,$0016        
4BE1: 02         LD      (BC),A          
4BE2: 03         INC     BC              
4BE3: 01 10 0C   LD      BC,$0C10        
4BE6: 03         INC     BC              
4BE7: 01 10 04   LD      BC,$0410        
4BEA: 03         INC     BC              
4BEB: 01 16 09   LD      BC,$0916        
4BEE: 03         INC     BC              
4BEF: 01 16 00   LD      BC,$0016        
4BF2: 0C         INC     C               
4BF3: 03         INC     BC              
4BF4: 01 10 03   LD      BC,$0310        
4BF7: 03         INC     BC              
4BF8: 01 10 01   LD      BC,$0110        
4BFB: 03         INC     BC              
4BFC: 01 1A 20   LD      BC,$201A        
4BFF: 03         INC     BC              
4C00: 01 1A 0A   LD      BC,$0A1A        
4C03: 03         INC     BC              
4C04: 01 36 00   LD      BC,$0036        
4C07: 12         LD      (DE),A          
4C08: 03         INC     BC              
4C09: 01 02 03   LD      BC,$0302        
4C0C: 03         INC     BC              
4C0D: 01 19 02   LD      BC,$0219        
4C10: 03         INC     BC              
4C11: 01 1B 00   LD      BC,$001B        
4C14: 0A         LD      A,(BC)          
4C15: 03         INC     BC              
4C16: 01 1A 20   LD      BC,$201A        
4C19: 03         INC     BC              
4C1A: 01 1A 09   LD      BC,$091A        
4C1D: 03         INC     BC              
4C1E: 01 0D 00   LD      BC,$000D        
4C21: 01 03 01   LD      BC,$0103        
4C24: 1C         INC     E               
4C25: 02         LD      (BC),A          
4C26: 03         INC     BC              
4C27: 01 20 03   LD      BC,$0320        
4C2A: 03         INC     BC              
4C2B: 01 1E 04   LD      BC,$041E        
4C2E: 03         INC     BC              
4C2F: 01 1D 09   LD      BC,$091D        
4C32: 03         INC     BC              
4C33: 01 13 00   LD      BC,$0013        
4C36: 01 03 01   LD      BC,$0103        
4C39: 1C         INC     E               
4C3A: 02         LD      (BC),A          
4C3B: 03         INC     BC              
4C3C: 01 33 03   LD      BC,$0333        
4C3F: 03         INC     BC              
4C40: 01 1D 04   LD      BC,$041D        
4C43: 03         INC     BC              
4C44: 01 1D 00   LD      BC,$001D        
4C47: 01 03 01   LD      BC,$0103        
4C4A: 20 02      JR      NZ,$4C4E        
4C4C: 03         INC     BC              
4C4D: 01 2A 03   LD      BC,$032A        
4C50: 03         INC     BC              
4C51: 01 2B 04   LD      BC,$042B        
4C54: 03         INC     BC              
4C55: 01 1C 09   LD      BC,$091C        
4C58: 03         INC     BC              
4C59: 01 1F 0A   LD      BC,$0A1F        
4C5C: 03         INC     BC              
4C5D: 01 1F 00   LD      BC,$001F        
4C60: 09         ADD     HL,BC           
4C61: 03         INC     BC              
4C62: 01 1E 0A   LD      BC,$0A1E        
4C65: 03         INC     BC              
4C66: 01 1E 00   LD      BC,$001E        
4C69: 02         LD      (BC),A          
4C6A: 03         INC     BC              
4C6B: 01 1E 03   LD      BC,$031E        
4C6E: 03         INC     BC              
4C6F: 01 21 04   LD      BC,$0421        
4C72: 03         INC     BC              
4C73: 01 1C 00   LD      BC,$001C        
4C76: 01 03 01   LD      BC,$0103        
4C79: 2C         INC     L               
4C7A: 02         LD      (BC),A          
4C7B: 03         INC     BC              
4C7C: 01 20 03   LD      BC,$0320        
4C7F: 03         INC     BC              
4C80: 01 22 0A   LD      BC,$0A22        
4C83: 03         INC     BC              
4C84: 01 2D 00   LD      BC,$002D        
4C87: 02         LD      (BC),A          
4C88: 03         INC     BC              
4C89: 01 21 03   LD      BC,$0321        
4C8C: 03         INC     BC              
4C8D: 01 23 04   LD      BC,$0423        
4C90: 03         INC     BC              
4C91: 01 25 0A   LD      BC,$0A25        
4C94: 03         INC     BC              
4C95: 01 26 00   LD      BC,$0026        
4C98: 01 03 01   LD      BC,$0103        
4C9B: 24         INC     H               
4C9C: 02         LD      (BC),A          
4C9D: 03         INC     BC              
4C9E: 01 26 03   LD      BC,$0326        
4CA1: 03         INC     BC              
4CA2: 01 23 04   LD      BC,$0423        
4CA5: 03         INC     BC              
4CA6: 01 22 09   LD      BC,$0922        
4CA9: 03         INC     BC              
4CAA: 01 27 0A   LD      BC,$0A27        
4CAD: 03         INC     BC              
4CAE: 01 2F 00   LD      BC,$002F        
4CB1: 01 03 01   LD      BC,$0103        
4CB4: 24         INC     H               
4CB5: 02         LD      (BC),A          
4CB6: 03         INC     BC              
4CB7: 01 34 04   LD      BC,$0434        
4CBA: 03         INC     BC              
4CBB: 01 23 0A   LD      BC,$0A23        
4CBE: 03         INC     BC              
4CBF: 01 30 00   LD      BC,$0030        
4CC2: 02         LD      (BC),A          
4CC3: 03         INC     BC              
4CC4: 01 22 04   LD      BC,$0422        
4CC7: 03         INC     BC              
4CC8: 01 26 00   LD      BC,$0026        
4CCB: 02         LD      (BC),A          
4CCC: 03         INC     BC              
4CCD: 01 23 03   LD      BC,$0323        
4CD0: 03         INC     BC              
4CD1: 01 27 04   LD      BC,$0427        
4CD4: 03         INC     BC              
4CD5: 01 25 09   LD      BC,$0925        
4CD8: 03         INC     BC              
4CD9: 01 22 00   LD      BC,$0022        
4CDC: 01 03 01   LD      BC,$0103        
4CDF: 23         INC     HL              
4CE0: 03         INC     BC              
4CE1: 03         INC     BC              
4CE2: 01 2E 04   LD      BC,$042E        
4CE5: 03         INC     BC              
4CE6: 01 26 00   LD      BC,$0026        
4CE9: 01 03 01   LD      BC,$0103        
4CEC: 34         INC     (HL)            
4CED: 04         INC     B               
4CEE: 03         INC     BC              
4CEF: 01 29 08   LD      BC,$0829        
4CF2: 03         INC     BC              
4CF3: 01 35 00   LD      BC,$0035        
4CF6: 02         LD      (BC),A          
4CF7: 03         INC     BC              
4CF8: 01 28 03   LD      BC,$0328        
4CFB: 03         INC     BC              
4CFC: 01 34 04   LD      BC,$0434        
4CFF: 03         INC     BC              
4D00: 01 32 00   LD      BC,$0032        
4D03: 04         INC     B               
4D04: 03         INC     BC              
4D05: 01 1E 00   LD      BC,$001E        
4D08: 02         LD      (BC),A          
4D09: 03         INC     BC              
4D0A: 01 1E 00   LD      BC,$001E        
4D0D: 03         INC     BC              
4D0E: 03         INC     BC              
4D0F: 01 21 00   LD      BC,$0021        
4D12: 09         ADD     HL,BC           
4D13: 03         INC     BC              
4D14: 01 21 00   LD      BC,$0021        
4D17: 04         INC     B               
4D18: 03         INC     BC              
4D19: 01 27 00   LD      BC,$0027        
4D1C: 09         ADD     HL,BC           
4D1D: 03         INC     BC              
4D1E: 01 23 00   LD      BC,$0023        
4D21: 09         ADD     HL,BC           
4D22: 03         INC     BC              
4D23: 01 24 00   LD      BC,$0024        
4D26: 02         LD      (BC),A          
4D27: 03         INC     BC              
4D28: 01 34 00   LD      BC,$0034        
4D2B: 02         LD      (BC),A          
4D2C: 03         INC     BC              
4D2D: 01 29 00   LD      BC,$0029        
4D30: 04         INC     B               
4D31: 03         INC     BC              
4D32: 01 1D 21   LD      BC,$211D        
4D35: 0B         DEC     BC              
4D36: 11 29 15   LD      DE,$1529        
4D39: 29         ADD     HL,HL           
4D3A: 00         NOP                     
4D3B: 18 23      JR      $4D60           
4D3D: 04         INC     B               
4D3E: 58         LD      E,B             
4D3F: 7C         LD      A,H             
4D40: 00         NOP                     
4D41: 01 03 01   LD      BC,$0103        
4D44: 29         ADD     HL,HL           
4D45: 02         LD      (BC),A          
4D46: 03         INC     BC              
4D47: 01 28 03   LD      BC,$0328        
4D4A: 03         INC     BC              
4D4B: 01 31 04   LD      BC,$0431        
4D4E: 03         INC     BC              
4D4F: 01 24 0A   LD      BC,$0A24        
4D52: 03         INC     BC              
4D53: 01 0B 00   LD      BC,$000B        
4D56: 06 03      LD      B,$03           
4D58: 01 28 00   LD      BC,$0028        
4D5B: 02         LD      (BC),A          
4D5C: 03         INC     BC              
4D5D: 01 37 04   LD      BC,$0437        
4D60: 03         INC     BC              
4D61: 01 39 09   LD      BC,$0939        
4D64: 03         INC     BC              
4D65: 01 19 00   LD      BC,$0019        
4D68: 04         INC     B               
4D69: 03         INC     BC              
4D6A: 01 36 0A   LD      BC,$0A36        
4D6D: 03         INC     BC              
4D6E: 01 38 11   LD      BC,$1138        
4D71: 03         INC     BC              
4D72: 01 38 00   LD      BC,$0038        
4D75: 09         ADD     HL,BC           
4D76: 03         INC     BC              
4D77: 01 37 0C   LD      BC,$0C37        
4D7A: 03         INC     BC              
4D7B: 01 37 11   LD      BC,$1137        
4D7E: 03         INC     BC              
4D7F: 01 37 0A   LD      BC,$0A37        
4D82: 04         INC     B               
4D83: 04         INC     B               
4D84: 7B         LD      A,E             
4D85: 72         LD      (HL),D          
4D86: 27         DAA                     
4D87: 0B         DEC     BC              
4D88: 07         RLCA                    
4D89: 06 02      LD      B,$02           
4D8B: 1C         INC     E               
4D8C: 04         INC     B               
4D8D: 37         SCF                     
4D8E: 7B         LD      A,E             
4D8F: 19         ADD     HL,DE           
4D90: 1C         INC     E               
4D91: 1B         DEC     DE              
4D92: 00         NOP                     
4D93: 02         LD      (BC),A          
4D94: 03         INC     BC              
4D95: 01 36 0A   LD      BC,$0A36        
4D98: 03         INC     BC              
4D99: 01 3A 00   LD      BC,$003A        
4D9C: 01 03 01   LD      BC,$0103        
4D9F: 3D         DEC     A               
4DA0: 02         LD      (BC),A          
4DA1: 03         INC     BC              
4DA2: 01 3B 04   LD      BC,$043B        
4DA5: 03         INC     BC              
4DA6: 01 41 09   LD      BC,$0941        
4DA9: 03         INC     BC              
4DAA: 01 39 11   LD      BC,$1139        
4DAD: 03         INC     BC              
4DAE: 01 39 00   LD      BC,$0039        
4DB1: 02         LD      (BC),A          
4DB2: 03         INC     BC              
4DB3: 01 3C 04   LD      BC,$043C        
4DB6: 03         INC     BC              
4DB7: 01 41 09   LD      BC,$0941        
4DBA: 03         INC     BC              
4DBB: 01 3A 00   LD      BC,$003A        
4DBE: 01 07 07   LD      BC,$0707        
4DC1: 03         INC     BC              
4DC2: 0A         LD      A,(BC)          
4DC3: F0         RET     P               
4DC4: 01 3B 02   LD      BC,$023B        
4DC7: 07         RLCA                    
4DC8: 07         RLCA                    
4DC9: 03         INC     BC              
4DCA: 0A         LD      A,(BC)          
4DCB: F0         RET     P               
4DCC: 01 3B 03   LD      BC,$033B        
4DCF: 07         RLCA                    
4DD0: 07         RLCA                    
4DD1: 03         INC     BC              
4DD2: 0A         LD      A,(BC)          
4DD3: F0         RET     P               
4DD4: 01 3B 05   LD      BC,$053B        
4DD7: 07         RLCA                    
4DD8: 07         RLCA                    
4DD9: 03         INC     BC              
4DDA: 0A         LD      A,(BC)          
4DDB: F0         RET     P               
4DDC: 01 3B 06   LD      BC,$063B        
4DDF: 07         RLCA                    
4DE0: 07         RLCA                    
4DE1: 03         INC     BC              
4DE2: 0A         LD      A,(BC)          
4DE3: F0         RET     P               
4DE4: 01 3B 07   LD      BC,$073B        
4DE7: 07         RLCA                    
4DE8: 07         RLCA                    
4DE9: 03         INC     BC              
4DEA: 0A         LD      A,(BC)          
4DEB: F0         RET     P               
4DEC: 01 3B 08   LD      BC,$083B        
4DEF: 07         RLCA                    
4DF0: 07         RLCA                    
4DF1: 03         INC     BC              
4DF2: 0A         LD      A,(BC)          
4DF3: F0         RET     P               
4DF4: 01 3B 09   LD      BC,$093B        
4DF7: 07         RLCA                    
4DF8: 07         RLCA                    
4DF9: 03         INC     BC              
4DFA: 0A         LD      A,(BC)          
4DFB: F0         RET     P               
4DFC: 01 3B 04   LD      BC,$043B        
4DFF: 06 04      LD      B,$04           
4E01: CF         RST     0X08            
4E02: 72         LD      (HL),D          
4E03: 01 3C 00   LD      BC,$003C        
4E06: 03         INC     BC              
4E07: 11 07 06   LD      DE,$0607        
4E0A: 02         LD      (BC),A          
4E0B: 17         RLA                     
4E0C: 04         INC     B               
4E0D: 27         DAA                     
4E0E: 73         LD      (HL),E          
4E0F: 07         RLCA                    
4E10: 06 02      LD      B,$02           
4E12: 18 04      JR      $4E18           
4E14: 27         DAA                     
4E15: 73         LD      (HL),E          
4E16: 01 3A 09   LD      BC,$093A        
4E19: 03         INC     BC              
4E1A: 01 3E 0A   LD      BC,$0A3E        
4E1D: 03         INC     BC              
4E1E: 01 3F 00   LD      BC,$003F        
4E21: 0A         LD      A,(BC)          
4E22: 03         INC     BC              
4E23: 01 3D 0C   LD      BC,$0C3D        
4E26: 03         INC     BC              
4E27: 01 3D 00   LD      BC,$003D        
4E2A: 09         ADD     HL,BC           
4E2B: 03         INC     BC              
4E2C: 01 3D 0A   LD      BC,$0A3D        
4E2F: 03         INC     BC              
4E30: 01 40 00   LD      BC,$0040        
4E33: 09         ADD     HL,BC           
4E34: 03         INC     BC              
4E35: 01 3F 0C   LD      BC,$0C3F        
4E38: 03         INC     BC              
4E39: 01 3F 00   LD      BC,$003F        
4E3C: 02         LD      (BC),A          
4E3D: 03         INC     BC              
4E3E: 01 3A 04   LD      BC,$043A        
4E41: 03         INC     BC              
4E42: 01 4E 09   LD      BC,$094E        
4E45: 07         RLCA                    
4E46: 07         RLCA                    
4E47: 03         INC     BC              
4E48: 0A         LD      A,(BC)          
4E49: CC 01 48   CALL    Z,$4801         
4E4C: 01 07 07   LD      BC,$0707        
4E4F: 03         INC     BC              
4E50: 0A         LD      A,(BC)          
4E51: CC 01 49   CALL    Z,$4901         
4E54: 03         INC     BC              
4E55: 07         RLCA                    
4E56: 07         RLCA                    
4E57: 03         INC     BC              
4E58: 0A         LD      A,(BC)          
4E59: CC 01 42   CALL    Z,$4201         
4E5C: 0A         LD      A,(BC)          
4E5D: 07         RLCA                    
4E5E: 07         RLCA                    
4E5F: 03         INC     BC              
4E60: 0A         LD      A,(BC)          
4E61: CC 01 3B   CALL    Z,$3B01         
4E64: 00         NOP                     
4E65: 01 03 01   LD      BC,$0103        
4E68: 41         LD      B,C             
4E69: 03         INC     BC              
4E6A: 03         INC     BC              
4E6B: 01 50 00   LD      BC,$0050        
4E6E: 04         INC     B               
4E6F: 03         INC     BC              
4E70: 01 41 0C   LD      BC,$0C41        
4E73: 03         INC     BC              
4E74: 01 41 00   LD      BC,$0041        
4E77: 04         INC     B               
4E78: 09         ADD     HL,BC           
4E79: 07         RLCA                    
4E7A: 04         INC     B               
4E7B: 0D         DEC     C               
4E7C: 01 4C 04   LD      BC,$044C        
4E7F: 53         LD      D,E             
4E80: 73         LD      (HL),E          
4E81: 06 03      LD      B,$03           
4E83: 01 41 00   LD      BC,$0041        
4E86: 02         LD      (BC),A          
4E87: 09         ADD     HL,BC           
4E88: 07         RLCA                    
4E89: 04         INC     B               
4E8A: 0D         DEC     C               
4E8B: 01 49 04   LD      BC,$0449        
4E8E: 53         LD      D,E             
4E8F: 73         LD      (HL),E          
4E90: 0C         INC     C               
4E91: 09         ADD     HL,BC           
4E92: 07         RLCA                    
4E93: 04         INC     B               
4E94: 0D         DEC     C               
4E95: 01 49 04   LD      BC,$0449        
4E98: 53         LD      D,E             
4E99: 73         LD      (HL),E          
4E9A: 00         NOP                     
4E9B: 02         LD      (BC),A          
4E9C: 03         INC     BC              
4E9D: 01 41 04   LD      BC,$0441        
4EA0: 03         INC     BC              
4EA1: 01 50 0A   LD      BC,$0A50        
4EA4: 03         INC     BC              
4EA5: 01 4F 00   LD      BC,$004F        
4EA8: 09         ADD     HL,BC           
4EA9: 03         INC     BC              
4EAA: 01 4E 0C   LD      BC,$0C4E        
4EAD: 03         INC     BC              
4EAE: 01 4E 00   LD      BC,$004E        
4EB1: 02         LD      (BC),A          
4EB2: 03         INC     BC              
4EB3: 01 4E 04   LD      BC,$044E        
4EB6: 03         INC     BC              
4EB7: 01 42 0A   LD      BC,$0A42        
4EBA: 03         INC     BC              
4EBB: 01 51 00   LD      BC,$0051        
4EBE: 09         ADD     HL,BC           
4EBF: 03         INC     BC              
4EC0: 01 50 0C   LD      BC,$0C50        
4EC3: 03         INC     BC              
4EC4: 01 50 11   LD      BC,$1150        
4EC7: 16 07      LD      D,$07           
4EC9: 08         EX      AF,AF'          
4ECA: 03         INC     BC              
4ECB: 09         ADD     HL,BC           
4ECC: 04         INC     B               
4ECD: 9E         SBC     (HL)            
4ECE: 73         LD      (HL),E          
4ECF: 01 4D 07   LD      BC,$074D        
4ED2: 06 03      LD      B,$03           
4ED4: 08         EX      AF,AF'          
4ED5: 04         INC     B               
4ED6: CB 73      SET     1,E             
4ED8: 01 50 04   LD      BC,$0450        
4EDB: 7D         LD      A,L             
4EDC: 7D         LD      A,L             
4EDD: 24         INC     H               
4EDE: 2F         CPL                     
4EDF: 11 1C 15   LD      DE,$151C        
4EE2: 1C         INC     E               
4EE3: 00         NOP                     
4EE4: 07         RLCA                    
4EE5: 0E 03      LD      C,$03           
4EE7: 07         RLCA                    
4EE8: 15         DEC     D               
4EE9: 07         RLCA                    
4EEA: 00         NOP                     
4EEB: 18 08      JR      $4EF5           
4EED: 04         INC     B               
4EEE: 02         LD      (BC),A          
4EEF: 7D         LD      A,L             
4EF0: 04         INC     B               
4EF1: 71         LD      (HL),C          
4EF2: 6E         LD      L,(HL)          
4EF3: 07         RLCA                    
4EF4: 0E 03      LD      C,$03           
4EF6: 08         EX      AF,AF'          
4EF7: 15         DEC     D               
4EF8: 08         EX      AF,AF'          
4EF9: 00         NOP                     
4EFA: 18 09      JR      $4F05           
4EFC: 04         INC     B               
4EFD: 29         ADD     HL,HL           
4EFE: 7D         LD      A,L             
4EFF: 04         INC     B               
4F00: B1         OR      C               
4F01: 6E         LD      L,(HL)          
4F02: 15         DEC     D               
4F03: 09         ADD     HL,BC           
4F04: 00         NOP                     
4F05: 18 07      JR      $4F0E           
4F07: 04         INC     B               
4F08: 59         LD      E,C             
4F09: 7D         LD      A,L             
4F0A: 04         INC     B               
4F0B: 45         LD      B,L             
4F0C: 6E         LD      L,(HL)          
4F0D: 00         NOP                     
4F0E: 02         LD      (BC),A          
4F0F: 03         INC     BC              
4F10: 01 51 0A   LD      BC,$0A51        
4F13: 03         INC     BC              
4F14: 01 51 11   LD      BC,$1151        
4F17: 03         INC     BC              
4F18: 01 51 10   LD      BC,$1051        
4F1B: 05         DEC     B               
4F1C: 04         INC     B               
4F1D: 71         LD      (HL),C          
4F1E: 71         LD      (HL),C          
4F1F: 05         DEC     B               
4F20: 04         INC     B               
4F21: 03         INC     BC              
4F22: 01 47 00   LD      BC,$0047        
4F25: 01 03 01   LD      BC,$0103        
4F28: 44         LD      B,H             
4F29: 02         LD      (BC),A          
4F2A: 03         INC     BC              
4F2B: 01 46 03   LD      BC,$0346        
4F2E: 03         INC     BC              
4F2F: 01 4D 00   LD      BC,$004D        
4F32: 03         INC     BC              
4F33: 03         INC     BC              
4F34: 01 47 0C   LD      BC,$0C47        
4F37: 03         INC     BC              
4F38: 01 47 00   LD      BC,$0047        
4F3B: 03         INC     BC              
4F3C: 03         INC     BC              
4F3D: 01 47 0C   LD      BC,$0C47        
4F40: 03         INC     BC              
4F41: 01 47 00   LD      BC,$0047        
4F44: FF         RST     0X38           
```

# Ambient Light Table 

```code
; 2 bytes per room
; * 0x4000 means there is light in the room (no need for a lamp)
; * 0x0000 means you better have a lamp

AmbientLight: 
4F45: 40         LD      B,B             
4F46: 00         NOP                     
4F47: 40         LD      B,B             
4F48: 00         NOP                     
4F49: 40         LD      B,B             
4F4A: 00         NOP                     
4F4B: 40         LD      B,B             
4F4C: 00         NOP                     
4F4D: 40         LD      B,B             
4F4E: 00         NOP                     
4F4F: 40         LD      B,B             
4F50: 00         NOP                     
4F51: 40         LD      B,B             
4F52: 00         NOP                     
4F53: 00         NOP                     
4F54: 00         NOP                     
4F55: 00         NOP                     
4F56: 00         NOP                     
4F57: 00         NOP                     
4F58: 00         NOP                     
4F59: 00         NOP                     
4F5A: 00         NOP                     
4F5B: 00         NOP                     
4F5C: 00         NOP                     
4F5D: 00         NOP                     
4F5E: 00         NOP                     
4F5F: 00         NOP                     
4F60: 00         NOP                     
4F61: 00         NOP                     
4F62: 00         NOP                     
4F63: 00         NOP                     
4F64: 00         NOP                     
4F65: 00         NOP                     
4F66: 00         NOP                     
4F67: 00         NOP                     
4F68: 00         NOP                     
4F69: 00         NOP                     
4F6A: 00         NOP                     
4F6B: 00         NOP                     
4F6C: 00         NOP                     
4F6D: 00         NOP                     
4F6E: 00         NOP                     
4F6F: 00         NOP                     
4F70: 00         NOP                     
4F71: 00         NOP                     
4F72: 00         NOP                     
4F73: 00         NOP                     
4F74: 00         NOP                     
4F75: 00         NOP                     
4F76: 00         NOP                     
4F77: 00         NOP                     
4F78: 00         NOP                     
4F79: 00         NOP                     
4F7A: 00         NOP                     
4F7B: 00         NOP                     
4F7C: 00         NOP                     
4F7D: 00         NOP                     
4F7E: 00         NOP                     
4F7F: 00         NOP                     
4F80: 00         NOP                     
4F81: 00         NOP                     
4F82: 00         NOP                     
4F83: 00         NOP                     
4F84: 00         NOP                     
4F85: 00         NOP                     
4F86: 00         NOP                     
4F87: 00         NOP                     
4F88: 00         NOP                     
4F89: 00         NOP                     
4F8A: 00         NOP                     
4F8B: 00         NOP                     
4F8C: 00         NOP                     
4F8D: 00         NOP                     
4F8E: 00         NOP                     
4F8F: 00         NOP                     
4F90: 00         NOP                     
4F91: 00         NOP                     
4F92: 00         NOP                     
4F93: 00         NOP                     
4F94: 00         NOP                     
4F95: 00         NOP                     
4F96: 00         NOP                     
4F97: 00         NOP                     
4F98: 00         NOP                     
4F99: 00         NOP                     
4F9A: 00         NOP                     
4F9B: 00         NOP                     
4F9C: 00         NOP                     
4F9D: 00         NOP                     
4F9E: 00         NOP                     
4F9F: 00         NOP                     
4FA0: 00         NOP                     
4FA1: 00         NOP                     
4FA2: 00         NOP                     
4FA3: 00         NOP                     
4FA4: 00         NOP                     
4FA5: 00         NOP                     
4FA6: 00         NOP                     
4FA7: 00         NOP                     
4FA8: 00         NOP                     
4FA9: 00         NOP                     
4FAA: 00         NOP                     
4FAB: 00         NOP                     
4FAC: 00         NOP                     
4FAD: 00         NOP                     
4FAE: 00         NOP                     
4FAF: 00         NOP                     
4FB0: 00         NOP                     
4FB1: 00         NOP                     
4FB2: 00         NOP                     
4FB3: 00         NOP                     
4FB4: 00         NOP                     
4FB5: 00         NOP                     
4FB6: 00         NOP                     
4FB7: 00         NOP                     
4FB8: 00         NOP                     
4FB9: 00         NOP                     
4FBA: 00         NOP                     
4FBB: 00         NOP                     
4FBC: 00         NOP                     
4FBD: 00         NOP                     
4FBE: 00         NOP                     
4FBF: 00         NOP                     
4FC0: 00         NOP                     
4FC1: 00         NOP                     
4FC2: 00         NOP                     
4FC3: 00         NOP                     
4FC4: 00         NOP                     
4FC5: 00         NOP                     
4FC6: 00         NOP                     
4FC7: 00         NOP                     
4FC8: 00         NOP                     
4FC9: 00         NOP                     
4FCA: 00         NOP                     
4FCB: 00         NOP                     
4FCC: 00         NOP                     
4FCD: 00         NOP                     
4FCE: 00         NOP                     
4FCF: 00         NOP                     
4FD0: 00         NOP                     
4FD1: 00         NOP                     
4FD2: 00         NOP                     
4FD3: 00         NOP                     
4FD4: 00         NOP                     
4FD5: 00         NOP                     
4FD6: 00         NOP                     
4FD7: 00         NOP                     
4FD8: 00         NOP                     
4FD9: 00         NOP                     
4FDA: 00         NOP                     
4FDB: 40         LD      B,B             
4FDC: 00         NOP                     
4FDD: 00         NOP                     
4FDE: 00         NOP                     
4FDF: 00         NOP                     
4FE0: 00         NOP                     
4FE1: 00         NOP                     
4FE2: 00         NOP                     
4FE3: 00         NOP                     
4FE4: 00         NOP                     
4FE5: 00         NOP                     
4FE6: 00         NOP   
```

# Object Data

```code
; This two-byte table contains the object's attributes ("isTreasure" and "isGettable") 
; and the object's current location (a room or inside another object).
;
; The code references the objects by numeric id, but I have given them unique names 
; in the table below. All object names begin with "#". All word names begin with "_".
;
; The format of the two bytes are:
;
;   MCT----- RRRRRRRR
;
;   M - if set, the second byte is an object number (container). if clear, the second byte is a room number.[[br]] 
;   C - if set, object can be picked up.[[br]]
;   T - if set, object is treasure.
;
;   RRRRRRRR - Second byte is the object's location (containing object or room number).

ObjectData:
; Object data table (2 bytes)
;              MCT              # Name             Start location                  
4FE7: 00         NOP                     
4FE8: 00         NOP                     
4FE9: 00         NOP                     
4FEA: 00         NOP                     
4FEB: 00         NOP                     
4FEC: 00         NOP                     
4FED: 00         NOP                     
4FEE: 00         NOP                     
4FEF: 00         NOP                     
4FF0: 00         NOP                     
4FF1: 00         NOP                     
4FF2: 33         INC     SP              
4FF3: 00         NOP                     
4FF4: 51         LD      D,C             
4FF5: 00         NOP                     
4FF6: 00         NOP                     
4FF7: 00         NOP                     
4FF8: 00         NOP                     
4FF9: 00         NOP                     
4FFA: 00         NOP                     
4FFB: 00         NOP                     
4FFC: 10 00      DJNZ    $4FFE           
4FFE: 00         NOP                     
4FFF: 00         NOP                     
5000: 00         NOP                     
5001: 40         LD      B,B             
5002: 02         LD      (BC),A          
5003: 40         LD      B,B             
5004: 00         NOP                     
5005: 40         LD      B,B             
5006: 08         EX      AF,AF'          
5007: 40         LD      B,B             
5008: 09         ADD     HL,BC           
5009: 40         LD      B,B             
500A: 48         LD      C,B             
500B: 40         LD      B,B             
500C: 0B         DEC     BC              
500D: 00         NOP                     
500E: 00         NOP                     
500F: 00         NOP                     
5010: 00         NOP                     
5011: 60         LD      H,B             
5012: 00         NOP                     
5013: 40         LD      B,B             
5014: 3D         DEC     A               
5015: 40         LD      B,B             
5016: 00         NOP                     
5017: 40         LD      B,B             
5018: 3B         DEC     SP              
5019: 40         LD      B,B             
501A: 02         LD      (BC),A          
501B: 40         LD      B,B             
501C: 02         LD      (BC),A          
501D: C0         RET     NZ              
501E: 1B         DEC     DE              
501F: 00         NOP                     
5020: 00         NOP                     
5021: 00         NOP                     
5022: 38 60      JR      C,$5084         
5024: 4C         LD      C,H             
5025: 60         LD      H,B             
5026: 00         NOP                     
5027: 60         LD      H,B             
5028: 49         LD      C,C             
5029: 60         LD      H,B             
502A: 44         LD      B,H             
502B: 40         LD      B,B             
502C: 00         NOP                     
502D: 40         LD      B,B             
502E: 00         NOP                     
502F: 60         LD      H,B             
5030: 0E 60      LD      C,$60           
5032: 11 60 19   LD      DE,$1960        
5035: 60         LD      H,B             
5036: 12         LD      (DE),A          
5037: 60         LD      H,B             
5038: 18 60      JR      $509A           
503A: 00         NOP                     
503B: 60         LD      H,B             
503C: 47         LD      B,A             
503D: 40         LD      B,B             
503E: 00         NOP
```

# Game Variables                      

```code
GameVariables:
503F: 01 00 00   LD      BC,$0000        
5042: 00         NOP                     
5043: 00         NOP                     
5044: 00         NOP                     
5045: 00         NOP                     
5046: 00         NOP                     
```

# Object Table

```code
ObjectDescriptions:
; Object descriptions (44 objects)
; For packable objects each slot points to a message pair. The first is the long
; description and the second is the short (if any).
;                  # Name              Description
5047: 58         LD      E,B             
5048: 6D         LD      L,L             
5049: 58         LD      E,B             
504A: 6D         LD      L,L             
504B: C0         RET     NZ              
504C: 47         LD      B,A             
504D: C0         RET     NZ              
504E: 47         LD      B,A             
504F: C0         RET     NZ              
5050: 47         LD      B,A             
5051: E1         POP     HL              
5052: 6E         LD      L,(HL)          
5053: 45         LD      B,L             
5054: 6E         LD      L,(HL)          
5055: 71         LD      (HL),C          
5056: 6E         LD      L,(HL)          
5057: B1         OR      C               
5058: 6E         LD      L,(HL)          
5059: 00         NOP                     
505A: 00         NOP                     
505B: 3A 6D 00   LD      A,($006D)       
505E: 00         NOP                     
505F: 00         NOP                     
5060: 00         NOP                     
5061: 2E 6C      LD      L,$6C           
5063: 53         LD      D,E             
5064: 6C         LD      L,H             
5065: 75         LD      (HL),L          
5066: 6C         LD      L,H             
5067: 9E         SBC     (HL)            
5068: 6C         LD      L,H             
5069: 12         LD      (DE),A          
506A: 6D         LD      L,L             
506B: CD 6C EB   CALL    $EB6C           
506E: 6C         LD      L,H             
506F: ED                              
5070: 70         LD      (HL),B          
5071: 47         LD      B,A             
5072: 71         LD      (HL),C          
5073: 78         LD      A,B             
5074: 6D         LD      L,L             
5075: 78         LD      A,B             
5076: 6D         LD      L,L             
5077: B1         OR      C               
5078: 6D         LD      L,L             
5079: EC 6D 04   CALL    PE,$046D        
507C: 6E         LD      L,(HL)          
507D: 20 6E      JR      NZ,$50ED        
507F: C0         RET     NZ              
5080: 47         LD      B,A             
5081: C0         RET     NZ              
5082: 47         LD      B,A             
5083: 14         INC     D               
5084: 71         LD      (HL),C          
5085: C5         PUSH    BC              
5086: 70         LD      (HL),B          
5087: A2         AND     D               
5088: 70         LD      (HL),B          
5089: 7E         LD      A,(HL)          
508A: 70         LD      (HL),B          
508B: 30 6F      JR      NC,$50FC        
508D: 4F         LD      C,A             
508E: 6F         LD      L,A             
508F: 7B         LD      A,E             
5090: 6F         LD      L,A             
5091: AB         XOR     E               
5092: 6F         LD      L,A             
5093: CA 6F EA   JP      Z,$EA6F         
5096: 6F         LD      L,A             
5097: 0E 70      LD      C,$70           
5099: 2B         DEC     HL              
509A: 70         LD      (HL),B          
509B: 52         LD      D,D             
509C: 70         LD      (HL),B          
509D: 2E 6C      LD      L,$6C           
```

# Script Commands 

```code
; This lookup table holds the pointers to the individual script commands. Each command 
; reads 1 or 2 bytes of data from the script. The number of extra bytes read is show 
; for reference in the table.
;
; Script Command Table
; *   b = 2 bytes ... message address
; *   c = 1 byte  ... object number
; *   d = 1 byte  ... room number
; *   e = 2 bytes ... target object and container object 
; *   f = 2 bytes ... target object and room number

ScriptCommands:
;    Address   Number Bytes Type Name
509F: 8A 51   ;   1     1    d   MoveToRoomX           
50A1: C8 52   ;   2     1    c   AssertObjectXIsInPack
50A3: D7 52   ;   3     1    c   AssertObjectXIsInCurrentRoomOrPack
50A5: 5E 53   ;   4     2    b   PrintMessageX
50A7: 49 54   ;   5     0        PrintScoreAndStop
50A9: 00 00   ;   6     -        
50AB: C2 43   ;   7     1    *   SubScripXtAbortIfPass 
50AD: C7 54   ;   8     0        PrintScore
50AF: EF 55   ;   9     0        PrintScoreAndStop
50B1: 18 53   ;  10     1        AssertRandomIsGreaterThanX
50B3: 6B 53   ;  11     1    c   DropObjectX
50B5: 32 53   ;  12     1    d   MoveToRoomXIfItWasLastRoom
50B7: FB 52   ;  13     0        AssertPackIsEmptyExceptForEmerald
50B9: 81 53   ;  14     0        MoveToLastRoom
50BB: 9B 53   ;  15     0        PrintInventory    
50BD: DB 53   ;  16     0        PrintRoomDescription
50BF: E1 53   ;  17     1    c   AssertObjectXMatchesUserInput
50C1: EF 53   ;  18     1    c   GetObjectFromRoom
50C3: 00 00   ;  19     -        
50C5: 2B 54   ;  20     0        PrintOK 
50C7: 34 54   ;  21     2    f   MoveObjectXToRoomY
50C9: 43 53   ;  22     0        GetUserInputObject
50CB: 24 54   ;  23     0        DropUserInputObject
50CD: A5 52   ;  24     1    c   MoveObjectXToCurrentRoom
50CF: B3 52   ;  25     2    e   MoveObjectXIntoContainerY
50D1: EA 52   ;  26     1    c   AssertObjectXIsInCurrentRoom
50D3: F5 55   ;  27     0        LoadGame  
50D5: 54 56   ;  28     0        SaveGame 
50D7: 94 56   ;  29     0        RandomizeDirections
```

# After Every Step 

```code
; This processing takes place after every user input.[[br]]
;  1. Increment the count on the lamp and the number of turns.[[br]]
;  2.  Warn the player if the lamp is going dim and change the batteries automatically.
     
50D9: 3E 0F      LD      A,$0F           
50DB: 21 E7 4F   LD      HL,$4FE7        
50DE: CD 61 43   CALL    $4361           
50E1: 23         INC     HL              
50E2: 7E         LD      A,(HL)          
50E3: A7         AND     A               
50E4: CA 34 51   JP      Z,$5134         
50E7: 2A 42 50   LD      HL,($5042)      
50EA: 23         INC     HL              
50EB: 22 42 50   LD      ($5042),HL      
50EE: 7C         LD      A,H             
50EF: FE 01      CP      $01             
50F1: C2 34 51   JP      NZ,$5134        
50F4: 7D         LD      A,L             
50F5: FE 22      CP      $22             
50F7: C2 03 51   JP      NZ,$5103        
50FA: 21 C5 79   LD      HL,$79C5        
50FD: CD AE 45   CALL    $45AE           
5100: C3 77 51   JP      $5177           
5103: FE 36      CP      $36             
5105: C2 34 51   JP      NZ,$5134        
5108: 3E 0F      LD      A,$0F           
510A: 21 E7 4F   LD      HL,$4FE7        
510D: CD 61 43   CALL    $4361           
5110: 23         INC     HL              
5111: 46         LD      B,(HL)          
5112: 36 00      LD      (HL),$00        
5114: 21 E7 4F   LD      HL,$4FE7        
5117: 3E 2C      LD      A,$2C           
5119: CD 61 43   CALL    $4361           
511C: 23         INC     HL              
511D: 70         LD      (HL),B          
511E: 3E 23      LD      A,$23           
5120: 1E FF      LD      E,$FF           
5122: CD 50 43   CALL    $4350           
5125: CA 34 51   JP      Z,$5134         
5128: 21 4A 7A   LD      HL,$7A4A        
512B: CD AE 45   CALL    $45AE           
512E: CD 45 52   CALL    $5245           
5131: C3 77 51   JP      $5177           
5134: 2A 42 50   LD      HL,($5042)      
5137: 11 2C 01   LD      DE,$012C        
513A: 7C         LD      A,H             
513B: BA         CP      D               
513C: DA 77 51   JP      C,$5177         
513F: 7D         LD      A,L             
5140: BB         CP      E               
5141: DA 77 51   JP      C,$5177         
5144: 3E 23      LD      A,$23           
5146: 1E FF      LD      E,$FF           
5148: CD 50 43   CALL    $4350           
514B: C2 77 51   JP      NZ,$5177        
514E: 3E 2C      LD      A,$2C           
5150: 1E FF      LD      E,$FF           
5152: CD 50 43   CALL    $4350           
5155: C2 77 51   JP      NZ,$5177        
5158: 23         INC     HL              
5159: 36 00      LD      (HL),$00        
515B: 3E 23      LD      A,$23           
515D: 21 E7 4F   LD      HL,$4FE7        
5160: CD 61 43   CALL    $4361           
5163: 23         INC     HL              
5164: 36 00      LD      (HL),$00        
5166: 23         INC     HL              
5167: 23         INC     HL              
5168: 36 FF      LD      (HL),$FF        
516A: 1E FF      LD      E,$FF           
516C: 3E 0F      LD      A,$0F           
516E: CD 76 43   CALL    $4376           
5171: 21 91 7A   LD      HL,$7A91        
5174: CD AE 45   CALL    $45AE           
5177: 3A 40 50   LD      A,($5040)       
517A: C6 01      ADD     $01             
517C: 27         DAA                     
517D: 32 40 50   LD      ($5040),A       
5180: 3A 41 50   LD      A,($5041)       
5183: CE 00      ADC     $00             
5185: 27         DAA                     
5186: 32 41 50   LD      ($5041),A       
5189: C9         RET                     
```

# Command 1: Move To Room X 

```code
; This routine moves the player to a new room. If there is light in the new room or light 
; in the old room then the move always works. Otherwise there is a 60% chance the move kills you.
;
; If there is light in the new room then the room description is printed.
;
; After every move the code checks the pack for treasures. If there are 2 or more treasures then 
; the Mummy moves them all to room 53 (the hard-to-find room in the maze). Then the code moves the 
; chest to room 53. Up till now the chest has been in room 0 (out of play). The only way to make the 
; chest appear in the maze is to encounter the Mummy!
;
; Once the chest is in a room (any room) the Mummy no longer appears. You only see the Mummy once.

MoveToRoomX:
518A: E1         POP     HL              
518B: 46         LD      B,(HL)          
518C: 23         INC     HL              
518D: E5         PUSH    HL              
518E: 3A 3F 50   LD      A,($503F)       
5191: 5F         LD      E,A             
5192: 3E 0F      LD      A,$0F           
5194: CD 50 43   CALL    $4350           
5197: CA DA 51   JP      Z,$51DA         
519A: 1E FF      LD      E,$FF           
519C: 3E 0F      LD      A,$0F           
519E: CD 50 43   CALL    $4350           
51A1: CA DA 51   JP      Z,$51DA         
51A4: 21 45 4F   LD      HL,$4F45        
51A7: 3A 3F 50   LD      A,($503F)       
51AA: CD 61 43   CALL    $4361           
51AD: 7E         LD      A,(HL)          
51AE: E6 40      AND     $40             
51B0: C2 DA 51   JP      NZ,$51DA        
51B3: 78         LD      A,B             
51B4: 21 45 4F   LD      HL,$4F45        
51B7: CD 61 43   CALL    $4361           
51BA: 7E         LD      A,(HL)          
51BB: E6 40      AND     $40             
51BD: C2 DA 51   JP      NZ,$51DA        
51C0: 58         LD      E,B             
51C1: 3E 0F      LD      A,$0F           
51C3: CD 50 43   CALL    $4350           
51C6: CA DA 51   JP      Z,$51DA         
51C9: 3A 74 47   LD      A,($4774)       
51CC: FE 67      CP      $67             
51CE: DA DA 51   JP      C,$51DA         
51D1: 21 04 79   LD      HL,$7904        
51D4: CD AE 45   CALL    $45AE           
51D7: C3 49 54   JP      $5449           
51DA: 3A 3F 50   LD      A,($503F)       
51DD: 32 44 50   LD      ($5044),A       
51E0: 78         LD      A,B             
51E1: 32 3F 50   LD      ($503F),A       
51E4: CD 45 52   CALL    $5245           
51E7: 3E 2A      LD      A,$2A           
51E9: 21 E7 4F   LD      HL,$4FE7        
51EC: CD 61 43   CALL    $4361           
51EF: 23         INC     HL              
51F0: 7E         LD      A,(HL)          
51F1: A7         AND     A               
51F2: C2 42 52   JP      NZ,$5242        
51F5: 21 E7 4F   LD      HL,$4FE7        
51F8: 0E 2C      LD      C,$2C           
51FA: 06 00      LD      B,$00           
51FC: 7E         LD      A,(HL)          
51FD: E6 20      AND     $20             
51FF: 23         INC     HL              
5200: CA 0A 52   JP      Z,$520A         
5203: 7E         LD      A,(HL)          
5204: FE FF      CP      $FF             
5206: C2 0A 52   JP      NZ,$520A        
5209: 04         INC     B               
520A: 23         INC     HL              
520B: 0D         DEC     C               
520C: C2 FC 51   JP      NZ,$51FC        
520F: 78         LD      A,B             
5210: FE 02      CP      $02             
5212: DA 42 52   JP      C,$5242         
5215: 21 E7 4F   LD      HL,$4FE7        
5218: 0E 2C      LD      C,$2C           
521A: 7E         LD      A,(HL)          
521B: E6 20      AND     $20             
521D: 23         INC     HL              
521E: CA 30 52   JP      Z,$5230         
5221: 7E         LD      A,(HL)          
5222: FE FF      CP      $FF             
5224: C2 30 52   JP      NZ,$5230        
5227: 36 35      LD      (HL),$35        
5229: 3A 45 50   LD      A,($5045)       
522C: 3D         DEC     A               
522D: 32 45 50   LD      ($5045),A       
5230: 23         INC     HL              
5231: 0D         DEC     C               
5232: C2 1A 52   JP      NZ,$521A        
5235: 1E 35      LD      E,$35           
5237: 3E 2A      LD      A,$2A           
5239: CD 76 43   CALL    $4376           
523C: 21 4C 7B   LD      HL,$7B4C        
523F: CD AE 45   CALL    $45AE           
5242: C3 AB 43   JP      $43AB           
5245: 3A 3F 50   LD      A,($503F)       
5248: 21 45 4F   LD      HL,$4F45        
524B: CD 61 43   CALL    $4361           
524E: 7E         LD      A,(HL)          
524F: E6 40      AND     $40             
5251: C2 71 52   JP      NZ,$5271        
5254: 3A 3F 50   LD      A,($503F)       
5257: 5F         LD      E,A             
5258: 3E 0F      LD      A,$0F           
525A: CD 50 43   CALL    $4350           
525D: CA 71 52   JP      Z,$5271         
5260: 1E FF      LD      E,$FF           
5262: 3E 0F      LD      A,$0F           
5264: CD 50 43   CALL    $4350           
5267: CA 71 52   JP      Z,$5271         
526A: 21 76 79   LD      HL,$7976        
526D: CD AE 45   CALL    $45AE           
5270: C9         RET                     
5271: 3A 3F 50   LD      A,($503F)       
5274: 21 88 48   LD      HL,$4888        
5277: CD 6B 43   CALL    $436B           
527A: 7E         LD      A,(HL)          
527B: 23         INC     HL              
527C: 66         LD      H,(HL)          
527D: 6F         LD      L,A             
527E: CD AE 45   CALL    $45AE           
5281: 06 00      LD      B,$00           
5283: 04         INC     B               
5284: 3A 3F 50   LD      A,($503F)       
5287: 5F         LD      E,A             
5288: 78         LD      A,B             
5289: FE 2D      CP      $2D             
528B: D0         RET     NC              
528C: CD 50 43   CALL    $4350           
528F: C2 83 52   JP      NZ,$5283        
5292: 78         LD      A,B             
5293: 21 47 50   LD      HL,$5047        
5296: CD 61 43   CALL    $4361           
5299: 7E         LD      A,(HL)          
529A: 23         INC     HL              
529B: 66         LD      H,(HL)          
529C: 6F         LD      L,A             
529D: C5         PUSH    BC              
529E: CD AE 45   CALL    $45AE           
52A1: C1         POP     BC              
52A2: C3 83 52   JP      $5283           
52A5: E1         POP     HL              
52A6: 3A 3F 50   LD      A,($503F)       
52A9: 5F         LD      E,A             
52AA: 7E         LD      A,(HL)          
52AB: 23         INC     HL              
52AC: E5         PUSH    HL              
52AD: CD 76 43   CALL    $4376           
52B0: C3 AB 43   JP      $43AB           
52B3: E1         POP     HL              
52B4: 7E         LD      A,(HL)          
52B5: 23         INC     HL              
52B6: 46         LD      B,(HL)          
52B7: 23         INC     HL              
52B8: E5         PUSH    HL              
52B9: 21 E7 4F   LD      HL,$4FE7        
52BC: CD 61 43   CALL    $4361           
52BF: 7E         LD      A,(HL)          
52C0: F6 80      OR      $80             
52C2: 77         LD      (HL),A          
52C3: 23         INC     HL              
52C4: 70         LD      (HL),B          
52C5: C3 2B 54   JP      $542B           
52C8: E1         POP     HL              
52C9: 7E         LD      A,(HL)          
52CA: 23         INC     HL              
52CB: E5         PUSH    HL              
52CC: 1E FF      LD      E,$FF           
52CE: CD 50 43   CALL    $4350           
52D1: CA AB 43   JP      Z,$43AB         
52D4: C3 BE 43   JP      $43BE           
52D7: E1         POP     HL              
52D8: 46         LD      B,(HL)          
52D9: 23         INC     HL              
52DA: E5         PUSH    HL              
52DB: 3A 3F 50   LD      A,($503F)       
52DE: 5F         LD      E,A             
52DF: 78         LD      A,B             
52E0: CD 50 43   CALL    $4350           
52E3: CA AB 43   JP      Z,$43AB         
52E6: 78         LD      A,B             
52E7: C3 CC 52   JP      $52CC           
52EA: E1         POP     HL              
52EB: 3A 3F 50   LD      A,($503F)       
52EE: 5F         LD      E,A             
52EF: 7E         LD      A,(HL)          
52F0: 23         INC     HL              
52F1: E5         PUSH    HL              
52F2: CD 50 43   CALL    $4350           
52F5: CA AB 43   JP      Z,$43AB         
52F8: C3 BE 43   JP      $43BE           
52FB: 21 E7 4F   LD      HL,$4FE7        
52FE: 0E 01      LD      C,$01           
5300: 23         INC     HL              
5301: 79         LD      A,C             
5302: FE 1F      CP      $1F             
5304: CA 0D 53   JP      Z,$530D         
5307: 7E         LD      A,(HL)          
5308: FE FF      CP      $FF             
530A: CA BE 43   JP      Z,$43BE         
530D: 23         INC     HL              
530E: 0C         INC     C               
530F: 79         LD      A,C             
5310: FE 2D      CP      $2D             
5312: C2 00 53   JP      NZ,$5300        
5315: C3 AB 43   JP      $43AB           
5318: E1         POP     HL              
5319: 46         LD      B,(HL)          
531A: 23         INC     HL              
531B: E5         PUSH    HL              
531C: 3A 74 47   LD      A,($4774)       
531F: B8         CP      B               
5320: CA 26 53   JP      Z,$5326         
5323: D2 BE 43   JP      NC,$43BE        
5326: 21 95 72   LD      HL,$7295        
5329: CD AE 45   CALL    $45AE           
532C: CD 45 52   CALL    $5245           
532F: C3 AB 43   JP      $43AB           
5332: E1         POP     HL              
5333: 46         LD      B,(HL)          
5334: 23         INC     HL              
5335: E5         PUSH    HL              
5336: 3A 44 50   LD      A,($5044)       
5339: B8         CP      B               
533A: C2 BE 43   JP      NZ,$43BE        
533D: E1         POP     HL              
533E: 2B         DEC     HL              
533F: E5         PUSH    HL              
5340: C3 8A 51   JP      $518A           
5343: 3A 7B 46   LD      A,($467B)       
5346: 1E FF      LD      E,$FF           
5348: CD 50 43   CALL    $4350           
534B: C2 57 53   JP      NZ,$5357        
534E: 21 60 75   LD      HL,$7560        
5351: CD AE 45   CALL    $45AE           
5354: C3 AB 43   JP      $43AB           
5357: 3A 7B 46   LD      A,($467B)       
535A: 47         LD      B,A             
535B: C3 F4 53   JP      $53F4           
535E: E1         POP     HL              
535F: 5E         LD      E,(HL)          
5360: 23         INC     HL              
5361: 56         LD      D,(HL)          
5362: 23         INC     HL              
5363: E5         PUSH    HL              
5364: EB         EX      DE,HL           
5365: CD AE 45   CALL    $45AE           
5368: C3 AB 43   JP      $43AB           
536B: E1         POP     HL              
536C: 46         LD      B,(HL)          
536D: 23         INC     HL              
536E: E5         PUSH    HL              
536F: 3A 45 50   LD      A,($5045)       
5372: 3D         DEC     A               
5373: 32 45 50   LD      ($5045),A       
5376: 3A 3F 50   LD      A,($503F)       
5379: 5F         LD      E,A             
537A: 78         LD      A,B             
537B: CD 76 43   CALL    $4376           
537E: C3 2B 54   JP      $542B           
5381: 3A 44 50   LD      A,($5044)       
5384: A7         AND     A               
5385: CA 92 53   JP      Z,$5392         
5388: 47         LD      B,A             
5389: 3A 3F 50   LD      A,($503F)       
538C: 32 44 50   LD      ($5044),A       
538F: C3 E0 51   JP      $51E0           
5392: 21 33 75   LD      HL,$7533        
5395: CD AE 45   CALL    $45AE           
5398: C3 AB 43   JP      $43AB           
539B: 3A 45 50   LD      A,($5045)       
539E: A7         AND     A               
539F: C2 AB 53   JP      NZ,$53AB        
53A2: 21 A6 75   LD      HL,$75A6        
53A5: CD AE 45   CALL    $45AE           
53A8: C3 AB 43   JP      $43AB           
53AB: 21 BC 75   LD      HL,$75BC        
53AE: CD AE 45   CALL    $45AE           
53B1: 06 00      LD      B,$00           
53B3: 1E FF      LD      E,$FF           
53B5: 04         INC     B               
53B6: 78         LD      A,B             
53B7: FE 2D      CP      $2D             
53B9: D2 AB 43   JP      NC,$43AB        
53BC: CD 50 43   CALL    $4350           
53BF: C2 B3 53   JP      NZ,$53B3        
53C2: 78         LD      A,B             
53C3: 21 47 50   LD      HL,$5047        
53C6: CD 61 43   CALL    $4361           
53C9: 7E         LD      A,(HL)          
53CA: 23         INC     HL              
53CB: 66         LD      H,(HL)          
53CC: 6F         LD      L,A             
53CD: 7E         LD      A,(HL)          
53CE: 23         INC     HL              
53CF: A7         AND     A               
53D0: C2 CD 53   JP      NZ,$53CD        
53D3: C5         PUSH    BC              
53D4: CD AE 45   CALL    $45AE           
53D7: C1         POP     BC              
53D8: C3 B3 53   JP      $53B3           
53DB: CD 45 52   CALL    $5245           
53DE: C3 AB 43   JP      $43AB           
53E1: E1         POP     HL              
53E2: 46         LD      B,(HL)          
53E3: 23         INC     HL              
53E4: E5         PUSH    HL              
53E5: 3A 7B 46   LD      A,($467B)       
53E8: B8         CP      B               
53E9: C2 BE 43   JP      NZ,$43BE        
53EC: C3 AB 43   JP      $43AB           
53EF: E1         POP     HL              
53F0: 46         LD      B,(HL)          
53F1: 23         INC     HL              
53F2: E5         PUSH    HL              
53F3: 78         LD      A,B             
53F4: CD 50 43   CALL    $4350           
53F7: 7E         LD      A,(HL)          
53F8: E6 40      AND     $40             
53FA: C2 06 54   JP      NZ,$5406        
53FD: 21 D9 75   LD      HL,$75D9        
5400: CD AE 45   CALL    $45AE           
5403: C3 AB 43   JP      $43AB           
5406: 3A 45 50   LD      A,($5045)       
5409: FE 08      CP      $08             
540B: DA 17 54   JP      C,$5417         
540E: 21 75 75   LD      HL,$7575        
5411: CD AE 45   CALL    $45AE           
5414: C3 AB 43   JP      $43AB           
5417: 3C         INC     A               
5418: 32 45 50   LD      ($5045),A       
541B: 78         LD      A,B             
541C: 1E FF      LD      E,$FF           
541E: CD 76 43   CALL    $4376           
5421: C3 2B 54   JP      $542B           
5424: 3A 7B 46   LD      A,($467B)       
5427: 47         LD      B,A             
5428: C3 6F 53   JP      $536F           
542B: 21 2F 75   LD      HL,$752F        
542E: CD AE 45   CALL    $45AE           
5431: C3 AB 43   JP      $43AB           
5434: E1         POP     HL              
5435: 7E         LD      A,(HL)          
5436: 23         INC     HL              
5437: 5E         LD      E,(HL)          
5438: 23         INC     HL              
5439: E5         PUSH    HL              
543A: 21 E7 4F   LD      HL,$4FE7        
543D: CD 61 43   CALL    $4361           
5440: 7E         LD      A,(HL)          
5441: E6 7F      AND     $7F             
5443: 77         LD      (HL),A          
5444: 23         INC     HL              
5445: 73         LD      (HL),E          
5446: C3 AB 43   JP      $43AB           
5449: 3A 46 50   LD      A,($5046)       
544C: 3C         INC     A               
544D: 32 46 50   LD      ($5046),A       
5450: FE 03      CP      $03             
5452: D2 BC 54   JP      NC,$54BC        
5455: FE 02      CP      $02             
5457: CA B0 54   JP      Z,$54B0         
545A: 21 B4 7E   LD      HL,$7EB4        
545D: 22 C5 54   LD      ($54C5),HL      
5460: 21 AA 7D   LD      HL,$7DAA        
5463: CD AE 45   CALL    $45AE           
5466: CD EE 45   CALL    $45EE           
5469: FE 59      CP      $59             
546B: C2 EF 55   JP      NZ,$55EF        
546E: 2A C5 54   LD      HL,($54C5)      
5471: CD AE 45   CALL    $45AE           
5474: 21 02 50   LD      HL,$5002        
5477: 36 01      LD      (HL),$01        
5479: 23         INC     HL              
547A: 23         INC     HL              
547B: 36 00      LD      (HL),$00        
547D: 21 E7 4F   LD      HL,$4FE7        
5480: 3A 3F 50   LD      A,($503F)       
5483: 47         LD      B,A             
5484: 3E FF      LD      A,$FF           
5486: 0E 2C      LD      C,$2C           
5488: 23         INC     HL              
5489: BE         CP      (HL)            
548A: C2 97 54   JP      NZ,$5497        
548D: 70         LD      (HL),B          
548E: 3A 45 50   LD      A,($5045)       
5491: 3D         DEC     A               
5492: 32 45 50   LD      ($5045),A       
5495: 3E FF      LD      A,$FF           
5497: 23         INC     HL              
5498: 0D         DEC     C               
5499: C2 88 54   JP      NZ,$5488        
549C: 3E 02      LD      A,$02           
549E: 32 3F 50   LD      ($503F),A       
54A1: CD 45 52   CALL    $5245           
54A4: 31 BF 47   LD      SP,$47BF        
54A7: 21 00 00   LD      HL,$0000        
54AA: 22 42 50   LD      ($5042),HL      
54AD: C3 19 43   JP      $4319           
54B0: 21 4E 7F   LD      HL,$7F4E        
54B3: 22 C5 54   LD      ($54C5),HL      
54B6: 21 1D 7E   LD      HL,$7E1D        
54B9: C3 63 54   JP      $5463           
54BC: 21 79 7E   LD      HL,$7E79        
54BF: CD AE 45   CALL    $45AE           
54C2: C3 EF 55   JP      $55EF           
54C5: 00         NOP                     
54C6: 00         NOP                     
54C7: CD CD 54   CALL    $54CD           
54CA: C3 AB 43   JP      $43AB           
54CD: 21 00 00   LD      HL,$0000        
54D0: 22 B2 55   LD      ($55B2),HL      
54D3: 21 45 4F   LD      HL,$4F45        
54D6: 0E 51      LD      C,$51           
54D8: 7E         LD      A,(HL)          
54D9: E6 80      AND     $80             
54DB: 23         INC     HL              
54DC: CA F0 54   JP      Z,$54F0         
54DF: 3A B2 55   LD      A,($55B2)       
54E2: 86         ADD     A,(HL)          
54E3: 27         DAA                     
54E4: 32 B2 55   LD      ($55B2),A       
54E7: 3A B3 55   LD      A,($55B3)       
54EA: CE 00      ADC     $00             
54EC: 27         DAA                     
54ED: 32 B3 55   LD      ($55B3),A       
54F0: 23         INC     HL              
54F1: 0D         DEC     C               
54F2: C2 D8 54   JP      NZ,$54D8        
54F5: 21 E7 4F   LD      HL,$4FE7        
54F8: 0E 2C      LD      C,$2C           
54FA: 7E         LD      A,(HL)          
54FB: E6 20      AND     $20             
54FD: 23         INC     HL              
54FE: CA 21 55   JP      Z,$5521         
5501: 7E         LD      A,(HL)          
5502: FE 02      CP      $02             
5504: 06 20      LD      B,$20           
5506: CA 10 55   JP      Z,$5510         
5509: FE FF      CP      $FF             
550B: C2 21 55   JP      NZ,$5521        
550E: 06 05      LD      B,$05           
5510: 3A B2 55   LD      A,($55B2)       
5513: 80         ADD     A,B             
5514: 27         DAA                     
5515: 32 B2 55   LD      ($55B2),A       
5518: 3A B3 55   LD      A,($55B3)       
551B: CE 00      ADC     $00             
551D: 27         DAA                     
551E: 32 B3 55   LD      ($55B3),A       
5521: 23         INC     HL              
5522: 0D         DEC     C               
5523: C2 FA 54   JP      NZ,$54FA        
5526: 3A 46 50   LD      A,($5046)       
5529: A7         AND     A               
552A: CA 48 55   JP      Z,$5548         
552D: 4F         LD      C,A             
552E: 06 90      LD      B,$90           
5530: 3A B2 55   LD      A,($55B2)       
5533: 80         ADD     A,B             
5534: 27         DAA                     
5535: 32 B2 55   LD      ($55B2),A       
5538: DA 44 55   JP      C,$5544         
553B: 3A B3 55   LD      A,($55B3)       
553E: C6 99      ADD     $99             
5540: 27         DAA                     
5541: 32 B3 55   LD      ($55B3),A       
5544: 0D         DEC     C               
5545: C2 30 55   JP      NZ,$5530        
5548: 3A B3 55   LD      A,($55B3)       
554B: FE 90      CP      $90             
554D: DA 78 55   JP      C,$5578         
5550: 3E 2D      LD      A,$2D           
5552: 32 BF 55   LD      ($55BF),A       
5555: 3A B3 55   LD      A,($55B3)       
5558: 47         LD      B,A             
5559: 3E 99      LD      A,$99           
555B: 90         SUB     B               
555C: 32 B3 55   LD      ($55B3),A       
555F: 3A B2 55   LD      A,($55B2)       
5562: 47         LD      B,A             
5563: 3E 99      LD      A,$99           
5565: 90         SUB     B               
5566: C6 01      ADD     $01             
5568: 27         DAA                     
5569: 32 B2 55   LD      ($55B2),A       
556C: 3A B3 55   LD      A,($55B3)       
556F: CE 00      ADC     $00             
5571: 27         DAA                     
5572: 32 B3 55   LD      ($55B3),A       
5575: C3 7D 55   JP      $557D           
5578: 3E 20      LD      A,$20           
557A: 32 BF 55   LD      ($55BF),A       
557D: 21 C0 55   LD      HL,$55C0        
5580: 3A B3 55   LD      A,($55B3)       
5583: CD A2 55   CALL    $55A2           
5586: 3A B2 55   LD      A,($55B2)       
5589: CD A2 55   CALL    $55A2           
558C: 21 E3 55   LD      HL,$55E3        
558F: 3A 41 50   LD      A,($5041)       
5592: CD A2 55   CALL    $55A2           
5595: 3A 40 50   LD      A,($5040)       
5598: CD A2 55   CALL    $55A2           
559B: 21 B4 55   LD      HL,$55B4        
559E: CD D0 45   CALL    $45D0           
55A1: C9         RET                     
55A2: F5         PUSH    AF              
55A3: 0F         RRCA                    
55A4: 0F         RRCA                    
55A5: 0F         RRCA                    
55A6: 0F         RRCA                    
55A7: CD AB 55   CALL    $55AB           
55AA: F1         POP     AF              
55AB: E6 0F      AND     $0F             
55AD: C6 30      ADD     $30             
55AF: 77         LD      (HL),A          
55B0: 23         INC     HL              
55B1: C9         RET                     

55B2: 00         NOP                     
55B3: 00         NOP                     no

; YOU_SCORED_______OUT_OF_A_POSSIBLE_0220,_USING______TURNS.[CR]
55B4: 59 4F 55 20 53 43 4F 52 45 44 20 20 20 20 20 20 20 4F 55 54 20 4F 46 20 41 20 50 4F 53 53 49 42
55D4: 4C 45 20 30 32 32 30 2C 20 55 53 49 4E 47 20 20 20 20 20 20 54 55 52 4E 53 2E 00      

55EF: CD CD 54   CALL    $54CD
; Endless loop           
55F2: C3 F2 55   JP      $55F2
           
55F5: 21 A0 7F   LD      HL,$7FA0        ; READY CASSETTE
55F8: CD AE 45   CALL    $45AE           ; Print message
55FB: CD EE 45   CALL    $45EE           ; Wait on key
55FE: FE 08      CP      $08             ; Backspace?
5600: CA AB 43   JP      Z,$43AB         ; Yes ... abort operation
5603: FE 0D      CP      $0D             ; Enter?
5605: C2 FB 55   JP      NZ,$55FB        ; No ... keep waiting
5608: 97         SUB     A               ; Make a zero
5609: CD 12 02   CALL    $0212           ; Turn on cassette 0
560C: CD 96 02   CALL    $0296           ; Read tape leader
560F: 21 45 4F   LD      HL,$4F45        ; Load destination
5612: 01 03 01   LD      BC,$0103        ; 259 bytes
5615: 1E 00      LD      E,$00           ; Initialize checksum
5617: E5         PUSH    HL              ; ROM ...
5618: C5         PUSH    BC              ; ... mangles ...
5619: D5         PUSH    DE              ; ... these
561A: CD 35 02   CALL    $0235           ; Read one byte of data
561D: D1         POP     DE              ; Un ...
561E: C1         POP     BC              ; ... mangle ...
561F: E1         POP     HL              ; ... these
5620: 77         LD      (HL),A          ; Store the byte
5621: 83         ADD     A,E             ; Add to ...
5622: 5F         LD      E,A             ; ... checksum
5623: 23         INC     HL              ; Next destination
5624: 0B         DEC     BC              ; All done?
5625: 78         LD      A,B             ; Remember, DEC doesn't ...
5626: B1         OR      C               ; ... affect the zero flag
5627: C2 17 56   JP      NZ,$5617        ; Nope ... do all $103 bytes
562A: D5         PUSH    DE              ; Hold
562B: CD 35 02   CALL    $0235           ; Read the checksum
562E: D1         POP     DE              ; Restore
562F: BB         CP      E               ; Checksum OK?
5630: CA 3F 56   JP      Z,$563F         ; Yes ... out
5633: 21 AC 7F   LD      HL,$7FAC        ; Error message
5636: CD AE 45   CALL    $45AE           ; Print error message
5639: CD F8 01   CALL    $01F8           ; Turn off tape drive
563C: C3 F5 55   JP      $55F5           ; Go back and try again (you better not abort ... we already changed memory)

563F: CD F8 01   CALL    $01F8           ; Turn off the tape  
5642: 21 58 6D   LD      HL,$6D58        
5645: 22 47 50   LD      ($5047),HL      
5648: 22 49 50   LD      ($5049),HL      
564B: CD 45 52   CALL    $5245           
564E: 31 BF 47   LD      SP,$47BF        ; Abandon previous stack
5651: C3 19 43   JP      $4319           ; Back to input loop

5654: 21 A0 7F   LD      HL,$7FA0        
5657: CD AE 45   CALL    $45AE           
565A: CD EE 45   CALL    $45EE           
565D: FE 08      CP      $08             
565F: CA AB 43   JP      Z,$43AB         
5662: FE 0D      CP      $0D             
5664: C2 5A 56   JP      NZ,$565A        
5667: 97         SUB     A               
5668: CD 12 02   CALL    $0212           
566B: CD 87 02   CALL    $0287           
566E: 21 45 4F   LD      HL,$4F45        
5671: 01 03 01   LD      BC,$0103        
5674: 1E 00      LD      E,$00           
5676: E5         PUSH    HL              
5677: C5         PUSH    BC              
5678: 7E         LD      A,(HL)          
5679: 83         ADD     A,E             
567A: 5F         LD      E,A             
567B: D5         PUSH    DE              
567C: 7E         LD      A,(HL)          
567D: CD 64 02   CALL    $0264           
5680: D1         POP     DE              
5681: C1         POP     BC              
5682: E1         POP     HL              
5683: 23         INC     HL              
5684: 0B         DEC     BC              
5685: 78         LD      A,B             
5686: B1         OR      C               
5687: C2 76 56   JP      NZ,$5676        
568A: 7B         LD      A,E             
568B: CD 64 02   CALL    $0264           
568E: CD F8 01   CALL    $01F8           
5691: C3 AB 43   JP      $43AB           

5694: 3A 74 47   LD      A,($4774)       
5697: E6 03      AND     $03             
5699: 47         LD      B,A             
569A: 21 CC 49   LD      HL,$49CC        
569D: 7E         LD      A,(HL)          
569E: 23         INC     HL              
569F: A7         AND     A               
56A0: CA 9D 56   JP      Z,$569D         
56A3: FE FF      CP      $FF             
56A5: CA C2 56   JP      Z,$56C2         
56A8: FE 05      CP      $05             
56AA: D2 B8 56   JP      NC,$56B8        
56AD: 80         ADD     A,B             
56AE: 2B         DEC     HL              
56AF: E6 03      AND     $03             
56B1: C2 B6 56   JP      NZ,$56B6        
56B4: 3E 04      LD      A,$04           
56B6: 77         LD      (HL),A          
56B7: 23         INC     HL              
56B8: 7E         LD      A,(HL)          
56B9: 85         ADD     A,L             
56BA: 6F         LD      L,A             
56BB: 7C         LD      A,H             
56BC: CE 00      ADC     $00             
56BE: 67         LD      H,A             
56BF: C3 9D 56   JP      $569D           
56C2: 21 B8 7F   LD      HL,$7FB8        
56C5: CD AE 45   CALL    $45AE           
56C8: 31 BF 47   LD      SP,$47BF        
56CB: C3 19 43   JP      $4319           

WordTable:
; Info + text + data
;   Info byte:
;   AA_BBB_CCC
;
;   AA = Grammar
;      0 = Noun
;      1 = Verb (and needs noun in pack)
;      2 = Verb (and needs noun in pack or room)
;      3 = Verb (stand alone)
;
;   BBB = number of bytes in token data
;   CCC = number of bytes in token text
;
; Object words
; A single name can refer to several objects. The object data is
; the search order for finding objects in the pack or room. For 
; instance, the LAMP refers to:
;   1) 0x0E unlit lamp
;   2) 0x0F lit lamp
;   3) 0x2C dead lamp
;
; Nouns
;                               Objects     AA BBB CCC Word     Code-reference   Nouns-referenced
56CE: 1C         INC     E               
56CF: 4C         LD      C,H             
56D0: 41         LD      B,C             
56D1: 4D         LD      C,L             
56D2: 50         LD      D,B             
56D3: 0E 0F      LD      C,$0F           
56D5: 2C         INC     L               
56D6: 1E 4C      LD      E,$4C           
56D8: 41         LD      B,C             
56D9: 4E         LD      C,(HL)          
56DA: 54         LD      D,H             
56DB: 45         LD      B,L             
56DC: 52         LD      D,D             
56DD: 0E 0F      LD      C,$0F           
56DF: 2C         INC     L               
56E0: 0B         DEC     BC              
56E1: 42         LD      B,D             
56E2: 4F         LD      C,A             
56E3: 58         LD      E,B             
56E4: 10 0F      DJNZ    $56F5           
56E6: 53         LD      D,E             
56E7: 43         LD      B,E             
56E8: 45         LD      B,L             
56E9: 50         LD      D,B             
56EA: 54         LD      D,H             
56EB: 45         LD      B,L             
56EC: 52         LD      D,D             
56ED: 11 14 42   LD      DE,$4214        
56F0: 49         LD      C,C             
56F1: 52         LD      D,D             
56F2: 44         LD      B,H             
56F3: 13         INC     DE              
56F4: 14         INC     D               
56F5: 16 53      LD      D,$53           
56F7: 54         LD      D,H             
56F8: 41         LD      B,C             
56F9: 54         LD      D,H             
56FA: 55         LD      D,L             
56FB: 45         LD      B,L             
56FC: 13         INC     DE              
56FD: 14         INC     D               
56FE: 0E 50      LD      C,$50           
5700: 49         LD      C,C             
5701: 4C         LD      C,H             
5702: 4C         LD      C,H             
5703: 4F         LD      C,A             
5704: 57         LD      D,A             
5705: 12         LD      (DE),A          
5706: 0E 56      LD      C,$56           
5708: 45         LD      B,L             
5709: 4C         LD      C,H             
570A: 56         LD      D,(HL)          
570B: 45         LD      B,L             
570C: 54         LD      D,H             
570D: 12         LD      (DE),A          
570E: 0E 53      LD      C,$53           
5710: 45         LD      B,L             
5711: 52         LD      D,D             
5712: 50         LD      D,B             
5713: 45         LD      B,L             
5714: 4E         LD      C,(HL)          
5715: 0B         DEC     BC              
5716: 16 53      LD      D,$53           
5718: 41         LD      B,C             
5719: 52         LD      D,D             
571A: 43         LD      B,E             
571B: 4F         LD      C,A             
571C: 50         LD      D,B             
571D: 17         RLA                     
571E: 18 0E      JR      $572E           
5720: 4D         LD      C,L             
5721: 41         LD      B,C             
5722: 47         LD      B,A             
5723: 41         LD      B,C             
5724: 5A         LD      E,D             
5725: 49         LD      C,C             
5726: 19         ADD     HL,DE           
5727: 0D         DEC     C               
5728: 49         LD      C,C             
5729: 53         LD      D,E             
572A: 53         LD      D,E             
572B: 55         LD      D,L             
572C: 45         LD      B,L             
572D: 19         ADD     HL,DE           
572E: 0E 45      LD      C,$45           
5730: 47         LD      B,A             
5731: 59         LD      E,C             
5732: 50         LD      D,B             
5733: 54         LD      D,H             
5734: 49         LD      C,C             
5735: 19         ADD     HL,DE           
5736: 0C         INC     C               
5737: 46         LD      B,(HL)          
5738: 4F         LD      C,A             
5739: 4F         LD      C,A             
573A: 44         LD      B,H             
573B: 1A         LD      A,(DE)          
573C: 0E 42      LD      C,$42           
573E: 4F         LD      C,A             
573F: 54         LD      D,H             
5740: 54         LD      D,H             
5741: 4C         LD      C,H             
5742: 45         LD      B,L             
5743: 1B         DEC     DE              
5744: 15         DEC     D               
5745: 57         LD      D,A             
5746: 41         LD      B,C             
5747: 54         LD      D,H             
5748: 45         LD      B,L             
5749: 52         LD      D,D             
574A: 1C         INC     E               
574B: 1E 1D      LD      E,$1D           
574D: 50         LD      D,B             
574E: 4C         LD      C,H             
574F: 41         LD      B,C             
5750: 4E         LD      C,(HL)          
5751: 54         LD      D,H             
5752: 07         RLCA                    
5753: 08         EX      AF,AF'          
5754: 09         ADD     HL,BC           
5755: 1E 42      LD      E,$42           
5757: 45         LD      B,L             
5758: 41         LD      B,C             
5759: 4E         LD      C,(HL)          
575A: 53         LD      D,E             
575B: 54         LD      D,H             
575C: 07         RLCA                    
575D: 08         EX      AF,AF'          
575E: 09         ADD     HL,BC           
575F: 0E 4D      LD      C,$4D           
5761: 41         LD      B,C             
5762: 43         LD      B,E             
5763: 48         LD      C,B             
5764: 49         LD      C,C             
5765: 4E         LD      C,(HL)          
5766: 06 0E      LD      B,$0E           
5768: 56         LD      D,(HL)          
5769: 45         LD      B,L             
576A: 4E         LD      C,(HL)          
576B: 44         LD      B,H             
576C: 49         LD      C,C             
576D: 4E         LD      C,(HL)          
576E: 06 16      LD      B,$16           
5770: 42         LD      B,D             
5771: 41         LD      B,C             
5772: 54         LD      D,H             
5773: 54         LD      D,H             
5774: 45         LD      B,L             
5775: 52         LD      D,D             
5776: 23         INC     HL              
5777: 24         INC     H               
5778: 0C         INC     C               
5779: 47         LD      B,A             
577A: 4F         LD      C,A             
577B: 4C         LD      C,H             
577C: 44         LD      B,H             
577D: 25         DEC     H               
577E: 0E 4E      LD      C,$4E           
5780: 55         LD      D,L             
5781: 47         LD      B,A             
5782: 47         LD      B,A             
5783: 45         LD      B,L             
5784: 54         LD      D,H             
5785: 25         DEC     H               
5786: 0E 44      LD      C,$44           
5788: 49         LD      C,C             
5789: 41         LD      B,C             
578A: 4D         LD      C,L             
578B: 4F         LD      C,A             
578C: 4E         LD      C,(HL)          
578D: 26 0E      LD      H,$0E           
578F: 53         LD      D,E             
5790: 49         LD      C,C             
5791: 4C         LD      C,H             
5792: 56         LD      D,(HL)          
5793: 45         LD      B,L             
5794: 52         LD      D,D             
5795: 27         DAA                     
5796: 0C         INC     C               
5797: 42         LD      B,D             
5798: 41         LD      B,C             
5799: 52         LD      D,D             
579A: 53         LD      D,E             
579B: 27         DAA                     
579C: 0E 4A      LD      C,$4A           
579E: 45         LD      B,L             
579F: 57         LD      D,A             
57A0: 45         LD      B,L             
57A1: 4C         LD      C,H             
57A2: 52         LD      D,D             
57A3: 28 0D      JR      Z,$57B2         
57A5: 43         LD      B,E             
57A6: 4F         LD      C,A             
57A7: 49         LD      C,C             
57A8: 4E         LD      C,(HL)          
57A9: 53         LD      D,E             
57AA: 29         ADD     HL,HL           
57AB: 0D         DEC     C               
57AC: 43         LD      B,E             
57AD: 48         LD      C,B             
57AE: 45         LD      B,L             
57AF: 53         LD      D,E             
57B0: 54         LD      D,H             
57B1: 2A 0E 54   LD      HL,($540E)      
57B4: 52         LD      D,D             
57B5: 45         LD      B,L             
57B6: 41         LD      B,C             
57B7: 53         LD      D,E             
57B8: 55         LD      D,L             
57B9: 2A 0C 45   LD      HL,($450C)      
57BC: 47         LD      B,A             
57BD: 47         LD      B,A             
57BE: 53         LD      D,E             
57BF: 2B         DEC     HL              
57C0: 0B         DEC     BC              
57C1: 45         LD      B,L             
57C2: 47         LD      B,A             
57C3: 47         LD      B,A             
57C4: 2B         DEC     HL              
57C5: 0C         INC     C               
57C6: 4E         LD      C,(HL)          
57C7: 45         LD      B,L             
57C8: 53         LD      D,E             
57C9: 54         LD      D,H             
57CA: 2B         DEC     HL              
57CB: 0B         DEC     BC              
57CC: 4B         LD      C,E             
57CD: 45         LD      B,L             
57CE: 59         LD      E,C             
57CF: 22 14 56   LD      ($5614),HL      
57D2: 41         LD      B,C             
57D3: 53         LD      D,E             
57D4: 45         LD      B,L             
57D5: 20 21      JR      NZ,$57F8        
57D7: 0E 53      LD      C,$53           
57D9: 48         LD      C,B             
57DA: 41         LD      B,C             
57DB: 52         LD      D,D             
57DC: 44         LD      B,H             
57DD: 53         LD      D,E             
57DE: 15         DEC     D               
57DF: 0E 50      LD      C,$50           
57E1: 4F         LD      C,A             
57E2: 54         LD      D,H             
57E3: 54         LD      D,H             
57E4: 45         LD      B,L             
57E5: 52         LD      D,D             
57E6: 15         DEC     D               
57E7: 0E 45      LD      C,$45           
57E9: 4D         LD      C,L             
57EA: 45         LD      B,L             
57EB: 52         LD      D,D             
57EC: 41         LD      B,C             
57ED: 4C         LD      C,H             
57EE: 1F         RRA                     
57EF: 0D         DEC     C               
57F0: 50         LD      D,B             
57F1: 45         LD      B,L             
57F2: 41         LD      B,C             
57F3: 52         LD      D,D             
57F4: 4C         LD      C,H             
57F5: 16 C9      LD      D,$C9           
57F7: 4E         LD      C,(HL)          
57F8: 01 CD 4E   LD      BC,$4ECD        
57FB: 4F         LD      C,A             
57FC: 52         LD      D,D             
57FD: 54         LD      D,H             
57FE: 48         LD      C,B             
57FF: 01 C9 45   LD      BC,$45C9        
5802: 02         LD      (BC),A          
5803: CC 45 41   CALL    Z,$4145         
5806: 53         LD      D,E             
5807: 54         LD      D,H             
5808: 02         LD      (BC),A          
5809: C9         RET                     
580A: 53         LD      D,E             
580B: 03         INC     BC              
580C: CD 53 4F   CALL    $4F53           
580F: 55         LD      D,L             
5810: 54         LD      D,H             
5811: 48         LD      C,B             
5812: 03         INC     BC              
5813: C9         RET                     
5814: 57         LD      D,A             
5815: 04         INC     B               
5816: CC 57 45   CALL    Z,$4557         
5819: 53         LD      D,E             
581A: 54         LD      D,H             
581B: 04         INC     B               
581C: CA 4E 45   JP      Z,$454E         
581F: 05         DEC     B               
5820: CE 4E      ADC     $4E             
5822: 4F         LD      C,A             
5823: 52         LD      D,D             
5824: 54         LD      D,H             
5825: 48         LD      C,B             
5826: 45         LD      B,L             
5827: 05         DEC     B               
5828: CA 53 45   JP      Z,$4553         
582B: 06 CE      LD      B,$CE           
582D: 53         LD      D,E             
582E: 4F         LD      C,A             
582F: 55         LD      D,L             
5830: 54         LD      D,H             
5831: 48         LD      C,B             
5832: 45         LD      B,L             
5833: 06 CA      LD      B,$CA           
5835: 53         LD      D,E             
5836: 57         LD      D,A             
5837: 07         RLCA                    
5838: CE 53      ADC     $53             
583A: 4F         LD      C,A             
583B: 55         LD      D,L             
583C: 54         LD      D,H             
583D: 48         LD      C,B             
583E: 57         LD      D,A             
583F: 07         RLCA                    
5840: CA 4E 57   JP      Z,$574E         
5843: 08         EX      AF,AF'          
5844: CE 4E      ADC     $4E             
5846: 4F         LD      C,A             
5847: 52         LD      D,D             
5848: 54         LD      D,H             
5849: 48         LD      C,B             
584A: 57         LD      D,A             
584B: 08         EX      AF,AF'          
584C: C9         RET                     
584D: 55         LD      D,L             
584E: 09         ADD     HL,BC           
584F: CA 55 50   JP      Z,$5055         
5852: 09         ADD     HL,BC           
5853: C9         RET                     
5854: 44         LD      B,H             
5855: 0A         LD      A,(BC)          
5856: CC 44 4F   CALL    Z,$4F44         
5859: 57         LD      D,A             
585A: 4E         LD      C,(HL)          
585B: 0A         LD      A,(BC)          
585C: CA 49 4E   JP      Z,$4E49         
585F: 0B         DEC     BC              
5860: CE 49      ADC     $49             
5862: 4E         LD      C,(HL)          
5863: 53         LD      D,E             
5864: 49         LD      C,C             
5865: 44         LD      B,H             
5866: 45         LD      B,L             
5867: 0B         DEC     BC              
5868: CB 4F      SET     1,E             
586A: 55         LD      D,L             
586B: 54         LD      D,H             
586C: 0C         INC     C               
586D: CE 4F      ADC     $4F             
586F: 55         LD      D,L             
5870: 54         LD      D,H             
5871: 53         LD      D,E             
5872: 49         LD      C,C             
5873: 44         LD      B,H             
5874: 0C         INC     C               
5875: CD 43 52   CALL    $5243           
5878: 4F         LD      C,A             
5879: 53         LD      D,E             
587A: 53         LD      D,E             
587B: 0D         DEC     C               
587C: CC 4C 45   CALL    Z,$454C         
587F: 46         LD      B,(HL)          
5880: 54         LD      D,H             
5881: 0E CD      LD      C,$CD           
5883: 52         LD      D,D             
5884: 49         LD      C,C             
5885: 47         LD      B,A             
5886: 48         LD      C,B             
5887: 54         LD      D,H             
5888: 0F         RRCA                    
5889: CC 4A 55   CALL    Z,$554A         
588C: 4D         LD      C,L             
588D: 50         LD      D,B             
588E: 10 CD      DJNZ    $585D           
5890: 43         LD      B,E             
5891: 4C         LD      C,H             
5892: 49         LD      C,C             
5893: 4D         LD      C,L             
5894: 42         LD      B,D             
5895: 11 CD 50   LD      DE,$50CD        
5898: 41         LD      B,C             
5899: 4E         LD      C,(HL)          
589A: 45         LD      B,L             
589B: 4C         LD      C,H             
589C: 12         LD      (DE),A          
589D: CC 42 41   CALL    Z,$4142         
58A0: 43         LD      B,E             
58A1: 4B         LD      C,E             
58A2: 14         INC     D               
58A3: CC 53 57   CALL    Z,$5753         
58A6: 49         LD      C,C             
58A7: 4D         LD      C,L             
58A8: 16 CA      LD      D,$CA           
58AA: 4F         LD      C,A             
58AB: 4E         LD      C,(HL)          
58AC: 17         RLA                     
58AD: CB 4F      SET     1,E             
58AF: 46         LD      B,(HL)          
58B0: 46         LD      B,(HL)          
58B1: 18 CC      JR      $587F           
58B3: 51         LD      D,C             
58B4: 55         LD      D,L             
58B5: 49         LD      C,C             
58B6: 54         LD      D,H             
58B7: 19         ADD     HL,DE           
58B8: CC 53 54   CALL    Z,$5453         
58BB: 4F         LD      C,A             
58BC: 50         LD      D,B             
58BD: 19         ADD     HL,DE           
58BE: CD 53 43   CALL    $4353           
58C1: 4F         LD      C,A             
58C2: 52         LD      D,D             
58C3: 45         LD      B,L             
58C4: 1A         LD      A,(DE)          
58C5: CE 49      ADC     $49             
58C7: 4E         LD      C,(HL)          
58C8: 56         LD      D,(HL)          
58C9: 45         LD      B,L             
58CA: 4E         LD      C,(HL)          
58CB: 54         LD      D,H             
58CC: 1B         DEC     DE              
58CD: CC 4C 4F   CALL    Z,$4F4C         
58D0: 4F         LD      C,A             
58D1: 4B         LD      C,E             
58D2: 1C         INC     E               
58D3: CC 48 45   CALL    Z,$4548         
58D6: 4C         LD      C,H             
58D7: 50         LD      D,B             
58D8: 1D         DEC     E               
58D9: CC 46 49   CALL    Z,$4946         
58DC: 4E         LD      C,(HL)          
58DD: 44         LD      B,H             
58DE: 1E 4C      LD      E,$4C           
58E0: 44         LD      B,H             
58E1: 52         LD      D,D             
58E2: 4F         LD      C,A             
58E3: 50         LD      D,B             
58E4: 21 4E 52   LD      HL,$524E        
58E7: 45         LD      B,L             
58E8: 4C         LD      C,H             
58E9: 45         LD      B,L             
58EA: 41         LD      B,C             
58EB: 53         LD      D,E             
58EC: 21 4C 46   LD      HL,$464C        
58EF: 52         LD      D,D             
58F0: 45         LD      B,L             
58F1: 45         LD      B,L             
58F2: 21 4E 44   LD      HL,$444E        
58F5: 49         LD      C,C             
58F6: 53         LD      D,E             
58F7: 43         LD      B,E             
58F8: 41         LD      B,C             
58F9: 52         LD      D,D             
58FA: 21 CD 4C   LD      HL,$4CCD        
58FD: 49         LD      C,C             
58FE: 47         LD      B,A             
58FF: 48         LD      C,B             
5900: 54         LD      D,H             
5901: 17         RLA                     
5902: 4C         LD      C,H             
5903: 57         LD      D,A             
5904: 41         LD      B,C             
5905: 56         LD      D,(HL)          
5906: 45         LD      B,L             
5907: 23         INC     HL              
5908: 4D         LD      C,L             
5909: 53         LD      D,E             
590A: 48         LD      C,B             
590B: 41         LD      B,C             
590C: 4B         LD      C,E             
590D: 45         LD      B,L             
590E: 23         INC     HL              
590F: 4D         LD      C,L             
5910: 53         LD      D,E             
5911: 57         LD      D,A             
5912: 49         LD      C,C             
5913: 4E         LD      C,(HL)          
5914: 47         LD      B,A             
5915: 23         INC     HL              
5916: 4C         LD      C,H             
5917: 50         LD      D,B             
5918: 4F         LD      C,A             
5919: 55         LD      D,L             
591A: 52         LD      D,D             
591B: 24         INC     H               
591C: 4B         LD      C,E             
591D: 52         LD      D,D             
591E: 55         LD      D,L             
591F: 42         LD      B,D             
5920: 25         DEC     H               
5921: 4D         LD      C,L             
5922: 54         LD      D,H             
5923: 48         LD      C,B             
5924: 52         LD      D,D             
5925: 4F         LD      C,A             
5926: 57         LD      D,A             
5927: 26 4C      LD      H,$4C           
5929: 54         LD      D,H             
592A: 4F         LD      C,A             
592B: 53         LD      D,E             
592C: 53         LD      D,E             
592D: 26 4C      LD      H,$4C           
592F: 46         LD      B,(HL)          
5930: 49         LD      C,C             
5931: 4C         LD      C,H             
5932: 4C         LD      C,H             
5933: 27         DAA                     
5934: 8C         ADC     A,H             
5935: 54         LD      D,H             
5936: 41         LD      B,C             
5937: 4B         LD      C,E             
5938: 45         LD      B,L             
5939: 28 8B      JR      Z,$58C6         
593B: 47         LD      B,A             
593C: 45         LD      B,L             
593D: 54         LD      D,H             
593E: 28 8D      JR      Z,$58CD         
5940: 43         LD      B,E             
5941: 41         LD      B,C             
5942: 52         LD      D,D             
5943: 52         LD      D,D             
5944: 59         LD      E,C             
5945: 28 8D      JR      Z,$58D4         
5947: 43         LD      B,E             
5948: 41         LD      B,C             
5949: 54         LD      D,H             
594A: 43         LD      B,E             
594B: 48         LD      C,B             
594C: 28 8D      JR      Z,$58DB         
594E: 53         LD      D,E             
594F: 54         LD      D,H             
5950: 45         LD      B,L             
5951: 41         LD      B,C             
5952: 4C         LD      C,H             
5953: 28 8E      JR      Z,$58E3         
5955: 43         LD      B,E             
5956: 41         LD      B,C             
5957: 50         LD      D,B             
5958: 54         LD      D,H             
5959: 55         LD      D,L             
595A: 52         LD      D,D             
595B: 28 8C      JR      Z,$58E9         
595D: 4F         LD      C,A             
595E: 50         LD      D,B             
595F: 45         LD      B,L             
5960: 4E         LD      C,(HL)          
5961: 29         ADD     HL,HL           
5962: 8E         ADC     A,(HL)          
5963: 41         LD      B,C             
5964: 54         LD      D,H             
5965: 54         LD      D,H             
5966: 41         LD      B,C             
5967: 43         LD      B,E             
5968: 4B         LD      C,E             
5969: 2C         INC     L               
596A: 8C         ADC     A,H             
596B: 4B         LD      C,E             
596C: 49         LD      C,C             
596D: 4C         LD      C,H             
596E: 4C         LD      C,H             
596F: 2C         INC     L               
5970: 8B         ADC     A,E             
5971: 48         LD      C,B             
5972: 49         LD      C,C             
5973: 54         LD      D,H             
5974: 2C         INC     L               
5975: 8D         ADC     A,L             
5976: 46         LD      B,(HL)          
5977: 49         LD      C,C             
5978: 47         LD      B,A             
5979: 48         LD      C,B             
597A: 54         LD      D,H             
597B: 2C         INC     L               
597C: 8C         ADC     A,H             
597D: 46         LD      B,(HL)          
597E: 45         LD      B,L             
597F: 45         LD      B,L             
5980: 44         LD      B,H             
5981: 2D         DEC     L               
5982: 8B         ADC     A,E             
5983: 45         LD      B,L             
5984: 41         LD      B,C             
5985: 54         LD      D,H             
5986: 2E 8D      LD      L,$8D           
5988: 44         LD      B,H             
5989: 52         LD      D,D             
598A: 49         LD      C,C             
598B: 4E         LD      C,(HL)          
598C: 4B         LD      C,E             
598D: 2F         CPL                     
598E: 8D         ADC     A,L             
598F: 42         LD      B,D             
5990: 52         LD      D,D             
5991: 45         LD      B,L             
5992: 41         LD      B,C             
5993: 4B         LD      C,E             
5994: 30 8D      JR      NC,$5923        
5996: 53         LD      D,E             
5997: 4D         LD      C,L             
5998: 41         LD      B,C             
5999: 53         LD      D,E             
599A: 48         LD      C,B             
599B: 30 CC      JR      NC,$5969        
599D: 4C         LD      C,H             
599E: 4F         LD      C,A             
599F: 41         LD      B,C             
59A0: 44         LD      B,H             
59A1: 3A CC 53   LD      A,($53CC)       
59A4: 41         LD      B,C             
59A5: 56         LD      D,(HL)          
59A6: 45         LD      B,L             
59A7: 3B         DEC     SP              
59A8: CD 50 4C   CALL    $4C50           
59AB: 55         LD      D,L             
59AC: 47         LD      B,A             
59AD: 48         LD      C,B             
59AE: 39         ADD     HL,SP           
59AF: 00         NOP                     
```

# General Command Handler 

```code
; This script is used when the room doesn't have a script for the input command.

GeneralCommandHandler:
59B0: 01 04 04   LD      BC,$0404        
59B3: ED                              
59B4: 73         LD      (HL),E          
59B5: 02         LD      (BC),A          
59B6: 04         INC     B               
59B7: 04         INC     B               
59B8: ED                              
59B9: 73         LD      (HL),E          
59BA: 03         INC     BC              
59BB: 04         INC     B               
59BC: 04         INC     B               
59BD: ED                              
59BE: 73         LD      (HL),E          
59BF: 04         INC     B               
59C0: 04         INC     B               
59C1: 04         INC     B               
59C2: ED                              
59C3: 73         LD      (HL),E          
59C4: 05         DEC     B               
59C5: 04         INC     B               
59C6: 04         INC     B               
59C7: ED                              
59C8: 73         LD      (HL),E          
59C9: 06 04      LD      B,$04           
59CB: 04         INC     B               
59CC: ED                              
59CD: 73         LD      (HL),E          
59CE: 07         RLCA                    
59CF: 04         INC     B               
59D0: 04         INC     B               
59D1: ED                              
59D2: 73         LD      (HL),E          
59D3: 08         EX      AF,AF'          
59D4: 04         INC     B               
59D5: 04         INC     B               
59D6: ED                              
59D7: 73         LD      (HL),E          
59D8: 09         ADD     HL,BC           
59D9: 04         INC     B               
59DA: 04         INC     B               
59DB: ED                              
59DC: 73         LD      (HL),E          
59DD: 0A         LD      A,(BC)          
59DE: 04         INC     B               
59DF: 04         INC     B               
59E0: ED                              
59E1: 73         LD      (HL),E          
59E2: 0B         DEC     BC              
59E3: 04         INC     B               
59E4: 04         INC     B               
59E5: 0D         DEC     C               
59E6: 74         LD      (HL),H          
59E7: 0C         INC     C               
59E8: 04         INC     B               
59E9: 04         INC     B               
59EA: 0D         DEC     C               
59EB: 74         LD      (HL),H          
59EC: 0E 04      LD      C,$04           
59EE: 04         INC     B               
59EF: 31 74 0F   LD      SP,$0F74        
59F2: 04         INC     B               
59F3: 04         INC     B               
59F4: 31 74 12   LD      SP,$1274        
59F7: 04         INC     B               
59F8: 04         INC     B               
59F9: 56         LD      D,(HL)          
59FA: 74         LD      (HL),H          
59FB: 14         INC     D               
59FC: 02         LD      (BC),A          
59FD: 0E 16      LD      C,$16           
59FF: 04         INC     B               
5A00: 04         INC     B               
5A01: 63         LD      H,E             
5A02: 74         LD      (HL),H          
5A03: 17         RLA                     
5A04: 18 07      JR      $5A0D           
5A06: 0C         INC     C               
5A07: 02         LD      (BC),A          
5A08: 0E 15      LD      C,$15           
5A0A: 0E 00      LD      C,$00           
5A0C: 15         DEC     D               
5A0D: 0F         RRCA                    
5A0E: FF         RST     0X38            
5A0F: 04         INC     B               
5A10: 8F         ADC     A,A             
5A11: 74         LD      (HL),H          
5A12: 07         RLCA                    
5A13: 06 02      LD      B,$02           
5A15: 0F         RRCA                    
5A16: 04         INC     B               
5A17: 8F         ADC     A,A             
5A18: 74         LD      (HL),H          
5A19: 04         INC     B               
5A1A: 9F         SBC     A               
5A1B: 74         LD      (HL),H          
5A1C: 18 18      JR      $5A36           
5A1E: 07         RLCA                    
5A1F: 0C         INC     C               
5A20: 02         LD      (BC),A          
5A21: 0F         RRCA                    
5A22: 15         DEC     D               
5A23: 0F         RRCA                    
5A24: 00         NOP                     
5A25: 15         DEC     D               
5A26: 0E FF      LD      C,$FF           
5A28: 04         INC     B               
5A29: B4         OR      H               
5A2A: 74         LD      (HL),H          
5A2B: 07         RLCA                    
5A2C: 06 02      LD      B,$02           
5A2E: 0E 04      LD      C,$04           
5A30: B4         OR      H               
5A31: 74         LD      (HL),H          
5A32: 04         INC     B               
5A33: 9F         SBC     A               
5A34: 74         LD      (HL),H          
5A35: 19         ADD     HL,DE           
5A36: 02         LD      (BC),A          
5A37: 09         ADD     HL,BC           
5A38: 1A         LD      A,(DE)          
5A39: 02         LD      (BC),A          
5A3A: 08         EX      AF,AF'          
5A3B: 1B         DEC     DE              
5A3C: 02         LD      (BC),A          
5A3D: 0F         RRCA                    
5A3E: 1C         INC     E               
5A3F: 02         LD      (BC),A          
5A40: 10 1D      DJNZ    $5A5F           
5A42: 04         INC     B               
5A43: 04         INC     B               
5A44: C4 74 1E   CALL    NZ,$1E74        
5A47: 04         INC     B               
5A48: 04         INC     B               
5A49: D8         RET     C               
5A4A: 74         LD      (HL),H          
5A4B: 28 47      JR      Z,$5A94         
5A4D: 07         RLCA                    
5A4E: 06 11      LD      B,$11           
5A50: 07         RLCA                    
5A51: 04         INC     B               
5A52: 61         LD      H,C             
5A53: 7A         LD      A,D             
5A54: 07         RLCA                    
5A55: 17         RLA                     
5A56: 11 13 07   LD      DE,$0713        
5A59: 06 02      LD      B,$02           
5A5B: 11 04 C7   LD      DE,$C704        
5A5E: 7A         LD      A,D             
5A5F: 07         RLCA                    
5A60: 09         ADD     HL,BC           
5A61: 02         LD      (BC),A          
5A62: 10 15      DJNZ    $5A79           
5A64: 13         INC     DE              
5A65: 00         NOP                     
5A66: 19         ADD     HL,DE           
5A67: 14         INC     D               
5A68: 10 04      DJNZ    $5A6E           
5A6A: 14         INC     D               
5A6B: 7B         LD      A,E             
5A6C: 07         RLCA                    
5A6D: 0A         LD      A,(BC)          
5A6E: 11 20 12   LD      DE,$1220        
5A71: 21 15 20   LD      HL,$2015        
5A74: 00         NOP                     
5A75: 18 12      JR      $5A89           
5A77: 07         RLCA                    
5A78: 0D         DEC     C               
5A79: 11 1E 07   LD      DE,$071E        
5A7C: 06 02      LD      B,$02           
5A7E: 1C         INC     E               
5A7F: 04         INC     B               
5A80: 37         SCF                     
5A81: 7B         LD      A,E             
5A82: 19         ADD     HL,DE           
5A83: 1C         INC     E               
5A84: 1B         DEC     DE              
5A85: 07         RLCA                    
5A86: 0C         INC     C               
5A87: 11 12 1A   LD      DE,$1A12        
5A8A: 20 15      JR      NZ,$5AA1        
5A8C: 20 00      JR      NZ,$5A8E        
5A8E: 18 21      JR      $5AB1           
5A90: 12         LD      (DE),A          
5A91: 12         LD      (DE),A          
5A92: 16 21      LD      D,$21           
5A94: 17         RLA                     
5A95: 07         RLCA                    
5A96: 14         INC     D               
5A97: 11 21 15   LD      DE,$1521        
5A9A: 21 00 07   LD      HL,$0700        
5A9D: 08         EX      AF,AF'          
5A9E: 1A         LD      A,(DE)          
5A9F: 12         LD      (DE),A          
5AA0: 18 20      JR      $5AC2           
5AA2: 04         INC     B               
5AA3: 15         DEC     D               
5AA4: 7C         LD      A,H             
5AA5: 18 15      JR      $5ABC           
5AA7: 04         INC     B               
5AA8: 3D         DEC     A               
5AA9: 7C         LD      A,H             
5AAA: 17         RLA                     
5AAB: 26 0E      LD      H,$0E           
5AAD: 07         RLCA                    
5AAE: 0B         DEC     BC              
5AAF: 11 21 15   LD      DE,$1521        
5AB2: 21 00 18   LD      HL,$1800        
5AB5: 15         DEC     D               
5AB6: 04         INC     B               
5AB7: 75         LD      (HL),L          
5AB8: 7C         LD      A,H             
5AB9: 17         RLA                     
5ABA: 29         ADD     HL,HL           
5ABB: 36 07      LD      (HL),$07        
5ABD: 1C         INC     E               
5ABE: 11 17 07   LD      DE,$0717        
5AC1: 06 02      LD      B,$02           
5AC3: 17         RLA                     
5AC4: 04         INC     B               
5AC5: 01 77 07   LD      BC,$0777        
5AC8: 0E 02      LD      C,$02           
5ACA: 22 04 BE   LD      ($BE04),HL      
5ACD: 76         HALT                    
5ACE: 15         DEC     D               
5ACF: 16 40      LD      D,$40           
5AD1: 15         DEC     D               
5AD2: 17         RLA                     
5AD3: 00         NOP                     
5AD4: 18 18      JR      $5AEE           
5AD6: 04         INC     B               
5AD7: 6B         LD      L,E             
5AD8: 77         LD      (HL),A          
5AD9: 07         RLCA                    
5ADA: 14         INC     D               
5ADB: 11 18 07   LD      DE,$0718        
5ADE: 06 02      LD      B,$02           
5AE0: 18 04      JR      $5AE6           
5AE2: 01 77 07   LD      BC,$0777        
5AE5: 06 02      LD      B,$02           
5AE7: 22 04 2D   LD      ($2D04),HL      
5AEA: 77         LD      (HL),A          
5AEB: 04         INC     B               
5AEC: 6B         LD      L,E             
5AED: 77         LD      (HL),A          
5AEE: 04         INC     B               
5AEF: 97         SUB     A               
5AF0: 77         LD      (HL),A          
5AF1: 23         INC     HL              
5AF2: 04         INC     B               
5AF3: 04         INC     B               
5AF4: 56         LD      D,(HL)          
5AF5: 74         LD      (HL),H          
5AF6: 24         INC     H               
5AF7: 0E 07      LD      C,$07           
5AF9: 09         ADD     HL,BC           
5AFA: 11 1C 15   LD      DE,$151C        
5AFD: 1C         INC     E               
5AFE: 00         NOP                     
5AFF: 04         INC     B               
5B00: E9         JP      (HL)            
5B01: 75         LD      (HL),L          
5B02: 04         INC     B               
5B03: 08         EX      AF,AF'          
5B04: 76         HALT                    
5B05: 25         DEC     H               
5B06: 12         LD      (DE),A          
5B07: 07         RLCA                    
5B08: 06 11      LD      B,$11           
5B0A: 0E 04      LD      C,$04           
5B0C: 18 76      JR      $5B84           
5B0E: 07         RLCA                    
5B0F: 06 11      LD      B,$11           
5B11: 0F         RRCA                    
5B12: 04         INC     B               
5B13: 18 76      JR      $5B8B           
5B15: 04         INC     B               
5B16: 5B         LD      E,E             
5B17: 76         HALT                    
5B18: 27         DAA                     
5B19: 12         LD      (DE),A          
5B1A: 07         RLCA                    
5B1B: 06 11      LD      B,$11           
5B1D: 1B         DEC     DE              
5B1E: 04         INC     B               
5B1F: 77         LD      (HL),A          
5B20: 76         HALT                    
5B21: 07         RLCA                    
5B22: 06 11      LD      B,$11           
5B24: 21 04 D9   LD      HL,$D904        
5B27: 75         LD      (HL),L          
5B28: 04         INC     B               
5B29: AE         XOR     (HL)            
5B2A: 76         HALT                    
5B2B: 2C         INC     L               
5B2C: 2D         DEC     L               
5B2D: 07         RLCA                    
5B2E: 09         ADD     HL,BC           
5B2F: 11 13 15   LD      DE,$1513        
5B32: 13         INC     DE              
5B33: 00         NOP                     
5B34: 04         INC     B               
5B35: B9         CP      C               
5B36: 77         LD      (HL),A          
5B37: 07         RLCA                    
5B38: 09         ADD     HL,BC           
5B39: 11 14 15   LD      DE,$1514        
5B3C: 14         INC     D               
5B3D: 00         NOP                     
5B3E: 04         INC     B               
5B3F: B9         CP      C               
5B40: 77         LD      (HL),A          
5B41: 07         RLCA                    
5B42: 06 11      LD      B,$11           
5B44: 17         RLA                     
5B45: 04         INC     B               
5B46: DD                              
5B47: 77         LD      (HL),A          
5B48: 07         RLCA                    
5B49: 06 11      LD      B,$11           
5B4B: 18 04      JR      $5B51           
5B4D: DD                              
5B4E: 77         LD      (HL),A          
5B4F: 07         RLCA                    
5B50: 06 11      LD      B,$11           
5B52: 0B         DEC     BC              
5B53: 04         INC     B               
5B54: 03         INC     BC              
5B55: 78         LD      A,B             
5B56: 04         INC     B               
5B57: 2F         CPL                     
5B58: 78         LD      A,B             
5B59: 30 04      JR      NC,$5B5F        
5B5B: 04         INC     B               
5B5C: 3F         CCF                     
5B5D: 78         LD      A,B             
5B5E: 2E 23      LD      L,$23           
5B60: 07         RLCA                    
5B61: 09         ADD     HL,BC           
5B62: 11 1A 15   LD      DE,$151A        
5B65: 1A         LD      A,(DE)          
5B66: 00         NOP                     
5B67: 04         INC     B               
5B68: 59         LD      E,C             
5B69: 78         LD      A,B             
5B6A: 07         RLCA                    
5B6B: 06 11      LD      B,$11           
5B6D: 0A         LD      A,(BC)          
5B6E: 04         INC     B               
5B6F: 6E         LD      L,(HL)          
5B70: 78         LD      A,B             
5B71: 07         RLCA                    
5B72: 06 11      LD      B,$11           
5B74: 13         INC     DE              
5B75: 04         INC     B               
5B76: 6E         LD      L,(HL)          
5B77: 78         LD      A,B             
5B78: 07         RLCA                    
5B79: 06 11      LD      B,$11           
5B7B: 14         INC     D               
5B7C: 04         INC     B               
5B7D: 6E         LD      L,(HL)          
5B7E: 78         LD      A,B             
5B7F: 04         INC     B               
5B80: D9         EXX                     
5B81: 75         LD      (HL),L          
5B82: 2F         CPL                     
5B83: 15         DEC     D               
5B84: 07         RLCA                    
5B85: 09         ADD     HL,BC           
5B86: 11 1C 15   LD      DE,$151C        
5B89: 1C         INC     E               
5B8A: 00         NOP                     
5B8B: 04         INC     B               
5B8C: 9C         SBC     H               
5B8D: 76         HALT                    
5B8E: 07         RLCA                    
5B8F: 06 11      LD      B,$11           
5B91: 1E 04      LD      E,$04           
5B93: 86         ADD     A,(HL)          
5B94: 78         LD      A,B             
5B95: 04         INC     B               
5B96: 2F         CPL                     
5B97: 78         LD      A,B             
5B98: 2D         DEC     L               
5B99: 38 07      JR      C,$5BA2         
5B9B: 06 11      LD      B,$11           
5B9D: 13         INC     DE              
5B9E: 04         INC     B               
5B9F: E1         POP     HL              
5BA0: 78         LD      A,B             
5BA1: 07         RLCA                    
5BA2: 06 11      LD      B,$11           
5BA4: 14         INC     D               
5BA5: 04         INC     B               
5BA6: E1         POP     HL              
5BA7: 78         LD      A,B             
5BA8: 07         RLCA                    
5BA9: 10 11      DJNZ    $5BBC           
5BAB: 0B         DEC     BC              
5BAC: 07         RLCA                    
5BAD: 09         ADD     HL,BC           
5BAE: 02         LD      (BC),A          
5BAF: 14         INC     D               
5BB0: 15         DEC     D               
5BB1: 14         INC     D               
5BB2: 00         NOP                     
5BB3: 04         INC     B               
5BB4: 2B         DEC     HL              
5BB5: 79         LD      A,C             
5BB6: 04         INC     B               
5BB7: 4C         LD      C,H             
5BB8: 79         LD      A,C             
5BB9: 07         RLCA                    
5BBA: 06 11      LD      B,$11           
5BBC: 17         RLA                     
5BBD: 04         INC     B               
5BBE: A7         AND     A               
5BBF: 79         LD      A,C             
5BC0: 07         RLCA                    
5BC1: 06 11      LD      B,$11           
5BC3: 18 04      JR      $5BC9           
5BC5: A7         AND     A               
5BC6: 79         LD      A,C             
5BC7: 07         RLCA                    
5BC8: 06 11      LD      B,$11           
5BCA: 0D         DEC     C               
5BCB: 04         INC     B               
5BCC: 4C         LD      C,H             
5BCD: 79         LD      A,C             
5BCE: 04         INC     B               
5BCF: D9         EXX                     
5BD0: 75         LD      (HL),L          

5BD1: 39         ADD     HL,SP           ; plugh
5BD2: 02         LD      (BC),A          
5BD3: 1D         DEC     E
               
5BD4: 3A 02 1B   LD      A,($1B02)       
5BD7: 3B         DEC     SP              
5BD8: 02         LD      (BC),A          
5BD9: 1C         INC     E               
5BDA: 00         NOP
```

# Room Descriptions

```code
RoomDescriptions:

; Description for room: 1
; YOU_ARE_STANDING_BEFORE_THE_ENTRANCE_OF_A_PYRAMID.__AROUND_YOU__IS_A_DESERT.[CR]
5BDB: 19 C7 DE 94 14 55 5E 50 BD 90 5A C4 6A 59 60 5B 
5BEB: B1 5F BE 30 15 EB BF 17 98 B8 16 7B 14 14 A8 6B 
5BFB: 48 9B 5D 94 14 30 A1 1B 58 1B A1 D5 15 7B 14 F5 
5C0B: 59 3E 62 2E 00 

; YOU_ARE_IN_THE_ENTRANCE_TO_THE_PYRAMID.__A_HOLE_IN_THE_FLOOR____LEADS_TO_A_PASSAGE_BENEATH_THE_SURFACE.[CR]
5C10: 22 C7 DE 94 14 4B 5E 96 96 DB 72 9E 61 D0 B0 9B 
5C20: 53 6B BF 5F BE F3 16 CF B0 17 79 43 13 A9 15 DB 
5C30: 8B 83 7A 5F BE 56 15 44 A0 3B 13 3F 16 0D 47 89 
5C40: 17 7B 14 55 A4 09 B7 44 5E 8F 61 82 49 82 17 55 
5C50: 5E 30 C6 D7 46 2E 00 

; YOU_ARE_IN_THE_DESERT.[CR]
5C57: 07 C7 DE 94 14 4B 5E 96 96 DB 72 F5 59 3E 62 2E 
5C67: 00 

; YOU_ARE_IN_A_SMALL_CHAMBER_BENEATH_A_HOLE_FROM_THE_SURFACE.__A__LOW_CRAWL_LEADS_INWARD_TO_THE_WEST.__
; HIEROGLYPHICS_ON_THE_WALL__TRANSLATE,_"CURSE_ALL_WHO_ENTER_THIS_SACRED_CRYPT."[CR]
5C68: 3B C7 DE 94 14 4B 5E 83 96 5F 17 46 48 DA 14 64 
5C78: 48 23 62 70 4D 96 5F 03 71 A9 15 DB 8B 79 68 56 
5C88: 90 DB 72 34 BA C5 65 DB 63 7B 14 49 16 C5 CE D9 
5C98: B0 0E 8A 86 5F CB B5 33 9B 33 B1 6B BF 5F BE F7 
5CA8: 17 17 BA 4A 13 34 79 FE 9E E2 DE E5 78 C0 16 82 
5CB8: 17 59 5E 46 48 56 13 D0 B0 BB B8 FE BD 6D 13 3D 
5CC8: C6 43 5E F3 8C 29 D1 30 15 F4 BD 82 17 4B 7B 05 
5CD8: B7 66 B1 E4 14 EE DE 2E 22 00 

; YOU_ARE_CRAWLING_OVER_PEBBLES_IN_A_LOW_PASSAGE.__THERE_IS_A_DIM_LIGHT_AT_THE_EAST_END_OF_THE_PASSAGE.[CR]
5CE2: 21 C7 DE 94 14 45 5E D9 B0 90 8C D1 6A 74 CA DF 
5CF2: 16 F6 4C 4B 62 83 7A 4E 45 6B A1 55 A4 09 B7 DB 
5D02: 63 82 17 2F 62 D5 15 7B 14 8F 5A 43 16 2E 6D 96 
5D12: 14 82 17 47 5E 66 49 30 15 11 58 96 64 DB 72 55 
5D22: A4 09 B7 45 2E 00 

; YOU_ARE_IN_A_ROOM_FILLED_WITH_BROKEN_POTTERY_SHARDS_OF_ANCIENT__EGYPTIAN_CRAFTS.__AN_AWKWARD_CORRIDOR_LEADS_
; UPWARD_AND_WEST.[CR]
5D28: 29 C7 DE 94 14 4B 5E 83 96 39 17 DB 9F 0E 67 E6 
5D38: 8B FB 17 53 BE 79 4F B0 85 E9 16 3F C0 7B B4 1B 
5D48: B8 4D B1 B8 16 90 14 47 54 B3 9A 29 15 EE DE 90 
5D58: 78 E4 14 5E 47 5B BB 90 14 99 14 73 88 33 B1 44 
5D68: 55 06 B2 A3 A0 E3 8B 0B 5C F1 C5 2E 49 90 14 19 
5D78: 58 66 62 2E 00 

; YOU_ARE_IN_AN_AWKWARD_SLOPING_EAST/WEST_CORRIDOR.[CR]
5D7D: 10 C7 DE 94 14 4B 5E 83 96 83 96 A9 D1 2E 49 5E 
5D8D: 17 63 A0 AB 98 95 5F E1 BC 66 62 E1 14 73 B3 84 
5D9D: 5B 2E 00 

; YOU_ARE_IN_A_SPLENDID_CHAMBER_THIRTY_FEET_HIGH.__THE_WALLS_ARE__FROZEN_RIVERS_OF_ORANGE_STONE.__AN_AWKWARD_
; CORRIDOR_AND_A_GOOD__PASSAGE_EXIT_FROM_THE_EAST_AND_WEST_SIDES_OF_THE_CHAMBER.[CR]
5DA0: 3D C7 DE 94 14 4B 5E 83 96 62 17 F0 8B 86 5A DA 
5DB0: 14 64 48 23 62 63 BE D3 B3 4F 15 73 62 89 73 9B 
5DC0: 76 82 17 59 5E 46 48 C3 B5 5B B1 5C 15 EF A1 94 
5DD0: 96 CF 7B 8B B3 C3 9E AB A0 B7 98 66 17 0F A0 3B 
5DE0: F4 83 48 FD 49 14 D0 05 58 BC A0 09 79 83 AF 33 
5DF0: 98 49 45 36 A0 52 13 65 49 77 47 3A 15 73 7B 79 
5E00: 68 56 90 DB 72 95 5F 03 BC 33 98 B5 D0 15 BC FF 
5E10: 78 D1 B5 96 64 DB 72 1B 54 AF 91 52 2E 00 

; AT_YOUR_FEET_IS_A_SMALL_PIT_BREATHING_TRACES_OF_WHITE_MIST.__AN_EAST_PASSAGE_ENDS_HERE_EXCEPT_FOR_A_SMALL_CRACK_
; LEADING_ON._____ROUGH_STONE_STEPS_LEAD_DOWN_THE_PIT.[CR]
5E1E: 36 73 49 C7 DE 88 AF 36 60 D5 15 7B 14 E3 B8 F3 
5E2E: 8C 96 A5 BC 14 96 5F 90 73 D6 6A C5 B0 4B 62 C3 
5E3E: 9E 23 D1 DB BD D5 92 9B C1 90 14 23 15 F3 B9 55 
5E4E: A4 09 B7 47 5E 4D 98 9F 15 5B B1 1D 63 EE 61 59 
5E5E: 15 83 AF 5F 17 46 48 E4 14 DD 46 3F 16 03 47 AB 
5E6E: 98 27 A0 3B 13 54 13 29 A1 15 71 80 BF 55 5E F2 
5E7E: BD CE B5 86 5F 09 15 03 D2 5F BE E3 16 54 2E 00 

; YOU_ARE_AT_ONE_END_OF_A_VAST_HALL_STRETCHING_FORWARD_OUT_OF_____SIGHT_TO_THE_WEST.__THERE_ARE_OPENINGS_TO_EITHER_
; SIDE.__NEARBY,_A_WIDE_STONE_STAIRCASE_LEADS_DOWNWARD.__THE_HALL_IS_VERY_MUSTY__AND_A_COLD_WIND_BLOWS_UP_THE_
; STAIRCASE.__THERE_IS_A_PASSAGE_AT__THE_TOP_OF_A_DOME_BEHIND_YOU.__ROUGH_STONE_STEPS_LEAD_UP_THE____DOME.[CR]
5E8E: 6C C7 DE 94 14 43 5E 11 BC 5B 98 8E 61 B8 16 7B 
5E9E: 14 D5 C9 0A BC 46 48 66 17 76 B1 23 54 AB 98 04 
5EAE: 68 14 D0 11 58 73 C6 C3 9E 3B 13 5B 17 2E 6D 89 
5EBE: 17 82 17 59 5E 66 62 3B F4 5F BE 5B B1 2F 49 C2 
5ECE: 16 93 61 C5 98 89 17 2B 15 5F BE 95 AF FF 78 3B 
5EDE: F4 63 98 03 B1 03 EE FB 17 DB 59 09 BA 5B 98 FB 
5EEE: B9 2D 7B 57 49 3F 16 0D 47 09 15 21 D2 2E 49 3B 
5EFE: F4 5F BE 9B 15 F3 8C 4B 7B 74 CA 4F DB 66 C6 3B 
5F0E: DB 8E 48 7B 14 3E 55 19 58 8E 7A B6 14 85 A1 B2 
5F1E: 17 82 17 55 5E 4B BD 13 B1 BF B7 56 13 F4 72 4B 
5F2E: 5E C3 B5 DB 16 D3 B9 9B 6C 73 49 82 17 56 5E 53 
5F3E: A0 C3 9E 46 45 E7 9F AF 14 90 73 1B 58 3F A1 54 
5F4E: 13 29 A1 15 71 80 BF 55 5E F2 BD CE B5 86 5F B2 
5F5E: 17 82 17 3B 5E 46 13 E7 9F 2E 00 

; THIS_IS_A_LOW_ROOM_WITH_A_HIEROGLYPH_ON_THE_WALL.__IT_TRANSLATES"YOU_WON'T_GET_IT_UP_THE_STEPS".[CR]
5F69: 20 63 BE CB B5 C3 B5 49 16 D4 CE 3F A0 FB 17 53 
5F79: BE 4A 45 34 79 FE 9E E2 DE C0 16 82 17 59 5E 46 
5F89: 48 3B F4 73 7B EB BF 9E 9A 7F 49 03 B6 1B A1 40 
5F99: D2 F3 23 B6 6C D6 15 B2 17 82 17 55 5E F2 BD 07 
5FA9: B6 00 

; YOU_ARE_ON_THE_EAST_BANK_OF_A_BOTTOMLESS_PIT_STRETCHING_ACROSS__THE_HALL.__THE_MIST_IS_QUITE_THICK_HERE,_AND_THE_
; PIT_IS_TOO_WIDETO_JUMP.[CR]
5FAB: 2D C7 DE 94 14 51 5E 96 96 DB 72 95 5F 04 BC 95 
5FBB: 48 B8 16 7B 14 06 4F 7F BF F5 8B D2 B5 73 7B 0C 
5FCB: BA 7D 62 90 73 C3 6A B9 55 CB B9 82 17 4A 5E 46 
5FDB: 48 3B F4 5F BE 6B 16 F3 B9 4B 7B AB AD DB BD 63 
5FEB: BE 8B 54 F4 72 B3 63 8E 48 82 17 52 5E 73 7B 4B 
5FFB: 7B 81 BF FB 17 F6 59 CC 9C 72 C5 2E 00 

; YOU_ARE_IN_THE_PHARAOH'S_CHAMBER,_WITH_PASSAGES_OFF_IN_ALL______DIRECTIONS.[CR]
6008: 19 C7 DE 94 14 4B 5E 96 96 DB 72 5B A5 D1 B0 65 
6018: 71 DA 14 64 48 46 62 FB 17 53 BE 55 A4 09 B7 4B 
6028: 62 D0 9E D0 15 8E 14 FB 89 3B 13 03 15 65 B1 91 
6038: BE AF 9A 00 

; YOU_ARE_IN_THE_SOUTH_SIDE_CHAMBER.[CR]
603C: 0B C7 DE 94 14 4B 5E 96 96 DB 72 47 B9 53 BE 46 
604C: B8 45 5E 4F 72 74 4D 2E 00 

; YOU_ARE_ON_THE_WEST_SIDE_OF_THE_BOTTOMLESS_PIT_IN_THE_HALL_OF___GODS.[CR]
6055: 17 C7 DE 94 14 51 5E 96 96 DB 72 B5 D0 15 BC FF 
6065: 78 B8 16 82 17 44 5E 0E A1 EE 9F 65 62 E3 16 0B 
6075: BC 96 96 DB 72 4E 72 11 8A 7B 64 81 15 2F 5C 00 

; YOU_ARE_AT_THE_WEST_END_OF_THE_HALL_OF_GODS.___A_LOW_WIDE_PASS__CONTINUES_WEST_AND_ANOTHER_GOES_NORTH.__TO_THE_SOUTH_
; IS_A_LITTLEPASSAGE_SIX_FEET_OFF_THE_FLOOR.[CR]
6085: 35 C7 DE 94 14 43 5E 16 BC DB 72 B5 D0 07 BC 33 
6095: 98 C3 9E 5F BE 9B 15 F3 8C C3 9E 36 6E 5B BB 43 
60A5: 13 49 16 D9 CE FF 78 DB 16 CB B9 E1 14 C3 9A E7 
60B5: 9A D9 B5 66 62 90 14 03 58 06 9A F4 72 81 15 4B 
60C5: 62 04 9A 77 BE 56 13 D6 9C DB 72 47 B9 53 BE 4B 
60D5: 7B 4E 45 8E 7B F2 8B 65 49 77 47 5B 17 08 D5 36 
60E5: 60 B8 16 96 64 DB 72 89 67 C7 A0 00 

; YOU_ARE_AT_EAST_END_OF_A_VERY_LONG_HALL_APPARENTLY_WITHOUT_SIDE_CHAMBERS.__TO_THE_EAST_A_LOW_WIDE_CRAWL_SLANTS_UP.__TO_
; THE_NORTHA_ROUND_TWO_FOOT_HOLE_SLANTS_DOWN.[CR]
60F1: 36 C7 DE 94 14 43 5E 07 BC 66 49 30 15 11 58 83 
6101: 64 CF 17 7B B4 80 8D CA 6A 46 48 92 14 54 A4 9E 
6111: 61 FB 8E 56 D1 87 74 15 BC FF 78 DA 14 64 48 3D 
6121: 62 3B F4 6B BF 5F BE 23 15 F3 B9 4E 45 6B A1 46 
6131: D1 45 5E D9 B0 15 8A 50 8B 0B C0 F7 C5 56 13 D6 
6141: 9C DB 72 04 9A 5B BE 39 17 8E C5 91 17 C8 9C 46 
6151: A0 A9 15 DB 8B BB B8 CD 9A 09 15 27 D2 00 

; YOU_ARE_AT_THE_WEST_END_OF_A_VERY_LONG_FEATURELESS_HALL.__THE___HALL_JOINS_UP_WITH_A_NARROW_NORTH/SOUTH_PASSAGE.[CR]
615F: 25 C7 DE 94 14 43 5E 16 BC DB 72 B5 D0 07 BC 33 
616F: 98 C3 9E 58 45 43 62 49 16 AB 98 63 66 74 C0 3F 
617F: 61 CB B9 4E 72 9B 8F 82 17 3B 5E 9B 15 F3 8C FB 
618F: 80 8B 9A D3 C5 56 D1 03 71 8B 16 79 B3 D0 CE BE 
619F: A0 DD 71 36 A1 12 71 65 49 77 47 2E 00 

; YOU_ARE_AT_A_CROSSOVER_OF_A_HIGH_N/S_PASSAGE_AND_A_LOW_E/W_ONE.[CR]
61AC: 15 C7 DE 94 14 43 5E 03 BC E4 14 E5 A0 4F A1 91 
61BC: AF 83 64 A3 15 13 6D 5D 97 DB 16 D3 B9 9B 6C 8E 
61CC: 48 7B 14 89 8D 20 15 D1 CE 7F 98 00 

; DEAD_END.[CR]
61D8: 03 E3 59 07 58 57 98 00 

; YOU_ARE_IN_THE_WEST_THRONE_CHAMBER.__A_PASSAGE_CONTINUES_WEST___AND_UP_FROM_HERE.[CR]
61E0: 1B C7 DE 94 14 4B 5E 96 96 DB 72 B5 D0 16 BC F9 
61F0: 74 5B 98 1B 54 AF 91 1B B5 7B 14 55 A4 09 B7 45 
6200: 5E 1E A0 9F 7A 4B 62 B5 D0 FB BB 90 14 17 58 08 
6210: A3 FF B2 9F 15 7F B1 00 

; YOU_ARE_IN_A_LOW_N/S_PASSAGE_AT_A_HOLE_IN_THE_FLOOR.__THE_HOLE__GOES_DOWN_TO_AN_E/W_PASSAGE.[CR]
6218: 1E C7 DE 94 14 4B 5E 83 96 49 16 D0 CE 8B 36 55 
6228: A4 09 B7 43 5E 03 BC A9 15 DB 8B 83 7A 5F BE 56 
6238: 15 44 A0 3B F4 5F BE A9 15 DB 8B 81 15 4B 62 89 
6248: 5B 96 96 C3 9C 87 96 2B 37 55 A4 09 B7 45 2E 00 

; YOU_ARE_IN_A_LARGE_ROOM,_WITH_A_PASSAGE_TO_THE_SOUTH,_AND_A_WALLOF_BROKEN_ROCK_TO_THE_EAST.__THERE_IS_A_PANEL_
; ON_THE_NORTH_WALL.[CR]
6258: 2A C7 DE 94 14 4B 5E 83 96 3B 16 B7 B1 39 17 FE 
6268: 9F FB 17 53 BE 52 45 65 49 77 47 89 17 82 17 55 
6278: 5E 36 A1 73 76 8E 48 7B 14 0E D0 78 8D BC 14 97 
6288: 9F 94 96 5D 9E 89 17 82 17 47 5E 66 49 3B F4 5F 
6298: BE 5B B1 4B 7B 52 45 8F 48 11 8A 96 96 DB 72 04 
62A8: 9A 53 BE 0E D0 4C 2E 00 

; YOU_ARE_IN_THE_CHAMBER_OF_ANUBIS.[CR]
62B0: 0B C7 DE 94 14 4B 5E 96 96 DB 72 1B 54 AF 91 91 
62C0: AF 83 64 E4 9A 6F 7B 00 

; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
62C8: 10 C7 DE 94 14 4B 5E 83 96 63 16 5B E3 C3 9E BB 
62D8: C0 13 BA DB 16 D3 B9 B5 6C 03 EE F3 8C 43 48 BF 
62E8: 85 00 

; YOU_ARE_ON_THE_BRINK_OF_A_LARGE_PIT.__YOU_COULD_CLIMB_DOWN,_BUT_YOU_WOULD_NOT_BE_ABLE_TO_CLIMB_BACK_UP.__THE_MAZE_
; CONTINUES_ON__THIS_LEVEL.[CR]
62EA: 2E C7 DE 94 14 51 5E 96 96 DB 72 73 4F 4B 99 C3 
62FA: 9E 4E 45 31 49 52 5E 97 7B 5B 13 1B A1 47 55 B3 
630A: 8B C3 54 A3 91 89 5B F3 9B F6 4F 51 18 59 C2 2E 
631A: A1 10 58 F3 A0 5B 4D B6 46 56 5E C5 9C 8F 8C 84 
632A: 4B DD 46 B2 17 3B F4 5F BE 63 16 5B E3 40 55 90 
633A: BE 35 C4 C0 16 56 13 95 73 3F 16 6E CA 2E 00 

; YOU_ARE_IN_A_DIRTY_BROKEN_PASSAGE.__TO_THE_EAST_IS_A_CRAWL.__TO_THE_WEST_IS_A_LARGE_PASSAGE.__ABOVE_YOU_IS_A_
; HOLE_TO_ANOTHER____PASSAGE.[CR]
6349: 2D C7 DE 94 14 4B 5E 83 96 03 15 D3 B3 BC 14 97 
6359: 9F 92 96 65 49 77 47 3B F4 6B BF 5F BE 23 15 F3 
6369: B9 4B 7B 45 45 D9 B0 9B 8F 89 17 82 17 59 5E 66 
6379: 62 D5 15 7B 14 54 8B 9B 6C 55 A4 09 B7 DB 63 84 
6389: 14 4F A1 51 18 4B C2 C3 B5 A9 15 DB 8B 6B BF 99 
6399: 48 5F BE 7B AF 52 13 65 49 77 47 2E 00 

; YOU_ARE_ON_THE_BRINK_OF_A_SMALL_CLEAN_CLIMBABLE_PIT.__A_CRAWL___LEADS_WEST.[CR]
63A6: 19 C7 DE 94 14 51 5E 96 96 DB 72 73 4F 4B 99 C3 
63B6: 9E 55 45 8E 91 05 8A E3 8B 85 96 8F 8C C4 4C DB 
63C6: 8B 96 A5 3B F4 45 45 D9 B0 FB 89 3F 16 0D 47 F7 
63D6: 17 17 BA 00 

; YOU_ARE_IN_THE_BOTTOM_OF_A_SMALL_PIT_WITH_A_LITTLE_STREAM,_WHICHENTERS_AND_EXITS_THROUGH_TINY_SLITS.[CR]
63DA: 21 C7 DE 94 14 4B 5E 96 96 DB 72 06 4F 7F BF B8 
63EA: 16 7B 14 E3 B8 F3 8C 96 A5 FB 17 53 BE 4E 45 8E 
63FA: 7B DB 8B 0C BA 8F 5F 19 EE 85 73 F0 72 F4 BD C3 
640A: B5 33 98 23 63 0B C0 6C BE 29 A1 16 71 A3 7A 5E 
641A: 17 8D 7B 2E 00 

; YOU_ARE_IN_A_THE_ROOM_OF_BES,_WHOSE_PICTURE_IS_ON_THE_WALL._____THERE_IS_A_BIG_HOLE_IN_THE_FLOOR.__THERE_IS_
; A_PASSAGE_LEADING___EAST.[CR]
641F: 2C C7 DE 94 14 4B 5E 83 96 82 17 54 5E 3F A0 B8 
642F: 16 AF 14 33 BB 29 D1 9B B7 85 A5 74 C0 4B 5E D1 
643F: B5 96 96 DB 72 0E D0 9B 8F 3B 13 82 17 2F 62 D5 
644F: 15 7B 14 09 4E A9 15 DB 8B 83 7A 5F BE 56 15 44 
645F: A0 3B F4 5F BE 5B B1 4B 7B 52 45 65 49 77 47 3F 
646F: 16 03 47 AB 98 47 13 66 49 2E 00 

; YOU_ARE_AT_A_COMPLEX_JUNCTION.__A_LOW_HANDS_AND_KNEES_PASSAGE___FROM_THE_NORTH_JOINS_A_HIGHER_CRAWL_FROM_THE_
; EAST_TO_MAKE_A_____WALKING_PASSAGE_GOING_WEST.__THERE_IS_ALSO_A_LARGE_ROOM_ABOVE.__THE_AIR_IS_DAMP_HERE.[CR]
647A: 47 C7 DE 94 14 43 5E 03 BC E1 14 E6 93 13 63 F0 
648A: 81 03 56 27 A0 43 13 49 16 CA CE 8E 48 C3 B5 33 
649A: 98 0F 87 4B 62 55 A4 09 B7 3B 5E 5C 15 DB 9F 5F 
64AA: BE 99 16 C2 B3 F9 15 9D 7A 7B 14 89 73 F4 72 E4 
64BA: 14 FE 49 5C 15 DB 9F 5F BE 23 15 F3 B9 6B BF 8D 
64CA: 91 43 5E 3B 13 59 13 45 48 91 7A DB 16 D3 B9 9B 
64DA: 6C 3B 6E AB 98 B5 D0 9B C1 82 17 2F 62 D5 15 8E 
64EA: 14 2B B9 4E 45 31 49 54 5E 3F A0 84 14 4F A1 3B 
64FA: F4 5F BE 8B 14 8B AF C6 B5 72 48 9F 15 7F B1 00 

; YOU_ARE_IN_THE_UNDERWORLD_ANTEROOM_OF_SEKER.__PASSAGES_GO_EAST,_WEST,_AND_UP.__HUMAN_BONES_ARE_STREWN_ABOUT_ON_
; THE_FLOOR._______HIEROGLYPHICS_ON_THE_WALL_ROUGHLY_TRANSLATE_TO_"THOSE_WHO_______PROCEED_EAST_MAY_NEVER_RETURN."[CR]
650A: 4A C7 DE 94 14 4B 5E 96 96 DB 72 8E C5 41 62 B6 
651A: A0 03 58 BF 9A 01 B3 51 90 95 64 17 61 1B B5 DB 
652A: 16 D3 B9 B5 6C 81 15 23 15 16 BA F7 17 16 BA 90 
653A: 14 17 58 9B A8 AF 15 90 91 B9 14 75 98 94 14 55 
654A: 5E EF BF 03 D2 B9 46 73 C6 03 A0 5F BE 56 15 44 
655A: A0 3B F4 3B 13 4A 13 34 79 FE 9E E2 DE E5 78 C0 
656A: 16 82 17 59 5E 46 48 39 17 7A C4 FB 8E EB BF 9E 
657A: 9A 7F 49 89 17 7E 13 85 74 59 5E 6B 74 3B 13 3B 
658A: 13 F9 A6 A7 53 07 58 66 49 63 16 50 DB CF 62 94 
659A: AF 8F 62 E7 B2 22 00 

; YOU_ARE_AT_THE_LAND_OF_DEAD.__PASSAGES_LEAD_OFF_IN_>ALL<________DIRECTIONS.[CR]
65A1: 19 C7 DE 94 14 43 5E 16 BC DB 72 50 8B 11 58 86 
65B1: 64 86 5F 3B F4 55 A4 09 B7 4B 62 E3 8B 11 58 83 
65C1: 66 83 7A 8E 2D 73 8A 3B 13 3B 13 03 15 65 B1 91 
65D1: BE AF 9A 00 

; YOU'RE_IN_A_LARGE_ROOM_WITH_ANCIENT_DRAWINGS_ON_ALL_WALLS.______THE_PICTURES_DEPICT_ATUM,_A_PHARAOH_WEARING_THE_DOUBLE_
; CROWN.___A_SHALLOW_PASSAGE_PROCEEDS_DOWNWARD,_AND_A_SOMEWHAT_STEEPER_ONE_LEADS_UP.__A_LOW_HANDS_AND_KNEES_PASSAGE_
; ENTERS_FROM_THE_SOUTH. [CR]
65D5: 55 C7 DE AF 23 D0 15 7B 14 54 8B 9B 6C 01 B3 59 
65E5: 90 82 7B 90 14 47 54 B3 9A EB 5B 50 D1 CB 6E 03 
65F5: A0 46 48 F3 17 0D 8D 3B F4 3B 13 82 17 52 5E E6 
6605: 78 2F C6 C6 B5 E3 61 F3 55 8F 49 B3 95 52 45 54 
6615: 72 BA 48 F7 17 33 49 AB 98 5F BE 09 15 B6 C3 45 
6625: 5E 09 B3 1B 9C 43 13 5A 17 46 48 6B A1 55 A4 09 
6635: B7 52 5E F5 B2 26 60 C6 B5 80 A1 14 D0 73 5D 8E 
6645: 48 7B 14 3F B9 FA 62 73 49 FF B9 DF 61 91 AF 5B 
6655: 98 E3 8B 0B 5C F7 C5 43 13 49 16 CA CE 8E 48 C3 
6665: B5 33 98 0F 87 4B 62 55 A4 09 B7 47 5E BF 9A 8B 
6675: B3 79 68 56 90 DB 72 47 B9 77 BE 20 00 

; YOU_ARE_IN_A_CHAMBER_WHOSE_WALL_CONTAINS_A_PICTURE_OF_A_MAN_____WEARING_THE_LUNAR_DISK_ON_HIS_HEAD.__HE_IS_THE_GOD_
; KHONS,_THE___MOON_GOD.[CR]
6682: 2D C7 DE 94 14 4B 5E 83 96 DA 14 64 48 23 62 29 
6692: D1 9B B7 0E D0 05 8A 1E A0 D0 47 C3 B5 E3 16 0F 
66A2: 56 5B B1 C3 9E 4F 45 83 48 3B 13 F7 17 33 49 AB 
66B2: 98 5F BE 4F 16 D4 97 03 15 8B B8 03 A0 95 73 9F 
66C2: 15 17 47 4A 13 4B 5E D6 B5 DB 72 36 6E 1A 16 1D 
66D2: A0 16 EE DB 72 4F 13 40 A0 81 15 44 2E 00 

; YOU_ARE_IN_A_LONG_SLOPING_CORRIDOR_WITH_RAGGED_WALLS._ [CR]
66E0: 12 C7 DE 94 14 4B 5E 83 96 49 16 AB 98 C9 B8 90 
66F0: A5 C5 6A BC A0 09 79 99 AF 82 7B 2B 17 F7 6C 19 
6700: 58 46 48 5B BB 20 00 

; YOU_ARE_IN_A_CUL-DE-SAC_ABOUT_EIGHT_FEET_ACROSS.[CR]
6707: 10 C7 DE 94 14 4B 5E 83 96 E7 14 56 8F A5 63 CB 
6717: 46 B9 46 73 C6 C9 60 33 75 67 66 03 BC B9 55 EF 
6727: B9 00 

; YOU_ARE_IN_THE_CHAMBER_OF_HORUS,_A_LONG_EAST/WEST_PASSAGE_WITH__HOLES_EVERYWHERE.__TO_EXPLORE_AT_RANDOM,_SELECT_
; NORTH,_SOUTH,___UP,_OR_DOWN.[CR]
6729: 2E C7 DE 94 14 4B 5E 96 96 DB 72 1B 54 AF 91 91 
6739: AF 8A 64 BF A0 33 BB 4E 45 11 A0 23 15 F8 B9 B5 
6749: D0 12 BC 65 49 77 47 FB 17 53 BE A9 15 F5 8B 38 
6759: 15 43 62 1F D1 7F B1 56 13 C7 9C A6 D8 AF A0 96 
6769: 14 2B 17 49 98 B3 95 AE B7 E6 5F 99 16 C2 B3 15 
6779: EE 36 A1 73 76 57 13 73 A8 A3 A0 89 5B 4E 2E 00 

; YOU_ARE_IN_A_LARGE_LOW_CIRCULAR_CHAMBER_WHOSE_FLOOR_IS_AN_______IMMENSE_SLAB_FALLEN_FROM_THE_CEILING.__EAST_AND_
; WEST_THERE_ONCE_WHERE_LARGE_PASSAGES,_BUT_THEY_ARE_NOW_FILLED_WITH_SAND.________LOW_SMALL_PASSAGES_GO_NORTH_
; AND_SOUTH.[CR]
6789: 4C C7 DE 94 14 4B 5E 83 96 3B 16 B7 B1 49 16 C5 
6799: CE 2D 7B 3B C5 85 AF 4F 72 74 4D FA 17 D7 A0 56 
67A9: 15 44 A0 D5 15 90 14 3B 13 3B 13 CF 15 30 92 9B 
67B9: B7 BB B8 88 4B 46 48 83 61 79 68 56 90 DB 72 AB 
67C9: 53 90 8C 5B 70 23 15 F3 B9 8E 48 F7 17 F3 B9 5F 
67D9: BE 5B B1 0D A0 59 5E F4 72 4E 5E 31 49 52 5E 65 
67E9: 49 77 47 33 BB F6 4F 82 17 3B 63 2F 49 99 16 C8 
67F9: CE 46 7A F3 5F 56 D1 15 71 8E 48 3B F4 3B 13 3B 
6809: 13 89 8D 5F 17 46 48 DB 16 D3 B9 B5 6C 81 15 99 
6819: 16 C2 B3 90 14 15 58 36 A1 48 2E 00 

; YOU_ARE_IN_THE_PRIEST'S_BEDROOM.__THE_WALLS_ARE_COVERED_WITH____CURTAINS,_THE_FLOOR_WITH_A_THICK_PILE_
; CARPET.__MOSS_COVERS_THE__CEILING.[CR]
6825: 2D C7 DE 94 14 4B 5E 96 96 DB 72 F3 A6 66 62 CB 
6835: 23 66 4D 01 B3 DB 95 82 17 59 5E 46 48 C3 B5 5B 
6845: B1 48 55 2F 62 19 58 82 7B 3B 13 E7 14 BB B3 9D 
6855: 7A 16 EE DB 72 89 67 A3 A0 56 D1 03 71 82 17 DD 
6865: 78 E3 16 DB 8B 14 53 F6 A4 3B F4 C5 93 C5 B5 4F 
6875: A1 8B B3 5F BE 45 13 CE 60 91 7A 2E 00 

; THIS_IS_THE_CHAMBER_OF_THE_HIGH_PRIEST.___ANCIENT_DRAWINGS_COVERTHE_WALLS.__AN_EXTREMELY_TIGHT_TUNNEL_LEADS_
; WEST.__IT_LOOKS_LIKEA_TIGHT_SQUEEZE.__ANOTHER_PASSAGE_LEADS_SE.[CR]
6882: 39 63 BE CB B5 D6 B5 DB 72 1B 54 AF 91 91 AF 96 
6892: 64 DB 72 89 73 12 71 07 B2 17 BA 3B 13 8D 48 30 
68A2: 79 06 BC D9 B0 91 7A C5 B5 4F A1 C2 B3 59 5E 46 
68B2: 48 5B BB 90 14 3A 15 EF BF 2E 92 56 DB 7A 79 16 
68C2: BC 98 C5 33 61 E3 8B 0B 5C B5 D0 9B C1 D6 15 49 
68D2: 16 A5 9F 43 16 A3 85 83 17 2E 6D 63 17 27 C4 7F 
68E2: E3 43 13 06 9A F4 72 DB 16 D3 B9 9B 6C E3 8B 0B 
68F2: 5C BF B7 00 

; YOU_ARE_IN_THE_HIGH_PRIEST'S_TREASURE_ROOM_LIT_BY_AN_EERIE_GREENLIGHT.__A_NARROW_TUNNEL_EXITS_TO_THE_EAST.[CR]
68F6: 23 C7 DE 94 14 4B 5E 96 96 DB 72 89 73 12 71 07 
6906: B2 F5 B9 D6 B5 63 B1 34 BA 54 5E 3F A0 43 16 04 
6916: BC 43 DB 87 96 33 62 49 5E 67 B1 83 99 2E 6D 3B 
6926: F4 50 45 3C 49 6B A1 70 C0 6E 98 3A 15 8D 7B 89 
6936: 17 82 17 47 5E 66 49 2E 00 

; YOU_ARE_AT_THE_EAST_END_OF_THE_TWOPIT_ROOM.__THE_FLOOR_HERE_IS__LITTERED_WITH_THIN_ROCK_SLABS,_WHICH_MAKE_IT_
; EASY_TO_DESCEND_THEPITS.__THERE_IS_A_PATH_HERE_BYPASSING_THE_PITS_TO_CONNECT_______PASSAGES_EAST_AND_WEST.__THERE_
; ARE_HOLES_ALL_OVER,_BUT_THE_ONLY_BIG_ONE_IS_ON_THE_WALL_DIRECTLY_OVER_THE_WEST_PIT_WHERE_YOU_____CAN'T_GET_TO_IT.[CR]
693F: 70 C7 DE 94 14 43 5E 16 BC DB 72 95 5F 07 BC 33 
694F: 98 C3 9E 5F BE 91 17 63 A0 14 BC 3F A0 3B F4 5F 
695F: BE 56 15 44 A0 9F 15 5B B1 4B 7B 43 16 3F C0 66 
696F: B1 FB 17 53 BE 63 BE 94 96 5D 9E 5E 17 BD 46 19 
697F: EE 85 73 0F 71 17 48 D6 15 23 15 BB BA 6B BF F5 
698F: 59 B0 53 16 58 F2 72 8D 7B 3B F4 5F BE 5B B1 4B 
699F: 7B 52 45 82 49 9F 15 5B B1 92 50 65 49 91 7A 82 
69AF: 17 52 5E 8D 7B 89 17 E1 14 CF 99 F3 55 3B 13 3B 
69BF: 13 55 A4 09 B7 4B 62 95 5F 03 BC 33 98 B5 D0 9B 
69CF: C1 82 17 2F 62 94 14 4A 5E BF 9F C3 B5 F3 8C 4F 
69DF: A1 F3 B4 F6 4F 82 17 51 5E 93 99 B3 14 D1 6A 5B 
69EF: 98 4B 7B 03 A0 5F BE F3 17 F3 8C 94 5A E6 5F FB 
69FF: 8E 4F A1 96 AF DB 72 B5 D0 12 BC 73 7B 1F D1 5B 
6A0F: B1 C7 DE 3B 13 45 13 85 48 09 BC 73 62 6B BF 97 
6A1F: 7B 00 

; YOU_ARE_AT_THE_BOTTOM_OF_THE_EASTERN_PIT_IN_THE_TWOPIT_ROOM.[CR]
6A21: 14 C7 DE 94 14 43 5E 16 BC DB 72 06 4F 7F BF B8 
6A31: 16 82 17 47 5E 66 49 38 62 E3 16 0B BC 96 96 DB 
6A41: 72 C1 C0 96 A5 39 17 FF 9F 00 

; YOU_ARE_AT_THE_WEST_END_OF_THE_TWOPIT_ROOM.__THERE_IS_A_LARGE___HOLE_IN_THE_WALL_ABOVE_THE_PIT_AT_THIS_END_
; OF_THE_ROOM.[CR]
6A4B: 27 C7 DE 94 14 43 5E 16 BC DB 72 B5 D0 07 BC 33 
6A5B: 98 C3 9E 5F BE 91 17 63 A0 14 BC 3F A0 3B F4 5F 
6A6B: BE 5B B1 4B 7B 4E 45 31 49 3B 5E A9 15 DB 8B 83 
6A7B: 7A 5F BE F3 17 F3 8C B9 46 5B CA 5F BE E3 16 03 
6A8B: BC 16 BC 95 73 30 15 11 58 96 64 DB 72 01 B3 4D 
6A9B: 2E 00 

; YOU_ARE_AT_THE_BOTTOM_OF_THE_WEST_PIT_IN_THE_TWOPIT_ROOM.__THEREIS_A_LARGE_HOLE_IN_THE_WALL_ABOUT_TWENTY_FIVE_
; FEET_ABOVE_YOU.[CR]
6A9D: 29 C7 DE 94 14 43 5E 16 BC DB 72 06 4F 7F BF B8 
6AAD: 16 82 17 59 5E 66 62 E3 16 0B BC 96 96 DB 72 C1 
6ABD: C0 96 A5 39 17 FF 9F 56 13 F4 72 D5 60 7B 14 54 
6ACD: 8B 9B 6C 7E 74 4B 5E 96 96 DB 72 0E D0 03 8A 07 
6ADD: 4F 16 BC B0 D0 FB C0 18 67 48 5E 36 60 84 14 4F 
6AED: A1 51 18 55 2E 00 

; YOU_ARE_IN_A_LONG,_NARROW_CORRIDOR_STRETCHING_OUT_OF_SIGHT_TO___THE_WEST.__AT_THE_EASTERN_END_IS_A_HOLE_THROUGH_WHICH_YOU_
; CAN___SEE_A_PROFUSION_OF_LEAVES.[CR]
6AF3: 33 C7 DE 94 14 4B 5E 83 96 49 16 CE 98 8B 16 79 
6B03: B3 C5 CE BC A0 09 79 95 AF EF BF 9A BD 91 7A C7 
6B13: 16 11 BC 95 64 7A 79 16 BC BB 9C 82 17 59 5E 66 
6B23: 62 3B F4 73 49 5F BE 23 15 FF B9 C3 B2 8E 61 D5 
6B33: 15 7B 14 7E 74 56 5E F9 74 7A C4 FA 17 DA 78 51 
6B43: 18 45 C2 83 48 55 13 1B 60 52 45 F8 B2 5B C6 03 
6B53: A0 C3 9E E3 8B 75 CA 2E 00 

; YOU_ARE_IN_THE_CHAMBER_OF_OSIRIS._THE_CEILING_IS_TOO_HIGH_UP_FORYOUR_LAMP_TO_SHOW_IT.__PASSAGES_LEAD_
; EAST,_NORTH,_AND_SOUTH.[CR]
6B5C: 29 C7 DE 94 14 4B 5E 96 96 DB 72 1B 54 AF 91 91 
6B6C: AF 91 64 54 B8 6F 7B 82 17 45 5E CE 60 91 7A D5 
6B7C: 15 89 17 CA 9C 7A 79 B2 17 59 15 91 B4 23 C6 4F 
6B8C: 8B 16 A3 D5 9C 89 74 D6 15 3B F4 55 A4 09 B7 4B 
6B9C: 62 E3 8B 07 58 66 49 10 EE BE A0 73 76 8E 48 61 
6BAC: 17 82 C6 2E 00 

; THE_PASSAGE_HERE_IS_BLOCKED_BY_A_FALLEN_BLOCK.[CR]
6BB1: 0F 5F BE DB 16 D3 B9 9B 6C F4 72 4B 5E C4 B5 75 
6BC1: 8D A6 85 C3 14 7B 14 CE 65 F0 8B B6 14 5D 9E 2E 
6BD1: 00 

; YOU_ARE_IN_THE_CHAMBER_OF_NEKHEBET,_A_WOMAN_WITH_THE_HEAD_OF_A__VULTURE,_WEARING_THE_CROWN_OF_EGYPT.__A_PASSAGE_
; EXITS_TO_THE____SOUTH.[CR]
6BD2: 2C C7 DE 94 14 4B 5E 96 96 DB 72 1B 54 AF 91 91 
6BE2: AF 90 64 1A 61 AF 5F 73 C1 59 45 E3 9F 99 96 82 
6BF2: 7B 82 17 4A 5E 86 5F B8 16 7B 14 DF 17 4F 8E 7E 
6C02: B1 F7 17 33 49 AB 98 5F BE E4 14 80 A1 B8 16 29 
6C12: 15 EE DE 3B F4 52 45 65 49 77 47 3A 15 8D 7B 89 
6C22: 17 82 17 3B 5E 55 13 36 A1 48 2E 00         
```

# Object Descriptions

```code
; These are the long (in a room description) and short (in the inventory) strings for each object.

ObjDescriptions:

;Description for objects: 14 "Lamp (not lit)",44 "Lamp (dead)"

; THERE_IS_A_SHINY_BRASS_LAMP_NEARBY.[CR]
6C2E: 0B 5F BE 5B B1 4B 7B 55 45 90 73 44 DB D5 B0 CE 
6C3E: B5 72 48 8F 16 2C 49 59 2E 00 

; BRASS_LANTERN[CR]
6C48: 04 6B 4F CB B9 50 8B F4 BD 4E 00 

; THERE_IS_A_LAMP_SHINING_NEARBY.[CR]
6C53: 0A 5F BE 5B B1 4B 7B 4E 45 72 48 5A 17 93 7A AB 
6C63: 98 63 98 03 B1 2E 00 

; BRASS_LANTERN[CR]
6C6A: 04 6B 4F CB B9 50 8B F4 BD 4E 00 

; THERE_IS_A_SMALL_STATUE_BOX_DISCARDED_NEARBY.[CR]
6C75: 0F 5F BE 5B B1 4B 7B 55 45 8E 91 15 8A 56 BD 1B 
6C85: C4 0A 4F 03 15 53 B7 3F B1 10 58 94 5F 9F 50 00 

; STATUE_BOX[CR]
6C95: 03 FB B9 67 C0 B9 14 58 00 

; A_THREE_FOOT_SCEPTER_WITH_AN_ANKH_ON_AN_END_LIES_NEARBY.[CR]
6C9E: 12 56 45 EF 74 48 5E 46 A0 55 17 EE 61 23 62 56 
6CAE: D1 03 71 83 96 5A 99 C0 16 90 14 30 15 0E 58 35 
6CBE: 79 8F 16 2C 49 59 2E 00 

; SCEPTER[CR]
6CC6: 02 57 B7 3F A7 52 00 

; A_STATUE_OF_THE_BIRD_GOD_IS_SITTING_HERE.[CR]
6CCD: 0D 55 45 56 BD 1B C4 C3 9E 5F BE B3 14 33 B1 36 
6CDD: 6E D5 15 5B 17 43 C0 AB 98 F4 72 45 2E 00 

; THERE_IS_A_BIRD_STATUE_IN_THE_BOX.[CR]
6CEB: 0B 5F BE 5B B1 4B 7B 44 45 2E 7B 66 17 8F 49 4B 
6CFB: 5E 96 96 DB 72 0A 4F 2E 00 

; BIRD_STATUE_IN_BOX[CR]
6D04: 06 14 4E 15 58 56 BD 1B C4 83 7A 0A 4F 00 

; A_SMALL_VELVET_PILLOW_LIES_ON_THE_FLOOR.[CR]
6D12: 0D 55 45 8E 91 18 8A 50 61 73 62 8E A5 89 8D 43 
6D22: 16 4B 62 03 A0 5F BE 56 15 44 A0 2E 00 

; VELVET_PILLOW[CR]
6D2F: 04 6E CA 76 CA E3 16 09 8D 57 00 

; A_HUGE_GREEN_FIERCE_SERPENT_BARS_THE_WAY![CR]
6D3A: 0D 4A 45 77 C4 84 15 30 60 53 15 2D 62 55 5E 3A 
6D4A: 62 9E 61 AB 14 8B B3 5F BE F3 17 59 21 00 

; A_STONE_BRIDGE_NOW_SPANS_THE_BOTTOMLESS_PIT.[CR]
6D58: 0E 55 45 80 BF 44 5E 06 B2 9B 6C 09 9A 62 17 9D 
6D68: 48 82 17 44 5E 0E A1 EE 9F 65 62 E3 16 54 2E 00 

; THERE_IS_A_SARCOPHAGUS_HERE_WITH_IT'S_COVER_TIGHTLY_CLOSED.[CR]
6D78: 13 5F BE 5B B1 4B 7B 55 45 2D 49 62 A0 87 47 CA 
6D88: B5 2F 62 FB 17 53 BE 75 7B C5 B5 4F A1 96 AF 7A 
6D98: 79 13 BF DE 14 D7 A0 44 2E 00 

; SARCOPHAGUS_>GROAN<[CR]
6DA2: 06 14 B7 42 55 49 72 4B C6 84 2E 10 9E 3C 00 

; THERE_ARE_A_FEW_RECENT_ISSUES_OF_"EGYPTIAN_WEEKLY"_MAGAZINE_HERE[CR]
6DB1: 15 5F BE 5B B1 2F 49 7B 14 79 66 2F 17 B0 53 0B 
6DC1: BC E7 B9 4B 62 C3 9E 69 1B EE DE 90 78 F7 17 1E 
6DD1: 61 63 DB 89 91 73 4A 5B 98 F4 72 45 00 

; "EGYPTIAN_WEEKLY"[CR]
6DDE: 05 69 1B EE DE 90 78 F7 17 1E 61 59 22 00 

; THERE_IS_FOOD_HERE.[CR]
6DEC: 06 5F BE 5B B1 4B 7B 01 68 0A 58 2F 62 2E 00 

; TASTY_FOOD[CR]
6DFB: 03 55 BD FB C0 01 68 44 00 

; THERE_IS_A_BOTTLE_HERE.[CR]
6E04: 07 5F BE 5B B1 4B 7B 44 45 0E A1 DB 8B F4 72 45 
6E14: 2E 00 

; SMALL_BOTTLE[CR]
6E16: 04 E3 B8 F3 8C 06 4F FF BE 00 

; THERE_IS_WATER_IN_THE_BOTTLE.[CR]
6E20: 09 5F BE 5B B1 4B 7B 16 D0 23 62 83 7A 5F BE B9 
6E30: 14 46 C0 45 2E 00 

; WATER_IN_THE_BOTTLE[CR]
6E36: 06 16 D0 23 62 83 7A 5F BE B9 14 46 C0 45 00 

; THERE_IS_A_TINY_PLANT_IN_THE_PIT,_MURMURING_"WATER,_WATER,_..."[CR]
6E45: 15 5F BE 5B B1 4B 7B 56 45 A3 7A E6 16 9E 48 D0 
6E55: 15 82 17 52 5E 96 7B 77 16 B7 B2 10 B2 BC 6A 16 
6E65: D0 46 62 F3 17 F4 BD 1F EE DC F9 00 

; THERE_IS_A_TWELVE_FOOT_BEAN_STALK_STRETCHING_UP_OUT_OF_THE_PIT,_BELLOWING_"WATER..._WATER..."[CR]
6E71: 1F 5F BE 5B B1 4B 7B 56 45 AE D0 5B CA 01 68 04 
6E81: BC 90 5F 66 17 45 48 66 17 76 B1 23 54 AB 98 D3 
6E91: C5 36 A1 B8 16 82 17 52 5E 96 7B AF 14 09 8D 50 
6EA1: D1 BC 6A 16 D0 47 62 DB F9 16 D0 47 62 DC F9 00 

; THERE_IS_A_GIGANTIC_BEAN_STALK_STRETCHING_ALL_THE_WAY_UP_TO_THE_HOLE.[CR]
6EB1: 17 5F BE 5B B1 4B 7B 49 45 73 79 C3 9A C4 51 90 
6EC1: 5F 66 17 45 48 66 17 76 B1 23 54 AB 98 46 48 82 
6ED1: 17 59 5E 3B 4A D3 C5 6B BF 5F BE A9 15 FF 8B 00 

; THERE_IS_A_MASSIVE_VENDING_MACHINE_HERE.__THE_INSTRUCTIONS_ON_ITREAD-_"DROP_COINS_HERE_TO_
; RECIEVE_FRESH_BATTERIES".[CR]
6EE1: 26 5F BE 5B B1 4B 7B 4F 45 65 49 CF 7B CF 17 43 
6EF1: 98 AB 98 85 91 90 73 4A 5E 2F 62 3B F4 5F BE D0 
6F01: 15 0C BA E6 C3 C0 7A D1 B5 8B 96 EF BF 15 47 6E 
6F11: 13 02 B3 E1 14 9D 7A 9F 15 5B B1 6B BF 65 B1 38 
6F21: 79 48 5E 75 B1 04 71 8E 49 33 62 4C 62 2E 00 

; THERE_ARE_FRESH_BATTERIES_HERE.[CR]
6F30: 0A 5F BE 5B B1 2F 49 5C 15 5A 62 AB 14 3F C0 07 
6F40: B2 CA B5 2F 62 2E 00 

; BATTERIES[CR]
6F47: 03 D6 4C F4 BD 35 79 00 

; SOME_WORN-OUT_BATTERIES_HAVE_BEEN_DISCARDED_NEARBY.[CR]
6F4F: 11 3F B9 59 5E B8 A0 47 EB 04 BC 8E 49 33 62 4B 
6F5F: 62 58 72 44 5E 30 60 03 15 53 B7 3F B1 10 58 94 
6F6F: 5F 9F 50 00 

; BATTERIES[CR]
6F73: 03 D6 4C F4 BD 35 79 00 

; THERE_IS_A_LARGE_SPARKLING_NUGGET_OF_GOLD_HERE![CR]
6F7B: 0F 5F BE 5B B1 4B 7B 4E 45 31 49 55 5E 54 A4 C3 
6F8B: 86 AB 98 E9 9A B6 6C B8 16 81 15 B3 8B F4 72 45 
6F9B: 21 00 

; LARGE_GOLD_NUGGET[CR]
6F9D: 05 54 8B 9B 6C 3E 6E 10 58 79 C4 45 54 00 

; THERE_ARE_DIAMONDS_HERE![CR]
6FAB: 08 5F BE 5B B1 2F 49 03 15 71 48 4D 98 9F 15 59 
6FBB: B1 00 

; SEVERAL_DIAMONDS[CR]
6FBD: 05 B8 B7 2B 62 06 8A 8F 78 0E A0 53 00 

; THERE_ARE_BARS_OF_SILVER_HERE![CR]
6FCA: 0A 5F BE 5B B1 2F 49 AB 14 8B B3 C3 9E 4E B8 74 
6FDA: CA 9F 15 59 B1 00 

; SILVER_BARS[CR]
6FE0: 03 4E B8 74 CA AB 14 52 53 00 

; THERE_IS_PRECIOUS_JEWELRY_HERE![CR]
6FEA: 0A 5F BE 5B B1 4B 7B EF A6 51 54 4B C6 79 7F 4C 
6FFA: 61 4A DB 2F 62 21 00 

; PRECIOUS_JEWELRY[CR]
7001: 05 EF A6 51 54 4B C6 79 7F 4C 61 59 00 

; THERE_ARE_MANY_COINS_HERE![CR]
700E: 08 5F BE 5B B1 2F 49 63 16 7B 9B 3B 55 8B 9A F4 
701E: 72 45 21 00 

; RARE_COINS[CR]
7022: 03 D4 B0 45 5E 50 9F 53 00 

; THE_PHARAOH'S_TREASURE_CHEST_IS_HERE![CR]
702B: 0C 5F BE E2 16 2B 49 15 9F D6 B5 63 B1 34 BA 45 
703B: 5E F5 72 0B BC CA B5 2F 62 21 00 

; TREASURE_CHEST[CR]
7046: 04 EF BF 67 49 5B B1 1F 54 53 54 00 

; THERE_IS_A_LARGE_NEST_HERE,_FULL_OF_GOLDEN_EGGS![CR]
7052: 10 5F BE 5B B1 4B 7B 4E 45 31 49 50 5E 66 62 9F 
7062: 15 7E B1 5F 15 F3 8C C3 9E 3E 6E F0 59 29 15 C9 
7072: 6E 00 

; GOLDEN_EGGS[CR]
7074: 03 3E 6E F0 59 29 15 47 53 00 

; THERE_IS_A_JEWEL-ENCRUSTED_KEY_HERE![CR]
707E: 0C 5F BE 5B B1 4B 7B 4C 45 F7 62 57 8F 24 98 66 
708E: C6 F3 5F BB 85 9F 15 59 B1 00 

; JEWELED_KEY[CR]
7098: 03 79 7F 3F 61 0D 58 45 59 00 

; THERE_IS_A_DELICATE,_PRECIOUS,_VASE_HERE![CR]
70A2: 0D 5F BE 5B B1 4B 7B 46 45 43 61 16 53 B3 63 EF 
70B2: A6 51 54 6E C6 CB 17 9B B7 F4 72 45 21 00 

; VASE[CR]
70C0: 01 D5 C9 45 00 

; THE_VASE_IS_NOW_RESTING,_DELICATELY,_ON_A_VELVET_PILLOW.[CR]
70C5: 12 5F BE CB 17 9B B7 4B 7B 09 9A 2F 17 03 BA CE 
70D5: 98 FF 14 85 8C 7F 49 1E 8F C0 16 7B 14 6E CA 76 
70E5: CA E3 16 09 8D 57 2E 00 

; THE_FLOOR_IS_LITTERED_WITH_WORTHLESS_SHARDS_OF_POTTERY.[CR]
70ED: 12 5F BE 56 15 44 A0 D5 15 43 16 3F C0 66 B1 FB 
70FD: 17 53 BE 44 D2 66 BE 65 62 5A 17 2E 49 D1 B5 92 
710D: 64 0E A1 43 62 2E 00 

; THERE_IS_AN_EMERALD_HERE_THE_SIZE_OF_A_PLOVER'S_EGG![CR]
7114: 11 5F BE 5B B1 4B 7B 83 48 67 61 CE B0 0A 58 2F 
7124: 62 82 17 55 5E 6F 7C B8 16 7B 14 09 A6 74 CA CB 
7134: 23 79 60 21 00 

; EGG-SIZED_EMERALD[CR]
7139: 05 79 60 DB EB 66 E3 2F 15 2B 62 4C 44 00 

; OFF_TO_ONE_SIDE_LIES_A_GLISTENING_PEARL![CR]
7147: 0D D0 9E 89 17 C0 16 55 5E FF 78 43 16 4B 62 49 
7157: 45 95 8C F0 BD 91 7A DF 16 36 49 21 00 

; GLISTENING_PEARL[CR]
7164: 05 C3 6D FF B9 10 99 D2 6A 94 5F 4C 00 

; YOU_ARE_AT_THE_BOTTOM_OF_THE_PIT_WITH_A_BROKEN_NECK.[CR]
7171: 11 C7 DE 94 14 43 5E 16 BC DB 72 06 4F 7F BF B8 
7181: 16 82 17 52 5E 73 7B 56 D1 03 71 BC 14 97 9F 90 
7191: 96 DD 5F 2E 00 

; THE_CRACK_IS_FAR_TOO_SMALL_FOR_YOU_TO_FOLLOW.[CR]
7196: 0F 5F BE E4 14 DD 46 D5 15 4B 15 96 AF 2B A0 E3 
71A6: B8 F3 8C 04 68 51 18 56 C2 C8 9C C6 9F 8F A1 00 

; THE_DOME_IS_UNCLIMBABLE.[CR]
71B6: 08 5F BE 09 15 1B 92 4B 7B 8D C5 8F 8C C4 4C FF 
71C6: 8B 00 

; I_RESPECTFULLY_SUGGEST_YOU_GO_ACROSS_THE_BRIDGE_INSTEAD_OF______JUMPING.[CR]
71C8: 18 54 77 62 62 E6 5F EE 68 FB 8E 29 BA B5 6C 1B 
71D8: BC 1B A1 2B 6E E4 46 E5 A0 82 17 44 5E 06 B2 9B 
71E8: 6C 9D 7A E3 BD 11 58 7B 64 3B 13 FF 15 E3 93 CF 
71F8: 98 00 

; YOU_DIDN'T_MAKE_IT.[CR]
71FA: 06 C7 DE 03 15 45 5B 0F BC 17 48 D6 15 2E 00 

; THERE_IS_NO_WAY_ACROSS_THE_BOTTOMLESS_PIT.[CR]
7209: 0E 5F BE 5B B1 4B 7B EB 99 1B D0 85 14 05 B3 D6 
7219: B5 DB 72 06 4F 7F BF F5 8B D2 B5 97 7B 00 

; YOU_CAN'T_GET_BY_THE_SERPENT.[CR]
7227: 09 C7 DE D3 14 E6 96 77 15 04 BC 56 DB DB 72 B4 
7237: B7 F0 A4 54 2E 00 

; YOU_HAVE_CRAWLED_THROUGH_A_VERY_LOW_WIDE_PASSAGE_PARALLEL_TO_ANDNORTH_OF_THE_
; HALL_OF_GODS.[CR]
723D: 1E C7 DE 9B 15 5B CA AB 55 BF D1 16 58 F9 74 7A 
724D: C4 7B 14 74 CA 4E DB 6B A1 46 D1 52 5E 65 49 77 
725D: 47 DB 16 CE B0 EE 8B 89 17 90 14 59 5B C2 B3 B8 
726D: 16 82 17 4A 5E 46 48 B8 16 81 15 2F 5C 00 

; YOU_DON'T_FIT_THROUGH_TWO-INCH_SLIT![CR]
727B: 0C C7 DE 09 15 E6 96 53 15 16 BC F9 74 7A C4 91 
728B: 17 1B A2 1A 98 5E 17 71 7B 00 

; YOU_HAVE_CRAWLED_AROUND_IN_SOME_LITTLE_HOLES_AND_WOUND_UP_BACK__IN_THE_MAIN_
; PASSAGE.[CR]
7295: 1C C7 DE 9B 15 5B CA AB 55 BF D1 03 58 07 B3 33 
72A5: 98 83 7A 3F B9 4E 5E 8E 7B DB 8B 7E 74 4B 62 8E 
72B5: 48 01 18 8E C5 B2 17 AB 14 8B 54 D0 15 82 17 4F 
72C5: 5E D0 47 DB 16 D3 B9 BF 6C 00 

; YOU_HAVE_CRAWLED_AROUND_IN_SOME_LITTLE_HOLES_AND_FOUND_YOUR_WAY_BLOCKED_BY_A_FALLEN_
; SLAB.__YOU_ARE_NOW_BACK_IN_THE_MAIN_PASSAGE.[CR]
72CF: 2A C7 DE 9B 15 5B CA AB 55 BF D1 03 58 07 B3 33 
72DF: 98 83 7A 3F B9 4E 5E 8E 7B DB 8B 7E 74 4B 62 8E 
72EF: 48 59 15 8E C5 51 18 23 C6 1B D0 B6 14 5D 9E F3 
72FF: 5F 7B 50 48 45 46 48 83 61 BB B8 1B 51 51 18 43 
730F: C2 5B B1 09 9A AB 14 8B 54 83 7A 5F BE 63 16 83 
731F: 7A 55 A4 09 B7 45 2E 00 

; YOU_CAN'T_FIT_THIS_BIG_SARCOPHAGUS_THROUGH_THAT_LITTLE_PASSAGE![CR]
7327: 15 C7 DE D3 14 E6 96 53 15 16 BC 95 73 B3 14 D5 
7337: 6A 2D 49 62 A0 87 47 D6 B5 F9 74 7A C4 82 17 73 
7347: 49 96 8C FF BE DB 16 D3 B9 99 6C 00 

; SOMETHING_YOU'RE_CARRYING_WON'T_FIT_THROUGH_THE_TUNNEL_WITH_YOU.YOU'D_BEST_TAKE_
; INVENTORY_AND_DROP_SOMETHING.[CR]
7353: 24 3F B9 82 62 91 7A 51 18 A4 C2 45 5E 3C 49 D0 
7363: DD D9 6A 05 A0 08 BC 73 7B 6C BE 29 A1 16 71 DB 
7373: 72 70 C0 6E 98 FB 17 53 BE C7 DE 51 F9 96 C2 AF 
7383: 14 F3 B9 4D BD 4B 5E 0F 9B C9 9A 7B B4 8E 48 0C 
7393: 15 53 A0 3F B9 82 62 91 7A 2E 00 

; YOU_CLAMBER_UP_THE_PLANT_AND_SCURRY_THROUGH_THE_HOLE_AT_THE_TOP.[CR]
739E: 15 C7 DE DE 14 64 48 23 62 D3 C5 5F BE E6 16 9E 
73AE: 48 90 14 15 58 34 56 7B B4 6C BE 29 A1 16 71 DB 
73BE: 72 7E 74 43 5E 16 BC DB 72 82 BF 2E 00 

; YOU'VE_CLIMBED_UP_THE_PLANT_AND_OUT_OF_THE_PIT.[CR]
73CB: 0F C7 DE 4F 24 DE 14 64 7A F3 5F D3 C5 5F BE E6 
73DB: 16 9E 48 90 14 11 58 73 C6 C3 9E 5F BE E3 16 54 
73EB: 2E 00 

; THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]
73ED: 0F 5F BE 5B B1 4B 7B EB 99 1B D0 59 15 9B AF 1B 
73FD: A1 6B BF 2B 6E 5B BE 06 BC 2F 7B 03 56 27 A0 00 

; I_DON'T_KNOW_IN_FROM_OUT_HERE.__USE_COMPASS_POINTS.[CR]
740D: 11 46 77 05 A0 0D BC 09 9A D0 15 5C 15 DB 9F 36 
741D: A1 9F 15 7F B1 57 13 9B B7 3F 55 55 A4 D2 B5 50 
742D: 9F 2F C0 00 

; I_AM_UNSURE_HOW_YOU_ARE_FACING.__USE_COMPASS_POINTS.[CR]
7431: 11 43 77 57 90 A7 9A 5B B1 89 74 51 18 43 C2 5B 
7441: B1 C5 65 91 7A 3B F4 57 C6 E1 14 DB 93 CB B9 7B 
7451: A6 CD 9A 2E 00 

; NOTHING_HAPPENS.[CR]
7456: 05 06 9A 90 73 CA 6A EA 48 9D 61 2E 00 

; I_DON'T_KNOW_HOW.[CR]
7463: 05 46 77 05 A0 0D BC 09 9A A9 15 57 2E 00 

; I_DON'T_KNOW_HOW_TO_APPLY_THAT_WORD_HERE.[CR]
7471: 0D 46 77 05 A0 0D BC 09 9A A9 15 D6 CE C3 9C A6 
7481: A6 56 DB 56 72 01 18 33 B1 F4 72 45 2E 00 

; YOUR_LAMP_IS_NOW_ON.[CR]
748F: 06 C7 DE 8E AF 72 48 D5 15 99 16 D1 CE 4E 2E 00 

; YOU_HAVE_NO_SOURCE_OF_LIGHT.[CR]
749F: 09 C7 DE 9B 15 5B CA EB 99 47 B9 17 B1 B8 16 43 
74AF: 16 2E 6D 2E 00 

; YOUR_LAMP_IS_NOW_OFF.[CR]
74B4: 07 C7 DE 8E AF 72 48 D5 15 99 16 D1 CE A7 66 00 

; I'M_AS_CONFUSED_AS_YOU_ARE.[CR]
74C4: 09 9F 77 95 14 E1 14 9F 98 A6 B7 95 14 51 18 43 
74D4: C2 7F B1 00 

; I_CAN_ONLY_TELL_YOU_WHAT_YOU_SEE_AS_YOU_MOVE_ABOUT_AND__________MANIPULATE_THINGS.__I_CAN_
; NOT_TELL_YOU_WHERE_REMOTE_THINGS_ARE.[CR]
74D8: 2A 45 77 83 48 16 A0 56 DB 46 61 51 18 59 C2 56 
74E8: 72 51 18 55 C2 1B 60 4B 49 C7 DE 71 16 5B CA B9 
74F8: 46 73 C6 8E 48 3B 13 3B 13 3B 13 63 16 12 99 3B 
7508: C5 DB BD 63 BE C5 98 3B F4 45 77 83 48 06 9A 7F 
7518: 17 F3 8C C7 DE FA 17 2F 62 2F 17 C6 93 56 5E 90 
7528: 73 CB 6E 2F 49 2E 00 

; OK_[CR]
752F: 01 8B 9F 00 

; SORRY,_BUT_I_NO_LONGER_SEEM_TO_REMEMBER_HOW_IT_WAS_YOU_GOT_HERE.[CR]
7533: 15 44 B9 9E B4 BF 14 0B BC 99 16 49 16 B7 98 95 
7543: AF 2F 60 89 17 2F 17 2F 92 74 4D A9 15 CB CE 19 
7553: BC 4B 49 C7 DE 81 15 0A BC 2F 62 2E 00 

; YOU_ARE_ALREADY_CARRYING_IT.[CR]
7560: 09 C7 DE 94 14 43 5E EF 8D 13 47 D3 14 83 B3 91 
7570: 7A D6 15 2E 00 

; YOU_CAN'T_CARRY_ANYTHING_MORE.__YOU'LL_HAVE_TO_DROP_SOMETHING___FIRST.[CR]
7575: 17 C7 DE D3 14 E6 96 D3 14 83 B3 90 14 82 DF 91 
7585: 7A 71 16 7F B1 5B 13 1D A1 F3 8C 58 72 56 5E C6 
7595: 9C 02 B3 61 17 36 92 90 73 BB 6A 53 15 A6 B3 2E 
75A5: 00 

; YOU'RE_NOT_CARRYING_ANYTHING.[CR]
75A6: 09 C7 DE AF 23 99 16 05 BC 3C 49 D0 DD C3 6A 96 
75B6: 9B 90 73 47 2E 00 

; YOU_ARE_CURRENTLY_HOLDING_THE_FOLLOWING:[CR]
75BC: 0D C7 DE 94 14 45 5E 3C C6 9E 61 FB 8E 7E 74 90 
75CC: 5A D6 6A DB 72 FE 67 89 8D 91 7A 3A 00 

; DON'T_BE_RIDICULOUS![CR]
75D9: 06 80 5B F3 23 5B 4D 06 B2 E7 78 87 8D 53 21 00 

; YOUR_BOTTLE_IS_EMPTY_AND_THE_GROUND_IS_WET.[CR]
75E9: 0E C7 DE 84 AF 0E A1 DB 8B 4B 7B 72 61 FB C0 8E 
75F9: 48 82 17 49 5E 07 B3 33 98 4B 7B B6 D0 2E 00 

; YOU_CAN'T_POUR_THAT.[CR]
7608: 06 C7 DE D3 14 E6 96 E9 16 23 C6 5B BE 54 2E 00 

; RUBBING_THE_ELECTRIC_LAMP_IS_NOT_PARTICULARLY_REWARDING.________ANYWAY,_NOTHING_
; EXCITING_HAPPENS.[CR]
7618: 20 E4 B3 10 4E D6 6A DB 72 3F 61 0C 56 CB 78 4F 
7628: 8B 0B A3 D0 B5 F3 A0 54 A4 85 BE 3B C5 93 B2 2F 
7638: 17 14 D0 90 5A 5B 70 3B 13 3B 13 90 14 F3 DF B3 
7648: E0 06 9A 90 73 C7 6A 9B D6 90 BE CA 6A EA 48 9D 
7658: 61 2E 00 

; PECULIAR.__NOTHING_UNEXPECTED_HAPPENS.[CR]
765B: 0C E5 A4 43 C5 47 49 50 13 02 A1 91 7A B0 17 2A 
766B: 63 E6 5F F3 5F 52 72 F0 A4 53 2E 00 

; THERE_IS_NOTHING_HERE_WITH_WHICH_TO_FILL_THE_BOTTLE.[CR]
7677: 11 5F BE 5B B1 4B 7B 06 9A 90 73 CA 6A 2F 62 FB 
7687: 17 53 BE 23 D1 13 54 6B BF 0E 67 16 8A DB 72 06 
7697: 4F FF BE 2E 00 

; THE_BOTTLE_IS_NOW_EMPTY.[CR]
769C: 08 5F BE B9 14 46 C0 4B 5E D0 B5 6B A1 72 61 1F 
76AC: C1 00 

; YOU_CAN'T_FILL_THAT.[CR]
76AE: 06 C7 DE D3 14 E6 96 53 15 F3 8C 5B BE 54 2E 00 

; A_GLISTENING_PEARL_FALLS_OUT_OF_THE_SARCOPHAGUS_AND_ROLLS_AWAY._THE_SARCOPHAGUS_SNAPS_
; SHUT_AGAIN.[CR]
76BE: 20 49 45 95 8C F0 BD 91 7A DF 16 36 49 4B 15 0D 
76CE: 8D C7 16 11 BC 96 64 DB 72 14 B7 42 55 49 72 4B 
76DE: C6 8E 48 39 17 0D 8D 99 14 5F 4A 82 17 55 5E 2D 
76EE: 49 62 A0 87 47 D5 B5 D2 97 D5 B5 76 75 89 14 D0 
76FE: 47 2E 00 

; I'D_ADVISE_YOU_TO_PUT_DOWN_THE_SARCOPHAGUS_BEFORE_OPENING_IT!![CR]
7701: 14 96 77 86 14 15 CB 5B 5E 1B A1 6B BF 76 A7 09 
7711: 15 03 D2 5F BE 53 17 21 B1 5B A5 35 6F AF 14 04 
7721: 68 51 5E F0 A4 91 7A D6 15 21 21 00 

; THE_SARCOPHAGUS_CREAKS_OPEN,_REVEALING_NOTHING_INSIDE.__IT______PROMPTLY_SNAPS_SHUT_
; AGAIN.[CR]
772D: 1E 5F BE 53 17 21 B1 5B A5 35 6F E4 14 8D 5F D1 
773D: B5 F0 A4 14 EE CF 62 43 48 AB 98 06 9A 90 73 CB 
774D: 6A 9B 9A FF 59 4B 13 FB BB 3B 13 EC 16 F2 9F 13 
775D: BF 60 17 ED 48 5A 17 73 C6 73 47 A7 7A 00 

; YOU_DON'T_HAVE_ANYTHING_STRONG_ENOUGH_TO_OPEN_THE_SARCOPHAGUS.[CR]
776B: 14 C7 DE 09 15 E6 96 9B 15 5B CA A3 48 63 BE AB 
777B: 98 0C BA 11 A0 30 15 29 A1 16 71 D1 9C F0 A4 82 
778B: 17 55 5E 2D 49 62 A0 87 47 53 2E 00 

; I_DON'T_KNOW_HOW_TO_LOCK_OR_UNLOCK_SUCH_A_THING.[CR]
7797: 10 46 77 05 A0 0D BC 09 9A A9 15 D6 CE CE 9C 5D 
77A7: 9E C4 16 B0 17 75 8D D5 83 DA C3 7B 14 63 BE CF 
77B7: 98 00 

; THE_BIRD_STATUE_IS_NOW_DEAD.__ITS_BODY_DISAPPEARS.[CR]
77B9: 10 5F BE B3 14 33 B1 FB B9 67 C0 D5 15 99 16 C6 
77C9: CE 86 5F 3B F4 8D 7B B9 14 FB 5C 95 5A EA 48 94 
77D9: 5F 53 2E 00 

; THE_STONE_IS_VERY_STRONG_AND_IS_IMPERVIOUS_TO_ATTACK.[CR]
77DD: 11 5F BE 66 17 0F A0 D5 15 CF 17 7B B4 0C BA 11 
77ED: A0 90 14 0B 58 CB B5 DF 93 13 B4 35 A1 89 17 96 
77FD: 14 45 BD 4B 2E 00 

; ATTACKING_THE_SERPENT_BOTH_DOESN'T_WORK_AND_IS_VERY_DANGEROUS.[CR]
7803: 14 8E 49 DD 46 91 7A 82 17 55 5E 3A 62 9E 61 B9 
7813: 14 53 BE 77 5B 05 B9 19 BC B5 A0 90 14 0B 58 D8 
7823: B5 43 62 FB 14 B7 98 07 B3 53 2E 00 

; YOU_CAN'T_BE_SERIOUS![CR]
782F: 07 C7 DE D3 14 E6 96 AF 14 57 17 11 B2 49 C6 00 

; IT_IS_BEYOND_YOUR_POWER_TO_DO_THAT.[CR]
783F: 0B 73 7B 4B 7B 7B 4D 0E A0 51 18 23 C6 89 A6 23 
784F: 62 6B BF 6B 5B 5B BE 54 2E 00 

; THANK_YOU,_IT_WAS_DELICIOUS![CR]
7859: 09 5B BE 4B 99 C7 DE 0B EE 19 BC 4B 49 EE 59 DB 
7869: 78 35 A1 21 00 

; I_THINK_I_JUST_LOST_MY_APPETITE.[CR]
786E: 0A 56 77 90 73 CB 83 FF 15 F3 B9 85 8D 0F BC 43 
787E: DB 9F A6 96 BE 45 2E 00 

; YOU_HAVE_TAKEN_A_DRINK_FROM_THE_STREAM.__THE_WATER_TASTES_______STRONGLY_OF_
; MINERALS,_BUT_IS_NOT_UNPLEASANT.__IT_IS_EXTREMELY___COLD.[CR]
7886: 2C C7 DE 9B 15 5B CA 4D BD 83 61 46 45 10 B2 C8 
7896: 83 FF B2 82 17 55 5E EF BF 7F 48 56 13 DB 72 16 
78A6: D0 23 62 55 BD F5 BD 3B 13 3B 13 66 17 00 B3 D3 
78B6: 6D B8 16 6B 16 74 98 4D 48 04 EE 73 C6 4B 7B 06 
78C6: 9A B0 17 FF A5 53 49 D7 9A 4B 13 0B BC C7 B5 4C 
78D6: D9 67 61 FB 8E 45 13 BE 9F 2E 00 

; IT'S_NOT_HUNGRY.__BESIDES,_YOU_HAVE_NO_BIRD_SEED.[CR]
78E1: 10 75 7B D0 B5 F3 A0 70 75 C3 6E 3B F4 75 4D FF 
78F1: 78 33 BB C7 DE 9B 15 5B CA EB 99 14 4E 15 58 26 
7901: 60 2E 00 

; YOU_FELL_INTO_A_PIT_AND_BROKE_EVERY_BONE_IN_YOUR_BODY. [CR]
7904: 12 C7 DE 4F 15 F3 8C 9E 7A C3 9C E3 16 03 BC 33 
7914: 98 79 4F 9B 85 CF 62 7B B4 00 4F 4B 5E 9B 96 34 
7924: A1 B9 14 1F 5D 20 00 

; THE_SERPENT_HAS_NOW_DEVOURED_YOUR_BIRD_STATUE.[CR]
792B: 0F 5F BE 57 17 1F B3 B3 9A 55 72 99 16 C6 CE D9 
793B: 62 2F C6 1B 58 34 A1 B3 14 33 B1 FB B9 67 C0 2E 
794B: 00 

; THERE_IS_NOTHING_HERE_IT_WANTS_TO_EAT_-_EXCEPT_PERHAPS_YOU.[CR]
794C: 13 5F BE 5B B1 4B 7B 06 9A 90 73 CA 6A 2F 62 D6 
795C: 15 F3 17 CD 9A 89 17 23 15 1D BC 3A 15 B2 53 12 
796C: BC 32 62 ED 48 51 18 55 2E 00 

; IT_IS_NOW_PITCH_DARK.__IF_YOU_PROCEED,_YOU_WILL_LIKELY_FALL_INTOA_PIT.[CR]
7976: 17 73 7B 4B 7B 09 9A E3 16 9A BD FB 14 6F B2 4B 
7986: 13 9B 64 1B A1 F9 A6 A7 53 73 5D C7 DE FB 17 F3 
7996: 8C 8D 8C 53 61 4B 15 F3 8C 9E 7A FB 9D 96 A5 2E 
79A6: 00 

; I'M_GAME.__WOULD_YOU_CARE_TO_EXPLAIN_HOW?[CR]
79A7: 0D 9F 77 73 15 3F 92 59 13 2E A1 1B 58 1B A1 14 
79B7: 53 56 5E C7 9C A6 D8 D0 47 A9 15 57 3F 00 

; YOUR_LAMP_IS_GETTING_DIM.__YOU'D_BEST_START_WRAPPING_THIS_UP,___UNLESS_YOU_CAN_
; FIND_SOME_FRESH_BATTERIES.__I_SEEM_TO_RECALL_____THERE_IS_A_VENDING_MACHINE_IN_
; THE_MAZE.__BRING_SOME_COINS_WITH__YOU.[CR]
79C5: 41 C7 DE 8E AF 72 48 D5 15 77 15 43 C0 AB 98 8F 
79D5: 5A 3B F4 C7 DE 73 21 75 4D 15 BC 54 BD 19 BC D2 
79E5: B0 90 A5 D6 6A 95 73 B2 17 FB ED B0 17 F5 8B DB 
79F5: B5 1B A1 10 53 53 15 33 98 3F B9 48 5E 75 B1 04 
7A05: 71 8E 49 33 62 6F 62 4B 13 57 17 5B 61 6B BF 65 
7A15: B1 46 48 3B 13 56 13 F4 72 4B 5E C3 B5 CF 17 43 
7A25: 98 AB 98 85 91 90 73 4B 5E 96 96 DB 72 9C 91 DB 
7A35: 63 BC 14 91 7A 61 17 1B 92 3B 55 8B 9A 56 D1 FB 
7A45: 70 C7 DE 2E 00 

; YOUR_LAMP_HAS_RUN_OUT_OF_POWER.[CR]
7A4A: 0A C7 DE 8E AF 72 48 9B 15 D4 B5 83 C5 36 A1 B8 
7A5A: 16 E9 16 B4 D0 2E 00 

; THE_PLANT_HAS_EXCEPTIONALLY_DEEP_ROOTS_AND_CANNOT_BE_PULLED_____FREE.[CR]
7A61: 17 5F BE E6 16 9E 48 9B 15 C7 B5 97 D6 43 A7 0B 
7A71: A0 13 8D FF 14 D3 61 01 B3 0B C0 8E 48 D3 14 D9 
7A81: 99 04 BC 52 5E 46 C5 F3 5F 3B 13 5C 15 3F 60 00 

; YOUR_LAMP_IS_GETTING_DIM.__I'M_TAKING_THE_LIBERTY_OF_REPLACING__THE_BATTERIES.[CR]
7A91: 1A C7 DE 8E AF 72 48 D5 15 77 15 43 C0 AB 98 8F 
7AA1: 5A 3B F4 9F 77 7B 17 50 86 D6 6A DB 72 84 8C 3E 
7AB1: 62 51 DB 94 64 E6 61 DB 46 AB 98 82 17 44 5E 8E 
7AC1: 49 33 62 6F 62 00 

; AS_YOU_APPROACH_THE_STATUE,_IT_COMES_TO_LIFE_AND_FLIES_ACROSS___THE_CHAMBER_WHERE_IT_
; LANDS_AND_RETURNS_TO_STONE.[CR]
7AC7: 25 4B 49 C7 DE 92 14 F9 A6 DA 46 82 17 55 5E 56 
7AD7: BD 3E C4 D6 15 E1 14 35 92 89 17 43 16 5B 66 8E 
7AE7: 48 56 15 35 79 85 14 05 B3 BB B5 82 17 45 5E 4F 
7AF7: 72 74 4D FA 17 2F 62 D6 15 3B 16 4D 98 90 14 14 
7B07: 58 8F 62 DD B2 89 17 66 17 0F A0 2E 00 

; YOU_CAN_LIFT_THE_STATUE,_BUT_YOU_CANNOT_CARRY_IT.[CR]
7B14: 10 C7 DE D3 14 8E 96 5E 79 82 17 55 5E 56 BD 3E 
7B24: C4 BF 14 1B BC 1B A1 10 53 06 9A D3 14 83 B3 D6 
7B34: 15 2E 00 

; YOUR_BOTTLE_IS_ALREADY_FULL.[CR]
7B37: 09 C7 DE 84 AF 0E A1 DB 8B 4B 7B 4C 48 86 5F 48 
7B47: DB 46 C5 2E 00 

; _____SUDDENLY,_A_MUMMY_CREEPS_UP_BEHIND_YOU!!______"I'M_THE_____KEEPER_OF_THE_TOMB",__HE_WAILS,_"I_TAKE_
; THESE_TREASURES_AND_PUT_THEM_IN_THE_CHEST_DEEP_IN_THE_MAZE!"__HE_GRABS_YOUR_TREASURE_ANDVANISHES_INTO_THE_GLOOM.[CR]
7B4C: 48 3B 13 55 13 FE C3 96 61 B3 E0 4F 45 6F C5 45 
7B5C: DB 67 B1 0B A7 D3 C5 6A 4D 8E 7A 51 18 E9 C1 3B 
7B6C: 13 3B 13 FD 1B 56 90 DB 72 3B 13 17 16 DF 61 91 
7B7C: AF 96 64 DB 72 7F BF C6 4B 4A 13 59 5E CE 47 33 
7B8C: BB FB 1B 4D BD 56 5E F5 72 56 5E 63 B1 34 BA 4B 
7B9C: 62 8E 48 EF 16 16 BC EF 72 D0 15 82 17 45 5E F5 
7BAC: 72 06 BC 32 60 D0 15 82 17 4F 5E 6F 4A E3 06 9F 
7BBC: 15 84 15 BD 46 51 18 23 C6 EF BF 67 49 5B B1 8E 
7BCC: 48 D0 C9 5A 7B 4B 62 9E 7A D6 9C DB 72 C9 6D FF 
7BDC: 9F 00 

; THE_STONE_BRIDGE_HAS_RETRACTED![CR]
7BDE: 0A 5F BE 66 17 0F A0 BC 14 01 79 4A 5E 4B 49 76 
7BEE: B1 C5 B0 E6 BD 21 00 

; A_STONE_BRIDGE_NOW_SPANS_THE_BOTTOMLESS_PIT.[CR]
7BF5: 0E 55 45 80 BF 44 5E 06 B2 9B 6C 09 9A 62 17 9D 
7C05: 48 82 17 44 5E 0E A1 EE 9F 65 62 E3 16 54 2E 00 

; THE_VASE_IS_NOW_RESTING,_DELICATELY,_ON_A_VELVET_PILLOW.[CR]
7C15: 12 5F BE CB 17 9B B7 4B 7B 09 9A 2F 17 03 BA CE 
7C25: 98 FF 14 85 8C 7F 49 1E 8F C0 16 7B 14 6E CA 76 
7C35: CA E3 16 09 8D 57 2E 00 

; THE_VASE_DROPS_WITH_A_DELICATE_CRASH.[CR]
7C3D: 0C 5F BE CB 17 9B B7 F9 5B 0B A7 56 D1 03 71 FF 
7C4D: 14 85 8C 7F 49 E4 14 5A 49 2E 00 

; THERE_ARE_NOW_SOME_FRESH_BATTERIES_HERE.[CR]
7C58: 0D 5F BE 5B B1 2F 49 99 16 D5 CE E7 9F 5C 15 5A 
7C68: 62 AB 14 3F C0 07 B2 CA B5 2F 62 2E 00 

; YOU_HAVE_TAKEN_THE_VASE_AND_HURLED_IT_DELICATELY_TO_THE_GROUND.[CR]
7C75: 15 C7 DE 9B 15 5B CA 4D BD 83 61 5F BE CB 17 9B 
7C85: B7 8E 48 AF 15 7F B2 0B 58 06 BC 43 61 16 53 53 
7C95: 61 89 17 82 17 49 5E 07 B3 57 98 00 

; THE_BIRD_STATUE_COMES_TO_LIFE_AND_ATTACKS_THE_SERPENT_AND_IN_AN_ASTOUNDING_FLURRY,_DRIVES_THE_SERPENT_
; AWAY.__THE_BIRD_TURNS_BACKINTO_A_STATUE.[CR]
7CA1: 2F 5F BE B3 14 33 B1 FB B9 67 C0 E1 14 35 92 89 
7CB1: 17 43 16 5B 66 8E 48 96 14 45 BD CB 87 5F BE 57 
7CC1: 17 1F B3 B3 9A 8E 48 D0 15 90 14 95 14 87 BF 43 
7CD1: 98 AB 98 8F 67 83 B3 06 EE 18 B2 4B 62 5F BE 57 
7CE1: 17 1F B3 B3 9A F3 49 DB E0 82 17 44 5E 2E 7B 8F 
7CF1: 17 DD B2 AB 14 9B 54 C9 9A 7B 14 FB B9 67 C0 2E 
7D01: 00 

; THE_PLANT_SPURTS_INTO_FURIOUS_GROWTH_FOR_A_FEW_SECONDS.[CR]
7D02: 12 5F BE E6 16 9E 48 62 17 3E C6 CB B5 C9 9A 5F 
7D12: 15 11 B2 4B C6 B9 6E 02 D3 59 15 83 AF 4F 15 D5 
7D22: CE E1 5F 4D 98 2E 00 

; THE_PLANT_GROWS_EXPLOSIVELY,_ALMOST_FILLING_THE_BOTTOM_OF_THE___PIT.[CR]
7D29: 16 5F BE E6 16 9E 48 84 15 85 A1 3A 15 09 A6 58 
7D39: B8 53 61 03 EE 31 8D F3 B9 0E 67 90 8C D6 6A DB 
7D49: 72 06 4F 7F BF B8 16 82 17 3B 5E E3 16 54 2E 00 

; YOU'VE_OVER-WATERED_THE_PLANT!__IT'S_SHRIVELING_UP![CR]
7D59: 11 C7 DE 4F 24 C8 16 45 62 16 D0 2F 62 16 58 DB 
7D69: 72 FB A5 B1 9A 4B 13 65 BC 5A 17 18 B2 43 61 AB 
7D79: 98 D1 C5 00 

; THERE_IS_NOTHING_HERE_TO_CLIMB.__USE_UP_OR_OUT_TO_LEAVE_THE_PIT.[CR]
7D7D: 15 5F BE 5B B1 4B 7B 06 9A 90 73 CA 6A 2F 62 89 
7D8D: 17 DE 14 64 7A 3B F4 57 C6 B2 17 C4 16 C7 16 16 
7D9D: BC CE 9C 98 5F 56 5E DB 72 96 A5 2E 00 

; OH_DEAR,_YOU_SEEM_TO_HAVE_GOTTEN_YOURSELF_KILLED.__I_MIGHT_BE___ABLE_TO_HELP_YOU_OUT,_BUT_I'VE_NEVER_
; REALLY_DONE_THIS_BEFORE.___DO_YOU_WANT_ME_TO_TRY_TO_REINCARNATE_YOU?[CR]
7DAA: 38 13 9F E3 59 F3 B4 C7 DE 57 17 5B 61 6B BF 58 
7DBA: 72 49 5E 0E A1 83 61 C7 DE 97 B3 03 8C 4E 86 E6 
7DCA: 8B 3B F4 4F 77 7A 79 04 BC 3B 5E 84 14 DB 8B 6B 
7DDA: BF EE 72 1B A3 1B A1 36 A1 04 EE 73 C6 A8 77 50 
7DEA: 5E CF 62 94 AF 8E 5F FB 8E 80 5B 56 5E 95 73 AF 
7DFA: 14 04 68 DB 63 46 13 DB 9C 1B A1 10 D0 0F BC 56 
7E0A: 5E D6 9C 7B B4 6B BF 6B B1 13 98 CB B2 DB BD C7 
7E1A: DE 3F 00 

; YOU_CLUMSY_OAF,_YOU'VE_DONE_IT_AGAIN!__I_DON'T_KNOW_HOW_LONG_I__CAN_KEEP_THIS_UP.__DO_YOU_WANT_ME_TO_
; TRY_REINCARNATING_YOU______AGAIN?[CR]
7E1D: 2C C7 DE DE 14 75 C5 51 DB 66 47 51 18 A8 C2 46 
7E2D: 5E 0F A0 D6 15 89 14 D0 47 BB 06 46 77 05 A0 0D 
7E3D: BC 09 9A A9 15 CE CE 11 A0 BB 15 D3 14 8D 96 32 
7E4D: 60 82 17 4B 7B F7 C5 46 13 DB 9C 1B A1 10 D0 0F 
7E5D: BC 56 5E D6 9C 7B B4 6B B1 13 98 CB B2 90 BE DB 
7E6D: 6A 1B A1 3B 13 43 13 0B 6C 4E 3F 00 

; I_SEEM_TO_BE_OUT_OF_ORANGE_SMOKE.__HOW_CAN_I_REINCARNATE_YOU____WITHOUT_ORANGE_SMOKE?[CR]
7E79: 1C 55 77 2F 60 89 17 AF 14 C7 16 11 BC 91 64 D0 
7E89: B0 9B 6C F1 B8 BF 85 4A 13 6B A1 10 53 BB 15 6B 
7E99: B1 13 98 CB B2 DB BD C7 DE 3B 13 FB 17 69 BE 73 
7EA9: C6 AB A0 B7 98 5F 17 97 9F 3F 00 

; ALL_RIGHT.__BUT_DON'T_BLAME_ME_IF_SOMETHING_GOES_WR.............______________________----__
; POOF_!!__----_______________________YOU_ARE_ENGULFED_IN_A_CLOUD_OF_ORANGE_SMOKE.__COUGHING_
; AND______GASPING,_YOU_EMERGE_FROM_THE_SMOKE.[CR]
7EB4: 4B 46 48 33 17 2E 6D 3B F4 F6 4F 09 15 E6 96 B6 
7EC4: 14 67 48 67 16 C8 15 61 17 36 92 90 73 C9 6A B5 
7ED4: 9E 04 18 FF F9 FF F9 FF F9 FF F9 3B F4 3B 13 3B 
7EE4: 13 3B 13 3B 13 3B 13 3B 13 5D 13 2D ED 52 13 38 
7EF4: A0 E9 12 5D 13 2D ED 3B 13 3B 13 3B 13 3B 13 3B 
7F04: 13 3B 13 3B 13 5B 13 1B A1 2F 49 30 15 2E 6F 66 
7F14: 66 D0 15 7B 14 C9 54 F3 C3 C3 9E AB A0 B7 98 5F 
7F24: 17 97 9F 3B F4 47 55 23 6D AB 98 8E 48 3B 13 3B 
7F34: 13 15 6C 90 A5 33 70 C7 DE 2F 15 31 62 48 5E FF 
7F44: B2 82 17 55 5E BD 93 45 2E 00 

; OKAY,_NOW_WHERE_DID_I_PUT_MY_ORANGE_SMOKE?..._>POOF!<___________EVERYTHING_DISAPPEARS_IN_A_
; DENSE_CLOUD_OF_ORANGE_SMOKE.[CR]
7F4E: 27 93 9F B3 E0 09 9A FA 17 2F 62 03 15 0B 58 EF 
7F5E: 16 0F BC 51 DB D0 B0 9B 6C F1 B8 98 85 FF F9 F2 
7F6E: 13 38 A0 33 07 3B 13 3B 13 3B 13 38 15 43 62 63 
7F7E: BE AB 98 95 5A EA 48 94 5F CB B5 83 96 FF 14 97 
7F8E: 9A DE 14 26 A1 B8 16 C4 16 91 48 55 5E BD 93 45 
7F9E: 2E 00 

; READY_CASSETTE[CR]
7FA0: 04 63 B1 FB 5C 15 53 B6 B7 54 45 00 

; CHECKSUM_ERROR[CR]
7FAC: 04 1F 54 A5 54 5B C5 3C 62 4F 52 00 

; OH,_NO!__I_LOST_MY_COMPASS.__I_NO_LONGER_SEEM_TO_KNOW_WHICH_WAY_IS_NORTH![CR]
7FB8: 18 36 9F 99 16 BB 06 4E 77 E6 A0 7B 16 E1 14 DB 
7FC8: 93 EF B9 4B 13 99 16 49 16 B7 98 95 AF 2F 60 89 
7FD8: 17 20 16 6B A1 23 D1 13 54 1B D0 D5 15 99 16 C2 
7FE8: B3 21 00 

7FB8: 18 36      JR      $7FF0           
7FBA: 9F         SBC     A               
7FBB: 99         SBC     C               
7FBC: 16 BB      LD      D,$BB           
7FBE: 06 4E      LD      B,$4E           
7FC0: 77         LD      (HL),A          
7FC1: E6 A0      AND     $A0             
7FC3: 7B         LD      A,E             
7FC4: 16 E1      LD      D,$E1           
7FC6: 14         INC     D               
7FC7: DB 93      IN      A,($93)         
7FC9: EF         RST     0X28            
7FCA: B9         CP      C               
7FCB: 4B         LD      C,E             
7FCC: 13         INC     DE              
7FCD: 99         SBC     C               
7FCE: 16 49      LD      D,$49           
7FD0: 16 B7      LD      D,$B7           
7FD2: 98         SBC     B               
7FD3: 95         SUB     L               
7FD4: AF         XOR     A               
7FD5: 2F         CPL                     
7FD6: 60         LD      H,B             
7FD7: 89         ADC     A,C             
7FD8: 17         RLA                     
7FD9: 20 16      JR      NZ,$7FF1        
7FDB: 6B         LD      L,E             
7FDC: A1         AND     C               
7FDD: 23         INC     HL              
7FDE: D1         POP     DE              
7FDF: 13         INC     DE              
7FE0: 54         LD      D,H             
7FE1: 1B         DEC     DE              
7FE2: D0         RET     NC              
7FE3: D5         PUSH    DE              
7FE4: 15         DEC     D               
7FE5: 99         SBC     C               
7FE6: 16 C2      LD      D,$C2           
7FE8: B3         OR      E               
7FE9: 21 00 39   LD      HL,$3900        
7FEC: 00         NOP                     
7FED: 39         ADD     HL,SP           
7FEE: 00         NOP                     
7FEF: 39         ADD     HL,SP           
7FF0: 00         NOP                     
7FF1: 39         ADD     HL,SP           
7FF2: 00         NOP                     
7FF3: 39         ADD     HL,SP           
7FF4: 00         NOP                     
7FF5: 39         ADD     HL,SP           
7FF6: 00         NOP                     
7FF7: 39         ADD     HL,SP           
7FF8: 00         NOP                     
7FF9: 39         ADD     HL,SP           
7FFA: 00         NOP                     
7FFB: 39         ADD     HL,SP           
7FFC: 00         NOP                     
7FFD: 39         ADD     HL,SP           
7FFE: 00         NOP                     
7FFF: 47         LD      B,A             
8000: 78         LD      A,B             
8001: 00         NOP                     
8002: 43         LD      B,E             
8003: FF         RST     0X38            
8004: FF         RST     0X38            
```