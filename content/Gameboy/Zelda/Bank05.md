![Bank 05](GBZelda.jpg)

# Bank 05

>>> cpu Z80GB

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

```
4000: 70         LD      (HL),B          
4001: 00         NOP                     
4002: 70         LD      (HL),B          
4003: 20 72      JR      NZ,$4077        
4005: 00         NOP                     
4006: 72         LD      (HL),D          
4007: 20 74      JR      NZ,$407D        
4009: 00         NOP                     
400A: 76         HALT                    
400B: 00         NOP                     
400C: 78         LD      A,B             
400D: 00         NOP                     
400E: 7A         LD      A,D             
400F: 00         NOP                     
4010: 76         HALT                    
4011: 20 74      JR      NZ,$4087        
4013: 20 7A      JR      NZ,$408F        
4015: 20 78      JR      NZ,$408F        
4017: 20 7C      JR      NZ,$4095        
4019: 00         NOP                     
401A: 7C         LD      A,H             
401B: 20 40      JR      NZ,$405D        
401D: 00         NOP                     
401E: 40         LD      B,B             
401F: 20 42      JR      NZ,$4063        
4021: 00         NOP                     
4022: 42         LD      B,D             
4023: 20 44      JR      NZ,$4069        
4025: 00         NOP                     
4026: 46         LD      B,(HL)          
4027: 00         NOP                     
4028: 48         LD      C,B             
4029: 00         NOP                     
402A: 4A         LD      C,D             
402B: 00         NOP                     
402C: 46         LD      B,(HL)          
402D: 20 44      JR      NZ,$4073        
402F: 20 4A      JR      NZ,$407B        
4031: 20 48      JR      NZ,$407B        
4033: 20 4C      JR      NZ,$4081        
4035: 00         NOP                     
4036: 4C         LD      C,H             
4037: 20 79      JR      NZ,$40B2        
4039: EA 54 D1   LD      ($D154),A       
403C: FA 56 DB   LD      A,($DB56)       
403F: FE 01      CP      $01             
4041: 20 11      JR      NZ,$4054        
4043: F0 F6      LD      A,($F6)         
4045: 21 E0 C3   LD      HL,$C3E0        
4048: 09         ADD     HL,BC           
4049: 77         LD      (HL),A          
404A: 21 20 C2   LD      HL,$C220        
404D: 09         ADD     HL,BC           
404E: 70         LD      (HL),B          
404F: 21 30 C2   LD      HL,$C230        
4052: 09         ADD     HL,BC           
4053: 70         LD      (HL),B          
4054: 11 1C 40   LD      DE,$401C        
4057: FA 56 DB   LD      A,($DB56)       
405A: A7         AND     A               
405B: 20 03      JR      NZ,$4060        
405D: 11 00 40   LD      DE,$4000        
4060: CD 3B 3C   CALL    $3C3B           
4063: FA 24 C1   LD      A,($C124)       
4066: A7         AND     A               
4067: 28 15      JR      Z,$407E         
4069: FA 56 DB   LD      A,($DB56)       
406C: FE 01      CP      $01             
406E: CA A4 40   JP      Z,$40A4         
4071: 21 E0 C3   LD      HL,$C3E0        
4074: 09         ADD     HL,BC           
4075: F0 F6      LD      A,($F6)         
4077: BE         CP      (HL)            
4078: CA A7 40   JP      Z,$40A7         
407B: C3 A4 40   JP      $40A4           
407E: FA A8 C1   LD      A,($C1A8)       
4081: 21 9F C1   LD      HL,$C19F        
4084: B6         OR      (HL)            
4085: 21 4F C1   LD      HL,$C14F        
4088: B6         OR      (HL)            
4089: C2 A4 40   JP      NZ,$40A4        
408C: FA 6B C1   LD      A,($C16B)       
408F: FE 04      CP      $04             
4091: C0         RET     NZ              
4092: CD D4 44   CALL    $44D4           
4095: CD E2 08   CALL    $08E2           
4098: FA 56 DB   LD      A,($DB56)       
409B: A7         AND     A               
409C: 20 03      JR      NZ,$40A1        
409E: CD EB 3B   CALL    $3BEB           
40A1: CD A8 40   CALL    $40A8           
40A4: CD 5B 42   CALL    $425B           
40A7: C9         RET                     
40A8: 21 40 C4   LD      HL,$C440        
40AB: 09         ADD     HL,BC           
40AC: 7E         LD      A,(HL)          
40AD: C7         RST     0X00            
40AE: B2         OR      D               
40AF: 40         LD      B,B             
40B0: E9         JP      (HL)            
40B1: 40         LD      B,B             
40B2: 21 00 C2   LD      HL,$C200        
40B5: 09         ADD     HL,BC           
40B6: 7E         LD      A,(HL)          
40B7: C6 04      ADD     $04             
40B9: 77         LD      (HL),A          
40BA: 21 B0 C2   LD      HL,$C2B0        
40BD: 09         ADD     HL,BC           
40BE: 77         LD      (HL),A          
40BF: 1E 10      LD      E,$10           
40C1: 21 00 D1   LD      HL,$D100        
40C4: 22         LD      (HLI),A         
40C5: 1D         DEC     E               
40C6: 20 FC      JR      NZ,$40C4        
40C8: 21 10 C2   LD      HL,$C210        
40CB: 09         ADD     HL,BC           
40CC: 7E         LD      A,(HL)          
40CD: C6 08      ADD     $08             
40CF: 77         LD      (HL),A          
40D0: 21 C0 C2   LD      HL,$C2C0        
40D3: 09         ADD     HL,BC           
40D4: 77         LD      (HL),A          
40D5: 21 10 C3   LD      HL,$C310        
40D8: 09         ADD     HL,BC           
40D9: 96         SUB     (HL)            
40DA: 1E 10      LD      E,$10           
40DC: 21 10 D1   LD      HL,$D110        
40DF: 22         LD      (HLI),A         
40E0: 1D         DEC     E               
40E1: 20 FC      JR      NZ,$40DF        
40E3: 21 40 C4   LD      HL,$C440        
40E6: 09         ADD     HL,BC           
40E7: 34         INC     (HL)            
40E8: C9         RET                     
40E9: FA 56 DB   LD      A,($DB56)       
40EC: A7         AND     A               
40ED: 28 4B      JR      Z,$413A         
40EF: FE 80      CP      $80             
40F1: 28 0A      JR      Z,$40FD         
40F3: F0 98      LD      A,($98)         
40F5: E0 D7      LDFF00  ($D7),A         
40F7: F0 B3      LD      A,($B3)         
40F9: E0 D8      LDFF00  ($D8),A         
40FB: 18 2F      JR      $412C           
40FD: F0 99      LD      A,($99)         
40FF: D6 40      SUB     $40             
4101: C6 10      ADD     $10             
4103: FE 20      CP      $20             
4105: 30 23      JR      NC,$412A        
4107: F0 98      LD      A,($98)         
4109: D6 88      SUB     $88             
410B: C6 10      ADD     $10             
410D: FE 20      CP      $20             
410F: 30 19      JR      NC,$412A        
4111: FA 33 C1   LD      A,($C133)       
4114: A7         AND     A               
4115: 28 13      JR      Z,$412A         
4117: 3E 10      LD      A,$10           
4119: EA 68 D3   LD      ($D368),A       
411C: 3E 6C      LD      A,$6C           
411E: CD 85 21   CALL    $2185           
4121: 3E 18      LD      A,$18           
4123: E0 F3      LDFF00  ($F3),A         
4125: 3E 01      LD      A,$01           
4127: EA 56 DB   LD      ($DB56),A       
412A: 18 0E      JR      $413A           
412C: F0 D7      LD      A,($D7)         
412E: 21 B0 C2   LD      HL,$C2B0        
4131: 09         ADD     HL,BC           
4132: 77         LD      (HL),A          
4133: F0 D8      LD      A,($D8)         
4135: 21 C0 C2   LD      HL,$C2C0        
4138: 09         ADD     HL,BC           
4139: 77         LD      (HL),A          
413A: 21 B0 C2   LD      HL,$C2B0        
413D: 09         ADD     HL,BC           
413E: 7E         LD      A,(HL)          
413F: EA 50 D1   LD      ($D150),A       
4142: 21 C0 C2   LD      HL,$C2C0        
4145: 09         ADD     HL,BC           
4146: 7E         LD      A,(HL)          
4147: EA 51 D1   LD      ($D151),A       
414A: CD 0A 7A   CALL    $7A0A           
414D: 21 20 C3   LD      HL,$C320        
4150: 09         ADD     HL,BC           
4151: 35         DEC     (HL)            
4152: 35         DEC     (HL)            
4153: E5         PUSH    HL              
4154: D1         POP     DE              
4155: 21 10 C3   LD      HL,$C310        
4158: 09         ADD     HL,BC           
4159: 7E         LD      A,(HL)          
415A: E6 80      AND     $80             
415C: E0 E8      LDFF00  ($E8),A         
415E: 28 03      JR      Z,$4163         
4160: AF         XOR     A               
4161: 77         LD      (HL),A          
4162: 12         LD      (DE),A          
4163: CD 9E 3B   CALL    $3B9E           
4166: F0 F0      LD      A,($F0)         
4168: C7         RST     0X00            
4169: 83         ADD     A,E             
416A: 41         LD      B,C             
416B: D4 41 F1   CALL    NC,$F141        
416E: 41         LD      B,C             
416F: 16 42      LD      D,$42           
4171: F1         POP     AF              
4172: 41         LD      B,C             
4173: 04         INC     B               
4174: 08 0C 08   LD      ($080C),SP      
4177: FC         ???                     
4178: F8 F4      LDHL    SP,$F4          
417A: F8 F4      LDHL    SP,$F4          
417C: F8 04      LDHL    SP,$04          
417E: 08 0C 08   LD      ($080C),SP      
4181: FC         ???                     
4182: F8 CD      LDHL    SP,$CD          
4184: 91         SUB     C               
4185: 08 28 2C   LD      ($2C28),SP      
4188: CD 8C 08   CALL    $088C           
418B: 20 26      JR      NZ,$41B3        
418D: CD ED 27   CALL    $27ED           
4190: E6 3F      AND     $3F             
4192: C6 20      ADD     $20             
4194: 77         LD      (HL),A          
4195: CD 8D 3B   CALL    $3B8D           
4198: CD ED 27   CALL    $27ED           
419B: E6 07      AND     $07             
419D: 5F         LD      E,A             
419E: 50         LD      D,B             
419F: 21 73 41   LD      HL,$4173        
41A2: 19         ADD     HL,DE           
41A3: 7E         LD      A,(HL)          
41A4: 21 40 C2   LD      HL,$C240        
41A7: 09         ADD     HL,BC           
41A8: 77         LD      (HL),A          
41A9: 21 7B 41   LD      HL,$417B        
41AC: 19         ADD     HL,DE           
41AD: 7E         LD      A,(HL)          
41AE: 21 50 C2   LD      HL,$C250        
41B1: 09         ADD     HL,BC           
41B2: 77         LD      (HL),A          
41B3: C9         RET                     
41B4: CD 91 08   CALL    $0891           
41B7: 36 28      LD      (HL),$28        
41B9: FA 56 DB   LD      A,($DB56)       
41BC: A7         AND     A               
41BD: 28 04      JR      Z,$41C3         
41BF: CD A0 42   CALL    $42A0           
41C2: C9         RET                     
41C3: 21 20 C3   LD      HL,$C320        
41C6: 09         ADD     HL,BC           
41C7: 36 20      LD      (HL),$20        
41C9: CD 8D 3B   CALL    $3B8D           
41CC: 36 02      LD      (HL),$02        
41CE: 3E 20      LD      A,$20           
41D0: CD 25 3C   CALL    $3C25           
41D3: C9         RET                     
41D4: CD 8C 08   CALL    $088C           
41D7: 20 06      JR      NZ,$41DF        
41D9: 36 20      LD      (HL),$20        
41DB: CD 8D 3B   CALL    $3B8D           
41DE: 70         LD      (HL),B          
41DF: F0 E8      LD      A,($E8)         
41E1: A7         AND     A               
41E2: 28 06      JR      Z,$41EA         
41E4: 21 20 C3   LD      HL,$C320        
41E7: 09         ADD     HL,BC           
41E8: 36 10      LD      (HL),$10        
41EA: CD D1 79   CALL    $79D1           
41ED: CD 30 42   CALL    $4230           
41F0: C9         RET                     
41F1: CD 91 08   CALL    $0891           
41F4: 28 09      JR      Z,$41FF         
41F6: CD D1 79   CALL    $79D1           
41F9: CD 30 42   CALL    $4230           
41FC: 1D         DEC     E               
41FD: 28 0D      JR      Z,$420C         
41FF: CD AF 3D   CALL    $3DAF           
4202: CD 8D 3B   CALL    $3B8D           
4205: 36 03      LD      (HL),$03        
4207: CD 91 08   CALL    $0891           
420A: 36 10      LD      (HL),$10        
420C: FA 56 DB   LD      A,($DB56)       
420F: A7         AND     A               
4210: 28 03      JR      Z,$4215         
4212: CD 3E 43   CALL    $433E           
4215: C9         RET                     
4216: CD 91 08   CALL    $0891           
4219: 20 14      JR      NZ,$422F        
421B: CD ED 27   CALL    $27ED           
421E: E6 3F      AND     $3F             
4220: C6 30      ADD     $30             
4222: 77         LD      (HL),A          
4223: FA 56 DB   LD      A,($DB56)       
4226: A7         AND     A               
4227: 28 02      JR      Z,$422B         
4229: 36 10      LD      (HL),$10        
422B: CD 8D 3B   CALL    $3B8D           
422E: 70         LD      (HL),B          
422F: C9         RET                     
4230: 1E 01      LD      E,$01           
4232: 21 B0 C2   LD      HL,$C2B0        
4235: 09         ADD     HL,BC           
4236: 7E         LD      A,(HL)          
4237: 21 00 C2   LD      HL,$C200        
423A: 09         ADD     HL,BC           
423B: 96         SUB     (HL)            
423C: C6 20      ADD     $20             
423E: FE 40      CP      $40             
4240: 38 04      JR      C,$4246         
4242: F0 EE      LD      A,($EE)         
4244: 77         LD      (HL),A          
4245: 1C         INC     E               
4246: 21 C0 C2   LD      HL,$C2C0        
4249: 09         ADD     HL,BC           
424A: 7E         LD      A,(HL)          
424B: 21 10 C2   LD      HL,$C210        
424E: 09         ADD     HL,BC           
424F: 96         SUB     (HL)            
4250: C6 20      ADD     $20             
4252: FE 40      CP      $40             
4254: 38 04      JR      C,$425A         
4256: F0 EF      LD      A,($EF)         
4258: 77         LD      (HL),A          
4259: 1C         INC     E               
425A: C9         RET                     
425B: CD B1 43   CALL    $43B1           
425E: CD 07 44   CALL    $4407           
4261: FA C0 C3   LD      A,($C3C0)       
4264: 5F         LD      E,A             
4265: 16 00      LD      D,$00           
4267: 21 30 C0   LD      HL,$C030        
426A: 19         ADD     HL,DE           
426B: E5         PUSH    HL              
426C: D1         POP     DE              
426D: C5         PUSH    BC              
426E: 0E 05      LD      C,$05           
4270: F0 E7      LD      A,($E7)         
4272: A9         XOR     C               
4273: 1F         RRA                     
4274: 38 20      JR      C,$4296         
4276: 21 10 D1   LD      HL,$D110        
4279: 09         ADD     HL,BC           
427A: 7E         LD      A,(HL)          
427B: 12         LD      (DE),A          
427C: 13         INC     DE              
427D: 21 00 D1   LD      HL,$D100        
4280: 09         ADD     HL,BC           
4281: 7E         LD      A,(HL)          
4282: C6 04      ADD     $04             
4284: 12         LD      (DE),A          
4285: 13         INC     DE              
4286: FA 56 DB   LD      A,($DB56)       
4289: A7         AND     A               
428A: 3E 4E      LD      A,$4E           
428C: 20 02      JR      NZ,$4290        
428E: 3E 7E      LD      A,$7E           
4290: 12         LD      (DE),A          
4291: 13         INC     DE              
4292: 3E 00      LD      A,$00           
4294: 12         LD      (DE),A          
4295: 13         INC     DE              
4296: 0D         DEC     C               
4297: 20 D7      JR      NZ,$4270        
4299: C1         POP     BC              
429A: 3E 03      LD      A,$03           
429C: CD D0 3D   CALL    $3DD0           
429F: C9         RET                     
42A0: FA 56 DB   LD      A,($DB56)       
42A3: FE 80      CP      $80             
42A5: CA 38 43   JP      Z,$4338         
42A8: CD ED 27   CALL    $27ED           
42AB: 50         LD      D,B             
42AC: E6 01      AND     $01             
42AE: 20 08      JR      NZ,$42B8        
42B0: 1E 0F      LD      E,$0F           
42B2: 3E FF      LD      A,$FF           
42B4: E0 D7      LDFF00  ($D7),A         
42B6: 18 08      JR      $42C0           
42B8: 1E 00      LD      E,$00           
42BA: 3E 01      LD      A,$01           
42BC: E0 D7      LDFF00  ($D7),A         
42BE: 3E 10      LD      A,$10           
42C0: E0 D8      LDFF00  ($D8),A         
42C2: 7B         LD      A,E             
42C3: B9         CP      C               
42C4: 28 66      JR      Z,$432C         
42C6: 21 80 C2   LD      HL,$C280        
42C9: 19         ADD     HL,DE           
42CA: 7E         LD      A,(HL)          
42CB: A7         AND     A               
42CC: 28 5E      JR      Z,$432C         
42CE: FE 01      CP      $01             
42D0: 28 5A      JR      Z,$432C         
42D2: 21 B0 C3   LD      HL,$C3B0        
42D5: 19         ADD     HL,DE           
42D6: 7E         LD      A,(HL)          
42D7: 3D         DEC     A               
42D8: 28 52      JR      Z,$432C         
42DA: D5         PUSH    DE              
42DB: 21 A0 C3   LD      HL,$C3A0        
42DE: 19         ADD     HL,DE           
42DF: 5E         LD      E,(HL)          
42E0: CD E6 37   CALL    $37E6           
42E3: D1         POP     DE              
42E4: A7         AND     A               
42E5: 28 45      JR      Z,$432C         
42E7: 21 00 C2   LD      HL,$C200        
42EA: 19         ADD     HL,DE           
42EB: F0 98      LD      A,($98)         
42ED: 96         SUB     (HL)            
42EE: C6 2F      ADD     $2F             
42F0: FE 5E      CP      $5E             
42F2: 30 38      JR      NC,$432C        
42F4: 21 10 C2   LD      HL,$C210        
42F7: 19         ADD     HL,DE           
42F8: F0 99      LD      A,($99)         
42FA: 96         SUB     (HL)            
42FB: C6 2F      ADD     $2F             
42FD: FE 5E      CP      $5E             
42FF: 30 2B      JR      NC,$432C        
4301: 7B         LD      A,E             
4302: EA 52 D1   LD      ($D152),A       
4305: F0 99      LD      A,($99)         
4307: F5         PUSH    AF              
4308: F0 98      LD      A,($98)         
430A: F5         PUSH    AF              
430B: 7E         LD      A,(HL)          
430C: E0 99      LDFF00  ($99),A         
430E: 21 00 C2   LD      HL,$C200        
4311: 19         ADD     HL,DE           
4312: 7E         LD      A,(HL)          
4313: E0 98      LDFF00  ($98),A         
4315: 3E 30      LD      A,$30           
4317: CD 25 3C   CALL    $3C25           
431A: F1         POP     AF              
431B: E0 98      LDFF00  ($98),A         
431D: F1         POP     AF              
431E: E0 99      LDFF00  ($99),A         
4320: 21 20 C3   LD      HL,$C320        
4323: 09         ADD     HL,BC           
4324: 36 10      LD      (HL),$10        
4326: CD 8D 3B   CALL    $3B8D           
4329: 36 04      LD      (HL),$04        
432B: C9         RET                     
432C: 21 D7 FF   LD      HL,$FFD7        
432F: 7B         LD      A,E             
4330: 86         ADD     A,(HL)          
4331: 5F         LD      E,A             
4332: 21 D8 FF   LD      HL,$FFD8        
4335: BE         CP      (HL)            
4336: 20 8A      JR      NZ,$42C2        
4338: CD 91 08   CALL    $0891           
433B: 36 10      LD      (HL),$10        
433D: C9         RET                     
433E: FA 52 D1   LD      A,($D152)       
4341: 5F         LD      E,A             
4342: 50         LD      D,B             
4343: 21 80 C2   LD      HL,$C280        
4346: 19         ADD     HL,DE           
4347: 7E         LD      A,(HL)          
4348: A7         AND     A               
4349: C8         RET     Z               
434A: 21 00 C2   LD      HL,$C200        
434D: 19         ADD     HL,DE           
434E: F0 EE      LD      A,($EE)         
4350: 96         SUB     (HL)            
4351: C6 0E      ADD     $0E             
4353: FE 1A      CP      $1A             
4355: D0         RET     NC              
4356: 21 10 C2   LD      HL,$C210        
4359: 19         ADD     HL,DE           
435A: F0 EC      LD      A,($EC)         
435C: 96         SUB     (HL)            
435D: C6 10      ADD     $10             
435F: FE 20      CP      $20             
4361: D0         RET     NC              
4362: 21 A0 C3   LD      HL,$C3A0        
4365: 19         ADD     HL,DE           
4366: 7E         LD      A,(HL)          
4367: FE 3D      CP      $3D             
4369: 20 1E      JR      NZ,$4389        
436B: 21 40 C4   LD      HL,$C440        
436E: 19         ADD     HL,DE           
436F: 7E         LD      A,(HL)          
4370: A7         AND     A               
4371: C8         RET     Z               
4372: FA 9F C1   LD      A,($C19F)       
4375: A7         AND     A               
4376: C0         RET     NZ              
4377: CD 91 08   CALL    $0891           
437A: 70         LD      (HL),B          
437B: 21 00 C3   LD      HL,$C300        
437E: 09         ADD     HL,BC           
437F: 7E         LD      A,(HL)          
4380: A7         AND     A               
4381: C0         RET     NZ              
4382: 36 80      LD      (HL),$80        
4384: 3E 15      LD      A,$15           
4386: C3 85 21   JP      $2185           
4389: 21 20 C4   LD      HL,$C420        
438C: 19         ADD     HL,DE           
438D: 7E         LD      A,(HL)          
438E: A7         AND     A               
438F: C0         RET     NZ              
4390: 3E 03      LD      A,$03           
4392: E0 F2      LDFF00  ($F2),A         
4394: 21 A0 C3   LD      HL,$C3A0        
4397: 19         ADD     HL,DE           
4398: 7E         LD      A,(HL)          
4399: FE AD      CP      $AD             
439B: 20 0C      JR      NZ,$43A9        
439D: 21 20 C4   LD      HL,$C420        
43A0: 19         ADD     HL,DE           
43A1: 36 18      LD      (HL),$18        
43A3: 21 D0 C3   LD      HL,$C3D0        
43A6: 19         ADD     HL,DE           
43A7: 34         INC     (HL)            
43A8: C9         RET                     
43A9: C5         PUSH    BC              
43AA: D5         PUSH    DE              
43AB: C1         POP     BC              
43AC: CD 7A 3F   CALL    $3F7A           
43AF: C1         POP     BC              
43B0: C9         RET                     
43B1: 21 00 C2   LD      HL,$C200        
43B4: 09         ADD     HL,BC           
43B5: 7E         LD      A,(HL)          
43B6: EA 00 D1   LD      ($D100),A       
43B9: 21 10 C2   LD      HL,$C210        
43BC: 09         ADD     HL,BC           
43BD: 7E         LD      A,(HL)          
43BE: 21 10 C3   LD      HL,$C310        
43C1: 09         ADD     HL,BC           
43C2: 96         SUB     (HL)            
43C3: EA 10 D1   LD      ($D110),A       
43C6: 11 00 D1   LD      DE,$D100        
43C9: 21 01 D1   LD      HL,$D101        
43CC: C5         PUSH    BC              
43CD: 0E 05      LD      C,$05           
43CF: 1A         LD      A,(DE)          
43D0: 96         SUB     (HL)            
43D1: C6 07      ADD     $07             
43D3: FE 0E      CP      $0E             
43D5: 38 0A      JR      C,$43E1         
43D7: CB 7F      SET     1,E             
43D9: 20 04      JR      NZ,$43DF        
43DB: 34         INC     (HL)            
43DC: 34         INC     (HL)            
43DD: 34         INC     (HL)            
43DE: 34         INC     (HL)            
43DF: 35         DEC     (HL)            
43E0: 35         DEC     (HL)            
43E1: 23         INC     HL              
43E2: 13         INC     DE              
43E3: 0D         DEC     C               
43E4: 20 E9      JR      NZ,$43CF        
43E6: 11 10 D1   LD      DE,$D110        
43E9: 21 11 D1   LD      HL,$D111        
43EC: 0E 05      LD      C,$05           
43EE: 1A         LD      A,(DE)          
43EF: 96         SUB     (HL)            
43F0: C6 07      ADD     $07             
43F2: FE 0E      CP      $0E             
43F4: 38 0A      JR      C,$4400         
43F6: CB 7F      SET     1,E             
43F8: 20 04      JR      NZ,$43FE        
43FA: 34         INC     (HL)            
43FB: 34         INC     (HL)            
43FC: 34         INC     (HL)            
43FD: 34         INC     (HL)            
43FE: 35         DEC     (HL)            
43FF: 35         DEC     (HL)            
4400: 23         INC     HL              
4401: 13         INC     DE              
4402: 0D         DEC     C               
4403: 20 E9      JR      NZ,$43EE        
4405: C1         POP     BC              
4406: C9         RET                     
4407: FA 56 DB   LD      A,($DB56)       
440A: A7         AND     A               
440B: C8         RET     Z               
440C: FE 80      CP      $80             
440E: C8         RET     Z               
440F: F0 9B      LD      A,($9B)         
4411: 21 9A FF   LD      HL,$FF9A        
4414: B6         OR      (HL)            
4415: 21 A3 FF   LD      HL,$FFA3        
4418: B6         OR      (HL)            
4419: CA D3 44   JP      Z,$44D3         
441C: 21 B0 C2   LD      HL,$C2B0        
441F: 09         ADD     HL,BC           
4420: 7E         LD      A,(HL)          
4421: EA 06 D1   LD      ($D106),A       
4424: 21 C0 C2   LD      HL,$C2C0        
4427: 09         ADD     HL,BC           
4428: 7E         LD      A,(HL)          
4429: EA 16 D1   LD      ($D116),A       
442C: 11 06 D1   LD      DE,$D106        
442F: 21 05 D1   LD      HL,$D105        
4432: C5         PUSH    BC              
4433: 01 06 00   LD      BC,$0006        
4436: 1A         LD      A,(DE)          
4437: 96         SUB     (HL)            
4438: C6 07      ADD     $07             
443A: FE 0E      CP      $0E             
443C: 38 13      JR      C,$4451         
443E: CB 7F      SET     1,E             
4440: 20 06      JR      NZ,$4448        
4442: 34         INC     (HL)            
4443: 34         INC     (HL)            
4444: 34         INC     (HL)            
4445: 34         INC     (HL)            
4446: 34         INC     (HL)            
4447: 34         INC     (HL)            
4448: 35         DEC     (HL)            
4449: 35         DEC     (HL)            
444A: 35         DEC     (HL)            
444B: 79         LD      A,C             
444C: FE 01      CP      $01             
444E: 20 01      JR      NZ,$4451        
4450: 04         INC     B               
4451: 2B         DEC     HL              
4452: 1B         DEC     DE              
4453: 0D         DEC     C               
4454: 20 E0      JR      NZ,$4436        
4456: 11 16 D1   LD      DE,$D116        
4459: 21 15 D1   LD      HL,$D115        
445C: 0E 06      LD      C,$06           
445E: 1A         LD      A,(DE)          
445F: 96         SUB     (HL)            
4460: C6 07      ADD     $07             
4462: FE 0E      CP      $0E             
4464: 38 16      JR      C,$447C         
4466: CB 7F      SET     1,E             
4468: 20 06      JR      NZ,$4470        
446A: 34         INC     (HL)            
446B: 34         INC     (HL)            
446C: 34         INC     (HL)            
446D: 34         INC     (HL)            
446E: 34         INC     (HL)            
446F: 34         INC     (HL)            
4470: 35         DEC     (HL)            
4471: 35         DEC     (HL)            
4472: 35         DEC     (HL)            
4473: 79         LD      A,C             
4474: FE 01      CP      $01             
4476: 20 04      JR      NZ,$447C        
4478: 78         LD      A,B             
4479: F6 02      OR      $02             
447B: 47         LD      B,A             
447C: 2B         DEC     HL              
447D: 1B         DEC     DE              
447E: 0D         DEC     C               
447F: 20 DD      JR      NZ,$445E        
4481: 78         LD      A,B             
4482: E0 D7      LDFF00  ($D7),A         
4484: C1         POP     BC              
4485: E6 01      AND     $01             
4487: 28 19      JR      Z,$44A2         
4489: 21 10 D1   LD      HL,$D110        
448C: 1E 06      LD      E,$06           
448E: FA 51 D1   LD      A,($D151)       
4491: 96         SUB     (HL)            
4492: 28 07      JR      Z,$449B         
4494: CB 7F      SET     1,E             
4496: 20 02      JR      NZ,$449A        
4498: 34         INC     (HL)            
4499: 34         INC     (HL)            
449A: 35         DEC     (HL)            
449B: 23         INC     HL              
449C: 1D         DEC     E               
449D: 20 EF      JR      NZ,$448E        
449F: CD BE 44   CALL    $44BE           
44A2: F0 D7      LD      A,($D7)         
44A4: E6 02      AND     $02             
44A6: 28 2B      JR      Z,$44D3         
44A8: 21 00 D1   LD      HL,$D100        
44AB: 1E 06      LD      E,$06           
44AD: FA 50 D1   LD      A,($D150)       
44B0: 96         SUB     (HL)            
44B1: 28 07      JR      Z,$44BA         
44B3: CB 7F      SET     1,E             
44B5: 20 02      JR      NZ,$44B9        
44B7: 34         INC     (HL)            
44B8: 34         INC     (HL)            
44B9: 35         DEC     (HL)            
44BA: 23         INC     HL              
44BB: 1D         DEC     E               
44BC: 20 EF      JR      NZ,$44AD        
44BE: FA 10 D1   LD      A,($D110)       
44C1: 21 10 C3   LD      HL,$C310        
44C4: 09         ADD     HL,BC           
44C5: 86         ADD     A,(HL)          
44C6: 21 10 C2   LD      HL,$C210        
44C9: 09         ADD     HL,BC           
44CA: 77         LD      (HL),A          
44CB: FA 00 D1   LD      A,($D100)       
44CE: 21 00 C2   LD      HL,$C200        
44D1: 09         ADD     HL,BC           
44D2: 77         LD      (HL),A          
44D3: C9         RET                     
44D4: 21 40 C2   LD      HL,$C240        
44D7: 09         ADD     HL,BC           
44D8: 7E         LD      A,(HL)          
44D9: 21 50 C2   LD      HL,$C250        
44DC: 09         ADD     HL,BC           
44DD: B6         OR      (HL)            
44DE: C8         RET     Z               
44DF: 21 40 C2   LD      HL,$C240        
44E2: 09         ADD     HL,BC           
44E3: 7E         LD      A,(HL)          
44E4: 57         LD      D,A             
44E5: CB 7F      SET     1,E             
44E7: 28 02      JR      Z,$44EB         
44E9: 2F         CPL                     
44EA: 3C         INC     A               
44EB: 5F         LD      E,A             
44EC: 21 50 C2   LD      HL,$C250        
44EF: 09         ADD     HL,BC           
44F0: 7E         LD      A,(HL)          
44F1: CB 7F      SET     1,E             
44F3: 28 02      JR      Z,$44F7         
44F5: 2F         CPL                     
44F6: 3C         INC     A               
44F7: BB         CP      E               
44F8: 30 0E      JR      NC,$4508        
44FA: CB 7A      SET     1,E             
44FC: 20 04      JR      NZ,$4502        
44FE: 1E 04      LD      E,$04           
4500: 18 11      JR      $4513           
4502: 1E 02      LD      E,$02           
4504: CD 13 45   CALL    $4513           
4507: C9         RET                     
4508: CB 7E      SET     1,E             
450A: 28 05      JR      Z,$4511         
450C: 3E 06      LD      A,$06           
450E: C3 87 3B   JP      $3B87           
4511: 1E 00      LD      E,$00           
4513: F0 E7      LD      A,($E7)         
4515: 1F         RRA                     
4516: 1F         RRA                     
4517: 1F         RRA                     
4518: E6 01      AND     $01             
451A: 83         ADD     A,E             
451B: C3 87 3B   JP      $3B87           
451E: 50         LD      D,B             
451F: 00         NOP                     
4520: 52         LD      D,D             
4521: 00         NOP                     
4522: 54         LD      D,H             
4523: 00         NOP                     
4524: 56         LD      D,(HL)          
4525: 00         NOP                     
4526: 52         LD      D,D             
4527: 20 50      JR      NZ,$4579        
4529: 20 56      JR      NZ,$4581        
452B: 20 54      JR      NZ,$4581        
452D: 20 21      JR      NZ,$4550        
452F: 60         LD      H,B             
4530: C3 09 36   JP      $3609           
4533: 4C         LD      C,H             
4534: 21 80 C3   LD      HL,$C380        
4537: 09         ADD     HL,BC           
4538: 7E         LD      A,(HL)          
4539: A7         AND     A               
453A: 20 06      JR      NZ,$4542        
453C: F0 F1      LD      A,($F1)         
453E: C6 02      ADD     $02             
4540: E0 F1      LDFF00  ($F1),A         
4542: 11 1E 45   LD      DE,$451E        
4545: CD 3B 3C   CALL    $3C3B           
4548: F0 EA      LD      A,($EA)         
454A: FE 07      CP      $07             
454C: 20 13      JR      NZ,$4561        
454E: F0 E7      LD      A,($E7)         
4550: E6 1F      AND     $1F             
4552: 20 04      JR      NZ,$4558        
4554: 3E 13      LD      A,$13           
4556: E0 F3      LDFF00  ($F3),A         
4558: F0 E7      LD      A,($E7)         
455A: 1F         RRA                     
455B: 1F         RRA                     
455C: E6 01      AND     $01             
455E: C3 87 3B   JP      $3B87           
4561: CD 65 79   CALL    $7965           
4564: CD EB 3B   CALL    $3BEB           
4567: CD E2 08   CALL    $08E2           
456A: F0 F0      LD      A,($F0)         
456C: FE 03      CP      $03             
456E: 28 1A      JR      Z,$458A         
4570: CD 0A 7A   CALL    $7A0A           
4573: 21 20 C3   LD      HL,$C320        
4576: 09         ADD     HL,BC           
4577: 35         DEC     (HL)            
4578: 21 10 C3   LD      HL,$C310        
457B: 09         ADD     HL,BC           
457C: 7E         LD      A,(HL)          
457D: E6 80      AND     $80             
457F: E0 E8      LDFF00  ($E8),A         
4581: 28 07      JR      Z,$458A         
4583: AF         XOR     A               
4584: 77         LD      (HL),A          
4585: 21 20 C3   LD      HL,$C320        
4588: 09         ADD     HL,BC           
4589: 77         LD      (HL),A          
458A: 21 20 C4   LD      HL,$C420        
458D: 09         ADD     HL,BC           
458E: 7E         LD      A,(HL)          
458F: A7         AND     A               
4590: 28 37      JR      Z,$45C9         
4592: FE 08      CP      $08             
4594: 20 2B      JR      NZ,$45C1        
4596: FA 73 DB   LD      A,($DB73)       
4599: A7         AND     A               
459A: 28 1B      JR      Z,$45B7         
459C: 35         DEC     (HL)            
459D: FA 6B C1   LD      A,($C16B)       
45A0: FE 04      CP      $04             
45A2: 20 13      JR      NZ,$45B7        
45A4: CD ED 27   CALL    $27ED           
45A7: E6 3F      AND     $3F             
45A9: 20 07      JR      NZ,$45B2        
45AB: 3E 76      LD      A,$76           
45AD: CD 8E 21   CALL    $218E           
45B0: 18 05      JR      $45B7           
45B2: 3E 8F      LD      A,$8F           
45B4: CD 97 21   CALL    $2197           
45B7: 21 B0 C2   LD      HL,$C2B0        
45BA: 09         ADD     HL,BC           
45BB: 7E         LD      A,(HL)          
45BC: FE 23      CP      $23             
45BE: 28 01      JR      Z,$45C1         
45C0: 34         INC     (HL)            
45C1: CD 8D 3B   CALL    $3B8D           
45C4: 3E 02      LD      A,$02           
45C6: 77         LD      (HL),A          
45C7: E0 F0      LDFF00  ($F0),A         
45C9: CD D5 3B   CALL    $3BD5           
45CC: 30 4D      JR      NC,$461B        
45CE: F0 F0      LD      A,($F0)         
45D0: FE 03      CP      $03             
45D2: 28 47      JR      Z,$461B         
45D4: FA 9B C1   LD      A,($C19B)       
45D7: A7         AND     A               
45D8: 20 41      JR      NZ,$461B        
45DA: FA 00 DB   LD      A,($DB00)       
45DD: FE 03      CP      $03             
45DF: 20 08      JR      NZ,$45E9        
45E1: F0 CC      LD      A,($CC)         
45E3: E6 20      AND     $20             
45E5: 20 0F      JR      NZ,$45F6        
45E7: 18 32      JR      $461B           
45E9: FA 01 DB   LD      A,($DB01)       
45EC: FE 03      CP      $03             
45EE: 20 2B      JR      NZ,$461B        
45F0: F0 CC      LD      A,($CC)         
45F2: E6 10      AND     $10             
45F4: 28 25      JR      Z,$461B         
45F6: FA CF C3   LD      A,($C3CF)       
45F9: A7         AND     A               
45FA: 20 1F      JR      NZ,$461B        
45FC: 3C         INC     A               
45FD: EA CF C3   LD      ($C3CF),A       
4600: 21 80 C2   LD      HL,$C280        
4603: 09         ADD     HL,BC           
4604: 36 07      LD      (HL),$07        
4606: 21 90 C4   LD      HL,$C490        
4609: 09         ADD     HL,BC           
460A: 70         LD      (HL),B          
460B: F0 9E      LD      A,($9E)         
460D: EA 5D C1   LD      ($C15D),A       
4610: CD 91 08   CALL    $0891           
4613: 36 02      LD      (HL),$02        
4615: 21 F3 FF   LD      HL,$FFF3        
4618: 36 02      LD      (HL),$02        
461A: C9         RET                     
461B: F0 F0      LD      A,($F0)         
461D: C7         RST     0X00            
461E: 2E 46      LD      L,$46           
4620: 6F         LD      L,A             
4621: 46         LD      B,(HL)          
4622: BC         CP      H               
4623: 46         LD      B,(HL)          
4624: 5B         LD      E,E             
4625: 47         LD      B,A             
4626: 00         NOP                     
4627: 04         INC     B               
4628: 06 04      LD      B,$04           
462A: 00         NOP                     
462B: FC         ???                     
462C: FA FC AF   LD      A,($AFFC)       
462F: CD 87 3B   CALL    $3B87           
4632: CD 91 08   CALL    $0891           
4635: 20 37      JR      NZ,$466E        
4637: CD ED 27   CALL    $27ED           
463A: E6 07      AND     $07             
463C: 5F         LD      E,A             
463D: 50         LD      D,B             
463E: 21 26 46   LD      HL,$4626        
4641: 19         ADD     HL,DE           
4642: 7E         LD      A,(HL)          
4643: 21 40 C2   LD      HL,$C240        
4646: 09         ADD     HL,BC           
4647: 77         LD      (HL),A          
4648: 7B         LD      A,E             
4649: E6 04      AND     $04             
464B: 21 80 C3   LD      HL,$C380        
464E: 09         ADD     HL,BC           
464F: 77         LD      (HL),A          
4650: CD ED 27   CALL    $27ED           
4653: E6 07      AND     $07             
4655: 5F         LD      E,A             
4656: 21 26 46   LD      HL,$4626        
4659: 19         ADD     HL,DE           
465A: 7E         LD      A,(HL)          
465B: 21 50 C2   LD      HL,$C250        
465E: 09         ADD     HL,BC           
465F: 77         LD      (HL),A          
4660: CD 91 08   CALL    $0891           
4663: CD ED 27   CALL    $27ED           
4666: E6 1F      AND     $1F             
4668: C6 30      ADD     $30             
466A: 77         LD      (HL),A          
466B: CD 8D 3B   CALL    $3B8D           
466E: C9         RET                     
466F: CD D1 79   CALL    $79D1           
4672: CD 9E 3B   CALL    $3B9E           
4675: F0 E8      LD      A,($E8)         
4677: A7         AND     A               
4678: 28 17      JR      Z,$4691         
467A: CD 91 08   CALL    $0891           
467D: 20 07      JR      NZ,$4686        
467F: 36 30      LD      (HL),$30        
4681: CD 8D 3B   CALL    $3B8D           
4684: 70         LD      (HL),B          
4685: C9         RET                     
4686: 21 20 C3   LD      HL,$C320        
4689: 09         ADD     HL,BC           
468A: 36 05      LD      (HL),$05        
468C: 21 10 C3   LD      HL,$C310        
468F: 09         ADD     HL,BC           
4690: 34         INC     (HL)            
4691: F0 E7      LD      A,($E7)         
4693: 1F         RRA                     
4694: 1F         RRA                     
4695: 1F         RRA                     
4696: E6 01      AND     $01             
4698: CD 87 3B   CALL    $3B87           
469B: C9         RET                     
469C: 28 48      JR      Z,$46E6         
469E: 68         LD      L,B             
469F: 88         ADC     A,B             
46A0: 18 38      JR      $46DA           
46A2: 58         LD      E,B             
46A3: 78         LD      A,B             
46A4: 00         NOP                     
46A5: 00         NOP                     
46A6: 00         NOP                     
46A7: 00         NOP                     
46A8: A0         AND     B               
46A9: A0         AND     B               
46AA: A0         AND     B               
46AB: A0         AND     B               
46AC: 00         NOP                     
46AD: 00         NOP                     
46AE: 00         NOP                     
46AF: 00         NOP                     
46B0: 90         SUB     B               
46B1: 90         SUB     B               
46B2: 90         SUB     B               
46B3: 90         SUB     B               
46B4: 20 40      JR      NZ,$46F6        
46B6: 60         LD      H,B             
46B7: 80         ADD     A,B             
46B8: 20 40      JR      NZ,$46FA        
46BA: 60         LD      H,B             
46BB: 80         ADD     A,B             
46BC: 21 10 C3   LD      HL,$C310        
46BF: 09         ADD     HL,BC           
46C0: F0 E7      LD      A,($E7)         
46C2: A9         XOR     C               
46C3: E6 1F      AND     $1F             
46C5: B6         OR      (HL)            
46C6: 20 17      JR      NZ,$46DF        
46C8: 3E 0C      LD      A,$0C           
46CA: CD 30 3C   CALL    $3C30           
46CD: F0 D7      LD      A,($D7)         
46CF: 2F         CPL                     
46D0: 3C         INC     A               
46D1: 21 50 C2   LD      HL,$C250        
46D4: 09         ADD     HL,BC           
46D5: 77         LD      (HL),A          
46D6: F0 D8      LD      A,($D8)         
46D8: 2F         CPL                     
46D9: 3C         INC     A               
46DA: 21 40 C2   LD      HL,$C240        
46DD: 09         ADD     HL,BC           
46DE: 77         LD      (HL),A          
46DF: CD D1 79   CALL    $79D1           
46E2: CD 9E 3B   CALL    $3B9E           
46E5: F0 E7      LD      A,($E7)         
46E7: 1F         RRA                     
46E8: 1F         RRA                     
46E9: E6 01      AND     $01             
46EB: CD 87 3B   CALL    $3B87           
46EE: CD 24 7A   CALL    $7A24           
46F1: 21 80 C3   LD      HL,$C380        
46F4: 09         ADD     HL,BC           
46F5: 7B         LD      A,E             
46F6: EE 01      XOR     $01             
46F8: 77         LD      (HL),A          
46F9: 21 B0 C2   LD      HL,$C2B0        
46FC: 09         ADD     HL,BC           
46FD: 7E         LD      A,(HL)          
46FE: FE 23      CP      $23             
4700: 20 58      JR      NZ,$475A        
4702: 21 A5 DB   LD      HL,$DBA5        
4705: F0 E7      LD      A,($E7)         
4707: E6 0F      AND     $0F             
4709: B6         OR      (HL)            
470A: 20 4E      JR      NZ,$475A        
470C: 3E 6C      LD      A,$6C           
470E: 1E 07      LD      E,$07           
4710: CD 13 3C   CALL    $3C13           
4713: 38 45      JR      C,$475A         
4715: 3E 13      LD      A,$13           
4717: E0 F3      LDFF00  ($F3),A         
4719: 21 90 C2   LD      HL,$C290        
471C: 19         ADD     HL,DE           
471D: 36 03      LD      (HL),$03        
471F: 21 10 C3   LD      HL,$C310        
4722: 19         ADD     HL,DE           
4723: 36 10      LD      (HL),$10        
4725: 21 40 C3   LD      HL,$C340        
4728: 19         ADD     HL,DE           
4729: 36 12      LD      (HL),$12        
472B: 21 50 C3   LD      HL,$C350        
472E: 19         ADD     HL,DE           
472F: 36 80      LD      (HL),$80        
4731: 21 30 C4   LD      HL,$C430        
4734: 19         ADD     HL,DE           
4735: 36 40      LD      (HL),$40        
4737: C5         PUSH    BC              
4738: CD ED 27   CALL    $27ED           
473B: E6 0F      AND     $0F             
473D: 4F         LD      C,A             
473E: 21 9C 46   LD      HL,$469C        
4741: 09         ADD     HL,BC           
4742: 7E         LD      A,(HL)          
4743: 21 00 C2   LD      HL,$C200        
4746: 19         ADD     HL,DE           
4747: 77         LD      (HL),A          
4748: 21 AC 46   LD      HL,$46AC        
474B: 09         ADD     HL,BC           
474C: 7E         LD      A,(HL)          
474D: 21 10 C2   LD      HL,$C210        
4750: 19         ADD     HL,DE           
4751: 77         LD      (HL),A          
4752: D5         PUSH    DE              
4753: C1         POP     BC              
4754: 3E 18      LD      A,$18           
4756: CD 25 3C   CALL    $3C25           
4759: C1         POP     BC              
475A: C9         RET                     
475B: CD BF 3B   CALL    $3BBF           
475E: CD D1 79   CALL    $79D1           
4761: F0 EE      LD      A,($EE)         
4763: FE A9      CP      $A9             
4765: D2 6B 7A   JP      NC,$7A6B        
4768: F0 EC      LD      A,($EC)         
476A: FE 91      CP      $91             
476C: D2 6B 7A   JP      NC,$7A6B        
476F: F0 E7      LD      A,($E7)         
4771: 1F         RRA                     
4772: 1F         RRA                     
4773: E6 01      AND     $01             
4775: CD 87 3B   CALL    $3B87           
4778: 1E 00      LD      E,$00           
477A: 21 40 C2   LD      HL,$C240        
477D: 09         ADD     HL,BC           
477E: 7E         LD      A,(HL)          
477F: E6 80      AND     $80             
4781: 28 01      JR      Z,$4784         
4783: 1C         INC     E               
4784: 21 80 C3   LD      HL,$C380        
4787: 09         ADD     HL,BC           
4788: 73         LD      (HL),E          
4789: C3 C5 29   JP      $29C5           
478C: C9         RET                     
478D: F0 00      LD      A,($00)         
478F: 60         LD      H,B             
4790: 00         NOP                     
4791: F0 08      LD      A,($08)         
4793: 62         LD      H,D             
4794: 00         NOP                     
4795: 00         NOP                     
4796: 00         NOP                     
4797: 64         LD      H,H             
4798: 00         NOP                     
4799: 00         NOP                     
479A: 08 66 00   LD      ($0066),SP      
479D: F0 00      LD      A,($00)         
479F: 68         LD      L,B             
47A0: 00         NOP                     
47A1: F0 08      LD      A,($08)         
47A3: 6A         LD      L,D             
47A4: 00         NOP                     
47A5: 00         NOP                     
47A6: 00         NOP                     
47A7: 6C         LD      L,H             
47A8: 00         NOP                     
47A9: 00         NOP                     
47AA: 08 6E 00   LD      ($006E),SP      
47AD: F0 00      LD      A,($00)         
47AF: 62         LD      H,D             
47B0: 20 F0      JR      NZ,$47A2        
47B2: 08 60 20   LD      ($2060),SP      
47B5: 00         NOP                     
47B6: 00         NOP                     
47B7: 66         LD      H,(HL)          
47B8: 20 00      JR      NZ,$47BA        
47BA: 08 64 20   LD      ($2064),SP      
47BD: F0 00      LD      A,($00)         
47BF: 68         LD      L,B             
47C0: 00         NOP                     
47C1: F0 08      LD      A,($08)         
47C3: 6A         LD      L,D             
47C4: 00         NOP                     
47C5: 00         NOP                     
47C6: 00         NOP                     
47C7: 6C         LD      L,H             
47C8: 00         NOP                     
47C9: 00         NOP                     
47CA: 08 6E 00   LD      ($006E),SP      
47CD: F0 F1      LD      A,($F1)         
47CF: 17         RLA                     
47D0: 17         RLA                     
47D1: 17         RLA                     
47D2: 17         RLA                     
47D3: E6 F0      AND     $F0             
47D5: 5F         LD      E,A             
47D6: 50         LD      D,B             
47D7: 21 8D 47   LD      HL,$478D        
47DA: 19         ADD     HL,DE           
47DB: 0E 04      LD      C,$04           
47DD: CD 26 3D   CALL    $3D26           
47E0: C9         RET                     
47E1: CD CD 47   CALL    $47CD           
47E4: 21 D0 C3   LD      HL,$C3D0        
47E7: 09         ADD     HL,BC           
47E8: 34         INC     (HL)            
47E9: 7E         LD      A,(HL)          
47EA: 1F         RRA                     
47EB: 1F         RRA                     
47EC: 1F         RRA                     
47ED: 1F         RRA                     
47EE: E6 03      AND     $03             
47F0: CD 87 3B   CALL    $3B87           
47F3: CD 09 54   CALL    $5409           
47F6: F0 F0      LD      A,($F0)         
47F8: C7         RST     0X00            
47F9: 03         INC     BC              
47FA: 48         LD      C,B             
47FB: 51         LD      D,C             
47FC: 48         LD      C,B             
47FD: 63         LD      H,E             
47FE: 48         LD      C,B             
47FF: 98         SBC     B               
4800: 48         LD      C,B             
4801: C0         RET     NZ              
4802: 48         LD      C,B             
4803: FA 9F C1   LD      A,($C19F)       
4806: A7         AND     A               
4807: 20 3B      JR      NZ,$4844        
4809: FA 4B DB   LD      A,($DB4B)       
480C: A7         AND     A               
480D: 28 2C      JR      Z,$483B         
480F: CD 4C 54   CALL    $544C           
4812: 7B         LD      A,E             
4813: A7         AND     A               
4814: 28 2E      JR      Z,$4844         
4816: 21 00 DB   LD      HL,$DB00        
4819: 7E         LD      A,(HL)          
481A: FE 0C      CP      $0C             
481C: 20 0F      JR      NZ,$482D        
481E: F0 CC      LD      A,($CC)         
4820: E6 20      AND     $20             
4822: 28 20      JR      Z,$4844         
4824: AF         XOR     A               
4825: EA A9 C1   LD      ($C1A9),A       
4828: EA A8 C1   LD      ($C1A8),A       
482B: 18 0B      JR      $4838           
482D: 23         INC     HL              
482E: 7E         LD      A,(HL)          
482F: FE 0C      CP      $0C             
4831: 20 08      JR      NZ,$483B        
4833: F0 CC      LD      A,($CC)         
4835: E6 10      AND     $10             
4837: C8         RET     Z               
4838: 70         LD      (HL),B          
4839: 18 0A      JR      $4845           
483B: CD 4C 54   CALL    $544C           
483E: D0         RET     NC              
483F: 3E 0C      LD      A,$0C           
4841: CD 97 21   CALL    $2197           
4844: C9         RET                     
4845: AF         XOR     A               
4846: EA 4B DB   LD      ($DB4B),A       
4849: CD 91 08   CALL    $0891           
484C: 36 04      LD      (HL),$04        
484E: C3 8D 3B   JP      $3B8D           
4851: CD 91 08   CALL    $0891           
4854: C0         RET     NZ              
4855: 3E 09      LD      A,$09           
4857: CD 97 21   CALL    $2197           
485A: CD 91 08   CALL    $0891           
485D: 36 C0      LD      (HL),$C0        
485F: CD 8D 3B   CALL    $3B8D           
4862: C9         RET                     
4863: FA 9F C1   LD      A,($C19F)       
4866: A7         AND     A               
4867: 20 2E      JR      NZ,$4897        
4869: FA 0B C1   LD      A,($C10B)       
486C: A7         AND     A               
486D: 20 0A      JR      NZ,$4879        
486F: F0 B0      LD      A,($B0)         
4871: EA 68 D3   LD      ($D368),A       
4874: 3E 01      LD      A,$01           
4876: EA 0B C1   LD      ($C10B),A       
4879: E0 A1      LDFF00  ($A1),A         
487B: 21 D0 C3   LD      HL,$C3D0        
487E: 09         ADD     HL,BC           
487F: 34         INC     (HL)            
4880: 34         INC     (HL)            
4881: 34         INC     (HL)            
4882: 34         INC     (HL)            
4883: CD 91 08   CALL    $0891           
4886: C0         RET     NZ              
4887: EA 0B C1   LD      ($C10B),A       
488A: F0 B0      LD      A,($B0)         
488C: EA 68 D3   LD      ($D368),A       
488F: 3E FE      LD      A,$FE           
4891: CD 97 21   CALL    $2197           
4894: CD 8D 3B   CALL    $3B8D           
4897: C9         RET                     
4898: FA 9F C1   LD      A,($C19F)       
489B: A7         AND     A               
489C: C0         RET     NZ              
489D: 3E 2A      LD      A,$2A           
489F: EA AA C1   LD      ($C1AA),A       
48A2: 3E 03      LD      A,$03           
48A4: EA A9 C1   LD      ($C1A9),A       
48A7: 16 0C      LD      D,$0C           
48A9: CD 61 52   CALL    $5261           
48AC: FA 4C DB   LD      A,($DB4C)       
48AF: C6 20      ADD     $20             
48B1: 27         DAA                     
48B2: EA 4C DB   LD      ($DB4C),A       
48B5: 3E 0B      LD      A,$0B           
48B7: E0 A5      LDFF00  ($A5),A         
48B9: 3E 01      LD      A,$01           
48BB: E0 F2      LDFF00  ($F2),A         
48BD: CD 8D 3B   CALL    $3B8D           
48C0: C9         RET                     
48C1: 78         LD      A,B             
48C2: 00         NOP                     
48C3: 7A         LD      A,D             
48C4: 00         NOP                     
48C5: 7A         LD      A,D             
48C6: 20 78      JR      NZ,$4940        
48C8: 20 7C      JR      NZ,$4946        
48CA: 00         NOP                     
48CB: 7E         LD      A,(HL)          
48CC: 00         NOP                     
48CD: 78         LD      A,B             
48CE: 00         NOP                     
48CF: 7A         LD      A,D             
48D0: 00         NOP                     
48D1: 70         LD      (HL),B          
48D2: 00         NOP                     
48D3: 72         LD      (HL),D          
48D4: 00         NOP                     
48D5: 74         LD      (HL),H          
48D6: 00         NOP                     
48D7: 76         HALT                    
48D8: 00         NOP                     
48D9: 76         HALT                    
48DA: 20 74      JR      NZ,$4950        
48DC: 20 72      JR      NZ,$4950        
48DE: 20 70      JR      NZ,$4950        
48E0: 20 5A      JR      NZ,$493C        
48E2: 20 58      JR      NZ,$493C        
48E4: 20 58      JR      NZ,$493E        
48E6: 00         NOP                     
48E7: 5A         LD      E,D             
48E8: 00         NOP                     
48E9: 50         LD      D,B             
48EA: 00         NOP                     
48EB: 52         LD      D,D             
48EC: 00         NOP                     
48ED: 50         LD      D,B             
48EE: 00         NOP                     
48EF: 52         LD      D,D             
48F0: 00         NOP                     
48F1: 54         LD      D,H             
48F2: 00         NOP                     
48F3: 56         LD      D,(HL)          
48F4: 00         NOP                     
48F5: 00         NOP                     
48F6: 00         NOP                     
48F7: 20 00      JR      NZ,$48F9        
48F9: 00         NOP                     
48FA: 08 22 00   LD      ($0022),SP      
48FD: 00         NOP                     
48FE: 00         NOP                     
48FF: 20 00      JR      NZ,$4901        
4901: 00         NOP                     
4902: 08 22 00   LD      ($0022),SP      
4905: F1         POP     AF              
4906: FA 2A 00   LD      A,($002A)       
4909: F1         POP     AF              
490A: 02         LD      (BC),A          
490B: 2A         LD      A,(HLI)         
490C: 20 00      JR      NZ,$490E        
490E: 00         NOP                     
490F: 24         INC     H               
4910: 00         NOP                     
4911: 00         NOP                     
4912: 08 28 00   LD      ($0028),SP      
4915: FA 95 DB   LD      A,($DB95)       
4918: FE 01      CP      $01             
491A: 20 24      JR      NZ,$4940        
491C: 21 40 C3   LD      HL,$C340        
491F: 09         ADD     HL,BC           
4920: 36 C4      LD      (HL),$C4        
4922: 21 D0 C3   LD      HL,$C3D0        
4925: 09         ADD     HL,BC           
4926: 7E         LD      A,(HL)          
4927: 21 F5 48   LD      HL,$48F5        
492A: FE 70      CP      $70             
492C: 20 03      JR      NZ,$4931        
492E: 21 05 49   LD      HL,$4905        
4931: 0E 04      LD      C,$04           
4933: CD 26 3D   CALL    $3D26           
4936: 21 D0 C3   LD      HL,$C3D0        
4939: 09         ADD     HL,BC           
493A: 7E         LD      A,(HL)          
493B: FE 70      CP      $70             
493D: C8         RET     Z               
493E: 34         INC     (HL)            
493F: C9         RET                     
4940: FA A5 DB   LD      A,($DBA5)       
4943: A7         AND     A               
4944: C2 68 4B   JP      NZ,$4B68        
4947: F0 F8      LD      A,($F8)         
4949: E6 10      AND     $10             
494B: C2 6B 7A   JP      NZ,$7A6B        
494E: F0 F0      LD      A,($F0)         
4950: A7         AND     A               
4951: 20 29      JR      NZ,$497C        
4953: F0 E7      LD      A,($E7)         
4955: 1F         RRA                     
4956: 1F         RRA                     
4957: 1F         RRA                     
4958: 1F         RRA                     
4959: E6 01      AND     $01             
495B: CD 87 3B   CALL    $3B87           
495E: F0 99      LD      A,($99)         
4960: FE 30      CP      $30             
4962: 30 13      JR      NC,$4977        
4964: 3E 01      LD      A,$01           
4966: EA 0C C1   LD      ($C10C),A       
4969: F0 E7      LD      A,($E7)         
496B: 1F         RRA                     
496C: 1F         RRA                     
496D: 1F         RRA                     
496E: E6 01      AND     $01             
4970: C6 02      ADD     $02             
4972: CD 87 3B   CALL    $3B87           
4975: 18 05      JR      $497C           
4977: 21 40 C4   LD      HL,$C440        
497A: 09         ADD     HL,BC           
497B: 70         LD      (HL),B          
497C: 11 C1 48   LD      DE,$48C1        
497F: CD 3B 3C   CALL    $3C3B           
4982: CD 65 79   CALL    $7965           
4985: F0 F0      LD      A,($F0)         
4987: C7         RST     0X00            
4988: 90         SUB     B               
4989: 49         LD      C,C             
498A: C2 49 EC   JP      NZ,$EC49        
498D: 4A         LD      C,D             
498E: 32         LD      (HLD),A         
498F: 4B         LD      C,E             
4990: CD 09 54   CALL    $5409           
4993: F0 99      LD      A,($99)         
4995: FE 20      CP      $20             
4997: 30 0F      JR      NC,$49A8        
4999: 21 40 C4   LD      HL,$C440        
499C: 09         ADD     HL,BC           
499D: 7E         LD      A,(HL)          
499E: A7         AND     A               
499F: 20 07      JR      NZ,$49A8        
49A1: 36 01      LD      (HL),$01        
49A3: 3E 21      LD      A,$21           
49A5: C3 97 21   JP      $2197           
49A8: CD 4C 54   CALL    $544C           
49AB: 30 0A      JR      NC,$49B7        
49AD: FA 9B C1   LD      A,($C19B)       
49B0: A7         AND     A               
49B1: C0         RET     NZ              
49B2: 3E 0D      LD      A,$0D           
49B4: C3 97 21   JP      $2197           
49B7: 21 AD C1   LD      HL,$C1AD        
49BA: 70         LD      (HL),B          
49BB: C9         RET                     
49BC: 00         NOP                     
49BD: 04         INC     B               
49BE: 05         DEC     B               
49BF: 06 07      LD      B,$07           
49C1: 01 3E 02   LD      BC,$023E        
49C4: E0 A1      LDFF00  ($A1),A         
49C6: AF         XOR     A               
49C7: EA 9B C1   LD      ($C19B),A       
49CA: CD 44 7A   CALL    $7A44           
49CD: 7B         LD      A,E             
49CE: EE 01      XOR     $01             
49D0: E0 9E      LDFF00  ($9E),A         
49D2: C5         PUSH    BC              
49D3: CD 7C 08   CALL    $087C           
49D6: C1         POP     BC              
49D7: 21 D0 C2   LD      HL,$C2D0        
49DA: 09         ADD     HL,BC           
49DB: 5E         LD      E,(HL)          
49DC: 21 C0 C2   LD      HL,$C2C0        
49DF: 09         ADD     HL,BC           
49E0: 7E         LD      A,(HL)          
49E1: 83         ADD     A,E             
49E2: 77         LD      (HL),A          
49E3: 30 0C      JR      NC,$49F1        
49E5: 21 90 C3   LD      HL,$C390        
49E8: 09         ADD     HL,BC           
49E9: 7E         LD      A,(HL)          
49EA: 3C         INC     A               
49EB: FE 06      CP      $06             
49ED: 20 01      JR      NZ,$49F0        
49EF: AF         XOR     A               
49F0: 77         LD      (HL),A          
49F1: 21 90 C3   LD      HL,$C390        
49F4: 09         ADD     HL,BC           
49F5: 5E         LD      E,(HL)          
49F6: 50         LD      D,B             
49F7: 21 BC 49   LD      HL,$49BC        
49FA: 19         ADD     HL,DE           
49FB: 7E         LD      A,(HL)          
49FC: CD 87 3B   CALL    $3B87           
49FF: CD 87 08   CALL    $0887           
4A02: 20 45      JR      NZ,$4A49        
4A04: 3E 02      LD      A,$02           
4A06: CD 01 3C   CALL    $3C01           
4A09: F0 D7      LD      A,($D7)         
4A0B: 21 00 C2   LD      HL,$C200        
4A0E: 19         ADD     HL,DE           
4A0F: 77         LD      (HL),A          
4A10: F0 D8      LD      A,($D8)         
4A12: 21 10 C2   LD      HL,$C210        
4A15: 19         ADD     HL,DE           
4A16: 77         LD      (HL),A          
4A17: F0 DA      LD      A,($DA)         
4A19: 21 10 C3   LD      HL,$C310        
4A1C: 19         ADD     HL,DE           
4A1D: 77         LD      (HL),A          
4A1E: 21 40 C4   LD      HL,$C440        
4A21: 19         ADD     HL,DE           
4A22: 36 4C      LD      (HL),$4C        
4A24: 21 E0 C2   LD      HL,$C2E0        
4A27: 19         ADD     HL,DE           
4A28: 36 20      LD      (HL),$20        
4A2A: 3E 09      LD      A,$09           
4A2C: CD 87 3B   CALL    $3B87           
4A2F: 21 20 C3   LD      HL,$C320        
4A32: 09         ADD     HL,BC           
4A33: 70         LD      (HL),B          
4A34: CD 8D 3B   CALL    $3B8D           
4A37: F0 F6      LD      A,($F6)         
4A39: 5F         LD      E,A             
4A3A: 50         LD      D,B             
4A3B: 21 00 D8   LD      HL,$D800        
4A3E: 19         ADD     HL,DE           
4A3F: 7E         LD      A,(HL)          
4A40: F6 10      OR      $10             
4A42: 77         LD      (HL),A          
4A43: 3E 01      LD      A,$01           
4A45: EA 48 DB   LD      ($DB48),A       
4A48: C9         RET                     
4A49: 21 D0 C2   LD      HL,$C2D0        
4A4C: 09         ADD     HL,BC           
4A4D: F0 E7      LD      A,($E7)         
4A4F: E6 01      AND     $01             
4A51: 20 06      JR      NZ,$4A59        
4A53: 7E         LD      A,(HL)          
4A54: FE F0      CP      $F0             
4A56: 30 01      JR      NC,$4A59        
4A58: 34         INC     (HL)            
4A59: CD D1 79   CALL    $79D1           
4A5C: CD 9E 3B   CALL    $3B9E           
4A5F: CD 87 08   CALL    $0887           
4A62: FE 06      CP      $06             
4A64: 30 31      JR      NC,$4A97        
4A66: F0 EF      LD      A,($EF)         
4A68: FE 30      CP      $30             
4A6A: 30 04      JR      NC,$4A70        
4A6C: 36 08      LD      (HL),$08        
4A6E: 18 27      JR      $4A97           
4A70: 21 20 C3   LD      HL,$C320        
4A73: 09         ADD     HL,BC           
4A74: 34         INC     (HL)            
4A75: 00         NOP                     
4A76: 21 40 C2   LD      HL,$C240        
4A79: 09         ADD     HL,BC           
4A7A: 7E         LD      A,(HL)          
4A7B: A7         AND     A               
4A7C: 28 07      JR      Z,$4A85         
4A7E: E6 80      AND     $80             
4A80: 28 02      JR      Z,$4A84         
4A82: 34         INC     (HL)            
4A83: 34         INC     (HL)            
4A84: 35         DEC     (HL)            
4A85: 21 50 C2   LD      HL,$C250        
4A88: 09         ADD     HL,BC           
4A89: 7E         LD      A,(HL)          
4A8A: A7         AND     A               
4A8B: 28 07      JR      Z,$4A94         
4A8D: E6 80      AND     $80             
4A8F: 28 02      JR      Z,$4A93         
4A91: 34         INC     (HL)            
4A92: 34         INC     (HL)            
4A93: 35         DEC     (HL)            
4A94: C3 0A 7A   JP      $7A0A           
4A97: 21 A0 C2   LD      HL,$C2A0        
4A9A: 09         ADD     HL,BC           
4A9B: 7E         LD      A,(HL)          
4A9C: E6 03      AND     $03             
4A9E: 28 0C      JR      Z,$4AAC         
4AA0: 21 40 C2   LD      HL,$C240        
4AA3: 09         ADD     HL,BC           
4AA4: 7E         LD      A,(HL)          
4AA5: 2F         CPL                     
4AA6: 3C         INC     A               
4AA7: 77         LD      (HL),A          
4AA8: 3E 09      LD      A,$09           
4AAA: E0 F2      LDFF00  ($F2),A         
4AAC: 21 A0 C2   LD      HL,$C2A0        
4AAF: 09         ADD     HL,BC           
4AB0: 7E         LD      A,(HL)          
4AB1: E6 0C      AND     $0C             
4AB3: 28 0C      JR      Z,$4AC1         
4AB5: 21 50 C2   LD      HL,$C250        
4AB8: 09         ADD     HL,BC           
4AB9: 7E         LD      A,(HL)          
4ABA: 2F         CPL                     
4ABB: 3C         INC     A               
4ABC: 77         LD      (HL),A          
4ABD: 3E 09      LD      A,$09           
4ABF: E0 F2      LDFF00  ($F2),A         
4AC1: CD 87 08   CALL    $0887           
4AC4: FE 60      CP      $60             
4AC6: 30 23      JR      NC,$4AEB        
4AC8: F0 E7      LD      A,($E7)         
4ACA: E6 03      AND     $03             
4ACC: 20 1D      JR      NZ,$4AEB        
4ACE: 21 40 C2   LD      HL,$C240        
4AD1: CD D7 4A   CALL    $4AD7           
4AD4: 21 50 C2   LD      HL,$C250        
4AD7: 09         ADD     HL,BC           
4AD8: 7E         LD      A,(HL)          
4AD9: FE 30      CP      $30             
4ADB: 28 0E      JR      Z,$4AEB         
4ADD: FE D0      CP      $D0             
4ADF: 28 0A      JR      Z,$4AEB         
4AE1: 1E 01      LD      E,$01           
4AE3: CB 7F      SET     1,E             
4AE5: 28 02      JR      Z,$4AE9         
4AE7: 1E FF      LD      E,$FF           
4AE9: 83         ADD     A,E             
4AEA: 77         LD      (HL),A          
4AEB: C9         RET                     
4AEC: CD 0A 7A   CALL    $7A0A           
4AEF: 21 20 C3   LD      HL,$C320        
4AF2: 09         ADD     HL,BC           
4AF3: 35         DEC     (HL)            
4AF4: 21 10 C3   LD      HL,$C310        
4AF7: 09         ADD     HL,BC           
4AF8: 7E         LD      A,(HL)          
4AF9: E6 80      AND     $80             
4AFB: 28 34      JR      Z,$4B31         
4AFD: 70         LD      (HL),B          
4AFE: AF         XOR     A               
4AFF: EA 67 C1   LD      ($C167),A       
4B02: 3E 23      LD      A,$23           
4B04: E0 F2      LDFF00  ($F2),A         
4B06: CD BD 27   CALL    $27BD           
4B09: CD 91 08   CALL    $0891           
4B0C: 36 40      LD      (HL),$40        
4B0E: CD 44 7A   CALL    $7A44           
4B11: C6 08      ADD     $08             
4B13: CD 87 3B   CALL    $3B87           
4B16: CD 24 7A   CALL    $7A24           
4B19: C6 12      ADD     $12             
4B1B: FE 24      CP      $24             
4B1D: 30 0F      JR      NC,$4B2E        
4B1F: CD 34 7A   CALL    $7A34           
4B22: C6 12      ADD     $12             
4B24: FE 24      CP      $24             
4B26: 30 06      JR      NC,$4B2E        
4B28: 21 B0 C2   LD      HL,$C2B0        
4B2B: 09         ADD     HL,BC           
4B2C: 36 01      LD      (HL),$01        
4B2E: CD 8D 3B   CALL    $3B8D           
4B31: C9         RET                     
4B32: CD 91 08   CALL    $0891           
4B35: FE 01      CP      $01             
4B37: 20 06      JR      NZ,$4B3F        
4B39: 3E 0A      LD      A,$0A           
4B3B: CD 97 21   CALL    $2197           
4B3E: C9         RET                     
4B3F: A7         AND     A               
4B40: 20 23      JR      NZ,$4B65        
4B42: F0 E7      LD      A,($E7)         
4B44: E6 1F      AND     $1F             
4B46: 20 08      JR      NZ,$4B50        
4B48: CD 44 7A   CALL    $7A44           
4B4B: C6 08      ADD     $08             
4B4D: CD 87 3B   CALL    $3B87           
4B50: 21 B0 C2   LD      HL,$C2B0        
4B53: 09         ADD     HL,BC           
4B54: 7E         LD      A,(HL)          
4B55: A7         AND     A               
4B56: 20 03      JR      NZ,$4B5B        
4B58: CD 09 54   CALL    $5409           
4B5B: CD 4C 54   CALL    $544C           
4B5E: 30 05      JR      NC,$4B65        
4B60: 3E 0B      LD      A,$0B           
4B62: CD 97 21   CALL    $2197           
4B65: C9         RET                     
4B66: 78         LD      A,B             
4B67: 00         NOP                     
4B68: 21 C0 C2   LD      HL,$C2C0        
4B6B: 09         ADD     HL,BC           
4B6C: 7E         LD      A,(HL)          
4B6D: A7         AND     A               
4B6E: 28 28      JR      Z,$4B98         
4B70: 11 66 4B   LD      DE,$4B66        
4B73: CD D0 3C   CALL    $3CD0           
4B76: CD 65 79   CALL    $7965           
4B79: CD D1 79   CALL    $79D1           
4B7C: CD 91 08   CALL    $0891           
4B7F: CA 6B 7A   JP      Z,$7A6B         
4B82: E6 10      AND     $10             
4B84: 1E 01      LD      E,$01           
4B86: 28 02      JR      Z,$4B8A         
4B88: 1E FF      LD      E,$FF           
4B8A: F0 E7      LD      A,($E7)         
4B8C: E6 01      AND     $01             
4B8E: 20 07      JR      NZ,$4B97        
4B90: 21 40 C2   LD      HL,$C240        
4B93: 09         ADD     HL,BC           
4B94: 7E         LD      A,(HL)          
4B95: 83         ADD     A,E             
4B96: 77         LD      (HL),A          
4B97: C9         RET                     
4B98: FA 73 DB   LD      A,($DB73)       
4B9B: A7         AND     A               
4B9C: 20 10      JR      NZ,$4BAE        
4B9E: FA 67 DB   LD      A,($DB67)       
4BA1: E6 02      AND     $02             
4BA3: C2 6B 7A   JP      NZ,$7A6B        
4BA6: FA 0E DB   LD      A,($DB0E)       
4BA9: FE 04      CP      $04             
4BAB: D2 6B 7A   JP      NC,$7A6B        
4BAE: FA 48 DB   LD      A,($DB48)       
4BB1: A7         AND     A               
4BB2: 20 07      JR      NZ,$4BBB        
4BB4: FA 4E DB   LD      A,($DB4E)       
4BB7: A7         AND     A               
4BB8: C2 6B 7A   JP      NZ,$7A6B        
4BBB: FA 73 DB   LD      A,($DB73)       
4BBE: A7         AND     A               
4BBF: 20 0A      JR      NZ,$4BCB        
4BC1: FA 48 DB   LD      A,($DB48)       
4BC4: A7         AND     A               
4BC5: 28 18      JR      Z,$4BDF         
4BC7: FE 01      CP      $01             
4BC9: 20 14      JR      NZ,$4BDF        
4BCB: 21 00 C2   LD      HL,$C200        
4BCE: 09         ADD     HL,BC           
4BCF: 36 18      LD      (HL),$18        
4BD1: 21 10 C2   LD      HL,$C210        
4BD4: 09         ADD     HL,BC           
4BD5: 36 34      LD      (HL),$34        
4BD7: CD BA 3D   CALL    $3DBA           
4BDA: 11 F1 48   LD      DE,$48F1        
4BDD: 18 14      JR      $4BF3           
4BDF: CD 52 4D   CALL    $4D52           
4BE2: F0 E7      LD      A,($E7)         
4BE4: E6 1F      AND     $1F             
4BE6: 20 08      JR      NZ,$4BF0        
4BE8: CD 44 7A   CALL    $7A44           
4BEB: 21 B0 C3   LD      HL,$C3B0        
4BEE: 09         ADD     HL,BC           
4BEF: 73         LD      (HL),E          
4BF0: 11 E1 48   LD      DE,$48E1        
4BF3: CD 3B 3C   CALL    $3C3B           
4BF6: CD 65 79   CALL    $7965           
4BF9: CD 09 54   CALL    $5409           
4BFC: F0 F0      LD      A,($F0)         
4BFE: C7         RST     0X00            
4BFF: 09         ADD     HL,BC           
4C00: 4C         LD      C,H             
4C01: 32         LD      (HLD),A         
4C02: 4C         LD      C,H             
4C03: 48         LD      C,B             
4C04: 4C         LD      C,H             
4C05: 89         ADC     A,C             
4C06: 4C         LD      C,H             
4C07: 26 4D      LD      H,$4D           
4C09: FA 44 DB   LD      A,($DB44)       
4C0C: A7         AND     A               
4C0D: 28 06      JR      Z,$4C15         
4C0F: CD 8D 3B   CALL    $3B8D           
4C12: 36 03      LD      (HL),$03        
4C14: C9         RET                     
4C15: F0 99      LD      A,($99)         
4C17: FE 7B      CP      $7B             
4C19: 38 09      JR      C,$4C24         
4C1B: D6 02      SUB     $02             
4C1D: E0 99      LDFF00  ($99),A         
4C1F: 3E 00      LD      A,$00           
4C21: C3 97 21   JP      $2197           
4C24: CD 4C 54   CALL    $544C           
4C27: 30 08      JR      NC,$4C31        
4C29: 3E 54      LD      A,$54           
4C2B: CD 97 21   CALL    $2197           
4C2E: CD 8D 3B   CALL    $3B8D           
4C31: C9         RET                     
4C32: FA 9F C1   LD      A,($C19F)       
4C35: A7         AND     A               
4C36: 20 0D      JR      NZ,$4C45        
4C38: CD 91 08   CALL    $0891           
4C3B: 36 80      LD      (HL),$80        
4C3D: 3E 10      LD      A,$10           
4C3F: EA 68 D3   LD      ($D368),A       
4C42: CD 8D 3B   CALL    $3B8D           
4C45: C9         RET                     
4C46: 86         ADD     A,(HL)          
4C47: 10 CD      STOP    $CD             
4C49: 91         SUB     C               
4C4A: 08 20 19   LD      ($1920),SP      
4C4D: EA 67 C1   LD      ($C167),A       
4C50: 16 04      LD      D,$04           
4C52: CD 61 52   CALL    $5261           
4C55: 3E 01      LD      A,$01           
4C57: EA 44 DB   LD      ($DB44),A       
4C5A: 3E 22      LD      A,$22           
4C5C: E0 9D      LDFF00  ($9D),A         
4C5E: 3E 91      LD      A,$91           
4C60: CD 97 21   CALL    $2197           
4C63: C3 8D 3B   JP      $3B8D           
4C66: F0 98      LD      A,($98)         
4C68: E0 EE      LDFF00  ($EE),A         
4C6A: F0 99      LD      A,($99)         
4C6C: D6 0C      SUB     $0C             
4C6E: E0 EC      LDFF00  ($EC),A         
4C70: AF         XOR     A               
4C71: E0 F1      LDFF00  ($F1),A         
4C73: 11 46 4C   LD      DE,$4C46        
4C76: CD D0 3C   CALL    $3CD0           
4C79: CD BA 3D   CALL    $3DBA           
4C7C: 3E 6C      LD      A,$6C           
4C7E: E0 9D      LDFF00  ($9D),A         
4C80: 3E 02      LD      A,$02           
4C82: E0 A1      LDFF00  ($A1),A         
4C84: 3E 03      LD      A,$03           
4C86: E0 9E      LDFF00  ($9E),A         
4C88: C9         RET                     
4C89: FA 48 DB   LD      A,($DB48)       
4C8C: A7         AND     A               
4C8D: 28 3F      JR      Z,$4CCE         
4C8F: FE 01      CP      $01             
4C91: 28 26      JR      Z,$4CB9         
4C93: CD 4C 54   CALL    $544C           
4C96: 30 14      JR      NC,$4CAC        
4C98: FA 73 DB   LD      A,($DB73)       
4C9B: A7         AND     A               
4C9C: 3E DD      LD      A,$DD           
4C9E: 20 15      JR      NZ,$4CB5        
4CA0: FA 0E DB   LD      A,($DB0E)       
4CA3: FE 03      CP      $03             
4CA5: 20 0C      JR      NZ,$4CB3        
4CA7: 3E C5      LD      A,$C5           
4CA9: CD 85 21   CALL    $2185           
4CAC: FA 73 DB   LD      A,($DB73)       
4CAF: A7         AND     A               
4CB0: 20 2E      JR      NZ,$4CE0        
4CB2: C9         RET                     
4CB3: 3E C5      LD      A,$C5           
4CB5: CD 85 21   CALL    $2185           
4CB8: C9         RET                     
4CB9: CD 4C 54   CALL    $544C           
4CBC: 30 0E      JR      NC,$4CCC        
4CBE: FA 65 DB   LD      A,($DB65)       
4CC1: CB 4F      SET     1,E             
4CC3: 3E 11      LD      A,$11           
4CC5: 28 02      JR      Z,$4CC9         
4CC7: 3E 10      LD      A,$10           
4CC9: CD 97 21   CALL    $2197           
4CCC: 18 0B      JR      $4CD9           
4CCE: CD 4C 54   CALL    $544C           
4CD1: 30 05      JR      NC,$4CD8        
4CD3: 3E 55      LD      A,$55           
4CD5: CD 97 21   CALL    $2197           
4CD8: C9         RET                     
4CD9: FA 48 DB   LD      A,($DB48)       
4CDC: FE 01      CP      $01             
4CDE: 20 45      JR      NZ,$4D25        
4CE0: 21 D0 C3   LD      HL,$C3D0        
4CE3: 09         ADD     HL,BC           
4CE4: 7E         LD      A,(HL)          
4CE5: C6 07      ADD     $07             
4CE7: 77         LD      (HL),A          
4CE8: 30 3B      JR      NC,$4D25        
4CEA: 3E 3F      LD      A,$3F           
4CEC: CD 01 3C   CALL    $3C01           
4CEF: F0 D7      LD      A,($D7)         
4CF1: C6 06      ADD     $06             
4CF3: 21 00 C2   LD      HL,$C200        
4CF6: 19         ADD     HL,DE           
4CF7: 77         LD      (HL),A          
4CF8: F0 D8      LD      A,($D8)         
4CFA: D6 03      SUB     $03             
4CFC: 21 10 C2   LD      HL,$C210        
4CFF: 19         ADD     HL,DE           
4D00: 77         LD      (HL),A          
4D01: 21 C0 C2   LD      HL,$C2C0        
4D04: 19         ADD     HL,DE           
4D05: 36 01      LD      (HL),$01        
4D07: 21 40 C2   LD      HL,$C240        
4D0A: 19         ADD     HL,DE           
4D0B: 36 FF      LD      (HL),$FF        
4D0D: 21 50 C2   LD      HL,$C250        
4D10: 19         ADD     HL,DE           
4D11: 36 FD      LD      (HL),$FD        
4D13: 21 E0 C2   LD      HL,$C2E0        
4D16: 19         ADD     HL,DE           
4D17: 36 30      LD      (HL),$30        
4D19: 21 40 C3   LD      HL,$C340        
4D1C: 19         ADD     HL,DE           
4D1D: 36 C1      LD      (HL),$C1        
4D1F: 21 50 C3   LD      HL,$C350        
4D22: 19         ADD     HL,DE           
4D23: 36 00      LD      (HL),$00        
4D25: C9         RET                     
4D26: FA 9F C1   LD      A,($C19F)       
4D29: A7         AND     A               
4D2A: 20 1D      JR      NZ,$4D49        
4D2C: FA 77 C1   LD      A,($C177)       
4D2F: A7         AND     A               
4D30: 20 0E      JR      NZ,$4D40        
4D32: 3E 04      LD      A,$04           
4D34: EA 0E DB   LD      ($DB0E),A       
4D37: 3E 0D      LD      A,$0D           
4D39: E0 A5      LDFF00  ($A5),A         
4D3B: CD 98 08   CALL    $0898           
4D3E: 18 05      JR      $4D45           
4D40: 3E C9      LD      A,$C9           
4D42: CD 85 21   CALL    $2185           
4D45: CD 8D 3B   CALL    $3B8D           
4D48: 70         LD      (HL),B          
4D49: C9         RET                     
4D4A: 74         LD      (HL),H          
4D4B: 00         NOP                     
4D4C: 76         HALT                    
4D4D: 00         NOP                     
4D4E: 70         LD      (HL),B          
4D4F: 00         NOP                     
4D50: 72         LD      (HL),D          
4D51: 00         NOP                     
4D52: FA 48 DB   LD      A,($DB48)       
4D55: FE 02      CP      $02             
4D57: C0         RET     NZ              
4D58: FA 0E DB   LD      A,($DB0E)       
4D5B: FE 04      CP      $04             
4D5D: 30 07      JR      NC,$4D66        
4D5F: 3E 78      LD      A,$78           
4D61: 11 4A 4D   LD      DE,$4D4A        
4D64: 18 10      JR      $4D76           
4D66: F0 F8      LD      A,($F8)         
4D68: E6 20      AND     $20             
4D6A: C8         RET     Z               
4D6B: 21 10 C2   LD      HL,$C210        
4D6E: 09         ADD     HL,BC           
4D6F: 36 4B      LD      (HL),$4B        
4D71: 11 4E 4D   LD      DE,$4D4E        
4D74: 3E 7C      LD      A,$7C           
4D76: E0 EE      LDFF00  ($EE),A         
4D78: 3E 5C      LD      A,$5C           
4D7A: E0 EC      LDFF00  ($EC),A         
4D7C: AF         XOR     A               
4D7D: E0 F1      LDFF00  ($F1),A         
4D7F: CD 3B 3C   CALL    $3C3B           
4D82: CD BA 3D   CALL    $3DBA           
4D85: 21 B0 C3   LD      HL,$C3B0        
4D88: 09         ADD     HL,BC           
4D89: 7E         LD      A,(HL)          
4D8A: E0 F1      LDFF00  ($F1),A         
4D8C: C9         RET                     
4D8D: 60         LD      H,B             
4D8E: 00         NOP                     
4D8F: 62         LD      H,D             
4D90: 00         NOP                     
4D91: 62         LD      H,D             
4D92: 20 60      JR      NZ,$4DF4        
4D94: 20 64      JR      NZ,$4DFA        
4D96: 00         NOP                     
4D97: 66         LD      H,(HL)          
4D98: 00         NOP                     
4D99: 66         LD      H,(HL)          
4D9A: 20 64      JR      NZ,$4E00        
4D9C: 20 68      JR      NZ,$4E06        
4D9E: 00         NOP                     
4D9F: 6A         LD      L,D             
4DA0: 00         NOP                     
4DA1: 6C         LD      L,H             
4DA2: 00         NOP                     
4DA3: 6E         LD      L,(HL)          
4DA4: 00         NOP                     
4DA5: 6A         LD      L,D             
4DA6: 20 68      JR      NZ,$4E10        
4DA8: 20 6E      JR      NZ,$4E18        
4DAA: 20 6C      JR      NZ,$4E18        
4DAC: 20 68      JR      NZ,$4E16        
4DAE: 00         NOP                     
4DAF: 6A         LD      L,D             
4DB0: 00         NOP                     
4DB1: 6A         LD      L,D             
4DB2: 20 68      JR      NZ,$4E1C        
4DB4: 20 66      JR      NZ,$4E1C        
4DB6: 00         NOP                     
4DB7: 66         LD      H,(HL)          
4DB8: 20 66      JR      NZ,$4E20        
4DBA: 00         NOP                     
4DBB: 66         LD      H,(HL)          
4DBC: 20 6C      JR      NZ,$4E2A        
4DBE: 00         NOP                     
4DBF: 6E         LD      L,(HL)          
4DC0: 00         NOP                     
4DC1: 6C         LD      L,H             
4DC2: 00         NOP                     
4DC3: 6E         LD      L,(HL)          
4DC4: 00         NOP                     
4DC5: 6E         LD      L,(HL)          
4DC6: 20 6C      JR      NZ,$4E34        
4DC8: 20 6E      JR      NZ,$4E38        
4DCA: 20 6C      JR      NZ,$4E38        
4DCC: 20 60      JR      NZ,$4E2E        
4DCE: 00         NOP                     
4DCF: 62         LD      H,D             
4DD0: 00         NOP                     
4DD1: 64         LD      H,H             
4DD2: 00         NOP                     
4DD3: 64         LD      H,H             
4DD4: 20 62      JR      NZ,$4E38        
4DD6: 20 60      JR      NZ,$4E38        
4DD8: 20 08      JR      NZ,$4DE2        
4DDA: 08 08 09   LD      ($0908),SP      
4DDD: 0A         LD      A,(BC)          
4DDE: 0A         LD      A,(BC)          
4DDF: 0A         LD      A,(BC)          
4DE0: 09         ADD     HL,BC           
4DE1: 08 F8 06   LD      ($06F8),SP      
4DE4: 01 FA 95   LD      BC,$95FA        
4DE7: DB         ???                     
4DE8: FE 01      CP      $01             
4DEA: CA 4E 4E   JP      Z,$4E4E         
4DED: FA 73 DB   LD      A,($DB73)       
4DF0: A7         AND     A               
4DF1: C2 6B 7A   JP      NZ,$7A6B        
4DF4: FA A5 DB   LD      A,($DBA5)       
4DF7: A7         AND     A               
4DF8: C2 1D 51   JP      NZ,$511D        
4DFB: FA 4E DB   LD      A,($DB4E)       
4DFE: A7         AND     A               
4DFF: CA 6B 7A   JP      Z,$7A6B         
4E02: F0 F6      LD      A,($F6)         
4E04: FE C0      CP      $C0             
4E06: 38 02      JR      C,$4E0A         
4E08: 18 0F      JR      $4E19           
4E0A: FA 08 D8   LD      A,($D808)       
4E0D: E6 10      AND     $10             
4E0F: 20 08      JR      NZ,$4E19        
4E11: FA 0E DB   LD      A,($DB0E)       
4E14: FE 07      CP      $07             
4E16: D2 6B 7A   JP      NC,$7A6B        
4E19: F0 E7      LD      A,($E7)         
4E1B: E6 1F      AND     $1F             
4E1D: 20 20      JR      NZ,$4E3F        
4E1F: 21 80 C3   LD      HL,$C380        
4E22: 09         ADD     HL,BC           
4E23: 36 03      LD      (HL),$03        
4E25: CD 24 7A   CALL    $7A24           
4E28: C6 14      ADD     $14             
4E2A: FE 28      CP      $28             
4E2C: 30 11      JR      NC,$4E3F        
4E2E: CD 34 7A   CALL    $7A34           
4E31: C6 14      ADD     $14             
4E33: FE 28      CP      $28             
4E35: 30 08      JR      NC,$4E3F        
4E37: CD 44 7A   CALL    $7A44           
4E3A: 21 80 C3   LD      HL,$C380        
4E3D: 09         ADD     HL,BC           
4E3E: 73         LD      (HL),E          
4E3F: CD 30 54   CALL    $5430           
4E42: FA C8 C3   LD      A,($C3C8)       
4E45: FE 01      CP      $01             
4E47: 20 5E      JR      NZ,$4EA7        
4E49: CD 8C 08   CALL    $088C           
4E4C: 20 59      JR      NZ,$4EA7        
4E4E: F0 E7      LD      A,($E7)         
4E50: 1F         RRA                     
4E51: 1F         RRA                     
4E52: 1F         RRA                     
4E53: 1F         RRA                     
4E54: E6 07      AND     $07             
4E56: 5F         LD      E,A             
4E57: 50         LD      D,B             
4E58: 21 D9 4D   LD      HL,$4DD9        
4E5B: 19         ADD     HL,DE           
4E5C: 7E         LD      A,(HL)          
4E5D: E0 F1      LDFF00  ($F1),A         
4E5F: F0 E7      LD      A,($E7)         
4E61: C6 10      ADD     $10             
4E63: E6 1F      AND     $1F             
4E65: 20 40      JR      NZ,$4EA7        
4E67: 3E C9      LD      A,$C9           
4E69: CD 01 3C   CALL    $3C01           
4E6C: 38 39      JR      C,$4EA7         
4E6E: F0 D8      LD      A,($D8)         
4E70: 21 10 C2   LD      HL,$C210        
4E73: 19         ADD     HL,DE           
4E74: D6 08      SUB     $08             
4E76: 77         LD      (HL),A          
4E77: C5         PUSH    BC              
4E78: F0 E7      LD      A,($E7)         
4E7A: C6 10      ADD     $10             
4E7C: 1F         RRA                     
4E7D: 1F         RRA                     
4E7E: 1F         RRA                     
4E7F: 1F         RRA                     
4E80: 1F         RRA                     
4E81: E6 01      AND     $01             
4E83: 4F         LD      C,A             
4E84: 21 E1 4D   LD      HL,$4DE1        
4E87: 09         ADD     HL,BC           
4E88: F0 D7      LD      A,($D7)         
4E8A: 86         ADD     A,(HL)          
4E8B: 21 00 C2   LD      HL,$C200        
4E8E: 19         ADD     HL,DE           
4E8F: 77         LD      (HL),A          
4E90: 21 E3 4D   LD      HL,$4DE3        
4E93: 09         ADD     HL,BC           
4E94: 7E         LD      A,(HL)          
4E95: 21 40 C2   LD      HL,$C240        
4E98: 19         ADD     HL,DE           
4E99: 77         LD      (HL),A          
4E9A: 21 50 C2   LD      HL,$C250        
4E9D: 19         ADD     HL,DE           
4E9E: 36 FC      LD      (HL),$FC        
4EA0: 21 D0 C3   LD      HL,$C3D0        
4EA3: 19         ADD     HL,DE           
4EA4: 36 40      LD      (HL),$40        
4EA6: C1         POP     BC              
4EA7: 79         LD      A,C             
4EA8: EA 0F C5   LD      ($C50F),A       
4EAB: 11 AD 4D   LD      DE,$4DAD        
4EAE: CD 3B 3C   CALL    $3C3B           
4EB1: CD 09 54   CALL    $5409           
4EB4: F0 F0      LD      A,($F0)         
4EB6: C7         RST     0X00            
4EB7: C3 4E 84   JP      $844E           
4EBA: 4F         LD      C,A             
4EBB: BD         CP      L               
4EBC: 4F         LD      C,A             
4EBD: 8C         ADC     A,H             
4EBE: 50         LD      D,B             
4EBF: B8         CP      B               
4EC0: 50         LD      D,B             
4EC1: 0B         DEC     BC              
4EC2: 51         LD      D,C             
4EC3: F0 F6      LD      A,($F6)         
4EC5: FE C0      CP      $C0             
4EC7: 30 07      JR      NC,$4ED0        
4EC9: FA C8 C3   LD      A,($C3C8)       
4ECC: A7         AND     A               
4ECD: C2 83 4F   JP      NZ,$4F83        
4ED0: CD 4C 54   CALL    $544C           
4ED3: D2 83 4F   JP      NC,$4F83        
4ED6: FA 08 D8   LD      A,($D808)       
4ED9: E6 10      AND     $10             
4EDB: 28 2D      JR      Z,$4F0A         
4EDD: 21 92 D8   LD      HL,$D892        
4EE0: 7E         LD      A,(HL)          
4EE1: E6 40      AND     $40             
4EE3: 20 07      JR      NZ,$4EEC        
4EE5: CB F6      SET     1,E             
4EE7: 3E 94      LD      A,$94           
4EE9: C3 85 21   JP      $2185           
4EEC: FA 49 DB   LD      A,($DB49)       
4EEF: E6 04      AND     $04             
4EF1: 28 05      JR      Z,$4EF8         
4EF3: 3E 95      LD      A,$95           
4EF5: C3 85 21   JP      $2185           
4EF8: 1E 0B      LD      E,$0B           
4EFA: 21 00 DB   LD      HL,$DB00        
4EFD: 2A         LD      A,(HLI)         
4EFE: FE 09      CP      $09             
4F00: 28 08      JR      Z,$4F0A         
4F02: 1D         DEC     E               
4F03: 7B         LD      A,E             
4F04: FE FF      CP      $FF             
4F06: 20 F5      JR      NZ,$4EFD        
4F08: 18 E9      JR      $4EF3           
4F0A: CD 8C 08   CALL    $088C           
4F0D: 36 10      LD      (HL),$10        
4F0F: 16 2F      LD      D,$2F           
4F11: 1E 03      LD      E,$03           
4F13: FA 48 DB   LD      A,($DB48)       
4F16: A7         AND     A               
4F17: 28 45      JR      Z,$4F5E         
4F19: 1E 06      LD      E,$06           
4F1B: FE 02      CP      $02             
4F1D: 20 14      JR      NZ,$4F33        
4F1F: 1E 05      LD      E,$05           
4F21: F0 F6      LD      A,($F6)         
4F23: FE C0      CP      $C0             
4F25: 38 0C      JR      C,$4F33         
4F27: D5         PUSH    DE              
4F28: CD BD 27   CALL    $27BD           
4F2B: D1         POP     DE              
4F2C: 21 D0 C2   LD      HL,$C2D0        
4F2F: 09         ADD     HL,BC           
4F30: 70         LD      (HL),B          
4F31: 1E 92      LD      E,$92           
4F33: C5         PUSH    BC              
4F34: 0E 0B      LD      C,$0B           
4F36: 21 00 DB   LD      HL,$DB00        
4F39: 2A         LD      A,(HLI)         
4F3A: FE 09      CP      $09             
4F3C: 20 19      JR      NZ,$4F57        
4F3E: 1E 04      LD      E,$04           
4F40: 16 4A      LD      D,$4A           
4F42: FA 49 DB   LD      A,($DB49)       
4F45: E6 04      AND     $04             
4F47: 28 14      JR      Z,$4F5D         
4F49: 1E 05      LD      E,$05           
4F4B: 16 2F      LD      D,$2F           
4F4D: F0 F6      LD      A,($F6)         
4F4F: FE C0      CP      $C0             
4F51: 38 0A      JR      C,$4F5D         
4F53: 1E 92      LD      E,$92           
4F55: 18 06      JR      $4F5D           
4F57: 0D         DEC     C               
4F58: 79         LD      A,C             
4F59: FE FF      CP      $FF             
4F5B: 20 DC      JR      NZ,$4F39        
4F5D: C1         POP     BC              
4F5E: 7B         LD      A,E             
4F5F: FE 80      CP      $80             
4F61: 38 05      JR      C,$4F68         
4F63: CD 85 21   CALL    $2185           
4F66: 18 03      JR      $4F6B           
4F68: CD 97 21   CALL    $2197           
4F6B: F0 F6      LD      A,($F6)         
4F6D: FE C0      CP      $C0             
4F6F: 38 0A      JR      C,$4F7B         
4F71: 21 D0 C2   LD      HL,$C2D0        
4F74: 09         ADD     HL,BC           
4F75: 70         LD      (HL),B          
4F76: D5         PUSH    DE              
4F77: CD BD 27   CALL    $27BD           
4F7A: D1         POP     DE              
4F7B: 21 40 C4   LD      HL,$C440        
4F7E: 09         ADD     HL,BC           
4F7F: 72         LD      (HL),D          
4F80: CD 8D 3B   CALL    $3B8D           
4F83: C9         RET                     
4F84: CD 65 79   CALL    $7965           
4F87: 21 40 C4   LD      HL,$C440        
4F8A: 09         ADD     HL,BC           
4F8B: 56         LD      D,(HL)          
4F8C: 21 D0 C2   LD      HL,$C2D0        
4F8F: 09         ADD     HL,BC           
4F90: 7E         LD      A,(HL)          
4F91: A7         AND     A               
4F92: 7A         LD      A,D             
4F93: 20 0D      JR      NZ,$4FA2        
4F95: 34         INC     (HL)            
4F96: EA 68 D3   LD      ($D368),A       
4F99: E0 B0      LDFF00  ($B0),A         
4F9B: E0 BD      LDFF00  ($BD),A         
4F9D: 21 C8 C3   LD      HL,$C3C8        
4FA0: 36 01      LD      (HL),$01        
4FA2: FE 4A      CP      $4A             
4FA4: 20 12      JR      NZ,$4FB8        
4FA6: FA 49 DB   LD      A,($DB49)       
4FA9: E6 04      AND     $04             
4FAB: 20 0B      JR      NZ,$4FB8        
4FAD: CD 8D 3B   CALL    $3B8D           
4FB0: AF         XOR     A               
4FB1: EA 10 D2   LD      ($D210),A       
4FB4: EA 11 D2   LD      ($D211),A       
4FB7: C9         RET                     
4FB8: CD 8D 3B   CALL    $3B8D           
4FBB: 70         LD      (HL),B          
4FBC: C9         RET                     
4FBD: 3E 02      LD      A,$02           
4FBF: E0 A1      LDFF00  ($A1),A         
4FC1: C5         PUSH    BC              
4FC2: CD 7C 08   CALL    $087C           
4FC5: C1         POP     BC              
4FC6: FA 11 D2   LD      A,($D211)       
4FC9: FE 07      CP      $07             
4FCB: 20 1E      JR      NZ,$4FEB        
4FCD: FA 10 D2   LD      A,($D210)       
4FD0: FE E8      CP      $E8             
4FD2: 20 17      JR      NZ,$4FEB        
4FD4: 3E 16      LD      A,$16           
4FD6: CD 97 21   CALL    $2197           
4FD9: C5         PUSH    BC              
4FDA: CD 7C 08   CALL    $087C           
4FDD: C1         POP     BC              
4FDE: AF         XOR     A               
4FDF: EA 10 D2   LD      ($D210),A       
4FE2: EA 11 D2   LD      ($D211),A       
4FE5: CD D2 27   CALL    $27D2           
4FE8: C3 8D 3B   JP      $3B8D           
4FEB: CD 44 7A   CALL    $7A44           
4FEE: 7B         LD      A,E             
4FEF: EE 01      XOR     $01             
4FF1: E0 9E      LDFF00  ($9E),A         
4FF3: FA 10 D2   LD      A,($D210)       
4FF6: C6 01      ADD     $01             
4FF8: EA 10 D2   LD      ($D210),A       
4FFB: 5F         LD      E,A             
4FFC: FA 11 D2   LD      A,($D211)       
4FFF: CE 00      ADC     $00             
5001: EA 11 D2   LD      ($D211),A       
5004: 57         LD      D,A             
5005: FA 11 D2   LD      A,($D211)       
5008: FE 07      CP      $07             
500A: 20 0C      JR      NZ,$5018        
500C: FA 10 D2   LD      A,($D210)       
500F: FE E0      CP      $E0             
5011: 38 05      JR      C,$5018         
5013: AF         XOR     A               
5014: EA C8 C3   LD      ($C3C8),A       
5017: C9         RET                     
5018: 21 C8 C3   LD      HL,$C3C8        
501B: 36 01      LD      (HL),$01        
501D: 7B         LD      A,E             
501E: CB 3A      SET     1,E             
5020: 1F         RRA                     
5021: CB 3A      SET     1,E             
5023: 1F         RRA                     
5024: CB 3A      SET     1,E             
5026: 1F         RRA                     
5027: CB 3A      SET     1,E             
5029: 1F         RRA                     
502A: FE 1D      CP      $1D             
502C: 38 05      JR      C,$5033         
502E: FE 3B      CP      $3B             
5030: 30 01      JR      NC,$5033        
5032: 34         INC     (HL)            
5033: FE 1D      CP      $1D             
5035: D8         RET     C               
5036: 3E 00      LD      A,$00           
5038: E0 9D      LDFF00  ($9D),A         
503A: F0 E7      LD      A,($E7)         
503C: 1E 75      LD      E,$75           
503E: E6 40      AND     $40             
5040: 28 01      JR      Z,$5043         
5042: 1C         INC     E               
5043: 7B         LD      A,E             
5044: E0 9D      LDFF00  ($9D),A         
5046: F0 E7      LD      A,($E7)         
5048: E6 1F      AND     $1F             
504A: 20 3F      JR      NZ,$508B        
504C: 3E C9      LD      A,$C9           
504E: CD 01 3C   CALL    $3C01           
5051: 38 38      JR      C,$508B         
5053: F0 99      LD      A,($99)         
5055: 21 10 C2   LD      HL,$C210        
5058: 19         ADD     HL,DE           
5059: D6 08      SUB     $08             
505B: 77         LD      (HL),A          
505C: C5         PUSH    BC              
505D: F0 E7      LD      A,($E7)         
505F: 1F         RRA                     
5060: 1F         RRA                     
5061: 1F         RRA                     
5062: 1F         RRA                     
5063: 1F         RRA                     
5064: E6 01      AND     $01             
5066: 4F         LD      C,A             
5067: 42         LD      B,D             
5068: 21 E1 4D   LD      HL,$4DE1        
506B: 09         ADD     HL,BC           
506C: F0 98      LD      A,($98)         
506E: 86         ADD     A,(HL)          
506F: 21 00 C2   LD      HL,$C200        
5072: 19         ADD     HL,DE           
5073: 77         LD      (HL),A          
5074: 21 E3 4D   LD      HL,$4DE3        
5077: 09         ADD     HL,BC           
5078: 7E         LD      A,(HL)          
5079: 21 40 C2   LD      HL,$C240        
507C: 19         ADD     HL,DE           
507D: 77         LD      (HL),A          
507E: C1         POP     BC              
507F: 21 50 C2   LD      HL,$C250        
5082: 19         ADD     HL,DE           
5083: 36 FC      LD      (HL),$FC        
5085: 21 D0 C3   LD      HL,$C3D0        
5088: 19         ADD     HL,DE           
5089: 36 40      LD      (HL),$40        
508B: C9         RET                     
508C: FA 9F C1   LD      A,($C19F)       
508F: A7         AND     A               
5090: 20 23      JR      NZ,$50B5        
5092: CD 8D 3B   CALL    $3B8D           
5095: FA 77 C1   LD      A,($C177)       
5098: A7         AND     A               
5099: 20 0B      JR      NZ,$50A6        
509B: 3E 10      LD      A,$10           
509D: EA 68 D3   LD      ($D368),A       
50A0: CD 91 08   CALL    $0891           
50A3: 36 80      LD      (HL),$80        
50A5: C9         RET                     
50A6: 3E 15      LD      A,$15           
50A8: CD 97 21   CALL    $2197           
50AB: CD 8D 3B   CALL    $3B8D           
50AE: 36 01      LD      (HL),$01        
50B0: 21 D0 C2   LD      HL,$C2D0        
50B3: 09         ADD     HL,BC           
50B4: 70         LD      (HL),B          
50B5: C9         RET                     
50B6: 90         SUB     B               
50B7: 10 CD      STOP    $CD             
50B9: 91         SUB     C               
50BA: 08 20 28   LD      ($2820),SP      
50BD: FA 9F C1   LD      A,($C19F)       
50C0: A7         AND     A               
50C1: C0         RET     NZ              
50C2: 21 49 DB   LD      HL,$DB49        
50C5: CB D6      SET     1,E             
50C7: AF         XOR     A               
50C8: EA 4A DB   LD      ($DB4A),A       
50CB: CD 8D 3B   CALL    $3B8D           
50CE: F0 F6      LD      A,($F6)         
50D0: FE C0      CP      $C0             
50D2: 38 01      JR      C,$50D5         
50D4: 70         LD      (HL),B          
50D5: F0 F6      LD      A,($F6)         
50D7: FE C0      CP      $C0             
50D9: 30 05      JR      NC,$50E0        
50DB: 3E 14      LD      A,$14           
50DD: C3 97 21   JP      $2197           
50E0: 3E 93      LD      A,$93           
50E2: C3 85 21   JP      $2185           
50E5: FE 08      CP      $08             
50E7: 20 06      JR      NZ,$50EF        
50E9: 35         DEC     (HL)            
50EA: 3E 13      LD      A,$13           
50EC: CD 97 21   CALL    $2197           
50EF: 3E 6C      LD      A,$6C           
50F1: E0 9D      LDFF00  ($9D),A         
50F3: 3E 02      LD      A,$02           
50F5: E0 A1      LDFF00  ($A1),A         
50F7: F0 98      LD      A,($98)         
50F9: E0 EE      LDFF00  ($EE),A         
50FB: F0 99      LD      A,($99)         
50FD: D6 0C      SUB     $0C             
50FF: E0 EC      LDFF00  ($EC),A         
5101: 11 B6 50   LD      DE,$50B6        
5104: AF         XOR     A               
5105: E0 F1      LDFF00  ($F1),A         
5107: CD D0 3C   CALL    $3CD0           
510A: C9         RET                     
510B: FA 9F C1   LD      A,($C19F)       
510E: A7         AND     A               
510F: C0         RET     NZ              
5110: CD 4C 54   CALL    $544C           
5113: D0         RET     NC              
5114: 3E 97      LD      A,$97           
5116: C3 85 21   JP      $2185           
5119: 5C         LD      E,H             
511A: 00         NOP                     
511B: 5C         LD      E,H             
511C: 20 FA      JR      NZ,$5118        
511E: 0E DB      LD      C,$DB           
5120: FE 07      CP      $07             
5122: 38 28      JR      C,$514C         
5124: FA FD D8   LD      A,($D8FD)       
5127: E6 30      AND     $30             
5129: C2 6B 7A   JP      NZ,$7A6B        
512C: 21 10 C2   LD      HL,$C210        
512F: 09         ADD     HL,BC           
5130: 36 60      LD      (HL),$60        
5132: 21 00 C2   LD      HL,$C200        
5135: 09         ADD     HL,BC           
5136: 36 7A      LD      (HL),$7A        
5138: 11 19 51   LD      DE,$5119        
513B: CD 3B 3C   CALL    $3C3B           
513E: CD 65 79   CALL    $7965           
5141: CD 4C 54   CALL    $544C           
5144: 30 05      JR      NC,$514B        
5146: 3E D7      LD      A,$D7           
5148: CD 85 21   CALL    $2185           
514B: C9         RET                     
514C: FA 4E DB   LD      A,($DB4E)       
514F: A7         AND     A               
5150: C2 6B 7A   JP      NZ,$7A6B        
5153: FA 44 DB   LD      A,($DB44)       
5156: A7         AND     A               
5157: 28 09      JR      Z,$5162         
5159: 21 90 C2   LD      HL,$C290        
515C: 09         ADD     HL,BC           
515D: 3E 03      LD      A,$03           
515F: 77         LD      (HL),A          
5160: E0 F0      LDFF00  ($F0),A         
5162: F0 F0      LD      A,($F0)         
5164: A7         AND     A               
5165: 20 22      JR      NZ,$5189        
5167: CD 87 08   CALL    $0887           
516A: 36 7F      LD      (HL),$7F        
516C: 21 80 C3   LD      HL,$C380        
516F: 09         ADD     HL,BC           
5170: 36 01      LD      (HL),$01        
5172: 21 00 C2   LD      HL,$C200        
5175: 09         ADD     HL,BC           
5176: 7E         LD      A,(HL)          
5177: D6 08      SUB     $08             
5179: 77         LD      (HL),A          
517A: 21 10 C2   LD      HL,$C210        
517D: 09         ADD     HL,BC           
517E: 7E         LD      A,(HL)          
517F: D6 08      SUB     $08             
5181: 77         LD      (HL),A          
5182: EA 67 C1   LD      ($C167),A       
5185: CD 8D 3B   CALL    $3B8D           
5188: C9         RET                     
5189: F0 E7      LD      A,($E7)         
518B: E6 1F      AND     $1F             
518D: 20 08      JR      NZ,$5197        
518F: CD 44 7A   CALL    $7A44           
5192: 21 80 C3   LD      HL,$C380        
5195: 09         ADD     HL,BC           
5196: 73         LD      (HL),E          
5197: CD 30 54   CALL    $5430           
519A: 11 8D 4D   LD      DE,$4D8D        
519D: CD 3B 3C   CALL    $3C3B           
51A0: F0 F0      LD      A,($F0)         
51A2: 3D         DEC     A               
51A3: C7         RST     0X00            
51A4: DE 51      SBC     $51             
51A6: 19         ADD     HL,DE           
51A7: 52         LD      D,D             
51A8: 50         LD      D,B             
51A9: 52         LD      D,D             
51AA: 40         LD      B,B             
51AB: 00         NOP                     
51AC: 42         LD      B,D             
51AD: 00         NOP                     
51AE: 42         LD      B,D             
51AF: 20 40      JR      NZ,$51F1        
51B1: 20 44      JR      NZ,$51F7        
51B3: 00         NOP                     
51B4: 46         LD      B,(HL)          
51B5: 00         NOP                     
51B6: 48         LD      C,B             
51B7: 00         NOP                     
51B8: 4A         LD      C,D             
51B9: 00         NOP                     
51BA: 48         LD      C,B             
51BB: 00         NOP                     
51BC: 4C         LD      C,H             
51BD: 00         NOP                     
51BE: 03         INC     BC              
51BF: 03         INC     BC              
51C0: 03         INC     BC              
51C1: 03         INC     BC              
51C2: 03         INC     BC              
51C3: 04         INC     B               
51C4: 03         INC     BC              
51C5: 04         INC     B               
51C6: 03         INC     BC              
51C7: 03         INC     BC              
51C8: 03         INC     BC              
51C9: 02         LD      (BC),A          
51CA: 02         LD      (BC),A          
51CB: 02         LD      (BC),A          
51CC: 02         LD      (BC),A          
51CD: 02         LD      (BC),A          
51CE: 00         NOP                     
51CF: 00         NOP                     
51D0: 01 01 00   LD      BC,$0001        
51D3: 00         NOP                     
51D4: 01 01 00   LD      BC,$0001        
51D7: 00         NOP                     
51D8: 01 01 00   LD      BC,$0001        
51DB: 00         NOP                     
51DC: 01 01 CD   LD      BC,$CD01        
51DF: 87         ADD     A,A             
51E0: 08 20 0B   LD      ($0B20),SP      
51E3: 3E 01      LD      A,$01           
51E5: CD 97 21   CALL    $2197           
51E8: 36 40      LD      (HL),$40        
51EA: CD 8D 3B   CALL    $3B8D           
51ED: AF         XOR     A               
51EE: 1F         RRA                     
51EF: 1F         RRA                     
51F0: E6 1F      AND     $1F             
51F2: 5F         LD      E,A             
51F3: 50         LD      D,B             
51F4: 21 BE 51   LD      HL,$51BE        
51F7: 19         ADD     HL,DE           
51F8: 7E         LD      A,(HL)          
51F9: E0 F1      LDFF00  ($F1),A         
51FB: 3E 38      LD      A,$38           
51FD: E0 EE      LDFF00  ($EE),A         
51FF: E0 98      LDFF00  ($98),A         
5201: 3E 34      LD      A,$34           
5203: E0 EC      LDFF00  ($EC),A         
5205: E0 99      LDFF00  ($99),A         
5207: 3E 02      LD      A,$02           
5209: E0 A1      LDFF00  ($A1),A         
520B: 3E FF      LD      A,$FF           
520D: E0 9D      LDFF00  ($9D),A         
520F: 11 AA 51   LD      DE,$51AA        
5212: CD 3B 3C   CALL    $3C3B           
5215: CD BA 3D   CALL    $3DBA           
5218: C9         RET                     
5219: 3E 03      LD      A,$03           
521B: CD F9 51   CALL    $51F9           
521E: CD 91 08   CALL    $0891           
5221: 21 9F C1   LD      HL,$C19F        
5224: B6         OR      (HL)            
5225: 20 28      JR      NZ,$524F        
5227: F0 CB      LD      A,($CB)         
5229: E6 0F      AND     $0F             
522B: 28 22      JR      Z,$524F         
522D: CD 8D 3B   CALL    $3B8D           
5230: 3E 01      LD      A,$01           
5232: E0 A2      LDFF00  ($A2),A         
5234: 3E 02      LD      A,$02           
5236: EA 46 C1   LD      ($C146),A       
5239: 3E 12      LD      A,$12           
523B: E0 A3      LDFF00  ($A3),A         
523D: 3E 0C      LD      A,$0C           
523F: E0 9A      LDFF00  ($9A),A         
5241: AF         XOR     A               
5242: E0 9B      LDFF00  ($9B),A         
5244: 3E 00      LD      A,$00           
5246: E0 9E      LDFF00  ($9E),A         
5248: E0 A1      LDFF00  ($A1),A         
524A: 3E 01      LD      A,$01           
524C: EA 0A C1   LD      ($C10A),A       
524F: C9         RET                     
5250: CD 65 79   CALL    $7965           
5253: CD 09 54   CALL    $5409           
5256: CD 4C 54   CALL    $544C           
5259: 30 05      JR      NC,$5260        
525B: 3E 02      LD      A,$02           
525D: CD 97 21   CALL    $2197           
5260: C9         RET                     
5261: 21 00 DB   LD      HL,$DB00        
5264: 1E 0C      LD      E,$0C           
5266: 2A         LD      A,(HLI)         
5267: BA         CP      D               
5268: 28 13      JR      Z,$527D         
526A: 1D         DEC     E               
526B: 20 F9      JR      NZ,$5266        
526D: 21 00 DB   LD      HL,$DB00        
5270: 7E         LD      A,(HL)          
5271: A7         AND     A               
5272: 20 02      JR      NZ,$5276        
5274: 72         LD      (HL),D          
5275: C9         RET                     
5276: 23         INC     HL              
5277: 1C         INC     E               
5278: 7B         LD      A,E             
5279: FE 0C      CP      $0C             
527B: 20 F3      JR      NZ,$5270        
527D: C9         RET                     
527E: 60         LD      H,B             
527F: 00         NOP                     
5280: 62         LD      H,D             
5281: 00         NOP                     
5282: 62         LD      H,D             
5283: 20 60      JR      NZ,$52E5        
5285: 20 64      JR      NZ,$52EB        
5287: 00         NOP                     
5288: 66         LD      H,(HL)          
5289: 00         NOP                     
528A: 66         LD      H,(HL)          
528B: 20 64      JR      NZ,$52F1        
528D: 20 68      JR      NZ,$52F7        
528F: 00         NOP                     
5290: 6A         LD      L,D             
5291: 00         NOP                     
5292: 6C         LD      L,H             
5293: 00         NOP                     
5294: 6E         LD      L,(HL)          
5295: 00         NOP                     
5296: 6A         LD      L,D             
5297: 20 68      JR      NZ,$5301        
5299: 20 6E      JR      NZ,$5309        
529B: 20 6C      JR      NZ,$5309        
529D: 20 FA      JR      NZ,$5299        
529F: A5         AND     L               
52A0: DB         ???                     
52A1: A7         AND     A               
52A2: 28 7E      JR      Z,$5322         
52A4: F0 E7      LD      A,($E7)         
52A6: E6 1F      AND     $1F             
52A8: 20 08      JR      NZ,$52B2        
52AA: CD 44 7A   CALL    $7A44           
52AD: 21 80 C3   LD      HL,$C380        
52B0: 09         ADD     HL,BC           
52B1: 73         LD      (HL),E          
52B2: CD 30 54   CALL    $5430           
52B5: 11 7E 52   LD      DE,$527E        
52B8: CD 3B 3C   CALL    $3C3B           
52BB: CD 65 79   CALL    $7965           
52BE: CD 09 54   CALL    $5409           
52C1: F0 F0      LD      A,($F0)         
52C3: C7         RST     0X00            
52C4: CA 52 DE   JP      Z,$DE52         
52C7: 52         LD      D,D             
52C8: 0F         RRCA                    
52C9: 53         LD      D,E             
52CA: FA 77 D4   LD      A,($D477)       
52CD: A7         AND     A               
52CE: 20 3F      JR      NZ,$530F        
52D0: CD 4C 54   CALL    $544C           
52D3: 30 08      JR      NC,$52DD        
52D5: 3E F0      LD      A,$F0           
52D7: CD 97 21   CALL    $2197           
52DA: CD 8D 3B   CALL    $3B8D           
52DD: C9         RET                     
52DE: FA 9F C1   LD      A,($C19F)       
52E1: A7         AND     A               
52E2: 20 24      JR      NZ,$5308        
52E4: CD 8D 3B   CALL    $3B8D           
52E7: FA 77 C1   LD      A,($C177)       
52EA: A7         AND     A               
52EB: 28 02      JR      Z,$52EF         
52ED: 70         LD      (HL),B          
52EE: C9         RET                     
52EF: FA 5E DB   LD      A,($DB5E)       
52F2: D6 00      SUB     $00             
52F4: FA 5D DB   LD      A,($DB5D)       
52F7: DE 01      SBC     $01             
52F9: 38 0E      JR      C,$5309         
52FB: 3E 64      LD      A,$64           
52FD: EA 92 DB   LD      ($DB92),A       
5300: 3E F1      LD      A,$F1           
5302: EA 77 D4   LD      ($D477),A       
5305: CD 97 21   CALL    $2197           
5308: C9         RET                     
5309: 70         LD      (HL),B          
530A: 3E 4E      LD      A,$4E           
530C: C3 97 21   JP      $2197           
530F: CD 4C 54   CALL    $544C           
5312: 30 05      JR      NC,$5319        
5314: 3E F1      LD      A,$F1           
5316: CD 97 21   CALL    $2197           
5319: C9         RET                     
531A: 5C         LD      E,H             
531B: 00         NOP                     
531C: 5C         LD      E,H             
531D: 20 5E      JR      NZ,$537D        
531F: 00         NOP                     
5320: 5E         LD      E,(HL)          
5321: 20 21      JR      NZ,$5344        
5323: 40         LD      B,B             
5324: C4 09 FA   CALL    NZ,$FA09        
5327: 77         LD      (HL),A          
5328: D4 B6 20   CALL    NC,$20B6        
532B: 2B         DEC     HL              
532C: 1E 0F      LD      E,$0F           
532E: 50         LD      D,B             
532F: 7B         LD      A,E             
5330: B9         CP      C               
5331: 28 12      JR      Z,$5345         
5333: 21 80 C2   LD      HL,$C280        
5336: 19         ADD     HL,DE           
5337: 7E         LD      A,(HL)          
5338: A7         AND     A               
5339: 28 0A      JR      Z,$5345         
533B: 21 A0 C3   LD      HL,$C3A0        
533E: 19         ADD     HL,DE           
533F: 7E         LD      A,(HL)          
5340: FE 6A      CP      $6A             
5342: CA 6B 7A   JP      Z,$7A6B         
5345: 1D         DEC     E               
5346: 7B         LD      A,E             
5347: FE FF      CP      $FF             
5349: 20 E4      JR      NZ,$532F        
534B: 11 1A 53   LD      DE,$531A        
534E: CD 3B 3C   CALL    $3C3B           
5351: CD 65 79   CALL    $7965           
5354: C3 09 54   JP      $5409           
5357: F0 E7      LD      A,($E7)         
5359: 1F         RRA                     
535A: 1F         RRA                     
535B: 1F         RRA                     
535C: 1F         RRA                     
535D: E6 01      AND     $01             
535F: CD 87 3B   CALL    $3B87           
5362: F0 98      LD      A,($98)         
5364: 21 EE FF   LD      HL,$FFEE        
5367: 96         SUB     (HL)            
5368: C6 10      ADD     $10             
536A: FE 20      CP      $20             
536C: 30 18      JR      NC,$5386        
536E: F0 99      LD      A,($99)         
5370: 21 EF FF   LD      HL,$FFEF        
5373: 96         SUB     (HL)            
5374: C6 14      ADD     $14             
5376: FE 1C      CP      $1C             
5378: 30 0C      JR      NC,$5386        
537A: 3E 80      LD      A,$80           
537C: EA AD C1   LD      ($C1AD),A       
537F: F0 98      LD      A,($98)         
5381: 21 00 C2   LD      HL,$C200        
5384: 09         ADD     HL,BC           
5385: 77         LD      (HL),A          
5386: FA 1F C1   LD      A,($C11F)       
5389: A7         AND     A               
538A: 28 06      JR      Z,$5392         
538C: CD 8D 3B   CALL    $3B8D           
538F: 70         LD      (HL),B          
5390: 18 3B      JR      $53CD           
5392: F0 F0      LD      A,($F0)         
5394: C7         RST     0X00            
5395: 9B         SBC     E               
5396: 53         LD      D,E             
5397: B2         OR      D               
5398: 53         LD      D,E             
5399: D6 53      SUB     $53             
539B: CD 24 7A   CALL    $7A24           
539E: C6 08      ADD     $08             
53A0: FE 10      CP      $10             
53A2: 30 0C      JR      NC,$53B0        
53A4: CD 34 7A   CALL    $7A34           
53A7: C6 09      ADD     $09             
53A9: FE 12      CP      $12             
53AB: 30 03      JR      NC,$53B0        
53AD: CD 8D 3B   CALL    $3B8D           
53B0: 18 1B      JR      $53CD           
53B2: F0 EE      LD      A,($EE)         
53B4: E0 98      LDFF00  ($98),A         
53B6: F0 EC      LD      A,($EC)         
53B8: D6 05      SUB     $05             
53BA: E0 99      LDFF00  ($99),A         
53BC: CD 8D 3B   CALL    $3B8D           
53BF: 21 40 C4   LD      HL,$C440        
53C2: 09         ADD     HL,BC           
53C3: 36 01      LD      (HL),$01        
53C5: AF         XOR     A               
53C6: EA 77 D4   LD      ($D477),A       
53C9: 3E 01      LD      A,$01           
53CB: E0 B2      LDFF00  ($B2),A         
53CD: CD BA 3D   CALL    $3DBA           
53D0: 11 1A 53   LD      DE,$531A        
53D3: C3 3B 3C   JP      $3C3B           
53D6: F0 E7      LD      A,($E7)         
53D8: 1F         RRA                     
53D9: 1F         RRA                     
53DA: 1F         RRA                     
53DB: 1F         RRA                     
53DC: E6 01      AND     $01             
53DE: EA 3B C1   LD      ($C13B),A       
53E1: F0 F6      LD      A,($F6)         
53E3: 21 E0 C3   LD      HL,$C3E0        
53E6: 09         ADD     HL,BC           
53E7: 77         LD      (HL),A          
53E8: F0 98      LD      A,($98)         
53EA: 21 00 C2   LD      HL,$C200        
53ED: 09         ADD     HL,BC           
53EE: 77         LD      (HL),A          
53EF: F0 99      LD      A,($99)         
53F1: 21 10 C2   LD      HL,$C210        
53F4: 09         ADD     HL,BC           
53F5: C6 05      ADD     $05             
53F7: 77         LD      (HL),A          
53F8: 21 10 C3   LD      HL,$C310        
53FB: 09         ADD     HL,BC           
53FC: 70         LD      (HL),B          
53FD: FA 1C C1   LD      A,($C11C)       
5400: FE 02      CP      $02             
5402: 20 03      JR      NZ,$5407        
5404: F0 A2      LD      A,($A2)         
5406: 77         LD      (HL),A          
5407: 18 C0      JR      $53C9           
5409: CD D5 3B   CALL    $3BD5           
540C: 30 1D      JR      NC,$542B        
540E: CD 4A 09   CALL    $094A           
5411: CD 42 09   CALL    $0942           
5414: FA A6 C1   LD      A,($C1A6)       
5417: A7         AND     A               
5418: 28 11      JR      Z,$542B         
541A: 5F         LD      E,A             
541B: 50         LD      D,B             
541C: 21 9F C3   LD      HL,$C39F        
541F: 19         ADD     HL,DE           
5420: 7E         LD      A,(HL)          
5421: FE 03      CP      $03             
5423: 20 06      JR      NZ,$542B        
5425: 21 8F C2   LD      HL,$C28F        
5428: 19         ADD     HL,DE           
5429: 36 00      LD      (HL),$00        
542B: C9         RET                     
542C: 06 04      LD      B,$04           
542E: 02         LD      (BC),A          
542F: 00         NOP                     
5430: 21 80 C3   LD      HL,$C380        
5433: 09         ADD     HL,BC           
5434: 5E         LD      E,(HL)          
5435: 50         LD      D,B             
5436: 21 2C 54   LD      HL,$542C        
5439: 19         ADD     HL,DE           
543A: E5         PUSH    HL              
543B: 21 D0 C3   LD      HL,$C3D0        
543E: 09         ADD     HL,BC           
543F: 34         INC     (HL)            
5440: 7E         LD      A,(HL)          
5441: 1F         RRA                     
5442: 1F         RRA                     
5443: 1F         RRA                     
5444: 1F         RRA                     
5445: E1         POP     HL              
5446: E6 01      AND     $01             
5448: B6         OR      (HL)            
5449: C3 87 3B   JP      $3B87           
544C: 58         LD      E,B             
544D: F0 99      LD      A,($99)         
544F: 21 EF FF   LD      HL,$FFEF        
5452: 96         SUB     (HL)            
5453: C6 14      ADD     $14             
5455: FE 28      CP      $28             
5457: 30 44      JR      NC,$549D        
5459: F0 98      LD      A,($98)         
545B: 21 EE FF   LD      HL,$FFEE        
545E: 96         SUB     (HL)            
545F: C6 10      ADD     $10             
5461: FE 20      CP      $20             
5463: 30 38      JR      NC,$549D        
5465: 1C         INC     E               
5466: F0 EB      LD      A,($EB)         
5468: FE 6D      CP      $6D             
546A: 28 0C      JR      Z,$5478         
546C: D5         PUSH    DE              
546D: CD 44 7A   CALL    $7A44           
5470: F0 9E      LD      A,($9E)         
5472: EE 01      XOR     $01             
5474: BB         CP      E               
5475: D1         POP     DE              
5476: 20 25      JR      NZ,$549D        
5478: 21 AD C1   LD      HL,$C1AD        
547B: 36 01      LD      (HL),$01        
547D: FA 9F C1   LD      A,($C19F)       
5480: 21 4F C1   LD      HL,$C14F        
5483: B6         OR      (HL)            
5484: 21 46 C1   LD      HL,$C146        
5487: B6         OR      (HL)            
5488: 21 34 C1   LD      HL,$C134        
548B: B6         OR      (HL)            
548C: 20 0F      JR      NZ,$549D        
548E: FA 9A DB   LD      A,($DB9A)       
5491: FE 80      CP      $80             
5493: 20 08      JR      NZ,$549D        
5495: F0 CC      LD      A,($CC)         
5497: E6 10      AND     $10             
5499: 28 02      JR      Z,$549D         
549B: 37         SCF                     
549C: C9         RET                     
549D: A7         AND     A               
549E: C9         RET                     
549F: CD 87 08   CALL    $0887           
54A2: 36 C0      LD      (HL),$C0        
54A4: 3E 18      LD      A,$18           
54A6: EA 02 D2   LD      ($D202),A       
54A9: C9         RET                     
54AA: 21 D0 C2   LD      HL,$C2D0        
54AD: 09         ADD     HL,BC           
54AE: 7E         LD      A,(HL)          
54AF: C7         RST     0X00            
54B0: B8         CP      B               
54B1: 54         LD      D,H             
54B2: 75         LD      (HL),L          
54B3: 58         LD      E,B             
54B4: 3C         INC     A               
54B5: 58         LD      E,B             
54B6: BF         CP      A               
54B7: 58         LD      E,B             
54B8: CD 12 3F   CALL    $3F12           
54BB: CD 0E 58   CALL    $580E           
54BE: F0 EA      LD      A,($EA)         
54C0: FE 05      CP      $05             
54C2: 28 3C      JR      Z,$5500         
54C4: EA C6 C1   LD      ($C1C6),A       
54C7: 21 C0 C2   LD      HL,$C2C0        
54CA: 09         ADD     HL,BC           
54CB: 7E         LD      A,(HL)          
54CC: C7         RST     0X00            
54CD: D1         POP     DE              
54CE: 54         LD      D,H             
54CF: DF         RST     0X18            
54D0: 54         LD      D,H             
54D1: CD 91 08   CALL    $0891           
54D4: 36 FF      LD      (HL),$FF        
54D6: 21 20 C4   LD      HL,$C420        
54D9: 09         ADD     HL,BC           
54DA: 36 FF      LD      (HL),$FF        
54DC: C3 94 62   JP      $6294           
54DF: CD 91 08   CALL    $0891           
54E2: CA F2 54   JP      Z,$54F2         
54E5: 21 20 C4   LD      HL,$C420        
54E8: 09         ADD     HL,BC           
54E9: 77         LD      (HL),A          
54EA: FE 80      CP      $80             
54EC: 30 03      JR      NC,$54F1        
54EE: CD 76 74   CALL    $7476           
54F1: C9         RET                     
54F2: CD AD 74   CALL    $74AD           
54F5: 21 80 C4   LD      HL,$C480        
54F8: 19         ADD     HL,DE           
54F9: 36 08      LD      (HL),$08        
54FB: C9         RET                     
54FC: F8 A8      LDHL    SP,$A8          
54FE: 08 F8 CD   LD      ($CDF8),SP      
5501: 65         LD      H,L             
5502: 79         LD      A,C             
5503: 21 00 C3   LD      HL,$C300        
5506: 09         ADD     HL,BC           
5507: 7E         LD      A,(HL)          
5508: A7         AND     A               
5509: 28 49      JR      Z,$5554         
550B: E6 3F      AND     $3F             
550D: 20 45      JR      NZ,$5554        
550F: 3E 65      LD      A,$65           
5511: 1E 04      LD      E,$04           
5513: CD 13 3C   CALL    $3C13           
5516: 38 6E      JR      C,$5586         
5518: 21 40 C3   LD      HL,$C340        
551B: 19         ADD     HL,DE           
551C: 36 02      LD      (HL),$02        
551E: 21 50 C3   LD      HL,$C350        
5521: 19         ADD     HL,DE           
5522: 36 80      LD      (HL),$80        
5524: 21 30 C4   LD      HL,$C430        
5527: 19         ADD     HL,DE           
5528: 36 40      LD      (HL),$40        
552A: 21 D0 C2   LD      HL,$C2D0        
552D: 19         ADD     HL,DE           
552E: 36 01      LD      (HL),$01        
5530: 21 00 C2   LD      HL,$C200        
5533: 19         ADD     HL,DE           
5534: FA 02 D2   LD      A,($D202)       
5537: 77         LD      (HL),A          
5538: C6 20      ADD     $20             
553A: EA 02 D2   LD      ($D202),A       
553D: FE A8      CP      $A8             
553F: 38 05      JR      C,$5546         
5541: 3E 08      LD      A,$08           
5543: EA 02 D2   LD      ($D202),A       
5546: CD ED 27   CALL    $27ED           
5549: 21 D0 C3   LD      HL,$C3D0        
554C: 19         ADD     HL,DE           
554D: 77         LD      (HL),A          
554E: 21 10 C2   LD      HL,$C210        
5551: 19         ADD     HL,DE           
5552: 36 00      LD      (HL),$00        
5554: FA 01 D2   LD      A,($D201)       
5557: 3C         INC     A               
5558: EA 01 D2   LD      ($D201),A       
555B: E6 7F      AND     $7F             
555D: 20 27      JR      NZ,$5586        
555F: 3E 65      LD      A,$65           
5561: 1E 04      LD      E,$04           
5563: CD 13 3C   CALL    $3C13           
5566: 38 1E      JR      C,$5586         
5568: 21 40 C3   LD      HL,$C340        
556B: 19         ADD     HL,DE           
556C: 36 41      LD      (HL),$41        
556E: 21 D0 C2   LD      HL,$C2D0        
5571: 19         ADD     HL,DE           
5572: 36 02      LD      (HL),$02        
5574: F0 D7      LD      A,($D7)         
5576: D6 14      SUB     $14             
5578: 21 00 C2   LD      HL,$C200        
557B: 19         ADD     HL,DE           
557C: 77         LD      (HL),A          
557D: F0 D8      LD      A,($D8)         
557F: D6 04      SUB     $04             
5581: 21 10 C2   LD      HL,$C210        
5584: 19         ADD     HL,DE           
5585: 77         LD      (HL),A          
5586: 21 60 C3   LD      HL,$C360        
5589: 09         ADD     HL,BC           
558A: 7E         LD      A,(HL)          
558B: FE 0A      CP      $0A             
558D: 30 58      JR      NC,$55E7        
558F: FA 01 D2   LD      A,($D201)       
5592: C6 40      ADD     $40             
5594: E6 FF      AND     $FF             
5596: 20 4F      JR      NZ,$55E7        
5598: 3E 65      LD      A,$65           
559A: 1E 04      LD      E,$04           
559C: CD 13 3C   CALL    $3C13           
559F: 38 46      JR      C,$55E7         
55A1: 21 D0 C4   LD      HL,$C4D0        
55A4: 19         ADD     HL,DE           
55A5: 72         LD      (HL),D          
55A6: 21 40 C3   LD      HL,$C340        
55A9: 19         ADD     HL,DE           
55AA: 36 02      LD      (HL),$02        
55AC: 21 30 C4   LD      HL,$C430        
55AF: 19         ADD     HL,DE           
55B0: 72         LD      (HL),D          
55B1: 21 60 C3   LD      HL,$C360        
55B4: 19         ADD     HL,DE           
55B5: 72         LD      (HL),D          
55B6: 21 D0 C2   LD      HL,$C2D0        
55B9: 19         ADD     HL,DE           
55BA: 36 03      LD      (HL),$03        
55BC: CD ED 27   CALL    $27ED           
55BF: E6 3F      AND     $3F             
55C1: C6 20      ADD     $20             
55C3: 21 10 C2   LD      HL,$C210        
55C6: 19         ADD     HL,DE           
55C7: 77         LD      (HL),A          
55C8: C5         PUSH    BC              
55C9: E6 01      AND     $01             
55CB: 4F         LD      C,A             
55CC: 21 FC 54   LD      HL,$54FC        
55CF: 09         ADD     HL,BC           
55D0: 7E         LD      A,(HL)          
55D1: 21 00 C2   LD      HL,$C200        
55D4: 19         ADD     HL,DE           
55D5: 77         LD      (HL),A          
55D6: 21 FE 54   LD      HL,$54FE        
55D9: 09         ADD     HL,BC           
55DA: 7E         LD      A,(HL)          
55DB: 21 40 C2   LD      HL,$C240        
55DE: 19         ADD     HL,DE           
55DF: 77         LD      (HL),A          
55E0: 21 E0 C2   LD      HL,$C2E0        
55E3: 19         ADD     HL,DE           
55E4: 36 40      LD      (HL),$40        
55E6: C1         POP     BC              
55E7: CD E2 08   CALL    $08E2           
55EA: 21 D0 C3   LD      HL,$C3D0        
55ED: 09         ADD     HL,BC           
55EE: 7E         LD      A,(HL)          
55EF: 34         INC     (HL)            
55F0: 1F         RRA                     
55F1: 1F         RRA                     
55F2: 1F         RRA                     
55F3: 1F         RRA                     
55F4: E6 01      AND     $01             
55F6: 21 B0 C3   LD      HL,$C3B0        
55F9: 09         ADD     HL,BC           
55FA: 77         LD      (HL),A          
55FB: F0 EE      LD      A,($EE)         
55FD: D6 10      SUB     $10             
55FF: E0 EE      LDFF00  ($EE),A         
5601: F0 EC      LD      A,($EC)         
5603: D6 10      SUB     $10             
5605: E0 EC      LDFF00  ($EC),A         
5607: 21 50 C3   LD      HL,$C350        
560A: 09         ADD     HL,BC           
560B: 36 00      LD      (HL),$00        
560D: CD 65 3B   CALL    $3B65           
5610: CD EB 3B   CALL    $3BEB           
5613: CD BA 3D   CALL    $3DBA           
5616: 21 50 C3   LD      HL,$C350        
5619: 09         ADD     HL,BC           
561A: 36 14      LD      (HL),$14        
561C: CD 65 3B   CALL    $3B65           
561F: CD BF 3B   CALL    $3BBF           
5622: F0 F0      LD      A,($F0)         
5624: C7         RST     0X00            
5625: 2F         CPL                     
5626: 56         LD      D,(HL)          
5627: 6E         LD      L,(HL)          
5628: 56         LD      D,(HL)          
5629: A8         XOR     B               
562A: 56         LD      D,(HL)          
562B: 08 F8 60   LD      ($60F8),SP      
562E: 18 CD      JR      $55FD           
5630: 87         ADD     A,A             
5631: 08 20 15   LD      ($1520),SP      
5634: CD 91 08   CALL    $0891           
5637: 36 80      LD      (HL),$80        
5639: CD 8D 3B   CALL    $3B8D           
563C: CD ED 27   CALL    $27ED           
563F: E6 1F      AND     $1F             
5641: C6 60      ADD     $60             
5643: 21 B0 C2   LD      HL,$C2B0        
5646: 09         ADD     HL,BC           
5647: 77         LD      (HL),A          
5648: C9         RET                     
5649: 21 80 C3   LD      HL,$C380        
564C: 09         ADD     HL,BC           
564D: 5E         LD      E,(HL)          
564E: 50         LD      D,B             
564F: 21 2D 56   LD      HL,$562D        
5652: 19         ADD     HL,DE           
5653: F0 EC      LD      A,($EC)         
5655: BE         CP      (HL)            
5656: 20 08      JR      NZ,$5660        
5658: 7B         LD      A,E             
5659: EE 01      XOR     $01             
565B: 21 80 C3   LD      HL,$C380        
565E: 09         ADD     HL,BC           
565F: 77         LD      (HL),A          
5660: 21 2B 56   LD      HL,$562B        
5663: 19         ADD     HL,DE           
5664: 7E         LD      A,(HL)          
5665: 21 50 C2   LD      HL,$C250        
5668: 09         ADD     HL,BC           
5669: 77         LD      (HL),A          
566A: CD D4 79   CALL    $79D4           
566D: C9         RET                     
566E: 21 D0 C3   LD      HL,$C3D0        
5671: 09         ADD     HL,BC           
5672: 7E         LD      A,(HL)          
5673: 34         INC     (HL)            
5674: 34         INC     (HL)            
5675: CD 91 08   CALL    $0891           
5678: FE 60      CP      $60             
567A: 20 05      JR      NZ,$5681        
567C: 21 F3 FF   LD      HL,$FFF3        
567F: 36 0D      LD      (HL),$0D        
5681: 30 24      JR      NC,$56A7        
5683: 21 40 C2   LD      HL,$C240        
5686: 09         ADD     HL,BC           
5687: 36 D0      LD      (HL),$D0        
5689: CD DE 79   CALL    $79DE           
568C: F0 EE      LD      A,($EE)         
568E: FE 18      CP      $18             
5690: 30 15      JR      NC,$56A7        
5692: 3E 30      LD      A,$30           
5694: EA 57 C1   LD      ($C157),A       
5697: AF         XOR     A               
5698: EA 58 C1   LD      ($C158),A       
569B: CD D7 08   CALL    $08D7           
569E: 21 00 C3   LD      HL,$C300        
56A1: 09         ADD     HL,BC           
56A2: 36 FF      LD      (HL),$FF        
56A4: CD 8D 3B   CALL    $3B8D           
56A7: C9         RET                     
56A8: 21 D0 C3   LD      HL,$C3D0        
56AB: 09         ADD     HL,BC           
56AC: 7E         LD      A,(HL)          
56AD: 34         INC     (HL)            
56AE: FA 57 C1   LD      A,($C157)       
56B1: A7         AND     A               
56B2: 20 21      JR      NZ,$56D5        
56B4: 21 40 C2   LD      HL,$C240        
56B7: 09         ADD     HL,BC           
56B8: 36 20      LD      (HL),$20        
56BA: CD DE 79   CALL    $79DE           
56BD: 21 B0 C2   LD      HL,$C2B0        
56C0: 09         ADD     HL,BC           
56C1: F0 EE      LD      A,($EE)         
56C3: BE         CP      (HL)            
56C4: 38 0F      JR      C,$56D5         
56C6: CD 87 08   CALL    $0887           
56C9: CD ED 27   CALL    $27ED           
56CC: E6 1F      AND     $1F             
56CE: C6 40      ADD     $40             
56D0: 77         LD      (HL),A          
56D1: CD 8D 3B   CALL    $3B8D           
56D4: 70         LD      (HL),B          
56D5: C9         RET                     
56D6: F0 F0      LD      A,($F0)         
56D8: 40         LD      B,B             
56D9: 00         NOP                     
56DA: F0 F8      LD      A,($F8)         
56DC: 42         LD      B,D             
56DD: 00         NOP                     
56DE: F0 00      LD      A,($00)         
56E0: 44         LD      B,H             
56E1: 00         NOP                     
56E2: F0 08      LD      A,($08)         
56E4: 46         LD      B,(HL)          
56E5: 10 F0      STOP    $F0             
56E7: 10 48      STOP    $48             
56E9: 10 F0      STOP    $F0             
56EB: 18 4A      JR      $5737           
56ED: 10 00      STOP    $00             
56EF: F0 4C      LD      A,($4C)         
56F1: 00         NOP                     
56F2: 00         NOP                     
56F3: F8 4E      LDHL    SP,$4E          
56F5: 00         NOP                     
56F6: 00         NOP                     
56F7: 00         NOP                     
56F8: 50         LD      D,B             
56F9: 10 00      STOP    $00             
56FB: 08 52 10   LD      ($1052),SP      
56FE: 00         NOP                     
56FF: 10 54      STOP    $54             
5701: 10 00      STOP    $00             
5703: 18 56      JR      $575B           
5705: 10 00      STOP    $00             
5707: 20 58      JR      NZ,$5761        
5709: 10 10      STOP    $10             
570B: F8 5A      LDHL    SP,$5A          
570D: 10 10      STOP    $10             
570F: 00         NOP                     
5710: 5C         LD      E,H             
5711: 10 10      STOP    $10             
5713: 08 5E 10   LD      ($105E),SP      
5716: 10 10      STOP    $10             
5718: 60         LD      H,B             
5719: 10 10      STOP    $10             
571B: 18 62      JR      $577F           
571D: 10 10      STOP    $10             
571F: 20 64      JR      NZ,$5785        
5721: 10 00      STOP    $00             
5723: 00         NOP                     
5724: FF         RST     0X38            
5725: 00         NOP                     
5726: F0 F0      LD      A,($F0)         
5728: 66         LD      H,(HL)          
5729: 00         NOP                     
572A: F0 F8      LD      A,($F8)         
572C: 42         LD      B,D             
572D: 00         NOP                     
572E: F0 00      LD      A,($00)         
5730: 44         LD      B,H             
5731: 00         NOP                     
5732: F0 08      LD      A,($08)         
5734: 46         LD      B,(HL)          
5735: 10 F0      STOP    $F0             
5737: 10 48      STOP    $48             
5739: 10 F0      STOP    $F0             
573B: 18 4A      JR      $5787           
573D: 10 00      STOP    $00             
573F: F0 68      LD      A,($68)         
5741: 00         NOP                     
5742: 00         NOP                     
5743: F8 4E      LDHL    SP,$4E          
5745: 00         NOP                     
5746: 00         NOP                     
5747: 00         NOP                     
5748: 50         LD      D,B             
5749: 10 00      STOP    $00             
574B: 08 52 10   LD      ($1052),SP      
574E: 00         NOP                     
574F: 10 54      STOP    $54             
5751: 10 00      STOP    $00             
5753: 18 56      JR      $57AB           
5755: 10 00      STOP    $00             
5757: 20 6A      JR      NZ,$57C3        
5759: 10 10      STOP    $10             
575B: F8 5A      LDHL    SP,$5A          
575D: 10 10      STOP    $10             
575F: 00         NOP                     
5760: 5C         LD      E,H             
5761: 10 10      STOP    $10             
5763: 08 5E 10   LD      ($105E),SP      
5766: 10 10      STOP    $10             
5768: 60         LD      H,B             
5769: 10 10      STOP    $10             
576B: 18 62      JR      $57CF           
576D: 10 10      STOP    $10             
576F: 20 6C      JR      NZ,$57DD        
5771: 10 F0      STOP    $F0             
5773: 18 4A      JR      $57BF           
5775: 10 F0      STOP    $F0             
5777: 08 46 10   LD      ($1046),SP      
577A: F0 10      LD      A,($10)         
577C: 48         LD      C,B             
577D: 10 F0      STOP    $F0             
577F: F8 42      LDHL    SP,$42          
5781: 00         NOP                     
5782: F0 00      LD      A,($00)         
5784: 44         LD      B,H             
5785: 00         NOP                     
5786: F0 F0      LD      A,($F0)         
5788: 40         LD      B,B             
5789: 00         NOP                     
578A: 00         NOP                     
578B: 20 58      JR      NZ,$57E5        
578D: 10 00      STOP    $00             
578F: 08 52 10   LD      ($1052),SP      
5792: 00         NOP                     
5793: 10 54      STOP    $54             
5795: 10 00      STOP    $00             
5797: 18 56      JR      $57EF           
5799: 10 00      STOP    $00             
579B: F8 4E      LDHL    SP,$4E          
579D: 00         NOP                     
579E: 00         NOP                     
579F: 00         NOP                     
57A0: 50         LD      D,B             
57A1: 10 00      STOP    $00             
57A3: F0 4C      LD      A,($4C)         
57A5: 00         NOP                     
57A6: 10 20      STOP    $20             
57A8: 64         LD      H,H             
57A9: 10 10      STOP    $10             
57AB: 10 60      STOP    $60             
57AD: 10 10      STOP    $10             
57AF: 18 62      JR      $5813           
57B1: 10 10      STOP    $10             
57B3: 00         NOP                     
57B4: 5C         LD      E,H             
57B5: 10 10      STOP    $10             
57B7: 08 5E 10   LD      ($105E),SP      
57BA: 10 F8      STOP    $F8             
57BC: 5A         LD      E,D             
57BD: 10 00      STOP    $00             
57BF: 00         NOP                     
57C0: FF         RST     0X38            
57C1: 00         NOP                     
57C2: F0 18      LD      A,($18)         
57C4: 4A         LD      C,D             
57C5: 10 F0      STOP    $F0             
57C7: 08 46 10   LD      ($1046),SP      
57CA: F0 10      LD      A,($10)         
57CC: 48         LD      C,B             
57CD: 10 F0      STOP    $F0             
57CF: F8 42      LDHL    SP,$42          
57D1: 00         NOP                     
57D2: F0 00      LD      A,($00)         
57D4: 44         LD      B,H             
57D5: 00         NOP                     
57D6: F0 F0      LD      A,($F0)         
57D8: 66         LD      H,(HL)          
57D9: 00         NOP                     
57DA: 00         NOP                     
57DB: 20 6A      JR      NZ,$5847        
57DD: 10 00      STOP    $00             
57DF: 08 52 10   LD      ($1052),SP      
57E2: 00         NOP                     
57E3: 10 54      STOP    $54             
57E5: 10 00      STOP    $00             
57E7: 18 56      JR      $583F           
57E9: 10 00      STOP    $00             
57EB: F8 4E      LDHL    SP,$4E          
57ED: 00         NOP                     
57EE: 00         NOP                     
57EF: 00         NOP                     
57F0: 50         LD      D,B             
57F1: 10 00      STOP    $00             
57F3: F0 68      LD      A,($68)         
57F5: 00         NOP                     
57F6: 10 20      STOP    $20             
57F8: 6C         LD      L,H             
57F9: 10 10      STOP    $10             
57FB: 10 60      STOP    $60             
57FD: 10 10      STOP    $10             
57FF: 18 62      JR      $5863           
5801: 10 10      STOP    $10             
5803: 00         NOP                     
5804: 5C         LD      E,H             
5805: 10 10      STOP    $10             
5807: 08 5E 10   LD      ($105E),SP      
580A: 10 F8      STOP    $F8             
580C: 5A         LD      E,D             
580D: 10 F0      STOP    $F0             
580F: F1         POP     AF              
5810: CB 27      SET     1,E             
5812: CB 27      SET     1,E             
5814: CB 27      SET     1,E             
5816: CB 27      SET     1,E             
5818: 5F         LD      E,A             
5819: CB 27      SET     1,E             
581B: CB 27      SET     1,E             
581D: 83         ADD     A,E             
581E: 5F         LD      E,A             
581F: 50         LD      D,B             
5820: 21 D6 56   LD      HL,$56D6        
5823: F0 E7      LD      A,($E7)         
5825: E6 01      AND     $01             
5827: 28 03      JR      Z,$582C         
5829: 21 72 57   LD      HL,$5772        
582C: 19         ADD     HL,DE           
582D: 0E 13      LD      C,$13           
582F: CD 26 3D   CALL    $3D26           
5832: 3E 13      LD      A,$13           
5834: CD D0 3D   CALL    $3DD0           
5837: C9         RET                     
5838: 72         LD      (HL),D          
5839: 00         NOP                     
583A: 72         LD      (HL),D          
583B: 20 11      JR      NZ,$584E        
583D: 38 58      JR      C,$5897         
583F: CD D0 3C   CALL    $3CD0           
5842: CD 65 79   CALL    $7965           
5845: 21 D0 C3   LD      HL,$C3D0        
5848: 09         ADD     HL,BC           
5849: 34         INC     (HL)            
584A: 7E         LD      A,(HL)          
584B: 1F         RRA                     
584C: 1F         RRA                     
584D: 1F         RRA                     
584E: E6 01      AND     $01             
5850: CD 87 3B   CALL    $3B87           
5853: 21 D0 C3   LD      HL,$C3D0        
5856: 09         ADD     HL,BC           
5857: 7E         LD      A,(HL)          
5858: E6 30      AND     $30             
585A: 28 09      JR      Z,$5865         
585C: 21 50 C2   LD      HL,$C250        
585F: 09         ADD     HL,BC           
5860: 36 F8      LD      (HL),$F8        
5862: CD D4 79   CALL    $79D4           
5865: F0 EC      LD      A,($EC)         
5867: FE 10      CP      $10             
5869: DA 6B 7A   JP      C,$7A6B         
586C: C9         RET                     
586D: 74         LD      (HL),H          
586E: 00         NOP                     
586F: 76         HALT                    
5870: 00         NOP                     
5871: 76         HALT                    
5872: 20 74      JR      NZ,$58E8        
5874: 20 11      JR      NZ,$5887        
5876: 6D         LD      L,L             
5877: 58         LD      E,B             
5878: CD 3B 3C   CALL    $3C3B           
587B: CD 65 79   CALL    $7965           
587E: CD E2 08   CALL    $08E2           
5881: 21 D0 C3   LD      HL,$C3D0        
5884: 09         ADD     HL,BC           
5885: 34         INC     (HL)            
5886: 7E         LD      A,(HL)          
5887: F5         PUSH    AF              
5888: 1F         RRA                     
5889: 1F         RRA                     
588A: 1F         RRA                     
588B: 1F         RRA                     
588C: E6 01      AND     $01             
588E: CD 87 3B   CALL    $3B87           
5891: CD B4 3B   CALL    $3BB4           
5894: F1         POP     AF              
5895: 1E FC      LD      E,$FC           
5897: E6 10      AND     $10             
5899: 28 02      JR      Z,$589D         
589B: 1E 04      LD      E,$04           
589D: 21 40 C2   LD      HL,$C240        
58A0: 09         ADD     HL,BC           
58A1: 73         LD      (HL),E          
58A2: 21 50 C2   LD      HL,$C250        
58A5: 09         ADD     HL,BC           
58A6: 36 0C      LD      (HL),$0C        
58A8: CD D1 79   CALL    $79D1           
58AB: F0 EC      LD      A,($EC)         
58AD: FE 8B      CP      $8B             
58AF: D2 6B 7A   JP      NC,$7A6B        
58B2: C9         RET                     
58B3: 78         LD      A,B             
58B4: 00         NOP                     
58B5: 7A         LD      A,D             
58B6: 00         NOP                     
58B7: 7C         LD      A,H             
58B8: 00         NOP                     
58B9: 7E         LD      A,(HL)          
58BA: 00         NOP                     
58BB: 01 FF 08   LD      BC,$08FF        
58BE: F8 21      LDHL    SP,$21          
58C0: 40         LD      B,B             
58C1: C2 09 7E   JP      NZ,$7E09        
58C4: 2F         CPL                     
58C5: 1F         RRA                     
58C6: 1F         RRA                     
58C7: E6 20      AND     $20             
58C9: E0 ED      LDFF00  ($ED),A         
58CB: 11 B3 58   LD      DE,$58B3        
58CE: CD 3B 3C   CALL    $3C3B           
58D1: CD 65 79   CALL    $7965           
58D4: CD E2 08   CALL    $08E2           
58D7: F0 E7      LD      A,($E7)         
58D9: 1F         RRA                     
58DA: 1F         RRA                     
58DB: 1F         RRA                     
58DC: 1F         RRA                     
58DD: E6 01      AND     $01             
58DF: CD 87 3B   CALL    $3B87           
58E2: CD B4 3B   CALL    $3BB4           
58E5: F0 E7      LD      A,($E7)         
58E7: E6 03      AND     $03             
58E9: 20 1E      JR      NZ,$5909        
58EB: 21 90 C2   LD      HL,$C290        
58EE: 09         ADD     HL,BC           
58EF: 7E         LD      A,(HL)          
58F0: E6 01      AND     $01             
58F2: 5F         LD      E,A             
58F3: 50         LD      D,B             
58F4: 21 BB 58   LD      HL,$58BB        
58F7: 19         ADD     HL,DE           
58F8: 7E         LD      A,(HL)          
58F9: 21 50 C2   LD      HL,$C250        
58FC: 09         ADD     HL,BC           
58FD: 86         ADD     A,(HL)          
58FE: 77         LD      (HL),A          
58FF: 21 BD 58   LD      HL,$58BD        
5902: 19         ADD     HL,DE           
5903: BE         CP      (HL)            
5904: 20 03      JR      NZ,$5909        
5906: CD 8D 3B   CALL    $3B8D           
5909: CD D1 79   CALL    $79D1           
590C: CD 91 08   CALL    $0891           
590F: 20 07      JR      NZ,$5918        
5911: F0 EE      LD      A,($EE)         
5913: FE A8      CP      $A8             
5915: D2 6B 7A   JP      NC,$7A6B        
5918: C9         RET                     
5919: 07         RLCA                    
591A: 00         NOP                     
591B: 0F         RRCA                    
591C: 07         RLCA                    
591D: 1E 0F      LD      E,$0F           
591F: 3F         CCF                     
5920: 18 3F      JR      $5961           
5922: 10 3F      STOP    $3F             
5924: 14         INC     D               
5925: 3F         CCF                     
5926: 10 27      STOP    $27             
5928: 1B         DEC     DE              
5929: E0 00      LDFF00  ($00),A         
592B: F0 E0      LD      A,($E0)         
592D: 18 F0      JR      $591F           
592F: 8C         ADC     A,H             
5930: 78         LD      A,B             
5931: 8C         ADC     A,H             
5932: 70         LD      (HL),B          
5933: 3F         CCF                     
5934: C0         RET     NZ              
5935: FF         RST     0X38            
5936: 3E EF      LD      A,$EF           
5938: F1         POP     AF              
5939: 00         NOP                     
593A: 00         NOP                     
593B: 00         NOP                     
593C: 00         NOP                     
593D: 00         NOP                     
593E: 00         NOP                     
593F: 00         NOP                     
5940: 00         NOP                     
5941: 00         NOP                     
5942: 00         NOP                     
5943: 00         NOP                     
5944: 00         NOP                     
5945: 03         INC     BC              
5946: 00         NOP                     
5947: 07         RLCA                    
5948: 03         INC     BC              
5949: 00         NOP                     
594A: 00         NOP                     
594B: 00         NOP                     
594C: 00         NOP                     
594D: 00         NOP                     
594E: 00         NOP                     
594F: 00         NOP                     
5950: 00         NOP                     
5951: 00         NOP                     
5952: 00         NOP                     
5953: 3F         CCF                     
5954: 00         NOP                     
5955: FF         RST     0X38            
5956: 3E EF      LD      A,$EF           
5958: F1         POP     AF              
5959: 21 30 C4   LD      HL,$C430        
595C: 09         ADD     HL,BC           
595D: 7E         LD      A,(HL)          
595E: E6 7F      AND     $7F             
5960: 77         LD      (HL),A          
5961: 1E 0F      LD      E,$0F           
5963: 50         LD      D,B             
5964: 21 80 C2   LD      HL,$C280        
5967: 19         ADD     HL,DE           
5968: 70         LD      (HL),B          
5969: 1D         DEC     E               
596A: 7B         LD      A,E             
596B: FE 01      CP      $01             
596D: 20 F5      JR      NZ,$5964        
596F: FA 78 D4   LD      A,($D478)       
5972: A7         AND     A               
5973: 28 23      JR      Z,$5998         
5975: 3E 05      LD      A,$05           
5977: CD B9 07   CALL    $07B9           
597A: CD 3F 5A   CALL    $5A3F           
597D: 21 90 C2   LD      HL,$C290        
5980: 19         ADD     HL,DE           
5981: 36 07      LD      (HL),$07        
5983: 21 E0 C2   LD      HL,$C2E0        
5986: 19         ADD     HL,DE           
5987: 36 60      LD      (HL),$60        
5989: 3E 01      LD      A,$01           
598B: E0 A5      LDFF00  ($A5),A         
598D: CD 8D 3B   CALL    $3B8D           
5990: 36 04      LD      (HL),$04        
5992: 3E C0      LD      A,$C0           
5994: EA 10 C2   LD      ($C210),A       
5997: C9         RET                     
5998: 3E 02      LD      A,$02           
599A: E0 A5      LDFF00  ($A5),A         
599C: EA 78 D4   LD      ($D478),A       
599F: CD 91 08   CALL    $0891           
59A2: 36 80      LD      (HL),$80        
59A4: 1E 0C      LD      E,$0C           
59A6: AF         XOR     A               
59A7: 21 90 D7   LD      HL,$D790        
59AA: 22         LD      (HLI),A         
59AB: 1D         DEC     E               
59AC: 20 FC      JR      NZ,$59AA        
59AE: 3E 02      LD      A,$02           
59B0: EA 05 D2   LD      ($D205),A       
59B3: 3E 5C      LD      A,$5C           
59B5: EA 68 D3   LD      ($D368),A       
59B8: C9         RET                     
59B9: 10 F0      STOP    $F0             
59BB: 21 B0 C2   LD      HL,$C2B0        
59BE: 09         ADD     HL,BC           
59BF: 7E         LD      A,(HL)          
59C0: C7         RST     0X00            
59C1: C9         RET                     
59C2: 59         LD      E,C             
59C3: AB         XOR     E               
59C4: 5A         LD      E,D             
59C5: A3         AND     E               
59C6: 61         LD      H,C             
59C7: 15         DEC     D               
59C8: 62         LD      H,D             
59C9: F0 F0      LD      A,($F0)         
59CB: C7         RST     0X00            
59CC: D7         RST     0X10            
59CD: 59         LD      E,C             
59CE: 16 5A      LD      D,$5A           
59D0: 76         HALT                    
59D1: 5A         LD      E,D             
59D2: 7A         LD      A,D             
59D3: 5A         LD      E,D             
59D4: 8A         ADC     A,D             
59D5: 5A         LD      E,D             
59D6: C9         RET                     
59D7: CD 99 5A   CALL    $5A99           
59DA: F0 EA      LD      A,($EA)         
59DC: FE 05      CP      $05             
59DE: 20 F6      JR      NZ,$59D6        
59E0: 3E 02      LD      A,$02           
59E2: E0 E8      LDFF00  ($E8),A         
59E4: 3E 63      LD      A,$63           
59E6: CD 01 3C   CALL    $3C01           
59E9: C5         PUSH    BC              
59EA: F0 E8      LD      A,($E8)         
59EC: 4F         LD      C,A             
59ED: 21 B8 59   LD      HL,$59B8        
59F0: 09         ADD     HL,BC           
59F1: F0 D7      LD      A,($D7)         
59F3: 86         ADD     A,(HL)          
59F4: 21 00 C2   LD      HL,$C200        
59F7: 19         ADD     HL,DE           
59F8: 77         LD      (HL),A          
59F9: F0 D8      LD      A,($D8)         
59FB: D6 10      SUB     $10             
59FD: 21 10 C2   LD      HL,$C210        
5A00: 19         ADD     HL,DE           
5A01: 77         LD      (HL),A          
5A02: C1         POP     BC              
5A03: 21 B0 C2   LD      HL,$C2B0        
5A06: 19         ADD     HL,DE           
5A07: 36 02      LD      (HL),$02        
5A09: F0 E8      LD      A,($E8)         
5A0B: 3D         DEC     A               
5A0C: 20 D4      JR      NZ,$59E2        
5A0E: CD 91 08   CALL    $0891           
5A11: 36 43      LD      (HL),$43        
5A13: C3 8D 3B   JP      $3B8D           
5A16: CD 99 5A   CALL    $5A99           
5A19: CD 65 79   CALL    $7965           
5A1C: 3E 02      LD      A,$02           
5A1E: E0 A1      LDFF00  ($A1),A         
5A20: CD 91 08   CALL    $0891           
5A23: A7         AND     A               
5A24: 28 14      JR      Z,$5A3A         
5A26: FE 20      CP      $20             
5A28: 20 4B      JR      NZ,$5A75        
5A2A: F0 99      LD      A,($99)         
5A2C: F5         PUSH    AF              
5A2D: 3E 10      LD      A,$10           
5A2F: E0 99      LDFF00  ($99),A         
5A31: 3E BA      LD      A,$BA           
5A33: CD 97 21   CALL    $2197           
5A36: F1         POP     AF              
5A37: E0 99      LDFF00  ($99),A         
5A39: C9         RET                     
5A3A: 3E 54      LD      A,$54           
5A3C: EA 68 D3   LD      ($D368),A       
5A3F: 3E 63      LD      A,$63           
5A41: CD 01 3C   CALL    $3C01           
5A44: 21 60 C3   LD      HL,$C360        
5A47: 19         ADD     HL,DE           
5A48: 36 0C      LD      (HL),$0C        
5A4A: 21 00 C2   LD      HL,$C200        
5A4D: 19         ADD     HL,DE           
5A4E: 36 D0      LD      (HL),$D0        
5A50: 21 10 C2   LD      HL,$C210        
5A53: 19         ADD     HL,DE           
5A54: 36 18      LD      (HL),$18        
5A56: 21 B0 C2   LD      HL,$C2B0        
5A59: 19         ADD     HL,DE           
5A5A: 36 01      LD      (HL),$01        
5A5C: 21 40 C2   LD      HL,$C240        
5A5F: 19         ADD     HL,DE           
5A60: 36 E0      LD      (HL),$E0        
5A62: 21 80 C3   LD      HL,$C380        
5A65: 19         ADD     HL,DE           
5A66: 36 00      LD      (HL),$00        
5A68: 21 E0 C2   LD      HL,$C2E0        
5A6B: 19         ADD     HL,DE           
5A6C: 36 80      LD      (HL),$80        
5A6E: CD 62 5B   CALL    $5B62           
5A71: CD 8D 3B   CALL    $3B8D           
5A74: C9         RET                     
5A75: C9         RET                     
5A76: CD 99 5A   CALL    $5A99           
5A79: C9         RET                     
5A7A: CD 99 5A   CALL    $5A99           
5A7D: CD 65 79   CALL    $7965           
5A80: CD D1 79   CALL    $79D1           
5A83: 21 50 C2   LD      HL,$C250        
5A86: 09         ADD     HL,BC           
5A87: 34         INC     (HL)            
5A88: 34         INC     (HL)            
5A89: C9         RET                     
5A8A: 21 40 C3   LD      HL,$C340        
5A8D: 09         ADD     HL,BC           
5A8E: 36 C2      LD      (HL),$C2        
5A90: C9         RET                     
5A91: 7E         LD      A,(HL)          
5A92: 00         NOP                     
5A93: 7E         LD      A,(HL)          
5A94: 20 7E      JR      NZ,$5B14        
5A96: 40         LD      B,B             
5A97: 7E         LD      A,(HL)          
5A98: 60         LD      H,B             
5A99: 11 91 5A   LD      DE,$5A91        
5A9C: CD 3B 3C   CALL    $3C3B           
5A9F: C9         RET                     
5AA0: 02         LD      (BC),A          
5AA1: 02         LD      (BC),A          
5AA2: 02         LD      (BC),A          
5AA3: 00         NOP                     
5AA4: 01 00 01   LD      BC,$0100        
5AA7: 04         INC     B               
5AA8: 04         INC     B               
5AA9: 04         INC     B               
5AAA: 04         INC     B               
5AAB: CD 3F 61   CALL    $613F           
5AAE: F0 EA      LD      A,($EA)         
5AB0: FE 05      CP      $05             
5AB2: C2 8D 7D   JP      NZ,$7D8D        
5AB5: CD 65 79   CALL    $7965           
5AB8: CD E2 08   CALL    $08E2           
5ABB: F0 F0      LD      A,($F0)         
5ABD: FE 0E      CP      $0E             
5ABF: 28 36      JR      Z,$5AF7         
5AC1: 21 20 C4   LD      HL,$C420        
5AC4: 09         ADD     HL,BC           
5AC5: 7E         LD      A,(HL)          
5AC6: A7         AND     A               
5AC7: 28 2E      JR      Z,$5AF7         
5AC9: 21 20 C4   LD      HL,$C420        
5ACC: 09         ADD     HL,BC           
5ACD: 36 50      LD      (HL),$50        
5ACF: CD AF 3D   CALL    $3DAF           
5AD2: CD 8D 3B   CALL    $3B8D           
5AD5: 36 0E      LD      (HL),$0E        
5AD7: 3E 31      LD      A,$31           
5AD9: E0 F4      LDFF00  ($F4),A         
5ADB: 21 40 C3   LD      HL,$C340        
5ADE: 09         ADD     HL,BC           
5ADF: 36 42      LD      (HL),$42        
5AE1: 21 D0 C2   LD      HL,$C2D0        
5AE4: 09         ADD     HL,BC           
5AE5: 34         INC     (HL)            
5AE6: 7E         LD      A,(HL)          
5AE7: FE 08      CP      $08             
5AE9: 20 01      JR      NZ,$5AEC        
5AEB: 35         DEC     (HL)            
5AEC: 5F         LD      E,A             
5AED: 50         LD      D,B             
5AEE: 21 A0 5A   LD      HL,$5AA0        
5AF1: 19         ADD     HL,DE           
5AF2: 7E         LD      A,(HL)          
5AF3: EA 05 D2   LD      ($D205),A       
5AF6: C9         RET                     
5AF7: F0 F0      LD      A,($F0)         
5AF9: C7         RST     0X00            
5AFA: 18 5B      JR      $5B57           
5AFC: 2E 5B      LD      L,$5B           
5AFE: 74         LD      (HL),H          
5AFF: 5B         LD      E,E             
5B00: 9F         SBC     A               
5B01: 5B         LD      E,E             
5B02: D0         RET     NC              
5B03: 5B         LD      E,E             
5B04: F2         ???                     
5B05: 5B         LD      E,E             
5B06: 15         DEC     D               
5B07: 5C         LD      E,H             
5B08: 5B         LD      E,E             
5B09: 5C         LD      E,H             
5B0A: 33         INC     SP              
5B0B: 5D         LD      E,L             
5B0C: 84         ADD     A,H             
5B0D: 5D         LD      E,L             
5B0E: 82         ADD     A,D             
5B0F: 5E         LD      E,(HL)          
5B10: DB         ???                     
5B11: 5E         LD      E,(HL)          
5B12: F1         POP     AF              
5B13: 5E         LD      E,(HL)          
5B14: 62         LD      H,D             
5B15: 5F         LD      E,A             
5B16: 73         LD      (HL),E          
5B17: 5F         LD      E,A             
5B18: CD D1 79   CALL    $79D1           
5B1B: CD 91 08   CALL    $0891           
5B1E: 20 0D      JR      NZ,$5B2D        
5B20: CD 8D 3B   CALL    $3B8D           
5B23: CD 91 08   CALL    $0891           
5B26: 36 20      LD      (HL),$20        
5B28: 3E FF      LD      A,$FF           
5B2A: CD 87 3B   CALL    $3B87           
5B2D: C9         RET                     
5B2E: CD 91 08   CALL    $0891           
5B31: 20 33      JR      NZ,$5B66        
5B33: AF         XOR     A               
5B34: CD 87 3B   CALL    $3B87           
5B37: 21 10 C2   LD      HL,$C210        
5B3A: 09         ADD     HL,BC           
5B3B: 7E         LD      A,(HL)          
5B3C: C6 14      ADD     $14             
5B3E: 77         LD      (HL),A          
5B3F: 21 40 C2   LD      HL,$C240        
5B42: 09         ADD     HL,BC           
5B43: 7E         LD      A,(HL)          
5B44: 2F         CPL                     
5B45: 3C         INC     A               
5B46: 77         LD      (HL),A          
5B47: 21 80 C3   LD      HL,$C380        
5B4A: 09         ADD     HL,BC           
5B4B: 7E         LD      A,(HL)          
5B4C: EE 04      XOR     $04             
5B4E: 77         LD      (HL),A          
5B4F: 21 C0 C2   LD      HL,$C2C0        
5B52: 09         ADD     HL,BC           
5B53: 34         INC     (HL)            
5B54: 7E         LD      A,(HL)          
5B55: FE 02      CP      $02             
5B57: 28 0E      JR      Z,$5B67         
5B59: CD 8D 3B   CALL    $3B8D           
5B5C: 70         LD      (HL),B          
5B5D: CD 91 08   CALL    $0891           
5B60: 36 80      LD      (HL),$80        
5B62: 3E 22      LD      A,$22           
5B64: E0 F4      LDFF00  ($F4),A         
5B66: C9         RET                     
5B67: CD 8D 3B   CALL    $3B8D           
5B6A: CD 91 08   CALL    $0891           
5B6D: 36 30      LD      (HL),$30        
5B6F: 3E 30      LD      A,$30           
5B71: E0 F4      LDFF00  ($F4),A         
5B73: C9         RET                     
5B74: CD D1 79   CALL    $79D1           
5B77: CD 91 08   CALL    $0891           
5B7A: FE 01      CP      $01             
5B7C: 20 05      JR      NZ,$5B83        
5B7E: 21 F2 FF   LD      HL,$FFF2        
5B81: 36 30      LD      (HL),$30        
5B83: A7         AND     A               
5B84: 20 18      JR      NZ,$5B9E        
5B86: 21 40 C2   LD      HL,$C240        
5B89: 09         ADD     HL,BC           
5B8A: 34         INC     (HL)            
5B8B: 20 0E      JR      NZ,$5B9B        
5B8D: CD 8D 3B   CALL    $3B8D           
5B90: CD 91 08   CALL    $0891           
5B93: 36 40      LD      (HL),$40        
5B95: 21 9E C2   LD      HL,$C29E        
5B98: 34         INC     (HL)            
5B99: 23         INC     HL              
5B9A: 34         INC     (HL)            
5B9B: CD BF 5B   CALL    $5BBF           
5B9E: C9         RET                     
5B9F: 3E 02      LD      A,$02           
5BA1: E0 A1      LDFF00  ($A1),A         
5BA3: CD 91 08   CALL    $0891           
5BA6: 20 17      JR      NZ,$5BBF        
5BA8: 36 28      LD      (HL),$28        
5BAA: 3E D0      LD      A,$D0           
5BAC: EA 50 C2   LD      ($C250),A       
5BAF: 3E 24      LD      A,$24           
5BB1: E0 F2      LDFF00  ($F2),A         
5BB3: 3E 12      LD      A,$12           
5BB5: EA 40 C2   LD      ($C240),A       
5BB8: 21 90 C2   LD      HL,$C290        
5BBB: 34         INC     (HL)            
5BBC: CD 8D 3B   CALL    $3B8D           
5BBF: 21 D0 C3   LD      HL,$C3D0        
5BC2: 09         ADD     HL,BC           
5BC3: 34         INC     (HL)            
5BC4: 7E         LD      A,(HL)          
5BC5: E6 04      AND     $04             
5BC7: 3E 01      LD      A,$01           
5BC9: 28 01      JR      Z,$5BCC         
5BCB: 3C         INC     A               
5BCC: CD 87 3B   CALL    $3B87           
5BCF: C9         RET                     
5BD0: 3E 02      LD      A,$02           
5BD2: E0 A1      LDFF00  ($A1),A         
5BD4: CD 91 08   CALL    $0891           
5BD7: 20 12      JR      NZ,$5BEB        
5BD9: 3E 01      LD      A,$01           
5BDB: E0 A5      LDFF00  ($A5),A         
5BDD: 36 20      LD      (HL),$20        
5BDF: CD 8D 3B   CALL    $3B8D           
5BE2: 21 90 C2   LD      HL,$C290        
5BE5: 34         INC     (HL)            
5BE6: 3E C0      LD      A,$C0           
5BE8: EA 10 C2   LD      ($C210),A       
5BEB: C3 BF 5B   JP      $5BBF           
5BEE: 01 02 03   LD      BC,$0302        
5BF1: 02         LD      (BC),A          
5BF2: 3E 02      LD      A,$02           
5BF4: E0 A1      LDFF00  ($A1),A         
5BF6: CD 91 08   CALL    $0891           
5BF9: 20 03      JR      NZ,$5BFE        
5BFB: CD 8D 3B   CALL    $3B8D           
5BFE: 21 D0 C3   LD      HL,$C3D0        
5C01: 09         ADD     HL,BC           
5C02: 34         INC     (HL)            
5C03: 7E         LD      A,(HL)          
5C04: 1F         RRA                     
5C05: 1F         RRA                     
5C06: 1F         RRA                     
5C07: 00         NOP                     
5C08: E6 03      AND     $03             
5C0A: 5F         LD      E,A             
5C0B: 50         LD      D,B             
5C0C: 21 EE 5B   LD      HL,$5BEE        
5C0F: 19         ADD     HL,DE           
5C10: 7E         LD      A,(HL)          
5C11: CD 87 3B   CALL    $3B87           
5C14: C9         RET                     
5C15: CD D1 79   CALL    $79D1           
5C18: 21 40 C2   LD      HL,$C240        
5C1B: 09         ADD     HL,BC           
5C1C: 7E         LD      A,(HL)          
5C1D: FE D4      CP      $D4             
5C1F: 20 21      JR      NZ,$5C42        
5C21: F0 EE      LD      A,($EE)         
5C23: E6 F8      AND     $F8             
5C25: FE C0      CP      $C0             
5C27: 20 09      JR      NZ,$5C32        
5C29: CD 8D 3B   CALL    $3B8D           
5C2C: CD 91 08   CALL    $0891           
5C2F: 36 80      LD      (HL),$80        
5C31: C9         RET                     
5C32: F0 E7      LD      A,($E7)         
5C34: E6 00      AND     $00             
5C36: 20 05      JR      NZ,$5C3D        
5C38: 21 50 C2   LD      HL,$C250        
5C3B: 09         ADD     HL,BC           
5C3C: 35         DEC     (HL)            
5C3D: AF         XOR     A               
5C3E: CD 87 3B   CALL    $3B87           
5C41: C9         RET                     
5C42: 35         DEC     (HL)            
5C43: 35         DEC     (HL)            
5C44: CD FE 5B   CALL    $5BFE           
5C47: CD FE 5B   CALL    $5BFE           
5C4A: C3 FE 5B   JP      $5BFE           
5C4D: F8 A8      LDHL    SP,$A8          
5C4F: 30 D0      JR      NC,$5C21        
5C51: 30 70      JR      NC,$5CC3        
5C53: DC 24 F8   CALL    C,$F824         
5C56: A8         XOR     B               
5C57: 20 E0      JR      NZ,$5C39        
5C59: 04         INC     B               
5C5A: 00         NOP                     
5C5B: CD 91 08   CALL    $0891           
5C5E: 20 4F      JR      NZ,$5CAF        
5C60: FA 05 D2   LD      A,($D205)       
5C63: C7         RST     0X00            
5C64: 6E         LD      L,(HL)          
5C65: 5C         LD      E,H             
5C66: B0         OR      B               
5C67: 5C         LD      E,H             
5C68: EA 5C EA   LD      ($EA5C),A       
5C6B: 5C         LD      E,H             
5C6C: B0         OR      B               
5C6D: 5C         LD      E,H             
5C6E: CD ED 27   CALL    $27ED           
5C71: E6 03      AND     $03             
5C73: EA 05 D2   LD      ($D205),A       
5C76: 1E 00      LD      E,$00           
5C78: F0 98      LD      A,($98)         
5C7A: FE 50      CP      $50             
5C7C: 30 01      JR      NC,$5C7F        
5C7E: 1C         INC     E               
5C7F: 50         LD      D,B             
5C80: 21 4D 5C   LD      HL,$5C4D        
5C83: 19         ADD     HL,DE           
5C84: 7E         LD      A,(HL)          
5C85: 21 00 C2   LD      HL,$C200        
5C88: 09         ADD     HL,BC           
5C89: 77         LD      (HL),A          
5C8A: 21 4F 5C   LD      HL,$5C4F        
5C8D: 19         ADD     HL,DE           
5C8E: 7E         LD      A,(HL)          
5C8F: 21 40 C2   LD      HL,$C240        
5C92: 09         ADD     HL,BC           
5C93: 77         LD      (HL),A          
5C94: 21 59 5C   LD      HL,$5C59        
5C97: 19         ADD     HL,DE           
5C98: 7E         LD      A,(HL)          
5C99: 21 80 C3   LD      HL,$C380        
5C9C: 09         ADD     HL,BC           
5C9D: 77         LD      (HL),A          
5C9E: 21 10 C2   LD      HL,$C210        
5CA1: 09         ADD     HL,BC           
5CA2: 36 00      LD      (HL),$00        
5CA4: 21 50 C2   LD      HL,$C250        
5CA7: 09         ADD     HL,BC           
5CA8: 36 20      LD      (HL),$20        
5CAA: CD 8D 3B   CALL    $3B8D           
5CAD: 36 08      LD      (HL),$08        
5CAF: C9         RET                     
5CB0: 1E 00      LD      E,$00           
5CB2: F0 98      LD      A,($98)         
5CB4: FE 50      CP      $50             
5CB6: 30 01      JR      NC,$5CB9        
5CB8: 1C         INC     E               
5CB9: 50         LD      D,B             
5CBA: 21 51 5C   LD      HL,$5C51        
5CBD: 19         ADD     HL,DE           
5CBE: 7E         LD      A,(HL)          
5CBF: 21 00 C2   LD      HL,$C200        
5CC2: 09         ADD     HL,BC           
5CC3: 77         LD      (HL),A          
5CC4: 21 40 C2   LD      HL,$C240        
5CC7: 09         ADD     HL,BC           
5CC8: 70         LD      (HL),B          
5CC9: 21 59 5C   LD      HL,$5C59        
5CCC: 19         ADD     HL,DE           
5CCD: 7E         LD      A,(HL)          
5CCE: 21 80 C3   LD      HL,$C380        
5CD1: 09         ADD     HL,BC           
5CD2: 77         LD      (HL),A          
5CD3: 21 10 C2   LD      HL,$C210        
5CD6: 09         ADD     HL,BC           
5CD7: 36 F0      LD      (HL),$F0        
5CD9: 21 50 C2   LD      HL,$C250        
5CDC: 09         ADD     HL,BC           
5CDD: 36 10      LD      (HL),$10        
5CDF: CD 8D 3B   CALL    $3B8D           
5CE2: 36 0B      LD      (HL),$0B        
5CE4: CD 91 08   CALL    $0891           
5CE7: 36 30      LD      (HL),$30        
5CE9: C9         RET                     
5CEA: CD ED 27   CALL    $27ED           
5CED: E6 01      AND     $01             
5CEF: 5F         LD      E,A             
5CF0: 50         LD      D,B             
5CF1: 21 55 5C   LD      HL,$5C55        
5CF4: 19         ADD     HL,DE           
5CF5: 7E         LD      A,(HL)          
5CF6: 21 00 C2   LD      HL,$C200        
5CF9: 09         ADD     HL,BC           
5CFA: 77         LD      (HL),A          
5CFB: 21 57 5C   LD      HL,$5C57        
5CFE: 19         ADD     HL,DE           
5CFF: 7E         LD      A,(HL)          
5D00: 21 40 C2   LD      HL,$C240        
5D03: 09         ADD     HL,BC           
5D04: 77         LD      (HL),A          
5D05: 21 50 C2   LD      HL,$C250        
5D08: 09         ADD     HL,BC           
5D09: 70         LD      (HL),B          
5D0A: 21 59 5C   LD      HL,$5C59        
5D0D: 19         ADD     HL,DE           
5D0E: 7E         LD      A,(HL)          
5D0F: 21 80 C3   LD      HL,$C380        
5D12: 09         ADD     HL,BC           
5D13: 77         LD      (HL),A          
5D14: CD ED 27   CALL    $27ED           
5D17: E6 3F      AND     $3F             
5D19: C6 18      ADD     $18             
5D1B: 21 10 C2   LD      HL,$C210        
5D1E: 09         ADD     HL,BC           
5D1F: 77         LD      (HL),A          
5D20: F0 9C      LD      A,($9C)         
5D22: A7         AND     A               
5D23: 28 03      JR      Z,$5D28         
5D25: F0 99      LD      A,($99)         
5D27: 77         LD      (HL),A          
5D28: CD 8D 3B   CALL    $3B8D           
5D2B: 36 0D      LD      (HL),$0D        
5D2D: CD 91 08   CALL    $0891           
5D30: 36 70      LD      (HL),$70        
5D32: C9         RET                     
5D33: 3E 01      LD      A,$01           
5D35: CD 87 3B   CALL    $3B87           
5D38: CD D1 79   CALL    $79D1           
5D3B: 21 50 C2   LD      HL,$C250        
5D3E: CD 48 5D   CALL    $5D48           
5D41: 7E         LD      A,(HL)          
5D42: A7         AND     A               
5D43: 28 10      JR      Z,$5D55         
5D45: 21 40 C2   LD      HL,$C240        
5D48: 09         ADD     HL,BC           
5D49: 7E         LD      A,(HL)          
5D4A: A7         AND     A               
5D4B: 28 07      JR      Z,$5D54         
5D4D: E6 80      AND     $80             
5D4F: 20 02      JR      NZ,$5D53        
5D51: 35         DEC     (HL)            
5D52: 35         DEC     (HL)            
5D53: 34         INC     (HL)            
5D54: C9         RET                     
5D55: CD 8D 3B   CALL    $3B8D           
5D58: CD 91 08   CALL    $0891           
5D5B: 36 FF      LD      (HL),$FF        
5D5D: C9         RET                     
5D5E: EE 12      XOR     $12             
5D60: D0         RET     NC              
5D61: 30 10      JR      NC,$5D73        
5D63: F0 D8      LD      A,($D8)         
5D65: D4 D0 CC   CALL    NC,$CCD0        
5D68: C8         RET     Z               
5D69: C4 C0 BC   CALL    NZ,$BCC0        
5D6C: 28 2C      JR      Z,$5D9A         
5D6E: 30 34      JR      NC,$5DA4        
5D70: 38 3C      JR      C,$5DAE         
5D72: 40         LD      B,B             
5D73: 44         LD      B,H             
5D74: 30 2E      JR      NC,$5DA4        
5D76: 2C         INC     L               
5D77: 2A         LD      A,(HLI)         
5D78: 28 26      JR      Z,$5DA0         
5D7A: 24         INC     H               
5D7B: 22         LD      (HLI),A         
5D7C: 30 2E      JR      NC,$5DAC        
5D7E: 2C         INC     L               
5D7F: 2A         LD      A,(HLI)         
5D80: 28 26      JR      Z,$5DA8         
5D82: 24         INC     H               
5D83: 22         LD      (HLI),A         
5D84: CD 91 08   CALL    $0891           
5D87: CA 77 5E   JP      Z,$5E77         
5D8A: 21 10 C2   LD      HL,$C210        
5D8D: 09         ADD     HL,BC           
5D8E: F0 E7      LD      A,($E7)         
5D90: E6 03      AND     $03             
5D92: 20 09      JR      NZ,$5D9D        
5D94: F0 E7      LD      A,($E7)         
5D96: E6 20      AND     $20             
5D98: 28 02      JR      Z,$5D9C         
5D9A: 34         INC     (HL)            
5D9B: 34         INC     (HL)            
5D9C: 35         DEC     (HL)            
5D9D: CD FE 5B   CALL    $5BFE           
5DA0: CD FE 5B   CALL    $5BFE           
5DA3: F0 9C      LD      A,($9C)         
5DA5: A7         AND     A               
5DA6: 20 29      JR      NZ,$5DD1        
5DA8: FA 46 C1   LD      A,($C146)       
5DAB: A7         AND     A               
5DAC: 28 23      JR      Z,$5DD1         
5DAE: 21 80 C3   LD      HL,$C380        
5DB1: 09         ADD     HL,BC           
5DB2: 7E         LD      A,(HL)          
5DB3: 1F         RRA                     
5DB4: 1F         RRA                     
5DB5: E6 01      AND     $01             
5DB7: 5F         LD      E,A             
5DB8: 50         LD      D,B             
5DB9: 21 60 5D   LD      HL,$5D60        
5DBC: 19         ADD     HL,DE           
5DBD: 7E         LD      A,(HL)          
5DBE: 21 9A FF   LD      HL,$FF9A        
5DC1: 96         SUB     (HL)            
5DC2: A7         AND     A               
5DC3: 28 25      JR      Z,$5DEA         
5DC5: E6 80      AND     $80             
5DC7: 20 04      JR      NZ,$5DCD        
5DC9: 34         INC     (HL)            
5DCA: 34         INC     (HL)            
5DCB: 34         INC     (HL)            
5DCC: 34         INC     (HL)            
5DCD: 35         DEC     (HL)            
5DCE: 35         DEC     (HL)            
5DCF: 18 19      JR      $5DEA           
5DD1: 21 80 C3   LD      HL,$C380        
5DD4: 09         ADD     HL,BC           
5DD5: 5E         LD      E,(HL)          
5DD6: CB 3B      SET     1,E             
5DD8: CB 3B      SET     1,E             
5DDA: 50         LD      D,B             
5DDB: 21 5E 5D   LD      HL,$5D5E        
5DDE: 19         ADD     HL,DE           
5DDF: 7E         LD      A,(HL)          
5DE0: E0 9A      LDFF00  ($9A),A         
5DE2: C5         PUSH    BC              
5DE3: CD E0 20   CALL    $20E0           
5DE6: CD 49 3E   CALL    $3E49           
5DE9: C1         POP     BC              
5DEA: FA 10 D2   LD      A,($D210)       
5DED: 3C         INC     A               
5DEE: FE 22      CP      $22             
5DF0: 38 05      JR      C,$5DF7         
5DF2: 3E 32      LD      A,$32           
5DF4: E0 F4      LDFF00  ($F4),A         
5DF6: AF         XOR     A               
5DF7: EA 10 D2   LD      ($D210),A       
5DFA: CD 91 08   CALL    $0891           
5DFD: FE C0      CP      $C0             
5DFF: 30 75      JR      NC,$5E76        
5E01: F0 E7      LD      A,($E7)         
5E03: E6 0F      AND     $0F             
5E05: 20 6F      JR      NZ,$5E76        
5E07: 3E 63      LD      A,$63           
5E09: 1E 03      LD      E,$03           
5E0B: CD 13 3C   CALL    $3C13           
5E0E: 38 66      JR      C,$5E76         
5E10: 21 B0 C2   LD      HL,$C2B0        
5E13: 19         ADD     HL,DE           
5E14: 36 03      LD      (HL),$03        
5E16: C5         PUSH    BC              
5E17: 21 80 C3   LD      HL,$C380        
5E1A: 09         ADD     HL,BC           
5E1B: 4E         LD      C,(HL)          
5E1C: CB 39      SET     1,E             
5E1E: CB 39      SET     1,E             
5E20: 21 62 5D   LD      HL,$5D62        
5E23: 09         ADD     HL,BC           
5E24: F0 D7      LD      A,($D7)         
5E26: 86         ADD     A,(HL)          
5E27: 21 00 C2   LD      HL,$C200        
5E2A: 19         ADD     HL,DE           
5E2B: 77         LD      (HL),A          
5E2C: F0 D8      LD      A,($D8)         
5E2E: 21 10 C2   LD      HL,$C210        
5E31: 19         ADD     HL,DE           
5E32: C6 0C      ADD     $0C             
5E34: 77         LD      (HL),A          
5E35: 21 B0 C3   LD      HL,$C3B0        
5E38: 19         ADD     HL,DE           
5E39: 79         LD      A,C             
5E3A: EE 01      XOR     $01             
5E3C: 77         LD      (HL),A          
5E3D: 21 80 C3   LD      HL,$C380        
5E40: 19         ADD     HL,DE           
5E41: 77         LD      (HL),A          
5E42: CB 21      SET     1,E             
5E44: CB 21      SET     1,E             
5E46: CB 21      SET     1,E             
5E48: CD ED 27   CALL    $27ED           
5E4B: E6 07      AND     $07             
5E4D: 81         ADD     A,C             
5E4E: 4F         LD      C,A             
5E4F: 21 74 5D   LD      HL,$5D74        
5E52: 09         ADD     HL,BC           
5E53: 7E         LD      A,(HL)          
5E54: 21 50 C2   LD      HL,$C250        
5E57: 19         ADD     HL,DE           
5E58: 77         LD      (HL),A          
5E59: 21 64 5D   LD      HL,$5D64        
5E5C: 09         ADD     HL,BC           
5E5D: 7E         LD      A,(HL)          
5E5E: 21 40 C2   LD      HL,$C240        
5E61: 19         ADD     HL,DE           
5E62: 77         LD      (HL),A          
5E63: C1         POP     BC              
5E64: 21 40 C3   LD      HL,$C340        
5E67: 19         ADD     HL,DE           
5E68: 36 02      LD      (HL),$02        
5E6A: 21 30 C4   LD      HL,$C430        
5E6D: 19         ADD     HL,DE           
5E6E: 36 00      LD      (HL),$00        
5E70: 21 D0 C4   LD      HL,$C4D0        
5E73: 19         ADD     HL,DE           
5E74: 36 02      LD      (HL),$02        
5E76: C9         RET                     
5E77: CD 8D 3B   CALL    $3B8D           
5E7A: CD 91 08   CALL    $0891           
5E7D: 36 50      LD      (HL),$50        
5E7F: C9         RET                     
5E80: E0 20      LDFF00  ($20),A         
5E82: CD D1 79   CALL    $79D1           
5E85: CD 91 08   CALL    $0891           
5E88: 28 36      JR      Z,$5EC0         
5E8A: 21 80 C3   LD      HL,$C380        
5E8D: 09         ADD     HL,BC           
5E8E: 7E         LD      A,(HL)          
5E8F: 1F         RRA                     
5E90: 1F         RRA                     
5E91: E6 01      AND     $01             
5E93: 5F         LD      E,A             
5E94: 50         LD      D,B             
5E95: 21 80 5E   LD      HL,$5E80        
5E98: 19         ADD     HL,DE           
5E99: 7E         LD      A,(HL)          
5E9A: 21 40 C2   LD      HL,$C240        
5E9D: 09         ADD     HL,BC           
5E9E: 96         SUB     (HL)            
5E9F: A7         AND     A               
5EA0: 28 0E      JR      Z,$5EB0         
5EA2: E6 80      AND     $80             
5EA4: 20 02      JR      NZ,$5EA8        
5EA6: 34         INC     (HL)            
5EA7: 34         INC     (HL)            
5EA8: 35         DEC     (HL)            
5EA9: CD FE 5B   CALL    $5BFE           
5EAC: CD FE 5B   CALL    $5BFE           
5EAF: C9         RET                     
5EB0: AF         XOR     A               
5EB1: CD 87 3B   CALL    $3B87           
5EB4: F0 E7      LD      A,($E7)         
5EB6: E6 01      AND     $01             
5EB8: 20 05      JR      NZ,$5EBF        
5EBA: 21 50 C2   LD      HL,$C250        
5EBD: 09         ADD     HL,BC           
5EBE: 35         DEC     (HL)            
5EBF: C9         RET                     
5EC0: 21 40 C3   LD      HL,$C340        
5EC3: 09         ADD     HL,BC           
5EC4: 36 02      LD      (HL),$02        
5EC6: CD 8D 3B   CALL    $3B8D           
5EC9: 36 07      LD      (HL),$07        
5ECB: CD 91 08   CALL    $0891           
5ECE: FA 05 D2   LD      A,($D205)       
5ED1: FE 04      CP      $04             
5ED3: 20 03      JR      NZ,$5ED8        
5ED5: 36 10      LD      (HL),$10        
5ED7: C9         RET                     
5ED8: 36 80      LD      (HL),$80        
5EDA: C9         RET                     
5EDB: CD D1 79   CALL    $79D1           
5EDE: CD 91 08   CALL    $0891           
5EE1: 20 08      JR      NZ,$5EEB        
5EE3: 36 30      LD      (HL),$30        
5EE5: CD 8D 3B   CALL    $3B8D           
5EE8: CD AF 3D   CALL    $3DAF           
5EEB: CD FE 5B   CALL    $5BFE           
5EEE: C9         RET                     
5EEF: E0 20      LDFF00  ($20),A         
5EF1: CD D1 79   CALL    $79D1           
5EF4: CD 91 08   CALL    $0891           
5EF7: 20 3A      JR      NZ,$5F33        
5EF9: F0 EC      LD      A,($EC)         
5EFB: FE B0      CP      $B0             
5EFD: D2 C0 5E   JP      NC,$5EC0        
5F00: 3E 01      LD      A,$01           
5F02: CD 87 3B   CALL    $3B87           
5F05: FA 3E C1   LD      A,($C13E)       
5F08: A7         AND     A               
5F09: 20 27      JR      NZ,$5F32        
5F0B: CD B4 3B   CALL    $3BB4           
5F0E: FA 3E C1   LD      A,($C13E)       
5F11: A7         AND     A               
5F12: 28 1E      JR      Z,$5F32         
5F14: 3E 10      LD      A,$10           
5F16: EA 3E C1   LD      ($C13E),A       
5F19: 21 80 C3   LD      HL,$C380        
5F1C: 09         ADD     HL,BC           
5F1D: 5E         LD      E,(HL)          
5F1E: CB 3B      SET     1,E             
5F20: CB 3B      SET     1,E             
5F22: 50         LD      D,B             
5F23: 21 EF 5E   LD      HL,$5EEF        
5F26: 19         ADD     HL,DE           
5F27: 7E         LD      A,(HL)          
5F28: E0 9A      LDFF00  ($9A),A         
5F2A: 3E F0      LD      A,$F0           
5F2C: E0 9B      LDFF00  ($9B),A         
5F2E: 21 99 FF   LD      HL,$FF99        
5F31: 35         DEC     (HL)            
5F32: C9         RET                     
5F33: FE 01      CP      $01             
5F35: 20 1A      JR      NZ,$5F51        
5F37: 21 80 C3   LD      HL,$C380        
5F3A: 09         ADD     HL,BC           
5F3B: 5E         LD      E,(HL)          
5F3C: CB 3B      SET     1,E             
5F3E: CB 3B      SET     1,E             
5F40: 50         LD      D,B             
5F41: 21 53 5C   LD      HL,$5C53        
5F44: 19         ADD     HL,DE           
5F45: 7E         LD      A,(HL)          
5F46: 21 40 C2   LD      HL,$C240        
5F49: 09         ADD     HL,BC           
5F4A: 77         LD      (HL),A          
5F4B: 21 50 C2   LD      HL,$C250        
5F4E: 09         ADD     HL,BC           
5F4F: 36 34      LD      (HL),$34        
5F51: CD FE 5B   CALL    $5BFE           
5F54: CD 91 08   CALL    $0891           
5F57: FE 40      CP      $40             
5F59: 30 06      JR      NC,$5F61        
5F5B: CD FE 5B   CALL    $5BFE           
5F5E: CD FE 5B   CALL    $5BFE           
5F61: C9         RET                     
5F62: AF         XOR     A               
5F63: CD 87 3B   CALL    $3B87           
5F66: CD D1 79   CALL    $79D1           
5F69: CD B4 3B   CALL    $3BB4           
5F6C: CD 91 08   CALL    $0891           
5F6F: CA C0 5E   JP      Z,$5EC0         
5F72: C9         RET                     
5F73: 21 20 C4   LD      HL,$C420        
5F76: 09         ADD     HL,BC           
5F77: 7E         LD      A,(HL)          
5F78: A7         AND     A               
5F79: 28 12      JR      Z,$5F8D         
5F7B: FE 30      CP      $30             
5F7D: 30 0D      JR      NC,$5F8C        
5F7F: 3D         DEC     A               
5F80: 20 04      JR      NZ,$5F86        
5F82: 3E 31      LD      A,$31           
5F84: E0 F4      LDFF00  ($F4),A         
5F86: CD FE 5B   CALL    $5BFE           
5F89: CD FE 5B   CALL    $5BFE           
5F8C: C9         RET                     
5F8D: CD FE 5B   CALL    $5BFE           
5F90: CD FE 5B   CALL    $5BFE           
5F93: CD FE 5B   CALL    $5BFE           
5F96: 21 50 C2   LD      HL,$C250        
5F99: 09         ADD     HL,BC           
5F9A: 7E         LD      A,(HL)          
5F9B: FE D0      CP      $D0             
5F9D: 28 01      JR      Z,$5FA0         
5F9F: 35         DEC     (HL)            
5FA0: CD D1 79   CALL    $79D1           
5FA3: F0 EC      LD      A,($EC)         
5FA5: E6 F0      AND     $F0             
5FA7: FE C0      CP      $C0             
5FA9: 20 03      JR      NZ,$5FAE        
5FAB: C3 C0 5E   JP      $5EC0           
5FAE: C9         RET                     
5FAF: 00         NOP                     
5FB0: 00         NOP                     
5FB1: 40         LD      B,B             
5FB2: 00         NOP                     
5FB3: 00         NOP                     
5FB4: 08 42 00   LD      ($0042),SP      
5FB7: 00         NOP                     
5FB8: 10 44      STOP    $44             
5FBA: 00         NOP                     
5FBB: F8 18      LDHL    SP,$18          
5FBD: 46         LD      B,(HL)          
5FBE: 00         NOP                     
5FBF: F8 20      LDHL    SP,$20          
5FC1: 48         LD      C,B             
5FC2: 00         NOP                     
5FC3: F8 28      LDHL    SP,$28          
5FC5: 4A         LD      C,D             
5FC6: 00         NOP                     
5FC7: 08 18 4C   LD      ($4C18),SP      
5FCA: 00         NOP                     
5FCB: 08 20 4E   LD      ($4E20),SP      
5FCE: 00         NOP                     
5FCF: 08 28 50   LD      ($5028),SP      
5FD2: 00         NOP                     
5FD3: 00         NOP                     
5FD4: 30 52      JR      NC,$6028        
5FD6: 00         NOP                     
5FD7: FF         RST     0X38            
5FD8: FF         RST     0X38            
5FD9: FF         RST     0X38            
5FDA: FF         RST     0X38            
5FDB: FF         RST     0X38            
5FDC: FF         RST     0X38            
5FDD: FF         RST     0X38            
5FDE: FF         RST     0X38            
5FDF: 00         NOP                     
5FE0: 00         NOP                     
5FE1: 40         LD      B,B             
5FE2: 00         NOP                     
5FE3: 00         NOP                     
5FE4: 08 42 00   LD      ($0042),SP      
5FE7: 00         NOP                     
5FE8: 10 5A      STOP    $5A             
5FEA: 00         NOP                     
5FEB: 00         NOP                     
5FEC: 18 5C      JR      $604A           
5FEE: 00         NOP                     
5FEF: 00         NOP                     
5FF0: 20 5E      JR      NZ,$6050        
5FF2: 00         NOP                     
5FF3: 10 08      STOP    $08             
5FF5: 60         LD      H,B             
5FF6: 00         NOP                     
5FF7: 10 10      STOP    $10             
5FF9: 62         LD      H,D             
5FFA: 00         NOP                     
5FFB: 10 18      STOP    $18             
5FFD: 64         LD      H,H             
5FFE: 00         NOP                     
5FFF: 10 20      STOP    $20             
6001: 66         LD      H,(HL)          
6002: 00         NOP                     
6003: F0 18      LD      A,($18)         
6005: 54         LD      D,H             
6006: 00         NOP                     
6007: F0 20      LD      A,($20)         
6009: 56         LD      D,(HL)          
600A: 00         NOP                     
600B: F0 28      LD      A,($28)         
600D: 58         LD      E,B             
600E: 00         NOP                     
600F: 00         NOP                     
6010: 00         NOP                     
6011: 40         LD      B,B             
6012: 00         NOP                     
6013: 00         NOP                     
6014: 08 42 00   LD      ($0042),SP      
6017: 00         NOP                     
6018: 10 5A      STOP    $5A             
601A: 00         NOP                     
601B: 00         NOP                     
601C: 18 68      JR      $6086           
601E: 00         NOP                     
601F: 00         NOP                     
6020: 20 6A      JR      NZ,$608C        
6022: 00         NOP                     
6023: 10 08      STOP    $08             
6025: 60         LD      H,B             
6026: 00         NOP                     
6027: 10 10      STOP    $10             
6029: 62         LD      H,D             
602A: 00         NOP                     
602B: 10 18      STOP    $18             
602D: 64         LD      H,H             
602E: 00         NOP                     
602F: 10 20      STOP    $20             
6031: 66         LD      H,(HL)          
6032: 00         NOP                     
6033: FF         RST     0X38            
6034: FF         RST     0X38            
6035: FF         RST     0X38            
6036: FF         RST     0X38            
6037: FF         RST     0X38            
6038: FF         RST     0X38            
6039: FF         RST     0X38            
603A: FF         RST     0X38            
603B: FF         RST     0X38            
603C: FF         RST     0X38            
603D: FF         RST     0X38            
603E: FF         RST     0X38            
603F: 00         NOP                     
6040: 00         NOP                     
6041: 40         LD      B,B             
6042: 00         NOP                     
6043: 00         NOP                     
6044: 08 42 00   LD      ($0042),SP      
6047: 00         NOP                     
6048: 10 6C      STOP    $6C             
604A: 00         NOP                     
604B: 00         NOP                     
604C: 18 6E      JR      $60BC           
604E: 00         NOP                     
604F: 00         NOP                     
6050: 20 70      JR      NZ,$60C2        
6052: 00         NOP                     
6053: 10 08      STOP    $08             
6055: 60         LD      H,B             
6056: 00         NOP                     
6057: 10 10      STOP    $10             
6059: 72         LD      (HL),D          
605A: 00         NOP                     
605B: 10 18      STOP    $18             
605D: 74         LD      (HL),H          
605E: 00         NOP                     
605F: 10 20      STOP    $20             
6061: 76         HALT                    
6062: 00         NOP                     
6063: FF         RST     0X38            
6064: FF         RST     0X38            
6065: FF         RST     0X38            
6066: FF         RST     0X38            
6067: FF         RST     0X38            
6068: FF         RST     0X38            
6069: FF         RST     0X38            
606A: FF         RST     0X38            
606B: FF         RST     0X38            
606C: FF         RST     0X38            
606D: FF         RST     0X38            
606E: FF         RST     0X38            
606F: 00         NOP                     
6070: 08 40 20   LD      ($2040),SP      
6073: 00         NOP                     
6074: 00         NOP                     
6075: 42         LD      B,D             
6076: 20 00      JR      NZ,$6078        
6078: F8 44      LDHL    SP,$44          
607A: 20 F8      JR      NZ,$6074        
607C: F0 46      LD      A,($46)         
607E: 20 F8      JR      NZ,$6078        
6080: E8 48      ADD     SP,$48          
6082: 20 F8      JR      NZ,$607C        
6084: E0 4A      LDFF00  ($4A),A         
6086: 20 08      JR      NZ,$6090        
6088: F0 4C      LD      A,($4C)         
608A: 20 08      JR      NZ,$6094        
608C: E8 4E      ADD     SP,$4E          
608E: 20 08      JR      NZ,$6098        
6090: E0 50      LDFF00  ($50),A         
6092: 20 00      JR      NZ,$6094        
6094: D8         RET     C               
6095: 52         LD      D,D             
6096: 20 FF      JR      NZ,$6097        
6098: FF         RST     0X38            
6099: FF         RST     0X38            
609A: FF         RST     0X38            
609B: FF         RST     0X38            
609C: FF         RST     0X38            
609D: FF         RST     0X38            
609E: FF         RST     0X38            
609F: 00         NOP                     
60A0: 08 40 20   LD      ($2040),SP      
60A3: 00         NOP                     
60A4: 00         NOP                     
60A5: 42         LD      B,D             
60A6: 20 00      JR      NZ,$60A8        
60A8: F8 5A      LDHL    SP,$5A          
60AA: 20 00      JR      NZ,$60AC        
60AC: F0 5C      LD      A,($5C)         
60AE: 20 00      JR      NZ,$60B0        
60B0: E8 5E      ADD     SP,$5E          
60B2: 20 10      JR      NZ,$60C4        
60B4: 00         NOP                     
60B5: 60         LD      H,B             
60B6: 20 10      JR      NZ,$60C8        
60B8: F8 62      LDHL    SP,$62          
60BA: 20 10      JR      NZ,$60CC        
60BC: F0 64      LD      A,($64)         
60BE: 20 10      JR      NZ,$60D0        
60C0: E8 66      ADD     SP,$66          
60C2: 20 F0      JR      NZ,$60B4        
60C4: F0 54      LD      A,($54)         
60C6: 20 F0      JR      NZ,$60B8        
60C8: E8 56      ADD     SP,$56          
60CA: 20 F0      JR      NZ,$60BC        
60CC: E0 58      LDFF00  ($58),A         
60CE: 20 00      JR      NZ,$60D0        
60D0: 08 40 20   LD      ($2040),SP      
60D3: 00         NOP                     
60D4: 00         NOP                     
60D5: 42         LD      B,D             
60D6: 20 00      JR      NZ,$60D8        
60D8: F8 5A      LDHL    SP,$5A          
60DA: 20 00      JR      NZ,$60DC        
60DC: F0 68      LD      A,($68)         
60DE: 20 00      JR      NZ,$60E0        
60E0: E8 6A      ADD     SP,$6A          
60E2: 20 10      JR      NZ,$60F4        
60E4: 00         NOP                     
60E5: 60         LD      H,B             
60E6: 20 10      JR      NZ,$60F8        
60E8: F8 62      LDHL    SP,$62          
60EA: 20 10      JR      NZ,$60FC        
60EC: F0 64      LD      A,($64)         
60EE: 20 10      JR      NZ,$6100        
60F0: E8 66      ADD     SP,$66          
60F2: 20 FF      JR      NZ,$60F3        
60F4: FF         RST     0X38            
60F5: FF         RST     0X38            
60F6: FF         RST     0X38            
60F7: FF         RST     0X38            
60F8: FF         RST     0X38            
60F9: FF         RST     0X38            
60FA: FF         RST     0X38            
60FB: FF         RST     0X38            
60FC: FF         RST     0X38            
60FD: FF         RST     0X38            
60FE: FF         RST     0X38            
60FF: 00         NOP                     
6100: 08 40 20   LD      ($2040),SP      
6103: 00         NOP                     
6104: 00         NOP                     
6105: 42         LD      B,D             
6106: 20 00      JR      NZ,$6108        
6108: F8 6C      LDHL    SP,$6C          
610A: 20 00      JR      NZ,$610C        
610C: F0 6E      LD      A,($6E)         
610E: 20 00      JR      NZ,$6110        
6110: E8 70      ADD     SP,$70          
6112: 20 10      JR      NZ,$6124        
6114: 00         NOP                     
6115: 60         LD      H,B             
6116: 20 10      JR      NZ,$6128        
6118: F8 72      LDHL    SP,$72          
611A: 20 10      JR      NZ,$612C        
611C: F0 74      LD      A,($74)         
611E: 20 10      JR      NZ,$6130        
6120: E8 76      ADD     SP,$76          
6122: 20 FF      JR      NZ,$6123        
6124: FF         RST     0X38            
6125: FF         RST     0X38            
6126: FF         RST     0X38            
6127: FF         RST     0X38            
6128: FF         RST     0X38            
6129: FF         RST     0X38            
612A: FF         RST     0X38            
612B: FF         RST     0X38            
612C: FF         RST     0X38            
612D: FF         RST     0X38            
612E: FF         RST     0X38            
612F: 1C         INC     E               
6130: 1C         INC     E               
6131: 08 0C 14   LD      ($140C),SP      
6134: 10 10      STOP    $10             
6136: 10 F4      STOP    $F4             
6138: 1C         INC     E               
6139: 08 0C FC   LD      ($FC0C),SP      
613C: 10 10      STOP    $10             
613E: 10 21      STOP    $21             
6140: 80         ADD     A,B             
6141: C3 09 F0   JP      $F009           
6144: F1         POP     AF              
6145: 86         ADD     A,(HL)          
6146: 21 AF 5F   LD      HL,$5FAF        
6149: FE 04      CP      $04             
614B: 38 05      JR      C,$6152         
614D: D6 04      SUB     $04             
614F: 21 6F 60   LD      HL,$606F        
6152: 5F         LD      E,A             
6153: 50         LD      D,B             
6154: CB 23      SET     1,E             
6156: CB 23      SET     1,E             
6158: CB 23      SET     1,E             
615A: CB 23      SET     1,E             
615C: 7B         LD      A,E             
615D: CB 23      SET     1,E             
615F: 83         ADD     A,E             
6160: 5F         LD      E,A             
6161: 19         ADD     HL,DE           
6162: 0E 0C      LD      C,$0C           
6164: CD 26 3D   CALL    $3D26           
6167: 3E 0A      LD      A,$0A           
6169: CD D0 3D   CALL    $3DD0           
616C: 1E 00      LD      E,$00           
616E: F0 F1      LD      A,($F1)         
6170: A7         AND     A               
6171: 28 02      JR      Z,$6175         
6173: 1E 04      LD      E,$04           
6175: 21 80 C3   LD      HL,$C380        
6178: 09         ADD     HL,BC           
6179: 7E         LD      A,(HL)          
617A: A7         AND     A               
617B: 28 04      JR      Z,$6181         
617D: 7B         LD      A,E             
617E: C6 08      ADD     $08             
6180: 5F         LD      E,A             
6181: 50         LD      D,B             
6182: 21 2F 61   LD      HL,$612F        
6185: 19         ADD     HL,DE           
6186: E5         PUSH    HL              
6187: D1         POP     DE              
6188: C5         PUSH    BC              
6189: CB 21      SET     1,E             
618B: CB 21      SET     1,E             
618D: 21 80 D5   LD      HL,$D580        
6190: 09         ADD     HL,BC           
6191: 0E 04      LD      C,$04           
6193: 1A         LD      A,(DE)          
6194: 13         INC     DE              
6195: 22         LD      (HLI),A         
6196: 0D         DEC     C               
6197: 20 FA      JR      NZ,$6193        
6199: C1         POP     BC              
619A: C9         RET                     
619B: 7C         LD      A,H             
619C: 00         NOP                     
619D: 7C         LD      A,H             
619E: 20 7C      JR      NZ,$621C        
61A0: 40         LD      B,B             
61A1: 7C         LD      A,H             
61A2: 60         LD      H,B             
61A3: 3E 02      LD      A,$02           
61A5: E0 A1      LDFF00  ($A1),A         
61A7: 11 9B 61   LD      DE,$619B        
61AA: CD 3B 3C   CALL    $3C3B           
61AD: CD 65 79   CALL    $7965           
61B0: F0 E7      LD      A,($E7)         
61B2: 1F         RRA                     
61B3: 1F         RRA                     
61B4: 1F         RRA                     
61B5: E6 01      AND     $01             
61B7: CD 87 3B   CALL    $3B87           
61BA: F0 F0      LD      A,($F0)         
61BC: C7         RST     0X00            
61BD: C1         POP     BC              
61BE: 61         LD      H,C             
61BF: E6 61      AND     $61             
61C1: 21 10 C2   LD      HL,$C210        
61C4: 09         ADD     HL,BC           
61C5: 1E 07      LD      E,$07           
61C7: CD D0 61   CALL    $61D0           
61CA: 21 00 C2   LD      HL,$C200        
61CD: 09         ADD     HL,BC           
61CE: 1E 00      LD      E,$00           
61D0: F0 E7      LD      A,($E7)         
61D2: 83         ADD     A,E             
61D3: 57         LD      D,A             
61D4: E6 03      AND     $03             
61D6: 20 0D      JR      NZ,$61E5        
61D8: 7A         LD      A,D             
61D9: 1F         RRA                     
61DA: 1F         RRA                     
61DB: 1F         RRA                     
61DC: 1F         RRA                     
61DD: A9         XOR     C               
61DE: E6 01      AND     $01             
61E0: 28 02      JR      Z,$61E4         
61E2: 34         INC     (HL)            
61E3: 34         INC     (HL)            
61E4: 35         DEC     (HL)            
61E5: C9         RET                     
61E6: CD D1 79   CALL    $79D1           
61E9: 21 40 C2   LD      HL,$C240        
61EC: 09         ADD     HL,BC           
61ED: 7E         LD      A,(HL)          
61EE: FE C0      CP      $C0             
61F0: 28 01      JR      Z,$61F3         
61F2: 35         DEC     (HL)            
61F3: 21 50 C2   LD      HL,$C250        
61F6: 09         ADD     HL,BC           
61F7: 7E         LD      A,(HL)          
61F8: FE F0      CP      $F0             
61FA: 28 01      JR      Z,$61FD         
61FC: 35         DEC     (HL)            
61FD: F0 EE      LD      A,($EE)         
61FF: FE E0      CP      $E0             
6201: D2 6B 7A   JP      NC,$7A6B        
6204: C9         RET                     
6205: 7A         LD      A,D             
6206: 20 78      JR      NZ,$6280        
6208: 20 78      JR      NZ,$6282        
620A: 00         NOP                     
620B: 7A         LD      A,D             
620C: 00         NOP                     
620D: 7A         LD      A,D             
620E: 60         LD      H,B             
620F: 78         LD      A,B             
6210: 60         LD      H,B             
6211: 78         LD      A,B             
6212: 40         LD      B,B             
6213: 7A         LD      A,D             
6214: 40         LD      B,B             
6215: 11 05 62   LD      DE,$6205        
6218: CD 3B 3C   CALL    $3C3B           
621B: CD 65 79   CALL    $7965           
621E: CD D1 79   CALL    $79D1           
6221: F0 F0      LD      A,($F0)         
6223: C7         RST     0X00            
6224: 28 62      JR      Z,$6288         
6226: 47         LD      B,A             
6227: 62         LD      H,D             
6228: CD CA 3B   CALL    $3BCA           
622B: 21 A0 C2   LD      HL,$C2A0        
622E: 09         ADD     HL,BC           
622F: 7E         LD      A,(HL)          
6230: A7         AND     A               
6231: 28 0F      JR      Z,$6242         
6233: CD 8D 3B   CALL    $3B8D           
6236: 21 50 C2   LD      HL,$C250        
6239: 09         ADD     HL,BC           
623A: 36 E0      LD      (HL),$E0        
623C: 21 B0 C3   LD      HL,$C3B0        
623F: 09         ADD     HL,BC           
6240: 34         INC     (HL)            
6241: 34         INC     (HL)            
6242: 21 50 C2   LD      HL,$C250        
6245: 09         ADD     HL,BC           
6246: 35         DEC     (HL)            
6247: F0 EE      LD      A,($EE)         
6249: FE A8      CP      $A8             
624B: D2 6B 7A   JP      NC,$7A6B        
624E: C9         RET                     
624F: CD 91 08   CALL    $0891           
6252: 36 40      LD      (HL),$40        
6254: 21 B0 C3   LD      HL,$C3B0        
6257: 09         ADD     HL,BC           
6258: 36 FF      LD      (HL),$FF        
625A: 21 60 C3   LD      HL,$C360        
625D: 09         ADD     HL,BC           
625E: 36 FF      LD      (HL),$FF        
6260: C9         RET                     
6261: CD 0E 38   CALL    $380E           
6264: CD 12 3F   CALL    $3F12           
6267: 21 B0 C2   LD      HL,$C2B0        
626A: 09         ADD     HL,BC           
626B: 7E         LD      A,(HL)          
626C: A7         AND     A               
626D: 28 0D      JR      Z,$627C         
626F: FE 01      CP      $01             
6271: CA CF 66   JP      Z,$66CF         
6274: FE 02      CP      $02             
6276: CA F2 66   JP      Z,$66F2         
6279: C3 46 67   JP      $6746           
627C: CD 5A 66   CALL    $665A           
627F: F0 EA      LD      A,($EA)         
6281: FE 01      CP      $01             
6283: 20 3F      JR      NZ,$62C4        
6285: 21 C0 C2   LD      HL,$C2C0        
6288: 09         ADD     HL,BC           
6289: 7E         LD      A,(HL)          
628A: C7         RST     0X00            
628B: 8F         ADC     A,A             
628C: 62         LD      H,D             
628D: 9A         SBC     D               
628E: 62         LD      H,D             
628F: CD 91 08   CALL    $0891           
6292: 36 FF      LD      (HL),$FF        
6294: 21 C0 C2   LD      HL,$C2C0        
6297: 09         ADD     HL,BC           
6298: 34         INC     (HL)            
6299: C9         RET                     
629A: CD 91 08   CALL    $0891           
629D: CA AD 62   JP      Z,$62AD         
62A0: 21 20 C4   LD      HL,$C420        
62A3: 09         ADD     HL,BC           
62A4: 77         LD      (HL),A          
62A5: FE 80      CP      $80             
62A7: 30 03      JR      NC,$62AC        
62A9: CD 76 74   CALL    $7476           
62AC: C9         RET                     
62AD: CD AD 74   CALL    $74AD           
62B0: 21 00 C2   LD      HL,$C200        
62B3: 19         ADD     HL,DE           
62B4: F0 98      LD      A,($98)         
62B6: 77         LD      (HL),A          
62B7: 21 10 C2   LD      HL,$C210        
62BA: 19         ADD     HL,DE           
62BB: 36 70      LD      (HL),$70        
62BD: 21 10 C3   LD      HL,$C310        
62C0: 19         ADD     HL,DE           
62C1: 36 70      LD      (HL),$70        
62C3: C9         RET                     
62C4: CD 65 79   CALL    $7965           
62C7: CD E2 08   CALL    $08E2           
62CA: F0 F0      LD      A,($F0)         
62CC: C7         RST     0X00            
62CD: F7         RST     0X30            
62CE: 62         LD      H,D             
62CF: 3C         INC     A               
62D0: 63         LD      H,E             
62D1: DF         RST     0X18            
62D2: 63         LD      H,E             
62D3: 88         ADC     A,B             
62D4: 64         LD      H,H             
62D5: CE 64      ADC     $64             
62D7: 28 38      JR      Z,$6311         
62D9: 58         LD      E,B             
62DA: 68         LD      L,B             
62DB: 28 38      JR      Z,$6315         
62DD: 58         LD      E,B             
62DE: 68         LD      L,B             
62DF: 38 30      JR      C,$6311         
62E1: 30 38      JR      NC,$631B        
62E3: 50         LD      D,B             
62E4: 58         LD      E,B             
62E5: 58         LD      E,B             
62E6: 50         LD      D,B             
62E7: 10 10      STOP    $10             
62E9: F0 F0      LD      A,($F0)         
62EB: 10 10      STOP    $10             
62ED: F0 F0      LD      A,($F0)         
62EF: FD         ???                     
62F0: 03         INC     BC              
62F1: 03         INC     BC              
62F2: FD         ???                     
62F3: 03         INC     BC              
62F4: FD         ???                     
62F5: FD         ???                     
62F6: 03         INC     BC              
62F7: CD 91 08   CALL    $0891           
62FA: 20 3F      JR      NZ,$633B        
62FC: CD ED 27   CALL    $27ED           
62FF: E6 07      AND     $07             
6301: 5F         LD      E,A             
6302: 50         LD      D,B             
6303: 21 D7 62   LD      HL,$62D7        
6306: 19         ADD     HL,DE           
6307: 7E         LD      A,(HL)          
6308: 21 00 C2   LD      HL,$C200        
630B: 09         ADD     HL,BC           
630C: 77         LD      (HL),A          
630D: 21 DF 62   LD      HL,$62DF        
6310: 19         ADD     HL,DE           
6311: 7E         LD      A,(HL)          
6312: 21 10 C2   LD      HL,$C210        
6315: 09         ADD     HL,BC           
6316: 77         LD      (HL),A          
6317: 21 E7 62   LD      HL,$62E7        
631A: 19         ADD     HL,DE           
631B: 7E         LD      A,(HL)          
631C: 21 40 C2   LD      HL,$C240        
631F: 09         ADD     HL,BC           
6320: 77         LD      (HL),A          
6321: 21 EF 62   LD      HL,$62EF        
6324: 19         ADD     HL,DE           
6325: 7E         LD      A,(HL)          
6326: 21 50 C2   LD      HL,$C250        
6329: 09         ADD     HL,BC           
632A: 77         LD      (HL),A          
632B: 21 20 C3   LD      HL,$C320        
632E: 09         ADD     HL,BC           
632F: 36 18      LD      (HL),$18        
6331: 3E 16      LD      A,$16           
6333: E0 F3      LDFF00  ($F3),A         
6335: CD 2E 65   CALL    $652E           
6338: CD 8D 3B   CALL    $3B8D           
633B: C9         RET                     
633C: 21 40 C2   LD      HL,$C240        
633F: 09         ADD     HL,BC           
6340: 7E         LD      A,(HL)          
6341: A7         AND     A               
6342: 28 51      JR      Z,$6395         
6344: 21 20 C4   LD      HL,$C420        
6347: 09         ADD     HL,BC           
6348: 7E         LD      A,(HL)          
6349: FE 0B      CP      $0B             
634B: 38 48      JR      C,$6395         
634D: 21 D0 C3   LD      HL,$C3D0        
6350: 09         ADD     HL,BC           
6351: 7E         LD      A,(HL)          
6352: FE 05      CP      $05             
6354: 30 3E      JR      NC,$6394        
6356: CD 8D 3B   CALL    $3B8D           
6359: CD 91 08   CALL    $0891           
635C: 36 40      LD      (HL),$40        
635E: 21 40 C2   LD      HL,$C240        
6361: 09         ADD     HL,BC           
6362: 36 18      LD      (HL),$18        
6364: 21 50 C2   LD      HL,$C250        
6367: 09         ADD     HL,BC           
6368: 36 18      LD      (HL),$18        
636A: 21 20 C3   LD      HL,$C320        
636D: 09         ADD     HL,BC           
636E: 70         LD      (HL),B          
636F: CD 87 08   CALL    $0887           
6372: 36 40      LD      (HL),$40        
6374: F0 EE      LD      A,($EE)         
6376: C6 F8      ADD     $F8             
6378: E0 D7      LDFF00  ($D7),A         
637A: CD 83 63   CALL    $6383           
637D: F0 EE      LD      A,($EE)         
637F: C6 08      ADD     $08             
6381: E0 D7      LDFF00  ($D7),A         
6383: F0 EC      LD      A,($EC)         
6385: D6 10      SUB     $10             
6387: E0 D8      LDFF00  ($D8),A         
6389: 3E 02      LD      A,$02           
638B: CD 53 09   CALL    $0953           
638E: 21 20 C5   LD      HL,$C520        
6391: 19         ADD     HL,DE           
6392: 36 0F      LD      (HL),$0F        
6394: C9         RET                     
6395: CD D1 79   CALL    $79D1           
6398: CD 0A 7A   CALL    $7A0A           
639B: 21 20 C3   LD      HL,$C320        
639E: 09         ADD     HL,BC           
639F: 35         DEC     (HL)            
63A0: 21 10 C3   LD      HL,$C310        
63A3: 09         ADD     HL,BC           
63A4: 7E         LD      A,(HL)          
63A5: E6 80      AND     $80             
63A7: 28 19      JR      Z,$63C2         
63A9: 70         LD      (HL),B          
63AA: CD 91 08   CALL    $0891           
63AD: 36 40      LD      (HL),$40        
63AF: CD 8D 3B   CALL    $3B8D           
63B2: 70         LD      (HL),B          
63B3: CD 66 65   CALL    $6566           
63B6: CD 2E 65   CALL    $652E           
63B9: 3E 32      LD      A,$32           
63BB: E0 F2      LDFF00  ($F2),A         
63BD: 3E FF      LD      A,$FF           
63BF: C3 87 3B   JP      $3B87           
63C2: 21 D0 C3   LD      HL,$C3D0        
63C5: 09         ADD     HL,BC           
63C6: 7E         LD      A,(HL)          
63C7: FE 05      CP      $05             
63C9: D2 C1 64   JP      NC,$64C1        
63CC: 21 40 C2   LD      HL,$C240        
63CF: 09         ADD     HL,BC           
63D0: 7E         LD      A,(HL)          
63D1: A7         AND     A               
63D2: 28 0A      JR      Z,$63DE         
63D4: F0 E7      LD      A,($E7)         
63D6: 1F         RRA                     
63D7: 1F         RRA                     
63D8: 1F         RRA                     
63D9: E6 01      AND     $01             
63DB: C3 87 3B   JP      $3B87           
63DE: C9         RET                     
63DF: 3E 02      LD      A,$02           
63E1: CD 87 3B   CALL    $3B87           
63E4: CD 91 08   CALL    $0891           
63E7: 28 17      JR      Z,$6400         
63E9: E6 02      AND     $02             
63EB: 1E 08      LD      E,$08           
63ED: 28 02      JR      Z,$63F1         
63EF: 1E F8      LD      E,$F8           
63F1: 21 40 C2   LD      HL,$C240        
63F4: 09         ADD     HL,BC           
63F5: E5         PUSH    HL              
63F6: 7E         LD      A,(HL)          
63F7: F5         PUSH    AF              
63F8: 73         LD      (HL),E          
63F9: CD DE 79   CALL    $79DE           
63FC: F1         POP     AF              
63FD: E1         POP     HL              
63FE: 77         LD      (HL),A          
63FF: C9         RET                     
6400: CD B4 3B   CALL    $3BB4           
6403: CD 87 08   CALL    $0887           
6406: 20 15      JR      NZ,$641D        
6408: F0 EE      LD      A,($EE)         
640A: FE 70      CP      $70             
640C: 30 0F      JR      NC,$641D        
640E: F0 EC      LD      A,($EC)         
6410: FE 50      CP      $50             
6412: 30 09      JR      NC,$641D        
6414: CD AF 3D   CALL    $3DAF           
6417: CD 8D 3B   CALL    $3B8D           
641A: 36 01      LD      (HL),$01        
641C: C9         RET                     
641D: 21 20 C4   LD      HL,$C420        
6420: 09         ADD     HL,BC           
6421: 7E         LD      A,(HL)          
6422: FE 08      CP      $08             
6424: 20 22      JR      NZ,$6448        
6426: F0 EE      LD      A,($EE)         
6428: FE 70      CP      $70             
642A: 30 1C      JR      NC,$6448        
642C: F0 EC      LD      A,($EC)         
642E: FE 50      CP      $50             
6430: 30 16      JR      NC,$6448        
6432: 21 D0 C3   LD      HL,$C3D0        
6435: 09         ADD     HL,BC           
6436: 34         INC     (HL)            
6437: 7E         LD      A,(HL)          
6438: FE 05      CP      $05             
643A: 38 0C      JR      C,$6448         
643C: CD 8D 3B   CALL    $3B8D           
643F: CD AF 3D   CALL    $3DAF           
6442: CD 91 08   CALL    $0891           
6445: 36 80      LD      (HL),$80        
6447: C9         RET                     
6448: 21 20 C4   LD      HL,$C420        
644B: 09         ADD     HL,BC           
644C: 7E         LD      A,(HL)          
644D: FE 0B      CP      $0B             
644F: 30 36      JR      NC,$6487        
6451: CD D1 79   CALL    $79D1           
6454: CD 9E 3B   CALL    $3B9E           
6457: 21 A0 C2   LD      HL,$C2A0        
645A: 09         ADD     HL,BC           
645B: 7E         LD      A,(HL)          
645C: F5         PUSH    AF              
645D: E6 03      AND     $03             
645F: 28 06      JR      Z,$6467         
6461: 21 40 C2   LD      HL,$C240        
6464: CD 6F 64   CALL    $646F           
6467: F1         POP     AF              
6468: E6 0C      AND     $0C             
646A: 28 08      JR      Z,$6474         
646C: 21 50 C2   LD      HL,$C250        
646F: 09         ADD     HL,BC           
6470: 7E         LD      A,(HL)          
6471: 2F         CPL                     
6472: 3C         INC     A               
6473: 77         LD      (HL),A          
6474: F0 E7      LD      A,($E7)         
6476: E6 07      AND     $07             
6478: 20 0D      JR      NZ,$6487        
647A: F0 EE      LD      A,($EE)         
647C: E0 D7      LDFF00  ($D7),A         
647E: F0 EC      LD      A,($EC)         
6480: E0 D8      LDFF00  ($D8),A         
6482: 3E 0A      LD      A,$0A           
6484: CD 53 09   CALL    $0953           
6487: C9         RET                     
6488: CD 91 08   CALL    $0891           
648B: FE 40      CP      $40             
648D: 38 20      JR      C,$64AF         
648F: 20 07      JR      NZ,$6498        
6491: 3E 29      LD      A,$29           
6493: E0 F4      LDFF00  ($F4),A         
6495: CD D4 64   CALL    $64D4           
6498: E6 02      AND     $02             
649A: 1E 10      LD      E,$10           
649C: 28 02      JR      Z,$64A0         
649E: 1E F0      LD      E,$F0           
64A0: 21 40 C2   LD      HL,$C240        
64A3: 09         ADD     HL,BC           
64A4: E5         PUSH    HL              
64A5: 7E         LD      A,(HL)          
64A6: F5         PUSH    AF              
64A7: 73         LD      (HL),E          
64A8: CD DE 79   CALL    $79DE           
64AB: F1         POP     AF              
64AC: E1         POP     HL              
64AD: 77         LD      (HL),A          
64AE: C9         RET                     
64AF: A7         AND     A               
64B0: 20 0F      JR      NZ,$64C1        
64B2: CD 8D 3B   CALL    $3B8D           
64B5: 36 01      LD      (HL),$01        
64B7: CD AF 3D   CALL    $3DAF           
64BA: 21 60 C3   LD      HL,$C360        
64BD: 09         ADD     HL,BC           
64BE: 36 08      LD      (HL),$08        
64C0: C9         RET                     
64C1: F0 E7      LD      A,($E7)         
64C3: 1F         RRA                     
64C4: 1F         RRA                     
64C5: 1F         RRA                     
64C6: E6 01      AND     $01             
64C8: C6 03      ADD     $03             
64CA: CD 87 3B   CALL    $3B87           
64CD: C9         RET                     
64CE: C9         RET                     
64CF: C9         RET                     
64D0: F8 08      LDHL    SP,$08          
64D2: F8 08      LDHL    SP,$08          
64D4: 3E 02      LD      A,$02           
64D6: E0 E8      LDFF00  ($E8),A         
64D8: 3E 62      LD      A,$62           
64DA: CD 01 3C   CALL    $3C01           
64DD: 38 49      JR      C,$6528         
64DF: 21 B0 C2   LD      HL,$C2B0        
64E2: 19         ADD     HL,DE           
64E3: 36 03      LD      (HL),$03        
64E5: C5         PUSH    BC              
64E6: F0 E8      LD      A,($E8)         
64E8: 4F         LD      C,A             
64E9: 21 CF 64   LD      HL,$64CF        
64EC: 09         ADD     HL,BC           
64ED: F0 D7      LD      A,($D7)         
64EF: 86         ADD     A,(HL)          
64F0: 21 00 C2   LD      HL,$C200        
64F3: 19         ADD     HL,DE           
64F4: 77         LD      (HL),A          
64F5: F0 D8      LD      A,($D8)         
64F7: 21 10 C2   LD      HL,$C210        
64FA: 19         ADD     HL,DE           
64FB: 77         LD      (HL),A          
64FC: F0 DA      LD      A,($DA)         
64FE: 21 10 C3   LD      HL,$C310        
6501: 19         ADD     HL,DE           
6502: 77         LD      (HL),A          
6503: 21 B0 C3   LD      HL,$C3B0        
6506: 19         ADD     HL,DE           
6507: F0 E8      LD      A,($E8)         
6509: 3D         DEC     A               
650A: 77         LD      (HL),A          
650B: 21 D1 64   LD      HL,$64D1        
650E: 09         ADD     HL,BC           
650F: 7E         LD      A,(HL)          
6510: 21 40 C2   LD      HL,$C240        
6513: 19         ADD     HL,DE           
6514: 77         LD      (HL),A          
6515: 21 50 C2   LD      HL,$C250        
6518: 19         ADD     HL,DE           
6519: 36 04      LD      (HL),$04        
651B: C1         POP     BC              
651C: 21 20 C3   LD      HL,$C320        
651F: 19         ADD     HL,DE           
6520: 36 08      LD      (HL),$08        
6522: 21 40 C3   LD      HL,$C340        
6525: 19         ADD     HL,DE           
6526: 36 42      LD      (HL),$42        
6528: F0 E8      LD      A,($E8)         
652A: 3D         DEC     A               
652B: 20 A9      JR      NZ,$64D6        
652D: C9         RET                     
652E: 3E 62      LD      A,$62           
6530: CD 01 3C   CALL    $3C01           
6533: 38 20      JR      C,$6555         
6535: 21 B0 C2   LD      HL,$C2B0        
6538: 19         ADD     HL,DE           
6539: 36 01      LD      (HL),$01        
653B: F0 D7      LD      A,($D7)         
653D: 21 00 C2   LD      HL,$C200        
6540: 19         ADD     HL,DE           
6541: 77         LD      (HL),A          
6542: F0 D8      LD      A,($D8)         
6544: 21 10 C2   LD      HL,$C210        
6547: 19         ADD     HL,DE           
6548: 77         LD      (HL),A          
6549: 21 E0 C2   LD      HL,$C2E0        
654C: 19         ADD     HL,DE           
654D: 36 14      LD      (HL),$14        
654F: 21 40 C3   LD      HL,$C340        
6552: 19         ADD     HL,DE           
6553: 36 C4      LD      (HL),$C4        
6555: C9         RET                     
6556: F8 08      LDHL    SP,$08          
6558: F8 08      LDHL    SP,$08          
655A: FC         ???                     
655B: FC         ???                     
655C: 04         INC     B               
655D: 04         INC     B               
655E: F4         ???                     
655F: 0C         INC     C               
6560: F4         ???                     
6561: 0C         INC     C               
6562: F4         ???                     
6563: F4         ???                     
6564: 0C         INC     C               
6565: 0C         INC     C               
6566: 3E 04      LD      A,$04           
6568: E0 E8      LDFF00  ($E8),A         
656A: 3E 62      LD      A,$62           
656C: CD 01 3C   CALL    $3C01           
656F: 38 43      JR      C,$65B4         
6571: 21 B0 C2   LD      HL,$C2B0        
6574: 19         ADD     HL,DE           
6575: 36 02      LD      (HL),$02        
6577: C5         PUSH    BC              
6578: F0 E8      LD      A,($E8)         
657A: 4F         LD      C,A             
657B: 21 55 65   LD      HL,$6555        
657E: 09         ADD     HL,BC           
657F: F0 D7      LD      A,($D7)         
6581: 86         ADD     A,(HL)          
6582: 21 00 C2   LD      HL,$C200        
6585: 19         ADD     HL,DE           
6586: 77         LD      (HL),A          
6587: 21 59 65   LD      HL,$6559        
658A: 09         ADD     HL,BC           
658B: F0 D8      LD      A,($D8)         
658D: 86         ADD     A,(HL)          
658E: 21 10 C2   LD      HL,$C210        
6591: 19         ADD     HL,DE           
6592: 77         LD      (HL),A          
6593: 21 5D 65   LD      HL,$655D        
6596: 09         ADD     HL,BC           
6597: 7E         LD      A,(HL)          
6598: 21 40 C2   LD      HL,$C240        
659B: 19         ADD     HL,DE           
659C: 77         LD      (HL),A          
659D: 21 61 65   LD      HL,$6561        
65A0: 09         ADD     HL,BC           
65A1: 7E         LD      A,(HL)          
65A2: 21 50 C2   LD      HL,$C250        
65A5: 19         ADD     HL,DE           
65A6: 77         LD      (HL),A          
65A7: C1         POP     BC              
65A8: 21 20 C3   LD      HL,$C320        
65AB: 19         ADD     HL,DE           
65AC: 36 13      LD      (HL),$13        
65AE: 21 40 C3   LD      HL,$C340        
65B1: 19         ADD     HL,DE           
65B2: 36 42      LD      (HL),$42        
65B4: F0 E8      LD      A,($E8)         
65B6: 3D         DEC     A               
65B7: 20 AF      JR      NZ,$6568        
65B9: C9         RET                     
65BA: F0 F8      LD      A,($F8)         
65BC: 60         LD      H,B             
65BD: 00         NOP                     
65BE: F0 00      LD      A,($00)         
65C0: 62         LD      H,D             
65C1: 00         NOP                     
65C2: F0 08      LD      A,($08)         
65C4: 64         LD      H,H             
65C5: 00         NOP                     
65C6: F0 10      LD      A,($10)         
65C8: 66         LD      H,(HL)          
65C9: 00         NOP                     
65CA: 00         NOP                     
65CB: F8 68      LDHL    SP,$68          
65CD: 00         NOP                     
65CE: 00         NOP                     
65CF: 00         NOP                     
65D0: 6A         LD      L,D             
65D1: 00         NOP                     
65D2: 00         NOP                     
65D3: 08 6A 20   LD      ($206A),SP      
65D6: 00         NOP                     
65D7: 10 68      STOP    $68             
65D9: 20 F0      JR      NZ,$65CB        
65DB: F8 66      LDHL    SP,$66          
65DD: 20 F0      JR      NZ,$65CF        
65DF: 00         NOP                     
65E0: 64         LD      H,H             
65E1: 20 F0      JR      NZ,$65D3        
65E3: 08 62 20   LD      ($2062),SP      
65E6: F0 10      LD      A,($10)         
65E8: 60         LD      H,B             
65E9: 20 00      JR      NZ,$65EB        
65EB: F8 68      LDHL    SP,$68          
65ED: 00         NOP                     
65EE: 00         NOP                     
65EF: 00         NOP                     
65F0: 6A         LD      L,D             
65F1: 00         NOP                     
65F2: 00         NOP                     
65F3: 08 6A 20   LD      ($206A),SP      
65F6: 00         NOP                     
65F7: 10 68      STOP    $68             
65F9: 20 00      JR      NZ,$65FB        
65FB: F8 6C      LDHL    SP,$6C          
65FD: 00         NOP                     
65FE: 00         NOP                     
65FF: 00         NOP                     
6600: 6E         LD      L,(HL)          
6601: 00         NOP                     
6602: 00         NOP                     
6603: 08 6E 20   LD      ($206E),SP      
6606: 00         NOP                     
6607: 10 6C      STOP    $6C             
6609: 20 00      JR      NZ,$660B        
660B: FC         ???                     
660C: 7C         LD      A,H             
660D: 00         NOP                     
660E: 00         NOP                     
660F: 04         INC     B               
6610: 7E         LD      A,(HL)          
6611: 00         NOP                     
6612: 00         NOP                     
6613: 0C         INC     C               
6614: 7C         LD      A,H             
6615: 20 00      JR      NZ,$6617        
6617: 00         NOP                     
6618: FF         RST     0X38            
6619: 00         NOP                     
661A: 00         NOP                     
661B: FC         ???                     
661C: 7C         LD      A,H             
661D: 00         NOP                     
661E: 00         NOP                     
661F: 04         INC     B               
6620: 7E         LD      A,(HL)          
6621: 20 00      JR      NZ,$6623        
6623: 0C         INC     C               
6624: 7C         LD      A,H             
6625: 20 00      JR      NZ,$6627        
6627: 00         NOP                     
6628: FF         RST     0X38            
6629: 00         NOP                     
662A: 00         NOP                     
662B: F8 74      LDHL    SP,$74          
662D: 00         NOP                     
662E: 00         NOP                     
662F: 00         NOP                     
6630: 76         HALT                    
6631: 00         NOP                     
6632: 00         NOP                     
6633: 08 76 20   LD      ($2076),SP      
6636: 00         NOP                     
6637: 10 74      STOP    $74             
6639: 20 00      JR      NZ,$663B        
663B: F8 70      LDHL    SP,$70          
663D: 00         NOP                     
663E: 00         NOP                     
663F: 00         NOP                     
6640: 72         LD      (HL),D          
6641: 00         NOP                     
6642: 00         NOP                     
6643: 08 72 20   LD      ($2072),SP      
6646: 00         NOP                     
6647: 10 70      STOP    $70             
6649: 20 0A      JR      NZ,$6655        
664B: FB         EI                      
664C: 26 00      LD      H,$00           
664E: 0A         LD      A,(BC)          
664F: 01 26 00   LD      BC,$0026        
6652: 0A         LD      A,(BC)          
6653: 06 26      LD      B,$26           
6655: 00         NOP                     
6656: 0A         LD      A,(BC)          
6657: 0C         INC     C               
6658: 26 00      LD      H,$00           
665A: F0 F1      LD      A,($F1)         
665C: FE 02      CP      $02             
665E: 30 4C      JR      NC,$66AC        
6660: 21 40 C3   LD      HL,$C340        
6663: 09         ADD     HL,BC           
6664: 7E         LD      A,(HL)          
6665: E6 F0      AND     $F0             
6667: F6 08      OR      $08             
6669: 77         LD      (HL),A          
666A: F0 F1      LD      A,($F1)         
666C: 17         RLA                     
666D: 17         RLA                     
666E: 17         RLA                     
666F: 17         RLA                     
6670: 17         RLA                     
6671: E6 E0      AND     $E0             
6673: 5F         LD      E,A             
6674: 50         LD      D,B             
6675: 21 BA 65   LD      HL,$65BA        
6678: 19         ADD     HL,DE           
6679: 0E 08      LD      C,$08           
667B: CD 26 3D   CALL    $3D26           
667E: 00         NOP                     
667F: F0 F1      LD      A,($F1)         
6681: FE 05      CP      $05             
6683: 30 26      JR      NC,$66AB        
6685: 21 10 C3   LD      HL,$C310        
6688: 09         ADD     HL,BC           
6689: 7E         LD      A,(HL)          
668A: 3D         DEC     A               
668B: FE 08      CP      $08             
668D: 38 1C      JR      C,$66AB         
668F: 21 40 C3   LD      HL,$C340        
6692: 09         ADD     HL,BC           
6693: 7E         LD      A,(HL)          
6694: E6 F0      AND     $F0             
6696: F6 04      OR      $04             
6698: 77         LD      (HL),A          
6699: F0 EF      LD      A,($EF)         
669B: E0 EC      LDFF00  ($EC),A         
669D: AF         XOR     A               
669E: E0 F1      LDFF00  ($F1),A         
66A0: 21 4A 66   LD      HL,$664A        
66A3: 0E 04      LD      C,$04           
66A5: CD 26 3D   CALL    $3D26           
66A8: CD BA 3D   CALL    $3DBA           
66AB: C9         RET                     
66AC: 21 40 C3   LD      HL,$C340        
66AF: 09         ADD     HL,BC           
66B0: 7E         LD      A,(HL)          
66B1: E6 F0      AND     $F0             
66B3: F6 04      OR      $04             
66B5: 77         LD      (HL),A          
66B6: F0 F1      LD      A,($F1)         
66B8: 3D         DEC     A               
66B9: 3D         DEC     A               
66BA: 17         RLA                     
66BB: 17         RLA                     
66BC: 17         RLA                     
66BD: 17         RLA                     
66BE: E6 F0      AND     $F0             
66C0: 5F         LD      E,A             
66C1: 50         LD      D,B             
66C2: 21 FA 65   LD      HL,$65FA        
66C5: 19         ADD     HL,DE           
66C6: 0E 04      LD      C,$04           
66C8: CD 26 3D   CALL    $3D26           
66CB: CD 7F 66   CALL    $667F           
66CE: C9         RET                     
66CF: CD 91 08   CALL    $0891           
66D2: CA 6B 7A   JP      Z,$7A6B         
66D5: FE 0A      CP      $0A             
66D7: 3E 05      LD      A,$05           
66D9: 38 01      JR      C,$66DC         
66DB: 3C         INC     A               
66DC: E0 F1      LDFF00  ($F1),A         
66DE: CD AC 66   CALL    $66AC           
66E1: C9         RET                     
66E2: 1E 00      LD      E,$00           
66E4: 1E 60      LD      E,$60           
66E6: 1E 40      LD      E,$40           
66E8: 1E 20      LD      E,$20           
66EA: 7A         LD      A,D             
66EB: 00         NOP                     
66EC: 7A         LD      A,D             
66ED: 20 78      JR      NZ,$6767        
66EF: 00         NOP                     
66F0: 78         LD      A,B             
66F1: 20 11      JR      NZ,$6704        
66F3: E2         LDFF00  (C),A           
66F4: 66         LD      H,(HL)          
66F5: CD 3B 3C   CALL    $3C3B           
66F8: CD 65 79   CALL    $7965           
66FB: CD BF 3B   CALL    $3BBF           
66FE: F0 F0      LD      A,($F0)         
6700: C7         RST     0X00            
6701: 05         DEC     B               
6702: 67         LD      H,A             
6703: 2D         DEC     L               
6704: 67         LD      H,A             
6705: CD D1 79   CALL    $79D1           
6708: CD 0A 7A   CALL    $7A0A           
670B: 21 20 C3   LD      HL,$C320        
670E: 09         ADD     HL,BC           
670F: 35         DEC     (HL)            
6710: 21 10 C3   LD      HL,$C310        
6713: 09         ADD     HL,BC           
6714: 7E         LD      A,(HL)          
6715: E6 80      AND     $80             
6717: 28 09      JR      Z,$6722         
6719: 70         LD      (HL),B          
671A: CD 8D 3B   CALL    $3B8D           
671D: CD 91 08   CALL    $0891           
6720: 36 0F      LD      (HL),$0F        
6722: F0 E7      LD      A,($E7)         
6724: 1F         RRA                     
6725: 1F         RRA                     
6726: 1F         RRA                     
6727: E6 01      AND     $01             
6729: CD 87 3B   CALL    $3B87           
672C: C9         RET                     
672D: CD 91 08   CALL    $0891           
6730: CA 6B 7A   JP      Z,$7A6B         
6733: 1F         RRA                     
6734: 1F         RRA                     
6735: 1F         RRA                     
6736: E6 01      AND     $01             
6738: 3C         INC     A               
6739: 3C         INC     A               
673A: CD 87 3B   CALL    $3B87           
673D: C9         RET                     
673E: 6C         LD      L,H             
673F: 00         NOP                     
6740: 6E         LD      L,(HL)          
6741: 00         NOP                     
6742: 6E         LD      L,(HL)          
6743: 20 6C      JR      NZ,$67B1        
6745: 20 11      JR      NZ,$6758        
6747: 3E 67      LD      A,$67           
6749: CD 3B 3C   CALL    $3C3B           
674C: CD 65 79   CALL    $7965           
674F: CD D1 79   CALL    $79D1           
6752: CD 0A 7A   CALL    $7A0A           
6755: 21 20 C3   LD      HL,$C320        
6758: 09         ADD     HL,BC           
6759: 35         DEC     (HL)            
675A: 21 10 C3   LD      HL,$C310        
675D: 09         ADD     HL,BC           
675E: 7E         LD      A,(HL)          
675F: E6 80      AND     $80             
6761: 28 12      JR      Z,$6775         
6763: AF         XOR     A               
6764: 77         LD      (HL),A          
6765: CD 91 08   CALL    $0891           
6768: 36 0F      LD      (HL),$0F        
676A: 21 B0 C2   LD      HL,$C2B0        
676D: 09         ADD     HL,BC           
676E: 36 02      LD      (HL),$02        
6770: 3E FF      LD      A,$FF           
6772: CD 87 3B   CALL    $3B87           
6775: C9         RET                     
6776: 21 60 C4   LD      HL,$C460        
6779: 09         ADD     HL,BC           
677A: 5E         LD      E,(HL)          
677B: CB 23      SET     1,E             
677D: CB 23      SET     1,E             
677F: CB 23      SET     1,E             
6781: CB 23      SET     1,E             
6783: CB 23      SET     1,E             
6785: CB 23      SET     1,E             
6787: 50         LD      D,B             
6788: 21 00 D0   LD      HL,$D000        
678B: 19         ADD     HL,DE           
678C: D5         PUSH    DE              
678D: 1E 20      LD      E,$20           
678F: AF         XOR     A               
6790: 22         LD      (HLI),A         
6791: 1D         DEC     E               
6792: 7B         LD      A,E             
6793: FE 00      CP      $00             
6795: 20 F8      JR      NZ,$678F        
6797: D1         POP     DE              
6798: 21 00 D1   LD      HL,$D100        
679B: 19         ADD     HL,DE           
679C: 1E 20      LD      E,$20           
679E: AF         XOR     A               
679F: 22         LD      (HLI),A         
67A0: 1D         DEC     E               
67A1: 7B         LD      A,E             
67A2: FE 00      CP      $00             
67A4: 20 F8      JR      NZ,$679E        
67A6: 21 50 C2   LD      HL,$C250        
67A9: 09         ADD     HL,BC           
67AA: 36 06      LD      (HL),$06        
67AC: CD 91 08   CALL    $0891           
67AF: 36 40      LD      (HL),$40        
67B1: CD 8C 08   CALL    $088C           
67B4: 36 40      LD      (HL),$40        
67B6: 21 B0 C3   LD      HL,$C3B0        
67B9: 09         ADD     HL,BC           
67BA: 36 03      LD      (HL),$03        
67BC: C9         RET                     
67BD: 06 FA      LD      B,$FA           
67BF: 00         NOP                     
67C0: 00         NOP                     
67C1: 00         NOP                     
67C2: 00         NOP                     
67C3: FA 06 02   LD      A,($0206)       
67C6: 01 00 01   LD      BC,$0100        
67C9: 21 22 23   LD      HL,$2322        
67CC: 22         LD      (HLI),A         
67CD: F0 F7      LD      A,($F7)         
67CF: FE 07      CP      $07             
67D1: 20 04      JR      NZ,$67D7        
67D3: 3E 10      LD      A,$10           
67D5: E0 F5      LDFF00  ($F5),A         
67D7: CD 9A 69   CALL    $699A           
67DA: CD 65 79   CALL    $7965           
67DD: CD 12 3F   CALL    $3F12           
67E0: CD E2 08   CALL    $08E2           
67E3: CD B4 3B   CALL    $3BB4           
67E6: F0 F0      LD      A,($F0)         
67E8: C7         RST     0X00            
67E9: EF         RST     0X28            
67EA: 67         LD      H,A             
67EB: B5         OR      L               
67EC: 68         LD      L,B             
67ED: 0F         RRCA                    
67EE: 69         LD      L,C             
67EF: CD 91 08   CALL    $0891           
67F2: 20 05      JR      NZ,$67F9        
67F4: 36 00      LD      (HL),$00        
67F6: CD 8D 3B   CALL    $3B8D           
67F9: 21 D0 C3   LD      HL,$C3D0        
67FC: 09         ADD     HL,BC           
67FD: 7E         LD      A,(HL)          
67FE: 3C         INC     A               
67FF: E6 3F      AND     $3F             
6801: 77         LD      (HL),A          
6802: E0 D7      LDFF00  ($D7),A         
6804: 1F         RRA                     
6805: 1F         RRA                     
6806: 00         NOP                     
6807: E6 03      AND     $03             
6809: 5F         LD      E,A             
680A: 16 00      LD      D,$00           
680C: 21 C5 67   LD      HL,$67C5        
680F: 19         ADD     HL,DE           
6810: 7E         LD      A,(HL)          
6811: 21 B0 C2   LD      HL,$C2B0        
6814: 09         ADD     HL,BC           
6815: 77         LD      (HL),A          
6816: 21 C9 67   LD      HL,$67C9        
6819: 19         ADD     HL,DE           
681A: 7E         LD      A,(HL)          
681B: 21 C0 C2   LD      HL,$C2C0        
681E: 09         ADD     HL,BC           
681F: 77         LD      (HL),A          
6820: 21 60 C4   LD      HL,$C460        
6823: 09         ADD     HL,BC           
6824: 5E         LD      E,(HL)          
6825: CB 23      SET     1,E             
6827: CB 23      SET     1,E             
6829: CB 23      SET     1,E             
682B: CB 23      SET     1,E             
682D: CB 23      SET     1,E             
682F: CB 23      SET     1,E             
6831: 16 00      LD      D,$00           
6833: D5         PUSH    DE              
6834: 21 00 D0   LD      HL,$D000        
6837: 19         ADD     HL,DE           
6838: F0 D7      LD      A,($D7)         
683A: 5F         LD      E,A             
683B: 19         ADD     HL,DE           
683C: F0 EE      LD      A,($EE)         
683E: 77         LD      (HL),A          
683F: D1         POP     DE              
6840: 21 00 D1   LD      HL,$D100        
6843: 19         ADD     HL,DE           
6844: F0 D7      LD      A,($D7)         
6846: 5F         LD      E,A             
6847: 19         ADD     HL,DE           
6848: F0 EC      LD      A,($EC)         
684A: 77         LD      (HL),A          
684B: CD D1 79   CALL    $79D1           
684E: CD 9E 3B   CALL    $3B9E           
6851: 1E 0F      LD      E,$0F           
6853: 50         LD      D,B             
6854: 21 80 C2   LD      HL,$C280        
6857: 19         ADD     HL,DE           
6858: 7E         LD      A,(HL)          
6859: FE 05      CP      $05             
685B: 20 54      JR      NZ,$68B1        
685D: 21 A0 C3   LD      HL,$C3A0        
6860: 19         ADD     HL,DE           
6861: 7E         LD      A,(HL)          
6862: FE 02      CP      $02             
6864: 20 4B      JR      NZ,$68B1        
6866: 21 E0 C2   LD      HL,$C2E0        
6869: 19         ADD     HL,DE           
686A: 7E         LD      A,(HL)          
686B: FE 38      CP      $38             
686D: 38 42      JR      C,$68B1         
686F: 21 00 C2   LD      HL,$C200        
6872: 19         ADD     HL,DE           
6873: F0 EE      LD      A,($EE)         
6875: 96         SUB     (HL)            
6876: C6 06      ADD     $06             
6878: FE 0C      CP      $0C             
687A: 30 35      JR      NC,$68B1        
687C: 21 10 C2   LD      HL,$C210        
687F: 19         ADD     HL,DE           
6880: F0 EC      LD      A,($EC)         
6882: 96         SUB     (HL)            
6883: C6 06      ADD     $06             
6885: FE 0C      CP      $0C             
6887: 30 28      JR      NC,$68B1        
6889: 21 10 C3   LD      HL,$C310        
688C: 19         ADD     HL,DE           
688D: 7E         LD      A,(HL)          
688E: A7         AND     A               
688F: 20 20      JR      NZ,$68B1        
6891: 21 80 C2   LD      HL,$C280        
6894: 19         ADD     HL,DE           
6895: 70         LD      (HL),B          
6896: CD 8D 3B   CALL    $3B8D           
6899: 36 02      LD      (HL),$02        
689B: 21 00 C3   LD      HL,$C300        
689E: 09         ADD     HL,BC           
689F: 36 60      LD      (HL),$60        
68A1: 21 20 C4   LD      HL,$C420        
68A4: 09         ADD     HL,BC           
68A5: 36 0C      LD      (HL),$0C        
68A7: 21 40 C4   LD      HL,$C440        
68AA: 09         ADD     HL,BC           
68AB: 34         INC     (HL)            
68AC: 3E 2A      LD      A,$2A           
68AE: E0 F2      LDFF00  ($F2),A         
68B0: C9         RET                     
68B1: 1D         DEC     E               
68B2: 20 A0      JR      NZ,$6854        
68B4: C9         RET                     
68B5: CD 91 08   CALL    $0891           
68B8: 20 44      JR      NZ,$68FE        
68BA: CD ED 27   CALL    $27ED           
68BD: E6 1F      AND     $1F             
68BF: C6 40      ADD     $40             
68C1: 77         LD      (HL),A          
68C2: CD 8D 3B   CALL    $3B8D           
68C5: 70         LD      (HL),B          
68C6: 21 D0 C2   LD      HL,$C2D0        
68C9: 09         ADD     HL,BC           
68CA: 7E         LD      A,(HL)          
68CB: 3C         INC     A               
68CC: E6 03      AND     $03             
68CE: 77         LD      (HL),A          
68CF: 20 05      JR      NZ,$68D6        
68D1: CD 44 7A   CALL    $7A44           
68D4: 18 06      JR      $68DC           
68D6: CD ED 27   CALL    $27ED           
68D9: E6 03      AND     $03             
68DB: 5F         LD      E,A             
68DC: 21 F1 FF   LD      HL,$FFF1        
68DF: AE         XOR     (HL)            
68E0: E6 02      AND     $02             
68E2: 28 F2      JR      Z,$68D6         
68E4: 50         LD      D,B             
68E5: 21 B0 C3   LD      HL,$C3B0        
68E8: 09         ADD     HL,BC           
68E9: 73         LD      (HL),E          
68EA: 21 BD 67   LD      HL,$67BD        
68ED: 19         ADD     HL,DE           
68EE: 7E         LD      A,(HL)          
68EF: 21 40 C2   LD      HL,$C240        
68F2: 09         ADD     HL,BC           
68F3: 77         LD      (HL),A          
68F4: 21 C1 67   LD      HL,$67C1        
68F7: 19         ADD     HL,DE           
68F8: 7E         LD      A,(HL)          
68F9: 21 50 C2   LD      HL,$C250        
68FC: 09         ADD     HL,BC           
68FD: 77         LD      (HL),A          
68FE: C9         RET                     
68FF: F3         DI                      
6900: 0D         DEC     C               
6901: 00         NOP                     
6902: 00         NOP                     
6903: 00         NOP                     
6904: 00         NOP                     
6905: 0D         DEC     C               
6906: F3         DI                      
6907: 0C         INC     C               
6908: F4         ???                     
6909: 00         NOP                     
690A: 00         NOP                     
690B: 00         NOP                     
690C: 00         NOP                     
690D: F4         ???                     
690E: 0C         INC     C               
690F: 21 00 C3   LD      HL,$C300        
6912: 09         ADD     HL,BC           
6913: 7E         LD      A,(HL)          
6914: A7         AND     A               
6915: 20 0B      JR      NZ,$6922        
6917: CD 91 08   CALL    $0891           
691A: 36 30      LD      (HL),$30        
691C: CD 8D 3B   CALL    $3B8D           
691F: 36 01      LD      (HL),$01        
6921: C9         RET                     
6922: FE 24      CP      $24             
6924: 20 03      JR      NZ,$6929        
6926: CD D7 08   CALL    $08D7           
6929: FE 04      CP      $04             
692B: 20 1C      JR      NZ,$6949        
692D: F0 F1      LD      A,($F1)         
692F: 5F         LD      E,A             
6930: 50         LD      D,B             
6931: 21 07 69   LD      HL,$6907        
6934: 19         ADD     HL,DE           
6935: F0 EE      LD      A,($EE)         
6937: 86         ADD     A,(HL)          
6938: E0 D7      LDFF00  ($D7),A         
693A: 21 0B 69   LD      HL,$690B        
693D: 19         ADD     HL,DE           
693E: F0 EC      LD      A,($EC)         
6940: 86         ADD     A,(HL)          
6941: E0 D8      LDFF00  ($D8),A         
6943: 3E 02      LD      A,$02           
6945: CD 53 09   CALL    $0953           
6948: AF         XOR     A               
6949: FE 20      CP      $20             
694B: 20 38      JR      NZ,$6985        
694D: 21 40 C4   LD      HL,$C440        
6950: 09         ADD     HL,BC           
6951: 7E         LD      A,(HL)          
6952: FE 03      CP      $03             
6954: 20 2F      JR      NZ,$6985        
6956: 3E 02      LD      A,$02           
6958: CD 01 3C   CALL    $3C01           
695B: 38 28      JR      C,$6985         
695D: 21 E0 C2   LD      HL,$C2E0        
6960: 19         ADD     HL,DE           
6961: 36 17      LD      (HL),$17        
6963: C5         PUSH    BC              
6964: 21 B0 C3   LD      HL,$C3B0        
6967: 09         ADD     HL,BC           
6968: 4E         LD      C,(HL)          
6969: 21 FF 68   LD      HL,$68FF        
696C: 09         ADD     HL,BC           
696D: F0 D7      LD      A,($D7)         
696F: 86         ADD     A,(HL)          
6970: 21 00 C2   LD      HL,$C200        
6973: 19         ADD     HL,DE           
6974: 77         LD      (HL),A          
6975: 21 03 69   LD      HL,$6903        
6978: 09         ADD     HL,BC           
6979: F0 D8      LD      A,($D8)         
697B: 86         ADD     A,(HL)          
697C: 21 10 C2   LD      HL,$C210        
697F: 19         ADD     HL,DE           
6980: 77         LD      (HL),A          
6981: C1         POP     BC              
6982: CD C0 7D   CALL    $7DC0           
6985: C9         RET                     
6986: 66         LD      H,(HL)          
6987: 20 64      JR      NZ,$69ED        
6989: 20 64      JR      NZ,$69EF        
698B: 00         NOP                     
698C: 66         LD      H,(HL)          
698D: 00         NOP                     
698E: 62         LD      H,D             
698F: 00         NOP                     
6990: 62         LD      H,D             
6991: 20 60      JR      NZ,$69F3        
6993: 00         NOP                     
6994: 60         LD      H,B             
6995: 20 68      JR      NZ,$69FF        
6997: 00         NOP                     
6998: 68         LD      L,B             
6999: 20 CD      JR      NZ,$6968        
699B: 8C         ADC     A,H             
699C: 08 21 24   LD      ($2421),SP      
699F: C1         POP     BC              
69A0: B6         OR      (HL)            
69A1: 21 00 C3   LD      HL,$C300        
69A4: 09         ADD     HL,BC           
69A5: B6         OR      (HL)            
69A6: C2 DA 6B   JP      NZ,$6BDA        
69A9: F0 F1      LD      A,($F1)         
69AB: FE 02      CP      $02             
69AD: 20 09      JR      NZ,$69B8        
69AF: CD 08 6A   CALL    $6A08           
69B2: CD C1 69   CALL    $69C1           
69B5: C3 BA 3D   JP      $3DBA           
69B8: CD C1 69   CALL    $69C1           
69BB: CD 08 6A   CALL    $6A08           
69BE: C3 BA 3D   JP      $3DBA           
69C1: 21 D0 C3   LD      HL,$C3D0        
69C4: 09         ADD     HL,BC           
69C5: 7E         LD      A,(HL)          
69C6: E0 D7      LDFF00  ($D7),A         
69C8: C5         PUSH    BC              
69C9: 21 60 C4   LD      HL,$C460        
69CC: 09         ADD     HL,BC           
69CD: 5E         LD      E,(HL)          
69CE: 21 B0 C2   LD      HL,$C2B0        
69D1: 09         ADD     HL,BC           
69D2: 4E         LD      C,(HL)          
69D3: CB 23      SET     1,E             
69D5: CB 23      SET     1,E             
69D7: CB 23      SET     1,E             
69D9: CB 23      SET     1,E             
69DB: CB 23      SET     1,E             
69DD: CB 23      SET     1,E             
69DF: 50         LD      D,B             
69E0: D5         PUSH    DE              
69E1: 21 00 D0   LD      HL,$D000        
69E4: 19         ADD     HL,DE           
69E5: F0 D7      LD      A,($D7)         
69E7: 91         SUB     C               
69E8: E6 3F      AND     $3F             
69EA: 5F         LD      E,A             
69EB: 50         LD      D,B             
69EC: 19         ADD     HL,DE           
69ED: 7E         LD      A,(HL)          
69EE: E0 EE      LDFF00  ($EE),A         
69F0: D1         POP     DE              
69F1: 21 00 D1   LD      HL,$D100        
69F4: 19         ADD     HL,DE           
69F5: F0 D7      LD      A,($D7)         
69F7: 91         SUB     C               
69F8: E6 3F      AND     $3F             
69FA: 5F         LD      E,A             
69FB: 50         LD      D,B             
69FC: 19         ADD     HL,DE           
69FD: 7E         LD      A,(HL)          
69FE: E0 EC      LDFF00  ($EC),A         
6A00: C1         POP     BC              
6A01: 11 86 69   LD      DE,$6986        
6A04: CD 3B 3C   CALL    $3C3B           
6A07: C9         RET                     
6A08: 21 D0 C3   LD      HL,$C3D0        
6A0B: 09         ADD     HL,BC           
6A0C: 7E         LD      A,(HL)          
6A0D: E0 D7      LDFF00  ($D7),A         
6A0F: C5         PUSH    BC              
6A10: 21 60 C4   LD      HL,$C460        
6A13: 09         ADD     HL,BC           
6A14: 5E         LD      E,(HL)          
6A15: 21 C0 C2   LD      HL,$C2C0        
6A18: 09         ADD     HL,BC           
6A19: 4E         LD      C,(HL)          
6A1A: CB 23      SET     1,E             
6A1C: CB 23      SET     1,E             
6A1E: CB 23      SET     1,E             
6A20: CB 23      SET     1,E             
6A22: CB 23      SET     1,E             
6A24: CB 23      SET     1,E             
6A26: 50         LD      D,B             
6A27: D5         PUSH    DE              
6A28: 21 00 D0   LD      HL,$D000        
6A2B: 19         ADD     HL,DE           
6A2C: F0 D7      LD      A,($D7)         
6A2E: 91         SUB     C               
6A2F: E6 3F      AND     $3F             
6A31: 5F         LD      E,A             
6A32: 50         LD      D,B             
6A33: 19         ADD     HL,DE           
6A34: 7E         LD      A,(HL)          
6A35: E0 EE      LDFF00  ($EE),A         
6A37: D1         POP     DE              
6A38: 21 00 D1   LD      HL,$D100        
6A3B: 19         ADD     HL,DE           
6A3C: F0 D7      LD      A,($D7)         
6A3E: 91         SUB     C               
6A3F: E6 3F      AND     $3F             
6A41: 5F         LD      E,A             
6A42: 50         LD      D,B             
6A43: 19         ADD     HL,DE           
6A44: 7E         LD      A,(HL)          
6A45: E0 EC      LDFF00  ($EC),A         
6A47: C1         POP     BC              
6A48: 3E 04      LD      A,$04           
6A4A: E0 F1      LDFF00  ($F1),A         
6A4C: 11 86 69   LD      DE,$6986        
6A4F: CD 3B 3C   CALL    $3C3B           
6A52: 21 B0 C3   LD      HL,$C3B0        
6A55: 09         ADD     HL,BC           
6A56: 7E         LD      A,(HL)          
6A57: E0 F1      LDFF00  ($F1),A         
6A59: C9         RET                     
6A5A: 00         NOP                     
6A5B: 00         NOP                     
6A5C: 66         LD      H,(HL)          
6A5D: 20 00      JR      NZ,$6A5F        
6A5F: 08 64 20   LD      ($2064),SP      
6A62: 00         NOP                     
6A63: F3         DI                      
6A64: 68         LD      L,B             
6A65: 00         NOP                     
6A66: 00         NOP                     
6A67: FB         EI                      
6A68: 68         LD      L,B             
6A69: 20 00      JR      NZ,$6A6B        
6A6B: 00         NOP                     
6A6C: 64         LD      H,H             
6A6D: 00         NOP                     
6A6E: 00         NOP                     
6A6F: 08 66 00   LD      ($0066),SP      
6A72: 00         NOP                     
6A73: 0D         DEC     C               
6A74: 68         LD      L,B             
6A75: 00         NOP                     
6A76: 00         NOP                     
6A77: 15         DEC     D               
6A78: 68         LD      L,B             
6A79: 20 00      JR      NZ,$6A7B        
6A7B: 00         NOP                     
6A7C: 62         LD      H,D             
6A7D: 00         NOP                     
6A7E: 00         NOP                     
6A7F: 08 62 20   LD      ($2062),SP      
6A82: 0D         DEC     C               
6A83: 00         NOP                     
6A84: 68         LD      L,B             
6A85: 00         NOP                     
6A86: 0D         DEC     C               
6A87: 08 68 20   LD      ($2068),SP      
6A8A: 00         NOP                     
6A8B: 00         NOP                     
6A8C: 60         LD      H,B             
6A8D: 00         NOP                     
6A8E: 00         NOP                     
6A8F: 08 60 20   LD      ($2060),SP      
6A92: F3         DI                      
6A93: 00         NOP                     
6A94: 68         LD      L,B             
6A95: 00         NOP                     
6A96: F3         DI                      
6A97: 08 68 20   LD      ($2068),SP      
6A9A: 00         NOP                     
6A9B: 04         INC     B               
6A9C: 66         LD      H,(HL)          
6A9D: 20 00      JR      NZ,$6A9F        
6A9F: 0C         INC     C               
6AA0: 64         LD      H,H             
6AA1: 20 F8      JR      NZ,$6A9B        
6AA3: EC         ???                     
6AA4: 6C         LD      L,H             
6AA5: 00         NOP                     
6AA6: F8 F4      LDHL    SP,$F4          
6AA8: 6A         LD      L,D             
6AA9: 00         NOP                     
6AAA: F8 FC      LDHL    SP,$FC          
6AAC: 6A         LD      L,D             
6AAD: 20 F8      JR      NZ,$6AA7        
6AAF: 04         INC     B               
6AB0: 6C         LD      L,H             
6AB1: 20 08      JR      NZ,$6ABB        
6AB3: EC         ???                     
6AB4: 6C         LD      L,H             
6AB5: 40         LD      B,B             
6AB6: 08 F4 6E   LD      ($6EF4),SP      
6AB9: 40         LD      B,B             
6ABA: 08 FC 6E   LD      ($6EFC),SP      
6ABD: 60         LD      H,B             
6ABE: 08 04 6C   LD      ($6C04),SP      
6AC1: 60         LD      H,B             
6AC2: 00         NOP                     
6AC3: FC         ???                     
6AC4: 64         LD      H,H             
6AC5: 00         NOP                     
6AC6: 00         NOP                     
6AC7: 04         INC     B               
6AC8: 66         LD      H,(HL)          
6AC9: 00         NOP                     
6ACA: F8 04      LDHL    SP,$04          
6ACC: 6C         LD      L,H             
6ACD: 00         NOP                     
6ACE: F8 0C      LDHL    SP,$0C          
6AD0: 6A         LD      L,D             
6AD1: 00         NOP                     
6AD2: F8 14      LDHL    SP,$14          
6AD4: 6A         LD      L,D             
6AD5: 20 F8      JR      NZ,$6ACF        
6AD7: 1C         INC     E               
6AD8: 6C         LD      L,H             
6AD9: 20 08      JR      NZ,$6AE3        
6ADB: 04         INC     B               
6ADC: 6C         LD      L,H             
6ADD: 40         LD      B,B             
6ADE: 08 0C 6E   LD      ($6E0C),SP      
6AE1: 40         LD      B,B             
6AE2: 08 14 6E   LD      ($6E14),SP      
6AE5: 60         LD      H,B             
6AE6: 08 1C 6C   LD      ($6C1C),SP      
6AE9: 60         LD      H,B             
6AEA: 04         INC     B               
6AEB: F8 6C      LDHL    SP,$6C          
6AED: 00         NOP                     
6AEE: 04         INC     B               
6AEF: 00         NOP                     
6AF0: 6A         LD      L,D             
6AF1: 00         NOP                     
6AF2: 04         INC     B               
6AF3: 08 6A 20   LD      ($206A),SP      
6AF6: 04         INC     B               
6AF7: 10 6C      STOP    $6C             
6AF9: 20 14      JR      NZ,$6B0F        
6AFB: F8 6C      LDHL    SP,$6C          
6AFD: 40         LD      B,B             
6AFE: 14         INC     D               
6AFF: 00         NOP                     
6B00: 6E         LD      L,(HL)          
6B01: 40         LD      B,B             
6B02: 14         INC     D               
6B03: 08 6E 60   LD      ($606E),SP      
6B06: 14         INC     D               
6B07: 10 6C      STOP    $6C             
6B09: 60         LD      H,B             
6B0A: FC         ???                     
6B0B: 00         NOP                     
6B0C: 62         LD      H,D             
6B0D: 00         NOP                     
6B0E: FC         ???                     
6B0F: 08 62 20   LD      ($2062),SP      
6B12: 04         INC     B               
6B13: 00         NOP                     
6B14: 60         LD      H,B             
6B15: 00         NOP                     
6B16: 04         INC     B               
6B17: 08 60 20   LD      ($2060),SP      
6B1A: EC         ???                     
6B1B: F8 6C      LDHL    SP,$6C          
6B1D: 00         NOP                     
6B1E: EC         ???                     
6B1F: 00         NOP                     
6B20: 6A         LD      L,D             
6B21: 00         NOP                     
6B22: EC         ???                     
6B23: 08 6A 20   LD      ($206A),SP      
6B26: EC         ???                     
6B27: 10 6C      STOP    $6C             
6B29: 20 FC      JR      NZ,$6B27        
6B2B: F8 6C      LDHL    SP,$6C          
6B2D: 40         LD      B,B             
6B2E: FC         ???                     
6B2F: 00         NOP                     
6B30: 6E         LD      L,(HL)          
6B31: 40         LD      B,B             
6B32: FC         ???                     
6B33: 08 6E 60   LD      ($606E),SP      
6B36: FC         ???                     
6B37: 10 6C      STOP    $6C             
6B39: 60         LD      H,B             
6B3A: 00         NOP                     
6B3B: 02         LD      (BC),A          
6B3C: 66         LD      H,(HL)          
6B3D: 20 00      JR      NZ,$6B3F        
6B3F: 0A         LD      A,(BC)          
6B40: 64         LD      H,H             
6B41: 20 FB      JR      NZ,$6B3E        
6B43: EF         RST     0X28            
6B44: 6C         LD      L,H             
6B45: 00         NOP                     
6B46: FB         EI                      
6B47: F7         RST     0X30            
6B48: 6E         LD      L,(HL)          
6B49: 00         NOP                     
6B4A: FB         EI                      
6B4B: F9         LD      SP,HL           
6B4C: 6E         LD      L,(HL)          
6B4D: 20 FB      JR      NZ,$6B4A        
6B4F: 01 6C 20   LD      BC,$206C        
6B52: 05         DEC     B               
6B53: EF         RST     0X28            
6B54: 6C         LD      L,H             
6B55: 40         LD      B,B             
6B56: 05         DEC     B               
6B57: F7         RST     0X30            
6B58: 6E         LD      L,(HL)          
6B59: 40         LD      B,B             
6B5A: 05         DEC     B               
6B5B: F9         LD      SP,HL           
6B5C: 6E         LD      L,(HL)          
6B5D: 60         LD      H,B             
6B5E: 05         DEC     B               
6B5F: 01 6C 60   LD      BC,$606C        
6B62: 00         NOP                     
6B63: FE 64      CP      $64             
6B65: 00         NOP                     
6B66: 00         NOP                     
6B67: 02         LD      (BC),A          
6B68: 66         LD      H,(HL)          
6B69: 00         NOP                     
6B6A: FB         EI                      
6B6B: 07         RLCA                    
6B6C: 6C         LD      L,H             
6B6D: 00         NOP                     
6B6E: FB         EI                      
6B6F: 0F         RRCA                    
6B70: 6E         LD      L,(HL)          
6B71: 00         NOP                     
6B72: FB         EI                      
6B73: 11 6E 20   LD      DE,$206E        
6B76: FB         EI                      
6B77: 19         ADD     HL,DE           
6B78: 6C         LD      L,H             
6B79: 20 05      JR      NZ,$6B80        
6B7B: 07         RLCA                    
6B7C: 6C         LD      L,H             
6B7D: 40         LD      B,B             
6B7E: 05         DEC     B               
6B7F: 0F         RRCA                    
6B80: 6E         LD      L,(HL)          
6B81: 40         LD      B,B             
6B82: 05         DEC     B               
6B83: 11 6E 60   LD      DE,$606E        
6B86: 05         DEC     B               
6B87: 19         ADD     HL,DE           
6B88: 6C         LD      L,H             
6B89: 60         LD      H,B             
6B8A: 07         RLCA                    
6B8B: FB         EI                      
6B8C: 6C         LD      L,H             
6B8D: 00         NOP                     
6B8E: 07         RLCA                    
6B8F: 03         INC     BC              
6B90: 6E         LD      L,(HL)          
6B91: 00         NOP                     
6B92: 07         RLCA                    
6B93: 05         DEC     B               
6B94: 6E         LD      L,(HL)          
6B95: 20 07      JR      NZ,$6B9E        
6B97: 0D         DEC     C               
6B98: 6C         LD      L,H             
6B99: 20 11      JR      NZ,$6BAC        
6B9B: FB         EI                      
6B9C: 6C         LD      L,H             
6B9D: 40         LD      B,B             
6B9E: 11 03 6E   LD      DE,$6E03        
6BA1: 40         LD      B,B             
6BA2: 11 05 6E   LD      DE,$6E05        
6BA5: 60         LD      H,B             
6BA6: 11 0D 6C   LD      DE,$6C0D        
6BA9: 60         LD      H,B             
6BAA: FE 00      CP      $00             
6BAC: 62         LD      H,D             
6BAD: 00         NOP                     
6BAE: FE 08      CP      $08             
6BB0: 62         LD      H,D             
6BB1: 20 02      JR      NZ,$6BB5        
6BB3: 00         NOP                     
6BB4: 60         LD      H,B             
6BB5: 00         NOP                     
6BB6: 02         LD      (BC),A          
6BB7: 08 60 20   LD      ($2060),SP      
6BBA: EF         RST     0X28            
6BBB: FB         EI                      
6BBC: 6C         LD      L,H             
6BBD: 00         NOP                     
6BBE: EF         RST     0X28            
6BBF: 03         INC     BC              
6BC0: 6E         LD      L,(HL)          
6BC1: 00         NOP                     
6BC2: EF         RST     0X28            
6BC3: 05         DEC     B               
6BC4: 6E         LD      L,(HL)          
6BC5: 20 EF      JR      NZ,$6BB6        
6BC7: 0D         DEC     C               
6BC8: 6C         LD      L,H             
6BC9: 20 F9      JR      NZ,$6BC4        
6BCB: FB         EI                      
6BCC: 6C         LD      L,H             
6BCD: 40         LD      B,B             
6BCE: F9         LD      SP,HL           
6BCF: 03         INC     BC              
6BD0: 6E         LD      L,(HL)          
6BD1: 40         LD      B,B             
6BD2: F9         LD      SP,HL           
6BD3: 05         DEC     B               
6BD4: 6E         LD      L,(HL)          
6BD5: 60         LD      H,B             
6BD6: F9         LD      SP,HL           
6BD7: 0D         DEC     C               
6BD8: 6C         LD      L,H             
6BD9: 60         LD      H,B             
6BDA: 21 00 C3   LD      HL,$C300        
6BDD: 09         ADD     HL,BC           
6BDE: 7E         LD      A,(HL)          
6BDF: FE 08      CP      $08             
6BE1: 38 2F      JR      C,$6C12         
6BE3: FE 28      CP      $28             
6BE5: 30 2B      JR      NC,$6C12        
6BE7: 21 3A 6B   LD      HL,$6B3A        
6BEA: FE 0E      CP      $0E             
6BEC: 38 07      JR      C,$6BF5         
6BEE: FE 22      CP      $22             
6BF0: 30 03      JR      NC,$6BF5        
6BF2: 21 9A 6A   LD      HL,$6A9A        
6BF5: F0 F1      LD      A,($F1)         
6BF7: 5F         LD      E,A             
6BF8: 50         LD      D,B             
6BF9: CB 23      SET     1,E             
6BFB: CB 23      SET     1,E             
6BFD: CB 23      SET     1,E             
6BFF: 7B         LD      A,E             
6C00: CB 23      SET     1,E             
6C02: CB 23      SET     1,E             
6C04: 83         ADD     A,E             
6C05: 5F         LD      E,A             
6C06: 19         ADD     HL,DE           
6C07: 0E 0A      LD      C,$0A           
6C09: CD 26 3D   CALL    $3D26           
6C0C: 3E 08      LD      A,$08           
6C0E: CD D0 3D   CALL    $3DD0           
6C11: C9         RET                     
6C12: F0 F1      LD      A,($F1)         
6C14: 17         RLA                     
6C15: 17         RLA                     
6C16: 17         RLA                     
6C17: 17         RLA                     
6C18: E6 F0      AND     $F0             
6C1A: 5F         LD      E,A             
6C1B: 50         LD      D,B             
6C1C: 21 5A 6A   LD      HL,$6A5A        
6C1F: 19         ADD     HL,DE           
6C20: 0E 04      LD      C,$04           
6C22: CD 26 3D   CALL    $3D26           
6C25: 3E 02      LD      A,$02           
6C27: CD D0 3D   CALL    $3DD0           
6C2A: C9         RET                     
6C2B: CD 91 08   CALL    $0891           
6C2E: 36 80      LD      (HL),$80        
6C30: AF         XOR     A               
6C31: EA 00 D2   LD      ($D200),A       
6C34: EA 03 D2   LD      ($D203),A       
6C37: EA 04 D2   LD      ($D204),A       
6C3A: 21 90 C3   LD      HL,$C390        
6C3D: 09         ADD     HL,BC           
6C3E: 36 01      LD      (HL),$01        
6C40: C9         RET                     
6C41: CD 0E 38   CALL    $380E           
6C44: CD 12 3F   CALL    $3F12           
6C47: CD E2 08   CALL    $08E2           
6C4A: 21 B0 C2   LD      HL,$C2B0        
6C4D: 09         ADD     HL,BC           
6C4E: 7E         LD      A,(HL)          
6C4F: C7         RST     0X00            
6C50: 56         LD      D,(HL)          
6C51: 6C         LD      L,H             
6C52: 07         RLCA                    
6C53: 72         LD      (HL),D          
6C54: F9         LD      SP,HL           
6C55: 74         LD      (HL),H          
6C56: 79         LD      A,C             
6C57: EA 01 D2   LD      ($D201),A       
6C5A: F0 F0      LD      A,($F0)         
6C5C: C7         RST     0X00            
6C5D: 65         LD      H,L             
6C5E: 6C         LD      L,H             
6C5F: A9         XOR     C               
6C60: 6C         LD      L,H             
6C61: 95         SUB     L               
6C62: 6D         LD      L,L             
6C63: 0B         DEC     BC              
6C64: 70         LD      (HL),B          
6C65: CD 91 08   CALL    $0891           
6C68: 20 16      JR      NZ,$6C80        
6C6A: 36 80      LD      (HL),$80        
6C6C: 3E FF      LD      A,$FF           
6C6E: EA 57 C1   LD      ($C157),A       
6C71: 3E 3E      LD      A,$3E           
6C73: E0 F4      LDFF00  ($F4),A         
6C75: EA E8 D3   LD      ($D3E8),A       
6C78: 3E 04      LD      A,$04           
6C7A: EA 58 C1   LD      ($C158),A       
6C7D: CD 8D 3B   CALL    $3B8D           
6C80: C9         RET                     
6C81: 20 60      JR      NZ,$6CE3        
6C83: 20 60      JR      NZ,$6CE5        
6C85: 00         NOP                     
6C86: 00         NOP                     
6C87: 70         LD      (HL),B          
6C88: 70         LD      (HL),B          
6C89: 08 08 08   LD      ($0808),SP      
6C8C: 08 09 0B   LD      ($0B09),SP      
6C8F: 0B         DEC     BC              
6C90: 0A         LD      A,(BC)          
6C91: 08 08 08   LD      ($0808),SP      
6C94: 08 09 0B   LD      ($0B09),SP      
6C97: 0B         DEC     BC              
6C98: 0A         LD      A,(BC)          
6C99: 05         DEC     B               
6C9A: 07         RLCA                    
6C9B: 07         RLCA                    
6C9C: 06 04      LD      B,$04           
6C9E: 04         INC     B               
6C9F: 04         INC     B               
6CA0: 04         INC     B               
6CA1: 05         DEC     B               
6CA2: 07         RLCA                    
6CA3: 07         RLCA                    
6CA4: 06 04      LD      B,$04           
6CA6: 04         INC     B               
6CA7: 04         INC     B               
6CA8: 04         INC     B               
6CA9: 3E 38      LD      A,$38           
6CAB: E0 CE      LDFF00  ($CE),A         
6CAD: C6 10      ADD     $10             
6CAF: 21 00 C2   LD      HL,$C200        
6CB2: 09         ADD     HL,BC           
6CB3: 77         LD      (HL),A          
6CB4: 3E 30      LD      A,$30           
6CB6: E0 CD      LDFF00  ($CD),A         
6CB8: C6 18      ADD     $18             
6CBA: 21 10 C2   LD      HL,$C210        
6CBD: 09         ADD     HL,BC           
6CBE: 77         LD      (HL),A          
6CBF: CD 91 08   CALL    $0891           
6CC2: C2 48 6D   JP      NZ,$6D48        
6CC5: 36 FF      LD      (HL),$FF        
6CC7: AF         XOR     A               
6CC8: EA E8 D3   LD      ($D3E8),A       
6CCB: CD 8D 3B   CALL    $3B8D           
6CCE: 3E AF      LD      A,$AF           
6CD0: EA 45 D7   LD      ($D745),A       
6CD3: 3E AF      LD      A,$AF           
6CD5: EA 46 D7   LD      ($D746),A       
6CD8: 3E B0      LD      A,$B0           
6CDA: EA 55 D7   LD      ($D755),A       
6CDD: 3E B0      LD      A,$B0           
6CDF: EA 56 D7   LD      ($D756),A       
6CE2: CD 8C 08   CALL    $088C           
6CE5: 36 1F      LD      (HL),$1F        
6CE7: CD 87 08   CALL    $0887           
6CEA: 36 B0      LD      (HL),$B0        
6CEC: CD 64 3E   CALL    $3E64           
6CEF: 21 80 C2   LD      HL,$C280        
6CF2: 09         ADD     HL,BC           
6CF3: 36 05      LD      (HL),$05        
6CF5: 21 00 C2   LD      HL,$C200        
6CF8: 09         ADD     HL,BC           
6CF9: 7E         LD      A,(HL)          
6CFA: C6 10      ADD     $10             
6CFC: 77         LD      (HL),A          
6CFD: CD 64 3E   CALL    $3E64           
6D00: 21 80 C2   LD      HL,$C280        
6D03: 09         ADD     HL,BC           
6D04: 36 05      LD      (HL),$05        
6D06: CD 64 3E   CALL    $3E64           
6D09: CD D7 08   CALL    $08D7           
6D0C: 21 80 C2   LD      HL,$C280        
6D0F: 09         ADD     HL,BC           
6D10: 36 05      LD      (HL),$05        
6D12: CD 39 28   CALL    $2839           
6D15: FA 00 D6   LD      A,($D600)       
6D18: 5F         LD      E,A             
6D19: 16 00      LD      D,$00           
6D1B: 21 01 D6   LD      HL,$D601        
6D1E: 19         ADD     HL,DE           
6D1F: C6 1C      ADD     $1C             
6D21: EA 00 D6   LD      ($D600),A       
6D24: CD 2D 6D   CALL    $6D2D           
6D27: CD 2D 6D   CALL    $6D2D           
6D2A: CD 2D 6D   CALL    $6D2D           
6D2D: F0 CF      LD      A,($CF)         
6D2F: 22         LD      (HLI),A         
6D30: F0 D0      LD      A,($D0)         
6D32: 3C         INC     A               
6D33: E0 D0      LDFF00  ($D0),A         
6D35: 22         LD      (HLI),A         
6D36: 3E 83      LD      A,$83           
6D38: 22         LD      (HLI),A         
6D39: 3E 76      LD      A,$76           
6D3B: 22         LD      (HLI),A         
6D3C: 3E 7E      LD      A,$7E           
6D3E: 22         LD      (HLI),A         
6D3F: 3E 7E      LD      A,$7E           
6D41: 22         LD      (HLI),A         
6D42: 3E 77      LD      A,$77           
6D44: 22         LD      (HLI),A         
6D45: AF         XOR     A               
6D46: 77         LD      (HL),A          
6D47: C9         RET                     
6D48: FE 40      CP      $40             
6D4A: C2 94 6D   JP      NZ,$6D94        
6D4D: CD 39 28   CALL    $2839           
6D50: FA 00 D6   LD      A,($D600)       
6D53: 5F         LD      E,A             
6D54: 16 00      LD      D,$00           
6D56: 21 01 D6   LD      HL,$D601        
6D59: 19         ADD     HL,DE           
6D5A: C6 1C      ADD     $1C             
6D5C: EA 00 D6   LD      ($D600),A       
6D5F: CD 62 6D   CALL    $6D62           
6D62: F0 CF      LD      A,($CF)         
6D64: 22         LD      (HLI),A         
6D65: F0 D0      LD      A,($D0)         
6D67: 3C         INC     A               
6D68: E0 D0      LDFF00  ($D0),A         
6D6A: 22         LD      (HLI),A         
6D6B: 3E 83      LD      A,$83           
6D6D: 22         LD      (HLI),A         
6D6E: 3E 1C      LD      A,$1C           
6D70: 22         LD      (HLI),A         
6D71: 3E 1E      LD      A,$1E           
6D73: 22         LD      (HLI),A         
6D74: 3E 1C      LD      A,$1C           
6D76: 22         LD      (HLI),A         
6D77: 3E 1E      LD      A,$1E           
6D79: 22         LD      (HLI),A         
6D7A: F0 CF      LD      A,($CF)         
6D7C: 22         LD      (HLI),A         
6D7D: F0 D0      LD      A,($D0)         
6D7F: 3C         INC     A               
6D80: E0 D0      LDFF00  ($D0),A         
6D82: 22         LD      (HLI),A         
6D83: 3E 83      LD      A,$83           
6D85: 22         LD      (HLI),A         
6D86: 3E 1D      LD      A,$1D           
6D88: 22         LD      (HLI),A         
6D89: 3E 1F      LD      A,$1F           
6D8B: 22         LD      (HLI),A         
6D8C: 3E 1D      LD      A,$1D           
6D8E: 22         LD      (HLI),A         
6D8F: 3E 1F      LD      A,$1F           
6D91: 22         LD      (HLI),A         
6D92: AF         XOR     A               
6D93: 77         LD      (HL),A          
6D94: C9         RET                     
6D95: 21 00 C2   LD      HL,$C200        
6D98: 09         ADD     HL,BC           
6D99: 7E         LD      A,(HL)          
6D9A: F5         PUSH    AF              
6D9B: 21 10 C2   LD      HL,$C210        
6D9E: 09         ADD     HL,BC           
6D9F: 7E         LD      A,(HL)          
6DA0: F5         PUSH    AF              
6DA1: CD 0B 70   CALL    $700B           
6DA4: F1         POP     AF              
6DA5: 21 10 C2   LD      HL,$C210        
6DA8: 09         ADD     HL,BC           
6DA9: 77         LD      (HL),A          
6DAA: F1         POP     AF              
6DAB: 21 00 C2   LD      HL,$C200        
6DAE: 09         ADD     HL,BC           
6DAF: 77         LD      (HL),A          
6DB0: CD BA 3D   CALL    $3DBA           
6DB3: CD 91 08   CALL    $0891           
6DB6: 20 04      JR      NZ,$6DBC        
6DB8: CD 8D 3B   CALL    $3B8D           
6DBB: C9         RET                     
6DBC: FE 98      CP      $98             
6DBE: 28 0D      JR      Z,$6DCD         
6DC0: FE 68      CP      $68             
6DC2: 28 09      JR      Z,$6DCD         
6DC4: FE 38      CP      $38             
6DC6: 28 05      JR      Z,$6DCD         
6DC8: FE 08      CP      $08             
6DCA: C2 A8 6E   JP      NZ,$6EA8        
6DCD: 21 D0 C3   LD      HL,$C3D0        
6DD0: 09         ADD     HL,BC           
6DD1: 7E         LD      A,(HL)          
6DD2: FE 04      CP      $04             
6DD4: CA A8 6E   JP      Z,$6EA8         
6DD7: 34         INC     (HL)            
6DD8: 5F         LD      E,A             
6DD9: 50         LD      D,B             
6DDA: 21 81 6C   LD      HL,$6C81        
6DDD: 19         ADD     HL,DE           
6DDE: 7E         LD      A,(HL)          
6DDF: E0 CE      LDFF00  ($CE),A         
6DE1: 21 85 6C   LD      HL,$6C85        
6DE4: 19         ADD     HL,DE           
6DE5: 7E         LD      A,(HL)          
6DE6: E0 CD      LDFF00  ($CD),A         
6DE8: CB 23      SET     1,E             
6DEA: CB 23      SET     1,E             
6DEC: CB 23      SET     1,E             
6DEE: 21 89 6C   LD      HL,$6C89        
6DF1: 19         ADD     HL,DE           
6DF2: E5         PUSH    HL              
6DF3: CD 39 28   CALL    $2839           
6DF6: FA 00 D6   LD      A,($D600)       
6DF9: 5F         LD      E,A             
6DFA: 16 00      LD      D,$00           
6DFC: 21 01 D6   LD      HL,$D601        
6DFF: 19         ADD     HL,DE           
6E00: C6 0E      ADD     $0E             
6E02: EA 00 D6   LD      ($D600),A       
6E05: D1         POP     DE              
6E06: F0 CF      LD      A,($CF)         
6E08: 22         LD      (HLI),A         
6E09: F0 D0      LD      A,($D0)         
6E0B: 22         LD      (HLI),A         
6E0C: 3E 03      LD      A,$03           
6E0E: 22         LD      (HLI),A         
6E0F: 1A         LD      A,(DE)          
6E10: 13         INC     DE              
6E11: 22         LD      (HLI),A         
6E12: 1A         LD      A,(DE)          
6E13: 13         INC     DE              
6E14: 22         LD      (HLI),A         
6E15: 1A         LD      A,(DE)          
6E16: 13         INC     DE              
6E17: 22         LD      (HLI),A         
6E18: 1A         LD      A,(DE)          
6E19: 13         INC     DE              
6E1A: 22         LD      (HLI),A         
6E1B: F0 CF      LD      A,($CF)         
6E1D: 22         LD      (HLI),A         
6E1E: F0 D0      LD      A,($D0)         
6E20: C6 20      ADD     $20             
6E22: 22         LD      (HLI),A         
6E23: 3E 03      LD      A,$03           
6E25: 22         LD      (HLI),A         
6E26: 1A         LD      A,(DE)          
6E27: 13         INC     DE              
6E28: 22         LD      (HLI),A         
6E29: 1A         LD      A,(DE)          
6E2A: 13         INC     DE              
6E2B: 22         LD      (HLI),A         
6E2C: 1A         LD      A,(DE)          
6E2D: 13         INC     DE              
6E2E: 22         LD      (HLI),A         
6E2F: 1A         LD      A,(DE)          
6E30: 22         LD      (HLI),A         
6E31: AF         XOR     A               
6E32: 77         LD      (HL),A          
6E33: 3E D5      LD      A,$D5           
6E35: EA 13 D7   LD      ($D713),A       
6E38: EA 17 D7   LD      ($D717),A       
6E3B: 3E D6      LD      A,$D6           
6E3D: EA 14 D7   LD      ($D714),A       
6E40: EA 18 D7   LD      ($D718),A       
6E43: 3E D7      LD      A,$D7           
6E45: EA 83 D7   LD      ($D783),A       
6E48: EA 87 D7   LD      ($D787),A       
6E4B: 3E D8      LD      A,$D8           
6E4D: EA 84 D7   LD      ($D784),A       
6E50: EA 88 D7   LD      ($D788),A       
6E53: 3E 5D      LD      A,$5D           
6E55: CD 01 3C   CALL    $3C01           
6E58: 21 B0 C2   LD      HL,$C2B0        
6E5B: 19         ADD     HL,DE           
6E5C: 36 01      LD      (HL),$01        
6E5E: 21 00 C2   LD      HL,$C200        
6E61: 19         ADD     HL,DE           
6E62: F0 CE      LD      A,($CE)         
6E64: C6 10      ADD     $10             
6E66: 77         LD      (HL),A          
6E67: 21 00 C2   LD      HL,$C200        
6E6A: 09         ADD     HL,BC           
6E6B: 77         LD      (HL),A          
6E6C: 21 10 C2   LD      HL,$C210        
6E6F: 19         ADD     HL,DE           
6E70: F0 CD      LD      A,($CD)         
6E72: C6 10      ADD     $10             
6E74: 77         LD      (HL),A          
6E75: 21 10 C2   LD      HL,$C210        
6E78: 09         ADD     HL,BC           
6E79: C6 08      ADD     $08             
6E7B: 77         LD      (HL),A          
6E7C: 21 E0 C2   LD      HL,$C2E0        
6E7F: 19         ADD     HL,DE           
6E80: 36 2F      LD      (HL),$2F        
6E82: 21 D0 C3   LD      HL,$C3D0        
6E85: 09         ADD     HL,BC           
6E86: 7E         LD      A,(HL)          
6E87: FE 03      CP      $03             
6E89: 3E 00      LD      A,$00           
6E8B: 38 0A      JR      C,$6E97         
6E8D: 21 10 C2   LD      HL,$C210        
6E90: 09         ADD     HL,BC           
6E91: 7E         LD      A,(HL)          
6E92: D6 08      SUB     $08             
6E94: 77         LD      (HL),A          
6E95: 3E 01      LD      A,$01           
6E97: 21 80 C3   LD      HL,$C380        
6E9A: 19         ADD     HL,DE           
6E9B: 77         LD      (HL),A          
6E9C: CD 64 3E   CALL    $3E64           
6E9F: 21 80 C2   LD      HL,$C280        
6EA2: 09         ADD     HL,BC           
6EA3: 36 05      LD      (HL),$05        
6EA5: CD D7 08   CALL    $08D7           
6EA8: C9         RET                     
6EA9: D0         RET     NC              
6EAA: D1         POP     DE              
6EAB: D4 D9 DF   CALL    NC,$DFD9        
6EAE: E6 EE      AND     $EE             
6EB0: F7         RST     0X30            
6EB1: 00         NOP                     
6EB2: 09         ADD     HL,BC           
6EB3: 12         LD      (DE),A          
6EB4: 1A         LD      A,(DE)          
6EB5: 21 27 2C   LD      HL,$2C27        
6EB8: 2F         CPL                     
6EB9: 30 2F      JR      NC,$6EEA        
6EBB: 2C         INC     L               
6EBC: 27         DAA                     
6EBD: 21 1A 12   LD      HL,$121A        
6EC0: 09         ADD     HL,BC           
6EC1: 00         NOP                     
6EC2: F7         RST     0X30            
6EC3: EE E6      XOR     $E6             
6EC5: DF         RST     0X18            
6EC6: D9         RETI                    
6EC7: D4 D1 D0   CALL    NC,$D0D1        
6ECA: D1         POP     DE              
6ECB: D4 D9 DF   CALL    NC,$DFD9        
6ECE: E6 EE      AND     $EE             
6ED0: F7         RST     0X30            
6ED1: DA DB DD   JP      C,$DDDB         
6ED4: E1         POP     HL              
6ED5: E6 EB      AND     $EB             
6ED7: F2         ???                     
6ED8: F9         LD      SP,HL           
6ED9: 00         NOP                     
6EDA: 07         RLCA                    
6EDB: 0E 15      LD      C,$15           
6EDD: 1A         LD      A,(DE)          
6EDE: 1F         RRA                     
6EDF: 23         INC     HL              
6EE0: 25         DEC     H               
6EE1: 26 25      LD      H,$25           
6EE3: 23         INC     HL              
6EE4: 1F         RRA                     
6EE5: 1A         LD      A,(DE)          
6EE6: 15         DEC     D               
6EE7: 0E 07      LD      C,$07           
6EE9: 00         NOP                     
6EEA: F9         LD      SP,HL           
6EEB: F2         ???                     
6EEC: EB         ???                     
6EED: E6 E1      AND     $E1             
6EEF: DD         ???                     
6EF0: DB         ???                     
6EF1: DA DB DD   JP      C,$DDDB         
6EF4: E1         POP     HL              
6EF5: E6 EB      AND     $EB             
6EF7: F2         ???                     
6EF8: F9         LD      SP,HL           
6EF9: E4         ???                     
6EFA: E5         PUSH    HL              
6EFB: E7         RST     0X20            
6EFC: E9         JP      (HL)            
6EFD: ED         ???                     
6EFE: F1         POP     AF              
6EFF: F6 FB      OR      $FB             
6F01: 00         NOP                     
6F02: 05         DEC     B               
6F03: 0A         LD      A,(BC)          
6F04: 0F         RRCA                    
6F05: 13         INC     DE              
6F06: 17         RLA                     
6F07: 19         ADD     HL,DE           
6F08: 1B         DEC     DE              
6F09: 1C         INC     E               
6F0A: 1B         DEC     DE              
6F0B: 19         ADD     HL,DE           
6F0C: 17         RLA                     
6F0D: 13         INC     DE              
6F0E: 0F         RRCA                    
6F0F: 0A         LD      A,(BC)          
6F10: 05         DEC     B               
6F11: 00         NOP                     
6F12: FB         EI                      
6F13: F6 F1      OR      $F1             
6F15: ED         ???                     
6F16: E9         JP      (HL)            
6F17: E7         RST     0X20            
6F18: E5         PUSH    HL              
6F19: E4         ???                     
6F1A: E5         PUSH    HL              
6F1B: E7         RST     0X20            
6F1C: E9         JP      (HL)            
6F1D: ED         ???                     
6F1E: F1         POP     AF              
6F1F: F6 FB      OR      $FB             
6F21: EE EF      XOR     $EF             
6F23: F0 F2      LD      A,($F2)         
6F25: F4         ???                     
6F26: F6 FA      OR      $FA             
6F28: FD         ???                     
6F29: 00         NOP                     
6F2A: 03         INC     BC              
6F2B: 06 0A      LD      B,$0A           
6F2D: 0C         INC     C               
6F2E: 0E 10      LD      C,$10           
6F30: 11 12 11   LD      DE,$1112        
6F33: 10 0E      STOP    $0E             
6F35: 0C         INC     C               
6F36: 0A         LD      A,(BC)          
6F37: 06 03      LD      B,$03           
6F39: 00         NOP                     
6F3A: FD         ???                     
6F3B: FA F6 F4   LD      A,($F4F6)       
6F3E: F2         ???                     
6F3F: F0 EF      LD      A,($EF)         
6F41: EE EF      XOR     $EF             
6F43: F0 F2      LD      A,($F2)         
6F45: F4         ???                     
6F46: F6 FA      OR      $FA             
6F48: FD         ???                     
6F49: F8 F9      LDHL    SP,$F9          
6F4B: FA FB FB   LD      A,($FBFB)       
6F4E: FC         ???                     
6F4F: FD         ???                     
6F50: FF         RST     0X38            
6F51: 00         NOP                     
6F52: 01 03 04   LD      BC,$0403        
6F55: 05         DEC     B               
6F56: 05         DEC     B               
6F57: 06 07      LD      B,$07           
6F59: 08 07 06   LD      ($0607),SP      
6F5C: 05         DEC     B               
6F5D: 05         DEC     B               
6F5E: 04         INC     B               
6F5F: 03         INC     BC              
6F60: 01 00 FF   LD      BC,$FF00        
6F63: FD         ???                     
6F64: FC         ???                     
6F65: FB         EI                      
6F66: FB         EI                      
6F67: FA F9 F8   LD      A,($F8F9)       
6F6A: F9         LD      SP,HL           
6F6B: FA FB FB   LD      A,($FBFB)       
6F6E: FC         ???                     
6F6F: FD         ???                     
6F70: FF         RST     0X38            
6F71: 00         NOP                     
6F72: 00         NOP                     
6F73: 01 02 03   LD      BC,$0302        
6F76: 04         INC     B               
6F77: 04         INC     B               
6F78: 04         INC     B               
6F79: 04         INC     B               
6F7A: 04         INC     B               
6F7B: 04         INC     B               
6F7C: 03         INC     BC              
6F7D: 02         LD      (BC),A          
6F7E: 01 00 00   LD      BC,$0000        
6F81: 00         NOP                     
6F82: 00         NOP                     
6F83: FF         RST     0X38            
6F84: FE FD      CP      $FD             
6F86: FC         ???                     
6F87: FC         ???                     
6F88: FC         ???                     
6F89: FC         ???                     
6F8A: FC         ???                     
6F8B: FC         ???                     
6F8C: FD         ???                     
6F8D: FE FF      CP      $FF             
6F8F: 00         NOP                     
6F90: 00         NOP                     
6F91: 00         NOP                     
6F92: 00         NOP                     
6F93: 01 01 02   LD      BC,$0201        
6F96: 02         LD      (BC),A          
6F97: 03         INC     BC              
6F98: 03         INC     BC              
6F99: 03         INC     BC              
6F9A: 03         INC     BC              
6F9B: 03         INC     BC              
6F9C: 02         LD      (BC),A          
6F9D: 02         LD      (BC),A          
6F9E: 01 01 00   LD      BC,$0001        
6FA1: 00         NOP                     
6FA2: 00         NOP                     
6FA3: FF         RST     0X38            
6FA4: FF         RST     0X38            
6FA5: FE FE      CP      $FE             
6FA7: FD         ???                     
6FA8: FD         ???                     
6FA9: FD         ???                     
6FAA: FD         ???                     
6FAB: FD         ???                     
6FAC: FE FE      CP      $FE             
6FAE: FF         RST     0X38            
6FAF: FF         RST     0X38            
6FB0: 00         NOP                     
6FB1: 00         NOP                     
6FB2: 00         NOP                     
6FB3: 01 01 01   LD      BC,$0101        
6FB6: 02         LD      (BC),A          
6FB7: 02         LD      (BC),A          
6FB8: 02         LD      (BC),A          
6FB9: 02         LD      (BC),A          
6FBA: 02         LD      (BC),A          
6FBB: 02         LD      (BC),A          
6FBC: 02         LD      (BC),A          
6FBD: 01 01 01   LD      BC,$0101        
6FC0: 00         NOP                     
6FC1: 00         NOP                     
6FC2: 00         NOP                     
6FC3: FF         RST     0X38            
6FC4: FF         RST     0X38            
6FC5: FF         RST     0X38            
6FC6: FE FE      CP      $FE             
6FC8: FE FE      CP      $FE             
6FCA: FE FE      CP      $FE             
6FCC: FE FF      CP      $FF             
6FCE: FF         RST     0X38            
6FCF: FF         RST     0X38            
6FD0: 00         NOP                     
6FD1: 00         NOP                     
6FD2: 00         NOP                     
6FD3: 01 01 01   LD      BC,$0101        
6FD6: 01 01 01   LD      BC,$0101        
6FD9: 01 01 01   LD      BC,$0101        
6FDC: 01 01 01   LD      BC,$0101        
6FDF: 00         NOP                     
6FE0: 00         NOP                     
6FE1: 00         NOP                     
6FE2: 00         NOP                     
6FE3: FF         RST     0X38            
6FE4: FF         RST     0X38            
6FE5: FF         RST     0X38            
6FE6: FF         RST     0X38            
6FE7: FF         RST     0X38            
6FE8: FF         RST     0X38            
6FE9: FF         RST     0X38            
6FEA: FF         RST     0X38            
6FEB: FF         RST     0X38            
6FEC: FF         RST     0X38            
6FED: FF         RST     0X38            
6FEE: FF         RST     0X38            
6FEF: 00         NOP                     
6FF0: 00         NOP                     
6FF1: 49         LD      C,C             
6FF2: 6F         LD      L,A             
6FF3: 21 6F F9   LD      HL,$F96F        
6FF6: 6E         LD      L,(HL)          
6FF7: D1         POP     DE              
6FF8: 6E         LD      L,(HL)          
6FF9: A9         XOR     C               
6FFA: 6E         LD      L,(HL)          
6FFB: 04         INC     B               
6FFC: 03         INC     BC              
6FFD: 02         LD      (BC),A          
6FFE: 01 30 70   LD      BC,$7030        
7001: 30 70      JR      NC,$7073        
7003: 10 10      STOP    $10             
7005: 80         ADD     A,B             
7006: 80         ADD     A,B             
7007: 00         NOP                     
7008: 00         NOP                     
7009: 01 01 CD   LD      BC,$CD01        
700C: 87         ADD     A,A             
700D: 08 FA 00   LD      ($00FA),SP      
7010: D2 A7 28   JP      NC,$28A7        
7013: 02         LD      (BC),A          
7014: 36 20      LD      (HL),$20        
7016: 7E         LD      A,(HL)          
7017: A7         AND     A               
7018: 20 57      JR      NZ,$7071        
701A: 36 2C      LD      (HL),$2C        
701C: 3E 5D      LD      A,$5D           
701E: CD 01 3C   CALL    $3C01           
7021: 38 4E      JR      C,$7071         
7023: 21 60 C3   LD      HL,$C360        
7026: 19         ADD     HL,DE           
7027: 36 FF      LD      (HL),$FF        
7029: 21 B0 C3   LD      HL,$C3B0        
702C: 19         ADD     HL,DE           
702D: 36 FF      LD      (HL),$FF        
702F: 21 B0 C2   LD      HL,$C2B0        
7032: 19         ADD     HL,DE           
7033: 36 01      LD      (HL),$01        
7035: 21 90 C2   LD      HL,$C290        
7038: 19         ADD     HL,DE           
7039: 36 01      LD      (HL),$01        
703B: C5         PUSH    BC              
703C: CD ED 27   CALL    $27ED           
703F: E6 03      AND     $03             
7041: 4F         LD      C,A             
7042: 21 FF 6F   LD      HL,$6FFF        
7045: 09         ADD     HL,BC           
7046: 7E         LD      A,(HL)          
7047: 21 00 C2   LD      HL,$C200        
704A: 19         ADD     HL,DE           
704B: 77         LD      (HL),A          
704C: 21 C0 C2   LD      HL,$C2C0        
704F: 19         ADD     HL,DE           
7050: 77         LD      (HL),A          
7051: 21 03 70   LD      HL,$7003        
7054: 09         ADD     HL,BC           
7055: 7E         LD      A,(HL)          
7056: 21 10 C2   LD      HL,$C210        
7059: 19         ADD     HL,DE           
705A: 77         LD      (HL),A          
705B: 21 D0 C2   LD      HL,$C2D0        
705E: 19         ADD     HL,DE           
705F: 77         LD      (HL),A          
7060: 21 E0 C2   LD      HL,$C2E0        
7063: 19         ADD     HL,DE           
7064: 36 5F      LD      (HL),$5F        
7066: 21 07 70   LD      HL,$7007        
7069: 09         ADD     HL,BC           
706A: 7E         LD      A,(HL)          
706B: 21 80 C3   LD      HL,$C380        
706E: 19         ADD     HL,DE           
706F: 77         LD      (HL),A          
7070: C1         POP     BC              
7071: CD 8C 08   CALL    $088C           
7074: 28 11      JR      Z,$7087         
7076: 1F         RRA                     
7077: 1F         RRA                     
7078: 1F         RRA                     
7079: E6 03      AND     $03             
707B: 5F         LD      E,A             
707C: 50         LD      D,B             
707D: 21 FB 6F   LD      HL,$6FFB        
7080: 19         ADD     HL,DE           
7081: 7E         LD      A,(HL)          
7082: 21 D0 C2   LD      HL,$C2D0        
7085: 09         ADD     HL,BC           
7086: 77         LD      (HL),A          
7087: 21 40 C4   LD      HL,$C440        
708A: 09         ADD     HL,BC           
708B: 7E         LD      A,(HL)          
708C: E6 07      AND     $07             
708E: 21 00 D2   LD      HL,$D200        
7091: B6         OR      (HL)            
7092: 20 14      JR      NZ,$70A8        
7094: F0 F0      LD      A,($F0)         
7096: FE 03      CP      $03             
7098: 20 0E      JR      NZ,$70A8        
709A: 21 90 C3   LD      HL,$C390        
709D: 09         ADD     HL,BC           
709E: 5E         LD      E,(HL)          
709F: 21 C0 C2   LD      HL,$C2C0        
70A2: 09         ADD     HL,BC           
70A3: 7E         LD      A,(HL)          
70A4: 83         ADD     A,E             
70A5: E6 1F      AND     $1F             
70A7: 77         LD      (HL),A          
70A8: FA 00 D2   LD      A,($D200)       
70AB: A7         AND     A               
70AC: 3E 00      LD      A,$00           
70AE: 20 0A      JR      NZ,$70BA        
70B0: 21 40 C4   LD      HL,$C440        
70B3: 09         ADD     HL,BC           
70B4: 34         INC     (HL)            
70B5: 7E         LD      A,(HL)          
70B6: 1F         RRA                     
70B7: 1F         RRA                     
70B8: E6 1F      AND     $1F             
70BA: E0 E8      LDFF00  ($E8),A         
70BC: 21 00 C2   LD      HL,$C200        
70BF: 09         ADD     HL,BC           
70C0: 36 50      LD      (HL),$50        
70C2: 21 10 C2   LD      HL,$C210        
70C5: 09         ADD     HL,BC           
70C6: 36 48      LD      (HL),$48        
70C8: F0 E8      LD      A,($E8)         
70CA: 5F         LD      E,A             
70CB: 50         LD      D,B             
70CC: 21 71 6F   LD      HL,$6F71        
70CF: 19         ADD     HL,DE           
70D0: 7E         LD      A,(HL)          
70D1: 21 C0 C2   LD      HL,$C2C0        
70D4: 09         ADD     HL,BC           
70D5: 86         ADD     A,(HL)          
70D6: E6 1F      AND     $1F             
70D8: 5F         LD      E,A             
70D9: 50         LD      D,B             
70DA: D5         PUSH    DE              
70DB: 21 D0 C2   LD      HL,$C2D0        
70DE: 09         ADD     HL,BC           
70DF: 5E         LD      E,(HL)          
70E0: CB 23      SET     1,E             
70E2: 50         LD      D,B             
70E3: 21 F1 6F   LD      HL,$6FF1        
70E6: 19         ADD     HL,DE           
70E7: 2A         LD      A,(HLI)         
70E8: 66         LD      H,(HL)          
70E9: 6F         LD      L,A             
70EA: D1         POP     DE              
70EB: 3E 02      LD      A,$02           
70ED: CD A3 71   CALL    $71A3           
70F0: F0 E8      LD      A,($E8)         
70F2: 5F         LD      E,A             
70F3: 50         LD      D,B             
70F4: 21 91 6F   LD      HL,$6F91        
70F7: 19         ADD     HL,DE           
70F8: 7E         LD      A,(HL)          
70F9: 21 C0 C2   LD      HL,$C2C0        
70FC: 09         ADD     HL,BC           
70FD: 86         ADD     A,(HL)          
70FE: E6 1F      AND     $1F             
7100: 5F         LD      E,A             
7101: 50         LD      D,B             
7102: D5         PUSH    DE              
7103: 21 D0 C2   LD      HL,$C2D0        
7106: 09         ADD     HL,BC           
7107: 5E         LD      E,(HL)          
7108: 1D         DEC     E               
7109: 7B         LD      A,E             
710A: FE F0      CP      $F0             
710C: D2 EA 71   JP      NC,$71EA        
710F: CB 23      SET     1,E             
7111: 50         LD      D,B             
7112: 21 F1 6F   LD      HL,$6FF1        
7115: 19         ADD     HL,DE           
7116: 2A         LD      A,(HLI)         
7117: 66         LD      H,(HL)          
7118: 6F         LD      L,A             
7119: D1         POP     DE              
711A: 3E 01      LD      A,$01           
711C: CD A3 71   CALL    $71A3           
711F: F0 E8      LD      A,($E8)         
7121: 5F         LD      E,A             
7122: 50         LD      D,B             
7123: 21 B1 6F   LD      HL,$6FB1        
7126: 19         ADD     HL,DE           
7127: 7E         LD      A,(HL)          
7128: 21 C0 C2   LD      HL,$C2C0        
712B: 09         ADD     HL,BC           
712C: 86         ADD     A,(HL)          
712D: E6 1F      AND     $1F             
712F: 5F         LD      E,A             
7130: 50         LD      D,B             
7131: D5         PUSH    DE              
7132: 21 D0 C2   LD      HL,$C2D0        
7135: 09         ADD     HL,BC           
7136: 5E         LD      E,(HL)          
7137: 1D         DEC     E               
7138: 1D         DEC     E               
7139: 7B         LD      A,E             
713A: FE F0      CP      $F0             
713C: D2 EA 71   JP      NC,$71EA        
713F: CB 23      SET     1,E             
7141: 50         LD      D,B             
7142: 21 F1 6F   LD      HL,$6FF1        
7145: 19         ADD     HL,DE           
7146: 2A         LD      A,(HLI)         
7147: 66         LD      H,(HL)          
7148: 6F         LD      L,A             
7149: D1         POP     DE              
714A: 3E 01      LD      A,$01           
714C: CD A3 71   CALL    $71A3           
714F: F0 E8      LD      A,($E8)         
7151: 5F         LD      E,A             
7152: 50         LD      D,B             
7153: 21 D1 6F   LD      HL,$6FD1        
7156: 19         ADD     HL,DE           
7157: 7E         LD      A,(HL)          
7158: 21 C0 C2   LD      HL,$C2C0        
715B: 09         ADD     HL,BC           
715C: 86         ADD     A,(HL)          
715D: E6 1F      AND     $1F             
715F: 5F         LD      E,A             
7160: 50         LD      D,B             
7161: D5         PUSH    DE              
7162: 21 D0 C2   LD      HL,$C2D0        
7165: 09         ADD     HL,BC           
7166: 5E         LD      E,(HL)          
7167: 1D         DEC     E               
7168: 1D         DEC     E               
7169: 1D         DEC     E               
716A: 7B         LD      A,E             
716B: FE F0      CP      $F0             
716D: D2 EA 71   JP      NC,$71EA        
7170: CB 23      SET     1,E             
7172: 50         LD      D,B             
7173: 21 F1 6F   LD      HL,$6FF1        
7176: 19         ADD     HL,DE           
7177: 2A         LD      A,(HLI)         
7178: 66         LD      H,(HL)          
7179: 6F         LD      L,A             
717A: D1         POP     DE              
717B: 3E 01      LD      A,$01           
717D: CD A3 71   CALL    $71A3           
7180: 21 C0 C2   LD      HL,$C2C0        
7183: 09         ADD     HL,BC           
7184: 5E         LD      E,(HL)          
7185: 50         LD      D,B             
7186: D5         PUSH    DE              
7187: 21 D0 C2   LD      HL,$C2D0        
718A: 09         ADD     HL,BC           
718B: 5E         LD      E,(HL)          
718C: 1D         DEC     E               
718D: 1D         DEC     E               
718E: 1D         DEC     E               
718F: 1D         DEC     E               
7190: 7B         LD      A,E             
7191: FE F0      CP      $F0             
7193: D2 EA 71   JP      NC,$71EA        
7196: CB 23      SET     1,E             
7198: 50         LD      D,B             
7199: 21 F1 6F   LD      HL,$6FF1        
719C: 19         ADD     HL,DE           
719D: 2A         LD      A,(HLI)         
719E: 66         LD      H,(HL)          
719F: 6F         LD      L,A             
71A0: D1         POP     DE              
71A1: 3E 00      LD      A,$00           
71A3: E0 F1      LDFF00  ($F1),A         
71A5: 19         ADD     HL,DE           
71A6: 3E 48      LD      A,$48           
71A8: 86         ADD     A,(HL)          
71A9: E0 EC      LDFF00  ($EC),A         
71AB: 7D         LD      A,L             
71AC: C6 08      ADD     $08             
71AE: 6F         LD      L,A             
71AF: 7C         LD      A,H             
71B0: CE 00      ADC     $00             
71B2: 67         LD      H,A             
71B3: 3E 50      LD      A,$50           
71B5: 86         ADD     A,(HL)          
71B6: E0 EE      LDFF00  ($EE),A         
71B8: CD 00 72   CALL    $7200           
71BB: F0 98      LD      A,($98)         
71BD: 21 EE FF   LD      HL,$FFEE        
71C0: 96         SUB     (HL)            
71C1: C6 08      ADD     $08             
71C3: FE 10      CP      $10             
71C5: 30 22      JR      NC,$71E9        
71C7: F0 99      LD      A,($99)         
71C9: 21 EC FF   LD      HL,$FFEC        
71CC: 96         SUB     (HL)            
71CD: C6 08      ADD     $08             
71CF: FE 10      CP      $10             
71D1: 30 16      JR      NC,$71E9        
71D3: FA 1C C1   LD      A,($C11C)       
71D6: A7         AND     A               
71D7: 20 10      JR      NZ,$71E9        
71D9: CD 93 3B   CALL    $3B93           
71DC: 3E 18      LD      A,$18           
71DE: CD 30 3C   CALL    $3C30           
71E1: F0 D7      LD      A,($D7)         
71E3: E0 9B      LDFF00  ($9B),A         
71E5: F0 D8      LD      A,($D8)         
71E7: E0 9A      LDFF00  ($9A),A         
71E9: C9         RET                     
71EA: D1         POP     DE              
71EB: C9         RET                     
71EC: 70         LD      (HL),B          
71ED: 00         NOP                     
71EE: 70         LD      (HL),B          
71EF: 20 72      JR      NZ,$7263        
71F1: 00         NOP                     
71F2: 72         LD      (HL),D          
71F3: 20 74      JR      NZ,$7269        
71F5: 00         NOP                     
71F6: 74         LD      (HL),H          
71F7: 20 7C      JR      NZ,$7275        
71F9: 00         NOP                     
71FA: 7C         LD      A,H             
71FB: 20 7E      JR      NZ,$727B        
71FD: 00         NOP                     
71FE: 7E         LD      A,(HL)          
71FF: 20 11      JR      NZ,$7212        
7201: EC         ???                     
7202: 71         LD      (HL),C          
7203: CD 3B 3C   CALL    $3C3B           
7206: C9         RET                     
7207: CD AC 78   CALL    $78AC           
720A: CD 65 79   CALL    $7965           
720D: F0 F0      LD      A,($F0)         
720F: C7         RST     0X00            
7210: 26 72      LD      H,$72           
7212: 85         ADD     A,L             
7213: 72         LD      (HL),D          
7214: 48         LD      C,B             
7215: 73         LD      (HL),E          
7216: D5         PUSH    DE              
7217: 73         LD      (HL),E          
7218: 60         LD      H,B             
7219: 74         LD      (HL),H          
721A: 09         ADD     HL,BC           
721B: 0A         LD      A,(BC)          
721C: 0B         DEC     BC              
721D: 0B         DEC     BC              
721E: 0B         DEC     BC              
721F: 0B         DEC     BC              
7220: 0C         INC     C               
7221: 0D         DEC     C               
7222: 0E 0E      LD      C,$0E           
7224: 0E 0E      LD      C,$0E           
7226: CD 91 08   CALL    $0891           
7229: CA 59 74   JP      Z,$7459         
722C: 5F         LD      E,A             
722D: FE 18      CP      $18             
722F: 20 04      JR      NZ,$7235        
7231: 3E 16      LD      A,$16           
7233: E0 F3      LDFF00  ($F3),A         
7235: 7B         LD      A,E             
7236: 1F         RRA                     
7237: 1F         RRA                     
7238: 1F         RRA                     
7239: E6 07      AND     $07             
723B: 5F         LD      E,A             
723C: 50         LD      D,B             
723D: 21 80 C3   LD      HL,$C380        
7240: 09         ADD     HL,BC           
7241: 7E         LD      A,(HL)          
7242: A7         AND     A               
7243: 21 1A 72   LD      HL,$721A        
7246: 28 03      JR      Z,$724B         
7248: 21 20 72   LD      HL,$7220        
724B: 19         ADD     HL,DE           
724C: 7E         LD      A,(HL)          
724D: CD 87 3B   CALL    $3B87           
7250: C9         RET                     
7251: 09         ADD     HL,BC           
7252: 09         ADD     HL,BC           
7253: 0A         LD      A,(BC)          
7254: 0A         LD      A,(BC)          
7255: 0B         DEC     BC              
7256: 0B         DEC     BC              
7257: 0B         DEC     BC              
7258: 0B         DEC     BC              
7259: 0B         DEC     BC              
725A: 0B         DEC     BC              
725B: 0B         DEC     BC              
725C: 0B         DEC     BC              
725D: 0A         LD      A,(BC)          
725E: 0A         LD      A,(BC)          
725F: 09         ADD     HL,BC           
7260: 09         ADD     HL,BC           
7261: 09         ADD     HL,BC           
7262: 09         ADD     HL,BC           
7263: 09         ADD     HL,BC           
7264: 09         ADD     HL,BC           
7265: 09         ADD     HL,BC           
7266: 09         ADD     HL,BC           
7267: 09         ADD     HL,BC           
7268: 09         ADD     HL,BC           
7269: 0C         INC     C               
726A: 0C         INC     C               
726B: 0D         DEC     C               
726C: 0D         DEC     C               
726D: 0E 0E      LD      C,$0E           
726F: 0E 0E      LD      C,$0E           
7271: 0E 0E      LD      C,$0E           
7273: 0E 0E      LD      C,$0E           
7275: 0D         DEC     C               
7276: 0D         DEC     C               
7277: 0C         INC     C               
7278: 0C         INC     C               
7279: 0C         INC     C               
727A: 0C         INC     C               
727B: 0C         INC     C               
727C: 0C         INC     C               
727D: 0C         INC     C               
727E: 0C         INC     C               
727F: 0C         INC     C               
7280: 0C         INC     C               
7281: 18 D8      JR      $725B           
7283: 04         INC     B               
7284: 0C         INC     C               
7285: CD 91 08   CALL    $0891           
7288: CA 59 74   JP      Z,$7459         
728B: 5F         LD      E,A             
728C: FE 20      CP      $20             
728E: 20 04      JR      NZ,$7294        
7290: 3E 16      LD      A,$16           
7292: E0 F3      LDFF00  ($F3),A         
7294: 7B         LD      A,E             
7295: 1F         RRA                     
7296: 1F         RRA                     
7297: E6 1F      AND     $1F             
7299: 5F         LD      E,A             
729A: 50         LD      D,B             
729B: 21 80 C3   LD      HL,$C380        
729E: 09         ADD     HL,BC           
729F: 7E         LD      A,(HL)          
72A0: A7         AND     A               
72A1: 21 51 72   LD      HL,$7251        
72A4: 28 03      JR      Z,$72A9         
72A6: 21 69 72   LD      HL,$7269        
72A9: 19         ADD     HL,DE           
72AA: 7E         LD      A,(HL)          
72AB: CD 87 3B   CALL    $3B87           
72AE: FE 0B      CP      $0B             
72B0: 28 05      JR      Z,$72B7         
72B2: FE 0E      CP      $0E             
72B4: C2 47 73   JP      NZ,$7347        
72B7: F0 9E      LD      A,($9E)         
72B9: E6 02      AND     $02             
72BB: CA 47 73   JP      Z,$7347         
72BE: FA A6 C1   LD      A,($C1A6)       
72C1: A7         AND     A               
72C2: CA 47 73   JP      Z,$7347         
72C5: 3D         DEC     A               
72C6: EA 02 D2   LD      ($D202),A       
72C9: 5F         LD      E,A             
72CA: 50         LD      D,B             
72CB: 21 80 C2   LD      HL,$C280        
72CE: 19         ADD     HL,DE           
72CF: 7E         LD      A,(HL)          
72D0: A7         AND     A               
72D1: 28 74      JR      Z,$7347         
72D3: 21 A0 C3   LD      HL,$C3A0        
72D6: 19         ADD     HL,DE           
72D7: 7E         LD      A,(HL)          
72D8: FE 03      CP      $03             
72DA: 20 6B      JR      NZ,$7347        
72DC: 21 00 C2   LD      HL,$C200        
72DF: 19         ADD     HL,DE           
72E0: F0 EE      LD      A,($EE)         
72E2: 96         SUB     (HL)            
72E3: C6 08      ADD     $08             
72E5: FE 10      CP      $10             
72E7: 30 5E      JR      NC,$7347        
72E9: 21 10 C2   LD      HL,$C210        
72EC: 19         ADD     HL,DE           
72ED: F0 EC      LD      A,($EC)         
72EF: 96         SUB     (HL)            
72F0: C6 0C      ADD     $0C             
72F2: FE 18      CP      $18             
72F4: 30 51      JR      NC,$7347        
72F6: FA 03 D2   LD      A,($D203)       
72F9: 3C         INC     A               
72FA: EA 03 D2   LD      ($D203),A       
72FD: FE 04      CP      $04             
72FF: 38 36      JR      C,$7337         
7301: CD ED 27   CALL    $27ED           
7304: E6 01      AND     $01             
7306: 20 2F      JR      NZ,$7337        
7308: 21 B0 C2   LD      HL,$C2B0        
730B: 09         ADD     HL,BC           
730C: 36 02      LD      (HL),$02        
730E: CD 87 08   CALL    $0887           
7311: 36 30      LD      (HL),$30        
7313: 21 00 C3   LD      HL,$C300        
7316: 09         ADD     HL,BC           
7317: 36 20      LD      (HL),$20        
7319: 21 80 C3   LD      HL,$C380        
731C: 09         ADD     HL,BC           
731D: 5E         LD      E,(HL)          
731E: 50         LD      D,B             
731F: 21 81 72   LD      HL,$7281        
7322: 19         ADD     HL,DE           
7323: 7E         LD      A,(HL)          
7324: 21 50 C2   LD      HL,$C250        
7327: 09         ADD     HL,BC           
7328: 77         LD      (HL),A          
7329: 21 83 72   LD      HL,$7283        
732C: 19         ADD     HL,DE           
732D: 7E         LD      A,(HL)          
732E: 21 90 C2   LD      HL,$C290        
7331: 09         ADD     HL,BC           
7332: 77         LD      (HL),A          
7333: CD A1 76   CALL    $76A1           
7336: C9         RET                     
7337: CD 8D 3B   CALL    $3B8D           
733A: FA 01 D2   LD      A,($D201)       
733D: 5F         LD      E,A             
733E: 50         LD      D,B             
733F: 21 90 C3   LD      HL,$C390        
7342: 19         ADD     HL,DE           
7343: 7E         LD      A,(HL)          
7344: 2F         CPL                     
7345: 3C         INC     A               
7346: 77         LD      (HL),A          
7347: C9         RET                     
7348: CD D2 78   CALL    $78D2           
734B: 3E 01      LD      A,$01           
734D: EA 00 D2   LD      ($D200),A       
7350: FA 02 D2   LD      A,($D202)       
7353: 5F         LD      E,A             
7354: 50         LD      D,B             
7355: 21 80 C2   LD      HL,$C280        
7358: 19         ADD     HL,DE           
7359: 7E         LD      A,(HL)          
735A: A7         AND     A               
735B: 28 3F      JR      Z,$739C         
735D: FA C7 DB   LD      A,($DBC7)       
7360: A7         AND     A               
7361: 20 39      JR      NZ,$739C        
7363: 21 10 C2   LD      HL,$C210        
7366: 19         ADD     HL,DE           
7367: 7E         LD      A,(HL)          
7368: 21 10 C2   LD      HL,$C210        
736B: 09         ADD     HL,BC           
736C: 77         LD      (HL),A          
736D: FA 01 D2   LD      A,($D201)       
7370: 5F         LD      E,A             
7371: 50         LD      D,B             
7372: 21 D0 C2   LD      HL,$C2D0        
7375: 19         ADD     HL,DE           
7376: 7E         LD      A,(HL)          
7377: FE 00      CP      $00             
7379: 28 07      JR      Z,$7382         
737B: F0 E7      LD      A,($E7)         
737D: E6 03      AND     $03             
737F: 20 01      JR      NZ,$7382        
7381: 35         DEC     (HL)            
7382: F0 E7      LD      A,($E7)         
7384: E6 07      AND     $07             
7386: 20 04      JR      NZ,$738C        
7388: 3E 29      LD      A,$29           
738A: E0 F2      LDFF00  ($F2),A         
738C: 21 80 C3   LD      HL,$C380        
738F: 09         ADD     HL,BC           
7390: 7E         LD      A,(HL)          
7391: A7         AND     A               
7392: 3E 00      LD      A,$00           
7394: 28 02      JR      Z,$7398         
7396: 3E 01      LD      A,$01           
7398: CD 87 3B   CALL    $3B87           
739B: C9         RET                     
739C: CD 8D 3B   CALL    $3B8D           
739F: CD 91 08   CALL    $0891           
73A2: 36 5F      LD      (HL),$5F        
73A4: C9         RET                     
73A5: 10 10      STOP    $10             
73A7: 0C         INC     C               
73A8: 08 04 03   LD      ($0304),SP      
73AB: 02         LD      (BC),A          
73AC: 01 01 01   LD      BC,$0101        
73AF: 01 01 01   LD      BC,$0101        
73B2: 01 01 01   LD      BC,$0101        
73B5: 01 01 01   LD      BC,$0101        
73B8: 01 01 01   LD      BC,$0101        
73BB: 01 01 03   LD      BC,$0301        
73BE: 1F         RRA                     
73BF: 1F         RRA                     
73C0: 3F         CCF                     
73C1: 3F         CCF                     
73C2: 3F         CCF                     
73C3: 3F         CCF                     
73C4: 3F         CCF                     
73C5: 3F         CCF                     
73C6: 3F         CCF                     
73C7: 3F         CCF                     
73C8: 3F         CCF                     
73C9: 3F         CCF                     
73CA: 3F         CCF                     
73CB: 3F         CCF                     
73CC: 3F         CCF                     
73CD: 3F         CCF                     
73CE: 3F         CCF                     
73CF: 3F         CCF                     
73D0: 3F         CCF                     
73D1: 3F         CCF                     
73D2: 3F         CCF                     
73D3: 3F         CCF                     
73D4: 3F         CCF                     
73D5: CD D2 78   CALL    $78D2           
73D8: 3E 01      LD      A,$01           
73DA: EA 00 D2   LD      ($D200),A       
73DD: 21 80 C3   LD      HL,$C380        
73E0: 09         ADD     HL,BC           
73E1: 7E         LD      A,(HL)          
73E2: A7         AND     A               
73E3: 3E 08      LD      A,$08           
73E5: 28 02      JR      Z,$73E9         
73E7: 3E 0F      LD      A,$0F           
73E9: CD 87 3B   CALL    $3B87           
73EC: F0 98      LD      A,($98)         
73EE: F5         PUSH    AF              
73EF: 21 C0 C2   LD      HL,$C2C0        
73F2: 09         ADD     HL,BC           
73F3: 7E         LD      A,(HL)          
73F4: E0 98      LDFF00  ($98),A         
73F6: F0 99      LD      A,($99)         
73F8: F5         PUSH    AF              
73F9: 21 D0 C2   LD      HL,$C2D0        
73FC: 09         ADD     HL,BC           
73FD: 7E         LD      A,(HL)          
73FE: E0 99      LDFF00  ($99),A         
7400: CD 91 08   CALL    $0891           
7403: 1F         RRA                     
7404: 1F         RRA                     
7405: E6 3F      AND     $3F             
7407: 5F         LD      E,A             
7408: 50         LD      D,B             
7409: 21 A5 73   LD      HL,$73A5        
740C: 19         ADD     HL,DE           
740D: 7E         LD      A,(HL)          
740E: CD 30 3C   CALL    $3C30           
7411: F0 D8      LD      A,($D8)         
7413: 21 40 C2   LD      HL,$C240        
7416: 09         ADD     HL,BC           
7417: 77         LD      (HL),A          
7418: F0 D7      LD      A,($D7)         
741A: 21 50 C2   LD      HL,$C250        
741D: 09         ADD     HL,BC           
741E: 77         LD      (HL),A          
741F: CD D1 79   CALL    $79D1           
7422: F0 99      LD      A,($99)         
7424: 21 EC FF   LD      HL,$FFEC        
7427: 96         SUB     (HL)            
7428: C6 03      ADD     $03             
742A: FE 06      CP      $06             
742C: 30 03      JR      NC,$7431        
742E: CD 59 74   CALL    $7459           
7431: F1         POP     AF              
7432: E0 99      LDFF00  ($99),A         
7434: F1         POP     AF              
7435: E0 98      LDFF00  ($98),A         
7437: CD 91 08   CALL    $0891           
743A: 1F         RRA                     
743B: 1F         RRA                     
743C: E6 3F      AND     $3F             
743E: 5F         LD      E,A             
743F: 50         LD      D,B             
7440: 21 BD 73   LD      HL,$73BD        
7443: 19         ADD     HL,DE           
7444: F0 E7      LD      A,($E7)         
7446: A6         AND     (HL)            
7447: 20 0F      JR      NZ,$7458        
7449: FA 01 D2   LD      A,($D201)       
744C: 5F         LD      E,A             
744D: 50         LD      D,B             
744E: 21 D0 C2   LD      HL,$C2D0        
7451: 19         ADD     HL,DE           
7452: 7E         LD      A,(HL)          
7453: FE 04      CP      $04             
7455: 28 01      JR      Z,$7458         
7457: 34         INC     (HL)            
7458: C9         RET                     
7459: AF         XOR     A               
745A: EA 00 D2   LD      ($D200),A       
745D: C3 6B 7A   JP      $7A6B           
7460: CD D2 78   CALL    $78D2           
7463: CD 91 08   CALL    $0891           
7466: CA AD 74   JP      Z,$74AD         
7469: 21 20 C4   LD      HL,$C420        
746C: 09         ADD     HL,BC           
746D: 77         LD      (HL),A          
746E: FE 80      CP      $80             
7470: 30 03      JR      NC,$7475        
7472: CD 76 74   CALL    $7476           
7475: C9         RET                     
7476: E6 07      AND     $07             
7478: 20 1D      JR      NZ,$7497        
747A: CD ED 27   CALL    $27ED           
747D: E6 1F      AND     $1F             
747F: D6 10      SUB     $10             
7481: 5F         LD      E,A             
7482: 21 EE FF   LD      HL,$FFEE        
7485: 86         ADD     A,(HL)          
7486: 77         LD      (HL),A          
7487: CD ED 27   CALL    $27ED           
748A: E6 1F      AND     $1F             
748C: D6 10      SUB     $10             
748E: 5F         LD      E,A             
748F: 21 EC FF   LD      HL,$FFEC        
7492: 86         ADD     A,(HL)          
7493: 77         LD      (HL),A          
7494: CD 98 74   CALL    $7498           
7497: C9         RET                     
7498: CD 6B 79   CALL    $796B           
749B: F0 EE      LD      A,($EE)         
749D: E0 D7      LDFF00  ($D7),A         
749F: F0 EC      LD      A,($EC)         
74A1: E0 D8      LDFF00  ($D8),A         
74A3: 3E 02      LD      A,$02           
74A5: CD 53 09   CALL    $0953           
74A8: 3E 13      LD      A,$13           
74AA: E0 F4      LDFF00  ($F4),A         
74AC: C9         RET                     
74AD: 3E 36      LD      A,$36           
74AF: CD 01 3C   CALL    $3C01           
74B2: 18 0D      JR      $74C1           
74B4: 3E 36      LD      A,$36           
74B6: CD 01 3C   CALL    $3C01           
74B9: 3E 48      LD      A,$48           
74BB: E0 D7      LDFF00  ($D7),A         
74BD: 3E 10      LD      A,$10           
74BF: E0 D8      LDFF00  ($D8),A         
74C1: F0 D8      LD      A,($D8)         
74C3: 21 10 C2   LD      HL,$C210        
74C6: 19         ADD     HL,DE           
74C7: 77         LD      (HL),A          
74C8: F0 D7      LD      A,($D7)         
74CA: 21 00 C2   LD      HL,$C200        
74CD: 19         ADD     HL,DE           
74CE: 77         LD      (HL),A          
74CF: F0 F9      LD      A,($F9)         
74D1: A7         AND     A               
74D2: 28 08      JR      Z,$74DC         
74D4: 21 50 C2   LD      HL,$C250        
74D7: 09         ADD     HL,BC           
74D8: 36 F0      LD      (HL),$F0        
74DA: 18 0C      JR      $74E8           
74DC: 21 20 C3   LD      HL,$C320        
74DF: 19         ADD     HL,DE           
74E0: 36 10      LD      (HL),$10        
74E2: 21 10 C3   LD      HL,$C310        
74E5: 19         ADD     HL,DE           
74E6: 36 08      LD      (HL),$08        
74E8: CD 6B 7A   CALL    $7A6B           
74EB: 21 F4 FF   LD      HL,$FFF4        
74EE: 36 1A      LD      (HL),$1A        
74F0: C9         RET                     
74F1: 03         INC     BC              
74F2: 05         DEC     B               
74F3: 00         NOP                     
74F4: 04         INC     B               
74F5: 02         LD      (BC),A          
74F6: 06 01      LD      B,$01           
74F8: 07         RLCA                    
74F9: CD 97 75   CALL    $7597           
74FC: CD BA 3D   CALL    $3DBA           
74FF: CD 65 79   CALL    $7965           
7502: 3E 01      LD      A,$01           
7504: EA 00 D2   LD      ($D200),A       
7507: CD 87 08   CALL    $0887           
750A: FE 10      CP      $10             
750C: 30 3B      JR      NC,$7549        
750E: A7         AND     A               
750F: 20 30      JR      NZ,$7541        
7511: FA 01 D2   LD      A,($D201)       
7514: 5F         LD      E,A             
7515: 50         LD      D,B             
7516: 21 F0 C2   LD      HL,$C2F0        
7519: 19         ADD     HL,DE           
751A: 36 1F      LD      (HL),$1F        
751C: 3E 02      LD      A,$02           
751E: CD 01 3C   CALL    $3C01           
7521: CD D7 08   CALL    $08D7           
7524: F0 D7      LD      A,($D7)         
7526: 21 00 C2   LD      HL,$C200        
7529: 19         ADD     HL,DE           
752A: 77         LD      (HL),A          
752B: F0 D8      LD      A,($D8)         
752D: 21 10 C2   LD      HL,$C210        
7530: 19         ADD     HL,DE           
7531: 77         LD      (HL),A          
7532: 21 E0 C2   LD      HL,$C2E0        
7535: 19         ADD     HL,DE           
7536: 36 17      LD      (HL),$17        
7538: 21 40 C4   LD      HL,$C440        
753B: 19         ADD     HL,DE           
753C: 36 01      LD      (HL),$01        
753E: C3 59 74   JP      $7459           
7541: F0 E7      LD      A,($E7)         
7543: 21 20 C4   LD      HL,$C420        
7546: 09         ADD     HL,BC           
7547: 77         LD      (HL),A          
7548: C9         RET                     
7549: F0 E7      LD      A,($E7)         
754B: E6 07      AND     $07             
754D: 20 0E      JR      NZ,$755D        
754F: FA 01 D2   LD      A,($D201)       
7552: 5F         LD      E,A             
7553: 50         LD      D,B             
7554: 21 D0 C2   LD      HL,$C2D0        
7557: 19         ADD     HL,DE           
7558: 7E         LD      A,(HL)          
7559: A7         AND     A               
755A: 28 01      JR      Z,$755D         
755C: 35         DEC     (HL)            
755D: 21 D0 C3   LD      HL,$C3D0        
7560: 09         ADD     HL,BC           
7561: 7E         LD      A,(HL)          
7562: 3C         INC     A               
7563: E6 7F      AND     $7F             
7565: 77         LD      (HL),A          
7566: 5F         LD      E,A             
7567: 50         LD      D,B             
7568: 21 00 D0   LD      HL,$D000        
756B: 19         ADD     HL,DE           
756C: F0 EE      LD      A,($EE)         
756E: 77         LD      (HL),A          
756F: 21 00 D1   LD      HL,$D100        
7572: 19         ADD     HL,DE           
7573: F0 EC      LD      A,($EC)         
7575: 77         LD      (HL),A          
7576: 21 00 C3   LD      HL,$C300        
7579: 09         ADD     HL,BC           
757A: 7E         LD      A,(HL)          
757B: A7         AND     A               
757C: 28 05      JR      Z,$7583         
757E: CD D1 79   CALL    $79D1           
7581: 18 03      JR      $7586           
7583: CD 2C 76   CALL    $762C           
7586: 21 90 C2   LD      HL,$C290        
7589: 09         ADD     HL,BC           
758A: 5E         LD      E,(HL)          
758B: CB 3B      SET     1,E             
758D: 50         LD      D,B             
758E: 21 F1 74   LD      HL,$74F1        
7591: 19         ADD     HL,DE           
7592: 7E         LD      A,(HL)          
7593: CD 87 3B   CALL    $3B87           
7596: C9         RET                     
7597: F0 F1      LD      A,($F1)         
7599: 17         RLA                     
759A: 17         RLA                     
759B: 17         RLA                     
759C: 17         RLA                     
759D: 17         RLA                     
759E: E6 E0      AND     $E0             
75A0: 5F         LD      E,A             
75A1: 50         LD      D,B             
75A2: 21 AC 76   LD      HL,$76AC        
75A5: 19         ADD     HL,DE           
75A6: 0E 08      LD      C,$08           
75A8: CD 26 3D   CALL    $3D26           
75AB: 3E 08      LD      A,$08           
75AD: CD D0 3D   CALL    $3DD0           
75B0: 21 D0 C3   LD      HL,$C3D0        
75B3: 09         ADD     HL,BC           
75B4: 7E         LD      A,(HL)          
75B5: E0 D7      LDFF00  ($D7),A         
75B7: F0 D7      LD      A,($D7)         
75B9: D6 0C      SUB     $0C             
75BB: E6 7F      AND     $7F             
75BD: 5F         LD      E,A             
75BE: 50         LD      D,B             
75BF: 21 00 D0   LD      HL,$D000        
75C2: 19         ADD     HL,DE           
75C3: 7E         LD      A,(HL)          
75C4: E0 EE      LDFF00  ($EE),A         
75C6: 21 00 D1   LD      HL,$D100        
75C9: 19         ADD     HL,DE           
75CA: 7E         LD      A,(HL)          
75CB: E0 EC      LDFF00  ($EC),A         
75CD: 3E 00      LD      A,$00           
75CF: E0 F1      LDFF00  ($F1),A         
75D1: 11 EC 71   LD      DE,$71EC        
75D4: CD 3B 3C   CALL    $3C3B           
75D7: F0 D7      LD      A,($D7)         
75D9: D6 18      SUB     $18             
75DB: E6 7F      AND     $7F             
75DD: 5F         LD      E,A             
75DE: 50         LD      D,B             
75DF: 21 00 D0   LD      HL,$D000        
75E2: 19         ADD     HL,DE           
75E3: 7E         LD      A,(HL)          
75E4: E0 EE      LDFF00  ($EE),A         
75E6: 21 00 D1   LD      HL,$D100        
75E9: 19         ADD     HL,DE           
75EA: 7E         LD      A,(HL)          
75EB: E0 EC      LDFF00  ($EC),A         
75ED: 3E 00      LD      A,$00           
75EF: E0 F1      LDFF00  ($F1),A         
75F1: 11 EC 71   LD      DE,$71EC        
75F4: CD 3B 3C   CALL    $3C3B           
75F7: F0 D7      LD      A,($D7)         
75F9: D6 24      SUB     $24             
75FB: E6 7F      AND     $7F             
75FD: 5F         LD      E,A             
75FE: 50         LD      D,B             
75FF: 21 00 D0   LD      HL,$D000        
7602: 19         ADD     HL,DE           
7603: 7E         LD      A,(HL)          
7604: E0 EE      LDFF00  ($EE),A         
7606: 21 00 D1   LD      HL,$D100        
7609: 19         ADD     HL,DE           
760A: 7E         LD      A,(HL)          
760B: E0 EC      LDFF00  ($EC),A         
760D: 3E 02      LD      A,$02           
760F: E0 F1      LDFF00  ($F1),A         
7611: 11 EC 71   LD      DE,$71EC        
7614: CD 3B 3C   CALL    $3C3B           
7617: C9         RET                     
7618: 00         NOP                     
7619: 06 0C      LD      B,$0C           
761B: 0E 10      LD      C,$10           
761D: 0E 0C      LD      C,$0C           
761F: 06 00      LD      B,$00           
7621: FA F4 F2   LD      A,($F2F4)       
7624: F0 F2      LD      A,($F2)         
7626: F4         ???                     
7627: FA 00 06   LD      A,($0600)       
762A: 0C         INC     C               
762B: 0E CD      LD      C,$CD           
762D: D1         POP     DE              
762E: 79         LD      A,C             
762F: CD BF 3B   CALL    $3BBF           
7632: CD 9E 3B   CALL    $3B9E           
7635: 21 A0 C2   LD      HL,$C2A0        
7638: 09         ADD     HL,BC           
7639: 7E         LD      A,(HL)          
763A: A7         AND     A               
763B: 28 1D      JR      Z,$765A         
763D: CD ED 27   CALL    $27ED           
7640: 1F         RRA                     
7641: 38 08      JR      C,$764B         
7643: 21 C0 C2   LD      HL,$C2C0        
7646: 09         ADD     HL,BC           
7647: 7E         LD      A,(HL)          
7648: 2F         CPL                     
7649: 3C         INC     A               
764A: 77         LD      (HL),A          
764B: 21 90 C2   LD      HL,$C290        
764E: 09         ADD     HL,BC           
764F: 7E         LD      A,(HL)          
7650: C6 08      ADD     $08             
7652: E6 0F      AND     $0F             
7654: 77         LD      (HL),A          
7655: CD 91 08   CALL    $0891           
7658: 36 10      LD      (HL),$10        
765A: CD 8C 08   CALL    $088C           
765D: 20 29      JR      NZ,$7688        
765F: 36 04      LD      (HL),$04        
7661: 21 C0 C2   LD      HL,$C2C0        
7664: 09         ADD     HL,BC           
7665: 7E         LD      A,(HL)          
7666: 21 90 C2   LD      HL,$C290        
7669: 09         ADD     HL,BC           
766A: 86         ADD     A,(HL)          
766B: E6 0F      AND     $0F             
766D: 77         LD      (HL),A          
766E: 21 90 C2   LD      HL,$C290        
7671: 09         ADD     HL,BC           
7672: 5E         LD      E,(HL)          
7673: 50         LD      D,B             
7674: 21 18 76   LD      HL,$7618        
7677: 19         ADD     HL,DE           
7678: 7E         LD      A,(HL)          
7679: 21 50 C2   LD      HL,$C250        
767C: 09         ADD     HL,BC           
767D: 77         LD      (HL),A          
767E: 21 1C 76   LD      HL,$761C        
7681: 19         ADD     HL,DE           
7682: 7E         LD      A,(HL)          
7683: 21 40 C2   LD      HL,$C240        
7686: 09         ADD     HL,BC           
7687: 77         LD      (HL),A          
7688: CD 91 08   CALL    $0891           
768B: 20 13      JR      NZ,$76A0        
768D: CD ED 27   CALL    $27ED           
7690: E6 1F      AND     $1F             
7692: C6 10      ADD     $10             
7694: 77         LD      (HL),A          
7695: CD ED 27   CALL    $27ED           
7698: E6 02      AND     $02             
769A: 3D         DEC     A               
769B: 21 C0 C2   LD      HL,$C2C0        
769E: 09         ADD     HL,BC           
769F: 77         LD      (HL),A          
76A0: C9         RET                     
76A1: 1E 80      LD      E,$80           
76A3: 21 00 D1   LD      HL,$D100        
76A6: AF         XOR     A               
76A7: 22         LD      (HLI),A         
76A8: 1D         DEC     E               
76A9: 20 FB      JR      NZ,$76A6        
76AB: C9         RET                     
76AC: F8 F8      LDHL    SP,$F8          
76AE: 60         LD      H,B             
76AF: 00         NOP                     
76B0: F8 00      LDHL    SP,$00          
76B2: 62         LD      H,D             
76B3: 00         NOP                     
76B4: F8 08      LDHL    SP,$08          
76B6: 62         LD      H,D             
76B7: 20 F8      JR      NZ,$76B1        
76B9: 10 60      STOP    $60             
76BB: 20 08      JR      NZ,$76C5        
76BD: F8 64      LDHL    SP,$64          
76BF: 00         NOP                     
76C0: 08 00 66   LD      ($6600),SP      
76C3: 00         NOP                     
76C4: 08 08 66   LD      ($6608),SP      
76C7: 20 08      JR      NZ,$76D1        
76C9: 10 64      STOP    $64             
76CB: 20 F8      JR      NZ,$76C5        
76CD: F8 64      LDHL    SP,$64          
76CF: 40         LD      B,B             
76D0: F8 00      LDHL    SP,$00          
76D2: 66         LD      H,(HL)          
76D3: 40         LD      B,B             
76D4: F8 08      LDHL    SP,$08          
76D6: 66         LD      H,(HL)          
76D7: 60         LD      H,B             
76D8: F8 10      LDHL    SP,$10          
76DA: 64         LD      H,H             
76DB: 60         LD      H,B             
76DC: 08 F8 60   LD      ($60F8),SP      
76DF: 40         LD      B,B             
76E0: 08 00 62   LD      ($6200),SP      
76E3: 40         LD      B,B             
76E4: 08 08 62   LD      ($6208),SP      
76E7: 60         LD      H,B             
76E8: 08 10 60   LD      ($6010),SP      
76EB: 60         LD      H,B             
76EC: F8 F8      LDHL    SP,$F8          
76EE: 68         LD      L,B             
76EF: 00         NOP                     
76F0: F8 00      LDHL    SP,$00          
76F2: 6A         LD      L,D             
76F3: 00         NOP                     
76F4: F8 08      LDHL    SP,$08          
76F6: 62         LD      H,D             
76F7: 20 F8      JR      NZ,$76F1        
76F9: 10 60      STOP    $60             
76FB: 20 08      JR      NZ,$7705        
76FD: F8 68      LDHL    SP,$68          
76FF: 40         LD      B,B             
7700: 08 00 6A   LD      ($6A00),SP      
7703: 40         LD      B,B             
7704: 08 08 62   LD      ($6208),SP      
7707: 60         LD      H,B             
7708: 08 10 60   LD      ($6010),SP      
770B: 60         LD      H,B             
770C: F8 F8      LDHL    SP,$F8          
770E: 60         LD      H,B             
770F: 00         NOP                     
7710: F8 00      LDHL    SP,$00          
7712: 62         LD      H,D             
7713: 00         NOP                     
7714: F8 08      LDHL    SP,$08          
7716: 6A         LD      L,D             
7717: 20 F8      JR      NZ,$7711        
7719: 10 68      STOP    $68             
771B: 20 08      JR      NZ,$7725        
771D: F8 60      LDHL    SP,$60          
771F: 40         LD      B,B             
7720: 08 00 62   LD      ($6200),SP      
7723: 40         LD      B,B             
7724: 08 08 6A   LD      ($6A08),SP      
7727: 60         LD      H,B             
7728: 08 10 68   LD      ($6810),SP      
772B: 60         LD      H,B             
772C: F8 F8      LDHL    SP,$F8          
772E: 60         LD      H,B             
772F: 00         NOP                     
7730: F8 00      LDHL    SP,$00          
7732: 62         LD      H,D             
7733: 00         NOP                     
7734: F8 08      LDHL    SP,$08          
7736: 62         LD      H,D             
7737: 20 F8      JR      NZ,$7731        
7739: 10 60      STOP    $60             
773B: 20 08      JR      NZ,$7745        
773D: F8 6C      LDHL    SP,$6C          
773F: 00         NOP                     
7740: 08 00 6E   LD      ($6E00),SP      
7743: 00         NOP                     
7744: 08 08 62   LD      ($6208),SP      
7747: 60         LD      H,B             
7748: 08 10 60   LD      ($6010),SP      
774B: 60         LD      H,B             
774C: F8 F8      LDHL    SP,$F8          
774E: 60         LD      H,B             
774F: 00         NOP                     
7750: F8 00      LDHL    SP,$00          
7752: 62         LD      H,D             
7753: 00         NOP                     
7754: F8 08      LDHL    SP,$08          
7756: 62         LD      H,D             
7757: 20 F8      JR      NZ,$7751        
7759: 10 60      STOP    $60             
775B: 20 08      JR      NZ,$7765        
775D: F8 60      LDHL    SP,$60          
775F: 40         LD      B,B             
7760: 08 00 62   LD      ($6200),SP      
7763: 40         LD      B,B             
7764: 08 08 6E   LD      ($6E08),SP      
7767: 20 08      JR      NZ,$7771        
7769: 10 6C      STOP    $6C             
776B: 20 F8      JR      NZ,$7765        
776D: F8 6C      LDHL    SP,$6C          
776F: 40         LD      B,B             
7770: F8 00      LDHL    SP,$00          
7772: 6E         LD      L,(HL)          
7773: 40         LD      B,B             
7774: F8 08      LDHL    SP,$08          
7776: 62         LD      H,D             
7777: 20 F8      JR      NZ,$7771        
7779: 10 60      STOP    $60             
777B: 20 08      JR      NZ,$7785        
777D: F8 60      LDHL    SP,$60          
777F: 40         LD      B,B             
7780: 08 00 62   LD      ($6200),SP      
7783: 40         LD      B,B             
7784: 08 08 62   LD      ($6208),SP      
7787: 60         LD      H,B             
7788: 08 10 60   LD      ($6010),SP      
778B: 60         LD      H,B             
778C: F8 F8      LDHL    SP,$F8          
778E: 60         LD      H,B             
778F: 00         NOP                     
7790: F8 00      LDHL    SP,$00          
7792: 62         LD      H,D             
7793: 00         NOP                     
7794: F8 08      LDHL    SP,$08          
7796: 6E         LD      L,(HL)          
7797: 60         LD      H,B             
7798: F8 10      LDHL    SP,$10          
779A: 6C         LD      L,H             
779B: 60         LD      H,B             
779C: 08 F8 60   LD      ($60F8),SP      
779F: 40         LD      B,B             
77A0: 08 00 62   LD      ($6200),SP      
77A3: 40         LD      B,B             
77A4: 08 08 62   LD      ($6208),SP      
77A7: 60         LD      H,B             
77A8: 08 10 60   LD      ($6010),SP      
77AB: 60         LD      H,B             
77AC: F8 F8      LDHL    SP,$F8          
77AE: 60         LD      H,B             
77AF: 00         NOP                     
77B0: F8 00      LDHL    SP,$00          
77B2: 62         LD      H,D             
77B3: 00         NOP                     
77B4: F8 08      LDHL    SP,$08          
77B6: 62         LD      H,D             
77B7: 20 F8      JR      NZ,$77B1        
77B9: 10 60      STOP    $60             
77BB: 20 08      JR      NZ,$77C5        
77BD: F8 78      LDHL    SP,$78          
77BF: 00         NOP                     
77C0: 08 00 7A   LD      ($7A00),SP      
77C3: 00         NOP                     
77C4: 08 08 7A   LD      ($7A08),SP      
77C7: 20 08      JR      NZ,$77D1        
77C9: 10 78      STOP    $78             
77CB: 20 08      JR      NZ,$77D5        
77CD: 00         NOP                     
77CE: 76         HALT                    
77CF: 00         NOP                     
77D0: 08 08 76   LD      ($7608),SP      
77D3: 20 08      JR      NZ,$77DD        
77D5: 08 76 20   LD      ($2076),SP      
77D8: 08 08 76   LD      ($7608),SP      
77DB: 20 08      JR      NZ,$77E5        
77DD: 08 76 20   LD      ($2076),SP      
77E0: 08 08 76   LD      ($7608),SP      
77E3: 20 08      JR      NZ,$77ED        
77E5: 08 76 20   LD      ($2076),SP      
77E8: 08 08 76   LD      ($7608),SP      
77EB: 20 08      JR      NZ,$77F5        
77ED: F8 64      LDHL    SP,$64          
77EF: 00         NOP                     
77F0: 08 00 66   LD      ($6600),SP      
77F3: 00         NOP                     
77F4: 08 08 66   LD      ($6608),SP      
77F7: 20 08      JR      NZ,$7801        
77F9: 10 64      STOP    $64             
77FB: 20 08      JR      NZ,$7805        
77FD: F8 64      LDHL    SP,$64          
77FF: 00         NOP                     
7800: 08 00 66   LD      ($6600),SP      
7803: 00         NOP                     
7804: 08 08 66   LD      ($6608),SP      
7807: 20 08      JR      NZ,$7811        
7809: 10 64      STOP    $64             
780B: 20 08      JR      NZ,$7815        
780D: F8 78      LDHL    SP,$78          
780F: 00         NOP                     
7810: 08 00 7A   LD      ($7A00),SP      
7813: 00         NOP                     
7814: 08 08 7A   LD      ($7A08),SP      
7817: 20 08      JR      NZ,$7821        
7819: 10 78      STOP    $78             
781B: 20 08      JR      NZ,$7825        
781D: F8 78      LDHL    SP,$78          
781F: 00         NOP                     
7820: 08 00 7A   LD      ($7A00),SP      
7823: 00         NOP                     
7824: 08 08 7A   LD      ($7A08),SP      
7827: 20 08      JR      NZ,$7831        
7829: 10 78      STOP    $78             
782B: 20 F8      JR      NZ,$7825        
782D: 00         NOP                     
782E: 76         HALT                    
782F: 40         LD      B,B             
7830: F8 08      LDHL    SP,$08          
7832: 76         HALT                    
7833: 60         LD      H,B             
7834: F8 08      LDHL    SP,$08          
7836: 76         HALT                    
7837: 60         LD      H,B             
7838: F8 08      LDHL    SP,$08          
783A: 76         HALT                    
783B: 60         LD      H,B             
783C: F8 08      LDHL    SP,$08          
783E: 76         HALT                    
783F: 60         LD      H,B             
7840: F8 08      LDHL    SP,$08          
7842: 76         HALT                    
7843: 60         LD      H,B             
7844: F8 08      LDHL    SP,$08          
7846: 76         HALT                    
7847: 60         LD      H,B             
7848: F8 08      LDHL    SP,$08          
784A: 76         HALT                    
784B: 60         LD      H,B             
784C: F8 F8      LDHL    SP,$F8          
784E: 64         LD      H,H             
784F: 40         LD      B,B             
7850: F8 00      LDHL    SP,$00          
7852: 66         LD      H,(HL)          
7853: 40         LD      B,B             
7854: F8 08      LDHL    SP,$08          
7856: 66         LD      H,(HL)          
7857: 60         LD      H,B             
7858: F8 10      LDHL    SP,$10          
785A: 64         LD      H,H             
785B: 60         LD      H,B             
785C: F8 F8      LDHL    SP,$F8          
785E: 64         LD      H,H             
785F: 40         LD      B,B             
7860: F8 00      LDHL    SP,$00          
7862: 66         LD      H,(HL)          
7863: 40         LD      B,B             
7864: F8 08      LDHL    SP,$08          
7866: 66         LD      H,(HL)          
7867: 60         LD      H,B             
7868: F8 10      LDHL    SP,$10          
786A: 64         LD      H,H             
786B: 60         LD      H,B             
786C: F8 F8      LDHL    SP,$F8          
786E: 78         LD      A,B             
786F: 40         LD      B,B             
7870: F8 00      LDHL    SP,$00          
7872: 7A         LD      A,D             
7873: 40         LD      B,B             
7874: F8 08      LDHL    SP,$08          
7876: 7A         LD      A,D             
7877: 60         LD      H,B             
7878: F8 10      LDHL    SP,$10          
787A: 78         LD      A,B             
787B: 60         LD      H,B             
787C: F8 F8      LDHL    SP,$F8          
787E: 78         LD      A,B             
787F: 40         LD      B,B             
7880: F8 00      LDHL    SP,$00          
7882: 7A         LD      A,D             
7883: 40         LD      B,B             
7884: F8 08      LDHL    SP,$08          
7886: 7A         LD      A,D             
7887: 60         LD      H,B             
7888: F8 10      LDHL    SP,$10          
788A: 78         LD      A,B             
788B: 60         LD      H,B             
788C: 08 F8 60   LD      ($60F8),SP      
788F: 40         LD      B,B             
7890: 08 00 62   LD      ($6200),SP      
7893: 40         LD      B,B             
7894: 08 08 62   LD      ($6208),SP      
7897: 60         LD      H,B             
7898: 08 10 60   LD      ($6010),SP      
789B: 60         LD      H,B             
789C: F8 F8      LDHL    SP,$F8          
789E: 78         LD      A,B             
789F: 40         LD      B,B             
78A0: F8 00      LDHL    SP,$00          
78A2: 7A         LD      A,D             
78A3: 40         LD      B,B             
78A4: F8 08      LDHL    SP,$08          
78A6: 7A         LD      A,D             
78A7: 60         LD      H,B             
78A8: F8 10      LDHL    SP,$10          
78AA: 78         LD      A,B             
78AB: 60         LD      H,B             
78AC: F0 F1      LD      A,($F1)         
78AE: 50         LD      D,B             
78AF: 17         RLA                     
78B0: CB 12      SET     1,E             
78B2: 17         RLA                     
78B3: CB 12      SET     1,E             
78B5: 17         RLA                     
78B6: CB 12      SET     1,E             
78B8: 17         RLA                     
78B9: CB 12      SET     1,E             
78BB: 17         RLA                     
78BC: CB 12      SET     1,E             
78BE: E6 E0      AND     $E0             
78C0: 5F         LD      E,A             
78C1: 21 AC 76   LD      HL,$76AC        
78C4: 19         ADD     HL,DE           
78C5: 0E 08      LD      C,$08           
78C7: CD 26 3D   CALL    $3D26           
78CA: 3E 08      LD      A,$08           
78CC: CD D0 3D   CALL    $3DD0           
78CF: C9         RET                     
78D0: F2         ???                     
78D1: 0E F0      LD      C,$F0           
78D3: E7         RST     0X20            
78D4: E6 10      AND     $10             
78D6: 3E 03      LD      A,$03           
78D8: 28 01      JR      Z,$78DB         
78DA: 3C         INC     A               
78DB: E0 F1      LDFF00  ($F1),A         
78DD: 00         NOP                     
78DE: 21 80 C3   LD      HL,$C380        
78E1: 09         ADD     HL,BC           
78E2: 5E         LD      E,(HL)          
78E3: 50         LD      D,B             
78E4: 21 D0 78   LD      HL,$78D0        
78E7: 19         ADD     HL,DE           
78E8: 7E         LD      A,(HL)          
78E9: 21 EC FF   LD      HL,$FFEC        
78EC: 86         ADD     A,(HL)          
78ED: 77         LD      (HL),A          
78EE: FE 14      CP      $14             
78F0: 38 58      JR      C,$794A         
78F2: FE 7C      CP      $7C             
78F4: 30 54      JR      NC,$794A        
78F6: 11 EC 71   LD      DE,$71EC        
78F9: CD 3B 3C   CALL    $3C3B           
78FC: F0 F0      LD      A,($F0)         
78FE: FE 04      CP      $04             
7900: 30 46      JR      NC,$7948        
7902: F0 F1      LD      A,($F1)         
7904: A7         AND     A               
7905: 28 3E      JR      Z,$7945         
7907: AF         XOR     A               
7908: E0 F1      LDFF00  ($F1),A         
790A: CD EB 3B   CALL    $3BEB           
790D: 21 20 C4   LD      HL,$C420        
7910: 09         ADD     HL,BC           
7911: 7E         LD      A,(HL)          
7912: FE 16      CP      $16             
7914: 20 2F      JR      NZ,$7945        
7916: 21 04 D2   LD      HL,$D204        
7919: 34         INC     (HL)            
791A: 7E         LD      A,(HL)          
791B: FE 08      CP      $08             
791D: 20 26      JR      NZ,$7945        
791F: FA 01 D2   LD      A,($D201)       
7922: 5F         LD      E,A             
7923: 50         LD      D,B             
7924: 21 80 C2   LD      HL,$C280        
7927: 19         ADD     HL,DE           
7928: 70         LD      (HL),B          
7929: CD 8D 3B   CALL    $3B8D           
792C: 36 04      LD      (HL),$04        
792E: CD 91 08   CALL    $0891           
7931: 36 FF      LD      (HL),$FF        
7933: CD D2 27   CALL    $27D2           
7936: 3E 03      LD      A,$03           
7938: EA A7 C5   LD      ($C5A7),A       
793B: 3E 5E      LD      A,$5E           
793D: EA 68 D3   LD      ($D368),A       
7940: 3E B5      LD      A,$B5           
7942: CD 97 21   CALL    $2197           
7945: CD BF 3B   CALL    $3BBF           
7948: 18 94      JR      $78DE           
794A: CD BA 3D   CALL    $3DBA           
794D: 21 20 C4   LD      HL,$C420        
7950: 09         ADD     HL,BC           
7951: 7E         LD      A,(HL)          
7952: A7         AND     A               
7953: 20 0F      JR      NZ,$7964        
7955: 21 30 C4   LD      HL,$C430        
7958: 09         ADD     HL,BC           
7959: 36 C0      LD      (HL),$C0        
795B: CD EB 3B   CALL    $3BEB           
795E: 21 30 C4   LD      HL,$C430        
7961: 09         ADD     HL,BC           
7962: 36 80      LD      (HL),$80        
7964: C9         RET                     
7965: F0 EA      LD      A,($EA)         
7967: FE 05      CP      $05             
7969: 20 1A      JR      NZ,$7985        
796B: FA 95 DB   LD      A,($DB95)       
796E: FE 07      CP      $07             
7970: 28 13      JR      Z,$7985         
7972: 21 A8 C1   LD      HL,$C1A8        
7975: FA 9F C1   LD      A,($C19F)       
7978: B6         OR      (HL)            
7979: 21 4F C1   LD      HL,$C14F        
797C: B6         OR      (HL)            
797D: 20 06      JR      NZ,$7985        
797F: FA 24 C1   LD      A,($C124)       
7982: A7         AND     A               
7983: 28 01      JR      Z,$7986         
7985: F1         POP     AF              
7986: C9         RET                     
7987: 21 10 C4   LD      HL,$C410        
798A: 09         ADD     HL,BC           
798B: 7E         LD      A,(HL)          
798C: A7         AND     A               
798D: 28 41      JR      Z,$79D0         
798F: 3D         DEC     A               
7990: 77         LD      (HL),A          
7991: CD B8 3E   CALL    $3EB8           
7994: 21 40 C2   LD      HL,$C240        
7997: 09         ADD     HL,BC           
7998: 7E         LD      A,(HL)          
7999: F5         PUSH    AF              
799A: 21 50 C2   LD      HL,$C250        
799D: 09         ADD     HL,BC           
799E: 7E         LD      A,(HL)          
799F: F5         PUSH    AF              
79A0: 21 F0 C3   LD      HL,$C3F0        
79A3: 09         ADD     HL,BC           
79A4: 7E         LD      A,(HL)          
79A5: 21 40 C2   LD      HL,$C240        
79A8: 09         ADD     HL,BC           
79A9: 77         LD      (HL),A          
79AA: 21 00 C4   LD      HL,$C400        
79AD: 09         ADD     HL,BC           
79AE: 7E         LD      A,(HL)          
79AF: 21 50 C2   LD      HL,$C250        
79B2: 09         ADD     HL,BC           
79B3: 77         LD      (HL),A          
79B4: CD D1 79   CALL    $79D1           
79B7: 21 30 C4   LD      HL,$C430        
79BA: 09         ADD     HL,BC           
79BB: 7E         LD      A,(HL)          
79BC: E6 20      AND     $20             
79BE: 20 03      JR      NZ,$79C3        
79C0: CD 9E 3B   CALL    $3B9E           
79C3: 21 50 C2   LD      HL,$C250        
79C6: 09         ADD     HL,BC           
79C7: F1         POP     AF              
79C8: 77         LD      (HL),A          
79C9: 21 40 C2   LD      HL,$C240        
79CC: 09         ADD     HL,BC           
79CD: F1         POP     AF              
79CE: 77         LD      (HL),A          
79CF: F1         POP     AF              
79D0: C9         RET                     
79D1: CD DE 79   CALL    $79DE           
79D4: C5         PUSH    BC              
79D5: 79         LD      A,C             
79D6: C6 10      ADD     $10             
79D8: 4F         LD      C,A             
79D9: CD DE 79   CALL    $79DE           
79DC: C1         POP     BC              
79DD: C9         RET                     
79DE: 21 40 C2   LD      HL,$C240        
79E1: 09         ADD     HL,BC           
79E2: 7E         LD      A,(HL)          
79E3: A7         AND     A               
79E4: 28 23      JR      Z,$7A09         
79E6: F5         PUSH    AF              
79E7: CB 37      SET     1,E             
79E9: E6 F0      AND     $F0             
79EB: 21 60 C2   LD      HL,$C260        
79EE: 09         ADD     HL,BC           
79EF: 86         ADD     A,(HL)          
79F0: 77         LD      (HL),A          
79F1: CB 12      SET     1,E             
79F3: 21 00 C2   LD      HL,$C200        
79F6: 09         ADD     HL,BC           
79F7: F1         POP     AF              
79F8: 1E 00      LD      E,$00           
79FA: CB 7F      SET     1,E             
79FC: 28 02      JR      Z,$7A00         
79FE: 1E F0      LD      E,$F0           
7A00: CB 37      SET     1,E             
7A02: E6 0F      AND     $0F             
7A04: B3         OR      E               
7A05: CB 1A      SET     1,E             
7A07: 8E         ADC     A,(HL)          
7A08: 77         LD      (HL),A          
7A09: C9         RET                     
7A0A: 21 20 C3   LD      HL,$C320        
7A0D: 09         ADD     HL,BC           
7A0E: 7E         LD      A,(HL)          
7A0F: A7         AND     A               
7A10: 28 F7      JR      Z,$7A09         
7A12: F5         PUSH    AF              
7A13: CB 37      SET     1,E             
7A15: E6 F0      AND     $F0             
7A17: 21 30 C3   LD      HL,$C330        
7A1A: 09         ADD     HL,BC           
7A1B: 86         ADD     A,(HL)          
7A1C: 77         LD      (HL),A          
7A1D: CB 12      SET     1,E             
7A1F: 21 10 C3   LD      HL,$C310        
7A22: 18 D2      JR      $79F6           
7A24: 1E 00      LD      E,$00           
7A26: F0 98      LD      A,($98)         
7A28: 21 00 C2   LD      HL,$C200        
7A2B: 09         ADD     HL,BC           
7A2C: 96         SUB     (HL)            
7A2D: CB 7F      SET     1,E             
7A2F: 28 01      JR      Z,$7A32         
7A31: 1C         INC     E               
7A32: 57         LD      D,A             
7A33: C9         RET                     
7A34: 1E 02      LD      E,$02           
7A36: F0 99      LD      A,($99)         
7A38: 21 10 C2   LD      HL,$C210        
7A3B: 09         ADD     HL,BC           
7A3C: 96         SUB     (HL)            
7A3D: CB 7F      SET     1,E             
7A3F: 20 01      JR      NZ,$7A42        
7A41: 1C         INC     E               
7A42: 57         LD      D,A             
7A43: C9         RET                     
7A44: CD 24 7A   CALL    $7A24           
7A47: 7B         LD      A,E             
7A48: E0 D7      LDFF00  ($D7),A         
7A4A: 7A         LD      A,D             
7A4B: CB 7F      SET     1,E             
7A4D: 28 02      JR      Z,$7A51         
7A4F: 2F         CPL                     
7A50: 3C         INC     A               
7A51: F5         PUSH    AF              
7A52: CD 34 7A   CALL    $7A34           
7A55: 7B         LD      A,E             
7A56: E0 D8      LDFF00  ($D8),A         
7A58: 7A         LD      A,D             
7A59: CB 7F      SET     1,E             
7A5B: 28 02      JR      Z,$7A5F         
7A5D: 2F         CPL                     
7A5E: 3C         INC     A               
7A5F: D1         POP     DE              
7A60: BA         CP      D               
7A61: 30 04      JR      NC,$7A67        
7A63: F0 D7      LD      A,($D7)         
7A65: 18 02      JR      $7A69           
7A67: F0 D8      LD      A,($D8)         
7A69: 5F         LD      E,A             
7A6A: C9         RET                     
7A6B: 21 80 C2   LD      HL,$C280        
7A6E: 09         ADD     HL,BC           
7A6F: 70         LD      (HL),B          
7A70: C9         RET                     
7A71: 10 F0      STOP    $F0             
7A73: 18 E8      JR      $7A5D           
7A75: 00         NOP                     
7A76: F0 64      LD      A,($64)         
7A78: 00         NOP                     
7A79: 00         NOP                     
7A7A: F8 66      LDHL    SP,$66          
7A7C: 00         NOP                     
7A7D: 00         NOP                     
7A7E: 00         NOP                     
7A7F: 60         LD      H,B             
7A80: 00         NOP                     
7A81: 00         NOP                     
7A82: 08 60 20   LD      ($2060),SP      
7A85: 00         NOP                     
7A86: 10 6A      STOP    $6A             
7A88: 20 00      JR      NZ,$7A8A        
7A8A: 18 68      JR      $7AF4           
7A8C: 20 00      JR      NZ,$7A8E        
7A8E: F0 6C      LD      A,($6C)         
7A90: 00         NOP                     
7A91: 00         NOP                     
7A92: F8 6E      LDHL    SP,$6E          
7A94: 00         NOP                     
7A95: 00         NOP                     
7A96: 00         NOP                     
7A97: 60         LD      H,B             
7A98: 00         NOP                     
7A99: 00         NOP                     
7A9A: 08 60 20   LD      ($2060),SP      
7A9D: 00         NOP                     
7A9E: 10 6E      STOP    $6E             
7AA0: 20 00      JR      NZ,$7AA2        
7AA2: 18 6C      JR      $7B10           
7AA4: 20 00      JR      NZ,$7AA6        
7AA6: F0 68      LD      A,($68)         
7AA8: 00         NOP                     
7AA9: 00         NOP                     
7AAA: F8 6A      LDHL    SP,$6A          
7AAC: 00         NOP                     
7AAD: 00         NOP                     
7AAE: 00         NOP                     
7AAF: 60         LD      H,B             
7AB0: 00         NOP                     
7AB1: 00         NOP                     
7AB2: 08 60 20   LD      ($2060),SP      
7AB5: 00         NOP                     
7AB6: 10 66      STOP    $66             
7AB8: 20 00      JR      NZ,$7ABA        
7ABA: 18 64      JR      $7B20           
7ABC: 20 00      JR      NZ,$7ABE        
7ABE: F0 64      LD      A,($64)         
7AC0: 00         NOP                     
7AC1: 00         NOP                     
7AC2: F8 66      LDHL    SP,$66          
7AC4: 00         NOP                     
7AC5: 00         NOP                     
7AC6: 00         NOP                     
7AC7: 62         LD      H,D             
7AC8: 00         NOP                     
7AC9: 00         NOP                     
7ACA: 08 62 20   LD      ($2062),SP      
7ACD: 00         NOP                     
7ACE: 10 6A      STOP    $6A             
7AD0: 20 00      JR      NZ,$7AD2        
7AD2: 18 68      JR      $7B3C           
7AD4: 20 00      JR      NZ,$7AD6        
7AD6: F0 6C      LD      A,($6C)         
7AD8: 00         NOP                     
7AD9: 00         NOP                     
7ADA: F8 6E      LDHL    SP,$6E          
7ADC: 00         NOP                     
7ADD: 00         NOP                     
7ADE: 00         NOP                     
7ADF: 62         LD      H,D             
7AE0: 00         NOP                     
7AE1: 00         NOP                     
7AE2: 08 62 20   LD      ($2062),SP      
7AE5: 00         NOP                     
7AE6: 10 6E      STOP    $6E             
7AE8: 20 00      JR      NZ,$7AEA        
7AEA: 18 6C      JR      $7B58           
7AEC: 20 00      JR      NZ,$7AEE        
7AEE: F0 68      LD      A,($68)         
7AF0: 00         NOP                     
7AF1: 00         NOP                     
7AF2: F8 6A      LDHL    SP,$6A          
7AF4: 00         NOP                     
7AF5: 00         NOP                     
7AF6: 00         NOP                     
7AF7: 62         LD      H,D             
7AF8: 00         NOP                     
7AF9: 00         NOP                     
7AFA: 08 62 20   LD      ($2062),SP      
7AFD: 00         NOP                     
7AFE: 10 66      STOP    $66             
7B00: 20 00      JR      NZ,$7B02        
7B02: 18 64      JR      $7B68           
7B04: 20 FA      JR      NZ,$7B00        
7B06: 66         LD      H,(HL)          
7B07: C1         POP     BC              
7B08: FE 01      CP      $01             
7B0A: 20 0A      JR      NZ,$7B16        
7B0C: CD F5 7B   CALL    $7BF5           
7B0F: 21 90 C2   LD      HL,$C290        
7B12: 09         ADD     HL,BC           
7B13: 7E         LD      A,(HL)          
7B14: E0 F0      LDFF00  ($F0),A         
7B16: F0 F1      LD      A,($F1)         
7B18: 17         RLA                     
7B19: 17         RLA                     
7B1A: 17         RLA                     
7B1B: E6 F8      AND     $F8             
7B1D: 4F         LD      C,A             
7B1E: 17         RLA                     
7B1F: E6 F0      AND     $F0             
7B21: 81         ADD     A,C             
7B22: 5F         LD      E,A             
7B23: 50         LD      D,B             
7B24: 21 75 7A   LD      HL,$7A75        
7B27: 19         ADD     HL,DE           
7B28: 0E 06      LD      C,$06           
7B2A: CD 26 3D   CALL    $3D26           
7B2D: 3E 06      LD      A,$06           
7B2F: CD D0 3D   CALL    $3DD0           
7B32: F0 EA      LD      A,($EA)         
7B34: FE 05      CP      $05             
7B36: C2 8D 7D   JP      NZ,$7D8D        
7B39: CD 65 79   CALL    $7965           
7B3C: CD 12 3F   CALL    $3F12           
7B3F: CD B4 3B   CALL    $3BB4           
7B42: CD D1 79   CALL    $79D1           
7B45: CD 9E 3B   CALL    $3B9E           
7B48: CD E2 08   CALL    $08E2           
7B4B: F0 F0      LD      A,($F0)         
7B4D: C7         RST     0X00            
7B4E: 56         LD      D,(HL)          
7B4F: 7B         LD      A,E             
7B50: 72         LD      (HL),D          
7B51: 7B         LD      A,E             
7B52: 83         ADD     A,E             
7B53: 7C         LD      A,H             
7B54: 2B         DEC     HL              
7B55: 7D         LD      A,L             
7B56: CD ED 27   CALL    $27ED           
7B59: E6 01      AND     $01             
7B5B: 21 B0 C2   LD      HL,$C2B0        
7B5E: 09         ADD     HL,BC           
7B5F: 77         LD      (HL),A          
7B60: 5F         LD      E,A             
7B61: 50         LD      D,B             
7B62: 21 71 7A   LD      HL,$7A71        
7B65: 19         ADD     HL,DE           
7B66: 7E         LD      A,(HL)          
7B67: 21 40 C2   LD      HL,$C240        
7B6A: 09         ADD     HL,BC           
7B6B: 77         LD      (HL),A          
7B6C: CD 8D 3B   CALL    $3B8D           
7B6F: 36 01      LD      (HL),$01        
7B71: C9         RET                     
7B72: 21 00 C3   LD      HL,$C300        
7B75: 09         ADD     HL,BC           
7B76: 7E         LD      A,(HL)          
7B77: A7         AND     A               
7B78: C0         RET     NZ              
7B79: CD 8C 08   CALL    $088C           
7B7C: C2 09 7C   JP      NZ,$7C09        
7B7F: CD 91 08   CALL    $0891           
7B82: 28 25      JR      Z,$7BA9         
7B84: FE 01      CP      $01             
7B86: 20 34      JR      NZ,$7BBC        
7B88: CD 24 7A   CALL    $7A24           
7B8B: 50         LD      D,B             
7B8C: 21 73 7A   LD      HL,$7A73        
7B8F: 19         ADD     HL,DE           
7B90: 7E         LD      A,(HL)          
7B91: 21 40 C2   LD      HL,$C240        
7B94: 09         ADD     HL,BC           
7B95: 77         LD      (HL),A          
7B96: 21 50 C2   LD      HL,$C250        
7B99: 09         ADD     HL,BC           
7B9A: 70         LD      (HL),B          
7B9B: CD 8C 08   CALL    $088C           
7B9E: CD ED 27   CALL    $27ED           
7BA1: E6 3F      AND     $3F             
7BA3: C6 60      ADD     $60             
7BA5: 77         LD      (HL),A          
7BA6: C3 09 7C   JP      $7C09           
7BA9: 21 10 C2   LD      HL,$C210        
7BAC: 09         ADD     HL,BC           
7BAD: 7E         LD      A,(HL)          
7BAE: C6 08      ADD     $08             
7BB0: 21 99 FF   LD      HL,$FF99        
7BB3: BE         CP      (HL)            
7BB4: DA D3 7B   JP      C,$7BD3         
7BB7: CD 91 08   CALL    $0891           
7BBA: 36 60      LD      (HL),$60        
7BBC: 21 50 C2   LD      HL,$C250        
7BBF: 09         ADD     HL,BC           
7BC0: 70         LD      (HL),B          
7BC1: 21 40 C2   LD      HL,$C240        
7BC4: 09         ADD     HL,BC           
7BC5: E6 04      AND     $04             
7BC7: 20 05      JR      NZ,$7BCE        
7BC9: 36 08      LD      (HL),$08        
7BCB: C3 61 7C   JP      $7C61           
7BCE: 36 F8      LD      (HL),$F8        
7BD0: C3 61 7C   JP      $7C61           
7BD3: 21 10 C2   LD      HL,$C210        
7BD6: 09         ADD     HL,BC           
7BD7: F0 99      LD      A,($99)         
7BD9: 96         SUB     (HL)            
7BDA: FE 28      CP      $28             
7BDC: 30 2B      JR      NC,$7C09        
7BDE: 21 80 C4   LD      HL,$C480        
7BE1: 09         ADD     HL,BC           
7BE2: 7E         LD      A,(HL)          
7BE3: A7         AND     A               
7BE4: 20 23      JR      NZ,$7C09        
7BE6: CD ED 27   CALL    $27ED           
7BE9: E6 7F      AND     $7F             
7BEB: C6 40      ADD     $40             
7BED: 77         LD      (HL),A          
7BEE: E6 03      AND     $03             
7BF0: 28 50      JR      Z,$7C42         
7BF2: 3D         DEC     A               
7BF3: 20 14      JR      NZ,$7C09        
7BF5: CD 8D 3B   CALL    $3B8D           
7BF8: 36 03      LD      (HL),$03        
7BFA: CD AF 3D   CALL    $3DAF           
7BFD: 21 00 C3   LD      HL,$C300        
7C00: 09         ADD     HL,BC           
7C01: 36 40      LD      (HL),$40        
7C03: 3E 01      LD      A,$01           
7C05: CD 80 7C   CALL    $7C80           
7C08: C9         RET                     
7C09: 21 A0 C2   LD      HL,$C2A0        
7C0C: 09         ADD     HL,BC           
7C0D: 7E         LD      A,(HL)          
7C0E: E6 03      AND     $03             
7C10: 28 18      JR      Z,$7C2A         
7C12: CD 8C 08   CALL    $088C           
7C15: 28 0B      JR      Z,$7C22         
7C17: 21 40 C2   LD      HL,$C240        
7C1A: 09         ADD     HL,BC           
7C1B: 7E         LD      A,(HL)          
7C1C: EE F0      XOR     $F0             
7C1E: 77         LD      (HL),A          
7C1F: C3 61 7C   JP      $7C61           
7C22: 21 B0 C2   LD      HL,$C2B0        
7C25: 09         ADD     HL,BC           
7C26: 7E         LD      A,(HL)          
7C27: EE 01      XOR     $01             
7C29: 77         LD      (HL),A          
7C2A: CD 8C 08   CALL    $088C           
7C2D: 20 32      JR      NZ,$7C61        
7C2F: 21 B0 C2   LD      HL,$C2B0        
7C32: 09         ADD     HL,BC           
7C33: 7E         LD      A,(HL)          
7C34: 5F         LD      E,A             
7C35: 50         LD      D,B             
7C36: 21 71 7A   LD      HL,$7A71        
7C39: 19         ADD     HL,DE           
7C3A: 7E         LD      A,(HL)          
7C3B: 21 40 C2   LD      HL,$C240        
7C3E: 09         ADD     HL,BC           
7C3F: 77         LD      (HL),A          
7C40: 18 27      JR      $7C69           
7C42: CD 91 08   CALL    $0891           
7C45: 36 60      LD      (HL),$60        
7C47: CD 8C 08   CALL    $088C           
7C4A: 70         LD      (HL),B          
7C4B: CD 8D 3B   CALL    $3B8D           
7C4E: 36 02      LD      (HL),$02        
7C50: 21 B0 C2   LD      HL,$C2B0        
7C53: 09         ADD     HL,BC           
7C54: 70         LD      (HL),B          
7C55: 21 10 C2   LD      HL,$C210        
7C58: 09         ADD     HL,BC           
7C59: 7E         LD      A,(HL)          
7C5A: 21 D0 C2   LD      HL,$C2D0        
7C5D: 09         ADD     HL,BC           
7C5E: 77         LD      (HL),A          
7C5F: 18 08      JR      $7C69           
7C61: F0 E7      LD      A,($E7)         
7C63: E6 07      AND     $07             
7C65: 28 08      JR      Z,$7C6F         
7C67: 18 12      JR      $7C7B           
7C69: F0 E7      LD      A,($E7)         
7C6B: E6 0F      AND     $0F             
7C6D: 20 0C      JR      NZ,$7C7B        
7C6F: 21 D0 C3   LD      HL,$C3D0        
7C72: 09         ADD     HL,BC           
7C73: 34         INC     (HL)            
7C74: 7E         LD      A,(HL)          
7C75: FE 03      CP      $03             
7C77: 20 02      JR      NZ,$7C7B        
7C79: 36 00      LD      (HL),$00        
7C7B: 21 D0 C3   LD      HL,$C3D0        
7C7E: 09         ADD     HL,BC           
7C7F: 7E         LD      A,(HL)          
7C80: C3 87 3B   JP      $3B87           
7C83: 21 B0 C2   LD      HL,$C2B0        
7C86: 09         ADD     HL,BC           
7C87: 7E         LD      A,(HL)          
7C88: A7         AND     A               
7C89: C2 FD 7C   JP      NZ,$7CFD        
7C8C: CD 91 08   CALL    $0891           
7C8F: FE 02      CP      $02             
7C91: 30 5A      JR      NC,$7CED        
7C93: FE 00      CP      $00             
7C95: 28 32      JR      Z,$7CC9         
7C97: 21 99 FF   LD      HL,$FF99        
7C9A: 7E         LD      A,(HL)          
7C9B: 21 90 C3   LD      HL,$C390        
7C9E: 09         ADD     HL,BC           
7C9F: 77         LD      (HL),A          
7CA0: CD ED 27   CALL    $27ED           
7CA3: E6 02      AND     $02             
7CA5: 28 0C      JR      Z,$7CB3         
7CA7: CD AF 3D   CALL    $3DAF           
7CAA: 21 50 C2   LD      HL,$C250        
7CAD: 09         ADD     HL,BC           
7CAE: 36 10      LD      (HL),$10        
7CB0: C3 B8 7C   JP      $7CB8           
7CB3: 3E 10      LD      A,$10           
7CB5: CD 25 3C   CALL    $3C25           
7CB8: 21 10 C2   LD      HL,$C210        
7CBB: 09         ADD     HL,BC           
7CBC: 7E         LD      A,(HL)          
7CBD: C6 08      ADD     $08             
7CBF: 21 99 FF   LD      HL,$FF99        
7CC2: BE         CP      (HL)            
7CC3: D2 09 7D   JP      NC,$7D09        
7CC6: C3 11 7D   JP      $7D11           
7CC9: 21 90 C3   LD      HL,$C390        
7CCC: 09         ADD     HL,BC           
7CCD: 7E         LD      A,(HL)          
7CCE: D6 08      SUB     $08             
7CD0: 21 10 C2   LD      HL,$C210        
7CD3: 09         ADD     HL,BC           
7CD4: BE         CP      (HL)            
7CD5: D2 11 7D   JP      NC,$7D11        
7CD8: 21 B0 C2   LD      HL,$C2B0        
7CDB: 09         ADD     HL,BC           
7CDC: 34         INC     (HL)            
7CDD: CD AF 3D   CALL    $3DAF           
7CE0: 21 50 C2   LD      HL,$C250        
7CE3: 09         ADD     HL,BC           
7CE4: 36 F0      LD      (HL),$F0        
7CE6: 3E 16      LD      A,$16           
7CE8: E0 F3      LDFF00  ($F3),A         
7CEA: C3 11 7D   JP      $7D11           
7CED: 21 40 C2   LD      HL,$C240        
7CF0: 09         ADD     HL,BC           
7CF1: E6 04      AND     $04             
7CF3: 20 04      JR      NZ,$7CF9        
7CF5: 36 08      LD      (HL),$08        
7CF7: 18 18      JR      $7D11           
7CF9: 36 F8      LD      (HL),$F8        
7CFB: 18 14      JR      $7D11           
7CFD: 21 D0 C2   LD      HL,$C2D0        
7D00: 09         ADD     HL,BC           
7D01: 7E         LD      A,(HL)          
7D02: 21 10 C2   LD      HL,$C210        
7D05: 09         ADD     HL,BC           
7D06: BE         CP      (HL)            
7D07: 38 08      JR      C,$7D11         
7D09: CD AF 3D   CALL    $3DAF           
7D0C: CD 8D 3B   CALL    $3B8D           
7D0F: 36 01      LD      (HL),$01        
7D11: F0 E7      LD      A,($E7)         
7D13: E6 0F      AND     $0F             
7D15: 20 0C      JR      NZ,$7D23        
7D17: 21 D0 C3   LD      HL,$C3D0        
7D1A: 09         ADD     HL,BC           
7D1B: 34         INC     (HL)            
7D1C: 7E         LD      A,(HL)          
7D1D: FE 03      CP      $03             
7D1F: 20 02      JR      NZ,$7D23        
7D21: 36 00      LD      (HL),$00        
7D23: 21 D0 C3   LD      HL,$C3D0        
7D26: 09         ADD     HL,BC           
7D27: 7E         LD      A,(HL)          
7D28: C3 87 3B   JP      $3B87           
7D2B: 21 00 C3   LD      HL,$C300        
7D2E: 09         ADD     HL,BC           
7D2F: 7E         LD      A,(HL)          
7D30: A7         AND     A               
7D31: 28 01      JR      Z,$7D34         
7D33: C9         RET                     
7D34: CD 8C 08   CALL    $088C           
7D37: FE 02      CP      $02             
7D39: 30 20      JR      NC,$7D5B        
7D3B: FE 00      CP      $00             
7D3D: 28 17      JR      Z,$7D56         
7D3F: 21 50 C3   LD      HL,$C350        
7D42: 09         ADD     HL,BC           
7D43: 36 80      LD      (HL),$80        
7D45: 3E 01      LD      A,$01           
7D47: CD 87 3B   CALL    $3B87           
7D4A: CD 8D 3B   CALL    $3B8D           
7D4D: 36 01      LD      (HL),$01        
7D4F: 21 00 C3   LD      HL,$C300        
7D52: 09         ADD     HL,BC           
7D53: 36 40      LD      (HL),$40        
7D55: C9         RET                     
7D56: CD 8C 08   CALL    $088C           
7D59: 36 30      LD      (HL),$30        
7D5B: FE 18      CP      $18             
7D5D: 20 23      JR      NZ,$7D82        
7D5F: 3E 7D      LD      A,$7D           
7D61: CD 01 3C   CALL    $3C01           
7D64: 38 1C      JR      C,$7D82         
7D66: F0 D7      LD      A,($D7)         
7D68: 21 00 C2   LD      HL,$C200        
7D6B: 19         ADD     HL,DE           
7D6C: 77         LD      (HL),A          
7D6D: F0 D8      LD      A,($D8)         
7D6F: 21 10 C2   LD      HL,$C210        
7D72: 19         ADD     HL,DE           
7D73: 77         LD      (HL),A          
7D74: 21 B0 C2   LD      HL,$C2B0        
7D77: 19         ADD     HL,DE           
7D78: 34         INC     (HL)            
7D79: C5         PUSH    BC              
7D7A: D5         PUSH    DE              
7D7B: C1         POP     BC              
7D7C: 3E 18      LD      A,$18           
7D7E: CD 25 3C   CALL    $3C25           
7D81: C1         POP     BC              
7D82: 21 50 C3   LD      HL,$C350        
7D85: 09         ADD     HL,BC           
7D86: 36 00      LD      (HL),$00        
7D88: 3E 04      LD      A,$04           
7D8A: C3 87 3B   JP      $3B87           
7D8D: 21 C0 C2   LD      HL,$C2C0        
7D90: 09         ADD     HL,BC           
7D91: 7E         LD      A,(HL)          
7D92: C7         RST     0X00            
7D93: 99         SBC     C               
7D94: 7D         LD      A,L             
7D95: AA         XOR     D               
7D96: 7D         LD      A,L             
7D97: BB         CP      E               
7D98: 7D         LD      A,L             
7D99: CD 91 08   CALL    $0891           
7D9C: 36 A0      LD      (HL),$A0        
7D9E: 21 20 C4   LD      HL,$C420        
7DA1: 09         ADD     HL,BC           
7DA2: 36 FF      LD      (HL),$FF        
7DA4: 21 C0 C2   LD      HL,$C2C0        
7DA7: 09         ADD     HL,BC           
7DA8: 34         INC     (HL)            
7DA9: C9         RET                     
7DAA: CD 91 08   CALL    $0891           
7DAD: 20 0B      JR      NZ,$7DBA        
7DAF: 36 C0      LD      (HL),$C0        
7DB1: 21 20 C4   LD      HL,$C420        
7DB4: 09         ADD     HL,BC           
7DB5: 36 FF      LD      (HL),$FF        
7DB7: CD A4 7D   CALL    $7DA4           
7DBA: C9         RET                     
7DBB: CD 91 08   CALL    $0891           
7DBE: 20 38      JR      NZ,$7DF8        
7DC0: 3E 1A      LD      A,$1A           
7DC2: E0 F4      LDFF00  ($F4),A         
7DC4: F0 EB      LD      A,($EB)         
7DC6: FE 63      CP      $63             
7DC8: CA B4 74   JP      Z,$74B4         
7DCB: CD 7A 3F   CALL    $3F7A           
7DCE: 1E 0F      LD      E,$0F           
7DD0: 50         LD      D,B             
7DD1: 21 80 C2   LD      HL,$C280        
7DD4: 19         ADD     HL,DE           
7DD5: 7E         LD      A,(HL)          
7DD6: A7         AND     A               
7DD7: 28 09      JR      Z,$7DE2         
7DD9: 21 30 C4   LD      HL,$C430        
7DDC: 19         ADD     HL,DE           
7DDD: 7E         LD      A,(HL)          
7DDE: E6 80      AND     $80             
7DE0: 20 0E      JR      NZ,$7DF0        
7DE2: 1D         DEC     E               
7DE3: 7B         LD      A,E             
7DE4: FE FF      CP      $FF             
7DE6: 20 E9      JR      NZ,$7DD1        
7DE8: AF         XOR     A               
7DE9: EA CF C1   LD      ($C1CF),A       
7DEC: CD BD 27   CALL    $27BD           
7DEF: C9         RET                     
7DF0: F0 F7      LD      A,($F7)         
7DF2: FE 05      CP      $05             
7DF4: D0         RET     NC              
7DF5: C3 FC 7D   JP      $7DFC           
7DF8: CD 76 74   CALL    $7476           
7DFB: C9         RET                     
7DFC: F0 F6      LD      A,($F6)         
7DFE: 5F         LD      E,A             
7DFF: 50         LD      D,B             
7E00: F0 F7      LD      A,($F7)         
7E02: FE 1A      CP      $1A             
7E04: 30 05      JR      NC,$7E0B        
7E06: FE 06      CP      $06             
7E08: 38 01      JR      C,$7E0B         
7E0A: 14         INC     D               
7E0B: 21 00 D9   LD      HL,$D900        
7E0E: 19         ADD     HL,DE           
7E0F: CB EE      SET     1,E             
7E11: C9         RET                     
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
