![Bank 13](GBZelda.jpg)

# Bank 13

>>> cpu Z80GB

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

```
4000: 00         NOP                     
4001: 00         NOP                     
4002: 39         ADD     HL,SP           
4003: 39         ADD     HL,SP           
4004: 25         DEC     H               
4005: 25         DEC     H               
4006: 25         DEC     H               
4007: 25         DEC     H               
4008: 39         ADD     HL,SP           
4009: 39         ADD     HL,SP           
400A: 21 21 21   LD      HL,$2121        
400D: 21 00 00   LD      HL,$0000        
4010: 00         NOP                     
4011: 00         NOP                     
4012: 0C         INC     C               
4013: 0C         INC     C               
4014: 12         LD      (DE),A          
4015: 12         LD      (DE),A          
4016: 12         LD      (DE),A          
4017: 12         LD      (DE),A          
4018: 1E 1E      LD      E,$1E           
401A: 12         LD      (DE),A          
401B: 12         LD      (DE),A          
401C: D2 D2 00   JP      NC,$00D2        
401F: 00         NOP                     
4020: 00         NOP                     
4021: 00         NOP                     
4022: 8B         ADC     A,E             
4023: 8B         ADC     A,E             
4024: 8A         ADC     A,D             
4025: 8A         ADC     A,D             
4026: 53         LD      D,E             
4027: 53         LD      D,E             
4028: 22         LD      (HLI),A         
4029: 22         LD      (HLI),A         
402A: 22         LD      (HLI),A         
402B: 22         LD      (HLI),A         
402C: 23         INC     HL              
402D: 23         INC     HL              
402E: 00         NOP                     
402F: 00         NOP                     
4030: 00         NOP                     
4031: 00         NOP                     
4032: B8         CP      B               
4033: B8         CP      B               
4034: 24         INC     H               
4035: 24         INC     H               
4036: A4         AND     H               
4037: A4         AND     H               
4038: 38 38      JR      C,$4072         
403A: 24         INC     H               
403B: 24         INC     H               
403C: A4         AND     H               
403D: A4         AND     H               
403E: 00         NOP                     
403F: 00         NOP                     
4040: 3F         CCF                     
4041: 00         NOP                     
4042: C0         RET     NZ              
4043: 3F         CCF                     
4044: B7         OR      A               
4045: FF         RST     0X38            
4046: 43         LD      B,E             
4047: FF         RST     0X38            
4048: 00         NOP                     
4049: FF         RST     0X38            
404A: 47         LD      B,A             
404B: FF         RST     0X38            
404C: C7         RST     0X00            
404D: FF         RST     0X38            
404E: 0F         RRCA                    
404F: FF         RST     0X38            
4050: 8F         ADC     A,A             
4051: FF         RST     0X38            
4052: DF         RST     0X18            
4053: FF         RST     0X38            
4054: DF         RST     0X18            
4055: FF         RST     0X38            
4056: 1F         RRA                     
4057: FF         RST     0X38            
4058: 3F         CCF                     
4059: FF         RST     0X38            
405A: 3F         CCF                     
405B: FF         RST     0X38            
405C: 3F         CCF                     
405D: FF         RST     0X38            
405E: 7F         LD      A,A             
405F: FF         RST     0X38            
4060: FF         RST     0X38            
4061: 00         NOP                     
4062: 00         NOP                     
4063: FF         RST     0X38            
4064: 9E         SBC     (HL)            
4065: FF         RST     0X38            
4066: 0C         INC     C               
4067: FF         RST     0X38            
4068: 00         NOP                     
4069: FF         RST     0X38            
406A: FF         RST     0X38            
406B: FF         RST     0X38            
406C: FF         RST     0X38            
406D: FF         RST     0X38            
406E: FF         RST     0X38            
406F: FF         RST     0X38            
4070: FF         RST     0X38            
4071: FF         RST     0X38            
4072: FF         RST     0X38            
4073: FF         RST     0X38            
4074: FF         RST     0X38            
4075: FF         RST     0X38            
4076: FF         RST     0X38            
4077: FF         RST     0X38            
4078: FF         RST     0X38            
4079: FF         RST     0X38            
407A: FF         RST     0X38            
407B: FF         RST     0X38            
407C: FF         RST     0X38            
407D: FF         RST     0X38            
407E: FF         RST     0X38            
407F: FF         RST     0X38            
4080: 34         INC     (HL)            
4081: 1F         RRA                     
4082: 30 1F      JR      NC,$40A3        
4084: 30 1F      JR      NC,$40A5        
4086: 68         LD      L,B             
4087: 3F         CCF                     
4088: 6C         LD      L,H             
4089: 3F         CCF                     
408A: 66         LD      H,(HL)          
408B: 3F         CCF                     
408C: 70         LD      (HL),B          
408D: 1F         RRA                     
408E: 5F         LD      E,A             
408F: 2F         CPL                     
4090: 01 3E 22   LD      BC,$223E        
4093: 1C         INC     E               
4094: 14         INC     D               
4095: 08 1C 00   LD      ($001C),SP      
4098: 1C         INC     E               
4099: 1C         INC     E               
409A: 22         LD      (HLI),A         
409B: 3E 2A      LD      A,$2A           
409D: 36 1C      LD      (HL),$1C        
409F: 1C         INC     E               
40A0: 7F         LD      A,A             
40A1: FF         RST     0X38            
40A2: 7F         LD      A,A             
40A3: FF         RST     0X38            
40A4: 00         NOP                     
40A5: FF         RST     0X38            
40A6: 18 FF      JR      $40A7           
40A8: 3C         INC     A               
40A9: FF         RST     0X38            
40AA: 7E         LD      A,(HL)          
40AB: FF         RST     0X38            
40AC: 00         NOP                     
40AD: FF         RST     0X38            
40AE: FF         RST     0X38            
40AF: FF         RST     0X38            
40B0: C1         POP     BC              
40B1: 3E 22      LD      A,$22           
40B3: 1C         INC     E               
40B4: 14         INC     D               
40B5: 08 1C 00   LD      ($001C),SP      
40B8: 1C         INC     E               
40B9: 1C         INC     E               
40BA: 22         LD      (HLI),A         
40BB: 3E 2A      LD      A,$2A           
40BD: 36 1C      LD      (HL),$1C        
40BF: 1C         INC     E               
40C0: FF         RST     0X38            
40C1: FF         RST     0X38            
40C2: FF         RST     0X38            
40C3: FF         RST     0X38            
40C4: 00         NOP                     
40C5: FF         RST     0X38            
40C6: 18 FF      JR      $40C7           
40C8: 3C         INC     A               
40C9: FF         RST     0X38            
40CA: 7E         LD      A,(HL)          
40CB: FF         RST     0X38            
40CC: 00         NOP                     
40CD: FF         RST     0X38            
40CE: FF         RST     0X38            
40CF: FF         RST     0X38            
40D0: 00         NOP                     
40D1: 00         NOP                     
40D2: C7         RST     0X00            
40D3: A7         AND     A               
40D4: EC         ???                     
40D5: EF         RST     0X28            
40D6: AB         XOR     E               
40D7: EC         ???                     
40D8: C0         RET     NZ              
40D9: A0         AND     B               
40DA: C7         RST     0X00            
40DB: A7         AND     A               
40DC: AC         XOR     H               
40DD: EF         RST     0X28            
40DE: CF         RST     0X08            
40DF: CC FF FF   CALL    Z,$FFFF         
40E2: FF         RST     0X38            
40E3: FF         RST     0X38            
40E4: 00         NOP                     
40E5: FF         RST     0X38            
40E6: 18 FF      JR      $40E7           
40E8: 3C         INC     A               
40E9: FF         RST     0X38            
40EA: 7E         LD      A,(HL)          
40EB: FF         RST     0X38            
40EC: 00         NOP                     
40ED: FF         RST     0X38            
40EE: FF         RST     0X38            
40EF: FF         RST     0X38            
40F0: 00         NOP                     
40F1: 00         NOP                     
40F2: FD         ???                     
40F3: FB         EI                      
40F4: 0F         RRCA                    
40F5: FF         RST     0X38            
40F6: FB         EI                      
40F7: 0F         RRCA                    
40F8: 05         DEC     B               
40F9: 0B         DEC     BC              
40FA: F5         PUSH    AF              
40FB: FB         EI                      
40FC: 03         INC     BC              
40FD: FF         RST     0X38            
40FE: F5         PUSH    AF              
40FF: 0D         DEC     C               
4100: 00         NOP                     
4101: 00         NOP                     
4102: 00         NOP                     
4103: 00         NOP                     
4104: 01 00 01   LD      BC,$0100        
4107: 00         NOP                     
4108: 03         INC     BC              
4109: 01 03 01   LD      BC,$0103        
410C: 03         INC     BC              
410D: 01 06 03   LD      BC,$0306        
4110: 06 03      LD      B,$03           
4112: 06 03      LD      B,$03           
4114: 0D         DEC     C               
4115: 07         RLCA                    
4116: 0D         DEC     C               
4117: 07         RLCA                    
4118: 0C         INC     C               
4119: 07         RLCA                    
411A: 1A         LD      A,(DE)          
411B: 0F         RRCA                    
411C: 1B         DEC     DE              
411D: 0F         RRCA                    
411E: 1B         DEC     DE              
411F: 0F         RRCA                    
4120: 00         NOP                     
4121: 00         NOP                     
4122: 00         NOP                     
4123: 00         NOP                     
4124: 01 00 01   LD      BC,$0100        
4127: 00         NOP                     
4128: 03         INC     BC              
4129: 01 03 01   LD      BC,$0103        
412C: 00         NOP                     
412D: 01 02 03   LD      BC,$0302        
4130: 06 03      LD      B,$03           
4132: 06 03      LD      B,$03           
4134: 0D         DEC     C               
4135: 07         RLCA                    
4136: 0D         DEC     C               
4137: 07         RLCA                    
4138: 0C         INC     C               
4139: 07         RLCA                    
413A: 18 0F      JR      $414B           
413C: 10 0F      STOP    $0F             
413E: 00         NOP                     
413F: 00         NOP                     
4140: 3F         CCF                     
4141: 00         NOP                     
4142: C0         RET     NZ              
4143: 3F         CCF                     
4144: BA         CP      D               
4145: FF         RST     0X38            
4146: 40         LD      B,B             
4147: FE 08      CP      $08             
4149: FD         ???                     
414A: 01 FD 1C   LD      BC,$1CFD        
414D: 9D         SBC     L               
414E: 0E FE      LD      C,$FE           
4150: 8E         ADC     A,(HL)          
4151: FE CF      CP      $CF             
4153: FF         RST     0X38            
4154: DF         RST     0X18            
4155: FF         RST     0X38            
4156: 9E         SBC     (HL)            
4157: FF         RST     0X38            
4158: 3C         INC     A               
4159: FF         RST     0X38            
415A: 38 FE      JR      C,$415A         
415C: 30 FC      JR      NC,$415A        
415E: 02         LD      (BC),A          
415F: FA 8F 00   LD      A,($008F)       
4162: 00         NOP                     
4163: AF         XOR     A               
4164: 07         RLCA                    
4165: 6F         LD      L,A             
4166: A3         AND     E               
4167: EF         RST     0X28            
4168: 00         NOP                     
4169: EF         RST     0X28            
416A: F0 F7      LD      A,($F7)         
416C: A0         AND     B               
416D: F7         RST     0X30            
416E: 00         NOP                     
416F: E0 0F      LDFF00  ($0F),A         
4171: 0F         RRCA                    
4172: 9F         SBC     A               
4173: DF         RST     0X18            
4174: 1F         RRA                     
4175: 9F         SBC     A               
4176: 1F         RRA                     
4177: BF         CP      A               
4178: 0F         RRCA                    
4179: 3F         CCF                     
417A: 07         RLCA                    
417B: 1F         RRA                     
417C: C0         RET     NZ              
417D: CF         RST     0X08            
417E: 80         ADD     A,B             
417F: E0 34      LDFF00  ($34),A         
4181: 1E 30      LD      E,$30           
4183: 1F         RRA                     
4184: 30 1F      JR      NC,$41A5        
4186: 6C         LD      L,H             
4187: 3F         CCF                     
4188: 6C         LD      L,H             
4189: 3F         CCF                     
418A: 66         LD      H,(HL)          
418B: 3F         CCF                     
418C: F0 1F      LD      A,($1F)         
418E: FF         RST     0X38            
418F: 0F         RRCA                    
4190: 41         LD      B,C             
4191: 3E 22      LD      A,$22           
4193: 1C         INC     E               
4194: 14         INC     D               
4195: 08 1C 00   LD      ($001C),SP      
4198: 18 18      JR      $41B2           
419A: 20 38      JR      NZ,$41D4        
419C: 22         LD      (HLI),A         
419D: 32         LD      (HLD),A         
419E: 0C         INC     C               
419F: 0C         INC     C               
41A0: 04         INC     B               
41A1: 06 28      LD      B,$28           
41A3: EC         ???                     
41A4: 01 E9 A0   LD      BC,$A0E9        
41A7: E3         ???                     
41A8: 64         LD      H,H             
41A9: E7         RST     0X20            
41AA: 4E         LD      C,(HL)          
41AB: EF         RST     0X28            
41AC: 00         NOP                     
41AD: CF         RST     0X08            
41AE: CF         RST     0X08            
41AF: CF         RST     0X08            
41B0: C1         POP     BC              
41B1: 3E 22      LD      A,$22           
41B3: 1C         INC     E               
41B4: 14         INC     D               
41B5: 08 18 00   LD      ($0018),SP      
41B8: 18 18      JR      $41D2           
41BA: 22         LD      (HLI),A         
41BB: 3A         LD      A,(HLD)         
41BC: 22         LD      (HLI),A         
41BD: 22         LD      (HLI),A         
41BE: 1C         INC     E               
41BF: 1C         INC     E               
41C0: 0F         RRCA                    
41C1: 8F         ADC     A,A             
41C2: 67         LD      H,A             
41C3: 6F         LD      L,A             
41C4: 0C         INC     C               
41C5: EF         RST     0X28            
41C6: 00         NOP                     
41C7: EF         RST     0X28            
41C8: 23         INC     HL              
41C9: EF         RST     0X28            
41CA: 70         LD      (HL),B          
41CB: F3         DI                      
41CC: 00         NOP                     
41CD: F8 FE      LDHL    SP,$FE          
41CF: FE 00      CP      $00             
41D1: 00         NOP                     
41D2: 44         LD      B,H             
41D3: 24         INC     H               
41D4: 68         LD      L,B             
41D5: 69         LD      L,C             
41D6: 03         INC     BC              
41D7: 00         NOP                     
41D8: 00         NOP                     
41D9: 00         NOP                     
41DA: 47         LD      B,A             
41DB: 27         DAA                     
41DC: AC         XOR     H               
41DD: ED         ???                     
41DE: C0         RET     NZ              
41DF: C0         RET     NZ              
41E0: 92         SUB     D               
41E1: 92         SUB     D               
41E2: 28 7C      JR      Z,$4260         
41E4: 7C         LD      A,H             
41E5: 44         LD      B,H             
41E6: BA         CP      D               
41E7: C6 7C      ADD     $7C             
41E9: 44         LD      B,H             
41EA: 28 7C      JR      Z,$4268         
41EC: 92         SUB     D               
41ED: 92         SUB     D               
41EE: 00         NOP                     
41EF: 00         NOP                     
41F0: 00         NOP                     
41F1: 00         NOP                     
41F2: 00         NOP                     
41F3: 00         NOP                     
41F4: 00         NOP                     
41F5: 00         NOP                     
41F6: 00         NOP                     
41F7: 00         NOP                     
41F8: 00         NOP                     
41F9: 00         NOP                     
41FA: 00         NOP                     
41FB: 00         NOP                     
41FC: 00         NOP                     
41FD: 00         NOP                     
41FE: 00         NOP                     
41FF: 00         NOP                     
4200: 00         NOP                     
4201: 00         NOP                     
4202: C7         RST     0X00            
4203: A7         AND     A               
4204: EC         ???                     
4205: EF         RST     0X28            
4206: AB         XOR     E               
4207: EC         ???                     
4208: C0         RET     NZ              
4209: A0         AND     B               
420A: C7         RST     0X00            
420B: A7         AND     A               
420C: AC         XOR     H               
420D: EF         RST     0X28            
420E: CF         RST     0X08            
420F: CC 00 00   CALL    Z,$0000         
4212: C7         RST     0X00            
4213: A7         AND     A               
4214: EC         ???                     
4215: EF         RST     0X28            
4216: AB         XOR     E               
4217: EC         ???                     
4218: C0         RET     NZ              
4219: A0         AND     B               
421A: C7         RST     0X00            
421B: A7         AND     A               
421C: AC         XOR     H               
421D: EF         RST     0X28            
421E: CF         RST     0X08            
421F: CC 00 00   CALL    Z,$0000         
4222: 01 00 03   LD      BC,$0300        
4225: 01 02 01   LD      BC,$0102        
4228: 06 03      LD      B,$03           
422A: 00         NOP                     
422B: 00         NOP                     
422C: 00         NOP                     
422D: 01 02 03   LD      BC,$0302        
4230: 06 03      LD      B,$03           
4232: 00         NOP                     
4233: 01 18 08   LD      BC,$0818        
4236: 1A         LD      A,(DE)          
4237: 0F         RRCA                    
4238: 18 0F      JR      $4249           
423A: 37         SCF                     
423B: 1F         RRA                     
423C: 21 1F 00   LD      HL,$001F        
423F: 01 63 00   LD      BC,$0063        
4242: 80         ADD     A,B             
4243: 67         LD      H,A             
4244: 66         LD      H,(HL)          
4245: E7         RST     0X20            
4246: C0         RET     NZ              
4247: E0 80      LDFF00  ($80),A         
4249: 80         ADD     A,B             
424A: 00         NOP                     
424B: 04         INC     B               
424C: 00         NOP                     
424D: 9C         SBC     H               
424E: CC CC 8E   CALL    Z,$8ECC         
4251: CE 87      ADC     $87             
4253: DF         RST     0X18            
4254: 06 3F      LD      B,$3F           
4256: 6C         LD      L,H             
4257: 7F         LD      A,A             
4258: 58         LD      E,B             
4259: 5E         LD      E,(HL)          
425A: 10 1C      STOP    $1C             
425C: 90         SUB     B               
425D: 9C         SBC     H               
425E: 02         LD      (BC),A          
425F: 82         ADD     A,D             
4260: 87         ADD     A,A             
4261: 00         NOP                     
4262: 00         NOP                     
4263: 07         RLCA                    
4264: 69         LD      L,C             
4265: 69         LD      L,C             
4266: EC         ???                     
4267: EC         ???                     
4268: 01 09 33   LD      BC,$3309        
426B: 37         SCF                     
426C: 20 77      JR      NZ,$42E5        
426E: 00         NOP                     
426F: E0 0F      LDFF00  ($0F),A         
4271: 0F         RRCA                    
4272: 86         ADD     A,(HL)          
4273: C6 10      ADD     $10             
4275: 90         SUB     B               
4276: 1D         DEC     E               
4277: BD         CP      L               
4278: 0C         INC     C               
4279: 3C         INC     A               
427A: 01 19 C0   LD      BC,$C019        
427D: CB 80      SET     1,E             
427F: E0 D8      LDFF00  ($D8),A         
4281: 78         LD      A,B             
4282: D0         RET     NC              
4283: 7F         LD      A,A             
4284: D0         RET     NC              
4285: 7E         LD      A,(HL)          
4286: B8         CP      B               
4287: FC         ???                     
4288: 60         LD      H,B             
4289: 31 07 07   LD      SP,$0707        
428C: E0 0F      LDFF00  ($0F),A         
428E: E0 00      LDFF00  ($00),A         
4290: 41         LD      B,C             
4291: 3E 22      LD      A,$22           
4293: 04         INC     B               
4294: 10 00      STOP    $00             
4296: 04         INC     B               
4297: 00         NOP                     
4298: 08 08 00   LD      ($0008),SP      
429B: 18 00      JR      $429D           
429D: 10 00      STOP    $00             
429F: 00         NOP                     
42A0: 04         INC     B               
42A1: 06 28      LD      B,$28           
42A3: 2C         INC     L               
42A4: 00         NOP                     
42A5: 29         ADD     HL,HL           
42A6: 00         NOP                     
42A7: A3         AND     E               
42A8: 00         NOP                     
42A9: E1         POP     HL              
42AA: 8D         ADC     A,L             
42AB: ED         ???                     
42AC: 00         NOP                     
42AD: CC CC CC   CALL    Z,$CCCC         
42B0: C1         POP     BC              
42B1: 3E 22      LD      A,$22           
42B3: 14         INC     D               
42B4: 04         INC     B               
42B5: 00         NOP                     
42B6: 08 00 10   LD      ($1000),SP      
42B9: 10 20      STOP    $20             
42BB: 20 20      JR      NZ,$42DD        
42BD: 20 04      JR      NZ,$42C3        
42BF: 04         INC     B               
42C0: 03         INC     BC              
42C1: 83         ADD     A,E             
42C2: 67         LD      H,A             
42C3: 67         LD      H,A             
42C4: 07         RLCA                    
42C5: E7         RST     0X20            
42C6: 07         RLCA                    
42C7: E7         RST     0X20            
42C8: 03         INC     BC              
42C9: E3         ???                     
42CA: 30 F0      JR      NC,$42BC        
42CC: 00         NOP                     
42CD: F0 0E      LD      A,($0E)         
42CF: 0E 00      LD      C,$00           
42D1: 00         NOP                     
42D2: 44         LD      B,H             
42D3: 24         INC     H               
42D4: 48         LD      C,B             
42D5: 49         LD      C,C             
42D6: 01 00 00   LD      BC,$0000        
42D9: 00         NOP                     
42DA: 06 26      LD      B,$26           
42DC: 20 20      JR      NZ,$42FE        
42DE: 80         ADD     A,B             
42DF: 80         ADD     A,B             
42E0: 00         NOP                     
42E1: 00         NOP                     
42E2: 44         LD      B,H             
42E3: 44         LD      B,H             
42E4: 10 38      STOP    $38             
42E6: 38 28      JR      C,$4310         
42E8: 10 38      STOP    $38             
42EA: 44         LD      B,H             
42EB: 44         LD      B,H             
42EC: 00         NOP                     
42ED: 00         NOP                     
42EE: 00         NOP                     
42EF: 00         NOP                     
42F0: 00         NOP                     
42F1: 00         NOP                     
42F2: 00         NOP                     
42F3: 00         NOP                     
42F4: 00         NOP                     
42F5: 00         NOP                     
42F6: 00         NOP                     
42F7: 00         NOP                     
42F8: 00         NOP                     
42F9: 00         NOP                     
42FA: 00         NOP                     
42FB: 00         NOP                     
42FC: 00         NOP                     
42FD: 00         NOP                     
42FE: 00         NOP                     
42FF: 00         NOP                     
4300: 00         NOP                     
4301: 00         NOP                     
4302: FD         ???                     
4303: FB         EI                      
4304: 0F         RRCA                    
4305: FF         RST     0X38            
4306: FB         EI                      
4307: 0F         RRCA                    
4308: 05         DEC     B               
4309: 0B         DEC     BC              
430A: F5         PUSH    AF              
430B: FB         EI                      
430C: 03         INC     BC              
430D: FF         RST     0X38            
430E: F5         PUSH    AF              
430F: 0D         DEC     C               
4310: 00         NOP                     
4311: 00         NOP                     
4312: FD         ???                     
4313: FB         EI                      
4314: 0F         RRCA                    
4315: FF         RST     0X38            
4316: FB         EI                      
4317: 0F         RRCA                    
4318: 05         DEC     B               
4319: 0B         DEC     BC              
431A: F5         PUSH    AF              
431B: FB         EI                      
431C: 03         INC     BC              
431D: FF         RST     0X38            
431E: F5         PUSH    AF              
431F: 0D         DEC     C               
4320: 00         NOP                     
4321: 00         NOP                     
4322: 01 00 02   LD      BC,$0200        
4325: 00         NOP                     
4326: 02         LD      (BC),A          
4327: 01 04 01   LD      BC,$0104        
432A: 00         NOP                     
432B: 00         NOP                     
432C: 00         NOP                     
432D: 01 02 03   LD      BC,$0302        
4330: 00         NOP                     
4331: 01 00 00   LD      BC,$0000        
4334: 00         NOP                     
4335: 00         NOP                     
4336: 1A         LD      A,(DE)          
4337: 0E 18      LD      C,$18           
4339: 0C         INC     C               
433A: 15         DEC     D               
433B: 1D         DEC     E               
433C: 00         NOP                     
433D: 00         NOP                     
433E: 00         NOP                     
433F: 00         NOP                     
4340: 43         LD      B,E             
4341: 00         NOP                     
4342: 80         ADD     A,B             
4343: 45         LD      B,L             
4344: 40         LD      B,B             
4345: 40         LD      B,B             
4346: 80         ADD     A,B             
4347: 80         ADD     A,B             
4348: 80         ADD     A,B             
4349: 80         ADD     A,B             
434A: 04         INC     B               
434B: 04         INC     B               
434C: 18 98      JR      $42E6           
434E: 88         ADC     A,B             
434F: 88         ADC     A,B             
4350: 02         LD      (BC),A          
4351: 02         LD      (BC),A          
4352: 4D         LD      C,L             
4353: 4D         LD      C,L             
4354: 2C         INC     L               
4355: 2C         INC     L               
4356: 60         LD      H,B             
4357: 61         LD      H,C             
4358: 58         LD      E,B             
4359: 58         LD      E,B             
435A: 10 18      STOP    $18             
435C: 10 1C      STOP    $1C             
435E: 02         LD      (BC),A          
435F: 02         LD      (BC),A          
4360: 86         ADD     A,(HL)          
4361: 00         NOP                     
4362: 00         NOP                     
4363: 04         INC     B               
4364: 29         ADD     HL,HL           
4365: 29         ADD     HL,HL           
4366: 8C         ADC     A,H             
4367: 8C         ADC     A,H             
4368: 01 09 10   LD      BC,$1009        
436B: 14         INC     D               
436C: 00         NOP                     
436D: 14         INC     D               
436E: 00         NOP                     
436F: 80         ADD     A,B             
4370: 0F         RRCA                    
4371: 0F         RRCA                    
4372: 80         ADD     A,B             
4373: C0         RET     NZ              
4374: 10 90      STOP    $90             
4376: 15         DEC     D               
4377: 95         SUB     L               
4378: 00         NOP                     
4379: 00         NOP                     
437A: 01 09 C0   LD      BC,$C009        
437D: C9         RET                     
437E: 80         ADD     A,B             
437F: E0 18      LDFF00  ($18),A         
4381: 38 5C      JR      C,$43DF         
4383: 7C         LD      A,H             
4384: D8         RET     C               
4385: 78         LD      A,B             
4386: B0         OR      B               
4387: B0         OR      B               
4388: 00         NOP                     
4389: 00         NOP                     
438A: 05         DEC     B               
438B: 05         DEC     B               
438C: C0         RET     NZ              
438D: 0C         INC     C               
438E: 80         ADD     A,B             
438F: 00         NOP                     
4390: 01 06 00   LD      BC,$0006        
4393: 00         NOP                     
4394: 00         NOP                     
4395: 00         NOP                     
4396: 04         INC     B               
4397: 00         NOP                     
4398: 00         NOP                     
4399: 00         NOP                     
439A: 00         NOP                     
439B: 00         NOP                     
439C: 00         NOP                     
439D: 10 00      STOP    $00             
439F: 00         NOP                     
43A0: 04         INC     B               
43A1: 06 28      LD      B,$28           
43A3: 2C         INC     L               
43A4: 01 09 82   LD      BC,$8209        
43A7: 82         ADD     A,D             
43A8: 00         NOP                     
43A9: 00         NOP                     
43AA: 0D         DEC     C               
43AB: 2D         DEC     L               
43AC: 00         NOP                     
43AD: 00         NOP                     
43AE: CC CC C1   CALL    Z,$C1CC         
43B1: 04         INC     B               
43B2: 00         NOP                     
43B3: 10 04      STOP    $04             
43B5: 00         NOP                     
43B6: 08 00 10   LD      ($1000),SP      
43B9: 10 20      STOP    $20             
43BB: 20 20      JR      NZ,$43DD        
43BD: 20 04      JR      NZ,$43C3        
43BF: 04         INC     B               
43C0: 02         LD      (BC),A          
43C1: 82         ADD     A,D             
43C2: 44         LD      B,H             
43C3: 44         LD      B,H             
43C4: 80         ADD     A,B             
43C5: 80         ADD     A,B             
43C6: 00         NOP                     
43C7: 00         NOP                     
43C8: 03         INC     BC              
43C9: 03         INC     BC              
43CA: 80         ADD     A,B             
43CB: 80         ADD     A,B             
43CC: 00         NOP                     
43CD: 90         SUB     B               
43CE: 0E 0E      LD      C,$0E           
43D0: 00         NOP                     
43D1: 00         NOP                     
43D2: 04         INC     B               
43D3: 04         INC     B               
43D4: 08 08 00   LD      ($0008),SP      
43D7: 00         NOP                     
43D8: 00         NOP                     
43D9: 00         NOP                     
43DA: 06 26      LD      B,$26           
43DC: 20 20      JR      NZ,$43FE        
43DE: 80         ADD     A,B             
43DF: 80         ADD     A,B             
43E0: 00         NOP                     
43E1: 00         NOP                     
43E2: 00         NOP                     
43E3: 00         NOP                     
43E4: 28 28      JR      Z,$440E         
43E6: 10 00      STOP    $00             
43E8: 28 28      JR      Z,$4412         
43EA: 00         NOP                     
43EB: 00         NOP                     
43EC: 00         NOP                     
43ED: 00         NOP                     
43EE: 00         NOP                     
43EF: 00         NOP                     
43F0: 00         NOP                     
43F1: 00         NOP                     
43F2: 00         NOP                     
43F3: 00         NOP                     
43F4: 00         NOP                     
43F5: 00         NOP                     
43F6: 00         NOP                     
43F7: 00         NOP                     
43F8: 00         NOP                     
43F9: 00         NOP                     
43FA: 00         NOP                     
43FB: 00         NOP                     
43FC: 00         NOP                     
43FD: 00         NOP                     
43FE: 00         NOP                     
43FF: 00         NOP                     
4400: 00         NOP                     
4401: 00         NOP                     
4402: C7         RST     0X00            
4403: A7         AND     A               
4404: EC         ???                     
4405: EF         RST     0X28            
4406: AB         XOR     E               
4407: AC         XOR     H               
4408: 80         ADD     A,B             
4409: 80         ADD     A,B             
440A: C5         PUSH    BC              
440B: A5         AND     L               
440C: AC         XOR     H               
440D: ED         ???                     
440E: CC CC 00   CALL    Z,$00CC         
4411: 00         NOP                     
4412: C7         RST     0X00            
4413: A7         AND     A               
4414: EC         ???                     
4415: EF         RST     0X28            
4416: AB         XOR     E               
4417: EC         ???                     
4418: 80         ADD     A,B             
4419: 80         ADD     A,B             
441A: 87         ADD     A,A             
441B: 87         ADD     A,A             
441C: AC         XOR     H               
441D: EE CC      XOR     $CC             
441F: CC 00 00   CALL    Z,$0000         
4422: 00         NOP                     
4423: 00         NOP                     
4424: 00         NOP                     
4425: 00         NOP                     
4426: 00         NOP                     
4427: 00         NOP                     
4428: 04         INC     B               
4429: 01 00 00   LD      BC,$0000        
442C: 00         NOP                     
442D: 00         NOP                     
442E: 02         LD      (BC),A          
442F: 03         INC     BC              
4430: 00         NOP                     
4431: 00         NOP                     
4432: 00         NOP                     
4433: 00         NOP                     
4434: 00         NOP                     
4435: 00         NOP                     
4436: 18 08      JR      $4440           
4438: 10 00      STOP    $00             
443A: 01 01 00   LD      BC,$0001        
443D: 00         NOP                     
443E: 00         NOP                     
443F: 00         NOP                     
4440: 02         LD      (BC),A          
4441: 00         NOP                     
4442: 00         NOP                     
4443: 44         LD      B,H             
4444: 00         NOP                     
4445: 00         NOP                     
4446: 00         NOP                     
4447: 00         NOP                     
4448: 80         ADD     A,B             
4449: 80         ADD     A,B             
444A: 04         INC     B               
444B: 04         INC     B               
444C: 10 10      STOP    $10             
444E: 00         NOP                     
444F: 00         NOP                     
4450: 02         LD      (BC),A          
4451: 02         LD      (BC),A          
4452: 00         NOP                     
4453: 00         NOP                     
4454: 04         INC     B               
4455: 04         INC     B               
4456: 20 20      JR      NZ,$4478        
4458: 48         LD      C,B             
4459: 48         LD      C,B             
445A: 00         NOP                     
445B: 00         NOP                     
445C: 00         NOP                     
445D: 00         NOP                     
445E: 00         NOP                     
445F: 00         NOP                     
4460: 02         LD      (BC),A          
4461: 00         NOP                     
4462: 00         NOP                     
4463: 00         NOP                     
4464: 21 21 00   LD      HL,$0021        
4467: 00         NOP                     
4468: 01 09 00   LD      BC,$0009        
446B: 00         NOP                     
446C: 00         NOP                     
446D: 14         INC     D               
446E: 00         NOP                     
446F: 80         ADD     A,B             
4470: 00         NOP                     
4471: 00         NOP                     
4472: 00         NOP                     
4473: 00         NOP                     
4474: 10 10      STOP    $10             
4476: 05         DEC     B               
4477: 05         DEC     B               
4478: 00         NOP                     
4479: 00         NOP                     
447A: 01 09 80   LD      BC,$8009        
447D: 81         ADD     A,C             
447E: 00         NOP                     
447F: 00         NOP                     
4480: 08 28 0C   LD      ($0C28),SP      
4483: 0C         INC     C               
4484: 80         ADD     A,B             
4485: 00         NOP                     
4486: 00         NOP                     
4487: 00         NOP                     
4488: 00         NOP                     
4489: 00         NOP                     
448A: 01 01 00   LD      BC,$0001        
448D: 00         NOP                     
448E: 00         NOP                     
448F: 00         NOP                     
4490: 00         NOP                     
4491: 00         NOP                     
4492: 00         NOP                     
4493: 00         NOP                     
4494: 00         NOP                     
4495: 00         NOP                     
4496: 00         NOP                     
4497: 00         NOP                     
4498: 00         NOP                     
4499: 00         NOP                     
449A: 00         NOP                     
449B: 00         NOP                     
449C: 00         NOP                     
449D: 10 00      STOP    $00             
449F: 00         NOP                     
44A0: 04         INC     B               
44A1: 04         INC     B               
44A2: 20 20      JR      NZ,$44C4        
44A4: 01 01 02   LD      BC,$0201        
44A7: 02         LD      (BC),A          
44A8: 00         NOP                     
44A9: 00         NOP                     
44AA: 01 21 00   LD      BC,$0021        
44AD: 00         NOP                     
44AE: 00         NOP                     
44AF: 00         NOP                     
44B0: 41         LD      B,C             
44B1: 00         NOP                     
44B2: 00         NOP                     
44B3: 10 04      STOP    $04             
44B5: 00         NOP                     
44B6: 00         NOP                     
44B7: 00         NOP                     
44B8: 00         NOP                     
44B9: 00         NOP                     
44BA: 20 20      JR      NZ,$44DC        
44BC: 00         NOP                     
44BD: 00         NOP                     
44BE: 04         INC     B               
44BF: 04         INC     B               
44C0: 02         LD      (BC),A          
44C1: 82         ADD     A,D             
44C2: 04         INC     B               
44C3: 04         INC     B               
44C4: 80         ADD     A,B             
44C5: 80         ADD     A,B             
44C6: 00         NOP                     
44C7: 00         NOP                     
44C8: 03         INC     BC              
44C9: 03         INC     BC              
44CA: 80         ADD     A,B             
44CB: 80         ADD     A,B             
44CC: 00         NOP                     
44CD: 80         ADD     A,B             
44CE: 06 06      LD      B,$06           
44D0: 00         NOP                     
44D1: 00         NOP                     
44D2: 04         INC     B               
44D3: 04         INC     B               
44D4: 00         NOP                     
44D5: 00         NOP                     
44D6: 00         NOP                     
44D7: 00         NOP                     
44D8: 00         NOP                     
44D9: 00         NOP                     
44DA: 02         LD      (BC),A          
44DB: 02         LD      (BC),A          
44DC: 00         NOP                     
44DD: 00         NOP                     
44DE: 80         ADD     A,B             
44DF: 80         ADD     A,B             
44E0: 00         NOP                     
44E1: 00         NOP                     
44E2: 00         NOP                     
44E3: 00         NOP                     
44E4: 00         NOP                     
44E5: 00         NOP                     
44E6: 00         NOP                     
44E7: 00         NOP                     
44E8: 00         NOP                     
44E9: 00         NOP                     
44EA: 3F         CCF                     
44EB: 00         NOP                     
44EC: 7F         LD      A,A             
44ED: 3F         CCF                     
44EE: 60         LD      H,B             
44EF: 1F         RRA                     
44F0: 3F         CCF                     
44F1: 00         NOP                     
44F2: 3F         CCF                     
44F3: 00         NOP                     
44F4: 00         NOP                     
44F5: 00         NOP                     
44F6: 03         INC     BC              
44F7: 00         NOP                     
44F8: 00         NOP                     
44F9: 00         NOP                     
44FA: 00         NOP                     
44FB: 00         NOP                     
44FC: 00         NOP                     
44FD: 00         NOP                     
44FE: 00         NOP                     
44FF: 00         NOP                     
4500: 00         NOP                     
4501: 00         NOP                     
4502: D9         RETI                    
4503: D9         RETI                    
4504: 0D         DEC     C               
4505: 9D         SBC     L               
4506: 39         ADD     HL,SP           
4507: 0D         DEC     C               
4508: 01 09 F1   LD      BC,$F109        
450B: FB         EI                      
450C: 03         INC     BC              
450D: FF         RST     0X38            
450E: F5         PUSH    AF              
450F: 0D         DEC     C               
4510: 00         NOP                     
4511: 00         NOP                     
4512: FD         ???                     
4513: FB         EI                      
4514: 0F         RRCA                    
4515: FF         RST     0X38            
4516: FB         EI                      
4517: 0F         RRCA                    
4518: 05         DEC     B               
4519: 0B         DEC     BC              
451A: 65         LD      H,L             
451B: 6B         LD      L,E             
451C: 03         INC     BC              
451D: 63         LD      H,E             
451E: C5         PUSH    BC              
451F: 0D         DEC     C               
4520: 00         NOP                     
4521: 00         NOP                     
4522: C2 A2 88   JP      NZ,$88A2        
4525: 88         ADC     A,B             
4526: 88         ADC     A,B             
4527: 8C         ADC     A,H             
4528: 00         NOP                     
4529: 00         NOP                     
452A: 85         ADD     A,L             
452B: 85         ADD     A,L             
452C: AC         XOR     H               
452D: EC         ???                     
452E: 80         ADD     A,B             
452F: 80         ADD     A,B             
4530: 00         NOP                     
4531: 00         NOP                     
4532: 87         ADD     A,A             
4533: 87         ADD     A,A             
4534: E4         ???                     
4535: E6 00      AND     $00             
4537: 00         NOP                     
4538: 00         NOP                     
4539: 00         NOP                     
453A: 84         ADD     A,H             
453B: 84         ADD     A,H             
453C: 80         ADD     A,B             
453D: C0         RET     NZ              
453E: 00         NOP                     
453F: 00         NOP                     
4540: 00         NOP                     
4541: 00         NOP                     
4542: 00         NOP                     
4543: 00         NOP                     
4544: 0F         RRCA                    
4545: 00         NOP                     
4546: 1F         RRA                     
4547: 0B         DEC     BC              
4548: 3F         CCF                     
4549: 1B         DEC     DE              
454A: 3C         INC     A               
454B: 1B         DEC     DE              
454C: 78         LD      A,B             
454D: 37         SCF                     
454E: 79         LD      A,C             
454F: 32         LD      (HLD),A         
4550: 71         LD      (HL),C          
4551: 20 62      JR      NZ,$45B5        
4553: 00         NOP                     
4554: 7F         LD      A,A             
4555: 00         NOP                     
4556: 3F         CCF                     
4557: 00         NOP                     
4558: 0F         RRCA                    
4559: 00         NOP                     
455A: 00         NOP                     
455B: 00         NOP                     
455C: 07         RLCA                    
455D: 00         NOP                     
455E: 00         NOP                     
455F: 00         NOP                     
4560: 00         NOP                     
4561: 00         NOP                     
4562: 02         LD      (BC),A          
4563: 22         LD      (HLI),A         
4564: 88         ADC     A,B             
4565: 88         ADC     A,B             
4566: 08 0C 00   LD      ($000C),SP      
4569: 00         NOP                     
456A: 05         DEC     B               
456B: 05         DEC     B               
456C: A0         AND     B               
456D: E0 80      LDFF00  ($80),A         
456F: 80         ADD     A,B             
4570: 00         NOP                     
4571: 00         NOP                     
4572: 85         ADD     A,L             
4573: 85         ADD     A,L             
4574: 20 20      JR      NZ,$4596        
4576: 00         NOP                     
4577: 00         NOP                     
4578: 00         NOP                     
4579: 00         NOP                     
457A: 84         ADD     A,H             
457B: 84         ADD     A,H             
457C: 80         ADD     A,B             
457D: C0         RET     NZ              
457E: 00         NOP                     
457F: 00         NOP                     
4580: 00         NOP                     
4581: 00         NOP                     
4582: 00         NOP                     
4583: 00         NOP                     
4584: 00         NOP                     
4585: 00         NOP                     
4586: 00         NOP                     
4587: 07         RLCA                    
4588: 07         RLCA                    
4589: 08 07 0F   LD      ($0F07),SP      
458C: 00         NOP                     
458D: 07         RLCA                    
458E: 01 00 00   LD      BC,$0000        
4591: 01 00 00   LD      BC,$0000        
4594: 00         NOP                     
4595: 00         NOP                     
4596: 00         NOP                     
4597: 00         NOP                     
4598: 00         NOP                     
4599: 00         NOP                     
459A: 00         NOP                     
459B: 00         NOP                     
459C: 00         NOP                     
459D: 00         NOP                     
459E: 00         NOP                     
459F: 00         NOP                     
45A0: 00         NOP                     
45A1: 00         NOP                     
45A2: 00         NOP                     
45A3: 00         NOP                     
45A4: 00         NOP                     
45A5: 00         NOP                     
45A6: 00         NOP                     
45A7: 00         NOP                     
45A8: 00         NOP                     
45A9: 0C         INC     C               
45AA: 04         INC     B               
45AB: 0B         DEC     BC              
45AC: 03         INC     BC              
45AD: 06 01      LD      B,$01           
45AF: 03         INC     BC              
45B0: 00         NOP                     
45B1: 07         RLCA                    
45B2: 03         INC     BC              
45B3: 04         INC     B               
45B4: 00         NOP                     
45B5: 03         INC     BC              
45B6: 00         NOP                     
45B7: 01 00 00   LD      BC,$0000        
45BA: 00         NOP                     
45BB: 00         NOP                     
45BC: 00         NOP                     
45BD: 00         NOP                     
45BE: 00         NOP                     
45BF: 00         NOP                     
45C0: 00         NOP                     
45C1: 00         NOP                     
45C2: 00         NOP                     
45C3: 00         NOP                     
45C4: 00         NOP                     
45C5: 00         NOP                     
45C6: 00         NOP                     
45C7: 00         NOP                     
45C8: 00         NOP                     
45C9: 00         NOP                     
45CA: 00         NOP                     
45CB: 00         NOP                     
45CC: 00         NOP                     
45CD: 00         NOP                     
45CE: 00         NOP                     
45CF: 00         NOP                     
45D0: 00         NOP                     
45D1: 00         NOP                     
45D2: 00         NOP                     
45D3: 00         NOP                     
45D4: 00         NOP                     
45D5: 01 00 01   LD      BC,$0100        
45D8: 00         NOP                     
45D9: 01 00 01   LD      BC,$0100        
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
45ED: 01 01 02   LD      BC,$0201        
45F0: 03         INC     BC              
45F1: 05         DEC     B               
45F2: 01 07 07   LD      BC,$0707        
45F5: 0B         DEC     BC              
45F6: 02         LD      (BC),A          
45F7: 0F         RRCA                    
45F8: 00         NOP                     
45F9: 06 00      LD      B,$00           
45FB: 02         LD      (BC),A          
45FC: 00         NOP                     
45FD: 00         NOP                     
45FE: 00         NOP                     
45FF: 00         NOP                     
4600: 00         NOP                     
4601: 00         NOP                     
4602: C3 A3 A8   JP      $A8A3           
4605: A9         XOR     C               
4606: 88         ADC     A,B             
4607: 8C         ADC     A,H             
4608: 80         ADD     A,B             
4609: 80         ADD     A,B             
460A: 85         ADD     A,L             
460B: 85         ADD     A,L             
460C: AC         XOR     H               
460D: ED         ???                     
460E: CC CC 00   CALL    Z,$00CC         
4611: 00         NOP                     
4612: 87         ADD     A,A             
4613: 87         ADD     A,A             
4614: EC         ???                     
4615: EF         RST     0X28            
4616: AA         XOR     D               
4617: EC         ???                     
4618: 80         ADD     A,B             
4619: 80         ADD     A,B             
461A: 87         ADD     A,A             
461B: 87         ADD     A,A             
461C: 80         ADD     A,B             
461D: C0         RET     NZ              
461E: CC CC 00   CALL    Z,$00CC         
4621: 00         NOP                     
4622: 99         SBC     C               
4623: 99         SBC     C               
4624: 00         NOP                     
4625: 00         NOP                     
4626: 11 01 00   LD      DE,$0001        
4629: 00         NOP                     
462A: C1         POP     BC              
462B: C1         POP     BC              
462C: 00         NOP                     
462D: 84         ADD     A,H             
462E: 05         DEC     B               
462F: 0D         DEC     C               
4630: 00         NOP                     
4631: 00         NOP                     
4632: B1         OR      C               
4633: B3         OR      E               
4634: 04         INC     B               
4635: 04         INC     B               
4636: 00         NOP                     
4637: 00         NOP                     
4638: 05         DEC     B               
4639: 03         INC     BC              
463A: 20 20      JR      NZ,$465C        
463C: 00         NOP                     
463D: 00         NOP                     
463E: 81         ADD     A,C             
463F: 01 00 00   LD      BC,$0000        
4642: 00         NOP                     
4643: 00         NOP                     
4644: 00         NOP                     
4645: 00         NOP                     
4646: C0         RET     NZ              
4647: 00         NOP                     
4648: F0 40      LD      A,($40)         
464A: F8 70      LDHL    SP,$70          
464C: BC         CP      H               
464D: 70         LD      (HL),B          
464E: 1E F4      LD      E,$F4           
4650: 16 EC      LD      D,$EC           
4652: 16 68      LD      D,$68           
4654: FE 00      CP      $00             
4656: FC         ???                     
4657: 00         NOP                     
4658: F0 00      LD      A,($00)         
465A: 00         NOP                     
465B: 00         NOP                     
465C: C0         RET     NZ              
465D: 00         NOP                     
465E: 00         NOP                     
465F: 00         NOP                     
4660: 00         NOP                     
4661: 00         NOP                     
4662: 91         SUB     C               
4663: 91         SUB     C               
4664: 00         NOP                     
4665: 00         NOP                     
4666: 10 00      STOP    $00             
4668: 00         NOP                     
4669: 00         NOP                     
466A: 41         LD      B,C             
466B: 41         LD      B,C             
466C: 00         NOP                     
466D: 84         ADD     A,H             
466E: 04         INC     B               
466F: 0C         INC     C               
4670: 00         NOP                     
4671: 00         NOP                     
4672: 01 03 04   LD      BC,$0403        
4675: 04         INC     B               
4676: 00         NOP                     
4677: 00         NOP                     
4678: 00         NOP                     
4679: 02         LD      (BC),A          
467A: 20 20      JR      NZ,$469C        
467C: 00         NOP                     
467D: 00         NOP                     
467E: 00         NOP                     
467F: 00         NOP                     
4680: 00         NOP                     
4681: 00         NOP                     
4682: 00         NOP                     
4683: 0C         INC     C               
4684: 00         NOP                     
4685: 07         RLCA                    
4686: 0C         INC     C               
4687: 8B         ADC     A,E             
4688: 9E         SBC     (HL)            
4689: 5D         LD      E,L             
468A: FF         RST     0X38            
468B: 98         SBC     B               
468C: FE D9      CP      $D9             
468E: AF         XOR     A               
468F: DE 73      SBC     $73             
4691: CD 1F 61   CALL    $611F           
4694: 0E 1D      LD      C,$1D           
4696: 0F         RRCA                    
4697: 1E 07      LD      E,$07           
4699: 0F         RRCA                    
469A: 0C         INC     C               
469B: 03         INC     BC              
469C: 0F         RRCA                    
469D: 0C         INC     C               
469E: 14         INC     D               
469F: 14         INC     D               
46A0: 00         NOP                     
46A1: 00         NOP                     
46A2: 00         NOP                     
46A3: 0C         INC     C               
46A4: 00         NOP                     
46A5: 07         RLCA                    
46A6: 0C         INC     C               
46A7: 0B         DEC     BC              
46A8: 1E 1D      LD      E,$1D           
46AA: 3F         CCF                     
46AB: 18 3E      JR      $46EB           
46AD: D9         RETI                    
46AE: EF         RST     0X28            
46AF: 1E F3      LD      E,$F3           
46B1: CD BF C1   CALL    $C1BF           
46B4: 6E         LD      L,(HL)          
46B5: FD         ???                     
46B6: CF         RST     0X08            
46B7: FE 07      CP      $07             
46B9: CF         RST     0X08            
46BA: 0C         INC     C               
46BB: 03         INC     BC              
46BC: 0F         RRCA                    
46BD: 0C         INC     C               
46BE: 14         INC     D               
46BF: 14         INC     D               
46C0: 00         NOP                     
46C1: 0C         INC     C               
46C2: 00         NOP                     
46C3: 07         RLCA                    
46C4: 0C         INC     C               
46C5: 0B         DEC     BC              
46C6: 1E 1D      LD      E,$1D           
46C8: 3F         CCF                     
46C9: 18 3E      JR      $4709           
46CB: 19         ADD     HL,DE           
46CC: 0F         RRCA                    
46CD: 1E 13      LD      E,$13           
46CF: 6D         LD      L,L             
46D0: 3F         CCF                     
46D1: C1         POP     BC              
46D2: 6E         LD      L,(HL)          
46D3: BD         CP      L               
46D4: 4F         LD      C,A             
46D5: BE         CP      (HL)            
46D6: 67         LD      H,A             
46D7: AF         XOR     A               
46D8: 2C         INC     L               
46D9: C3 0F AC   JP      $AC0F           
46DC: 0C         INC     C               
46DD: CC 0C 4C   CALL    Z,$4C0C         
46E0: 00         NOP                     
46E1: 0C         INC     C               
46E2: 00         NOP                     
46E3: 07         RLCA                    
46E4: 0C         INC     C               
46E5: 0B         DEC     BC              
46E6: 1E 1D      LD      E,$1D           
46E8: 3F         CCF                     
46E9: 18 1E      JR      $4709           
46EB: 79         LD      A,C             
46EC: 6F         LD      L,A             
46ED: 9E         SBC     (HL)            
46EE: F3         DI                      
46EF: 0D         DEC     C               
46F0: FF         RST     0X38            
46F1: C1         POP     BC              
46F2: AE         XOR     (HL)            
46F3: DD         ???                     
46F4: 0F         RRCA                    
46F5: FE 07      CP      $07             
46F7: 0F         RRCA                    
46F8: 0C         INC     C               
46F9: 03         INC     BC              
46FA: 0F         RRCA                    
46FB: 0C         INC     C               
46FC: 0C         INC     C               
46FD: 0C         INC     C               
46FE: 0C         INC     C               
46FF: 0C         INC     C               
4700: 00         NOP                     
4701: 00         NOP                     
4702: 99         SBC     C               
4703: 99         SBC     C               
4704: 0D         DEC     C               
4705: 1D         DEC     E               
4706: 19         ADD     HL,DE           
4707: 09         ADD     HL,BC           
4708: 00         NOP                     
4709: 00         NOP                     
470A: F1         POP     AF              
470B: F1         POP     AF              
470C: 01 E5 C5   LD      BC,$C5E5        
470F: 0D         DEC     C               
4710: 00         NOP                     
4711: 00         NOP                     
4712: BD         CP      L               
4713: BB         CP      E               
4714: 05         DEC     B               
4715: 35         DEC     (HL)            
4716: 01 01 05   LD      BC,$0501        
4719: 03         INC     BC              
471A: 64         LD      H,H             
471B: 6A         LD      L,D             
471C: 00         NOP                     
471D: 00         NOP                     
471E: 81         ADD     A,C             
471F: 01 00 00   LD      BC,$0000        
4722: 00         NOP                     
4723: 00         NOP                     
4724: 38 00      JR      C,$4726         
4726: 7C         LD      A,H             
4727: 38 9E      JR      C,$46C7         
4729: 7C         LD      A,H             
472A: 9F         SBC     A               
472B: 66         LD      H,(HL)          
472C: F7         RST     0X30            
472D: 03         INC     BC              
472E: 07         RLCA                    
472F: 03         INC     BC              
4730: 02         LD      (BC),A          
4731: 01 01 00   LD      BC,$0001        
4734: 00         NOP                     
4735: 00         NOP                     
4736: 00         NOP                     
4737: 00         NOP                     
4738: 00         NOP                     
4739: 00         NOP                     
473A: 00         NOP                     
473B: 00         NOP                     
473C: 00         NOP                     
473D: 00         NOP                     
473E: 00         NOP                     
473F: 00         NOP                     
4740: 38 00      JR      C,$4742         
4742: 7C         LD      A,H             
4743: 38 BE      JR      C,$4703         
4745: 7C         LD      A,H             
4746: 9E         SBC     (HL)            
4747: 7C         LD      A,H             
4748: 9E         SBC     (HL)            
4749: 64         LD      H,H             
474A: 6F         LD      L,A             
474B: 06 07      LD      B,$07           
474D: 03         INC     BC              
474E: 07         RLCA                    
474F: 03         INC     BC              
4750: 02         LD      (BC),A          
4751: 01 01 00   LD      BC,$0001        
4754: 00         NOP                     
4755: 00         NOP                     
4756: 00         NOP                     
4757: 00         NOP                     
4758: 00         NOP                     
4759: 00         NOP                     
475A: 00         NOP                     
475B: 00         NOP                     
475C: 00         NOP                     
475D: 00         NOP                     
475E: 00         NOP                     
475F: 00         NOP                     
4760: E0 00      LDFF00  ($00),A         
4762: 90         SUB     B               
4763: 60         LD      H,B             
4764: 90         SUB     B               
4765: 60         LD      H,B             
4766: F8 70      LDHL    SP,$70          
4768: 78         LD      A,B             
4769: 30 3F      JR      NC,$47AA        
476B: 18 1F      JR      $478C           
476D: 0F         RRCA                    
476E: 0F         RRCA                    
476F: 07         RLCA                    
4770: 06 01      LD      B,$01           
4772: 01 00 00   LD      BC,$0000        
4775: 00         NOP                     
4776: 00         NOP                     
4777: 00         NOP                     
4778: 00         NOP                     
4779: 00         NOP                     
477A: 00         NOP                     
477B: 00         NOP                     
477C: 00         NOP                     
477D: 00         NOP                     
477E: 00         NOP                     
477F: 00         NOP                     
4780: 00         NOP                     
4781: 00         NOP                     
4782: 00         NOP                     
4783: 00         NOP                     
4784: 00         NOP                     
4785: 00         NOP                     
4786: 60         LD      H,B             
4787: 00         NOP                     
4788: 90         SUB     B               
4789: 60         LD      H,B             
478A: 91         SUB     C               
478B: 60         LD      H,B             
478C: EF         RST     0X28            
478D: 71         LD      (HL),C          
478E: FF         RST     0X38            
478F: 3F         CCF                     
4790: 3E 19      LD      A,$19           
4792: 19         ADD     HL,DE           
4793: 00         NOP                     
4794: 00         NOP                     
4795: 00         NOP                     
4796: 00         NOP                     
4797: 00         NOP                     
4798: 00         NOP                     
4799: 00         NOP                     
479A: 00         NOP                     
479B: 00         NOP                     
479C: 00         NOP                     
479D: 00         NOP                     
479E: 00         NOP                     
479F: 00         NOP                     
47A0: 00         NOP                     
47A1: 00         NOP                     
47A2: 00         NOP                     
47A3: 00         NOP                     
47A4: 00         NOP                     
47A5: 00         NOP                     
47A6: 00         NOP                     
47A7: 00         NOP                     
47A8: 00         NOP                     
47A9: 00         NOP                     
47AA: 01 00 03   LD      BC,$0300        
47AD: 01 07 03   LD      BC,$0307        
47B0: 06 03      LD      B,$03           
47B2: 07         RLCA                    
47B3: 02         LD      (BC),A          
47B4: 0F         RRCA                    
47B5: 06 1F      LD      B,$1F           
47B7: 0E 7E      LD      C,$7E           
47B9: 1C         INC     E               
47BA: 9E         SBC     (HL)            
47BB: 7C         LD      A,H             
47BC: 8C         ADC     A,H             
47BD: 78         LD      A,B             
47BE: F8 00      LDHL    SP,$00          
47C0: 00         NOP                     
47C1: 00         NOP                     
47C2: 00         NOP                     
47C3: 00         NOP                     
47C4: 00         NOP                     
47C5: 00         NOP                     
47C6: 00         NOP                     
47C7: 00         NOP                     
47C8: 00         NOP                     
47C9: 00         NOP                     
47CA: 03         INC     BC              
47CB: 00         NOP                     
47CC: 0F         RRCA                    
47CD: 03         INC     BC              
47CE: 1F         RRA                     
47CF: 0F         RRCA                    
47D0: 3E 19      LD      A,$19           
47D2: 7D         LD      A,L             
47D3: 38 78      JR      C,$484D         
47D5: 30 F8      JR      NC,$47CF        
47D7: 70         LD      (HL),B          
47D8: 88         ADC     A,B             
47D9: 70         LD      (HL),B          
47DA: 88         ADC     A,B             
47DB: 70         LD      (HL),B          
47DC: 48         LD      C,B             
47DD: 30 38      JR      NC,$4817        
47DF: 00         NOP                     
47E0: 00         NOP                     
47E1: 00         NOP                     
47E2: 00         NOP                     
47E3: 00         NOP                     
47E4: 00         NOP                     
47E5: 00         NOP                     
47E6: 00         NOP                     
47E7: 00         NOP                     
47E8: 00         NOP                     
47E9: 00         NOP                     
47EA: FC         ???                     
47EB: 00         NOP                     
47EC: FE FC      CP      $FC             
47EE: 02         LD      (BC),A          
47EF: FC         ???                     
47F0: FE 00      CP      $00             
47F2: FC         ???                     
47F3: 00         NOP                     
47F4: 00         NOP                     
47F5: 00         NOP                     
47F6: C0         RET     NZ              
47F7: 00         NOP                     
47F8: 00         NOP                     
47F9: 00         NOP                     
47FA: 00         NOP                     
47FB: 00         NOP                     
47FC: 00         NOP                     
47FD: 00         NOP                     
47FE: 00         NOP                     
47FF: 00         NOP                     
4800: FF         RST     0X38            
4801: 7F         LD      A,A             
4802: FF         RST     0X38            
4803: 77         LD      (HL),A          
4804: FF         RST     0X38            
4805: 36 FF      LD      (HL),$FF        
4807: 06 FF      LD      B,$FF           
4809: 04         INC     B               
480A: FF         RST     0X38            
480B: 04         INC     B               
480C: BF         CP      A               
480D: 40         LD      B,B             
480E: BF         CP      A               
480F: 40         LD      B,B             
4810: FF         RST     0X38            
4811: 1F         RRA                     
4812: FF         RST     0X38            
4813: B7         OR      A               
4814: FF         RST     0X38            
4815: B3         OR      E               
4816: FF         RST     0X38            
4817: A2         AND     D               
4818: FF         RST     0X38            
4819: 22         LD      (HLI),A         
481A: FF         RST     0X38            
481B: 02         LD      (BC),A          
481C: FF         RST     0X38            
481D: 00         NOP                     
481E: FF         RST     0X38            
481F: 00         NOP                     
4820: 09         ADD     HL,BC           
4821: 07         RLCA                    
4822: 08 07 0C   LD      ($0C07),SP      
4825: 03         INC     BC              
4826: 04         INC     B               
4827: 03         INC     BC              
4828: 07         RLCA                    
4829: 00         NOP                     
482A: 03         INC     BC              
482B: 00         NOP                     
482C: 01 00 00   LD      BC,$0000        
482F: 00         NOP                     
4830: 00         NOP                     
4831: 00         NOP                     
4832: 00         NOP                     
4833: 00         NOP                     
4834: 00         NOP                     
4835: 00         NOP                     
4836: 00         NOP                     
4837: 00         NOP                     
4838: 00         NOP                     
4839: 00         NOP                     
483A: 00         NOP                     
483B: 00         NOP                     
483C: 00         NOP                     
483D: 0F         RRCA                    
483E: 00         NOP                     
483F: 7F         LD      A,A             
4840: 01 00 07   LD      BC,$0700        
4843: 00         NOP                     
4844: 0F         RRCA                    
4845: 00         NOP                     
4846: 1E 01      LD      E,$01           
4848: 1C         INC     E               
4849: 03         INC     BC              
484A: 1C         INC     E               
484B: 03         INC     BC              
484C: 19         ADD     HL,DE           
484D: 07         RLCA                    
484E: 09         ADD     HL,BC           
484F: E7         RST     0X20            
4850: E0 00      LDFF00  ($00),A         
4852: F8 00      LDHL    SP,$00          
4854: CE 30      ADC     $30             
4856: 03         INC     BC              
4857: FC         ???                     
4858: 38 FF      JR      C,$4859         
485A: FE FF      CP      $FF             
485C: FF         RST     0X38            
485D: C3 FF 80   JP      $80FF           
4860: 03         INC     BC              
4861: 03         INC     BC              
4862: 0F         RRCA                    
4863: 0F         RRCA                    
4864: 1F         RRA                     
4865: 1E 1F      LD      E,$1F           
4867: 18 9E      JR      $4807           
4869: 11 50 8F   LD      DE,$8F50        
486C: 21 DF 8F   LD      HL,$8FDF        
486F: FF         RST     0X38            
4870: C0         RET     NZ              
4871: C0         RET     NZ              
4872: F0 F0      LD      A,($F0)         
4874: F8 18      LDHL    SP,$18          
4876: FC         ???                     
4877: 04         INC     B               
4878: 1E E6      LD      E,$E6           
487A: 0E F0      LD      C,$F0           
487C: C7         RST     0X00            
487D: F8 F7      LDHL    SP,$F7          
487F: F8 00      LDHL    SP,$00          
4881: 0E 00      LD      C,$00           
4883: 3F         CCF                     
4884: 1E 7F      LD      E,$7F           
4886: 7F         LD      A,A             
4887: FF         RST     0X38            
4888: FF         RST     0X38            
4889: E1         POP     HL              
488A: FF         RST     0X38            
488B: 80         ADD     A,B             
488C: C3 3C 80   JP      $803C           
488F: 7F         LD      A,A             
4890: 00         NOP                     
4891: 00         NOP                     
4892: 01 00 07   LD      BC,$0700        
4895: 80         ADD     A,B             
4896: 0C         INC     C               
4897: C3 88 F7   JP      $F788           
489A: D9         RETI                    
489B: E7         RST     0X20            
489C: E7         RST     0X20            
489D: 7F         LD      A,A             
489E: EF         RST     0X28            
489F: 1C         INC     E               
48A0: 7C         LD      A,H             
48A1: 00         NOP                     
48A2: FF         RST     0X38            
48A3: 00         NOP                     
48A4: FF         RST     0X38            
48A5: 00         NOP                     
48A6: 03         INC     BC              
48A7: FC         ???                     
48A8: 01 FE F0   LD      BC,$F0FE        
48AB: FF         RST     0X38            
48AC: FC         ???                     
48AD: FF         RST     0X38            
48AE: FE 1F      CP      $1F             
48B0: 00         NOP                     
48B1: 00         NOP                     
48B2: 00         NOP                     
48B3: 00         NOP                     
48B4: 80         ADD     A,B             
48B5: 00         NOP                     
48B6: C0         RET     NZ              
48B7: 00         NOP                     
48B8: C0         RET     NZ              
48B9: 00         NOP                     
48BA: C7         RST     0X00            
48BB: 07         RLCA                    
48BC: DF         RST     0X18            
48BD: 1F         RRA                     
48BE: 7F         LD      A,A             
48BF: B8         CP      B               
48C0: 00         NOP                     
48C1: 00         NOP                     
48C2: 00         NOP                     
48C3: 00         NOP                     
48C4: 00         NOP                     
48C5: 00         NOP                     
48C6: 00         NOP                     
48C7: 00         NOP                     
48C8: 00         NOP                     
48C9: 00         NOP                     
48CA: 00         NOP                     
48CB: 00         NOP                     
48CC: C0         RET     NZ              
48CD: C0         RET     NZ              
48CE: E0 E0      LDFF00  ($E0),A         
48D0: F0 30      LD      A,($30)         
48D2: F0 30      LD      A,($30)         
48D4: E0 60      LDFF00  ($60),A         
48D6: E0 E0      LDFF00  ($E0),A         
48D8: E0 E0      LDFF00  ($E0),A         
48DA: C0         RET     NZ              
48DB: C0         RET     NZ              
48DC: 80         ADD     A,B             
48DD: 80         ADD     A,B             
48DE: 00         NOP                     
48DF: 00         NOP                     
48E0: FE 1F      CP      $1F             
48E2: FC         ???                     
48E3: FF         RST     0X38            
48E4: FC         ???                     
48E5: E7         RST     0X20            
48E6: 1C         INC     E               
48E7: E7         RST     0X20            
48E8: 7D         LD      A,L             
48E9: 8E         ADC     A,(HL)          
48EA: F9         LD      SP,HL           
48EB: 1E F3      LD      E,$F3           
48ED: 3C         INC     A               
48EE: E3         ???                     
48EF: FD         ???                     
48F0: FC         ???                     
48F1: 1F         RRA                     
48F2: 79         LD      A,C             
48F3: FE 83      CP      $83             
48F5: FC         ???                     
48F6: C7         RST     0X00            
48F7: B8         CP      B               
48F8: FF         RST     0X38            
48F9: 81         ADD     A,C             
48FA: FF         RST     0X38            
48FB: C3 FF FF   JP      $FFFF           
48FE: 9F         SBC     A               
48FF: FC         ???                     
4900: 1B         DEC     DE              
4901: E4         ???                     
4902: 19         ADD     HL,DE           
4903: E6 11      AND     $11             
4905: EE 00      XOR     $00             
4907: FF         RST     0X38            
4908: 00         NOP                     
4909: FF         RST     0X38            
490A: 00         NOP                     
490B: FF         RST     0X38            
490C: 61         LD      H,C             
490D: FF         RST     0X38            
490E: F9         LD      SP,HL           
490F: FF         RST     0X38            
4910: 77         LD      (HL),A          
4911: 88         ADC     A,B             
4912: 66         LD      H,(HL)          
4913: 99         SBC     C               
4914: 00         NOP                     
4915: FF         RST     0X38            
4916: 00         NOP                     
4917: FF         RST     0X38            
4918: 00         NOP                     
4919: FF         RST     0X38            
491A: 80         ADD     A,B             
491B: FF         RST     0X38            
491C: 8A         ADC     A,D             
491D: FF         RST     0X38            
491E: CF         RST     0X08            
491F: FF         RST     0X38            
4920: 00         NOP                     
4921: 01 00 03   LD      BC,$0300        
4924: 00         NOP                     
4925: 07         RLCA                    
4926: 01 07 01   LD      BC,$0107        
4929: 0F         RRCA                    
492A: 03         INC     BC              
492B: 0F         RRCA                    
492C: 01 0F 00   LD      BC,$000F        
492F: 07         RLCA                    
4930: 03         INC     BC              
4931: FF         RST     0X38            
4932: 7F         LD      A,A             
4933: FE FF      CP      $FF             
4935: E0 F8      LDFF00  ($F8),A         
4937: C7         RST     0X00            
4938: F1         POP     AF              
4939: 8F         ADC     A,A             
493A: E3         ???                     
493B: 9F         SBC     A               
493C: E7         RST     0X20            
493D: 9E         SBC     (HL)            
493E: E7         RST     0X20            
493F: DE C4      SBC     $C4             
4941: FF         RST     0X38            
4942: F0 7F      LD      A,($7F)         
4944: F0 3F      LD      A,($3F)         
4946: 23         INC     HL              
4947: DF         RST     0X18            
4948: C3 FF E7   JP      $E7FF           
494B: 3F         CCF                     
494C: E7         RST     0X20            
494D: 1E 87      LD      E,$87           
494F: 7E         LD      A,(HL)          
4950: 13         INC     DE              
4951: EC         ???                     
4952: 00         NOP                     
4953: FF         RST     0X38            
4954: C0         RET     NZ              
4955: FF         RST     0X38            
4956: F3         DI                      
4957: FF         RST     0X38            
4958: F9         LD      SP,HL           
4959: 9F         SBC     A               
495A: FD         ???                     
495B: 07         RLCA                    
495C: FE 03      CP      $03             
495E: C3 3D CF   JP      $CF3D           
4961: 7C         LD      A,H             
4962: DF         RST     0X18            
4963: 38 63      JR      C,$49C8         
4965: BC         CP      H               
4966: 00         NOP                     
4967: FF         RST     0X38            
4968: 80         ADD     A,B             
4969: FF         RST     0X38            
496A: 0E FF      LD      C,$FF           
496C: 1F         RRA                     
496D: FF         RST     0X38            
496E: 3F         CCF                     
496F: FF         RST     0X38            
4970: F3         DI                      
4971: 3C         INC     A               
4972: F9         LD      SP,HL           
4973: 1E FC      LD      E,$FC           
4975: 07         RLCA                    
4976: 1E E7      LD      E,$E7           
4978: 0C         INC     C               
4979: F3         DI                      
497A: 20 FF      JR      NZ,$497B        
497C: 31 FF 93   LD      SP,$93FF        
497F: FF         RST     0X38            
4980: 1C         INC     E               
4981: FF         RST     0X38            
4982: 7F         LD      A,A             
4983: FF         RST     0X38            
4984: FF         RST     0X38            
4985: E7         RST     0X20            
4986: FF         RST     0X38            
4987: 86         ADD     A,(HL)          
4988: CF         RST     0X08            
4989: 3C         INC     A               
498A: FE 79      CP      $79             
498C: FE FF      CP      $FF             
498E: FF         RST     0X38            
498F: FF         RST     0X38            
4990: FF         RST     0X38            
4991: F8 FE      LDHL    SP,$FE          
4993: FF         RST     0X38            
4994: FF         RST     0X38            
4995: 87         ADD     A,A             
4996: FF         RST     0X38            
4997: 03         INC     BC              
4998: 0F         RRCA                    
4999: F1         POP     AF              
499A: 07         RLCA                    
499B: F8 F3      LDHL    SP,$F3          
499D: FC         ???                     
499E: F9         LD      SP,HL           
499F: FE FE      CP      $FE             
49A1: 07         RLCA                    
49A2: 1F         RRA                     
49A3: E3         ???                     
49A4: 07         RLCA                    
49A5: F9         LD      SP,HL           
49A6: 03         INC     BC              
49A7: FD         ???                     
49A8: 83         ADD     A,E             
49A9: FD         ???                     
49AA: C3 FC C3   JP      $C3FC           
49AD: FF         RST     0X38            
49AE: CF         RST     0X08            
49AF: FF         RST     0X38            
49B0: 7F         LD      A,A             
49B1: E0 F0      LDFF00  ($F0),A         
49B3: CF         RST     0X08            
49B4: E0 1F      LDFF00  ($1F),A         
49B6: 9F         SBC     A               
49B7: 7F         LD      A,A             
49B8: 3F         CCF                     
49B9: FF         RST     0X38            
49BA: 7F         LD      A,A             
49BB: E3         ???                     
49BC: EF         RST     0X28            
49BD: DE FF      SBC     $FF             
49BF: F8 F0      LDHL    SP,$F0          
49C1: 30 F0      JR      NC,$49B3        
49C3: 10 78      STOP    $78             
49C5: 98         SBC     B               
49C6: 3B         DEC     SP              
49C7: C8         RET     Z               
49C8: FC         ???                     
49C9: EB         ???                     
49CA: FF         RST     0X38            
49CB: FF         RST     0X38            
49CC: FF         RST     0X38            
49CD: 1C         INC     E               
49CE: FF         RST     0X38            
49CF: 06 00      LD      B,$00           
49D1: 00         NOP                     
49D2: 00         NOP                     
49D3: 00         NOP                     
49D4: 00         NOP                     
49D5: 00         NOP                     
49D6: E0 00      LDFF00  ($00),A         
49D8: 38 C0      JR      C,$499A         
49DA: C8         RET     Z               
49DB: F0 E4      LD      A,($E4)         
49DD: F8 F2      LDHL    SP,$F2          
49DF: 3C         INC     A               
49E0: 00         NOP                     
49E1: 00         NOP                     
49E2: 3C         INC     A               
49E3: 00         NOP                     
49E4: 7E         LD      A,(HL)          
49E5: 00         NOP                     
49E6: 7E         LD      A,(HL)          
49E7: 00         NOP                     
49E8: 7E         LD      A,(HL)          
49E9: 00         NOP                     
49EA: 7E         LD      A,(HL)          
49EB: 00         NOP                     
49EC: 3C         INC     A               
49ED: 00         NOP                     
49EE: 00         NOP                     
49EF: 00         NOP                     
49F0: 00         NOP                     
49F1: 00         NOP                     
49F2: 00         NOP                     
49F3: 00         NOP                     
49F4: 00         NOP                     
49F5: 00         NOP                     
49F6: 00         NOP                     
49F7: 00         NOP                     
49F8: 00         NOP                     
49F9: 00         NOP                     
49FA: 00         NOP                     
49FB: 00         NOP                     
49FC: 00         NOP                     
49FD: 00         NOP                     
49FE: 00         NOP                     
49FF: 00         NOP                     
4A00: 00         NOP                     
4A01: 00         NOP                     
4A02: 00         NOP                     
4A03: 00         NOP                     
4A04: 00         NOP                     
4A05: 00         NOP                     
4A06: 00         NOP                     
4A07: 00         NOP                     
4A08: 00         NOP                     
4A09: 00         NOP                     
4A0A: 00         NOP                     
4A0B: 00         NOP                     
4A0C: 00         NOP                     
4A0D: 00         NOP                     
4A0E: 00         NOP                     
4A0F: 00         NOP                     
4A10: 00         NOP                     
4A11: 00         NOP                     
4A12: 03         INC     BC              
4A13: 03         INC     BC              
4A14: 0F         RRCA                    
4A15: 0E 1F      LD      C,$1F           
4A17: 1C         INC     E               
4A18: 3E 31      LD      A,$31           
4A1A: 3C         INC     A               
4A1B: 33         INC     SP              
4A1C: 3C         INC     A               
4A1D: 33         INC     SP              
4A1E: 1C         INC     E               
4A1F: 1B         DEC     DE              
4A20: 78         LD      A,B             
4A21: 01 E0 9F   LD      BC,$9FE0        
4A24: C3 3F 0E   JP      $0E3F           
4A27: FD         ???                     
4A28: 1E F9      LD      E,$F9           
4A2A: 3E F9      LD      A,$F9           
4A2C: 3E F9      LD      A,$F9           
4A2E: 1E F9      LD      E,$F9           
4A30: 80         ADD     A,B             
4A31: FF         RST     0X38            
4A32: 00         NOP                     
4A33: FF         RST     0X38            
4A34: 07         RLCA                    
4A35: FF         RST     0X38            
4A36: 1F         RRA                     
4A37: FC         ???                     
4A38: 3F         CCF                     
4A39: F8 3F      LDHL    SP,$3F          
4A3B: F0 3E      LD      A,($3E)         
4A3D: F1         POP     AF              
4A3E: 1C         INC     E               
4A3F: F3         DI                      
4A40: 97         SUB     A               
4A41: 7E         LD      A,(HL)          
4A42: 13         INC     DE              
4A43: FE CB      CP      $CB             
4A45: FE F7      CP      $F7             
4A47: 3E FF      LD      A,$FF           
4A49: 07         RLCA                    
4A4A: 03         INC     BC              
4A4B: FF         RST     0X38            
4A4C: 09         ADD     HL,BC           
4A4D: FF         RST     0X38            
4A4E: 7F         LD      A,A             
4A4F: FF         RST     0X38            
4A50: 81         ADD     A,C             
4A51: 7E         LD      A,(HL)          
4A52: 1E FF      LD      E,$FF           
4A54: 3F         CCF                     
4A55: FF         RST     0X38            
4A56: 7C         LD      A,H             
4A57: E3         ???                     
4A58: 70         LD      (HL),B          
4A59: CF         RST     0X08            
4A5A: 73         LD      (HL),E          
4A5B: CF         RST     0X08            
4A5C: F9         LD      SP,HL           
4A5D: C7         RST     0X00            
4A5E: 7F         LD      A,A             
4A5F: F0 3F      LD      A,($3F)         
4A61: F0 7F      LD      A,($7F)         
4A63: E0 78      LDFF00  ($78),A         
4A65: C7         RST     0X00            
4A66: F0 CF      LD      A,($CF)         
4A68: 60         LD      H,B             
4A69: 9F         SBC     A               
4A6A: E3         ???                     
4A6B: 9F         SBC     A               
4A6C: C7         RST     0X00            
4A6D: BF         CP      A               
4A6E: CF         RST     0X08            
4A6F: B8         CP      B               
4A70: D7         RST     0X10            
4A71: FF         RST     0X38            
4A72: C7         RST     0X00            
4A73: 7C         LD      A,H             
4A74: EF         RST     0X28            
4A75: 38 7F      JR      C,$4AF6         
4A77: 98         SBC     B               
4A78: 1C         INC     E               
4A79: F3         DI                      
4A7A: 89         ADC     A,C             
4A7B: F7         RST     0X30            
4A7C: CB F7      SET     1,E             
4A7E: FF         RST     0X38            
4A7F: 6F         LD      L,A             
4A80: FF         RST     0X38            
4A81: 07         RLCA                    
4A82: FF         RST     0X38            
4A83: 01 FF 00   LD      BC,$00FF        
4A86: 03         INC     BC              
4A87: FC         ???                     
4A88: 00         NOP                     
4A89: FF         RST     0X38            
4A8A: C0         RET     NZ              
4A8B: FF         RST     0X38            
4A8C: F0 FF      LD      A,($FF)         
4A8E: F9         LD      SP,HL           
4A8F: FE FD      CP      $FD             
4A91: 8E         ADC     A,(HL)          
4A92: DD         ???                     
4A93: E6 CD      AND     $CD             
4A95: F6 FF      OR      $FF             
4A97: 3F         CCF                     
4A98: FF         RST     0X38            
4A99: 87         ADD     A,A             
4A9A: 7F         LD      A,A             
4A9B: C3 37 E9   JP      $E937           
4A9E: A7         AND     A               
4A9F: 78         LD      A,B             
4AA0: FF         RST     0X38            
4AA1: 70         LD      (HL),B          
4AA2: FF         RST     0X38            
4AA3: 40         LD      B,B             
4AA4: E0 5F      LDFF00  ($5F),A         
4AA6: CE 7F      ADC     $7F             
4AA8: FF         RST     0X38            
4AA9: FF         RST     0X38            
4AAA: FF         RST     0X38            
4AAB: C3 EF F7   JP      $F7EF           
4AAE: EF         RST     0X28            
4AAF: F0 FC      LD      A,($FC)         
4AB1: 7B         LD      A,E             
4AB2: FC         ???                     
4AB3: 1F         RRA                     
4AB4: FF         RST     0X38            
4AB5: 0F         RRCA                    
4AB6: 1F         RRA                     
4AB7: E6 1E      AND     $1E             
4AB9: E3         ???                     
4ABA: 8F         ADC     A,A             
4ABB: F3         DI                      
4ABC: C7         RST     0X00            
4ABD: FA F7 78   LD      A,($78F7)       
4AC0: 3E C3      LD      A,$C3           
4AC2: 0F         RRCA                    
4AC3: F3         DI                      
4AC4: C7         RST     0X00            
4AC5: F9         LD      SP,HL           
4AC6: E3         ???                     
4AC7: 7D         LD      A,L             
4AC8: FF         RST     0X38            
4AC9: 7D         LD      A,L             
4ACA: FF         RST     0X38            
4ACB: C3 FF 01   JP      $01FF           
4ACE: 07         RLCA                    
4ACF: F8 FA      LDHL    SP,$FA          
4AD1: 1C         INC     E               
4AD2: 3E CC      LD      A,$CC           
4AD4: 3C         INC     A               
4AD5: CC DC E7   CALL    Z,$E7DC         
4AD8: 5E         LD      E,(HL)          
4AD9: EF         RST     0X28            
4ADA: FF         RST     0X38            
4ADB: FF         RST     0X38            
4ADC: FF         RST     0X38            
4ADD: C7         RST     0X00            
4ADE: FF         RST     0X38            
4ADF: E1         POP     HL              
4AE0: 00         NOP                     
4AE1: 00         NOP                     
4AE2: 00         NOP                     
4AE3: 00         NOP                     
4AE4: 00         NOP                     
4AE5: 00         NOP                     
4AE6: 00         NOP                     
4AE7: 80         ADD     A,B             
4AE8: 00         NOP                     
4AE9: F0 80      LD      A,($80)         
4AEB: F8 C0      LDHL    SP,$C0          
4AED: F8 E0      LDHL    SP,$E0          
4AEF: FC         ???                     
4AF0: E0 F0      LDFF00  ($F0),A         
4AF2: F0 F8      LD      A,($F8)         
4AF4: F0 F8      LD      A,($F8)         
4AF6: F8 FC      LDHL    SP,$FC          
4AF8: F8 FC      LDHL    SP,$FC          
4AFA: FC         ???                     
4AFB: FE FC      CP      $FC             
4AFD: FF         RST     0X38            
4AFE: 00         NOP                     
4AFF: FF         RST     0X38            
4B00: 00         NOP                     
4B01: 00         NOP                     
4B02: 00         NOP                     
4B03: 00         NOP                     
4B04: 03         INC     BC              
4B05: 03         INC     BC              
4B06: 07         RLCA                    
4B07: 06 0E      LD      B,$0E           
4B09: 09         ADD     HL,BC           
4B0A: 1C         INC     E               
4B0B: 13         INC     DE              
4B0C: 39         ADD     HL,SP           
4B0D: 37         SCF                     
4B0E: 73         LD      (HL),E          
4B0F: 6F         LD      L,A             
4B10: 0F         RRCA                    
4B11: 0F         RRCA                    
4B12: FC         ???                     
4B13: FF         RST     0X38            
4B14: DC 33 38   CALL    C,$3833         
4B17: E7         RST     0X20            
4B18: 71         LD      (HL),C          
4B19: EF         RST     0X28            
4B1A: F1         POP     AF              
4B1B: CF         RST     0X08            
4B1C: F1         POP     AF              
4B1D: 8F         ADC     A,A             
4B1E: F0 8F      LD      A,($8F)         
4B20: 9F         SBC     A               
4B21: FC         ???                     
4B22: 07         RLCA                    
4B23: FE 7F      CP      $7F             
4B25: FF         RST     0X38            
4B26: FF         RST     0X38            
4B27: E0 FC      LDFF00  ($FC),A         
4B29: C3 FC C3   JP      $C3FC           
4B2C: FD         ???                     
4B2D: E3         ???                     
4B2E: FE FD      CP      $FD             
4B30: 9C         SBC     H               
4B31: 73         LD      (HL),E          
4B32: CC 3B C4   CALL    Z,$C43B         
4B35: BB         CP      E               
4B36: F6 09      OR      $09             
4B38: DF         RST     0X18            
4B39: 3C         INC     A               
4B3A: 3F         CCF                     
4B3B: F8 EF      LDHL    SP,$EF          
4B3D: FF         RST     0X38            
4B3E: 0E FF      LD      C,$FF           
4B40: FF         RST     0X38            
4B41: FE FF      CP      $FF             
4B43: E4         ???                     
4B44: F7         RST     0X30            
4B45: CC 67 DF   CALL    Z,$DF67         
4B48: 67         LD      H,A             
4B49: 9F         SBC     A               
4B4A: E3         ???                     
4B4B: 1F         RRA                     
4B4C: F0 0F      LD      A,($0F)         
4B4E: F0 0F      LD      A,($0F)         
4B50: 3C         INC     A               
4B51: FF         RST     0X38            
4B52: 01 FF FF   LD      BC,$FFFF        
4B55: 03         INC     BC              
4B56: FE 07      CP      $07             
4B58: FC         ???                     
4B59: FF         RST     0X38            
4B5A: F1         POP     AF              
4B5B: FF         RST     0X38            
4B5C: 02         LD      (BC),A          
4B5D: FD         ???                     
4B5E: 1F         RRA                     
4B5F: E1         POP     HL              
4B60: FC         ???                     
4B61: E3         ???                     
4B62: F8 C7      LDHL    SP,$C7          
4B64: F1         POP     AF              
4B65: CF         RST     0X08            
4B66: F1         POP     AF              
4B67: CF         RST     0X08            
4B68: F9         LD      SP,HL           
4B69: 87         ADD     A,A             
4B6A: 78         LD      A,B             
4B6B: 87         ADD     A,A             
4B6C: 7E         LD      A,(HL)          
4B6D: E1         POP     HL              
4B6E: 7F         LD      A,A             
4B6F: F0 7F      LD      A,($7F)         
4B71: CB FF      SET     1,E             
4B73: 98         SBC     B               
4B74: F7         RST     0X30            
4B75: 8C         ADC     A,H             
4B76: F3         DI                      
4B77: CF         RST     0X08            
4B78: FB         EI                      
4B79: FF         RST     0X38            
4B7A: F4         ???                     
4B7B: FB         EI                      
4B7C: 0E F1      LD      C,$F1           
4B7E: 7F         LD      A,A             
4B7F: 88         ADC     A,B             
4B80: FD         ???                     
4B81: 0E F1      LD      C,$F1           
4B83: 0E E1      LD      C,$E1           
4B85: 3E E3      LD      A,$E3           
4B87: FC         ???                     
4B88: C7         RST     0X00            
4B89: F9         LD      SP,HL           
4B8A: 07         RLCA                    
4B8B: F9         LD      SP,HL           
4B8C: 1F         RRA                     
4B8D: E3         ???                     
4B8E: FF         RST     0X38            
4B8F: 07         RLCA                    
4B90: B3         OR      E               
4B91: FC         ???                     
4B92: F3         DI                      
4B93: FC         ???                     
4B94: E7         RST     0X20            
4B95: F8 87      LDHL    SP,$87          
4B97: FB         EI                      
4B98: 8F         ADC     A,A             
4B99: F3         DI                      
4B9A: 7F         LD      A,A             
4B9B: FF         RST     0X38            
4B9C: 1E FF      LD      E,$FF           
4B9E: 3C         INC     A               
4B9F: CF         RST     0X08            
4BA0: FB         EI                      
4BA1: FC         ???                     
4BA2: FC         ???                     
4BA3: FF         RST     0X38            
4BA4: F1         POP     AF              
4BA5: FE DF      CP      $DF             
4BA7: E0 DF      LDFF00  ($DF),A         
4BA9: FC         ???                     
4BAA: 6F         LD      L,A             
4BAB: 9F         SBC     A               
4BAC: E0 5F      LDFF00  ($5F),A         
4BAE: F8 47      LDHL    SP,$47          
4BB0: FD         ???                     
4BB1: 3B         DEC     SP              
4BB2: FB         EI                      
4BB3: 1F         RRA                     
4BB4: F8 1F      LDHL    SP,$1F          
4BB6: F8 3F      LDHL    SP,$3F          
4BB8: F3         DI                      
4BB9: FF         RST     0X38            
4BBA: C7         RST     0X00            
4BBB: FB         EI                      
4BBC: 07         RLCA                    
4BBD: F9         LD      SP,HL           
4BBE: 0F         RRCA                    
4BBF: F1         POP     AF              
4BC0: E3         ???                     
4BC1: FC         ???                     
4BC2: F3         DI                      
4BC3: FC         ???                     
4BC4: E7         RST     0X20            
4BC5: F8 DF      LDHL    SP,$DF          
4BC7: E1         POP     HL              
4BC8: 7F         LD      A,A             
4BC9: 8F         ADC     A,A             
4BCA: FF         RST     0X38            
4BCB: 7C         LD      A,H             
4BCC: 8F         ADC     A,A             
4BCD: F0 FF      LD      A,($FF)         
4BCF: 81         ADD     A,C             
4BD0: E3         ???                     
4BD1: FC         ???                     
4BD2: E1         POP     HL              
4BD3: FE FD      CP      $FD             
4BD5: DE FF      SBC     $FF             
4BD7: C7         RST     0X00            
4BD8: 8F         ADC     A,A             
4BD9: F3         DI                      
4BDA: C7         RST     0X00            
4BDB: F8 C7      LDHL    SP,$C7          
4BDD: F8 C7      LDHL    SP,$C7          
4BDF: F8 F0      LDHL    SP,$F0          
4BE1: 7C         LD      A,H             
4BE2: F0 3C      LD      A,($3C)         
4BE4: FF         RST     0X38            
4BE5: FC         ???                     
4BE6: 3E C3      LD      A,$C3           
4BE8: 83         ADD     A,E             
4BE9: FD         ???                     
4BEA: F9         LD      SP,HL           
4BEB: FE ED      CP      $ED             
4BED: FE ED      CP      $ED             
4BEF: FE 00      CP      $00             
4BF1: 00         NOP                     
4BF2: 00         NOP                     
4BF3: 00         NOP                     
4BF4: C0         RET     NZ              
4BF5: 00         NOP                     
4BF6: 70         LD      (HL),B          
4BF7: 80         ADD     A,B             
4BF8: BC         CP      H               
4BF9: C0         RET     NZ              
4BFA: DE E0      SBC     $E0             
4BFC: C6 78      ADD     $78             
4BFE: E7         RST     0X20            
4BFF: 78         LD      A,B             
4C00: 73         LD      (HL),E          
4C01: 4F         LD      C,A             
4C02: F0 CF      LD      A,($CF)         
4C04: F0 CF      LD      A,($CF)         
4C06: FB         EI                      
4C07: E4         ???                     
4C08: FF         RST     0X38            
4C09: E0 FF      LDFF00  ($FF),A         
4C0B: F3         DI                      
4C0C: 7F         LD      A,A             
4C0D: 7F         LD      A,A             
4C0E: 3E 3E      LD      A,$3E           
4C10: FC         ???                     
4C11: C3 FE F9   JP      $F9FE           
4C14: 07         RLCA                    
4C15: FF         RST     0X38            
4C16: FF         RST     0X38            
4C17: 07         RLCA                    
4C18: FF         RST     0X38            
4C19: 3F         CCF                     
4C1A: F1         POP     AF              
4C1B: F7         RST     0X30            
4C1C: C9         RET                     
4C1D: C7         RST     0X00            
4C1E: 09         ADD     HL,BC           
4C1F: 07         RLCA                    
4C20: 7F         LD      A,A             
4C21: FC         ???                     
4C22: 0F         RRCA                    
4C23: FC         ???                     
4C24: CF         RST     0X08            
4C25: 3F         CCF                     
4C26: C7         RST     0X00            
4C27: 3F         CCF                     
4C28: C0         RET     NZ              
4C29: 3F         CCF                     
4C2A: E0 1F      LDFF00  ($1F),A         
4C2C: F0 0F      LD      A,($0F)         
4C2E: FF         RST     0X38            
4C2F: 00         NOP                     
4C30: 00         NOP                     
4C31: FF         RST     0X38            
4C32: E3         ???                     
4C33: 1C         INC     E               
4C34: FF         RST     0X38            
4C35: C0         RET     NZ              
4C36: DF         RST     0X18            
4C37: E1         POP     HL              
4C38: 1E FD      LD      E,$FD           
4C3A: 3F         CCF                     
4C3B: CC FF 1C   CALL    Z,$1CFF         
4C3E: FF         RST     0X38            
4C3F: 3E FC      LD      A,$FC           
4C41: 03         INC     BC              
4C42: FF         RST     0X38            
4C43: 40         LD      B,B             
4C44: FF         RST     0X38            
4C45: 70         LD      (HL),B          
4C46: FF         RST     0X38            
4C47: FF         RST     0X38            
4C48: FF         RST     0X38            
4C49: FF         RST     0X38            
4C4A: 3F         CCF                     
4C4B: FF         RST     0X38            
4C4C: 00         NOP                     
4C4D: FF         RST     0X38            
4C4E: 80         ADD     A,B             
4C4F: 7F         LD      A,A             
4C50: 7F         LD      A,A             
4C51: 87         ADD     A,A             
4C52: FE 1F      CP      $1F             
4C54: FE 3F      CP      $3F             
4C56: FC         ???                     
4C57: FF         RST     0X38            
4C58: F9         LD      SP,HL           
4C59: FE E3      CP      $E3             
4C5B: FC         ???                     
4C5C: 03         INC     BC              
4C5D: FC         ???                     
4C5E: 1F         RRA                     
4C5F: E1         POP     HL              
4C60: 3F         CCF                     
4C61: FC         ???                     
4C62: 1F         RRA                     
4C63: FF         RST     0X38            
4C64: 8F         ADC     A,A             
4C65: 7F         LD      A,A             
4C66: 80         ADD     A,B             
4C67: 7F         LD      A,A             
4C68: E0 1F      LDFF00  ($1F),A         
4C6A: FF         RST     0X38            
4C6B: 80         ADD     A,B             
4C6C: FF         RST     0X38            
4C6D: C0         RET     NZ              
4C6E: BF         CP      A               
4C6F: FF         RST     0X38            
4C70: FF         RST     0X38            
4C71: 3C         INC     A               
4C72: EB         ???                     
4C73: F7         RST     0X30            
4C74: 89         ADC     A,C             
4C75: F7         RST     0X30            
4C76: 38 C7      JR      C,$4C3F         
4C78: FC         ???                     
4C79: 13         INC     DE              
4C7A: FF         RST     0X38            
4C7B: 30 FF      JR      NC,$4C7C        
4C7D: F8 BF      LDHL    SP,$BF          
4C7F: FF         RST     0X38            
4C80: FF         RST     0X38            
4C81: FF         RST     0X38            
4C82: FF         RST     0X38            
4C83: FF         RST     0X38            
4C84: FF         RST     0X38            
4C85: FF         RST     0X38            
4C86: FF         RST     0X38            
4C87: FF         RST     0X38            
4C88: F8 F8      LDHL    SP,$F8          
4C8A: FA FA F8   LD      A,($F8FA)       
4C8D: F8 FF      LDHL    SP,$FF          
4C8F: FF         RST     0X38            
4C90: FF         RST     0X38            
4C91: FF         RST     0X38            
4C92: FF         RST     0X38            
4C93: FF         RST     0X38            
4C94: FF         RST     0X38            
4C95: FF         RST     0X38            
4C96: FF         RST     0X38            
4C97: FF         RST     0X38            
4C98: FF         RST     0X38            
4C99: FF         RST     0X38            
4C9A: FA FA FA   LD      A,($FAFA)       
4C9D: FA FF FF   LD      A,($FFFF)       
4CA0: FE 71      CP      $71             
4CA2: FF         RST     0X38            
4CA3: 78         LD      A,B             
4CA4: EF         RST     0X28            
4CA5: 7E         LD      A,(HL)          
4CA6: E7         RST     0X20            
4CA7: FF         RST     0X38            
4CA8: F1         POP     AF              
4CA9: EF         RST     0X28            
4CAA: B8         CP      B               
4CAB: E7         RST     0X20            
4CAC: FE 71      CP      $71             
4CAE: DF         RST     0X18            
4CAF: F8 3F      LDHL    SP,$3F          
4CB1: C3 FF 07   JP      $07FF           
4CB4: FF         RST     0X38            
4CB5: 3F         CCF                     
4CB6: FF         RST     0X38            
4CB7: FF         RST     0X38            
4CB8: FE FF      CP      $FF             
4CBA: 38 FF      JR      C,$4CBB         
4CBC: 00         NOP                     
4CBD: FF         RST     0X38            
4CBE: 01 FE FF   LD      BC,$FFFE        
4CC1: 8F         ADC     A,A             
4CC2: FC         ???                     
4CC3: FF         RST     0X38            
4CC4: 00         NOP                     
4CC5: FF         RST     0X38            
4CC6: 7F         LD      A,A             
4CC7: 80         ADD     A,B             
4CC8: 5F         LD      E,A             
4CC9: BF         CP      A               
4CCA: FF         RST     0X38            
4CCB: 07         RLCA                    
4CCC: FF         RST     0X38            
4CCD: 70         LD      (HL),B          
4CCE: DF         RST     0X18            
4CCF: 7F         LD      A,A             
4CD0: 87         ADD     A,A             
4CD1: F8 0F      LDHL    SP,$0F          
4CD3: F1         POP     AF              
4CD4: 3F         CCF                     
4CD5: C1         POP     BC              
4CD6: FF         RST     0X38            
4CD7: 03         INC     BC              
4CD8: FF         RST     0X38            
4CD9: 0F         RRCA                    
4CDA: FF         RST     0X38            
4CDB: FF         RST     0X38            
4CDC: FC         ???                     
4CDD: 7F         LD      A,A             
4CDE: F8 FF      LDHL    SP,$FF          
4CE0: F3         DI                      
4CE1: FC         ???                     
4CE2: FF         RST     0X38            
4CE3: E0 FF      LDFF00  ($FF),A         
4CE5: FF         RST     0X38            
4CE6: E7         RST     0X20            
4CE7: FF         RST     0X38            
4CE8: F8 C7      LDHL    SP,$C7          
4CEA: BF         CP      A               
4CEB: C0         RET     NZ              
4CEC: 77         LD      (HL),A          
4CED: 90         SUB     B               
4CEE: 70         LD      (HL),B          
4CEF: 90         SUB     B               
4CF0: E3         ???                     
4CF1: 7C         LD      A,H             
4CF2: E3         ???                     
4CF3: FC         ???                     
4CF4: E3         ???                     
4CF5: FC         ???                     
4CF6: C3 FC 07   JP      $07FC           
4CF9: F8 3E      LDHL    SP,$3E          
4CFB: C0         RET     NZ              
4CFC: FC         ???                     
4CFD: 00         NOP                     
4CFE: E0 00      LDFF00  ($00),A         
4D00: 00         NOP                     
4D01: 00         NOP                     
4D02: 18 00      JR      $4D04           
4D04: 1C         INC     E               
4D05: 00         NOP                     
4D06: 1C         INC     E               
4D07: 00         NOP                     
4D08: 14         INC     D               
4D09: 1C         INC     E               
4D0A: 14         INC     D               
4D0B: 1C         INC     E               
4D0C: 18 18      JR      $4D26           
4D0E: A4         AND     H               
4D0F: BE         CP      (HL)            
4D10: 43         LD      B,E             
4D11: FF         RST     0X38            
4D12: A4         AND     H               
4D13: BE         CP      (HL)            
4D14: 18 18      JR      $4D2E           
4D16: 14         INC     D               
4D17: 1C         INC     E               
4D18: 14         INC     D               
4D19: 1C         INC     E               
4D1A: 1C         INC     E               
4D1B: 00         NOP                     
4D1C: 1C         INC     E               
4D1D: 00         NOP                     
4D1E: 18 00      JR      $4D20           
4D20: 00         NOP                     
4D21: 00         NOP                     
4D22: 00         NOP                     
4D23: 00         NOP                     
4D24: 18 00      JR      $4D26           
4D26: 1C         INC     E               
4D27: 00         NOP                     
4D28: 14         INC     D               
4D29: 1C         INC     E               
4D2A: 14         INC     D               
4D2B: 1C         INC     E               
4D2C: 14         INC     D               
4D2D: 1C         INC     E               
4D2E: A4         AND     H               
4D2F: BE         CP      (HL)            
4D30: 43         LD      B,E             
4D31: FF         RST     0X38            
4D32: A4         AND     H               
4D33: BE         CP      (HL)            
4D34: 14         INC     D               
4D35: 1C         INC     E               
4D36: 14         INC     D               
4D37: 1C         INC     E               
4D38: 14         INC     D               
4D39: 1C         INC     E               
4D3A: 1C         INC     E               
4D3B: 00         NOP                     
4D3C: 18 00      JR      $4D3E           
4D3E: 00         NOP                     
4D3F: 00         NOP                     
4D40: 00         NOP                     
4D41: 00         NOP                     
4D42: 00         NOP                     
4D43: 00         NOP                     
4D44: 00         NOP                     
4D45: 00         NOP                     
4D46: 18 00      JR      $4D48           
4D48: 1C         INC     E               
4D49: 00         NOP                     
4D4A: 14         INC     D               
4D4B: 1C         INC     E               
4D4C: 14         INC     D               
4D4D: 1C         INC     E               
4D4E: A4         AND     H               
4D4F: BE         CP      (HL)            
4D50: 43         LD      B,E             
4D51: FF         RST     0X38            
4D52: A4         AND     H               
4D53: BE         CP      (HL)            
4D54: 14         INC     D               
4D55: 1C         INC     E               
4D56: 14         INC     D               
4D57: 1C         INC     E               
4D58: 1C         INC     E               
4D59: 00         NOP                     
4D5A: 18 00      JR      $4D5C           
4D5C: 00         NOP                     
4D5D: 00         NOP                     
4D5E: 00         NOP                     
4D5F: 00         NOP                     
4D60: 00         NOP                     
4D61: 00         NOP                     
4D62: 00         NOP                     
4D63: 00         NOP                     
4D64: 00         NOP                     
4D65: 00         NOP                     
4D66: 00         NOP                     
4D67: 00         NOP                     
4D68: 1C         INC     E               
4D69: 00         NOP                     
4D6A: 14         INC     D               
4D6B: 1C         INC     E               
4D6C: 14         INC     D               
4D6D: 1C         INC     E               
4D6E: A4         AND     H               
4D6F: BE         CP      (HL)            
4D70: 43         LD      B,E             
4D71: FF         RST     0X38            
4D72: A4         AND     H               
4D73: BE         CP      (HL)            
4D74: 14         INC     D               
4D75: 1C         INC     E               
4D76: 14         INC     D               
4D77: 1C         INC     E               
4D78: 1C         INC     E               
4D79: 00         NOP                     
4D7A: 00         NOP                     
4D7B: 00         NOP                     
4D7C: 00         NOP                     
4D7D: 00         NOP                     
4D7E: 00         NOP                     
4D7F: 00         NOP                     
4D80: 00         NOP                     
4D81: 00         NOP                     
4D82: 00         NOP                     
4D83: 00         NOP                     
4D84: 00         NOP                     
4D85: 00         NOP                     
4D86: 00         NOP                     
4D87: 00         NOP                     
4D88: 00         NOP                     
4D89: 00         NOP                     
4D8A: 18 00      JR      $4D8C           
4D8C: 1C         INC     E               
4D8D: 04         INC     B               
4D8E: A4         AND     H               
4D8F: BE         CP      (HL)            
4D90: 43         LD      B,E             
4D91: FF         RST     0X38            
4D92: A4         AND     H               
4D93: BE         CP      (HL)            
4D94: 1C         INC     E               
4D95: 04         INC     B               
4D96: 18 00      JR      $4D98           
4D98: 00         NOP                     
4D99: 00         NOP                     
4D9A: 00         NOP                     
4D9B: 00         NOP                     
4D9C: 00         NOP                     
4D9D: 00         NOP                     
4D9E: 00         NOP                     
4D9F: 00         NOP                     
4DA0: 00         NOP                     
4DA1: 00         NOP                     
4DA2: 00         NOP                     
4DA3: 00         NOP                     
4DA4: 00         NOP                     
4DA5: 00         NOP                     
4DA6: 00         NOP                     
4DA7: 00         NOP                     
4DA8: 1C         INC     E               
4DA9: 00         NOP                     
4DAA: 1C         INC     E               
4DAB: 04         INC     B               
4DAC: 14         INC     D               
4DAD: 1C         INC     E               
4DAE: A4         AND     H               
4DAF: BE         CP      (HL)            
4DB0: 43         LD      B,E             
4DB1: FF         RST     0X38            
4DB2: A4         AND     H               
4DB3: BE         CP      (HL)            
4DB4: 14         INC     D               
4DB5: 1C         INC     E               
4DB6: 1C         INC     E               
4DB7: 04         INC     B               
4DB8: 1C         INC     E               
4DB9: 00         NOP                     
4DBA: 00         NOP                     
4DBB: 00         NOP                     
4DBC: 00         NOP                     
4DBD: 00         NOP                     
4DBE: 00         NOP                     
4DBF: 00         NOP                     
4DC0: 00         NOP                     
4DC1: F0 00      LD      A,($00)         
4DC3: F8 00      LDHL    SP,$00          
4DC5: FC         ???                     
4DC6: 00         NOP                     
4DC7: FC         ???                     
4DC8: 00         NOP                     
4DC9: 7C         LD      A,H             
4DCA: 00         NOP                     
4DCB: 3C         INC     A               
4DCC: 00         NOP                     
4DCD: 00         NOP                     
4DCE: 00         NOP                     
4DCF: 00         NOP                     
4DD0: 00         NOP                     
4DD1: 00         NOP                     
4DD2: 00         NOP                     
4DD3: 00         NOP                     
4DD4: 00         NOP                     
4DD5: 00         NOP                     
4DD6: 00         NOP                     
4DD7: 00         NOP                     
4DD8: 00         NOP                     
4DD9: 00         NOP                     
4DDA: 00         NOP                     
4DDB: 00         NOP                     
4DDC: 00         NOP                     
4DDD: 00         NOP                     
4DDE: 00         NOP                     
4DDF: 00         NOP                     
4DE0: 00         NOP                     
4DE1: F0 00      LD      A,($00)         
4DE3: F8 00      LDHL    SP,$00          
4DE5: FC         ???                     
4DE6: 00         NOP                     
4DE7: FC         ???                     
4DE8: 0C         INC     C               
4DE9: 7F         LD      A,A             
4DEA: 0C         INC     C               
4DEB: 3F         CCF                     
4DEC: 00         NOP                     
4DED: 0F         RRCA                    
4DEE: 00         NOP                     
4DEF: 0F         RRCA                    
4DF0: 00         NOP                     
4DF1: 0F         RRCA                    
4DF2: 00         NOP                     
4DF3: 0F         RRCA                    
4DF4: 00         NOP                     
4DF5: 07         RLCA                    
4DF6: 00         NOP                     
4DF7: 03         INC     BC              
4DF8: 00         NOP                     
4DF9: 01 00 00   LD      BC,$0000        
4DFC: 00         NOP                     
4DFD: 00         NOP                     
4DFE: 00         NOP                     
4DFF: 00         NOP                     
4E00: 00         NOP                     
4E01: 00         NOP                     
4E02: 00         NOP                     
4E03: 00         NOP                     
4E04: 00         NOP                     
4E05: 00         NOP                     
4E06: 00         NOP                     
4E07: 00         NOP                     
4E08: 00         NOP                     
4E09: C0         RET     NZ              
4E0A: 00         NOP                     
4E0B: E0 00      LDFF00  ($00),A         
4E0D: F0 00      LD      A,($00)         
4E0F: F8 00      LDHL    SP,$00          
4E11: F8 00      LDHL    SP,$00          
4E13: F8 00      LDHL    SP,$00          
4E15: F8 00      LDHL    SP,$00          
4E17: F8 00      LDHL    SP,$00          
4E19: F8 00      LDHL    SP,$00          
4E1B: 00         NOP                     
4E1C: 00         NOP                     
4E1D: 00         NOP                     
4E1E: 00         NOP                     
4E1F: 00         NOP                     
4E20: 03         INC     BC              
4E21: 00         NOP                     
4E22: 06 01      LD      B,$01           
4E24: 04         INC     B               
4E25: 03         INC     BC              
4E26: 09         ADD     HL,BC           
4E27: 07         RLCA                    
4E28: 09         ADD     HL,BC           
4E29: 07         RLCA                    
4E2A: 13         INC     DE              
4E2B: 0F         RRCA                    
4E2C: 13         INC     DE              
4E2D: 0F         RRCA                    
4E2E: 27         DAA                     
4E2F: 1F         RRA                     
4E30: 27         DAA                     
4E31: 1F         RRA                     
4E32: 4F         LD      C,A             
4E33: 3F         CCF                     
4E34: 4F         LD      C,A             
4E35: 3F         CCF                     
4E36: 4F         LD      C,A             
4E37: 3F         CCF                     
4E38: 9F         SBC     A               
4E39: 7F         LD      A,A             
4E3A: 9F         SBC     A               
4E3B: 7F         LD      A,A             
4E3C: 9F         SBC     A               
4E3D: 7F         LD      A,A             
4E3E: 9F         SBC     A               
4E3F: 7F         LD      A,A             
4E40: 00         NOP                     
4E41: 00         NOP                     
4E42: 00         NOP                     
4E43: 00         NOP                     
4E44: 00         NOP                     
4E45: 00         NOP                     
4E46: 00         NOP                     
4E47: 00         NOP                     
4E48: 00         NOP                     
4E49: 00         NOP                     
4E4A: 00         NOP                     
4E4B: 00         NOP                     
4E4C: 00         NOP                     
4E4D: 00         NOP                     
4E4E: 00         NOP                     
4E4F: 00         NOP                     
4E50: 01 00 02   LD      BC,$0200        
4E53: 01 02 01   LD      BC,$0102        
4E56: 04         INC     B               
4E57: 03         INC     BC              
4E58: 04         INC     B               
4E59: 03         INC     BC              
4E5A: 05         DEC     B               
4E5B: 02         LD      (BC),A          
4E5C: 06 00      LD      B,$00           
4E5E: 06 00      LD      B,$00           
4E60: 00         NOP                     
4E61: 00         NOP                     
4E62: 01 00 02   LD      BC,$0200        
4E65: 01 0C 03   LD      BC,$030C        
4E68: 11 0F 20   LD      DE,$200F        
4E6B: 1F         RRA                     
4E6C: 48         LD      C,B             
4E6D: 3F         CCF                     
4E6E: 93         SUB     E               
4E6F: 7C         LD      A,H             
4E70: 23         INC     HL              
4E71: FC         ???                     
4E72: 45         LD      B,L             
4E73: F8 09      LDHL    SP,$09          
4E75: F0 71      LD      A,($71)         
4E77: 80         ADD     A,B             
4E78: 81         ADD     A,C             
4E79: 00         NOP                     
4E7A: 00         NOP                     
4E7B: 00         NOP                     
4E7C: 00         NOP                     
4E7D: 00         NOP                     
4E7E: 00         NOP                     
4E7F: 00         NOP                     
4E80: 9F         SBC     A               
4E81: 7F         LD      A,A             
4E82: 3F         CCF                     
4E83: FF         RST     0X38            
4E84: 7F         LD      A,A             
4E85: FF         RST     0X38            
4E86: FF         RST     0X38            
4E87: FF         RST     0X38            
4E88: FF         RST     0X38            
4E89: FF         RST     0X38            
4E8A: 7F         LD      A,A             
4E8B: FF         RST     0X38            
4E8C: 3F         CCF                     
4E8D: FF         RST     0X38            
4E8E: 3F         CCF                     
4E8F: FF         RST     0X38            
4E90: 3F         CCF                     
4E91: FF         RST     0X38            
4E92: 3F         CCF                     
4E93: FF         RST     0X38            
4E94: 3F         CCF                     
4E95: FF         RST     0X38            
4E96: 3F         CCF                     
4E97: FF         RST     0X38            
4E98: 3F         CCF                     
4E99: FF         RST     0X38            
4E9A: 9F         SBC     A               
4E9B: 7F         LD      A,A             
4E9C: 9F         SBC     A               
4E9D: 7F         LD      A,A             
4E9E: 9F         SBC     A               
4E9F: 7F         LD      A,A             
4EA0: 9F         SBC     A               
4EA1: 7F         LD      A,A             
4EA2: 9F         SBC     A               
4EA3: 7F         LD      A,A             
4EA4: 4F         LD      C,A             
4EA5: 3F         CCF                     
4EA6: 4F         LD      C,A             
4EA7: 3F         CCF                     
4EA8: 4F         LD      C,A             
4EA9: 3F         CCF                     
4EAA: 27         DAA                     
4EAB: 1F         RRA                     
4EAC: 27         DAA                     
4EAD: 1F         RRA                     
4EAE: 13         INC     DE              
4EAF: 0F         RRCA                    
4EB0: 13         INC     DE              
4EB1: 0F         RRCA                    
4EB2: 09         ADD     HL,BC           
4EB3: 07         RLCA                    
4EB4: 09         ADD     HL,BC           
4EB5: 07         RLCA                    
4EB6: 09         ADD     HL,BC           
4EB7: 07         RLCA                    
4EB8: 04         INC     B               
4EB9: 03         INC     BC              
4EBA: 04         INC     B               
4EBB: 03         INC     BC              
4EBC: 04         INC     B               
4EBD: 03         INC     BC              
4EBE: 04         INC     B               
4EBF: 03         INC     BC              
4EC0: 00         NOP                     
4EC1: 00         NOP                     
4EC2: 00         NOP                     
4EC3: 00         NOP                     
4EC4: 00         NOP                     
4EC5: 00         NOP                     
4EC6: 00         NOP                     
4EC7: 00         NOP                     
4EC8: 00         NOP                     
4EC9: 00         NOP                     
4ECA: 00         NOP                     
4ECB: 00         NOP                     
4ECC: 00         NOP                     
4ECD: 00         NOP                     
4ECE: 01 00 01   LD      BC,$0100        
4ED1: 00         NOP                     
4ED2: 02         LD      (BC),A          
4ED3: 01 02 01   LD      BC,$0102        
4ED6: 04         INC     B               
4ED7: 03         INC     BC              
4ED8: 04         INC     B               
4ED9: 03         INC     BC              
4EDA: 05         DEC     B               
4EDB: 02         LD      (BC),A          
4EDC: 06 00      LD      B,$00           
4EDE: 04         INC     B               
4EDF: 00         NOP                     
4EE0: 02         LD      (BC),A          
4EE1: 01 02 01   LD      BC,$0102        
4EE4: 02         LD      (BC),A          
4EE5: 01 06 01   LD      BC,$0106        
4EE8: 18 07      JR      $4EF1           
4EEA: 60         LD      H,B             
4EEB: 1F         RRA                     
4EEC: 84         ADD     A,H             
4EED: 7F         LD      A,A             
4EEE: 18 FF      JR      $4EEF           
4EF0: 21 FE 02   LD      HL,$02FE        
4EF3: FC         ???                     
4EF4: 1C         INC     E               
4EF5: E0 60      LDFF00  ($60),A         
4EF7: 80         ADD     A,B             
4EF8: 80         ADD     A,B             
4EF9: 00         NOP                     
4EFA: 00         NOP                     
4EFB: 00         NOP                     
4EFC: 00         NOP                     
4EFD: 00         NOP                     
4EFE: 00         NOP                     
4EFF: 00         NOP                     
4F00: 00         NOP                     
4F01: 00         NOP                     
4F02: 00         NOP                     
4F03: 00         NOP                     
4F04: 00         NOP                     
4F05: 00         NOP                     
4F06: 00         NOP                     
4F07: 10 00      STOP    $00             
4F09: 00         NOP                     
4F0A: 00         NOP                     
4F0B: 06 00      LD      B,$00           
4F0D: 07         RLCA                    
4F0E: 00         NOP                     
4F0F: 03         INC     BC              
4F10: 00         NOP                     
4F11: 00         NOP                     
4F12: 00         NOP                     
4F13: 00         NOP                     
4F14: 00         NOP                     
4F15: 00         NOP                     
4F16: 00         NOP                     
4F17: 00         NOP                     
4F18: 00         NOP                     
4F19: 00         NOP                     
4F1A: 00         NOP                     
4F1B: 00         NOP                     
4F1C: 00         NOP                     
4F1D: 00         NOP                     
4F1E: 00         NOP                     
4F1F: 00         NOP                     
4F20: FF         RST     0X38            
4F21: E0 FF      LDFF00  ($FF),A         
4F23: FF         RST     0X38            
4F24: 3E FF      LD      A,$FF           
4F26: 00         NOP                     
4F27: FF         RST     0X38            
4F28: 0F         RRCA                    
4F29: F0 FE      LD      A,($FE)         
4F2B: 00         NOP                     
4F2C: F0 00      LD      A,($00)         
4F2E: 00         NOP                     
4F2F: 00         NOP                     
4F30: FB         EI                      
4F31: FE C3      CP      $C3             
4F33: FF         RST     0X38            
4F34: 11 E7 40   LD      DE,$40E7        
4F37: A7         AND     A               
4F38: 80         ADD     A,B             
4F39: 03         INC     BC              
4F3A: 00         NOP                     
4F3B: 01 00 00   LD      BC,$0000        
4F3E: 00         NOP                     
4F3F: 00         NOP                     
4F40: FF         RST     0X38            
4F41: 00         NOP                     
4F42: FF         RST     0X38            
4F43: 80         ADD     A,B             
4F44: FF         RST     0X38            
4F45: F0 FF      LD      A,($FF)         
4F47: FF         RST     0X38            
4F48: 3F         CCF                     
4F49: FF         RST     0X38            
4F4A: 0E FF      LD      C,$FF           
4F4C: 00         NOP                     
4F4D: FF         RST     0X38            
4F4E: 00         NOP                     
4F4F: 3F         CCF                     
4F50: FF         RST     0X38            
4F51: 07         RLCA                    
4F52: FE 3F      CP      $3F             
4F54: F8 FF      LDHL    SP,$FF          
4F56: F0 FF      LD      A,($FF)         
4F58: 80         ADD     A,B             
4F59: FF         RST     0X38            
4F5A: 0C         INC     C               
4F5B: FF         RST     0X38            
4F5C: 3E FF      LD      A,$FF           
4F5E: 7F         LD      A,A             
4F5F: FF         RST     0X38            
4F60: 1E FF      LD      E,$FF           
4F62: 40         LD      B,B             
4F63: BF         CP      A               
4F64: 61         LD      H,C             
4F65: DE 7F      SBC     $7F             
4F67: C0         RET     NZ              
4F68: 3F         CCF                     
4F69: E3         ???                     
4F6A: 9D         SBC     L               
4F6B: FF         RST     0X38            
4F6C: E7         RST     0X20            
4F6D: FF         RST     0X38            
4F6E: EF         RST     0X28            
4F6F: FF         RST     0X38            
4F70: 0F         RRCA                    
4F71: FF         RST     0X38            
4F72: C6 3F      ADD     $3F             
4F74: A0         AND     B               
4F75: DF         RST     0X18            
4F76: B8         CP      B               
4F77: C7         RST     0X00            
4F78: 1F         RRA                     
4F79: E0 DF      LDFF00  ($DF),A         
4F7B: E0 FF      LDFF00  ($FF),A         
4F7D: FC         ???                     
4F7E: FF         RST     0X38            
4F7F: FF         RST     0X38            
4F80: C7         RST     0X00            
4F81: F9         LD      SP,HL           
4F82: 8F         ADC     A,A             
4F83: F3         DI                      
4F84: 1F         RRA                     
4F85: E3         ???                     
4F86: 3F         CCF                     
4F87: C7         RST     0X00            
4F88: FE 0F      CP      $0F             
4F8A: FC         ???                     
4F8B: 1F         RRA                     
4F8C: F9         LD      SP,HL           
4F8D: 7F         LD      A,A             
4F8E: FF         RST     0X38            
4F8F: FF         RST     0X38            
4F90: 9F         SBC     A               
4F91: E1         POP     HL              
4F92: 3F         CCF                     
4F93: FF         RST     0X38            
4F94: 1F         RRA                     
4F95: FF         RST     0X38            
4F96: 00         NOP                     
4F97: FF         RST     0X38            
4F98: 38 E7      JR      C,$4F81         
4F9A: 7F         LD      A,A             
4F9B: F0 FF      LD      A,($FF)         
4F9D: F8 FF      LDHL    SP,$FF          
4F9F: FE CF      CP      $CF             
4FA1: FC         ???                     
4FA2: 8F         ADC     A,A             
4FA3: F7         RST     0X30            
4FA4: 1F         RRA                     
4FA5: E7         RST     0X20            
4FA6: 39         ADD     HL,SP           
4FA7: CF         RST     0X08            
4FA8: 7C         LD      A,H             
4FA9: 9F         SBC     A               
4FAA: FE 1F      CP      $1F             
4FAC: FF         RST     0X38            
4FAD: 3F         CCF                     
4FAE: FF         RST     0X38            
4FAF: 7F         LD      A,A             
4FB0: E3         ???                     
4FB1: 1C         INC     E               
4FB2: FF         RST     0X38            
4FB3: 01 FF C3   LD      BC,$C3FF        
4FB6: FF         RST     0X38            
4FB7: FF         RST     0X38            
4FB8: 7E         LD      A,(HL)          
4FB9: FF         RST     0X38            
4FBA: 3C         INC     A               
4FBB: FF         RST     0X38            
4FBC: 00         NOP                     
4FBD: FF         RST     0X38            
4FBE: C3 FF E1   JP      $E1FF           
4FC1: DF         RST     0X18            
4FC2: F8 C7      LDHL    SP,$C7          
4FC4: BF         CP      A               
4FC5: F0 1F      LD      A,($1F)         
4FC7: D8         RET     C               
4FC8: 0F         RRCA                    
4FC9: CE 07      ADC     $07             
4FCB: 87         ADD     A,A             
4FCC: 03         INC     BC              
4FCD: 03         INC     BC              
4FCE: 00         NOP                     
4FCF: 00         NOP                     
4FD0: F0 FF      LD      A,($FF)         
4FD2: 01 FE 1F   LD      BC,$1FFE        
4FD5: E0 FF      LDFF00  ($FF),A         
4FD7: 00         NOP                     
4FD8: FF         RST     0X38            
4FD9: 01 FF FF   LD      BC,$FFFF        
4FDC: FF         RST     0X38            
4FDD: FF         RST     0X38            
4FDE: FC         ???                     
4FDF: FC         ???                     
4FE0: 00         NOP                     
4FE1: 00         NOP                     
4FE2: 00         NOP                     
4FE3: 00         NOP                     
4FE4: 00         NOP                     
4FE5: 00         NOP                     
4FE6: 00         NOP                     
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
4FF2: 18 00      JR      $4FF4           
4FF4: 3C         INC     A               
4FF5: 00         NOP                     
4FF6: 7E         LD      A,(HL)          
4FF7: 00         NOP                     
4FF8: FF         RST     0X38            
4FF9: 00         NOP                     
4FFA: 3C         INC     A               
4FFB: 00         NOP                     
4FFC: 3C         INC     A               
4FFD: 00         NOP                     
4FFE: 00         NOP                     
4FFF: 00         NOP                     
5000: FF         RST     0X38            
5001: 0F         RRCA                    
5002: FF         RST     0X38            
5003: 0F         RRCA                    
5004: 7F         LD      A,A             
5005: 0F         RRCA                    
5006: 7F         LD      A,A             
5007: 0F         RRCA                    
5008: 3F         CCF                     
5009: 30 1F      JR      NC,$502A        
500B: 10 0F      STOP    $0F             
500D: 00         NOP                     
500E: 03         INC     BC              
500F: 00         NOP                     
5010: FF         RST     0X38            
5011: 0F         RRCA                    
5012: FF         RST     0X38            
5013: 0F         RRCA                    
5014: FE 0E      CP      $0E             
5016: FE 0E      CP      $0E             
5018: FC         ???                     
5019: F0 F8      LD      A,($F8)         
501B: F0 F0      LD      A,($F0)         
501D: F0 C0      LD      A,($C0)         
501F: C0         RET     NZ              
5020: 03         INC     BC              
5021: 03         INC     BC              
5022: 0F         RRCA                    
5023: 0F         RRCA                    
5024: 1F         RRA                     
5025: 1F         RRA                     
5026: 3F         CCF                     
5027: 2F         CPL                     
5028: 7F         LD      A,A             
5029: 70         LD      (HL),B          
502A: 7F         LD      A,A             
502B: 70         LD      (HL),B          
502C: FF         RST     0X38            
502D: F0 FF      LD      A,($FF)         
502F: F0 03      LD      A,($03)         
5031: 00         NOP                     
5032: 0F         RRCA                    
5033: 00         NOP                     
5034: 1F         RRA                     
5035: 00         NOP                     
5036: 2F         CPL                     
5037: 10 70      STOP    $70             
5039: 0F         RRCA                    
503A: 70         LD      (HL),B          
503B: 0F         RRCA                    
503C: F0 0F      LD      A,($0F)         
503E: F0 0F      LD      A,($0F)         
5040: 00         NOP                     
5041: C0         RET     NZ              
5042: 00         NOP                     
5043: F0 08      LD      A,($08)         
5045: F0 0C      LD      A,($0C)         
5047: F0 F0      LD      A,($F0)         
5049: 0E F0      LD      C,$F0           
504B: 0E F0      LD      C,$F0           
504D: 0F         RRCA                    
504E: F0 0F      LD      A,($0F)         
5050: 00         NOP                     
5051: 00         NOP                     
5052: 00         NOP                     
5053: 00         NOP                     
5054: 00         NOP                     
5055: 00         NOP                     
5056: 00         NOP                     
5057: 00         NOP                     
5058: 00         NOP                     
5059: 00         NOP                     
505A: 00         NOP                     
505B: 00         NOP                     
505C: 02         LD      (BC),A          
505D: 01 07 18   LD      BC,$1807        
5060: 00         NOP                     
5061: 00         NOP                     
5062: 00         NOP                     
5063: 00         NOP                     
5064: 00         NOP                     
5065: 00         NOP                     
5066: 01 00 00   LD      BC,$0000        
5069: 07         RLCA                    
506A: 00         NOP                     
506B: 71         LD      (HL),C          
506C: C0         RET     NZ              
506D: 3C         INC     A               
506E: 60         LD      H,B             
506F: 9E         SBC     (HL)            
5070: 00         NOP                     
5071: 00         NOP                     
5072: 00         NOP                     
5073: 00         NOP                     
5074: 0F         RRCA                    
5075: 00         NOP                     
5076: E0 1F      LDFF00  ($1F),A         
5078: 80         ADD     A,B             
5079: 7F         LD      A,A             
507A: 7D         LD      A,L             
507B: 82         ADD     A,D             
507C: 3F         CCF                     
507D: C0         RET     NZ              
507E: 1F         RRA                     
507F: E0 00      LDFF00  ($00),A         
5081: 08 02 7D   LD      ($7D02),SP      
5084: 01 FE 81   LD      BC,$81FE        
5087: 7E         LD      A,(HL)          
5088: 80         ADD     A,B             
5089: 7F         LD      A,A             
508A: C0         RET     NZ              
508B: 3F         CCF                     
508C: 60         LD      H,B             
508D: 9F         SBC     A               
508E: 22         LD      (HLI),A         
508F: DD         ???                     
5090: 7E         LD      A,(HL)          
5091: 3F         CCF                     
5092: 3C         INC     A               
5093: FF         RST     0X38            
5094: 00         NOP                     
5095: FF         RST     0X38            
5096: 00         NOP                     
5097: FF         RST     0X38            
5098: F8 07      LDHL    SP,$07          
509A: 78         LD      A,B             
509B: 87         ADD     A,A             
509C: 3D         DEC     A               
509D: D2 BB 6E   JP      NC,$6EBB        
50A0: 00         NOP                     
50A1: FF         RST     0X38            
50A2: 00         NOP                     
50A3: FF         RST     0X38            
50A4: 00         NOP                     
50A5: FF         RST     0X38            
50A6: 00         NOP                     
50A7: FF         RST     0X38            
50A8: 00         NOP                     
50A9: FF         RST     0X38            
50AA: AA         XOR     D               
50AB: 55         LD      D,L             
50AC: D7         RST     0X10            
50AD: 68         LD      L,B             
50AE: EF         RST     0X28            
50AF: 92         SUB     D               
50B0: 00         NOP                     
50B1: E0 00      LDFF00  ($00),A         
50B3: FF         RST     0X38            
50B4: 00         NOP                     
50B5: FF         RST     0X38            
50B6: 00         NOP                     
50B7: FF         RST     0X38            
50B8: 00         NOP                     
50B9: FF         RST     0X38            
50BA: A9         XOR     C               
50BB: 56         LD      D,(HL)          
50BC: 55         LD      D,L             
50BD: BB         CP      E               
50BE: BE         CP      (HL)            
50BF: 69         LD      L,C             
50C0: 00         NOP                     
50C1: 00         NOP                     
50C2: 00         NOP                     
50C3: E0 7C      LDFF00  ($7C),A         
50C5: 83         ADD     A,E             
50C6: 3C         INC     A               
50C7: C3 08 F7   JP      $F708           
50CA: F8 07      LDHL    SP,$07          
50CC: F0 5F      LD      A,($5F)         
50CE: E0 BF      LDFF00  ($BF),A         
50D0: 00         NOP                     
50D1: 00         NOP                     
50D2: 00         NOP                     
50D3: 00         NOP                     
50D4: 00         NOP                     
50D5: 00         NOP                     
50D6: 00         NOP                     
50D7: E0 28      LDFF00  ($28),A         
50D9: D4 26 D9   CALL    NC,$D926        
50DC: 21 DE 58   LD      HL,$58DE        
50DF: A7         AND     A               
50E0: 00         NOP                     
50E1: 00         NOP                     
50E2: 00         NOP                     
50E3: 00         NOP                     
50E4: 00         NOP                     
50E5: 00         NOP                     
50E6: 00         NOP                     
50E7: 00         NOP                     
50E8: 00         NOP                     
50E9: 00         NOP                     
50EA: 00         NOP                     
50EB: 00         NOP                     
50EC: 80         ADD     A,B             
50ED: 40         LD      B,B             
50EE: E0 00      LDFF00  ($00),A         
50F0: 0F         RRCA                    
50F1: F0 0F      LD      A,($0F)         
50F3: F0 0E      LD      A,($0E)         
50F5: F0 0E      LD      A,($0E)         
50F7: F0 F0      LD      A,($F0)         
50F9: 0C         INC     C               
50FA: F0 08      LD      A,($08)         
50FC: F0 00      LD      A,($00)         
50FE: C0         RET     NZ              
50FF: 00         NOP                     
5100: CF         RST     0X08            
5101: 30 FF      JR      NC,$5102        
5103: 00         NOP                     
5104: FF         RST     0X38            
5105: 08 FF 0C   LD      ($0CFF),SP      
5108: FE F1      CP      $F1             
510A: FE F1      CP      $F1             
510C: FF         RST     0X38            
510D: F0 FF      LD      A,($FF)         
510F: F0 0F      LD      A,($0F)         
5111: F3         DI                      
5112: 0F         RRCA                    
5113: FF         RST     0X38            
5114: 1F         RRA                     
5115: EF         RST     0X28            
5116: 3F         CCF                     
5117: CF         RST     0X08            
5118: FF         RST     0X38            
5119: 70         LD      (HL),B          
511A: FF         RST     0X38            
511B: 70         LD      (HL),B          
511C: FF         RST     0X38            
511D: F0 FF      LD      A,($FF)         
511F: F0 03      LD      A,($03)         
5121: 00         NOP                     
5122: 0F         RRCA                    
5123: 00         NOP                     
5124: 1F         RRA                     
5125: 00         NOP                     
5126: 2F         CPL                     
5127: 10 7C      STOP    $7C             
5129: 13         INC     DE              
512A: 7E         LD      A,(HL)          
512B: 31 FF 70   LD      SP,$70FF        
512E: FF         RST     0X38            
512F: F0 00      LD      A,($00)         
5131: 00         NOP                     
5132: 00         NOP                     
5133: 00         NOP                     
5134: 00         NOP                     
5135: 00         NOP                     
5136: 00         NOP                     
5137: 00         NOP                     
5138: 00         NOP                     
5139: 00         NOP                     
513A: 01 00 07   LD      BC,$0700        
513D: 00         NOP                     
513E: 0F         RRCA                    
513F: 10 00      STOP    $00             
5141: 00         NOP                     
5142: 01 00 0F   LD      BC,$0F00        
5145: 00         NOP                     
5146: 3F         CCF                     
5147: 00         NOP                     
5148: FF         RST     0X38            
5149: 00         NOP                     
514A: FE 01      CP      $01             
514C: FC         ???                     
514D: 03         INC     BC              
514E: C1         POP     BC              
514F: 3F         CCF                     
5150: 30 4F      JR      NC,$51A1        
5152: 89         ADC     A,C             
5153: 76         HALT                    
5154: 88         ADC     A,B             
5155: 77         LD      (HL),A          
5156: 90         SUB     B               
5157: 6F         LD      L,A             
5158: 10 EF      STOP    $EF             
515A: 25         DEC     H               
515B: DA 6A 95   JP      C,$956A         
515E: D7         RST     0X10            
515F: 28 B0      JR      Z,$5111         
5161: 4F         LD      C,A             
5162: 70         LD      (HL),B          
5163: 8F         ADC     A,A             
5164: 8A         ADC     A,D             
5165: 75         LD      (HL),L          
5166: 7C         LD      A,H             
5167: 83         ADD     A,E             
5168: AA         XOR     D               
5169: 5D         LD      E,L             
516A: 7F         LD      A,A             
516B: 98         SBC     B               
516C: FF         RST     0X38            
516D: 48         LD      C,B             
516E: FF         RST     0X38            
516F: B8         CP      B               
5170: 1F         RRA                     
5171: 60         LD      H,B             
5172: 0F         RRCA                    
5173: 3E 1F      LD      A,$1F           
5175: AE         XOR     (HL)            
5176: 5F         LD      E,A             
5177: E6 5F      AND     $5F             
5179: E3         ???                     
517A: 6F         LD      L,A             
517B: F1         POP     AF              
517C: 77         LD      (HL),A          
517D: F8 7B      LDHL    SP,$7B          
517F: FC         ???                     
5180: 1D         DEC     E               
5181: F2         ???                     
5182: FF         RST     0X38            
5183: 08 FF 06   LD      ($06FF),SP      
5186: FF         RST     0X38            
5187: 3F         CCF                     
5188: FF         RST     0X38            
5189: FC         ???                     
518A: FF         RST     0X38            
518B: FC         ???                     
518C: FF         RST     0X38            
518D: FC         ???                     
518E: FF         RST     0X38            
518F: 3C         INC     A               
5190: 5F         LD      E,A             
5191: A7         AND     A               
5192: FF         RST     0X38            
5193: 00         NOP                     
5194: FF         RST     0X38            
5195: 00         NOP                     
5196: FF         RST     0X38            
5197: 00         NOP                     
5198: FF         RST     0X38            
5199: 80         ADD     A,B             
519A: FF         RST     0X38            
519B: 70         LD      (HL),B          
519C: FF         RST     0X38            
519D: 0F         RRCA                    
519E: FF         RST     0X38            
519F: 04         INC     B               
51A0: FF         RST     0X38            
51A1: CF         RST     0X08            
51A2: FF         RST     0X38            
51A3: FF         RST     0X38            
51A4: FF         RST     0X38            
51A5: 00         NOP                     
51A6: FF         RST     0X38            
51A7: 00         NOP                     
51A8: FF         RST     0X38            
51A9: 00         NOP                     
51AA: FF         RST     0X38            
51AB: 00         NOP                     
51AC: FF         RST     0X38            
51AD: FF         RST     0X38            
51AE: FF         RST     0X38            
51AF: 08 FF BF   LD      ($BFFF),SP      
51B2: FF         RST     0X38            
51B3: FC         ???                     
51B4: FF         RST     0X38            
51B5: 00         NOP                     
51B6: FF         RST     0X38            
51B7: 00         NOP                     
51B8: FF         RST     0X38            
51B9: 00         NOP                     
51BA: FF         RST     0X38            
51BB: 00         NOP                     
51BC: FF         RST     0X38            
51BD: FF         RST     0X38            
51BE: FF         RST     0X38            
51BF: 10 D5      STOP    $D5             
51C1: 2A         LD      A,(HLI)         
51C2: AA         XOR     D               
51C3: 55         LD      D,L             
51C4: FF         RST     0X38            
51C5: 01 FF 02   LD      BC,$02FF        
51C8: FF         RST     0X38            
51C9: 0D         DEC     C               
51CA: FF         RST     0X38            
51CB: 31 FF C0   LD      SP,$C0FF        
51CE: FF         RST     0X38            
51CF: 30 4F      JR      NC,$5220        
51D1: F0 8F      LD      A,($8F)         
51D3: F0 87      LD      A,($87)         
51D5: F8 F3      LDHL    SP,$F3          
51D7: 0C         INC     C               
51D8: FF         RST     0X38            
51D9: 81         ADD     A,C             
51DA: FF         RST     0X38            
51DB: F8 FF      LDHL    SP,$FF          
51DD: FF         RST     0X38            
51DE: FF         RST     0X38            
51DF: FE 20      CP      $20             
51E1: D0         RET     NC              
51E2: C0         RET     NZ              
51E3: 38 E0      JR      C,$51C5         
51E5: 1C         INC     E               
51E6: E0 12      LDFF00  ($12),A         
51E8: E0 19      LDFF00  ($19),A         
51EA: C0         RET     NZ              
51EB: FC         ???                     
51EC: 80         ADD     A,B             
51ED: F8 00      LDHL    SP,$00          
51EF: F0 00      LD      A,($00)         
51F1: 00         NOP                     
51F2: 00         NOP                     
51F3: 00         NOP                     
51F4: 00         NOP                     
51F5: 00         NOP                     
51F6: 00         NOP                     
51F7: 00         NOP                     
51F8: 00         NOP                     
51F9: 00         NOP                     
51FA: 00         NOP                     
51FB: 80         ADD     A,B             
51FC: 00         NOP                     
51FD: 40         LD      B,B             
51FE: 00         NOP                     
51FF: 20 0F      JR      NZ,$5210        
5201: F1         POP     AF              
5202: CF         RST     0X08            
5203: 37         SCF                     
5204: EF         RST     0X28            
5205: 1F         RRA                     
5206: EF         RST     0X28            
5207: 1F         RRA                     
5208: FF         RST     0X38            
5209: F0 FF      LD      A,($FF)         
520B: F0 FF      LD      A,($FF)         
520D: F0 FF      LD      A,($FF)         
520F: F0 8F      LD      A,($8F)         
5211: 70         LD      (HL),B          
5212: 8F         ADC     A,A             
5213: 70         LD      (HL),B          
5214: CE 30      ADC     $30             
5216: CE 30      ADC     $30             
5218: F0 CC      LD      A,($CC)         
521A: F0 C8      LD      A,($C8)         
521C: F0 80      LD      A,($80)         
521E: C0         RET     NZ              
521F: 00         NOP                     
5220: 00         NOP                     
5221: 00         NOP                     
5222: 00         NOP                     
5223: 00         NOP                     
5224: 00         NOP                     
5225: 01 01 02   LD      BC,$0201        
5228: 02         LD      (BC),A          
5229: 0D         DEC     C               
522A: 05         DEC     B               
522B: 1A         LD      A,(DE)          
522C: 3A         LD      A,(HLD)         
522D: 05         DEC     B               
522E: 07         RLCA                    
522F: 79         LD      A,C             
5230: 00         NOP                     
5231: 3F         CCF                     
5232: 60         LD      H,B             
5233: 9F         SBC     A               
5234: 1F         RRA                     
5235: E0 81      LDFF00  ($81),A         
5237: 7E         LD      A,(HL)          
5238: 4A         LD      C,D             
5239: B5         OR      L               
523A: 57         LD      D,A             
523B: AE         XOR     (HL)            
523C: AF         XOR     A               
523D: D9         RETI                    
523E: 7F         LD      A,A             
523F: 96         SUB     (HL)            
5240: 0E F3      LD      C,$F3           
5242: 7D         LD      A,L             
5243: 92         SUB     D               
5244: AF         XOR     A               
5245: D0         RET     NC              
5246: 5F         LD      E,A             
5247: A0         AND     B               
5248: FF         RST     0X38            
5249: 06 FF      LD      B,$FF           
524B: 09         ADD     HL,BC           
524C: FF         RST     0X38            
524D: 16 FF      LD      D,$FF           
524F: 96         SUB     (HL)            
5250: BF         CP      A               
5251: 40         LD      B,B             
5252: FF         RST     0X38            
5253: 0C         INC     C               
5254: FF         RST     0X38            
5255: 12         LD      (DE),A          
5256: FF         RST     0X38            
5257: 2D         DEC     L               
5258: FF         RST     0X38            
5259: 2D         DEC     L               
525A: FF         RST     0X38            
525B: 13         INC     DE              
525C: FF         RST     0X38            
525D: 8E         ADC     A,(HL)          
525E: FF         RST     0X38            
525F: F8 FE      LDHL    SP,$FE          
5261: B1         OR      C               
5262: FE 51      CP      $51             
5264: FC         ???                     
5265: 23         INC     HL              
5266: FC         ???                     
5267: 43         LD      B,E             
5268: F9         LD      SP,HL           
5269: C7         RST     0X00            
526A: F3         DI                      
526B: 0F         RRCA                    
526C: E3         ???                     
526D: 1F         RRA                     
526E: DB         ???                     
526F: 27         DAA                     
5270: 3D         DEC     A               
5271: FE 9E      CP      $9E             
5273: 7F         LD      A,A             
5274: DF         RST     0X18            
5275: 3F         CCF                     
5276: 0F         RRCA                    
5277: FF         RST     0X38            
5278: C3 F3 ED   JP      $EDF3           
527B: ED         ???                     
527C: E9         JP      (HL)            
527D: E5         PUSH    HL              
527E: F3         DI                      
527F: F3         DI                      
5280: FF         RST     0X38            
5281: 1C         INC     E               
5282: FF         RST     0X38            
5283: 03         INC     BC              
5284: 7F         LD      A,A             
5285: 83         ADD     A,E             
5286: 9F         SBC     A               
5287: E0 E3      LDFF00  ($E3),A         
5289: FC         ???                     
528A: FC         ???                     
528B: FF         RST     0X38            
528C: FF         RST     0X38            
528D: FF         RST     0X38            
528E: FF         RST     0X38            
528F: FF         RST     0X38            
5290: FF         RST     0X38            
5291: 3C         INC     A               
5292: FF         RST     0X38            
5293: FE FF      CP      $FF             
5295: FF         RST     0X38            
5296: FF         RST     0X38            
5297: 3F         CCF                     
5298: FF         RST     0X38            
5299: 00         NOP                     
529A: 0F         RRCA                    
529B: F0 A0      LD      A,($A0)         
529D: FF         RST     0X38            
529E: BB         CP      E               
529F: FF         RST     0X38            
52A0: FF         RST     0X38            
52A1: 1C         INC     E               
52A2: FF         RST     0X38            
52A3: 3E FF      LD      A,$FF           
52A5: 7F         LD      A,A             
52A6: FF         RST     0X38            
52A7: FF         RST     0X38            
52A8: FF         RST     0X38            
52A9: 00         NOP                     
52AA: FF         RST     0X38            
52AB: 00         NOP                     
52AC: 00         NOP                     
52AD: FF         RST     0X38            
52AE: B7         OR      A               
52AF: FF         RST     0X38            
52B0: FF         RST     0X38            
52B1: 18 FF      JR      $52B2           
52B3: 3C         INC     A               
52B4: FF         RST     0X38            
52B5: 7E         LD      A,(HL)          
52B6: FF         RST     0X38            
52B7: FF         RST     0X38            
52B8: FF         RST     0X38            
52B9: 00         NOP                     
52BA: FF         RST     0X38            
52BB: 00         NOP                     
52BC: 00         NOP                     
52BD: E0 65      LDFF00  ($65),A         
52BF: EA FF 3C   LD      ($3CFF),A       
52C2: FF         RST     0X38            
52C3: 7F         LD      A,A             
52C4: FF         RST     0X38            
52C5: FF         RST     0X38            
52C6: FF         RST     0X38            
52C7: 80         ADD     A,B             
52C8: FF         RST     0X38            
52C9: 00         NOP                     
52CA: E0 00      LDFF00  ($00),A         
52CC: 0A         LD      A,(BC)          
52CD: 15         DEC     D               
52CE: 00         NOP                     
52CF: FF         RST     0X38            
52D0: FE FD      CP      $FD             
52D2: FF         RST     0X38            
52D3: F8 FE      LDHL    SP,$FE          
52D5: 01 FC 02   LD      BC,$02FC        
52D8: E0 00      LDFF00  ($00),A         
52DA: 04         INC     B               
52DB: 0B         DEC     BC              
52DC: AA         XOR     D               
52DD: 55         LD      D,L             
52DE: 01 FE 00   LD      BC,$00FE        
52E1: E0 00      LDFF00  ($00),A         
52E3: C0         RET     NZ              
52E4: 00         NOP                     
52E5: 00         NOP                     
52E6: 00         NOP                     
52E7: 28 00      JR      Z,$52E9         
52E9: 54         LD      D,H             
52EA: 00         NOP                     
52EB: FA 80 7D   LD      A,($7D80)       
52EE: 50         LD      D,B             
52EF: AE         XOR     (HL)            
52F0: 00         NOP                     
52F1: 20 00      JR      NZ,$52F3        
52F3: 10 00      STOP    $00             
52F5: 10 00      STOP    $00             
52F7: 08 00 04   LD      ($0400),SP      
52FA: 00         NOP                     
52FB: 04         INC     B               
52FC: 00         NOP                     
52FD: 06 00      LD      B,$00           
52FF: 82         ADD     A,D             
5300: 0F         RRCA                    
5301: F0 0F      LD      A,($0F)         
5303: F0 0F      LD      A,($0F)         
5305: F0 0F      LD      A,($0F)         
5307: F0 F0      LD      A,($F0)         
5309: 0F         RRCA                    
530A: F0 0F      LD      A,($0F)         
530C: F0 0F      LD      A,($0F)         
530E: F0 0F      LD      A,($0F)         
5310: 00         NOP                     
5311: 00         NOP                     
5312: 00         NOP                     
5313: 00         NOP                     
5314: 00         NOP                     
5315: 07         RLCA                    
5316: 00         NOP                     
5317: 07         RLCA                    
5318: 01 1E 07   LD      BC,$071E        
531B: 38 1F      JR      C,$533C         
531D: 67         LD      H,A             
531E: 3F         CCF                     
531F: C8         RET     Z               
5320: 0B         DEC     BC              
5321: F5         PUSH    AF              
5322: 07         RLCA                    
5323: 38 43      JR      C,$5368         
5325: 84         ADD     A,H             
5326: 7C         LD      A,H             
5327: 8F         ADC     A,A             
5328: FF         RST     0X38            
5329: 3F         CCF                     
532A: FF         RST     0X38            
532B: FF         RST     0X38            
532C: FF         RST     0X38            
532D: 00         NOP                     
532E: E0 1F      LDFF00  ($1F),A         
5330: FF         RST     0X38            
5331: D6 FF      SUB     $FF             
5333: 3D         DEC     A               
5334: FF         RST     0X38            
5335: 03         INC     BC              
5336: 7F         LD      A,A             
5337: 80         ADD     A,B             
5338: 87         ADD     A,A             
5339: F8 F0      LDHL    SP,$F0          
533B: FF         RST     0X38            
533C: FF         RST     0X38            
533D: FF         RST     0X38            
533E: FF         RST     0X38            
533F: 0F         RRCA                    
5340: FF         RST     0X38            
5341: 89         ADC     A,C             
5342: FF         RST     0X38            
5343: 07         RLCA                    
5344: FF         RST     0X38            
5345: F8 FF      LDHL    SP,$FF          
5347: 00         NOP                     
5348: FF         RST     0X38            
5349: 00         NOP                     
534A: 00         NOP                     
534B: FF         RST     0X38            
534C: FF         RST     0X38            
534D: FF         RST     0X38            
534E: FF         RST     0X38            
534F: FF         RST     0X38            
5350: FF         RST     0X38            
5351: E0 FF      LDFF00  ($FF),A         
5353: 80         ADD     A,B             
5354: FC         ???                     
5355: 03         INC     BC              
5356: C1         POP     BC              
5357: 3E 1C      LD      A,$1C           
5359: FF         RST     0X38            
535A: FF         RST     0X38            
535B: FF         RST     0X38            
535C: FE FE      CP      $FE             
535E: FE FE      CP      $FE             
5360: 81         ADD     A,C             
5361: 7F         LD      A,A             
5362: 31 FF BC   LD      SP,$BCFF        
5365: 7C         LD      A,H             
5366: BB         CP      E               
5367: 7B         LD      A,E             
5368: 3A         LD      A,(HLD)         
5369: F9         LD      SP,HL           
536A: 3C         INC     A               
536B: 3C         INC     A               
536C: DF         RST     0X18            
536D: DF         RST     0X18            
536E: 9F         SBC     A               
536F: 5F         LD      E,A             
5370: FF         RST     0X38            
5371: FF         RST     0X38            
5372: FF         RST     0X38            
5373: FF         RST     0X38            
5374: FF         RST     0X38            
5375: FF         RST     0X38            
5376: 7F         LD      A,A             
5377: 7F         LD      A,A             
5378: 7F         LD      A,A             
5379: 7F         LD      A,A             
537A: F7         RST     0X30            
537B: FF         RST     0X38            
537C: E3         ???                     
537D: F7         RST     0X30            
537E: C1         POP     BC              
537F: F3         DI                      
5380: FF         RST     0X38            
5381: FF         RST     0X38            
5382: FF         RST     0X38            
5383: FF         RST     0X38            
5384: EF         RST     0X28            
5385: FF         RST     0X38            
5386: C7         RST     0X00            
5387: EF         RST     0X28            
5388: 83         ADD     A,E             
5389: E7         RST     0X20            
538A: B3         OR      E               
538B: CF         RST     0X08            
538C: BB         CP      E               
538D: F7         RST     0X30            
538E: D7         RST     0X10            
538F: FF         RST     0X38            
5390: 9B         SBC     E               
5391: FF         RST     0X38            
5392: DA FF D9   JP      C,$D9FF         
5395: FF         RST     0X38            
5396: DB         ???                     
5397: FF         RST     0X38            
5398: DF         RST     0X18            
5399: FF         RST     0X38            
539A: DF         RST     0X18            
539B: FF         RST     0X38            
539C: DE FF      SBC     $FF             
539E: DD         ???                     
539F: FF         RST     0X38            
53A0: 7B         LD      A,E             
53A1: FF         RST     0X38            
53A2: ED         ???                     
53A3: FF         RST     0X38            
53A4: D6 FF      SUB     $FF             
53A6: B7         OR      A               
53A7: FF         RST     0X38            
53A8: BB         CP      E               
53A9: FF         RST     0X38            
53AA: 7D         LD      A,L             
53AB: FE FE      CP      $FE             
53AD: FF         RST     0X38            
53AE: FD         ???                     
53AF: C0         RET     NZ              
53B0: A0         AND     B               
53B1: EF         RST     0X28            
53B2: A0         AND     B               
53B3: EF         RST     0X28            
53B4: B0         OR      B               
53B5: F5         PUSH    AF              
53B6: 30 C2      JR      NC,$537A        
53B8: F0 05      LD      A,($05)         
53BA: F0 02      LD      A,($02)         
53BC: F0 00      LD      A,($00)         
53BE: B0         OR      B               
53BF: 00         NOP                     
53C0: 00         NOP                     
53C1: FF         RST     0X38            
53C2: 00         NOP                     
53C3: EA 00 55   LD      ($5500),A       
53C6: 00         NOP                     
53C7: AA         XOR     D               
53C8: 00         NOP                     
53C9: 50         LD      D,B             
53CA: 00         NOP                     
53CB: 00         NOP                     
53CC: 00         NOP                     
53CD: 00         NOP                     
53CE: 00         NOP                     
53CF: 00         NOP                     
53D0: 00         NOP                     
53D1: FF         RST     0X38            
53D2: 00         NOP                     
53D3: BF         CP      A               
53D4: 00         NOP                     
53D5: 57         LD      D,A             
53D6: 00         NOP                     
53D7: AA         XOR     D               
53D8: 00         NOP                     
53D9: 05         DEC     B               
53DA: 00         NOP                     
53DB: 00         NOP                     
53DC: 00         NOP                     
53DD: 00         NOP                     
53DE: 00         NOP                     
53DF: FC         ???                     
53E0: 28 D7      JR      Z,$53B9         
53E2: 14         INC     D               
53E3: EB         ???                     
53E4: 0A         LD      A,(BC)          
53E5: F5         PUSH    AF              
53E6: 04         INC     B               
53E7: FB         EI                      
53E8: 02         LD      (BC),A          
53E9: 7D         LD      A,L             
53EA: 01 BE 00   LD      BC,$00BE        
53ED: 57         LD      D,A             
53EE: 00         NOP                     
53EF: 0F         RRCA                    
53F0: 00         NOP                     
53F1: 42         LD      B,D             
53F2: 00         NOP                     
53F3: A7         AND     A               
53F4: 02         LD      (BC),A          
53F5: 5D         LD      E,L             
53F6: 06 B9      LD      B,$B9           
53F8: 0E 71      LD      C,$71           
53FA: 1E E1      LD      E,$E1           
53FC: 3E C1      LD      A,$C1           
53FE: FE 81      CP      $81             
5400: 00         NOP                     
5401: 03         INC     BC              
5402: 01 06 00   LD      BC,$0006        
5405: 07         RLCA                    
5406: 07         RLCA                    
5407: 0E 07      LD      C,$07           
5409: 06 03      LD      B,$03           
540B: 03         INC     BC              
540C: 03         INC     BC              
540D: 03         INC     BC              
540E: 01 01 F8   LD      BC,$F801        
5411: 07         RLCA                    
5412: 07         RLCA                    
5413: FD         ???                     
5414: 7F         LD      A,A             
5415: DD         ???                     
5416: FF         RST     0X38            
5417: DE FE      SBC     $FE             
5419: EF         RST     0X28            
541A: F0 6F      LD      A,($6F)         
541C: C7         RST     0X00            
541D: 78         LD      A,B             
541E: 1F         RRA                     
541F: E0 1F      LDFF00  ($1F),A         
5421: FD         ???                     
5422: FF         RST     0X38            
5423: DD         ???                     
5424: FF         RST     0X38            
5425: EE FF      XOR     $FF             
5427: EE 00      XOR     $00             
5429: FF         RST     0X38            
542A: 7F         LD      A,A             
542B: 80         ADD     A,B             
542C: FF         RST     0X38            
542D: 00         NOP                     
542E: FF         RST     0X38            
542F: FF         RST     0X38            
5430: 1F         RRA                     
5431: E1         POP     HL              
5432: E7         RST     0X20            
5433: D8         RET     C               
5434: F9         LD      SP,HL           
5435: DE FE      SBC     $FE             
5437: ED         ???                     
5438: 7F         LD      A,A             
5439: ED         ???                     
543A: 0F         RRCA                    
543B: F6 F1      OR      $F1             
543D: 0E FE      LD      C,$FE           
543F: 01 FF FF   LD      BC,$FFFF        
5442: FF         RST     0X38            
5443: 7F         LD      A,A             
5444: FC         ???                     
5445: 3F         CCF                     
5446: F8 18      LDHL    SP,$18          
5448: 7D         LD      A,L             
5449: 8D         ADC     A,L             
544A: BE         CP      (HL)            
544B: C6 DF      ADD     $DF             
544D: A1         AND     C               
544E: 67         LD      H,A             
544F: B8         CP      B               
5450: FF         RST     0X38            
5451: FF         RST     0X38            
5452: 03         INC     BC              
5453: FF         RST     0X38            
5454: F8 16      LDHL    SP,$16          
5456: 1C         INC     E               
5457: 0A         LD      A,(BC)          
5458: C0         RET     NZ              
5459: C0         RET     NZ              
545A: C2 C2 3D   JP      NZ,$3DC2        
545D: 3D         DEC     A               
545E: C3 C3 37   JP      $37C3           
5461: 3F         CCF                     
5462: E3         ???                     
5463: F7         RST     0X30            
5464: C1         POP     BC              
5465: F3         DI                      
5466: 59         LD      E,C             
5467: 67         LD      H,A             
5468: DD         ???                     
5469: FB         EI                      
546A: EB         ???                     
546B: FF         RST     0X38            
546C: F7         RST     0X30            
546D: FF         RST     0X38            
546E: FF         RST     0X38            
546F: FF         RST     0X38            
5470: D9         RETI                    
5471: E7         RST     0X20            
5472: DD         ???                     
5473: FB         EI                      
5474: EB         ???                     
5475: FF         RST     0X38            
5476: F7         RST     0X30            
5477: FF         RST     0X38            
5478: FF         RST     0X38            
5479: FF         RST     0X38            
547A: FF         RST     0X38            
547B: FF         RST     0X38            
547C: F3         DI                      
547D: FC         ???                     
547E: FC         ???                     
547F: F3         DI                      
5480: EF         RST     0X28            
5481: FF         RST     0X38            
5482: FF         RST     0X38            
5483: FF         RST     0X38            
5484: FF         RST     0X38            
5485: FF         RST     0X38            
5486: FF         RST     0X38            
5487: FD         ???                     
5488: FF         RST     0X38            
5489: EA FC 57   LD      ($57FC),A       
548C: E3         ???                     
548D: BC         CP      H               
548E: 1E E1      LD      E,$E1           
5490: DD         ???                     
5491: F0 DE      LD      A,($DE)         
5493: E0 BF      LDFF00  ($BF),A         
5495: 00         NOP                     
5496: BB         CP      E               
5497: 00         NOP                     
5498: B9         CP      C               
5499: 00         NOP                     
549A: 36 00      LD      (HL),$00        
549C: 74         LD      (HL),H          
549D: 00         NOP                     
549E: 73         LD      (HL),E          
549F: 00         NOP                     
54A0: FB         EI                      
54A1: 00         NOP                     
54A2: F6 00      OR      $00             
54A4: 6D         LD      L,L             
54A5: 00         NOP                     
54A6: 98         SBC     B               
54A7: 00         NOP                     
54A8: F3         DI                      
54A9: 00         NOP                     
54AA: 7C         LD      A,H             
54AB: 03         INC     BC              
54AC: E0 1C      LDFF00  ($1C),A         
54AE: 00         NOP                     
54AF: E0 30      LDFF00  ($30),A         
54B1: 00         NOP                     
54B2: B0         OR      B               
54B3: 00         NOP                     
54B4: A0         AND     B               
54B5: 03         INC     BC              
54B6: 60         LD      H,B             
54B7: 1C         INC     E               
54B8: 80         ADD     A,B             
54B9: 60         LD      H,B             
54BA: 00         NOP                     
54BB: 80         ADD     A,B             
54BC: 00         NOP                     
54BD: 00         NOP                     
54BE: 00         NOP                     
54BF: 00         NOP                     
54C0: 00         NOP                     
54C1: 1F         RRA                     
54C2: 00         NOP                     
54C3: E0 00      LDFF00  ($00),A         
54C5: 00         NOP                     
54C6: 00         NOP                     
54C7: 00         NOP                     
54C8: 00         NOP                     
54C9: 00         NOP                     
54CA: 00         NOP                     
54CB: 03         INC     BC              
54CC: 03         INC     BC              
54CD: 0C         INC     C               
54CE: 0F         RRCA                    
54CF: 70         LD      (HL),B          
54D0: 00         NOP                     
54D1: 03         INC     BC              
54D2: 00         NOP                     
54D3: 00         NOP                     
54D4: 00         NOP                     
54D5: 00         NOP                     
54D6: 00         NOP                     
54D7: 00         NOP                     
54D8: 00         NOP                     
54D9: 00         NOP                     
54DA: 00         NOP                     
54DB: FF         RST     0X38            
54DC: FF         RST     0X38            
54DD: 00         NOP                     
54DE: FF         RST     0X38            
54DF: 00         NOP                     
54E0: 01 87 0F   LD      BC,$0F87        
54E3: 61         LD      H,C             
54E4: 0F         RRCA                    
54E5: 20 03      JR      NZ,$54EA        
54E7: 40         LD      B,B             
54E8: 08 50 58   LD      ($5850),SP      
54EB: 88         ADC     A,B             
54EC: E1         POP     HL              
54ED: 02         LD      (BC),A          
54EE: FB         EI                      
54EF: 01 FE C1   LD      BC,$C1FE        
54F2: FE C1      CP      $C1             
54F4: FC         ???                     
54F5: C2 FC C2   JP      NZ,$C2FC        
54F8: 7C         LD      A,H             
54F9: 40         LD      B,B             
54FA: 00         NOP                     
54FB: 04         INC     B               
54FC: 00         NOP                     
54FD: 04         INC     B               
54FE: 20 44      JR      NZ,$5544        
5500: 00         NOP                     
5501: 03         INC     BC              
5502: 00         NOP                     
5503: 07         RLCA                    
5504: 01 0E 07   LD      BC,$070E        
5507: 18 1F      JR      $5528           
5509: 20 30      JR      NZ,$553B        
550B: CF         RST     0X08            
550C: 03         INC     BC              
550D: 7C         LD      A,H             
550E: 00         NOP                     
550F: 1F         RRA                     
5510: 7F         LD      A,A             
5511: 80         ADD     A,B             
5512: FF         RST     0X38            
5513: 3F         CCF                     
5514: FF         RST     0X38            
5515: 00         NOP                     
5516: FF         RST     0X38            
5517: FF         RST     0X38            
5518: C7         RST     0X00            
5519: 3B         DEC     SP              
551A: 7F         LD      A,A             
551B: A8         XOR     B               
551C: 87         ADD     A,A             
551D: 7B         LD      A,E             
551E: 78         LD      A,B             
551F: 8F         ADC     A,A             
5520: FF         RST     0X38            
5521: 01 FF FE   LD      BC,$FEFF        
5524: FF         RST     0X38            
5525: 7F         LD      A,A             
5526: FF         RST     0X38            
5527: 83         ADD     A,E             
5528: FF         RST     0X38            
5529: FC         ???                     
552A: FF         RST     0X38            
552B: 7F         LD      A,A             
552C: FF         RST     0X38            
552D: 83         ADD     A,E             
552E: FF         RST     0X38            
552F: FC         ???                     
5530: FF         RST     0X38            
5531: FE FF      CP      $FF             
5533: 07         RLCA                    
5534: FF         RST     0X38            
5535: F8 FF      LDHL    SP,$FF          
5537: FF         RST     0X38            
5538: FF         RST     0X38            
5539: 00         NOP                     
553A: FF         RST     0X38            
553B: FF         RST     0X38            
553C: FF         RST     0X38            
553D: FF         RST     0X38            
553E: FF         RST     0X38            
553F: 00         NOP                     
5540: 87         ADD     A,A             
5541: 60         LD      H,B             
5542: F8 C0      LDHL    SP,$C0          
5544: FF         RST     0X38            
5545: 3F         CCF                     
5546: FF         RST     0X38            
5547: FF         RST     0X38            
5548: FF         RST     0X38            
5549: 00         NOP                     
554A: FF         RST     0X38            
554B: FF         RST     0X38            
554C: FF         RST     0X38            
554D: FF         RST     0X38            
554E: FF         RST     0X38            
554F: 00         NOP                     
5550: FF         RST     0X38            
5551: FF         RST     0X38            
5552: FF         RST     0X38            
5553: 3F         CCF                     
5554: FF         RST     0X38            
5555: FC         ???                     
5556: FF         RST     0X38            
5557: 03         INC     BC              
5558: FF         RST     0X38            
5559: FF         RST     0X38            
555A: FE FD      CP      $FD             
555C: FF         RST     0X38            
555D: 01 FF EA   LD      BC,$EAFF        
5560: FF         RST     0X38            
5561: F7         RST     0X30            
5562: FF         RST     0X38            
5563: E8 F3      ADD     SP,$F3          
5565: 0E FD      LD      C,$FD           
5567: EB         ???                     
5568: F8 57      LDHL    SP,$57          
556A: A6         AND     (HL)            
556B: 59         LD      E,C             
556C: FC         ???                     
556D: 43         LD      B,E             
556E: E3         ???                     
556F: 1C         INC     E               
5570: FF         RST     0X38            
5571: C0         RET     NZ              
5572: FF         RST     0X38            
5573: 00         NOP                     
5574: E7         RST     0X20            
5575: 00         NOP                     
5576: D3         ???                     
5577: 00         NOP                     
5578: CB 88      SET     1,E             
557A: E7         RST     0X20            
557B: 80         ADD     A,B             
557C: FC         ???                     
557D: C0         RET     NZ              
557E: 7A         LD      A,D             
557F: C0         RET     NZ              
5580: 71         LD      (HL),C          
5581: 8E         ADC     A,(HL)          
5582: 8F         ADC     A,A             
5583: 50         LD      D,B             
5584: CC 22 E2   CALL    Z,$E222         
5587: 0D         DEC     C               
5588: E0 16      LDFF00  ($16),A         
558A: E0 17      LDFF00  ($17),A         
558C: F7         RST     0X30            
558D: 0F         RRCA                    
558E: 73         LD      (HL),E          
558F: 0F         RRCA                    
5590: 7C         LD      A,H             
5591: 03         INC     BC              
5592: 70         LD      (HL),B          
5593: 0C         INC     C               
5594: C0         RET     NZ              
5595: 30 00      JR      NC,$5597        
5597: C0         RET     NZ              
5598: 00         NOP                     
5599: 38 18      JR      C,$55B3         
559B: E0 B8      LDFF00  ($B8),A         
559D: D8         RET     C               
559E: 00         NOP                     
559F: 80         ADD     A,B             
55A0: FF         RST     0X38            
55A1: 0F         RRCA                    
55A2: FF         RST     0X38            
55A3: 0F         RRCA                    
55A4: FF         RST     0X38            
55A5: 0F         RRCA                    
55A6: FF         RST     0X38            
55A7: 0F         RRCA                    
55A8: FF         RST     0X38            
55A9: F0 FF      LD      A,($FF)         
55AB: F0 FF      LD      A,($FF)         
55AD: F0 FF      LD      A,($FF)         
55AF: F0 00      LD      A,($00)         
55B1: 01 00 03   LD      BC,$0300        
55B4: 03         INC     BC              
55B5: 0C         INC     C               
55B6: 07         RLCA                    
55B7: 1F         RRA                     
55B8: 00         NOP                     
55B9: 3F         CCF                     
55BA: 00         NOP                     
55BB: 00         NOP                     
55BC: 00         NOP                     
55BD: 00         NOP                     
55BE: 00         NOP                     
55BF: 00         NOP                     
55C0: 7F         LD      A,A             
55C1: 80         ADD     A,B             
55C2: FF         RST     0X38            
55C3: 00         NOP                     
55C4: FF         RST     0X38            
55C5: 38 FF      JR      C,$55C6         
55C7: FF         RST     0X38            
55C8: FF         RST     0X38            
55C9: FF         RST     0X38            
55CA: 3F         CCF                     
55CB: FF         RST     0X38            
55CC: 1F         RRA                     
55CD: 3F         CCF                     
55CE: 0F         RRCA                    
55CF: 1F         RRA                     
55D0: FF         RST     0X38            
55D1: 00         NOP                     
55D2: FF         RST     0X38            
55D3: 00         NOP                     
55D4: FF         RST     0X38            
55D5: 00         NOP                     
55D6: FF         RST     0X38            
55D7: 00         NOP                     
55D8: FF         RST     0X38            
55D9: FF         RST     0X38            
55DA: FF         RST     0X38            
55DB: FF         RST     0X38            
55DC: FF         RST     0X38            
55DD: FF         RST     0X38            
55DE: FF         RST     0X38            
55DF: FF         RST     0X38            
55E0: FC         ???                     
55E1: 00         NOP                     
55E2: FE 00      CP      $00             
55E4: FF         RST     0X38            
55E5: 00         NOP                     
55E6: FF         RST     0X38            
55E7: 00         NOP                     
55E8: FF         RST     0X38            
55E9: E0 FF      LDFF00  ($FF),A         
55EB: F0 FF      LD      A,($FF)         
55ED: F8 BF      LDHL    SP,$BF          
55EF: F0 60      LD      A,($60)         
55F1: 24         INC     H               
55F2: 00         NOP                     
55F3: 04         INC     B               
55F4: 80         ADD     A,B             
55F5: 08 E0 08   LD      ($08E0),SP      
55F8: C0         RET     NZ              
55F9: 30 C0      JR      NC,$55BB        
55FB: 20 C0      JR      NZ,$55BD        
55FD: 20 C0      JR      NZ,$55BF        
55FF: 20 00      JR      NZ,$5601        
5601: 07         RLCA                    
5602: 00         NOP                     
5603: 01 00 00   LD      BC,$0000        
5606: 00         NOP                     
5607: 00         NOP                     
5608: 00         NOP                     
5609: 00         NOP                     
560A: 00         NOP                     
560B: 00         NOP                     
560C: 00         NOP                     
560D: 00         NOP                     
560E: 00         NOP                     
560F: 00         NOP                     
5610: 8F         ADC     A,A             
5611: 71         LD      (HL),C          
5612: 11 EE 06   LD      DE,$06EE        
5615: 79         LD      A,C             
5616: 00         NOP                     
5617: 0F         RRCA                    
5618: 00         NOP                     
5619: 03         INC     BC              
561A: 00         NOP                     
561B: 00         NOP                     
561C: 00         NOP                     
561D: 00         NOP                     
561E: 00         NOP                     
561F: 00         NOP                     
5620: 5F         LD      E,A             
5621: B5         OR      L               
5622: FB         EI                      
5623: 26 3C      LD      H,$3C           
5625: C3 47 B8   JP      $B847           
5628: 08 F7 00   LD      ($00F7),SP      
562B: 3F         CCF                     
562C: 00         NOP                     
562D: 07         RLCA                    
562E: 00         NOP                     
562F: 00         NOP                     
5630: FF         RST     0X38            
5631: 77         LD      (HL),A          
5632: FF         RST     0X38            
5633: AA         XOR     D               
5634: 57         LD      D,A             
5635: AD         XOR     L               
5636: FA 05 1F   LD      A,($1F05)       
5639: E0 20      LDFF00  ($20),A         
563B: DF         RST     0X18            
563C: 00         NOP                     
563D: FF         RST     0X38            
563E: 00         NOP                     
563F: 1F         RRA                     
5640: FF         RST     0X38            
5641: FF         RST     0X38            
5642: FF         RST     0X38            
5643: AA         XOR     D               
5644: FD         ???                     
5645: 56         LD      D,(HL)          
5646: AB         XOR     E               
5647: 54         LD      D,H             
5648: FF         RST     0X38            
5649: 00         NOP                     
564A: 08 F7 00   LD      ($00F7),SP      
564D: FE 00      CP      $00             
564F: 00         NOP                     
5650: FE D5      CP      $D5             
5652: E9         JP      (HL)            
5653: B6         OR      (HL)            
5654: 5F         LD      E,A             
5655: A0         AND     B               
5656: F8 07      LDHL    SP,$07          
5658: 80         ADD     A,B             
5659: 7F         LD      A,A             
565A: 00         NOP                     
565B: F8 07      LDHL    SP,$07          
565D: 05         DEC     B               
565E: 03         INC     BC              
565F: 06 1E      LD      B,$1E           
5661: E1         POP     HL              
5662: F8 07      LDHL    SP,$07          
5664: 00         NOP                     
5665: FF         RST     0X38            
5666: 80         ADD     A,B             
5667: 70         LD      (HL),B          
5668: 0C         INC     C               
5669: 86         ADD     A,(HL)          
566A: FC         ???                     
566B: AA         XOR     D               
566C: FE 55      CP      $55             
566E: FE AB      CP      $AB             
5670: 39         ADD     HL,SP           
5671: E1         POP     HL              
5672: 3C         INC     A               
5673: F0 1F      LD      A,($1F)         
5675: 30 1F      JR      NC,$5696        
5677: 38 0F      JR      C,$5688         
5679: 18 37      JR      $56B2           
567B: 0C         INC     C               
567C: B7         OR      A               
567D: 5E         LD      E,(HL)          
567E: 03         INC     BC              
567F: 87         ADD     A,A             
5680: 78         LD      A,B             
5681: 07         RLCA                    
5682: FC         ???                     
5683: 03         INC     BC              
5684: CF         RST     0X08            
5685: 00         NOP                     
5686: A7         AND     A               
5687: 00         NOP                     
5688: 97         SUB     A               
5689: 10 CF      STOP    $CF             
568B: 00         NOP                     
568C: FC         ???                     
568D: 00         NOP                     
568E: FA 00 00   LD      A,($0000)       
5691: 03         INC     BC              
5692: 01 C2 03   LD      BC,$03C2        
5695: BD         CP      L               
5696: BC         CP      H               
5697: 7E         LD      A,(HL)          
5698: D8         RET     C               
5699: 3C         INC     A               
569A: E0 1C      LDFF00  ($1C),A         
569C: F0 08      LD      A,($08)         
569E: 78         LD      A,B             
569F: 07         RLCA                    
56A0: 00         NOP                     
56A1: 80         ADD     A,B             
56A2: 80         ADD     A,B             
56A3: 00         NOP                     
56A4: 80         ADD     A,B             
56A5: 80         ADD     A,B             
56A6: 00         NOP                     
56A7: 07         RLCA                    
56A8: 03         INC     BC              
56A9: 04         INC     B               
56AA: 07         RLCA                    
56AB: 03         INC     BC              
56AC: 00         NOP                     
56AD: 3C         INC     A               
56AE: 10 F8      STOP    $F8             
56B0: FF         RST     0X38            
56B1: 0F         RRCA                    
56B2: FF         RST     0X38            
56B3: 0F         RRCA                    
56B4: FF         RST     0X38            
56B5: 0E FF      LD      C,$FF           
56B7: 0E FC      LD      C,$FC           
56B9: F3         DI                      
56BA: F8 F7      LDHL    SP,$F7          
56BC: F0 FF      LD      A,($FF)         
56BE: F0 CF      LD      A,($CF)         
56C0: 07         RLCA                    
56C1: 1F         RRA                     
56C2: 03         INC     BC              
56C3: 0F         RRCA                    
56C4: 00         NOP                     
56C5: 03         INC     BC              
56C6: 00         NOP                     
56C7: 00         NOP                     
56C8: 00         NOP                     
56C9: 00         NOP                     
56CA: 00         NOP                     
56CB: 00         NOP                     
56CC: 00         NOP                     
56CD: 00         NOP                     
56CE: 00         NOP                     
56CF: 00         NOP                     
56D0: FC         ???                     
56D1: FF         RST     0X38            
56D2: C0         RET     NZ              
56D3: FC         ???                     
56D4: 00         NOP                     
56D5: C1         POP     BC              
56D6: 00         NOP                     
56D7: 01 00 01   LD      BC,$0100        
56DA: 00         NOP                     
56DB: 01 00 01   LD      BC,$0100        
56DE: 00         NOP                     
56DF: 01 3F F0   LD      BC,$F03F        
56E2: 7F         LD      A,A             
56E3: F0 7F      LD      A,($7F)         
56E5: F8 FF      LDHL    SP,$FF          
56E7: F8 FF      LDHL    SP,$FF          
56E9: F8 FF      LDHL    SP,$FF          
56EB: FC         ???                     
56EC: FF         RST     0X38            
56ED: FE FF      CP      $FF             
56EF: FF         RST     0X38            
56F0: C0         RET     NZ              
56F1: 20 C0      JR      NZ,$56B3        
56F3: 20 C0      JR      NZ,$56B5        
56F5: 20 C0      JR      NZ,$56B7        
56F7: 20 C0      JR      NZ,$56B9        
56F9: 20 C0      JR      NZ,$56BB        
56FB: 20 C0      JR      NZ,$56BD        
56FD: 70         LD      (HL),B          
56FE: E0 F0      LDFF00  ($F0),A         
5700: 0F         RRCA                    
5701: F0 0F      LD      A,($0F)         
5703: F0 0E      LD      A,($0E)         
5705: F0 0E      LD      A,($0E)         
5707: F0 F0      LD      A,($F0)         
5709: 0C         INC     C               
570A: F0 08      LD      A,($08)         
570C: F0 00      LD      A,($00)         
570E: C0         RET     NZ              
570F: 00         NOP                     
5710: FF         RST     0X38            
5711: 0F         RRCA                    
5712: FF         RST     0X38            
5713: 0F         RRCA                    
5714: 7F         LD      A,A             
5715: 8F         ADC     A,A             
5716: 7F         LD      A,A             
5717: 8F         ADC     A,A             
5718: FF         RST     0X38            
5719: 30 FF      JR      NC,$571A        
571B: 10 FF      STOP    $FF             
571D: 00         NOP                     
571E: F3         DI                      
571F: 0C         INC     C               
5720: 00         NOP                     
5721: 00         NOP                     
5722: 00         NOP                     
5723: 00         NOP                     
5724: 00         NOP                     
5725: 01 01 06   LD      BC,$0601        
5728: 07         RLCA                    
5729: 38 3F      JR      C,$576A         
572B: 40         LD      B,B             
572C: 79         LD      A,C             
572D: 86         ADD     A,(HL)          
572E: 7E         LD      A,(HL)          
572F: 81         ADD     A,C             
5730: 00         NOP                     
5731: 60         LD      H,B             
5732: 60         LD      H,B             
5733: 90         SUB     B               
5734: E0 10      LDFF00  ($10),A         
5736: C0         RET     NZ              
5737: 20 00      JR      NZ,$5739        
5739: C7         RST     0X00            
573A: C7         RST     0X00            
573B: 28 8F      JR      Z,$56CC         
573D: 73         LD      (HL),E          
573E: 5F         LD      E,A             
573F: AF         XOR     A               
5740: 00         NOP                     
5741: 07         RLCA                    
5742: 06 0B      LD      B,$0B           
5744: 0E 17      LD      C,$17           
5746: 1E 6E      LD      E,$6E           
5748: 7C         LD      A,H             
5749: BE         CP      (HL)            
574A: F8 77      LDHL    SP,$77          
574C: F6 CB      OR      $CB             
574E: DE A7      SBC     $A7             
5750: 01 03 01   LD      BC,$0103        
5753: 03         INC     BC              
5754: 00         NOP                     
5755: 01 00 00   LD      BC,$0000        
5758: 00         NOP                     
5759: 00         NOP                     
575A: 00         NOP                     
575B: 00         NOP                     
575C: 00         NOP                     
575D: 00         NOP                     
575E: 00         NOP                     
575F: 00         NOP                     
5760: FE 55      CP      $55             
5762: FE AB      CP      $AB             
5764: FF         RST     0X38            
5765: FF         RST     0X38            
5766: 7F         LD      A,A             
5767: FF         RST     0X38            
5768: 3F         CCF                     
5769: FF         RST     0X38            
576A: 0F         RRCA                    
576B: 7F         LD      A,A             
576C: 01 1F 00   LD      BC,$001F        
576F: 01 0D 03   LD      BC,$030D        
5772: 0C         INC     C               
5773: F5         PUSH    AF              
5774: 40         LD      B,B             
5775: A0         AND     B               
5776: 00         NOP                     
5777: C0         RET     NZ              
5778: 00         NOP                     
5779: 80         ADD     A,B             
577A: 00         NOP                     
577B: 80         ADD     A,B             
577C: 00         NOP                     
577D: 80         ADD     A,B             
577E: 00         NOP                     
577F: 80         ADD     A,B             
5780: F9         LD      SP,HL           
5781: 81         ADD     A,C             
5782: FC         ???                     
5783: E0 3F      LDFF00  ($3F),A         
5785: F8 1F      LDHL    SP,$1F          
5787: 7C         LD      A,H             
5788: 07         RLCA                    
5789: 1F         RRA                     
578A: 00         NOP                     
578B: 07         RLCA                    
578C: 00         NOP                     
578D: 00         NOP                     
578E: 00         NOP                     
578F: 00         NOP                     
5790: 79         LD      A,C             
5791: 07         RLCA                    
5792: E4         ???                     
5793: 03         INC     BC              
5794: D2 01 CB   JP      NC,$CB01        
5797: 08 E7 80   LD      ($80E7),SP      
579A: FF         RST     0X38            
579B: FF         RST     0X38            
579C: 00         NOP                     
579D: FF         RST     0X38            
579E: 00         NOP                     
579F: 00         NOP                     
57A0: F0 F8      LD      A,($F8)         
57A2: F0 F8      LD      A,($F8)         
57A4: 30 F8      JR      NC,$579E        
57A6: D0         RET     NC              
57A7: 38 E0      JR      C,$5789         
57A9: 18 F8      JR      $57A3           
57AB: 87         ADD     A,A             
57AC: 7E         LD      A,(HL)          
57AD: FF         RST     0X38            
57AE: 00         NOP                     
57AF: 7F         LD      A,A             
57B0: 7E         LD      A,(HL)          
57B1: C1         POP     BC              
57B2: 7D         LD      A,L             
57B3: C2 3E 61   JP      NZ,$613E        
57B6: 3F         CCF                     
57B7: 60         LD      H,B             
57B8: 1E 31      LD      E,$31           
57BA: 1F         RRA                     
57BB: 30 0F      JR      NC,$57CC        
57BD: 38 0F      JR      C,$57CE         
57BF: 18 9F      JR      $5760           
57C1: 69         LD      L,C             
57C2: BF         CP      A               
57C3: 5E         LD      E,(HL)          
57C4: 3F         CCF                     
57C5: DD         ???                     
57C6: 3F         CCF                     
57C7: DA BF 5F   JP      C,$5FBF         
57CA: 3F         CCF                     
57CB: DE 7F      SBC     $7F             
57CD: BD         CP      L               
57CE: 7F         LD      A,A             
57CF: BF         CP      A               
57D0: FC         ???                     
57D1: 1E F0      LD      E,$F0           
57D3: FC         ???                     
57D4: 9C         SBC     H               
57D5: E2         LDFF00  (C),A           
57D6: FC         ???                     
57D7: FE F8      CP      $F8             
57D9: 7C         LD      A,H             
57DA: 80         ADD     A,B             
57DB: F8 E0      LDHL    SP,$E0          
57DD: F0 00      LD      A,($00)         
57DF: E0 FF      LDFF00  ($FF),A         
57E1: FF         RST     0X38            
57E2: FF         RST     0X38            
57E3: FF         RST     0X38            
57E4: 7F         LD      A,A             
57E5: FF         RST     0X38            
57E6: 7F         LD      A,A             
57E7: FF         RST     0X38            
57E8: 1F         RRA                     
57E9: 7F         LD      A,A             
57EA: 0F         RRCA                    
57EB: 3F         CCF                     
57EC: 01 0F 00   LD      BC,$000F        
57EF: 01 00 00   LD      BC,$0000        
57F2: 00         NOP                     
57F3: 00         NOP                     
57F4: 00         NOP                     
57F5: 00         NOP                     
57F6: 00         NOP                     
57F7: 00         NOP                     
57F8: 00         NOP                     
57F9: 00         NOP                     
57FA: 00         NOP                     
57FB: 00         NOP                     
57FC: 00         NOP                     
57FD: 00         NOP                     
57FE: 00         NOP                     
57FF: 00         NOP                     
5800: E0 E0      LDFF00  ($E0),A         
5802: F0 F0      LD      A,($F0)         
5804: 78         LD      A,B             
5805: F8 38      LDHL    SP,$38          
5807: F8 0F      LDHL    SP,$0F          
5809: FF         RST     0X38            
580A: C7         RST     0X00            
580B: FF         RST     0X38            
580C: 47         LD      B,A             
580D: FF         RST     0X38            
580E: 7F         LD      A,A             
580F: FF         RST     0X38            
5810: 00         NOP                     
5811: 00         NOP                     
5812: 00         NOP                     
5813: 00         NOP                     
5814: 00         NOP                     
5815: 00         NOP                     
5816: 00         NOP                     
5817: 00         NOP                     
5818: E0 E0      LDFF00  ($E0),A         
581A: F8 F8      LDHL    SP,$F8          
581C: 64         LD      H,H             
581D: FC         ???                     
581E: 86         ADD     A,(HL)          
581F: FE FF      CP      $FF             
5821: FF         RST     0X38            
5822: 55         LD      D,L             
5823: FF         RST     0X38            
5824: A2         AND     D               
5825: FF         RST     0X38            
5826: 81         ADD     A,C             
5827: FF         RST     0X38            
5828: 08 BF 01   LD      ($01BF),SP      
582B: 9F         SBC     A               
582C: 20 72      JR      NZ,$58A0        
582E: 00         NOP                     
582F: 9C         SBC     H               
5830: FF         RST     0X38            
5831: FF         RST     0X38            
5832: 55         LD      D,L             
5833: FF         RST     0X38            
5834: 45         LD      B,L             
5835: FF         RST     0X38            
5836: 10 FF      STOP    $FF             
5838: 08 FB 00   LD      ($00FB),SP      
583B: BC         CP      H               
583C: 02         LD      (BC),A          
583D: 9F         SBC     A               
583E: 00         NOP                     
583F: AC         XOR     H               
5840: 00         NOP                     
5841: 00         NOP                     
5842: 00         NOP                     
5843: 00         NOP                     
5844: 00         NOP                     
5845: 00         NOP                     
5846: 00         NOP                     
5847: 04         INC     B               
5848: 00         NOP                     
5849: 09         ADD     HL,BC           
584A: 00         NOP                     
584B: 02         LD      (BC),A          
584C: 00         NOP                     
584D: 08 00 10   LD      ($1000),SP      
5850: 00         NOP                     
5851: 03         INC     BC              
5852: 00         NOP                     
5853: 00         NOP                     
5854: 00         NOP                     
5855: 00         NOP                     
5856: 00         NOP                     
5857: C7         RST     0X00            
5858: 00         NOP                     
5859: 00         NOP                     
585A: 00         NOP                     
585B: 07         RLCA                    
585C: 0C         INC     C               
585D: 1E 10      LD      E,$10           
585F: B9         CP      C               
5860: 00         NOP                     
5861: 00         NOP                     
5862: 00         NOP                     
5863: 00         NOP                     
5864: 00         NOP                     
5865: 00         NOP                     
5866: 07         RLCA                    
5867: 00         NOP                     
5868: 18 00      JR      $586A           
586A: 20 00      JR      NZ,$586C        
586C: 40         LD      B,B             
586D: 00         NOP                     
586E: C0         RET     NZ              
586F: 00         NOP                     
5870: 00         NOP                     
5871: 00         NOP                     
5872: 0F         RRCA                    
5873: 00         NOP                     
5874: 70         LD      (HL),B          
5875: 00         NOP                     
5876: C0         RET     NZ              
5877: 00         NOP                     
5878: 00         NOP                     
5879: 00         NOP                     
587A: 00         NOP                     
587B: 00         NOP                     
587C: 01 00 03   LD      BC,$0300        
587F: 00         NOP                     
5880: 00         NOP                     
5881: 00         NOP                     
5882: 80         ADD     A,B             
5883: 00         NOP                     
5884: 70         LD      (HL),B          
5885: 00         NOP                     
5886: 18 00      JR      $5888           
5888: 06 00      LD      B,$00           
588A: 03         INC     BC              
588B: 00         NOP                     
588C: C0         RET     NZ              
588D: 00         NOP                     
588E: E1         POP     HL              
588F: 00         NOP                     
5890: 00         NOP                     
5891: 00         NOP                     
5892: 00         NOP                     
5893: 00         NOP                     
5894: 00         NOP                     
5895: 00         NOP                     
5896: 00         NOP                     
5897: 00         NOP                     
5898: 00         NOP                     
5899: 00         NOP                     
589A: E0 00      LDFF00  ($00),A         
589C: 30 00      JR      NC,$589E        
589E: 08 00 37   LD      ($3700),SP      
58A1: C2 59 A6   JP      NZ,$A659        
58A4: 51         LD      D,C             
58A5: 2E 83      LD      L,$83           
58A7: 7C         LD      A,H             
58A8: 86         ADD     A,(HL)          
58A9: 79         LD      A,C             
58AA: 80         ADD     A,B             
58AB: 7F         LD      A,A             
58AC: E0 1F      LDFF00  ($1F),A         
58AE: 98         SBC     B               
58AF: 67         LD      H,A             
58B0: F2         ???                     
58B1: 3C         INC     A               
58B2: F1         POP     AF              
58B3: 7E         LD      A,(HL)          
58B4: 7B         LD      A,E             
58B5: F7         RST     0X30            
58B6: 0F         RRCA                    
58B7: F7         RST     0X30            
58B8: 1F         RRA                     
58B9: E7         RST     0X20            
58BA: 7F         LD      A,A             
58BB: 0F         RRCA                    
58BC: 1F         RRA                     
58BD: FF         RST     0X38            
58BE: 0F         RRCA                    
58BF: FF         RST     0X38            
58C0: 37         SCF                     
58C1: C0         RET     NZ              
58C2: 5B         LD      E,E             
58C3: A4         AND     H               
58C4: 52         LD      D,D             
58C5: 2D         DEC     L               
58C6: 86         ADD     A,(HL)          
58C7: 79         LD      A,C             
58C8: 84         ADD     A,H             
58C9: 7B         LD      A,E             
58CA: C4 3B A0   CALL    NZ,$A03B        
58CD: 5F         LD      E,A             
58CE: 88         ADC     A,B             
58CF: 77         LD      (HL),A          
58D0: F2         ???                     
58D1: 7C         LD      A,H             
58D2: FD         ???                     
58D3: FE 77      CP      $77             
58D5: F7         RST     0X30            
58D6: 1F         RRA                     
58D7: E7         RST     0X20            
58D8: 3F         CCF                     
58D9: D7         RST     0X10            
58DA: 7F         LD      A,A             
58DB: 8F         ADC     A,A             
58DC: 1F         RRA                     
58DD: FF         RST     0X38            
58DE: 0F         RRCA                    
58DF: FF         RST     0X38            
58E0: 37         SCF                     
58E1: C0         RET     NZ              
58E2: 5B         LD      E,E             
58E3: A4         AND     H               
58E4: 52         LD      D,D             
58E5: 2D         DEC     L               
58E6: 86         ADD     A,(HL)          
58E7: 79         LD      A,C             
58E8: 84         ADD     A,H             
58E9: 7B         LD      A,E             
58EA: C4 3B A0   CALL    NZ,$A03B        
58ED: 5F         LD      E,A             
58EE: 98         SBC     B               
58EF: 67         LD      H,A             
58F0: F2         ???                     
58F1: 7C         LD      A,H             
58F2: FD         ???                     
58F3: FE 77      CP      $77             
58F5: FF         RST     0X38            
58F6: 3F         CCF                     
58F7: C7         RST     0X00            
58F8: 7F         LD      A,A             
58F9: 97         SUB     A               
58FA: FF         RST     0X38            
58FB: 0F         RRCA                    
58FC: 1F         RRA                     
58FD: FF         RST     0X38            
58FE: 0F         RRCA                    
58FF: FF         RST     0X38            
5900: 71         LD      (HL),C          
5901: FF         RST     0X38            
5902: 80         ADD     A,B             
5903: FF         RST     0X38            
5904: 40         LD      B,B             
5905: FF         RST     0X38            
5906: F8 FF      LDHL    SP,$FF          
5908: FC         ???                     
5909: FF         RST     0X38            
590A: 7C         LD      A,H             
590B: FF         RST     0X38            
590C: 07         RLCA                    
590D: FF         RST     0X38            
590E: 03         INC     BC              
590F: FF         RST     0X38            
5910: 9A         SBC     D               
5911: FE 8E      CP      $8E             
5913: FE 46      CP      $46             
5915: FE 06      CP      $06             
5917: FE 04      CP      $04             
5919: FC         ???                     
591A: 3C         INC     A               
591B: FC         ???                     
591C: 0E FE      LD      C,$FE           
591E: 01 FF 00   LD      BC,$00FF        
5921: 69         LD      L,C             
5922: 00         NOP                     
5923: 34         INC     (HL)            
5924: 21 21 00   LD      HL,$0021        
5927: 00         NOP                     
5928: 00         NOP                     
5929: 44         LD      B,H             
592A: 00         NOP                     
592B: 20 00      JR      NZ,$592D        
592D: 08 00 00   LD      ($0000),SP      
5930: 10 5A      STOP    $5A             
5932: 00         NOP                     
5933: 0D         DEC     C               
5934: 00         NOP                     
5935: 80         ADD     A,B             
5936: 00         NOP                     
5937: 12         LD      (DE),A          
5938: 80         ADD     A,B             
5939: 80         ADD     A,B             
593A: 00         NOP                     
593B: 08 00 00   LD      ($0000),SP      
593E: 00         NOP                     
593F: 08 00 00   LD      ($0000),SP      
5942: 00         NOP                     
5943: 00         NOP                     
5944: 00         NOP                     
5945: 00         NOP                     
5946: 08 00 10   LD      ($1000),SP      
5949: 00         NOP                     
594A: 30 00      JR      NC,$594C        
594C: 50         LD      D,B             
594D: 20 4F      JR      NZ,$599E        
594F: 10 01      STOP    $01             
5951: 00         NOP                     
5952: 07         RLCA                    
5953: 00         NOP                     
5954: 0F         RRCA                    
5955: 03         INC     BC              
5956: 0C         INC     C               
5957: 04         INC     B               
5958: 3B         DEC     SP              
5959: 03         INC     BC              
595A: 7C         LD      A,H             
595B: 1F         RRA                     
595C: 63         LD      H,E             
595D: 3C         INC     A               
595E: DE 20      SBC     $20             
5960: FF         RST     0X38            
5961: 00         NOP                     
5962: FF         RST     0X38            
5963: FF         RST     0X38            
5964: FF         RST     0X38            
5965: FF         RST     0X38            
5966: FF         RST     0X38            
5967: FF         RST     0X38            
5968: FF         RST     0X38            
5969: FF         RST     0X38            
596A: 1F         RRA                     
596B: FF         RST     0X38            
596C: E0 1F      LDFF00  ($1F),A         
596E: 1F         RRA                     
596F: 20 07      JR      NZ,$5978        
5971: 00         NOP                     
5972: FF         RST     0X38            
5973: 00         NOP                     
5974: FF         RST     0X38            
5975: F0 3F      LD      A,($3F)         
5977: FD         ???                     
5978: CB C5      SET     1,E             
597A: C7         RST     0X00            
597B: F9         LD      SP,HL           
597C: 03         INC     BC              
597D: FD         ???                     
597E: 83         ADD     A,E             
597F: 01 E3 00   LD      BC,$00E3        
5982: FC         ???                     
5983: 80         ADD     A,B             
5984: FC         ???                     
5985: C0         RET     NZ              
5986: FC         ???                     
5987: C0         RET     NZ              
5988: 7F         LD      A,A             
5989: 60         LD      H,B             
598A: BF         CP      A               
598B: 60         LD      H,B             
598C: 9F         SBC     A               
598D: 70         LD      (HL),B          
598E: DF         RST     0X18            
598F: 30 0C      JR      NC,$599D        
5991: 00         NOP                     
5992: 04         INC     B               
5993: 00         NOP                     
5994: 06 00      LD      B,$00           
5996: 02         LD      (BC),A          
5997: 00         NOP                     
5998: A3         AND     E               
5999: 00         NOP                     
599A: C1         POP     BC              
599B: 00         NOP                     
599C: E1         POP     HL              
599D: 00         NOP                     
599E: FF         RST     0X38            
599F: 00         NOP                     
59A0: CC 13 7B   CALL    Z,$7B13         
59A3: 05         DEC     B               
59A4: 23         INC     HL              
59A5: 0D         DEC     C               
59A6: 17         RLA                     
59A7: 0B         DEC     BC              
59A8: 8F         ADC     A,A             
59A9: 03         INC     BC              
59AA: 84         ADD     A,H             
59AB: 03         INC     BC              
59AC: E7         RST     0X20            
59AD: 00         NOP                     
59AE: 79         LD      A,C             
59AF: 00         NOP                     
59B0: 0F         RRCA                    
59B1: FF         RST     0X38            
59B2: 03         INC     BC              
59B3: FF         RST     0X38            
59B4: 81         ADD     A,C             
59B5: FF         RST     0X38            
59B6: 0C         INC     C               
59B7: F3         DI                      
59B8: 08 F7 50   LD      ($50F7),SP      
59BB: AF         XOR     A               
59BC: 80         ADD     A,B             
59BD: 7F         LD      A,A             
59BE: E1         POP     HL              
59BF: 1E DC      LD      E,$DC           
59C1: 23         INC     HL              
59C2: 7A         LD      A,D             
59C3: 05         DEC     B               
59C4: 23         INC     HL              
59C5: 1D         DEC     E               
59C6: 17         RLA                     
59C7: 0B         DEC     BC              
59C8: 8F         ADC     A,A             
59C9: 03         INC     BC              
59CA: 84         ADD     A,H             
59CB: 03         INC     BC              
59CC: E7         RST     0X20            
59CD: 00         NOP                     
59CE: 79         LD      A,C             
59CF: 00         NOP                     
59D0: 00         NOP                     
59D1: C0         RET     NZ              
59D2: 00         NOP                     
59D3: 0C         INC     C               
59D4: 00         NOP                     
59D5: 03         INC     BC              
59D6: 00         NOP                     
59D7: 00         NOP                     
59D8: 00         NOP                     
59D9: 30 00      JR      NC,$59DB        
59DB: EC         ???                     
59DC: 00         NOP                     
59DD: 36 60      LD      (HL),$60        
59DF: F8 FC      LDHL    SP,$FC          
59E1: 0B         DEC     BC              
59E2: 7A         LD      A,D             
59E3: 05         DEC     B               
59E4: 23         INC     HL              
59E5: 1D         DEC     E               
59E6: 17         RLA                     
59E7: 0B         DEC     BC              
59E8: 8F         ADC     A,A             
59E9: 03         INC     BC              
59EA: 84         ADD     A,H             
59EB: 03         INC     BC              
59EC: E7         RST     0X20            
59ED: 00         NOP                     
59EE: 79         LD      A,C             
59EF: 00         NOP                     
59F0: 00         NOP                     
59F1: 00         NOP                     
59F2: 00         NOP                     
59F3: 00         NOP                     
59F4: 00         NOP                     
59F5: 00         NOP                     
59F6: 00         NOP                     
59F7: 80         ADD     A,B             
59F8: 00         NOP                     
59F9: 00         NOP                     
59FA: 00         NOP                     
59FB: 90         SUB     B               
59FC: 00         NOP                     
59FD: 48         LD      C,B             
59FE: 00         NOP                     
59FF: 20 00      JR      NZ,$5A01        
5A01: FF         RST     0X38            
5A02: 7C         LD      A,H             
5A03: FF         RST     0X38            
5A04: FF         RST     0X38            
5A05: FF         RST     0X38            
5A06: FF         RST     0X38            
5A07: FF         RST     0X38            
5A08: DF         RST     0X18            
5A09: FF         RST     0X38            
5A0A: 07         RLCA                    
5A0B: FF         RST     0X38            
5A0C: 01 FF 00   LD      BC,$00FF        
5A0F: FF         RST     0X38            
5A10: 61         LD      H,C             
5A11: FF         RST     0X38            
5A12: E7         RST     0X20            
5A13: FF         RST     0X38            
5A14: FC         ???                     
5A15: FF         RST     0X38            
5A16: FC         ???                     
5A17: FF         RST     0X38            
5A18: BF         CP      A               
5A19: FF         RST     0X38            
5A1A: 8F         ADC     A,A             
5A1B: FF         RST     0X38            
5A1C: 86         ADD     A,(HL)          
5A1D: FF         RST     0X38            
5A1E: 82         ADD     A,D             
5A1F: FF         RST     0X38            
5A20: 00         NOP                     
5A21: 01 00 03   LD      BC,$0300        
5A24: 00         NOP                     
5A25: 21 00 47   LD      HL,$4700        
5A28: 00         NOP                     
5A29: 4B         LD      C,E             
5A2A: 00         NOP                     
5A2B: 0F         RRCA                    
5A2C: 02         LD      (BC),A          
5A2D: 07         RLCA                    
5A2E: 02         LD      (BC),A          
5A2F: 83         ADD     A,E             
5A30: 02         LD      (BC),A          
5A31: DF         RST     0X18            
5A32: 0D         DEC     C               
5A33: BF         CP      A               
5A34: 10 7F      STOP    $7F             
5A36: 4B         LD      C,E             
5A37: FF         RST     0X38            
5A38: 9F         SBC     A               
5A39: FF         RST     0X38            
5A3A: 9F         SBC     A               
5A3B: FF         RST     0X38            
5A3C: 1F         RRA                     
5A3D: FF         RST     0X38            
5A3E: BF         CP      A               
5A3F: FF         RST     0X38            
5A40: 43         LD      B,E             
5A41: 1C         INC     E               
5A42: 20 0F      JR      NZ,$5A53        
5A44: 10 01      STOP    $01             
5A46: 1C         INC     E               
5A47: 03         INC     BC              
5A48: 10 0F      STOP    $0F             
5A4A: 20 1F      JR      NZ,$5A6B        
5A4C: 40         LD      B,B             
5A4D: 3F         CCF                     
5A4E: 40         LD      B,B             
5A4F: 3F         CCF                     
5A50: E0 03      LDFF00  ($03),A         
5A52: 00         NOP                     
5A53: FF         RST     0X38            
5A54: 00         NOP                     
5A55: FF         RST     0X38            
5A56: 00         NOP                     
5A57: FF         RST     0X38            
5A58: 00         NOP                     
5A59: FF         RST     0X38            
5A5A: 00         NOP                     
5A5B: FF         RST     0X38            
5A5C: 00         NOP                     
5A5D: FF         RST     0X38            
5A5E: 00         NOP                     
5A5F: FF         RST     0X38            
5A60: 04         INC     B               
5A61: F8 02      LDHL    SP,$02          
5A63: FC         ???                     
5A64: 03         INC     BC              
5A65: FC         ???                     
5A66: 23         INC     HL              
5A67: DC 12 ED   CALL    C,$ED12         
5A6A: 12         LD      (DE),A          
5A6B: E9         JP      (HL)            
5A6C: 17         RLA                     
5A6D: E3         ???                     
5A6E: 37         SCF                     
5A6F: C2 7D 00   JP      NZ,$007D        
5A72: 01 FC 03   LD      BC,$03FC        
5A75: 7C         LD      A,H             
5A76: 00         NOP                     
5A77: 1C         INC     E               
5A78: 80         ADD     A,B             
5A79: 00         NOP                     
5A7A: 40         LD      B,B             
5A7B: 80         ADD     A,B             
5A7C: BB         CP      E               
5A7D: 00         NOP                     
5A7E: 44         LD      B,H             
5A7F: 39         ADD     HL,SP           
5A80: FF         RST     0X38            
5A81: 90         SUB     B               
5A82: DD         ???                     
5A83: AA         XOR     D               
5A84: CC AB 8D   CALL    Z,$8DAB         
5A87: 2A         LD      A,(HLI)         
5A88: 8E         ADC     A,(HL)          
5A89: 2C         INC     L               
5A8A: 8E         ADC     A,(HL)          
5A8B: 3C         INC     A               
5A8C: 8E         ADC     A,(HL)          
5A8D: 7C         LD      A,H             
5A8E: 5E         LD      E,(HL)          
5A8F: BC         CP      H               
5A90: FF         RST     0X38            
5A91: 00         NOP                     
5A92: C1         POP     BC              
5A93: 00         NOP                     
5A94: 80         ADD     A,B             
5A95: 00         NOP                     
5A96: 00         NOP                     
5A97: 00         NOP                     
5A98: 04         INC     B               
5A99: 00         NOP                     
5A9A: 09         ADD     HL,BC           
5A9B: 00         NOP                     
5A9C: 12         LD      (DE),A          
5A9D: 01 16 01   LD      BC,$0116        
5AA0: 00         NOP                     
5AA1: 00         NOP                     
5AA2: F0 00      LD      A,($00)         
5AA4: 0E 00      LD      C,$00           
5AA6: 3F         CCF                     
5AA7: 00         NOP                     
5AA8: C1         POP     BC              
5AA9: 3E 00      LD      A,$00           
5AAB: FF         RST     0X38            
5AAC: 00         NOP                     
5AAD: FF         RST     0X38            
5AAE: 00         NOP                     
5AAF: FF         RST     0X38            
5AB0: 00         NOP                     
5AB1: 00         NOP                     
5AB2: 00         NOP                     
5AB3: 00         NOP                     
5AB4: 00         NOP                     
5AB5: 00         NOP                     
5AB6: 80         ADD     A,B             
5AB7: 00         NOP                     
5AB8: C0         RET     NZ              
5AB9: 00         NOP                     
5ABA: 60         LD      H,B             
5ABB: 80         ADD     A,B             
5ABC: 10 C0      STOP    $C0             
5ABE: 0C         INC     C               
5ABF: E0 00      LDFF00  ($00),A         
5AC1: 00         NOP                     
5AC2: 00         NOP                     
5AC3: 00         NOP                     
5AC4: 00         NOP                     
5AC5: 00         NOP                     
5AC6: 00         NOP                     
5AC7: 00         NOP                     
5AC8: 00         NOP                     
5AC9: 00         NOP                     
5ACA: 00         NOP                     
5ACB: 00         NOP                     
5ACC: 00         NOP                     
5ACD: 00         NOP                     
5ACE: 00         NOP                     
5ACF: 00         NOP                     
5AD0: FF         RST     0X38            
5AD1: 00         NOP                     
5AD2: FF         RST     0X38            
5AD3: 00         NOP                     
5AD4: FF         RST     0X38            
5AD5: 00         NOP                     
5AD6: FF         RST     0X38            
5AD7: 00         NOP                     
5AD8: FF         RST     0X38            
5AD9: 00         NOP                     
5ADA: FF         RST     0X38            
5ADB: 00         NOP                     
5ADC: FF         RST     0X38            
5ADD: 00         NOP                     
5ADE: FF         RST     0X38            
5ADF: 00         NOP                     
5AE0: 00         NOP                     
5AE1: FF         RST     0X38            
5AE2: 00         NOP                     
5AE3: FF         RST     0X38            
5AE4: 00         NOP                     
5AE5: FF         RST     0X38            
5AE6: 00         NOP                     
5AE7: FF         RST     0X38            
5AE8: 00         NOP                     
5AE9: FF         RST     0X38            
5AEA: 00         NOP                     
5AEB: FF         RST     0X38            
5AEC: 00         NOP                     
5AED: FF         RST     0X38            
5AEE: 00         NOP                     
5AEF: FF         RST     0X38            
5AF0: FF         RST     0X38            
5AF1: FF         RST     0X38            
5AF2: FF         RST     0X38            
5AF3: FF         RST     0X38            
5AF4: FF         RST     0X38            
5AF5: FF         RST     0X38            
5AF6: FF         RST     0X38            
5AF7: FF         RST     0X38            
5AF8: FF         RST     0X38            
5AF9: FF         RST     0X38            
5AFA: FF         RST     0X38            
5AFB: FF         RST     0X38            
5AFC: FF         RST     0X38            
5AFD: FF         RST     0X38            
5AFE: FF         RST     0X38            
5AFF: FF         RST     0X38            
5B00: 00         NOP                     
5B01: FF         RST     0X38            
5B02: 07         RLCA                    
5B03: FF         RST     0X38            
5B04: 0F         RRCA                    
5B05: FF         RST     0X38            
5B06: 1F         RRA                     
5B07: FF         RST     0X38            
5B08: 30 FF      JR      NC,$5B09        
5B0A: 00         NOP                     
5B0B: FF         RST     0X38            
5B0C: 00         NOP                     
5B0D: FF         RST     0X38            
5B0E: 00         NOP                     
5B0F: FF         RST     0X38            
5B10: 00         NOP                     
5B11: FF         RST     0X38            
5B12: 80         ADD     A,B             
5B13: FF         RST     0X38            
5B14: E0 FF      LDFF00  ($FF),A         
5B16: F3         DI                      
5B17: FF         RST     0X38            
5B18: 1F         RRA                     
5B19: FF         RST     0X38            
5B1A: 0C         INC     C               
5B1B: FF         RST     0X38            
5B1C: 10 FF      STOP    $FF             
5B1E: 00         NOP                     
5B1F: FF         RST     0X38            
5B20: 00         NOP                     
5B21: 00         NOP                     
5B22: 00         NOP                     
5B23: 00         NOP                     
5B24: 00         NOP                     
5B25: 00         NOP                     
5B26: 00         NOP                     
5B27: 00         NOP                     
5B28: 00         NOP                     
5B29: 00         NOP                     
5B2A: 00         NOP                     
5B2B: 00         NOP                     
5B2C: 07         RLCA                    
5B2D: 00         NOP                     
5B2E: 07         RLCA                    
5B2F: 01 00 00   LD      BC,$0000        
5B32: 00         NOP                     
5B33: 00         NOP                     
5B34: 00         NOP                     
5B35: 00         NOP                     
5B36: 00         NOP                     
5B37: 00         NOP                     
5B38: 00         NOP                     
5B39: 00         NOP                     
5B3A: 01 00 8F   LD      BC,$8F00        
5B3D: 01 CE 87   LD      BC,$87CE        
5B40: 88         ADC     A,B             
5B41: 17         RLA                     
5B42: 90         SUB     B               
5B43: 0F         RRCA                    
5B44: A0         AND     B               
5B45: 07         RLCA                    
5B46: A0         AND     B               
5B47: 07         RLCA                    
5B48: C0         RET     NZ              
5B49: 00         NOP                     
5B4A: C0         RET     NZ              
5B4B: 00         NOP                     
5B4C: C0         RET     NZ              
5B4D: 00         NOP                     
5B4E: C0         RET     NZ              
5B4F: 00         NOP                     
5B50: 01 FE 02   LD      BC,$02FE        
5B53: FD         ???                     
5B54: 02         LD      (BC),A          
5B55: E1         POP     HL              
5B56: 04         INC     B               
5B57: 00         NOP                     
5B58: 04         INC     B               
5B59: 00         NOP                     
5B5A: 05         DEC     B               
5B5B: 00         NOP                     
5B5C: 07         RLCA                    
5B5D: 00         NOP                     
5B5E: 09         ADD     HL,BC           
5B5F: 00         NOP                     
5B60: 37         SCF                     
5B61: C0         RET     NZ              
5B62: 5B         LD      E,E             
5B63: A4         AND     H               
5B64: 52         LD      D,D             
5B65: 2D         DEC     L               
5B66: 86         ADD     A,(HL)          
5B67: 79         LD      A,C             
5B68: 84         ADD     A,H             
5B69: 7B         LD      A,E             
5B6A: C4 3B A0   CALL    NZ,$A03B        
5B6D: 5F         LD      E,A             
5B6E: 88         ADC     A,B             
5B6F: 77         LD      (HL),A          
5B70: F2         ???                     
5B71: 7C         LD      A,H             
5B72: FD         ???                     
5B73: FE 7F      CP      $7F             
5B75: F7         RST     0X30            
5B76: 0F         RRCA                    
5B77: F7         RST     0X30            
5B78: 1F         RRA                     
5B79: E7         RST     0X20            
5B7A: 7F         LD      A,A             
5B7B: 8F         ADC     A,A             
5B7C: 1F         RRA                     
5B7D: FF         RST     0X38            
5B7E: 0F         RRCA                    
5B7F: FF         RST     0X38            
5B80: 3C         INC     A               
5B81: C8         RET     Z               
5B82: 0E 70      LD      C,$70           
5B84: 87         ADD     A,A             
5B85: 38 83      JR      C,$5B0A         
5B87: 3C         INC     A               
5B88: 43         LD      B,E             
5B89: 9C         SBC     H               
5B8A: 41         LD      B,C             
5B8B: 9E         SBC     (HL)            
5B8C: 41         LD      B,C             
5B8D: 9E         SBC     (HL)            
5B8E: 41         LD      B,C             
5B8F: 96         SUB     (HL)            
5B90: 1C         INC     E               
5B91: 03         INC     BC              
5B92: 3C         INC     A               
5B93: 03         INC     BC              
5B94: FC         ???                     
5B95: 01 FC 00   LD      BC,$00FC        
5B98: FC         ???                     
5B99: 00         NOP                     
5B9A: FE 00      CP      $00             
5B9C: E7         RST     0X20            
5B9D: 0E D7      LD      C,$D7           
5B9F: 0E 10      LD      C,$10           
5BA1: EF         RST     0X28            
5BA2: 20 DF      JR      NZ,$5B83        
5BA4: 5C         LD      E,H             
5BA5: 83         ADD     A,E             
5BA6: 60         LD      H,B             
5BA7: 1F         RRA                     
5BA8: 40         LD      B,B             
5BA9: 3F         CCF                     
5BAA: 80         ADD     A,B             
5BAB: 7F         LD      A,A             
5BAC: 80         ADD     A,B             
5BAD: 7F         LD      A,A             
5BAE: E0 9E      LDFF00  ($9E),A         
5BB0: 06 E0      LD      B,$E0           
5BB2: 02         LD      (BC),A          
5BB3: E0 03      LDFF00  ($03),A         
5BB5: E0 01      LDFF00  ($01),A         
5BB7: C0         RET     NZ              
5BB8: 01 C0 01   LD      BC,$01C0        
5BBB: 80         ADD     A,B             
5BBC: 01 00 03   LD      BC,$0300        
5BBF: 00         NOP                     
5BC0: 00         NOP                     
5BC1: 00         NOP                     
5BC2: 00         NOP                     
5BC3: 00         NOP                     
5BC4: 00         NOP                     
5BC5: 00         NOP                     
5BC6: 80         ADD     A,B             
5BC7: 00         NOP                     
5BC8: 40         LD      B,B             
5BC9: 00         NOP                     
5BCA: 60         LD      H,B             
5BCB: 00         NOP                     
5BCC: A0         AND     B               
5BCD: 00         NOP                     
5BCE: F0 00      LD      A,($00)         
5BD0: 00         NOP                     
5BD1: 00         NOP                     
5BD2: 00         NOP                     
5BD3: 00         NOP                     
5BD4: 00         NOP                     
5BD5: 00         NOP                     
5BD6: 00         NOP                     
5BD7: 00         NOP                     
5BD8: 00         NOP                     
5BD9: 00         NOP                     
5BDA: 00         NOP                     
5BDB: 00         NOP                     
5BDC: 03         INC     BC              
5BDD: 00         NOP                     
5BDE: 0F         RRCA                    
5BDF: 01 00 00   LD      BC,$0000        
5BE2: 00         NOP                     
5BE3: 00         NOP                     
5BE4: 00         NOP                     
5BE5: 00         NOP                     
5BE6: 00         NOP                     
5BE7: 00         NOP                     
5BE8: 00         NOP                     
5BE9: 00         NOP                     
5BEA: 78         LD      A,B             
5BEB: 00         NOP                     
5BEC: FE 68      CP      $68             
5BEE: CB F4      SET     1,E             
5BF0: 14         INC     D               
5BF1: FE A2      CP      $A2             
5BF3: FF         RST     0X38            
5BF4: 09         ADD     HL,BC           
5BF5: FF         RST     0X38            
5BF6: F4         ???                     
5BF7: FF         RST     0X38            
5BF8: F9         LD      SP,HL           
5BF9: FF         RST     0X38            
5BFA: FA FF FE   LD      A,($FEFF)       
5BFD: FF         RST     0X38            
5BFE: FC         ???                     
5BFF: FF         RST     0X38            
5C00: 03         INC     BC              
5C01: 00         NOP                     
5C02: 02         LD      (BC),A          
5C03: 01 0D 03   LD      BC,$030D        
5C06: 1F         RRA                     
5C07: 07         RLCA                    
5C08: 17         RLA                     
5C09: 0F         RRCA                    
5C0A: 20 19      JR      NZ,$5C25        
5C0C: 30 01      JR      NC,$5C0F        
5C0E: 18 07      JR      $5C17           
5C10: FF         RST     0X38            
5C11: 00         NOP                     
5C12: 1E E1      LD      E,$E1           
5C14: F0 FF      LD      A,($FF)         
5C16: 82         ADD     A,D             
5C17: FF         RST     0X38            
5C18: FF         RST     0X38            
5C19: FF         RST     0X38            
5C1A: FE FE      CP      $FE             
5C1C: 03         INC     BC              
5C1D: FF         RST     0X38            
5C1E: 00         NOP                     
5C1F: 0F         RRCA                    
5C20: FF         RST     0X38            
5C21: 06 3D      LD      B,$3D           
5C23: C6 BF      ADD     $BF             
5C25: D8         RET     C               
5C26: 7E         LD      A,(HL)          
5C27: D8         RET     C               
5C28: FD         ???                     
5C29: CB 7D      SET     1,E             
5C2B: 93         SUB     E               
5C2C: 6C         LD      L,H             
5C2D: B1         OR      C               
5C2E: 48         LD      C,B             
5C2F: B3         OR      E               
5C30: FD         ???                     
5C31: 06 1B      LD      B,$1B           
5C33: EC         ???                     
5C34: F3         DI                      
5C35: EC         ???                     
5C36: 8D         ADC     A,L             
5C37: F0 F0      LD      A,($F0)         
5C39: F2         ???                     
5C3A: FE FE      CP      $FE             
5C3C: 03         INC     BC              
5C3D: FF         RST     0X38            
5C3E: 00         NOP                     
5C3F: 0F         RRCA                    
5C40: C0         RET     NZ              
5C41: 80         ADD     A,B             
5C42: E0 80      LDFF00  ($80),A         
5C44: 61         LD      H,C             
5C45: 80         ADD     A,B             
5C46: 51         LD      D,C             
5C47: A0         AND     B               
5C48: F8 00      LDHL    SP,$00          
5C4A: 6C         LD      L,H             
5C4B: 88         ADC     A,B             
5C4C: 03         INC     BC              
5C4D: FC         ???                     
5C4E: 00         NOP                     
5C4F: 3F         CCF                     
5C50: 0F         RRCA                    
5C51: 00         NOP                     
5C52: 0F         RRCA                    
5C53: 00         NOP                     
5C54: 0F         RRCA                    
5C55: 00         NOP                     
5C56: 0F         RRCA                    
5C57: 00         NOP                     
5C58: 87         ADD     A,A             
5C59: 00         NOP                     
5C5A: 47         LD      B,A             
5C5B: 00         NOP                     
5C5C: 33         INC     SP              
5C5D: 00         NOP                     
5C5E: EB         ???                     
5C5F: 10 CC      STOP    $CC             
5C61: 33         INC     SP              
5C62: 7A         LD      A,D             
5C63: 05         DEC     B               
5C64: 23         INC     HL              
5C65: 1D         DEC     E               
5C66: 17         RLA                     
5C67: 0B         DEC     BC              
5C68: 8F         ADC     A,A             
5C69: 03         INC     BC              
5C6A: 84         ADD     A,H             
5C6B: 03         INC     BC              
5C6C: E7         RST     0X20            
5C6D: 00         NOP                     
5C6E: 79         LD      A,C             
5C6F: 00         NOP                     
5C70: 0F         RRCA                    
5C71: FF         RST     0X38            
5C72: 07         RLCA                    
5C73: FF         RST     0X38            
5C74: 81         ADD     A,C             
5C75: FF         RST     0X38            
5C76: 84         ADD     A,H             
5C77: FB         EI                      
5C78: 08 F7 50   LD      ($50F7),SP      
5C7B: AF         XOR     A               
5C7C: 80         ADD     A,B             
5C7D: 7F         LD      A,A             
5C7E: E1         POP     HL              
5C7F: 1E A9      LD      E,$A9           
5C81: C6 A9      ADD     $A9             
5C83: C2 A9 C0   JP      NZ,$C0A9        
5C86: 39         ADD     HL,SP           
5C87: C0         RET     NZ              
5C88: 53         LD      D,E             
5C89: A0         AND     B               
5C8A: 53         LD      D,E             
5C8B: A0         AND     B               
5C8C: 8B         ADC     A,E             
5C8D: 50         LD      D,B             
5C8E: 0B         DEC     BC              
5C8F: 10 F9      STOP    $F9             
5C91: 06 27      LD      B,$27           
5C93: C0         RET     NZ              
5C94: 09         ADD     HL,BC           
5C95: E0 B0      LDFF00  ($B0),A         
5C97: 6E         LD      L,(HL)          
5C98: F0 6F      LD      A,($6F)         
5C9A: 20 1F      JR      NZ,$5CBB        
5C9C: 40         LD      B,B             
5C9D: 3F         CCF                     
5C9E: 48         LD      C,B             
5C9F: 37         SCF                     
5CA0: F0 EC      LD      A,($EC)         
5CA2: 78         LD      A,B             
5CA3: F0 9C      LD      A,($9C)         
5CA5: 70         LD      (HL),B          
5CA6: 5E         LD      E,(HL)          
5CA7: 2C         INC     L               
5CA8: 3A         LD      A,(HLD)         
5CA9: 0C         INC     C               
5CAA: 31 8A 31   LD      SP,$318A        
5CAD: 80         ADD     A,B             
5CAE: 3B         DEC     SP              
5CAF: 81         ADD     A,C             
5CB0: 07         RLCA                    
5CB1: 00         NOP                     
5CB2: 0C         INC     C               
5CB3: 00         NOP                     
5CB4: 0E 00      LD      C,$00           
5CB6: 18 02      JR      $5CBA           
5CB8: 31 07 23   LD      SP,$2307        
5CBB: 0F         RRCA                    
5CBC: E0 07      LDFF00  ($07),A         
5CBE: C0         RET     NZ              
5CBF: 0F         RRCA                    
5CC0: FF         RST     0X38            
5CC1: 00         NOP                     
5CC2: 78         LD      A,B             
5CC3: 87         ADD     A,A             
5CC4: 01 FF 7F   LD      BC,$7FFF        
5CC7: FE FB      CP      $FB             
5CC9: FD         ???                     
5CCA: 7C         LD      A,H             
5CCB: 7B         LD      A,E             
5CCC: C4 FA 07   CALL    NZ,$07FA        
5CCF: F0 FF      LD      A,($FF)         
5CD1: 0E 79      LD      C,$79           
5CD3: 9E         SBC     (HL)            
5CD4: F3         DI                      
5CD5: 3C         INC     A               
5CD6: F4         ???                     
5CD7: C8         RET     Z               
5CD8: 18 E3      JR      $5CBD           
5CDA: 33         INC     SP              
5CDB: 87         ADD     A,A             
5CDC: 60         LD      H,B             
5CDD: 07         RLCA                    
5CDE: C0         RET     NZ              
5CDF: 0F         RRCA                    
5CE0: 3F         CCF                     
5CE1: C0         RET     NZ              
5CE2: C7         RST     0X00            
5CE3: 18 1E      JR      $5D03           
5CE5: 7F         LD      A,A             
5CE6: 01 FE FF   LD      BC,$FFFE        
5CE9: FC         ???                     
5CEA: 7F         LD      A,A             
5CEB: F8 73      LDHL    SP,$73          
5CED: F8 07      LDHL    SP,$07          
5CEF: F9         LD      SP,HL           
5CF0: FF         RST     0X38            
5CF1: 00         NOP                     
5CF2: C3 3C BF   JP      $BF3C           
5CF5: 42         LD      B,D             
5CF6: EE 1C      XOR     $1C             
5CF8: 4C         LD      C,H             
5CF9: 70         LD      (HL),B          
5CFA: 04         INC     B               
5CFB: 00         NOP                     
5CFC: 18 20      JR      $5D1E           
5CFE: F8 F0      LDHL    SP,$F0          
5D00: 70         LD      (HL),B          
5D01: 0F         RRCA                    
5D02: 40         LD      B,B             
5D03: 30 80      JR      NC,$5C85        
5D05: 40         LD      B,B             
5D06: C0         RET     NZ              
5D07: 00         NOP                     
5D08: 67         LD      H,A             
5D09: 00         NOP                     
5D0A: F7         RST     0X30            
5D0B: 00         NOP                     
5D0C: 7F         LD      A,A             
5D0D: 00         NOP                     
5D0E: 3C         INC     A               
5D0F: 00         NOP                     
5D10: 00         NOP                     
5D11: FC         ???                     
5D12: 00         NOP                     
5D13: 0E 03      LD      C,$03           
5D15: 00         NOP                     
5D16: 1E 00      LD      E,$00           
5D18: C0         RET     NZ              
5D19: 00         NOP                     
5D1A: FF         RST     0X38            
5D1B: 00         NOP                     
5D1C: F8 07      LDHL    SP,$07          
5D1E: 00         NOP                     
5D1F: 3F         CCF                     
5D20: 6C         LD      L,H             
5D21: 80         ADD     A,B             
5D22: DC 20 9C   CALL    C,$9C20         
5D25: 60         LD      H,B             
5D26: 98         SBC     B               
5D27: 40         LD      B,B             
5D28: CC 00 9F   CALL    Z,$9F00         
5D2B: 00         NOP                     
5D2C: FF         RST     0X38            
5D2D: 00         NOP                     
5D2E: 00         NOP                     
5D2F: 0F         RRCA                    
5D30: 00         NOP                     
5D31: 3F         CCF                     
5D32: 00         NOP                     
5D33: 70         LD      (HL),B          
5D34: C0         RET     NZ              
5D35: 00         NOP                     
5D36: 78         LD      A,B             
5D37: 00         NOP                     
5D38: 03         INC     BC              
5D39: 00         NOP                     
5D3A: FF         RST     0X38            
5D3B: 00         NOP                     
5D3C: 1F         RRA                     
5D3D: E0 00      LDFF00  ($00),A         
5D3F: F8 00      LDHL    SP,$00          
5D41: 3F         CCF                     
5D42: 00         NOP                     
5D43: 70         LD      (HL),B          
5D44: C0         RET     NZ              
5D45: 00         NOP                     
5D46: 78         LD      A,B             
5D47: 00         NOP                     
5D48: 03         INC     BC              
5D49: 00         NOP                     
5D4A: FF         RST     0X38            
5D4B: 00         NOP                     
5D4C: 1F         RRA                     
5D4D: E0 00      LDFF00  ($00),A         
5D4F: 0F         RRCA                    
5D50: 1F         RRA                     
5D51: E0 E7      LDFF00  ($E7),A         
5D53: 00         NOP                     
5D54: 7F         LD      A,A             
5D55: 00         NOP                     
5D56: 06 F8      LD      B,$F8           
5D58: FF         RST     0X38            
5D59: 00         NOP                     
5D5A: FF         RST     0X38            
5D5B: 00         NOP                     
5D5C: FF         RST     0X38            
5D5D: 00         NOP                     
5D5E: 00         NOP                     
5D5F: F8 FC      LDHL    SP,$FC          
5D61: 00         NOP                     
5D62: 8E         ADC     A,(HL)          
5D63: 00         NOP                     
5D64: FF         RST     0X38            
5D65: 00         NOP                     
5D66: 07         RLCA                    
5D67: 00         NOP                     
5D68: FF         RST     0X38            
5D69: 00         NOP                     
5D6A: FF         RST     0X38            
5D6B: 00         NOP                     
5D6C: 1F         RRA                     
5D6D: E0 00      LDFF00  ($00),A         
5D6F: 0F         RRCA                    
5D70: BF         CP      A               
5D71: 00         NOP                     
5D72: FF         RST     0X38            
5D73: 00         NOP                     
5D74: F7         RST     0X30            
5D75: 00         NOP                     
5D76: 04         INC     B               
5D77: 00         NOP                     
5D78: FF         RST     0X38            
5D79: 00         NOP                     
5D7A: FF         RST     0X38            
5D7B: 00         NOP                     
5D7C: FF         RST     0X38            
5D7D: 00         NOP                     
5D7E: 00         NOP                     
5D7F: F8 CA      LDHL    SP,$CA          
5D81: 10 8C      STOP    $8C             
5D83: 00         NOP                     
5D84: DF         RST     0X18            
5D85: 00         NOP                     
5D86: FF         RST     0X38            
5D87: 00         NOP                     
5D88: 1B         DEC     DE              
5D89: 00         NOP                     
5D8A: FE 01      CP      $01             
5D8C: 1F         RRA                     
5D8D: E1         POP     HL              
5D8E: 0F         RRCA                    
5D8F: 00         NOP                     
5D90: 98         SBC     B               
5D91: 67         LD      H,A             
5D92: 30 CE      JR      NC,$5D62        
5D94: 70         LD      (HL),B          
5D95: 8E         ADC     A,(HL)          
5D96: D3         ???                     
5D97: 2C         INC     L               
5D98: 1A         LD      A,(DE)          
5D99: E4         ???                     
5D9A: 1D         DEC     E               
5D9B: E0 FB      LDFF00  ($FB),A         
5D9D: F4         ???                     
5D9E: FF         RST     0X38            
5D9F: 00         NOP                     
5DA0: 1A         LD      A,(DE)          
5DA1: 01 5E 81   LD      BC,$815E        
5DA4: 8C         ADC     A,H             
5DA5: 00         NOP                     
5DA6: 8E         ADC     A,(HL)          
5DA7: 00         NOP                     
5DA8: 8F         ADC     A,A             
5DA9: 00         NOP                     
5DAA: 9F         SBC     A               
5DAB: 00         NOP                     
5DAC: BF         CP      A               
5DAD: 00         NOP                     
5DAE: 80         ADD     A,B             
5DAF: 7F         LD      A,A             
5DB0: 80         ADD     A,B             
5DB1: 10 40      STOP    $40             
5DB3: 80         ADD     A,B             
5DB4: 60         LD      H,B             
5DB5: 08 F0 68   LD      ($68F0),SP      
5DB8: BC         CP      H               
5DB9: 60         LD      H,B             
5DBA: 09         ADD     HL,BC           
5DBB: 30 AF      JR      NC,$5D6C        
5DBD: 10 F8      STOP    $F8             
5DBF: 00         NOP                     
5DC0: 0C         INC     C               
5DC1: 26 19      LD      H,$19           
5DC3: 4C         LD      C,H             
5DC4: 91         SUB     C               
5DC5: 08 27 00   LD      ($0027),SP      
5DC8: 3F         CCF                     
5DC9: 04         INC     B               
5DCA: 33         INC     SP              
5DCB: 08 23 C0   LD      ($C023),SP      
5DCE: 3E 01      LD      A,$01           
5DD0: E0 07      LDFF00  ($07),A         
5DD2: E0 00      LDFF00  ($00),A         
5DD4: C0         RET     NZ              
5DD5: 08 C0 18   LD      ($18C0),SP      
5DD8: FC         ???                     
5DD9: 00         NOP                     
5DDA: B9         CP      C               
5DDB: 00         NOP                     
5DDC: FF         RST     0X38            
5DDD: 00         NOP                     
5DDE: 00         NOP                     
5DDF: F8 03      LDHL    SP,$03          
5DE1: 70         LD      (HL),B          
5DE2: 00         NOP                     
5DE3: 00         NOP                     
5DE4: 00         NOP                     
5DE5: EE 03      XOR     $03             
5DE7: 00         NOP                     
5DE8: 02         LD      (BC),A          
5DE9: 00         NOP                     
5DEA: 3C         INC     A               
5DEB: 00         NOP                     
5DEC: F4         ???                     
5DED: 00         NOP                     
5DEE: 00         NOP                     
5DEF: 83         ADD     A,E             
5DF0: FC         ???                     
5DF1: F8 FE      LDHL    SP,$FE          
5DF3: 3C         INC     A               
5DF4: E3         ???                     
5DF5: 7A         LD      A,D             
5DF6: 27         DAA                     
5DF7: 60         LD      H,B             
5DF8: 08 00 10   LD      ($1000),SP      
5DFB: 00         NOP                     
5DFC: FC         ???                     
5DFD: 00         NOP                     
5DFE: 7E         LD      A,(HL)          
5DFF: 80         ADD     A,B             
5E00: 1F         RRA                     
5E01: 00         NOP                     
5E02: 07         RLCA                    
5E03: 00         NOP                     
5E04: 00         NOP                     
5E05: 00         NOP                     
5E06: 00         NOP                     
5E07: 00         NOP                     
5E08: 00         NOP                     
5E09: 00         NOP                     
5E0A: 00         NOP                     
5E0B: 00         NOP                     
5E0C: 00         NOP                     
5E0D: 00         NOP                     
5E0E: 00         NOP                     
5E0F: 00         NOP                     
5E10: E0 E0      LDFF00  ($E0),A         
5E12: F0 F0      LD      A,($F0)         
5E14: 7F         LD      A,A             
5E15: FF         RST     0X38            
5E16: 7F         LD      A,A             
5E17: FF         RST     0X38            
5E18: 19         ADD     HL,DE           
5E19: FF         RST     0X38            
5E1A: 7F         LD      A,A             
5E1B: FF         RST     0X38            
5E1C: 9F         SBC     A               
5E1D: FF         RST     0X38            
5E1E: CF         RST     0X08            
5E1F: FF         RST     0X38            
5E20: 00         NOP                     
5E21: 00         NOP                     
5E22: 00         NOP                     
5E23: 00         NOP                     
5E24: 00         NOP                     
5E25: 00         NOP                     
5E26: C0         RET     NZ              
5E27: C0         RET     NZ              
5E28: E0 E0      LDFF00  ($E0),A         
5E2A: E0 E0      LDFF00  ($E0),A         
5E2C: F0 F0      LD      A,($F0)         
5E2E: F0 F0      LD      A,($F0)         
5E30: 00         NOP                     
5E31: 00         NOP                     
5E32: 00         NOP                     
5E33: 00         NOP                     
5E34: 00         NOP                     
5E35: 00         NOP                     
5E36: 01 01 07   LD      BC,$0701        
5E39: 07         RLCA                    
5E3A: 0F         RRCA                    
5E3B: 0F         RRCA                    
5E3C: 1F         RRA                     
5E3D: 1F         RRA                     
5E3E: 1C         INC     E               
5E3F: 1F         RRA                     
5E40: 0F         RRCA                    
5E41: 0F         RRCA                    
5E42: 1F         RRA                     
5E43: 1F         RRA                     
5E44: 3E 3F      LD      A,$3F           
5E46: F8 FF      LDHL    SP,$FF          
5E48: F0 FF      LD      A,($FF)         
5E4A: FE FF      CP      $FF             
5E4C: EF         RST     0X28            
5E4D: FF         RST     0X38            
5E4E: 1E FF      LD      E,$FF           
5E50: 00         NOP                     
5E51: 00         NOP                     
5E52: 00         NOP                     
5E53: 00         NOP                     
5E54: 00         NOP                     
5E55: 00         NOP                     
5E56: 01 01 07   LD      BC,$0701        
5E59: 07         RLCA                    
5E5A: 0F         RRCA                    
5E5B: 0F         RRCA                    
5E5C: 1F         RRA                     
5E5D: 1F         RRA                     
5E5E: 1F         RRA                     
5E5F: 1F         RRA                     
5E60: 0F         RRCA                    
5E61: 0F         RRCA                    
5E62: 1F         RRA                     
5E63: 1F         RRA                     
5E64: 1C         INC     E               
5E65: 1F         RRA                     
5E66: D8         RET     C               
5E67: DF         RST     0X18            
5E68: F0 FF      LD      A,($FF)         
5E6A: FE FF      CP      $FF             
5E6C: 8F         ADC     A,A             
5E6D: FF         RST     0X38            
5E6E: 1F         RRA                     
5E6F: FF         RST     0X38            
5E70: C6 FF      ADD     $FF             
5E72: CE FF      ADC     $FF             
5E74: CC FF DC   CALL    Z,$DCFF         
5E77: FF         RST     0X38            
5E78: 74         LD      (HL),H          
5E79: FF         RST     0X38            
5E7A: 67         LD      H,A             
5E7B: FF         RST     0X38            
5E7C: C7         RST     0X00            
5E7D: FF         RST     0X38            
5E7E: 8F         ADC     A,A             
5E7F: FF         RST     0X38            
5E80: 20 FF      JR      NZ,$5E81        
5E82: 20 FF      JR      NZ,$5E83        
5E84: 00         NOP                     
5E85: FF         RST     0X38            
5E86: 01 FF 01   LD      BC,$01FF        
5E89: FF         RST     0X38            
5E8A: E0 FF      LDFF00  ($FF),A         
5E8C: 80         ADD     A,B             
5E8D: FF         RST     0X38            
5E8E: 00         NOP                     
5E8F: FF         RST     0X38            
5E90: 37         SCF                     
5E91: C0         RET     NZ              
5E92: 5B         LD      E,E             
5E93: A4         AND     H               
5E94: 52         LD      D,D             
5E95: 2D         DEC     L               
5E96: 86         ADD     A,(HL)          
5E97: 79         LD      A,C             
5E98: 84         ADD     A,H             
5E99: 7B         LD      A,E             
5E9A: C4 3B B0   CALL    NZ,$B03B        
5E9D: 4F         LD      C,A             
5E9E: B8         CP      B               
5E9F: 57         LD      D,A             
5EA0: F2         ???                     
5EA1: 7C         LD      A,H             
5EA2: FD         ???                     
5EA3: FE 7F      CP      $7F             
5EA5: 8F         ADC     A,A             
5EA6: FF         RST     0X38            
5EA7: 37         SCF                     
5EA8: BF         CP      A               
5EA9: 57         LD      D,A             
5EAA: FF         RST     0X38            
5EAB: 0F         RRCA                    
5EAC: 1F         RRA                     
5EAD: FF         RST     0X38            
5EAE: 0F         RRCA                    
5EAF: FF         RST     0X38            
5EB0: 37         SCF                     
5EB1: C0         RET     NZ              
5EB2: 5B         LD      E,E             
5EB3: A4         AND     H               
5EB4: 52         LD      D,D             
5EB5: 2D         DEC     L               
5EB6: 86         ADD     A,(HL)          
5EB7: 79         LD      A,C             
5EB8: 84         ADD     A,H             
5EB9: 7B         LD      A,E             
5EBA: C4 3B B0   CALL    NZ,$B03B        
5EBD: 4F         LD      C,A             
5EBE: A8         XOR     B               
5EBF: 57         LD      D,A             
5EC0: F2         ???                     
5EC1: 7C         LD      A,H             
5EC2: FD         ???                     
5EC3: FE 7F      CP      $7F             
5EC5: 8F         ADC     A,A             
5EC6: DF         RST     0X18            
5EC7: 37         SCF                     
5EC8: BF         CP      A               
5EC9: 57         LD      D,A             
5ECA: DF         RST     0X18            
5ECB: 2F         CPL                     
5ECC: 1F         RRA                     
5ECD: FF         RST     0X38            
5ECE: 0F         RRCA                    
5ECF: FF         RST     0X38            
5ED0: 37         SCF                     
5ED1: C0         RET     NZ              
5ED2: 5B         LD      E,E             
5ED3: A4         AND     H               
5ED4: 52         LD      D,D             
5ED5: 2D         DEC     L               
5ED6: 86         ADD     A,(HL)          
5ED7: 79         LD      A,C             
5ED8: 84         ADD     A,H             
5ED9: 7B         LD      A,E             
5EDA: C4 3B B0   CALL    NZ,$B03B        
5EDD: 4F         LD      C,A             
5EDE: B8         CP      B               
5EDF: 47         LD      B,A             
5EE0: F2         ???                     
5EE1: 7C         LD      A,H             
5EE2: FD         ???                     
5EE3: FE 7F      CP      $7F             
5EE5: 8F         ADC     A,A             
5EE6: BF         CP      A               
5EE7: 57         LD      D,A             
5EE8: FF         RST     0X38            
5EE9: 17         RLA                     
5EEA: FF         RST     0X38            
5EEB: 6F         LD      L,A             
5EEC: 1F         RRA                     
5EED: FF         RST     0X38            
5EEE: 0F         RRCA                    
5EEF: FF         RST     0X38            
5EF0: FC         ???                     
5EF1: 00         NOP                     
5EF2: F8 00      LDHL    SP,$00          
5EF4: 60         LD      H,B             
5EF5: 00         NOP                     
5EF6: 00         NOP                     
5EF7: 00         NOP                     
5EF8: 00         NOP                     
5EF9: 00         NOP                     
5EFA: 00         NOP                     
5EFB: 00         NOP                     
5EFC: 00         NOP                     
5EFD: 00         NOP                     
5EFE: 00         NOP                     
5EFF: 00         NOP                     
5F00: 00         NOP                     
5F01: 40         LD      B,B             
5F02: 00         NOP                     
5F03: 20 00      JR      NZ,$5F05        
5F05: A2         AND     D               
5F06: 00         NOP                     
5F07: 49         LD      C,C             
5F08: 00         NOP                     
5F09: 85         ADD     A,L             
5F0A: 80         ADD     A,B             
5F0B: A5         AND     L               
5F0C: 80         ADD     A,B             
5F0D: A0         AND     B               
5F0E: 00         NOP                     
5F0F: A8         XOR     B               
5F10: 67         LD      H,A             
5F11: FF         RST     0X38            
5F12: 23         INC     HL              
5F13: FF         RST     0X38            
5F14: 03         INC     BC              
5F15: FF         RST     0X38            
5F16: 07         RLCA                    
5F17: FF         RST     0X38            
5F18: 3D         DEC     A               
5F19: FF         RST     0X38            
5F1A: 0F         RRCA                    
5F1B: FF         RST     0X38            
5F1C: 03         INC     BC              
5F1D: FF         RST     0X38            
5F1E: 00         NOP                     
5F1F: FF         RST     0X38            
5F20: F0 F0      LD      A,($F0)         
5F22: 60         LD      H,B             
5F23: E0 40      LDFF00  ($40),A         
5F25: E0 FC      LDFF00  ($FC),A         
5F27: FC         ???                     
5F28: FE FE      CP      $FE             
5F2A: BF         CP      A               
5F2B: FF         RST     0X38            
5F2C: CF         RST     0X08            
5F2D: FF         RST     0X38            
5F2E: C3 FF 08   JP      $08FF           
5F31: 1F         RRA                     
5F32: 00         NOP                     
5F33: 1F         RRA                     
5F34: 00         NOP                     
5F35: 1F         RRA                     
5F36: 0C         INC     C               
5F37: 1F         RRA                     
5F38: 38 3F      JR      C,$5F79         
5F3A: 79         LD      A,C             
5F3B: 7F         LD      A,A             
5F3C: 6B         LD      L,E             
5F3D: 7F         LD      A,A             
5F3E: 67         LD      H,A             
5F3F: 7F         LD      A,A             
5F40: 38 FF      JR      C,$5F41         
5F42: 30 FF      JR      NC,$5F43        
5F44: 20 FF      JR      NZ,$5F45        
5F46: 2C         INC     L               
5F47: FF         RST     0X38            
5F48: 3F         CCF                     
5F49: FF         RST     0X38            
5F4A: FC         ???                     
5F4B: FF         RST     0X38            
5F4C: F0 FF      LD      A,($FF)         
5F4E: 60         LD      H,B             
5F4F: FF         RST     0X38            
5F50: 02         LD      (BC),A          
5F51: 1F         RRA                     
5F52: 07         RLCA                    
5F53: 1F         RRA                     
5F54: 06 1F      LD      B,$1F           
5F56: 0C         INC     C               
5F57: 1F         RRA                     
5F58: 18 3F      JR      $5F99           
5F5A: 79         LD      A,C             
5F5B: 7F         LD      A,A             
5F5C: 6B         LD      L,E             
5F5D: 7F         LD      A,A             
5F5E: 67         LD      H,A             
5F5F: 7F         LD      A,A             
5F60: 79         LD      A,C             
5F61: FF         RST     0X38            
5F62: F6 FF      OR      $FF             
5F64: 6F         LD      L,A             
5F65: FF         RST     0X38            
5F66: FC         ???                     
5F67: FF         RST     0X38            
5F68: FF         RST     0X38            
5F69: FF         RST     0X38            
5F6A: FC         ???                     
5F6B: FF         RST     0X38            
5F6C: F0 FF      LD      A,($FF)         
5F6E: 60         LD      H,B             
5F6F: FF         RST     0X38            
5F70: 9C         SBC     H               
5F71: FF         RST     0X38            
5F72: 1C         INC     E               
5F73: FF         RST     0X38            
5F74: 18 FF      JR      $5F75           
5F76: 18 FF      JR      $5F77           
5F78: 10 FF      STOP    $FF             
5F7A: 00         NOP                     
5F7B: FF         RST     0X38            
5F7C: 00         NOP                     
5F7D: FF         RST     0X38            
5F7E: 00         NOP                     
5F7F: FF         RST     0X38            
5F80: 02         LD      (BC),A          
5F81: 83         ADD     A,E             
5F82: 00         NOP                     
5F83: 93         SUB     E               
5F84: 00         NOP                     
5F85: 16 00      LD      D,$00           
5F87: 13         INC     DE              
5F88: 00         NOP                     
5F89: 4A         LD      C,D             
5F8A: 00         NOP                     
5F8B: 49         LD      C,C             
5F8C: 00         NOP                     
5F8D: 24         INC     H               
5F8E: 00         NOP                     
5F8F: 10 F4      STOP    $F4             
5F91: 0B         DEC     BC              
5F92: 7A         LD      A,D             
5F93: 05         DEC     B               
5F94: 23         INC     HL              
5F95: 1D         DEC     E               
5F96: 17         RLA                     
5F97: 0B         DEC     BC              
5F98: 8F         ADC     A,A             
5F99: 03         INC     BC              
5F9A: 84         ADD     A,H             
5F9B: 03         INC     BC              
5F9C: E7         RST     0X20            
5F9D: 00         NOP                     
5F9E: 79         LD      A,C             
5F9F: 00         NOP                     
5FA0: BF         CP      A               
5FA1: FF         RST     0X38            
5FA2: 9F         SBC     A               
5FA3: FF         RST     0X38            
5FA4: 2F         CPL                     
5FA5: FF         RST     0X38            
5FA6: 1F         RRA                     
5FA7: 7F         LD      A,A             
5FA8: 27         DAA                     
5FA9: BF         CP      A               
5FAA: 16 7F      LD      D,$7F           
5FAC: 20 7F      JR      NZ,$602D        
5FAE: 13         INC     DE              
5FAF: 3F         CCF                     
5FB0: FC         ???                     
5FB1: 0B         DEC     BC              
5FB2: 6A         LD      L,D             
5FB3: 15         DEC     D               
5FB4: 23         INC     HL              
5FB5: 1D         DEC     E               
5FB6: 17         RLA                     
5FB7: 0B         DEC     BC              
5FB8: 8F         ADC     A,A             
5FB9: 03         INC     BC              
5FBA: 84         ADD     A,H             
5FBB: 03         INC     BC              
5FBC: E7         RST     0X20            
5FBD: 00         NOP                     
5FBE: 79         LD      A,C             
5FBF: 00         NOP                     
5FC0: FC         ???                     
5FC1: FF         RST     0X38            
5FC2: FD         ???                     
5FC3: FF         RST     0X38            
5FC4: F1         POP     AF              
5FC5: FF         RST     0X38            
5FC6: FA FF F0   LD      A,($F0FF)       
5FC9: FF         RST     0X38            
5FCA: 24         INC     H               
5FCB: FE 48      CP      $48             
5FCD: FD         ???                     
5FCE: 00         NOP                     
5FCF: FA 40 E8   LD      A,($E840)       
5FD2: 40         LD      B,B             
5FD3: E8 40      ADD     SP,$40          
5FD5: E0 00      LDFF00  ($00),A         
5FD7: C2 00 C2   JP      NZ,$C200        
5FDA: 00         NOP                     
5FDB: 24         INC     H               
5FDC: 00         NOP                     
5FDD: 40         LD      B,B             
5FDE: 00         NOP                     
5FDF: 80         ADD     A,B             
5FE0: 00         NOP                     
5FE1: 00         NOP                     
5FE2: 00         NOP                     
5FE3: 08 00 04   LD      ($0400),SP      
5FE6: 00         NOP                     
5FE7: 20 00      JR      NZ,$5FE9        
5FE9: 10 00      STOP    $00             
5FEB: 08 00 00   LD      ($0000),SP      
5FEE: 00         NOP                     
5FEF: 00         NOP                     
5FF0: 00         NOP                     
5FF1: 3F         CCF                     
5FF2: 00         NOP                     
5FF3: 99         SBC     C               
5FF4: 00         NOP                     
5FF5: 67         LD      H,A             
5FF6: 00         NOP                     
5FF7: 00         NOP                     
5FF8: 00         NOP                     
5FF9: 03         INC     BC              
5FFA: 00         NOP                     
5FFB: 40         LD      B,B             
5FFC: 00         NOP                     
5FFD: 30 00      JR      NC,$5FFF        
5FFF: 01 00 00   LD      BC,$0000        
6002: 00         NOP                     
6003: 00         NOP                     
6004: 01 00 03   LD      BC,$0300        
6007: 00         NOP                     
6008: 05         DEC     B               
6009: 02         LD      (BC),A          
600A: 09         ADD     HL,BC           
600B: 06 08      LD      B,$08           
600D: 07         RLCA                    
600E: 08 03 00   LD      ($0003),SP      
6011: 00         NOP                     
6012: 00         NOP                     
6013: 00         NOP                     
6014: 00         NOP                     
6015: 00         NOP                     
6016: 01 00 07   LD      BC,$0700        
6019: 01 0E 06   LD      BC,$060E        
601C: BF         CP      A               
601D: 0F         RRCA                    
601E: 70         LD      (HL),B          
601F: 9F         SBC     A               
6020: 07         RLCA                    
6021: 00         NOP                     
6022: 18 00      JR      $6024           
6024: 20 00      JR      NZ,$6026        
6026: FE 00      CP      $00             
6028: FF         RST     0X38            
6029: FE 0F      CP      $0F             
602B: 1F         RRA                     
602C: F7         RST     0X30            
602D: FF         RST     0X38            
602E: 3F         CCF                     
602F: FF         RST     0X38            
6030: F0 00      LD      A,($00)         
6032: 3E 00      LD      A,$00           
6034: 03         INC     BC              
6035: 00         NOP                     
6036: 00         NOP                     
6037: 00         NOP                     
6038: C0         RET     NZ              
6039: 00         NOP                     
603A: F0 C0      LD      A,($C0)         
603C: FE F0      CP      $F0             
603E: FF         RST     0X38            
603F: FC         ???                     
6040: 00         NOP                     
6041: 00         NOP                     
6042: 00         NOP                     
6043: 00         NOP                     
6044: F0 00      LD      A,($00)         
6046: 18 00      JR      $6048           
6048: 0C         INC     C               
6049: 00         NOP                     
604A: 06 00      LD      B,$00           
604C: 06 00      LD      B,$00           
604E: 83         ADD     A,E             
604F: 00         NOP                     
6050: 30 FC      JR      NC,$604E        
6052: C0         RET     NZ              
6053: FA 00 E4   LD      A,($E400)       
6056: 00         NOP                     
6057: 39         ADD     HL,SP           
6058: 00         NOP                     
6059: 82         ADD     A,D             
605A: 00         NOP                     
605B: 0C         INC     C               
605C: 00         NOP                     
605D: 00         NOP                     
605E: 00         NOP                     
605F: C0         RET     NZ              
6060: 0C         INC     C               
6061: 03         INC     BC              
6062: 10 0F      STOP    $0F             
6064: 20 1F      JR      NZ,$6085        
6066: 20 1F      JR      NZ,$6087        
6068: 46         LD      B,(HL)          
6069: 20 58      JR      NZ,$60C3        
606B: 07         RLCA                    
606C: 60         LD      H,B             
606D: 1F         RRA                     
606E: 60         LD      H,B             
606F: 1F         RRA                     
6070: 10 E7      STOP    $E7             
6072: 00         NOP                     
6073: FF         RST     0X38            
6074: 00         NOP                     
6075: FF         RST     0X38            
6076: 00         NOP                     
6077: FF         RST     0X38            
6078: 00         NOP                     
6079: FF         RST     0X38            
607A: 00         NOP                     
607B: FF         RST     0X38            
607C: 00         NOP                     
607D: FF         RST     0X38            
607E: 00         NOP                     
607F: FF         RST     0X38            
6080: 0F         RRCA                    
6081: F1         POP     AF              
6082: 01 FE 00   LD      BC,$00FE        
6085: FF         RST     0X38            
6086: 00         NOP                     
6087: FF         RST     0X38            
6088: 00         NOP                     
6089: FF         RST     0X38            
608A: 00         NOP                     
608B: EF         RST     0X28            
608C: 00         NOP                     
608D: EF         RST     0X28            
608E: 10 CF      STOP    $CF             
6090: DC F8 FE   CALL    C,$FEF8         
6093: 7C         LD      A,H             
6094: 7F         LD      A,A             
6095: BE         CP      (HL)            
6096: 3F         CCF                     
6097: DF         RST     0X18            
6098: 1F         RRA                     
6099: EF         RST     0X28            
609A: 0F         RRCA                    
609B: F7         RST     0X30            
609C: 0F         RRCA                    
609D: F7         RST     0X30            
609E: 05         DEC     B               
609F: EB         ???                     
60A0: 60         LD      H,B             
60A1: 00         NOP                     
60A2: 10 00      STOP    $00             
60A4: 08 00 84   LD      ($8400),SP      
60A7: 00         NOP                     
60A8: C2 80 E1   JP      NZ,$E180        
60AB: C0         RET     NZ              
60AC: F1         POP     AF              
60AD: C0         RET     NZ              
60AE: F1         POP     AF              
60AF: E0 00      LDFF00  ($00),A         
60B1: 10 00      STOP    $00             
60B3: 20 00      JR      NZ,$60B5        
60B5: 08 00 10   LD      ($1000),SP      
60B8: 00         NOP                     
60B9: 20 00      JR      NZ,$60BB        
60BB: 00         NOP                     
60BC: 00         NOP                     
60BD: 00         NOP                     
60BE: 00         NOP                     
60BF: 00         NOP                     
60C0: 00         NOP                     
60C1: 00         NOP                     
60C2: 00         NOP                     
60C3: 00         NOP                     
60C4: 00         NOP                     
60C5: 00         NOP                     
60C6: 00         NOP                     
60C7: 00         NOP                     
60C8: 00         NOP                     
60C9: 00         NOP                     
60CA: 00         NOP                     
60CB: 00         NOP                     
60CC: 00         NOP                     
60CD: 00         NOP                     
60CE: 03         INC     BC              
60CF: 00         NOP                     
60D0: 00         NOP                     
60D1: 00         NOP                     
60D2: 00         NOP                     
60D3: 00         NOP                     
60D4: 07         RLCA                    
60D5: 00         NOP                     
60D6: 09         ADD     HL,BC           
60D7: 06 12      LD      B,$12           
60D9: 0C         INC     C               
60DA: 22         LD      (HLI),A         
60DB: 1C         INC     E               
60DC: 21 1E F0   LD      HL,$F01E        
60DF: 0F         RRCA                    
60E0: 00         NOP                     
60E1: 00         NOP                     
60E2: 00         NOP                     
60E3: 00         NOP                     
60E4: 00         NOP                     
60E5: 00         NOP                     
60E6: 00         NOP                     
60E7: 00         NOP                     
60E8: 00         NOP                     
60E9: 00         NOP                     
60EA: 00         NOP                     
60EB: 00         NOP                     
60EC: 00         NOP                     
60ED: 00         NOP                     
60EE: 00         NOP                     
60EF: 00         NOP                     
60F0: 00         NOP                     
60F1: 00         NOP                     
60F2: 07         RLCA                    
60F3: 00         NOP                     
60F4: 18 00      JR      $60F6           
60F6: 30 00      JR      NC,$60F8        
60F8: 5C         LD      E,H             
60F9: 20 BF      JR      NZ,$60BA        
60FB: 50         LD      D,B             
60FC: 9F         SBC     A               
60FD: 00         NOP                     
60FE: 64         LD      H,H             
60FF: 18 04      JR      $6105           
6101: 00         NOP                     
6102: 06 00      LD      B,$00           
6104: 08 07 10   LD      ($1007),SP      
6107: 0F         RRCA                    
6108: 20 1F      JR      NZ,$6129        
610A: 40         LD      B,B             
610B: 3F         CCF                     
610C: 40         LD      B,B             
610D: 3F         CCF                     
610E: 88         ADC     A,B             
610F: 17         RLA                     
6110: 2F         CPL                     
6111: 50         LD      D,B             
6112: 30 C3      JR      NC,$60D7        
6114: 00         NOP                     
6115: FF         RST     0X38            
6116: 00         NOP                     
6117: FF         RST     0X38            
6118: 00         NOP                     
6119: FF         RST     0X38            
611A: 00         NOP                     
611B: FF         RST     0X38            
611C: 00         NOP                     
611D: FF         RST     0X38            
611E: 00         NOP                     
611F: FF         RST     0X38            
6120: DF         RST     0X18            
6121: 3F         CCF                     
6122: 3F         CCF                     
6123: C1         POP     BC              
6124: 01 FE 00   LD      BC,$00FE        
6127: FF         RST     0X38            
6128: 00         NOP                     
6129: FF         RST     0X38            
612A: 00         NOP                     
612B: FE 00      CP      $00             
612D: FE 00      CP      $00             
612F: EE CF      XOR     $CF             
6131: FE FF      CP      $FF             
6133: FF         RST     0X38            
6134: FF         RST     0X38            
6135: 7F         LD      A,A             
6136: 7F         LD      A,A             
6137: 1F         RRA                     
6138: 9F         SBC     A               
6139: 6F         LD      L,A             
613A: 8E         ADC     A,(HL)          
613B: 77         LD      (HL),A          
613C: 87         ADD     A,A             
613D: 7A         LD      A,D             
613E: 83         ADD     A,E             
613F: 7C         LD      A,H             
6140: E1         POP     HL              
6141: 00         NOP                     
6142: F8 00      LDHL    SP,$00          
6144: FC         ???                     
6145: 00         NOP                     
6146: FC         ???                     
6147: 90         SUB     B               
6148: FF         RST     0X38            
6149: B0         OR      B               
614A: FF         RST     0X38            
614B: 78         LD      A,B             
614C: EF         RST     0X28            
614D: 58         LD      E,B             
614E: EF         RST     0X28            
614F: D8         RET     C               
6150: C0         RET     NZ              
6151: 00         NOP                     
6152: 30 00      JR      NC,$6154        
6154: 08 00 84   LD      ($8400),SP      
6157: 00         NOP                     
6158: 82         ADD     A,D             
6159: 00         NOP                     
615A: 02         LD      (BC),A          
615B: 00         NOP                     
615C: 7A         LD      A,D             
615D: 00         NOP                     
615E: FD         ???                     
615F: 00         NOP                     
6160: 40         LD      B,B             
6161: 3F         CCF                     
6162: C0         RET     NZ              
6163: 3F         CCF                     
6164: 80         ADD     A,B             
6165: 7F         LD      A,A             
6166: 80         ADD     A,B             
6167: 7F         LD      A,A             
6168: 80         ADD     A,B             
6169: 7C         LD      A,H             
616A: 82         ADD     A,D             
616B: 61         LD      H,C             
616C: 84         ADD     A,H             
616D: 03         INC     BC              
616E: 84         ADD     A,H             
616F: 02         LD      (BC),A          
6170: 00         NOP                     
6171: FF         RST     0X38            
6172: 04         INC     B               
6173: FB         EI                      
6174: 04         INC     B               
6175: FA 09 F4   LD      A,($F409)       
6178: 12         LD      (DE),A          
6179: E9         JP      (HL)            
617A: 37         SCF                     
617B: 81         ADD     A,C             
617C: 39         ADD     HL,SP           
617D: 04         INC     B               
617E: 76         HALT                    
617F: 08 10 8F   LD      ($8F10),SP      
6182: 20 1C      JR      NZ,$61A0        
6184: C7         RST     0X00            
6185: 20 FC      JR      NZ,$6183        
6187: 00         NOP                     
6188: 0F         RRCA                    
6189: F0 DF      LD      A,($DF)         
618B: EF         RST     0X28            
618C: FF         RST     0X38            
618D: D8         RET     C               
618E: 7B         LD      A,E             
618F: 74         LD      (HL),H          
6190: 07         RLCA                    
6191: 0B         DEC     BC              
6192: E7         RST     0X20            
6193: 1B         DEC     DE              
6194: C3 9D C3   JP      $C39D           
6197: 1D         DEC     E               
6198: 41         LD      B,C             
6199: 1E E1      LD      E,$E1           
619B: 0E E0      LD      C,$E0           
619D: CE E0      ADC     $E0             
619F: 46         LD      B,(HL)          
61A0: F8 E0      LDHL    SP,$E0          
61A2: FC         ???                     
61A3: F0 FE      LD      A,($FE)         
61A5: F0 FE      LD      A,($FE)         
61A7: C4 FF CC   CALL    NZ,$CCFF        
61AA: FF         RST     0X38            
61AB: 1C         INC     E               
61AC: 7F         LD      A,A             
61AD: 34         INC     (HL)            
61AE: F7         RST     0X30            
61AF: 6C         LD      L,H             
61B0: 80         ADD     A,B             
61B1: 00         NOP                     
61B2: C0         RET     NZ              
61B3: 00         NOP                     
61B4: 70         LD      (HL),B          
61B5: 00         NOP                     
61B6: 18 00      JR      $61B8           
61B8: 0C         INC     C               
61B9: 00         NOP                     
61BA: 84         ADD     A,H             
61BB: 00         NOP                     
61BC: E4         ???                     
61BD: 00         NOP                     
61BE: FE 00      CP      $00             
61C0: 00         NOP                     
61C1: 00         NOP                     
61C2: 00         NOP                     
61C3: 00         NOP                     
61C4: 80         ADD     A,B             
61C5: 00         NOP                     
61C6: 00         NOP                     
61C7: 00         NOP                     
61C8: 00         NOP                     
61C9: 00         NOP                     
61CA: 1F         RRA                     
61CB: 00         NOP                     
61CC: FE 1C      CP      $1C             
61CE: 3F         CCF                     
61CF: CF         RST     0X08            
61D0: 00         NOP                     
61D1: 00         NOP                     
61D2: 00         NOP                     
61D3: 00         NOP                     
61D4: 00         NOP                     
61D5: 00         NOP                     
61D6: 00         NOP                     
61D7: 00         NOP                     
61D8: 00         NOP                     
61D9: 00         NOP                     
61DA: C0         RET     NZ              
61DB: 00         NOP                     
61DC: F8 C0      LDHL    SP,$C0          
61DE: 3F         CCF                     
61DF: 70         LD      (HL),B          
61E0: 00         NOP                     
61E1: 00         NOP                     
61E2: 00         NOP                     
61E3: 00         NOP                     
61E4: 00         NOP                     
61E5: 00         NOP                     
61E6: 00         NOP                     
61E7: 00         NOP                     
61E8: 00         NOP                     
61E9: 00         NOP                     
61EA: 00         NOP                     
61EB: 00         NOP                     
61EC: 00         NOP                     
61ED: 00         NOP                     
61EE: 00         NOP                     
61EF: 00         NOP                     
61F0: 80         ADD     A,B             
61F1: 00         NOP                     
61F2: C0         RET     NZ              
61F3: 00         NOP                     
61F4: 20 00      JR      NZ,$61F6        
61F6: 10 00      STOP    $00             
61F8: 17         RLA                     
61F9: 00         NOP                     
61FA: 8F         ADC     A,A             
61FB: 06 CF      LD      B,$CF           
61FD: 00         NOP                     
61FE: EA 01 90   LD      ($9001),A       
6201: 0F         RRCA                    
6202: 40         LD      B,B             
6203: 3F         CCF                     
6204: 40         LD      B,B             
6205: 3E 80      LD      A,$80           
6207: 7C         LD      A,H             
6208: 80         ADD     A,B             
6209: 38 80      JR      C,$618B         
620B: 00         NOP                     
620C: 80         ADD     A,B             
620D: 00         NOP                     
620E: 80         ADD     A,B             
620F: 00         NOP                     
6210: 00         NOP                     
6211: FF         RST     0X38            
6212: 02         LD      (BC),A          
6213: F9         LD      SP,HL           
6214: 04         INC     B               
6215: F3         DI                      
6216: 04         INC     B               
6217: C3 04 00   JP      $0004           
621A: 05         DEC     B               
621B: 00         NOP                     
621C: 0B         DEC     BC              
621D: 00         NOP                     
621E: 0F         RRCA                    
621F: 00         NOP                     
6220: 01 EC 02   LD      BC,$02EC        
6223: E1         POP     HL              
6224: 27         DAA                     
6225: C0         RET     NZ              
6226: 6C         LD      L,H             
6227: 83         ADD     A,E             
6228: AB         XOR     E               
6229: 44         LD      B,H             
622A: BD         CP      L               
622B: 42         LD      B,D             
622C: 17         RLA                     
622D: E8 87      ADD     SP,$87          
622F: 7F         LD      A,A             
6230: 81         ADD     A,C             
6231: 1E 81      LD      E,$81           
6233: 0C         INC     C               
6234: C1         POP     BC              
6235: 00         NOP                     
6236: E1         POP     HL              
6237: 80         ADD     A,B             
6238: D9         RETI                    
6239: 60         LD      H,B             
623A: E4         ???                     
623B: B8         CP      B               
623C: F4         ???                     
623D: B8         CP      B               
623E: F2         ???                     
623F: 7D         LD      A,L             
6240: EF         RST     0X28            
6241: D8         RET     C               
6242: DD         ???                     
6243: AA         XOR     D               
6244: DD         ???                     
6245: AA         XOR     D               
6246: 9F         SBC     A               
6247: 68         LD      L,B             
6248: 1D         DEC     E               
6249: D8         RET     C               
624A: 9C         SBC     H               
624B: 58         LD      E,B             
624C: BC         CP      H               
624D: 78         LD      A,B             
624E: 78         LD      A,B             
624F: 30 C7      JR      NC,$6218        
6251: 00         NOP                     
6252: 81         ADD     A,C             
6253: 00         NOP                     
6254: 00         NOP                     
6255: 00         NOP                     
6256: 00         NOP                     
6257: 00         NOP                     
6258: 04         INC     B               
6259: 00         NOP                     
625A: 09         ADD     HL,BC           
625B: 00         NOP                     
625C: 12         LD      (DE),A          
625D: 01 36 01   LD      BC,$0136        
6260: 48         LD      C,B             
6261: 06 48      LD      B,$48           
6263: 04         INC     B               
6264: 28 00      JR      Z,$6266         
6266: 18 00      JR      $6268           
6268: 04         INC     B               
6269: 00         NOP                     
626A: 03         INC     BC              
626B: 00         NOP                     
626C: 00         NOP                     
626D: 00         NOP                     
626E: 00         NOP                     
626F: 00         NOP                     
6270: 5B         LD      E,E             
6271: 04         INC     B               
6272: 97         SUB     A               
6273: 01 97 0F   LD      BC,$0F97        
6276: 90         SUB     B               
6277: 0E 97      LD      C,$97           
6279: 08 9F 07   LD      ($079F),SP      
627C: DF         RST     0X18            
627D: 07         RLCA                    
627E: 3C         INC     A               
627F: 0B         DEC     BC              
6280: 7F         LD      A,A             
6281: 71         LD      (HL),C          
6282: 7F         LD      A,A             
6283: FF         RST     0X38            
6284: FC         ???                     
6285: 79         LD      A,C             
6286: FF         RST     0X38            
6287: 7F         LD      A,A             
6288: FE FF      CP      $FF             
628A: FF         RST     0X38            
628B: FF         RST     0X38            
628C: FF         RST     0X38            
628D: FF         RST     0X38            
628E: 3F         CCF                     
628F: FF         RST     0X38            
6290: F0 60      LD      A,($60)         
6292: 70         LD      (HL),B          
6293: E0 F8      LDFF00  ($F8),A         
6295: F0 F4      LD      A,($F4)         
6297: F9         LD      SP,HL           
6298: 74         LD      (HL),H          
6299: FB         EI                      
629A: A8         XOR     B               
629B: F7         RST     0X30            
629C: E8 F7      ADD     SP,$F7          
629E: F0 E7      LD      A,($E7)         
62A0: F6 4D      OR      $4D             
62A2: F6 4D      OR      $4D             
62A4: DF         RST     0X18            
62A5: 28 9F      JR      Z,$6246         
62A7: 68         LD      L,B             
62A8: BF         CP      A               
62A9: 58         LD      E,B             
62AA: FF         RST     0X38            
62AB: 70         LD      (HL),B          
62AC: FD         ???                     
62AD: 70         LD      (HL),B          
62AE: FC         ???                     
62AF: 20 C7      JR      NZ,$6278        
62B1: 00         NOP                     
62B2: 81         ADD     A,C             
62B3: 00         NOP                     
62B4: 80         ADD     A,B             
62B5: 00         NOP                     
62B6: 80         ADD     A,B             
62B7: 00         NOP                     
62B8: 04         INC     B               
62B9: 00         NOP                     
62BA: 19         ADD     HL,DE           
62BB: 00         NOP                     
62BC: 32         LD      (HLD),A         
62BD: 01 76 01   LD      BC,$0176        
62C0: 00         NOP                     
62C1: FF         RST     0X38            
62C2: 00         NOP                     
62C3: FF         RST     0X38            
62C4: 07         RLCA                    
62C5: FF         RST     0X38            
62C6: 03         INC     BC              
62C7: FF         RST     0X38            
62C8: 07         RLCA                    
62C9: FF         RST     0X38            
62CA: 0F         RRCA                    
62CB: FF         RST     0X38            
62CC: 1E FE      LD      E,$FE           
62CE: FE FE      CP      $FE             
62D0: 1F         RRA                     
62D1: FF         RST     0X38            
62D2: 3E FE      LD      A,$FE           
62D4: FC         ???                     
62D5: FC         ???                     
62D6: E0 E0      LDFF00  ($E0),A         
62D8: 00         NOP                     
62D9: 00         NOP                     
62DA: 00         NOP                     
62DB: 00         NOP                     
62DC: 00         NOP                     
62DD: 00         NOP                     
62DE: 00         NOP                     
62DF: 00         NOP                     
62E0: 00         NOP                     
62E1: 00         NOP                     
62E2: 00         NOP                     
62E3: 00         NOP                     
62E4: 00         NOP                     
62E5: 00         NOP                     
62E6: 00         NOP                     
62E7: 00         NOP                     
62E8: 00         NOP                     
62E9: 00         NOP                     
62EA: 00         NOP                     
62EB: 00         NOP                     
62EC: 00         NOP                     
62ED: 00         NOP                     
62EE: 00         NOP                     
62EF: 00         NOP                     
62F0: 00         NOP                     
62F1: 00         NOP                     
62F2: 00         NOP                     
62F3: 00         NOP                     
62F4: 00         NOP                     
62F5: 00         NOP                     
62F6: 00         NOP                     
62F7: 00         NOP                     
62F8: 00         NOP                     
62F9: 00         NOP                     
62FA: 80         ADD     A,B             
62FB: 00         NOP                     
62FC: FC         ???                     
62FD: 00         NOP                     
62FE: 42         LD      B,D             
62FF: BC         CP      H               
6300: 80         ADD     A,B             
6301: 00         NOP                     
6302: 84         ADD     A,H             
6303: 00         NOP                     
6304: 44         LD      B,H             
6305: 00         NOP                     
6306: C4 00 A2   CALL    NZ,$A200        
6309: 00         NOP                     
630A: A2         AND     D               
630B: 00         NOP                     
630C: 72         LD      (HL),D          
630D: 00         NOP                     
630E: B9         CP      C               
630F: 60         LD      H,B             
6310: 1D         DEC     E               
6311: 02         LD      (BC),A          
6312: 1F         RRA                     
6313: 00         NOP                     
6314: 1C         INC     E               
6315: 03         INC     BC              
6316: 3C         INC     A               
6317: 03         INC     BC              
6318: 2D         DEC     L               
6319: 02         LD      (BC),A          
631A: 2B         DEC     HL              
631B: 00         NOP                     
631C: 2B         DEC     HL              
631D: 00         NOP                     
631E: 15         DEC     D               
631F: 00         NOP                     
6320: 8F         ADC     A,A             
6321: 7F         LD      A,A             
6322: FF         RST     0X38            
6323: FF         RST     0X38            
6324: 7F         LD      A,A             
6325: BF         CP      A               
6326: 77         LD      (HL),A          
6327: BF         CP      A               
6328: E3         ???                     
6329: 7F         LD      A,A             
632A: C1         POP     BC              
632B: FF         RST     0X38            
632C: C0         RET     NZ              
632D: FF         RST     0X38            
632E: E3         ???                     
632F: 1C         INC     E               
6330: FA FD FA   LD      A,($FAFD)       
6333: FD         ???                     
6334: FA FD FA   LD      A,($FAFD)       
6337: FC         ???                     
6338: F2         ???                     
6339: FC         ???                     
633A: F2         ???                     
633B: FC         ???                     
633C: E2         LDFF00  (C),A           
633D: FC         ???                     
633E: 03         INC     BC              
633F: FC         ???                     
6340: 78         LD      A,B             
6341: B0         OR      B               
6342: 38 C0      JR      C,$6304         
6344: 1F         RRA                     
6345: E0 1F      LDFF00  ($1F),A         
6347: E0 0F      LDFF00  ($0F),A         
6349: F0 0F      LD      A,($0F)         
634B: 70         LD      (HL),B          
634C: 0F         RRCA                    
634D: 70         LD      (HL),B          
634E: 07         RLCA                    
634F: 38 3C      JR      C,$638D         
6351: 03         INC     BC              
6352: 7C         LD      A,H             
6353: 03         INC     BC              
6354: FC         ???                     
6355: 01 FC 00   LD      BC,$00FC        
6358: FC         ???                     
6359: 00         NOP                     
635A: FE 00      CP      $00             
635C: E7         RST     0X20            
635D: 0E D7      LD      C,$D7           
635F: 0E 00      LD      C,$00           
6361: 00         NOP                     
6362: 00         NOP                     
6363: 00         NOP                     
6364: 00         NOP                     
6365: 00         NOP                     
6366: 00         NOP                     
6367: 00         NOP                     
6368: 00         NOP                     
6369: 00         NOP                     
636A: DB         ???                     
636B: 00         NOP                     
636C: FF         RST     0X38            
636D: DB         ???                     
636E: FE FF      CP      $FF             
6370: 37         SCF                     
6371: 0C         INC     C               
6372: 30 0F      JR      NC,$6383        
6374: 28 07      JR      Z,$637D         
6376: 28 07      JR      Z,$637F         
6378: 24         INC     H               
6379: 03         INC     BC              
637A: 12         LD      (DE),A          
637B: 01 91 00   LD      BC,$0091        
637E: D0         RET     NC              
637F: 00         NOP                     
6380: 1F         RRA                     
6381: FF         RST     0X38            
6382: 3F         CCF                     
6383: FF         RST     0X38            
6384: FF         RST     0X38            
6385: 0F         RRCA                    
6386: FE FF      CP      $FF             
6388: 8C         ADC     A,H             
6389: 9F         SBC     A               
638A: 7C         LD      A,H             
638B: FF         RST     0X38            
638C: 70         LD      (HL),B          
638D: FF         RST     0X38            
638E: 83         ADD     A,E             
638F: 7C         LD      A,H             
6390: D0         RET     NC              
6391: E7         RST     0X20            
6392: D0         RET     NC              
6393: E7         RST     0X20            
6394: 90         SUB     B               
6395: E7         RST     0X20            
6396: 10 E7      STOP    $E7             
6398: 28 D3      JR      Z,$636D         
639A: 48         LD      C,B             
639B: B3         OR      E               
639C: C8         RET     Z               
639D: 11 28 01   LD      DE,$0128        
63A0: F8 00      LDHL    SP,$00          
63A2: 7C         LD      A,H             
63A3: 80         ADD     A,B             
63A4: 7F         LD      A,A             
63A5: 80         ADD     A,B             
63A6: 3F         CCF                     
63A7: C0         RET     NZ              
63A8: 3F         CCF                     
63A9: C0         RET     NZ              
63AA: 3F         CCF                     
63AB: C0         RET     NZ              
63AC: 1F         RRA                     
63AD: E0 1F      LDFF00  ($1F),A         
63AF: E0 FC      LDFF00  ($FC),A         
63B1: 03         INC     BC              
63B2: FC         ???                     
63B3: 03         INC     BC              
63B4: FC         ???                     
63B5: 01 FC 00   LD      BC,$00FC        
63B8: FC         ???                     
63B9: 00         NOP                     
63BA: FE 00      CP      $00             
63BC: E7         RST     0X20            
63BD: 0E D7      LD      C,$D7           
63BF: 0E 7C      LD      C,$7C           
63C1: FC         ???                     
63C2: 60         LD      H,B             
63C3: E0 30      LDFF00  ($30),A         
63C5: F0 30      LD      A,($30)         
63C7: F0 70      LD      A,($70)         
63C9: F0 60      LD      A,($60)         
63CB: E0 E0      LDFF00  ($E0),A         
63CD: E0 C0      LDFF00  ($C0),A         
63CF: C0         RET     NZ              
63D0: 02         LD      (BC),A          
63D1: FF         RST     0X38            
63D2: 03         INC     BC              
63D3: FF         RST     0X38            
63D4: 07         RLCA                    
63D5: FF         RST     0X38            
63D6: 0E FE      LD      C,$FE           
63D8: 1E FE      LD      E,$FE           
63DA: FE FE      CP      $FE             
63DC: FC         ???                     
63DD: FC         ???                     
63DE: F0 F0      LD      A,($F0)         
63E0: 07         RLCA                    
63E1: FF         RST     0X38            
63E2: 07         RLCA                    
63E3: FF         RST     0X38            
63E4: 07         RLCA                    
63E5: FF         RST     0X38            
63E6: 0E FE      LD      C,$FE           
63E8: 1C         INC     E               
63E9: FC         ???                     
63EA: 18 F8      JR      $63E4           
63EC: 38 F8      JR      C,$63E6         
63EE: 38 F8      JR      C,$63E8         
63F0: F8 F8      LDHL    SP,$F8          
63F2: F0 F0      LD      A,($F0)         
63F4: E0 E0      LDFF00  ($E0),A         
63F6: 00         NOP                     
63F7: 00         NOP                     
63F8: 00         NOP                     
63F9: 00         NOP                     
63FA: 00         NOP                     
63FB: 00         NOP                     
63FC: 00         NOP                     
63FD: 00         NOP                     
63FE: 00         NOP                     
63FF: 00         NOP                     
6400: F7         RST     0X30            
6401: 38 F4      JR      C,$63F7         
6403: 3B         DEC     SP              
6404: 47         LD      B,A             
6405: B8         CP      B               
6406: 48         LD      C,B             
6407: B0         OR      B               
6408: F3         DI                      
6409: 07         RLCA                    
640A: 0E 0E      LD      C,$0E           
640C: 03         INC     BC              
640D: FF         RST     0X38            
640E: 00         NOP                     
640F: 0F         RRCA                    
6410: 9D         SBC     L               
6411: 00         NOP                     
6412: D4 00 A2   CALL    NC,$A200        
6415: C8         RET     Z               
6416: 82         ADD     A,D             
6417: F0 00      LD      A,($00)         
6419: F0 C0      LD      A,($C0)         
641B: F0 01      LD      A,($01)         
641D: 60         LD      H,B             
641E: 06 00      LD      B,$00           
6420: 8C         ADC     A,H             
6421: 73         LD      (HL),E          
6422: 83         ADD     A,E             
6423: 7C         LD      A,H             
6424: 40         LD      B,B             
6425: 3F         CCF                     
6426: 30 0F      JR      NC,$6437        
6428: 08 07 F7   LD      ($F707),SP      
642B: 00         NOP                     
642C: 08 00 10   LD      ($1000),SP      
642F: 80         ADD     A,B             
6430: 05         DEC     B               
6431: FA 09 F0   LD      A,($F009)       
6434: 10 E0      STOP    $E0             
6436: 20 C8      JR      NZ,$6400        
6438: C7         RST     0X00            
6439: 00         NOP                     
643A: 1E 20      LD      E,$20           
643C: 00         NOP                     
643D: 07         RLCA                    
643E: 09         ADD     HL,BC           
643F: 00         NOP                     
6440: 07         RLCA                    
6441: 18 07      JR      $644A           
6443: 08 86 01   LD      ($0186),SP      
6446: 47         LD      B,A             
6447: 00         NOP                     
6448: C7         RST     0X00            
6449: 00         NOP                     
644A: 26 00      LD      H,$00           
644C: 16 60      LD      D,$60           
644E: 8B         ADC     A,E             
644F: 10 E0      STOP    $E0             
6451: FF         RST     0X38            
6452: E0 FF      LDFF00  ($FF),A         
6454: E0 FF      LDFF00  ($FF),A         
6456: E0 FF      LDFF00  ($FF),A         
6458: E0 FF      LDFF00  ($FF),A         
645A: 70         LD      (HL),B          
645B: 7F         LD      A,A             
645C: 78         LD      A,B             
645D: 7F         LD      A,A             
645E: 1F         RRA                     
645F: 1F         RRA                     
6460: F4         ???                     
6461: BB         CP      E               
6462: F4         ???                     
6463: BB         CP      E               
6464: 47         LD      B,A             
6465: B8         CP      B               
6466: 48         LD      C,B             
6467: B0         OR      B               
6468: F3         DI                      
6469: 07         RLCA                    
646A: 0E 0E      LD      C,$0E           
646C: 03         INC     BC              
646D: FF         RST     0X38            
646E: 00         NOP                     
646F: 0F         RRCA                    
6470: F8 00      LDHL    SP,$00          
6472: 88         ADC     A,B             
6473: 60         LD      H,B             
6474: 84         ADD     A,H             
6475: 68         LD      L,B             
6476: 86         ADD     A,(HL)          
6477: FC         ???                     
6478: 09         ADD     HL,BC           
6479: FE C0      CP      $C0             
647B: FF         RST     0X38            
647C: 00         NOP                     
647D: 7C         LD      A,H             
647E: 00         NOP                     
647F: 00         NOP                     
6480: FF         RST     0X38            
6481: 00         NOP                     
6482: FF         RST     0X38            
6483: 00         NOP                     
6484: BC         CP      H               
6485: 00         NOP                     
6486: 40         LD      B,B             
6487: 24         INC     H               
6488: C1         POP     BC              
6489: 00         NOP                     
648A: 3F         CCF                     
648B: C0         RET     NZ              
648C: 00         NOP                     
648D: 40         LD      B,B             
648E: 00         NOP                     
648F: E2         LDFF00  (C),A           
6490: FC         ???                     
6491: 00         NOP                     
6492: FE 00      CP      $00             
6494: 3F         CCF                     
6495: 00         NOP                     
6496: 00         NOP                     
6497: 00         NOP                     
6498: E0 00      LDFF00  ($00),A         
649A: C7         RST     0X00            
649B: 00         NOP                     
649C: 00         NOP                     
649D: 00         NOP                     
649E: 78         LD      A,B             
649F: 00         NOP                     
64A0: 1F         RRA                     
64A1: 60         LD      H,B             
64A2: 1F         RRA                     
64A3: 00         NOP                     
64A4: 1E 01      LD      E,$01           
64A6: 9F         SBC     A               
64A7: 00         NOP                     
64A8: 5F         LD      E,A             
64A9: 00         NOP                     
64AA: FE 00      CP      $00             
64AC: 76         HALT                    
64AD: 80         ADD     A,B             
64AE: 8B         ADC     A,E             
64AF: 10 00      STOP    $00             
64B1: FF         RST     0X38            
64B2: 00         NOP                     
64B3: FF         RST     0X38            
64B4: 00         NOP                     
64B5: FF         RST     0X38            
64B6: 00         NOP                     
64B7: FF         RST     0X38            
64B8: 04         INC     B               
64B9: FF         RST     0X38            
64BA: 1C         INC     E               
64BB: FF         RST     0X38            
64BC: FC         ???                     
64BD: FF         RST     0X38            
64BE: FC         ???                     
64BF: FF         RST     0X38            
64C0: 8F         ADC     A,A             
64C1: 00         NOP                     
64C2: FF         RST     0X38            
64C3: 00         NOP                     
64C4: DF         RST     0X18            
64C5: 00         NOP                     
64C6: 7F         LD      A,A             
64C7: 00         NOP                     
64C8: 3F         CCF                     
64C9: 00         NOP                     
64CA: 07         RLCA                    
64CB: 00         NOP                     
64CC: 00         NOP                     
64CD: 00         NOP                     
64CE: 40         LD      B,B             
64CF: 00         NOP                     
64D0: FF         RST     0X38            
64D1: 00         NOP                     
64D2: FE 00      CP      $00             
64D4: FB         EI                      
64D5: 00         NOP                     
64D6: FE 00      CP      $00             
64D8: FC         ???                     
64D9: 00         NOP                     
64DA: E1         POP     HL              
64DB: 00         NOP                     
64DC: 00         NOP                     
64DD: 00         NOP                     
64DE: 00         NOP                     
64DF: 00         NOP                     
64E0: FC         ???                     
64E1: 00         NOP                     
64E2: FF         RST     0X38            
64E3: 00         NOP                     
64E4: FF         RST     0X38            
64E5: 00         NOP                     
64E6: FF         RST     0X38            
64E7: 00         NOP                     
64E8: 0F         RRCA                    
64E9: 00         NOP                     
64EA: C1         POP     BC              
64EB: 00         NOP                     
64EC: 00         NOP                     
64ED: 00         NOP                     
64EE: 00         NOP                     
64EF: 00         NOP                     
64F0: 3F         CCF                     
64F1: 00         NOP                     
64F2: FF         RST     0X38            
64F3: 00         NOP                     
64F4: FF         RST     0X38            
64F5: 00         NOP                     
64F6: FF         RST     0X38            
64F7: 00         NOP                     
64F8: F0 00      LD      A,($00)         
64FA: 80         ADD     A,B             
64FB: 00         NOP                     
64FC: 00         NOP                     
64FD: 00         NOP                     
64FE: 00         NOP                     
64FF: 00         NOP                     
6500: 00         NOP                     
6501: 00         NOP                     
6502: 01 00 01   LD      BC,$0100        
6505: 00         NOP                     
6506: 0F         RRCA                    
6507: 00         NOP                     
6508: 78         LD      A,B             
6509: 07         RLCA                    
650A: FC         ???                     
650B: 32         LD      (HLD),A         
650C: FC         ???                     
650D: 78         LD      A,B             
650E: C3 78 E3   JP      $E378           
6511: 10 FF      STOP    $FF             
6513: 00         NOP                     
6514: 33         INC     SP              
6515: 00         NOP                     
6516: 1C         INC     E               
6517: 00         NOP                     
6518: 00         NOP                     
6519: 00         NOP                     
651A: 00         NOP                     
651B: 00         NOP                     
651C: 00         NOP                     
651D: 00         NOP                     
651E: 00         NOP                     
651F: 00         NOP                     
6520: 84         ADD     A,H             
6521: 78         LD      A,B             
6522: 06 C0      LD      B,$C0           
6524: 7F         LD      A,A             
6525: 80         ADD     A,B             
6526: 87         ADD     A,A             
6527: 78         LD      A,B             
6528: 03         INC     BC              
6529: F8 03      LDHL    SP,$03          
652B: C0         RET     NZ              
652C: 1F         RRA                     
652D: 00         NOP                     
652E: FF         RST     0X38            
652F: 00         NOP                     
6530: FF         RST     0X38            
6531: 00         NOP                     
6532: E6 00      AND     $00             
6534: 39         ADD     HL,SP           
6535: 00         NOP                     
6536: 00         NOP                     
6537: 00         NOP                     
6538: 00         NOP                     
6539: 00         NOP                     
653A: 00         NOP                     
653B: 00         NOP                     
653C: 00         NOP                     
653D: 00         NOP                     
653E: 00         NOP                     
653F: 00         NOP                     
6540: 19         ADD     HL,DE           
6541: 00         NOP                     
6542: 01 00 00   LD      BC,$0000        
6545: 00         NOP                     
6546: 00         NOP                     
6547: 00         NOP                     
6548: 80         ADD     A,B             
6549: 00         NOP                     
654A: C0         RET     NZ              
654B: 00         NOP                     
654C: C1         POP     BC              
654D: 00         NOP                     
654E: FF         RST     0X38            
654F: 00         NOP                     
6550: FF         RST     0X38            
6551: 00         NOP                     
6552: 7F         LD      A,A             
6553: 00         NOP                     
6554: F8 00      LDHL    SP,$00          
6556: 1E 00      LD      E,$00           
6558: 3C         INC     A               
6559: 00         NOP                     
655A: 00         NOP                     
655B: 00         NOP                     
655C: 00         NOP                     
655D: 00         NOP                     
655E: 00         NOP                     
655F: 00         NOP                     
6560: 00         NOP                     
6561: 00         NOP                     
6562: 03         INC     BC              
6563: 03         INC     BC              
6564: 07         RLCA                    
6565: 07         RLCA                    
6566: 0F         RRCA                    
6567: 0F         RRCA                    
6568: 1C         INC     E               
6569: 1F         RRA                     
656A: 18 1F      JR      $658B           
656C: 18 1F      JR      $658D           
656E: 1C         INC     E               
656F: 1F         RRA                     
6570: 07         RLCA                    
6571: 07         RLCA                    
6572: 1F         RRA                     
6573: 1F         RRA                     
6574: 1F         RRA                     
6575: 1F         RRA                     
6576: 3C         INC     A               
6577: 3F         CCF                     
6578: 38 3F      JR      C,$65B9         
657A: 30 3F      JR      NC,$65BB        
657C: 30 3F      JR      NC,$65BD        
657E: F0 FF      LD      A,($FF)         
6580: 41         LD      B,C             
6581: B2         OR      D               
6582: 41         LD      B,C             
6583: 00         NOP                     
6584: CF         RST     0X08            
6585: 00         NOP                     
6586: FE 00      CP      $00             
6588: 7E         LD      A,(HL)          
6589: 00         NOP                     
658A: 70         LD      (HL),B          
658B: 00         NOP                     
658C: FC         ???                     
658D: 00         NOP                     
658E: C0         RET     NZ              
658F: 00         NOP                     
6590: C0         RET     NZ              
6591: 00         NOP                     
6592: E0 00      LDFF00  ($00),A         
6594: 00         NOP                     
6595: 00         NOP                     
6596: 00         NOP                     
6597: 00         NOP                     
6598: 00         NOP                     
6599: 00         NOP                     
659A: 00         NOP                     
659B: 00         NOP                     
659C: 00         NOP                     
659D: 00         NOP                     
659E: 00         NOP                     
659F: 00         NOP                     
65A0: 30 00      JR      NC,$65A2        
65A2: 6C         LD      L,H             
65A3: 10 F2      STOP    $F2             
65A5: 6C         LD      L,H             
65A6: F1         POP     AF              
65A7: 26 73      LD      H,$73           
65A9: 00         NOP                     
65AA: 3E 00      LD      A,$00           
65AC: 1C         INC     E               
65AD: 00         NOP                     
65AE: 00         NOP                     
65AF: 00         NOP                     
65B0: 00         NOP                     
65B1: 00         NOP                     
65B2: 00         NOP                     
65B3: 00         NOP                     
65B4: 00         NOP                     
65B5: 00         NOP                     
65B6: 00         NOP                     
65B7: 00         NOP                     
65B8: 00         NOP                     
65B9: 00         NOP                     
65BA: 00         NOP                     
65BB: 00         NOP                     
65BC: 00         NOP                     
65BD: 00         NOP                     
65BE: 00         NOP                     
65BF: 00         NOP                     
65C0: FC         ???                     
65C1: 00         NOP                     
65C2: DF         RST     0X18            
65C3: 00         NOP                     
65C4: FF         RST     0X38            
65C5: 00         NOP                     
65C6: 9F         SBC     A               
65C7: 00         NOP                     
65C8: FF         RST     0X38            
65C9: 00         NOP                     
65CA: 0F         RRCA                    
65CB: 00         NOP                     
65CC: 00         NOP                     
65CD: 00         NOP                     
65CE: 00         NOP                     
65CF: 00         NOP                     
65D0: 7F         LD      A,A             
65D1: 00         NOP                     
65D2: FF         RST     0X38            
65D3: 00         NOP                     
65D4: FF         RST     0X38            
65D5: 00         NOP                     
65D6: F9         LD      SP,HL           
65D7: 00         NOP                     
65D8: FC         ???                     
65D9: 00         NOP                     
65DA: F0 00      LD      A,($00)         
65DC: 00         NOP                     
65DD: 00         NOP                     
65DE: 00         NOP                     
65DF: 00         NOP                     
65E0: FF         RST     0X38            
65E1: 00         NOP                     
65E2: FE 00      CP      $00             
65E4: FF         RST     0X38            
65E5: 00         NOP                     
65E6: FF         RST     0X38            
65E7: 00         NOP                     
65E8: 3F         CCF                     
65E9: 00         NOP                     
65EA: 01 00 80   LD      BC,$8000        
65ED: 00         NOP                     
65EE: 00         NOP                     
65EF: 00         NOP                     
65F0: FF         RST     0X38            
65F1: 00         NOP                     
65F2: 7F         LD      A,A             
65F3: 00         NOP                     
65F4: FF         RST     0X38            
65F5: 00         NOP                     
65F6: FF         RST     0X38            
65F7: 00         NOP                     
65F8: FC         ???                     
65F9: 00         NOP                     
65FA: 80         ADD     A,B             
65FB: 00         NOP                     
65FC: 00         NOP                     
65FD: 00         NOP                     
65FE: 00         NOP                     
65FF: 00         NOP                     
6600: 00         NOP                     
6601: 00         NOP                     
6602: 01 00 01   LD      BC,$0100        
6605: 00         NOP                     
6606: 0F         RRCA                    
6607: 00         NOP                     
6608: 78         LD      A,B             
6609: 07         RLCA                    
660A: FC         ???                     
660B: 32         LD      (HLD),A         
660C: FC         ???                     
660D: 78         LD      A,B             
660E: C3 78 E3   JP      $E378           
6611: 10 FF      STOP    $FF             
6613: 00         NOP                     
6614: 3F         CCF                     
6615: 00         NOP                     
6616: 12         LD      (DE),A          
6617: 00         NOP                     
6618: 08 00 00   LD      ($0000),SP      
661B: 00         NOP                     
661C: 00         NOP                     
661D: 00         NOP                     
661E: 00         NOP                     
661F: 00         NOP                     
6620: 84         ADD     A,H             
6621: 78         LD      A,B             
6622: 06 C0      LD      B,$C0           
6624: 7F         LD      A,A             
6625: 80         ADD     A,B             
6626: 87         ADD     A,A             
6627: 78         LD      A,B             
6628: 03         INC     BC              
6629: F8 03      LDHL    SP,$03          
662B: C0         RET     NZ              
662C: 1F         RRA                     
662D: 00         NOP                     
662E: FF         RST     0X38            
662F: 00         NOP                     
6630: FF         RST     0X38            
6631: 00         NOP                     
6632: FE 00      CP      $00             
6634: C4 00 10   CALL    NZ,$1000        
6637: 00         NOP                     
6638: 00         NOP                     
6639: 00         NOP                     
663A: 00         NOP                     
663B: 00         NOP                     
663C: 00         NOP                     
663D: 00         NOP                     
663E: 00         NOP                     
663F: 00         NOP                     
6640: 19         ADD     HL,DE           
6641: 00         NOP                     
6642: 01 00 00   LD      BC,$0000        
6645: 00         NOP                     
6646: 00         NOP                     
6647: 00         NOP                     
6648: 80         ADD     A,B             
6649: 00         NOP                     
664A: C0         RET     NZ              
664B: 00         NOP                     
664C: C1         POP     BC              
664D: 00         NOP                     
664E: FF         RST     0X38            
664F: 00         NOP                     
6650: FF         RST     0X38            
6651: 00         NOP                     
6652: 0F         RRCA                    
6653: 00         NOP                     
6654: 1F         RRA                     
6655: 00         NOP                     
6656: F0 00      LD      A,($00)         
6658: 0C         INC     C               
6659: 00         NOP                     
665A: 18 00      JR      $665C           
665C: 00         NOP                     
665D: 00         NOP                     
665E: 00         NOP                     
665F: 00         NOP                     
6660: 80         ADD     A,B             
6661: 80         ADD     A,B             
6662: C0         RET     NZ              
6663: C0         RET     NZ              
6664: C0         RET     NZ              
6665: C0         RET     NZ              
6666: E0 E0      LDFF00  ($E0),A         
6668: E0 E0      LDFF00  ($E0),A         
666A: E0 E0      LDFF00  ($E0),A         
666C: 70         LD      (HL),B          
666D: F0 38      LD      A,($38)         
666F: F8 00      LDHL    SP,$00          
6671: 00         NOP                     
6672: 00         NOP                     
6673: 00         NOP                     
6674: 00         NOP                     
6675: 00         NOP                     
6676: E0 E0      LDFF00  ($E0),A         
6678: F8 F8      LDHL    SP,$F8          
667A: F8 F8      LDHL    SP,$F8          
667C: FC         ???                     
667D: FC         ???                     
667E: 7C         LD      A,H             
667F: FC         ???                     
6680: 41         LD      B,C             
6681: B2         OR      D               
6682: 41         LD      B,C             
6683: 00         NOP                     
6684: CF         RST     0X08            
6685: 00         NOP                     
6686: FE 00      CP      $00             
6688: 64         LD      H,H             
6689: 00         NOP                     
668A: 5C         LD      E,H             
668B: 00         NOP                     
668C: E0 00      LDFF00  ($00),A         
668E: D8         RET     C               
668F: 00         NOP                     
6690: C0         RET     NZ              
6691: 00         NOP                     
6692: 00         NOP                     
6693: 00         NOP                     
6694: 80         ADD     A,B             
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
669F: 00         NOP                     
66A0: 00         NOP                     
66A1: 00         NOP                     
66A2: 60         LD      H,B             
66A3: 00         NOP                     
66A4: 98         SBC     B               
66A5: 20 C6      JR      NZ,$666D        
66A7: 08 71 02   LD      ($0271),SP      
66AA: 1D         DEC     E               
66AB: 00         NOP                     
66AC: 0F         RRCA                    
66AD: 00         NOP                     
66AE: 00         NOP                     
66AF: 00         NOP                     
66B0: 00         NOP                     
66B1: 00         NOP                     
66B2: 00         NOP                     
66B3: 00         NOP                     
66B4: 00         NOP                     
66B5: 00         NOP                     
66B6: 00         NOP                     
66B7: 00         NOP                     
66B8: 00         NOP                     
66B9: 00         NOP                     
66BA: 00         NOP                     
66BB: 00         NOP                     
66BC: 00         NOP                     
66BD: 00         NOP                     
66BE: 00         NOP                     
66BF: 00         NOP                     
66C0: FF         RST     0X38            
66C1: 00         NOP                     
66C2: FE 00      CP      $00             
66C4: FF         RST     0X38            
66C5: 00         NOP                     
66C6: FF         RST     0X38            
66C7: 00         NOP                     
66C8: 0F         RRCA                    
66C9: 00         NOP                     
66CA: 61         LD      H,C             
66CB: 00         NOP                     
66CC: 00         NOP                     
66CD: 00         NOP                     
66CE: 00         NOP                     
66CF: 00         NOP                     
66D0: FF         RST     0X38            
66D1: 00         NOP                     
66D2: FF         RST     0X38            
66D3: 00         NOP                     
66D4: FF         RST     0X38            
66D5: 00         NOP                     
66D6: FF         RST     0X38            
66D7: 00         NOP                     
66D8: F0 00      LD      A,($00)         
66DA: 80         ADD     A,B             
66DB: 00         NOP                     
66DC: 00         NOP                     
66DD: 00         NOP                     
66DE: 00         NOP                     
66DF: 00         NOP                     
66E0: FF         RST     0X38            
66E1: 00         NOP                     
66E2: FF         RST     0X38            
66E3: 00         NOP                     
66E4: DE 00      SBC     $00             
66E6: 7F         LD      A,A             
66E7: 00         NOP                     
66E8: 3F         CCF                     
66E9: 00         NOP                     
66EA: 07         RLCA                    
66EB: 00         NOP                     
66EC: 00         NOP                     
66ED: 00         NOP                     
66EE: 80         ADD     A,B             
66EF: 00         NOP                     
66F0: C3 00 FF   JP      $FF00           
66F3: 00         NOP                     
66F4: FB         EI                      
66F5: 00         NOP                     
66F6: FE 00      CP      $00             
66F8: FC         ???                     
66F9: 00         NOP                     
66FA: E0 00      LDFF00  ($00),A         
66FC: 00         NOP                     
66FD: 00         NOP                     
66FE: 00         NOP                     
66FF: 00         NOP                     
6700: 01 01 03   LD      BC,$0301        
6703: 03         INC     BC              
6704: 03         INC     BC              
6705: 03         INC     BC              
6706: 03         INC     BC              
6707: 03         INC     BC              
6708: 3F         CCF                     
6709: 3F         CCF                     
670A: FF         RST     0X38            
670B: FF         RST     0X38            
670C: F0 FF      LD      A,($FF)         
670E: C0         RET     NZ              
670F: FF         RST     0X38            
6710: F0 FF      LD      A,($FF)         
6712: 88         ADC     A,B             
6713: FF         RST     0X38            
6714: 00         NOP                     
6715: FF         RST     0X38            
6716: 00         NOP                     
6717: FF         RST     0X38            
6718: 00         NOP                     
6719: FF         RST     0X38            
671A: 00         NOP                     
671B: FF         RST     0X38            
671C: 80         ADD     A,B             
671D: FF         RST     0X38            
671E: 00         NOP                     
671F: FF         RST     0X38            
6720: 0C         INC     C               
6721: 0F         RRCA                    
6722: 0C         INC     C               
6723: 0F         RRCA                    
6724: 3E 3F      LD      A,$3F           
6726: 7F         LD      A,A             
6727: 7F         LD      A,A             
6728: 78         LD      A,B             
6729: 7F         LD      A,A             
672A: 70         LD      (HL),B          
672B: 7F         LD      A,A             
672C: 60         LD      H,B             
672D: 7F         LD      A,A             
672E: E0 FF      LDFF00  ($FF),A         
6730: 73         LD      (HL),E          
6731: 73         LD      (HL),E          
6732: FF         RST     0X38            
6733: FF         RST     0X38            
6734: FF         RST     0X38            
6735: FF         RST     0X38            
6736: 0D         DEC     C               
6737: FF         RST     0X38            
6738: 00         NOP                     
6739: FF         RST     0X38            
673A: 00         NOP                     
673B: FF         RST     0X38            
673C: 00         NOP                     
673D: FF         RST     0X38            
673E: 00         NOP                     
673F: FF         RST     0X38            
6740: F0 F0      LD      A,($F0)         
6742: F8 F8      LDHL    SP,$F8          
6744: FC         ???                     
6745: FC         ???                     
6746: 1C         INC     E               
6747: FC         ???                     
6748: 0F         RRCA                    
6749: FF         RST     0X38            
674A: 0F         RRCA                    
674B: FF         RST     0X38            
674C: 07         RLCA                    
674D: FF         RST     0X38            
674E: 04         INC     B               
674F: FF         RST     0X38            
6750: 38 F8      JR      C,$674A         
6752: 18 F8      JR      $674C           
6754: 1C         INC     E               
6755: FC         ???                     
6756: 3E FE      LD      A,$FE           
6758: 3E FE      LD      A,$FE           
675A: 0F         RRCA                    
675B: FF         RST     0X38            
675C: 0F         RRCA                    
675D: FF         RST     0X38            
675E: 07         RLCA                    
675F: FF         RST     0X38            
6760: 1C         INC     E               
6761: FC         ???                     
6762: 0D         DEC     C               
6763: FD         ???                     
6764: 0F         RRCA                    
6765: FF         RST     0X38            
6766: 0F         RRCA                    
6767: FF         RST     0X38            
6768: 04         INC     B               
6769: FF         RST     0X38            
676A: 00         NOP                     
676B: FF         RST     0X38            
676C: 00         NOP                     
676D: FF         RST     0X38            
676E: 00         NOP                     
676F: FF         RST     0X38            
6770: 00         NOP                     
6771: 00         NOP                     
6772: C0         RET     NZ              
6773: C0         RET     NZ              
6774: E0 E0      LDFF00  ($E0),A         
6776: F0 F0      LD      A,($F0)         
6778: 70         LD      (HL),B          
6779: F0 3C      LD      A,($3C)         
677B: FC         ???                     
677C: 3E FE      LD      A,$FE           
677E: 0F         RRCA                    
677F: FF         RST     0X38            
6780: 0F         RRCA                    
6781: 0F         RRCA                    
6782: 0E 0F      LD      C,$0F           
6784: 1C         INC     E               
6785: 1F         RRA                     
6786: 1E 1F      LD      E,$1F           
6788: 1E 1F      LD      E,$1F           
678A: 0E 0F      LD      C,$0F           
678C: 0F         RRCA                    
678D: 0F         RRCA                    
678E: 03         INC     BC              
678F: 03         INC     BC              
6790: 00         NOP                     
6791: FF         RST     0X38            
6792: 00         NOP                     
6793: FF         RST     0X38            
6794: 01 FF 02   LD      BC,$02FF        
6797: FF         RST     0X38            
6798: 0E FF      LD      C,$FF           
679A: 3F         CCF                     
679B: FF         RST     0X38            
679C: F7         RST     0X30            
679D: F7         RST     0X30            
679E: C3 C3 FF   JP      $FFC3           
67A1: FF         RST     0X38            
67A2: FF         RST     0X38            
67A3: FF         RST     0X38            
67A4: 3E 3F      LD      A,$3F           
67A6: 06 07      LD      B,$07           
67A8: 07         RLCA                    
67A9: 07         RLCA                    
67AA: 07         RLCA                    
67AB: 07         RLCA                    
67AC: 03         INC     BC              
67AD: 03         INC     BC              
67AE: 03         INC     BC              
67AF: 03         INC     BC              
67B0: EC         ???                     
67B1: EF         RST     0X28            
67B2: 0C         INC     C               
67B3: 0F         RRCA                    
67B4: 0E 0F      LD      C,$0F           
67B6: 0E 0F      LD      C,$0F           
67B8: 07         RLCA                    
67B9: 07         RLCA                    
67BA: 07         RLCA                    
67BB: 07         RLCA                    
67BC: 03         INC     BC              
67BD: 03         INC     BC              
67BE: 01 01 FF   LD      BC,$FF01        
67C1: 00         NOP                     
67C2: FF         RST     0X38            
67C3: 00         NOP                     
67C4: FF         RST     0X38            
67C5: 00         NOP                     
67C6: FF         RST     0X38            
67C7: 00         NOP                     
67C8: 3F         CCF                     
67C9: 00         NOP                     
67CA: 01 00 40   LD      BC,$4000        
67CD: 00         NOP                     
67CE: 00         NOP                     
67CF: 00         NOP                     
67D0: FC         ???                     
67D1: 00         NOP                     
67D2: FF         RST     0X38            
67D3: 00         NOP                     
67D4: FF         RST     0X38            
67D5: 00         NOP                     
67D6: FF         RST     0X38            
67D7: 00         NOP                     
67D8: FD         ???                     
67D9: 00         NOP                     
67DA: 80         ADD     A,B             
67DB: 00         NOP                     
67DC: 00         NOP                     
67DD: 00         NOP                     
67DE: 00         NOP                     
67DF: 00         NOP                     
67E0: 7F         LD      A,A             
67E1: 00         NOP                     
67E2: FF         RST     0X38            
67E3: 00         NOP                     
67E4: FF         RST     0X38            
67E5: 00         NOP                     
67E6: 9E         SBC     (HL)            
67E7: 00         NOP                     
67E8: FF         RST     0X38            
67E9: 00         NOP                     
67EA: 0F         RRCA                    
67EB: 00         NOP                     
67EC: 00         NOP                     
67ED: 00         NOP                     
67EE: 00         NOP                     
67EF: 00         NOP                     
67F0: FF         RST     0X38            
67F1: 00         NOP                     
67F2: E7         RST     0X20            
67F3: 00         NOP                     
67F4: FF         RST     0X38            
67F5: 00         NOP                     
67F6: F9         LD      SP,HL           
67F7: 00         NOP                     
67F8: FC         ???                     
67F9: 00         NOP                     
67FA: F0 00      LD      A,($00)         
67FC: 00         NOP                     
67FD: 00         NOP                     
67FE: 00         NOP                     
67FF: 00         NOP                     
6800: E0 FF      LDFF00  ($FF),A         
6802: F0 FF      LD      A,($FF)         
6804: 7C         LD      A,H             
6805: FF         RST     0X38            
6806: 7F         LD      A,A             
6807: FF         RST     0X38            
6808: 1F         RRA                     
6809: FF         RST     0X38            
680A: 7F         LD      A,A             
680B: FF         RST     0X38            
680C: 9C         SBC     H               
680D: FF         RST     0X38            
680E: CE FF      ADC     $FF             
6810: 00         NOP                     
6811: FF         RST     0X38            
6812: 00         NOP                     
6813: FF         RST     0X38            
6814: 00         NOP                     
6815: FF         RST     0X38            
6816: C0         RET     NZ              
6817: FF         RST     0X38            
6818: E0 FF      LDFF00  ($FF),A         
681A: E0 FF      LDFF00  ($FF),A         
681C: E0 FF      LDFF00  ($FF),A         
681E: 40         LD      B,B             
681F: FF         RST     0X38            
6820: 00         NOP                     
6821: FF         RST     0X38            
6822: 00         NOP                     
6823: FF         RST     0X38            
6824: 00         NOP                     
6825: FF         RST     0X38            
6826: 01 FF 07   LD      BC,$07FF        
6829: FF         RST     0X38            
682A: 0F         RRCA                    
682B: FF         RST     0X38            
682C: 1F         RRA                     
682D: FF         RST     0X38            
682E: 1C         INC     E               
682F: FF         RST     0X38            
6830: 0F         RRCA                    
6831: FF         RST     0X38            
6832: 1F         RRA                     
6833: FF         RST     0X38            
6834: 3E FF      LD      A,$FF           
6836: F8 FF      LDHL    SP,$FF          
6838: F0 FF      LD      A,($FF)         
683A: FE FF      CP      $FF             
683C: EF         RST     0X28            
683D: FF         RST     0X38            
683E: 1E FF      LD      E,$FF           
6840: 3F         CCF                     
6841: 00         NOP                     
6842: 0F         RRCA                    
6843: 00         NOP                     
6844: 07         RLCA                    
6845: 00         NOP                     
6846: 07         RLCA                    
6847: 00         NOP                     
6848: 03         INC     BC              
6849: 00         NOP                     
684A: 03         INC     BC              
684B: 00         NOP                     
684C: 00         NOP                     
684D: 00         NOP                     
684E: 00         NOP                     
684F: 00         NOP                     
6850: 30 FC      JR      NC,$684E        
6852: C0         RET     NZ              
6853: FA 00 E4   LD      A,($E400)       
6856: 00         NOP                     
6857: 39         ADD     HL,SP           
6858: 00         NOP                     
6859: 82         ADD     A,D             
685A: 00         NOP                     
685B: 0C         INC     C               
685C: 00         NOP                     
685D: 00         NOP                     
685E: 00         NOP                     
685F: C0         RET     NZ              
6860: 00         NOP                     
6861: 01 00 01   LD      BC,$0100        
6864: 00         NOP                     
6865: 01 01 02   LD      BC,$0201        
6868: 01 02 01   LD      BC,$0102        
686B: 00         NOP                     
686C: 03         INC     BC              
686D: 04         INC     B               
686E: 07         RLCA                    
686F: 00         NOP                     
6870: 00         NOP                     
6871: 03         INC     BC              
6872: 03         INC     BC              
6873: 04         INC     B               
6874: 07         RLCA                    
6875: 08 07 08   LD      ($0807),SP      
6878: 0F         RRCA                    
6879: 10 1F      STOP    $1F             
687B: 00         NOP                     
687C: 1F         RRA                     
687D: 20 7F      JR      NZ,$68FE        
687F: 80         ADD     A,B             
6880: 00         NOP                     
6881: 80         ADD     A,B             
6882: 80         ADD     A,B             
6883: 40         LD      B,B             
6884: F0 0C      LD      A,($0C)         
6886: FE 01      CP      $01             
6888: FF         RST     0X38            
6889: 00         NOP                     
688A: FF         RST     0X38            
688B: 00         NOP                     
688C: FF         RST     0X38            
688D: 00         NOP                     
688E: FF         RST     0X38            
688F: 00         NOP                     
6890: 00         NOP                     
6891: 00         NOP                     
6892: 00         NOP                     
6893: 00         NOP                     
6894: 00         NOP                     
6895: 00         NOP                     
6896: 00         NOP                     
6897: 00         NOP                     
6898: 80         ADD     A,B             
6899: 00         NOP                     
689A: D0         RET     NC              
689B: 28 FC      JR      Z,$6899         
689D: 02         LD      (BC),A          
689E: FE 01      CP      $01             
68A0: 00         NOP                     
68A1: 80         ADD     A,B             
68A2: 80         ADD     A,B             
68A3: 00         NOP                     
68A4: 80         ADD     A,B             
68A5: 40         LD      B,B             
68A6: C0         RET     NZ              
68A7: 00         NOP                     
68A8: C0         RET     NZ              
68A9: 00         NOP                     
68AA: C0         RET     NZ              
68AB: 20 E0      JR      NZ,$688D        
68AD: 10 F0      STOP    $F0             
68AF: 08 00 10   LD      ($1000),SP      
68B2: 00         NOP                     
68B3: 20 00      JR      NZ,$68B5        
68B5: 08 00 10   LD      ($1000),SP      
68B8: 00         NOP                     
68B9: 20 00      JR      NZ,$68BB        
68BB: 00         NOP                     
68BC: 00         NOP                     
68BD: 00         NOP                     
68BE: 00         NOP                     
68BF: 00         NOP                     
68C0: 08 BF 30   LD      ($30BF),SP      
68C3: FF         RST     0X38            
68C4: 00         NOP                     
68C5: 72         LD      (HL),D          
68C6: 88         ADC     A,B             
68C7: 9C         SBC     H               
68C8: 00         NOP                     
68C9: 61         LD      H,C             
68CA: 00         NOP                     
68CB: 0D         DEC     C               
68CC: 20 20      JR      NZ,$68EE        
68CE: 00         NOP                     
68CF: 00         NOP                     
68D0: 00         NOP                     
68D1: FD         ???                     
68D2: 81         ADD     A,C             
68D3: B3         OR      E               
68D4: 06 DF      LD      B,$DF           
68D6: 00         NOP                     
68D7: 0C         INC     C               
68D8: 10 D8      STOP    $D8             
68DA: 20 2F      JR      NZ,$690B        
68DC: 00         NOP                     
68DD: 00         NOP                     
68DE: 00         NOP                     
68DF: 10 00      STOP    $00             
68E1: FF         RST     0X38            
68E2: 08 0D 20   LD      ($200D),SP      
68E5: 23         INC     HL              
68E6: 00         NOP                     
68E7: 00         NOP                     
68E8: 08 48 00   LD      ($0048),SP      
68EB: 04         INC     B               
68EC: 00         NOP                     
68ED: 00         NOP                     
68EE: 20 20      JR      NZ,$6910        
68F0: 10 FF      STOP    $FF             
68F2: 02         LD      (BC),A          
68F3: 0F         RRCA                    
68F4: 00         NOP                     
68F5: 90         SUB     B               
68F6: 00         NOP                     
68F7: 10 41      STOP    $41             
68F9: 41         LD      B,C             
68FA: 00         NOP                     
68FB: 00         NOP                     
68FC: 00         NOP                     
68FD: 04         INC     B               
68FE: 00         NOP                     
68FF: 40         LD      B,B             
6900: E7         RST     0X20            
6901: FF         RST     0X38            
6902: 07         RLCA                    
6903: FF         RST     0X38            
6904: 03         INC     BC              
6905: FF         RST     0X38            
6906: 07         RLCA                    
6907: FF         RST     0X38            
6908: 3F         CCF                     
6909: FF         RST     0X38            
690A: 0F         RRCA                    
690B: FF         RST     0X38            
690C: 03         INC     BC              
690D: FF         RST     0X38            
690E: 00         NOP                     
690F: FF         RST     0X38            
6910: 80         ADD     A,B             
6911: FF         RST     0X38            
6912: 40         LD      B,B             
6913: FF         RST     0X38            
6914: 40         LD      B,B             
6915: FF         RST     0X38            
6916: FC         ???                     
6917: FF         RST     0X38            
6918: FE FF      CP      $FF             
691A: BF         CP      A               
691B: FF         RST     0X38            
691C: CF         RST     0X08            
691D: FF         RST     0X38            
691E: C3 FF 08   JP      $08FF           
6921: FF         RST     0X38            
6922: 00         NOP                     
6923: FF         RST     0X38            
6924: 00         NOP                     
6925: FF         RST     0X38            
6926: 0C         INC     C               
6927: FF         RST     0X38            
6928: 38 FF      JR      C,$6929         
692A: 79         LD      A,C             
692B: FF         RST     0X38            
692C: 6B         LD      L,E             
692D: FF         RST     0X38            
692E: 67         LD      H,A             
692F: FF         RST     0X38            
6930: 38 FF      JR      C,$6931         
6932: 30 FF      JR      NC,$6933        
6934: 20 FF      JR      NZ,$6935        
6936: 2C         INC     L               
6937: FF         RST     0X38            
6938: 3F         CCF                     
6939: FF         RST     0X38            
693A: FC         ???                     
693B: FF         RST     0X38            
693C: F0 FF      LD      A,($FF)         
693E: 60         LD      H,B             
693F: FF         RST     0X38            
6940: FF         RST     0X38            
6941: 00         NOP                     
6942: FF         RST     0X38            
6943: 00         NOP                     
6944: FF         RST     0X38            
6945: 00         NOP                     
6946: FF         RST     0X38            
6947: 00         NOP                     
6948: FF         RST     0X38            
6949: 00         NOP                     
694A: FF         RST     0X38            
694B: 00         NOP                     
694C: 1F         RRA                     
694D: 00         NOP                     
694E: 07         RLCA                    
694F: 00         NOP                     
6950: FF         RST     0X38            
6951: 00         NOP                     
6952: FF         RST     0X38            
6953: 00         NOP                     
6954: FF         RST     0X38            
6955: 00         NOP                     
6956: FF         RST     0X38            
6957: 00         NOP                     
6958: FF         RST     0X38            
6959: 00         NOP                     
695A: FF         RST     0X38            
695B: 00         NOP                     
695C: FF         RST     0X38            
695D: 00         NOP                     
695E: FF         RST     0X38            
695F: 00         NOP                     
6960: 07         RLCA                    
6961: 00         NOP                     
6962: 0F         RRCA                    
6963: 00         NOP                     
6964: 0F         RRCA                    
6965: 10 1F      STOP    $1F             
6967: 20 3F      JR      NZ,$69A8        
6969: 00         NOP                     
696A: 3F         CCF                     
696B: 40         LD      B,B             
696C: 7F         LD      A,A             
696D: 00         NOP                     
696E: 7F         LD      A,A             
696F: 80         ADD     A,B             
6970: 00         NOP                     
6971: 00         NOP                     
6972: 00         NOP                     
6973: 00         NOP                     
6974: 00         NOP                     
6975: 00         NOP                     
6976: 00         NOP                     
6977: 00         NOP                     
6978: 02         LD      (BC),A          
6979: 01 07 18   LD      BC,$1807        
697C: 3F         CCF                     
697D: 40         LD      B,B             
697E: 7F         LD      A,A             
697F: 80         ADD     A,B             
6980: 00         NOP                     
6981: 01 03 04   LD      BC,$0403        
6984: 07         RLCA                    
6985: 08 1F 20   LD      ($201F),SP      
6988: 7F         LD      A,A             
6989: 80         ADD     A,B             
698A: FF         RST     0X38            
698B: 00         NOP                     
698C: FF         RST     0X38            
698D: 00         NOP                     
698E: FF         RST     0X38            
698F: 00         NOP                     
6990: 00         NOP                     
6991: 80         ADD     A,B             
6992: 80         ADD     A,B             
6993: 40         LD      B,B             
6994: C0         RET     NZ              
6995: 00         NOP                     
6996: E0 10      LDFF00  ($10),A         
6998: F8 04      LDHL    SP,$04          
699A: FC         ???                     
699B: 00         NOP                     
699C: FC         ???                     
699D: 02         LD      (BC),A          
699E: FE 01      CP      $01             
69A0: F8 00      LDHL    SP,$00          
69A2: F8 04      LDHL    SP,$04          
69A4: F8 04      LDHL    SP,$04          
69A6: FC         ???                     
69A7: 00         NOP                     
69A8: FC         ???                     
69A9: 00         NOP                     
69AA: FC         ???                     
69AB: 02         LD      (BC),A          
69AC: FC         ???                     
69AD: 02         LD      (BC),A          
69AE: FE 00      CP      $00             
69B0: 30 3F      JR      NC,$69F1        
69B2: 6C         LD      L,H             
69B3: 7F         LD      A,A             
69B4: 78         LD      A,B             
69B5: 7F         LD      A,A             
69B6: E0 FF      LDFF00  ($FF),A         
69B8: C0         RET     NZ              
69B9: FF         RST     0X38            
69BA: C0         RET     NZ              
69BB: FF         RST     0X38            
69BC: 40         LD      B,B             
69BD: 7F         LD      A,A             
69BE: 60         LD      H,B             
69BF: 7F         LD      A,A             
69C0: 00         NOP                     
69C1: 40         LD      B,B             
69C2: 00         NOP                     
69C3: 04         INC     B               
69C4: 00         NOP                     
69C5: 00         NOP                     
69C6: 00         NOP                     
69C7: 00         NOP                     
69C8: 00         NOP                     
69C9: 00         NOP                     
69CA: 00         NOP                     
69CB: 00         NOP                     
69CC: 00         NOP                     
69CD: 00         NOP                     
69CE: 00         NOP                     
69CF: 00         NOP                     
69D0: 40         LD      B,B             
69D1: 40         LD      B,B             
69D2: 00         NOP                     
69D3: 00         NOP                     
69D4: 00         NOP                     
69D5: 04         INC     B               
69D6: 00         NOP                     
69D7: 40         LD      B,B             
69D8: 00         NOP                     
69D9: 00         NOP                     
69DA: 00         NOP                     
69DB: 00         NOP                     
69DC: 00         NOP                     
69DD: 00         NOP                     
69DE: 00         NOP                     
69DF: 00         NOP                     
69E0: 03         INC     BC              
69E1: 00         NOP                     
69E2: 01 00 01   LD      BC,$0100        
69E5: 00         NOP                     
69E6: 01 00 00   LD      BC,$0000        
69E9: 00         NOP                     
69EA: 00         NOP                     
69EB: 00         NOP                     
69EC: 00         NOP                     
69ED: 00         NOP                     
69EE: 00         NOP                     
69EF: 00         NOP                     
69F0: 18 18      JR      $6A0A           
69F2: 3C         INC     A               
69F3: 3C         INC     A               
69F4: 66         LD      H,(HL)          
69F5: 7E         LD      A,(HL)          
69F6: 42         LD      B,D             
69F7: 42         LD      B,D             
69F8: 81         ADD     A,C             
69F9: 81         ADD     A,C             
69FA: 81         ADD     A,C             
69FB: 81         ADD     A,C             
69FC: 00         NOP                     
69FD: 00         NOP                     
69FE: D7         RST     0X10            
69FF: 81         ADD     A,C             
6A00: 00         NOP                     
6A01: FF         RST     0X38            
6A02: 00         NOP                     
6A03: FF         RST     0X38            
6A04: 00         NOP                     
6A05: FF         RST     0X38            
6A06: 07         RLCA                    
6A07: FF         RST     0X38            
6A08: 03         INC     BC              
6A09: FF         RST     0X38            
6A0A: 70         LD      (HL),B          
6A0B: FF         RST     0X38            
6A0C: 98         SBC     B               
6A0D: FF         RST     0X38            
6A0E: 04         INC     B               
6A0F: FF         RST     0X38            
6A10: 11 FF 09   LD      DE,$09FF        
6A13: FF         RST     0X38            
6A14: 0B         DEC     BC              
6A15: FF         RST     0X38            
6A16: 06 FE      LD      B,$FE           
6A18: CE FE      ADC     $FE             
6A1A: EC         ???                     
6A1B: FC         ???                     
6A1C: 7C         LD      A,H             
6A1D: FC         ???                     
6A1E: 78         LD      A,B             
6A1F: F8 48      LDHL    SP,$48          
6A21: 7F         LD      A,A             
6A22: CE FF      ADC     $FF             
6A24: 9F         SBC     A               
6A25: FF         RST     0X38            
6A26: DC FF F8   CALL    C,$F8FF         
6A29: FF         RST     0X38            
6A2A: 70         LD      (HL),B          
6A2B: 7F         LD      A,A             
6A2C: 71         LD      (HL),C          
6A2D: 7F         LD      A,A             
6A2E: 13         INC     DE              
6A2F: 1F         RRA                     
6A30: 00         NOP                     
6A31: FF         RST     0X38            
6A32: 00         NOP                     
6A33: FF         RST     0X38            
6A34: 04         INC     B               
6A35: FF         RST     0X38            
6A36: 00         NOP                     
6A37: FF         RST     0X38            
6A38: 00         NOP                     
6A39: FF         RST     0X38            
6A3A: 70         LD      (HL),B          
6A3B: FF         RST     0X38            
6A3C: C0         RET     NZ              
6A3D: FF         RST     0X38            
6A3E: 80         ADD     A,B             
6A3F: FF         RST     0X38            
6A40: FF         RST     0X38            
6A41: FF         RST     0X38            
6A42: FF         RST     0X38            
6A43: A4         AND     H               
6A44: A4         AND     H               
6A45: FF         RST     0X38            
6A46: A4         AND     H               
6A47: FF         RST     0X38            
6A48: FF         RST     0X38            
6A49: FF         RST     0X38            
6A4A: FF         RST     0X38            
6A4B: 91         SUB     C               
6A4C: 93         SUB     E               
6A4D: FD         ???                     
6A4E: 93         SUB     E               
6A4F: FD         ???                     
6A50: FF         RST     0X38            
6A51: FF         RST     0X38            
6A52: F8 20      LDHL    SP,$20          
6A54: 35         DEC     (HL)            
6A55: EA 2B F4   LD      ($F42B),A       
6A58: FF         RST     0X38            
6A59: FF         RST     0X38            
6A5A: E6 04      AND     $04             
6A5C: AF         XOR     A               
6A5D: 54         LD      D,H             
6A5E: 9F         SBC     A               
6A5F: 64         LD      H,H             
6A60: FF         RST     0X38            
6A61: FF         RST     0X38            
6A62: 40         LD      B,B             
6A63: 40         LD      B,B             
6A64: D7         RST     0X10            
6A65: 40         LD      B,B             
6A66: FF         RST     0X38            
6A67: 40         LD      B,B             
6A68: FF         RST     0X38            
6A69: FF         RST     0X38            
6A6A: 08 08 7B   LD      ($7B08),SP      
6A6D: 08 FF 08   LD      ($08FF),SP      
6A70: FF         RST     0X38            
6A71: FF         RST     0X38            
6A72: 1F         RRA                     
6A73: 04         INC     B               
6A74: EC         ???                     
6A75: 17         RLA                     
6A76: D4 2F FF   CALL    NC,$FF2F        
6A79: FF         RST     0X38            
6A7A: 67         LD      H,A             
6A7B: 20 F4      JR      NZ,$6A71        
6A7D: 2B         DEC     HL              
6A7E: FA 25 FF   LD      A,($FF25)       
6A81: FF         RST     0X38            
6A82: F5         PUSH    AF              
6A83: 2F         CPL                     
6A84: 25         DEC     H               
6A85: FF         RST     0X38            
6A86: 25         DEC     H               
6A87: FF         RST     0X38            
6A88: FF         RST     0X38            
6A89: FF         RST     0X38            
6A8A: E9         JP      (HL)            
6A8B: 9F         SBC     A               
6A8C: C9         RET                     
6A8D: BF         CP      A               
6A8E: C9         RET                     
6A8F: BF         CP      A               
6A90: FF         RST     0X38            
6A91: FF         RST     0X38            
6A92: 02         LD      (BC),A          
6A93: 02         LD      (BC),A          
6A94: EB         ???                     
6A95: 02         LD      (BC),A          
6A96: FF         RST     0X38            
6A97: 02         LD      (BC),A          
6A98: FF         RST     0X38            
6A99: FF         RST     0X38            
6A9A: 10 10      STOP    $10             
6A9C: DE 10      SBC     $10             
6A9E: FF         RST     0X38            
6A9F: 10 FF      STOP    $FF             
6AA1: 00         NOP                     
6AA2: FF         RST     0X38            
6AA3: 00         NOP                     
6AA4: FF         RST     0X38            
6AA5: 00         NOP                     
6AA6: FE 00      CP      $00             
6AA8: FC         ???                     
6AA9: 00         NOP                     
6AAA: FC         ???                     
6AAB: 00         NOP                     
6AAC: F8 00      LDHL    SP,$00          
6AAE: F8 00      LDHL    SP,$00          
6AB0: FC         ???                     
6AB1: 00         NOP                     
6AB2: E0 00      LDFF00  ($00),A         
6AB4: 00         NOP                     
6AB5: 00         NOP                     
6AB6: 00         NOP                     
6AB7: 00         NOP                     
6AB8: 00         NOP                     
6AB9: 00         NOP                     
6ABA: 00         NOP                     
6ABB: 00         NOP                     
6ABC: 00         NOP                     
6ABD: 00         NOP                     
6ABE: 00         NOP                     
6ABF: 00         NOP                     
6AC0: 00         NOP                     
6AC1: FF         RST     0X38            
6AC2: 00         NOP                     
6AC3: FF         RST     0X38            
6AC4: 07         RLCA                    
6AC5: FF         RST     0X38            
6AC6: 03         INC     BC              
6AC7: FF         RST     0X38            
6AC8: 07         RLCA                    
6AC9: FF         RST     0X38            
6ACA: 0F         RRCA                    
6ACB: FF         RST     0X38            
6ACC: 1E FE      LD      E,$FE           
6ACE: FE FE      CP      $FE             
6AD0: 1F         RRA                     
6AD1: FF         RST     0X38            
6AD2: 3E FE      LD      A,$FE           
6AD4: FC         ???                     
6AD5: FC         ???                     
6AD6: E0 E0      LDFF00  ($E0),A         
6AD8: 00         NOP                     
6AD9: 00         NOP                     
6ADA: 00         NOP                     
6ADB: 00         NOP                     
6ADC: 00         NOP                     
6ADD: 00         NOP                     
6ADE: 00         NOP                     
6ADF: 00         NOP                     
6AE0: 00         NOP                     
6AE1: FF         RST     0X38            
6AE2: 00         NOP                     
6AE3: FF         RST     0X38            
6AE4: 00         NOP                     
6AE5: FF         RST     0X38            
6AE6: 00         NOP                     
6AE7: FF         RST     0X38            
6AE8: 00         NOP                     
6AE9: FF         RST     0X38            
6AEA: 00         NOP                     
6AEB: FF         RST     0X38            
6AEC: 00         NOP                     
6AED: FF         RST     0X38            
6AEE: 00         NOP                     
6AEF: FF         RST     0X38            
6AF0: 3C         INC     A               
6AF1: FC         ???                     
6AF2: 1C         INC     E               
6AF3: FC         ???                     
6AF4: E6 FE      AND     $FE             
6AF6: 37         SCF                     
6AF7: FF         RST     0X38            
6AF8: 0B         DEC     BC              
6AF9: FF         RST     0X38            
6AFA: 03         INC     BC              
6AFB: FF         RST     0X38            
6AFC: 03         INC     BC              
6AFD: FF         RST     0X38            
6AFE: 06 FE      LD      B,$FE           
6B00: 00         NOP                     
6B01: FF         RST     0X38            
6B02: 00         NOP                     
6B03: FF         RST     0X38            
6B04: 00         NOP                     
6B05: FF         RST     0X38            
6B06: 00         NOP                     
6B07: FF         RST     0X38            
6B08: 01 FF 03   LD      BC,$03FF        
6B0B: FF         RST     0X38            
6B0C: 04         INC     B               
6B0D: FC         ???                     
6B0E: 70         LD      (HL),B          
6B0F: F0 38      LD      A,($38)         
6B11: F8 38      LDHL    SP,$38          
6B13: F8 30      LDHL    SP,$30          
6B15: F0 60      LD      A,($60)         
6B17: E0 C0      LDFF00  ($C0),A         
6B19: C0         RET     NZ              
6B1A: 00         NOP                     
6B1B: 00         NOP                     
6B1C: 00         NOP                     
6B1D: 00         NOP                     
6B1E: 00         NOP                     
6B1F: 00         NOP                     
6B20: 33         INC     SP              
6B21: 3F         CCF                     
6B22: 23         INC     HL              
6B23: 3F         CCF                     
6B24: 22         LD      (HLI),A         
6B25: 3F         CCF                     
6B26: 10 1F      STOP    $1F             
6B28: 18 1F      JR      $6B49           
6B2A: 0C         INC     C               
6B2B: 0F         RRCA                    
6B2C: 03         INC     BC              
6B2D: 03         INC     BC              
6B2E: 00         NOP                     
6B2F: 00         NOP                     
6B30: 00         NOP                     
6B31: FF         RST     0X38            
6B32: 0E FF      LD      C,$FF           
6B34: 08 FF 00   LD      ($00FF),SP      
6B37: FF         RST     0X38            
6B38: 20 FF      JR      NZ,$6B39        
6B3A: 50         LD      D,B             
6B3B: DF         RST     0X18            
6B3C: 8C         ADC     A,H             
6B3D: 8F         ADC     A,A             
6B3E: 03         INC     BC              
6B3F: 03         INC     BC              
6B40: FF         RST     0X38            
6B41: FF         RST     0X38            
6B42: FF         RST     0X38            
6B43: FF         RST     0X38            
6B44: FF         RST     0X38            
6B45: FF         RST     0X38            
6B46: FF         RST     0X38            
6B47: FF         RST     0X38            
6B48: FF         RST     0X38            
6B49: FF         RST     0X38            
6B4A: FF         RST     0X38            
6B4B: 91         SUB     C               
6B4C: 93         SUB     E               
6B4D: FD         ???                     
6B4E: 93         SUB     E               
6B4F: FD         ???                     
6B50: FF         RST     0X38            
6B51: FF         RST     0X38            
6B52: FF         RST     0X38            
6B53: FF         RST     0X38            
6B54: FF         RST     0X38            
6B55: FF         RST     0X38            
6B56: FF         RST     0X38            
6B57: FF         RST     0X38            
6B58: FF         RST     0X38            
6B59: FF         RST     0X38            
6B5A: E6 04      AND     $04             
6B5C: AF         XOR     A               
6B5D: 54         LD      D,H             
6B5E: 97         SUB     A               
6B5F: 6C         LD      L,H             
6B60: FF         RST     0X38            
6B61: FF         RST     0X38            
6B62: FF         RST     0X38            
6B63: FF         RST     0X38            
6B64: FF         RST     0X38            
6B65: FF         RST     0X38            
6B66: FF         RST     0X38            
6B67: FF         RST     0X38            
6B68: FF         RST     0X38            
6B69: FF         RST     0X38            
6B6A: 04         INC     B               
6B6B: 04         INC     B               
6B6C: BD         CP      L               
6B6D: 04         INC     B               
6B6E: FF         RST     0X38            
6B6F: 04         INC     B               
6B70: FF         RST     0X38            
6B71: FF         RST     0X38            
6B72: FF         RST     0X38            
6B73: FF         RST     0X38            
6B74: FF         RST     0X38            
6B75: FF         RST     0X38            
6B76: FF         RST     0X38            
6B77: FF         RST     0X38            
6B78: FF         RST     0X38            
6B79: FF         RST     0X38            
6B7A: 67         LD      H,A             
6B7B: 20 F4      JR      NZ,$6B71        
6B7D: 2B         DEC     HL              
6B7E: FA 25 FF   LD      A,($FF25)       
6B81: FF         RST     0X38            
6B82: FF         RST     0X38            
6B83: FF         RST     0X38            
6B84: FF         RST     0X38            
6B85: FF         RST     0X38            
6B86: FF         RST     0X38            
6B87: FF         RST     0X38            
6B88: FF         RST     0X38            
6B89: FF         RST     0X38            
6B8A: ED         ???                     
6B8B: 9B         SBC     E               
6B8C: C9         RET                     
6B8D: BF         CP      A               
6B8E: C9         RET                     
6B8F: BF         CP      A               
6B90: F8 00      LDHL    SP,$00          
6B92: C0         RET     NZ              
6B93: 00         NOP                     
6B94: 80         ADD     A,B             
6B95: 00         NOP                     
6B96: 80         ADD     A,B             
6B97: 00         NOP                     
6B98: 80         ADD     A,B             
6B99: 00         NOP                     
6B9A: 00         NOP                     
6B9B: 00         NOP                     
6B9C: 00         NOP                     
6B9D: 00         NOP                     
6B9E: 00         NOP                     
6B9F: 00         NOP                     
6BA0: FE 00      CP      $00             
6BA2: FC         ???                     
6BA3: 00         NOP                     
6BA4: FC         ???                     
6BA5: 00         NOP                     
6BA6: F8 00      LDHL    SP,$00          
6BA8: F8 00      LDHL    SP,$00          
6BAA: C0         RET     NZ              
6BAB: 00         NOP                     
6BAC: 80         ADD     A,B             
6BAD: 00         NOP                     
6BAE: 00         NOP                     
6BAF: 00         NOP                     
6BB0: 1F         RRA                     
6BB1: 00         NOP                     
6BB2: 0F         RRCA                    
6BB3: 00         NOP                     
6BB4: 0F         RRCA                    
6BB5: 00         NOP                     
6BB6: 07         RLCA                    
6BB7: 00         NOP                     
6BB8: 03         INC     BC              
6BB9: 00         NOP                     
6BBA: 03         INC     BC              
6BBB: 00         NOP                     
6BBC: 01 00 00   LD      BC,$0000        
6BBF: 00         NOP                     
6BC0: 7C         LD      A,H             
6BC1: FC         ???                     
6BC2: 60         LD      H,B             
6BC3: E0 30      LDFF00  ($30),A         
6BC5: F0 30      LD      A,($30)         
6BC7: F0 70      LD      A,($70)         
6BC9: F0 60      LD      A,($60)         
6BCB: E0 E0      LDFF00  ($E0),A         
6BCD: E0 C0      LDFF00  ($C0),A         
6BCF: C0         RET     NZ              
6BD0: 02         LD      (BC),A          
6BD1: FF         RST     0X38            
6BD2: 03         INC     BC              
6BD3: FF         RST     0X38            
6BD4: 07         RLCA                    
6BD5: FF         RST     0X38            
6BD6: 0E FE      LD      C,$FE           
6BD8: 1E FE      LD      E,$FE           
6BDA: FE FE      CP      $FE             
6BDC: FC         ???                     
6BDD: FC         ???                     
6BDE: F0 F0      LD      A,($F0)         
6BE0: 07         RLCA                    
6BE1: FF         RST     0X38            
6BE2: 07         RLCA                    
6BE3: FF         RST     0X38            
6BE4: 07         RLCA                    
6BE5: FF         RST     0X38            
6BE6: 0E FE      LD      C,$FE           
6BE8: 1C         INC     E               
6BE9: FC         ???                     
6BEA: 18 F8      JR      $6BE4           
6BEC: 38 F8      JR      C,$6BE6         
6BEE: 38 F8      JR      C,$6BE8         
6BF0: F8 F8      LDHL    SP,$F8          
6BF2: F0 F0      LD      A,($F0)         
6BF4: E0 E0      LDFF00  ($E0),A         
6BF6: 00         NOP                     
6BF7: 00         NOP                     
6BF8: 00         NOP                     
6BF9: 00         NOP                     
6BFA: 00         NOP                     
6BFB: 00         NOP                     
6BFC: 00         NOP                     
6BFD: 00         NOP                     
6BFE: 00         NOP                     
6BFF: 00         NOP                     
6C00: 30 3F      JR      NC,$6C41        
6C02: 18 1F      JR      $6C23           
6C04: 0E 0F      LD      C,$0F           
6C06: 01 01 00   LD      BC,$0001        
6C09: 00         NOP                     
6C0A: 00         NOP                     
6C0B: 00         NOP                     
6C0C: 00         NOP                     
6C0D: 00         NOP                     
6C0E: 00         NOP                     
6C0F: 00         NOP                     
6C10: 00         NOP                     
6C11: FF         RST     0X38            
6C12: 00         NOP                     
6C13: FF         RST     0X38            
6C14: 00         NOP                     
6C15: FF         RST     0X38            
6C16: 07         RLCA                    
6C17: FF         RST     0X38            
6C18: F8 F8      LDHL    SP,$F8          
6C1A: 00         NOP                     
6C1B: 00         NOP                     
6C1C: 00         NOP                     
6C1D: 00         NOP                     
6C1E: 00         NOP                     
6C1F: 00         NOP                     
6C20: 00         NOP                     
6C21: FF         RST     0X38            
6C22: 00         NOP                     
6C23: FF         RST     0X38            
6C24: 00         NOP                     
6C25: FF         RST     0X38            
6C26: 80         ADD     A,B             
6C27: FF         RST     0X38            
6C28: 40         LD      B,B             
6C29: 7F         LD      A,A             
6C2A: 30 3F      JR      NC,$6C6B        
6C2C: 0F         RRCA                    
6C2D: 0F         RRCA                    
6C2E: 00         NOP                     
6C2F: 00         NOP                     
6C30: 00         NOP                     
6C31: FF         RST     0X38            
6C32: 00         NOP                     
6C33: FF         RST     0X38            
6C34: 00         NOP                     
6C35: FF         RST     0X38            
6C36: 00         NOP                     
6C37: FF         RST     0X38            
6C38: 00         NOP                     
6C39: FF         RST     0X38            
6C3A: 00         NOP                     
6C3B: FF         RST     0X38            
6C3C: F1         POP     AF              
6C3D: FF         RST     0X38            
6C3E: 0E 0E      LD      C,$0E           
6C40: FF         RST     0X38            
6C41: 00         NOP                     
6C42: FF         RST     0X38            
6C43: 42         LD      B,D             
6C44: FF         RST     0X38            
6C45: 24         INC     H               
6C46: FF         RST     0X38            
6C47: 18 FF      JR      $6C48           
6C49: 18 FF      JR      $6C4A           
6C4B: 24         INC     H               
6C4C: FF         RST     0X38            
6C4D: 42         LD      B,D             
6C4E: FF         RST     0X38            
6C4F: 00         NOP                     
6C50: E0 FF      LDFF00  ($FF),A         
6C52: E0 FF      LDFF00  ($FF),A         
6C54: E0 FF      LDFF00  ($FF),A         
6C56: E0 FF      LDFF00  ($FF),A         
6C58: E0 FF      LDFF00  ($FF),A         
6C5A: 70         LD      (HL),B          
6C5B: 7F         LD      A,A             
6C5C: 78         LD      A,B             
6C5D: 7F         LD      A,A             
6C5E: 1F         RRA                     
6C5F: 1F         RRA                     
6C60: FF         RST     0X38            
6C61: 00         NOP                     
6C62: FF         RST     0X38            
6C63: 42         LD      B,D             
6C64: FF         RST     0X38            
6C65: 24         INC     H               
6C66: FF         RST     0X38            
6C67: 18 FF      JR      $6C68           
6C69: 18 FF      JR      $6C6A           
6C6B: 24         INC     H               
6C6C: FF         RST     0X38            
6C6D: 42         LD      B,D             
6C6E: FF         RST     0X38            
6C6F: 00         NOP                     
6C70: FF         RST     0X38            
6C71: 00         NOP                     
6C72: FF         RST     0X38            
6C73: 42         LD      B,D             
6C74: FF         RST     0X38            
6C75: 24         INC     H               
6C76: FF         RST     0X38            
6C77: 18 FF      JR      $6C78           
6C79: 18 FF      JR      $6C7A           
6C7B: 24         INC     H               
6C7C: FF         RST     0X38            
6C7D: 42         LD      B,D             
6C7E: FF         RST     0X38            
6C7F: 00         NOP                     
6C80: FF         RST     0X38            
6C81: 00         NOP                     
6C82: FF         RST     0X38            
6C83: 42         LD      B,D             
6C84: FF         RST     0X38            
6C85: 24         INC     H               
6C86: FF         RST     0X38            
6C87: 18 FF      JR      $6C88           
6C89: 18 FF      JR      $6C8A           
6C8B: 24         INC     H               
6C8C: FF         RST     0X38            
6C8D: 42         LD      B,D             
6C8E: FF         RST     0X38            
6C8F: 00         NOP                     
6C90: FF         RST     0X38            
6C91: 00         NOP                     
6C92: FF         RST     0X38            
6C93: 42         LD      B,D             
6C94: FF         RST     0X38            
6C95: 24         INC     H               
6C96: FF         RST     0X38            
6C97: 18 FF      JR      $6C98           
6C99: 18 FF      JR      $6C9A           
6C9B: 24         INC     H               
6C9C: FF         RST     0X38            
6C9D: 42         LD      B,D             
6C9E: FF         RST     0X38            
6C9F: 00         NOP                     
6CA0: FF         RST     0X38            
6CA1: 00         NOP                     
6CA2: FF         RST     0X38            
6CA3: 42         LD      B,D             
6CA4: FF         RST     0X38            
6CA5: 24         INC     H               
6CA6: FF         RST     0X38            
6CA7: 18 FF      JR      $6CA8           
6CA9: 18 FF      JR      $6CAA           
6CAB: 24         INC     H               
6CAC: FF         RST     0X38            
6CAD: 42         LD      B,D             
6CAE: FF         RST     0X38            
6CAF: 00         NOP                     
6CB0: 00         NOP                     
6CB1: FF         RST     0X38            
6CB2: 00         NOP                     
6CB3: FF         RST     0X38            
6CB4: 00         NOP                     
6CB5: FF         RST     0X38            
6CB6: 00         NOP                     
6CB7: FF         RST     0X38            
6CB8: 04         INC     B               
6CB9: FF         RST     0X38            
6CBA: 1C         INC     E               
6CBB: FF         RST     0X38            
6CBC: FC         ???                     
6CBD: FF         RST     0X38            
6CBE: FC         ???                     
6CBF: FF         RST     0X38            
6CC0: 8F         ADC     A,A             
6CC1: 00         NOP                     
6CC2: FF         RST     0X38            
6CC3: 00         NOP                     
6CC4: DF         RST     0X18            
6CC5: 00         NOP                     
6CC6: 7F         LD      A,A             
6CC7: 00         NOP                     
6CC8: 3F         CCF                     
6CC9: 00         NOP                     
6CCA: 07         RLCA                    
6CCB: 00         NOP                     
6CCC: 00         NOP                     
6CCD: 00         NOP                     
6CCE: 40         LD      B,B             
6CCF: 00         NOP                     
6CD0: FF         RST     0X38            
6CD1: 00         NOP                     
6CD2: FE 00      CP      $00             
6CD4: FB         EI                      
6CD5: 00         NOP                     
6CD6: FE 00      CP      $00             
6CD8: FC         ???                     
6CD9: 00         NOP                     
6CDA: E1         POP     HL              
6CDB: 00         NOP                     
6CDC: 00         NOP                     
6CDD: 00         NOP                     
6CDE: 00         NOP                     
6CDF: 00         NOP                     
6CE0: FC         ???                     
6CE1: 00         NOP                     
6CE2: FF         RST     0X38            
6CE3: 00         NOP                     
6CE4: FF         RST     0X38            
6CE5: 00         NOP                     
6CE6: FF         RST     0X38            
6CE7: 00         NOP                     
6CE8: 0F         RRCA                    
6CE9: 00         NOP                     
6CEA: C1         POP     BC              
6CEB: 00         NOP                     
6CEC: 00         NOP                     
6CED: 00         NOP                     
6CEE: 00         NOP                     
6CEF: 00         NOP                     
6CF0: 3F         CCF                     
6CF1: 00         NOP                     
6CF2: FF         RST     0X38            
6CF3: 00         NOP                     
6CF4: FF         RST     0X38            
6CF5: 00         NOP                     
6CF6: FF         RST     0X38            
6CF7: 00         NOP                     
6CF8: F0 00      LD      A,($00)         
6CFA: 80         ADD     A,B             
6CFB: 00         NOP                     
6CFC: 00         NOP                     
6CFD: 00         NOP                     
6CFE: 00         NOP                     
6CFF: 00         NOP                     
6D00: 00         NOP                     
6D01: 00         NOP                     
6D02: 00         NOP                     
6D03: 00         NOP                     
6D04: 00         NOP                     
6D05: 00         NOP                     
6D06: 00         NOP                     
6D07: 00         NOP                     
6D08: 00         NOP                     
6D09: 00         NOP                     
6D0A: 01 01 0F   LD      BC,$0F01        
6D0D: 0F         RRCA                    
6D0E: 3F         CCF                     
6D0F: 3F         CCF                     
6D10: 00         NOP                     
6D11: 00         NOP                     
6D12: 00         NOP                     
6D13: 00         NOP                     
6D14: 00         NOP                     
6D15: 00         NOP                     
6D16: 00         NOP                     
6D17: 00         NOP                     
6D18: 03         INC     BC              
6D19: 03         INC     BC              
6D1A: C7         RST     0X00            
6D1B: C7         RST     0X00            
6D1C: FF         RST     0X38            
6D1D: FF         RST     0X38            
6D1E: F8 FF      LDHL    SP,$FF          
6D20: 00         NOP                     
6D21: 00         NOP                     
6D22: 00         NOP                     
6D23: 00         NOP                     
6D24: 00         NOP                     
6D25: 00         NOP                     
6D26: 38 38      JR      C,$6D60         
6D28: FC         ???                     
6D29: FC         ???                     
6D2A: FF         RST     0X38            
6D2B: FF         RST     0X38            
6D2C: 1F         RRA                     
6D2D: FF         RST     0X38            
6D2E: 59         LD      E,C             
6D2F: FF         RST     0X38            
6D30: 00         NOP                     
6D31: 00         NOP                     
6D32: 00         NOP                     
6D33: 00         NOP                     
6D34: 00         NOP                     
6D35: 00         NOP                     
6D36: 00         NOP                     
6D37: 00         NOP                     
6D38: 00         NOP                     
6D39: 00         NOP                     
6D3A: 00         NOP                     
6D3B: 00         NOP                     
6D3C: B0         OR      B               
6D3D: B0         OR      B               
6D3E: FC         ???                     
6D3F: FC         ???                     
6D40: 00         NOP                     
6D41: FF         RST     0X38            
6D42: 00         NOP                     
6D43: FF         RST     0X38            
6D44: 00         NOP                     
6D45: FF         RST     0X38            
6D46: 0F         RRCA                    
6D47: FF         RST     0X38            
6D48: 19         ADD     HL,DE           
6D49: F9         LD      SP,HL           
6D4A: 70         LD      (HL),B          
6D4B: F0 C0      LD      A,($C0)         
6D4D: C0         RET     NZ              
6D4E: 00         NOP                     
6D4F: 00         NOP                     
6D50: 0C         INC     C               
6D51: FC         ???                     
6D52: 08 F8 18   LD      ($18F8),SP      
6D55: F8 30      LDHL    SP,$30          
6D57: F0 E0      LD      A,($E0)         
6D59: E0 00      LDFF00  ($00),A         
6D5B: 00         NOP                     
6D5C: 00         NOP                     
6D5D: 00         NOP                     
6D5E: 00         NOP                     
6D5F: 00         NOP                     
6D60: 00         NOP                     
6D61: 00         NOP                     
6D62: 03         INC     BC              
6D63: 03         INC     BC              
6D64: 07         RLCA                    
6D65: 07         RLCA                    
6D66: 0F         RRCA                    
6D67: 0F         RRCA                    
6D68: 1C         INC     E               
6D69: 1F         RRA                     
6D6A: 18 1F      JR      $6D8B           
6D6C: 18 1F      JR      $6D8D           
6D6E: 1C         INC     E               
6D6F: 1F         RRA                     
6D70: 07         RLCA                    
6D71: 07         RLCA                    
6D72: 1F         RRA                     
6D73: 1F         RRA                     
6D74: 1F         RRA                     
6D75: 1F         RRA                     
6D76: 3C         INC     A               
6D77: 3F         CCF                     
6D78: 38 3F      JR      C,$6DB9         
6D7A: 30 3F      JR      NC,$6DBB        
6D7C: 30 3F      JR      NC,$6DBD        
6D7E: F0 FF      LD      A,($FF)         
6D80: 00         NOP                     
6D81: 00         NOP                     
6D82: 01 01 0F   LD      BC,$0F01        
6D85: 0F         RRCA                    
6D86: 1F         RRA                     
6D87: 1F         RRA                     
6D88: 7F         LD      A,A             
6D89: 7F         LD      A,A             
6D8A: F8 FF      LDHL    SP,$FF          
6D8C: 60         LD      H,B             
6D8D: 7F         LD      A,A             
6D8E: E1         POP     HL              
6D8F: FF         RST     0X38            
6D90: 03         INC     BC              
6D91: 03         INC     BC              
6D92: 8F         ADC     A,A             
6D93: 8F         ADC     A,A             
6D94: FF         RST     0X38            
6D95: FF         RST     0X38            
6D96: FF         RST     0X38            
6D97: FF         RST     0X38            
6D98: FF         RST     0X38            
6D99: FF         RST     0X38            
6D9A: 3F         CCF                     
6D9B: FF         RST     0X38            
6D9C: FE FF      CP      $FF             
6D9E: 83         ADD     A,E             
6D9F: FF         RST     0X38            
6DA0: E0 E0      LDFF00  ($E0),A         
6DA2: F0 F0      LD      A,($F0)         
6DA4: FF         RST     0X38            
6DA5: FF         RST     0X38            
6DA6: FF         RST     0X38            
6DA7: FF         RST     0X38            
6DA8: F8 FF      LDHL    SP,$FF          
6DAA: C3 FF 07   JP      $07FF           
6DAD: FF         RST     0X38            
6DAE: 84         ADD     A,H             
6DAF: FF         RST     0X38            
6DB0: 01 01 FF   LD      BC,$FF01        
6DB3: FF         RST     0X38            
6DB4: FF         RST     0X38            
6DB5: FF         RST     0X38            
6DB6: FF         RST     0X38            
6DB7: FF         RST     0X38            
6DB8: FF         RST     0X38            
6DB9: FF         RST     0X38            
6DBA: F8 FF      LDHL    SP,$FF          
6DBC: 0E FF      LD      C,$FF           
6DBE: 02         LD      (BC),A          
6DBF: FF         RST     0X38            
6DC0: C0         RET     NZ              
6DC1: C0         RET     NZ              
6DC2: FC         ???                     
6DC3: FC         ???                     
6DC4: FF         RST     0X38            
6DC5: FF         RST     0X38            
6DC6: FF         RST     0X38            
6DC7: FF         RST     0X38            
6DC8: FF         RST     0X38            
6DC9: FF         RST     0X38            
6DCA: 1E FF      LD      E,$FF           
6DCC: 07         RLCA                    
6DCD: FF         RST     0X38            
6DCE: 08 FF 00   LD      ($00FF),SP      
6DD1: 00         NOP                     
6DD2: 00         NOP                     
6DD3: 00         NOP                     
6DD4: 00         NOP                     
6DD5: 00         NOP                     
6DD6: F0 F0      LD      A,($F0)         
6DD8: FC         ???                     
6DD9: FC         ???                     
6DDA: 3E FE      LD      A,$FE           
6DDC: 1E FE      LD      E,$FE           
6DDE: 8F         ADC     A,A             
6DDF: FF         RST     0X38            
6DE0: FF         RST     0X38            
6DE1: 00         NOP                     
6DE2: FF         RST     0X38            
6DE3: 42         LD      B,D             
6DE4: FF         RST     0X38            
6DE5: 24         INC     H               
6DE6: FF         RST     0X38            
6DE7: 18 FF      JR      $6DE8           
6DE9: 18 FF      JR      $6DEA           
6DEB: 24         INC     H               
6DEC: FF         RST     0X38            
6DED: 42         LD      B,D             
6DEE: FF         RST     0X38            
6DEF: 00         NOP                     
6DF0: FF         RST     0X38            
6DF1: 00         NOP                     
6DF2: FF         RST     0X38            
6DF3: 42         LD      B,D             
6DF4: FF         RST     0X38            
6DF5: 24         INC     H               
6DF6: FF         RST     0X38            
6DF7: 18 FF      JR      $6DF8           
6DF9: 18 FF      JR      $6DFA           
6DFB: 24         INC     H               
6DFC: FF         RST     0X38            
6DFD: 42         LD      B,D             
6DFE: FF         RST     0X38            
6DFF: 00         NOP                     
6E00: 7F         LD      A,A             
6E01: 7F         LD      A,A             
6E02: E8 FF      ADD     SP,$FF          
6E04: 81         ADD     A,C             
6E05: FF         RST     0X38            
6E06: 40         LD      B,B             
6E07: 7F         LD      A,A             
6E08: 00         NOP                     
6E09: 3F         CCF                     
6E0A: 00         NOP                     
6E0B: 07         RLCA                    
6E0C: 00         NOP                     
6E0D: 00         NOP                     
6E0E: 00         NOP                     
6E0F: 00         NOP                     
6E10: AD         XOR     L               
6E11: FF         RST     0X38            
6E12: 63         LD      H,E             
6E13: FF         RST     0X38            
6E14: F8 FF      LDHL    SP,$FF          
6E16: 08 FF 00   LD      ($00FF),SP      
6E19: FF         RST     0X38            
6E1A: 00         NOP                     
6E1B: BF         CP      A               
6E1C: 00         NOP                     
6E1D: 07         RLCA                    
6E1E: 00         NOP                     
6E1F: 00         NOP                     
6E20: C3 FF 07   JP      $07FF           
6E23: FF         RST     0X38            
6E24: 08 FF 00   LD      ($00FF),SP      
6E27: FF         RST     0X38            
6E28: 00         NOP                     
6E29: FF         RST     0X38            
6E2A: 00         NOP                     
6E2B: EF         RST     0X28            
6E2C: 00         NOP                     
6E2D: 86         ADD     A,(HL)          
6E2E: 00         NOP                     
6E2F: 00         NOP                     
6E30: 9E         SBC     (HL)            
6E31: FE CF      CP      $CF             
6E33: FF         RST     0X38            
6E34: 47         LD      B,A             
6E35: FF         RST     0X38            
6E36: 03         INC     BC              
6E37: FF         RST     0X38            
6E38: 00         NOP                     
6E39: FE 00      CP      $00             
6E3B: BE         CP      (HL)            
6E3C: 00         NOP                     
6E3D: 00         NOP                     
6E3E: 00         NOP                     
6E3F: 00         NOP                     
6E40: 07         RLCA                    
6E41: 07         RLCA                    
6E42: 3F         CCF                     
6E43: 3F         CCF                     
6E44: 7C         LD      A,H             
6E45: 7F         LD      A,A             
6E46: C6 FF      ADD     $FF             
6E48: 08 FF 00   LD      ($00FF),SP      
6E4B: 7F         LD      A,A             
6E4C: 00         NOP                     
6E4D: 1E 00      LD      E,$00           
6E4F: 00         NOP                     
6E50: C0         RET     NZ              
6E51: C0         RET     NZ              
6E52: F0 F0      LD      A,($F0)         
6E54: 3E FE      LD      A,$FE           
6E56: 0F         RRCA                    
6E57: FF         RST     0X38            
6E58: 60         LD      H,B             
6E59: FF         RST     0X38            
6E5A: 00         NOP                     
6E5B: FF         RST     0X38            
6E5C: 00         NOP                     
6E5D: F8 00      LDHL    SP,$00          
6E5F: 00         NOP                     
6E60: 80         ADD     A,B             
6E61: 80         ADD     A,B             
6E62: C0         RET     NZ              
6E63: C0         RET     NZ              
6E64: C0         RET     NZ              
6E65: C0         RET     NZ              
6E66: E0 E0      LDFF00  ($E0),A         
6E68: E0 E0      LDFF00  ($E0),A         
6E6A: E0 E0      LDFF00  ($E0),A         
6E6C: 70         LD      (HL),B          
6E6D: F0 38      LD      A,($38)         
6E6F: F8 00      LDHL    SP,$00          
6E71: 00         NOP                     
6E72: 00         NOP                     
6E73: 00         NOP                     
6E74: 00         NOP                     
6E75: 00         NOP                     
6E76: E0 E0      LDFF00  ($E0),A         
6E78: F8 F8      LDHL    SP,$F8          
6E7A: F8 F8      LDHL    SP,$F8          
6E7C: FC         ???                     
6E7D: FC         ???                     
6E7E: 7C         LD      A,H             
6E7F: FC         ???                     
6E80: 40         LD      B,B             
6E81: 7F         LD      A,A             
6E82: 40         LD      B,B             
6E83: 7F         LD      A,A             
6E84: 20 3F      JR      NZ,$6EC5        
6E86: 18 1F      JR      $6EA7           
6E88: 07         RLCA                    
6E89: 07         RLCA                    
6E8A: 00         NOP                     
6E8B: 00         NOP                     
6E8C: 00         NOP                     
6E8D: 00         NOP                     
6E8E: 00         NOP                     
6E8F: 00         NOP                     
6E90: 00         NOP                     
6E91: FF         RST     0X38            
6E92: 00         NOP                     
6E93: FF         RST     0X38            
6E94: 00         NOP                     
6E95: FF         RST     0X38            
6E96: 00         NOP                     
6E97: FF         RST     0X38            
6E98: C0         RET     NZ              
6E99: FF         RST     0X38            
6E9A: 3B         DEC     SP              
6E9B: 3F         CCF                     
6E9C: 00         NOP                     
6E9D: 00         NOP                     
6E9E: 00         NOP                     
6E9F: 00         NOP                     
6EA0: C0         RET     NZ              
6EA1: FF         RST     0X38            
6EA2: 00         NOP                     
6EA3: FF         RST     0X38            
6EA4: 00         NOP                     
6EA5: FF         RST     0X38            
6EA6: 00         NOP                     
6EA7: FF         RST     0X38            
6EA8: 00         NOP                     
6EA9: FF         RST     0X38            
6EAA: B0         OR      B               
6EAB: FF         RST     0X38            
6EAC: 0C         INC     C               
6EAD: 0F         RRCA                    
6EAE: 03         INC     BC              
6EAF: 03         INC     BC              
6EB0: 00         NOP                     
6EB1: FF         RST     0X38            
6EB2: 00         NOP                     
6EB3: FF         RST     0X38            
6EB4: 00         NOP                     
6EB5: FF         RST     0X38            
6EB6: 00         NOP                     
6EB7: FF         RST     0X38            
6EB8: 07         RLCA                    
6EB9: FF         RST     0X38            
6EBA: 00         NOP                     
6EBB: FC         ???                     
6EBC: 30 F0      JR      NC,$6EAE        
6EBE: 80         ADD     A,B             
6EBF: 80         ADD     A,B             
6EC0: 00         NOP                     
6EC1: FF         RST     0X38            
6EC2: 00         NOP                     
6EC3: FF         RST     0X38            
6EC4: 01 FF 08   LD      BC,$08FF        
6EC7: F8 80      LDHL    SP,$80          
6EC9: C0         RET     NZ              
6ECA: 00         NOP                     
6ECB: 00         NOP                     
6ECC: 00         NOP                     
6ECD: 00         NOP                     
6ECE: 00         NOP                     
6ECF: 00         NOP                     
6ED0: 01 FF 06   LD      BC,$06FF        
6ED3: FE 00      CP      $00             
6ED5: FC         ???                     
6ED6: A0         AND     B               
6ED7: F0 00      LD      A,($00)         
6ED9: 00         NOP                     
6EDA: 00         NOP                     
6EDB: 00         NOP                     
6EDC: 00         NOP                     
6EDD: 00         NOP                     
6EDE: 00         NOP                     
6EDF: 00         NOP                     
6EE0: FF         RST     0X38            
6EE1: 00         NOP                     
6EE2: FF         RST     0X38            
6EE3: 42         LD      B,D             
6EE4: FF         RST     0X38            
6EE5: 24         INC     H               
6EE6: FF         RST     0X38            
6EE7: 18 FF      JR      $6EE8           
6EE9: 18 FF      JR      $6EEA           
6EEB: 24         INC     H               
6EEC: FF         RST     0X38            
6EED: 42         LD      B,D             
6EEE: FF         RST     0X38            
6EEF: 00         NOP                     
6EF0: FF         RST     0X38            
6EF1: 00         NOP                     
6EF2: FF         RST     0X38            
6EF3: 42         LD      B,D             
6EF4: FF         RST     0X38            
6EF5: 24         INC     H               
6EF6: FF         RST     0X38            
6EF7: 18 FF      JR      $6EF8           
6EF9: 18 FF      JR      $6EFA           
6EFB: 24         INC     H               
6EFC: FF         RST     0X38            
6EFD: 42         LD      B,D             
6EFE: FF         RST     0X38            
6EFF: 00         NOP                     
6F00: 01 01 03   LD      BC,$0301        
6F03: 03         INC     BC              
6F04: 03         INC     BC              
6F05: 03         INC     BC              
6F06: 03         INC     BC              
6F07: 03         INC     BC              
6F08: 3F         CCF                     
6F09: 3F         CCF                     
6F0A: FF         RST     0X38            
6F0B: FF         RST     0X38            
6F0C: F0 FF      LD      A,($FF)         
6F0E: C0         RET     NZ              
6F0F: FF         RST     0X38            
6F10: F0 FF      LD      A,($FF)         
6F12: 88         ADC     A,B             
6F13: FF         RST     0X38            
6F14: 00         NOP                     
6F15: FF         RST     0X38            
6F16: 00         NOP                     
6F17: FF         RST     0X38            
6F18: 00         NOP                     
6F19: FF         RST     0X38            
6F1A: 00         NOP                     
6F1B: FF         RST     0X38            
6F1C: 80         ADD     A,B             
6F1D: FF         RST     0X38            
6F1E: 00         NOP                     
6F1F: FF         RST     0X38            
6F20: 0C         INC     C               
6F21: 0F         RRCA                    
6F22: 0C         INC     C               
6F23: 0F         RRCA                    
6F24: 3E 3F      LD      A,$3F           
6F26: 7F         LD      A,A             
6F27: 7F         LD      A,A             
6F28: 78         LD      A,B             
6F29: 7F         LD      A,A             
6F2A: 70         LD      (HL),B          
6F2B: 7F         LD      A,A             
6F2C: 60         LD      H,B             
6F2D: 7F         LD      A,A             
6F2E: E0 FF      LDFF00  ($FF),A         
6F30: 73         LD      (HL),E          
6F31: 73         LD      (HL),E          
6F32: FF         RST     0X38            
6F33: FF         RST     0X38            
6F34: FF         RST     0X38            
6F35: FF         RST     0X38            
6F36: 0D         DEC     C               
6F37: FF         RST     0X38            
6F38: 00         NOP                     
6F39: FF         RST     0X38            
6F3A: 00         NOP                     
6F3B: FF         RST     0X38            
6F3C: 00         NOP                     
6F3D: FF         RST     0X38            
6F3E: 00         NOP                     
6F3F: FF         RST     0X38            
6F40: F0 F0      LD      A,($F0)         
6F42: F8 F8      LDHL    SP,$F8          
6F44: FC         ???                     
6F45: FC         ???                     
6F46: 1C         INC     E               
6F47: FC         ???                     
6F48: 0F         RRCA                    
6F49: FF         RST     0X38            
6F4A: 0F         RRCA                    
6F4B: FF         RST     0X38            
6F4C: 07         RLCA                    
6F4D: FF         RST     0X38            
6F4E: 04         INC     B               
6F4F: FF         RST     0X38            
6F50: 38 F8      JR      C,$6F4A         
6F52: 18 F8      JR      $6F4C           
6F54: 1C         INC     E               
6F55: FC         ???                     
6F56: 3E FE      LD      A,$FE           
6F58: 3E FE      LD      A,$FE           
6F5A: 0F         RRCA                    
6F5B: FF         RST     0X38            
6F5C: 0F         RRCA                    
6F5D: FF         RST     0X38            
6F5E: 07         RLCA                    
6F5F: FF         RST     0X38            
6F60: 1C         INC     E               
6F61: FC         ???                     
6F62: 0D         DEC     C               
6F63: FD         ???                     
6F64: 0F         RRCA                    
6F65: FF         RST     0X38            
6F66: 0F         RRCA                    
6F67: FF         RST     0X38            
6F68: 04         INC     B               
6F69: FF         RST     0X38            
6F6A: 00         NOP                     
6F6B: FF         RST     0X38            
6F6C: 00         NOP                     
6F6D: FF         RST     0X38            
6F6E: 00         NOP                     
6F6F: FF         RST     0X38            
6F70: 00         NOP                     
6F71: 00         NOP                     
6F72: C0         RET     NZ              
6F73: C0         RET     NZ              
6F74: E0 E0      LDFF00  ($E0),A         
6F76: F0 F0      LD      A,($F0)         
6F78: 70         LD      (HL),B          
6F79: F0 3C      LD      A,($3C)         
6F7B: FC         ???                     
6F7C: 3E FE      LD      A,$FE           
6F7E: 0F         RRCA                    
6F7F: FF         RST     0X38            
6F80: 0F         RRCA                    
6F81: 0F         RRCA                    
6F82: 0E 0F      LD      C,$0F           
6F84: 1C         INC     E               
6F85: 1F         RRA                     
6F86: 1E 1F      LD      E,$1F           
6F88: 1E 1F      LD      E,$1F           
6F8A: 0E 0F      LD      C,$0F           
6F8C: 0F         RRCA                    
6F8D: 0F         RRCA                    
6F8E: 03         INC     BC              
6F8F: 03         INC     BC              
6F90: 00         NOP                     
6F91: FF         RST     0X38            
6F92: 00         NOP                     
6F93: FF         RST     0X38            
6F94: 01 FF 02   LD      BC,$02FF        
6F97: FF         RST     0X38            
6F98: 0E FF      LD      C,$FF           
6F9A: 3F         CCF                     
6F9B: FF         RST     0X38            
6F9C: F7         RST     0X30            
6F9D: F7         RST     0X30            
6F9E: C3 C3 FF   JP      $FFC3           
6FA1: FF         RST     0X38            
6FA2: FF         RST     0X38            
6FA3: FF         RST     0X38            
6FA4: 3E 3F      LD      A,$3F           
6FA6: 06 07      LD      B,$07           
6FA8: 07         RLCA                    
6FA9: 07         RLCA                    
6FAA: 07         RLCA                    
6FAB: 07         RLCA                    
6FAC: 03         INC     BC              
6FAD: 03         INC     BC              
6FAE: 03         INC     BC              
6FAF: 03         INC     BC              
6FB0: EC         ???                     
6FB1: EF         RST     0X28            
6FB2: 0C         INC     C               
6FB3: 0F         RRCA                    
6FB4: 0E 0F      LD      C,$0F           
6FB6: 0E 0F      LD      C,$0F           
6FB8: 07         RLCA                    
6FB9: 07         RLCA                    
6FBA: 07         RLCA                    
6FBB: 07         RLCA                    
6FBC: 03         INC     BC              
6FBD: 03         INC     BC              
6FBE: 01 01 FF   LD      BC,$FF01        
6FC1: 00         NOP                     
6FC2: FF         RST     0X38            
6FC3: 00         NOP                     
6FC4: FF         RST     0X38            
6FC5: 00         NOP                     
6FC6: FF         RST     0X38            
6FC7: 00         NOP                     
6FC8: FF         RST     0X38            
6FC9: 00         NOP                     
6FCA: FF         RST     0X38            
6FCB: 00         NOP                     
6FCC: FF         RST     0X38            
6FCD: 00         NOP                     
6FCE: FF         RST     0X38            
6FCF: 00         NOP                     
6FD0: 00         NOP                     
6FD1: FF         RST     0X38            
6FD2: 00         NOP                     
6FD3: FF         RST     0X38            
6FD4: 00         NOP                     
6FD5: FF         RST     0X38            
6FD6: 00         NOP                     
6FD7: FF         RST     0X38            
6FD8: 00         NOP                     
6FD9: FF         RST     0X38            
6FDA: 00         NOP                     
6FDB: FF         RST     0X38            
6FDC: 00         NOP                     
6FDD: FF         RST     0X38            
6FDE: 00         NOP                     
6FDF: FF         RST     0X38            
6FE0: FF         RST     0X38            
6FE1: FF         RST     0X38            
6FE2: FF         RST     0X38            
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
6FEF: FF         RST     0X38            
6FF0: 00         NOP                     
6FF1: 00         NOP                     
6FF2: 00         NOP                     
6FF3: 00         NOP                     
6FF4: 00         NOP                     
6FF5: 00         NOP                     
6FF6: 00         NOP                     
6FF7: 00         NOP                     
6FF8: 00         NOP                     
6FF9: 00         NOP                     
6FFA: 00         NOP                     
6FFB: 00         NOP                     
6FFC: 00         NOP                     
6FFD: 00         NOP                     
6FFE: 00         NOP                     
6FFF: 00         NOP                     
7000: E0 E0      LDFF00  ($E0),A         
7002: F0 F0      LD      A,($F0)         
7004: 78         LD      A,B             
7005: F8 38      LDHL    SP,$38          
7007: F8 0F      LDHL    SP,$0F          
7009: FF         RST     0X38            
700A: C7         RST     0X00            
700B: FF         RST     0X38            
700C: 47         LD      B,A             
700D: FF         RST     0X38            
700E: 7F         LD      A,A             
700F: FF         RST     0X38            
7010: 00         NOP                     
7011: 00         NOP                     
7012: 00         NOP                     
7013: 00         NOP                     
7014: 00         NOP                     
7015: 00         NOP                     
7016: 00         NOP                     
7017: 00         NOP                     
7018: E0 E0      LDFF00  ($E0),A         
701A: F8 F8      LDHL    SP,$F8          
701C: 64         LD      H,H             
701D: FC         ???                     
701E: 86         ADD     A,(HL)          
701F: FE FF      CP      $FF             
7021: FF         RST     0X38            
7022: 55         LD      D,L             
7023: FF         RST     0X38            
7024: A2         AND     D               
7025: FF         RST     0X38            
7026: 81         ADD     A,C             
7027: FF         RST     0X38            
7028: 08 BF 01   LD      ($01BF),SP      
702B: 9F         SBC     A               
702C: 20 72      JR      NZ,$70A0        
702E: 00         NOP                     
702F: 9C         SBC     H               
7030: FF         RST     0X38            
7031: FF         RST     0X38            
7032: 55         LD      D,L             
7033: FF         RST     0X38            
7034: 45         LD      B,L             
7035: FF         RST     0X38            
7036: 10 FF      STOP    $FF             
7038: 08 FB 00   LD      ($00FB),SP      
703B: BC         CP      H               
703C: 02         LD      (BC),A          
703D: 9F         SBC     A               
703E: 00         NOP                     
703F: AC         XOR     H               
7040: 00         NOP                     
7041: 00         NOP                     
7042: 00         NOP                     
7043: 00         NOP                     
7044: 00         NOP                     
7045: 00         NOP                     
7046: 00         NOP                     
7047: 04         INC     B               
7048: 00         NOP                     
7049: 09         ADD     HL,BC           
704A: 00         NOP                     
704B: 02         LD      (BC),A          
704C: 00         NOP                     
704D: 08 00 10   LD      ($1000),SP      
7050: 00         NOP                     
7051: 03         INC     BC              
7052: 00         NOP                     
7053: 00         NOP                     
7054: 00         NOP                     
7055: 00         NOP                     
7056: 00         NOP                     
7057: C7         RST     0X00            
7058: 00         NOP                     
7059: 00         NOP                     
705A: 00         NOP                     
705B: 07         RLCA                    
705C: 0C         INC     C               
705D: 1E 10      LD      E,$10           
705F: B9         CP      C               
7060: BD         CP      L               
7061: E2         LDFF00  (C),A           
7062: FD         ???                     
7063: C2 FD 02   JP      NZ,$02FD        
7066: 7D         LD      A,L             
7067: 82         ADD     A,D             
7068: 3D         DEC     A               
7069: C2 3F C0   JP      NZ,$C03F        
706C: 5F         LD      E,A             
706D: 80         ADD     A,B             
706E: 8F         ADC     A,A             
706F: 00         NOP                     
7070: 0E 00      LD      C,$00           
7072: 86         ADD     A,(HL)          
7073: 00         NOP                     
7074: 80         ADD     A,B             
7075: 00         NOP                     
7076: 40         LD      B,B             
7077: 00         NOP                     
7078: 40         LD      B,B             
7079: 00         NOP                     
707A: 40         LD      B,B             
707B: 00         NOP                     
707C: 20 00      JR      NZ,$707E        
707E: 20 00      JR      NZ,$7080        
7080: 00         NOP                     
7081: 00         NOP                     
7082: 00         NOP                     
7083: 00         NOP                     
7084: 00         NOP                     
7085: 00         NOP                     
7086: 00         NOP                     
7087: 00         NOP                     
7088: 00         NOP                     
7089: 00         NOP                     
708A: 00         NOP                     
708B: 00         NOP                     
708C: 00         NOP                     
708D: 00         NOP                     
708E: 03         INC     BC              
708F: 00         NOP                     
7090: 0F         RRCA                    
7091: 03         INC     BC              
7092: 1F         RRA                     
7093: 0F         RRCA                    
7094: 3F         CCF                     
7095: 1C         INC     E               
7096: 3F         CCF                     
7097: 13         INC     DE              
7098: 7F         LD      A,A             
7099: 0F         RRCA                    
709A: 7F         LD      A,A             
709B: 1F         RRA                     
709C: 7F         LD      A,A             
709D: 1F         RRA                     
709E: 7C         LD      A,H             
709F: 0F         RRCA                    
70A0: 00         NOP                     
70A1: 00         NOP                     
70A2: 00         NOP                     
70A3: 00         NOP                     
70A4: 00         NOP                     
70A5: 00         NOP                     
70A6: 00         NOP                     
70A7: 00         NOP                     
70A8: 00         NOP                     
70A9: 00         NOP                     
70AA: 00         NOP                     
70AB: 00         NOP                     
70AC: 00         NOP                     
70AD: 00         NOP                     
70AE: 80         ADD     A,B             
70AF: 00         NOP                     
70B0: C0         RET     NZ              
70B1: 80         ADD     A,B             
70B2: F0 C0      LD      A,($C0)         
70B4: FF         RST     0X38            
70B5: 70         LD      (HL),B          
70B6: FE 84      CP      $84             
70B8: FE F8      CP      $F8             
70BA: FF         RST     0X38            
70BB: FE 7F      CP      $7F             
70BD: FE 1F      CP      $1F             
70BF: 7C         LD      A,H             
70C0: 09         ADD     HL,BC           
70C1: 00         NOP                     
70C2: 0F         RRCA                    
70C3: 00         NOP                     
70C4: 17         RLA                     
70C5: 08 17 08   LD      ($0817),SP      
70C8: 26 19      LD      H,$19           
70CA: 2A         LD      A,(HLI)         
70CB: 11 4C 33   LD      DE,$334C        
70CE: 4C         LD      C,H             
70CF: 33         INC     SP              
70D0: 98         SBC     B               
70D1: 67         LD      H,A             
70D2: F0 0F      LD      A,($0F)         
70D4: E0 1E      LDFF00  ($1E),A         
70D6: 20 1C      JR      NZ,$70F4        
70D8: 40         LD      B,B             
70D9: 38 81      JR      C,$705C         
70DB: 70         LD      (HL),B          
70DC: 03         INC     BC              
70DD: C0         RET     NZ              
70DE: 8F         ADC     A,A             
70DF: 00         NOP                     
70E0: 01 FC 03   LD      BC,$03FC        
70E3: F8 03      LDHL    SP,$03          
70E5: F8 06      LDHL    SP,$06          
70E7: F0 06      LD      A,($06)         
70E9: E0 0D      LDFF00  ($0D),A         
70EB: E0 0C      LDFF00  ($0C),A         
70ED: C0         RET     NZ              
70EE: 1C         INC     E               
70EF: 80         ADD     A,B             
70F0: 38 80      JR      C,$7072         
70F2: 37         SCF                     
70F3: 00         NOP                     
70F4: 5F         LD      E,A             
70F5: 00         NOP                     
70F6: 4F         LD      C,A             
70F7: 0F         RRCA                    
70F8: FF         RST     0X38            
70F9: 00         NOP                     
70FA: 80         ADD     A,B             
70FB: 00         NOP                     
70FC: 80         ADD     A,B             
70FD: 00         NOP                     
70FE: 00         NOP                     
70FF: 00         NOP                     
7100: 71         LD      (HL),C          
7101: FF         RST     0X38            
7102: 80         ADD     A,B             
7103: FF         RST     0X38            
7104: 40         LD      B,B             
7105: FF         RST     0X38            
7106: F8 FF      LDHL    SP,$FF          
7108: FC         ???                     
7109: FF         RST     0X38            
710A: 7C         LD      A,H             
710B: FF         RST     0X38            
710C: 07         RLCA                    
710D: FF         RST     0X38            
710E: 03         INC     BC              
710F: FF         RST     0X38            
7110: 9A         SBC     D               
7111: FE 8E      CP      $8E             
7113: FE 46      CP      $46             
7115: FE 06      CP      $06             
7117: FE 04      CP      $04             
7119: FC         ???                     
711A: 3C         INC     A               
711B: FC         ???                     
711C: 0E FE      LD      C,$FE           
711E: 01 FF 00   LD      BC,$00FF        
7121: 69         LD      L,C             
7122: 00         NOP                     
7123: 34         INC     (HL)            
7124: 21 21 00   LD      HL,$0021        
7127: 00         NOP                     
7128: 00         NOP                     
7129: 44         LD      B,H             
712A: 00         NOP                     
712B: 20 00      JR      NZ,$712D        
712D: 08 00 00   LD      ($0000),SP      
7130: 10 5A      STOP    $5A             
7132: 00         NOP                     
7133: 0D         DEC     C               
7134: 00         NOP                     
7135: 80         ADD     A,B             
7136: 00         NOP                     
7137: 12         LD      (DE),A          
7138: 80         ADD     A,B             
7139: 80         ADD     A,B             
713A: 00         NOP                     
713B: 08 00 00   LD      ($0000),SP      
713E: 00         NOP                     
713F: 08 20 00   LD      ($0020),SP      
7142: 20 00      JR      NZ,$7144        
7144: 60         LD      H,B             
7145: 00         NOP                     
7146: 60         LD      H,B             
7147: 00         NOP                     
7148: E0 00      LDFF00  ($00),A         
714A: E0 00      LDFF00  ($00),A         
714C: E0 00      LDFF00  ($00),A         
714E: 40         LD      B,B             
714F: 00         NOP                     
7150: 60         LD      H,B             
7151: 00         NOP                     
7152: E0 00      LDFF00  ($00),A         
7154: C0         RET     NZ              
7155: 00         NOP                     
7156: 80         ADD     A,B             
7157: 00         NOP                     
7158: 80         ADD     A,B             
7159: 00         NOP                     
715A: C0         RET     NZ              
715B: 00         NOP                     
715C: 40         LD      B,B             
715D: 00         NOP                     
715E: B0         OR      B               
715F: 00         NOP                     
7160: FD         ???                     
7161: A2         AND     D               
7162: B9         CP      C               
7163: 76         HALT                    
7164: FD         ???                     
7165: 72         LD      (HL),D          
7166: FD         ???                     
7167: 62         LD      H,D             
7168: 7D         LD      A,L             
7169: 82         ADD     A,D             
716A: 3D         DEC     A               
716B: C2 7A 84   JP      NZ,$847A        
716E: FA 04 BA   LD      A,($BA04)       
7171: 04         INC     B               
7172: BC         CP      H               
7173: 00         NOP                     
7174: 9C         SBC     H               
7175: 00         NOP                     
7176: 5C         LD      E,H             
7177: 00         NOP                     
7178: 4C         LD      C,H             
7179: 00         NOP                     
717A: 40         LD      B,B             
717B: 00         NOP                     
717C: 20 00      JR      NZ,$717E        
717E: 20 00      JR      NZ,$7180        
7180: 7C         LD      A,H             
7181: 33         INC     SP              
7182: FF         RST     0X38            
7183: 1C         INC     E               
7184: FF         RST     0X38            
7185: 2F         CPL                     
7186: FF         RST     0X38            
7187: 3F         CCF                     
7188: FF         RST     0X38            
7189: 1C         INC     E               
718A: 9F         SBC     A               
718B: 07         RLCA                    
718C: 8F         ADC     A,A             
718D: 00         NOP                     
718E: 81         ADD     A,C             
718F: 00         NOP                     
7190: 87         ADD     A,A             
7191: 00         NOP                     
7192: C1         POP     BC              
7193: 00         NOP                     
7194: 7F         LD      A,A             
7195: 00         NOP                     
7196: 1E 00      LD      E,$00           
7198: 00         NOP                     
7199: 00         NOP                     
719A: 1E 00      LD      E,$00           
719C: 00         NOP                     
719D: 00         NOP                     
719E: 00         NOP                     
719F: 00         NOP                     
71A0: 03         INC     BC              
71A1: 7D         LD      A,L             
71A2: BF         CP      A               
71A3: 03         INC     BC              
71A4: FF         RST     0X38            
71A5: 3F         CCF                     
71A6: FF         RST     0X38            
71A7: 7F         LD      A,A             
71A8: FF         RST     0X38            
71A9: 60         LD      H,B             
71AA: FF         RST     0X38            
71AB: 43         LD      B,E             
71AC: FC         ???                     
71AD: 0F         RRCA                    
71AE: F3         DI                      
71AF: 1F         RRA                     
71B0: F6 1F      OR      $1F             
71B2: ED         ???                     
71B3: 3F         CCF                     
71B4: EB         ???                     
71B5: 3F         CCF                     
71B6: 6A         LD      L,D             
71B7: 3E 3F      LD      A,$3F           
71B9: 00         NOP                     
71BA: 3F         CCF                     
71BB: 00         NOP                     
71BC: 00         NOP                     
71BD: 00         NOP                     
71BE: 03         INC     BC              
71BF: 00         NOP                     
71C0: 00         NOP                     
71C1: 00         NOP                     
71C2: 00         NOP                     
71C3: 00         NOP                     
71C4: 00         NOP                     
71C5: 00         NOP                     
71C6: 03         INC     BC              
71C7: 03         INC     BC              
71C8: 0F         RRCA                    
71C9: 0F         RRCA                    
71CA: 0F         RRCA                    
71CB: 0F         RRCA                    
71CC: 1C         INC     E               
71CD: 1F         RRA                     
71CE: 38 3F      JR      C,$720F         
71D0: 00         NOP                     
71D1: C0         RET     NZ              
71D2: 00         NOP                     
71D3: 0C         INC     C               
71D4: 00         NOP                     
71D5: 03         INC     BC              
71D6: 00         NOP                     
71D7: 00         NOP                     
71D8: 00         NOP                     
71D9: 30 00      JR      NC,$71DB        
71DB: EC         ???                     
71DC: 00         NOP                     
71DD: 36 60      LD      (HL),$60        
71DF: F8 00      LDHL    SP,$00          
71E1: 00         NOP                     
71E2: 00         NOP                     
71E3: 00         NOP                     
71E4: DF         RST     0X18            
71E5: DF         RST     0X18            
71E6: FF         RST     0X38            
71E7: FF         RST     0X38            
71E8: FE FF      CP      $FF             
71EA: 60         LD      H,B             
71EB: FF         RST     0X38            
71EC: 78         LD      A,B             
71ED: FF         RST     0X38            
71EE: 86         ADD     A,(HL)          
71EF: FF         RST     0X38            
71F0: 00         NOP                     
71F1: 00         NOP                     
71F2: 00         NOP                     
71F3: 00         NOP                     
71F4: 00         NOP                     
71F5: 00         NOP                     
71F6: 00         NOP                     
71F7: 80         ADD     A,B             
71F8: 00         NOP                     
71F9: 00         NOP                     
71FA: 00         NOP                     
71FB: 90         SUB     B               
71FC: 00         NOP                     
71FD: 48         LD      C,B             
71FE: 00         NOP                     
71FF: 20 00      JR      NZ,$7201        
7201: FF         RST     0X38            
7202: 7C         LD      A,H             
7203: FF         RST     0X38            
7204: FF         RST     0X38            
7205: FF         RST     0X38            
7206: FF         RST     0X38            
7207: FF         RST     0X38            
7208: DF         RST     0X18            
7209: FF         RST     0X38            
720A: 07         RLCA                    
720B: FF         RST     0X38            
720C: 01 FF 00   LD      BC,$00FF        
720F: FF         RST     0X38            
7210: 61         LD      H,C             
7211: FF         RST     0X38            
7212: E7         RST     0X20            
7213: FF         RST     0X38            
7214: FC         ???                     
7215: FF         RST     0X38            
7216: FC         ???                     
7217: FF         RST     0X38            
7218: BF         CP      A               
7219: FF         RST     0X38            
721A: 8F         ADC     A,A             
721B: FF         RST     0X38            
721C: 86         ADD     A,(HL)          
721D: FF         RST     0X38            
721E: 82         ADD     A,D             
721F: FF         RST     0X38            
7220: 00         NOP                     
7221: 01 00 03   LD      BC,$0300        
7224: 00         NOP                     
7225: 21 00 47   LD      HL,$4700        
7228: 00         NOP                     
7229: 4B         LD      C,E             
722A: 00         NOP                     
722B: 0F         RRCA                    
722C: 02         LD      (BC),A          
722D: 07         RLCA                    
722E: 02         LD      (BC),A          
722F: 83         ADD     A,E             
7230: 02         LD      (BC),A          
7231: DF         RST     0X18            
7232: 0D         DEC     C               
7233: BF         CP      A               
7234: 10 7F      STOP    $7F             
7236: 4B         LD      C,E             
7237: FF         RST     0X38            
7238: 9F         SBC     A               
7239: FF         RST     0X38            
723A: 9F         SBC     A               
723B: FF         RST     0X38            
723C: 1F         RRA                     
723D: FF         RST     0X38            
723E: BF         CP      A               
723F: FF         RST     0X38            
7240: DE 80      SBC     $80             
7242: FC         ???                     
7243: 80         ADD     A,B             
7244: F8 00      LDHL    SP,$00          
7246: F9         LD      SP,HL           
7247: 00         NOP                     
7248: FF         RST     0X38            
7249: 00         NOP                     
724A: FF         RST     0X38            
724B: F0 0F      LD      A,($0F)         
724D: FC         ???                     
724E: F3         DI                      
724F: FE 1B      CP      $1B             
7251: FE ED      CP      $ED             
7253: FF         RST     0X38            
7254: 35         DEC     (HL)            
7255: 3F         CCF                     
7256: 15         DEC     D               
7257: 1F         RRA                     
7258: FF         RST     0X38            
7259: 00         NOP                     
725A: FF         RST     0X38            
725B: 00         NOP                     
725C: 07         RLCA                    
725D: 00         NOP                     
725E: FF         RST     0X38            
725F: 00         NOP                     
7260: F9         LD      SP,HL           
7261: 96         SUB     (HL)            
7262: F9         LD      SP,HL           
7263: 66         LD      H,(HL)          
7264: FA C4 FE   LD      A,($FEC4)       
7267: 30 FE      JR      NC,$7267        
7269: 70         LD      (HL),B          
726A: FE 60      CP      $60             
726C: FE 00      CP      $00             
726E: 7E         LD      A,(HL)          
726F: 80         ADD     A,B             
7270: FA 04 BE   LD      A,($BE04)       
7273: 00         NOP                     
7274: BA         CP      D               
7275: 04         INC     B               
7276: 7E         LD      A,(HL)          
7277: 00         NOP                     
7278: 5C         LD      E,H             
7279: 00         NOP                     
727A: 4C         LD      C,H             
727B: 00         NOP                     
727C: 20 00      JR      NZ,$727E        
727E: 20 00      JR      NZ,$7280        
7280: 01 00 07   LD      BC,$0700        
7283: 00         NOP                     
7284: 3F         CCF                     
7285: 00         NOP                     
7286: FF         RST     0X38            
7287: 00         NOP                     
7288: FF         RST     0X38            
7289: 00         NOP                     
728A: FF         RST     0X38            
728B: 07         RLCA                    
728C: F8 1F      LDHL    SP,$1F          
728E: E7         RST     0X20            
728F: 3F         CCF                     
7290: 6C         LD      L,H             
7291: BF         CP      A               
7292: DB         ???                     
7293: 7F         LD      A,A             
7294: D6 7E      SUB     $7E             
7296: D4 7C FF   CALL    NC,$FF7C        
7299: 00         NOP                     
729A: FF         RST     0X38            
729B: 00         NOP                     
729C: FF         RST     0X38            
729D: 00         NOP                     
729E: FF         RST     0X38            
729F: 00         NOP                     
72A0: E8 10      ADD     SP,$10          
72A2: E4         ???                     
72A3: 18 C4      JR      $7269           
72A5: 38 82      JR      C,$7229         
72A7: 7C         LD      A,H             
72A8: F2         ???                     
72A9: 0C         INC     C               
72AA: F9         LD      SP,HL           
72AB: E6 1D      AND     $1D             
72AD: FA E7 FC   LD      A,($FCE7)       
72B0: 37         SCF                     
72B1: FC         ???                     
72B2: DB         ???                     
72B3: FE 6B      CP      $6B             
72B5: 7E         LD      A,(HL)          
72B6: 2B         DEC     HL              
72B7: 3E FF      LD      A,$FF           
72B9: 00         NOP                     
72BA: FE 00      CP      $00             
72BC: 80         ADD     A,B             
72BD: 00         NOP                     
72BE: B0         OR      B               
72BF: 00         NOP                     
72C0: 00         NOP                     
72C1: 00         NOP                     
72C2: 00         NOP                     
72C3: 00         NOP                     
72C4: 00         NOP                     
72C5: 00         NOP                     
72C6: 00         NOP                     
72C7: 00         NOP                     
72C8: 00         NOP                     
72C9: 00         NOP                     
72CA: 00         NOP                     
72CB: 00         NOP                     
72CC: 00         NOP                     
72CD: 00         NOP                     
72CE: 00         NOP                     
72CF: 00         NOP                     
72D0: FF         RST     0X38            
72D1: 00         NOP                     
72D2: FF         RST     0X38            
72D3: 00         NOP                     
72D4: FF         RST     0X38            
72D5: 00         NOP                     
72D6: FF         RST     0X38            
72D7: 00         NOP                     
72D8: FF         RST     0X38            
72D9: 00         NOP                     
72DA: FF         RST     0X38            
72DB: 00         NOP                     
72DC: FF         RST     0X38            
72DD: 00         NOP                     
72DE: FF         RST     0X38            
72DF: 00         NOP                     
72E0: 00         NOP                     
72E1: FF         RST     0X38            
72E2: 00         NOP                     
72E3: FF         RST     0X38            
72E4: 00         NOP                     
72E5: FF         RST     0X38            
72E6: 00         NOP                     
72E7: FF         RST     0X38            
72E8: 00         NOP                     
72E9: FF         RST     0X38            
72EA: 00         NOP                     
72EB: FF         RST     0X38            
72EC: 00         NOP                     
72ED: FF         RST     0X38            
72EE: 00         NOP                     
72EF: FF         RST     0X38            
72F0: FF         RST     0X38            
72F1: FF         RST     0X38            
72F2: FF         RST     0X38            
72F3: FF         RST     0X38            
72F4: FF         RST     0X38            
72F5: FF         RST     0X38            
72F6: FF         RST     0X38            
72F7: FF         RST     0X38            
72F8: FF         RST     0X38            
72F9: FF         RST     0X38            
72FA: FF         RST     0X38            
72FB: FF         RST     0X38            
72FC: FF         RST     0X38            
72FD: FF         RST     0X38            
72FE: FF         RST     0X38            
72FF: FF         RST     0X38            
7300: 00         NOP                     
7301: FF         RST     0X38            
7302: 07         RLCA                    
7303: FF         RST     0X38            
7304: 0F         RRCA                    
7305: FF         RST     0X38            
7306: 1F         RRA                     
7307: FF         RST     0X38            
7308: 30 FF      JR      NC,$7309        
730A: 00         NOP                     
730B: FF         RST     0X38            
730C: 00         NOP                     
730D: FF         RST     0X38            
730E: 00         NOP                     
730F: FF         RST     0X38            
7310: 00         NOP                     
7311: FF         RST     0X38            
7312: 80         ADD     A,B             
7313: FF         RST     0X38            
7314: E0 FF      LDFF00  ($FF),A         
7316: F3         DI                      
7317: FF         RST     0X38            
7318: 1F         RRA                     
7319: FF         RST     0X38            
731A: 0C         INC     C               
731B: FF         RST     0X38            
731C: 10 FF      STOP    $FF             
731E: 00         NOP                     
731F: FF         RST     0X38            
7320: 00         NOP                     
7321: 00         NOP                     
7322: 00         NOP                     
7323: 00         NOP                     
7324: 00         NOP                     
7325: 00         NOP                     
7326: 00         NOP                     
7327: 00         NOP                     
7328: 0F         RRCA                    
7329: 00         NOP                     
732A: 10 0F      STOP    $0F             
732C: 20 1F      JR      NZ,$734D        
732E: 20 1F      JR      NZ,$734F        
7330: 40         LD      B,B             
7331: 3F         CCF                     
7332: 40         LD      B,B             
7333: 3F         CCF                     
7334: 40         LD      B,B             
7335: 3F         CCF                     
7336: 43         LD      B,E             
7337: 3C         INC     A               
7338: 24         INC     H               
7339: 18 28      JR      $7363           
733B: 10 19      STOP    $19             
733D: 00         NOP                     
733E: 05         DEC     B               
733F: 00         NOP                     
7340: 00         NOP                     
7341: 00         NOP                     
7342: 00         NOP                     
7343: 00         NOP                     
7344: 38 00      JR      C,$7346         
7346: D0         RET     NC              
7347: 20 1F      JR      NZ,$7368        
7349: E0 07      LDFF00  ($07),A         
734B: FB         EI                      
734C: 03         INC     BC              
734D: FD         ???                     
734E: 01 FE 20   LD      BC,$20FE        
7351: DF         RST     0X18            
7352: 44         LD      B,H             
7353: BB         CP      E               
7354: F8 07      LDHL    SP,$07          
7356: 1F         RRA                     
7357: 00         NOP                     
7358: 17         RLA                     
7359: 08 F7 1A   LD      ($1AF7),SP      
735C: FC         ???                     
735D: FF         RST     0X38            
735E: 7F         LD      A,A             
735F: FF         RST     0X38            
7360: 00         NOP                     
7361: 00         NOP                     
7362: 00         NOP                     
7363: 00         NOP                     
7364: 00         NOP                     
7365: 00         NOP                     
7366: C0         RET     NZ              
7367: 00         NOP                     
7368: FF         RST     0X38            
7369: C0         RET     NZ              
736A: F8 77      LDHL    SP,$77          
736C: 9C         SBC     H               
736D: FB         EI                      
736E: EE 7D      XOR     $7D             
7370: 7F         LD      A,A             
7371: BE         CP      (HL)            
7372: 3F         CCF                     
7373: DE DF      SBC     $DF             
7375: 2D         DEC     L               
7376: 5F         LD      E,A             
7377: AA         XOR     D               
7378: 4E         LD      C,(HL)          
7379: B5         OR      L               
737A: 4F         LD      C,A             
737B: B5         OR      L               
737C: 2D         DEC     L               
737D: D3         ???                     
737E: AB         XOR     E               
737F: D7         RST     0X10            
7380: 00         NOP                     
7381: 00         NOP                     
7382: 00         NOP                     
7383: 00         NOP                     
7384: 00         NOP                     
7385: 00         NOP                     
7386: 00         NOP                     
7387: 00         NOP                     
7388: 80         ADD     A,B             
7389: 00         NOP                     
738A: 60         LD      H,B             
738B: 80         ADD     A,B             
738C: 10 E0      STOP    $E0             
738E: 08 F0 84   LD      ($84F0),SP      
7391: 78         LD      A,B             
7392: C4 38 E4   CALL    NZ,$E438        
7395: 98         SBC     B               
7396: E4         ???                     
7397: 98         SBC     B               
7398: F2         ???                     
7399: 8C         ADC     A,H             
739A: F9         LD      SP,HL           
739B: 86         ADD     A,(HL)          
739C: F9         LD      SP,HL           
739D: 46         LD      B,(HL)          
739E: FD         ???                     
739F: 62         LD      H,D             
73A0: 9F         SBC     A               
73A1: 7F         LD      A,A             
73A2: 5F         LD      E,A             
73A3: 3F         CCF                     
73A4: 7E         LD      A,(HL)          
73A5: 3F         CCF                     
73A6: 7C         LD      A,H             
73A7: 3F         CCF                     
73A8: 70         LD      (HL),B          
73A9: 3F         CCF                     
73AA: 21 1E 1F   LD      HL,$1F1E        
73AD: 00         NOP                     
73AE: 01 00 01   LD      BC,$0100        
73B1: 00         NOP                     
73B2: 02         LD      (BC),A          
73B3: 00         NOP                     
73B4: 04         INC     B               
73B5: 00         NOP                     
73B6: 04         INC     B               
73B7: 00         NOP                     
73B8: 04         INC     B               
73B9: 00         NOP                     
73BA: 08 00 08   LD      ($0800),SP      
73BD: 00         NOP                     
73BE: 08 00 2F   LD      ($2F00),SP      
73C1: D6 2F      SUB     $2F             
73C3: D4 4C B3   CALL    NC,$B34C        
73C6: 4C         LD      C,H             
73C7: B3         OR      E               
73C8: 8E         ADC     A,(HL)          
73C9: 75         LD      (HL),L          
73CA: 0E F5      LD      C,$F5           
73CC: 0C         INC     C               
73CD: F3         DI                      
73CE: 0F         RRCA                    
73CF: F0 91      LD      A,($91)         
73D1: 60         LD      H,B             
73D2: 9C         SBC     H               
73D3: 60         LD      H,B             
73D4: 52         LD      D,D             
73D5: 2C         INC     L               
73D6: 71         LD      (HL),C          
73D7: 0E 51      LD      C,$51           
73D9: 2E 81      LD      L,$81           
73DB: 7E         LD      A,(HL)          
73DC: 81         ADD     A,C             
73DD: 7E         LD      A,(HL)          
73DE: 81         ADD     A,C             
73DF: 7C         LD      A,H             
73E0: 7C         LD      A,H             
73E1: 7C         LD      A,H             
73E2: FF         RST     0X38            
73E3: FF         RST     0X38            
73E4: FF         RST     0X38            
73E5: FF         RST     0X38            
73E6: EF         RST     0X28            
73E7: FF         RST     0X38            
73E8: 00         NOP                     
73E9: FF         RST     0X38            
73EA: 00         NOP                     
73EB: FF         RST     0X38            
73EC: 00         NOP                     
73ED: FF         RST     0X38            
73EE: 00         NOP                     
73EF: FF         RST     0X38            
73F0: 14         INC     D               
73F1: FE A2      CP      $A2             
73F3: FF         RST     0X38            
73F4: 09         ADD     HL,BC           
73F5: FF         RST     0X38            
73F6: F4         ???                     
73F7: FF         RST     0X38            
73F8: F9         LD      SP,HL           
73F9: FF         RST     0X38            
73FA: FA FF FE   LD      A,($FEFF)       
73FD: FF         RST     0X38            
73FE: FC         ???                     
73FF: FF         RST     0X38            
7400: 07         RLCA                    
7401: 00         NOP                     
7402: 0F         RRCA                    
7403: 07         RLCA                    
7404: 0F         RRCA                    
7405: 00         NOP                     
7406: 1F         RRA                     
7407: 0F         RRCA                    
7408: 30 1F      JR      NC,$7429        
740A: 18 07      JR      $7413           
740C: 07         RLCA                    
740D: 00         NOP                     
740E: 0C         INC     C               
740F: 03         INC     BC              
7410: 33         INC     SP              
7411: 0F         RRCA                    
7412: 44         LD      B,H             
7413: 03         INC     BC              
7414: 83         ADD     A,E             
7415: 00         NOP                     
7416: C8         RET     Z               
7417: 00         NOP                     
7418: BF         CP      A               
7419: C0         RET     NZ              
741A: FF         RST     0X38            
741B: 80         ADD     A,B             
741C: 40         LD      B,B             
741D: 80         ADD     A,B             
741E: 80         ADD     A,B             
741F: 00         NOP                     
7420: 00         NOP                     
7421: 00         NOP                     
7422: 00         NOP                     
7423: 00         NOP                     
7424: 00         NOP                     
7425: 00         NOP                     
7426: 01 00 02   LD      BC,$0200        
7429: 01 04 03   LD      BC,$0304        
742C: 04         INC     B               
742D: 03         INC     BC              
742E: 04         INC     B               
742F: 03         INC     BC              
7430: 04         INC     B               
7431: 03         INC     BC              
7432: 05         DEC     B               
7433: 02         LD      (BC),A          
7434: 03         INC     BC              
7435: 00         NOP                     
7436: 01 00 00   LD      BC,$0000        
7439: 00         NOP                     
743A: 00         NOP                     
743B: 00         NOP                     
743C: 00         NOP                     
743D: 00         NOP                     
743E: 00         NOP                     
743F: 00         NOP                     
7440: 00         NOP                     
7441: 00         NOP                     
7442: 00         NOP                     
7443: 00         NOP                     
7444: FE 00      CP      $00             
7446: 01 FE 00   LD      BC,$00FE        
7449: FF         RST     0X38            
744A: 00         NOP                     
744B: FF         RST     0X38            
744C: 04         INC     B               
744D: FB         EI                      
744E: 08 F7 7E   LD      ($7EF7),SP      
7451: 81         ADD     A,C             
7452: 83         ADD     A,E             
7453: 00         NOP                     
7454: 07         RLCA                    
7455: 00         NOP                     
7456: 7D         LD      A,L             
7457: 06 7F      LD      B,$7F           
7459: 3E 5F      LD      A,$5F           
745B: 3F         CCF                     
745C: 6F         LD      L,A             
745D: 1F         RRA                     
745E: 2F         CPL                     
745F: 1F         RRA                     
7460: 00         NOP                     
7461: 00         NOP                     
7462: 00         NOP                     
7463: 00         NOP                     
7464: E0 00      LDFF00  ($00),A         
7466: B8         CP      B               
7467: 40         LD      B,B             
7468: FF         RST     0X38            
7469: 38 3F      JR      C,$74AA         
746B: CE 13      ADC     $13             
746D: EF         RST     0X28            
746E: 0D         DEC     C               
746F: F7         RST     0X30            
7470: 87         ADD     A,A             
7471: 7B         LD      A,E             
7472: 07         RLCA                    
7473: FB         EI                      
7474: 3B         DEC     SP              
7475: C5         PUSH    BC              
7476: CB 35      SET     1,E             
7478: D3         ???                     
7479: AD         XOR     L               
747A: D3         ???                     
747B: AC         XOR     H               
747C: 17         RLA                     
747D: EB         ???                     
747E: AF         XOR     A               
747F: D4 00 00   CALL    NC,$0000        
7482: 00         NOP                     
7483: 00         NOP                     
7484: 00         NOP                     
7485: 00         NOP                     
7486: 00         NOP                     
7487: 00         NOP                     
7488: 80         ADD     A,B             
7489: 00         NOP                     
748A: 60         LD      H,B             
748B: 80         ADD     A,B             
748C: 98         SBC     B               
748D: 60         LD      H,B             
748E: C4 B8 E4   CALL    NZ,$E4B8        
7491: D8         RET     C               
7492: E2         LDFF00  (C),A           
7493: DC F2 CC   CALL    C,$CCF2         
7496: FA E4 F9   LD      A,($F9E4)       
7499: 06 F9      LD      B,$F9           
749B: E6 F9      AND     $F9             
749D: 66         LD      H,(HL)          
749E: F9         LD      SP,HL           
749F: C6 7F      ADD     $7F             
74A1: 3F         CCF                     
74A2: 7F         LD      A,A             
74A3: 3F         CCF                     
74A4: 7E         LD      A,(HL)          
74A5: 3F         CCF                     
74A6: 78         LD      A,B             
74A7: 3F         CCF                     
74A8: 20 1F      JR      NZ,$74C9        
74AA: 1C         INC     E               
74AB: 03         INC     BC              
74AC: 03         INC     BC              
74AD: 00         NOP                     
74AE: 00         NOP                     
74AF: 00         NOP                     
74B0: 01 00 02   LD      BC,$0200        
74B3: 00         NOP                     
74B4: 04         INC     B               
74B5: 00         NOP                     
74B6: 04         INC     B               
74B7: 00         NOP                     
74B8: 04         INC     B               
74B9: 00         NOP                     
74BA: 08 00 08   LD      ($0800),SP      
74BD: 00         NOP                     
74BE: 08 00 AF   LD      ($AF00),SP      
74C1: D3         ???                     
74C2: 4F         LD      C,A             
74C3: B7         OR      A               
74C4: 4F         LD      C,A             
74C5: B6         OR      (HL)            
74C6: 8E         ADC     A,(HL)          
74C7: 71         LD      (HL),C          
74C8: 8E         ADC     A,(HL)          
74C9: 75         LD      (HL),L          
74CA: 86         ADD     A,(HL)          
74CB: 79         LD      A,C             
74CC: 84         ADD     A,H             
74CD: 7B         LD      A,E             
74CE: 84         ADD     A,H             
74CF: 7B         LD      A,E             
74D0: CF         RST     0X08            
74D1: 30 4C      JR      NC,$751F        
74D3: 30 2A      JR      NC,$74FF        
74D5: 14         INC     D               
74D6: 39         ADD     HL,SP           
74D7: 06 29      LD      B,$29           
74D9: 16 81      LD      D,$81           
74DB: 7E         LD      A,(HL)          
74DC: 81         ADD     A,C             
74DD: 7E         LD      A,(HL)          
74DE: 81         ADD     A,C             
74DF: 7C         LD      A,H             
74E0: 00         NOP                     
74E1: 00         NOP                     
74E2: 80         ADD     A,B             
74E3: 00         NOP                     
74E4: C7         RST     0X00            
74E5: 80         ADD     A,B             
74E6: DD         ???                     
74E7: 06 E5      LD      B,$E5           
74E9: 9E         SBC     (HL)            
74EA: C5         PUSH    BC              
74EB: BE         CP      (HL)            
74EC: 9B         SBC     E               
74ED: 7D         LD      A,L             
74EE: 67         LD      H,A             
74EF: FB         EI                      
74F0: 9F         SBC     A               
74F1: E7         RST     0X20            
74F2: 7E         LD      A,(HL)          
74F3: 9F         SBC     A               
74F4: BC         CP      H               
74F5: 1F         RRA                     
74F6: F0 1F      LD      A,($1F)         
74F8: F1         POP     AF              
74F9: 0E FF      LD      C,$FF           
74FB: 00         NOP                     
74FC: 01 00 01   LD      BC,$0100        
74FF: 00         NOP                     
7500: 07         RLCA                    
7501: 00         NOP                     
7502: 0F         RRCA                    
7503: 07         RLCA                    
7504: 0F         RRCA                    
7505: 00         NOP                     
7506: 1F         RRA                     
7507: 0F         RRCA                    
7508: 30 1F      JR      NC,$7529        
750A: 18 07      JR      $7513           
750C: 07         RLCA                    
750D: 00         NOP                     
750E: 0C         INC     C               
750F: 03         INC     BC              
7510: 13         INC     DE              
7511: 0F         RRCA                    
7512: 2C         INC     L               
7513: 03         INC     BC              
7514: 43         LD      B,E             
7515: 00         NOP                     
7516: 80         ADD     A,B             
7517: 00         NOP                     
7518: CF         RST     0X08            
7519: 80         ADD     A,B             
751A: BF         CP      A               
751B: C0         RET     NZ              
751C: 7F         LD      A,A             
751D: 80         ADD     A,B             
751E: F0 00      LD      A,($00)         
7520: 00         NOP                     
7521: 00         NOP                     
7522: 00         NOP                     
7523: 00         NOP                     
7524: 00         NOP                     
7525: 00         NOP                     
7526: 01 00 01   LD      BC,$0100        
7529: 00         NOP                     
752A: 02         LD      (BC),A          
752B: 01 02 01   LD      BC,$0102        
752E: 02         LD      (BC),A          
752F: 01 01 00   LD      BC,$0001        
7532: 00         NOP                     
7533: 00         NOP                     
7534: 00         NOP                     
7535: 00         NOP                     
7536: 00         NOP                     
7537: 00         NOP                     
7538: 00         NOP                     
7539: 00         NOP                     
753A: 00         NOP                     
753B: 00         NOP                     
753C: 00         NOP                     
753D: 00         NOP                     
753E: 00         NOP                     
753F: 00         NOP                     
7540: 0F         RRCA                    
7541: 00         NOP                     
7542: 70         LD      (HL),B          
7543: 0F         RRCA                    
7544: 80         ADD     A,B             
7545: 7F         LD      A,A             
7546: 00         NOP                     
7547: FF         RST     0X38            
7548: 00         NOP                     
7549: FF         RST     0X38            
754A: 01 FE 0F   LD      BC,$0FFE        
754D: F0 31      LD      A,($31)         
754F: C0         RET     NZ              
7550: 40         LD      B,B             
7551: 80         ADD     A,B             
7552: F3         DI                      
7553: 00         NOP                     
7554: 7E         LD      A,(HL)          
7555: 33         INC     SP              
7556: 7F         LD      A,A             
7557: 3E 5F      LD      A,$5F           
7559: 3F         CCF                     
755A: 4F         LD      C,A             
755B: 3F         CCF                     
755C: 7F         LD      A,A             
755D: 3F         CCF                     
755E: FF         RST     0X38            
755F: 7F         LD      A,A             
7560: 00         NOP                     
7561: 00         NOP                     
7562: C6 00      ADD     $00             
7564: 39         ADD     HL,SP           
7565: C6 0A      ADD     $0A             
7567: F4         ???                     
7568: 07         RLCA                    
7569: F8 87      LDHL    SP,$87          
756B: 7B         LD      A,E             
756C: 03         INC     BC              
756D: FD         ???                     
756E: C1         POP     BC              
756F: 3E F1      LD      A,$F1           
7571: 0E E0      LD      C,$E0           
7573: 1F         RRA                     
7574: FC         ???                     
7575: 03         INC     BC              
7576: C8         RET     Z               
7577: 37         SCF                     
7578: C8         RET     Z               
7579: B7         OR      A               
757A: 90         SUB     B               
757B: EF         RST     0X28            
757C: 90         SUB     B               
757D: EF         RST     0X28            
757E: 17         RLA                     
757F: E8 00      ADD     SP,$00          
7581: 00         NOP                     
7582: 00         NOP                     
7583: 00         NOP                     
7584: 80         ADD     A,B             
7585: 00         NOP                     
7586: 00         NOP                     
7587: 00         NOP                     
7588: 80         ADD     A,B             
7589: 00         NOP                     
758A: C0         RET     NZ              
758B: 80         ADD     A,B             
758C: F0 C0      LD      A,($C0)         
758E: F8 E0      LDHL    SP,$E0          
7590: F4         ???                     
7591: E8 F2      ADD     SP,$F2          
7593: 6C         LD      L,H             
7594: FA 74 F9   LD      A,($F974)       
7597: 76         HALT                    
7598: F9         LD      SP,HL           
7599: 76         HALT                    
759A: FB         EI                      
759B: 74         LD      (HL),H          
759C: FB         EI                      
759D: 04         INC     B               
759E: F9         LD      SP,HL           
759F: 76         HALT                    
75A0: FE 7F      CP      $7F             
75A2: F8 7F      LDHL    SP,$7F          
75A4: 40         LD      B,B             
75A5: 3F         CCF                     
75A6: 20 1F      JR      NZ,$75C7        
75A8: 1C         INC     E               
75A9: 03         INC     BC              
75AA: 03         INC     BC              
75AB: 00         NOP                     
75AC: 00         NOP                     
75AD: 00         NOP                     
75AE: 00         NOP                     
75AF: 00         NOP                     
75B0: 01 00 02   LD      BC,$0200        
75B3: 00         NOP                     
75B4: 04         INC     B               
75B5: 00         NOP                     
75B6: 04         INC     B               
75B7: 00         NOP                     
75B8: 04         INC     B               
75B9: 00         NOP                     
75BA: 08 00 08   LD      ($0800),SP      
75BD: 00         NOP                     
75BE: 08 00 2F   LD      ($2F00),SP      
75C1: D3         ???                     
75C2: 4F         LD      C,A             
75C3: B4         OR      H               
75C4: 4F         LD      C,A             
75C5: B7         OR      A               
75C6: 8F         ADC     A,A             
75C7: 76         HALT                    
75C8: 8E         ADC     A,(HL)          
75C9: 71         LD      (HL),C          
75CA: 8E         ADC     A,(HL)          
75CB: 75         LD      (HL),L          
75CC: 86         ADD     A,(HL)          
75CD: 79         LD      A,C             
75CE: 84         ADD     A,H             
75CF: 7B         LD      A,E             
75D0: 4F         LD      C,A             
75D1: 30 4C      JR      NC,$761F        
75D3: 30 2A      JR      NC,$75FF        
75D5: 14         INC     D               
75D6: 39         ADD     HL,SP           
75D7: 06 69      LD      B,$69           
75D9: 16 81      LD      D,$81           
75DB: 7E         LD      A,(HL)          
75DC: 81         ADD     A,C             
75DD: 7E         LD      A,(HL)          
75DE: 81         ADD     A,C             
75DF: 7C         LD      A,H             
75E0: 07         RLCA                    
75E1: 00         NOP                     
75E2: 78         LD      A,B             
75E3: 07         RLCA                    
75E4: 80         ADD     A,B             
75E5: 7F         LD      A,A             
75E6: C3 3C FF   JP      $FF3C           
75E9: C2 FF FC   JP      NZ,$FCFF        
75EC: FF         RST     0X38            
75ED: FF         RST     0X38            
75EE: F8 FF      LDHL    SP,$FF          
75F0: F0 AF      LD      A,($AF)         
75F2: F1         POP     AF              
75F3: 6E         LD      L,(HL)          
75F4: F6 68      OR      $68             
75F6: F8 60      LDHL    SP,$60          
75F8: F0 E0      LD      A,($E0)         
75FA: E0 C0      LDFF00  ($C0),A         
75FC: E0 80      LDFF00  ($80),A         
75FE: 80         ADD     A,B             
75FF: 00         NOP                     
7600: 7C         LD      A,H             
7601: 7C         LD      A,H             
7602: FF         RST     0X38            
7603: FF         RST     0X38            
7604: FF         RST     0X38            
7605: FF         RST     0X38            
7606: EF         RST     0X28            
7607: FF         RST     0X38            
7608: 00         NOP                     
7609: FF         RST     0X38            
760A: 00         NOP                     
760B: FF         RST     0X38            
760C: 03         INC     BC              
760D: FF         RST     0X38            
760E: 00         NOP                     
760F: FF         RST     0X38            
7610: E0 E0      LDFF00  ($E0),A         
7612: F0 F0      LD      A,($F0)         
7614: 7F         LD      A,A             
7615: FF         RST     0X38            
7616: 7F         LD      A,A             
7617: FF         RST     0X38            
7618: 19         ADD     HL,DE           
7619: FF         RST     0X38            
761A: 7F         LD      A,A             
761B: FF         RST     0X38            
761C: 9F         SBC     A               
761D: FF         RST     0X38            
761E: CF         RST     0X08            
761F: FF         RST     0X38            
7620: 00         NOP                     
7621: 00         NOP                     
7622: 00         NOP                     
7623: 00         NOP                     
7624: 00         NOP                     
7625: 00         NOP                     
7626: C0         RET     NZ              
7627: C0         RET     NZ              
7628: E0 E0      LDFF00  ($E0),A         
762A: E0 E0      LDFF00  ($E0),A         
762C: F0 F0      LD      A,($F0)         
762E: F0 F0      LD      A,($F0)         
7630: 00         NOP                     
7631: 00         NOP                     
7632: 00         NOP                     
7633: 00         NOP                     
7634: 00         NOP                     
7635: 00         NOP                     
7636: 01 01 07   LD      BC,$0701        
7639: 07         RLCA                    
763A: 0F         RRCA                    
763B: 0F         RRCA                    
763C: 1F         RRA                     
763D: 1F         RRA                     
763E: 1C         INC     E               
763F: 1F         RRA                     
7640: 0F         RRCA                    
7641: 0F         RRCA                    
7642: 1F         RRA                     
7643: 1F         RRA                     
7644: 3E 3F      LD      A,$3F           
7646: F8 FF      LDHL    SP,$FF          
7648: F0 FF      LD      A,($FF)         
764A: FE FF      CP      $FF             
764C: EF         RST     0X28            
764D: FF         RST     0X38            
764E: 1E FF      LD      E,$FF           
7650: 00         NOP                     
7651: 00         NOP                     
7652: 00         NOP                     
7653: 00         NOP                     
7654: 00         NOP                     
7655: 00         NOP                     
7656: 01 01 07   LD      BC,$0701        
7659: 07         RLCA                    
765A: 0F         RRCA                    
765B: 0F         RRCA                    
765C: 1F         RRA                     
765D: 1F         RRA                     
765E: 1F         RRA                     
765F: 1F         RRA                     
7660: 0F         RRCA                    
7661: 0F         RRCA                    
7662: 1F         RRA                     
7663: 1F         RRA                     
7664: 1C         INC     E               
7665: 1F         RRA                     
7666: D8         RET     C               
7667: DF         RST     0X18            
7668: F0 FF      LD      A,($FF)         
766A: FE FF      CP      $FF             
766C: 8F         ADC     A,A             
766D: FF         RST     0X38            
766E: 1F         RRA                     
766F: FF         RST     0X38            
7670: C6 FF      ADD     $FF             
7672: CE FF      ADC     $FF             
7674: CC FF DC   CALL    Z,$DCFF         
7677: FF         RST     0X38            
7678: 74         LD      (HL),H          
7679: FF         RST     0X38            
767A: 67         LD      H,A             
767B: FF         RST     0X38            
767C: C7         RST     0X00            
767D: FF         RST     0X38            
767E: 8F         ADC     A,A             
767F: FF         RST     0X38            
7680: 20 FF      JR      NZ,$7681        
7682: 20 FF      JR      NZ,$7683        
7684: 00         NOP                     
7685: FF         RST     0X38            
7686: 01 FF 01   LD      BC,$01FF        
7689: FF         RST     0X38            
768A: E0 FF      LDFF00  ($FF),A         
768C: 80         ADD     A,B             
768D: FF         RST     0X38            
768E: 00         NOP                     
768F: FF         RST     0X38            
7690: 00         NOP                     
7691: 00         NOP                     
7692: 80         ADD     A,B             
7693: 80         ADD     A,B             
7694: CF         RST     0X08            
7695: CF         RST     0X08            
7696: FF         RST     0X38            
7697: FF         RST     0X38            
7698: 7F         LD      A,A             
7699: FF         RST     0X38            
769A: 19         ADD     HL,DE           
769B: FF         RST     0X38            
769C: 7C         LD      A,H             
769D: FF         RST     0X38            
769E: 82         ADD     A,D             
769F: FF         RST     0X38            
76A0: F0 00      LD      A,($00)         
76A2: 7C         LD      A,H             
76A3: B0         OR      B               
76A4: FE 7C      CP      $7C             
76A6: FF         RST     0X38            
76A7: E2         LDFF00  (C),A           
76A8: FA 5C E4   LD      A,($E45C)       
76AB: B8         CP      B               
76AC: C8         RET     Z               
76AD: 70         LD      (HL),B          
76AE: 30 C0      JR      NC,$7670        
76B0: 40         LD      B,B             
76B1: 80         ADD     A,B             
76B2: 80         ADD     A,B             
76B3: 00         NOP                     
76B4: 00         NOP                     
76B5: 00         NOP                     
76B6: 00         NOP                     
76B7: 00         NOP                     
76B8: 00         NOP                     
76B9: 00         NOP                     
76BA: 00         NOP                     
76BB: 00         NOP                     
76BC: 00         NOP                     
76BD: 00         NOP                     
76BE: 00         NOP                     
76BF: 00         NOP                     
76C0: 00         NOP                     
76C1: 00         NOP                     
76C2: F8 00      LDHL    SP,$00          
76C4: 9E         SBC     (HL)            
76C5: 78         LD      A,B             
76C6: 6F         LD      L,A             
76C7: 1E 1F      LD      E,$1F           
76C9: 07         RLCA                    
76CA: 3F         CCF                     
76CB: 1F         RRA                     
76CC: F4         ???                     
76CD: 3F         CCF                     
76CE: FF         RST     0X38            
76CF: 70         LD      (HL),B          
76D0: F0 40      LD      A,($40)         
76D2: 40         LD      B,B             
76D3: 00         NOP                     
76D4: 00         NOP                     
76D5: 00         NOP                     
76D6: 00         NOP                     
76D7: 00         NOP                     
76D8: 00         NOP                     
76D9: 00         NOP                     
76DA: 00         NOP                     
76DB: 00         NOP                     
76DC: 00         NOP                     
76DD: 00         NOP                     
76DE: 00         NOP                     
76DF: 00         NOP                     
76E0: 00         NOP                     
76E1: 00         NOP                     
76E2: 00         NOP                     
76E3: 00         NOP                     
76E4: 00         NOP                     
76E5: 00         NOP                     
76E6: F8 00      LDHL    SP,$00          
76E8: FF         RST     0X38            
76E9: 78         LD      A,B             
76EA: E7         RST     0X20            
76EB: 3F         CCF                     
76EC: 7F         LD      A,A             
76ED: 07         RLCA                    
76EE: 1E 0F      LD      E,$0F           
76F0: 78         LD      A,B             
76F1: 1F         RRA                     
76F2: F9         LD      SP,HL           
76F3: 7E         LD      A,(HL)          
76F4: 7E         LD      A,(HL)          
76F5: 00         NOP                     
76F6: 00         NOP                     
76F7: 00         NOP                     
76F8: 00         NOP                     
76F9: 00         NOP                     
76FA: 00         NOP                     
76FB: 00         NOP                     
76FC: 00         NOP                     
76FD: 00         NOP                     
76FE: 00         NOP                     
76FF: 00         NOP                     
7700: 00         NOP                     
7701: 40         LD      B,B             
7702: 00         NOP                     
7703: 20 00      JR      NZ,$7705        
7705: A2         AND     D               
7706: 00         NOP                     
7707: 49         LD      C,C             
7708: 00         NOP                     
7709: 85         ADD     A,L             
770A: 80         ADD     A,B             
770B: A5         AND     L               
770C: 80         ADD     A,B             
770D: A0         AND     B               
770E: 00         NOP                     
770F: A8         XOR     B               
7710: 67         LD      H,A             
7711: FF         RST     0X38            
7712: 23         INC     HL              
7713: FF         RST     0X38            
7714: 03         INC     BC              
7715: FF         RST     0X38            
7716: 07         RLCA                    
7717: FF         RST     0X38            
7718: 3D         DEC     A               
7719: FF         RST     0X38            
771A: 0F         RRCA                    
771B: FF         RST     0X38            
771C: 03         INC     BC              
771D: FF         RST     0X38            
771E: 00         NOP                     
771F: FF         RST     0X38            
7720: F0 F0      LD      A,($F0)         
7722: 60         LD      H,B             
7723: E0 40      LDFF00  ($40),A         
7725: E0 FC      LDFF00  ($FC),A         
7727: FC         ???                     
7728: FE FE      CP      $FE             
772A: BF         CP      A               
772B: FF         RST     0X38            
772C: CF         RST     0X08            
772D: FF         RST     0X38            
772E: C3 FF 08   JP      $08FF           
7731: 1F         RRA                     
7732: 00         NOP                     
7733: 1F         RRA                     
7734: 00         NOP                     
7735: 1F         RRA                     
7736: 0C         INC     C               
7737: 1F         RRA                     
7738: 38 3F      JR      C,$7779         
773A: 79         LD      A,C             
773B: 7F         LD      A,A             
773C: 6B         LD      L,E             
773D: 7F         LD      A,A             
773E: 67         LD      H,A             
773F: 7F         LD      A,A             
7740: 38 FF      JR      C,$7741         
7742: 30 FF      JR      NC,$7743        
7744: 20 FF      JR      NZ,$7745        
7746: 2C         INC     L               
7747: FF         RST     0X38            
7748: 3F         CCF                     
7749: FF         RST     0X38            
774A: FC         ???                     
774B: FF         RST     0X38            
774C: F0 FF      LD      A,($FF)         
774E: 60         LD      H,B             
774F: FF         RST     0X38            
7750: 02         LD      (BC),A          
7751: 1F         RRA                     
7752: 07         RLCA                    
7753: 1F         RRA                     
7754: 06 1F      LD      B,$1F           
7756: 0C         INC     C               
7757: 1F         RRA                     
7758: 18 3F      JR      $7799           
775A: 79         LD      A,C             
775B: 7F         LD      A,A             
775C: 6B         LD      L,E             
775D: 7F         LD      A,A             
775E: 67         LD      H,A             
775F: 7F         LD      A,A             
7760: 79         LD      A,C             
7761: FF         RST     0X38            
7762: F6 FF      OR      $FF             
7764: 6F         LD      L,A             
7765: FF         RST     0X38            
7766: FC         ???                     
7767: FF         RST     0X38            
7768: FF         RST     0X38            
7769: FF         RST     0X38            
776A: FC         ???                     
776B: FF         RST     0X38            
776C: F0 FF      LD      A,($FF)         
776E: 60         LD      H,B             
776F: FF         RST     0X38            
7770: 9C         SBC     H               
7771: FF         RST     0X38            
7772: 1C         INC     E               
7773: FF         RST     0X38            
7774: 18 FF      JR      $7775           
7776: 18 FF      JR      $7777           
7778: 10 FF      STOP    $FF             
777A: 00         NOP                     
777B: FF         RST     0X38            
777C: 00         NOP                     
777D: FF         RST     0X38            
777E: 00         NOP                     
777F: FF         RST     0X38            
7780: 02         LD      (BC),A          
7781: 83         ADD     A,E             
7782: 00         NOP                     
7783: 93         SUB     E               
7784: 00         NOP                     
7785: 16 00      LD      D,$00           
7787: 13         INC     DE              
7788: 00         NOP                     
7789: 4A         LD      C,D             
778A: 00         NOP                     
778B: 49         LD      C,C             
778C: 00         NOP                     
778D: 24         INC     H               
778E: 00         NOP                     
778F: 10 00      STOP    $00             
7791: 00         NOP                     
7792: 00         NOP                     
7793: 00         NOP                     
7794: 00         NOP                     
7795: 00         NOP                     
7796: 80         ADD     A,B             
7797: 80         ADD     A,B             
7798: F0 F0      LD      A,($F0)         
779A: FF         RST     0X38            
779B: FF         RST     0X38            
779C: 47         LD      B,A             
779D: FF         RST     0X38            
779E: 39         ADD     HL,SP           
779F: FF         RST     0X38            
77A0: BF         CP      A               
77A1: FF         RST     0X38            
77A2: 9F         SBC     A               
77A3: FF         RST     0X38            
77A4: 2F         CPL                     
77A5: FF         RST     0X38            
77A6: 1F         RRA                     
77A7: 7F         LD      A,A             
77A8: 27         DAA                     
77A9: BF         CP      A               
77AA: 16 7F      LD      D,$7F           
77AC: 20 7F      JR      NZ,$782D        
77AE: 13         INC     DE              
77AF: 3F         CCF                     
77B0: 00         NOP                     
77B1: 00         NOP                     
77B2: 00         NOP                     
77B3: 00         NOP                     
77B4: 00         NOP                     
77B5: 00         NOP                     
77B6: 00         NOP                     
77B7: 00         NOP                     
77B8: 00         NOP                     
77B9: 00         NOP                     
77BA: C0         RET     NZ              
77BB: C0         RET     NZ              
77BC: E0 E0      LDFF00  ($E0),A         
77BE: F0 F0      LD      A,($F0)         
77C0: FC         ???                     
77C1: FF         RST     0X38            
77C2: FD         ???                     
77C3: FF         RST     0X38            
77C4: F1         POP     AF              
77C5: FF         RST     0X38            
77C6: FA FF F0   LD      A,($F0FF)       
77C9: FF         RST     0X38            
77CA: 24         INC     H               
77CB: FE 48      CP      $48             
77CD: FD         ???                     
77CE: 00         NOP                     
77CF: FA 40 E8   LD      A,($E840)       
77D2: 40         LD      B,B             
77D3: E8 40      ADD     SP,$40          
77D5: E0 00      LDFF00  ($00),A         
77D7: C2 00 C2   JP      NZ,$C200        
77DA: 00         NOP                     
77DB: 24         INC     H               
77DC: 00         NOP                     
77DD: 40         LD      B,B             
77DE: 00         NOP                     
77DF: 80         ADD     A,B             
77E0: 00         NOP                     
77E1: 00         NOP                     
77E2: 00         NOP                     
77E3: 08 00 04   LD      ($0400),SP      
77E6: 00         NOP                     
77E7: 20 00      JR      NZ,$77E9        
77E9: 10 00      STOP    $00             
77EB: 08 00 00   LD      ($0000),SP      
77EE: 00         NOP                     
77EF: 00         NOP                     
77F0: 00         NOP                     
77F1: 3F         CCF                     
77F2: 00         NOP                     
77F3: 99         SBC     C               
77F4: 00         NOP                     
77F5: 67         LD      H,A             
77F6: 00         NOP                     
77F7: 00         NOP                     
77F8: 00         NOP                     
77F9: 03         INC     BC              
77FA: 00         NOP                     
77FB: 40         LD      B,B             
77FC: 00         NOP                     
77FD: 30 00      JR      NC,$77FF        
77FF: 01 00 00   LD      BC,$0000        
7802: 00         NOP                     
7803: 00         NOP                     
7804: 00         NOP                     
7805: 00         NOP                     
7806: 00         NOP                     
7807: 00         NOP                     
7808: 01 00 02   LD      BC,$0200        
780B: 01 07 00   LD      BC,$0007        
780E: 0E 01      LD      C,$01           
7810: 18 07      JR      $7819           
7812: 10 0F      STOP    $0F             
7814: 20 1F      JR      NZ,$7835        
7816: 20 1F      JR      NZ,$7837        
7818: 40         LD      B,B             
7819: 3F         CCF                     
781A: 40         LD      B,B             
781B: 3F         CCF                     
781C: 80         ADD     A,B             
781D: 7F         LD      A,A             
781E: 80         ADD     A,B             
781F: 77         LD      (HL),A          
7820: 00         NOP                     
7821: 00         NOP                     
7822: 07         RLCA                    
7823: 00         NOP                     
7824: 38 07      JR      C,$782D         
7826: 60         LD      H,B             
7827: 1F         RRA                     
7828: 80         ADD     A,B             
7829: 7F         LD      A,A             
782A: 70         LD      (HL),B          
782B: 8F         ADC     A,A             
782C: 80         ADD     A,B             
782D: 7F         LD      A,A             
782E: 00         NOP                     
782F: FF         RST     0X38            
7830: 00         NOP                     
7831: FF         RST     0X38            
7832: 00         NOP                     
7833: FF         RST     0X38            
7834: 00         NOP                     
7835: FF         RST     0X38            
7836: 00         NOP                     
7837: FF         RST     0X38            
7838: 00         NOP                     
7839: FF         RST     0X38            
783A: 00         NOP                     
783B: FF         RST     0X38            
783C: 20 DF      JR      NZ,$781D        
783E: 40         LD      B,B             
783F: 3F         CCF                     
7840: FE 00      CP      $00             
7842: 81         ADD     A,C             
7843: 7E         LD      A,(HL)          
7844: 70         LD      (HL),B          
7845: 8F         ADC     A,A             
7846: 0C         INC     C               
7847: F3         DI                      
7848: 00         NOP                     
7849: FF         RST     0X38            
784A: 00         NOP                     
784B: FF         RST     0X38            
784C: 00         NOP                     
784D: FF         RST     0X38            
784E: 00         NOP                     
784F: FF         RST     0X38            
7850: 00         NOP                     
7851: FF         RST     0X38            
7852: 00         NOP                     
7853: FF         RST     0X38            
7854: 00         NOP                     
7855: FF         RST     0X38            
7856: 00         NOP                     
7857: FF         RST     0X38            
7858: 00         NOP                     
7859: FF         RST     0X38            
785A: 00         NOP                     
785B: FF         RST     0X38            
785C: 00         NOP                     
785D: F3         DI                      
785E: 18 C7      JR      $7827           
7860: 01 00 E2   LD      BC,$E200        
7863: 01 3C C3   LD      BC,$C33C        
7866: 06 F9      LD      B,$F9           
7868: 01 FE 00   LD      BC,$00FE        
786B: FF         RST     0X38            
786C: 00         NOP                     
786D: FF         RST     0X38            
786E: 00         NOP                     
786F: FF         RST     0X38            
7870: 00         NOP                     
7871: FF         RST     0X38            
7872: 00         NOP                     
7873: FF         RST     0X38            
7874: 00         NOP                     
7875: FF         RST     0X38            
7876: 00         NOP                     
7877: FF         RST     0X38            
7878: 00         NOP                     
7879: FE 00      CP      $00             
787B: F8 00      LDHL    SP,$00          
787D: C0         RET     NZ              
787E: 00         NOP                     
787F: 00         NOP                     
7880: C0         RET     NZ              
7881: 00         NOP                     
7882: 30 C0      JR      NC,$7844        
7884: 18 C0      JR      $7846           
7886: 20 80      JR      NZ,$7808        
7888: 40         LD      B,B             
7889: 00         NOP                     
788A: 40         LD      B,B             
788B: 00         NOP                     
788C: 40         LD      B,B             
788D: 00         NOP                     
788E: 70         LD      (HL),B          
788F: 00         NOP                     
7890: 78         LD      A,B             
7891: 80         ADD     A,B             
7892: 3C         INC     A               
7893: 88         ADC     A,B             
7894: 1E 84      LD      E,$84           
7896: 0F         RRCA                    
7897: 06 07      LD      B,$07           
7899: 02         LD      (BC),A          
789A: 07         RLCA                    
789B: 01 13 01   LD      BC,$0113        
789E: 73         LD      (HL),E          
789F: 01 00 00   LD      BC,$0000        
78A2: 00         NOP                     
78A3: 00         NOP                     
78A4: 00         NOP                     
78A5: 00         NOP                     
78A6: 00         NOP                     
78A7: 00         NOP                     
78A8: 00         NOP                     
78A9: 00         NOP                     
78AA: 00         NOP                     
78AB: 00         NOP                     
78AC: 00         NOP                     
78AD: 00         NOP                     
78AE: 00         NOP                     
78AF: 00         NOP                     
78B0: 00         NOP                     
78B1: 00         NOP                     
78B2: 00         NOP                     
78B3: 00         NOP                     
78B4: 00         NOP                     
78B5: 00         NOP                     
78B6: 00         NOP                     
78B7: 00         NOP                     
78B8: 80         ADD     A,B             
78B9: 00         NOP                     
78BA: C0         RET     NZ              
78BB: 00         NOP                     
78BC: B8         CP      B               
78BD: 00         NOP                     
78BE: BC         CP      H               
78BF: 18 80      JR      $7841           
78C1: 6E         LD      L,(HL)          
78C2: 91         SUB     C               
78C3: 4C         LD      C,H             
78C4: 91         SUB     C               
78C5: 48         LD      C,B             
78C6: A1         AND     C               
78C7: 18 A2      JR      $786B           
78C9: 10 62      STOP    $62             
78CB: 10 62      STOP    $62             
78CD: 10 22      STOP    $22             
78CF: 00         NOP                     
78D0: 12         LD      (DE),A          
78D1: 00         NOP                     
78D2: 0A         LD      A,(BC)          
78D3: 00         NOP                     
78D4: 05         DEC     B               
78D5: 00         NOP                     
78D6: 03         INC     BC              
78D7: 00         NOP                     
78D8: 00         NOP                     
78D9: 00         NOP                     
78DA: 00         NOP                     
78DB: 00         NOP                     
78DC: 00         NOP                     
78DD: 00         NOP                     
78DE: 00         NOP                     
78DF: 00         NOP                     
78E0: C0         RET     NZ              
78E1: 3F         CCF                     
78E2: 40         LD      B,B             
78E3: 3C         INC     A               
78E4: 81         ADD     A,C             
78E5: 78         LD      A,B             
78E6: 83         ADD     A,E             
78E7: 70         LD      (HL),B          
78E8: 87         ADD     A,A             
78E9: 60         LD      H,B             
78EA: 87         ADD     A,A             
78EB: 61         LD      H,C             
78EC: 87         ADD     A,A             
78ED: 41         LD      B,C             
78EE: 4F         LD      C,A             
78EF: 02         LD      (BC),A          
78F0: 4F         LD      C,A             
78F1: 05         DEC     B               
78F2: 2F         CPL                     
78F3: 04         INC     B               
78F4: 2F         CPL                     
78F5: 06 3F      LD      B,$3F           
78F7: 06 9F      LD      B,$9F           
78F9: 06 1F      LD      B,$1F           
78FB: 06 1F      LD      B,$1F           
78FD: 07         RLCA                    
78FE: 1F         RRA                     
78FF: 07         RLCA                    
7900: 30 0C      JR      NC,$790E        
7902: 53         LD      D,E             
7903: 28 EF      JR      Z,$78F4         
7905: 53         LD      D,E             
7906: FF         RST     0X38            
7907: 4F         LD      C,A             
7908: FF         RST     0X38            
7909: 1E FF      LD      E,$FF           
790B: BE         CP      (HL)            
790C: FF         RST     0X38            
790D: FD         ???                     
790E: FF         RST     0X38            
790F: 3F         CCF                     
7910: FF         RST     0X38            
7911: 1F         RRA                     
7912: FF         RST     0X38            
7913: 1F         RRA                     
7914: FF         RST     0X38            
7915: 6F         LD      L,A             
7916: FF         RST     0X38            
7917: 0F         RRCA                    
7918: FF         RST     0X38            
7919: FF         RST     0X38            
791A: FF         RST     0X38            
791B: FF         RST     0X38            
791C: 87         ADD     A,A             
791D: 7F         LD      A,A             
791E: C3 BF FF   JP      $FFBF           
7921: 00         NOP                     
7922: 80         ADD     A,B             
7923: FF         RST     0X38            
7924: FE C1      CP      $C1             
7926: FF         RST     0X38            
7927: 00         NOP                     
7928: FC         ???                     
7929: 3F         CCF                     
792A: FE FF      CP      $FF             
792C: FE C7      CP      $C7             
792E: FC         ???                     
792F: A3         AND     E               
7930: FE 05      CP      $05             
7932: FE CF      CP      $CF             
7934: FC         ???                     
7935: C7         RST     0X00            
7936: F8 FF      LDHL    SP,$FF          
7938: FC         ???                     
7939: FF         RST     0X38            
793A: FE FF      CP      $FF             
793C: FE FF      CP      $FF             
793E: FC         ???                     
793F: FF         RST     0X38            
7940: A3         AND     E               
7941: 41         LD      B,C             
7942: 41         LD      B,C             
7943: 80         ADD     A,B             
7944: 41         LD      B,C             
7945: 80         ADD     A,B             
7946: 41         LD      B,C             
7947: A0         AND     B               
7948: 43         LD      B,E             
7949: B1         OR      C               
794A: 43         LD      B,E             
794B: B1         OR      C               
794C: 43         LD      B,E             
794D: B1         OR      C               
794E: 47         LD      B,A             
794F: B2         OR      D               
7950: 47         LD      B,A             
7951: B2         OR      D               
7952: 27         DAA                     
7953: DA 26 DA   JP      C,$DA26         
7956: 16 EA      LD      D,$EA           
7958: 16 EB      LD      D,$EB           
795A: 13         INC     DE              
795B: E9         JP      (HL)            
795C: 23         INC     HL              
795D: DD         ???                     
795E: 21 DE FC   LD      HL,$FCDE        
7961: 38 FC      JR      C,$795F         
7963: 78         LD      A,B             
7964: EC         ???                     
7965: D8         RET     C               
7966: CC 98 CE   CALL    Z,$CE98         
7969: B8         CP      B               
796A: 9E         SBC     (HL)            
796B: 38 9D      JR      C,$790A         
796D: 78         LD      A,B             
796E: 39         ADD     HL,SP           
796F: 70         LD      (HL),B          
7970: 39         ADD     HL,SP           
7971: F0 39      LD      A,($39)         
7973: F0 79      LD      A,($79)         
7975: F0 79      LD      A,($79)         
7977: E0 F2      LDFF00  ($F2),A         
7979: E0 E2      LDFF00  ($E2),A         
797B: C0         RET     NZ              
797C: E2         LDFF00  (C),A           
797D: C0         RET     NZ              
797E: E2         LDFF00  (C),A           
797F: C0         RET     NZ              
7980: 2F         CPL                     
7981: 17         RLA                     
7982: 2F         CPL                     
7983: 17         RLA                     
7984: 2F         CPL                     
7985: 17         RLA                     
7986: 4F         LD      C,A             
7987: 37         SCF                     
7988: 4F         LD      C,A             
7989: 37         SCF                     
798A: 47         LD      B,A             
798B: 3B         DEC     SP              
798C: 47         LD      B,A             
798D: 3B         DEC     SP              
798E: 43         LD      B,E             
798F: 39         ADD     HL,SP           
7990: 41         LD      B,C             
7991: 38 40      JR      C,$79D3         
7993: 38 40      JR      C,$79D5         
7995: 38 40      JR      C,$79D7         
7997: 38 40      JR      C,$79D9         
7999: 38 20      JR      C,$79BB         
799B: 18 20      JR      $79BD           
799D: 10 20      STOP    $20             
799F: 00         NOP                     
79A0: E7         RST     0X20            
79A1: DF         RST     0X18            
79A2: FF         RST     0X38            
79A3: FF         RST     0X38            
79A4: FE FF      CP      $FF             
79A6: FF         RST     0X38            
79A7: E0 FF      LDFF00  ($FF),A         
79A9: EF         RST     0X28            
79AA: FF         RST     0X38            
79AB: F0 FF      LD      A,($FF)         
79AD: F0 F7      LD      A,($F7)         
79AF: F0 FF      LD      A,($FF)         
79B1: FF         RST     0X38            
79B2: F9         LD      SP,HL           
79B3: 7F         LD      A,A             
79B4: 7F         LD      A,A             
79B5: 3F         CCF                     
79B6: 4E         LD      C,(HL)          
79B7: 3F         CCF                     
79B8: A0         AND     B               
79B9: 1F         RRA                     
79BA: 90         SUB     B               
79BB: 0F         RRCA                    
79BC: 8F         ADC     A,A             
79BD: 00         NOP                     
79BE: 84         ADD     A,H             
79BF: 03         INC     BC              
79C0: FC         ???                     
79C1: FF         RST     0X38            
79C2: FC         ???                     
79C3: FF         RST     0X38            
79C4: FC         ???                     
79C5: FF         RST     0X38            
79C6: 78         LD      A,B             
79C7: 7F         LD      A,A             
79C8: F8 7F      LDHL    SP,$7F          
79CA: F8 7F      LDHL    SP,$7F          
79CC: F0 7F      LD      A,($7F)         
79CE: F0 FF      LD      A,($FF)         
79D0: E0 FF      LDFF00  ($FF),A         
79D2: C4 FB 88   CALL    NZ,$88FB        
79D5: F7         RST     0X30            
79D6: 10 EF      STOP    $EF             
79D8: 20 DF      JR      NZ,$79B9        
79DA: C0         RET     NZ              
79DB: 3F         CCF                     
79DC: 00         NOP                     
79DD: FF         RST     0X38            
79DE: 00         NOP                     
79DF: FF         RST     0X38            
79E0: 21 DE 41   LD      HL,$41DE        
79E3: BE         CP      (HL)            
79E4: 41         LD      B,C             
79E5: BE         CP      (HL)            
79E6: 41         LD      B,C             
79E7: BE         CP      (HL)            
79E8: 40         LD      B,B             
79E9: BE         CP      (HL)            
79EA: 40         LD      B,B             
79EB: BE         CP      (HL)            
79EC: 40         LD      B,B             
79ED: BE         CP      (HL)            
79EE: 80         ADD     A,B             
79EF: 7C         LD      A,H             
79F0: 80         ADD     A,B             
79F1: 7C         LD      A,H             
79F2: 80         ADD     A,B             
79F3: 7C         LD      A,H             
79F4: 80         ADD     A,B             
79F5: 7C         LD      A,H             
79F6: 80         ADD     A,B             
79F7: 38 80      JR      C,$7979         
79F9: 38 40      JR      C,$7A3B         
79FB: 90         SUB     B               
79FC: 41         LD      B,C             
79FD: 80         ADD     A,B             
79FE: 41         LD      B,C             
79FF: 80         ADD     A,B             
7A00: C2 80 C2   JP      NZ,$C280        
7A03: 00         NOP                     
7A04: A2         AND     D               
7A05: 40         LD      B,B             
7A06: 91         SUB     C               
7A07: 60         LD      H,B             
7A08: 91         SUB     C               
7A09: 60         LD      H,B             
7A0A: 89         ADC     A,C             
7A0B: 70         LD      (HL),B          
7A0C: 8B         ADC     A,E             
7A0D: 60         LD      H,B             
7A0E: 8B         ADC     A,E             
7A0F: 60         LD      H,B             
7A10: 8A         ADC     A,D             
7A11: 40         LD      B,B             
7A12: 92         SUB     D               
7A13: 40         LD      B,B             
7A14: 92         SUB     D               
7A15: 00         NOP                     
7A16: B2         OR      D               
7A17: 00         NOP                     
7A18: B6         OR      (HL)            
7A19: 00         NOP                     
7A1A: F6 00      OR      $00             
7A1C: FE 00      CP      $00             
7A1E: FE 00      CP      $00             
7A20: 10 00      STOP    $00             
7A22: 10 00      STOP    $00             
7A24: 10 00      STOP    $00             
7A26: 08 00 08   LD      ($0800),SP      
7A29: 00         NOP                     
7A2A: 04         INC     B               
7A2B: 00         NOP                     
7A2C: 04         INC     B               
7A2D: 00         NOP                     
7A2E: 0C         INC     C               
7A2F: 00         NOP                     
7A30: 15         DEC     D               
7A31: 00         NOP                     
7A32: 65         LD      H,L             
7A33: 00         NOP                     
7A34: 85         ADD     A,L             
7A35: 00         NOP                     
7A36: 02         LD      (BC),A          
7A37: 00         NOP                     
7A38: 00         NOP                     
7A39: 00         NOP                     
7A3A: 00         NOP                     
7A3B: 00         NOP                     
7A3C: 00         NOP                     
7A3D: 00         NOP                     
7A3E: 00         NOP                     
7A3F: 00         NOP                     
7A40: 86         ADD     A,(HL)          
7A41: 03         INC     BC              
7A42: 87         ADD     A,A             
7A43: 03         INC     BC              
7A44: 8F         ADC     A,A             
7A45: 07         RLCA                    
7A46: BF         CP      A               
7A47: 0F         RRCA                    
7A48: FF         RST     0X38            
7A49: 3F         CCF                     
7A4A: FF         RST     0X38            
7A4B: 7F         LD      A,A             
7A4C: FF         RST     0X38            
7A4D: 3F         CCF                     
7A4E: BF         CP      A               
7A4F: 1F         RRA                     
7A50: 9F         SBC     A               
7A51: 07         RLCA                    
7A52: 07         RLCA                    
7A53: 01 02 01   LD      BC,$0102        
7A56: 02         LD      (BC),A          
7A57: 01 0F 00   LD      BC,$000F        
7A5A: 09         ADD     HL,BC           
7A5B: 06 06      LD      B,$06           
7A5D: 01 05 02   LD      BC,$0205        
7A60: 00         NOP                     
7A61: FF         RST     0X38            
7A62: FC         ???                     
7A63: FF         RST     0X38            
7A64: FF         RST     0X38            
7A65: FF         RST     0X38            
7A66: FF         RST     0X38            
7A67: FF         RST     0X38            
7A68: FF         RST     0X38            
7A69: FF         RST     0X38            
7A6A: FF         RST     0X38            
7A6B: FF         RST     0X38            
7A6C: FF         RST     0X38            
7A6D: FF         RST     0X38            
7A6E: FF         RST     0X38            
7A6F: FC         ???                     
7A70: FC         ???                     
7A71: E0 F0      LDFF00  ($F0),A         
7A73: E0 F0      LDFF00  ($F0),A         
7A75: E0 FC      LDFF00  ($FC),A         
7A77: C0         RET     NZ              
7A78: E4         ???                     
7A79: 98         SBC     B               
7A7A: 98         SBC     B               
7A7B: 60         LD      H,B             
7A7C: 70         LD      (HL),B          
7A7D: 80         ADD     A,B             
7A7E: 88         ADC     A,B             
7A7F: 70         LD      (HL),B          
7A80: 21 C0 21   LD      HL,$21C0        
7A83: C0         RET     NZ              
7A84: 21 C0 91   LD      HL,$91C0        
7A87: E0 D1      LDFF00  ($D1),A         
7A89: E0 FA      LDFF00  ($FA),A         
7A8B: E0 FA      LDFF00  ($FA),A         
7A8D: 80         ADD     A,B             
7A8E: 8A         ADC     A,D             
7A8F: 00         NOP                     
7A90: 04         INC     B               
7A91: 00         NOP                     
7A92: 00         NOP                     
7A93: 00         NOP                     
7A94: 00         NOP                     
7A95: 00         NOP                     
7A96: 00         NOP                     
7A97: 00         NOP                     
7A98: 00         NOP                     
7A99: 00         NOP                     
7A9A: 00         NOP                     
7A9B: 00         NOP                     
7A9C: 00         NOP                     
7A9D: 00         NOP                     
7A9E: 00         NOP                     
7A9F: 00         NOP                     
7AA0: FE 00      CP      $00             
7AA2: FE 00      CP      $00             
7AA4: 1C         INC     E               
7AA5: 00         NOP                     
7AA6: 06 00      LD      B,$00           
7AA8: 03         INC     BC              
7AA9: 00         NOP                     
7AAA: 00         NOP                     
7AAB: 00         NOP                     
7AAC: 00         NOP                     
7AAD: 00         NOP                     
7AAE: 00         NOP                     
7AAF: 00         NOP                     
7AB0: 00         NOP                     
7AB1: 00         NOP                     
7AB2: 00         NOP                     
7AB3: 00         NOP                     
7AB4: 00         NOP                     
7AB5: 00         NOP                     
7AB6: 00         NOP                     
7AB7: 00         NOP                     
7AB8: 00         NOP                     
7AB9: 00         NOP                     
7ABA: 00         NOP                     
7ABB: 00         NOP                     
7ABC: 00         NOP                     
7ABD: 00         NOP                     
7ABE: 00         NOP                     
7ABF: 00         NOP                     
7AC0: 00         NOP                     
7AC1: 00         NOP                     
7AC2: 00         NOP                     
7AC3: 00         NOP                     
7AC4: 00         NOP                     
7AC5: 00         NOP                     
7AC6: 00         NOP                     
7AC7: 00         NOP                     
7AC8: F0 00      LD      A,($00)         
7ACA: 0F         RRCA                    
7ACB: 00         NOP                     
7ACC: 00         NOP                     
7ACD: 00         NOP                     
7ACE: 00         NOP                     
7ACF: 00         NOP                     
7AD0: 00         NOP                     
7AD1: 00         NOP                     
7AD2: 01 00 01   LD      BC,$0100        
7AD5: 00         NOP                     
7AD6: 01 00 01   LD      BC,$0100        
7AD9: 00         NOP                     
7ADA: 02         LD      (BC),A          
7ADB: 01 02 01   LD      BC,$0102        
7ADE: 02         LD      (BC),A          
7ADF: 01 00 00   LD      BC,$0000        
7AE2: 00         NOP                     
7AE3: 00         NOP                     
7AE4: 00         NOP                     
7AE5: 00         NOP                     
7AE6: 00         NOP                     
7AE7: 00         NOP                     
7AE8: 00         NOP                     
7AE9: 00         NOP                     
7AEA: C0         RET     NZ              
7AEB: 00         NOP                     
7AEC: 70         LD      (HL),B          
7AED: 00         NOP                     
7AEE: C8         RET     Z               
7AEF: 30 84      JR      NC,$7A75        
7AF1: 78         LD      A,B             
7AF2: 82         ADD     A,D             
7AF3: 7C         LD      A,H             
7AF4: 02         LD      (BC),A          
7AF5: FC         ???                     
7AF6: 02         LD      (BC),A          
7AF7: FC         ???                     
7AF8: 02         LD      (BC),A          
7AF9: FC         ???                     
7AFA: 01 FE 01   LD      BC,$01FE        
7AFD: FE 01      CP      $01             
7AFF: FE 05      CP      $05             
7B01: 02         LD      (BC),A          
7B02: 04         INC     B               
7B03: 03         INC     BC              
7B04: 04         INC     B               
7B05: 03         INC     BC              
7B06: 04         INC     B               
7B07: 03         INC     BC              
7B08: 04         INC     B               
7B09: 03         INC     BC              
7B0A: 06 01      LD      B,$01           
7B0C: 06 01      LD      B,$01           
7B0E: 05         DEC     B               
7B0F: 02         LD      (BC),A          
7B10: 04         INC     B               
7B11: 03         INC     BC              
7B12: 04         INC     B               
7B13: 03         INC     BC              
7B14: 06 01      LD      B,$01           
7B16: 02         LD      (BC),A          
7B17: 01 02 01   LD      BC,$0102        
7B1A: 02         LD      (BC),A          
7B1B: 01 02 01   LD      BC,$0102        
7B1E: 02         LD      (BC),A          
7B1F: 01 80 00   LD      BC,$0080        
7B22: 80         ADD     A,B             
7B23: 00         NOP                     
7B24: C0         RET     NZ              
7B25: 00         NOP                     
7B26: C0         RET     NZ              
7B27: 00         NOP                     
7B28: C0         RET     NZ              
7B29: 00         NOP                     
7B2A: E0 00      LDFF00  ($00),A         
7B2C: 60         LD      H,B             
7B2D: 80         ADD     A,B             
7B2E: 70         LD      (HL),B          
7B2F: 80         ADD     A,B             
7B30: 78         LD      A,B             
7B31: 80         ADD     A,B             
7B32: 7C         LD      A,H             
7B33: 80         ADD     A,B             
7B34: 7E         LD      A,(HL)          
7B35: 80         ADD     A,B             
7B36: 3F         CCF                     
7B37: C0         RET     NZ              
7B38: 3F         CCF                     
7B39: C0         RET     NZ              
7B3A: 3F         CCF                     
7B3B: C0         RET     NZ              
7B3C: 1F         RRA                     
7B3D: E0 1F      LDFF00  ($1F),A         
7B3F: E0 0B      LDFF00  ($0B),A         
7B41: 04         INC     B               
7B42: 0D         DEC     C               
7B43: 00         NOP                     
7B44: 07         RLCA                    
7B45: 00         NOP                     
7B46: 04         INC     B               
7B47: 03         INC     BC              
7B48: 03         INC     BC              
7B49: 00         NOP                     
7B4A: 02         LD      (BC),A          
7B4B: 01 05 02   LD      BC,$0205        
7B4E: 06 00      LD      B,$00           
7B50: 00         NOP                     
7B51: 00         NOP                     
7B52: 00         NOP                     
7B53: 00         NOP                     
7B54: 00         NOP                     
7B55: 00         NOP                     
7B56: E0 00      LDFF00  ($00),A         
7B58: F0 00      LD      A,($00)         
7B5A: EC         ???                     
7B5B: 00         NOP                     
7B5C: F7         RST     0X30            
7B5D: 00         NOP                     
7B5E: F9         LD      SP,HL           
7B5F: 00         NOP                     
7B60: F0 00      LD      A,($00)         
7B62: 7C         LD      A,H             
7B63: C0         RET     NZ              
7B64: 28 D0      JR      Z,$7B36         
7B66: D0         RET     NC              
7B67: 20 30      JR      NZ,$7B99        
7B69: C0         RET     NZ              
7B6A: C8         RET     Z               
7B6B: 30 B4      JR      NC,$7B21        
7B6D: 48         LD      C,B             
7B6E: EC         ???                     
7B6F: 00         NOP                     
7B70: 20 00      JR      NZ,$7B72        
7B72: 00         NOP                     
7B73: 00         NOP                     
7B74: 00         NOP                     
7B75: 00         NOP                     
7B76: 00         NOP                     
7B77: 00         NOP                     
7B78: 00         NOP                     
7B79: 00         NOP                     
7B7A: 00         NOP                     
7B7B: 00         NOP                     
7B7C: 00         NOP                     
7B7D: 00         NOP                     
7B7E: 80         ADD     A,B             
7B7F: 00         NOP                     
7B80: 00         NOP                     
7B81: 00         NOP                     
7B82: 00         NOP                     
7B83: 00         NOP                     
7B84: 00         NOP                     
7B85: 00         NOP                     
7B86: 00         NOP                     
7B87: 00         NOP                     
7B88: 00         NOP                     
7B89: 00         NOP                     
7B8A: 00         NOP                     
7B8B: 00         NOP                     
7B8C: 00         NOP                     
7B8D: 00         NOP                     
7B8E: 00         NOP                     
7B8F: 00         NOP                     
7B90: 00         NOP                     
7B91: 00         NOP                     
7B92: 00         NOP                     
7B93: 00         NOP                     
7B94: 00         NOP                     
7B95: 00         NOP                     
7B96: 00         NOP                     
7B97: 00         NOP                     
7B98: 00         NOP                     
7B99: 00         NOP                     
7B9A: 00         NOP                     
7B9B: 00         NOP                     
7B9C: 07         RLCA                    
7B9D: 00         NOP                     
7B9E: 00         NOP                     
7B9F: 00         NOP                     
7BA0: 00         NOP                     
7BA1: 00         NOP                     
7BA2: 00         NOP                     
7BA3: 00         NOP                     
7BA4: 00         NOP                     
7BA5: 00         NOP                     
7BA6: 00         NOP                     
7BA7: 00         NOP                     
7BA8: 0F         RRCA                    
7BA9: 00         NOP                     
7BAA: 07         RLCA                    
7BAB: 00         NOP                     
7BAC: 03         INC     BC              
7BAD: 00         NOP                     
7BAE: 00         NOP                     
7BAF: 00         NOP                     
7BB0: 00         NOP                     
7BB1: 00         NOP                     
7BB2: 00         NOP                     
7BB3: 00         NOP                     
7BB4: 00         NOP                     
7BB5: 00         NOP                     
7BB6: 01 00 0F   LD      BC,$0F00        
7BB9: 00         NOP                     
7BBA: FF         RST     0X38            
7BBB: 00         NOP                     
7BBC: FE 00      CP      $00             
7BBE: 00         NOP                     
7BBF: 00         NOP                     
7BC0: 02         LD      (BC),A          
7BC1: 01 02 01   LD      BC,$0102        
7BC4: 04         INC     B               
7BC5: 00         NOP                     
7BC6: 04         INC     B               
7BC7: 00         NOP                     
7BC8: F4         ???                     
7BC9: 00         NOP                     
7BCA: FC         ???                     
7BCB: 00         NOP                     
7BCC: FC         ???                     
7BCD: 00         NOP                     
7BCE: FC         ???                     
7BCF: 00         NOP                     
7BD0: 7C         LD      A,H             
7BD1: 00         NOP                     
7BD2: 7E         LD      A,(HL)          
7BD3: 00         NOP                     
7BD4: FE 00      CP      $00             
7BD6: FF         RST     0X38            
7BD7: 00         NOP                     
7BD8: FF         RST     0X38            
7BD9: 00         NOP                     
7BDA: FF         RST     0X38            
7BDB: 00         NOP                     
7BDC: 07         RLCA                    
7BDD: 00         NOP                     
7BDE: 01 00 00   LD      BC,$0000        
7BE1: FF         RST     0X38            
7BE2: 00         NOP                     
7BE3: FF         RST     0X38            
7BE4: 00         NOP                     
7BE5: FF         RST     0X38            
7BE6: 00         NOP                     
7BE7: FF         RST     0X38            
7BE8: 00         NOP                     
7BE9: FF         RST     0X38            
7BEA: 00         NOP                     
7BEB: 7F         LD      A,A             
7BEC: 00         NOP                     
7BED: 7F         LD      A,A             
7BEE: 00         NOP                     
7BEF: 7F         LD      A,A             
7BF0: 00         NOP                     
7BF1: 3F         CCF                     
7BF2: 00         NOP                     
7BF3: 3F         CCF                     
7BF4: 00         NOP                     
7BF5: 1F         RRA                     
7BF6: 00         NOP                     
7BF7: 0F         RRCA                    
7BF8: 00         NOP                     
7BF9: 07         RLCA                    
7BFA: 80         ADD     A,B             
7BFB: 03         INC     BC              
7BFC: C0         RET     NZ              
7BFD: 00         NOP                     
7BFE: C0         RET     NZ              
7BFF: 00         NOP                     
7C00: 80         ADD     A,B             
7C01: 00         NOP                     
7C02: 80         ADD     A,B             
7C03: 00         NOP                     
7C04: 40         LD      B,B             
7C05: 80         ADD     A,B             
7C06: 40         LD      B,B             
7C07: 80         ADD     A,B             
7C08: 20 C0      JR      NZ,$7BCA        
7C0A: 20 C0      JR      NZ,$7BCC        
7C0C: 10 E0      STOP    $E0             
7C0E: 10 E0      STOP    $E0             
7C10: 08 F0 08   LD      ($08F0),SP      
7C13: F0 04      LD      A,($04)         
7C15: F8 04      LDHL    SP,$04          
7C17: F8 02      LDHL    SP,$02          
7C19: FC         ???                     
7C1A: 02         LD      (BC),A          
7C1B: FC         ???                     
7C1C: 03         INC     BC              
7C1D: 7C         LD      A,H             
7C1E: 01 7E C0   LD      BC,$C07E        
7C21: 3F         CCF                     
7C22: 40         LD      B,B             
7C23: 3C         INC     A               
7C24: 81         ADD     A,C             
7C25: 78         LD      A,B             
7C26: 83         ADD     A,E             
7C27: 70         LD      (HL),B          
7C28: 87         ADD     A,A             
7C29: 60         LD      H,B             
7C2A: 87         ADD     A,A             
7C2B: 61         LD      H,C             
7C2C: 86         ADD     A,(HL)          
7C2D: 43         LD      B,E             
7C2E: 4D         LD      C,L             
7C2F: 02         LD      (BC),A          
7C30: 4F         LD      C,A             
7C31: 05         DEC     B               
7C32: 2F         CPL                     
7C33: 04         INC     B               
7C34: 2F         CPL                     
7C35: 06 3F      LD      B,$3F           
7C37: 06 9F      LD      B,$9F           
7C39: 06 1F      LD      B,$1F           
7C3B: 06 1F      LD      B,$1F           
7C3D: 07         RLCA                    
7C3E: 1F         RRA                     
7C3F: 07         RLCA                    
7C40: 30 0C      JR      NC,$7C4E        
7C42: 53         LD      D,E             
7C43: 28 EF      JR      Z,$7C34         
7C45: 53         LD      D,E             
7C46: FF         RST     0X38            
7C47: 4E         LD      C,(HL)          
7C48: FF         RST     0X38            
7C49: 1E FF      LD      E,$FF           
7C4B: FD         ???                     
7C4C: 7F         LD      A,A             
7C4D: FF         RST     0X38            
7C4E: DF         RST     0X18            
7C4F: 3F         CCF                     
7C50: FF         RST     0X38            
7C51: 1F         RRA                     
7C52: FF         RST     0X38            
7C53: 1F         RRA                     
7C54: FF         RST     0X38            
7C55: 6F         LD      L,A             
7C56: FF         RST     0X38            
7C57: 0F         RRCA                    
7C58: FF         RST     0X38            
7C59: FF         RST     0X38            
7C5A: FF         RST     0X38            
7C5B: FF         RST     0X38            
7C5C: 87         ADD     A,A             
7C5D: 7F         LD      A,A             
7C5E: C3 BF FF   JP      $FFBF           
7C61: 00         NOP                     
7C62: E0 FF      LDFF00  ($FF),A         
7C64: FE 81      CP      $81             
7C66: FF         RST     0X38            
7C67: 00         NOP                     
7C68: FC         ???                     
7C69: 7F         LD      A,A             
7C6A: FE FF      CP      $FF             
7C6C: BA         CP      D               
7C6D: C7         RST     0X00            
7C6E: 7C         LD      A,H             
7C6F: A3         AND     E               
7C70: FE 05      CP      $05             
7C72: FE CF      CP      $CF             
7C74: FC         ???                     
7C75: C7         RST     0X00            
7C76: F8 FF      LDHL    SP,$FF          
7C78: FC         ???                     
7C79: FF         RST     0X38            
7C7A: FE FF      CP      $FF             
7C7C: FE FF      CP      $FF             
7C7E: FE FF      CP      $FF             
7C80: E7         RST     0X20            
7C81: DF         RST     0X18            
7C82: FF         RST     0X38            
7C83: FF         RST     0X38            
7C84: FF         RST     0X38            
7C85: FF         RST     0X38            
7C86: FF         RST     0X38            
7C87: E0 FF      LDFF00  ($FF),A         
7C89: EF         RST     0X28            
7C8A: FF         RST     0X38            
7C8B: E0 FF      LDFF00  ($FF),A         
7C8D: F0 FF      LD      A,($FF)         
7C8F: F0 FF      LD      A,($FF)         
7C91: FF         RST     0X38            
7C92: F9         LD      SP,HL           
7C93: 7F         LD      A,A             
7C94: 7F         LD      A,A             
7C95: 3F         CCF                     
7C96: 4E         LD      C,(HL)          
7C97: 3F         CCF                     
7C98: A0         AND     B               
7C99: 1F         RRA                     
7C9A: 90         SUB     B               
7C9B: 0F         RRCA                    
7C9C: 8F         ADC     A,A             
7C9D: 00         NOP                     
7C9E: 84         ADD     A,H             
7C9F: 03         INC     BC              
7CA0: FE FF      CP      $FF             
7CA2: FC         ???                     
7CA3: FF         RST     0X38            
7CA4: BC         CP      H               
7CA5: FF         RST     0X38            
7CA6: FC         ???                     
7CA7: 3F         CCF                     
7CA8: FC         ???                     
7CA9: 3F         CCF                     
7CAA: F8 3F      LDHL    SP,$3F          
7CAC: F8 7F      LDHL    SP,$7F          
7CAE: F0 FF      LD      A,($FF)         
7CB0: F0 FF      LD      A,($FF)         
7CB2: E4         ???                     
7CB3: FB         EI                      
7CB4: 88         ADC     A,B             
7CB5: F7         RST     0X30            
7CB6: 10 EF      STOP    $EF             
7CB8: 20 DF      JR      NZ,$7C99        
7CBA: C0         RET     NZ              
7CBB: 3F         CCF                     
7CBC: 00         NOP                     
7CBD: FF         RST     0X38            
7CBE: 00         NOP                     
7CBF: FF         RST     0X38            
7CC0: 00         NOP                     
7CC1: 00         NOP                     
7CC2: FF         RST     0X38            
7CC3: FF         RST     0X38            
7CC4: FF         RST     0X38            
7CC5: A4         AND     H               
7CC6: A4         AND     H               
7CC7: FF         RST     0X38            
7CC8: FF         RST     0X38            
7CC9: FF         RST     0X38            
7CCA: 93         SUB     E               
7CCB: FD         ???                     
7CCC: 91         SUB     C               
7CCD: FF         RST     0X38            
7CCE: FF         RST     0X38            
7CCF: FF         RST     0X38            
7CD0: 0F         RRCA                    
7CD1: 0F         RRCA                    
7CD2: 0F         RRCA                    
7CD3: 0F         RRCA                    
7CD4: 0F         RRCA                    
7CD5: 0F         RRCA                    
7CD6: 0A         LD      A,(BC)          
7CD7: 0F         RRCA                    
7CD8: 0A         LD      A,(BC)          
7CD9: 0F         RRCA                    
7CDA: FF         RST     0X38            
7CDB: FF         RST     0X38            
7CDC: BF         CP      A               
7CDD: E4         ???                     
7CDE: A4         AND     H               
7CDF: FF         RST     0X38            
7CE0: 00         NOP                     
7CE1: 00         NOP                     
7CE2: FF         RST     0X38            
7CE3: FF         RST     0X38            
7CE4: FF         RST     0X38            
7CE5: 40         LD      B,B             
7CE6: FF         RST     0X38            
7CE7: 40         LD      B,B             
7CE8: FF         RST     0X38            
7CE9: FF         RST     0X38            
7CEA: FF         RST     0X38            
7CEB: 08 FF 08   LD      ($08FF),SP      
7CEE: FF         RST     0X38            
7CEF: FF         RST     0X38            
7CF0: FF         RST     0X38            
7CF1: FF         RST     0X38            
7CF2: FF         RST     0X38            
7CF3: FF         RST     0X38            
7CF4: FF         RST     0X38            
7CF5: FF         RST     0X38            
7CF6: FF         RST     0X38            
7CF7: 44         LD      B,H             
7CF8: FF         RST     0X38            
7CF9: 44         LD      B,H             
7CFA: FF         RST     0X38            
7CFB: FF         RST     0X38            
7CFC: FF         RST     0X38            
7CFD: 40         LD      B,B             
7CFE: FF         RST     0X38            
7CFF: 40         LD      B,B             
7D00: 00         NOP                     
7D01: 00         NOP                     
7D02: 00         NOP                     
7D03: 00         NOP                     
7D04: 00         NOP                     
7D05: 00         NOP                     
7D06: 00         NOP                     
7D07: 00         NOP                     
7D08: 00         NOP                     
7D09: 00         NOP                     
7D0A: 00         NOP                     
7D0B: 00         NOP                     
7D0C: 00         NOP                     
7D0D: 00         NOP                     
7D0E: 00         NOP                     
7D0F: 00         NOP                     
7D10: 00         NOP                     
7D11: 00         NOP                     
7D12: 00         NOP                     
7D13: 00         NOP                     
7D14: 00         NOP                     
7D15: 00         NOP                     
7D16: 01 00 03   LD      BC,$0300        
7D19: 00         NOP                     
7D1A: 03         INC     BC              
7D1B: 00         NOP                     
7D1C: 03         INC     BC              
7D1D: 00         NOP                     
7D1E: 05         DEC     B               
7D1F: 02         LD      (BC),A          
7D20: C0         RET     NZ              
7D21: 3F         CCF                     
7D22: 40         LD      B,B             
7D23: 3C         INC     A               
7D24: 81         ADD     A,C             
7D25: 78         LD      A,B             
7D26: 83         ADD     A,E             
7D27: 70         LD      (HL),B          
7D28: 87         ADD     A,A             
7D29: 61         LD      H,C             
7D2A: 87         ADD     A,A             
7D2B: 61         LD      H,C             
7D2C: 87         ADD     A,A             
7D2D: 42         LD      B,D             
7D2E: 4F         LD      C,A             
7D2F: 00         NOP                     
7D30: 4F         LD      C,A             
7D31: 05         DEC     B               
7D32: 2F         CPL                     
7D33: 04         INC     B               
7D34: 2F         CPL                     
7D35: 06 3F      LD      B,$3F           
7D37: 06 9F      LD      B,$9F           
7D39: 06 1F      LD      B,$1F           
7D3B: 06 1F      LD      B,$1F           
7D3D: 07         RLCA                    
7D3E: 1F         RRA                     
7D3F: 07         RLCA                    
7D40: 30 0C      JR      NC,$7D4E        
7D42: 53         LD      D,E             
7D43: 28 EF      JR      Z,$7D34         
7D45: 53         LD      D,E             
7D46: FF         RST     0X38            
7D47: 0E FF      LD      C,$FF           
7D49: 9E         SBC     (HL)            
7D4A: FF         RST     0X38            
7D4B: DF         RST     0X18            
7D4C: FF         RST     0X38            
7D4D: 3F         CCF                     
7D4E: FF         RST     0X38            
7D4F: 1F         RRA                     
7D50: FF         RST     0X38            
7D51: 1F         RRA                     
7D52: FF         RST     0X38            
7D53: 3F         CCF                     
7D54: FF         RST     0X38            
7D55: 6F         LD      L,A             
7D56: FF         RST     0X38            
7D57: 0F         RRCA                    
7D58: FF         RST     0X38            
7D59: FF         RST     0X38            
7D5A: FF         RST     0X38            
7D5B: FF         RST     0X38            
7D5C: 87         ADD     A,A             
7D5D: 7F         LD      A,A             
7D5E: C3 BF FF   JP      $FFBF           
7D61: 00         NOP                     
7D62: FC         ???                     
7D63: C3 FF 00   JP      $00FF           
7D66: FF         RST     0X38            
7D67: 7C         LD      A,H             
7D68: FC         ???                     
7D69: FF         RST     0X38            
7D6A: BE         CP      (HL)            
7D6B: C7         RST     0X00            
7D6C: 7E         LD      A,(HL)          
7D6D: 83         ADD     A,E             
7D6E: F8 25      LDHL    SP,$25          
7D70: FC         ???                     
7D71: 05         DEC     B               
7D72: FE CF      CP      $CF             
7D74: FC         ???                     
7D75: C7         RST     0X00            
7D76: FC         ???                     
7D77: FF         RST     0X38            
7D78: FE FF      CP      $FF             
7D7A: FF         RST     0X38            
7D7B: FF         RST     0X38            
7D7C: FF         RST     0X38            
7D7D: FF         RST     0X38            
7D7E: FF         RST     0X38            
7D7F: FF         RST     0X38            
7D80: E7         RST     0X20            
7D81: DF         RST     0X18            
7D82: FF         RST     0X38            
7D83: FF         RST     0X38            
7D84: FF         RST     0X38            
7D85: E0 FF      LDFF00  ($FF),A         
7D87: EF         RST     0X28            
7D88: FF         RST     0X38            
7D89: EF         RST     0X28            
7D8A: EF         RST     0X28            
7D8B: E0 FF      LDFF00  ($FF),A         
7D8D: F0 F7      LD      A,($F7)         
7D8F: F0 FF      LD      A,($FF)         
7D91: FF         RST     0X38            
7D92: F8 7F      LDHL    SP,$7F          
7D94: 7F         LD      A,A             
7D95: 3F         CCF                     
7D96: 4E         LD      C,(HL)          
7D97: 3F         CCF                     
7D98: A0         AND     B               
7D99: 1F         RRA                     
7D9A: 90         SUB     B               
7D9B: 0F         RRCA                    
7D9C: 8F         ADC     A,A             
7D9D: 00         NOP                     
7D9E: 84         ADD     A,H             
7D9F: 03         INC     BC              
7DA0: FF         RST     0X38            
7DA1: FF         RST     0X38            
7DA2: DF         RST     0X18            
7DA3: FF         RST     0X38            
7DA4: FE 1F      CP      $1F             
7DA6: 2E DF      LD      L,$DF           
7DA8: 7E         LD      A,(HL)          
7DA9: 9F         SBC     A               
7DAA: FC         ???                     
7DAB: 1F         RRA                     
7DAC: FC         ???                     
7DAD: 3F         CCF                     
7DAE: F8 7F      LDHL    SP,$7F          
7DB0: F0 FF      LD      A,($FF)         
7DB2: E4         ???                     
7DB3: FB         EI                      
7DB4: 88         ADC     A,B             
7DB5: F7         RST     0X30            
7DB6: 10 EF      STOP    $EF             
7DB8: 20 DF      JR      NZ,$7D99        
7DBA: C0         RET     NZ              
7DBB: 3F         CCF                     
7DBC: 00         NOP                     
7DBD: FF         RST     0X38            
7DBE: 00         NOP                     
7DBF: FF         RST     0X38            
7DC0: 00         NOP                     
7DC1: 00         NOP                     
7DC2: FF         RST     0X38            
7DC3: FF         RST     0X38            
7DC4: FF         RST     0X38            
7DC5: 82         ADD     A,D             
7DC6: FF         RST     0X38            
7DC7: FE FF      CP      $FF             
7DC9: FF         RST     0X38            
7DCA: FF         RST     0X38            
7DCB: 82         ADD     A,D             
7DCC: FF         RST     0X38            
7DCD: FE FF      CP      $FF             
7DCF: FF         RST     0X38            
7DD0: 83         ADD     A,E             
7DD1: FF         RST     0X38            
7DD2: FF         RST     0X38            
7DD3: FF         RST     0X38            
7DD4: FF         RST     0X38            
7DD5: FF         RST     0X38            
7DD6: 83         ADD     A,E             
7DD7: FE FF      CP      $FF             
7DD9: FE FF      CP      $FF             
7DDB: FF         RST     0X38            
7DDC: FF         RST     0X38            
7DDD: 82         ADD     A,D             
7DDE: FF         RST     0X38            
7DDF: FE FF      CP      $FF             
7DE1: FF         RST     0X38            
7DE2: 97         SUB     A               
7DE3: F9         LD      SP,HL           
7DE4: 91         SUB     C               
7DE5: FF         RST     0X38            
7DE6: FF         RST     0X38            
7DE7: FF         RST     0X38            
7DE8: A5         AND     L               
7DE9: FE A4      CP      $A4             
7DEB: FF         RST     0X38            
7DEC: FF         RST     0X38            
7DED: FF         RST     0X38            
7DEE: 97         SUB     A               
7DEF: F9         LD      SP,HL           
7DF0: 91         SUB     C               
7DF1: FF         RST     0X38            
7DF2: FF         RST     0X38            
7DF3: FF         RST     0X38            
7DF4: A5         AND     L               
7DF5: FE A4      CP      $A4             
7DF7: FF         RST     0X38            
7DF8: FF         RST     0X38            
7DF9: FF         RST     0X38            
7DFA: 97         SUB     A               
7DFB: F9         LD      SP,HL           
7DFC: 91         SUB     C               
7DFD: FF         RST     0X38            
7DFE: FF         RST     0X38            
7DFF: FF         RST     0X38            
7E00: FF         RST     0X38            
7E01: FF         RST     0X38            
7E02: FF         RST     0X38            
7E03: 08 FF 08   LD      ($08FF),SP      
7E06: FF         RST     0X38            
7E07: FF         RST     0X38            
7E08: FF         RST     0X38            
7E09: 41         LD      B,C             
7E0A: FF         RST     0X38            
7E0B: 41         LD      B,C             
7E0C: FF         RST     0X38            
7E0D: FF         RST     0X38            
7E0E: FF         RST     0X38            
7E0F: 08 FF 08   LD      ($08FF),SP      
7E12: FF         RST     0X38            
7E13: FF         RST     0X38            
7E14: FF         RST     0X38            
7E15: 41         LD      B,C             
7E16: FF         RST     0X38            
7E17: 41         LD      B,C             
7E18: FF         RST     0X38            
7E19: FF         RST     0X38            
7E1A: FF         RST     0X38            
7E1B: 08 FF 08   LD      ($08FF),SP      
7E1E: FF         RST     0X38            
7E1F: FF         RST     0X38            
7E20: FF         RST     0X38            
7E21: FF         RST     0X38            
7E22: FF         RST     0X38            
7E23: 82         ADD     A,D             
7E24: FE FF      CP      $FF             
7E26: FF         RST     0X38            
7E27: FF         RST     0X38            
7E28: FF         RST     0X38            
7E29: 82         ADD     A,D             
7E2A: FF         RST     0X38            
7E2B: FE FF      CP      $FF             
7E2D: FF         RST     0X38            
7E2E: FF         RST     0X38            
7E2F: 82         ADD     A,D             
7E30: FE FF      CP      $FF             
7E32: FF         RST     0X38            
7E33: FF         RST     0X38            
7E34: FF         RST     0X38            
7E35: 82         ADD     A,D             
7E36: FF         RST     0X38            
7E37: FE FF      CP      $FF             
7E39: FF         RST     0X38            
7E3A: FF         RST     0X38            
7E3B: 82         ADD     A,D             
7E3C: FE FF      CP      $FF             
7E3E: FF         RST     0X38            
7E3F: FF         RST     0X38            
7E40: A5         AND     L               
7E41: FE A4      CP      $A4             
7E43: FF         RST     0X38            
7E44: FF         RST     0X38            
7E45: FF         RST     0X38            
7E46: 97         SUB     A               
7E47: F9         LD      SP,HL           
7E48: 91         SUB     C               
7E49: FF         RST     0X38            
7E4A: FF         RST     0X38            
7E4B: FF         RST     0X38            
7E4C: A5         AND     L               
7E4D: FE A4      CP      $A4             
7E4F: FF         RST     0X38            
7E50: FF         RST     0X38            
7E51: FF         RST     0X38            
7E52: 02         LD      (BC),A          
7E53: 03         INC     BC              
7E54: 04         INC     B               
7E55: 07         RLCA                    
7E56: 05         DEC     B               
7E57: 07         RLCA                    
7E58: 03         INC     BC              
7E59: 03         INC     BC              
7E5A: 05         DEC     B               
7E5B: 07         RLCA                    
7E5C: 04         INC     B               
7E5D: 07         RLCA                    
7E5E: 02         LD      (BC),A          
7E5F: 03         INC     BC              
7E60: FF         RST     0X38            
7E61: 40         LD      B,B             
7E62: FF         RST     0X38            
7E63: 40         LD      B,B             
7E64: FF         RST     0X38            
7E65: FF         RST     0X38            
7E66: FF         RST     0X38            
7E67: 08 FF 08   LD      ($08FF),SP      
7E6A: FF         RST     0X38            
7E6B: FF         RST     0X38            
7E6C: FF         RST     0X38            
7E6D: 40         LD      B,B             
7E6E: FF         RST     0X38            
7E6F: 40         LD      B,B             
7E70: FF         RST     0X38            
7E71: FF         RST     0X38            
7E72: 9F         SBC     A               
7E73: FF         RST     0X38            
7E74: 9F         SBC     A               
7E75: FF         RST     0X38            
7E76: 5F         LD      E,A             
7E77: FF         RST     0X38            
7E78: 7F         LD      A,A             
7E79: FF         RST     0X38            
7E7A: 5F         LD      E,A             
7E7B: FF         RST     0X38            
7E7C: 9F         SBC     A               
7E7D: FF         RST     0X38            
7E7E: 9F         SBC     A               
7E7F: FF         RST     0X38            
7E80: FF         RST     0X38            
7E81: 82         ADD     A,D             
7E82: FF         RST     0X38            
7E83: FE FF      CP      $FF             
7E85: FF         RST     0X38            
7E86: FF         RST     0X38            
7E87: 82         ADD     A,D             
7E88: FE FF      CP      $FF             
7E8A: FF         RST     0X38            
7E8B: FF         RST     0X38            
7E8C: FF         RST     0X38            
7E8D: 82         ADD     A,D             
7E8E: FF         RST     0X38            
7E8F: FE FF      CP      $FF             
7E91: FF         RST     0X38            
7E92: FF         RST     0X38            
7E93: FF         RST     0X38            
7E94: 83         ADD     A,E             
7E95: FF         RST     0X38            
7E96: FF         RST     0X38            
7E97: FF         RST     0X38            
7E98: FF         RST     0X38            
7E99: FF         RST     0X38            
7E9A: 83         ADD     A,E             
7E9B: FF         RST     0X38            
7E9C: FF         RST     0X38            
7E9D: FF         RST     0X38            
7E9E: FF         RST     0X38            
7E9F: FF         RST     0X38            
7EA0: FF         RST     0X38            
7EA1: FF         RST     0X38            
7EA2: 97         SUB     A               
7EA3: F9         LD      SP,HL           
7EA4: 91         SUB     C               
7EA5: FF         RST     0X38            
7EA6: FF         RST     0X38            
7EA7: FF         RST     0X38            
7EA8: A5         AND     L               
7EA9: FE A4      CP      $A4             
7EAB: FF         RST     0X38            
7EAC: FF         RST     0X38            
7EAD: FF         RST     0X38            
7EAE: 97         SUB     A               
7EAF: F9         LD      SP,HL           
7EB0: 00         NOP                     
7EB1: 00         NOP                     
7EB2: 00         NOP                     
7EB3: 00         NOP                     
7EB4: 00         NOP                     
7EB5: 00         NOP                     
7EB6: 00         NOP                     
7EB7: 00         NOP                     
7EB8: 00         NOP                     
7EB9: 00         NOP                     
7EBA: 00         NOP                     
7EBB: 00         NOP                     
7EBC: 00         NOP                     
7EBD: 00         NOP                     
7EBE: 00         NOP                     
7EBF: 00         NOP                     
7EC0: FF         RST     0X38            
7EC1: FF         RST     0X38            
7EC2: FF         RST     0X38            
7EC3: 08 FF 08   LD      ($08FF),SP      
7EC6: FF         RST     0X38            
7EC7: FF         RST     0X38            
7EC8: FF         RST     0X38            
7EC9: 41         LD      B,C             
7ECA: FF         RST     0X38            
7ECB: 41         LD      B,C             
7ECC: FF         RST     0X38            
7ECD: FF         RST     0X38            
7ECE: FF         RST     0X38            
7ECF: 08 00 00   LD      ($0000),SP      
7ED2: 00         NOP                     
7ED3: 00         NOP                     
7ED4: 00         NOP                     
7ED5: 00         NOP                     
7ED6: 00         NOP                     
7ED7: 00         NOP                     
7ED8: 00         NOP                     
7ED9: 00         NOP                     
7EDA: 00         NOP                     
7EDB: 00         NOP                     
7EDC: 00         NOP                     
7EDD: 00         NOP                     
7EDE: 00         NOP                     
7EDF: 00         NOP                     
7EE0: 00         NOP                     
7EE1: 00         NOP                     
7EE2: 87         ADD     A,A             
7EE3: 00         NOP                     
7EE4: DF         RST     0X18            
7EE5: 87         ADD     A,A             
7EE6: FF         RST     0X38            
7EE7: DF         RST     0X18            
7EE8: FF         RST     0X38            
7EE9: FF         RST     0X38            
7EEA: FF         RST     0X38            
7EEB: FF         RST     0X38            
7EEC: FF         RST     0X38            
7EED: FF         RST     0X38            
7EEE: FF         RST     0X38            
7EEF: FF         RST     0X38            
7EF0: FF         RST     0X38            
7EF1: 00         NOP                     
7EF2: FF         RST     0X38            
7EF3: BF         CP      A               
7EF4: 68         LD      L,B             
7EF5: BF         CP      A               
7EF6: 40         LD      B,B             
7EF7: BF         CP      A               
7EF8: FF         RST     0X38            
7EF9: 00         NOP                     
7EFA: FF         RST     0X38            
7EFB: F7         RST     0X30            
7EFC: 8C         ADC     A,H             
7EFD: F7         RST     0X30            
7EFE: 08 F7 03   LD      ($03F7),SP      
7F01: 00         NOP                     
7F02: 07         RLCA                    
7F03: 03         INC     BC              
7F04: 1F         RRA                     
7F05: 07         RLCA                    
7F06: 3F         CCF                     
7F07: 17         RLA                     
7F08: 7F         LD      A,A             
7F09: 3B         DEC     SP              
7F0A: 7F         LD      A,A             
7F0B: 3F         CCF                     
7F0C: 3F         CCF                     
7F0D: 1F         RRA                     
7F0E: 3F         CCF                     
7F0F: 1F         RRA                     
7F10: 00         NOP                     
7F11: 00         NOP                     
7F12: 00         NOP                     
7F13: 00         NOP                     
7F14: 00         NOP                     
7F15: 00         NOP                     
7F16: 00         NOP                     
7F17: 00         NOP                     
7F18: 00         NOP                     
7F19: 00         NOP                     
7F1A: 00         NOP                     
7F1B: 00         NOP                     
7F1C: 00         NOP                     
7F1D: 00         NOP                     
7F1E: 00         NOP                     
7F1F: 00         NOP                     
7F20: C0         RET     NZ              
7F21: 00         NOP                     
7F22: E0 C0      LDFF00  ($C0),A         
7F24: F7         RST     0X30            
7F25: E0 FF      LDFF00  ($FF),A         
7F27: F7         RST     0X30            
7F28: FF         RST     0X38            
7F29: F7         RST     0X30            
7F2A: FF         RST     0X38            
7F2B: FF         RST     0X38            
7F2C: FF         RST     0X38            
7F2D: FF         RST     0X38            
7F2E: FF         RST     0X38            
7F2F: FF         RST     0X38            
7F30: FF         RST     0X38            
7F31: 00         NOP                     
7F32: FF         RST     0X38            
7F33: BF         CP      A               
7F34: 68         LD      L,B             
7F35: BF         CP      A               
7F36: 40         LD      B,B             
7F37: BF         CP      A               
7F38: FF         RST     0X38            
7F39: 00         NOP                     
7F3A: FF         RST     0X38            
7F3B: F7         RST     0X30            
7F3C: 8C         ADC     A,H             
7F3D: F7         RST     0X30            
7F3E: 08 F7 3C   LD      ($3CF7),SP      
7F41: 00         NOP                     
7F42: 7E         LD      A,(HL)          
7F43: 3C         INC     A               
7F44: FF         RST     0X38            
7F45: 7E         LD      A,(HL)          
7F46: FF         RST     0X38            
7F47: 7F         LD      A,A             
7F48: FF         RST     0X38            
7F49: FF         RST     0X38            
7F4A: FF         RST     0X38            
7F4B: FF         RST     0X38            
7F4C: FF         RST     0X38            
7F4D: FF         RST     0X38            
7F4E: FF         RST     0X38            
7F4F: FF         RST     0X38            
7F50: FF         RST     0X38            
7F51: 00         NOP                     
7F52: FF         RST     0X38            
7F53: BF         CP      A               
7F54: 68         LD      L,B             
7F55: BF         CP      A               
7F56: 40         LD      B,B             
7F57: BF         CP      A               
7F58: FF         RST     0X38            
7F59: 00         NOP                     
7F5A: FF         RST     0X38            
7F5B: F7         RST     0X30            
7F5C: 8C         ADC     A,H             
7F5D: F7         RST     0X30            
7F5E: 08 F7 00   LD      ($00F7),SP      
7F61: 00         NOP                     
7F62: 3C         INC     A               
7F63: 00         NOP                     
7F64: 7E         LD      A,(HL)          
7F65: 3C         INC     A               
7F66: FF         RST     0X38            
7F67: 7E         LD      A,(HL)          
7F68: FF         RST     0X38            
7F69: 7F         LD      A,A             
7F6A: FF         RST     0X38            
7F6B: 7F         LD      A,A             
7F6C: 7F         LD      A,A             
7F6D: 3F         CCF                     
7F6E: 7F         LD      A,A             
7F6F: 3F         CCF                     
7F70: 00         NOP                     
7F71: 00         NOP                     
7F72: 00         NOP                     
7F73: 00         NOP                     
7F74: 00         NOP                     
7F75: 00         NOP                     
7F76: 00         NOP                     
7F77: 00         NOP                     
7F78: 00         NOP                     
7F79: 00         NOP                     
7F7A: 00         NOP                     
7F7B: 00         NOP                     
7F7C: 00         NOP                     
7F7D: 00         NOP                     
7F7E: 00         NOP                     
7F7F: 00         NOP                     
7F80: 00         NOP                     
7F81: 00         NOP                     
7F82: 01 00 63   LD      BC,$6300        
7F85: 01 F7 63   LD      BC,$63F7        
7F88: FF         RST     0X38            
7F89: 73         LD      (HL),E          
7F8A: FF         RST     0X38            
7F8B: FF         RST     0X38            
7F8C: FF         RST     0X38            
7F8D: FF         RST     0X38            
7F8E: FF         RST     0X38            
7F8F: FF         RST     0X38            
7F90: FF         RST     0X38            
7F91: 00         NOP                     
7F92: FF         RST     0X38            
7F93: BF         CP      A               
7F94: 68         LD      L,B             
7F95: BF         CP      A               
7F96: 40         LD      B,B             
7F97: BF         CP      A               
7F98: FF         RST     0X38            
7F99: 00         NOP                     
7F9A: FF         RST     0X38            
7F9B: F7         RST     0X30            
7F9C: 8C         ADC     A,H             
7F9D: F7         RST     0X30            
7F9E: 08 F7 00   LD      ($00F7),SP      
7FA1: 00         NOP                     
7FA2: E0 00      LDFF00  ($00),A         
7FA4: F3         DI                      
7FA5: E0 FF      LDFF00  ($FF),A         
7FA7: F3         DI                      
7FA8: FF         RST     0X38            
7FA9: FB         EI                      
7FAA: FF         RST     0X38            
7FAB: FF         RST     0X38            
7FAC: FF         RST     0X38            
7FAD: FF         RST     0X38            
7FAE: FF         RST     0X38            
7FAF: FF         RST     0X38            
7FB0: FF         RST     0X38            
7FB1: 00         NOP                     
7FB2: FF         RST     0X38            
7FB3: BF         CP      A               
7FB4: 68         LD      L,B             
7FB5: BF         CP      A               
7FB6: 40         LD      B,B             
7FB7: BF         CP      A               
7FB8: FF         RST     0X38            
7FB9: 00         NOP                     
7FBA: FF         RST     0X38            
7FBB: F7         RST     0X30            
7FBC: 8C         ADC     A,H             
7FBD: F7         RST     0X30            
7FBE: 08 F7 00   LD      ($00F7),SP      
7FC1: 00         NOP                     
7FC2: 00         NOP                     
7FC3: 00         NOP                     
7FC4: 03         INC     BC              
7FC5: 00         NOP                     
7FC6: 07         RLCA                    
7FC7: 03         INC     BC              
7FC8: 77         LD      (HL),A          
7FC9: 03         INC     BC              
7FCA: FF         RST     0X38            
7FCB: 77         LD      (HL),A          
7FCC: FF         RST     0X38            
7FCD: 7F         LD      A,A             
7FCE: FF         RST     0X38            
7FCF: 7F         LD      A,A             
7FD0: 00         NOP                     
7FD1: 00         NOP                     
7FD2: 00         NOP                     
7FD3: 00         NOP                     
7FD4: 00         NOP                     
7FD5: 00         NOP                     
7FD6: 00         NOP                     
7FD7: 00         NOP                     
7FD8: 00         NOP                     
7FD9: 00         NOP                     
7FDA: 00         NOP                     
7FDB: 00         NOP                     
7FDC: 00         NOP                     
7FDD: 00         NOP                     
7FDE: 00         NOP                     
7FDF: 00         NOP                     
7FE0: 1F         RRA                     
7FE1: 00         NOP                     
7FE2: 3F         CCF                     
7FE3: 1F         RRA                     
7FE4: 7F         LD      A,A             
7FE5: 3F         CCF                     
7FE6: FF         RST     0X38            
7FE7: 3F         CCF                     
7FE8: FF         RST     0X38            
7FE9: BF         CP      A               
7FEA: FF         RST     0X38            
7FEB: FF         RST     0X38            
7FEC: FF         RST     0X38            
7FED: FF         RST     0X38            
7FEE: FF         RST     0X38            
7FEF: FF         RST     0X38            
7FF0: FF         RST     0X38            
7FF1: 00         NOP                     
7FF2: FF         RST     0X38            
7FF3: BF         CP      A               
7FF4: 68         LD      L,B             
7FF5: BF         CP      A               
7FF6: 40         LD      B,B             
7FF7: BF         CP      A               
7FF8: FF         RST     0X38            
7FF9: 00         NOP                     
7FFA: FF         RST     0X38            
7FFB: F7         RST     0X30            
7FFC: 8C         ADC     A,H             
7FFD: F7         RST     0X30            
7FFE: 08 F7 00   LD      ($00F7),SP      
```