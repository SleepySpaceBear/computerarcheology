![Bank 18](GBZelda.jpg)

# Bank `8

>>> cpu Z80GB

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

```
4000: FA 16 C1   LD      A,($C116)       
4003: A7         AND     A               
4004: 20 09      JR      NZ,$400F        
4006: 3C         INC     A               
4007: EA 16 C1   LD      ($C116),A       
400A: 3E 14      LD      A,$14           
400C: EA FF D6   LD      ($D6FF),A       
400F: F0 EE      LD      A,($EE)         
4011: FE 48      CP      $48             
4013: C2 78 43   JP      NZ,$4378        
4016: CD 5E 43   CALL    $435E           
4019: CD AF 7C   CALL    $7CAF           
401C: F0 F0      LD      A,($F0)         
401E: C7         RST     0X00            
401F: 2D         DEC     L               
4020: 40         LD      B,B             
4021: 98         SBC     B               
4022: 40         LD      B,B             
4023: D9         RETI                    
4024: 40         LD      B,B             
4025: CE 41      ADC     $41             
4027: 55         LD      D,L             
4028: 42         LD      B,D             
4029: 6E         LD      L,(HL)          
402A: 42         LD      B,D             
402B: A9         XOR     C               
402C: 42         LD      B,D             
402D: AF         XOR     A               
402E: EA 01 D2   LD      ($D201),A       
4031: FA 49 DB   LD      A,($DB49)       
4034: E6 01      AND     $01             
4036: 28 12      JR      Z,$404A         
4038: F0 99      LD      A,($99)         
403A: 21 EF FF   LD      HL,$FFEF        
403D: 96         SUB     (HL)            
403E: C6 28      ADD     $28             
4040: FE 50      CP      $50             
4042: CD 19 7D   CALL    $7D19           
4045: 30 35      JR      NC,$407C        
4047: C3 B6 42   JP      $42B6           
404A: F0 99      LD      A,($99)         
404C: FE 4C      CP      $4C             
404E: 30 2C      JR      NC,$407C        
4050: 3E 4C      LD      A,$4C           
4052: E0 99      LDFF00  ($99),A         
4054: CD 95 14   CALL    $1495           
4057: CD 3B 09   CALL    $093B           
405A: 1E 0B      LD      E,$0B           
405C: 21 00 DB   LD      HL,$DB00        
405F: 2A         LD      A,(HLI)         
4060: FE 09      CP      $09             
4062: 28 10      JR      Z,$4074         
4064: 1D         DEC     E               
4065: 7B         LD      A,E             
4066: FE FF      CP      $FF             
4068: 20 F5      JR      NZ,$405F        
406A: 3E DB      LD      A,$DB           
406C: CD 88 40   CALL    $4088           
406F: CD 8D 3B   CALL    $3B8D           
4072: 70         LD      (HL),B          
4073: C9         RET                     
4074: 3E DC      LD      A,$DC           
4076: CD 88 40   CALL    $4088           
4079: CD 8D 3B   CALL    $3B8D           
407C: F0 E7      LD      A,($E7)         
407E: 1F         RRA                     
407F: 1F         RRA                     
4080: 1F         RRA                     
4081: 1F         RRA                     
4082: E6 01      AND     $01             
4084: CD 87 3B   CALL    $3B87           
4087: C9         RET                     
4088: 5F         LD      E,A             
4089: F0 99      LD      A,($99)         
408B: F5         PUSH    AF              
408C: 3E 10      LD      A,$10           
408E: E0 99      LDFF00  ($99),A         
4090: 7B         LD      A,E             
4091: CD 97 21   CALL    $2197           
4094: F1         POP     AF              
4095: E0 99      LDFF00  ($99),A         
4097: C9         RET                     
4098: CD 7C 40   CALL    $407C           
409B: FA 9F C1   LD      A,($C19F)       
409E: A7         AND     A               
409F: 20 37      JR      NZ,$40D8        
40A1: CD 8D 3B   CALL    $3B8D           
40A4: FA 77 C1   LD      A,($C177)       
40A7: A7         AND     A               
40A8: 28 07      JR      Z,$40B1         
40AA: 70         LD      (HL),B          
40AB: 3E DE      LD      A,$DE           
40AD: CD 88 40   CALL    $4088           
40B0: C9         RET                     
40B1: FA 5D DB   LD      A,($DB5D)       
40B4: FE 03      CP      $03             
40B6: 38 F2      JR      C,$40AA         
40B8: FA 92 DB   LD      A,($DB92)       
40BB: C6 2C      ADD     $2C             
40BD: EA 92 DB   LD      ($DB92),A       
40C0: FA 91 DB   LD      A,($DB91)       
40C3: CE 01      ADC     $01             
40C5: EA 91 DB   LD      ($DB91),A       
40C8: CD 91 08   CALL    $0891           
40CB: 36 FF      LD      (HL),$FF        
40CD: CD D2 27   CALL    $27D2           
40D0: CD C1 45   CALL    $45C1           
40D3: 3E 01      LD      A,$01           
40D5: EA 00 C5   LD      ($C500),A       
40D8: C9         RET                     
40D9: 3E 02      LD      A,$02           
40DB: E0 A1      LDFF00  ($A1),A         
40DD: EA 67 C1   LD      ($C167),A       
40E0: CD 91 08   CALL    $0891           
40E3: 20 0D      JR      NZ,$40F2        
40E5: 3E 35      LD      A,$35           
40E7: EA 68 D3   LD      ($D368),A       
40EA: 3E 01      LD      A,$01           
40EC: EA 15 D2   LD      ($D215),A       
40EF: C3 8D 3B   JP      $3B8D           
40F2: C9         RET                     
40F3: 3E 30      LD      A,$30           
40F5: E0 CD      LDFF00  ($CD),A         
40F7: 3E 18      LD      A,$18           
40F9: E0 CE      LDFF00  ($CE),A         
40FB: C3 B5 44   JP      $44B5           
40FE: 3E 30      LD      A,$30           
4100: E0 CD      LDFF00  ($CD),A         
4102: 3E 68      LD      A,$68           
4104: E0 CE      LDFF00  ($CE),A         
4106: C3 B5 44   JP      $44B5           
4109: 3E 38      LD      A,$38           
410B: E0 CE      LDFF00  ($CE),A         
410D: 3E 08      LD      A,$08           
410F: E0 CD      LDFF00  ($CD),A         
4111: C3 09 44   JP      $4409           
4114: 3E 38      LD      A,$38           
4116: E0 CE      LDFF00  ($CE),A         
4118: 3E 08      LD      A,$08           
411A: E0 CD      LDFF00  ($CD),A         
411C: C3 5E 44   JP      $445E           
411F: C9         RET                     
4120: 03         INC     BC              
4121: 03         INC     BC              
4122: 03         INC     BC              
4123: 03         INC     BC              
4124: 03         INC     BC              
4125: 03         INC     BC              
4126: 03         INC     BC              
4127: 01 02 04   LD      BC,$0402        
412A: 03         INC     BC              
412B: 01 02 04   LD      BC,$0402        
412E: 03         INC     BC              
412F: 01 02 04   LD      BC,$0402        
4132: 03         INC     BC              
4133: 01 02 04   LD      BC,$0402        
4136: 03         INC     BC              
4137: 01 02 04   LD      BC,$0402        
413A: 03         INC     BC              
413B: 03         INC     BC              
413C: 03         INC     BC              
413D: 03         INC     BC              
413E: 03         INC     BC              
413F: 04         INC     B               
4140: 03         INC     BC              
4141: 01 02 04   LD      BC,$0402        
4144: 03         INC     BC              
4145: 01 02 04   LD      BC,$0402        
4148: 03         INC     BC              
4149: 01 02 04   LD      BC,$0402        
414C: 03         INC     BC              
414D: 01 02 04   LD      BC,$0402        
4150: 03         INC     BC              
4151: 01 02 02   LD      BC,$0202        
4154: 02         LD      (BC),A          
4155: 02         LD      (BC),A          
4156: 02         LD      (BC),A          
4157: 02         LD      (BC),A          
4158: 02         LD      (BC),A          
4159: 02         LD      (BC),A          
415A: 01 01 05   LD      BC,$0501        
415D: 05         DEC     B               
415E: 05         DEC     B               
415F: 05         DEC     B               
4160: 05         DEC     B               
4161: 05         DEC     B               
4162: 01 01 04   LD      BC,$0401        
4165: 01 05 01   LD      BC,$0105        
4168: 04         INC     B               
4169: 01 05 01   LD      BC,$0105        
416C: 04         INC     B               
416D: 01 05 01   LD      BC,$0105        
4170: 04         INC     B               
4171: 01 05 01   LD      BC,$0105        
4174: 04         INC     B               
4175: 01 05 05   LD      BC,$0505        
4178: 05         DEC     B               
4179: 05         DEC     B               
417A: 01 01 05   LD      BC,$0501        
417D: 01 04 01   LD      BC,$0104        
4180: 05         DEC     B               
4181: 01 04 01   LD      BC,$0104        
4184: 05         DEC     B               
4185: 01 04 01   LD      BC,$0104        
4188: 05         DEC     B               
4189: 01 04 01   LD      BC,$0104        
418C: 05         DEC     B               
418D: 01 04 04   LD      BC,$0404        
4190: 04         INC     B               
4191: 04         INC     B               
4192: 04         INC     B               
4193: 04         INC     B               
4194: 01 01 01   LD      BC,$0101        
4197: 01 05 05   LD      BC,$0505        
419A: 05         DEC     B               
419B: 05         DEC     B               
419C: 01 01 01   LD      BC,$0101        
419F: 01 04 01   LD      BC,$0104        
41A2: 05         DEC     B               
41A3: 01 04 01   LD      BC,$0104        
41A6: 05         DEC     B               
41A7: 01 04 01   LD      BC,$0104        
41AA: 05         DEC     B               
41AB: 01 04 01   LD      BC,$0104        
41AE: 05         DEC     B               
41AF: 01 04 01   LD      BC,$0104        
41B2: 05         DEC     B               
41B3: 05         DEC     B               
41B4: 01 01 01   LD      BC,$0101        
41B7: 01 05 01   LD      BC,$0105        
41BA: 04         INC     B               
41BB: 01 05 01   LD      BC,$0105        
41BE: 04         INC     B               
41BF: 01 05 01   LD      BC,$0105        
41C2: 04         INC     B               
41C3: 01 05 01   LD      BC,$0105        
41C6: 04         INC     B               
41C7: 01 05 01   LD      BC,$0105        
41CA: 04         INC     B               
41CB: 04         INC     B               
41CC: 04         INC     B               
41CD: 04         INC     B               
41CE: 3E 02      LD      A,$02           
41D0: E0 A1      LDFF00  ($A1),A         
41D2: EA 67 C1   LD      ($C167),A       
41D5: FA 11 D2   LD      A,($D211)       
41D8: A7         AND     A               
41D9: 20 20      JR      NZ,$41FB        
41DB: FA 10 D2   LD      A,($D210)       
41DE: FE 00      CP      $00             
41E0: CC 09 41   CALL    Z,$4109         
41E3: FA 10 D2   LD      A,($D210)       
41E6: FE 01      CP      $01             
41E8: CC 14 41   CALL    Z,$4114         
41EB: FA 10 D2   LD      A,($D210)       
41EE: FE 38      CP      $38             
41F0: CC F3 40   CALL    Z,$40F3         
41F3: FA 10 D2   LD      A,($D210)       
41F6: FE 70      CP      $70             
41F8: CC FE 40   CALL    Z,$40FE         
41FB: FA 10 D2   LD      A,($D210)       
41FE: C6 01      ADD     $01             
4200: EA 10 D2   LD      ($D210),A       
4203: 5F         LD      E,A             
4204: FA 11 D2   LD      A,($D211)       
4207: CE 00      ADC     $00             
4209: EA 11 D2   LD      ($D211),A       
420C: 57         LD      D,A             
420D: FE 06      CP      $06             
420F: 20 12      JR      NZ,$4223        
4211: 7B         LD      A,E             
4212: FE 20      CP      $20             
4214: 20 0D      JR      NZ,$4223        
4216: 3E DD      LD      A,$DD           
4218: CD 88 40   CALL    $4088           
421B: AF         XOR     A               
421C: EA 00 C5   LD      ($C500),A       
421F: CD 8D 3B   CALL    $3B8D           
4222: C9         RET                     
4223: FA 12 D2   LD      A,($D212)       
4226: 3C         INC     A               
4227: FE 1C      CP      $1C             
4229: 20 08      JR      NZ,$4233        
422B: FA 13 D2   LD      A,($D213)       
422E: 3C         INC     A               
422F: EA 13 D2   LD      ($D213),A       
4232: AF         XOR     A               
4233: EA 12 D2   LD      ($D212),A       
4236: FA 13 D2   LD      A,($D213)       
4239: 5F         LD      E,A             
423A: 50         LD      D,B             
423B: 21 20 41   LD      HL,$4120        
423E: 19         ADD     HL,DE           
423F: 7E         LD      A,(HL)          
4240: CD 87 3B   CALL    $3B87           
4243: 21 5A 41   LD      HL,$415A        
4246: 19         ADD     HL,DE           
4247: 7E         LD      A,(HL)          
4248: EA B1 C3   LD      ($C3B1),A       
424B: 21 94 41   LD      HL,$4194        
424E: 19         ADD     HL,DE           
424F: 7E         LD      A,(HL)          
4250: EA B2 C3   LD      ($C3B2),A       
4253: C9         RET                     
4254: C9         RET                     
4255: FA 9F C1   LD      A,($C19F)       
4258: A7         AND     A               
4259: 20 10      JR      NZ,$426B        
425B: EA 15 D2   LD      ($D215),A       
425E: CD 91 08   CALL    $0891           
4261: 36 70      LD      (HL),$70        
4263: 3E 10      LD      A,$10           
4265: EA 68 D3   LD      ($D368),A       
4268: CD 8D 3B   CALL    $3B8D           
426B: C3 7C 40   JP      $407C           
426E: CD 91 08   CALL    $0891           
4271: 20 0E      JR      NZ,$4281        
4273: 3E 02      LD      A,$02           
4275: EA 4A DB   LD      ($DB4A),A       
4278: 21 49 DB   LD      HL,$DB49        
427B: CB C6      SET     1,E             
427D: CD 8D 3B   CALL    $3B8D           
4280: C9         RET                     
4281: FE 08      CP      $08             
4283: 20 06      JR      NZ,$428B        
4285: 35         DEC     (HL)            
4286: 3E DF      LD      A,$DF           
4288: CD 88 40   CALL    $4088           
428B: 3E 6C      LD      A,$6C           
428D: E0 9D      LDFF00  ($9D),A         
428F: 3E 02      LD      A,$02           
4291: E0 A1      LDFF00  ($A1),A         
4293: F0 98      LD      A,($98)         
4295: E0 EE      LDFF00  ($EE),A         
4297: F0 99      LD      A,($99)         
4299: D6 0C      SUB     $0C             
429B: E0 EC      LDFF00  ($EC),A         
429D: 11 6C 47   LD      DE,$476C        
42A0: AF         XOR     A               
42A1: E0 F1      LDFF00  ($F1),A         
42A3: CD D0 3C   CALL    $3CD0           
42A6: C3 7C 40   JP      $407C           
42A9: FA 9F C1   LD      A,($C19F)       
42AC: A7         AND     A               
42AD: 20 0C      JR      NZ,$42BB        
42AF: EA 67 C1   LD      ($C167),A       
42B2: CD 8D 3B   CALL    $3B8D           
42B5: 70         LD      (HL),B          
42B6: 3E E0      LD      A,$E0           
42B8: CD 88 40   CALL    $4088           
42BB: C3 7C 40   JP      $407C           
42BE: 00         NOP                     
42BF: 00         NOP                     
42C0: 60         LD      H,B             
42C1: 00         NOP                     
42C2: 00         NOP                     
42C3: 08 62 00   LD      ($0062),SP      
42C6: 00         NOP                     
42C7: 10 64      STOP    $64             
42C9: 00         NOP                     
42CA: 00         NOP                     
42CB: 18 66      JR      $4333           
42CD: 00         NOP                     
42CE: 10 00      STOP    $00             
42D0: 68         LD      L,B             
42D1: 00         NOP                     
42D2: 10 08      STOP    $08             
42D4: 6A         LD      L,D             
42D5: 00         NOP                     
42D6: 10 10      STOP    $10             
42D8: 6C         LD      L,H             
42D9: 00         NOP                     
42DA: 10 18      STOP    $18             
42DC: 6E         LD      L,(HL)          
42DD: 00         NOP                     
42DE: 00         NOP                     
42DF: 00         NOP                     
42E0: 70         LD      (HL),B          
42E1: 00         NOP                     
42E2: 00         NOP                     
42E3: 08 72 00   LD      ($0072),SP      
42E6: 00         NOP                     
42E7: 10 74      STOP    $74             
42E9: 00         NOP                     
42EA: 00         NOP                     
42EB: 18 76      JR      $4363           
42ED: 00         NOP                     
42EE: 10 00      STOP    $00             
42F0: 68         LD      L,B             
42F1: 00         NOP                     
42F2: 10 08      STOP    $08             
42F4: 6A         LD      L,D             
42F5: 00         NOP                     
42F6: 10 10      STOP    $10             
42F8: 6C         LD      L,H             
42F9: 00         NOP                     
42FA: 10 18      STOP    $18             
42FC: 6E         LD      L,(HL)          
42FD: 00         NOP                     
42FE: 00         NOP                     
42FF: 00         NOP                     
4300: 78         LD      A,B             
4301: 00         NOP                     
4302: 00         NOP                     
4303: 08 7A 00   LD      ($007A),SP      
4306: 00         NOP                     
4307: 10 7C      STOP    $7C             
4309: 00         NOP                     
430A: 00         NOP                     
430B: 18 7E      JR      $438B           
430D: 00         NOP                     
430E: 10 00      STOP    $00             
4310: 68         LD      L,B             
4311: 00         NOP                     
4312: 10 08      STOP    $08             
4314: 6A         LD      L,D             
4315: 00         NOP                     
4316: 10 10      STOP    $10             
4318: 6C         LD      L,H             
4319: 00         NOP                     
431A: 10 18      STOP    $18             
431C: 6E         LD      L,(HL)          
431D: 00         NOP                     
431E: 00         NOP                     
431F: 00         NOP                     
4320: 7E         LD      A,(HL)          
4321: 20 00      JR      NZ,$4323        
4323: 08 7C 20   LD      ($207C),SP      
4326: 00         NOP                     
4327: 10 7A      STOP    $7A             
4329: 20 00      JR      NZ,$432B        
432B: 18 78      JR      $43A5           
432D: 20 10      JR      NZ,$433F        
432F: 00         NOP                     
4330: 6E         LD      L,(HL)          
4331: 20 10      JR      NZ,$4343        
4333: 08 6C 20   LD      ($206C),SP      
4336: 10 10      STOP    $10             
4338: 6A         LD      L,D             
4339: 20 10      JR      NZ,$434B        
433B: 18 68      JR      $43A5           
433D: 20 00      JR      NZ,$433F        
433F: 00         NOP                     
4340: 76         HALT                    
4341: 20 00      JR      NZ,$4343        
4343: 08 74 20   LD      ($2074),SP      
4346: 00         NOP                     
4347: 10 72      STOP    $72             
4349: 20 00      JR      NZ,$434B        
434B: 18 70      JR      $43BD           
434D: 20 10      JR      NZ,$435F        
434F: 00         NOP                     
4350: 6E         LD      L,(HL)          
4351: 20 10      JR      NZ,$4363        
4353: 08 6C 20   LD      ($206C),SP      
4356: 10 10      STOP    $10             
4358: 6A         LD      L,D             
4359: 20 10      JR      NZ,$436B        
435B: 18 68      JR      $43C5           
435D: 20 F0      JR      NZ,$434F        
435F: F1         POP     AF              
4360: 17         RLA                     
4361: 17         RLA                     
4362: 17         RLA                     
4363: 17         RLA                     
4364: 17         RLA                     
4365: E6 E0      AND     $E0             
4367: 5F         LD      E,A             
4368: 50         LD      D,B             
4369: 21 BE 42   LD      HL,$42BE        
436C: 19         ADD     HL,DE           
436D: 0E 08      LD      C,$08           
436F: CD 26 3D   CALL    $3D26           
4372: 3E 04      LD      A,$04           
4374: CD D0 3D   CALL    $3DD0           
4377: C9         RET                     
4378: 21 10 C2   LD      HL,$C210        
437B: 09         ADD     HL,BC           
437C: 36 4A      LD      (HL),$4A        
437E: 21 50 C3   LD      HL,$C350        
4381: 09         ADD     HL,BC           
4382: 36 98      LD      (HL),$98        
4384: CD 65 3B   CALL    $3B65           
4387: CD E9 43   CALL    $43E9           
438A: CD AF 7C   CALL    $7CAF           
438D: F0 F0      LD      A,($F0)         
438F: C7         RST     0X00            
4390: 94         SUB     H               
4391: 43         LD      B,E             
4392: 9F         SBC     A               
4393: 43         LD      B,E             
4394: CD ED 27   CALL    $27ED           
4397: 21 D0 C3   LD      HL,$C3D0        
439A: 09         ADD     HL,BC           
439B: 77         LD      (HL),A          
439C: CD 8D 3B   CALL    $3B8D           
439F: FA 15 D2   LD      A,($D215)       
43A2: A7         AND     A               
43A3: C2 B8 43   JP      NZ,$43B8        
43A6: 21 D0 C3   LD      HL,$C3D0        
43A9: 09         ADD     HL,BC           
43AA: 34         INC     (HL)            
43AB: 7E         LD      A,(HL)          
43AC: 1E 00      LD      E,$00           
43AE: E6 30      AND     $30             
43B0: 28 01      JR      Z,$43B3         
43B2: 1C         INC     E               
43B3: 7B         LD      A,E             
43B4: CD 87 3B   CALL    $3B87           
43B7: C9         RET                     
43B8: C9         RET                     
43B9: 58         LD      E,B             
43BA: 00         NOP                     
43BB: 58         LD      E,B             
43BC: 20 5A      JR      NZ,$4418        
43BE: 00         NOP                     
43BF: 5A         LD      E,D             
43C0: 20 5C      JR      NZ,$441E        
43C2: 00         NOP                     
43C3: 5E         LD      E,(HL)          
43C4: 00         NOP                     
43C5: 5E         LD      E,(HL)          
43C6: 20 5C      JR      NZ,$4424        
43C8: 20 F0      JR      NZ,$43BA        
43CA: 00         NOP                     
43CB: 50         LD      D,B             
43CC: 00         NOP                     
43CD: F0 08      LD      A,($08)         
43CF: 52         LD      D,D             
43D0: 00         NOP                     
43D1: 00         NOP                     
43D2: 00         NOP                     
43D3: 54         LD      D,H             
43D4: 00         NOP                     
43D5: 00         NOP                     
43D6: 08 56 00   LD      ($0056),SP      
43D9: F0 00      LD      A,($00)         
43DB: 52         LD      D,D             
43DC: 20 F0      JR      NZ,$43CE        
43DE: 08 50 20   LD      ($2050),SP      
43E1: 00         NOP                     
43E2: 00         NOP                     
43E3: 56         LD      D,(HL)          
43E4: 20 00      JR      NZ,$43E6        
43E6: 08 54 20   LD      ($2054),SP      
43E9: F0 F1      LD      A,($F1)         
43EB: FE 04      CP      $04             
43ED: 30 06      JR      NC,$43F5        
43EF: 11 B9 43   LD      DE,$43B9        
43F2: C3 3B 3C   JP      $3C3B           
43F5: D6 04      SUB     $04             
43F7: 17         RLA                     
43F8: 17         RLA                     
43F9: 17         RLA                     
43FA: 17         RLA                     
43FB: E6 F0      AND     $F0             
43FD: 5F         LD      E,A             
43FE: 50         LD      D,B             
43FF: 21 C9 43   LD      HL,$43C9        
4402: 19         ADD     HL,DE           
4403: 0E 04      LD      C,$04           
4405: CD 26 3D   CALL    $3D26           
4408: C9         RET                     
4409: CD 39 28   CALL    $2839           
440C: 3E 1B      LD      A,$1B           
440E: EA 00 D6   LD      ($D600),A       
4411: 21 01 D6   LD      HL,$D601        
4414: F0 CF      LD      A,($CF)         
4416: C6 02      ADD     $02             
4418: 5F         LD      E,A             
4419: 22         LD      (HLI),A         
441A: F0 D0      LD      A,($D0)         
441C: 22         LD      (HLI),A         
441D: 3E 85      LD      A,$85           
441F: 22         LD      (HLI),A         
4420: 3E 00      LD      A,$00           
4422: 22         LD      (HLI),A         
4423: 3E 04      LD      A,$04           
4425: 22         LD      (HLI),A         
4426: 3E 7F      LD      A,$7F           
4428: 22         LD      (HLI),A         
4429: 3E 7F      LD      A,$7F           
442B: 22         LD      (HLI),A         
442C: 3E 06      LD      A,$06           
442E: 22         LD      (HLI),A         
442F: 3E 0C      LD      A,$0C           
4431: 22         LD      (HLI),A         
4432: 7B         LD      A,E             
4433: 22         LD      (HLI),A         
4434: F0 D0      LD      A,($D0)         
4436: C6 01      ADD     $01             
4438: 22         LD      (HLI),A         
4439: 3E 85      LD      A,$85           
443B: 22         LD      (HLI),A         
443C: 3E 01      LD      A,$01           
443E: 22         LD      (HLI),A         
443F: 3E 7F      LD      A,$7F           
4441: 22         LD      (HLI),A         
4442: 3E 7F      LD      A,$7F           
4444: 22         LD      (HLI),A         
4445: 3E 7F      LD      A,$7F           
4447: 22         LD      (HLI),A         
4448: 3E 7F      LD      A,$7F           
444A: 22         LD      (HLI),A         
444B: 3E 0D      LD      A,$0D           
444D: 22         LD      (HLI),A         
444E: 7B         LD      A,E             
444F: 22         LD      (HLI),A         
4450: F0 D0      LD      A,($D0)         
4452: C6 02      ADD     $02             
4454: 22         LD      (HLI),A         
4455: 3E C5      LD      A,$C5           
4457: 22         LD      (HLI),A         
4458: 3E 7F      LD      A,$7F           
445A: 22         LD      (HLI),A         
445B: 36 00      LD      (HL),$00        
445D: C9         RET                     
445E: CD 39 28   CALL    $2839           
4461: 3E 1B      LD      A,$1B           
4463: EA 00 D6   LD      ($D600),A       
4466: 21 01 D6   LD      HL,$D601        
4469: F0 CF      LD      A,($CF)         
446B: C6 02      ADD     $02             
446D: 5F         LD      E,A             
446E: 22         LD      (HLI),A         
446F: F0 D0      LD      A,($D0)         
4471: C6 03      ADD     $03             
4473: 22         LD      (HLI),A         
4474: 3E C5      LD      A,$C5           
4476: 22         LD      (HLI),A         
4477: 3E 7F      LD      A,$7F           
4479: 22         LD      (HLI),A         
447A: 7B         LD      A,E             
447B: 22         LD      (HLI),A         
447C: F0 D0      LD      A,($D0)         
447E: C6 04      ADD     $04             
4480: 22         LD      (HLI),A         
4481: 3E 85      LD      A,$85           
4483: 22         LD      (HLI),A         
4484: 3E 02      LD      A,$02           
4486: 22         LD      (HLI),A         
4487: 3E 7F      LD      A,$7F           
4489: 22         LD      (HLI),A         
448A: 3E 7F      LD      A,$7F           
448C: 22         LD      (HLI),A         
448D: 3E 7F      LD      A,$7F           
448F: 22         LD      (HLI),A         
4490: 3E 7F      LD      A,$7F           
4492: 22         LD      (HLI),A         
4493: 3E 0E      LD      A,$0E           
4495: 22         LD      (HLI),A         
4496: 7B         LD      A,E             
4497: 22         LD      (HLI),A         
4498: F0 D0      LD      A,($D0)         
449A: C6 05      ADD     $05             
449C: 22         LD      (HLI),A         
449D: 3E 85      LD      A,$85           
449F: 22         LD      (HLI),A         
44A0: 3E 03      LD      A,$03           
44A2: 22         LD      (HLI),A         
44A3: 3E 05      LD      A,$05           
44A5: 22         LD      (HLI),A         
44A6: 3E 7F      LD      A,$7F           
44A8: 22         LD      (HLI),A         
44A9: 3E 7F      LD      A,$7F           
44AB: 22         LD      (HLI),A         
44AC: 3E 07      LD      A,$07           
44AE: 22         LD      (HLI),A         
44AF: 3E 0F      LD      A,$0F           
44B1: 22         LD      (HLI),A         
44B2: 36 00      LD      (HL),$00        
44B4: C9         RET                     
44B5: CD 39 28   CALL    $2839           
44B8: 3E 15      LD      A,$15           
44BA: EA 00 D6   LD      ($D600),A       
44BD: 21 01 D6   LD      HL,$D601        
44C0: F0 CF      LD      A,($CF)         
44C2: C6 02      ADD     $02             
44C4: 5F         LD      E,A             
44C5: 22         LD      (HLI),A         
44C6: F0 D0      LD      A,($D0)         
44C8: 22         LD      (HLI),A         
44C9: 3E 83      LD      A,$83           
44CB: 22         LD      (HLI),A         
44CC: 3E 00      LD      A,$00           
44CE: 22         LD      (HLI),A         
44CF: 3E 04      LD      A,$04           
44D1: 22         LD      (HLI),A         
44D2: 3E 06      LD      A,$06           
44D4: 22         LD      (HLI),A         
44D5: 3E 0C      LD      A,$0C           
44D7: 22         LD      (HLI),A         
44D8: 7B         LD      A,E             
44D9: 22         LD      (HLI),A         
44DA: F0 D0      LD      A,($D0)         
44DC: C6 01      ADD     $01             
44DE: 22         LD      (HLI),A         
44DF: 3E 83      LD      A,$83           
44E1: 22         LD      (HLI),A         
44E2: 3E 01      LD      A,$01           
44E4: 22         LD      (HLI),A         
44E5: 3E 7F      LD      A,$7F           
44E7: 22         LD      (HLI),A         
44E8: 3E 7F      LD      A,$7F           
44EA: 22         LD      (HLI),A         
44EB: 3E 0D      LD      A,$0D           
44ED: 22         LD      (HLI),A         
44EE: 7B         LD      A,E             
44EF: 22         LD      (HLI),A         
44F0: F0 D0      LD      A,($D0)         
44F2: C6 02      ADD     $02             
44F4: 22         LD      (HLI),A         
44F5: 3E 83      LD      A,$83           
44F7: 22         LD      (HLI),A         
44F8: 3E 02      LD      A,$02           
44FA: 22         LD      (HLI),A         
44FB: 3E 7F      LD      A,$7F           
44FD: 22         LD      (HLI),A         
44FE: 3E 7F      LD      A,$7F           
4500: 22         LD      (HLI),A         
4501: 3E 0E      LD      A,$0E           
4503: 22         LD      (HLI),A         
4504: 7B         LD      A,E             
4505: 22         LD      (HLI),A         
4506: F0 D0      LD      A,($D0)         
4508: C6 03      ADD     $03             
450A: 22         LD      (HLI),A         
450B: 3E 83      LD      A,$83           
450D: 22         LD      (HLI),A         
450E: 3E 03      LD      A,$03           
4510: 22         LD      (HLI),A         
4511: 3E 05      LD      A,$05           
4513: 22         LD      (HLI),A         
4514: 3E 07      LD      A,$07           
4516: 22         LD      (HLI),A         
4517: 3E 0F      LD      A,$0F           
4519: 22         LD      (HLI),A         
451A: 36 00      LD      (HL),$00        
451C: C9         RET                     
451D: F0 EC      LD      A,($EC)         
451F: FE 50      CP      $50             
4521: D2 E5 48   JP      NC,$48E5        
4524: 21 10 C2   LD      HL,$C210        
4527: 09         ADD     HL,BC           
4528: 36 3E      LD      (HL),$3E        
452A: FA 14 D2   LD      A,($D214)       
452D: A7         AND     A               
452E: 28 04      JR      Z,$4534         
4530: 3D         DEC     A               
4531: EA 14 D2   LD      ($D214),A       
4534: FA 18 D2   LD      A,($D218)       
4537: A7         AND     A               
4538: 28 04      JR      Z,$453E         
453A: 3D         DEC     A               
453B: EA 18 D2   LD      ($D218),A       
453E: CD 4F 48   CALL    $484F           
4541: CD AF 7C   CALL    $7CAF           
4544: F0 F0      LD      A,($F0)         
4546: C7         RST     0X00            
4547: 53         LD      D,E             
4548: 45         LD      B,L             
4549: 85         ADD     A,L             
454A: 45         LD      B,L             
454B: B3         OR      E               
454C: 45         LD      B,L             
454D: C2 46 55   JP      NZ,$5546        
4550: 47         LD      B,A             
4551: 6E         LD      L,(HL)          
4552: 47         LD      B,A             
4553: FA 49 DB   LD      A,($DB49)       
4556: E6 02      AND     $02             
4558: 28 0B      JR      Z,$4565         
455A: CD F5 7C   CALL    $7CF5           
455D: 30 1B      JR      NC,$457A        
455F: 3E 89      LD      A,$89           
4561: CD 85 21   CALL    $2185           
4564: C9         RET                     
4565: F0 98      LD      A,($98)         
4567: FE 30      CP      $30             
4569: 38 0F      JR      C,$457A         
456B: 3E 2F      LD      A,$2F           
456D: E0 98      LDFF00  ($98),A         
456F: CD 95 14   CALL    $1495           
4572: 3E 85      LD      A,$85           
4574: CD 85 21   CALL    $2185           
4577: CD 8D 3B   CALL    $3B8D           
457A: F0 E7      LD      A,($E7)         
457C: 1F         RRA                     
457D: 1F         RRA                     
457E: 1F         RRA                     
457F: E6 01      AND     $01             
4581: CD 87 3B   CALL    $3B87           
4584: C9         RET                     
4585: FA 9F C1   LD      A,($C19F)       
4588: A7         AND     A               
4589: 20 1F      JR      NZ,$45AA        
458B: FA 77 C1   LD      A,($C177)       
458E: A7         AND     A               
458F: 20 10      JR      NZ,$45A1        
4591: 1E 0B      LD      E,$0B           
4593: 21 00 DB   LD      HL,$DB00        
4596: 2A         LD      A,(HLI)         
4597: FE 09      CP      $09             
4599: 28 10      JR      Z,$45AB         
459B: 1D         DEC     E               
459C: 7B         LD      A,E             
459D: FE FF      CP      $FF             
459F: 20 F5      JR      NZ,$4596        
45A1: CD 8D 3B   CALL    $3B8D           
45A4: 70         LD      (HL),B          
45A5: 3E 8A      LD      A,$8A           
45A7: CD 85 21   CALL    $2185           
45AA: C9         RET                     
45AB: CD 8D 3B   CALL    $3B8D           
45AE: 3E 87      LD      A,$87           
45B0: C3 85 21   JP      $2185           
45B3: FA 9F C1   LD      A,($C19F)       
45B6: A7         AND     A               
45B7: 20 1E      JR      NZ,$45D7        
45B9: 3E 30      LD      A,$30           
45BB: EA 68 D3   LD      ($D368),A       
45BE: CD 8D 3B   CALL    $3B8D           
45C1: AF         XOR     A               
45C2: EA 10 D2   LD      ($D210),A       
45C5: EA 11 D2   LD      ($D211),A       
45C8: EA 12 D2   LD      ($D212),A       
45CB: EA 13 D2   LD      ($D213),A       
45CE: EA 17 D2   LD      ($D217),A       
45D1: EA 14 D2   LD      ($D214),A       
45D4: EA 18 D2   LD      ($D218),A       
45D7: C9         RET                     
45D8: 00         NOP                     
45D9: 00         NOP                     
45DA: 00         NOP                     
45DB: 00         NOP                     
45DC: 00         NOP                     
45DD: 00         NOP                     
45DE: 00         NOP                     
45DF: 00         NOP                     
45E0: 00         NOP                     
45E1: 00         NOP                     
45E2: 00         NOP                     
45E3: 00         NOP                     
45E4: 00         NOP                     
45E5: 00         NOP                     
45E6: 00         NOP                     
45E7: 00         NOP                     
45E8: 00         NOP                     
45E9: 00         NOP                     
45EA: 00         NOP                     
45EB: 00         NOP                     
45EC: 00         NOP                     
45ED: 00         NOP                     
45EE: 00         NOP                     
45EF: 00         NOP                     
45F0: 01 02 03   LD      BC,$0302        
45F3: 04         INC     B               
45F4: 00         NOP                     
45F5: 00         NOP                     
45F6: 00         NOP                     
45F7: 00         NOP                     
45F8: 00         NOP                     
45F9: 00         NOP                     
45FA: 00         NOP                     
45FB: 00         NOP                     
45FC: 00         NOP                     
45FD: 00         NOP                     
45FE: 00         NOP                     
45FF: 00         NOP                     
4600: 01 02 03   LD      BC,$0302        
4603: 04         INC     B               
4604: 00         NOP                     
4605: 00         NOP                     
4606: 00         NOP                     
4607: 00         NOP                     
4608: 00         NOP                     
4609: 00         NOP                     
460A: 00         NOP                     
460B: 00         NOP                     
460C: 00         NOP                     
460D: 00         NOP                     
460E: 00         NOP                     
460F: 00         NOP                     
4610: 01 02 03   LD      BC,$0302        
4613: 04         INC     B               
4614: 00         NOP                     
4615: 00         NOP                     
4616: 00         NOP                     
4617: 00         NOP                     
4618: 00         NOP                     
4619: 00         NOP                     
461A: 00         NOP                     
461B: 00         NOP                     
461C: 01 02 03   LD      BC,$0302        
461F: 04         INC     B               
4620: 00         NOP                     
4621: 00         NOP                     
4622: 00         NOP                     
4623: 00         NOP                     
4624: 00         NOP                     
4625: 00         NOP                     
4626: 02         LD      (BC),A          
4627: 01 02 01   LD      BC,$0102        
462A: 02         LD      (BC),A          
462B: 01 02 01   LD      BC,$0102        
462E: 00         NOP                     
462F: 00         NOP                     
4630: 00         NOP                     
4631: 00         NOP                     
4632: 00         NOP                     
4633: 01 00 01   LD      BC,$0100        
4636: 00         NOP                     
4637: 01 00 01   LD      BC,$0100        
463A: 00         NOP                     
463B: 01 00 01   LD      BC,$0100        
463E: 00         NOP                     
463F: 01 00 01   LD      BC,$0100        
4642: 02         LD      (BC),A          
4643: 01 02 01   LD      BC,$0102        
4646: 02         LD      (BC),A          
4647: 01 02 01   LD      BC,$0102        
464A: 02         LD      (BC),A          
464B: 01 02 01   LD      BC,$0102        
464E: 02         LD      (BC),A          
464F: 01 02 01   LD      BC,$0102        
4652: 02         LD      (BC),A          
4653: 01 02 01   LD      BC,$0102        
4656: 02         LD      (BC),A          
4657: 01 02 01   LD      BC,$0102        
465A: 02         LD      (BC),A          
465B: 01 02 01   LD      BC,$0102        
465E: 02         LD      (BC),A          
465F: 01 02 01   LD      BC,$0102        
4662: 02         LD      (BC),A          
4663: 01 02 01   LD      BC,$0102        
4666: 02         LD      (BC),A          
4667: 01 02 01   LD      BC,$0102        
466A: 02         LD      (BC),A          
466B: 01 02 02   LD      BC,$0202        
466E: 02         LD      (BC),A          
466F: 02         LD      (BC),A          
4670: 02         LD      (BC),A          
4671: 02         LD      (BC),A          
4672: 02         LD      (BC),A          
4673: 02         LD      (BC),A          
4674: 04         INC     B               
4675: 04         INC     B               
4676: 04         INC     B               
4677: 04         INC     B               
4678: 04         INC     B               
4679: 04         INC     B               
467A: 04         INC     B               
467B: 04         INC     B               
467C: 04         INC     B               
467D: 04         INC     B               
467E: 04         INC     B               
467F: 04         INC     B               
4680: 02         LD      (BC),A          
4681: 03         INC     BC              
4682: 02         LD      (BC),A          
4683: 03         INC     BC              
4684: 02         LD      (BC),A          
4685: 03         INC     BC              
4686: 02         LD      (BC),A          
4687: 03         INC     BC              
4688: 02         LD      (BC),A          
4689: 03         INC     BC              
468A: 02         LD      (BC),A          
468B: 02         LD      (BC),A          
468C: 03         INC     BC              
468D: 04         INC     B               
468E: 05         DEC     B               
468F: 06 05      LD      B,$05           
4691: 06 05      LD      B,$05           
4693: 06 05      LD      B,$05           
4695: 06 05      LD      B,$05           
4697: 06 05      LD      B,$05           
4699: 06 05      LD      B,$05           
469B: 06 05      LD      B,$05           
469D: 06 04      LD      B,$04           
469F: 02         LD      (BC),A          
46A0: 03         INC     BC              
46A1: 02         LD      (BC),A          
46A2: 03         INC     BC              
46A3: 02         LD      (BC),A          
46A4: 03         INC     BC              
46A5: 02         LD      (BC),A          
46A6: 03         INC     BC              
46A7: 02         LD      (BC),A          
46A8: 03         INC     BC              
46A9: 02         LD      (BC),A          
46AA: 03         INC     BC              
46AB: 02         LD      (BC),A          
46AC: 04         INC     B               
46AD: 05         DEC     B               
46AE: 04         INC     B               
46AF: 05         DEC     B               
46B0: 03         INC     BC              
46B1: 02         LD      (BC),A          
46B2: 03         INC     BC              
46B3: 02         LD      (BC),A          
46B4: 03         INC     BC              
46B5: 02         LD      (BC),A          
46B6: 03         INC     BC              
46B7: 02         LD      (BC),A          
46B8: 01 01 01   LD      BC,$0101        
46BB: 01 01 01   LD      BC,$0101        
46BE: 00         NOP                     
46BF: 00         NOP                     
46C0: 00         NOP                     
46C1: 00         NOP                     
46C2: 3E 02      LD      A,$02           
46C4: E0 A1      LDFF00  ($A1),A         
46C6: EA 67 C1   LD      ($C167),A       
46C9: FA 10 D2   LD      A,($D210)       
46CC: C6 01      ADD     $01             
46CE: EA 10 D2   LD      ($D210),A       
46D1: FA 11 D2   LD      A,($D211)       
46D4: CE 00      ADC     $00             
46D6: EA 11 D2   LD      ($D211),A       
46D9: FA 11 D2   LD      A,($D211)       
46DC: FE 05      CP      $05             
46DE: 20 10      JR      NZ,$46F0        
46E0: FA 10 D2   LD      A,($D210)       
46E3: FE F0      CP      $F0             
46E5: 20 09      JR      NZ,$46F0        
46E7: CD 8D 3B   CALL    $3B8D           
46EA: CD 91 08   CALL    $0891           
46ED: 36 20      LD      (HL),$20        
46EF: C9         RET                     
46F0: FA 12 D2   LD      A,($D212)       
46F3: 3C         INC     A               
46F4: FE 14      CP      $14             
46F6: 20 08      JR      NZ,$4700        
46F8: FA 13 D2   LD      A,($D213)       
46FB: 3C         INC     A               
46FC: EA 13 D2   LD      ($D213),A       
46FF: AF         XOR     A               
4700: EA 12 D2   LD      ($D212),A       
4703: FA 13 D2   LD      A,($D213)       
4706: 5F         LD      E,A             
4707: 50         LD      D,B             
4708: 21 26 46   LD      HL,$4626        
470B: 19         ADD     HL,DE           
470C: 7E         LD      A,(HL)          
470D: CD 87 3B   CALL    $3B87           
4710: 21 D8 45   LD      HL,$45D8        
4713: 19         ADD     HL,DE           
4714: 7E         LD      A,(HL)          
4715: 21 B0 C2   LD      HL,$C2B0        
4718: 09         ADD     HL,BC           
4719: 77         LD      (HL),A          
471A: 21 74 46   LD      HL,$4674        
471D: 19         ADD     HL,DE           
471E: 7E         LD      A,(HL)          
471F: EA 15 D2   LD      ($D215),A       
4722: FA 11 D2   LD      A,($D211)       
4725: 57         LD      D,A             
4726: FA 10 D2   LD      A,($D210)       
4729: 5F         LD      E,A             
472A: FE CC      CP      $CC             
472C: 20 05      JR      NZ,$4733        
472E: 7A         LD      A,D             
472F: FE 00      CP      $00             
4731: 28 10      JR      Z,$4743         
4733: 7B         LD      A,E             
4734: FE BE      CP      $BE             
4736: 20 05      JR      NZ,$473D        
4738: 7A         LD      A,D             
4739: FE 05      CP      $05             
473B: 28 01      JR      Z,$473E         
473D: C9         RET                     
473E: 3E 28      LD      A,$28           
4740: EA 14 D2   LD      ($D214),A       
4743: CD 8C 08   CALL    $088C           
4746: 36 28      LD      (HL),$28        
4748: C9         RET                     
4749: 00         NOP                     
474A: 00         NOP                     
474B: 40         LD      B,B             
474C: 00         NOP                     
474D: 00         NOP                     
474E: 08 42 00   LD      ($0042),SP      
4751: 00         NOP                     
4752: 10 44      STOP    $44             
4754: 00         NOP                     
4755: CD 91 08   CALL    $0891           
4758: 20 0A      JR      NZ,$4764        
475A: 36 70      LD      (HL),$70        
475C: 3E 10      LD      A,$10           
475E: EA 68 D3   LD      ($D368),A       
4761: CD 8D 3B   CALL    $3B8D           
4764: 3E 02      LD      A,$02           
4766: E0 A1      LDFF00  ($A1),A         
4768: CD 7A 45   CALL    $457A           
476B: C9         RET                     
476C: 90         SUB     B               
476D: 10 CD      STOP    $CD             
476F: 7A         LD      A,D             
4770: 45         LD      B,L             
4771: CD 91 08   CALL    $0891           
4774: 20 0F      JR      NZ,$4785        
4776: 3E 01      LD      A,$01           
4778: EA 4A DB   LD      ($DB4A),A       
477B: 21 49 DB   LD      HL,$DB49        
477E: CB CE      SET     1,E             
4780: CD 8D 3B   CALL    $3B8D           
4783: 70         LD      (HL),B          
4784: C9         RET                     
4785: FE 08      CP      $08             
4787: 20 06      JR      NZ,$478F        
4789: 35         DEC     (HL)            
478A: 3E 88      LD      A,$88           
478C: CD 85 21   CALL    $2185           
478F: 3E 6C      LD      A,$6C           
4791: E0 9D      LDFF00  ($9D),A         
4793: 3E 02      LD      A,$02           
4795: E0 A1      LDFF00  ($A1),A         
4797: F0 98      LD      A,($98)         
4799: E0 EE      LDFF00  ($EE),A         
479B: F0 99      LD      A,($99)         
479D: D6 0C      SUB     $0C             
479F: E0 EC      LDFF00  ($EC),A         
47A1: 11 6C 47   LD      DE,$476C        
47A4: AF         XOR     A               
47A5: E0 F1      LDFF00  ($F1),A         
47A7: CD D0 3C   CALL    $3CD0           
47AA: C9         RET                     
47AB: 00         NOP                     
47AC: 00         NOP                     
47AD: 50         LD      D,B             
47AE: 00         NOP                     
47AF: 00         NOP                     
47B0: 08 52 00   LD      ($0052),SP      
47B3: 10 00      STOP    $00             
47B5: 54         LD      D,H             
47B6: 00         NOP                     
47B7: 10 08      STOP    $08             
47B9: 56         LD      D,(HL)          
47BA: 00         NOP                     
47BB: F8 10      LDHL    SP,$10          
47BD: 58         LD      E,B             
47BE: 00         NOP                     
47BF: 08 10 5A   LD      ($5A10),SP      
47C2: 00         NOP                     
47C3: 18 10      JR      $47D5           
47C5: 5C         LD      E,H             
47C6: 00         NOP                     
47C7: 00         NOP                     
47C8: 18 5E      JR      $4828           
47CA: 00         NOP                     
47CB: 10 18      STOP    $18             
47CD: 5E         LD      E,(HL)          
47CE: 40         LD      B,B             
47CF: 00         NOP                     
47D0: 00         NOP                     
47D1: 50         LD      D,B             
47D2: 00         NOP                     
47D3: 00         NOP                     
47D4: 08 52 00   LD      ($0052),SP      
47D7: 10 00      STOP    $00             
47D9: 4A         LD      C,D             
47DA: 00         NOP                     
47DB: 10 08      STOP    $08             
47DD: 4C         LD      C,H             
47DE: 00         NOP                     
47DF: F8 10      LDHL    SP,$10          
47E1: 58         LD      E,B             
47E2: 00         NOP                     
47E3: 08 10 4E   LD      ($4E10),SP      
47E6: 00         NOP                     
47E7: 18 10      JR      $47F9           
47E9: 5C         LD      E,H             
47EA: 00         NOP                     
47EB: 00         NOP                     
47EC: 18 5E      JR      $484C           
47EE: 00         NOP                     
47EF: 10 18      STOP    $18             
47F1: 5E         LD      E,(HL)          
47F2: 40         LD      B,B             
47F3: 00         NOP                     
47F4: 00         NOP                     
47F5: 50         LD      D,B             
47F6: 00         NOP                     
47F7: 00         NOP                     
47F8: 08 52 00   LD      ($0052),SP      
47FB: 10 00      STOP    $00             
47FD: 54         LD      D,H             
47FE: 00         NOP                     
47FF: 10 08      STOP    $08             
4801: 56         LD      D,(HL)          
4802: 00         NOP                     
4803: F8 10      LDHL    SP,$10          
4805: 60         LD      H,B             
4806: 00         NOP                     
4807: 08 10 5A   LD      ($5A10),SP      
480A: 00         NOP                     
480B: 18 10      JR      $481D           
480D: 62         LD      H,D             
480E: 00         NOP                     
480F: 00         NOP                     
4810: 18 5E      JR      $4870           
4812: 00         NOP                     
4813: 10 18      STOP    $18             
4815: 5E         LD      E,(HL)          
4816: 40         LD      B,B             
4817: 00         NOP                     
4818: 00         NOP                     
4819: 46         LD      B,(HL)          
481A: 00         NOP                     
481B: 00         NOP                     
481C: 08 48 00   LD      ($0048),SP      
481F: 10 00      STOP    $00             
4821: 4A         LD      C,D             
4822: 00         NOP                     
4823: 10 08      STOP    $08             
4825: 4C         LD      C,H             
4826: 00         NOP                     
4827: F8 10      LDHL    SP,$10          
4829: 60         LD      H,B             
482A: 00         NOP                     
482B: 08 10 4E   LD      ($4E10),SP      
482E: 00         NOP                     
482F: 18 10      JR      $4841           
4831: 62         LD      H,D             
4832: 00         NOP                     
4833: 00         NOP                     
4834: 18 5E      JR      $4894           
4836: 00         NOP                     
4837: 10 18      STOP    $18             
4839: 5E         LD      E,(HL)          
483A: 40         LD      B,B             
483B: FF         RST     0X38            
483C: FF         RST     0X38            
483D: FF         RST     0X38            
483E: FF         RST     0X38            
483F: 64         LD      H,H             
4840: 00         NOP                     
4841: 66         LD      H,(HL)          
4842: 00         NOP                     
4843: 64         LD      H,H             
4844: 40         LD      B,B             
4845: 66         LD      H,(HL)          
4846: 40         LD      B,B             
4847: 66         LD      H,(HL)          
4848: 60         LD      H,B             
4849: 64         LD      H,H             
484A: 60         LD      H,B             
484B: 66         LD      H,(HL)          
484C: 20 64      JR      NZ,$48B2        
484E: 20 21      JR      NZ,$4871        
4850: B0         OR      B               
4851: C2 09 7E   JP      NZ,$7E09        
4854: E0 F1      LDFF00  ($F1),A         
4856: F0 EC      LD      A,($EC)         
4858: C6 03      ADD     $03             
485A: E0 EC      LDFF00  ($EC),A         
485C: 11 3B 48   LD      DE,$483B        
485F: CD 3B 3C   CALL    $3C3B           
4862: 3E 02      LD      A,$02           
4864: CD D0 3D   CALL    $3DD0           
4867: CD BA 3D   CALL    $3DBA           
486A: CD 8C 08   CALL    $088C           
486D: 28 04      JR      Z,$4873         
486F: 3E 03      LD      A,$03           
4871: 18 05      JR      $4878           
4873: 21 B0 C3   LD      HL,$C3B0        
4876: 09         ADD     HL,BC           
4877: 7E         LD      A,(HL)          
4878: 17         RLA                     
4879: 17         RLA                     
487A: E6 FC      AND     $FC             
487C: 5F         LD      E,A             
487D: 17         RLA                     
487E: 17         RLA                     
487F: 17         RLA                     
4880: E6 E0      AND     $E0             
4882: 83         ADD     A,E             
4883: 5F         LD      E,A             
4884: 50         LD      D,B             
4885: 21 AB 47   LD      HL,$47AB        
4888: 19         ADD     HL,DE           
4889: 0E 09      LD      C,$09           
488B: CD 26 3D   CALL    $3D26           
488E: 3E 09      LD      A,$09           
4890: CD D0 3D   CALL    $3DD0           
4893: CD 8C 08   CALL    $088C           
4896: C8         RET     Z               
4897: F0 EE      LD      A,($EE)         
4899: D6 18      SUB     $18             
489B: E0 EE      LDFF00  ($EE),A         
489D: F0 EC      LD      A,($EC)         
489F: D6 10      SUB     $10             
48A1: E0 EC      LDFF00  ($EC),A         
48A3: 21 49 47   LD      HL,$4749        
48A6: 0E 03      LD      C,$03           
48A8: CD 26 3D   CALL    $3D26           
48AB: 3E 03      LD      A,$03           
48AD: CD D0 3D   CALL    $3DD0           
48B0: C9         RET                     
48B1: 00         NOP                     
48B2: FC         ???                     
48B3: 76         HALT                    
48B4: 00         NOP                     
48B5: 00         NOP                     
48B6: 04         INC     B               
48B7: 78         LD      A,B             
48B8: 00         NOP                     
48B9: 00         NOP                     
48BA: 0C         INC     C               
48BB: 7A         LD      A,D             
48BC: 00         NOP                     
48BD: 00         NOP                     
48BE: FC         ???                     
48BF: 7C         LD      A,H             
48C0: 00         NOP                     
48C1: 00         NOP                     
48C2: 04         INC     B               
48C3: 78         LD      A,B             
48C4: 00         NOP                     
48C5: 00         NOP                     
48C6: 0C         INC     C               
48C7: 7E         LD      A,(HL)          
48C8: 00         NOP                     
48C9: 68         LD      L,B             
48CA: 00         NOP                     
48CB: 6A         LD      L,D             
48CC: 00         NOP                     
48CD: 6C         LD      L,H             
48CE: 00         NOP                     
48CF: 6E         LD      L,(HL)          
48D0: 00         NOP                     
48D1: 70         LD      (HL),B          
48D2: 00         NOP                     
48D3: 70         LD      (HL),B          
48D4: 20 6A      JR      NZ,$4940        
48D6: 20 68      JR      NZ,$4940        
48D8: 20 6E      JR      NZ,$4948        
48DA: 20 6C      JR      NZ,$4948        
48DC: 20 72      JR      NZ,$4950        
48DE: 00         NOP                     
48DF: 74         LD      (HL),H          
48E0: 00         NOP                     
48E1: 74         LD      (HL),H          
48E2: 20 72      JR      NZ,$4956        
48E4: 20 CD      JR      NZ,$48B3        
48E6: FD         ???                     
48E7: 48         LD      C,B             
48E8: F0 E7      LD      A,($E7)         
48EA: 1F         RRA                     
48EB: 1F         RRA                     
48EC: 1F         RRA                     
48ED: 1F         RRA                     
48EE: E6 01      AND     $01             
48F0: CD 87 3B   CALL    $3B87           
48F3: FA 15 D2   LD      A,($D215)       
48F6: A7         AND     A               
48F7: 28 03      JR      Z,$48FC         
48F9: CD 87 3B   CALL    $3B87           
48FC: C9         RET                     
48FD: FA 14 D2   LD      A,($D214)       
4900: A7         AND     A               
4901: 28 20      JR      Z,$4923         
4903: F0 EE      LD      A,($EE)         
4905: D6 18      SUB     $18             
4907: E0 EE      LDFF00  ($EE),A         
4909: F0 EC      LD      A,($EC)         
490B: D6 10      SUB     $10             
490D: E0 EC      LDFF00  ($EC),A         
490F: 21 49 47   LD      HL,$4749        
4912: 0E 03      LD      C,$03           
4914: CD 26 3D   CALL    $3D26           
4917: 3E 03      LD      A,$03           
4919: CD D0 3D   CALL    $3DD0           
491C: CD BA 3D   CALL    $3DBA           
491F: 3E 07      LD      A,$07           
4921: E0 F1      LDFF00  ($F1),A         
4923: F0 F1      LD      A,($F1)         
4925: FE 02      CP      $02             
4927: 30 13      JR      NC,$493C        
4929: 21 B1 48   LD      HL,$48B1        
492C: 3D         DEC     A               
492D: 20 03      JR      NZ,$4932        
492F: 21 BD 48   LD      HL,$48BD        
4932: 0E 03      LD      C,$03           
4934: CD 26 3D   CALL    $3D26           
4937: 3E 03      LD      A,$03           
4939: C3 D0 3D   JP      $3DD0           
493C: 11 C1 48   LD      DE,$48C1        
493F: CD 3B 3C   CALL    $3C3B           
4942: 3E 02      LD      A,$02           
4944: C3 D0 3D   JP      $3DD0           
4947: F0 00      LD      A,($00)         
4949: 70         LD      (HL),B          
494A: 00         NOP                     
494B: F0 08      LD      A,($08)         
494D: 72         LD      (HL),D          
494E: 00         NOP                     
494F: 00         NOP                     
4950: 00         NOP                     
4951: 74         LD      (HL),H          
4952: 00         NOP                     
4953: 00         NOP                     
4954: 08 76 00   LD      ($0076),SP      
4957: 21 47 49   LD      HL,$4947        
495A: 0E 04      LD      C,$04           
495C: CD 26 3D   CALL    $3D26           
495F: F0 F0      LD      A,($F0)         
4961: C7         RST     0X00            
4962: 68         LD      L,B             
4963: 49         LD      C,C             
4964: 7A         LD      A,D             
4965: 49         LD      C,C             
4966: B2         OR      D               
4967: 49         LD      C,C             
4968: F0 F8      LD      A,($F8)         
496A: E6 20      AND     $20             
496C: 28 08      JR      Z,$4976         
496E: 21 00 C2   LD      HL,$C200        
4971: 09         ADD     HL,BC           
4972: 7E         LD      A,(HL)          
4973: D6 10      SUB     $10             
4975: 77         LD      (HL),A          
4976: CD 8D 3B   CALL    $3B8D           
4979: C9         RET                     
497A: CD AF 7C   CALL    $7CAF           
497D: FA 7F DB   LD      A,($DB7F)       
4980: A7         AND     A               
4981: C0         RET     NZ              
4982: CD 0E 7D   CALL    $7D0E           
4985: 30 2A      JR      NC,$49B1        
4987: FA 0E DB   LD      A,($DB0E)       
498A: FE 0D      CP      $0D             
498C: 20 1E      JR      NZ,$49AC        
498E: 3E 0E      LD      A,$0E           
4990: EA 0E DB   LD      ($DB0E),A       
4993: 3E 01      LD      A,$01           
4995: EA 7F DB   LD      ($DB7F),A       
4998: 3E 04      LD      A,$04           
499A: E0 F4      LDFF00  ($F4),A         
499C: CD 91 08   CALL    $0891           
499F: 36 60      LD      (HL),$60        
49A1: CD 2B 7F   CALL    $7F2B           
49A4: 3E 16      LD      A,$16           
49A6: CD 85 21   CALL    $2185           
49A9: C3 8D 3B   JP      $3B8D           
49AC: 3E 9C      LD      A,$9C           
49AE: CD 85 21   CALL    $2185           
49B1: C9         RET                     
49B2: 3E 02      LD      A,$02           
49B4: E0 A1      LDFF00  ($A1),A         
49B6: EA 67 C1   LD      ($C167),A       
49B9: CD 91 08   CALL    $0891           
49BC: 20 0E      JR      NZ,$49CC        
49BE: CD 8D 3B   CALL    $3B8D           
49C1: 36 01      LD      (HL),$01        
49C3: 3E 02      LD      A,$02           
49C5: E0 F2      LDFF00  ($F2),A         
49C7: AF         XOR     A               
49C8: EA 67 C1   LD      ($C167),A       
49CB: C9         RET                     
49CC: FE 40      CP      $40             
49CE: 20 05      JR      NZ,$49D5        
49D0: 21 F4 FF   LD      HL,$FFF4        
49D3: 36 11      LD      (HL),$11        
49D5: 30 09      JR      NC,$49E0        
49D7: 21 40 C2   LD      HL,$C240        
49DA: 09         ADD     HL,BC           
49DB: 36 FC      LD      (HL),$FC        
49DD: CD DA 7D   CALL    $7DDA           
49E0: C9         RET                     
49E1: FF         RST     0X38            
49E2: FF         RST     0X38            
49E3: FF         RST     0X38            
49E4: FF         RST     0X38            
49E5: 54         LD      D,H             
49E6: 00         NOP                     
49E7: 54         LD      D,H             
49E8: 60         LD      H,B             
49E9: 54         LD      D,H             
49EA: 40         LD      B,B             
49EB: 54         LD      D,H             
49EC: 20 56      JR      NZ,$4A44        
49EE: 00         NOP                     
49EF: 56         LD      D,(HL)          
49F0: 20 52      JR      NZ,$4A44        
49F2: 00         NOP                     
49F3: 52         LD      D,D             
49F4: 20 11      JR      NZ,$4A07        
49F6: E1         POP     HL              
49F7: 49         LD      C,C             
49F8: CD 3B 3C   CALL    $3C3B           
49FB: CD 61 7D   CALL    $7D61           
49FE: CD 83 7D   CALL    $7D83           
4A01: F0 F0      LD      A,($F0)         
4A03: C7         RST     0X00            
4A04: 0C         INC     C               
4A05: 4A         LD      C,D             
4A06: 45         LD      B,L             
4A07: 4A         LD      C,D             
4A08: 50         LD      D,B             
4A09: 4A         LD      C,D             
4A0A: 77         LD      (HL),A          
4A0B: 4A         LD      C,D             
4A0C: 21 40 C3   LD      HL,$C340        
4A0F: 09         ADD     HL,BC           
4A10: CB F6      SET     1,E             
4A12: CD ED 27   CALL    $27ED           
4A15: E6 07      AND     $07             
4A17: 5F         LD      E,A             
4A18: 50         LD      D,B             
4A19: 21 5A 63   LD      HL,$635A        
4A1C: 19         ADD     HL,DE           
4A1D: 7E         LD      A,(HL)          
4A1E: 21 00 C2   LD      HL,$C200        
4A21: 09         ADD     HL,BC           
4A22: 77         LD      (HL),A          
4A23: 21 52 63   LD      HL,$6352        
4A26: 19         ADD     HL,DE           
4A27: 7E         LD      A,(HL)          
4A28: 21 10 C2   LD      HL,$C210        
4A2B: 09         ADD     HL,BC           
4A2C: 77         LD      (HL),A          
4A2D: CD 6E 64   CALL    $646E           
4A30: F0 DA      LD      A,($DA)         
4A32: FE 07      CP      $07             
4A34: 28 01      JR      Z,$4A37         
4A36: C9         RET                     
4A37: CD 91 08   CALL    $0891           
4A3A: CD ED 27   CALL    $27ED           
4A3D: E6 7F      AND     $7F             
4A3F: F6 40      OR      $40             
4A41: 77         LD      (HL),A          
4A42: C3 8D 3B   JP      $3B8D           
4A45: CD 91 08   CALL    $0891           
4A48: 20 05      JR      NZ,$4A4F        
4A4A: 36 60      LD      (HL),$60        
4A4C: CD 8D 3B   CALL    $3B8D           
4A4F: C9         RET                     
4A50: CD 91 08   CALL    $0891           
4A53: 20 10      JR      NZ,$4A65        
4A55: 36 60      LD      (HL),$60        
4A57: 21 D0 C3   LD      HL,$C3D0        
4A5A: 09         ADD     HL,BC           
4A5B: 70         LD      (HL),B          
4A5C: 21 40 C3   LD      HL,$C340        
4A5F: 09         ADD     HL,BC           
4A60: CB B6      SET     1,E             
4A62: C3 8D 3B   JP      $3B8D           
4A65: E6 04      AND     $04             
4A67: 3E 01      LD      A,$01           
4A69: 28 01      JR      Z,$4A6C         
4A6B: 3C         INC     A               
4A6C: C3 87 3B   JP      $3B87           
4A6F: 00         NOP                     
4A70: 00         NOP                     
4A71: 01 02 02   LD      BC,$0202        
4A74: 02         LD      (BC),A          
4A75: 01 00 21   LD      BC,$2100        
4A78: D0         RET     NC              
4A79: C3 09 7E   JP      $7E09           
4A7C: 34         INC     (HL)            
4A7D: 1F         RRA                     
4A7E: 1F         RRA                     
4A7F: 1F         RRA                     
4A80: E6 07      AND     $07             
4A82: 5F         LD      E,A             
4A83: 50         LD      D,B             
4A84: 21 6F 4A   LD      HL,$4A6F        
4A87: 19         ADD     HL,DE           
4A88: 7E         LD      A,(HL)          
4A89: 21 10 C3   LD      HL,$C310        
4A8C: 09         ADD     HL,BC           
4A8D: 77         LD      (HL),A          
4A8E: CD B4 3B   CALL    $3BB4           
4A91: CD 91 08   CALL    $0891           
4A94: 20 1C      JR      NZ,$4AB2        
4A96: CD 8D 3B   CALL    $3B8D           
4A99: 70         LD      (HL),B          
4A9A: AF         XOR     A               
4A9B: CD 87 3B   CALL    $3B87           
4A9E: 3E 0E      LD      A,$0E           
4AA0: E0 F2      LDFF00  ($F2),A         
4AA2: F0 EE      LD      A,($EE)         
4AA4: E0 D7      LDFF00  ($D7),A         
4AA6: F0 EC      LD      A,($EC)         
4AA8: C6 00      ADD     $00             
4AAA: E0 D8      LDFF00  ($D8),A         
4AAC: 3E 01      LD      A,$01           
4AAE: CD 53 09   CALL    $0953           
4AB1: C9         RET                     
4AB2: FE 30      CP      $30             
4AB4: 20 23      JR      NZ,$4AD9        
4AB6: 3E 7D      LD      A,$7D           
4AB8: CD 01 3C   CALL    $3C01           
4ABB: 38 1C      JR      C,$4AD9         
4ABD: F0 D7      LD      A,($D7)         
4ABF: 21 00 C2   LD      HL,$C200        
4AC2: 19         ADD     HL,DE           
4AC3: 77         LD      (HL),A          
4AC4: F0 D8      LD      A,($D8)         
4AC6: 21 10 C2   LD      HL,$C210        
4AC9: 19         ADD     HL,DE           
4ACA: 77         LD      (HL),A          
4ACB: 21 B0 C2   LD      HL,$C2B0        
4ACE: 19         ADD     HL,DE           
4ACF: 34         INC     (HL)            
4AD0: C5         PUSH    BC              
4AD1: D5         PUSH    DE              
4AD2: C1         POP     BC              
4AD3: 3E 18      LD      A,$18           
4AD5: CD 25 3C   CALL    $3C25           
4AD8: C1         POP     BC              
4AD9: CD 91 08   CALL    $0891           
4ADC: 1E 03      LD      E,$03           
4ADE: FE 50      CP      $50             
4AE0: 30 05      JR      NC,$4AE7        
4AE2: FE 20      CP      $20             
4AE4: 38 01      JR      C,$4AE7         
4AE6: 1C         INC     E               
4AE7: 7B         LD      A,E             
4AE8: C3 87 3B   JP      $3B87           
4AEB: 00         NOP                     
4AEC: 00         NOP                     
4AED: 70         LD      (HL),B          
4AEE: 00         NOP                     
4AEF: 00         NOP                     
4AF0: 08 72 00   LD      ($0072),SP      
4AF3: 10 00      STOP    $00             
4AF5: 74         LD      (HL),H          
4AF6: 00         NOP                     
4AF7: 10 08      STOP    $08             
4AF9: 74         LD      (HL),H          
4AFA: 20 00      JR      NZ,$4AFC        
4AFC: 00         NOP                     
4AFD: 72         LD      (HL),D          
4AFE: 20 00      JR      NZ,$4B00        
4B00: 08 70 20   LD      ($2070),SP      
4B03: 10 00      STOP    $00             
4B05: 74         LD      (HL),H          
4B06: 00         NOP                     
4B07: 10 08      STOP    $08             
4B09: 74         LD      (HL),H          
4B0A: 20 00      JR      NZ,$4B0C        
4B0C: 00         NOP                     
4B0D: 78         LD      A,B             
4B0E: 20 00      JR      NZ,$4B10        
4B10: 08 76 20   LD      ($2076),SP      
4B13: 10 00      STOP    $00             
4B15: 74         LD      (HL),H          
4B16: 00         NOP                     
4B17: 10 08      STOP    $08             
4B19: 74         LD      (HL),H          
4B1A: 20 00      JR      NZ,$4B1C        
4B1C: 00         NOP                     
4B1D: 76         HALT                    
4B1E: 00         NOP                     
4B1F: 00         NOP                     
4B20: 08 78 00   LD      ($0078),SP      
4B23: 10 00      STOP    $00             
4B25: 74         LD      (HL),H          
4B26: 00         NOP                     
4B27: 10 08      STOP    $08             
4B29: 74         LD      (HL),H          
4B2A: 20 7A      JR      NZ,$4BA6        
4B2C: 00         NOP                     
4B2D: 7C         LD      A,H             
4B2E: 00         NOP                     
4B2F: 7E         LD      A,(HL)          
4B30: 00         NOP                     
4B31: 7E         LD      A,(HL)          
4B32: 20 F0      JR      NZ,$4B24        
4B34: F1         POP     AF              
4B35: 17         RLA                     
4B36: 17         RLA                     
4B37: 17         RLA                     
4B38: 17         RLA                     
4B39: E6 F0      AND     $F0             
4B3B: 5F         LD      E,A             
4B3C: 50         LD      D,B             
4B3D: 21 EB 4A   LD      HL,$4AEB        
4B40: 19         ADD     HL,DE           
4B41: 0E 04      LD      C,$04           
4B43: CD 26 3D   CALL    $3D26           
4B46: 3E 04      LD      A,$04           
4B48: CD D0 3D   CALL    $3DD0           
4B4B: F0 E7      LD      A,($E7)         
4B4D: 1F         RRA                     
4B4E: 1F         RRA                     
4B4F: 1F         RRA                     
4B50: 1F         RRA                     
4B51: 1F         RRA                     
4B52: E6 01      AND     $01             
4B54: CD 87 3B   CALL    $3B87           
4B57: CD 30 7E   CALL    $7E30           
4B5A: C6 0C      ADD     $0C             
4B5C: FE 18      CP      $18             
4B5E: 30 0F      JR      NC,$4B6F        
4B60: CD 20 7E   CALL    $7E20           
4B63: C6 10      ADD     $10             
4B65: FE 20      CP      $20             
4B67: 30 06      JR      NC,$4B6F        
4B69: 7B         LD      A,E             
4B6A: C6 02      ADD     $02             
4B6C: CD 87 3B   CALL    $3B87           
4B6F: CD AF 7C   CALL    $7CAF           
4B72: F0 F6      LD      A,($F6)         
4B74: FE A8      CP      $A8             
4B76: CA F6 4B   JP      Z,$4BF6         
4B79: 11 2B 4B   LD      DE,$4B2B        
4B7C: FA 0E DB   LD      A,($DB0E)       
4B7F: FE 09      CP      $09             
4B81: 30 03      JR      NC,$4B86        
4B83: 11 2F 4B   LD      DE,$4B2F        
4B86: AF         XOR     A               
4B87: E0 F1      LDFF00  ($F1),A         
4B89: F0 EE      LD      A,($EE)         
4B8B: C6 18      ADD     $18             
4B8D: E0 EE      LDFF00  ($EE),A         
4B8F: F0 EC      LD      A,($EC)         
4B91: C6 08      ADD     $08             
4B93: E0 EC      LDFF00  ($EC),A         
4B95: CD 3B 3C   CALL    $3C3B           
4B98: CD BA 3D   CALL    $3DBA           
4B9B: CD 61 7D   CALL    $7D61           
4B9E: F0 F0      LD      A,($F0)         
4BA0: C7         RST     0X00            
4BA1: A7         AND     A               
4BA2: 4B         LD      C,E             
4BA3: C5         PUSH    BC              
4BA4: 4B         LD      C,E             
4BA5: DF         RST     0X18            
4BA6: 4B         LD      C,E             
4BA7: CD 02 7D   CALL    $7D02           
4BAA: 30 18      JR      NC,$4BC4        
4BAC: FA 0E DB   LD      A,($DB0E)       
4BAF: FE 08      CP      $08             
4BB1: 20 08      JR      NZ,$4BBB        
4BB3: 3E 67      LD      A,$67           
4BB5: CD 85 21   CALL    $2185           
4BB8: C3 8D 3B   JP      $3B8D           
4BBB: 3E 66      LD      A,$66           
4BBD: 38 02      JR      C,$4BC1         
4BBF: 3E 6B      LD      A,$6B           
4BC1: CD 85 21   CALL    $2185           
4BC4: C9         RET                     
4BC5: FA 9F C1   LD      A,($C19F)       
4BC8: A7         AND     A               
4BC9: 20 0E      JR      NZ,$4BD9        
4BCB: CD 8D 3B   CALL    $3B8D           
4BCE: FA 77 C1   LD      A,($C177)       
4BD1: A7         AND     A               
4BD2: 20 05      JR      NZ,$4BD9        
4BD4: 3E 68      LD      A,$68           
4BD6: C3 85 21   JP      $2185           
4BD9: 70         LD      (HL),B          
4BDA: 3E 69      LD      A,$69           
4BDC: C3 85 21   JP      $2185           
4BDF: FA 9F C1   LD      A,($C19F)       
4BE2: A7         AND     A               
4BE3: 20 10      JR      NZ,$4BF5        
4BE5: CD 8D 3B   CALL    $3B8D           
4BE8: 70         LD      (HL),B          
4BE9: CD 98 08   CALL    $0898           
4BEC: 3E 09      LD      A,$09           
4BEE: EA 0E DB   LD      ($DB0E),A       
4BF1: 3E 0D      LD      A,$0D           
4BF3: E0 A5      LDFF00  ($A5),A         
4BF5: C9         RET                     
4BF6: CD 61 7D   CALL    $7D61           
4BF9: F0 F0      LD      A,($F0)         
4BFB: C7         RST     0X00            
4BFC: 08 4C 26   LD      ($264C),SP      
4BFF: 4C         LD      C,H             
4C00: 31 4C 44   LD      SP,$444C        
4C03: 4C         LD      C,H             
4C04: 5A         LD      E,D             
4C05: 4C         LD      C,H             
4C06: 7D         LD      A,L             
4C07: 4C         LD      C,H             
4C08: CD 02 7D   CALL    $7D02           
4C0B: 30 18      JR      NC,$4C25        
4C0D: FA 0E DB   LD      A,($DB0E)       
4C10: FE 09      CP      $09             
4C12: 20 08      JR      NZ,$4C1C        
4C14: 3E 34      LD      A,$34           
4C16: CD 85 21   CALL    $2185           
4C19: C3 8D 3B   JP      $3B8D           
4C1C: 3E 33      LD      A,$33           
4C1E: 38 02      JR      C,$4C22         
4C20: 3E 39      LD      A,$39           
4C22: CD 85 21   CALL    $2185           
4C25: C9         RET                     
4C26: FA 9F C1   LD      A,($C19F)       
4C29: A7         AND     A               
4C2A: 20 04      JR      NZ,$4C30        
4C2C: CD 8D 3B   CALL    $3B8D           
4C2F: C9         RET                     
4C30: C9         RET                     
4C31: CD 8D 3B   CALL    $3B8D           
4C34: 3E 08      LD      A,$08           
4C36: EA 95 DB   LD      ($DB95),A       
4C39: AF         XOR     A               
4C3A: EA 6B C1   LD      ($C16B),A       
4C3D: EA 6C C1   LD      ($C16C),A       
4C40: EA 96 DB   LD      ($DB96),A       
4C43: C9         RET                     
4C44: FA 6B C1   LD      A,($C16B)       
4C47: FE 04      CP      $04             
4C49: 20 0E      JR      NZ,$4C59        
4C4B: FA 9F C1   LD      A,($C19F)       
4C4E: A7         AND     A               
4C4F: 20 08      JR      NZ,$4C59        
4C51: CD 8D 3B   CALL    $3B8D           
4C54: 3E 35      LD      A,$35           
4C56: CD 85 21   CALL    $2185           
4C59: C9         RET                     
4C5A: FA 9F C1   LD      A,($C19F)       
4C5D: A7         AND     A               
4C5E: 20 1C      JR      NZ,$4C7C        
4C60: CD 8D 3B   CALL    $3B8D           
4C63: FA 77 C1   LD      A,($C177)       
4C66: A7         AND     A               
4C67: 20 0D      JR      NZ,$4C76        
4C69: CD 98 08   CALL    $0898           
4C6C: 3E 0A      LD      A,$0A           
4C6E: EA 0E DB   LD      ($DB0E),A       
4C71: 3E 0D      LD      A,$0D           
4C73: E0 A5      LDFF00  ($A5),A         
4C75: C9         RET                     
4C76: 35         DEC     (HL)            
4C77: 3E 37      LD      A,$37           
4C79: CD 85 21   CALL    $2185           
4C7C: C9         RET                     
4C7D: CD 02 7D   CALL    $7D02           
4C80: 30 05      JR      NC,$4C87        
4C82: 3E 38      LD      A,$38           
4C84: CD 85 21   CALL    $2185           
4C87: C9         RET                     
4C88: 62         LD      H,D             
4C89: 20 60      JR      NZ,$4CEB        
4C8B: 20 66      JR      NZ,$4CF3        
4C8D: 20 64      JR      NZ,$4CF3        
4C8F: 20 6C      JR      NZ,$4CFD        
4C91: 00         NOP                     
4C92: 6E         LD      L,(HL)          
4C93: 00         NOP                     
4C94: 68         LD      L,B             
4C95: 00         NOP                     
4C96: 6A         LD      L,D             
4C97: 00         NOP                     
4C98: 6A         LD      L,D             
4C99: 20 68      JR      NZ,$4D03        
4C9B: 20 6C      JR      NZ,$4D09        
4C9D: 00         NOP                     
4C9E: 6E         LD      L,(HL)          
4C9F: 00         NOP                     
4CA0: 9A         SBC     D               
4CA1: 10 9C      STOP    $9C             
4CA3: 10 21      STOP    $21             
4CA5: 40         LD      B,B             
4CA6: C4 09 7E   CALL    NZ,$7E09        
4CA9: A7         AND     A               
4CAA: 20 12      JR      NZ,$4CBE        
4CAC: 34         INC     (HL)            
4CAD: FA 69 DB   LD      A,($DB69)       
4CB0: 16 B1      LD      D,$B1           
4CB2: E6 02      AND     $02             
4CB4: 28 02      JR      Z,$4CB8         
4CB6: 16 CD      LD      D,$CD           
4CB8: F0 F6      LD      A,($F6)         
4CBA: BA         CP      D               
4CBB: C2 76 7E   JP      NZ,$7E76        
4CBE: 11 88 4C   LD      DE,$4C88        
4CC1: AF         XOR     A               
4CC2: E0 E8      LDFF00  ($E8),A         
4CC4: FA 0E DB   LD      A,($DB0E)       
4CC7: FE 0B      CP      $0B             
4CC9: 30 15      JR      NC,$4CE0        
4CCB: FA 69 DB   LD      A,($DB69)       
4CCE: E6 02      AND     $02             
4CD0: 20 07      JR      NZ,$4CD9        
4CD2: FA 0E DB   LD      A,($DB0E)       
4CD5: FE 0A      CP      $0A             
4CD7: 38 07      JR      C,$4CE0         
4CD9: 3E 01      LD      A,$01           
4CDB: E0 E8      LDFF00  ($E8),A         
4CDD: 11 94 4C   LD      DE,$4C94        
4CE0: CD 3B 3C   CALL    $3C3B           
4CE3: CD 61 7D   CALL    $7D61           
4CE6: F0 E7      LD      A,($E7)         
4CE8: 1F         RRA                     
4CE9: 1F         RRA                     
4CEA: 1F         RRA                     
4CEB: 1F         RRA                     
4CEC: E6 01      AND     $01             
4CEE: CD 87 3B   CALL    $3B87           
4CF1: CD AF 7C   CALL    $7CAF           
4CF4: F0 F0      LD      A,($F0)         
4CF6: C7         RST     0X00            
4CF7: FF         RST     0X38            
4CF8: 4C         LD      C,H             
4CF9: 35         DEC     (HL)            
4CFA: 4D         LD      C,L             
4CFB: 55         LD      D,L             
4CFC: 4D         LD      C,L             
4CFD: 8F         ADC     A,A             
4CFE: 4D         LD      C,L             
4CFF: CD 0E 7D   CALL    $7D0E           
4D02: 30 30      JR      NC,$4D34        
4D04: FA 56 DB   LD      A,($DB56)       
4D07: FE 80      CP      $80             
4D09: 3E 78      LD      A,$78           
4D0B: 28 10      JR      Z,$4D1D         
4D0D: F0 E8      LD      A,($E8)         
4D0F: A7         AND     A               
4D10: 20 0E      JR      NZ,$4D20        
4D12: FA 0E DB   LD      A,($DB0E)       
4D15: FE 0B      CP      $0B             
4D17: 3E 5A      LD      A,$5A           
4D19: 38 02      JR      C,$4D1D         
4D1B: 3E 5F      LD      A,$5F           
4D1D: C3 85 21   JP      $2185           
4D20: FA 0E DB   LD      A,($DB0E)       
4D23: FE 0A      CP      $0A             
4D25: 20 08      JR      NZ,$4D2F        
4D27: 3E 5C      LD      A,$5C           
4D29: CD 85 21   CALL    $2185           
4D2C: C3 8D 3B   JP      $3B8D           
4D2F: 3E 5B      LD      A,$5B           
4D31: CD 85 21   CALL    $2185           
4D34: C9         RET                     
4D35: FA 77 C1   LD      A,($C177)       
4D38: A7         AND     A               
4D39: 20 10      JR      NZ,$4D4B        
4D3B: 3E 01      LD      A,$01           
4D3D: E0 F2      LDFF00  ($F2),A         
4D3F: EA 7F DB   LD      ($DB7F),A       
4D42: CD 91 08   CALL    $0891           
4D45: 36 80      LD      (HL),$80        
4D47: CD 8D 3B   CALL    $3B8D           
4D4A: C9         RET                     
4D4B: 3E 59      LD      A,$59           
4D4D: CD 85 21   CALL    $2185           
4D50: CD 8D 3B   CALL    $3B8D           
4D53: 70         LD      (HL),B          
4D54: C9         RET                     
4D55: CD 91 08   CALL    $0891           
4D58: 20 11      JR      NZ,$4D6B        
4D5A: 3E 0B      LD      A,$0B           
4D5C: EA 0E DB   LD      ($DB0E),A       
4D5F: 3E 0D      LD      A,$0D           
4D61: E0 A5      LDFF00  ($A5),A         
4D63: 3E 5D      LD      A,$5D           
4D65: CD 85 21   CALL    $2185           
4D68: C3 8D 3B   JP      $3B8D           
4D6B: 3E 02      LD      A,$02           
4D6D: E0 A1      LDFF00  ($A1),A         
4D6F: EA 67 C1   LD      ($C167),A       
4D72: AF         XOR     A               
4D73: E0 F1      LDFF00  ($F1),A         
4D75: F0 EC      LD      A,($EC)         
4D77: D6 0E      SUB     $0E             
4D79: E0 EC      LDFF00  ($EC),A         
4D7B: F0 EE      LD      A,($EE)         
4D7D: D6 04      SUB     $04             
4D7F: E0 EE      LDFF00  ($EE),A         
4D81: 11 A0 4C   LD      DE,$4CA0        
4D84: CD 3B 3C   CALL    $3C3B           
4D87: CD BA 3D   CALL    $3DBA           
4D8A: 3E 02      LD      A,$02           
4D8C: C3 87 3B   JP      $3B87           
4D8F: FA 9F C1   LD      A,($C19F)       
4D92: A7         AND     A               
4D93: 20 0D      JR      NZ,$4DA2        
4D95: EA 7F DB   LD      ($DB7F),A       
4D98: EA 67 C1   LD      ($C167),A       
4D9B: CD 98 08   CALL    $0898           
4D9E: CD 8D 3B   CALL    $3B8D           
4DA1: 70         LD      (HL),B          
4DA2: C9         RET                     
4DA3: 00         NOP                     
4DA4: F8 60      LDHL    SP,$60          
4DA6: 00         NOP                     
4DA7: 00         NOP                     
4DA8: 00         NOP                     
4DA9: 62         LD      H,D             
4DAA: 00         NOP                     
4DAB: 00         NOP                     
4DAC: 08 64 00   LD      ($0064),SP      
4DAF: 00         NOP                     
4DB0: F8 66      LDHL    SP,$66          
4DB2: 00         NOP                     
4DB3: 00         NOP                     
4DB4: 00         NOP                     
4DB5: 68         LD      L,B             
4DB6: 00         NOP                     
4DB7: 00         NOP                     
4DB8: 08 6A 00   LD      ($006A),SP      
4DBB: 02         LD      (BC),A          
4DBC: 00         NOP                     
4DBD: 06 04      LD      B,$04           
4DBF: F0 F1      LD      A,($F1)         
4DC1: CB 27      SET     1,E             
4DC3: CB 27      SET     1,E             
4DC5: 5F         LD      E,A             
4DC6: CB 27      SET     1,E             
4DC8: 83         ADD     A,E             
4DC9: 5F         LD      E,A             
4DCA: 50         LD      D,B             
4DCB: 21 A3 4D   LD      HL,$4DA3        
4DCE: 19         ADD     HL,DE           
4DCF: 0E 03      LD      C,$03           
4DD1: CD 26 3D   CALL    $3D26           
4DD4: F0 E7      LD      A,($E7)         
4DD6: 1F         RRA                     
4DD7: 1F         RRA                     
4DD8: 1F         RRA                     
4DD9: 1F         RRA                     
4DDA: E6 01      AND     $01             
4DDC: CD 87 3B   CALL    $3B87           
4DDF: CD 61 7D   CALL    $7D61           
4DE2: CD AF 7C   CALL    $7CAF           
4DE5: F0 F0      LD      A,($F0)         
4DE7: C7         RST     0X00            
4DE8: EE 4D      XOR     $4D             
4DEA: 0B         DEC     BC              
4DEB: 4E         LD      C,(HL)          
4DEC: 32         LD      (HLD),A         
4DED: 4E         LD      C,(HL)          
4DEE: CD 0E 7D   CALL    $7D0E           
4DF1: 30 17      JR      NC,$4E0A        
4DF3: FA 0E DB   LD      A,($DB0E)       
4DF6: A7         AND     A               
4DF7: 1E 2A      LD      E,$2A           
4DF9: 28 0B      JR      Z,$4E06         
4DFB: 1E 2C      LD      E,$2C           
4DFD: FE 01      CP      $01             
4DFF: 20 05      JR      NZ,$4E06        
4E01: CD 8D 3B   CALL    $3B8D           
4E04: 1E 2B      LD      E,$2B           
4E06: 7B         LD      A,E             
4E07: CD 85 21   CALL    $2185           
4E0A: C9         RET                     
4E0B: FA 9F C1   LD      A,($C19F)       
4E0E: A7         AND     A               
4E0F: 20 20      JR      NZ,$4E31        
4E11: FA 77 C1   LD      A,($C177)       
4E14: A7         AND     A               
4E15: 20 11      JR      NZ,$4E28        
4E17: 3E 02      LD      A,$02           
4E19: EA 0E DB   LD      ($DB0E),A       
4E1C: 3E 0D      LD      A,$0D           
4E1E: E0 A5      LDFF00  ($A5),A         
4E20: 3E 28      LD      A,$28           
4E22: CD 85 21   CALL    $2185           
4E25: C3 8D 3B   JP      $3B8D           
4E28: 3E 27      LD      A,$27           
4E2A: CD 85 21   CALL    $2185           
4E2D: CD 8D 3B   CALL    $3B8D           
4E30: 70         LD      (HL),B          
4E31: C9         RET                     
4E32: FA 9F C1   LD      A,($C19F)       
4E35: A7         AND     A               
4E36: 20 07      JR      NZ,$4E3F        
4E38: CD 98 08   CALL    $0898           
4E3B: CD 8D 3B   CALL    $3B8D           
4E3E: 70         LD      (HL),B          
4E3F: C9         RET                     
4E40: 21 D0 C2   LD      HL,$C2D0        
4E43: 09         ADD     HL,BC           
4E44: 7E         LD      A,(HL)          
4E45: A7         AND     A               
4E46: C2 50 50   JP      NZ,$5050        
4E49: F0 F8      LD      A,($F8)         
4E4B: E6 20      AND     $20             
4E4D: C2 76 7E   JP      NZ,$7E76        
4E50: CD E2 08   CALL    $08E2           
4E53: F0 F0      LD      A,($F0)         
4E55: C7         RST     0X00            
4E56: 68         LD      L,B             
4E57: 4E         LD      C,(HL)          
4E58: 81         ADD     A,C             
4E59: 4E         LD      C,(HL)          
4E5A: 9B         SBC     E               
4E5B: 4E         LD      C,(HL)          
4E5C: C1         POP     BC              
4E5D: 4E         LD      C,(HL)          
4E5E: E8 4E      ADD     SP,$4E          
4E60: FF         RST     0X38            
4E61: 4E         LD      C,(HL)          
4E62: 32         LD      (HLD),A         
4E63: 4F         LD      C,A             
4E64: 6F         LD      L,A             
4E65: 4F         LD      C,A             
4E66: BD         CP      L               
4E67: 4F         LD      C,A             
4E68: FA 76 DB   LD      A,($DB76)       
4E6B: 21 F9 4E   LD      HL,$4EF9        
4E6E: BE         CP      (HL)            
4E6F: 20 0F      JR      NZ,$4E80        
4E71: 23         INC     HL              
4E72: FA 77 DB   LD      A,($DB77)       
4E75: BE         CP      (HL)            
4E76: 20 08      JR      NZ,$4E80        
4E78: 23         INC     HL              
4E79: FA 78 DB   LD      A,($DB78)       
4E7C: BE         CP      (HL)            
4E7D: CA 76 7E   JP      Z,$7E76         
4E80: C9         RET                     
4E81: CD 91 08   CALL    $0891           
4E84: 36 90      LD      (HL),$90        
4E86: F0 EE      LD      A,($EE)         
4E88: E0 D7      LDFF00  ($D7),A         
4E8A: F0 EC      LD      A,($EC)         
4E8C: E0 D8      LDFF00  ($D8),A         
4E8E: 3E 02      LD      A,$02           
4E90: CD 53 09   CALL    $0953           
4E93: 3E 06      LD      A,$06           
4E95: E0 F2      LDFF00  ($F2),A         
4E97: CD 8D 3B   CALL    $3B8D           
4E9A: C9         RET                     
4E9B: CD 31 50   CALL    $5031           
4E9E: CD 91 08   CALL    $0891           
4EA1: 20 05      JR      NZ,$4EA8        
4EA3: 36 60      LD      (HL),$60        
4EA5: C3 8D 3B   JP      $3B8D           
4EA8: 1E FC      LD      E,$FC           
4EAA: D6 08      SUB     $08             
4EAC: E6 10      AND     $10             
4EAE: 28 02      JR      Z,$4EB2         
4EB0: 1E 04      LD      E,$04           
4EB2: 21 40 C2   LD      HL,$C240        
4EB5: 09         ADD     HL,BC           
4EB6: 73         LD      (HL),E          
4EB7: 21 50 C2   LD      HL,$C250        
4EBA: 09         ADD     HL,BC           
4EBB: 36 FC      LD      (HL),$FC        
4EBD: CD CD 7D   CALL    $7DCD           
4EC0: C9         RET                     
4EC1: CD 31 50   CALL    $5031           
4EC4: CD 91 08   CALL    $0891           
4EC7: 20 1E      JR      NZ,$4EE7        
4EC9: 36 48      LD      (HL),$48        
4ECB: 3E 02      LD      A,$02           
4ECD: CD 01 3C   CALL    $3C01           
4ED0: F0 D7      LD      A,($D7)         
4ED2: 21 00 C2   LD      HL,$C200        
4ED5: 19         ADD     HL,DE           
4ED6: 77         LD      (HL),A          
4ED7: F0 D8      LD      A,($D8)         
4ED9: 21 10 C2   LD      HL,$C210        
4EDC: 19         ADD     HL,DE           
4EDD: 77         LD      (HL),A          
4EDE: 21 E0 C2   LD      HL,$C2E0        
4EE1: 19         ADD     HL,DE           
4EE2: 36 20      LD      (HL),$20        
4EE4: CD 8D 3B   CALL    $3B8D           
4EE7: C9         RET                     
4EE8: CD 16 50   CALL    $5016           
4EEB: CD 91 08   CALL    $0891           
4EEE: 20 08      JR      NZ,$4EF8        
4EF0: 3E E1      LD      A,$E1           
4EF2: CD EE 4F   CALL    $4FEE           
4EF5: CD 8D 3B   CALL    $3B8D           
4EF8: C9         RET                     
4EF9: 40         LD      B,B             
4EFA: 60         LD      H,B             
4EFB: 60         LD      H,B             
4EFC: E2         LDFF00  (C),A           
4EFD: E3         ???                     
4EFE: E4         ???                     
4EFF: CD 16 50   CALL    $5016           
4F02: FA 9F C1   LD      A,($C19F)       
4F05: A7         AND     A               
4F06: 20 29      JR      NZ,$4F31        
4F08: 21 B0 C2   LD      HL,$C2B0        
4F0B: 09         ADD     HL,BC           
4F0C: 5E         LD      E,(HL)          
4F0D: 16 00      LD      D,$00           
4F0F: 7B         LD      A,E             
4F10: EA 01 D2   LD      ($D201),A       
4F13: 3C         INC     A               
4F14: FE 03      CP      $03             
4F16: 20 01      JR      NZ,$4F19        
4F18: AF         XOR     A               
4F19: 77         LD      (HL),A          
4F1A: 21 F9 4E   LD      HL,$4EF9        
4F1D: 19         ADD     HL,DE           
4F1E: 7E         LD      A,(HL)          
4F1F: 21 76 DB   LD      HL,$DB76        
4F22: 19         ADD     HL,DE           
4F23: BE         CP      (HL)            
4F24: 28 E2      JR      Z,$4F08         
4F26: 21 FC 4E   LD      HL,$4EFC        
4F29: 19         ADD     HL,DE           
4F2A: 7E         LD      A,(HL)          
4F2B: CD EE 4F   CALL    $4FEE           
4F2E: CD 8D 3B   CALL    $3B8D           
4F31: C9         RET                     
4F32: CD 16 50   CALL    $5016           
4F35: FA 9F C1   LD      A,($C19F)       
4F38: A7         AND     A               
4F39: C0         RET     NZ              
4F3A: CD 8D 3B   CALL    $3B8D           
4F3D: FA 77 C1   LD      A,($C177)       
4F40: A7         AND     A               
4F41: 20 29      JR      NZ,$4F6C        
4F43: 3E CA      LD      A,$CA           
4F45: CD 01 3C   CALL    $3C01           
4F48: 3E 26      LD      A,$26           
4F4A: E0 F4      LDFF00  ($F4),A         
4F4C: F0 D7      LD      A,($D7)         
4F4E: 21 00 C2   LD      HL,$C200        
4F51: 19         ADD     HL,DE           
4F52: 77         LD      (HL),A          
4F53: F0 D8      LD      A,($D8)         
4F55: 21 10 C2   LD      HL,$C210        
4F58: 19         ADD     HL,DE           
4F59: 77         LD      (HL),A          
4F5A: 21 D0 C2   LD      HL,$C2D0        
4F5D: 19         ADD     HL,DE           
4F5E: 36 01      LD      (HL),$01        
4F60: 21 E0 C2   LD      HL,$C2E0        
4F63: 19         ADD     HL,DE           
4F64: 36 C0      LD      (HL),$C0        
4F66: CD 91 08   CALL    $0891           
4F69: 36 C0      LD      (HL),$C0        
4F6B: C9         RET                     
4F6C: 35         DEC     (HL)            
4F6D: 35         DEC     (HL)            
4F6E: C9         RET                     
4F6F: 21 FE 4F   LD      HL,$4FFE        
4F72: 0E 03      LD      C,$03           
4F74: CD 26 3D   CALL    $3D26           
4F77: CD 40 50   CALL    $5040           
4F7A: CD 91 08   CALL    $0891           
4F7D: C0         RET     NZ              
4F7E: CD AF 3D   CALL    $3DAF           
4F81: 3E E5      LD      A,$E5           
4F83: CD EE 4F   CALL    $4FEE           
4F86: CD 8D 3B   CALL    $3B8D           
4F89: FA 01 D2   LD      A,($D201)       
4F8C: 5F         LD      E,A             
4F8D: 50         LD      D,B             
4F8E: 21 F9 4E   LD      HL,$4EF9        
4F91: 19         ADD     HL,DE           
4F92: 7E         LD      A,(HL)          
4F93: 21 76 DB   LD      HL,$DB76        
4F96: 19         ADD     HL,DE           
4F97: 77         LD      (HL),A          
4F98: 57         LD      D,A             
4F99: 7B         LD      A,E             
4F9A: A7         AND     A               
4F9B: 20 12      JR      NZ,$4FAF        
4F9D: 21 4C DB   LD      HL,$DB4C        
4FA0: 72         LD      (HL),D          
4FA1: 16 0C      LD      D,$0C           
4FA3: CD 95 3E   CALL    $3E95           
4FA6: AF         XOR     A               
4FA7: EA 4B DB   LD      ($DB4B),A       
4FAA: 3E 0B      LD      A,$0B           
4FAC: E0 A5      LDFF00  ($A5),A         
4FAE: C9         RET                     
4FAF: FE 01      CP      $01             
4FB1: 20 05      JR      NZ,$4FB8        
4FB3: 21 4D DB   LD      HL,$DB4D        
4FB6: 72         LD      (HL),D          
4FB7: C9         RET                     
4FB8: 21 45 DB   LD      HL,$DB45        
4FBB: 72         LD      (HL),D          
4FBC: C9         RET                     
4FBD: CD 16 50   CALL    $5016           
4FC0: FA 9F C1   LD      A,($C19F)       
4FC3: A7         AND     A               
4FC4: 20 27      JR      NZ,$4FED        
4FC6: 21 40 C4   LD      HL,$C440        
4FC9: 09         ADD     HL,BC           
4FCA: 7E         LD      A,(HL)          
4FCB: A7         AND     A               
4FCC: 20 05      JR      NZ,$4FD3        
4FCE: 34         INC     (HL)            
4FCF: 3E 3B      LD      A,$3B           
4FD1: E0 F2      LDFF00  ($F2),A         
4FD3: CD D0 7D   CALL    $7DD0           
4FD6: 21 50 C2   LD      HL,$C250        
4FD9: 09         ADD     HL,BC           
4FDA: 35         DEC     (HL)            
4FDB: 35         DEC     (HL)            
4FDC: 35         DEC     (HL)            
4FDD: F0 EC      LD      A,($EC)         
4FDF: FE F0      CP      $F0             
4FE1: 38 0A      JR      C,$4FED         
4FE3: CD 2B 7F   CALL    $7F2B           
4FE6: AF         XOR     A               
4FE7: EA 67 C1   LD      ($C167),A       
4FEA: CD 76 7E   CALL    $7E76           
4FED: C9         RET                     
4FEE: 5F         LD      E,A             
4FEF: F0 99      LD      A,($99)         
4FF1: F5         PUSH    AF              
4FF2: 3E 20      LD      A,$20           
4FF4: E0 99      LDFF00  ($99),A         
4FF6: 7B         LD      A,E             
4FF7: CD 97 21   CALL    $2197           
4FFA: F1         POP     AF              
4FFB: E0 99      LDFF00  ($99),A         
4FFD: C9         RET                     
4FFE: 00         NOP                     
4FFF: FC         ???                     
5000: 70         LD      (HL),B          
5001: 00         NOP                     
5002: 00         NOP                     
5003: 04         INC     B               
5004: 72         LD      (HL),D          
5005: 00         NOP                     
5006: 00         NOP                     
5007: 0C         INC     C               
5008: 70         LD      (HL),B          
5009: 20 00      JR      NZ,$500B        
500B: FC         ???                     
500C: 74         LD      (HL),H          
500D: 00         NOP                     
500E: 00         NOP                     
500F: 04         INC     B               
5010: 76         HALT                    
5011: 00         NOP                     
5012: 00         NOP                     
5013: 0C         INC     C               
5014: 74         LD      (HL),H          
5015: 20 21      JR      NZ,$5038        
5017: FE 4F      CP      $4F             
5019: F0 E7      LD      A,($E7)         
501B: E6 08      AND     $08             
501D: 28 03      JR      Z,$5022         
501F: 21 0A 50   LD      HL,$500A        
5022: 0E 03      LD      C,$03           
5024: CD 26 3D   CALL    $3D26           
5027: 18 17      JR      $5040           
5029: 7E         LD      A,(HL)          
502A: 00         NOP                     
502B: 7E         LD      A,(HL)          
502C: 20 7E      JR      NZ,$50AC        
502E: 40         LD      B,B             
502F: 7E         LD      A,(HL)          
5030: 60         LD      H,B             
5031: F0 E7      LD      A,($E7)         
5033: 1F         RRA                     
5034: 1F         RRA                     
5035: 1F         RRA                     
5036: E6 01      AND     $01             
5038: E0 F1      LDFF00  ($F1),A         
503A: 11 29 50   LD      DE,$5029        
503D: CD 3B 3C   CALL    $3C3B           
5040: 3E 02      LD      A,$02           
5042: E0 A1      LDFF00  ($A1),A         
5044: EA 67 C1   LD      ($C167),A       
5047: 3E 04      LD      A,$04           
5049: E0 9D      LDFF00  ($9D),A         
504B: AF         XOR     A               
504C: EA 9B C1   LD      ($C19B),A       
504F: C9         RET                     
5050: CD C9 50   CALL    $50C9           
5053: CD 91 08   CALL    $0891           
5056: CA 76 7E   JP      Z,$7E76         
5059: CB 4F      SET     1,E             
505B: 3E E4      LD      A,$E4           
505D: 28 02      JR      Z,$5061         
505F: 3E 44      LD      A,$44           
5061: EA 97 DB   LD      ($DB97),A       
5064: C9         RET                     
5065: 10 00      STOP    $00             
5067: 7C         LD      A,H             
5068: 00         NOP                     
5069: 10 08      STOP    $08             
506B: 7C         LD      A,H             
506C: 60         LD      H,B             
506D: 20 00      JR      NZ,$506F        
506F: 7C         LD      A,H             
5070: 00         NOP                     
5071: 20 08      JR      NZ,$507B        
5073: 7C         LD      A,H             
5074: 60         LD      H,B             
5075: 30 F8      JR      NC,$506F        
5077: 78         LD      A,B             
5078: 00         NOP                     
5079: 30 00      JR      NC,$507B        
507B: 7A         LD      A,D             
507C: 00         NOP                     
507D: 30 08      JR      NC,$5087        
507F: 7A         LD      A,D             
5080: 20 30      JR      NZ,$50B2        
5082: 10 78      STOP    $78             
5084: 20 40      JR      NZ,$50C6        
5086: F8 78      LDHL    SP,$78          
5088: 40         LD      B,B             
5089: 40         LD      B,B             
508A: 00         NOP                     
508B: 7A         LD      A,D             
508C: 40         LD      B,B             
508D: 40         LD      B,B             
508E: 08 7A 60   LD      ($607A),SP      
5091: 40         LD      B,B             
5092: 10 78      STOP    $78             
5094: 60         LD      H,B             
5095: 10 00      STOP    $00             
5097: 7C         LD      A,H             
5098: 50         LD      D,B             
5099: 10 08      STOP    $08             
509B: 7C         LD      A,H             
509C: 30 20      JR      NC,$50BE        
509E: 00         NOP                     
509F: 7C         LD      A,H             
50A0: 50         LD      D,B             
50A1: 20 08      JR      NZ,$50AB        
50A3: 7C         LD      A,H             
50A4: 30 30      JR      NC,$50D6        
50A6: F8 78      LDHL    SP,$78          
50A8: 10 30      STOP    $30             
50AA: 00         NOP                     
50AB: 7A         LD      A,D             
50AC: 10 30      STOP    $30             
50AE: 08 7A 30   LD      ($307A),SP      
50B1: 30 10      JR      NC,$50C3        
50B3: 78         LD      A,B             
50B4: 30 40      JR      NC,$50F6        
50B6: F8 78      LDHL    SP,$78          
50B8: 50         LD      D,B             
50B9: 40         LD      B,B             
50BA: 00         NOP                     
50BB: 7A         LD      A,D             
50BC: 50         LD      D,B             
50BD: 40         LD      B,B             
50BE: 08 7A 70   LD      ($707A),SP      
50C1: 40         LD      B,B             
50C2: 10 78      STOP    $78             
50C4: 70         LD      (HL),B          
50C5: 0C         INC     C               
50C6: 0C         INC     C               
50C7: 04         INC     B               
50C8: 02         LD      (BC),A          
50C9: F0 EC      LD      A,($EC)         
50CB: D6 05      SUB     $05             
50CD: E0 EC      LDFF00  ($EC),A         
50CF: CD 91 08   CALL    $0891           
50D2: 0E 0C      LD      C,$0C           
50D4: FE B0      CP      $B0             
50D6: 38 0D      JR      C,$50E5         
50D8: D6 B0      SUB     $B0             
50DA: 1F         RRA                     
50DB: 1F         RRA                     
50DC: E6 03      AND     $03             
50DE: 5F         LD      E,A             
50DF: 50         LD      D,B             
50E0: 21 C5 50   LD      HL,$50C5        
50E3: 19         ADD     HL,DE           
50E4: 4E         LD      C,(HL)          
50E5: 21 65 50   LD      HL,$5065        
50E8: F0 E7      LD      A,($E7)         
50EA: E6 04      AND     $04             
50EC: 28 03      JR      Z,$50F1         
50EE: 21 95 50   LD      HL,$5095        
50F1: CD 26 3D   CALL    $3D26           
50F4: 3E 04      LD      A,$04           
50F6: CD D0 3D   CALL    $3DD0           
50F9: C9         RET                     
50FA: 0E 00      LD      C,$00           
50FC: 11 FA 50   LD      DE,$50FA        
50FF: CD D0 3C   CALL    $3CD0           
5102: 21 D0 C3   LD      HL,$C3D0        
5105: 09         ADD     HL,BC           
5106: 7E         LD      A,(HL)          
5107: 3D         DEC     A               
5108: 77         LD      (HL),A          
5109: CA 76 7E   JP      Z,$7E76         
510C: CB 67      SET     1,E             
510E: 1E 01      LD      E,$01           
5110: 28 02      JR      Z,$5114         
5112: 1E FF      LD      E,$FF           
5114: CB 47      SET     1,E             
5116: 20 07      JR      NZ,$511F        
5118: 21 40 C2   LD      HL,$C240        
511B: 09         ADD     HL,BC           
511C: 7E         LD      A,(HL)          
511D: 83         ADD     A,E             
511E: 77         LD      (HL),A          
511F: C3 CD 7D   JP      $7DCD           
5122: 50         LD      D,B             
5123: 00         NOP                     
5124: 52         LD      D,D             
5125: 00         NOP                     
5126: 52         LD      D,D             
5127: 20 50      JR      NZ,$5179        
5129: 20 54      JR      NZ,$517F        
512B: 00         NOP                     
512C: 56         LD      D,(HL)          
512D: 00         NOP                     
512E: 56         LD      D,(HL)          
512F: 20 54      JR      NZ,$5185        
5131: 20 CD      JR      NZ,$5100        
5133: 68         LD      L,B             
5134: 51         LD      D,C             
5135: 11 22 51   LD      DE,$5122        
5138: CD 3B 3C   CALL    $3C3B           
513B: FA 0F C5   LD      A,($C50F)       
513E: 5F         LD      E,A             
513F: 50         LD      D,B             
5140: 21 10 C2   LD      HL,$C210        
5143: 19         ADD     HL,DE           
5144: F0 EF      LD      A,($EF)         
5146: 1E 00      LD      E,$00           
5148: BE         CP      (HL)            
5149: 38 02      JR      C,$514D         
514B: 1E 02      LD      E,$02           
514D: F0 E7      LD      A,($E7)         
514F: 1F         RRA                     
5150: 1F         RRA                     
5151: 1F         RRA                     
5152: 1F         RRA                     
5153: 1F         RRA                     
5154: E6 01      AND     $01             
5156: 83         ADD     A,E             
5157: CD 87 3B   CALL    $3B87           
515A: CD AF 7C   CALL    $7CAF           
515D: CD 0E 7D   CALL    $7D0E           
5160: 30 05      JR      NC,$5167        
5162: 3E 96      LD      A,$96           
5164: CD 85 21   CALL    $2185           
5167: C9         RET                     
5168: FA 74 DB   LD      A,($DB74)       
516B: A7         AND     A               
516C: CA 76 7E   JP      Z,$7E76         
516F: C0         RET     NZ              
5170: 74         LD      (HL),H          
5171: 00         NOP                     
5172: 76         HALT                    
5173: 00         NOP                     
5174: 70         LD      (HL),B          
5175: 00         NOP                     
5176: 72         LD      (HL),D          
5177: 00         NOP                     
5178: 76         HALT                    
5179: 20 74      JR      NZ,$51EF        
517B: 20 72      JR      NZ,$51EF        
517D: 20 70      JR      NZ,$51EF        
517F: 20 CD      JR      NZ,$514E        
5181: 68         LD      L,B             
5182: 51         LD      D,C             
5183: 11 70 51   LD      DE,$5170        
5186: CD 3B 3C   CALL    $3C3B           
5189: FA 0F C5   LD      A,($C50F)       
518C: 5F         LD      E,A             
518D: 50         LD      D,B             
518E: 21 00 C2   LD      HL,$C200        
5191: 19         ADD     HL,DE           
5192: F0 EE      LD      A,($EE)         
5194: 1E 00      LD      E,$00           
5196: BE         CP      (HL)            
5197: 30 02      JR      NC,$519B        
5199: 1E 02      LD      E,$02           
519B: F0 E7      LD      A,($E7)         
519D: 1F         RRA                     
519E: 1F         RRA                     
519F: 1F         RRA                     
51A0: 1F         RRA                     
51A1: 1F         RRA                     
51A2: E6 01      AND     $01             
51A4: 83         ADD     A,E             
51A5: CD 87 3B   CALL    $3B87           
51A8: 18 B0      JR      $515A           
51AA: 50         LD      D,B             
51AB: 00         NOP                     
51AC: 52         LD      D,D             
51AD: 00         NOP                     
51AE: 52         LD      D,D             
51AF: 20 50      JR      NZ,$5201        
51B1: 20 54      JR      NZ,$5207        
51B3: 00         NOP                     
51B4: 56         LD      D,(HL)          
51B5: 00         NOP                     
51B6: 56         LD      D,(HL)          
51B7: 20 54      JR      NZ,$520D        
51B9: 20 58      JR      NZ,$5213        
51BB: 00         NOP                     
51BC: 5A         LD      E,D             
51BD: 00         NOP                     
51BE: 58         LD      E,B             
51BF: 00         NOP                     
51C0: 5A         LD      E,D             
51C1: 00         NOP                     
51C2: 5A         LD      E,D             
51C3: 20 58      JR      NZ,$521D        
51C5: 20 5A      JR      NZ,$5221        
51C7: 20 58      JR      NZ,$5221        
51C9: 20 FA      JR      NZ,$51C5        
51CB: 74         LD      (HL),H          
51CC: DB         ???                     
51CD: A7         AND     A               
51CE: C2 76 7E   JP      NZ,$7E76        
51D1: 11 AA 51   LD      DE,$51AA        
51D4: CD 3B 3C   CALL    $3C3B           
51D7: F0 E7      LD      A,($E7)         
51D9: E6 3F      AND     $3F             
51DB: 20 08      JR      NZ,$51E5        
51DD: CD 4F 7E   CALL    $7E4F           
51E0: 21 80 C3   LD      HL,$C380        
51E3: 09         ADD     HL,BC           
51E4: 73         LD      (HL),E          
51E5: CD D9 7C   CALL    $7CD9           
51E8: CD 61 7D   CALL    $7D61           
51EB: CD 06 7E   CALL    $7E06           
51EE: 21 20 C3   LD      HL,$C320        
51F1: 09         ADD     HL,BC           
51F2: 35         DEC     (HL)            
51F3: 35         DEC     (HL)            
51F4: 21 10 C3   LD      HL,$C310        
51F7: 09         ADD     HL,BC           
51F8: 7E         LD      A,(HL)          
51F9: A7         AND     A               
51FA: 28 04      JR      Z,$5200         
51FC: E6 80      AND     $80             
51FE: 28 0E      JR      Z,$520E         
5200: 70         LD      (HL),B          
5201: 21 20 C3   LD      HL,$C320        
5204: 09         ADD     HL,BC           
5205: 70         LD      (HL),B          
5206: F0 E7      LD      A,($E7)         
5208: E6 1F      AND     $1F             
520A: 20 02      JR      NZ,$520E        
520C: 36 0C      LD      (HL),$0C        
520E: F0 EF      LD      A,($EF)         
5210: E0 EC      LDFF00  ($EC),A         
5212: CD AF 7C   CALL    $7CAF           
5215: CD BA 3D   CALL    $3DBA           
5218: CD 0E 7D   CALL    $7D0E           
521B: D0         RET     NC              
521C: 1E 00      LD      E,$00           
521E: FA A5 DB   LD      A,($DBA5)       
5221: A7         AND     A               
5222: 20 0D      JR      NZ,$5231        
5224: 1C         INC     E               
5225: F0 F6      LD      A,($F6)         
5227: FE CC      CP      $CC             
5229: 28 06      JR      Z,$5231         
522B: 1C         INC     E               
522C: FE CD      CP      $CD             
522E: 28 01      JR      Z,$5231         
5230: 1C         INC     E               
5231: FA 6A DB   LD      A,($DB6A)       
5234: E6 02      AND     $02             
5236: 28 04      JR      Z,$523C         
5238: 7B         LD      A,E             
5239: C6 04      ADD     $04             
523B: 5F         LD      E,A             
523C: FA 73 DB   LD      A,($DB73)       
523F: A7         AND     A               
5240: 28 05      JR      Z,$5247         
5242: 3E 52      LD      A,$52           
5244: C3 8E 21   JP      $218E           
5247: 7B         LD      A,E             
5248: C6 4A      ADD     $4A             
524A: C3 8E 21   JP      $218E           
524D: 78         LD      A,B             
524E: 00         NOP                     
524F: 7A         LD      A,D             
5250: 00         NOP                     
5251: 7C         LD      A,H             
5252: 00         NOP                     
5253: 7E         LD      A,(HL)          
5254: 00         NOP                     
5255: 7A         LD      A,D             
5256: 20 78      JR      NZ,$52D0        
5258: 20 7E      JR      NZ,$52D8        
525A: 20 7C      JR      NZ,$52D8        
525C: 20 CD      JR      NZ,$522B        
525E: 68         LD      L,B             
525F: 51         LD      D,C             
5260: 11 4D 52   LD      DE,$524D        
5263: CD 3B 3C   CALL    $3C3B           
5266: FA 0F C5   LD      A,($C50F)       
5269: 5F         LD      E,A             
526A: 50         LD      D,B             
526B: 21 00 C2   LD      HL,$C200        
526E: 19         ADD     HL,DE           
526F: F0 EE      LD      A,($EE)         
5271: 1E 00      LD      E,$00           
5273: BE         CP      (HL)            
5274: 30 02      JR      NC,$5278        
5276: 1E 02      LD      E,$02           
5278: F0 E7      LD      A,($E7)         
527A: 1F         RRA                     
527B: 1F         RRA                     
527C: 1F         RRA                     
527D: 1F         RRA                     
527E: 1F         RRA                     
527F: E6 01      AND     $01             
5281: 83         ADD     A,E             
5282: CD 87 3B   CALL    $3B87           
5285: C3 5A 51   JP      $515A           
5288: 5A         LD      E,D             
5289: 20 58      JR      NZ,$52E3        
528B: 20 5E      JR      NZ,$52EB        
528D: 20 5C      JR      NZ,$52EB        
528F: 20 58      JR      NZ,$52E9        
5291: 00         NOP                     
5292: 5A         LD      E,D             
5293: 00         NOP                     
5294: 5C         LD      E,H             
5295: 00         NOP                     
5296: 5E         LD      E,(HL)          
5297: 00         NOP                     
5298: 11 88 52   LD      DE,$5288        
529B: CD 3B 3C   CALL    $3C3B           
529E: F0 E7      LD      A,($E7)         
52A0: 1F         RRA                     
52A1: 1F         RRA                     
52A2: 1F         RRA                     
52A3: E6 01      AND     $01             
52A5: CD 87 3B   CALL    $3B87           
52A8: 3E 02      LD      A,$02           
52AA: E0 A1      LDFF00  ($A1),A         
52AC: EA 67 C1   LD      ($C167),A       
52AF: CD 06 7E   CALL    $7E06           
52B2: 21 20 C3   LD      HL,$C320        
52B5: 09         ADD     HL,BC           
52B6: 35         DEC     (HL)            
52B7: 35         DEC     (HL)            
52B8: 21 10 C3   LD      HL,$C310        
52BB: 09         ADD     HL,BC           
52BC: 7E         LD      A,(HL)          
52BD: E6 80      AND     $80             
52BF: E0 E8      LDFF00  ($E8),A         
52C1: 28 06      JR      Z,$52C9         
52C3: 70         LD      (HL),B          
52C4: 21 20 C3   LD      HL,$C320        
52C7: 09         ADD     HL,BC           
52C8: 70         LD      (HL),B          
52C9: F0 F0      LD      A,($F0)         
52CB: C7         RST     0X00            
52CC: D4 52 01   CALL    NC,$0152        
52CF: 53         LD      D,E             
52D0: 2A         LD      A,(HLI)         
52D1: 53         LD      D,E             
52D2: 4F         LD      C,A             
52D3: 53         LD      D,E             
52D4: CD 91 08   CALL    $0891           
52D7: C0         RET     NZ              
52D8: 21 40 C2   LD      HL,$C240        
52DB: 09         ADD     HL,BC           
52DC: 36 0C      LD      (HL),$0C        
52DE: CD DA 7D   CALL    $7DDA           
52E1: F0 EE      LD      A,($EE)         
52E3: FE 20      CP      $20             
52E5: 20 0F      JR      NZ,$52F6        
52E7: 3E 01      LD      A,$01           
52E9: CD BA 59   CALL    $59BA           
52EC: 3E 01      LD      A,$01           
52EE: E0 9E      LDFF00  ($9E),A         
52F0: C5         PUSH    BC              
52F1: CD 7C 08   CALL    $087C           
52F4: C1         POP     BC              
52F5: C9         RET                     
52F6: FE 48      CP      $48             
52F8: C0         RET     NZ              
52F9: CD 91 08   CALL    $0891           
52FC: 36 40      LD      (HL),$40        
52FE: C3 8D 3B   JP      $3B8D           
5301: CD 91 08   CALL    $0891           
5304: 20 0D      JR      NZ,$5313        
5306: 3E E3      LD      A,$E3           
5308: CD 85 21   CALL    $2185           
530B: CD 91 08   CALL    $0891           
530E: 36 10      LD      (HL),$10        
5310: CD 8D 3B   CALL    $3B8D           
5313: F0 E8      LD      A,($E8)         
5315: A7         AND     A               
5316: 28 11      JR      Z,$5329         
5318: 21 40 C4   LD      HL,$C440        
531B: 09         ADD     HL,BC           
531C: 7E         LD      A,(HL)          
531D: 35         DEC     (HL)            
531E: A7         AND     A               
531F: 20 08      JR      NZ,$5329        
5321: 36 08      LD      (HL),$08        
5323: 21 20 C3   LD      HL,$C320        
5326: 09         ADD     HL,BC           
5327: 36 12      LD      (HL),$12        
5329: C9         RET                     
532A: CD 13 53   CALL    $5313           
532D: FA 9F C1   LD      A,($C19F)       
5330: A7         AND     A               
5331: 20 1B      JR      NZ,$534E        
5333: CD 91 08   CALL    $0891           
5336: 20 0A      JR      NZ,$5342        
5338: 36 10      LD      (HL),$10        
533A: 3E E5      LD      A,$E5           
533C: CD 85 21   CALL    $2185           
533F: C3 8D 3B   JP      $3B8D           
5342: 1E 02      LD      E,$02           
5344: FE 08      CP      $08             
5346: 30 02      JR      NC,$534A        
5348: 1E 00      LD      E,$00           
534A: 7B         LD      A,E             
534B: CD BA 59   CALL    $59BA           
534E: C9         RET                     
534F: CD 13 53   CALL    $5313           
5352: FA 9F C1   LD      A,($C19F)       
5355: A7         AND     A               
5356: 20 69      JR      NZ,$53C1        
5358: CD 91 08   CALL    $0891           
535B: 28 0C      JR      Z,$5369         
535D: 1E 01      LD      E,$01           
535F: FE 08      CP      $08             
5361: 38 02      JR      C,$5365         
5363: 1E 02      LD      E,$02           
5365: 7B         LD      A,E             
5366: C3 BA 59   JP      $59BA           
5369: F0 E7      LD      A,($E7)         
536B: 1F         RRA                     
536C: 1F         RRA                     
536D: 1F         RRA                     
536E: E6 01      AND     $01             
5370: C6 02      ADD     $02             
5372: CD 87 3B   CALL    $3B87           
5375: 21 74 DB   LD      HL,$DB74        
5378: 36 01      LD      (HL),$01        
537A: F0 EE      LD      A,($EE)         
537C: E6 FC      AND     $FC             
537E: FE E0      CP      $E0             
5380: 28 09      JR      Z,$538B         
5382: 21 40 C2   LD      HL,$C240        
5385: 09         ADD     HL,BC           
5386: 36 EC      LD      (HL),$EC        
5388: CD DA 7D   CALL    $7DDA           
538B: FA 0F C5   LD      A,($C50F)       
538E: 5F         LD      E,A             
538F: 50         LD      D,B             
5390: 21 40 C2   LD      HL,$C240        
5393: 19         ADD     HL,DE           
5394: 36 F4      LD      (HL),$F4        
5396: F0 E7      LD      A,($E7)         
5398: 1F         RRA                     
5399: 1F         RRA                     
539A: 1F         RRA                     
539B: E6 01      AND     $01             
539D: C6 04      ADD     $04             
539F: 21 B0 C3   LD      HL,$C3B0        
53A2: 19         ADD     HL,DE           
53A3: 77         LD      (HL),A          
53A4: D5         PUSH    DE              
53A5: C5         PUSH    BC              
53A6: D5         PUSH    DE              
53A7: C1         POP     BC              
53A8: CD DA 7D   CALL    $7DDA           
53AB: C1         POP     BC              
53AC: D1         POP     DE              
53AD: 21 00 C2   LD      HL,$C200        
53B0: 19         ADD     HL,DE           
53B1: 7E         LD      A,(HL)          
53B2: FE F0      CP      $F0             
53B4: 20 0B      JR      NZ,$53C1        
53B6: CD 76 7E   CALL    $7E76           
53B9: AF         XOR     A               
53BA: EA 73 DB   LD      ($DB73),A       
53BD: AF         XOR     A               
53BE: EA 67 C1   LD      ($C167),A       
53C1: C9         RET                     
53C2: CD 7E 54   CALL    $547E           
53C5: CD 61 7D   CALL    $7D61           
53C8: 21 98 FF   LD      HL,$FF98        
53CB: F0 EE      LD      A,($EE)         
53CD: 96         SUB     (HL)            
53CE: C6 04      ADD     $04             
53D0: FE 08      CP      $08             
53D2: 30 0D      JR      NC,$53E1        
53D4: 21 99 FF   LD      HL,$FF99        
53D7: F0 EC      LD      A,($EC)         
53D9: C6 04      ADD     $04             
53DB: 96         SUB     (HL)            
53DC: 38 03      JR      C,$53E1         
53DE: CD B4 7C   CALL    $7CB4           
53E1: 21 98 FF   LD      HL,$FF98        
53E4: F0 EE      LD      A,($EE)         
53E6: 96         SUB     (HL)            
53E7: C6 06      ADD     $06             
53E9: FE 0C      CP      $0C             
53EB: 30 6D      JR      NC,$545A        
53ED: 21 99 FF   LD      HL,$FF99        
53F0: F0 EC      LD      A,($EC)         
53F2: 96         SUB     (HL)            
53F3: C6 08      ADD     $08             
53F5: FE 04      CP      $04             
53F7: 30 61      JR      NC,$545A        
53F9: 1E 20      LD      E,$20           
53FB: FA 00 DB   LD      A,($DB00)       
53FE: FE 03      CP      $03             
5400: 28 09      JR      Z,$540B         
5402: 1E 10      LD      E,$10           
5404: FA 01 DB   LD      A,($DB01)       
5407: FE 03      CP      $03             
5409: 20 4F      JR      NZ,$545A        
540B: F0 CB      LD      A,($CB)         
540D: A3         AND     E               
540E: 28 4A      JR      Z,$545A         
5410: 3E 02      LD      A,$02           
5412: E0 BA      LDFF00  ($BA),A         
5414: 3E 3A      LD      A,$3A           
5416: E0 9D      LDFF00  ($9D),A         
5418: 3E 02      LD      A,$02           
541A: E0 9E      LDFF00  ($9E),A         
541C: 3E 01      LD      A,$01           
541E: E0 A1      LDFF00  ($A1),A         
5420: CD 3B 09   CALL    $093B           
5423: F0 EE      LD      A,($EE)         
5425: E0 98      LDFF00  ($98),A         
5427: F0 EC      LD      A,($EC)         
5429: C6 08      ADD     $08             
542B: E0 99      LDFF00  ($99),A         
542D: FE 50      CP      $50             
542F: 30 22      JR      NC,$5453        
5431: F0 CB      LD      A,($CB)         
5433: E6 08      AND     $08             
5435: 28 1C      JR      Z,$5453         
5437: 21 D0 C3   LD      HL,$C3D0        
543A: 09         ADD     HL,BC           
543B: 7E         LD      A,(HL)          
543C: 34         INC     (HL)            
543D: E6 18      AND     $18             
543F: 28 11      JR      Z,$5452         
5441: 21 9D FF   LD      HL,$FF9D        
5444: 34         INC     (HL)            
5445: 21 50 C2   LD      HL,$C250        
5448: 09         ADD     HL,BC           
5449: 36 04      LD      (HL),$04        
544B: CD D0 7D   CALL    $7DD0           
544E: 3E 01      LD      A,$01           
5450: E0 BA      LDFF00  ($BA),A         
5452: C9         RET                     
5453: 21 D0 C3   LD      HL,$C3D0        
5456: 09         ADD     HL,BC           
5457: 36 08      LD      (HL),$08        
5459: C9         RET                     
545A: F0 EC      LD      A,($EC)         
545C: FE 1B      CP      $1B             
545E: 38 0D      JR      C,$546D         
5460: 21 50 C2   LD      HL,$C250        
5463: 09         ADD     HL,BC           
5464: 36 FD      LD      (HL),$FD        
5466: CD D0 7D   CALL    $7DD0           
5469: 3E 00      LD      A,$00           
546B: E0 BA      LDFF00  ($BA),A         
546D: C9         RET                     
546E: 44         LD      B,H             
546F: 00         NOP                     
5470: 44         LD      B,H             
5471: 20 74      JR      NZ,$54E7        
5473: 00         NOP                     
5474: 74         LD      (HL),H          
5475: 20 46      JR      NZ,$54BD        
5477: 00         NOP                     
5478: 46         LD      B,(HL)          
5479: 20 76      JR      NZ,$54F1        
547B: 00         NOP                     
547C: 76         HALT                    
547D: 20 F0      JR      NZ,$546F        
547F: F7         RST     0X30            
5480: FE 01      CP      $01             
5482: 20 02      JR      NZ,$5486        
5484: E0 F1      LDFF00  ($F1),A         
5486: 11 6E 54   LD      DE,$546E        
5489: CD 3B 3C   CALL    $3C3B           
548C: 21 C0 C2   LD      HL,$C2C0        
548F: 09         ADD     HL,BC           
5490: 7E         LD      A,(HL)          
5491: C6 FC      ADD     $FC             
5493: FE F0      CP      $F0             
5495: D0         RET     NC              
5496: E0 EC      LDFF00  ($EC),A         
5498: 11 76 54   LD      DE,$5476        
549B: CD 3B 3C   CALL    $3C3B           
549E: F0 EC      LD      A,($EC)         
54A0: C6 10      ADD     $10             
54A2: E0 EC      LDFF00  ($EC),A         
54A4: 21 EF FF   LD      HL,$FFEF        
54A7: BE         CP      (HL)            
54A8: 38 EE      JR      C,$5498         
54AA: CD BA 3D   CALL    $3DBA           
54AD: C9         RET                     
54AE: 24         INC     H               
54AF: 00         NOP                     
54B0: 3E 00      LD      A,$00           
54B2: 11 AE 54   LD      DE,$54AE        
54B5: CD D0 3C   CALL    $3CD0           
54B8: CD 61 7D   CALL    $7D61           
54BB: CD 91 08   CALL    $0891           
54BE: CA 76 7E   JP      Z,$7E76         
54C1: 1E 01      LD      E,$01           
54C3: FE 40      CP      $40             
54C5: 38 0D      JR      C,$54D4         
54C7: 20 0A      JR      NZ,$54D3        
54C9: 21 10 C2   LD      HL,$C210        
54CC: 09         ADD     HL,BC           
54CD: 7E         LD      A,(HL)          
54CE: C6 04      ADD     $04             
54D0: 77         LD      (HL),A          
54D1: 18 01      JR      $54D4           
54D3: 1D         DEC     E               
54D4: 7B         LD      A,E             
54D5: CD 87 3B   CALL    $3B87           
54D8: CD 91 08   CALL    $0891           
54DB: 1E FE      LD      E,$FE           
54DD: E6 20      AND     $20             
54DF: 28 02      JR      Z,$54E3         
54E1: 1E FC      LD      E,$FC           
54E3: 21 50 C2   LD      HL,$C250        
54E6: 09         ADD     HL,BC           
54E7: 73         LD      (HL),E          
54E8: 21 40 C2   LD      HL,$C240        
54EB: 09         ADD     HL,BC           
54EC: 36 FF      LD      (HL),$FF        
54EE: F0 E7      LD      A,($E7)         
54F0: E6 03      AND     $03             
54F2: C0         RET     NZ              
54F3: CD CD 7D   CALL    $7DCD           
54F6: C9         RET                     
54F7: 21 B0 C2   LD      HL,$C2B0        
54FA: 09         ADD     HL,BC           
54FB: 7E         LD      A,(HL)          
54FC: A7         AND     A               
54FD: C2 B2 54   JP      NZ,$54B2        
5500: FA FD D8   LD      A,($D8FD)       
5503: E6 20      AND     $20             
5505: C2 A0 58   JP      NZ,$58A0        
5508: CD 70 58   CALL    $5870           
550B: CD 61 7D   CALL    $7D61           
550E: CD 06 7E   CALL    $7E06           
5511: 21 20 C3   LD      HL,$C320        
5514: 09         ADD     HL,BC           
5515: 35         DEC     (HL)            
5516: 21 10 C3   LD      HL,$C310        
5519: 09         ADD     HL,BC           
551A: 7E         LD      A,(HL)          
551B: E6 80      AND     $80             
551D: 28 06      JR      Z,$5525         
551F: 70         LD      (HL),B          
5520: 21 20 C3   LD      HL,$C320        
5523: 09         ADD     HL,BC           
5524: 70         LD      (HL),B          
5525: CD AF 7C   CALL    $7CAF           
5528: F0 F0      LD      A,($F0)         
552A: C7         RST     0X00            
552B: 3D         DEC     A               
552C: 55         LD      D,L             
552D: B5         OR      L               
552E: 55         LD      D,L             
552F: DA 55 73   JP      C,$7355         
5532: 56         LD      D,(HL)          
5533: E9         JP      (HL)            
5534: 56         LD      D,(HL)          
5535: 1D         DEC     E               
5536: 57         LD      D,A             
5537: 56         LD      D,(HL)          
5538: 57         LD      D,A             
5539: 81         ADD     A,C             
553A: 57         LD      D,A             
553B: 9F         SBC     A               
553C: 57         LD      D,A             
553D: 21 D0 C3   LD      HL,$C3D0        
5540: 09         ADD     HL,BC           
5541: 34         INC     (HL)            
5542: 3E 7F      LD      A,$7F           
5544: A6         AND     (HL)            
5545: 20 2A      JR      NZ,$5571        
5547: 3E C4      LD      A,$C4           
5549: CD 01 3C   CALL    $3C01           
554C: 38 23      JR      C,$5571         
554E: F0 D7      LD      A,($D7)         
5550: D6 08      SUB     $08             
5552: 21 00 C2   LD      HL,$C200        
5555: 19         ADD     HL,DE           
5556: 77         LD      (HL),A          
5557: F0 D8      LD      A,($D8)         
5559: C6 02      ADD     $02             
555B: 21 10 C2   LD      HL,$C210        
555E: 19         ADD     HL,DE           
555F: 77         LD      (HL),A          
5560: 21 E0 C2   LD      HL,$C2E0        
5563: 19         ADD     HL,DE           
5564: 36 60      LD      (HL),$60        
5566: 21 40 C3   LD      HL,$C340        
5569: 19         ADD     HL,DE           
556A: 36 C1      LD      (HL),$C1        
556C: 21 B0 C2   LD      HL,$C2B0        
556F: 19         ADD     HL,DE           
5570: 34         INC     (HL)            
5571: FA 73 DB   LD      A,($DB73)       
5574: A7         AND     A               
5575: 20 0B      JR      NZ,$5582        
5577: CD F5 7C   CALL    $7CF5           
557A: 30 05      JR      NC,$5581        
557C: 3E E0      LD      A,$E0           
557E: CD 85 21   CALL    $2185           
5581: C9         RET                     
5582: CD 20 7E   CALL    $7E20           
5585: C6 13      ADD     $13             
5587: FE 26      CP      $26             
5589: D0         RET     NC              
558A: CD 30 7E   CALL    $7E30           
558D: C6 20      ADD     $20             
558F: FE 40      CP      $40             
5591: D0         RET     NC              
5592: CD 3B 09   CALL    $093B           
5595: CD 95 14   CALL    $1495           
5598: FA 46 C1   LD      A,($C146)       
559B: A7         AND     A               
559C: C0         RET     NZ              
559D: FA 0F C5   LD      A,($C50F)       
55A0: 5F         LD      E,A             
55A1: 50         LD      D,B             
55A2: 21 10 C3   LD      HL,$C310        
55A5: 19         ADD     HL,DE           
55A6: 7E         LD      A,(HL)          
55A7: A7         AND     A               
55A8: C0         RET     NZ              
55A9: CD 8D 3B   CALL    $3B8D           
55AC: 3E E1      LD      A,$E1           
55AE: CD 85 21   CALL    $2185           
55B1: CD B8 59   CALL    $59B8           
55B4: C9         RET                     
55B5: FA 9F C1   LD      A,($C19F)       
55B8: A7         AND     A               
55B9: 20 1E      JR      NZ,$55D9        
55BB: CD 8D 3B   CALL    $3B8D           
55BE: FA 77 C1   LD      A,($C177)       
55C1: A7         AND     A               
55C2: 20 0E      JR      NZ,$55D2        
55C4: 3E 2F      LD      A,$2F           
55C6: EA 68 D3   LD      ($D368),A       
55C9: EA C8 C3   LD      ($C3C8),A       
55CC: CD 87 08   CALL    $0887           
55CF: 36 50      LD      (HL),$50        
55D1: C9         RET                     
55D2: 36 08      LD      (HL),$08        
55D4: 3E E4      LD      A,$E4           
55D6: CD 85 21   CALL    $2185           
55D9: C9         RET                     
55DA: 3E 01      LD      A,$01           
55DC: EA 67 C1   LD      ($C167),A       
55DF: 3E 02      LD      A,$02           
55E1: E0 A1      LDFF00  ($A1),A         
55E3: CD 87 08   CALL    $0887           
55E6: 20 06      JR      NZ,$55EE        
55E8: 36 C0      LD      (HL),$C0        
55EA: CD 8D 3B   CALL    $3B8D           
55ED: C9         RET                     
55EE: 1E 00      LD      E,$00           
55F0: FE 40      CP      $40             
55F2: 30 1A      JR      NC,$560E        
55F4: 1E 02      LD      E,$02           
55F6: FE 10      CP      $10             
55F8: 38 14      JR      C,$560E         
55FA: 1E 00      LD      E,$00           
55FC: FE 3C      CP      $3C             
55FE: 30 0C      JR      NC,$560C        
5600: FE 20      CP      $20             
5602: 28 0A      JR      Z,$560E         
5604: FE 21      CP      $21             
5606: 28 06      JR      Z,$560E         
5608: FE 22      CP      $22             
560A: 28 02      JR      Z,$560E         
560C: 1E 01      LD      E,$01           
560E: 7B         LD      A,E             
560F: CD 87 3B   CALL    $3B87           
5612: C9         RET                     
5613: 01 02 01   LD      BC,$0102        
5616: 02         LD      (BC),A          
5617: 01 01 02   LD      BC,$0201        
561A: 02         LD      (BC),A          
561B: 01 02 01   LD      BC,$0102        
561E: 02         LD      (BC),A          
561F: 01 01 02   LD      BC,$0201        
5622: 02         LD      (BC),A          
5623: 01 02 01   LD      BC,$0102        
5626: 02         LD      (BC),A          
5627: 01 01 02   LD      BC,$0201        
562A: 02         LD      (BC),A          
562B: 01 02 01   LD      BC,$0102        
562E: 02         LD      (BC),A          
562F: 01 01 02   LD      BC,$0201        
5632: 02         LD      (BC),A          
5633: 01 02 01   LD      BC,$0102        
5636: 02         LD      (BC),A          
5637: 01 01 02   LD      BC,$0201        
563A: 02         LD      (BC),A          
563B: 01 02 01   LD      BC,$0102        
563E: 02         LD      (BC),A          
563F: 01 01 02   LD      BC,$0201        
5642: 02         LD      (BC),A          
5643: 01 02 01   LD      BC,$0102        
5646: 02         LD      (BC),A          
5647: 01 01 02   LD      BC,$0201        
564A: 02         LD      (BC),A          
564B: 01 02 01   LD      BC,$0102        
564E: 02         LD      (BC),A          
564F: 01 01 02   LD      BC,$0201        
5652: 02         LD      (BC),A          
5653: 01 02 01   LD      BC,$0102        
5656: 02         LD      (BC),A          
5657: 01 01 02   LD      BC,$0201        
565A: 02         LD      (BC),A          
565B: 01 02 01   LD      BC,$0102        
565E: 02         LD      (BC),A          
565F: 01 01 02   LD      BC,$0201        
5662: 02         LD      (BC),A          
5663: 01 02 01   LD      BC,$0102        
5666: 02         LD      (BC),A          
5667: 01 01 02   LD      BC,$0201        
566A: 02         LD      (BC),A          
566B: 01 02 01   LD      BC,$0102        
566E: 02         LD      (BC),A          
566F: 01 01 02   LD      BC,$0201        
5672: 02         LD      (BC),A          
5673: 3E 01      LD      A,$01           
5675: EA 67 C1   LD      ($C167),A       
5678: 3E 02      LD      A,$02           
567A: E0 A1      LDFF00  ($A1),A         
567C: CD 87 08   CALL    $0887           
567F: 20 14      JR      NZ,$5695        
5681: EA C8 C3   LD      ($C3C8),A       
5684: 3E 11      LD      A,$11           
5686: E0 F4      LDFF00  ($F4),A         
5688: CD 91 08   CALL    $0891           
568B: 36 08      LD      (HL),$08        
568D: 3E 02      LD      A,$02           
568F: CD 87 3B   CALL    $3B87           
5692: C3 8D 3B   JP      $3B8D           
5695: 21 D0 C2   LD      HL,$C2D0        
5698: 09         ADD     HL,BC           
5699: 5E         LD      E,(HL)          
569A: 50         LD      D,B             
569B: F0 E7      LD      A,($E7)         
569D: E6 07      AND     $07             
569F: 20 14      JR      NZ,$56B5        
56A1: 34         INC     (HL)            
56A2: 7E         LD      A,(HL)          
56A3: FE 60      CP      $60             
56A5: 30 0E      JR      NC,$56B5        
56A7: E6 0F      AND     $0F             
56A9: 20 0A      JR      NZ,$56B5        
56AB: 21 20 C3   LD      HL,$C320        
56AE: 09         ADD     HL,BC           
56AF: 36 10      LD      (HL),$10        
56B1: 3E 24      LD      A,$24           
56B3: E0 F2      LDFF00  ($F2),A         
56B5: 21 13 56   LD      HL,$5613        
56B8: 19         ADD     HL,DE           
56B9: 7E         LD      A,(HL)          
56BA: FE 02      CP      $02             
56BC: 20 0D      JR      NZ,$56CB        
56BE: F0 E7      LD      A,($E7)         
56C0: E6 3F      AND     $3F             
56C2: 20 05      JR      NZ,$56C9        
56C4: 21 F2 FF   LD      HL,$FFF2        
56C7: 36 27      LD      (HL),$27        
56C9: 3E 02      LD      A,$02           
56CB: CD 87 3B   CALL    $3B87           
56CE: 21 10 C3   LD      HL,$C310        
56D1: 09         ADD     HL,BC           
56D2: 7E         LD      A,(HL)          
56D3: A7         AND     A               
56D4: 28 12      JR      Z,$56E8         
56D6: 1E 01      LD      E,$01           
56D8: 21 20 C3   LD      HL,$C320        
56DB: 09         ADD     HL,BC           
56DC: 7E         LD      A,(HL)          
56DD: D6 F8      SUB     $F8             
56DF: E6 80      AND     $80             
56E1: 20 01      JR      NZ,$56E4        
56E3: 1C         INC     E               
56E4: 7B         LD      A,E             
56E5: CD 87 3B   CALL    $3B87           
56E8: C9         RET                     
56E9: 3E 02      LD      A,$02           
56EB: E0 A1      LDFF00  ($A1),A         
56ED: CD 91 08   CALL    $0891           
56F0: 20 2A      JR      NZ,$571C        
56F2: 36 10      LD      (HL),$10        
56F4: 21 10 C2   LD      HL,$C210        
56F7: 09         ADD     HL,BC           
56F8: 7E         LD      A,(HL)          
56F9: C6 04      ADD     $04             
56FB: 77         LD      (HL),A          
56FC: 21 B0 C3   LD      HL,$C3B0        
56FF: 09         ADD     HL,BC           
5700: 7E         LD      A,(HL)          
5701: 3C         INC     A               
5702: 77         LD      (HL),A          
5703: FE 04      CP      $04             
5705: 20 15      JR      NZ,$571C        
5707: 21 10 C3   LD      HL,$C310        
570A: 09         ADD     HL,BC           
570B: 36 18      LD      (HL),$18        
570D: 21 10 C2   LD      HL,$C210        
5710: 09         ADD     HL,BC           
5711: 7E         LD      A,(HL)          
5712: C6 18      ADD     $18             
5714: 77         LD      (HL),A          
5715: 3E 08      LD      A,$08           
5717: E0 F2      LDFF00  ($F2),A         
5719: CD 8D 3B   CALL    $3B8D           
571C: C9         RET                     
571D: 3E 02      LD      A,$02           
571F: E0 A1      LDFF00  ($A1),A         
5721: 21 10 C3   LD      HL,$C310        
5724: 09         ADD     HL,BC           
5725: 7E         LD      A,(HL)          
5726: A7         AND     A               
5727: 20 2C      JR      NZ,$5755        
5729: CD 8D 3B   CALL    $3B8D           
572C: CD 91 08   CALL    $0891           
572F: 36 08      LD      (HL),$08        
5731: 3E 24      LD      A,$24           
5733: E0 F4      LDFF00  ($F4),A         
5735: F0 EE      LD      A,($EE)         
5737: E0 D7      LDFF00  ($D7),A         
5739: F0 EC      LD      A,($EC)         
573B: C6 10      ADD     $10             
573D: E0 D8      LDFF00  ($D8),A         
573F: 3E 01      LD      A,$01           
5741: CD 53 09   CALL    $0953           
5744: F0 EE      LD      A,($EE)         
5746: C6 10      ADD     $10             
5748: E0 D7      LDFF00  ($D7),A         
574A: F0 EC      LD      A,($EC)         
574C: C6 10      ADD     $10             
574E: E0 D8      LDFF00  ($D8),A         
5750: 3E 01      LD      A,$01           
5752: CD 53 09   CALL    $0953           
5755: C9         RET                     
5756: CD 91 08   CALL    $0891           
5759: 20 21      JR      NZ,$577C        
575B: CD 8D 3B   CALL    $3B8D           
575E: F0 B0      LD      A,($B0)         
5760: EA 68 D3   LD      ($D368),A       
5763: 3E FF      LD      A,$FF           
5765: CD 87 3B   CALL    $3B87           
5768: 3E E2      LD      A,$E2           
576A: CD 85 21   CALL    $2185           
576D: 3E 03      LD      A,$03           
576F: CD BA 59   CALL    $59BA           
5772: 3E 03      LD      A,$03           
5774: E0 9E      LDFF00  ($9E),A         
5776: C5         PUSH    BC              
5777: CD 7C 08   CALL    $087C           
577A: C1         POP     BC              
577B: C9         RET                     
577C: 3E 05      LD      A,$05           
577E: C3 87 3B   JP      $3B87           
5781: 3E C8      LD      A,$C8           
5783: CD 01 3C   CALL    $3C01           
5786: 21 00 C2   LD      HL,$C200        
5789: 19         ADD     HL,DE           
578A: 36 F8      LD      (HL),$F8        
578C: 21 E0 C2   LD      HL,$C2E0        
578F: 19         ADD     HL,DE           
5790: 36 20      LD      (HL),$20        
5792: 21 10 C2   LD      HL,$C210        
5795: 19         ADD     HL,DE           
5796: 36 48      LD      (HL),$48        
5798: CD 76 7E   CALL    $7E76           
579B: CD 2B 7F   CALL    $7F2B           
579E: C9         RET                     
579F: C9         RET                     
57A0: 00         NOP                     
57A1: 00         NOP                     
57A2: 60         LD      H,B             
57A3: 00         NOP                     
57A4: 00         NOP                     
57A5: 08 62 00   LD      ($0062),SP      
57A8: 00         NOP                     
57A9: 10 64      STOP    $64             
57AB: 00         NOP                     
57AC: 00         NOP                     
57AD: 18 66      JR      $5815           
57AF: 00         NOP                     
57B0: 10 00      STOP    $00             
57B2: 68         LD      L,B             
57B3: 00         NOP                     
57B4: 10 08      STOP    $08             
57B6: 6A         LD      L,D             
57B7: 00         NOP                     
57B8: 10 10      STOP    $10             
57BA: 6C         LD      L,H             
57BB: 00         NOP                     
57BC: 10 18      STOP    $18             
57BE: 6E         LD      L,(HL)          
57BF: 00         NOP                     
57C0: 00         NOP                     
57C1: 00         NOP                     
57C2: 60         LD      H,B             
57C3: 00         NOP                     
57C4: 00         NOP                     
57C5: 08 70 00   LD      ($0070),SP      
57C8: 00         NOP                     
57C9: 10 64      STOP    $64             
57CB: 00         NOP                     
57CC: 00         NOP                     
57CD: 18 66      JR      $5835           
57CF: 00         NOP                     
57D0: 10 00      STOP    $00             
57D2: 68         LD      L,B             
57D3: 00         NOP                     
57D4: 10 08      STOP    $08             
57D6: 6A         LD      L,D             
57D7: 00         NOP                     
57D8: 10 10      STOP    $10             
57DA: 6C         LD      L,H             
57DB: 00         NOP                     
57DC: 10 18      STOP    $18             
57DE: 6E         LD      L,(HL)          
57DF: 00         NOP                     
57E0: 00         NOP                     
57E1: 00         NOP                     
57E2: 72         LD      (HL),D          
57E3: 00         NOP                     
57E4: 00         NOP                     
57E5: 08 74 00   LD      ($0074),SP      
57E8: 00         NOP                     
57E9: 10 64      STOP    $64             
57EB: 00         NOP                     
57EC: 00         NOP                     
57ED: 18 66      JR      $5855           
57EF: 00         NOP                     
57F0: 10 00      STOP    $00             
57F2: 76         HALT                    
57F3: 00         NOP                     
57F4: 10 08      STOP    $08             
57F6: 6A         LD      L,D             
57F7: 00         NOP                     
57F8: 10 10      STOP    $10             
57FA: 6C         LD      L,H             
57FB: 00         NOP                     
57FC: 10 18      STOP    $18             
57FE: 6E         LD      L,(HL)          
57FF: 00         NOP                     
5800: 00         NOP                     
5801: 00         NOP                     
5802: 78         LD      A,B             
5803: 00         NOP                     
5804: 00         NOP                     
5805: 08 7A 00   LD      ($007A),SP      
5808: 00         NOP                     
5809: 10 7C      STOP    $7C             
580B: 00         NOP                     
580C: 00         NOP                     
580D: 18 7E      JR      $588D           
580F: 00         NOP                     
5810: 10 00      STOP    $00             
5812: 78         LD      A,B             
5813: 40         LD      B,B             
5814: 10 08      STOP    $08             
5816: 7A         LD      A,D             
5817: 40         LD      B,B             
5818: 10 10      STOP    $10             
581A: 7C         LD      A,H             
581B: 40         LD      B,B             
581C: 10 18      STOP    $18             
581E: 7E         LD      A,(HL)          
581F: 40         LD      B,B             
5820: 00         NOP                     
5821: 00         NOP                     
5822: 68         LD      L,B             
5823: 40         LD      B,B             
5824: 00         NOP                     
5825: 08 6A 40   LD      ($406A),SP      
5828: 00         NOP                     
5829: 10 6C      STOP    $6C             
582B: 40         LD      B,B             
582C: 00         NOP                     
582D: 18 6E      JR      $589D           
582F: 40         LD      B,B             
5830: 10 00      STOP    $00             
5832: 60         LD      H,B             
5833: 40         LD      B,B             
5834: 10 08      STOP    $08             
5836: 62         LD      H,D             
5837: 40         LD      B,B             
5838: 10 10      STOP    $10             
583A: 64         LD      H,H             
583B: 40         LD      B,B             
583C: 10 18      STOP    $18             
583E: 66         LD      H,(HL)          
583F: 40         LD      B,B             
5840: 0E 00      LD      C,$00           
5842: 68         LD      L,B             
5843: 40         LD      B,B             
5844: 0E 08      LD      C,$08           
5846: 6A         LD      L,D             
5847: 40         LD      B,B             
5848: 0E 10      LD      C,$10           
584A: 6C         LD      L,H             
584B: 40         LD      B,B             
584C: 0E 18      LD      C,$18           
584E: 6E         LD      L,(HL)          
584F: 40         LD      B,B             
5850: 10 00      STOP    $00             
5852: FF         RST     0X38            
5853: 40         LD      B,B             
5854: 10 08      STOP    $08             
5856: FF         RST     0X38            
5857: 40         LD      B,B             
5858: 10 10      STOP    $10             
585A: FF         RST     0X38            
585B: 40         LD      B,B             
585C: 10 18      STOP    $18             
585E: FF         RST     0X38            
585F: 40         LD      B,B             
5860: 17         RLA                     
5861: 03         INC     BC              
5862: 26 00      LD      H,$00           
5864: 17         RLA                     
5865: 09         ADD     HL,BC           
5866: 26 00      LD      H,$00           
5868: 17         RLA                     
5869: 0F         RRCA                    
586A: 26 00      LD      H,$00           
586C: 17         RLA                     
586D: 15         DEC     D               
586E: 26 00      LD      H,$00           
5870: F0 F1      LD      A,($F1)         
5872: 17         RLA                     
5873: 17         RLA                     
5874: 17         RLA                     
5875: 17         RLA                     
5876: 17         RLA                     
5877: E6 E0      AND     $E0             
5879: 5F         LD      E,A             
587A: 50         LD      D,B             
587B: 21 A0 57   LD      HL,$57A0        
587E: 19         ADD     HL,DE           
587F: 0E 08      LD      C,$08           
5881: CD 26 3D   CALL    $3D26           
5884: 21 10 C3   LD      HL,$C310        
5887: 09         ADD     HL,BC           
5888: 7E         LD      A,(HL)          
5889: A7         AND     A               
588A: C8         RET     Z               
588B: F0 EF      LD      A,($EF)         
588D: E0 EC      LDFF00  ($EC),A         
588F: 21 60 58   LD      HL,$5860        
5892: 0E 04      LD      C,$04           
5894: CD 26 3D   CALL    $3D26           
5897: 3E 04      LD      A,$04           
5899: CD D0 3D   CALL    $3DD0           
589C: CD BA 3D   CALL    $3DBA           
589F: C9         RET                     
58A0: CD 77 59   CALL    $5977           
58A3: FA 24 C1   LD      A,($C124)       
58A6: A7         AND     A               
58A7: C0         RET     NZ              
58A8: F0 F0      LD      A,($F0)         
58AA: C7         RST     0X00            
58AB: B3         OR      E               
58AC: 58         LD      E,B             
58AD: C7         RST     0X00            
58AE: 58         LD      E,B             
58AF: E7         RST     0X20            
58B0: 58         LD      E,B             
58B1: FC         ???                     
58B2: 58         LD      E,B             
58B3: 21 10 C2   LD      HL,$C210        
58B6: 09         ADD     HL,BC           
58B7: 36 68      LD      (HL),$68        
58B9: 21 00 C2   LD      HL,$C200        
58BC: 09         ADD     HL,BC           
58BD: 36 80      LD      (HL),$80        
58BF: CD 91 08   CALL    $0891           
58C2: 36 20      LD      (HL),$20        
58C4: C3 8D 3B   JP      $3B8D           
58C7: CD 91 08   CALL    $0891           
58CA: 20 1A      JR      NZ,$58E6        
58CC: FA 4A DB   LD      A,($DB4A)       
58CF: FE 00      CP      $00             
58D1: 20 13      JR      NZ,$58E6        
58D3: FA 66 C1   LD      A,($C166)       
58D6: A7         AND     A               
58D7: FE 40      CP      $40             
58D9: 20 0B      JR      NZ,$58E6        
58DB: CD 8D 3B   CALL    $3B8D           
58DE: CD 91 08   CALL    $0891           
58E1: 36 20      LD      (HL),$20        
58E3: CD 31 57   CALL    $5731           
58E6: C9         RET                     
58E7: CD 91 08   CALL    $0891           
58EA: 20 05      JR      NZ,$58F1        
58EC: 36 C8      LD      (HL),$C8        
58EE: C3 8D 3B   JP      $3B8D           
58F1: FE 10      CP      $10             
58F3: 3E 01      LD      A,$01           
58F5: 38 01      JR      C,$58F8         
58F7: 3C         INC     A               
58F8: CD 87 3B   CALL    $3B87           
58FB: C9         RET                     
58FC: CD 91 08   CALL    $0891           
58FF: 20 06      JR      NZ,$5907        
5901: CD 31 57   CALL    $5731           
5904: C3 76 7E   JP      $7E76           
5907: FE B0      CP      $B0             
5909: 20 00      JR      NZ,$590B        
590B: CD 91 08   CALL    $0891           
590E: FE 80      CP      $80             
5910: 20 06      JR      NZ,$5918        
5912: 35         DEC     (HL)            
5913: 3E E6      LD      A,$E6           
5915: CD 85 21   CALL    $2185           
5918: CD 91 08   CALL    $0891           
591B: 16 00      LD      D,$00           
591D: FE 10      CP      $10             
591F: 1E 02      LD      E,$02           
5921: 38 06      JR      C,$5929         
5923: 1D         DEC     E               
5924: FE 20      CP      $20             
5926: 38 01      JR      C,$5929         
5928: 14         INC     D               
5929: 21 90 C3   LD      HL,$C390        
592C: 09         ADD     HL,BC           
592D: 72         LD      (HL),D          
592E: 7B         LD      A,E             
592F: CD 87 3B   CALL    $3B87           
5932: C9         RET                     
5933: FF         RST     0X38            
5934: 04         INC     B               
5935: FF         RST     0X38            
5936: 00         NOP                     
5937: FF         RST     0X38            
5938: 0C         INC     C               
5939: FF         RST     0X38            
593A: 00         NOP                     
593B: FF         RST     0X38            
593C: 04         INC     B               
593D: FF         RST     0X38            
593E: 00         NOP                     
593F: FF         RST     0X38            
5940: 0C         INC     C               
5941: FF         RST     0X38            
5942: 00         NOP                     
5943: FF         RST     0X38            
5944: 14         INC     D               
5945: FF         RST     0X38            
5946: 00         NOP                     
5947: FC         ???                     
5948: 04         INC     B               
5949: 70         LD      (HL),B          
594A: 00         NOP                     
594B: FC         ???                     
594C: 0C         INC     C               
594D: 72         LD      (HL),D          
594E: 00         NOP                     
594F: 0C         INC     C               
5950: 04         INC     B               
5951: 74         LD      (HL),H          
5952: 00         NOP                     
5953: 0C         INC     C               
5954: 0C         INC     C               
5955: 76         HALT                    
5956: 00         NOP                     
5957: 0C         INC     C               
5958: 14         INC     D               
5959: 78         LD      A,B             
595A: 00         NOP                     
595B: 0C         INC     C               
595C: 04         INC     B               
595D: 7A         LD      A,D             
595E: 00         NOP                     
595F: 0C         INC     C               
5960: 0C         INC     C               
5961: 7C         LD      A,H             
5962: 00         NOP                     
5963: 0C         INC     C               
5964: 14         INC     D               
5965: 7E         LD      A,(HL)          
5966: 00         NOP                     
5967: FF         RST     0X38            
5968: FF         RST     0X38            
5969: FF         RST     0X38            
596A: FF         RST     0X38            
596B: FF         RST     0X38            
596C: FF         RST     0X38            
596D: FF         RST     0X38            
596E: FF         RST     0X38            
596F: 00         NOP                     
5970: 00         NOP                     
5971: 01 02 03   LD      BC,$0302        
5974: 03         INC     BC              
5975: 02         LD      (BC),A          
5976: 01 F0 E7   LD      BC,$E7F0        
5979: 1F         RRA                     
597A: 1F         RRA                     
597B: 1F         RRA                     
597C: 1F         RRA                     
597D: 00         NOP                     
597E: 00         NOP                     
597F: E6 07      AND     $07             
5981: 5F         LD      E,A             
5982: 50         LD      D,B             
5983: 21 6F 59   LD      HL,$596F        
5986: 19         ADD     HL,DE           
5987: F0 EC      LD      A,($EC)         
5989: 86         ADD     A,(HL)          
598A: E0 EC      LDFF00  ($EC),A         
598C: 21 90 C3   LD      HL,$C390        
598F: 09         ADD     HL,BC           
5990: 7E         LD      A,(HL)          
5991: A7         AND     A               
5992: 28 0D      JR      Z,$59A1         
5994: F0 E7      LD      A,($E7)         
5996: 1F         RRA                     
5997: 1F         RRA                     
5998: 1F         RRA                     
5999: 1F         RRA                     
599A: 1F         RRA                     
599B: 1F         RRA                     
599C: E6 01      AND     $01             
599E: 3C         INC     A               
599F: E0 F1      LDFF00  ($F1),A         
59A1: F0 F1      LD      A,($F1)         
59A3: 17         RLA                     
59A4: 17         RLA                     
59A5: E6 FC      AND     $FC             
59A7: 5F         LD      E,A             
59A8: 17         RLA                     
59A9: 17         RLA                     
59AA: E6 F0      AND     $F0             
59AC: 83         ADD     A,E             
59AD: 5F         LD      E,A             
59AE: 50         LD      D,B             
59AF: 21 33 59   LD      HL,$5933        
59B2: 19         ADD     HL,DE           
59B3: 0E 05      LD      C,$05           
59B5: C3 26 3D   JP      $3D26           
59B8: 3E 00      LD      A,$00           
59BA: 1E 10      LD      E,$10           
59BC: 21 B5 D1   LD      HL,$D1B5        
59BF: 22         LD      (HLI),A         
59C0: 1D         DEC     E               
59C1: 20 FC      JR      NZ,$59BF        
59C3: C9         RET                     
59C4: 42         LD      B,D             
59C5: 20 40      JR      NZ,$5A07        
59C7: 20 40      JR      NZ,$5A09        
59C9: 00         NOP                     
59CA: 42         LD      B,D             
59CB: 00         NOP                     
59CC: 44         LD      B,H             
59CD: 00         NOP                     
59CE: 46         LD      B,(HL)          
59CF: 00         NOP                     
59D0: 46         LD      B,(HL)          
59D1: 20 44      JR      NZ,$5A17        
59D3: 20 48      JR      NZ,$5A1D        
59D5: 00         NOP                     
59D6: 4A         LD      C,D             
59D7: 00         NOP                     
59D8: 4C         LD      C,H             
59D9: 00         NOP                     
59DA: 4E         LD      C,(HL)          
59DB: 00         NOP                     
59DC: 4A         LD      C,D             
59DD: 20 48      JR      NZ,$5A27        
59DF: 20 4E      JR      NZ,$5A2F        
59E1: 20 4C      JR      NZ,$5A2F        
59E3: 20 50      JR      NZ,$5A35        
59E5: 00         NOP                     
59E6: 52         LD      D,D             
59E7: 00         NOP                     
59E8: 54         LD      D,H             
59E9: 00         NOP                     
59EA: 54         LD      D,H             
59EB: 20 52      JR      NZ,$5A3F        
59ED: 20 50      JR      NZ,$5A3F        
59EF: 20 06      JR      NZ,$59F7        
59F1: 04         INC     B               
59F2: 02         LD      (BC),A          
59F3: 00         NOP                     
59F4: 79         LD      A,C             
59F5: EA 0F C5   LD      ($C50F),A       
59F8: CD 91 08   CALL    $0891           
59FB: 28 4E      JR      Z,$5A4B         
59FD: FE 10      CP      $10             
59FF: 20 12      JR      NZ,$5A13        
5A01: 35         DEC     (HL)            
5A02: F0 99      LD      A,($99)         
5A04: F5         PUSH    AF              
5A05: 3E 28      LD      A,$28           
5A07: E0 99      LDFF00  ($99),A         
5A09: 3E 1F      LD      A,$1F           
5A0B: CD 97 21   CALL    $2197           
5A0E: F1         POP     AF              
5A0F: E0 99      LDFF00  ($99),A         
5A11: 3E 0F      LD      A,$0F           
5A13: FE 01      CP      $01             
5A15: 20 0D      JR      NZ,$5A24        
5A17: AF         XOR     A               
5A18: EA 67 C1   LD      ($C167),A       
5A1B: 3E 31      LD      A,$31           
5A1D: EA 68 D3   LD      ($D368),A       
5A20: 3E 05      LD      A,$05           
5A22: E0 B0      LDFF00  ($B0),A         
5A24: AF         XOR     A               
5A25: EA B0 C3   LD      ($C3B0),A       
5A28: 11 C4 59   LD      DE,$59C4        
5A2B: CD 3B 3C   CALL    $3C3B           
5A2E: 3E 6C      LD      A,$6C           
5A30: E0 9D      LDFF00  ($9D),A         
5A32: 3E 02      LD      A,$02           
5A34: E0 A1      LDFF00  ($A1),A         
5A36: 3E 03      LD      A,$03           
5A38: E0 9E      LDFF00  ($9E),A         
5A3A: F0 98      LD      A,($98)         
5A3C: 21 00 C2   LD      HL,$C200        
5A3F: 09         ADD     HL,BC           
5A40: 77         LD      (HL),A          
5A41: F0 99      LD      A,($99)         
5A43: D6 10      SUB     $10             
5A45: 21 10 C2   LD      HL,$C210        
5A48: 09         ADD     HL,BC           
5A49: 77         LD      (HL),A          
5A4A: C9         RET                     
5A4B: 21 40 C4   LD      HL,$C440        
5A4E: 09         ADD     HL,BC           
5A4F: 7E         LD      A,(HL)          
5A50: A7         AND     A               
5A51: 20 45      JR      NZ,$5A98        
5A53: FA 6B C1   LD      A,($C16B)       
5A56: FE 04      CP      $04             
5A58: 20 31      JR      NZ,$5A8B        
5A5A: 34         INC     (HL)            
5A5B: CD 91 08   CALL    $0891           
5A5E: 36 70      LD      (HL),$70        
5A60: 3E 10      LD      A,$10           
5A62: EA 68 D3   LD      ($D368),A       
5A65: 3E FF      LD      A,$FF           
5A67: E0 BF      LDFF00  ($BF),A         
5A69: F0 98      LD      A,($98)         
5A6B: 21 55 D1   LD      HL,$D155        
5A6E: CD 85 5A   CALL    $5A85           
5A71: F0 99      LD      A,($99)         
5A73: 21 75 D1   LD      HL,$D175        
5A76: CD 85 5A   CALL    $5A85           
5A79: AF         XOR     A               
5A7A: 21 95 D1   LD      HL,$D195        
5A7D: CD 85 5A   CALL    $5A85           
5A80: F0 9E      LD      A,($9E)         
5A82: 21 B5 D1   LD      HL,$D1B5        
5A85: 1E 10      LD      E,$10           
5A87: 22         LD      (HLI),A         
5A88: 1D         DEC     E               
5A89: 20 FC      JR      NZ,$5A87        
5A8B: C9         RET                     
5A8C: 08 08 08   LD      ($0808),SP      
5A8F: 09         ADD     HL,BC           
5A90: 0A         LD      A,(BC)          
5A91: 0A         LD      A,(BC)          
5A92: 0A         LD      A,(BC)          
5A93: 09         ADD     HL,BC           
5A94: 08 F8 06   LD      ($06F8),SP      
5A97: 01 FA C8   LD      BC,$C8FA        
5A9A: C3 A7 28   JP      $28A7           
5A9D: 55         LD      D,L             
5A9E: F0 E7      LD      A,($E7)         
5AA0: 1F         RRA                     
5AA1: 1F         RRA                     
5AA2: 1F         RRA                     
5AA3: 1F         RRA                     
5AA4: E6 07      AND     $07             
5AA6: 5F         LD      E,A             
5AA7: 50         LD      D,B             
5AA8: 21 8C 5A   LD      HL,$5A8C        
5AAB: 19         ADD     HL,DE           
5AAC: 7E         LD      A,(HL)          
5AAD: E0 F1      LDFF00  ($F1),A         
5AAF: F0 E7      LD      A,($E7)         
5AB1: E6 1F      AND     $1F             
5AB3: 20 3E      JR      NZ,$5AF3        
5AB5: 3E C9      LD      A,$C9           
5AB7: CD 01 3C   CALL    $3C01           
5ABA: 38 37      JR      C,$5AF3         
5ABC: F0 D8      LD      A,($D8)         
5ABE: 21 10 C2   LD      HL,$C210        
5AC1: 19         ADD     HL,DE           
5AC2: D6 08      SUB     $08             
5AC4: 77         LD      (HL),A          
5AC5: C5         PUSH    BC              
5AC6: F0 E7      LD      A,($E7)         
5AC8: 1F         RRA                     
5AC9: 1F         RRA                     
5ACA: 1F         RRA                     
5ACB: 1F         RRA                     
5ACC: 1F         RRA                     
5ACD: E6 01      AND     $01             
5ACF: 4F         LD      C,A             
5AD0: 21 94 5A   LD      HL,$5A94        
5AD3: 09         ADD     HL,BC           
5AD4: F0 D7      LD      A,($D7)         
5AD6: 86         ADD     A,(HL)          
5AD7: 21 00 C2   LD      HL,$C200        
5ADA: 19         ADD     HL,DE           
5ADB: 77         LD      (HL),A          
5ADC: 21 96 5A   LD      HL,$5A96        
5ADF: 09         ADD     HL,BC           
5AE0: 7E         LD      A,(HL)          
5AE1: 21 40 C2   LD      HL,$C240        
5AE4: 19         ADD     HL,DE           
5AE5: 77         LD      (HL),A          
5AE6: 21 50 C2   LD      HL,$C250        
5AE9: 19         ADD     HL,DE           
5AEA: 36 FC      LD      (HL),$FC        
5AEC: 21 D0 C3   LD      HL,$C3D0        
5AEF: 19         ADD     HL,DE           
5AF0: 36 40      LD      (HL),$40        
5AF2: C1         POP     BC              
5AF3: 11 C4 59   LD      DE,$59C4        
5AF6: CD 3B 3C   CALL    $3C3B           
5AF9: FA 4F C1   LD      A,($C14F)       
5AFC: A7         AND     A               
5AFD: C0         RET     NZ              
5AFE: 21 80 C4   LD      HL,$C480        
5B01: 09         ADD     HL,BC           
5B02: 7E         LD      A,(HL)          
5B03: A7         AND     A               
5B04: 28 09      JR      Z,$5B0F         
5B06: 3D         DEC     A               
5B07: 20 06      JR      NZ,$5B0F        
5B09: 35         DEC     (HL)            
5B0A: 3E 7A      LD      A,$7A           
5B0C: CD 8E 21   CALL    $218E           
5B0F: 21 00 C3   LD      HL,$C300        
5B12: 09         ADD     HL,BC           
5B13: 7E         LD      A,(HL)          
5B14: A7         AND     A               
5B15: 28 53      JR      Z,$5B6A         
5B17: FE 30      CP      $30             
5B19: 20 3A      JR      NZ,$5B55        
5B1B: AF         XOR     A               
5B1C: EA 67 C1   LD      ($C167),A       
5B1F: F0 98      LD      A,($98)         
5B21: D6 58      SUB     $58             
5B23: C6 03      ADD     $03             
5B25: FE 06      CP      $06             
5B27: 30 0A      JR      NC,$5B33        
5B29: F0 99      LD      A,($99)         
5B2B: D6 50      SUB     $50             
5B2D: C6 03      ADD     $03             
5B2F: FE 06      CP      $06             
5B31: 38 08      JR      C,$5B3B         
5B33: 70         LD      (HL),B          
5B34: 21 80 C4   LD      HL,$C480        
5B37: 09         ADD     HL,BC           
5B38: 36 1C      LD      (HL),$1C        
5B3A: C9         RET                     
5B3B: 21 F2 FF   LD      HL,$FFF2        
5B3E: 36 0B      LD      (HL),$0B        
5B40: 21 F3 FF   LD      HL,$FFF3        
5B43: 36 03      LD      (HL),$03        
5B45: 21 57 C1   LD      HL,$C157        
5B48: 36 18      LD      (HL),$18        
5B4A: 21 58 C1   LD      HL,$C158        
5B4D: 36 04      LD      (HL),$04        
5B4F: 21 98 FF   LD      HL,$FF98        
5B52: 34         INC     (HL)            
5B53: 18 0C      JR      $5B61           
5B55: 30 13      JR      NC,$5B6A        
5B57: FE 10      CP      $10             
5B59: 20 06      JR      NZ,$5B61        
5B5B: 35         DEC     (HL)            
5B5C: 3E 7B      LD      A,$7B           
5B5E: CD 8E 21   CALL    $218E           
5B61: 3E 02      LD      A,$02           
5B63: E0 A1      LDFF00  ($A1),A         
5B65: 3E 6A      LD      A,$6A           
5B67: E0 9D      LDFF00  ($9D),A         
5B69: C9         RET                     
5B6A: FA 74 DB   LD      A,($DB74)       
5B6D: 21 BC C1   LD      HL,$C1BC        
5B70: B6         OR      (HL)            
5B71: C0         RET     NZ              
5B72: FA 10 DB   LD      A,($DB10)       
5B75: A7         AND     A               
5B76: CA 70 5C   JP      Z,$5C70         
5B79: CD 9E 3B   CALL    $3B9E           
5B7C: 3E 02      LD      A,$02           
5B7E: E0 A1      LDFF00  ($A1),A         
5B80: EA 67 C1   LD      ($C167),A       
5B83: CD 61 7D   CALL    $7D61           
5B86: FA 68 D4   LD      A,($D468)       
5B89: A7         AND     A               
5B8A: 28 04      JR      Z,$5B90         
5B8C: 3D         DEC     A               
5B8D: EA 68 D4   LD      ($D468),A       
5B90: F0 F0      LD      A,($F0)         
5B92: C7         RST     0X00            
5B93: 9D         SBC     L               
5B94: 5B         LD      E,E             
5B95: B4         OR      H               
5B96: 5B         LD      E,E             
5B97: D2 5B 0B   JP      NC,$0B5B        
5B9A: 5C         LD      E,H             
5B9B: 3F         CCF                     
5B9C: 5C         LD      E,H             
5B9D: FA 1C C1   LD      A,($C11C)       
5BA0: FE 03      CP      $03             
5BA2: C8         RET     Z               
5BA3: 3E 40      LD      A,$40           
5BA5: EA 68 D4   LD      ($D468),A       
5BA8: 3E 0F      LD      A,$0F           
5BAA: E0 A5      LDFF00  ($A5),A         
5BAC: 3E 01      LD      A,$01           
5BAE: CD 87 3B   CALL    $3B87           
5BB1: C3 8D 3B   JP      $3B8D           
5BB4: FA 68 D4   LD      A,($D468)       
5BB7: A7         AND     A               
5BB8: 20 17      JR      NZ,$5BD1        
5BBA: 3E 18      LD      A,$18           
5BBC: EA 68 D4   LD      ($D468),A       
5BBF: 21 80 C3   LD      HL,$C380        
5BC2: 09         ADD     HL,BC           
5BC3: 36 01      LD      (HL),$01        
5BC5: 3E 04      LD      A,$04           
5BC7: CD 87 3B   CALL    $3B87           
5BCA: 3E 10      LD      A,$10           
5BCC: E0 A5      LDFF00  ($A5),A         
5BCE: CD 8D 3B   CALL    $3B8D           
5BD1: C9         RET                     
5BD2: FA 68 D4   LD      A,($D468)       
5BD5: A7         AND     A               
5BD6: 20 32      JR      NZ,$5C0A        
5BD8: 21 40 C2   LD      HL,$C240        
5BDB: 09         ADD     HL,BC           
5BDC: 36 F4      LD      (HL),$F4        
5BDE: CD DA 7D   CALL    $7DDA           
5BE1: F0 E7      LD      A,($E7)         
5BE3: E6 08      AND     $08             
5BE5: 1E 04      LD      E,$04           
5BE7: 28 01      JR      Z,$5BEA         
5BE9: 1C         INC     E               
5BEA: 7B         LD      A,E             
5BEB: CD 87 3B   CALL    $3B87           
5BEE: CD 20 7E   CALL    $7E20           
5BF1: C6 02      ADD     $02             
5BF3: FE 04      CP      $04             
5BF5: D0         RET     NC              
5BF6: 21 B0 C3   LD      HL,$C3B0        
5BF9: 09         ADD     HL,BC           
5BFA: 36 02      LD      (HL),$02        
5BFC: 21 80 C3   LD      HL,$C380        
5BFF: 09         ADD     HL,BC           
5C00: 36 02      LD      (HL),$02        
5C02: 3E 10      LD      A,$10           
5C04: EA 68 D4   LD      ($D468),A       
5C07: CD 8D 3B   CALL    $3B8D           
5C0A: C9         RET                     
5C0B: FA 68 D4   LD      A,($D468)       
5C0E: A7         AND     A               
5C0F: 20 2D      JR      NZ,$5C3E        
5C11: FA 10 DB   LD      A,($DB10)       
5C14: 3D         DEC     A               
5C15: 5F         LD      E,A             
5C16: FA 63 C1   LD      A,($C163)       
5C19: BB         CP      E               
5C1A: 28 10      JR      Z,$5C2C         
5C1C: A7         AND     A               
5C1D: 28 0D      JR      Z,$5C2C         
5C1F: 1E 1C      LD      E,$1C           
5C21: CD ED 27   CALL    $27ED           
5C24: E6 3F      AND     $3F             
5C26: 20 0F      JR      NZ,$5C37        
5C28: 1E 1E      LD      E,$1E           
5C2A: 18 0B      JR      $5C37           
5C2C: 1E 1B      LD      E,$1B           
5C2E: FA 47 DB   LD      A,($DB47)       
5C31: FE 80      CP      $80             
5C33: 30 02      JR      NC,$5C37        
5C35: 1E 1D      LD      E,$1D           
5C37: 7B         LD      A,E             
5C38: CD 8E 21   CALL    $218E           
5C3B: CD 8D 3B   CALL    $3B8D           
5C3E: C9         RET                     
5C3F: AF         XOR     A               
5C40: EA 10 DB   LD      ($DB10),A       
5C43: EA 67 C1   LD      ($C167),A       
5C46: CD 8D 3B   CALL    $3B8D           
5C49: 70         LD      (HL),B          
5C4A: 21 D0 C3   LD      HL,$C3D0        
5C4D: 09         ADD     HL,BC           
5C4E: 36 FF      LD      (HL),$FF        
5C50: F0 EE      LD      A,($EE)         
5C52: 21 55 D1   LD      HL,$D155        
5C55: CD 69 5C   CALL    $5C69           
5C58: 21 75 D1   LD      HL,$D175        
5C5B: F0 EC      LD      A,($EC)         
5C5D: 1E 10      LD      E,$10           
5C5F: 22         LD      (HLI),A         
5C60: 3D         DEC     A               
5C61: 1D         DEC     E               
5C62: 20 FB      JR      NZ,$5C5F        
5C64: 3E 02      LD      A,$02           
5C66: 21 B5 D1   LD      HL,$D1B5        
5C69: 1E 10      LD      E,$10           
5C6B: 22         LD      (HLI),A         
5C6C: 1D         DEC     E               
5C6D: 20 FC      JR      NZ,$5C6B        
5C6F: C9         RET                     
5C70: FA 6B C1   LD      A,($C16B)       
5C73: FE 04      CP      $04             
5C75: C0         RET     NZ              
5C76: F0 F6      LD      A,($F6)         
5C78: 21 E0 C3   LD      HL,$C3E0        
5C7B: 09         ADD     HL,BC           
5C7C: 77         LD      (HL),A          
5C7D: 21 20 C2   LD      HL,$C220        
5C80: 09         ADD     HL,BC           
5C81: 70         LD      (HL),B          
5C82: 21 30 C2   LD      HL,$C230        
5C85: 09         ADD     HL,BC           
5C86: 70         LD      (HL),B          
5C87: 21 80 C3   LD      HL,$C380        
5C8A: 09         ADD     HL,BC           
5C8B: 5E         LD      E,(HL)          
5C8C: 50         LD      D,B             
5C8D: 21 F0 59   LD      HL,$59F0        
5C90: 19         ADD     HL,DE           
5C91: E5         PUSH    HL              
5C92: FA 20 C1   LD      A,($C120)       
5C95: 1F         RRA                     
5C96: 1F         RRA                     
5C97: 1F         RRA                     
5C98: E1         POP     HL              
5C99: E6 01      AND     $01             
5C9B: B6         OR      (HL)            
5C9C: CD 87 3B   CALL    $3B87           
5C9F: 21 D0 C3   LD      HL,$C3D0        
5CA2: 09         ADD     HL,BC           
5CA3: 7E         LD      A,(HL)          
5CA4: E0 E8      LDFF00  ($E8),A         
5CA6: E6 0F      AND     $0F             
5CA8: 5F         LD      E,A             
5CA9: 50         LD      D,B             
5CAA: 21 55 D1   LD      HL,$D155        
5CAD: 19         ADD     HL,DE           
5CAE: F0 9F      LD      A,($9F)         
5CB0: 77         LD      (HL),A          
5CB1: F0 A0      LD      A,($A0)         
5CB3: 21 3B C1   LD      HL,$C13B        
5CB6: 86         ADD     A,(HL)          
5CB7: 21 75 D1   LD      HL,$D175        
5CBA: 19         ADD     HL,DE           
5CBB: 77         LD      (HL),A          
5CBC: 21 B5 D1   LD      HL,$D1B5        
5CBF: 19         ADD     HL,DE           
5CC0: F0 9E      LD      A,($9E)         
5CC2: 77         LD      (HL),A          
5CC3: 21 B0 C2   LD      HL,$C2B0        
5CC6: 09         ADD     HL,BC           
5CC7: 7E         LD      A,(HL)          
5CC8: E0 E9      LDFF00  ($E9),A         
5CCA: E6 0F      AND     $0F             
5CCC: 5F         LD      E,A             
5CCD: 50         LD      D,B             
5CCE: 21 95 D1   LD      HL,$D195        
5CD1: 19         ADD     HL,DE           
5CD2: F0 A2      LD      A,($A2)         
5CD4: 77         LD      (HL),A          
5CD5: FA 1C C1   LD      A,($C11C)       
5CD8: FE 02      CP      $02             
5CDA: 28 14      JR      Z,$5CF0         
5CDC: FA 24 C1   LD      A,($C124)       
5CDF: A7         AND     A               
5CE0: 20 0E      JR      NZ,$5CF0        
5CE2: FA 9F C1   LD      A,($C19F)       
5CE5: A7         AND     A               
5CE6: 20 0D      JR      NZ,$5CF5        
5CE8: 21 9A FF   LD      HL,$FF9A        
5CEB: F0 9B      LD      A,($9B)         
5CED: B6         OR      (HL)            
5CEE: 28 05      JR      Z,$5CF5         
5CF0: 21 D0 C3   LD      HL,$C3D0        
5CF3: 09         ADD     HL,BC           
5CF4: 34         INC     (HL)            
5CF5: 21 B0 C2   LD      HL,$C2B0        
5CF8: 09         ADD     HL,BC           
5CF9: 34         INC     (HL)            
5CFA: F0 E8      LD      A,($E8)         
5CFC: 3C         INC     A               
5CFD: E6 0F      AND     $0F             
5CFF: 5F         LD      E,A             
5D00: 50         LD      D,B             
5D01: 21 55 D1   LD      HL,$D155        
5D04: 19         ADD     HL,DE           
5D05: 7E         LD      A,(HL)          
5D06: 21 00 C2   LD      HL,$C200        
5D09: 09         ADD     HL,BC           
5D0A: 77         LD      (HL),A          
5D0B: 21 75 D1   LD      HL,$D175        
5D0E: 19         ADD     HL,DE           
5D0F: 7E         LD      A,(HL)          
5D10: 21 10 C2   LD      HL,$C210        
5D13: 09         ADD     HL,BC           
5D14: 77         LD      (HL),A          
5D15: 21 B5 D1   LD      HL,$D1B5        
5D18: 19         ADD     HL,DE           
5D19: 7E         LD      A,(HL)          
5D1A: 21 80 C3   LD      HL,$C380        
5D1D: 09         ADD     HL,BC           
5D1E: 77         LD      (HL),A          
5D1F: F0 E9      LD      A,($E9)         
5D21: 3C         INC     A               
5D22: E6 0F      AND     $0F             
5D24: 5F         LD      E,A             
5D25: 50         LD      D,B             
5D26: 21 10 C3   LD      HL,$C310        
5D29: 09         ADD     HL,BC           
5D2A: 7E         LD      A,(HL)          
5D2B: F5         PUSH    AF              
5D2C: 21 95 D1   LD      HL,$D195        
5D2F: 19         ADD     HL,DE           
5D30: 5E         LD      E,(HL)          
5D31: 21 10 C3   LD      HL,$C310        
5D34: 09         ADD     HL,BC           
5D35: 73         LD      (HL),E          
5D36: CD 8C 08   CALL    $088C           
5D39: 21 24 C1   LD      HL,$C124        
5D3C: B6         OR      (HL)            
5D3D: 20 44      JR      NZ,$5D83        
5D3F: F1         POP     AF              
5D40: BB         CP      E               
5D41: 28 3D      JR      Z,$5D80         
5D43: A7         AND     A               
5D44: 28 2F      JR      Z,$5D75         
5D46: 7B         LD      A,E             
5D47: A7         AND     A               
5D48: 20 36      JR      NZ,$5D80        
5D4A: CD 9E 3B   CALL    $3B9E           
5D4D: 21 80 C2   LD      HL,$C280        
5D50: 09         ADD     HL,BC           
5D51: 7E         LD      A,(HL)          
5D52: FE 02      CP      $02             
5D54: C8         RET     Z               
5D55: 21 70 C4   LD      HL,$C470        
5D58: 09         ADD     HL,BC           
5D59: 7E         LD      A,(HL)          
5D5A: 3D         DEC     A               
5D5B: FE 02      CP      $02             
5D5D: 38 05      JR      C,$5D64         
5D5F: 3E 07      LD      A,$07           
5D61: E0 F4      LDFF00  ($F4),A         
5D63: C9         RET                     
5D64: F0 EC      LD      A,($EC)         
5D66: E0 D8      LDFF00  ($D8),A         
5D68: F0 EE      LD      A,($EE)         
5D6A: E0 D7      LDFF00  ($D7),A         
5D6C: 3E 0E      LD      A,$0E           
5D6E: E0 F2      LDFF00  ($F2),A         
5D70: 3E 0C      LD      A,$0C           
5D72: C3 53 09   JP      $0953           
5D75: 7B         LD      A,E             
5D76: FE 08      CP      $08             
5D78: 3E 08      LD      A,$08           
5D7A: 30 02      JR      NC,$5D7E        
5D7C: 3E 24      LD      A,$24           
5D7E: E0 F2      LDFF00  ($F2),A         
5D80: C3 9E 3B   JP      $3B9E           
5D83: F1         POP     AF              
5D84: C9         RET                     
5D85: 00         NOP                     
5D86: 01 FF 00   LD      BC,$00FF        
5D89: 10 F0      STOP    $F0             
5D8B: CD 61 7D   CALL    $7D61           
5D8E: 3E 01      LD      A,$01           
5D90: E0 A4      LDFF00  ($A4),A         
5D92: 3C         INC     A               
5D93: E0 A1      LDFF00  ($A1),A         
5D95: EA 67 C1   LD      ($C167),A       
5D98: F0 CC      LD      A,($CC)         
5D9A: E6 03      AND     $03             
5D9C: 5F         LD      E,A             
5D9D: 50         LD      D,B             
5D9E: 21 85 5D   LD      HL,$5D85        
5DA1: 19         ADD     HL,DE           
5DA2: FA 09 C1   LD      A,($C109)       
5DA5: F5         PUSH    AF              
5DA6: 86         ADD     A,(HL)          
5DA7: E6 0F      AND     $0F             
5DA9: 5F         LD      E,A             
5DAA: F1         POP     AF              
5DAB: E6 F0      AND     $F0             
5DAD: B3         OR      E               
5DAE: EA 09 C1   LD      ($C109),A       
5DB1: F0 CC      LD      A,($CC)         
5DB3: 1F         RRA                     
5DB4: 1F         RRA                     
5DB5: E6 03      AND     $03             
5DB7: 5F         LD      E,A             
5DB8: 50         LD      D,B             
5DB9: 21 88 5D   LD      HL,$5D88        
5DBC: 19         ADD     HL,DE           
5DBD: FA 09 C1   LD      A,($C109)       
5DC0: 86         ADD     A,(HL)          
5DC1: EA 09 C1   LD      ($C109),A       
5DC4: FA 9F C1   LD      A,($C19F)       
5DC7: A7         AND     A               
5DC8: 20 18      JR      NZ,$5DE2        
5DCA: F0 CC      LD      A,($CC)         
5DCC: E6 10      AND     $10             
5DCE: 28 06      JR      Z,$5DD6         
5DD0: FA 09 C1   LD      A,($C109)       
5DD3: C3 97 21   JP      $2197           
5DD6: F0 CC      LD      A,($CC)         
5DD8: E6 20      AND     $20             
5DDA: 28 06      JR      Z,$5DE2         
5DDC: FA 09 C1   LD      A,($C109)       
5DDF: C3 85 21   JP      $2185           
5DE2: F0 CC      LD      A,($CC)         
5DE4: E6 40      AND     $40             
5DE6: 28 06      JR      Z,$5DEE         
5DE8: FA 09 C1   LD      A,($C109)       
5DEB: C3 8E 21   JP      $218E           
5DEE: C9         RET                     
5DEF: CD 61 7D   CALL    $7D61           
5DF2: F0 E7      LD      A,($E7)         
5DF4: E6 03      AND     $03             
5DF6: 20 04      JR      NZ,$5DFC        
5DF8: 21 BF C1   LD      HL,$C1BF        
5DFB: 34         INC     (HL)            
5DFC: C9         RET                     
5DFD: 5E         LD      E,(HL)          
5DFE: 00         NOP                     
5DFF: 5E         LD      E,(HL)          
5E00: 20 00      JR      NZ,$5E02        
5E02: F8 50      LDHL    SP,$50          
5E04: 00         NOP                     
5E05: 00         NOP                     
5E06: 00         NOP                     
5E07: 52         LD      D,D             
5E08: 00         NOP                     
5E09: 00         NOP                     
5E0A: 08 54 00   LD      ($0054),SP      
5E0D: 00         NOP                     
5E0E: 10 56      STOP    $56             
5E10: 00         NOP                     
5E11: 21 01 5E   LD      HL,$5E01        
5E14: 0E 04      LD      C,$04           
5E16: CD 26 3D   CALL    $3D26           
5E19: 3E 02      LD      A,$02           
5E1B: CD D0 3D   CALL    $3DD0           
5E1E: F0 F0      LD      A,($F0)         
5E20: C7         RST     0X00            
5E21: 27         DAA                     
5E22: 5E         LD      E,(HL)          
5E23: 30 5E      JR      NC,$5E83        
5E25: 4B         LD      C,E             
5E26: 5E         LD      E,(HL)          
5E27: 21 00 C2   LD      HL,$C200        
5E2A: 09         ADD     HL,BC           
5E2B: 36 50      LD      (HL),$50        
5E2D: C3 8D 3B   JP      $3B8D           
5E30: CD 61 7D   CALL    $7D61           
5E33: CD 91 08   CALL    $0891           
5E36: C0         RET     NZ              
5E37: CD 0E 7D   CALL    $7D0E           
5E3A: D0         RET     NC              
5E3B: FA 97 DB   LD      A,($DB97)       
5E3E: FE E4      CP      $E4             
5E40: 20 03      JR      NZ,$5E45        
5E42: C3 8D 3B   JP      $3B8D           
5E45: 3E E6      LD      A,$E6           
5E47: CD 97 21   CALL    $2197           
5E4A: C9         RET                     
5E4B: CD 61 7D   CALL    $7D61           
5E4E: FA 9F C1   LD      A,($C19F)       
5E51: A7         AND     A               
5E52: 20 13      JR      NZ,$5E67        
5E54: 3E 0A      LD      A,$0A           
5E56: CD 36 4C   CALL    $4C36           
5E59: CD 91 08   CALL    $0891           
5E5C: 36 20      LD      (HL),$20        
5E5E: CD 8D 3B   CALL    $3B8D           
5E61: 70         LD      (HL),B          
5E62: 21 AC D8   LD      HL,$D8AC        
5E65: CB E6      SET     1,E             
5E67: C9         RET                     
5E68: F0 F7      LD      A,($F7)         
5E6A: FE 16      CP      $16             
5E6C: CA 11 5E   JP      Z,$5E11         
5E6F: F0 EC      LD      A,($EC)         
5E71: C6 01      ADD     $01             
5E73: E0 EC      LDFF00  ($EC),A         
5E75: 11 FD 5D   LD      DE,$5DFD        
5E78: CD 3B 3C   CALL    $3C3B           
5E7B: CD AF 7C   CALL    $7CAF           
5E7E: CD 61 7D   CALL    $7D61           
5E81: CD 0E 7D   CALL    $7D0E           
5E84: 30 0F      JR      NC,$5E95        
5E86: FA CE DB   LD      A,($DBCE)       
5E89: A7         AND     A               
5E8A: 3E 10      LD      A,$10           
5E8C: 28 04      JR      Z,$5E92         
5E8E: F0 F7      LD      A,($F7)         
5E90: C6 08      ADD     $08             
5E92: CD 85 21   CALL    $2185           
5E95: C9         RET                     
5E96: 60         LD      H,B             
5E97: 00         NOP                     
5E98: 62         LD      H,D             
5E99: 00         NOP                     
5E9A: 62         LD      H,D             
5E9B: 20 60      JR      NZ,$5EFD        
5E9D: 20 64      JR      NZ,$5F03        
5E9F: 00         NOP                     
5EA0: 66         LD      H,(HL)          
5EA1: 00         NOP                     
5EA2: 66         LD      H,(HL)          
5EA3: 20 64      JR      NZ,$5F09        
5EA5: 20 68      JR      NZ,$5F0F        
5EA7: 00         NOP                     
5EA8: 6A         LD      L,D             
5EA9: 00         NOP                     
5EAA: 6C         LD      L,H             
5EAB: 00         NOP                     
5EAC: 6E         LD      L,(HL)          
5EAD: 00         NOP                     
5EAE: 6A         LD      L,D             
5EAF: 20 68      JR      NZ,$5F19        
5EB1: 20 6E      JR      NZ,$5F21        
5EB3: 20 6C      JR      NZ,$5F21        
5EB5: 20 FA      JR      NZ,$5EB1        
5EB7: 6B         LD      L,E             
5EB8: DB         ???                     
5EB9: E6 02      AND     $02             
5EBB: CA 76 7E   JP      Z,$7E76         
5EBE: FA 7B DB   LD      A,($DB7B)       
5EC1: A7         AND     A               
5EC2: C2 76 7E   JP      NZ,$7E76        
5EC5: F0 F8      LD      A,($F8)         
5EC7: E6 10      AND     $10             
5EC9: C2 76 7E   JP      NZ,$7E76        
5ECC: 21 C0 C2   LD      HL,$C2C0        
5ECF: 09         ADD     HL,BC           
5ED0: 7E         LD      A,(HL)          
5ED1: A7         AND     A               
5ED2: C2 DD 60   JP      NZ,$60DD        
5ED5: 79         LD      A,C             
5ED6: EA 0F C5   LD      ($C50F),A       
5ED9: 11 96 5E   LD      DE,$5E96        
5EDC: CD 3B 3C   CALL    $3C3B           
5EDF: CD D9 7C   CALL    $7CD9           
5EE2: CD 06 7E   CALL    $7E06           
5EE5: 21 20 C3   LD      HL,$C320        
5EE8: 09         ADD     HL,BC           
5EE9: 35         DEC     (HL)            
5EEA: 35         DEC     (HL)            
5EEB: 21 10 C3   LD      HL,$C310        
5EEE: 09         ADD     HL,BC           
5EEF: 7E         LD      A,(HL)          
5EF0: A7         AND     A               
5EF1: E0 E8      LDFF00  ($E8),A         
5EF3: 28 04      JR      Z,$5EF9         
5EF5: E6 80      AND     $80             
5EF7: 28 06      JR      Z,$5EFF         
5EF9: 70         LD      (HL),B          
5EFA: 21 20 C3   LD      HL,$C320        
5EFD: 09         ADD     HL,BC           
5EFE: 70         LD      (HL),B          
5EFF: F0 F0      LD      A,($F0)         
5F01: C7         RST     0X00            
5F02: 22         LD      (HLI),A         
5F03: 5F         LD      E,A             
5F04: 54         LD      D,H             
5F05: 5F         LD      E,A             
5F06: 62         LD      H,D             
5F07: 5F         LD      E,A             
5F08: 7C         LD      A,H             
5F09: 5F         LD      E,A             
5F0A: AD         XOR     L               
5F0B: 5F         LD      E,A             
5F0C: D1         POP     DE              
5F0D: 5F         LD      E,A             
5F0E: E3         ???                     
5F0F: 5F         LD      E,A             
5F10: FA 5F 12   LD      A,($125F)       
5F13: 60         LD      H,B             
5F14: 35         DEC     (HL)            
5F15: 60         LD      H,B             
5F16: 3D         DEC     A               
5F17: 60         LD      H,B             
5F18: 59         LD      E,C             
5F19: 60         LD      H,B             
5F1A: 7B         LD      A,E             
5F1B: 60         LD      H,B             
5F1C: 21 D0 C3   LD      HL,$C3D0        
5F1F: 09         ADD     HL,BC           
5F20: 70         LD      (HL),B          
5F21: C9         RET                     
5F22: CD 3F 5F   CALL    $5F3F           
5F25: CD 61 7D   CALL    $7D61           
5F28: CD 20 7E   CALL    $7E20           
5F2B: 21 80 C3   LD      HL,$C380        
5F2E: 09         ADD     HL,BC           
5F2F: 73         LD      (HL),E          
5F30: F0 98      LD      A,($98)         
5F32: FE 90      CP      $90             
5F34: 30 08      JR      NC,$5F3E        
5F36: 3E 35      LD      A,$35           
5F38: CD 8E 21   CALL    $218E           
5F3B: CD 8D 3B   CALL    $3B8D           
5F3E: C9         RET                     
5F3F: F0 E8      LD      A,($E8)         
5F41: A7         AND     A               
5F42: 28 03      JR      Z,$5F47         
5F44: E6 80      AND     $80             
5F46: C8         RET     Z               
5F47: F0 E7      LD      A,($E7)         
5F49: E6 3F      AND     $3F             
5F4B: 20 06      JR      NZ,$5F53        
5F4D: 21 20 C3   LD      HL,$C320        
5F50: 09         ADD     HL,BC           
5F51: 36 10      LD      (HL),$10        
5F53: C9         RET                     
5F54: CD 3F 5F   CALL    $5F3F           
5F57: CD 61 7D   CALL    $7D61           
5F5A: 3E 36      LD      A,$36           
5F5C: CD 8E 21   CALL    $218E           
5F5F: C3 8D 3B   JP      $3B8D           
5F62: CD 3F 5F   CALL    $5F3F           
5F65: CD 61 7D   CALL    $7D61           
5F68: CD 20 7E   CALL    $7E20           
5F6B: C6 08      ADD     $08             
5F6D: FE 10      CP      $10             
5F6F: D0         RET     NC              
5F70: CD 30 7E   CALL    $7E30           
5F73: C6 10      ADD     $10             
5F75: FE 20      CP      $20             
5F77: D0         RET     NC              
5F78: CD 8D 3B   CALL    $3B8D           
5F7B: C9         RET                     
5F7C: CD 1C 5F   CALL    $5F1C           
5F7F: CD 61 7D   CALL    $7D61           
5F82: CD 20 7E   CALL    $7E20           
5F85: 21 80 C3   LD      HL,$C380        
5F88: 09         ADD     HL,BC           
5F89: 73         LD      (HL),E          
5F8A: FA A4 C1   LD      A,($C1A4)       
5F8D: A7         AND     A               
5F8E: 28 11      JR      Z,$5FA1         
5F90: F0 98      LD      A,($98)         
5F92: 21 00 C2   LD      HL,$C200        
5F95: 09         ADD     HL,BC           
5F96: C6 10      ADD     $10             
5F98: 77         LD      (HL),A          
5F99: F0 99      LD      A,($99)         
5F9B: 21 10 C2   LD      HL,$C210        
5F9E: 09         ADD     HL,BC           
5F9F: 77         LD      (HL),A          
5FA0: C9         RET                     
5FA1: AF         XOR     A               
5FA2: EA 9B C1   LD      ($C19B),A       
5FA5: CD 91 08   CALL    $0891           
5FA8: 36 10      LD      (HL),$10        
5FAA: C3 8D 3B   JP      $3B8D           
5FAD: CD 1C 5F   CALL    $5F1C           
5FB0: CD 61 7D   CALL    $7D61           
5FB3: 3E 02      LD      A,$02           
5FB5: E0 A1      LDFF00  ($A1),A         
5FB7: EA 67 C1   LD      ($C167),A       
5FBA: 3E 00      LD      A,$00           
5FBC: E0 9E      LDFF00  ($9E),A         
5FBE: C5         PUSH    BC              
5FBF: CD 7C 08   CALL    $087C           
5FC2: C1         POP     BC              
5FC3: CD 91 08   CALL    $0891           
5FC6: 20 08      JR      NZ,$5FD0        
5FC8: 3E 37      LD      A,$37           
5FCA: CD 8E 21   CALL    $218E           
5FCD: CD 8D 3B   CALL    $3B8D           
5FD0: C9         RET                     
5FD1: CD 1C 5F   CALL    $5F1C           
5FD4: CD 61 7D   CALL    $7D61           
5FD7: 3E 02      LD      A,$02           
5FD9: E0 A1      LDFF00  ($A1),A         
5FDB: 3E 38      LD      A,$38           
5FDD: CD 8E 21   CALL    $218E           
5FE0: C3 8D 3B   JP      $3B8D           
5FE3: CD 1C 5F   CALL    $5F1C           
5FE6: 3E 02      LD      A,$02           
5FE8: E0 A1      LDFF00  ($A1),A         
5FEA: CD 61 7D   CALL    $7D61           
5FED: 3E 39      LD      A,$39           
5FEF: CD 8E 21   CALL    $218E           
5FF2: 21 B0 C2   LD      HL,$C2B0        
5FF5: 09         ADD     HL,BC           
5FF6: 70         LD      (HL),B          
5FF7: C3 8D 3B   JP      $3B8D           
5FFA: CD 1C 5F   CALL    $5F1C           
5FFD: 3E 02      LD      A,$02           
5FFF: E0 A1      LDFF00  ($A1),A         
6001: CD 61 7D   CALL    $7D61           
6004: 21 B0 C2   LD      HL,$C2B0        
6007: 09         ADD     HL,BC           
6008: 34         INC     (HL)            
6009: 7E         LD      A,(HL)          
600A: FE A0      CP      $A0             
600C: 20 03      JR      NZ,$6011        
600E: C3 8D 3B   JP      $3B8D           
6011: C9         RET                     
6012: CD 1C 5F   CALL    $5F1C           
6015: 3E 02      LD      A,$02           
6017: E0 A1      LDFF00  ($A1),A         
6019: CD 61 7D   CALL    $7D61           
601C: 3E C2      LD      A,$C2           
601E: CD 01 3C   CALL    $3C01           
6021: 21 00 C2   LD      HL,$C200        
6024: 19         ADD     HL,DE           
6025: 36 12      LD      (HL),$12        
6027: 21 10 C2   LD      HL,$C210        
602A: 19         ADD     HL,DE           
602B: 36 88      LD      (HL),$88        
602D: 21 C0 C2   LD      HL,$C2C0        
6030: 19         ADD     HL,DE           
6031: 34         INC     (HL)            
6032: C3 8D 3B   JP      $3B8D           
6035: CD 1C 5F   CALL    $5F1C           
6038: 3E 02      LD      A,$02           
603A: E0 A1      LDFF00  ($A1),A         
603C: C9         RET                     
603D: 3E 02      LD      A,$02           
603F: E0 A1      LDFF00  ($A1),A         
6041: F0 EC      LD      A,($EC)         
6043: FE 3E      CP      $3E             
6045: 38 03      JR      C,$604A         
6047: C3 8D 3B   JP      $3B8D           
604A: 21 50 C2   LD      HL,$C250        
604D: 09         ADD     HL,BC           
604E: 36 06      LD      (HL),$06        
6050: 21 80 C3   LD      HL,$C380        
6053: 09         ADD     HL,BC           
6054: 36 03      LD      (HL),$03        
6056: C3 D0 7D   JP      $7DD0           
6059: 3E 02      LD      A,$02           
605B: E0 A1      LDFF00  ($A1),A         
605D: 21 40 C2   LD      HL,$C240        
6060: 09         ADD     HL,BC           
6061: 36 FA      LD      (HL),$FA        
6063: 21 80 C3   LD      HL,$C380        
6066: 09         ADD     HL,BC           
6067: 36 01      LD      (HL),$01        
6069: CD DA 7D   CALL    $7DDA           
606C: F0 EE      LD      A,($EE)         
606E: FE 18      CP      $18             
6070: 30 08      JR      NC,$607A        
6072: CD 91 08   CALL    $0891           
6075: 36 60      LD      (HL),$60        
6077: CD 8D 3B   CALL    $3B8D           
607A: C9         RET                     
607B: 3E 02      LD      A,$02           
607D: E0 A1      LDFF00  ($A1),A         
607F: CD 91 08   CALL    $0891           
6082: 28 07      JR      Z,$608B         
6084: 21 80 C3   LD      HL,$C380        
6087: 09         ADD     HL,BC           
6088: 36 02      LD      (HL),$02        
608A: C9         RET                     
608B: 21 40 C2   LD      HL,$C240        
608E: 09         ADD     HL,BC           
608F: 36 F4      LD      (HL),$F4        
6091: 21 80 C3   LD      HL,$C380        
6094: 09         ADD     HL,BC           
6095: 36 01      LD      (HL),$01        
6097: CD DA 7D   CALL    $7DDA           
609A: F0 EE      LD      A,($EE)         
609C: FE F0      CP      $F0             
609E: 20 0F      JR      NZ,$60AF        
60A0: AF         XOR     A               
60A1: EA 67 C1   LD      ($C167),A       
60A4: 21 08 D8   LD      HL,$D808        
60A7: CB E6      SET     1,E             
60A9: 7E         LD      A,(HL)          
60AA: E0 F8      LDFF00  ($F8),A         
60AC: C3 76 7E   JP      $7E76           
60AF: CD 20 7E   CALL    $7E20           
60B2: 7B         LD      A,E             
60B3: EE 01      XOR     $01             
60B5: E0 9E      LDFF00  ($9E),A         
60B7: C5         PUSH    BC              
60B8: CD 7C 08   CALL    $087C           
60BB: C1         POP     BC              
60BC: C9         RET                     
60BD: 50         LD      D,B             
60BE: 00         NOP                     
60BF: 52         LD      D,D             
60C0: 00         NOP                     
60C1: 52         LD      D,D             
60C2: 20 50      JR      NZ,$6114        
60C4: 20 54      JR      NZ,$611A        
60C6: 00         NOP                     
60C7: 56         LD      D,(HL)          
60C8: 00         NOP                     
60C9: 56         LD      D,(HL)          
60CA: 20 54      JR      NZ,$6120        
60CC: 20 58      JR      NZ,$6126        
60CE: 00         NOP                     
60CF: 5A         LD      E,D             
60D0: 00         NOP                     
60D1: 5C         LD      E,H             
60D2: 00         NOP                     
60D3: 5E         LD      E,(HL)          
60D4: 00         NOP                     
60D5: 5A         LD      E,D             
60D6: 20 58      JR      NZ,$6130        
60D8: 20 5E      JR      NZ,$6138        
60DA: 20 5C      JR      NZ,$6138        
60DC: 20 11      JR      NZ,$60EF        
60DE: BD         CP      L               
60DF: 60         LD      H,B             
60E0: CD 3B 3C   CALL    $3C3B           
60E3: CD D9 7C   CALL    $7CD9           
60E6: F0 F0      LD      A,($F0)         
60E8: C7         RST     0X00            
60E9: F1         POP     AF              
60EA: 60         LD      H,B             
60EB: 23         INC     HL              
60EC: 61         LD      H,C             
60ED: 39         ADD     HL,SP           
60EE: 61         LD      H,C             
60EF: 5D         LD      E,L             
60F0: 61         LD      H,C             
60F1: 21 80 C3   LD      HL,$C380        
60F4: 09         ADD     HL,BC           
60F5: 36 02      LD      (HL),$02        
60F7: 21 50 C2   LD      HL,$C250        
60FA: 09         ADD     HL,BC           
60FB: 36 F4      LD      (HL),$F4        
60FD: CD D0 7D   CALL    $7DD0           
6100: F0 EC      LD      A,($EC)         
6102: FE 70      CP      $70             
6104: 30 1C      JR      NC,$6122        
6106: 3E 3B      LD      A,$3B           
6108: CD 8E 21   CALL    $218E           
610B: 3E 03      LD      A,$03           
610D: E0 9E      LDFF00  ($9E),A         
610F: FA 0F C5   LD      A,($C50F)       
6112: 5F         LD      E,A             
6113: 50         LD      D,B             
6114: 21 80 C3   LD      HL,$C380        
6117: 19         ADD     HL,DE           
6118: 36 03      LD      (HL),$03        
611A: C5         PUSH    BC              
611B: CD 7C 08   CALL    $087C           
611E: C1         POP     BC              
611F: CD 8D 3B   CALL    $3B8D           
6122: C9         RET                     
6123: FA 0F C5   LD      A,($C50F)       
6126: 5F         LD      E,A             
6127: 50         LD      D,B             
6128: 21 80 C3   LD      HL,$C380        
612B: 19         ADD     HL,DE           
612C: 36 03      LD      (HL),$03        
612E: CD 61 7D   CALL    $7D61           
6131: 3E 3A      LD      A,$3A           
6133: CD 8E 21   CALL    $218E           
6136: C3 8D 3B   JP      $3B8D           
6139: FA 0F C5   LD      A,($C50F)       
613C: 5F         LD      E,A             
613D: 50         LD      D,B             
613E: 21 80 C3   LD      HL,$C380        
6141: 19         ADD     HL,DE           
6142: 36 03      LD      (HL),$03        
6144: FA 70 C1   LD      A,($C170)       
6147: FE 22      CP      $22             
6149: 38 02      JR      C,$614D         
614B: 36 01      LD      (HL),$01        
614D: CD 61 7D   CALL    $7D61           
6150: FA 0F C5   LD      A,($C50F)       
6153: 5F         LD      E,A             
6154: 50         LD      D,B             
6155: 21 90 C2   LD      HL,$C290        
6158: 19         ADD     HL,DE           
6159: 34         INC     (HL)            
615A: C3 8D 3B   JP      $3B8D           
615D: 21 80 C3   LD      HL,$C380        
6160: 09         ADD     HL,BC           
6161: 36 01      LD      (HL),$01        
6163: 21 40 C2   LD      HL,$C240        
6166: 09         ADD     HL,BC           
6167: 36 F8      LD      (HL),$F8        
6169: CD DA 7D   CALL    $7DDA           
616C: F0 EE      LD      A,($EE)         
616E: FE E0      CP      $E0             
6170: 20 03      JR      NZ,$6175        
6172: CD 76 7E   CALL    $7E76           
6175: C9         RET                     
6176: FA 73 DB   LD      A,($DB73)       
6179: A7         AND     A               
617A: C2 F4 59   JP      NZ,$59F4        
617D: FA 74 DB   LD      A,($DB74)       
6180: A7         AND     A               
6181: C0         RET     NZ              
6182: FA FD D8   LD      A,($D8FD)       
6185: E6 20      AND     $20             
6187: C2 76 7E   JP      NZ,$7E76        
618A: FA 0E DB   LD      A,($DB0E)       
618D: FE 07      CP      $07             
618F: DA 76 7E   JP      C,$7E76         
6192: 11 96 5E   LD      DE,$5E96        
6195: CD 3B 3C   CALL    $3C3B           
6198: FA 24 C1   LD      A,($C124)       
619B: A7         AND     A               
619C: C0         RET     NZ              
619D: CD AF 7C   CALL    $7CAF           
61A0: F0 F0      LD      A,($F0)         
61A2: C7         RST     0X00            
61A3: B1         OR      C               
61A4: 61         LD      H,C             
61A5: BE         CP      (HL)            
61A6: 61         LD      H,C             
61A7: DB         ???                     
61A8: 61         LD      H,C             
61A9: FB         EI                      
61AA: 61         LD      H,C             
61AB: 2E 62      LD      L,$62           
61AD: 3D         DEC     A               
61AE: 62         LD      H,D             
61AF: 52         LD      D,D             
61B0: 62         LD      H,D             
61B1: 3E 4D      LD      A,$4D           
61B3: EA 68 D3   LD      ($D368),A       
61B6: E0 B0      LDFF00  ($B0),A         
61B8: E0 BD      LDFF00  ($BD),A         
61BA: CD 8D 3B   CALL    $3B8D           
61BD: C9         RET                     
61BE: FA 9F C1   LD      A,($C19F)       
61C1: A7         AND     A               
61C2: 20 16      JR      NZ,$61DA        
61C4: CD 30 7E   CALL    $7E30           
61C7: C6 14      ADD     $14             
61C9: FE 28      CP      $28             
61CB: 30 0D      JR      NC,$61DA        
61CD: 3E 01      LD      A,$01           
61CF: EA 67 C1   LD      ($C167),A       
61D2: CD 91 08   CALL    $0891           
61D5: 36 18      LD      (HL),$18        
61D7: CD 8D 3B   CALL    $3B8D           
61DA: C9         RET                     
61DB: FA 9F C1   LD      A,($C19F)       
61DE: A7         AND     A               
61DF: 20 19      JR      NZ,$61FA        
61E1: CD 91 08   CALL    $0891           
61E4: 20 08      JR      NZ,$61EE        
61E6: 3E D5      LD      A,$D5           
61E8: CD 85 21   CALL    $2185           
61EB: CD 8D 3B   CALL    $3B8D           
61EE: 1E 02      LD      E,$02           
61F0: FE 0C      CP      $0C             
61F2: 38 02      JR      C,$61F6         
61F4: 1E 04      LD      E,$04           
61F6: 7B         LD      A,E             
61F7: CD 87 3B   CALL    $3B87           
61FA: C9         RET                     
61FB: FA 9F C1   LD      A,($C19F)       
61FE: A7         AND     A               
61FF: 20 2C      JR      NZ,$622D        
6201: CD 8D 3B   CALL    $3B8D           
6204: FA 77 C1   LD      A,($C177)       
6207: A7         AND     A               
6208: 20 1A      JR      NZ,$6224        
620A: 36 06      LD      (HL),$06        
620C: AF         XOR     A               
620D: EA 6B C1   LD      ($C16B),A       
6210: EA 6C C1   LD      ($C16C),A       
6213: EA 7C D4   LD      ($D47C),A       
6216: EA 96 DB   LD      ($DB96),A       
6219: 3E 09      LD      A,$09           
621B: EA 95 DB   LD      ($DB95),A       
621E: 3E 4E      LD      A,$4E           
6220: EA 68 D3   LD      ($D368),A       
6223: C9         RET                     
6224: AF         XOR     A               
6225: EA 67 C1   LD      ($C167),A       
6228: 3E D6      LD      A,$D6           
622A: CD 85 21   CALL    $2185           
622D: C9         RET                     
622E: FA 9F C1   LD      A,($C19F)       
6231: A7         AND     A               
6232: 20 08      JR      NZ,$623C        
6234: CD 91 08   CALL    $0891           
6237: 36 60      LD      (HL),$60        
6239: CD 8D 3B   CALL    $3B8D           
623C: C9         RET                     
623D: CD 91 08   CALL    $0891           
6240: 20 03      JR      NZ,$6245        
6242: CD 8D 3B   CALL    $3B8D           
6245: 1E 00      LD      E,$00           
6247: FE 54      CP      $54             
6249: 38 02      JR      C,$624D         
624B: 1E 04      LD      E,$04           
624D: 7B         LD      A,E             
624E: CD 87 3B   CALL    $3B87           
6251: C9         RET                     
6252: C9         RET                     
6253: 65         LD      H,L             
6254: 64         LD      H,H             
6255: 54         LD      D,H             
6256: 52         LD      D,D             
6257: 22         LD      (HLI),A         
6258: 22         LD      (HLI),A         
6259: 32         LD      (HLD),A         
625A: 37         SCF                     
625B: 37         SCF                     
625C: 37         SCF                     
625D: 57         LD      D,A             
625E: 56         LD      D,(HL)          
625F: 26 21      LD      H,$21           
6261: C4 C5 D5   CALL    NZ,$D5C5        
6264: D4 C4 C5   CALL    NC,$C5C4        
6267: D5         PUSH    DE              
6268: D5         PUSH    DE              
6269: C5         PUSH    BC              
626A: C4 C4 C5   CALL    NZ,$C5C4        
626D: D5         PUSH    DE              
626E: D4 AB A9   CALL    NC,$A9AB        
6271: AC         XOR     H               
6272: AA         XOR     D               
6273: AB         XOR     E               
6274: A9         XOR     C               
6275: AB         XOR     E               
6276: AA         XOR     D               
6277: AC         XOR     H               
6278: A9         XOR     C               
6279: AB         XOR     E               
627A: A9         XOR     C               
627B: AC         XOR     H               
627C: AE         XOR     (HL)            
627D: CD 61 7D   CALL    $7D61           
6280: F0 F6      LD      A,($F6)         
6282: FE B4      CP      $B4             
6284: 20 07      JR      NZ,$628D        
6286: AF         XOR     A               
6287: EA 72 D4   LD      ($D472),A       
628A: EA 73 D4   LD      ($D473),A       
628D: FA 73 D4   LD      A,($D473)       
6290: A7         AND     A               
6291: 28 4C      JR      Z,$62DF         
6293: FA 72 D4   LD      A,($D472)       
6296: 5F         LD      E,A             
6297: 50         LD      D,B             
6298: 21 53 62   LD      HL,$6253        
629B: 19         ADD     HL,DE           
629C: FA 73 D4   LD      A,($D473)       
629F: BE         CP      (HL)            
62A0: 20 2D      JR      NZ,$62CF        
62A2: 21 61 62   LD      HL,$6261        
62A5: 19         ADD     HL,DE           
62A6: F0 F6      LD      A,($F6)         
62A8: BE         CP      (HL)            
62A9: 20 24      JR      NZ,$62CF        
62AB: AF         XOR     A               
62AC: EA 73 D4   LD      ($D473),A       
62AF: FA 72 D4   LD      A,($D472)       
62B2: 3C         INC     A               
62B3: EA 72 D4   LD      ($D472),A       
62B6: FE 0E      CP      $0E             
62B8: 20 0D      JR      NZ,$62C7        
62BA: AF         XOR     A               
62BB: EA 72 D4   LD      ($D472),A       
62BE: 3E 02      LD      A,$02           
62C0: E0 F2      LDFF00  ($F2),A         
62C2: D5         PUSH    DE              
62C3: CD E0 62   CALL    $62E0           
62C6: D1         POP     DE              
62C7: 21 6F 62   LD      HL,$626F        
62CA: 19         ADD     HL,DE           
62CB: 7E         LD      A,(HL)          
62CC: C3 85 21   JP      $2185           
62CF: AF         XOR     A               
62D0: EA 72 D4   LD      ($D472),A       
62D3: EA 73 D4   LD      ($D473),A       
62D6: 3E 1D      LD      A,$1D           
62D8: E0 F2      LDFF00  ($F2),A         
62DA: 3E AD      LD      A,$AD           
62DC: CD 85 21   CALL    $2185           
62DF: C9         RET                     
62E0: 21 39 D7   LD      HL,$D739        
62E3: 36 C6      LD      (HL),$C6        
62E5: 3E 28      LD      A,$28           
62E7: EA 16 D4   LD      ($D416),A       
62EA: 3E 20      LD      A,$20           
62EC: E0 CD      LDFF00  ($CD),A         
62EE: C6 10      ADD     $10             
62F0: E0 D8      LDFF00  ($D8),A         
62F2: 3E 80      LD      A,$80           
62F4: E0 CE      LDFF00  ($CE),A         
62F6: C6 08      ADD     $08             
62F8: E0 D7      LDFF00  ($D7),A         
62FA: 3E 02      LD      A,$02           
62FC: CD 53 09   CALL    $0953           
62FF: CD 39 28   CALL    $2839           
6302: 21 01 D6   LD      HL,$D601        
6305: FA 00 D6   LD      A,($D600)       
6308: 5F         LD      E,A             
6309: C6 0A      ADD     $0A             
630B: EA 00 D6   LD      ($D600),A       
630E: 16 00      LD      D,$00           
6310: 19         ADD     HL,DE           
6311: F0 CF      LD      A,($CF)         
6313: 22         LD      (HLI),A         
6314: F0 D0      LD      A,($D0)         
6316: 22         LD      (HLI),A         
6317: 3E 81      LD      A,$81           
6319: 22         LD      (HLI),A         
631A: 3E 68      LD      A,$68           
631C: 22         LD      (HLI),A         
631D: 3E 77      LD      A,$77           
631F: 22         LD      (HLI),A         
6320: F0 CF      LD      A,($CF)         
6322: 22         LD      (HLI),A         
6323: F0 D0      LD      A,($D0)         
6325: 3C         INC     A               
6326: 22         LD      (HLI),A         
6327: 3E 81      LD      A,$81           
6329: 22         LD      (HLI),A         
632A: 3E 69      LD      A,$69           
632C: 22         LD      (HLI),A         
632D: 3E 4B      LD      A,$4B           
632F: 22         LD      (HLI),A         
6330: 36 00      LD      (HL),$00        
6332: 3E 01      LD      A,$01           
6334: E0 AC      LDFF00  ($AC),A         
6336: F0 CD      LD      A,($CD)         
6338: E6 F0      AND     $F0             
633A: C6 10      ADD     $10             
633C: E0 AE      LDFF00  ($AE),A         
633E: F0 CE      LD      A,($CE)         
6340: E6 F0      AND     $F0             
6342: C6 08      ADD     $08             
6344: E0 AD      LDFF00  ($AD),A         
6346: F0 F6      LD      A,($F6)         
6348: 5F         LD      E,A             
6349: 16 00      LD      D,$00           
634B: 21 00 D8   LD      HL,$D800        
634E: 19         ADD     HL,DE           
634F: CB E6      SET     1,E             
6351: C9         RET                     
6352: 10 20      STOP    $20             
6354: 30 40      JR      NC,$6396        
6356: 50         LD      D,B             
6357: 60         LD      H,B             
6358: 70         LD      (HL),B          
6359: 80         ADD     A,B             
635A: 18 28      JR      $6384           
635C: 38 48      JR      C,$63A6         
635E: 58         LD      E,B             
635F: 68         LD      L,B             
6360: 78         LD      A,B             
6361: 88         ADC     A,B             
6362: 21 B0 C2   LD      HL,$C2B0        
6365: 09         ADD     HL,BC           
6366: 7E         LD      A,(HL)          
6367: A7         AND     A               
6368: C2 E3 63   JP      NZ,$63E3        
636B: CD 61 7D   CALL    $7D61           
636E: CD 91 08   CALL    $0891           
6371: 20 5B      JR      NZ,$63CE        
6373: CD ED 27   CALL    $27ED           
6376: E6 07      AND     $07             
6378: 5F         LD      E,A             
6379: 50         LD      D,B             
637A: 21 5A 63   LD      HL,$635A        
637D: 19         ADD     HL,DE           
637E: 7E         LD      A,(HL)          
637F: 21 00 C2   LD      HL,$C200        
6382: 09         ADD     HL,BC           
6383: 77         LD      (HL),A          
6384: 21 52 63   LD      HL,$6352        
6387: 19         ADD     HL,DE           
6388: 7E         LD      A,(HL)          
6389: 21 10 C2   LD      HL,$C210        
638C: 09         ADD     HL,BC           
638D: 77         LD      (HL),A          
638E: CD 6E 64   CALL    $646E           
6391: F0 DA      LD      A,($DA)         
6393: FE 00      CP      $00             
6395: 28 09      JR      Z,$63A0         
6397: FE 06      CP      $06             
6399: 28 05      JR      Z,$63A0         
639B: FE 09      CP      $09             
639D: 28 01      JR      Z,$63A0         
639F: C9         RET                     
63A0: CD 91 08   CALL    $0891           
63A3: CD ED 27   CALL    $27ED           
63A6: E6 3F      AND     $3F             
63A8: C6 40      ADD     $40             
63AA: 77         LD      (HL),A          
63AB: 3E BF      LD      A,$BF           
63AD: 1E 05      LD      E,$05           
63AF: CD 13 3C   CALL    $3C13           
63B2: 38 1A      JR      C,$63CE         
63B4: F0 D7      LD      A,($D7)         
63B6: 21 00 C2   LD      HL,$C200        
63B9: 19         ADD     HL,DE           
63BA: 77         LD      (HL),A          
63BB: F0 D8      LD      A,($D8)         
63BD: 21 10 C2   LD      HL,$C210        
63C0: 19         ADD     HL,DE           
63C1: 77         LD      (HL),A          
63C2: 21 B0 C2   LD      HL,$C2B0        
63C5: 19         ADD     HL,DE           
63C6: 36 01      LD      (HL),$01        
63C8: 21 40 C3   LD      HL,$C340        
63CB: 19         ADD     HL,DE           
63CC: CB B6      SET     1,E             
63CE: C9         RET                     
63CF: FF         RST     0X38            
63D0: FF         RST     0X38            
63D1: FF         RST     0X38            
63D2: FF         RST     0X38            
63D3: 6C         LD      L,H             
63D4: 00         NOP                     
63D5: 6C         LD      L,H             
63D6: 20 68      JR      NZ,$6440        
63D8: 00         NOP                     
63D9: 6A         LD      L,D             
63DA: 00         NOP                     
63DB: 60         LD      H,B             
63DC: 00         NOP                     
63DD: 62         LD      H,D             
63DE: 00         NOP                     
63DF: 64         LD      H,H             
63E0: 00         NOP                     
63E1: 66         LD      H,(HL)          
63E2: 00         NOP                     
63E3: 11 CF 63   LD      DE,$63CF        
63E6: CD 3B 3C   CALL    $3C3B           
63E9: CD 61 7D   CALL    $7D61           
63EC: CD 83 7D   CALL    $7D83           
63EF: F0 F0      LD      A,($F0)         
63F1: C7         RST     0X00            
63F2: FA 63 03   LD      A,($0363)       
63F5: 64         LD      H,H             
63F6: 29         ADD     HL,HL           
63F7: 64         LD      H,H             
63F8: 5C         LD      E,H             
63F9: 64         LD      H,H             
63FA: CD 91 08   CALL    $0891           
63FD: 36 30      LD      (HL),$30        
63FF: CD 8D 3B   CALL    $3B8D           
6402: C9         RET                     
6403: CD 91 08   CALL    $0891           
6406: 20 15      JR      NZ,$641D        
6408: CD ED 27   CALL    $27ED           
640B: E6 3F      AND     $3F             
640D: C6 70      ADD     $70             
640F: 77         LD      (HL),A          
6410: CD ED 27   CALL    $27ED           
6413: E6 07      AND     $07             
6415: C6 05      ADD     $05             
6417: CD 25 3C   CALL    $3C25           
641A: CD 8D 3B   CALL    $3B8D           
641D: 1E 01      LD      E,$01           
641F: FE 18      CP      $18             
6421: 30 01      JR      NC,$6424        
6423: 1C         INC     E               
6424: 7B         LD      A,E             
6425: CD 87 3B   CALL    $3B87           
6428: C9         RET                     
6429: CD CD 7D   CALL    $7DCD           
642C: CD 9E 3B   CALL    $3B9E           
642F: CD B4 3B   CALL    $3BB4           
6432: 21 A0 C2   LD      HL,$C2A0        
6435: 09         ADD     HL,BC           
6436: 7E         LD      A,(HL)          
6437: E6 0F      AND     $0F             
6439: 20 05      JR      NZ,$6440        
643B: CD 91 08   CALL    $0891           
643E: 20 0E      JR      NZ,$644E        
6440: CD 91 08   CALL    $0891           
6443: 36 30      LD      (HL),$30        
6445: CD 8D 3B   CALL    $3B8D           
6448: 21 40 C3   LD      HL,$C340        
644B: 09         ADD     HL,BC           
644C: CB F6      SET     1,E             
644E: F0 E7      LD      A,($E7)         
6450: 1F         RRA                     
6451: 1F         RRA                     
6452: 1F         RRA                     
6453: 1F         RRA                     
6454: E6 01      AND     $01             
6456: C6 03      ADD     $03             
6458: CD 87 3B   CALL    $3B87           
645B: C9         RET                     
645C: CD 91 08   CALL    $0891           
645F: CA 76 7E   JP      Z,$7E76         
6462: 1E 01      LD      E,$01           
6464: FE 18      CP      $18             
6466: 38 01      JR      C,$6469         
6468: 1C         INC     E               
6469: 7B         LD      A,E             
646A: CD 87 3B   CALL    $3B87           
646D: C9         RET                     
646E: C5         PUSH    BC              
646F: 21 00 C2   LD      HL,$C200        
6472: 09         ADD     HL,BC           
6473: 7E         LD      A,(HL)          
6474: D6 01      SUB     $01             
6476: E0 DB      LDFF00  ($DB),A         
6478: E6 F0      AND     $F0             
647A: E0 CE      LDFF00  ($CE),A         
647C: CB 37      SET     1,E             
647E: 21 10 C2   LD      HL,$C210        
6481: 09         ADD     HL,BC           
6482: 4F         LD      C,A             
6483: 7E         LD      A,(HL)          
6484: D6 07      SUB     $07             
6486: E0 DC      LDFF00  ($DC),A         
6488: E6 F0      AND     $F0             
648A: E0 CD      LDFF00  ($CD),A         
648C: B1         OR      C               
648D: 4F         LD      C,A             
648E: 06 00      LD      B,$00           
6490: 21 11 D7   LD      HL,$D711        
6493: 7C         LD      A,H             
6494: 09         ADD     HL,BC           
6495: 67         LD      H,A             
6496: C1         POP     BC              
6497: 7E         LD      A,(HL)          
6498: E0 AF      LDFF00  ($AF),A         
649A: 5F         LD      E,A             
649B: FA A5 DB   LD      A,($DBA5)       
649E: 57         LD      D,A             
649F: CD DB 29   CALL    $29DB           
64A2: E0 DA      LDFF00  ($DA),A         
64A4: C9         RET                     
64A5: EC         ???                     
64A6: 14         INC     D               
64A7: CD C6 68   CALL    $68C6           
64AA: F0 EA      LD      A,($EA)         
64AC: FE 01      CP      $01             
64AE: CA 7C 7E   JP      Z,$7E7C         
64B1: CD 61 7D   CALL    $7D61           
64B4: CD 12 3F   CALL    $3F12           
64B7: 21 B0 C2   LD      HL,$C2B0        
64BA: 09         ADD     HL,BC           
64BB: 7E         LD      A,(HL)          
64BC: A7         AND     A               
64BD: 20 06      JR      NZ,$64C5        
64BF: 34         INC     (HL)            
64C0: CD 87 08   CALL    $0887           
64C3: 36 20      LD      (HL),$20        
64C5: CD 8C 08   CALL    $088C           
64C8: 28 1B      JR      Z,$64E5         
64CA: FA 3E C1   LD      A,($C13E)       
64CD: A7         AND     A               
64CE: FE 01      CP      $01             
64D0: 20 05      JR      NZ,$64D7        
64D2: 21 F2 FF   LD      HL,$FFF2        
64D5: 36 33      LD      (HL),$33        
64D7: A7         AND     A               
64D8: 20 0B      JR      NZ,$64E5        
64DA: 3E 02      LD      A,$02           
64DC: E0 A1      LDFF00  ($A1),A         
64DE: 3E 6A      LD      A,$6A           
64E0: E0 9D      LDFF00  ($9D),A         
64E2: CD 90 69   CALL    $6990           
64E5: CD 83 7D   CALL    $7D83           
64E8: CD E0 3B   CALL    $3BE0           
64EB: FA 3E C1   LD      A,($C13E)       
64EE: A7         AND     A               
64EF: 20 03      JR      NZ,$64F4        
64F1: CD B4 3B   CALL    $3BB4           
64F4: CD CD 7D   CALL    $7DCD           
64F7: CD 9E 3B   CALL    $3B9E           
64FA: CD 06 7E   CALL    $7E06           
64FD: 21 20 C3   LD      HL,$C320        
6500: 09         ADD     HL,BC           
6501: 35         DEC     (HL)            
6502: 35         DEC     (HL)            
6503: 35         DEC     (HL)            
6504: 21 10 C3   LD      HL,$C310        
6507: 09         ADD     HL,BC           
6508: 7E         LD      A,(HL)          
6509: E6 80      AND     $80             
650B: E0 E8      LDFF00  ($E8),A         
650D: A7         AND     A               
650E: 28 09      JR      Z,$6519         
6510: 70         LD      (HL),B          
6511: 21 20 C3   LD      HL,$C320        
6514: 09         ADD     HL,BC           
6515: 70         LD      (HL),B          
6516: CD AF 3D   CALL    $3DAF           
6519: CD AB 65   CALL    $65AB           
651C: CD 20 7E   CALL    $7E20           
651F: 21 80 C3   LD      HL,$C380        
6522: 09         ADD     HL,BC           
6523: 73         LD      (HL),E          
6524: CD 30 7E   CALL    $7E30           
6527: FE 00      CP      $00             
6529: 28 0B      JR      Z,$6536         
652B: 50         LD      D,B             
652C: 21 A3 64   LD      HL,$64A3        
652F: 19         ADD     HL,DE           
6530: 7E         LD      A,(HL)          
6531: 21 50 C2   LD      HL,$C250        
6534: 09         ADD     HL,BC           
6535: 77         LD      (HL),A          
6536: F0 E8      LD      A,($E8)         
6538: A7         AND     A               
6539: 28 28      JR      Z,$6563         
653B: 21 20 C3   LD      HL,$C320        
653E: 09         ADD     HL,BC           
653F: 36 10      LD      (HL),$10        
6541: CD ED 27   CALL    $27ED           
6544: E6 0F      AND     $0F             
6546: D6 08      SUB     $08             
6548: 21 40 C2   LD      HL,$C240        
654B: 09         ADD     HL,BC           
654C: 77         LD      (HL),A          
654D: CD 20 7E   CALL    $7E20           
6550: C6 28      ADD     $28             
6552: FE 50      CP      $50             
6554: 38 0D      JR      C,$6563         
6556: 3E 08      LD      A,$08           
6558: CD 30 3C   CALL    $3C30           
655B: F0 D8      LD      A,($D8)         
655D: 21 40 C2   LD      HL,$C240        
6560: 09         ADD     HL,BC           
6561: 86         ADD     A,(HL)          
6562: 77         LD      (HL),A          
6563: CD 72 65   CALL    $6572           
6566: F0 E7      LD      A,($E7)         
6568: 1F         RRA                     
6569: 1F         RRA                     
656A: 1F         RRA                     
656B: 1F         RRA                     
656C: E6 01      AND     $01             
656E: CD 87 3B   CALL    $3B87           
6571: C9         RET                     
6572: CD 8C 08   CALL    $088C           
6575: 28 04      JR      Z,$657B         
6577: 3E 03      LD      A,$03           
6579: 18 19      JR      $6594           
657B: CD 87 08   CALL    $0887           
657E: 20 2A      JR      NZ,$65AA        
6580: 21 B0 C2   LD      HL,$C2B0        
6583: 09         ADD     HL,BC           
6584: 7E         LD      A,(HL)          
6585: FE 05      CP      $05             
6587: 30 05      JR      NC,$658E        
6589: 34         INC     (HL)            
658A: 3E 01      LD      A,$01           
658C: 18 06      JR      $6594           
658E: CD ED 27   CALL    $27ED           
6591: E6 03      AND     $03             
6593: 3C         INC     A               
6594: EA 05 D2   LD      ($D205),A       
6597: FE 01      CP      $01             
6599: 20 04      JR      NZ,$659F        
659B: 3E 0A      LD      A,$0A           
659D: E0 F4      LDFF00  ($F4),A         
659F: CD 91 08   CALL    $0891           
65A2: 36 00      LD      (HL),$00        
65A4: 21 D0 C3   LD      HL,$C3D0        
65A7: 09         ADD     HL,BC           
65A8: 36 00      LD      (HL),$00        
65AA: C9         RET                     
65AB: FA 05 D2   LD      A,($D205)       
65AE: A7         AND     A               
65AF: C8         RET     Z               
65B0: D1         POP     DE              
65B1: 3D         DEC     A               
65B2: C7         RST     0X00            
65B3: C8         RET     Z               
65B4: 65         LD      H,L             
65B5: 1F         RRA                     
65B6: 66         LD      H,(HL)          
65B7: A9         XOR     C               
65B8: 66         LD      H,(HL)          
65B9: C8         RET     Z               
65BA: 65         LD      H,L             
65BB: 01 01 01   LD      BC,$0101        
65BE: 02         LD      (BC),A          
65BF: 02         LD      (BC),A          
65C0: 03         INC     BC              
65C1: 03         INC     BC              
65C2: 03         INC     BC              
65C3: 03         INC     BC              
65C4: 03         INC     BC              
65C5: 02         LD      (BC),A          
65C6: 02         LD      (BC),A          
65C7: 01 CD 91   LD      BC,$91CD        
65CA: 08 20 1A   LD      ($1A20),SP      
65CD: 21 D0 C3   LD      HL,$C3D0        
65D0: 09         ADD     HL,BC           
65D1: 7E         LD      A,(HL)          
65D2: FE 0D      CP      $0D             
65D4: CA E8 65   JP      Z,$65E8         
65D7: 34         INC     (HL)            
65D8: 5F         LD      E,A             
65D9: 50         LD      D,B             
65DA: 21 BB 65   LD      HL,$65BB        
65DD: 19         ADD     HL,DE           
65DE: 7E         LD      A,(HL)          
65DF: CD 87 3B   CALL    $3B87           
65E2: CD 91 08   CALL    $0891           
65E5: 36 01      LD      (HL),$01        
65E7: C9         RET                     
65E8: CD ED 27   CALL    $27ED           
65EB: E6 03      AND     $03             
65ED: CA 06 67   JP      Z,$6706         
65F0: 3E 01      LD      A,$01           
65F2: C3 94 65   JP      $6594           
65F5: 04         INC     B               
65F6: 05         DEC     B               
65F7: 05         DEC     B               
65F8: 05         DEC     B               
65F9: 05         DEC     B               
65FA: 05         DEC     B               
65FB: 05         DEC     B               
65FC: 05         DEC     B               
65FD: 05         DEC     B               
65FE: 05         DEC     B               
65FF: 05         DEC     B               
6600: 06 07      LD      B,$07           
6602: 08 08 08   LD      ($0808),SP      
6605: 08 08 07   LD      ($0708),SP      
6608: 06 01      LD      B,$01           
660A: 08 10 08   LD      ($0810),SP      
660D: 08 02 00   LD      ($0002),SP      
6610: 00         NOP                     
6611: 00         NOP                     
6612: FC         ???                     
6613: F8 F0      LDHL    SP,$F0          
6615: F8 E0      LDHL    SP,$E0          
6617: 90         SUB     B               
6618: A0         AND     B               
6619: 00         NOP                     
661A: 00         NOP                     
661B: 00         NOP                     
661C: 00         NOP                     
661D: 00         NOP                     
661E: 00         NOP                     
661F: CD 91 08   CALL    $0891           
6622: 20 30      JR      NZ,$6654        
6624: 21 D0 C3   LD      HL,$C3D0        
6627: 09         ADD     HL,BC           
6628: 7E         LD      A,(HL)          
6629: FE 15      CP      $15             
662B: CA 06 67   JP      Z,$6706         
662E: 34         INC     (HL)            
662F: 5F         LD      E,A             
6630: 50         LD      D,B             
6631: 21 F5 65   LD      HL,$65F5        
6634: 19         ADD     HL,DE           
6635: 7E         LD      A,(HL)          
6636: CD 87 3B   CALL    $3B87           
6639: 21 0A 66   LD      HL,$660A        
663C: 19         ADD     HL,DE           
663D: 5E         LD      E,(HL)          
663E: 21 80 C3   LD      HL,$C380        
6641: 09         ADD     HL,BC           
6642: 7E         LD      A,(HL)          
6643: A7         AND     A               
6644: 20 04      JR      NZ,$664A        
6646: 7B         LD      A,E             
6647: 2F         CPL                     
6648: 3C         INC     A               
6649: 5F         LD      E,A             
664A: 21 40 C2   LD      HL,$C240        
664D: 09         ADD     HL,BC           
664E: 73         LD      (HL),E          
664F: CD 91 08   CALL    $0891           
6652: 36 03      LD      (HL),$03        
6654: C9         RET                     
6655: 09         ADD     HL,BC           
6656: 09         ADD     HL,BC           
6657: 0A         LD      A,(BC)          
6658: 0A         LD      A,(BC)          
6659: 0B         DEC     BC              
665A: 0B         DEC     BC              
665B: 0C         INC     C               
665C: 0C         INC     C               
665D: 09         ADD     HL,BC           
665E: 09         ADD     HL,BC           
665F: 0A         LD      A,(BC)          
6660: 0A         LD      A,(BC)          
6661: 0B         DEC     BC              
6662: 0B         DEC     BC              
6663: 0C         INC     C               
6664: 0C         INC     C               
6665: 09         ADD     HL,BC           
6666: 09         ADD     HL,BC           
6667: 0A         LD      A,(BC)          
6668: 0A         LD      A,(BC)          
6669: 0B         DEC     BC              
666A: 0B         DEC     BC              
666B: 0C         INC     C               
666C: 0C         INC     C               
666D: 09         ADD     HL,BC           
666E: 09         ADD     HL,BC           
666F: 09         ADD     HL,BC           
6670: 09         ADD     HL,BC           
6671: 09         ADD     HL,BC           
6672: 09         ADD     HL,BC           
6673: 09         ADD     HL,BC           
6674: 09         ADD     HL,BC           
6675: 09         ADD     HL,BC           
6676: 09         ADD     HL,BC           
6677: 0D         DEC     C               
6678: 0E 0F      LD      C,$0F           
667A: 10 11      STOP    $11             
667C: 11 11 01   LD      DE,$0111        
667F: 0C         INC     C               
6680: 0C         INC     C               
6681: 0C         INC     C               
6682: 0C         INC     C               
6683: 0C         INC     C               
6684: 0C         INC     C               
6685: 0C         INC     C               
6686: 0C         INC     C               
6687: 08 08 08   LD      ($0808),SP      
668A: 08 08 08   LD      ($0808),SP      
668D: 08 08 00   LD      ($0008),SP      
6690: 00         NOP                     
6691: 00         NOP                     
6692: 00         NOP                     
6693: 00         NOP                     
6694: 00         NOP                     
6695: 00         NOP                     
6696: 00         NOP                     
6697: 00         NOP                     
6698: 00         NOP                     
6699: 00         NOP                     
669A: 00         NOP                     
669B: 00         NOP                     
669C: 00         NOP                     
669D: 00         NOP                     
669E: 00         NOP                     
669F: F0 E0      LD      A,($E0)         
66A1: D0         RET     NC              
66A2: C0         RET     NZ              
66A3: C0         RET     NZ              
66A4: E0 F0      LDFF00  ($F0),A         
66A6: 00         NOP                     
66A7: 00         NOP                     
66A8: 00         NOP                     
66A9: CD 91 08   CALL    $0891           
66AC: 20 57      JR      NZ,$6705        
66AE: 21 D0 C3   LD      HL,$C3D0        
66B1: 09         ADD     HL,BC           
66B2: 7E         LD      A,(HL)          
66B3: FE 2A      CP      $2A             
66B5: CA 06 67   JP      Z,$6706         
66B8: 5F         LD      E,A             
66B9: FE 28      CP      $28             
66BB: 20 07      JR      NZ,$66C4        
66BD: FA 1C C1   LD      A,($C11C)       
66C0: FE 0A      CP      $0A             
66C2: 28 01      JR      Z,$66C5         
66C4: 34         INC     (HL)            
66C5: 50         LD      D,B             
66C6: 21 55 66   LD      HL,$6655        
66C9: 19         ADD     HL,DE           
66CA: 7E         LD      A,(HL)          
66CB: CD 87 3B   CALL    $3B87           
66CE: 21 7F 66   LD      HL,$667F        
66D1: 19         ADD     HL,DE           
66D2: 5E         LD      E,(HL)          
66D3: 21 80 C3   LD      HL,$C380        
66D6: 09         ADD     HL,BC           
66D7: 7E         LD      A,(HL)          
66D8: A7         AND     A               
66D9: 20 04      JR      NZ,$66DF        
66DB: 7B         LD      A,E             
66DC: 2F         CPL                     
66DD: 3C         INC     A               
66DE: 5F         LD      E,A             
66DF: 21 40 C2   LD      HL,$C240        
66E2: 09         ADD     HL,BC           
66E3: 73         LD      (HL),E          
66E4: CD 8C 08   CALL    $088C           
66E7: 28 17      JR      Z,$6700         
66E9: CD 20 7E   CALL    $7E20           
66EC: C6 30      ADD     $30             
66EE: FE 60      CP      $60             
66F0: 38 0E      JR      C,$6700         
66F2: 21 D0 C3   LD      HL,$C3D0        
66F5: 09         ADD     HL,BC           
66F6: 7E         LD      A,(HL)          
66F7: FE 18      CP      $18             
66F9: 30 05      JR      NC,$6700        
66FB: 3E 10      LD      A,$10           
66FD: CD 25 3C   CALL    $3C25           
6700: CD 91 08   CALL    $0891           
6703: 36 03      LD      (HL),$03        
6705: C9         RET                     
6706: AF         XOR     A               
6707: EA 05 D2   LD      ($D205),A       
670A: CD 87 08   CALL    $0887           
670D: CD ED 27   CALL    $27ED           
6710: E6 0F      AND     $0F             
6712: C6 0C      ADD     $0C             
6714: 77         LD      (HL),A          
6715: C9         RET                     
6716: 00         NOP                     
6717: F8 6C      LDHL    SP,$6C          
6719: 00         NOP                     
671A: 00         NOP                     
671B: 00         NOP                     
671C: 6E         LD      L,(HL)          
671D: 00         NOP                     
671E: 00         NOP                     
671F: 00         NOP                     
6720: 60         LD      H,B             
6721: 00         NOP                     
6722: 00         NOP                     
6723: 08 62 00   LD      ($0062),SP      
6726: FD         ???                     
6727: F8 6E      LDHL    SP,$6E          
6729: 20 FD      JR      NZ,$6728        
672B: 00         NOP                     
672C: 6C         LD      L,H             
672D: 20 FF      JR      NZ,$672E        
672F: F8 6C      LDHL    SP,$6C          
6731: 00         NOP                     
6732: FF         RST     0X38            
6733: 00         NOP                     
6734: 6E         LD      L,(HL)          
6735: 00         NOP                     
6736: 00         NOP                     
6737: 00         NOP                     
6738: 64         LD      H,H             
6739: 00         NOP                     
673A: 00         NOP                     
673B: 08 66 00   LD      ($0066),SP      
673E: FD         ???                     
673F: F8 6E      LDHL    SP,$6E          
6741: 20 FD      JR      NZ,$6740        
6743: 00         NOP                     
6744: 6C         LD      L,H             
6745: 20 00      JR      NZ,$6747        
6747: F8 6E      LDHL    SP,$6E          
6749: 20 00      JR      NZ,$674B        
674B: 00         NOP                     
674C: 6C         LD      L,H             
674D: 20 00      JR      NZ,$674F        
674F: 00         NOP                     
6750: 60         LD      H,B             
6751: 00         NOP                     
6752: 00         NOP                     
6753: 08 62 00   LD      ($0062),SP      
6756: FD         ???                     
6757: F8 6C      LDHL    SP,$6C          
6759: 00         NOP                     
675A: FD         ???                     
675B: 00         NOP                     
675C: 6E         LD      L,(HL)          
675D: 00         NOP                     
675E: FD         ???                     
675F: F0 6C      LD      A,($6C)         
6761: 00         NOP                     
6762: FD         ???                     
6763: F8 6E      LDHL    SP,$6E          
6765: 00         NOP                     
6766: 00         NOP                     
6767: F8 6E      LDHL    SP,$6E          
6769: 20 00      JR      NZ,$676B        
676B: 00         NOP                     
676C: 6C         LD      L,H             
676D: 20 00      JR      NZ,$676F        
676F: 00         NOP                     
6770: 60         LD      H,B             
6771: 00         NOP                     
6772: 00         NOP                     
6773: 08 62 00   LD      ($0062),SP      
6776: 00         NOP                     
6777: 00         NOP                     
6778: 6E         LD      L,(HL)          
6779: 20 00      JR      NZ,$677B        
677B: 08 6C 20   LD      ($206C),SP      
677E: 00         NOP                     
677F: 00         NOP                     
6780: 64         LD      H,H             
6781: 00         NOP                     
6782: 00         NOP                     
6783: 08 66 00   LD      ($0066),SP      
6786: FD         ???                     
6787: F8 6E      LDHL    SP,$6E          
6789: 20 FD      JR      NZ,$6788        
678B: 00         NOP                     
678C: 6C         LD      L,H             
678D: 20 FD      JR      NZ,$678C        
678F: 08 6E 20   LD      ($206E),SP      
6792: FD         ???                     
6793: 10 6C      STOP    $6C             
6795: 20 00      JR      NZ,$6797        
6797: 00         NOP                     
6798: 68         LD      L,B             
6799: 00         NOP                     
679A: 00         NOP                     
679B: 08 6A 00   LD      ($006A),SP      
679E: FD         ???                     
679F: F8 6E      LDHL    SP,$6E          
67A1: 20 FD      JR      NZ,$67A0        
67A3: 00         NOP                     
67A4: 6C         LD      L,H             
67A5: 20 00      JR      NZ,$67A7        
67A7: F8 6C      LDHL    SP,$6C          
67A9: 00         NOP                     
67AA: 00         NOP                     
67AB: 00         NOP                     
67AC: 6E         LD      L,(HL)          
67AD: 00         NOP                     
67AE: 00         NOP                     
67AF: 00         NOP                     
67B0: 60         LD      H,B             
67B1: 00         NOP                     
67B2: 00         NOP                     
67B3: 08 62 00   LD      ($0062),SP      
67B6: 00         NOP                     
67B7: 00         NOP                     
67B8: FF         RST     0X38            
67B9: 00         NOP                     
67BA: 00         NOP                     
67BB: 00         NOP                     
67BC: FF         RST     0X38            
67BD: 00         NOP                     
67BE: 00         NOP                     
67BF: F0 6C      LD      A,($6C)         
67C1: 00         NOP                     
67C2: 00         NOP                     
67C3: F8 6E      LDHL    SP,$6E          
67C5: 00         NOP                     
67C6: 00         NOP                     
67C7: 00         NOP                     
67C8: 60         LD      H,B             
67C9: 00         NOP                     
67CA: 00         NOP                     
67CB: 08 62 00   LD      ($0062),SP      
67CE: 00         NOP                     
67CF: 00         NOP                     
67D0: FF         RST     0X38            
67D1: 00         NOP                     
67D2: 00         NOP                     
67D3: 00         NOP                     
67D4: FF         RST     0X38            
67D5: 00         NOP                     
67D6: 00         NOP                     
67D7: E8 6C      ADD     SP,$6C          
67D9: 00         NOP                     
67DA: 00         NOP                     
67DB: F0 6E      LD      A,($6E)         
67DD: 00         NOP                     
67DE: 00         NOP                     
67DF: 00         NOP                     
67E0: 60         LD      H,B             
67E1: 00         NOP                     
67E2: 00         NOP                     
67E3: 08 62 00   LD      ($0062),SP      
67E6: 00         NOP                     
67E7: 00         NOP                     
67E8: FF         RST     0X38            
67E9: 00         NOP                     
67EA: 00         NOP                     
67EB: 00         NOP                     
67EC: FF         RST     0X38            
67ED: 00         NOP                     
67EE: F8 10      LDHL    SP,$10          
67F0: 6C         LD      L,H             
67F1: 00         NOP                     
67F2: F8 18      LDHL    SP,$18          
67F4: 6E         LD      L,(HL)          
67F5: 00         NOP                     
67F6: 00         NOP                     
67F7: 00         NOP                     
67F8: 68         LD      L,B             
67F9: 00         NOP                     
67FA: 00         NOP                     
67FB: 08 6A 00   LD      ($006A),SP      
67FE: FD         ???                     
67FF: F8 6E      LDHL    SP,$6E          
6801: 20 FD      JR      NZ,$6800        
6803: 00         NOP                     
6804: 6C         LD      L,H             
6805: 20 F0      JR      NZ,$67F7        
6807: 08 6C 00   LD      ($006C),SP      
680A: F0 10      LD      A,($10)         
680C: 6E         LD      L,(HL)          
680D: 00         NOP                     
680E: 00         NOP                     
680F: 00         NOP                     
6810: 68         LD      L,B             
6811: 00         NOP                     
6812: 00         NOP                     
6813: 08 6A 00   LD      ($006A),SP      
6816: FD         ???                     
6817: F8 6E      LDHL    SP,$6E          
6819: 20 FD      JR      NZ,$6818        
681B: 00         NOP                     
681C: 6C         LD      L,H             
681D: 20 FC      JR      NZ,$681B        
681F: 08 6E 20   LD      ($206E),SP      
6822: FC         ???                     
6823: 10 6C      STOP    $6C             
6825: 20 00      JR      NZ,$6827        
6827: 00         NOP                     
6828: 68         LD      L,B             
6829: 00         NOP                     
682A: 00         NOP                     
682B: 08 6A 00   LD      ($006A),SP      
682E: FD         ???                     
682F: F8 6E      LDHL    SP,$6E          
6831: 20 FD      JR      NZ,$6830        
6833: 00         NOP                     
6834: 6C         LD      L,H             
6835: 20 00      JR      NZ,$6837        
6837: 10 6E      STOP    $6E             
6839: 20 00      JR      NZ,$683B        
683B: 18 6C      JR      $68A9           
683D: 20 00      JR      NZ,$683F        
683F: 00         NOP                     
6840: 68         LD      L,B             
6841: 00         NOP                     
6842: 00         NOP                     
6843: 08 6A 00   LD      ($006A),SP      
6846: FD         ???                     
6847: F8 6E      LDHL    SP,$6E          
6849: 20 FD      JR      NZ,$6848        
684B: 00         NOP                     
684C: 6C         LD      L,H             
684D: 20 04      JR      NZ,$6853        
684F: 08 6E 20   LD      ($206E),SP      
6852: 04         INC     B               
6853: 10 6C      STOP    $6C             
6855: 20 00      JR      NZ,$6857        
6857: 00         NOP                     
6858: 68         LD      L,B             
6859: 00         NOP                     
685A: 00         NOP                     
685B: 08 6A 00   LD      ($006A),SP      
685E: FD         ???                     
685F: F8 6E      LDHL    SP,$6E          
6861: 20 FD      JR      NZ,$6860        
6863: 00         NOP                     
6864: 6C         LD      L,H             
6865: 20 08      JR      NZ,$686F        
6867: 00         NOP                     
6868: 6C         LD      L,H             
6869: 00         NOP                     
686A: 08 08 6E   LD      ($6E08),SP      
686D: 00         NOP                     
686E: 00         NOP                     
686F: 00         NOP                     
6870: 64         LD      H,H             
6871: 00         NOP                     
6872: 00         NOP                     
6873: 08 66 00   LD      ($0066),SP      
6876: 00         NOP                     
6877: 00         NOP                     
6878: FF         RST     0X38            
6879: 00         NOP                     
687A: 00         NOP                     
687B: 00         NOP                     
687C: FF         RST     0X38            
687D: 00         NOP                     
687E: 08 F8 6C   LD      ($6CF8),SP      
6881: 00         NOP                     
6882: 08 00 6E   LD      ($6E00),SP      
6885: 00         NOP                     
6886: 00         NOP                     
6887: 00         NOP                     
6888: 60         LD      H,B             
6889: 00         NOP                     
688A: 00         NOP                     
688B: 08 62 00   LD      ($0062),SP      
688E: 00         NOP                     
688F: 00         NOP                     
6890: FF         RST     0X38            
6891: 00         NOP                     
6892: 00         NOP                     
6893: 00         NOP                     
6894: FF         RST     0X38            
6895: 00         NOP                     
6896: 05         DEC     B               
6897: F0 6C      LD      A,($6C)         
6899: 00         NOP                     
689A: 05         DEC     B               
689B: F8 6E      LDHL    SP,$6E          
689D: 00         NOP                     
689E: 00         NOP                     
689F: 00         NOP                     
68A0: 60         LD      H,B             
68A1: 00         NOP                     
68A2: 00         NOP                     
68A3: 08 62 00   LD      ($0062),SP      
68A6: 00         NOP                     
68A7: 00         NOP                     
68A8: FF         RST     0X38            
68A9: 00         NOP                     
68AA: 00         NOP                     
68AB: 00         NOP                     
68AC: FF         RST     0X38            
68AD: 00         NOP                     
68AE: F4         ???                     
68AF: F0 6E      LD      A,($6E)         
68B1: 20 F4      JR      NZ,$68A7        
68B3: F8 6C      LDHL    SP,$6C          
68B5: 20 00      JR      NZ,$68B7        
68B7: 00         NOP                     
68B8: 60         LD      H,B             
68B9: 00         NOP                     
68BA: 00         NOP                     
68BB: 08 62 00   LD      ($0062),SP      
68BE: 00         NOP                     
68BF: 00         NOP                     
68C0: FF         RST     0X38            
68C1: 00         NOP                     
68C2: 00         NOP                     
68C3: 00         NOP                     
68C4: FF         RST     0X38            
68C5: 00         NOP                     
68C6: 3E 80      LD      A,$80           
68C8: EA C0 D5   LD      ($D5C0),A       
68CB: EA C2 D5   LD      ($D5C2),A       
68CE: F0 F1      LD      A,($F1)         
68D0: CB 27      SET     1,E             
68D2: CB 27      SET     1,E             
68D4: 50         LD      D,B             
68D5: CB 27      SET     1,E             
68D7: 5F         LD      E,A             
68D8: CB 12      SET     1,E             
68DA: CB 27      SET     1,E             
68DC: CB 12      SET     1,E             
68DE: 83         ADD     A,E             
68DF: 5F         LD      E,A             
68E0: 7A         LD      A,D             
68E1: CE 00      ADC     $00             
68E3: 57         LD      D,A             
68E4: AF         XOR     A               
68E5: E0 E8      LDFF00  ($E8),A         
68E7: 21 80 C3   LD      HL,$C380        
68EA: 09         ADD     HL,BC           
68EB: 7E         LD      A,(HL)          
68EC: A7         AND     A               
68ED: 20 08      JR      NZ,$68F7        
68EF: 3C         INC     A               
68F0: E0 E8      LDFF00  ($E8),A         
68F2: 21 ED FF   LD      HL,$FFED        
68F5: CB EE      SET     1,E             
68F7: 21 16 67   LD      HL,$6716        
68FA: 19         ADD     HL,DE           
68FB: 0E 06      LD      C,$06           
68FD: E5         PUSH    HL              
68FE: FA C0 C3   LD      A,($C3C0)       
6901: 5F         LD      E,A             
6902: 16 00      LD      D,$00           
6904: 21 30 C0   LD      HL,$C030        
6907: 19         ADD     HL,DE           
6908: E5         PUSH    HL              
6909: D1         POP     DE              
690A: E1         POP     HL              
690B: 79         LD      A,C             
690C: E0 D7      LDFF00  ($D7),A         
690E: FA 23 C1   LD      A,($C123)       
6911: 4F         LD      C,A             
6912: CD 87 3D   CALL    $3D87           
6915: F0 D7      LD      A,($D7)         
6917: 4F         LD      C,A             
6918: FA C2 D5   LD      A,($D5C2)       
691B: FE 80      CP      $80             
691D: 20 06      JR      NZ,$6925        
691F: 7E         LD      A,(HL)          
6920: C6 08      ADD     $08             
6922: EA C2 D5   LD      ($D5C2),A       
6925: F0 EC      LD      A,($EC)         
6927: 86         ADD     A,(HL)          
6928: 12         LD      (DE),A          
6929: 23         INC     HL              
692A: 13         INC     DE              
692B: C5         PUSH    BC              
692C: FA 55 C1   LD      A,($C155)       
692F: 4F         LD      C,A             
6930: 46         LD      B,(HL)          
6931: F0 E8      LD      A,($E8)         
6933: A7         AND     A               
6934: 28 06      JR      Z,$693C         
6936: 78         LD      A,B             
6937: 2F         CPL                     
6938: 3C         INC     A               
6939: C6 08      ADD     $08             
693B: 47         LD      B,A             
693C: FA C0 D5   LD      A,($D5C0)       
693F: FE 80      CP      $80             
6941: 20 0B      JR      NZ,$694E        
6943: F0 E8      LD      A,($E8)         
6945: A7         AND     A               
6946: 78         LD      A,B             
6947: 20 02      JR      NZ,$694B        
6949: C6 08      ADD     $08             
694B: EA C0 D5   LD      ($D5C0),A       
694E: F0 EE      LD      A,($EE)         
6950: 80         ADD     A,B             
6951: 91         SUB     C               
6952: 12         LD      (DE),A          
6953: 23         INC     HL              
6954: 13         INC     DE              
6955: C1         POP     BC              
6956: 2A         LD      A,(HLI)         
6957: 12         LD      (DE),A          
6958: FE FF      CP      $FF             
695A: 20 04      JR      NZ,$6960        
695C: 1B         DEC     DE              
695D: AF         XOR     A               
695E: 12         LD      (DE),A          
695F: 13         INC     DE              
6960: 13         INC     DE              
6961: F0 ED      LD      A,($ED)         
6963: AE         XOR     (HL)            
6964: 23         INC     HL              
6965: 12         LD      (DE),A          
6966: 13         INC     DE              
6967: 0D         DEC     C               
6968: 20 AE      JR      NZ,$6918        
696A: 3E 08      LD      A,$08           
696C: EA C1 D5   LD      ($D5C1),A       
696F: 3E 04      LD      A,$04           
6971: EA C3 D5   LD      ($D5C3),A       
6974: FA 23 C1   LD      A,($C123)       
6977: 4F         LD      C,A             
6978: 3E 06      LD      A,$06           
697A: CD D0 3D   CALL    $3DD0           
697D: C3 19 3D   JP      $3D19           
6980: 00         NOP                     
6981: FE FD      CP      $FD             
6983: FE 00      CP      $00             
6985: 02         LD      (BC),A          
6986: 03         INC     BC              
6987: 02         LD      (BC),A          
6988: 00         NOP                     
6989: 04         INC     B               
698A: 08 0C 10   LD      ($100C),SP      
698D: 0C         INC     C               
698E: 08 04 21   LD      ($2104),SP      
6991: 10 C0      STOP    $C0             
6993: F0 E7      LD      A,($E7)         
6995: 1F         RRA                     
6996: 1F         RRA                     
6997: 1F         RRA                     
6998: F5         PUSH    AF              
6999: E6 07      AND     $07             
699B: CD A3 69   CALL    $69A3           
699E: F1         POP     AF              
699F: C6 04      ADD     $04             
69A1: E6 07      AND     $07             
69A3: C5         PUSH    BC              
69A4: E5         PUSH    HL              
69A5: 5F         LD      E,A             
69A6: 16 00      LD      D,$00           
69A8: 21 80 69   LD      HL,$6980        
69AB: 19         ADD     HL,DE           
69AC: 46         LD      B,(HL)          
69AD: 21 88 69   LD      HL,$6988        
69B0: 19         ADD     HL,DE           
69B1: 4E         LD      C,(HL)          
69B2: E1         POP     HL              
69B3: F0 99      LD      A,($99)         
69B5: 80         ADD     A,B             
69B6: C6 F6      ADD     $F6             
69B8: 22         LD      (HLI),A         
69B9: F0 98      LD      A,($98)         
69BB: 81         ADD     A,C             
69BC: C6 FC      ADD     $FC             
69BE: 22         LD      (HLI),A         
69BF: 36 24      LD      (HL),$24        
69C1: 23         INC     HL              
69C2: 36 00      LD      (HL),$00        
69C4: 23         INC     HL              
69C5: C1         POP     BC              
69C6: C9         RET                     
69C7: 21 B0 C2   LD      HL,$C2B0        
69CA: 09         ADD     HL,BC           
69CB: 7E         LD      A,(HL)          
69CC: FE 02      CP      $02             
69CE: CA ED 6E   JP      Z,$6EED         
69D1: A7         AND     A               
69D2: C2 3E 6F   JP      NZ,$6F3E        
69D5: F0 EA      LD      A,($EA)         
69D7: FE 01      CP      $01             
69D9: 20 61      JR      NZ,$6A3C        
69DB: F0 EE      LD      A,($EE)         
69DD: E0 D7      LDFF00  ($D7),A         
69DF: F0 EC      LD      A,($EC)         
69E1: E0 D8      LDFF00  ($D8),A         
69E3: 3E 02      LD      A,$02           
69E5: CD 53 09   CALL    $0953           
69E8: 3E 0C      LD      A,$0C           
69EA: E0 E8      LDFF00  ($E8),A         
69EC: CD FC 69   CALL    $69FC           
69EF: 3E F4      LD      A,$F4           
69F1: E0 E8      LDFF00  ($E8),A         
69F3: CD FC 69   CALL    $69FC           
69F6: CD 88 3F   CALL    $3F88           
69F9: C3 76 7E   JP      $7E76           
69FC: 3E BD      LD      A,$BD           
69FE: CD 01 3C   CALL    $3C01           
6A01: 38 38      JR      C,$6A3B         
6A03: 21 60 C4   LD      HL,$C460        
6A06: 09         ADD     HL,BC           
6A07: 7E         LD      A,(HL)          
6A08: 21 60 C4   LD      HL,$C460        
6A0B: 19         ADD     HL,DE           
6A0C: 77         LD      (HL),A          
6A0D: F0 D7      LD      A,($D7)         
6A0F: 21 00 C2   LD      HL,$C200        
6A12: 19         ADD     HL,DE           
6A13: 77         LD      (HL),A          
6A14: F0 D8      LD      A,($D8)         
6A16: 21 10 C2   LD      HL,$C210        
6A19: 19         ADD     HL,DE           
6A1A: 77         LD      (HL),A          
6A1B: F0 DA      LD      A,($DA)         
6A1D: 21 10 C3   LD      HL,$C310        
6A20: 19         ADD     HL,DE           
6A21: 77         LD      (HL),A          
6A22: 21 B0 C2   LD      HL,$C2B0        
6A25: 19         ADD     HL,DE           
6A26: 36 01      LD      (HL),$01        
6A28: F0 E8      LD      A,($E8)         
6A2A: 21 40 C2   LD      HL,$C240        
6A2D: 19         ADD     HL,DE           
6A2E: 77         LD      (HL),A          
6A2F: 21 E0 C2   LD      HL,$C2E0        
6A32: 19         ADD     HL,DE           
6A33: 36 20      LD      (HL),$20        
6A35: 21 60 C3   LD      HL,$C360        
6A38: 19         ADD     HL,DE           
6A39: 36 01      LD      (HL),$01        
6A3B: C9         RET                     
6A3C: CD C9 6E   CALL    $6EC9           
6A3F: F0 F6      LD      A,($F6)         
6A41: 21 E0 C3   LD      HL,$C3E0        
6A44: 09         ADD     HL,BC           
6A45: BE         CP      (HL)            
6A46: 28 0E      JR      Z,$6A56         
6A48: F0 EE      LD      A,($EE)         
6A4A: FE 98      CP      $98             
6A4C: D2 76 7E   JP      NC,$7E76        
6A4F: F0 EC      LD      A,($EC)         
6A51: FE 70      CP      $70             
6A53: D2 76 7E   JP      NC,$7E76        
6A56: CD 61 7D   CALL    $7D61           
6A59: CD 83 7D   CALL    $7D83           
6A5C: CD CD 7D   CALL    $7DCD           
6A5F: CD 06 7E   CALL    $7E06           
6A62: F0 F0      LD      A,($F0)         
6A64: C7         RST     0X00            
6A65: 75         LD      (HL),L          
6A66: 6A         LD      L,D             
6A67: 96         SUB     (HL)            
6A68: 6A         LD      L,D             
6A69: 68         LD      L,B             
6A6A: 6B         LD      L,E             
6A6B: A9         XOR     C               
6A6C: 6B         LD      L,E             
6A6D: B9         CP      C               
6A6E: 6C         LD      L,H             
6A6F: E5         PUSH    HL              
6A70: 6C         LD      L,H             
6A71: 36 6D      LD      (HL),$6D        
6A73: 4F         LD      C,A             
6A74: 6D         LD      L,L             
6A75: 21 60 C3   LD      HL,$C360        
6A78: 09         ADD     HL,BC           
6A79: 36 03      LD      (HL),$03        
6A7B: CD 91 08   CALL    $0891           
6A7E: 36 C0      LD      (HL),$C0        
6A80: 21 50 C4   LD      HL,$C450        
6A83: 09         ADD     HL,BC           
6A84: 36 80      LD      (HL),$80        
6A86: CD AF 3D   CALL    $3DAF           
6A89: 21 40 C2   LD      HL,$C240        
6A8C: 09         ADD     HL,BC           
6A8D: 36 08      LD      (HL),$08        
6A8F: C3 8D 3B   JP      $3B8D           
6A92: 08 F8 08   LD      ($08F8),SP      
6A95: F8 CD      LDHL    SP,$CD          
6A97: 08 6E CD   LD      ($CD6E),SP      
6A9A: 20 7E      JR      NZ,$6B1A        
6A9C: C6 1C      ADD     $1C             
6A9E: FE 38      CP      $38             
6AA0: 30 2B      JR      NC,$6ACD        
6AA2: CD 40 7E   CALL    $7E40           
6AA5: C6 20      ADD     $20             
6AA7: FE 40      CP      $40             
6AA9: 30 22      JR      NC,$6ACD        
6AAB: 3E 10      LD      A,$10           
6AAD: CD 30 3C   CALL    $3C30           
6AB0: F0 D7      LD      A,($D7)         
6AB2: 2F         CPL                     
6AB3: 3C         INC     A               
6AB4: 21 50 C2   LD      HL,$C250        
6AB7: 09         ADD     HL,BC           
6AB8: 77         LD      (HL),A          
6AB9: F0 D8      LD      A,($D8)         
6ABB: 2F         CPL                     
6ABC: 3C         INC     A               
6ABD: 21 40 C2   LD      HL,$C240        
6AC0: 09         ADD     HL,BC           
6AC1: 77         LD      (HL),A          
6AC2: CD 8D 3B   CALL    $3B8D           
6AC5: 36 03      LD      (HL),$03        
6AC7: 21 C0 C2   LD      HL,$C2C0        
6ACA: 09         ADD     HL,BC           
6ACB: 36 FF      LD      (HL),$FF        
6ACD: 21 50 C4   LD      HL,$C450        
6AD0: 09         ADD     HL,BC           
6AD1: 7E         LD      A,(HL)          
6AD2: A7         AND     A               
6AD3: 20 0B      JR      NZ,$6AE0        
6AD5: CD 8D 3B   CALL    $3B8D           
6AD8: 36 02      LD      (HL),$02        
6ADA: CD 91 08   CALL    $0891           
6ADD: 36 20      LD      (HL),$20        
6ADF: C9         RET                     
6AE0: 21 20 C3   LD      HL,$C320        
6AE3: 09         ADD     HL,BC           
6AE4: 70         LD      (HL),B          
6AE5: 21 10 C3   LD      HL,$C310        
6AE8: 09         ADD     HL,BC           
6AE9: 7E         LD      A,(HL)          
6AEA: D6 28      SUB     $28             
6AEC: 28 0D      JR      Z,$6AFB         
6AEE: 1E 08      LD      E,$08           
6AF0: E6 80      AND     $80             
6AF2: 20 02      JR      NZ,$6AF6        
6AF4: 1E F8      LD      E,$F8           
6AF6: 21 20 C3   LD      HL,$C320        
6AF9: 09         ADD     HL,BC           
6AFA: 73         LD      (HL),E          
6AFB: 21 A0 C2   LD      HL,$C2A0        
6AFE: 09         ADD     HL,BC           
6AFF: 7E         LD      A,(HL)          
6B00: E6 03      AND     $03             
6B02: 28 12      JR      Z,$6B16         
6B04: 5F         LD      E,A             
6B05: 50         LD      D,B             
6B06: 21 93 6A   LD      HL,$6A93        
6B09: 19         ADD     HL,DE           
6B0A: 7E         LD      A,(HL)          
6B0B: 21 50 C2   LD      HL,$C250        
6B0E: 09         ADD     HL,BC           
6B0F: 77         LD      (HL),A          
6B10: 21 40 C2   LD      HL,$C240        
6B13: 09         ADD     HL,BC           
6B14: 36 00      LD      (HL),$00        
6B16: 21 A0 C2   LD      HL,$C2A0        
6B19: 09         ADD     HL,BC           
6B1A: 7E         LD      A,(HL)          
6B1B: 1F         RRA                     
6B1C: 1F         RRA                     
6B1D: E6 03      AND     $03             
6B1F: 28 12      JR      Z,$6B33         
6B21: 5F         LD      E,A             
6B22: 50         LD      D,B             
6B23: 21 91 6A   LD      HL,$6A91        
6B26: 19         ADD     HL,DE           
6B27: 7E         LD      A,(HL)          
6B28: 21 40 C2   LD      HL,$C240        
6B2B: 09         ADD     HL,BC           
6B2C: 77         LD      (HL),A          
6B2D: 21 50 C2   LD      HL,$C250        
6B30: 09         ADD     HL,BC           
6B31: 36 00      LD      (HL),$00        
6B33: CD 91 08   CALL    $0891           
6B36: 20 0E      JR      NZ,$6B46        
6B38: CD ED 27   CALL    $27ED           
6B3B: E6 7F      AND     $7F             
6B3D: C6 40      ADD     $40             
6B3F: 77         LD      (HL),A          
6B40: 21 F0 C2   LD      HL,$C2F0        
6B43: 09         ADD     HL,BC           
6B44: 36 10      LD      (HL),$10        
6B46: 21 F0 C2   LD      HL,$C2F0        
6B49: 09         ADD     HL,BC           
6B4A: 7E         LD      A,(HL)          
6B4B: A7         AND     A               
6B4C: 28 0C      JR      Z,$6B5A         
6B4E: FE 08      CP      $08             
6B50: 20 03      JR      NZ,$6B55        
6B52: CD 65 6D   CALL    $6D65           
6B55: 3E 02      LD      A,$02           
6B57: C3 87 3B   JP      $3B87           
6B5A: CD 25 6E   CALL    $6E25           
6B5D: F0 E7      LD      A,($E7)         
6B5F: 1F         RRA                     
6B60: 1F         RRA                     
6B61: 1F         RRA                     
6B62: E6 01      AND     $01             
6B64: CD 87 3B   CALL    $3B87           
6B67: C9         RET                     
6B68: CD 91 08   CALL    $0891           
6B6B: 20 33      JR      NZ,$6BA0        
6B6D: CD 8D 3B   CALL    $3B8D           
6B70: 36 03      LD      (HL),$03        
6B72: F0 99      LD      A,($99)         
6B74: F5         PUSH    AF              
6B75: D6 14      SUB     $14             
6B77: E0 99      LDFF00  ($99),A         
6B79: 3E 20      LD      A,$20           
6B7B: CD 25 3C   CALL    $3C25           
6B7E: F1         POP     AF              
6B7F: E0 99      LDFF00  ($99),A         
6B81: 21 20 C3   LD      HL,$C320        
6B84: 09         ADD     HL,BC           
6B85: 36 EC      LD      (HL),$EC        
6B87: 21 50 C4   LD      HL,$C450        
6B8A: 09         ADD     HL,BC           
6B8B: 36 30      LD      (HL),$30        
6B8D: CD ED 27   CALL    $27ED           
6B90: E6 03      AND     $03             
6B92: 21 C0 C2   LD      HL,$C2C0        
6B95: 09         ADD     HL,BC           
6B96: 77         LD      (HL),A          
6B97: A7         AND     A               
6B98: 20 05      JR      NZ,$6B9F        
6B9A: CD 91 08   CALL    $0891           
6B9D: 36 10      LD      (HL),$10        
6B9F: C9         RET                     
6BA0: CD A0 6C   CALL    $6CA0           
6BA3: 3E 02      LD      A,$02           
6BA5: CD 87 3B   CALL    $3B87           
6BA8: C9         RET                     
6BA9: 21 C0 C2   LD      HL,$C2C0        
6BAC: 09         ADD     HL,BC           
6BAD: 7E         LD      A,(HL)          
6BAE: FE FF      CP      $FF             
6BB0: 28 42      JR      Z,$6BF4         
6BB2: CD 20 7E   CALL    $7E20           
6BB5: C6 18      ADD     $18             
6BB7: FE 30      CP      $30             
6BB9: 30 39      JR      NC,$6BF4        
6BBB: CD 40 7E   CALL    $7E40           
6BBE: C6 18      ADD     $18             
6BC0: FE 30      CP      $30             
6BC2: 30 30      JR      NC,$6BF4        
6BC4: 21 20 C4   LD      HL,$C420        
6BC7: 09         ADD     HL,BC           
6BC8: 7E         LD      A,(HL)          
6BC9: A7         AND     A               
6BCA: 20 28      JR      NZ,$6BF4        
6BCC: FA 37 C1   LD      A,($C137)       
6BCF: A7         AND     A               
6BD0: 28 22      JR      Z,$6BF4         
6BD2: 3E 20      LD      A,$20           
6BD4: CD 30 3C   CALL    $3C30           
6BD7: F0 D7      LD      A,($D7)         
6BD9: 2F         CPL                     
6BDA: 3C         INC     A               
6BDB: 21 50 C2   LD      HL,$C250        
6BDE: 09         ADD     HL,BC           
6BDF: 77         LD      (HL),A          
6BE0: F0 D8      LD      A,($D8)         
6BE2: 2F         CPL                     
6BE3: 3C         INC     A               
6BE4: 21 40 C2   LD      HL,$C240        
6BE7: 09         ADD     HL,BC           
6BE8: 77         LD      (HL),A          
6BE9: CD 91 08   CALL    $0891           
6BEC: 36 0B      LD      (HL),$0B        
6BEE: CD 8D 3B   CALL    $3B8D           
6BF1: 36 06      LD      (HL),$06        
6BF3: C9         RET                     
6BF4: 21 C0 C2   LD      HL,$C2C0        
6BF7: 09         ADD     HL,BC           
6BF8: 7E         LD      A,(HL)          
6BF9: FE FF      CP      $FF             
6BFB: 28 08      JR      Z,$6C05         
6BFD: A7         AND     A               
6BFE: 20 30      JR      NZ,$6C30        
6C00: CD 91 08   CALL    $0891           
6C03: 20 2B      JR      NZ,$6C30        
6C05: 3E 20      LD      A,$20           
6C07: CD 30 3C   CALL    $3C30           
6C0A: F0 D7      LD      A,($D7)         
6C0C: 2F         CPL                     
6C0D: 3C         INC     A               
6C0E: 21 50 C2   LD      HL,$C250        
6C11: 09         ADD     HL,BC           
6C12: 96         SUB     (HL)            
6C13: E6 80      AND     $80             
6C15: 20 04      JR      NZ,$6C1B        
6C17: 34         INC     (HL)            
6C18: 34         INC     (HL)            
6C19: 34         INC     (HL)            
6C1A: 34         INC     (HL)            
6C1B: 35         DEC     (HL)            
6C1C: 35         DEC     (HL)            
6C1D: F0 D8      LD      A,($D8)         
6C1F: 2F         CPL                     
6C20: 3C         INC     A               
6C21: 21 40 C2   LD      HL,$C240        
6C24: 09         ADD     HL,BC           
6C25: 96         SUB     (HL)            
6C26: E6 80      AND     $80             
6C28: 20 04      JR      NZ,$6C2E        
6C2A: 34         INC     (HL)            
6C2B: 34         INC     (HL)            
6C2C: 34         INC     (HL)            
6C2D: 34         INC     (HL)            
6C2E: 35         DEC     (HL)            
6C2F: 35         DEC     (HL)            
6C30: 21 10 C3   LD      HL,$C310        
6C33: 09         ADD     HL,BC           
6C34: 7E         LD      A,(HL)          
6C35: FE 40      CP      $40             
6C37: 38 0C      JR      C,$6C45         
6C39: 21 20 C3   LD      HL,$C320        
6C3C: 09         ADD     HL,BC           
6C3D: 7E         LD      A,(HL)          
6C3E: E6 80      AND     $80             
6C40: 20 03      JR      NZ,$6C45        
6C42: 70         LD      (HL),B          
6C43: 18 10      JR      $6C55           
6C45: 21 20 C3   LD      HL,$C320        
6C48: 09         ADD     HL,BC           
6C49: F0 E7      LD      A,($E7)         
6C4B: E6 01      AND     $01             
6C4D: 20 01      JR      NZ,$6C50        
6C4F: 34         INC     (HL)            
6C50: 7E         LD      A,(HL)          
6C51: E6 80      AND     $80             
6C53: 20 30      JR      NZ,$6C85        
6C55: 21 50 C4   LD      HL,$C450        
6C58: 09         ADD     HL,BC           
6C59: 7E         LD      A,(HL)          
6C5A: A7         AND     A               
6C5B: 28 10      JR      Z,$6C6D         
6C5D: F0 EE      LD      A,($EE)         
6C5F: FE A8      CP      $A8             
6C61: 30 0A      JR      NC,$6C6D        
6C63: F0 EC      LD      A,($EC)         
6C65: FE 90      CP      $90             
6C67: 38 1C      JR      C,$6C85         
6C69: FE C0      CP      $C0             
6C6B: 30 18      JR      NC,$6C85        
6C6D: CD 8D 3B   CALL    $3B8D           
6C70: 36 04      LD      (HL),$04        
6C72: CD A0 6C   CALL    $6CA0           
6C75: CD 91 08   CALL    $0891           
6C78: CD ED 27   CALL    $27ED           
6C7B: E6 3F      AND     $3F             
6C7D: C6 20      ADD     $20             
6C7F: 77         LD      (HL),A          
6C80: 3E FF      LD      A,$FF           
6C82: C3 87 3B   JP      $3B87           
6C85: CD B4 3B   CALL    $3BB4           
6C88: 21 20 C4   LD      HL,$C420        
6C8B: 09         ADD     HL,BC           
6C8C: 7E         LD      A,(HL)          
6C8D: A7         AND     A               
6C8E: 28 0A      JR      Z,$6C9A         
6C90: CD AF 3D   CALL    $3DAF           
6C93: 21 C0 C2   LD      HL,$C2C0        
6C96: 09         ADD     HL,BC           
6C97: 36 FF      LD      (HL),$FF        
6C99: C9         RET                     
6C9A: CD 25 6E   CALL    $6E25           
6C9D: C3 5D 6B   JP      $6B5D           
6CA0: CD AF 3D   CALL    $3DAF           
6CA3: 21 20 C3   LD      HL,$C320        
6CA6: 09         ADD     HL,BC           
6CA7: 70         LD      (HL),B          
6CA8: C9         RET                     
6CA9: 00         NOP                     
6CAA: 00         NOP                     
6CAB: D0         RET     NC              
6CAC: D0         RET     NC              
6CAD: 40         LD      B,B             
6CAE: 40         LD      B,B             
6CAF: 80         ADD     A,B             
6CB0: 80         ADD     A,B             
6CB1: 08 98 38   LD      ($3898),SP      
6CB4: 78         LD      A,B             
6CB5: F8 A8      LDHL    SP,$A8          
6CB7: F8 A8      LDHL    SP,$A8          
6CB9: CD 91 08   CALL    $0891           
6CBC: 20 26      JR      NZ,$6CE4        
6CBE: 21 10 C3   LD      HL,$C310        
6CC1: 09         ADD     HL,BC           
6CC2: 36 28      LD      (HL),$28        
6CC4: CD 8D 3B   CALL    $3B8D           
6CC7: 36 05      LD      (HL),$05        
6CC9: CD ED 27   CALL    $27ED           
6CCC: E6 07      AND     $07             
6CCE: 5F         LD      E,A             
6CCF: 50         LD      D,B             
6CD0: 21 A9 6C   LD      HL,$6CA9        
6CD3: 19         ADD     HL,DE           
6CD4: 7E         LD      A,(HL)          
6CD5: 21 10 C2   LD      HL,$C210        
6CD8: 09         ADD     HL,BC           
6CD9: 77         LD      (HL),A          
6CDA: 21 B1 6C   LD      HL,$6CB1        
6CDD: 19         ADD     HL,DE           
6CDE: 7E         LD      A,(HL)          
6CDF: 21 00 C2   LD      HL,$C200        
6CE2: 09         ADD     HL,BC           
6CE3: 77         LD      (HL),A          
6CE4: C9         RET                     
6CE5: 3E 08      LD      A,$08           
6CE7: CD 25 3C   CALL    $3C25           
6CEA: F0 EE      LD      A,($EE)         
6CEC: FE 09      CP      $09             
6CEE: 38 2F      JR      C,$6D1F         
6CF0: FE 97      CP      $97             
6CF2: 30 2B      JR      NC,$6D1F        
6CF4: F0 EC      LD      A,($EC)         
6CF6: FE 20      CP      $20             
6CF8: 38 25      JR      C,$6D1F         
6CFA: FE 70      CP      $70             
6CFC: 30 21      JR      NC,$6D1F        
6CFE: CD 8D 3B   CALL    $3B8D           
6D01: 36 01      LD      (HL),$01        
6D03: 21 50 C4   LD      HL,$C450        
6D06: 09         ADD     HL,BC           
6D07: CD ED 27   CALL    $27ED           
6D0A: E6 3F      AND     $3F             
6D0C: C6 20      ADD     $20             
6D0E: 77         LD      (HL),A          
6D0F: 21 40 C2   LD      HL,$C240        
6D12: 09         ADD     HL,BC           
6D13: 7E         LD      A,(HL)          
6D14: 2F         CPL                     
6D15: 3C         INC     A               
6D16: 77         LD      (HL),A          
6D17: 21 50 C2   LD      HL,$C250        
6D1A: 09         ADD     HL,BC           
6D1B: 7E         LD      A,(HL)          
6D1C: 2F         CPL                     
6D1D: 3C         INC     A               
6D1E: 77         LD      (HL),A          
6D1F: C3 5D 6B   JP      $6B5D           
6D22: 00         NOP                     
6D23: 09         ADD     HL,BC           
6D24: 12         LD      (DE),A          
6D25: 15         DEC     D               
6D26: 18 15      JR      $6D3D           
6D28: 12         LD      (DE),A          
6D29: 09         ADD     HL,BC           
6D2A: 00         NOP                     
6D2B: F7         RST     0X30            
6D2C: EE EB      XOR     $EB             
6D2E: E8 EB      ADD     SP,$EB          
6D30: EE F7      XOR     $F7             
6D32: 00         NOP                     
6D33: 09         ADD     HL,BC           
6D34: 12         LD      (DE),A          
6D35: 15         DEC     D               
6D36: CD 91 08   CALL    $0891           
6D39: 20 0A      JR      NZ,$6D45        
6D3B: 36 20      LD      (HL),$20        
6D3D: CD 8D 3B   CALL    $3B8D           
6D40: 36 07      LD      (HL),$07        
6D42: C3 A0 6C   JP      $6CA0           
6D45: FE 08      CP      $08             
6D47: 38 03      JR      C,$6D4C         
6D49: CD 85 6C   CALL    $6C85           
6D4C: C3 5D 6B   JP      $6B5D           
6D4F: CD 91 08   CALL    $0891           
6D52: 20 0C      JR      NZ,$6D60        
6D54: 21 C0 C2   LD      HL,$C2C0        
6D57: 09         ADD     HL,BC           
6D58: 36 FF      LD      (HL),$FF        
6D5A: CD 8D 3B   CALL    $3B8D           
6D5D: 36 03      LD      (HL),$03        
6D5F: C9         RET                     
6D60: FE 08      CP      $08             
6D62: C2 03 6E   JP      NZ,$6E03        
6D65: 3E 0D      LD      A,$0D           
6D67: E0 F4      LDFF00  ($F4),A         
6D69: F0 99      LD      A,($99)         
6D6B: F5         PUSH    AF              
6D6C: D6 08      SUB     $08             
6D6E: E0 99      LDFF00  ($99),A         
6D70: 3E 1F      LD      A,$1F           
6D72: CD 30 3C   CALL    $3C30           
6D75: F1         POP     AF              
6D76: E0 99      LDFF00  ($99),A         
6D78: CD 1B 7B   CALL    $7B1B           
6D7B: E6 0F      AND     $0F             
6D7D: E0 E8      LDFF00  ($E8),A         
6D7F: 1E 00      LD      E,$00           
6D81: CD 86 6D   CALL    $6D86           
6D84: 1E 01      LD      E,$01           
6D86: F0 E8      LD      A,($E8)         
6D88: 83         ADD     A,E             
6D89: E6 0F      AND     $0F             
6D8B: E0 E8      LDFF00  ($E8),A         
6D8D: 1E 0F      LD      E,$0F           
6D8F: 50         LD      D,B             
6D90: 21 80 C2   LD      HL,$C280        
6D93: 19         ADD     HL,DE           
6D94: 7E         LD      A,(HL)          
6D95: A7         AND     A               
6D96: 28 13      JR      Z,$6DAB         
6D98: 21 A0 C3   LD      HL,$C3A0        
6D9B: 19         ADD     HL,DE           
6D9C: 7E         LD      A,(HL)          
6D9D: FE BD      CP      $BD             
6D9F: 20 0A      JR      NZ,$6DAB        
6DA1: 21 B0 C2   LD      HL,$C2B0        
6DA4: 19         ADD     HL,DE           
6DA5: 7E         LD      A,(HL)          
6DA6: FE 02      CP      $02             
6DA8: 20 01      JR      NZ,$6DAB        
6DAA: 04         INC     B               
6DAB: 1D         DEC     E               
6DAC: 7B         LD      A,E             
6DAD: FE FF      CP      $FF             
6DAF: 20 DF      JR      NZ,$6D90        
6DB1: 78         LD      A,B             
6DB2: 06 00      LD      B,$00           
6DB4: FE 03      CP      $03             
6DB6: 30 4A      JR      NC,$6E02        
6DB8: 3E BD      LD      A,$BD           
6DBA: CD 01 3C   CALL    $3C01           
6DBD: 38 43      JR      C,$6E02         
6DBF: F0 D7      LD      A,($D7)         
6DC1: 21 00 C2   LD      HL,$C200        
6DC4: 19         ADD     HL,DE           
6DC5: 77         LD      (HL),A          
6DC6: F0 D8      LD      A,($D8)         
6DC8: 21 DA FF   LD      HL,$FFDA        
6DCB: 96         SUB     (HL)            
6DCC: 21 10 C2   LD      HL,$C210        
6DCF: 19         ADD     HL,DE           
6DD0: 77         LD      (HL),A          
6DD1: 21 B0 C2   LD      HL,$C2B0        
6DD4: 19         ADD     HL,DE           
6DD5: 36 02      LD      (HL),$02        
6DD7: 21 40 C3   LD      HL,$C340        
6DDA: 19         ADD     HL,DE           
6DDB: 36 02      LD      (HL),$02        
6DDD: 21 60 C3   LD      HL,$C360        
6DE0: 19         ADD     HL,DE           
6DE1: 36 4C      LD      (HL),$4C        
6DE3: C5         PUSH    BC              
6DE4: F0 E8      LD      A,($E8)         
6DE6: 4F         LD      C,A             
6DE7: 21 26 6D   LD      HL,$6D26        
6DEA: 09         ADD     HL,BC           
6DEB: 7E         LD      A,(HL)          
6DEC: 21 40 C2   LD      HL,$C240        
6DEF: 19         ADD     HL,DE           
6DF0: 77         LD      (HL),A          
6DF1: 21 22 6D   LD      HL,$6D22        
6DF4: 09         ADD     HL,BC           
6DF5: 7E         LD      A,(HL)          
6DF6: 21 50 C2   LD      HL,$C250        
6DF9: 19         ADD     HL,DE           
6DFA: 77         LD      (HL),A          
6DFB: 21 E0 C2   LD      HL,$C2E0        
6DFE: 19         ADD     HL,DE           
6DFF: 36 20      LD      (HL),$20        
6E01: C1         POP     BC              
6E02: C9         RET                     
6E03: 3E 02      LD      A,$02           
6E05: C3 87 3B   JP      $3B87           
6E08: 21 10 C2   LD      HL,$C210        
6E0B: 09         ADD     HL,BC           
6E0C: 7E         LD      A,(HL)          
6E0D: D6 28      SUB     $28             
6E0F: 77         LD      (HL),A          
6E10: F0 EF      LD      A,($EF)         
6E12: D6 28      SUB     $28             
6E14: E0 EF      LDFF00  ($EF),A         
6E16: CD 9E 3B   CALL    $3B9E           
6E19: 21 10 C2   LD      HL,$C210        
6E1C: 09         ADD     HL,BC           
6E1D: 7E         LD      A,(HL)          
6E1E: C6 28      ADD     $28             
6E20: 77         LD      (HL),A          
6E21: CD BA 3D   CALL    $3DBA           
6E24: C9         RET                     
6E25: 1E 0F      LD      E,$0F           
6E27: 50         LD      D,B             
6E28: 21 80 C2   LD      HL,$C280        
6E2B: 19         ADD     HL,DE           
6E2C: 7E         LD      A,(HL)          
6E2D: FE 05      CP      $05             
6E2F: 20 6D      JR      NZ,$6E9E        
6E31: 21 A0 C3   LD      HL,$C3A0        
6E34: 19         ADD     HL,DE           
6E35: 7E         LD      A,(HL)          
6E36: FE 03      CP      $03             
6E38: 28 08      JR      Z,$6E42         
6E3A: FE 00      CP      $00             
6E3C: 28 04      JR      Z,$6E42         
6E3E: FE 02      CP      $02             
6E40: 20 5C      JR      NZ,$6E9E        
6E42: 21 00 C2   LD      HL,$C200        
6E45: 19         ADD     HL,DE           
6E46: F0 EE      LD      A,($EE)         
6E48: 96         SUB     (HL)            
6E49: C6 18      ADD     $18             
6E4B: FE 30      CP      $30             
6E4D: 30 4F      JR      NC,$6E9E        
6E4F: 21 10 C2   LD      HL,$C210        
6E52: 19         ADD     HL,DE           
6E53: F0 EC      LD      A,($EC)         
6E55: 96         SUB     (HL)            
6E56: C6 20      ADD     $20             
6E58: FE 40      CP      $40             
6E5A: 30 42      JR      NC,$6E9E        
6E5C: F0 99      LD      A,($99)         
6E5E: F5         PUSH    AF              
6E5F: F0 98      LD      A,($98)         
6E61: F5         PUSH    AF              
6E62: 7E         LD      A,(HL)          
6E63: E0 99      LDFF00  ($99),A         
6E65: 21 00 C2   LD      HL,$C200        
6E68: 19         ADD     HL,DE           
6E69: 7E         LD      A,(HL)          
6E6A: E0 98      LDFF00  ($98),A         
6E6C: D5         PUSH    DE              
6E6D: 3E 20      LD      A,$20           
6E6F: CD 30 3C   CALL    $3C30           
6E72: D1         POP     DE              
6E73: F0 D8      LD      A,($D8)         
6E75: 2F         CPL                     
6E76: 3C         INC     A               
6E77: 20 02      JR      NZ,$6E7B        
6E79: 3E 20      LD      A,$20           
6E7B: 21 40 C2   LD      HL,$C240        
6E7E: 09         ADD     HL,BC           
6E7F: 77         LD      (HL),A          
6E80: F0 D7      LD      A,($D7)         
6E82: 2F         CPL                     
6E83: 3C         INC     A               
6E84: 20 02      JR      NZ,$6E88        
6E86: 3E 20      LD      A,$20           
6E88: 21 50 C2   LD      HL,$C250        
6E8B: 09         ADD     HL,BC           
6E8C: 77         LD      (HL),A          
6E8D: F1         POP     AF              
6E8E: E0 98      LDFF00  ($98),A         
6E90: F1         POP     AF              
6E91: E0 99      LDFF00  ($99),A         
6E93: CD 8D 3B   CALL    $3B8D           
6E96: 36 03      LD      (HL),$03        
6E98: 21 C0 C2   LD      HL,$C2C0        
6E9B: 09         ADD     HL,BC           
6E9C: 36 01      LD      (HL),$01        
6E9E: 1D         DEC     E               
6E9F: 7B         LD      A,E             
6EA0: FE FF      CP      $FF             
6EA2: 20 83      JR      NZ,$6E27        
6EA4: C9         RET                     
6EA5: 00         NOP                     
6EA6: FC         ???                     
6EA7: 60         LD      H,B             
6EA8: 00         NOP                     
6EA9: 00         NOP                     
6EAA: 04         INC     B               
6EAB: 62         LD      H,D             
6EAC: 00         NOP                     
6EAD: 00         NOP                     
6EAE: 0C         INC     C               
6EAF: 60         LD      H,B             
6EB0: 20 00      JR      NZ,$6EB2        
6EB2: FC         ???                     
6EB3: 64         LD      H,H             
6EB4: 00         NOP                     
6EB5: 00         NOP                     
6EB6: 04         INC     B               
6EB7: 66         LD      H,(HL)          
6EB8: 00         NOP                     
6EB9: 00         NOP                     
6EBA: 0C         INC     C               
6EBB: 64         LD      H,H             
6EBC: 20 00      JR      NZ,$6EBE        
6EBE: FC         ???                     
6EBF: 68         LD      L,B             
6EC0: 00         NOP                     
6EC1: 00         NOP                     
6EC2: 04         INC     B               
6EC3: 6A         LD      L,D             
6EC4: 00         NOP                     
6EC5: 00         NOP                     
6EC6: 0C         INC     C               
6EC7: 68         LD      L,B             
6EC8: 20 F0      JR      NZ,$6EBA        
6ECA: F1         POP     AF              
6ECB: FE FF      CP      $FF             
6ECD: C8         RET     Z               
6ECE: 17         RLA                     
6ECF: 17         RLA                     
6ED0: E6 FC      AND     $FC             
6ED2: 5F         LD      E,A             
6ED3: 17         RLA                     
6ED4: E6 F8      AND     $F8             
6ED6: 83         ADD     A,E             
6ED7: 5F         LD      E,A             
6ED8: 50         LD      D,B             
6ED9: 21 A5 6E   LD      HL,$6EA5        
6EDC: 19         ADD     HL,DE           
6EDD: 0E 03      LD      C,$03           
6EDF: CD 26 3D   CALL    $3D26           
6EE2: C3 19 3D   JP      $3D19           
6EE5: 1E 00      LD      E,$00           
6EE7: 1E 60      LD      E,$60           
6EE9: 1E 40      LD      E,$40           
6EEB: 1E 20      LD      E,$20           
6EED: 11 E5 6E   LD      DE,$6EE5        
6EF0: CD 3B 3C   CALL    $3C3B           
6EF3: CD 61 7D   CALL    $7D61           
6EF6: CD E2 08   CALL    $08E2           
6EF9: F0 E7      LD      A,($E7)         
6EFB: 1F         RRA                     
6EFC: 1F         RRA                     
6EFD: E6 01      AND     $01             
6EFF: CD 87 3B   CALL    $3B87           
6F02: CD EB 3B   CALL    $3BEB           
6F05: CD BF 3B   CALL    $3BBF           
6F08: 38 15      JR      C,$6F1F         
6F0A: 21 10 C4   LD      HL,$C410        
6F0D: 09         ADD     HL,BC           
6F0E: 7E         LD      A,(HL)          
6F0F: A7         AND     A               
6F10: 28 10      JR      Z,$6F22         
6F12: F0 EE      LD      A,($EE)         
6F14: E0 D7      LDFF00  ($D7),A         
6F16: F0 EC      LD      A,($EC)         
6F18: E0 D8      LDFF00  ($D8),A         
6F1A: 3E 02      LD      A,$02           
6F1C: CD 53 09   CALL    $0953           
6F1F: C3 76 7E   JP      $7E76           
6F22: CD CD 7D   CALL    $7DCD           
6F25: CD 91 08   CALL    $0891           
6F28: C0         RET     NZ              
6F29: CD 9E 3B   CALL    $3B9E           
6F2C: 21 A0 C2   LD      HL,$C2A0        
6F2F: 09         ADD     HL,BC           
6F30: 7E         LD      A,(HL)          
6F31: A7         AND     A               
6F32: C2 76 7E   JP      NZ,$7E76        
6F35: C9         RET                     
6F36: 6C         LD      L,H             
6F37: 00         NOP                     
6F38: 6C         LD      L,H             
6F39: 20 6E      JR      NZ,$6FA9        
6F3B: 00         NOP                     
6F3C: 6E         LD      L,(HL)          
6F3D: 20 11      JR      NZ,$6F50        
6F3F: 36 6F      LD      (HL),$6F        
6F41: CD 3B 3C   CALL    $3C3B           
6F44: CD 61 7D   CALL    $7D61           
6F47: CD 83 7D   CALL    $7D83           
6F4A: CD CD 7D   CALL    $7DCD           
6F4D: F0 E7      LD      A,($E7)         
6F4F: E6 03      AND     $03             
6F51: 20 10      JR      NZ,$6F63        
6F53: 21 10 C3   LD      HL,$C310        
6F56: 09         ADD     HL,BC           
6F57: 7E         LD      A,(HL)          
6F58: D6 10      SUB     $10             
6F5A: 28 07      JR      Z,$6F63         
6F5C: E6 80      AND     $80             
6F5E: 28 02      JR      Z,$6F62         
6F60: 34         INC     (HL)            
6F61: 34         INC     (HL)            
6F62: 35         DEC     (HL)            
6F63: F0 E7      LD      A,($E7)         
6F65: 1F         RRA                     
6F66: 1F         RRA                     
6F67: 1F         RRA                     
6F68: E6 01      AND     $01             
6F6A: CD 87 3B   CALL    $3B87           
6F6D: F0 F0      LD      A,($F0)         
6F6F: C7         RST     0X00            
6F70: 76         HALT                    
6F71: 6F         LD      L,A             
6F72: 84         ADD     A,H             
6F73: 6F         LD      L,A             
6F74: 94         SUB     H               
6F75: 6F         LD      L,A             
6F76: CD 91 08   CALL    $0891           
6F79: 20 08      JR      NZ,$6F83        
6F7B: 36 20      LD      (HL),$20        
6F7D: CD AF 3D   CALL    $3DAF           
6F80: CD 8D 3B   CALL    $3B8D           
6F83: C9         RET                     
6F84: CD 91 08   CALL    $0891           
6F87: 20 0A      JR      NZ,$6F93        
6F89: 36 20      LD      (HL),$20        
6F8B: 3E 20      LD      A,$20           
6F8D: CD 25 3C   CALL    $3C25           
6F90: CD 8D 3B   CALL    $3B8D           
6F93: C9         RET                     
6F94: CD B4 3B   CALL    $3BB4           
6F97: CD 91 08   CALL    $0891           
6F9A: C0         RET     NZ              
6F9B: CD 9E 3B   CALL    $3B9E           
6F9E: 21 A0 C2   LD      HL,$C2A0        
6FA1: 09         ADD     HL,BC           
6FA2: 7E         LD      A,(HL)          
6FA3: A7         AND     A               
6FA4: C2 76 7E   JP      NZ,$7E76        
6FA7: C9         RET                     
6FA8: 21 B0 C2   LD      HL,$C2B0        
6FAB: 09         ADD     HL,BC           
6FAC: 7E         LD      A,(HL)          
6FAD: A7         AND     A               
6FAE: C2 66 71   JP      NZ,$7166        
6FB1: 21 40 C3   LD      HL,$C340        
6FB4: 09         ADD     HL,BC           
6FB5: CB F6      SET     1,E             
6FB7: CD 44 71   CALL    $7144           
6FBA: CD 0E 38   CALL    $380E           
6FBD: CD 12 3F   CALL    $3F12           
6FC0: CD 61 7D   CALL    $7D61           
6FC3: FA 8F C1   LD      A,($C18F)       
6FC6: A7         AND     A               
6FC7: 28 31      JR      Z,$6FFA         
6FC9: 21 D0 C2   LD      HL,$C2D0        
6FCC: 09         ADD     HL,BC           
6FCD: 7E         LD      A,(HL)          
6FCE: A7         AND     A               
6FCF: 20 09      JR      NZ,$6FDA        
6FD1: 34         INC     (HL)            
6FD2: 3E 25      LD      A,$25           
6FD4: CD 97 21   CALL    $2197           
6FD7: C3 2B 7F   JP      $7F2B           
6FDA: FE 01      CP      $01             
6FDC: 20 05      JR      NZ,$6FE3        
6FDE: 3E 3F      LD      A,$3F           
6FE0: E0 F4      LDFF00  ($F4),A         
6FE2: 34         INC     (HL)            
6FE3: 21 20 C3   LD      HL,$C320        
6FE6: 09         ADD     HL,BC           
6FE7: 36 20      LD      (HL),$20        
6FE9: CD 06 7E   CALL    $7E06           
6FEC: 21 10 C3   LD      HL,$C310        
6FEF: 09         ADD     HL,BC           
6FF0: 7E         LD      A,(HL)          
6FF1: FE 78      CP      $78             
6FF3: D8         RET     C               
6FF4: CD BD 27   CALL    $27BD           
6FF7: C3 76 7E   JP      $7E76           
6FFA: F0 F0      LD      A,($F0)         
6FFC: C7         RST     0X00            
6FFD: 0B         DEC     BC              
6FFE: 70         LD      (HL),B          
6FFF: 13         INC     DE              
7000: 70         LD      (HL),B          
7001: 2B         DEC     HL              
7002: 70         LD      (HL),B          
7003: 67         LD      H,A             
7004: 70         LD      (HL),B          
7005: DC 70 F8   CALL    C,$F870         
7008: 70         LD      (HL),B          
7009: 0C         INC     C               
700A: 71         LD      (HL),C          
700B: 3E 07      LD      A,$07           
700D: EA 05 D2   LD      ($D205),A       
7010: C3 8D 3B   JP      $3B8D           
7013: CD 91 08   CALL    $0891           
7016: 36 80      LD      (HL),$80        
7018: AF         XOR     A               
7019: EA 01 D2   LD      ($D201),A       
701C: EA 02 D2   LD      ($D202),A       
701F: FA 05 D2   LD      A,($D205)       
7022: 3C         INC     A               
7023: E6 07      AND     $07             
7025: EA 05 D2   LD      ($D205),A       
7028: C3 8D 3B   JP      $3B8D           
702B: CD 91 08   CALL    $0891           
702E: 20 2A      JR      NZ,$705A        
7030: 36 FF      LD      (HL),$FF        
7032: 21 30 C4   LD      HL,$C430        
7035: 09         ADD     HL,BC           
7036: CB 8E      SET     1,E             
7038: 1E 0F      LD      E,$0F           
703A: 50         LD      D,B             
703B: 21 A0 C3   LD      HL,$C3A0        
703E: 19         ADD     HL,DE           
703F: 7E         LD      A,(HL)          
7040: FE BC      CP      $BC             
7042: 20 0D      JR      NZ,$7051        
7044: 21 B0 C2   LD      HL,$C2B0        
7047: 19         ADD     HL,DE           
7048: 7E         LD      A,(HL)          
7049: A7         AND     A               
704A: 28 05      JR      Z,$7051         
704C: 21 80 C2   LD      HL,$C280        
704F: 19         ADD     HL,DE           
7050: 70         LD      (HL),B          
7051: 1D         DEC     E               
7052: 7B         LD      A,E             
7053: FE FF      CP      $FF             
7055: 20 E4      JR      NZ,$703B        
7057: C3 8D 3B   JP      $3B8D           
705A: C9         RET                     
705B: 78         LD      A,B             
705C: 68         LD      L,B             
705D: 58         LD      E,B             
705E: 48         LD      C,B             
705F: 38 28      JR      C,$7089         
7061: 00         NOP                     
7062: 00         NOP                     
7063: 00         NOP                     
7064: 00         NOP                     
7065: 00         NOP                     
7066: 00         NOP                     
7067: CD 91 08   CALL    $0891           
706A: 20 0A      JR      NZ,$7076        
706C: 21 30 C4   LD      HL,$C430        
706F: 09         ADD     HL,BC           
7070: CB CE      SET     1,E             
7072: CD 8D 3B   CALL    $3B8D           
7075: AF         XOR     A               
7076: E6 1F      AND     $1F             
7078: 20 55      JR      NZ,$70CF        
707A: 21 D0 C3   LD      HL,$C3D0        
707D: 09         ADD     HL,BC           
707E: 7E         LD      A,(HL)          
707F: FE 06      CP      $06             
7081: 30 4C      JR      NC,$70CF        
7083: 3E BC      LD      A,$BC           
7085: CD 01 3C   CALL    $3C01           
7088: 38 45      JR      C,$70CF         
708A: 3E 31      LD      A,$31           
708C: E0 F2      LDFF00  ($F2),A         
708E: 21 D0 C3   LD      HL,$C3D0        
7091: 09         ADD     HL,BC           
7092: C5         PUSH    BC              
7093: 4E         LD      C,(HL)          
7094: 34         INC     (HL)            
7095: 21 5B 70   LD      HL,$705B        
7098: 09         ADD     HL,BC           
7099: 7E         LD      A,(HL)          
709A: 21 00 C2   LD      HL,$C200        
709D: 19         ADD     HL,DE           
709E: 77         LD      (HL),A          
709F: 21 61 70   LD      HL,$7061        
70A2: 09         ADD     HL,BC           
70A3: 7E         LD      A,(HL)          
70A4: 21 10 C2   LD      HL,$C210        
70A7: 19         ADD     HL,DE           
70A8: 77         LD      (HL),A          
70A9: 21 10 C3   LD      HL,$C310        
70AC: 19         ADD     HL,DE           
70AD: 36 1C      LD      (HL),$1C        
70AF: 21 D0 C3   LD      HL,$C3D0        
70B2: 19         ADD     HL,DE           
70B3: 71         LD      (HL),C          
70B4: 21 30 C4   LD      HL,$C430        
70B7: 19         ADD     HL,DE           
70B8: 7E         LD      A,(HL)          
70B9: E6 7B      AND     $7B             
70BB: 77         LD      (HL),A          
70BC: 21 60 C3   LD      HL,$C360        
70BF: 19         ADD     HL,DE           
70C0: 36 01      LD      (HL),$01        
70C2: 21 B0 C2   LD      HL,$C2B0        
70C5: 19         ADD     HL,DE           
70C6: 36 01      LD      (HL),$01        
70C8: 21 40 C3   LD      HL,$C340        
70CB: 19         ADD     HL,DE           
70CC: CB F6      SET     1,E             
70CE: C1         POP     BC              
70CF: F0 E7      LD      A,($E7)         
70D1: 1F         RRA                     
70D2: 1F         RRA                     
70D3: 1F         RRA                     
70D4: 1F         RRA                     
70D5: 1F         RRA                     
70D6: E6 01      AND     $01             
70D8: CD 87 3B   CALL    $3B87           
70DB: C9         RET                     
70DC: FA 01 D2   LD      A,($D201)       
70DF: FE 06      CP      $06             
70E1: 20 11      JR      NZ,$70F4        
70E3: 21 D0 C3   LD      HL,$C3D0        
70E6: 09         ADD     HL,BC           
70E7: 70         LD      (HL),B          
70E8: AF         XOR     A               
70E9: EA 01 D2   LD      ($D201),A       
70EC: CD 91 08   CALL    $0891           
70EF: 36 40      LD      (HL),$40        
70F1: CD 8D 3B   CALL    $3B8D           
70F4: CD CF 70   CALL    $70CF           
70F7: C9         RET                     
70F8: CD 91 08   CALL    $0891           
70FB: 20 0E      JR      NZ,$710B        
70FD: 3E FF      LD      A,$FF           
70FF: EA 01 D2   LD      ($D201),A       
7102: 21 50 C4   LD      HL,$C450        
7105: 09         ADD     HL,BC           
7106: 36 40      LD      (HL),$40        
7108: CD 8D 3B   CALL    $3B8D           
710B: C9         RET                     
710C: 21 50 C4   LD      HL,$C450        
710F: 09         ADD     HL,BC           
7110: 7E         LD      A,(HL)          
7111: A7         AND     A               
7112: 20 05      JR      NZ,$7119        
7114: CD 8D 3B   CALL    $3B8D           
7117: 36 01      LD      (HL),$01        
7119: 3E 02      LD      A,$02           
711B: CD 87 3B   CALL    $3B87           
711E: C9         RET                     
711F: C9         RET                     
7120: 00         NOP                     
7121: F8 60      LDHL    SP,$60          
7123: 00         NOP                     
7124: 00         NOP                     
7125: 00         NOP                     
7126: 62         LD      H,D             
7127: 00         NOP                     
7128: 00         NOP                     
7129: 08 64 00   LD      ($0064),SP      
712C: 00         NOP                     
712D: F8 66      LDHL    SP,$66          
712F: 00         NOP                     
7130: 00         NOP                     
7131: 00         NOP                     
7132: 62         LD      H,D             
7133: 00         NOP                     
7134: 00         NOP                     
7135: 08 64 00   LD      ($0064),SP      
7138: 10 00      STOP    $00             
713A: 68         LD      L,B             
713B: 00         NOP                     
713C: 00         NOP                     
713D: 00         NOP                     
713E: 62         LD      H,D             
713F: 00         NOP                     
7140: 00         NOP                     
7141: 08 64 00   LD      ($0064),SP      
7144: F0 F1      LD      A,($F1)         
7146: 17         RLA                     
7147: 17         RLA                     
7148: E6 FC      AND     $FC             
714A: 5F         LD      E,A             
714B: CB 27      SET     1,E             
714D: 83         ADD     A,E             
714E: 5F         LD      E,A             
714F: 50         LD      D,B             
7150: 21 20 71   LD      HL,$7120        
7153: 19         ADD     HL,DE           
7154: 0E 03      LD      C,$03           
7156: CD 26 3D   CALL    $3D26           
7159: 3E 01      LD      A,$01           
715B: C3 D0 3D   JP      $3DD0           
715E: 6E         LD      L,(HL)          
715F: 00         NOP                     
7160: 6E         LD      L,(HL)          
7161: 20 6E      JR      NZ,$71D1        
7163: 40         LD      B,B             
7164: 6E         LD      L,(HL)          
7165: 60         LD      H,B             
7166: 11 5E 71   LD      DE,$715E        
7169: CD 3B 3C   CALL    $3C3B           
716C: CD 61 7D   CALL    $7D61           
716F: CD E2 08   CALL    $08E2           
7172: F0 F0      LD      A,($F0)         
7174: C7         RST     0X00            
7175: DF         RST     0X18            
7176: 71         LD      (HL),C          
7177: 4C         LD      C,H             
7178: 72         LD      (HL),D          
7179: 69         LD      L,C             
717A: 72         LD      (HL),D          
717B: 8C         ADC     A,H             
717C: 72         LD      (HL),D          
717D: B9         CP      C               
717E: 72         LD      (HL),D          
717F: 28 38      JR      Z,$71B9         
7181: 48         LD      C,B             
7182: 58         LD      E,B             
7183: 68         LD      L,B             
7184: 78         LD      A,B             
7185: 38 68      JR      C,$71EF         
7187: 48         LD      C,B             
7188: 58         LD      E,B             
7189: 48         LD      C,B             
718A: 58         LD      E,B             
718B: 18 88      JR      $7115           
718D: 28 78      JR      Z,$7207         
718F: 60         LD      H,B             
7190: 40         LD      B,B             
7191: 28 78      JR      Z,$720B         
7193: 78         LD      A,B             
7194: 28 60      JR      Z,$71F6         
7196: 40         LD      B,B             
7197: 28 78      JR      Z,$7211         
7199: 28 78      JR      Z,$7213         
719B: 50         LD      D,B             
719C: 50         LD      D,B             
719D: 38 68      JR      C,$7207         
719F: 50         LD      D,B             
71A0: 50         LD      D,B             
71A1: 38 68      JR      C,$720B         
71A3: 38 68      JR      C,$720D         
71A5: 38 68      JR      C,$720F         
71A7: 38 68      JR      C,$7211         
71A9: 28 78      JR      Z,$7223         
71AB: 38 48      JR      C,$71F5         
71AD: 68         LD      L,B             
71AE: 58         LD      E,B             
71AF: 20 30      JR      NZ,$71E1        
71B1: 40         LD      B,B             
71B2: 40         LD      B,B             
71B3: 30 20      JR      NC,$71D5        
71B5: 60         LD      H,B             
71B6: 60         LD      H,B             
71B7: 50         LD      D,B             
71B8: 70         LD      (HL),B          
71B9: 70         LD      (HL),B          
71BA: 50         LD      D,B             
71BB: 38 38      JR      C,$71F5         
71BD: 58         LD      E,B             
71BE: 58         LD      E,B             
71BF: 70         LD      (HL),B          
71C0: 70         LD      (HL),B          
71C1: 30 30      JR      NC,$71F3        
71C3: 70         LD      (HL),B          
71C4: 70         LD      (HL),B          
71C5: 50         LD      D,B             
71C6: 50         LD      D,B             
71C7: 30 70      JR      NC,$7239        
71C9: 70         LD      (HL),B          
71CA: 30 30      JR      NC,$71FC        
71CC: 70         LD      (HL),B          
71CD: 40         LD      B,B             
71CE: 60         LD      H,B             
71CF: 70         LD      (HL),B          
71D0: 30 60      JR      NC,$7232        
71D2: 40         LD      B,B             
71D3: 30 30      JR      NC,$7205        
71D5: 50         LD      D,B             
71D6: 50         LD      D,B             
71D7: 70         LD      (HL),B          
71D8: 70         LD      (HL),B          
71D9: 40         LD      B,B             
71DA: 40         LD      B,B             
71DB: 50         LD      D,B             
71DC: 40         LD      B,B             
71DD: 50         LD      D,B             
71DE: 40         LD      B,B             
71DF: F0 98      LD      A,($98)         
71E1: F5         PUSH    AF              
71E2: F0 99      LD      A,($99)         
71E4: F5         PUSH    AF              
71E5: FA 05 D2   LD      A,($D205)       
71E8: 17         RLA                     
71E9: E6 FE      AND     $FE             
71EB: 5F         LD      E,A             
71EC: 17         RLA                     
71ED: E6 FC      AND     $FC             
71EF: 83         ADD     A,E             
71F0: 21 D0 C3   LD      HL,$C3D0        
71F3: 09         ADD     HL,BC           
71F4: 86         ADD     A,(HL)          
71F5: 5F         LD      E,A             
71F6: 50         LD      D,B             
71F7: 21 7F 71   LD      HL,$717F        
71FA: 19         ADD     HL,DE           
71FB: 7E         LD      A,(HL)          
71FC: E0 98      LDFF00  ($98),A         
71FE: 21 AF 71   LD      HL,$71AF        
7201: 19         ADD     HL,DE           
7202: 7E         LD      A,(HL)          
7203: E0 99      LDFF00  ($99),A         
7205: F0 E7      LD      A,($E7)         
7207: A9         XOR     C               
7208: E6 03      AND     $03             
720A: 20 05      JR      NZ,$7211        
720C: 3E 10      LD      A,$10           
720E: CD 25 3C   CALL    $3C25           
7211: 21 EE FF   LD      HL,$FFEE        
7214: F0 98      LD      A,($98)         
7216: 96         SUB     (HL)            
7217: C6 03      ADD     $03             
7219: FE 06      CP      $06             
721B: 30 13      JR      NC,$7230        
721D: 21 EC FF   LD      HL,$FFEC        
7220: F0 99      LD      A,($99)         
7222: 96         SUB     (HL)            
7223: C6 03      ADD     $03             
7225: FE 06      CP      $06             
7227: 30 07      JR      NC,$7230        
7229: 21 01 D2   LD      HL,$D201        
722C: 34         INC     (HL)            
722D: CD 8D 3B   CALL    $3B8D           
7230: F1         POP     AF              
7231: E0 99      LDFF00  ($99),A         
7233: F1         POP     AF              
7234: E0 98      LDFF00  ($98),A         
7236: CD CD 7D   CALL    $7DCD           
7239: F0 E7      LD      A,($E7)         
723B: 1F         RRA                     
723C: 1F         RRA                     
723D: 1F         RRA                     
723E: E6 01      AND     $01             
7240: CD 87 3B   CALL    $3B87           
7243: C9         RET                     
7244: 04         INC     B               
7245: 0C         INC     C               
7246: 14         INC     D               
7247: 1C         INC     E               
7248: 24         INC     H               
7249: 2C         INC     L               
724A: 34         INC     (HL)            
724B: 3C         INC     A               
724C: FA 01 D2   LD      A,($D201)       
724F: FE FF      CP      $FF             
7251: 20 13      JR      NZ,$7266        
7253: 21 D0 C3   LD      HL,$C3D0        
7256: 09         ADD     HL,BC           
7257: 5E         LD      E,(HL)          
7258: 50         LD      D,B             
7259: 21 44 72   LD      HL,$7244        
725C: 19         ADD     HL,DE           
725D: 7E         LD      A,(HL)          
725E: 21 50 C4   LD      HL,$C450        
7261: 09         ADD     HL,BC           
7262: 77         LD      (HL),A          
7263: CD 8D 3B   CALL    $3B8D           
7266: C3 39 72   JP      $7239           
7269: 21 50 C4   LD      HL,$C450        
726C: 09         ADD     HL,BC           
726D: 7E         LD      A,(HL)          
726E: A7         AND     A               
726F: 20 18      JR      NZ,$7289        
7271: 21 40 C3   LD      HL,$C340        
7274: 09         ADD     HL,BC           
7275: CB B6      SET     1,E             
7277: 3E 20      LD      A,$20           
7279: CD 25 3C   CALL    $3C25           
727C: 21 20 C3   LD      HL,$C320        
727F: 09         ADD     HL,BC           
7280: 36 F4      LD      (HL),$F4        
7282: 3E 31      LD      A,$31           
7284: E0 F2      LDFF00  ($F2),A         
7286: CD 8D 3B   CALL    $3B8D           
7289: C3 39 72   JP      $7239           
728C: CD B4 3B   CALL    $3BB4           
728F: CD 36 72   CALL    $7236           
7292: CD 06 7E   CALL    $7E06           
7295: F0 E7      LD      A,($E7)         
7297: E6 03      AND     $03             
7299: 20 0A      JR      NZ,$72A5        
729B: 21 20 C3   LD      HL,$C320        
729E: 09         ADD     HL,BC           
729F: 7E         LD      A,(HL)          
72A0: FE 0C      CP      $0C             
72A2: 28 01      JR      Z,$72A5         
72A4: 34         INC     (HL)            
72A5: F0 EC      LD      A,($EC)         
72A7: FE 88      CP      $88             
72A9: 30 05      JR      NC,$72B0        
72AB: F0 EE      LD      A,($EE)         
72AD: FE A8      CP      $A8             
72AF: D8         RET     C               
72B0: CD 8D 3B   CALL    $3B8D           
72B3: 3E FF      LD      A,$FF           
72B5: CD 87 3B   CALL    $3B87           
72B8: C9         RET                     
72B9: C9         RET                     
72BA: 7A         LD      A,D             
72BB: 10 7E      STOP    $7E             
72BD: 30 7A      JR      NC,$7339        
72BF: 30 7E      JR      NC,$733F        
72C1: 10 7C      STOP    $7C             
72C3: 10 7C      STOP    $7C             
72C5: 30 F0      JR      NC,$72B7        
72C7: F8 E6      LDHL    SP,$E6          
72C9: 20 C2      JR      NZ,$728D        
72CB: 76         HALT                    
72CC: 7E         LD      A,(HL)          
72CD: 21 B0 C2   LD      HL,$C2B0        
72D0: 09         ADD     HL,BC           
72D1: 7E         LD      A,(HL)          
72D2: A7         AND     A               
72D3: 28 20      JR      Z,$72F5         
72D5: 11 BA 72   LD      DE,$72BA        
72D8: CD D0 3C   CALL    $3CD0           
72DB: CD 61 7D   CALL    $7D61           
72DE: CD CD 7D   CALL    $7DCD           
72E1: CD 06 7E   CALL    $7E06           
72E4: 21 20 C3   LD      HL,$C320        
72E7: 09         ADD     HL,BC           
72E8: 35         DEC     (HL)            
72E9: 35         DEC     (HL)            
72EA: 21 10 C3   LD      HL,$C310        
72ED: 09         ADD     HL,BC           
72EE: 7E         LD      A,(HL)          
72EF: E6 80      AND     $80             
72F1: C2 76 7E   JP      NZ,$7E76        
72F4: C9         RET                     
72F5: 21 20 C4   LD      HL,$C420        
72F8: 09         ADD     HL,BC           
72F9: 7E         LD      A,(HL)          
72FA: A7         AND     A               
72FB: 28 04      JR      Z,$7301         
72FD: 3E 07      LD      A,$07           
72FF: E0 F1      LDFF00  ($F1),A         
7301: CD 3B 76   CALL    $763B           
7304: F0 F0      LD      A,($F0)         
7306: A7         AND     A               
7307: 20 1F      JR      NZ,$7328        
7309: FA 4A DB   LD      A,($DB4A)       
730C: FE 02      CP      $02             
730E: 20 18      JR      NZ,$7328        
7310: FA 66 C1   LD      A,($C166)       
7313: A7         AND     A               
7314: 28 12      JR      Z,$7328         
7316: CD 8D 3B   CALL    $3B8D           
7319: 21 30 C4   LD      HL,$C430        
731C: 09         ADD     HL,BC           
731D: CB FE      SET     1,E             
731F: CB D6      SET     1,E             
7321: 21 60 C3   LD      HL,$C360        
7324: 09         ADD     HL,BC           
7325: 36 10      LD      (HL),$10        
7327: C9         RET                     
7328: F0 EA      LD      A,($EA)         
732A: FE 05      CP      $05             
732C: 28 15      JR      Z,$7343         
732E: CD 7C 7E   CALL    $7E7C           
7331: 21 80 C2   LD      HL,$C280        
7334: 09         ADD     HL,BC           
7335: 7E         LD      A,(HL)          
7336: A7         AND     A               
7337: 20 09      JR      NZ,$7342        
7339: 21 10 D8   LD      HL,$D810        
733C: CB EE      SET     1,E             
733E: 3E 02      LD      A,$02           
7340: E0 F2      LDFF00  ($F2),A         
7342: C9         RET                     
7343: CD 61 7D   CALL    $7D61           
7346: CD E2 08   CALL    $08E2           
7349: CD EB 3B   CALL    $3BEB           
734C: F0 F0      LD      A,($F0)         
734E: FE 05      CP      $05             
7350: 30 05      JR      NC,$7357        
7352: CD AF 7C   CALL    $7CAF           
7355: 18 03      JR      $735A           
7357: CD BF 3B   CALL    $3BBF           
735A: F0 F0      LD      A,($F0)         
735C: C7         RST     0X00            
735D: 75         LD      (HL),L          
735E: 73         LD      (HL),E          
735F: 76         HALT                    
7360: 73         LD      (HL),E          
7361: 89         ADC     A,C             
7362: 73         LD      (HL),E          
7363: D3         ???                     
7364: 73         LD      (HL),E          
7365: 42         LD      B,D             
7366: 74         LD      (HL),H          
7367: 64         LD      H,H             
7368: 74         LD      (HL),H          
7369: 8F         ADC     A,A             
736A: 74         LD      (HL),H          
736B: A0         AND     B               
736C: 74         LD      (HL),H          
736D: B7         OR      A               
736E: 74         LD      (HL),H          
736F: EC         ???                     
7370: 74         LD      (HL),H          
7371: 08 75 1C   LD      ($1C75),SP      
7374: 75         LD      (HL),L          
7375: C9         RET                     
7376: CD 91 08   CALL    $0891           
7379: 36 80      LD      (HL),$80        
737B: 3E 39      LD      A,$39           
737D: EA 68 D3   LD      ($D368),A       
7380: E0 B0      LDFF00  ($B0),A         
7382: E0 BD      LDFF00  ($BD),A         
7384: E0 BF      LDFF00  ($BF),A         
7386: C3 8D 3B   JP      $3B8D           
7389: F0 EE      LD      A,($EE)         
738B: 21 40 C4   LD      HL,$C440        
738E: 09         ADD     HL,BC           
738F: 77         LD      (HL),A          
7390: F0 EC      LD      A,($EC)         
7392: 21 D0 C2   LD      HL,$C2D0        
7395: 09         ADD     HL,BC           
7396: D6 14      SUB     $14             
7398: 77         LD      (HL),A          
7399: CD 91 08   CALL    $0891           
739C: 20 06      JR      NZ,$73A4        
739E: 36 FF      LD      (HL),$FF        
73A0: CD 8D 3B   CALL    $3B8D           
73A3: C9         RET                     
73A4: 1E 08      LD      E,$08           
73A6: E6 04      AND     $04             
73A8: 28 02      JR      Z,$73AC         
73AA: 1E F8      LD      E,$F8           
73AC: 21 40 C2   LD      HL,$C240        
73AF: 09         ADD     HL,BC           
73B0: 73         LD      (HL),E          
73B1: CD DA 7D   CALL    $7DDA           
73B4: C9         RET                     
73B5: F8 08      LDHL    SP,$08          
73B7: 10 00      STOP    $00             
73B9: 00         NOP                     
73BA: 08 F0 00   LD      ($00F0),SP      
73BD: F0 00      LD      A,($00)         
73BF: F0 F0      LD      A,($F0)         
73C1: F8 08      LDHL    SP,$08          
73C3: 08 F8 F8   LD      ($F8F8),SP      
73C6: 08 FC 02   LD      ($02FC),SP      
73C9: FC         ???                     
73CA: 02         LD      (BC),A          
73CB: FC         ???                     
73CC: FC         ???                     
73CD: 10 10      STOP    $10             
73CF: 10 10      STOP    $10             
73D1: 10 10      STOP    $10             
73D3: CD 91 08   CALL    $0891           
73D6: 20 06      JR      NZ,$73DE        
73D8: 36 80      LD      (HL),$80        
73DA: CD 8D 3B   CALL    $3B8D           
73DD: C9         RET                     
73DE: E6 1F      AND     $1F             
73E0: 20 5F      JR      NZ,$7441        
73E2: F0 F1      LD      A,($F1)         
73E4: FE 06      CP      $06             
73E6: 28 4E      JR      Z,$7436         
73E8: 3E 13      LD      A,$13           
73EA: E0 F4      LDFF00  ($F4),A         
73EC: 3E 7F      LD      A,$7F           
73EE: CD 01 3C   CALL    $3C01           
73F1: C5         PUSH    BC              
73F2: F0 F1      LD      A,($F1)         
73F4: 4F         LD      C,A             
73F5: 21 B0 C3   LD      HL,$C3B0        
73F8: 19         ADD     HL,DE           
73F9: 77         LD      (HL),A          
73FA: 21 B5 73   LD      HL,$73B5        
73FD: 09         ADD     HL,BC           
73FE: F0 D7      LD      A,($D7)         
7400: 86         ADD     A,(HL)          
7401: 21 00 C2   LD      HL,$C200        
7404: 19         ADD     HL,DE           
7405: 77         LD      (HL),A          
7406: 21 BB 73   LD      HL,$73BB        
7409: 09         ADD     HL,BC           
740A: F0 D8      LD      A,($D8)         
740C: 86         ADD     A,(HL)          
740D: 21 10 C2   LD      HL,$C210        
7410: 19         ADD     HL,DE           
7411: 77         LD      (HL),A          
7412: 21 C1 73   LD      HL,$73C1        
7415: 09         ADD     HL,BC           
7416: 7E         LD      A,(HL)          
7417: 21 40 C2   LD      HL,$C240        
741A: 19         ADD     HL,DE           
741B: 77         LD      (HL),A          
741C: 21 C7 73   LD      HL,$73C7        
741F: 09         ADD     HL,BC           
7420: 7E         LD      A,(HL)          
7421: 21 50 C2   LD      HL,$C250        
7424: 19         ADD     HL,DE           
7425: 77         LD      (HL),A          
7426: 21 CD 73   LD      HL,$73CD        
7429: 09         ADD     HL,BC           
742A: 7E         LD      A,(HL)          
742B: 21 20 C3   LD      HL,$C320        
742E: 19         ADD     HL,DE           
742F: 77         LD      (HL),A          
7430: 21 B0 C2   LD      HL,$C2B0        
7433: 19         ADD     HL,DE           
7434: 77         LD      (HL),A          
7435: C1         POP     BC              
7436: 21 B0 C3   LD      HL,$C3B0        
7439: 09         ADD     HL,BC           
743A: 7E         LD      A,(HL)          
743B: FE 07      CP      $07             
743D: 28 02      JR      Z,$7441         
743F: 3C         INC     A               
7440: 77         LD      (HL),A          
7441: C9         RET                     
7442: CD 91 08   CALL    $0891           
7445: 20 05      JR      NZ,$744C        
7447: 36 80      LD      (HL),$80        
7449: C3 8D 3B   JP      $3B8D           
744C: 1E 07      LD      E,$07           
744E: FE 60      CP      $60             
7450: 30 0C      JR      NC,$745E        
7452: FE 40      CP      $40             
7454: 30 09      JR      NC,$745F        
7456: FE 30      CP      $30             
7458: 38 04      JR      C,$745E         
745A: FE 20      CP      $20             
745C: 38 01      JR      C,$745F         
745E: 1C         INC     E               
745F: 7B         LD      A,E             
7460: CD 87 3B   CALL    $3B87           
7463: C9         RET                     
7464: CD 91 08   CALL    $0891           
7467: 20 1C      JR      NZ,$7485        
7469: 36 40      LD      (HL),$40        
746B: 21 40 C3   LD      HL,$C340        
746E: 09         ADD     HL,BC           
746F: CB BE      SET     1,E             
7471: 21 30 C4   LD      HL,$C430        
7474: 09         ADD     HL,BC           
7475: CB B6      SET     1,E             
7477: CD 8D 3B   CALL    $3B8D           
747A: F0 EE      LD      A,($EE)         
747C: EA 01 D2   LD      ($D201),A       
747F: F0 EC      LD      A,($EC)         
7481: EA 02 D2   LD      ($D202),A       
7484: C9         RET                     
7485: 21 50 C2   LD      HL,$C250        
7488: 09         ADD     HL,BC           
7489: 36 04      LD      (HL),$04        
748B: CD D0 7D   CALL    $7DD0           
748E: C9         RET                     
748F: CD 91 08   CALL    $0891           
7492: 20 0B      JR      NZ,$749F        
7494: 36 20      LD      (HL),$20        
7496: 21 40 C2   LD      HL,$C240        
7499: 09         ADD     HL,BC           
749A: 36 08      LD      (HL),$08        
749C: CD 8D 3B   CALL    $3B8D           
749F: C9         RET                     
74A0: CD 91 08   CALL    $0891           
74A3: 20 0E      JR      NZ,$74B3        
74A5: CD 91 08   CALL    $0891           
74A8: CD ED 27   CALL    $27ED           
74AB: E6 1F      AND     $1F             
74AD: C6 08      ADD     $08             
74AF: 77         LD      (HL),A          
74B0: CD 8D 3B   CALL    $3B8D           
74B3: CD DA 7D   CALL    $7DDA           
74B6: C9         RET                     
74B7: CD 91 08   CALL    $0891           
74BA: 20 2F      JR      NZ,$74EB        
74BC: 21 90 C3   LD      HL,$C390        
74BF: 09         ADD     HL,BC           
74C0: 34         INC     (HL)            
74C1: 7E         LD      A,(HL)          
74C2: FE 03      CP      $03             
74C4: 38 13      JR      C,$74D9         
74C6: CD ED 27   CALL    $27ED           
74C9: E6 01      AND     $01             
74CB: 20 0C      JR      NZ,$74D9        
74CD: CD 8D 3B   CALL    $3B8D           
74D0: 3E 09      LD      A,$09           
74D2: 77         LD      (HL),A          
74D3: CD 91 08   CALL    $0891           
74D6: 36 20      LD      (HL),$20        
74D8: C9         RET                     
74D9: CD 91 08   CALL    $0891           
74DC: 36 40      LD      (HL),$40        
74DE: CD 8D 3B   CALL    $3B8D           
74E1: 35         DEC     (HL)            
74E2: 35         DEC     (HL)            
74E3: 21 40 C2   LD      HL,$C240        
74E6: 09         ADD     HL,BC           
74E7: 7E         LD      A,(HL)          
74E8: 2F         CPL                     
74E9: 3C         INC     A               
74EA: 77         LD      (HL),A          
74EB: C9         RET                     
74EC: CD 91 08   CALL    $0891           
74EF: 20 16      JR      NZ,$7507        
74F1: 36 20      LD      (HL),$20        
74F3: 3E 18      LD      A,$18           
74F5: CD 25 3C   CALL    $3C25           
74F8: 21 50 C2   LD      HL,$C250        
74FB: 09         ADD     HL,BC           
74FC: 7E         LD      A,(HL)          
74FD: CB 7E      SET     1,E             
74FF: 28 03      JR      Z,$7504         
7501: 2F         CPL                     
7502: 3C         INC     A               
7503: 77         LD      (HL),A          
7504: CD 8D 3B   CALL    $3B8D           
7507: C9         RET                     
7508: 21 20 C4   LD      HL,$C420        
750B: 09         ADD     HL,BC           
750C: 7E         LD      A,(HL)          
750D: A7         AND     A               
750E: 20 05      JR      NZ,$7515        
7510: CD 91 08   CALL    $0891           
7513: 20 03      JR      NZ,$7518        
7515: CD 8D 3B   CALL    $3B8D           
7518: CD CD 7D   CALL    $7DCD           
751B: C9         RET                     
751C: F0 98      LD      A,($98)         
751E: F5         PUSH    AF              
751F: F0 99      LD      A,($99)         
7521: F5         PUSH    AF              
7522: FA 01 D2   LD      A,($D201)       
7525: E0 98      LDFF00  ($98),A         
7527: FA 02 D2   LD      A,($D202)       
752A: E0 99      LDFF00  ($99),A         
752C: 3E 08      LD      A,$08           
752E: CD 25 3C   CALL    $3C25           
7531: FA 01 D2   LD      A,($D201)       
7534: 21 EE FF   LD      HL,$FFEE        
7537: 96         SUB     (HL)            
7538: C6 01      ADD     $01             
753A: FE 02      CP      $02             
753C: 30 17      JR      NC,$7555        
753E: FA 02 D2   LD      A,($D202)       
7541: 21 EC FF   LD      HL,$FFEC        
7544: 96         SUB     (HL)            
7545: C6 01      ADD     $01             
7547: FE 02      CP      $02             
7549: 30 0A      JR      NC,$7555        
754B: CD 8D 3B   CALL    $3B8D           
754E: 36 06      LD      (HL),$06        
7550: CD 91 08   CALL    $0891           
7553: 36 20      LD      (HL),$20        
7555: F1         POP     AF              
7556: E0 99      LDFF00  ($99),A         
7558: F1         POP     AF              
7559: E0 98      LDFF00  ($98),A         
755B: CD CD 7D   CALL    $7DCD           
755E: C9         RET                     
755F: F0 F8      LD      A,($F8)         
7561: 7A         LD      A,D             
7562: 10 F0      STOP    $F0             
7564: 00         NOP                     
7565: 7C         LD      A,H             
7566: 10 F0      STOP    $F0             
7568: 08 7C 30   LD      ($307C),SP      
756B: F0 10      LD      A,($10)         
756D: 7A         LD      A,D             
756E: 30 00      JR      NC,$7570        
7570: 00         NOP                     
7571: 7E         LD      A,(HL)          
7572: 10 00      STOP    $00             
7574: 08 7E 30   LD      ($307E),SP      
7577: F0 F8      LD      A,($F8)         
7579: 70         LD      (HL),B          
757A: 00         NOP                     
757B: F0 00      LD      A,($00)         
757D: 7C         LD      A,H             
757E: 10 F0      STOP    $F0             
7580: 08 7C 30   LD      ($307C),SP      
7583: F0 10      LD      A,($10)         
7585: 7A         LD      A,D             
7586: 30 00      JR      NC,$7588        
7588: 00         NOP                     
7589: 7E         LD      A,(HL)          
758A: 10 00      STOP    $00             
758C: 08 7E 30   LD      ($307E),SP      
758F: F0 F8      LD      A,($F8)         
7591: 70         LD      (HL),B          
7592: 00         NOP                     
7593: F0 00      LD      A,($00)         
7595: 7C         LD      A,H             
7596: 10 F0      STOP    $F0             
7598: 08 7C 30   LD      ($307C),SP      
759B: F0 10      LD      A,($10)         
759D: 7A         LD      A,D             
759E: 30 00      JR      NC,$75A0        
75A0: 00         NOP                     
75A1: 7E         LD      A,(HL)          
75A2: 10 00      STOP    $00             
75A4: 08 74 20   LD      ($2074),SP      
75A7: F0 F8      LD      A,($F8)         
75A9: 70         LD      (HL),B          
75AA: 00         NOP                     
75AB: F0 00      LD      A,($00)         
75AD: 7C         LD      A,H             
75AE: 10 F0      STOP    $F0             
75B0: 08 7C 30   LD      ($307C),SP      
75B3: F0 10      LD      A,($10)         
75B5: 70         LD      (HL),B          
75B6: 20 00      JR      NZ,$75B8        
75B8: 00         NOP                     
75B9: 7E         LD      A,(HL)          
75BA: 10 00      STOP    $00             
75BC: 08 74 20   LD      ($2074),SP      
75BF: F0 F8      LD      A,($F8)         
75C1: 70         LD      (HL),B          
75C2: 00         NOP                     
75C3: F0 00      LD      A,($00)         
75C5: 7C         LD      A,H             
75C6: 10 F0      STOP    $F0             
75C8: 08 7C 30   LD      ($307C),SP      
75CB: F0 10      LD      A,($10)         
75CD: 70         LD      (HL),B          
75CE: 20 00      JR      NZ,$75D0        
75D0: 00         NOP                     
75D1: 74         LD      (HL),H          
75D2: 00         NOP                     
75D3: 00         NOP                     
75D4: 08 74 20   LD      ($2074),SP      
75D7: F0 F8      LD      A,($F8)         
75D9: 70         LD      (HL),B          
75DA: 00         NOP                     
75DB: F0 00      LD      A,($00)         
75DD: 78         LD      A,B             
75DE: 00         NOP                     
75DF: F0 08      LD      A,($08)         
75E1: 7C         LD      A,H             
75E2: 30 F0      JR      NC,$75D4        
75E4: 10 70      STOP    $70             
75E6: 20 00      JR      NZ,$75E8        
75E8: 00         NOP                     
75E9: 74         LD      (HL),H          
75EA: 00         NOP                     
75EB: 00         NOP                     
75EC: 08 74 20   LD      ($2074),SP      
75EF: F0 F8      LD      A,($F8)         
75F1: 70         LD      (HL),B          
75F2: 00         NOP                     
75F3: F0 00      LD      A,($00)         
75F5: 78         LD      A,B             
75F6: 00         NOP                     
75F7: F0 08      LD      A,($08)         
75F9: 78         LD      A,B             
75FA: 20 F0      JR      NZ,$75EC        
75FC: 10 70      STOP    $70             
75FE: 20 00      JR      NZ,$7600        
7600: 00         NOP                     
7601: 74         LD      (HL),H          
7602: 00         NOP                     
7603: 00         NOP                     
7604: 08 74 20   LD      ($2074),SP      
7607: F0 F8      LD      A,($F8)         
7609: 70         LD      (HL),B          
760A: 00         NOP                     
760B: F0 00      LD      A,($00)         
760D: 78         LD      A,B             
760E: 00         NOP                     
760F: F0 08      LD      A,($08)         
7611: 78         LD      A,B             
7612: 20 F0      JR      NZ,$7604        
7614: 10 70      STOP    $70             
7616: 20 00      JR      NZ,$7618        
7618: 00         NOP                     
7619: 74         LD      (HL),H          
761A: 00         NOP                     
761B: 00         NOP                     
761C: 08 74 20   LD      ($2074),SP      
761F: F0 F8      LD      A,($F8)         
7621: 70         LD      (HL),B          
7622: 00         NOP                     
7623: F0 00      LD      A,($00)         
7625: 72         LD      (HL),D          
7626: 00         NOP                     
7627: F0 08      LD      A,($08)         
7629: 72         LD      (HL),D          
762A: 20 F0      JR      NZ,$761C        
762C: 10 70      STOP    $70             
762E: 20 00      JR      NZ,$7630        
7630: 00         NOP                     
7631: 74         LD      (HL),H          
7632: 00         NOP                     
7633: 00         NOP                     
7634: 08 74 20   LD      ($2074),SP      
7637: 76         HALT                    
7638: 00         NOP                     
7639: 76         HALT                    
763A: 20 F0      JR      NZ,$762C        
763C: F1         POP     AF              
763D: 17         RLA                     
763E: 17         RLA                     
763F: 17         RLA                     
7640: E6 F8      AND     $F8             
7642: 5F         LD      E,A             
7643: 17         RLA                     
7644: 83         ADD     A,E             
7645: 5F         LD      E,A             
7646: 50         LD      D,B             
7647: 21 5F 75   LD      HL,$755F        
764A: 19         ADD     HL,DE           
764B: 0E 06      LD      C,$06           
764D: CD 26 3D   CALL    $3D26           
7650: 3E 06      LD      A,$06           
7652: CD D0 3D   CALL    $3DD0           
7655: F0 EA      LD      A,($EA)         
7657: FE 01      CP      $01             
7659: 28 07      JR      Z,$7662         
765B: F0 F0      LD      A,($F0)         
765D: FE 05      CP      $05             
765F: DA F7 76   JP      C,$76F7         
7662: 21 40 C4   LD      HL,$C440        
7665: 09         ADD     HL,BC           
7666: 7E         LD      A,(HL)          
7667: E0 E8      LDFF00  ($E8),A         
7669: F0 EE      LD      A,($EE)         
766B: 96         SUB     (HL)            
766C: CB 2F      SET     1,E             
766E: E0 E1      LDFF00  ($E1),A         
7670: CB 2F      SET     1,E             
7672: E0 E2      LDFF00  ($E2),A         
7674: CB 2F      SET     1,E             
7676: E0 E3      LDFF00  ($E3),A         
7678: CB 2F      SET     1,E             
767A: E0 E4      LDFF00  ($E4),A         
767C: CB 2F      SET     1,E             
767E: E0 E5      LDFF00  ($E5),A         
7680: CB 2F      SET     1,E             
7682: E0 E6      LDFF00  ($E6),A         
7684: 21 D0 C2   LD      HL,$C2D0        
7687: 09         ADD     HL,BC           
7688: 7E         LD      A,(HL)          
7689: E0 E9      LDFF00  ($E9),A         
768B: F0 EC      LD      A,($EC)         
768D: D6 20      SUB     $20             
768F: BE         CP      (HL)            
7690: 38 65      JR      C,$76F7         
7692: E0 EC      LDFF00  ($EC),A         
7694: AF         XOR     A               
7695: E0 F1      LDFF00  ($F1),A         
7697: 21 E1 FF   LD      HL,$FFE1        
769A: F0 E8      LD      A,($E8)         
769C: 86         ADD     A,(HL)          
769D: E0 EE      LDFF00  ($EE),A         
769F: 23         INC     HL              
76A0: E5         PUSH    HL              
76A1: 11 37 76   LD      DE,$7637        
76A4: CD 3B 3C   CALL    $3C3B           
76A7: FA C7 DB   LD      A,($DBC7)       
76AA: A7         AND     A               
76AB: 20 3B      JR      NZ,$76E8        
76AD: 21 EC FF   LD      HL,$FFEC        
76B0: F0 99      LD      A,($99)         
76B2: 96         SUB     (HL)            
76B3: C6 0C      ADD     $0C             
76B5: FE 18      CP      $18             
76B7: 30 2F      JR      NC,$76E8        
76B9: 21 EE FF   LD      HL,$FFEE        
76BC: F0 98      LD      A,($98)         
76BE: 96         SUB     (HL)            
76BF: 5F         LD      E,A             
76C0: C6 0C      ADD     $0C             
76C2: FE 18      CP      $18             
76C4: 30 22      JR      NC,$76E8        
76C6: 7B         LD      A,E             
76C7: 1E 20      LD      E,$20           
76C9: E6 80      AND     $80             
76CB: 28 02      JR      Z,$76CF         
76CD: 1E E0      LD      E,$E0           
76CF: 7B         LD      A,E             
76D0: E0 9A      LDFF00  ($9A),A         
76D2: AF         XOR     A               
76D3: E0 9B      LDFF00  ($9B),A         
76D5: 3E 18      LD      A,$18           
76D7: EA 3E C1   LD      ($C13E),A       
76DA: 3E 10      LD      A,$10           
76DC: EA C7 DB   LD      ($DBC7),A       
76DF: 3E 08      LD      A,$08           
76E1: EA 94 DB   LD      ($DB94),A       
76E4: 3E 03      LD      A,$03           
76E6: E0 F3      LDFF00  ($F3),A         
76E8: E1         POP     HL              
76E9: F0 E9      LD      A,($E9)         
76EB: 5F         LD      E,A             
76EC: F0 EC      LD      A,($EC)         
76EE: D6 10      SUB     $10             
76F0: E0 EC      LDFF00  ($EC),A         
76F2: 93         SUB     E               
76F3: E6 80      AND     $80             
76F5: 28 A3      JR      Z,$769A         
76F7: CD BA 3D   CALL    $3DBA           
76FA: C9         RET                     
76FB: 62         LD      H,D             
76FC: 00         NOP                     
76FD: 64         LD      H,H             
76FE: 00         NOP                     
76FF: 60         LD      H,B             
7700: 00         NOP                     
7701: 60         LD      H,B             
7702: 20 64      JR      NZ,$7768        
7704: 20 62      JR      NZ,$7768        
7706: 20 66      JR      NZ,$776E        
7708: 00         NOP                     
7709: 68         LD      L,B             
770A: 00         NOP                     
770B: 60         LD      H,B             
770C: 00         NOP                     
770D: 60         LD      H,B             
770E: 20 68      JR      NZ,$7778        
7710: 20 66      JR      NZ,$7778        
7712: 20 6C      JR      NZ,$7780        
7714: 00         NOP                     
7715: 6E         LD      L,(HL)          
7716: 00         NOP                     
7717: 6A         LD      L,D             
7718: 00         NOP                     
7719: 6A         LD      L,D             
771A: 20 6E      JR      NZ,$778A        
771C: 20 6C      JR      NZ,$778A        
771E: 20 00      JR      NZ,$7720        
7720: 01 02 01   LD      BC,$0102        
7723: 03         INC     BC              
7724: 04         INC     B               
7725: 05         DEC     B               
7726: 04         INC     B               
7727: 06 07      LD      B,$07           
7729: 08 07 11   LD      ($1107),SP      
772C: FB         EI                      
772D: 76         HALT                    
772E: CD 3B 3C   CALL    $3C3B           
7731: CD 61 7D   CALL    $7D61           
7734: CD 83 7D   CALL    $7D83           
7737: CD B4 3B   CALL    $3BB4           
773A: F0 F0      LD      A,($F0)         
773C: C7         RST     0X00            
773D: 4B         LD      C,E             
773E: 77         LD      (HL),A          
773F: A5         AND     L               
7740: 77         LD      (HL),A          
7741: FA FC 00   LD      A,($00FC)       
7744: 04         INC     B               
7745: 06 04      LD      B,$04           
7747: 00         NOP                     
7748: FC         ???                     
7749: FA FC CD   LD      A,($CDFC)       
774C: 91         SUB     C               
774D: 08 20 20   LD      ($2020),SP      
7750: CD ED 27   CALL    $27ED           
7753: E6 3F      AND     $3F             
7755: C6 30      ADD     $30             
7757: 77         LD      (HL),A          
7758: E6 07      AND     $07             
775A: 5F         LD      E,A             
775B: 50         LD      D,B             
775C: 21 43 77   LD      HL,$7743        
775F: 19         ADD     HL,DE           
7760: 7E         LD      A,(HL)          
7761: 21 40 C2   LD      HL,$C240        
7764: 09         ADD     HL,BC           
7765: 77         LD      (HL),A          
7766: 21 41 77   LD      HL,$7741        
7769: 19         ADD     HL,DE           
776A: 7E         LD      A,(HL)          
776B: 21 50 C2   LD      HL,$C250        
776E: 09         ADD     HL,BC           
776F: 77         LD      (HL),A          
7770: CD CD 7D   CALL    $7DCD           
7773: CD 9E 3B   CALL    $3B9E           
7776: 21 B0 C2   LD      HL,$C2B0        
7779: 09         ADD     HL,BC           
777A: 7E         LD      A,(HL)          
777B: 21 1F 77   LD      HL,$771F        
777E: A7         AND     A               
777F: 28 15      JR      Z,$7796         
7781: CD 0E 7D   CALL    $7D0E           
7784: 30 0D      JR      NC,$7793        
7786: 21 C0 C2   LD      HL,$C2C0        
7789: 09         ADD     HL,BC           
778A: 7E         LD      A,(HL)          
778B: E6 03      AND     $03             
778D: C6 7C      ADD     $7C             
778F: 34         INC     (HL)            
7790: CD 8E 21   CALL    $218E           
7793: 21 27 77   LD      HL,$7727        
7796: F0 E7      LD      A,($E7)         
7798: 1F         RRA                     
7799: 1F         RRA                     
779A: 1F         RRA                     
779B: E6 03      AND     $03             
779D: 5F         LD      E,A             
779E: 50         LD      D,B             
779F: 19         ADD     HL,DE           
77A0: 7E         LD      A,(HL)          
77A1: CD 87 3B   CALL    $3B87           
77A4: C9         RET                     
77A5: CD 91 08   CALL    $0891           
77A8: 20 05      JR      NZ,$77AF        
77AA: CD 8D 3B   CALL    $3B8D           
77AD: 70         LD      (HL),B          
77AE: C9         RET                     
77AF: 21 23 77   LD      HL,$7723        
77B2: CD 96 77   CALL    $7796           
77B5: C9         RET                     
77B6: 00         NOP                     
77B7: FC         ???                     
77B8: 70         LD      (HL),B          
77B9: 00         NOP                     
77BA: 00         NOP                     
77BB: 04         INC     B               
77BC: 72         LD      (HL),D          
77BD: 00         NOP                     
77BE: 00         NOP                     
77BF: 0C         INC     C               
77C0: 70         LD      (HL),B          
77C1: 20 00      JR      NZ,$77C3        
77C3: FC         ???                     
77C4: 74         LD      (HL),H          
77C5: 00         NOP                     
77C6: 00         NOP                     
77C7: 04         INC     B               
77C8: 72         LD      (HL),D          
77C9: 00         NOP                     
77CA: 00         NOP                     
77CB: 0C         INC     C               
77CC: 74         LD      (HL),H          
77CD: 20 00      JR      NZ,$77CF        
77CF: FC         ???                     
77D0: 76         HALT                    
77D1: 00         NOP                     
77D2: 00         NOP                     
77D3: 04         INC     B               
77D4: 72         LD      (HL),D          
77D5: 00         NOP                     
77D6: 00         NOP                     
77D7: 0C         INC     C               
77D8: 76         HALT                    
77D9: 20 00      JR      NZ,$77DB        
77DB: FC         ???                     
77DC: 74         LD      (HL),H          
77DD: 00         NOP                     
77DE: 00         NOP                     
77DF: 04         INC     B               
77E0: 72         LD      (HL),D          
77E1: 00         NOP                     
77E2: 00         NOP                     
77E3: 0C         INC     C               
77E4: 74         LD      (HL),H          
77E5: 20 10      JR      NZ,$77F7        
77E7: 11 12 11   LD      DE,$1112        
77EA: F0 F1      LD      A,($F1)         
77EC: 17         RLA                     
77ED: 17         RLA                     
77EE: E6 FC      AND     $FC             
77F0: 5F         LD      E,A             
77F1: 17         RLA                     
77F2: E6 F8      AND     $F8             
77F4: 83         ADD     A,E             
77F5: 5F         LD      E,A             
77F6: 50         LD      D,B             
77F7: 21 B6 77   LD      HL,$77B6        
77FA: 19         ADD     HL,DE           
77FB: 0E 03      LD      C,$03           
77FD: CD 26 3D   CALL    $3D26           
7800: CD 61 7D   CALL    $7D61           
7803: CD 19 3D   CALL    $3D19           
7806: 21 D0 C3   LD      HL,$C3D0        
7809: 09         ADD     HL,BC           
780A: 7E         LD      A,(HL)          
780B: 1F         RRA                     
780C: 1F         RRA                     
780D: 1F         RRA                     
780E: E6 03      AND     $03             
7810: 5F         LD      E,A             
7811: 50         LD      D,B             
7812: 21 E6 77   LD      HL,$77E6        
7815: 19         ADD     HL,DE           
7816: 7E         LD      A,(HL)          
7817: 21 10 C3   LD      HL,$C310        
781A: 09         ADD     HL,BC           
781B: 77         LD      (HL),A          
781C: CD 83 7D   CALL    $7D83           
781F: CD CD 7D   CALL    $7DCD           
7822: CD 9E 3B   CALL    $3B9E           
7825: F0 F0      LD      A,($F0)         
7827: C7         RST     0X00            
7828: 38 78      JR      C,$78A2         
782A: 0B         DEC     BC              
782B: 79         LD      A,C             
782C: 1C         INC     E               
782D: 79         LD      A,C             
782E: F8 FA      LDHL    SP,$FA          
7830: 00         NOP                     
7831: 06 08      LD      B,$08           
7833: 06 00      LD      B,$00           
7835: FA F8 FA   LD      A,($FAF8)       
7838: CD 91 08   CALL    $0891           
783B: 20 32      JR      NZ,$786F        
783D: CD ED 27   CALL    $27ED           
7840: E6 1F      AND     $1F             
7842: C6 20      ADD     $20             
7844: 77         LD      (HL),A          
7845: E6 07      AND     $07             
7847: 5F         LD      E,A             
7848: 50         LD      D,B             
7849: 21 30 78   LD      HL,$7830        
784C: 19         ADD     HL,DE           
784D: 7E         LD      A,(HL)          
784E: 21 40 C2   LD      HL,$C240        
7851: 09         ADD     HL,BC           
7852: 77         LD      (HL),A          
7853: 21 2E 78   LD      HL,$782E        
7856: 19         ADD     HL,DE           
7857: 7E         LD      A,(HL)          
7858: 21 50 C2   LD      HL,$C250        
785B: 09         ADD     HL,BC           
785C: 77         LD      (HL),A          
785D: 21 B0 C2   LD      HL,$C2B0        
7860: 09         ADD     HL,BC           
7861: 34         INC     (HL)            
7862: 7E         LD      A,(HL)          
7863: E6 07      AND     $07             
7865: 20 05      JR      NZ,$786C        
7867: 3E 0A      LD      A,$0A           
7869: CD 25 3C   CALL    $3C25           
786C: CD 8D 3B   CALL    $3B8D           
786F: 21 D0 C3   LD      HL,$C3D0        
7872: 09         ADD     HL,BC           
7873: 7E         LD      A,(HL)          
7874: 34         INC     (HL)            
7875: E6 7F      AND     $7F             
7877: 20 41      JR      NZ,$78BA        
7879: 3E 02      LD      A,$02           
787B: CD 01 3C   CALL    $3C01           
787E: 38 3A      JR      C,$78BA         
7880: 21 30 C4   LD      HL,$C430        
7883: 19         ADD     HL,DE           
7884: CB 86      SET     1,E             
7886: F0 D7      LD      A,($D7)         
7888: 21 00 C2   LD      HL,$C200        
788B: 19         ADD     HL,DE           
788C: 77         LD      (HL),A          
788D: F0 D8      LD      A,($D8)         
788F: 21 10 C2   LD      HL,$C210        
7892: 19         ADD     HL,DE           
7893: 77         LD      (HL),A          
7894: F0 DA      LD      A,($DA)         
7896: 21 10 C3   LD      HL,$C310        
7899: 19         ADD     HL,DE           
789A: 77         LD      (HL),A          
789B: 21 20 C3   LD      HL,$C320        
789E: 19         ADD     HL,DE           
789F: 36 08      LD      (HL),$08        
78A1: 21 E0 C2   LD      HL,$C2E0        
78A4: 19         ADD     HL,DE           
78A5: 36 40      LD      (HL),$40        
78A7: 21 40 C4   LD      HL,$C440        
78AA: 19         ADD     HL,DE           
78AB: 36 01      LD      (HL),$01        
78AD: C5         PUSH    BC              
78AE: D5         PUSH    DE              
78AF: C1         POP     BC              
78B0: 3E 10      LD      A,$10           
78B2: CD 25 3C   CALL    $3C25           
78B5: C1         POP     BC              
78B6: 3E 08      LD      A,$08           
78B8: E0 F2      LDFF00  ($F2),A         
78BA: CD 4F 7E   CALL    $7E4F           
78BD: F0 9E      LD      A,($9E)         
78BF: EE 01      XOR     $01             
78C1: BB         CP      E               
78C2: 20 3A      JR      NZ,$78FE        
78C4: CD 20 7E   CALL    $7E20           
78C7: C6 20      ADD     $20             
78C9: FE 40      CP      $40             
78CB: 30 31      JR      NC,$78FE        
78CD: CD 40 7E   CALL    $7E40           
78D0: C6 20      ADD     $20             
78D2: FE 40      CP      $40             
78D4: 30 28      JR      NC,$78FE        
78D6: FA 37 C1   LD      A,($C137)       
78D9: A7         AND     A               
78DA: 28 22      JR      Z,$78FE         
78DC: CD 8D 3B   CALL    $3B8D           
78DF: 36 02      LD      (HL),$02        
78E1: CD 91 08   CALL    $0891           
78E4: 36 12      LD      (HL),$12        
78E6: 3E 20      LD      A,$20           
78E8: CD 30 3C   CALL    $3C30           
78EB: F0 D7      LD      A,($D7)         
78ED: 2F         CPL                     
78EE: 3C         INC     A               
78EF: 21 50 C2   LD      HL,$C250        
78F2: 09         ADD     HL,BC           
78F3: 77         LD      (HL),A          
78F4: F0 D8      LD      A,($D8)         
78F6: 2F         CPL                     
78F7: 3C         INC     A               
78F8: 21 40 C2   LD      HL,$C240        
78FB: 09         ADD     HL,BC           
78FC: 77         LD      (HL),A          
78FD: C9         RET                     
78FE: CD B4 3B   CALL    $3BB4           
7901: F0 E7      LD      A,($E7)         
7903: 1F         RRA                     
7904: 1F         RRA                     
7905: E6 03      AND     $03             
7907: CD 87 3B   CALL    $3B87           
790A: C9         RET                     
790B: CD 91 08   CALL    $0891           
790E: 20 09      JR      NZ,$7919        
7910: 36 20      LD      (HL),$20        
7912: CD 8D 3B   CALL    $3B8D           
7915: 70         LD      (HL),B          
7916: CD AF 3D   CALL    $3DAF           
7919: C3 6F 78   JP      $786F           
791C: CD 91 08   CALL    $0891           
791F: 20 04      JR      NZ,$7925        
7921: CD 8D 3B   CALL    $3B8D           
7924: 70         LD      (HL),B          
7925: C3 01 79   JP      $7901           
7928: 6C         LD      L,H             
7929: 74         LD      (HL),H          
792A: 6D         LD      L,L             
792B: 75         LD      (HL),L          
792C: 64         LD      H,H             
792D: 74         LD      (HL),H          
792E: 65         LD      H,L             
792F: 75         LD      (HL),L          
7930: CD 8A 7A   CALL    $7A8A           
7933: CD 61 7D   CALL    $7D61           
7936: F0 F0      LD      A,($F0)         
7938: A7         AND     A               
7939: C2 02 7A   JP      NZ,$7A02        
793C: CD 91 08   CALL    $0891           
793F: CA EB 79   JP      Z,$79EB         
7942: FE 07      CP      $07             
7944: C2 EE 79   JP      NZ,$79EE        
7947: C5         PUSH    BC              
7948: 21 00 C2   LD      HL,$C200        
794B: 09         ADD     HL,BC           
794C: 7E         LD      A,(HL)          
794D: C6 07      ADD     $07             
794F: D6 08      SUB     $08             
7951: E6 F0      AND     $F0             
7953: E0 CE      LDFF00  ($CE),A         
7955: CB 37      SET     1,E             
7957: 21 10 C2   LD      HL,$C210        
795A: 09         ADD     HL,BC           
795B: 4F         LD      C,A             
795C: 7E         LD      A,(HL)          
795D: C6 07      ADD     $07             
795F: D6 10      SUB     $10             
7961: E6 F0      AND     $F0             
7963: E0 CD      LDFF00  ($CD),A         
7965: B1         OR      C               
7966: 4F         LD      C,A             
7967: 06 00      LD      B,$00           
7969: 21 11 D7   LD      HL,$D711        
796C: 7C         LD      A,H             
796D: 09         ADD     HL,BC           
796E: C5         PUSH    BC              
796F: D1         POP     DE              
7970: 67         LD      H,A             
7971: C1         POP     BC              
7972: 7E         LD      A,(HL)          
7973: E0 AF      LDFF00  ($AF),A         
7975: FE D3      CP      $D3             
7977: 28 04      JR      Z,$797D         
7979: FE 5C      CP      $5C             
797B: 20 1C      JR      NZ,$7999        
797D: FA A5 DB   LD      A,($DBA5)       
7980: A7         AND     A               
7981: 20 16      JR      NZ,$7999        
7983: CD A6 20   CALL    $20A6           
7986: F0 EE      LD      A,($EE)         
7988: E0 D7      LDFF00  ($D7),A         
798A: F0 EC      LD      A,($EC)         
798C: E0 D8      LDFF00  ($D8),A         
798E: 3E 02      LD      A,$02           
7990: CD 53 09   CALL    $0953           
7993: 3E 2F      LD      A,$2F           
7995: E0 F2      LDFF00  ($F2),A         
7997: 18 52      JR      $79EB           
7999: FA A5 DB   LD      A,($DBA5)       
799C: A7         AND     A               
799D: CA EE 79   JP      Z,$79EE         
79A0: F0 AF      LD      A,($AF)         
79A2: FE AB      CP      $AB             
79A4: 20 5B      JR      NZ,$7A01        
79A6: 36 AC      LD      (HL),$AC        
79A8: 54         LD      D,H             
79A9: 5D         LD      E,L             
79AA: 21 B0 C2   LD      HL,$C2B0        
79AD: 09         ADD     HL,BC           
79AE: 72         LD      (HL),D          
79AF: 21 C0 C2   LD      HL,$C2C0        
79B2: 09         ADD     HL,BC           
79B3: 73         LD      (HL),E          
79B4: 21 90 C2   LD      HL,$C290        
79B7: 09         ADD     HL,BC           
79B8: 36 01      LD      (HL),$01        
79BA: CD 87 08   CALL    $0887           
79BD: 36 80      LD      (HL),$80        
79BF: 21 00 C2   LD      HL,$C200        
79C2: 09         ADD     HL,BC           
79C3: F0 CE      LD      A,($CE)         
79C5: 77         LD      (HL),A          
79C6: 21 10 C2   LD      HL,$C210        
79C9: 09         ADD     HL,BC           
79CA: F0 CD      LD      A,($CD)         
79CC: 77         LD      (HL),A          
79CD: 21 A2 C1   LD      HL,$C1A2        
79D0: 34         INC     (HL)            
79D1: FA CD C3   LD      A,($C3CD)       
79D4: A7         AND     A               
79D5: 28 05      JR      Z,$79DC         
79D7: D6 04      SUB     $04             
79D9: EA CD C3   LD      ($C3CD),A       
79DC: CD 91 08   CALL    $0891           
79DF: 70         LD      (HL),B          
79E0: 3E 12      LD      A,$12           
79E2: E0 F4      LDFF00  ($F4),A         
79E4: 11 28 79   LD      DE,$7928        
79E7: D5         PUSH    DE              
79E8: C3 A7 7A   JP      $7AA7           
79EB: C3 76 7E   JP      $7E76           
79EE: FE 10      CP      $10             
79F0: 30 0F      JR      NC,$7A01        
79F2: 21 40 C4   LD      HL,$C440        
79F5: 09         ADD     HL,BC           
79F6: 7E         LD      A,(HL)          
79F7: A7         AND     A               
79F8: C0         RET     NZ              
79F9: 3E 09      LD      A,$09           
79FB: EA 9E C1   LD      ($C19E),A       
79FE: CD F6 3B   CALL    $3BF6           
7A01: C9         RET                     
7A02: CD 87 08   CALL    $0887           
7A05: 20 3A      JR      NZ,$7A41        
7A07: 21 00 C2   LD      HL,$C200        
7A0A: 09         ADD     HL,BC           
7A0B: 7E         LD      A,(HL)          
7A0C: E0 CE      LDFF00  ($CE),A         
7A0E: 21 10 C2   LD      HL,$C210        
7A11: 09         ADD     HL,BC           
7A12: 7E         LD      A,(HL)          
7A13: E0 CD      LDFF00  ($CD),A         
7A15: 21 B0 C2   LD      HL,$C2B0        
7A18: 09         ADD     HL,BC           
7A19: 56         LD      D,(HL)          
7A1A: 21 C0 C2   LD      HL,$C2C0        
7A1D: 09         ADD     HL,BC           
7A1E: 5E         LD      E,(HL)          
7A1F: 3E AB      LD      A,$AB           
7A21: 12         LD      (DE),A          
7A22: CD 76 7E   CALL    $7E76           
7A25: F0 F6      LD      A,($F6)         
7A27: FE 74      CP      $74             
7A29: C8         RET     Z               
7A2A: 21 A2 C1   LD      HL,$C1A2        
7A2D: 35         DEC     (HL)            
7A2E: FA CD C3   LD      A,($C3CD)       
7A31: FE 0C      CP      $0C             
7A33: 30 05      JR      NC,$7A3A        
7A35: C6 04      ADD     $04             
7A37: EA CD C3   LD      ($C3CD),A       
7A3A: 11 2C 79   LD      DE,$792C        
7A3D: D5         PUSH    DE              
7A3E: C3 A7 7A   JP      $7AA7           
7A41: C9         RET                     
7A42: 06 FE      LD      B,$FE           
7A44: 24         INC     H               
7A45: 00         NOP                     
7A46: 03         INC     BC              
7A47: 04         INC     B               
7A48: 24         INC     H               
7A49: 10 05      STOP    $05             
7A4B: 0A         LD      A,(BC)          
7A4C: 24         INC     H               
7A4D: 00         NOP                     
7A4E: 05         DEC     B               
7A4F: FE 24      CP      $24             
7A51: 10 02      STOP    $02             
7A53: 04         INC     B               
7A54: 24         INC     H               
7A55: 00         NOP                     
7A56: 04         INC     B               
7A57: 0A         LD      A,(BC)          
7A58: 24         INC     H               
7A59: 10 03      STOP    $03             
7A5B: FF         RST     0X38            
7A5C: 24         INC     H               
7A5D: 00         NOP                     
7A5E: 01 04 24   LD      BC,$2404        
7A61: 10 02      STOP    $02             
7A63: 09         ADD     HL,BC           
7A64: 24         INC     H               
7A65: 00         NOP                     
7A66: 01 00 24   LD      BC,$2400        
7A69: 10 FF      STOP    $FF             
7A6B: 04         INC     B               
7A6C: 24         INC     H               
7A6D: 00         NOP                     
7A6E: 00         NOP                     
7A6F: 06 24      LD      B,$24           
7A71: 10 00      STOP    $00             
7A73: 01 24 00   LD      BC,$0024        
7A76: FE 03      CP      $03             
7A78: 24         INC     H               
7A79: 10 FF      STOP    $FF             
7A7B: 05         DEC     B               
7A7C: 24         INC     H               
7A7D: 00         NOP                     
7A7E: FF         RST     0X38            
7A7F: 01 24 10   LD      BC,$1024        
7A82: FD         ???                     
7A83: 03         INC     BC              
7A84: 24         INC     H               
7A85: 00         NOP                     
7A86: FE 05      CP      $05             
7A88: 24         INC     H               
7A89: 10 CD      STOP    $CD             
7A8B: 91         SUB     C               
7A8C: 08 28 17   LD      ($1728),SP      
7A8F: 1F         RRA                     
7A90: 1F         RRA                     
7A91: E6 07      AND     $07             
7A93: CB 27      SET     1,E             
7A95: CB 27      SET     1,E             
7A97: 5F         LD      E,A             
7A98: CB 27      SET     1,E             
7A9A: 83         ADD     A,E             
7A9B: 5F         LD      E,A             
7A9C: 50         LD      D,B             
7A9D: 21 42 7A   LD      HL,$7A42        
7AA0: 19         ADD     HL,DE           
7AA1: 0E 03      LD      C,$03           
7AA3: CD 26 3D   CALL    $3D26           
7AA6: C9         RET                     
7AA7: CD 39 28   CALL    $2839           
7AAA: FA 00 D6   LD      A,($D600)       
7AAD: 5F         LD      E,A             
7AAE: 16 00      LD      D,$00           
7AB0: 21 01 D6   LD      HL,$D601        
7AB3: 19         ADD     HL,DE           
7AB4: C6 0A      ADD     $0A             
7AB6: EA 00 D6   LD      ($D600),A       
7AB9: D1         POP     DE              
7ABA: F0 CF      LD      A,($CF)         
7ABC: 22         LD      (HLI),A         
7ABD: F0 D0      LD      A,($D0)         
7ABF: 22         LD      (HLI),A         
7AC0: 3E 81      LD      A,$81           
7AC2: 22         LD      (HLI),A         
7AC3: 1A         LD      A,(DE)          
7AC4: 13         INC     DE              
7AC5: 22         LD      (HLI),A         
7AC6: 1A         LD      A,(DE)          
7AC7: 13         INC     DE              
7AC8: 22         LD      (HLI),A         
7AC9: F0 CF      LD      A,($CF)         
7ACB: 22         LD      (HLI),A         
7ACC: F0 D0      LD      A,($D0)         
7ACE: 3C         INC     A               
7ACF: 22         LD      (HLI),A         
7AD0: 3E 81      LD      A,$81           
7AD2: 22         LD      (HLI),A         
7AD3: 1A         LD      A,(DE)          
7AD4: 13         INC     DE              
7AD5: 22         LD      (HLI),A         
7AD6: 1A         LD      A,(DE)          
7AD7: 22         LD      (HLI),A         
7AD8: AF         XOR     A               
7AD9: 77         LD      (HL),A          
7ADA: C9         RET                     
7ADB: 00         NOP                     
7ADC: 00         NOP                     
7ADD: 01 01 01   LD      BC,$0101        
7AE0: 02         LD      (BC),A          
7AE1: 02         LD      (BC),A          
7AE2: 02         LD      (BC),A          
7AE3: 00         NOP                     
7AE4: 00         NOP                     
7AE5: 0F         RRCA                    
7AE6: 0F         RRCA                    
7AE7: 0F         RRCA                    
7AE8: 0E 0E      LD      C,$0E           
7AEA: 0E 08      LD      C,$08           
7AEC: 08 07 07   LD      ($0707),SP      
7AEF: 07         RLCA                    
7AF0: 06 06      LD      B,$06           
7AF2: 06 08      LD      B,$08           
7AF4: 08 09 09   LD      ($0909),SP      
7AF7: 09         ADD     HL,BC           
7AF8: 0A         LD      A,(BC)          
7AF9: 0A         LD      A,(BC)          
7AFA: 0A         LD      A,(BC)          
7AFB: 04         INC     B               
7AFC: 04         INC     B               
7AFD: 03         INC     BC              
7AFE: 03         INC     BC              
7AFF: 03         INC     BC              
7B00: 02         LD      (BC),A          
7B01: 02         LD      (BC),A          
7B02: 02         LD      (BC),A          
7B03: 0C         INC     C               
7B04: 0C         INC     C               
7B05: 0D         DEC     C               
7B06: 0D         DEC     C               
7B07: 0D         DEC     C               
7B08: 0E 0E      LD      C,$0E           
7B0A: 0E 04      LD      C,$04           
7B0C: 04         INC     B               
7B0D: 05         DEC     B               
7B0E: 05         DEC     B               
7B0F: 05         DEC     B               
7B10: 06 06      LD      B,$06           
7B12: 06 0C      LD      B,$0C           
7B14: 0C         INC     C               
7B15: 0B         DEC     BC              
7B16: 0B         DEC     BC              
7B17: 0B         DEC     BC              
7B18: 0A         LD      A,(BC)          
7B19: 0A         LD      A,(BC)          
7B1A: 0A         LD      A,(BC)          
7B1B: F0 D7      LD      A,($D7)         
7B1D: 07         RLCA                    
7B1E: E6 01      AND     $01             
7B20: 5F         LD      E,A             
7B21: F0 D8      LD      A,($D8)         
7B23: 07         RLCA                    
7B24: 17         RLA                     
7B25: E6 02      AND     $02             
7B27: B3         OR      E               
7B28: 17         RLA                     
7B29: 17         RLA                     
7B2A: 17         RLA                     
7B2B: E6 18      AND     $18             
7B2D: 67         LD      H,A             
7B2E: F0 D8      LD      A,($D8)         
7B30: CB 7F      SET     1,E             
7B32: 28 02      JR      Z,$7B36         
7B34: 2F         CPL                     
7B35: 3C         INC     A               
7B36: 57         LD      D,A             
7B37: F0 D7      LD      A,($D7)         
7B39: CB 7F      SET     1,E             
7B3B: 28 02      JR      Z,$7B3F         
7B3D: 2F         CPL                     
7B3E: 3C         INC     A               
7B3F: BA         CP      D               
7B40: 30 0D      JR      NC,$7B4F        
7B42: CB 2F      SET     1,E             
7B44: CB 2F      SET     1,E             
7B46: 84         ADD     A,H             
7B47: 5F         LD      E,A             
7B48: 50         LD      D,B             
7B49: 21 DB 7A   LD      HL,$7ADB        
7B4C: 19         ADD     HL,DE           
7B4D: 7E         LD      A,(HL)          
7B4E: C9         RET                     
7B4F: 7A         LD      A,D             
7B50: CB 2F      SET     1,E             
7B52: CB 2F      SET     1,E             
7B54: 84         ADD     A,H             
7B55: 5F         LD      E,A             
7B56: 50         LD      D,B             
7B57: 21 FB 7A   LD      HL,$7AFB        
7B5A: 19         ADD     HL,DE           
7B5B: 7E         LD      A,(HL)          
7B5C: C9         RET                     
7B5D: 11 10 0F   LD      DE,$0F10        
7B60: 0E 3E      LD      C,$3E           
7B62: 02         LD      (BC),A          
7B63: E0 A1      LDFF00  ($A1),A         
7B65: EA A4 C1   LD      ($C1A4),A       
7B68: EA C6 C1   LD      ($C1C6),A       
7B6B: 79         LD      A,C             
7B6C: 3C         INC     A               
7B6D: EA A6 C1   LD      ($C1A6),A       
7B70: AF         XOR     A               
7B71: CD 3B 09   CALL    $093B           
7B74: EA 3E C1   LD      ($C13E),A       
7B77: F0 9E      LD      A,($9E)         
7B79: 5F         LD      E,A             
7B7A: 16 00      LD      D,$00           
7B7C: 21 5D 7B   LD      HL,$7B5D        
7B7F: 19         ADD     HL,DE           
7B80: 7E         LD      A,(HL)          
7B81: E0 9D      LDFF00  ($9D),A         
7B83: CD 40 7C   CALL    $7C40           
7B86: CD 61 7D   CALL    $7D61           
7B89: F0 E7      LD      A,($E7)         
7B8B: E6 03      AND     $03             
7B8D: 20 04      JR      NZ,$7B93        
7B8F: 3E 0B      LD      A,$0B           
7B91: E0 F4      LDFF00  ($F4),A         
7B93: F0 F0      LD      A,($F0)         
7B95: A7         AND     A               
7B96: 28 18      JR      Z,$7BB0         
7B98: 3E 30      LD      A,$30           
7B9A: CD 30 3C   CALL    $3C30           
7B9D: F0 D7      LD      A,($D7)         
7B9F: 2F         CPL                     
7BA0: 3C         INC     A               
7BA1: E0 9B      LDFF00  ($9B),A         
7BA3: F0 D8      LD      A,($D8)         
7BA5: 2F         CPL                     
7BA6: 3C         INC     A               
7BA7: E0 9A      LDFF00  ($9A),A         
7BA9: C5         PUSH    BC              
7BAA: CD D6 20   CALL    $20D6           
7BAD: C1         POP     BC              
7BAE: 18 0D      JR      $7BBD           
7BB0: CD CD 7D   CALL    $7DCD           
7BB3: CD 91 08   CALL    $0891           
7BB6: 20 13      JR      NZ,$7BCB        
7BB8: 3E 30      LD      A,$30           
7BBA: CD 25 3C   CALL    $3C25           
7BBD: CD D5 3B   CALL    $3BD5           
7BC0: 30 63      JR      NC,$7C25        
7BC2: AF         XOR     A               
7BC3: EA C6 C1   LD      ($C1C6),A       
7BC6: CD 76 7E   CALL    $7E76           
7BC9: 18 5A      JR      $7C25           
7BCB: 3E 06      LD      A,$06           
7BCD: EA 9E C1   LD      ($C19E),A       
7BD0: CD F6 3B   CALL    $3BF6           
7BD3: 21 A0 C2   LD      HL,$C2A0        
7BD6: 09         ADD     HL,BC           
7BD7: 7E         LD      A,(HL)          
7BD8: A7         AND     A               
7BD9: 20 4B      JR      NZ,$7C26        
7BDB: CD 9E 3B   CALL    $3B9E           
7BDE: FA A5 DB   LD      A,($DBA5)       
7BE1: A7         AND     A               
7BE2: 28 41      JR      Z,$7C25         
7BE4: CD 6E 64   CALL    $646E           
7BE7: 21 50 C2   LD      HL,$C250        
7BEA: 09         ADD     HL,BC           
7BEB: 7E         LD      A,(HL)          
7BEC: A7         AND     A               
7BED: 28 36      JR      Z,$7C25         
7BEF: 1E 9E      LD      E,$9E           
7BF1: CB 7F      SET     1,E             
7BF3: 20 02      JR      NZ,$7BF7        
7BF5: 1E 9F      LD      E,$9F           
7BF7: F0 AF      LD      A,($AF)         
7BF9: BB         CP      E               
7BFA: 20 29      JR      NZ,$7C25        
7BFC: 3E 68      LD      A,$68           
7BFE: CD 01 3C   CALL    $3C01           
7C01: 21 00 C2   LD      HL,$C200        
7C04: 19         ADD     HL,DE           
7C05: F0 CE      LD      A,($CE)         
7C07: C6 08      ADD     $08             
7C09: 77         LD      (HL),A          
7C0A: 21 10 C2   LD      HL,$C210        
7C0D: 19         ADD     HL,DE           
7C0E: F0 CD      LD      A,($CD)         
7C10: C6 10      ADD     $10             
7C12: 77         LD      (HL),A          
7C13: F0 AF      LD      A,($AF)         
7C15: FE 9E      CP      $9E             
7C17: 3E 00      LD      A,$00           
7C19: 28 01      JR      Z,$7C1C         
7C1B: 3C         INC     A               
7C1C: 21 80 C3   LD      HL,$C380        
7C1F: 19         ADD     HL,DE           
7C20: 77         LD      (HL),A          
7C21: CD 91 08   CALL    $0891           
7C24: 70         LD      (HL),B          
7C25: C9         RET                     
7C26: CD 91 08   CALL    $0891           
7C29: 70         LD      (HL),B          
7C2A: 3E 07      LD      A,$07           
7C2C: E0 F2      LDFF00  ($F2),A         
7C2E: F0 EE      LD      A,($EE)         
7C30: E0 D7      LDFF00  ($D7),A         
7C32: F0 EC      LD      A,($EC)         
7C34: E0 D8      LDFF00  ($D8),A         
7C36: 3E 05      LD      A,$05           
7C38: CD 53 09   CALL    $0953           
7C3B: C9         RET                     
7C3C: 36 00      LD      (HL),$00        
7C3E: 36 20      LD      (HL),$20        
7C40: 11 3C 7C   LD      DE,$7C3C        
7C43: CD 3B 3C   CALL    $3C3B           
7C46: F0 EE      LD      A,($EE)         
7C48: 21 98 FF   LD      HL,$FF98        
7C4B: 96         SUB     (HL)            
7C4C: CB 2F      SET     1,E             
7C4E: CB 2F      SET     1,E             
7C50: E0 D7      LDFF00  ($D7),A         
7C52: E0 D9      LDFF00  ($D9),A         
7C54: F0 EF      LD      A,($EF)         
7C56: 21 99 FF   LD      HL,$FF99        
7C59: 96         SUB     (HL)            
7C5A: CB 2F      SET     1,E             
7C5C: CB 2F      SET     1,E             
7C5E: E0 D8      LDFF00  ($D8),A         
7C60: E0 DA      LDFF00  ($DA),A         
7C62: FA C0 C3   LD      A,($C3C0)       
7C65: 5F         LD      E,A             
7C66: 16 00      LD      D,$00           
7C68: 21 30 C0   LD      HL,$C030        
7C6B: 19         ADD     HL,DE           
7C6C: E5         PUSH    HL              
7C6D: D1         POP     DE              
7C6E: 3E 03      LD      A,$03           
7C70: E0 DB      LDFF00  ($DB),A         
7C72: 21 E7 FF   LD      HL,$FFE7        
7C75: AE         XOR     (HL)            
7C76: E6 01      AND     $01             
7C78: 20 07      JR      NZ,$7C81        
7C7A: F0 99      LD      A,($99)         
7C7C: 21 D8 FF   LD      HL,$FFD8        
7C7F: 86         ADD     A,(HL)          
7C80: 12         LD      (DE),A          
7C81: 13         INC     DE              
7C82: F0 98      LD      A,($98)         
7C84: 21 D7 FF   LD      HL,$FFD7        
7C87: 86         ADD     A,(HL)          
7C88: C6 04      ADD     $04             
7C8A: 12         LD      (DE),A          
7C8B: 13         INC     DE              
7C8C: 3E 24      LD      A,$24           
7C8E: 12         LD      (DE),A          
7C8F: 13         INC     DE              
7C90: 3E 00      LD      A,$00           
7C92: 12         LD      (DE),A          
7C93: 13         INC     DE              
7C94: F0 D7      LD      A,($D7)         
7C96: 21 D9 FF   LD      HL,$FFD9        
7C99: 86         ADD     A,(HL)          
7C9A: E0 D7      LDFF00  ($D7),A         
7C9C: F0 D8      LD      A,($D8)         
7C9E: 21 DA FF   LD      HL,$FFDA        
7CA1: 86         ADD     A,(HL)          
7CA2: E0 D8      LDFF00  ($D8),A         
7CA4: F0 DB      LD      A,($DB)         
7CA6: 3D         DEC     A               
7CA7: 20 C7      JR      NZ,$7C70        
7CA9: 3E 03      LD      A,$03           
7CAB: CD D0 3D   CALL    $3DD0           
7CAE: C9         RET                     
7CAF: CD D5 3B   CALL    $3BD5           
7CB2: 30 1F      JR      NC,$7CD3        
7CB4: CD 4A 09   CALL    $094A           
7CB7: CD 42 09   CALL    $0942           
7CBA: FA A6 C1   LD      A,($C1A6)       
7CBD: A7         AND     A               
7CBE: 28 11      JR      Z,$7CD1         
7CC0: 5F         LD      E,A             
7CC1: 50         LD      D,B             
7CC2: 21 9F C3   LD      HL,$C39F        
7CC5: 19         ADD     HL,DE           
7CC6: 7E         LD      A,(HL)          
7CC7: FE 03      CP      $03             
7CC9: 20 06      JR      NZ,$7CD1        
7CCB: 21 8F C2   LD      HL,$C28F        
7CCE: 19         ADD     HL,DE           
7CCF: 36 00      LD      (HL),$00        
7CD1: 37         SCF                     
7CD2: C9         RET                     
7CD3: A7         AND     A               
7CD4: C9         RET                     
7CD5: 06 04      LD      B,$04           
7CD7: 02         LD      (BC),A          
7CD8: 00         NOP                     
7CD9: 21 80 C3   LD      HL,$C380        
7CDC: 09         ADD     HL,BC           
7CDD: 5E         LD      E,(HL)          
7CDE: 50         LD      D,B             
7CDF: 21 D5 7C   LD      HL,$7CD5        
7CE2: 19         ADD     HL,DE           
7CE3: E5         PUSH    HL              
7CE4: 21 D0 C3   LD      HL,$C3D0        
7CE7: 09         ADD     HL,BC           
7CE8: 34         INC     (HL)            
7CE9: 7E         LD      A,(HL)          
7CEA: 1F         RRA                     
7CEB: 1F         RRA                     
7CEC: 1F         RRA                     
7CED: 1F         RRA                     
7CEE: E1         POP     HL              
7CEF: E6 01      AND     $01             
7CF1: B6         OR      (HL)            
7CF2: C3 87 3B   JP      $3B87           
7CF5: 58         LD      E,B             
7CF6: F0 99      LD      A,($99)         
7CF8: 21 EF FF   LD      HL,$FFEF        
7CFB: 96         SUB     (HL)            
7CFC: C6 18      ADD     $18             
7CFE: FE 38      CP      $38             
7D00: 18 17      JR      $7D19           
7D02: F0 99      LD      A,($99)         
7D04: 21 EF FF   LD      HL,$FFEF        
7D07: 96         SUB     (HL)            
7D08: C6 14      ADD     $14             
7D0A: FE 38      CP      $38             
7D0C: 18 0B      JR      $7D19           
7D0E: 58         LD      E,B             
7D0F: F0 99      LD      A,($99)         
7D11: 21 EF FF   LD      HL,$FFEF        
7D14: 96         SUB     (HL)            
7D15: C6 14      ADD     $14             
7D17: FE 28      CP      $28             
7D19: 30 44      JR      NC,$7D5F        
7D1B: F0 98      LD      A,($98)         
7D1D: 21 EE FF   LD      HL,$FFEE        
7D20: 96         SUB     (HL)            
7D21: C6 10      ADD     $10             
7D23: FE 20      CP      $20             
7D25: 30 38      JR      NC,$7D5F        
7D27: 1C         INC     E               
7D28: F0 EB      LD      A,($EB)         
7D2A: FE C4      CP      $C4             
7D2C: 28 0C      JR      Z,$7D3A         
7D2E: D5         PUSH    DE              
7D2F: CD 4F 7E   CALL    $7E4F           
7D32: F0 9E      LD      A,($9E)         
7D34: EE 01      XOR     $01             
7D36: BB         CP      E               
7D37: D1         POP     DE              
7D38: 20 25      JR      NZ,$7D5F        
7D3A: 21 AD C1   LD      HL,$C1AD        
7D3D: 36 01      LD      (HL),$01        
7D3F: FA 9F C1   LD      A,($C19F)       
7D42: 21 4F C1   LD      HL,$C14F        
7D45: B6         OR      (HL)            
7D46: 21 46 C1   LD      HL,$C146        
7D49: B6         OR      (HL)            
7D4A: 21 34 C1   LD      HL,$C134        
7D4D: B6         OR      (HL)            
7D4E: 20 0F      JR      NZ,$7D5F        
7D50: FA 9A DB   LD      A,($DB9A)       
7D53: FE 80      CP      $80             
7D55: 20 08      JR      NZ,$7D5F        
7D57: F0 CC      LD      A,($CC)         
7D59: E6 10      AND     $10             
7D5B: 28 02      JR      Z,$7D5F         
7D5D: 37         SCF                     
7D5E: C9         RET                     
7D5F: A7         AND     A               
7D60: C9         RET                     
7D61: F0 EA      LD      A,($EA)         
7D63: FE 05      CP      $05             
7D65: 20 1A      JR      NZ,$7D81        
7D67: FA 95 DB   LD      A,($DB95)       
7D6A: FE 07      CP      $07             
7D6C: 28 13      JR      Z,$7D81         
7D6E: 21 A8 C1   LD      HL,$C1A8        
7D71: FA 9F C1   LD      A,($C19F)       
7D74: B6         OR      (HL)            
7D75: 21 4F C1   LD      HL,$C14F        
7D78: B6         OR      (HL)            
7D79: 20 06      JR      NZ,$7D81        
7D7B: FA 24 C1   LD      A,($C124)       
7D7E: A7         AND     A               
7D7F: 28 01      JR      Z,$7D82         
7D81: F1         POP     AF              
7D82: C9         RET                     
7D83: 21 10 C4   LD      HL,$C410        
7D86: 09         ADD     HL,BC           
7D87: 7E         LD      A,(HL)          
7D88: A7         AND     A               
7D89: 28 41      JR      Z,$7DCC         
7D8B: 3D         DEC     A               
7D8C: 77         LD      (HL),A          
7D8D: CD B8 3E   CALL    $3EB8           
7D90: 21 40 C2   LD      HL,$C240        
7D93: 09         ADD     HL,BC           
7D94: 7E         LD      A,(HL)          
7D95: F5         PUSH    AF              
7D96: 21 50 C2   LD      HL,$C250        
7D99: 09         ADD     HL,BC           
7D9A: 7E         LD      A,(HL)          
7D9B: F5         PUSH    AF              
7D9C: 21 F0 C3   LD      HL,$C3F0        
7D9F: 09         ADD     HL,BC           
7DA0: 7E         LD      A,(HL)          
7DA1: 21 40 C2   LD      HL,$C240        
7DA4: 09         ADD     HL,BC           
7DA5: 77         LD      (HL),A          
7DA6: 21 00 C4   LD      HL,$C400        
7DA9: 09         ADD     HL,BC           
7DAA: 7E         LD      A,(HL)          
7DAB: 21 50 C2   LD      HL,$C250        
7DAE: 09         ADD     HL,BC           
7DAF: 77         LD      (HL),A          
7DB0: CD CD 7D   CALL    $7DCD           
7DB3: 21 30 C4   LD      HL,$C430        
7DB6: 09         ADD     HL,BC           
7DB7: 7E         LD      A,(HL)          
7DB8: E6 20      AND     $20             
7DBA: 20 03      JR      NZ,$7DBF        
7DBC: CD 9E 3B   CALL    $3B9E           
7DBF: 21 50 C2   LD      HL,$C250        
7DC2: 09         ADD     HL,BC           
7DC3: F1         POP     AF              
7DC4: 77         LD      (HL),A          
7DC5: 21 40 C2   LD      HL,$C240        
7DC8: 09         ADD     HL,BC           
7DC9: F1         POP     AF              
7DCA: 77         LD      (HL),A          
7DCB: F1         POP     AF              
7DCC: C9         RET                     
7DCD: CD DA 7D   CALL    $7DDA           
7DD0: C5         PUSH    BC              
7DD1: 79         LD      A,C             
7DD2: C6 10      ADD     $10             
7DD4: 4F         LD      C,A             
7DD5: CD DA 7D   CALL    $7DDA           
7DD8: C1         POP     BC              
7DD9: C9         RET                     
7DDA: 21 40 C2   LD      HL,$C240        
7DDD: 09         ADD     HL,BC           
7DDE: 7E         LD      A,(HL)          
7DDF: A7         AND     A               
7DE0: 28 23      JR      Z,$7E05         
7DE2: F5         PUSH    AF              
7DE3: CB 37      SET     1,E             
7DE5: E6 F0      AND     $F0             
7DE7: 21 60 C2   LD      HL,$C260        
7DEA: 09         ADD     HL,BC           
7DEB: 86         ADD     A,(HL)          
7DEC: 77         LD      (HL),A          
7DED: CB 12      SET     1,E             
7DEF: 21 00 C2   LD      HL,$C200        
7DF2: 09         ADD     HL,BC           
7DF3: F1         POP     AF              
7DF4: 1E 00      LD      E,$00           
7DF6: CB 7F      SET     1,E             
7DF8: 28 02      JR      Z,$7DFC         
7DFA: 1E F0      LD      E,$F0           
7DFC: CB 37      SET     1,E             
7DFE: E6 0F      AND     $0F             
7E00: B3         OR      E               
7E01: CB 1A      SET     1,E             
7E03: 8E         ADC     A,(HL)          
7E04: 77         LD      (HL),A          
7E05: C9         RET                     
7E06: 21 20 C3   LD      HL,$C320        
7E09: 09         ADD     HL,BC           
7E0A: 7E         LD      A,(HL)          
7E0B: A7         AND     A               
7E0C: 28 F7      JR      Z,$7E05         
7E0E: F5         PUSH    AF              
7E0F: CB 37      SET     1,E             
7E11: E6 F0      AND     $F0             
7E13: 21 30 C3   LD      HL,$C330        
7E16: 09         ADD     HL,BC           
7E17: 86         ADD     A,(HL)          
7E18: 77         LD      (HL),A          
7E19: CB 12      SET     1,E             
7E1B: 21 10 C3   LD      HL,$C310        
7E1E: 18 D2      JR      $7DF2           
7E20: 1E 00      LD      E,$00           
7E22: F0 98      LD      A,($98)         
7E24: 21 00 C2   LD      HL,$C200        
7E27: 09         ADD     HL,BC           
7E28: 96         SUB     (HL)            
7E29: CB 7F      SET     1,E             
7E2B: 28 01      JR      Z,$7E2E         
7E2D: 1C         INC     E               
7E2E: 57         LD      D,A             
7E2F: C9         RET                     
7E30: 1E 02      LD      E,$02           
7E32: F0 99      LD      A,($99)         
7E34: 21 10 C2   LD      HL,$C210        
7E37: 09         ADD     HL,BC           
7E38: 96         SUB     (HL)            
7E39: CB 7F      SET     1,E             
7E3B: 20 01      JR      NZ,$7E3E        
7E3D: 1C         INC     E               
7E3E: 57         LD      D,A             
7E3F: C9         RET                     
7E40: 1E 02      LD      E,$02           
7E42: F0 99      LD      A,($99)         
7E44: 21 EC FF   LD      HL,$FFEC        
7E47: 96         SUB     (HL)            
7E48: CB 7F      SET     1,E             
7E4A: 20 01      JR      NZ,$7E4D        
7E4C: 1C         INC     E               
7E4D: 57         LD      D,A             
7E4E: C9         RET                     
7E4F: CD 20 7E   CALL    $7E20           
7E52: 7B         LD      A,E             
7E53: E0 D7      LDFF00  ($D7),A         
7E55: 7A         LD      A,D             
7E56: CB 7F      SET     1,E             
7E58: 28 02      JR      Z,$7E5C         
7E5A: 2F         CPL                     
7E5B: 3C         INC     A               
7E5C: F5         PUSH    AF              
7E5D: CD 30 7E   CALL    $7E30           
7E60: 7B         LD      A,E             
7E61: E0 D8      LDFF00  ($D8),A         
7E63: 7A         LD      A,D             
7E64: CB 7F      SET     1,E             
7E66: 28 02      JR      Z,$7E6A         
7E68: 2F         CPL                     
7E69: 3C         INC     A               
7E6A: D1         POP     DE              
7E6B: BA         CP      D               
7E6C: 30 04      JR      NC,$7E72        
7E6E: F0 D7      LD      A,($D7)         
7E70: 18 02      JR      $7E74           
7E72: F0 D8      LD      A,($D8)         
7E74: 5F         LD      E,A             
7E75: C9         RET                     
7E76: 21 80 C2   LD      HL,$C280        
7E79: 09         ADD     HL,BC           
7E7A: 70         LD      (HL),B          
7E7B: C9         RET                     
7E7C: 21 C0 C2   LD      HL,$C2C0        
7E7F: 09         ADD     HL,BC           
7E80: 7E         LD      A,(HL)          
7E81: C7         RST     0X00            
7E82: 88         ADC     A,B             
7E83: 7E         LD      A,(HL)          
7E84: 99         SBC     C               
7E85: 7E         LD      A,(HL)          
7E86: AA         XOR     D               
7E87: 7E         LD      A,(HL)          
7E88: CD 91 08   CALL    $0891           
7E8B: 36 A0      LD      (HL),$A0        
7E8D: 21 20 C4   LD      HL,$C420        
7E90: 09         ADD     HL,BC           
7E91: 36 FF      LD      (HL),$FF        
7E93: 21 C0 C2   LD      HL,$C2C0        
7E96: 09         ADD     HL,BC           
7E97: 34         INC     (HL)            
7E98: C9         RET                     
7E99: CD 91 08   CALL    $0891           
7E9C: 20 0B      JR      NZ,$7EA9        
7E9E: 36 C0      LD      (HL),$C0        
7EA0: 21 20 C4   LD      HL,$C420        
7EA3: 09         ADD     HL,BC           
7EA4: 36 FF      LD      (HL),$FF        
7EA6: CD 93 7E   CALL    $7E93           
7EA9: C9         RET                     
7EAA: CD 91 08   CALL    $0891           
7EAD: 20 0C      JR      NZ,$7EBB        
7EAF: CD D7 08   CALL    $08D7           
7EB2: CD BD 27   CALL    $27BD           
7EB5: CD 2B 7F   CALL    $7F2B           
7EB8: C3 7A 3F   JP      $3F7A           
7EBB: CD BF 7E   CALL    $7EBF           
7EBE: C9         RET                     
7EBF: E6 07      AND     $07             
7EC1: 20 1D      JR      NZ,$7EE0        
7EC3: CD ED 27   CALL    $27ED           
7EC6: E6 1F      AND     $1F             
7EC8: D6 10      SUB     $10             
7ECA: 5F         LD      E,A             
7ECB: 21 EE FF   LD      HL,$FFEE        
7ECE: 86         ADD     A,(HL)          
7ECF: 77         LD      (HL),A          
7ED0: CD ED 27   CALL    $27ED           
7ED3: E6 1F      AND     $1F             
7ED5: D6 14      SUB     $14             
7ED7: 5F         LD      E,A             
7ED8: 21 EC FF   LD      HL,$FFEC        
7EDB: 86         ADD     A,(HL)          
7EDC: 77         LD      (HL),A          
7EDD: CD E1 7E   CALL    $7EE1           
7EE0: C9         RET                     
7EE1: CD 67 7D   CALL    $7D67           
7EE4: F0 EE      LD      A,($EE)         
7EE6: E0 D7      LDFF00  ($D7),A         
7EE8: F0 EC      LD      A,($EC)         
7EEA: E0 D8      LDFF00  ($D8),A         
7EEC: 3E 02      LD      A,$02           
7EEE: CD 53 09   CALL    $0953           
7EF1: 3E 13      LD      A,$13           
7EF3: E0 F4      LDFF00  ($F4),A         
7EF5: C9         RET                     
7EF6: 3E 36      LD      A,$36           
7EF8: CD 01 3C   CALL    $3C01           
7EFB: F0 D7      LD      A,($D7)         
7EFD: 21 00 C2   LD      HL,$C200        
7F00: 19         ADD     HL,DE           
7F01: 77         LD      (HL),A          
7F02: F0 D8      LD      A,($D8)         
7F04: 21 10 C2   LD      HL,$C210        
7F07: 19         ADD     HL,DE           
7F08: 77         LD      (HL),A          
7F09: F0 F9      LD      A,($F9)         
7F0B: A7         AND     A               
7F0C: 28 08      JR      Z,$7F16         
7F0E: 21 50 C2   LD      HL,$C250        
7F11: 09         ADD     HL,BC           
7F12: 36 F0      LD      (HL),$F0        
7F14: 18 0C      JR      $7F22           
7F16: 21 20 C3   LD      HL,$C320        
7F19: 19         ADD     HL,DE           
7F1A: 36 10      LD      (HL),$10        
7F1C: 21 10 C3   LD      HL,$C310        
7F1F: 19         ADD     HL,DE           
7F20: 36 08      LD      (HL),$08        
7F22: CD 76 7E   CALL    $7E76           
7F25: 21 F4 FF   LD      HL,$FFF4        
7F28: 36 1A      LD      (HL),$1A        
7F2A: C9         RET                     
7F2B: 21 00 D8   LD      HL,$D800        
7F2E: F0 F6      LD      A,($F6)         
7F30: 5F         LD      E,A             
7F31: FA A5 DB   LD      A,($DBA5)       
7F34: 57         LD      D,A             
7F35: F0 F7      LD      A,($F7)         
7F37: FE 1A      CP      $1A             
7F39: 30 05      JR      NC,$7F40        
7F3B: FE 06      CP      $06             
7F3D: 38 01      JR      C,$7F40         
7F3F: 14         INC     D               
7F40: 19         ADD     HL,DE           
7F41: 7E         LD      A,(HL)          
7F42: F6 20      OR      $20             
7F44: 77         LD      (HL),A          
7F45: E0 F8      LDFF00  ($F8),A         
7F47: C9         RET                     
7F48: FF         RST     0X38            
7F49: FF         RST     0X38            
7F4A: FF         RST     0X38            
7F4B: FF         RST     0X38            
7F4C: FF         RST     0X38            
7F4D: FF         RST     0X38            
7F4E: FF         RST     0X38            
7F4F: FF         RST     0X38            
7F50: FF         RST     0X38            
7F51: FF         RST     0X38            
7F52: FF         RST     0X38            
7F53: FF         RST     0X38            
7F54: FF         RST     0X38            
7F55: FF         RST     0X38            
7F56: FF         RST     0X38            
7F57: FF         RST     0X38            
7F58: FF         RST     0X38            
7F59: FF         RST     0X38            
7F5A: FF         RST     0X38            
7F5B: FF         RST     0X38            
7F5C: FF         RST     0X38            
7F5D: FF         RST     0X38            
7F5E: FF         RST     0X38            
7F5F: FF         RST     0X38            
7F60: FF         RST     0X38            
7F61: FF         RST     0X38            
7F62: FF         RST     0X38            
7F63: FF         RST     0X38            
7F64: FF         RST     0X38            
7F65: FF         RST     0X38            
7F66: FF         RST     0X38            
7F67: FF         RST     0X38            
7F68: FF         RST     0X38            
7F69: FF         RST     0X38            
7F6A: FF         RST     0X38            
7F6B: FF         RST     0X38            
7F6C: FF         RST     0X38            
7F6D: FF         RST     0X38            
7F6E: FF         RST     0X38            
7F6F: FF         RST     0X38            
7F70: FF         RST     0X38            
7F71: FF         RST     0X38            
7F72: FF         RST     0X38            
7F73: FF         RST     0X38            
7F74: FF         RST     0X38            
7F75: FF         RST     0X38            
7F76: FF         RST     0X38            
7F77: FF         RST     0X38            
7F78: FF         RST     0X38            
7F79: FF         RST     0X38            
7F7A: FF         RST     0X38            
7F7B: FF         RST     0X38            
7F7C: FF         RST     0X38            
7F7D: FF         RST     0X38            
7F7E: FF         RST     0X38            
7F7F: FF         RST     0X38            
7F80: FF         RST     0X38            
7F81: FF         RST     0X38            
7F82: FF         RST     0X38            
7F83: FF         RST     0X38            
7F84: FF         RST     0X38            
7F85: FF         RST     0X38            
7F86: FF         RST     0X38            
7F87: FF         RST     0X38            
7F88: FF         RST     0X38            
7F89: FF         RST     0X38            
7F8A: FF         RST     0X38            
7F8B: FF         RST     0X38            
7F8C: FF         RST     0X38            
7F8D: FF         RST     0X38            
7F8E: FF         RST     0X38            
7F8F: FF         RST     0X38            
7F90: FF         RST     0X38            
7F91: FF         RST     0X38            
7F92: FF         RST     0X38            
7F93: FF         RST     0X38            
7F94: FF         RST     0X38            
7F95: FF         RST     0X38            
7F96: FF         RST     0X38            
7F97: FF         RST     0X38            
7F98: FF         RST     0X38            
7F99: FF         RST     0X38            
7F9A: FF         RST     0X38            
7F9B: FF         RST     0X38            
7F9C: FF         RST     0X38            
7F9D: FF         RST     0X38            
7F9E: FF         RST     0X38            
7F9F: FF         RST     0X38            
7FA0: FF         RST     0X38            
7FA1: FF         RST     0X38            
7FA2: FF         RST     0X38            
7FA3: FF         RST     0X38            
7FA4: FF         RST     0X38            
7FA5: FF         RST     0X38            
7FA6: FF         RST     0X38            
7FA7: FF         RST     0X38            
7FA8: FF         RST     0X38            
7FA9: FF         RST     0X38            
7FAA: FF         RST     0X38            
7FAB: FF         RST     0X38            
7FAC: FF         RST     0X38            
7FAD: FF         RST     0X38            
7FAE: FF         RST     0X38            
7FAF: FF         RST     0X38            
7FB0: FF         RST     0X38            
7FB1: FF         RST     0X38            
7FB2: FF         RST     0X38            
7FB3: FF         RST     0X38            
7FB4: FF         RST     0X38            
7FB5: FF         RST     0X38            
7FB6: FF         RST     0X38            
7FB7: FF         RST     0X38            
7FB8: FF         RST     0X38            
7FB9: FF         RST     0X38            
7FBA: FF         RST     0X38            
7FBB: FF         RST     0X38            
7FBC: FF         RST     0X38            
7FBD: FF         RST     0X38            
7FBE: FF         RST     0X38            
7FBF: FF         RST     0X38            
7FC0: FF         RST     0X38            
7FC1: FF         RST     0X38            
7FC2: FF         RST     0X38            
7FC3: FF         RST     0X38            
7FC4: FF         RST     0X38            
7FC5: FF         RST     0X38            
7FC6: FF         RST     0X38            
7FC7: FF         RST     0X38            
7FC8: FF         RST     0X38            
7FC9: FF         RST     0X38            
7FCA: FF         RST     0X38            
7FCB: FF         RST     0X38            
7FCC: FF         RST     0X38            
7FCD: FF         RST     0X38            
7FCE: FF         RST     0X38            
7FCF: FF         RST     0X38            
7FD0: FF         RST     0X38            
7FD1: FF         RST     0X38            
7FD2: FF         RST     0X38            
7FD3: FF         RST     0X38            
7FD4: FF         RST     0X38            
7FD5: FF         RST     0X38            
7FD6: FF         RST     0X38            
7FD7: FF         RST     0X38            
7FD8: FF         RST     0X38            
7FD9: FF         RST     0X38            
7FDA: FF         RST     0X38            
7FDB: FF         RST     0X38            
7FDC: FF         RST     0X38            
7FDD: FF         RST     0X38            
7FDE: FF         RST     0X38            
7FDF: FF         RST     0X38            
7FE0: FF         RST     0X38            
7FE1: FF         RST     0X38            
7FE2: FF         RST     0X38            
7FE3: FF         RST     0X38            
7FE4: FF         RST     0X38            
7FE5: FF         RST     0X38            
7FE6: FF         RST     0X38            
7FE7: FF         RST     0X38            
7FE8: FF         RST     0X38            
7FE9: FF         RST     0X38            
7FEA: FF         RST     0X38            
7FEB: FF         RST     0X38            
7FEC: FF         RST     0X38            
7FED: FF         RST     0X38            
7FEE: FF         RST     0X38            
7FEF: FF         RST     0X38            
7FF0: FF         RST     0X38            
7FF1: FF         RST     0X38            
7FF2: FF         RST     0X38            
7FF3: FF         RST     0X38            
7FF4: FF         RST     0X38            
7FF5: FF         RST     0X38            
7FF6: FF         RST     0X38            
7FF7: FF         RST     0X38            
7FF8: FF         RST     0X38            
7FF9: FF         RST     0X38            
7FFA: FF         RST     0X38            
7FFB: FF         RST     0X38            
7FFC: FF         RST     0X38            
7FFD: FF         RST     0X38            
7FFE: FF         RST     0X38            
7FFF: FF         RST     0X38            
```
