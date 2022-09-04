![Bank 0B](GBZelda.jpg)

# Bank 0B

>>> cpu Z80GB

>>> binary 4000:roms/zelda.gb[2C000:30000]

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](../Hardware.md)

```code
4000: 00              NOP                         
4001: 42              LD      B,D                 
4002: 00              NOP                         
4003: 42              LD      B,D                 
4004: 2A              LD      A,(HLI)             
4005: 42              LD      B,D                 
4006: 58              LD      E,B                 
4007: 42              LD      B,D                 
4008: 74              LD      (HL),H              
4009: 42              LD      B,D                 
400A: 97              SUB     A                   
400B: 42              LD      B,D                 
400C: D6 42           SUB     $42                 
400E: 2C              INC     L                   
400F: 43              LD      B,E                 
4010: 66              LD      H,(HL)              
4011: 43              LD      B,E                 
4012: 9E              SBC     (HL)                
4013: 43              LD      B,E                 
4014: DB                              
4015: 43              LD      B,E                 
4016: 25              DEC     H                   
4017: 44              LD      B,H                 
4018: A3              AND     E                   
4019: 44              LD      B,H                 
401A: DB                              
401B: 44              LD      B,H                 
401C: 0C              INC     C                   
401D: 45              LD      B,L                 
401E: 3F              CCF                         
401F: 45              LD      B,L                 
4020: 78              LD      A,B                 
4021: 45              LD      B,L                 
4022: A1              AND     C                   
4023: 45              LD      B,L                 
4024: D4 45 04        CALL    NC,$0445            
4027: 46              LD      B,(HL)              
4028: 29              ADD     HL,HL               
4029: 46              LD      B,(HL)              
402A: 69              LD      L,C                 
402B: 46              LD      B,(HL)              
402C: B5              OR      L                   
402D: 46              LD      B,(HL)              
402E: F5              PUSH    AF                  
402F: 46              LD      B,(HL)              
4030: 1C              INC     E                   
4031: 47              LD      B,A                 
4032: 4B              LD      C,E                 
4033: 47              LD      B,A                 
4034: 8B              ADC     A,E                 
4035: 47              LD      B,A                 
4036: EA 47 18        LD      ($1847),A           
4039: 48              LD      C,B                 
403A: 5A              LD      E,D                 
403B: 48              LD      C,B                 
403C: 9E              SBC     (HL)                
403D: 48              LD      C,B                 
403E: D5              PUSH    DE                  
403F: 48              LD      C,B                 
4040: 03              INC     BC                  
4041: 49              LD      C,C                 
4042: 2C              INC     L                   
4043: 49              LD      C,C                 
4044: 51              LD      D,C                 
4045: 49              LD      C,C                 
4046: AC              XOR     H                   
4047: 49              LD      C,C                 
4048: B6              OR      (HL)                
4049: 49              LD      C,C                 
404A: D6 49           SUB     $49                 
404C: 01 4A 50        LD      BC,$504A            
404F: 4A              LD      C,D                 
4050: 85              ADD     A,L                 
4051: 4A              LD      C,D                 
4052: A5              AND     L                   
4053: 4A              LD      C,D                 
4054: CA 4A E9        JP      Z,$E94A             
4057: 4A              LD      C,D                 
4058: 3D              DEC     A                   
4059: 4B              LD      C,E                 
405A: 94              SUB     H                   
405B: 4B              LD      C,E                 
405C: CC 4B FB        CALL    Z,$FB4B             
405F: 4B              LD      C,E                 
4060: FE 4B           CP      $4B                 
4062: 3F              CCF                         
4063: 4C              LD      C,H                 
4064: 5E              LD      E,(HL)              
4065: 4C              LD      C,H                 
4066: 8A              ADC     A,D                 
4067: 4C              LD      C,H                 
4068: 8A              ADC     A,D                 
4069: 4C              LD      C,H                 
406A: A4              AND     H                   
406B: 4C              LD      C,H                 
406C: E2              LD      (C),A               
406D: 4C              LD      C,H                 
406E: E2              LD      (C),A               
406F: 4C              LD      C,H                 
4070: 40              LD      B,B                 
4071: 4D              LD      C,L                 
4072: 57              LD      D,A                 
4073: 4D              LD      C,L                 
4074: B7              OR      A                   
4075: 4D              LD      C,L                 
4076: 09              ADD     HL,BC               
4077: 4E              LD      C,(HL)              
4078: 4B              LD      C,E                 
4079: 4E              LD      C,(HL)              
407A: A2              AND     D                   
407B: 4E              LD      C,(HL)              
407C: DD                              
407D: 4E              LD      C,(HL)              
407E: 0F              RRCA                        
407F: 4F              LD      C,A                 
4080: 24              INC     H                   
4081: 4F              LD      C,A                 
4082: 64              LD      H,H                 
4083: 4F              LD      C,A                 
4084: AF              XOR     A                   
4085: 4F              LD      C,A                 
4086: DF              RST     0X18                
4087: 4F              LD      C,A                 
4088: 31 50 52        LD      SP,$5250            
408B: 50              LD      D,B                 
408C: 82              ADD     A,D                 
408D: 50              LD      D,B                 
408E: B8              CP      B                   
408F: 50              LD      D,B                 
4090: DD                              
4091: 50              LD      D,B                 
4092: 0E 51           LD      C,$51               
4094: 5D              LD      E,L                 
4095: 51              LD      D,C                 
4096: 89              ADC     A,C                 
4097: 51              LD      D,C                 
4098: A3              AND     E                   
4099: 51              LD      D,C                 
409A: D3                              
409B: 51              LD      D,C                 
409C: 11 52 2C        LD      DE,$2C52            
409F: 52              LD      D,D                 
40A0: 58              LD      E,B                 
40A1: 52              LD      D,D                 
40A2: B5              OR      L                   
40A3: 52              LD      D,D                 
40A4: 01 53 2E        LD      BC,$2E53            
40A7: 53              LD      D,E                 
40A8: 66              LD      H,(HL)              
40A9: 53              LD      D,E                 
40AA: 77              LD      (HL),A              
40AB: 53              LD      D,E                 
40AC: 9F              SBC     A                   
40AD: 53              LD      D,E                 
40AE: BB              CP      E                   
40AF: 53              LD      D,E                 
40B0: E9              JP      (HL)                
40B1: 53              LD      D,E                 
40B2: 24              INC     H                   
40B3: 54              LD      D,H                 
40B4: 71              LD      (HL),C              
40B5: 54              LD      D,H                 
40B6: AD              XOR     L                   
40B7: 54              LD      D,H                 
40B8: B6              OR      (HL)                
40B9: 54              LD      D,H                 
40BA: EF              RST     0X28                
40BB: 54              LD      D,H                 
40BC: 3C              INC     A                   
40BD: 55              LD      D,L                 
40BE: 5C              LD      E,H                 
40BF: 55              LD      D,L                 
40C0: B5              OR      L                   
40C1: 55              LD      D,L                 
40C2: EF              RST     0X28                
40C3: 55              LD      D,L                 
40C4: 29              ADD     HL,HL               
40C5: 56              LD      D,(HL)              
40C6: 7A              LD      A,D                 
40C7: 56              LD      D,(HL)              
40C8: D4 56 08        CALL    NC,$0856            
40CB: 57              LD      D,A                 
40CC: 40              LD      B,B                 
40CD: 57              LD      D,A                 
40CE: 85              ADD     A,L                 
40CF: 57              LD      D,A                 
40D0: D0              RET     NC                  
40D1: 57              LD      D,A                 
40D2: 0E 58           LD      C,$58               
40D4: 5A              LD      E,D                 
40D5: 58              LD      E,B                 
40D6: A8              XOR     B                   
40D7: 58              LD      E,B                 
40D8: F0 58           LD      A,($58)             
40DA: F0 58           LD      A,($58)             
40DC: F0 58           LD      A,($58)             
40DE: F0 58           LD      A,($58)             
40E0: 3D              DEC     A                   
40E1: 59              LD      E,C                 
40E2: 72              LD      (HL),D              
40E3: 59              LD      E,C                 
40E4: 91              SUB     C                   
40E5: 59              LD      E,C                 
40E6: C6 59           ADD     $59                 
40E8: 1F              RRA                         
40E9: 5A              LD      E,D                 
40EA: 4A              LD      C,D                 
40EB: 5A              LD      E,D                 
40EC: 3D              DEC     A                   
40ED: 59              LD      E,C                 
40EE: 9C              SBC     H                   
40EF: 5A              LD      E,D                 
40F0: 9C              SBC     H                   
40F1: 5A              LD      E,D                 
40F2: 9C              SBC     H                   
40F3: 5A              LD      E,D                 
40F4: 9C              SBC     H                   
40F5: 5A              LD      E,D                 
40F6: FF              RST     0X38                
40F7: 5A              LD      E,D                 
40F8: 59              LD      E,C                 
40F9: 5B              LD      E,E                 
40FA: CC 5B 20        CALL    Z,$205B             
40FD: 5C              LD      E,H                 
40FE: 76              HALT                        
40FF: 5C              LD      E,H                 
4100: B2              OR      D                   
4101: 5C              LD      E,H                 
4102: 17              RLA                         
4103: 5D              LD      E,L                 
4104: 46              LD      B,(HL)              
4105: 5D              LD      E,L                 
4106: B4              OR      H                   
4107: 5D              LD      E,L                 
4108: 19              ADD     HL,DE               
4109: 5E              LD      E,(HL)              
410A: 4D              LD      C,L                 
410B: 5E              LD      E,(HL)              
410C: AC              XOR     H                   
410D: 5E              LD      E,(HL)              
410E: F6 5E           OR      $5E                 
4110: 46              LD      B,(HL)              
4111: 5F              LD      E,A                 
4112: B6              OR      (HL)                
4113: 5F              LD      E,A                 
4114: 19              ADD     HL,DE               
4115: 60              LD      H,B                 
4116: 7C              LD      A,H                 
4117: 60              LD      H,B                 
4118: B7              OR      A                   
4119: 60              LD      H,B                 
411A: 08 61 69        LD      ($6961),SP          ; {}
411D: 61              LD      H,C                 
411E: A8              XOR     B                   
411F: 61              LD      H,C                 
4120: DB                              
4121: 61              LD      H,C                 
4122: 47              LD      B,A                 
4123: 62              LD      H,D                 
4124: 7A              LD      A,D                 
4125: 62              LD      H,D                 
4126: BF              CP      A                   
4127: 62              LD      H,D                 
4128: FB              EI                          
4129: 62              LD      H,D                 
412A: 3C              INC     A                   
412B: 63              LD      H,E                 
412C: 80              ADD     A,B                 
412D: 63              LD      H,E                 
412E: C9              RET                         
412F: 63              LD      H,E                 
4130: 12              LD      (DE),A              
4131: 64              LD      H,H                 
4132: 39              ADD     HL,SP               
4133: 64              LD      H,H                 
4134: 66              LD      H,(HL)              
4135: 64              LD      H,H                 
4136: 9A              SBC     D                   
4137: 64              LD      H,H                 
4138: C7              RST     0X00                
4139: 64              LD      H,H                 
413A: F4                              
413B: 64              LD      H,H                 
413C: 21 65 21        LD      HL,$2165            
413F: 65              LD      H,L                 
4140: 44              LD      B,H                 
4141: 65              LD      H,L                 
4142: 80              ADD     A,B                 
4143: 65              LD      H,L                 
4144: 99              SBC     C                   
4145: 65              LD      H,L                 
4146: CB 65           BIT     1,E                 
4148: FB              EI                          
4149: 65              LD      H,L                 
414A: 4E              LD      C,(HL)              
414B: 66              LD      H,(HL)              
414C: 7E              LD      A,(HL)              
414D: 66              LD      H,(HL)              
414E: AB              XOR     E                   
414F: 66              LD      H,(HL)              
4150: D1              POP     DE                  
4151: 66              LD      H,(HL)              
4152: F0 66           LD      A,($66)             
4154: 1E 67           LD      E,$67               
4156: 5A              LD      E,D                 
4157: 67              LD      H,A                 
4158: AE              XOR     (HL)                
4159: 67              LD      H,A                 
415A: FC                              
415B: 67              LD      H,A                 
415C: 22              LD      (HLI),A             
415D: 68              LD      L,B                 
415E: 7E              LD      A,(HL)              
415F: 68              LD      L,B                 
4160: D7              RST     0X10                
4161: 68              LD      L,B                 
4162: 0C              INC     C                   
4163: 69              LD      L,C                 
4164: 55              LD      D,L                 
4165: 69              LD      L,C                 
4166: 8F              ADC     A,A                 
4167: 69              LD      L,C                 
4168: CE 69           ADC     $69                 
416A: FB              EI                          
416B: 69              LD      L,C                 
416C: FE 69           CP      $69                 
416E: 49              LD      C,C                 
416F: 6A              LD      L,D                 
4170: 9E              SBC     (HL)                
4171: 6A              LD      L,D                 
4172: D2 6A 04        JP      NC,$046A            
4175: 6B              LD      L,E                 
4176: 58              LD      E,B                 
4177: 6B              LD      L,E                 
4178: B3              OR      E                   
4179: 6B              LD      L,E                 
417A: FC                              
417B: 6B              LD      L,E                 
417C: 49              LD      C,C                 
417D: 6C              LD      L,H                 
417E: 81              ADD     A,C                 
417F: 6C              LD      L,H                 
4180: B9              CP      C                   
4181: 6C              LD      L,H                 
4182: 09              ADD     HL,BC               
4183: 6D              LD      L,L                 
4184: 61              LD      H,C                 
4185: 6D              LD      L,L                 
4186: AA              XOR     D                   
4187: 6D              LD      L,L                 
4188: EA 6D 45        LD      ($456D),A           ; {}
418B: 6E              LD      L,(HL)              
418C: 79              LD      A,C                 
418D: 6E              LD      L,(HL)              
418E: A7              AND     A                   
418F: 6E              LD      L,(HL)              
4190: E1              POP     HL                  
4191: 6E              LD      L,(HL)              
4192: 41              LD      B,C                 
4193: 6F              LD      L,A                 
4194: A0              AND     B                   
4195: 6F              LD      L,A                 
4196: F0 6F           LD      A,($6F)             
4198: 1D              DEC     E                   
4199: 70              LD      (HL),B              
419A: 4A              LD      C,D                 
419B: 70              LD      (HL),B              
419C: 8B              ADC     A,E                 
419D: 70              LD      (HL),B              
419E: DA 70 14        JP      C,$1470             
41A1: 71              LD      (HL),C              
41A2: 5E              LD      E,(HL)              
41A3: 71              LD      (HL),C              
41A4: B2              OR      D                   
41A5: 71              LD      (HL),C              
41A6: CC 71 F8        CALL    Z,$F871             
41A9: 71              LD      (HL),C              
41AA: 47              LD      B,A                 
41AB: 72              LD      (HL),D              
41AC: 76              HALT                        
41AD: 72              LD      (HL),D              
41AE: BF              CP      A                   
41AF: 72              LD      (HL),D              
41B0: F0 72           LD      A,($72)             
41B2: 3F              CCF                         
41B3: 73              LD      (HL),E              
41B4: 72              LD      (HL),D              
41B5: 73              LD      (HL),E              
41B6: A7              AND     A                   
41B7: 73              LD      (HL),E              
41B8: D9              RETI                        
41B9: 73              LD      (HL),E              
41BA: FF              RST     0X38                
41BB: 73              LD      (HL),E              
41BC: 32              LD      (HLD),A             
41BD: 74              LD      (HL),H              
41BE: 74              LD      (HL),H              
41BF: 74              LD      (HL),H              
41C0: D4 74 F4        CALL    NC,$F474            
41C3: 74              LD      (HL),H              
41C4: 23              INC     HL                  
41C5: 75              LD      (HL),L              
41C6: 6D              LD      L,L                 
41C7: 75              LD      (HL),L              
41C8: 9A              SBC     D                   
41C9: 75              LD      (HL),L              
41CA: DF              RST     0X18                
41CB: 75              LD      (HL),L              
41CC: 37              SCF                         
41CD: 76              HALT                        
41CE: 77              LD      (HL),A              
41CF: 76              HALT                        
41D0: C5              PUSH    BC                  
41D1: 76              HALT                        
41D2: 01 77 39        LD      BC,$3977            
41D5: 77              LD      (HL),A              
41D6: 96              SUB     (HL)                
41D7: 77              LD      (HL),A              
41D8: F0 77           LD      A,($77)             
41DA: 54              LD      D,H                 
41DB: 78              LD      A,B                 
41DC: B6              OR      (HL)                
41DD: 78              LD      A,B                 
41DE: 17              RLA                         
41DF: 79              LD      A,C                 
41E0: 65              LD      H,L                 
41E1: 79              LD      A,C                 
41E2: AE              XOR     (HL)                
41E3: 79              LD      A,C                 
41E4: FB              EI                          
41E5: 79              LD      A,C                 
41E6: 4F              LD      C,A                 
41E7: 7A              LD      A,D                 
41E8: AA              XOR     D                   
41E9: 7A              LD      A,D                 
41EA: DB                              
41EB: 7A              LD      A,D                 
41EC: 26 7B           LD      H,$7B               
41EE: 6A              LD      L,D                 
41EF: 7B              LD      A,E                 
41F0: C2 7B FC        JP      NZ,$FC7B            
41F3: 7B              LD      A,E                 
41F4: 61              LD      H,C                 
41F5: 7C              LD      A,H                 
41F6: BF              CP      A                   
41F7: 7C              LD      A,H                 
41F8: F2                              
41F9: 7C              LD      A,H                 
41FA: 5E              LD      E,(HL)              
41FB: 7D              LD      A,L                 
41FC: A0              AND     B                   
41FD: 7D              LD      A,L                 
41FE: D7              RST     0X10                
41FF: 7D              LD      A,L                 
4200: 04              INC     B                   
4201: 8D              ADC     A,L                 
4202: 19              ADD     HL,DE               
4203: F7              RST     0X30                
4204: 75              LD      (HL),L              
4205: F5              PUSH    AF                  
4206: 89              ADC     A,C                 
4207: 11 0F C6        LD      DE,$C60F            
420A: 21 0F 22        LD      HL,$220F            
420D: 25              DEC     H                   
420E: 87              ADD     A,A                 
420F: 23              INC     HL                  
4210: 21 C5 32        LD      HL,$32C5            
4213: 23              INC     HL                  
4214: 86              ADD     A,(HL)              
4215: 44              LD      B,H                 
4216: DB                              
4217: C3 54 DB        JP      $DB54               
421A: 24              INC     H                   
421B: C7              RST     0X00                
421C: 27              DAA                         
421D: C7              RST     0X00                
421E: 42              LD      B,D                 
421F: C9              RET                         
4220: 75              LD      (HL),L              
4221: 0D              DEC     C                   
4222: 76              HALT                        
4223: 2C              INC     L                   
4224: 83              ADD     A,E                 
4225: 77              LD      (HL),A              
4226: 22              LD      (HLI),A             
4227: 11 A0 FE        LD      DE,$FEA0            
422A: 04              INC     B                   
422B: 4D              LD      C,L                 
422C: 10 F6           ;;STOP    $F6                 
422E: 19              ADD     HL,DE               
422F: F7              RST     0X30                
4230: 72              LD      (HL),D              
4231: F5              PUSH    AF                  
4232: 09              ADD     HL,BC               
4233: 21 8A 10        LD      HL,$108A            
4236: 0F              RRCA                        
4237: 89              ADC     A,C                 
4238: 20 21           JR      NZ,$425B            ; {}
423A: 29              ADD     HL,HL               
423B: 26 C5           LD      H,$C5               
423D: 32              LD      (HLD),A             
423E: DC 82 40        CALL    C,$4082             ; {}
4241: DB                              
4242: 71              LD      (HL),C              
4243: 2B              DEC     HL                  
4244: 73              LD      (HL),E              
4245: 2C              INC     L                   
4246: 76              HALT                        
4247: 2B              DEC     HL                  
4248: 77              LD      (HL),A              
4249: DC 78 2C        CALL    C,$2C78             
424C: 23              INC     HL                  
424D: C7              RST     0X00                
424E: 27              DAA                         
424F: C7              RST     0X00                
4250: 25              DEC     H                   
4251: A3              AND     E                   
4252: E1              POP     HL                  
4253: 06 11           LD      B,$11               
4255: 58              LD      E,B                 
4256: 30 FE           JR      NC,$4256            ; {}
4258: 04              INC     B                   
4259: 2D              DEC     L                   
425A: 10 F6           ;;STOP    $F6                 
425C: 19              ADD     HL,DE               
425D: F7              RST     0X30                
425E: 00              NOP                         
425F: 21 8A 10        LD      HL,$108A            
4262: 0F              RRCA                        
4263: 20 25           JR      NZ,$428A            ; {}
4265: 89              ADC     A,C                 
4266: 21 21 22        LD      HL,$2221            
4269: C7              RST     0X00                
426A: 26 C7           LD      H,$C7               
426C: 24              INC     H                   
426D: A3              AND     E                   
426E: E1              POP     HL                  
426F: 06 12           LD      B,$12               
4271: 48              LD      C,B                 
4272: 30 FE           JR      NC,$4272            ; {}
4274: 04              INC     B                   
4275: 7D              LD      A,L                 
4276: 10 F6           ;;STOP    $F6                 
4278: 74              LD      (HL),H              
4279: F5              PUSH    AF                  
427A: 89              ADC     A,C                 
427B: 10 0F           ;;STOP    $0F                 
427D: C6 28           ADD     $28                 
427F: 0F              RRCA                        
4280: 87              ADD     A,A                 
4281: 20 21           JR      NZ,$42A4            ; {}
4283: 27              DAA                         
4284: 26 C5           LD      H,$C5               
4286: 37              SCF                         
4287: 24              INC     H                   
4288: 70              LD      (HL),B              
4289: 2B              DEC     HL                  
428A: 73              LD      (HL),E              
428B: 2C              INC     L                   
428C: 74              LD      (HL),H              
428D: 22              LD      (HLI),A             
428E: 75              LD      (HL),L              
428F: 2B              DEC     HL                  
4290: 22              LD      (HLI),A             
4291: C7              RST     0X00                
4292: 25              DEC     H                   
4293: C7              RST     0X00                
4294: 18 A0           JR      $4236               ; {}
4296: FE 04           CP      $04                 
4298: 9D              SBC     L                   
4299: 01 F4 29        LD      BC,$29F4            
429C: F7              RST     0X30                
429D: 71              LD      (HL),C              
429E: F5              PUSH    AF                  
429F: C8              RET     Z                   
42A0: 00              NOP                         
42A1: 23              INC     HL                  
42A2: C8              RET     Z                   
42A3: 01 0F C8        LD      BC,$C80F            
42A6: 02              LD      (BC),A              
42A7: 23              INC     HL                  
42A8: 06 2A           LD      B,$2A               
42AA: 82              ADD     A,D                 
42AB: 07              RLCA                        
42AC: 21 09 26        LD      HL,$2609            
42AF: 18 AC           JR      $425D               ; {}
42B1: 19              ADD     HL,DE               
42B2: 2A              LD      A,(HLI)             
42B3: 27              DAA                         
42B4: 0D              DEC     C                   
42B5: 39              ADD     HL,SP               
42B6: 2C              INC     L                   
42B7: 49              LD      C,C                 
42B8: 2A              LD      A,(HLI)             
42B9: 68              LD      L,B                 
42BA: AC              XOR     H                   
42BB: 69              LD      L,C                 
42BC: 2C              INC     L                   
42BD: 79              LD      A,C                 
42BE: 24              INC     H                   
42BF: 22              LD      (HLI),A             
42C0: C9              RET                         
42C1: 52              LD      D,D                 
42C2: C9              RET                         
42C3: C8              RET     Z                   
42C4: 04              INC     B                   
42C5: DB                              
42C6: C6 16           ADD     $16                 
42C8: DC 85 25        CALL    C,$2585             
42CB: DB                              
42CC: 76              HALT                        
42CD: 2C              INC     L                   
42CE: 82              ADD     A,D                 
42CF: 77              LD      (HL),A              
42D0: 22              LD      (HLI),A             
42D1: 79              LD      A,C                 
42D2: 28 59           JR      Z,$432D             ; {}
42D4: DC FE 04        CALL    C,$04FE             
42D7: 0D              DEC     C                   
42D8: 02              LD      (BC),A              
42D9: F4                              
42DA: 20 F6           JR      NZ,$42D2            ; {}
42DC: 29              ADD     HL,HL               
42DD: F7              RST     0X30                
42DE: 72              LD      (HL),D              
42DF: F5              PUSH    AF                  
42E0: 88              ADC     A,B                 
42E1: 11 B0 88        LD      DE,$88B0            
42E4: 31 AF 88        LD      SP,$88AF            
42E7: 41              LD      B,C                 
42E8: B0              OR      B                   
42E9: 86              ADD     A,(HL)              
42EA: 61              LD      H,C                 
42EB: AF              XOR     A                   
42EC: 01 29 C2        LD      BC,$C229            
42EF: 02              LD      (BC),A              
42F0: DC 03 2A        CALL    C,$2A03             
42F3: 82              ADD     A,D                 
42F4: 04              INC     B                   
42F5: C7              RST     0X00                
42F6: 06 29           LD      B,$29               
42F8: C5              PUSH    BC                  
42F9: 07              RLCA                        
42FA: DC 08 2A        CALL    C,$2A08             
42FD: 10 29           ;;STOP    $29                 
42FF: 19              ADD     HL,DE               
4300: 2A              LD      A,(HLI)             
4301: 8A              ADC     A,D                 
4302: 20 DB           JR      NZ,$42DF            ; {}
4304: 30 2B           JR      NC,$4331            ; {}
4306: C2 32 DB        JP      NZ,$DB32            
4309: 39              ADD     HL,SP               
430A: 2C              INC     L                   
430B: 40              LD      B,B                 
430C: 29              ADD     HL,HL               
430D: 49              LD      C,C                 
430E: 2A              LD      A,(HLI)             
430F: 8A              ADC     A,D                 
4310: 50              LD      D,B                 
4311: DC 60 2B        CALL    C,$2B60             
4314: C2 62 DB        JP      NZ,$DB62            
4317: C2 67 DB        JP      NZ,$DB67            
431A: 68              LD      L,B                 
431B: 2C              INC     L                   
431C: 69              LD      L,C                 
431D: 22              LD      (HLI),A             
431E: 71              LD      (HL),C              
431F: 2B              DEC     HL                  
4320: 73              LD      (HL),E              
4321: 2C              INC     L                   
4322: 82              ADD     A,D                 
4323: 74              LD      (HL),H              
4324: C8              RET     Z                   
4325: 76              HALT                        
4326: 2B              DEC     HL                  
4327: 78              LD      A,B                 
4328: 24              INC     H                   
4329: 79              LD      A,C                 
432A: 0F              RRCA                        
432B: FE 04           CP      $04                 
432D: 0D              DEC     C                   
432E: 10 F6           ;;STOP    $F6                 
4330: 19              ADD     HL,DE               
4331: F7              RST     0X30                
4332: 74              LD      (HL),H              
4333: F5              PUSH    AF                  
4334: 10 29           ;;STOP    $29                 
4336: 11 AC 18        LD      DE,$18AC            
4339: AC              XOR     H                   
433A: 19              ADD     HL,DE               
433B: 2A              LD      A,(HLI)             
433C: 85              ADD     A,L                 
433D: 20 DB           JR      NZ,$431A            ; {}
433F: 29              ADD     HL,HL               
4340: 0D              DEC     C                   
4341: 30 2B           JR      NC,$436E            ; {}
4343: 8A              ADC     A,D                 
4344: 50              LD      D,B                 
4345: DC C5 34        CALL    C,$34C5             
4348: DB                              
4349: 39              ADD     HL,SP               
434A: 2C              INC     L                   
434B: 40              LD      B,B                 
434C: 29              ADD     HL,HL               
434D: 49              LD      C,C                 
434E: 2A              LD      A,(HLI)             
434F: 83              ADD     A,E                 
4350: 60              LD      H,B                 
4351: 22              LD      (HLI),A             
4352: 63              LD      H,E                 
4353: 2B              DEC     HL                  
4354: C2 65 DC        JP      NZ,$DC65            
4357: 68              LD      L,B                 
4358: AC              XOR     H                   
4359: 69              LD      L,C                 
435A: 2C              INC     L                   
435B: 83              ADD     A,E                 
435C: 70              LD      (HL),B              
435D: 0F              RRCA                        
435E: 73              LD      (HL),E              
435F: 23              INC     HL                  
4360: 76              HALT                        
4361: 2C              INC     L                   
4362: 82              ADD     A,D                 
4363: 66              LD      H,(HL)              
4364: DC FE 04        CALL    C,$04FE             
4367: 1D              DEC     E                   
4368: 03              INC     BC                  
4369: F4                              
436A: 30 F6           JR      NC,$4362            ; {}
436C: 77              LD      (HL),A              
436D: F5              PUSH    AF                  
436E: 03              INC     BC                  
436F: 24              INC     H                   
4370: 04              INC     B                   
4371: AC              XOR     H                   
4372: 05              DEC     B                   
4373: 23              INC     HL                  
4374: C7              RST     0X00                
4375: 07              RLCA                        
4376: 24              INC     H                   
4377: C8              RET     Z                   
4378: 08 0F 10        LD      ($100F),SP          
437B: 29              ADD     HL,HL               
437C: 13              INC     DE                  
437D: 2A              LD      A,(HLI)             
437E: 14              INC     D                   
437F: 21 15 29        LD      HL,$2915            
4382: 20 0D           JR      NZ,$4391            ; {}
4384: 30 2B           JR      NC,$43B1            ; {}
4386: 40              LD      B,B                 
4387: 29              ADD     HL,HL               
4388: 50              LD      D,B                 
4389: DC 60 2B        CALL    C,$2B60             
438C: 27              DAA                         
438D: CA 57 CA        JP      Z,$CA57             
4390: 77              LD      (HL),A              
4391: 28 79           JR      Z,$440C             ; {}
4393: 24              INC     H                   
4394: 83              ADD     A,E                 
4395: 43              LD      B,E                 
4396: D4 83 53        CALL    NC,$5383            ; {}
4399: D4 83 63        CALL    NC,$6383            ; {}
439C: D4 FE 04        CALL    NC,$04FE            
439F: 9D              SBC     L                   
43A0: 01 F4 71        LD      BC,$71F4            
43A3: F5              PUSH    AF                  
43A4: C8              RET     Z                   
43A5: 00              NOP                         
43A6: 23              INC     HL                  
43A7: C8              RET     Z                   
43A8: 01 0F C8        LD      BC,$C80F            
43AB: 02              LD      (BC),A              
43AC: 23              INC     HL                  
43AD: C8              RET     Z                   
43AE: 09              ADD     HL,BC               
43AF: 24              INC     H                   
43B0: 29              ADD     HL,HL               
43B1: F3              DI                          
43B2: 86              ADD     A,(HL)              
43B3: 53              LD      D,E                 
43B4: DC 22 C9        CALL    C,$C922             
43B7: 52              LD      D,D                 
43B8: C9              RET                         
43B9: 06 2A           LD      B,$2A               
43BB: 82              ADD     A,D                 
43BC: 07              RLCA                        
43BD: 21 09 26        LD      HL,$2609            
43C0: C4 04 DB        CALL    NZ,$DB04            
43C3: 35              DEC     (HL)                
43C4: DB                              
43C5: C2 26 DB        JP      NZ,$DB26            
43C8: 83              ADD     A,E                 
43C9: 16 DC           LD      D,$DC               
43CB: 25              DEC     H                   
43CC: A0              AND     B                   
43CD: 07              RLCA                        
43CE: A3              AND     E                   
43CF: E1              POP     HL                  
43D0: 06 17           LD      B,$17               
43D2: 78              LD      A,B                 
43D3: 10 29           ;;STOP    $29                 
43D5: 2A              LD      A,(HLI)             
43D6: 39              ADD     HL,SP               
43D7: 0D              DEC     C                   
43D8: 49              LD      C,C                 
43D9: 2C              INC     L                   
43DA: FE 04           CP      $04                 
43DC: 0D              DEC     C                   
43DD: 01 F4 20        LD      BC,$20F4            
43E0: F6 39           OR      $39                 
43E2: F7              RST     0X30                
43E3: 01 29 02        LD      BC,$0229            
43E6: DB                              
43E7: 03              INC     BC                  
43E8: 2A              LD      A,(HLI)             
43E9: 06 29           LD      B,$29               
43EB: C3 07 DB        JP      $DB07               
43EE: C2 08 24        JP      NZ,$2408            
43F1: C2 09 0F        JP      NZ,$0F09            
43F4: 11 25 12        LD      DE,$1225            
43F7: 21 13 26        LD      HL,$2613            
43FA: C2 21 23        JP      NZ,$2321            
43FD: C2 22 01        JP      NZ,$0122            
4400: C2 23 24        JP      NZ,$2423            
4403: 83              ADD     A,E                 
4404: 37              SCF                         
4405: DB                              
4406: 28 2A           JR      Z,$4432             ; {}
4408: 29              ADD     HL,HL               
4409: 21 41 27        LD      HL,$2741            
440C: 42              LD      B,D                 
440D: 22              LD      (HLI),A             
440E: 43              LD      B,E                 
440F: 28 49           JR      Z,$445A             ; {}
4411: DC 59 2C        CALL    C,$2C59             
4414: 61              LD      H,C                 
4415: AC              XOR     H                   
4416: 36 20           LD      (HL),$20            
4418: 62              LD      H,D                 
4419: 20 67           JR      NZ,$4482            ; {}
441B: 20 68           JR      NZ,$4485            ; {}
441D: AC              XOR     H                   
441E: 20 29           JR      NZ,$4449            ; {}
4420: 30 0D           JR      NC,$442F            ; {}
4422: 40              LD      B,B                 
4423: 2B              DEC     HL                  
4424: FE 04           CP      $04                 
4426: 9D              SBC     L                   
4427: 04              INC     B                   
4428: F4                              
4429: 30 F6           JR      NC,$4421            ; {}
442B: 39              ADD     HL,SP               
442C: F7              RST     0X30                
442D: 72              LD      (HL),D              
442E: F5              PUSH    AF                  
442F: 83              ADD     A,E                 
4430: 00              NOP                         
4431: 0F              RRCA                        
4432: 03              INC     BC                  
4433: 23              INC     HL                  
4434: 04              INC     B                   
4435: DB                              
4436: 05              DEC     B                   
4437: DC 06 2A        CALL    C,$2A06             
443A: 07              RLCA                        
443B: C7              RST     0X00                
443C: 08 26 C2        LD      ($C226),SP          
443F: 09              ADD     HL,BC               
4440: 03              INC     BC                  
4441: 10 0F           ;;STOP    $0F                 
4443: 11 25 12        LD      DE,$1225            
4446: 98              SBC     B                   
4447: 13              INC     DE                  
4448: 29              ADD     HL,HL               
4449: 84              ADD     A,H                 
444A: 14              INC     D                   
444B: DC 08 26        CALL    C,$2608             
444E: 18 24           JR      $4474               ; {}
4450: 20 21           JR      NZ,$4473            ; {}
4452: 21 29 22        LD      HL,$2229            
4455: DB                              
4456: 84              ADD     A,H                 
4457: 23              INC     HL                  
4458: AC              XOR     H                   
4459: 27              DAA                         
445A: DC 28 2A        CALL    C,$2A28             
445D: 29              ADD     HL,HL               
445E: 21 83 30        LD      HL,$3083            
4461: DB                              
4462: C2 33 AC        JP      NZ,$AC33            
4465: 82              ADD     A,D                 
4466: 34              INC     (HL)                
4467: 0F              RRCA                        
4468: C2 36 AC        JP      NZ,$AC36            
446B: 83              ADD     A,E                 
446C: 37              SCF                         
446D: DC 83 40        CALL    C,$4083             ; {}
4470: DC 82 44        CALL    C,$4482             ; {}
4473: 0F              RRCA                        
4474: 83              ADD     A,E                 
4475: 47              LD      B,A                 
4476: DB                              
4477: 50              LD      D,B                 
4478: 22              LD      (HLI),A             
4479: 51              LD      D,C                 
447A: 2B              DEC     HL                  
447B: 52              LD      D,D                 
447C: DC 84 53        CALL    C,$5384             ; {}
447F: AC              XOR     H                   
4480: 57              LD      D,A                 
4481: DB                              
4482: 58              LD      E,B                 
4483: 2C              INC     L                   
4484: 59              LD      E,C                 
4485: 22              LD      (HLI),A             
4486: C2 60 03        JP      NZ,$0360            
4489: 61              LD      H,C                 
448A: 23              INC     HL                  
448B: 83              ADD     A,E                 
448C: 62              LD      H,D                 
448D: DC 83 65        CALL    C,$6583             ; {}
4490: DB                              
4491: 68              LD      L,B                 
4492: 24              INC     H                   
4493: C2 69 03        JP      NZ,$0369            
4496: 71              LD      (HL),C              
4497: 27              DAA                         
4498: 72              LD      (HL),D              
4499: C8              RET     Z                   
449A: 73              LD      (HL),E              
449B: 2B              DEC     HL                  
449C: 76              HALT                        
449D: 2C              INC     L                   
449E: 77              LD      (HL),A              
449F: C8              RET     Z                   
44A0: 78              LD      A,B                 
44A1: 28 FE           JR      Z,$44A1             ; {}
44A3: 04              INC     B                   
44A4: 0D              DEC     C                   
44A5: 05              DEC     B                   
44A6: A3              AND     E                   
44A7: 07              RLCA                        
44A8: F4                              
44A9: 30 F6           JR      NC,$44A1            ; {}
44AB: 75              LD      (HL),L              
44AC: ED                              
44AD: 07              RLCA                        
44AE: 26 C8           LD      H,$C8               
44B0: 08 0F 09        LD      ($090F),SP          
44B3: 24              INC     H                   
44B4: C6 14           ADD     $14                 
44B6: A6              AND     (HL)                
44B7: C6 17           ADD     $17                 
44B9: 24              INC     H                   
44BA: 20 29           JR      NZ,$44E5            ; {}
44BC: 30 DC           JR      NC,$449A            ; {}
44BE: 82              ADD     A,D                 
44BF: 31 0F 40        LD      SP,$400F            
44C2: DB                              
44C3: 82              ADD     A,D                 
44C4: 41              LD      B,C                 
44C5: 0F              RRCA                        
44C6: 50              LD      D,B                 
44C7: 2B              DEC     HL                  
44C8: C3 52 0F        JP      $0F52               
44CB: 71              LD      (HL),C              
44CC: 2B              DEC     HL                  
44CD: 73              LD      (HL),E              
44CE: 0D              DEC     C                   
44CF: 74              LD      (HL),H              
44D0: 2C              INC     L                   
44D1: 77              LD      (HL),A              
44D2: 28 79           JR      Z,$454D             ; {}
44D4: 24              INC     H                   
44D5: E1              POP     HL                  
44D6: 06 1A           LD      B,$1A               
44D8: 68              LD      L,B                 
44D9: 30 FE           JR      NC,$44D9            ; {}
44DB: 04              INC     B                   
44DC: 5D              LD      E,L                 
44DD: 01 F4 59        LD      BC,$59F4            
44E0: F7              RST     0X30                
44E1: C6 01           ADD     $01                 
44E3: 0F              RRCA                        
44E4: C5              PUSH    BC                  
44E5: 02              LD      (BC),A              
44E6: 23              INC     HL                  
44E7: 09              ADD     HL,BC               
44E8: 24              INC     H                   
44E9: 86              ADD     A,(HL)              
44EA: 13              INC     DE                  
44EB: 0F              RRCA                        
44EC: 86              ADD     A,(HL)              
44ED: 23              INC     HL                  
44EE: 0F              RRCA                        
44EF: 87              ADD     A,A                 
44F0: 33              INC     SP                  
44F1: 0F              RRCA                        
44F2: 86              ADD     A,(HL)              
44F3: 43              LD      B,E                 
44F4: 0F              RRCA                        
44F5: 25              DEC     H                   
44F6: 20 26           JR      NZ,$451E            ; {}
44F8: 20 35           JR      NZ,$452F            ; {}
44FA: 20 36           JR      NZ,$4532            ; {}
44FC: 20 19           JR      NZ,$4517            ; {}
44FE: 2A              LD      A,(HLI)             
44FF: 52              LD      D,D                 
4500: 27              DAA                         
4501: 87              ADD     A,A                 
4502: 53              LD      D,E                 
4503: 22              LD      (HLI),A             
4504: 88              ADC     A,B                 
4505: 61              LD      H,C                 
4506: 0F              RRCA                        
4507: 69              LD      L,C                 
4508: AC              XOR     H                   
4509: 79              LD      A,C                 
450A: 2B              DEC     HL                  
450B: FE 04           CP      $04                 
450D: 0D              DEC     C                   
450E: 30 F6           JR      NC,$4506            ; {}
4510: 39              ADD     HL,SP               
4511: F7              RST     0X30                
4512: 11 AC 18        LD      DE,$18AC            
4515: AC              XOR     H                   
4516: 61              LD      H,C                 
4517: AC              XOR     H                   
4518: 68              LD      L,B                 
4519: AC              XOR     H                   
451A: 10 29           ;;STOP    $29                 
451C: 19              ADD     HL,DE               
451D: 2A              LD      A,(HLI)             
451E: C3 20 0D        JP      $0D20               
4521: C3 29 0D        JP      $0D29               
4524: 50              LD      D,B                 
4525: 2B              DEC     HL                  
4526: 59              LD      E,C                 
4527: 2C              INC     L                   
4528: C2 42 C0        JP      NZ,$C042            
452B: C2 47 C0        JP      NZ,$C047            
452E: 84              ADD     A,H                 
452F: 23              INC     HL                  
4530: 0F              RRCA                        
4531: 8A              ADC     A,D                 
4532: 30 0F           JR      NC,$4543            ; {}
4534: 84              ADD     A,H                 
4535: 43              LD      B,E                 
4536: 0F              RRCA                        
4537: 53              LD      D,E                 
4538: FC                              
4539: E0 00           LD      ($FF00+$00),A       
453B: 0E 58           LD      C,$58               
453D: 30 FE           JR      NC,$453D            ; {}
453F: 04              INC     B                   
4540: 0D              DEC     C                   
4541: 04              INC     B                   
4542: F4                              
4543: 20 F6           JR      NZ,$453B            ; {}
4545: 29              ADD     HL,HL               
4546: F7              RST     0X30                
4547: C3 20 0D        JP      $0D20               
454A: C3 29 0D        JP      $0D29               
454D: 79              LD      A,C                 
454E: 22              LD      (HLI),A             
454F: 03              INC     BC                  
4550: 29              ADD     HL,HL               
4551: 82              ADD     A,D                 
4552: 04              INC     B                   
4553: 0D              DEC     C                   
4554: 06 2A           LD      B,$2A               
4556: 10 29           ;;STOP    $29                 
4558: 19              ADD     HL,DE               
4559: 2A              LD      A,(HLI)             
455A: 8A              ADC     A,D                 
455B: 30 0F           JR      NC,$456C            ; {}
455D: 8A              ADC     A,D                 
455E: 50              LD      D,B                 
455F: 22              LD      (HLI),A             
4560: 8A              ADC     A,D                 
4561: 60              LD      H,B                 
4562: 0F              RRCA                        
4563: 60              LD      H,B                 
4564: AC              XOR     H                   
4565: 70              LD      (HL),B              
4566: 2C              INC     L                   
4567: 41              LD      B,C                 
4568: A6              AND     (HL)                
4569: 48              LD      C,B                 
456A: A6              AND     (HL)                
456B: 68              LD      L,B                 
456C: A6              AND     (HL)                
456D: 84              ADD     A,H                 
456E: 23              INC     HL                  
456F: D4 33 D4        CALL    NC,$D433            
4572: 36 D4           LD      (HL),$D4            
4574: 84              ADD     A,H                 
4575: 43              LD      B,E                 
4576: D4 FE 04        CALL    NC,$04FE            
4579: 6D              LD      L,L                 
457A: 05              DEC     B                   
457B: EC                              
457C: 50              LD      D,B                 
457D: F6 00           OR      $00                 
457F: AC              XOR     H                   
4580: 01 23 C3        LD      BC,$C323            
4583: 02              LD      (BC),A              
4584: 0F              RRCA                        
4585: 03              INC     BC                  
4586: 0D              DEC     C                   
4587: 04              INC     B                   
4588: 2A              LD      A,(HLI)             
4589: 07              RLCA                        
458A: 26 C6           LD      H,$C6               
458C: 08 0F 10        LD      ($100F),SP          
458F: 21 11 29        LD      HL,$2911            
4592: C4 17 24        CALL    NZ,$2417            
4595: 83              ADD     A,E                 
4596: 30 0F           JR      NC,$45A7            ; {}
4598: 87              ADD     A,A                 
4599: 50              LD      D,B                 
459A: 22              LD      (HLI),A             
459B: 57              LD      D,A                 
459C: 28 89           JR      Z,$4527             ; {}
459E: 60              LD      H,B                 
459F: 0F              RRCA                        
45A0: FE 04           CP      $04                 
45A2: 07              RLCA                        
45A3: 72              LD      (HL),D              
45A4: F5              PUSH    AF                  
45A5: 02              LD      (BC),A              
45A6: C7              RST     0X00                
45A7: 03              INC     BC                  
45A8: 26 82           LD      H,$82               
45AA: 04              INC     B                   
45AB: 8B              ADC     A,E                 
45AC: 06 25           LD      B,$25               
45AE: 07              RLCA                        
45AF: C7              RST     0X00                
45B0: 13              INC     DE                  
45B1: 24              INC     H                   
45B2: 82              ADD     A,D                 
45B3: 14              INC     D                   
45B4: 8B              ADC     A,E                 
45B5: 16 23           LD      D,$23               
45B7: 23              INC     HL                  
45B8: 2A              LD      A,(HLI)             
45B9: 82              ADD     A,D                 
45BA: 24              INC     H                   
45BB: 21 26 29        LD      HL,$2926            
45BE: 28 A1           JR      Z,$4561             ; {}
45C0: 25              DEC     H                   
45C1: A2              AND     D                   
45C2: 72              LD      (HL),D              
45C3: 2B              DEC     HL                  
45C4: 73              LD      (HL),E              
45C5: 07              RLCA                        
45C6: 74              LD      (HL),H              
45C7: 2C              INC     L                   
45C8: 77              LD      (HL),A              
45C9: 2B              DEC     HL                  
45CA: 78              LD      A,B                 
45CB: 07              RLCA                        
45CC: 79              LD      A,C                 
45CD: 24              INC     H                   
45CE: E1              POP     HL                  
45CF: 06 02           LD      B,$02               
45D1: 58              LD      E,B                 
45D2: 30 FE           JR      NC,$45D2            ; {}
45D4: 04              INC     B                   
45D5: 0D              DEC     C                   
45D6: 71              LD      (HL),C              
45D7: F5              PUSH    AF                  
45D8: 02              LD      (BC),A              
45D9: C7              RST     0X00                
45DA: 03              INC     BC                  
45DB: 26 82           LD      H,$82               
45DD: 04              INC     B                   
45DE: 8B              ADC     A,E                 
45DF: 06 25           LD      B,$25               
45E1: 07              RLCA                        
45E2: C7              RST     0X00                
45E3: 13              INC     DE                  
45E4: 24              INC     H                   
45E5: 82              ADD     A,D                 
45E6: 14              INC     D                   
45E7: 8B              ADC     A,E                 
45E8: 16 23           LD      D,$23               
45EA: 23              INC     HL                  
45EB: 2A              LD      A,(HLI)             
45EC: 82              ADD     A,D                 
45ED: 24              INC     H                   
45EE: 21 26 29        LD      HL,$2926            
45F1: 28 A1           JR      Z,$4594             ; {}
45F3: 24              INC     H                   
45F4: A2              AND     D                   
45F5: 70              LD      (HL),B              
45F6: 23              INC     HL                  
45F7: 82              ADD     A,D                 
45F8: 71              LD      (HL),C              
45F9: 0D              DEC     C                   
45FA: 73              LD      (HL),E              
45FB: 2C              INC     L                   
45FC: 34              INC     (HL)                
45FD: DC E1 06        CALL    C,$06E1             
4600: 03              INC     BC                  
4601: 48              LD      C,B                 
4602: 30 FE           JR      NC,$4602            ; {}
4604: 04              INC     B                   
4605: 0D              DEC     C                   
4606: 49              LD      C,C                 
4607: F3              DI                          
4608: 74              LD      (HL),H              
4609: FB              EI                          
460A: 03              INC     BC                  
460B: C7              RST     0X00                
460C: 06 C7           LD      B,$C7               
460E: 82              ADD     A,D                 
460F: 14              INC     D                   
4610: DA C3 21        JP      C,$21C3             
4613: DA C3 28        JP      C,$28C3             
4616: DA 82 34        JP      C,$3482             
4619: DA 82 44        JP      C,$4482             ; {}
461C: DA C2 53        JP      C,$53C2             ; {}
461F: DA C2 56        JP      C,$56C2             ; {}
4622: DA E1 06        JP      C,$06E1             
4625: 05              DEC     B                   
4626: 00              NOP                         
4627: 00              NOP                         
4628: FE 04           CP      $04                 
462A: 0D              DEC     C                   
462B: 02              LD      (BC),A              
462C: F4                              
462D: 40              LD      B,B                 
462E: F6 59           OR      $59                 
4630: F7              RST     0X30                
4631: 72              LD      (HL),D              
4632: 48              LD      C,B                 
4633: 02              LD      (BC),A              
4634: 29              ADD     HL,HL               
4635: 03              INC     BC                  
4636: 0D              DEC     C                   
4637: 04              INC     B                   
4638: 2A              LD      A,(HLI)             
4639: 07              RLCA                        
463A: 29              ADD     HL,HL               
463B: 08 0D 09        LD      ($090D),SP          
463E: 24              INC     H                   
463F: 11 AC C2        LD      DE,$C2AC            
4642: 14              INC     D                   
4643: 11 C5 17        LD      DE,$17C5            
4646: A6              AND     (HL)                
4647: 83              ADD     A,E                 
4648: 21 13 32        LD      HL,$3213            
464B: 1E 42           LD      E,$42               
464D: 1F              RRA                         
464E: 59              LD      E,C                 
464F: 2A              LD      A,(HLI)             
4650: 66              LD      H,(HL)              
4651: A7              AND     A                   
4652: 67              LD      H,A                 
4653: 1D              DEC     E                   
4654: 69              LD      L,C                 
4655: 0D              DEC     C                   
4656: 79              LD      A,C                 
4657: 22              LD      (HLI),A             
4658: C2 16 D4        JP      NZ,$D416            
465B: 28 D4           JR      Z,$4631             ; {}
465D: 34              INC     (HL)                
465E: D4 71 C8        CALL    NC,$C871            
4661: 73              LD      (HL),E              
4662: C8              RET     Z                   
4663: E1              POP     HL                  
4664: 06 06           LD      B,$06               
4666: 00              NOP                         
4667: 00              NOP                         
4668: FE 04           CP      $04                 
466A: 0D              DEC     C                   
466B: 01 F4 39        LD      BC,$39F4            
466E: F7              RST     0X30                
466F: 50              LD      D,B                 
4670: F6 71           OR      $71                 
4672: F5              PUSH    AF                  
4673: 04              INC     B                   
4674: C7              RST     0X00                
4675: 07              RLCA                        
4676: C7              RST     0X00                
4677: 00              NOP                         
4678: 23              INC     HL                  
4679: 82              ADD     A,D                 
467A: 01 0D 03        LD      BC,$030D            
467D: 2A              LD      A,(HLI)             
467E: 38 13           JR      C,$4693             ; {}
4680: 47              LD      B,A                 
4681: 1E 50           LD      E,$50               
4683: 29              ADD     HL,HL               
4684: 85              ADD     A,L                 
4685: 51              LD      D,C                 
4686: DC 57 1C        CALL    C,$1C57             
4689: 60              LD      H,B                 
468A: 0D              DEC     C                   
468B: 61              LD      H,C                 
468C: A7              AND     A                   
468D: 83              ADD     A,E                 
468E: 64              LD      H,H                 
468F: 1D              DEC     E                   
4690: 67              LD      H,A                 
4691: 1F              RRA                         
4692: 70              LD      (HL),B              
4693: 2B              DEC     HL                  
4694: 82              ADD     A,D                 
4695: 71              LD      (HL),C              
4696: 0D              DEC     C                   
4697: 73              LD      (HL),E              
4698: 2C              INC     L                   
4699: 76              HALT                        
469A: 2B              DEC     HL                  
469B: 82              ADD     A,D                 
469C: 77              LD      (HL),A              
469D: 0D              DEC     C                   
469E: 79              LD      A,C                 
469F: 24              INC     H                   
46A0: 82              ADD     A,D                 
46A1: 12              LD      (DE),A              
46A2: D4 82 15        CALL    NC,$1582            
46A5: D4 23 D4        CALL    NC,$D423            
46A8: 25              DEC     H                   
46A9: D4 C3 38        CALL    NC,$38C3            
46AC: 11 68 15        LD      DE,$1568            
46AF: E1              POP     HL                  
46B0: 06 07           LD      B,$07               
46B2: 00              NOP                         
46B3: 00              NOP                         
46B4: FE 04           CP      $04                 
46B6: 0D              DEC     C                   
46B7: 30 F6           JR      NC,$46AF            ; {}
46B9: 77              LD      (HL),A              
46BA: F5              PUSH    AF                  
46BB: C2 31 0F        JP      NZ,$0F31            
46BE: 20 C9           JR      NZ,$4689            ; {}
46C0: 50              LD      D,B                 
46C1: C9              RET                         
46C2: 29              ADD     HL,HL               
46C3: CA 59 CA        JP      Z,$CA59             
46C6: 77              LD      (HL),A              
46C7: 2B              DEC     HL                  
46C8: 79              LD      A,C                 
46C9: 24              INC     H                   
46CA: 78              LD      A,B                 
46CB: DB                              
46CC: 02              LD      (BC),A              
46CD: 26 07           LD      H,$07               
46CF: 25              DEC     H                   
46D0: 03              INC     BC                  
46D1: AC              XOR     H                   
46D2: 82              ADD     A,D                 
46D3: 04              INC     B                   
46D4: C7              RST     0X00                
46D5: 06 AC           LD      B,$AC               
46D7: 12              LD      (DE),A              
46D8: 2A              LD      A,(HLI)             
46D9: 13              INC     DE                  
46DA: 26 82           LD      H,$82               
46DC: 14              INC     D                   
46DD: 0F              RRCA                        
46DE: 82              ADD     A,D                 
46DF: 24              INC     H                   
46E0: 0F              RRCA                        
46E1: 16 25           LD      D,$25               
46E3: 17              RLA                         
46E4: 29              ADD     HL,HL               
46E5: 23              INC     HL                  
46E6: 24              INC     H                   
46E7: 33              INC     SP                  
46E8: 2A              LD      A,(HLI)             
46E9: 82              ADD     A,D                 
46EA: 34              INC     (HL)                
46EB: 97              SUB     A                   
46EC: 26 23           LD      H,$23               
46EE: 36 29           LD      (HL),$29            
46F0: 43              LD      B,E                 
46F1: AC              XOR     H                   
46F2: 46              LD      B,(HL)              
46F3: AC              XOR     H                   
46F4: FE 04           CP      $04                 
46F6: 2D              DEC     L                   
46F7: 04              INC     B                   
46F8: F4                              
46F9: 04              INC     B                   
46FA: FA 07 A2        LD      A,($A207)           
46FD: 39              ADD     HL,SP               
46FE: F7              RST     0X30                
46FF: 75              LD      (HL),L              
4700: F5              PUSH    AF                  
4701: 20 C9           JR      NZ,$46CC            ; {}
4703: 50              LD      D,B                 
4704: C9              RET                         
4705: C2 39 0D        JP      NZ,$0D39            
4708: 34              INC     (HL)                
4709: 2C              INC     L                   
470A: 35              DEC     (HL)                
470B: 2B              DEC     HL                  
470C: 44              LD      B,H                 
470D: 2A              LD      A,(HLI)             
470E: 45              LD      B,L                 
470F: 29              ADD     HL,HL               
4710: 75              LD      (HL),L              
4711: 2B              DEC     HL                  
4712: 76              HALT                        
4713: 0D              DEC     C                   
4714: 77              LD      (HL),A              
4715: 2C              INC     L                   
4716: E1              POP     HL                  
4717: 06 09           LD      B,$09               
4719: 78              LD      A,B                 
471A: 10 FE           ;;STOP    $FE                 
471C: 04              INC     B                   
471D: 4D              LD      C,L                 
471E: 10 F6           ;;STOP    $F6                 
4720: 75              LD      (HL),L              
4721: ED                              
4722: 02              LD      (BC),A              
4723: 3F              CCF                         
4724: 72              LD      (HL),D              
4725: 40              LD      B,B                 
4726: 01 C7 03        LD      BC,$03C7            
4729: C7              RST     0X00                
472A: 71              LD      (HL),C              
472B: C8              RET     Z                   
472C: 73              LD      (HL),E              
472D: C8              RET     Z                   
472E: C6 10           ADD     $10                 
4730: 0D              DEC     C                   
4731: C6 11           ADD     $11                 
4733: A7              AND     A                   
4734: C6 13           ADD     $13                 
4736: A6              AND     (HL)                
4737: 18 20           JR      $4759               ; {}
4739: 68              LD      L,B                 
473A: 20 74           JR      NZ,$47B0            ; {}
473C: 2B              DEC     HL                  
473D: 82              ADD     A,D                 
473E: 75              LD      (HL),L              
473F: 0D              DEC     C                   
4740: 77              LD      (HL),A              
4741: 2C              INC     L                   
4742: 84              ADD     A,H                 
4743: 14              INC     D                   
4744: D4 27 D4        CALL    NC,$D427            
4747: 82              ADD     A,D                 
4748: 37              SCF                         
4749: D4 FE 04        CALL    NC,$04FE            
474C: 1D              DEC     E                   
474D: 03              INC     BC                  
474E: F4                              
474F: 73              LD      (HL),E              
4750: F5              PUSH    AF                  
4751: 72              LD      (HL),D              
4752: C8              RET     Z                   
4753: 76              HALT                        
4754: C8              RET     Z                   
4755: 03              INC     BC                  
4756: 2A              LD      A,(HLI)             
4757: 82              ADD     A,D                 
4758: 04              INC     B                   
4759: 21 06 29        LD      HL,$2906            
475C: C3 13 DC        JP      $DC13               
475F: 83              ADD     A,E                 
4760: 14              INC     D                   
4761: 1D              DEC     E                   
4762: 26 DC           LD      H,$DC               
4764: 27              DAA                         
4765: 1D              DEC     E                   
4766: 82              ADD     A,D                 
4767: 31 1D 28        LD      SP,$281D            
476A: 2C              INC     L                   
476B: 29              ADD     HL,HL               
476C: 28 C4           JR      Z,$4732             ; {}
476E: 38 24           JR      C,$4794             ; {}
4770: C5              PUSH    BC                  
4771: 39              ADD     HL,SP               
4772: 0F              RRCA                        
4773: 73              LD      (HL),E              
4774: 2B              DEC     HL                  
4775: 74              LD      (HL),H              
4776: 0D              DEC     C                   
4777: 75              LD      (HL),L              
4778: 2C              INC     L                   
4779: 78              LD      A,B                 
477A: 28 21           JR      Z,$479D             ; {}
477C: D4 C2 41        CALL    NC,$41C2            ; {}
477F: D4 57 D4        CALL    NC,$D457            
4782: 83              ADD     A,E                 
4783: 65              LD      H,L                 
4784: D4 E1 06        CALL    NC,$06E1            
4787: 0B              DEC     BC                  
4788: 00              NOP                         
4789: 00              NOP                         
478A: FE 04           CP      $04                 
478C: 0D              DEC     C                   
478D: 07              RLCA                        
478E: F4                              
478F: 30 F6           JR      NC,$4787            ; {}
4791: 75              LD      (HL),L              
4792: F5              PUSH    AF                  
4793: 00              NOP                         
4794: 2C              INC     L                   
4795: 01 2B 02        LD      BC,$022B            
4798: 25              DEC     H                   
4799: 03              INC     BC                  
479A: C7              RST     0X00                
479B: 06 C7           LD      B,$C7               
479D: 07              RLCA                        
479E: 29              ADD     HL,HL               
479F: 08 0D 09        LD      ($090D),SP          
47A2: 24              INC     H                   
47A3: 10 24           ;;STOP    $24                 
47A5: 11 23 C6        LD      DE,$C623            
47A8: 12              LD      (DE),A              
47A9: 23              INC     HL                  
47AA: 82              ADD     A,D                 
47AB: 13              INC     DE                  
47AC: DC 82 23        CALL    C,$2382             
47AF: DC 82 33        CALL    C,$3382             
47B2: DC 84 43        CALL    C,$4384             ; {}
47B5: DC 86 53        CALL    C,$5386             ; {}
47B8: DC 84 63        CALL    C,$6384             ; {}
47BB: DC 20 2A        CALL    C,$2A20             
47BE: 21 29 C5        LD      HL,$C529            
47C1: 30 0F           JR      NC,$47D2            ; {}
47C3: C5              PUSH    BC                  
47C4: 31 0F 71        LD      SP,$710F            
47C7: C0              RET     NZ                  
47C8: 72              LD      (HL),D              
47C9: 27              DAA                         
47CA: 75              LD      (HL),L              
47CB: 2B              DEC     HL                  
47CC: 76              HALT                        
47CD: DC 77 2C        CALL    C,$2C77             
47D0: 83              ADD     A,E                 
47D1: 15              DEC     D                   
47D2: 0F              RRCA                        
47D3: 83              ADD     A,E                 
47D4: 25              DEC     H                   
47D5: 0F              RRCA                        
47D6: 83              ADD     A,E                 
47D7: 35              DEC     (HL)                
47D8: 0F              RRCA                        
47D9: 26 BE           LD      H,$BE               
47DB: 23              INC     HL                  
47DC: A0              AND     B                   
47DD: 58              LD      E,B                 
47DE: 1D              DEC     E                   
47DF: 82              ADD     A,D                 
47E0: 47              LD      B,A                 
47E1: A6              AND     (HL)                
47E2: E1              POP     HL                  
47E3: 06 0C           LD      B,$0C               
47E5: 58              LD      E,B                 
47E6: 10 08           ;;STOP    $08                 
47E8: DB                              
47E9: FE 04           CP      $04                 
47EB: 0D              DEC     C                   
47EC: 05              DEC     B                   
47ED: F4                              
47EE: 39              ADD     HL,SP               
47EF: F7              RST     0X30                
47F0: 05              DEC     B                   
47F1: 29              ADD     HL,HL               
47F2: 06 0D           LD      B,$0D               
47F4: 07              RLCA                        
47F5: 2A              LD      A,(HLI)             
47F6: 11 AC 14        LD      DE,$14AC            
47F9: 1D              DEC     E                   
47FA: 18 AC           JR      $47A8               ; {}
47FC: 21 1D 27        LD      HL,$271D            
47FF: 1D              DEC     E                   
4800: 39              ADD     HL,SP               
4801: 2A              LD      A,(HLI)             
4802: 49              LD      C,C                 
4803: 0D              DEC     C                   
4804: 41              LD      B,C                 
4805: 1D              DEC     E                   
4806: 47              LD      B,A                 
4807: 1D              DEC     E                   
4808: 59              LD      E,C                 
4809: 2C              INC     L                   
480A: 61              LD      H,C                 
480B: AC              XOR     H                   
480C: 64              LD      H,H                 
480D: 1D              DEC     E                   
480E: 68              LD      L,B                 
480F: AC              XOR     H                   
4810: 32              LD      (HLD),A             
4811: 0F              RRCA                        
4812: E1              POP     HL                  
4813: 06 0D           LD      B,$0D               
4815: 00              NOP                         
4816: 00              NOP                         
4817: FE 04           CP      $04                 
4819: 0D              DEC     C                   
481A: 02              LD      (BC),A              
481B: 47              LD      B,A                 
481C: 30 F6           JR      NC,$4814            ; {}
481E: 49              LD      C,C                 
481F: F7              RST     0X30                
4820: 82              ADD     A,D                 
4821: 13              INC     DE                  
4822: A6              AND     (HL)                
4823: 82              ADD     A,D                 
4824: 27              DAA                         
4825: 0F              RRCA                        
4826: 82              ADD     A,D                 
4827: 17              RLA                         
4828: 0F              RRCA                        
4829: 84              ADD     A,H                 
482A: 23              INC     HL                  
482B: 1D              DEC     E                   
482C: 30 29           JR      NC,$4857            ; {}
482E: 82              ADD     A,D                 
482F: 31 A7 84        LD      SP,$84A7            
4832: 33              INC     SP                  
4833: A6              AND     (HL)                
4834: 82              ADD     A,D                 
4835: 37              SCF                         
4836: 0F              RRCA                        
4837: 40              LD      B,B                 
4838: 0D              DEC     C                   
4839: 46              LD      B,(HL)              
483A: A6              AND     (HL)                
483B: 82              ADD     A,D                 
483C: 47              LD      B,A                 
483D: A7              AND     A                   
483E: 49              LD      C,C                 
483F: 2A              LD      A,(HLI)             
4840: 50              LD      D,B                 
4841: 2B              DEC     HL                  
4842: 59              LD      E,C                 
4843: 0D              DEC     C                   
4844: 69              LD      L,C                 
4845: 2C              INC     L                   
4846: 04              INC     B                   
4847: 29              ADD     HL,HL               
4848: 82              ADD     A,D                 
4849: 05              DEC     B                   
484A: 0D              DEC     C                   
484B: 07              RLCA                        
484C: 2A              LD      A,(HLI)             
484D: 82              ADD     A,D                 
484E: 15              DEC     D                   
484F: 13              INC     DE                  
4850: 35              DEC     (HL)                
4851: 12              LD      (DE),A              
4852: 28 A1           JR      Z,$47F5             ; {}
4854: E1              POP     HL                  
4855: 06 0E           LD      B,$0E               
4857: 00              NOP                         
4858: 00              NOP                         
4859: FE 04           CP      $04                 
485B: 0D              DEC     C                   
485C: 03              INC     BC                  
485D: F4                              
485E: 50              LD      D,B                 
485F: F6 29           OR      $29                 
4861: F7              RST     0X30                
4862: 03              INC     BC                  
4863: 29              ADD     HL,HL               
4864: 04              INC     B                   
4865: 0D              DEC     C                   
4866: 05              DEC     B                   
4867: 2A              LD      A,(HLI)             
4868: 08 26 C2        LD      ($C226),SP          
486B: 09              ADD     HL,BC               
486C: 0F              RRCA                        
486D: 11 AC C3        LD      DE,$C3AC            
4870: 12              LD      (DE),A              
4871: 10 83           ;;STOP    $83                 
4873: 13              INC     DE                  
4874: 0F              RRCA                        
4875: C3 16 11        JP      $1116               
4878: 07              RLCA                        
4879: A3              AND     E                   
487A: E1              POP     HL                  
487B: 06 2A           LD      B,$2A               
487D: 88              ADC     A,B                 
487E: 20 18           JR      NZ,$4898            ; {}
4880: 24              INC     H                   
4881: 83              ADD     A,E                 
4882: 23              INC     HL                  
4883: 0F              RRCA                        
4884: 28 2A           JR      Z,$48B0             ; {}
4886: 29              ADD     HL,HL               
4887: 21 83 33        LD      HL,$3383            
488A: 0F              RRCA                        
488B: C2 39 DB        JP      NZ,$DB39            
488E: 40              LD      B,B                 
488F: 29              ADD     HL,HL               
4890: 42              LD      B,D                 
4891: 94              SUB     H                   
4892: 83              ADD     A,E                 
4893: 43              LD      B,E                 
4894: 12              LD      (DE),A              
4895: 46              LD      B,(HL)              
4896: 93              SUB     E                   
4897: 50              LD      D,B                 
4898: 0D              DEC     C                   
4899: 59              LD      E,C                 
489A: 2C              INC     L                   
489B: 60              LD      H,B                 
489C: 2B              DEC     HL                  
489D: FE 04           CP      $04                 
489F: 0D              DEC     C                   
48A0: 05              DEC     B                   
48A1: F4                              
48A2: 20 F6           JR      NZ,$489A            ; {}
48A4: 82              ADD     A,D                 
48A5: 00              NOP                         
48A6: 0F              RRCA                        
48A7: 02              LD      (BC),A              
48A8: 25              DEC     H                   
48A9: 04              INC     B                   
48AA: C7              RST     0X00                
48AB: 05              DEC     B                   
48AC: 29              ADD     HL,HL               
48AD: 06 DC           LD      B,$DC               
48AF: 07              RLCA                        
48B0: 2A              LD      A,(HLI)             
48B1: 08 C7 82        LD      ($82C7),SP          
48B4: 10 0F           ;;STOP    $0F                 
48B6: 12              LD      (DE),A              
48B7: 23              INC     HL                  
48B8: 82              ADD     A,D                 
48B9: 20 21           JR      NZ,$48DC            ; {}
48BB: 21 98 22        LD      HL,$2298            
48BE: 29              ADD     HL,HL               
48BF: 24              INC     H                   
48C0: 20 27           JR      NZ,$48E9            ; {}
48C2: 20 C2           JR      NZ,$4886            ; {}
48C4: 30 DB           JR      NC,$48A1            ; {}
48C6: 31 DE 44        LD      SP,$44DE            
48C9: 20 47           JR      NZ,$4912            ; {}
48CB: 20 50           JR      NZ,$491D            ; {}
48CD: 2B              DEC     HL                  
48CE: 64              LD      H,H                 
48CF: 20 67           JR      NZ,$4938            ; {}
48D1: 20 01           JR      NZ,$48D4            ; {}
48D3: C0              RET     NZ                  
48D4: FE 07           CP      $07                 
48D6: 0D              DEC     C                   
48D7: 29              ADD     HL,HL               
48D8: CF              RST     0X08                
48D9: 29              ADD     HL,HL               
48DA: F3              DI                          
48DB: 74              LD      (HL),H              
48DC: F5              PUSH    AF                  
48DD: 03              INC     BC                  
48DE: C7              RST     0X00                
48DF: 06 C7           LD      B,$C7               
48E1: 60              LD      H,B                 
48E2: 27              DAA                         
48E3: 88              ADC     A,B                 
48E4: 61              LD      H,C                 
48E5: 22              LD      (HLI),A             
48E6: 63              LD      H,E                 
48E7: 2B              DEC     HL                  
48E8: 82              ADD     A,D                 
48E9: 64              LD      H,H                 
48EA: 0D              DEC     C                   
48EB: 66              LD      H,(HL)              
48EC: 2C              INC     L                   
48ED: 69              LD      L,C                 
48EE: 28 70           JR      Z,$4960             ; {}
48F0: 2C              INC     L                   
48F1: 71              LD      (HL),C              
48F2: 22              LD      (HLI),A             
48F3: 72              LD      (HL),D              
48F4: 2B              DEC     HL                  
48F5: 73              LD      (HL),E              
48F6: 23              INC     HL                  
48F7: 82              ADD     A,D                 
48F8: 74              LD      (HL),H              
48F9: 0D              DEC     C                   
48FA: 76              HALT                        
48FB: 24              INC     H                   
48FC: 77              LD      (HL),A              
48FD: 2C              INC     L                   
48FE: 78              LD      A,B                 
48FF: 22              LD      (HLI),A             
4900: 79              LD      A,C                 
4901: 2B              DEC     HL                  
4902: FE 07           CP      $07                 
4904: 0D              DEC     C                   
4905: 20 F6           JR      NZ,$48FD            ; {}
4907: 85              ADD     A,L                 
4908: 12              LD      (DE),A              
4909: D2 C4 17        JP      NC,$17C4            
490C: CF              RST     0X08                
490D: 85              ADD     A,L                 
490E: 53              LD      D,E                 
490F: D1              POP     DE                  
4910: C4 22 D0        CALL    NZ,$D022            
4913: 62              LD      H,D                 
4914: 2C              INC     L                   
4915: 84              ADD     A,H                 
4916: 63              LD      H,E                 
4917: 22              LD      (HLI),A             
4918: 67              LD      H,A                 
4919: 2B              DEC     HL                  
491A: 72              LD      (HL),D              
491B: 28 73           JR      Z,$4990             ; {}
491D: 2C              INC     L                   
491E: 82              ADD     A,D                 
491F: 74              LD      (HL),H              
4920: 22              LD      (HLI),A             
4921: 76              HALT                        
4922: 2B              DEC     HL                  
4923: 77              LD      (HL),A              
4924: 27              DAA                         
4925: 61              LD      H,C                 
4926: AC              XOR     H                   
4927: 68              LD      L,B                 
4928: AC              XOR     H                   
4929: 28 A1           JR      Z,$48CC             ; {}
492B: FE 04           CP      $04                 
492D: 0D              DEC     C                   
492E: 29              ADD     HL,HL               
492F: F7              RST     0X30                
4930: 76              HALT                        
4931: F5              PUSH    AF                  
4932: 03              INC     BC                  
4933: C7              RST     0X00                
4934: 06 C7           LD      B,$C7               
4936: 11 20 18        LD      DE,$1820            
4939: 20 61           JR      NZ,$499C            ; {}
493B: 20 68           JR      NZ,$49A5            ; {}
493D: 20 29           JR      NZ,$4968            ; {}
493F: 2A              LD      A,(HLI)             
4940: 85              ADD     A,L                 
4941: 35              DEC     (HL)                
4942: DC 49 2C        CALL    C,$2C49             
4945: C3 44 DC        JP      $DC44               
4948: 72              LD      (HL),D              
4949: 2B              DEC     HL                  
494A: 73              LD      (HL),E              
494B: 0D              DEC     C                   
494C: 74              LD      (HL),H              
494D: 2C              INC     L                   
494E: 63              LD      H,E                 
494F: DE FE           SBC     $FE                 
4951: 04              INC     B                   
4952: 8D              ADC     A,L                 
4953: 04              INC     B                   
4954: F4                              
4955: 20 F6           JR      NZ,$494D            ; {}
4957: 89              ADC     A,C                 
4958: 11 1C 89        LD      DE,$891C            
495B: 21 1C 89        LD      HL,$891C            
495E: 31 1C 89        LD      SP,$891C            
4961: 41              LD      B,C                 
4962: 1C              INC     E                   
4963: 89              ADC     A,C                 
4964: 51              LD      D,C                 
4965: 1C              INC     E                   
4966: 89              ADC     A,C                 
4967: 61              LD      H,C                 
4968: 1C              INC     E                   
4969: 89              ADC     A,C                 
496A: 71              LD      (HL),C              
496B: 1C              INC     E                   
496C: 00              NOP                         
496D: 2A              LD      A,(HLI)             
496E: 01 C7 02        LD      BC,$02C7            
4971: 29              ADD     HL,HL               
4972: 03              INC     BC                  
4973: 23              INC     HL                  
4974: 82              ADD     A,D                 
4975: 04              INC     B                   
4976: 0D              DEC     C                   
4977: 06 24           LD      B,$24               
4979: 07              RLCA                        
497A: 2A              LD      A,(HLI)             
497B: 08 C7 09        LD      ($09C7),SP          
497E: 29              ADD     HL,HL               
497F: 03              INC     BC                  
4980: 23              INC     HL                  
4981: 10 03           ;;STOP    $03                 
4983: 11 25 12        LD      DE,$1225            
4986: 21 13 29        LD      HL,$2913            
4989: 20 21           JR      NZ,$49AC            ; {}
498B: 21 29 82        LD      HL,$8229            
498E: 30 DC           JR      NC,$496C            ; {}
4990: 40              LD      B,B                 
4991: 2B              DEC     HL                  
4992: C3 16 11        JP      $1116               
4995: 86              ADD     A,(HL)              
4996: 41              LD      B,C                 
4997: 1E 82           LD      E,$82               
4999: 14              INC     D                   
499A: 0D              DEC     C                   
499B: 84              ADD     A,H                 
499C: 22              LD      (HLI),A             
499D: 0D              DEC     C                   
499E: 84              ADD     A,H                 
499F: 32              LD      (HLD),A             
49A0: 0D              DEC     C                   
49A1: 16 2A           LD      D,$2A               
49A3: 83              ADD     A,E                 
49A4: 17              RLA                         
49A5: 21 E1 06        LD      HL,$06E1            
49A8: 14              INC     D                   
49A9: 00              NOP                         
49AA: 00              NOP                         
49AB: FE 04           CP      $04                 
49AD: 7D              LD      A,L                 
49AE: 34              INC     (HL)                
49AF: BE              CP      (HL)                
49B0: E1              POP     HL                  
49B1: 06 2B           LD      B,$2B               
49B3: 18 10           JR      $49C5               ; {}
49B5: FE 04           CP      $04                 
49B7: 0D              DEC     C                   
49B8: 77              LD      (HL),A              
49B9: F5              PUSH    AF                  
49BA: 82              ADD     A,D                 
49BB: 11 0F 82        LD      DE,$820F            
49BE: 21 0F 82        LD      HL,$820F            
49C1: 31 0F 82        LD      SP,$820F            
49C4: 17              RLA                         
49C5: 0F              RRCA                        
49C6: 27              DAA                         
49C7: 0F              RRCA                        
49C8: 82              ADD     A,D                 
49C9: 37              SCF                         
49CA: 0F              RRCA                        
49CB: 33              INC     SP                  
49CC: A7              AND     A                   
49CD: 36 A7           LD      (HL),$A7            
49CF: 53              LD      D,E                 
49D0: AC              XOR     H                   
49D1: 56              LD      D,(HL)              
49D2: AC              XOR     H                   
49D3: 28 A1           JR      Z,$4976             ; {}
49D5: FE 04           CP      $04                 
49D7: 0D              DEC     C                   
49D8: 06 F0           LD      B,$F0               
49DA: 29              ADD     HL,HL               
49DB: F7              RST     0X30                
49DC: 82              ADD     A,D                 
49DD: 00              NOP                         
49DE: 03              INC     BC                  
49DF: 02              LD      (BC),A              
49E0: 23              INC     HL                  
49E1: 03              INC     BC                  
49E2: 0D              DEC     C                   
49E3: 04              INC     B                   
49E4: 2A              LD      A,(HLI)             
49E5: 10 25           ;;STOP    $25                 
49E7: 11 21 12        LD      DE,$1221            
49EA: 29              ADD     HL,HL               
49EB: 18 AC           JR      $4999               ; {}
49ED: 21 AC 29        LD      HL,$29AC            
49F0: 2A              LD      A,(HLI)             
49F1: 39              ADD     HL,SP               
49F2: DB                              
49F3: 49              LD      C,C                 
49F4: 2C              INC     L                   
49F5: 22              LD      (HLI),A             
49F6: D4 C2 31        CALL    NC,$31C2            
49F9: D4 C2 48        CALL    NC,$48C2            ; {}
49FC: D4 82 67        CALL    NC,$6782            ; {}
49FF: D4 FE 04        CALL    NC,$04FE            
4A02: 9D              SBC     L                   
4A03: 20 F6           JR      NZ,$49FB            ; {}
4A05: 75              LD      (HL),L              
4A06: F5              PUSH    AF                  
4A07: C8              RET     Z                   
4A08: 00              NOP                         
4A09: 23              INC     HL                  
4A0A: 20 29           JR      NZ,$4A35            ; {}
4A0C: 40              LD      B,B                 
4A0D: 2B              DEC     HL                  
4A0E: 88              ADC     A,B                 
4A0F: 72              LD      (HL),D              
4A10: 22              LD      (HLI),A             
4A11: 72              LD      (HL),D              
4A12: 2C              INC     L                   
4A13: 75              LD      (HL),L              
4A14: 2B              DEC     HL                  
4A15: 77              LD      (HL),A              
4A16: 2C              INC     L                   
4A17: 82              ADD     A,D                 
4A18: 01 1C 87        LD      BC,$871C            
4A1B: 03              INC     BC                  
4A1C: 1C              INC     E                   
4A1D: 89              ADC     A,C                 
4A1E: 11 1F C6        LD      DE,$C61F            
4A21: 18 1C           JR      $4A3F               ; {}
4A23: C6 19           ADD     $19                 
4A25: 1C              INC     E                   
4A26: 83              ADD     A,E                 
4A27: 21 13 84        LD      HL,$8413            
4A2A: 24              INC     H                   
4A2B: 13              INC     DE                  
4A2C: C4 37 11        CALL    NZ,$1137            
4A2F: 87              ADD     A,A                 
4A30: 30 DB           JR      NC,$4A0D            ; {}
4A32: 42              LD      B,D                 
4A33: 17              RLA                         
4A34: 82              ADD     A,D                 
4A35: 43              LD      B,E                 
4A36: 12              LD      (DE),A              
4A37: 45              LD      B,L                 
4A38: 16 C2           LD      D,$C2               
4A3A: 52              LD      D,D                 
4A3B: 11 C2 55        LD      DE,$55C2            
4A3E: 10 82           ;;STOP    $82                 
4A40: 53              LD      D,E                 
4A41: 1E 82           LD      E,$82               
4A43: 63              LD      H,E                 
4A44: 1C              INC     E                   
4A45: C4 46 DC        CALL    NZ,$DC46            
4A48: 27              DAA                         
4A49: 95              SUB     L                   
4A4A: E1              POP     HL                  
4A4B: 06 18           LD      B,$18               
4A4D: 00              NOP                         
4A4E: 00              NOP                         
4A4F: FE 04           CP      $04                 
4A51: 6D              LD      L,L                 
4A52: 29              ADD     HL,HL               
4A53: F7              RST     0X30                
4A54: 72              LD      (HL),D              
4A55: F5              PUSH    AF                  
4A56: 89              ADC     A,C                 
4A57: 00              NOP                         
4A58: 1C              INC     E                   
4A59: C6 10           ADD     $10                 
4A5B: 1C              INC     E                   
4A5C: C6 11           ADD     $11                 
4A5E: 1C              INC     E                   
4A5F: 87              ADD     A,A                 
4A60: 12              LD      (DE),A              
4A61: 1F              RRA                         
4A62: C5              PUSH    BC                  
4A63: 22              LD      (HLI),A             
4A64: 10 86           ;;STOP    $86                 
4A66: 23              INC     HL                  
4A67: 12              LD      (DE),A              
4A68: 34              INC     (HL)                
4A69: 13              INC     DE                  
4A6A: 38 13           JR      C,$4A7F             ; {}
4A6C: 44              LD      B,H                 
4A6D: 11 84 45        LD      DE,$4584            
4A70: 1E 54           LD      E,$54               
4A72: 1E 84           LD      E,$84               
4A74: 55              LD      D,L                 
4A75: 1C              INC     E                   
4A76: 85              ADD     A,L                 
4A77: 64              LD      H,H                 
4A78: 1C              INC     E                   
4A79: 72              LD      (HL),D              
4A7A: 2B              DEC     HL                  
4A7B: 73              LD      (HL),E              
4A7C: 0D              DEC     C                   
4A7D: 74              LD      (HL),H              
4A7E: 2C              INC     L                   
4A7F: E1              POP     HL                  
4A80: 06 19           LD      B,$19               
4A82: 00              NOP                         
4A83: 00              NOP                         
4A84: FE 04           CP      $04                 
4A86: 0D              DEC     C                   
4A87: 07              RLCA                        
4A88: F0 20           LD      A,($20)             
4A8A: F2                              
4A8B: 03              INC     BC                  
4A8C: 26 82           LD      H,$82               
4A8E: 04              INC     B                   
4A8F: 0F              RRCA                        
4A90: 06 25           LD      B,$25               
4A92: 13              INC     DE                  
4A93: 24              INC     H                   
4A94: 82              ADD     A,D                 
4A95: 14              INC     D                   
4A96: 0F              RRCA                        
4A97: 16 23           LD      D,$23               
4A99: 23              INC     HL                  
4A9A: 2A              LD      A,(HLI)             
4A9B: 82              ADD     A,D                 
4A9C: 24              INC     H                   
4A9D: 21 26 29        LD      HL,$2926            
4AA0: 61              LD      H,C                 
4AA1: AC              XOR     H                   
4AA2: 68              LD      L,B                 
4AA3: AC              XOR     H                   
4AA4: FE 04           CP      $04                 
4AA6: 1D              DEC     E                   
4AA7: 01 F4 49        LD      BC,$49F4            
4AAA: F3              DI                          
4AAB: 01 0D 02        LD      BC,$020D            
4AAE: 2A              LD      A,(HLI)             
4AAF: 82              ADD     A,D                 
4AB0: 03              INC     BC                  
4AB1: 21 05 29        LD      HL,$2905            
4AB4: C3 06 DC        JP      $DC06               
4AB7: C3 07 24        JP      $2407               
4ABA: 08 12 09        LD      ($0912),SP          
4ABD: 16 11           LD      D,$11               
4ABF: A7              AND     A                   
4AC0: C2 19 10        JP      NZ,$1019            
4AC3: 37              SCF                         
4AC4: 2A              LD      A,(HLI)             
4AC5: 38 98           JR      C,$4A5F             ; {}
4AC7: 39              ADD     HL,SP               
4AC8: 26 FE           LD      H,$FE               
4ACA: 04              INC     B                   
4ACB: 0D              DEC     C                   
4ACC: 02              LD      (BC),A              
4ACD: F4                              
4ACE: 40              LD      B,B                 
4ACF: F2                              
4AD0: 02              LD      (BC),A              
4AD1: 29              ADD     HL,HL               
4AD2: 03              INC     BC                  
4AD3: 0D              DEC     C                   
4AD4: 04              INC     B                   
4AD5: 2A              LD      A,(HLI)             
4AD6: 06 C7           LD      B,$C7               
4AD8: 18 BE           JR      $4A98               ; {}
4ADA: 08 C7 49        LD      ($49C7),SP          ; {}
4ADD: CA 16 DB        JP      Z,$DB16             
4AE0: 83              ADD     A,E                 
4AE1: 26 DB           LD      H,$DB               
4AE3: E1              POP     HL                  
4AE4: 06 1D           LD      B,$1D               
4AE6: 78              LD      A,B                 
4AE7: 10 FE           ;;STOP    $FE                 
4AE9: 04              INC     B                   
4AEA: 9D              SBC     L                   
4AEB: 02              LD      (BC),A              
4AEC: F4                              
4AED: 20 F6           JR      NZ,$4AE5            ; {}
4AEF: 71              LD      (HL),C              
4AF0: F5              PUSH    AF                  
4AF1: 00              NOP                         
4AF2: 2A              LD      A,(HLI)             
4AF3: 01 C7 02        LD      BC,$02C7            
4AF6: 29              ADD     HL,HL               
4AF7: C2 03 23        JP      NZ,$2303            
4AFA: C3 06 24        JP      $2406               
4AFD: 07              RLCA                        
4AFE: 2A              LD      A,(HLI)             
4AFF: 08 C7 09        LD      ($09C7),SP          
4B02: 29              ADD     HL,HL               
4B03: 10 A6           ;;STOP    $A6                 
4B05: 18 A6           JR      $4AAD               ; {}
4B07: 19              ADD     HL,DE               
4B08: 16 83           LD      D,$83               
4B0A: 20 21           JR      NZ,$4B2D            ; {}
4B0C: 21 98 23        LD      HL,$2398            
4B0F: 29              ADD     HL,HL               
4B10: C6 29           ADD     $29                 
4B12: 10 30           ;;STOP    $30                 
4B14: DC 40 22        CALL    C,$2240             
4B17: 41              LD      B,C                 
4B18: 2B              DEC     HL                  
4B19: C3 50 03        JP      $0350               
4B1C: C3 51 23        JP      $2351               
4B1F: 35              DEC     (HL)                
4B20: 2C              INC     L                   
4B21: 36 28           LD      (HL),$28            
4B23: C3 45 24        JP      $2445               
4B26: 84              ADD     A,H                 
4B27: 71              LD      (HL),C              
4B28: 22              LD      (HLI),A             
4B29: 71              LD      (HL),C              
4B2A: 27              DAA                         
4B2B: 72              LD      (HL),D              
4B2C: F5              PUSH    AF                  
4B2D: 64              LD      H,H                 
4B2E: 2C              INC     L                   
4B2F: 65              LD      H,L                 
4B30: 28 74           JR      Z,$4BA6             ; {}
4B32: 28 79           JR      Z,$4BAD             ; {}
4B34: 2C              INC     L                   
4B35: 42              LD      B,D                 
4B36: 1D              DEC     E                   
4B37: E1              POP     HL                  
4B38: 06 14           LD      B,$14               
4B3A: 00              NOP                         
4B3B: 00              NOP                         
4B3C: FE 04           CP      $04                 
4B3E: 0D              DEC     C                   
4B3F: 74              LD      (HL),H              
4B40: F1              POP     AF                  
4B41: 84              ADD     A,H                 
4B42: 13              INC     DE                  
4B43: 0F              RRCA                        
4B44: 84              ADD     A,H                 
4B45: 23              INC     HL                  
4B46: 0F              RRCA                        
4B47: 84              ADD     A,H                 
4B48: 33              INC     SP                  
4B49: 0F              RRCA                        
4B4A: 82              ADD     A,D                 
4B4B: 54              LD      D,H                 
4B4C: 0F              RRCA                        
4B4D: 82              ADD     A,D                 
4B4E: 64              LD      H,H                 
4B4F: 0F              RRCA                        
4B50: 02              LD      (BC),A              
4B51: 26 03           LD      H,$03               
4B53: 2A              LD      A,(HLI)             
4B54: 06 29           LD      B,$29               
4B56: 07              RLCA                        
4B57: 25              DEC     H                   
4B58: C3 12 24        JP      $2412               
4B5B: 42              LD      B,D                 
4B5C: 2A              LD      A,(HLI)             
4B5D: 84              ADD     A,H                 
4B5E: 43              LD      B,E                 
4B5F: 21 82 44        LD      HL,$4482            
4B62: 97              SUB     A                   
4B63: 47              LD      B,A                 
4B64: 29              ADD     HL,HL               
4B65: C3 17 23        JP      $2317               
4B68: 13              INC     DE                  
4B69: C0              RET     NZ                  
4B6A: 16 C0           LD      D,$C0               
4B6C: 33              INC     SP                  
4B6D: C0              RET     NZ                  
4B6E: 36 C0           LD      (HL),$C0            
4B70: 11 AC 18        LD      DE,$18AC            
4B73: AC              XOR     H                   
4B74: 60              LD      H,B                 
4B75: 27              DAA                         
4B76: 82              ADD     A,D                 
4B77: 61              LD      H,C                 
4B78: 22              LD      (HLI),A             
4B79: 63              LD      H,E                 
4B7A: 2B              DEC     HL                  
4B7B: 66              LD      H,(HL)              
4B7C: 2C              INC     L                   
4B7D: 82              ADD     A,D                 
4B7E: 67              LD      H,A                 
4B7F: 22              LD      (HLI),A             
4B80: 69              LD      L,C                 
4B81: 28 83           JR      Z,$4B06             ; {}
4B83: 77              LD      (HL),A              
4B84: 03              INC     BC                  
4B85: 82              ADD     A,D                 
4B86: 70              LD      (HL),B              
4B87: 22              LD      (HLI),A             
4B88: 72              LD      (HL),D              
4B89: 2B              DEC     HL                  
4B8A: 73              LD      (HL),E              
4B8B: 27              DAA                         
4B8C: 76              HALT                        
4B8D: 28 E0           JR      Z,$4B6F             ; {}
4B8F: 00              NOP                         
4B90: 0E 58           LD      C,$58               
4B92: 32              LD      (HLD),A             
4B93: FE 04           CP      $04                 
4B95: 5D              LD      E,L                 
4B96: 20 F6           JR      NZ,$4B8E            ; {}
4B98: 59              LD      E,C                 
4B99: F7              RST     0X30                
4B9A: 75              LD      (HL),L              
4B9B: F5              PUSH    AF                  
4B9C: 00              NOP                         
4B9D: AC              XOR     H                   
4B9E: 01 25 02        LD      BC,$0225            
4BA1: F8 04           LD      HL,SP+$04           
4BA3: 26 09           LD      H,$09               
4BA5: 2A              LD      A,(HLI)             
4BA6: 10 03           ;;STOP    $03                 
4BA8: 11 23 C3        LD      DE,$C323            
4BAB: 14              INC     D                   
4BAC: 24              INC     H                   
4BAD: 20 21           JR      NZ,$4BD0            ; {}
4BAF: 21 29 30        LD      HL,$3029            
4BB2: DB                              
4BB3: 34              INC     (HL)                
4BB4: 2A              LD      A,(HLI)             
4BB5: 85              ADD     A,L                 
4BB6: 35              DEC     (HL)                
4BB7: 21 40 2B        LD      HL,$2B40            
4BBA: C2 59 0D        JP      NZ,$0D59            
4BBD: 75              LD      (HL),L              
4BBE: 2B              DEC     HL                  
4BBF: 76              HALT                        
4BC0: 0D              DEC     C                   
4BC1: 77              LD      (HL),A              
4BC2: 2C              INC     L                   
4BC3: 70              LD      (HL),B              
4BC4: 23              INC     HL                  
4BC5: 71              LD      (HL),C              
4BC6: 0D              DEC     C                   
4BC7: 72              LD      (HL),D              
4BC8: 2C              INC     L                   
4BC9: 76              HALT                        
4BCA: DC FE 04        CALL    C,$04FE             
4BCD: 4D              LD      C,L                 
4BCE: 04              INC     B                   
4BCF: F0 50           LD      A,($50)             
4BD1: F6 29           OR      $29                 
4BD3: F7              RST     0X30                
4BD4: 72              LD      (HL),D              
4BD5: F5              PUSH    AF                  
4BD6: 02              LD      (BC),A              
4BD7: 29              ADD     HL,HL               
4BD8: 03              INC     BC                  
4BD9: 25              DEC     H                   
4BDA: C3 13 23        JP      $2313               
4BDD: 83              ADD     A,E                 
4BDE: 30 21           JR      NC,$4C01            ; {}
4BE0: 33              INC     SP                  
4BE1: 29              ADD     HL,HL               
4BE2: C2 50 0D        JP      NZ,$0D50            
4BE5: 72              LD      (HL),D              
4BE6: 2B              DEC     HL                  
4BE7: 73              LD      (HL),E              
4BE8: 0D              DEC     C                   
4BE9: 74              LD      (HL),H              
4BEA: 2C              INC     L                   
4BEB: 82              ADD     A,D                 
4BEC: 34              INC     (HL)                
4BED: A6              AND     (HL)                
4BEE: 36 A7           LD      (HL),$A7            
4BF0: C3 17 A7        JP      $A717               
4BF3: 01 A8 E2        LD      BC,$E2A8            
4BF6: 06 F8           LD      B,$F8               
4BF8: 48              LD      C,B                 
4BF9: 50              LD      D,B                 
4BFA: FE 04           CP      $04                 
4BFC: 0D              DEC     C                   
4BFD: FE 06           CP      $06                 
4BFF: 0D              DEC     C                   
4C00: 74              LD      (HL),H              
4C01: F1              POP     AF                  
4C02: 84              ADD     A,H                 
4C03: 13              INC     DE                  
4C04: 0F              RRCA                        
4C05: 84              ADD     A,H                 
4C06: 23              INC     HL                  
4C07: 0F              RRCA                        
4C08: 84              ADD     A,H                 
4C09: 33              INC     SP                  
4C0A: 0F              RRCA                        
4C0B: 82              ADD     A,D                 
4C0C: 54              LD      D,H                 
4C0D: 0F              RRCA                        
4C0E: 82              ADD     A,D                 
4C0F: 64              LD      H,H                 
4C10: 0F              RRCA                        
4C11: 02              LD      (BC),A              
4C12: 26 03           LD      H,$03               
4C14: 2A              LD      A,(HLI)             
4C15: 06 29           LD      B,$29               
4C17: 07              RLCA                        
4C18: 25              DEC     H                   
4C19: C3 12 24        JP      $2412               
4C1C: 42              LD      B,D                 
4C1D: 2A              LD      A,(HLI)             
4C1E: 84              ADD     A,H                 
4C1F: 43              LD      B,E                 
4C20: 21 82 44        LD      HL,$4482            
4C23: 97              SUB     A                   
4C24: 47              LD      B,A                 
4C25: 29              ADD     HL,HL               
4C26: C3 17 23        JP      $2317               
4C29: 13              INC     DE                  
4C2A: C0              RET     NZ                  
4C2B: 16 C0           LD      D,$C0               
4C2D: 33              INC     SP                  
4C2E: C0              RET     NZ                  
4C2F: 36 C0           LD      (HL),$C0            
4C31: 11 AC 18        LD      DE,$18AC            
4C34: AC              XOR     H                   
4C35: 61              LD      H,C                 
4C36: AC              XOR     H                   
4C37: 68              LD      L,B                 
4C38: AC              XOR     H                   
4C39: E0 00           LD      ($FF00+$00),A       
4C3B: 10 58           ;;STOP    $58                 
4C3D: 10 FE           ;;STOP    $FE                 
4C3F: 06 93           LD      B,$93               
4C41: 76              HALT                        
4C42: F5              PUSH    AF                  
4C43: 05              DEC     B                   
4C44: 25              DEC     H                   
4C45: 82              ADD     A,D                 
4C46: 06 21           LD      B,$21               
4C48: 08 26 C7        LD      ($C726),SP          
4C4B: 15              DEC     D                   
4C4C: 23              INC     HL                  
4C4D: C7              RST     0X00                
4C4E: 16 0D           LD      D,$0D               
4C50: C7              RST     0X00                
4C51: 17              RLA                         
4C52: 0D              DEC     C                   
4C53: C7              RST     0X00                
4C54: 18 24           JR      $4C7A               ; {}
4C56: 17              RLA                         
4C57: CB E2           SET     1,E                 
4C59: 07              RLCA                        
4C5A: 66              LD      H,(HL)              
4C5B: 18 80           JR      $4BDD               ; {}
4C5D: FE 06           CP      $06                 
4C5F: 0D              DEC     C                   
4C60: 71              LD      (HL),C              
4C61: F5              PUSH    AF                  
4C62: 86              ADD     A,(HL)              
4C63: 22              LD      (HLI),A             
4C64: AF              XOR     A                   
4C65: 86              ADD     A,(HL)              
4C66: 32              LD      (HLD),A             
4C67: 01 86 42        LD      BC,$4286            
4C6A: 01 86 52        LD      BC,$5286            
4C6D: 01 85 63        LD      BC,$6385            
4C70: B0              OR      B                   
4C71: 23              INC     HL                  
4C72: AE              XOR     (HL)                
4C73: 26 AE           LD      H,$AE               
4C75: 33              INC     SP                  
4C76: 0D              DEC     C                   
4C77: 36 0D           LD      (HL),$0D            
4C79: 43              LD      B,E                 
4C7A: AF              XOR     A                   
4C7B: 46              LD      B,(HL)              
4C7C: AF              XOR     A                   
4C7D: 68              LD      L,B                 
4C7E: AE              XOR     (HL)                
4C7F: 33              INC     SP                  
4C80: AC              XOR     H                   
4C81: 36 AC           LD      (HL),$AC            
4C83: 52              LD      D,D                 
4C84: 0D              DEC     C                   
4C85: 42              LD      B,D                 
4C86: B0              OR      B                   
4C87: 28 A1           JR      Z,$4C2A             ; {}
4C89: FE 06           CP      $06                 
4C8B: 0D              DEC     C                   
4C8C: 04              INC     B                   
4C8D: F0 74           LD      A,($74)             
4C8F: F1              POP     AF                  
4C90: 12              LD      (DE),A              
4C91: 06 17           LD      B,$17               
4C93: 06 86           LD      B,$86               
4C95: 22              LD      (HLI),A             
4C96: 06 86           LD      B,$86               
4C98: 32              LD      (HLD),A             
4C99: 06 86           LD      B,$86               
4C9B: 42              LD      B,D                 
4C9C: 06 86           LD      B,$86               
4C9E: 52              LD      D,D                 
4C9F: 06 C5           LD      B,$C5               
4CA1: 11 06 FE        LD      DE,$FE06            
4CA4: 06 3D           LD      B,$3D               
4CA6: 06 F4           LD      B,$F4               
4CA8: 71              LD      (HL),C              
4CA9: F5              PUSH    AF                  
4CAA: 02              LD      (BC),A              
4CAB: 26 03           LD      H,$03               
4CAD: 12              LD      (DE),A              
4CAE: 04              INC     B                   
4CAF: 25              DEC     H                   
4CB0: C7              RST     0X00                
4CB1: 11 06 C2        LD      DE,$C206            
4CB4: 12              LD      (DE),A              
4CB5: 24              INC     H                   
4CB6: 13              INC     DE                  
4CB7: A0              AND     B                   
4CB8: C7              RST     0X00                
4CB9: 14              INC     D                   
4CBA: 23              INC     HL                  
4CBB: 32              LD      (HLD),A             
4CBC: 2A              LD      A,(HLI)             
4CBD: 33              INC     SP                  
4CBE: 21 34 29        LD      HL,$2934            
4CC1: 83              ADD     A,E                 
4CC2: 42              LD      B,D                 
4CC3: 06 52           LD      B,$52               
4CC5: 2C              INC     L                   
4CC6: 53              LD      D,E                 
4CC7: 22              LD      (HLI),A             
4CC8: 54              LD      D,H                 
4CC9: 2B              DEC     HL                  
4CCA: C2 62 24        JP      NZ,$2462            
4CCD: C2 64 23        JP      NZ,$2364            
4CD0: 74              LD      (HL),H              
4CD1: 27              DAA                         
4CD2: 84              ADD     A,H                 
4CD3: 75              LD      (HL),L              
4CD4: 22              LD      (HLI),A             
4CD5: 79              LD      A,C                 
4CD6: 28 C2           JR      Z,$4C9A             ; {}
4CD8: 61              LD      H,C                 
4CD9: 0D              DEC     C                   
4CDA: 05              DEC     B                   
4CDB: 29              ADD     HL,HL               
4CDC: 82              ADD     A,D                 
4CDD: 06 0D           LD      B,$0D               
4CDF: 08 2A FE        LD      ($FE2A),SP          
4CE2: 04              INC     B                   
4CE3: 0D              DEC     C                   
4CE4: 85              ADD     A,L                 
4CE5: 71              LD      (HL),C              
4CE6: 0D              DEC     C                   
4CE7: 00              NOP                         
4CE8: C0              RET     NZ                  
4CE9: 01 25 08        LD      BC,$0825            
4CEC: 26 09           LD      H,$09               
4CEE: C0              RET     NZ                  
4CEF: 10 25           ;;STOP    $25                 
4CF1: 11 29 86        LD      DE,$8629            
4CF4: 12              LD      (DE),A              
4CF5: 0F              RRCA                        
4CF6: 18 2A           JR      $4D22               ; {}
4CF8: 19              ADD     HL,DE               
4CF9: 21 20 29        LD      HL,$2920            
4CFC: 84              ADD     A,H                 
4CFD: 21 0F 25        LD      HL,$250F            
4D00: 25              DEC     H                   
4D01: 26 C7           LD      H,$C7               
4D03: 27              DAA                         
4D04: 98              SBC     B                   
4D05: 28 C7           JR      Z,$4CCE             ; {}
4D07: 29              ADD     HL,HL               
4D08: 26 30           LD      H,$30               
4D0A: 25              DEC     H                   
4D0B: 84              ADD     A,H                 
4D0C: 31 21 35        LD      SP,$3521            
4D0F: 29              ADD     HL,HL               
4D10: 45              LD      B,L                 
4D11: A6              AND     (HL)                
4D12: 54              LD      D,H                 
4D13: A6              AND     (HL)                
4D14: 49              LD      C,C                 
4D15: 2A              LD      A,(HLI)             
4D16: 50              LD      D,B                 
4D17: 29              ADD     HL,HL               
4D18: 83              ADD     A,E                 
4D19: 46              LD      B,(HL)              
4D1A: DC 55 25        CALL    C,$2555             
4D1D: 56              LD      D,(HL)              
4D1E: C7              RST     0X00                
4D1F: 57              LD      D,A                 
4D20: 98              SBC     B                   
4D21: 58              LD      E,B                 
4D22: C7              RST     0X00                
4D23: 59              LD      E,C                 
4D24: 26 60           LD      H,$60               
4D26: 25              DEC     H                   
4D27: 82              ADD     A,D                 
4D28: 61              LD      H,C                 
4D29: 21 63 26        LD      HL,$2663            
4D2C: 65              LD      H,L                 
4D2D: 23              INC     HL                  
4D2E: 70              LD      (HL),B              
4D2F: 23              INC     HL                  
4D30: 73              LD      (HL),E              
4D31: 24              INC     H                   
4D32: 75              LD      (HL),L              
4D33: 27              DAA                         
4D34: 76              HALT                        
4D35: F5              PUSH    AF                  
4D36: 13              INC     DE                  
4D37: A0              AND     B                   
4D38: 42              LD      B,D                 
4D39: BE              CP      (HL)                
4D3A: E2              LD      (C),A               
4D3B: 07              RLCA                        
4D3C: 65              LD      H,L                 
4D3D: 88              ADC     A,B                 
4D3E: 10 FE           ;;STOP    $FE                 
4D40: 06 06           LD      B,$06               
4D42: 01 F0 59        LD      BC,$59F0            
4D45: F3              DI                          
4D46: 88              ADC     A,B                 
4D47: 11 0D C4        LD      DE,$C40D            
4D4A: 21 0D C4        LD      HL,$C40D            
4D4D: 28 0D           JR      Z,$4D5C             ; {}
4D4F: 88              ADC     A,B                 
4D50: 61              LD      H,C                 
4D51: 0D              DEC     C                   
4D52: 16 06           LD      D,$06               
4D54: 63              LD      H,E                 
4D55: 06 FE           LD      B,$FE               
4D57: 06 2D           LD      B,$2D               
4D59: 50              LD      D,B                 
4D5A: EE C2           XOR     $C2                 
4D5C: 00              NOP                         
4D5D: 24              INC     H                   
4D5E: 01 17 83        LD      BC,$8317            
4D61: 02              LD      (BC),A              
4D62: 12              LD      (DE),A              
4D63: 05              DEC     B                   
4D64: 16 06           LD      D,$06               
4D66: 25              DEC     H                   
4D67: 11 11 15        LD      DE,$1511            
4D6A: 10 16           ;;STOP    $16                 
4D6C: 23              INC     HL                  
4D6D: 20 2A           JR      NZ,$4D99            ; {}
4D6F: 85              ADD     A,L                 
4D70: 21 21 22        LD      HL,$2221            
4D73: 98              SBC     B                   
4D74: 26 29           LD      H,$29               
4D76: 27              DAA                         
4D77: 25              DEC     H                   
4D78: 28 98           JR      Z,$4D12             ; {}
4D7A: 29              ADD     HL,HL               
4D7B: 26 30           LD      H,$30               
4D7D: C0              RET     NZ                  
4D7E: 86              ADD     A,(HL)              
4D7F: 31 0F C3        LD      SP,$C30F            
4D82: 37              SCF                         
4D83: 23              INC     HL                  
4D84: C3 39 24        JP      $2439               
4D87: 40              LD      B,B                 
4D88: 25              DEC     H                   
4D89: 41              LD      B,C                 
4D8A: 98              SBC     B                   
4D8B: 42              LD      B,D                 
4D8C: 21 43 26        LD      HL,$2643            
4D8F: 44              LD      B,H                 
4D90: 2C              INC     L                   
4D91: 45              LD      B,L                 
4D92: 22              LD      (HLI),A             
4D93: 46              LD      B,(HL)              
4D94: 2B              DEC     HL                  
4D95: 49              LD      C,C                 
4D96: F3              DI                          
4D97: C2 53 24        JP      NZ,$2453            
4D9A: C3 54 24        JP      $2454               
4D9D: C3 55 03        JP      $0355               
4DA0: C2 56 23        JP      NZ,$2356            
4DA3: 67              LD      H,A                 
4DA4: 27              DAA                         
4DA5: 68              LD      L,B                 
4DA6: 22              LD      (HLI),A             
4DA7: 69              LD      L,C                 
4DA8: 28 73           JR      Z,$4E1D             ; {}
4DAA: 28 76           JR      Z,$4E22             ; {}
4DAC: 27              DAA                         
4DAD: 79              LD      A,C                 
4DAE: 2B              DEC     HL                  
4DAF: 14              INC     D                   
4DB0: CB E2           SET     1,E                 
4DB2: 07              RLCA                        
4DB3: 60              LD      H,B                 
4DB4: 18 80           JR      $4D36               ; {}
4DB6: FE 06           CP      $06                 
4DB8: 2D              DEC     L                   
4DB9: 40              LD      B,B                 
4DBA: F2                              
4DBB: 29              ADD     HL,HL               
4DBC: F7              RST     0X30                
4DBD: 71              LD      (HL),C              
4DBE: F5              PUSH    AF                  
4DBF: 00              NOP                         
4DC0: 21 02 29        LD      HL,$2902            
4DC3: 03              INC     BC                  
4DC4: 25              DEC     H                   
4DC5: 06 26           LD      B,$26               
4DC7: 07              RLCA                        
4DC8: 17              RLA                         
4DC9: 08 12 09        LD      ($0912),SP          
4DCC: 16 83           LD      D,$83               
4DCE: 10 0D           ;;STOP    $0D                 
4DD0: 13              INC     DE                  
4DD1: 23              INC     HL                  
4DD2: C2 16 24        JP      NZ,$2416            
4DD5: 19              ADD     HL,DE               
4DD6: 10 20           ;;STOP    $20                 
4DD8: 25              DEC     H                   
4DD9: 82              ADD     A,D                 
4DDA: 21 21 23        LD      HL,$2321            
4DDD: 29              ADD     HL,HL               
4DDE: 29              ADD     HL,HL               
4DDF: 14              INC     D                   
4DE0: 36 2A           LD      (HL),$2A            
4DE2: 83              ADD     A,E                 
4DE3: 37              SCF                         
4DE4: 21 82 68        LD      HL,$6882            
4DE7: 06 70           LD      B,$70               
4DE9: 23              INC     HL                  
4DEA: 71              LD      (HL),C              
4DEB: 0D              DEC     C                   
4DEC: 72              LD      (HL),D              
4DED: 2C              INC     L                   
4DEE: 73              LD      (HL),E              
4DEF: 2B              DEC     HL                  
4DF0: 74              LD      (HL),H              
4DF1: 06 75           LD      B,$75               
4DF3: 2C              INC     L                   
4DF4: 77              LD      (HL),A              
4DF5: 2B              DEC     HL                  
4DF6: 78              LD      A,B                 
4DF7: 06 79           LD      B,$79               
4DF9: 2C              INC     L                   
4DFA: 86              ADD     A,(HL)              
4DFB: 62              LD      H,D                 
4DFC: 20 64           JR      NZ,$4E62            ; {}
4DFE: 0D              DEC     C                   
4DFF: 18 A0           JR      $4DA1               ; {}
4E01: 05              DEC     B                   
4E02: A8              XOR     B                   
4E03: E0 00           LD      ($FF00+$00),A       
4E05: 00              NOP                         
4E06: 48              LD      C,B                 
4E07: 50              LD      D,B                 
4E08: FE 06           CP      $06                 
4E0A: 06 39           LD      B,$39               
4E0C: EF              RST     0X28                
4E0D: 04              INC     B                   
4E0E: F8 C3           LD      HL,SP+$C3           
4E10: 14              INC     D                   
4E11: 11 C3 15        LD      DE,$15C3            
4E14: 10 30           ;;STOP    $30                 
4E16: 29              ADD     HL,HL               
4E17: 21 12 22        LD      HL,$2212            
4E1A: AC              XOR     H                   
4E1B: 27              DAA                         
4E1C: AC              XOR     H                   
4E1D: 28 12           JR      Z,$4E31             ; {}
4E1F: C2 40 0D        JP      NZ,$0D40            
4E22: C3 32 10        JP      $1032               
4E25: C3 37 11        JP      $1137               
4E28: 44              LD      B,H                 
4E29: 15              DEC     D                   
4E2A: 45              LD      B,L                 
4E2B: 14              INC     D                   
4E2C: 59              LD      E,C                 
4E2D: 2A              LD      A,(HLI)             
4E2E: 60              LD      H,B                 
4E2F: 06 62           LD      B,$62               
4E31: 94              SUB     H                   
4E32: 84              ADD     A,H                 
4E33: 63              LD      H,E                 
4E34: 12              LD      (DE),A              
4E35: 67              LD      H,A                 
4E36: 93              SUB     E                   
4E37: 69              LD      L,C                 
4E38: 06 70           LD      B,$70               
4E3A: 22              LD      (HLI),A             
4E3B: 79              LD      A,C                 
4E3C: 22              LD      (HLI),A             
4E3D: C4 31 0D        CALL    NZ,$0D31            
4E40: C4 38 0D        CALL    NZ,$0D38            
4E43: 35              DEC     (HL)                
4E44: CB E2           SET     1,E                 
4E46: 07              RLCA                        
4E47: 62              LD      H,D                 
4E48: 18 80           JR      $4DCA               ; {}
4E4A: FE 06           CP      $06                 
4E4C: 1D              DEC     E                   
4E4D: 01 F4 30        LD      BC,$30F4            
4E50: EE 39           XOR     $39                 
4E52: EF              RST     0X28                
4E53: C3 01 06        JP      $0601               
4E56: C2 02 24        JP      NZ,$2402            
4E59: C2 04 23        JP      NZ,$2304            
4E5C: 04              INC     B                   
4E5D: 25              DEC     H                   
4E5E: 84              ADD     A,H                 
4E5F: 05              DEC     B                   
4E60: 21 09 26        LD      HL,$2609            
4E63: 22              LD      (HLI),A             
4E64: 2A              LD      A,(HLI)             
4E65: 23              INC     HL                  
4E66: 98              SBC     B                   
4E67: 24              INC     H                   
4E68: 29              ADD     HL,HL               
4E69: 39              ADD     HL,SP               
4E6A: 0D              DEC     C                   
4E6B: 49              LD      C,C                 
4E6C: 2C              INC     L                   
4E6D: 50              LD      D,B                 
4E6E: 29              ADD     HL,HL               
4E6F: 70              LD      (HL),B              
4E70: 22              LD      (HLI),A             
4E71: C5              PUSH    BC                  
4E72: 01 0D C2        LD      BC,$C20D            
4E75: 15              DEC     D                   
4E76: 0D              DEC     C                   
4E77: 82              ADD     A,D                 
4E78: 27              DAA                         
4E79: 0D              DEC     C                   
4E7A: 86              ADD     A,(HL)              
4E7B: 33              INC     SP                  
4E7C: 0D              DEC     C                   
4E7D: 82              ADD     A,D                 
4E7E: 43              LD      B,E                 
4E7F: 0D              DEC     C                   
4E80: 51              LD      D,C                 
4E81: 06 53           LD      B,$53               
4E83: 0D              DEC     C                   
4E84: C3 32 06        JP      $0632               
4E87: 16 06           LD      D,$06               
4E89: C2 26 06        JP      NZ,$0626            
4E8C: 84              ADD     A,H                 
4E8D: 45              LD      B,L                 
4E8E: 06 85           LD      B,$85               
4E90: 54              LD      D,H                 
4E91: 06 89           LD      B,$89               
4E93: 60              LD      H,B                 
4E94: 06 08           LD      B,$08               
4E96: 26 09           LD      H,$09               
4E98: C0              RET     NZ                  
4E99: 18 24           JR      $4EBF               ; {}
4E9B: 19              ADD     HL,DE               
4E9C: 13              INC     DE                  
4E9D: 28 2A           JR      Z,$4EC9             ; {}
4E9F: 29              ADD     HL,HL               
4EA0: 21 FE 06        LD      HL,$06FE            
4EA3: 2D              DEC     L                   
4EA4: 05              DEC     B                   
4EA5: A3              AND     E                   
4EA6: 10 F6           ;;STOP    $F6                 
4EA8: 19              ADD     HL,DE               
4EA9: F7              RST     0X30                
4EAA: 00              NOP                         
4EAB: 2A              LD      A,(HLI)             
4EAC: 09              ADD     HL,BC               
4EAD: 29              ADD     HL,HL               
4EAE: 87              ADD     A,A                 
4EAF: 10 13           ;;STOP    $13                 
4EB1: 17              RLA                         
4EB2: 95              SUB     L                   
4EB3: 19              ADD     HL,DE               
4EB4: 0D              DEC     C                   
4EB5: 86              ADD     A,(HL)              
4EB6: 20 21           JR      NZ,$4ED9            ; {}
4EB8: 26 26           LD      H,$26               
4EBA: C2 27 11        JP      NZ,$1127            
4EBD: 29              ADD     HL,HL               
4EBE: 2C              INC     L                   
4EBF: 30 0D           JR      NC,$4ECE            ; {}
4EC1: C2 36 24        JP      NZ,$2436            
4EC4: 47              LD      B,A                 
4EC5: 15              DEC     D                   
4EC6: 39              ADD     HL,SP               
4EC7: 24              INC     H                   
4EC8: 40              LD      B,B                 
4EC9: 2B              DEC     HL                  
4ECA: 56              LD      D,(HL)              
4ECB: 2A              LD      A,(HLI)             
4ECC: 82              ADD     A,D                 
4ECD: 57              LD      D,A                 
4ECE: 21 49 2A        LD      HL,$2A49            
4ED1: 59              LD      E,C                 
4ED2: 21 48 13        LD      HL,$1348            
4ED5: 28 A1           JR      Z,$4E78             ; {}
4ED7: E0 00           LD      ($FF00+$00),A       
4ED9: 02              LD      (BC),A              
4EDA: 38 50           JR      C,$4F2C             ; {}
4EDC: FE 06           CP      $06                 
4EDE: 4D              LD      C,L                 
4EDF: 10 F6           ;;STOP    $F6                 
4EE1: 74              LD      (HL),H              
4EE2: F1              POP     AF                  
4EE3: 87              ADD     A,A                 
4EE4: 12              LD      (DE),A              
4EE5: DF              RST     0X18                
4EE6: 87              ADD     A,A                 
4EE7: 22              LD      (HLI),A             
4EE8: DF              RST     0X18                
4EE9: 87              ADD     A,A                 
4EEA: 32              LD      (HLD),A             
4EEB: DF              RST     0X18                
4EEC: 87              ADD     A,A                 
4EED: 42              LD      B,D                 
4EEE: DF              RST     0X18                
4EEF: 82              ADD     A,D                 
4EF0: 57              LD      D,A                 
4EF1: DF              RST     0X18                
4EF2: 83              ADD     A,E                 
4EF3: 61              LD      H,C                 
4EF4: DF              RST     0X18                
4EF5: 83              ADD     A,E                 
4EF6: 66              LD      H,(HL)              
4EF7: DF              RST     0X18                
4EF8: 00              NOP                         
4EF9: C0              RET     NZ                  
4EFA: 01 25 10        LD      BC,$1025            
4EFD: 0D              DEC     C                   
4EFE: C4 11 23        CALL    NZ,$2311            
4F01: 20 2B           JR      NZ,$4F2E            ; {}
4F03: 30 23           JR      NC,$4F28            ; {}
4F05: 40              LD      B,B                 
4F06: 29              ADD     HL,HL               
4F07: 50              LD      D,B                 
4F08: 21 51 29        LD      HL,$2951            
4F0B: 85              ADD     A,L                 
4F0C: 52              LD      D,D                 
4F0D: A6              AND     (HL)                
4F0E: FE 04           CP      $04                 
4F10: 0D              DEC     C                   
4F11: 00              NOP                         
4F12: 23              INC     HL                  
4F13: 82              ADD     A,D                 
4F14: 01 0D 03        LD      BC,$030D            
4F17: 2A              LD      A,(HLI)             
4F18: 05              DEC     B                   
4F19: C7              RST     0X00                
4F1A: 06 F0           LD      B,$F0               
4F1C: 08 C7 E1        LD      ($E1C7),SP          
4F1F: 07              RLCA                        
4F20: 5D              LD      E,L                 
4F21: 50              LD      D,B                 
4F22: 50              LD      D,B                 
4F23: FE 06           CP      $06                 
4F25: 0D              DEC     C                   
4F26: 19              ADD     HL,DE               
4F27: F7              RST     0X30                
4F28: 70              LD      (HL),B              
4F29: F5              PUSH    AF                  
4F2A: 00              NOP                         
4F2B: 17              RLA                         
4F2C: 83              ADD     A,E                 
4F2D: 01 12 04        LD      BC,$0412            
4F30: 2A              LD      A,(HLI)             
4F31: 84              ADD     A,H                 
4F32: 05              DEC     B                   
4F33: 21 09 29        LD      HL,$2909            
4F36: C7              RST     0X00                
4F37: 10 11           ;;STOP    $11                 
4F39: C7              RST     0X00                
4F3A: 11 10 12        LD      DE,$1210            
4F3D: 25              DEC     H                   
4F3E: 13              INC     DE                  
4F3F: 98              SBC     B                   
4F40: 85              ADD     A,L                 
4F41: 14              INC     D                   
4F42: 21 19 26        LD      HL,$2619            
4F45: C5              PUSH    BC                  
4F46: 22              LD      (HLI),A             
4F47: 23              INC     HL                  
4F48: 24              INC     H                   
4F49: A6              AND     (HL)                
4F4A: 27              DAA                         
4F4B: A6              AND     (HL)                
4F4C: 36 A0           LD      (HL),$A0            
4F4E: 43              LD      B,E                 
4F4F: AF              XOR     A                   
4F50: 82              ADD     A,D                 
4F51: 45              LD      B,L                 
4F52: A7              AND     A                   
4F53: 48              LD      C,B                 
4F54: AF              XOR     A                   
4F55: 53              LD      D,E                 
4F56: B0              OR      B                   
4F57: 58              LD      E,B                 
4F58: 01 68 B0        LD      BC,$B068            
4F5B: 72              LD      (HL),D              
4F5C: 27              DAA                         
4F5D: 19              ADD     HL,DE               
4F5E: 21 29 0D        LD      HL,$0D29            
4F61: 39              ADD     HL,SP               
4F62: 2C              INC     L                   
4F63: FE 06           CP      $06                 
4F65: 0D              DEC     C                   
4F66: 39              ADD     HL,SP               
4F67: 4A              LD      C,D                 
4F68: 01 F4 10        LD      BC,$10F4            
4F6B: F6 71           OR      $71                 
4F6D: F5              PUSH    AF                  
4F6E: 70              LD      (HL),B              
4F6F: 23              INC     HL                  
4F70: 71              LD      (HL),C              
4F71: 0D              DEC     C                   
4F72: 72              LD      (HL),D              
4F73: 2C              INC     L                   
4F74: 00              NOP                         
4F75: 23              INC     HL                  
4F76: 01 0D 02        LD      BC,$020D            
4F79: 2A              LD      A,(HLI)             
4F7A: 03              INC     BC                  
4F7B: 29              ADD     HL,HL               
4F7C: 04              INC     B                   
4F7D: 06 05           LD      B,$05               
4F7F: 2A              LD      A,(HLI)             
4F80: 07              RLCA                        
4F81: 29              ADD     HL,HL               
4F82: C8              RET     Z                   
4F83: 08 06 09        LD      ($0906),SP          
4F86: 24              INC     H                   
4F87: 12              LD      (DE),A              
4F88: 10 83           ;;STOP    $83                 
4F8A: 13              INC     DE                  
4F8B: 06 14           LD      B,$14               
4F8D: C0              RET     NZ                  
4F8E: 16 11           LD      D,$11               
4F90: 22              LD      (HLI),A             
4F91: 94              SUB     H                   
4F92: 23              INC     HL                  
4F93: 16 24           LD      D,$24               
4F95: 06 25           LD      B,$25               
4F97: 17              RLA                         
4F98: 26 93           LD      H,$93               
4F9A: C4 34 0F        CALL    NZ,$0F34            
4F9D: 85              ADD     A,L                 
4F9E: 42              LD      B,D                 
4F9F: A6              AND     (HL)                
4FA0: 44              LD      B,H                 
4FA1: 0F              RRCA                        
4FA2: 77              LD      (HL),A              
4FA3: 2B              DEC     HL                  
4FA4: 79              LD      A,C                 
4FA5: 24              INC     H                   
4FA6: 10 29           ;;STOP    $29                 
4FA8: 20 0D           JR      NZ,$4FB7            ; {}
4FAA: 30 2B           JR      NC,$4FD7            ; {}
4FAC: 32              LD      (HLD),A             
4FAD: 0F              RRCA                        
4FAE: FE 06           CP      $06                 
4FB0: 0D              DEC     C                   
4FB1: 30 41           JR      NC,$4FF4            ; {}
4FB3: 39              ADD     HL,SP               
4FB4: F3              DI                          
4FB5: 74              LD      (HL),H              
4FB6: 40              LD      B,B                 
4FB7: 06 26           LD      B,$26               
4FB9: 83              ADD     A,E                 
4FBA: 07              RLCA                        
4FBB: A6              AND     (HL)                
4FBC: 25              DEC     H                   
4FBD: AB              XOR     E                   
4FBE: 16 24           LD      D,$24               
4FC0: 18 DE           JR      $4FA0               ; {}
4FC2: 19              ADD     HL,DE               
4FC3: 0D              DEC     C                   
4FC4: 23              INC     HL                  
4FC5: AE              XOR     (HL)                
4FC6: 26 2A           LD      H,$2A               
4FC8: 27              DAA                         
4FC9: 98              SBC     B                   
4FCA: 28 21           JR      Z,$4FED             ; {}
4FCC: 29              ADD     HL,HL               
4FCD: 26 33           LD      H,$33               
4FCF: A6              AND     (HL)                
4FD0: 45              LD      B,L                 
4FD1: AE              XOR     (HL)                
4FD2: 47              LD      B,A                 
4FD3: A6              AND     (HL)                
4FD4: 52              LD      D,D                 
4FD5: AE              XOR     (HL)                
4FD6: 58              LD      E,B                 
4FD7: AE              XOR     (HL)                
4FD8: 61              LD      H,C                 
4FD9: AB              XOR     E                   
4FDA: 65              LD      H,L                 
4FDB: A6              AND     (HL)                
4FDC: 67              LD      H,A                 
4FDD: AE              XOR     (HL)                
4FDE: FE 06           CP      $06                 
4FE0: 07              RLCA                        
4FE1: 30 F2           JR      NC,$4FD5            ; {}
4FE3: 59              LD      E,C                 
4FE4: F7              RST     0X30                
4FE5: 71              LD      (HL),C              
4FE6: 40              LD      B,B                 
4FE7: 8A              ADC     A,D                 
4FE8: 00              NOP                         
4FE9: 0D              DEC     C                   
4FEA: 8A              ADC     A,D                 
4FEB: 10 0D           ;;STOP    $0D                 
4FED: 00              NOP                         
4FEE: A6              AND     (HL)                
4FEF: 88              ADC     A,B                 
4FF0: 01 12 82        LD      BC,$8212            
4FF3: 04              INC     B                   
4FF4: A6              AND     (HL)                
4FF5: C2 09 A6        JP      NZ,$A609            
4FF8: 12              LD      (DE),A              
4FF9: AB              XOR     E                   
4FFA: 17              RLA                         
4FFB: AB              XOR     E                   
4FFC: 20 25           JR      NZ,$5023            ; {}
4FFE: 88              ADC     A,B                 
4FFF: 21 21 22        LD      HL,$2221            
5002: 98              SBC     B                   
5003: 27              DAA                         
5004: 98              SBC     B                   
5005: 29              ADD     HL,HL               
5006: 26 42           LD      H,$42               
5008: 2C              INC     L                   
5009: 83              ADD     A,E                 
500A: 43              LD      B,E                 
500B: 22              LD      (HLI),A             
500C: 46              LD      B,(HL)              
500D: 2B              DEC     HL                  
500E: 59              LD      E,C                 
500F: 2A              LD      A,(HLI)             
5010: C2 52 24        JP      NZ,$2452            
5013: 83              ADD     A,E                 
5014: 53              LD      D,E                 
5015: 0D              DEC     C                   
5016: 54              LD      D,H                 
5017: DE C2           SBC     $C2                 
5019: 56              LD      D,(HL)              
501A: 23              INC     HL                  
501B: 83              ADD     A,E                 
501C: 63              LD      H,E                 
501D: A6              AND     (HL)                
501E: 69              LD      L,C                 
501F: 0D              DEC     C                   
5020: 72              LD      (HL),D              
5021: 28 83           JR      Z,$4FA6             ; {}
5023: 73              LD      (HL),E              
5024: A6              AND     (HL)                
5025: 76              HALT                        
5026: 27              DAA                         
5027: 79              LD      A,C                 
5028: 22              LD      (HLI),A             
5029: 64              LD      H,H                 
502A: BE              CP      (HL)                
502B: E2              LD      (C),A               
502C: 07              RLCA                        
502D: 64              LD      H,H                 
502E: 18 10           JR      $5040               ; {}
5030: FE 06           CP      $06                 
5032: 07              RLCA                        
5033: 50              LD      D,B                 
5034: F6 49           OR      $49                 
5036: 42              LD      B,D                 
5037: 14              INC     D                   
5038: AF              XOR     A                   
5039: C4 24 01        CALL    NZ,$0124            
503C: 32              LD      (HLD),A             
503D: AB              XOR     E                   
503E: C4 33 A6        CALL    NZ,$A633            
5041: 35              DEC     (HL)                
5042: AE              XOR     (HL)                
5043: 37              SCF                         
5044: AB              XOR     E                   
5045: 50              LD      D,B                 
5046: 29              ADD     HL,HL               
5047: 60              LD      H,B                 
5048: 0D              DEC     C                   
5049: 61              LD      H,C                 
504A: DE 64           SBC     $64                 
504C: B0              OR      B                   
504D: 65              LD      H,L                 
504E: AE              XOR     (HL)                
504F: 70              LD      (HL),B              
5050: 22              LD      (HLI),A             
5051: FE 06           CP      $06                 
5053: 0F              RRCA                        
5054: 04              INC     B                   
5055: F0 40           LD      A,($40)             
5057: 49              LD      C,C                 
5058: 74              LD      (HL),H              
5059: FB              EI                          
505A: C3 13 0D        JP      $0D13               
505D: C2 22 A9        JP      NZ,$A922            
5060: C2 31 A9        JP      NZ,$A931            
5063: 83              ADD     A,E                 
5064: 33              INC     SP                  
5065: 0D              DEC     C                   
5066: 34              INC     (HL)                
5067: A9              XOR     C                   
5068: 83              ADD     A,E                 
5069: 36 A9           LD      (HL),$A9            
506B: 42              LD      B,D                 
506C: 0D              DEC     C                   
506D: 83              ADD     A,E                 
506E: 43              LD      B,E                 
506F: A9              XOR     C                   
5070: 82              ADD     A,D                 
5071: 46              LD      B,(HL)              
5072: 0D              DEC     C                   
5073: 48              LD      C,B                 
5074: A9              XOR     C                   
5075: 82              ADD     A,D                 
5076: 52              LD      D,D                 
5077: 0D              DEC     C                   
5078: 63              LD      H,E                 
5079: 0D              DEC     C                   
507A: C2 38 0D        JP      NZ,$0D38            
507D: 47              LD      B,A                 
507E: A9              XOR     C                   
507F: 41              LD      B,C                 
5080: 0D              DEC     C                   
5081: FE 04           CP      $04                 
5083: 0D              DEC     C                   
5084: 00              NOP                         
5085: F4                              
5086: 74              LD      (HL),H              
5087: F5              PUSH    AF                  
5088: 00              NOP                         
5089: 11 01 94        LD      DE,$9401            
508C: 83              ADD     A,E                 
508D: 02              LD      (BC),A              
508E: 12              LD      (DE),A              
508F: 05              DEC     B                   
5090: 16 06           LD      D,$06               
5092: 25              DEC     H                   
5093: 10 15           ;;STOP    $15                 
5095: 16 23           LD      D,$23               
5097: 20 25           JR      NZ,$50BE            ; {}
5099: 85              ADD     A,L                 
509A: 21 21 26        LD      HL,$2621            
509D: 29              ADD     HL,HL               
509E: 88              ADC     A,B                 
509F: 41              LD      B,C                 
50A0: 13              INC     DE                  
50A1: 82              ADD     A,D                 
50A2: 44              LD      B,H                 
50A3: 0D              DEC     C                   
50A4: C2 53 10        JP      NZ,$1053            
50A7: C2 56 11        JP      NZ,$1156            
50AA: 61              LD      H,C                 
50AB: AB              XOR     E                   
50AC: 68              LD      L,B                 
50AD: AB              XOR     E                   
50AE: 73              LD      (HL),E              
50AF: 2B              DEC     HL                  
50B0: 82              ADD     A,D                 
50B1: 74              LD      (HL),H              
50B2: 0D              DEC     C                   
50B3: 76              HALT                        
50B4: 2C              INC     L                   
50B5: 28 A1           JR      Z,$5058             ; {}
50B7: FE 06           CP      $06                 
50B9: 0D              DEC     C                   
50BA: 01 F4 29        LD      BC,$29F4            
50BD: F7              RST     0X30                
50BE: 00              NOP                         
50BF: 23              INC     HL                  
50C0: 01 0D 02        LD      BC,$020D            
50C3: 2A              LD      A,(HLI)             
50C4: 07              RLCA                        
50C5: 29              ADD     HL,HL               
50C6: 08 06 09        LD      ($0906),SP          
50C9: 2A              LD      A,(HLI)             
50CA: 83              ADD     A,E                 
50CB: 17              RLA                         
50CC: 06 27           LD      B,$27               
50CE: 06 82           LD      B,$82               
50D0: 28 06           JR      Z,$50D8             ; {}
50D2: 39              ADD     HL,SP               
50D3: 0D              DEC     C                   
50D4: 49              LD      C,C                 
50D5: 2C              INC     L                   
50D6: C6 15           ADD     $15                 
50D8: A7              AND     A                   
50D9: C6 16           ADD     $16                 
50DB: 06 FE           LD      B,$FE               
50DD: 06 2D           LD      B,$2D               
50DF: 04              INC     B                   
50E0: 47              LD      B,A                 
50E1: 10 F6           ;;STOP    $F6                 
50E3: 29              ADD     HL,HL               
50E4: F7              RST     0X30                
50E5: 77              LD      (HL),A              
50E6: 40              LD      B,B                 
50E7: 00              NOP                         
50E8: 21 30 0D        LD      HL,$0D30            
50EB: C3 29 0D        JP      $0D29               
50EE: 09              ADD     HL,BC               
50EF: 26 19           LD      H,$19               
50F1: 2A              LD      A,(HLI)             
50F2: 40              LD      B,B                 
50F3: 2B              DEC     HL                  
50F4: C2 10 06        JP      NZ,$0610            
50F7: 12              LD      (DE),A              
50F8: AC              XOR     H                   
50F9: 84              ADD     A,H                 
50FA: 13              INC     DE                  
50FB: 06 17           LD      B,$17               
50FD: AC              XOR     H                   
50FE: 82              ADD     A,D                 
50FF: 41              LD      B,C                 
5100: A6              AND     (HL)                
5101: 86              ADD     A,(HL)              
5102: 54              LD      D,H                 
5103: A6              AND     (HL)                
5104: 53              LD      D,E                 
5105: A7              AND     A                   
5106: 61              LD      H,C                 
5107: BE              CP      (HL)                
5108: E2              LD      (C),A               
5109: 07              RLCA                        
510A: 6A              LD      L,D                 
510B: 18 10           JR      $511D               ; {}
510D: FE 06           CP      $06                 
510F: 3D              DEC     A                   
5110: 01 47 20        LD      BC,$2047            
5113: F6 29           OR      $29                 
5115: F7              RST     0X30                
5116: 71              LD      (HL),C              
5117: F5              PUSH    AF                  
5118: C6 20           ADD     $20                 
511A: 0D              DEC     C                   
511B: C6 29           ADD     $29                 
511D: 0D              DEC     C                   
511E: 10 29           ;;STOP    $29                 
5120: 88              ADC     A,B                 
5121: 11 06 19        LD      DE,$1906            
5124: 2A              LD      A,(HLI)             
5125: 26 DE           LD      H,$DE               
5127: 32              LD      (HLD),A             
5128: 2C              INC     L                   
5129: 82              ADD     A,D                 
512A: 33              INC     SP                  
512B: 22              LD      (HLI),A             
512C: 35              DEC     (HL)                
512D: 2B              DEC     HL                  
512E: 37              SCF                         
512F: 2C              INC     L                   
5130: 82              ADD     A,D                 
5131: 38 22           JR      C,$5155             ; {}
5133: 42              LD      B,D                 
5134: 24              INC     H                   
5135: 82              ADD     A,D                 
5136: 43              LD      B,E                 
5137: 03              INC     BC                  
5138: 45              LD      B,L                 
5139: 23              INC     HL                  
513A: 47              LD      B,A                 
513B: 2A              LD      A,(HLI)             
513C: 82              ADD     A,D                 
513D: 48              LD      C,B                 
513E: 21 82 50        LD      HL,$5082            
5141: A6              AND     (HL)                
5142: 52              LD      D,D                 
5143: 2A              LD      A,(HLI)             
5144: 82              ADD     A,D                 
5145: 53              LD      D,E                 
5146: 21 55 29        LD      HL,$2955            
5149: C3 57 A6        JP      $A657               
514C: 62              LD      H,D                 
514D: A7              AND     A                   
514E: C2 65 A6        JP      NZ,$A665            
5151: 69              LD      L,C                 
5152: 2C              INC     L                   
5153: 70              LD      (HL),B              
5154: 2B              DEC     HL                  
5155: 73              LD      (HL),E              
5156: A6              AND     (HL)                
5157: 79              LD      A,C                 
5158: 24              INC     H                   
5159: 82              ADD     A,D                 
515A: 71              LD      (HL),C              
515B: 0D              DEC     C                   
515C: FE 06           CP      $06                 
515E: 4D              LD      C,L                 
515F: 30 F6           JR      NC,$5157            ; {}
5161: 39              ADD     HL,SP               
5162: EF              RST     0X28                
5163: 71              LD      (HL),C              
5164: F5              PUSH    AF                  
5165: 00              NOP                         
5166: 25              DEC     H                   
5167: 10 29           ;;STOP    $29                 
5169: 20 0D           JR      NZ,$5178            ; {}
516B: 30 2B           JR      NC,$5198            ; {}
516D: 40              LD      B,B                 
516E: 29              ADD     HL,HL               
516F: 84              ADD     A,H                 
5170: 41              LD      B,C                 
5171: A6              AND     (HL)                
5172: 54              LD      D,H                 
5173: A6              AND     (HL)                
5174: 84              ADD     A,H                 
5175: 60              LD      H,B                 
5176: 22              LD      (HLI),A             
5177: 62              LD      H,D                 
5178: 98              SBC     B                   
5179: 64              LD      H,H                 
517A: 2B              DEC     HL                  
517B: 70              LD      (HL),B              
517C: A6              AND     (HL)                
517D: 83              ADD     A,E                 
517E: 71              LD      (HL),C              
517F: 0D              DEC     C                   
5180: 74              LD      (HL),H              
5181: 27              DAA                         
5182: 88              ADC     A,B                 
5183: 11 06 C3        LD      DE,$C306            
5186: 26 06           LD      H,$06               
5188: FE 06           CP      $06                 
518A: 0D              DEC     C                   
518B: 04              INC     B                   
518C: F4                              
518D: 04              INC     B                   
518E: FA 30 EE        LD      A,($EE30)           
5191: C4 23 20        CALL    NZ,$2023            
5194: C4 26 20        CALL    NZ,$2026            
5197: 35              DEC     (HL)                
5198: 20 44           JR      NZ,$51DE            ; {}
519A: 20 45           JR      NZ,$51E1            ; {}
519C: CB E2           SET     1,E                 
519E: 07              RLCA                        
519F: 67              LD      H,A                 
51A0: 88              ADC     A,B                 
51A1: 80              ADD     A,B                 
51A2: FE 04           CP      $04                 
51A4: 0D              DEC     C                   
51A5: 71              LD      (HL),C              
51A6: F5              PUSH    AF                  
51A7: 02              LD      (BC),A              
51A8: C7              RST     0X00                
51A9: 07              RLCA                        
51AA: C7              RST     0X00                
51AB: C2 00 03        JP      NZ,$0300            
51AE: 01 25 08        LD      BC,$0825            
51B1: 26 C2           LD      H,$C2               
51B3: 09              ADD     HL,BC               
51B4: 03              INC     BC                  
51B5: 11 23 18        LD      DE,$1823            
51B8: 24              INC     H                   
51B9: 20 25           JR      NZ,$51E0            ; {}
51BB: 21 29 28        LD      HL,$2829            
51BE: 2A              LD      A,(HLI)             
51BF: 29              ADD     HL,HL               
51C0: 26 82           LD      H,$82               
51C2: 14              INC     D                   
51C3: AE              XOR     (HL)                
51C4: 31 AF 38        LD      SP,$38AF            
51C7: AF              XOR     A                   
51C8: 41              LD      B,C                 
51C9: B0              OR      B                   
51CA: 48              LD      C,B                 
51CB: B0              OR      B                   
51CC: 82              ADD     A,D                 
51CD: 54              LD      D,H                 
51CE: AF              XOR     A                   
51CF: 82              ADD     A,D                 
51D0: 64              LD      H,H                 
51D1: B0              OR      B                   
51D2: FE 04           CP      $04                 
51D4: 0D              DEC     C                   
51D5: 04              INC     B                   
51D6: F4                              
51D7: 39              ADD     HL,SP               
51D8: F7              RST     0X30                
51D9: 71              LD      (HL),C              
51DA: F5              PUSH    AF                  
51DB: 03              INC     BC                  
51DC: 29              ADD     HL,HL               
51DD: 82              ADD     A,D                 
51DE: 04              INC     B                   
51DF: 0D              DEC     C                   
51E0: 06 2A           LD      B,$2A               
51E2: 82              ADD     A,D                 
51E3: 11 AF 17        LD      DE,$17AF            
51E6: A7              AND     A                   
51E7: C4 21 01        CALL    NZ,$0121            
51EA: 22              LD      (HLI),A             
51EB: 01 84 23        LD      BC,$2384            
51EE: A6              AND     (HL)                
51EF: 32              LD      (HLD),A             
51F0: B0              OR      B                   
51F1: 83              ADD     A,E                 
51F2: 33              INC     SP                  
51F3: AE              XOR     (HL)                
51F4: 42              LD      B,D                 
51F5: AC              XOR     H                   
51F6: 84              ADD     A,H                 
51F7: 43              LD      B,E                 
51F8: A6              AND     (HL)                
51F9: 57              LD      D,A                 
51FA: A7              AND     A                   
51FB: 61              LD      H,C                 
51FC: B0              OR      B                   
51FD: 63              LD      H,E                 
51FE: 2C              INC     L                   
51FF: 85              ADD     A,L                 
5200: 64              LD      H,H                 
5201: 22              LD      (HLI),A             
5202: 69              LD      L,C                 
5203: 28 70           JR      Z,$5275             ; {}
5205: 23              INC     HL                  
5206: 82              ADD     A,D                 
5207: 71              LD      (HL),C              
5208: 0D              DEC     C                   
5209: 73              LD      (HL),E              
520A: 24              INC     H                   
520B: 86              ADD     A,(HL)              
520C: 74              LD      (HL),H              
520D: 03              INC     BC                  
520E: 28 A1           JR      Z,$51B1             ; {}
5210: FE 06           CP      $06                 
5212: 0D              DEC     C                   
5213: 30 F2           JR      NC,$5207            ; {}
5215: 74              LD      (HL),H              
5216: F5              PUSH    AF                  
5217: 22              LD      (HLI),A             
5218: 0F              RRCA                        
5219: C4 24 0F        CALL    NZ,$0F24            
521C: C4 25 0F        CALL    NZ,$0F25            
521F: 27              DAA                         
5220: 0F              RRCA                        
5221: 84              ADD     A,H                 
5222: 33              INC     SP                  
5223: 0F              RRCA                        
5224: 84              ADD     A,H                 
5225: 43              LD      B,E                 
5226: 0F              RRCA                        
5227: 52              LD      D,D                 
5228: 0F              RRCA                        
5229: 57              LD      D,A                 
522A: 0F              RRCA                        
522B: FE 06           CP      $06                 
522D: 2D              DEC     L                   
522E: 07              RLCA                        
522F: 3F              CCF                         
5230: 49              LD      C,C                 
5231: F7              RST     0X30                
5232: 74              LD      (HL),H              
5233: F5              PUSH    AF                  
5234: C3 16 A7        JP      $A716               
5237: 18 A6           JR      $51DF               ; {}
5239: 82              ADD     A,D                 
523A: 28 A6           JR      Z,$51E2             ; {}
523C: 89              ADC     A,C                 
523D: 41              LD      B,C                 
523E: A6              AND     (HL)                
523F: 82              ADD     A,D                 
5240: 47              LD      B,A                 
5241: A7              AND     A                   
5242: 89              ADC     A,C                 
5243: 51              LD      D,C                 
5244: 06 82           LD      B,$82               
5246: 61              LD      H,C                 
5247: 06 70           LD      B,$70               
5249: 23              INC     HL                  
524A: 71              LD      (HL),C              
524B: 06 72           LD      B,$72               
524D: 2C              INC     L                   
524E: 73              LD      (HL),E              
524F: 2B              DEC     HL                  
5250: 82              ADD     A,D                 
5251: 74              LD      (HL),H              
5252: 0D              DEC     C                   
5253: 76              HALT                        
5254: 2C              INC     L                   
5255: 23              INC     HL                  
5256: A0              AND     B                   
5257: FE 06           CP      $06                 
5259: 96              SUB     (HL)                
525A: 03              INC     BC                  
525B: F4                              
525C: 20 F6           JR      NZ,$5254            ; {}
525E: 29              ADD     HL,HL               
525F: F7              RST     0X30                
5260: 73              LD      (HL),E              
5261: F5              PUSH    AF                  
5262: 00              NOP                         
5263: 29              ADD     HL,HL               
5264: 82              ADD     A,D                 
5265: 01 0D 82        LD      BC,$820D            
5268: 03              INC     BC                  
5269: 0D              DEC     C                   
526A: 03              INC     BC                  
526B: A6              AND     (HL)                
526C: 05              DEC     B                   
526D: A6              AND     (HL)                
526E: 06 0D           LD      B,$0D               
5270: 07              RLCA                        
5271: A6              AND     (HL)                
5272: C2 08 0D        JP      NZ,$0D08            
5275: 09              ADD     HL,BC               
5276: 2A              LD      A,(HLI)             
5277: 82              ADD     A,D                 
5278: 10 0D           ;;STOP    $0D                 
527A: 14              INC     D                   
527B: A7              AND     A                   
527C: 16 A7           LD      D,$A7               
527E: 19              ADD     HL,DE               
527F: A6              AND     (HL)                
5280: 82              ADD     A,D                 
5281: 20 A6           JR      NZ,$5229            ; {}
5283: 28 A7           JR      Z,$522C             ; {}
5285: 29              ADD     HL,HL               
5286: 0D              DEC     C                   
5287: 30 0D           JR      NC,$5296            ; {}
5289: 39              ADD     HL,SP               
528A: A6              AND     (HL)                
528B: 82              ADD     A,D                 
528C: 40              LD      B,B                 
528D: A6              AND     (HL)                
528E: 49              LD      C,C                 
528F: 0D              DEC     C                   
5290: 56              LD      D,(HL)              
5291: 2C              INC     L                   
5292: 57              LD      D,A                 
5293: 98              SBC     B                   
5294: 82              ADD     A,D                 
5295: 58              LD      E,B                 
5296: 22              LD      (HLI),A             
5297: 85              ADD     A,L                 
5298: 60              LD      H,B                 
5299: 0D              DEC     C                   
529A: 66              LD      H,(HL)              
529B: 24              INC     H                   
529C: 68              LD      L,B                 
529D: 0F              RRCA                        
529E: C2 69 C0        JP      NZ,$C069            
52A1: 86              ADD     A,(HL)              
52A2: 70              LD      (HL),B              
52A3: 22              LD      (HLI),A             
52A4: 76              HALT                        
52A5: 28 82           JR      Z,$5229             ; {}
52A7: 77              LD      (HL),A              
52A8: 0F              RRCA                        
52A9: 51              LD      D,C                 
52AA: 0D              DEC     C                   
52AB: 53              LD      D,E                 
52AC: 0D              DEC     C                   
52AD: 67              LD      H,A                 
52AE: CB E2           SET     1,E                 
52B0: 07              RLCA                        
52B1: 61              LD      H,C                 
52B2: 88              ADC     A,B                 
52B3: 80              ADD     A,B                 
52B4: FE 06           CP      $06                 
52B6: 7D              LD      A,L                 
52B7: 01 F4 49        LD      BC,$49F4            
52BA: 4A              LD      C,D                 
52BB: 60              LD      H,B                 
52BC: F6 73           OR      $73                 
52BE: F5              PUSH    AF                  
52BF: 00              NOP                         
52C0: 26 83           LD      H,$83               
52C2: 01 0D 04        LD      BC,$040D            
52C5: 25              DEC     H                   
52C6: 10 2A           ;;STOP    $2A                 
52C8: 11 98 12        LD      DE,$1298            
52CB: 26 14           LD      H,$14               
52CD: 23              INC     HL                  
52CE: 22              LD      (HLI),A             
52CF: 2A              LD      A,(HLI)             
52D0: 23              INC     HL                  
52D1: 21 24 29        LD      HL,$2924            
52D4: 82              ADD     A,D                 
52D5: 30 A6           JR      NC,$527D            ; {}
52D7: 86              ADD     A,(HL)              
52D8: 50              LD      D,B                 
52D9: 22              LD      (HLI),A             
52DA: 56              LD      D,(HL)              
52DB: 98              SBC     B                   
52DC: 57              LD      D,A                 
52DD: 2B              DEC     HL                  
52DE: 82              ADD     A,D                 
52DF: 60              LD      H,B                 
52E0: C0              RET     NZ                  
52E1: 85              ADD     A,L                 
52E2: 62              LD      H,D                 
52E3: 0F              RRCA                        
52E4: 64              LD      H,H                 
52E5: A6              AND     (HL)                
52E6: 67              LD      H,A                 
52E7: 23              INC     HL                  
52E8: 82              ADD     A,D                 
52E9: 70              LD      (HL),B              
52EA: C0              RET     NZ                  
52EB: 72              LD      (HL),D              
52EC: 0F              RRCA                        
52ED: 82              ADD     A,D                 
52EE: 73              LD      (HL),E              
52EF: A6              AND     (HL)                
52F0: 82              ADD     A,D                 
52F1: 75              LD      (HL),L              
52F2: 0F              RRCA                        
52F3: 77              LD      (HL),A              
52F4: 27              DAA                         
52F5: 78              LD      A,B                 
52F6: 22              LD      (HLI),A             
52F7: 79              LD      A,C                 
52F8: 28 18           JR      Z,$5312             ; {}
52FA: CB E2           SET     1,E                 
52FC: 07              RLCA                        
52FD: 63              LD      H,E                 
52FE: 88              ADC     A,B                 
52FF: 80              ADD     A,B                 
5300: FE 06           CP      $06                 
5302: 0D              DEC     C                   
5303: 40              LD      B,B                 
5304: 41              LD      B,C                 
5305: 74              LD      (HL),H              
5306: 40              LD      B,B                 
5307: 08 26 C8        LD      ($C826),SP          
530A: 09              ADD     HL,BC               
530B: 03              INC     BC                  
530C: C6 18           ADD     $18                 
530E: 24              INC     H                   
530F: 78              LD      A,B                 
5310: 28 22           JR      Z,$5334             ; {}
5312: 2C              INC     L                   
5313: 83              ADD     A,E                 
5314: 23              INC     HL                  
5315: 22              LD      (HLI),A             
5316: 26 2B           LD      H,$2B               
5318: C2 32 24        JP      NZ,$2432            
531B: 83              ADD     A,E                 
531C: 33              INC     SP                  
531D: 0F              RRCA                        
531E: C2 36 23        JP      NZ,$2336            
5321: 83              ADD     A,E                 
5322: 43              LD      B,E                 
5323: 0F              RRCA                        
5324: 52              LD      D,D                 
5325: 2A              LD      A,(HLI)             
5326: 83              ADD     A,E                 
5327: 53              LD      D,E                 
5328: 21 56 29        LD      HL,$2956            
532B: 54              LD      D,H                 
532C: 98              SBC     B                   
532D: FE 04           CP      $04                 
532F: 0D              DEC     C                   
5330: 77              LD      (HL),A              
5331: F1              POP     AF                  
5332: 03              INC     BC                  
5333: C7              RST     0X00                
5334: 06 C7           LD      B,$C7               
5336: 85              ADD     A,L                 
5337: 13              INC     DE                  
5338: AF              XOR     A                   
5339: 13              INC     DE                  
533A: A6              AND     (HL)                
533B: 82              ADD     A,D                 
533C: 23              INC     HL                  
533D: B0              OR      B                   
533E: 83              ADD     A,E                 
533F: 25              DEC     H                   
5340: 01 31 AF        LD      BC,$AF31            
5343: 83              ADD     A,E                 
5344: 35              DEC     (HL)                
5345: 01 C2 41        LD      BC,$41C2            
5348: 01 42 AF        LD      BC,$AF42            
534B: 83              ADD     A,E                 
534C: 45              LD      B,L                 
534D: B0              OR      B                   
534E: 52              LD      D,D                 
534F: 01 53 AF        LD      BC,$AF53            
5352: 82              ADD     A,D                 
5353: 65              LD      H,L                 
5354: AE              XOR     (HL)                
5355: 23              INC     HL                  
5356: 0D              DEC     C                   
5357: 82              ADD     A,D                 
5358: 51              LD      D,C                 
5359: B0              OR      B                   
535A: 53              LD      D,E                 
535B: AE              XOR     (HL)                
535C: 48              LD      C,B                 
535D: 8E              ADC     A,(HL)              
535E: 11 BE E2        LD      DE,$E2BE            
5361: 07              RLCA                        
5362: 69              LD      L,C                 
5363: 88              ADC     A,B                 
5364: 10 FE           ;;STOP    $FE                 
5366: 04              INC     B                   
5367: 0D              DEC     C                   
5368: 01 F0 39        LD      BC,$39F0            
536B: F3              DI                          
536C: 71              LD      (HL),C              
536D: F1              POP     AF                  
536E: 20 C9           JR      NZ,$5339            ; {}
5370: 29              ADD     HL,HL               
5371: CA 50 C9        JP      Z,$C950             
5374: 59              LD      E,C                 
5375: CA FE 04        JP      Z,$04FE             
5378: 0D              DEC     C                   
5379: 01 F4 30        LD      BC,$30F4            
537C: F6 00           OR      $00                 
537E: 23              INC     HL                  
537F: 82              ADD     A,D                 
5380: 01 0D 03        LD      BC,$030D            
5383: 2A              LD      A,(HLI)             
5384: 13              INC     DE                  
5385: AF              XOR     A                   
5386: 15              DEC     D                   
5387: AE              XOR     (HL)                
5388: 17              RLA                         
5389: AE              XOR     (HL)                
538A: C3 23 01        JP      $0123               
538D: 26 A0           LD      H,$A0               
538F: 35              DEC     (HL)                
5390: AE              XOR     (HL)                
5391: 37              SCF                         
5392: AE              XOR     (HL)                
5393: 82              ADD     A,D                 
5394: 51              LD      D,C                 
5395: AE              XOR     (HL)                
5396: 53              LD      D,E                 
5397: B0              OR      B                   
5398: 56              LD      D,(HL)              
5399: AE              XOR     (HL)                
539A: 64              LD      H,H                 
539B: AE              XOR     (HL)                
539C: 68              LD      L,B                 
539D: AE              XOR     (HL)                
539E: FE 06           CP      $06                 
53A0: 0D              DEC     C                   
53A1: 04              INC     B                   
53A2: F0 39           LD      A,($39)             
53A4: F7              RST     0X30                
53A5: 09              ADD     HL,BC               
53A6: 21 82 18        LD      HL,$1882            
53A9: 06 24           LD      B,$24               
53AB: A6              AND     (HL)                
53AC: 29              ADD     HL,HL               
53AD: 2C              INC     L                   
53AE: 46              LD      B,(HL)              
53AF: A6              AND     (HL)                
53B0: 42              LD      B,D                 
53B1: A6              AND     (HL)                
53B2: 82              ADD     A,D                 
53B3: 43              LD      B,E                 
53B4: 06 53           LD      B,$53               
53B6: 06 88           LD      B,$88               
53B8: 61              LD      H,C                 
53B9: 06 FE           LD      B,$FE               
53BB: 06 0D           LD      B,$0D               
53BD: 04              INC     B                   
53BE: F4                              
53BF: 30 F2           JR      NC,$53B3            ; {}
53C1: 39              ADD     HL,SP               
53C2: F3              DI                          
53C3: 74              LD      (HL),H              
53C4: F5              PUSH    AF                  
53C5: 00              NOP                         
53C6: 29              ADD     HL,HL               
53C7: 01 06 02        LD      BC,$0206            
53CA: 2A              LD      A,(HLI)             
53CB: 03              INC     BC                  
53CC: 29              ADD     HL,HL               
53CD: 82              ADD     A,D                 
53CE: 04              INC     B                   
53CF: 0D              DEC     C                   
53D0: 06 2A           LD      B,$2A               
53D2: 89              ADC     A,C                 
53D3: 10 06           ;;STOP    $06                 
53D5: 82              ADD     A,D                 
53D6: 14              INC     D                   
53D7: 0D              DEC     C                   
53D8: 20 2B           JR      NZ,$5405            ; {}
53DA: 23              INC     HL                  
53DB: 06 26           LD      B,$26               
53DD: 06 84           LD      B,$84               
53DF: 33              INC     SP                  
53E0: 06 73           LD      B,$73               
53E2: 2B              DEC     HL                  
53E3: 82              ADD     A,D                 
53E4: 74              LD      (HL),H              
53E5: 0D              DEC     C                   
53E6: 76              HALT                        
53E7: 2C              INC     L                   
53E8: FE 06           CP      $06                 
53EA: 0D              DEC     C                   
53EB: 07              RLCA                        
53EC: F4                              
53ED: 30 F6           JR      NC,$53E5            ; {}
53EF: 39              ADD     HL,SP               
53F0: F3              DI                          
53F1: 74              LD      (HL),H              
53F2: F1              POP     AF                  
53F3: C2 11 06        JP      NZ,$0611            
53F6: 22              LD      (HLI),A             
53F7: 06 06           LD      B,$06               
53F9: 26 82           LD      H,$82               
53FB: 07              RLCA                        
53FC: 0F              RRCA                        
53FD: 09              ADD     HL,BC               
53FE: C0              RET     NZ                  
53FF: C2 14 20        JP      NZ,$2014            
5402: C3 15 20        JP      $2015               
5405: 16 2A           LD      D,$2A               
5407: 82              ADD     A,D                 
5408: 17              RLA                         
5409: 21 19 26        LD      HL,$2619            
540C: 26 20           LD      H,$20               
540E: 27              DAA                         
540F: 06 82           LD      B,$82               
5411: 32              LD      (HLD),A             
5412: 20 C2           JR      NZ,$53D6            ; {}
5414: 37              SCF                         
5415: 20 83           JR      NZ,$539A            ; {}
5417: 42              LD      B,D                 
5418: 20 83           JR      NZ,$539D            ; {}
541A: 54              LD      D,H                 
541B: 20 82           JR      NZ,$539F            ; {}
541D: 61              LD      H,C                 
541E: 20 68           JR      NZ,$5488            ; {}
5420: 20 12           JR      NZ,$5434            ; {}
5422: 8E              ADC     A,(HL)              
5423: FE 06           CP      $06                 
5425: 0D              DEC     C                   
5426: 03              INC     BC                  
5427: F4                              
5428: 30 F6           JR      NC,$5420            ; {}
542A: 39              ADD     HL,SP               
542B: F7              RST     0X30                
542C: 82              ADD     A,D                 
542D: 00              NOP                         
542E: C0              RET     NZ                  
542F: 85              ADD     A,L                 
5430: 02              LD      (BC),A              
5431: 0F              RRCA                        
5432: 82              ADD     A,D                 
5433: 03              INC     BC                  
5434: A6              AND     (HL)                
5435: 83              ADD     A,E                 
5436: 07              RLCA                        
5437: C0              RET     NZ                  
5438: 10 25           ;;STOP    $25                 
543A: 86              ADD     A,(HL)              
543B: 11 21 17        LD      DE,$1721            
543E: 26 82           LD      H,$82               
5440: 18 C0           JR      $5402               ; {}
5442: C5              PUSH    BC                  
5443: 26 06           LD      H,$06               
5445: 27              DAA                         
5446: 2A              LD      A,(HLI)             
5447: 28 21           JR      Z,$546A             ; {}
5449: 29              ADD     HL,HL               
544A: 26 83           LD      H,$83               
544C: 33              INC     SP                  
544D: 0F              RRCA                        
544E: 83              ADD     A,E                 
544F: 43              LD      B,E                 
5450: 0F              RRCA                        
5451: 44              LD      B,H                 
5452: A0              AND     B                   
5453: 83              ADD     A,E                 
5454: 53              LD      D,E                 
5455: 0F              RRCA                        
5456: 57              LD      D,A                 
5457: 2C              INC     L                   
5458: 58              LD      E,B                 
5459: 22              LD      (HLI),A             
545A: 59              LD      E,C                 
545B: 28 82           JR      Z,$53DF             ; {}
545D: 61              LD      H,C                 
545E: 06 67           LD      B,$67               
5460: 24              INC     H                   
5461: 82              ADD     A,D                 
5462: 68              LD      L,B                 
5463: C0              RET     NZ                  
5464: 77              LD      (HL),A              
5465: 28 82           JR      Z,$53E9             ; {}
5467: 78              LD      A,B                 
5468: C0              RET     NZ                  
5469: 29              ADD     HL,HL               
546A: 21 C2 39        LD      HL,$39C2            
546D: 0D              DEC     C                   
546E: 59              LD      E,C                 
546F: 22              LD      (HLI),A             
5470: FE 06           CP      $06                 
5472: 0D              DEC     C                   
5473: 04              INC     B                   
5474: 47              LD      B,A                 
5475: 30 F6           JR      NC,$546D            ; {}
5477: 39              ADD     HL,SP               
5478: F7              RST     0X30                
5479: 83              ADD     A,E                 
547A: 11 AF 21        LD      DE,$21AF            
547D: B0              OR      B                   
547E: 82              ADD     A,D                 
547F: 22              LD      (HLI),A             
5480: 01 24 AF        LD      BC,$AF24            
5483: 25              DEC     H                   
5484: A6              AND     (HL)                
5485: 32              LD      (HLD),A             
5486: B0              OR      B                   
5487: 82              ADD     A,D                 
5488: 33              INC     SP                  
5489: 01 35 AF        LD      BC,$AF35            
548C: 36 A6           LD      (HL),$A6            
548E: 43              LD      B,E                 
548F: B0              OR      B                   
5490: 82              ADD     A,D                 
5491: 44              LD      B,H                 
5492: 01 46 AF        LD      BC,$AF46            
5495: 54              LD      D,H                 
5496: B0              OR      B                   
5497: 82              ADD     A,D                 
5498: 55              LD      D,L                 
5499: 01 57 AF        LD      BC,$AF57            
549C: 83              ADD     A,E                 
549D: 65              LD      H,L                 
549E: B0              OR      B                   
549F: 68              LD      L,B                 
54A0: AE              XOR     (HL)                
54A1: 18 C0           JR      $5463               ; {}
54A3: 61              LD      H,C                 
54A4: C0              RET     NZ                  
54A5: 20 29           JR      NZ,$54D0            ; {}
54A7: C2 30 0D        JP      NZ,$0D30            
54AA: 50              LD      D,B                 
54AB: 2B              DEC     HL                  
54AC: FE 04           CP      $04                 
54AE: 0D              DEC     C                   
54AF: 07              RLCA                        
54B0: F0 30           LD      A,($30)             
54B2: F2                              
54B3: 77              LD      (HL),A              
54B4: F1              POP     AF                  
54B5: FE 04           CP      $04                 
54B7: 0D              DEC     C                   
54B8: 01 F4 03        LD      BC,$03F4            
54BB: C7              RST     0X00                
54BC: 05              DEC     B                   
54BD: C7              RST     0X00                
54BE: 08 26 C8        LD      ($C826),SP          
54C1: 09              ADD     HL,BC               
54C2: 03              INC     BC                  
54C3: C6 18           ADD     $18                 
54C5: 24              INC     H                   
54C6: 22              LD      (HLI),A             
54C7: A6              AND     (HL)                
54C8: 83              ADD     A,E                 
54C9: 23              INC     HL                  
54CA: 12              LD      (DE),A              
54CB: 26 11           LD      H,$11               
54CD: C2 32 11        JP      NZ,$1132            
54D0: 83              ADD     A,E                 
54D1: 33              INC     SP                  
54D2: 0F              RRCA                        
54D3: 34              INC     (HL)                
54D4: A0              AND     B                   
54D5: 36 16           LD      (HL),$16            
54D7: 83              ADD     A,E                 
54D8: 43              LD      B,E                 
54D9: 0F              RRCA                        
54DA: 46              LD      B,(HL)              
54DB: 10 52           ;;STOP    $52                 
54DD: 12              LD      (DE),A              
54DE: 53              LD      D,E                 
54DF: 15              DEC     D                   
54E0: 82              ADD     A,D                 
54E1: 54              LD      D,H                 
54E2: 13              INC     DE                  
54E3: 78              LD      A,B                 
54E4: 28 73           JR      Z,$5559             ; {}
54E6: C8              RET     Z                   
54E7: 75              LD      (HL),L              
54E8: C8              RET     Z                   
54E9: E1              POP     HL                  
54EA: 07              RLCA                        
54EB: 5D              LD      E,L                 
54EC: 50              LD      D,B                 
54ED: 7C              LD      A,H                 
54EE: FE 06           CP      $06                 
54F0: 0D              DEC     C                   
54F1: 01 06 01        LD      BC,$0106            
54F4: F4                              
54F5: 82              ADD     A,D                 
54F6: 04              INC     B                   
54F7: 0D              DEC     C                   
54F8: 83              ADD     A,E                 
54F9: 00              NOP                         
54FA: 03              INC     BC                  
54FB: 83              ADD     A,E                 
54FC: 07              RLCA                        
54FD: 03              INC     BC                  
54FE: 83              ADD     A,E                 
54FF: 10 03           ;;STOP    $03                 
5501: 83              ADD     A,E                 
5502: 17              RLA                         
5503: 03              INC     BC                  
5504: 82              ADD     A,D                 
5505: 20 03           JR      NZ,$550A            ; {}
5507: 82              ADD     A,D                 
5508: 28 03           JR      Z,$550D             ; {}
550A: C5              PUSH    BC                  
550B: 30 03           JR      NC,$5510            ; {}
550D: C5              PUSH    BC                  
550E: 39              ADD     HL,SP               
550F: 03              INC     BC                  
5510: C2 03 23        JP      NZ,$2303            
5513: C2 06 24        JP      NZ,$2406            
5516: 22              LD      (HLI),A             
5517: 25              DEC     H                   
5518: 23              INC     HL                  
5519: 29              ADD     HL,HL               
551A: 26 2A           LD      H,$2A               
551C: 27              DAA                         
551D: 26 31           LD      H,$31               
551F: 25              DEC     H                   
5520: 32              LD      (HLD),A             
5521: 29              ADD     HL,HL               
5522: 33              INC     SP                  
5523: C0              RET     NZ                  
5524: 36 C0           LD      (HL),$C0            
5526: 37              SCF                         
5527: 2A              LD      A,(HLI)             
5528: 38 26           JR      C,$5550             ; {}
552A: C3 41 23        JP      $2341               
552D: C3 48 24        JP      $2448               
5530: 71              LD      (HL),C              
5531: 27              DAA                         
5532: 78              LD      A,B                 
5533: 28 53           JR      Z,$5588             ; {}
5535: FC                              
5536: E0 00           LD      ($FF00+$00),A       
5538: 10 58           ;;STOP    $58                 
553A: 10 FE           ;;STOP    $FE                 
553C: 06 0D           LD      B,$0D               
553E: 04              INC     B                   
553F: F4                              
5540: 21 20 28        LD      HL,$2820            
5543: 20 41           JR      NZ,$5586            ; {}
5545: 20 48           JR      NZ,$558F            ; {}
5547: 20 34           JR      NZ,$557D            ; {}
5549: 2C              INC     L                   
554A: 35              DEC     (HL)                
554B: 2B              DEC     HL                  
554C: 44              LD      B,H                 
554D: 2A              LD      A,(HLI)             
554E: 45              LD      B,L                 
554F: 29              ADD     HL,HL               
5550: 61              LD      H,C                 
5551: AC              XOR     H                   
5552: 68              LD      L,B                 
5553: AC              XOR     H                   
5554: 18 BF           JR      $5515               ; {}
5556: E2              LD      (C),A               
5557: 07              RLCA                        
5558: 68              LD      L,B                 
5559: 18 10           JR      $556B               ; {}
555B: FE 04           CP      $04                 
555D: 0D              DEC     C                   
555E: 07              RLCA                        
555F: F0 04           LD      A,($04)             
5561: C7              RST     0X00                
5562: 06 C7           LD      B,$C7               
5564: 83              ADD     A,E                 
5565: 00              NOP                         
5566: 03              INC     BC                  
5567: 03              INC     BC                  
5568: 25              DEC     H                   
5569: C3 10 03        JP      $0310               
556C: C3 11 03        JP      $0311               
556F: 12              LD      (DE),A              
5570: 25              DEC     H                   
5571: 13              INC     DE                  
5572: 29              ADD     HL,HL               
5573: 14              INC     D                   
5574: AF              XOR     A                   
5575: 16 20           LD      D,$20               
5577: C2 22 23        JP      NZ,$2322            
557A: 24              INC     H                   
557B: B0              OR      B                   
557C: 82              ADD     A,D                 
557D: 26 AE           LD      H,$AE               
557F: 82              ADD     A,D                 
5580: 34              INC     (HL)                
5581: 20 40           JR      NZ,$55C3            ; {}
5583: 25              DEC     H                   
5584: 41              LD      B,C                 
5585: 21 42 29        LD      HL,$2942            
5588: 44              LD      B,H                 
5589: AF              XOR     A                   
558A: 46              LD      B,(HL)              
558B: 2C              INC     L                   
558C: 82              ADD     A,D                 
558D: 47              LD      B,A                 
558E: 22              LD      (HLI),A             
558F: 49              LD      C,C                 
5590: 28 53           JR      Z,$55E5             ; {}
5592: 20 54           JR      NZ,$55E8            ; {}
5594: B0              OR      B                   
5595: 56              LD      D,(HL)              
5596: 24              INC     H                   
5597: 83              ADD     A,E                 
5598: 57              LD      D,A                 
5599: 03              INC     BC                  
559A: 63              LD      H,E                 
559B: 2C              INC     L                   
559C: 56              LD      D,(HL)              
559D: 24              INC     H                   
559E: 82              ADD     A,D                 
559F: 64              LD      H,H                 
55A0: 22              LD      (HLI),A             
55A1: 66              LD      H,(HL)              
55A2: 28 83           JR      Z,$5527             ; {}
55A4: 67              LD      H,A                 
55A5: 03              INC     BC                  
55A6: 73              LD      (HL),E              
55A7: 28 86           JR      Z,$552F             ; {}
55A9: 74              LD      (HL),H              
55AA: 03              INC     BC                  
55AB: 28 A0           JR      Z,$554D             ; {}
55AD: 61              LD      H,C                 
55AE: BE              CP      (HL)                
55AF: E2              LD      (C),A               
55B0: 07              RLCA                        
55B1: 6B              LD      L,E                 
55B2: 88              ADC     A,B                 
55B3: 10 FE           ;;STOP    $FE                 
55B5: 0E 94           LD      C,$94               
55B7: 82              ADD     A,D                 
55B8: 00              NOP                         
55B9: 54              LD      D,H                 
55BA: 87              ADD     A,A                 
55BB: 02              LD      (BC),A              
55BC: 5C              LD      E,H                 
55BD: 09              ADD     HL,BC               
55BE: 54              LD      D,H                 
55BF: C2 10 54        JP      NZ,$5410            ; {}
55C2: 11 57 C3        LD      DE,$C357            
55C5: 19              ADD     HL,DE               
55C6: 51              LD      D,C                 
55C7: 21 5E 87        LD      HL,$875E            
55CA: 22              LD      (HLI),A             
55CB: 8A              ADC     A,D                 
55CC: C5              PUSH    BC                  
55CD: 30 57           JR      NC,$5626            ; {}
55CF: 41              LD      B,C                 
55D0: 62              LD      H,D                 
55D1: 42              LD      B,D                 
55D2: 5B              LD      E,E                 
55D3: 84              ADD     A,H                 
55D4: 43              LD      B,E                 
55D5: 8A              ADC     A,D                 
55D6: 49              LD      C,C                 
55D7: 5C              LD      E,H                 
55D8: C3 51 63        JP      $6351               ; {}
55DB: 52              LD      D,D                 
55DC: 57              LD      D,A                 
55DD: 84              ADD     A,H                 
55DE: 53              LD      D,E                 
55DF: 8A              ADC     A,D                 
55E0: C2 62 54        JP      NZ,$5462            ; {}
55E3: 87              ADD     A,A                 
55E4: 63              LD      H,E                 
55E5: 5B              LD      E,E                 
55E6: 87              ADD     A,A                 
55E7: 73              LD      (HL),E              
55E8: 54              LD      D,H                 
55E9: E1              POP     HL                  
55EA: 07              RLCA                        
55EB: 39              ADD     HL,SP               
55EC: 48              LD      C,B                 
55ED: 20 FE           JR      NZ,$55ED            ; {}
55EF: 0E 94           LD      C,$94               
55F1: 8A              ADC     A,D                 
55F2: 00              NOP                         
55F3: 54              LD      D,H                 
55F4: 8A              ADC     A,D                 
55F5: 10 54           ;;STOP    $54                 
55F7: 8A              ADC     A,D                 
55F8: 20 54           JR      NZ,$564E            ; {}
55FA: 8A              ADC     A,D                 
55FB: 30 54           JR      NC,$5651            ; {}
55FD: 84              ADD     A,H                 
55FE: 22              LD      (HLI),A             
55FF: 5C              LD      E,H                 
5600: 31 5E 84        LD      SP,$845E            
5603: 32              LD      (HLD),A             
5604: 8A              ADC     A,D                 
5605: 82              ADD     A,D                 
5606: 36 5C           LD      (HL),$5C            
5608: 40              LD      B,B                 
5609: 5E              LD      E,(HL)              
560A: 82              ADD     A,D                 
560B: 41              LD      B,C                 
560C: 8A              ADC     A,D                 
560D: 46              LD      B,(HL)              
560E: 8A              ADC     A,D                 
560F: 48              LD      C,B                 
5610: 5A              LD      E,D                 
5611: 49              LD      C,C                 
5612: 54              LD      D,H                 
5613: 85              ADD     A,L                 
5614: 52              LD      D,D                 
5615: 8A              ADC     A,D                 
5616: C3 59 51        JP      $5159               ; {}
5619: 88              ADC     A,B                 
561A: 60              LD      H,B                 
561B: 5B              LD      E,E                 
561C: 88              ADC     A,B                 
561D: 70              LD      (HL),B              
561E: 54              LD      D,H                 
561F: 68              LD      L,B                 
5620: 62              LD      H,D                 
5621: 78              LD      A,B                 
5622: 63              LD      H,E                 
5623: E1              POP     HL                  
5624: 07              RLCA                        
5625: 50              LD      D,B                 
5626: 78              LD      A,B                 
5627: 70              LD      (HL),B              
5628: FE 0E           CP      $0E                 
562A: 94              SUB     H                   
562B: 00              NOP                         
562C: 54              LD      D,H                 
562D: 86              ADD     A,(HL)              
562E: 01 5C 83        LD      BC,$835C            
5631: 07              RLCA                        
5632: 54              LD      D,H                 
5633: C7              RST     0X00                
5634: 10 57           ;;STOP    $57                 
5636: 82              ADD     A,D                 
5637: 15              DEC     D                   
5638: 8A              ADC     A,D                 
5639: 83              ADD     A,E                 
563A: 17              RLA                         
563B: 5C              LD      E,H                 
563C: 21 62 22        LD      HL,$2262            
563F: 5B              LD      E,E                 
5640: 83              ADD     A,E                 
5641: 25              DEC     H                   
5642: 8A              ADC     A,D                 
5643: C5              PUSH    BC                  
5644: 31 63 C5        LD      SP,$C563            
5647: 32              LD      (HLD),A             
5648: 57              LD      D,A                 
5649: C4 33 8A        CALL    NZ,$8A33            
564C: C2 36 8A        JP      NZ,$8A36            
564F: C3 44 8A        JP      $8A44               
5652: 48              LD      C,B                 
5653: 64              LD      H,H                 
5654: 49              LD      C,C                 
5655: 5B              LD      E,E                 
5656: C2 55 8A        JP      NZ,$8A55            
5659: 57              LD      D,A                 
565A: 8A              ADC     A,D                 
565B: 58              LD      E,B                 
565C: 65              LD      H,L                 
565D: C2 59 51        JP      NZ,$5159            ; {}
5660: 66              LD      H,(HL)              
5661: 8A              ADC     A,D                 
5662: 86              ADD     A,(HL)              
5663: 73              LD      (HL),E              
5664: 5B              LD      E,E                 
5665: 79              LD      A,C                 
5666: 54              LD      D,H                 
5667: 56              LD      D,(HL)              
5668: 8A              ADC     A,D                 
5669: 67              LD      H,A                 
566A: 8A              ADC     A,D                 
566B: 06 54           LD      B,$54               
566D: 16 51           LD      D,$51               
566F: 17              RLA                         
5670: 54              LD      D,H                 
5671: 82              ADD     A,D                 
5672: 26 5C           LD      H,$5C               
5674: E1              POP     HL                  
5675: 07              RLCA                        
5676: 3B              DEC     SP                  
5677: 58              LD      E,B                 
5678: 40              LD      B,B                 
5679: FE 0E           CP      $0E                 
567B: 94              SUB     H                   
567C: 82              ADD     A,D                 
567D: 00              NOP                         
567E: 54              LD      D,H                 
567F: 86              ADD     A,(HL)              
5680: 02              LD      (BC),A              
5681: 5C              LD      E,H                 
5682: 83              ADD     A,E                 
5683: 07              RLCA                        
5684: 54              LD      D,H                 
5685: 10 5C           ;;STOP    $5C                 
5687: 11 54 85        LD      DE,$8554            
568A: 12              LD      (DE),A              
568B: 8A              ADC     A,D                 
568C: 82              ADD     A,D                 
568D: 17              RLA                         
568E: 54              LD      D,H                 
568F: 19              ADD     HL,DE               
5690: 54              LD      D,H                 
5691: 82              ADD     A,D                 
5692: 21 5C 82        LD      HL,$825C            
5695: 23              INC     HL                  
5696: 8A              ADC     A,D                 
5697: 25              DEC     H                   
5698: 5B              LD      E,E                 
5699: 82              ADD     A,D                 
569A: 26 8A           LD      H,$8A               
569C: C6 29           ADD     $29                 
569E: 51              LD      D,C                 
569F: 85              ADD     A,L                 
56A0: 32              LD      (HLD),A             
56A1: 8A              ADC     A,D                 
56A2: 35              DEC     (HL)                
56A3: 5C              LD      E,H                 
56A4: 37              SCF                         
56A5: 5B              LD      E,E                 
56A6: 38 64           JR      C,$570C             ; {}
56A8: 83              ADD     A,E                 
56A9: 40              LD      B,B                 
56AA: 5B              LD      E,E                 
56AB: 83              ADD     A,E                 
56AC: 44              LD      B,H                 
56AD: 8A              ADC     A,D                 
56AE: 47              LD      B,A                 
56AF: 57              LD      D,A                 
56B0: C2 48 65        JP      NZ,$6548            ; {}
56B3: 82              ADD     A,D                 
56B4: 50              LD      D,B                 
56B5: 54              LD      D,H                 
56B6: C2 52 57        JP      NZ,$5752            ; {}
56B9: 55              LD      D,L                 
56BA: 8A              ADC     A,D                 
56BB: 82              ADD     A,D                 
56BC: 56              LD      D,(HL)              
56BD: 5C              LD      E,H                 
56BE: 82              ADD     A,D                 
56BF: 60              LD      H,B                 
56C0: 54              LD      D,H                 
56C1: 82              ADD     A,D                 
56C2: 63              LD      H,E                 
56C3: 5B              LD      E,E                 
56C4: 67              LD      H,A                 
56C5: 8A              ADC     A,D                 
56C6: 85              ADD     A,L                 
56C7: 70              LD      (HL),B              
56C8: 54              LD      D,H                 
56C9: 83              ADD     A,E                 
56CA: 75              LD      (HL),L              
56CB: 5B              LD      E,E                 
56CC: 78              LD      A,B                 
56CD: 62              LD      H,D                 
56CE: E1              POP     HL                  
56CF: 07              RLCA                        
56D0: 51              LD      D,C                 
56D1: 88              ADC     A,B                 
56D2: 20 FE           JR      NZ,$56D2            ; {}
56D4: 0F              RRCA                        
56D5: 94              SUB     H                   
56D6: 02              LD      (BC),A              
56D7: 5C              LD      E,H                 
56D8: 87              ADD     A,A                 
56D9: 03              INC     BC                  
56DA: 54              LD      D,H                 
56DB: C3 01 63        JP      $6301               ; {}
56DE: C5              PUSH    BC                  
56DF: 00              NOP                         
56E0: 57              LD      D,A                 
56E1: 09              ADD     HL,BC               
56E2: 5C              LD      E,H                 
56E3: 31 5B 35        LD      SP,$355B            
56E6: 61              LD      H,C                 
56E7: 39              ADD     HL,SP               
56E8: 59              LD      E,C                 
56E9: C4 40 54        CALL    NZ,$5440            ; {}
56EC: C4 41 57        CALL    NZ,$5741            ; {}
56EF: C4 49 51        CALL    NZ,$5149            ; {}
56F2: 87              ADD     A,A                 
56F3: 62              LD      H,D                 
56F4: 85              ADD     A,L                 
56F5: 87              ADD     A,A                 
56F6: 72              LD      (HL),D              
56F7: AD              XOR     L                   
56F8: 86              ADD     A,(HL)              
56F9: 13              INC     DE                  
56FA: 71              LD      (HL),C              
56FB: C2 15 4D        JP      NZ,$4D15            ; {}
56FE: 17              RLA                         
56FF: 70              LD      (HL),B              
5700: 27              DAA                         
5701: 71              LD      (HL),C              
5702: E1              POP     HL                  
5703: 07              RLCA                        
5704: 43              LD      B,E                 
5705: 48              LD      C,B                 
5706: 70              LD      (HL),B              
5707: FE 0F           CP      $0F                 
5709: 94              SUB     H                   
570A: 8A              ADC     A,D                 
570B: 00              NOP                         
570C: 54              LD      D,H                 
570D: 82              ADD     A,D                 
570E: 00              NOP                         
570F: 5C              LD      E,H                 
5710: 07              RLCA                        
5711: 5C              LD      E,H                 
5712: C3 08 62        JP      $6208               ; {}
5715: C3 09 51        JP      $5109               ; {}
5718: 30 5D           JR      NC,$5777            ; {}
571A: 38 59           JR      C,$5775             ; {}
571C: 38 5B           JR      C,$5779             ; {}
571E: 39              ADD     HL,SP               
571F: 54              LD      D,H                 
5720: C4 40 57        CALL    NZ,$5740            ; {}
5723: C4 48 51        CALL    NZ,$5148            ; {}
5726: C4 49 54        CALL    NZ,$5449            ; {}
5729: 87              ADD     A,A                 
572A: 61              LD      H,C                 
572B: 85              ADD     A,L                 
572C: 87              ADD     A,A                 
572D: 71              LD      (HL),C              
572E: AD              XOR     L                   
572F: 85              ADD     A,L                 
5730: 12              LD      (DE),A              
5731: 71              LD      (HL),C              
5732: 13              INC     DE                  
5733: 70              LD      (HL),B              
5734: 15              DEC     D                   
5735: 70              LD      (HL),B              
5736: 23              INC     HL                  
5737: 71              LD      (HL),C              
5738: 25              DEC     H                   
5739: 71              LD      (HL),C              
573A: E1              POP     HL                  
573B: 07              RLCA                        
573C: 37              SCF                         
573D: 28 50           JR      Z,$578F             ; {}
573F: FE 0F           CP      $0F                 
5741: 94              SUB     H                   
5742: 86              ADD     A,(HL)              
5743: 00              NOP                         
5744: 54              LD      D,H                 
5745: 84              ADD     A,H                 
5746: 06 5C           LD      B,$5C               
5748: 83              ADD     A,E                 
5749: 10 54           ;;STOP    $54                 
574B: 13              INC     DE                  
574C: 70              LD      (HL),B              
574D: 82              ADD     A,D                 
574E: 14              INC     D                   
574F: 71              LD      (HL),C              
5750: C6 20           ADD     $20                 
5752: 54              LD      D,H                 
5753: 21 57 82        LD      HL,$8257            
5756: 22              LD      (HLI),A             
5757: 71              LD      (HL),C              
5758: 27              DAA                         
5759: 59              LD      E,C                 
575A: 82              ADD     A,D                 
575B: 28 5B           JR      Z,$57B8             ; {}
575D: 31 54 32        LD      SP,$3254            
5760: 5B              LD      E,E                 
5761: 35              DEC     (HL)                
5762: 5B              LD      E,E                 
5763: 37              SCF                         
5764: 5A              LD      E,D                 
5765: 82              ADD     A,D                 
5766: 38 5C           JR      C,$57C4             ; {}
5768: 41              LD      B,C                 
5769: 71              LD      (HL),C              
576A: 84              ADD     A,H                 
576B: 42              LD      B,D                 
576C: 5C              LD      E,H                 
576D: 61              LD      H,C                 
576E: 64              LD      H,H                 
576F: 62              LD      H,D                 
5770: 5B              LD      E,E                 
5771: 68              LD      L,B                 
5772: 59              LD      E,C                 
5773: 69              LD      L,C                 
5774: 5B              LD      E,E                 
5775: 71              LD      (HL),C              
5776: 65              LD      H,L                 
5777: 72              LD      (HL),D              
5778: 54              LD      D,H                 
5779: 85              ADD     A,L                 
577A: 73              LD      (HL),E              
577B: 5B              LD      E,E                 
577C: 82              ADD     A,D                 
577D: 78              LD      A,B                 
577E: 54              LD      D,H                 
577F: E1              POP     HL                  
5780: 07              RLCA                        
5781: 31 78 20        LD      SP,$2078            
5784: FE 0F           CP      $0F                 
5786: 94              SUB     H                   
5787: 8A              ADC     A,D                 
5788: 00              NOP                         
5789: 5C              LD      E,H                 
578A: 83              ADD     A,E                 
578B: 03              INC     BC                  
578C: 54              LD      D,H                 
578D: 09              ADD     HL,BC               
578E: 54              LD      D,H                 
578F: 13              INC     DE                  
5790: 71              LD      (HL),C              
5791: 14              INC     D                   
5792: 70              LD      (HL),B              
5793: 15              DEC     D                   
5794: 71              LD      (HL),C              
5795: 18 8F           JR      $5726               ; {}
5797: 19              ADD     HL,DE               
5798: 54              LD      D,H                 
5799: 20 5B           JR      NZ,$57F6            ; {}
579B: 82              ADD     A,D                 
579C: 21 64 24        LD      HL,$2464            
579F: 71              LD      (HL),C              
57A0: 28 64           JR      Z,$5806             ; {}
57A2: C6 29           ADD     $29                 
57A4: 51              LD      D,C                 
57A5: 30 5C           JR      NC,$5803            ; {}
57A7: 31 D9 32        LD      SP,$32D9            
57AA: 65              LD      H,L                 
57AB: C5              PUSH    BC                  
57AC: 38 65           JR      C,$5813             ; {}
57AE: 52              LD      D,D                 
57AF: 5B              LD      E,E                 
57B0: 82              ADD     A,D                 
57B1: 60              LD      H,B                 
57B2: 5B              LD      E,E                 
57B3: C2 62 57        JP      NZ,$5762            ; {}
57B6: 84              ADD     A,H                 
57B7: 63              LD      H,E                 
57B8: 85              ADD     A,L                 
57B9: 47              LD      B,A                 
57BA: 5B              LD      E,E                 
57BB: 82              ADD     A,D                 
57BC: 70              LD      (HL),B              
57BD: 54              LD      D,H                 
57BE: 84              ADD     A,H                 
57BF: 73              LD      (HL),E              
57C0: AD              XOR     L                   
57C1: C3 57 57        JP      $5757               ; {}
57C4: 28 64           JR      Z,$582A             ; {}
57C6: 48              LD      C,B                 
57C7: 64              LD      H,H                 
57C8: 68              LD      L,B                 
57C9: 64              LD      H,H                 
57CA: E1              POP     HL                  
57CB: 07              RLCA                        
57CC: 4B              LD      C,E                 
57CD: 58              LD      E,B                 
57CE: 50              LD      D,B                 
57CF: FE 05           CP      $05                 
57D1: 94              SUB     H                   
57D2: 88              ADC     A,B                 
57D3: 02              LD      (BC),A              
57D4: 54              LD      D,H                 
57D5: 02              LD      (BC),A              
57D6: 51              LD      D,C                 
57D7: 09              ADD     HL,BC               
57D8: 5C              LD      E,H                 
57D9: C7              RST     0X00                
57DA: 01 63 87        LD      BC,$8763            
57DD: 12              LD      (DE),A              
57DE: 71              LD      (HL),C              
57DF: 13              INC     DE                  
57E0: 70              LD      (HL),B              
57E1: 15              DEC     D                   
57E2: 70              LD      (HL),B              
57E3: 17              RLA                         
57E4: 70              LD      (HL),B              
57E5: 23              INC     HL                  
57E6: 71              LD      (HL),C              
57E7: 25              DEC     H                   
57E8: 71              LD      (HL),C              
57E9: 27              DAA                         
57EA: 71              LD      (HL),C              
57EB: 36 59           LD      (HL),$59            
57ED: 37              SCF                         
57EE: 5D              LD      E,L                 
57EF: 39              ADD     HL,SP               
57F0: 5B              LD      E,E                 
57F1: C7              RST     0X00                
57F2: 00              NOP                         
57F3: 57              LD      D,A                 
57F4: 82              ADD     A,D                 
57F5: 46              LD      B,(HL)              
57F6: 5C              LD      E,H                 
57F7: C3 49 51        JP      $5149               ; {}
57FA: 65              LD      H,L                 
57FB: 4C              LD      C,H                 
57FC: 68              LD      L,B                 
57FD: 4C              LD      C,H                 
57FE: 70              LD      (HL),B              
57FF: 54              LD      D,H                 
5800: 87              ADD     A,A                 
5801: 71              LD      (HL),C              
5802: 5B              LD      E,E                 
5803: 75              LD      (HL),L              
5804: 54              LD      D,H                 
5805: 82              ADD     A,D                 
5806: 78              LD      A,B                 
5807: 54              LD      D,H                 
5808: E1              POP     HL                  
5809: 07              RLCA                        
580A: 5E              LD      E,(HL)              
580B: 88              ADC     A,B                 
580C: 20 FE           JR      NZ,$580C            ; {}
580E: 05              DEC     B                   
580F: 94              SUB     H                   
5810: 8A              ADC     A,D                 
5811: 00              NOP                         
5812: 54              LD      D,H                 
5813: 00              NOP                         
5814: 5C              LD      E,H                 
5815: 07              RLCA                        
5816: 57              LD      D,A                 
5817: C3 08 63        JP      $6308               ; {}
581A: 13              INC     DE                  
581B: 5A              LD      E,D                 
581C: C2 14 54        JP      NZ,$5414            ; {}
581F: 83              ADD     A,E                 
5820: 15              DEC     D                   
5821: 5C              LD      E,H                 
5822: 17              RLA                         
5823: 5E              LD      E,(HL)              
5824: 34              INC     (HL)                
5825: 5C              LD      E,H                 
5826: C3 09 51        JP      $5109               ; {}
5829: 30 5B           JR      NC,$5886            ; {}
582B: 31 64 35        LD      SP,$3564            
582E: 64              LD      H,H                 
582F: 83              ADD     A,E                 
5830: 36 5B           LD      (HL),$5B            
5832: 39              ADD     HL,SP               
5833: 54              LD      D,H                 
5834: C3 40 57        JP      $5740               ; {}
5837: C3 41 65        JP      $6541               ; {}
583A: 82              ADD     A,D                 
583B: 46              LD      B,(HL)              
583C: 5C              LD      E,H                 
583D: 82              ADD     A,D                 
583E: 48              LD      C,B                 
583F: 54              LD      D,H                 
5840: 58              LD      E,B                 
5841: 51              LD      D,C                 
5842: 59              LD      E,C                 
5843: 54              LD      D,H                 
5844: 82              ADD     A,D                 
5845: 65              LD      H,L                 
5846: 4C              LD      C,H                 
5847: 67              LD      H,A                 
5848: 5B              LD      E,E                 
5849: 82              ADD     A,D                 
584A: 68              LD      L,B                 
584B: 54              LD      D,H                 
584C: 70              LD      (HL),B              
584D: 54              LD      D,H                 
584E: 84              ADD     A,H                 
584F: 71              LD      (HL),C              
5850: 5B              LD      E,E                 
5851: 85              ADD     A,L                 
5852: 75              LD      (HL),L              
5853: 54              LD      D,H                 
5854: E1              POP     HL                  
5855: 07              RLCA                        
5856: 53              LD      D,E                 
5857: 18 20           JR      $5879               ; {}
5859: FE 0F           CP      $0F                 
585B: 94              SUB     H                   
585C: 02              LD      (BC),A              
585D: 5C              LD      E,H                 
585E: 87              ADD     A,A                 
585F: 03              INC     BC                  
5860: 54              LD      D,H                 
5861: C4 01 63        CALL    NZ,$6301            ; {}
5864: C5              PUSH    BC                  
5865: 00              NOP                         
5866: 57              LD      D,A                 
5867: 41              LD      B,C                 
5868: 5B              LD      E,E                 
5869: 42              LD      B,D                 
586A: 5D              LD      E,L                 
586B: 46              LD      B,(HL)              
586C: 5B              LD      E,E                 
586D: C3 50 54        JP      $5450               ; {}
5870: C3 51 54        JP      $5451               ; {}
5873: C3 52 57        JP      $5752               ; {}
5876: 54              LD      D,H                 
5877: 5B              LD      E,E                 
5878: 85              ADD     A,L                 
5879: 63              LD      H,E                 
587A: 85              ADD     A,L                 
587B: 85              ADD     A,L                 
587C: 73              LD      (HL),E              
587D: AD              XOR     L                   
587E: C3 56 54        JP      $5456               ; {}
5881: 58              LD      E,B                 
5882: 59              LD      E,C                 
5883: 59              LD      E,C                 
5884: 5B              LD      E,E                 
5885: C2 64 54        JP      NZ,$5464            ; {}
5888: C2 68 51        JP      NZ,$5168            ; {}
588B: C2 69 54        JP      NZ,$5469            ; {}
588E: 13              INC     DE                  
588F: 71              LD      (HL),C              
5890: 14              INC     D                   
5891: 70              LD      (HL),B              
5892: 15              DEC     D                   
5893: 71              LD      (HL),C              
5894: 16 70           LD      D,$70               
5896: 17              RLA                         
5897: 71              LD      (HL),C              
5898: 18 70           JR      $590A               ; {}
589A: 19              ADD     HL,DE               
589B: 71              LD      (HL),C              
589C: 24              INC     H                   
589D: 71              LD      (HL),C              
589E: 26 71           LD      H,$71               
58A0: 28 71           JR      Z,$5913             ; {}
58A2: E1              POP     HL                  
58A3: 07              RLCA                        
58A4: 48              LD      C,B                 
58A5: 18 70           JR      $5917               ; {}
58A7: FE 0F           CP      $0F                 
58A9: 94              SUB     H                   
58AA: 8A              ADC     A,D                 
58AB: 00              NOP                         
58AC: 6D              LD      L,L                 
58AD: C5              PUSH    BC                  
58AE: 08 63 11        LD      ($1163),SP          
58B1: 5C              LD      E,H                 
58B2: 85              ADD     A,L                 
58B3: 12              LD      (DE),A              
58B4: 54              LD      D,H                 
58B5: 17              RLA                         
58B6: 5C              LD      E,H                 
58B7: C6 09           ADD     $09                 
58B9: 51              LD      D,C                 
58BA: 22              LD      (HLI),A             
58BB: 5A              LD      E,D                 
58BC: 83              ADD     A,E                 
58BD: 23              INC     HL                  
58BE: 5C              LD      E,H                 
58BF: 26 5E           LD      H,$5E               
58C1: 86              ADD     A,(HL)              
58C2: 31 64 46        LD      SP,$4664            
58C5: 65              LD      H,L                 
58C6: 50              LD      D,B                 
58C7: 5B              LD      E,E                 
58C8: 51              LD      D,C                 
58C9: 5D              LD      E,L                 
58CA: 57              LD      D,A                 
58CB: 59              LD      E,C                 
58CC: 58              LD      E,B                 
58CD: 5B              LD      E,E                 
58CE: C2 60 54        JP      NZ,$5460            ; {}
58D1: C2 61 57        JP      NZ,$5761            ; {}
58D4: 85              ADD     A,L                 
58D5: 62              LD      H,D                 
58D6: 85              ADD     A,L                 
58D7: 85              ADD     A,L                 
58D8: 72              LD      (HL),D              
58D9: AD              XOR     L                   
58DA: C2 67 51        JP      NZ,$5167            ; {}
58DD: C2 68 54        JP      NZ,$5468            ; {}
58E0: C2 69 54        JP      NZ,$5469            ; {}
58E3: 00              NOP                         
58E4: 5C              LD      E,H                 
58E5: 86              ADD     A,(HL)              
58E6: 01 54 07        LD      BC,$0754            
58E9: 57              LD      D,A                 
58EA: E1              POP     HL                  
58EB: 07              RLCA                        
58EC: 5F              LD      E,A                 
58ED: 18 70           JR      $595F               ; {}
58EF: FE 04           CP      $04                 
58F1: 0F              RRCA                        
58F2: 74              LD      (HL),H              
58F3: F5              PUSH    AF                  
58F4: 82              ADD     A,D                 
58F5: 00              NOP                         
58F6: 03              INC     BC                  
58F7: 02              LD      (BC),A              
58F8: 25              DEC     H                   
58F9: 07              RLCA                        
58FA: 26 82           LD      H,$82               
58FC: 08 03 C2        LD      ($C203),SP          
58FF: 10 03           ;;STOP    $03                 
5901: 11 25 12        LD      DE,$1225            
5904: 29              ADD     HL,HL               
5905: 17              RLA                         
5906: 2A              LD      A,(HLI)             
5907: 18 26           JR      $592F               ; {}
5909: C2 19 03        JP      NZ,$0319            
590C: 21 23 28        LD      HL,$2823            
590F: 24              INC     H                   
5910: 30 25           JR      NC,$5937            ; {}
5912: 31 29 32        LD      SP,$3229            
5915: 25              DEC     H                   
5916: 84              ADD     A,H                 
5917: 33              INC     SP                  
5918: 21 82 34        LD      HL,$3482            
591B: 97              SUB     A                   
591C: 37              SCF                         
591D: 26 38           LD      H,$38               
591F: 2A              LD      A,(HLI)             
5920: 39              ADD     HL,SP               
5921: 26 41           LD      H,$41               
5923: 25              DEC     H                   
5924: 42              LD      B,D                 
5925: 29              ADD     HL,HL               
5926: 47              LD      B,A                 
5927: 2A              LD      A,(HLI)             
5928: 48              LD      C,B                 
5929: 26 C2           LD      H,$C2               
592B: 51              LD      D,C                 
592C: 23              INC     HL                  
592D: C2 58 24        JP      NZ,$2458            
5930: 70              LD      (HL),B              
5931: 23              INC     HL                  
5932: 71              LD      (HL),C              
5933: 27              DAA                         
5934: 78              LD      A,B                 
5935: 28 79           JR      Z,$59B0             ; {}
5937: 24              INC     H                   
5938: 53              LD      D,E                 
5939: AB              XOR     E                   
593A: 56              LD      D,(HL)              
593B: AB              XOR     E                   
593C: FE 04           CP      $04                 
593E: 0F              RRCA                        
593F: 00              NOP                         
5940: 00              NOP                         
5941: 01 25 03        LD      BC,$0325            
5944: 29              ADD     HL,HL               
5945: 82              ADD     A,D                 
5946: 04              INC     B                   
5947: 0F              RRCA                        
5948: 06 2A           LD      B,$2A               
594A: 08 26 09        LD      ($0926),SP          
594D: 00              NOP                         
594E: 10 25           ;;STOP    $25                 
5950: 11 29 18        LD      DE,$1829            
5953: 2A              LD      A,(HLI)             
5954: 19              ADD     HL,DE               
5955: 26 60           LD      H,$60               
5957: 27              DAA                         
5958: 61              LD      H,C                 
5959: 2B              DEC     HL                  
595A: 68              LD      L,B                 
595B: 2C              INC     L                   
595C: 69              LD      L,C                 
595D: 28 70           JR      Z,$59CF             ; {}
595F: 00              NOP                         
5960: 71              LD      (HL),C              
5961: 27              DAA                         
5962: 78              LD      A,B                 
5963: 28 79           JR      Z,$59DE             ; {}
5965: 00              NOP                         
5966: 00              NOP                         
5967: AB              XOR     E                   
5968: 09              ADD     HL,BC               
5969: AB              XOR     E                   
596A: 74              LD      (HL),H              
596B: FD                              
596C: E0 00           LD      ($FF00+$00),A       
596E: 06 58           LD      B,$58               
5970: 40              LD      B,B                 
5971: FE 04           CP      $04                 
5973: 0D              DEC     C                   
5974: 03              INC     BC                  
5975: 29              ADD     HL,HL               
5976: 82              ADD     A,D                 
5977: 04              INC     B                   
5978: 0D              DEC     C                   
5979: 06 2A           LD      B,$2A               
597B: 20 29           JR      NZ,$59A6            ; {}
597D: 29              ADD     HL,HL               
597E: 2A              LD      A,(HLI)             
597F: C2 30 0D        JP      NZ,$0D30            
5982: C2 39 0D        JP      NZ,$0D39            
5985: 50              LD      D,B                 
5986: 2B              DEC     HL                  
5987: 59              LD      E,C                 
5988: 2C              INC     L                   
5989: 73              LD      (HL),E              
598A: 2B              DEC     HL                  
598B: 82              ADD     A,D                 
598C: 74              LD      (HL),H              
598D: 0D              DEC     C                   
598E: 76              HALT                        
598F: 2C              INC     L                   
5990: FE 04           CP      $04                 
5992: 0D              DEC     C                   
5993: 00              NOP                         
5994: 00              NOP                         
5995: 01 25 03        LD      BC,$0325            
5998: 29              ADD     HL,HL               
5999: 82              ADD     A,D                 
599A: 04              INC     B                   
599B: 0D              DEC     C                   
599C: 06 2A           LD      B,$2A               
599E: 08 26 09        LD      ($0926),SP          
59A1: 00              NOP                         
59A2: 10 25           ;;STOP    $25                 
59A4: 11 29 18        LD      DE,$1829            
59A7: 2A              LD      A,(HLI)             
59A8: 19              ADD     HL,DE               
59A9: 26 60           LD      H,$60               
59AB: 27              DAA                         
59AC: 61              LD      H,C                 
59AD: 2B              DEC     HL                  
59AE: 68              LD      L,B                 
59AF: 2C              INC     L                   
59B0: 69              LD      L,C                 
59B1: 28 70           JR      Z,$5A23             ; {}
59B3: 00              NOP                         
59B4: 71              LD      (HL),C              
59B5: 27              DAA                         
59B6: 78              LD      A,B                 
59B7: 28 79           JR      Z,$5A32             ; {}
59B9: 00              NOP                         
59BA: 32              LD      (HLD),A             
59BB: AC              XOR     H                   
59BC: 37              SCF                         
59BD: AC              XOR     H                   
59BE: 73              LD      (HL),E              
59BF: 2B              DEC     HL                  
59C0: 82              ADD     A,D                 
59C1: 74              LD      (HL),H              
59C2: 0D              DEC     C                   
59C3: 76              HALT                        
59C4: 2C              INC     L                   
59C5: FE 04           CP      $04                 
59C7: 3D              DEC     A                   
59C8: 11 25 86        LD      DE,$8625            
59CB: 12              LD      (DE),A              
59CC: 21 18 26        LD      HL,$2618            
59CF: C5              PUSH    BC                  
59D0: 21 23 22        LD      HL,$2223            
59D3: 25              DEC     H                   
59D4: 84              ADD     A,H                 
59D5: 23              INC     HL                  
59D6: 21 27 26        LD      HL,$2627            
59D9: C5              PUSH    BC                  
59DA: 28 24           JR      Z,$5A00             ; {}
59DC: C3 32 23        JP      $2332               
59DF: 33              INC     SP                  
59E0: 25              DEC     H                   
59E1: 82              ADD     A,D                 
59E2: 34              INC     (HL)                
59E3: 21 36 26        LD      HL,$2636            
59E6: C3 37 24        JP      $2437               
59E9: 43              LD      B,E                 
59EA: 23              INC     HL                  
59EB: 82              ADD     A,D                 
59EC: 44              LD      B,H                 
59ED: 1C              INC     E                   
59EE: 46              LD      B,(HL)              
59EF: 24              INC     H                   
59F0: 53              LD      D,E                 
59F1: 27              DAA                         
59F2: 82              ADD     A,D                 
59F3: 54              LD      D,H                 
59F4: 22              LD      (HLI),A             
59F5: 56              LD      D,(HL)              
59F6: 28 60           JR      Z,$5A58             ; {}
59F8: 29              ADD     HL,HL               
59F9: 62              LD      H,D                 
59FA: 27              DAA                         
59FB: 63              LD      H,E                 
59FC: 2B              DEC     HL                  
59FD: 82              ADD     A,D                 
59FE: 64              LD      H,H                 
59FF: 0D              DEC     C                   
5A00: 66              LD      H,(HL)              
5A01: 2C              INC     L                   
5A02: 67              LD      H,A                 
5A03: 28 69           JR      Z,$5A6E             ; {}
5A05: 2A              LD      A,(HLI)             
5A06: 70              LD      (HL),B              
5A07: 21 71 29        LD      HL,$2971            
5A0A: 72              LD      (HL),D              
5A0B: AC              XOR     H                   
5A0C: 73              LD      (HL),E              
5A0D: 23              INC     HL                  
5A0E: 82              ADD     A,D                 
5A0F: 74              LD      (HL),H              
5A10: 0D              DEC     C                   
5A11: 76              HALT                        
5A12: 24              INC     H                   
5A13: 77              LD      (HL),A              
5A14: AC              XOR     H                   
5A15: 78              LD      A,B                 
5A16: 2A              LD      A,(HLI)             
5A17: 79              LD      A,C                 
5A18: 21 E1 08        LD      HL,$08E1            
5A1B: 74              LD      (HL),H              
5A1C: 48              LD      C,B                 
5A1D: 70              LD      (HL),B              
5A1E: FE 04           CP      $04                 
5A20: 0D              DEC     C                   
5A21: 00              NOP                         
5A22: 00              NOP                         
5A23: 01 25 08        LD      BC,$0825            
5A26: 26 09           LD      H,$09               
5A28: 00              NOP                         
5A29: 10 25           ;;STOP    $25                 
5A2B: 11 29 18        LD      DE,$1829            
5A2E: 2A              LD      A,(HLI)             
5A2F: 19              ADD     HL,DE               
5A30: 26 60           LD      H,$60               
5A32: 27              DAA                         
5A33: 61              LD      H,C                 
5A34: 2B              DEC     HL                  
5A35: 68              LD      L,B                 
5A36: 2C              INC     L                   
5A37: 69              LD      L,C                 
5A38: 28 70           JR      Z,$5AAA             ; {}
5A3A: 00              NOP                         
5A3B: 71              LD      (HL),C              
5A3C: 27              DAA                         
5A3D: 78              LD      A,B                 
5A3E: 28 79           JR      Z,$5AB9             ; {}
5A40: 00              NOP                         
5A41: 34              INC     (HL)                
5A42: E7              RST     0X20                
5A43: 35              DEC     (HL)                
5A44: E8 44           ADD     SP,$44              
5A46: E9              JP      (HL)                
5A47: 45              LD      B,L                 
5A48: EA FE 04        LD      ($04FE),A           
5A4B: 0F              RRCA                        
5A4C: 00              NOP                         
5A4D: 00              NOP                         
5A4E: 01 25 03        LD      BC,$0325            
5A51: 29              ADD     HL,HL               
5A52: 82              ADD     A,D                 
5A53: 04              INC     B                   
5A54: 0F              RRCA                        
5A55: 06 2A           LD      B,$2A               
5A57: 08 26 09        LD      ($0926),SP          
5A5A: 00              NOP                         
5A5B: 10 25           ;;STOP    $25                 
5A5D: 11 29 18        LD      DE,$1829            
5A60: 2A              LD      A,(HLI)             
5A61: 19              ADD     HL,DE               
5A62: 26 60           LD      H,$60               
5A64: 27              DAA                         
5A65: 61              LD      H,C                 
5A66: 2B              DEC     HL                  
5A67: 68              LD      L,B                 
5A68: 2C              INC     L                   
5A69: 69              LD      L,C                 
5A6A: 28 70           JR      Z,$5ADC             ; {}
5A6C: 00              NOP                         
5A6D: 71              LD      (HL),C              
5A6E: 27              DAA                         
5A6F: 78              LD      A,B                 
5A70: 28 79           JR      Z,$5AEB             ; {}
5A72: 00              NOP                         
5A73: 86              ADD     A,(HL)              
5A74: 12              LD      (DE),A              
5A75: 1C              INC     E                   
5A76: 88              ADC     A,B                 
5A77: 21 1C 88        LD      HL,$881C            
5A7A: 31 1C 88        LD      SP,$881C            
5A7D: 41              LD      B,C                 
5A7E: 1C              INC     E                   
5A7F: 88              ADC     A,B                 
5A80: 51              LD      D,C                 
5A81: 1C              INC     E                   
5A82: 86              ADD     A,(HL)              
5A83: 62              LD      H,D                 
5A84: 1C              INC     E                   
5A85: 82              ADD     A,D                 
5A86: 54              LD      D,H                 
5A87: 1C              INC     E                   
5A88: 82              ADD     A,D                 
5A89: 64              LD      H,H                 
5A8A: 0F              RRCA                        
5A8B: 32              LD      (HLD),A             
5A8C: AB              XOR     E                   
5A8D: 37              SCF                         
5A8E: AB              XOR     E                   
5A8F: 73              LD      (HL),E              
5A90: 2B              DEC     HL                  
5A91: 82              ADD     A,D                 
5A92: 74              LD      (HL),H              
5A93: 0F              RRCA                        
5A94: 76              HALT                        
5A95: 2C              INC     L                   
5A96: E1              POP     HL                  
5A97: 08 71 48        LD      ($4871),SP          ; {}
5A9A: 40              LD      B,B                 
5A9B: FE 04           CP      $04                 
5A9D: 95              SUB     L                   
5A9E: 00              NOP                         
5A9F: 25              DEC     H                   
5AA0: 88              ADC     A,B                 
5AA1: 01 21 09        LD      BC,$0921            
5AA4: 26 10           LD      H,$10               
5AA6: 29              ADD     HL,HL               
5AA7: 11 AC 18        LD      DE,$18AC            
5AAA: AC              XOR     H                   
5AAB: 19              ADD     HL,DE               
5AAC: 2A              LD      A,(HLI)             
5AAD: 20 AC           JR      NZ,$5A5B            ; {}
5AAF: 29              ADD     HL,HL               
5AB0: AC              XOR     H                   
5AB1: 21 25 22        LD      HL,$2225            
5AB4: 21 23 26        LD      HL,$2623            
5AB7: 26 25           LD      H,$25               
5AB9: 27              DAA                         
5ABA: 21 28 26        LD      HL,$2628            
5ABD: 29              ADD     HL,HL               
5ABE: AC              XOR     H                   
5ABF: 30 25           JR      NC,$5AE6            ; {}
5AC1: 31 29 33        LD      SP,$3329            
5AC4: 24              INC     H                   
5AC5: 36 23           LD      (HL),$23            
5AC7: 38 2A           JR      C,$5AF3             ; {}
5AC9: 39              ADD     HL,SP               
5ACA: 21 C4 40        LD      HL,$40C4            
5ACD: 23              INC     HL                  
5ACE: 43              LD      B,E                 
5ACF: 2A              LD      A,(HLI)             
5AD0: 82              ADD     A,D                 
5AD1: 44              LD      B,H                 
5AD2: 97              SUB     A                   
5AD3: 46              LD      B,(HL)              
5AD4: 29              ADD     HL,HL               
5AD5: 51              LD      D,C                 
5AD6: 2C              INC     L                   
5AD7: 52              LD      D,D                 
5AD8: 22              LD      (HLI),A             
5AD9: 53              LD      D,E                 
5ADA: 2B              DEC     HL                  
5ADB: 61              LD      H,C                 
5ADC: 2A              LD      A,(HLI)             
5ADD: 62              LD      H,D                 
5ADE: 26 63           LD      H,$63               
5AE0: 27              DAA                         
5AE1: 64              LD      H,H                 
5AE2: 22              LD      (HLI),A             
5AE3: 65              LD      H,L                 
5AE4: 2B              DEC     HL                  
5AE5: 69              LD      L,C                 
5AE6: 2C              INC     L                   
5AE7: 72              LD      (HL),D              
5AE8: 24              INC     H                   
5AE9: 82              ADD     A,D                 
5AEA: 74              LD      (HL),H              
5AEB: DF              RST     0X18                
5AEC: 75              LD      (HL),L              
5AED: 27              DAA                         
5AEE: 84              ADD     A,H                 
5AEF: 76              HALT                        
5AF0: 22              LD      (HLI),A             
5AF1: 79              LD      A,C                 
5AF2: 28 32           JR      Z,$5B26             ; {}
5AF4: 01 37 B0        LD      BC,$B037            
5AF7: 82              ADD     A,D                 
5AF8: 41              LD      B,C                 
5AF9: B0              OR      B                   
5AFA: 57              LD      D,A                 
5AFB: AE              XOR     (HL)                
5AFC: 68              LD      L,B                 
5AFD: AE              XOR     (HL)                
5AFE: FE 04           CP      $04                 
5B00: 05              DEC     B                   
5B01: 00              NOP                         
5B02: DF              RST     0X18                
5B03: 01 25 03        LD      BC,$0325            
5B06: C7              RST     0X00                
5B07: 06 C7           LD      B,$C7               
5B09: 08 26 09        LD      ($0926),SP          
5B0C: DF              RST     0X18                
5B0D: 10 25           ;;STOP    $25                 
5B0F: 11 29 18        LD      DE,$1829            
5B12: 2A              LD      A,(HLI)             
5B13: 19              ADD     HL,DE               
5B14: 26 30           LD      H,$30               
5B16: 29              ADD     HL,HL               
5B17: 34              INC     (HL)                
5B18: 2C              INC     L                   
5B19: 35              DEC     (HL)                
5B1A: 2B              DEC     HL                  
5B1B: C2 40 05        JP      NZ,$0540            
5B1E: C3 44 24        JP      $2444               
5B21: C4 45 23        CALL    NZ,$2345            
5B24: 60              LD      H,B                 
5B25: 22              LD      (HLI),A             
5B26: 61              LD      H,C                 
5B27: 2B              DEC     HL                  
5B28: 68              LD      L,B                 
5B29: 2C              INC     L                   
5B2A: 69              LD      L,C                 
5B2B: 28 70           JR      Z,$5B9D             ; {}
5B2D: DF              RST     0X18                
5B2E: 71              LD      (HL),C              
5B2F: 27              DAA                         
5B30: 74              LD      (HL),H              
5B31: 28 76           JR      Z,$5BA9             ; {}
5B33: 05              DEC     B                   
5B34: 77              LD      (HL),A              
5B35: 2C              INC     L                   
5B36: 78              LD      A,B                 
5B37: 28 79           JR      Z,$5BB2             ; {}
5B39: 0D              DEC     C                   
5B3A: 86              ADD     A,(HL)              
5B3B: 12              LD      (DE),A              
5B3C: AF              XOR     A                   
5B3D: 21 AF 28        LD      HL,$28AF            
5B40: AF              XOR     A                   
5B41: 31 B0 86        LD      SP,$86B0            
5B44: 22              LD      (HLI),A             
5B45: 01 C3 32        LD      BC,$32C3            
5B48: 01 C3 33        LD      BC,$33C3            
5B4B: 01 83 36        LD      BC,$3683            
5B4E: 01 83 46        LD      BC,$4683            
5B51: 01 83 56        LD      BC,$5683            
5B54: B0              OR      B                   
5B55: 82              ADD     A,D                 
5B56: 62              LD      H,D                 
5B57: B0              OR      B                   
5B58: FE 04           CP      $04                 
5B5A: 95              SUB     L                   
5B5B: C2 00 23        JP      NZ,$2300            
5B5E: 02              LD      (BC),A              
5B5F: 2A              LD      A,(HLI)             
5B60: 03              INC     BC                  
5B61: 26 82           LD      H,$82               
5B63: 04              INC     B                   
5B64: DF              RST     0X18                
5B65: 82              ADD     A,D                 
5B66: 06 0D           LD      B,$0D               
5B68: 08 00 09        LD      ($0900),SP          
5B6B: DF              RST     0X18                
5B6C: 10 C9           ;;STOP    $C9                 
5B6E: 13              INC     DE                  
5B6F: 2A              LD      A,(HLI)             
5B70: 14              INC     D                   
5B71: 21 15 26        LD      HL,$2615            
5B74: 82              ADD     A,D                 
5B75: 16 DF           LD      D,$DF               
5B77: 82              ADD     A,D                 
5B78: 18 0D           JR      $5B87               ; {}
5B7A: 20 27           JR      NZ,$5BA3            ; {}
5B7C: 21 2B 25        LD      HL,$252B            
5B7F: 2A              LD      A,(HLI)             
5B80: 26 21           LD      H,$21               
5B82: 27              DAA                         
5B83: 26 82           LD      H,$82               
5B85: 28 DF           JR      Z,$5B66             ; {}
5B87: 30 DF           JR      NC,$5B68            ; {}
5B89: 31 27 32        LD      SP,$3227            
5B8C: 2B              DEC     HL                  
5B8D: 37              SCF                         
5B8E: 2A              LD      A,(HLI)             
5B8F: 38 21           JR      C,$5BB2             ; {}
5B91: 39              ADD     HL,SP               
5B92: 26 40           LD      H,$40               
5B94: 0D              DEC     C                   
5B95: 41              LD      B,C                 
5B96: DF              RST     0X18                
5B97: 42              LD      B,D                 
5B98: 27              DAA                         
5B99: 43              LD      B,E                 
5B9A: 2B              DEC     HL                  
5B9B: 49              LD      C,C                 
5B9C: 2A              LD      A,(HLI)             
5B9D: 82              ADD     A,D                 
5B9E: 50              LD      D,B                 
5B9F: 0D              DEC     C                   
5BA0: 52              LD      D,D                 
5BA1: DF              RST     0X18                
5BA2: 53              LD      D,E                 
5BA3: 27              DAA                         
5BA4: 54              LD      D,H                 
5BA5: 22              LD      (HLI),A             
5BA6: 55              LD      D,L                 
5BA7: 2B              DEC     HL                  
5BA8: 60              LD      H,B                 
5BA9: 00              NOP                         
5BAA: 82              ADD     A,D                 
5BAB: 61              LD      H,C                 
5BAC: 0D              DEC     C                   
5BAD: 82              ADD     A,D                 
5BAE: 63              LD      H,E                 
5BAF: DF              RST     0X18                
5BB0: 65              LD      H,L                 
5BB1: 27              DAA                         
5BB2: 84              ADD     A,H                 
5BB3: 66              LD      H,(HL)              
5BB4: 22              LD      (HLI),A             
5BB5: 67              LD      H,A                 
5BB6: C8              RET     Z                   
5BB7: 82              ADD     A,D                 
5BB8: 70              LD      (HL),B              
5BB9: 00              NOP                         
5BBA: 83              ADD     A,E                 
5BBB: 72              LD      (HL),D              
5BBC: 0D              DEC     C                   
5BBD: 85              ADD     A,L                 
5BBE: 75              LD      (HL),L              
5BBF: DF              RST     0X18                
5BC0: 24              INC     H                   
5BC1: AE              XOR     (HL)                
5BC2: 35              DEC     (HL)                
5BC3: AE              XOR     (HL)                
5BC4: 36 AF           LD      (HL),$AF            
5BC6: 46              LD      B,(HL)              
5BC7: B0              OR      B                   
5BC8: 82              ADD     A,D                 
5BC9: 47              LD      B,A                 
5BCA: AE              XOR     (HL)                
5BCB: FE 04           CP      $04                 
5BCD: 05              DEC     B                   
5BCE: 02              LD      (BC),A              
5BCF: C7              RST     0X00                
5BD0: 05              DEC     B                   
5BD1: 29              ADD     HL,HL               
5BD2: 07              RLCA                        
5BD3: 2A              LD      A,(HLI)             
5BD4: 08 C7 82        LD      ($82C7),SP          
5BD7: 17              RLA                         
5BD8: A6              AND     (HL)                
5BD9: 82              ADD     A,D                 
5BDA: 22              LD      (HLI),A             
5BDB: A7              AND     A                   
5BDC: 82              ADD     A,D                 
5BDD: 25              DEC     H                   
5BDE: A7              AND     A                   
5BDF: 28 A6           JR      Z,$5B87             ; {}
5BE1: 82              ADD     A,D                 
5BE2: 33              INC     SP                  
5BE3: A7              AND     A                   
5BE4: 37              SCF                         
5BE5: A7              AND     A                   
5BE6: 83              ADD     A,E                 
5BE7: 44              LD      B,H                 
5BE8: A7              AND     A                   
5BE9: 83              ADD     A,E                 
5BEA: 52              LD      D,D                 
5BEB: A7              AND     A                   
5BEC: 40              LD      B,B                 
5BED: 29              ADD     HL,HL               
5BEE: 49              LD      C,C                 
5BEF: 2A              LD      A,(HLI)             
5BF0: 60              LD      H,B                 
5BF1: 2B              DEC     HL                  
5BF2: 68              LD      L,B                 
5BF3: 2C              INC     L                   
5BF4: 69              LD      L,C                 
5BF5: 22              LD      (HLI),A             
5BF6: 70              LD      (HL),B              
5BF7: 27              DAA                         
5BF8: 72              LD      (HL),D              
5BF9: C8              RET     Z                   
5BFA: 77              LD      (HL),A              
5BFB: C8              RET     Z                   
5BFC: 78              LD      A,B                 
5BFD: 28 79           JR      Z,$5C78             ; {}
5BFF: DF              RST     0X18                
5C00: 11 AF 13        LD      DE,$13AF            
5C03: AE              XOR     (HL)                
5C04: 14              INC     D                   
5C05: AF              XOR     A                   
5C06: 21 01 24        LD      HL,$2401            
5C09: B0              OR      B                   
5C0A: 31 B0 32        LD      SP,$32B0            
5C0D: AF              XOR     A                   
5C0E: 82              ADD     A,D                 
5C0F: 35              DEC     (HL)                
5C10: AE              XOR     (HL)                
5C11: 42              LD      B,D                 
5C12: B0              OR      B                   
5C13: 43              LD      B,E                 
5C14: AE              XOR     (HL)                
5C15: 47              LD      B,A                 
5C16: AE              XOR     (HL)                
5C17: 56              LD      D,(HL)              
5C18: AE              XOR     (HL)                
5C19: 06 05           LD      B,$05               
5C1B: 50              LD      D,B                 
5C1C: 05              DEC     B                   
5C1D: 59              LD      E,C                 
5C1E: 05              DEC     B                   
5C1F: FE 04           CP      $04                 
5C21: 95              SUB     L                   
5C22: 00              NOP                         
5C23: 0D              DEC     C                   
5C24: 86              ADD     A,(HL)              
5C25: 01 DF 82        LD      BC,$82DF            
5C28: 07              RLCA                        
5C29: 0D              DEC     C                   
5C2A: 09              ADD     HL,BC               
5C2B: 00              NOP                         
5C2C: 10 DF           ;;STOP    $DF                 
5C2E: 11 25 84        LD      DE,$8425            
5C31: 12              LD      (DE),A              
5C32: 21 16 26        LD      HL,$2616            
5C35: 17              RLA                         
5C36: DF              RST     0X18                
5C37: 18 0D           JR      $5C46               ; {}
5C39: C6 19           ADD     $19                 
5C3B: 0D              DEC     C                   
5C3C: 20 25           JR      NZ,$5C63            ; {}
5C3E: 21 29 26        LD      HL,$2629            
5C41: 2A              LD      A,(HLI)             
5C42: 27              DAA                         
5C43: 26 C5           LD      H,$C5               
5C45: 28 DF           JR      Z,$5C26             ; {}
5C47: 30 23           JR      NC,$5C6C            ; {}
5C49: C5              PUSH    BC                  
5C4A: 37              SCF                         
5C4B: 24              INC     H                   
5C4C: 40              LD      B,B                 
5C4D: 29              ADD     HL,HL               
5C4E: 42              LD      B,D                 
5C4F: 2C              INC     L                   
5C50: 43              LD      B,E                 
5C51: 22              LD      (HLI),A             
5C52: 44              LD      B,H                 
5C53: 2B              DEC     HL                  
5C54: 52              LD      D,D                 
5C55: 24              INC     H                   
5C56: C2 53 DF        JP      NZ,$DF53            
5C59: C2 54 23        JP      NZ,$2354            
5C5C: 82              ADD     A,D                 
5C5D: 60              LD      H,B                 
5C5E: 22              LD      (HLI),A             
5C5F: 62              LD      H,D                 
5C60: 28 83           JR      Z,$5BE5             ; {}
5C62: 70              LD      (HL),B              
5C63: DF              RST     0X18                
5C64: 73              LD      (HL),E              
5C65: 0D              DEC     C                   
5C66: 74              LD      (HL),H              
5C67: 27              DAA                         
5C68: 77              LD      (HL),A              
5C69: 28 78           JR      Z,$5CE3             ; {}
5C6B: 0D              DEC     C                   
5C6C: 79              LD      A,C                 
5C6D: 00              NOP                         
5C6E: 75              LD      (HL),L              
5C6F: FD                              
5C70: E0 00           LD      ($FF00+$00),A       
5C72: 0A              LD      A,(BC)              
5C73: 78              LD      A,B                 
5C74: 70              LD      (HL),B              
5C75: FE 04           CP      $04                 
5C77: 3F              CCF                         
5C78: 00              NOP                         
5C79: 23              INC     HL                  
5C7A: 01 25 08        LD      BC,$0825            
5C7D: 26 09           LD      H,$09               
5C7F: 24              INC     H                   
5C80: C5              PUSH    BC                  
5C81: 11 23 C5        LD      DE,$C523            
5C84: 18 24           JR      $5CAA               ; {}
5C86: 61              LD      H,C                 
5C87: 27              DAA                         
5C88: 62              LD      H,D                 
5C89: 2B              DEC     HL                  
5C8A: 67              LD      H,A                 
5C8B: 2C              INC     L                   
5C8C: 68              LD      L,B                 
5C8D: 28 71           JR      Z,$5D00             ; {}
5C8F: 0D              DEC     C                   
5C90: 72              LD      (HL),D              
5C91: 27              DAA                         
5C92: 84              ADD     A,H                 
5C93: 73              LD      (HL),E              
5C94: 22              LD      (HLI),A             
5C95: 77              LD      (HL),A              
5C96: 28 78           JR      Z,$5D10             ; {}
5C98: 0D              DEC     C                   
5C99: 03              INC     BC                  
5C9A: C7              RST     0X00                
5C9B: 06 C7           LD      B,$C7               
5C9D: 20 C9           JR      NZ,$5C68            ; {}
5C9F: 31 C9 51        LD      SP,$51C9            
5CA2: C9              RET                         
5CA3: 60              LD      H,B                 
5CA4: C9              RET                         
5CA5: 29              ADD     HL,HL               
5CA6: CA 38 CA        JP      Z,$CA38             
5CA9: 58              LD      E,B                 
5CAA: CA 69 CA        JP      Z,$CA69             
5CAD: 04              INC     B                   
5CAE: F0 74           LD      A,($74)             
5CB0: F1              POP     AF                  
5CB1: FE 0C           CP      $0C                 
5CB3: 95              SUB     L                   
5CB4: 82              ADD     A,D                 
5CB5: 00              NOP                         
5CB6: 0D              DEC     C                   
5CB7: 82              ADD     A,D                 
5CB8: 02              LD      (BC),A              
5CB9: DF              RST     0X18                
5CBA: 04              INC     B                   
5CBB: 25              DEC     H                   
5CBC: 85              ADD     A,L                 
5CBD: 05              DEC     B                   
5CBE: 21 C3 10        LD      HL,$10C3            
5CC1: 0D              DEC     C                   
5CC2: 11 DF 12        LD      DE,$12DF            
5CC5: 25              DEC     H                   
5CC6: 13              INC     DE                  
5CC7: 21 14 29        LD      HL,$2914            
5CCA: 21 25 22        LD      HL,$2225            
5CCD: 29              ADD     HL,HL               
5CCE: 26 2C           LD      H,$2C               
5CD0: 83              ADD     A,E                 
5CD1: 27              DAA                         
5CD2: 22              LD      (HLI),A             
5CD3: 31 23 34        LD      SP,$3423            
5CD6: 2C              INC     L                   
5CD7: 35              DEC     (HL)                
5CD8: 22              LD      (HLI),A             
5CD9: 36 28           LD      (HL),$28            
5CDB: 83              ADD     A,E                 
5CDC: 37              SCF                         
5CDD: DF              RST     0X18                
5CDE: 40              LD      B,B                 
5CDF: 25              DEC     H                   
5CE0: 41              LD      B,C                 
5CE1: 29              ADD     HL,HL               
5CE2: 43              LD      B,E                 
5CE3: 2C              INC     L                   
5CE4: 44              LD      B,H                 
5CE5: 28 82           JR      Z,$5C69             ; {}
5CE7: 45              LD      B,L                 
5CE8: DF              RST     0X18                
5CE9: 47              LD      B,A                 
5CEA: 25              DEC     H                   
5CEB: 82              ADD     A,D                 
5CEC: 48              LD      C,B                 
5CED: 21 C2 50        LD      HL,$50C2            
5CF0: 23              INC     HL                  
5CF1: C2 53 24        JP      NZ,$2453            
5CF4: 82              ADD     A,D                 
5CF5: 54              LD      D,H                 
5CF6: DF              RST     0X18                
5CF7: 56              LD      D,(HL)              
5CF8: 25              DEC     H                   
5CF9: 57              LD      D,A                 
5CFA: 29              ADD     HL,HL               
5CFB: C2 64 DF        JP      NZ,$DF64            
5CFE: C2 65 0D        JP      NZ,$0D65            
5D01: 66              LD      H,(HL)              
5D02: 23              INC     HL                  
5D03: 70              LD      (HL),B              
5D04: 27              DAA                         
5D05: 73              LD      (HL),E              
5D06: 28 76           JR      Z,$5D7E             ; {}
5D08: 27              DAA                         
5D09: 77              LD      (HL),A              
5D0A: C1              POP     BC                  
5D0B: 78              LD      A,B                 
5D0C: C2 79 22        JP      NZ,$2279            
5D0F: 71              LD      (HL),C              
5D10: FD                              
5D11: E0 00           LD      ($FF00+$00),A       
5D13: 1E 38           LD      E,$38               
5D15: 10 FE           ;;STOP    $FE                 
5D17: 0C              INC     C                   
5D18: 95              SUB     L                   
5D19: 8A              ADC     A,D                 
5D1A: 00              NOP                         
5D1B: 21 82 17        LD      HL,$1782            
5D1E: DF              RST     0X18                
5D1F: 8A              ADC     A,D                 
5D20: 20 22           JR      NZ,$5D44            ; {}
5D22: 89              ADC     A,C                 
5D23: 30 DF           JR      NC,$5D04            ; {}
5D25: 39              ADD     HL,SP               
5D26: 0D              DEC     C                   
5D27: 85              ADD     A,L                 
5D28: 40              LD      B,B                 
5D29: 21 45 26        LD      HL,$2645            
5D2C: 84              ADD     A,H                 
5D2D: 46              LD      B,(HL)              
5D2E: DF              RST     0X18                
5D2F: 55              LD      D,L                 
5D30: 2A              LD      A,(HLI)             
5D31: 56              LD      D,(HL)              
5D32: 26 83           LD      H,$83               
5D34: 57              LD      D,A                 
5D35: DF              RST     0X18                
5D36: 66              LD      H,(HL)              
5D37: 24              INC     H                   
5D38: 83              ADD     A,E                 
5D39: 67              LD      H,A                 
5D3A: DF              RST     0X18                
5D3B: 86              ADD     A,(HL)              
5D3C: 70              LD      (HL),B              
5D3D: 22              LD      (HLI),A             
5D3E: 76              HALT                        
5D3F: 28 83           JR      Z,$5CC4             ; {}
5D41: 77              LD      (HL),A              
5D42: DF              RST     0X18                
5D43: 64              LD      H,H                 
5D44: BE              CP      (HL)                
5D45: FE 0C           CP      $0C                 
5D47: 95              SUB     L                   
5D48: 85              ADD     A,L                 
5D49: 00              NOP                         
5D4A: 21 05 26        LD      HL,$2605            
5D4D: 06 0D           LD      B,$0D               
5D4F: 83              ADD     A,E                 
5D50: 07              RLCA                        
5D51: DF              RST     0X18                
5D52: 83              ADD     A,E                 
5D53: 11 DF 15        LD      DE,$15DF            
5D56: 2A              LD      A,(HLI)             
5D57: 16 21           LD      D,$21               
5D59: 17              RLA                         
5D5A: 26 82           LD      H,$82               
5D5C: 18 DF           JR      $5D3D               ; {}
5D5E: 83              ADD     A,E                 
5D5F: 20 22           JR      NZ,$5D83            ; {}
5D61: 23              INC     HL                  
5D62: 2B              DEC     HL                  
5D63: 24              INC     H                   
5D64: DF              RST     0X18                
5D65: 27              DAA                         
5D66: 24              INC     H                   
5D67: 28 0D           JR      Z,$5D76             ; {}
5D69: 29              ADD     HL,HL               
5D6A: DF              RST     0X18                
5D6B: 82              ADD     A,D                 
5D6C: 30 0D           JR      NC,$5D7B            ; {}
5D6E: 32              LD      (HLD),A             
5D6F: 00              NOP                         
5D70: 33              INC     SP                  
5D71: 27              DAA                         
5D72: 34              INC     (HL)                
5D73: 2B              DEC     HL                  
5D74: C2 35 DF        JP      NZ,$DF35            
5D77: 37              SCF                         
5D78: 2A              LD      A,(HLI)             
5D79: 38 26           JR      C,$5DA1             ; {}
5D7B: 39              ADD     HL,SP               
5D7C: 0D              DEC     C                   
5D7D: 40              LD      B,B                 
5D7E: DF              RST     0X18                
5D7F: 83              ADD     A,E                 
5D80: 41              LD      B,C                 
5D81: 0D              DEC     C                   
5D82: 44              LD      B,H                 
5D83: 23              INC     HL                  
5D84: C3 48 24        JP      $2448               
5D87: C2 49 DF        JP      NZ,$DF49            
5D8A: 82              ADD     A,D                 
5D8B: 50              LD      D,B                 
5D8C: DF              RST     0X18                
5D8D: C3 52 0D        JP      $0D52               
5D90: C3 53 00        JP      $0053               
5D93: 54              LD      D,H                 
5D94: 27              DAA                         
5D95: 55              LD      D,L                 
5D96: 2B              DEC     HL                  
5D97: 82              ADD     A,D                 
5D98: 60              LD      H,B                 
5D99: DF              RST     0X18                
5D9A: 64              LD      H,H                 
5D9B: 0D              DEC     C                   
5D9C: 65              LD      H,L                 
5D9D: 23              INC     HL                  
5D9E: C2 69 0D        JP      NZ,$0D69            
5DA1: 70              LD      (HL),B              
5DA2: DF              RST     0X18                
5DA3: 71              LD      (HL),C              
5DA4: 0D              DEC     C                   
5DA5: 82              ADD     A,D                 
5DA6: 73              LD      (HL),E              
5DA7: 00              NOP                         
5DA8: 75              LD      (HL),L              
5DA9: 27              DAA                         
5DAA: 78              LD      A,B                 
5DAB: 28 76           JR      Z,$5E23             ; {}
5DAD: FD                              
5DAE: E0 00           LD      ($FF00+$00),A       
5DB0: 1F              RRA                         
5DB1: 28 10           JR      Z,$5DC3             ; {}
5DB3: FE 0C           CP      $0C                 
5DB5: 95              SUB     L                   
5DB6: 82              ADD     A,D                 
5DB7: 00              NOP                         
5DB8: 0D              DEC     C                   
5DB9: 82              ADD     A,D                 
5DBA: 02              LD      (BC),A              
5DBB: DF              RST     0X18                
5DBC: 04              INC     B                   
5DBD: 25              DEC     H                   
5DBE: 85              ADD     A,L                 
5DBF: 05              DEC     B                   
5DC0: 21 C3 10        LD      HL,$10C3            
5DC3: 0D              DEC     C                   
5DC4: 11 DF 12        LD      DE,$12DF            
5DC7: 25              DEC     H                   
5DC8: 13              INC     DE                  
5DC9: 21 14 29        LD      HL,$2914            
5DCC: 21 25 22        LD      HL,$2225            
5DCF: 29              ADD     HL,HL               
5DD0: 26 2C           LD      H,$2C               
5DD2: 83              ADD     A,E                 
5DD3: 27              DAA                         
5DD4: 22              LD      (HLI),A             
5DD5: 31 23 34        LD      SP,$3423            
5DD8: 2C              INC     L                   
5DD9: 35              DEC     (HL)                
5DDA: 22              LD      (HLI),A             
5DDB: 36 28           LD      (HL),$28            
5DDD: 83              ADD     A,E                 
5DDE: 37              SCF                         
5DDF: DF              RST     0X18                
5DE0: 40              LD      B,B                 
5DE1: 25              DEC     H                   
5DE2: 41              LD      B,C                 
5DE3: 29              ADD     HL,HL               
5DE4: 43              LD      B,E                 
5DE5: 2C              INC     L                   
5DE6: 44              LD      B,H                 
5DE7: 28 82           JR      Z,$5D6B             ; {}
5DE9: 45              LD      B,L                 
5DEA: DF              RST     0X18                
5DEB: 47              LD      B,A                 
5DEC: 25              DEC     H                   
5DED: 82              ADD     A,D                 
5DEE: 48              LD      C,B                 
5DEF: 21 C2 50        LD      HL,$50C2            
5DF2: 23              INC     HL                  
5DF3: C2 53 24        JP      NZ,$2453            
5DF6: 82              ADD     A,D                 
5DF7: 54              LD      D,H                 
5DF8: DF              RST     0X18                
5DF9: 56              LD      D,(HL)              
5DFA: 25              DEC     H                   
5DFB: 57              LD      D,A                 
5DFC: 29              ADD     HL,HL               
5DFD: C2 64 DF        JP      NZ,$DF64            
5E00: C2 65 0D        JP      NZ,$0D65            
5E03: 66              LD      H,(HL)              
5E04: 23              INC     HL                  
5E05: 70              LD      (HL),B              
5E06: 27              DAA                         
5E07: 71              LD      (HL),C              
5E08: C1              POP     BC                  
5E09: 72              LD      (HL),D              
5E0A: C2 73 28        JP      NZ,$2873            
5E0D: 76              HALT                        
5E0E: 27              DAA                         
5E0F: 79              LD      A,C                 
5E10: 22              LD      (HLI),A             
5E11: 77              LD      (HL),A              
5E12: FD                              
5E13: E0 00           LD      ($FF00+$00),A       
5E15: 1E 78           LD      E,$78               
5E17: 10 FE           ;;STOP    $FE                 
5E19: 0C              INC     C                   
5E1A: 95              SUB     L                   
5E1B: 8A              ADC     A,D                 
5E1C: 00              NOP                         
5E1D: 21 82 17        LD      HL,$1782            
5E20: DF              RST     0X18                
5E21: 8A              ADC     A,D                 
5E22: 20 22           JR      NZ,$5E46            ; {}
5E24: 89              ADC     A,C                 
5E25: 30 DF           JR      NC,$5E06            ; {}
5E27: 39              ADD     HL,SP               
5E28: 0D              DEC     C                   
5E29: 85              ADD     A,L                 
5E2A: 40              LD      B,B                 
5E2B: 21 45 26        LD      HL,$2645            
5E2E: 84              ADD     A,H                 
5E2F: 46              LD      B,(HL)              
5E30: DF              RST     0X18                
5E31: 55              LD      D,L                 
5E32: 2A              LD      A,(HLI)             
5E33: 56              LD      D,(HL)              
5E34: 26 83           LD      H,$83               
5E36: 57              LD      D,A                 
5E37: DF              RST     0X18                
5E38: 66              LD      H,(HL)              
5E39: 24              INC     H                   
5E3A: 83              ADD     A,E                 
5E3B: 67              LD      H,A                 
5E3C: DF              RST     0X18                
5E3D: 86              ADD     A,(HL)              
5E3E: 70              LD      (HL),B              
5E3F: 22              LD      (HLI),A             
5E40: 76              HALT                        
5E41: 28 83           JR      Z,$5DC6             ; {}
5E43: 77              LD      (HL),A              
5E44: DF              RST     0X18                
5E45: 64              LD      H,H                 
5E46: BE              CP      (HL)                
5E47: E1              POP     HL                  
5E48: 0A              LD      A,(BC)              
5E49: 85              ADD     A,L                 
5E4A: 48              LD      C,B                 
5E4B: 40              LD      B,B                 
5E4C: FE 0C           CP      $0C                 
5E4E: 25              DEC     H                   
5E4F: 82              ADD     A,D                 
5E50: 00              NOP                         
5E51: 0D              DEC     C                   
5E52: 82              ADD     A,D                 
5E53: 02              LD      (BC),A              
5E54: DF              RST     0X18                
5E55: 04              INC     B                   
5E56: 25              DEC     H                   
5E57: 06 26           LD      B,$26               
5E59: 07              RLCA                        
5E5A: 2A              LD      A,(HLI)             
5E5B: 10 0D           ;;STOP    $0D                 
5E5D: 11 DF 12        LD      DE,$12DF            
5E60: 25              DEC     H                   
5E61: 13              INC     DE                  
5E62: 21 14 29        LD      HL,$2914            
5E65: 15              DEC     D                   
5E66: AF              XOR     A                   
5E67: 16 2A           LD      D,$2A               
5E69: 17              RLA                         
5E6A: 26 20           LD      H,$20               
5E6C: 0D              DEC     C                   
5E6D: 21 25 22        LD      HL,$2225            
5E70: 29              ADD     HL,HL               
5E71: 23              INC     HL                  
5E72: AE              XOR     (HL)                
5E73: 25              DEC     H                   
5E74: B0              OR      B                   
5E75: 26 AF           LD      H,$AF               
5E77: 27              DAA                         
5E78: 2A              LD      A,(HLI)             
5E79: 28 98           JR      Z,$5E13             ; {}
5E7B: 29              ADD     HL,HL               
5E7C: 21 30 25        LD      HL,$2530            
5E7F: 31 29 32        LD      SP,$3229            
5E82: AF              XOR     A                   
5E83: 36 01           LD      (HL),$01            
5E85: 42              LD      B,D                 
5E86: B0              OR      B                   
5E87: 43              LD      B,E                 
5E88: AF              XOR     A                   
5E89: 45              LD      B,L                 
5E8A: AF              XOR     A                   
5E8B: 46              LD      B,(HL)              
5E8C: B0              OR      B                   
5E8D: 83              ADD     A,E                 
5E8E: 53              LD      D,E                 
5E8F: B0              OR      B                   
5E90: 54              LD      D,H                 
5E91: AE              XOR     (HL)                
5E92: 60              LD      H,B                 
5E93: 27              DAA                         
5E94: 61              LD      H,C                 
5E95: 2B              DEC     HL                  
5E96: 66              LD      H,(HL)              
5E97: 2C              INC     L                   
5E98: 83              ADD     A,E                 
5E99: 67              LD      H,A                 
5E9A: 22              LD      (HLI),A             
5E9B: 70              LD      (HL),B              
5E9C: DF              RST     0X18                
5E9D: 71              LD      (HL),C              
5E9E: 27              DAA                         
5E9F: 76              HALT                        
5EA0: 28 83           JR      Z,$5E25             ; {}
5EA2: 77              LD      (HL),A              
5EA3: DF              RST     0X18                
5EA4: 34              INC     (HL)                
5EA5: CB E1           SET     1,E                 
5EA7: 0A              LD      A,(BC)              
5EA8: 84              ADD     A,H                 
5EA9: 48              LD      C,B                 
5EAA: 70              LD      (HL),B              
5EAB: FE 0C           CP      $0C                 
5EAD: 75              LD      (HL),L              
5EAE: 03              INC     BC                  
5EAF: 26 04           LD      H,$04               
5EB1: DF              RST     0X18                
5EB2: 05              DEC     B                   
5EB3: 25              DEC     H                   
5EB4: 07              RLCA                        
5EB5: 26 82           LD      H,$82               
5EB7: 08 DF 13        LD      ($13DF),SP          
5EBA: 2A              LD      A,(HLI)             
5EBB: 14              INC     D                   
5EBC: 21 15 29        LD      HL,$2915            
5EBF: 17              RLA                         
5EC0: 2A              LD      A,(HLI)             
5EC1: 18 26           JR      $5EE9               ; {}
5EC3: 19              ADD     HL,DE               
5EC4: DF              RST     0X18                
5EC5: 20 21           JR      NZ,$5EE8            ; {}
5EC7: 21 26 31        LD      HL,$3126            
5ECA: 2A              LD      A,(HLI)             
5ECB: 28 2A           JR      Z,$5EF7             ; {}
5ECD: 29              ADD     HL,HL               
5ECE: 26 32           LD      H,$32               
5ED0: 21 33 26        LD      HL,$2633            
5ED3: 43              LD      B,E                 
5ED4: 2A              LD      A,(HLI)             
5ED5: 82              ADD     A,D                 
5ED6: 44              LD      B,H                 
5ED7: 21 46 26        LD      HL,$2646            
5EDA: 82              ADD     A,D                 
5EDB: 54              LD      D,H                 
5EDC: AF              XOR     A                   
5EDD: 56              LD      D,(HL)              
5EDE: 2A              LD      A,(HLI)             
5EDF: 57              LD      D,A                 
5EE0: 26 60           LD      H,$60               
5EE2: 2B              DEC     HL                  
5EE3: 84              ADD     A,H                 
5EE4: 63              LD      H,E                 
5EE5: AF              XOR     A                   
5EE6: 82              ADD     A,D                 
5EE7: 64              LD      H,H                 
5EE8: 01 C2 67        LD      BC,$67C2            
5EEB: 24              INC     H                   
5EEC: 70              LD      (HL),B              
5EED: 27              DAA                         
5EEE: 71              LD      (HL),C              
5EEF: 22              LD      (HLI),A             
5EF0: 72              LD      (HL),D              
5EF1: 2B              DEC     HL                  
5EF2: 84              ADD     A,H                 
5EF3: 73              LD      (HL),E              
5EF4: 01 FE 0C        LD      BC,$0CFE            
5EF7: 15              DEC     D                   
5EF8: 00              NOP                         
5EF9: 2B              DEC     HL                  
5EFA: 02              LD      (BC),A              
5EFB: 27              DAA                         
5EFC: 03              INC     BC                  
5EFD: 2B              DEC     HL                  
5EFE: C5              PUSH    BC                  
5EFF: 04              INC     B                   
5F00: 01 C5 05        LD      BC,$05C5            
5F03: 01 06 2C        LD      BC,$2C06            
5F06: 07              RLCA                        
5F07: 28 11           JR      Z,$5F1A             ; {}
5F09: A6              AND     (HL)                
5F0A: C2 13 23        JP      NZ,$2313            
5F0D: C2 16 24        JP      NZ,$2416            
5F10: 28 A6           JR      Z,$5EB8             ; {}
5F12: 29              ADD     HL,HL               
5F13: 2A              LD      A,(HLI)             
5F14: 32              LD      (HLD),A             
5F15: 25              DEC     H                   
5F16: 33              INC     SP                  
5F17: 29              ADD     HL,HL               
5F18: 36 2A           LD      (HL),$2A            
5F1A: 82              ADD     A,D                 
5F1B: 37              SCF                         
5F1C: 21 39 26        LD      HL,$2639            
5F1F: C2 42 23        JP      NZ,$2342            
5F22: 43              LD      B,E                 
5F23: AE              XOR     (HL)                
5F24: 44              LD      B,H                 
5F25: B0              OR      B                   
5F26: 83              ADD     A,E                 
5F27: 46              LD      B,(HL)              
5F28: AF              XOR     A                   
5F29: 84              ADD     A,H                 
5F2A: 55              LD      D,L                 
5F2B: B0              OR      B                   
5F2C: 62              LD      H,D                 
5F2D: 27              DAA                         
5F2E: 63              LD      H,E                 
5F2F: 2B              DEC     HL                  
5F30: 68              LD      L,B                 
5F31: 2C              INC     L                   
5F32: 69              LD      L,C                 
5F33: 28 71           JR      Z,$5FA6             ; {}
5F35: 2B              DEC     HL                  
5F36: 72              LD      (HL),D              
5F37: DF              RST     0X18                
5F38: 73              LD      (HL),E              
5F39: 27              DAA                         
5F3A: 78              LD      A,B                 
5F3B: 28 79           JR      Z,$5FB6             ; {}
5F3D: DF              RST     0X18                
5F3E: 75              LD      (HL),L              
5F3F: FD                              
5F40: E0 00           LD      ($FF00+$00),A       
5F42: 1F              RRA                         
5F43: 58              LD      E,B                 
5F44: 40              LD      B,B                 
5F45: FE 0C           CP      $0C                 
5F47: 9D              SBC     L                   
5F48: 00              NOP                         
5F49: DF              RST     0X18                
5F4A: 03              INC     BC                  
5F4B: DF              RST     0X18                
5F4C: 04              INC     B                   
5F4D: 25              DEC     H                   
5F4E: 83              ADD     A,E                 
5F4F: 05              DEC     B                   
5F50: 21 08 26        LD      HL,$2608            
5F53: 09              ADD     HL,BC               
5F54: DF              RST     0X18                
5F55: 82              ADD     A,D                 
5F56: 11 DF 13        LD      DE,$13DF            
5F59: 25              DEC     H                   
5F5A: 14              INC     D                   
5F5B: 29              ADD     HL,HL               
5F5C: 83              ADD     A,E                 
5F5D: 15              DEC     D                   
5F5E: 1B              DEC     DE                  
5F5F: 18 2A           JR      $5F8B               ; {}
5F61: 19              ADD     HL,DE               
5F62: 26 C2           LD      H,$C2               
5F64: 22              LD      (HLI),A             
5F65: DF              RST     0X18                
5F66: C3 23 23        JP      $2323               
5F69: 85              ADD     A,L                 
5F6A: 24              INC     H                   
5F6B: 1B              DEC     DE                  
5F6C: 26 05           LD      H,$05               
5F6E: C3 29 24        JP      $2429               
5F71: 30 DF           JR      NC,$5F52            ; {}
5F73: 83              ADD     A,E                 
5F74: 40              LD      B,B                 
5F75: DF              RST     0X18                
5F76: 51              LD      D,C                 
5F77: DF              RST     0X18                
5F78: 53              LD      D,E                 
5F79: 27              DAA                         
5F7A: 54              LD      D,H                 
5F7B: 2B              DEC     HL                  
5F7C: 85              ADD     A,L                 
5F7D: 34              INC     (HL)                
5F7E: 1B              DEC     DE                  
5F7F: 83              ADD     A,E                 
5F80: 35              DEC     (HL)                
5F81: 05              DEC     B                   
5F82: 85              ADD     A,L                 
5F83: 44              LD      B,H                 
5F84: 1B              DEC     DE                  
5F85: 46              LD      B,(HL)              
5F86: 05              DEC     B                   
5F87: 51              LD      D,C                 
5F88: DF              RST     0X18                
5F89: 53              LD      D,E                 
5F8A: 27              DAA                         
5F8B: 54              LD      D,H                 
5F8C: 2B              DEC     HL                  
5F8D: 83              ADD     A,E                 
5F8E: 55              LD      D,L                 
5F8F: 1B              DEC     DE                  
5F90: 58              LD      E,B                 
5F91: 2C              INC     L                   
5F92: 59              LD      E,C                 
5F93: 28 83           JR      Z,$5F18             ; {}
5F95: 61              LD      H,C                 
5F96: DF              RST     0X18                
5F97: 64              LD      H,H                 
5F98: 27              DAA                         
5F99: 65              LD      H,L                 
5F9A: 2B              DEC     HL                  
5F9B: C2 66 1B        JP      NZ,$1B66            
5F9E: 67              LD      H,A                 
5F9F: 2C              INC     L                   
5FA0: 68              LD      L,B                 
5FA1: 28 69           JR      Z,$600C             ; {}
5FA3: DF              RST     0X18                
5FA4: 83              ADD     A,E                 
5FA5: 72              LD      (HL),D              
5FA6: DF              RST     0X18                
5FA7: 75              LD      (HL),L              
5FA8: 23              INC     HL                  
5FA9: 77              LD      (HL),A              
5FAA: 24              INC     H                   
5FAB: 82              ADD     A,D                 
5FAC: 78              LD      A,B                 
5FAD: DF              RST     0X18                
5FAE: 36 CB           LD      (HL),$CB            
5FB0: E1              POP     HL                  
5FB1: 0A              LD      A,(BC)              
5FB2: 8A              ADC     A,D                 
5FB3: 68              LD      L,B                 
5FB4: 60              LD      H,B                 
5FB5: FE 0C           CP      $0C                 
5FB7: 9D              SBC     L                   
5FB8: 00              NOP                         
5FB9: DF              RST     0X18                
5FBA: 04              INC     B                   
5FBB: 25              DEC     H                   
5FBC: 05              DEC     B                   
5FBD: 29              ADD     HL,HL               
5FBE: 06 1B           LD      B,$1B               
5FC0: C2 07 24        JP      NZ,$2407            
5FC3: 09              ADD     HL,BC               
5FC4: DF              RST     0X18                
5FC5: 82              ADD     A,D                 
5FC6: 10 DF           ;;STOP    $DF                 
5FC8: C2 14 23        JP      NZ,$2314            
5FCB: 82              ADD     A,D                 
5FCC: 15              DEC     D                   
5FCD: 1B              DEC     DE                  
5FCE: 21 DF C2        LD      HL,$C2DF            
5FD1: 25              DEC     H                   
5FD2: 1B              DEC     DE                  
5FD3: 26 2C           LD      H,$2C               
5FD5: 27              DAA                         
5FD6: 28 28           JR      Z,$6000             ; {}
5FD8: DF              RST     0X18                
5FD9: 32              LD      (HLD),A             
5FDA: 25              DEC     H                   
5FDB: 33              INC     SP                  
5FDC: 21 34 29        LD      HL,$2934            
5FDF: C2 36 24        JP      NZ,$2436            
5FE2: 82              ADD     A,D                 
5FE3: 37              SCF                         
5FE4: DF              RST     0X18                
5FE5: 38 DF           JR      C,$5FC6             ; {}
5FE7: 40              LD      B,B                 
5FE8: DF              RST     0X18                
5FE9: C3 42 23        JP      $2342               
5FEC: 83              ADD     A,E                 
5FED: 43              LD      B,E                 
5FEE: 1B              DEC     DE                  
5FEF: 47              LD      B,A                 
5FF0: DF              RST     0X18                
5FF1: 49              LD      C,C                 
5FF2: DF              RST     0X18                
5FF3: C2 51 DF        JP      NZ,$DF51            
5FF6: 82              ADD     A,D                 
5FF7: 53              LD      D,E                 
5FF8: 1B              DEC     DE                  
5FF9: 55              LD      D,L                 
5FFA: 2C              INC     L                   
5FFB: 56              LD      D,(HL)              
5FFC: 28 82           JR      Z,$5F80             ; {}
5FFE: 58              LD      E,B                 
5FFF: DF              RST     0X18                
6000: 82              ADD     A,D                 
6001: 63              LD      H,E                 
6002: 1B              DEC     DE                  
6003: 65              LD      H,L                 
6004: 24              INC     H                   
6005: 68              LD      L,B                 
6006: DF              RST     0X18                
6007: 82              ADD     A,D                 
6008: 70              LD      (HL),B              
6009: DF              RST     0X18                
600A: 72              LD      (HL),D              
600B: 27              DAA                         
600C: 75              LD      (HL),L              
600D: 28 82           JR      Z,$5F91             ; {}
600F: 76              HALT                        
6010: DF              RST     0X18                
6011: 73              LD      (HL),E              
6012: FD                              
6013: E0 00           LD      ($FF00+$00),A       
6015: 19              ADD     HL,DE               
6016: 88              ADC     A,B                 
6017: 40              LD      B,B                 
6018: FE 0C           CP      $0C                 
601A: 9D              SBC     L                   
601B: 83              ADD     A,E                 
601C: 01 DF 82        LD      BC,$82DF            
601F: 08 DF 84        LD      ($84DF),SP          
6022: 12              LD      (DE),A              
6023: DF              RST     0X18                
6024: 19              ADD     HL,DE               
6025: DF              RST     0X18                
6026: C3 20 DF        JP      $DF20               
6029: 22              LD      (HLI),A             
602A: DF              RST     0X18                
602B: 23              INC     HL                  
602C: 25              DEC     H                   
602D: 82              ADD     A,D                 
602E: 24              INC     H                   
602F: 21 26 26        LD      HL,$2626            
6032: 30 DF           JR      NC,$6013            ; {}
6034: 32              LD      (HLD),A             
6035: 25              DEC     H                   
6036: 33              INC     SP                  
6037: 29              ADD     HL,HL               
6038: 82              ADD     A,D                 
6039: 34              INC     (HL)                
603A: 05              DEC     B                   
603B: 36 2A           LD      (HL),$2A            
603D: 37              SCF                         
603E: 26 38           LD      H,$38               
6040: DF              RST     0X18                
6041: 41              LD      B,C                 
6042: 25              DEC     H                   
6043: 42              LD      B,D                 
6044: 29              ADD     HL,HL               
6045: 84              ADD     A,H                 
6046: 43              LD      B,E                 
6047: 05              DEC     B                   
6048: 47              LD      B,A                 
6049: 2A              LD      A,(HLI)             
604A: 48              LD      C,B                 
604B: 26 C2           LD      H,$C2               
604D: 49              LD      C,C                 
604E: DF              RST     0X18                
604F: 51              LD      D,C                 
6050: 23              INC     HL                  
6051: 86              ADD     A,(HL)              
6052: 52              LD      D,D                 
6053: 05              DEC     B                   
6054: 58              LD      E,B                 
6055: 24              INC     H                   
6056: 60              LD      H,B                 
6057: DF              RST     0X18                
6058: 61              LD      H,C                 
6059: 27              DAA                         
605A: 62              LD      H,D                 
605B: 2B              DEC     HL                  
605C: 84              ADD     A,H                 
605D: 63              LD      H,E                 
605E: 05              DEC     B                   
605F: 67              LD      H,A                 
6060: 2C              INC     L                   
6061: 68              LD      L,B                 
6062: 28 71           JR      Z,$60D5             ; {}
6064: DF              RST     0X18                
6065: 72              LD      (HL),D              
6066: 27              DAA                         
6067: 73              LD      (HL),E              
6068: 2B              DEC     HL                  
6069: 82              ADD     A,D                 
606A: 74              LD      (HL),H              
606B: 05              DEC     B                   
606C: 76              HALT                        
606D: 2C              INC     L                   
606E: 77              LD      (HL),A              
606F: 28 79           JR      Z,$60EA             ; {}
6071: DF              RST     0X18                
6072: 53              LD      D,E                 
6073: A0              AND     B                   
6074: 56              LD      D,(HL)              
6075: BE              CP      (HL)                
6076: E1              POP     HL                  
6077: 0A              LD      A,(BC)              
6078: 88              ADC     A,B                 
6079: 68              LD      L,B                 
607A: 40              LD      B,B                 
607B: FE 0C           CP      $0C                 
607D: 9D              SBC     L                   
607E: C2 02 DF        JP      NZ,$DF02            
6081: 10 DF           ;;STOP    $DF                 
6083: 82              ADD     A,D                 
6084: 20 DF           JR      NZ,$6065            ; {}
6086: 31 DF 40        LD      SP,$40DF            
6089: DF              RST     0X18                
608A: 42              LD      B,D                 
608B: DF              RST     0X18                
608C: 82              ADD     A,D                 
608D: 50              LD      D,B                 
608E: DF              RST     0X18                
608F: 62              LD      H,D                 
6090: DF              RST     0X18                
6091: 70              LD      (HL),B              
6092: DF              RST     0X18                
6093: 83              ADD     A,E                 
6094: 27              DAA                         
6095: DF              RST     0X18                
6096: 83              ADD     A,E                 
6097: 37              SCF                         
6098: DF              RST     0X18                
6099: 83              ADD     A,E                 
609A: 47              LD      B,A                 
609B: DF              RST     0X18                
609C: 83              ADD     A,E                 
609D: 67              LD      H,A                 
609E: DF              RST     0X18                
609F: C7              RST     0X00                
60A0: 03              INC     BC                  
60A1: 23              INC     HL                  
60A2: C7              RST     0X00                
60A3: 04              INC     B                   
60A4: 05              DEC     B                   
60A5: C7              RST     0X00                
60A6: 05              DEC     B                   
60A7: 05              DEC     B                   
60A8: C7              RST     0X00                
60A9: 06 24           LD      B,$24               
60AB: 73              LD      (HL),E              
60AC: 27              DAA                         
60AD: 76              HALT                        
60AE: 28 74           JR      Z,$6124             ; {}
60B0: FD                              
60B1: E0 00           LD      ($FF00+$00),A       
60B3: 0A              LD      A,(BC)              
60B4: 18 70           JR      $6126               ; {}
60B6: FE 0C           CP      $0C                 
60B8: 95              SUB     L                   
60B9: 83              ADD     A,E                 
60BA: 00              NOP                         
60BB: DF              RST     0X18                
60BC: C5              PUSH    BC                  
60BD: 03              INC     BC                  
60BE: 23              INC     HL                  
60BF: C3 05 24        JP      $2405               
60C2: C3 06 DF        JP      $DF06               
60C5: C2 09 0D        JP      NZ,$0D09            
60C8: 10 0D           ;;STOP    $0D                 
60CA: 11 DF C2        LD      DE,$C2DF            
60CD: 17              RLA                         
60CE: 0D              DEC     C                   
60CF: 82              ADD     A,D                 
60D0: 21 0D C3        LD      HL,$C30D            
60D3: 28 0D           JR      Z,$60E2             ; {}
60D5: 30 DF           JR      NC,$60B6            ; {}
60D7: 35              DEC     (HL)                
60D8: 2A              LD      A,(HLI)             
60D9: 36 26           LD      (HL),$26            
60DB: C2 37 DF        JP      NZ,$DF37            
60DE: 82              ADD     A,D                 
60DF: 40              LD      B,B                 
60E0: DF              RST     0X18                
60E1: 46              LD      B,(HL)              
60E2: 24              INC     H                   
60E3: C2 51 0D        JP      NZ,$0D51            
60E6: 52              LD      D,D                 
60E7: DF              RST     0X18                
60E8: 53              LD      D,E                 
60E9: 27              DAA                         
60EA: 54              LD      D,H                 
60EB: 2B              DEC     HL                  
60EC: 56              LD      D,(HL)              
60ED: 2A              LD      A,(HLI)             
60EE: 57              LD      D,A                 
60EF: 26 C2           LD      H,$C2               
60F1: 59              LD      E,C                 
60F2: DF              RST     0X18                
60F3: 64              LD      H,H                 
60F4: 23              INC     HL                  
60F5: 67              LD      H,A                 
60F6: 24              INC     H                   
60F7: 82              ADD     A,D                 
60F8: 72              LD      (HL),D              
60F9: DF              RST     0X18                
60FA: 74              LD      (HL),H              
60FB: 27              DAA                         
60FC: 77              LD      (HL),A              
60FD: 28 78           JR      Z,$6177             ; {}
60FF: DF              RST     0X18                
6100: 75              LD      (HL),L              
6101: FD                              
6102: E0 00           LD      ($FF00+$00),A       
6104: 1F              RRA                         
6105: 78              LD      A,B                 
6106: 10 FE           ;;STOP    $FE                 
6108: 0C              INC     C                   
6109: 9D              SBC     L                   
610A: 82              ADD     A,D                 
610B: 00              NOP                         
610C: DF              RST     0X18                
610D: 83              ADD     A,E                 
610E: 04              INC     B                   
610F: DF              RST     0X18                
6110: 82              ADD     A,D                 
6111: 08 DF C3        LD      ($C3DF),SP          
6114: 10 DF           ;;STOP    $DF                 
6116: C3 12 DF        JP      $DF12               
6119: C2 13 DF        JP      NZ,$DF13            
611C: C2 15 DF        JP      NZ,$DF15            
611F: C3 16 DF        JP      $DF16               
6122: C2 18 DF        JP      NZ,$DF18            
6125: C2 19 DF        JP      NZ,$DF19            
6128: 33              INC     SP                  
6129: 25              DEC     H                   
612A: 34              INC     (HL)                
612B: 21 35 26        LD      HL,$2635            
612E: C5              PUSH    BC                  
612F: 37              SCF                         
6130: DF              RST     0X18                
6131: 42              LD      B,D                 
6132: 25              DEC     H                   
6133: 43              LD      B,E                 
6134: 29              ADD     HL,HL               
6135: 44              LD      B,H                 
6136: 05              DEC     B                   
6137: 45              LD      B,L                 
6138: 2A              LD      A,(HLI)             
6139: 46              LD      B,(HL)              
613A: 26 82           LD      H,$82               
613C: 48              LD      C,B                 
613D: DF              RST     0X18                
613E: C3 51 DF        JP      $DF51               
6141: C2 52 23        JP      NZ,$2352            
6144: 83              ADD     A,E                 
6145: 53              LD      D,E                 
6146: 05              DEC     B                   
6147: C3 56 24        JP      $2456               
614A: C2 60 DF        JP      NZ,$DF60            
614D: 83              ADD     A,E                 
614E: 63              LD      H,E                 
614F: 05              DEC     B                   
6150: 82              ADD     A,D                 
6151: 68              LD      L,B                 
6152: DF              RST     0X18                
6153: 72              LD      (HL),D              
6154: 27              DAA                         
6155: 73              LD      (HL),E              
6156: 2B              DEC     HL                  
6157: 82              ADD     A,D                 
6158: 74              LD      (HL),H              
6159: 05              DEC     B                   
615A: 82              ADD     A,D                 
615B: 77              LD      (HL),A              
615C: DF              RST     0X18                
615D: 75              LD      (HL),L              
615E: 2C              INC     L                   
615F: 76              HALT                        
6160: 28 54           JR      Z,$61B6             ; {}
6162: CB E1           SET     1,E                 
6164: 0A              LD      A,(BC)              
6165: 9A              SBC     D                   
6166: 38 40           JR      C,$61A8             ; {}
6168: FE 0C           CP      $0C                 
616A: 25              DEC     H                   
616B: 83              ADD     A,E                 
616C: 00              NOP                         
616D: 00              NOP                         
616E: 03              INC     BC                  
616F: 25              DEC     H                   
6170: 10 00           ;;STOP    $00                 
6172: 11 25 12        LD      DE,$1225            
6175: 21 13 29        LD      HL,$2913            
6178: 20 25           JR      NZ,$619F            ; {}
617A: 21 29 60        LD      HL,$6029            
617D: 27              DAA                         
617E: 83              ADD     A,E                 
617F: 61              LD      H,C                 
6180: 22              LD      (HLI),A             
6181: 64              LD      H,H                 
6182: 2B              DEC     HL                  
6183: 84              ADD     A,H                 
6184: 70              LD      (HL),B              
6185: 00              NOP                         
6186: 74              LD      (HL),H              
6187: 27              DAA                         
6188: 79              LD      A,C                 
6189: 28 69           JR      Z,$61F4             ; {}
618B: 2C              INC     L                   
618C: 86              ADD     A,(HL)              
618D: 24              INC     H                   
618E: AF              XOR     A                   
618F: 86              ADD     A,(HL)              
6190: 34              INC     (HL)                
6191: 01 82 44        LD      BC,$4482            
6194: B0              OR      B                   
6195: 49              LD      C,C                 
6196: B0              OR      B                   
6197: 36 B0           LD      (HL),$B0            
6199: 38 B0           JR      C,$614B             ; {}
619B: C2 27 05        JP      NZ,$0527            
619E: 57              LD      D,A                 
619F: AE              XOR     (HL)                
61A0: 76              HALT                        
61A1: FD                              
61A2: E0 00           LD      ($FF00+$00),A       
61A4: 0F              RRCA                        
61A5: 48              LD      C,B                 
61A6: 50              LD      D,B                 
61A7: FE 04           CP      $04                 
61A9: 1D              DEC     E                   
61AA: 02              LD      (BC),A              
61AB: 25              DEC     H                   
61AC: 84              ADD     A,H                 
61AD: 03              INC     BC                  
61AE: 21 07 26        LD      HL,$2607            
61B1: 04              INC     B                   
61B2: F4                              
61B3: C2 12 23        JP      NZ,$2312            
61B6: 84              ADD     A,H                 
61B7: 13              INC     DE                  
61B8: 0F              RRCA                        
61B9: C2 17 24        JP      NZ,$2417            
61BC: 84              ADD     A,H                 
61BD: 23              INC     HL                  
61BE: 0F              RRCA                        
61BF: 32              LD      (HLD),A             
61C0: 27              DAA                         
61C1: 84              ADD     A,H                 
61C2: 33              INC     SP                  
61C3: 22              LD      (HLI),A             
61C4: 37              SCF                         
61C5: 28 82           JR      Z,$6149             ; {}
61C7: 34              INC     (HL)                
61C8: 97              SUB     A                   
61C9: C3 42 AC        JP      $AC42               
61CC: 43              LD      B,E                 
61CD: 20 46           JR      NZ,$6215            ; {}
61CF: 20 C3           JR      NZ,$6194            ; {}
61D1: 47              LD      B,A                 
61D2: AC              XOR     H                   
61D3: 53              LD      D,E                 
61D4: FC                              
61D5: E0 00           LD      ($FF00+$00),A       
61D7: AC              XOR     H                   
61D8: 58              LD      E,B                 
61D9: 40              LD      B,B                 
61DA: FE 0C           CP      $0C                 
61DC: 05              DEC     B                   
61DD: 49              LD      C,C                 
61DE: 3E C8           LD      A,$C8               
61E0: 00              NOP                         
61E1: 00              NOP                         
61E2: 01 00 82        LD      BC,$8200            
61E5: 02              LD      (BC),A              
61E6: 0D              DEC     C                   
61E7: 86              ADD     A,(HL)              
61E8: 04              INC     B                   
61E9: DF              RST     0X18                
61EA: 07              RLCA                        
61EB: 0D              DEC     C                   
61EC: 84              ADD     A,H                 
61ED: 11 0D 12        LD      DE,$120D            
61F0: 0D              DEC     C                   
61F1: 14              INC     D                   
61F2: 25              DEC     H                   
61F3: 83              ADD     A,E                 
61F4: 15              DEC     D                   
61F5: 21 18 26        LD      HL,$2618            
61F8: 19              ADD     HL,DE               
61F9: DF              RST     0X18                
61FA: C5              PUSH    BC                  
61FB: 21 0D 22        LD      HL,$220D            
61FE: DF              RST     0X18                
61FF: 23              INC     HL                  
6200: 25              DEC     H                   
6201: 24              INC     H                   
6202: 29              ADD     HL,HL               
6203: 82              ADD     A,D                 
6204: 25              DEC     H                   
6205: AE              XOR     (HL)                
6206: 27              DAA                         
6207: AF              XOR     A                   
6208: 28 2A           JR      Z,$6234             ; {}
620A: 29              ADD     HL,HL               
620B: 26 32           LD      H,$32               
620D: 25              DEC     H                   
620E: 33              INC     SP                  
620F: 29              ADD     HL,HL               
6210: 34              INC     (HL)                
6211: AE              XOR     (HL)                
6212: 37              SCF                         
6213: B0              OR      B                   
6214: 38 AF           JR      C,$61C5             ; {}
6216: C2 42 23        JP      NZ,$2342            
6219: 43              LD      B,E                 
621A: AF              XOR     A                   
621B: 48              LD      C,B                 
621C: 01 51 DF        LD      BC,$DF51            
621F: 53              LD      D,E                 
6220: B0              OR      B                   
6221: 54              LD      D,H                 
6222: AF              XOR     A                   
6223: 57              LD      D,A                 
6224: AF              XOR     A                   
6225: 58              LD      E,B                 
6226: B0              OR      B                   
6227: 62              LD      H,D                 
6228: 27              DAA                         
6229: 63              LD      H,E                 
622A: 2B              DEC     HL                  
622B: 64              LD      H,H                 
622C: B0              OR      B                   
622D: 82              ADD     A,D                 
622E: 65              LD      H,L                 
622F: AE              XOR     (HL)                
6230: 67              LD      H,A                 
6231: B0              OR      B                   
6232: 68              LD      L,B                 
6233: 2C              INC     L                   
6234: 69              LD      L,C                 
6235: 28 82           JR      Z,$61B9             ; {}
6237: 71              LD      (HL),C              
6238: 0D              DEC     C                   
6239: 73              LD      (HL),E              
623A: 27              DAA                         
623B: 78              LD      A,B                 
623C: 28 79           JR      Z,$62B7             ; {}
623E: DF              RST     0X18                
623F: 45              LD      B,L                 
6240: CB E1           SET     1,E                 
6242: 0A              LD      A,(BC)              
6243: 96              SUB     (HL)                
6244: 28 20           JR      Z,$6266             ; {}
6246: FE 0C           CP      $0C                 
6248: 95              SUB     L                   
6249: 8A              ADC     A,D                 
624A: 00              NOP                         
624B: DF              RST     0X18                
624C: 83              ADD     A,E                 
624D: 10 DF           ;;STOP    $DF                 
624F: 13              INC     DE                  
6250: 25              DEC     H                   
6251: 86              ADD     A,(HL)              
6252: 14              INC     D                   
6253: 21 20 DF        LD      HL,$DF20            
6256: 21 25 22        LD      HL,$2225            
6259: 21 23 29        LD      HL,$2923            
625C: 30 25           JR      NC,$6283            ; {}
625E: 31 29 40        LD      SP,$4029            
6261: 49              LD      C,C                 
6262: 41              LD      B,C                 
6263: 0D              DEC     C                   
6264: 50              LD      D,B                 
6265: 27              DAA                         
6266: 51              LD      D,C                 
6267: 2B              DEC     HL                  
6268: 60              LD      H,B                 
6269: DF              RST     0X18                
626A: 61              LD      H,C                 
626B: 27              DAA                         
626C: 62              LD      H,D                 
626D: 2B              DEC     HL                  
626E: 69              LD      L,C                 
626F: 2C              INC     L                   
6270: 82              ADD     A,D                 
6271: 70              LD      (HL),B              
6272: DF              RST     0X18                
6273: 72              LD      (HL),D              
6274: 23              INC     HL                  
6275: 78              LD      A,B                 
6276: 2C              INC     L                   
6277: 79              LD      A,C                 
6278: 28 FE           JR      Z,$6278             ; {}
627A: 0C              INC     C                   
627B: 95              SUB     L                   
627C: 00              NOP                         
627D: 0D              DEC     C                   
627E: 83              ADD     A,E                 
627F: 01 DF 82        LD      BC,$82DF            
6282: 04              INC     B                   
6283: 0D              DEC     C                   
6284: C2 06 00        JP      NZ,$0006            
6287: C8              RET     Z                   
6288: 07              RLCA                        
6289: 00              NOP                         
628A: C8              RET     Z                   
628B: 08 00 C8        LD      ($C800),SP          
628E: 09              ADD     HL,BC               
628F: 00              NOP                         
6290: 83              ADD     A,E                 
6291: 10 21           ;;STOP    $21                 
6293: 13              INC     DE                  
6294: 26 14           LD      H,$14               
6296: DF              RST     0X18                
6297: 15              DEC     D                   
6298: 0D              DEC     C                   
6299: 23              INC     HL                  
629A: 2A              LD      A,(HLI)             
629B: 24              INC     H                   
629C: 21 25 26        LD      HL,$2625            
629F: 26 0D           LD      H,$0D               
62A1: 35              DEC     (HL)                
62A2: 2A              LD      A,(HLI)             
62A3: 36 26           LD      (HL),$26            
62A5: C2 46 24        JP      NZ,$2446            
62A8: 60              LD      H,B                 
62A9: 2B              DEC     HL                  
62AA: 65              LD      H,L                 
62AB: 2C              INC     L                   
62AC: 66              LD      H,(HL)              
62AD: 28 70           JR      Z,$631F             ; {}
62AF: 27              DAA                         
62B0: 84              ADD     A,H                 
62B1: 71              LD      (HL),C              
62B2: 22              LD      (HLI),A             
62B3: 75              LD      (HL),L              
62B4: 28 76           JR      Z,$632C             ; {}
62B6: 0D              DEC     C                   
62B7: 72              LD      (HL),D              
62B8: FD                              
62B9: E0 00           LD      ($FF00+$00),A       
62BB: B8              CP      B                   
62BC: 78              LD      A,B                 
62BD: 60              LD      H,B                 
62BE: FE 0C           CP      $0C                 
62C0: 15              DEC     D                   
62C1: 00              NOP                         
62C2: DF              RST     0X18                
62C3: 01 25 02        LD      BC,$0225            
62C6: 29              ADD     HL,HL               
62C7: C4 08 24        CALL    NZ,$2408            
62CA: C2 09 DF        JP      NZ,$DF09            
62CD: 10 25           ;;STOP    $25                 
62CF: 11 29 C2        LD      DE,$C229            
62D2: 29              ADD     HL,HL               
62D3: 0D              DEC     C                   
62D4: 45              LD      B,L                 
62D5: 2C              INC     L                   
62D6: 82              ADD     A,D                 
62D7: 46              LD      B,(HL)              
62D8: 22              LD      (HLI),A             
62D9: 48              LD      C,B                 
62DA: 28 49           JR      Z,$6325             ; {}
62DC: 00              NOP                         
62DD: C2 55 24        JP      NZ,$2455            
62E0: 84              ADD     A,H                 
62E1: 56              LD      D,(HL)              
62E2: 00              NOP                         
62E3: 60              LD      H,B                 
62E4: 27              DAA                         
62E5: 61              LD      H,C                 
62E6: 2B              DEC     HL                  
62E7: 84              ADD     A,H                 
62E8: 66              LD      H,(HL)              
62E9: 00              NOP                         
62EA: 70              LD      (HL),B              
62EB: 0D              DEC     C                   
62EC: 71              LD      (HL),C              
62ED: 27              DAA                         
62EE: 75              LD      (HL),L              
62EF: 28 84           JR      Z,$6275             ; {}
62F1: 76              HALT                        
62F2: 00              NOP                         
62F3: 72              LD      (HL),D              
62F4: FD                              
62F5: E0 00           LD      ($FF00+$00),A       
62F7: C8              RET     Z                   
62F8: 28 50           JR      Z,$634A             ; {}
62FA: FE 0C           CP      $0C                 
62FC: 90              SUB     B                   
62FD: 05              DEC     B                   
62FE: 0D              DEC     C                   
62FF: 06 DF           LD      B,$DF               
6301: 07              RLCA                        
6302: 25              DEC     H                   
6303: 82              ADD     A,D                 
6304: 08 21 C3        LD      ($C321),SP          
6307: 15              DEC     D                   
6308: DF              RST     0X18                
6309: 16 25           LD      D,$25               
630B: 17              RLA                         
630C: 29              ADD     HL,HL               
630D: 82              ADD     A,D                 
630E: 18 0D           JR      $631D               ; {}
6310: 26 23           LD      H,$23               
6312: 82              ADD     A,D                 
6313: 27              DAA                         
6314: 0D              DEC     C                   
6315: 29              ADD     HL,HL               
6316: A6              AND     (HL)                
6317: 36 27           LD      (HL),$27            
6319: 37              SCF                         
631A: 2B              DEC     HL                  
631B: 82              ADD     A,D                 
631C: 38 0D           JR      C,$632B             ; {}
631E: C2 45 0D        JP      NZ,$0D45            
6321: 46              LD      B,(HL)              
6322: DF              RST     0X18                
6323: 47              LD      B,A                 
6324: 27              DAA                         
6325: 82              ADD     A,D                 
6326: 48              LD      C,B                 
6327: 22              LD      (HLI),A             
6328: 56              LD      D,(HL)              
6329: 0D              DEC     C                   
632A: 83              ADD     A,E                 
632B: 57              LD      D,A                 
632C: DF              RST     0X18                
632D: 65              LD      H,L                 
632E: DF              RST     0X18                
632F: 67              LD      H,A                 
6330: 0D              DEC     C                   
6331: 82              ADD     A,D                 
6332: 68              LD      L,B                 
6333: DF              RST     0X18                
6334: 76              HALT                        
6335: DF              RST     0X18                
6336: 82              ADD     A,D                 
6337: 77              LD      (HL),A              
6338: 0D              DEC     C                   
6339: 79              LD      A,C                 
633A: DF              RST     0X18                
633B: FE 0C           CP      $0C                 
633D: 95              SUB     L                   
633E: 8A              ADC     A,D                 
633F: 00              NOP                         
6340: 21 C3 10        LD      HL,$10C3            
6343: 0D              DEC     C                   
6344: 13              INC     DE                  
6345: AE              XOR     (HL)                
6346: 14              INC     D                   
6347: A7              AND     A                   
6348: 20 A6           JR      NZ,$62F0            ; {}
634A: 83              ADD     A,E                 
634B: 21 A7 25        LD      HL,$25A7            
634E: A7              AND     A                   
634F: 26 A6           LD      H,$A6               
6351: 27              DAA                         
6352: 2C              INC     L                   
6353: 82              ADD     A,D                 
6354: 28 22           JR      Z,$6378             ; {}
6356: 33              INC     SP                  
6357: A7              AND     A                   
6358: C3 34 A7        JP      $A734               
635B: C2 37 24        JP      NZ,$2437            
635E: 40              LD      B,B                 
635F: 2B              DEC     HL                  
6360: 82              ADD     A,D                 
6361: 48              LD      C,B                 
6362: 21 47 2A        LD      HL,$2A47            
6365: 50              LD      D,B                 
6366: 23              INC     HL                  
6367: 60              LD      H,B                 
6368: 27              DAA                         
6369: 61              LD      H,C                 
636A: 2B              DEC     HL                  
636B: 82              ADD     A,D                 
636C: 64              LD      H,H                 
636D: A6              AND     (HL)                
636E: 82              ADD     A,D                 
636F: 67              LD      H,A                 
6370: 0D              DEC     C                   
6371: 70              LD      (HL),B              
6372: DF              RST     0X18                
6373: 71              LD      (HL),C              
6374: 27              DAA                         
6375: 88              ADC     A,B                 
6376: 72              LD      (HL),D              
6377: 22              LD      (HLI),A             
6378: 76              HALT                        
6379: FD                              
637A: E0 00           LD      ($FF00+$00),A       
637C: B8              CP      B                   
637D: 58              LD      E,B                 
637E: 30 FE           JR      NC,$637E            ; {}
6380: 0C              INC     C                   
6381: 90              SUB     B                   
6382: 83              ADD     A,E                 
6383: 00              NOP                         
6384: 21 03 26        LD      HL,$2603            
6387: C7              RST     0X00                
6388: 04              INC     B                   
6389: DF              RST     0X18                
638A: 05              DEC     B                   
638B: 0D              DEC     C                   
638C: 82              ADD     A,D                 
638D: 10 05           ;;STOP    $05                 
638F: 13              INC     DE                  
6390: 24              INC     H                   
6391: C4 15 DF        CALL    NZ,$DF15            
6394: 83              ADD     A,E                 
6395: 20 22           JR      NZ,$63B9            ; {}
6397: 23              INC     HL                  
6398: 28 82           JR      Z,$631C             ; {}
639A: 30 05           JR      NC,$63A1            ; {}
639C: 32              LD      (HLD),A             
639D: A6              AND     (HL)                
639E: 33              INC     SP                  
639F: DF              RST     0X18                
63A0: 83              ADD     A,E                 
63A1: 40              LD      B,B                 
63A2: 21 41 98        LD      HL,$9841            
63A5: 43              LD      B,E                 
63A6: 26 82           LD      H,$82               
63A8: 50              LD      D,B                 
63A9: 05              DEC     B                   
63AA: 52              LD      D,D                 
63AB: 0D              DEC     C                   
63AC: 53              LD      D,E                 
63AD: 24              INC     H                   
63AE: C2 55 0D        JP      NZ,$0D55            
63B1: 82              ADD     A,D                 
63B2: 60              LD      H,B                 
63B3: 05              DEC     B                   
63B4: 62              LD      H,D                 
63B5: 2C              INC     L                   
63B6: 63              LD      H,E                 
63B7: 28 82           JR      Z,$633B             ; {}
63B9: 70              LD      (HL),B              
63BA: 22              LD      (HLI),A             
63BB: 72              LD      (HL),D              
63BC: 28 73           JR      Z,$6431             ; {}
63BE: DF              RST     0X18                
63BF: 74              LD      (HL),H              
63C0: 0D              DEC     C                   
63C1: 12              LD      (DE),A              
63C2: BE              CP      (HL)                
63C3: E1              POP     HL                  
63C4: 0A              LD      A,(BC)              
63C5: 90              SUB     B                   
63C6: 58              LD      E,B                 
63C7: 50              LD      D,B                 
63C8: FE 04           CP      $04                 
63CA: 05              DEC     B                   
63CB: 02              LD      (BC),A              
63CC: 26 03           LD      H,$03               
63CE: 2A              LD      A,(HLI)             
63CF: 06 29           LD      B,$29               
63D1: 07              RLCA                        
63D2: 25              DEC     H                   
63D3: C3 11 20        JP      $2011               
63D6: C2 12 24        JP      NZ,$2412            
63D9: C2 13 AC        JP      NZ,$AC13            
63DC: C3 14 0D        JP      $0D14               
63DF: C3 15 0D        JP      $0D15               
63E2: C2 16 AC        JP      NZ,$AC16            
63E5: C2 17 23        JP      NZ,$2317            
63E8: C3 18 20        JP      $2018               
63EB: 32              LD      (HLD),A             
63EC: 2A              LD      A,(HLI)             
63ED: 33              INC     SP                  
63EE: 26 36           LD      H,$36               
63F0: 25              DEC     H                   
63F1: 37              SCF                         
63F2: 29              ADD     HL,HL               
63F3: 43              LD      B,E                 
63F4: 2A              LD      A,(HLI)             
63F5: 82              ADD     A,D                 
63F6: 44              LD      B,H                 
63F7: 97              SUB     A                   
63F8: 46              LD      B,(HL)              
63F9: 29              ADD     HL,HL               
63FA: 60              LD      H,B                 
63FB: 27              DAA                         
63FC: 61              LD      H,C                 
63FD: 2B              DEC     HL                  
63FE: 68              LD      L,B                 
63FF: 2C              INC     L                   
6400: 69              LD      L,C                 
6401: 28 70           JR      Z,$6473             ; {}
6403: DF              RST     0X18                
6404: 71              LD      (HL),C              
6405: 27              DAA                         
6406: 73              LD      (HL),E              
6407: 2B              DEC     HL                  
6408: 82              ADD     A,D                 
6409: 74              LD      (HL),H              
640A: 05              DEC     B                   
640B: 76              HALT                        
640C: 2C              INC     L                   
640D: 78              LD      A,B                 
640E: 28 79           JR      Z,$6489             ; {}
6410: DF              RST     0X18                
6411: FE 04           CP      $04                 
6413: 05              DEC     B                   
6414: 03              INC     BC                  
6415: 29              ADD     HL,HL               
6416: 82              ADD     A,D                 
6417: 04              INC     B                   
6418: 05              DEC     B                   
6419: 06 2A           LD      B,$2A               
641B: C3 46 0D        JP      $0D46               
641E: 83              ADD     A,E                 
641F: 55              LD      D,L                 
6420: 0D              DEC     C                   
6421: 60              LD      H,B                 
6422: 27              DAA                         
6423: 61              LD      H,C                 
6424: 2B              DEC     HL                  
6425: 68              LD      L,B                 
6426: 2C              INC     L                   
6427: 69              LD      L,C                 
6428: 28 70           JR      Z,$649A             ; {}
642A: DF              RST     0X18                
642B: 71              LD      (HL),C              
642C: 27              DAA                         
642D: 78              LD      A,B                 
642E: 28 79           JR      Z,$64A9             ; {}
6430: DF              RST     0X18                
6431: 56              LD      D,(HL)              
6432: CB E0           SET     1,E                 
6434: 00              NOP                         
6435: E9              JP      (HL)                
6436: 68              LD      L,B                 
6437: 30 FE           JR      NC,$6437            ; {}
6439: 04              INC     B                   
643A: 91              SUB     C                   
643B: 84              ADD     A,H                 
643C: 43              LD      B,E                 
643D: 0D              DEC     C                   
643E: 84              ADD     A,H                 
643F: 53              LD      D,E                 
6440: 0D              DEC     C                   
6441: 84              ADD     A,H                 
6442: 63              LD      H,E                 
6443: 0D              DEC     C                   
6444: 32              LD      (HLD),A             
6445: 25              DEC     H                   
6446: 84              ADD     A,H                 
6447: 33              INC     SP                  
6448: 21 37 26        LD      HL,$2637            
644B: C3 42 23        JP      $2342               
644E: 72              LD      (HL),D              
644F: 27              DAA                         
6450: 84              ADD     A,H                 
6451: 73              LD      (HL),E              
6452: 22              LD      (HLI),A             
6453: C4 47 24        CALL    NZ,$2447            
6456: 34              INC     (HL)                
6457: 99              SBC     C                   
6458: 44              LD      B,H                 
6459: 9A              SBC     D                   
645A: 55              LD      D,L                 
645B: C0              RET     NZ                  
645C: 77              LD      (HL),A              
645D: 28 74           JR      Z,$64D3             ; {}
645F: FD                              
6460: E0 00           LD      ($FF00+$00),A       
6462: 11 68 32        LD      DE,$3268            
6465: FE 0C           CP      $0C                 
6467: 90              SUB     B                   
6468: 00              NOP                         
6469: 21 01 26        LD      HL,$2601            
646C: 10 05           ;;STOP    $05                 
646E: 11 2A 12        LD      DE,$122A            
6471: 21 13 26        LD      HL,$2613            
6474: 20 AF           JR      NZ,$6425            ; {}
6476: 82              ADD     A,D                 
6477: 21 05 23        LD      HL,$2305            
647A: 2A              LD      A,(HLI)             
647B: 24              INC     H                   
647C: 26 30           LD      H,$30               
647E: 01 82 31        LD      BC,$3182            
6481: 05              DEC     B                   
6482: C3 34 24        JP      $2434               
6485: 40              LD      B,B                 
6486: B0              OR      B                   
6487: 83              ADD     A,E                 
6488: 41              LD      B,C                 
6489: 05              DEC     B                   
648A: 84              ADD     A,H                 
648B: 50              LD      D,B                 
648C: 05              DEC     B                   
648D: 84              ADD     A,H                 
648E: 60              LD      H,B                 
648F: 22              LD      (HLI),A             
6490: 64              LD      H,H                 
6491: 28 33           JR      Z,$64C6             ; {}
6493: BE              CP      (HL)                
6494: E1              POP     HL                  
6495: 0A              LD      A,(BC)              
6496: 8D              ADC     A,L                 
6497: 48              LD      C,B                 
6498: 60              LD      H,B                 
6499: FE 04           CP      $04                 
649B: 91              SUB     C                   
649C: 84              ADD     A,H                 
649D: 43              LD      B,E                 
649E: 0D              DEC     C                   
649F: 84              ADD     A,H                 
64A0: 53              LD      D,E                 
64A1: 0D              DEC     C                   
64A2: 84              ADD     A,H                 
64A3: 63              LD      H,E                 
64A4: 0D              DEC     C                   
64A5: 32              LD      (HLD),A             
64A6: 25              DEC     H                   
64A7: 84              ADD     A,H                 
64A8: 33              INC     SP                  
64A9: 21 37 26        LD      HL,$2637            
64AC: C3 42 23        JP      $2342               
64AF: 72              LD      (HL),D              
64B0: 27              DAA                         
64B1: 84              ADD     A,H                 
64B2: 73              LD      (HL),E              
64B3: 22              LD      (HLI),A             
64B4: C4 47 24        CALL    NZ,$2447            
64B7: 34              INC     (HL)                
64B8: 99              SBC     C                   
64B9: 44              LD      B,H                 
64BA: 9A              SBC     D                   
64BB: 55              LD      D,L                 
64BC: C0              RET     NZ                  
64BD: 77              LD      (HL),A              
64BE: 28 74           JR      Z,$6534             ; {}
64C0: FD                              
64C1: E0 00           LD      ($FF00+$00),A       
64C3: 31 68 52        LD      SP,$5268            
64C6: FE 04           CP      $04                 
64C8: 91              SUB     C                   
64C9: 84              ADD     A,H                 
64CA: 43              LD      B,E                 
64CB: 0D              DEC     C                   
64CC: 84              ADD     A,H                 
64CD: 53              LD      D,E                 
64CE: 0D              DEC     C                   
64CF: 84              ADD     A,H                 
64D0: 63              LD      H,E                 
64D1: 0D              DEC     C                   
64D2: 32              LD      (HLD),A             
64D3: 25              DEC     H                   
64D4: 84              ADD     A,H                 
64D5: 33              INC     SP                  
64D6: 21 37 26        LD      HL,$2637            
64D9: C3 42 23        JP      $2342               
64DC: 72              LD      (HL),D              
64DD: 27              DAA                         
64DE: 84              ADD     A,H                 
64DF: 73              LD      (HL),E              
64E0: 22              LD      (HLI),A             
64E1: C4 47 24        CALL    NZ,$2447            
64E4: 34              INC     (HL)                
64E5: 99              SBC     C                   
64E6: 44              LD      B,H                 
64E7: 9A              SBC     D                   
64E8: 55              LD      D,L                 
64E9: C0              RET     NZ                  
64EA: 77              LD      (HL),A              
64EB: 28 74           JR      Z,$6561             ; {}
64ED: FD                              
64EE: E0 00           LD      ($FF00+$00),A       
64F0: 88              ADC     A,B                 
64F1: 58              LD      E,B                 
64F2: 52              LD      D,D                 
64F3: FE 04           CP      $04                 
64F5: 91              SUB     C                   
64F6: 84              ADD     A,H                 
64F7: 43              LD      B,E                 
64F8: 0D              DEC     C                   
64F9: 84              ADD     A,H                 
64FA: 53              LD      D,E                 
64FB: 0D              DEC     C                   
64FC: 84              ADD     A,H                 
64FD: 63              LD      H,E                 
64FE: 0D              DEC     C                   
64FF: 32              LD      (HLD),A             
6500: 25              DEC     H                   
6501: 84              ADD     A,H                 
6502: 33              INC     SP                  
6503: 21 37 26        LD      HL,$2637            
6506: C3 42 23        JP      $2342               
6509: 72              LD      (HL),D              
650A: 27              DAA                         
650B: 84              ADD     A,H                 
650C: 73              LD      (HL),E              
650D: 22              LD      (HLI),A             
650E: C4 47 24        CALL    NZ,$2447            
6511: 34              INC     (HL)                
6512: 99              SBC     C                   
6513: 44              LD      B,H                 
6514: 9A              SBC     D                   
6515: 55              LD      D,L                 
6516: C0              RET     NZ                  
6517: 77              LD      (HL),A              
6518: 28 74           JR      Z,$658E             ; {}
651A: FD                              
651B: E0 00           LD      ($FF00+$00),A       
651D: E8 38           ADD     SP,$38              
651F: 62              LD      H,D                 
6520: FE 0C           CP      $0C                 
6522: 0D              DEC     C                   
6523: 07              RLCA                        
6524: C7              RST     0X00                
6525: 02              LD      (BC),A              
6526: 99              SBC     C                   
6527: 12              LD      (DE),A              
6528: 9A              SBC     D                   
6529: 11 C5 21        LD      DE,$21C5            
652C: C6 C2           ADD     $C2                 
652E: 13              INC     DE                  
652F: 10 85           ;;STOP    $85                 
6531: 14              INC     D                   
6532: 1B              DEC     DE                  
6533: 85              ADD     A,L                 
6534: 24              INC     H                   
6535: 12              LD      (DE),A              
6536: 26 0D           LD      H,$0D               
6538: 31 13 33        LD      SP,$3313            
653B: 14              INC     D                   
653C: 74              LD      (HL),H              
653D: FD                              
653E: E0 00           LD      ($FF00+$00),A       
6540: 0A              LD      A,(BC)              
6541: 48              LD      C,B                 
6542: 22              LD      (HLI),A             
6543: FE 07           CP      $07                 
6545: 0D              DEC     C                   
6546: 88              ADC     A,B                 
6547: 11 00 C3        LD      DE,$C300            
654A: 22              LD      (HLI),A             
654B: 00              NOP                         
654C: C3 28 00        JP      $0028               
654F: 83              ADD     A,E                 
6550: 34              INC     (HL)                
6551: 00              NOP                         
6552: 02              LD      (BC),A              
6553: C7              RST     0X00                
6554: 07              RLCA                        
6555: C7              RST     0X00                
6556: 72              LD      (HL),D              
6557: C8              RET     Z                   
6558: 77              LD      (HL),A              
6559: C8              RET     Z                   
655A: 20 C9           JR      NZ,$6525            ; {}
655C: 50              LD      D,B                 
655D: C9              RET                         
655E: 29              ADD     HL,HL               
655F: CA 59 CA        JP      Z,$CA59             
6562: C4 11 CF        CALL    NZ,$CF11            
6565: 84              ADD     A,H                 
6566: 24              INC     H                   
6567: D1              POP     DE                  
6568: C2 37 D0        JP      NZ,$D037            
656B: C2 23 CF        JP      NZ,$CF23            
656E: 84              ADD     A,H                 
656F: 43              LD      B,E                 
6570: D2 87 52        JP      NC,$5287            ; {}
6573: D3                              
6574: 62              LD      H,D                 
6575: 0F              RRCA                        
6576: 51              LD      D,C                 
6577: CD 74 FD        CALL    $FD74               
657A: E0 00           LD      ($FF00+$00),A       
657C: B3              OR      E                   
657D: 58              LD      E,B                 
657E: 52              LD      D,D                 
657F: FE 04           CP      $04                 
6581: 0D              DEC     C                   
6582: 88              ADC     A,B                 
6583: 11 00 88        LD      DE,$8800            
6586: 21 00 88        LD      HL,$8800            
6589: 31 CD 02        LD      SP,$02CD            
658C: C7              RST     0X00                
658D: 07              RLCA                        
658E: C7              RST     0X00                
658F: 56              LD      D,(HL)              
6590: CE 74           ADC     $74                 
6592: FD                              
6593: E0 00           LD      ($FF00+$00),A       
6595: 93              SUB     E                   
6596: 48              LD      C,B                 
6597: 62              LD      H,D                 
6598: FE 04           CP      $04                 
659A: 0D              DEC     C                   
659B: 02              LD      (BC),A              
659C: 99              SBC     C                   
659D: C6 11           ADD     $11                 
659F: 20 12           JR      NZ,$65B3            ; {}
65A1: 9A              SBC     D                   
65A2: 85              ADD     A,L                 
65A3: 13              INC     DE                  
65A4: 20 18           JR      NZ,$65BE            ; {}
65A6: C5              PUSH    BC                  
65A7: 82              ADD     A,D                 
65A8: 22              LD      (HLI),A             
65A9: 20 26           JR      NZ,$65D1            ; {}
65AB: 20 C2           JR      NZ,$656F            ; {}
65AD: 27              DAA                         
65AE: 20 28           JR      NZ,$65D8            ; {}
65B0: C6 32           ADD     $32                 
65B2: 20 84           JR      NZ,$6538            ; {}
65B4: 33              INC     SP                  
65B5: 0F              RRCA                        
65B6: C4 38 20        CALL    NZ,$2038            
65B9: 84              ADD     A,H                 
65BA: 43              LD      B,E                 
65BB: 0F              RRCA                        
65BC: 84              ADD     A,H                 
65BD: 53              LD      D,E                 
65BE: 0F              RRCA                        
65BF: 53              LD      D,E                 
65C0: A6              AND     (HL)                
65C1: 56              LD      D,(HL)              
65C2: AB              XOR     E                   
65C3: 74              LD      (HL),H              
65C4: FD                              
65C5: E0 00           LD      ($FF00+$00),A       
65C7: 65              LD      H,L                 
65C8: 48              LD      C,B                 
65C9: 32              LD      (HLD),A             
65CA: FE 04           CP      $04                 
65CC: 0D              DEC     C                   
65CD: 85              ADD     A,L                 
65CE: 11 0F 85        LD      DE,$850F            
65D1: 21 0F 85        LD      HL,$850F            
65D4: 31 0F 85        LD      SP,$850F            
65D7: 41              LD      B,C                 
65D8: 0F              RRCA                        
65D9: 21 C5 31        LD      HL,$31C5            
65DC: C6 23           ADD     $23                 
65DE: C5              PUSH    BC                  
65DF: 33              INC     SP                  
65E0: C6 C2           ADD     $C2                 
65E2: 18 A7           JR      $658B               ; {}
65E4: 82              ADD     A,D                 
65E5: 61              LD      H,C                 
65E6: 20 48           JR      NZ,$6630            ; {}
65E8: C0              RET     NZ                  
65E9: 68              LD      L,B                 
65EA: C0              RET     NZ                  
65EB: 57              LD      D,A                 
65EC: 9B              SBC     E                   
65ED: 58              LD      E,B                 
65EE: 9C              SBC     H                   
65EF: 07              RLCA                        
65F0: 99              SBC     C                   
65F1: 17              RLA                         
65F2: 9A              SBC     D                   
65F3: 74              LD      (HL),H              
65F4: FD                              
65F5: E0 00           LD      ($FF00+$00),A       
65F7: A2              AND     D                   
65F8: 58              LD      E,B                 
65F9: 52              LD      D,D                 
65FA: FE 0C           CP      $0C                 
65FC: 05              DEC     B                   
65FD: 82              ADD     A,D                 
65FE: 00              NOP                         
65FF: 00              NOP                         
6600: 10 00           ;;STOP    $00                 
6602: 82              ADD     A,D                 
6603: 08 00 19        LD      ($1900),SP          
6606: 00              NOP                         
6607: 82              ADD     A,D                 
6608: 70              LD      (HL),B              
6609: 00              NOP                         
660A: 60              LD      H,B                 
660B: 00              NOP                         
660C: 82              ADD     A,D                 
660D: 78              LD      A,B                 
660E: 00              NOP                         
660F: 69              LD      L,C                 
6610: 00              NOP                         
6611: 02              LD      (BC),A              
6612: 25              DEC     H                   
6613: 11 25 20        LD      DE,$2025            
6616: 25              DEC     H                   
6617: 07              RLCA                        
6618: 26 18           LD      H,$18               
661A: 26 29           LD      H,$29               
661C: 26 50           LD      H,$50               
661E: 27              DAA                         
661F: 61              LD      H,C                 
6620: 27              DAA                         
6621: 72              LD      (HL),D              
6622: 27              DAA                         
6623: 59              LD      E,C                 
6624: 28 68           JR      Z,$668E             ; {}
6626: 28 77           JR      Z,$669F             ; {}
6628: 28 12           JR      Z,$663C             ; {}
662A: 29              ADD     HL,HL               
662B: 21 29 17        LD      HL,$1729            
662E: 2A              LD      A,(HLI)             
662F: 28 2A           JR      Z,$665B             ; {}
6631: 51              LD      D,C                 
6632: 2B              DEC     HL                  
6633: 62              LD      H,D                 
6634: 2B              DEC     HL                  
6635: 58              LD      E,B                 
6636: 2C              INC     L                   
6637: 67              LD      H,A                 
6638: 2C              INC     L                   
6639: 84              ADD     A,H                 
663A: 33              INC     SP                  
663B: 1B              DEC     DE                  
663C: 84              ADD     A,H                 
663D: 43              LD      B,E                 
663E: 1B              DEC     DE                  
663F: 82              ADD     A,D                 
6640: 54              LD      D,H                 
6641: 1B              DEC     DE                  
6642: 24              INC     H                   
6643: 0F              RRCA                        
6644: 57              LD      D,A                 
6645: 0F              RRCA                        
6646: 35              DEC     (HL)                
6647: CB E0           SET     1,E                 
6649: 00              NOP                         
664A: A0              AND     B                   
664B: 58              LD      E,B                 
664C: 72              LD      (HL),D              
664D: FE 04           CP      $04                 
664F: 2F              CPL                         
6650: 11 25 85        LD      DE,$8525            
6653: 12              LD      (DE),A              
6654: 21 17 26        LD      HL,$2617            
6657: C2 21 23        JP      NZ,$2321            
665A: C2 27 24        JP      NZ,$2427            
665D: 41              LD      B,C                 
665E: 27              DAA                         
665F: 85              ADD     A,L                 
6660: 42              LD      B,D                 
6661: 22              LD      (HLI),A             
6662: 47              LD      B,A                 
6663: 28 89           JR      Z,$65EE             ; {}
6665: 61              LD      H,C                 
6666: 0D              DEC     C                   
6667: 84              ADD     A,H                 
6668: 22              LD      (HLI),A             
6669: 20 26           JR      NZ,$6691            ; {}
666B: 0D              DEC     C                   
666C: 82              ADD     A,D                 
666D: 61              LD      H,C                 
666E: 20 43           JR      NZ,$66B3            ; {}
6670: 98              SBC     B                   
6671: 13              INC     DE                  
6672: C7              RST     0X00                
6673: 85              ADD     A,L                 
6674: 32              LD      (HLD),A             
6675: 0D              DEC     C                   
6676: 74              LD      (HL),H              
6677: FD                              
6678: E0 00           LD      ($FF00+$00),A       
667A: 82              ADD     A,D                 
667B: 58              LD      E,B                 
667C: 52              LD      D,D                 
667D: FE 04           CP      $04                 
667F: 4D              LD      C,L                 
6680: C5              PUSH    BC                  
6681: 10 0F           ;;STOP    $0F                 
6683: 03              INC     BC                  
6684: 99              SBC     C                   
6685: 84              ADD     A,H                 
6686: 05              DEC     B                   
6687: 99              SBC     C                   
6688: 13              INC     DE                  
6689: 9A              SBC     D                   
668A: 84              ADD     A,H                 
668B: 15              DEC     D                   
668C: 9A              SBC     D                   
668D: 23              INC     HL                  
668E: C5              PUSH    BC                  
668F: 84              ADD     A,H                 
6690: 25              DEC     H                   
6691: C5              PUSH    BC                  
6692: 33              INC     SP                  
6693: C6 84           ADD     $84                 
6695: 35              DEC     (HL)                
6696: C6 52           ADD     $52                 
6698: C0              RET     NZ                  
6699: 42              LD      B,D                 
669A: 9B              SBC     E                   
669B: 43              LD      B,E                 
669C: 9C              SBC     H                   
669D: 84              ADD     A,H                 
669E: 45              LD      B,L                 
669F: CE 84           ADC     $84                 
66A1: 55              LD      D,L                 
66A2: C0              RET     NZ                  
66A3: 74              LD      (HL),H              
66A4: FD                              
66A5: E0 00           LD      ($FF00+$00),A       
66A7: 82              ADD     A,D                 
66A8: 78              LD      A,B                 
66A9: 52              LD      D,D                 
66AA: FE 04           CP      $04                 
66AC: 0D              DEC     C                   
66AD: 74              LD      (HL),H              
66AE: FD                              
66AF: 11 C5 21        LD      DE,$21C5            
66B2: C6 83           ADD     $83                 
66B4: 61              LD      H,C                 
66B5: C0              RET     NZ                  
66B6: 62              LD      H,D                 
66B7: CE C4           ADC     $C4                 
66B9: 17              RLA                         
66BA: 20 C6           JR      NZ,$6682            ; {}
66BC: 18 20           JR      $66DE               ; {}
66BE: 06 99           LD      B,$99               
66C0: 16 9A           LD      D,$9A               
66C2: 24              INC     H                   
66C3: C0              RET     NZ                  
66C4: 25              DEC     H                   
66C5: 9B              SBC     E                   
66C6: 26 9C           LD      H,$9C               
66C8: 82              ADD     A,D                 
66C9: 35              DEC     (HL)                
66CA: C0              RET     NZ                  
66CB: E0 00           LD      ($FF00+$00),A       
66CD: A1              AND     C                   
66CE: 38 42           JR      C,$6712             ; {}
66D0: FE 04           CP      $04                 
66D2: 0D              DEC     C                   
66D3: 74              LD      (HL),H              
66D4: FD                              
66D5: C6 11           ADD     $11                 
66D7: 20 C6           JR      NZ,$669F            ; {}
66D9: 12              LD      (DE),A              
66DA: 20 03           JR      NZ,$66DF            ; {}
66DC: 99              SBC     C                   
66DD: 13              INC     DE                  
66DE: 9A              SBC     D                   
66DF: 23              INC     HL                  
66E0: C5              PUSH    BC                  
66E1: 33              INC     SP                  
66E2: C6 44           ADD     $44                 
66E4: 9B              SBC     E                   
66E5: 45              LD      B,L                 
66E6: 9C              SBC     H                   
66E7: 82              ADD     A,D                 
66E8: 64              LD      H,H                 
66E9: 0F              RRCA                        
66EA: E0 00           LD      ($FF00+$00),A       
66EC: 30 78           JR      NC,$6766            ; {}
66EE: 32              LD      (HLD),A             
66EF: FE 04           CP      $04                 
66F1: 0D              DEC     C                   
66F2: 74              LD      (HL),H              
66F3: FD                              
66F4: 86              ADD     A,(HL)              
66F5: 02              LD      (BC),A              
66F6: 99              SBC     C                   
66F7: 86              ADD     A,(HL)              
66F8: 12              LD      (DE),A              
66F9: 9A              SBC     D                   
66FA: 21 9B 22        LD      HL,$229B            
66FD: 9C              SBC     H                   
66FE: 82              ADD     A,D                 
66FF: 26 C5           LD      H,$C5               
6701: 82              ADD     A,D                 
6702: 36 C6           LD      (HL),$C6            
6704: 28 CE           JR      Z,$66D4             ; {}
6706: 51              LD      D,C                 
6707: CE 41           ADC     $41                 
6709: C0              RET     NZ                  
670A: 61              LD      H,C                 
670B: C0              RET     NZ                  
670C: 84              ADD     A,H                 
670D: 53              LD      D,E                 
670E: 0F              RRCA                        
670F: 84              ADD     A,H                 
6710: 63              LD      H,E                 
6711: 0F              RRCA                        
6712: 82              ADD     A,D                 
6713: 57              LD      D,A                 
6714: 20 82           JR      NZ,$6698            ; {}
6716: 67              LD      H,A                 
6717: 20 E0           JR      NZ,$66F9            ; {}
6719: 00              NOP                         
671A: B1              OR      C                   
671B: 48              LD      C,B                 
671C: 62              LD      H,D                 
671D: FE 04           CP      $04                 
671F: 0F              RRCA                        
6720: 11 AC 18        LD      DE,$18AC            
6723: AC              XOR     H                   
6724: 61              LD      H,C                 
6725: AC              XOR     H                   
6726: 68              LD      L,B                 
6727: AC              XOR     H                   
6728: 22              LD      (HLI),A             
6729: 2C              INC     L                   
672A: 27              DAA                         
672B: 2B              DEC     HL                  
672C: 52              LD      D,D                 
672D: 2A              LD      A,(HLI)             
672E: 57              LD      D,A                 
672F: 29              ADD     HL,HL               
6730: 84              ADD     A,H                 
6731: 33              INC     SP                  
6732: 0D              DEC     C                   
6733: 84              ADD     A,H                 
6734: 43              LD      B,E                 
6735: 0D              DEC     C                   
6736: 84              ADD     A,H                 
6737: 23              INC     HL                  
6738: 22              LD      (HLI),A             
6739: 84              ADD     A,H                 
673A: 53              LD      D,E                 
673B: 21 C2 32        LD      HL,$32C2            
673E: 24              INC     H                   
673F: C2 37 23        JP      NZ,$2337            
6742: 35              DEC     (HL)                
6743: C5              PUSH    BC                  
6744: 45              LD      B,L                 
6745: C6 54           ADD     $54                 
6747: 98              SBC     B                   
6748: 33              INC     SP                  
6749: 17              RLA                         
674A: 34              INC     (HL)                
674B: 12              LD      (DE),A              
674C: 36 16           LD      (HL),$16            
674E: 43              LD      B,E                 
674F: 15              DEC     D                   
6750: 46              LD      B,(HL)              
6751: 14              INC     D                   
6752: 74              LD      (HL),H              
6753: FD                              
6754: E0 00           LD      ($FF00+$00),A       
6756: 83              ADD     A,E                 
6757: 28 42           JR      Z,$679B             ; {}
6759: FE 04           CP      $04                 
675B: 05              DEC     B                   
675C: 11 A6 14        LD      DE,$14A6            
675F: A6              AND     (HL)                
6760: 19              ADD     HL,DE               
6761: 2A              LD      A,(HLI)             
6762: 23              INC     HL                  
6763: A6              AND     (HL)                
6764: 25              DEC     H                   
6765: 20 82           JR      NZ,$66E9            ; {}
6767: 26 A7           LD      H,$A7               
6769: C2 29 05        JP      NZ,$0529            
676C: 34              INC     (HL)                
676D: 20 35           JR      NZ,$67A4            ; {}
676F: A7              AND     A                   
6770: 37              SCF                         
6771: A7              AND     A                   
6772: 49              LD      C,C                 
6773: 2C              INC     L                   
6774: 41              LD      B,C                 
6775: A7              AND     A                   
6776: 82              ADD     A,D                 
6777: 43              LD      B,E                 
6778: A7              AND     A                   
6779: 46              LD      B,(HL)              
677A: A7              AND     A                   
677B: 48              LD      C,B                 
677C: A7              AND     A                   
677D: 82              ADD     A,D                 
677E: 52              LD      D,D                 
677F: A7              AND     A                   
6780: 57              LD      D,A                 
6781: A7              AND     A                   
6782: 60              LD      H,B                 
6783: 27              DAA                         
6784: 61              LD      H,C                 
6785: 2B              DEC     HL                  
6786: 62              LD      H,D                 
6787: A6              AND     (HL)                
6788: 68              LD      L,B                 
6789: 2C              INC     L                   
678A: 69              LD      L,C                 
678B: 28 70           JR      Z,$67FD             ; {}
678D: DF              RST     0X18                
678E: 71              LD      (HL),C              
678F: 27              DAA                         
6790: 78              LD      A,B                 
6791: 28 79           JR      Z,$680C             ; {}
6793: DF              RST     0X18                
6794: 13              INC     DE                  
6795: 0D              DEC     C                   
6796: 18 0D           JR      $67A5               ; {}
6798: 22              LD      (HLI),A             
6799: 0D              DEC     C                   
679A: 82              ADD     A,D                 
679B: 31 0D 45        LD      SP,$450D            
679E: 0D              DEC     C                   
679F: 47              LD      B,A                 
67A0: 0D              DEC     C                   
67A1: 64              LD      H,H                 
67A2: 0D              DEC     C                   
67A3: 82              ADD     A,D                 
67A4: 66              LD      H,(HL)              
67A5: 0D              DEC     C                   
67A6: 74              LD      (HL),H              
67A7: FD                              
67A8: E0 00           LD      ($FF00+$00),A       
67AA: 50              LD      D,B                 
67AB: 88              ADC     A,B                 
67AC: 32              LD      (HLD),A             
67AD: FE 04           CP      $04                 
67AF: 9D              SBC     L                   
67B0: 00              NOP                         
67B1: DF              RST     0X18                
67B2: 83              ADD     A,E                 
67B3: 03              INC     BC                  
67B4: DF              RST     0X18                
67B5: 83              ADD     A,E                 
67B6: 07              RLCA                        
67B7: DF              RST     0X18                
67B8: 84              ADD     A,H                 
67B9: 10 21           ;;STOP    $21                 
67BB: 14              INC     D                   
67BC: 26 15           LD      H,$15               
67BE: DF              RST     0X18                
67BF: 17              RLA                         
67C0: DF              RST     0X18                
67C1: C3 19 DF        JP      $DF19               
67C4: 84              ADD     A,H                 
67C5: 20 05           JR      NZ,$67CC            ; {}
67C7: 24              INC     H                   
67C8: 2A              LD      A,(HLI)             
67C9: 25              DEC     H                   
67CA: 26 C4           LD      H,$C4               
67CC: 26 DF           LD      H,$DF               
67CE: 84              ADD     A,H                 
67CF: 30 05           JR      NC,$67D6            ; {}
67D1: 82              ADD     A,D                 
67D2: 40              LD      B,B                 
67D3: 22              LD      (HLI),A             
67D4: 42              LD      B,D                 
67D5: 2B              DEC     HL                  
67D6: 33              INC     SP                  
67D7: 05              DEC     B                   
67D8: C5              PUSH    BC                  
67D9: 34              INC     (HL)                
67DA: 05              DEC     B                   
67DB: C5              PUSH    BC                  
67DC: 35              DEC     (HL)                
67DD: 24              INC     H                   
67DE: C4 38 DF        CALL    NZ,$DF38            
67E1: 43              LD      B,E                 
67E2: 05              DEC     B                   
67E3: 52              LD      D,D                 
67E4: 27              DAA                         
67E5: 53              LD      D,E                 
67E6: 2B              DEC     HL                  
67E7: 47              LD      B,A                 
67E8: DF              RST     0X18                
67E9: 51              LD      D,C                 
67EA: DF              RST     0X18                
67EB: C2 63 23        JP      NZ,$2363            
67EE: 59              LD      E,C                 
67EF: DF              RST     0X18                
67F0: 83              ADD     A,E                 
67F1: 60              LD      H,B                 
67F2: DF              RST     0X18                
67F3: 67              LD      H,A                 
67F4: DF              RST     0X18                
67F5: 82              ADD     A,D                 
67F6: 70              LD      (HL),B              
67F7: DF              RST     0X18                
67F8: 82              ADD     A,D                 
67F9: 76              HALT                        
67FA: DF              RST     0X18                
67FB: FE 04           CP      $04                 
67FD: 0D              DEC     C                   
67FE: 11 C0 31        LD      DE,$31C0            
6801: C0              RET     NZ                  
6802: 21 CE 34        LD      HL,$34CE            
6805: CE 24           ADC     $24                 
6807: C0              RET     NZ                  
6808: C2 25 20        JP      NZ,$2025            
680B: 84              ADD     A,H                 
680C: 45              LD      B,L                 
680D: 20 61           JR      NZ,$6870            ; {}
680F: AC              XOR     H                   
6810: 68              LD      L,B                 
6811: AC              XOR     H                   
6812: 17              RLA                         
6813: C5              PUSH    BC                  
6814: 27              DAA                         
6815: C6 08           ADD     $08                 
6817: 99              SBC     C                   
6818: 18 9A           JR      $67B4               ; {}
681A: 74              LD      (HL),H              
681B: FD                              
681C: E0 00           LD      ($FF00+$00),A       
681E: 45              LD      B,L                 
681F: 88              ADC     A,B                 
6820: 42              LD      B,D                 
6821: FE 04           CP      $04                 
6823: 25              DEC     H                   
6824: 82              ADD     A,D                 
6825: 70              LD      (HL),B              
6826: 05              DEC     B                   
6827: 16 0D           LD      D,$0D               
6829: 19              ADD     HL,DE               
682A: 0D              DEC     C                   
682B: 22              LD      (HLI),A             
682C: 0D              DEC     C                   
682D: 82              ADD     A,D                 
682E: 27              DAA                         
682F: 0D              DEC     C                   
6830: 31 0D C2        LD      SP,$C20D            
6833: 38 0D           JR      C,$6842             ; {}
6835: 49              LD      C,C                 
6836: 0D              DEC     C                   
6837: 82              ADD     A,D                 
6838: 42              LD      B,D                 
6839: 0D              DEC     C                   
683A: 55              LD      D,L                 
683B: 0D              DEC     C                   
683C: 69              LD      L,C                 
683D: 0D              DEC     C                   
683E: 60              LD      H,B                 
683F: 27              DAA                         
6840: 61              LD      H,C                 
6841: 22              LD      (HLI),A             
6842: 62              LD      H,D                 
6843: 2B              DEC     HL                  
6844: 72              LD      (HL),D              
6845: 27              DAA                         
6846: 41              LD      B,C                 
6847: DF              RST     0X18                
6848: 84              ADD     A,H                 
6849: 51              LD      D,C                 
684A: DF              RST     0X18                
684B: 83              ADD     A,E                 
684C: 63              LD      H,E                 
684D: DF              RST     0X18                
684E: 14              INC     D                   
684F: DF              RST     0X18                
6850: 82              ADD     A,D                 
6851: 24              INC     H                   
6852: DF              RST     0X18                
6853: 29              ADD     HL,HL               
6854: 0F              RRCA                        
6855: 53              LD      D,E                 
6856: 0F              RRCA                        
6857: 66              LD      H,(HL)              
6858: 0F              RRCA                        
6859: 82              ADD     A,D                 
685A: 11 B0 C2        LD      DE,$C2B0            
685D: 13              INC     DE                  
685E: 01 33 B0        LD      BC,$B033            
6861: 83              ADD     A,E                 
6862: 34              INC     (HL)                
6863: AE              XOR     (HL)                
6864: 37              SCF                         
6865: AF              XOR     A                   
6866: 47              LD      B,A                 
6867: 01 57 B0        LD      BC,$B057            
686A: 82              ADD     A,D                 
686B: 58              LD      E,B                 
686C: AE              XOR     (HL)                
686D: 17              RLA                         
686E: A0              AND     B                   
686F: 48              LD      C,B                 
6870: 15              DEC     D                   
6871: 49              LD      C,C                 
6872: 13              INC     DE                  
6873: 82              ADD     A,D                 
6874: 68              LD      L,B                 
6875: 12              LD      (DE),A              
6876: 74              LD      (HL),H              
6877: FD                              
6878: E0 00           LD      ($FF00+$00),A       
687A: 20 88           JR      NZ,$6804            ; {}
687C: 32              LD      (HLD),A             
687D: FE 04           CP      $04                 
687F: 45              LD      B,L                 
6880: 13              INC     DE                  
6881: 2C              INC     L                   
6882: 84              ADD     A,H                 
6883: 14              INC     D                   
6884: 22              LD      (HLI),A             
6885: 18 2B           JR      $68B2               ; {}
6887: C2 23 24        JP      NZ,$2423            
688A: C2 28 23        JP      NZ,$2328            
688D: 43              LD      B,E                 
688E: 2A              LD      A,(HLI)             
688F: 84              ADD     A,H                 
6890: 44              LD      B,H                 
6891: 21 48 29        LD      HL,$2948            
6894: 82              ADD     A,D                 
6895: 50              LD      D,B                 
6896: AE              XOR     (HL)                
6897: 22              LD      (HLI),A             
6898: AF              XOR     A                   
6899: C2 32 01        JP      NZ,$0132            
689C: 52              LD      D,D                 
689D: B0              OR      B                   
689E: 83              ADD     A,E                 
689F: 10 0D           ;;STOP    $0D                 
68A1: 20 0D           JR      NZ,$68B0            ; {}
68A3: 34              INC     (HL)                
68A4: 0F              RRCA                        
68A5: 57              LD      D,A                 
68A6: 0F              RRCA                        
68A7: 25              DEC     H                   
68A8: 0D              DEC     C                   
68A9: 40              LD      B,B                 
68AA: 0D              DEC     C                   
68AB: 60              LD      H,B                 
68AC: 0D              DEC     C                   
68AD: 54              LD      D,H                 
68AE: 0D              DEC     C                   
68AF: 45              LD      B,L                 
68B0: 98              SBC     B                   
68B1: 69              LD      L,C                 
68B2: 28 68           JR      Z,$691C             ; {}
68B4: 2C              INC     L                   
68B5: 78              LD      A,B                 
68B6: 28 79           JR      Z,$6931             ; {}
68B8: 05              DEC     B                   
68B9: 40              LD      B,B                 
68BA: 13              INC     DE                  
68BB: 41              LD      B,C                 
68BC: 14              INC     D                   
68BD: 82              ADD     A,D                 
68BE: 60              LD      H,B                 
68BF: 12              LD      (DE),A              
68C0: 24              INC     H                   
68C1: 17              RLA                         
68C2: 82              ADD     A,D                 
68C3: 25              DEC     H                   
68C4: 12              LD      (DE),A              
68C5: 26 A0           LD      H,$A0               
68C7: 27              DAA                         
68C8: 16 36           LD      D,$36               
68CA: 20 37           JR      NZ,$6903            ; {}
68CC: 14              INC     D                   
68CD: 34              INC     (HL)                
68CE: 15              DEC     D                   
68CF: 74              LD      (HL),H              
68D0: FD                              
68D1: E0 00           LD      ($FF00+$00),A       
68D3: 21 18 32        LD      HL,$3218            
68D6: FE 04           CP      $04                 
68D8: 0D              DEC     C                   
68D9: 04              INC     B                   
68DA: 99              SBC     C                   
68DB: 83              ADD     A,E                 
68DC: 11 0F 83        LD      DE,$830F            
68DF: 21 0F 83        LD      HL,$830F            
68E2: 31 0F 12        LD      SP,$120F            
68E5: C5              PUSH    BC                  
68E6: 14              INC     D                   
68E7: 9A              SBC     D                   
68E8: C2 15 11        JP      NZ,$1115            
68EB: 83              ADD     A,E                 
68EC: 16 20           LD      D,$20               
68EE: 22              LD      (HLI),A             
68EF: C6 24           ADD     $24                 
68F1: 13              INC     DE                  
68F2: 83              ADD     A,E                 
68F3: 26 20           LD      H,$20               
68F5: 34              INC     (HL)                
68F6: 11 82 41        LD      DE,$4182            
68F9: 12              LD      (DE),A              
68FA: 44              LD      B,H                 
68FB: 93              SUB     E                   
68FC: 56              LD      D,(HL)              
68FD: C0              RET     NZ                  
68FE: 57              LD      D,A                 
68FF: CE 72           ADC     $72                 
6901: C8              RET     Z                   
6902: 77              LD      (HL),A              
6903: C8              RET     Z                   
6904: 74              LD      (HL),H              
6905: FD                              
6906: E0 00           LD      ($FF00+$00),A       
6908: 3F              CCF                         
6909: 28 22           JR      Z,$692D             ; {}
690B: FE 05           CP      $05                 
690D: 90              SUB     B                   
690E: 8A              ADC     A,D                 
690F: 00              NOP                         
6910: 78              LD      A,B                 
6911: 01 79 03        LD      BC,$0379            
6914: 79              LD      A,C                 
6915: 05              DEC     B                   
6916: 79              LD      A,C                 
6917: 07              RLCA                        
6918: 79              LD      A,C                 
6919: 09              ADD     HL,BC               
691A: 79              LD      A,C                 
691B: 8A              ADC     A,D                 
691C: 10 03           ;;STOP    $03                 
691E: 82              ADD     A,D                 
691F: 18 7C           JR      $699D               ; {}
6921: 88              ADC     A,B                 
6922: 20 80           JR      NZ,$68A4            ; {}
6924: 8A              ADC     A,D                 
6925: 30 81           JR      NC,$68A8            ; {}
6927: 8A              ADC     A,D                 
6928: 40              LD      B,B                 
6929: 81              ADD     A,C                 
692A: 8A              ADC     A,D                 
692B: 50              LD      D,B                 
692C: 81              ADD     A,C                 
692D: 8A              ADC     A,D                 
692E: 60              LD      H,B                 
692F: 81              ADD     A,C                 
6930: 28 5F           JR      Z,$6991             ; {}
6932: 29              ADD     HL,HL               
6933: 60              LD      H,B                 
6934: 38 52           JR      C,$6988             ; {}
6936: 39              ADD     HL,SP               
6937: 54              LD      D,H                 
6938: 49              LD      C,C                 
6939: 51              LD      D,C                 
693A: 57              LD      D,A                 
693B: 72              LD      (HL),D              
693C: 58              LD      E,B                 
693D: 50              LD      D,B                 
693E: 59              LD      E,C                 
693F: 54              LD      D,H                 
6940: 61              LD      H,C                 
6941: 72              LD      (HL),D              
6942: 66              LD      H,(HL)              
6943: 72              LD      (HL),D              
6944: 67              LD      H,A                 
6945: 50              LD      D,B                 
6946: 82              ADD     A,D                 
6947: 68              LD      L,B                 
6948: 54              LD      D,H                 
6949: 87              ADD     A,A                 
694A: 70              LD      (HL),B              
694B: 53              LD      D,E                 
694C: 83              ADD     A,E                 
694D: 77              LD      (HL),A              
694E: 54              LD      D,H                 
694F: E0 00           LD      ($FF00+$00),A       
6951: 81              ADD     A,C                 
6952: 68              LD      L,B                 
6953: 60              LD      H,B                 
6954: FE 00           CP      $00                 
6956: 91              SUB     C                   
6957: C8              RET     Z                   
6958: 00              NOP                         
6959: 0D              DEC     C                   
695A: 00              NOP                         
695B: 21 01 26        LD      HL,$2601            
695E: C6 11           ADD     $11                 
6960: 24              INC     H                   
6961: 70              LD      (HL),B              
6962: 22              LD      (HLI),A             
6963: 71              LD      (HL),C              
6964: 28 C6           JR      Z,$692C             ; {}
6966: 10 20           ;;STOP    $20                 
6968: 72              LD      (HL),D              
6969: 27              DAA                         
696A: 84              ADD     A,H                 
696B: 73              LD      (HL),E              
696C: 22              LD      (HLI),A             
696D: 77              LD      (HL),A              
696E: 28 C3           JR      Z,$6933             ; {}
6970: 42              LD      B,D                 
6971: 23              INC     HL                  
6972: C3 47 24        JP      $2447               
6975: 32              LD      (HLD),A             
6976: 25              DEC     H                   
6977: 37              SCF                         
6978: 26 84           LD      H,$84               
697A: 33              INC     SP                  
697B: 21 84 43        LD      HL,$4384            
697E: 05              DEC     B                   
697F: 84              ADD     A,H                 
6980: 53              LD      D,E                 
6981: 05              DEC     B                   
6982: 84              ADD     A,H                 
6983: 63              LD      H,E                 
6984: 05              DEC     B                   
6985: 54              LD      D,H                 
6986: 0F              RRCA                        
6987: 74              LD      (HL),H              
6988: FD                              
6989: E0 00           LD      ($FF00+$00),A       
698B: A1              AND     C                   
698C: 58              LD      E,B                 
698D: 42              LD      B,D                 
698E: FE 04           CP      $04                 
6990: 05              DEC     B                   
6991: 84              ADD     A,H                 
6992: 23              INC     HL                  
6993: 01 86 41        LD      BC,$4186            
6996: 01 83 43        LD      BC,$4383            
6999: 01 83 51        LD      BC,$5183            
699C: 01 88 31        LD      BC,$3188            
699F: AF              XOR     A                   
69A0: 36 01           LD      (HL),$01            
69A2: 84              ADD     A,H                 
69A3: 13              INC     DE                  
69A4: 01 83 61        LD      BC,$6183            
69A7: 01 83 54        LD      BC,$5483            
69AA: B0              OR      B                   
69AB: 82              ADD     A,D                 
69AC: 47              LD      B,A                 
69AD: B0              OR      B                   
69AE: 82              ADD     A,D                 
69AF: 11 0D 82        LD      DE,$820D            
69B2: 21 0D 82        LD      HL,$820D            
69B5: 17              RLA                         
69B6: 0D              DEC     C                   
69B7: 83              ADD     A,E                 
69B8: 33              INC     SP                  
69B9: 01 28 0D        LD      BC,$0D28            
69BC: 65              LD      H,L                 
69BD: 0D              DEC     C                   
69BE: 67              LD      H,A                 
69BF: 0D              DEC     C                   
69C0: 11 A0 18        LD      DE,$18A0            
69C3: A6              AND     (HL)                
69C4: 68              LD      L,B                 
69C5: A6              AND     (HL)                
69C6: 74              LD      (HL),H              
69C7: FD                              
69C8: E0 00           LD      ($FF00+$00),A       
69CA: 42              LD      B,D                 
69CB: 38 42           JR      C,$6A0F             ; {}
69CD: FE 04           CP      $04                 
69CF: 91              SUB     C                   
69D0: 84              ADD     A,H                 
69D1: 43              LD      B,E                 
69D2: 0D              DEC     C                   
69D3: 84              ADD     A,H                 
69D4: 53              LD      D,E                 
69D5: 0D              DEC     C                   
69D6: 84              ADD     A,H                 
69D7: 63              LD      H,E                 
69D8: 0D              DEC     C                   
69D9: 32              LD      (HLD),A             
69DA: 25              DEC     H                   
69DB: 84              ADD     A,H                 
69DC: 33              INC     SP                  
69DD: 21 37 26        LD      HL,$2637            
69E0: C3 42 23        JP      $2342               
69E3: 72              LD      (HL),D              
69E4: 27              DAA                         
69E5: 84              ADD     A,H                 
69E6: 73              LD      (HL),E              
69E7: 22              LD      (HLI),A             
69E8: C4 47 24        CALL    NZ,$2447            
69EB: 34              INC     (HL)                
69EC: 99              SBC     C                   
69ED: 44              LD      B,H                 
69EE: 9A              SBC     D                   
69EF: 55              LD      D,L                 
69F0: C0              RET     NZ                  
69F1: 77              LD      (HL),A              
69F2: 28 74           JR      Z,$6A68             ; {}
69F4: FD                              
69F5: E0 00           LD      ($FF00+$00),A       
69F7: A4              AND     H                   
69F8: 38 42           JR      C,$6A3C             ; {}
69FA: FE 04           CP      $04                 
69FC: 0D              DEC     C                   
69FD: FE 04           CP      $04                 
69FF: 2D              DEC     L                   
6A00: 83              ADD     A,E                 
6A01: 00              NOP                         
6A02: DF              RST     0X18                
6A03: 83              ADD     A,E                 
6A04: 10 DF           ;;STOP    $DF                 
6A06: 20 DF           JR      NZ,$69E7            ; {}
6A08: 03              INC     BC                  
6A09: 25              DEC     H                   
6A0A: 13              INC     DE                  
6A0B: 23              INC     HL                  
6A0C: 21 25 22        LD      HL,$2225            
6A0F: 21 23 29        LD      HL,$2923            
6A12: 30 25           JR      NC,$6A39            ; {}
6A14: 31 29 14        LD      SP,$1429            
6A17: 0F              RRCA                        
6A18: 32              LD      (HLD),A             
6A19: 0F              RRCA                        
6A1A: 51              LD      D,C                 
6A1B: 0F              RRCA                        
6A1C: 62              LD      H,D                 
6A1D: 0F              RRCA                        
6A1E: 15              DEC     D                   
6A1F: 05              DEC     B                   
6A20: 18 05           JR      $6A27               ; {}
6A22: 33              INC     SP                  
6A23: 05              DEC     B                   
6A24: 41              LD      B,C                 
6A25: 05              DEC     B                   
6A26: 52              LD      D,D                 
6A27: 05              DEC     B                   
6A28: 61              LD      H,C                 
6A29: 05              DEC     B                   
6A2A: 67              LD      H,A                 
6A2B: 05              DEC     B                   
6A2C: 85              ADD     A,L                 
6A2D: 25              DEC     H                   
6A2E: AE              XOR     (HL)                
6A2F: 34              INC     (HL)                
6A30: AE              XOR     (HL)                
6A31: 43              LD      B,E                 
6A32: AF              XOR     A                   
6A33: C2 53 01        JP      NZ,$0153            
6A36: 83              ADD     A,E                 
6A37: 57              LD      D,A                 
6A38: AE              XOR     (HL)                
6A39: 56              LD      D,(HL)              
6A3A: AF              XOR     A                   
6A3B: 66              LD      H,(HL)              
6A3C: 01 29 AC        LD      BC,$AC29            
6A3F: 59              LD      E,C                 
6A40: AC              XOR     H                   
6A41: 74              LD      (HL),H              
6A42: FD                              
6A43: E0 00           LD      ($FF00+$00),A       
6A45: 17              RLA                         
6A46: 38 32           JR      C,$6A7A             ; {}
6A48: FE 04           CP      $04                 
6A4A: 4D              LD      C,L                 
6A4B: 89              ADC     A,C                 
6A4C: 60              LD      H,B                 
6A4D: DF              RST     0X18                
6A4E: 82              ADD     A,D                 
6A4F: 60              LD      H,B                 
6A50: 0D              DEC     C                   
6A51: 08 26 C2        LD      ($C226),SP          
6A54: 09              ADD     HL,BC               
6A55: DF              RST     0X18                
6A56: 18 24           JR      $6A7C               ; {}
6A58: 28 2A           JR      Z,$6A84             ; {}
6A5A: 29              ADD     HL,HL               
6A5B: 26 11           LD      H,$11               
6A5D: 05              DEC     B                   
6A5E: C2 17 05        JP      NZ,$0517            
6A61: 38 05           JR      C,$6A68             ; {}
6A63: 84              ADD     A,H                 
6A64: 12              LD      (DE),A              
6A65: DF              RST     0X18                
6A66: 24              INC     H                   
6A67: DF              RST     0X18                
6A68: 82              ADD     A,D                 
6A69: 33              INC     SP                  
6A6A: DF              RST     0X18                
6A6B: 46              LD      B,(HL)              
6A6C: DF              RST     0X18                
6A6D: 83              ADD     A,E                 
6A6E: 55              LD      D,L                 
6A6F: DF              RST     0X18                
6A70: 84              ADD     A,H                 
6A71: 20 AE           JR      NZ,$6A21            ; {}
6A73: 83              ADD     A,E                 
6A74: 50              LD      D,B                 
6A75: AE              XOR     (HL)                
6A76: 43              LD      B,E                 
6A77: AF              XOR     A                   
6A78: 53              LD      D,E                 
6A79: B0              OR      B                   
6A7A: C3 16 A7        JP      $A716               
6A7D: 32              LD      (HLD),A             
6A7E: A7              AND     A                   
6A7F: 35              DEC     (HL)                
6A80: A7              AND     A                   
6A81: C2 44 A7        JP      NZ,$A744            
6A84: 47              LD      B,A                 
6A85: A7              AND     A                   
6A86: 58              LD      E,B                 
6A87: A7              AND     A                   
6A88: 65              LD      H,L                 
6A89: A7              AND     A                   
6A8A: 25              DEC     H                   
6A8B: DD                              
6A8C: 45              LD      B,L                 
6A8D: DD                              
6A8E: 48              LD      C,B                 
6A8F: DD                              
6A90: 64              LD      H,H                 
6A91: DD                              
6A92: 37              SCF                         
6A93: BE              CP      (HL)                
6A94: E1              POP     HL                  
6A95: 0A              LD      A,(BC)              
6A96: B8              CP      B                   
6A97: 38 42           JR      C,$6ADB             ; {}
6A99: 20 AC           JR      NZ,$6A47            ; {}
6A9B: 50              LD      D,B                 
6A9C: AC              XOR     H                   
6A9D: FE 04           CP      $04                 
6A9F: 9D              SBC     L                   
6AA0: 8A              ADC     A,D                 
6AA1: 00              NOP                         
6AA2: DF              RST     0X18                
6AA3: 8A              ADC     A,D                 
6AA4: 10 DF           ;;STOP    $DF                 
6AA6: 8A              ADC     A,D                 
6AA7: 60              LD      H,B                 
6AA8: DF              RST     0X18                
6AA9: 8A              ADC     A,D                 
6AAA: 70              LD      (HL),B              
6AAB: DF              RST     0X18                
6AAC: 20 DF           JR      NZ,$6A8D            ; {}
6AAE: 21 25 88        LD      HL,$8825            
6AB1: 22              LD      (HLI),A             
6AB2: 21 30 25        LD      HL,$2530            
6AB5: 31 29 40        LD      SP,$4029            
6AB8: 23              INC     HL                  
6AB9: 50              LD      D,B                 
6ABA: 27              DAA                         
6ABB: 89              ADC     A,C                 
6ABC: 51              LD      D,C                 
6ABD: 22              LD      (HLI),A             
6ABE: 38 05           JR      C,$6AC5             ; {}
6AC0: 39              ADD     HL,SP               
6AC1: 0F              RRCA                        
6AC2: 42              LD      B,D                 
6AC3: 05              DEC     B                   
6AC4: 44              LD      B,H                 
6AC5: 05              DEC     B                   
6AC6: 49              LD      C,C                 
6AC7: 05              DEC     B                   
6AC8: 46              LD      B,(HL)              
6AC9: 0F              RRCA                        
6ACA: 33              INC     SP                  
6ACB: CB E1           SET     1,E                 
6ACD: 0A              LD      A,(BC)              
6ACE: B7              OR      A                   
6ACF: 78              LD      A,B                 
6AD0: 42              LD      B,D                 
6AD1: FE 04           CP      $04                 
6AD3: 9D              SBC     L                   
6AD4: 8A              ADC     A,D                 
6AD5: 00              NOP                         
6AD6: DF              RST     0X18                
6AD7: 8A              ADC     A,D                 
6AD8: 10 DF           ;;STOP    $DF                 
6ADA: 8A              ADC     A,D                 
6ADB: 60              LD      H,B                 
6ADC: DF              RST     0X18                
6ADD: 8A              ADC     A,D                 
6ADE: 70              LD      (HL),B              
6ADF: DF              RST     0X18                
6AE0: 59              LD      E,C                 
6AE1: DF              RST     0X18                
6AE2: 89              ADC     A,C                 
6AE3: 20 21           JR      NZ,$6B06            ; {}
6AE5: 29              ADD     HL,HL               
6AE6: 26 33           LD      H,$33               
6AE8: 0F              RRCA                        
6AE9: 35              DEC     (HL)                
6AEA: 05              DEC     B                   
6AEB: 40              LD      B,B                 
6AEC: 05              DEC     B                   
6AED: 42              LD      B,D                 
6AEE: 05              DEC     B                   
6AEF: 47              LD      B,A                 
6AF0: 05              DEC     B                   
6AF1: 48              LD      C,B                 
6AF2: 2C              INC     L                   
6AF3: 49              LD      C,C                 
6AF4: 28 58           JR      Z,$6B4E             ; {}
6AF6: 28 88           JR      Z,$6A80             ; {}
6AF8: 50              LD      D,B                 
6AF9: 22              LD      (HLI),A             
6AFA: 46              LD      B,(HL)              
6AFB: CB E1           SET     1,E                 
6AFD: 0A              LD      A,(BC)              
6AFE: BA              CP      D                   
6AFF: 88              ADC     A,B                 
6B00: 42              LD      B,D                 
6B01: 39              ADD     HL,SP               
6B02: 24              INC     H                   
6B03: FE 04           CP      $04                 
6B05: 95              SUB     L                   
6B06: C5              PUSH    BC                  
6B07: 20 23           JR      NZ,$6B2C            ; {}
6B09: 30 F6           JR      NC,$6B01            ; {}
6B0B: 30 29           JR      NC,$6B36            ; {}
6B0D: 40              LD      B,B                 
6B0E: 0D              DEC     C                   
6B0F: 50              LD      D,B                 
6B10: 2B              DEC     HL                  
6B11: 00              NOP                         
6B12: DF              RST     0X18                
6B13: 01 25 88        LD      BC,$8825            
6B16: 02              LD      (BC),A              
6B17: 21 04 26        LD      HL,$2604            
6B1A: 82              ADD     A,D                 
6B1B: 05              DEC     B                   
6B1C: DF              RST     0X18                
6B1D: 07              RLCA                        
6B1E: 25              DEC     H                   
6B1F: 10 25           ;;STOP    $25                 
6B21: 11 29 12        LD      DE,$1229            
6B24: 0F              RRCA                        
6B25: 14              INC     D                   
6B26: 2A              LD      A,(HLI)             
6B27: 15              DEC     D                   
6B28: 26 16           LD      H,$16               
6B2A: 25              DEC     H                   
6B2B: 17              RLA                         
6B2C: 29              ADD     HL,HL               
6B2D: 18 0F           JR      $6B3E               ; {}
6B2F: C4 25 24        CALL    NZ,$2425            
6B32: C4 26 23        CALL    NZ,$2326            
6B35: 56              LD      D,(HL)              
6B36: 27              DAA                         
6B37: 57              LD      D,A                 
6B38: 2B              DEC     HL                  
6B39: 64              LD      H,H                 
6B3A: 2C              INC     L                   
6B3B: 65              LD      H,L                 
6B3C: 28 66           JR      Z,$6BA4             ; {}
6B3E: DF              RST     0X18                
6B3F: 67              LD      H,A                 
6B40: 27              DAA                         
6B41: 82              ADD     A,D                 
6B42: 68              LD      L,B                 
6B43: 22              LD      (HLI),A             
6B44: 70              LD      (HL),B              
6B45: 27              DAA                         
6B46: 83              ADD     A,E                 
6B47: 71              LD      (HL),C              
6B48: 22              LD      (HLI),A             
6B49: 74              LD      (HL),H              
6B4A: 28 85           JR      Z,$6AD1             ; {}
6B4C: 75              LD      (HL),L              
6B4D: DF              RST     0X18                
6B4E: 53              LD      D,E                 
6B4F: 0F              RRCA                        
6B50: 38 BE           JR      C,$6B10             ; {}
6B52: E1              POP     HL                  
6B53: 0A              LD      A,(BC)              
6B54: B9              CP      C                   
6B55: 68              LD      L,B                 
6B56: 52              LD      D,D                 
6B57: FE 04           CP      $04                 
6B59: 95              SUB     L                   
6B5A: 8A              ADC     A,D                 
6B5B: 00              NOP                         
6B5C: 21 8A 70        LD      HL,$708A            
6B5F: 22              LD      (HLI),A             
6B60: 82              ADD     A,D                 
6B61: 60              LD      H,B                 
6B62: 22              LD      (HLI),A             
6B63: 62              LD      H,D                 
6B64: 2B              DEC     HL                  
6B65: 82              ADD     A,D                 
6B66: 70              LD      (HL),B              
6B67: DF              RST     0X18                
6B68: 72              LD      (HL),D              
6B69: 27              DAA                         
6B6A: C5              PUSH    BC                  
6B6B: 10 0D           ;;STOP    $0D                 
6B6D: 11 0D 52        LD      DE,$520D            
6B70: 0D              DEC     C                   
6B71: 63              LD      H,E                 
6B72: 0D              DEC     C                   
6B73: 82              ADD     A,D                 
6B74: 68              LD      L,B                 
6B75: 0D              DEC     C                   
6B76: 82              ADD     A,D                 
6B77: 18 0D           JR      $6B86               ; {}
6B79: 27              DAA                         
6B7A: 0D              DEC     C                   
6B7B: 37              SCF                         
6B7C: 0F              RRCA                        
6B7D: 38 0D           JR      C,$6B8C             ; {}
6B7F: 84              ADD     A,H                 
6B80: 13              INC     DE                  
6B81: 01 83 23        LD      BC,$2383            
6B84: 01 26 B0        LD      BC,$B026            
6B87: 33              INC     SP                  
6B88: B0              OR      B                   
6B89: C2 34 01        JP      NZ,$0134            
6B8C: C2 35 01        JP      NZ,$0135            
6B8F: 46              LD      B,(HL)              
6B90: AF              XOR     A                   
6B91: 49              LD      C,C                 
6B92: AF              XOR     A                   
6B93: 86              ADD     A,(HL)              
6B94: 54              LD      D,H                 
6B95: B0              OR      B                   
6B96: 82              ADD     A,D                 
6B97: 57              LD      D,A                 
6B98: AE              XOR     (HL)                
6B99: 30 0F           JR      NC,$6BAA            ; {}
6B9B: 21 20 51        LD      HL,$5120            
6B9E: 4E              LD      C,(HL)              
6B9F: 82              ADD     A,D                 
6BA0: 66              LD      H,(HL)              
6BA1: 4E              LD      C,(HL)              
6BA2: 28 A0           JR      Z,$6B44             ; {}
6BA4: 36 A6           LD      (HL),$A6            
6BA6: 39              ADD     HL,SP               
6BA7: A6              AND     (HL)                
6BA8: 82              ADD     A,D                 
6BA9: 47              LD      B,A                 
6BAA: A6              AND     (HL)                
6BAB: 74              LD      (HL),H              
6BAC: FD                              
6BAD: E0 00           LD      ($FF00+$00),A       
6BAF: 18 68           JR      $6C19               ; {}
6BB1: 12              LD      (DE),A              
6BB2: FE 04           CP      $04                 
6BB4: 4D              LD      C,L                 
6BB5: 08 26 18        LD      ($1826),SP          
6BB8: 24              INC     H                   
6BB9: 28 2A           JR      Z,$6BE5             ; {}
6BBB: 29              ADD     HL,HL               
6BBC: 26 C2           LD      H,$C2               
6BBE: 09              ADD     HL,BC               
6BBF: DF              RST     0X18                
6BC0: 82              ADD     A,D                 
6BC1: 11 DF C2        LD      DE,$C2DF            
6BC4: 13              INC     DE                  
6BC5: A6              AND     (HL)                
6BC6: C4 14 01        CALL    NZ,$0114            
6BC9: C2 15 01        JP      NZ,$0115            
6BCC: C3 17 DF        JP      $DF17               
6BCF: 26 DF           LD      H,$DF               
6BD1: 83              ADD     A,E                 
6BD2: 30 A6           JR      NC,$6B7A            ; {}
6BD4: C2 33 01        JP      NZ,$0133            
6BD7: 35              DEC     (HL)                
6BD8: B0              OR      B                   
6BD9: 83              ADD     A,E                 
6BDA: 40              LD      B,B                 
6BDB: AF              XOR     A                   
6BDC: 45              LD      B,L                 
6BDD: 0F              RRCA                        
6BDE: C2 48 DF        JP      NZ,$DF48            
6BE1: 85              ADD     A,L                 
6BE2: 50              LD      D,B                 
6BE3: B0              OR      B                   
6BE4: 55              LD      D,L                 
6BE5: 05              DEC     B                   
6BE6: 56              LD      D,(HL)              
6BE7: DF              RST     0X18                
6BE8: 61              LD      H,C                 
6BE9: 05              DEC     B                   
6BEA: 64              LD      H,H                 
6BEB: DF              RST     0X18                
6BEC: 65              LD      H,L                 
6BED: DF              RST     0X18                
6BEE: 67              LD      H,A                 
6BEF: 05              DEC     B                   
6BF0: 68              LD      L,B                 
6BF1: 0F              RRCA                        
6BF2: 61              LD      H,C                 
6BF3: 4E              LD      C,(HL)              
6BF4: 72              LD      (HL),D              
6BF5: FD                              
6BF6: E0 00           LD      ($FF00+$00),A       
6BF8: 18 88           JR      $6B82               ; {}
6BFA: 12              LD      (DE),A              
6BFB: FE 04           CP      $04                 
6BFD: 05              DEC     B                   
6BFE: 03              INC     BC                  
6BFF: 29              ADD     HL,HL               
6C00: 04              INC     B                   
6C01: 05              DEC     B                   
6C02: 05              DEC     B                   
6C03: 2A              LD      A,(HLI)             
6C04: 08 26 09        LD      ($0926),SP          
6C07: DF              RST     0X18                
6C08: 87              ADD     A,A                 
6C09: 11 DF 18        LD      DE,$18DF            
6C0C: 2A              LD      A,(HLI)             
6C0D: 19              ADD     HL,DE               
6C0E: 26 C5           LD      H,$C5               
6C10: 21 DF 22        LD      HL,$22DF            
6C13: AF              XOR     A                   
6C14: C3 23 DD        JP      $DD23               
6C17: 24              INC     H                   
6C18: DD                              
6C19: 82              ADD     A,D                 
6C1A: 25              DEC     H                   
6C1B: AE              XOR     (HL)                
6C1C: 82              ADD     A,D                 
6C1D: 27              DAA                         
6C1E: DF              RST     0X18                
6C1F: 32              LD      (HLD),A             
6C20: B0              OR      B                   
6C21: 34              INC     (HL)                
6C22: A0              AND     B                   
6C23: C2 35 DD        JP      NZ,$DD35            
6C26: 82              ADD     A,D                 
6C27: 37              SCF                         
6C28: DF              RST     0X18                
6C29: 44              LD      B,H                 
6C2A: A7              AND     A                   
6C2B: 83              ADD     A,E                 
6C2C: 52              LD      D,D                 
6C2D: AE              XOR     (HL)                
6C2E: 55              LD      D,L                 
6C2F: A7              AND     A                   
6C30: 48              LD      C,B                 
6C31: 0D              DEC     C                   
6C32: 82              ADD     A,D                 
6C33: 57              LD      D,A                 
6C34: 0D              DEC     C                   
6C35: 66              LD      H,(HL)              
6C36: 2C              INC     L                   
6C37: 82              ADD     A,D                 
6C38: 67              LD      H,A                 
6C39: 22              LD      (HLI),A             
6C3A: 69              LD      L,C                 
6C3B: 28 76           JR      Z,$6CB3             ; {}
6C3D: 28 83           JR      Z,$6BC2             ; {}
6C3F: 77              LD      (HL),A              
6C40: DF              RST     0X18                
6C41: 74              LD      (HL),H              
6C42: FD                              
6C43: E0 00           LD      ($FF00+$00),A       
6C45: 62              LD      H,D                 
6C46: 78              LD      A,B                 
6C47: 42              LD      B,D                 
6C48: FE 04           CP      $04                 
6C4A: 8D              ADC     A,L                 
6C4B: C6 13           ADD     $13                 
6C4D: DF              RST     0X18                
6C4E: C4 31 DF        CALL    NZ,$DF31            
6C51: 22              LD      (HLI),A             
6C52: 2C              INC     L                   
6C53: 87              ADD     A,A                 
6C54: 23              INC     HL                  
6C55: 22              LD      (HLI),A             
6C56: C5              PUSH    BC                  
6C57: 32              LD      (HLD),A             
6C58: 24              INC     H                   
6C59: C4 43 11        CALL    NZ,$1143            
6C5C: 33              INC     SP                  
6C5D: 17              RLA                         
6C5E: 34              INC     (HL)                
6C5F: 12              LD      (DE),A              
6C60: 35              DEC     (HL)                
6C61: 2C              INC     L                   
6C62: 84              ADD     A,H                 
6C63: 36 22           LD      (HL),$22            
6C65: C4 45 24        CALL    NZ,$2445            
6C68: 46              LD      B,(HL)              
6C69: AC              XOR     H                   
6C6A: 83              ADD     A,E                 
6C6B: 47              LD      B,A                 
6C6C: 12              LD      (DE),A              
6C6D: C3 56 11        JP      $1156               
6C70: 83              ADD     A,E                 
6C71: 57              LD      D,A                 
6C72: 0F              RRCA                        
6C73: 83              ADD     A,E                 
6C74: 67              LD      H,A                 
6C75: 0F              RRCA                        
6C76: 83              ADD     A,E                 
6C77: 77              LD      (HL),A              
6C78: 0F              RRCA                        
6C79: 68              LD      L,B                 
6C7A: A0              AND     B                   
6C7B: 49              LD      C,C                 
6C7C: 16 C3           LD      D,$C3               
6C7E: 59              LD      E,C                 
6C7F: 10 FE           ;;STOP    $FE                 
6C81: 04              INC     B                   
6C82: 7D              LD      A,L                 
6C83: 86              ADD     A,(HL)              
6C84: 11 DF C4        LD      DE,$C4DF            
6C87: 38 DF           JR      C,$6C68             ; {}
6C89: 87              ADD     A,A                 
6C8A: 20 22           JR      NZ,$6CAE            ; {}
6C8C: 27              DAA                         
6C8D: 2B              DEC     HL                  
6C8E: C5              PUSH    BC                  
6C8F: 37              SCF                         
6C90: 23              INC     HL                  
6C91: 84              ADD     A,H                 
6C92: 30 22           JR      NC,$6CB6            ; {}
6C94: 34              INC     (HL)                
6C95: 2B              DEC     HL                  
6C96: 35              DEC     (HL)                
6C97: 12              LD      (DE),A              
6C98: 36 16           LD      (HL),$16            
6C9A: C4 46 10        CALL    NZ,$1046            
6C9D: C4 44 23        CALL    NZ,$2344            
6CA0: 83              ADD     A,E                 
6CA1: 40              LD      B,B                 
6CA2: 12              LD      (DE),A              
6CA3: 43              LD      B,E                 
6CA4: AC              XOR     H                   
6CA5: C3 53 10        JP      $1053               
6CA8: 83              ADD     A,E                 
6CA9: 50              LD      D,B                 
6CAA: 0F              RRCA                        
6CAB: 83              ADD     A,E                 
6CAC: 60              LD      H,B                 
6CAD: 0F              RRCA                        
6CAE: 83              ADD     A,E                 
6CAF: 70              LD      (HL),B              
6CB0: 0F              RRCA                        
6CB1: 61              LD      H,C                 
6CB2: A0              AND     B                   
6CB3: 40              LD      B,B                 
6CB4: 17              RLA                         
6CB5: C3 50 11        JP      $1150               
6CB8: FE 05           CP      $05                 
6CBA: 94              SUB     H                   
6CBB: 86              ADD     A,(HL)              
6CBC: 00              NOP                         
6CBD: 03              INC     BC                  
6CBE: 86              ADD     A,(HL)              
6CBF: 00              NOP                         
6CC0: 80              ADD     A,B                 
6CC1: 86              ADD     A,(HL)              
6CC2: 10 81           ;;STOP    $81                 
6CC4: 86              ADD     A,(HL)              
6CC5: 20 81           JR      NZ,$6C48            ; {}
6CC7: 86              ADD     A,(HL)              
6CC8: 30 81           JR      NC,$6C4B            ; {}
6CCA: 86              ADD     A,(HL)              
6CCB: 40              LD      B,B                 
6CCC: 81              ADD     A,C                 
6CCD: 86              ADD     A,(HL)              
6CCE: 50              LD      D,B                 
6CCF: 81              ADD     A,C                 
6CD0: 83              ADD     A,E                 
6CD1: 07              RLCA                        
6CD2: 54              LD      D,H                 
6CD3: 83              ADD     A,E                 
6CD4: 17              RLA                         
6CD5: 54              LD      D,H                 
6CD6: 83              ADD     A,E                 
6CD7: 27              DAA                         
6CD8: 54              LD      D,H                 
6CD9: 84              ADD     A,H                 
6CDA: 36 54           LD      (HL),$54            
6CDC: C3 06 51        JP      $5106               ; {}
6CDF: 35              DEC     (HL)                
6CE0: 50              LD      D,B                 
6CE1: 45              LD      B,L                 
6CE2: 52              LD      D,D                 
6CE3: 84              ADD     A,H                 
6CE4: 46              LD      B,(HL)              
6CE5: 5C              LD      E,H                 
6CE6: 56              LD      D,(HL)              
6CE7: 7D              LD      A,L                 
6CE8: 83              ADD     A,E                 
6CE9: 57              LD      D,A                 
6CEA: 84              ADD     A,H                 
6CEB: 8A              ADC     A,D                 
6CEC: 60              LD      H,B                 
6CED: 53              LD      D,E                 
6CEE: 61              LD      H,C                 
6CEF: 56              LD      D,(HL)              
6CF0: 62              LD      H,D                 
6CF1: 81              ADD     A,C                 
6CF2: 64              LD      H,H                 
6CF3: 50              LD      D,B                 
6CF4: 8A              ADC     A,D                 
6CF5: 70              LD      (HL),B              
6CF6: 54              LD      D,H                 
6CF7: 82              ADD     A,D                 
6CF8: 72              LD      (HL),D              
6CF9: 53              LD      D,E                 
6CFA: 25              DEC     H                   
6CFB: 72              LD      (HL),D              
6CFC: 50              LD      D,B                 
6CFD: 72              LD      (HL),D              
6CFE: 63              LD      H,E                 
6CFF: 72              LD      (HL),D              
6D00: 84              ADD     A,H                 
6D01: 66              LD      H,(HL)              
6D02: 5B              LD      E,E                 
6D03: E0 00           LD      ($FF00+$00),A       
6D05: D9              RETI                        
6D06: 28 60           JR      Z,$6D68             ; {}
6D08: FE 05           CP      $05                 
6D0A: 94              SUB     H                   
6D0B: 86              ADD     A,(HL)              
6D0C: 03              INC     BC                  
6D0D: 80              ADD     A,B                 
6D0E: 86              ADD     A,(HL)              
6D0F: 13              INC     DE                  
6D10: 81              ADD     A,C                 
6D11: 86              ADD     A,(HL)              
6D12: 23              INC     HL                  
6D13: 81              ADD     A,C                 
6D14: 86              ADD     A,(HL)              
6D15: 33              INC     SP                  
6D16: 81              ADD     A,C                 
6D17: 86              ADD     A,(HL)              
6D18: 43              LD      B,E                 
6D19: 81              ADD     A,C                 
6D1A: 86              ADD     A,(HL)              
6D1B: 53              LD      D,E                 
6D1C: 81              ADD     A,C                 
6D1D: C4 00 54        CALL    NZ,$5400            ; {}
6D20: C4 01 54        CALL    NZ,$5401            ; {}
6D23: C3 02 57        JP      $5702               ; {}
6D26: 32              LD      (HLD),A             
6D27: 54              LD      D,H                 
6D28: 33              INC     SP                  
6D29: 56              LD      D,(HL)              
6D2A: 83              ADD     A,E                 
6D2B: 40              LD      B,B                 
6D2C: 5C              LD      E,H                 
6D2D: 43              LD      B,E                 
6D2E: 58              LD      E,B                 
6D2F: 82              ADD     A,D                 
6D30: 50              LD      D,B                 
6D31: 84              ADD     A,H                 
6D32: 52              LD      D,D                 
6D33: 7E              LD      A,(HL)              
6D34: 83              ADD     A,E                 
6D35: 60              LD      H,B                 
6D36: 5B              LD      E,E                 
6D37: 63              LD      H,E                 
6D38: 53              LD      D,E                 
6D39: 8A              ADC     A,D                 
6D3A: 70              LD      (HL),B              
6D3B: 54              LD      D,H                 
6D3C: 68              LD      L,B                 
6D3D: 54              LD      D,H                 
6D3E: C3 49 54        JP      $5449               ; {}
6D41: C4 09 51        CALL    NZ,$5109            ; {}
6D44: 48              LD      C,B                 
6D45: 50              LD      D,B                 
6D46: 58              LD      E,B                 
6D47: 51              LD      D,C                 
6D48: 67              LD      H,A                 
6D49: 50              LD      D,B                 
6D4A: 65              LD      H,L                 
6D4B: 81              ADD     A,C                 
6D4C: 82              ADD     A,D                 
6D4D: 75              LD      (HL),L              
6D4E: 53              LD      D,E                 
6D4F: 23              INC     HL                  
6D50: 72              LD      (HL),D              
6D51: 38 72           JR      C,$6DC5             ; {}
6D53: 54              LD      D,H                 
6D54: 72              LD      (HL),D              
6D55: 57              LD      D,A                 
6D56: 72              LD      (HL),D              
6D57: 66              LD      H,(HL)              
6D58: 72              LD      (HL),D              
6D59: 64              LD      H,H                 
6D5A: 56              LD      D,(HL)              
6D5B: E0 00           LD      ($FF00+$00),A       
6D5D: D9              RETI                        
6D5E: 48              LD      C,B                 
6D5F: 60              LD      H,B                 
6D60: FE 04           CP      $04                 
6D62: 8D              ADC     A,L                 
6D63: 82              ADD     A,D                 
6D64: 00              NOP                         
6D65: 03              INC     BC                  
6D66: 02              LD      (BC),A              
6D67: 25              DEC     H                   
6D68: 04              INC     B                   
6D69: C7              RST     0X00                
6D6A: 08 C7 10        LD      ($10C7),SP          
6D6D: 03              INC     BC                  
6D6E: 11 25 12        LD      DE,$1225            
6D71: 29              ADD     HL,HL               
6D72: 87              ADD     A,A                 
6D73: 13              INC     DE                  
6D74: 0F              RRCA                        
6D75: 20 25           JR      NZ,$6D9C            ; {}
6D77: 21 29 22        LD      HL,$2229            
6D7A: 0F              RRCA                        
6D7B: 23              INC     HL                  
6D7C: 96              SUB     (HL)                
6D7D: 86              ADD     A,(HL)              
6D7E: 24              INC     H                   
6D7F: 13              INC     DE                  
6D80: 31 AC 32        LD      SP,$32AC            
6D83: 13              INC     DE                  
6D84: 33              INC     SP                  
6D85: 14              INC     D                   
6D86: 34              INC     (HL)                
6D87: 25              DEC     H                   
6D88: 85              ADD     A,L                 
6D89: 35              DEC     (HL)                
6D8A: 21 40 29        LD      HL,$2940            
6D8D: 41              LD      B,C                 
6D8E: 25              DEC     H                   
6D8F: 82              ADD     A,D                 
6D90: 42              LD      B,D                 
6D91: 21 44 29        LD      HL,$2944            
6D94: 45              LD      B,L                 
6D95: AC              XOR     H                   
6D96: 50              LD      D,B                 
6D97: 25              DEC     H                   
6D98: 51              LD      D,C                 
6D99: 29              ADD     HL,HL               
6D9A: 61              LD      H,C                 
6D9B: AC              XOR     H                   
6D9C: 73              LD      (HL),E              
6D9D: C0              RET     NZ                  
6D9E: 76              HALT                        
6D9F: C0              RET     NZ                  
6DA0: 79              LD      A,C                 
6DA1: 2C              INC     L                   
6DA2: 06 A3           LD      B,$A3               
6DA4: E1              POP     HL                  
6DA5: 14              INC     D                   
6DA6: C5              PUSH    BC                  
6DA7: 48              LD      C,B                 
6DA8: 10 FE           ;;STOP    $FE                 
6DAA: 04              INC     B                   
6DAB: 4D              LD      C,L                 
6DAC: 07              RLCA                        
6DAD: 26 82           LD      H,$82               
6DAF: 08 03 87        LD      ($8703),SP          
6DB2: 10 0F           ;;STOP    $0F                 
6DB4: 17              RLA                         
6DB5: 2A              LD      A,(HLI)             
6DB6: 18 26           JR      $6DDE               ; {}
6DB8: 19              ADD     HL,DE               
6DB9: 03              INC     BC                  
6DBA: 86              ADD     A,(HL)              
6DBB: 20 13           JR      NZ,$6DD0            ; {}
6DBD: 22              LD      (HLI),A             
6DBE: 0D              DEC     C                   
6DBF: 26 95           LD      H,$95               
6DC1: 27              DAA                         
6DC2: 0F              RRCA                        
6DC3: 28 2A           JR      Z,$6DEF             ; {}
6DC5: 29              ADD     HL,HL               
6DC6: 26 85           LD      H,$85               
6DC8: 30 21           JR      NC,$6DEB            ; {}
6DCA: 32              LD      (HLD),A             
6DCB: 98              SBC     B                   
6DCC: 35              DEC     (HL)                
6DCD: 26 36           LD      H,$36               
6DCF: 15              DEC     D                   
6DD0: 37              SCF                         
6DD1: 13              INC     DE                  
6DD2: 38 AC           JR      C,$6D80             ; {}
6DD4: 44              LD      B,H                 
6DD5: AC              XOR     H                   
6DD6: 45              LD      B,L                 
6DD7: 2A              LD      A,(HLI)             
6DD8: 82              ADD     A,D                 
6DD9: 46              LD      B,(HL)              
6DDA: 21 48 26        LD      HL,$2648            
6DDD: 49              LD      C,C                 
6DDE: 2A              LD      A,(HLI)             
6DDF: 57              LD      D,A                 
6DE0: AC              XOR     H                   
6DE1: 58              LD      E,B                 
6DE2: 2A              LD      A,(HLI)             
6DE3: 59              LD      E,C                 
6DE4: 26 67           LD      H,$67               
6DE6: 0F              RRCA                        
6DE7: 68              LD      L,B                 
6DE8: AA              XOR     D                   
6DE9: FE 04           CP      $04                 
6DEB: 73              LD      (HL),E              
6DEC: 85              ADD     A,L                 
6DED: 00              NOP                         
6DEE: 03              INC     BC                  
6DEF: C3 59 03        JP      $0359               
6DF2: 05              DEC     B                   
6DF3: 25              DEC     H                   
6DF4: C2 15 23        JP      NZ,$2315            
6DF7: 35              DEC     (HL)                
6DF8: 27              DAA                         
6DF9: 36 2B           LD      (HL),$2B            
6DFB: 46              LD      B,(HL)              
6DFC: 23              INC     HL                  
6DFD: 53              LD      D,E                 
6DFE: 25              DEC     H                   
6DFF: 82              ADD     A,D                 
6E00: 54              LD      D,H                 
6E01: 21 56 29        LD      HL,$2956            
6E04: C2 58 24        JP      NZ,$2458            
6E07: 78              LD      A,B                 
6E08: 28 C2           JR      Z,$6DCC             ; {}
6E0A: 63              LD      H,E                 
6E0B: 23              INC     HL                  
6E0C: 75              LD      (HL),L              
6E0D: 2C              INC     L                   
6E0E: 82              ADD     A,D                 
6E0F: 76              HALT                        
6E10: 22              LD      (HLI),A             
6E11: 16 AB           LD      D,$AB               
6E13: C2 17 0D        JP      NZ,$0D17            
6E16: 26 0D           LD      H,$0D               
6E18: C2 28 0D        JP      NZ,$0D28            
6E1B: C3 37 0D        JP      $0D37               
6E1E: 82              ADD     A,D                 
6E1F: 64              LD      H,H                 
6E20: 0D              DEC     C                   
6E21: 82              ADD     A,D                 
6E22: 66              LD      H,(HL)              
6E23: 0D              DEC     C                   
6E24: 74              LD      (HL),H              
6E25: 0D              DEC     C                   
6E26: 48              LD      C,B                 
6E27: 2C              INC     L                   
6E28: 49              LD      C,C                 
6E29: 28 18           JR      Z,$6E43             ; {}
6E2B: CB C2           SET     1,E                 
6E2D: 17              RLA                         
6E2E: 07              RLCA                        
6E2F: 26 07           LD      H,$07               
6E31: C2 28 07        JP      NZ,$0728            
6E34: C3 37 07        JP      $0737               
6E37: 82              ADD     A,D                 
6E38: 64              LD      H,H                 
6E39: 07              RLCA                        
6E3A: 82              ADD     A,D                 
6E3B: 66              LD      H,(HL)              
6E3C: 07              RLCA                        
6E3D: 74              LD      (HL),H              
6E3E: 07              RLCA                        
6E3F: E0 00           LD      ($FF00+$00),A       
6E41: 4A              LD      C,D                 
6E42: 88              ADC     A,B                 
6E43: 30 FE           JR      NC,$6E43            ; {}
6E45: 04              INC     B                   
6E46: 0D              DEC     C                   
6E47: 03              INC     BC                  
6E48: C7              RST     0X00                
6E49: 05              DEC     B                   
6E4A: C7              RST     0X00                
6E4B: 00              NOP                         
6E4C: 03              INC     BC                  
6E4D: 01 25 10        LD      BC,$1025            
6E50: 25              DEC     H                   
6E51: 11 29 14        LD      DE,$1429            
6E54: 0F              RRCA                        
6E55: 20 29           JR      NZ,$6E80            ; {}
6E57: 89              ADC     A,C                 
6E58: 21 13 24        LD      HL,$2413            
6E5B: 0D              DEC     C                   
6E5C: 30 25           JR      NC,$6E83            ; {}
6E5E: 88              ADC     A,B                 
6E5F: 31 21 39        LD      SP,$3921            
6E62: 26 34           LD      H,$34               
6E64: 98              SBC     B                   
6E65: 52              LD      D,D                 
6E66: AC              XOR     H                   
6E67: 57              LD      D,A                 
6E68: AC              XOR     H                   
6E69: 09              ADD     HL,BC               
6E6A: 21 19 0D        LD      HL,$0D19            
6E6D: 32              LD      (HLD),A             
6E6E: 90              SUB     B                   
6E6F: 37              SCF                         
6E70: 90              SUB     B                   
6E71: 04              INC     B                   
6E72: A2              AND     D                   
6E73: E1              POP     HL                  
6E74: 14              INC     D                   
6E75: C2 68 10        JP      NZ,$1068            
6E78: FE 04           CP      $04                 
6E7A: 4D              LD      C,L                 
6E7B: 74              LD      (HL),H              
6E7C: F1              POP     AF                  
6E7D: 01 29 02        LD      BC,$0229            
6E80: 25              DEC     H                   
6E81: C7              RST     0X00                
6E82: 11 10 C5        LD      DE,$C510            
6E85: 30 11           JR      NC,$6E98            ; {}
6E87: 20 95           JR      NZ,$6E1E            ; {}
6E89: C6 12           ADD     $12                 
6E8B: 23              INC     HL                  
6E8C: 72              LD      (HL),D              
6E8D: 27              DAA                         
6E8E: 67              LD      H,A                 
6E8F: 2C              INC     L                   
6E90: 68              LD      L,B                 
6E91: 22              LD      (HLI),A             
6E92: 69              LD      L,C                 
6E93: 28 77           JR      Z,$6F0C             ; {}
6E95: 28 82           JR      Z,$6E19             ; {}
6E97: 78              LD      A,B                 
6E98: 03              INC     BC                  
6E99: C5              PUSH    BC                  
6E9A: 23              INC     HL                  
6E9B: DF              RST     0X18                
6E9C: 86              ADD     A,(HL)              
6E9D: 13              INC     DE                  
6E9E: DF              RST     0X18                
6E9F: C4 28 DF        CALL    NZ,$DF28            
6EA2: 13              INC     DE                  
6EA3: AC              XOR     H                   
6EA4: 18 AC           JR      $6E52               ; {}
6EA6: FE 04           CP      $04                 
6EA8: 0D              DEC     C                   
6EA9: 00              NOP                         
6EAA: 17              RLA                         
6EAB: 01 12 02        LD      BC,$0212            
6EAE: 99              SBC     C                   
6EAF: 03              INC     BC                  
6EB0: 16 C2           LD      D,$C2               
6EB2: 10 11           ;;STOP    $11                 
6EB4: 13              INC     DE                  
6EB5: 10 23           ;;STOP    $23                 
6EB7: 14              INC     D                   
6EB8: 12              LD      (DE),A              
6EB9: 9A              SBC     D                   
6EBA: 11 C5 21        LD      DE,$21C5            
6EBD: C6 04           ADD     $04                 
6EBF: 25              DEC     H                   
6EC0: 30 25           JR      NC,$6EE7            ; {}
6EC2: C2 14 23        JP      NZ,$2314            
6EC5: 83              ADD     A,E                 
6EC6: 31 21 34        LD      SP,$3421            
6EC9: 29              ADD     HL,HL               
6ECA: 32              LD      (HLD),A             
6ECB: 98              SBC     B                   
6ECC: C3 41 20        JP      $2041               
6ECF: 17              RLA                         
6ED0: A7              AND     A                   
6ED1: 27              DAA                         
6ED2: CE 57           ADC     $57                 
6ED4: CE 28           ADC     $28                 
6ED6: C0              RET     NZ                  
6ED7: 37              SCF                         
6ED8: C0              RET     NZ                  
6ED9: 74              LD      (HL),H              
6EDA: FD                              
6EDB: E0 00           LD      ($FF00+$00),A       
6EDD: D6 48           SUB     $48                 
6EDF: 50              LD      D,B                 
6EE0: FE 04           CP      $04                 
6EE2: 9D              SBC     L                   
6EE3: 00              NOP                         
6EE4: 00              NOP                         
6EE5: 01 25 87        LD      BC,$8725            
6EE8: 02              LD      (BC),A              
6EE9: 21 09 26        LD      HL,$2609            
6EEC: 04              INC     B                   
6EED: 26 05           LD      H,$05               
6EEF: 25              DEC     H                   
6EF0: 10 25           ;;STOP    $25                 
6EF2: 11 29 C3        LD      DE,$C329            
6EF5: 14              INC     D                   
6EF6: 24              INC     H                   
6EF7: C2 15 23        JP      NZ,$2315            
6EFA: 19              ADD     HL,DE               
6EFB: 24              INC     H                   
6EFC: 40              LD      B,B                 
6EFD: 27              DAA                         
6EFE: 41              LD      B,C                 
6EFF: 2B              DEC     HL                  
6F00: C3 50 23        JP      $2350               
6F03: 43              LD      B,E                 
6F04: 2C              INC     L                   
6F05: 44              LD      B,H                 
6F06: 28 C3           JR      Z,$6ECB             ; {}
6F08: 53              LD      D,E                 
6F09: 24              INC     H                   
6F0A: 35              DEC     (HL)                
6F0B: 27              DAA                         
6F0C: 36 2B           LD      (HL),$2B            
6F0E: 46              LD      B,(HL)              
6F0F: 23              INC     HL                  
6F10: 55              LD      D,L                 
6F11: 25              DEC     H                   
6F12: 56              LD      D,(HL)              
6F13: 29              ADD     HL,HL               
6F14: C2 65 23        JP      NZ,$2365            
6F17: 28 2C           JR      Z,$6F45             ; {}
6F19: 29              ADD     HL,HL               
6F1A: 28 C4           JR      Z,$6EE0             ; {}
6F1C: 38 24           JR      C,$6F42             ; {}
6F1E: 77              LD      (HL),A              
6F1F: 2C              INC     L                   
6F20: 78              LD      A,B                 
6F21: 28 C4           JR      Z,$6EE7             ; {}
6F23: 50              LD      D,B                 
6F24: 00              NOP                         
6F25: 45              LD      B,L                 
6F26: 00              NOP                         
6F27: C3 54 00        JP      $0054               
6F2A: C5              PUSH    BC                  
6F2B: 39              ADD     HL,SP               
6F2C: 00              NOP                         
6F2D: 22              LD      (HLI),A             
6F2E: A0              AND     B                   
6F2F: 52              LD      D,D                 
6F30: AE              XOR     (HL)                
6F31: 62              LD      H,D                 
6F32: A7              AND     A                   
6F33: C2 20 23        JP      NZ,$2320            
6F36: C3 51 23        JP      $2351               
6F39: 18 CB           JR      $6F06               ; {}
6F3B: E1              POP     HL                  
6F3C: 11 CA 28        LD      DE,$28CA            
6F3F: 20 FE           JR      NZ,$6F3F            ; {}
6F41: 04              INC     B                   
6F42: 90              SUB     B                   
6F43: 84              ADD     A,H                 
6F44: 46              LD      B,(HL)              
6F45: 05              DEC     B                   
6F46: 84              ADD     A,H                 
6F47: 56              LD      D,(HL)              
6F48: 05              DEC     B                   
6F49: 84              ADD     A,H                 
6F4A: 66              LD      H,(HL)              
6F4B: 05              DEC     B                   
6F4C: C6 00           ADD     $00                 
6F4E: 24              INC     H                   
6F4F: 60              LD      H,B                 
6F50: 2A              LD      A,(HLI)             
6F51: 82              ADD     A,D                 
6F52: 61              LD      H,C                 
6F53: 21 63 29        LD      HL,$2963            
6F56: 03              INC     BC                  
6F57: 25              DEC     H                   
6F58: 12              LD      (DE),A              
6F59: 25              DEC     H                   
6F5A: 13              INC     DE                  
6F5B: 29              ADD     HL,HL               
6F5C: C2 22 23        JP      NZ,$2322            
6F5F: 42              LD      B,D                 
6F60: 27              DAA                         
6F61: 43              LD      B,E                 
6F62: 2B              DEC     HL                  
6F63: 53              LD      D,E                 
6F64: 23              INC     HL                  
6F65: 86              ADD     A,(HL)              
6F66: 04              INC     B                   
6F67: 21 35 25        LD      HL,$2535            
6F6A: 44              LD      B,H                 
6F6B: 25              DEC     H                   
6F6C: 45              LD      B,L                 
6F6D: 29              ADD     HL,HL               
6F6E: 84              ADD     A,H                 
6F6F: 36 21           LD      (HL),$21            
6F71: 37              SCF                         
6F72: 98              SBC     B                   
6F73: C2 54 23        JP      NZ,$2354            
6F76: 74              LD      (HL),H              
6F77: 27              DAA                         
6F78: 85              ADD     A,L                 
6F79: 75              LD      (HL),L              
6F7A: 22              LD      (HLI),A             
6F7B: 85              ADD     A,L                 
6F7C: 25              DEC     H                   
6F7D: 13              INC     DE                  
6F7E: 86              ADD     A,(HL)              
6F7F: 14              INC     D                   
6F80: 0D              DEC     C                   
6F81: 82              ADD     A,D                 
6F82: 23              INC     HL                  
6F83: 0D              DEC     C                   
6F84: 27              DAA                         
6F85: 0D              DEC     C                   
6F86: 34              INC     (HL)                
6F87: AC              XOR     H                   
6F88: 82              ADD     A,D                 
6F89: 47              LD      B,A                 
6F8A: 0D              DEC     C                   
6F8B: 55              LD      D,L                 
6F8C: 0D              DEC     C                   
6F8D: 57              LD      D,A                 
6F8E: 0D              DEC     C                   
6F8F: 58              LD      E,B                 
6F90: 0F              RRCA                        
6F91: 82              ADD     A,D                 
6F92: 65              LD      H,L                 
6F93: 0D              DEC     C                   
6F94: 68              LD      L,B                 
6F95: 0D              DEC     C                   
6F96: 33              INC     SP                  
6F97: 0D              DEC     C                   
6F98: 77              LD      (HL),A              
6F99: FD                              
6F9A: E0 00           LD      ($FF00+$00),A       
6F9C: C6 38           ADD     $38                 
6F9E: 50              LD      D,B                 
6F9F: FE 04           CP      $04                 
6FA1: 90              SUB     B                   
6FA2: 88              ADC     A,B                 
6FA3: 40              LD      B,B                 
6FA4: 05              DEC     B                   
6FA5: 88              ADC     A,B                 
6FA6: 50              LD      D,B                 
6FA7: 05              DEC     B                   
6FA8: 88              ADC     A,B                 
6FA9: 60              LD      H,B                 
6FAA: 05              DEC     B                   
6FAB: 88              ADC     A,B                 
6FAC: 70              LD      (HL),B              
6FAD: 05              DEC     B                   
6FAE: 83              ADD     A,E                 
6FAF: 00              NOP                         
6FB0: 21 03 26        LD      HL,$2603            
6FB3: 13              INC     DE                  
6FB4: 2A              LD      A,(HLI)             
6FB5: 14              INC     D                   
6FB6: 26 24           LD      H,$24               
6FB8: 2A              LD      A,(HLI)             
6FB9: 25              DEC     H                   
6FBA: 21 C2 06        LD      HL,$06C2            
6FBD: 23              INC     HL                  
6FBE: 26 29           LD      H,$29               
6FC0: 11 0D 84        LD      DE,$840D            
6FC3: 20 13           JR      NZ,$6FD8            ; {}
6FC5: 87              ADD     A,A                 
6FC6: 30 21           JR      NC,$6FE9            ; {}
6FC8: 37              SCF                         
6FC9: 26 47           LD      H,$47               
6FCB: 2A              LD      A,(HLI)             
6FCC: 48              LD      C,B                 
6FCD: 26 C2           LD      H,$C2               
6FCF: 58              LD      E,B                 
6FD0: 24              INC     H                   
6FD1: 88              ADC     A,B                 
6FD2: 70              LD      (HL),B              
6FD3: 22              LD      (HLI),A             
6FD4: 40              LD      B,B                 
6FD5: 0D              DEC     C                   
6FD6: 42              LD      B,D                 
6FD7: 0D              DEC     C                   
6FD8: 46              LD      B,(HL)              
6FD9: 0D              DEC     C                   
6FDA: 82              ADD     A,D                 
6FDB: 54              LD      D,H                 
6FDC: 0D              DEC     C                   
6FDD: 62              LD      H,D                 
6FDE: 0D              DEC     C                   
6FDF: 83              ADD     A,E                 
6FE0: 65              LD      H,L                 
6FE1: 0D              DEC     C                   
6FE2: 43              LD      B,E                 
6FE3: 0F              RRCA                        
6FE4: 66              LD      H,(HL)              
6FE5: 0F              RRCA                        
6FE6: 78              LD      A,B                 
6FE7: 28 12           JR      Z,$6FFB             ; {}
6FE9: BE              CP      (HL)                
6FEA: E1              POP     HL                  
6FEB: 11 C8 88        LD      DE,$88C8            
6FEE: 20 FE           JR      NZ,$6FEE            ; {}
6FF0: 04              INC     B                   
6FF1: 91              SUB     C                   
6FF2: 84              ADD     A,H                 
6FF3: 43              LD      B,E                 
6FF4: 0D              DEC     C                   
6FF5: 84              ADD     A,H                 
6FF6: 53              LD      D,E                 
6FF7: 0D              DEC     C                   
6FF8: 84              ADD     A,H                 
6FF9: 63              LD      H,E                 
6FFA: 0D              DEC     C                   
6FFB: 32              LD      (HLD),A             
6FFC: 25              DEC     H                   
6FFD: 84              ADD     A,H                 
6FFE: 33              INC     SP                  
6FFF: 21 37 26        LD      HL,$2637            
7002: C3 42 23        JP      $2342               
7005: 72              LD      (HL),D              
7006: 27              DAA                         
7007: 84              ADD     A,H                 
7008: 73              LD      (HL),E              
7009: 22              LD      (HLI),A             
700A: C4 47 24        CALL    NZ,$2447            
700D: 34              INC     (HL)                
700E: 99              SBC     C                   
700F: 44              LD      B,H                 
7010: 9A              SBC     D                   
7011: 55              LD      D,L                 
7012: C0              RET     NZ                  
7013: 77              LD      (HL),A              
7014: 28 74           JR      Z,$708A             ; {}
7016: FD                              
7017: E0 00           LD      ($FF00+$00),A       
7019: B2              OR      D                   
701A: 58              LD      E,B                 
701B: 52              LD      D,D                 
701C: FE 04           CP      $04                 
701E: 91              SUB     C                   
701F: 84              ADD     A,H                 
7020: 43              LD      B,E                 
7021: 0D              DEC     C                   
7022: 84              ADD     A,H                 
7023: 53              LD      D,E                 
7024: 0D              DEC     C                   
7025: 84              ADD     A,H                 
7026: 63              LD      H,E                 
7027: 0D              DEC     C                   
7028: 32              LD      (HLD),A             
7029: 25              DEC     H                   
702A: 84              ADD     A,H                 
702B: 33              INC     SP                  
702C: 21 37 26        LD      HL,$2637            
702F: C3 42 23        JP      $2342               
7032: 72              LD      (HL),D              
7033: 27              DAA                         
7034: 84              ADD     A,H                 
7035: 73              LD      (HL),E              
7036: 22              LD      (HLI),A             
7037: C4 47 24        CALL    NZ,$2447            
703A: 34              INC     (HL)                
703B: 99              SBC     C                   
703C: 44              LD      B,H                 
703D: 9A              SBC     D                   
703E: 55              LD      D,L                 
703F: C0              RET     NZ                  
7040: 77              LD      (HL),A              
7041: 28 74           JR      Z,$70B7             ; {}
7043: FD                              
7044: E0 00           LD      ($FF00+$00),A       
7046: 4B              LD      C,E                 
7047: 48              LD      C,B                 
7048: 22              LD      (HLI),A             
7049: FE 04           CP      $04                 
704B: 0D              DEC     C                   
704C: 12              LD      (DE),A              
704D: DF              RST     0X18                
704E: 82              ADD     A,D                 
704F: 14              INC     D                   
7050: 05              DEC     B                   
7051: 16 A7           LD      D,$A7               
7053: 25              DEC     H                   
7054: A7              AND     A                   
7055: 34              INC     (HL)                
7056: A7              AND     A                   
7057: 36 A7           LD      (HL),$A7            
7059: 45              LD      B,L                 
705A: A7              AND     A                   
705B: 53              LD      D,E                 
705C: A7              AND     A                   
705D: 55              LD      D,L                 
705E: A7              AND     A                   
705F: 66              LD      H,(HL)              
7060: A7              AND     A                   
7061: 21 0F 23        LD      HL,$230F            
7064: 05              DEC     B                   
7065: 24              INC     H                   
7066: A0              AND     B                   
7067: 26 DF           LD      H,$DF               
7069: 27              DAA                         
706A: 0F              RRCA                        
706B: 28 20           JR      Z,$708D             ; {}
706D: 32              LD      (HLD),A             
706E: 05              DEC     B                   
706F: 33              INC     SP                  
7070: DF              RST     0X18                
7071: 35              DEC     (HL)                
7072: 05              DEC     B                   
7073: 43              LD      B,E                 
7074: 0F              RRCA                        
7075: 44              LD      B,H                 
7076: DF              RST     0X18                
7077: 46              LD      B,(HL)              
7078: 05              DEC     B                   
7079: 48              LD      C,B                 
707A: 0F              RRCA                        
707B: 51              LD      D,C                 
707C: 05              DEC     B                   
707D: 61              LD      H,C                 
707E: 20 62           JR      NZ,$70E2            ; {}
7080: 05              DEC     B                   
7081: 68              LD      L,B                 
7082: 05              DEC     B                   
7083: 74              LD      (HL),H              
7084: FD                              
7085: E0 00           LD      ($FF00+$00),A       
7087: 84              ADD     A,H                 
7088: 98              SBC     B                   
7089: 62              LD      H,D                 
708A: FE 04           CP      $04                 
708C: 5D              LD      E,L                 
708D: 73              LD      (HL),E              
708E: C8              RET     Z                   
708F: 76              HALT                        
7090: C8              RET     Z                   
7091: C4 11 DF        CALL    NZ,$DF11            
7094: C5              PUSH    BC                  
7095: 02              LD      (BC),A              
7096: 24              INC     H                   
7097: C4 03 11        CALL    NZ,$1103            
709A: C2 05 24        JP      NZ,$2405            
709D: 06 11           LD      B,$11               
709F: 83              ADD     A,E                 
70A0: 07              RLCA                        
70A1: 0F              RRCA                        
70A2: 52              LD      D,D                 
70A3: 2A              LD      A,(HLI)             
70A4: 43              LD      B,E                 
70A5: 15              DEC     D                   
70A6: 86              ADD     A,(HL)              
70A7: 44              LD      B,H                 
70A8: 13              INC     DE                  
70A9: 66              LD      H,(HL)              
70AA: AC              XOR     H                   
70AB: C2 05 24        JP      NZ,$2405            
70AE: 25              DEC     H                   
70AF: 2A              LD      A,(HLI)             
70B0: 84              ADD     A,H                 
70B1: 26 21           LD      H,$21               
70B3: 16 AC           LD      D,$AC               
70B5: 83              ADD     A,E                 
70B6: 17              RLA                         
70B7: 13              INC     DE                  
70B8: 18 0D           JR      $70C7               ; {}
70BA: 83              ADD     A,E                 
70BB: 07              RLCA                        
70BC: 0F              RRCA                        
70BD: 28 98           JR      Z,$7057             ; {}
70BF: 87              ADD     A,A                 
70C0: 53              LD      D,E                 
70C1: 21 09 10        LD      HL,$1009            
70C4: 19              ADD     HL,DE               
70C5: 14              INC     D                   
70C6: 39              ADD     HL,SP               
70C7: 10 44           ;;STOP    $44                 
70C9: 95              SUB     L                   
70CA: 45              LD      B,L                 
70CB: 96              SUB     (HL)                
70CC: 47              LD      B,A                 
70CD: 0D              DEC     C                   
70CE: 49              LD      C,C                 
70CF: 14              INC     D                   
70D0: 57              LD      D,A                 
70D1: 98              SBC     B                   
70D2: 74              LD      (HL),H              
70D3: FD                              
70D4: E1              POP     HL                  
70D5: 13              INC     DE                  
70D6: AA              XOR     D                   
70D7: 48              LD      C,B                 
70D8: 48              LD      C,B                 
70D9: FE 04           CP      $04                 
70DB: 6D              LD      L,L                 
70DC: 83              ADD     A,E                 
70DD: 00              NOP                         
70DE: 0F              RRCA                        
70DF: 03              INC     BC                  
70E0: 10 C2           ;;STOP    $C2                 
70E2: 04              INC     B                   
70E3: 23              INC     HL                  
70E4: C4 06 10        CALL    NZ,$1006            
70E7: C5              PUSH    BC                  
70E8: 07              RLCA                        
70E9: 23              INC     HL                  
70EA: C4 18 DF        CALL    NZ,$DF18            
70ED: 86              ADD     A,(HL)              
70EE: 40              LD      B,B                 
70EF: 13              INC     DE                  
70F0: 42              LD      B,D                 
70F1: 0D              DEC     C                   
70F2: 87              ADD     A,A                 
70F3: 50              LD      D,B                 
70F4: 21 52 98        LD      HL,$9852            
70F7: 46              LD      B,(HL)              
70F8: 14              INC     D                   
70F9: 24              INC     H                   
70FA: 29              ADD     HL,HL               
70FB: 57              LD      D,A                 
70FC: 29              ADD     HL,HL               
70FD: 13              INC     DE                  
70FE: AC              XOR     H                   
70FF: 84              ADD     A,H                 
7100: 20 21           JR      NZ,$7123            ; {}
7102: 83              ADD     A,E                 
7103: 10 13           ;;STOP    $13                 
7105: 11 0D 00        LD      DE,$000D            
7108: 11 10 15        LD      DE,$1510            
710B: 21 98 30        LD      HL,$3098            
710E: 11 40 15        LD      DE,$1540            
7111: 61              LD      H,C                 
7112: 4E              LD      C,(HL)              
7113: FE 0C           CP      $0C                 
7115: 90              SUB     B                   
7116: 86              ADD     A,(HL)              
7117: 21 05 86        LD      HL,$8605            
711A: 31 05 85        LD      SP,$8505            
711D: 41              LD      B,C                 
711E: 05              DEC     B                   
711F: 84              ADD     A,H                 
7120: 51              LD      D,C                 
7121: 05              DEC     B                   
7122: 11 25 86        LD      DE,$8625            
7125: 12              LD      (DE),A              
7126: 21 18 26        LD      HL,$2618            
7129: 13              INC     DE                  
712A: C7              RST     0X00                
712B: 16 C7           LD      D,$C7               
712D: 20 25           JR      NZ,$7154            ; {}
712F: 21 29 28        LD      HL,$2829            
7132: 2A              LD      A,(HLI)             
7133: 29              ADD     HL,HL               
7134: 21 C2 30        LD      HL,$30C2            
7137: 23              INC     HL                  
7138: 50              LD      D,B                 
7139: 27              DAA                         
713A: 51              LD      D,C                 
713B: 2B              DEC     HL                  
713C: 58              LD      E,B                 
713D: 2C              INC     L                   
713E: 59              LD      E,C                 
713F: 22              LD      (HLI),A             
7140: 61              LD      H,C                 
7141: 27              DAA                         
7142: 86              ADD     A,(HL)              
7143: 62              LD      H,D                 
7144: 22              LD      (HLI),A             
7145: 63              LD      H,E                 
7146: C8              RET     Z                   
7147: 66              LD      H,(HL)              
7148: C8              RET     Z                   
7149: 68              LD      L,B                 
714A: 28 27           JR      Z,$7173             ; {}
714C: 1B              DEC     DE                  
714D: 83              ADD     A,E                 
714E: 37              SCF                         
714F: 1B              DEC     DE                  
7150: 84              ADD     A,H                 
7151: 46              LD      B,(HL)              
7152: 1B              DEC     DE                  
7153: 83              ADD     A,E                 
7154: 55              LD      D,L                 
7155: 1B              DEC     DE                  
7156: 32              LD      (HLD),A             
7157: CB E0           SET     1,E                 
7159: 00              NOP                         
715A: AA              XOR     D                   
715B: 88              ADC     A,B                 
715C: 40              LD      B,B                 
715D: FE 0C           CP      $0C                 
715F: 90              SUB     B                   
7160: 88              ADC     A,B                 
7161: 20 1B           JR      NZ,$717E            ; {}
7163: 88              ADC     A,B                 
7164: 30 1B           JR      NC,$7181            ; {}
7166: 88              ADC     A,B                 
7167: 40              LD      B,B                 
7168: 1B              DEC     DE                  
7169: 88              ADC     A,B                 
716A: 50              LD      D,B                 
716B: 1B              DEC     DE                  
716C: 83              ADD     A,E                 
716D: 41              LD      B,C                 
716E: 0E 83           LD      C,$83               
7170: 52              LD      D,D                 
7171: 0E 83           LD      C,$83               
7173: 36 05           LD      (HL),$05            
7175: 83              ADD     A,E                 
7176: 46              LD      B,(HL)              
7177: 05              DEC     B                   
7178: 57              LD      D,A                 
7179: 05              DEC     B                   
717A: C2 25 4E        JP      NZ,$4E25            ; {}
717D: 46              LD      B,(HL)              
717E: 4E              LD      C,(HL)              
717F: 57              LD      D,A                 
7180: 4E              LD      C,(HL)              
7181: 11 25 86        LD      DE,$8625            
7184: 12              LD      (DE),A              
7185: 21 13 C7        LD      HL,$C713            
7188: 16 C7           LD      D,$C7               
718A: 18 26           JR      $71B2               ; {}
718C: 20 21           JR      NZ,$71AF            ; {}
718E: 21 29 28        LD      HL,$2829            
7191: 2A              LD      A,(HLI)             
7192: 29              ADD     HL,HL               
7193: 26 C2           LD      H,$C2               
7195: 39              ADD     HL,SP               
7196: 24              INC     H                   
7197: 50              LD      D,B                 
7198: 22              LD      (HLI),A             
7199: 51              LD      D,C                 
719A: 2B              DEC     HL                  
719B: 58              LD      E,B                 
719C: 2C              INC     L                   
719D: 59              LD      E,C                 
719E: 28 61           JR      Z,$7201             ; {}
71A0: 27              DAA                         
71A1: 86              ADD     A,(HL)              
71A2: 62              LD      H,D                 
71A3: 22              LD      (HLI),A             
71A4: 63              LD      H,E                 
71A5: C8              RET     Z                   
71A6: 66              LD      H,(HL)              
71A7: C8              RET     Z                   
71A8: 68              LD      L,B                 
71A9: 28 37           JR      Z,$71E2             ; {}
71AB: CB E0           SET     1,E                 
71AD: 00              NOP                         
71AE: AB              XOR     E                   
71AF: 78              LD      A,B                 
71B0: 50              LD      D,B                 
71B1: FE 04           CP      $04                 
71B3: 9D              SBC     L                   
71B4: C4 00 23        CALL    NZ,$2300            
71B7: 40              LD      B,B                 
71B8: 27              DAA                         
71B9: 89              ADC     A,C                 
71BA: 41              LD      B,C                 
71BB: 22              LD      (HLI),A             
71BC: 8A              ADC     A,D                 
71BD: 50              LD      D,B                 
71BE: 03              INC     BC                  
71BF: 8A              ADC     A,D                 
71C0: 60              LD      H,B                 
71C1: 03              INC     BC                  
71C2: 8A              ADC     A,D                 
71C3: 70              LD      (HL),B              
71C4: 03              INC     BC                  
71C5: 03              INC     BC                  
71C6: C0              RET     NZ                  
71C7: 06 C0           LD      B,$C0               
71C9: 09              ADD     HL,BC               
71CA: 2A              LD      A,(HLI)             
71CB: FE 04           CP      $04                 
71CD: 4D              LD      C,L                 
71CE: 13              INC     DE                  
71CF: C0              RET     NZ                  
71D0: 16 C0           LD      D,$C0               
71D2: 40              LD      B,B                 
71D3: 22              LD      (HLI),A             
71D4: 41              LD      B,C                 
71D5: 2B              DEC     HL                  
71D6: C2 51 23        JP      NZ,$2351            
71D9: 71              LD      (HL),C              
71DA: 27              DAA                         
71DB: 48              LD      C,B                 
71DC: 2C              INC     L                   
71DD: 49              LD      C,C                 
71DE: 28 C2           JR      Z,$71A2             ; {}
71E0: 58              LD      E,B                 
71E1: 24              INC     H                   
71E2: 78              LD      A,B                 
71E3: 28 C3           JR      Z,$71A8             ; {}
71E5: 50              LD      D,B                 
71E6: 03              INC     BC                  
71E7: C3 59 03        JP      $0359               
71EA: C3 42 AC        JP      $AC42               
71ED: C3 47 AC        JP      $AC47               
71F0: 53              LD      D,E                 
71F1: FC                              
71F2: E0 00           LD      ($FF00+$00),A       
71F4: 69              LD      L,C                 
71F5: 58              LD      E,B                 
71F6: 40              LD      B,B                 
71F7: FE 04           CP      $04                 
71F9: 53              LD      D,E                 
71FA: 04              INC     B                   
71FB: 0D              DEC     C                   
71FC: 82              ADD     A,D                 
71FD: 13              INC     DE                  
71FE: 0D              DEC     C                   
71FF: 02              LD      (BC),A              
7200: 21 C3 00        LD      HL,$00C3            
7203: 03              INC     BC                  
7204: 30 25           JR      NC,$722B            ; {}
7206: 31 29 C2        LD      SP,$C229            
7209: 11 23 01        LD      DE,$0123            
720C: 25              DEC     H                   
720D: 03              INC     BC                  
720E: 29              ADD     HL,HL               
720F: C2 05 24        JP      NZ,$2405            
7212: 23              INC     HL                  
7213: 2C              INC     L                   
7214: 24              INC     H                   
7215: 22              LD      (HLI),A             
7216: 25              DEC     H                   
7217: 28 33           JR      Z,$724C             ; {}
7219: 24              INC     H                   
721A: 43              LD      B,E                 
721B: 2A              LD      A,(HLI)             
721C: 44              LD      B,H                 
721D: 26 C2           LD      H,$C2               
721F: 54              LD      D,H                 
7220: 24              INC     H                   
7221: 74              LD      (HL),H              
7222: 28 C4           JR      Z,$71E8             ; {}
7224: 12              LD      (DE),A              
7225: 0D              DEC     C                   
7226: 83              ADD     A,E                 
7227: 51              LD      D,C                 
7228: 0D              DEC     C                   
7229: 83              ADD     A,E                 
722A: 61              LD      H,C                 
722B: 0D              DEC     C                   
722C: 41              LD      B,C                 
722D: AB              XOR     E                   
722E: 85              ADD     A,L                 
722F: 75              LD      (HL),L              
7230: 03              INC     BC                  
7231: 04              INC     B                   
7232: 07              RLCA                        
7233: 82              ADD     A,D                 
7234: 13              INC     DE                  
7235: 07              RLCA                        
7236: C4 12 07        CALL    NZ,$0712            
7239: 83              ADD     A,E                 
723A: 51              LD      D,C                 
723B: 07              RLCA                        
723C: 83              ADD     A,E                 
723D: 61              LD      H,C                 
723E: 07              RLCA                        
723F: 63              LD      H,E                 
7240: CB E1           SET     1,E                 
7242: 14              INC     D                   
7243: C3 28 10        JP      $1028               
7246: FE 04           CP      $04                 
7248: 0D              DEC     C                   
7249: 00              NOP                         
724A: 17              RLA                         
724B: 89              ADC     A,C                 
724C: 01 12 10        LD      BC,$1012            
724F: 15              DEC     D                   
7250: 89              ADC     A,C                 
7251: 11 13 82        LD      DE,$8213            
7254: 14              INC     D                   
7255: 0D              DEC     C                   
7256: 20 25           JR      NZ,$727D            ; {}
7258: 88              ADC     A,B                 
7259: 21 21 29        LD      HL,$2921            
725C: 26 31           LD      H,$31               
725E: C0              RET     NZ                  
725F: 38 C0           JR      C,$7221             ; {}
7261: 82              ADD     A,D                 
7262: 34              INC     (HL)                
7263: 0F              RRCA                        
7264: 82              ADD     A,D                 
7265: 44              LD      B,H                 
7266: 0F              RRCA                        
7267: 62              LD      H,D                 
7268: AC              XOR     H                   
7269: 67              LD      H,A                 
726A: AC              XOR     H                   
726B: 82              ADD     A,D                 
726C: 24              INC     H                   
726D: 97              SUB     A                   
726E: 53              LD      D,E                 
726F: FC                              
7270: E0 00           LD      ($FF00+$00),A       
7272: 59              LD      E,C                 
7273: 18 30           JR      $72A5               ; {}
7275: FE 04           CP      $04                 
7277: 0D              DEC     C                   
7278: 04              INC     B                   
7279: F0 00           LD      A,($00)             
727B: 93              SUB     E                   
727C: 01 10 10        LD      BC,$1010            
727F: 13              INC     DE                  
7280: 11 14 02        LD      DE,$0214            
7283: 25              DEC     H                   
7284: 07              RLCA                        
7285: 26 82           LD      H,$82               
7287: 08 03 82        LD      ($8203),SP          
728A: 18 03           JR      $728F               ; {}
728C: 20 25           JR      NZ,$72B3            ; {}
728E: 21 21 22        LD      HL,$2221            
7291: 29              ADD     HL,HL               
7292: 12              LD      (DE),A              
7293: 23              INC     HL                  
7294: 17              RLA                         
7295: 24              INC     H                   
7296: 27              DAA                         
7297: 2A              LD      A,(HLI)             
7298: 28 21           JR      Z,$72BB             ; {}
729A: 29              ADD     HL,HL               
729B: 26 84           LD      H,$84               
729D: 13              INC     DE                  
729E: 0F              RRCA                        
729F: C4 14 0F        CALL    NZ,$0F14            
72A2: C4 15 0F        CALL    NZ,$0F15            
72A5: 23              INC     HL                  
72A6: 20 26           JR      NZ,$72CE            ; {}
72A8: 20 82           JR      NZ,$722C            ; {}
72AA: 31 20 82        LD      SP,$8220            
72AD: 37              SCF                         
72AE: 20 41           JR      NZ,$72F1            ; {}
72B0: 20 48           JR      NZ,$72FA            ; {}
72B2: 20 62           JR      NZ,$7316            ; {}
72B4: AC              XOR     H                   
72B5: 67              LD      H,A                 
72B6: AC              XOR     H                   
72B7: 53              LD      D,E                 
72B8: FC                              
72B9: E0 00           LD      ($FF00+$00),A       
72BB: 59              LD      E,C                 
72BC: 58              LD      E,B                 
72BD: 40              LD      B,B                 
72BE: FE 04           CP      $04                 
72C0: 0D              DEC     C                   
72C1: 82              ADD     A,D                 
72C2: 05              DEC     B                   
72C3: 99              SBC     C                   
72C4: 83              ADD     A,E                 
72C5: 11 20 82        LD      DE,$8220            
72C8: 15              DEC     D                   
72C9: 9A              SBC     D                   
72CA: 82              ADD     A,D                 
72CB: 17              RLA                         
72CC: C5              PUSH    BC                  
72CD: 82              ADD     A,D                 
72CE: 27              DAA                         
72CF: C6 82           ADD     $82                 
72D1: 31 C0 41        LD      SP,$41C0            
72D4: 9B              SBC     E                   
72D5: 42              LD      B,D                 
72D6: 9C              SBC     H                   
72D7: 45              LD      B,L                 
72D8: 9B              SBC     E                   
72D9: 46              LD      B,(HL)              
72DA: 9C              SBC     H                   
72DB: 47              LD      B,A                 
72DC: 9B              SBC     E                   
72DD: 48              LD      C,B                 
72DE: 9C              SBC     H                   
72DF: 82              ADD     A,D                 
72E0: 51              LD      D,C                 
72E1: C0              RET     NZ                  
72E2: 84              ADD     A,H                 
72E3: 55              LD      D,L                 
72E4: C0              RET     NZ                  
72E5: 84              ADD     A,H                 
72E6: 63              LD      H,E                 
72E7: 0F              RRCA                        
72E8: 74              LD      (HL),H              
72E9: FD                              
72EA: E0 00           LD      ($FF00+$00),A       
72EC: DD                              
72ED: 58              LD      E,B                 
72EE: 42              LD      B,D                 
72EF: FE 04           CP      $04                 
72F1: 90              SUB     B                   
72F2: C2 01 23        JP      NZ,$2301            
72F5: 21 27 83        LD      HL,$8327            
72F8: 22              LD      (HLI),A             
72F9: 22              LD      (HLI),A             
72FA: 25              DEC     H                   
72FB: 2B              DEC     HL                  
72FC: 35              DEC     (HL)                
72FD: 27              DAA                         
72FE: 36 2B           LD      (HL),$2B            
7300: 46              LD      B,(HL)              
7301: 23              INC     HL                  
7302: 55              LD      D,L                 
7303: 25              DEC     H                   
7304: 56              LD      D,(HL)              
7305: 29              ADD     HL,HL               
7306: 65              LD      H,L                 
7307: 23              INC     HL                  
7308: 75              LD      (HL),L              
7309: 27              DAA                         
730A: 83              ADD     A,E                 
730B: 76              HALT                        
730C: 22              LD      (HLI),A             
730D: 79              LD      A,C                 
730E: 28 85           JR      Z,$7295             ; {}
7310: 02              LD      (BC),A              
7311: 0D              DEC     C                   
7312: 03              INC     BC                  
7313: 2A              LD      A,(HLI)             
7314: 04              INC     B                   
7315: 21 05 29        LD      HL,$2905            
7318: 07              RLCA                        
7319: 24              INC     H                   
731A: 17              RLA                         
731B: 2A              LD      A,(HLI)             
731C: 18 26           JR      $7344               ; {}
731E: C2 28 24        JP      NZ,$2428            
7321: 48              LD      C,B                 
7322: 2A              LD      A,(HLI)             
7323: 49              LD      C,C                 
7324: 26 C2           LD      H,$C2               
7326: 59              LD      E,C                 
7327: 24              INC     H                   
7328: 85              ADD     A,L                 
7329: 12              LD      (DE),A              
732A: 0D              DEC     C                   
732B: 26 0D           LD      H,$0D               
732D: C4 27 0D        CALL    NZ,$0D27            
7330: 58              LD      E,B                 
7331: 0D              DEC     C                   
7332: 82              ADD     A,D                 
7333: 66              LD      H,(HL)              
7334: 0D              DEC     C                   
7335: 13              INC     DE                  
7336: 0F              RRCA                        
7337: 68              LD      L,B                 
7338: CB E1           SET     1,E                 
733A: 10 C7           ;;STOP    $C7                 
733C: 68              LD      L,B                 
733D: 32              LD      (HLD),A             
733E: FE 0C           CP      $0C                 
7340: 0D              DEC     C                   
7341: 02              LD      (BC),A              
7342: C7              RST     0X00                
7343: 07              RLCA                        
7344: C7              RST     0X00                
7345: 83              ADD     A,E                 
7346: 11 1B 83        LD      DE,$831B            
7349: 21 1B 31        LD      HL,$311B            
734C: 12              LD      (DE),A              
734D: 33              INC     SP                  
734E: 12              LD      (DE),A              
734F: 34              INC     (HL)                
7350: 93              SUB     E                   
7351: C2 14 11        JP      NZ,$1114            
7354: C3 17 0F        JP      $0F17               
7357: C3 18 0F        JP      $0F18               
735A: 18 C5           JR      $7321               ; {}
735C: 28 C6           JR      Z,$7324             ; {}
735E: C3 41 20        JP      $2041               
7361: C3 42 20        JP      $2042               
7364: 56              LD      D,(HL)              
7365: 9B              SBC     E                   
7366: 57              LD      D,A                 
7367: 9C              SBC     H                   
7368: 58              LD      E,B                 
7369: CE 74           ADC     $74                 
736B: FD                              
736C: E0 00           LD      ($FF00+$00),A       
736E: CD 28 50        CALL    $5028               ; {}
7371: FE 0C           CP      $0C                 
7373: 0D              DEC     C                   
7374: 02              LD      (BC),A              
7375: C7              RST     0X00                
7376: 07              RLCA                        
7377: C7              RST     0X00                
7378: C4 11 0F        CALL    NZ,$0F11            
737B: C4 12 0F        CALL    NZ,$0F12            
737E: C2 15 10        JP      NZ,$1015            
7381: 83              ADD     A,E                 
7382: 16 1B           LD      D,$1B               
7384: 83              ADD     A,E                 
7385: 26 1B           LD      H,$1B               
7387: 82              ADD     A,D                 
7388: 26 1B           LD      H,$1B               
738A: 36 12           LD      (HL),$12            
738C: 38 12           JR      C,$73A0             ; {}
738E: 35              DEC     (HL)                
738F: 94              SUB     H                   
7390: 21 C5 31        LD      HL,$31C5            
7393: C6 C3           ADD     $C3                 
7395: 47              LD      B,A                 
7396: 20 C3           JR      NZ,$735B            ; {}
7398: 48              LD      C,B                 
7399: 20 83           JR      NZ,$731E            ; {}
739B: 51              LD      D,C                 
739C: C0              RET     NZ                  
739D: 52              LD      D,D                 
739E: CE 74           ADC     $74                 
73A0: FD                              
73A1: E0 00           LD      ($FF00+$00),A       
73A3: CD 58 50        CALL    $5058               ; {}
73A6: FE 0C           CP      $0C                 
73A8: 2D              DEC     L                   
73A9: 03              INC     BC                  
73AA: C7              RST     0X00                
73AB: 06 C7           LD      B,$C7               
73AD: C2 11 10        JP      NZ,$1011            
73B0: C2 18 11        JP      NZ,$1118            
73B3: 82              ADD     A,D                 
73B4: 32              LD      (HLD),A             
73B5: 12              LD      (DE),A              
73B6: 82              ADD     A,D                 
73B7: 36 12           LD      (HL),$12            
73B9: 31 94 38        LD      SP,$3894            
73BC: 93              SUB     E                   
73BD: 86              ADD     A,(HL)              
73BE: 12              LD      (DE),A              
73BF: 1B              DEC     DE                  
73C0: 86              ADD     A,(HL)              
73C1: 22              LD      (HLI),A             
73C2: 1B              DEC     DE                  
73C3: 83              ADD     A,E                 
73C4: 41              LD      B,C                 
73C5: 20 83           JR      NZ,$734A            ; {}
73C7: 51              LD      D,C                 
73C8: 20 83           JR      NZ,$734D            ; {}
73CA: 61              LD      H,C                 
73CB: 20 83           JR      NZ,$7350            ; {}
73CD: 56              LD      D,(HL)              
73CE: C0              RET     NZ                  
73CF: 57              LD      D,A                 
73D0: CE 74           ADC     $74                 
73D2: FD                              
73D3: E0 00           LD      ($FF00+$00),A       
73D5: CC 28 50        CALL    Z,$5028             ; {}
73D8: FE 0C           CP      $0C                 
73DA: 4D              LD      C,L                 
73DB: 06 26           LD      B,$26               
73DD: C6 16           ADD     $16                 
73DF: 24              INC     H                   
73E0: 76              HALT                        
73E1: 28 C8           JR      Z,$73AB             ; {}
73E3: 07              RLCA                        
73E4: 03              INC     BC                  
73E5: C8              RET     Z                   
73E6: 08 03 C8        LD      ($C803),SP          
73E9: 09              ADD     HL,BC               
73EA: 03              INC     BC                  
73EB: 84              ADD     A,H                 
73EC: 12              LD      (DE),A              
73ED: C5              PUSH    BC                  
73EE: 84              ADD     A,H                 
73EF: 22              LD      (HLI),A             
73F0: C6 82           ADD     $82                 
73F2: 43              LD      B,E                 
73F3: C0              RET     NZ                  
73F4: 84              ADD     A,H                 
73F5: 52              LD      D,D                 
73F6: C0              RET     NZ                  
73F7: 82              ADD     A,D                 
73F8: 63              LD      H,E                 
73F9: C0              RET     NZ                  
73FA: 53              LD      D,E                 
73FB: 9B              SBC     E                   
73FC: 54              LD      D,H                 
73FD: 9C              SBC     H                   
73FE: FE 0C           CP      $0C                 
7400: 0D              DEC     C                   
7401: 83              ADD     A,E                 
7402: 04              INC     B                   
7403: 99              SBC     C                   
7404: 83              ADD     A,E                 
7405: 14              INC     D                   
7406: 9A              SBC     D                   
7407: 82              ADD     A,D                 
7408: 17              RLA                         
7409: C0              RET     NZ                  
740A: 27              DAA                         
740B: 20 28           JR      NZ,$7435            ; {}
740D: A6              AND     (HL)                
740E: 38 C0           JR      C,$73D0             ; {}
7410: 83              ADD     A,E                 
7411: 41              LD      B,C                 
7412: 0F              RRCA                        
7413: 47              LD      B,A                 
7414: 9B              SBC     E                   
7415: 48              LD      C,B                 
7416: 9C              SBC     H                   
7417: 83              ADD     A,E                 
7418: 51              LD      D,C                 
7419: 0F              RRCA                        
741A: 51              LD      D,C                 
741B: C5              PUSH    BC                  
741C: 52              LD      D,D                 
741D: CE 58           ADC     $58                 
741F: 20 83           JR      NZ,$73A4            ; {}
7421: 61              LD      H,C                 
7422: 0F              RRCA                        
7423: 61              LD      H,C                 
7424: C6 66           ADD     $66                 
7426: A6              AND     (HL)                
7427: 82              ADD     A,D                 
7428: 67              LD      H,A                 
7429: 20 74           JR      NZ,$749F            ; {}
742B: FD                              
742C: E0 00           LD      ($FF00+$00),A       
742E: CC 78 50        CALL    Z,$5078             ; {}
7431: FE 04           CP      $04                 
7433: 25              DEC     H                   
7434: 00              NOP                         
7435: 00              NOP                         
7436: 01 25 06        LD      BC,$0625            
7439: 26 83           LD      H,$83               
743B: 07              RLCA                        
743C: 00              NOP                         
743D: 10 25           ;;STOP    $25                 
743F: 11 29 12        LD      DE,$1229            
7442: AF              XOR     A                   
7443: 83              ADD     A,E                 
7444: 13              INC     DE                  
7445: AE              XOR     (HL)                
7446: 16 2A           LD      D,$2A               
7448: 83              ADD     A,E                 
7449: 17              RLA                         
744A: 21 21 AF        LD      HL,$AF21            
744D: 22              LD      (HLI),A             
744E: B0              OR      B                   
744F: 84              ADD     A,H                 
7450: 26 AE           LD      H,$AE               
7452: C2 31 01        JP      NZ,$0131            
7455: 44              LD      B,H                 
7456: AE              XOR     (HL)                
7457: 47              LD      B,A                 
7458: AE              XOR     (HL)                
7459: 51              LD      D,C                 
745A: B0              OR      B                   
745B: 52              LD      D,D                 
745C: AF              XOR     A                   
745D: 55              LD      D,L                 
745E: AE              XOR     (HL)                
745F: 60              LD      H,B                 
7460: 27              DAA                         
7461: 61              LD      H,C                 
7462: 2B              DEC     HL                  
7463: 62              LD      H,D                 
7464: B0              OR      B                   
7465: 87              ADD     A,A                 
7466: 63              LD      H,E                 
7467: AE              XOR     (HL)                
7468: 70              LD      (HL),B              
7469: 0D              DEC     C                   
746A: 71              LD      (HL),C              
746B: 27              DAA                         
746C: 33              INC     SP                  
746D: CB E0           SET     1,E                 
746F: 00              NOP                         
7470: 75              LD      (HL),L              
7471: 38 40           JR      C,$74B3             ; {}
7473: FE 04           CP      $04                 
7475: 45              LD      B,L                 
7476: 00              NOP                         
7477: 00              NOP                         
7478: 01 0D 02        LD      BC,$020D            
747B: 25              DEC     H                   
747C: 08 26 09        LD      ($0926),SP          
747F: 00              NOP                         
7480: 82              ADD     A,D                 
7481: 10 21           ;;STOP    $21                 
7483: 12              LD      (DE),A              
7484: 29              ADD     HL,HL               
7485: 82              ADD     A,D                 
7486: 13              INC     DE                  
7487: AE              XOR     (HL)                
7488: C2 15 A7        JP      NZ,$A715            
748B: 18 2A           JR      $74B7               ; {}
748D: 19              ADD     HL,DE               
748E: 26 82           LD      H,$82               
7490: 20 AE           JR      NZ,$7440            ; {}
7492: 22              LD      (HLI),A             
7493: AF              XOR     A                   
7494: 28 01           JR      Z,$7497             ; {}
7496: C3 32 01        JP      $0132               
7499: 83              ADD     A,E                 
749A: 34              INC     (HL)                
749B: AF              XOR     A                   
749C: 37              SCF                         
749D: AE              XOR     (HL)                
749E: 38 B0           JR      C,$7450             ; {}
74A0: 43              LD      B,E                 
74A1: A9              XOR     C                   
74A2: 83              ADD     A,E                 
74A3: 44              LD      B,H                 
74A4: 01 48 A7        LD      BC,$A748            
74A7: 51              LD      D,C                 
74A8: AF              XOR     A                   
74A9: 53              LD      D,E                 
74AA: AF              XOR     A                   
74AB: 54              LD      D,H                 
74AC: 01 82 55        LD      BC,$5582            
74AF: B0              OR      B                   
74B0: 57              LD      D,A                 
74B1: AE              XOR     (HL)                
74B2: 58              LD      E,B                 
74B3: 2C              INC     L                   
74B4: 59              LD      E,C                 
74B5: 28 60           JR      Z,$7517             ; {}
74B7: AE              XOR     (HL)                
74B8: 84              ADD     A,H                 
74B9: 61              LD      H,C                 
74BA: B0              OR      B                   
74BB: 65              LD      H,L                 
74BC: 2C              INC     L                   
74BD: 82              ADD     A,D                 
74BE: 66              LD      H,(HL)              
74BF: 22              LD      (HLI),A             
74C0: 68              LD      L,B                 
74C1: 28 69           JR      Z,$752C             ; {}
74C3: 0D              DEC     C                   
74C4: 75              LD      (HL),L              
74C5: 28 84           JR      Z,$744B             ; {}
74C7: 76              HALT                        
74C8: 00              NOP                         
74C9: 82              ADD     A,D                 
74CA: 78              LD      A,B                 
74CB: 0D              DEC     C                   
74CC: 23              INC     HL                  
74CD: CB E0           SET     1,E                 
74CF: 00              NOP                         
74D0: 76              HALT                        
74D1: 68              LD      L,B                 
74D2: 50              LD      D,B                 
74D3: FE 04           CP      $04                 
74D5: 0D              DEC     C                   
74D6: 39              ADD     HL,SP               
74D7: F3              DI                          
74D8: 71              LD      (HL),C              
74D9: F1              POP     AF                  
74DA: 00              NOP                         
74DB: 00              NOP                         
74DC: 01 25 10        LD      BC,$1025            
74DF: 25              DEC     H                   
74E0: 11 29 03        LD      DE,$0329            
74E3: C7              RST     0X00                
74E4: 06 C7           LD      B,$C7               
74E6: 08 26 09        LD      ($0926),SP          
74E9: 00              NOP                         
74EA: 18 2A           JR      $7516               ; {}
74EC: 19              ADD     HL,DE               
74ED: 26 12           LD      H,$12               
74EF: DF              RST     0X18                
74F0: C2 31 DF        JP      NZ,$DF31            
74F3: FE 04           CP      $04                 
74F5: 0D              DEC     C                   
74F6: 30 F2           JR      NC,$74EA            ; {}
74F8: 39              ADD     HL,SP               
74F9: F3              DI                          
74FA: 03              INC     BC                  
74FB: C7              RST     0X00                
74FC: 06 C7           LD      B,$C7               
74FE: 73              LD      (HL),E              
74FF: C8              RET     Z                   
7500: 76              HALT                        
7501: C8              RET     Z                   
7502: 00              NOP                         
7503: 00              NOP                         
7504: 09              ADD     HL,BC               
7505: 00              NOP                         
7506: 70              LD      (HL),B              
7507: 00              NOP                         
7508: 79              LD      A,C                 
7509: 00              NOP                         
750A: 10 25           ;;STOP    $25                 
750C: 11 29 01        LD      DE,$0129            
750F: 25              DEC     H                   
7510: 08 26 18        LD      ($1826),SP          
7513: 2A              LD      A,(HLI)             
7514: 19              ADD     HL,DE               
7515: 26 60           LD      H,$60               
7517: 27              DAA                         
7518: 61              LD      H,C                 
7519: 2B              DEC     HL                  
751A: 71              LD      (HL),C              
751B: 27              DAA                         
751C: 68              LD      L,B                 
751D: 2C              INC     L                   
751E: 69              LD      L,C                 
751F: 28 78           JR      Z,$7599             ; {}
7521: 28 FE           JR      Z,$7521             ; {}
7523: 04              INC     B                   
7524: 9D              SBC     L                   
7525: 30 F6           JR      NC,$751D            ; {}
7527: 85              ADD     A,L                 
7528: 00              NOP                         
7529: 00              NOP                         
752A: 05              DEC     B                   
752B: 25              DEC     H                   
752C: 82              ADD     A,D                 
752D: 06 21           LD      B,$21               
752F: 08 26 09        LD      ($0926),SP          
7532: 00              NOP                         
7533: 84              ADD     A,H                 
7534: 10 00           ;;STOP    $00                 
7536: 14              INC     D                   
7537: 25              DEC     H                   
7538: 15              DEC     D                   
7539: 29              ADD     HL,HL               
753A: 18 2A           JR      $7566               ; {}
753C: 19              ADD     HL,DE               
753D: 26 20           LD      H,$20               
753F: 25              DEC     H                   
7540: 83              ADD     A,E                 
7541: 21 21 22        LD      HL,$2221            
7544: C7              RST     0X00                
7545: 24              INC     H                   
7546: 29              ADD     HL,HL               
7547: C4 29 24        CALL    NZ,$2429            
754A: 38 A6           JR      C,$74F2             ; {}
754C: 50              LD      D,B                 
754D: 27              DAA                         
754E: 83              ADD     A,E                 
754F: 51              LD      D,C                 
7550: 22              LD      (HLI),A             
7551: 52              LD      D,D                 
7552: C8              RET     Z                   
7553: 54              LD      D,H                 
7554: 2B              DEC     HL                  
7555: 84              ADD     A,H                 
7556: 60              LD      H,B                 
7557: 00              NOP                         
7558: 64              LD      H,H                 
7559: 27              DAA                         
755A: 65              LD      H,L                 
755B: 2B              DEC     HL                  
755C: 68              LD      L,B                 
755D: 2C              INC     L                   
755E: 69              LD      L,C                 
755F: 28 85           JR      Z,$74E6             ; {}
7561: 70              LD      (HL),B              
7562: 00              NOP                         
7563: 75              LD      (HL),L              
7564: 27              DAA                         
7565: 82              ADD     A,D                 
7566: 76              HALT                        
7567: 22              LD      (HLI),A             
7568: 78              LD      A,B                 
7569: 28 79           JR      Z,$75E4             ; {}
756B: 00              NOP                         
756C: FE 04           CP      $04                 
756E: 91              SUB     C                   
756F: 84              ADD     A,H                 
7570: 43              LD      B,E                 
7571: 0D              DEC     C                   
7572: 84              ADD     A,H                 
7573: 53              LD      D,E                 
7574: 0D              DEC     C                   
7575: 84              ADD     A,H                 
7576: 63              LD      H,E                 
7577: 0D              DEC     C                   
7578: 32              LD      (HLD),A             
7579: 25              DEC     H                   
757A: 84              ADD     A,H                 
757B: 33              INC     SP                  
757C: 21 37 26        LD      HL,$2637            
757F: C3 42 23        JP      $2342               
7582: 72              LD      (HL),D              
7583: 27              DAA                         
7584: 84              ADD     A,H                 
7585: 73              LD      (HL),E              
7586: 22              LD      (HLI),A             
7587: C4 47 24        CALL    NZ,$2447            
758A: 34              INC     (HL)                
758B: 99              SBC     C                   
758C: 44              LD      B,H                 
758D: 9A              SBC     D                   
758E: 55              LD      D,L                 
758F: C0              RET     NZ                  
7590: 77              LD      (HL),A              
7591: 28 74           JR      Z,$7607             ; {}
7593: FD                              
7594: E0 00           LD      ($FF00+$00),A       
7596: DB                              
7597: 78              LD      A,B                 
7598: 52              LD      D,D                 
7599: FE 0C           CP      $0C                 
759B: 35              DEC     (HL)                
759C: C5              PUSH    BC                  
759D: 00              NOP                         
759E: 00              NOP                         
759F: 01 00 C2        LD      BC,$C200            
75A2: 11 0D 02        LD      DE,$020D            
75A5: 25              DEC     H                   
75A6: 07              RLCA                        
75A7: 26 08           LD      H,$08               
75A9: 0D              DEC     C                   
75AA: C2 18 00        JP      NZ,$0018            
75AD: C5              PUSH    BC                  
75AE: 09              ADD     HL,BC               
75AF: 00              NOP                         
75B0: 29              ADD     HL,HL               
75B1: 0D              DEC     C                   
75B2: C2 12 23        JP      NZ,$2312            
75B5: C2 17 24        JP      NZ,$2417            
75B8: 31 25 32        LD      SP,$3225            
75BB: 29              ADD     HL,HL               
75BC: 37              SCF                         
75BD: 2A              LD      A,(HLI)             
75BE: 38 26           JR      C,$75E6             ; {}
75C0: 41              LD      B,C                 
75C1: 23              INC     HL                  
75C2: 48              LD      C,B                 
75C3: 24              INC     H                   
75C4: 50              LD      D,B                 
75C5: 25              DEC     H                   
75C6: 51              LD      D,C                 
75C7: 29              ADD     HL,HL               
75C8: 58              LD      E,B                 
75C9: 2A              LD      A,(HLI)             
75CA: 59              LD      E,C                 
75CB: 26 C2           LD      H,$C2               
75CD: 60              LD      H,B                 
75CE: 23              INC     HL                  
75CF: C2 69 24        JP      NZ,$2469            
75D2: 69              LD      L,C                 
75D3: 4A              LD      C,D                 
75D4: C7              RST     0X00                
75D5: 15              DEC     D                   
75D6: A6              AND     (HL)                
75D7: C3 53 A6        JP      $A653               
75DA: 02              LD      (BC),A              
75DB: 25              DEC     H                   
75DC: 07              RLCA                        
75DD: 26 FE           LD      H,$FE               
75DF: 0C              INC     C                   
75E0: 90              SUB     B                   
75E1: 00              NOP                         
75E2: 0D              DEC     C                   
75E3: 82              ADD     A,D                 
75E4: 02              LD      (BC),A              
75E5: 0D              DEC     C                   
75E6: 07              RLCA                        
75E7: 0D              DEC     C                   
75E8: 11 0D 18        LD      DE,$180D            
75EB: 0D              DEC     C                   
75EC: 30 0D           JR      NC,$75FB            ; {}
75EE: 41              LD      B,C                 
75EF: 0D              DEC     C                   
75F0: C2 49 0D        JP      NZ,$0D49            
75F3: 78              LD      A,B                 
75F4: 0D              DEC     C                   
75F5: 13              INC     DE                  
75F6: 25              DEC     H                   
75F7: 83              ADD     A,E                 
75F8: 14              INC     D                   
75F9: 21 17 26        LD      HL,$2617            
75FC: 22              LD      (HLI),A             
75FD: 25              DEC     H                   
75FE: 23              INC     HL                  
75FF: 29              ADD     HL,HL               
7600: 83              ADD     A,E                 
7601: 24              INC     H                   
7602: 1B              DEC     DE                  
7603: 27              DAA                         
7604: 2A              LD      A,(HLI)             
7605: 28 26           JR      Z,$762D             ; {}
7607: C2 32 23        JP      NZ,$2332            
760A: 85              ADD     A,L                 
760B: 33              INC     SP                  
760C: 1B              DEC     DE                  
760D: 35              DEC     (HL)                
760E: 05              DEC     B                   
760F: C3 38 24        JP      $2438               
7612: 85              ADD     A,L                 
7613: 43              LD      B,E                 
7614: 1B              DEC     DE                  
7615: 83              ADD     A,E                 
7616: 44              LD      B,H                 
7617: 05              DEC     B                   
7618: 50              LD      D,B                 
7619: 25              DEC     H                   
761A: 51              LD      D,C                 
761B: 21 52 29        LD      HL,$2952            
761E: 85              ADD     A,L                 
761F: 53              LD      D,E                 
7620: 1B              DEC     DE                  
7621: 55              LD      D,L                 
7622: 05              DEC     B                   
7623: 60              LD      H,B                 
7624: 3E 83           LD      A,$83               
7626: 61              LD      H,C                 
7627: 05              DEC     B                   
7628: 83              ADD     A,E                 
7629: 64              LD      H,H                 
762A: 1B              DEC     DE                  
762B: 67              LD      H,A                 
762C: 2C              INC     L                   
762D: 68              LD      L,B                 
762E: 28 70           JR      Z,$76A0             ; {}
7630: 27              DAA                         
7631: 86              ADD     A,(HL)              
7632: 71              LD      (HL),C              
7633: 22              LD      (HLI),A             
7634: 77              LD      (HL),A              
7635: 28 FE           JR      Z,$7635             ; {}
7637: 0C              INC     C                   
7638: 55              LD      D,L                 
7639: 84              ADD     A,H                 
763A: 00              NOP                         
763B: 21 04 26        LD      HL,$2604            
763E: 85              ADD     A,L                 
763F: 05              DEC     B                   
7640: 00              NOP                         
7641: 00              NOP                         
7642: 25              DEC     H                   
7643: 14              INC     D                   
7644: 2A              LD      A,(HLI)             
7645: 85              ADD     A,L                 
7646: 15              DEC     D                   
7647: 21 22 25        LD      HL,$2522            
764A: 87              ADD     A,A                 
764B: 23              INC     HL                  
764C: 21 30 29        LD      HL,$2930            
764F: 32              LD      (HLD),A             
7650: 23              INC     HL                  
7651: 39              ADD     HL,SP               
7652: 05              DEC     B                   
7653: 40              LD      B,B                 
7654: 25              DEC     H                   
7655: 41              LD      B,C                 
7656: 98              SBC     B                   
7657: 42              LD      B,D                 
7658: 29              ADD     HL,HL               
7659: 82              ADD     A,D                 
765A: 43              LD      B,E                 
765B: 12              LD      (DE),A              
765C: 45              LD      B,L                 
765D: 2C              INC     L                   
765E: 84              ADD     A,H                 
765F: 46              LD      B,(HL)              
7660: 22              LD      (HLI),A             
7661: 55              LD      D,L                 
7662: 2A              LD      A,(HLI)             
7663: 83              ADD     A,E                 
7664: 56              LD      D,(HL)              
7665: 21 59 26        LD      HL,$2659            
7668: 62              LD      H,D                 
7669: A6              AND     (HL)                
766A: 84              ADD     A,H                 
766B: 64              LD      H,H                 
766C: AF              XOR     A                   
766D: 63              LD      H,E                 
766E: A9              XOR     C                   
766F: C2 69 24        JP      NZ,$2469            
7672: 77              LD      (HL),A              
7673: 2B              DEC     HL                  
7674: 78              LD      A,B                 
7675: 05              DEC     B                   
7676: FE 0C           CP      $0C                 
7678: 90              SUB     B                   
7679: 02              LD      (BC),A              
767A: 0D              DEC     C                   
767B: 82              ADD     A,D                 
767C: 05              DEC     B                   
767D: 0D              DEC     C                   
767E: 86              ADD     A,(HL)              
767F: 10 21           ;;STOP    $21                 
7681: 16 26           LD      D,$26               
7683: 17              RLA                         
7684: 0D              DEC     C                   
7685: 85              ADD     A,L                 
7686: 20 21           JR      NZ,$76A9            ; {}
7688: 25              DEC     H                   
7689: 26 26           LD      H,$26               
768B: 2A              LD      A,(HLI)             
768C: 27              DAA                         
768D: 26 30           LD      H,$30               
768F: 05              DEC     B                   
7690: 84              ADD     A,H                 
7691: 31 05 35        LD      SP,$3505            
7694: 2A              LD      A,(HLI)             
7695: 36 26           LD      (HL),$26            
7697: C3 37 24        JP      $2437               
769A: 83              ADD     A,E                 
769B: 40              LD      B,B                 
769C: 22              LD      (HLI),A             
769D: 43              LD      B,E                 
769E: 2B              DEC     HL                  
769F: 82              ADD     A,D                 
76A0: 44              LD      B,H                 
76A1: 05              DEC     B                   
76A2: C3 46 24        JP      $2446               
76A5: C2 49 0D        JP      NZ,$0D49            
76A8: 50              LD      D,B                 
76A9: 0D              DEC     C                   
76AA: 53              LD      D,E                 
76AB: 27              DAA                         
76AC: 54              LD      D,H                 
76AD: 2B              DEC     HL                  
76AE: C2 55 05        JP      NZ,$0555            
76B1: C2 61 0D        JP      NZ,$0D61            
76B4: 64              LD      H,H                 
76B5: 23              INC     HL                  
76B6: 67              LD      H,A                 
76B7: 2A              LD      A,(HLI)             
76B8: 68              LD      L,B                 
76B9: 26 74           LD      H,$74               
76BB: 27              DAA                         
76BC: 75              LD      (HL),L              
76BD: 40              LD      B,B                 
76BE: 76              HALT                        
76BF: 28 77           JR      Z,$7738             ; {}
76C1: 0D              DEC     C                   
76C2: 78              LD      A,B                 
76C3: 24              INC     H                   
76C4: FE 00           CP      $00                 
76C6: 90              SUB     B                   
76C7: 8A              ADC     A,D                 
76C8: 00              NOP                         
76C9: 03              INC     BC                  
76CA: 8A              ADC     A,D                 
76CB: 10 03           ;;STOP    $03                 
76CD: 8A              ADC     A,D                 
76CE: 20 03           JR      NZ,$76D3            ; {}
76D0: 8A              ADC     A,D                 
76D1: 30 03           JR      NC,$76D6            ; {}
76D3: 30 76           JR      NC,$774B            ; {}
76D5: 35              DEC     (HL)                
76D6: 75              LD      (HL),L              
76D7: 36 76           LD      (HL),$76            
76D9: 39              ADD     HL,SP               
76DA: 75              LD      (HL),L              
76DB: 41              LD      B,C                 
76DC: 76              HALT                        
76DD: 82              ADD     A,D                 
76DE: 42              LD      B,D                 
76DF: 77              LD      (HL),A              
76E0: 44              LD      B,H                 
76E1: 75              LD      (HL),L              
76E2: 47              LD      B,A                 
76E3: 76              HALT                        
76E4: 48              LD      C,B                 
76E5: 75              LD      (HL),L              
76E6: 52              LD      D,D                 
76E7: 6C              LD      L,H                 
76E8: 84              ADD     A,H                 
76E9: 53              LD      D,E                 
76EA: 68              LD      L,B                 
76EB: 57              LD      D,A                 
76EC: 6D              LD      L,L                 
76ED: 63              LD      H,E                 
76EE: 6E              LD      L,(HL)              
76EF: 64              LD      H,H                 
76F0: 6A              LD      L,D                 
76F1: 66              LD      H,(HL)              
76F2: 6F              LD      L,A                 
76F3: 72              LD      (HL),D              
76F4: E1              POP     HL                  
76F5: 84              ADD     A,H                 
76F6: 73              LD      (HL),E              
76F7: E0 77           LD      ($FF00+$77),A       
76F9: E2              LD      (C),A               
76FA: 55              LD      D,L                 
76FB: 62              LD      H,D                 
76FC: 65              LD      H,L                 
76FD: 65              LD      H,L                 
76FE: 75              LD      (HL),L              
76FF: 62              LD      H,D                 
7700: FE 0D           CP      $0D                 
7702: 90              SUB     B                   
7703: 8A              ADC     A,D                 
7704: 00              NOP                         
7705: 61              LD      H,C                 
7706: 10 61           ;;STOP    $61                 
7708: 20 61           JR      NZ,$776B            ; {}
770A: 8A              ADC     A,D                 
770B: 70              LD      (HL),B              
770C: 61              LD      H,C                 
770D: 17              RLA                         
770E: 5F              LD      E,A                 
770F: C7              RST     0X00                
7710: 18 69           JR      $777B               ; {}
7712: 19              ADD     HL,DE               
7713: 5F              LD      E,A                 
7714: C5              PUSH    BC                  
7715: 27              DAA                         
7716: 61              LD      H,C                 
7717: C5              PUSH    BC                  
7718: 29              ADD     HL,HL               
7719: 61              LD      H,C                 
771A: 37              SCF                         
771B: 5F              LD      E,A                 
771C: 39              ADD     HL,SP               
771D: 5F              LD      E,A                 
771E: 57              LD      D,A                 
771F: 5F              LD      E,A                 
7720: 59              LD      E,C                 
7721: 5F              LD      E,A                 
7722: 41              LD      B,C                 
7723: 77              LD      (HL),A              
7724: 42              LD      B,D                 
7725: 77              LD      (HL),A              
7726: C2 51 76        JP      NZ,$7651            ; {}
7729: C2 52 76        JP      NZ,$7652            ; {}
772C: 86              ADD     A,(HL)              
772D: 11 7F 22        LD      DE,$227F            
7730: 7C              LD      A,H                 
7731: 25              DEC     H                   
7732: 7C              LD      A,H                 
7733: E0 00           LD      ($FF00+$00),A       
7735: 8A              ADC     A,D                 
7736: 58              LD      E,B                 
7737: 40              LD      B,B                 
7738: FE 04           CP      $04                 
773A: 90              SUB     B                   
773B: 82              ADD     A,D                 
773C: 38 05           JR      C,$7743             ; {}
773E: 84              ADD     A,H                 
773F: 46              LD      B,(HL)              
7740: 05              DEC     B                   
7741: 84              ADD     A,H                 
7742: 54              LD      D,H                 
7743: 05              DEC     B                   
7744: 82              ADD     A,D                 
7745: 64              LD      H,H                 
7746: 05              DEC     B                   
7747: 01 DF 83        LD      BC,$83DF            
774A: 03              INC     BC                  
774B: DF              RST     0X18                
774C: 82              ADD     A,D                 
774D: 08 DF 13        LD      ($13DF),SP          
7750: DF              RST     0X18                
7751: 85              ADD     A,L                 
7752: 15              DEC     D                   
7753: DF              RST     0X18                
7754: 24              INC     H                   
7755: DF              RST     0X18                
7756: 26 DF           LD      H,$DF               
7758: 85              ADD     A,L                 
7759: 30 DF           JR      NC,$773A            ; {}
775B: 32              LD      (HLD),A             
775C: 00              NOP                         
775D: 40              LD      B,B                 
775E: DF              RST     0X18                
775F: 50              LD      D,B                 
7760: DF              RST     0X18                
7761: 52              LD      D,D                 
7762: DF              RST     0X18                
7763: 61              LD      H,C                 
7764: DF              RST     0X18                
7765: 70              LD      (HL),B              
7766: DF              RST     0X18                
7767: 27              DAA                         
7768: 25              DEC     H                   
7769: 82              ADD     A,D                 
776A: 28 21           JR      Z,$778D             ; {}
776C: 35              DEC     (HL)                
776D: 25              DEC     H                   
776E: 36 21           LD      (HL),$21            
7770: 37              SCF                         
7771: 29              ADD     HL,HL               
7772: 43              LD      B,E                 
7773: 25              DEC     H                   
7774: 44              LD      B,H                 
7775: 21 45 29        LD      HL,$2945            
7778: C2 53 23        JP      NZ,$2353            
777B: 73              LD      (HL),E              
777C: 27              DAA                         
777D: 58              LD      E,B                 
777E: 2C              INC     L                   
777F: 59              LD      E,C                 
7780: 22              LD      (HLI),A             
7781: 66              LD      H,(HL)              
7782: 2C              INC     L                   
7783: 67              LD      H,A                 
7784: 22              LD      (HLI),A             
7785: 68              LD      L,B                 
7786: 28 76           JR      Z,$77FE             ; {}
7788: 28 69           JR      Z,$77F3             ; {}
778A: DF              RST     0X18                
778B: 83              ADD     A,E                 
778C: 77              LD      (HL),A              
778D: DF              RST     0X18                
778E: 74              LD      (HL),H              
778F: FD                              
7790: E0 00           LD      ($FF00+$00),A       
7792: 15              DEC     D                   
7793: 88              ADC     A,B                 
7794: 40              LD      B,B                 
7795: FE 04           CP      $04                 
7797: 90              SUB     B                   
7798: 8A              ADC     A,D                 
7799: 30 05           JR      NC,$77A0            ; {}
779B: 8A              ADC     A,D                 
779C: 40              LD      B,B                 
779D: 05              DEC     B                   
779E: 00              NOP                         
779F: DF              RST     0X18                
77A0: 01 27 02        LD      BC,$0227            
77A3: 2B              DEC     HL                  
77A4: C6 03           ADD     $03                 
77A6: 01 C8 04        LD      BC,$04C8            
77A9: 01 C8 05        LD      BC,$05C8            
77AC: 01 C6 26        LD      BC,$26C6            
77AF: 01 06 2A        LD      BC,$2A06            
77B2: 07              RLCA                        
77B3: 26 82           LD      H,$82               
77B5: 08 DF 11        LD      ($11DF),SP          
77B8: DF              RST     0X18                
77B9: 12              LD      (DE),A              
77BA: 23              INC     HL                  
77BB: 16 AF           LD      D,$AF               
77BD: 17              RLA                         
77BE: 24              INC     H                   
77BF: 19              ADD     HL,DE               
77C0: DF              RST     0X18                
77C1: 82              ADD     A,D                 
77C2: 20 21           JR      NZ,$77E5            ; {}
77C4: 22              LD      (HLI),A             
77C5: 29              ADD     HL,HL               
77C6: 27              DAA                         
77C7: 2A              LD      A,(HLI)             
77C8: 82              ADD     A,D                 
77C9: 28 21           JR      Z,$77EC             ; {}
77CB: 38 A7           JR      C,$7774             ; {}
77CD: 41              LD      B,C                 
77CE: A7              AND     A                   
77CF: 82              ADD     A,D                 
77D0: 50              LD      D,B                 
77D1: 22              LD      (HLI),A             
77D2: 52              LD      D,D                 
77D3: 2B              DEC     HL                  
77D4: 57              LD      D,A                 
77D5: 2C              INC     L                   
77D6: 82              ADD     A,D                 
77D7: 58              LD      E,B                 
77D8: 22              LD      (HLI),A             
77D9: C2 61 DF        JP      NZ,$DF61            
77DC: 62              LD      H,D                 
77DD: 23              INC     HL                  
77DE: 63              LD      H,E                 
77DF: B0              OR      B                   
77E0: 67              LD      H,A                 
77E1: 2A              LD      A,(HLI)             
77E2: 68              LD      L,B                 
77E3: 26 C2           LD      H,$C2               
77E5: 69              LD      L,C                 
77E6: DF              RST     0X18                
77E7: 72              LD      (HL),D              
77E8: 27              DAA                         
77E9: 73              LD      (HL),E              
77EA: 2B              DEC     HL                  
77EB: 77              LD      (HL),A              
77EC: AF              XOR     A                   
77ED: 78              LD      A,B                 
77EE: 24              INC     H                   
77EF: FE 04           CP      $04                 
77F1: 90              SUB     B                   
77F2: 16 05           LD      D,$05               
77F4: 87              ADD     A,A                 
77F5: 21 05 82        LD      HL,$8205            
77F8: 30 05           JR      NC,$77FF            ; {}
77FA: 36 05           LD      (HL),$05            
77FC: 82              ADD     A,D                 
77FD: 40              LD      B,B                 
77FE: 05              DEC     B                   
77FF: 82              ADD     A,D                 
7800: 00              NOP                         
7801: DF              RST     0X18                
7802: 03              INC     BC                  
7803: DF              RST     0X18                
7804: 05              DEC     B                   
7805: 25              DEC     H                   
7806: 06 21           LD      B,$21               
7808: 07              RLCA                        
7809: 26 82           LD      H,$82               
780B: 08 DF 10        LD      ($10DF),SP          
780E: 25              DEC     H                   
780F: 84              ADD     A,H                 
7810: 11 21 15        LD      DE,$1521            
7813: 29              ADD     HL,HL               
7814: 17              RLA                         
7815: 2A              LD      A,(HLI)             
7816: 18 26           JR      $783E               ; {}
7818: C6 19           ADD     $19                 
781A: DF              RST     0X18                
781B: 20 29           JR      NZ,$7846            ; {}
781D: 28 24           JR      Z,$7843             ; {}
781F: 32              LD      (HLD),A             
7820: 2C              INC     L                   
7821: 82              ADD     A,D                 
7822: 33              INC     SP                  
7823: 22              LD      (HLI),A             
7824: 35              DEC     (HL)                
7825: 2B              DEC     HL                  
7826: 37              SCF                         
7827: 2C              INC     L                   
7828: 38 28           JR      C,$7852             ; {}
782A: 39              ADD     HL,SP               
782B: 00              NOP                         
782C: 42              LD      B,D                 
782D: 24              INC     H                   
782E: 44              LD      B,H                 
782F: DF              RST     0X18                
7830: 45              LD      B,L                 
7831: 27              DAA                         
7832: 46              LD      B,(HL)              
7833: 22              LD      (HLI),A             
7834: 47              LD      B,A                 
7835: 28 82           JR      Z,$77B9             ; {}
7837: 50              LD      D,B                 
7838: 22              LD      (HLI),A             
7839: 52              LD      D,D                 
783A: 28 82           JR      Z,$77BE             ; {}
783C: 54              LD      D,H                 
783D: DF              RST     0X18                
783E: 83              ADD     A,E                 
783F: 60              LD      H,B                 
7840: DF              RST     0X18                
7841: 83              ADD     A,E                 
7842: 67              LD      H,A                 
7843: DF              RST     0X18                
7844: 84              ADD     A,H                 
7845: 70              LD      (HL),B              
7846: DF              RST     0X18                
7847: 75              LD      (HL),L              
7848: DF              RST     0X18                
7849: 82              ADD     A,D                 
784A: 77              LD      (HL),A              
784B: DF              RST     0X18                
784C: 26 CB           LD      H,$CB               
784E: E1              POP     HL                  
784F: 0A              LD      A,(BC)              
7850: ED                              
7851: 48              LD      C,B                 
7852: 40              LD      B,B                 
7853: FE 04           CP      $04                 
7855: 95              SUB     L                   
7856: C8              RET     Z                   
7857: 00              NOP                         
7858: DF              RST     0X18                
7859: 01 DF 02        LD      BC,$02DF            
785C: 25              DEC     H                   
785D: 86              ADD     A,(HL)              
785E: 03              INC     BC                  
785F: 21 09 26        LD      HL,$2609            
7862: 11 25 12        LD      DE,$1225            
7865: 29              ADD     HL,HL               
7866: 13              INC     DE                  
7867: 25              DEC     H                   
7868: 14              INC     D                   
7869: 21 15 26        LD      HL,$2615            
786C: 19              ADD     HL,DE               
786D: 2A              LD      A,(HLI)             
786E: C3 21 23        JP      $2321               
7871: 22              LD      (HLI),A             
7872: 25              DEC     H                   
7873: 23              INC     HL                  
7874: 29              ADD     HL,HL               
7875: 25              DEC     H                   
7876: 2A              LD      A,(HLI)             
7877: 26 21           LD      H,$21               
7879: 27              DAA                         
787A: 26 32           LD      H,$32               
787C: 23              INC     HL                  
787D: 37              SCF                         
787E: 24              INC     H                   
787F: 42              LD      B,D                 
7880: 27              DAA                         
7881: 43              LD      B,E                 
7882: 2B              DEC     HL                  
7883: 45              LD      B,L                 
7884: 2C              INC     L                   
7885: 46              LD      B,(HL)              
7886: 22              LD      (HLI),A             
7887: 47              LD      B,A                 
7888: 28 48           JR      Z,$78D2             ; {}
788A: 2C              INC     L                   
788B: 49              LD      C,C                 
788C: 22              LD      (HLI),A             
788D: 51              LD      D,C                 
788E: 27              DAA                         
788F: 52              LD      D,D                 
7890: 2B              DEC     HL                  
7891: 53              LD      D,E                 
7892: 27              DAA                         
7893: 54              LD      D,H                 
7894: 22              LD      (HLI),A             
7895: 55              LD      D,L                 
7896: 28 56           JR      Z,$78EE             ; {}
7898: 2C              INC     L                   
7899: 57              LD      D,A                 
789A: 22              LD      (HLI),A             
789B: 58              LD      E,B                 
789C: 28 59           JR      Z,$78F7             ; {}
789E: DF              RST     0X18                
789F: 61              LD      H,C                 
78A0: DF              RST     0X18                
78A1: 62              LD      H,D                 
78A2: 27              DAA                         
78A3: 83              ADD     A,E                 
78A4: 63              LD      H,E                 
78A5: 22              LD      (HLI),A             
78A6: 66              LD      H,(HL)              
78A7: 28 83           JR      Z,$782C             ; {}
78A9: 67              LD      H,A                 
78AA: DF              RST     0X18                
78AB: 89              ADC     A,C                 
78AC: 71              LD      (HL),C              
78AD: DF              RST     0X18                
78AE: 34              INC     (HL)                
78AF: BE              CP      (HL)                
78B0: E1              POP     HL                  
78B1: 0A              LD      A,(BC)              
78B2: EC                              
78B3: 68              LD      L,B                 
78B4: 30 FE           JR      NC,$78B4            ; {}
78B6: 04              INC     B                   
78B7: 95              SUB     L                   
78B8: 00              NOP                         
78B9: DF              RST     0X18                
78BA: 01 25 82        LD      BC,$8225            
78BD: 02              LD      (BC),A              
78BE: 21 04 26        LD      HL,$2604            
78C1: 05              DEC     B                   
78C2: 2A              LD      A,(HLI)             
78C3: 06 21           LD      B,$21               
78C5: 07              RLCA                        
78C6: 26 82           LD      H,$82               
78C8: 08 DF 10        LD      ($10DF),SP          
78CB: 21 11 29        LD      HL,$2911            
78CE: 14              INC     D                   
78CF: 2A              LD      A,(HLI)             
78D0: 15              DEC     D                   
78D1: 26 17           LD      H,$17               
78D3: 2A              LD      A,(HLI)             
78D4: 18 26           JR      $78FC               ; {}
78D6: 19              ADD     HL,DE               
78D7: DF              RST     0X18                
78D8: C2 25 24        JP      NZ,$2425            
78DB: 28 2A           JR      Z,$7907             ; {}
78DD: 29              ADD     HL,HL               
78DE: 26 39           LD      H,$39               
78E0: 24              INC     H                   
78E1: 40              LD      B,B                 
78E2: 22              LD      (HLI),A             
78E3: 41              LD      B,C                 
78E4: 2B              DEC     HL                  
78E5: 45              LD      B,L                 
78E6: 2A              LD      A,(HLI)             
78E7: 46              LD      B,(HL)              
78E8: 21 47 98        LD      HL,$9847            
78EB: 48              LD      C,B                 
78EC: 26 49           LD      H,$49               
78EE: 2A              LD      A,(HLI)             
78EF: C3 50 DF        JP      $DF50               
78F2: 51              LD      D,C                 
78F3: 23              INC     HL                  
78F4: 58              LD      E,B                 
78F5: 24              INC     H                   
78F6: C2 59 DF        JP      NZ,$DF59            
78F9: 61              LD      H,C                 
78FA: 27              DAA                         
78FB: 62              LD      H,D                 
78FC: 2B              DEC     HL                  
78FD: 64              LD      H,H                 
78FE: 2C              INC     L                   
78FF: 83              ADD     A,E                 
7900: 65              LD      H,L                 
7901: 22              LD      (HLI),A             
7902: 68              LD      L,B                 
7903: 28 71           JR      Z,$7976             ; {}
7905: DF              RST     0X18                
7906: 72              LD      (HL),D              
7907: 27              DAA                         
7908: 73              LD      (HL),E              
7909: 48              LD      C,B                 
790A: 74              LD      (HL),H              
790B: 28 85           JR      Z,$7892             ; {}
790D: 75              LD      (HL),L              
790E: DF              RST     0X18                
790F: 27              DAA                         
7910: CB E0           SET     1,E                 
7912: 00              NOP                         
7913: 07              RLCA                        
7914: 38 50           JR      C,$7966             ; {}
7916: FE 04           CP      $04                 
7918: 95              SUB     L                   
7919: 8A              ADC     A,D                 
791A: 00              NOP                         
791B: DF              RST     0X18                
791C: 02              LD      (BC),A              
791D: 25              DEC     H                   
791E: 03              INC     BC                  
791F: 3D              DEC     A                   
7920: 04              INC     B                   
7921: 26 10           LD      H,$10               
7923: DF              RST     0X18                
7924: 11 25 12        LD      DE,$1225            
7927: 29              ADD     HL,HL               
7928: 14              INC     D                   
7929: 2A              LD      A,(HLI)             
792A: 82              ADD     A,D                 
792B: 15              DEC     D                   
792C: 21 17 26        LD      HL,$2617            
792F: 82              ADD     A,D                 
7930: 18 DF           JR      $7911               ; {}
7932: 20 25           JR      NZ,$7959            ; {}
7934: 21 29 27        LD      HL,$2729            
7937: 2A              LD      A,(HLI)             
7938: 28 21           JR      Z,$795B             ; {}
793A: 29              ADD     HL,HL               
793B: 26 C2           LD      H,$C2               
793D: 30 23           JR      NC,$7962            ; {}
793F: 39              ADD     HL,SP               
7940: 2A              LD      A,(HLI)             
7941: 50              LD      D,B                 
7942: 27              DAA                         
7943: 51              LD      D,C                 
7944: 2B              DEC     HL                  
7945: 58              LD      E,B                 
7946: 2C              INC     L                   
7947: 59              LD      E,C                 
7948: 22              LD      (HLI),A             
7949: 60              LD      H,B                 
794A: DF              RST     0X18                
794B: 61              LD      H,C                 
794C: 27              DAA                         
794D: 62              LD      H,D                 
794E: 22              LD      (HLI),A             
794F: 63              LD      H,E                 
7950: 2B              DEC     HL                  
7951: 67              LD      H,A                 
7952: 2C              INC     L                   
7953: 68              LD      L,B                 
7954: 28 69           JR      Z,$79BF             ; {}
7956: DF              RST     0X18                
7957: 83              ADD     A,E                 
7958: 70              LD      (HL),B              
7959: DF              RST     0X18                
795A: 73              LD      (HL),E              
795B: 27              DAA                         
795C: 83              ADD     A,E                 
795D: 74              LD      (HL),H              
795E: 22              LD      (HLI),A             
795F: 77              LD      (HL),A              
7960: 28 82           JR      Z,$78E4             ; {}
7962: 78              LD      A,B                 
7963: DF              RST     0X18                
7964: FE 04           CP      $04                 
7966: 05              DEC     B                   
7967: 01 F0 03        LD      BC,$03F0            
796A: 26 82           LD      H,$82               
796C: 04              INC     B                   
796D: AC              XOR     H                   
796E: 06 25           LD      B,$25               
7970: 13              INC     DE                  
7971: 2A              LD      A,(HLI)             
7972: 82              ADD     A,D                 
7973: 14              INC     D                   
7974: 21 16 29        LD      HL,$2916            
7977: 60              LD      H,B                 
7978: 27              DAA                         
7979: 61              LD      H,C                 
797A: 2B              DEC     HL                  
797B: 68              LD      L,B                 
797C: 2C              INC     L                   
797D: 69              LD      L,C                 
797E: 28 70           JR      Z,$79F0             ; {}
7980: 00              NOP                         
7981: 71              LD      (HL),C              
7982: 27              DAA                         
7983: 78              LD      A,B                 
7984: 28 79           JR      Z,$79FF             ; {}
7986: 00              NOP                         
7987: 82              ADD     A,D                 
7988: 17              RLA                         
7989: 0D              DEC     C                   
798A: 82              ADD     A,D                 
798B: 22              LD      (HLI),A             
798C: 0D              DEC     C                   
798D: 25              DEC     H                   
798E: 0D              DEC     C                   
798F: 27              DAA                         
7990: 0D              DEC     C                   
7991: 83              ADD     A,E                 
7992: 31 0D C3        LD      SP,$C30D            
7995: 38 DF           JR      C,$7976             ; {}
7997: 41              LD      B,C                 
7998: 0D              DEC     C                   
7999: 46              LD      B,(HL)              
799A: 0D              DEC     C                   
799B: 82              ADD     A,D                 
799C: 51              LD      D,C                 
799D: 0D              DEC     C                   
799E: 55              LD      D,L                 
799F: 0D              DEC     C                   
79A0: 62              LD      H,D                 
79A1: 0D              DEC     C                   
79A2: 63              LD      H,E                 
79A3: DF              RST     0X18                
79A4: 67              LD      H,A                 
79A5: DF              RST     0X18                
79A6: 74              LD      (HL),H              
79A7: FD                              
79A8: E0 00           LD      ($FF00+$00),A       
79AA: 35              DEC     (HL)                
79AB: 68              LD      L,B                 
79AC: 50              LD      D,B                 
79AD: FE 0C           CP      $0C                 
79AF: 05              DEC     B                   
79B0: 82              ADD     A,D                 
79B1: 00              NOP                         
79B2: DF              RST     0X18                
79B3: 02              LD      (BC),A              
79B4: 25              DEC     H                   
79B5: 05              DEC     B                   
79B6: 29              ADD     HL,HL               
79B7: 06 25           LD      B,$25               
79B9: 10 DF           ;;STOP    $DF                 
79BB: 11 25 12        LD      DE,$1225            
79BE: 29              ADD     HL,HL               
79BF: 16 23           LD      D,$23               
79C1: 82              ADD     A,D                 
79C2: 17              RLA                         
79C3: 1B              DEC     DE                  
79C4: 20 25           JR      NZ,$79EB            ; {}
79C6: 21 29 24        LD      HL,$2429            
79C9: 25              DEC     H                   
79CA: 25              DEC     H                   
79CB: 98              SBC     B                   
79CC: 26 29           LD      H,$29               
79CE: 82              ADD     A,D                 
79CF: 27              DAA                         
79D0: 1B              DEC     DE                  
79D1: 33              INC     SP                  
79D2: 25              DEC     H                   
79D3: 34              INC     (HL)                
79D4: 29              ADD     HL,HL               
79D5: 84              ADD     A,H                 
79D6: 35              DEC     (HL)                
79D7: 1B              DEC     DE                  
79D8: 43              LD      B,E                 
79D9: 23              INC     HL                  
79DA: 85              ADD     A,L                 
79DB: 44              LD      B,H                 
79DC: 1B              DEC     DE                  
79DD: 51              LD      D,C                 
79DE: 25              DEC     H                   
79DF: 52              LD      D,D                 
79E0: 21 53 29        LD      HL,$2953            
79E3: 85              ADD     A,L                 
79E4: 54              LD      D,H                 
79E5: 1B              DEC     DE                  
79E6: 60              LD      H,B                 
79E7: 29              ADD     HL,HL               
79E8: 61              LD      H,C                 
79E9: 23              INC     HL                  
79EA: 87              ADD     A,A                 
79EB: 62              LD      H,D                 
79EC: 1B              DEC     DE                  
79ED: 70              LD      (HL),B              
79EE: 0D              DEC     C                   
79EF: 71              LD      (HL),C              
79F0: 27              DAA                         
79F1: 78              LD      A,B                 
79F2: 3D              DEC     A                   
79F3: 23              INC     HL                  
79F4: CB E1           SET     1,E                 
79F6: 0A              LD      A,(BC)              
79F7: F3              DI                          
79F8: 58              LD      E,B                 
79F9: 40              LD      B,B                 
79FA: FE 0C           CP      $0C                 
79FC: 05              DEC     B                   
79FD: 00              NOP                         
79FE: DF              RST     0X18                
79FF: 01 25 08        LD      BC,$0825            
7A02: 26 09           LD      H,$09               
7A04: DF              RST     0X18                
7A05: 10 DF           ;;STOP    $DF                 
7A07: 11 23 18        LD      DE,$1823            
7A0A: 24              INC     H                   
7A0B: 19              ADD     HL,DE               
7A0C: DF              RST     0X18                
7A0D: 20 25           JR      NZ,$7A34            ; {}
7A0F: 21 29 28        LD      HL,$2829            
7A12: 2A              LD      A,(HLI)             
7A13: 29              ADD     HL,HL               
7A14: 26 60           LD      H,$60               
7A16: 27              DAA                         
7A17: 61              LD      H,C                 
7A18: 2B              DEC     HL                  
7A19: 68              LD      L,B                 
7A1A: 2C              INC     L                   
7A1B: 69              LD      L,C                 
7A1C: 28 70           JR      Z,$7A8E             ; {}
7A1E: DF              RST     0X18                
7A1F: 71              LD      (HL),C              
7A20: 27              DAA                         
7A21: 78              LD      A,B                 
7A22: 28 79           JR      Z,$7A9D             ; {}
7A24: DF              RST     0X18                
7A25: 23              INC     HL                  
7A26: A7              AND     A                   
7A27: 83              ADD     A,E                 
7A28: 34              INC     (HL)                
7A29: A7              AND     A                   
7A2A: 41              LD      B,C                 
7A2B: A7              AND     A                   
7A2C: 43              LD      B,E                 
7A2D: A7              AND     A                   
7A2E: 82              ADD     A,D                 
7A2F: 46              LD      B,(HL)              
7A30: A7              AND     A                   
7A31: 52              LD      D,D                 
7A32: A7              AND     A                   
7A33: 58              LD      E,B                 
7A34: A7              AND     A                   
7A35: 66              LD      H,(HL)              
7A36: A7              AND     A                   
7A37: 13              INC     DE                  
7A38: A0              AND     B                   
7A39: 38 A0           JR      C,$79DB             ; {}
7A3B: 42              LD      B,D                 
7A3C: A0              AND     B                   
7A3D: 54              LD      D,H                 
7A3E: A0              AND     B                   
7A3F: 56              LD      D,(HL)              
7A40: A0              AND     B                   
7A41: 04              INC     B                   
7A42: 29              ADD     HL,HL               
7A43: 05              DEC     B                   
7A44: 05              DEC     B                   
7A45: 06 2A           LD      B,$2A               
7A47: 74              LD      (HL),H              
7A48: FD                              
7A49: E0 00           LD      ($FF00+$00),A       
7A4B: 0D              DEC     C                   
7A4C: 18 70           JR      $7ABE               ; {}
7A4E: FE 0C           CP      $0C                 
7A50: 9D              SBC     L                   
7A51: 87              ADD     A,A                 
7A52: 02              LD      (BC),A              
7A53: DF              RST     0X18                
7A54: 87              ADD     A,A                 
7A55: 12              LD      (DE),A              
7A56: DF              RST     0X18                
7A57: 82              ADD     A,D                 
7A58: 21 DF C2        LD      HL,$C2DF            
7A5B: 29              ADD     HL,HL               
7A5C: DF              RST     0X18                
7A5D: 30 DF           JR      NC,$7A3E            ; {}
7A5F: 32              LD      (HLD),A             
7A60: DF              RST     0X18                
7A61: 82              ADD     A,D                 
7A62: 40              LD      B,B                 
7A63: DF              RST     0X18                
7A64: C2 43 DF        JP      NZ,$DF43            
7A67: 48              LD      C,B                 
7A68: DF              RST     0X18                
7A69: 51              LD      D,C                 
7A6A: DF              RST     0X18                
7A6B: 82              ADD     A,D                 
7A6C: 58              LD      E,B                 
7A6D: DF              RST     0X18                
7A6E: 82              ADD     A,D                 
7A6F: 61              LD      H,C                 
7A70: DF              RST     0X18                
7A71: 82              ADD     A,D                 
7A72: 67              LD      H,A                 
7A73: DF              RST     0X18                
7A74: 70              LD      (HL),B              
7A75: DF              RST     0X18                
7A76: 72              LD      (HL),D              
7A77: DF              RST     0X18                
7A78: 77              LD      (HL),A              
7A79: DF              RST     0X18                
7A7A: 79              LD      A,C                 
7A7B: DF              RST     0X18                
7A7C: C7              RST     0X00                
7A7D: 15              DEC     D                   
7A7E: 05              DEC     B                   
7A7F: 83              ADD     A,E                 
7A80: 24              INC     H                   
7A81: 05              DEC     B                   
7A82: 04              INC     B                   
7A83: 25              DEC     H                   
7A84: 05              DEC     B                   
7A85: 21 06 26        LD      HL,$2606            
7A88: 13              INC     DE                  
7A89: 25              DEC     H                   
7A8A: 14              INC     D                   
7A8B: 29              ADD     HL,HL               
7A8C: 16 2A           LD      D,$2A               
7A8E: 17              RLA                         
7A8F: 26 23           LD      H,$23               
7A91: 23              INC     HL                  
7A92: 27              DAA                         
7A93: 24              INC     H                   
7A94: 33              INC     SP                  
7A95: 27              DAA                         
7A96: 34              INC     (HL)                
7A97: 2B              DEC     HL                  
7A98: 36 2C           LD      (HL),$2C            
7A9A: 37              SCF                         
7A9B: 28 C4           JR      Z,$7A61             ; {}
7A9D: 44              LD      B,H                 
7A9E: 23              INC     HL                  
7A9F: C4 46 24        CALL    NZ,$2446            
7AA2: 25              DEC     H                   
7AA3: BE              CP      (HL)                
7AA4: E1              POP     HL                  
7AA5: 0A              LD      A,(BC)              
7AA6: F1              POP     AF                  
7AA7: 38 30           JR      C,$7AD9             ; {}
7AA9: FE 0C           CP      $0C                 
7AAB: 15              DEC     D                   
7AAC: C2 03 A6        JP      NZ,$A603            
7AAF: 05              DEC     B                   
7AB0: A6              AND     (HL)                
7AB1: 85              ADD     A,L                 
7AB2: 23              INC     HL                  
7AB3: A6              AND     (HL)                
7AB4: 85              ADD     A,L                 
7AB5: 31 4E 37        LD      SP,$374E            
7AB8: A7              AND     A                   
7AB9: 38 4E           JR      C,$7B09             ; {}
7ABB: 84              ADD     A,H                 
7ABC: 41              LD      B,C                 
7ABD: A6              AND     (HL)                
7ABE: C3 46 A6        JP      $A646               
7AC1: 48              LD      C,B                 
7AC2: A0              AND     B                   
7AC3: 60              LD      H,B                 
7AC4: 27              DAA                         
7AC5: 61              LD      H,C                 
7AC6: 2B              DEC     HL                  
7AC7: 68              LD      L,B                 
7AC8: 2C              INC     L                   
7AC9: 69              LD      L,C                 
7ACA: 28 70           JR      Z,$7B3C             ; {}
7ACC: 0D              DEC     C                   
7ACD: 71              LD      (HL),C              
7ACE: 27              DAA                         
7ACF: 78              LD      A,B                 
7AD0: 28 79           JR      Z,$7B4B             ; {}
7AD2: 0D              DEC     C                   
7AD3: 73              LD      (HL),E              
7AD4: FD                              
7AD5: E0 00           LD      ($FF00+$00),A       
7AD7: 86              ADD     A,(HL)              
7AD8: 18 40           JR      $7B1A               ; {}
7ADA: FE 05           CP      $05                 
7ADC: 90              SUB     B                   
7ADD: 8A              ADC     A,D                 
7ADE: 10 7B           ;;STOP    $7B                 
7AE0: 88              ADC     A,B                 
7AE1: 22              LD      (HLI),A             
7AE2: 78              LD      A,B                 
7AE3: 23              INC     HL                  
7AE4: 79              LD      A,C                 
7AE5: 25              DEC     H                   
7AE6: 79              LD      A,C                 
7AE7: 27              DAA                         
7AE8: 79              LD      A,C                 
7AE9: 29              ADD     HL,HL               
7AEA: 79              LD      A,C                 
7AEB: 88              ADC     A,B                 
7AEC: 32              LD      (HLD),A             
7AED: 03              INC     BC                  
7AEE: 88              ADC     A,B                 
7AEF: 42              LD      B,D                 
7AF0: 80              ADD     A,B                 
7AF1: 88              ADC     A,B                 
7AF2: 52              LD      D,D                 
7AF3: 81              ADD     A,C                 
7AF4: 84              ADD     A,H                 
7AF5: 63              LD      H,E                 
7AF6: 81              ADD     A,C                 
7AF7: 73              LD      (HL),E              
7AF8: 81              ADD     A,C                 
7AF9: 20 6C           JR      NZ,$7B67            ; {}
7AFB: 21 6D 30        LD      HL,$306D            
7AFE: 60              LD      H,B                 
7AFF: 31 61 C4        LD      SP,$C461            
7B02: 40              LD      B,B                 
7B03: 54              LD      D,H                 
7B04: C2 41 57        JP      NZ,$5741            ; {}
7B07: C2 61 54        JP      NZ,$5461            ; {}
7B0A: 62              LD      H,D                 
7B0B: 56              LD      D,(HL)              
7B0C: 72              LD      (HL),D              
7B0D: 54              LD      D,H                 
7B0E: 52              LD      D,D                 
7B0F: 72              LD      (HL),D              
7B10: 82              ADD     A,D                 
7B11: 57              LD      D,A                 
7B12: 72              LD      (HL),D              
7B13: 65              LD      H,L                 
7B14: 72              LD      (HL),D              
7B15: 67              LD      H,A                 
7B16: 50              LD      D,B                 
7B17: 82              ADD     A,D                 
7B18: 68              LD      L,B                 
7B19: 53              LD      D,E                 
7B1A: 84              ADD     A,H                 
7B1B: 73              LD      (HL),E              
7B1C: 53              LD      D,E                 
7B1D: 83              ADD     A,E                 
7B1E: 77              LD      (HL),A              
7B1F: 54              LD      D,H                 
7B20: E0 00           LD      ($FF00+$00),A       
7B22: EA 68 30        LD      ($3068),A           
7B25: FE 0C           CP      $0C                 
7B27: 25              DEC     H                   
7B28: 07              RLCA                        
7B29: 29              ADD     HL,HL               
7B2A: 08 0D 09        LD      ($090D),SP          
7B2D: 24              INC     H                   
7B2E: 85              ADD     A,L                 
7B2F: 11 DF 19        LD      DE,$19DF            
7B32: 2A              LD      A,(HLI)             
7B33: 82              ADD     A,D                 
7B34: 21 DF 23        LD      HL,$23DF            
7B37: 2C              INC     L                   
7B38: 24              INC     H                   
7B39: 2B              DEC     HL                  
7B3A: 28 AE           JR      Z,$7AEA             ; {}
7B3C: 29              ADD     HL,HL               
7B3D: AF              XOR     A                   
7B3E: 31 DF 33        LD      SP,$33DF            
7B41: 2A              LD      A,(HLI)             
7B42: 34              INC     (HL)                
7B43: 29              ADD     HL,HL               
7B44: 36 2C           LD      (HL),$2C            
7B46: 37              SCF                         
7B47: 2B              DEC     HL                  
7B48: 39              ADD     HL,SP               
7B49: B0              OR      B                   
7B4A: 41              LD      B,C                 
7B4B: AE              XOR     (HL)                
7B4C: 46              LD      B,(HL)              
7B4D: 2A              LD      A,(HLI)             
7B4E: 47              LD      B,A                 
7B4F: 29              ADD     HL,HL               
7B50: 50              LD      D,B                 
7B51: 27              DAA                         
7B52: 51              LD      D,C                 
7B53: 2B              DEC     HL                  
7B54: 82              ADD     A,D                 
7B55: 52              LD      D,D                 
7B56: AE              XOR     (HL)                
7B57: 60              LD      H,B                 
7B58: 0D              DEC     C                   
7B59: 61              LD      H,C                 
7B5A: 27              DAA                         
7B5B: 62              LD      H,D                 
7B5C: 22              LD      (HLI),A             
7B5D: 63              LD      H,E                 
7B5E: 2B              DEC     HL                  
7B5F: 86              ADD     A,(HL)              
7B60: 64              LD      H,H                 
7B61: AE              XOR     (HL)                
7B62: 82              ADD     A,D                 
7B63: 70              LD      (HL),B              
7B64: 0D              DEC     C                   
7B65: 72              LD      (HL),D              
7B66: 00              NOP                         
7B67: 73              LD      (HL),E              
7B68: 27              DAA                         
7B69: FE 0C           CP      $0C                 
7B6B: 45              LD      B,L                 
7B6C: 82              ADD     A,D                 
7B6D: 00              NOP                         
7B6E: 00              NOP                         
7B6F: 02              LD      (BC),A              
7B70: 25              DEC     H                   
7B71: 05              DEC     B                   
7B72: 47              LD      B,A                 
7B73: 07              RLCA                        
7B74: 26 08           LD      H,$08               
7B76: 24              INC     H                   
7B77: 09              ADD     HL,BC               
7B78: 00              NOP                         
7B79: 82              ADD     A,D                 
7B7A: 10 21           ;;STOP    $21                 
7B7C: 12              LD      (DE),A              
7B7D: 29              ADD     HL,HL               
7B7E: 82              ADD     A,D                 
7B7F: 13              INC     DE                  
7B80: AE              XOR     (HL)                
7B81: 16 A7           LD      D,$A7               
7B83: 17              RLA                         
7B84: 24              INC     H                   
7B85: 18 2A           JR      $7BB1               ; {}
7B87: 19              ADD     HL,DE               
7B88: 26 83           LD      H,$83               
7B8A: 20 AF           JR      NZ,$7B3B            ; {}
7B8C: 27              DAA                         
7B8D: 2A              LD      A,(HLI)             
7B8E: 28 26           JR      Z,$7BB6             ; {}
7B90: 82              ADD     A,D                 
7B91: 30 B0           JR      NC,$7B43            ; {}
7B93: C3 32 01        JP      $0132               
7B96: 33              INC     SP                  
7B97: AE              XOR     (HL)                
7B98: 83              ADD     A,E                 
7B99: 34              INC     (HL)                
7B9A: AF              XOR     A                   
7B9B: C3 38 24        JP      $2438               
7B9E: 44              LD      B,H                 
7B9F: B0              OR      B                   
7BA0: 46              LD      B,(HL)              
7BA1: 01 45 B0        LD      BC,$B045            
7BA4: 56              LD      D,(HL)              
7BA5: B0              OR      B                   
7BA6: 51              LD      D,C                 
7BA7: AF              XOR     A                   
7BA8: 84              ADD     A,H                 
7BA9: 60              LD      H,B                 
7BAA: AE              XOR     (HL)                
7BAB: 82              ADD     A,D                 
7BAC: 61              LD      H,C                 
7BAD: B0              OR      B                   
7BAE: 55              LD      D,L                 
7BAF: A7              AND     A                   
7BB0: 64              LD      H,H                 
7BB1: A7              AND     A                   
7BB2: 67              LD      H,A                 
7BB3: 2C              INC     L                   
7BB4: 68              LD      L,B                 
7BB5: 28 77           JR      Z,$7C2E             ; {}
7BB7: 28 78           JR      Z,$7C31             ; {}
7BB9: 2C              INC     L                   
7BBA: 75              LD      (HL),L              
7BBB: FD                              
7BBC: E0 00           LD      ($FF00+$00),A       
7BBE: CD 88 20        CALL    $2088               
7BC1: FE 00           CP      $00                 
7BC3: 90              SUB     B                   
7BC4: C4 02 E1        CALL    NZ,$E102            
7BC7: 84              ADD     A,H                 
7BC8: 03              INC     BC                  
7BC9: E0 84           LD      ($FF00+$84),A       
7BCB: 13              INC     DE                  
7BCC: E0 84           LD      ($FF00+$84),A       
7BCE: 23              INC     HL                  
7BCF: E0 84           LD      ($FF00+$84),A       
7BD1: 33              INC     SP                  
7BD2: E0 C4           LD      ($FF00+$C4),A       
7BD4: 07              RLCA                        
7BD5: E2              LD      (C),A               
7BD6: C4 05 63        CALL    NZ,$6305            ; {}
7BD9: 43              LD      B,E                 
7BDA: 70              LD      (HL),B              
7BDB: 44              LD      B,H                 
7BDC: 04              INC     B                   
7BDD: 45              LD      B,L                 
7BDE: 64              LD      H,H                 
7BDF: 46              LD      B,(HL)              
7BE0: 71              LD      (HL),C              
7BE1: 50              LD      D,B                 
7BE2: 6C              LD      L,H                 
7BE3: 88              ADC     A,B                 
7BE4: 51              LD      D,C                 
7BE5: 68              LD      L,B                 
7BE6: 59              LD      E,C                 
7BE7: 6D              LD      L,L                 
7BE8: 61              LD      H,C                 
7BE9: 6E              LD      L,(HL)              
7BEA: 86              ADD     A,(HL)              
7BEB: 62              LD      H,D                 
7BEC: 6A              LD      L,D                 
7BED: 68              LD      L,B                 
7BEE: 6F              LD      L,A                 
7BEF: 71              LD      (HL),C              
7BF0: 6C              LD      L,H                 
7BF1: 86              ADD     A,(HL)              
7BF2: 72              LD      (HL),D              
7BF3: 68              LD      L,B                 
7BF4: 78              LD      A,B                 
7BF5: 6D              LD      L,L                 
7BF6: E1              POP     HL                  
7BF7: 06 2E           LD      B,$2E               
7BF9: 18 10           JR      $7C0B               ; {}
7BFB: FE 0C           CP      $0C                 
7BFD: 90              SUB     B                   
7BFE: 04              INC     B                   
7BFF: 25              DEC     H                   
7C00: 85              ADD     A,L                 
7C01: 05              DEC     B                   
7C02: 21 08 47        LD      HL,$4708            
7C05: 84              ADD     A,H                 
7C06: 00              NOP                         
7C07: 0D              DEC     C                   
7C08: 03              INC     BC                  
7C09: DF              RST     0X18                
7C0A: 10 0D           ;;STOP    $0D                 
7C0C: 11 DF 12        LD      DE,$12DF            
7C0F: 25              DEC     H                   
7C10: 13              INC     DE                  
7C11: 21 14 29        LD      HL,$2914            
7C14: 85              ADD     A,L                 
7C15: 15              DEC     D                   
7C16: 1B              DEC     DE                  
7C17: 20 DF           JR      NZ,$7BF8            ; {}
7C19: 21 25 22        LD      HL,$2225            
7C1C: 29              ADD     HL,HL               
7C1D: 87              ADD     A,A                 
7C1E: 23              INC     HL                  
7C1F: 1B              DEC     DE                  
7C20: 30 0D           JR      NC,$7C2F            ; {}
7C22: 31 23 83        LD      SP,$8323            
7C25: 32              LD      (HLD),A             
7C26: 1B              DEC     DE                  
7C27: 35              DEC     (HL)                
7C28: 2C              INC     L                   
7C29: 84              ADD     A,H                 
7C2A: 36 22           LD      (HL),$22            
7C2C: 40              LD      B,B                 
7C2D: 25              DEC     H                   
7C2E: 41              LD      B,C                 
7C2F: 29              ADD     HL,HL               
7C30: 82              ADD     A,D                 
7C31: 42              LD      B,D                 
7C32: 1B              DEC     DE                  
7C33: 44              LD      B,H                 
7C34: 2C              INC     L                   
7C35: 45              LD      B,L                 
7C36: 28 49           JR      Z,$7C81             ; {}
7C38: DF              RST     0X18                
7C39: C2 50 23        JP      NZ,$2350            
7C3C: 82              ADD     A,D                 
7C3D: 51              LD      D,C                 
7C3E: 1B              DEC     DE                  
7C3F: 82              ADD     A,D                 
7C40: 61              LD      H,C                 
7C41: 1B              DEC     DE                  
7C42: 53              LD      D,E                 
7C43: 2C              INC     L                   
7C44: 54              LD      D,H                 
7C45: 28 83           JR      Z,$7BCA             ; {}
7C47: 56              LD      D,(HL)              
7C48: DF              RST     0X18                
7C49: 63              LD      H,E                 
7C4A: 24              INC     H                   
7C4B: 85              ADD     A,L                 
7C4C: 65              LD      H,L                 
7C4D: DF              RST     0X18                
7C4E: 70              LD      (HL),B              
7C4F: 27              DAA                         
7C50: 73              LD      (HL),E              
7C51: 28 82           JR      Z,$7BD5             ; {}
7C53: 74              LD      (HL),H              
7C54: DF              RST     0X18                
7C55: 79              LD      A,C                 
7C56: DF              RST     0X18                
7C57: 18 05           JR      $7C5E               ; {}
7C59: 71              LD      (HL),C              
7C5A: FD                              
7C5B: E0 00           LD      ($FF00+$00),A       
7C5D: 1D              DEC     E                   
7C5E: 18 30           JR      $7C90               ; {}
7C60: FE 0C           CP      $0C                 
7C62: 90              SUB     B                   
7C63: 85              ADD     A,L                 
7C64: 00              NOP                         
7C65: 21 05 26        LD      HL,$2605            
7C68: 15              DEC     D                   
7C69: 2A              LD      A,(HLI)             
7C6A: 16 21           LD      D,$21               
7C6C: 17              RLA                         
7C6D: 26 27           LD      H,$27               
7C6F: 24              INC     H                   
7C70: 37              SCF                         
7C71: 2A              LD      A,(HLI)             
7C72: 38 26           JR      C,$7C9A             ; {}
7C74: C4 48 24        CALL    NZ,$2448            
7C77: 85              ADD     A,L                 
7C78: 10 05           ;;STOP    $05                 
7C7A: 83              ADD     A,E                 
7C7B: 20 1B           JR      NZ,$7C98            ; {}
7C7D: 84              ADD     A,H                 
7C7E: 23              INC     HL                  
7C7F: 05              DEC     B                   
7C80: 83              ADD     A,E                 
7C81: 30 22           JR      NC,$7CA5            ; {}
7C83: 33              INC     SP                  
7C84: 2B              DEC     HL                  
7C85: 83              ADD     A,E                 
7C86: 34              INC     (HL)                
7C87: 05              DEC     B                   
7C88: 83              ADD     A,E                 
7C89: 45              LD      B,L                 
7C8A: 05              DEC     B                   
7C8B: 82              ADD     A,D                 
7C8C: 56              LD      D,(HL)              
7C8D: 05              DEC     B                   
7C8E: 82              ADD     A,D                 
7C8F: 66              LD      H,(HL)              
7C90: 05              DEC     B                   
7C91: 43              LD      B,E                 
7C92: 27              DAA                         
7C93: 44              LD      B,H                 
7C94: 2B              DEC     HL                  
7C95: 54              LD      D,H                 
7C96: 27              DAA                         
7C97: 55              LD      D,L                 
7C98: 2B              DEC     HL                  
7C99: C2 65 23        JP      NZ,$2365            
7C9C: 40              LD      B,B                 
7C9D: DF              RST     0X18                
7C9E: 82              ADD     A,D                 
7C9F: 51              LD      D,C                 
7CA0: DF              RST     0X18                
7CA1: 84              ADD     A,H                 
7CA2: 60              LD      H,B                 
7CA3: DF              RST     0X18                
7CA4: 70              LD      (HL),B              
7CA5: DF              RST     0X18                
7CA6: 82              ADD     A,D                 
7CA7: 73              LD      (HL),E              
7CA8: DF              RST     0X18                
7CA9: 84              ADD     A,H                 
7CAA: 06 DF           LD      B,$DF               
7CAC: 09              ADD     HL,BC               
7CAD: 0D              DEC     C                   
7CAE: C2 18 0D        JP      NZ,$0D18            
7CB1: C4 19 DF        CALL    NZ,$DF19            
7CB4: C3 59 0D        JP      $0D59               
7CB7: 76              HALT                        
7CB8: FD                              
7CB9: E0 00           LD      ($FF00+$00),A       
7CBB: 1D              DEC     E                   
7CBC: 78              LD      A,B                 
7CBD: 50              LD      D,B                 
7CBE: FE 0C           CP      $0C                 
7CC0: 0D              DEC     C                   
7CC1: 00              NOP                         
7CC2: DF              RST     0X18                
7CC3: 01 25 10        LD      BC,$1025            
7CC6: 25              DEC     H                   
7CC7: 11 29 18        LD      DE,$1829            
7CCA: 2A              LD      A,(HLI)             
7CCB: 19              ADD     HL,DE               
7CCC: 26 08           LD      H,$08               
7CCE: 26 09           LD      H,$09               
7CD0: DF              RST     0X18                
7CD1: 60              LD      H,B                 
7CD2: 27              DAA                         
7CD3: 61              LD      H,C                 
7CD4: 2B              DEC     HL                  
7CD5: 70              LD      (HL),B              
7CD6: DF              RST     0X18                
7CD7: 71              LD      (HL),C              
7CD8: 27              DAA                         
7CD9: 03              INC     BC                  
7CDA: C7              RST     0X00                
7CDB: 06 C7           LD      B,$C7               
7CDD: 84              ADD     A,H                 
7CDE: 33              INC     SP                  
7CDF: 1B              DEC     DE                  
7CE0: 84              ADD     A,H                 
7CE1: 43              LD      B,E                 
7CE2: 1B              DEC     DE                  
7CE3: 82              ADD     A,D                 
7CE4: 54              LD      D,H                 
7CE5: 1B              DEC     DE                  
7CE6: 38 0F           JR      C,$7CF7             ; {}
7CE8: 62              LD      H,D                 
7CE9: 0F              RRCA                        
7CEA: 68              LD      L,B                 
7CEB: CB E0           SET     1,E                 
7CED: 00              NOP                         
7CEE: D4 88 30        CALL    NC,$3088            
7CF1: FE 0C           CP      $0C                 
7CF3: 05              DEC     B                   
7CF4: 00              NOP                         
7CF5: 0D              DEC     C                   
7CF6: 82              ADD     A,D                 
7CF7: 01 DF 82        LD      BC,$82DF            
7CFA: 03              INC     BC                  
7CFB: 0D              DEC     C                   
7CFC: 82              ADD     A,D                 
7CFD: 05              DEC     B                   
7CFE: DF              RST     0X18                
7CFF: 07              RLCA                        
7D00: 0D              DEC     C                   
7D01: 82              ADD     A,D                 
7D02: 08 DF 82        LD      ($82DF),SP          
7D05: 10 DF           ;;STOP    $DF                 
7D07: 12              LD      (DE),A              
7D08: 25              DEC     H                   
7D09: 83              ADD     A,E                 
7D0A: 13              INC     DE                  
7D0B: 21 16 26        LD      HL,$2616            
7D0E: 17              RLA                         
7D0F: DF              RST     0X18                
7D10: 18 0D           JR      $7D1F               ; {}
7D12: 19              ADD     HL,DE               
7D13: DF              RST     0X18                
7D14: 20 DF           JR      NZ,$7CF5            ; {}
7D16: 21 25 22        LD      HL,$2225            
7D19: 29              ADD     HL,HL               
7D1A: 26 2A           LD      H,$2A               
7D1C: 27              DAA                         
7D1D: 26 82           LD      H,$82               
7D1F: 28 DF           JR      Z,$7D00             ; {}
7D21: 30 DF           JR      NC,$7D02            ; {}
7D23: C2 31 23        JP      NZ,$2331            
7D26: 34              INC     (HL)                
7D27: A0              AND     B                   
7D28: C3 37 24        JP      $2437               
7D2B: 38 DF           JR      C,$7D0C             ; {}
7D2D: 39              ADD     HL,SP               
7D2E: 0D              DEC     C                   
7D2F: C2 40 0D        JP      NZ,$0D40            
7D32: 48              LD      C,B                 
7D33: 0D              DEC     C                   
7D34: 49              LD      C,C                 
7D35: DF              RST     0X18                
7D36: 51              LD      D,C                 
7D37: 27              DAA                         
7D38: 52              LD      D,D                 
7D39: 2B              DEC     HL                  
7D3A: 58              LD      E,B                 
7D3B: DF              RST     0X18                
7D3C: 59              LD      E,C                 
7D3D: 0D              DEC     C                   
7D3E: 82              ADD     A,D                 
7D3F: 60              LD      H,B                 
7D40: DF              RST     0X18                
7D41: 62              LD      H,D                 
7D42: 27              DAA                         
7D43: 84              ADD     A,H                 
7D44: 63              LD      H,E                 
7D45: 22              LD      (HLI),A             
7D46: 67              LD      H,A                 
7D47: 28 82           JR      Z,$7CCB             ; {}
7D49: 68              LD      L,B                 
7D4A: DF              RST     0X18                
7D4B: 70              LD      (HL),B              
7D4C: DF              RST     0X18                
7D4D: 82              ADD     A,D                 
7D4E: 71              LD      (HL),C              
7D4F: 0D              DEC     C                   
7D50: 85              ADD     A,L                 
7D51: 73              LD      (HL),E              
7D52: DF              RST     0X18                
7D53: 82              ADD     A,D                 
7D54: 78              LD      A,B                 
7D55: 0D              DEC     C                   
7D56: 56              LD      D,(HL)              
7D57: CB E0           SET     1,E                 
7D59: 00              NOP                         
7D5A: AE              XOR     (HL)                
7D5B: 48              LD      C,B                 
7D5C: 70              LD      (HL),B              
7D5D: FE 05           CP      $05                 
7D5F: 94              SUB     H                   
7D60: 89              ADC     A,C                 
7D61: 20 80           JR      NZ,$7CE3            ; {}
7D63: 89              ADC     A,C                 
7D64: 30 81           JR      NC,$7CE7            ; {}
7D66: 89              ADC     A,C                 
7D67: 40              LD      B,B                 
7D68: 81              ADD     A,C                 
7D69: 89              ADC     A,C                 
7D6A: 50              LD      D,B                 
7D6B: 81              ADD     A,C                 
7D6C: 89              ADC     A,C                 
7D6D: 60              LD      H,B                 
7D6E: 81              ADD     A,C                 
7D6F: 89              ADC     A,C                 
7D70: 70              LD      (HL),B              
7D71: 81              ADD     A,C                 
7D72: 00              NOP                         
7D73: 57              LD      D,A                 
7D74: 01 5E 10        LD      BC,$105E            
7D77: 5E              LD      E,(HL)              
7D78: 06 5A           LD      B,$5A               
7D7A: 07              RLCA                        
7D7B: 51              LD      D,C                 
7D7C: C2 08 51        JP      NZ,$5108            ; {}
7D7F: C8              RET     Z                   
7D80: 09              ADD     HL,BC               
7D81: 51              LD      D,C                 
7D82: 17              RLA                         
7D83: 5A              LD      E,D                 
7D84: 28 52           JR      Z,$7DD8             ; {}
7D86: 58              LD      E,B                 
7D87: 72              LD      (HL),D              
7D88: 60              LD      H,B                 
7D89: 56              LD      D,(HL)              
7D8A: 70              LD      (HL),B              
7D8B: 57              LD      D,A                 
7D8C: 71              LD      (HL),C              
7D8D: 56              LD      D,(HL)              
7D8E: 73              LD      (HL),E              
7D8F: 72              LD      (HL),D              
7D90: 76              HALT                        
7D91: 72              LD      (HL),D              
7D92: 67              LD      H,A                 
7D93: 72              LD      (HL),D              
7D94: 68              LD      L,B                 
7D95: 50              LD      D,B                 
7D96: 77              LD      (HL),A              
7D97: 50              LD      D,B                 
7D98: 78              LD      A,B                 
7D99: 51              LD      D,C                 
7D9A: E0 00           LD      ($FF00+$00),A       
7D9C: 2A              LD      A,(HLI)             
7D9D: 68              LD      L,B                 
7D9E: 30 FE           JR      NC,$7D9E            ; {}
7DA0: 0C              INC     C                   
7DA1: 0D              DEC     C                   
7DA2: 82              ADD     A,D                 
7DA3: 05              DEC     B                   
7DA4: 99              SBC     C                   
7DA5: 83              ADD     A,E                 
7DA6: 11 1B 82        LD      DE,$821B            
7DA9: 15              DEC     D                   
7DAA: 9A              SBC     D                   
7DAB: 82              ADD     A,D                 
7DAC: 17              RLA                         
7DAD: 20 83           JR      NZ,$7D32            ; {}
7DAF: 21 1B 28        LD      HL,$281B            
7DB2: 20 83           JR      NZ,$7D37            ; {}
7DB4: 31 1B C3        LD      SP,$C31B            
7DB7: 14              INC     D                   
7DB8: 11 41 12        LD      DE,$1241            
7DBB: 43              LD      B,E                 
7DBC: 12              LD      (DE),A              
7DBD: 44              LD      B,H                 
7DBE: 93              SUB     E                   
7DBF: 83              ADD     A,E                 
7DC0: 51              LD      D,C                 
7DC1: A6              AND     (HL)                
7DC2: 83              ADD     A,E                 
7DC3: 56              LD      D,(HL)              
7DC4: A6              AND     (HL)                
7DC5: 83              ADD     A,E                 
7DC6: 61              LD      H,C                 
7DC7: A6              AND     (HL)                
7DC8: 83              ADD     A,E                 
7DC9: 66              LD      H,(HL)              
7DCA: A6              AND     (HL)                
7DCB: 12              LD      (DE),A              
7DCC: C5              PUSH    BC                  
7DCD: 22              LD      (HLI),A             
7DCE: C6 74           ADD     $74                 
7DD0: FD                              
7DD1: E0 00           LD      ($FF00+$00),A       
7DD3: E3                              
7DD4: 48              LD      C,B                 
7DD5: 30 FE           JR      NC,$7DD5            ; {}
7DD7: FF              RST     0X38                
7DD8: FF              RST     0X38                
7DD9: FF              RST     0X38                
7DDA: FF              RST     0X38                
7DDB: FF              RST     0X38                
7DDC: FF              RST     0X38                
7DDD: FF              RST     0X38                
7DDE: FF              RST     0X38                
7DDF: FF              RST     0X38                
7DE0: FF              RST     0X38                
7DE1: FF              RST     0X38                
7DE2: FF              RST     0X38                
7DE3: FF              RST     0X38                
7DE4: FF              RST     0X38                
7DE5: FF              RST     0X38                
7DE6: FF              RST     0X38                
7DE7: FF              RST     0X38                
7DE8: FF              RST     0X38                
7DE9: FF              RST     0X38                
7DEA: FF              RST     0X38                
7DEB: FF              RST     0X38                
7DEC: FF              RST     0X38                
7DED: FF              RST     0X38                
7DEE: FF              RST     0X38                
7DEF: FF              RST     0X38                
7DF0: FF              RST     0X38                
7DF1: FF              RST     0X38                
7DF2: FF              RST     0X38                
7DF3: FF              RST     0X38                
7DF4: FF              RST     0X38                
7DF5: FF              RST     0X38                
7DF6: FF              RST     0X38                
7DF7: FF              RST     0X38                
7DF8: FF              RST     0X38                
7DF9: FF              RST     0X38                
7DFA: FF              RST     0X38                
7DFB: FF              RST     0X38                
7DFC: FF              RST     0X38                
7DFD: FF              RST     0X38                
7DFE: FF              RST     0X38                
7DFF: FF              RST     0X38                
7E00: FF              RST     0X38                
7E01: FF              RST     0X38                
7E02: FF              RST     0X38                
7E03: FF              RST     0X38                
7E04: FF              RST     0X38                
7E05: FF              RST     0X38                
7E06: FF              RST     0X38                
7E07: FF              RST     0X38                
7E08: FF              RST     0X38                
7E09: FF              RST     0X38                
7E0A: FF              RST     0X38                
7E0B: FF              RST     0X38                
7E0C: FF              RST     0X38                
7E0D: FF              RST     0X38                
7E0E: FF              RST     0X38                
7E0F: FF              RST     0X38                
7E10: FF              RST     0X38                
7E11: FF              RST     0X38                
7E12: FF              RST     0X38                
7E13: FF              RST     0X38                
7E14: FF              RST     0X38                
7E15: FF              RST     0X38                
7E16: FF              RST     0X38                
7E17: FF              RST     0X38                
7E18: FF              RST     0X38                
7E19: FF              RST     0X38                
7E1A: FF              RST     0X38                
7E1B: FF              RST     0X38                
7E1C: FF              RST     0X38                
7E1D: FF              RST     0X38                
7E1E: FF              RST     0X38                
7E1F: FF              RST     0X38                
7E20: FF              RST     0X38                
7E21: FF              RST     0X38                
7E22: FF              RST     0X38                
7E23: FF              RST     0X38                
7E24: FF              RST     0X38                
7E25: FF              RST     0X38                
7E26: FF              RST     0X38                
7E27: FF              RST     0X38                
7E28: FF              RST     0X38                
7E29: FF              RST     0X38                
7E2A: FF              RST     0X38                
7E2B: FF              RST     0X38                
7E2C: FF              RST     0X38                
7E2D: FF              RST     0X38                
7E2E: FF              RST     0X38                
7E2F: FF              RST     0X38                
7E30: FF              RST     0X38                
7E31: FF              RST     0X38                
7E32: FF              RST     0X38                
7E33: FF              RST     0X38                
7E34: FF              RST     0X38                
7E35: FF              RST     0X38                
7E36: FF              RST     0X38                
7E37: FF              RST     0X38                
7E38: FF              RST     0X38                
7E39: FF              RST     0X38                
7E3A: FF              RST     0X38                
7E3B: FF              RST     0X38                
7E3C: FF              RST     0X38                
7E3D: FF              RST     0X38                
7E3E: FF              RST     0X38                
7E3F: FF              RST     0X38                
7E40: FF              RST     0X38                
7E41: FF              RST     0X38                
7E42: FF              RST     0X38                
7E43: FF              RST     0X38                
7E44: FF              RST     0X38                
7E45: FF              RST     0X38                
7E46: FF              RST     0X38                
7E47: FF              RST     0X38                
7E48: FF              RST     0X38                
7E49: FF              RST     0X38                
7E4A: FF              RST     0X38                
7E4B: FF              RST     0X38                
7E4C: FF              RST     0X38                
7E4D: FF              RST     0X38                
7E4E: FF              RST     0X38                
7E4F: FF              RST     0X38                
7E50: FF              RST     0X38                
7E51: FF              RST     0X38                
7E52: FF              RST     0X38                
7E53: FF              RST     0X38                
7E54: FF              RST     0X38                
7E55: FF              RST     0X38                
7E56: FF              RST     0X38                
7E57: FF              RST     0X38                
7E58: FF              RST     0X38                
7E59: FF              RST     0X38                
7E5A: FF              RST     0X38                
7E5B: FF              RST     0X38                
7E5C: FF              RST     0X38                
7E5D: FF              RST     0X38                
7E5E: FF              RST     0X38                
7E5F: FF              RST     0X38                
7E60: FF              RST     0X38                
7E61: FF              RST     0X38                
7E62: FF              RST     0X38                
7E63: FF              RST     0X38                
7E64: FF              RST     0X38                
7E65: FF              RST     0X38                
7E66: FF              RST     0X38                
7E67: FF              RST     0X38                
7E68: FF              RST     0X38                
7E69: FF              RST     0X38                
7E6A: FF              RST     0X38                
7E6B: FF              RST     0X38                
7E6C: FF              RST     0X38                
7E6D: FF              RST     0X38                
7E6E: FF              RST     0X38                
7E6F: FF              RST     0X38                
7E70: FF              RST     0X38                
7E71: FF              RST     0X38                
7E72: FF              RST     0X38                
7E73: FF              RST     0X38                
7E74: FF              RST     0X38                
7E75: FF              RST     0X38                
7E76: FF              RST     0X38                
7E77: FF              RST     0X38                
7E78: FF              RST     0X38                
7E79: FF              RST     0X38                
7E7A: FF              RST     0X38                
7E7B: FF              RST     0X38                
7E7C: FF              RST     0X38                
7E7D: FF              RST     0X38                
7E7E: FF              RST     0X38                
7E7F: FF              RST     0X38                
7E80: FF              RST     0X38                
7E81: FF              RST     0X38                
7E82: FF              RST     0X38                
7E83: FF              RST     0X38                
7E84: FF              RST     0X38                
7E85: FF              RST     0X38                
7E86: FF              RST     0X38                
7E87: FF              RST     0X38                
7E88: FF              RST     0X38                
7E89: FF              RST     0X38                
7E8A: FF              RST     0X38                
7E8B: FF              RST     0X38                
7E8C: FF              RST     0X38                
7E8D: FF              RST     0X38                
7E8E: FF              RST     0X38                
7E8F: FF              RST     0X38                
7E90: FF              RST     0X38                
7E91: FF              RST     0X38                
7E92: FF              RST     0X38                
7E93: FF              RST     0X38                
7E94: FF              RST     0X38                
7E95: FF              RST     0X38                
7E96: FF              RST     0X38                
7E97: FF              RST     0X38                
7E98: FF              RST     0X38                
7E99: FF              RST     0X38                
7E9A: FF              RST     0X38                
7E9B: FF              RST     0X38                
7E9C: FF              RST     0X38                
7E9D: FF              RST     0X38                
7E9E: FF              RST     0X38                
7E9F: FF              RST     0X38                
7EA0: FF              RST     0X38                
7EA1: FF              RST     0X38                
7EA2: FF              RST     0X38                
7EA3: FF              RST     0X38                
7EA4: FF              RST     0X38                
7EA5: FF              RST     0X38                
7EA6: FF              RST     0X38                
7EA7: FF              RST     0X38                
7EA8: FF              RST     0X38                
7EA9: FF              RST     0X38                
7EAA: FF              RST     0X38                
7EAB: FF              RST     0X38                
7EAC: FF              RST     0X38                
7EAD: FF              RST     0X38                
7EAE: FF              RST     0X38                
7EAF: FF              RST     0X38                
7EB0: FF              RST     0X38                
7EB1: FF              RST     0X38                
7EB2: FF              RST     0X38                
7EB3: FF              RST     0X38                
7EB4: FF              RST     0X38                
7EB5: FF              RST     0X38                
7EB6: FF              RST     0X38                
7EB7: FF              RST     0X38                
7EB8: FF              RST     0X38                
7EB9: FF              RST     0X38                
7EBA: FF              RST     0X38                
7EBB: FF              RST     0X38                
7EBC: FF              RST     0X38                
7EBD: FF              RST     0X38                
7EBE: FF              RST     0X38                
7EBF: FF              RST     0X38                
7EC0: FF              RST     0X38                
7EC1: FF              RST     0X38                
7EC2: FF              RST     0X38                
7EC3: FF              RST     0X38                
7EC4: FF              RST     0X38                
7EC5: FF              RST     0X38                
7EC6: FF              RST     0X38                
7EC7: FF              RST     0X38                
7EC8: FF              RST     0X38                
7EC9: FF              RST     0X38                
7ECA: FF              RST     0X38                
7ECB: FF              RST     0X38                
7ECC: FF              RST     0X38                
7ECD: FF              RST     0X38                
7ECE: FF              RST     0X38                
7ECF: FF              RST     0X38                
7ED0: FF              RST     0X38                
7ED1: FF              RST     0X38                
7ED2: FF              RST     0X38                
7ED3: FF              RST     0X38                
7ED4: FF              RST     0X38                
7ED5: FF              RST     0X38                
7ED6: FF              RST     0X38                
7ED7: FF              RST     0X38                
7ED8: FF              RST     0X38                
7ED9: FF              RST     0X38                
7EDA: FF              RST     0X38                
7EDB: FF              RST     0X38                
7EDC: FF              RST     0X38                
7EDD: FF              RST     0X38                
7EDE: FF              RST     0X38                
7EDF: FF              RST     0X38                
7EE0: FF              RST     0X38                
7EE1: FF              RST     0X38                
7EE2: FF              RST     0X38                
7EE3: FF              RST     0X38                
7EE4: FF              RST     0X38                
7EE5: FF              RST     0X38                
7EE6: FF              RST     0X38                
7EE7: FF              RST     0X38                
7EE8: FF              RST     0X38                
7EE9: FF              RST     0X38                
7EEA: FF              RST     0X38                
7EEB: FF              RST     0X38                
7EEC: FF              RST     0X38                
7EED: FF              RST     0X38                
7EEE: FF              RST     0X38                
7EEF: FF              RST     0X38                
7EF0: FF              RST     0X38                
7EF1: FF              RST     0X38                
7EF2: FF              RST     0X38                
7EF3: FF              RST     0X38                
7EF4: FF              RST     0X38                
7EF5: FF              RST     0X38                
7EF6: FF              RST     0X38                
7EF7: FF              RST     0X38                
7EF8: FF              RST     0X38                
7EF9: FF              RST     0X38                
7EFA: FF              RST     0X38                
7EFB: FF              RST     0X38                
7EFC: FF              RST     0X38                
7EFD: FF              RST     0X38                
7EFE: FF              RST     0X38                
7EFF: FF              RST     0X38                
7F00: FF              RST     0X38                
7F01: FF              RST     0X38                
7F02: FF              RST     0X38                
7F03: FF              RST     0X38                
7F04: FF              RST     0X38                
7F05: FF              RST     0X38                
7F06: FF              RST     0X38                
7F07: FF              RST     0X38                
7F08: FF              RST     0X38                
7F09: FF              RST     0X38                
7F0A: FF              RST     0X38                
7F0B: FF              RST     0X38                
7F0C: FF              RST     0X38                
7F0D: FF              RST     0X38                
7F0E: FF              RST     0X38                
7F0F: FF              RST     0X38                
7F10: FF              RST     0X38                
7F11: FF              RST     0X38                
7F12: FF              RST     0X38                
7F13: FF              RST     0X38                
7F14: FF              RST     0X38                
7F15: FF              RST     0X38                
7F16: FF              RST     0X38                
7F17: FF              RST     0X38                
7F18: FF              RST     0X38                
7F19: FF              RST     0X38                
7F1A: FF              RST     0X38                
7F1B: FF              RST     0X38                
7F1C: FF              RST     0X38                
7F1D: FF              RST     0X38                
7F1E: FF              RST     0X38                
7F1F: FF              RST     0X38                
7F20: FF              RST     0X38                
7F21: FF              RST     0X38                
7F22: FF              RST     0X38                
7F23: FF              RST     0X38                
7F24: FF              RST     0X38                
7F25: FF              RST     0X38                
7F26: FF              RST     0X38                
7F27: FF              RST     0X38                
7F28: FF              RST     0X38                
7F29: FF              RST     0X38                
7F2A: FF              RST     0X38                
7F2B: FF              RST     0X38                
7F2C: FF              RST     0X38                
7F2D: FF              RST     0X38                
7F2E: FF              RST     0X38                
7F2F: FF              RST     0X38                
7F30: FF              RST     0X38                
7F31: FF              RST     0X38                
7F32: FF              RST     0X38                
7F33: FF              RST     0X38                
7F34: FF              RST     0X38                
7F35: FF              RST     0X38                
7F36: FF              RST     0X38                
7F37: FF              RST     0X38                
7F38: FF              RST     0X38                
7F39: FF              RST     0X38                
7F3A: FF              RST     0X38                
7F3B: FF              RST     0X38                
7F3C: FF              RST     0X38                
7F3D: FF              RST     0X38                
7F3E: FF              RST     0X38                
7F3F: FF              RST     0X38                
7F40: FF              RST     0X38                
7F41: FF              RST     0X38                
7F42: FF              RST     0X38                
7F43: FF              RST     0X38                
7F44: FF              RST     0X38                
7F45: FF              RST     0X38                
7F46: FF              RST     0X38                
7F47: FF              RST     0X38                
7F48: FF              RST     0X38                
7F49: FF              RST     0X38                
7F4A: FF              RST     0X38                
7F4B: FF              RST     0X38                
7F4C: FF              RST     0X38                
7F4D: FF              RST     0X38                
7F4E: FF              RST     0X38                
7F4F: FF              RST     0X38                
7F50: FF              RST     0X38                
7F51: FF              RST     0X38                
7F52: FF              RST     0X38                
7F53: FF              RST     0X38                
7F54: FF              RST     0X38                
7F55: FF              RST     0X38                
7F56: FF              RST     0X38                
7F57: FF              RST     0X38                
7F58: FF              RST     0X38                
7F59: FF              RST     0X38                
7F5A: FF              RST     0X38                
7F5B: FF              RST     0X38                
7F5C: FF              RST     0X38                
7F5D: FF              RST     0X38                
7F5E: FF              RST     0X38                
7F5F: FF              RST     0X38                
7F60: FF              RST     0X38                
7F61: FF              RST     0X38                
7F62: FF              RST     0X38                
7F63: FF              RST     0X38                
7F64: FF              RST     0X38                
7F65: FF              RST     0X38                
7F66: FF              RST     0X38                
7F67: FF              RST     0X38                
7F68: FF              RST     0X38                
7F69: FF              RST     0X38                
7F6A: FF              RST     0X38                
7F6B: FF              RST     0X38                
7F6C: FF              RST     0X38                
7F6D: FF              RST     0X38                
7F6E: FF              RST     0X38                
7F6F: FF              RST     0X38                
7F70: FF              RST     0X38                
7F71: FF              RST     0X38                
7F72: FF              RST     0X38                
7F73: FF              RST     0X38                
7F74: FF              RST     0X38                
7F75: FF              RST     0X38                
7F76: FF              RST     0X38                
7F77: FF              RST     0X38                
7F78: FF              RST     0X38                
7F79: FF              RST     0X38                
7F7A: FF              RST     0X38                
7F7B: FF              RST     0X38                
7F7C: FF              RST     0X38                
7F7D: FF              RST     0X38                
7F7E: FF              RST     0X38                
7F7F: FF              RST     0X38                
7F80: FF              RST     0X38                
7F81: FF              RST     0X38                
7F82: FF              RST     0X38                
7F83: FF              RST     0X38                
7F84: FF              RST     0X38                
7F85: FF              RST     0X38                
7F86: FF              RST     0X38                
7F87: FF              RST     0X38                
7F88: FF              RST     0X38                
7F89: FF              RST     0X38                
7F8A: FF              RST     0X38                
7F8B: FF              RST     0X38                
7F8C: FF              RST     0X38                
7F8D: FF              RST     0X38                
7F8E: FF              RST     0X38                
7F8F: FF              RST     0X38                
7F90: FF              RST     0X38                
7F91: FF              RST     0X38                
7F92: FF              RST     0X38                
7F93: FF              RST     0X38                
7F94: FF              RST     0X38                
7F95: FF              RST     0X38                
7F96: FF              RST     0X38                
7F97: FF              RST     0X38                
7F98: FF              RST     0X38                
7F99: FF              RST     0X38                
7F9A: FF              RST     0X38                
7F9B: FF              RST     0X38                
7F9C: FF              RST     0X38                
7F9D: FF              RST     0X38                
7F9E: FF              RST     0X38                
7F9F: FF              RST     0X38                
7FA0: FF              RST     0X38                
7FA1: FF              RST     0X38                
7FA2: FF              RST     0X38                
7FA3: FF              RST     0X38                
7FA4: FF              RST     0X38                
7FA5: FF              RST     0X38                
7FA6: FF              RST     0X38                
7FA7: FF              RST     0X38                
7FA8: FF              RST     0X38                
7FA9: FF              RST     0X38                
7FAA: FF              RST     0X38                
7FAB: FF              RST     0X38                
7FAC: FF              RST     0X38                
7FAD: FF              RST     0X38                
7FAE: FF              RST     0X38                
7FAF: FF              RST     0X38                
7FB0: FF              RST     0X38                
7FB1: FF              RST     0X38                
7FB2: FF              RST     0X38                
7FB3: FF              RST     0X38                
7FB4: FF              RST     0X38                
7FB5: FF              RST     0X38                
7FB6: FF              RST     0X38                
7FB7: FF              RST     0X38                
7FB8: FF              RST     0X38                
7FB9: FF              RST     0X38                
7FBA: FF              RST     0X38                
7FBB: FF              RST     0X38                
7FBC: FF              RST     0X38                
7FBD: FF              RST     0X38                
7FBE: FF              RST     0X38                
7FBF: FF              RST     0X38                
7FC0: FF              RST     0X38                
7FC1: FF              RST     0X38                
7FC2: FF              RST     0X38                
7FC3: FF              RST     0X38                
7FC4: FF              RST     0X38                
7FC5: FF              RST     0X38                
7FC6: FF              RST     0X38                
7FC7: FF              RST     0X38                
7FC8: FF              RST     0X38                
7FC9: FF              RST     0X38                
7FCA: FF              RST     0X38                
7FCB: FF              RST     0X38                
7FCC: FF              RST     0X38                
7FCD: FF              RST     0X38                
7FCE: FF              RST     0X38                
7FCF: FF              RST     0X38                
7FD0: FF              RST     0X38                
7FD1: FF              RST     0X38                
7FD2: FF              RST     0X38                
7FD3: FF              RST     0X38                
7FD4: FF              RST     0X38                
7FD5: FF              RST     0X38                
7FD6: FF              RST     0X38                
7FD7: FF              RST     0X38                
7FD8: FF              RST     0X38                
7FD9: FF              RST     0X38                
7FDA: FF              RST     0X38                
7FDB: FF              RST     0X38                
7FDC: FF              RST     0X38                
7FDD: FF              RST     0X38                
7FDE: FF              RST     0X38                
7FDF: FF              RST     0X38                
7FE0: FF              RST     0X38                
7FE1: FF              RST     0X38                
7FE2: FF              RST     0X38                
7FE3: FF              RST     0X38                
7FE4: FF              RST     0X38                
7FE5: FF              RST     0X38                
7FE6: FF              RST     0X38                
7FE7: FF              RST     0X38                
7FE8: FF              RST     0X38                
7FE9: FF              RST     0X38                
7FEA: FF              RST     0X38                
7FEB: FF              RST     0X38                
7FEC: FF              RST     0X38                
7FED: FF              RST     0X38                
7FEE: FF              RST     0X38                
7FEF: FF              RST     0X38                
7FF0: FF              RST     0X38                
7FF1: FF              RST     0X38                
7FF2: FF              RST     0X38                
7FF3: FF              RST     0X38                
7FF4: FF              RST     0X38                
7FF5: FF              RST     0X38                
7FF6: FF              RST     0X38                
7FF7: FF              RST     0X38                
7FF8: FF              RST     0X38                
7FF9: FF              RST     0X38                
7FFA: FF              RST     0X38                
7FFB: FF              RST     0X38                
7FFC: FF              RST     0X38                
7FFD: FF              RST     0X38                
7FFE: FF              RST     0X38                
7FFF: FF              RST     0X38                
```

