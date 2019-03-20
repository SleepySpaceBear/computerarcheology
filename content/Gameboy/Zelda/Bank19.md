![Bank 19](GBZelda.jpg)

# Bank 19

>>> cpu Z80GB

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

```code
4000: F0 00      LD      A,($00)         
4002: 48         LD      C,B             
4003: 00         NOP                     
4004: F0 08      LD      A,($08)         
4006: 48         LD      C,B             
4007: 20 00      JR      NZ,$4009        
4009: 00         NOP                     
400A: 4A         LD      C,D             
400B: 00         NOP                     
400C: 00         NOP                     
400D: 08 4A 20   LD      ($204A),SP      
4010: F0 00      LD      A,($00)         
4012: 78         LD      A,B             
4013: 00         NOP                     
4014: F0 08      LD      A,($08)         
4016: 78         LD      A,B             
4017: 20 00      JR      NZ,$4019        
4019: 00         NOP                     
401A: 7A         LD      A,D             
401B: 00         NOP                     
401C: 00         NOP                     
401D: 08 7A 20   LD      ($207A),SP      
4020: 16 00      LD      D,$00           
4022: 21 B0 C2   LD      HL,$C2B0        
4025: 09         ADD     HL,BC           
4026: 7E         LD      A,(HL)          
4027: A7         AND     A               
4028: 28 20      JR      Z,$404A         
402A: 11 20 40   LD      DE,$4020        
402D: CD D0 3C   CALL    $3CD0           
4030: CD 9B 78   CALL    $789B           
4033: CD 07 79   CALL    $7907           
4036: CD 40 79   CALL    $7940           
4039: 21 20 C3   LD      HL,$C320        
403C: 09         ADD     HL,BC           
403D: 35         DEC     (HL)            
403E: 35         DEC     (HL)            
403F: 21 10 C3   LD      HL,$C310        
4042: 09         ADD     HL,BC           
4043: 7E         LD      A,(HL)          
4044: E6 80      AND     $80             
4046: C2 B0 79   JP      NZ,$79B0        
4049: C9         RET                     
404A: 21 00 40   LD      HL,$4000        
404D: F0 F7      LD      A,($F7)         
404F: FE 01      CP      $01             
4051: 20 03      JR      NZ,$4056        
4053: 21 10 40   LD      HL,$4010        
4056: 0E 04      LD      C,$04           
4058: CD 26 3D   CALL    $3D26           
405B: CD 19 3D   CALL    $3D19           
405E: CD 9B 78   CALL    $789B           
4061: CD E2 08   CALL    $08E2           
4064: CD EB 3B   CALL    $3BEB           
4067: F0 F0      LD      A,($F0)         
4069: C7         RST     0X00            
406A: 70         LD      (HL),B          
406B: 40         LD      B,B             
406C: 23         INC     HL              
406D: 41         LD      B,C             
406E: 23         INC     HL              
406F: 41         LD      B,C             
4070: CD 9E 3B   CALL    $3B9E           
4073: CD 00 78   CALL    $7800           
4076: CD 5A 79   CALL    $795A           
4079: C6 10      ADD     $10             
407B: FE 20      CP      $20             
407D: D2 1C 41   JP      NC,$411C        
4080: CD 6A 79   CALL    $796A           
4083: C6 20      ADD     $20             
4085: FE 30      CP      $30             
4087: D2 1C 41   JP      NC,$411C        
408A: FA 9B C1   LD      A,($C19B)       
408D: A7         AND     A               
408E: C2 1C 41   JP      NZ,$411C        
4091: FA 00 DB   LD      A,($DB00)       
4094: FE 03      CP      $03             
4096: 20 08      JR      NZ,$40A0        
4098: F0 CB      LD      A,($CB)         
409A: E6 20      AND     $20             
409C: 20 0F      JR      NZ,$40AD        
409E: 18 7C      JR      $411C           
40A0: FA 01 DB   LD      A,($DB01)       
40A3: FE 03      CP      $03             
40A5: 20 75      JR      NZ,$411C        
40A7: F0 CB      LD      A,($CB)         
40A9: E6 10      AND     $10             
40AB: 28 6F      JR      Z,$411C         
40AD: FA CF C3   LD      A,($C3CF)       
40B0: A7         AND     A               
40B1: 20 69      JR      NZ,$411C        
40B3: 3E 01      LD      A,$01           
40B5: E0 A1      LDFF00  ($A1),A         
40B7: EA CF C3   LD      ($C3CF),A       
40BA: F0 9E      LD      A,($9E)         
40BC: 5F         LD      E,A             
40BD: 16 00      LD      D,$00           
40BF: 21 63 1E   LD      HL,$1E63        
40C2: 19         ADD     HL,DE           
40C3: 7E         LD      A,(HL)          
40C4: E0 9D      LDFF00  ($9D),A         
40C6: 21 67 1E   LD      HL,$1E67        
40C9: 19         ADD     HL,DE           
40CA: F0 CB      LD      A,($CB)         
40CC: A6         AND     (HL)            
40CD: 28 4D      JR      Z,$411C         
40CF: 21 6B 1E   LD      HL,$1E6B        
40D2: 19         ADD     HL,DE           
40D3: 7E         LD      A,(HL)          
40D4: EA 3C C1   LD      ($C13C),A       
40D7: 21 6F 1E   LD      HL,$1E6F        
40DA: 19         ADD     HL,DE           
40DB: 7E         LD      A,(HL)          
40DC: EA 3B C1   LD      ($C13B),A       
40DF: 21 9D FF   LD      HL,$FF9D        
40E2: 34         INC     (HL)            
40E3: FA 43 DB   LD      A,($DB43)       
40E6: FE 02      CP      $02             
40E8: 20 32      JR      NZ,$411C        
40EA: 1E 08      LD      E,$08           
40EC: FA 7C D4   LD      A,($D47C)       
40EF: A7         AND     A               
40F0: 28 02      JR      Z,$40F4         
40F2: 1E 03      LD      E,$03           
40F4: 21 D0 C3   LD      HL,$C3D0        
40F7: 09         ADD     HL,BC           
40F8: 34         INC     (HL)            
40F9: 7E         LD      A,(HL)          
40FA: BB         CP      E               
40FB: 38 25      JR      C,$4122         
40FD: CD 8D 3B   CALL    $3B8D           
4100: 36 02      LD      (HL),$02        
4102: 21 80 C2   LD      HL,$C280        
4105: 09         ADD     HL,BC           
4106: 36 07      LD      (HL),$07        
4108: 21 90 C4   LD      HL,$C490        
410B: 09         ADD     HL,BC           
410C: 70         LD      (HL),B          
410D: F0 9E      LD      A,($9E)         
410F: EA 5D C1   LD      ($C15D),A       
4112: CD 91 08   CALL    $0891           
4115: 36 02      LD      (HL),$02        
4117: 21 F3 FF   LD      HL,$FFF3        
411A: 36 02      LD      (HL),$02        
411C: 21 D0 C3   LD      HL,$C3D0        
411F: 09         ADD     HL,BC           
4120: 70         LD      (HL),B          
4121: C9         RET                     
4122: C9         RET                     
4123: CD 07 79   CALL    $7907           
4126: CD 40 79   CALL    $7940           
4129: CD 9E 3B   CALL    $3B9E           
412C: 21 20 C3   LD      HL,$C320        
412F: 09         ADD     HL,BC           
4130: 35         DEC     (HL)            
4131: 35         DEC     (HL)            
4132: 21 A0 C2   LD      HL,$C2A0        
4135: 09         ADD     HL,BC           
4136: 7E         LD      A,(HL)          
4137: E6 0F      AND     $0F             
4139: 20 09      JR      NZ,$4144        
413B: 21 10 C3   LD      HL,$C310        
413E: 09         ADD     HL,BC           
413F: 7E         LD      A,(HL)          
4140: E6 80      AND     $80             
4142: 28 25      JR      Z,$4169         
4144: CD 88 41   CALL    $4188           
4147: FA 8E C1   LD      A,($C18E)       
414A: E6 1F      AND     $1F             
414C: FE 0B      CP      $0B             
414E: 20 19      JR      NZ,$4169        
4150: FA 0D C5   LD      A,($C50D)       
4153: FE 35      CP      $35             
4155: 38 04      JR      C,$415B         
4157: FE 3D      CP      $3D             
4159: 38 0B      JR      C,$4166         
415B: FA 03 C5   LD      A,($C503)       
415E: FE 35      CP      $35             
4160: 38 07      JR      C,$4169         
4162: FE 3D      CP      $3D             
4164: 30 03      JR      NC,$4169        
4166: CD EC 08   CALL    $08EC           
4169: C9         RET                     
416A: 00         NOP                     
416B: 08 00 08   LD      ($0800),SP      
416E: 00         NOP                     
416F: 08 F8 F8   LD      ($F8F8),SP      
4172: 00         NOP                     
4173: 00         NOP                     
4174: 08 08 FC   LD      ($FC08),SP      
4177: 05         DEC     B               
4178: FA 06 FB   LD      A,($FB06)       
417B: 04         INC     B               
417C: FC                              
417D: F8 FE      LDHL    SP,$FE          
417F: FF         RST     0X38            
4180: 03         INC     BC              
4181: 02         LD      (BC),A          
4182: 18 14      JR      $4198           
4184: 13         INC     DE              
4185: 16 12      LD      D,$12           
4187: 14         INC     D               
4188: 3E 00      LD      A,$00           
418A: E0 E8      LDFF00  ($E8),A         
418C: 3E 9D      LD      A,$9D           
418E: CD 01 3C   CALL    $3C01           
4191: 38 54      JR      C,$41E7         
4193: 21 B0 C2   LD      HL,$C2B0        
4196: 19         ADD     HL,DE           
4197: 34         INC     (HL)            
4198: 21 40 C3   LD      HL,$C340        
419B: 19         ADD     HL,DE           
419C: 36 C1      LD      (HL),$C1        
419E: C5         PUSH    BC              
419F: F0 E8      LD      A,($E8)         
41A1: 4F         LD      C,A             
41A2: 21 6A 41   LD      HL,$416A        
41A5: 09         ADD     HL,BC           
41A6: F0 D7      LD      A,($D7)         
41A8: 86         ADD     A,(HL)          
41A9: 21 00 C2   LD      HL,$C200        
41AC: 19         ADD     HL,DE           
41AD: 77         LD      (HL),A          
41AE: 21 70 41   LD      HL,$4170        
41B1: 09         ADD     HL,BC           
41B2: F0 D8      LD      A,($D8)         
41B4: 86         ADD     A,(HL)          
41B5: 21 10 C2   LD      HL,$C210        
41B8: 19         ADD     HL,DE           
41B9: 77         LD      (HL),A          
41BA: F0 DA      LD      A,($DA)         
41BC: 21 10 C3   LD      HL,$C310        
41BF: 19         ADD     HL,DE           
41C0: 77         LD      (HL),A          
41C1: 21 76 41   LD      HL,$4176        
41C4: 09         ADD     HL,BC           
41C5: 7E         LD      A,(HL)          
41C6: 21 40 C2   LD      HL,$C240        
41C9: 19         ADD     HL,DE           
41CA: 77         LD      (HL),A          
41CB: 21 7C 41   LD      HL,$417C        
41CE: 09         ADD     HL,BC           
41CF: 7E         LD      A,(HL)          
41D0: 21 50 C2   LD      HL,$C250        
41D3: 19         ADD     HL,DE           
41D4: 77         LD      (HL),A          
41D5: 21 82 41   LD      HL,$4182        
41D8: 09         ADD     HL,BC           
41D9: 7E         LD      A,(HL)          
41DA: 21 20 C3   LD      HL,$C320        
41DD: 19         ADD     HL,DE           
41DE: 77         LD      (HL),A          
41DF: C1         POP     BC              
41E0: F0 E8      LD      A,($E8)         
41E2: 3C         INC     A               
41E3: FE 06      CP      $06             
41E5: 20 A3      JR      NZ,$418A        
41E7: 3E 29      LD      A,$29           
41E9: E0 F4      LDFF00  ($F4),A         
41EB: F0 EE      LD      A,($EE)         
41ED: E0 D7      LDFF00  ($D7),A         
41EF: F0 EC      LD      A,($EC)         
41F1: E0 D8      LDFF00  ($D8),A         
41F3: 3E 02      LD      A,$02           
41F5: CD 53 09   CALL    $0953           
41F8: F0 EC      LD      A,($EC)         
41FA: D6 10      SUB     $10             
41FC: E0 D8      LDFF00  ($D8),A         
41FE: 3E 02      LD      A,$02           
4200: CD 53 09   CALL    $0953           
4203: C3 B0 79   JP      $79B0           
4206: 17         RLA                     
4207: 11 36 28   LD      DE,$2836        
420A: 45         LD      B,L             
420B: 52         LD      D,D             
420C: 7A         LD      A,D             
420D: 64         LD      H,H             
420E: 93         SUB     E               
420F: A1         AND     C               
4210: C5         PUSH    BC              
4211: D4 28 0E   CALL    NC,$0E28        
4214: 3F         CCF                     
4215: 5D         LD      E,L             
4216: FA A5 DB   LD      A,($DBA5)       
4219: A7         AND     A               
421A: 20 5A      JR      NZ,$4276        
421C: F0 F6      LD      A,($F6)         
421E: FE CE      CP      $CE             
4220: C2 05 44   JP      NZ,$4405        
4223: CD 9B 78   CALL    $789B           
4226: FA 46 C1   LD      A,($C146)       
4229: A7         AND     A               
422A: C0         RET     NZ              
422B: F0 98      LD      A,($98)         
422D: D6 50      SUB     $50             
422F: C6 03      ADD     $03             
4231: FE 06      CP      $06             
4233: D0         RET     NC              
4234: F0 99      LD      A,($99)         
4236: D6 46      SUB     $46             
4238: C6 04      ADD     $04             
423A: FE 08      CP      $08             
423C: D0         RET     NC              
423D: 3E 01      LD      A,$01           
423F: EA 01 D4   LD      ($D401),A       
4242: 3E 1F      LD      A,$1F           
4244: EA 02 D4   LD      ($D402),A       
4247: 3E F8      LD      A,$F8           
4249: EA 03 D4   LD      ($D403),A       
424C: 3E 50      LD      A,$50           
424E: EA 04 D4   LD      ($D404),A       
4251: E0 98      LDFF00  ($98),A         
4253: 3E 48      LD      A,$48           
4255: EA 05 D4   LD      ($D405),A       
4258: E0 99      LDFF00  ($99),A         
425A: 3E 45      LD      A,$45           
425C: EA 16 D4   LD      ($D416),A       
425F: 3E 06      LD      A,$06           
4261: EA 1C C1   LD      ($C11C),A       
4264: CD 3B 09   CALL    $093B           
4267: EA 98 C1   LD      ($C198),A       
426A: 3E 51      LD      A,$51           
426C: EA CB DB   LD      ($DBCB),A       
426F: 3E 0C      LD      A,$0C           
4271: E0 F3      LDFF00  ($F3),A         
4273: C3 B0 79   JP      $79B0           
4276: 3E 01      LD      A,$01           
4278: EA 9D C1   LD      ($C19D),A       
427B: F0 F7      LD      A,($F7)         
427D: 5F         LD      E,A             
427E: 50         LD      D,B             
427F: 21 65 DB   LD      HL,$DB65        
4282: 19         ADD     HL,DE           
4283: 7E         LD      A,(HL)          
4284: E6 01      AND     $01             
4286: CA DE 42   JP      Z,$42DE         
4289: CD A7 43   CALL    $43A7           
428C: F0 F0      LD      A,($F0)         
428E: C7         RST     0X00            
428F: 97         SUB     A               
4290: 42         LD      B,D             
4291: A0         AND     B               
4292: 42         LD      B,D             
4293: B6         OR      (HL)            
4294: 42         LD      B,D             
4295: F3         DI                      
4296: 42         LD      B,D             
4297: CD 8D 3B   CALL    $3B8D           
429A: 3E 1B      LD      A,$1B           
429C: EA 68 D3   LD      ($D368),A       
429F: C9         RET                     
42A0: CD 5A 79   CALL    $795A           
42A3: C6 04      ADD     $04             
42A5: FE 08      CP      $08             
42A7: 30 09      JR      NC,$42B2        
42A9: CD 6A 79   CALL    $796A           
42AC: C6 04      ADD     $04             
42AE: FE 08      CP      $08             
42B0: 38 03      JR      C,$42B5         
42B2: CD 8D 3B   CALL    $3B8D           
42B5: C9         RET                     
42B6: F0 A2      LD      A,($A2)         
42B8: A7         AND     A               
42B9: 20 23      JR      NZ,$42DE        
42BB: CD 5A 79   CALL    $795A           
42BE: C6 03      ADD     $03             
42C0: FE 06      CP      $06             
42C2: 30 1A      JR      NC,$42DE        
42C4: CD 6A 79   CALL    $796A           
42C7: C6 03      ADD     $03             
42C9: FE 06      CP      $06             
42CB: 30 11      JR      NC,$42DE        
42CD: CD 8D 3B   CALL    $3B8D           
42D0: 3E 20      LD      A,$20           
42D2: EA C6 C1   LD      ($C1C6),A       
42D5: CD 91 08   CALL    $0891           
42D8: 36 50      LD      (HL),$50        
42DA: 3E 1C      LD      A,$1C           
42DC: E0 F2      LDFF00  ($F2),A         
42DE: C9         RET                     
42DF: E4                              
42E0: E4                              
42E1: E4                              
42E2: E4                              
42E3: 94         SUB     H               
42E4: 94         SUB     H               
42E5: 94         SUB     H               
42E6: 94         SUB     H               
42E7: 54         LD      D,H             
42E8: 54         LD      D,H             
42E9: 54         LD      D,H             
42EA: 54         LD      D,H             
42EB: 00         NOP                     
42EC: 00         NOP                     
42ED: 00         NOP                     
42EE: 00         NOP                     
42EF: 00         NOP                     
42F0: 03         INC     BC              
42F1: 01 02 CD   LD      BC,$CD02        
42F4: 3B         DEC     SP              
42F5: 09         ADD     HL,BC           
42F6: EA 94 DB   LD      ($DB94),A       
42F9: EA C7 DB   LD      ($DBC7),A       
42FC: EA 3E C1   LD      ($C13E),A       
42FF: EA 37 C1   LD      ($C137),A       
4302: EA 6A C1   LD      ($C16A),A       
4305: EA 66 C1   LD      ($C166),A       
4308: EA A9 C1   LD      ($C1A9),A       
430B: 3C         INC     A               
430C: EA 67 C1   LD      ($C167),A       
430F: F0 EE      LD      A,($EE)         
4311: E0 98      LDFF00  ($98),A         
4313: F0 EC      LD      A,($EC)         
4315: E0 99      LDFF00  ($99),A         
4317: CD 91 08   CALL    $0891           
431A: 20 37      JR      NZ,$4353        
431C: 21 01 D4   LD      HL,$D401        
431F: 3E 01      LD      A,$01           
4321: 22         LD      (HLI),A         
4322: F0 F7      LD      A,($F7)         
4324: 22         LD      (HLI),A         
4325: 23         INC     HL              
4326: 3E 50      LD      A,$50           
4328: 22         LD      (HLI),A         
4329: E5         PUSH    HL              
432A: F0 F7      LD      A,($F7)         
432C: 5F         LD      E,A             
432D: CB 23      SET     1,E             
432F: 16 00      LD      D,$00           
4331: 21 06 42   LD      HL,$4206        
4334: 19         ADD     HL,DE           
4335: F0 F6      LD      A,($F6)         
4337: BE         CP      (HL)            
4338: 20 01      JR      NZ,$433B        
433A: 23         INC     HL              
433B: 7E         LD      A,(HL)          
433C: EA 03 D4   LD      ($D403),A       
433F: E1         POP     HL              
4340: FE 64      CP      $64             
4342: 3E 48      LD      A,$48           
4344: 20 02      JR      NZ,$4348        
4346: 3E 28      LD      A,$28           
4348: 77         LD      (HL),A          
4349: AF         XOR     A               
434A: EA 67 C1   LD      ($C167),A       
434D: CD B0 79   CALL    $79B0           
4350: C3 2A 09   JP      $092A           
4353: 21 A1 FF   LD      HL,$FFA1        
4356: 36 01      LD      (HL),$01        
4358: F5         PUSH    AF              
4359: F0 E7      LD      A,($E7)         
435B: 1F         RRA                     
435C: 1F         RRA                     
435D: 1F         RRA                     
435E: E6 03      AND     $03             
4360: 5F         LD      E,A             
4361: 50         LD      D,B             
4362: 21 EF 42   LD      HL,$42EF        
4365: 19         ADD     HL,DE           
4366: 7E         LD      A,(HL)          
4367: E0 9E      LDFF00  ($9E),A         
4369: C5         PUSH    BC              
436A: CD 7C 08   CALL    $087C           
436D: C1         POP     BC              
436E: 21 40 C4   LD      HL,$C440        
4371: 09         ADD     HL,BC           
4372: F1         POP     AF              
4373: FE 40      CP      $40             
4375: 30 0A      JR      NC,$4381        
4377: E6 03      AND     $03             
4379: 20 06      JR      NZ,$4381        
437B: 7E         LD      A,(HL)          
437C: FE 0C      CP      $0C             
437E: 28 01      JR      Z,$4381         
4380: 34         INC     (HL)            
4381: F0 E7      LD      A,($E7)         
4383: E6 03      AND     $03             
4385: 86         ADD     A,(HL)          
4386: 5F         LD      E,A             
4387: 50         LD      D,B             
4388: 21 DF 42   LD      HL,$42DF        
438B: 19         ADD     HL,DE           
438C: 7E         LD      A,(HL)          
438D: EA 97 DB   LD      ($DB97),A       
4390: C9         RET                     
4391: 1E 00      LD      E,$00           
4393: 1E 60      LD      E,$60           
4395: 1E 40      LD      E,$40           
4397: 1E 20      LD      E,$20           
4399: F8 FA      LDHL    SP,$FA          
439B: 00         NOP                     
439C: 06 08      LD      B,$08           
439E: 06 00      LD      B,$00           
43A0: FA F8 FA   LD      A,($FAF8)       
43A3: 24         INC     H               
43A4: 00         NOP                     
43A5: 24         INC     H               
43A6: 00         NOP                     
43A7: 21 40 C3   LD      HL,$C340        
43AA: 09         ADD     HL,BC           
43AB: 36 C2      LD      (HL),$C2        
43AD: F0 E7      LD      A,($E7)         
43AF: 1F         RRA                     
43B0: 1F         RRA                     
43B1: 1F         RRA                     
43B2: E6 01      AND     $01             
43B4: E0 F1      LDFF00  ($F1),A         
43B6: 11 91 43   LD      DE,$4391        
43B9: CD 3B 3C   CALL    $3C3B           
43BC: 21 40 C3   LD      HL,$C340        
43BF: 09         ADD     HL,BC           
43C0: 36 C1      LD      (HL),$C1        
43C2: AF         XOR     A               
43C3: E0 E8      LDFF00  ($E8),A         
43C5: 5F         LD      E,A             
43C6: CD D2 43   CALL    $43D2           
43C9: F0 E8      LD      A,($E8)         
43CB: C6 02      ADD     $02             
43CD: E6 07      AND     $07             
43CF: 20 F2      JR      NZ,$43C3        
43D1: C9         RET                     
43D2: F0 E7      LD      A,($E7)         
43D4: 1F         RRA                     
43D5: 1F         RRA                     
43D6: 1F         RRA                     
43D7: 00         NOP                     
43D8: 83         ADD     A,E             
43D9: E6 07      AND     $07             
43DB: 5F         LD      E,A             
43DC: 50         LD      D,B             
43DD: 21 9B 43   LD      HL,$439B        
43E0: 19         ADD     HL,DE           
43E1: F0 EE      LD      A,($EE)         
43E3: 86         ADD     A,(HL)          
43E4: E0 EE      LDFF00  ($EE),A         
43E6: 21 99 43   LD      HL,$4399        
43E9: 19         ADD     HL,DE           
43EA: F0 EC      LD      A,($EC)         
43EC: 86         ADD     A,(HL)          
43ED: E0 EC      LDFF00  ($EC),A         
43EF: 11 A3 43   LD      DE,$43A3        
43F2: CD D0 3C   CALL    $3CD0           
43F5: CD BA 3D   CALL    $3DBA           
43F8: C9         RET                     
43F9: FA FC 00   LD      A,($00FC)       
43FC: 04         INC     B               
43FD: 06 04      LD      B,$04           
43FF: 00         NOP                     
4400: FC                              
4401: FA FC 3E   LD      A,($3EFC)       
4404: 00         NOP                     
4405: 21 40 C3   LD      HL,$C340        
4408: 09         ADD     HL,BC           
4409: 36 C1      LD      (HL),$C1        
440B: F0 E7      LD      A,($E7)         
440D: 17         RLA                     
440E: 17         RLA                     
440F: E6 10      AND     $10             
4411: E0 ED      LDFF00  ($ED),A         
4413: F0 EE      LD      A,($EE)         
4415: E0 E5      LDFF00  ($E5),A         
4417: F0 EC      LD      A,($EC)         
4419: E0 E6      LDFF00  ($E6),A         
441B: AF         XOR     A               
441C: E0 E8      LDFF00  ($E8),A         
441E: 5F         LD      E,A             
441F: CD 2B 44   CALL    $442B           
4422: F0 E8      LD      A,($E8)         
4424: C6 02      ADD     $02             
4426: E6 07      AND     $07             
4428: 20 F2      JR      NZ,$441C        
442A: C9         RET                     
442B: F0 E7      LD      A,($E7)         
442D: 1F         RRA                     
442E: 1F         RRA                     
442F: 1F         RRA                     
4430: 00         NOP                     
4431: 83         ADD     A,E             
4432: E6 07      AND     $07             
4434: 5F         LD      E,A             
4435: 50         LD      D,B             
4436: 21 FB 43   LD      HL,$43FB        
4439: 19         ADD     HL,DE           
443A: F0 E5      LD      A,($E5)         
443C: 86         ADD     A,(HL)          
443D: E0 EE      LDFF00  ($EE),A         
443F: 21 F9 43   LD      HL,$43F9        
4442: 19         ADD     HL,DE           
4443: F0 E6      LD      A,($E6)         
4445: 86         ADD     A,(HL)          
4446: C6 04      ADD     $04             
4448: E0 EC      LDFF00  ($EC),A         
444A: 11 03 44   LD      DE,$4403        
444D: CD D0 3C   CALL    $3CD0           
4450: C9         RET                     
4451: 38 10      JR      C,$4463         
4453: 38 30      JR      C,$4485         
4455: A4         AND     H               
4456: 10 FF      STOP    $FF             
4458: FF         RST     0X38            
4459: 38 50      JR      C,$44AB         
445B: 38 70      JR      C,$44CD         
445D: FF         RST     0X38            
445E: FF         RST     0X38            
445F: A4         AND     H               
4460: 30 3E      JR      NC,$44A0        
4462: 01 EA 4D   LD      BC,$4DEA        
4465: C1         POP     BC              
4466: 11 51 44   LD      DE,$4451        
4469: CD 3B 3C   CALL    $3C3B           
446C: CD 9B 78   CALL    $789B           
446F: CD C5 29   CALL    $29C5           
4472: F0 E7      LD      A,($E7)         
4474: E6 03      AND     $03             
4476: 20 09      JR      NZ,$4481        
4478: 21 B0 C3   LD      HL,$C3B0        
447B: 09         ADD     HL,BC           
447C: 7E         LD      A,(HL)          
447D: 3C         INC     A               
447E: E6 03      AND     $03             
4480: 77         LD      (HL),A          
4481: 3E 08      LD      A,$08           
4483: EA 9E C1   LD      ($C19E),A       
4486: CD F6 3B   CALL    $3BF6           
4489: CD 07 79   CALL    $7907           
448C: CD A9 3B   CALL    $3BA9           
448F: CD CF 44   CALL    $44CF           
4492: F0 F0      LD      A,($F0)         
4494: C7         RST     0X00            
4495: 99         SBC     C               
4496: 44         LD      B,H             
4497: BB         CP      E               
4498: 44         LD      B,H             
4499: CD 91 08   CALL    $0891           
449C: 20 09      JR      NZ,$44A7        
449E: 3E 08      LD      A,$08           
44A0: CD 25 3C   CALL    $3C25           
44A3: CD 8D 3B   CALL    $3B8D           
44A6: C9         RET                     
44A7: 21 A0 C2   LD      HL,$C2A0        
44AA: 09         ADD     HL,BC           
44AB: 7E         LD      A,(HL)          
44AC: A7         AND     A               
44AD: 28 0B      JR      Z,$44BA         
44AF: CD 91 08   CALL    $0891           
44B2: 70         LD      (HL),B          
44B3: CD A6 45   CALL    $45A6           
44B6: 3E 07      LD      A,$07           
44B8: E0 F2      LDFF00  ($F2),A         
44BA: C9         RET                     
44BB: F0 E7      LD      A,($E7)         
44BD: E6 03      AND     $03             
44BF: 20 05      JR      NZ,$44C6        
44C1: 3E 20      LD      A,$20           
44C3: CD 25 3C   CALL    $3C25           
44C6: CD BF 3B   CALL    $3BBF           
44C9: 30 03      JR      NC,$44CE        
44CB: CD B0 79   CALL    $79B0           
44CE: C9         RET                     
44CF: FA A5 DB   LD      A,($DBA5)       
44D2: A7         AND     A               
44D3: C0         RET     NZ              
44D4: F0 AF      LD      A,($AF)         
44D6: FE D3      CP      $D3             
44D8: 28 03      JR      Z,$44DD         
44DA: FE 5C      CP      $5C             
44DC: C0         RET     NZ              
44DD: 21 A0 C2   LD      HL,$C2A0        
44E0: 09         ADD     HL,BC           
44E1: 70         LD      (HL),B          
44E2: F0 E9      LD      A,($E9)         
44E4: 5F         LD      E,A             
44E5: 50         LD      D,B             
44E6: CD A6 20   CALL    $20A6           
44E9: F0 CE      LD      A,($CE)         
44EB: C6 08      ADD     $08             
44ED: E0 D7      LDFF00  ($D7),A         
44EF: F0 CD      LD      A,($CD)         
44F1: C6 10      ADD     $10             
44F3: E0 D8      LDFF00  ($D8),A         
44F5: 3E 08      LD      A,$08           
44F7: CD 53 09   CALL    $0953           
44FA: 3E 13      LD      A,$13           
44FC: E0 F4      LDFF00  ($F4),A         
44FE: C9         RET                     
44FF: 00         NOP                     
4500: 00         NOP                     
4501: 08 20 00   LD      ($0020),SP      
4504: 08 06 20   LD      ($2006),SP      
4507: 00         NOP                     
4508: 00         NOP                     
4509: 06 00      LD      B,$00           
450B: 00         NOP                     
450C: 08 08 00   LD      ($0008),SP      
450F: 00         NOP                     
4510: 04         INC     B               
4511: 04         INC     B               
4512: 40         LD      B,B             
4513: FF         RST     0X38            
4514: FF         RST     0X38            
4515: FF         RST     0X38            
4516: FF         RST     0X38            
4517: 00         NOP                     
4518: 04         INC     B               
4519: 04         INC     B               
451A: 00         NOP                     
451B: FF         RST     0X38            
451C: FF         RST     0X38            
451D: FF         RST     0X38            
451E: FF         RST     0X38            
451F: 00         NOP                     
4520: 00         NOP                     
4521: FC                              
4522: 04         INC     B               
4523: 01 01 00   LD      BC,$0001        
4526: 00         NOP                     
4527: 21 4D C1   LD      HL,$C14D        
452A: 34         INC     (HL)            
452B: F0 F0      LD      A,($F0)         
452D: A7         AND     A               
452E: 20 35      JR      NZ,$4565        
4530: F0 9E      LD      A,($9E)         
4532: 5F         LD      E,A             
4533: 50         LD      D,B             
4534: 21 1F 45   LD      HL,$451F        
4537: 19         ADD     HL,DE           
4538: F0 98      LD      A,($98)         
453A: 86         ADD     A,(HL)          
453B: 21 00 C2   LD      HL,$C200        
453E: 09         ADD     HL,BC           
453F: 77         LD      (HL),A          
4540: 21 23 45   LD      HL,$4523        
4543: 19         ADD     HL,DE           
4544: F0 99      LD      A,($99)         
4546: 86         ADD     A,(HL)          
4547: 21 10 C2   LD      HL,$C210        
454A: 09         ADD     HL,BC           
454B: 77         LD      (HL),A          
454C: 21 40 C2   LD      HL,$C240        
454F: 09         ADD     HL,BC           
4550: CB 26      SET     1,E             
4552: 21 50 C2   LD      HL,$C250        
4555: 09         ADD     HL,BC           
4556: CB 26      SET     1,E             
4558: 21 20 C4   LD      HL,$C420        
455B: 09         ADD     HL,BC           
455C: 36 FF      LD      (HL),$FF        
455E: 3E 3B      LD      A,$3B           
4560: E0 F2      LDFF00  ($F2),A         
4562: C3 8D 3B   JP      $3B8D           
4565: CD B6 45   CALL    $45B6           
4568: CD 9B 78   CALL    $789B           
456B: 3E 01      LD      A,$01           
456D: EA 9E C1   LD      ($C19E),A       
4570: CD F6 3B   CALL    $3BF6           
4573: CD 07 79   CALL    $7907           
4576: CD A9 3B   CALL    $3BA9           
4579: 21 A0 C2   LD      HL,$C2A0        
457C: 09         ADD     HL,BC           
457D: 7E         LD      A,(HL)          
457E: A7         AND     A               
457F: 20 22      JR      NZ,$45A3        
4581: F0 E7      LD      A,($E7)         
4583: 3C         INC     A               
4584: E6 03      AND     $03             
4586: 20 1A      JR      NZ,$45A2        
4588: F0 EE      LD      A,($EE)         
458A: E0 D7      LDFF00  ($D7),A         
458C: F0 EC      LD      A,($EC)         
458E: E0 D8      LDFF00  ($D8),A         
4590: 3E 0D      LD      A,$0D           
4592: CD 53 09   CALL    $0953           
4595: 21 20 C5   LD      HL,$C520        
4598: 19         ADD     HL,DE           
4599: 36 08      LD      (HL),$08        
459B: F0 F1      LD      A,($F1)         
459D: 21 90 C5   LD      HL,$C590        
45A0: 19         ADD     HL,DE           
45A1: 77         LD      (HL),A          
45A2: C9         RET                     
45A3: CD B0 79   CALL    $79B0           
45A6: F0 EE      LD      A,($EE)         
45A8: E0 D7      LDFF00  ($D7),A         
45AA: F0 EC      LD      A,($EC)         
45AC: C6 03      ADD     $03             
45AE: E0 D8      LDFF00  ($D8),A         
45B0: 3E 05      LD      A,$05           
45B2: CD 53 09   CALL    $0953           
45B5: C9         RET                     
45B6: F0 F1      LD      A,($F1)         
45B8: 17         RLA                     
45B9: 17         RLA                     
45BA: 17         RLA                     
45BB: E6 F8      AND     $F8             
45BD: 5F         LD      E,A             
45BE: 50         LD      D,B             
45BF: 21 FF 44   LD      HL,$44FF        
45C2: 19         ADD     HL,DE           
45C3: 0E 02      LD      C,$02           
45C5: CD 26 3D   CALL    $3D26           
45C8: C9         RET                     
45C9: 60         LD      H,B             
45CA: 00         NOP                     
45CB: 62         LD      H,D             
45CC: 00         NOP                     
45CD: 62         LD      H,D             
45CE: 20 60      JR      NZ,$4630        
45D0: 20 64      JR      NZ,$4636        
45D2: 00         NOP                     
45D3: 66         LD      H,(HL)          
45D4: 00         NOP                     
45D5: 66         LD      H,(HL)          
45D6: 20 64      JR      NZ,$463C        
45D8: 20 68      JR      NZ,$4642        
45DA: 00         NOP                     
45DB: 6A         LD      L,D             
45DC: 00         NOP                     
45DD: 6C         LD      L,H             
45DE: 00         NOP                     
45DF: 6E         LD      L,(HL)          
45E0: 00         NOP                     
45E1: 6A         LD      L,D             
45E2: 20 68      JR      NZ,$464C        
45E4: 20 6E      JR      NZ,$4654        
45E6: 20 6C      JR      NZ,$4654        
45E8: 20 21      JR      NZ,$460B        
45EA: 40         LD      B,B             
45EB: C3 09 CB   JP      $CB09           
45EE: F6 CB      OR      $CB             
45F0: FE FA      CP      $FA             
45F2: 0E DB      LD      C,$DB           
45F4: FE 0E      CP      $0E             
45F6: C2 B0 79   JP      NZ,$79B0        
45F9: 21 00 C2   LD      HL,$C200        
45FC: 09         ADD     HL,BC           
45FD: 36 50      LD      (HL),$50        
45FF: 11 C9 45   LD      DE,$45C9        
4602: CD 3B 3C   CALL    $3C3B           
4605: CD 32 78   CALL    $7832           
4608: F0 E7      LD      A,($E7)         
460A: E6 3F      AND     $3F             
460C: 20 08      JR      NZ,$4616        
460E: CD 89 79   CALL    $7989           
4611: 21 80 C3   LD      HL,$C380        
4614: 09         ADD     HL,BC           
4615: 73         LD      (HL),E          
4616: CD 00 78   CALL    $7800           
4619: F0 F0      LD      A,($F0)         
461B: C7         RST     0X00            
461C: 24         INC     H               
461D: 46         LD      B,(HL)          
461E: 55         LD      D,L             
461F: 46         LD      B,(HL)          
4620: 05         DEC     B               
4621: 47         LD      B,A             
4622: A9         XOR     C               
4623: 46         LD      B,(HL)          
4624: CD 9B 78   CALL    $789B           
4627: 58         LD      E,B             
4628: F0 99      LD      A,($99)         
462A: 21 EF FF   LD      HL,$FFEF        
462D: 96         SUB     (HL)            
462E: C6 26      ADD     $26             
4630: FE 4C      CP      $4C             
4632: CD 59 78   CALL    $7859           
4635: D0         RET     NC              
4636: FA 7D DB   LD      A,($DB7D)       
4639: FE 00      CP      $00             
463B: 28 04      JR      Z,$4641         
463D: FE 0D      CP      $0D             
463F: 20 09      JR      NZ,$464A        
4641: 3E 21      LD      A,$21           
4643: CD 8E 21   CALL    $218E           
4646: CD 8D 3B   CALL    $3B8D           
4649: C9         RET                     
464A: 3E 25      LD      A,$25           
464C: CD 8E 21   CALL    $218E           
464F: CD 8D 3B   CALL    $3B8D           
4652: 36 03      LD      (HL),$03        
4654: C9         RET                     
4655: CD 9B 78   CALL    $789B           
4658: CD 8D 3B   CALL    $3B8D           
465B: FA 77 C1   LD      A,($C177)       
465E: A7         AND     A               
465F: 20 3A      JR      NZ,$469B        
4661: FA 00 DB   LD      A,($DB00)       
4664: A7         AND     A               
4665: 28 34      JR      Z,$469B         
4667: FE 01      CP      $01             
4669: 28 37      JR      Z,$46A2         
466B: FE 04      CP      $04             
466D: 28 33      JR      Z,$46A2         
466F: FE 03      CP      $03             
4671: 28 2F      JR      Z,$46A2         
4673: FE 02      CP      $02             
4675: 28 2B      JR      Z,$46A2         
4677: FE 09      CP      $09             
4679: 28 27      JR      Z,$46A2         
467B: FE 0C      CP      $0C             
467D: 28 23      JR      Z,$46A2         
467F: FE 05      CP      $05             
4681: 28 1F      JR      Z,$46A2         
4683: EA 7D DB   LD      ($DB7D),A       
4686: 3E 0D      LD      A,$0D           
4688: EA 00 DB   LD      ($DB00),A       
468B: 21 B0 C2   LD      HL,$C2B0        
468E: 09         ADD     HL,BC           
468F: 77         LD      (HL),A          
4690: CD 91 08   CALL    $0891           
4693: 36 80      LD      (HL),$80        
4695: 3E 10      LD      A,$10           
4697: EA 68 D3   LD      ($D368),A       
469A: C9         RET                     
469B: 70         LD      (HL),B          
469C: 3E 23      LD      A,$23           
469E: CD 8E 21   CALL    $218E           
46A1: C9         RET                     
46A2: 70         LD      (HL),B          
46A3: 3E 27      LD      A,$27           
46A5: CD 8E 21   CALL    $218E           
46A8: C9         RET                     
46A9: CD 9B 78   CALL    $789B           
46AC: CD 8D 3B   CALL    $3B8D           
46AF: 36 02      LD      (HL),$02        
46B1: FA 77 C1   LD      A,($C177)       
46B4: A7         AND     A               
46B5: 20 2B      JR      NZ,$46E2        
46B7: 21 00 DB   LD      HL,$DB00        
46BA: 11 00 00   LD      DE,$0000        
46BD: 7E         LD      A,(HL)          
46BE: FE 0D      CP      $0D             
46C0: 28 07      JR      Z,$46C9         
46C2: 23         INC     HL              
46C3: 1C         INC     E               
46C4: 7B         LD      A,E             
46C5: FE 0C      CP      $0C             
46C7: 20 F4      JR      NZ,$46BD        
46C9: FA 7D DB   LD      A,($DB7D)       
46CC: 77         LD      (HL),A          
46CD: 21 B0 C2   LD      HL,$C2B0        
46D0: 09         ADD     HL,BC           
46D1: 77         LD      (HL),A          
46D2: 3E 0D      LD      A,$0D           
46D4: EA 7D DB   LD      ($DB7D),A       
46D7: CD 91 08   CALL    $0891           
46DA: 36 80      LD      (HL),$80        
46DC: 3E 10      LD      A,$10           
46DE: EA 68 D3   LD      ($D368),A       
46E1: C9         RET                     
46E2: 70         LD      (HL),B          
46E3: 3E 23      LD      A,$23           
46E5: CD 8E 21   CALL    $218E           
46E8: C9         RET                     
46E9: 00         NOP                     
46EA: 10 84      STOP    $84             
46EC: 10 80      STOP    $80             
46EE: 10 82      STOP    $82             
46F0: 10 86      STOP    $86             
46F2: 10 88      STOP    $88             
46F4: 10 8A      STOP    $8A             
46F6: 10 8C      STOP    $8C             
46F8: 10 98      STOP    $98             
46FA: 10 90      STOP    $90             
46FC: 10 92      STOP    $92             
46FE: 10 96      STOP    $96             
4700: 10 8E      STOP    $8E             
4702: 10 A4      STOP    $A4             
4704: 10 CD      STOP    $CD             
4706: 91         SUB     C               
4707: 08 20 05   LD      ($0520),SP      
470A: CD 8D 3B   CALL    $3B8D           
470D: 70         LD      (HL),B          
470E: C9         RET                     
470F: FE 08      CP      $08             
4711: 20 11      JR      NZ,$4724        
4713: 35         DEC     (HL)            
4714: 21 B0 C2   LD      HL,$C2B0        
4717: 09         ADD     HL,BC           
4718: 7E         LD      A,(HL)          
4719: FE 0D      CP      $0D             
471B: 3E 24      LD      A,$24           
471D: 28 02      JR      Z,$4721         
471F: 3E 26      LD      A,$26           
4721: CD 8E 21   CALL    $218E           
4724: F0 98      LD      A,($98)         
4726: E0 EE      LDFF00  ($EE),A         
4728: F0 99      LD      A,($99)         
472A: D6 0C      SUB     $0C             
472C: E0 EC      LDFF00  ($EC),A         
472E: F0 A2      LD      A,($A2)         
4730: 21 10 C3   LD      HL,$C310        
4733: 09         ADD     HL,BC           
4734: 77         LD      (HL),A          
4735: 3E 6C      LD      A,$6C           
4737: E0 9D      LDFF00  ($9D),A         
4739: 3E 02      LD      A,$02           
473B: E0 A1      LDFF00  ($A1),A         
473D: CD 3B 09   CALL    $093B           
4740: 21 B0 C2   LD      HL,$C2B0        
4743: 09         ADD     HL,BC           
4744: 7E         LD      A,(HL)          
4745: E0 F1      LDFF00  ($F1),A         
4747: 11 E9 46   LD      DE,$46E9        
474A: CD D0 3C   CALL    $3CD0           
474D: CD BA 3D   CALL    $3DBA           
4750: C9         RET                     
4751: 6A         LD      L,D             
4752: 20 68      JR      NZ,$47BC        
4754: 20 6E      JR      NZ,$47C4        
4756: 20 6C      JR      NZ,$47C4        
4758: 20 68      JR      NZ,$47C2        
475A: 00         NOP                     
475B: 6A         LD      L,D             
475C: 00         NOP                     
475D: 6C         LD      L,H             
475E: 00         NOP                     
475F: 6E         LD      L,(HL)          
4760: 00         NOP                     
4761: 64         LD      H,H             
4762: 00         NOP                     
4763: 66         LD      H,(HL)          
4764: 00         NOP                     
4765: 66         LD      H,(HL)          
4766: 20 64      JR      NZ,$47CC        
4768: 20 60      JR      NZ,$47CA        
476A: 00         NOP                     
476B: 62         LD      H,D             
476C: 00         NOP                     
476D: 62         LD      H,D             
476E: 20 60      JR      NZ,$47D0        
4770: 20 00      JR      NZ,$4772        
4772: F4                              
4773: 0C         INC     C               
4774: 00         NOP                     
4775: 0C         INC     C               
4776: F4                              
4777: F0 F7      LD      A,($F7)         
4779: FE 1F      CP      $1F             
477B: CA E9 45   JP      Z,$45E9         
477E: 11 51 47   LD      DE,$4751        
4781: CD 3B 3C   CALL    $3C3B           
4784: CD 9B 78   CALL    $789B           
4787: CD BD 78   CALL    $78BD           
478A: 21 30 C4   LD      HL,$C430        
478D: 09         ADD     HL,BC           
478E: 36 48      LD      (HL),$48        
4790: CD 89 79   CALL    $7989           
4793: 21 80 C3   LD      HL,$C380        
4796: 09         ADD     HL,BC           
4797: 7E         LD      A,(HL)          
4798: EE 01      XOR     $01             
479A: BB         CP      E               
479B: 20 06      JR      NZ,$47A3        
479D: 21 30 C4   LD      HL,$C430        
47A0: 09         ADD     HL,BC           
47A1: 36 08      LD      (HL),$08        
47A3: CD B4 3B   CALL    $3BB4           
47A6: FA 33 C1   LD      A,($C133)       
47A9: A7         AND     A               
47AA: 20 49      JR      NZ,$47F5        
47AC: F0 CB      LD      A,($CB)         
47AE: E6 0F      AND     $0F             
47B0: 28 43      JR      Z,$47F5         
47B2: E6 03      AND     $03             
47B4: 5F         LD      E,A             
47B5: 50         LD      D,B             
47B6: 21 71 47   LD      HL,$4771        
47B9: 19         ADD     HL,DE           
47BA: 7E         LD      A,(HL)          
47BB: 21 40 C2   LD      HL,$C240        
47BE: 09         ADD     HL,BC           
47BF: 77         LD      (HL),A          
47C0: F0 CB      LD      A,($CB)         
47C2: 1F         RRA                     
47C3: 1F         RRA                     
47C4: E6 03      AND     $03             
47C6: 5F         LD      E,A             
47C7: 50         LD      D,B             
47C8: 21 74 47   LD      HL,$4774        
47CB: 19         ADD     HL,DE           
47CC: 7E         LD      A,(HL)          
47CD: 21 50 C2   LD      HL,$C250        
47D0: 09         ADD     HL,BC           
47D1: 77         LD      (HL),A          
47D2: CD 07 79   CALL    $7907           
47D5: CD 9E 3B   CALL    $3B9E           
47D8: F0 9E      LD      A,($9E)         
47DA: EE 01      XOR     $01             
47DC: 21 80 C3   LD      HL,$C380        
47DF: 09         ADD     HL,BC           
47E0: 77         LD      (HL),A          
47E1: 17         RLA                     
47E2: E6 06      AND     $06             
47E4: 5F         LD      E,A             
47E5: 21 D0 C3   LD      HL,$C3D0        
47E8: 09         ADD     HL,BC           
47E9: 34         INC     (HL)            
47EA: 7E         LD      A,(HL)          
47EB: 1F         RRA                     
47EC: 1F         RRA                     
47ED: 1F         RRA                     
47EE: 1F         RRA                     
47EF: E6 01      AND     $01             
47F1: B3         OR      E               
47F2: CD 87 3B   CALL    $3B87           
47F5: C9         RET                     
47F6: 02         LD      (BC),A          
47F7: 11 C0 30   LD      DE,$30C0        
47FA: 14         INC     D               
47FB: 02         LD      (BC),A          
47FC: 11 C1 50   LD      DE,$50C1        
47FF: 14         INC     D               
4800: 02         LD      (BC),A          
4801: 0F         RRCA                    
4802: F5         PUSH    AF              
4803: 94         SUB     H               
4804: 52         LD      D,D             
4805: CD 9B 78   CALL    $789B           
4808: CD 91 08   CALL    $0891           
480B: 28 1A      JR      Z,$4827         
480D: FE 01      CP      $01             
480F: 20 09      JR      NZ,$481A        
4811: FA 1C C1   LD      A,($C11C)       
4814: EA 63 D4   LD      ($D463),A       
4817: CD 4B 48   CALL    $484B           
481A: 3E 02      LD      A,$02           
481C: E0 A1      LDFF00  ($A1),A         
481E: EA 67 C1   LD      ($C167),A       
4821: 3E 04      LD      A,$04           
4823: EA 3B C1   LD      ($C13B),A       
4826: C9         RET                     
4827: FA 1C C1   LD      A,($C11C)       
482A: FE 01      CP      $01             
482C: 20 1C      JR      NZ,$484A        
482E: F0 9C      LD      A,($9C)         
4830: A7         AND     A               
4831: 28 17      JR      Z,$484A         
4833: CD 5A 79   CALL    $795A           
4836: C6 0C      ADD     $0C             
4838: FE 18      CP      $18             
483A: 30 0E      JR      NC,$484A        
483C: CD 6A 79   CALL    $796A           
483F: C6 0C      ADD     $0C             
4841: FE 18      CP      $18             
4843: 30 05      JR      NC,$484A        
4845: CD 91 08   CALL    $0891           
4848: 36 10      LD      (HL),$10        
484A: C9         RET                     
484B: 11 00 48   LD      DE,$4800        
484E: F0 F6      LD      A,($F6)         
4850: FE EA      CP      $EA             
4852: 28 0C      JR      Z,$4860         
4854: 11 F6 47   LD      DE,$47F6        
4857: F0 98      LD      A,($98)         
4859: FE 30      CP      $30             
485B: 38 03      JR      C,$4860         
485D: 11 FB 47   LD      DE,$47FB        
4860: 21 01 D4   LD      HL,$D401        
4863: C5         PUSH    BC              
4864: 0E 05      LD      C,$05           
4866: 1A         LD      A,(DE)          
4867: 13         INC     DE              
4868: 22         LD      (HLI),A         
4869: 0D         DEC     C               
486A: 20 FA      JR      NZ,$4866        
486C: C1         POP     BC              
486D: CD B0 79   CALL    $79B0           
4870: F0 98      LD      A,($98)         
4872: CB 37      SET     1,E             
4874: E6 0F      AND     $0F             
4876: 5F         LD      E,A             
4877: F0 99      LD      A,($99)         
4879: D6 08      SUB     $08             
487B: E6 F0      AND     $F0             
487D: B3         OR      E               
487E: EA 16 D4   LD      ($D416),A       
4881: C3 0F 09   JP      $090F           
4884: 58         LD      E,B             
4885: 00         NOP                     
4886: 5A         LD      E,D             
4887: 00         NOP                     
4888: 58         LD      E,B             
4889: 00         NOP                     
488A: 5C         LD      E,H             
488B: 00         NOP                     
488C: 5A         LD      E,D             
488D: 20 58      JR      NZ,$48E7        
488F: 20 5C      JR      NZ,$48ED        
4891: 20 58      JR      NZ,$48EB        
4893: 20 21      JR      NZ,$48B6        
4895: 60         LD      H,B             
4896: C3 09 36   JP      $3609           
4899: 4C         LD      C,H             
489A: 21 80 C3   LD      HL,$C380        
489D: 09         ADD     HL,BC           
489E: 7E         LD      A,(HL)          
489F: A7         AND     A               
48A0: 20 06      JR      NZ,$48A8        
48A2: F0 F1      LD      A,($F1)         
48A4: C6 02      ADD     $02             
48A6: E0 F1      LDFF00  ($F1),A         
48A8: 11 84 48   LD      DE,$4884        
48AB: CD 3B 3C   CALL    $3C3B           
48AE: CD 9B 78   CALL    $789B           
48B1: CD E2 08   CALL    $08E2           
48B4: CD 40 79   CALL    $7940           
48B7: 21 20 C3   LD      HL,$C320        
48BA: 09         ADD     HL,BC           
48BB: 35         DEC     (HL)            
48BC: 35         DEC     (HL)            
48BD: 21 10 C3   LD      HL,$C310        
48C0: 09         ADD     HL,BC           
48C1: 7E         LD      A,(HL)          
48C2: E6 80      AND     $80             
48C4: E0 E8      LDFF00  ($E8),A         
48C6: 28 06      JR      Z,$48CE         
48C8: 70         LD      (HL),B          
48C9: 21 20 C3   LD      HL,$C320        
48CC: 09         ADD     HL,BC           
48CD: 70         LD      (HL),B          
48CE: FA C8 C3   LD      A,($C3C8)       
48D1: A7         AND     A               
48D2: 28 2D      JR      Z,$4901         
48D4: 21 40 C3   LD      HL,$C340        
48D7: 09         ADD     HL,BC           
48D8: CB F6      SET     1,E             
48DA: FA 0F C5   LD      A,($C50F)       
48DD: 5F         LD      E,A             
48DE: 50         LD      D,B             
48DF: 21 00 C2   LD      HL,$C200        
48E2: 19         ADD     HL,DE           
48E3: F0 EE      LD      A,($EE)         
48E5: 1E 00      LD      E,$00           
48E7: BE         CP      (HL)            
48E8: 38 01      JR      C,$48EB         
48EA: 1C         INC     E               
48EB: 21 80 C3   LD      HL,$C380        
48EE: 09         ADD     HL,BC           
48EF: 73         LD      (HL),E          
48F0: F0 E7      LD      A,($E7)         
48F2: E6 3F      AND     $3F             
48F4: 20 06      JR      NZ,$48FC        
48F6: 21 20 C3   LD      HL,$C320        
48F9: 09         ADD     HL,BC           
48FA: 36 0C      LD      (HL),$0C        
48FC: CD B7 49   CALL    $49B7           
48FF: 18 03      JR      $4904           
4901: CD EB 3B   CALL    $3BEB           
4904: 21 20 C4   LD      HL,$C420        
4907: 09         ADD     HL,BC           
4908: 7E         LD      A,(HL)          
4909: A7         AND     A               
490A: 28 11      JR      Z,$491D         
490C: FE 08      CP      $08             
490E: 20 0D      JR      NZ,$491D        
4910: CD 8D 3B   CALL    $3B8D           
4913: 3E 02      LD      A,$02           
4915: 77         LD      (HL),A          
4916: E0 F0      LDFF00  ($F0),A         
4918: CD 91 08   CALL    $0891           
491B: 36 10      LD      (HL),$10        
491D: F0 F0      LD      A,($F0)         
491F: FE 02      CP      $02             
4921: 30 17      JR      NC,$493A        
4923: CD 4E 78   CALL    $784E           
4926: 30 12      JR      NC,$493A        
4928: FA C8 C3   LD      A,($C3C8)       
492B: A7         AND     A               
492C: 3E 20      LD      A,$20           
492E: 28 07      JR      Z,$4937         
4930: 3E 96      LD      A,$96           
4932: CD 85 21   CALL    $2185           
4935: 18 03      JR      $493A           
4937: CD 97 21   CALL    $2197           
493A: FA C8 C3   LD      A,($C3C8)       
493D: A7         AND     A               
493E: C0         RET     NZ              
493F: F0 F0      LD      A,($F0)         
4941: C7         RST     0X00            
4942: 52         LD      D,D             
4943: 49         LD      C,C             
4944: 95         SUB     L               
4945: 49         LD      C,C             
4946: C2 49 E8   JP      NZ,$E849        
4949: 49         LD      C,C             
494A: 02         LD      (BC),A          
494B: 08 0C 08   LD      ($080C),SP      
494E: FE F8      CP      $F8             
4950: F4                              
4951: F8 AF      LDHL    SP,$AF          
4953: CD 87 3B   CALL    $3B87           
4956: CD 91 08   CALL    $0891           
4959: 20 37      JR      NZ,$4992        
495B: CD ED 27   CALL    $27ED           
495E: E6 07      AND     $07             
4960: 5F         LD      E,A             
4961: 50         LD      D,B             
4962: 21 4A 49   LD      HL,$494A        
4965: 19         ADD     HL,DE           
4966: 7E         LD      A,(HL)          
4967: 21 40 C2   LD      HL,$C240        
496A: 09         ADD     HL,BC           
496B: 77         LD      (HL),A          
496C: 7B         LD      A,E             
496D: E6 04      AND     $04             
496F: 21 80 C3   LD      HL,$C380        
4972: 09         ADD     HL,BC           
4973: 77         LD      (HL),A          
4974: CD ED 27   CALL    $27ED           
4977: E6 07      AND     $07             
4979: 5F         LD      E,A             
497A: 21 4A 49   LD      HL,$494A        
497D: 19         ADD     HL,DE           
497E: 7E         LD      A,(HL)          
497F: 21 50 C2   LD      HL,$C250        
4982: 09         ADD     HL,BC           
4983: 77         LD      (HL),A          
4984: CD 91 08   CALL    $0891           
4987: CD ED 27   CALL    $27ED           
498A: E6 1F      AND     $1F             
498C: C6 30      ADD     $30             
498E: 77         LD      (HL),A          
498F: CD 8D 3B   CALL    $3B8D           
4992: C3 B7 49   JP      $49B7           
4995: CD 07 79   CALL    $7907           
4998: CD 9E 3B   CALL    $3B9E           
499B: F0 E8      LD      A,($E8)         
499D: A7         AND     A               
499E: 28 17      JR      Z,$49B7         
49A0: CD 91 08   CALL    $0891           
49A3: 20 07      JR      NZ,$49AC        
49A5: 36 30      LD      (HL),$30        
49A7: CD 8D 3B   CALL    $3B8D           
49AA: 70         LD      (HL),B          
49AB: C9         RET                     
49AC: 21 20 C3   LD      HL,$C320        
49AF: 09         ADD     HL,BC           
49B0: 36 08      LD      (HL),$08        
49B2: 21 10 C3   LD      HL,$C310        
49B5: 09         ADD     HL,BC           
49B6: 34         INC     (HL)            
49B7: F0 E7      LD      A,($E7)         
49B9: 1F         RRA                     
49BA: 1F         RRA                     
49BB: 1F         RRA                     
49BC: E6 01      AND     $01             
49BE: CD 87 3B   CALL    $3B87           
49C1: C9         RET                     
49C2: CD 91 08   CALL    $0891           
49C5: 20 17      JR      NZ,$49DE        
49C7: CD 8D 3B   CALL    $3B8D           
49CA: 3E 24      LD      A,$24           
49CC: CD 25 3C   CALL    $3C25           
49CF: 21 20 C3   LD      HL,$C320        
49D2: 09         ADD     HL,BC           
49D3: 36 18      LD      (HL),$18        
49D5: CD 5A 79   CALL    $795A           
49D8: 21 80 C3   LD      HL,$C380        
49DB: 09         ADD     HL,BC           
49DC: 7B         LD      A,E             
49DD: 77         LD      (HL),A          
49DE: F0 E7      LD      A,($E7)         
49E0: 1F         RRA                     
49E1: 1F         RRA                     
49E2: E6 01      AND     $01             
49E4: CD 87 3B   CALL    $3B87           
49E7: C9         RET                     
49E8: CD 07 79   CALL    $7907           
49EB: CD 9E 3B   CALL    $3B9E           
49EE: 21 40 C3   LD      HL,$C340        
49F1: 09         ADD     HL,BC           
49F2: 36 52      LD      (HL),$52        
49F4: CD BF 3B   CALL    $3BBF           
49F7: 21 40 C3   LD      HL,$C340        
49FA: 09         ADD     HL,BC           
49FB: 36 92      LD      (HL),$92        
49FD: F0 E8      LD      A,($E8)         
49FF: A7         AND     A               
4A00: 28 09      JR      Z,$4A0B         
4A02: CD 8D 3B   CALL    $3B8D           
4A05: 70         LD      (HL),B          
4A06: CD 91 08   CALL    $0891           
4A09: 36 20      LD      (HL),$20        
4A0B: C9         RET                     
4A0C: 60         LD      H,B             
4A0D: 78         LD      A,B             
4A0E: 78         LD      A,B             
4A0F: 60         LD      H,B             
4A10: 40         LD      B,B             
4A11: 28 28      JR      Z,$4A3B         
4A13: 40         LD      B,B             
4A14: 20 38      JR      NZ,$4A4E        
4A16: 58         LD      E,B             
4A17: 78         LD      A,B             
4A18: 78         LD      A,B             
4A19: 58         LD      E,B             
4A1A: 38 20      JR      C,$4A3C         
4A1C: 21 B0 C2   LD      HL,$C2B0        
4A1F: 09         ADD     HL,BC           
4A20: 7E         LD      A,(HL)          
4A21: A7         AND     A               
4A22: C2 22 4B   JP      NZ,$4B22        
4A25: 79         LD      A,C             
4A26: EA 61 D4   LD      ($D461),A       
4A29: F0 F8      LD      A,($F8)         
4A2B: E6 10      AND     $10             
4A2D: C2 B0 79   JP      NZ,$79B0        
4A30: F0 F0      LD      A,($F0)         
4A32: C7         RST     0X00            
4A33: 3D         DEC     A               
4A34: 4A         LD      C,D             
4A35: 5F         LD      E,A             
4A36: 4A         LD      C,D             
4A37: 6F         LD      L,A             
4A38: 4A         LD      C,D             
4A39: 93         SUB     E               
4A3A: 4A         LD      C,D             
4A3B: C3 4A FA   JP      $FA4A           
4A3E: 49         LD      C,C             
4A3F: DB                              
4A40: E6 04      AND     $04             
4A42: C8         RET     Z               
4A43: FA 4A DB   LD      A,($DB4A)       
4A46: FE 00      CP      $00             
4A48: C0         RET     NZ              
4A49: FA 66 C1   LD      A,($C166)       
4A4C: FE 01      CP      $01             
4A4E: C0         RET     NZ              
4A4F: CD D2 27   CALL    $27D2           
4A52: CD 91 08   CALL    $0891           
4A55: 36 30      LD      (HL),$30        
4A57: AF         XOR     A               
4A58: EA A3 C5   LD      ($C5A3),A       
4A5B: CD 8D 3B   CALL    $3B8D           
4A5E: C9         RET                     
4A5F: 3E 02      LD      A,$02           
4A61: E0 A1      LDFF00  ($A1),A         
4A63: EA 67 C1   LD      ($C167),A       
4A66: CD 91 08   CALL    $0891           
4A69: 20 03      JR      NZ,$4A6E        
4A6B: CD 8D 3B   CALL    $3B8D           
4A6E: C9         RET                     
4A6F: 3E 02      LD      A,$02           
4A71: E0 A1      LDFF00  ($A1),A         
4A73: CD 91 08   CALL    $0891           
4A76: C0         RET     NZ              
4A77: 21 D0 C3   LD      HL,$C3D0        
4A7A: 09         ADD     HL,BC           
4A7B: 7E         LD      A,(HL)          
4A7C: 34         INC     (HL)            
4A7D: FE 08      CP      $08             
4A7F: 20 09      JR      NZ,$4A8A        
4A81: 70         LD      (HL),B          
4A82: CD 91 08   CALL    $0891           
4A85: 36 40      LD      (HL),$40        
4A87: C3 8D 3B   JP      $3B8D           
4A8A: CD C4 4A   CALL    $4AC4           
4A8D: CD 91 08   CALL    $0891           
4A90: 36 20      LD      (HL),$20        
4A92: C9         RET                     
4A93: 3E 02      LD      A,$02           
4A95: E0 A1      LDFF00  ($A1),A         
4A97: CD 91 08   CALL    $0891           
4A9A: 20 26      JR      NZ,$4AC2        
4A9C: 1E 41      LD      E,$41           
4A9E: 21 67 DB   LD      HL,$DB67        
4AA1: 2A         LD      A,(HLI)         
4AA2: E6 02      AND     $02             
4AA4: 28 06      JR      Z,$4AAC         
4AA6: 1C         INC     E               
4AA7: 7B         LD      A,E             
4AA8: FE 47      CP      $47             
4AAA: 20 F5      JR      NZ,$4AA1        
4AAC: 7B         LD      A,E             
4AAD: EA 68 D3   LD      ($D368),A       
4AB0: EA 65 D4   LD      ($D465),A       
4AB3: 3E FF      LD      A,$FF           
4AB5: EA 66 C1   LD      ($C166),A       
4AB8: AF         XOR     A               
4AB9: EA 10 D2   LD      ($D210),A       
4ABC: EA 11 D2   LD      ($D211),A       
4ABF: CD 8D 3B   CALL    $3B8D           
4AC2: C9         RET                     
4AC3: C9         RET                     
4AC4: E0 E8      LDFF00  ($E8),A         
4AC6: 5F         LD      E,A             
4AC7: 50         LD      D,B             
4AC8: 21 65 DB   LD      HL,$DB65        
4ACB: 19         ADD     HL,DE           
4ACC: 7E         LD      A,(HL)          
4ACD: E6 02      AND     $02             
4ACF: 28 30      JR      Z,$4B01         
4AD1: 3E DE      LD      A,$DE           
4AD3: CD 01 3C   CALL    $3C01           
4AD6: D8         RET     C               
4AD7: 3E 2B      LD      A,$2B           
4AD9: E0 F4      LDFF00  ($F4),A         
4ADB: C5         PUSH    BC              
4ADC: F0 E8      LD      A,($E8)         
4ADE: 4F         LD      C,A             
4ADF: 21 0C 4A   LD      HL,$4A0C        
4AE2: 09         ADD     HL,BC           
4AE3: 7E         LD      A,(HL)          
4AE4: 21 00 C2   LD      HL,$C200        
4AE7: 19         ADD     HL,DE           
4AE8: C6 08      ADD     $08             
4AEA: 77         LD      (HL),A          
4AEB: 21 14 4A   LD      HL,$4A14        
4AEE: 09         ADD     HL,BC           
4AEF: 7E         LD      A,(HL)          
4AF0: 21 10 C2   LD      HL,$C210        
4AF3: 19         ADD     HL,DE           
4AF4: 77         LD      (HL),A          
4AF5: 79         LD      A,C             
4AF6: 21 B0 C3   LD      HL,$C3B0        
4AF9: 19         ADD     HL,DE           
4AFA: 77         LD      (HL),A          
4AFB: 21 B0 C2   LD      HL,$C2B0        
4AFE: 19         ADD     HL,DE           
4AFF: 34         INC     (HL)            
4B00: C1         POP     BC              
4B01: C9         RET                     
4B02: 50         LD      D,B             
4B03: 00         NOP                     
4B04: 52         LD      D,D             
4B05: 00         NOP                     
4B06: 54         LD      D,H             
4B07: 00         NOP                     
4B08: 56         LD      D,(HL)          
4B09: 00         NOP                     
4B0A: 58         LD      E,B             
4B0B: 00         NOP                     
4B0C: 5A         LD      E,D             
4B0D: 00         NOP                     
4B0E: 5C         LD      E,H             
4B0F: 00         NOP                     
4B10: 5E         LD      E,(HL)          
4B11: 00         NOP                     
4B12: 60         LD      H,B             
4B13: 00         NOP                     
4B14: 62         LD      H,D             
4B15: 00         NOP                     
4B16: 64         LD      H,H             
4B17: 00         NOP                     
4B18: 66         LD      H,(HL)          
4B19: 00         NOP                     
4B1A: 68         LD      L,B             
4B1B: 00         NOP                     
4B1C: 6A         LD      L,D             
4B1D: 00         NOP                     
4B1E: 6C         LD      L,H             
4B1F: 00         NOP                     
4B20: 6E         LD      L,(HL)          
4B21: 00         NOP                     
4B22: FE 02      CP      $02             
4B24: CA F8 4B   JP      Z,$4BF8         
4B27: F0 F0      LD      A,($F0)         
4B29: A7         AND     A               
4B2A: 20 45      JR      NZ,$4B71        
4B2C: FA A3 C5   LD      A,($C5A3)       
4B2F: FE 03      CP      $03             
4B31: 28 13      JR      Z,$4B46         
4B33: 21 F1 FF   LD      HL,$FFF1        
4B36: F0 E7      LD      A,($E7)         
4B38: 1F         RRA                     
4B39: 1F         RRA                     
4B3A: 1F         RRA                     
4B3B: AE         XOR     (HL)            
4B3C: E6 03      AND     $03             
4B3E: C8         RET     Z               
4B3F: 11 02 4B   LD      DE,$4B02        
4B42: CD 3B 3C   CALL    $3C3B           
4B45: C9         RET                     
4B46: F0 F1      LD      A,($F1)         
4B48: FE 07      CP      $07             
4B4A: C2 B0 79   JP      NZ,$79B0        
4B4D: 1E 08      LD      E,$08           
4B4F: 21 65 DB   LD      HL,$DB65        
4B52: 2A         LD      A,(HLI)         
4B53: E6 02      AND     $02             
4B55: 28 13      JR      Z,$4B6A         
4B57: 1D         DEC     E               
4B58: 20 F8      JR      NZ,$4B52        
4B5A: F0 F8      LD      A,($F8)         
4B5C: E6 10      AND     $10             
4B5E: C2 B0 79   JP      NZ,$79B0        
4B61: CD 91 08   CALL    $0891           
4B64: 36 A0      LD      (HL),$A0        
4B66: CD 8D 3B   CALL    $3B8D           
4B69: C9         RET                     
4B6A: AF         XOR     A               
4B6B: EA A3 C5   LD      ($C5A3),A       
4B6E: C3 B0 79   JP      $79B0           
4B71: 3E 02      LD      A,$02           
4B73: E0 A1      LDFF00  ($A1),A         
4B75: EA 67 C1   LD      ($C167),A       
4B78: CD 91 08   CALL    $0891           
4B7B: 20 66      JR      NZ,$4BE3        
4B7D: EA 55 C1   LD      ($C155),A       
4B80: EA A3 C5   LD      ($C5A3),A       
4B83: 3E C1      LD      A,$C1           
4B85: EA 36 D7   LD      ($D736),A       
4B88: 3E CB      LD      A,$CB           
4B8A: EA 46 D7   LD      ($D746),A       
4B8D: 3E 50      LD      A,$50           
4B8F: E0 CE      LDFF00  ($CE),A         
4B91: 3E 20      LD      A,$20           
4B93: E0 CD      LDFF00  ($CD),A         
4B95: CD 39 28   CALL    $2839           
4B98: 21 01 D6   LD      HL,$D601        
4B9B: FA 00 D6   LD      A,($D600)       
4B9E: 5F         LD      E,A             
4B9F: C6 07      ADD     $07             
4BA1: EA 00 D6   LD      ($D600),A       
4BA4: 16 00      LD      D,$00           
4BA6: 19         ADD     HL,DE           
4BA7: F0 CF      LD      A,($CF)         
4BA9: 22         LD      (HLI),A         
4BAA: F0 D0      LD      A,($D0)         
4BAC: 22         LD      (HLI),A         
4BAD: 3E 83      LD      A,$83           
4BAF: 22         LD      (HLI),A         
4BB0: 3E 7F      LD      A,$7F           
4BB2: 22         LD      (HLI),A         
4BB3: 3E 0F      LD      A,$0F           
4BB5: 22         LD      (HLI),A         
4BB6: 3E 7E      LD      A,$7E           
4BB8: 22         LD      (HLI),A         
4BB9: 3E 1F      LD      A,$1F           
4BBB: 22         LD      (HLI),A         
4BBC: F0 CF      LD      A,($CF)         
4BBE: 22         LD      (HLI),A         
4BBF: F0 D0      LD      A,($D0)         
4BC1: 3C         INC     A               
4BC2: 22         LD      (HLI),A         
4BC3: 3E 83      LD      A,$83           
4BC5: 22         LD      (HLI),A         
4BC6: 3E 7F      LD      A,$7F           
4BC8: 22         LD      (HLI),A         
4BC9: 3E 0F      LD      A,$0F           
4BCB: 22         LD      (HLI),A         
4BCC: 3E 7E      LD      A,$7E           
4BCE: 22         LD      (HLI),A         
4BCF: 3E 1F      LD      A,$1F           
4BD1: 22         LD      (HLI),A         
4BD2: 70         LD      (HL),B          
4BD3: CD D2 27   CALL    $27D2           
4BD6: 3E 23      LD      A,$23           
4BD8: E0 F2      LDFF00  ($F2),A         
4BDA: CD 3E 4C   CALL    $4C3E           
4BDD: CD D7 08   CALL    $08D7           
4BE0: C3 B0 79   JP      $79B0           
4BE3: 1E 01      LD      E,$01           
4BE5: E6 04      AND     $04             
4BE7: 28 02      JR      Z,$4BEB         
4BE9: 1E FF      LD      E,$FF           
4BEB: 7B         LD      A,E             
4BEC: EA 55 C1   LD      ($C155),A       
4BEF: C9         RET                     
4BF0: 16 00      LD      D,$00           
4BF2: 16 20      LD      D,$20           
4BF4: 16 60      LD      D,$60           
4BF6: 16 40      LD      D,$40           
4BF8: 11 F0 4B   LD      DE,$4BF0        
4BFB: CD D0 3C   CALL    $3CD0           
4BFE: CD 07 79   CALL    $7907           
4C01: 21 50 C2   LD      HL,$C250        
4C04: 09         ADD     HL,BC           
4C05: 34         INC     (HL)            
4C06: CD 91 08   CALL    $0891           
4C09: EA 67 C1   LD      ($C167),A       
4C0C: 28 05      JR      Z,$4C13         
4C0E: 3E 02      LD      A,$02           
4C10: E0 A1      LDFF00  ($A1),A         
4C12: C9         RET                     
4C13: 21 06 D8   LD      HL,$D806        
4C16: CB E6      SET     1,E             
4C18: 7E         LD      A,(HL)          
4C19: E0 F8      LDFF00  ($F8),A         
4C1B: C3 B0 79   JP      $79B0           
4C1E: 00         NOP                     
4C1F: 04         INC     B               
4C20: 08 00 08   LD      ($0800),SP      
4C23: 00         NOP                     
4C24: 04         INC     B               
4C25: 08 00 00   LD      ($0000),SP      
4C28: 00         NOP                     
4C29: 04         INC     B               
4C2A: 04         INC     B               
4C2B: 08 08 08   LD      ($0808),SP      
4C2E: F0 FC      LD      A,($FC)         
4C30: 10 F0      STOP    $F0             
4C32: 10 F0      STOP    $F0             
4C34: 04         INC     B               
4C35: 10 F0      STOP    $F0             
4C37: E8 F0      ADD     SP,$F0          
4C39: F8 F8      LDHL    SP,$F8          
4C3B: 08 0C 08   LD      ($080C),SP      
4C3E: AF         XOR     A               
4C3F: E0 E8      LDFF00  ($E8),A         
4C41: 3E DE      LD      A,$DE           
4C43: CD 01 3C   CALL    $3C01           
4C46: D8         RET     C               
4C47: 21 B0 C2   LD      HL,$C2B0        
4C4A: 19         ADD     HL,DE           
4C4B: 36 02      LD      (HL),$02        
4C4D: CD ED 27   CALL    $27ED           
4C50: E6 1F      AND     $1F             
4C52: C6 30      ADD     $30             
4C54: 21 E0 C2   LD      HL,$C2E0        
4C57: 19         ADD     HL,DE           
4C58: 77         LD      (HL),A          
4C59: C5         PUSH    BC              
4C5A: F0 E8      LD      A,($E8)         
4C5C: 4F         LD      C,A             
4C5D: 21 1E 4C   LD      HL,$4C1E        
4C60: 09         ADD     HL,BC           
4C61: 7E         LD      A,(HL)          
4C62: 21 00 C2   LD      HL,$C200        
4C65: 19         ADD     HL,DE           
4C66: C6 54      ADD     $54             
4C68: 77         LD      (HL),A          
4C69: 21 26 4C   LD      HL,$4C26        
4C6C: 09         ADD     HL,BC           
4C6D: 7E         LD      A,(HL)          
4C6E: 21 10 C2   LD      HL,$C210        
4C71: 19         ADD     HL,DE           
4C72: C6 3C      ADD     $3C             
4C74: 77         LD      (HL),A          
4C75: 21 2E 4C   LD      HL,$4C2E        
4C78: 09         ADD     HL,BC           
4C79: 7E         LD      A,(HL)          
4C7A: 21 40 C2   LD      HL,$C240        
4C7D: 19         ADD     HL,DE           
4C7E: 77         LD      (HL),A          
4C7F: 21 36 4C   LD      HL,$4C36        
4C82: 09         ADD     HL,BC           
4C83: 7E         LD      A,(HL)          
4C84: 21 50 C2   LD      HL,$C250        
4C87: 19         ADD     HL,DE           
4C88: D6 08      SUB     $08             
4C8A: 77         LD      (HL),A          
4C8B: C1         POP     BC              
4C8C: F0 E8      LD      A,($E8)         
4C8E: 3C         INC     A               
4C8F: FE 08      CP      $08             
4C91: 20 AC      JR      NZ,$4C3F        
4C93: C9         RET                     
4C94: 58         LD      E,B             
4C95: 00         NOP                     
4C96: 5A         LD      E,D             
4C97: 00         NOP                     
4C98: 5A         LD      E,D             
4C99: 20 F0      JR      NZ,$4C8B        
4C9B: F1         POP     AF              
4C9C: A7         AND     A               
4C9D: 28 08      JR      Z,$4CA7         
4C9F: 11 92 4C   LD      DE,$4C92        
4CA2: CD 3B 3C   CALL    $3C3B           
4CA5: 18 06      JR      $4CAD           
4CA7: 11 94 4C   LD      DE,$4C94        
4CAA: CD D0 3C   CALL    $3CD0           
4CAD: CD 9B 78   CALL    $789B           
4CB0: F0 F0      LD      A,($F0)         
4CB2: C7         RST     0X00            
4CB3: BF         CP      A               
4CB4: 4C         LD      C,H             
4CB5: 01 4D 02   LD      BC,$024D        
4CB8: 04         INC     B               
4CB9: 06 00      LD      B,$00           
4CBB: 0A         LD      A,(BC)          
4CBC: 08 0C 0D   LD      ($0D0C),SP      
4CBF: FA 95 DB   LD      A,($DB95)       
4CC2: FE 07      CP      $07             
4CC4: 28 04      JR      Z,$4CCA         
4CC6: AF         XOR     A               
4CC7: EA A2 C5   LD      ($C5A2),A       
4CCA: AF         XOR     A               
4CCB: CD 87 3B   CALL    $3B87           
4CCE: CD 4E 78   CALL    $784E           
4CD1: D0         RET     NC              
4CD2: 1E 00      LD      E,$00           
4CD4: F0 EE      LD      A,($EE)         
4CD6: FE 20      CP      $20             
4CD8: 38 0B      JR      C,$4CE5         
4CDA: 1C         INC     E               
4CDB: FE 40      CP      $40             
4CDD: 38 06      JR      C,$4CE5         
4CDF: 1C         INC     E               
4CE0: FE 70      CP      $70             
4CE2: 38 01      JR      C,$4CE5         
4CE4: 1C         INC     E               
4CE5: F0 EF      LD      A,($EF)         
4CE7: FE 40      CP      $40             
4CE9: 38 04      JR      C,$4CEF         
4CEB: 7B         LD      A,E             
4CEC: C6 04      ADD     $04             
4CEE: 5F         LD      E,A             
4CEF: 50         LD      D,B             
4CF0: 21 B7 4C   LD      HL,$4CB7        
4CF3: 19         ADD     HL,DE           
4CF4: 7E         LD      A,(HL)          
4CF5: 21 B0 C2   LD      HL,$C2B0        
4CF8: 09         ADD     HL,BC           
4CF9: 77         LD      (HL),A          
4CFA: CD 8E 21   CALL    $218E           
4CFD: CD 8D 3B   CALL    $3B8D           
4D00: C9         RET                     
4D01: 3E 01      LD      A,$01           
4D03: CD 87 3B   CALL    $3B87           
4D06: FA 9F C1   LD      A,($C19F)       
4D09: A7         AND     A               
4D0A: C0         RET     NZ              
4D0B: CD 8D 3B   CALL    $3B8D           
4D0E: 70         LD      (HL),B          
4D0F: FA 77 C1   LD      A,($C177)       
4D12: A7         AND     A               
4D13: 20 4F      JR      NZ,$4D64        
4D15: 21 B0 C2   LD      HL,$C2B0        
4D18: 09         ADD     HL,BC           
4D19: 7E         LD      A,(HL)          
4D1A: 3C         INC     A               
4D1B: 5F         LD      E,A             
4D1C: FE 0E      CP      $0E             
4D1E: 20 26      JR      NZ,$4D46        
4D20: FA 0E DB   LD      A,($DB0E)       
4D23: FE 0E      CP      $0E             
4D25: 20 1F      JR      NZ,$4D46        
4D27: F0 F8      LD      A,($F8)         
4D29: E6 20      AND     $20             
4D2B: 20 0E      JR      NZ,$4D3B        
4D2D: CD 62 7A   CALL    $7A62           
4D30: CD ED 27   CALL    $27ED           
4D33: 17         RLA                     
4D34: 17         RLA                     
4D35: 17         RLA                     
4D36: E6 18      AND     $18             
4D38: EA 7C DB   LD      ($DB7C),A       
4D3B: FA 7C DB   LD      A,($DB7C)       
4D3E: 1F         RRA                     
4D3F: 1F         RRA                     
4D40: 1F         RRA                     
4D41: E6 03      AND     $03             
4D43: C6 17      ADD     $17             
4D45: 5F         LD      E,A             
4D46: 7B         LD      A,E             
4D47: FE 0D      CP      $0D             
4D49: 20 15      JR      NZ,$4D60        
4D4B: AF         XOR     A               
4D4C: EA 6B C1   LD      ($C16B),A       
4D4F: EA 6C C1   LD      ($C16C),A       
4D52: EA 96 DB   LD      ($DB96),A       
4D55: 3E 07      LD      A,$07           
4D57: EA 95 DB   LD      ($DB95),A       
4D5A: 3E 01      LD      A,$01           
4D5C: EA A2 C5   LD      ($C5A2),A       
4D5F: C9         RET                     
4D60: CD 8E 21   CALL    $218E           
4D63: C9         RET                     
4D64: AF         XOR     A               
4D65: C3 87 3B   JP      $3B87           
4D68: F0 F8      LD      A,($F8)         
4D6A: E6 20      AND     $20             
4D6C: C2 B0 79   JP      NZ,$79B0        
4D6F: 21 B0 C2   LD      HL,$C2B0        
4D72: 09         ADD     HL,BC           
4D73: 7E         LD      A,(HL)          
4D74: A7         AND     A               
4D75: C2 00 4F   JP      NZ,$4F00        
4D78: F0 F0      LD      A,($F0)         
4D7A: C7         RST     0X00            
4D7B: 89         ADC     A,C             
4D7C: 4D         LD      C,L             
4D7D: CD 4D D7   CALL    $D74D           
4D80: 4D         LD      C,L             
4D81: 11 4E 42   LD      DE,$424E        
4D84: 4E         LD      C,(HL)          
4D85: 60         LD      H,B             
4D86: 00         NOP                     
4D87: 62         LD      H,D             
4D88: 00         NOP                     
4D89: 79         LD      A,C             
4D8A: EA 01 D2   LD      ($D201),A       
4D8D: 21 00 C2   LD      HL,$C200        
4D90: 09         ADD     HL,BC           
4D91: 36 50      LD      (HL),$50        
4D93: CD CD 4D   CALL    $4DCD           
4D96: FA 49 DB   LD      A,($DB49)       
4D99: E6 01      AND     $01             
4D9B: C8         RET     Z               
4D9C: FA 66 C1   LD      A,($C166)       
4D9F: FE 01      CP      $01             
4DA1: C0         RET     NZ              
4DA2: FA 4A DB   LD      A,($DB4A)       
4DA5: FE 02      CP      $02             
4DA7: C0         RET     NZ              
4DA8: 3E DC      LD      A,$DC           
4DAA: CD 01 3C   CALL    $3C01           
4DAD: 21 00 C2   LD      HL,$C200        
4DB0: 19         ADD     HL,DE           
4DB1: 36 94      LD      (HL),$94        
4DB3: 21 10 C2   LD      HL,$C210        
4DB6: 19         ADD     HL,DE           
4DB7: 36 D8      LD      (HL),$D8        
4DB9: 21 B0 C2   LD      HL,$C2B0        
4DBC: 19         ADD     HL,DE           
4DBD: 34         INC     (HL)            
4DBE: 21 40 C3   LD      HL,$C340        
4DC1: 19         ADD     HL,DE           
4DC2: 36 C1      LD      (HL),$C1        
4DC4: 3E 55      LD      A,$55           
4DC6: EA 68 D3   LD      ($D368),A       
4DC9: C3 8D 3B   JP      $3B8D           
4DCC: C9         RET                     
4DCD: 11 85 4D   LD      DE,$4D85        
4DD0: CD 3B 3C   CALL    $3C3B           
4DD3: CD 00 78   CALL    $7800           
4DD6: C9         RET                     
4DD7: 3E 02      LD      A,$02           
4DD9: E0 A1      LDFF00  ($A1),A         
4DDB: EA 67 C1   LD      ($C167),A       
4DDE: CD CD 4D   CALL    $4DCD           
4DE1: CD 91 08   CALL    $0891           
4DE4: 20 1E      JR      NZ,$4E04        
4DE6: 36 A0      LD      (HL),$A0        
4DE8: CD 8D 3B   CALL    $3B8D           
4DEB: 3E 02      LD      A,$02           
4DED: CD 01 3C   CALL    $3C01           
4DF0: 21 00 C2   LD      HL,$C200        
4DF3: 19         ADD     HL,DE           
4DF4: F0 D7      LD      A,($D7)         
4DF6: 77         LD      (HL),A          
4DF7: 21 10 C2   LD      HL,$C210        
4DFA: 19         ADD     HL,DE           
4DFB: F0 D8      LD      A,($D8)         
4DFD: 77         LD      (HL),A          
4DFE: 21 E0 C2   LD      HL,$C2E0        
4E01: 19         ADD     HL,DE           
4E02: 36 20      LD      (HL),$20        
4E04: C9         RET                     
4E05: F0 00      LD      A,($00)         
4E07: 64         LD      H,H             
4E08: 00         NOP                     
4E09: 00         NOP                     
4E0A: 00         NOP                     
4E0B: 66         LD      H,(HL)          
4E0C: 00         NOP                     
4E0D: 00         NOP                     
4E0E: 08 68 00   LD      ($0068),SP      
4E11: 3E 02      LD      A,$02           
4E13: E0 A1      LDFF00  ($A1),A         
4E15: EA 67 C1   LD      ($C167),A       
4E18: 21 05 4E   LD      HL,$4E05        
4E1B: 0E 03      LD      C,$03           
4E1D: CD 26 3D   CALL    $3D26           
4E20: CD 91 08   CALL    $0891           
4E23: CA 30 4E   JP      Z,$4E30         
4E26: FE 70      CP      $70             
4E28: 20 05      JR      NZ,$4E2F        
4E2A: 3E 10      LD      A,$10           
4E2C: EA 68 D3   LD      ($D368),A       
4E2F: C9         RET                     
4E30: F0 99      LD      A,($99)         
4E32: F5         PUSH    AF              
4E33: 3E 10      LD      A,$10           
4E35: E0 99      LDFF00  ($99),A         
4E37: 3E 6D      LD      A,$6D           
4E39: CD 85 21   CALL    $2185           
4E3C: F1         POP     AF              
4E3D: E0 99      LDFF00  ($99),A         
4E3F: C3 8D 3B   JP      $3B8D           
4E42: 3E 02      LD      A,$02           
4E44: E0 A1      LDFF00  ($A1),A         
4E46: EA 67 C1   LD      ($C167),A       
4E49: 21 05 4E   LD      HL,$4E05        
4E4C: 0E 03      LD      C,$03           
4E4E: CD 26 3D   CALL    $3D26           
4E51: FA 9F C1   LD      A,($C19F)       
4E54: A7         AND     A               
4E55: 20 22      JR      NZ,$4E79        
4E57: 3E D5      LD      A,$D5           
4E59: CD 01 3C   CALL    $3C01           
4E5C: F0 D7      LD      A,($D7)         
4E5E: 21 00 C2   LD      HL,$C200        
4E61: 19         ADD     HL,DE           
4E62: 77         LD      (HL),A          
4E63: F0 D8      LD      A,($D8)         
4E65: 21 10 C2   LD      HL,$C210        
4E68: 19         ADD     HL,DE           
4E69: 77         LD      (HL),A          
4E6A: 3E 01      LD      A,$01           
4E6C: EA 7B DB   LD      ($DB7B),A       
4E6F: AF         XOR     A               
4E70: EA 67 C1   LD      ($C167),A       
4E73: CD 62 7A   CALL    $7A62           
4E76: C3 B0 79   JP      $79B0           
4E79: C9         RET                     
4E7A: 6A         LD      L,D             
4E7B: 00         NOP                     
4E7C: 6C         LD      L,H             
4E7D: 00         NOP                     
4E7E: 6E         LD      L,(HL)          
4E7F: 00         NOP                     
4E80: 02         LD      (BC),A          
4E81: 02         LD      (BC),A          
4E82: 01 01 04   LD      BC,$0401        
4E85: 04         INC     B               
4E86: 04         INC     B               
4E87: 04         INC     B               
4E88: 04         INC     B               
4E89: 04         INC     B               
4E8A: 04         INC     B               
4E8B: 04         INC     B               
4E8C: 05         DEC     B               
4E8D: 06 07      LD      B,$07           
4E8F: 08 07 06   LD      ($0607),SP      
4E92: 05         DEC     B               
4E93: 04         INC     B               
4E94: 04         INC     B               
4E95: 04         INC     B               
4E96: 03         INC     BC              
4E97: 02         LD      (BC),A          
4E98: 01 00 01   LD      BC,$0100        
4E9B: 02         LD      (BC),A          
4E9C: 03         INC     BC              
4E9D: 04         INC     B               
4E9E: 05         DEC     B               
4E9F: 06 07      LD      B,$07           
4EA1: 08 08 08   LD      ($0808),SP      
4EA4: 09         ADD     HL,BC           
4EA5: 0A         LD      A,(BC)          
4EA6: 0B         DEC     BC              
4EA7: 0C         INC     C               
4EA8: 0C         INC     C               
4EA9: 0C         INC     C               
4EAA: 0B         DEC     BC              
4EAB: 0A         LD      A,(BC)          
4EAC: 09         ADD     HL,BC           
4EAD: 08 07 06   LD      ($0607),SP      
4EB0: 05         DEC     B               
4EB1: 04         INC     B               
4EB2: 05         DEC     B               
4EB3: 06 07      LD      B,$07           
4EB5: 08 09 0A   LD      ($0A09),SP      
4EB8: 0B         DEC     BC              
4EB9: 0B         DEC     BC              
4EBA: 0A         LD      A,(BC)          
4EBB: 09         ADD     HL,BC           
4EBC: 08 07 06   LD      ($0607),SP      
4EBF: 05         DEC     B               
4EC0: 04         INC     B               
4EC1: 03         INC     BC              
4EC2: 02         LD      (BC),A          
4EC3: 01 00 01   LD      BC,$0100        
4EC6: 02         LD      (BC),A          
4EC7: 03         INC     BC              
4EC8: 04         INC     B               
4EC9: 04         INC     B               
4ECA: 04         INC     B               
4ECB: 04         INC     B               
4ECC: 04         INC     B               
4ECD: 04         INC     B               
4ECE: 04         INC     B               
4ECF: 04         INC     B               
4ED0: 04         INC     B               
4ED1: 04         INC     B               
4ED2: 04         INC     B               
4ED3: 04         INC     B               
4ED4: 04         INC     B               
4ED5: 04         INC     B               
4ED6: 04         INC     B               
4ED7: 04         INC     B               
4ED8: 04         INC     B               
4ED9: 04         INC     B               
4EDA: 04         INC     B               
4EDB: 04         INC     B               
4EDC: 04         INC     B               
4EDD: 04         INC     B               
4EDE: 04         INC     B               
4EDF: 04         INC     B               
4EE0: 04         INC     B               
4EE1: 04         INC     B               
4EE2: 04         INC     B               
4EE3: 04         INC     B               
4EE4: 04         INC     B               
4EE5: 04         INC     B               
4EE6: 04         INC     B               
4EE7: 04         INC     B               
4EE8: 04         INC     B               
4EE9: 04         INC     B               
4EEA: 04         INC     B               
4EEB: 04         INC     B               
4EEC: 00         NOP                     
4EED: 03         INC     BC              
4EEE: 06 07      LD      B,$07           
4EF0: 08 07 06   LD      ($0607),SP      
4EF3: 03         INC     BC              
4EF4: 00         NOP                     
4EF5: FD                              
4EF6: FA F9 F8   LD      A,($F8F9)       
4EF9: F9         LD      SP,HL           
4EFA: FA FD 00   LD      A,($00FD)       
4EFD: 03         INC     BC              
4EFE: 06 07      LD      B,$07           
4F00: F0 E7      LD      A,($E7)         
4F02: 17         RLA                     
4F03: 17         RLA                     
4F04: E6 10      AND     $10             
4F06: E0 ED      LDFF00  ($ED),A         
4F08: 11 7A 4E   LD      DE,$4E7A        
4F0B: CD D0 3C   CALL    $3CD0           
4F0E: CD 9B 78   CALL    $789B           
4F11: CD 91 08   CALL    $0891           
4F14: 28 14      JR      Z,$4F2A         
4F16: FE 01      CP      $01             
4F18: CA B0 79   JP      Z,$79B0         
4F1B: 1F         RRA                     
4F1C: 1F         RRA                     
4F1D: 1F         RRA                     
4F1E: E6 03      AND     $03             
4F20: 5F         LD      E,A             
4F21: 50         LD      D,B             
4F22: 21 80 4E   LD      HL,$4E80        
4F25: 19         ADD     HL,DE           
4F26: 7E         LD      A,(HL)          
4F27: C3 87 3B   JP      $3B87           
4F2A: 3E 02      LD      A,$02           
4F2C: E0 A1      LDFF00  ($A1),A         
4F2E: EA 67 C1   LD      ($C167),A       
4F31: 21 D0 C3   LD      HL,$C3D0        
4F34: 09         ADD     HL,BC           
4F35: 7E         LD      A,(HL)          
4F36: 3C         INC     A               
4F37: 77         LD      (HL),A          
4F38: E6 07      AND     $07             
4F3A: 20 23      JR      NZ,$4F5F        
4F3C: 21 C0 C2   LD      HL,$C2C0        
4F3F: 09         ADD     HL,BC           
4F40: 34         INC     (HL)            
4F41: 7E         LD      A,(HL)          
4F42: FE 49      CP      $49             
4F44: 20 19      JR      NZ,$4F5F        
4F46: FA 01 D2   LD      A,($D201)       
4F49: 5F         LD      E,A             
4F4A: 50         LD      D,B             
4F4B: 21 90 C2   LD      HL,$C290        
4F4E: 19         ADD     HL,DE           
4F4F: 34         INC     (HL)            
4F50: 21 20 C4   LD      HL,$C420        
4F53: 19         ADD     HL,DE           
4F54: 36 40      LD      (HL),$40        
4F56: 21 E0 C2   LD      HL,$C2E0        
4F59: 19         ADD     HL,DE           
4F5A: 36 80      LD      (HL),$80        
4F5C: C3 B0 79   JP      $79B0           
4F5F: 21 C0 C2   LD      HL,$C2C0        
4F62: 09         ADD     HL,BC           
4F63: 5E         LD      E,(HL)          
4F64: 50         LD      D,B             
4F65: 21 84 4E   LD      HL,$4E84        
4F68: 19         ADD     HL,DE           
4F69: 5E         LD      E,(HL)          
4F6A: 21 F0 4E   LD      HL,$4EF0        
4F6D: 19         ADD     HL,DE           
4F6E: 7E         LD      A,(HL)          
4F6F: 21 40 C2   LD      HL,$C240        
4F72: 09         ADD     HL,BC           
4F73: 77         LD      (HL),A          
4F74: 21 EC 4E   LD      HL,$4EEC        
4F77: 19         ADD     HL,DE           
4F78: 7E         LD      A,(HL)          
4F79: 21 50 C2   LD      HL,$C250        
4F7C: 09         ADD     HL,BC           
4F7D: 77         LD      (HL),A          
4F7E: CD 07 79   CALL    $7907           
4F81: 21 D0 C3   LD      HL,$C3D0        
4F84: 09         ADD     HL,BC           
4F85: 7E         LD      A,(HL)          
4F86: E6 07      AND     $07             
4F88: 20 20      JR      NZ,$4FAA        
4F8A: 3E DC      LD      A,$DC           
4F8C: CD 01 3C   CALL    $3C01           
4F8F: D8         RET     C               
4F90: F0 D7      LD      A,($D7)         
4F92: 21 00 C2   LD      HL,$C200        
4F95: 19         ADD     HL,DE           
4F96: 77         LD      (HL),A          
4F97: F0 D8      LD      A,($D8)         
4F99: 21 10 C2   LD      HL,$C210        
4F9C: 19         ADD     HL,DE           
4F9D: 77         LD      (HL),A          
4F9E: 21 B0 C2   LD      HL,$C2B0        
4FA1: 19         ADD     HL,DE           
4FA2: 36 01      LD      (HL),$01        
4FA4: 21 E0 C2   LD      HL,$C2E0        
4FA7: 19         ADD     HL,DE           
4FA8: 36 1F      LD      (HL),$1F        
4FAA: C9         RET                     
4FAB: 60         LD      H,B             
4FAC: 00         NOP                     
4FAD: 62         LD      H,D             
4FAE: 00         NOP                     
4FAF: 64         LD      H,H             
4FB0: 00         NOP                     
4FB1: 66         LD      H,(HL)          
4FB2: 00         NOP                     
4FB3: 62         LD      H,D             
4FB4: 20 60      JR      NZ,$5016        
4FB6: 20 66      JR      NZ,$501E        
4FB8: 20 64      JR      NZ,$501E        
4FBA: 20 68      JR      NZ,$5024        
4FBC: 00         NOP                     
4FBD: 6A         LD      L,D             
4FBE: 00         NOP                     
4FBF: 6C         LD      L,H             
4FC0: 00         NOP                     
4FC1: 6E         LD      L,(HL)          
4FC2: 00         NOP                     
4FC3: 6A         LD      L,D             
4FC4: 20 68      JR      NZ,$502E        
4FC6: 20 6E      JR      NZ,$5036        
4FC8: 20 6C      JR      NZ,$5036        
4FCA: 20 70      JR      NZ,$503C        
4FCC: 00         NOP                     
4FCD: 72         LD      (HL),D          
4FCE: 00         NOP                     
4FCF: 74         LD      (HL),H          
4FD0: 00         NOP                     
4FD1: 76         HALT                    
4FD2: 00         NOP                     
4FD3: 72         LD      (HL),D          
4FD4: 20 70      JR      NZ,$5046        
4FD6: 20 76      JR      NZ,$504E        
4FD8: 20 74      JR      NZ,$504E        
4FDA: 20 F2      JR      NZ,$4FCE        
4FDC: 0E 21      LD      C,$21           
4FDE: 40         LD      B,B             
4FDF: C3 09 36   JP      $3609           
4FE2: D2 11 AB   JP      NC,$AB11        
4FE5: 4F         LD      C,A             
4FE6: CD 3B 3C   CALL    $3C3B           
4FE9: 21 D0 C2   LD      HL,$C2D0        
4FEC: 09         ADD     HL,BC           
4FED: 7E         LD      A,(HL)          
4FEE: A7         AND     A               
4FEF: 20 06      JR      NZ,$4FF7        
4FF1: 34         INC     (HL)            
4FF2: 3E 57      LD      A,$57           
4FF4: EA 68 D3   LD      ($D368),A       
4FF7: FA 6B DB   LD      A,($DB6B)       
4FFA: A7         AND     A               
4FFB: C2 90 50   JP      NZ,$5090        
4FFE: CD 9B 78   CALL    $789B           
5001: CD 00 78   CALL    $7800           
5004: F0 E7      LD      A,($E7)         
5006: E6 7F      AND     $7F             
5008: 20 0A      JR      NZ,$5014        
500A: CD ED 27   CALL    $27ED           
500D: E6 02      AND     $02             
500F: 21 80 C3   LD      HL,$C380        
5012: 09         ADD     HL,BC           
5013: 77         LD      (HL),A          
5014: F0 E7      LD      A,($E7)         
5016: 1E 00      LD      E,$00           
5018: E6 30      AND     $30             
501A: 28 01      JR      Z,$501D         
501C: 1C         INC     E               
501D: 21 80 C3   LD      HL,$C380        
5020: 09         ADD     HL,BC           
5021: 7B         LD      A,E             
5022: 86         ADD     A,(HL)          
5023: CD 87 3B   CALL    $3B87           
5026: F0 E7      LD      A,($E7)         
5028: E6 3F      AND     $3F             
502A: FE 0F      CP      $0F             
502C: 20 2F      JR      NZ,$505D        
502E: 3E 08      LD      A,$08           
5030: CD 01 3C   CALL    $3C01           
5033: 38 27      JR      C,$505C         
5035: C5         PUSH    BC              
5036: 21 80 C3   LD      HL,$C380        
5039: 09         ADD     HL,BC           
503A: 4E         LD      C,(HL)          
503B: CB 39      SET     1,E             
503D: 21 DB 4F   LD      HL,$4FDB        
5040: 09         ADD     HL,BC           
5041: F0 D7      LD      A,($D7)         
5043: 86         ADD     A,(HL)          
5044: 21 00 C2   LD      HL,$C200        
5047: 19         ADD     HL,DE           
5048: 77         LD      (HL),A          
5049: F0 D8      LD      A,($D8)         
504B: 21 10 C2   LD      HL,$C210        
504E: 19         ADD     HL,DE           
504F: 77         LD      (HL),A          
5050: 21 E0 C2   LD      HL,$C2E0        
5053: 19         ADD     HL,DE           
5054: 36 17      LD      (HL),$17        
5056: 21 40 C4   LD      HL,$C440        
5059: 19         ADD     HL,DE           
505A: 34         INC     (HL)            
505B: C1         POP     BC              
505C: C9         RET                     
505D: CD 4E 78   CALL    $784E           
5060: 30 0D      JR      NC,$506F        
5062: FA 7B DB   LD      A,($DB7B)       
5065: A7         AND     A               
5066: 3E 8B      LD      A,$8B           
5068: 28 02      JR      Z,$506C         
506A: 3E 8C      LD      A,$8C           
506C: CD 85 21   CALL    $2185           
506F: C9         RET                     
5070: 10 11      STOP    $11             
5072: 12         LD      (DE),A          
5073: 13         INC     DE              
5074: 13         INC     DE              
5075: 12         LD      (DE),A          
5076: 11 10 00   LD      DE,$0010        
5079: 09         ADD     HL,BC           
507A: 02         LD      (BC),A          
507B: 09         ADD     HL,BC           
507C: 00         NOP                     
507D: F7         RST     0X30            
507E: FE F7      CP      $F7             
5080: 0C         INC     C               
5081: 09         ADD     HL,BC           
5082: 0A         LD      A,(BC)          
5083: F7         RST     0X30            
5084: F4                              
5085: F7         RST     0X30            
5086: F6 09      OR      $09             
5088: 03         INC     BC              
5089: 01 00 00   LD      BC,$0000        
508C: 00         NOP                     
508D: 00         NOP                     
508E: 01 03 F0   LD      BC,$F003        
5091: F0 A7      LD      A,($A7)         
5093: 20 09      JR      NZ,$509E        
5095: 21 10 C2   LD      HL,$C210        
5098: 09         ADD     HL,BC           
5099: 36 50      LD      (HL),$50        
509B: CD 8D 3B   CALL    $3B8D           
509E: 1E 00      LD      E,$00           
50A0: 21 40 C2   LD      HL,$C240        
50A3: 09         ADD     HL,BC           
50A4: 7E         LD      A,(HL)          
50A5: E6 80      AND     $80             
50A7: 20 02      JR      NZ,$50AB        
50A9: 1E 02      LD      E,$02           
50AB: 21 80 C3   LD      HL,$C380        
50AE: 09         ADD     HL,BC           
50AF: 73         LD      (HL),E          
50B0: F0 E7      LD      A,($E7)         
50B2: 1F         RRA                     
50B3: 1F         RRA                     
50B4: 1F         RRA                     
50B5: E6 07      AND     $07             
50B7: 5F         LD      E,A             
50B8: 50         LD      D,B             
50B9: 21 70 50   LD      HL,$5070        
50BC: 19         ADD     HL,DE           
50BD: 7E         LD      A,(HL)          
50BE: D6 03      SUB     $03             
50C0: 21 10 C3   LD      HL,$C310        
50C3: 09         ADD     HL,BC           
50C4: 77         LD      (HL),A          
50C5: 21 80 C3   LD      HL,$C380        
50C8: 09         ADD     HL,BC           
50C9: F0 E7      LD      A,($E7)         
50CB: E6 20      AND     $20             
50CD: 3E 04      LD      A,$04           
50CF: 20 02      JR      NZ,$50D3        
50D1: 3E 05      LD      A,$05           
50D3: 86         ADD     A,(HL)          
50D4: CD 87 3B   CALL    $3B87           
50D7: F0 EC      LD      A,($EC)         
50D9: D6 10      SUB     $10             
50DB: E0 EC      LDFF00  ($EC),A         
50DD: 21 80 C3   LD      HL,$C380        
50E0: 09         ADD     HL,BC           
50E1: F0 E7      LD      A,($E7)         
50E3: 1F         RRA                     
50E4: 1F         RRA                     
50E5: E6 01      AND     $01             
50E7: 86         ADD     A,(HL)          
50E8: E0 F1      LDFF00  ($F1),A         
50EA: 21 40 C3   LD      HL,$C340        
50ED: 09         ADD     HL,BC           
50EE: CB A6      SET     1,E             
50F0: 11 CB 4F   LD      DE,$4FCB        
50F3: CD 3B 3C   CALL    $3C3B           
50F6: CD BA 3D   CALL    $3DBA           
50F9: CD 9B 78   CALL    $789B           
50FC: F0 E7      LD      A,($E7)         
50FE: E6 3F      AND     $3F             
5100: 20 22      JR      NZ,$5124        
5102: CD ED 27   CALL    $27ED           
5105: E6 01      AND     $01             
5107: 20 1B      JR      NZ,$5124        
5109: CD ED 27   CALL    $27ED           
510C: E6 07      AND     $07             
510E: 5F         LD      E,A             
510F: 50         LD      D,B             
5110: 21 80 50   LD      HL,$5080        
5113: 19         ADD     HL,DE           
5114: 7E         LD      A,(HL)          
5115: 21 40 C2   LD      HL,$C240        
5118: 09         ADD     HL,BC           
5119: 77         LD      (HL),A          
511A: 21 78 50   LD      HL,$5078        
511D: 19         ADD     HL,DE           
511E: 7E         LD      A,(HL)          
511F: 21 50 C2   LD      HL,$C250        
5122: 09         ADD     HL,BC           
5123: 77         LD      (HL),A          
5124: F0 E7      LD      A,($E7)         
5126: 1F         RRA                     
5127: 1F         RRA                     
5128: 1F         RRA                     
5129: 00         NOP                     
512A: 00         NOP                     
512B: E6 07      AND     $07             
512D: 5F         LD      E,A             
512E: 50         LD      D,B             
512F: 21 88 50   LD      HL,$5088        
5132: 19         ADD     HL,DE           
5133: F0 E7      LD      A,($E7)         
5135: A6         AND     (HL)            
5136: CC 07 79   CALL    Z,$7907         
5139: CD 9E 3B   CALL    $3B9E           
513C: 21 A0 C2   LD      HL,$C2A0        
513F: 09         ADD     HL,BC           
5140: 7E         LD      A,(HL)          
5141: E6 03      AND     $03             
5143: 28 08      JR      Z,$514D         
5145: 21 40 C2   LD      HL,$C240        
5148: 09         ADD     HL,BC           
5149: 7E         LD      A,(HL)          
514A: 2F         CPL                     
514B: 3C         INC     A               
514C: 77         LD      (HL),A          
514D: 21 A0 C2   LD      HL,$C2A0        
5150: 09         ADD     HL,BC           
5151: 7E         LD      A,(HL)          
5152: E6 0C      AND     $0C             
5154: 28 08      JR      Z,$515E         
5156: 21 50 C2   LD      HL,$C250        
5159: 09         ADD     HL,BC           
515A: 7E         LD      A,(HL)          
515B: 2F         CPL                     
515C: 3C         INC     A               
515D: 77         LD      (HL),A          
515E: CD 5A 79   CALL    $795A           
5161: C6 12      ADD     $12             
5163: FE 24      CP      $24             
5165: D0         RET     NC              
5166: CD 6A 79   CALL    $796A           
5169: C6 10      ADD     $10             
516B: FE 20      CP      $20             
516D: D0         RET     NC              
516E: CD 91 08   CALL    $0891           
5171: C0         RET     NZ              
5172: 36 80      LD      (HL),$80        
5174: 3E 8D      LD      A,$8D           
5176: CD 85 21   CALL    $2185           
5179: C9         RET                     
517A: F0 00      LD      A,($00)         
517C: 78         LD      A,B             
517D: 00         NOP                     
517E: F0 08      LD      A,($08)         
5180: 7A         LD      A,D             
5181: 00         NOP                     
5182: 00         NOP                     
5183: 00         NOP                     
5184: 7C         LD      A,H             
5185: 00         NOP                     
5186: 00         NOP                     
5187: 08 7E 00   LD      ($007E),SP      
518A: FA A5 DB   LD      A,($DBA5)       
518D: A7         AND     A               
518E: 28 0F      JR      Z,$519F         
5190: F0 F6      LD      A,($F6)         
5192: FE E4      CP      $E4             
5194: CA 68 4D   JP      Z,$4D68         
5197: FE F4      CP      $F4             
5199: CA 68 4D   JP      Z,$4D68         
519C: C3 DD 4F   JP      $4FDD           
519F: F0 F8      LD      A,($F8)         
51A1: E6 20      AND     $20             
51A3: C2 B0 79   JP      NZ,$79B0        
51A6: F0 F0      LD      A,($F0)         
51A8: C7         RST     0X00            
51A9: AD         XOR     L               
51AA: 51         LD      D,C             
51AB: 42         LD      B,D             
51AC: 52         LD      D,D             
51AD: CD 9B 78   CALL    $789B           
51B0: FA 43 DB   LD      A,($DB43)       
51B3: FE 02      CP      $02             
51B5: D8         RET     C               
51B6: CD 5A 79   CALL    $795A           
51B9: C6 08      ADD     $08             
51BB: FE 10      CP      $10             
51BD: 30 7D      JR      NC,$523C        
51BF: CD 6A 79   CALL    $796A           
51C2: C6 10      ADD     $10             
51C4: FE 20      CP      $20             
51C6: 30 74      JR      NC,$523C        
51C8: FA 33 C1   LD      A,($C133)       
51CB: A7         AND     A               
51CC: 28 6E      JR      Z,$523C         
51CE: F0 9E      LD      A,($9E)         
51D0: FE 02      CP      $02             
51D2: 20 68      JR      NZ,$523C        
51D4: 21 D0 C3   LD      HL,$C3D0        
51D7: 09         ADD     HL,BC           
51D8: 7E         LD      A,(HL)          
51D9: 3C         INC     A               
51DA: 77         LD      (HL),A          
51DB: FE 18      CP      $18             
51DD: C0         RET     NZ              
51DE: CD 91 08   CALL    $0891           
51E1: 36 40      LD      (HL),$40        
51E3: 21 46 D7   LD      HL,$D746        
51E6: 36 0C      LD      (HL),$0C        
51E8: 21 56 D7   LD      HL,$D756        
51EB: 36 C6      LD      (HL),$C6        
51ED: 3E 50      LD      A,$50           
51EF: E0 CE      LDFF00  ($CE),A         
51F1: 3E 30      LD      A,$30           
51F3: E0 CD      LDFF00  ($CD),A         
51F5: CD 39 28   CALL    $2839           
51F8: 21 01 D6   LD      HL,$D601        
51FB: FA 00 D6   LD      A,($D600)       
51FE: 5F         LD      E,A             
51FF: C6 0E      ADD     $0E             
5201: EA 00 D6   LD      ($D600),A       
5204: 16 00      LD      D,$00           
5206: 19         ADD     HL,DE           
5207: F0 CF      LD      A,($CF)         
5209: 22         LD      (HLI),A         
520A: F0 D0      LD      A,($D0)         
520C: 22         LD      (HLI),A         
520D: 3E 83      LD      A,$83           
520F: 22         LD      (HLI),A         
5210: 3E 0F      LD      A,$0F           
5212: 22         LD      (HLI),A         
5213: 3E 0F      LD      A,$0F           
5215: 22         LD      (HLI),A         
5216: 3E 68      LD      A,$68           
5218: 22         LD      (HLI),A         
5219: 3E 77      LD      A,$77           
521B: 22         LD      (HLI),A         
521C: F0 CF      LD      A,($CF)         
521E: 22         LD      (HLI),A         
521F: F0 D0      LD      A,($D0)         
5221: 3C         INC     A               
5222: 22         LD      (HLI),A         
5223: 3E 83      LD      A,$83           
5225: 22         LD      (HLI),A         
5226: 3E 0F      LD      A,$0F           
5228: 22         LD      (HLI),A         
5229: 3E 0F      LD      A,$0F           
522B: 22         LD      (HLI),A         
522C: 3E 69      LD      A,$69           
522E: 22         LD      (HLI),A         
522F: 3E 4B      LD      A,$4B           
5231: 22         LD      (HLI),A         
5232: 70         LD      (HL),B          
5233: 3E 11      LD      A,$11           
5235: E0 F4      LDFF00  ($F4),A         
5237: CD 8D 3B   CALL    $3B8D           
523A: 18 06      JR      $5242           
523C: 21 D0 C3   LD      HL,$C3D0        
523F: 09         ADD     HL,BC           
5240: 70         LD      (HL),B          
5241: C9         RET                     
5242: CD 9B 78   CALL    $789B           
5245: 3E 02      LD      A,$02           
5247: E0 A1      LDFF00  ($A1),A         
5249: EA 67 C1   LD      ($C167),A       
524C: 21 7A 51   LD      HL,$517A        
524F: 0E 04      LD      C,$04           
5251: CD 26 3D   CALL    $3D26           
5254: CD 91 08   CALL    $0891           
5257: 20 5D      JR      NZ,$52B6        
5259: EA 67 C1   LD      ($C167),A       
525C: 21 36 D7   LD      HL,$D736        
525F: 36 91      LD      (HL),$91        
5261: 21 46 D7   LD      HL,$D746        
5264: 36 5E      LD      (HL),$5E        
5266: 3E 50      LD      A,$50           
5268: E0 CE      LDFF00  ($CE),A         
526A: 3E 20      LD      A,$20           
526C: E0 CD      LDFF00  ($CD),A         
526E: CD 39 28   CALL    $2839           
5271: 21 01 D6   LD      HL,$D601        
5274: FA 00 D6   LD      A,($D600)       
5277: 5F         LD      E,A             
5278: C6 0E      ADD     $0E             
527A: EA 00 D6   LD      ($D600),A       
527D: 16 00      LD      D,$00           
527F: 19         ADD     HL,DE           
5280: F0 CF      LD      A,($CF)         
5282: 22         LD      (HLI),A         
5283: F0 D0      LD      A,($D0)         
5285: 22         LD      (HLI),A         
5286: 3E 83      LD      A,$83           
5288: 22         LD      (HLI),A         
5289: 3E 00      LD      A,$00           
528B: 22         LD      (HLI),A         
528C: 3E 10      LD      A,$10           
528E: 22         LD      (HLI),A         
528F: 3E 02      LD      A,$02           
5291: 22         LD      (HLI),A         
5292: 3E 12      LD      A,$12           
5294: 22         LD      (HLI),A         
5295: F0 CF      LD      A,($CF)         
5297: 22         LD      (HLI),A         
5298: F0 D0      LD      A,($D0)         
529A: 3C         INC     A               
529B: 22         LD      (HLI),A         
529C: 3E 83      LD      A,$83           
529E: 22         LD      (HLI),A         
529F: 3E 6C      LD      A,$6C           
52A1: 22         LD      (HLI),A         
52A2: 3E 6D      LD      A,$6D           
52A4: 22         LD      (HLI),A         
52A5: 3E 03      LD      A,$03           
52A7: 22         LD      (HLI),A         
52A8: 3E 13      LD      A,$13           
52AA: 22         LD      (HLI),A         
52AB: 70         LD      (HL),B          
52AC: 3E 23      LD      A,$23           
52AE: E0 F2      LDFF00  ($F2),A         
52B0: CD 62 7A   CALL    $7A62           
52B3: C3 B0 79   JP      $79B0           
52B6: 21 50 C2   LD      HL,$C250        
52B9: 09         ADD     HL,BC           
52BA: 36 FC      LD      (HL),$FC        
52BC: CD 0A 79   CALL    $790A           
52BF: C9         RET                     
52C0: F8 F8      LDHL    SP,$F8          
52C2: 60         LD      H,B             
52C3: 00         NOP                     
52C4: F8 00      LDHL    SP,$00          
52C6: 62         LD      H,D             
52C7: 00         NOP                     
52C8: F8 08      LDHL    SP,$08          
52CA: 62         LD      H,D             
52CB: 20 F8      JR      NZ,$52C5        
52CD: 10 60      STOP    $60             
52CF: 20 08      JR      NZ,$52D9        
52D1: F8 60      LDHL    SP,$60          
52D3: 40         LD      B,B             
52D4: 08 00 62   LD      ($6200),SP      
52D7: 40         LD      B,B             
52D8: 08 08 62   LD      ($6208),SP      
52DB: 60         LD      H,B             
52DC: 08 10 60   LD      ($6010),SP      
52DF: 60         LD      H,B             
52E0: 00         NOP                     
52E1: 04         INC     B               
52E2: 08 04 F0   LD      ($F004),SP      
52E5: E7         RST     0X20            
52E6: 17         RLA                     
52E7: 17         RLA                     
52E8: E6 10      AND     $10             
52EA: E0 ED      LDFF00  ($ED),A         
52EC: F0 E7      LD      A,($E7)         
52EE: 1F         RRA                     
52EF: 1F         RRA                     
52F0: 1F         RRA                     
52F1: 1F         RRA                     
52F2: E6 03      AND     $03             
52F4: 5F         LD      E,A             
52F5: 50         LD      D,B             
52F6: 21 E0 52   LD      HL,$52E0        
52F9: 19         ADD     HL,DE           
52FA: 7E         LD      A,(HL)          
52FB: E0 F5      LDFF00  ($F5),A         
52FD: 21 C0 52   LD      HL,$52C0        
5300: 0E 08      LD      C,$08           
5302: CD 26 3D   CALL    $3D26           
5305: CD 9B 78   CALL    $789B           
5308: CD BF 3B   CALL    $3BBF           
530B: CD 07 79   CALL    $7907           
530E: CD 9E 3B   CALL    $3B9E           
5311: 21 A0 C2   LD      HL,$C2A0        
5314: 09         ADD     HL,BC           
5315: 7E         LD      A,(HL)          
5316: E6 03      AND     $03             
5318: 28 08      JR      Z,$5322         
531A: 21 40 C2   LD      HL,$C240        
531D: 09         ADD     HL,BC           
531E: 7E         LD      A,(HL)          
531F: 2F         CPL                     
5320: 3C         INC     A               
5321: 77         LD      (HL),A          
5322: 21 A0 C2   LD      HL,$C2A0        
5325: 09         ADD     HL,BC           
5326: 7E         LD      A,(HL)          
5327: E6 0C      AND     $0C             
5329: 28 08      JR      Z,$5333         
532B: 21 50 C2   LD      HL,$C250        
532E: 09         ADD     HL,BC           
532F: 7E         LD      A,(HL)          
5330: 2F         CPL                     
5331: 3C         INC     A               
5332: 77         LD      (HL),A          
5333: C9         RET                     
5334: 7A         LD      A,D             
5335: 40         LD      B,B             
5336: 7A         LD      A,D             
5337: 60         LD      H,B             
5338: 7A         LD      A,D             
5339: 50         LD      D,B             
533A: 7A         LD      A,D             
533B: 70         LD      (HL),B          
533C: 7A         LD      A,D             
533D: 00         NOP                     
533E: 7A         LD      A,D             
533F: 20 7A      JR      NZ,$53BB        
5341: 10 7A      STOP    $7A             
5343: 30 21      JR      NC,$5366        
5345: B0         OR      B               
5346: C2 09 7E   JP      NZ,$7E09        
5349: A7         AND     A               
534A: C2 51 54   JP      NZ,$5451        
534D: F0 F0      LD      A,($F0)         
534F: C7         RST     0X00            
5350: 56         LD      D,(HL)          
5351: 53         LD      D,E             
5352: 6A         LD      L,D             
5353: 53         LD      D,E             
5354: C3 53 CD   JP      $CD53           
5357: 91         SUB     C               
5358: 08 CD ED   LD      ($EDCD),SP      
535B: 27         DAA                     
535C: E6 3F      AND     $3F             
535E: C6 30      ADD     $30             
5360: 77         LD      (HL),A          
5361: C3 8D 3B   JP      $3B8D           
5364: FF         RST     0X38            
5365: 01 FD 03   LD      BC,$03FD        
5368: F4                              
5369: F4                              
536A: CD 91 08   CALL    $0891           
536D: 20 53      JR      NZ,$53C2        
536F: FA A1 C5   LD      A,($C5A1)       
5372: FE 02      CP      $02             
5374: D0         RET     NC              
5375: 21 50 C2   LD      HL,$C250        
5378: 09         ADD     HL,BC           
5379: 36 D0      LD      (HL),$D0        
537B: CD 8D 3B   CALL    $3B8D           
537E: 3E 01      LD      A,$01           
5380: E0 E9      LDFF00  ($E9),A         
5382: 3E DA      LD      A,$DA           
5384: CD 01 3C   CALL    $3C01           
5387: D8         RET     C               
5388: F0 D8      LD      A,($D8)         
538A: 21 10 C2   LD      HL,$C210        
538D: 19         ADD     HL,DE           
538E: 77         LD      (HL),A          
538F: 21 B0 C2   LD      HL,$C2B0        
5392: 19         ADD     HL,DE           
5393: 36 02      LD      (HL),$02        
5395: C5         PUSH    BC              
5396: F0 E9      LD      A,($E9)         
5398: 4F         LD      C,A             
5399: 21 64 53   LD      HL,$5364        
539C: 09         ADD     HL,BC           
539D: F0 D7      LD      A,($D7)         
539F: 86         ADD     A,(HL)          
53A0: 21 00 C2   LD      HL,$C200        
53A3: 19         ADD     HL,DE           
53A4: 77         LD      (HL),A          
53A5: 21 66 53   LD      HL,$5366        
53A8: 09         ADD     HL,BC           
53A9: 7E         LD      A,(HL)          
53AA: 21 40 C2   LD      HL,$C240        
53AD: 19         ADD     HL,DE           
53AE: 77         LD      (HL),A          
53AF: 21 68 53   LD      HL,$5368        
53B2: 09         ADD     HL,BC           
53B3: 7E         LD      A,(HL)          
53B4: 21 50 C2   LD      HL,$C250        
53B7: 19         ADD     HL,DE           
53B8: 77         LD      (HL),A          
53B9: C1         POP     BC              
53BA: F0 E9      LD      A,($E9)         
53BC: 3D         DEC     A               
53BD: FE FF      CP      $FF             
53BF: 20 BF      JR      NZ,$5380        
53C1: C9         RET                     
53C2: C9         RET                     
53C3: 21 A0 C5   LD      HL,$C5A0        
53C6: 34         INC     (HL)            
53C7: 11 34 53   LD      DE,$5334        
53CA: CD 3B 3C   CALL    $3C3B           
53CD: CD 9B 78   CALL    $789B           
53D0: CD BF 3B   CALL    $3BBF           
53D3: CD 0A 79   CALL    $790A           
53D6: 21 50 C2   LD      HL,$C250        
53D9: 09         ADD     HL,BC           
53DA: 34         INC     (HL)            
53DB: 1E 00      LD      E,$00           
53DD: 7E         LD      A,(HL)          
53DE: E6 80      AND     $80             
53E0: 20 02      JR      NZ,$53E4        
53E2: 1E 02      LD      E,$02           
53E4: F0 E7      LD      A,($E7)         
53E6: 1F         RRA                     
53E7: 1F         RRA                     
53E8: E6 01      AND     $01             
53EA: 83         ADD     A,E             
53EB: CD 87 3B   CALL    $3B87           
53EE: 21 10 C2   LD      HL,$C210        
53F1: 09         ADD     HL,BC           
53F2: 7E         LD      A,(HL)          
53F3: FE 70      CP      $70             
53F5: 38 09      JR      C,$5400         
53F7: 36 70      LD      (HL),$70        
53F9: CD 8D 3B   CALL    $3B8D           
53FC: 70         LD      (HL),B          
53FD: CD 7E 53   CALL    $537E           
5400: F0 E7      LD      A,($E7)         
5402: A9         XOR     C               
5403: E6 0F      AND     $0F             
5405: C0         RET     NZ              
5406: 3E DA      LD      A,$DA           
5408: CD 01 3C   CALL    $3C01           
540B: D8         RET     C               
540C: F0 D7      LD      A,($D7)         
540E: 21 00 C2   LD      HL,$C200        
5411: 19         ADD     HL,DE           
5412: 77         LD      (HL),A          
5413: F0 D8      LD      A,($D8)         
5415: 21 10 C2   LD      HL,$C210        
5418: 19         ADD     HL,DE           
5419: 77         LD      (HL),A          
541A: 21 E0 C2   LD      HL,$C2E0        
541D: 19         ADD     HL,DE           
541E: 36 18      LD      (HL),$18        
5420: 21 B0 C2   LD      HL,$C2B0        
5423: 19         ADD     HL,DE           
5424: 36 01      LD      (HL),$01        
5426: F0 F1      LD      A,($F1)         
5428: 17         RLA                     
5429: E6 04      AND     $04             
542B: 21 B0 C3   LD      HL,$C3B0        
542E: 19         ADD     HL,DE           
542F: 77         LD      (HL),A          
5430: C9         RET                     
5431: 7C         LD      A,H             
5432: 40         LD      B,B             
5433: 7C         LD      A,H             
5434: 60         LD      H,B             
5435: 7C         LD      A,H             
5436: 50         LD      D,B             
5437: 7C         LD      A,H             
5438: 70         LD      (HL),B          
5439: 7E         LD      A,(HL)          
543A: 40         LD      B,B             
543B: 7E         LD      A,(HL)          
543C: 60         LD      H,B             
543D: 7E         LD      A,(HL)          
543E: 50         LD      D,B             
543F: 7E         LD      A,(HL)          
5440: 70         LD      (HL),B          
5441: 7C         LD      A,H             
5442: 00         NOP                     
5443: 7C         LD      A,H             
5444: 20 7C      JR      NZ,$54C2        
5446: 10 7C      STOP    $7C             
5448: 30 7E      JR      NC,$54C8        
544A: 00         NOP                     
544B: 7E         LD      A,(HL)          
544C: 20 7E      JR      NZ,$54CC        
544E: 10 7E      STOP    $7E             
5450: 30 FE      JR      NC,$5450        
5452: 02         LD      (BC),A          
5453: 28 2C      JR      Z,$5481         
5455: F0 E7      LD      A,($E7)         
5457: A9         XOR     C               
5458: 1F         RRA                     
5459: 38 12      JR      C,$546D         
545B: F0 E7      LD      A,($E7)         
545D: 1F         RRA                     
545E: 1F         RRA                     
545F: E6 01      AND     $01             
5461: 5F         LD      E,A             
5462: F0 F1      LD      A,($F1)         
5464: 83         ADD     A,E             
5465: E0 F1      LDFF00  ($F1),A         
5467: 11 31 54   LD      DE,$5431        
546A: CD 3B 3C   CALL    $3C3B           
546D: CD 9B 78   CALL    $789B           
5470: CD 91 08   CALL    $0891           
5473: CA B0 79   JP      Z,$79B0         
5476: FE 08      CP      $08             
5478: 20 06      JR      NZ,$5480        
547A: 21 B0 C3   LD      HL,$C3B0        
547D: 09         ADD     HL,BC           
547E: 34         INC     (HL)            
547F: 34         INC     (HL)            
5480: C9         RET                     
5481: 11 49 54   LD      DE,$5449        
5484: CD 3B 3C   CALL    $3C3B           
5487: F0 E7      LD      A,($E7)         
5489: 1F         RRA                     
548A: 1F         RRA                     
548B: E6 01      AND     $01             
548D: CD 87 3B   CALL    $3B87           
5490: CD 07 79   CALL    $7907           
5493: 21 50 C2   LD      HL,$C250        
5496: 09         ADD     HL,BC           
5497: 34         INC     (HL)            
5498: 7E         LD      A,(HL)          
5499: FE 10      CP      $10             
549B: 20 03      JR      NZ,$54A0        
549D: CD B0 79   CALL    $79B0           
54A0: C9         RET                     
54A1: 00         NOP                     
54A2: 00         NOP                     
54A3: 50         LD      D,B             
54A4: 00         NOP                     
54A5: 00         NOP                     
54A6: 08 52 00   LD      ($0052),SP      
54A9: 00         NOP                     
54AA: 10 52      STOP    $52             
54AC: 20 00      JR      NZ,$54AE        
54AE: 18 50      JR      $5500           
54B0: 20 10      JR      NZ,$54C2        
54B2: 00         NOP                     
54B3: 54         LD      D,H             
54B4: 00         NOP                     
54B5: 10 08      STOP    $08             
54B7: 56         LD      D,(HL)          
54B8: 00         NOP                     
54B9: 10 10      STOP    $10             
54BB: 56         LD      D,(HL)          
54BC: 20 10      JR      NZ,$54CE        
54BE: 18 54      JR      $5514           
54C0: 20 F0      JR      NZ,$54B2        
54C2: F1         POP     AF              
54C3: A7         AND     A               
54C4: 3E 00      LD      A,$00           
54C6: 28 02      JR      Z,$54CA         
54C8: 3E 08      LD      A,$08           
54CA: E0 F5      LDFF00  ($F5),A         
54CC: 21 A1 54   LD      HL,$54A1        
54CF: 0E 08      LD      C,$08           
54D1: CD 26 3D   CALL    $3D26           
54D4: CD 9B 78   CALL    $789B           
54D7: CD E2 08   CALL    $08E2           
54DA: F0 F0      LD      A,($F0)         
54DC: C7         RST     0X00            
54DD: E3                              
54DE: 54         LD      D,H             
54DF: 0B         DEC     BC              
54E0: 55         LD      D,L             
54E1: 65         LD      H,L             
54E2: 55         LD      D,L             
54E3: CD 00 78   CALL    $7800           
54E6: D0         RET     NC              
54E7: A7         AND     A               
54E8: C8         RET     Z               
54E9: CD 3B 09   CALL    $093B           
54EC: F0 9A      LD      A,($9A)         
54EE: 2F         CPL                     
54EF: 3C         INC     A               
54F0: CB 2F      SET     1,E             
54F2: CB 2F      SET     1,E             
54F4: E0 9A      LDFF00  ($9A),A         
54F6: 3E E8      LD      A,$E8           
54F8: E0 9B      LDFF00  ($9B),A         
54FA: CD 91 08   CALL    $0891           
54FD: 36 20      LD      (HL),$20        
54FF: 3E 01      LD      A,$01           
5501: CD 87 3B   CALL    $3B87           
5504: 3E 0B      LD      A,$0B           
5506: E0 F2      LDFF00  ($F2),A         
5508: C3 8D 3B   JP      $3B8D           
550B: CD 91 08   CALL    $0891           
550E: FE 01      CP      $01             
5510: 20 05      JR      NZ,$5517        
5512: 21 F2 FF   LD      HL,$FFF2        
5515: 36 08      LD      (HL),$08        
5517: A7         AND     A               
5518: C0         RET     NZ              
5519: CD 0A 79   CALL    $790A           
551C: 21 50 C2   LD      HL,$C250        
551F: 09         ADD     HL,BC           
5520: 7E         LD      A,(HL)          
5521: FE 70      CP      $70             
5523: 30 03      JR      NC,$5528        
5525: C6 03      ADD     $03             
5527: 77         LD      (HL),A          
5528: 21 10 C2   LD      HL,$C210        
552B: 09         ADD     HL,BC           
552C: 7E         LD      A,(HL)          
552D: C6 10      ADD     $10             
552F: 77         LD      (HL),A          
5530: F0 EF      LD      A,($EF)         
5532: C6 10      ADD     $10             
5534: E0 EF      LDFF00  ($EF),A         
5536: CD 9E 3B   CALL    $3B9E           
5539: 21 10 C2   LD      HL,$C210        
553C: 09         ADD     HL,BC           
553D: 7E         LD      A,(HL)          
553E: D6 10      SUB     $10             
5540: 77         LD      (HL),A          
5541: F0 EF      LD      A,($EF)         
5543: D6 10      SUB     $10             
5545: E0 EF      LDFF00  ($EF),A         
5547: 21 A0 C2   LD      HL,$C2A0        
554A: 09         ADD     HL,BC           
554B: 7E         LD      A,(HL)          
554C: A7         AND     A               
554D: 28 15      JR      Z,$5564         
554F: CD D7 08   CALL    $08D7           
5552: CD 91 08   CALL    $0891           
5555: 36 30      LD      (HL),$30        
5557: 3E 30      LD      A,$30           
5559: EA 57 C1   LD      ($C157),A       
555C: 3E 04      LD      A,$04           
555E: EA 58 C1   LD      ($C158),A       
5561: CD 8D 3B   CALL    $3B8D           
5564: C9         RET                     
5565: CD DC 57   CALL    $57DC           
5568: C9         RET                     
5569: 00         NOP                     
556A: 00         NOP                     
556B: 01 01 01   LD      BC,$0101        
556E: 02         LD      (BC),A          
556F: 02         LD      (BC),A          
5570: 02         LD      (BC),A          
5571: 00         NOP                     
5572: 00         NOP                     
5573: 0F         RRCA                    
5574: 0F         RRCA                    
5575: 0F         RRCA                    
5576: 0E 0E      LD      C,$0E           
5578: 0E 08      LD      C,$08           
557A: 08 07 07   LD      ($0707),SP      
557D: 07         RLCA                    
557E: 06 06      LD      B,$06           
5580: 06 08      LD      B,$08           
5582: 08 09 09   LD      ($0909),SP      
5585: 09         ADD     HL,BC           
5586: 0A         LD      A,(BC)          
5587: 0A         LD      A,(BC)          
5588: 0A         LD      A,(BC)          
5589: 04         INC     B               
558A: 04         INC     B               
558B: 03         INC     BC              
558C: 03         INC     BC              
558D: 03         INC     BC              
558E: 02         LD      (BC),A          
558F: 02         LD      (BC),A          
5590: 02         LD      (BC),A          
5591: 0C         INC     C               
5592: 0C         INC     C               
5593: 0D         DEC     C               
5594: 0D         DEC     C               
5595: 0D         DEC     C               
5596: 0E 0E      LD      C,$0E           
5598: 0E 04      LD      C,$04           
559A: 04         INC     B               
559B: 05         DEC     B               
559C: 05         DEC     B               
559D: 05         DEC     B               
559E: 06 06      LD      B,$06           
55A0: 06 0C      LD      B,$0C           
55A2: 0C         INC     C               
55A3: 0B         DEC     BC              
55A4: 0B         DEC     BC              
55A5: 0B         DEC     BC              
55A6: 0A         LD      A,(BC)          
55A7: 0A         LD      A,(BC)          
55A8: 0A         LD      A,(BC)          
55A9: F0 D7      LD      A,($D7)         
55AB: 07         RLCA                    
55AC: E6 01      AND     $01             
55AE: 5F         LD      E,A             
55AF: F0 D8      LD      A,($D8)         
55B1: 07         RLCA                    
55B2: 17         RLA                     
55B3: E6 02      AND     $02             
55B5: B3         OR      E               
55B6: 17         RLA                     
55B7: 17         RLA                     
55B8: 17         RLA                     
55B9: E6 18      AND     $18             
55BB: 67         LD      H,A             
55BC: F0 D8      LD      A,($D8)         
55BE: CB 7F      SET     1,E             
55C0: 28 02      JR      Z,$55C4         
55C2: 2F         CPL                     
55C3: 3C         INC     A               
55C4: 57         LD      D,A             
55C5: F0 D7      LD      A,($D7)         
55C7: CB 7F      SET     1,E             
55C9: 28 02      JR      Z,$55CD         
55CB: 2F         CPL                     
55CC: 3C         INC     A               
55CD: BA         CP      D               
55CE: 30 0D      JR      NC,$55DD        
55D0: CB 2F      SET     1,E             
55D2: CB 2F      SET     1,E             
55D4: 84         ADD     A,H             
55D5: 5F         LD      E,A             
55D6: 50         LD      D,B             
55D7: 21 69 55   LD      HL,$5569        
55DA: 19         ADD     HL,DE           
55DB: 7E         LD      A,(HL)          
55DC: C9         RET                     
55DD: 7A         LD      A,D             
55DE: CB 2F      SET     1,E             
55E0: CB 2F      SET     1,E             
55E2: 84         ADD     A,H             
55E3: 5F         LD      E,A             
55E4: 50         LD      D,B             
55E5: 21 89 55   LD      HL,$5589        
55E8: 19         ADD     HL,DE           
55E9: 7E         LD      A,(HL)          
55EA: C9         RET                     
55EB: 5A         LD      E,D             
55EC: 00         NOP                     
55ED: 5A         LD      E,D             
55EE: 20 58      JR      NZ,$5648        
55F0: 00         NOP                     
55F1: 58         LD      E,B             
55F2: 20 11      JR      NZ,$5605        
55F4: EB                              
55F5: 55         LD      D,L             
55F6: CD 3B 3C   CALL    $3C3B           
55F9: CD 9B 78   CALL    $789B           
55FC: CD E2 08   CALL    $08E2           
55FF: CD B4 3B   CALL    $3BB4           
5602: AF         XOR     A               
5603: CD 87 3B   CALL    $3B87           
5606: F0 F0      LD      A,($F0)         
5608: C7         RST     0X00            
5609: 11 56 1B   LD      DE,$1B56        
560C: 56         LD      D,(HL)          
560D: 41         LD      B,C             
560E: 56         LD      D,(HL)          
560F: 7B         LD      A,E             
5610: 56         LD      D,(HL)          
5611: F0 EC      LD      A,($EC)         
5613: 21 B0 C2   LD      HL,$C2B0        
5616: 09         ADD     HL,BC           
5617: 77         LD      (HL),A          
5618: CD 8D 3B   CALL    $3B8D           
561B: CD 91 08   CALL    $0891           
561E: C0         RET     NZ              
561F: CD 5A 79   CALL    $795A           
5622: 5F         LD      E,A             
5623: C6 28      ADD     $28             
5625: FE 50      CP      $50             
5627: 30 17      JR      NC,$5640        
5629: 3E 01      LD      A,$01           
562B: CD 87 3B   CALL    $3B87           
562E: 7B         LD      A,E             
562F: C6 18      ADD     $18             
5631: FE 30      CP      $30             
5633: 30 0B      JR      NC,$5640        
5635: CD AF 3D   CALL    $3DAF           
5638: CD 91 08   CALL    $0891           
563B: 36 08      LD      (HL),$08        
563D: CD 8D 3B   CALL    $3B8D           
5640: C9         RET                     
5641: 3E 01      LD      A,$01           
5643: CD 87 3B   CALL    $3B87           
5646: CD 91 08   CALL    $0891           
5649: FE 01      CP      $01             
564B: 20 05      JR      NZ,$5652        
564D: 21 F2 FF   LD      HL,$FFF2        
5650: 36 08      LD      (HL),$08        
5652: A7         AND     A               
5653: C0         RET     NZ              
5654: CD 0A 79   CALL    $790A           
5657: 21 50 C2   LD      HL,$C250        
565A: 09         ADD     HL,BC           
565B: 7E         LD      A,(HL)          
565C: FE 70      CP      $70             
565E: 30 03      JR      NC,$5663        
5660: C6 03      ADD     $03             
5662: 77         LD      (HL),A          
5663: CD 9E 3B   CALL    $3B9E           
5666: 21 A0 C2   LD      HL,$C2A0        
5669: 09         ADD     HL,BC           
566A: 7E         LD      A,(HL)          
566B: A7         AND     A               
566C: 28 0C      JR      Z,$567A         
566E: 3E 09      LD      A,$09           
5670: E0 F2      LDFF00  ($F2),A         
5672: CD 91 08   CALL    $0891           
5675: 36 30      LD      (HL),$30        
5677: CD 8D 3B   CALL    $3B8D           
567A: C9         RET                     
567B: CD 91 08   CALL    $0891           
567E: C0         RET     NZ              
567F: 21 B0 C2   LD      HL,$C2B0        
5682: 09         ADD     HL,BC           
5683: F0 EC      LD      A,($EC)         
5685: BE         CP      (HL)            
5686: 20 0A      JR      NZ,$5692        
5688: CD 8D 3B   CALL    $3B8D           
568B: 70         LD      (HL),B          
568C: CD 91 08   CALL    $0891           
568F: 36 20      LD      (HL),$20        
5691: C9         RET                     
5692: 21 50 C2   LD      HL,$C250        
5695: 09         ADD     HL,BC           
5696: 36 F8      LD      (HL),$F8        
5698: CD 0A 79   CALL    $790A           
569B: C9         RET                     
569C: 00         NOP                     
569D: 00         NOP                     
569E: 70         LD      (HL),B          
569F: 00         NOP                     
56A0: 00         NOP                     
56A1: 08 72 00   LD      ($0072),SP      
56A4: 00         NOP                     
56A5: 10 72      STOP    $72             
56A7: 20 00      JR      NZ,$56A9        
56A9: 18 70      JR      $571B           
56AB: 20 10      JR      NZ,$56BD        
56AD: 00         NOP                     
56AE: 74         LD      (HL),H          
56AF: 00         NOP                     
56B0: 10 08      STOP    $08             
56B2: 76         HALT                    
56B3: 00         NOP                     
56B4: 10 10      STOP    $10             
56B6: 76         HALT                    
56B7: 20 10      JR      NZ,$56C9        
56B9: 18 74      JR      $572F           
56BB: 20 FF      JR      NZ,$56BC        
56BD: 00         NOP                     
56BE: FF         RST     0X38            
56BF: 00         NOP                     
56C0: 6E         LD      L,(HL)          
56C1: 00         NOP                     
56C2: 7E         LD      A,(HL)          
56C3: 00         NOP                     
56C4: 7A         LD      A,D             
56C5: 00         NOP                     
56C6: 7A         LD      A,D             
56C7: 20 7E      JR      NZ,$5747        
56C9: 20 6E      JR      NZ,$5739        
56CB: 20 7E      JR      NZ,$574B        
56CD: 20 7C      JR      NZ,$574B        
56CF: 20 7E      JR      NZ,$574F        
56D1: 20 6C      JR      NZ,$573F        
56D3: 20 78      JR      NZ,$574D        
56D5: 00         NOP                     
56D6: 78         LD      A,B             
56D7: 20 6C      JR      NZ,$5745        
56D9: 00         NOP                     
56DA: 7E         LD      A,(HL)          
56DB: 00         NOP                     
56DC: 7C         LD      A,H             
56DD: 00         NOP                     
56DE: 7E         LD      A,(HL)          
56DF: 00         NOP                     
56E0: 04         INC     B               
56E1: 05         DEC     B               
56E2: 06 07      LD      B,$07           
56E4: 08 01 02   LD      ($0201),SP      
56E7: 03         INC     BC              
56E8: F0 EC      LD      A,($EC)         
56EA: C6 08      ADD     $08             
56EC: E0 EC      LDFF00  ($EC),A         
56EE: F0 EE      LD      A,($EE)         
56F0: C6 08      ADD     $08             
56F2: E0 EE      LDFF00  ($EE),A         
56F4: 11 BC 56   LD      DE,$56BC        
56F7: CD 3B 3C   CALL    $3C3B           
56FA: CD BA 3D   CALL    $3DBA           
56FD: 21 9C 56   LD      HL,$569C        
5700: 0E 08      LD      C,$08           
5702: CD 26 3D   CALL    $3D26           
5705: 3E 06      LD      A,$06           
5707: CD D0 3D   CALL    $3DD0           
570A: CD 9B 78   CALL    $789B           
570D: CD E2 08   CALL    $08E2           
5710: CD EB 3B   CALL    $3BEB           
5713: CD DC 57   CALL    $57DC           
5716: F0 F0      LD      A,($F0)         
5718: C7         RST     0X00            
5719: 21 57 2B   LD      HL,$2B57        
571C: 57         LD      D,A             
571D: 6E         LD      L,(HL)          
571E: 57         LD      D,A             
571F: BA         CP      D               
5720: 57         LD      D,A             
5721: F0 EC      LD      A,($EC)         
5723: 21 B0 C2   LD      HL,$C2B0        
5726: 09         ADD     HL,BC           
5727: 77         LD      (HL),A          
5728: CD 8D 3B   CALL    $3B8D           
572B: CD 91 08   CALL    $0891           
572E: C0         RET     NZ              
572F: CD 5A 79   CALL    $795A           
5732: C6 F8      ADD     $F8             
5734: 5F         LD      E,A             
5735: C6 28      ADD     $28             
5737: FE 50      CP      $50             
5739: 30 17      JR      NC,$5752        
573B: 7B         LD      A,E             
573C: C6 18      ADD     $18             
573E: FE 30      CP      $30             
5740: 30 10      JR      NC,$5752        
5742: CD AF 3D   CALL    $3DAF           
5745: 3E 08      LD      A,$08           
5747: E0 F2      LDFF00  ($F2),A         
5749: 3E 00      LD      A,$00           
574B: CD 87 3B   CALL    $3B87           
574E: CD 8D 3B   CALL    $3B8D           
5751: C9         RET                     
5752: F0 E7      LD      A,($E7)         
5754: E6 07      AND     $07             
5756: 20 15      JR      NZ,$576D        
5758: 3E 1F      LD      A,$1F           
575A: CD 30 3C   CALL    $3C30           
575D: CD A9 55   CALL    $55A9           
5760: 1F         RRA                     
5761: E6 07      AND     $07             
5763: 5F         LD      E,A             
5764: 50         LD      D,B             
5765: 21 E0 56   LD      HL,$56E0        
5768: 19         ADD     HL,DE           
5769: 7E         LD      A,(HL)          
576A: CD 87 3B   CALL    $3B87           
576D: C9         RET                     
576E: CD 0A 79   CALL    $790A           
5771: 21 50 C2   LD      HL,$C250        
5774: 09         ADD     HL,BC           
5775: 7E         LD      A,(HL)          
5776: FE 70      CP      $70             
5778: 30 03      JR      NC,$577D        
577A: C6 03      ADD     $03             
577C: 77         LD      (HL),A          
577D: 21 10 C2   LD      HL,$C210        
5780: 09         ADD     HL,BC           
5781: 7E         LD      A,(HL)          
5782: C6 10      ADD     $10             
5784: 77         LD      (HL),A          
5785: F0 EF      LD      A,($EF)         
5787: C6 10      ADD     $10             
5789: E0 EF      LDFF00  ($EF),A         
578B: CD 9E 3B   CALL    $3B9E           
578E: 21 10 C2   LD      HL,$C210        
5791: 09         ADD     HL,BC           
5792: 7E         LD      A,(HL)          
5793: D6 10      SUB     $10             
5795: 77         LD      (HL),A          
5796: F0 EF      LD      A,($EF)         
5798: D6 10      SUB     $10             
579A: E0 EF      LDFF00  ($EF),A         
579C: 21 A0 C2   LD      HL,$C2A0        
579F: 09         ADD     HL,BC           
57A0: 7E         LD      A,(HL)          
57A1: A7         AND     A               
57A2: 28 15      JR      Z,$57B9         
57A4: CD D7 08   CALL    $08D7           
57A7: CD 91 08   CALL    $0891           
57AA: 36 30      LD      (HL),$30        
57AC: 3E 30      LD      A,$30           
57AE: EA 57 C1   LD      ($C157),A       
57B1: 3E 04      LD      A,$04           
57B3: EA 58 C1   LD      ($C158),A       
57B6: CD 8D 3B   CALL    $3B8D           
57B9: C9         RET                     
57BA: CD 91 08   CALL    $0891           
57BD: C0         RET     NZ              
57BE: 21 B0 C2   LD      HL,$C2B0        
57C1: 09         ADD     HL,BC           
57C2: F0 EC      LD      A,($EC)         
57C4: BE         CP      (HL)            
57C5: 20 0B      JR      NZ,$57D2        
57C7: CD 8D 3B   CALL    $3B8D           
57CA: 36 01      LD      (HL),$01        
57CC: CD 91 08   CALL    $0891           
57CF: 36 20      LD      (HL),$20        
57D1: C9         RET                     
57D2: 21 50 C2   LD      HL,$C250        
57D5: 09         ADD     HL,BC           
57D6: 36 F8      LD      (HL),$F8        
57D8: CD 0A 79   CALL    $790A           
57DB: C9         RET                     
57DC: CD D5 3B   CALL    $3BD5           
57DF: D0         RET     NC              
57E0: CD 6A 79   CALL    $796A           
57E3: C6 08      ADD     $08             
57E5: CB 7F      SET     1,E             
57E7: 20 11      JR      NZ,$57FA        
57E9: CD 93 3B   CALL    $3B93           
57EC: 3E 10      LD      A,$10           
57EE: CD 30 3C   CALL    $3C30           
57F1: F0 D7      LD      A,($D7)         
57F3: E0 9B      LDFF00  ($9B),A         
57F5: F0 D8      LD      A,($D8)         
57F7: E0 9A      LDFF00  ($9A),A         
57F9: C9         RET                     
57FA: F0 9B      LD      A,($9B)         
57FC: E6 80      AND     $80             
57FE: 20 12      JR      NZ,$5812        
5800: 21 10 C2   LD      HL,$C210        
5803: 09         ADD     HL,BC           
5804: 7E         LD      A,(HL)          
5805: D6 10      SUB     $10             
5807: E0 99      LDFF00  ($99),A         
5809: 3E 02      LD      A,$02           
580B: E0 9B      LDFF00  ($9B),A         
580D: 3E 01      LD      A,$01           
580F: EA 47 C1   LD      ($C147),A       
5812: C9         RET                     
5813: 5E         LD      E,(HL)          
5814: 00         NOP                     
5815: 5E         LD      E,(HL)          
5816: 20 11      JR      NZ,$5829        
5818: 13         INC     DE              
5819: 58         LD      E,B             
581A: CD 3B 3C   CALL    $3C3B           
581D: CD 9B 78   CALL    $789B           
5820: F0 F0      LD      A,($F0)         
5822: C7         RST     0X00            
5823: 29         ADD     HL,HL           
5824: 58         LD      E,B             
5825: B3         OR      E               
5826: 58         LD      E,B             
5827: B3         OR      E               
5828: 58         LD      E,B             
5829: CD D5 3B   CALL    $3BD5           
582C: 30 2E      JR      NC,$585C        
582E: CD 6A 79   CALL    $796A           
5831: 5F         LD      E,A             
5832: C6 03      ADD     $03             
5834: FE 06      CP      $06             
5836: 30 03      JR      NC,$583B        
5838: CD D7 58   CALL    $58D7           
583B: F0 9B      LD      A,($9B)         
583D: E6 80      AND     $80             
583F: 20 1B      JR      NZ,$585C        
5841: CD 6A 79   CALL    $796A           
5844: C6 08      ADD     $08             
5846: CB 7F      SET     1,E             
5848: 28 12      JR      Z,$585C         
584A: 21 10 C2   LD      HL,$C210        
584D: 09         ADD     HL,BC           
584E: 7E         LD      A,(HL)          
584F: D6 10      SUB     $10             
5851: E0 99      LDFF00  ($99),A         
5853: 3E 02      LD      A,$02           
5855: E0 9B      LDFF00  ($9B),A         
5857: 3E 01      LD      A,$01           
5859: EA 47 C1   LD      ($C147),A       
585C: CD 5A 79   CALL    $795A           
585F: C6 12      ADD     $12             
5861: FE 24      CP      $24             
5863: D0         RET     NC              
5864: CD 6A 79   CALL    $796A           
5867: C6 12      ADD     $12             
5869: FE 24      CP      $24             
586B: D0         RET     NC              
586C: FA 9B C1   LD      A,($C19B)       
586F: A7         AND     A               
5870: C0         RET     NZ              
5871: FA 00 DB   LD      A,($DB00)       
5874: FE 03      CP      $03             
5876: 20 07      JR      NZ,$587F        
5878: F0 CC      LD      A,($CC)         
587A: E6 20      AND     $20             
587C: 20 0C      JR      NZ,$588A        
587E: C9         RET                     
587F: FA 01 DB   LD      A,($DB01)       
5882: FE 03      CP      $03             
5884: C0         RET     NZ              
5885: F0 CC      LD      A,($CC)         
5887: E6 10      AND     $10             
5889: C8         RET     Z               
588A: FA CF C3   LD      A,($C3CF)       
588D: A7         AND     A               
588E: C0         RET     NZ              
588F: 3C         INC     A               
5890: EA CF C3   LD      ($C3CF),A       
5893: 21 80 C2   LD      HL,$C280        
5896: 09         ADD     HL,BC           
5897: 36 07      LD      (HL),$07        
5899: 21 90 C4   LD      HL,$C490        
589C: 09         ADD     HL,BC           
589D: 70         LD      (HL),B          
589E: CD 91 08   CALL    $0891           
58A1: 36 02      LD      (HL),$02        
58A3: 21 F3 FF   LD      HL,$FFF3        
58A6: 36 02      LD      (HL),$02        
58A8: CD 8D 3B   CALL    $3B8D           
58AB: 36 02      LD      (HL),$02        
58AD: F0 9E      LD      A,($9E)         
58AF: EA 5D C1   LD      ($C15D),A       
58B2: C9         RET                     
58B3: CD 07 79   CALL    $7907           
58B6: 21 50 C2   LD      HL,$C250        
58B9: 09         ADD     HL,BC           
58BA: 7E         LD      A,(HL)          
58BB: CB 7F      SET     1,E             
58BD: 20 04      JR      NZ,$58C3        
58BF: FE 40      CP      $40             
58C1: 30 02      JR      NC,$58C5        
58C3: 34         INC     (HL)            
58C4: 34         INC     (HL)            
58C5: CD 9E 3B   CALL    $3B9E           
58C8: 21 A0 C2   LD      HL,$C2A0        
58CB: 09         ADD     HL,BC           
58CC: 7E         LD      A,(HL)          
58CD: A7         AND     A               
58CE: 28 06      JR      Z,$58D6         
58D0: CD 64 3E   CALL    $3E64           
58D3: CD B0 79   CALL    $79B0           
58D6: C9         RET                     
58D7: CD 42 09   CALL    $0942           
58DA: FA 46 C1   LD      A,($C146)       
58DD: A7         AND     A               
58DE: 20 13      JR      NZ,$58F3        
58E0: 3E 02      LD      A,$02           
58E2: EA 3E C1   LD      ($C13E),A       
58E5: CD 5A 79   CALL    $795A           
58E8: 7B         LD      A,E             
58E9: A7         AND     A               
58EA: 3E 10      LD      A,$10           
58EC: 28 02      JR      Z,$58F0         
58EE: 3E F0      LD      A,$F0           
58F0: E0 9A      LDFF00  ($9A),A         
58F2: C9         RET                     
58F3: F0 9F      LD      A,($9F)         
58F5: E0 98      LDFF00  ($98),A         
58F7: C9         RET                     
58F8: 42         LD      B,D             
58F9: 20 40      JR      NZ,$593B        
58FB: 20 46      JR      NZ,$5943        
58FD: 20 44      JR      NZ,$5943        
58FF: 20 40      JR      NZ,$5941        
5901: 00         NOP                     
5902: 42         LD      B,D             
5903: 00         NOP                     
5904: 44         LD      B,H             
5905: 00         NOP                     
5906: 46         LD      B,(HL)          
5907: 00         NOP                     
5908: 4C         LD      C,H             
5909: 00         NOP                     
590A: 4C         LD      C,H             
590B: 20 4E      JR      NZ,$595B        
590D: 00         NOP                     
590E: 4E         LD      C,(HL)          
590F: 20 48      JR      NZ,$5959        
5911: 00         NOP                     
5912: 48         LD      C,B             
5913: 20 4A      JR      NZ,$595F        
5915: 00         NOP                     
5916: 4A         LD      C,D             
5917: 20 FA      JR      NZ,$5913        
5919: 7B         LD      A,E             
591A: DB                              
591B: A7         AND     A               
591C: CA B0 79   JP      Z,$79B0         
591F: F0 F6      LD      A,($F6)         
5921: 21 E0 C3   LD      HL,$C3E0        
5924: 09         ADD     HL,BC           
5925: 77         LD      (HL),A          
5926: 21 20 C2   LD      HL,$C220        
5929: 09         ADD     HL,BC           
592A: 70         LD      (HL),B          
592B: 21 30 C2   LD      HL,$C230        
592E: 09         ADD     HL,BC           
592F: 70         LD      (HL),B          
5930: 11 F8 58   LD      DE,$58F8        
5933: CD 3B 3C   CALL    $3C3B           
5936: F0 EA      LD      A,($EA)         
5938: FE 07      CP      $07             
593A: CA 78 5A   JP      Z,$5A78         
593D: FA 1C C1   LD      A,($C11C)       
5940: FE 01      CP      $01             
5942: 20 05      JR      NZ,$5949        
5944: CD 3C 5A   CALL    $5A3C           
5947: 18 24      JR      $596D           
5949: CD 40 79   CALL    $7940           
594C: 21 20 C3   LD      HL,$C320        
594F: 09         ADD     HL,BC           
5950: 35         DEC     (HL)            
5951: 21 10 C3   LD      HL,$C310        
5954: 09         ADD     HL,BC           
5955: 7E         LD      A,(HL)          
5956: E6 80      AND     $80             
5958: 28 17      JR      Z,$5971         
595A: 70         LD      (HL),B          
595B: 21 20 C3   LD      HL,$C320        
595E: 09         ADD     HL,BC           
595F: 36 10      LD      (HL),$10        
5961: FA 46 C1   LD      A,($C146)       
5964: 5F         LD      E,A             
5965: FA 4A C1   LD      A,($C14A)       
5968: B3         OR      E               
5969: 28 02      JR      Z,$596D         
596B: 36 20      LD      (HL),$20        
596D: CD 8D 3B   CALL    $3B8D           
5970: 70         LD      (HL),B          
5971: CD 9B 78   CALL    $789B           
5974: F0 F0      LD      A,($F0)         
5976: A7         AND     A               
5977: 20 48      JR      NZ,$59C1        
5979: CD 89 79   CALL    $7989           
597C: CB 23      SET     1,E             
597E: F0 E7      LD      A,($E7)         
5980: 1F         RRA                     
5981: 1F         RRA                     
5982: 1F         RRA                     
5983: E6 01      AND     $01             
5985: 83         ADD     A,E             
5986: CD 87 3B   CALL    $3B87           
5989: CD 5A 79   CALL    $795A           
598C: C6 12      ADD     $12             
598E: FE 24      CP      $24             
5990: 30 09      JR      NC,$599B        
5992: CD 6A 79   CALL    $796A           
5995: C6 12      ADD     $12             
5997: FE 24      CP      $24             
5999: 38 40      JR      C,$59DB         
599B: F0 E7      LD      A,($E7)         
599D: E6 07      AND     $07             
599F: 20 1A      JR      NZ,$59BB        
59A1: FA 4A C1   LD      A,($C14A)       
59A4: A7         AND     A               
59A5: 3E 0C      LD      A,$0C           
59A7: 28 02      JR      Z,$59AB         
59A9: 3E 20      LD      A,$20           
59AB: 5F         LD      E,A             
59AC: 21 10 C3   LD      HL,$C310        
59AF: 09         ADD     HL,BC           
59B0: 7E         LD      A,(HL)          
59B1: F5         PUSH    AF              
59B2: E5         PUSH    HL              
59B3: 70         LD      (HL),B          
59B4: 7B         LD      A,E             
59B5: CD 25 3C   CALL    $3C25           
59B8: E1         POP     HL              
59B9: F1         POP     AF              
59BA: 77         LD      (HL),A          
59BB: CD 07 79   CALL    $7907           
59BE: C3 9E 3B   JP      $3B9E           
59C1: 21 40 C2   LD      HL,$C240        
59C4: 09         ADD     HL,BC           
59C5: 7E         LD      A,(HL)          
59C6: E6 80      AND     $80             
59C8: 28 02      JR      Z,$59CC         
59CA: 34         INC     (HL)            
59CB: 34         INC     (HL)            
59CC: 35         DEC     (HL)            
59CD: 21 50 C2   LD      HL,$C250        
59D0: 09         ADD     HL,BC           
59D1: 7E         LD      A,(HL)          
59D2: E6 80      AND     $80             
59D4: 28 02      JR      Z,$59D8         
59D6: 34         INC     (HL)            
59D7: 34         INC     (HL)            
59D8: 35         DEC     (HL)            
59D9: 18 E0      JR      $59BB           
59DB: CD AF 3D   CALL    $3DAF           
59DE: CD D5 3B   CALL    $3BD5           
59E1: D0         RET     NC              
59E2: FA 9B C1   LD      A,($C19B)       
59E5: A7         AND     A               
59E6: C0         RET     NZ              
59E7: FA 00 DB   LD      A,($DB00)       
59EA: FE 03      CP      $03             
59EC: 20 07      JR      NZ,$59F5        
59EE: F0 CC      LD      A,($CC)         
59F0: E6 20      AND     $20             
59F2: 20 0C      JR      NZ,$5A00        
59F4: C9         RET                     
59F5: FA 01 DB   LD      A,($DB01)       
59F8: FE 03      CP      $03             
59FA: C0         RET     NZ              
59FB: F0 CC      LD      A,($CC)         
59FD: E6 10      AND     $10             
59FF: C8         RET     Z               
5A00: FA 1C C1   LD      A,($C11C)       
5A03: FE 02      CP      $02             
5A05: D0         RET     NC              
5A06: FA CF C3   LD      A,($C3CF)       
5A09: A7         AND     A               
5A0A: C0         RET     NZ              
5A0B: EA 1C C1   LD      ($C11C),A       
5A0E: 3C         INC     A               
5A0F: EA CF C3   LD      ($C3CF),A       
5A12: 21 80 C2   LD      HL,$C280        
5A15: 09         ADD     HL,BC           
5A16: 36 07      LD      (HL),$07        
5A18: 21 90 C4   LD      HL,$C490        
5A1B: 09         ADD     HL,BC           
5A1C: 70         LD      (HL),B          
5A1D: CD 91 08   CALL    $0891           
5A20: 36 02      LD      (HL),$02        
5A22: 21 F3 FF   LD      HL,$FFF3        
5A25: 36 02      LD      (HL),$02        
5A27: CD 8D 3B   CALL    $3B8D           
5A2A: 36 01      LD      (HL),$01        
5A2C: 3E 02      LD      A,$02           
5A2E: E0 A2      LDFF00  ($A2),A         
5A30: EA 46 C1   LD      ($C146),A       
5A33: C9         RET                     
5A34: 06 07      LD      B,$07           
5A36: 08 09 09   LD      ($0909),SP      
5A39: 08 07 06   LD      ($0607),SP      
5A3C: 21 20 C3   LD      HL,$C320        
5A3F: 09         ADD     HL,BC           
5A40: 70         LD      (HL),B          
5A41: F0 E7      LD      A,($E7)         
5A43: 1F         RRA                     
5A44: 1F         RRA                     
5A45: 1F         RRA                     
5A46: E6 07      AND     $07             
5A48: 5F         LD      E,A             
5A49: 50         LD      D,B             
5A4A: 21 34 5A   LD      HL,$5A34        
5A4D: 19         ADD     HL,DE           
5A4E: 5E         LD      E,(HL)          
5A4F: 21 10 C3   LD      HL,$C310        
5A52: 09         ADD     HL,BC           
5A53: 7E         LD      A,(HL)          
5A54: 93         SUB     E               
5A55: C8         RET     Z               
5A56: 5F         LD      E,A             
5A57: F0 E7      LD      A,($E7)         
5A59: E6 01      AND     $01             
5A5B: C0         RET     NZ              
5A5C: 7B         LD      A,E             
5A5D: E6 80      AND     $80             
5A5F: 28 02      JR      Z,$5A63         
5A61: 34         INC     (HL)            
5A62: 34         INC     (HL)            
5A63: 35         DEC     (HL)            
5A64: C9         RET                     
5A65: 0F         RRCA                    
5A66: 00         NOP                     
5A67: 01 0F 02   LD      BC,$020F        
5A6A: 0F         RRCA                    
5A6B: 0F         RRCA                    
5A6C: 0F         RRCA                    
5A6D: 03         INC     BC              
5A6E: 0F         RRCA                    
5A6F: 0F         RRCA                    
5A70: 14         INC     D               
5A71: 14         INC     D               
5A72: 15         DEC     D               
5A73: 16 17      LD      D,$17           
5A75: 17         RLA                     
5A76: 16 15      LD      D,$15           
5A78: F0 9E      LD      A,($9E)         
5A7A: 17         RLA                     
5A7B: E6 06      AND     $06             
5A7D: 5F         LD      E,A             
5A7E: F0 E7      LD      A,($E7)         
5A80: 1F         RRA                     
5A81: 1F         RRA                     
5A82: E6 01      AND     $01             
5A84: 83         ADD     A,E             
5A85: CD 87 3B   CALL    $3B87           
5A88: 3E 02      LD      A,$02           
5A8A: EA 46 C1   LD      ($C146),A       
5A8D: AF         XOR     A               
5A8E: E0 A3      LDFF00  ($A3),A         
5A90: F0 E7      LD      A,($E7)         
5A92: E6 03      AND     $03             
5A94: 20 1B      JR      NZ,$5AB1        
5A96: F0 E7      LD      A,($E7)         
5A98: 1F         RRA                     
5A99: 1F         RRA                     
5A9A: E6 07      AND     $07             
5A9C: 5F         LD      E,A             
5A9D: 50         LD      D,B             
5A9E: 21 70 5A   LD      HL,$5A70        
5AA1: 19         ADD     HL,DE           
5AA2: 5E         LD      E,(HL)          
5AA3: 21 A2 FF   LD      HL,$FFA2        
5AA6: 7E         LD      A,(HL)          
5AA7: 93         SUB     E               
5AA8: 28 07      JR      Z,$5AB1         
5AAA: E6 80      AND     $80             
5AAC: 28 02      JR      Z,$5AB0         
5AAE: 34         INC     (HL)            
5AAF: 34         INC     (HL)            
5AB0: 35         DEC     (HL)            
5AB1: F0 CB      LD      A,($CB)         
5AB3: E6 0F      AND     $0F             
5AB5: 5F         LD      E,A             
5AB6: 50         LD      D,B             
5AB7: 21 65 5A   LD      HL,$5A65        
5ABA: 19         ADD     HL,DE           
5ABB: 7E         LD      A,(HL)          
5ABC: FE 0F      CP      $0F             
5ABE: 28 05      JR      Z,$5AC5         
5AC0: E0 9E      LDFF00  ($9E),A         
5AC2: EA 5D C1   LD      ($C15D),A       
5AC5: FA 33 C1   LD      A,($C133)       
5AC8: E6 03      AND     $03             
5ACA: 28 03      JR      Z,$5ACF         
5ACC: AF         XOR     A               
5ACD: E0 9B      LDFF00  ($9B),A         
5ACF: FA 33 C1   LD      A,($C133)       
5AD2: E6 0C      AND     $0C             
5AD4: 28 03      JR      Z,$5AD9         
5AD6: AF         XOR     A               
5AD7: E0 9A      LDFF00  ($9A),A         
5AD9: CD C5 29   CALL    $29C5           
5ADC: C9         RET                     
5ADD: 64         LD      H,H             
5ADE: 00         NOP                     
5ADF: 64         LD      H,H             
5AE0: 20 66      JR      NZ,$5B48        
5AE2: 00         NOP                     
5AE3: 66         LD      H,(HL)          
5AE4: 20 60      JR      NZ,$5B46        
5AE6: 00         NOP                     
5AE7: 60         LD      H,B             
5AE8: 20 62      JR      NZ,$5B4C        
5AEA: 00         NOP                     
5AEB: 62         LD      H,D             
5AEC: 20 68      JR      NZ,$5B56        
5AEE: 00         NOP                     
5AEF: 6A         LD      L,D             
5AF0: 00         NOP                     
5AF1: 6C         LD      L,H             
5AF2: 00         NOP                     
5AF3: 6E         LD      L,(HL)          
5AF4: 00         NOP                     
5AF5: 6A         LD      L,D             
5AF6: 20 68      JR      NZ,$5B60        
5AF8: 20 6E      JR      NZ,$5B68        
5AFA: 20 6C      JR      NZ,$5B68        
5AFC: 20 11      JR      NZ,$5B0F        
5AFE: DD                              
5AFF: 5A         LD      E,D             
5B00: CD 3B 3C   CALL    $3C3B           
5B03: CD 9B 78   CALL    $789B           
5B06: CD 07 79   CALL    $7907           
5B09: CD 40 79   CALL    $7940           
5B0C: CD 9E 3B   CALL    $3B9E           
5B0F: 21 20 C3   LD      HL,$C320        
5B12: 09         ADD     HL,BC           
5B13: 35         DEC     (HL)            
5B14: 35         DEC     (HL)            
5B15: 21 10 C3   LD      HL,$C310        
5B18: 09         ADD     HL,BC           
5B19: 7E         LD      A,(HL)          
5B1A: E6 80      AND     $80             
5B1C: E0 E8      LDFF00  ($E8),A         
5B1E: 28 06      JR      Z,$5B26         
5B20: 70         LD      (HL),B          
5B21: 21 20 C3   LD      HL,$C320        
5B24: 09         ADD     HL,BC           
5B25: 70         LD      (HL),B          
5B26: F0 F0      LD      A,($F0)         
5B28: C7         RST     0X00            
5B29: 45         LD      B,L             
5B2A: 5B         LD      E,E             
5B2B: 87         ADD     A,A             
5B2C: 5B         LD      E,E             
5B2D: 00         NOP                     
5B2E: 10 00      STOP    $00             
5B30: F0 0C      LD      A,($0C)         
5B32: 0C         INC     C               
5B33: F4                              
5B34: F4                              
5B35: F0 00      LD      A,($00)         
5B37: 10 00      STOP    $00             
5B39: F4                              
5B3A: 0C         INC     C               
5B3B: 0C         INC     C               
5B3C: F4                              
5B3D: 00         NOP                     
5B3E: 06 02      LD      B,$02           
5B40: 04         INC     B               
5B41: 00         NOP                     
5B42: 06 02      LD      B,$02           
5B44: 04         INC     B               
5B45: CD 91 08   CALL    $0891           
5B48: 20 34      JR      NZ,$5B7E        
5B4A: CD 8D 3B   CALL    $3B8D           
5B4D: CD ED 27   CALL    $27ED           
5B50: E6 1F      AND     $1F             
5B52: F6 10      OR      $10             
5B54: 21 20 C3   LD      HL,$C320        
5B57: 09         ADD     HL,BC           
5B58: 77         LD      (HL),A          
5B59: CD ED 27   CALL    $27ED           
5B5C: E6 07      AND     $07             
5B5E: 5F         LD      E,A             
5B5F: 50         LD      D,B             
5B60: 21 2D 5B   LD      HL,$5B2D        
5B63: 19         ADD     HL,DE           
5B64: 7E         LD      A,(HL)          
5B65: 21 40 C2   LD      HL,$C240        
5B68: 09         ADD     HL,BC           
5B69: 77         LD      (HL),A          
5B6A: 21 35 5B   LD      HL,$5B35        
5B6D: 19         ADD     HL,DE           
5B6E: 7E         LD      A,(HL)          
5B6F: 21 50 C2   LD      HL,$C250        
5B72: 09         ADD     HL,BC           
5B73: 77         LD      (HL),A          
5B74: 21 3D 5B   LD      HL,$5B3D        
5B77: 19         ADD     HL,DE           
5B78: 7E         LD      A,(HL)          
5B79: 21 80 C3   LD      HL,$C380        
5B7C: 09         ADD     HL,BC           
5B7D: 77         LD      (HL),A          
5B7E: 21 80 C3   LD      HL,$C380        
5B81: 09         ADD     HL,BC           
5B82: 7E         LD      A,(HL)          
5B83: CD 87 3B   CALL    $3B87           
5B86: C9         RET                     
5B87: F0 E8      LD      A,($E8)         
5B89: A7         AND     A               
5B8A: 28 13      JR      Z,$5B9F         
5B8C: CD 91 08   CALL    $0891           
5B8F: CD ED 27   CALL    $27ED           
5B92: E6 1F      AND     $1F             
5B94: C6 10      ADD     $10             
5B96: 77         LD      (HL),A          
5B97: CD AF 3D   CALL    $3DAF           
5B9A: CD 8D 3B   CALL    $3B8D           
5B9D: 70         LD      (HL),B          
5B9E: C9         RET                     
5B9F: 21 80 C3   LD      HL,$C380        
5BA2: 09         ADD     HL,BC           
5BA3: 7E         LD      A,(HL)          
5BA4: 3C         INC     A               
5BA5: CD 87 3B   CALL    $3B87           
5BA8: C9         RET                     
5BA9: 00         NOP                     
5BAA: 2C         INC     L               
5BAB: 00         NOP                     
5BAC: 00         NOP                     
5BAD: 00         NOP                     
5BAE: 00         NOP                     
5BAF: 00         NOP                     
5BB0: 00         NOP                     
5BB1: 00         NOP                     
5BB2: 00         NOP                     
5BB3: 00         NOP                     
5BB4: 00         NOP                     
5BB5: 00         NOP                     
5BB6: 00         NOP                     
5BB7: 00         NOP                     
5BB8: 00         NOP                     
5BB9: 00         NOP                     
5BBA: 00         NOP                     
5BBB: 00         NOP                     
5BBC: 00         NOP                     
5BBD: 00         NOP                     
5BBE: 00         NOP                     
5BBF: 00         NOP                     
5BC0: 00         NOP                     
5BC1: 00         NOP                     
5BC2: 00         NOP                     
5BC3: 00         NOP                     
5BC4: 00         NOP                     
5BC5: 00         NOP                     
5BC6: 00         NOP                     
5BC7: 00         NOP                     
5BC8: 00         NOP                     
5BC9: 00         NOP                     
5BCA: 00         NOP                     
5BCB: 00         NOP                     
5BCC: 00         NOP                     
5BCD: 00         NOP                     
5BCE: 00         NOP                     
5BCF: 00         NOP                     
5BD0: 00         NOP                     
5BD1: 00         NOP                     
5BD2: 00         NOP                     
5BD3: 00         NOP                     
5BD4: 00         NOP                     
5BD5: EC                              
5BD6: 00         NOP                     
5BD7: 00         NOP                     
5BD8: 00         NOP                     
5BD9: 00         NOP                     
5BDA: 00         NOP                     
5BDB: 00         NOP                     
5BDC: 00         NOP                     
5BDD: 00         NOP                     
5BDE: 00         NOP                     
5BDF: 00         NOP                     
5BE0: 00         NOP                     
5BE1: 00         NOP                     
5BE2: 00         NOP                     
5BE3: 00         NOP                     
5BE4: 00         NOP                     
5BE5: 00         NOP                     
5BE6: 00         NOP                     
5BE7: 00         NOP                     
5BE8: 00         NOP                     
5BE9: 00         NOP                     
5BEA: 00         NOP                     
5BEB: 00         NOP                     
5BEC: 00         NOP                     
5BED: 00         NOP                     
5BEE: 00         NOP                     
5BEF: 00         NOP                     
5BF0: 00         NOP                     
5BF1: 00         NOP                     
5BF2: 00         NOP                     
5BF3: 00         NOP                     
5BF4: 00         NOP                     
5BF5: 00         NOP                     
5BF6: 00         NOP                     
5BF7: 00         NOP                     
5BF8: 00         NOP                     
5BF9: 00         NOP                     
5BFA: 00         NOP                     
5BFB: 00         NOP                     
5BFC: 00         NOP                     
5BFD: 00         NOP                     
5BFE: 00         NOP                     
5BFF: 00         NOP                     
5C00: 00         NOP                     
5C01: 00         NOP                     
5C02: 00         NOP                     
5C03: 00         NOP                     
5C04: 00         NOP                     
5C05: 00         NOP                     
5C06: 00         NOP                     
5C07: 00         NOP                     
5C08: 00         NOP                     
5C09: 00         NOP                     
5C0A: 00         NOP                     
5C0B: 00         NOP                     
5C0C: 00         NOP                     
5C0D: 00         NOP                     
5C0E: 00         NOP                     
5C0F: 00         NOP                     
5C10: 00         NOP                     
5C11: 00         NOP                     
5C12: 00         NOP                     
5C13: 00         NOP                     
5C14: 00         NOP                     
5C15: 00         NOP                     
5C16: 00         NOP                     
5C17: 00         NOP                     
5C18: 00         NOP                     
5C19: 00         NOP                     
5C1A: 00         NOP                     
5C1B: 00         NOP                     
5C1C: 00         NOP                     
5C1D: 00         NOP                     
5C1E: 00         NOP                     
5C1F: 00         NOP                     
5C20: 00         NOP                     
5C21: 00         NOP                     
5C22: 00         NOP                     
5C23: 00         NOP                     
5C24: 00         NOP                     
5C25: 00         NOP                     
5C26: 00         NOP                     
5C27: 00         NOP                     
5C28: 00         NOP                     
5C29: 00         NOP                     
5C2A: 00         NOP                     
5C2B: 00         NOP                     
5C2C: 00         NOP                     
5C2D: 00         NOP                     
5C2E: 00         NOP                     
5C2F: 00         NOP                     
5C30: 00         NOP                     
5C31: 00         NOP                     
5C32: 00         NOP                     
5C33: 00         NOP                     
5C34: 00         NOP                     
5C35: 00         NOP                     
5C36: 00         NOP                     
5C37: 00         NOP                     
5C38: 00         NOP                     
5C39: 00         NOP                     
5C3A: 00         NOP                     
5C3B: 00         NOP                     
5C3C: 00         NOP                     
5C3D: 00         NOP                     
5C3E: 01 00 00   LD      BC,$0000        
5C41: 00         NOP                     
5C42: 00         NOP                     
5C43: 00         NOP                     
5C44: 00         NOP                     
5C45: 00         NOP                     
5C46: 00         NOP                     
5C47: 00         NOP                     
5C48: 00         NOP                     
5C49: 00         NOP                     
5C4A: 00         NOP                     
5C4B: 00         NOP                     
5C4C: 00         NOP                     
5C4D: 00         NOP                     
5C4E: 00         NOP                     
5C4F: 00         NOP                     
5C50: 00         NOP                     
5C51: 00         NOP                     
5C52: 00         NOP                     
5C53: 00         NOP                     
5C54: 00         NOP                     
5C55: 00         NOP                     
5C56: 00         NOP                     
5C57: 00         NOP                     
5C58: 00         NOP                     
5C59: 00         NOP                     
5C5A: 00         NOP                     
5C5B: 00         NOP                     
5C5C: 00         NOP                     
5C5D: 00         NOP                     
5C5E: 00         NOP                     
5C5F: 00         NOP                     
5C60: 00         NOP                     
5C61: 00         NOP                     
5C62: 00         NOP                     
5C63: 00         NOP                     
5C64: 00         NOP                     
5C65: 00         NOP                     
5C66: 00         NOP                     
5C67: 00         NOP                     
5C68: 00         NOP                     
5C69: 00         NOP                     
5C6A: 00         NOP                     
5C6B: 00         NOP                     
5C6C: 00         NOP                     
5C6D: 00         NOP                     
5C6E: 00         NOP                     
5C6F: 00         NOP                     
5C70: 00         NOP                     
5C71: 00         NOP                     
5C72: 00         NOP                     
5C73: 00         NOP                     
5C74: 00         NOP                     
5C75: 00         NOP                     
5C76: 00         NOP                     
5C77: 00         NOP                     
5C78: 00         NOP                     
5C79: 00         NOP                     
5C7A: 00         NOP                     
5C7B: 00         NOP                     
5C7C: 00         NOP                     
5C7D: 00         NOP                     
5C7E: 00         NOP                     
5C7F: 00         NOP                     
5C80: 00         NOP                     
5C81: 00         NOP                     
5C82: 00         NOP                     
5C83: 00         NOP                     
5C84: 00         NOP                     
5C85: 00         NOP                     
5C86: 00         NOP                     
5C87: 00         NOP                     
5C88: 00         NOP                     
5C89: 00         NOP                     
5C8A: 00         NOP                     
5C8B: 00         NOP                     
5C8C: 00         NOP                     
5C8D: 00         NOP                     
5C8E: 00         NOP                     
5C8F: 00         NOP                     
5C90: 00         NOP                     
5C91: 00         NOP                     
5C92: 00         NOP                     
5C93: 00         NOP                     
5C94: 00         NOP                     
5C95: 95         SUB     L               
5C96: 00         NOP                     
5C97: 00         NOP                     
5C98: 00         NOP                     
5C99: 00         NOP                     
5C9A: 00         NOP                     
5C9B: 00         NOP                     
5C9C: 00         NOP                     
5C9D: 00         NOP                     
5C9E: 00         NOP                     
5C9F: 00         NOP                     
5CA0: 00         NOP                     
5CA1: 00         NOP                     
5CA2: 00         NOP                     
5CA3: 00         NOP                     
5CA4: 00         NOP                     
5CA5: 00         NOP                     
5CA6: 00         NOP                     
5CA7: 00         NOP                     
5CA8: 00         NOP                     
5CA9: 3E 01      LD      A,$01           
5CAB: E0 A1      LDFF00  ($A1),A         
5CAD: EA 67 C1   LD      ($C167),A       
5CB0: CD 95 14   CALL    $1495           
5CB3: F0 9C      LD      A,($9C)         
5CB5: C7         RST     0X00            
5CB6: BC         CP      H               
5CB7: 5C         LD      E,H             
5CB8: CE 5C      ADC     $5C             
5CBA: EC                              
5CBB: 5C         LD      E,H             
5CBC: F0 B7      LD      A,($B7)         
5CBE: A7         AND     A               
5CBF: 20 08      JR      NZ,$5CC9        
5CC1: 3E 01      LD      A,$01           
5CC3: E0 9C      LDFF00  ($9C),A         
5CC5: 3E 25      LD      A,$25           
5CC7: E0 F2      LDFF00  ($F2),A         
5CC9: C9         RET                     
5CCA: 00         NOP                     
5CCB: 03         INC     BC              
5CCC: 01 02 F0   LD      BC,$F002        
5CCF: B7         OR      A               
5CD0: A7         AND     A               
5CD1: 20 05      JR      NZ,$5CD8        
5CD3: 3E 02      LD      A,$02           
5CD5: E0 9C      LDFF00  ($9C),A         
5CD7: C9         RET                     
5CD8: F0 E7      LD      A,($E7)         
5CDA: 1F         RRA                     
5CDB: 1F         RRA                     
5CDC: E6 03      AND     $03             
5CDE: 5F         LD      E,A             
5CDF: 16 00      LD      D,$00           
5CE1: 21 CA 5C   LD      HL,$5CCA        
5CE4: 19         ADD     HL,DE           
5CE5: 7E         LD      A,(HL)          
5CE6: E0 9E      LDFF00  ($9E),A         
5CE8: CD 7C 08   CALL    $087C           
5CEB: C9         RET                     
5CEC: CD D8 5C   CALL    $5CD8           
5CEF: F0 A2      LD      A,($A2)         
5CF1: C6 04      ADD     $04             
5CF3: E0 A2      LDFF00  ($A2),A         
5CF5: FE 78      CP      $78             
5CF7: 38 3E      JR      C,$5D37         
5CF9: EA C8 DB   LD      ($DBC8),A       
5CFC: F0 F6      LD      A,($F6)         
5CFE: 5F         LD      E,A             
5CFF: 16 00      LD      D,$00           
5D01: 21 A9 5B   LD      HL,$5BA9        
5D04: 19         ADD     HL,DE           
5D05: 5E         LD      E,(HL)          
5D06: 21 00 D8   LD      HL,$D800        
5D09: 19         ADD     HL,DE           
5D0A: 7E         LD      A,(HL)          
5D0B: E6 80      AND     $80             
5D0D: 28 F2      JR      Z,$5D01         
5D0F: 7B         LD      A,E             
5D10: EA 03 D4   LD      ($D403),A       
5D13: AF         XOR     A               
5D14: EA 01 D4   LD      ($D401),A       
5D17: EA 02 D4   LD      ($D402),A       
5D1A: 3E 70      LD      A,$70           
5D1C: EA 05 D4   LD      ($D405),A       
5D1F: E0 99      LDFF00  ($99),A         
5D21: 3E 68      LD      A,$68           
5D23: EA 04 D4   LD      ($D404),A       
5D26: E0 98      LDFF00  ($98),A         
5D28: EA 75 D4   LD      ($D475),A       
5D2B: 3E 66      LD      A,$66           
5D2D: EA 16 D4   LD      ($D416),A       
5D30: CD 0F 09   CALL    $090F           
5D33: AF         XOR     A               
5D34: EA 67 C1   LD      ($C167),A       
5D37: C9         RET                     
5D38: 42         LD      B,D             
5D39: 20 40      JR      NZ,$5D7B        
5D3B: 20 46      JR      NZ,$5D83        
5D3D: 20 44      JR      NZ,$5D83        
5D3F: 20 40      JR      NZ,$5D81        
5D41: 00         NOP                     
5D42: 42         LD      B,D             
5D43: 00         NOP                     
5D44: 44         LD      B,H             
5D45: 00         NOP                     
5D46: 46         LD      B,(HL)          
5D47: 00         NOP                     
5D48: 48         LD      C,B             
5D49: 00         NOP                     
5D4A: 4A         LD      C,D             
5D4B: 00         NOP                     
5D4C: 4C         LD      C,H             
5D4D: 00         NOP                     
5D4E: 4E         LD      C,(HL)          
5D4F: 00         NOP                     
5D50: 10 11      STOP    $11             
5D52: 12         LD      (DE),A          
5D53: 13         INC     DE              
5D54: 13         INC     DE              
5D55: 12         LD      (DE),A          
5D56: 11 10 FA   LD      DE,$FA10        
5D59: 79         LD      A,C             
5D5A: DB                              
5D5B: FE 01      CP      $01             
5D5D: C2 B0 79   JP      NZ,$79B0        
5D60: F0 F6      LD      A,($F6)         
5D62: 21 E0 C3   LD      HL,$C3E0        
5D65: 09         ADD     HL,BC           
5D66: 77         LD      (HL),A          
5D67: 21 20 C2   LD      HL,$C220        
5D6A: 09         ADD     HL,BC           
5D6B: 70         LD      (HL),B          
5D6C: 21 30 C2   LD      HL,$C230        
5D6F: 09         ADD     HL,BC           
5D70: 70         LD      (HL),B          
5D71: F0 E7      LD      A,($E7)         
5D73: A9         XOR     C               
5D74: E6 01      AND     $01             
5D76: 20 06      JR      NZ,$5D7E        
5D78: 11 38 5D   LD      DE,$5D38        
5D7B: CD 3B 3C   CALL    $3C3B           
5D7E: 21 C0 C2   LD      HL,$C2C0        
5D81: 09         ADD     HL,BC           
5D82: 7E         LD      A,(HL)          
5D83: A7         AND     A               
5D84: 20 15      JR      NZ,$5D9B        
5D86: F0 E7      LD      A,($E7)         
5D88: 1F         RRA                     
5D89: 1F         RRA                     
5D8A: 1F         RRA                     
5D8B: E6 07      AND     $07             
5D8D: 5F         LD      E,A             
5D8E: 50         LD      D,B             
5D8F: 21 50 5D   LD      HL,$5D50        
5D92: 19         ADD     HL,DE           
5D93: 7E         LD      A,(HL)          
5D94: D6 04      SUB     $04             
5D96: 21 10 C3   LD      HL,$C310        
5D99: 09         ADD     HL,BC           
5D9A: 77         LD      (HL),A          
5D9B: F0 F0      LD      A,($F0)         
5D9D: A7         AND     A               
5D9E: 20 4F      JR      NZ,$5DEF        
5DA0: CD 89 79   CALL    $7989           
5DA3: 7B         LD      A,E             
5DA4: FE 02      CP      $02             
5DA6: 1E 04      LD      E,$04           
5DA8: 28 05      JR      Z,$5DAF         
5DAA: CD 5A 79   CALL    $795A           
5DAD: CB 23      SET     1,E             
5DAF: F0 E7      LD      A,($E7)         
5DB1: 1F         RRA                     
5DB2: 1F         RRA                     
5DB3: 1F         RRA                     
5DB4: 1F         RRA                     
5DB5: E6 01      AND     $01             
5DB7: 83         ADD     A,E             
5DB8: CD 87 3B   CALL    $3B87           
5DBB: CD 5A 79   CALL    $795A           
5DBE: C6 18      ADD     $18             
5DC0: FE 30      CP      $30             
5DC2: 30 15      JR      NC,$5DD9        
5DC4: F0 99      LD      A,($99)         
5DC6: F5         PUSH    AF              
5DC7: C6 0C      ADD     $0C             
5DC9: E0 99      LDFF00  ($99),A         
5DCB: CD 6A 79   CALL    $796A           
5DCE: 5F         LD      E,A             
5DCF: F1         POP     AF              
5DD0: E0 99      LDFF00  ($99),A         
5DD2: 7B         LD      A,E             
5DD3: C6 18      ADD     $18             
5DD5: FE 30      CP      $30             
5DD7: 38 16      JR      C,$5DEF         
5DD9: F0 E7      LD      A,($E7)         
5DDB: E6 03      AND     $03             
5DDD: 20 0D      JR      NZ,$5DEC        
5DDF: FA 4A C1   LD      A,($C14A)       
5DE2: A7         AND     A               
5DE3: 3E 08      LD      A,$08           
5DE5: 28 02      JR      Z,$5DE9         
5DE7: 3E 18      LD      A,$18           
5DE9: CD 25 3C   CALL    $3C25           
5DEC: CD 07 79   CALL    $7907           
5DEF: FA A5 DB   LD      A,($DBA5)       
5DF2: A7         AND     A               
5DF3: C2 02 5F   JP      NZ,$5F02        
5DF6: FA 7A DB   LD      A,($DB7A)       
5DF9: A7         AND     A               
5DFA: CA A1 5E   JP      Z,$5EA1         
5DFD: F0 F6      LD      A,($F6)         
5DFF: FE 64      CP      $64             
5E01: C2 C7 5E   JP      NZ,$5EC7        
5E04: F0 F0      LD      A,($F0)         
5E06: C7         RST     0X00            
5E07: 0D         DEC     C               
5E08: 5E         LD      E,(HL)          
5E09: 20 5E      JR      NZ,$5E69        
5E0B: 7D         LD      A,L             
5E0C: 5E         LD      E,(HL)          
5E0D: CD 9B 78   CALL    $789B           
5E10: F0 98      LD      A,($98)         
5E12: FE 3C      CP      $3C             
5E14: D0         RET     NC              
5E15: F0 99      LD      A,($99)         
5E17: FE 7A      CP      $7A             
5E19: D0         RET     NC              
5E1A: EA 67 C1   LD      ($C167),A       
5E1D: C3 8D 3B   JP      $3B8D           
5E20: 3E 02      LD      A,$02           
5E22: E0 A1      LDFF00  ($A1),A         
5E24: F0 99      LD      A,($99)         
5E26: F5         PUSH    AF              
5E27: F0 98      LD      A,($98)         
5E29: F5         PUSH    AF              
5E2A: 21 10 C3   LD      HL,$C310        
5E2D: 09         ADD     HL,BC           
5E2E: 3E 60      LD      A,$60           
5E30: 96         SUB     (HL)            
5E31: E0 99      LDFF00  ($99),A         
5E33: 3E 28      LD      A,$28           
5E35: E0 98      LDFF00  ($98),A         
5E37: 3E 08      LD      A,$08           
5E39: CD 25 3C   CALL    $3C25           
5E3C: CD 5A 79   CALL    $795A           
5E3F: F5         PUSH    AF              
5E40: 7B         LD      A,E             
5E41: CB 27      SET     1,E             
5E43: 21 80 C3   LD      HL,$C380        
5E46: 09         ADD     HL,BC           
5E47: 77         LD      (HL),A          
5E48: F1         POP     AF              
5E49: C6 03      ADD     $03             
5E4B: FE 06      CP      $06             
5E4D: 30 21      JR      NC,$5E70        
5E4F: CD 6A 79   CALL    $796A           
5E52: C6 0C      ADD     $0C             
5E54: FE 18      CP      $18             
5E56: 30 18      JR      NC,$5E70        
5E58: F1         POP     AF              
5E59: E0 98      LDFF00  ($98),A         
5E5B: F1         POP     AF              
5E5C: E0 99      LDFF00  ($99),A         
5E5E: 3E 16      LD      A,$16           
5E60: CD 8E 21   CALL    $218E           
5E63: 3E 2D      LD      A,$2D           
5E65: E0 F2      LDFF00  ($F2),A         
5E67: CD 8D 3B   CALL    $3B8D           
5E6A: 21 C0 C2   LD      HL,$C2C0        
5E6D: 09         ADD     HL,BC           
5E6E: 34         INC     (HL)            
5E6F: C9         RET                     
5E70: F1         POP     AF              
5E71: E0 98      LDFF00  ($98),A         
5E73: F1         POP     AF              
5E74: E0 99      LDFF00  ($99),A         
5E76: CD 07 79   CALL    $7907           
5E79: CD 96 5F   CALL    $5F96           
5E7C: C9         RET                     
5E7D: 3E 02      LD      A,$02           
5E7F: E0 A1      LDFF00  ($A1),A         
5E81: CD 9B 78   CALL    $789B           
5E84: 21 10 C3   LD      HL,$C310        
5E87: 09         ADD     HL,BC           
5E88: 35         DEC     (HL)            
5E89: 20 12      JR      NZ,$5E9D        
5E8B: AF         XOR     A               
5E8C: EA 79 DB   LD      ($DB79),A       
5E8F: EA 7A DB   LD      ($DB7A),A       
5E92: EA 67 C1   LD      ($C167),A       
5E95: 21 E3 D9   LD      HL,$D9E3        
5E98: CB F6      SET     1,E             
5E9A: C3 B0 79   JP      $79B0           
5E9D: CD 96 5F   CALL    $5F96           
5EA0: C9         RET                     
5EA1: CD 9B 78   CALL    $789B           
5EA4: 21 D0 C2   LD      HL,$C2D0        
5EA7: 09         ADD     HL,BC           
5EA8: 7E         LD      A,(HL)          
5EA9: A7         AND     A               
5EAA: C0         RET     NZ              
5EAB: F0 F6      LD      A,($F6)         
5EAD: FE F6      CP      $F6             
5EAF: C2 C7 5E   JP      NZ,$5EC7        
5EB2: F0 99      LD      A,($99)         
5EB4: FE 40      CP      $40             
5EB6: D8         RET     C               
5EB7: F0 98      LD      A,($98)         
5EB9: FE 78      CP      $78             
5EBB: D0         RET     NC              
5EBC: 34         INC     (HL)            
5EBD: 3E 2D      LD      A,$2D           
5EBF: E0 F2      LDFF00  ($F2),A         
5EC1: 3E 13      LD      A,$13           
5EC3: CD 8E 21   CALL    $218E           
5EC6: C9         RET                     
5EC7: CD 9B 78   CALL    $789B           
5ECA: 21 D0 C2   LD      HL,$C2D0        
5ECD: 09         ADD     HL,BC           
5ECE: 7E         LD      A,(HL)          
5ECF: A7         AND     A               
5ED0: C0         RET     NZ              
5ED1: FA 6B C1   LD      A,($C16B)       
5ED4: FE 04      CP      $04             
5ED6: C0         RET     NZ              
5ED7: F0 E7      LD      A,($E7)         
5ED9: E6 01      AND     $01             
5EDB: C0         RET     NZ              
5EDC: 21 40 C4   LD      HL,$C440        
5EDF: 09         ADD     HL,BC           
5EE0: 35         DEC     (HL)            
5EE1: C0         RET     NZ              
5EE2: CD ED 27   CALL    $27ED           
5EE5: E6 03      AND     $03             
5EE7: 21 C8 C3   LD      HL,$C3C8        
5EEA: B6         OR      (HL)            
5EEB: C0         RET     NZ              
5EEC: 21 D0 C2   LD      HL,$C2D0        
5EEF: 09         ADD     HL,BC           
5EF0: 34         INC     (HL)            
5EF1: 3E 2D      LD      A,$2D           
5EF3: E0 F2      LDFF00  ($F2),A         
5EF5: FA 7A DB   LD      A,($DB7A)       
5EF8: A7         AND     A               
5EF9: 3E 11      LD      A,$11           
5EFB: 28 02      JR      Z,$5EFF         
5EFD: 3E 10      LD      A,$10           
5EFF: C3 8E 21   JP      $218E           
5F02: CD 9B 78   CALL    $789B           
5F05: F0 F7      LD      A,($F7)         
5F07: FE 1E      CP      $1E             
5F09: C0         RET     NZ              
5F0A: F0 F6      LD      A,($F6)         
5F0C: FE E3      CP      $E3             
5F0E: C0         RET     NZ              
5F0F: F0 F8      LD      A,($F8)         
5F11: E6 20      AND     $20             
5F13: C0         RET     NZ              
5F14: 3E 02      LD      A,$02           
5F16: E0 A1      LDFF00  ($A1),A         
5F18: EA 67 C1   LD      ($C167),A       
5F1B: F0 F0      LD      A,($F0)         
5F1D: C7         RST     0X00            
5F1E: 2A         LD      A,(HLI)         
5F1F: 5F         LD      E,A             
5F20: 42         LD      B,D             
5F21: 5F         LD      E,A             
5F22: 7A         LD      A,D             
5F23: 5F         LD      E,A             
5F24: A8         XOR     B               
5F25: 5F         LD      E,A             
5F26: C4 5F EA   CALL    NZ,$EA5F        
5F29: 5F         LD      E,A             
5F2A: CD 91 08   CALL    $0891           
5F2D: 36 40      LD      (HL),$40        
5F2F: C3 8D 3B   JP      $3B8D           
5F32: 60         LD      H,B             
5F33: 28 28      JR      Z,$5F5D         
5F35: 68         LD      L,B             
5F36: 00         NOP                     
5F37: F8 FC      LDHL    SP,$FC          
5F39: 08 F8 FC   LD      ($FCF8),SP      
5F3C: F8 02      LDHL    SP,$02          
5F3E: 04         INC     B               
5F3F: 02         LD      (BC),A          
5F40: 04         INC     B               
5F41: 00         NOP                     
5F42: CD 91 08   CALL    $0891           
5F45: 20 31      JR      NZ,$5F78        
5F47: 21 D0 C3   LD      HL,$C3D0        
5F4A: 09         ADD     HL,BC           
5F4B: 5E         LD      E,(HL)          
5F4C: 50         LD      D,B             
5F4D: 21 32 5F   LD      HL,$5F32        
5F50: 19         ADD     HL,DE           
5F51: 7E         LD      A,(HL)          
5F52: 21 E0 C2   LD      HL,$C2E0        
5F55: 09         ADD     HL,BC           
5F56: 77         LD      (HL),A          
5F57: 21 36 5F   LD      HL,$5F36        
5F5A: 19         ADD     HL,DE           
5F5B: 7E         LD      A,(HL)          
5F5C: 21 40 C2   LD      HL,$C240        
5F5F: 09         ADD     HL,BC           
5F60: 77         LD      (HL),A          
5F61: 21 3A 5F   LD      HL,$5F3A        
5F64: 19         ADD     HL,DE           
5F65: 7E         LD      A,(HL)          
5F66: 21 50 C2   LD      HL,$C250        
5F69: 09         ADD     HL,BC           
5F6A: 77         LD      (HL),A          
5F6B: 21 3E 5F   LD      HL,$5F3E        
5F6E: 19         ADD     HL,DE           
5F6F: 7E         LD      A,(HL)          
5F70: 21 80 C3   LD      HL,$C380        
5F73: 09         ADD     HL,BC           
5F74: 77         LD      (HL),A          
5F75: CD 8D 3B   CALL    $3B8D           
5F78: 18 1C      JR      $5F96           
5F7A: CD 91 08   CALL    $0891           
5F7D: 20 14      JR      NZ,$5F93        
5F7F: 36 50      LD      (HL),$50        
5F81: CD 8D 3B   CALL    $3B8D           
5F84: 21 D0 C3   LD      HL,$C3D0        
5F87: 09         ADD     HL,BC           
5F88: 7E         LD      A,(HL)          
5F89: 3C         INC     A               
5F8A: 77         LD      (HL),A          
5F8B: FE 04      CP      $04             
5F8D: 28 04      JR      Z,$5F93         
5F8F: CD 8D 3B   CALL    $3B8D           
5F92: 70         LD      (HL),B          
5F93: CD 07 79   CALL    $7907           
5F96: 21 80 C3   LD      HL,$C380        
5F99: 09         ADD     HL,BC           
5F9A: 5E         LD      E,(HL)          
5F9B: F0 E7      LD      A,($E7)         
5F9D: 1F         RRA                     
5F9E: 1F         RRA                     
5F9F: 1F         RRA                     
5FA0: 1F         RRA                     
5FA1: E6 01      AND     $01             
5FA3: 83         ADD     A,E             
5FA4: CD 87 3B   CALL    $3B87           
5FA7: C9         RET                     
5FA8: CD 91 08   CALL    $0891           
5FAB: 20 14      JR      NZ,$5FC1        
5FAD: 36 50      LD      (HL),$50        
5FAF: F0 99      LD      A,($99)         
5FB1: F5         PUSH    AF              
5FB2: 3E 10      LD      A,$10           
5FB4: E0 99      LDFF00  ($99),A         
5FB6: 3E 14      LD      A,$14           
5FB8: CD 8E 21   CALL    $218E           
5FBB: F1         POP     AF              
5FBC: E0 99      LDFF00  ($99),A         
5FBE: CD 8D 3B   CALL    $3B8D           
5FC1: C3 96 5F   JP      $5F96           
5FC4: CD 91 08   CALL    $0891           
5FC7: 20 08      JR      NZ,$5FD1        
5FC9: 3E 15      LD      A,$15           
5FCB: CD 8E 21   CALL    $218E           
5FCE: CD 8D 3B   CALL    $3B8D           
5FD1: 21 50 C2   LD      HL,$C250        
5FD4: 09         ADD     HL,BC           
5FD5: 36 0A      LD      (HL),$0A        
5FD7: 21 40 C2   LD      HL,$C240        
5FDA: 09         ADD     HL,BC           
5FDB: 36 FC      LD      (HL),$FC        
5FDD: 21 80 C3   LD      HL,$C380        
5FE0: 09         ADD     HL,BC           
5FE1: 36 02      LD      (HL),$02        
5FE3: CD 07 79   CALL    $7907           
5FE6: C3 96 5F   JP      $5F96           
5FE9: C9         RET                     
5FEA: 3E 01      LD      A,$01           
5FEC: EA 7A DB   LD      ($DB7A),A       
5FEF: CD 62 7A   CALL    $7A62           
5FF2: CD B0 79   CALL    $79B0           
5FF5: C3 09 09   JP      $0909           
5FF8: 00         NOP                     
5FF9: 98         SBC     B               
5FFA: 06 89      LD      B,$89           
5FFC: 00         NOP                     
5FFD: 04         INC     B               
5FFE: 00         NOP                     
5FFF: 04         INC     B               
6000: 00         NOP                     
6001: 04         INC     B               
6002: 00         NOP                     
6003: 04         INC     B               
6004: 00         NOP                     
6005: 10 98      STOP    $98             
6007: 07         RLCA                    
6008: 89         ADC     A,C             
6009: 01 11 01   LD      BC,$0111        
600C: 11 01 11   LD      DE,$1101        
600F: 01 11 01   LD      BC,$0111        
6012: 11 98 08   LD      DE,$0898        
6015: 89         ADC     A,C             
6016: 07         RLCA                    
6017: 06 07      LD      B,$07           
6019: 06 07      LD      B,$07           
601B: 06 07      LD      B,$07           
601D: 06 07      LD      B,$07           
601F: 06 98      LD      B,$98           
6021: 08 89 07   LD      ($0789),SP      
6024: 06 07      LD      B,$07           
6026: 06 07      LD      B,$07           
6028: 06 07      LD      B,$07           
602A: 06 07      LD      B,$07           
602C: 06 98      LD      B,$98           
602E: 09         ADD     HL,BC           
602F: 89         ADC     A,C             
6030: 06 07      LD      B,$07           
6032: 06 07      LD      B,$07           
6034: 06 07      LD      B,$07           
6036: 06 07      LD      B,$07           
6038: 06 07      LD      B,$07           
603A: 98         SBC     B               
603B: 0A         LD      A,(BC)          
603C: 89         ADC     A,C             
603D: 07         RLCA                    
603E: 06 07      LD      B,$07           
6040: 06 07      LD      B,$07           
6042: 06 07      LD      B,$07           
6044: 06 07      LD      B,$07           
6046: 06 98      LD      B,$98           
6048: 0B         DEC     BC              
6049: 89         ADC     A,C             
604A: 06 07      LD      B,$07           
604C: 06 07      LD      B,$07           
604E: 06 07      LD      B,$07           
6050: 06 07      LD      B,$07           
6052: 06 07      LD      B,$07           
6054: 98         SBC     B               
6055: 0B         DEC     BC              
6056: 89         ADC     A,C             
6057: 06 07      LD      B,$07           
6059: 06 07      LD      B,$07           
605B: 06 07      LD      B,$07           
605D: 06 07      LD      B,$07           
605F: 06 07      LD      B,$07           
6061: 98         SBC     B               
6062: 0C         INC     C               
6063: 89         ADC     A,C             
6064: 07         RLCA                    
6065: 06 07      LD      B,$07           
6067: 06 07      LD      B,$07           
6069: 06 07      LD      B,$07           
606B: 06 07      LD      B,$07           
606D: 06 98      LD      B,$98           
606F: 0D         DEC     C               
6070: 89         ADC     A,C             
6071: 06 07      LD      B,$07           
6073: 06 07      LD      B,$07           
6075: 06 07      LD      B,$07           
6077: 06 07      LD      B,$07           
6079: 06 07      LD      B,$07           
607B: 98         SBC     B               
607C: 0E 89      LD      C,$89           
607E: 02         LD      (BC),A          
607F: 12         LD      (DE),A          
6080: 02         LD      (BC),A          
6081: 12         LD      (DE),A          
6082: 02         LD      (BC),A          
6083: 12         LD      (DE),A          
6084: 02         LD      (BC),A          
6085: 12         LD      (DE),A          
6086: 02         LD      (BC),A          
6087: 12         LD      (DE),A          
6088: 98         SBC     B               
6089: 0F         RRCA                    
608A: 89         ADC     A,C             
608B: 03         INC     BC              
608C: 05         DEC     B               
608D: 03         INC     BC              
608E: 05         DEC     B               
608F: 03         INC     BC              
6090: 05         DEC     B               
6091: 03         INC     BC              
6092: 05         DEC     B               
6093: 03         INC     BC              
6094: 13         INC     DE              
6095: 98         SBC     B               
6096: 06 89      LD      B,$89           
6098: 04         INC     B               
6099: 00         NOP                     
609A: 04         INC     B               
609B: 00         NOP                     
609C: 04         INC     B               
609D: 00         NOP                     
609E: 04         INC     B               
609F: 00         NOP                     
60A0: 04         INC     B               
60A1: 14         INC     D               
60A2: 98         SBC     B               
60A3: 07         RLCA                    
60A4: 89         ADC     A,C             
60A5: 11 01 11   LD      DE,$1101        
60A8: 01 11 01   LD      BC,$0111        
60AB: 11 01 11   LD      DE,$1101        
60AE: 01 98 08   LD      BC,$0898        
60B1: 89         ADC     A,C             
60B2: 06 07      LD      B,$07           
60B4: 06 07      LD      B,$07           
60B6: 06 07      LD      B,$07           
60B8: 06 07      LD      B,$07           
60BA: 06 07      LD      B,$07           
60BC: 98         SBC     B               
60BD: 08 89 06   LD      ($0689),SP      
60C0: 07         RLCA                    
60C1: 06 07      LD      B,$07           
60C3: 06 07      LD      B,$07           
60C5: 06 07      LD      B,$07           
60C7: 06 07      LD      B,$07           
60C9: 98         SBC     B               
60CA: 09         ADD     HL,BC           
60CB: 89         ADC     A,C             
60CC: 07         RLCA                    
60CD: 06 07      LD      B,$07           
60CF: 06 07      LD      B,$07           
60D1: 06 07      LD      B,$07           
60D3: 06 07      LD      B,$07           
60D5: 06 98      LD      B,$98           
60D7: 0A         LD      A,(BC)          
60D8: 89         ADC     A,C             
60D9: 06 07      LD      B,$07           
60DB: 06 07      LD      B,$07           
60DD: 06 07      LD      B,$07           
60DF: 06 07      LD      B,$07           
60E1: 06 07      LD      B,$07           
60E3: 98         SBC     B               
60E4: 0B         DEC     BC              
60E5: 89         ADC     A,C             
60E6: 07         RLCA                    
60E7: 06 07      LD      B,$07           
60E9: 06 07      LD      B,$07           
60EB: 06 07      LD      B,$07           
60ED: 06 07      LD      B,$07           
60EF: 06 98      LD      B,$98           
60F1: 0B         DEC     BC              
60F2: 89         ADC     A,C             
60F3: 07         RLCA                    
60F4: 06 07      LD      B,$07           
60F6: 06 07      LD      B,$07           
60F8: 06 07      LD      B,$07           
60FA: 06 07      LD      B,$07           
60FC: 06 98      LD      B,$98           
60FE: 0C         INC     C               
60FF: 89         ADC     A,C             
6100: 06 07      LD      B,$07           
6102: 06 07      LD      B,$07           
6104: 06 07      LD      B,$07           
6106: 06 07      LD      B,$07           
6108: 06 07      LD      B,$07           
610A: 98         SBC     B               
610B: 0D         DEC     C               
610C: 89         ADC     A,C             
610D: 07         RLCA                    
610E: 06 07      LD      B,$07           
6110: 06 07      LD      B,$07           
6112: 06 07      LD      B,$07           
6114: 06 07      LD      B,$07           
6116: 06 98      LD      B,$98           
6118: 0E 89      LD      C,$89           
611A: 12         LD      (DE),A          
611B: 02         LD      (BC),A          
611C: 12         LD      (DE),A          
611D: 02         LD      (BC),A          
611E: 12         LD      (DE),A          
611F: 02         LD      (BC),A          
6120: 12         LD      (DE),A          
6121: 02         LD      (BC),A          
6122: 12         LD      (DE),A          
6123: 02         LD      (BC),A          
6124: 98         SBC     B               
6125: 0F         RRCA                    
6126: 89         ADC     A,C             
6127: 05         DEC     B               
6128: 03         INC     BC              
6129: 05         DEC     B               
612A: 03         INC     BC              
612B: 05         DEC     B               
612C: 03         INC     BC              
612D: 05         DEC     B               
612E: 03         INC     BC              
612F: 05         DEC     B               
6130: 15         DEC     D               
6131: 95         SUB     L               
6132: 60         LD      H,B             
6133: F9         LD      SP,HL           
6134: 5F         LD      E,A             
6135: C9         RET                     
6136: 60         LD      H,B             
6137: 2D         DEC     L               
6138: 60         LD      H,B             
6139: FD                              
613A: 60         LD      H,B             
613B: 61         LD      H,C             
613C: 60         LD      H,B             
613D: 3E 02      LD      A,$02           
613F: E0 A1      LDFF00  ($A1),A         
6141: EA 67 C1   LD      ($C167),A       
6144: CD BE 63   CALL    $63BE           
6147: F0 F0      LD      A,($F0)         
6149: C7         RST     0X00            
614A: 58         LD      E,B             
614B: 61         LD      H,C             
614C: 63         LD      H,E             
614D: 61         LD      H,C             
614E: 99         SBC     C               
614F: 61         LD      H,C             
6150: A3         AND     E               
6151: 61         LD      H,C             
6152: A8         XOR     B               
6153: 61         LD      H,C             
6154: DD                              
6155: 61         LD      H,C             
6156: 04         INC     B               
6157: 62         LD      H,D             
6158: CD D2 27   CALL    $27D2           
615B: CD 91 08   CALL    $0891           
615E: 36 FF      LD      (HL),$FF        
6160: CD 8D 3B   CALL    $3B8D           
6163: CD 91 08   CALL    $0891           
6166: 20 0E      JR      NZ,$6176        
6168: EA 55 C1   LD      ($C155),A       
616B: CD 87 3B   CALL    $3B87           
616E: 3E 2E      LD      A,$2E           
6170: E0 F2      LDFF00  ($F2),A         
6172: CD 8D 3B   CALL    $3B8D           
6175: C9         RET                     
6176: FE A0      CP      $A0             
6178: 20 04      JR      NZ,$617E        
617A: 3E 1D      LD      A,$1D           
617C: E0 F4      LDFF00  ($F4),A         
617E: 38 0C      JR      C,$618C         
6180: E6 10      AND     $10             
6182: 3E 00      LD      A,$00           
6184: 28 02      JR      Z,$6188         
6186: 3E FF      LD      A,$FF           
6188: CD 87 3B   CALL    $3B87           
618B: C9         RET                     
618C: 1E 01      LD      E,$01           
618E: E6 04      AND     $04             
6190: 28 02      JR      Z,$6194         
6192: 1E FE      LD      E,$FE           
6194: 7B         LD      A,E             
6195: EA 55 C1   LD      ($C155),A       
6198: C9         RET                     
6199: CD 91 08   CALL    $0891           
619C: A7         AND     A               
619D: 20 03      JR      NZ,$61A2        
619F: CD 8D 3B   CALL    $3B8D           
61A2: C9         RET                     
61A3: 21 31 61   LD      HL,$6131        
61A6: 18 03      JR      $61AB           
61A8: 21 35 61   LD      HL,$6135        
61AB: C5         PUSH    BC              
61AC: E5         PUSH    HL              
61AD: 21 B0 C2   LD      HL,$C2B0        
61B0: 09         ADD     HL,BC           
61B1: 7E         LD      A,(HL)          
61B2: 17         RLA                     
61B3: E6 02      AND     $02             
61B5: 5F         LD      E,A             
61B6: 50         LD      D,B             
61B7: E1         POP     HL              
61B8: 19         ADD     HL,DE           
61B9: 2A         LD      A,(HLI)         
61BA: 56         LD      D,(HL)          
61BB: 5F         LD      E,A             
61BC: 0E 34      LD      C,$34           
61BE: 21 01 D6   LD      HL,$D601        
61C1: 1B         DEC     DE              
61C2: 1A         LD      A,(DE)          
61C3: 13         INC     DE              
61C4: FE 98      CP      $98             
61C6: 1A         LD      A,(DE)          
61C7: 20 08      JR      NZ,$61D1        
61C9: F0 96      LD      A,($96)         
61CB: A7         AND     A               
61CC: 1A         LD      A,(DE)          
61CD: 28 02      JR      Z,$61D1         
61CF: C6 0C      ADD     $0C             
61D1: 13         INC     DE              
61D2: 22         LD      (HLI),A         
61D3: 0D         DEC     C               
61D4: 20 EB      JR      NZ,$61C1        
61D6: 36 00      LD      (HL),$00        
61D8: C1         POP     BC              
61D9: CD 8D 3B   CALL    $3B8D           
61DC: C9         RET                     
61DD: 21 39 61   LD      HL,$6139        
61E0: CD AB 61   CALL    $61AB           
61E3: CD 91 08   CALL    $0891           
61E6: 36 18      LD      (HL),$18        
61E8: 21 B0 C2   LD      HL,$C2B0        
61EB: 09         ADD     HL,BC           
61EC: 34         INC     (HL)            
61ED: 21 D0 C3   LD      HL,$C3D0        
61F0: 09         ADD     HL,BC           
61F1: 7E         LD      A,(HL)          
61F2: 3C         INC     A               
61F3: 77         LD      (HL),A          
61F4: FE 0C      CP      $0C             
61F6: 20 06      JR      NZ,$61FE        
61F8: F0 BF      LD      A,($BF)         
61FA: EA 68 D3   LD      ($D368),A       
61FD: C9         RET                     
61FE: CD 8D 3B   CALL    $3B8D           
6201: 36 02      LD      (HL),$02        
6203: C9         RET                     
6204: CD 62 7A   CALL    $7A62           
6207: CB E6      SET     1,E             
6209: AF         XOR     A               
620A: EA 55 C1   LD      ($C155),A       
620D: EA 67 C1   LD      ($C167),A       
6210: 3E 02      LD      A,$02           
6212: E0 F2      LDFF00  ($F2),A         
6214: 3E E1      LD      A,$E1           
6216: EA 36 D7   LD      ($D736),A       
6219: 3E 77      LD      A,$77           
621B: EA 46 D7   LD      ($D746),A       
621E: 3E 77      LD      A,$77           
6220: EA 56 D7   LD      ($D756),A       
6223: CD 69 62   CALL    $6269           
6226: C3 B0 79   JP      $79B0           
6229: 98         SBC     B               
622A: 4A         LD      C,D             
622B: 87         ADD     A,A             
622C: 0C         INC     C               
622D: 1C         INC     E               
622E: 64         LD      H,H             
622F: 66         LD      H,(HL)          
6230: 0F         RRCA                    
6231: 0F         RRCA                    
6232: 0F         RRCA                    
6233: 0F         RRCA                    
6234: 98         SBC     B               
6235: 4B         LD      C,E             
6236: 87         ADD     A,A             
6237: 0D         DEC     C               
6238: 1D         DEC     E               
6239: 65         LD      H,L             
623A: 67         LD      H,A             
623B: 1F         RRA                     
623C: 1F         RRA                     
623D: 1F         RRA                     
623E: 1F         RRA                     
623F: 98         SBC     B               
6240: 49         LD      C,C             
6241: 81         ADD     A,C             
6242: 0B         DEC     BC              
6243: 1B         DEC     DE              
6244: 98         SBC     B               
6245: 4C         LD      C,H             
6246: 81         ADD     A,C             
6247: 0E 1E      LD      C,$1E           
6249: 98         SBC     B               
624A: 56         LD      D,(HL)          
624B: 87         ADD     A,A             
624C: 0C         INC     C               
624D: 1C         INC     E               
624E: 64         LD      H,H             
624F: 66         LD      H,(HL)          
6250: 0F         RRCA                    
6251: 0F         RRCA                    
6252: 0F         RRCA                    
6253: 0F         RRCA                    
6254: 98         SBC     B               
6255: 57         LD      D,A             
6256: 87         ADD     A,A             
6257: 0D         DEC     C               
6258: 1D         DEC     E               
6259: 65         LD      H,L             
625A: 67         LD      H,A             
625B: 1F         RRA                     
625C: 1F         RRA                     
625D: 1F         RRA                     
625E: 1F         RRA                     
625F: 98         SBC     B               
6260: 55         LD      D,L             
6261: 81         ADD     A,C             
6262: 0B         DEC     BC              
6263: 1B         DEC     DE              
6264: 98         SBC     B               
6265: 58         LD      E,B             
6266: 81         ADD     A,C             
6267: 0E 1E      LD      C,$1E           
6269: 3E 20      LD      A,$20           
626B: EA 00 D6   LD      ($D600),A       
626E: 21 01 D6   LD      HL,$D601        
6271: 11 29 62   LD      DE,$6229        
6274: F0 96      LD      A,($96)         
6276: A7         AND     A               
6277: 28 03      JR      Z,$627C         
6279: 11 49 62   LD      DE,$6249        
627C: C5         PUSH    BC              
627D: 0E 20      LD      C,$20           
627F: 1A         LD      A,(DE)          
6280: 13         INC     DE              
6281: 22         LD      (HLI),A         
6282: 0D         DEC     C               
6283: 20 FA      JR      NZ,$627F        
6285: C1         POP     BC              
6286: 70         LD      (HL),B          
6287: C9         RET                     
6288: 50         LD      D,B             
6289: 5C         LD      E,H             
628A: 68         LD      L,B             
628B: 70         LD      (HL),B          
628C: 7A         LD      A,D             
628D: 7E         LD      A,(HL)          
628E: 58         LD      E,B             
628F: 32         LD      (HLD),A         
6290: 38 38      JR      C,$62CA         
6292: 40         LD      B,B             
6293: 44         LD      B,H             
6294: 50         LD      D,B             
6295: 20 20      JR      NZ,$62B7        
6297: 20 20      JR      NZ,$62B9        
6299: 20 1F      JR      NZ,$62BA        
629B: 1E 1F      LD      E,$1F           
629D: 20 20      JR      NZ,$62BF        
629F: 20 20      JR      NZ,$62C1        
62A1: 20 03      JR      NZ,$62A6        
62A3: 03         INC     BC              
62A4: 04         INC     B               
62A5: 04         INC     B               
62A6: 05         DEC     B               
62A7: 05         DEC     B               
62A8: 06 01      LD      B,$01           
62AA: 01 02 02   LD      BC,$0202        
62AD: 03         INC     BC              
62AE: 03         INC     BC              
62AF: C0         RET     NZ              
62B0: C0         RET     NZ              
62B1: C0         RET     NZ              
62B2: C0         RET     NZ              
62B3: C0         RET     NZ              
62B4: C0         RET     NZ              
62B5: C0         RET     NZ              
62B6: 38 3A      JR      C,$62F2         
62B8: 3B         DEC     SP              
62B9: 44         LD      B,H             
62BA: 4C         LD      C,H             
62BB: 58         LD      E,B             
62BC: FF         RST     0X38            
62BD: FF         RST     0X38            
62BE: FF         RST     0X38            
62BF: FF         RST     0X38            
62C0: FF         RST     0X38            
62C1: FF         RST     0X38            
62C2: FF         RST     0X38            
62C3: 2F         CPL                     
62C4: 30 30      JR      NC,$62F6        
62C6: 30 30      JR      NC,$62F8        
62C8: 30 00      JR      NC,$62CA        
62CA: 00         NOP                     
62CB: 00         NOP                     
62CC: 00         NOP                     
62CD: 00         NOP                     
62CE: 00         NOP                     
62CF: 00         NOP                     
62D0: 00         NOP                     
62D1: 01 02 03   LD      BC,$0302        
62D4: 04         INC     B               
62D5: 04         INC     B               
62D6: 00         NOP                     
62D7: 00         NOP                     
62D8: 70         LD      (HL),B          
62D9: 00         NOP                     
62DA: 00         NOP                     
62DB: 00         NOP                     
62DC: FF         RST     0X38            
62DD: 00         NOP                     
62DE: 00         NOP                     
62DF: 00         NOP                     
62E0: FF         RST     0X38            
62E1: 00         NOP                     
62E2: 00         NOP                     
62E3: 00         NOP                     
62E4: FF         RST     0X38            
62E5: 00         NOP                     
62E6: 00         NOP                     
62E7: 00         NOP                     
62E8: 72         LD      (HL),D          
62E9: 00         NOP                     
62EA: 00         NOP                     
62EB: 08 74 00   LD      ($0074),SP      
62EE: 00         NOP                     
62EF: 00         NOP                     
62F0: FF         RST     0X38            
62F1: 00         NOP                     
62F2: 00         NOP                     
62F3: 00         NOP                     
62F4: FF         RST     0X38            
62F5: 00         NOP                     
62F6: 00         NOP                     
62F7: 00         NOP                     
62F8: 76         HALT                    
62F9: 00         NOP                     
62FA: 00         NOP                     
62FB: 08 78 00   LD      ($0078),SP      
62FE: 00         NOP                     
62FF: 10 7A      STOP    $7A             
6301: 00         NOP                     
6302: 00         NOP                     
6303: 00         NOP                     
6304: FF         RST     0X38            
6305: 00         NOP                     
6306: 00         NOP                     
6307: 00         NOP                     
6308: 7C         LD      A,H             
6309: 00         NOP                     
630A: 00         NOP                     
630B: 08 7E 00   LD      ($007E),SP      
630E: 00         NOP                     
630F: 10 7E      STOP    $7E             
6311: 20 00      JR      NZ,$6313        
6313: 18 7C      JR      $6391           
6315: 20 00      JR      NZ,$6317        
6317: 00         NOP                     
6318: 7A         LD      A,D             
6319: 20 00      JR      NZ,$631B        
631B: 08 78 20   LD      ($2078),SP      
631E: 00         NOP                     
631F: 10 76      STOP    $76             
6321: 20 00      JR      NZ,$6323        
6323: 00         NOP                     
6324: FF         RST     0X38            
6325: 00         NOP                     
6326: 00         NOP                     
6327: 00         NOP                     
6328: 74         LD      (HL),H          
6329: 20 00      JR      NZ,$632B        
632B: 08 72 20   LD      ($2072),SP      
632E: 00         NOP                     
632F: 00         NOP                     
6330: FF         RST     0X38            
6331: 00         NOP                     
6332: 00         NOP                     
6333: 00         NOP                     
6334: FF         RST     0X38            
6335: 00         NOP                     
6336: 00         NOP                     
6337: 30 70      JR      NC,$63A9        
6339: 20 00      JR      NZ,$633B        
633B: D8         RET     C               
633C: 70         LD      (HL),B          
633D: 00         NOP                     
633E: 00         NOP                     
633F: 00         NOP                     
6340: FF         RST     0X38            
6341: 00         NOP                     
6342: 00         NOP                     
6343: 00         NOP                     
6344: FF         RST     0X38            
6345: 00         NOP                     
6346: 00         NOP                     
6347: 00         NOP                     
6348: 60         LD      H,B             
6349: 10 10      STOP    $10             
634B: 00         NOP                     
634C: 62         LD      H,D             
634D: 00         NOP                     
634E: 20 00      JR      NZ,$6350        
6350: 62         LD      H,D             
6351: 00         NOP                     
6352: 00         NOP                     
6353: 00         NOP                     
6354: FF         RST     0X38            
6355: 00         NOP                     
6356: 00         NOP                     
6357: 00         NOP                     
6358: FF         RST     0X38            
6359: 00         NOP                     
635A: 00         NOP                     
635B: 00         NOP                     
635C: FF         RST     0X38            
635D: 00         NOP                     
635E: 00         NOP                     
635F: 00         NOP                     
6360: 64         LD      H,H             
6361: 10 10      STOP    $10             
6363: 00         NOP                     
6364: 66         LD      H,(HL)          
6365: 00         NOP                     
6366: 20 00      JR      NZ,$6368        
6368: 66         LD      H,(HL)          
6369: 00         NOP                     
636A: 00         NOP                     
636B: 00         NOP                     
636C: FF         RST     0X38            
636D: 00         NOP                     
636E: 00         NOP                     
636F: 00         NOP                     
6370: FF         RST     0X38            
6371: 00         NOP                     
6372: 00         NOP                     
6373: 00         NOP                     
6374: FF         RST     0X38            
6375: 00         NOP                     
6376: 00         NOP                     
6377: 02         LD      (BC),A          
6378: 68         LD      L,B             
6379: 10 10      STOP    $10             
637B: 02         LD      (BC),A          
637C: 6A         LD      L,D             
637D: 00         NOP                     
637E: 20 02      JR      NZ,$6382        
6380: 6A         LD      L,D             
6381: 00         NOP                     
6382: 00         NOP                     
6383: 05         DEC     B               
6384: 68         LD      L,B             
6385: 30 10      JR      NC,$6397        
6387: 05         DEC     B               
6388: 6A         LD      L,D             
6389: 20 20      JR      NZ,$63AB        
638B: 05         DEC     B               
638C: 6A         LD      L,D             
638D: 20 00      JR      NZ,$638F        
638F: 01 68 10   LD      BC,$1068        
6392: 10 01      STOP    $01             
6394: 6A         LD      L,D             
6395: 00         NOP                     
6396: 20 01      JR      NZ,$6399        
6398: 6A         LD      L,D             
6399: 00         NOP                     
639A: 00         NOP                     
639B: 07         RLCA                    
639C: 68         LD      L,B             
639D: 30 10      JR      NC,$63AF        
639F: 07         RLCA                    
63A0: 6A         LD      L,D             
63A1: 20 20      JR      NZ,$63C3        
63A3: 07         RLCA                    
63A4: 6A         LD      L,D             
63A5: 20 00      JR      NZ,$63A7        
63A7: 00         NOP                     
63A8: 68         LD      L,B             
63A9: 10 10      STOP    $10             
63AB: 00         NOP                     
63AC: 6A         LD      L,D             
63AD: 00         NOP                     
63AE: 20 00      JR      NZ,$63B0        
63B0: 6A         LD      L,D             
63B1: 00         NOP                     
63B2: 00         NOP                     
63B3: 08 68 30   LD      ($3068),SP      
63B6: 10 08      STOP    $08             
63B8: 6A         LD      L,D             
63B9: 20 20      JR      NZ,$63DB        
63BB: 08 6A 20   LD      ($206A),SP      
63BE: 21 D0 C3   LD      HL,$C3D0        
63C1: 09         ADD     HL,BC           
63C2: 5E         LD      E,(HL)          
63C3: 50         LD      D,B             
63C4: 21 88 62   LD      HL,$6288        
63C7: 19         ADD     HL,DE           
63C8: 7E         LD      A,(HL)          
63C9: E0 EE      LDFF00  ($EE),A         
63CB: 21 95 62   LD      HL,$6295        
63CE: 19         ADD     HL,DE           
63CF: 7E         LD      A,(HL)          
63D0: E0 EC      LDFF00  ($EC),A         
63D2: 21 A2 62   LD      HL,$62A2        
63D5: 19         ADD     HL,DE           
63D6: 7E         LD      A,(HL)          
63D7: 17         RLA                     
63D8: 17         RLA                     
63D9: 17         RLA                     
63DA: 17         RLA                     
63DB: E6 F0      AND     $F0             
63DD: 5F         LD      E,A             
63DE: 50         LD      D,B             
63DF: 21 D6 62   LD      HL,$62D6        
63E2: 19         ADD     HL,DE           
63E3: 0E 04      LD      C,$04           
63E5: CD 26 3D   CALL    $3D26           
63E8: 3E 02      LD      A,$02           
63EA: CD D0 3D   CALL    $3DD0           
63ED: 21 D0 C3   LD      HL,$C3D0        
63F0: 09         ADD     HL,BC           
63F1: 5E         LD      E,(HL)          
63F2: 50         LD      D,B             
63F3: 21 AF 62   LD      HL,$62AF        
63F6: 19         ADD     HL,DE           
63F7: 7E         LD      A,(HL)          
63F8: E0 EE      LDFF00  ($EE),A         
63FA: 21 BC 62   LD      HL,$62BC        
63FD: 19         ADD     HL,DE           
63FE: 7E         LD      A,(HL)          
63FF: E0 EC      LDFF00  ($EC),A         
6401: 21 C9 62   LD      HL,$62C9        
6404: 19         ADD     HL,DE           
6405: 7E         LD      A,(HL)          
6406: 17         RLA                     
6407: 17         RLA                     
6408: 17         RLA                     
6409: E6 F8      AND     $F8             
640B: 5F         LD      E,A             
640C: 17         RLA                     
640D: E6 F0      AND     $F0             
640F: 83         ADD     A,E             
6410: 5F         LD      E,A             
6411: 50         LD      D,B             
6412: 21 46 63   LD      HL,$6346        
6415: 19         ADD     HL,DE           
6416: 0E 06      LD      C,$06           
6418: CD 26 3D   CALL    $3D26           
641B: 3E 04      LD      A,$04           
641D: CD D0 3D   CALL    $3DD0           
6420: C9         RET                     
6421: 98         SBC     B               
6422: 02         LD      (BC),A          
6423: 09         ADD     HL,BC           
6424: 55         LD      D,L             
6425: 56         LD      D,(HL)          
6426: 55         LD      D,L             
6427: 56         LD      D,(HL)          
6428: 55         LD      D,L             
6429: 56         LD      D,(HL)          
642A: 55         LD      D,L             
642B: 56         LD      D,(HL)          
642C: 55         LD      D,L             
642D: 56         LD      D,(HL)          
642E: 98         SBC     B               
642F: 22         LD      (HLI),A         
6430: 09         ADD     HL,BC           
6431: 55         LD      D,L             
6432: 56         LD      D,(HL)          
6433: 55         LD      D,L             
6434: 56         LD      D,(HL)          
6435: 55         LD      D,L             
6436: 56         LD      D,(HL)          
6437: 55         LD      D,L             
6438: 56         LD      D,(HL)          
6439: 55         LD      D,L             
643A: 56         LD      D,(HL)          
643B: 98         SBC     B               
643C: 42         LD      B,D             
643D: 09         ADD     HL,BC           
643E: 0C         INC     C               
643F: 0D         DEC     C               
6440: 0C         INC     C               
6441: 0D         DEC     C               
6442: 0C         INC     C               
6443: 0D         DEC     C               
6444: 0C         INC     C               
6445: 0D         DEC     C               
6446: 0C         INC     C               
6447: 0D         DEC     C               
6448: 98         SBC     B               
6449: 62         LD      H,D             
644A: 09         ADD     HL,BC           
644B: 0E 0F      LD      C,$0F           
644D: 0E 0F      LD      C,$0F           
644F: 0E 0F      LD      C,$0F           
6451: 0E 0F      LD      C,$0F           
6453: 0E 0F      LD      C,$0F           
6455: 98         SBC     B               
6456: 02         LD      (BC),A          
6457: 09         ADD     HL,BC           
6458: 55         LD      D,L             
6459: 56         LD      D,(HL)          
645A: 55         LD      D,L             
645B: 56         LD      D,(HL)          
645C: 55         LD      D,L             
645D: 56         LD      D,(HL)          
645E: 55         LD      D,L             
645F: 56         LD      D,(HL)          
6460: 55         LD      D,L             
6461: 56         LD      D,(HL)          
6462: 98         SBC     B               
6463: 22         LD      (HLI),A         
6464: 09         ADD     HL,BC           
6465: 55         LD      D,L             
6466: 56         LD      D,(HL)          
6467: 55         LD      D,L             
6468: 56         LD      D,(HL)          
6469: 55         LD      D,L             
646A: 56         LD      D,(HL)          
646B: 55         LD      D,L             
646C: 56         LD      D,(HL)          
646D: 55         LD      D,L             
646E: 56         LD      D,(HL)          
646F: 98         SBC     B               
6470: 42         LD      B,D             
6471: 09         ADD     HL,BC           
6472: 0E 0F      LD      C,$0F           
6474: 0E 0F      LD      C,$0F           
6476: 0E 0F      LD      C,$0F           
6478: 0E 0F      LD      C,$0F           
647A: 0E 0F      LD      C,$0F           
647C: 98         SBC     B               
647D: 62         LD      H,D             
647E: 09         ADD     HL,BC           
647F: 0F         RRCA                    
6480: 0E 0F      LD      C,$0F           
6482: 0E 0F      LD      C,$0F           
6484: 0E 0F      LD      C,$0F           
6486: 0E 0F      LD      C,$0F           
6488: 0E 98      LD      C,$98           
648A: 02         LD      (BC),A          
648B: 09         ADD     HL,BC           
648C: 55         LD      D,L             
648D: 56         LD      D,(HL)          
648E: 55         LD      D,L             
648F: 56         LD      D,(HL)          
6490: 55         LD      D,L             
6491: 56         LD      D,(HL)          
6492: 55         LD      D,L             
6493: 56         LD      D,(HL)          
6494: 55         LD      D,L             
6495: 56         LD      D,(HL)          
6496: 98         SBC     B               
6497: 22         LD      (HLI),A         
6498: 09         ADD     HL,BC           
6499: 0E 0F      LD      C,$0F           
649B: 0E 0F      LD      C,$0F           
649D: 0E 0F      LD      C,$0F           
649F: 0E 0F      LD      C,$0F           
64A1: 0E 0F      LD      C,$0F           
64A3: 98         SBC     B               
64A4: 42         LD      B,D             
64A5: 09         ADD     HL,BC           
64A6: 0F         RRCA                    
64A7: 0E 0F      LD      C,$0F           
64A9: 0E 0F      LD      C,$0F           
64AB: 0E 0F      LD      C,$0F           
64AD: 0E 0F      LD      C,$0F           
64AF: 0E 98      LD      C,$98           
64B1: 62         LD      H,D             
64B2: 09         ADD     HL,BC           
64B3: 0E 0F      LD      C,$0F           
64B5: 0E 0F      LD      C,$0F           
64B7: 0E 0F      LD      C,$0F           
64B9: 0E 0F      LD      C,$0F           
64BB: 0E 0F      LD      C,$0F           
64BD: 98         SBC     B               
64BE: 02         LD      (BC),A          
64BF: 09         ADD     HL,BC           
64C0: 0E 0F      LD      C,$0F           
64C2: 0E 0F      LD      C,$0F           
64C4: 0E 0F      LD      C,$0F           
64C6: 0E 0F      LD      C,$0F           
64C8: 0E 0F      LD      C,$0F           
64CA: 98         SBC     B               
64CB: 22         LD      (HLI),A         
64CC: 09         ADD     HL,BC           
64CD: 0F         RRCA                    
64CE: 0E 0F      LD      C,$0F           
64D0: 0E 0F      LD      C,$0F           
64D2: 0E 0F      LD      C,$0F           
64D4: 0E 0F      LD      C,$0F           
64D6: 0E 98      LD      C,$98           
64D8: 42         LD      B,D             
64D9: 09         ADD     HL,BC           
64DA: 0E 0F      LD      C,$0F           
64DC: 0E 0F      LD      C,$0F           
64DE: 0E 0F      LD      C,$0F           
64E0: 0E 0F      LD      C,$0F           
64E2: 0E 0F      LD      C,$0F           
64E4: 98         SBC     B               
64E5: 62         LD      H,D             
64E6: 09         ADD     HL,BC           
64E7: 0F         RRCA                    
64E8: 0E 0F      LD      C,$0F           
64EA: 0E 0F      LD      C,$0F           
64EC: 0E 0F      LD      C,$0F           
64EE: 0E 0F      LD      C,$0F           
64F0: 0E 98      LD      C,$98           
64F2: 82         ADD     A,D             
64F3: 09         ADD     HL,BC           
64F4: 0F         RRCA                    
64F5: 0E 0F      LD      C,$0F           
64F7: 0F         RRCA                    
64F8: 0F         RRCA                    
64F9: 0E 0F      LD      C,$0F           
64FB: 0E 0F      LD      C,$0F           
64FD: 0E 98      LD      C,$98           
64FF: A2         AND     D               
6500: 09         ADD     HL,BC           
6501: 0E 0F      LD      C,$0F           
6503: 0E 0F      LD      C,$0F           
6505: 0E 0F      LD      C,$0F           
6507: 0E 0F      LD      C,$0F           
6509: 0E 0F      LD      C,$0F           
650B: 98         SBC     B               
650C: C2 09 0F   JP      NZ,$0F09        
650F: 0E 0F      LD      C,$0F           
6511: 0E 0F      LD      C,$0F           
6513: 0E 0F      LD      C,$0F           
6515: 0E 0F      LD      C,$0F           
6517: 0E 98      LD      C,$98           
6519: E2         LDFF00  (C),A           
651A: 09         ADD     HL,BC           
651B: 1E 1E      LD      E,$1E           
651D: 1E 1E      LD      E,$1E           
651F: 1E 1E      LD      E,$1E           
6521: 1E 1E      LD      E,$1E           
6523: 1E 1E      LD      E,$1E           
6525: 98         SBC     B               
6526: 82         ADD     A,D             
6527: 09         ADD     HL,BC           
6528: 0E 0F      LD      C,$0F           
652A: 0E 0F      LD      C,$0F           
652C: 0E 0F      LD      C,$0F           
652E: 0E 0F      LD      C,$0F           
6530: 0E 0F      LD      C,$0F           
6532: 98         SBC     B               
6533: A2         AND     D               
6534: 09         ADD     HL,BC           
6535: 0F         RRCA                    
6536: 0E 0F      LD      C,$0F           
6538: 0E 0F      LD      C,$0F           
653A: 0E 0F      LD      C,$0F           
653C: 0E 0F      LD      C,$0F           
653E: 0E 98      LD      C,$98           
6540: C2 09 1E   JP      NZ,$1E09        
6543: 1E 1E      LD      E,$1E           
6545: 1E 1E      LD      E,$1E           
6547: 1E 1E      LD      E,$1E           
6549: 1E 1E      LD      E,$1E           
654B: 1E 98      LD      E,$98           
654D: E2         LDFF00  (C),A           
654E: 09         ADD     HL,BC           
654F: 09         ADD     HL,BC           
6550: 08 18 09   LD      ($0918),SP      
6553: 7E         LD      A,(HL)          
6554: 7E         LD      A,(HL)          
6555: 09         ADD     HL,BC           
6556: 08 18 09   LD      ($0918),SP      
6559: 98         SBC     B               
655A: 82         ADD     A,D             
655B: 09         ADD     HL,BC           
655C: 0E 0F      LD      C,$0F           
655E: 0E 0F      LD      C,$0F           
6560: 0E 0F      LD      C,$0F           
6562: 0E 0F      LD      C,$0F           
6564: 0E 0F      LD      C,$0F           
6566: 98         SBC     B               
6567: A2         AND     D               
6568: 09         ADD     HL,BC           
6569: 1E 1E      LD      E,$1E           
656B: 1E 1E      LD      E,$1E           
656D: 1E 1E      LD      E,$1E           
656F: 1E 1E      LD      E,$1E           
6571: 1E 1E      LD      E,$1E           
6573: 98         SBC     B               
6574: C2 09 09   JP      NZ,$0909        
6577: 08 18 09   LD      ($0918),SP      
657A: 7E         LD      A,(HL)          
657B: 7E         LD      A,(HL)          
657C: 09         ADD     HL,BC           
657D: 08 18 09   LD      ($0918),SP      
6580: 98         SBC     B               
6581: E2         LDFF00  (C),A           
6582: 09         ADD     HL,BC           
6583: 09         ADD     HL,BC           
6584: 04         INC     B               
6585: 05         DEC     B               
6586: 09         ADD     HL,BC           
6587: 7E         LD      A,(HL)          
6588: 7E         LD      A,(HL)          
6589: 09         ADD     HL,BC           
658A: 04         INC     B               
658B: 05         DEC     B               
658C: 09         ADD     HL,BC           
658D: 98         SBC     B               
658E: 82         ADD     A,D             
658F: 09         ADD     HL,BC           
6590: 1E 1E      LD      E,$1E           
6592: 1E 1E      LD      E,$1E           
6594: 1E 1E      LD      E,$1E           
6596: 1E 1E      LD      E,$1E           
6598: 1E 1E      LD      E,$1E           
659A: 98         SBC     B               
659B: A2         AND     D               
659C: 09         ADD     HL,BC           
659D: 09         ADD     HL,BC           
659E: 08 18 09   LD      ($0918),SP      
65A1: 7E         LD      A,(HL)          
65A2: 7E         LD      A,(HL)          
65A3: 09         ADD     HL,BC           
65A4: 08 18 09   LD      ($0918),SP      
65A7: 98         SBC     B               
65A8: C2 09 09   JP      NZ,$0909        
65AB: 04         INC     B               
65AC: 05         DEC     B               
65AD: 09         ADD     HL,BC           
65AE: 7E         LD      A,(HL)          
65AF: 7E         LD      A,(HL)          
65B0: 09         ADD     HL,BC           
65B1: 04         INC     B               
65B2: 05         DEC     B               
65B3: 09         ADD     HL,BC           
65B4: 98         SBC     B               
65B5: E2         LDFF00  (C),A           
65B6: 09         ADD     HL,BC           
65B7: 19         ADD     HL,DE           
65B8: 14         INC     D               
65B9: 15         DEC     D               
65BA: 19         ADD     HL,DE           
65BB: 1F         RRA                     
65BC: 1F         RRA                     
65BD: 19         ADD     HL,DE           
65BE: 14         INC     D               
65BF: 15         DEC     D               
65C0: 19         ADD     HL,DE           
65C1: 21 64 55   LD      HL,$5564        
65C4: 64         LD      H,H             
65C5: 89         ADC     A,C             
65C6: 64         LD      H,H             
65C7: BD         CP      L               
65C8: 64         LD      H,H             
65C9: F1         POP     AF              
65CA: 64         LD      H,H             
65CB: 25         DEC     H               
65CC: 65         LD      H,L             
65CD: 59         LD      E,C             
65CE: 65         LD      H,L             
65CF: 8D         ADC     A,L             
65D0: 65         LD      H,L             
65D1: F0 F6      LD      A,($F6)         
65D3: FE 0E      CP      $0E             
65D5: CA 3D 61   JP      Z,$613D         
65D8: 3E 02      LD      A,$02           
65DA: E0 A1      LDFF00  ($A1),A         
65DC: EA 67 C1   LD      ($C167),A       
65DF: F0 F0      LD      A,($F0)         
65E1: C7         RST     0X00            
65E2: EA 65 FB   LD      ($FB65),A       
65E5: 65         LD      H,L             
65E6: 24         INC     H               
65E7: 66         LD      H,(HL)          
65E8: 5F         LD      E,A             
65E9: 66         LD      H,(HL)          
65EA: 3E 04      LD      A,$04           
65EC: E0 F4      LDFF00  ($F4),A         
65EE: CD 91 08   CALL    $0891           
65F1: 36 AC      LD      (HL),$AC        
65F3: CD 8C 08   CALL    $088C           
65F6: 36 AC      LD      (HL),$AC        
65F8: CD 8D 3B   CALL    $3B8D           
65FB: CD 91 08   CALL    $0891           
65FE: FE A0      CP      $A0             
6600: 20 05      JR      NZ,$6607        
6602: 21 F4 FF   LD      HL,$FFF4        
6605: 36 2E      LD      (HL),$2E        
6607: A7         AND     A               
6608: 20 07      JR      NZ,$6611        
660A: 3E 2F      LD      A,$2F           
660C: E0 F2      LDFF00  ($F2),A         
660E: CD 8D 3B   CALL    $3B8D           
6611: 1E 01      LD      E,$01           
6613: E6 04      AND     $04             
6615: 28 02      JR      Z,$6619         
6617: 1E FE      LD      E,$FE           
6619: 7B         LD      A,E             
661A: EA 55 C1   LD      ($C155),A       
661D: CD 8C 08   CALL    $088C           
6620: C0         RET     NZ              
6621: C3 05 67   JP      $6705           
6624: 21 B0 C2   LD      HL,$C2B0        
6627: 09         ADD     HL,BC           
6628: 7E         LD      A,(HL)          
6629: F5         PUSH    AF              
662A: 17         RLA                     
662B: E6 06      AND     $06             
662D: 5F         LD      E,A             
662E: 50         LD      D,B             
662F: 21 C1 65   LD      HL,$65C1        
6632: 19         ADD     HL,DE           
6633: 2A         LD      A,(HLI)         
6634: 56         LD      D,(HL)          
6635: 5F         LD      E,A             
6636: C5         PUSH    BC              
6637: 0E 34      LD      C,$34           
6639: 21 01 D6   LD      HL,$D601        
663C: 1A         LD      A,(DE)          
663D: FE 98      CP      $98             
663F: 20 09      JR      NZ,$664A        
6641: F0 97      LD      A,($97)         
6643: A7         AND     A               
6644: 3E 98      LD      A,$98           
6646: 28 02      JR      Z,$664A         
6648: 3E 9A      LD      A,$9A           
664A: 13         INC     DE              
664B: 22         LD      (HLI),A         
664C: 0D         DEC     C               
664D: 20 ED      JR      NZ,$663C        
664F: 36 00      LD      (HL),$00        
6651: C1         POP     BC              
6652: F1         POP     AF              
6653: FE 03      CP      $03             
6655: 20 05      JR      NZ,$665C        
6657: F0 BF      LD      A,($BF)         
6659: EA 68 D3   LD      ($D368),A       
665C: C3 8D 3B   JP      $3B8D           
665F: C5         PUSH    BC              
6660: 21 B0 C2   LD      HL,$C2B0        
6663: 09         ADD     HL,BC           
6664: 7E         LD      A,(HL)          
6665: 17         RLA                     
6666: E6 06      AND     $06             
6668: 5F         LD      E,A             
6669: 50         LD      D,B             
666A: 21 C9 65   LD      HL,$65C9        
666D: 19         ADD     HL,DE           
666E: 2A         LD      A,(HLI)         
666F: 56         LD      D,(HL)          
6670: 5F         LD      E,A             
6671: 0E 34      LD      C,$34           
6673: 21 01 D6   LD      HL,$D601        
6676: 1A         LD      A,(DE)          
6677: FE 98      CP      $98             
6679: 20 09      JR      NZ,$6684        
667B: F0 97      LD      A,($97)         
667D: A7         AND     A               
667E: 3E 98      LD      A,$98           
6680: 28 02      JR      Z,$6684         
6682: 3E 9A      LD      A,$9A           
6684: 13         INC     DE              
6685: 22         LD      (HLI),A         
6686: 0D         DEC     C               
6687: 20 ED      JR      NZ,$6676        
6689: 36 00      LD      (HL),$00        
668B: C1         POP     BC              
668C: 21 B0 C2   LD      HL,$C2B0        
668F: 09         ADD     HL,BC           
6690: 7E         LD      A,(HL)          
6691: 3C         INC     A               
6692: 77         LD      (HL),A          
6693: FE 04      CP      $04             
6695: 20 5B      JR      NZ,$66F2        
6697: 21 12 D7   LD      HL,$D712        
669A: 3E B3      LD      A,$B3           
669C: 22         LD      (HLI),A         
669D: 3E B3      LD      A,$B3           
669F: 22         LD      (HLI),A         
66A0: 3E B3      LD      A,$B3           
66A2: 22         LD      (HLI),A         
66A3: 3E B3      LD      A,$B3           
66A5: 22         LD      (HLI),A         
66A6: 3E B3      LD      A,$B3           
66A8: 22         LD      (HLI),A         
66A9: 21 22 D7   LD      HL,$D722        
66AC: 3E B3      LD      A,$B3           
66AE: 22         LD      (HLI),A         
66AF: 3E B3      LD      A,$B3           
66B1: 22         LD      (HLI),A         
66B2: 3E B3      LD      A,$B3           
66B4: 22         LD      (HLI),A         
66B5: 3E B3      LD      A,$B3           
66B7: 22         LD      (HLI),A         
66B8: 3E B3      LD      A,$B3           
66BA: 22         LD      (HLI),A         
66BB: 21 32 D7   LD      HL,$D732        
66BE: 3E AD      LD      A,$AD           
66C0: 22         LD      (HLI),A         
66C1: 3E B1      LD      A,$B1           
66C3: 22         LD      (HLI),A         
66C4: 3E E7      LD      A,$E7           
66C6: 22         LD      (HLI),A         
66C7: 3E AD      LD      A,$AD           
66C9: 22         LD      (HLI),A         
66CA: 3E B1      LD      A,$B1           
66CC: 22         LD      (HLI),A         
66CD: 21 42 D7   LD      HL,$D742        
66D0: 3E AE      LD      A,$AE           
66D2: 22         LD      (HLI),A         
66D3: 3E B2      LD      A,$B2           
66D5: 22         LD      (HLI),A         
66D6: 3E E3      LD      A,$E3           
66D8: 22         LD      (HLI),A         
66D9: 3E AE      LD      A,$AE           
66DB: 22         LD      (HLI),A         
66DC: 3E B2      LD      A,$B2           
66DE: 22         LD      (HLI),A         
66DF: CD 62 7A   CALL    $7A62           
66E2: CB E6      SET     1,E             
66E4: AF         XOR     A               
66E5: EA 55 C1   LD      ($C155),A       
66E8: EA 67 C1   LD      ($C167),A       
66EB: 3E 02      LD      A,$02           
66ED: E0 F2      LDFF00  ($F2),A         
66EF: C3 B0 79   JP      $79B0           
66F2: CD 8D 3B   CALL    $3B8D           
66F5: 36 01      LD      (HL),$01        
66F7: CD 91 08   CALL    $0891           
66FA: 36 30      LD      (HL),$30        
66FC: C9         RET                     
66FD: 18 58      JR      $6757           
66FF: 28 48      JR      Z,$6749         
6701: 38 20      JR      C,$6723         
6703: 50         LD      D,B             
6704: 40         LD      B,B             
6705: F0 E7      LD      A,($E7)         
6707: E6 03      AND     $03             
6709: 20 37      JR      NZ,$6742        
670B: 3E A7      LD      A,$A7           
670D: CD 01 3C   CALL    $3C01           
6710: 38 30      JR      C,$6742         
6712: C5         PUSH    BC              
6713: CD ED 27   CALL    $27ED           
6716: E6 07      AND     $07             
6718: 4F         LD      C,A             
6719: 21 FD 66   LD      HL,$66FD        
671C: 09         ADD     HL,BC           
671D: 7E         LD      A,(HL)          
671E: 21 00 C2   LD      HL,$C200        
6721: 19         ADD     HL,DE           
6722: 77         LD      (HL),A          
6723: CD ED 27   CALL    $27ED           
6726: E6 07      AND     $07             
6728: C6 47      ADD     $47             
672A: 21 10 C2   LD      HL,$C210        
672D: 19         ADD     HL,DE           
672E: 77         LD      (HL),A          
672F: C1         POP     BC              
6730: 21 40 C3   LD      HL,$C340        
6733: 19         ADD     HL,DE           
6734: 36 C2      LD      (HL),$C2        
6736: 21 E0 C2   LD      HL,$C2E0        
6739: 19         ADD     HL,DE           
673A: 36 10      LD      (HL),$10        
673C: 21 B0 C2   LD      HL,$C2B0        
673F: 19         ADD     HL,DE           
6740: 36 01      LD      (HL),$01        
6742: C9         RET                     
6743: 60         LD      H,B             
6744: 00         NOP                     
6745: 62         LD      H,D             
6746: 00         NOP                     
6747: 62         LD      H,D             
6748: 20 60      JR      NZ,$67AA        
674A: 20 64      JR      NZ,$67B0        
674C: 00         NOP                     
674D: 66         LD      H,(HL)          
674E: 00         NOP                     
674F: 66         LD      H,(HL)          
6750: 20 64      JR      NZ,$67B6        
6752: 20 68      JR      NZ,$67BC        
6754: 00         NOP                     
6755: 6A         LD      L,D             
6756: 00         NOP                     
6757: 6C         LD      L,H             
6758: 00         NOP                     
6759: 6E         LD      L,(HL)          
675A: 00         NOP                     
675B: 6A         LD      L,D             
675C: 20 68      JR      NZ,$67C6        
675E: 20 6E      JR      NZ,$67CE        
6760: 20 6C      JR      NZ,$67CE        
6762: 20 F0      JR      NZ,$6754        
6764: 10 21      STOP    $21             
6766: C0         RET     NZ              
6767: C2 09 7E   JP      NZ,$7E09        
676A: A7         AND     A               
676B: C2 D1 65   JP      NZ,$65D1        
676E: F0 F7      LD      A,($F7)         
6770: FE 0A      CP      $0A             
6772: 20 10      JR      NZ,$6784        
6774: F0 F6      LD      A,($F6)         
6776: FE 97      CP      $97             
6778: 28 04      JR      Z,$677E         
677A: FE 98      CP      $98             
677C: 20 06      JR      NZ,$6784        
677E: FA 7F DB   LD      A,($DB7F)       
6781: A7         AND     A               
6782: 20 06      JR      NZ,$678A        
6784: 11 43 67   LD      DE,$6743        
6787: CD 3B 3C   CALL    $3C3B           
678A: CD 9B 78   CALL    $789B           
678D: CD BD 78   CALL    $78BD           
6790: CD B4 3B   CALL    $3BB4           
6793: CD 07 79   CALL    $7907           
6796: CD 9E 3B   CALL    $3B9E           
6799: FA 33 C1   LD      A,($C133)       
679C: A7         AND     A               
679D: 20 58      JR      NZ,$67F7        
679F: F0 CB      LD      A,($CB)         
67A1: E6 03      AND     $03             
67A3: 28 22      JR      Z,$67C7         
67A5: 5F         LD      E,A             
67A6: 50         LD      D,B             
67A7: 21 62 67   LD      HL,$6762        
67AA: 19         ADD     HL,DE           
67AB: 7E         LD      A,(HL)          
67AC: 21 40 C2   LD      HL,$C240        
67AF: 09         ADD     HL,BC           
67B0: 77         LD      (HL),A          
67B1: 21 50 C2   LD      HL,$C250        
67B4: 09         ADD     HL,BC           
67B5: 70         LD      (HL),B          
67B6: 7B         LD      A,E             
67B7: E6 02      AND     $02             
67B9: C6 04      ADD     $04             
67BB: 5F         LD      E,A             
67BC: F0 E7      LD      A,($E7)         
67BE: 1F         RRA                     
67BF: 1F         RRA                     
67C0: 1F         RRA                     
67C1: E6 01      AND     $01             
67C3: 83         ADD     A,E             
67C4: C3 87 3B   JP      $3B87           
67C7: F0 CB      LD      A,($CB)         
67C9: E6 0F      AND     $0F             
67CB: 28 2A      JR      Z,$67F7         
67CD: 1F         RRA                     
67CE: 1F         RRA                     
67CF: 2F         CPL                     
67D0: E6 03      AND     $03             
67D2: 5F         LD      E,A             
67D3: 50         LD      D,B             
67D4: 21 62 67   LD      HL,$6762        
67D7: 19         ADD     HL,DE           
67D8: 7E         LD      A,(HL)          
67D9: 21 50 C2   LD      HL,$C250        
67DC: 09         ADD     HL,BC           
67DD: 77         LD      (HL),A          
67DE: 21 40 C2   LD      HL,$C240        
67E1: 09         ADD     HL,BC           
67E2: 70         LD      (HL),B          
67E3: 7B         LD      A,E             
67E4: 3D         DEC     A               
67E5: EE 01      XOR     $01             
67E7: CB 2F      SET     1,E             
67E9: 17         RLA                     
67EA: 17         RLA                     
67EB: 5F         LD      E,A             
67EC: F0 E7      LD      A,($E7)         
67EE: 1F         RRA                     
67EF: 1F         RRA                     
67F0: 1F         RRA                     
67F1: E6 01      AND     $01             
67F3: 83         ADD     A,E             
67F4: C3 87 3B   JP      $3B87           
67F7: C3 AF 3D   JP      $3DAF           
67FA: 60         LD      H,B             
67FB: 00         NOP                     
67FC: 62         LD      H,D             
67FD: 00         NOP                     
67FE: 64         LD      H,H             
67FF: 00         NOP                     
6800: 66         LD      H,(HL)          
6801: 00         NOP                     
6802: 62         LD      H,D             
6803: 20 60      JR      NZ,$6865        
6805: 20 66      JR      NZ,$686D        
6807: 20 64      JR      NZ,$686D        
6809: 20 11      JR      NZ,$681C        
680B: FA 67 CD   LD      A,($CD67)       
680E: 3B         DEC     SP              
680F: 3C         INC     A               
6810: CD 9B 78   CALL    $789B           
6813: 21 40 C2   LD      HL,$C240        
6816: 09         ADD     HL,BC           
6817: 7E         LD      A,(HL)          
6818: 07         RLCA                    
6819: 07         RLCA                    
681A: E6 02      AND     $02             
681C: 5F         LD      E,A             
681D: F0 E7      LD      A,($E7)         
681F: 1F         RRA                     
6820: 1F         RRA                     
6821: 1F         RRA                     
6822: E6 01      AND     $01             
6824: B3         OR      E               
6825: CD 87 3B   CALL    $3B87           
6828: CD B4 3B   CALL    $3BB4           
682B: F0 F0      LD      A,($F0)         
682D: C7         RST     0X00            
682E: 34         INC     (HL)            
682F: 68         LD      L,B             
6830: 57         LD      D,A             
6831: 68         LD      L,B             
6832: 65         LD      H,L             
6833: 68         LD      L,B             
6834: 21 40 C2   LD      HL,$C240        
6837: F0 EB      LD      A,($EB)         
6839: FE AA      CP      $AA             
683B: 28 03      JR      Z,$6840         
683D: 21 50 C2   LD      HL,$C250        
6840: 09         ADD     HL,BC           
6841: 36 08      LD      (HL),$08        
6843: 1E 80      LD      E,$80           
6845: F0 EB      LD      A,($EB)         
6847: FE AA      CP      $AA             
6849: 28 02      JR      Z,$684D         
684B: 1E 60      LD      E,$60           
684D: CD 91 08   CALL    $0891           
6850: 73         LD      (HL),E          
6851: CD 8D 3B   CALL    $3B8D           
6854: 36 01      LD      (HL),$01        
6856: C9         RET                     
6857: CD 91 08   CALL    $0891           
685A: 20 05      JR      NZ,$6861        
685C: 36 28      LD      (HL),$28        
685E: CD 8D 3B   CALL    $3B8D           
6861: CD 07 79   CALL    $7907           
6864: C9         RET                     
6865: CD 91 08   CALL    $0891           
6868: 20 13      JR      NZ,$687D        
686A: 21 40 C2   LD      HL,$C240        
686D: 09         ADD     HL,BC           
686E: 7E         LD      A,(HL)          
686F: 2F         CPL                     
6870: 3C         INC     A               
6871: 77         LD      (HL),A          
6872: 21 50 C2   LD      HL,$C250        
6875: 09         ADD     HL,BC           
6876: 7E         LD      A,(HL)          
6877: 2F         CPL                     
6878: 3C         INC     A               
6879: 77         LD      (HL),A          
687A: C3 43 68   JP      $6843           
687D: C9         RET                     
687E: F0 F0      LD      A,($F0)         
6880: FE 05      CP      $05             
6882: 20 06      JR      NZ,$688A        
6884: F0 ED      LD      A,($ED)         
6886: F6 40      OR      $40             
6888: E0 ED      LDFF00  ($ED),A         
688A: 11 FA 67   LD      DE,$67FA        
688D: CD 3B 3C   CALL    $3C3B           
6890: CD 9B 78   CALL    $789B           
6893: 21 40 C2   LD      HL,$C240        
6896: 09         ADD     HL,BC           
6897: 7E         LD      A,(HL)          
6898: 07         RLCA                    
6899: 07         RLCA                    
689A: E6 02      AND     $02             
689C: 5F         LD      E,A             
689D: CD BD 78   CALL    $78BD           
68A0: F0 F0      LD      A,($F0)         
68A2: FE 05      CP      $05             
68A4: 28 0E      JR      Z,$68B4         
68A6: F0 E7      LD      A,($E7)         
68A8: 1F         RRA                     
68A9: 1F         RRA                     
68AA: 1F         RRA                     
68AB: E6 01      AND     $01             
68AD: B3         OR      E               
68AE: CD 87 3B   CALL    $3B87           
68B1: CD B4 3B   CALL    $3BB4           
68B4: F0 F0      LD      A,($F0)         
68B6: C7         RST     0X00            
68B7: C3 68 D3   JP      $D368           
68BA: 68         LD      L,B             
68BB: F1         POP     AF              
68BC: 68         LD      L,B             
68BD: 25         DEC     H               
68BE: 69         LD      L,C             
68BF: 3E 69      LD      A,$69           
68C1: 63         LD      H,E             
68C2: 69         LD      L,C             
68C3: 21 80 C4   LD      HL,$C480        
68C6: 09         ADD     HL,BC           
68C7: 36 03      LD      (HL),$03        
68C9: F0 EF      LD      A,($EF)         
68CB: 21 B0 C2   LD      HL,$C2B0        
68CE: 09         ADD     HL,BC           
68CF: 77         LD      (HL),A          
68D0: C3 8D 3B   JP      $3B8D           
68D3: CD 91 08   CALL    $0891           
68D6: CD ED 27   CALL    $27ED           
68D9: E6 7F      AND     $7F             
68DB: C6 30      ADD     $30             
68DD: 77         LD      (HL),A          
68DE: CD ED 27   CALL    $27ED           
68E1: 1E F4      LD      E,$F4           
68E3: E6 01      AND     $01             
68E5: 28 02      JR      Z,$68E9         
68E7: 1E 0C      LD      E,$0C           
68E9: 21 40 C2   LD      HL,$C240        
68EC: 09         ADD     HL,BC           
68ED: 73         LD      (HL),E          
68EE: C3 8D 3B   JP      $3B8D           
68F1: CD 91 08   CALL    $0891           
68F4: 20 14      JR      NZ,$690A        
68F6: 21 50 C2   LD      HL,$C250        
68F9: 09         ADD     HL,BC           
68FA: 36 D4      LD      (HL),$D4        
68FC: F0 EC      LD      A,($EC)         
68FE: D6 08      SUB     $08             
6900: CD 8D 69   CALL    $698D           
6903: 3E 24      LD      A,$24           
6905: E0 F2      LDFF00  ($F2),A         
6907: C3 8D 3B   JP      $3B8D           
690A: CD 8C 08   CALL    $088C           
690D: 20 10      JR      NZ,$691F        
690F: CD ED 27   CALL    $27ED           
6912: E6 3F      AND     $3F             
6914: F6 10      OR      $10             
6916: 77         LD      (HL),A          
6917: 21 40 C2   LD      HL,$C240        
691A: 09         ADD     HL,BC           
691B: 7E         LD      A,(HL)          
691C: 2F         CPL                     
691D: 3C         INC     A               
691E: 77         LD      (HL),A          
691F: CD 14 79   CALL    $7914           
6922: C3 9E 3B   JP      $3B9E           
6925: CD 91 08   CALL    $0891           
6928: 20 13      JR      NZ,$693D        
692A: CD 0A 79   CALL    $790A           
692D: CD 53 69   CALL    $6953           
6930: 21 50 C2   LD      HL,$C250        
6933: 09         ADD     HL,BC           
6934: 34         INC     (HL)            
6935: 7E         LD      A,(HL)          
6936: FE 18      CP      $18             
6938: 20 03      JR      NZ,$693D        
693A: CD 8D 3B   CALL    $3B8D           
693D: C9         RET                     
693E: 21 B0 C2   LD      HL,$C2B0        
6941: 09         ADD     HL,BC           
6942: 7E         LD      A,(HL)          
6943: 21 10 C2   LD      HL,$C210        
6946: 09         ADD     HL,BC           
6947: BE         CP      (HL)            
6948: 30 06      JR      NC,$6950        
694A: CD 8D 3B   CALL    $3B8D           
694D: 36 01      LD      (HL),$01        
694F: C9         RET                     
6950: CD 0A 79   CALL    $790A           
6953: 21 30 C4   LD      HL,$C430        
6956: 09         ADD     HL,BC           
6957: CB C6      SET     1,E             
6959: CD 9E 3B   CALL    $3B9E           
695C: 21 30 C4   LD      HL,$C430        
695F: 09         ADD     HL,BC           
6960: CB 86      SET     1,E             
6962: C9         RET                     
6963: 21 40 C3   LD      HL,$C340        
6966: 09         ADD     HL,BC           
6967: CB FE      SET     1,E             
6969: CB F6      SET     1,E             
696B: 21 50 C2   LD      HL,$C250        
696E: 09         ADD     HL,BC           
696F: 34         INC     (HL)            
6970: E5         PUSH    HL              
6971: 21 70 C4   LD      HL,$C470        
6974: 09         ADD     HL,BC           
6975: 7E         LD      A,(HL)          
6976: E1         POP     HL              
6977: A7         AND     A               
6978: 28 02      JR      Z,$697C         
697A: 36 06      LD      (HL),$06        
697C: CD 0A 79   CALL    $790A           
697F: F0 EC      LD      A,($EC)         
6981: FE 70      CP      $70             
6983: 38 CE      JR      C,$6953         
6985: FE 88      CP      $88             
6987: D2 B0 79   JP      NC,$79B0        
698A: C9         RET                     
698B: F0 EC      LD      A,($EC)         
698D: E0 D8      LDFF00  ($D8),A         
698F: F0 EE      LD      A,($EE)         
6991: E0 D7      LDFF00  ($D7),A         
6993: 3E 01      LD      A,$01           
6995: CD 53 09   CALL    $0953           
6998: 3E 0E      LD      A,$0E           
699A: E0 F2      LDFF00  ($F2),A         
699C: C9         RET                     
699D: 9A         SBC     D               
699E: 10 9C      STOP    $9C             
69A0: 10 11      STOP    $11             
69A2: 9D         SBC     L               
69A3: 69         LD      L,C             
69A4: CD 3B 3C   CALL    $3C3B           
69A7: CD 40 79   CALL    $7940           
69AA: 21 20 C3   LD      HL,$C320        
69AD: 09         ADD     HL,BC           
69AE: 35         DEC     (HL)            
69AF: 21 10 C3   LD      HL,$C310        
69B2: 09         ADD     HL,BC           
69B3: 7E         LD      A,(HL)          
69B4: E6 80      AND     $80             
69B6: C2 B0 79   JP      NZ,$79B0        
69B9: C9         RET                     
69BA: 21 B0 C2   LD      HL,$C2B0        
69BD: 09         ADD     HL,BC           
69BE: 7E         LD      A,(HL)          
69BF: A7         AND     A               
69C0: C2 A1 69   JP      NZ,$69A1        
69C3: CD 4A 6B   CALL    $6B4A           
69C6: CD 00 78   CALL    $7800           
69C9: F0 F0      LD      A,($F0)         
69CB: C7         RST     0X00            
69CC: D4 69 0B   CALL    NC,$0B69        
69CF: 6A         LD      L,D             
69D0: 26 6A      LD      H,$6A           
69D2: 64         LD      H,H             
69D3: 6A         LD      L,D             
69D4: CD 4E 78   CALL    $784E           
69D7: 30 26      JR      NC,$69FF        
69D9: 1E CD      LD      E,$CD           
69DB: F0 F8      LD      A,($F8)         
69DD: E6 20      AND     $20             
69DF: 20 1A      JR      NZ,$69FB        
69E1: 1E CC      LD      E,$CC           
69E3: FA FE DA   LD      A,($DAFE)       
69E6: E6 20      AND     $20             
69E8: 20 11      JR      NZ,$69FB        
69EA: 1E C6      LD      E,$C6           
69EC: FA 0E DB   LD      A,($DB0E)       
69EF: FE 03      CP      $03             
69F1: 20 08      JR      NZ,$69FB        
69F3: 3E C7      LD      A,$C7           
69F5: CD 85 21   CALL    $2185           
69F8: C3 8D 3B   JP      $3B8D           
69FB: 7B         LD      A,E             
69FC: CD 85 21   CALL    $2185           
69FF: F0 E7      LD      A,($E7)         
6A01: 1F         RRA                     
6A02: 1F         RRA                     
6A03: 1F         RRA                     
6A04: 1F         RRA                     
6A05: E6 01      AND     $01             
6A07: CD 87 3B   CALL    $3B87           
6A0A: C9         RET                     
6A0B: FA 9F C1   LD      A,($C19F)       
6A0E: A7         AND     A               
6A0F: 20 14      JR      NZ,$6A25        
6A11: CD 8D 3B   CALL    $3B8D           
6A14: FA 77 C1   LD      A,($C177)       
6A17: A7         AND     A               
6A18: 28 06      JR      Z,$6A20         
6A1A: 70         LD      (HL),B          
6A1B: 3E C9      LD      A,$C9           
6A1D: C3 85 21   JP      $2185           
6A20: 3E C8      LD      A,$C8           
6A22: CD 85 21   CALL    $2185           
6A25: C9         RET                     
6A26: FA 9F C1   LD      A,($C19F)       
6A29: A7         AND     A               
6A2A: 20 33      JR      NZ,$6A5F        
6A2C: 3E CD      LD      A,$CD           
6A2E: CD 01 3C   CALL    $3C01           
6A31: F0 D7      LD      A,($D7)         
6A33: 21 00 C2   LD      HL,$C200        
6A36: 19         ADD     HL,DE           
6A37: D6 02      SUB     $02             
6A39: 77         LD      (HL),A          
6A3A: F0 D8      LD      A,($D8)         
6A3C: 21 10 C2   LD      HL,$C210        
6A3F: 19         ADD     HL,DE           
6A40: 77         LD      (HL),A          
6A41: 21 B0 C2   LD      HL,$C2B0        
6A44: 19         ADD     HL,DE           
6A45: 36 01      LD      (HL),$01        
6A47: 21 20 C3   LD      HL,$C320        
6A4A: 19         ADD     HL,DE           
6A4B: 36 20      LD      (HL),$20        
6A4D: 21 40 C3   LD      HL,$C340        
6A50: 19         ADD     HL,DE           
6A51: 36 C2      LD      (HL),$C2        
6A53: 3E 24      LD      A,$24           
6A55: E0 F2      LDFF00  ($F2),A         
6A57: CD 91 08   CALL    $0891           
6A5A: 36 C0      LD      (HL),$C0        
6A5C: CD 8D 3B   CALL    $3B8D           
6A5F: C9         RET                     
6A60: 00         NOP                     
6A61: 01 02 01   LD      BC,$0102        
6A64: 3E 02      LD      A,$02           
6A66: E0 A1      LDFF00  ($A1),A         
6A68: EA 67 C1   LD      ($C167),A       
6A6B: CD 91 08   CALL    $0891           
6A6E: 20 15      JR      NZ,$6A85        
6A70: AF         XOR     A               
6A71: EA 67 C1   LD      ($C167),A       
6A74: 3E 04      LD      A,$04           
6A76: EA 0E DB   LD      ($DB0E),A       
6A79: 3E 0D      LD      A,$0D           
6A7B: E0 A5      LDFF00  ($A5),A         
6A7D: CD 98 08   CALL    $0898           
6A80: CD 8D 3B   CALL    $3B8D           
6A83: 70         LD      (HL),B          
6A84: C9         RET                     
6A85: FE 80      CP      $80             
6A87: 38 05      JR      C,$6A8E         
6A89: 3E 03      LD      A,$03           
6A8B: C3 87 3B   JP      $3B87           
6A8E: FE 08      CP      $08             
6A90: 20 06      JR      NZ,$6A98        
6A92: 35         DEC     (HL)            
6A93: 3E CA      LD      A,$CA           
6A95: CD 85 21   CALL    $2185           
6A98: F0 E7      LD      A,($E7)         
6A9A: 1F         RRA                     
6A9B: 1F         RRA                     
6A9C: 1F         RRA                     
6A9D: E6 03      AND     $03             
6A9F: 5F         LD      E,A             
6AA0: 50         LD      D,B             
6AA1: 21 60 6A   LD      HL,$6A60        
6AA4: 19         ADD     HL,DE           
6AA5: 7E         LD      A,(HL)          
6AA6: CD 87 3B   CALL    $3B87           
6AA9: C9         RET                     
6AAA: 00         NOP                     
6AAB: 00         NOP                     
6AAC: 50         LD      D,B             
6AAD: 00         NOP                     
6AAE: 00         NOP                     
6AAF: 08 52 00   LD      ($0052),SP      
6AB2: 00         NOP                     
6AB3: 10 54      STOP    $54             
6AB5: 00         NOP                     
6AB6: 10 00      STOP    $00             
6AB8: 56         LD      D,(HL)          
6AB9: 00         NOP                     
6ABA: 10 08      STOP    $08             
6ABC: 58         LD      E,B             
6ABD: 00         NOP                     
6ABE: 10 10      STOP    $10             
6AC0: 5A         LD      E,D             
6AC1: 00         NOP                     
6AC2: FF         RST     0X38            
6AC3: FF         RST     0X38            
6AC4: FF         RST     0X38            
6AC5: FF         RST     0X38            
6AC6: FF         RST     0X38            
6AC7: FF         RST     0X38            
6AC8: FF         RST     0X38            
6AC9: FF         RST     0X38            
6ACA: 00         NOP                     
6ACB: 00         NOP                     
6ACC: 50         LD      D,B             
6ACD: 00         NOP                     
6ACE: 00         NOP                     
6ACF: 08 52 00   LD      ($0052),SP      
6AD2: 00         NOP                     
6AD3: 10 5C      STOP    $5C             
6AD5: 00         NOP                     
6AD6: 10 00      STOP    $00             
6AD8: 56         LD      D,(HL)          
6AD9: 00         NOP                     
6ADA: 10 08      STOP    $08             
6ADC: 58         LD      E,B             
6ADD: 00         NOP                     
6ADE: 10 10      STOP    $10             
6AE0: 5E         LD      E,(HL)          
6AE1: 00         NOP                     
6AE2: 10 18      STOP    $18             
6AE4: 60         LD      H,B             
6AE5: 00         NOP                     
6AE6: FF         RST     0X38            
6AE7: FF         RST     0X38            
6AE8: FF         RST     0X38            
6AE9: FF         RST     0X38            
6AEA: 00         NOP                     
6AEB: 00         NOP                     
6AEC: 62         LD      H,D             
6AED: 00         NOP                     
6AEE: 00         NOP                     
6AEF: 08 64 00   LD      ($0064),SP      
6AF2: 00         NOP                     
6AF3: 10 66      STOP    $66             
6AF5: 00         NOP                     
6AF6: 10 00      STOP    $00             
6AF8: 68         LD      L,B             
6AF9: 00         NOP                     
6AFA: 10 08      STOP    $08             
6AFC: 58         LD      E,B             
6AFD: 00         NOP                     
6AFE: 10 10      STOP    $10             
6B00: 5E         LD      E,(HL)          
6B01: 00         NOP                     
6B02: 10 10      STOP    $10             
6B04: 60         LD      H,B             
6B05: 00         NOP                     
6B06: FF         RST     0X38            
6B07: FF         RST     0X38            
6B08: FF         RST     0X38            
6B09: FF         RST     0X38            
6B0A: 00         NOP                     
6B0B: 00         NOP                     
6B0C: 6A         LD      L,D             
6B0D: 00         NOP                     
6B0E: 00         NOP                     
6B0F: 08 6C 00   LD      ($006C),SP      
6B12: 00         NOP                     
6B13: 10 6E      STOP    $6E             
6B15: 00         NOP                     
6B16: 10 00      STOP    $00             
6B18: 68         LD      L,B             
6B19: 00         NOP                     
6B1A: 10 08      STOP    $08             
6B1C: 58         LD      E,B             
6B1D: 00         NOP                     
6B1E: 10 10      STOP    $10             
6B20: 5E         LD      E,(HL)          
6B21: 00         NOP                     
6B22: 10 10      STOP    $10             
6B24: 60         LD      H,B             
6B25: 00         NOP                     
6B26: FF         RST     0X38            
6B27: FF         RST     0X38            
6B28: FF         RST     0X38            
6B29: FF         RST     0X38            
6B2A: 10 00      STOP    $00             
6B2C: 74         LD      (HL),H          
6B2D: 00         NOP                     
6B2E: 10 08      STOP    $08             
6B30: 76         HALT                    
6B31: 00         NOP                     
6B32: 10 10      STOP    $10             
6B34: 74         LD      (HL),H          
6B35: 00         NOP                     
6B36: 10 18      STOP    $18             
6B38: 76         HALT                    
6B39: 00         NOP                     
6B3A: 00         NOP                     
6B3B: 10 74      STOP    $74             
6B3D: 00         NOP                     
6B3E: 00         NOP                     
6B3F: 18 76      JR      $6BB7           
6B41: 00         NOP                     
6B42: 00         NOP                     
6B43: 00         NOP                     
6B44: 74         LD      (HL),H          
6B45: 00         NOP                     
6B46: 00         NOP                     
6B47: 08 76 00   LD      ($0076),SP      
6B4A: F0 F1      LD      A,($F1)         
6B4C: 17         RLA                     
6B4D: 17         RLA                     
6B4E: 17         RLA                     
6B4F: 17         RLA                     
6B50: 17         RLA                     
6B51: E6 E0      AND     $E0             
6B53: 5F         LD      E,A             
6B54: 50         LD      D,B             
6B55: 21 AA 6A   LD      HL,$6AAA        
6B58: 19         ADD     HL,DE           
6B59: F0 EE      LD      A,($EE)         
6B5B: C6 03      ADD     $03             
6B5D: E0 EE      LDFF00  ($EE),A         
6B5F: 0E 07      LD      C,$07           
6B61: CD 26 3D   CALL    $3D26           
6B64: 3E 02      LD      A,$02           
6B66: CD D0 3D   CALL    $3DD0           
6B69: 3E 78      LD      A,$78           
6B6B: E0 EE      LDFF00  ($EE),A         
6B6D: 3E 5C      LD      A,$5C           
6B6F: E0 EC      LDFF00  ($EC),A         
6B71: 21 2A 6B   LD      HL,$6B2A        
6B74: 0E 08      LD      C,$08           
6B76: FA 0E DB   LD      A,($DB0E)       
6B79: FE 04      CP      $04             
6B7B: 20 02      JR      NZ,$6B7F        
6B7D: 0D         DEC     C               
6B7E: 0D         DEC     C               
6B7F: CD 26 3D   CALL    $3D26           
6B82: 3E 03      LD      A,$03           
6B84: CD D0 3D   CALL    $3DD0           
6B87: CD BA 3D   CALL    $3DBA           
6B8A: C9         RET                     
6B8B: 08 04 70   LD      ($7004),SP      
6B8E: 00         NOP                     
6B8F: 08 0C 72   LD      ($720C),SP      
6B92: 00         NOP                     
6B93: 08 14 70   LD      ($7014),SP      
6B96: 20 FA      JR      NZ,$6B92        
6B98: A5         AND     L               
6B99: DB                              
6B9A: A7         AND     A               
6B9B: 20 0E      JR      NZ,$6BAB        
6B9D: 21 40 C3   LD      HL,$C340        
6BA0: 09         ADD     HL,BC           
6BA1: 36 C3      LD      (HL),$C3        
6BA3: 21 8B 6B   LD      HL,$6B8B        
6BA6: 0E 03      LD      C,$03           
6BA8: C3 26 3D   JP      $3D26           
6BAB: F0 F6      LD      A,($F6)         
6BAD: FE FE      CP      $FE             
6BAF: CA BA 69   JP      Z,$69BA         
6BB2: F0 EE      LD      A,($EE)         
6BB4: FE 30      CP      $30             
6BB6: DA 0D 6D   JP      C,$6D0D         
6BB9: F0 F0      LD      A,($F0)         
6BBB: A7         AND     A               
6BBC: 20 2E      JR      NZ,$6BEC        
6BBE: CD 8D 3B   CALL    $3B8D           
6BC1: 21 10 C2   LD      HL,$C210        
6BC4: 09         ADD     HL,BC           
6BC5: 36 48      LD      (HL),$48        
6BC7: 21 00 C2   LD      HL,$C200        
6BCA: 09         ADD     HL,BC           
6BCB: 7E         LD      A,(HL)          
6BCC: D6 04      SUB     $04             
6BCE: 77         LD      (HL),A          
6BCF: 3E CD      LD      A,$CD           
6BD1: CD 01 3C   CALL    $3C01           
6BD4: 21 00 C2   LD      HL,$C200        
6BD7: 19         ADD     HL,DE           
6BD8: 36 28      LD      (HL),$28        
6BDA: 21 10 C2   LD      HL,$C210        
6BDD: 19         ADD     HL,DE           
6BDE: 36 28      LD      (HL),$28        
6BE0: 21 B0 C2   LD      HL,$C2B0        
6BE3: 19         ADD     HL,DE           
6BE4: 36 01      LD      (HL),$01        
6BE6: 21 E0 C2   LD      HL,$C2E0        
6BE9: 19         ADD     HL,DE           
6BEA: 36 40      LD      (HL),$40        
6BEC: CD A3 6C   CALL    $6CA3           
6BEF: CD 00 78   CALL    $7800           
6BF2: F0 F0      LD      A,($F0)         
6BF4: C7         RST     0X00            
6BF5: FB         EI                      
6BF6: 6B         LD      L,E             
6BF7: FC                              
6BF8: 6B         LD      L,E             
6BF9: 2E 6C      LD      L,$6C           
6BFB: C9         RET                     
6BFC: CD 87 08   CALL    $0887           
6BFF: C0         RET     NZ              
6C00: CD 4E 78   CALL    $784E           
6C03: 30 1B      JR      NC,$6C20        
6C05: FA 0E DB   LD      A,($DB0E)       
6C08: FE 0E      CP      $0E             
6C0A: 20 07      JR      NZ,$6C13        
6C0C: 3E D8      LD      A,$D8           
6C0E: CD 97 21   CALL    $2197           
6C11: 18 05      JR      $6C18           
6C13: 3E 9B      LD      A,$9B           
6C15: CD 85 21   CALL    $2185           
6C18: 21 9F C1   LD      HL,$C19F        
6C1B: CB FE      SET     1,E             
6C1D: CD 8D 3B   CALL    $3B8D           
6C20: F0 E7      LD      A,($E7)         
6C22: 1E 00      LD      E,$00           
6C24: E6 20      AND     $20             
6C26: 28 01      JR      Z,$6C29         
6C28: 1C         INC     E               
6C29: 7B         LD      A,E             
6C2A: CD 87 3B   CALL    $3B87           
6C2D: C9         RET                     
6C2E: FA 9F C1   LD      A,($C19F)       
6C31: A7         AND     A               
6C32: 20 05      JR      NZ,$6C39        
6C34: CD 8D 3B   CALL    $3B8D           
6C37: 36 01      LD      (HL),$01        
6C39: CD 5A 79   CALL    $795A           
6C3C: 7B         LD      A,E             
6C3D: C6 02      ADD     $02             
6C3F: CD 87 3B   CALL    $3B87           
6C42: C9         RET                     
6C43: F8 F8      LDHL    SP,$F8          
6C45: 5A         LD      E,D             
6C46: 00         NOP                     
6C47: F8 00      LDHL    SP,$00          
6C49: 5C         LD      E,H             
6C4A: 00         NOP                     
6C4B: F8 08      LDHL    SP,$08          
6C4D: 5E         LD      E,(HL)          
6C4E: 00         NOP                     
6C4F: 08 00 60   LD      ($6000),SP      
6C52: 00         NOP                     
6C53: 08 08 62   LD      ($6208),SP      
6C56: 00         NOP                     
6C57: F8 10      LDHL    SP,$10          
6C59: 5A         LD      E,D             
6C5A: 20 F8      JR      NZ,$6C54        
6C5C: 00         NOP                     
6C5D: 5E         LD      E,(HL)          
6C5E: 20 F8      JR      NZ,$6C58        
6C60: 08 5C 20   LD      ($205C),SP      
6C63: 08 00 62   LD      ($6200),SP      
6C66: 20 08      JR      NZ,$6C70        
6C68: 08 60 20   LD      ($2060),SP      
6C6B: 00         NOP                     
6C6C: 10 50      STOP    $50             
6C6E: 20 F8      JR      NZ,$6C68        
6C70: 00         NOP                     
6C71: 54         LD      D,H             
6C72: 20 F8      JR      NZ,$6C6C        
6C74: 08 52 20   LD      ($2052),SP      
6C77: 08 00 58   LD      ($5800),SP      
6C7A: 20 08      JR      NZ,$6C84        
6C7C: 08 56 20   LD      ($2056),SP      
6C7F: 00         NOP                     
6C80: F8 50      LDHL    SP,$50          
6C82: 00         NOP                     
6C83: F8 00      LDHL    SP,$00          
6C85: 52         LD      D,D             
6C86: 00         NOP                     
6C87: F8 08      LDHL    SP,$08          
6C89: 54         LD      D,H             
6C8A: 00         NOP                     
6C8B: 08 00 56   LD      ($5600),SP      
6C8E: 00         NOP                     
6C8F: 08 08 58   LD      ($5808),SP      
6C92: 00         NOP                     
6C93: F0 00      LD      A,($00)         
6C95: 76         HALT                    
6C96: 00         NOP                     
6C97: F0 08      LD      A,($08)         
6C99: 76         HALT                    
6C9A: 20 00      JR      NZ,$6C9C        
6C9C: 00         NOP                     
6C9D: 78         LD      A,B             
6C9E: 00         NOP                     
6C9F: 00         NOP                     
6CA0: 08 78 20   LD      ($2078),SP      
6CA3: F0 F1      LD      A,($F1)         
6CA5: 17         RLA                     
6CA6: 17         RLA                     
6CA7: E6 FC      AND     $FC             
6CA9: 5F         LD      E,A             
6CAA: 17         RLA                     
6CAB: 17         RLA                     
6CAC: E6 F0      AND     $F0             
6CAE: 83         ADD     A,E             
6CAF: 5F         LD      E,A             
6CB0: 50         LD      D,B             
6CB1: 21 43 6C   LD      HL,$6C43        
6CB4: 19         ADD     HL,DE           
6CB5: F0 EE      LD      A,($EE)         
6CB7: C6 04      ADD     $04             
6CB9: E0 EE      LDFF00  ($EE),A         
6CBB: 0E 05      LD      C,$05           
6CBD: CD 26 3D   CALL    $3D26           
6CC0: F0 EE      LD      A,($EE)         
6CC2: C6 10      ADD     $10             
6CC4: E0 EE      LDFF00  ($EE),A         
6CC6: 21 93 6C   LD      HL,$6C93        
6CC9: 0E 04      LD      C,$04           
6CCB: CD 26 3D   CALL    $3D26           
6CCE: CD 00 78   CALL    $7800           
6CD1: F0 98      LD      A,($98)         
6CD3: D6 68      SUB     $68             
6CD5: C6 04      ADD     $04             
6CD7: FE 08      CP      $08             
6CD9: 30 2E      JR      NC,$6D09        
6CDB: F0 99      LD      A,($99)         
6CDD: D6 50      SUB     $50             
6CDF: C6 04      ADD     $04             
6CE1: FE 08      CP      $08             
6CE3: 30 24      JR      NC,$6D09        
6CE5: F0 9E      LD      A,($9E)         
6CE7: FE 02      CP      $02             
6CE9: 20 1E      JR      NZ,$6D09        
6CEB: CD 74 78   CALL    $7874           
6CEE: 30 19      JR      NC,$6D09        
6CF0: CD 87 08   CALL    $0887           
6CF3: 20 14      JR      NZ,$6D09        
6CF5: 3E 08      LD      A,$08           
6CF7: EA 95 DB   LD      ($DB95),A       
6CFA: AF         XOR     A               
6CFB: EA 6B C1   LD      ($C16B),A       
6CFE: EA 6C C1   LD      ($C16C),A       
6D01: EA 96 DB   LD      ($DB96),A       
6D04: CD 87 08   CALL    $0887           
6D07: 36 08      LD      (HL),$08        
6D09: CD BA 3D   CALL    $3DBA           
6D0C: C9         RET                     
6D0D: CD 91 08   CALL    $0891           
6D10: 28 04      JR      Z,$6D16         
6D12: 3E 00      LD      A,$00           
6D14: E0 F1      LDFF00  ($F1),A         
6D16: CD D2 6D   CALL    $6DD2           
6D19: CD 00 78   CALL    $7800           
6D1C: 21 80 C3   LD      HL,$C380        
6D1F: 09         ADD     HL,BC           
6D20: F0 E7      LD      A,($E7)         
6D22: 1F         RRA                     
6D23: 1F         RRA                     
6D24: 1F         RRA                     
6D25: E6 01      AND     $01             
6D27: 3C         INC     A               
6D28: 86         ADD     A,(HL)          
6D29: CD 87 3B   CALL    $3B87           
6D2C: CD 6A 79   CALL    $796A           
6D2F: C6 13      ADD     $13             
6D31: FE 26      CP      $26             
6D33: 30 11      JR      NC,$6D46        
6D35: CD 5A 79   CALL    $795A           
6D38: C6 13      ADD     $13             
6D3A: FE 26      CP      $26             
6D3C: 30 08      JR      NC,$6D46        
6D3E: 7B         LD      A,E             
6D3F: CB 27      SET     1,E             
6D41: 21 80 C3   LD      HL,$C380        
6D44: 09         ADD     HL,BC           
6D45: 77         LD      (HL),A          
6D46: CD 4E 78   CALL    $784E           
6D49: 30 22      JR      NC,$6D6D        
6D4B: 21 D0 C3   LD      HL,$C3D0        
6D4E: 09         ADD     HL,BC           
6D4F: 7E         LD      A,(HL)          
6D50: 34         INC     (HL)            
6D51: E6 01      AND     $01             
6D53: 28 12      JR      Z,$6D67         
6D55: 1E AF      LD      E,$AF           
6D57: CD ED 27   CALL    $27ED           
6D5A: E6 3F      AND     $3F             
6D5C: 28 0B      JR      Z,$6D69         
6D5E: 1E FB      LD      E,$FB           
6D60: CD ED 27   CALL    $27ED           
6D63: E6 07      AND     $07             
6D65: 28 02      JR      Z,$6D69         
6D67: 1E FA      LD      E,$FA           
6D69: 7B         LD      A,E             
6D6A: CD 97 21   CALL    $2197           
6D6D: C9         RET                     
6D6E: F4                              
6D6F: 00         NOP                     
6D70: 64         LD      H,H             
6D71: 00         NOP                     
6D72: F4                              
6D73: 08 66 00   LD      ($0066),SP      
6D76: 04         INC     B               
6D77: 00         NOP                     
6D78: 68         LD      L,B             
6D79: 00         NOP                     
6D7A: 04         INC     B               
6D7B: 08 6A 00   LD      ($006A),SP      
6D7E: FF         RST     0X38            
6D7F: FF         RST     0X38            
6D80: FF         RST     0X38            
6D81: FF         RST     0X38            
6D82: 04         INC     B               
6D83: F8 70      LDHL    SP,$70          
6D85: 00         NOP                     
6D86: F4                              
6D87: 00         NOP                     
6D88: 6C         LD      L,H             
6D89: 00         NOP                     
6D8A: F4                              
6D8B: 08 6E 00   LD      ($006E),SP      
6D8E: 04         INC     B               
6D8F: 00         NOP                     
6D90: 72         LD      (HL),D          
6D91: 00         NOP                     
6D92: 04         INC     B               
6D93: 08 74 00   LD      ($0074),SP      
6D96: 04         INC     B               
6D97: F8 7A      LDHL    SP,$7A          
6D99: 00         NOP                     
6D9A: F4                              
6D9B: 00         NOP                     
6D9C: 6C         LD      L,H             
6D9D: 00         NOP                     
6D9E: F4                              
6D9F: 08 6E 00   LD      ($006E),SP      
6DA2: 04         INC     B               
6DA3: 00         NOP                     
6DA4: 7C         LD      A,H             
6DA5: 00         NOP                     
6DA6: 04         INC     B               
6DA7: 08 74 00   LD      ($0074),SP      
6DAA: 04         INC     B               
6DAB: 10 70      STOP    $70             
6DAD: 20 F4      JR      NZ,$6DA3        
6DAF: 00         NOP                     
6DB0: 6E         LD      L,(HL)          
6DB1: 20 F4      JR      NZ,$6DA7        
6DB3: 08 6C 20   LD      ($206C),SP      
6DB6: 04         INC     B               
6DB7: 00         NOP                     
6DB8: 74         LD      (HL),H          
6DB9: 20 04      JR      NZ,$6DBF        
6DBB: 08 72 20   LD      ($2072),SP      
6DBE: 04         INC     B               
6DBF: 10 7A      STOP    $7A             
6DC1: 20 F4      JR      NZ,$6DB7        
6DC3: 00         NOP                     
6DC4: 6E         LD      L,(HL)          
6DC5: 20 F4      JR      NZ,$6DBB        
6DC7: 08 6C 20   LD      ($206C),SP      
6DCA: 04         INC     B               
6DCB: 00         NOP                     
6DCC: 74         LD      (HL),H          
6DCD: 20 04      JR      NZ,$6DD3        
6DCF: 08 7C 20   LD      ($207C),SP      
6DD2: F0 F1      LD      A,($F1)         
6DD4: 17         RLA                     
6DD5: 17         RLA                     
6DD6: E6 FC      AND     $FC             
6DD8: 5F         LD      E,A             
6DD9: 17         RLA                     
6DDA: 17         RLA                     
6DDB: E6 F0      AND     $F0             
6DDD: 83         ADD     A,E             
6DDE: 5F         LD      E,A             
6DDF: 50         LD      D,B             
6DE0: 21 6E 6D   LD      HL,$6D6E        
6DE3: 19         ADD     HL,DE           
6DE4: 0E 05      LD      C,$05           
6DE6: CD 26 3D   CALL    $3D26           
6DE9: C9         RET                     
6DEA: 00         NOP                     
6DEB: 06 0C      LD      B,$0C           
6DED: 13         INC     DE              
6DEE: 19         ADD     HL,DE           
6DEF: 20 26      JR      NZ,$6E17        
6DF1: 2C         INC     L               
6DF2: 33         INC     SP              
6DF3: 39         ADD     HL,SP           
6DF4: 00         NOP                     
6DF5: 00         NOP                     
6DF6: 00         NOP                     
6DF7: 00         NOP                     
6DF8: 00         NOP                     
6DF9: 00         NOP                     
6DFA: 40         LD      B,B             
6DFB: 43         LD      B,E             
6DFC: 46         LD      B,(HL)          
6DFD: 49         LD      C,C             
6DFE: 4C         LD      C,H             
6DFF: 4F         LD      C,A             
6E00: 52         LD      D,D             
6E01: 55         LD      D,L             
6E02: 58         LD      E,B             
6E03: 5C         LD      E,H             
6E04: 00         NOP                     
6E05: 00         NOP                     
6E06: 00         NOP                     
6E07: 00         NOP                     
6E08: 00         NOP                     
6E09: 00         NOP                     
6E0A: 60         LD      H,B             
6E0B: 60         LD      H,B             
6E0C: 60         LD      H,B             
6E0D: 60         LD      H,B             
6E0E: 60         LD      H,B             
6E0F: 60         LD      H,B             
6E10: 60         LD      H,B             
6E11: 60         LD      H,B             
6E12: 60         LD      H,B             
6E13: 21 B0 C2   LD      HL,$C2B0        
6E16: 09         ADD     HL,BC           
6E17: 7E         LD      A,(HL)          
6E18: FE 02      CP      $02             
6E1A: CA 77 74   JP      Z,$7477         
6E1D: A7         AND     A               
6E1E: C2 CA 70   JP      NZ,$70CA        
6E21: F0 98      LD      A,($98)         
6E23: FE 38      CP      $38             
6E25: 30 12      JR      NC,$6E39        
6E27: FE 20      CP      $20             
6E29: 38 0E      JR      C,$6E39         
6E2B: 21 1E C1   LD      HL,$C11E        
6E2E: CB FE      SET     1,E             
6E30: FE 24      CP      $24             
6E32: 38 05      JR      C,$6E39         
6E34: 21 1D C1   LD      HL,$C11D        
6E37: CB FE      SET     1,E             
6E39: FA 0F DB   LD      A,($DB0F)       
6E3C: A7         AND     A               
6E3D: C8         RET     Z               
6E3E: 5F         LD      E,A             
6E3F: 50         LD      D,B             
6E40: 21 EA 6D   LD      HL,$6DEA        
6E43: 19         ADD     HL,DE           
6E44: 7E         LD      A,(HL)          
6E45: E0 E8      LDFF00  ($E8),A         
6E47: F0 F8      LD      A,($F8)         
6E49: E6 10      AND     $10             
6E4B: CD AD 6F   CALL    $6FAD           
6E4E: F0 F0      LD      A,($F0)         
6E50: C7         RST     0X00            
6E51: 61         LD      H,C             
6E52: 6E         LD      L,(HL)          
6E53: 76         HALT                    
6E54: 6E         LD      L,(HL)          
6E55: 83         ADD     A,E             
6E56: 6E         LD      L,(HL)          
6E57: BC         CP      H               
6E58: 6E         LD      L,(HL)          
6E59: 23         INC     HL              
6E5A: 6F         LD      L,A             
6E5B: 5A         LD      E,D             
6E5C: 6F         LD      L,A             
6E5D: 5B         LD      E,E             
6E5E: 6F         LD      L,A             
6E5F: 98         SBC     B               
6E60: 6F         LD      L,A             
6E61: F0 98      LD      A,($98)         
6E63: FE 3C      CP      $3C             
6E65: 38 0E      JR      C,$6E75         
6E67: CD 95 14   CALL    $1495           
6E6A: CD 3B 09   CALL    $093B           
6E6D: CD 8D 3B   CALL    $3B8D           
6E70: CD 91 08   CALL    $0891           
6E73: 36 58      LD      (HL),$58        
6E75: C9         RET                     
6E76: 3E 01      LD      A,$01           
6E78: EA 67 C1   LD      ($C167),A       
6E7B: FA 46 C1   LD      A,($C146)       
6E7E: A7         AND     A               
6E7F: CA 8D 3B   JP      Z,$3B8D         
6E82: C9         RET                     
6E83: 3E 02      LD      A,$02           
6E85: E0 A1      LDFF00  ($A1),A         
6E87: CD 91 08   CALL    $0891           
6E8A: C0         RET     NZ              
6E8B: 21 D0 C3   LD      HL,$C3D0        
6E8E: 09         ADD     HL,BC           
6E8F: F0 E8      LD      A,($E8)         
6E91: 96         SUB     (HL)            
6E92: 30 07      JR      NC,$6E9B        
6E94: F0 E8      LD      A,($E8)         
6E96: 77         LD      (HL),A          
6E97: CD 8D 3B   CALL    $3B8D           
6E9A: C9         RET                     
6E9B: 5F         LD      E,A             
6E9C: F0 E7      LD      A,($E7)         
6E9E: E6 03      AND     $03             
6EA0: 20 19      JR      NZ,$6EBB        
6EA2: CD ED 27   CALL    $27ED           
6EA5: E6 01      AND     $01             
6EA7: 20 12      JR      NZ,$6EBB        
6EA9: 7B         LD      A,E             
6EAA: 1F         RRA                     
6EAB: 1F         RRA                     
6EAC: 1F         RRA                     
6EAD: 1F         RRA                     
6EAE: E6 0F      AND     $0F             
6EB0: A7         AND     A               
6EB1: 20 02      JR      NZ,$6EB5        
6EB3: 3E 01      LD      A,$01           
6EB5: 86         ADD     A,(HL)          
6EB6: 77         LD      (HL),A          
6EB7: 3E 06      LD      A,$06           
6EB9: E0 F3      LDFF00  ($F3),A         
6EBB: C9         RET                     
6EBC: 3E 02      LD      A,$02           
6EBE: E0 A1      LDFF00  ($A1),A         
6EC0: EA 67 C1   LD      ($C167),A       
6EC3: FA 0F DB   LD      A,($DB0F)       
6EC6: FE 20      CP      $20             
6EC8: 38 20      JR      C,$6EEA         
6ECA: CD 91 08   CALL    $0891           
6ECD: 36 40      LD      (HL),$40        
6ECF: CD 8D 3B   CALL    $3B8D           
6ED2: CD 1C 75   CALL    $751C           
6ED5: 21 C0 C2   LD      HL,$C2C0        
6ED8: 09         ADD     HL,BC           
6ED9: 36 01      LD      (HL),$01        
6EDB: 3E 56      LD      A,$56           
6EDD: EA 68 D3   LD      ($D368),A       
6EE0: AF         XOR     A               
6EE1: EA 67 C1   LD      ($C167),A       
6EE4: CD 8C 08   CALL    $088C           
6EE7: 36 3F      LD      (HL),$3F        
6EE9: C9         RET                     
6EEA: 21 E9 DA   LD      HL,$DAE9        
6EED: FE 05      CP      $05             
6EEF: 20 10      JR      NZ,$6F01        
6EF1: CB 6E      SET     1,E             
6EF3: 20 20      JR      NZ,$6F15        
6EF5: CD 8D 3B   CALL    $3B8D           
6EF8: 36 06      LD      (HL),$06        
6EFA: 3E 23      LD      A,$23           
6EFC: E0 F2      LDFF00  ($F2),A         
6EFE: C3 E0 6E   JP      $6EE0           
6F01: FE 10      CP      $10             
6F03: 20 10      JR      NZ,$6F15        
6F05: CB 76      SET     1,E             
6F07: 20 0C      JR      NZ,$6F15        
6F09: CD 8D 3B   CALL    $3B8D           
6F0C: 36 06      LD      (HL),$06        
6F0E: 3E 23      LD      A,$23           
6F10: E0 F2      LDFF00  ($F2),A         
6F12: C3 E0 6E   JP      $6EE0           
6F15: 3E 1D      LD      A,$1D           
6F17: E0 F2      LDFF00  ($F2),A         
6F19: CD 8D 3B   CALL    $3B8D           
6F1C: 36 05      LD      (HL),$05        
6F1E: AF         XOR     A               
6F1F: EA 67 C1   LD      ($C167),A       
6F22: C9         RET                     
6F23: 3E 02      LD      A,$02           
6F25: E0 A1      LDFF00  ($A1),A         
6F27: EA 67 C1   LD      ($C167),A       
6F2A: CD 91 08   CALL    $0891           
6F2D: FE 3E      CP      $3E             
6F2F: 20 05      JR      NZ,$6F36        
6F31: 21 F2 FF   LD      HL,$FFF2        
6F34: 36 23      LD      (HL),$23        
6F36: A7         AND     A               
6F37: 20 20      JR      NZ,$6F59        
6F39: 3E CF      LD      A,$CF           
6F3B: CD 01 3C   CALL    $3C01           
6F3E: 21 00 C2   LD      HL,$C200        
6F41: 19         ADD     HL,DE           
6F42: 36 50      LD      (HL),$50        
6F44: 21 10 C2   LD      HL,$C210        
6F47: 19         ADD     HL,DE           
6F48: 36 48      LD      (HL),$48        
6F4A: 21 B0 C2   LD      HL,$C2B0        
6F4D: 19         ADD     HL,DE           
6F4E: 36 01      LD      (HL),$01        
6F50: 21 E0 C2   LD      HL,$C2E0        
6F53: 19         ADD     HL,DE           
6F54: 36 4F      LD      (HL),$4F        
6F56: CD 8D 3B   CALL    $3B8D           
6F59: C9         RET                     
6F5A: C9         RET                     
6F5B: CD 8C 08   CALL    $088C           
6F5E: 20 37      JR      NZ,$6F97        
6F60: CD 8D 3B   CALL    $3B8D           
6F63: 3E CF      LD      A,$CF           
6F65: CD 01 3C   CALL    $3C01           
6F68: 21 00 C2   LD      HL,$C200        
6F6B: 19         ADD     HL,DE           
6F6C: 36 50      LD      (HL),$50        
6F6E: 21 10 C2   LD      HL,$C210        
6F71: 19         ADD     HL,DE           
6F72: 36 48      LD      (HL),$48        
6F74: 21 B0 C2   LD      HL,$C2B0        
6F77: 19         ADD     HL,DE           
6F78: 36 02      LD      (HL),$02        
6F7A: 21 E0 C2   LD      HL,$C2E0        
6F7D: 19         ADD     HL,DE           
6F7E: 36 14      LD      (HL),$14        
6F80: 3E 02      LD      A,$02           
6F82: CD 01 3C   CALL    $3C01           
6F85: 21 00 C2   LD      HL,$C200        
6F88: 19         ADD     HL,DE           
6F89: 36 50      LD      (HL),$50        
6F8B: 21 10 C2   LD      HL,$C210        
6F8E: 19         ADD     HL,DE           
6F8F: 36 48      LD      (HL),$48        
6F91: 21 E0 C2   LD      HL,$C2E0        
6F94: 19         ADD     HL,DE           
6F95: 36 20      LD      (HL),$20        
6F97: C9         RET                     
6F98: C9         RET                     
6F99: 50         LD      D,B             
6F9A: 00         NOP                     
6F9B: 50         LD      D,B             
6F9C: 20 3C      JR      NZ,$6FDA        
6F9E: 00         NOP                     
6F9F: 3C         INC     A               
6FA0: 20 3A      JR      NZ,$6FDC        
6FA2: 00         NOP                     
6FA3: 3A         LD      A,(HLD)         
6FA4: 20 1E      JR      NZ,$6FC4        
6FA6: 00         NOP                     
6FA7: 1E 60      LD      E,$60           
6FA9: 1E 10      LD      E,$10           
6FAB: 1E 70      LD      E,$70           
6FAD: 21 C0 C2   LD      HL,$C2C0        
6FB0: 09         ADD     HL,BC           
6FB1: 7E         LD      A,(HL)          
6FB2: A7         AND     A               
6FB3: 20 29      JR      NZ,$6FDE        
6FB5: 3E 88      LD      A,$88           
6FB7: E0 EE      LDFF00  ($EE),A         
6FB9: 3E 80      LD      A,$80           
6FBB: E0 EC      LDFF00  ($EC),A         
6FBD: 11 99 6F   LD      DE,$6F99        
6FC0: CD 3B 3C   CALL    $3C3B           
6FC3: 21 D0 C3   LD      HL,$C3D0        
6FC6: 09         ADD     HL,BC           
6FC7: 7E         LD      A,(HL)          
6FC8: 5F         LD      E,A             
6FC9: 3E 80      LD      A,$80           
6FCB: 93         SUB     E               
6FCC: E0 EC      LDFF00  ($EC),A         
6FCE: 11 99 6F   LD      DE,$6F99        
6FD1: CD 3B 3C   CALL    $3C3B           
6FD4: F0 EC      LD      A,($EC)         
6FD6: C6 10      ADD     $10             
6FD8: E0 EC      LDFF00  ($EC),A         
6FDA: FE 80      CP      $80             
6FDC: 38 F0      JR      C,$6FCE         
6FDE: CD 8C 08   CALL    $088C           
6FE1: 28 26      JR      Z,$7009         
6FE3: 1F         RRA                     
6FE4: 1F         RRA                     
6FE5: 1F         RRA                     
6FE6: E6 03      AND     $03             
6FE8: E0 F1      LDFF00  ($F1),A         
6FEA: 21 D0 C3   LD      HL,$C3D0        
6FED: 09         ADD     HL,BC           
6FEE: 7E         LD      A,(HL)          
6FEF: 5F         LD      E,A             
6FF0: 3E 80      LD      A,$80           
6FF2: 93         SUB     E               
6FF3: E0 EC      LDFF00  ($EC),A         
6FF5: 3E 78      LD      A,$78           
6FF7: E0 EE      LDFF00  ($EE),A         
6FF9: 11 9D 6F   LD      DE,$6F9D        
6FFC: CD 3B 3C   CALL    $3C3B           
6FFF: 3E 98      LD      A,$98           
7001: E0 EE      LDFF00  ($EE),A         
7003: 11 9D 6F   LD      DE,$6F9D        
7006: CD 3B 3C   CALL    $3C3B           
7009: C9         RET                     
700A: D8         RET     C               
700B: E8 7C      ADD     SP,$7C          
700D: 40         LD      B,B             
700E: D8         RET     C               
700F: F0 7C      LD      A,($7C)         
7011: 20 E8      JR      NZ,$6FFB        
7013: E8 7C      ADD     SP,$7C          
7015: 00         NOP                     
7016: E8 F0      ADD     SP,$F0          
7018: 7C         LD      A,H             
7019: 60         LD      H,B             
701A: F8 F8      LDHL    SP,$F8          
701C: 7C         LD      A,H             
701D: 00         NOP                     
701E: F8 00      LDHL    SP,$00          
7020: 7C         LD      A,H             
7021: 60         LD      H,B             
7022: 08 08 7C   LD      ($7C08),SP      
7025: 00         NOP                     
7026: 08 10 7C   LD      ($7C10),SP      
7029: 60         LD      H,B             
702A: 18 18      JR      $7044           
702C: 7C         LD      A,H             
702D: 00         NOP                     
702E: 18 20      JR      $7050           
7030: 7C         LD      A,H             
7031: 60         LD      H,B             
7032: 28 18      JR      Z,$704C         
7034: 7C         LD      A,H             
7035: 40         LD      B,B             
7036: 28 20      JR      Z,$7058         
7038: 7C         LD      A,H             
7039: 20 D8      JR      NZ,$7013        
703B: F8 7C      LDHL    SP,$7C          
703D: 00         NOP                     
703E: D8         RET     C               
703F: 00         NOP                     
7040: 7C         LD      A,H             
7041: 60         LD      H,B             
7042: E8 08      ADD     SP,$08          
7044: 7C         LD      A,H             
7045: 00         NOP                     
7046: E8 10      ADD     SP,$10          
7048: 7C         LD      A,H             
7049: 60         LD      H,B             
704A: F8 08      LDHL    SP,$08          
704C: 7C         LD      A,H             
704D: 40         LD      B,B             
704E: F8 10      LDHL    SP,$10          
7050: 7C         LD      A,H             
7051: 20 08      JR      NZ,$705B        
7053: F8 7C      LDHL    SP,$7C          
7055: 40         LD      B,B             
7056: 08 00 7C   LD      ($7C00),SP      
7059: 20 18      JR      NZ,$7073        
705B: F8 7C      LDHL    SP,$7C          
705D: 00         NOP                     
705E: 18 00      JR      $7060           
7060: 7C         LD      A,H             
7061: 60         LD      H,B             
7062: 28 08      JR      Z,$706C         
7064: 7C         LD      A,H             
7065: 00         NOP                     
7066: 28 10      JR      Z,$7078         
7068: 7C         LD      A,H             
7069: 60         LD      H,B             
706A: D8         RET     C               
706B: 08 7C 40   LD      ($407C),SP      
706E: D8         RET     C               
706F: 10 7C      STOP    $7C             
7071: 20 E8      JR      NZ,$705B        
7073: F8 7C      LDHL    SP,$7C          
7075: 40         LD      B,B             
7076: E8 00      ADD     SP,$00          
7078: 7C         LD      A,H             
7079: 20 F8      JR      NZ,$7073        
707B: F8 7C      LDHL    SP,$7C          
707D: 00         NOP                     
707E: F8 00      LDHL    SP,$00          
7080: 7C         LD      A,H             
7081: 60         LD      H,B             
7082: 08 08 7C   LD      ($7C08),SP      
7085: 00         NOP                     
7086: 08 10 7C   LD      ($7C10),SP      
7089: 60         LD      H,B             
708A: 18 08      JR      $7094           
708C: 7C         LD      A,H             
708D: 40         LD      B,B             
708E: 18 10      JR      $70A0           
7090: 7C         LD      A,H             
7091: 20 28      JR      NZ,$70BB        
7093: F8 7C      LDHL    SP,$7C          
7095: 40         LD      B,B             
7096: 28 00      JR      Z,$7098         
7098: 7C         LD      A,H             
7099: 20 D8      JR      NZ,$7073        
709B: 18 7C      JR      $7119           
709D: 00         NOP                     
709E: D8         RET     C               
709F: 20 7C      JR      NZ,$711D        
70A1: 60         LD      H,B             
70A2: E8 18      ADD     SP,$18          
70A4: 7C         LD      A,H             
70A5: 40         LD      B,B             
70A6: E8 20      ADD     SP,$20          
70A8: 7C         LD      A,H             
70A9: 20 F8      JR      NZ,$70A3        
70AB: 08 7C 40   LD      ($407C),SP      
70AE: F8 10      LDHL    SP,$10          
70B0: 7C         LD      A,H             
70B1: 20 08      JR      NZ,$70BB        
70B3: F8 7C      LDHL    SP,$7C          
70B5: 40         LD      B,B             
70B6: 08 00 7C   LD      ($7C00),SP      
70B9: 20 18      JR      NZ,$70D3        
70BB: E8 7C      ADD     SP,$7C          
70BD: 40         LD      B,B             
70BE: 18 F0      JR      $70B0           
70C0: 7C         LD      A,H             
70C1: 20 28      JR      NZ,$70EB        
70C3: E8 7C      ADD     SP,$7C          
70C5: 00         NOP                     
70C6: 28 F0      JR      Z,$70B8         
70C8: 7C         LD      A,H             
70C9: 60         LD      H,B             
70CA: F0 F0      LD      A,($F0)         
70CC: C7         RST     0X00            
70CD: DD                              
70CE: 70         LD      (HL),B          
70CF: 04         INC     B               
70D0: 71         LD      (HL),C          
70D1: 63         LD      H,E             
70D2: 71         LD      (HL),C          
70D3: 35         DEC     (HL)            
70D4: 72         LD      (HL),D          
70D5: 71         LD      (HL),C          
70D6: 72         LD      (HL),D          
70D7: A7         AND     A               
70D8: 72         LD      (HL),D          
70D9: C1         POP     BC              
70DA: 72         LD      (HL),D          
70DB: 3B         DEC     SP              
70DC: 73         LD      (HL),E          
70DD: 3E 02      LD      A,$02           
70DF: E0 A1      LDFF00  ($A1),A         
70E1: EA 67 C1   LD      ($C167),A       
70E4: CD 91 08   CALL    $0891           
70E7: 28 13      JR      Z,$70FC         
70E9: FE 30      CP      $30             
70EB: D8         RET     C               
70EC: D6 30      SUB     $30             
70EE: 1F         RRA                     
70EF: 1F         RRA                     
70F0: 1F         RRA                     
70F1: E6 03      AND     $03             
70F3: E0 F1      LDFF00  ($F1),A         
70F5: 11 9D 6F   LD      DE,$6F9D        
70F8: CD 3B 3C   CALL    $3C3B           
70FB: C9         RET                     
70FC: CD 91 08   CALL    $0891           
70FF: 36 A0      LD      (HL),$A0        
7101: C3 8D 3B   JP      $3B8D           
7104: 3E 02      LD      A,$02           
7106: E0 A1      LDFF00  ($A1),A         
7108: EA 67 C1   LD      ($C167),A       
710B: CD 91 08   CALL    $0891           
710E: 20 09      JR      NZ,$7119        
7110: 36 FF      LD      (HL),$FF        
7112: 3E 1E      LD      A,$1E           
7114: E0 F3      LDFF00  ($F3),A         
7116: CD 8D 3B   CALL    $3B8D           
7119: CD 91 08   CALL    $0891           
711C: E6 04      AND     $04             
711E: 1E E4      LD      E,$E4           
7120: 28 02      JR      Z,$7124         
7122: 1E 84      LD      E,$84           
7124: 7B         LD      A,E             
7125: EA 97 DB   LD      ($DB97),A       
7128: F0 E7      LD      A,($E7)         
712A: E6 07      AND     $07             
712C: 20 0C      JR      NZ,$713A        
712E: 3E 33      LD      A,$33           
7130: E0 F4      LDFF00  ($F4),A         
7132: CD ED 27   CALL    $27ED           
7135: E6 03      AND     $03             
7137: CD 87 3B   CALL    $3B87           
713A: F0 E7      LD      A,($E7)         
713C: 21 20 C4   LD      HL,$C420        
713F: 09         ADD     HL,BC           
7140: 77         LD      (HL),A          
7141: F0 F1      LD      A,($F1)         
7143: 17         RLA                     
7144: 17         RLA                     
7145: 17         RLA                     
7146: 17         RLA                     
7147: E6 F0      AND     $F0             
7149: 5F         LD      E,A             
714A: 17         RLA                     
714B: E6 E0      AND     $E0             
714D: 83         ADD     A,E             
714E: 5F         LD      E,A             
714F: 50         LD      D,B             
7150: 21 0A 70   LD      HL,$700A        
7153: 19         ADD     HL,DE           
7154: 0E 0C      LD      C,$0C           
7156: CD 26 3D   CALL    $3D26           
7159: 3E 0A      LD      A,$0A           
715B: CD D0 3D   CALL    $3DD0           
715E: C9         RET                     
715F: 7A         LD      A,D             
7160: 00         NOP                     
7161: 7A         LD      A,D             
7162: 20 3E      JR      NZ,$71A2        
7164: 02         LD      (BC),A          
7165: E0 A1      LDFF00  ($A1),A         
7167: EA 67 C1   LD      ($C167),A       
716A: CD 19 71   CALL    $7119           
716D: CD 91 08   CALL    $0891           
7170: 20 08      JR      NZ,$717A        
7172: CD 87 08   CALL    $0887           
7175: 36 28      LD      (HL),$28        
7177: C3 8D 3B   JP      $3B8D           
717A: FE 50      CP      $50             
717C: 30 0D      JR      NC,$718B        
717E: 21 15 72   LD      HL,$7215        
7181: 0E 08      LD      C,$08           
7183: CD 26 3D   CALL    $3D26           
7186: 3E 06      LD      A,$06           
7188: C3 D0 3D   JP      $3DD0           
718B: AF         XOR     A               
718C: E0 F1      LDFF00  ($F1),A         
718E: 11 5F 71   LD      DE,$715F        
7191: CD 3B 3C   CALL    $3C3B           
7194: C9         RET                     
7195: F8 00      LDHL    SP,$00          
7197: 6E         LD      L,(HL)          
7198: 00         NOP                     
7199: F8 08      LDHL    SP,$08          
719B: 6E         LD      L,(HL)          
719C: 20 F8      JR      NZ,$7196        
719E: 00         NOP                     
719F: 6E         LD      L,(HL)          
71A0: 00         NOP                     
71A1: F8 08      LDHL    SP,$08          
71A3: 6E         LD      L,(HL)          
71A4: 20 08      JR      NZ,$71AE        
71A6: 00         NOP                     
71A7: 70         LD      (HL),B          
71A8: 00         NOP                     
71A9: 08 08 70   LD      ($7008),SP      
71AC: 20 08      JR      NZ,$71B6        
71AE: 00         NOP                     
71AF: 70         LD      (HL),B          
71B0: 00         NOP                     
71B1: 08 08 70   LD      ($7008),SP      
71B4: 20 F8      JR      NZ,$71AE        
71B6: F8 68      LDHL    SP,$68          
71B8: 00         NOP                     
71B9: F8 00      LDHL    SP,$00          
71BB: 6A         LD      L,D             
71BC: 00         NOP                     
71BD: F8 08      LDHL    SP,$08          
71BF: 6A         LD      L,D             
71C0: 20 F8      JR      NZ,$71BA        
71C2: 10 68      STOP    $68             
71C4: 20 08      JR      NZ,$71CE        
71C6: 00         NOP                     
71C7: 6C         LD      L,H             
71C8: 00         NOP                     
71C9: 08 08 6C   LD      ($6C08),SP      
71CC: 20 08      JR      NZ,$71D6        
71CE: 00         NOP                     
71CF: 6C         LD      L,H             
71D0: 00         NOP                     
71D1: 08 08 6C   LD      ($6C08),SP      
71D4: 20 F8      JR      NZ,$71CE        
71D6: F8 62      LDHL    SP,$62          
71D8: 00         NOP                     
71D9: F8 00      LDHL    SP,$00          
71DB: 64         LD      H,H             
71DC: 00         NOP                     
71DD: F8 08      LDHL    SP,$08          
71DF: 64         LD      H,H             
71E0: 20 F8      JR      NZ,$71DA        
71E2: 10 62      STOP    $62             
71E4: 20 08      JR      NZ,$71EE        
71E6: 00         NOP                     
71E7: 66         LD      H,(HL)          
71E8: 00         NOP                     
71E9: 08 08 66   LD      ($6608),SP      
71EC: 20 08      JR      NZ,$71F6        
71EE: 00         NOP                     
71EF: 66         LD      H,(HL)          
71F0: 00         NOP                     
71F1: 08 08 66   LD      ($6608),SP      
71F4: 20 F8      JR      NZ,$71EE        
71F6: F8 5A      LDHL    SP,$5A          
71F8: 00         NOP                     
71F9: F8 00      LDHL    SP,$00          
71FB: 5C         LD      E,H             
71FC: 00         NOP                     
71FD: F8 08      LDHL    SP,$08          
71FF: 5C         LD      E,H             
7200: 20 F8      JR      NZ,$71FA        
7202: 10 5A      STOP    $5A             
7204: 20 08      JR      NZ,$720E        
7206: F8 5E      LDHL    SP,$5E          
7208: 00         NOP                     
7209: 08 00 60   LD      ($6000),SP      
720C: 00         NOP                     
720D: 08 08 60   LD      ($6008),SP      
7210: 20 08      JR      NZ,$721A        
7212: 10 5E      STOP    $5E             
7214: 20 F8      JR      NZ,$720E        
7216: F8 56      LDHL    SP,$56          
7218: 00         NOP                     
7219: F8 00      LDHL    SP,$00          
721B: 58         LD      E,B             
721C: 00         NOP                     
721D: F8 08      LDHL    SP,$08          
721F: 58         LD      E,B             
7220: 20 F8      JR      NZ,$721A        
7222: 10 56      STOP    $56             
7224: 20 08      JR      NZ,$722E        
7226: F8 56      LDHL    SP,$56          
7228: 40         LD      B,B             
7229: 08 00 58   LD      ($5800),SP      
722C: 40         LD      B,B             
722D: 08 08 58   LD      ($5808),SP      
7230: 60         LD      H,B             
7231: 08 10 56   LD      ($5610),SP      
7234: 60         LD      H,B             
7235: 3E 02      LD      A,$02           
7237: E0 A1      LDFF00  ($A1),A         
7239: EA 67 C1   LD      ($C167),A       
723C: F0 E7      LD      A,($E7)         
723E: E6 0F      AND     $0F             
7240: F6 20      OR      $20             
7242: 21 20 C4   LD      HL,$C420        
7245: 09         ADD     HL,BC           
7246: 77         LD      (HL),A          
7247: CD 87 08   CALL    $0887           
724A: 20 03      JR      NZ,$724F        
724C: C3 8D 3B   JP      $3B8D           
724F: 1F         RRA                     
7250: 1F         RRA                     
7251: E6 0F      AND     $0F             
7253: FE 04      CP      $04             
7255: 38 02      JR      C,$7259         
7257: 3E 04      LD      A,$04           
7259: 17         RLA                     
725A: 17         RLA                     
725B: 17         RLA                     
725C: 17         RLA                     
725D: 17         RLA                     
725E: E6 E0      AND     $E0             
7260: 5F         LD      E,A             
7261: 50         LD      D,B             
7262: 21 95 71   LD      HL,$7195        
7265: 19         ADD     HL,DE           
7266: 0E 08      LD      C,$08           
7268: CD 26 3D   CALL    $3D26           
726B: 3E 06      LD      A,$06           
726D: CD D0 3D   CALL    $3DD0           
7270: C9         RET                     
7271: 3E 02      LD      A,$02           
7273: E0 A1      LDFF00  ($A1),A         
7275: EA 67 C1   LD      ($C167),A       
7278: CD EB 74   CALL    $74EB           
727B: CD 0A 79   CALL    $790A           
727E: 21 50 C2   LD      HL,$C250        
7281: 09         ADD     HL,BC           
7282: 34         INC     (HL)            
7283: 7E         LD      A,(HL)          
7284: E6 80      AND     $80             
7286: 20 1E      JR      NZ,$72A6        
7288: 21 10 C2   LD      HL,$C210        
728B: 09         ADD     HL,BC           
728C: 7E         LD      A,(HL)          
728D: FE 70      CP      $70             
728F: 38 15      JR      C,$72A6         
7291: 36 70      LD      (HL),$70        
7293: 3E 17      LD      A,$17           
7295: E0 F4      LDFF00  ($F4),A         
7297: 21 50 C2   LD      HL,$C250        
729A: 09         ADD     HL,BC           
729B: 7E         LD      A,(HL)          
729C: FE 04      CP      $04             
729E: DA 8D 3B   JP      C,$3B8D         
72A1: 2F         CPL                     
72A2: 3C         INC     A               
72A3: CB 2F      SET     1,E             
72A5: 77         LD      (HL),A          
72A6: C9         RET                     
72A7: AF         XOR     A               
72A8: EA 67 C1   LD      ($C167),A       
72AB: CD EB 74   CALL    $74EB           
72AE: CD D5 3B   CALL    $3BD5           
72B1: 30 0D      JR      NC,$72C0        
72B3: CD 8D 3B   CALL    $3B8D           
72B6: 3E 0F      LD      A,$0F           
72B8: EA 68 D3   LD      ($D368),A       
72BB: CD 91 08   CALL    $0891           
72BE: 36 FF      LD      (HL),$FF        
72C0: C9         RET                     
72C1: CD 91 08   CALL    $0891           
72C4: E6 08      AND     $08             
72C6: 1E E4      LD      E,$E4           
72C8: 28 02      JR      Z,$72CC         
72CA: 1E 84      LD      E,$84           
72CC: 7B         LD      A,E             
72CD: EA 97 DB   LD      ($DB97),A       
72D0: CD 91 08   CALL    $0891           
72D3: 20 2A      JR      NZ,$72FF        
72D5: 36 20      LD      (HL),$20        
72D7: 3E 10      LD      A,$10           
72D9: EA 68 D3   LD      ($D368),A       
72DC: 3E 9F      LD      A,$9F           
72DE: CD 97 21   CALL    $2197           
72E1: FA E9 DA   LD      A,($DAE9)       
72E4: F6 10      OR      $10             
72E6: EA E9 DA   LD      ($DAE9),A       
72E9: E0 F8      LDFF00  ($F8),A         
72EB: 3E 02      LD      A,$02           
72ED: EA 4E DB   LD      ($DB4E),A       
72F0: 3E FF      LD      A,$FF           
72F2: EA 93 DB   LD      ($DB93),A       
72F5: AF         XOR     A               
72F6: EA 0F DB   LD      ($DB0F),A       
72F9: EA 67 C1   LD      ($C167),A       
72FC: CD 8D 3B   CALL    $3B8D           
72FF: F0 98      LD      A,($98)         
7301: 21 00 C2   LD      HL,$C200        
7304: 09         ADD     HL,BC           
7305: D6 04      SUB     $04             
7307: 77         LD      (HL),A          
7308: F0 99      LD      A,($99)         
730A: 21 10 C2   LD      HL,$C210        
730D: 09         ADD     HL,BC           
730E: D6 13      SUB     $13             
7310: 77         LD      (HL),A          
7311: CD BA 3D   CALL    $3DBA           
7314: F0 A2      LD      A,($A2)         
7316: 21 10 C3   LD      HL,$C310        
7319: 09         ADD     HL,BC           
731A: 77         LD      (HL),A          
731B: 3E 6B      LD      A,$6B           
731D: E0 9D      LDFF00  ($9D),A         
731F: 3E 02      LD      A,$02           
7321: E0 A1      LDFF00  ($A1),A         
7323: 3E 03      LD      A,$03           
7325: E0 9E      LDFF00  ($9E),A         
7327: AF         XOR     A               
7328: EA 37 C1   LD      ($C137),A       
732B: EA 6A C1   LD      ($C16A),A       
732E: EA 22 C1   LD      ($C122),A       
7331: EA 21 C1   LD      ($C121),A       
7334: CD 48 74   CALL    $7448           
7337: CD E6 74   CALL    $74E6           
733A: C9         RET                     
733B: CD E6 74   CALL    $74E6           
733E: FA 9F C1   LD      A,($C19F)       
7341: A7         AND     A               
7342: 20 03      JR      NZ,$7347        
7344: CD B0 79   CALL    $79B0           
7347: C9         RET                     
7348: 00         NOP                     
7349: 04         INC     B               
734A: 72         LD      (HL),D          
734B: 00         NOP                     
734C: E0 04      LDFF00  ($04),A         
734E: 72         LD      (HL),D          
734F: 00         NOP                     
7350: 00         NOP                     
7351: F0 78      LD      A,($78)         
7353: 20 00      JR      NZ,$7355        
7355: F8 78      LDHL    SP,$78          
7357: 40         LD      B,B             
7358: 00         NOP                     
7359: 10 78      STOP    $78             
735B: 60         LD      H,B             
735C: 00         NOP                     
735D: 18 78      JR      $73D7           
735F: 00         NOP                     
7360: F0 E8      LD      A,($E8)         
7362: 76         HALT                    
7363: 20 F0      JR      NZ,$7355        
7365: F0 76      LD      A,($76)         
7367: 40         LD      B,B             
7368: F0 18      LD      A,($18)         
736A: 76         HALT                    
736B: 60         LD      H,B             
736C: F0 20      LD      A,($20)         
736E: 76         HALT                    
736F: 00         NOP                     
7370: E8 F4      ADD     SP,$F4          
7372: 74         LD      (HL),H          
7373: 20 E8      JR      NZ,$735D        
7375: 14         INC     D               
7376: 74         LD      (HL),H          
7377: 00         NOP                     
7378: F8 04      LDHL    SP,$04          
737A: 72         LD      (HL),D          
737B: 00         NOP                     
737C: D8         RET     C               
737D: 04         INC     B               
737E: 72         LD      (HL),D          
737F: 00         NOP                     
7380: FC                              
7381: E8 78      ADD     SP,$78          
7383: 20 FC      JR      NZ,$7381        
7385: F0 78      LD      A,($78)         
7387: 40         LD      B,B             
7388: FC                              
7389: 18 78      JR      $7403           
738B: 60         LD      H,B             
738C: FC                              
738D: 20 78      JR      NZ,$7407        
738F: 00         NOP                     
7390: E8 E0      ADD     SP,$E0          
7392: 76         HALT                    
7393: 20 E8      JR      NZ,$737D        
7395: E8 76      ADD     SP,$76          
7397: 40         LD      B,B             
7398: E8 20      ADD     SP,$20          
739A: 76         HALT                    
739B: 60         LD      H,B             
739C: E8 28      ADD     SP,$28          
739E: 76         HALT                    
739F: 00         NOP                     
73A0: E0 F0      LDFF00  ($F0),A         
73A2: 74         LD      (HL),H          
73A3: 20 E0      JR      NZ,$7385        
73A5: 18 74      JR      $741B           
73A7: 00         NOP                     
73A8: 00         NOP                     
73A9: 00         NOP                     
73AA: 74         LD      (HL),H          
73AB: 20 00      JR      NZ,$73AD        
73AD: 08 74 00   LD      ($0074),SP      
73B0: F0 04      LD      A,($04)         
73B2: 72         LD      (HL),D          
73B3: 00         NOP                     
73B4: D0         RET     NC              
73B5: 04         INC     B               
73B6: 72         LD      (HL),D          
73B7: 00         NOP                     
73B8: F8 E0      LDHL    SP,$E0          
73BA: 78         LD      A,B             
73BB: 20 F8      JR      NZ,$73B5        
73BD: E8 78      ADD     SP,$78          
73BF: 40         LD      B,B             
73C0: F8 20      LDHL    SP,$20          
73C2: 78         LD      A,B             
73C3: 60         LD      H,B             
73C4: F8 28      LDHL    SP,$28          
73C6: 78         LD      A,B             
73C7: 00         NOP                     
73C8: E0 D8      LDFF00  ($D8),A         
73CA: 76         HALT                    
73CB: 20 E0      JR      NZ,$73AD        
73CD: E0 76      LDFF00  ($76),A         
73CF: 40         LD      B,B             
73D0: E0 28      LDFF00  ($28),A         
73D2: 76         HALT                    
73D3: 60         LD      H,B             
73D4: E0 30      LDFF00  ($30),A         
73D6: 76         HALT                    
73D7: 00         NOP                     
73D8: D8         RET     C               
73D9: EC                              
73DA: 74         LD      (HL),H          
73DB: 20 D8      JR      NZ,$73B5        
73DD: 1C         INC     E               
73DE: 74         LD      (HL),H          
73DF: 00         NOP                     
73E0: F8 FC      LDHL    SP,$FC          
73E2: 74         LD      (HL),H          
73E3: 20 F8      JR      NZ,$73DD        
73E5: 0C         INC     C               
73E6: 74         LD      (HL),H          
73E7: 00         NOP                     
73E8: 00         NOP                     
73E9: F8 76      LDHL    SP,$76          
73EB: 20 00      JR      NZ,$73ED        
73ED: 00         NOP                     
73EE: 76         HALT                    
73EF: 40         LD      B,B             
73F0: 00         NOP                     
73F1: 08 76 60   LD      ($6076),SP      
73F4: 00         NOP                     
73F5: 10 76      STOP    $76             
73F7: 00         NOP                     
73F8: E4                              
73F9: 04         INC     B               
73FA: 72         LD      (HL),D          
73FB: 00         NOP                     
73FC: 00         NOP                     
73FD: F8 78      LDHL    SP,$78          
73FF: 20 00      JR      NZ,$7401        
7401: 00         NOP                     
7402: 78         LD      A,B             
7403: 40         LD      B,B             
7404: 00         NOP                     
7405: 08 78 60   LD      ($6078),SP      
7408: 00         NOP                     
7409: 10 78      STOP    $78             
740B: 00         NOP                     
740C: F4                              
740D: F0 76      LD      A,($76)         
740F: 20 F4      JR      NZ,$7405        
7411: F8 76      LDHL    SP,$76          
7413: 40         LD      B,B             
7414: F4                              
7415: 10 76      STOP    $76             
7417: 60         LD      H,B             
7418: F4                              
7419: 18 76      JR      $7491           
741B: 00         NOP                     
741C: EC                              
741D: F8 74      LDHL    SP,$74          
741F: 20 EC      JR      NZ,$740D        
7421: 10 74      STOP    $74             
7423: 00         NOP                     
7424: F0 D8      LD      A,($D8)         
7426: 78         LD      A,B             
7427: 20 F0      JR      NZ,$7419        
7429: E0 78      LDFF00  ($78),A         
742B: 40         LD      B,B             
742C: F0 28      LD      A,($28)         
742E: 78         LD      A,B             
742F: 60         LD      H,B             
7430: F0 30      LD      A,($30)         
7432: 78         LD      A,B             
7433: 00         NOP                     
7434: CC E8 74   CALL    Z,$74E8         
7437: 20 CC      JR      NZ,$7405        
7439: 20 74      JR      NZ,$74AF        
743B: 00         NOP                     
743C: 48         LD      C,B             
743D: 73         LD      (HL),E          
743E: 78         LD      A,B             
743F: 73         LD      (HL),E          
7440: B0         OR      B               
7441: 73         LD      (HL),E          
7442: F8 73      LDHL    SP,$73          
7444: 0C         INC     C               
7445: 0E 12      LD      C,$12           
7447: 11 F0 EC   LD      DE,$ECF0        
744A: D6 00      SUB     $00             
744C: E0 EC      LDFF00  ($EC),A         
744E: F0 E7      LD      A,($E7)         
7450: 1F         RRA                     
7451: 1F         RRA                     
7452: 00         NOP                     
7453: F5         PUSH    AF              
7454: E6 03      AND     $03             
7456: 5F         LD      E,A             
7457: 50         LD      D,B             
7458: 21 44 74   LD      HL,$7444        
745B: 19         ADD     HL,DE           
745C: 4E         LD      C,(HL)          
745D: F1         POP     AF              
745E: 17         RLA                     
745F: E6 06      AND     $06             
7461: 5F         LD      E,A             
7462: 50         LD      D,B             
7463: 21 3C 74   LD      HL,$743C        
7466: 19         ADD     HL,DE           
7467: 2A         LD      A,(HLI)         
7468: 66         LD      H,(HL)          
7469: 6F         LD      L,A             
746A: CD 26 3D   CALL    $3D26           
746D: 3E 10      LD      A,$10           
746F: CD D0 3D   CALL    $3DD0           
7472: C9         RET                     
7473: 7E         LD      A,(HL)          
7474: 00         NOP                     
7475: 7E         LD      A,(HL)          
7476: 20 CD      JR      NZ,$7445        
7478: 91         SUB     C               
7479: 08 C0 11   LD      ($11C0),SP      
747C: 73         LD      (HL),E          
747D: 74         LD      (HL),H          
747E: CD 3B 3C   CALL    $3C3B           
7481: CD 0A 79   CALL    $790A           
7484: 21 50 C2   LD      HL,$C250        
7487: 09         ADD     HL,BC           
7488: 34         INC     (HL)            
7489: 7E         LD      A,(HL)          
748A: E6 80      AND     $80             
748C: 20 37      JR      NZ,$74C5        
748E: 21 10 C2   LD      HL,$C210        
7491: 09         ADD     HL,BC           
7492: 7E         LD      A,(HL)          
7493: FE 70      CP      $70             
7495: 38 2E      JR      C,$74C5         
7497: 36 70      LD      (HL),$70        
7499: 21 50 C2   LD      HL,$C250        
749C: 09         ADD     HL,BC           
749D: 70         LD      (HL),B          
749E: CD D5 3B   CALL    $3BD5           
74A1: 30 22      JR      NC,$74C5        
74A3: 3E 01      LD      A,$01           
74A5: E0 F3      LDFF00  ($F3),A         
74A7: CD B0 79   CALL    $79B0           
74AA: 21 E9 DA   LD      HL,$DAE9        
74AD: FA 0F DB   LD      A,($DB0F)       
74B0: FE 05      CP      $05             
74B2: 20 04      JR      NZ,$74B8        
74B4: CB EE      SET     1,E             
74B6: 18 02      JR      $74BA           
74B8: CB F6      SET     1,E             
74BA: C6 01      ADD     $01             
74BC: 27         DAA                     
74BD: EA 0F DB   LD      ($DB0F),A       
74C0: 3E EF      LD      A,$EF           
74C2: CD 97 21   CALL    $2197           
74C5: C9         RET                     
74C6: F8 00      LDHL    SP,$00          
74C8: 52         LD      D,D             
74C9: 00         NOP                     
74CA: F8 08      LDHL    SP,$08          
74CC: 52         LD      D,D             
74CD: 20 08      JR      NZ,$74D7        
74CF: 00         NOP                     
74D0: 54         LD      D,H             
74D1: 00         NOP                     
74D2: 08 08 54   LD      ($5408),SP      
74D5: 20 F8      JR      NZ,$74CF        
74D7: 00         NOP                     
74D8: 54         LD      D,H             
74D9: 40         LD      B,B             
74DA: F8 08      LDHL    SP,$08          
74DC: 54         LD      D,H             
74DD: 60         LD      H,B             
74DE: 08 00 52   LD      ($5200),SP      
74E1: 40         LD      B,B             
74E2: 08 08 52   LD      ($5208),SP      
74E5: 60         LD      H,B             
74E6: 21 D6 74   LD      HL,$74D6        
74E9: 18 03      JR      $74EE           
74EB: 21 C6 74   LD      HL,$74C6        
74EE: 0E 04      LD      C,$04           
74F0: CD 26 3D   CALL    $3D26           
74F3: 3E 02      LD      A,$02           
74F5: CD D0 3D   CALL    $3DD0           
74F8: C9         RET                     
74F9: 98         SBC     B               
74FA: 50         LD      D,B             
74FB: 8D         ADC     A,L             
74FC: 6C         LD      L,H             
74FD: 6E         LD      L,(HL)          
74FE: 6C         LD      L,H             
74FF: 6E         LD      L,(HL)          
7500: 6C         LD      L,H             
7501: 6E         LD      L,(HL)          
7502: 6C         LD      L,H             
7503: 6E         LD      L,(HL)          
7504: 6C         LD      L,H             
7505: 6E         LD      L,(HL)          
7506: 6C         LD      L,H             
7507: 6E         LD      L,(HL)          
7508: 6C         LD      L,H             
7509: 6E         LD      L,(HL)          
750A: 98         SBC     B               
750B: 51         LD      D,C             
750C: 8D         ADC     A,L             
750D: 6D         LD      L,L             
750E: 6F         LD      L,A             
750F: 6D         LD      L,L             
7510: 6F         LD      L,A             
7511: 6D         LD      L,L             
7512: 6F         LD      L,A             
7513: 6D         LD      L,L             
7514: 6F         LD      L,A             
7515: 6D         LD      L,L             
7516: 6F         LD      L,A             
7517: 6D         LD      L,L             
7518: 6F         LD      L,A             
7519: 6D         LD      L,L             
751A: 6F         LD      L,A             
751B: 00         NOP                     
751C: C5         PUSH    BC              
751D: 0E 23      LD      C,$23           
751F: 3E 22      LD      A,$22           
7521: EA 00 D6   LD      ($D600),A       
7524: 21 01 D6   LD      HL,$D601        
7527: 11 F9 74   LD      DE,$74F9        
752A: 1A         LD      A,(DE)          
752B: 13         INC     DE              
752C: 22         LD      (HLI),A         
752D: 0D         DEC     C               
752E: 20 FA      JR      NZ,$752A        
7530: C1         POP     BC              
7531: 3E 89      LD      A,$89           
7533: EA 29 D7   LD      ($D729),A       
7536: EA 39 D7   LD      ($D739),A       
7539: EA 49 D7   LD      ($D749),A       
753C: EA 59 D7   LD      ($D759),A       
753F: EA 69 D7   LD      ($D769),A       
7542: EA 79 D7   LD      ($D779),A       
7545: EA 89 D7   LD      ($D789),A       
7548: C9         RET                     
7549: FC                              
754A: 04         INC     B               
754B: 00         NOP                     
754C: 00         NOP                     
754D: FF         RST     0X38            
754E: 00         NOP                     
754F: 00         NOP                     
7550: 00         NOP                     
7551: 00         NOP                     
7552: 00         NOP                     
7553: 04         INC     B               
7554: FC                              
7555: 00         NOP                     
7556: 00         NOP                     
7557: 00         NOP                     
7558: FF         RST     0X38            
7559: 0C         INC     C               
755A: 18 24      JR      $7580           
755C: 30 3C      JR      NC,$759A        
755E: 48         LD      C,B             
755F: FA 24 C1   LD      A,($C124)       
7562: FE 03      CP      $03             
7564: 30 01      JR      NC,$7567        
7566: C9         RET                     
7567: FA 25 C1   LD      A,($C125)       
756A: 5F         LD      E,A             
756B: 16 00      LD      D,$00           
756D: 21 49 75   LD      HL,$7549        
7570: 19         ADD     HL,DE           
7571: 7E         LD      A,(HL)          
7572: E0 D7      LDFF00  ($D7),A         
7574: 21 4D 75   LD      HL,$754D        
7577: 19         ADD     HL,DE           
7578: 7E         LD      A,(HL)          
7579: E0 D8      LDFF00  ($D8),A         
757B: 21 51 75   LD      HL,$7551        
757E: 19         ADD     HL,DE           
757F: 7E         LD      A,(HL)          
7580: E0 D9      LDFF00  ($D9),A         
7582: 21 55 75   LD      HL,$7555        
7585: 19         ADD     HL,DE           
7586: 7E         LD      A,(HL)          
7587: E0 DA      LDFF00  ($DA),A         
7589: 21 00 C2   LD      HL,$C200        
758C: 09         ADD     HL,BC           
758D: F0 D7      LD      A,($D7)         
758F: 86         ADD     A,(HL)          
7590: CB 12      SET     1,E             
7592: 77         LD      (HL),A          
7593: 21 20 C2   LD      HL,$C220        
7596: 09         ADD     HL,BC           
7597: F0 D8      LD      A,($D8)         
7599: CB 1A      SET     1,E             
759B: 8E         ADC     A,(HL)          
759C: 77         LD      (HL),A          
759D: 21 10 C2   LD      HL,$C210        
75A0: 09         ADD     HL,BC           
75A1: F0 D9      LD      A,($D9)         
75A3: 86         ADD     A,(HL)          
75A4: CB 12      SET     1,E             
75A6: 77         LD      (HL),A          
75A7: 21 30 C2   LD      HL,$C230        
75AA: 09         ADD     HL,BC           
75AB: F0 DA      LD      A,($DA)         
75AD: CB 1A      SET     1,E             
75AF: 8E         ADC     A,(HL)          
75B0: 77         LD      (HL),A          
75B1: F0 EB      LD      A,($EB)         
75B3: FE 7F      CP      $7F             
75B5: 20 13      JR      NZ,$75CA        
75B7: 21 40 C4   LD      HL,$C440        
75BA: 09         ADD     HL,BC           
75BB: F0 D7      LD      A,($D7)         
75BD: 86         ADD     A,(HL)          
75BE: 77         LD      (HL),A          
75BF: 21 D0 C2   LD      HL,$C2D0        
75C2: 09         ADD     HL,BC           
75C3: F0 D9      LD      A,($D9)         
75C5: 86         ADD     A,(HL)          
75C6: 77         LD      (HL),A          
75C7: C3 6F 76   JP      $766F           
75CA: FE 87      CP      $87             
75CC: 20 3C      JR      NZ,$760A        
75CE: 21 D0 C2   LD      HL,$C2D0        
75D1: 09         ADD     HL,BC           
75D2: 7E         LD      A,(HL)          
75D3: FE 02      CP      $02             
75D5: CA 6F 76   JP      Z,$766F         
75D8: 21 D0 C3   LD      HL,$C3D0        
75DB: 09         ADD     HL,BC           
75DC: 7E         LD      A,(HL)          
75DD: E0 E6      LDFF00  ($E6),A         
75DF: 3E 06      LD      A,$06           
75E1: E0 E8      LDFF00  ($E8),A         
75E3: 5F         LD      E,A             
75E4: 50         LD      D,B             
75E5: 21 58 75   LD      HL,$7558        
75E8: 19         ADD     HL,DE           
75E9: E5         PUSH    HL              
75EA: F0 E6      LD      A,($E6)         
75EC: 96         SUB     (HL)            
75ED: 5F         LD      E,A             
75EE: 50         LD      D,B             
75EF: 21 00 D0   LD      HL,$D000        
75F2: 19         ADD     HL,DE           
75F3: F0 D7      LD      A,($D7)         
75F5: 86         ADD     A,(HL)          
75F6: 77         LD      (HL),A          
75F7: F0 E6      LD      A,($E6)         
75F9: E1         POP     HL              
75FA: 96         SUB     (HL)            
75FB: 5F         LD      E,A             
75FC: 50         LD      D,B             
75FD: 21 00 D1   LD      HL,$D100        
7600: 19         ADD     HL,DE           
7601: F0 D9      LD      A,($D9)         
7603: 86         ADD     A,(HL)          
7604: 77         LD      (HL),A          
7605: F0 E8      LD      A,($E8)         
7607: 3D         DEC     A               
7608: 20 D7      JR      NZ,$75E1        
760A: FE C1      CP      $C1             
760C: 20 20      JR      NZ,$762E        
760E: FA 73 DB   LD      A,($DB73)       
7611: A7         AND     A               
7612: 28 5B      JR      Z,$766F         
7614: 1E 10      LD      E,$10           
7616: 21 55 D1   LD      HL,$D155        
7619: F0 D7      LD      A,($D7)         
761B: 86         ADD     A,(HL)          
761C: 22         LD      (HLI),A         
761D: 1D         DEC     E               
761E: 20 F9      JR      NZ,$7619        
7620: 1E 10      LD      E,$10           
7622: 21 75 D1   LD      HL,$D175        
7625: F0 D9      LD      A,($D9)         
7627: 86         ADD     A,(HL)          
7628: 22         LD      (HLI),A         
7629: 1D         DEC     E               
762A: 20 F9      JR      NZ,$7625        
762C: 18 41      JR      $766F           
762E: FE 69      CP      $69             
7630: 28 2D      JR      Z,$765F         
7632: FE B0      CP      $B0             
7634: 28 29      JR      Z,$765F         
7636: FE 6D      CP      $6D             
7638: 20 35      JR      NZ,$766F        
763A: FA 56 DB   LD      A,($DB56)       
763D: FE 01      CP      $01             
763F: 20 06      JR      NZ,$7647        
7641: F0 E7      LD      A,($E7)         
7643: E6 07      AND     $07             
7645: 28 28      JR      Z,$766F         
7647: 1E 06      LD      E,$06           
7649: 21 00 D1   LD      HL,$D100        
764C: F0 D7      LD      A,($D7)         
764E: 86         ADD     A,(HL)          
764F: 22         LD      (HLI),A         
7650: 1D         DEC     E               
7651: 20 F9      JR      NZ,$764C        
7653: 1E 06      LD      E,$06           
7655: 21 10 D1   LD      HL,$D110        
7658: F0 D9      LD      A,($D9)         
765A: 86         ADD     A,(HL)          
765B: 22         LD      (HLI),A         
765C: 1D         DEC     E               
765D: 20 F9      JR      NZ,$7658        
765F: 21 B0 C2   LD      HL,$C2B0        
7662: 09         ADD     HL,BC           
7663: F0 D7      LD      A,($D7)         
7665: 86         ADD     A,(HL)          
7666: 77         LD      (HL),A          
7667: 21 C0 C2   LD      HL,$C2C0        
766A: 09         ADD     HL,BC           
766B: F0 D9      LD      A,($D9)         
766D: 86         ADD     A,(HL)          
766E: 77         LD      (HL),A          
766F: F0 F6      LD      A,($F6)         
7671: 21 E0 C3   LD      HL,$C3E0        
7674: 09         ADD     HL,BC           
7675: BE         CP      (HL)            
7676: 28 1E      JR      Z,$7696         
7678: 21 00 C2   LD      HL,$C200        
767B: 09         ADD     HL,BC           
767C: 7E         LD      A,(HL)          
767D: FE A0      CP      $A0             
767F: 30 0B      JR      NC,$768C        
7681: 21 10 C2   LD      HL,$C210        
7684: 09         ADD     HL,BC           
7685: 7E         LD      A,(HL)          
7686: D6 10      SUB     $10             
7688: FE 78      CP      $78             
768A: 38 0A      JR      C,$7696         
768C: F0 EB      LD      A,($EB)         
768E: FE A7      CP      $A7             
7690: C8         RET     Z               
7691: 21 80 C2   LD      HL,$C280        
7694: 09         ADD     HL,BC           
7695: 70         LD      (HL),B          
7696: C9         RET                     
7697: FA A5 C1   LD      A,($C1A5)       
769A: A7         AND     A               
769B: 28 2F      JR      Z,$76CC         
769D: FA 9F C1   LD      A,($C19F)       
76A0: A7         AND     A               
76A1: 20 29      JR      NZ,$76CC        
76A3: F0 E7      LD      A,($E7)         
76A5: E6 03      AND     $03             
76A7: C7         RST     0X00            
76A8: B0         OR      B               
76A9: 76         HALT                    
76AA: CD 76 EA   CALL    $EA76           
76AD: 76         HALT                    
76AE: F6 76      OR      $76             
76B0: 21 CF DC   LD      HL,$DCCF        
76B3: 11 CF DC   LD      DE,$DCCF        
76B6: 3A         LD      A,(HLD)         
76B7: F5         PUSH    AF              
76B8: 3A         LD      A,(HLD)         
76B9: F5         PUSH    AF              
76BA: 0E 07      LD      C,$07           
76BC: 3A         LD      A,(HLD)         
76BD: 12         LD      (DE),A          
76BE: 1B         DEC     DE              
76BF: 3A         LD      A,(HLD)         
76C0: 12         LD      (DE),A          
76C1: 1B         DEC     DE              
76C2: 0D         DEC     C               
76C3: 20 F7      JR      NZ,$76BC        
76C5: E1         POP     HL              
76C6: C1         POP     BC              
76C7: 78         LD      A,B             
76C8: 12         LD      (DE),A          
76C9: 1B         DEC     DE              
76CA: 7C         LD      A,H             
76CB: 12         LD      (DE),A          
76CC: C9         RET                     
76CD: 21 D0 DC   LD      HL,$DCD0        
76D0: 11 D0 DC   LD      DE,$DCD0        
76D3: 2A         LD      A,(HLI)         
76D4: F5         PUSH    AF              
76D5: 2A         LD      A,(HLI)         
76D6: F5         PUSH    AF              
76D7: 0E 07      LD      C,$07           
76D9: 2A         LD      A,(HLI)         
76DA: 12         LD      (DE),A          
76DB: 13         INC     DE              
76DC: 2A         LD      A,(HLI)         
76DD: 12         LD      (DE),A          
76DE: 13         INC     DE              
76DF: 0D         DEC     C               
76E0: 20 F7      JR      NZ,$76D9        
76E2: E1         POP     HL              
76E3: C1         POP     BC              
76E4: 78         LD      A,B             
76E5: 12         LD      (DE),A          
76E6: 13         INC     DE              
76E7: 7C         LD      A,H             
76E8: 12         LD      (DE),A          
76E9: C9         RET                     
76EA: 21 E0 DC   LD      HL,$DCE0        
76ED: 1E 10      LD      E,$10           
76EF: CB 06      SET     1,E             
76F1: 23         INC     HL              
76F2: 1D         DEC     E               
76F3: 20 FA      JR      NZ,$76EF        
76F5: C9         RET                     
76F6: 21 F0 DC   LD      HL,$DCF0        
76F9: 1E 10      LD      E,$10           
76FB: CB 0E      SET     1,E             
76FD: 23         INC     HL              
76FE: 1D         DEC     E               
76FF: 20 FA      JR      NZ,$76FB        
7701: C9         RET                     
7702: FD                              
7703: FC                              
7704: 16 00      LD      D,$00           
7706: FC                              
7707: 0C         INC     C               
7708: 16 00      LD      D,$00           
770A: 0E FB      LD      C,$FB           
770C: 16 00      LD      D,$00           
770E: 0C         INC     C               
770F: 0D         DEC     C               
7710: 16 00      LD      D,$00           
7712: FB         EI                      
7713: FD                              
7714: 16 00      LD      D,$00           
7716: FA 0B 16   LD      A,($160B)       
7719: 00         NOP                     
771A: 0B         DEC     BC              
771B: FC                              
771C: 16 00      LD      D,$00           
771E: 09         ADD     HL,BC           
771F: 0C         INC     C               
7720: 16 00      LD      D,$00           
7722: FD                              
7723: FE 16      CP      $16             
7725: 00         NOP                     
7726: FC                              
7727: 0A         LD      A,(BC)          
7728: 16 00      LD      D,$00           
772A: 0B         DEC     BC              
772B: FD                              
772C: 16 00      LD      D,$00           
772E: 08 0A 16   LD      ($160A),SP      
7731: 00         NOP                     
7732: FF         RST     0X38            
7733: 00         NOP                     
7734: 16 00      LD      D,$00           
7736: 00         NOP                     
7737: 08 16 00   LD      ($0016),SP      
773A: 0A         LD      A,(BC)          
773B: FF         RST     0X38            
773C: 16 00      LD      D,$00           
773E: 08 09 16   LD      ($1609),SP      
7741: 00         NOP                     
7742: 02         LD      (BC),A          
7743: FC                              
7744: 28 00      JR      Z,$7746         
7746: FB         EI                      
7747: 04         INC     B               
7748: 28 60      JR      Z,$77AA         
774A: 05         DEC     B               
774B: 06 28      LD      B,$28           
774D: 00         NOP                     
774E: 01 0A 28   LD      BC,$280A        
7751: 20 01      JR      NZ,$7754        
7753: FF         RST     0X38            
7754: 28 00      JR      Z,$7756         
7756: F9         LD      SP,HL           
7757: 04         INC     B               
7758: 28 60      JR      Z,$77BA         
775A: 08 06 28   LD      ($2806),SP      
775D: 00         NOP                     
775E: 02         LD      (BC),A          
775F: 07         RLCA                    
7760: 28 20      JR      Z,$7782         
7762: 00         NOP                     
7763: 00         NOP                     
7764: 28 20      JR      Z,$7786         
7766: F8 02      LDHL    SP,$02          
7768: 28 60      JR      Z,$77CA         
776A: 04         INC     B               
776B: 04         INC     B               
776C: 28 20      JR      Z,$778E         
776E: 0A         LD      A,(BC)          
776F: 07         RLCA                    
7770: 28 20      JR      Z,$7792         
7772: FE 01      CP      $01             
7774: 28 20      JR      Z,$7796         
7776: 04         INC     B               
7777: 01 28 60   LD      BC,$6028        
777A: 04         INC     B               
777B: 05         DEC     B               
777C: 28 20      JR      Z,$779E         
777E: 0C         INC     C               
777F: 07         RLCA                    
7780: 28 20      JR      Z,$77A2         
7782: FD                              
7783: 00         NOP                     
7784: 28 20      JR      Z,$77A6         
7786: 04         INC     B               
7787: FE 28      CP      $28             
7789: 60         LD      H,B             
778A: 08 08 28   LD      ($2808),SP      
778D: 20 0E      JR      NZ,$779D        
778F: 09         ADD     HL,BC           
7790: 28 20      JR      Z,$77B2         
7792: FC                              
7793: FF         RST     0X38            
7794: 28 00      JR      Z,$7796         
7796: 04         INC     B               
7797: FA 28 40   LD      A,($4028)       
779A: 08 09 28   LD      ($2809),SP      
779D: 20 0F      JR      NZ,$77AE        
779F: 0A         LD      A,(BC)          
77A0: 28 00      JR      Z,$77A2         
77A2: FB         EI                      
77A3: FE 28      CP      $28             
77A5: 00         NOP                     
77A6: 03         INC     BC              
77A7: F9         LD      SP,HL           
77A8: 28 40      JR      Z,$77EA         
77AA: 08 0C 28   LD      ($280C),SP      
77AD: 00         NOP                     
77AE: 11 0B 28   LD      DE,$280B        
77B1: 00         NOP                     
77B2: FA FD 28   LD      A,($28FD)       
77B5: 00         NOP                     
77B6: 01 F7 28   LD      BC,$28F7        
77B9: 40         LD      B,B             
77BA: 09         ADD     HL,BC           
77BB: 0D         DEC     C               
77BC: 28 00      JR      Z,$77BE         
77BE: 0F         RRCA                    
77BF: 0C         INC     C               
77C0: 28 00      JR      Z,$77C2         
77C2: F0 F1      LD      A,($F1)         
77C4: FE FF      CP      $FF             
77C6: 28 18      JR      Z,$77E0         
77C8: FE 01      CP      $01             
77CA: 28 14      JR      Z,$77E0         
77CC: F0 D7      LD      A,($D7)         
77CE: E6 0C      AND     $0C             
77D0: CB 27      SET     1,E             
77D2: CB 27      SET     1,E             
77D4: 5F         LD      E,A             
77D5: 50         LD      D,B             
77D6: 21 02 77   LD      HL,$7702        
77D9: 19         ADD     HL,DE           
77DA: 0E 04      LD      C,$04           
77DC: CD 26 3D   CALL    $3D26           
77DF: C9         RET                     
77E0: 3C         INC     A               
77E1: 20 07      JR      NZ,$77EA        
77E3: E0 F1      LDFF00  ($F1),A         
77E5: F0 E7      LD      A,($E7)         
77E7: A9         XOR     C               
77E8: 1F         RRA                     
77E9: D8         RET     C               
77EA: F0 D7      LD      A,($D7)         
77EC: E6 1C      AND     $1C             
77EE: EE 1C      XOR     $1C             
77F0: CB 27      SET     1,E             
77F2: CB 27      SET     1,E             
77F4: 5F         LD      E,A             
77F5: 50         LD      D,B             
77F6: 21 42 77   LD      HL,$7742        
77F9: 19         ADD     HL,DE           
77FA: 0E 04      LD      C,$04           
77FC: CD 26 3D   CALL    $3D26           
77FF: C9         RET                     
7800: CD D5 3B   CALL    $3BD5           
7803: 30 27      JR      NC,$782C        
7805: CD 4A 09   CALL    $094A           
7808: FA A6 C1   LD      A,($C1A6)       
780B: A7         AND     A               
780C: 28 11      JR      Z,$781F         
780E: 5F         LD      E,A             
780F: 50         LD      D,B             
7810: 21 9F C3   LD      HL,$C39F        
7813: 19         ADD     HL,DE           
7814: 7E         LD      A,(HL)          
7815: FE 03      CP      $03             
7817: 20 06      JR      NZ,$781F        
7819: 21 8F C2   LD      HL,$C28F        
781C: 19         ADD     HL,DE           
781D: 36 00      LD      (HL),$00        
781F: FA 4A C1   LD      A,($C14A)       
7822: 5F         LD      E,A             
7823: CD 42 09   CALL    $0942           
7826: CD 95 14   CALL    $1495           
7829: 7B         LD      A,E             
782A: 37         SCF                     
782B: C9         RET                     
782C: A7         AND     A               
782D: C9         RET                     
782E: 06 04      LD      B,$04           
7830: 02         LD      (BC),A          
7831: 00         NOP                     
7832: 21 80 C3   LD      HL,$C380        
7835: 09         ADD     HL,BC           
7836: 5E         LD      E,(HL)          
7837: 50         LD      D,B             
7838: 21 2E 78   LD      HL,$782E        
783B: 19         ADD     HL,DE           
783C: E5         PUSH    HL              
783D: 21 D0 C3   LD      HL,$C3D0        
7840: 09         ADD     HL,BC           
7841: 34         INC     (HL)            
7842: 7E         LD      A,(HL)          
7843: 1F         RRA                     
7844: 1F         RRA                     
7845: 1F         RRA                     
7846: 1F         RRA                     
7847: E1         POP     HL              
7848: E6 01      AND     $01             
784A: B6         OR      (HL)            
784B: C3 87 3B   JP      $3B87           
784E: 58         LD      E,B             
784F: F0 99      LD      A,($99)         
7851: 21 EF FF   LD      HL,$FFEF        
7854: 96         SUB     (HL)            
7855: C6 14      ADD     $14             
7857: FE 28      CP      $28             
7859: 30 3E      JR      NC,$7899        
785B: F0 98      LD      A,($98)         
785D: 21 EE FF   LD      HL,$FFEE        
7860: 96         SUB     (HL)            
7861: C6 10      ADD     $10             
7863: FE 20      CP      $20             
7865: 30 32      JR      NC,$7899        
7867: 1C         INC     E               
7868: D5         PUSH    DE              
7869: CD 89 79   CALL    $7989           
786C: F0 9E      LD      A,($9E)         
786E: EE 01      XOR     $01             
7870: BB         CP      E               
7871: D1         POP     DE              
7872: 20 25      JR      NZ,$7899        
7874: 21 AD C1   LD      HL,$C1AD        
7877: 36 01      LD      (HL),$01        
7879: FA 9F C1   LD      A,($C19F)       
787C: 21 4F C1   LD      HL,$C14F        
787F: B6         OR      (HL)            
7880: 21 46 C1   LD      HL,$C146        
7883: B6         OR      (HL)            
7884: 21 34 C1   LD      HL,$C134        
7887: B6         OR      (HL)            
7888: 20 0F      JR      NZ,$7899        
788A: FA 9A DB   LD      A,($DB9A)       
788D: FE 80      CP      $80             
788F: 20 08      JR      NZ,$7899        
7891: F0 CC      LD      A,($CC)         
7893: E6 10      AND     $10             
7895: 28 02      JR      Z,$7899         
7897: 37         SCF                     
7898: C9         RET                     
7899: A7         AND     A               
789A: C9         RET                     
789B: F0 EA      LD      A,($EA)         
789D: FE 05      CP      $05             
789F: 20 1A      JR      NZ,$78BB        
78A1: FA 95 DB   LD      A,($DB95)       
78A4: FE 07      CP      $07             
78A6: 28 13      JR      Z,$78BB         
78A8: 21 A8 C1   LD      HL,$C1A8        
78AB: FA 9F C1   LD      A,($C19F)       
78AE: B6         OR      (HL)            
78AF: 21 4F C1   LD      HL,$C14F        
78B2: B6         OR      (HL)            
78B3: 20 06      JR      NZ,$78BB        
78B5: FA 24 C1   LD      A,($C124)       
78B8: A7         AND     A               
78B9: 28 01      JR      Z,$78BC         
78BB: F1         POP     AF              
78BC: C9         RET                     
78BD: 21 10 C4   LD      HL,$C410        
78C0: 09         ADD     HL,BC           
78C1: 7E         LD      A,(HL)          
78C2: A7         AND     A               
78C3: 28 41      JR      Z,$7906         
78C5: 3D         DEC     A               
78C6: 77         LD      (HL),A          
78C7: CD B8 3E   CALL    $3EB8           
78CA: 21 40 C2   LD      HL,$C240        
78CD: 09         ADD     HL,BC           
78CE: 7E         LD      A,(HL)          
78CF: F5         PUSH    AF              
78D0: 21 50 C2   LD      HL,$C250        
78D3: 09         ADD     HL,BC           
78D4: 7E         LD      A,(HL)          
78D5: F5         PUSH    AF              
78D6: 21 F0 C3   LD      HL,$C3F0        
78D9: 09         ADD     HL,BC           
78DA: 7E         LD      A,(HL)          
78DB: 21 40 C2   LD      HL,$C240        
78DE: 09         ADD     HL,BC           
78DF: 77         LD      (HL),A          
78E0: 21 00 C4   LD      HL,$C400        
78E3: 09         ADD     HL,BC           
78E4: 7E         LD      A,(HL)          
78E5: 21 50 C2   LD      HL,$C250        
78E8: 09         ADD     HL,BC           
78E9: 77         LD      (HL),A          
78EA: CD 07 79   CALL    $7907           
78ED: 21 30 C4   LD      HL,$C430        
78F0: 09         ADD     HL,BC           
78F1: 7E         LD      A,(HL)          
78F2: E6 20      AND     $20             
78F4: 20 03      JR      NZ,$78F9        
78F6: CD 9E 3B   CALL    $3B9E           
78F9: 21 50 C2   LD      HL,$C250        
78FC: 09         ADD     HL,BC           
78FD: F1         POP     AF              
78FE: 77         LD      (HL),A          
78FF: 21 40 C2   LD      HL,$C240        
7902: 09         ADD     HL,BC           
7903: F1         POP     AF              
7904: 77         LD      (HL),A          
7905: F1         POP     AF              
7906: C9         RET                     
7907: CD 14 79   CALL    $7914           
790A: C5         PUSH    BC              
790B: 79         LD      A,C             
790C: C6 10      ADD     $10             
790E: 4F         LD      C,A             
790F: CD 14 79   CALL    $7914           
7912: C1         POP     BC              
7913: C9         RET                     
7914: 21 40 C2   LD      HL,$C240        
7917: 09         ADD     HL,BC           
7918: 7E         LD      A,(HL)          
7919: A7         AND     A               
791A: 28 23      JR      Z,$793F         
791C: F5         PUSH    AF              
791D: CB 37      SET     1,E             
791F: E6 F0      AND     $F0             
7921: 21 60 C2   LD      HL,$C260        
7924: 09         ADD     HL,BC           
7925: 86         ADD     A,(HL)          
7926: 77         LD      (HL),A          
7927: CB 12      SET     1,E             
7929: 21 00 C2   LD      HL,$C200        
792C: 09         ADD     HL,BC           
792D: F1         POP     AF              
792E: 1E 00      LD      E,$00           
7930: CB 7F      SET     1,E             
7932: 28 02      JR      Z,$7936         
7934: 1E F0      LD      E,$F0           
7936: CB 37      SET     1,E             
7938: E6 0F      AND     $0F             
793A: B3         OR      E               
793B: CB 1A      SET     1,E             
793D: 8E         ADC     A,(HL)          
793E: 77         LD      (HL),A          
793F: C9         RET                     
7940: 21 20 C3   LD      HL,$C320        
7943: 09         ADD     HL,BC           
7944: 7E         LD      A,(HL)          
7945: A7         AND     A               
7946: 28 F7      JR      Z,$793F         
7948: F5         PUSH    AF              
7949: CB 37      SET     1,E             
794B: E6 F0      AND     $F0             
794D: 21 30 C3   LD      HL,$C330        
7950: 09         ADD     HL,BC           
7951: 86         ADD     A,(HL)          
7952: 77         LD      (HL),A          
7953: CB 12      SET     1,E             
7955: 21 10 C3   LD      HL,$C310        
7958: 18 D2      JR      $792C           
795A: 1E 00      LD      E,$00           
795C: F0 98      LD      A,($98)         
795E: 21 00 C2   LD      HL,$C200        
7961: 09         ADD     HL,BC           
7962: 96         SUB     (HL)            
7963: CB 7F      SET     1,E             
7965: 28 01      JR      Z,$7968         
7967: 1C         INC     E               
7968: 57         LD      D,A             
7969: C9         RET                     
796A: 1E 02      LD      E,$02           
796C: F0 99      LD      A,($99)         
796E: 21 10 C2   LD      HL,$C210        
7971: 09         ADD     HL,BC           
7972: 96         SUB     (HL)            
7973: CB 7F      SET     1,E             
7975: 20 01      JR      NZ,$7978        
7977: 1C         INC     E               
7978: 57         LD      D,A             
7979: C9         RET                     
797A: 1E 02      LD      E,$02           
797C: F0 99      LD      A,($99)         
797E: 21 EC FF   LD      HL,$FFEC        
7981: 96         SUB     (HL)            
7982: CB 7F      SET     1,E             
7984: 20 01      JR      NZ,$7987        
7986: 1C         INC     E               
7987: 57         LD      D,A             
7988: C9         RET                     
7989: CD 5A 79   CALL    $795A           
798C: 7B         LD      A,E             
798D: E0 D7      LDFF00  ($D7),A         
798F: 7A         LD      A,D             
7990: CB 7F      SET     1,E             
7992: 28 02      JR      Z,$7996         
7994: 2F         CPL                     
7995: 3C         INC     A               
7996: F5         PUSH    AF              
7997: CD 6A 79   CALL    $796A           
799A: 7B         LD      A,E             
799B: E0 D8      LDFF00  ($D8),A         
799D: 7A         LD      A,D             
799E: CB 7F      SET     1,E             
79A0: 28 02      JR      Z,$79A4         
79A2: 2F         CPL                     
79A3: 3C         INC     A               
79A4: D1         POP     DE              
79A5: BA         CP      D               
79A6: 30 04      JR      NC,$79AC        
79A8: F0 D7      LD      A,($D7)         
79AA: 18 02      JR      $79AE           
79AC: F0 D8      LD      A,($D8)         
79AE: 5F         LD      E,A             
79AF: C9         RET                     
79B0: 21 80 C2   LD      HL,$C280        
79B3: 09         ADD     HL,BC           
79B4: 70         LD      (HL),B          
79B5: C9         RET                     
79B6: 21 C0 C2   LD      HL,$C2C0        
79B9: 09         ADD     HL,BC           
79BA: 7E         LD      A,(HL)          
79BB: C7         RST     0X00            
79BC: C2 79 D3   JP      NZ,$D379        
79BF: 79         LD      A,C             
79C0: E4                              
79C1: 79         LD      A,C             
79C2: CD 91 08   CALL    $0891           
79C5: 36 A0      LD      (HL),$A0        
79C7: 21 20 C4   LD      HL,$C420        
79CA: 09         ADD     HL,BC           
79CB: 36 FF      LD      (HL),$FF        
79CD: 21 C0 C2   LD      HL,$C2C0        
79D0: 09         ADD     HL,BC           
79D1: 34         INC     (HL)            
79D2: C9         RET                     
79D3: CD 91 08   CALL    $0891           
79D6: 20 0B      JR      NZ,$79E3        
79D8: 36 C0      LD      (HL),$C0        
79DA: 21 20 C4   LD      HL,$C420        
79DD: 09         ADD     HL,BC           
79DE: 36 FF      LD      (HL),$FF        
79E0: CD CD 79   CALL    $79CD           
79E3: C9         RET                     
79E4: CD 91 08   CALL    $0891           
79E7: 20 09      JR      NZ,$79F2        
79E9: CD D7 08   CALL    $08D7           
79EC: CD BD 27   CALL    $27BD           
79EF: C3 7A 3F   JP      $3F7A           
79F2: CD F6 79   CALL    $79F6           
79F5: C9         RET                     
79F6: E6 07      AND     $07             
79F8: 20 1D      JR      NZ,$7A17        
79FA: CD ED 27   CALL    $27ED           
79FD: E6 1F      AND     $1F             
79FF: D6 10      SUB     $10             
7A01: 5F         LD      E,A             
7A02: 21 EE FF   LD      HL,$FFEE        
7A05: 86         ADD     A,(HL)          
7A06: 77         LD      (HL),A          
7A07: CD ED 27   CALL    $27ED           
7A0A: E6 1F      AND     $1F             
7A0C: D6 14      SUB     $14             
7A0E: 5F         LD      E,A             
7A0F: 21 EC FF   LD      HL,$FFEC        
7A12: 86         ADD     A,(HL)          
7A13: 77         LD      (HL),A          
7A14: CD 18 7A   CALL    $7A18           
7A17: C9         RET                     
7A18: CD A1 78   CALL    $78A1           
7A1B: F0 EE      LD      A,($EE)         
7A1D: E0 D7      LDFF00  ($D7),A         
7A1F: F0 EC      LD      A,($EC)         
7A21: E0 D8      LDFF00  ($D8),A         
7A23: 3E 02      LD      A,$02           
7A25: CD 53 09   CALL    $0953           
7A28: 3E 13      LD      A,$13           
7A2A: E0 F4      LDFF00  ($F4),A         
7A2C: C9         RET                     
7A2D: 3E 36      LD      A,$36           
7A2F: CD 01 3C   CALL    $3C01           
7A32: F0 D7      LD      A,($D7)         
7A34: 21 00 C2   LD      HL,$C200        
7A37: 19         ADD     HL,DE           
7A38: 77         LD      (HL),A          
7A39: F0 D8      LD      A,($D8)         
7A3B: 21 10 C2   LD      HL,$C210        
7A3E: 19         ADD     HL,DE           
7A3F: 77         LD      (HL),A          
7A40: F0 F9      LD      A,($F9)         
7A42: A7         AND     A               
7A43: 28 08      JR      Z,$7A4D         
7A45: 21 50 C2   LD      HL,$C250        
7A48: 09         ADD     HL,BC           
7A49: 36 F0      LD      (HL),$F0        
7A4B: 18 0C      JR      $7A59           
7A4D: 21 20 C3   LD      HL,$C320        
7A50: 19         ADD     HL,DE           
7A51: 36 10      LD      (HL),$10        
7A53: 21 10 C3   LD      HL,$C310        
7A56: 19         ADD     HL,DE           
7A57: 36 08      LD      (HL),$08        
7A59: CD B0 79   CALL    $79B0           
7A5C: 21 F4 FF   LD      HL,$FFF4        
7A5F: 36 1A      LD      (HL),$1A        
7A61: C9         RET                     
7A62: 21 00 D8   LD      HL,$D800        
7A65: F0 F6      LD      A,($F6)         
7A67: 5F         LD      E,A             
7A68: FA A5 DB   LD      A,($DBA5)       
7A6B: 57         LD      D,A             
7A6C: F0 F7      LD      A,($F7)         
7A6E: FE 1A      CP      $1A             
7A70: 30 05      JR      NC,$7A77        
7A72: FE 06      CP      $06             
7A74: 38 01      JR      C,$7A77         
7A76: 14         INC     D               
7A77: 19         ADD     HL,DE           
7A78: 7E         LD      A,(HL)          
7A79: F6 20      OR      $20             
7A7B: 77         LD      (HL),A          
7A7C: E0 F8      LDFF00  ($F8),A         
7A7E: C9         RET                     
7A7F: FF         RST     0X38            
7A80: FF         RST     0X38            
7A81: FF         RST     0X38            
7A82: FF         RST     0X38            
7A83: FF         RST     0X38            
7A84: FF         RST     0X38            
7A85: FF         RST     0X38            
7A86: FF         RST     0X38            
7A87: FF         RST     0X38            
7A88: FF         RST     0X38            
7A89: FF         RST     0X38            
7A8A: FF         RST     0X38            
7A8B: FF         RST     0X38            
7A8C: FF         RST     0X38            
7A8D: FF         RST     0X38            
7A8E: FF         RST     0X38            
7A8F: FF         RST     0X38            
7A90: FF         RST     0X38            
7A91: FF         RST     0X38            
7A92: FF         RST     0X38            
7A93: FF         RST     0X38            
7A94: FF         RST     0X38            
7A95: FF         RST     0X38            
7A96: FF         RST     0X38            
7A97: FF         RST     0X38            
7A98: FF         RST     0X38            
7A99: FF         RST     0X38            
7A9A: FF         RST     0X38            
7A9B: FF         RST     0X38            
7A9C: FF         RST     0X38            
7A9D: FF         RST     0X38            
7A9E: FF         RST     0X38            
7A9F: FF         RST     0X38            
7AA0: FF         RST     0X38            
7AA1: FF         RST     0X38            
7AA2: FF         RST     0X38            
7AA3: FF         RST     0X38            
7AA4: FF         RST     0X38            
7AA5: FF         RST     0X38            
7AA6: FF         RST     0X38            
7AA7: FF         RST     0X38            
7AA8: FF         RST     0X38            
7AA9: FF         RST     0X38            
7AAA: FF         RST     0X38            
7AAB: FF         RST     0X38            
7AAC: FF         RST     0X38            
7AAD: FF         RST     0X38            
7AAE: FF         RST     0X38            
7AAF: FF         RST     0X38            
7AB0: FF         RST     0X38            
7AB1: FF         RST     0X38            
7AB2: FF         RST     0X38            
7AB3: FF         RST     0X38            
7AB4: FF         RST     0X38            
7AB5: FF         RST     0X38            
7AB6: FF         RST     0X38            
7AB7: FF         RST     0X38            
7AB8: FF         RST     0X38            
7AB9: FF         RST     0X38            
7ABA: FF         RST     0X38            
7ABB: FF         RST     0X38            
7ABC: FF         RST     0X38            
7ABD: FF         RST     0X38            
7ABE: FF         RST     0X38            
7ABF: FF         RST     0X38            
7AC0: FF         RST     0X38            
7AC1: FF         RST     0X38            
7AC2: FF         RST     0X38            
7AC3: FF         RST     0X38            
7AC4: FF         RST     0X38            
7AC5: FF         RST     0X38            
7AC6: FF         RST     0X38            
7AC7: FF         RST     0X38            
7AC8: FF         RST     0X38            
7AC9: FF         RST     0X38            
7ACA: FF         RST     0X38            
7ACB: FF         RST     0X38            
7ACC: FF         RST     0X38            
7ACD: FF         RST     0X38            
7ACE: FF         RST     0X38            
7ACF: FF         RST     0X38            
7AD0: FF         RST     0X38            
7AD1: FF         RST     0X38            
7AD2: FF         RST     0X38            
7AD3: FF         RST     0X38            
7AD4: FF         RST     0X38            
7AD5: FF         RST     0X38            
7AD6: FF         RST     0X38            
7AD7: FF         RST     0X38            
7AD8: FF         RST     0X38            
7AD9: FF         RST     0X38            
7ADA: FF         RST     0X38            
7ADB: FF         RST     0X38            
7ADC: FF         RST     0X38            
7ADD: FF         RST     0X38            
7ADE: FF         RST     0X38            
7ADF: FF         RST     0X38            
7AE0: FF         RST     0X38            
7AE1: FF         RST     0X38            
7AE2: FF         RST     0X38            
7AE3: FF         RST     0X38            
7AE4: FF         RST     0X38            
7AE5: FF         RST     0X38            
7AE6: FF         RST     0X38            
7AE7: FF         RST     0X38            
7AE8: FF         RST     0X38            
7AE9: FF         RST     0X38            
7AEA: FF         RST     0X38            
7AEB: FF         RST     0X38            
7AEC: FF         RST     0X38            
7AED: FF         RST     0X38            
7AEE: FF         RST     0X38            
7AEF: FF         RST     0X38            
7AF0: FF         RST     0X38            
7AF1: FF         RST     0X38            
7AF2: FF         RST     0X38            
7AF3: FF         RST     0X38            
7AF4: FF         RST     0X38            
7AF5: FF         RST     0X38            
7AF6: FF         RST     0X38            
7AF7: FF         RST     0X38            
7AF8: FF         RST     0X38            
7AF9: FF         RST     0X38            
7AFA: FF         RST     0X38            
7AFB: FF         RST     0X38            
7AFC: FF         RST     0X38            
7AFD: FF         RST     0X38            
7AFE: FF         RST     0X38            
7AFF: FF         RST     0X38            
7B00: FF         RST     0X38            
7B01: FF         RST     0X38            
7B02: FF         RST     0X38            
7B03: FF         RST     0X38            
7B04: FF         RST     0X38            
7B05: FF         RST     0X38            
7B06: FF         RST     0X38            
7B07: FF         RST     0X38            
7B08: FF         RST     0X38            
7B09: FF         RST     0X38            
7B0A: FF         RST     0X38            
7B0B: FF         RST     0X38            
7B0C: FF         RST     0X38            
7B0D: FF         RST     0X38            
7B0E: FF         RST     0X38            
7B0F: FF         RST     0X38            
7B10: FF         RST     0X38            
7B11: FF         RST     0X38            
7B12: FF         RST     0X38            
7B13: FF         RST     0X38            
7B14: FF         RST     0X38            
7B15: FF         RST     0X38            
7B16: FF         RST     0X38            
7B17: FF         RST     0X38            
7B18: FF         RST     0X38            
7B19: FF         RST     0X38            
7B1A: FF         RST     0X38            
7B1B: FF         RST     0X38            
7B1C: FF         RST     0X38            
7B1D: FF         RST     0X38            
7B1E: FF         RST     0X38            
7B1F: FF         RST     0X38            
7B20: FF         RST     0X38            
7B21: FF         RST     0X38            
7B22: FF         RST     0X38            
7B23: FF         RST     0X38            
7B24: FF         RST     0X38            
7B25: FF         RST     0X38            
7B26: FF         RST     0X38            
7B27: FF         RST     0X38            
7B28: FF         RST     0X38            
7B29: FF         RST     0X38            
7B2A: FF         RST     0X38            
7B2B: FF         RST     0X38            
7B2C: FF         RST     0X38            
7B2D: FF         RST     0X38            
7B2E: FF         RST     0X38            
7B2F: FF         RST     0X38            
7B30: FF         RST     0X38            
7B31: FF         RST     0X38            
7B32: FF         RST     0X38            
7B33: FF         RST     0X38            
7B34: FF         RST     0X38            
7B35: FF         RST     0X38            
7B36: FF         RST     0X38            
7B37: FF         RST     0X38            
7B38: FF         RST     0X38            
7B39: FF         RST     0X38            
7B3A: FF         RST     0X38            
7B3B: FF         RST     0X38            
7B3C: FF         RST     0X38            
7B3D: FF         RST     0X38            
7B3E: FF         RST     0X38            
7B3F: FF         RST     0X38            
7B40: FF         RST     0X38            
7B41: FF         RST     0X38            
7B42: FF         RST     0X38            
7B43: FF         RST     0X38            
7B44: FF         RST     0X38            
7B45: FF         RST     0X38            
7B46: FF         RST     0X38            
7B47: FF         RST     0X38            
7B48: FF         RST     0X38            
7B49: FF         RST     0X38            
7B4A: FF         RST     0X38            
7B4B: FF         RST     0X38            
7B4C: FF         RST     0X38            
7B4D: FF         RST     0X38            
7B4E: FF         RST     0X38            
7B4F: FF         RST     0X38            
7B50: FF         RST     0X38            
7B51: FF         RST     0X38            
7B52: FF         RST     0X38            
7B53: FF         RST     0X38            
7B54: FF         RST     0X38            
7B55: FF         RST     0X38            
7B56: FF         RST     0X38            
7B57: FF         RST     0X38            
7B58: FF         RST     0X38            
7B59: FF         RST     0X38            
7B5A: FF         RST     0X38            
7B5B: FF         RST     0X38            
7B5C: FF         RST     0X38            
7B5D: FF         RST     0X38            
7B5E: FF         RST     0X38            
7B5F: FF         RST     0X38            
7B60: FF         RST     0X38            
7B61: FF         RST     0X38            
7B62: FF         RST     0X38            
7B63: FF         RST     0X38            
7B64: FF         RST     0X38            
7B65: FF         RST     0X38            
7B66: FF         RST     0X38            
7B67: FF         RST     0X38            
7B68: FF         RST     0X38            
7B69: FF         RST     0X38            
7B6A: FF         RST     0X38            
7B6B: FF         RST     0X38            
7B6C: FF         RST     0X38            
7B6D: FF         RST     0X38            
7B6E: FF         RST     0X38            
7B6F: FF         RST     0X38            
7B70: FF         RST     0X38            
7B71: FF         RST     0X38            
7B72: FF         RST     0X38            
7B73: FF         RST     0X38            
7B74: FF         RST     0X38            
7B75: FF         RST     0X38            
7B76: FF         RST     0X38            
7B77: FF         RST     0X38            
7B78: FF         RST     0X38            
7B79: FF         RST     0X38            
7B7A: FF         RST     0X38            
7B7B: FF         RST     0X38            
7B7C: FF         RST     0X38            
7B7D: FF         RST     0X38            
7B7E: FF         RST     0X38            
7B7F: FF         RST     0X38            
7B80: FF         RST     0X38            
7B81: FF         RST     0X38            
7B82: FF         RST     0X38            
7B83: FF         RST     0X38            
7B84: FF         RST     0X38            
7B85: FF         RST     0X38            
7B86: FF         RST     0X38            
7B87: FF         RST     0X38            
7B88: FF         RST     0X38            
7B89: FF         RST     0X38            
7B8A: FF         RST     0X38            
7B8B: FF         RST     0X38            
7B8C: FF         RST     0X38            
7B8D: FF         RST     0X38            
7B8E: FF         RST     0X38            
7B8F: FF         RST     0X38            
7B90: FF         RST     0X38            
7B91: FF         RST     0X38            
7B92: FF         RST     0X38            
7B93: FF         RST     0X38            
7B94: FF         RST     0X38            
7B95: FF         RST     0X38            
7B96: FF         RST     0X38            
7B97: FF         RST     0X38            
7B98: FF         RST     0X38            
7B99: FF         RST     0X38            
7B9A: FF         RST     0X38            
7B9B: FF         RST     0X38            
7B9C: FF         RST     0X38            
7B9D: FF         RST     0X38            
7B9E: FF         RST     0X38            
7B9F: FF         RST     0X38            
7BA0: FF         RST     0X38            
7BA1: FF         RST     0X38            
7BA2: FF         RST     0X38            
7BA3: FF         RST     0X38            
7BA4: FF         RST     0X38            
7BA5: FF         RST     0X38            
7BA6: FF         RST     0X38            
7BA7: FF         RST     0X38            
7BA8: FF         RST     0X38            
7BA9: FF         RST     0X38            
7BAA: FF         RST     0X38            
7BAB: FF         RST     0X38            
7BAC: FF         RST     0X38            
7BAD: FF         RST     0X38            
7BAE: FF         RST     0X38            
7BAF: FF         RST     0X38            
7BB0: FF         RST     0X38            
7BB1: FF         RST     0X38            
7BB2: FF         RST     0X38            
7BB3: FF         RST     0X38            
7BB4: FF         RST     0X38            
7BB5: FF         RST     0X38            
7BB6: FF         RST     0X38            
7BB7: FF         RST     0X38            
7BB8: FF         RST     0X38            
7BB9: FF         RST     0X38            
7BBA: FF         RST     0X38            
7BBB: FF         RST     0X38            
7BBC: FF         RST     0X38            
7BBD: FF         RST     0X38            
7BBE: FF         RST     0X38            
7BBF: FF         RST     0X38            
7BC0: FF         RST     0X38            
7BC1: FF         RST     0X38            
7BC2: FF         RST     0X38            
7BC3: FF         RST     0X38            
7BC4: FF         RST     0X38            
7BC5: FF         RST     0X38            
7BC6: FF         RST     0X38            
7BC7: FF         RST     0X38            
7BC8: FF         RST     0X38            
7BC9: FF         RST     0X38            
7BCA: FF         RST     0X38            
7BCB: FF         RST     0X38            
7BCC: FF         RST     0X38            
7BCD: FF         RST     0X38            
7BCE: FF         RST     0X38            
7BCF: FF         RST     0X38            
7BD0: FF         RST     0X38            
7BD1: FF         RST     0X38            
7BD2: FF         RST     0X38            
7BD3: FF         RST     0X38            
7BD4: FF         RST     0X38            
7BD5: FF         RST     0X38            
7BD6: FF         RST     0X38            
7BD7: FF         RST     0X38            
7BD8: FF         RST     0X38            
7BD9: FF         RST     0X38            
7BDA: FF         RST     0X38            
7BDB: FF         RST     0X38            
7BDC: FF         RST     0X38            
7BDD: FF         RST     0X38            
7BDE: FF         RST     0X38            
7BDF: FF         RST     0X38            
7BE0: FF         RST     0X38            
7BE1: FF         RST     0X38            
7BE2: FF         RST     0X38            
7BE3: FF         RST     0X38            
7BE4: FF         RST     0X38            
7BE5: FF         RST     0X38            
7BE6: FF         RST     0X38            
7BE7: FF         RST     0X38            
7BE8: FF         RST     0X38            
7BE9: FF         RST     0X38            
7BEA: FF         RST     0X38            
7BEB: FF         RST     0X38            
7BEC: FF         RST     0X38            
7BED: FF         RST     0X38            
7BEE: FF         RST     0X38            
7BEF: FF         RST     0X38            
7BF0: FF         RST     0X38            
7BF1: FF         RST     0X38            
7BF2: FF         RST     0X38            
7BF3: FF         RST     0X38            
7BF4: FF         RST     0X38            
7BF5: FF         RST     0X38            
7BF6: FF         RST     0X38            
7BF7: FF         RST     0X38            
7BF8: FF         RST     0X38            
7BF9: FF         RST     0X38            
7BFA: FF         RST     0X38            
7BFB: FF         RST     0X38            
7BFC: FF         RST     0X38            
7BFD: FF         RST     0X38            
7BFE: FF         RST     0X38            
7BFF: FF         RST     0X38            
7C00: FF         RST     0X38            
7C01: FF         RST     0X38            
7C02: FF         RST     0X38            
7C03: FF         RST     0X38            
7C04: FF         RST     0X38            
7C05: FF         RST     0X38            
7C06: FF         RST     0X38            
7C07: FF         RST     0X38            
7C08: FF         RST     0X38            
7C09: FF         RST     0X38            
7C0A: FF         RST     0X38            
7C0B: FF         RST     0X38            
7C0C: FF         RST     0X38            
7C0D: FF         RST     0X38            
7C0E: FF         RST     0X38            
7C0F: FF         RST     0X38            
7C10: FF         RST     0X38            
7C11: FF         RST     0X38            
7C12: FF         RST     0X38            
7C13: FF         RST     0X38            
7C14: FF         RST     0X38            
7C15: FF         RST     0X38            
7C16: FF         RST     0X38            
7C17: FF         RST     0X38            
7C18: FF         RST     0X38            
7C19: FF         RST     0X38            
7C1A: FF         RST     0X38            
7C1B: FF         RST     0X38            
7C1C: FF         RST     0X38            
7C1D: FF         RST     0X38            
7C1E: FF         RST     0X38            
7C1F: FF         RST     0X38            
7C20: FF         RST     0X38            
7C21: FF         RST     0X38            
7C22: FF         RST     0X38            
7C23: FF         RST     0X38            
7C24: FF         RST     0X38            
7C25: FF         RST     0X38            
7C26: FF         RST     0X38            
7C27: FF         RST     0X38            
7C28: FF         RST     0X38            
7C29: FF         RST     0X38            
7C2A: FF         RST     0X38            
7C2B: FF         RST     0X38            
7C2C: FF         RST     0X38            
7C2D: FF         RST     0X38            
7C2E: FF         RST     0X38            
7C2F: FF         RST     0X38            
7C30: FF         RST     0X38            
7C31: FF         RST     0X38            
7C32: FF         RST     0X38            
7C33: FF         RST     0X38            
7C34: FF         RST     0X38            
7C35: FF         RST     0X38            
7C36: FF         RST     0X38            
7C37: FF         RST     0X38            
7C38: FF         RST     0X38            
7C39: FF         RST     0X38            
7C3A: FF         RST     0X38            
7C3B: FF         RST     0X38            
7C3C: FF         RST     0X38            
7C3D: FF         RST     0X38            
7C3E: FF         RST     0X38            
7C3F: FF         RST     0X38            
7C40: FF         RST     0X38            
7C41: FF         RST     0X38            
7C42: FF         RST     0X38            
7C43: FF         RST     0X38            
7C44: FF         RST     0X38            
7C45: FF         RST     0X38            
7C46: FF         RST     0X38            
7C47: FF         RST     0X38            
7C48: FF         RST     0X38            
7C49: FF         RST     0X38            
7C4A: FF         RST     0X38            
7C4B: FF         RST     0X38            
7C4C: FF         RST     0X38            
7C4D: FF         RST     0X38            
7C4E: FF         RST     0X38            
7C4F: FF         RST     0X38            
7C50: FF         RST     0X38            
7C51: FF         RST     0X38            
7C52: FF         RST     0X38            
7C53: FF         RST     0X38            
7C54: FF         RST     0X38            
7C55: FF         RST     0X38            
7C56: FF         RST     0X38            
7C57: FF         RST     0X38            
7C58: FF         RST     0X38            
7C59: FF         RST     0X38            
7C5A: FF         RST     0X38            
7C5B: FF         RST     0X38            
7C5C: FF         RST     0X38            
7C5D: FF         RST     0X38            
7C5E: FF         RST     0X38            
7C5F: FF         RST     0X38            
7C60: FF         RST     0X38            
7C61: FF         RST     0X38            
7C62: FF         RST     0X38            
7C63: FF         RST     0X38            
7C64: FF         RST     0X38            
7C65: FF         RST     0X38            
7C66: FF         RST     0X38            
7C67: FF         RST     0X38            
7C68: FF         RST     0X38            
7C69: FF         RST     0X38            
7C6A: FF         RST     0X38            
7C6B: FF         RST     0X38            
7C6C: FF         RST     0X38            
7C6D: FF         RST     0X38            
7C6E: FF         RST     0X38            
7C6F: FF         RST     0X38            
7C70: FF         RST     0X38            
7C71: FF         RST     0X38            
7C72: FF         RST     0X38            
7C73: FF         RST     0X38            
7C74: FF         RST     0X38            
7C75: FF         RST     0X38            
7C76: FF         RST     0X38            
7C77: FF         RST     0X38            
7C78: FF         RST     0X38            
7C79: FF         RST     0X38            
7C7A: FF         RST     0X38            
7C7B: FF         RST     0X38            
7C7C: FF         RST     0X38            
7C7D: FF         RST     0X38            
7C7E: FF         RST     0X38            
7C7F: FF         RST     0X38            
7C80: FF         RST     0X38            
7C81: FF         RST     0X38            
7C82: FF         RST     0X38            
7C83: FF         RST     0X38            
7C84: FF         RST     0X38            
7C85: FF         RST     0X38            
7C86: FF         RST     0X38            
7C87: FF         RST     0X38            
7C88: FF         RST     0X38            
7C89: FF         RST     0X38            
7C8A: FF         RST     0X38            
7C8B: FF         RST     0X38            
7C8C: FF         RST     0X38            
7C8D: FF         RST     0X38            
7C8E: FF         RST     0X38            
7C8F: FF         RST     0X38            
7C90: FF         RST     0X38            
7C91: FF         RST     0X38            
7C92: FF         RST     0X38            
7C93: FF         RST     0X38            
7C94: FF         RST     0X38            
7C95: FF         RST     0X38            
7C96: FF         RST     0X38            
7C97: FF         RST     0X38            
7C98: FF         RST     0X38            
7C99: FF         RST     0X38            
7C9A: FF         RST     0X38            
7C9B: FF         RST     0X38            
7C9C: FF         RST     0X38            
7C9D: FF         RST     0X38            
7C9E: FF         RST     0X38            
7C9F: FF         RST     0X38            
7CA0: FF         RST     0X38            
7CA1: FF         RST     0X38            
7CA2: FF         RST     0X38            
7CA3: FF         RST     0X38            
7CA4: FF         RST     0X38            
7CA5: FF         RST     0X38            
7CA6: FF         RST     0X38            
7CA7: FF         RST     0X38            
7CA8: FF         RST     0X38            
7CA9: FF         RST     0X38            
7CAA: FF         RST     0X38            
7CAB: FF         RST     0X38            
7CAC: FF         RST     0X38            
7CAD: FF         RST     0X38            
7CAE: FF         RST     0X38            
7CAF: FF         RST     0X38            
7CB0: FF         RST     0X38            
7CB1: FF         RST     0X38            
7CB2: FF         RST     0X38            
7CB3: FF         RST     0X38            
7CB4: FF         RST     0X38            
7CB5: FF         RST     0X38            
7CB6: FF         RST     0X38            
7CB7: FF         RST     0X38            
7CB8: FF         RST     0X38            
7CB9: FF         RST     0X38            
7CBA: FF         RST     0X38            
7CBB: FF         RST     0X38            
7CBC: FF         RST     0X38            
7CBD: FF         RST     0X38            
7CBE: FF         RST     0X38            
7CBF: FF         RST     0X38            
7CC0: FF         RST     0X38            
7CC1: FF         RST     0X38            
7CC2: FF         RST     0X38            
7CC3: FF         RST     0X38            
7CC4: FF         RST     0X38            
7CC5: FF         RST     0X38            
7CC6: FF         RST     0X38            
7CC7: FF         RST     0X38            
7CC8: FF         RST     0X38            
7CC9: FF         RST     0X38            
7CCA: FF         RST     0X38            
7CCB: FF         RST     0X38            
7CCC: FF         RST     0X38            
7CCD: FF         RST     0X38            
7CCE: FF         RST     0X38            
7CCF: FF         RST     0X38            
7CD0: FF         RST     0X38            
7CD1: FF         RST     0X38            
7CD2: FF         RST     0X38            
7CD3: FF         RST     0X38            
7CD4: FF         RST     0X38            
7CD5: FF         RST     0X38            
7CD6: FF         RST     0X38            
7CD7: FF         RST     0X38            
7CD8: FF         RST     0X38            
7CD9: FF         RST     0X38            
7CDA: FF         RST     0X38            
7CDB: FF         RST     0X38            
7CDC: FF         RST     0X38            
7CDD: FF         RST     0X38            
7CDE: FF         RST     0X38            
7CDF: FF         RST     0X38            
7CE0: FF         RST     0X38            
7CE1: FF         RST     0X38            
7CE2: FF         RST     0X38            
7CE3: FF         RST     0X38            
7CE4: FF         RST     0X38            
7CE5: FF         RST     0X38            
7CE6: FF         RST     0X38            
7CE7: FF         RST     0X38            
7CE8: FF         RST     0X38            
7CE9: FF         RST     0X38            
7CEA: FF         RST     0X38            
7CEB: FF         RST     0X38            
7CEC: FF         RST     0X38            
7CED: FF         RST     0X38            
7CEE: FF         RST     0X38            
7CEF: FF         RST     0X38            
7CF0: FF         RST     0X38            
7CF1: FF         RST     0X38            
7CF2: FF         RST     0X38            
7CF3: FF         RST     0X38            
7CF4: FF         RST     0X38            
7CF5: FF         RST     0X38            
7CF6: FF         RST     0X38            
7CF7: FF         RST     0X38            
7CF8: FF         RST     0X38            
7CF9: FF         RST     0X38            
7CFA: FF         RST     0X38            
7CFB: FF         RST     0X38            
7CFC: FF         RST     0X38            
7CFD: FF         RST     0X38            
7CFE: FF         RST     0X38            
7CFF: FF         RST     0X38            
7D00: FF         RST     0X38            
7D01: FF         RST     0X38            
7D02: FF         RST     0X38            
7D03: FF         RST     0X38            
7D04: FF         RST     0X38            
7D05: FF         RST     0X38            
7D06: FF         RST     0X38            
7D07: FF         RST     0X38            
7D08: FF         RST     0X38            
7D09: FF         RST     0X38            
7D0A: FF         RST     0X38            
7D0B: FF         RST     0X38            
7D0C: FF         RST     0X38            
7D0D: FF         RST     0X38            
7D0E: FF         RST     0X38            
7D0F: FF         RST     0X38            
7D10: FF         RST     0X38            
7D11: FF         RST     0X38            
7D12: FF         RST     0X38            
7D13: FF         RST     0X38            
7D14: FF         RST     0X38            
7D15: FF         RST     0X38            
7D16: FF         RST     0X38            
7D17: FF         RST     0X38            
7D18: FF         RST     0X38            
7D19: FF         RST     0X38            
7D1A: FF         RST     0X38            
7D1B: FF         RST     0X38            
7D1C: FF         RST     0X38            
7D1D: FF         RST     0X38            
7D1E: FF         RST     0X38            
7D1F: FF         RST     0X38            
7D20: FF         RST     0X38            
7D21: FF         RST     0X38            
7D22: FF         RST     0X38            
7D23: FF         RST     0X38            
7D24: FF         RST     0X38            
7D25: FF         RST     0X38            
7D26: FF         RST     0X38            
7D27: FF         RST     0X38            
7D28: FF         RST     0X38            
7D29: FF         RST     0X38            
7D2A: FF         RST     0X38            
7D2B: FF         RST     0X38            
7D2C: FF         RST     0X38            
7D2D: FF         RST     0X38            
7D2E: FF         RST     0X38            
7D2F: FF         RST     0X38            
7D30: FF         RST     0X38            
7D31: FF         RST     0X38            
7D32: FF         RST     0X38            
7D33: FF         RST     0X38            
7D34: FF         RST     0X38            
7D35: FF         RST     0X38            
7D36: FF         RST     0X38            
7D37: FF         RST     0X38            
7D38: FF         RST     0X38            
7D39: FF         RST     0X38            
7D3A: FF         RST     0X38            
7D3B: FF         RST     0X38            
7D3C: FF         RST     0X38            
7D3D: FF         RST     0X38            
7D3E: FF         RST     0X38            
7D3F: FF         RST     0X38            
7D40: FF         RST     0X38            
7D41: FF         RST     0X38            
7D42: FF         RST     0X38            
7D43: FF         RST     0X38            
7D44: FF         RST     0X38            
7D45: FF         RST     0X38            
7D46: FF         RST     0X38            
7D47: FF         RST     0X38            
7D48: FF         RST     0X38            
7D49: FF         RST     0X38            
7D4A: FF         RST     0X38            
7D4B: FF         RST     0X38            
7D4C: FF         RST     0X38            
7D4D: FF         RST     0X38            
7D4E: FF         RST     0X38            
7D4F: FF         RST     0X38            
7D50: FF         RST     0X38            
7D51: FF         RST     0X38            
7D52: FF         RST     0X38            
7D53: FF         RST     0X38            
7D54: FF         RST     0X38            
7D55: FF         RST     0X38            
7D56: FF         RST     0X38            
7D57: FF         RST     0X38            
7D58: FF         RST     0X38            
7D59: FF         RST     0X38            
7D5A: FF         RST     0X38            
7D5B: FF         RST     0X38            
7D5C: FF         RST     0X38            
7D5D: FF         RST     0X38            
7D5E: FF         RST     0X38            
7D5F: FF         RST     0X38            
7D60: FF         RST     0X38            
7D61: FF         RST     0X38            
7D62: FF         RST     0X38            
7D63: FF         RST     0X38            
7D64: FF         RST     0X38            
7D65: FF         RST     0X38            
7D66: FF         RST     0X38            
7D67: FF         RST     0X38            
7D68: FF         RST     0X38            
7D69: FF         RST     0X38            
7D6A: FF         RST     0X38            
7D6B: FF         RST     0X38            
7D6C: FF         RST     0X38            
7D6D: FF         RST     0X38            
7D6E: FF         RST     0X38            
7D6F: FF         RST     0X38            
7D70: FF         RST     0X38            
7D71: FF         RST     0X38            
7D72: FF         RST     0X38            
7D73: FF         RST     0X38            
7D74: FF         RST     0X38            
7D75: FF         RST     0X38            
7D76: FF         RST     0X38            
7D77: FF         RST     0X38            
7D78: FF         RST     0X38            
7D79: FF         RST     0X38            
7D7A: FF         RST     0X38            
7D7B: FF         RST     0X38            
7D7C: FF         RST     0X38            
7D7D: FF         RST     0X38            
7D7E: FF         RST     0X38            
7D7F: FF         RST     0X38            
7D80: FF         RST     0X38            
7D81: FF         RST     0X38            
7D82: FF         RST     0X38            
7D83: FF         RST     0X38            
7D84: FF         RST     0X38            
7D85: FF         RST     0X38            
7D86: FF         RST     0X38            
7D87: FF         RST     0X38            
7D88: FF         RST     0X38            
7D89: FF         RST     0X38            
7D8A: FF         RST     0X38            
7D8B: FF         RST     0X38            
7D8C: FF         RST     0X38            
7D8D: FF         RST     0X38            
7D8E: FF         RST     0X38            
7D8F: FF         RST     0X38            
7D90: FF         RST     0X38            
7D91: FF         RST     0X38            
7D92: FF         RST     0X38            
7D93: FF         RST     0X38            
7D94: FF         RST     0X38            
7D95: FF         RST     0X38            
7D96: FF         RST     0X38            
7D97: FF         RST     0X38            
7D98: FF         RST     0X38            
7D99: FF         RST     0X38            
7D9A: FF         RST     0X38            
7D9B: FF         RST     0X38            
7D9C: FF         RST     0X38            
7D9D: FF         RST     0X38            
7D9E: FF         RST     0X38            
7D9F: FF         RST     0X38            
7DA0: FF         RST     0X38            
7DA1: FF         RST     0X38            
7DA2: FF         RST     0X38            
7DA3: FF         RST     0X38            
7DA4: FF         RST     0X38            
7DA5: FF         RST     0X38            
7DA6: FF         RST     0X38            
7DA7: FF         RST     0X38            
7DA8: FF         RST     0X38            
7DA9: FF         RST     0X38            
7DAA: FF         RST     0X38            
7DAB: FF         RST     0X38            
7DAC: FF         RST     0X38            
7DAD: FF         RST     0X38            
7DAE: FF         RST     0X38            
7DAF: FF         RST     0X38            
7DB0: FF         RST     0X38            
7DB1: FF         RST     0X38            
7DB2: FF         RST     0X38            
7DB3: FF         RST     0X38            
7DB4: FF         RST     0X38            
7DB5: FF         RST     0X38            
7DB6: FF         RST     0X38            
7DB7: FF         RST     0X38            
7DB8: FF         RST     0X38            
7DB9: FF         RST     0X38            
7DBA: FF         RST     0X38            
7DBB: FF         RST     0X38            
7DBC: FF         RST     0X38            
7DBD: FF         RST     0X38            
7DBE: FF         RST     0X38            
7DBF: FF         RST     0X38            
7DC0: FF         RST     0X38            
7DC1: FF         RST     0X38            
7DC2: FF         RST     0X38            
7DC3: FF         RST     0X38            
7DC4: FF         RST     0X38            
7DC5: FF         RST     0X38            
7DC6: FF         RST     0X38            
7DC7: FF         RST     0X38            
7DC8: FF         RST     0X38            
7DC9: FF         RST     0X38            
7DCA: FF         RST     0X38            
7DCB: FF         RST     0X38            
7DCC: FF         RST     0X38            
7DCD: FF         RST     0X38            
7DCE: FF         RST     0X38            
7DCF: FF         RST     0X38            
7DD0: FF         RST     0X38            
7DD1: FF         RST     0X38            
7DD2: FF         RST     0X38            
7DD3: FF         RST     0X38            
7DD4: FF         RST     0X38            
7DD5: FF         RST     0X38            
7DD6: FF         RST     0X38            
7DD7: FF         RST     0X38            
7DD8: FF         RST     0X38            
7DD9: FF         RST     0X38            
7DDA: FF         RST     0X38            
7DDB: FF         RST     0X38            
7DDC: FF         RST     0X38            
7DDD: FF         RST     0X38            
7DDE: FF         RST     0X38            
7DDF: FF         RST     0X38            
7DE0: FF         RST     0X38            
7DE1: FF         RST     0X38            
7DE2: FF         RST     0X38            
7DE3: FF         RST     0X38            
7DE4: FF         RST     0X38            
7DE5: FF         RST     0X38            
7DE6: FF         RST     0X38            
7DE7: FF         RST     0X38            
7DE8: FF         RST     0X38            
7DE9: FF         RST     0X38            
7DEA: FF         RST     0X38            
7DEB: FF         RST     0X38            
7DEC: FF         RST     0X38            
7DED: FF         RST     0X38            
7DEE: FF         RST     0X38            
7DEF: FF         RST     0X38            
7DF0: FF         RST     0X38            
7DF1: FF         RST     0X38            
7DF2: FF         RST     0X38            
7DF3: FF         RST     0X38            
7DF4: FF         RST     0X38            
7DF5: FF         RST     0X38            
7DF6: FF         RST     0X38            
7DF7: FF         RST     0X38            
7DF8: FF         RST     0X38            
7DF9: FF         RST     0X38            
7DFA: FF         RST     0X38            
7DFB: FF         RST     0X38            
7DFC: FF         RST     0X38            
7DFD: FF         RST     0X38            
7DFE: FF         RST     0X38            
7DFF: FF         RST     0X38            
7E00: FF         RST     0X38            
7E01: FF         RST     0X38            
7E02: FF         RST     0X38            
7E03: FF         RST     0X38            
7E04: FF         RST     0X38            
7E05: FF         RST     0X38            
7E06: FF         RST     0X38            
7E07: FF         RST     0X38            
7E08: FF         RST     0X38            
7E09: FF         RST     0X38            
7E0A: FF         RST     0X38            
7E0B: FF         RST     0X38            
7E0C: FF         RST     0X38            
7E0D: FF         RST     0X38            
7E0E: FF         RST     0X38            
7E0F: FF         RST     0X38            
7E10: FF         RST     0X38            
7E11: FF         RST     0X38            
7E12: FF         RST     0X38            
7E13: FF         RST     0X38            
7E14: FF         RST     0X38            
7E15: FF         RST     0X38            
7E16: FF         RST     0X38            
7E17: FF         RST     0X38            
7E18: FF         RST     0X38            
7E19: FF         RST     0X38            
7E1A: FF         RST     0X38            
7E1B: FF         RST     0X38            
7E1C: FF         RST     0X38            
7E1D: FF         RST     0X38            
7E1E: FF         RST     0X38            
7E1F: FF         RST     0X38            
7E20: FF         RST     0X38            
7E21: FF         RST     0X38            
7E22: FF         RST     0X38            
7E23: FF         RST     0X38            
7E24: FF         RST     0X38            
7E25: FF         RST     0X38            
7E26: FF         RST     0X38            
7E27: FF         RST     0X38            
7E28: FF         RST     0X38            
7E29: FF         RST     0X38            
7E2A: FF         RST     0X38            
7E2B: FF         RST     0X38            
7E2C: FF         RST     0X38            
7E2D: FF         RST     0X38            
7E2E: FF         RST     0X38            
7E2F: FF         RST     0X38            
7E30: FF         RST     0X38            
7E31: FF         RST     0X38            
7E32: FF         RST     0X38            
7E33: FF         RST     0X38            
7E34: FF         RST     0X38            
7E35: FF         RST     0X38            
7E36: FF         RST     0X38            
7E37: FF         RST     0X38            
7E38: FF         RST     0X38            
7E39: FF         RST     0X38            
7E3A: FF         RST     0X38            
7E3B: FF         RST     0X38            
7E3C: FF         RST     0X38            
7E3D: FF         RST     0X38            
7E3E: FF         RST     0X38            
7E3F: FF         RST     0X38            
7E40: FF         RST     0X38            
7E41: FF         RST     0X38            
7E42: FF         RST     0X38            
7E43: FF         RST     0X38            
7E44: FF         RST     0X38            
7E45: FF         RST     0X38            
7E46: FF         RST     0X38            
7E47: FF         RST     0X38            
7E48: FF         RST     0X38            
7E49: FF         RST     0X38            
7E4A: FF         RST     0X38            
7E4B: FF         RST     0X38            
7E4C: FF         RST     0X38            
7E4D: FF         RST     0X38            
7E4E: FF         RST     0X38            
7E4F: FF         RST     0X38            
7E50: FF         RST     0X38            
7E51: FF         RST     0X38            
7E52: FF         RST     0X38            
7E53: FF         RST     0X38            
7E54: FF         RST     0X38            
7E55: FF         RST     0X38            
7E56: FF         RST     0X38            
7E57: FF         RST     0X38            
7E58: FF         RST     0X38            
7E59: FF         RST     0X38            
7E5A: FF         RST     0X38            
7E5B: FF         RST     0X38            
7E5C: FF         RST     0X38            
7E5D: FF         RST     0X38            
7E5E: FF         RST     0X38            
7E5F: FF         RST     0X38            
7E60: FF         RST     0X38            
7E61: FF         RST     0X38            
7E62: FF         RST     0X38            
7E63: FF         RST     0X38            
7E64: FF         RST     0X38            
7E65: FF         RST     0X38            
7E66: FF         RST     0X38            
7E67: FF         RST     0X38            
7E68: FF         RST     0X38            
7E69: FF         RST     0X38            
7E6A: FF         RST     0X38            
7E6B: FF         RST     0X38            
7E6C: FF         RST     0X38            
7E6D: FF         RST     0X38            
7E6E: FF         RST     0X38            
7E6F: FF         RST     0X38            
7E70: FF         RST     0X38            
7E71: FF         RST     0X38            
7E72: FF         RST     0X38            
7E73: FF         RST     0X38            
7E74: FF         RST     0X38            
7E75: FF         RST     0X38            
7E76: FF         RST     0X38            
7E77: FF         RST     0X38            
7E78: FF         RST     0X38            
7E79: FF         RST     0X38            
7E7A: FF         RST     0X38            
7E7B: FF         RST     0X38            
7E7C: FF         RST     0X38            
7E7D: FF         RST     0X38            
7E7E: FF         RST     0X38            
7E7F: FF         RST     0X38            
7E80: FF         RST     0X38            
7E81: FF         RST     0X38            
7E82: FF         RST     0X38            
7E83: FF         RST     0X38            
7E84: FF         RST     0X38            
7E85: FF         RST     0X38            
7E86: FF         RST     0X38            
7E87: FF         RST     0X38            
7E88: FF         RST     0X38            
7E89: FF         RST     0X38            
7E8A: FF         RST     0X38            
7E8B: FF         RST     0X38            
7E8C: FF         RST     0X38            
7E8D: FF         RST     0X38            
7E8E: FF         RST     0X38            
7E8F: FF         RST     0X38            
7E90: FF         RST     0X38            
7E91: FF         RST     0X38            
7E92: FF         RST     0X38            
7E93: FF         RST     0X38            
7E94: FF         RST     0X38            
7E95: FF         RST     0X38            
7E96: FF         RST     0X38            
7E97: FF         RST     0X38            
7E98: FF         RST     0X38            
7E99: FF         RST     0X38            
7E9A: FF         RST     0X38            
7E9B: FF         RST     0X38            
7E9C: FF         RST     0X38            
7E9D: FF         RST     0X38            
7E9E: FF         RST     0X38            
7E9F: FF         RST     0X38            
7EA0: FF         RST     0X38            
7EA1: FF         RST     0X38            
7EA2: FF         RST     0X38            
7EA3: FF         RST     0X38            
7EA4: FF         RST     0X38            
7EA5: FF         RST     0X38            
7EA6: FF         RST     0X38            
7EA7: FF         RST     0X38            
7EA8: FF         RST     0X38            
7EA9: FF         RST     0X38            
7EAA: FF         RST     0X38            
7EAB: FF         RST     0X38            
7EAC: FF         RST     0X38            
7EAD: FF         RST     0X38            
7EAE: FF         RST     0X38            
7EAF: FF         RST     0X38            
7EB0: FF         RST     0X38            
7EB1: FF         RST     0X38            
7EB2: FF         RST     0X38            
7EB3: FF         RST     0X38            
7EB4: FF         RST     0X38            
7EB5: FF         RST     0X38            
7EB6: FF         RST     0X38            
7EB7: FF         RST     0X38            
7EB8: FF         RST     0X38            
7EB9: FF         RST     0X38            
7EBA: FF         RST     0X38            
7EBB: FF         RST     0X38            
7EBC: FF         RST     0X38            
7EBD: FF         RST     0X38            
7EBE: FF         RST     0X38            
7EBF: FF         RST     0X38            
7EC0: FF         RST     0X38            
7EC1: FF         RST     0X38            
7EC2: FF         RST     0X38            
7EC3: FF         RST     0X38            
7EC4: FF         RST     0X38            
7EC5: FF         RST     0X38            
7EC6: FF         RST     0X38            
7EC7: FF         RST     0X38            
7EC8: FF         RST     0X38            
7EC9: FF         RST     0X38            
7ECA: FF         RST     0X38            
7ECB: FF         RST     0X38            
7ECC: FF         RST     0X38            
7ECD: FF         RST     0X38            
7ECE: FF         RST     0X38            
7ECF: FF         RST     0X38            
7ED0: FF         RST     0X38            
7ED1: FF         RST     0X38            
7ED2: FF         RST     0X38            
7ED3: FF         RST     0X38            
7ED4: FF         RST     0X38            
7ED5: FF         RST     0X38            
7ED6: FF         RST     0X38            
7ED7: FF         RST     0X38            
7ED8: FF         RST     0X38            
7ED9: FF         RST     0X38            
7EDA: FF         RST     0X38            
7EDB: FF         RST     0X38            
7EDC: FF         RST     0X38            
7EDD: FF         RST     0X38            
7EDE: FF         RST     0X38            
7EDF: FF         RST     0X38            
7EE0: FF         RST     0X38            
7EE1: FF         RST     0X38            
7EE2: FF         RST     0X38            
7EE3: FF         RST     0X38            
7EE4: FF         RST     0X38            
7EE5: FF         RST     0X38            
7EE6: FF         RST     0X38            
7EE7: FF         RST     0X38            
7EE8: FF         RST     0X38            
7EE9: FF         RST     0X38            
7EEA: FF         RST     0X38            
7EEB: FF         RST     0X38            
7EEC: FF         RST     0X38            
7EED: FF         RST     0X38            
7EEE: FF         RST     0X38            
7EEF: FF         RST     0X38            
7EF0: FF         RST     0X38            
7EF1: FF         RST     0X38            
7EF2: FF         RST     0X38            
7EF3: FF         RST     0X38            
7EF4: FF         RST     0X38            
7EF5: FF         RST     0X38            
7EF6: FF         RST     0X38            
7EF7: FF         RST     0X38            
7EF8: FF         RST     0X38            
7EF9: FF         RST     0X38            
7EFA: FF         RST     0X38            
7EFB: FF         RST     0X38            
7EFC: FF         RST     0X38            
7EFD: FF         RST     0X38            
7EFE: FF         RST     0X38            
7EFF: FF         RST     0X38            
7F00: FF         RST     0X38            
7F01: FF         RST     0X38            
7F02: FF         RST     0X38            
7F03: FF         RST     0X38            
7F04: FF         RST     0X38            
7F05: FF         RST     0X38            
7F06: FF         RST     0X38            
7F07: FF         RST     0X38            
7F08: FF         RST     0X38            
7F09: FF         RST     0X38            
7F0A: FF         RST     0X38            
7F0B: FF         RST     0X38            
7F0C: FF         RST     0X38            
7F0D: FF         RST     0X38            
7F0E: FF         RST     0X38            
7F0F: FF         RST     0X38            
7F10: FF         RST     0X38            
7F11: FF         RST     0X38            
7F12: FF         RST     0X38            
7F13: FF         RST     0X38            
7F14: FF         RST     0X38            
7F15: FF         RST     0X38            
7F16: FF         RST     0X38            
7F17: FF         RST     0X38            
7F18: FF         RST     0X38            
7F19: FF         RST     0X38            
7F1A: FF         RST     0X38            
7F1B: FF         RST     0X38            
7F1C: FF         RST     0X38            
7F1D: FF         RST     0X38            
7F1E: FF         RST     0X38            
7F1F: FF         RST     0X38            
7F20: FF         RST     0X38            
7F21: FF         RST     0X38            
7F22: FF         RST     0X38            
7F23: FF         RST     0X38            
7F24: FF         RST     0X38            
7F25: FF         RST     0X38            
7F26: FF         RST     0X38            
7F27: FF         RST     0X38            
7F28: FF         RST     0X38            
7F29: FF         RST     0X38            
7F2A: FF         RST     0X38            
7F2B: FF         RST     0X38            
7F2C: FF         RST     0X38            
7F2D: FF         RST     0X38            
7F2E: FF         RST     0X38            
7F2F: FF         RST     0X38            
7F30: FF         RST     0X38            
7F31: FF         RST     0X38            
7F32: FF         RST     0X38            
7F33: FF         RST     0X38            
7F34: FF         RST     0X38            
7F35: FF         RST     0X38            
7F36: FF         RST     0X38            
7F37: FF         RST     0X38            
7F38: FF         RST     0X38            
7F39: FF         RST     0X38            
7F3A: FF         RST     0X38            
7F3B: FF         RST     0X38            
7F3C: FF         RST     0X38            
7F3D: FF         RST     0X38            
7F3E: FF         RST     0X38            
7F3F: FF         RST     0X38            
7F40: FF         RST     0X38            
7F41: FF         RST     0X38            
7F42: FF         RST     0X38            
7F43: FF         RST     0X38            
7F44: FF         RST     0X38            
7F45: FF         RST     0X38            
7F46: FF         RST     0X38            
7F47: FF         RST     0X38            
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
