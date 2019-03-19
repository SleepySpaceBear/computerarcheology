![Bank 17](GBZelda.jpg)

# Bank 17

>>> cpu Z80GB

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

```
4000: 18 05      JR      $4007           
4002: 37         SCF                     
4003: 20 36      JR      NZ,$403B        
4005: 0E 1E      LD      C,$1E           
4007: 2B         DEC     HL              
4008: 25         DEC     H               
4009: 14         INC     D               
400A: 1F         RRA                     
400B: 12         LD      (DE),A          
400C: 15         DEC     D               
400D: 2C         INC     L               
400E: 31 3F 0C   LD      SP,$0C3F        
4011: 30 01      JR      NC,$4014        
4013: 33         INC     SP              
4014: 04         INC     B               
4015: 27         DAA                     
4016: 08 1D 38   LD      ($381D),SP      
4019: 17         RLA                     
401A: 3E 28      LD      A,$28           
401C: 11 00 3A   LD      DE,$3A00        
401F: 3D         DEC     A               
4020: 2A         LD      A,(HLI)         
4021: 0B         DEC     BC              
4022: 1B         DEC     DE              
4023: 0A         LD      A,(BC)          
4024: 34         INC     (HL)            
4025: 07         RLCA                    
4026: 22         LD      (HLI),A         
4027: 0F         RRCA                    
4028: 1C         INC     E               
4029: 23         INC     HL              
402A: 2F         CPL                     
402B: 3B         DEC     SP              
402C: 2D         DEC     L               
402D: 16 3C      LD      D,$3C           
402F: 32         LD      (HLD),A         
4030: 10 29      STOP    $29             
4032: 02         LD      (BC),A          
4033: 2E 0D      LD      L,$0D           
4035: 19         ADD     HL,DE           
4036: 09         ADD     HL,BC           
4037: 26 24      LD      H,$24           
4039: 06 13      LD      B,$13           
403B: 21 1A 03   LD      HL,$031A        
403E: 39         ADD     HL,SP           
403F: 35         DEC     (HL)            
4040: 7F         LD      A,A             
4041: BF         CP      A               
4042: DF         RST     0X18            
4043: EF         RST     0X28            
4044: F7         RST     0X30            
4045: FB         EI                      
4046: FD         ???                     
4047: FE 50      CP      $50             
4049: 91         SUB     C               
404A: 60         LD      H,B             
404B: 90         SUB     B               
404C: 70         LD      (HL),B          
404D: 90         SUB     B               
404E: 80         ADD     A,B             
404F: 90         SUB     B               
4050: 90         SUB     B               
4051: 90         SUB     B               
4052: A0         AND     B               
4053: 90         SUB     B               
4054: F0 91      LD      A,($91)         
4056: 60         LD      H,B             
4057: 91         SUB     C               
4058: 70         LD      (HL),B          
4059: 91         SUB     C               
405A: 80         ADD     A,B             
405B: 91         SUB     C               
405C: 90         SUB     B               
405D: 91         SUB     C               
405E: A0         AND     B               
405F: 91         SUB     C               
4060: FA 0B D0   LD      A,($D00B)       
4063: 5F         LD      E,A             
4064: 16 00      LD      D,$00           
4066: 21 00 40   LD      HL,$4000        
4069: 19         ADD     HL,DE           
406A: 7E         LD      A,(HL)          
406B: 1F         RRA                     
406C: 1F         RRA                     
406D: E6 0E      AND     $0E             
406F: 47         LD      B,A             
4070: 7E         LD      A,(HL)          
4071: E6 07      AND     $07             
4073: 5F         LD      E,A             
4074: 21 40 40   LD      HL,$4040        
4077: 19         ADD     HL,DE           
4078: 4E         LD      C,(HL)          
4079: AF         XOR     A               
407A: 57         LD      D,A             
407B: E0 D9      LDFF00  ($D9),A         
407D: CB 27      SET     1,E             
407F: 5F         LD      E,A             
4080: 21 48 40   LD      HL,$4048        
4083: 19         ADD     HL,DE           
4084: 2A         LD      A,(HLI)         
4085: 66         LD      H,(HL)          
4086: 80         ADD     A,B             
4087: 6F         LD      L,A             
4088: 7E         LD      A,(HL)          
4089: A1         AND     C               
408A: 22         LD      (HLI),A         
408B: 7E         LD      A,(HL)          
408C: A1         AND     C               
408D: 77         LD      (HL),A          
408E: F0 D9      LD      A,($D9)         
4090: 3C         INC     A               
4091: FE 0C      CP      $0C             
4093: 20 E6      JR      NZ,$407B        
4095: AF         XOR     A               
4096: E0 A5      LDFF00  ($A5),A         
4098: C9         RET                     
4099: 20 20      JR      NZ,$40BB        
409B: 20 20      JR      NZ,$40BD        
409D: 20 44      JR      NZ,$40E3        
409F: 49         LD      C,C             
40A0: 52         LD      D,D             
40A1: 45         LD      B,L             
40A2: 43         LD      B,E             
40A3: 54         LD      D,H             
40A4: 4F         LD      C,A             
40A5: 52         LD      D,D             
40A6: 20 20      JR      NZ,$40C8        
40A8: 20 20      JR      NZ,$40CA        
40AA: 20 20      JR      NZ,$40CC        
40AC: 44         LD      B,H             
40AD: 55         LD      D,L             
40AE: 4E         LD      C,(HL)          
40AF: 47         LD      B,A             
40B0: 45         LD      B,L             
40B1: 4F         LD      C,A             
40B2: 4E         LD      C,(HL)          
40B3: 20 44      JR      NZ,$40F9        
40B5: 45         LD      B,L             
40B6: 53         LD      D,E             
40B7: 49         LD      C,C             
40B8: 47         LD      B,A             
40B9: 4E         LD      C,(HL)          
40BA: 45         LD      B,L             
40BB: 52         LD      D,D             
40BC: 20 20      JR      NZ,$40DE        
40BE: 20 53      JR      NZ,$4113        
40C0: 43         LD      B,E             
40C1: 52         LD      D,D             
40C2: 49         LD      C,C             
40C3: 50         LD      D,B             
40C4: 54         LD      D,H             
40C5: 20 57      JR      NZ,$411E        
40C7: 52         LD      D,D             
40C8: 49         LD      C,C             
40C9: 54         LD      D,H             
40CA: 45         LD      B,L             
40CB: 52         LD      D,D             
40CC: 20 20      JR      NZ,$40EE        
40CE: 20 20      JR      NZ,$40F0        
40D0: 20 20      JR      NZ,$40F2        
40D2: 20 50      JR      NZ,$4124        
40D4: 52         LD      D,D             
40D5: 4F         LD      C,A             
40D6: 47         LD      B,A             
40D7: 52         LD      D,D             
40D8: 41         LD      B,C             
40D9: 4D         LD      C,L             
40DA: 4D         LD      C,L             
40DB: 45         LD      B,L             
40DC: 52         LD      D,D             
40DD: 20 20      JR      NZ,$40FF        
40DF: 20 20      JR      NZ,$4101        
40E1: 43         LD      B,E             
40E2: 48         LD      C,B             
40E3: 41         LD      B,C             
40E4: 52         LD      D,D             
40E5: 41         LD      B,C             
40E6: 43         LD      B,E             
40E7: 54         LD      D,H             
40E8: 45         LD      B,L             
40E9: 52         LD      D,D             
40EA: 20 44      JR      NZ,$4130        
40EC: 45         LD      B,L             
40ED: 53         LD      D,E             
40EE: 49         LD      C,C             
40EF: 47         LD      B,A             
40F0: 4E         LD      C,(HL)          
40F1: 45         LD      B,L             
40F2: 52         LD      D,D             
40F3: 20 20      JR      NZ,$4115        
40F5: 53         LD      D,E             
40F6: 4F         LD      C,A             
40F7: 55         LD      D,L             
40F8: 4E         LD      C,(HL)          
40F9: 44         LD      B,H             
40FA: 20 43      JR      NZ,$413F        
40FC: 4F         LD      C,A             
40FD: 4D         LD      C,L             
40FE: 50         LD      D,B             
40FF: 4F         LD      C,A             
4100: 53         LD      D,E             
4101: 45         LD      B,L             
4102: 52         LD      D,D             
4103: 20 20      JR      NZ,$4125        
4105: 20 20      JR      NZ,$4127        
4107: 20 49      JR      NZ,$4152        
4109: 4C         LD      C,H             
410A: 4C         LD      C,H             
410B: 55         LD      D,L             
410C: 53         LD      D,E             
410D: 54         LD      D,H             
410E: 52         LD      D,D             
410F: 41         LD      B,C             
4110: 54         LD      D,H             
4111: 4F         LD      C,A             
4112: 52         LD      D,D             
4113: 20 20      JR      NZ,$4135        
4115: 20 20      JR      NZ,$4137        
4117: 20 53      JR      NZ,$416C        
4119: 50         LD      D,B             
411A: 45         LD      B,L             
411B: 43         LD      B,E             
411C: 49         LD      C,C             
411D: 41         LD      B,C             
411E: 4C         LD      C,H             
411F: 20 54      JR      NZ,$4175        
4121: 48         LD      C,B             
4122: 41         LD      B,C             
4123: 4E         LD      C,(HL)          
4124: 4B         LD      C,E             
4125: 53         LD      D,E             
4126: 20 54      JR      NZ,$417C        
4128: 4F         LD      C,A             
4129: 20 20      JR      NZ,$414B        
412B: 20 20      JR      NZ,$414D        
412D: 20 50      JR      NZ,$417F        
412F: 52         LD      D,D             
4130: 4F         LD      C,A             
4131: 44         LD      B,H             
4132: 55         LD      D,L             
4133: 43         LD      B,E             
4134: 45         LD      B,L             
4135: 52         LD      D,D             
4136: 20 20      JR      NZ,$4158        
4138: 20 20      JR      NZ,$415A        
413A: 20 45      JR      NZ,$4181        
413C: 58         LD      E,B             
413D: 45         LD      B,L             
413E: 43         LD      B,E             
413F: 55         LD      D,L             
4140: 54         LD      D,H             
4141: 49         LD      C,C             
4142: 56         LD      D,(HL)          
4143: 45         LD      B,L             
4144: 20 50      JR      NZ,$4196        
4146: 52         LD      D,D             
4147: 4F         LD      C,A             
4148: 44         LD      B,H             
4149: 55         LD      D,L             
414A: 43         LD      B,E             
414B: 45         LD      B,L             
414C: 52         LD      D,D             
414D: 20 20      JR      NZ,$416F        
414F: 45         LD      B,L             
4150: 4E         LD      C,(HL)          
4151: 47         LD      B,A             
4152: 4C         LD      C,H             
4153: 49         LD      C,C             
4154: 53         LD      D,E             
4155: 48         LD      C,B             
4156: 20 53      JR      NZ,$41AB        
4158: 43         LD      B,E             
4159: 52         LD      D,D             
415A: 49         LD      C,C             
415B: 50         LD      D,B             
415C: 54         LD      D,H             
415D: 20 20      JR      NZ,$417F        
415F: 20 20      JR      NZ,$4181        
4161: 20 20      JR      NZ,$4183        
4163: 20 20      JR      NZ,$4185        
4165: 20 20      JR      NZ,$4187        
4167: 20 20      JR      NZ,$4189        
4169: 20 20      JR      NZ,$418B        
416B: 20 20      JR      NZ,$418D        
416D: 20 20      JR      NZ,$418F        
416F: 20 20      JR      NZ,$4191        
4171: 20 20      JR      NZ,$4193        
4173: 54         LD      D,H             
4174: 41         LD      B,C             
4175: 4B         LD      C,E             
4176: 41         LD      B,C             
4177: 53         LD      D,E             
4178: 48         LD      C,B             
4179: 49         LD      C,C             
417A: 20 54      JR      NZ,$41D0        
417C: 45         LD      B,L             
417D: 5A         LD      E,D             
417E: 55         LD      D,L             
417F: 4B         LD      C,E             
4180: 41         LD      B,C             
4181: 20 20      JR      NZ,$41A3        
4183: 20 59      JR      NZ,$41DE        
4185: 41         LD      B,C             
4186: 53         LD      D,E             
4187: 55         LD      D,L             
4188: 48         LD      C,B             
4189: 49         LD      C,C             
418A: 53         LD      D,E             
418B: 41         LD      B,C             
418C: 20 59      JR      NZ,$41E7        
418E: 41         LD      B,C             
418F: 4D         LD      C,L             
4190: 41         LD      B,C             
4191: 4D         LD      C,L             
4192: 55         LD      D,L             
4193: 52         LD      D,D             
4194: 41         LD      B,C             
4195: 20 20      JR      NZ,$41B7        
4197: 4B         LD      C,E             
4198: 45         LD      B,L             
4199: 4E         LD      C,(HL)          
419A: 53         LD      D,E             
419B: 55         LD      D,L             
419C: 4B         LD      C,E             
419D: 45         LD      B,L             
419E: 20 54      JR      NZ,$41F4        
41A0: 41         LD      B,C             
41A1: 4E         LD      C,(HL)          
41A2: 41         LD      B,C             
41A3: 42         LD      B,D             
41A4: 45         LD      B,L             
41A5: 20 20      JR      NZ,$41C7        
41A7: 20 59      JR      NZ,$4202        
41A9: 4F         LD      C,A             
41AA: 53         LD      D,E             
41AB: 48         LD      C,B             
41AC: 49         LD      C,C             
41AD: 41         LD      B,C             
41AE: 4B         LD      C,E             
41AF: 49         LD      C,C             
41B0: 20 4B      JR      NZ,$41FD        
41B2: 4F         LD      C,A             
41B3: 49         LD      C,C             
41B4: 5A         LD      E,D             
41B5: 55         LD      D,L             
41B6: 4D         LD      C,L             
41B7: 49         LD      C,C             
41B8: 20 20      JR      NZ,$41DA        
41BA: 20 4B      JR      NZ,$4207        
41BC: 41         LD      B,C             
41BD: 5A         LD      E,D             
41BE: 55         LD      D,L             
41BF: 41         LD      B,C             
41C0: 4B         LD      C,E             
41C1: 49         LD      C,C             
41C2: 20 4D      JR      NZ,$4211        
41C4: 4F         LD      C,A             
41C5: 52         LD      D,D             
41C6: 49         LD      C,C             
41C7: 54         LD      D,H             
41C8: 41         LD      B,C             
41C9: 20 20      JR      NZ,$41EB        
41CB: 54         LD      D,H             
41CC: 41         LD      B,C             
41CD: 4B         LD      C,E             
41CE: 41         LD      B,C             
41CF: 4D         LD      C,L             
41D0: 49         LD      C,C             
41D1: 54         LD      D,H             
41D2: 53         LD      D,E             
41D3: 55         LD      D,L             
41D4: 20 4B      JR      NZ,$4221        
41D6: 55         LD      D,L             
41D7: 5A         LD      E,D             
41D8: 55         LD      D,L             
41D9: 48         LD      C,B             
41DA: 41         LD      B,C             
41DB: 52         LD      D,D             
41DC: 41         LD      B,C             
41DD: 20 20      JR      NZ,$41FF        
41DF: 4D         LD      C,L             
41E0: 41         LD      B,C             
41E1: 53         LD      D,E             
41E2: 41         LD      B,C             
41E3: 4E         LD      C,(HL)          
41E4: 41         LD      B,C             
41E5: 4F         LD      C,A             
41E6: 20 41      JR      NZ,$4229        
41E8: 52         LD      D,D             
41E9: 49         LD      C,C             
41EA: 4D         LD      C,L             
41EB: 4F         LD      C,A             
41EC: 54         LD      D,H             
41ED: 4F         LD      C,A             
41EE: 20 20      JR      NZ,$4210        
41F0: 20 53      JR      NZ,$4245        
41F2: 48         LD      C,B             
41F3: 49         LD      C,C             
41F4: 47         LD      B,A             
41F5: 45         LD      B,L             
41F6: 46         LD      B,(HL)          
41F7: 55         LD      D,L             
41F8: 4D         LD      C,L             
41F9: 49         LD      C,C             
41FA: 20 48      JR      NZ,$4244        
41FC: 49         LD      C,C             
41FD: 4E         LD      C,(HL)          
41FE: 4F         LD      C,A             
41FF: 20 20      JR      NZ,$4221        
4201: 20 20      JR      NZ,$4223        
4203: 20 4B      JR      NZ,$4250        
4205: 41         LD      B,C             
4206: 5A         LD      E,D             
4207: 55         LD      D,L             
4208: 4D         LD      C,L             
4209: 49         LD      C,C             
420A: 20 54      JR      NZ,$4260        
420C: 4F         LD      C,A             
420D: 54         LD      D,H             
420E: 41         LD      B,C             
420F: 4B         LD      C,E             
4210: 41         LD      B,C             
4211: 20 20      JR      NZ,$4233        
4213: 20 20      JR      NZ,$4235        
4215: 20 4D      JR      NZ,$4264        
4217: 49         LD      C,C             
4218: 4E         LD      C,(HL)          
4219: 41         LD      B,C             
421A: 4B         LD      C,E             
421B: 4F         LD      C,A             
421C: 20 48      JR      NZ,$4266        
421E: 41         LD      B,C             
421F: 4D         LD      C,L             
4220: 41         LD      B,C             
4221: 4E         LD      C,(HL)          
4222: 4F         LD      C,A             
4223: 20 20      JR      NZ,$4245        
4225: 20 20      JR      NZ,$4247        
4227: 4B         LD      C,E             
4228: 4F         LD      C,A             
4229: 5A         LD      E,D             
422A: 55         LD      D,L             
422B: 45         LD      B,L             
422C: 20 49      JR      NZ,$4277        
422E: 53         LD      D,E             
422F: 48         LD      C,B             
4230: 49         LD      C,C             
4231: 4B         LD      C,E             
4232: 41         LD      B,C             
4233: 57         LD      D,A             
4234: 41         LD      B,C             
4235: 20 20      JR      NZ,$4257        
4237: 20 20      JR      NZ,$4259        
4239: 59         LD      E,C             
423A: 4F         LD      C,A             
423B: 55         LD      D,L             
423C: 49         LD      C,C             
423D: 43         LD      B,E             
423E: 48         LD      C,B             
423F: 49         LD      C,C             
4240: 20 4B      JR      NZ,$428D        
4242: 4F         LD      C,A             
4243: 54         LD      D,H             
4244: 41         LD      B,C             
4245: 42         LD      B,D             
4246: 45         LD      B,L             
4247: 20 20      JR      NZ,$4269        
4249: 20 54      JR      NZ,$429F        
424B: 4F         LD      C,A             
424C: 53         LD      D,E             
424D: 48         LD      C,B             
424E: 49         LD      C,C             
424F: 48         LD      C,B             
4250: 49         LD      C,C             
4251: 4B         LD      C,E             
4252: 4F         LD      C,A             
4253: 20 4E      JR      NZ,$42A3        
4255: 41         LD      B,C             
4256: 4B         LD      C,E             
4257: 41         LD      B,C             
4258: 47         LD      B,A             
4259: 4F         LD      C,A             
425A: 20 20      JR      NZ,$427C        
425C: 20 20      JR      NZ,$427E        
425E: 20 4B      JR      NZ,$42AB        
4260: 45         LD      B,L             
4261: 49         LD      C,C             
4262: 5A         LD      E,D             
4263: 4F         LD      C,A             
4264: 20 4B      JR      NZ,$42B1        
4266: 41         LD      B,C             
4267: 54         LD      D,H             
4268: 4F         LD      C,A             
4269: 20 20      JR      NZ,$428B        
426B: 20 20      JR      NZ,$428D        
426D: 20 20      JR      NZ,$428F        
426F: 20 20      JR      NZ,$4291        
4271: 4B         LD      C,E             
4272: 4F         LD      C,A             
4273: 4A         LD      C,D             
4274: 49         LD      C,C             
4275: 20 4B      JR      NZ,$42C2        
4277: 4F         LD      C,A             
4278: 4E         LD      C,(HL)          
4279: 44         LD      B,H             
427A: 4F         LD      C,A             
427B: 20 20      JR      NZ,$429D        
427D: 20 20      JR      NZ,$429F        
427F: 20 20      JR      NZ,$42A1        
4281: 54         LD      D,H             
4282: 4F         LD      C,A             
4283: 4D         LD      C,L             
4284: 4F         LD      C,A             
4285: 41         LD      B,C             
4286: 4B         LD      C,E             
4287: 49         LD      C,C             
4288: 20 4B      JR      NZ,$42D5        
428A: 55         LD      D,L             
428B: 52         LD      D,D             
428C: 4F         LD      C,A             
428D: 55         LD      D,L             
428E: 4D         LD      C,L             
428F: 45         LD      B,L             
4290: 20 20      JR      NZ,$42B2        
4292: 53         LD      D,E             
4293: 48         LD      C,B             
4294: 49         LD      C,C             
4295: 47         LD      B,A             
4296: 45         LD      B,L             
4297: 52         LD      D,D             
4298: 55         LD      D,L             
4299: 20 4D      JR      NZ,$42E8        
429B: 49         LD      C,C             
429C: 59         LD      E,C             
429D: 41         LD      B,C             
429E: 4D         LD      C,L             
429F: 4F         LD      C,A             
42A0: 54         LD      D,H             
42A1: 4F         LD      C,A             
42A2: 20 20      JR      NZ,$42C4        
42A4: 48         LD      C,B             
42A5: 49         LD      C,C             
42A6: 52         LD      D,D             
42A7: 4F         LD      C,A             
42A8: 53         LD      D,E             
42A9: 48         LD      C,B             
42AA: 49         LD      C,C             
42AB: 20 59      JR      NZ,$4306        
42AD: 41         LD      B,C             
42AE: 4D         LD      C,L             
42AF: 41         LD      B,C             
42B0: 55         LD      D,L             
42B1: 43         LD      B,E             
42B2: 48         LD      C,B             
42B3: 49         LD      C,C             
42B4: 20 20      JR      NZ,$42D6        
42B6: 20 20      JR      NZ,$42D8        
42B8: 20 20      JR      NZ,$42DA        
42BA: 44         LD      B,H             
42BB: 41         LD      B,C             
42BC: 4E         LD      C,(HL)          
42BD: 20 4F      JR      NZ,$430E        
42BF: 57         LD      D,A             
42C0: 53         LD      D,E             
42C1: 45         LD      B,L             
42C2: 4E         LD      C,(HL)          
42C3: 20 20      JR      NZ,$42E5        
42C5: 20 20      JR      NZ,$42E7        
42C7: 20 4D      JR      NZ,$4316        
42C9: 41         LD      B,C             
42CA: 53         LD      D,E             
42CB: 41         LD      B,C             
42CC: 49         LD      C,C             
42CD: 43         LD      B,E             
42CE: 48         LD      C,B             
42CF: 49         LD      C,C             
42D0: 20 4F      JR      NZ,$4321        
42D2: 4B         LD      C,E             
42D3: 55         LD      D,L             
42D4: 4D         LD      C,L             
42D5: 55         LD      D,L             
42D6: 52         LD      D,D             
42D7: 41         LD      B,C             
42D8: 20 20      JR      NZ,$42FA        
42DA: 20 20      JR      NZ,$42FC        
42DC: 20 4B      JR      NZ,$4329        
42DE: 41         LD      B,C             
42DF: 4E         LD      C,(HL)          
42E0: 41         LD      B,C             
42E1: 45         LD      B,L             
42E2: 20 57      JR      NZ,$433B        
42E4: 41         LD      B,C             
42E5: 44         LD      B,H             
42E6: 41         LD      B,C             
42E7: 20 20      JR      NZ,$4309        
42E9: 20 20      JR      NZ,$430B        
42EB: 54         LD      D,H             
42EC: 48         LD      C,B             
42ED: 45         LD      B,L             
42EE: 20 20      JR      NZ,$4310        
42F0: 45         LD      B,L             
42F1: 4E         LD      C,(HL)          
42F2: 44         LD      B,H             
42F3: 20 20      JR      NZ,$4315        
42F5: 20 20      JR      NZ,$4317        
42F7: 20 20      JR      NZ,$4319        
42F9: 20 20      JR      NZ,$431B        
42FB: 20 20      JR      NZ,$431D        
42FD: FA 09 D0   LD      A,($D009)       
4300: A7         AND     A               
4301: C0         RET     NZ              
4302: CD AE 44   CALL    $44AE           
4305: CD 6D 45   CALL    $456D           
4308: FA 12 D0   LD      A,($D012)       
430B: C7         RST     0X00            
430C: 42         LD      B,D             
430D: 43         LD      B,E             
430E: B1         OR      C               
430F: 43         LD      B,E             
4310: F2         ???                     
4311: 43         LD      B,E             
4312: 18 44      JR      $4358           
4314: 6D         LD      L,L             
4315: 44         LD      B,H             
4316: 93         SUB     E               
4317: 44         LD      B,H             
4318: 00         NOP                     
4319: 01 02 02   LD      BC,$0202        
431C: 03         INC     BC              
431D: 03         INC     BC              
431E: 04         INC     B               
431F: 04         INC     B               
4320: 05         DEC     B               
4321: 05         DEC     B               
4322: 05         DEC     B               
4323: 06 0A      LD      B,$0A           
4325: 07         RLCA                    
4326: 07         RLCA                    
4327: 07         RLCA                    
4328: 07         RLCA                    
4329: 07         RLCA                    
432A: 08 09 0B   LD      ($0B09),SP      
432D: 00         NOP                     
432E: 01 02 03   LD      BC,$0302        
4331: 04         INC     B               
4332: 05         DEC     B               
4333: 06 07      LD      B,$07           
4335: 08 09 0A   LD      ($0A09),SP      
4338: 0B         DEC     BC              
4339: 12         LD      (DE),A          
433A: 0C         INC     C               
433B: 0E 0F      LD      C,$0F           
433D: 13         INC     DE              
433E: 14         INC     D               
433F: 10 11      STOP    $11             
4341: 15         DEC     D               
4342: FA 08 D0   LD      A,($D008)       
4345: A7         AND     A               
4346: C0         RET     NZ              
4347: 0E 00      LD      C,$00           
4349: FA 0A D0   LD      A,($D00A)       
434C: 5F         LD      E,A             
434D: 16 00      LD      D,$00           
434F: 21 18 43   LD      HL,$4318        
4352: 19         ADD     HL,DE           
4353: FA 10 D0   LD      A,($D010)       
4356: BE         CP      (HL)            
4357: 20 01      JR      NZ,$435A        
4359: 0C         INC     C               
435A: 79         LD      A,C             
435B: EA 05 D0   LD      ($D005),A       
435E: 7E         LD      A,(HL)          
435F: EA 10 D0   LD      ($D010),A       
4362: 21 2D 43   LD      HL,$432D        
4365: 19         ADD     HL,DE           
4366: 7E         LD      A,(HL)          
4367: EA 11 D0   LD      ($D011),A       
436A: AF         XOR     A               
436B: EA 00 D0   LD      ($D000),A       
436E: C3 13 44   JP      $4413           
4371: 00         NOP                     
4372: 00         NOP                     
4373: 00         NOP                     
4374: 00         NOP                     
4375: 04         INC     B               
4376: 04         INC     B               
4377: 04         INC     B               
4378: 04         INC     B               
4379: 19         ADD     HL,DE           
437A: 19         ADD     HL,DE           
437B: 19         ADD     HL,DE           
437C: 19         ADD     HL,DE           
437D: 1E 1E      LD      E,$1E           
437F: 1E 1E      LD      E,$1E           
4381: FF         RST     0X38            
4382: FF         RST     0X38            
4383: FF         RST     0X38            
4384: FF         RST     0X38            
4385: AF         XOR     A               
4386: AF         XOR     A               
4387: AF         XOR     A               
4388: AF         XOR     A               
4389: 5A         LD      E,D             
438A: 5A         LD      E,D             
438B: 5A         LD      E,D             
438C: 5A         LD      E,D             
438D: 1E 1E      LD      E,$1E           
438F: 1E 1E      LD      E,$1E           
4391: 1E 1E      LD      E,$1E           
4393: 1E 1E      LD      E,$1E           
4395: 19         ADD     HL,DE           
4396: 19         ADD     HL,DE           
4397: 19         ADD     HL,DE           
4398: 19         ADD     HL,DE           
4399: 04         INC     B               
439A: 04         INC     B               
439B: 04         INC     B               
439C: 04         INC     B               
439D: 00         NOP                     
439E: 00         NOP                     
439F: 00         NOP                     
43A0: 00         NOP                     
43A1: 1E 1E      LD      E,$1E           
43A3: 1E 1E      LD      E,$1E           
43A5: 6F         LD      L,A             
43A6: 6F         LD      L,A             
43A7: 6F         LD      L,A             
43A8: 6F         LD      L,A             
43A9: BF         CP      A               
43AA: BF         CP      A               
43AB: BF         CP      A               
43AC: BF         CP      A               
43AD: FF         RST     0X38            
43AE: FF         RST     0X38            
43AF: FF         RST     0X38            
43B0: FF         RST     0X38            
43B1: F0 E7      LD      A,($E7)         
43B3: E6 07      AND     $07             
43B5: 20 1C      JR      NZ,$43D3        
43B7: FA 00 D0   LD      A,($D000)       
43BA: 3C         INC     A               
43BB: EA 00 D0   LD      ($D000),A       
43BE: FE 0C      CP      $0C             
43C0: 20 11      JR      NZ,$43D3        
43C2: 3E 7C      LD      A,$7C           
43C4: EA 08 D0   LD      ($D008),A       
43C7: CD 13 44   CALL    $4413           
43CA: FA 0A D0   LD      A,($D00A)       
43CD: FE 14      CP      $14             
43CF: 20 02      JR      NZ,$43D3        
43D1: 36 04      LD      (HL),$04        
43D3: FA 00 D0   LD      A,($D000)       
43D6: 5F         LD      E,A             
43D7: F0 E7      LD      A,($E7)         
43D9: E6 03      AND     $03             
43DB: 83         ADD     A,E             
43DC: 5F         LD      E,A             
43DD: 16 00      LD      D,$00           
43DF: 21 71 43   LD      HL,$4371        
43E2: FA 0A D0   LD      A,($D00A)       
43E5: FE 14      CP      $14             
43E7: 20 03      JR      NZ,$43EC        
43E9: 21 81 43   LD      HL,$4381        
43EC: 19         ADD     HL,DE           
43ED: 7E         LD      A,(HL)          
43EE: EA 99 DB   LD      ($DB99),A       
43F1: C9         RET                     
43F2: FA 08 D0   LD      A,($D008)       
43F5: A7         AND     A               
43F6: C0         RET     NZ              
43F7: 0E 00      LD      C,$00           
43F9: FA 0A D0   LD      A,($D00A)       
43FC: 3C         INC     A               
43FD: 5F         LD      E,A             
43FE: 16 00      LD      D,$00           
4400: 21 18 43   LD      HL,$4318        
4403: 19         ADD     HL,DE           
4404: FA 10 D0   LD      A,($D010)       
4407: BE         CP      (HL)            
4408: 20 01      JR      NZ,$440B        
440A: 0C         INC     C               
440B: 79         LD      A,C             
440C: EA 05 D0   LD      ($D005),A       
440F: AF         XOR     A               
4410: EA 00 D0   LD      ($D000),A       
4413: 21 12 D0   LD      HL,$D012        
4416: 34         INC     (HL)            
4417: C9         RET                     
4418: FA 0A D0   LD      A,($D00A)       
441B: E0 E4      LDFF00  ($E4),A         
441D: F0 E7      LD      A,($E7)         
441F: E6 07      AND     $07             
4421: 20 24      JR      NZ,$4447        
4423: FA 00 D0   LD      A,($D000)       
4426: 3C         INC     A               
4427: EA 00 D0   LD      ($D000),A       
442A: FE 0C      CP      $0C             
442C: 20 19      JR      NZ,$4447        
442E: F0 E4      LD      A,($E4)         
4430: FE 13      CP      $13             
4432: 3E 10      LD      A,$10           
4434: 38 02      JR      C,$4438         
4436: 3E 80      LD      A,$80           
4438: EA 08 D0   LD      ($D008),A       
443B: 3E 00      LD      A,$00           
443D: EA 12 D0   LD      ($D012),A       
4440: FA 0A D0   LD      A,($D00A)       
4443: 3C         INC     A               
4444: EA 0A D0   LD      ($D00A),A       
4447: FA 00 D0   LD      A,($D000)       
444A: 5F         LD      E,A             
444B: F0 E7      LD      A,($E7)         
444D: E6 03      AND     $03             
444F: 83         ADD     A,E             
4450: 5F         LD      E,A             
4451: 16 00      LD      D,$00           
4453: 21 91 43   LD      HL,$4391        
4456: 19         ADD     HL,DE           
4457: 7E         LD      A,(HL)          
4458: EA 99 DB   LD      ($DB99),A       
445B: F0 E4      LD      A,($E4)         
445D: FE 13      CP      $13             
445F: 38 0B      JR      C,$446C         
4461: 21 A1 43   LD      HL,$43A1        
4464: 19         ADD     HL,DE           
4465: 7E         LD      A,(HL)          
4466: EA 97 DB   LD      ($DB97),A       
4469: EA 99 DB   LD      ($DB99),A       
446C: C9         RET                     
446D: 3E E8      LD      A,$E8           
446F: CD 01 3C   CALL    $3C01           
4472: 21 00 C2   LD      HL,$C200        
4475: 19         ADD     HL,DE           
4476: 36 E0      LD      (HL),$E0        
4478: 21 10 C2   LD      HL,$C210        
447B: 19         ADD     HL,DE           
447C: 36 10      LD      (HL),$10        
447E: 21 40 C2   LD      HL,$C240        
4481: 19         ADD     HL,DE           
4482: 36 08      LD      (HL),$08        
4484: 21 50 C2   LD      HL,$C250        
4487: 19         ADD     HL,DE           
4488: 36 08      LD      (HL),$08        
448A: 21 B0 C2   LD      HL,$C2B0        
448D: 19         ADD     HL,DE           
448E: 36 10      LD      (HL),$10        
4490: C3 13 44   JP      $4413           
4493: C9         RET                     
4494: 40         LD      B,B             
4495: 00         NOP                     
4496: 41         LD      B,C             
4497: 42         LD      B,D             
4498: 43         LD      B,E             
4499: 00         NOP                     
449A: 44         LD      B,H             
449B: 45         LD      B,L             
449C: 46         LD      B,(HL)          
449D: 00         NOP                     
449E: 47         LD      B,A             
449F: 48         LD      C,B             
44A0: 49         LD      C,C             
44A1: 4A         LD      C,D             
44A2: 4B         LD      C,E             
44A3: 50         LD      D,B             
44A4: 00         NOP                     
44A5: 51         LD      D,C             
44A6: 52         LD      D,D             
44A7: 53         LD      D,E             
44A8: 54         LD      D,H             
44A9: 55         LD      D,L             
44AA: 2F         CPL                     
44AB: 3F         CCF                     
44AC: 00         NOP                     
44AD: 00         NOP                     
44AE: FA 10 D0   LD      A,($D010)       
44B1: FE FF      CP      $FF             
44B3: C8         RET     Z               
44B4: 17         RLA                     
44B5: E6 FE      AND     $FE             
44B7: 5F         LD      E,A             
44B8: 17         RLA                     
44B9: 17         RLA                     
44BA: 17         RLA                     
44BB: E6 F0      AND     $F0             
44BD: 83         ADD     A,E             
44BE: 5F         LD      E,A             
44BF: 16 00      LD      D,$00           
44C1: 21 99 40   LD      HL,$4099        
44C4: 19         ADD     HL,DE           
44C5: 11 30 C0   LD      DE,$C030        
44C8: F0 E7      LD      A,($E7)         
44CA: E6 01      AND     $01             
44CC: 3E 10      LD      A,$10           
44CE: 28 03      JR      Z,$44D3         
44D0: 23         INC     HL              
44D1: 3E 18      LD      A,$18           
44D3: E0 D7      LDFF00  ($D7),A         
44D5: 0E 09      LD      C,$09           
44D7: 3E 40      LD      A,$40           
44D9: 12         LD      (DE),A          
44DA: 13         INC     DE              
44DB: F0 D7      LD      A,($D7)         
44DD: 12         LD      (DE),A          
44DE: 13         INC     DE              
44DF: C6 10      ADD     $10             
44E1: E0 D7      LDFF00  ($D7),A         
44E3: 2A         LD      A,(HLI)         
44E4: 23         INC     HL              
44E5: E5         PUSH    HL              
44E6: D5         PUSH    DE              
44E7: FE 20      CP      $20             
44E9: 20 04      JR      NZ,$44EF        
44EB: 3E 0F      LD      A,$0F           
44ED: 18 0A      JR      $44F9           
44EF: D6 41      SUB     $41             
44F1: 5F         LD      E,A             
44F2: 16 00      LD      D,$00           
44F4: 21 94 44   LD      HL,$4494        
44F7: 19         ADD     HL,DE           
44F8: 7E         LD      A,(HL)          
44F9: D1         POP     DE              
44FA: E1         POP     HL              
44FB: 12         LD      (DE),A          
44FC: 13         INC     DE              
44FD: 3E 10      LD      A,$10           
44FF: 12         LD      (DE),A          
4500: 13         INC     DE              
4501: 0D         DEC     C               
4502: 20 D3      JR      NZ,$44D7        
4504: C9         RET                     
4505: 20 30      JR      NZ,$4537        
4507: 21 31 22   LD      HL,$2231        
450A: 22         LD      (HLI),A         
450B: 23         INC     HL              
450C: 33         INC     SP              
450D: 24         INC     H               
450E: 34         INC     (HL)            
450F: 24         INC     H               
4510: 35         DEC     (HL)            
4511: 22         LD      (HLI),A         
4512: 32         LD      (HLD),A         
4513: 36 30      LD      (HL),$30        
4515: 27         DAA                     
4516: 27         DAA                     
4517: 28 38      JR      Z,$4551         
4519: 29         ADD     HL,HL           
451A: 39         ADD     HL,SP           
451B: 00         NOP                     
451C: 00         NOP                     
451D: 2A         LD      A,(HLI)         
451E: 3A         LD      A,(HLD)         
451F: 2B         DEC     HL              
4520: 3B         DEC     SP              
4521: 20 20      JR      NZ,$4543        
4523: 21 35 00   LD      HL,$0035        
4526: 00         NOP                     
4527: 21 26 2C   LD      HL,$2C26        
452A: 3C         INC     A               
452B: 2D         DEC     L               
452C: 3D         DEC     A               
452D: 36 20      LD      (HL),$20        
452F: 00         NOP                     
4530: 00         NOP                     
4531: 2E 3E      LD      L,$3E           
4533: 00         NOP                     
4534: 00         NOP                     
4535: 36 25      LD      (HL),$25        
4537: 37         SCF                     
4538: 37         SCF                     
4539: 10 10      STOP    $10             
453B: 10 10      STOP    $10             
453D: 10 50      STOP    $50             
453F: 10 10      STOP    $10             
4541: 10 10      STOP    $10             
4543: 10 10      STOP    $10             
4545: 10 10      STOP    $10             
4547: 50         LD      D,B             
4548: 10 10      STOP    $10             
454A: 50         LD      D,B             
454B: 10 10      STOP    $10             
454D: 10 10      STOP    $10             
454F: 10 10      STOP    $10             
4551: 10 10      STOP    $10             
4553: 10 10      STOP    $10             
4555: 10 50      STOP    $50             
4557: 10 10      STOP    $10             
4559: 10 10      STOP    $10             
455B: 10 10      STOP    $10             
455D: 10 10      STOP    $10             
455F: 10 10      STOP    $10             
4561: 50         LD      D,B             
4562: 50         LD      D,B             
4563: 10 10      STOP    $10             
4565: 10 10      STOP    $10             
4567: 10 10      STOP    $10             
4569: 50         LD      D,B             
456A: 10 10      STOP    $10             
456C: 70         LD      (HL),B          
456D: FA 11 D0   LD      A,($D011)       
4570: 17         RLA                     
4571: E6 FE      AND     $FE             
4573: 5F         LD      E,A             
4574: 16 00      LD      D,$00           
4576: 17         RLA                     
4577: CB 12      SET     1,E             
4579: 17         RLA                     
457A: CB 12      SET     1,E             
457C: 17         RLA                     
457D: CB 12      SET     1,E             
457F: E6 F0      AND     $F0             
4581: 83         ADD     A,E             
4582: 5F         LD      E,A             
4583: 7A         LD      A,D             
4584: CE 00      ADC     $00             
4586: 57         LD      D,A             
4587: 21 71 41   LD      HL,$4171        
458A: 19         ADD     HL,DE           
458B: E5         PUSH    HL              
458C: AF         XOR     A               
458D: E0 D8      LDFF00  ($D8),A         
458F: 11 54 C0   LD      DE,$C054        
4592: 3E 55      LD      A,$55           
4594: CD A1 45   CALL    $45A1           
4597: 21 D8 FF   LD      HL,$FFD8        
459A: 34         INC     (HL)            
459B: E1         POP     HL              
459C: 11 78 C0   LD      DE,$C078        
459F: 3E 5D      LD      A,$5D           
45A1: E0 E9      LDFF00  ($E9),A         
45A3: 0E 12      LD      C,$12           
45A5: 06 08      LD      B,$08           
45A7: FA 11 D0   LD      A,($D011)       
45AA: FE 15      CP      $15             
45AC: 3E 38      LD      A,$38           
45AE: 28 0F      JR      Z,$45BF         
45B0: 0E 09      LD      C,$09           
45B2: 06 10      LD      B,$10           
45B4: F0 E7      LD      A,($E7)         
45B6: E6 01      AND     $01             
45B8: 3E 10      LD      A,$10           
45BA: 28 03      JR      Z,$45BF         
45BC: 23         INC     HL              
45BD: 3E 18      LD      A,$18           
45BF: E0 D7      LDFF00  ($D7),A         
45C1: F0 E9      LD      A,($E9)         
45C3: 12         LD      (DE),A          
45C4: 13         INC     DE              
45C5: F0 D7      LD      A,($D7)         
45C7: 12         LD      (DE),A          
45C8: 13         INC     DE              
45C9: 80         ADD     A,B             
45CA: E0 D7      LDFF00  ($D7),A         
45CC: FA 11 D0   LD      A,($D011)       
45CF: FE 15      CP      $15             
45D1: 2A         LD      A,(HLI)         
45D2: 28 01      JR      Z,$45D5         
45D4: 23         INC     HL              
45D5: E5         PUSH    HL              
45D6: D5         PUSH    DE              
45D7: FE 20      CP      $20             
45D9: 20 04      JR      NZ,$45DF        
45DB: 3E 0F      LD      A,$0F           
45DD: 18 17      JR      $45F6           
45DF: D6 41      SUB     $41             
45E1: CB 27      SET     1,E             
45E3: 21 D8 FF   LD      HL,$FFD8        
45E6: 86         ADD     A,(HL)          
45E7: 5F         LD      E,A             
45E8: 16 00      LD      D,$00           
45EA: 21 39 45   LD      HL,$4539        
45ED: 19         ADD     HL,DE           
45EE: 7E         LD      A,(HL)          
45EF: E0 E8      LDFF00  ($E8),A         
45F1: 21 05 45   LD      HL,$4505        
45F4: 19         ADD     HL,DE           
45F5: 7E         LD      A,(HL)          
45F6: D1         POP     DE              
45F7: E1         POP     HL              
45F8: 12         LD      (DE),A          
45F9: 13         INC     DE              
45FA: F0 E8      LD      A,($E8)         
45FC: 12         LD      (DE),A          
45FD: 13         INC     DE              
45FE: 0D         DEC     C               
45FF: 20 C0      JR      NZ,$45C1        
4601: C9         RET                     
4602: FA 14 C1   LD      A,($C114)       
4605: 3C         INC     A               
4606: FE C0      CP      $C0             
4608: 38 05      JR      C,$460F         
460A: 3E 0F      LD      A,$0F           
460C: E0 F4      LDFF00  ($F4),A         
460E: AF         XOR     A               
460F: EA 14 C1   LD      ($C114),A       
4612: FA 66 D4   LD      A,($D466)       
4615: A7         AND     A               
4616: 20 0E      JR      NZ,$4626        
4618: 3E 21      LD      A,$21           
461A: E0 F2      LDFF00  ($F2),A         
461C: CD ED 27   CALL    $27ED           
461F: E6 7F      AND     $7F             
4621: C6 50      ADD     $50             
4623: EA 66 D4   LD      ($D466),A       
4626: 3D         DEC     A               
4627: EA 66 D4   LD      ($D466),A       
462A: C9         RET                     
462B: 92         SUB     D               
462C: 93         SUB     E               
462D: 92         SUB     D               
462E: 93         SUB     E               
462F: 92         SUB     D               
4630: 93         SUB     E               
4631: 92         SUB     D               
4632: 93         SUB     E               
4633: 92         SUB     D               
4634: 93         SUB     E               
4635: 92         SUB     D               
4636: 93         SUB     E               
4637: 92         SUB     D               
4638: 93         SUB     E               
4639: 92         SUB     D               
463A: 93         SUB     E               
463B: 92         SUB     D               
463C: 93         SUB     E               
463D: 92         SUB     D               
463E: 93         SUB     E               
463F: 92         SUB     D               
4640: 82         ADD     A,D             
4641: 83         ADD     A,E             
4642: 82         ADD     A,D             
4643: 83         ADD     A,E             
4644: 82         ADD     A,D             
4645: 83         ADD     A,E             
4646: 82         ADD     A,D             
4647: 83         ADD     A,E             
4648: 82         ADD     A,D             
4649: 83         ADD     A,E             
464A: 82         ADD     A,D             
464B: 83         ADD     A,E             
464C: 82         ADD     A,D             
464D: 83         ADD     A,E             
464E: 82         ADD     A,D             
464F: 83         ADD     A,E             
4650: 82         ADD     A,D             
4651: 83         ADD     A,E             
4652: 82         ADD     A,D             
4653: 83         ADD     A,E             
4654: 82         ADD     A,D             
4655: F0 E7      LD      A,($E7)         
4657: E6 0F      AND     $0F             
4659: FE 02      CP      $02             
465B: 20 38      JR      NZ,$4695        
465D: D5         PUSH    DE              
465E: 21 01 D6   LD      HL,$D601        
4661: 7A         LD      A,D             
4662: 22         LD      (HLI),A         
4663: 7B         LD      A,E             
4664: 22         LD      (HLI),A         
4665: 3E 13      LD      A,$13           
4667: 22         LD      (HLI),A         
4668: 11 2B 46   LD      DE,$462B        
466B: F0 E7      LD      A,($E7)         
466D: E6 10      AND     $10             
466F: 28 01      JR      Z,$4672         
4671: 13         INC     DE              
4672: 0E 14      LD      C,$14           
4674: 1A         LD      A,(DE)          
4675: 22         LD      (HLI),A         
4676: 0D         DEC     C               
4677: 20 FB      JR      NZ,$4674        
4679: D1         POP     DE              
467A: 7A         LD      A,D             
467B: 22         LD      (HLI),A         
467C: 7B         LD      A,E             
467D: D6 20      SUB     $20             
467F: 22         LD      (HLI),A         
4680: 3E 13      LD      A,$13           
4682: 22         LD      (HLI),A         
4683: 11 40 46   LD      DE,$4640        
4686: F0 E7      LD      A,($E7)         
4688: E6 10      AND     $10             
468A: 28 01      JR      Z,$468D         
468C: 13         INC     DE              
468D: 0E 14      LD      C,$14           
468F: 1A         LD      A,(DE)          
4690: 22         LD      (HLI),A         
4691: 0D         DEC     C               
4692: 20 FB      JR      NZ,$468F        
4694: 71         LD      (HL),C          
4695: C9         RET                     
4696: F4         ???                     
4697: F4         ???                     
4698: F5         PUSH    AF              
4699: F6 F7      OR      $F7             
469B: F7         RST     0X30            
469C: F8 F8      LDHL    SP,$F8          
469E: F8 F8      LDHL    SP,$F8          
46A0: F7         RST     0X30            
46A1: F7         RST     0X30            
46A2: F6 F5      OR      $F5             
46A4: F4         ???                     
46A5: F4         ???                     
46A6: F0 E7      LD      A,($E7)         
46A8: 1F         RRA                     
46A9: 1F         RRA                     
46AA: 1F         RRA                     
46AB: 00         NOP                     
46AC: E6 0F      AND     $0F             
46AE: 5F         LD      E,A             
46AF: 16 00      LD      D,$00           
46B1: 21 96 46   LD      HL,$4696        
46B4: 19         ADD     HL,DE           
46B5: 7E         LD      A,(HL)          
46B6: D6 05      SUB     $05             
46B8: E0 42      LDFF00  ($42),A         
46BA: E0 E8      LDFF00  ($E8),A         
46BC: FA 7F C1   LD      A,($C17F)       
46BF: FE FE      CP      $FE             
46C1: C8         RET     Z               
46C2: FA 80 C1   LD      A,($C180)       
46C5: 3C         INC     A               
46C6: EA 80 C1   LD      ($C180),A       
46C9: FA 05 D0   LD      A,($D005)       
46CC: E0 D8      LDFF00  ($D8),A         
46CE: 21 7C C1   LD      HL,$C17C        
46D1: AF         XOR     A               
46D2: 22         LD      (HLI),A         
46D3: 22         LD      (HLI),A         
46D4: 22         LD      (HLI),A         
46D5: F0 41      LD      A,($41)         
46D7: E6 03      AND     $03             
46D9: 20 FA      JR      NZ,$46D5        
46DB: 16 00      LD      D,$00           
46DD: FA 7E C1   LD      A,($C17E)       
46E0: 3C         INC     A               
46E1: EA 7E C1   LD      ($C17E),A       
46E4: E6 01      AND     $01             
46E6: 20 F5      JR      NZ,$46DD        
46E8: FA 7C C1   LD      A,($C17C)       
46EB: C6 01      ADD     $01             
46ED: EA 7C C1   LD      ($C17C),A       
46F0: FA 7D C1   LD      A,($C17D)       
46F3: CE 00      ADC     $00             
46F5: EA 7D C1   LD      ($C17D),A       
46F8: FA 7C C1   LD      A,($C17C)       
46FB: FE 50      CP      $50             
46FD: CA 26 47   JP      Z,$4726         
4700: 21 80 C1   LD      HL,$C180        
4703: FA 7C C1   LD      A,($C17C)       
4706: 86         ADD     A,(HL)          
4707: E6 1F      AND     $1F             
4709: 21 D8 FF   LD      HL,$FFD8        
470C: B6         OR      (HL)            
470D: 5F         LD      E,A             
470E: 21 2A 47   LD      HL,$472A        
4711: 19         ADD     HL,DE           
4712: 7E         LD      A,(HL)          
4713: F5         PUSH    AF              
4714: 21 96 FF   LD      HL,$FF96        
4717: 86         ADD     A,(HL)          
4718: E0 43      LDFF00  ($43),A         
471A: F1         POP     AF              
471B: CB 2F      SET     1,E             
471D: 21 E8 FF   LD      HL,$FFE8        
4720: 86         ADD     A,(HL)          
4721: E0 42      LDFF00  ($42),A         
4723: C3 D5 46   JP      $46D5           
4726: AF         XOR     A               
4727: E0 43      LDFF00  ($43),A         
4729: C9         RET                     
472A: 00         NOP                     
472B: 05         DEC     B               
472C: 09         ADD     HL,BC           
472D: 0C         INC     C               
472E: 0D         DEC     C               
472F: 0E 0E      LD      C,$0E           
4731: 0F         RRCA                    
4732: 0F         RRCA                    
4733: 0F         RRCA                    
4734: 0E 0E      LD      C,$0E           
4736: 0D         DEC     C               
4737: 0C         INC     C               
4738: 09         ADD     HL,BC           
4739: 05         DEC     B               
473A: 00         NOP                     
473B: FB         EI                      
473C: F7         RST     0X30            
473D: F4         ???                     
473E: F3         DI                      
473F: F2         ???                     
4740: F2         ???                     
4741: F1         POP     AF              
4742: F1         POP     AF              
4743: F1         POP     AF              
4744: F2         ???                     
4745: F2         ???                     
4746: F3         DI                      
4747: F4         ???                     
4748: F7         RST     0X30            
4749: FB         EI                      
474A: 00         NOP                     
474B: 04         INC     B               
474C: 07         RLCA                    
474D: 09         ADD     HL,BC           
474E: 0B         DEC     BC              
474F: 0C         INC     C               
4750: 0C         INC     C               
4751: 0D         DEC     C               
4752: 0D         DEC     C               
4753: 0D         DEC     C               
4754: 0C         INC     C               
4755: 0C         INC     C               
4756: 0B         DEC     BC              
4757: 09         ADD     HL,BC           
4758: 07         RLCA                    
4759: 04         INC     B               
475A: 00         NOP                     
475B: FC         ???                     
475C: F9         LD      SP,HL           
475D: F7         RST     0X30            
475E: F5         PUSH    AF              
475F: F4         ???                     
4760: F4         ???                     
4761: F3         DI                      
4762: F3         DI                      
4763: F3         DI                      
4764: F4         ???                     
4765: F4         ???                     
4766: F5         PUSH    AF              
4767: F7         RST     0X30            
4768: F9         LD      SP,HL           
4769: FC         ???                     
476A: 00         NOP                     
476B: 03         INC     BC              
476C: 05         DEC     B               
476D: 07         RLCA                    
476E: 08 09 0A   LD      ($0A09),SP      
4771: 0B         DEC     BC              
4772: 0B         DEC     BC              
4773: 0B         DEC     BC              
4774: 0A         LD      A,(BC)          
4775: 09         ADD     HL,BC           
4776: 08 07 05   LD      ($0507),SP      
4779: 03         INC     BC              
477A: 00         NOP                     
477B: FD         ???                     
477C: FB         EI                      
477D: F9         LD      SP,HL           
477E: F8 F7      LDHL    SP,$F7          
4780: F6 F5      OR      $F5             
4782: F5         PUSH    AF              
4783: F5         PUSH    AF              
4784: F6 F7      OR      $F7             
4786: F8 F9      LDHL    SP,$F9          
4788: FB         EI                      
4789: FD         ???                     
478A: 00         NOP                     
478B: 03         INC     BC              
478C: 05         DEC     B               
478D: 06 07      LD      B,$07           
478F: 08 08 09   LD      ($0908),SP      
4792: 09         ADD     HL,BC           
4793: 09         ADD     HL,BC           
4794: 08 08 07   LD      ($0708),SP      
4797: 06 05      LD      B,$05           
4799: 03         INC     BC              
479A: 00         NOP                     
479B: FD         ???                     
479C: FB         EI                      
479D: FA F9 F8   LD      A,($F8F9)       
47A0: F8 F7      LDHL    SP,$F7          
47A2: F7         RST     0X30            
47A3: F7         RST     0X30            
47A4: F8 F8      LDHL    SP,$F8          
47A6: F9         LD      SP,HL           
47A7: FA FB FD   LD      A,($FDFB)       
47AA: 00         NOP                     
47AB: 02         LD      (BC),A          
47AC: 04         INC     B               
47AD: 05         DEC     B               
47AE: 05         DEC     B               
47AF: 06 06      LD      B,$06           
47B1: 07         RLCA                    
47B2: 07         RLCA                    
47B3: 07         RLCA                    
47B4: 06 06      LD      B,$06           
47B6: 05         DEC     B               
47B7: 05         DEC     B               
47B8: 04         INC     B               
47B9: 02         LD      (BC),A          
47BA: 00         NOP                     
47BB: FE FC      CP      $FC             
47BD: FB         EI                      
47BE: FB         EI                      
47BF: FA FA F9   LD      A,($F9FA)       
47C2: F9         LD      SP,HL           
47C3: F9         LD      SP,HL           
47C4: FA FA FB   LD      A,($FBFA)       
47C7: FB         EI                      
47C8: FC         ???                     
47C9: FE 00      CP      $00             
47CB: 01 02 03   LD      BC,$0302        
47CE: 03         INC     BC              
47CF: 04         INC     B               
47D0: 04         INC     B               
47D1: 05         DEC     B               
47D2: 05         DEC     B               
47D3: 05         DEC     B               
47D4: 04         INC     B               
47D5: 04         INC     B               
47D6: 03         INC     BC              
47D7: 03         INC     BC              
47D8: 02         LD      (BC),A          
47D9: 01 00 FF   LD      BC,$FF00        
47DC: FE FD      CP      $FD             
47DE: FD         ???                     
47DF: FC         ???                     
47E0: FC         ???                     
47E1: FB         EI                      
47E2: FB         EI                      
47E3: FB         EI                      
47E4: FC         ???                     
47E5: FC         ???                     
47E6: FD         ???                     
47E7: FD         ???                     
47E8: FE FF      CP      $FF             
47EA: 00         NOP                     
47EB: 01 01 01   LD      BC,$0101        
47EE: 02         LD      (BC),A          
47EF: 02         LD      (BC),A          
47F0: 02         LD      (BC),A          
47F1: 03         INC     BC              
47F2: 03         INC     BC              
47F3: 03         INC     BC              
47F4: 02         LD      (BC),A          
47F5: 02         LD      (BC),A          
47F6: 02         LD      (BC),A          
47F7: 01 01 01   LD      BC,$0101        
47FA: 00         NOP                     
47FB: FF         RST     0X38            
47FC: FF         RST     0X38            
47FD: FF         RST     0X38            
47FE: FE FE      CP      $FE             
4800: FE FD      CP      $FD             
4802: FD         ???                     
4803: FD         ???                     
4804: FE FE      CP      $FE             
4806: FE FF      CP      $FF             
4808: FF         RST     0X38            
4809: FF         RST     0X38            
480A: 00         NOP                     
480B: 00         NOP                     
480C: 00         NOP                     
480D: 00         NOP                     
480E: 01 01 01   LD      BC,$0101        
4811: 01 01 01   LD      BC,$0101        
4814: 01 01 01   LD      BC,$0101        
4817: 00         NOP                     
4818: 00         NOP                     
4819: 00         NOP                     
481A: 00         NOP                     
481B: 00         NOP                     
481C: 00         NOP                     
481D: 00         NOP                     
481E: FF         RST     0X38            
481F: FF         RST     0X38            
4820: FF         RST     0X38            
4821: FF         RST     0X38            
4822: FF         RST     0X38            
4823: FF         RST     0X38            
4824: FF         RST     0X38            
4825: FF         RST     0X38            
4826: FF         RST     0X38            
4827: 00         NOP                     
4828: 00         NOP                     
4829: 00         NOP                     
482A: F0 CC      LD      A,($CC)         
482C: E6 0C      AND     $0C             
482E: 28 0A      JR      Z,$483A         
4830: FA 04 00   LD      A,($0004)       
4833: A7         AND     A               
4834: 28 04      JR      Z,$483A         
4836: AF         XOR     A               
4837: EA 96 DB   LD      ($DB96),A       
483A: F0 CC      LD      A,($CC)         
483C: E6 03      AND     $03             
483E: 28 09      JR      Z,$4849         
4840: FA 04 00   LD      A,($0004)       
4843: A7         AND     A               
4844: 28 03      JR      Z,$4849         
4846: CD C1 5C   CALL    $5CC1           
4849: FA 06 D0   LD      A,($D006)       
484C: A7         AND     A               
484D: 28 04      JR      Z,$4853         
484F: 3D         DEC     A               
4850: EA 06 D0   LD      ($D006),A       
4853: FA 07 D0   LD      A,($D007)       
4856: A7         AND     A               
4857: 28 04      JR      Z,$485D         
4859: 3D         DEC     A               
485A: EA 07 D0   LD      ($D007),A       
485D: FA 08 D0   LD      A,($D008)       
4860: A7         AND     A               
4861: 28 04      JR      Z,$4867         
4863: 3D         DEC     A               
4864: EA 08 D0   LD      ($D008),A       
4867: F0 E7      LD      A,($E7)         
4869: E6 03      AND     $03             
486B: 20 0A      JR      NZ,$4877        
486D: FA 09 D0   LD      A,($D009)       
4870: A7         AND     A               
4871: 28 04      JR      Z,$4877         
4873: 3D         DEC     A               
4874: EA 09 D0   LD      ($D009),A       
4877: F0 E7      LD      A,($E7)         
4879: E6 0F      AND     $0F             
487B: 20 0A      JR      NZ,$4887        
487D: FA 13 D0   LD      A,($D013)       
4880: A7         AND     A               
4881: 28 04      JR      Z,$4887         
4883: 3D         DEC     A               
4884: EA 13 D0   LD      ($D013),A       
4887: FA 96 DB   LD      A,($DB96)       
488A: C7         RST     0X00            
488B: 3D         DEC     A               
488C: 49         LD      C,C             
488D: 43         LD      B,E             
488E: 49         LD      C,C             
488F: B7         OR      A               
4890: 49         LD      C,C             
4891: 51         LD      D,C             
4892: 59         LD      E,C             
4893: 96         SUB     (HL)            
4894: 58         LD      E,B             
4895: 70         LD      (HL),B          
4896: 5A         LD      E,D             
4897: 1E 5F      LD      E,$5F           
4899: BF         CP      A               
489A: 6A         LD      L,D             
489B: DE 6B      SBC     $6B             
489D: 00         NOP                     
489E: 00         NOP                     
489F: 00         NOP                     
48A0: 00         NOP                     
48A1: 00         NOP                     
48A2: 00         NOP                     
48A3: 00         NOP                     
48A4: 00         NOP                     
48A5: 00         NOP                     
48A6: 00         NOP                     
48A7: 00         NOP                     
48A8: 00         NOP                     
48A9: 00         NOP                     
48AA: 00         NOP                     
48AB: 00         NOP                     
48AC: 00         NOP                     
48AD: 00         NOP                     
48AE: 00         NOP                     
48AF: 00         NOP                     
48B0: 00         NOP                     
48B1: 00         NOP                     
48B2: 00         NOP                     
48B3: 00         NOP                     
48B4: 00         NOP                     
48B5: 00         NOP                     
48B6: 00         NOP                     
48B7: 00         NOP                     
48B8: 00         NOP                     
48B9: 00         NOP                     
48BA: 00         NOP                     
48BB: 00         NOP                     
48BC: 00         NOP                     
48BD: 01 01 01   LD      BC,$0101        
48C0: 01 01 01   LD      BC,$0101        
48C3: 01 01 01   LD      BC,$0101        
48C6: 01 01 01   LD      BC,$0101        
48C9: 01 01 01   LD      BC,$0101        
48CC: 01 01 01   LD      BC,$0101        
48CF: 00         NOP                     
48D0: 00         NOP                     
48D1: 00         NOP                     
48D2: 00         NOP                     
48D3: 00         NOP                     
48D4: 00         NOP                     
48D5: 00         NOP                     
48D6: 00         NOP                     
48D7: 01 01 01   LD      BC,$0101        
48DA: 01 01 01   LD      BC,$0101        
48DD: 01 01 00   LD      BC,$0001        
48E0: 01 01 01   LD      BC,$0101        
48E3: 01 01 01   LD      BC,$0101        
48E6: 00         NOP                     
48E7: 01 00 00   LD      BC,$0000        
48EA: 00         NOP                     
48EB: 00         NOP                     
48EC: 00         NOP                     
48ED: 01 01 00   LD      BC,$0001        
48F0: 01 01 01   LD      BC,$0101        
48F3: 01 01 01   LD      BC,$0101        
48F6: 00         NOP                     
48F7: 01 00 00   LD      BC,$0000        
48FA: 00         NOP                     
48FB: 00         NOP                     
48FC: 00         NOP                     
48FD: 01 01 00   LD      BC,$0001        
4900: 01 01 01   LD      BC,$0101        
4903: 01 01 01   LD      BC,$0101        
4906: 00         NOP                     
4907: 01 00 00   LD      BC,$0000        
490A: 00         NOP                     
490B: 00         NOP                     
490C: 00         NOP                     
490D: 01 01 00   LD      BC,$0001        
4910: 00         NOP                     
4911: 00         NOP                     
4912: 00         NOP                     
4913: 00         NOP                     
4914: 00         NOP                     
4915: 00         NOP                     
4916: 00         NOP                     
4917: 01 00 00   LD      BC,$0000        
491A: 00         NOP                     
491B: 00         NOP                     
491C: 00         NOP                     
491D: E4         ???                     
491E: E4         ???                     
491F: E4         ???                     
4920: E4         ???                     
4921: 94         SUB     H               
4922: 94         SUB     H               
4923: 94         SUB     H               
4924: 94         SUB     H               
4925: 40         LD      B,B             
4926: 40         LD      B,B             
4927: 40         LD      B,B             
4928: 40         LD      B,B             
4929: 00         NOP                     
492A: 00         NOP                     
492B: 00         NOP                     
492C: 00         NOP                     
492D: 1C         INC     E               
492E: 1C         INC     E               
492F: 1C         INC     E               
4930: 1C         INC     E               
4931: 18 18      JR      $494B           
4933: 18 18      JR      $494D           
4935: 04         INC     B               
4936: 04         INC     B               
4937: 04         INC     B               
4938: 04         INC     B               
4939: 00         NOP                     
493A: 00         NOP                     
493B: 00         NOP                     
493C: 00         NOP                     
493D: CD EB 4A   CALL    $4AEB           
4940: C3 B2 49   JP      $49B2           
4943: CD 13 0B   CALL    $0B13           
4946: F0 E7      LD      A,($E7)         
4948: E6 03      AND     $03             
494A: 20 0E      JR      NZ,$495A        
494C: FA 01 D0   LD      A,($D001)       
494F: 3C         INC     A               
4950: EA 01 D0   LD      ($D001),A       
4953: FE 0D      CP      $0D             
4955: 20 03      JR      NZ,$495A        
4957: C3 79 49   JP      $4979           
495A: FA 01 D0   LD      A,($D001)       
495D: 5F         LD      E,A             
495E: F0 E7      LD      A,($E7)         
4960: E6 03      AND     $03             
4962: 83         ADD     A,E             
4963: 5F         LD      E,A             
4964: 50         LD      D,B             
4965: 21 1D 49   LD      HL,$491D        
4968: 19         ADD     HL,DE           
4969: 7E         LD      A,(HL)          
496A: EA 97 DB   LD      ($DB97),A       
496D: EA 99 DB   LD      ($DB99),A       
4970: 21 2D 49   LD      HL,$492D        
4973: 19         ADD     HL,DE           
4974: 7E         LD      A,(HL)          
4975: EA 98 DB   LD      ($DB98),A       
4978: C9         RET                     
4979: CD 7B 29   CALL    $297B           
497C: 21 00 D7   LD      HL,$D700        
497F: 11 9D 48   LD      DE,$489D        
4982: 0E 80      LD      C,$80           
4984: 3E 01      LD      A,$01           
4986: 1A         LD      A,(DE)          
4987: 13         INC     DE              
4988: 22         LD      (HLI),A         
4989: 0D         DEC     C               
498A: 20 FA      JR      NZ,$4986        
498C: CD D2 27   CALL    $27D2           
498F: 3E 01      LD      A,$01           
4991: E0 FF      LDFF00  ($FF),A         
4993: 3E 00      LD      A,$00           
4995: E0 45      LDFF00  ($45),A         
4997: 21 FD D6   LD      HL,$D6FD        
499A: CB 9E      SET     1,E             
499C: CD EB 4A   CALL    $4AEB           
499F: CD B2 49   CALL    $49B2           
49A2: 3E 59      LD      A,$59           
49A4: EA 68 D3   LD      ($D368),A       
49A7: 3E 40      LD      A,$40           
49A9: EA 06 D0   LD      ($D006),A       
49AC: 3E 04      LD      A,$04           
49AE: EA 6B C1   LD      ($C16B),A       
49B1: C9         RET                     
49B2: 21 96 DB   LD      HL,$DB96        
49B5: 34         INC     (HL)            
49B6: C9         RET                     
49B7: 3E 80      LD      A,$80           
49B9: EA 56 DB   LD      ($DB56),A       
49BC: AF         XOR     A               
49BD: EA A5 DB   LD      ($DBA5),A       
49C0: E0 F8      LDFF00  ($F8),A         
49C2: 3E 01      LD      A,$01           
49C4: EA C8 C3   LD      ($C3C8),A       
49C7: 3E 92      LD      A,$92           
49C9: E0 F6      LDFF00  ($F6),A         
49CB: 3E FF      LD      A,$FF           
49CD: EA C7 DB   LD      ($DBC7),A       
49D0: CD 13 0B   CALL    $0B13           
49D3: FA 0E D0   LD      A,($D00E)       
49D6: C7         RST     0X00            
49D7: 09         ADD     HL,BC           
49D8: 4A         LD      C,D             
49D9: 30 4A      JR      NC,$4A25        
49DB: 8B         ADC     A,E             
49DC: 4A         LD      C,D             
49DD: C7         RST     0X00            
49DE: 4A         LD      C,D             
49DF: 5F         LD      E,A             
49E0: 4B         LD      C,E             
49E1: 8C         ADC     A,H             
49E2: 4B         LD      C,E             
49E3: 8D         ADC     A,L             
49E4: 4B         LD      C,E             
49E5: 9E         SBC     (HL)            
49E6: 4B         LD      C,E             
49E7: BF         CP      A               
49E8: 4C         LD      C,H             
49E9: 1B         DEC     DE              
49EA: 4D         LD      C,L             
49EB: 76         HALT                    
49EC: 4D         LD      C,L             
49ED: 89         ADC     A,C             
49EE: 4D         LD      C,L             
49EF: 93         SUB     E               
49F0: 4D         LD      C,L             
49F1: C4 4D 47   CALL    NZ,$474D        
49F4: 4E         LD      C,(HL)          
49F5: 7D         LD      A,L             
49F6: 4E         LD      C,(HL)          
49F7: 92         SUB     D               
49F8: 4E         LD      C,(HL)          
49F9: DD         ???                     
49FA: 4E         LD      C,(HL)          
49FB: 5C         LD      E,H             
49FC: 4F         LD      C,A             
49FD: 6F         LD      L,A             
49FE: 4F         LD      C,A             
49FF: CF         RST     0X08            
4A00: 53         LD      D,E             
4A01: 0E 54      LD      C,$54           
4A03: 7C         LD      A,H             
4A04: 57         LD      D,A             
4A05: 25         DEC     H               
4A06: 58         LD      E,B             
4A07: 74         LD      (HL),H          
4A08: 58         LD      E,B             
4A09: 3E FF      LD      A,$FF           
4A0B: EA 9A DB   LD      ($DB9A),A       
4A0E: 3E 1F      LD      A,$1F           
4A10: EA FE D6   LD      ($D6FE),A       
4A13: AF         XOR     A               
4A14: E0 96      LDFF00  ($96),A         
4A16: EA 55 C1   LD      ($C155),A       
4A19: EA 56 C1   LD      ($C156),A       
4A1C: E0 97      LDFF00  ($97),A         
4A1E: 21 24 C1   LD      HL,$C124        
4A21: 1E 00      LD      E,$00           
4A23: AF         XOR     A               
4A24: 22         LD      (HLI),A         
4A25: 1C         INC     E               
4A26: 7B         LD      A,E             
4A27: FE 0C      CP      $0C             
4A29: 20 F8      JR      NZ,$4A23        
4A2B: 21 0E D0   LD      HL,$D00E        
4A2E: 34         INC     (HL)            
4A2F: C9         RET                     
4A30: 3E 16      LD      A,$16           
4A32: EA FF D6   LD      ($D6FF),A       
4A35: 3E E8      LD      A,$E8           
4A37: CD 01 3C   CALL    $3C01           
4A3A: 21 00 C2   LD      HL,$C200        
4A3D: 19         ADD     HL,DE           
4A3E: 36 40      LD      (HL),$40        
4A40: 21 10 C2   LD      HL,$C210        
4A43: 19         ADD     HL,DE           
4A44: 36 E0      LD      (HL),$E0        
4A46: 3E E8      LD      A,$E8           
4A48: CD 01 3C   CALL    $3C01           
4A4B: 21 B0 C2   LD      HL,$C2B0        
4A4E: 19         ADD     HL,DE           
4A4F: 34         INC     (HL)            
4A50: 3E 50      LD      A,$50           
4A52: E0 98      LDFF00  ($98),A         
4A54: 3E 98      LD      A,$98           
4A56: E0 99      LDFF00  ($99),A         
4A58: C3 2B 4A   JP      $4A2B           
4A5B: 00         NOP                     
4A5C: 00         NOP                     
4A5D: 00         NOP                     
4A5E: 00         NOP                     
4A5F: 01 01 01   LD      BC,$0101        
4A62: 01 16 16   LD      BC,$1616        
4A65: 16 16      LD      D,$16           
4A67: 27         DAA                     
4A68: 27         DAA                     
4A69: 27         DAA                     
4A6A: 27         DAA                     
4A6B: 00         NOP                     
4A6C: 00         NOP                     
4A6D: 00         NOP                     
4A6E: 00         NOP                     
4A6F: 04         INC     B               
4A70: 04         INC     B               
4A71: 04         INC     B               
4A72: 04         INC     B               
4A73: 18 18      JR      $4A8D           
4A75: 18 18      JR      $4A8F           
4A77: 1C         INC     E               
4A78: 1C         INC     E               
4A79: 1C         INC     E               
4A7A: 1C         INC     E               
4A7B: 00         NOP                     
4A7C: 00         NOP                     
4A7D: 00         NOP                     
4A7E: 00         NOP                     
4A7F: 00         NOP                     
4A80: 00         NOP                     
4A81: 00         NOP                     
4A82: 00         NOP                     
4A83: 50         LD      D,B             
4A84: 50         LD      D,B             
4A85: 50         LD      D,B             
4A86: 50         LD      D,B             
4A87: 90         SUB     B               
4A88: 90         SUB     B               
4A89: 90         SUB     B               
4A8A: 90         SUB     B               
4A8B: FA 06 D0   LD      A,($D006)       
4A8E: 5F         LD      E,A             
4A8F: F0 E7      LD      A,($E7)         
4A91: E6 07      AND     $07             
4A93: B3         OR      E               
4A94: 20 0E      JR      NZ,$4AA4        
4A96: FA 01 D0   LD      A,($D001)       
4A99: 3C         INC     A               
4A9A: EA 01 D0   LD      ($D001),A       
4A9D: FE 0C      CP      $0C             
4A9F: 20 03      JR      NZ,$4AA4        
4AA1: CD 2B 4A   CALL    $4A2B           
4AA4: FA 01 D0   LD      A,($D001)       
4AA7: 5F         LD      E,A             
4AA8: F0 E7      LD      A,($E7)         
4AAA: E6 03      AND     $03             
4AAC: 83         ADD     A,E             
4AAD: 5F         LD      E,A             
4AAE: 50         LD      D,B             
4AAF: 21 5B 4A   LD      HL,$4A5B        
4AB2: 19         ADD     HL,DE           
4AB3: 7E         LD      A,(HL)          
4AB4: EA 97 DB   LD      ($DB97),A       
4AB7: 21 6B 4A   LD      HL,$4A6B        
4ABA: 19         ADD     HL,DE           
4ABB: 7E         LD      A,(HL)          
4ABC: EA 98 DB   LD      ($DB98),A       
4ABF: 21 7B 4A   LD      HL,$4A7B        
4AC2: 19         ADD     HL,DE           
4AC3: 7E         LD      A,(HL)          
4AC4: EA 99 DB   LD      ($DB99),A       
4AC7: FA 03 D0   LD      A,($D003)       
4ACA: C6 18      ADD     $18             
4ACC: EA 03 D0   LD      ($D003),A       
4ACF: 30 04      JR      NC,$4AD5        
4AD1: 21 1E C2   LD      HL,$C21E        
4AD4: 34         INC     (HL)            
4AD5: FA 02 D0   LD      A,($D002)       
4AD8: C6 40      ADD     $40             
4ADA: EA 02 D0   LD      ($D002),A       
4ADD: 30 37      JR      NC,$4B16        
4ADF: F0 97      LD      A,($97)         
4AE1: 3D         DEC     A               
4AE2: E0 97      LDFF00  ($97),A         
4AE4: FE 90      CP      $90             
4AE6: 20 2E      JR      NZ,$4B16        
4AE8: CD 2B 4A   CALL    $4A2B           
4AEB: AF         XOR     A               
4AEC: EA 00 D0   LD      ($D000),A       
4AEF: EA 01 D0   LD      ($D001),A       
4AF2: EA 02 D0   LD      ($D002),A       
4AF5: EA 03 D0   LD      ($D003),A       
4AF8: EA 04 D0   LD      ($D004),A       
4AFB: EA 05 D0   LD      ($D005),A       
4AFE: EA 0A D0   LD      ($D00A),A       
4B01: EA 0B D0   LD      ($D00B),A       
4B04: EA 0C D0   LD      ($D00C),A       
4B07: EA 0D D0   LD      ($D00D),A       
4B0A: EA 06 D0   LD      ($D006),A       
4B0D: EA 07 D0   LD      ($D007),A       
4B10: EA 08 D0   LD      ($D008),A       
4B13: EA 09 D0   LD      ($D009),A       
4B16: C9         RET                     
4B17: 98         SBC     B               
4B18: 00         NOP                     
4B19: 53         LD      D,E             
4B1A: A0         AND     B               
4B1B: 98         SBC     B               
4B1C: 20 53      JR      NZ,$4B71        
4B1E: A0         AND     B               
4B1F: 98         SBC     B               
4B20: 40         LD      B,B             
4B21: 53         LD      D,E             
4B22: A0         AND     B               
4B23: 98         SBC     B               
4B24: 60         LD      H,B             
4B25: 53         LD      D,E             
4B26: A0         AND     B               
4B27: 98         SBC     B               
4B28: 80         ADD     A,B             
4B29: 53         LD      D,E             
4B2A: A0         AND     B               
4B2B: 98         SBC     B               
4B2C: A0         AND     B               
4B2D: 53         LD      D,E             
4B2E: A0         AND     B               
4B2F: 98         SBC     B               
4B30: C0         RET     NZ              
4B31: 53         LD      D,E             
4B32: A0         AND     B               
4B33: 98         SBC     B               
4B34: E0 53      LDFF00  ($53),A         
4B36: A0         AND     B               
4B37: 99         SBC     C               
4B38: 00         NOP                     
4B39: 53         LD      D,E             
4B3A: A0         AND     B               
4B3B: 99         SBC     C               
4B3C: 20 53      JR      NZ,$4B91        
4B3E: A0         AND     B               
4B3F: 99         SBC     C               
4B40: 40         LD      B,B             
4B41: 53         LD      D,E             
4B42: A0         AND     B               
4B43: 99         SBC     C               
4B44: 60         LD      H,B             
4B45: 53         LD      D,E             
4B46: A0         AND     B               
4B47: 99         SBC     C               
4B48: 80         ADD     A,B             
4B49: 53         LD      D,E             
4B4A: A0         AND     B               
4B4B: 99         SBC     C               
4B4C: A0         AND     B               
4B4D: 53         LD      D,E             
4B4E: A0         AND     B               
4B4F: 99         SBC     C               
4B50: C0         RET     NZ              
4B51: 53         LD      D,E             
4B52: A0         AND     B               
4B53: 99         SBC     C               
4B54: E0 53      LDFF00  ($53),A         
4B56: A0         AND     B               
4B57: 9A         SBC     D               
4B58: 00         NOP                     
4B59: 53         LD      D,E             
4B5A: A0         AND     B               
4B5B: 9A         SBC     D               
4B5C: 20 53      JR      NZ,$4BB1        
4B5E: A0         AND     B               
4B5F: FA 00 D0   LD      A,($D000)       
4B62: FE 09      CP      $09             
4B64: 20 07      JR      NZ,$4B6D        
4B66: 3E F0      LD      A,$F0           
4B68: E0 97      LDFF00  ($97),A         
4B6A: C3 2B 4A   JP      $4A2B           
4B6D: 5F         LD      E,A             
4B6E: 3C         INC     A               
4B6F: EA 00 D0   LD      ($D000),A       
4B72: CB 23      SET     1,E             
4B74: CB 23      SET     1,E             
4B76: CB 23      SET     1,E             
4B78: 16 00      LD      D,$00           
4B7A: 21 17 4B   LD      HL,$4B17        
4B7D: 19         ADD     HL,DE           
4B7E: 11 01 D6   LD      DE,$D601        
4B81: 0E 08      LD      C,$08           
4B83: 2A         LD      A,(HLI)         
4B84: 12         LD      (DE),A          
4B85: 13         INC     DE              
4B86: 0D         DEC     C               
4B87: 20 FA      JR      NZ,$4B83        
4B89: AF         XOR     A               
4B8A: 12         LD      (DE),A          
4B8B: C9         RET                     
4B8C: C9         RET                     
4B8D: CD EB 4A   CALL    $4AEB           
4B90: 3E 08      LD      A,$08           
4B92: EA 06 D0   LD      ($D006),A       
4B95: C3 2B 4A   JP      $4A2B           
4B98: 27         DAA                     
4B99: 27         DAA                     
4B9A: EB         ???                     
4B9B: FF         RST     0X38            
4B9C: FF         RST     0X38            
4B9D: FF         RST     0X38            
4B9E: F0 E7      LD      A,($E7)         
4BA0: E6 01      AND     $01             
4BA2: 5F         LD      E,A             
4BA3: FA 0A D0   LD      A,($D00A)       
4BA6: 83         ADD     A,E             
4BA7: 5F         LD      E,A             
4BA8: 16 00      LD      D,$00           
4BAA: 21 98 4B   LD      HL,$4B98        
4BAD: 19         ADD     HL,DE           
4BAE: 7E         LD      A,(HL)          
4BAF: EA 97 DB   LD      ($DB97),A       
4BB2: FA 06 D0   LD      A,($D006)       
4BB5: A7         AND     A               
4BB6: 20 16      JR      NZ,$4BCE        
4BB8: 3E 08      LD      A,$08           
4BBA: EA 06 D0   LD      ($D006),A       
4BBD: FA 0A D0   LD      A,($D00A)       
4BC0: 3C         INC     A               
4BC1: EA 0A D0   LD      ($D00A),A       
4BC4: FE 05      CP      $05             
4BC6: 20 06      JR      NZ,$4BCE        
4BC8: CD EB 4A   CALL    $4AEB           
4BCB: C3 2B 4A   JP      $4A2B           
4BCE: C9         RET                     
4BCF: 9B         SBC     E               
4BD0: C0         RET     NZ              
4BD1: 13         INC     DE              
4BD2: A0         AND     B               
4BD3: A0         AND     B               
4BD4: A0         AND     B               
4BD5: A0         AND     B               
4BD6: A0         AND     B               
4BD7: A0         AND     B               
4BD8: A0         AND     B               
4BD9: A0         AND     B               
4BDA: A0         AND     B               
4BDB: A0         AND     B               
4BDC: 72         LD      (HL),D          
4BDD: 73         LD      (HL),E          
4BDE: 74         LD      (HL),H          
4BDF: A0         AND     B               
4BE0: A0         AND     B               
4BE1: A0         AND     B               
4BE2: A0         AND     B               
4BE3: A0         AND     B               
4BE4: A0         AND     B               
4BE5: A0         AND     B               
4BE6: 00         NOP                     
4BE7: 9B         SBC     E               
4BE8: E0 13      LDFF00  ($13),A         
4BEA: A0         AND     B               
4BEB: A0         AND     B               
4BEC: A0         AND     B               
4BED: A0         AND     B               
4BEE: A0         AND     B               
4BEF: A0         AND     B               
4BF0: A0         AND     B               
4BF1: A0         AND     B               
4BF2: A0         AND     B               
4BF3: A0         AND     B               
4BF4: 7B         LD      A,E             
4BF5: 7C         LD      A,H             
4BF6: 7D         LD      A,L             
4BF7: A0         AND     B               
4BF8: A0         AND     B               
4BF9: A0         AND     B               
4BFA: A0         AND     B               
4BFB: A0         AND     B               
4BFC: A0         AND     B               
4BFD: A0         AND     B               
4BFE: 00         NOP                     
4BFF: 98         SBC     B               
4C00: 00         NOP                     
4C01: 13         INC     DE              
4C02: A0         AND     B               
4C03: A0         AND     B               
4C04: A0         AND     B               
4C05: A0         AND     B               
4C06: A0         AND     B               
4C07: A0         AND     B               
4C08: A0         AND     B               
4C09: 05         DEC     B               
4C0A: 06 07      LD      B,$07           
4C0C: 08 09 0A   LD      ($0A09),SP      
4C0F: 0B         DEC     BC              
4C10: 0C         INC     C               
4C11: 0D         DEC     C               
4C12: 0E A0      LD      C,$A0           
4C14: A0         AND     B               
4C15: A0         AND     B               
4C16: 00         NOP                     
4C17: 98         SBC     B               
4C18: 20 13      JR      NZ,$4C2D        
4C1A: A0         AND     B               
4C1B: A0         AND     B               
4C1C: A0         AND     B               
4C1D: A0         AND     B               
4C1E: A0         AND     B               
4C1F: 13         INC     DE              
4C20: 14         INC     D               
4C21: 15         DEC     D               
4C22: 16 17      LD      D,$17           
4C24: 18 19      JR      $4C3F           
4C26: 1A         LD      A,(DE)          
4C27: 1B         DEC     DE              
4C28: 1C         INC     E               
4C29: 1D         DEC     E               
4C2A: 1E 1F      LD      E,$1F           
4C2C: A0         AND     B               
4C2D: A0         AND     B               
4C2E: 00         NOP                     
4C2F: 98         SBC     B               
4C30: 40         LD      B,B             
4C31: 13         INC     DE              
4C32: A0         AND     B               
4C33: A0         AND     B               
4C34: A0         AND     B               
4C35: A0         AND     B               
4C36: 22         LD      (HLI),A         
4C37: 23         INC     HL              
4C38: 24         INC     H               
4C39: 25         DEC     H               
4C3A: 26 27      LD      H,$27           
4C3C: 28 29      JR      Z,$4C67         
4C3E: 2A         LD      A,(HLI)         
4C3F: 2B         DEC     HL              
4C40: 2C         INC     L               
4C41: 2D         DEC     L               
4C42: 2E 2F      LD      L,$2F           
4C44: A0         AND     B               
4C45: A0         AND     B               
4C46: 00         NOP                     
4C47: 98         SBC     B               
4C48: 60         LD      H,B             
4C49: 13         INC     DE              
4C4A: A0         AND     B               
4C4B: A0         AND     B               
4C4C: A0         AND     B               
4C4D: 31 32 33   LD      SP,$3332        
4C50: 34         INC     (HL)            
4C51: 35         DEC     (HL)            
4C52: 36 37      LD      (HL),$37        
4C54: 38 39      JR      C,$4C8F         
4C56: 3A         LD      A,(HLD)         
4C57: 3B         DEC     SP              
4C58: 3C         INC     A               
4C59: 3D         DEC     A               
4C5A: 3E 3F      LD      A,$3F           
4C5C: A0         AND     B               
4C5D: A0         AND     B               
4C5E: 00         NOP                     
4C5F: 98         SBC     B               
4C60: 80         ADD     A,B             
4C61: 13         INC     DE              
4C62: A0         AND     B               
4C63: A0         AND     B               
4C64: 40         LD      B,B             
4C65: 41         LD      B,C             
4C66: 42         LD      B,D             
4C67: 43         LD      B,E             
4C68: 44         LD      B,H             
4C69: 45         LD      B,L             
4C6A: 46         LD      B,(HL)          
4C6B: 47         LD      B,A             
4C6C: 48         LD      C,B             
4C6D: 49         LD      C,C             
4C6E: 4A         LD      C,D             
4C6F: 4B         LD      C,E             
4C70: 4C         LD      C,H             
4C71: 4D         LD      C,L             
4C72: 4E         LD      C,(HL)          
4C73: 4F         LD      C,A             
4C74: A0         AND     B               
4C75: A0         AND     B               
4C76: 00         NOP                     
4C77: 98         SBC     B               
4C78: A0         AND     B               
4C79: 13         INC     DE              
4C7A: A0         AND     B               
4C7B: A0         AND     B               
4C7C: 50         LD      D,B             
4C7D: 51         LD      D,C             
4C7E: 52         LD      D,D             
4C7F: 53         LD      D,E             
4C80: 54         LD      D,H             
4C81: 55         LD      D,L             
4C82: 56         LD      D,(HL)          
4C83: 57         LD      D,A             
4C84: 58         LD      E,B             
4C85: 59         LD      E,C             
4C86: A0         AND     B               
4C87: 5B         LD      E,E             
4C88: 5C         LD      E,H             
4C89: 5D         LD      E,L             
4C8A: 5E         LD      E,(HL)          
4C8B: 5F         LD      E,A             
4C8C: A0         AND     B               
4C8D: A0         AND     B               
4C8E: 00         NOP                     
4C8F: 98         SBC     B               
4C90: C0         RET     NZ              
4C91: 13         INC     DE              
4C92: A0         AND     B               
4C93: A0         AND     B               
4C94: 60         LD      H,B             
4C95: 61         LD      H,C             
4C96: 62         LD      H,D             
4C97: 63         LD      H,E             
4C98: 64         LD      H,H             
4C99: 65         LD      H,L             
4C9A: 66         LD      H,(HL)          
4C9B: 67         LD      H,A             
4C9C: 68         LD      L,B             
4C9D: 69         LD      L,C             
4C9E: 6A         LD      L,D             
4C9F: A0         AND     B               
4CA0: 6C         LD      L,H             
4CA1: 6D         LD      L,L             
4CA2: 6E         LD      L,(HL)          
4CA3: 6F         LD      L,A             
4CA4: A0         AND     B               
4CA5: A0         AND     B               
4CA6: 00         NOP                     
4CA7: 98         SBC     B               
4CA8: E0 13      LDFF00  ($13),A         
4CAA: A0         AND     B               
4CAB: A0         AND     B               
4CAC: A0         AND     B               
4CAD: A0         AND     B               
4CAE: A0         AND     B               
4CAF: A0         AND     B               
4CB0: A0         AND     B               
4CB1: 75         LD      (HL),L          
4CB2: 76         HALT                    
4CB3: 77         LD      (HL),A          
4CB4: 78         LD      A,B             
4CB5: 79         LD      A,C             
4CB6: 7A         LD      A,D             
4CB7: A0         AND     B               
4CB8: A0         AND     B               
4CB9: A0         AND     B               
4CBA: 7E         LD      A,(HL)          
4CBB: AF         XOR     A               
4CBC: A0         AND     B               
4CBD: A0         AND     B               
4CBE: 00         NOP                     
4CBF: FA 00 D0   LD      A,($D000)       
4CC2: FE 0A      CP      $0A             
4CC4: 20 23      JR      NZ,$4CE9        
4CC6: 3E F0      LD      A,$F0           
4CC8: E0 97      LDFF00  ($97),A         
4CCA: CD EB 4A   CALL    $4AEB           
4CCD: 3E 01      LD      A,$01           
4CCF: E0 FF      LDFF00  ($FF),A         
4CD1: 3E 56      LD      A,$56           
4CD3: E0 45      LDFF00  ($45),A         
4CD5: 3E 0C      LD      A,$0C           
4CD7: EA 06 D0   LD      ($D006),A       
4CDA: 3E FF      LD      A,$FF           
4CDC: EA 7F C1   LD      ($C17F),A       
4CDF: 3E 09      LD      A,$09           
4CE1: EA 0E D0   LD      ($D00E),A       
4CE4: 3E 1F      LD      A,$1F           
4CE6: E0 F3      LDFF00  ($F3),A         
4CE8: C9         RET                     
4CE9: 5F         LD      E,A             
4CEA: 3C         INC     A               
4CEB: EA 00 D0   LD      ($D000),A       
4CEE: CB 23      SET     1,E             
4CF0: CB 23      SET     1,E             
4CF2: CB 23      SET     1,E             
4CF4: 7B         LD      A,E             
4CF5: CB 23      SET     1,E             
4CF7: 83         ADD     A,E             
4CF8: 5F         LD      E,A             
4CF9: 16 00      LD      D,$00           
4CFB: 21 CF 4B   LD      HL,$4BCF        
4CFE: 19         ADD     HL,DE           
4CFF: 11 01 D6   LD      DE,$D601        
4D02: 0E 18      LD      C,$18           
4D04: 2A         LD      A,(HLI)         
4D05: 12         LD      (DE),A          
4D06: 13         INC     DE              
4D07: 0D         DEC     C               
4D08: 20 FA      JR      NZ,$4D04        
4D0A: C9         RET                     
4D0B: FF         RST     0X38            
4D0C: FF         RST     0X38            
4D0D: FF         RST     0X38            
4D0E: FF         RST     0X38            
4D0F: BF         CP      A               
4D10: BF         CP      A               
4D11: BF         CP      A               
4D12: BF         CP      A               
4D13: 6B         LD      L,E             
4D14: 6B         LD      L,E             
4D15: 6B         LD      L,E             
4D16: 6B         LD      L,E             
4D17: 27         DAA                     
4D18: 27         DAA                     
4D19: 27         DAA                     
4D1A: 27         DAA                     
4D1B: F0 E7      LD      A,($E7)         
4D1D: E6 03      AND     $03             
4D1F: 5F         LD      E,A             
4D20: FA 0A D0   LD      A,($D00A)       
4D23: 83         ADD     A,E             
4D24: 5F         LD      E,A             
4D25: 16 00      LD      D,$00           
4D27: 21 0B 4D   LD      HL,$4D0B        
4D2A: 19         ADD     HL,DE           
4D2B: 7E         LD      A,(HL)          
4D2C: EA 97 DB   LD      ($DB97),A       
4D2F: FA 06 D0   LD      A,($D006)       
4D32: A7         AND     A               
4D33: 20 10      JR      NZ,$4D45        
4D35: FA 0A D0   LD      A,($D00A)       
4D38: FE 0C      CP      $0C             
4D3A: 28 09      JR      Z,$4D45         
4D3C: 3C         INC     A               
4D3D: EA 0A D0   LD      ($D00A),A       
4D40: 3E 0C      LD      A,$0C           
4D42: EA 06 D0   LD      ($D006),A       
4D45: FA 0A D0   LD      A,($D00A)       
4D48: FE 07      CP      $07             
4D4A: 38 29      JR      C,$4D75         
4D4C: FA 0B D0   LD      A,($D00B)       
4D4F: 3C         INC     A               
4D50: EA 0B D0   LD      ($D00B),A       
4D53: E6 0F      AND     $0F             
4D55: 20 1E      JR      NZ,$4D75        
4D57: FA 05 D0   LD      A,($D005)       
4D5A: C6 20      ADD     $20             
4D5C: EA 05 D0   LD      ($D005),A       
4D5F: 20 14      JR      NZ,$4D75        
4D61: 3E FE      LD      A,$FE           
4D63: EA 7F C1   LD      ($C17F),A       
4D66: CD EB 4A   CALL    $4AEB           
4D69: 3E 40      LD      A,$40           
4D6B: EA 06 D0   LD      ($D006),A       
4D6E: 3E 03      LD      A,$03           
4D70: E0 FF      LDFF00  ($FF),A         
4D72: C3 2B 4A   JP      $4A2B           
4D75: C9         RET                     
4D76: FA 06 D0   LD      A,($D006)       
4D79: A7         AND     A               
4D7A: 20 0C      JR      NZ,$4D88        
4D7C: CD 2B 4A   CALL    $4A2B           
4D7F: 3E D0      LD      A,$D0           
4D81: CD 8F 7A   CALL    $7A8F           
4D84: 3E 17      LD      A,$17           
4D86: E0 F3      LDFF00  ($F3),A         
4D88: C9         RET                     
4D89: FA 9F C1   LD      A,($C19F)       
4D8C: A7         AND     A               
4D8D: 20 03      JR      NZ,$4D92        
4D8F: CD 2B 4A   CALL    $4A2B           
4D92: C9         RET                     
4D93: FA 9F C1   LD      A,($C19F)       
4D96: A7         AND     A               
4D97: 20 1A      JR      NZ,$4DB3        
4D99: 3E 01      LD      A,$01           
4D9B: E0 FF      LDFF00  ($FF),A         
4D9D: 3E FF      LD      A,$FF           
4D9F: EA 7F C1   LD      ($C17F),A       
4DA2: 3E E0      LD      A,$E0           
4DA4: EA 05 D0   LD      ($D005),A       
4DA7: 3E 50      LD      A,$50           
4DA9: EA 06 D0   LD      ($D006),A       
4DAC: 3E 1F      LD      A,$1F           
4DAE: E0 F3      LDFF00  ($F3),A         
4DB0: CD 2B 4A   CALL    $4A2B           
4DB3: C9         RET                     
4DB4: 27         DAA                     
4DB5: 27         DAA                     
4DB6: 27         DAA                     
4DB7: 27         DAA                     
4DB8: 6B         LD      L,E             
4DB9: 6B         LD      L,E             
4DBA: 6B         LD      L,E             
4DBB: 6B         LD      L,E             
4DBC: BF         CP      A               
4DBD: BF         CP      A               
4DBE: BF         CP      A               
4DBF: BF         CP      A               
4DC0: FF         RST     0X38            
4DC1: FF         RST     0X38            
4DC2: FF         RST     0X38            
4DC3: FF         RST     0X38            
4DC4: F0 E7      LD      A,($E7)         
4DC6: E6 03      AND     $03             
4DC8: 5F         LD      E,A             
4DC9: FA 0A D0   LD      A,($D00A)       
4DCC: 83         ADD     A,E             
4DCD: 5F         LD      E,A             
4DCE: 16 00      LD      D,$00           
4DD0: 21 B4 4D   LD      HL,$4DB4        
4DD3: 19         ADD     HL,DE           
4DD4: 7E         LD      A,(HL)          
4DD5: EA 97 DB   LD      ($DB97),A       
4DD8: FA 05 D0   LD      A,($D005)       
4DDB: FE A0      CP      $A0             
4DDD: 30 29      JR      NC,$4E08        
4DDF: FA 06 D0   LD      A,($D006)       
4DE2: A7         AND     A               
4DE3: 20 23      JR      NZ,$4E08        
4DE5: 3E 0C      LD      A,$0C           
4DE7: EA 06 D0   LD      ($D006),A       
4DEA: FA 0A D0   LD      A,($D00A)       
4DED: 3C         INC     A               
4DEE: EA 0A D0   LD      ($D00A),A       
4DF1: FE 0D      CP      $0D             
4DF3: 20 13      JR      NZ,$4E08        
4DF5: AF         XOR     A               
4DF6: EA 7F C1   LD      ($C17F),A       
4DF9: CD EB 4A   CALL    $4AEB           
4DFC: 3E 30      LD      A,$30           
4DFE: EA 06 D0   LD      ($D006),A       
4E01: 3E 01      LD      A,$01           
4E03: E0 FF      LDFF00  ($FF),A         
4E05: C3 2B 4A   JP      $4A2B           
4E08: FA 0B D0   LD      A,($D00B)       
4E0B: 3C         INC     A               
4E0C: EA 0B D0   LD      ($D00B),A       
4E0F: E6 0F      AND     $0F             
4E11: 20 0B      JR      NZ,$4E1E        
4E13: FA 05 D0   LD      A,($D005)       
4E16: A7         AND     A               
4E17: 28 05      JR      Z,$4E1E         
4E19: D6 20      SUB     $20             
4E1B: EA 05 D0   LD      ($D005),A       
4E1E: C9         RET                     
4E1F: 9B         SBC     E               
4E20: C0         RET     NZ              
4E21: 53         LD      D,E             
4E22: A0         AND     B               
4E23: 9B         SBC     E               
4E24: E0 53      LDFF00  ($53),A         
4E26: A0         AND     B               
4E27: 98         SBC     B               
4E28: 00         NOP                     
4E29: 53         LD      D,E             
4E2A: A0         AND     B               
4E2B: 98         SBC     B               
4E2C: 20 53      JR      NZ,$4E81        
4E2E: A0         AND     B               
4E2F: 98         SBC     B               
4E30: 40         LD      B,B             
4E31: 53         LD      D,E             
4E32: A0         AND     B               
4E33: 98         SBC     B               
4E34: 60         LD      H,B             
4E35: 53         LD      D,E             
4E36: A0         AND     B               
4E37: 98         SBC     B               
4E38: 80         ADD     A,B             
4E39: 53         LD      D,E             
4E3A: A0         AND     B               
4E3B: 98         SBC     B               
4E3C: A0         AND     B               
4E3D: 53         LD      D,E             
4E3E: A0         AND     B               
4E3F: 98         SBC     B               
4E40: C0         RET     NZ              
4E41: 53         LD      D,E             
4E42: A0         AND     B               
4E43: 98         SBC     B               
4E44: E0 53      LDFF00  ($53),A         
4E46: A0         AND     B               
4E47: FA 06 D0   LD      A,($D006)       
4E4A: A7         AND     A               
4E4B: C0         RET     NZ              
4E4C: FA 00 D0   LD      A,($D000)       
4E4F: FE 0A      CP      $0A             
4E51: 20 0D      JR      NZ,$4E60        
4E53: 3E D2      LD      A,$D2           
4E55: CD 81 4D   CALL    $4D81           
4E58: 3E 27      LD      A,$27           
4E5A: EA 97 DB   LD      ($DB97),A       
4E5D: C3 2B 4A   JP      $4A2B           
4E60: 5F         LD      E,A             
4E61: 3C         INC     A               
4E62: EA 00 D0   LD      ($D000),A       
4E65: CB 23      SET     1,E             
4E67: CB 23      SET     1,E             
4E69: 16 00      LD      D,$00           
4E6B: 21 1F 4E   LD      HL,$4E1F        
4E6E: 19         ADD     HL,DE           
4E6F: 11 01 D6   LD      DE,$D601        
4E72: 0E 04      LD      C,$04           
4E74: 2A         LD      A,(HLI)         
4E75: 12         LD      (DE),A          
4E76: 13         INC     DE              
4E77: 0D         DEC     C               
4E78: 20 FA      JR      NZ,$4E74        
4E7A: AF         XOR     A               
4E7B: 12         LD      (DE),A          
4E7C: C9         RET                     
4E7D: FA 9F C1   LD      A,($C19F)       
4E80: A7         AND     A               
4E81: 20 0E      JR      NZ,$4E91        
4E83: CD EB 4A   CALL    $4AEB           
4E86: 3E 03      LD      A,$03           
4E88: E0 9D      LDFF00  ($9D),A         
4E8A: 3E 0C      LD      A,$0C           
4E8C: E0 A5      LDFF00  ($A5),A         
4E8E: CD 2B 4A   CALL    $4A2B           
4E91: C9         RET                     
4E92: FA 00 D0   LD      A,($D000)       
4E95: FE 07      CP      $07             
4E97: 20 0B      JR      NZ,$4EA4        
4E99: CD EB 4A   CALL    $4AEB           
4E9C: 3E 80      LD      A,$80           
4E9E: EA 06 D0   LD      ($D006),A       
4EA1: C3 2B 4A   JP      $4A2B           
4EA4: 3C         INC     A               
4EA5: EA 00 D0   LD      ($D000),A       
4EA8: 3E 0C      LD      A,$0C           
4EAA: E0 A5      LDFF00  ($A5),A         
4EAC: C9         RET                     
4EAD: 48         LD      C,B             
4EAE: 58         LD      E,B             
4EAF: 60         LD      H,B             
4EB0: 60         LD      H,B             
4EB1: 58         LD      E,B             
4EB2: 48         LD      C,B             
4EB3: 40         LD      B,B             
4EB4: 40         LD      B,B             
4EB5: 40         LD      B,B             
4EB6: 40         LD      B,B             
4EB7: 48         LD      C,B             
4EB8: 58         LD      E,B             
4EB9: 60         LD      H,B             
4EBA: 60         LD      H,B             
4EBB: 58         LD      E,B             
4EBC: 48         LD      C,B             
4EBD: FF         RST     0X38            
4EBE: 01 02 02   LD      BC,$0202        
4EC1: 01 FF FE   LD      BC,$FEFF        
4EC4: FE FE      CP      $FE             
4EC6: FE FF      CP      $FF             
4EC8: 01 02 02   LD      BC,$0202        
4ECB: 01 FF 00   LD      BC,$00FF        
4ECE: 01 02 03   LD      BC,$0302        
4ED1: 04         INC     B               
4ED2: 05         DEC     B               
4ED3: 06 07      LD      B,$07           
4ED5: 00         NOP                     
4ED6: 08 10 18   LD      ($1810),SP      
4ED9: 20 28      JR      NZ,$4F03        
4EDB: 30 38      JR      NC,$4F15        
4EDD: FA 06 D0   LD      A,($D006)       
4EE0: A7         AND     A               
4EE1: 20 78      JR      NZ,$4F5B        
4EE3: 3E 04      LD      A,$04           
4EE5: E0 9D      LDFF00  ($9D),A         
4EE7: 3E 3F      LD      A,$3F           
4EE9: EA 68 D3   LD      ($D368),A       
4EEC: 3E E8      LD      A,$E8           
4EEE: CD 01 3C   CALL    $3C01           
4EF1: FA 00 D0   LD      A,($D000)       
4EF4: 4F         LD      C,A             
4EF5: 06 00      LD      B,$00           
4EF7: 21 AD 4E   LD      HL,$4EAD        
4EFA: 09         ADD     HL,BC           
4EFB: 7E         LD      A,(HL)          
4EFC: 21 00 C2   LD      HL,$C200        
4EFF: 19         ADD     HL,DE           
4F00: 77         LD      (HL),A          
4F01: 21 B5 4E   LD      HL,$4EB5        
4F04: 09         ADD     HL,BC           
4F05: 7E         LD      A,(HL)          
4F06: 21 10 C2   LD      HL,$C210        
4F09: 19         ADD     HL,DE           
4F0A: D6 20      SUB     $20             
4F0C: 77         LD      (HL),A          
4F0D: 21 BD 4E   LD      HL,$4EBD        
4F10: 09         ADD     HL,BC           
4F11: 7E         LD      A,(HL)          
4F12: 21 40 C2   LD      HL,$C240        
4F15: 19         ADD     HL,DE           
4F16: 77         LD      (HL),A          
4F17: 21 C5 4E   LD      HL,$4EC5        
4F1A: 09         ADD     HL,BC           
4F1B: 7E         LD      A,(HL)          
4F1C: 21 50 C2   LD      HL,$C250        
4F1F: 19         ADD     HL,DE           
4F20: 77         LD      (HL),A          
4F21: 21 CD 4E   LD      HL,$4ECD        
4F24: 09         ADD     HL,BC           
4F25: 7E         LD      A,(HL)          
4F26: 21 B0 C3   LD      HL,$C3B0        
4F29: 19         ADD     HL,DE           
4F2A: 77         LD      (HL),A          
4F2B: 21 D5 4E   LD      HL,$4ED5        
4F2E: 09         ADD     HL,BC           
4F2F: 7E         LD      A,(HL)          
4F30: 21 C0 C2   LD      HL,$C2C0        
4F33: 19         ADD     HL,DE           
4F34: 77         LD      (HL),A          
4F35: 21 B0 C2   LD      HL,$C2B0        
4F38: 19         ADD     HL,DE           
4F39: 36 03      LD      (HL),$03        
4F3B: 21 40 C3   LD      HL,$C340        
4F3E: 19         ADD     HL,DE           
4F3F: 36 C2      LD      (HL),$C2        
4F41: 21 50 C4   LD      HL,$C450        
4F44: 19         ADD     HL,DE           
4F45: 36 20      LD      (HL),$20        
4F47: 79         LD      A,C             
4F48: 3C         INC     A               
4F49: EA 00 D0   LD      ($D000),A       
4F4C: FE 08      CP      $08             
4F4E: 20 9C      JR      NZ,$4EEC        
4F50: CD EB 4A   CALL    $4AEB           
4F53: 3E A0      LD      A,$A0           
4F55: EA 06 D0   LD      ($D006),A       
4F58: CD 2B 4A   CALL    $4A2B           
4F5B: C9         RET                     
4F5C: FA 06 D0   LD      A,($D006)       
4F5F: FE 9E      CP      $9E             
4F61: 20 05      JR      NZ,$4F68        
4F63: 21 F2 FF   LD      HL,$FFF2        
4F66: 36 34      LD      (HL),$34        
4F68: A7         AND     A               
4F69: 20 03      JR      NZ,$4F6E        
4F6B: CD 2B 4A   CALL    $4A2B           
4F6E: C9         RET                     
4F6F: FA 00 D0   LD      A,($D000)       
4F72: C7         RST     0X00            
4F73: D7         RST     0X10            
4F74: 4F         LD      C,A             
4F75: 2A         LD      A,(HLI)         
4F76: 50         LD      D,B             
4F77: 7F         LD      A,A             
4F78: 50         LD      D,B             
4F79: 94         SUB     H               
4F7A: 50         LD      D,B             
4F7B: E1         POP     HL              
4F7C: 50         LD      D,B             
4F7D: EF         RST     0X28            
4F7E: 50         LD      D,B             
4F7F: 3C         INC     A               
4F80: 51         LD      D,C             
4F81: 4A         LD      C,D             
4F82: 51         LD      D,C             
4F83: 75         LD      (HL),L          
4F84: 51         LD      D,C             
4F85: 83         ADD     A,E             
4F86: 51         LD      D,C             
4F87: F2         ???                     
4F88: 51         LD      D,C             
4F89: 00         NOP                     
4F8A: 52         LD      D,D             
4F8B: 1A         LD      A,(DE)          
4F8C: 52         LD      D,D             
4F8D: 22         LD      (HLI),A         
4F8E: 52         LD      D,D             
4F8F: 35         DEC     (HL)            
4F90: 52         LD      D,D             
4F91: 62         LD      H,D             
4F92: 52         LD      D,D             
4F93: 5C         LD      E,H             
4F94: 53         LD      D,E             
4F95: BF         CP      A               
4F96: 53         LD      D,E             
4F97: 21 00 D0   LD      HL,$D000        
4F9A: 34         INC     (HL)            
4F9B: C9         RET                     
4F9C: 1E 10      LD      E,$10           
4F9E: 21 80 C2   LD      HL,$C280        
4FA1: AF         XOR     A               
4FA2: 22         LD      (HLI),A         
4FA3: 1D         DEC     E               
4FA4: 20 FC      JR      NZ,$4FA2        
4FA6: C9         RET                     
4FA7: FF         RST     0X38            
4FA8: FF         RST     0X38            
4FA9: FF         RST     0X38            
4FAA: FF         RST     0X38            
4FAB: AA         XOR     D               
4FAC: AA         XOR     D               
4FAD: AA         XOR     D               
4FAE: AA         XOR     D               
4FAF: 55         LD      D,L             
4FB0: 55         LD      D,L             
4FB1: 55         LD      D,L             
4FB2: 55         LD      D,L             
4FB3: 00         NOP                     
4FB4: 00         NOP                     
4FB5: 00         NOP                     
4FB6: 00         NOP                     
4FB7: 1C         INC     E               
4FB8: 1C         INC     E               
4FB9: 1C         INC     E               
4FBA: 1C         INC     E               
4FBB: 18 18      JR      $4FD5           
4FBD: 18 18      JR      $4FD7           
4FBF: 04         INC     B               
4FC0: 04         INC     B               
4FC1: 04         INC     B               
4FC2: 04         INC     B               
4FC3: 00         NOP                     
4FC4: 00         NOP                     
4FC5: 00         NOP                     
4FC6: 00         NOP                     
4FC7: 90         SUB     B               
4FC8: 90         SUB     B               
4FC9: 90         SUB     B               
4FCA: 90         SUB     B               
4FCB: 50         LD      D,B             
4FCC: 50         LD      D,B             
4FCD: 50         LD      D,B             
4FCE: 50         LD      D,B             
4FCF: 00         NOP                     
4FD0: 00         NOP                     
4FD1: 00         NOP                     
4FD2: 00         NOP                     
4FD3: 00         NOP                     
4FD4: 00         NOP                     
4FD5: 00         NOP                     
4FD6: 00         NOP                     
4FD7: F0 E7      LD      A,($E7)         
4FD9: E6 07      AND     $07             
4FDB: 20 19      JR      NZ,$4FF6        
4FDD: FA 0A D0   LD      A,($D00A)       
4FE0: 3C         INC     A               
4FE1: EA 0A D0   LD      ($D00A),A       
4FE4: FE 0C      CP      $0C             
4FE6: 20 0E      JR      NZ,$4FF6        
4FE8: 3E 1D      LD      A,$1D           
4FEA: EA FE D6   LD      ($D6FE),A       
4FED: AF         XOR     A               
4FEE: E0 97      LDFF00  ($97),A         
4FF0: CD 9C 4F   CALL    $4F9C           
4FF3: C3 97 4F   JP      $4F97           
4FF6: F0 E7      LD      A,($E7)         
4FF8: E6 03      AND     $03             
4FFA: 5F         LD      E,A             
4FFB: FA 0A D0   LD      A,($D00A)       
4FFE: 83         ADD     A,E             
4FFF: 5F         LD      E,A             
5000: 16 00      LD      D,$00           
5002: 21 A7 4F   LD      HL,$4FA7        
5005: 19         ADD     HL,DE           
5006: 7E         LD      A,(HL)          
5007: EA 97 DB   LD      ($DB97),A       
500A: 21 B7 4F   LD      HL,$4FB7        
500D: 19         ADD     HL,DE           
500E: 7E         LD      A,(HL)          
500F: EA 98 DB   LD      ($DB98),A       
5012: 21 C7 4F   LD      HL,$4FC7        
5015: 19         ADD     HL,DE           
5016: 7E         LD      A,(HL)          
5017: EA 99 DB   LD      ($DB99),A       
501A: C9         RET                     
501B: F0 E7      LD      A,($E7)         
501D: 1E 01      LD      E,$01           
501F: E6 04      AND     $04             
5021: 28 02      JR      Z,$5025         
5023: 1E FE      LD      E,$FE           
5025: 21 55 C1   LD      HL,$C155        
5028: 73         LD      (HL),E          
5029: C9         RET                     
502A: AF         XOR     A               
502B: EA 0A D0   LD      ($D00A),A       
502E: 3E 20      LD      A,$20           
5030: EA FF D6   LD      ($D6FF),A       
5033: 3E 6D      LD      A,$6D           
5035: CD 01 3C   CALL    $3C01           
5038: 21 00 C2   LD      HL,$C200        
503B: 19         ADD     HL,DE           
503C: 36 48      LD      (HL),$48        
503E: 21 10 C2   LD      HL,$C210        
5041: 19         ADD     HL,DE           
5042: 36 50      LD      (HL),$50        
5044: 3E 6F      LD      A,$6F           
5046: CD 01 3C   CALL    $3C01           
5049: 21 00 C2   LD      HL,$C200        
504C: 19         ADD     HL,DE           
504D: 36 68      LD      (HL),$68        
504F: 21 10 C2   LD      HL,$C210        
5052: 19         ADD     HL,DE           
5053: 36 30      LD      (HL),$30        
5055: 3E 78      LD      A,$78           
5057: CD 01 3C   CALL    $3C01           
505A: 21 00 C2   LD      HL,$C200        
505D: 19         ADD     HL,DE           
505E: 36 2C      LD      (HL),$2C        
5060: 21 10 C2   LD      HL,$C210        
5063: 19         ADD     HL,DE           
5064: 36 58      LD      (HL),$58        
5066: 3E 78      LD      A,$78           
5068: CD 01 3C   CALL    $3C01           
506B: 21 00 C2   LD      HL,$C200        
506E: 19         ADD     HL,DE           
506F: 36 60      LD      (HL),$60        
5071: 21 10 C2   LD      HL,$C210        
5074: 19         ADD     HL,DE           
5075: 36 52      LD      (HL),$52        
5077: 21 B0 C2   LD      HL,$C2B0        
507A: 19         ADD     HL,DE           
507B: 34         INC     (HL)            
507C: C3 97 4F   JP      $4F97           
507F: CD 9A 52   CALL    $529A           
5082: 20 08      JR      NZ,$508C        
5084: 3E 50      LD      A,$50           
5086: EA 06 D0   LD      ($D006),A       
5089: C3 97 4F   JP      $4F97           
508C: C9         RET                     
508D: F0 CB      LD      A,($CB)         
508F: E6 30      AND     $30             
5091: C0         RET     NZ              
5092: 00         NOP                     
5093: C9         RET                     
5094: FA 06 D0   LD      A,($D006)       
5097: A7         AND     A               
5098: 20 46      JR      NZ,$50E0        
509A: CD 8D 50   CALL    $508D           
509D: CD 04 53   CALL    $5304           
50A0: 20 3E      JR      NZ,$50E0        
50A2: 3E 1E      LD      A,$1E           
50A4: EA FF D6   LD      ($D6FF),A       
50A7: CD 9C 4F   CALL    $4F9C           
50AA: 3E 71      LD      A,$71           
50AC: CD 01 3C   CALL    $3C01           
50AF: 21 00 C2   LD      HL,$C200        
50B2: 19         ADD     HL,DE           
50B3: 36 48      LD      (HL),$48        
50B5: 21 10 C2   LD      HL,$C210        
50B8: 19         ADD     HL,DE           
50B9: 36 50      LD      (HL),$50        
50BB: 21 90 C2   LD      HL,$C290        
50BE: 19         ADD     HL,DE           
50BF: 34         INC     (HL)            
50C0: 21 E0 C2   LD      HL,$C2E0        
50C3: 19         ADD     HL,DE           
50C4: 36 20      LD      (HL),$20        
50C6: 21 80 C3   LD      HL,$C380        
50C9: 19         ADD     HL,DE           
50CA: 36 02      LD      (HL),$02        
50CC: 3E 72      LD      A,$72           
50CE: CD 01 3C   CALL    $3C01           
50D1: 21 00 C2   LD      HL,$C200        
50D4: 19         ADD     HL,DE           
50D5: 36 78      LD      (HL),$78        
50D7: 21 10 C2   LD      HL,$C210        
50DA: 19         ADD     HL,DE           
50DB: 36 50      LD      (HL),$50        
50DD: C3 97 4F   JP      $4F97           
50E0: C9         RET                     
50E1: CD 9A 52   CALL    $529A           
50E4: 20 08      JR      NZ,$50EE        
50E6: 3E 50      LD      A,$50           
50E8: EA 06 D0   LD      ($D006),A       
50EB: C3 97 4F   JP      $4F97           
50EE: C9         RET                     
50EF: FA 06 D0   LD      A,($D006)       
50F2: A7         AND     A               
50F3: 20 46      JR      NZ,$513B        
50F5: CD 8D 50   CALL    $508D           
50F8: CD 04 53   CALL    $5304           
50FB: 20 3E      JR      NZ,$513B        
50FD: 3E 22      LD      A,$22           
50FF: EA FF D6   LD      ($D6FF),A       
5102: CD 9C 4F   CALL    $4F9C           
5105: 3E C5      LD      A,$C5           
5107: CD 01 3C   CALL    $3C01           
510A: 21 00 C2   LD      HL,$C200        
510D: 19         ADD     HL,DE           
510E: 36 28      LD      (HL),$28        
5110: 21 10 C2   LD      HL,$C210        
5113: 19         ADD     HL,DE           
5114: 36 40      LD      (HL),$40        
5116: 3E 09      LD      A,$09           
5118: CD 01 3C   CALL    $3C01           
511B: 21 00 C2   LD      HL,$C200        
511E: 19         ADD     HL,DE           
511F: 36 48      LD      (HL),$48        
5121: 21 10 C2   LD      HL,$C210        
5124: 19         ADD     HL,DE           
5125: 36 50      LD      (HL),$50        
5127: 3E 09      LD      A,$09           
5129: CD 01 3C   CALL    $3C01           
512C: 21 00 C2   LD      HL,$C200        
512F: 19         ADD     HL,DE           
5130: 36 68      LD      (HL),$68        
5132: 21 10 C2   LD      HL,$C210        
5135: 19         ADD     HL,DE           
5136: 36 60      LD      (HL),$60        
5138: C3 97 4F   JP      $4F97           
513B: C9         RET                     
513C: CD 9A 52   CALL    $529A           
513F: 20 08      JR      NZ,$5149        
5141: 3E 50      LD      A,$50           
5143: EA 06 D0   LD      ($D006),A       
5146: C3 97 4F   JP      $4F97           
5149: C9         RET                     
514A: FA 06 D0   LD      A,($D006)       
514D: A7         AND     A               
514E: 20 24      JR      NZ,$5174        
5150: CD 8D 50   CALL    $508D           
5153: CD 04 53   CALL    $5304           
5156: 20 1C      JR      NZ,$5174        
5158: 3E 21      LD      A,$21           
515A: EA FF D6   LD      ($D6FF),A       
515D: CD 9C 4F   CALL    $4F9C           
5160: 3E 3F      LD      A,$3F           
5162: CD 01 3C   CALL    $3C01           
5165: 21 00 C2   LD      HL,$C200        
5168: 19         ADD     HL,DE           
5169: 36 78      LD      (HL),$78        
516B: 21 10 C2   LD      HL,$C210        
516E: 19         ADD     HL,DE           
516F: 36 50      LD      (HL),$50        
5171: C3 97 4F   JP      $4F97           
5174: C9         RET                     
5175: CD 9A 52   CALL    $529A           
5178: 20 08      JR      NZ,$5182        
517A: 3E 50      LD      A,$50           
517C: EA 06 D0   LD      ($D006),A       
517F: C3 97 4F   JP      $4F97           
5182: C9         RET                     
5183: FA 06 D0   LD      A,($D006)       
5186: A7         AND     A               
5187: 20 68      JR      NZ,$51F1        
5189: CD 8D 50   CALL    $508D           
518C: CD 04 53   CALL    $5304           
518F: 20 60      JR      NZ,$51F1        
5191: 3E 1F      LD      A,$1F           
5193: EA FF D6   LD      ($D6FF),A       
5196: CD 9C 4F   CALL    $4F9C           
5199: 3E 3E      LD      A,$3E           
519B: CD 01 3C   CALL    $3C01           
519E: 21 00 C2   LD      HL,$C200        
51A1: 19         ADD     HL,DE           
51A2: 36 28      LD      (HL),$28        
51A4: 21 10 C2   LD      HL,$C210        
51A7: 19         ADD     HL,DE           
51A8: 36 50      LD      (HL),$50        
51AA: 3E 6E      LD      A,$6E           
51AC: CD 01 3C   CALL    $3C01           
51AF: 21 00 C2   LD      HL,$C200        
51B2: 19         ADD     HL,DE           
51B3: 36 18      LD      (HL),$18        
51B5: 21 10 C2   LD      HL,$C210        
51B8: 19         ADD     HL,DE           
51B9: 36 4C      LD      (HL),$4C        
51BB: 3E 6E      LD      A,$6E           
51BD: CD 01 3C   CALL    $3C01           
51C0: 21 00 C2   LD      HL,$C200        
51C3: 19         ADD     HL,DE           
51C4: 36 38      LD      (HL),$38        
51C6: 21 10 C2   LD      HL,$C210        
51C9: 19         ADD     HL,DE           
51CA: 36 54      LD      (HL),$54        
51CC: 3E 6E      LD      A,$6E           
51CE: CD 01 3C   CALL    $3C01           
51D1: 21 00 C2   LD      HL,$C200        
51D4: 19         ADD     HL,DE           
51D5: 36 28      LD      (HL),$28        
51D7: 21 10 C2   LD      HL,$C210        
51DA: 19         ADD     HL,DE           
51DB: 36 30      LD      (HL),$30        
51DD: 3E 6F      LD      A,$6F           
51DF: CD 01 3C   CALL    $3C01           
51E2: 21 00 C2   LD      HL,$C200        
51E5: 19         ADD     HL,DE           
51E6: 36 78      LD      (HL),$78        
51E8: 21 10 C2   LD      HL,$C210        
51EB: 19         ADD     HL,DE           
51EC: 36 60      LD      (HL),$60        
51EE: C3 97 4F   JP      $4F97           
51F1: C9         RET                     
51F2: CD 9A 52   CALL    $529A           
51F5: 20 08      JR      NZ,$51FF        
51F7: 3E C0      LD      A,$C0           
51F9: EA 06 D0   LD      ($D006),A       
51FC: C3 97 4F   JP      $4F97           
51FF: C9         RET                     
5200: FA 06 D0   LD      A,($D006)       
5203: A7         AND     A               
5204: 20 13      JR      NZ,$5219        
5206: CD 8D 50   CALL    $508D           
5209: CD 04 53   CALL    $5304           
520C: 20 0B      JR      NZ,$5219        
520E: 3E 1E      LD      A,$1E           
5210: EA FE D6   LD      ($D6FE),A       
5213: CD 9C 4F   CALL    $4F9C           
5216: C3 97 4F   JP      $4F97           
5219: C9         RET                     
521A: 3E 01      LD      A,$01           
521C: EA FF D6   LD      ($D6FF),A       
521F: C3 97 4F   JP      $4F97           
5222: CD C1 52   CALL    $52C1           
5225: 20 0D      JR      NZ,$5234        
5227: 3E A0      LD      A,$A0           
5229: EA 06 D0   LD      ($D006),A       
522C: 3E FF      LD      A,$FF           
522E: EA 0B D0   LD      ($D00B),A       
5231: C3 97 4F   JP      $4F97           
5234: C9         RET                     
5235: FA 06 D0   LD      A,($D006)       
5238: FE 01      CP      $01             
523A: 20 05      JR      NZ,$5241        
523C: 21 F4 FF   LD      HL,$FFF4        
523F: 36 35      LD      (HL),$35        
5241: A7         AND     A               
5242: 20 35      JR      NZ,$5279        
5244: F0 E7      LD      A,($E7)         
5246: E6 03      AND     $03             
5248: 20 2F      JR      NZ,$5279        
524A: FA 0B D0   LD      A,($D00B)       
524D: FE 3F      CP      $3F             
524F: 28 09      JR      Z,$525A         
5251: 3C         INC     A               
5252: EA 0B D0   LD      ($D00B),A       
5255: 3E 0E      LD      A,$0E           
5257: E0 A5      LDFF00  ($A5),A         
5259: C9         RET                     
525A: 3E 40      LD      A,$40           
525C: EA 06 D0   LD      ($D006),A       
525F: C3 97 4F   JP      $4F97           
5262: FA 06 D0   LD      A,($D006)       
5265: A7         AND     A               
5266: C0         RET     NZ              
5267: AF         XOR     A               
5268: EA 97 DB   LD      ($DB97),A       
526B: EA 98 DB   LD      ($DB98),A       
526E: EA 99 DB   LD      ($DB99),A       
5271: 3E 15      LD      A,$15           
5273: EA FE D6   LD      ($D6FE),A       
5276: C3 97 4F   JP      $4F97           
5279: C9         RET                     
527A: 00         NOP                     
527B: 00         NOP                     
527C: 00         NOP                     
527D: 00         NOP                     
527E: 40         LD      B,B             
527F: 40         LD      B,B             
5280: 40         LD      B,B             
5281: 40         LD      B,B             
5282: 94         SUB     H               
5283: 94         SUB     H               
5284: 94         SUB     H               
5285: 94         SUB     H               
5286: E4         ???                     
5287: E4         ???                     
5288: E4         ???                     
5289: E4         ???                     
528A: 00         NOP                     
528B: 00         NOP                     
528C: 00         NOP                     
528D: 00         NOP                     
528E: 04         INC     B               
528F: 04         INC     B               
5290: 04         INC     B               
5291: 04         INC     B               
5292: 18 18      JR      $52AC           
5294: 18 18      JR      $52AE           
5296: 1C         INC     E               
5297: 1C         INC     E               
5298: 1C         INC     E               
5299: 1C         INC     E               
529A: F0 E7      LD      A,($E7)         
529C: E6 01      AND     $01             
529E: 20 07      JR      NZ,$52A7        
52A0: FA 0A D0   LD      A,($D00A)       
52A3: 3C         INC     A               
52A4: EA 0A D0   LD      ($D00A),A       
52A7: F0 E7      LD      A,($E7)         
52A9: E6 03      AND     $03             
52AB: 5F         LD      E,A             
52AC: FA 0A D0   LD      A,($D00A)       
52AF: 83         ADD     A,E             
52B0: 5F         LD      E,A             
52B1: 16 00      LD      D,$00           
52B3: 21 7A 52   LD      HL,$527A        
52B6: 19         ADD     HL,DE           
52B7: 7E         LD      A,(HL)          
52B8: EA 97 DB   LD      ($DB97),A       
52BB: 21 8A 52   LD      HL,$528A        
52BE: C3 28 53   JP      $5328           
52C1: F0 E7      LD      A,($E7)         
52C3: E6 03      AND     $03             
52C5: 20 07      JR      NZ,$52CE        
52C7: FA 0A D0   LD      A,($D00A)       
52CA: 3C         INC     A               
52CB: EA 0A D0   LD      ($D00A),A       
52CE: F0 E7      LD      A,($E7)         
52D0: E6 03      AND     $03             
52D2: 5F         LD      E,A             
52D3: FA 0A D0   LD      A,($D00A)       
52D6: 83         ADD     A,E             
52D7: 5F         LD      E,A             
52D8: 16 00      LD      D,$00           
52DA: 21 3C 6C   LD      HL,$6C3C        
52DD: 19         ADD     HL,DE           
52DE: 7E         LD      A,(HL)          
52DF: EA 97 DB   LD      ($DB97),A       
52E2: 18 49      JR      $532D           
52E4: E4         ???                     
52E5: E4         ???                     
52E6: E4         ???                     
52E7: E4         ???                     
52E8: 94         SUB     H               
52E9: 94         SUB     H               
52EA: 94         SUB     H               
52EB: 94         SUB     H               
52EC: 40         LD      B,B             
52ED: 40         LD      B,B             
52EE: 40         LD      B,B             
52EF: 40         LD      B,B             
52F0: 00         NOP                     
52F1: 00         NOP                     
52F2: 00         NOP                     
52F3: 00         NOP                     
52F4: 1C         INC     E               
52F5: 1C         INC     E               
52F6: 1C         INC     E               
52F7: 1C         INC     E               
52F8: 18 18      JR      $5312           
52FA: 18 18      JR      $5314           
52FC: 04         INC     B               
52FD: 04         INC     B               
52FE: 04         INC     B               
52FF: 04         INC     B               
5300: 00         NOP                     
5301: 00         NOP                     
5302: 00         NOP                     
5303: 00         NOP                     
5304: F0 E7      LD      A,($E7)         
5306: E6 0F      AND     $0F             
5308: 20 07      JR      NZ,$5311        
530A: FA 0A D0   LD      A,($D00A)       
530D: 3C         INC     A               
530E: EA 0A D0   LD      ($D00A),A       
5311: F0 E7      LD      A,($E7)         
5313: E6 03      AND     $03             
5315: 5F         LD      E,A             
5316: FA 0A D0   LD      A,($D00A)       
5319: 83         ADD     A,E             
531A: 5F         LD      E,A             
531B: 16 00      LD      D,$00           
531D: 21 E4 52   LD      HL,$52E4        
5320: 19         ADD     HL,DE           
5321: 7E         LD      A,(HL)          
5322: EA 97 DB   LD      ($DB97),A       
5325: 21 F4 52   LD      HL,$52F4        
5328: 19         ADD     HL,DE           
5329: 7E         LD      A,(HL)          
532A: EA 98 DB   LD      ($DB98),A       
532D: FA 0A D0   LD      A,($D00A)       
5330: FE 0C      CP      $0C             
5332: 20 04      JR      NZ,$5338        
5334: AF         XOR     A               
5335: EA 0A D0   LD      ($D00A),A       
5338: C9         RET                     
5339: F0 E7      LD      A,($E7)         
533B: E6 07      AND     $07             
533D: 20 07      JR      NZ,$5346        
533F: FA 0A D0   LD      A,($D00A)       
5342: 3C         INC     A               
5343: EA 0A D0   LD      ($D00A),A       
5346: F0 E7      LD      A,($E7)         
5348: E6 03      AND     $03             
534A: 5F         LD      E,A             
534B: FA 0A D0   LD      A,($D00A)       
534E: 83         ADD     A,E             
534F: 5F         LD      E,A             
5350: 16 00      LD      D,$00           
5352: 21 53 5C   LD      HL,$5C53        
5355: 19         ADD     HL,DE           
5356: 7E         LD      A,(HL)          
5357: EA 97 DB   LD      ($DB97),A       
535A: 18 D1      JR      $532D           
535C: 3E C9      LD      A,$C9           
535E: EA 97 DB   LD      ($DB97),A       
5361: 3E 1C      LD      A,$1C           
5363: EA 98 DB   LD      ($DB98),A       
5366: 3E 90      LD      A,$90           
5368: EA 99 DB   LD      ($DB99),A       
536B: FA 06 D0   LD      A,($D006)       
536E: A7         AND     A               
536F: C2 1B 50   JP      NZ,$501B        
5372: 3E 00      LD      A,$00           
5374: EA 55 C1   LD      ($C155),A       
5377: 3E 00      LD      A,$00           
5379: E0 9D      LDFF00  ($9D),A         
537B: 3E 15      LD      A,$15           
537D: EA FE D6   LD      ($D6FE),A       
5380: 3E E8      LD      A,$E8           
5382: CD 01 3C   CALL    $3C01           
5385: 21 00 C2   LD      HL,$C200        
5388: 19         ADD     HL,DE           
5389: 36 40      LD      (HL),$40        
538B: 21 10 C2   LD      HL,$C210        
538E: 19         ADD     HL,DE           
538F: 36 60      LD      (HL),$60        
5391: 21 90 C2   LD      HL,$C290        
5394: 19         ADD     HL,DE           
5395: 36 02      LD      (HL),$02        
5397: 3E E8      LD      A,$E8           
5399: CD 01 3C   CALL    $3C01           
539C: 21 B0 C2   LD      HL,$C2B0        
539F: 19         ADD     HL,DE           
53A0: 34         INC     (HL)            
53A1: 3E 50      LD      A,$50           
53A3: E0 98      LDFF00  ($98),A         
53A5: 21 FD D6   LD      HL,$D6FD        
53A8: CB DE      SET     1,E             
53AA: 3E A0      LD      A,$A0           
53AC: EA 06 D0   LD      ($D006),A       
53AF: 3E FF      LD      A,$FF           
53B1: EA 97 DB   LD      ($DB97),A       
53B4: 3E 5C      LD      A,$5C           
53B6: E0 99      LDFF00  ($99),A         
53B8: 3E 34      LD      A,$34           
53BA: E0 F4      LDFF00  ($F4),A         
53BC: C3 97 4F   JP      $4F97           
53BF: FA 06 D0   LD      A,($D006)       
53C2: A7         AND     A               
53C3: C2 1B 50   JP      NZ,$501B        
53C6: EA 55 C1   LD      ($C155),A       
53C9: CD EB 4A   CALL    $4AEB           
53CC: C3 2B 4A   JP      $4A2B           
53CF: F0 99      LD      A,($99)         
53D1: D6 02      SUB     $02             
53D3: E0 99      LDFF00  ($99),A         
53D5: F0 97      LD      A,($97)         
53D7: C6 08      ADD     $08             
53D9: E0 97      LDFF00  ($97),A         
53DB: FE 60      CP      $60             
53DD: 20 0F      JR      NZ,$53EE        
53DF: FA 9F C2   LD      A,($C29F)       
53E2: 3C         INC     A               
53E3: EA 9F C2   LD      ($C29F),A       
53E6: 3E 40      LD      A,$40           
53E8: EA 09 D0   LD      ($D009),A       
53EB: CD 2B 4A   CALL    $4A2B           
53EE: CD 3D 54   CALL    $543D           
53F1: C9         RET                     
53F2: 43         LD      B,E             
53F3: 13         INC     DE              
53F4: 07         RLCA                    
53F5: 83         ADD     A,E             
53F6: 23         INC     HL              
53F7: 0B         DEC     BC              
53F8: 53         LD      D,E             
53F9: 17         RLA                     
53FA: 47         LD      B,A             
53FB: 27         DAA                     
53FC: 4B         LD      C,E             
53FD: 93         SUB     E               
53FE: 60         LD      H,B             
53FF: 60         LD      H,B             
5400: 61         LD      H,C             
5401: 62         LD      H,D             
5402: 63         LD      H,E             
5403: 64         LD      H,H             
5404: 65         LD      H,L             
5405: 65         LD      H,L             
5406: 65         LD      H,L             
5407: 65         LD      H,L             
5408: 64         LD      H,H             
5409: 63         LD      H,E             
540A: 62         LD      H,D             
540B: 61         LD      H,C             
540C: 60         LD      H,B             
540D: 60         LD      H,B             
540E: CD 3D 54   CALL    $543D           
5411: FA 09 D0   LD      A,($D009)       
5414: A7         AND     A               
5415: 20 03      JR      NZ,$541A        
5417: C3 2B 4A   JP      $4A2B           
541A: FA 1E C2   LD      A,($C21E)       
541D: C6 08      ADD     $08             
541F: EA 1E C2   LD      ($C21E),A       
5422: FA 0A D0   LD      A,($D00A)       
5425: 3C         INC     A               
5426: EA 0A D0   LD      ($D00A),A       
5429: 1F         RRA                     
542A: 1F         RRA                     
542B: 1F         RRA                     
542C: 00         NOP                     
542D: E6 0F      AND     $0F             
542F: 5F         LD      E,A             
5430: 16 00      LD      D,$00           
5432: 21 FE 53   LD      HL,$53FE        
5435: 19         ADD     HL,DE           
5436: 7E         LD      A,(HL)          
5437: E0 97      LDFF00  ($97),A         
5439: CD 71 54   CALL    $5471           
543C: C9         RET                     
543D: F0 E7      LD      A,($E7)         
543F: 1F         RRA                     
5440: 1F         RRA                     
5441: 1F         RRA                     
5442: E6 07      AND     $07             
5444: C6 05      ADD     $05             
5446: E0 9D      LDFF00  ($9D),A         
5448: FA 06 D0   LD      A,($D006)       
544B: A7         AND     A               
544C: 20 14      JR      NZ,$5462        
544E: 3E 03      LD      A,$03           
5450: EA 06 D0   LD      ($D006),A       
5453: FA 00 D0   LD      A,($D000)       
5456: 3C         INC     A               
5457: EA 00 D0   LD      ($D000),A       
545A: FE 03      CP      $03             
545C: 20 04      JR      NZ,$5462        
545E: AF         XOR     A               
545F: EA 00 D0   LD      ($D000),A       
5462: FA 00 D0   LD      A,($D000)       
5465: 5F         LD      E,A             
5466: 16 00      LD      D,$00           
5468: 21 FB 53   LD      HL,$53FB        
546B: 19         ADD     HL,DE           
546C: 7E         LD      A,(HL)          
546D: EA 97 DB   LD      ($DB97),A       
5470: C9         RET                     
5471: F0 97      LD      A,($97)         
5473: 2F         CPL                     
5474: 3C         INC     A               
5475: D6 A0      SUB     $A0             
5477: C6 3C      ADD     $3C             
5479: E0 99      LDFF00  ($99),A         
547B: C9         RET                     
547C: 9C         SBC     H               
547D: 00         NOP                     
547E: 13         INC     DE              
547F: A0         AND     B               
5480: A0         AND     B               
5481: A0         AND     B               
5482: A0         AND     B               
5483: A0         AND     B               
5484: A0         AND     B               
5485: 80         ADD     A,B             
5486: 81         ADD     A,C             
5487: 80         ADD     A,B             
5488: 81         ADD     A,C             
5489: 80         ADD     A,B             
548A: 81         ADD     A,C             
548B: 80         ADD     A,B             
548C: 81         ADD     A,C             
548D: A0         AND     B               
548E: A0         AND     B               
548F: A0         AND     B               
5490: A0         AND     B               
5491: A0         AND     B               
5492: A0         AND     B               
5493: 00         NOP                     
5494: 9C         SBC     H               
5495: 20 13      JR      NZ,$54AA        
5497: A0         AND     B               
5498: A0         AND     B               
5499: A0         AND     B               
549A: A0         AND     B               
549B: A0         AND     B               
549C: A0         AND     B               
549D: 90         SUB     B               
549E: 91         SUB     C               
549F: 90         SUB     B               
54A0: 91         SUB     C               
54A1: 90         SUB     B               
54A2: 91         SUB     C               
54A3: 90         SUB     B               
54A4: 91         SUB     C               
54A5: A0         AND     B               
54A6: A0         AND     B               
54A7: A0         AND     B               
54A8: A0         AND     B               
54A9: A0         AND     B               
54AA: A0         AND     B               
54AB: 00         NOP                     
54AC: 9C         SBC     H               
54AD: 40         LD      B,B             
54AE: 13         INC     DE              
54AF: A0         AND     B               
54B0: A0         AND     B               
54B1: A0         AND     B               
54B2: A0         AND     B               
54B3: A0         AND     B               
54B4: A0         AND     B               
54B5: 80         ADD     A,B             
54B6: 81         ADD     A,C             
54B7: 80         ADD     A,B             
54B8: 81         ADD     A,C             
54B9: 80         ADD     A,B             
54BA: 81         ADD     A,C             
54BB: 80         ADD     A,B             
54BC: 81         ADD     A,C             
54BD: A0         AND     B               
54BE: A0         AND     B               
54BF: A0         AND     B               
54C0: A0         AND     B               
54C1: A0         AND     B               
54C2: A0         AND     B               
54C3: 00         NOP                     
54C4: 9C         SBC     H               
54C5: 60         LD      H,B             
54C6: 13         INC     DE              
54C7: A0         AND     B               
54C8: A0         AND     B               
54C9: A0         AND     B               
54CA: A0         AND     B               
54CB: A0         AND     B               
54CC: A0         AND     B               
54CD: 90         SUB     B               
54CE: 91         SUB     C               
54CF: 90         SUB     B               
54D0: 91         SUB     C               
54D1: 90         SUB     B               
54D2: 91         SUB     C               
54D3: 90         SUB     B               
54D4: 91         SUB     C               
54D5: A0         AND     B               
54D6: A0         AND     B               
54D7: A0         AND     B               
54D8: A0         AND     B               
54D9: A0         AND     B               
54DA: A0         AND     B               
54DB: 00         NOP                     
54DC: 9C         SBC     H               
54DD: 80         ADD     A,B             
54DE: 13         INC     DE              
54DF: A0         AND     B               
54E0: A0         AND     B               
54E1: A0         AND     B               
54E2: A0         AND     B               
54E3: A0         AND     B               
54E4: A0         AND     B               
54E5: 80         ADD     A,B             
54E6: 81         ADD     A,C             
54E7: 80         ADD     A,B             
54E8: 81         ADD     A,C             
54E9: 80         ADD     A,B             
54EA: 81         ADD     A,C             
54EB: 80         ADD     A,B             
54EC: 81         ADD     A,C             
54ED: A0         AND     B               
54EE: A0         AND     B               
54EF: A0         AND     B               
54F0: A0         AND     B               
54F1: A0         AND     B               
54F2: A0         AND     B               
54F3: 00         NOP                     
54F4: 9C         SBC     H               
54F5: A0         AND     B               
54F6: 13         INC     DE              
54F7: A0         AND     B               
54F8: A0         AND     B               
54F9: A0         AND     B               
54FA: A0         AND     B               
54FB: A0         AND     B               
54FC: A0         AND     B               
54FD: 90         SUB     B               
54FE: 91         SUB     C               
54FF: 90         SUB     B               
5500: 91         SUB     C               
5501: 90         SUB     B               
5502: 91         SUB     C               
5503: 90         SUB     B               
5504: 91         SUB     C               
5505: A0         AND     B               
5506: A0         AND     B               
5507: A0         AND     B               
5508: A0         AND     B               
5509: A0         AND     B               
550A: A0         AND     B               
550B: 00         NOP                     
550C: 9C         SBC     H               
550D: C0         RET     NZ              
550E: 13         INC     DE              
550F: A0         AND     B               
5510: A0         AND     B               
5511: A0         AND     B               
5512: A0         AND     B               
5513: A0         AND     B               
5514: A0         AND     B               
5515: 80         ADD     A,B             
5516: 81         ADD     A,C             
5517: 80         ADD     A,B             
5518: 81         ADD     A,C             
5519: 80         ADD     A,B             
551A: 81         ADD     A,C             
551B: 80         ADD     A,B             
551C: 81         ADD     A,C             
551D: A0         AND     B               
551E: A0         AND     B               
551F: A0         AND     B               
5520: A0         AND     B               
5521: A0         AND     B               
5522: A0         AND     B               
5523: 00         NOP                     
5524: 9C         SBC     H               
5525: E0 13      LDFF00  ($13),A         
5527: A0         AND     B               
5528: A0         AND     B               
5529: A0         AND     B               
552A: A0         AND     B               
552B: A0         AND     B               
552C: A0         AND     B               
552D: 90         SUB     B               
552E: 91         SUB     C               
552F: 90         SUB     B               
5530: 91         SUB     C               
5531: 90         SUB     B               
5532: 91         SUB     C               
5533: 90         SUB     B               
5534: 91         SUB     C               
5535: A0         AND     B               
5536: A0         AND     B               
5537: A0         AND     B               
5538: A0         AND     B               
5539: A0         AND     B               
553A: A0         AND     B               
553B: 00         NOP                     
553C: 9D         SBC     L               
553D: 00         NOP                     
553E: 13         INC     DE              
553F: A0         AND     B               
5540: A0         AND     B               
5541: A0         AND     B               
5542: A0         AND     B               
5543: A0         AND     B               
5544: A0         AND     B               
5545: 80         ADD     A,B             
5546: 81         ADD     A,C             
5547: 80         ADD     A,B             
5548: 81         ADD     A,C             
5549: 80         ADD     A,B             
554A: 81         ADD     A,C             
554B: 80         ADD     A,B             
554C: 81         ADD     A,C             
554D: A0         AND     B               
554E: A0         AND     B               
554F: A0         AND     B               
5550: A0         AND     B               
5551: A0         AND     B               
5552: A0         AND     B               
5553: 00         NOP                     
5554: 9D         SBC     L               
5555: 20 13      JR      NZ,$556A        
5557: A0         AND     B               
5558: A0         AND     B               
5559: A0         AND     B               
555A: A0         AND     B               
555B: A0         AND     B               
555C: A0         AND     B               
555D: 90         SUB     B               
555E: 91         SUB     C               
555F: 90         SUB     B               
5560: 91         SUB     C               
5561: 90         SUB     B               
5562: 91         SUB     C               
5563: 90         SUB     B               
5564: 91         SUB     C               
5565: A0         AND     B               
5566: A0         AND     B               
5567: A0         AND     B               
5568: A0         AND     B               
5569: A0         AND     B               
556A: A0         AND     B               
556B: 00         NOP                     
556C: 9D         SBC     L               
556D: 40         LD      B,B             
556E: 13         INC     DE              
556F: A0         AND     B               
5570: A0         AND     B               
5571: A0         AND     B               
5572: A0         AND     B               
5573: A0         AND     B               
5574: A0         AND     B               
5575: 80         ADD     A,B             
5576: 81         ADD     A,C             
5577: 80         ADD     A,B             
5578: 81         ADD     A,C             
5579: 80         ADD     A,B             
557A: 81         ADD     A,C             
557B: 80         ADD     A,B             
557C: 81         ADD     A,C             
557D: A0         AND     B               
557E: A0         AND     B               
557F: A0         AND     B               
5580: A0         AND     B               
5581: A0         AND     B               
5582: A0         AND     B               
5583: 00         NOP                     
5584: 9D         SBC     L               
5585: 60         LD      H,B             
5586: 13         INC     DE              
5587: A0         AND     B               
5588: A0         AND     B               
5589: A0         AND     B               
558A: A0         AND     B               
558B: A0         AND     B               
558C: A0         AND     B               
558D: 90         SUB     B               
558E: 91         SUB     C               
558F: 90         SUB     B               
5590: 91         SUB     C               
5591: 90         SUB     B               
5592: 91         SUB     C               
5593: 90         SUB     B               
5594: 91         SUB     C               
5595: A0         AND     B               
5596: A0         AND     B               
5597: A0         AND     B               
5598: A0         AND     B               
5599: A0         AND     B               
559A: A0         AND     B               
559B: 00         NOP                     
559C: 9D         SBC     L               
559D: 80         ADD     A,B             
559E: 13         INC     DE              
559F: A0         AND     B               
55A0: A0         AND     B               
55A1: A0         AND     B               
55A2: A0         AND     B               
55A3: A0         AND     B               
55A4: A0         AND     B               
55A5: 80         ADD     A,B             
55A6: 81         ADD     A,C             
55A7: 80         ADD     A,B             
55A8: 81         ADD     A,C             
55A9: 80         ADD     A,B             
55AA: 81         ADD     A,C             
55AB: 80         ADD     A,B             
55AC: 81         ADD     A,C             
55AD: A0         AND     B               
55AE: A0         AND     B               
55AF: A0         AND     B               
55B0: A0         AND     B               
55B1: A0         AND     B               
55B2: A0         AND     B               
55B3: 00         NOP                     
55B4: 9D         SBC     L               
55B5: A0         AND     B               
55B6: 13         INC     DE              
55B7: A0         AND     B               
55B8: A0         AND     B               
55B9: A0         AND     B               
55BA: A0         AND     B               
55BB: A0         AND     B               
55BC: A0         AND     B               
55BD: 90         SUB     B               
55BE: 91         SUB     C               
55BF: 90         SUB     B               
55C0: 91         SUB     C               
55C1: 90         SUB     B               
55C2: 91         SUB     C               
55C3: 90         SUB     B               
55C4: 91         SUB     C               
55C5: A0         AND     B               
55C6: A0         AND     B               
55C7: A0         AND     B               
55C8: A0         AND     B               
55C9: A0         AND     B               
55CA: A0         AND     B               
55CB: 00         NOP                     
55CC: 9D         SBC     L               
55CD: C0         RET     NZ              
55CE: 13         INC     DE              
55CF: A0         AND     B               
55D0: A0         AND     B               
55D1: A0         AND     B               
55D2: A0         AND     B               
55D3: A0         AND     B               
55D4: A0         AND     B               
55D5: 80         ADD     A,B             
55D6: 81         ADD     A,C             
55D7: 80         ADD     A,B             
55D8: 81         ADD     A,C             
55D9: 80         ADD     A,B             
55DA: 81         ADD     A,C             
55DB: 80         ADD     A,B             
55DC: 81         ADD     A,C             
55DD: A0         AND     B               
55DE: A0         AND     B               
55DF: A0         AND     B               
55E0: A0         AND     B               
55E1: A0         AND     B               
55E2: A0         AND     B               
55E3: 00         NOP                     
55E4: 9D         SBC     L               
55E5: E0 13      LDFF00  ($13),A         
55E7: A0         AND     B               
55E8: A0         AND     B               
55E9: A0         AND     B               
55EA: A0         AND     B               
55EB: A0         AND     B               
55EC: A0         AND     B               
55ED: 90         SUB     B               
55EE: 91         SUB     C               
55EF: 90         SUB     B               
55F0: 91         SUB     C               
55F1: 90         SUB     B               
55F2: 91         SUB     C               
55F3: 90         SUB     B               
55F4: 91         SUB     C               
55F5: A0         AND     B               
55F6: A0         AND     B               
55F7: A0         AND     B               
55F8: A0         AND     B               
55F9: A0         AND     B               
55FA: A0         AND     B               
55FB: 00         NOP                     
55FC: 9E         SBC     (HL)            
55FD: 00         NOP                     
55FE: 13         INC     DE              
55FF: A0         AND     B               
5600: A0         AND     B               
5601: A0         AND     B               
5602: A0         AND     B               
5603: A0         AND     B               
5604: A0         AND     B               
5605: 80         ADD     A,B             
5606: 81         ADD     A,C             
5607: 80         ADD     A,B             
5608: 81         ADD     A,C             
5609: 80         ADD     A,B             
560A: 81         ADD     A,C             
560B: 80         ADD     A,B             
560C: 81         ADD     A,C             
560D: A0         AND     B               
560E: A0         AND     B               
560F: A0         AND     B               
5610: A0         AND     B               
5611: A0         AND     B               
5612: A0         AND     B               
5613: 00         NOP                     
5614: 9E         SBC     (HL)            
5615: 20 13      JR      NZ,$562A        
5617: A0         AND     B               
5618: A0         AND     B               
5619: A0         AND     B               
561A: A0         AND     B               
561B: A0         AND     B               
561C: A0         AND     B               
561D: 90         SUB     B               
561E: 91         SUB     C               
561F: 90         SUB     B               
5620: 91         SUB     C               
5621: 90         SUB     B               
5622: 91         SUB     C               
5623: 90         SUB     B               
5624: 91         SUB     C               
5625: A0         AND     B               
5626: A0         AND     B               
5627: A0         AND     B               
5628: A0         AND     B               
5629: A0         AND     B               
562A: A0         AND     B               
562B: 00         NOP                     
562C: 9E         SBC     (HL)            
562D: 40         LD      B,B             
562E: 13         INC     DE              
562F: A0         AND     B               
5630: A0         AND     B               
5631: A0         AND     B               
5632: A0         AND     B               
5633: A0         AND     B               
5634: A0         AND     B               
5635: 80         ADD     A,B             
5636: 81         ADD     A,C             
5637: 80         ADD     A,B             
5638: 81         ADD     A,C             
5639: 80         ADD     A,B             
563A: 81         ADD     A,C             
563B: 80         ADD     A,B             
563C: 81         ADD     A,C             
563D: A0         AND     B               
563E: A0         AND     B               
563F: A0         AND     B               
5640: A0         AND     B               
5641: A0         AND     B               
5642: A0         AND     B               
5643: 00         NOP                     
5644: 9E         SBC     (HL)            
5645: 60         LD      H,B             
5646: 13         INC     DE              
5647: A0         AND     B               
5648: A0         AND     B               
5649: A0         AND     B               
564A: A0         AND     B               
564B: A0         AND     B               
564C: A0         AND     B               
564D: 90         SUB     B               
564E: 91         SUB     C               
564F: 90         SUB     B               
5650: 91         SUB     C               
5651: 90         SUB     B               
5652: 91         SUB     C               
5653: 90         SUB     B               
5654: 91         SUB     C               
5655: A0         AND     B               
5656: A0         AND     B               
5657: A0         AND     B               
5658: A0         AND     B               
5659: A0         AND     B               
565A: A0         AND     B               
565B: 00         NOP                     
565C: 9E         SBC     (HL)            
565D: 80         ADD     A,B             
565E: 13         INC     DE              
565F: A0         AND     B               
5660: A0         AND     B               
5661: A0         AND     B               
5662: A0         AND     B               
5663: A0         AND     B               
5664: A0         AND     B               
5665: 80         ADD     A,B             
5666: 81         ADD     A,C             
5667: 80         ADD     A,B             
5668: 81         ADD     A,C             
5669: 80         ADD     A,B             
566A: 81         ADD     A,C             
566B: 80         ADD     A,B             
566C: 81         ADD     A,C             
566D: A0         AND     B               
566E: A0         AND     B               
566F: A0         AND     B               
5670: A0         AND     B               
5671: A0         AND     B               
5672: A0         AND     B               
5673: 00         NOP                     
5674: 9E         SBC     (HL)            
5675: A0         AND     B               
5676: 13         INC     DE              
5677: A0         AND     B               
5678: A0         AND     B               
5679: A0         AND     B               
567A: A0         AND     B               
567B: A0         AND     B               
567C: A0         AND     B               
567D: 90         SUB     B               
567E: 91         SUB     C               
567F: 90         SUB     B               
5680: 91         SUB     C               
5681: 90         SUB     B               
5682: 91         SUB     C               
5683: 90         SUB     B               
5684: 91         SUB     C               
5685: A0         AND     B               
5686: A0         AND     B               
5687: A0         AND     B               
5688: A0         AND     B               
5689: A0         AND     B               
568A: A0         AND     B               
568B: 00         NOP                     
568C: 9E         SBC     (HL)            
568D: C0         RET     NZ              
568E: 13         INC     DE              
568F: A0         AND     B               
5690: A0         AND     B               
5691: A0         AND     B               
5692: A0         AND     B               
5693: A0         AND     B               
5694: A0         AND     B               
5695: 80         ADD     A,B             
5696: 81         ADD     A,C             
5697: 80         ADD     A,B             
5698: 81         ADD     A,C             
5699: 80         ADD     A,B             
569A: 81         ADD     A,C             
569B: 80         ADD     A,B             
569C: 81         ADD     A,C             
569D: A0         AND     B               
569E: A0         AND     B               
569F: A0         AND     B               
56A0: A0         AND     B               
56A1: A0         AND     B               
56A2: A0         AND     B               
56A3: 00         NOP                     
56A4: 9E         SBC     (HL)            
56A5: E0 13      LDFF00  ($13),A         
56A7: A0         AND     B               
56A8: A0         AND     B               
56A9: A0         AND     B               
56AA: A0         AND     B               
56AB: A0         AND     B               
56AC: A0         AND     B               
56AD: 90         SUB     B               
56AE: 91         SUB     C               
56AF: 90         SUB     B               
56B0: 91         SUB     C               
56B1: 90         SUB     B               
56B2: 91         SUB     C               
56B3: 90         SUB     B               
56B4: 91         SUB     C               
56B5: A0         AND     B               
56B6: A0         AND     B               
56B7: A0         AND     B               
56B8: A0         AND     B               
56B9: A0         AND     B               
56BA: A0         AND     B               
56BB: 00         NOP                     
56BC: 9F         SBC     A               
56BD: 00         NOP                     
56BE: 13         INC     DE              
56BF: A0         AND     B               
56C0: A0         AND     B               
56C1: A0         AND     B               
56C2: A0         AND     B               
56C3: A0         AND     B               
56C4: A0         AND     B               
56C5: 80         ADD     A,B             
56C6: 81         ADD     A,C             
56C7: 80         ADD     A,B             
56C8: 81         ADD     A,C             
56C9: 80         ADD     A,B             
56CA: 81         ADD     A,C             
56CB: 80         ADD     A,B             
56CC: 81         ADD     A,C             
56CD: A0         AND     B               
56CE: A0         AND     B               
56CF: A0         AND     B               
56D0: A0         AND     B               
56D1: A0         AND     B               
56D2: A0         AND     B               
56D3: 00         NOP                     
56D4: 9F         SBC     A               
56D5: 20 13      JR      NZ,$56EA        
56D7: A0         AND     B               
56D8: A0         AND     B               
56D9: A0         AND     B               
56DA: A0         AND     B               
56DB: A0         AND     B               
56DC: A0         AND     B               
56DD: 90         SUB     B               
56DE: 91         SUB     C               
56DF: 90         SUB     B               
56E0: 91         SUB     C               
56E1: 90         SUB     B               
56E2: 91         SUB     C               
56E3: 90         SUB     B               
56E4: 91         SUB     C               
56E5: A0         AND     B               
56E6: A0         AND     B               
56E7: A0         AND     B               
56E8: A0         AND     B               
56E9: A0         AND     B               
56EA: A0         AND     B               
56EB: 00         NOP                     
56EC: 9F         SBC     A               
56ED: 40         LD      B,B             
56EE: 13         INC     DE              
56EF: A0         AND     B               
56F0: A0         AND     B               
56F1: A0         AND     B               
56F2: A0         AND     B               
56F3: A0         AND     B               
56F4: A0         AND     B               
56F5: 80         ADD     A,B             
56F6: 81         ADD     A,C             
56F7: 80         ADD     A,B             
56F8: 81         ADD     A,C             
56F9: 80         ADD     A,B             
56FA: 81         ADD     A,C             
56FB: 80         ADD     A,B             
56FC: 81         ADD     A,C             
56FD: A0         AND     B               
56FE: A0         AND     B               
56FF: A0         AND     B               
5700: A0         AND     B               
5701: A0         AND     B               
5702: A0         AND     B               
5703: 00         NOP                     
5704: 9F         SBC     A               
5705: 60         LD      H,B             
5706: 13         INC     DE              
5707: A0         AND     B               
5708: A0         AND     B               
5709: A0         AND     B               
570A: A0         AND     B               
570B: A0         AND     B               
570C: A0         AND     B               
570D: 90         SUB     B               
570E: 91         SUB     C               
570F: 90         SUB     B               
5710: 91         SUB     C               
5711: 90         SUB     B               
5712: 91         SUB     C               
5713: 90         SUB     B               
5714: 91         SUB     C               
5715: A0         AND     B               
5716: A0         AND     B               
5717: A0         AND     B               
5718: A0         AND     B               
5719: A0         AND     B               
571A: A0         AND     B               
571B: 00         NOP                     
571C: 9F         SBC     A               
571D: 80         ADD     A,B             
571E: 13         INC     DE              
571F: A0         AND     B               
5720: A0         AND     B               
5721: A0         AND     B               
5722: A0         AND     B               
5723: A0         AND     B               
5724: A0         AND     B               
5725: 80         ADD     A,B             
5726: 81         ADD     A,C             
5727: 80         ADD     A,B             
5728: 81         ADD     A,C             
5729: 80         ADD     A,B             
572A: 81         ADD     A,C             
572B: 80         ADD     A,B             
572C: 81         ADD     A,C             
572D: A0         AND     B               
572E: A0         AND     B               
572F: A0         AND     B               
5730: A0         AND     B               
5731: A0         AND     B               
5732: A0         AND     B               
5733: 00         NOP                     
5734: 9F         SBC     A               
5735: A0         AND     B               
5736: 13         INC     DE              
5737: A0         AND     B               
5738: A0         AND     B               
5739: A0         AND     B               
573A: A0         AND     B               
573B: A0         AND     B               
573C: A0         AND     B               
573D: 90         SUB     B               
573E: 91         SUB     C               
573F: 90         SUB     B               
5740: 91         SUB     C               
5741: 90         SUB     B               
5742: 91         SUB     C               
5743: 90         SUB     B               
5744: 91         SUB     C               
5745: A0         AND     B               
5746: A0         AND     B               
5747: A0         AND     B               
5748: A0         AND     B               
5749: A0         AND     B               
574A: A0         AND     B               
574B: 00         NOP                     
574C: 9F         SBC     A               
574D: C0         RET     NZ              
574E: 13         INC     DE              
574F: A0         AND     B               
5750: A0         AND     B               
5751: A0         AND     B               
5752: A0         AND     B               
5753: A0         AND     B               
5754: A0         AND     B               
5755: 80         ADD     A,B             
5756: 81         ADD     A,C             
5757: 80         ADD     A,B             
5758: 81         ADD     A,C             
5759: 80         ADD     A,B             
575A: 81         ADD     A,C             
575B: 80         ADD     A,B             
575C: 81         ADD     A,C             
575D: A0         AND     B               
575E: A0         AND     B               
575F: A0         AND     B               
5760: A0         AND     B               
5761: A0         AND     B               
5762: A0         AND     B               
5763: 00         NOP                     
5764: 9F         SBC     A               
5765: E0 13      LDFF00  ($13),A         
5767: A0         AND     B               
5768: A0         AND     B               
5769: A0         AND     B               
576A: A0         AND     B               
576B: A0         AND     B               
576C: A0         AND     B               
576D: 90         SUB     B               
576E: 91         SUB     C               
576F: 90         SUB     B               
5770: 91         SUB     C               
5771: 90         SUB     B               
5772: 91         SUB     C               
5773: 90         SUB     B               
5774: 91         SUB     C               
5775: A0         AND     B               
5776: A0         AND     B               
5777: A0         AND     B               
5778: A0         AND     B               
5779: A0         AND     B               
577A: A0         AND     B               
577B: 00         NOP                     
577C: CD 3D 54   CALL    $543D           
577F: FA 1E C2   LD      A,($C21E)       
5782: C6 04      ADD     $04             
5784: EA 1E C2   LD      ($C21E),A       
5787: FA 0B D0   LD      A,($D00B)       
578A: 3C         INC     A               
578B: EA 0B D0   LD      ($D00B),A       
578E: E6 07      AND     $07             
5790: 20 0B      JR      NZ,$579D        
5792: FA 0C D0   LD      A,($D00C)       
5795: FE 08      CP      $08             
5797: 28 04      JR      Z,$579D         
5799: 3C         INC     A               
579A: EA 0C D0   LD      ($D00C),A       
579D: FA 0C D0   LD      A,($D00C)       
57A0: 5F         LD      E,A             
57A1: F0 97      LD      A,($97)         
57A3: 83         ADD     A,E             
57A4: E0 97      LDFF00  ($97),A         
57A6: CD 71 54   CALL    $5471           
57A9: F0 99      LD      A,($99)         
57AB: FE F0      CP      $F0             
57AD: 38 04      JR      C,$57B3         
57AF: AF         XOR     A               
57B0: EA 8F C2   LD      ($C28F),A       
57B3: FA 0B D0   LD      A,($D00B)       
57B6: E6 01      AND     $01             
57B8: C0         RET     NZ              
57B9: FA 01 D0   LD      A,($D001)       
57BC: FE 20      CP      $20             
57BE: 20 07      JR      NZ,$57C7        
57C0: CD EB 4A   CALL    $4AEB           
57C3: CD 2B 4A   CALL    $4A2B           
57C6: C9         RET                     
57C7: 5F         LD      E,A             
57C8: 3C         INC     A               
57C9: EA 01 D0   LD      ($D001),A       
57CC: 16 00      LD      D,$00           
57CE: CB 23      SET     1,E             
57D0: CB 12      SET     1,E             
57D2: CB 23      SET     1,E             
57D4: CB 12      SET     1,E             
57D6: CB 23      SET     1,E             
57D8: CB 12      SET     1,E             
57DA: 7B         LD      A,E             
57DB: CB 23      SET     1,E             
57DD: CB 12      SET     1,E             
57DF: 83         ADD     A,E             
57E0: 5F         LD      E,A             
57E1: 7A         LD      A,D             
57E2: CE 00      ADC     $00             
57E4: 57         LD      D,A             
57E5: 21 7C 54   LD      HL,$547C        
57E8: 19         ADD     HL,DE           
57E9: 11 01 D6   LD      DE,$D601        
57EC: 0E 18      LD      C,$18           
57EE: 2A         LD      A,(HLI)         
57EF: 12         LD      (DE),A          
57F0: 13         INC     DE              
57F1: 0D         DEC     C               
57F2: 20 FA      JR      NZ,$57EE        
57F4: C9         RET                     
57F5: 27         DAA                     
57F6: 27         DAA                     
57F7: 27         DAA                     
57F8: 27         DAA                     
57F9: 16 16      LD      D,$16           
57FB: 16 16      LD      D,$16           
57FD: 01 01 01   LD      BC,$0101        
5800: 01 00 00   LD      BC,$0000        
5803: 00         NOP                     
5804: 00         NOP                     
5805: 1C         INC     E               
5806: 1C         INC     E               
5807: 1C         INC     E               
5808: 1C         INC     E               
5809: 1C         INC     E               
580A: 1C         INC     E               
580B: 18 18      JR      $5825           
580D: 08 08 08   LD      ($0808),SP      
5810: 08 00 00   LD      ($0000),SP      
5813: 00         NOP                     
5814: 00         NOP                     
5815: 90         SUB     B               
5816: 90         SUB     B               
5817: 90         SUB     B               
5818: 90         SUB     B               
5819: 50         LD      D,B             
581A: 50         LD      D,B             
581B: 50         LD      D,B             
581C: 50         LD      D,B             
581D: 00         NOP                     
581E: 00         NOP                     
581F: 00         NOP                     
5820: 00         NOP                     
5821: 00         NOP                     
5822: 00         NOP                     
5823: 00         NOP                     
5824: 00         NOP                     
5825: FA 1E C2   LD      A,($C21E)       
5828: C6 02      ADD     $02             
582A: EA 1E C2   LD      ($C21E),A       
582D: F0 97      LD      A,($97)         
582F: C6 04      ADD     $04             
5831: E0 97      LDFF00  ($97),A         
5833: F0 E7      LD      A,($E7)         
5835: E6 07      AND     $07             
5837: 20 16      JR      NZ,$584F        
5839: FA 0A D0   LD      A,($D00A)       
583C: FE 0C      CP      $0C             
583E: 20 0B      JR      NZ,$584B        
5840: CD EB 4A   CALL    $4AEB           
5843: 3E C0      LD      A,$C0           
5845: EA 06 D0   LD      ($D006),A       
5848: C3 2B 4A   JP      $4A2B           
584B: 3C         INC     A               
584C: EA 0A D0   LD      ($D00A),A       
584F: F0 E7      LD      A,($E7)         
5851: E6 03      AND     $03             
5853: 5F         LD      E,A             
5854: FA 0A D0   LD      A,($D00A)       
5857: 83         ADD     A,E             
5858: 5F         LD      E,A             
5859: 16 00      LD      D,$00           
585B: 21 F5 57   LD      HL,$57F5        
585E: 19         ADD     HL,DE           
585F: 7E         LD      A,(HL)          
5860: EA 97 DB   LD      ($DB97),A       
5863: 21 05 58   LD      HL,$5805        
5866: 19         ADD     HL,DE           
5867: 7E         LD      A,(HL)          
5868: EA 98 DB   LD      ($DB98),A       
586B: 21 15 58   LD      HL,$5815        
586E: 19         ADD     HL,DE           
586F: 7E         LD      A,(HL)          
5870: EA 99 DB   LD      ($DB99),A       
5873: C9         RET                     
5874: FA 06 D0   LD      A,($D006)       
5877: A7         AND     A               
5878: 20 1B      JR      NZ,$5895        
587A: AF         XOR     A               
587B: EA 0E D0   LD      ($D00E),A       
587E: EA 8E C2   LD      ($C28E),A       
5881: EA 8F C2   LD      ($C28F),A       
5884: EA 14 C1   LD      ($C114),A       
5887: 3E 80      LD      A,$80           
5889: EA 66 D4   LD      ($D466),A       
588C: 21 FD D6   LD      HL,$D6FD        
588F: CB 9E      SET     1,E             
5891: 21 96 DB   LD      HL,$DB96        
5894: 34         INC     (HL)            
5895: C9         RET                     
5896: CD 02 46   CALL    $4602           
5899: 11 E0 98   LD      DE,$98E0        
589C: CD 55 46   CALL    $4655           
589F: CD 13 0B   CALL    $0B13           
58A2: FA 0E D0   LD      A,($D00E)       
58A5: C7         RST     0X00            
58A6: AE         XOR     (HL)            
58A7: 58         LD      E,B             
58A8: B9         CP      C               
58A9: 58         LD      E,B             
58AA: 2B         DEC     HL              
58AB: 59         LD      E,C             
58AC: 36 59      LD      (HL),$59        
58AE: 3E 16      LD      A,$16           
58B0: EA FE D6   LD      ($D6FE),A       
58B3: CD EB 4A   CALL    $4AEB           
58B6: C3 2B 4A   JP      $4A2B           
58B9: 3E 17      LD      A,$17           
58BB: EA FF D6   LD      ($D6FF),A       
58BE: 3E E8      LD      A,$E8           
58C0: CD 01 3C   CALL    $3C01           
58C3: 21 00 C2   LD      HL,$C200        
58C6: 19         ADD     HL,DE           
58C7: 36 48      LD      (HL),$48        
58C9: 21 10 C2   LD      HL,$C210        
58CC: 19         ADD     HL,DE           
58CD: 36 60      LD      (HL),$60        
58CF: 21 B0 C2   LD      HL,$C2B0        
58D2: 19         ADD     HL,DE           
58D3: 36 04      LD      (HL),$04        
58D5: 3E E8      LD      A,$E8           
58D7: CD 01 3C   CALL    $3C01           
58DA: 21 00 C2   LD      HL,$C200        
58DD: 19         ADD     HL,DE           
58DE: 36 28      LD      (HL),$28        
58E0: 21 10 C2   LD      HL,$C210        
58E3: 19         ADD     HL,DE           
58E4: 36 68      LD      (HL),$68        
58E6: 21 B0 C2   LD      HL,$C2B0        
58E9: 19         ADD     HL,DE           
58EA: 36 05      LD      (HL),$05        
58EC: 3E E8      LD      A,$E8           
58EE: CD 01 3C   CALL    $3C01           
58F1: 21 00 C2   LD      HL,$C200        
58F4: 19         ADD     HL,DE           
58F5: 36 78      LD      (HL),$78        
58F7: 21 10 C2   LD      HL,$C210        
58FA: 19         ADD     HL,DE           
58FB: 36 60      LD      (HL),$60        
58FD: 21 B0 C2   LD      HL,$C2B0        
5900: 19         ADD     HL,DE           
5901: 36 05      LD      (HL),$05        
5903: 21 B0 C3   LD      HL,$C3B0        
5906: 19         ADD     HL,DE           
5907: 34         INC     (HL)            
5908: C3 2B 4A   JP      $4A2B           
590B: 00         NOP                     
590C: 00         NOP                     
590D: 00         NOP                     
590E: 00         NOP                     
590F: 05         DEC     B               
5910: 05         DEC     B               
5911: 05         DEC     B               
5912: 05         DEC     B               
5913: 19         ADD     HL,DE           
5914: 19         ADD     HL,DE           
5915: 1A         LD      A,(DE)          
5916: 1A         LD      A,(DE)          
5917: 1E 1E      LD      E,$1E           
5919: 1E 1E      LD      E,$1E           
591B: 00         NOP                     
591C: 00         NOP                     
591D: 00         NOP                     
591E: 00         NOP                     
591F: 00         NOP                     
5920: 01 01 01   LD      BC,$0101        
5923: 51         LD      D,C             
5924: 51         LD      D,C             
5925: 52         LD      D,D             
5926: 52         LD      D,D             
5927: 92         SUB     D               
5928: 92         SUB     D               
5929: 92         SUB     D               
592A: 92         SUB     D               
592B: CD EB 4A   CALL    $4AEB           
592E: 3E 60      LD      A,$60           
5930: EA 09 D0   LD      ($D009),A       
5933: C3 2B 4A   JP      $4A2B           
5936: FA 09 D0   LD      A,($D009)       
5939: A7         AND     A               
593A: 20 14      JR      NZ,$5950        
593C: AF         XOR     A               
593D: EA 0E D0   LD      ($D00E),A       
5940: EA 8C C2   LD      ($C28C),A       
5943: EA 8D C2   LD      ($C28D),A       
5946: EA 8E C2   LD      ($C28E),A       
5949: EA 8F C2   LD      ($C28F),A       
594C: 21 96 DB   LD      HL,$DB96        
594F: 34         INC     (HL)            
5950: C9         RET                     
5951: CD 02 46   CALL    $4602           
5954: CD 13 0B   CALL    $0B13           
5957: FA 0E D0   LD      A,($D00E)       
595A: C7         RST     0X00            
595B: 65         LD      H,L             
595C: 59         LD      E,C             
595D: 80         ADD     A,B             
595E: 59         LD      E,C             
595F: 0D         DEC     C               
5960: 5A         LD      E,D             
5961: 4E         LD      C,(HL)          
5962: 5A         LD      E,D             
5963: 5B         LD      E,E             
5964: 5A         LD      E,D             
5965: 3E 17      LD      A,$17           
5967: EA FE D6   LD      ($D6FE),A       
596A: AF         XOR     A               
596B: E0 96      LDFF00  ($96),A         
596D: E0 97      LDFF00  ($97),A         
596F: EA 55 C1   LD      ($C155),A       
5972: EA 56 C1   LD      ($C156),A       
5975: 3E 3D      LD      A,$3D           
5977: EA 68 D3   LD      ($D368),A       
597A: CD EB 4A   CALL    $4AEB           
597D: C3 2B 4A   JP      $4A2B           
5980: 3E 18      LD      A,$18           
5982: EA FF D6   LD      ($D6FF),A       
5985: 3E E8      LD      A,$E8           
5987: CD 01 3C   CALL    $3C01           
598A: 21 00 C2   LD      HL,$C200        
598D: 19         ADD     HL,DE           
598E: 36 18      LD      (HL),$18        
5990: 21 10 C2   LD      HL,$C210        
5993: 19         ADD     HL,DE           
5994: 36 20      LD      (HL),$20        
5996: 21 B0 C2   LD      HL,$C2B0        
5999: 19         ADD     HL,DE           
599A: 36 06      LD      (HL),$06        
599C: 21 40 C2   LD      HL,$C240        
599F: 19         ADD     HL,DE           
59A0: 36 03      LD      (HL),$03        
59A2: 3E E8      LD      A,$E8           
59A4: CD 01 3C   CALL    $3C01           
59A7: 21 00 C2   LD      HL,$C200        
59AA: 19         ADD     HL,DE           
59AB: 36 78      LD      (HL),$78        
59AD: 21 10 C2   LD      HL,$C210        
59B0: 19         ADD     HL,DE           
59B1: 36 78      LD      (HL),$78        
59B3: 21 B0 C2   LD      HL,$C2B0        
59B6: 19         ADD     HL,DE           
59B7: 36 06      LD      (HL),$06        
59B9: 21 40 C2   LD      HL,$C240        
59BC: 19         ADD     HL,DE           
59BD: 36 FD      LD      (HL),$FD        
59BF: 21 B0 C3   LD      HL,$C3B0        
59C2: 19         ADD     HL,DE           
59C3: 36 03      LD      (HL),$03        
59C5: 3E E8      LD      A,$E8           
59C7: CD 01 3C   CALL    $3C01           
59CA: 21 00 C2   LD      HL,$C200        
59CD: 19         ADD     HL,DE           
59CE: 36 68      LD      (HL),$68        
59D0: 21 10 C2   LD      HL,$C210        
59D3: 19         ADD     HL,DE           
59D4: 36 60      LD      (HL),$60        
59D6: 21 B0 C2   LD      HL,$C2B0        
59D9: 19         ADD     HL,DE           
59DA: 36 07      LD      (HL),$07        
59DC: 3E 60      LD      A,$60           
59DE: EA 09 D0   LD      ($D009),A       
59E1: C3 2B 4A   JP      $4A2B           
59E4: 00         NOP                     
59E5: 00         NOP                     
59E6: 00         NOP                     
59E7: 00         NOP                     
59E8: 05         DEC     B               
59E9: 05         DEC     B               
59EA: 05         DEC     B               
59EB: 05         DEC     B               
59EC: 05         DEC     B               
59ED: 05         DEC     B               
59EE: 05         DEC     B               
59EF: 05         DEC     B               
59F0: 19         ADD     HL,DE           
59F1: 19         ADD     HL,DE           
59F2: 1A         LD      A,(DE)          
59F3: 1A         LD      A,(DE)          
59F4: 1E 1E      LD      E,$1E           
59F6: 1E 1E      LD      E,$1E           
59F8: 00         NOP                     
59F9: 00         NOP                     
59FA: 00         NOP                     
59FB: 00         NOP                     
59FC: 00         NOP                     
59FD: 01 01 01   LD      BC,$0101        
5A00: 01 01 01   LD      BC,$0101        
5A03: 01 51 51   LD      BC,$5151        
5A06: 51         LD      D,C             
5A07: 52         LD      D,D             
5A08: 52         LD      D,D             
5A09: 92         SUB     D               
5A0A: 92         SUB     D               
5A0B: 92         SUB     D               
5A0C: 92         SUB     D               
5A0D: F0 E7      LD      A,($E7)         
5A0F: E6 0F      AND     $0F             
5A11: 20 16      JR      NZ,$5A29        
5A13: FA 0A D0   LD      A,($D00A)       
5A16: FE 10      CP      $10             
5A18: 20 0B      JR      NZ,$5A25        
5A1A: CD EB 4A   CALL    $4AEB           
5A1D: 3E 60      LD      A,$60           
5A1F: EA 09 D0   LD      ($D009),A       
5A22: C3 2B 4A   JP      $4A2B           
5A25: 3C         INC     A               
5A26: EA 0A D0   LD      ($D00A),A       
5A29: F0 E7      LD      A,($E7)         
5A2B: E6 03      AND     $03             
5A2D: 5F         LD      E,A             
5A2E: FA 0A D0   LD      A,($D00A)       
5A31: 83         ADD     A,E             
5A32: 5F         LD      E,A             
5A33: 16 00      LD      D,$00           
5A35: 21 E4 59   LD      HL,$59E4        
5A38: 19         ADD     HL,DE           
5A39: 7E         LD      A,(HL)          
5A3A: EA 97 DB   LD      ($DB97),A       
5A3D: 21 E4 59   LD      HL,$59E4        
5A40: 19         ADD     HL,DE           
5A41: 7E         LD      A,(HL)          
5A42: EA 98 DB   LD      ($DB98),A       
5A45: 21 F8 59   LD      HL,$59F8        
5A48: 19         ADD     HL,DE           
5A49: 7E         LD      A,(HL)          
5A4A: EA 99 DB   LD      ($DB99),A       
5A4D: C9         RET                     
5A4E: FA 09 D0   LD      A,($D009)       
5A51: A7         AND     A               
5A52: 20 06      JR      NZ,$5A5A        
5A54: CD EB 4A   CALL    $4AEB           
5A57: C3 2B 4A   JP      $4A2B           
5A5A: C9         RET                     
5A5B: CD EB 4A   CALL    $4AEB           
5A5E: AF         XOR     A               
5A5F: EA 0E D0   LD      ($D00E),A       
5A62: EA 8D C2   LD      ($C28D),A       
5A65: EA 8E C2   LD      ($C28E),A       
5A68: EA 8F C2   LD      ($C28F),A       
5A6B: 21 96 DB   LD      HL,$DB96        
5A6E: 34         INC     (HL)            
5A6F: C9         RET                     
5A70: CD 02 46   CALL    $4602           
5A73: 11 E0 98   LD      DE,$98E0        
5A76: CD 55 46   CALL    $4655           
5A79: CD 13 0B   CALL    $0B13           
5A7C: FA 0F D0   LD      A,($D00F)       
5A7F: 3C         INC     A               
5A80: EA 0F D0   LD      ($D00F),A       
5A83: FE 05      CP      $05             
5A85: 38 10      JR      C,$5A97         
5A87: AF         XOR     A               
5A88: EA 0F D0   LD      ($D00F),A       
5A8B: FA 0A D0   LD      A,($D00A)       
5A8E: 3C         INC     A               
5A8F: FE 2B      CP      $2B             
5A91: 20 01      JR      NZ,$5A94        
5A93: AF         XOR     A               
5A94: EA 0A D0   LD      ($D00A),A       
5A97: FA 0A D0   LD      A,($D00A)       
5A9A: 5F         LD      E,A             
5A9B: 16 00      LD      D,$00           
5A9D: 21 49 5B   LD      HL,$5B49        
5AA0: 19         ADD     HL,DE           
5AA1: 7E         LD      A,(HL)          
5AA2: C6 00      ADD     $00             
5AA4: EA 00 D0   LD      ($D000),A       
5AA7: FA 0E D0   LD      A,($D00E)       
5AAA: C7         RST     0X00            
5AAB: B5         OR      L               
5AAC: 5A         LD      E,D             
5AAD: BD         CP      L               
5AAE: 5A         LD      E,D             
5AAF: B9         CP      C               
5AB0: 5B         LD      E,E             
5AB1: 73         LD      (HL),E          
5AB2: 5C         LD      E,H             
5AB3: BB         CP      E               
5AB4: 5C         LD      E,H             
5AB5: 3E 18      LD      A,$18           
5AB7: EA FE D6   LD      ($D6FE),A       
5ABA: C3 2B 4A   JP      $4A2B           
5ABD: 3E 19      LD      A,$19           
5ABF: EA FF D6   LD      ($D6FF),A       
5AC2: 21 FF FF   LD      HL,$FFFF        
5AC5: CB CE      SET     1,E             
5AC7: 3E 42      LD      A,$42           
5AC9: E0 45      LDFF00  ($45),A         
5ACB: 3E E8      LD      A,$E8           
5ACD: CD 01 3C   CALL    $3C01           
5AD0: 21 00 C2   LD      HL,$C200        
5AD3: 19         ADD     HL,DE           
5AD4: 36 18      LD      (HL),$18        
5AD6: 21 10 C2   LD      HL,$C210        
5AD9: 19         ADD     HL,DE           
5ADA: 36 55      LD      (HL),$55        
5ADC: 21 B0 C2   LD      HL,$C2B0        
5ADF: 19         ADD     HL,DE           
5AE0: 36 08      LD      (HL),$08        
5AE2: 21 B0 C3   LD      HL,$C3B0        
5AE5: 19         ADD     HL,DE           
5AE6: 36 02      LD      (HL),$02        
5AE8: 3E E8      LD      A,$E8           
5AEA: CD 01 3C   CALL    $3C01           
5AED: 21 00 C2   LD      HL,$C200        
5AF0: 19         ADD     HL,DE           
5AF1: 36 68      LD      (HL),$68        
5AF3: 21 10 C2   LD      HL,$C210        
5AF6: 19         ADD     HL,DE           
5AF7: 36 58      LD      (HL),$58        
5AF9: 21 B0 C2   LD      HL,$C2B0        
5AFC: 19         ADD     HL,DE           
5AFD: 36 08      LD      (HL),$08        
5AFF: 21 B0 C3   LD      HL,$C3B0        
5B02: 19         ADD     HL,DE           
5B03: 34         INC     (HL)            
5B04: 3E E8      LD      A,$E8           
5B06: CD 01 3C   CALL    $3C01           
5B09: 21 00 C2   LD      HL,$C200        
5B0C: 19         ADD     HL,DE           
5B0D: 36 88      LD      (HL),$88        
5B0F: 21 10 C2   LD      HL,$C210        
5B12: 19         ADD     HL,DE           
5B13: 36 60      LD      (HL),$60        
5B15: 21 B0 C2   LD      HL,$C2B0        
5B18: 19         ADD     HL,DE           
5B19: 36 08      LD      (HL),$08        
5B1B: 3E E8      LD      A,$E8           
5B1D: CD 01 3C   CALL    $3C01           
5B20: 21 00 C2   LD      HL,$C200        
5B23: 19         ADD     HL,DE           
5B24: 36 08      LD      (HL),$08        
5B26: 21 10 C2   LD      HL,$C210        
5B29: 19         ADD     HL,DE           
5B2A: 36 50      LD      (HL),$50        
5B2C: 21 B0 C2   LD      HL,$C2B0        
5B2F: 19         ADD     HL,DE           
5B30: 36 09      LD      (HL),$09        
5B32: 21 40 C2   LD      HL,$C240        
5B35: 19         ADD     HL,DE           
5B36: 36 08      LD      (HL),$08        
5B38: 21 50 C2   LD      HL,$C250        
5B3B: 19         ADD     HL,DE           
5B3C: 36 F8      LD      (HL),$F8        
5B3E: CD EB 4A   CALL    $4AEB           
5B41: 3E 50      LD      A,$50           
5B43: EA 09 D0   LD      ($D009),A       
5B46: C3 2B 4A   JP      $4A2B           
5B49: 00         NOP                     
5B4A: 00         NOP                     
5B4B: 00         NOP                     
5B4C: 00         NOP                     
5B4D: 01 01 01   LD      BC,$0101        
5B50: 02         LD      (BC),A          
5B51: 02         LD      (BC),A          
5B52: 03         INC     BC              
5B53: 03         INC     BC              
5B54: 04         INC     B               
5B55: 05         DEC     B               
5B56: 06 07      LD      B,$07           
5B58: 08 09 0A   LD      ($0A09),SP      
5B5B: 0A         LD      A,(BC)          
5B5C: 0B         DEC     BC              
5B5D: 0B         DEC     BC              
5B5E: 0C         INC     C               
5B5F: 0C         INC     C               
5B60: 0C         INC     C               
5B61: 0B         DEC     BC              
5B62: 0B         DEC     BC              
5B63: 0A         LD      A,(BC)          
5B64: 0A         LD      A,(BC)          
5B65: 09         ADD     HL,BC           
5B66: 08 07 06   LD      ($0607),SP      
5B69: 05         DEC     B               
5B6A: 04         INC     B               
5B6B: 03         INC     BC              
5B6C: 03         INC     BC              
5B6D: 02         LD      (BC),A          
5B6E: 02         LD      (BC),A          
5B6F: 01 01 01   LD      BC,$0101        
5B72: 00         NOP                     
5B73: 00         NOP                     
5B74: 00         NOP                     
5B75: 00         NOP                     
5B76: 00         NOP                     
5B77: 00         NOP                     
5B78: 00         NOP                     
5B79: 0D         DEC     C               
5B7A: 4C         LD      C,H             
5B7B: 4D         LD      C,L             
5B7C: 4E         LD      C,(HL)          
5B7D: 4F         LD      C,A             
5B7E: 4C         LD      C,H             
5B7F: 4D         LD      C,L             
5B80: 4E         LD      C,(HL)          
5B81: 4F         LD      C,A             
5B82: 4C         LD      C,H             
5B83: 4D         LD      C,L             
5B84: 4E         LD      C,(HL)          
5B85: 4F         LD      C,A             
5B86: 4C         LD      C,H             
5B87: 4D         LD      C,L             
5B88: 00         NOP                     
5B89: 0D         DEC     C               
5B8A: 5C         LD      E,H             
5B8B: 5D         LD      E,L             
5B8C: 5E         LD      E,(HL)          
5B8D: 5F         LD      E,A             
5B8E: 5C         LD      E,H             
5B8F: 5D         LD      E,L             
5B90: 5E         LD      E,(HL)          
5B91: 5F         LD      E,A             
5B92: 5C         LD      E,H             
5B93: 5D         LD      E,L             
5B94: 5E         LD      E,(HL)          
5B95: 5F         LD      E,A             
5B96: 5C         LD      E,H             
5B97: 5D         LD      E,L             
5B98: 00         NOP                     
5B99: 0D         DEC     C               
5B9A: 6C         LD      L,H             
5B9B: 6D         LD      L,L             
5B9C: 6E         LD      L,(HL)          
5B9D: 6F         LD      L,A             
5B9E: 6C         LD      L,H             
5B9F: 6D         LD      L,L             
5BA0: 6E         LD      L,(HL)          
5BA1: 6F         LD      L,A             
5BA2: 6C         LD      L,H             
5BA3: 6D         LD      L,L             
5BA4: 6E         LD      L,(HL)          
5BA5: 6F         LD      L,A             
5BA6: 6C         LD      L,H             
5BA7: 6D         LD      L,L             
5BA8: 00         NOP                     
5BA9: 0D         DEC     C               
5BAA: 7C         LD      A,H             
5BAB: 7D         LD      A,L             
5BAC: 7E         LD      A,(HL)          
5BAD: 7F         LD      A,A             
5BAE: 7C         LD      A,H             
5BAF: 7D         LD      A,L             
5BB0: 7E         LD      A,(HL)          
5BB1: 7F         LD      A,A             
5BB2: 7C         LD      A,H             
5BB3: 7D         LD      A,L             
5BB4: 7E         LD      A,(HL)          
5BB5: 7F         LD      A,A             
5BB6: 7C         LD      A,H             
5BB7: 7D         LD      A,L             
5BB8: 00         NOP                     
5BB9: F0 E7      LD      A,($E7)         
5BBB: E6 07      AND     $07             
5BBD: 20 2C      JR      NZ,$5BEB        
5BBF: 21 01 D6   LD      HL,$D601        
5BC2: 3E 9A      LD      A,$9A           
5BC4: 22         LD      (HLI),A         
5BC5: 3E 23      LD      A,$23           
5BC7: 22         LD      (HLI),A         
5BC8: FA 0B D0   LD      A,($D00B)       
5BCB: 3C         INC     A               
5BCC: E6 03      AND     $03             
5BCE: EA 0B D0   LD      ($D00B),A       
5BD1: 17         RLA                     
5BD2: 17         RLA                     
5BD3: 17         RLA                     
5BD4: 17         RLA                     
5BD5: E6 F0      AND     $F0             
5BD7: 5F         LD      E,A             
5BD8: 16 00      LD      D,$00           
5BDA: 21 79 5B   LD      HL,$5B79        
5BDD: 19         ADD     HL,DE           
5BDE: 11 03 D6   LD      DE,$D603        
5BE1: 0E 10      LD      C,$10           
5BE3: 2A         LD      A,(HLI)         
5BE4: 12         LD      (DE),A          
5BE5: 13         INC     DE              
5BE6: 0D         DEC     C               
5BE7: 20 FA      JR      NZ,$5BE3        
5BE9: 18 03      JR      $5BEE           
5BEB: CD F9 5E   CALL    $5EF9           
5BEE: FA 01 D0   LD      A,($D001)       
5BF1: C7         RST     0X00            
5BF2: F8 5B      LDHL    SP,$5B          
5BF4: 1B         DEC     DE              
5BF5: 5C         LD      E,H             
5BF6: 44         LD      B,H             
5BF7: 5C         LD      E,H             
5BF8: FA 09 D0   LD      A,($D009)       
5BFB: A7         AND     A               
5BFC: 20 04      JR      NZ,$5C02        
5BFE: 21 01 D0   LD      HL,$D001        
5C01: 34         INC     (HL)            
5C02: C9         RET                     
5C03: 01 00 01   LD      BC,$0100        
5C06: 02         LD      (BC),A          
5C07: 01 02 03   LD      BC,$0302        
5C0A: 04         INC     B               
5C0B: 05         DEC     B               
5C0C: 06 07      LD      B,$07           
5C0E: 08 20 18   LD      ($1820),SP      
5C11: 20 18      JR      NZ,$5C2B        
5C13: 18 18      JR      $5C2D           
5C15: 20 40      JR      NZ,$5C57        
5C17: 0C         INC     C               
5C18: 0C         INC     C               
5C19: 0C         INC     C               
5C1A: 40         LD      B,B             
5C1B: FA 06 D0   LD      A,($D006)       
5C1E: A7         AND     A               
5C1F: 20 22      JR      NZ,$5C43        
5C21: FA 0D D0   LD      A,($D00D)       
5C24: 5F         LD      E,A             
5C25: 16 00      LD      D,$00           
5C27: 21 03 5C   LD      HL,$5C03        
5C2A: 19         ADD     HL,DE           
5C2B: 7E         LD      A,(HL)          
5C2C: EA 02 D0   LD      ($D002),A       
5C2F: 21 0F 5C   LD      HL,$5C0F        
5C32: 19         ADD     HL,DE           
5C33: 7E         LD      A,(HL)          
5C34: EA 06 D0   LD      ($D006),A       
5C37: 7B         LD      A,E             
5C38: 3C         INC     A               
5C39: EA 0D D0   LD      ($D00D),A       
5C3C: FE 0C      CP      $0C             
5C3E: 20 03      JR      NZ,$5C43        
5C40: C3 FE 5B   JP      $5BFE           
5C43: C9         RET                     
5C44: FA 06 D0   LD      A,($D006)       
5C47: A7         AND     A               
5C48: 20 08      JR      NZ,$5C52        
5C4A: AF         XOR     A               
5C4B: EA 05 D0   LD      ($D005),A       
5C4E: CD 2B 4A   CALL    $4A2B           
5C51: C9         RET                     
5C52: C9         RET                     
5C53: 1E 1E      LD      E,$1E           
5C55: 1E 1E      LD      E,$1E           
5C57: 1A         LD      A,(DE)          
5C58: 1A         LD      A,(DE)          
5C59: 19         ADD     HL,DE           
5C5A: 19         ADD     HL,DE           
5C5B: 05         DEC     B               
5C5C: 05         DEC     B               
5C5D: 05         DEC     B               
5C5E: 05         DEC     B               
5C5F: 00         NOP                     
5C60: 00         NOP                     
5C61: 00         NOP                     
5C62: 00         NOP                     
5C63: 92         SUB     D               
5C64: 92         SUB     D               
5C65: 92         SUB     D               
5C66: 92         SUB     D               
5C67: 92         SUB     D               
5C68: 92         SUB     D               
5C69: 51         LD      D,C             
5C6A: 51         LD      D,C             
5C6B: 41         LD      B,C             
5C6C: 41         LD      B,C             
5C6D: 00         NOP                     
5C6E: 00         NOP                     
5C6F: 00         NOP                     
5C70: 00         NOP                     
5C71: 00         NOP                     
5C72: 00         NOP                     
5C73: F0 E7      LD      A,($E7)         
5C75: E6 07      AND     $07             
5C77: 20 1D      JR      NZ,$5C96        
5C79: FA 05 D0   LD      A,($D005)       
5C7C: FE 0C      CP      $0C             
5C7E: 20 12      JR      NZ,$5C92        
5C80: 3E C0      LD      A,$C0           
5C82: EA 06 D0   LD      ($D006),A       
5C85: AF         XOR     A               
5C86: EA 97 DB   LD      ($DB97),A       
5C89: EA 98 DB   LD      ($DB98),A       
5C8C: EA 99 DB   LD      ($DB99),A       
5C8F: C3 2B 4A   JP      $4A2B           
5C92: 3C         INC     A               
5C93: EA 05 D0   LD      ($D005),A       
5C96: F0 E7      LD      A,($E7)         
5C98: E6 03      AND     $03             
5C9A: 5F         LD      E,A             
5C9B: FA 05 D0   LD      A,($D005)       
5C9E: 83         ADD     A,E             
5C9F: 5F         LD      E,A             
5CA0: 16 00      LD      D,$00           
5CA2: 21 53 5C   LD      HL,$5C53        
5CA5: 19         ADD     HL,DE           
5CA6: 7E         LD      A,(HL)          
5CA7: EA 97 DB   LD      ($DB97),A       
5CAA: 21 53 5C   LD      HL,$5C53        
5CAD: 19         ADD     HL,DE           
5CAE: 7E         LD      A,(HL)          
5CAF: EA 98 DB   LD      ($DB98),A       
5CB2: 21 63 5C   LD      HL,$5C63        
5CB5: 19         ADD     HL,DE           
5CB6: 7E         LD      A,(HL)          
5CB7: EA 99 DB   LD      ($DB99),A       
5CBA: C9         RET                     
5CBB: FA 06 D0   LD      A,($D006)       
5CBE: A7         AND     A               
5CBF: 20 3F      JR      NZ,$5D00        
5CC1: AF         XOR     A               
5CC2: EA 0E D0   LD      ($D00E),A       
5CC5: EA 87 C2   LD      ($C287),A       
5CC8: EA 88 C2   LD      ($C288),A       
5CCB: EA 89 C2   LD      ($C289),A       
5CCE: EA 8A C2   LD      ($C28A),A       
5CD1: EA 8B C2   LD      ($C28B),A       
5CD4: EA 8C C2   LD      ($C28C),A       
5CD7: EA 8D C2   LD      ($C28D),A       
5CDA: EA 8E C2   LD      ($C28E),A       
5CDD: EA 8F C2   LD      ($C28F),A       
5CE0: E0 97      LDFF00  ($97),A         
5CE2: EA 0F D0   LD      ($D00F),A       
5CE5: EA 0F D0   LD      ($D00F),A       
5CE8: CD EB 4A   CALL    $4AEB           
5CEB: 21 FF FF   LD      HL,$FFFF        
5CEE: CB 8E      SET     1,E             
5CF0: 21 FD D6   LD      HL,$D6FD        
5CF3: CB D6      SET     1,E             
5CF5: 21 96 DB   LD      HL,$DB96        
5CF8: 34         INC     (HL)            
5CF9: 7E         LD      A,(HL)          
5CFA: FE 09      CP      $09             
5CFC: 20 02      JR      NZ,$5D00        
5CFE: 36 00      LD      (HL),$00        
5D00: C9         RET                     
5D01: 99         SBC     C               
5D02: 46         LD      B,(HL)          
5D03: 05         DEC     B               
5D04: AC         XOR     H               
5D05: AC         XOR     H               
5D06: AC         XOR     H               
5D07: AC         XOR     H               
5D08: AC         XOR     H               
5D09: AC         XOR     H               
5D0A: 99         SBC     C               
5D0B: 66         LD      H,(HL)          
5D0C: 05         DEC     B               
5D0D: AC         XOR     H               
5D0E: AC         XOR     H               
5D0F: 86         ADD     A,(HL)          
5D10: 87         ADD     A,A             
5D11: 88         ADC     A,B             
5D12: 89         ADC     A,C             
5D13: 99         SBC     C               
5D14: 86         ADD     A,(HL)          
5D15: 05         DEC     B               
5D16: 94         SUB     H               
5D17: 95         SUB     L               
5D18: 96         SUB     (HL)            
5D19: 97         SUB     A               
5D1A: 98         SBC     B               
5D1B: 99         SBC     C               
5D1C: 99         SBC     C               
5D1D: A6         AND     (HL)            
5D1E: 05         DEC     B               
5D1F: A4         AND     H               
5D20: A5         AND     L               
5D21: A6         AND     (HL)            
5D22: A7         AND     A               
5D23: A8         XOR     B               
5D24: A9         XOR     C               
5D25: 99         SBC     C               
5D26: C6 05      ADD     $05             
5D28: B4         OR      H               
5D29: B5         OR      L               
5D2A: B6         OR      (HL)            
5D2B: B7         OR      A               
5D2C: B8         CP      B               
5D2D: B9         CP      C               
5D2E: 99         SBC     C               
5D2F: E6 05      AND     $05             
5D31: C4 C5 C6   CALL    NZ,$C6C5        
5D34: C7         RST     0X00            
5D35: C8         RET     Z               
5D36: C9         RET                     
5D37: 99         SBC     C               
5D38: 46         LD      B,(HL)          
5D39: 05         DEC     B               
5D3A: AC         XOR     H               
5D3B: AC         XOR     H               
5D3C: AC         XOR     H               
5D3D: AC         XOR     H               
5D3E: AC         XOR     H               
5D3F: AC         XOR     H               
5D40: 99         SBC     C               
5D41: 66         LD      H,(HL)          
5D42: 05         DEC     B               
5D43: AC         XOR     H               
5D44: AC         XOR     H               
5D45: 86         ADD     A,(HL)          
5D46: 87         ADD     A,A             
5D47: 88         ADC     A,B             
5D48: 89         ADC     A,C             
5D49: 99         SBC     C               
5D4A: 86         ADD     A,(HL)          
5D4B: 05         DEC     B               
5D4C: 94         SUB     H               
5D4D: 95         SUB     L               
5D4E: 96         SUB     (HL)            
5D4F: 97         SUB     A               
5D50: 98         SBC     B               
5D51: 99         SBC     C               
5D52: 99         SBC     C               
5D53: A6         AND     (HL)            
5D54: 05         DEC     B               
5D55: A4         AND     H               
5D56: A5         AND     L               
5D57: A6         AND     (HL)            
5D58: A7         AND     A               
5D59: A8         XOR     B               
5D5A: A9         XOR     C               
5D5B: 99         SBC     C               
5D5C: C6 05      ADD     $05             
5D5E: B4         OR      H               
5D5F: B5         OR      L               
5D60: 8A         ADC     A,D             
5D61: 8B         ADC     A,E             
5D62: B8         CP      B               
5D63: B9         CP      C               
5D64: 99         SBC     C               
5D65: E6 05      AND     $05             
5D67: C4 C5 9A   CALL    NZ,$9AC5        
5D6A: 9B         SBC     E               
5D6B: C8         RET     Z               
5D6C: C9         RET                     
5D6D: 99         SBC     C               
5D6E: 46         LD      B,(HL)          
5D6F: 05         DEC     B               
5D70: AC         XOR     H               
5D71: AC         XOR     H               
5D72: AC         XOR     H               
5D73: AC         XOR     H               
5D74: AC         XOR     H               
5D75: AC         XOR     H               
5D76: 99         SBC     C               
5D77: 66         LD      H,(HL)          
5D78: 05         DEC     B               
5D79: AC         XOR     H               
5D7A: AC         XOR     H               
5D7B: 86         ADD     A,(HL)          
5D7C: 87         ADD     A,A             
5D7D: 88         ADC     A,B             
5D7E: 89         ADC     A,C             
5D7F: 99         SBC     C               
5D80: 86         ADD     A,(HL)          
5D81: 05         DEC     B               
5D82: 94         SUB     H               
5D83: 95         SUB     L               
5D84: 96         SUB     (HL)            
5D85: 97         SUB     A               
5D86: 98         SBC     B               
5D87: 99         SBC     C               
5D88: 99         SBC     C               
5D89: A6         AND     (HL)            
5D8A: 05         DEC     B               
5D8B: A4         AND     H               
5D8C: A5         AND     L               
5D8D: A6         AND     (HL)            
5D8E: A7         AND     A               
5D8F: A8         XOR     B               
5D90: A9         XOR     C               
5D91: 99         SBC     C               
5D92: C6 05      ADD     $05             
5D94: B4         OR      H               
5D95: B5         OR      L               
5D96: 8C         ADC     A,H             
5D97: 8D         ADC     A,L             
5D98: B8         CP      B               
5D99: B9         CP      C               
5D9A: 99         SBC     C               
5D9B: E6 05      AND     $05             
5D9D: C4 C5 9C   CALL    NZ,$9CC5        
5DA0: C7         RST     0X00            
5DA1: C8         RET     Z               
5DA2: C9         RET                     
5DA3: 99         SBC     C               
5DA4: 46         LD      B,(HL)          
5DA5: 05         DEC     B               
5DA6: AC         XOR     H               
5DA7: AC         XOR     H               
5DA8: AC         XOR     H               
5DA9: AC         XOR     H               
5DAA: AC         XOR     H               
5DAB: AC         XOR     H               
5DAC: 99         SBC     C               
5DAD: 66         LD      H,(HL)          
5DAE: 05         DEC     B               
5DAF: AC         XOR     H               
5DB0: AC         XOR     H               
5DB1: 86         ADD     A,(HL)          
5DB2: 87         ADD     A,A             
5DB3: 88         ADC     A,B             
5DB4: 89         ADC     A,C             
5DB5: 99         SBC     C               
5DB6: 86         ADD     A,(HL)          
5DB7: 05         DEC     B               
5DB8: 94         SUB     H               
5DB9: 95         SUB     L               
5DBA: 96         SUB     (HL)            
5DBB: 97         SUB     A               
5DBC: 98         SBC     B               
5DBD: 99         SBC     C               
5DBE: 99         SBC     C               
5DBF: A6         AND     (HL)            
5DC0: 05         DEC     B               
5DC1: A4         AND     H               
5DC2: A5         AND     L               
5DC3: A6         AND     (HL)            
5DC4: A7         AND     A               
5DC5: A8         XOR     B               
5DC6: A9         XOR     C               
5DC7: 99         SBC     C               
5DC8: C6 05      ADD     $05             
5DCA: B4         OR      H               
5DCB: B5         OR      L               
5DCC: 8E         ADC     A,(HL)          
5DCD: 8F         ADC     A,A             
5DCE: B8         CP      B               
5DCF: B9         CP      C               
5DD0: 99         SBC     C               
5DD1: E6 05      AND     $05             
5DD3: C4 C5 9E   CALL    NZ,$9EC5        
5DD6: C7         RST     0X00            
5DD7: C8         RET     Z               
5DD8: C9         RET                     
5DD9: 99         SBC     C               
5DDA: 46         LD      B,(HL)          
5DDB: 05         DEC     B               
5DDC: AC         XOR     H               
5DDD: AC         XOR     H               
5DDE: AC         XOR     H               
5DDF: AC         XOR     H               
5DE0: AC         XOR     H               
5DE1: AC         XOR     H               
5DE2: 99         SBC     C               
5DE3: 66         LD      H,(HL)          
5DE4: 05         DEC     B               
5DE5: AC         XOR     H               
5DE6: AC         XOR     H               
5DE7: 86         ADD     A,(HL)          
5DE8: 87         ADD     A,A             
5DE9: 88         ADC     A,B             
5DEA: 89         ADC     A,C             
5DEB: 99         SBC     C               
5DEC: 86         ADD     A,(HL)          
5DED: 05         DEC     B               
5DEE: 94         SUB     H               
5DEF: 95         SUB     L               
5DF0: 96         SUB     (HL)            
5DF1: 97         SUB     A               
5DF2: 98         SBC     B               
5DF3: 99         SBC     C               
5DF4: 99         SBC     C               
5DF5: A6         AND     (HL)            
5DF6: 05         DEC     B               
5DF7: A4         AND     H               
5DF8: A5         AND     L               
5DF9: A6         AND     (HL)            
5DFA: A7         AND     A               
5DFB: A8         XOR     B               
5DFC: A9         XOR     C               
5DFD: 99         SBC     C               
5DFE: C6 05      ADD     $05             
5E00: B4         OR      H               
5E01: B5         OR      L               
5E02: E9         JP      (HL)            
5E03: EA B8 B9   LD      ($B9B8),A       
5E06: 99         SBC     C               
5E07: E6 05      AND     $05             
5E09: C4 C5 F9   CALL    NZ,$F9C5        
5E0C: C7         RST     0X00            
5E0D: C8         RET     Z               
5E0E: C9         RET                     
5E0F: 99         SBC     C               
5E10: 46         LD      B,(HL)          
5E11: 05         DEC     B               
5E12: AC         XOR     H               
5E13: AC         XOR     H               
5E14: AC         XOR     H               
5E15: AC         XOR     H               
5E16: AC         XOR     H               
5E17: AC         XOR     H               
5E18: 99         SBC     C               
5E19: 66         LD      H,(HL)          
5E1A: 05         DEC     B               
5E1B: AC         XOR     H               
5E1C: AC         XOR     H               
5E1D: 86         ADD     A,(HL)          
5E1E: 87         ADD     A,A             
5E1F: 88         ADC     A,B             
5E20: 89         ADC     A,C             
5E21: 99         SBC     C               
5E22: 86         ADD     A,(HL)          
5E23: 05         DEC     B               
5E24: 94         SUB     H               
5E25: 95         SUB     L               
5E26: 96         SUB     (HL)            
5E27: 97         SUB     A               
5E28: 98         SBC     B               
5E29: 99         SBC     C               
5E2A: 99         SBC     C               
5E2B: A6         AND     (HL)            
5E2C: 05         DEC     B               
5E2D: A4         AND     H               
5E2E: A5         AND     L               
5E2F: A6         AND     (HL)            
5E30: A7         AND     A               
5E31: A8         XOR     B               
5E32: A9         XOR     C               
5E33: 99         SBC     C               
5E34: C6 05      ADD     $05             
5E36: B4         OR      H               
5E37: B5         OR      L               
5E38: EB         ???                     
5E39: EC         ???                     
5E3A: B8         CP      B               
5E3B: B9         CP      C               
5E3C: 99         SBC     C               
5E3D: E6 05      AND     $05             
5E3F: C4 C5 FB   CALL    NZ,$FBC5        
5E42: C7         RST     0X00            
5E43: C8         RET     Z               
5E44: C9         RET                     
5E45: 99         SBC     C               
5E46: 46         LD      B,(HL)          
5E47: 05         DEC     B               
5E48: AC         XOR     H               
5E49: AC         XOR     H               
5E4A: AC         XOR     H               
5E4B: AC         XOR     H               
5E4C: AC         XOR     H               
5E4D: AC         XOR     H               
5E4E: 99         SBC     C               
5E4F: 66         LD      H,(HL)          
5E50: 05         DEC     B               
5E51: AC         XOR     H               
5E52: AC         XOR     H               
5E53: 86         ADD     A,(HL)          
5E54: 87         ADD     A,A             
5E55: 88         ADC     A,B             
5E56: 89         ADC     A,C             
5E57: 99         SBC     C               
5E58: 86         ADD     A,(HL)          
5E59: 05         DEC     B               
5E5A: 94         SUB     H               
5E5B: 95         SUB     L               
5E5C: 96         SUB     (HL)            
5E5D: 97         SUB     A               
5E5E: 98         SBC     B               
5E5F: 99         SBC     C               
5E60: 99         SBC     C               
5E61: A6         AND     (HL)            
5E62: 05         DEC     B               
5E63: A4         AND     H               
5E64: A5         AND     L               
5E65: A6         AND     (HL)            
5E66: A7         AND     A               
5E67: A8         XOR     B               
5E68: A9         XOR     C               
5E69: 99         SBC     C               
5E6A: C6 05      ADD     $05             
5E6C: B4         OR      H               
5E6D: B5         OR      L               
5E6E: ED         ???                     
5E6F: EE B8      XOR     $B8             
5E71: B9         CP      C               
5E72: 99         SBC     C               
5E73: E6 05      AND     $05             
5E75: C4 C5 FB   CALL    NZ,$FBC5        
5E78: C7         RST     0X00            
5E79: C8         RET     Z               
5E7A: C9         RET                     
5E7B: 99         SBC     C               
5E7C: 46         LD      B,(HL)          
5E7D: 05         DEC     B               
5E7E: AC         XOR     H               
5E7F: AC         XOR     H               
5E80: AC         XOR     H               
5E81: AC         XOR     H               
5E82: AC         XOR     H               
5E83: AC         XOR     H               
5E84: 99         SBC     C               
5E85: 66         LD      H,(HL)          
5E86: 05         DEC     B               
5E87: 00         NOP                     
5E88: 01 02 03   LD      BC,$0302        
5E8B: 04         INC     B               
5E8C: AC         XOR     H               
5E8D: 99         SBC     C               
5E8E: 86         ADD     A,(HL)          
5E8F: 05         DEC     B               
5E90: 10 11      STOP    $11             
5E92: 12         LD      (DE),A          
5E93: 13         INC     DE              
5E94: 14         INC     D               
5E95: 15         DEC     D               
5E96: 99         SBC     C               
5E97: A6         AND     (HL)            
5E98: 05         DEC     B               
5E99: 20 21      JR      NZ,$5EBC        
5E9B: 22         LD      (HLI),A         
5E9C: 23         INC     HL              
5E9D: 24         INC     H               
5E9E: 25         DEC     H               
5E9F: 99         SBC     C               
5EA0: C6 05      ADD     $05             
5EA2: 30 31      JR      NC,$5ED5        
5EA4: 32         LD      (HLD),A         
5EA5: 33         INC     SP              
5EA6: 34         INC     (HL)            
5EA7: 35         DEC     (HL)            
5EA8: 99         SBC     C               
5EA9: E6 05      AND     $05             
5EAB: 40         LD      B,B             
5EAC: 41         LD      B,C             
5EAD: 42         LD      B,D             
5EAE: 43         LD      B,E             
5EAF: 44         LD      B,H             
5EB0: C9         RET                     
5EB1: 99         SBC     C               
5EB2: 46         LD      B,(HL)          
5EB3: 05         DEC     B               
5EB4: 0C         INC     C               
5EB5: 0D         DEC     C               
5EB6: 1C         INC     E               
5EB7: 1D         DEC     E               
5EB8: AC         XOR     H               
5EB9: AC         XOR     H               
5EBA: 99         SBC     C               
5EBB: 66         LD      H,(HL)          
5EBC: 05         DEC     B               
5EBD: 06 07      LD      B,$07           
5EBF: 08 09 0A   LD      ($0A09),SP      
5EC2: AC         XOR     H               
5EC3: 99         SBC     C               
5EC4: 86         ADD     A,(HL)          
5EC5: 05         DEC     B               
5EC6: 16 17      LD      D,$17           
5EC8: 18 19      JR      $5EE3           
5ECA: 1A         LD      A,(DE)          
5ECB: 1B         DEC     DE              
5ECC: 99         SBC     C               
5ECD: A6         AND     (HL)            
5ECE: 05         DEC     B               
5ECF: 26 27      LD      H,$27           
5ED1: 28 29      JR      Z,$5EFC         
5ED3: 2A         LD      A,(HLI)         
5ED4: 2B         DEC     HL              
5ED5: 99         SBC     C               
5ED6: C6 05      ADD     $05             
5ED8: 36 37      LD      (HL),$37        
5EDA: 38 39      JR      C,$5F15         
5EDC: 3A         LD      A,(HLD)         
5EDD: 3B         DEC     SP              
5EDE: 99         SBC     C               
5EDF: E6 05      AND     $05             
5EE1: 46         LD      B,(HL)          
5EE2: 47         LD      B,A             
5EE3: 48         LD      C,B             
5EE4: 49         LD      C,C             
5EE5: 4A         LD      C,D             
5EE6: C9         RET                     
5EE7: 01 5D 37   LD      BC,$375D        
5EEA: 5D         LD      E,L             
5EEB: 6D         LD      L,L             
5EEC: 5D         LD      E,L             
5EED: A3         AND     E               
5EEE: 5D         LD      E,L             
5EEF: D9         RETI                    
5EF0: 5D         LD      E,L             
5EF1: 0F         RRCA                    
5EF2: 5E         LD      E,(HL)          
5EF3: 45         LD      B,L             
5EF4: 5E         LD      E,(HL)          
5EF5: 7B         LD      A,E             
5EF6: 5E         LD      E,(HL)          
5EF7: B1         OR      C               
5EF8: 5E         LD      E,(HL)          
5EF9: F0 E7      LD      A,($E7)         
5EFB: E6 01      AND     $01             
5EFD: FE 01      CP      $01             
5EFF: 20 1C      JR      NZ,$5F1D        
5F01: FA 02 D0   LD      A,($D002)       
5F04: CB 27      SET     1,E             
5F06: 5F         LD      E,A             
5F07: 16 00      LD      D,$00           
5F09: 21 E7 5E   LD      HL,$5EE7        
5F0C: 19         ADD     HL,DE           
5F0D: 2A         LD      A,(HLI)         
5F0E: 66         LD      H,(HL)          
5F0F: 6F         LD      L,A             
5F10: 11 01 D6   LD      DE,$D601        
5F13: 0E 36      LD      C,$36           
5F15: 2A         LD      A,(HLI)         
5F16: 12         LD      (DE),A          
5F17: 13         INC     DE              
5F18: 0D         DEC     C               
5F19: 20 FA      JR      NZ,$5F15        
5F1B: AF         XOR     A               
5F1C: 12         LD      (DE),A          
5F1D: C9         RET                     
5F1E: CD 13 0B   CALL    $0B13           
5F21: FA 0E D0   LD      A,($D00E)       
5F24: C7         RST     0X00            
5F25: 37         SCF                     
5F26: 5F         LD      E,A             
5F27: 3F         CCF                     
5F28: 5F         LD      E,A             
5F29: 5E         LD      E,(HL)          
5F2A: 5F         LD      E,A             
5F2B: A8         XOR     B               
5F2C: 5F         LD      E,A             
5F2D: C7         RST     0X00            
5F2E: 5F         LD      E,A             
5F2F: FE 5F      CP      $5F             
5F31: 23         INC     HL              
5F32: 60         LD      H,B             
5F33: 8B         ADC     A,E             
5F34: 69         LD      L,C             
5F35: 5B         LD      E,E             
5F36: 6A         LD      L,D             
5F37: 3E 19      LD      A,$19           
5F39: EA FE D6   LD      ($D6FE),A       
5F3C: C3 2B 4A   JP      $4A2B           
5F3F: 3E 1A      LD      A,$1A           
5F41: EA FF D6   LD      ($D6FF),A       
5F44: 3E E8      LD      A,$E8           
5F46: CD 01 3C   CALL    $3C01           
5F49: 21 00 C2   LD      HL,$C200        
5F4C: 19         ADD     HL,DE           
5F4D: 36 40      LD      (HL),$40        
5F4F: 21 10 C2   LD      HL,$C210        
5F52: 19         ADD     HL,DE           
5F53: 36 4E      LD      (HL),$4E        
5F55: 21 B0 C2   LD      HL,$C2B0        
5F58: 19         ADD     HL,DE           
5F59: 36 0A      LD      (HL),$0A        
5F5B: C3 2B 4A   JP      $4A2B           
5F5E: 11 60 99   LD      DE,$9960        
5F61: CD 55 46   CALL    $4655           
5F64: F0 E7      LD      A,($E7)         
5F66: E6 03      AND     $03             
5F68: 20 16      JR      NZ,$5F80        
5F6A: FA 0A D0   LD      A,($D00A)       
5F6D: FE 0C      CP      $0C             
5F6F: 20 0B      JR      NZ,$5F7C        
5F71: CD EB 4A   CALL    $4AEB           
5F74: 3E 60      LD      A,$60           
5F76: EA 09 D0   LD      ($D009),A       
5F79: C3 2B 4A   JP      $4A2B           
5F7C: 3C         INC     A               
5F7D: EA 0A D0   LD      ($D00A),A       
5F80: F0 E7      LD      A,($E7)         
5F82: E6 03      AND     $03             
5F84: 5F         LD      E,A             
5F85: FA 0A D0   LD      A,($D00A)       
5F88: 83         ADD     A,E             
5F89: 5F         LD      E,A             
5F8A: 16 00      LD      D,$00           
5F8C: 21 0B 59   LD      HL,$590B        
5F8F: 19         ADD     HL,DE           
5F90: 7E         LD      A,(HL)          
5F91: EA 97 DB   LD      ($DB97),A       
5F94: EA 98 DB   LD      ($DB98),A       
5F97: 21 0B 59   LD      HL,$590B        
5F9A: 19         ADD     HL,DE           
5F9B: 7E         LD      A,(HL)          
5F9C: EA 98 DB   LD      ($DB98),A       
5F9F: 21 1B 59   LD      HL,$591B        
5FA2: 19         ADD     HL,DE           
5FA3: 7E         LD      A,(HL)          
5FA4: EA 99 DB   LD      ($DB99),A       
5FA7: C9         RET                     
5FA8: 11 60 99   LD      DE,$9960        
5FAB: CD 55 46   CALL    $4655           
5FAE: FA 09 D0   LD      A,($D009)       
5FB1: A7         AND     A               
5FB2: 20 06      JR      NZ,$5FBA        
5FB4: CD EB 4A   CALL    $4AEB           
5FB7: C3 2B 4A   JP      $4A2B           
5FBA: C9         RET                     
5FBB: 1E 1E      LD      E,$1E           
5FBD: 1E 1E      LD      E,$1E           
5FBF: 2E 2E      LD      L,$2E           
5FC1: 2E 2E      LD      L,$2E           
5FC3: 6E         LD      L,(HL)          
5FC4: 6E         LD      L,(HL)          
5FC5: 6E         LD      L,(HL)          
5FC6: 6E         LD      L,(HL)          
5FC7: 11 60 99   LD      DE,$9960        
5FCA: CD 55 46   CALL    $4655           
5FCD: F0 E7      LD      A,($E7)         
5FCF: E6 07      AND     $07             
5FD1: 20 16      JR      NZ,$5FE9        
5FD3: FA 0A D0   LD      A,($D00A)       
5FD6: FE 08      CP      $08             
5FD8: 20 0B      JR      NZ,$5FE5        
5FDA: CD EB 4A   CALL    $4AEB           
5FDD: 3E 20      LD      A,$20           
5FDF: EA 06 D0   LD      ($D006),A       
5FE2: C3 2B 4A   JP      $4A2B           
5FE5: 3C         INC     A               
5FE6: EA 0A D0   LD      ($D00A),A       
5FE9: F0 E7      LD      A,($E7)         
5FEB: E6 03      AND     $03             
5FED: 5F         LD      E,A             
5FEE: FA 0A D0   LD      A,($D00A)       
5FF1: 83         ADD     A,E             
5FF2: 5F         LD      E,A             
5FF3: 16 00      LD      D,$00           
5FF5: 21 BB 5F   LD      HL,$5FBB        
5FF8: 19         ADD     HL,DE           
5FF9: 7E         LD      A,(HL)          
5FFA: EA 98 DB   LD      ($DB98),A       
5FFD: C9         RET                     
5FFE: 11 60 99   LD      DE,$9960        
6001: CD 55 46   CALL    $4655           
6004: FA 06 D0   LD      A,($D006)       
6007: A7         AND     A               
6008: 20 18      JR      NZ,$6022        
600A: 3E 0A      LD      A,$0A           
600C: EA 06 D0   LD      ($D006),A       
600F: FA 00 D0   LD      A,($D000)       
6012: 3C         INC     A               
6013: EA 00 D0   LD      ($D000),A       
6016: FE 02      CP      $02             
6018: 20 08      JR      NZ,$6022        
601A: 3E 20      LD      A,$20           
601C: EA 06 D0   LD      ($D006),A       
601F: C3 2B 4A   JP      $4A2B           
6022: C9         RET                     
6023: 11 60 99   LD      DE,$9960        
6026: CD 55 46   CALL    $4655           
6029: FA 06 D0   LD      A,($D006)       
602C: A7         AND     A               
602D: 20 03      JR      NZ,$6032        
602F: C3 2B 4A   JP      $4A2B           
6032: C9         RET                     
6033: 9B         SBC     E               
6034: E0 13      LDFF00  ($13),A         
6036: AC         XOR     H               
6037: AC         XOR     H               
6038: AC         XOR     H               
6039: AC         XOR     H               
603A: AC         XOR     H               
603B: AC         XOR     H               
603C: AC         XOR     H               
603D: AC         XOR     H               
603E: AC         XOR     H               
603F: AC         XOR     H               
6040: AC         XOR     H               
6041: AC         XOR     H               
6042: AC         XOR     H               
6043: AC         XOR     H               
6044: AC         XOR     H               
6045: AC         XOR     H               
6046: AC         XOR     H               
6047: AC         XOR     H               
6048: AC         XOR     H               
6049: AC         XOR     H               
604A: 00         NOP                     
604B: 9B         SBC     E               
604C: C0         RET     NZ              
604D: 13         INC     DE              
604E: AC         XOR     H               
604F: AC         XOR     H               
6050: AC         XOR     H               
6051: AC         XOR     H               
6052: AC         XOR     H               
6053: AC         XOR     H               
6054: AC         XOR     H               
6055: AC         XOR     H               
6056: AC         XOR     H               
6057: AC         XOR     H               
6058: AC         XOR     H               
6059: AC         XOR     H               
605A: AC         XOR     H               
605B: AC         XOR     H               
605C: AC         XOR     H               
605D: AC         XOR     H               
605E: AC         XOR     H               
605F: AC         XOR     H               
6060: AC         XOR     H               
6061: AC         XOR     H               
6062: 00         NOP                     
6063: 9B         SBC     E               
6064: A0         AND     B               
6065: 13         INC     DE              
6066: AC         XOR     H               
6067: AC         XOR     H               
6068: AC         XOR     H               
6069: AC         XOR     H               
606A: AC         XOR     H               
606B: AC         XOR     H               
606C: AC         XOR     H               
606D: AC         XOR     H               
606E: AC         XOR     H               
606F: AC         XOR     H               
6070: AC         XOR     H               
6071: AC         XOR     H               
6072: AC         XOR     H               
6073: AC         XOR     H               
6074: AC         XOR     H               
6075: AC         XOR     H               
6076: AC         XOR     H               
6077: AC         XOR     H               
6078: AC         XOR     H               
6079: AC         XOR     H               
607A: 00         NOP                     
607B: 9B         SBC     E               
607C: 80         ADD     A,B             
607D: 13         INC     DE              
607E: 60         LD      H,B             
607F: 61         LD      H,C             
6080: 62         LD      H,D             
6081: 63         LD      H,E             
6082: AC         XOR     H               
6083: AC         XOR     H               
6084: AC         XOR     H               
6085: AC         XOR     H               
6086: AC         XOR     H               
6087: AC         XOR     H               
6088: AC         XOR     H               
6089: AC         XOR     H               
608A: AC         XOR     H               
608B: AC         XOR     H               
608C: AC         XOR     H               
608D: AC         XOR     H               
608E: AC         XOR     H               
608F: AC         XOR     H               
6090: AC         XOR     H               
6091: AC         XOR     H               
6092: 00         NOP                     
6093: 9B         SBC     E               
6094: 60         LD      H,B             
6095: 13         INC     DE              
6096: 50         LD      D,B             
6097: 51         LD      D,C             
6098: 52         LD      D,D             
6099: 53         LD      D,E             
609A: AC         XOR     H               
609B: AC         XOR     H               
609C: AC         XOR     H               
609D: AC         XOR     H               
609E: AC         XOR     H               
609F: AC         XOR     H               
60A0: AC         XOR     H               
60A1: AC         XOR     H               
60A2: AC         XOR     H               
60A3: AC         XOR     H               
60A4: AC         XOR     H               
60A5: AC         XOR     H               
60A6: AC         XOR     H               
60A7: AC         XOR     H               
60A8: AC         XOR     H               
60A9: AC         XOR     H               
60AA: 00         NOP                     
60AB: 9B         SBC     E               
60AC: 40         LD      B,B             
60AD: 13         INC     DE              
60AE: AC         XOR     H               
60AF: AC         XOR     H               
60B0: AC         XOR     H               
60B1: AC         XOR     H               
60B2: AC         XOR     H               
60B3: AC         XOR     H               
60B4: AC         XOR     H               
60B5: AC         XOR     H               
60B6: AC         XOR     H               
60B7: AC         XOR     H               
60B8: AC         XOR     H               
60B9: AC         XOR     H               
60BA: AC         XOR     H               
60BB: AC         XOR     H               
60BC: AC         XOR     H               
60BD: AC         XOR     H               
60BE: AC         XOR     H               
60BF: AC         XOR     H               
60C0: AC         XOR     H               
60C1: AC         XOR     H               
60C2: 00         NOP                     
60C3: 9B         SBC     E               
60C4: 20 13      JR      NZ,$60D9        
60C6: AC         XOR     H               
60C7: AC         XOR     H               
60C8: AC         XOR     H               
60C9: AC         XOR     H               
60CA: AC         XOR     H               
60CB: AC         XOR     H               
60CC: AC         XOR     H               
60CD: AC         XOR     H               
60CE: AC         XOR     H               
60CF: AC         XOR     H               
60D0: AC         XOR     H               
60D1: AC         XOR     H               
60D2: AC         XOR     H               
60D3: AC         XOR     H               
60D4: AC         XOR     H               
60D5: AC         XOR     H               
60D6: AC         XOR     H               
60D7: AC         XOR     H               
60D8: AC         XOR     H               
60D9: AC         XOR     H               
60DA: 00         NOP                     
60DB: 9B         SBC     E               
60DC: 00         NOP                     
60DD: 13         INC     DE              
60DE: AC         XOR     H               
60DF: AC         XOR     H               
60E0: AC         XOR     H               
60E1: AC         XOR     H               
60E2: AC         XOR     H               
60E3: AC         XOR     H               
60E4: AC         XOR     H               
60E5: AC         XOR     H               
60E6: AC         XOR     H               
60E7: AC         XOR     H               
60E8: AC         XOR     H               
60E9: AC         XOR     H               
60EA: AC         XOR     H               
60EB: AC         XOR     H               
60EC: AC         XOR     H               
60ED: AC         XOR     H               
60EE: AC         XOR     H               
60EF: AC         XOR     H               
60F0: AC         XOR     H               
60F1: AC         XOR     H               
60F2: 00         NOP                     
60F3: 9A         SBC     D               
60F4: E0 13      LDFF00  ($13),A         
60F6: AC         XOR     H               
60F7: AC         XOR     H               
60F8: AC         XOR     H               
60F9: AC         XOR     H               
60FA: AC         XOR     H               
60FB: AC         XOR     H               
60FC: AC         XOR     H               
60FD: AC         XOR     H               
60FE: AC         XOR     H               
60FF: AC         XOR     H               
6100: AC         XOR     H               
6101: AC         XOR     H               
6102: AC         XOR     H               
6103: 60         LD      H,B             
6104: 61         LD      H,C             
6105: 62         LD      H,D             
6106: 63         LD      H,E             
6107: AC         XOR     H               
6108: AC         XOR     H               
6109: AC         XOR     H               
610A: 00         NOP                     
610B: 9A         SBC     D               
610C: C0         RET     NZ              
610D: 13         INC     DE              
610E: AC         XOR     H               
610F: AC         XOR     H               
6110: AC         XOR     H               
6111: AC         XOR     H               
6112: AC         XOR     H               
6113: AC         XOR     H               
6114: AC         XOR     H               
6115: AC         XOR     H               
6116: AC         XOR     H               
6117: AC         XOR     H               
6118: AC         XOR     H               
6119: AC         XOR     H               
611A: AC         XOR     H               
611B: 50         LD      D,B             
611C: 51         LD      D,C             
611D: 52         LD      D,D             
611E: 53         LD      D,E             
611F: AC         XOR     H               
6120: AC         XOR     H               
6121: AC         XOR     H               
6122: 00         NOP                     
6123: 9A         SBC     D               
6124: A0         AND     B               
6125: 13         INC     DE              
6126: AC         XOR     H               
6127: AC         XOR     H               
6128: AC         XOR     H               
6129: AC         XOR     H               
612A: AC         XOR     H               
612B: AC         XOR     H               
612C: AC         XOR     H               
612D: AC         XOR     H               
612E: AC         XOR     H               
612F: AC         XOR     H               
6130: AC         XOR     H               
6131: AC         XOR     H               
6132: AC         XOR     H               
6133: AC         XOR     H               
6134: AC         XOR     H               
6135: AC         XOR     H               
6136: AC         XOR     H               
6137: AC         XOR     H               
6138: AC         XOR     H               
6139: AC         XOR     H               
613A: 00         NOP                     
613B: 9A         SBC     D               
613C: 80         ADD     A,B             
613D: 13         INC     DE              
613E: AC         XOR     H               
613F: AC         XOR     H               
6140: AC         XOR     H               
6141: AC         XOR     H               
6142: AC         XOR     H               
6143: AC         XOR     H               
6144: AC         XOR     H               
6145: AC         XOR     H               
6146: AC         XOR     H               
6147: AC         XOR     H               
6148: AC         XOR     H               
6149: AC         XOR     H               
614A: AC         XOR     H               
614B: AC         XOR     H               
614C: AC         XOR     H               
614D: AC         XOR     H               
614E: AC         XOR     H               
614F: AC         XOR     H               
6150: AC         XOR     H               
6151: AC         XOR     H               
6152: 00         NOP                     
6153: 9A         SBC     D               
6154: 60         LD      H,B             
6155: 13         INC     DE              
6156: AC         XOR     H               
6157: AC         XOR     H               
6158: AC         XOR     H               
6159: AC         XOR     H               
615A: AC         XOR     H               
615B: AC         XOR     H               
615C: AC         XOR     H               
615D: AC         XOR     H               
615E: AC         XOR     H               
615F: AC         XOR     H               
6160: AC         XOR     H               
6161: AC         XOR     H               
6162: AC         XOR     H               
6163: AC         XOR     H               
6164: AC         XOR     H               
6165: AC         XOR     H               
6166: AC         XOR     H               
6167: AC         XOR     H               
6168: 60         LD      H,B             
6169: 61         LD      H,C             
616A: 00         NOP                     
616B: 9A         SBC     D               
616C: 40         LD      B,B             
616D: 13         INC     DE              
616E: AC         XOR     H               
616F: AC         XOR     H               
6170: AC         XOR     H               
6171: AC         XOR     H               
6172: AC         XOR     H               
6173: AC         XOR     H               
6174: AC         XOR     H               
6175: AC         XOR     H               
6176: AC         XOR     H               
6177: AC         XOR     H               
6178: AC         XOR     H               
6179: AC         XOR     H               
617A: AC         XOR     H               
617B: AC         XOR     H               
617C: AC         XOR     H               
617D: AC         XOR     H               
617E: AC         XOR     H               
617F: AC         XOR     H               
6180: 50         LD      D,B             
6181: 51         LD      D,C             
6182: 00         NOP                     
6183: 9A         SBC     D               
6184: 20 13      JR      NZ,$6199        
6186: AC         XOR     H               
6187: AC         XOR     H               
6188: AC         XOR     H               
6189: AC         XOR     H               
618A: AC         XOR     H               
618B: AC         XOR     H               
618C: AC         XOR     H               
618D: AC         XOR     H               
618E: AC         XOR     H               
618F: AC         XOR     H               
6190: AC         XOR     H               
6191: AC         XOR     H               
6192: AC         XOR     H               
6193: AC         XOR     H               
6194: AC         XOR     H               
6195: AC         XOR     H               
6196: AC         XOR     H               
6197: AC         XOR     H               
6198: AC         XOR     H               
6199: AC         XOR     H               
619A: 00         NOP                     
619B: 9A         SBC     D               
619C: 00         NOP                     
619D: 13         INC     DE              
619E: 6B         LD      L,E             
619F: 6C         LD      L,H             
61A0: 6D         LD      L,L             
61A1: AC         XOR     H               
61A2: AC         XOR     H               
61A3: AC         XOR     H               
61A4: AC         XOR     H               
61A5: AC         XOR     H               
61A6: AC         XOR     H               
61A7: AC         XOR     H               
61A8: AC         XOR     H               
61A9: AC         XOR     H               
61AA: AC         XOR     H               
61AB: AC         XOR     H               
61AC: AC         XOR     H               
61AD: AC         XOR     H               
61AE: AC         XOR     H               
61AF: AC         XOR     H               
61B0: AC         XOR     H               
61B1: AC         XOR     H               
61B2: 00         NOP                     
61B3: 99         SBC     C               
61B4: E0 13      LDFF00  ($13),A         
61B6: 5B         LD      E,E             
61B7: 5C         LD      E,H             
61B8: 5D         LD      E,L             
61B9: AC         XOR     H               
61BA: AC         XOR     H               
61BB: AC         XOR     H               
61BC: AC         XOR     H               
61BD: AC         XOR     H               
61BE: AC         XOR     H               
61BF: AC         XOR     H               
61C0: AC         XOR     H               
61C1: AC         XOR     H               
61C2: 68         LD      L,B             
61C3: 69         LD      L,C             
61C4: 6A         LD      L,D             
61C5: 6B         LD      L,E             
61C6: 6C         LD      L,H             
61C7: 6D         LD      L,L             
61C8: AC         XOR     H               
61C9: AC         XOR     H               
61CA: 00         NOP                     
61CB: 99         SBC     C               
61CC: C0         RET     NZ              
61CD: 13         INC     DE              
61CE: AC         XOR     H               
61CF: AC         XOR     H               
61D0: AC         XOR     H               
61D1: AC         XOR     H               
61D2: AC         XOR     H               
61D3: AC         XOR     H               
61D4: AC         XOR     H               
61D5: AC         XOR     H               
61D6: AC         XOR     H               
61D7: AC         XOR     H               
61D8: AC         XOR     H               
61D9: AC         XOR     H               
61DA: 58         LD      E,B             
61DB: 59         LD      E,C             
61DC: 5A         LD      E,D             
61DD: 5B         LD      E,E             
61DE: 5C         LD      E,H             
61DF: 5D         LD      E,L             
61E0: AC         XOR     H               
61E1: AC         XOR     H               
61E2: 00         NOP                     
61E3: 99         SBC     C               
61E4: A0         AND     B               
61E5: 13         INC     DE              
61E6: AC         XOR     H               
61E7: AC         XOR     H               
61E8: AC         XOR     H               
61E9: AC         XOR     H               
61EA: AC         XOR     H               
61EB: AC         XOR     H               
61EC: AC         XOR     H               
61ED: AC         XOR     H               
61EE: AC         XOR     H               
61EF: AC         XOR     H               
61F0: AC         XOR     H               
61F1: AC         XOR     H               
61F2: AC         XOR     H               
61F3: AC         XOR     H               
61F4: AC         XOR     H               
61F5: AC         XOR     H               
61F6: AC         XOR     H               
61F7: AC         XOR     H               
61F8: AC         XOR     H               
61F9: AC         XOR     H               
61FA: 00         NOP                     
61FB: 99         SBC     C               
61FC: 80         ADD     A,B             
61FD: 13         INC     DE              
61FE: AC         XOR     H               
61FF: AC         XOR     H               
6200: AC         XOR     H               
6201: AC         XOR     H               
6202: AC         XOR     H               
6203: AC         XOR     H               
6204: AC         XOR     H               
6205: AC         XOR     H               
6206: AC         XOR     H               
6207: AC         XOR     H               
6208: AC         XOR     H               
6209: AC         XOR     H               
620A: AC         XOR     H               
620B: AC         XOR     H               
620C: AC         XOR     H               
620D: AC         XOR     H               
620E: AC         XOR     H               
620F: AC         XOR     H               
6210: AC         XOR     H               
6211: AC         XOR     H               
6212: 00         NOP                     
6213: 99         SBC     C               
6214: 60         LD      H,B             
6215: 13         INC     DE              
6216: AC         XOR     H               
6217: AC         XOR     H               
6218: AC         XOR     H               
6219: AC         XOR     H               
621A: AC         XOR     H               
621B: AC         XOR     H               
621C: AC         XOR     H               
621D: AC         XOR     H               
621E: AC         XOR     H               
621F: AC         XOR     H               
6220: AC         XOR     H               
6221: AC         XOR     H               
6222: AC         XOR     H               
6223: AC         XOR     H               
6224: AC         XOR     H               
6225: AC         XOR     H               
6226: AC         XOR     H               
6227: AC         XOR     H               
6228: 68         LD      L,B             
6229: 69         LD      L,C             
622A: 00         NOP                     
622B: 99         SBC     C               
622C: 40         LD      B,B             
622D: 13         INC     DE              
622E: AC         XOR     H               
622F: AC         XOR     H               
6230: AC         XOR     H               
6231: AC         XOR     H               
6232: 68         LD      L,B             
6233: 69         LD      L,C             
6234: 6A         LD      L,D             
6235: 6B         LD      L,E             
6236: 6C         LD      L,H             
6237: 6D         LD      L,L             
6238: AC         XOR     H               
6239: AC         XOR     H               
623A: AC         XOR     H               
623B: AC         XOR     H               
623C: AC         XOR     H               
623D: AC         XOR     H               
623E: AC         XOR     H               
623F: AC         XOR     H               
6240: 58         LD      E,B             
6241: 59         LD      E,C             
6242: 00         NOP                     
6243: 99         SBC     C               
6244: 20 13      JR      NZ,$6259        
6246: AC         XOR     H               
6247: AC         XOR     H               
6248: AC         XOR     H               
6249: AC         XOR     H               
624A: 58         LD      E,B             
624B: 59         LD      E,C             
624C: 5A         LD      E,D             
624D: 5B         LD      E,E             
624E: 5C         LD      E,H             
624F: 5D         LD      E,L             
6250: AC         XOR     H               
6251: AC         XOR     H               
6252: AC         XOR     H               
6253: AC         XOR     H               
6254: AC         XOR     H               
6255: AC         XOR     H               
6256: AC         XOR     H               
6257: AC         XOR     H               
6258: AC         XOR     H               
6259: AC         XOR     H               
625A: 00         NOP                     
625B: 99         SBC     C               
625C: 00         NOP                     
625D: 13         INC     DE              
625E: AC         XOR     H               
625F: AC         XOR     H               
6260: AC         XOR     H               
6261: AC         XOR     H               
6262: AC         XOR     H               
6263: AC         XOR     H               
6264: AC         XOR     H               
6265: AC         XOR     H               
6266: AC         XOR     H               
6267: AC         XOR     H               
6268: AC         XOR     H               
6269: AC         XOR     H               
626A: AC         XOR     H               
626B: AC         XOR     H               
626C: AC         XOR     H               
626D: AC         XOR     H               
626E: AC         XOR     H               
626F: AC         XOR     H               
6270: AC         XOR     H               
6271: AC         XOR     H               
6272: 00         NOP                     
6273: 98         SBC     B               
6274: E0 13      LDFF00  ($13),A         
6276: AC         XOR     H               
6277: AC         XOR     H               
6278: AC         XOR     H               
6279: AC         XOR     H               
627A: AC         XOR     H               
627B: AC         XOR     H               
627C: AC         XOR     H               
627D: AC         XOR     H               
627E: AC         XOR     H               
627F: AC         XOR     H               
6280: AC         XOR     H               
6281: AC         XOR     H               
6282: AC         XOR     H               
6283: AC         XOR     H               
6284: AC         XOR     H               
6285: AC         XOR     H               
6286: AC         XOR     H               
6287: AC         XOR     H               
6288: AC         XOR     H               
6289: AC         XOR     H               
628A: 00         NOP                     
628B: 98         SBC     B               
628C: C0         RET     NZ              
628D: 13         INC     DE              
628E: AC         XOR     H               
628F: AC         XOR     H               
6290: AC         XOR     H               
6291: AC         XOR     H               
6292: AC         XOR     H               
6293: AC         XOR     H               
6294: AC         XOR     H               
6295: AC         XOR     H               
6296: AC         XOR     H               
6297: AC         XOR     H               
6298: AC         XOR     H               
6299: AC         XOR     H               
629A: AC         XOR     H               
629B: AC         XOR     H               
629C: AC         XOR     H               
629D: AC         XOR     H               
629E: AC         XOR     H               
629F: AC         XOR     H               
62A0: AC         XOR     H               
62A1: AC         XOR     H               
62A2: 00         NOP                     
62A3: 98         SBC     B               
62A4: A0         AND     B               
62A5: 13         INC     DE              
62A6: AC         XOR     H               
62A7: AC         XOR     H               
62A8: AC         XOR     H               
62A9: AC         XOR     H               
62AA: AC         XOR     H               
62AB: AC         XOR     H               
62AC: AC         XOR     H               
62AD: AC         XOR     H               
62AE: AC         XOR     H               
62AF: AC         XOR     H               
62B0: AC         XOR     H               
62B1: AC         XOR     H               
62B2: AC         XOR     H               
62B3: AC         XOR     H               
62B4: AC         XOR     H               
62B5: AC         XOR     H               
62B6: AC         XOR     H               
62B7: AC         XOR     H               
62B8: AC         XOR     H               
62B9: AC         XOR     H               
62BA: 00         NOP                     
62BB: 98         SBC     B               
62BC: 80         ADD     A,B             
62BD: 13         INC     DE              
62BE: AC         XOR     H               
62BF: AC         XOR     H               
62C0: AC         XOR     H               
62C1: AC         XOR     H               
62C2: AC         XOR     H               
62C3: AC         XOR     H               
62C4: AC         XOR     H               
62C5: AC         XOR     H               
62C6: AC         XOR     H               
62C7: AC         XOR     H               
62C8: AC         XOR     H               
62C9: AC         XOR     H               
62CA: AC         XOR     H               
62CB: AC         XOR     H               
62CC: AC         XOR     H               
62CD: AC         XOR     H               
62CE: AC         XOR     H               
62CF: AC         XOR     H               
62D0: AC         XOR     H               
62D1: AC         XOR     H               
62D2: 00         NOP                     
62D3: 98         SBC     B               
62D4: 60         LD      H,B             
62D5: 13         INC     DE              
62D6: AC         XOR     H               
62D7: AC         XOR     H               
62D8: AC         XOR     H               
62D9: AC         XOR     H               
62DA: AC         XOR     H               
62DB: AC         XOR     H               
62DC: AC         XOR     H               
62DD: AC         XOR     H               
62DE: AC         XOR     H               
62DF: AC         XOR     H               
62E0: AC         XOR     H               
62E1: AC         XOR     H               
62E2: AC         XOR     H               
62E3: AC         XOR     H               
62E4: AC         XOR     H               
62E5: AC         XOR     H               
62E6: AC         XOR     H               
62E7: AC         XOR     H               
62E8: AC         XOR     H               
62E9: AC         XOR     H               
62EA: 00         NOP                     
62EB: 98         SBC     B               
62EC: 40         LD      B,B             
62ED: 13         INC     DE              
62EE: AC         XOR     H               
62EF: AC         XOR     H               
62F0: AC         XOR     H               
62F1: AC         XOR     H               
62F2: AC         XOR     H               
62F3: AC         XOR     H               
62F4: AC         XOR     H               
62F5: AC         XOR     H               
62F6: AC         XOR     H               
62F7: AC         XOR     H               
62F8: AC         XOR     H               
62F9: AC         XOR     H               
62FA: AC         XOR     H               
62FB: AC         XOR     H               
62FC: AC         XOR     H               
62FD: AC         XOR     H               
62FE: AC         XOR     H               
62FF: AC         XOR     H               
6300: AC         XOR     H               
6301: AC         XOR     H               
6302: 00         NOP                     
6303: 98         SBC     B               
6304: 20 13      JR      NZ,$6319        
6306: AC         XOR     H               
6307: AC         XOR     H               
6308: AC         XOR     H               
6309: AC         XOR     H               
630A: AC         XOR     H               
630B: AC         XOR     H               
630C: AC         XOR     H               
630D: AC         XOR     H               
630E: AC         XOR     H               
630F: AC         XOR     H               
6310: AC         XOR     H               
6311: AC         XOR     H               
6312: AC         XOR     H               
6313: AC         XOR     H               
6314: AC         XOR     H               
6315: AC         XOR     H               
6316: 40         LD      B,B             
6317: 41         LD      B,C             
6318: 42         LD      B,D             
6319: 43         LD      B,E             
631A: 00         NOP                     
631B: 98         SBC     B               
631C: 00         NOP                     
631D: 13         INC     DE              
631E: AC         XOR     H               
631F: AC         XOR     H               
6320: AC         XOR     H               
6321: AC         XOR     H               
6322: AC         XOR     H               
6323: AC         XOR     H               
6324: AC         XOR     H               
6325: AC         XOR     H               
6326: AC         XOR     H               
6327: AC         XOR     H               
6328: AC         XOR     H               
6329: AC         XOR     H               
632A: AC         XOR     H               
632B: AC         XOR     H               
632C: AC         XOR     H               
632D: AC         XOR     H               
632E: 1B         DEC     DE              
632F: 2E 2E      LD      L,$2E           
6331: 2E 00      LD      L,$00           
6333: 9B         SBC     E               
6334: E0 13      LDFF00  ($13),A         
6336: 41         LD      B,C             
6337: 42         LD      B,D             
6338: 43         LD      B,E             
6339: 54         LD      D,H             
633A: 55         LD      D,L             
633B: AC         XOR     H               
633C: AC         XOR     H               
633D: AC         XOR     H               
633E: AC         XOR     H               
633F: AC         XOR     H               
6340: AC         XOR     H               
6341: AC         XOR     H               
6342: AC         XOR     H               
6343: AC         XOR     H               
6344: AC         XOR     H               
6345: AC         XOR     H               
6346: 9C         SBC     H               
6347: 9E         SBC     (HL)            
6348: BE         CP      (HL)            
6349: E9         JP      (HL)            
634A: 00         NOP                     
634B: 9B         SBC     E               
634C: C0         RET     NZ              
634D: 13         INC     DE              
634E: 2E 2E      LD      L,$2E           
6350: 2E 2E      LD      L,$2E           
6352: 2F         CPL                     
6353: AC         XOR     H               
6354: AC         XOR     H               
6355: AC         XOR     H               
6356: AC         XOR     H               
6357: AC         XOR     H               
6358: AC         XOR     H               
6359: AC         XOR     H               
635A: AC         XOR     H               
635B: AC         XOR     H               
635C: AC         XOR     H               
635D: AC         XOR     H               
635E: AC         XOR     H               
635F: AC         XOR     H               
6360: AC         XOR     H               
6361: AC         XOR     H               
6362: 00         NOP                     
6363: 9B         SBC     E               
6364: A0         AND     B               
6365: 13         INC     DE              
6366: 9E         SBC     (HL)            
6367: BE         CP      (HL)            
6368: E9         JP      (HL)            
6369: F9         LD      SP,HL           
636A: FB         EI                      
636B: AC         XOR     H               
636C: AC         XOR     H               
636D: AC         XOR     H               
636E: AC         XOR     H               
636F: AC         XOR     H               
6370: AC         XOR     H               
6371: AC         XOR     H               
6372: AC         XOR     H               
6373: AC         XOR     H               
6374: AC         XOR     H               
6375: AC         XOR     H               
6376: AC         XOR     H               
6377: AC         XOR     H               
6378: AC         XOR     H               
6379: AC         XOR     H               
637A: 00         NOP                     
637B: 9B         SBC     E               
637C: 80         ADD     A,B             
637D: 13         INC     DE              
637E: AC         XOR     H               
637F: AC         XOR     H               
6380: AC         XOR     H               
6381: AC         XOR     H               
6382: AC         XOR     H               
6383: AC         XOR     H               
6384: AC         XOR     H               
6385: AC         XOR     H               
6386: AC         XOR     H               
6387: AC         XOR     H               
6388: AC         XOR     H               
6389: AC         XOR     H               
638A: AC         XOR     H               
638B: AC         XOR     H               
638C: AC         XOR     H               
638D: AC         XOR     H               
638E: AC         XOR     H               
638F: AC         XOR     H               
6390: AC         XOR     H               
6391: AC         XOR     H               
6392: 00         NOP                     
6393: 9B         SBC     E               
6394: 60         LD      H,B             
6395: 13         INC     DE              
6396: AC         XOR     H               
6397: AC         XOR     H               
6398: AC         XOR     H               
6399: AC         XOR     H               
639A: AC         XOR     H               
639B: AC         XOR     H               
639C: AC         XOR     H               
639D: AC         XOR     H               
639E: AC         XOR     H               
639F: AC         XOR     H               
63A0: AC         XOR     H               
63A1: AC         XOR     H               
63A2: AC         XOR     H               
63A3: AC         XOR     H               
63A4: AC         XOR     H               
63A5: AC         XOR     H               
63A6: AC         XOR     H               
63A7: AC         XOR     H               
63A8: AC         XOR     H               
63A9: AC         XOR     H               
63AA: 00         NOP                     
63AB: 9B         SBC     E               
63AC: 40         LD      B,B             
63AD: 13         INC     DE              
63AE: 43         LD      B,E             
63AF: 54         LD      D,H             
63B0: 55         LD      D,L             
63B1: AC         XOR     H               
63B2: AC         XOR     H               
63B3: AC         XOR     H               
63B4: AC         XOR     H               
63B5: AC         XOR     H               
63B6: AC         XOR     H               
63B7: AC         XOR     H               
63B8: AC         XOR     H               
63B9: AC         XOR     H               
63BA: AC         XOR     H               
63BB: AC         XOR     H               
63BC: AC         XOR     H               
63BD: AC         XOR     H               
63BE: AC         XOR     H               
63BF: AC         XOR     H               
63C0: AC         XOR     H               
63C1: AC         XOR     H               
63C2: 00         NOP                     
63C3: 9B         SBC     E               
63C4: 20 13      JR      NZ,$63D9        
63C6: 2E 2E      LD      L,$2E           
63C8: 2F         CPL                     
63C9: AC         XOR     H               
63CA: AC         XOR     H               
63CB: AC         XOR     H               
63CC: AC         XOR     H               
63CD: AC         XOR     H               
63CE: AC         XOR     H               
63CF: AC         XOR     H               
63D0: AC         XOR     H               
63D1: AC         XOR     H               
63D2: AC         XOR     H               
63D3: AC         XOR     H               
63D4: AC         XOR     H               
63D5: AC         XOR     H               
63D6: AC         XOR     H               
63D7: AC         XOR     H               
63D8: AC         XOR     H               
63D9: AC         XOR     H               
63DA: 00         NOP                     
63DB: 9B         SBC     E               
63DC: 00         NOP                     
63DD: 13         INC     DE              
63DE: E9         JP      (HL)            
63DF: F9         LD      SP,HL           
63E0: FB         EI                      
63E1: AC         XOR     H               
63E2: AC         XOR     H               
63E3: AC         XOR     H               
63E4: AC         XOR     H               
63E5: AC         XOR     H               
63E6: AC         XOR     H               
63E7: AC         XOR     H               
63E8: AC         XOR     H               
63E9: AC         XOR     H               
63EA: AC         XOR     H               
63EB: AC         XOR     H               
63EC: AC         XOR     H               
63ED: AC         XOR     H               
63EE: AC         XOR     H               
63EF: AC         XOR     H               
63F0: AC         XOR     H               
63F1: AC         XOR     H               
63F2: 00         NOP                     
63F3: 9A         SBC     D               
63F4: E0 13      LDFF00  ($13),A         
63F6: AC         XOR     H               
63F7: AC         XOR     H               
63F8: AC         XOR     H               
63F9: AC         XOR     H               
63FA: AC         XOR     H               
63FB: AC         XOR     H               
63FC: AC         XOR     H               
63FD: AC         XOR     H               
63FE: AC         XOR     H               
63FF: AC         XOR     H               
6400: AC         XOR     H               
6401: AC         XOR     H               
6402: AC         XOR     H               
6403: AC         XOR     H               
6404: AC         XOR     H               
6405: AC         XOR     H               
6406: AC         XOR     H               
6407: AC         XOR     H               
6408: AC         XOR     H               
6409: AC         XOR     H               
640A: 00         NOP                     
640B: 9A         SBC     D               
640C: C0         RET     NZ              
640D: 13         INC     DE              
640E: AC         XOR     H               
640F: AC         XOR     H               
6410: AC         XOR     H               
6411: AC         XOR     H               
6412: AC         XOR     H               
6413: AC         XOR     H               
6414: AC         XOR     H               
6415: AC         XOR     H               
6416: AC         XOR     H               
6417: AC         XOR     H               
6418: AC         XOR     H               
6419: AC         XOR     H               
641A: AC         XOR     H               
641B: AC         XOR     H               
641C: AC         XOR     H               
641D: AC         XOR     H               
641E: AC         XOR     H               
641F: AC         XOR     H               
6420: AC         XOR     H               
6421: AC         XOR     H               
6422: 00         NOP                     
6423: 9A         SBC     D               
6424: A0         AND     B               
6425: 13         INC     DE              
6426: AC         XOR     H               
6427: AC         XOR     H               
6428: AC         XOR     H               
6429: AC         XOR     H               
642A: AC         XOR     H               
642B: AC         XOR     H               
642C: AC         XOR     H               
642D: AC         XOR     H               
642E: AC         XOR     H               
642F: AC         XOR     H               
6430: AC         XOR     H               
6431: AC         XOR     H               
6432: AC         XOR     H               
6433: AC         XOR     H               
6434: AC         XOR     H               
6435: AC         XOR     H               
6436: AC         XOR     H               
6437: AC         XOR     H               
6438: AC         XOR     H               
6439: AC         XOR     H               
643A: 00         NOP                     
643B: 9A         SBC     D               
643C: 80         ADD     A,B             
643D: 13         INC     DE              
643E: AC         XOR     H               
643F: AC         XOR     H               
6440: AC         XOR     H               
6441: AC         XOR     H               
6442: AC         XOR     H               
6443: AC         XOR     H               
6444: AC         XOR     H               
6445: 40         LD      B,B             
6446: 41         LD      B,C             
6447: 42         LD      B,D             
6448: 43         LD      B,E             
6449: 54         LD      D,H             
644A: 55         LD      D,L             
644B: AC         XOR     H               
644C: AC         XOR     H               
644D: AC         XOR     H               
644E: AC         XOR     H               
644F: AC         XOR     H               
6450: AC         XOR     H               
6451: AC         XOR     H               
6452: 00         NOP                     
6453: 9A         SBC     D               
6454: 60         LD      H,B             
6455: 13         INC     DE              
6456: AC         XOR     H               
6457: AC         XOR     H               
6458: AC         XOR     H               
6459: AC         XOR     H               
645A: AC         XOR     H               
645B: AC         XOR     H               
645C: AC         XOR     H               
645D: 1B         DEC     DE              
645E: 2E 2E      LD      L,$2E           
6460: 2E 2E      LD      L,$2E           
6462: 2F         CPL                     
6463: AC         XOR     H               
6464: AC         XOR     H               
6465: AC         XOR     H               
6466: AC         XOR     H               
6467: AC         XOR     H               
6468: AC         XOR     H               
6469: AC         XOR     H               
646A: 00         NOP                     
646B: 9A         SBC     D               
646C: 40         LD      B,B             
646D: 13         INC     DE              
646E: AC         XOR     H               
646F: AC         XOR     H               
6470: AC         XOR     H               
6471: AC         XOR     H               
6472: AC         XOR     H               
6473: AC         XOR     H               
6474: AC         XOR     H               
6475: 9C         SBC     H               
6476: 9E         SBC     (HL)            
6477: BE         CP      (HL)            
6478: E9         JP      (HL)            
6479: F9         LD      SP,HL           
647A: FB         EI                      
647B: AC         XOR     H               
647C: AC         XOR     H               
647D: AC         XOR     H               
647E: AC         XOR     H               
647F: AC         XOR     H               
6480: AC         XOR     H               
6481: AC         XOR     H               
6482: 00         NOP                     
6483: 9A         SBC     D               
6484: 20 13      JR      NZ,$6499        
6486: AC         XOR     H               
6487: AC         XOR     H               
6488: AC         XOR     H               
6489: AC         XOR     H               
648A: AC         XOR     H               
648B: AC         XOR     H               
648C: AC         XOR     H               
648D: AC         XOR     H               
648E: AC         XOR     H               
648F: AC         XOR     H               
6490: AC         XOR     H               
6491: AC         XOR     H               
6492: AC         XOR     H               
6493: AC         XOR     H               
6494: AC         XOR     H               
6495: AC         XOR     H               
6496: AC         XOR     H               
6497: AC         XOR     H               
6498: AC         XOR     H               
6499: AC         XOR     H               
649A: 00         NOP                     
649B: 9A         SBC     D               
649C: 00         NOP                     
649D: 13         INC     DE              
649E: AC         XOR     H               
649F: AC         XOR     H               
64A0: AC         XOR     H               
64A1: AC         XOR     H               
64A2: AC         XOR     H               
64A3: AC         XOR     H               
64A4: AC         XOR     H               
64A5: AC         XOR     H               
64A6: AC         XOR     H               
64A7: AC         XOR     H               
64A8: AC         XOR     H               
64A9: AC         XOR     H               
64AA: AC         XOR     H               
64AB: AC         XOR     H               
64AC: AC         XOR     H               
64AD: AC         XOR     H               
64AE: AC         XOR     H               
64AF: AC         XOR     H               
64B0: AC         XOR     H               
64B1: AC         XOR     H               
64B2: 00         NOP                     
64B3: 99         SBC     C               
64B4: E0 13      LDFF00  ($13),A         
64B6: AC         XOR     H               
64B7: AC         XOR     H               
64B8: AC         XOR     H               
64B9: AC         XOR     H               
64BA: AC         XOR     H               
64BB: AC         XOR     H               
64BC: AC         XOR     H               
64BD: AC         XOR     H               
64BE: AC         XOR     H               
64BF: AC         XOR     H               
64C0: AC         XOR     H               
64C1: AC         XOR     H               
64C2: AC         XOR     H               
64C3: AC         XOR     H               
64C4: AC         XOR     H               
64C5: AC         XOR     H               
64C6: AC         XOR     H               
64C7: AC         XOR     H               
64C8: AC         XOR     H               
64C9: AC         XOR     H               
64CA: 00         NOP                     
64CB: 99         SBC     C               
64CC: C0         RET     NZ              
64CD: 13         INC     DE              
64CE: AC         XOR     H               
64CF: AC         XOR     H               
64D0: AC         XOR     H               
64D1: AC         XOR     H               
64D2: AC         XOR     H               
64D3: AC         XOR     H               
64D4: AC         XOR     H               
64D5: AC         XOR     H               
64D6: AC         XOR     H               
64D7: AC         XOR     H               
64D8: AC         XOR     H               
64D9: AC         XOR     H               
64DA: AC         XOR     H               
64DB: AC         XOR     H               
64DC: AC         XOR     H               
64DD: AC         XOR     H               
64DE: AC         XOR     H               
64DF: AC         XOR     H               
64E0: AC         XOR     H               
64E1: AC         XOR     H               
64E2: 00         NOP                     
64E3: 99         SBC     C               
64E4: A0         AND     B               
64E5: 13         INC     DE              
64E6: AC         XOR     H               
64E7: AC         XOR     H               
64E8: AC         XOR     H               
64E9: AC         XOR     H               
64EA: AC         XOR     H               
64EB: AC         XOR     H               
64EC: AC         XOR     H               
64ED: AC         XOR     H               
64EE: AC         XOR     H               
64EF: AC         XOR     H               
64F0: AC         XOR     H               
64F1: AC         XOR     H               
64F2: AC         XOR     H               
64F3: AC         XOR     H               
64F4: AC         XOR     H               
64F5: AC         XOR     H               
64F6: AC         XOR     H               
64F7: AC         XOR     H               
64F8: AC         XOR     H               
64F9: AC         XOR     H               
64FA: 00         NOP                     
64FB: 99         SBC     C               
64FC: 80         ADD     A,B             
64FD: 13         INC     DE              
64FE: AC         XOR     H               
64FF: AC         XOR     H               
6500: AC         XOR     H               
6501: AC         XOR     H               
6502: AC         XOR     H               
6503: AC         XOR     H               
6504: AC         XOR     H               
6505: AC         XOR     H               
6506: AC         XOR     H               
6507: AC         XOR     H               
6508: AC         XOR     H               
6509: AC         XOR     H               
650A: AC         XOR     H               
650B: AC         XOR     H               
650C: AC         XOR     H               
650D: AC         XOR     H               
650E: 40         LD      B,B             
650F: 41         LD      B,C             
6510: 42         LD      B,D             
6511: 43         LD      B,E             
6512: 00         NOP                     
6513: 99         SBC     C               
6514: 60         LD      H,B             
6515: 13         INC     DE              
6516: AC         XOR     H               
6517: AC         XOR     H               
6518: AC         XOR     H               
6519: AC         XOR     H               
651A: AC         XOR     H               
651B: AC         XOR     H               
651C: AC         XOR     H               
651D: AC         XOR     H               
651E: AC         XOR     H               
651F: AC         XOR     H               
6520: AC         XOR     H               
6521: AC         XOR     H               
6522: AC         XOR     H               
6523: AC         XOR     H               
6524: AC         XOR     H               
6525: AC         XOR     H               
6526: 1B         DEC     DE              
6527: 2E 2E      LD      L,$2E           
6529: 2E 00      LD      L,$00           
652B: 99         SBC     C               
652C: 40         LD      B,B             
652D: 13         INC     DE              
652E: 40         LD      B,B             
652F: 41         LD      B,C             
6530: 42         LD      B,D             
6531: 43         LD      B,E             
6532: 54         LD      D,H             
6533: 55         LD      D,L             
6534: AC         XOR     H               
6535: AC         XOR     H               
6536: AC         XOR     H               
6537: AC         XOR     H               
6538: AC         XOR     H               
6539: AC         XOR     H               
653A: AC         XOR     H               
653B: AC         XOR     H               
653C: AC         XOR     H               
653D: AC         XOR     H               
653E: 9C         SBC     H               
653F: 9E         SBC     (HL)            
6540: BE         CP      (HL)            
6541: E9         JP      (HL)            
6542: 00         NOP                     
6543: 99         SBC     C               
6544: 20 13      JR      NZ,$6559        
6546: 1B         DEC     DE              
6547: 2E 2E      LD      L,$2E           
6549: 2E 2E      LD      L,$2E           
654B: 2F         CPL                     
654C: AC         XOR     H               
654D: AC         XOR     H               
654E: AC         XOR     H               
654F: AC         XOR     H               
6550: AC         XOR     H               
6551: AC         XOR     H               
6552: AC         XOR     H               
6553: AC         XOR     H               
6554: AC         XOR     H               
6555: AC         XOR     H               
6556: AC         XOR     H               
6557: AC         XOR     H               
6558: AC         XOR     H               
6559: AC         XOR     H               
655A: 00         NOP                     
655B: 99         SBC     C               
655C: 00         NOP                     
655D: 13         INC     DE              
655E: 9C         SBC     H               
655F: 9E         SBC     (HL)            
6560: BE         CP      (HL)            
6561: E9         JP      (HL)            
6562: F9         LD      SP,HL           
6563: FB         EI                      
6564: AC         XOR     H               
6565: AC         XOR     H               
6566: AC         XOR     H               
6567: AC         XOR     H               
6568: AC         XOR     H               
6569: AC         XOR     H               
656A: AC         XOR     H               
656B: AC         XOR     H               
656C: AC         XOR     H               
656D: AC         XOR     H               
656E: AC         XOR     H               
656F: AC         XOR     H               
6570: AC         XOR     H               
6571: AC         XOR     H               
6572: 00         NOP                     
6573: 98         SBC     B               
6574: E0 13      LDFF00  ($13),A         
6576: AC         XOR     H               
6577: AC         XOR     H               
6578: AC         XOR     H               
6579: AC         XOR     H               
657A: AC         XOR     H               
657B: AC         XOR     H               
657C: AC         XOR     H               
657D: AC         XOR     H               
657E: AC         XOR     H               
657F: AC         XOR     H               
6580: AC         XOR     H               
6581: AC         XOR     H               
6582: AC         XOR     H               
6583: AC         XOR     H               
6584: AC         XOR     H               
6585: AC         XOR     H               
6586: AC         XOR     H               
6587: AC         XOR     H               
6588: AC         XOR     H               
6589: AC         XOR     H               
658A: 00         NOP                     
658B: 98         SBC     B               
658C: C0         RET     NZ              
658D: 13         INC     DE              
658E: AC         XOR     H               
658F: AC         XOR     H               
6590: AC         XOR     H               
6591: AC         XOR     H               
6592: AC         XOR     H               
6593: AC         XOR     H               
6594: AC         XOR     H               
6595: AC         XOR     H               
6596: AC         XOR     H               
6597: AC         XOR     H               
6598: AC         XOR     H               
6599: AC         XOR     H               
659A: AC         XOR     H               
659B: AC         XOR     H               
659C: AC         XOR     H               
659D: AC         XOR     H               
659E: AC         XOR     H               
659F: AC         XOR     H               
65A0: AC         XOR     H               
65A1: AC         XOR     H               
65A2: 00         NOP                     
65A3: 98         SBC     B               
65A4: A0         AND     B               
65A5: 13         INC     DE              
65A6: AC         XOR     H               
65A7: AC         XOR     H               
65A8: AC         XOR     H               
65A9: AC         XOR     H               
65AA: AC         XOR     H               
65AB: AC         XOR     H               
65AC: AC         XOR     H               
65AD: AC         XOR     H               
65AE: AC         XOR     H               
65AF: AC         XOR     H               
65B0: AC         XOR     H               
65B1: AC         XOR     H               
65B2: AC         XOR     H               
65B3: AC         XOR     H               
65B4: AC         XOR     H               
65B5: AC         XOR     H               
65B6: AC         XOR     H               
65B7: AC         XOR     H               
65B8: AC         XOR     H               
65B9: AC         XOR     H               
65BA: 00         NOP                     
65BB: 98         SBC     B               
65BC: 80         ADD     A,B             
65BD: 13         INC     DE              
65BE: AC         XOR     H               
65BF: AC         XOR     H               
65C0: AC         XOR     H               
65C1: AC         XOR     H               
65C2: AC         XOR     H               
65C3: AC         XOR     H               
65C4: AC         XOR     H               
65C5: AC         XOR     H               
65C6: AC         XOR     H               
65C7: AC         XOR     H               
65C8: AC         XOR     H               
65C9: AC         XOR     H               
65CA: AC         XOR     H               
65CB: AC         XOR     H               
65CC: AC         XOR     H               
65CD: AC         XOR     H               
65CE: AC         XOR     H               
65CF: AC         XOR     H               
65D0: AC         XOR     H               
65D1: AC         XOR     H               
65D2: 00         NOP                     
65D3: 98         SBC     B               
65D4: 60         LD      H,B             
65D5: 13         INC     DE              
65D6: AC         XOR     H               
65D7: AC         XOR     H               
65D8: AC         XOR     H               
65D9: AC         XOR     H               
65DA: AC         XOR     H               
65DB: AC         XOR     H               
65DC: AC         XOR     H               
65DD: AC         XOR     H               
65DE: AC         XOR     H               
65DF: AC         XOR     H               
65E0: AC         XOR     H               
65E1: AC         XOR     H               
65E2: AC         XOR     H               
65E3: AC         XOR     H               
65E4: AC         XOR     H               
65E5: AC         XOR     H               
65E6: AC         XOR     H               
65E7: AC         XOR     H               
65E8: AC         XOR     H               
65E9: AC         XOR     H               
65EA: 00         NOP                     
65EB: 98         SBC     B               
65EC: 40         LD      B,B             
65ED: 13         INC     DE              
65EE: AC         XOR     H               
65EF: AC         XOR     H               
65F0: AC         XOR     H               
65F1: AC         XOR     H               
65F2: AC         XOR     H               
65F3: AC         XOR     H               
65F4: AC         XOR     H               
65F5: AC         XOR     H               
65F6: AC         XOR     H               
65F7: AC         XOR     H               
65F8: AC         XOR     H               
65F9: AC         XOR     H               
65FA: AC         XOR     H               
65FB: AC         XOR     H               
65FC: AC         XOR     H               
65FD: AC         XOR     H               
65FE: AC         XOR     H               
65FF: AC         XOR     H               
6600: AC         XOR     H               
6601: AC         XOR     H               
6602: 00         NOP                     
6603: 98         SBC     B               
6604: 20 13      JR      NZ,$6619        
6606: AC         XOR     H               
6607: AC         XOR     H               
6608: AC         XOR     H               
6609: AC         XOR     H               
660A: AC         XOR     H               
660B: AC         XOR     H               
660C: AC         XOR     H               
660D: AC         XOR     H               
660E: AC         XOR     H               
660F: AC         XOR     H               
6610: AC         XOR     H               
6611: AC         XOR     H               
6612: AC         XOR     H               
6613: AC         XOR     H               
6614: AC         XOR     H               
6615: AC         XOR     H               
6616: AC         XOR     H               
6617: AC         XOR     H               
6618: AC         XOR     H               
6619: AC         XOR     H               
661A: 00         NOP                     
661B: 98         SBC     B               
661C: 00         NOP                     
661D: 13         INC     DE              
661E: AC         XOR     H               
661F: AC         XOR     H               
6620: AC         XOR     H               
6621: AC         XOR     H               
6622: AC         XOR     H               
6623: AC         XOR     H               
6624: AC         XOR     H               
6625: AC         XOR     H               
6626: AC         XOR     H               
6627: AC         XOR     H               
6628: AC         XOR     H               
6629: AC         XOR     H               
662A: AC         XOR     H               
662B: AC         XOR     H               
662C: AC         XOR     H               
662D: AC         XOR     H               
662E: AC         XOR     H               
662F: AC         XOR     H               
6630: AC         XOR     H               
6631: AC         XOR     H               
6632: 00         NOP                     
6633: 9B         SBC     E               
6634: E0 13      LDFF00  ($13),A         
6636: AC         XOR     H               
6637: AC         XOR     H               
6638: AC         XOR     H               
6639: AC         XOR     H               
663A: AC         XOR     H               
663B: AC         XOR     H               
663C: AC         XOR     H               
663D: AC         XOR     H               
663E: AC         XOR     H               
663F: AC         XOR     H               
6640: AC         XOR     H               
6641: AC         XOR     H               
6642: AC         XOR     H               
6643: AC         XOR     H               
6644: AC         XOR     H               
6645: AC         XOR     H               
6646: AC         XOR     H               
6647: AC         XOR     H               
6648: AC         XOR     H               
6649: AC         XOR     H               
664A: 00         NOP                     
664B: 9B         SBC     E               
664C: C0         RET     NZ              
664D: 13         INC     DE              
664E: AC         XOR     H               
664F: AC         XOR     H               
6650: AC         XOR     H               
6651: AC         XOR     H               
6652: AC         XOR     H               
6653: AC         XOR     H               
6654: AC         XOR     H               
6655: AC         XOR     H               
6656: AC         XOR     H               
6657: AC         XOR     H               
6658: AC         XOR     H               
6659: AC         XOR     H               
665A: AC         XOR     H               
665B: AC         XOR     H               
665C: AC         XOR     H               
665D: AC         XOR     H               
665E: AC         XOR     H               
665F: AC         XOR     H               
6660: AC         XOR     H               
6661: AC         XOR     H               
6662: 00         NOP                     
6663: 9B         SBC     E               
6664: A0         AND     B               
6665: 13         INC     DE              
6666: AC         XOR     H               
6667: AC         XOR     H               
6668: AC         XOR     H               
6669: AC         XOR     H               
666A: AC         XOR     H               
666B: AC         XOR     H               
666C: AC         XOR     H               
666D: AC         XOR     H               
666E: AC         XOR     H               
666F: AC         XOR     H               
6670: AC         XOR     H               
6671: AC         XOR     H               
6672: AC         XOR     H               
6673: AC         XOR     H               
6674: AC         XOR     H               
6675: AC         XOR     H               
6676: AC         XOR     H               
6677: AC         XOR     H               
6678: AC         XOR     H               
6679: AC         XOR     H               
667A: 00         NOP                     
667B: 9B         SBC     E               
667C: 80         ADD     A,B             
667D: 13         INC     DE              
667E: AC         XOR     H               
667F: AC         XOR     H               
6680: AC         XOR     H               
6681: AC         XOR     H               
6682: AC         XOR     H               
6683: AC         XOR     H               
6684: AC         XOR     H               
6685: AC         XOR     H               
6686: AC         XOR     H               
6687: AC         XOR     H               
6688: AC         XOR     H               
6689: AC         XOR     H               
668A: AC         XOR     H               
668B: AC         XOR     H               
668C: AC         XOR     H               
668D: AC         XOR     H               
668E: AC         XOR     H               
668F: AC         XOR     H               
6690: AC         XOR     H               
6691: AC         XOR     H               
6692: 00         NOP                     
6693: 9B         SBC     E               
6694: 60         LD      H,B             
6695: 13         INC     DE              
6696: 3C         INC     A               
6697: AC         XOR     H               
6698: AC         XOR     H               
6699: AC         XOR     H               
669A: AC         XOR     H               
669B: AC         XOR     H               
669C: AC         XOR     H               
669D: AC         XOR     H               
669E: AC         XOR     H               
669F: AC         XOR     H               
66A0: AC         XOR     H               
66A1: AC         XOR     H               
66A2: AC         XOR     H               
66A3: AC         XOR     H               
66A4: AC         XOR     H               
66A5: AC         XOR     H               
66A6: AC         XOR     H               
66A7: AC         XOR     H               
66A8: AC         XOR     H               
66A9: AC         XOR     H               
66AA: 00         NOP                     
66AB: 9B         SBC     E               
66AC: 40         LD      B,B             
66AD: 13         INC     DE              
66AE: 2C         INC     L               
66AF: 2D         DEC     L               
66B0: AC         XOR     H               
66B1: AC         XOR     H               
66B2: AC         XOR     H               
66B3: AC         XOR     H               
66B4: AC         XOR     H               
66B5: AC         XOR     H               
66B6: 78         LD      A,B             
66B7: 79         LD      A,C             
66B8: 3C         INC     A               
66B9: AC         XOR     H               
66BA: AC         XOR     H               
66BB: AC         XOR     H               
66BC: AC         XOR     H               
66BD: AC         XOR     H               
66BE: AC         XOR     H               
66BF: AC         XOR     H               
66C0: AC         XOR     H               
66C1: AC         XOR     H               
66C2: 00         NOP                     
66C3: 9B         SBC     E               
66C4: 20 13      JR      NZ,$66D9        
66C6: AE         XOR     (HL)            
66C7: AE         XOR     (HL)            
66C8: 3D         DEC     A               
66C9: 3F         CCF                     
66CA: AC         XOR     H               
66CB: AC         XOR     H               
66CC: AC         XOR     H               
66CD: AC         XOR     H               
66CE: 45         LD      B,L             
66CF: AE         XOR     (HL)            
66D0: 2C         INC     L               
66D1: 2D         DEC     L               
66D2: AC         XOR     H               
66D3: AC         XOR     H               
66D4: AC         XOR     H               
66D5: 7B         LD      A,E             
66D6: 3D         DEC     A               
66D7: 3F         CCF                     
66D8: 78         LD      A,B             
66D9: 79         LD      A,C             
66DA: 00         NOP                     
66DB: 9B         SBC     E               
66DC: 00         NOP                     
66DD: 13         INC     DE              
66DE: AE         XOR     (HL)            
66DF: AE         XOR     (HL)            
66E0: AE         XOR     (HL)            
66E1: 3E AC      LD      A,$AC           
66E3: AC         XOR     H               
66E4: AC         XOR     H               
66E5: AC         XOR     H               
66E6: 72         LD      (HL),D          
66E7: AE         XOR     (HL)            
66E8: AE         XOR     (HL)            
66E9: 75         LD      (HL),L          
66EA: AC         XOR     H               
66EB: AC         XOR     H               
66EC: 7A         LD      A,D             
66ED: 4B         LD      C,E             
66EE: AE         XOR     (HL)            
66EF: 3E 45      LD      A,$45           
66F1: AE         XOR     (HL)            
66F2: 00         NOP                     
66F3: 9A         SBC     D               
66F4: E0 13      LDFF00  ($13),A         
66F6: AE         XOR     (HL)            
66F7: AE         XOR     (HL)            
66F8: AE         XOR     (HL)            
66F9: AE         XOR     (HL)            
66FA: 3D         DEC     A               
66FB: 3F         CCF                     
66FC: AC         XOR     H               
66FD: AC         XOR     H               
66FE: 56         LD      D,(HL)          
66FF: 73         LD      (HL),E          
6700: 74         LD      (HL),H          
6701: 67         LD      H,A             
6702: AC         XOR     H               
6703: AC         XOR     H               
6704: 72         LD      (HL),D          
6705: AE         XOR     (HL)            
6706: AE         XOR     (HL)            
6707: AE         XOR     (HL)            
6708: AE         XOR     (HL)            
6709: AE         XOR     (HL)            
670A: 00         NOP                     
670B: 9A         SBC     D               
670C: C0         RET     NZ              
670D: 13         INC     DE              
670E: AE         XOR     (HL)            
670F: AE         XOR     (HL)            
6710: AE         XOR     (HL)            
6711: AE         XOR     (HL)            
6712: AE         XOR     (HL)            
6713: 3E AC      LD      A,$AC           
6715: AC         XOR     H               
6716: AC         XOR     H               
6717: AC         XOR     H               
6718: AC         XOR     H               
6719: AC         XOR     H               
671A: AC         XOR     H               
671B: AC         XOR     H               
671C: 56         LD      D,(HL)          
671D: 73         LD      (HL),E          
671E: AE         XOR     (HL)            
671F: AE         XOR     (HL)            
6720: AE         XOR     (HL)            
6721: AE         XOR     (HL)            
6722: 00         NOP                     
6723: 9A         SBC     D               
6724: A0         AND     B               
6725: 13         INC     DE              
6726: AE         XOR     (HL)            
6727: AE         XOR     (HL)            
6728: AE         XOR     (HL)            
6729: AE         XOR     (HL)            
672A: AE         XOR     (HL)            
672B: 75         LD      (HL),L          
672C: AC         XOR     H               
672D: AC         XOR     H               
672E: AC         XOR     H               
672F: AC         XOR     H               
6730: AC         XOR     H               
6731: AC         XOR     H               
6732: AC         XOR     H               
6733: AC         XOR     H               
6734: AC         XOR     H               
6735: AC         XOR     H               
6736: 70         LD      (HL),B          
6737: 71         LD      (HL),C          
6738: AE         XOR     (HL)            
6739: AE         XOR     (HL)            
673A: 00         NOP                     
673B: 9A         SBC     D               
673C: 80         ADD     A,B             
673D: 13         INC     DE              
673E: AE         XOR     (HL)            
673F: AE         XOR     (HL)            
6740: AE         XOR     (HL)            
6741: AE         XOR     (HL)            
6742: 74         LD      (HL),H          
6743: 67         LD      H,A             
6744: AC         XOR     H               
6745: AC         XOR     H               
6746: AC         XOR     H               
6747: AC         XOR     H               
6748: AC         XOR     H               
6749: AC         XOR     H               
674A: AC         XOR     H               
674B: AC         XOR     H               
674C: AC         XOR     H               
674D: AC         XOR     H               
674E: AC         XOR     H               
674F: 57         LD      D,A             
6750: AE         XOR     (HL)            
6751: AE         XOR     (HL)            
6752: 00         NOP                     
6753: 9A         SBC     D               
6754: 60         LD      H,B             
6755: 13         INC     DE              
6756: 72         LD      (HL),D          
6757: AE         XOR     (HL)            
6758: 76         HALT                    
6759: 77         LD      (HL),A          
675A: AC         XOR     H               
675B: AC         XOR     H               
675C: AC         XOR     H               
675D: AC         XOR     H               
675E: AC         XOR     H               
675F: AC         XOR     H               
6760: AC         XOR     H               
6761: AC         XOR     H               
6762: AC         XOR     H               
6763: AC         XOR     H               
6764: AC         XOR     H               
6765: AC         XOR     H               
6766: AC         XOR     H               
6767: 7B         LD      A,E             
6768: AE         XOR     (HL)            
6769: AE         XOR     (HL)            
676A: 00         NOP                     
676B: 9A         SBC     D               
676C: 40         LD      B,B             
676D: 13         INC     DE              
676E: 56         LD      D,(HL)          
676F: 73         LD      (HL),E          
6770: 66         LD      H,(HL)          
6771: AC         XOR     H               
6772: AC         XOR     H               
6773: AC         XOR     H               
6774: AC         XOR     H               
6775: AC         XOR     H               
6776: AC         XOR     H               
6777: AC         XOR     H               
6778: AC         XOR     H               
6779: AC         XOR     H               
677A: AC         XOR     H               
677B: AC         XOR     H               
677C: AC         XOR     H               
677D: AC         XOR     H               
677E: 7A         LD      A,D             
677F: 4B         LD      C,E             
6780: AE         XOR     (HL)            
6781: AE         XOR     (HL)            
6782: 00         NOP                     
6783: 9A         SBC     D               
6784: 20 13      JR      NZ,$6799        
6786: AC         XOR     H               
6787: AC         XOR     H               
6788: AC         XOR     H               
6789: 7B         LD      A,E             
678A: 3D         DEC     A               
678B: 3F         CCF                     
678C: AC         XOR     H               
678D: AC         XOR     H               
678E: AC         XOR     H               
678F: AC         XOR     H               
6790: AC         XOR     H               
6791: AC         XOR     H               
6792: AC         XOR     H               
6793: AC         XOR     H               
6794: AC         XOR     H               
6795: AC         XOR     H               
6796: 72         LD      (HL),D          
6797: AE         XOR     (HL)            
6798: AE         XOR     (HL)            
6799: AE         XOR     (HL)            
679A: 00         NOP                     
679B: 9A         SBC     D               
679C: 00         NOP                     
679D: 13         INC     DE              
679E: AC         XOR     H               
679F: AC         XOR     H               
67A0: 7A         LD      A,D             
67A1: 4B         LD      C,E             
67A2: AE         XOR     (HL)            
67A3: 3E AC      LD      A,$AC           
67A5: AC         XOR     H               
67A6: AC         XOR     H               
67A7: AC         XOR     H               
67A8: AC         XOR     H               
67A9: AC         XOR     H               
67AA: AC         XOR     H               
67AB: AC         XOR     H               
67AC: AC         XOR     H               
67AD: AC         XOR     H               
67AE: 56         LD      D,(HL)          
67AF: 73         LD      (HL),E          
67B0: AE         XOR     (HL)            
67B1: AE         XOR     (HL)            
67B2: 00         NOP                     
67B3: 99         SBC     C               
67B4: E0 13      LDFF00  ($13),A         
67B6: AC         XOR     H               
67B7: AC         XOR     H               
67B8: 72         LD      (HL),D          
67B9: AE         XOR     (HL)            
67BA: AE         XOR     (HL)            
67BB: 75         LD      (HL),L          
67BC: AC         XOR     H               
67BD: AC         XOR     H               
67BE: FE FF      CP      $FF             
67C0: 05         DEC     B               
67C1: 0B         DEC     BC              
67C2: AC         XOR     H               
67C3: AC         XOR     H               
67C4: AC         XOR     H               
67C5: AC         XOR     H               
67C6: AC         XOR     H               
67C7: AC         XOR     H               
67C8: 70         LD      (HL),B          
67C9: 71         LD      (HL),C          
67CA: 00         NOP                     
67CB: 99         SBC     C               
67CC: C0         RET     NZ              
67CD: 13         INC     DE              
67CE: AC         XOR     H               
67CF: AC         XOR     H               
67D0: 56         LD      D,(HL)          
67D1: 73         LD      (HL),E          
67D2: 74         LD      (HL),H          
67D3: 67         LD      H,A             
67D4: AC         XOR     H               
67D5: AC         XOR     H               
67D6: F8 FA      LDHL    SP,$FA          
67D8: FC         ???                     
67D9: FD         ???                     
67DA: AC         XOR     H               
67DB: AC         XOR     H               
67DC: AC         XOR     H               
67DD: AC         XOR     H               
67DE: AC         XOR     H               
67DF: AC         XOR     H               
67E0: AC         XOR     H               
67E1: 57         LD      D,A             
67E2: 00         NOP                     
67E3: 99         SBC     C               
67E4: A0         AND     B               
67E5: 13         INC     DE              
67E6: AC         XOR     H               
67E7: AC         XOR     H               
67E8: AC         XOR     H               
67E9: AC         XOR     H               
67EA: AC         XOR     H               
67EB: AC         XOR     H               
67EC: AC         XOR     H               
67ED: AC         XOR     H               
67EE: A2         AND     D               
67EF: A3         AND     E               
67F0: BF         CP      A               
67F1: F0 AC      LD      A,($AC)         
67F3: AC         XOR     H               
67F4: AC         XOR     H               
67F5: AC         XOR     H               
67F6: AC         XOR     H               
67F7: AC         XOR     H               
67F8: AC         XOR     H               
67F9: AC         XOR     H               
67FA: 00         NOP                     
67FB: 99         SBC     C               
67FC: 80         ADD     A,B             
67FD: 13         INC     DE              
67FE: AC         XOR     H               
67FF: AC         XOR     H               
6800: AC         XOR     H               
6801: AC         XOR     H               
6802: AC         XOR     H               
6803: AC         XOR     H               
6804: AC         XOR     H               
6805: AC         XOR     H               
6806: 84         ADD     A,H             
6807: 85         ADD     A,L             
6808: 9D         SBC     L               
6809: 9F         SBC     A               
680A: AC         XOR     H               
680B: AC         XOR     H               
680C: AC         XOR     H               
680D: AC         XOR     H               
680E: AC         XOR     H               
680F: AC         XOR     H               
6810: AC         XOR     H               
6811: AC         XOR     H               
6812: 00         NOP                     
6813: 99         SBC     C               
6814: 60         LD      H,B             
6815: 13         INC     DE              
6816: AC         XOR     H               
6817: AC         XOR     H               
6818: AC         XOR     H               
6819: AC         XOR     H               
681A: AC         XOR     H               
681B: AC         XOR     H               
681C: AC         XOR     H               
681D: AC         XOR     H               
681E: AC         XOR     H               
681F: AC         XOR     H               
6820: AC         XOR     H               
6821: AC         XOR     H               
6822: AC         XOR     H               
6823: AC         XOR     H               
6824: AC         XOR     H               
6825: AC         XOR     H               
6826: AC         XOR     H               
6827: AC         XOR     H               
6828: AC         XOR     H               
6829: AC         XOR     H               
682A: 00         NOP                     
682B: 99         SBC     C               
682C: 40         LD      B,B             
682D: 13         INC     DE              
682E: AC         XOR     H               
682F: AC         XOR     H               
6830: AC         XOR     H               
6831: AC         XOR     H               
6832: AC         XOR     H               
6833: AC         XOR     H               
6834: AC         XOR     H               
6835: AC         XOR     H               
6836: AC         XOR     H               
6837: AC         XOR     H               
6838: AC         XOR     H               
6839: AC         XOR     H               
683A: AC         XOR     H               
683B: AC         XOR     H               
683C: AC         XOR     H               
683D: AC         XOR     H               
683E: AC         XOR     H               
683F: AC         XOR     H               
6840: AC         XOR     H               
6841: AC         XOR     H               
6842: 00         NOP                     
6843: 99         SBC     C               
6844: 20 13      JR      NZ,$6859        
6846: 3C         INC     A               
6847: AC         XOR     H               
6848: 78         LD      A,B             
6849: 79         LD      A,C             
684A: 3C         INC     A               
684B: AC         XOR     H               
684C: AC         XOR     H               
684D: AC         XOR     H               
684E: AC         XOR     H               
684F: AC         XOR     H               
6850: AC         XOR     H               
6851: AC         XOR     H               
6852: AC         XOR     H               
6853: AC         XOR     H               
6854: AC         XOR     H               
6855: 7B         LD      A,E             
6856: 3D         DEC     A               
6857: 3F         CCF                     
6858: AC         XOR     H               
6859: AC         XOR     H               
685A: 00         NOP                     
685B: 99         SBC     C               
685C: 00         NOP                     
685D: 13         INC     DE              
685E: 2C         INC     L               
685F: 2D         DEC     L               
6860: 45         LD      B,L             
6861: AE         XOR     (HL)            
6862: 2C         INC     L               
6863: 2D         DEC     L               
6864: AC         XOR     H               
6865: AC         XOR     H               
6866: AC         XOR     H               
6867: AC         XOR     H               
6868: AC         XOR     H               
6869: AC         XOR     H               
686A: AC         XOR     H               
686B: AC         XOR     H               
686C: 7A         LD      A,D             
686D: 4B         LD      C,E             
686E: AE         XOR     (HL)            
686F: 3E AC      LD      A,$AC           
6871: AC         XOR     H               
6872: 00         NOP                     
6873: 98         SBC     B               
6874: E0 13      LDFF00  ($13),A         
6876: AE         XOR     (HL)            
6877: AE         XOR     (HL)            
6878: AE         XOR     (HL)            
6879: AE         XOR     (HL)            
687A: AE         XOR     (HL)            
687B: 75         LD      (HL),L          
687C: AC         XOR     H               
687D: AC         XOR     H               
687E: AC         XOR     H               
687F: AC         XOR     H               
6880: AC         XOR     H               
6881: AC         XOR     H               
6882: 78         LD      A,B             
6883: 79         LD      A,C             
6884: AE         XOR     (HL)            
6885: AE         XOR     (HL)            
6886: AE         XOR     (HL)            
6887: AE         XOR     (HL)            
6888: 3C         INC     A               
6889: AC         XOR     H               
688A: 00         NOP                     
688B: 98         SBC     B               
688C: C0         RET     NZ              
688D: 13         INC     DE              
688E: AE         XOR     (HL)            
688F: AE         XOR     (HL)            
6890: AE         XOR     (HL)            
6891: AE         XOR     (HL)            
6892: 74         LD      (HL),H          
6893: 67         LD      H,A             
6894: AC         XOR     H               
6895: AC         XOR     H               
6896: AC         XOR     H               
6897: AC         XOR     H               
6898: AC         XOR     H               
6899: AC         XOR     H               
689A: 45         LD      B,L             
689B: AE         XOR     (HL)            
689C: AE         XOR     (HL)            
689D: AE         XOR     (HL)            
689E: AE         XOR     (HL)            
689F: AE         XOR     (HL)            
68A0: 2C         INC     L               
68A1: 2D         DEC     L               
68A2: 00         NOP                     
68A3: 02         LD      (BC),A          
68A4: 04         INC     B               
68A5: 06 08      LD      B,$08           
68A7: 0A         LD      A,(BC)          
68A8: 0C         INC     C               
68A9: 0E 10      LD      C,$10           
68AB: 12         LD      (DE),A          
68AC: 14         INC     D               
68AD: 16 18      LD      D,$18           
68AF: 1A         LD      A,(DE)          
68B0: 1C         INC     E               
68B1: 1E 20      LD      E,$20           
68B3: 22         LD      (HLI),A         
68B4: 24         INC     H               
68B5: 26 28      LD      H,$28           
68B7: 28 28      JR      Z,$68E1         
68B9: 28 28      JR      Z,$68E3         
68BB: 28 28      JR      Z,$68E5         
68BD: 28 28      JR      Z,$68E7         
68BF: 28 28      JR      Z,$68E9         
68C1: 28 28      JR      Z,$68EB         
68C3: 28 28      JR      Z,$68ED         
68C5: 28 28      JR      Z,$68EF         
68C7: 28 28      JR      Z,$68F1         
68C9: 28 28      JR      Z,$68F3         
68CB: 28 28      JR      Z,$68F5         
68CD: 28 28      JR      Z,$68F7         
68CF: 28 28      JR      Z,$68F9         
68D1: 28 28      JR      Z,$68FB         
68D3: 28 28      JR      Z,$68FD         
68D5: 28 27      JR      Z,$68FE         
68D7: 26 25      LD      H,$25           
68D9: 24         INC     H               
68DA: 23         INC     HL              
68DB: 22         LD      (HLI),A         
68DC: 21 20 1F   LD      HL,$1F20        
68DF: 1E 1D      LD      E,$1D           
68E1: 1C         INC     E               
68E2: 1B         DEC     DE              
68E3: 1A         LD      A,(DE)          
68E4: 19         ADD     HL,DE           
68E5: 18 17      JR      $68FE           
68E7: 16 15      LD      D,$15           
68E9: 14         INC     D               
68EA: 13         INC     DE              
68EB: 12         LD      (DE),A          
68EC: 11 10 0F   LD      DE,$0F10        
68EF: 0E 0D      LD      C,$0D           
68F1: 0C         INC     C               
68F2: 0B         DEC     BC              
68F3: 0A         LD      A,(BC)          
68F4: 09         ADD     HL,BC           
68F5: 08 07 06   LD      ($0607),SP      
68F8: 05         DEC     B               
68F9: 04         INC     B               
68FA: 04         INC     B               
68FB: 04         INC     B               
68FC: 04         INC     B               
68FD: 04         INC     B               
68FE: 04         INC     B               
68FF: 00         NOP                     
6900: 00         NOP                     
6901: 00         NOP                     
6902: 00         NOP                     
6903: 00         NOP                     
6904: 00         NOP                     
6905: 00         NOP                     
6906: 00         NOP                     
6907: 00         NOP                     
6908: 00         NOP                     
6909: 00         NOP                     
690A: 00         NOP                     
690B: 00         NOP                     
690C: 00         NOP                     
690D: 00         NOP                     
690E: 00         NOP                     
690F: 00         NOP                     
6910: 00         NOP                     
6911: 00         NOP                     
6912: 00         NOP                     
6913: 00         NOP                     
6914: 00         NOP                     
6915: 00         NOP                     
6916: 00         NOP                     
6917: 00         NOP                     
6918: 00         NOP                     
6919: 01 01 01   LD      BC,$0101        
691C: 01 01 01   LD      BC,$0101        
691F: 01 01 01   LD      BC,$0101        
6922: 01 02 02   LD      BC,$0202        
6925: 02         LD      (BC),A          
6926: 02         LD      (BC),A          
6927: 02         LD      (BC),A          
6928: 02         LD      (BC),A          
6929: 02         LD      (BC),A          
692A: 02         LD      (BC),A          
692B: 02         LD      (BC),A          
692C: 02         LD      (BC),A          
692D: 03         INC     BC              
692E: 03         INC     BC              
692F: 03         INC     BC              
6930: 03         INC     BC              
6931: 03         INC     BC              
6932: 03         INC     BC              
6933: 03         INC     BC              
6934: 03         INC     BC              
6935: 03         INC     BC              
6936: 03         INC     BC              
6937: 04         INC     B               
6938: 04         INC     B               
6939: 04         INC     B               
693A: 04         INC     B               
693B: 04         INC     B               
693C: 04         INC     B               
693D: 04         INC     B               
693E: 04         INC     B               
693F: 04         INC     B               
6940: 04         INC     B               
6941: 04         INC     B               
6942: 04         INC     B               
6943: 04         INC     B               
6944: 04         INC     B               
6945: 04         INC     B               
6946: 04         INC     B               
6947: 04         INC     B               
6948: 04         INC     B               
6949: 04         INC     B               
694A: 04         INC     B               
694B: 04         INC     B               
694C: 04         INC     B               
694D: 04         INC     B               
694E: 04         INC     B               
694F: 04         INC     B               
6950: 04         INC     B               
6951: 04         INC     B               
6952: 04         INC     B               
6953: 04         INC     B               
6954: 04         INC     B               
6955: 04         INC     B               
6956: 04         INC     B               
6957: 04         INC     B               
6958: 04         INC     B               
6959: 04         INC     B               
695A: 04         INC     B               
695B: 04         INC     B               
695C: 04         INC     B               
695D: 04         INC     B               
695E: 04         INC     B               
695F: 04         INC     B               
6960: 04         INC     B               
6961: 04         INC     B               
6962: 04         INC     B               
6963: 1E 1E      LD      E,$1E           
6965: 1E 1E      LD      E,$1E           
6967: 1F         RRA                     
6968: 1F         RRA                     
6969: 1F         RRA                     
696A: 1F         RRA                     
696B: 1A         LD      A,(DE)          
696C: 1A         LD      A,(DE)          
696D: 1A         LD      A,(DE)          
696E: 1A         LD      A,(DE)          
696F: 15         DEC     D               
6970: 15         DEC     D               
6971: 15         DEC     D               
6972: 15         DEC     D               
6973: 10 10      STOP    $10             
6975: 10 10      STOP    $10             
6977: 10 10      STOP    $10             
6979: 10 10      STOP    $10             
697B: 10 10      STOP    $10             
697D: 10 10      STOP    $10             
697F: 15         DEC     D               
6980: 15         DEC     D               
6981: 15         DEC     D               
6982: 15         DEC     D               
6983: 19         ADD     HL,DE           
6984: 19         ADD     HL,DE           
6985: 1A         LD      A,(DE)          
6986: 1A         LD      A,(DE)          
6987: 1E 1E      LD      E,$1E           
6989: 1E 1E      LD      E,$1E           
698B: FA 0D D0   LD      A,($D00D)       
698E: FE 0E      CP      $0E             
6990: 30 06      JR      NC,$6998        
6992: 11 60 99   LD      DE,$9960        
6995: CD 55 46   CALL    $4655           
6998: FA 0D D0   LD      A,($D00D)       
699B: 5F         LD      E,A             
699C: 16 00      LD      D,$00           
699E: 21 03 69   LD      HL,$6903        
69A1: 19         ADD     HL,DE           
69A2: 7E         LD      A,(HL)          
69A3: EA 0C D0   LD      ($D00C),A       
69A6: F0 E7      LD      A,($E7)         
69A8: E6 03      AND     $03             
69AA: 5F         LD      E,A             
69AB: FA 0C D0   LD      A,($D00C)       
69AE: 83         ADD     A,E             
69AF: 5F         LD      E,A             
69B0: 16 00      LD      D,$00           
69B2: 21 63 69   LD      HL,$6963        
69B5: 19         ADD     HL,DE           
69B6: 7E         LD      A,(HL)          
69B7: EA 97 DB   LD      ($DB97),A       
69BA: FA 0D D0   LD      A,($D00D)       
69BD: 5F         LD      E,A             
69BE: 16 00      LD      D,$00           
69C0: FE 59      CP      $59             
69C2: 20 13      JR      NZ,$69D7        
69C4: F0 97      LD      A,($97)         
69C6: FE 30      CP      $30             
69C8: 20 0D      JR      NZ,$69D7        
69CA: 3E FF      LD      A,$FF           
69CC: EA 08 D0   LD      ($D008),A       
69CF: 3E A8      LD      A,$A8           
69D1: EA 09 D0   LD      ($D009),A       
69D4: C3 2B 4A   JP      $4A2B           
69D7: 21 A3 68   LD      HL,$68A3        
69DA: 19         ADD     HL,DE           
69DB: 7E         LD      A,(HL)          
69DC: 2F         CPL                     
69DD: 3C         INC     A               
69DE: CB 27      SET     1,E             
69E0: EA 40 C2   LD      ($C240),A       
69E3: 01 00 00   LD      BC,$0000        
69E6: FA 00 C2   LD      A,($C200)       
69E9: F5         PUSH    AF              
69EA: CD C5 7B   CALL    $7BC5           
69ED: FA 00 C2   LD      A,($C200)       
69F0: E0 97      LDFF00  ($97),A         
69F2: E6 F8      AND     $F8             
69F4: 5F         LD      E,A             
69F5: F1         POP     AF              
69F6: E6 F8      AND     $F8             
69F8: BB         CP      E               
69F9: 28 5F      JR      Z,$6A5A         
69FB: FA 0D D0   LD      A,($D00D)       
69FE: FE 59      CP      $59             
6A00: 28 58      JR      Z,$6A5A         
6A02: 3C         INC     A               
6A03: EA 0D D0   LD      ($D00D),A       
6A06: FE 44      CP      $44             
6A08: 20 22      JR      NZ,$6A2C        
6A0A: 3E E3      LD      A,$E3           
6A0C: EA 99 DB   LD      ($DB99),A       
6A0F: 3E E8      LD      A,$E8           
6A11: CD 01 3C   CALL    $3C01           
6A14: 21 00 C2   LD      HL,$C200        
6A17: 19         ADD     HL,DE           
6A18: 36 50      LD      (HL),$50        
6A1A: 21 10 C2   LD      HL,$C210        
6A1D: 19         ADD     HL,DE           
6A1E: 36 80      LD      (HL),$80        
6A20: 21 B0 C2   LD      HL,$C2B0        
6A23: 19         ADD     HL,DE           
6A24: 36 0B      LD      (HL),$0B        
6A26: 21 E0 C2   LD      HL,$C2E0        
6A29: 19         ADD     HL,DE           
6A2A: 36 A8      LD      (HL),$A8        
6A2C: FA 0D D0   LD      A,($D00D)       
6A2F: 5F         LD      E,A             
6A30: 16 00      LD      D,$00           
6A32: CB 23      SET     1,E             
6A34: CB 12      SET     1,E             
6A36: CB 23      SET     1,E             
6A38: CB 12      SET     1,E             
6A3A: CB 23      SET     1,E             
6A3C: CB 12      SET     1,E             
6A3E: 7B         LD      A,E             
6A3F: 6A         LD      L,D             
6A40: CB 23      SET     1,E             
6A42: CB 12      SET     1,E             
6A44: 83         ADD     A,E             
6A45: 5F         LD      E,A             
6A46: 7A         LD      A,D             
6A47: CE 00      ADC     $00             
6A49: 85         ADD     A,L             
6A4A: 57         LD      D,A             
6A4B: 21 33 60   LD      HL,$6033        
6A4E: 19         ADD     HL,DE           
6A4F: 11 01 D6   LD      DE,$D601        
6A52: 0E 18      LD      C,$18           
6A54: 2A         LD      A,(HLI)         
6A55: 12         LD      (DE),A          
6A56: 13         INC     DE              
6A57: 0D         DEC     C               
6A58: 20 FA      JR      NZ,$6A54        
6A5A: C9         RET                     
6A5B: FA 09 D0   LD      A,($D009)       
6A5E: A7         AND     A               
6A5F: 20 07      JR      NZ,$6A68        
6A61: AF         XOR     A               
6A62: EA 97 DB   LD      ($DB97),A       
6A65: C3 C1 5C   JP      $5CC1           
6A68: F0 E7      LD      A,($E7)         
6A6A: E6 03      AND     $03             
6A6C: 5F         LD      E,A             
6A6D: FA 0C D0   LD      A,($D00C)       
6A70: 83         ADD     A,E             
6A71: 5F         LD      E,A             
6A72: 16 00      LD      D,$00           
6A74: 21 63 69   LD      HL,$6963        
6A77: 19         ADD     HL,DE           
6A78: 7E         LD      A,(HL)          
6A79: EA 97 DB   LD      ($DB97),A       
6A7C: FA 08 D0   LD      A,($D008)       
6A7F: A7         AND     A               
6A80: 20 3C      JR      NZ,$6ABE        
6A82: FA 0B D0   LD      A,($D00B)       
6A85: 3C         INC     A               
6A86: EA 0B D0   LD      ($D00B),A       
6A89: E6 07      AND     $07             
6A8B: 20 31      JR      NZ,$6ABE        
6A8D: FA 0C D0   LD      A,($D00C)       
6A90: FE 24      CP      $24             
6A92: 28 2A      JR      Z,$6ABE         
6A94: 3C         INC     A               
6A95: EA 0C D0   LD      ($D00C),A       
6A98: FE 05      CP      $05             
6A9A: 20 22      JR      NZ,$6ABE        
6A9C: 3E 1E      LD      A,$1E           
6A9E: EA 98 DB   LD      ($DB98),A       
6AA1: 3E E8      LD      A,$E8           
6AA3: CD 01 3C   CALL    $3C01           
6AA6: 21 00 C2   LD      HL,$C200        
6AA9: 19         ADD     HL,DE           
6AAA: 36 62      LD      (HL),$62        
6AAC: 21 10 C2   LD      HL,$C210        
6AAF: 19         ADD     HL,DE           
6AB0: 36 5A      LD      (HL),$5A        
6AB2: 21 B0 C2   LD      HL,$C2B0        
6AB5: 19         ADD     HL,DE           
6AB6: 36 0C      LD      (HL),$0C        
6AB8: 21 E0 C2   LD      HL,$C2E0        
6ABB: 19         ADD     HL,DE           
6ABC: 36 60      LD      (HL),$60        
6ABE: C9         RET                     
6ABF: CD 13 0B   CALL    $0B13           
6AC2: FA 0E D0   LD      A,($D00E)       
6AC5: C7         RST     0X00            
6AC6: D4 6A DC   CALL    NC,$DC6A        
6AC9: 6A         LD      L,D             
6ACA: 0D         DEC     C               
6ACB: 6B         LD      L,E             
6ACC: 3F         CCF                     
6ACD: 6B         LD      L,E             
6ACE: 70         LD      (HL),B          
6ACF: 6B         LD      L,E             
6AD0: 8F         ADC     A,A             
6AD1: 6B         LD      L,E             
6AD2: D4 6B 3E   CALL    NC,$3E6B        
6AD5: 1A         LD      A,(DE)          
6AD6: EA FE D6   LD      ($D6FE),A       
6AD9: C3 2B 4A   JP      $4A2B           
6ADC: 3E 1B      LD      A,$1B           
6ADE: EA FF D6   LD      ($D6FF),A       
6AE1: CD EB 4A   CALL    $4AEB           
6AE4: 3E 1E      LD      A,$1E           
6AE6: EA 97 DB   LD      ($DB97),A       
6AE9: 3E 6E      LD      A,$6E           
6AEB: EA 98 DB   LD      ($DB98),A       
6AEE: 3E E8      LD      A,$E8           
6AF0: CD 01 3C   CALL    $3C01           
6AF3: 21 00 C2   LD      HL,$C200        
6AF6: 19         ADD     HL,DE           
6AF7: 36 38      LD      (HL),$38        
6AF9: 21 10 C2   LD      HL,$C210        
6AFC: 19         ADD     HL,DE           
6AFD: 36 50      LD      (HL),$50        
6AFF: 21 B0 C2   LD      HL,$C2B0        
6B02: 19         ADD     HL,DE           
6B03: 36 0D      LD      (HL),$0D        
6B05: 3E 20      LD      A,$20           
6B07: EA 06 D0   LD      ($D006),A       
6B0A: C3 2B 4A   JP      $4A2B           
6B0D: FA 06 D0   LD      A,($D006)       
6B10: A7         AND     A               
6B11: 20 03      JR      NZ,$6B16        
6B13: CD 2B 4A   CALL    $4A2B           
6B16: F0 E7      LD      A,($E7)         
6B18: E6 03      AND     $03             
6B1A: 20 0C      JR      NZ,$6B28        
6B1C: FA 0F D0   LD      A,($D00F)       
6B1F: 3C         INC     A               
6B20: FE 31      CP      $31             
6B22: 20 01      JR      NZ,$6B25        
6B24: AF         XOR     A               
6B25: EA 0F D0   LD      ($D00F),A       
6B28: FA 0F D0   LD      A,($D00F)       
6B2B: 5F         LD      E,A             
6B2C: 50         LD      D,B             
6B2D: 21 67 72   LD      HL,$7267        
6B30: 19         ADD     HL,DE           
6B31: 7E         LD      A,(HL)          
6B32: CB 2F      SET     1,E             
6B34: E0 97      LDFF00  ($97),A         
6B36: C9         RET                     
6B37: 6E         LD      L,(HL)          
6B38: 6E         LD      L,(HL)          
6B39: 6E         LD      L,(HL)          
6B3A: 6E         LD      L,(HL)          
6B3B: 1E 1E      LD      E,$1E           
6B3D: 1E 1E      LD      E,$1E           
6B3F: CD 16 6B   CALL    $6B16           
6B42: F0 E7      LD      A,($E7)         
6B44: E6 07      AND     $07             
6B46: 20 13      JR      NZ,$6B5B        
6B48: FA 0A D0   LD      A,($D00A)       
6B4B: 3C         INC     A               
6B4C: EA 0A D0   LD      ($D00A),A       
6B4F: FE 04      CP      $04             
6B51: 20 08      JR      NZ,$6B5B        
6B53: 3E FF      LD      A,$FF           
6B55: EA 06 D0   LD      ($D006),A       
6B58: C3 2B 4A   JP      $4A2B           
6B5B: F0 E7      LD      A,($E7)         
6B5D: E6 03      AND     $03             
6B5F: 5F         LD      E,A             
6B60: FA 0A D0   LD      A,($D00A)       
6B63: 83         ADD     A,E             
6B64: 5F         LD      E,A             
6B65: 16 00      LD      D,$00           
6B67: 21 37 6B   LD      HL,$6B37        
6B6A: 19         ADD     HL,DE           
6B6B: 7E         LD      A,(HL)          
6B6C: EA 98 DB   LD      ($DB98),A       
6B6F: C9         RET                     
6B70: CD 16 6B   CALL    $6B16           
6B73: FA 06 D0   LD      A,($D006)       
6B76: A7         AND     A               
6B77: 20 09      JR      NZ,$6B82        
6B79: 3E E0      LD      A,$E0           
6B7B: EA 06 D0   LD      ($D006),A       
6B7E: C3 2B 4A   JP      $4A2B           
6B81: C9         RET                     
6B82: FE 44      CP      $44             
6B84: 28 04      JR      Z,$6B8A         
6B86: FE 50      CP      $50             
6B88: 20 04      JR      NZ,$6B8E        
6B8A: 21 03 D0   LD      HL,$D003        
6B8D: 34         INC     (HL)            
6B8E: C9         RET                     
6B8F: CD 16 6B   CALL    $6B16           
6B92: 21 06 D0   LD      HL,$D006        
6B95: F0 E7      LD      A,($E7)         
6B97: E6 07      AND     $07             
6B99: B6         OR      (HL)            
6B9A: 20 13      JR      NZ,$6BAF        
6B9C: FA 02 D0   LD      A,($D002)       
6B9F: 3C         INC     A               
6BA0: EA 02 D0   LD      ($D002),A       
6BA3: FE 0C      CP      $0C             
6BA5: 20 08      JR      NZ,$6BAF        
6BA7: 3E 40      LD      A,$40           
6BA9: EA 06 D0   LD      ($D006),A       
6BAC: CD 2B 4A   CALL    $4A2B           
6BAF: F0 E7      LD      A,($E7)         
6BB1: E6 03      AND     $03             
6BB3: 5F         LD      E,A             
6BB4: FA 02 D0   LD      A,($D002)       
6BB7: 83         ADD     A,E             
6BB8: 5F         LD      E,A             
6BB9: 16 00      LD      D,$00           
6BBB: 21 53 5C   LD      HL,$5C53        
6BBE: 19         ADD     HL,DE           
6BBF: 7E         LD      A,(HL)          
6BC0: EA 97 DB   LD      ($DB97),A       
6BC3: 21 53 5C   LD      HL,$5C53        
6BC6: 19         ADD     HL,DE           
6BC7: 7E         LD      A,(HL)          
6BC8: EA 98 DB   LD      ($DB98),A       
6BCB: 21 63 5C   LD      HL,$5C63        
6BCE: 19         ADD     HL,DE           
6BCF: 7E         LD      A,(HL)          
6BD0: EA 99 DB   LD      ($DB99),A       
6BD3: C9         RET                     
6BD4: FA 06 D0   LD      A,($D006)       
6BD7: A7         AND     A               
6BD8: 20 03      JR      NZ,$6BDD        
6BDA: C3 C1 5C   JP      $5CC1           
6BDD: C9         RET                     
6BDE: 11 A0 99   LD      DE,$99A0        
6BE1: CD 55 46   CALL    $4655           
6BE4: CD FD 42   CALL    $42FD           
6BE7: CD 13 0B   CALL    $0B13           
6BEA: FA 0E D0   LD      A,($D00E)       
6BED: C7         RST     0X00            
6BEE: FA 6B 07   LD      A,($076B)       
6BF1: 6C         LD      L,H             
6BF2: 4C         LD      C,H             
6BF3: 6C         LD      L,H             
6BF4: 80         ADD     A,B             
6BF5: 6C         LD      L,H             
6BF6: C0         RET     NZ              
6BF7: 6C         LD      L,H             
6BF8: C1         POP     BC              
6BF9: 6C         LD      L,H             
6BFA: 3E 1B      LD      A,$1B           
6BFC: EA FE D6   LD      ($D6FE),A       
6BFF: 21 FD D6   LD      HL,$D6FD        
6C02: CB 96      SET     1,E             
6C04: C3 2B 4A   JP      $4A2B           
6C07: 3E 1C      LD      A,$1C           
6C09: EA FF D6   LD      ($D6FF),A       
6C0C: CD EB 4A   CALL    $4AEB           
6C0F: 3E E8      LD      A,$E8           
6C11: CD 01 3C   CALL    $3C01           
6C14: 21 00 C2   LD      HL,$C200        
6C17: 19         ADD     HL,DE           
6C18: 36 50      LD      (HL),$50        
6C1A: 21 10 C2   LD      HL,$C210        
6C1D: 19         ADD     HL,DE           
6C1E: 36 78      LD      (HL),$78        
6C20: 21 B0 C2   LD      HL,$C2B0        
6C23: 19         ADD     HL,DE           
6C24: 36 0E      LD      (HL),$0E        
6C26: AF         XOR     A               
6C27: EA 12 D0   LD      ($D012),A       
6C2A: 3D         DEC     A               
6C2B: EA 10 D0   LD      ($D010),A       
6C2E: 3E B0      LD      A,$B0           
6C30: EA 09 D0   LD      ($D009),A       
6C33: AF         XOR     A               
6C34: E0 E7      LDFF00  ($E7),A         
6C36: EA 99 DB   LD      ($DB99),A       
6C39: C3 2B 4A   JP      $4A2B           
6C3C: 00         NOP                     
6C3D: 00         NOP                     
6C3E: 00         NOP                     
6C3F: 00         NOP                     
6C40: 04         INC     B               
6C41: 04         INC     B               
6C42: 04         INC     B               
6C43: 04         INC     B               
6C44: 19         ADD     HL,DE           
6C45: 19         ADD     HL,DE           
6C46: 19         ADD     HL,DE           
6C47: 19         ADD     HL,DE           
6C48: 1E 1E      LD      E,$1E           
6C4A: 1E 1E      LD      E,$1E           
6C4C: F0 E7      LD      A,($E7)         
6C4E: E6 07      AND     $07             
6C50: 20 16      JR      NZ,$6C68        
6C52: FA 02 D0   LD      A,($D002)       
6C55: 3C         INC     A               
6C56: EA 02 D0   LD      ($D002),A       
6C59: FE 0C      CP      $0C             
6C5B: 20 0B      JR      NZ,$6C68        
6C5D: 3E FF      LD      A,$FF           
6C5F: EA 13 D0   LD      ($D013),A       
6C62: AF         XOR     A               
6C63: E0 E7      LDFF00  ($E7),A         
6C65: CD 2B 4A   CALL    $4A2B           
6C68: F0 E7      LD      A,($E7)         
6C6A: E6 03      AND     $03             
6C6C: 5F         LD      E,A             
6C6D: FA 02 D0   LD      A,($D002)       
6C70: 83         ADD     A,E             
6C71: 5F         LD      E,A             
6C72: 16 00      LD      D,$00           
6C74: 21 3C 6C   LD      HL,$6C3C        
6C77: 19         ADD     HL,DE           
6C78: 7E         LD      A,(HL)          
6C79: EA 97 DB   LD      ($DB97),A       
6C7C: EA 98 DB   LD      ($DB98),A       
6C7F: C9         RET                     
6C80: FA 13 D0   LD      A,($D013)       
6C83: A7         AND     A               
6C84: 20 39      JR      NZ,$6CBF        
6C86: F0 E7      LD      A,($E7)         
6C88: E6 07      AND     $07             
6C8A: 20 33      JR      NZ,$6CBF        
6C8C: 21 97 FF   LD      HL,$FF97        
6C8F: 35         DEC     (HL)            
6C90: 7E         LD      A,(HL)          
6C91: FE 70      CP      $70             
6C93: 20 03      JR      NZ,$6C98        
6C95: C3 2B 4A   JP      $4A2B           
6C98: FE A0      CP      $A0             
6C9A: 20 08      JR      NZ,$6CA4        
6C9C: 21 8F C2   LD      HL,$C28F        
6C9F: 36 00      LD      (HL),$00        
6CA1: C3 E6 6C   JP      $6CE6           
6CA4: FE C0      CP      $C0             
6CA6: 20 17      JR      NZ,$6CBF        
6CA8: 3E E8      LD      A,$E8           
6CAA: CD 01 3C   CALL    $3C01           
6CAD: 21 00 C2   LD      HL,$C200        
6CB0: 19         ADD     HL,DE           
6CB1: 36 18      LD      (HL),$18        
6CB3: 21 10 C2   LD      HL,$C210        
6CB6: 19         ADD     HL,DE           
6CB7: 36 B0      LD      (HL),$B0        
6CB9: 21 B0 C2   LD      HL,$C2B0        
6CBC: 19         ADD     HL,DE           
6CBD: 36 0F      LD      (HL),$0F        
6CBF: C9         RET                     
6CC0: C9         RET                     
6CC1: C9         RET                     
6CC2: 99         SBC     C               
6CC3: C1         POP     BC              
6CC4: 05         DEC     B               
6CC5: 58         LD      E,B             
6CC6: 59         LD      E,C             
6CC7: 5A         LD      E,D             
6CC8: 5B         LD      E,E             
6CC9: 5C         LD      E,H             
6CCA: 5D         LD      E,L             
6CCB: 99         SBC     C               
6CCC: E1         POP     HL              
6CCD: 05         DEC     B               
6CCE: 68         LD      L,B             
6CCF: 69         LD      L,C             
6CD0: 6A         LD      L,D             
6CD1: 6B         LD      L,E             
6CD2: 6C         LD      L,H             
6CD3: 6D         LD      L,L             
6CD4: 99         SBC     C               
6CD5: F1         POP     AF              
6CD6: 02         LD      (BC),A          
6CD7: 58         LD      E,B             
6CD8: 59         LD      E,C             
6CD9: 5A         LD      E,D             
6CDA: 9A         SBC     D               
6CDB: 11 02 68   LD      DE,$6802        
6CDE: 69         LD      L,C             
6CDF: 6A         LD      L,D             
6CE0: 9A         SBC     D               
6CE1: 20 01      JR      NZ,$6CE4        
6CE3: 5C         LD      E,H             
6CE4: 5D         LD      E,L             
6CE5: 00         NOP                     
6CE6: 21 C2 6C   LD      HL,$6CC2        
6CE9: 11 01 D6   LD      DE,$D601        
6CEC: 0E 24      LD      C,$24           
6CEE: 2A         LD      A,(HLI)         
6CEF: 12         LD      (DE),A          
6CF0: 13         INC     DE              
6CF1: 0D         DEC     C               
6CF2: 20 FA      JR      NZ,$6CEE        
6CF4: C9         RET                     
6CF5: 08 00 5C   LD      ($5C00),SP      
6CF8: 00         NOP                     
6CF9: 10 00      STOP    $00             
6CFB: 5D         LD      E,L             
6CFC: 00         NOP                     
6CFD: 00         NOP                     
6CFE: 08 C0 00   LD      ($00C0),SP      
6D01: 08 08 C1   LD      ($C108),SP      
6D04: 00         NOP                     
6D05: 00         NOP                     
6D06: 10 CE      STOP    $CE             
6D08: 00         NOP                     
6D09: 08 10 CF   LD      ($CF10),SP      
6D0C: 00         NOP                     
6D0D: 00         NOP                     
6D0E: 18 DE      JR      $6CEE           
6D10: 00         NOP                     
6D11: 08 18 DF   LD      ($DF18),SP      
6D14: 00         NOP                     
6D15: 00         NOP                     
6D16: 20 EA      JR      NZ,$6D02        
6D18: 00         NOP                     
6D19: 08 20 EB   LD      ($EB20),SP      
6D1C: 00         NOP                     
6D1D: 08 00 5E   LD      ($5E00),SP      
6D20: 00         NOP                     
6D21: 10 00      STOP    $00             
6D23: 5F         LD      E,A             
6D24: 00         NOP                     
6D25: 00         NOP                     
6D26: 08 C0 00   LD      ($00C0),SP      
6D29: 08 08 C1   LD      ($C108),SP      
6D2C: 00         NOP                     
6D2D: 00         NOP                     
6D2E: 10 CE      STOP    $CE             
6D30: 00         NOP                     
6D31: 08 10 CF   LD      ($CF10),SP      
6D34: 00         NOP                     
6D35: 00         NOP                     
6D36: 18 DE      JR      $6D16           
6D38: 00         NOP                     
6D39: 08 18 DF   LD      ($DF18),SP      
6D3C: 00         NOP                     
6D3D: 00         NOP                     
6D3E: 20 EA      JR      NZ,$6D2A        
6D40: 00         NOP                     
6D41: 08 20 EB   LD      ($EB20),SP      
6D44: 00         NOP                     
6D45: 08 00 EC   LD      ($EC00),SP      
6D48: 00         NOP                     
6D49: 10 00      STOP    $00             
6D4B: ED         ???                     
6D4C: 00         NOP                     
6D4D: 00         NOP                     
6D4E: 08 D0 00   LD      ($00D0),SP      
6D51: 08 08 D1   LD      ($D108),SP      
6D54: 00         NOP                     
6D55: 00         NOP                     
6D56: 10 CE      STOP    $CE             
6D58: 00         NOP                     
6D59: 08 10 CF   LD      ($CF10),SP      
6D5C: 00         NOP                     
6D5D: 00         NOP                     
6D5E: 18 DE      JR      $6D3E           
6D60: 00         NOP                     
6D61: 08 18 DF   LD      ($DF18),SP      
6D64: 00         NOP                     
6D65: 00         NOP                     
6D66: 20 EA      JR      NZ,$6D52        
6D68: 00         NOP                     
6D69: 08 20 EB   LD      ($EB20),SP      
6D6C: 00         NOP                     
6D6D: 08 00 EE   LD      ($EE00),SP      
6D70: 00         NOP                     
6D71: 10 00      STOP    $00             
6D73: EF         RST     0X28            
6D74: 00         NOP                     
6D75: 00         NOP                     
6D76: 08 D0 00   LD      ($00D0),SP      
6D79: 08 08 D1   LD      ($D108),SP      
6D7C: 00         NOP                     
6D7D: 00         NOP                     
6D7E: 10 CE      STOP    $CE             
6D80: 00         NOP                     
6D81: 08 10 CF   LD      ($CF10),SP      
6D84: 00         NOP                     
6D85: 00         NOP                     
6D86: 18 DE      JR      $6D66           
6D88: 00         NOP                     
6D89: 08 18 DF   LD      ($DF18),SP      
6D8C: 00         NOP                     
6D8D: 00         NOP                     
6D8E: 20 EA      JR      NZ,$6D7A        
6D90: 00         NOP                     
6D91: 08 20 EB   LD      ($EB20),SP      
6D94: 00         NOP                     
6D95: 3E 3C      LD      A,$3C           
6D97: EA C0 C3   LD      ($C3C0),A       
6D9A: F0 97      LD      A,($97)         
6D9C: 5F         LD      E,A             
6D9D: F0 EC      LD      A,($EC)         
6D9F: 93         SUB     E               
6DA0: E0 EC      LDFF00  ($EC),A         
6DA2: F0 E7      LD      A,($E7)         
6DA4: 1F         RRA                     
6DA5: 1F         RRA                     
6DA6: 1F         RRA                     
6DA7: 1F         RRA                     
6DA8: 1F         RRA                     
6DA9: E6 03      AND     $03             
6DAB: 17         RLA                     
6DAC: 17         RLA                     
6DAD: 17         RLA                     
6DAE: E6 F8      AND     $F8             
6DB0: 5F         LD      E,A             
6DB1: 17         RLA                     
6DB2: 17         RLA                     
6DB3: E6 E0      AND     $E0             
6DB5: 83         ADD     A,E             
6DB6: 5F         LD      E,A             
6DB7: 50         LD      D,B             
6DB8: 21 F5 6C   LD      HL,$6CF5        
6DBB: 19         ADD     HL,DE           
6DBC: 0E 0A      LD      C,$0A           
6DBE: CD 20 3D   CALL    $3D20           
6DC1: 3E 0A      LD      A,$0A           
6DC3: CD D0 3D   CALL    $3DD0           
6DC6: F0 E7      LD      A,($E7)         
6DC8: E6 01      AND     $01             
6DCA: 20 1A      JR      NZ,$6DE6        
6DCC: 21 40 C2   LD      HL,$C240        
6DCF: 09         ADD     HL,BC           
6DD0: 36 04      LD      (HL),$04        
6DD2: 21 50 C2   LD      HL,$C250        
6DD5: 09         ADD     HL,BC           
6DD6: 36 FF      LD      (HL),$FF        
6DD8: CD B8 7B   CALL    $7BB8           
6DDB: F0 EE      LD      A,($EE)         
6DDD: FE A8      CP      $A8             
6DDF: D8         RET     C               
6DE0: CD 2B 4A   CALL    $4A2B           
6DE3: C3 61 7A   JP      $7A61           
6DE6: C9         RET                     
6DE7: 00         NOP                     
6DE8: 00         NOP                     
6DE9: 00         NOP                     
6DEA: 00         NOP                     
6DEB: 08 00 01   LD      ($0100),SP      
6DEE: 00         NOP                     
6DEF: 00         NOP                     
6DF0: 08 02 00   LD      ($0002),SP      
6DF3: 08 08 03   LD      ($0308),SP      
6DF6: 00         NOP                     
6DF7: 00         NOP                     
6DF8: FA 10 00   LD      A,($0010)       
6DFB: 08 FA 11   LD      ($11FA),SP      
6DFE: 00         NOP                     
6DFF: 00         NOP                     
6E00: 0E 10      LD      C,$10           
6E02: 20 08      JR      NZ,$6E0C        
6E04: 0E 11      LD      C,$11           
6E06: 20 00      JR      NZ,$6E08        
6E08: 00         NOP                     
6E09: 00         NOP                     
6E0A: 00         NOP                     
6E0B: 08 00 01   LD      ($0100),SP      
6E0E: 00         NOP                     
6E0F: 00         NOP                     
6E10: 08 02 00   LD      ($0002),SP      
6E13: 08 08 03   LD      ($0308),SP      
6E16: 00         NOP                     
6E17: 08 FA 10   LD      ($10FA),SP      
6E1A: 40         LD      B,B             
6E1B: 00         NOP                     
6E1C: FA 11 40   LD      A,($4011)       
6E1F: 08 0E 10   LD      ($100E),SP      
6E22: 60         LD      H,B             
6E23: 00         NOP                     
6E24: 0E 11      LD      C,$11           
6E26: 60         LD      H,B             
6E27: 00         NOP                     
6E28: 08 00 20   LD      ($2000),SP      
6E2B: 08 08 01   LD      ($0108),SP      
6E2E: 20 00      JR      NZ,$6E30        
6E30: 00         NOP                     
6E31: 02         LD      (BC),A          
6E32: 20 08      JR      NZ,$6E3C        
6E34: 00         NOP                     
6E35: 03         INC     BC              
6E36: 20 00      JR      NZ,$6E38        
6E38: FA 10 00   LD      A,($0010)       
6E3B: 08 FA 11   LD      ($11FA),SP      
6E3E: 00         NOP                     
6E3F: 00         NOP                     
6E40: 0E 10      LD      C,$10           
6E42: 20 08      JR      NZ,$6E4C        
6E44: 0E 11      LD      C,$11           
6E46: 20 00      JR      NZ,$6E48        
6E48: 08 00 20   LD      ($2000),SP      
6E4B: 08 08 01   LD      ($0108),SP      
6E4E: 20 00      JR      NZ,$6E50        
6E50: 00         NOP                     
6E51: 02         LD      (BC),A          
6E52: 20 08      JR      NZ,$6E5C        
6E54: 00         NOP                     
6E55: 03         INC     BC              
6E56: 20 08      JR      NZ,$6E60        
6E58: FA 10 40   LD      A,($4010)       
6E5B: 00         NOP                     
6E5C: FA 11 40   LD      A,($4011)       
6E5F: 08 0E 10   LD      ($100E),SP      
6E62: 60         LD      H,B             
6E63: 00         NOP                     
6E64: 0E 11      LD      C,$11           
6E66: 60         LD      H,B             
6E67: 21 57 DB   LD      HL,$DB57        
6E6A: 2A         LD      A,(HLI)         
6E6B: B6         OR      (HL)            
6E6C: 20 28      JR      NZ,$6E96        
6E6E: 3E 1C      LD      A,$1C           
6E70: EA 98 DB   LD      ($DB98),A       
6E73: 3E 3C      LD      A,$3C           
6E75: EA C0 C3   LD      ($C3C0),A       
6E78: F0 E7      LD      A,($E7)         
6E7A: 1F         RRA                     
6E7B: 1F         RRA                     
6E7C: 1F         RRA                     
6E7D: E6 03      AND     $03             
6E7F: 17         RLA                     
6E80: 17         RLA                     
6E81: 17         RLA                     
6E82: 17         RLA                     
6E83: 17         RLA                     
6E84: E6 E0      AND     $E0             
6E86: 5F         LD      E,A             
6E87: 50         LD      D,B             
6E88: 21 E7 6D   LD      HL,$6DE7        
6E8B: 19         ADD     HL,DE           
6E8C: 0E 08      LD      C,$08           
6E8E: CD 20 3D   CALL    $3D20           
6E91: 3E 08      LD      A,$08           
6E93: CD D0 3D   CALL    $3DD0           
6E96: CD B8 7B   CALL    $7BB8           
6E99: F0 E7      LD      A,($E7)         
6E9B: E6 0F      AND     $0F             
6E9D: 20 0A      JR      NZ,$6EA9        
6E9F: 21 50 C2   LD      HL,$C250        
6EA2: 09         ADD     HL,BC           
6EA3: 7E         LD      A,(HL)          
6EA4: FE FC      CP      $FC             
6EA6: 28 01      JR      Z,$6EA9         
6EA8: 35         DEC     (HL)            
6EA9: F0 EE      LD      A,($EE)         
6EAB: FE A8      CP      $A8             
6EAD: CA 61 7A   JP      Z,$7A61         
6EB0: 21 D0 C3   LD      HL,$C3D0        
6EB3: 09         ADD     HL,BC           
6EB4: 7E         LD      A,(HL)          
6EB5: 3C         INC     A               
6EB6: 77         LD      (HL),A          
6EB7: E6 7F      AND     $7F             
6EB9: 20 04      JR      NZ,$6EBF        
6EBB: 3E 21      LD      A,$21           
6EBD: E0 F2      LDFF00  ($F2),A         
6EBF: C9         RET                     
6EC0: 00         NOP                     
6EC1: 00         NOP                     
6EC2: 4C         LD      C,H             
6EC3: 00         NOP                     
6EC4: 08 00 4D   LD      ($4D00),SP      
6EC7: 00         NOP                     
6EC8: 00         NOP                     
6EC9: 08 4E 00   LD      ($004E),SP      
6ECC: 08 08 4F   LD      ($4F08),SP      
6ECF: 00         NOP                     
6ED0: 10 F8      STOP    $F8             
6ED2: 60         LD      H,B             
6ED3: 00         NOP                     
6ED4: 18 F8      JR      $6ECE           
6ED6: 61         LD      H,C             
6ED7: 00         NOP                     
6ED8: 10 00      STOP    $00             
6EDA: 62         LD      H,D             
6EDB: 00         NOP                     
6EDC: 18 00      JR      $6EDE           
6EDE: 63         LD      H,E             
6EDF: 00         NOP                     
6EE0: 10 08      STOP    $08             
6EE2: 64         LD      H,H             
6EE3: 00         NOP                     
6EE4: 18 08      JR      $6EEE           
6EE6: 65         LD      H,L             
6EE7: 00         NOP                     
6EE8: 10 10      STOP    $10             
6EEA: 66         LD      H,(HL)          
6EEB: 00         NOP                     
6EEC: 18 10      JR      $6EFE           
6EEE: 67         LD      H,A             
6EEF: 00         NOP                     
6EF0: 00         NOP                     
6EF1: 00         NOP                     
6EF2: 4C         LD      C,H             
6EF3: 00         NOP                     
6EF4: 08 00 4D   LD      ($4D00),SP      
6EF7: 00         NOP                     
6EF8: 00         NOP                     
6EF9: 08 4E 00   LD      ($004E),SP      
6EFC: 08 08 4F   LD      ($4F08),SP      
6EFF: 00         NOP                     
6F00: 10 F8      STOP    $F8             
6F02: 68         LD      L,B             
6F03: 00         NOP                     
6F04: 18 F8      JR      $6EFE           
6F06: 69         LD      L,C             
6F07: 00         NOP                     
6F08: 10 00      STOP    $00             
6F0A: 6A         LD      L,D             
6F0B: 00         NOP                     
6F0C: 18 00      JR      $6F0E           
6F0E: 6B         LD      L,E             
6F0F: 00         NOP                     
6F10: 10 08      STOP    $08             
6F12: 6C         LD      L,H             
6F13: 00         NOP                     
6F14: 18 08      JR      $6F1E           
6F16: 6D         LD      L,L             
6F17: 00         NOP                     
6F18: 10 10      STOP    $10             
6F1A: 6E         LD      L,(HL)          
6F1B: 00         NOP                     
6F1C: 18 10      JR      $6F2E           
6F1E: 6F         LD      L,A             
6F1F: 00         NOP                     
6F20: 00         NOP                     
6F21: 00         NOP                     
6F22: 4C         LD      C,H             
6F23: 00         NOP                     
6F24: 08 00 4D   LD      ($4D00),SP      
6F27: 00         NOP                     
6F28: 00         NOP                     
6F29: 08 4E 00   LD      ($004E),SP      
6F2C: 08 08 4F   LD      ($4F08),SP      
6F2F: 00         NOP                     
6F30: 10 F8      STOP    $F8             
6F32: 70         LD      (HL),B          
6F33: 00         NOP                     
6F34: 18 F8      JR      $6F2E           
6F36: 71         LD      (HL),C          
6F37: 00         NOP                     
6F38: 10 00      STOP    $00             
6F3A: 72         LD      (HL),D          
6F3B: 00         NOP                     
6F3C: 18 00      JR      $6F3E           
6F3E: 73         LD      (HL),E          
6F3F: 00         NOP                     
6F40: 10 08      STOP    $08             
6F42: 74         LD      (HL),H          
6F43: 00         NOP                     
6F44: 18 08      JR      $6F4E           
6F46: 75         LD      (HL),L          
6F47: 00         NOP                     
6F48: 10 10      STOP    $10             
6F4A: 76         HALT                    
6F4B: 00         NOP                     
6F4C: 18 10      JR      $6F5E           
6F4E: 77         LD      (HL),A          
6F4F: 00         NOP                     
6F50: 00         NOP                     
6F51: 00         NOP                     
6F52: 4C         LD      C,H             
6F53: 00         NOP                     
6F54: 08 00 4D   LD      ($4D00),SP      
6F57: 00         NOP                     
6F58: 00         NOP                     
6F59: 08 4E 00   LD      ($004E),SP      
6F5C: 08 08 4F   LD      ($4F08),SP      
6F5F: 00         NOP                     
6F60: 10 F8      STOP    $F8             
6F62: 78         LD      A,B             
6F63: 00         NOP                     
6F64: 18 F8      JR      $6F5E           
6F66: 79         LD      A,C             
6F67: 00         NOP                     
6F68: 10 00      STOP    $00             
6F6A: 7A         LD      A,D             
6F6B: 00         NOP                     
6F6C: 18 00      JR      $6F6E           
6F6E: 7B         LD      A,E             
6F6F: 00         NOP                     
6F70: 10 08      STOP    $08             
6F72: 7C         LD      A,H             
6F73: 00         NOP                     
6F74: 18 08      JR      $6F7E           
6F76: 7D         LD      A,L             
6F77: 00         NOP                     
6F78: 10 10      STOP    $10             
6F7A: 7E         LD      A,(HL)          
6F7B: 00         NOP                     
6F7C: 18 10      JR      $6F8E           
6F7E: 7F         LD      A,A             
6F7F: 00         NOP                     
6F80: 3E 3C      LD      A,$3C           
6F82: EA C0 C3   LD      ($C3C0),A       
6F85: F0 E7      LD      A,($E7)         
6F87: E6 03      AND     $03             
6F89: 20 0C      JR      NZ,$6F97        
6F8B: FA 0F D0   LD      A,($D00F)       
6F8E: 3C         INC     A               
6F8F: FE 31      CP      $31             
6F91: 38 01      JR      C,$6F94         
6F93: AF         XOR     A               
6F94: EA 0F D0   LD      ($D00F),A       
6F97: FA 0F D0   LD      A,($D00F)       
6F9A: 5F         LD      E,A             
6F9B: 50         LD      D,B             
6F9C: 21 67 72   LD      HL,$7267        
6F9F: 19         ADD     HL,DE           
6FA0: F0 97      LD      A,($97)         
6FA2: 57         LD      D,A             
6FA3: 7E         LD      A,(HL)          
6FA4: CB 2F      SET     1,E             
6FA6: 5F         LD      E,A             
6FA7: F0 EC      LD      A,($EC)         
6FA9: 83         ADD     A,E             
6FAA: 92         SUB     D               
6FAB: E0 EC      LDFF00  ($EC),A         
6FAD: F0 E7      LD      A,($E7)         
6FAF: 1F         RRA                     
6FB0: 1F         RRA                     
6FB1: 1F         RRA                     
6FB2: E6 03      AND     $03             
6FB4: 17         RLA                     
6FB5: 17         RLA                     
6FB6: 17         RLA                     
6FB7: 17         RLA                     
6FB8: E6 F0      AND     $F0             
6FBA: 5F         LD      E,A             
6FBB: 17         RLA                     
6FBC: E6 E0      AND     $E0             
6FBE: 83         ADD     A,E             
6FBF: 5F         LD      E,A             
6FC0: 50         LD      D,B             
6FC1: 21 C0 6E   LD      HL,$6EC0        
6FC4: 19         ADD     HL,DE           
6FC5: 0E 0C      LD      C,$0C           
6FC7: CD 20 3D   CALL    $3D20           
6FCA: 3E 0C      LD      A,$0C           
6FCC: CD D0 3D   CALL    $3DD0           
6FCF: C9         RET                     
6FD0: 00         NOP                     
6FD1: 00         NOP                     
6FD2: 00         NOP                     
6FD3: 00         NOP                     
6FD4: 00         NOP                     
6FD5: 08 02 00   LD      ($0002),SP      
6FD8: 00         NOP                     
6FD9: 10 04      STOP    $04             
6FDB: 00         NOP                     
6FDC: 00         NOP                     
6FDD: 18 06      JR      $6FE5           
6FDF: 00         NOP                     
6FE0: 00         NOP                     
6FE1: 20 08      JR      NZ,$6FEB        
6FE3: 00         NOP                     
6FE4: 00         NOP                     
6FE5: 28 0A      JR      Z,$6FF1         
6FE7: 00         NOP                     
6FE8: 10 20      STOP    $20             
6FEA: 14         INC     D               
6FEB: 00         NOP                     
6FEC: 10 28      STOP    $28             
6FEE: 16 00      LD      D,$00           
6FF0: 20 20      JR      NZ,$7012        
6FF2: 1E 00      LD      E,$00           
6FF4: 20 28      JR      NZ,$701E        
6FF6: 20 00      JR      NZ,$6FF8        
6FF8: 30 00      JR      NC,$6FFA        
6FFA: 50         LD      D,B             
6FFB: 00         NOP                     
6FFC: 30 08      JR      NC,$7006        
6FFE: 22         LD      (HLI),A         
6FFF: 00         NOP                     
7000: 30 10      JR      NC,$7012        
7002: 24         INC     H               
7003: 00         NOP                     
7004: 30 18      JR      NC,$701E        
7006: 26 00      LD      H,$00           
7008: 30 20      JR      NC,$702A        
700A: 28 00      JR      Z,$700C         
700C: 30 28      JR      NC,$7036        
700E: 2A         LD      A,(HLI)         
700F: 00         NOP                     
7010: 30 30      JR      NC,$7042        
7012: 2C         INC     L               
7013: 00         NOP                     
7014: 30 38      JR      NC,$704E        
7016: 2E 00      LD      L,$00           
7018: 40         LD      B,B             
7019: 00         NOP                     
701A: 30 00      JR      NC,$701C        
701C: 40         LD      B,B             
701D: 08 32 00   LD      ($0032),SP      
7020: 40         LD      B,B             
7021: 10 34      STOP    $34             
7023: 00         NOP                     
7024: 40         LD      B,B             
7025: 18 36      JR      $705D           
7027: 00         NOP                     
7028: 40         LD      B,B             
7029: 20 38      JR      NZ,$7063        
702B: 00         NOP                     
702C: 40         LD      B,B             
702D: 28 3A      JR      Z,$7069         
702F: 00         NOP                     
7030: 40         LD      B,B             
7031: 30 3C      JR      NC,$706F        
7033: 00         NOP                     
7034: 40         LD      B,B             
7035: 38 3E      JR      C,$7075         
7037: 00         NOP                     
7038: 40         LD      B,B             
7039: 40         LD      B,B             
703A: 40         LD      B,B             
703B: 00         NOP                     
703C: 10 00      STOP    $00             
703E: 0C         INC     C               
703F: 00         NOP                     
7040: 10 08      STOP    $08             
7042: 0E 00      LD      C,$00           
7044: 10 10      STOP    $10             
7046: 10 00      STOP    $00             
7048: 10 18      STOP    $18             
704A: 12         LD      (DE),A          
704B: 00         NOP                     
704C: 20 08      JR      NZ,$7056        
704E: 18 00      JR      $7050           
7050: 20 10      JR      NZ,$7062        
7052: 1A         LD      A,(DE)          
7053: 00         NOP                     
7054: 20 18      JR      NZ,$706E        
7056: 1C         INC     E               
7057: 00         NOP                     
7058: FF         RST     0X38            
7059: FF         RST     0X38            
705A: FF         RST     0X38            
705B: FF         RST     0X38            
705C: 10 00      STOP    $00             
705E: 0C         INC     C               
705F: 00         NOP                     
7060: 10 08      STOP    $08             
7062: 42         LD      B,D             
7063: 00         NOP                     
7064: 10 10      STOP    $10             
7066: 44         LD      B,H             
7067: 00         NOP                     
7068: 10 18      STOP    $18             
706A: 46         LD      B,(HL)          
706B: 00         NOP                     
706C: 20 08      JR      NZ,$7076        
706E: 18 00      JR      $7070           
7070: 20 10      JR      NZ,$7082        
7072: 48         LD      C,B             
7073: 00         NOP                     
7074: 20 18      JR      NZ,$708E        
7076: 4A         LD      C,D             
7077: 00         NOP                     
7078: FF         RST     0X38            
7079: FF         RST     0X38            
707A: FF         RST     0X38            
707B: FF         RST     0X38            
707C: 10 00      STOP    $00             
707E: 0C         INC     C               
707F: 00         NOP                     
7080: 10 08      STOP    $08             
7082: 52         LD      D,D             
7083: 00         NOP                     
7084: 10 10      STOP    $10             
7086: 54         LD      D,H             
7087: 00         NOP                     
7088: 10 18      STOP    $18             
708A: 56         LD      D,(HL)          
708B: 00         NOP                     
708C: 20 08      JR      NZ,$7096        
708E: 18 00      JR      $7090           
7090: 20 10      JR      NZ,$70A2        
7092: 58         LD      E,B             
7093: 00         NOP                     
7094: 20 18      JR      NZ,$70AE        
7096: 5A         LD      E,D             
7097: 00         NOP                     
7098: FF         RST     0X38            
7099: FF         RST     0X38            
709A: FF         RST     0X38            
709B: FF         RST     0X38            
709C: FA 0F D0   LD      A,($D00F)       
709F: 5F         LD      E,A             
70A0: 50         LD      D,B             
70A1: 21 67 72   LD      HL,$7267        
70A4: 19         ADD     HL,DE           
70A5: 7E         LD      A,(HL)          
70A6: CB 2F      SET     1,E             
70A8: 5F         LD      E,A             
70A9: F0 EC      LD      A,($EC)         
70AB: 83         ADD     A,E             
70AC: E0 EC      LDFF00  ($EC),A         
70AE: 21 D0 6F   LD      HL,$6FD0        
70B1: 0E 1B      LD      C,$1B           
70B3: CD 20 3D   CALL    $3D20           
70B6: 3E 1B      LD      A,$1B           
70B8: CD D0 3D   CALL    $3DD0           
70BB: FA 03 D0   LD      A,($D003)       
70BE: 17         RLA                     
70BF: 17         RLA                     
70C0: 17         RLA                     
70C1: 17         RLA                     
70C2: 17         RLA                     
70C3: E6 E0      AND     $E0             
70C5: 5F         LD      E,A             
70C6: 50         LD      D,B             
70C7: 21 3C 70   LD      HL,$703C        
70CA: 19         ADD     HL,DE           
70CB: 0E 07      LD      C,$07           
70CD: 3E 40      LD      A,$40           
70CF: EA C0 C3   LD      ($C3C0),A       
70D2: CD 26 3D   CALL    $3D26           
70D5: 3E 07      LD      A,$07           
70D7: CD D0 3D   CALL    $3DD0           
70DA: C9         RET                     
70DB: 00         NOP                     
70DC: 00         NOP                     
70DD: 70         LD      (HL),B          
70DE: 00         NOP                     
70DF: 00         NOP                     
70E0: 00         NOP                     
70E1: 70         LD      (HL),B          
70E2: 00         NOP                     
70E3: 00         NOP                     
70E4: 00         NOP                     
70E5: 70         LD      (HL),B          
70E6: 00         NOP                     
70E7: 00         NOP                     
70E8: 00         NOP                     
70E9: 70         LD      (HL),B          
70EA: 00         NOP                     
70EB: 08 08 5C   LD      ($5C08),SP      
70EE: 00         NOP                     
70EF: 08 08 5C   LD      ($5C08),SP      
70F2: 00         NOP                     
70F3: 00         NOP                     
70F4: 00         NOP                     
70F5: 70         LD      (HL),B          
70F6: 00         NOP                     
70F7: 08 08 5E   LD      ($5E08),SP      
70FA: 00         NOP                     
70FB: 08 10 60   LD      ($6010),SP      
70FE: 00         NOP                     
70FF: 21 40 C3   LD      HL,$C340        
7102: 09         ADD     HL,BC           
7103: 36 C3      LD      (HL),$C3        
7105: F0 F1      LD      A,($F1)         
7107: 17         RLA                     
7108: 17         RLA                     
7109: E6 FC      AND     $FC             
710B: 5F         LD      E,A             
710C: 17         RLA                     
710D: E6 F8      AND     $F8             
710F: 83         ADD     A,E             
7110: 5F         LD      E,A             
7111: 50         LD      D,B             
7112: 21 DB 70   LD      HL,$70DB        
7115: 19         ADD     HL,DE           
7116: 0E 03      LD      C,$03           
7118: CD 26 3D   CALL    $3D26           
711B: CD 91 08   CALL    $0891           
711E: FE 01      CP      $01             
7120: 28 04      JR      Z,$7126         
7122: FE 30      CP      $30             
7124: 20 05      JR      NZ,$712B        
7126: 21 B0 C3   LD      HL,$C3B0        
7129: 09         ADD     HL,BC           
712A: 34         INC     (HL)            
712B: C9         RET                     
712C: 00         NOP                     
712D: 00         NOP                     
712E: 62         LD      H,D             
712F: 10 00      STOP    $00             
7131: 08 62 30   LD      ($3062),SP      
7134: 10 F0      STOP    $F0             
7136: 64         LD      H,H             
7137: 10 10      STOP    $10             
7139: F8 66      LDHL    SP,$66          
713B: 10 10      STOP    $10             
713D: 00         NOP                     
713E: 68         LD      L,B             
713F: 10 10      STOP    $10             
7141: 08 68 30   LD      ($3068),SP      
7144: 10 10      STOP    $10             
7146: 66         LD      H,(HL)          
7147: 30 10      JR      NC,$7159        
7149: 18 64      JR      $71AF           
714B: 30 20      JR      NC,$716D        
714D: 00         NOP                     
714E: 6A         LD      L,D             
714F: 10 20      STOP    $20             
7151: 08 6A 30   LD      ($306A),SP      
7154: 30 F8      JR      NC,$714E        
7156: 6C         LD      L,H             
7157: 10 30      STOP    $30             
7159: 00         NOP                     
715A: 6E         LD      L,(HL)          
715B: 10 30      STOP    $30             
715D: 08 6E 30   LD      ($306E),SP      
7160: 30 10      JR      NC,$7172        
7162: 6C         LD      L,H             
7163: 30 AF      JR      NC,$7114        
7165: EA C0 C3   LD      ($C3C0),A       
7168: 21 97 FF   LD      HL,$FF97        
716B: F0 EC      LD      A,($EC)         
716D: 96         SUB     (HL)            
716E: E0 EC      LDFF00  ($EC),A         
7170: 21 2C 71   LD      HL,$712C        
7173: 0E 0E      LD      C,$0E           
7175: CD 26 3D   CALL    $3D26           
7178: 3E 0E      LD      A,$0E           
717A: CD D0 3D   CALL    $3DD0           
717D: 21 50 C2   LD      HL,$C250        
7180: 09         ADD     HL,BC           
7181: 36 FE      LD      (HL),$FE        
7183: CD BB 7B   CALL    $7BBB           
7186: F0 F0      LD      A,($F0)         
7188: FE 02      CP      $02             
718A: 30 0E      JR      NC,$719A        
718C: CD 91 08   CALL    $0891           
718F: 20 09      JR      NZ,$719A        
7191: 36 C0      LD      (HL),$C0        
7193: CD 8D 3B   CALL    $3B8D           
7196: 3E 17      LD      A,$17           
7198: E0 F3      LDFF00  ($F3),A         
719A: C9         RET                     
719B: 00         NOP                     
719C: 08 B2 00   LD      ($00B2),SP      
719F: 00         NOP                     
71A0: 10 B4      STOP    $B4             
71A2: 00         NOP                     
71A3: 00         NOP                     
71A4: 18 B6      JR      $715C           
71A6: 00         NOP                     
71A7: 00         NOP                     
71A8: 20 B8      JR      NZ,$7162        
71AA: 00         NOP                     
71AB: 10 10      STOP    $10             
71AD: BA         CP      D               
71AE: 00         NOP                     
71AF: 10 18      STOP    $18             
71B1: BC         CP      H               
71B2: 00         NOP                     
71B3: 10 20      STOP    $20             
71B5: 86         ADD     A,(HL)          
71B6: 00         NOP                     
71B7: 20 00      JR      NZ,$71B9        
71B9: 88         ADC     A,B             
71BA: 00         NOP                     
71BB: 20 08      JR      NZ,$71C5        
71BD: 8A         ADC     A,D             
71BE: 00         NOP                     
71BF: 20 10      JR      NZ,$71D1        
71C1: 8C         ADC     A,H             
71C2: 00         NOP                     
71C3: 20 18      JR      NZ,$71DD        
71C5: 8E         ADC     A,(HL)          
71C6: 00         NOP                     
71C7: 20 20      JR      NZ,$71E9        
71C9: 94         SUB     H               
71CA: 00         NOP                     
71CB: 30 00      JR      NC,$71CD        
71CD: 98         SBC     B               
71CE: 00         NOP                     
71CF: 30 08      JR      NC,$71D9        
71D1: 9A         SBC     D               
71D2: 00         NOP                     
71D3: 30 10      JR      NC,$71E5        
71D5: A4         AND     H               
71D6: 00         NOP                     
71D7: 30 18      JR      NC,$71F1        
71D9: A8         XOR     B               
71DA: 00         NOP                     
71DB: 30 20      JR      NC,$71FD        
71DD: AA         XOR     D               
71DE: 00         NOP                     
71DF: 00         NOP                     
71E0: 08 C2 00   LD      ($00C2),SP      
71E3: 00         NOP                     
71E4: 10 C4      STOP    $C4             
71E6: 00         NOP                     
71E7: 00         NOP                     
71E8: 18 C6      JR      $71B0           
71EA: 00         NOP                     
71EB: 00         NOP                     
71EC: 20 C8      JR      NZ,$71B6        
71EE: 00         NOP                     
71EF: 10 10      STOP    $10             
71F1: CA 00 10   JP      Z,$1000         
71F4: 18 CC      JR      $71C2           
71F6: 00         NOP                     
71F7: 10 20      STOP    $20             
71F9: 96         SUB     (HL)            
71FA: 00         NOP                     
71FB: 20 00      JR      NZ,$71FD        
71FD: 88         ADC     A,B             
71FE: 00         NOP                     
71FF: 20 08      JR      NZ,$7209        
7201: 8A         ADC     A,D             
7202: 00         NOP                     
7203: 20 10      JR      NZ,$7215        
7205: 8C         ADC     A,H             
7206: 00         NOP                     
7207: 20 18      JR      NZ,$7221        
7209: 8E         ADC     A,(HL)          
720A: 00         NOP                     
720B: 20 20      JR      NZ,$722D        
720D: 94         SUB     H               
720E: 00         NOP                     
720F: 30 00      JR      NC,$7211        
7211: 98         SBC     B               
7212: 00         NOP                     
7213: 30 08      JR      NC,$721D        
7215: 9A         SBC     D               
7216: 00         NOP                     
7217: 30 10      JR      NC,$7229        
7219: A4         AND     H               
721A: 00         NOP                     
721B: 30 18      JR      NC,$7235        
721D: A8         XOR     B               
721E: 00         NOP                     
721F: 30 20      JR      NC,$7241        
7221: AA         XOR     D               
7222: 00         NOP                     
7223: 00         NOP                     
7224: 08 D2 00   LD      ($00D2),SP      
7227: 00         NOP                     
7228: 10 D4      STOP    $D4             
722A: 00         NOP                     
722B: 00         NOP                     
722C: 18 D6      JR      $7204           
722E: 00         NOP                     
722F: 00         NOP                     
7230: 20 D8      JR      NZ,$720A        
7232: 00         NOP                     
7233: 10 10      STOP    $10             
7235: DA 00 10   JP      C,$1000         
7238: 18 DC      JR      $7216           
723A: 00         NOP                     
723B: 10 20      STOP    $20             
723D: A6         AND     (HL)            
723E: 00         NOP                     
723F: 20 00      JR      NZ,$7241        
7241: 88         ADC     A,B             
7242: 00         NOP                     
7243: 20 08      JR      NZ,$724D        
7245: 8A         ADC     A,D             
7246: 00         NOP                     
7247: 20 10      JR      NZ,$7259        
7249: 8C         ADC     A,H             
724A: 00         NOP                     
724B: 20 18      JR      NZ,$7265        
724D: 8E         ADC     A,(HL)          
724E: 00         NOP                     
724F: 20 20      JR      NZ,$7271        
7251: 94         SUB     H               
7252: 00         NOP                     
7253: 30 00      JR      NC,$7255        
7255: 98         SBC     B               
7256: 00         NOP                     
7257: 30 08      JR      NC,$7261        
7259: 9A         SBC     D               
725A: 00         NOP                     
725B: 30 10      JR      NC,$726D        
725D: A4         AND     H               
725E: 00         NOP                     
725F: 30 18      JR      NC,$7279        
7261: A8         XOR     B               
7262: 00         NOP                     
7263: 30 20      JR      NC,$7285        
7265: AA         XOR     D               
7266: 00         NOP                     
7267: 00         NOP                     
7268: 00         NOP                     
7269: 00         NOP                     
726A: 00         NOP                     
726B: 00         NOP                     
726C: 00         NOP                     
726D: 01 01 01   LD      BC,$0101        
7270: 01 02 02   LD      BC,$0202        
7273: 02         LD      (BC),A          
7274: 03         INC     BC              
7275: 03         INC     BC              
7276: 04         INC     B               
7277: 05         DEC     B               
7278: 05         DEC     B               
7279: 06 06      LD      B,$06           
727B: 06 07      LD      B,$07           
727D: 07         RLCA                    
727E: 07         RLCA                    
727F: 07         RLCA                    
7280: 08 08 08   LD      ($0808),SP      
7283: 08 08 08   LD      ($0808),SP      
7286: 07         RLCA                    
7287: 07         RLCA                    
7288: 07         RLCA                    
7289: 07         RLCA                    
728A: 06 06      LD      B,$06           
728C: 06 05      LD      B,$05           
728E: 05         DEC     B               
728F: 04         INC     B               
7290: 03         INC     BC              
7291: 02         LD      (BC),A          
7292: 02         LD      (BC),A          
7293: 02         LD      (BC),A          
7294: 01 01 01   LD      BC,$0101        
7297: 01 3E 00   LD      BC,$003E        
729A: EA C0 C3   LD      ($C3C0),A       
729D: F0 97      LD      A,($97)         
729F: 57         LD      D,A             
72A0: CB 2F      SET     1,E             
72A2: 82         ADD     A,D             
72A3: E0 D7      LDFF00  ($D7),A         
72A5: F0 E7      LD      A,($E7)         
72A7: E6 03      AND     $03             
72A9: 20 0C      JR      NZ,$72B7        
72AB: FA 0F D0   LD      A,($D00F)       
72AE: 3C         INC     A               
72AF: FE 31      CP      $31             
72B1: 38 01      JR      C,$72B4         
72B3: AF         XOR     A               
72B4: EA 0F D0   LD      ($D00F),A       
72B7: FA 0F D0   LD      A,($D00F)       
72BA: 5F         LD      E,A             
72BB: 50         LD      D,B             
72BC: 21 67 72   LD      HL,$7267        
72BF: 19         ADD     HL,DE           
72C0: F0 EC      LD      A,($EC)         
72C2: 86         ADD     A,(HL)          
72C3: 21 D7 FF   LD      HL,$FFD7        
72C6: 96         SUB     (HL)            
72C7: E0 EC      LDFF00  ($EC),A         
72C9: FE A8      CP      $A8             
72CB: D2 61 7A   JP      NC,$7A61        
72CE: FA 00 D0   LD      A,($D000)       
72D1: 17         RLA                     
72D2: 17         RLA                     
72D3: E6 FC      AND     $FC             
72D5: 5F         LD      E,A             
72D6: 17         RLA                     
72D7: 17         RLA                     
72D8: 17         RLA                     
72D9: 17         RLA                     
72DA: E6 C0      AND     $C0             
72DC: 83         ADD     A,E             
72DD: 5F         LD      E,A             
72DE: 50         LD      D,B             
72DF: 21 9B 71   LD      HL,$719B        
72E2: 19         ADD     HL,DE           
72E3: 0E 11      LD      C,$11           
72E5: CD 26 3D   CALL    $3D26           
72E8: 3E 11      LD      A,$11           
72EA: CD D0 3D   CALL    $3DD0           
72ED: C9         RET                     
72EE: 00         NOP                     
72EF: 00         NOP                     
72F0: 70         LD      (HL),B          
72F1: 00         NOP                     
72F2: 08 08 5E   LD      ($5E08),SP      
72F5: 00         NOP                     
72F6: 08 10 60   LD      ($6010),SP      
72F9: 00         NOP                     
72FA: 21 40 C3   LD      HL,$C340        
72FD: 09         ADD     HL,BC           
72FE: 36 C3      LD      (HL),$C3        
7300: 21 EE 72   LD      HL,$72EE        
7303: 0E 03      LD      C,$03           
7305: CD 26 3D   CALL    $3D26           
7308: C9         RET                     
7309: 50         LD      D,B             
730A: 00         NOP                     
730B: 52         LD      D,D             
730C: 00         NOP                     
730D: 54         LD      D,H             
730E: 00         NOP                     
730F: 56         LD      D,(HL)          
7310: 00         NOP                     
7311: 57         LD      D,A             
7312: 00         NOP                     
7313: 5A         LD      E,D             
7314: 00         NOP                     
7315: F0 E7      LD      A,($E7)         
7317: E6 07      AND     $07             
7319: 20 0C      JR      NZ,$7327        
731B: 21 B0 C3   LD      HL,$C3B0        
731E: 09         ADD     HL,BC           
731F: 7E         LD      A,(HL)          
7320: 3C         INC     A               
7321: FE 06      CP      $06             
7323: 20 01      JR      NZ,$7326        
7325: AF         XOR     A               
7326: 77         LD      (HL),A          
7327: 21 40 C3   LD      HL,$C340        
732A: 09         ADD     HL,BC           
732B: 36 C1      LD      (HL),$C1        
732D: 21 40 C2   LD      HL,$C240        
7330: 09         ADD     HL,BC           
7331: 7E         LD      A,(HL)          
7332: E6 80      AND     $80             
7334: 28 05      JR      Z,$733B         
7336: 21 ED FF   LD      HL,$FFED        
7339: CB EE      SET     1,E             
733B: 11 09 73   LD      DE,$7309        
733E: CD D0 3C   CALL    $3CD0           
7341: CD C5 7B   CALL    $7BC5           
7344: F0 EE      LD      A,($EE)         
7346: FE B0      CP      $B0             
7348: D2 61 7A   JP      NC,$7A61        
734B: C9         RET                     
734C: 00         NOP                     
734D: 08 0E 00   LD      ($000E),SP      
7350: 00         NOP                     
7351: 10 1E      STOP    $1E             
7353: 00         NOP                     
7354: 00         NOP                     
7355: 18 2E      JR      $7385           
7357: 00         NOP                     
7358: 10 00      STOP    $00             
735A: 50         LD      D,B             
735B: 00         NOP                     
735C: 10 08      STOP    $08             
735E: 52         LD      D,D             
735F: 00         NOP                     
7360: 10 10      STOP    $10             
7362: 54         LD      D,H             
7363: 00         NOP                     
7364: 10 18      STOP    $18             
7366: 58         LD      E,B             
7367: 00         NOP                     
7368: 00         NOP                     
7369: 08 0E 00   LD      ($000E),SP      
736C: 00         NOP                     
736D: 10 1E      STOP    $1E             
736F: 00         NOP                     
7370: 00         NOP                     
7371: 18 2E      JR      $73A1           
7373: 00         NOP                     
7374: 10 00      STOP    $00             
7376: 60         LD      H,B             
7377: 00         NOP                     
7378: 10 08      STOP    $08             
737A: 62         LD      H,D             
737B: 00         NOP                     
737C: 10 10      STOP    $10             
737E: 64         LD      H,H             
737F: 00         NOP                     
7380: 10 18      STOP    $18             
7382: 68         LD      L,B             
7383: 00         NOP                     
7384: 00         NOP                     
7385: 00         NOP                     
7386: 00         NOP                     
7387: 01 02 02   LD      BC,$0202        
738A: 02         LD      (BC),A          
738B: 01 00 00   LD      BC,$0000        
738E: 00         NOP                     
738F: 00         NOP                     
7390: 01 01 01   LD      BC,$0101        
7393: 01 21 40   LD      BC,$4021        
7396: C3 09 36   JP      $3609           
7399: C7         RST     0X00            
739A: 3E 00      LD      A,$00           
739C: EA C0 C3   LD      ($C3C0),A       
739F: F0 E7      LD      A,($E7)         
73A1: 1F         RRA                     
73A2: 1F         RRA                     
73A3: 1F         RRA                     
73A4: 1F         RRA                     
73A5: E6 07      AND     $07             
73A7: 5F         LD      E,A             
73A8: 50         LD      D,B             
73A9: 21 84 73   LD      HL,$7384        
73AC: 19         ADD     HL,DE           
73AD: F0 EC      LD      A,($EC)         
73AF: 86         ADD     A,(HL)          
73B0: E0 EC      LDFF00  ($EC),A         
73B2: 21 4C 73   LD      HL,$734C        
73B5: F0 E7      LD      A,($E7)         
73B7: E6 10      AND     $10             
73B9: 28 03      JR      Z,$73BE         
73BB: 21 68 73   LD      HL,$7368        
73BE: 0E 07      LD      C,$07           
73C0: CD 26 3D   CALL    $3D26           
73C3: C9         RET                     
73C4: 5A         LD      E,D             
73C5: 00         NOP                     
73C6: 6A         LD      L,D             
73C7: 00         NOP                     
73C8: 21 40 C3   LD      HL,$C340        
73CB: 09         ADD     HL,BC           
73CC: 36 C1      LD      (HL),$C1        
73CE: 79         LD      A,C             
73CF: 17         RLA                     
73D0: E6 06      AND     $06             
73D2: 5F         LD      E,A             
73D3: F0 E7      LD      A,($E7)         
73D5: 1F         RRA                     
73D6: 1F         RRA                     
73D7: 1F         RRA                     
73D8: 1F         RRA                     
73D9: 83         ADD     A,E             
73DA: E6 07      AND     $07             
73DC: 5F         LD      E,A             
73DD: 50         LD      D,B             
73DE: 21 8C 73   LD      HL,$738C        
73E1: 19         ADD     HL,DE           
73E2: F0 EC      LD      A,($EC)         
73E4: 86         ADD     A,(HL)          
73E5: E0 EC      LDFF00  ($EC),A         
73E7: 11 C4 73   LD      DE,$73C4        
73EA: CD D0 3C   CALL    $3CD0           
73ED: C9         RET                     
73EE: 54         LD      D,H             
73EF: 00         NOP                     
73F0: 64         LD      H,H             
73F1: 00         NOP                     
73F2: 64         LD      H,H             
73F3: 20 54      JR      NZ,$7449        
73F5: 20 4E      JR      NZ,$7445        
73F7: 00         NOP                     
73F8: 7E         LD      A,(HL)          
73F9: 00         NOP                     
73FA: 21 40 C3   LD      HL,$C340        
73FD: 09         ADD     HL,BC           
73FE: 36 C2      LD      (HL),$C2        
7400: F0 F1      LD      A,($F1)         
7402: FE 01      CP      $01             
7404: 28 21      JR      Z,$7427         
7406: FE 02      CP      $02             
7408: 28 2A      JR      Z,$7434         
740A: FA 0A D0   LD      A,($D00A)       
740D: 5F         LD      E,A             
740E: 50         LD      D,B             
740F: 21 49 5B   LD      HL,$5B49        
7412: 19         ADD     HL,DE           
7413: 7E         LD      A,(HL)          
7414: D6 04      SUB     $04             
7416: 2F         CPL                     
7417: 3C         INC     A               
7418: CB 2F      SET     1,E             
741A: 5F         LD      E,A             
741B: F0 EC      LD      A,($EC)         
741D: 83         ADD     A,E             
741E: E0 EC      LDFF00  ($EC),A         
7420: 11 EE 73   LD      DE,$73EE        
7423: CD 3B 3C   CALL    $3C3B           
7426: C9         RET                     
7427: FA 0A D0   LD      A,($D00A)       
742A: C6 06      ADD     $06             
742C: FE 2B      CP      $2B             
742E: 38 02      JR      C,$7432         
7430: D6 2B      SUB     $2B             
7432: 18 D9      JR      $740D           
7434: FA 0A D0   LD      A,($D00A)       
7437: C6 18      ADD     $18             
7439: FE 2B      CP      $2B             
743B: 38 02      JR      C,$743F         
743D: D6 2B      SUB     $2B             
743F: 5F         LD      E,A             
7440: 16 00      LD      D,$00           
7442: 21 49 5B   LD      HL,$5B49        
7445: 19         ADD     HL,DE           
7446: 7E         LD      A,(HL)          
7447: D6 04      SUB     $04             
7449: CB 2F      SET     1,E             
744B: 18 C9      JR      $7416           
744D: 72         LD      (HL),D          
744E: 00         NOP                     
744F: 72         LD      (HL),D          
7450: 20 74      JR      NZ,$74C6        
7452: 00         NOP                     
7453: 74         LD      (HL),H          
7454: 20 76      JR      NZ,$74CC        
7456: 00         NOP                     
7457: 76         HALT                    
7458: 20 78      JR      NZ,$74D2        
745A: 00         NOP                     
745B: 78         LD      A,B             
745C: 20 7A      JR      NZ,$74D8        
745E: 00         NOP                     
745F: 7A         LD      A,D             
7460: 20 7C      JR      NZ,$74DE        
7462: 00         NOP                     
7463: 7C         LD      A,H             
7464: 20 08      JR      NZ,$746E        
7466: 06 06      LD      B,$06           
7468: 06 06      LD      B,$06           
746A: 08 21 40   LD      ($4021),SP      
746D: C3 09 36   JP      $3609           
7470: C2 11 4D   JP      NZ,$4D11        
7473: 74         LD      (HL),H          
7474: CD 3B 3C   CALL    $3C3B           
7477: CD 91 08   CALL    $0891           
747A: 20 16      JR      NZ,$7492        
747C: E5         PUSH    HL              
747D: 21 B0 C3   LD      HL,$C3B0        
7480: 09         ADD     HL,BC           
7481: 7E         LD      A,(HL)          
7482: 3C         INC     A               
7483: FE 06      CP      $06             
7485: 20 01      JR      NZ,$7488        
7487: AF         XOR     A               
7488: 77         LD      (HL),A          
7489: 5F         LD      E,A             
748A: 50         LD      D,B             
748B: 21 65 74   LD      HL,$7465        
748E: 19         ADD     HL,DE           
748F: 7E         LD      A,(HL)          
7490: E1         POP     HL              
7491: 77         LD      (HL),A          
7492: 21 D0 C3   LD      HL,$C3D0        
7495: 09         ADD     HL,BC           
7496: 7E         LD      A,(HL)          
7497: 3C         INC     A               
7498: 77         LD      (HL),A          
7499: E6 1F      AND     $1F             
749B: 20 0A      JR      NZ,$74A7        
749D: 21 50 C2   LD      HL,$C250        
74A0: 09         ADD     HL,BC           
74A1: 7E         LD      A,(HL)          
74A2: FE FF      CP      $FF             
74A4: 28 01      JR      Z,$74A7         
74A6: 34         INC     (HL)            
74A7: CD B8 7B   CALL    $7BB8           
74AA: F0 EE      LD      A,($EE)         
74AC: FE B0      CP      $B0             
74AE: D2 61 7A   JP      NC,$7A61        
74B1: C9         RET                     
74B2: D0         RET     NC              
74B3: 00         NOP                     
74B4: D2 00 D4   JP      NC,$D400        
74B7: 00         NOP                     
74B8: D6 00      SUB     $00             
74BA: D8         RET     C               
74BB: 00         NOP                     
74BC: DA 00 DC   JP      C,$DC00         
74BF: 00         NOP                     
74C0: DE 00      SBC     $00             
74C2: E0 00      LDFF00  ($00),A         
74C4: E2         LDFF00  (C),A           
74C5: 00         NOP                     
74C6: E4         ???                     
74C7: 00         NOP                     
74C8: E6 00      AND     $00             
74CA: E8 00      ADD     SP,$00          
74CC: EA 00 EC   LD      ($EC00),A       
74CF: 00         NOP                     
74D0: EE 00      XOR     $00             
74D2: 21 C0 C2   LD      HL,$C2C0        
74D5: 09         ADD     HL,BC           
74D6: 7E         LD      A,(HL)          
74D7: C6 50      ADD     $50             
74D9: E0 D7      LDFF00  ($D7),A         
74DB: 11 B2 74   LD      DE,$74B2        
74DE: CD E9 74   CALL    $74E9           
74E1: CD 87 08   CALL    $0887           
74E4: C8         RET     Z               
74E5: CD B8 7B   CALL    $7BB8           
74E8: C9         RET                     
74E9: C5         PUSH    BC              
74EA: D5         PUSH    DE              
74EB: F0 D7      LD      A,($D7)         
74ED: 5F         LD      E,A             
74EE: 50         LD      D,B             
74EF: 21 00 C0   LD      HL,$C000        
74F2: 19         ADD     HL,DE           
74F3: E5         PUSH    HL              
74F4: D1         POP     DE              
74F5: F0 EC      LD      A,($EC)         
74F7: 12         LD      (DE),A          
74F8: 13         INC     DE              
74F9: FA 55 C1   LD      A,($C155)       
74FC: 4F         LD      C,A             
74FD: F0 ED      LD      A,($ED)         
74FF: E6 20      AND     $20             
7501: 1F         RRA                     
7502: 1F         RRA                     
7503: 21 EE FF   LD      HL,$FFEE        
7506: 86         ADD     A,(HL)          
7507: 91         SUB     C               
7508: 12         LD      (DE),A          
7509: 13         INC     DE              
750A: F0 F1      LD      A,($F1)         
750C: 4F         LD      C,A             
750D: 06 00      LD      B,$00           
750F: CB 21      SET     1,E             
7511: CB 10      SET     1,E             
7513: CB 21      SET     1,E             
7515: CB 10      SET     1,E             
7517: E1         POP     HL              
7518: 09         ADD     HL,BC           
7519: 2A         LD      A,(HLI)         
751A: 12         LD      (DE),A          
751B: 13         INC     DE              
751C: 2A         LD      A,(HLI)         
751D: E5         PUSH    HL              
751E: 21 ED FF   LD      HL,$FFED        
7521: AE         XOR     (HL)            
7522: 12         LD      (DE),A          
7523: 13         INC     DE              
7524: F0 EC      LD      A,($EC)         
7526: 12         LD      (DE),A          
7527: 13         INC     DE              
7528: FA 55 C1   LD      A,($C155)       
752B: 4F         LD      C,A             
752C: F0 ED      LD      A,($ED)         
752E: E6 20      AND     $20             
7530: EE 20      XOR     $20             
7532: 1F         RRA                     
7533: 1F         RRA                     
7534: 21 EE FF   LD      HL,$FFEE        
7537: 91         SUB     C               
7538: 86         ADD     A,(HL)          
7539: 12         LD      (DE),A          
753A: 13         INC     DE              
753B: E1         POP     HL              
753C: 2A         LD      A,(HLI)         
753D: 12         LD      (DE),A          
753E: 13         INC     DE              
753F: 7E         LD      A,(HL)          
7540: 21 ED FF   LD      HL,$FFED        
7543: AE         XOR     (HL)            
7544: 12         LD      (DE),A          
7545: C1         POP     BC              
7546: C9         RET                     
7547: 21 B0 C2   LD      HL,$C2B0        
754A: 09         ADD     HL,BC           
754B: 7E         LD      A,(HL)          
754C: C7         RST     0X00            
754D: 6F         LD      L,A             
754E: 75         LD      (HL),L          
754F: 0C         INC     C               
7550: 79         LD      A,C             
7551: BA         CP      D               
7552: 79         LD      A,C             
7553: D2 74 94   JP      NC,$9474        
7556: 73         LD      (HL),E          
7557: C8         RET     Z               
7558: 73         LD      (HL),E          
7559: 15         DEC     D               
755A: 73         LD      (HL),E          
755B: FA 72 FA   LD      A,($FA72)       
755E: 73         LD      (HL),E          
755F: 6B         LD      L,E             
7560: 74         LD      (HL),H          
7561: 98         SBC     B               
7562: 72         LD      (HL),D          
7563: 64         LD      H,H             
7564: 71         LD      (HL),C          
7565: FF         RST     0X38            
7566: 70         LD      (HL),B          
7567: 9C         SBC     H               
7568: 70         LD      (HL),B          
7569: 80         ADD     A,B             
756A: 6F         LD      L,A             
756B: 95         SUB     L               
756C: 6D         LD      L,L             
756D: 67         LD      H,A             
756E: 6E         LD      L,(HL)          
756F: CD B3 78   CALL    $78B3           
7572: F0 F0      LD      A,($F0)         
7574: C7         RST     0X00            
7575: 7F         LD      A,A             
7576: 75         LD      (HL),L          
7577: C4 75 FF   CALL    NZ,$FF75        
757A: 75         LD      (HL),L          
757B: 03         INC     BC              
757C: 76         HALT                    
757D: 1F         RRA                     
757E: 76         HALT                    
757F: F0 EC      LD      A,($EC)         
7581: FE 60      CP      $60             
7583: CA 8D 3B   JP      Z,$3B8D         
7586: 21 50 C2   LD      HL,$C250        
7589: 09         ADD     HL,BC           
758A: 36 08      LD      (HL),$08        
758C: CD BB 7B   CALL    $7BBB           
758F: 21 10 C2   LD      HL,$C210        
7592: 09         ADD     HL,BC           
7593: 7E         LD      A,(HL)          
7594: FE F0      CP      $F0             
7596: 20 11      JR      NZ,$75A9        
7598: 21 C0 C2   LD      HL,$C2C0        
759B: 09         ADD     HL,BC           
759C: 7E         LD      A,(HL)          
759D: FE 08      CP      $08             
759F: 30 08      JR      NC,$75A9        
75A1: 3C         INC     A               
75A2: 77         LD      (HL),A          
75A3: 21 10 C2   LD      HL,$C210        
75A6: 09         ADD     HL,BC           
75A7: 36 E0      LD      (HL),$E0        
75A9: 3E FF      LD      A,$FF           
75AB: E0 9B      LDFF00  ($9B),A         
75AD: F0 E7      LD      A,($E7)         
75AF: 1F         RRA                     
75B0: 1F         RRA                     
75B1: 1F         RRA                     
75B2: E6 01      AND     $01             
75B4: C6 00      ADD     $00             
75B6: E0 9D      LDFF00  ($9D),A         
75B8: C5         PUSH    BC              
75B9: AF         XOR     A               
75BA: E0 9A      LDFF00  ($9A),A         
75BC: CD D6 20   CALL    $20D6           
75BF: CD D3 7A   CALL    $7AD3           
75C2: C1         POP     BC              
75C3: C9         RET                     
75C4: 3E F8      LD      A,$F8           
75C6: E0 9B      LDFF00  ($9B),A         
75C8: CD AD 75   CALL    $75AD           
75CB: F0 99      LD      A,($99)         
75CD: FE 5C      CP      $5C             
75CF: 20 2D      JR      NZ,$75FE        
75D1: AF         XOR     A               
75D2: E0 9B      LDFF00  ($9B),A         
75D4: 3E 02      LD      A,$02           
75D6: E0 9D      LDFF00  ($9D),A         
75D8: 3E E8      LD      A,$E8           
75DA: CD 01 3C   CALL    $3C01           
75DD: 21 B0 C2   LD      HL,$C2B0        
75E0: 19         ADD     HL,DE           
75E1: 36 02      LD      (HL),$02        
75E3: 21 00 C2   LD      HL,$C200        
75E6: 19         ADD     HL,DE           
75E7: 36 50      LD      (HL),$50        
75E9: 21 10 C2   LD      HL,$C210        
75EC: 19         ADD     HL,DE           
75ED: 36 00      LD      (HL),$00        
75EF: 21 50 C2   LD      HL,$C250        
75F2: 19         ADD     HL,DE           
75F3: 36 14      LD      (HL),$14        
75F5: 21 E0 C2   LD      HL,$C2E0        
75F8: 19         ADD     HL,DE           
75F9: 36 30      LD      (HL),$30        
75FB: CD 8D 3B   CALL    $3B8D           
75FE: C9         RET                     
75FF: CD B8 75   CALL    $75B8           
7602: C9         RET                     
7603: CD B8 75   CALL    $75B8           
7606: CD 91 08   CALL    $0891           
7609: 20 10      JR      NZ,$761B        
760B: 36 08      LD      (HL),$08        
760D: 21 B0 C3   LD      HL,$C3B0        
7610: 09         ADD     HL,BC           
7611: 7E         LD      A,(HL)          
7612: 3C         INC     A               
7613: 77         LD      (HL),A          
7614: FE 05      CP      $05             
7616: 20 03      JR      NZ,$761B        
7618: CD 8D 3B   CALL    $3B8D           
761B: CD B8 75   CALL    $75B8           
761E: C9         RET                     
761F: CD B8 75   CALL    $75B8           
7622: C9         RET                     
7623: 00         NOP                     
7624: 00         NOP                     
7625: 10 10      STOP    $10             
7627: 00         NOP                     
7628: 08 04 10   LD      ($1004),SP      
762B: 00         NOP                     
762C: 10 06      STOP    $06             
762E: 10 00      STOP    $00             
7630: 18 06      JR      $7638           
7632: 30 00      JR      NC,$7634        
7634: 20 04      JR      NZ,$763A        
7636: 30 00      JR      NC,$7638        
7638: 28 10      JR      Z,$764A         
763A: 30 10      JR      NC,$764C        
763C: 00         NOP                     
763D: 08 10 10   LD      ($1010),SP      
7640: 08 0A 10   LD      ($100A),SP      
7643: 10 10      STOP    $10             
7645: 0C         INC     C               
7646: 10 10      STOP    $10             
7648: 18 0C      JR      $7656           
764A: 30 10      JR      NC,$765C        
764C: 20 0A      JR      NZ,$7658        
764E: 30 10      JR      NC,$7660        
7650: 28 08      JR      Z,$765A         
7652: 30 20      JR      NC,$7674        
7654: 10 20      STOP    $20             
7656: 10 20      STOP    $20             
7658: 18 30      JR      $768A           
765A: 10 30      STOP    $30             
765C: 10 20      STOP    $20             
765E: 10 30      STOP    $30             
7660: 18 30      JR      $7692           
7662: 10 40      STOP    $40             
7664: 10 20      STOP    $20             
7666: 10 40      STOP    $40             
7668: 18 30      JR      $769A           
766A: 10 50      STOP    $50             
766C: 10 20      STOP    $20             
766E: 10 50      STOP    $50             
7670: 18 30      JR      $76A2           
7672: 10 60      STOP    $60             
7674: 10 20      STOP    $20             
7676: 10 60      STOP    $60             
7678: 18 30      JR      $76AA           
767A: 10 70      STOP    $70             
767C: 10 20      STOP    $20             
767E: 10 70      STOP    $70             
7680: 18 30      JR      $76B2           
7682: 10 80      STOP    $80             
7684: 10 20      STOP    $20             
7686: 10 80      STOP    $80             
7688: 18 30      JR      $76BA           
768A: 10 90      STOP    $90             
768C: 10 20      STOP    $20             
768E: 10 90      STOP    $90             
7690: 18 30      JR      $76C2           
7692: 10 A0      STOP    $A0             
7694: 10 20      STOP    $20             
7696: 10 A0      STOP    $A0             
7698: 18 30      JR      $76CA           
769A: 10 B0      STOP    $B0             
769C: 10 20      STOP    $20             
769E: 10 B0      STOP    $B0             
76A0: 18 30      JR      $76D2           
76A2: 10 00      STOP    $00             
76A4: 00         NOP                     
76A5: 12         LD      (DE),A          
76A6: 10 00      STOP    $00             
76A8: 08 14 10   LD      ($1014),SP      
76AB: 00         NOP                     
76AC: 10 16      STOP    $16             
76AE: 10 00      STOP    $00             
76B0: 18 16      JR      $76C8           
76B2: 30 00      JR      NC,$76B4        
76B4: 20 14      JR      NZ,$76CA        
76B6: 30 00      JR      NC,$76B8        
76B8: 28 12      JR      Z,$76CC         
76BA: 30 10      JR      NC,$76CC        
76BC: 00         NOP                     
76BD: 18 10      JR      $76CF           
76BF: 10 08      STOP    $08             
76C1: 1A         LD      A,(DE)          
76C2: 10 10      STOP    $10             
76C4: 10 1C      STOP    $1C             
76C6: 10 10      STOP    $10             
76C8: 18 1C      JR      $76E6           
76CA: 30 10      JR      NC,$76DC        
76CC: 20 1A      JR      NZ,$76E8        
76CE: 30 10      JR      NC,$76E0        
76D0: 28 18      JR      Z,$76EA         
76D2: 30 20      JR      NC,$76F4        
76D4: 10 40      STOP    $40             
76D6: 10 20      STOP    $20             
76D8: 18 50      JR      $772A           
76DA: 10 30      STOP    $30             
76DC: 10 40      STOP    $40             
76DE: 10 30      STOP    $30             
76E0: 18 50      JR      $7732           
76E2: 10 40      STOP    $40             
76E4: 10 40      STOP    $40             
76E6: 10 40      STOP    $40             
76E8: 18 50      JR      $773A           
76EA: 10 50      STOP    $50             
76EC: 10 40      STOP    $40             
76EE: 10 50      STOP    $50             
76F0: 18 50      JR      $7742           
76F2: 10 60      STOP    $60             
76F4: 10 40      STOP    $40             
76F6: 10 60      STOP    $60             
76F8: 18 50      JR      $774A           
76FA: 10 70      STOP    $70             
76FC: 10 40      STOP    $40             
76FE: 10 70      STOP    $70             
7700: 18 50      JR      $7752           
7702: 10 80      STOP    $80             
7704: 10 40      STOP    $40             
7706: 10 80      STOP    $80             
7708: 18 50      JR      $775A           
770A: 10 90      STOP    $90             
770C: 10 40      STOP    $40             
770E: 10 90      STOP    $90             
7710: 18 50      JR      $7762           
7712: 10 A0      STOP    $A0             
7714: 10 40      STOP    $40             
7716: 10 A0      STOP    $A0             
7718: 18 50      JR      $776A           
771A: 10 B0      STOP    $B0             
771C: 10 40      STOP    $40             
771E: 10 B0      STOP    $B0             
7720: 18 50      JR      $7772           
7722: 10 00      STOP    $00             
7724: 00         NOP                     
7725: 22         LD      (HLI),A         
7726: 10 00      STOP    $00             
7728: 08 24 10   LD      ($1024),SP      
772B: 00         NOP                     
772C: 10 26      STOP    $26             
772E: 10 00      STOP    $00             
7730: 18 26      JR      $7758           
7732: 30 00      JR      NC,$7734        
7734: 20 24      JR      NZ,$775A        
7736: 30 00      JR      NC,$7738        
7738: 28 22      JR      Z,$775C         
773A: 30 10      JR      NC,$774C        
773C: 00         NOP                     
773D: 28 10      JR      Z,$774F         
773F: 10 08      STOP    $08             
7741: 2A         LD      A,(HLI)         
7742: 10 10      STOP    $10             
7744: 10 2C      STOP    $2C             
7746: 10 10      STOP    $10             
7748: 18 2C      JR      $7776           
774A: 30 10      JR      NC,$775C        
774C: 20 2A      JR      NZ,$7778        
774E: 30 10      JR      NC,$7760        
7750: 28 28      JR      Z,$777A         
7752: 30 20      JR      NC,$7774        
7754: 10 60      STOP    $60             
7756: 10 20      STOP    $20             
7758: 18 70      JR      $77CA           
775A: 10 30      STOP    $30             
775C: 10 60      STOP    $60             
775E: 10 30      STOP    $30             
7760: 18 70      JR      $77D2           
7762: 10 40      STOP    $40             
7764: 10 60      STOP    $60             
7766: 10 40      STOP    $40             
7768: 18 70      JR      $77DA           
776A: 10 50      STOP    $50             
776C: 10 60      STOP    $60             
776E: 10 50      STOP    $50             
7770: 18 70      JR      $77E2           
7772: 10 60      STOP    $60             
7774: 10 60      STOP    $60             
7776: 10 60      STOP    $60             
7778: 18 70      JR      $77EA           
777A: 10 70      STOP    $70             
777C: 10 60      STOP    $60             
777E: 10 70      STOP    $70             
7780: 18 70      JR      $77F2           
7782: 10 80      STOP    $80             
7784: 10 60      STOP    $60             
7786: 10 80      STOP    $80             
7788: 18 70      JR      $77FA           
778A: 10 90      STOP    $90             
778C: 10 60      STOP    $60             
778E: 10 90      STOP    $90             
7790: 18 70      JR      $7802           
7792: 10 A0      STOP    $A0             
7794: 10 60      STOP    $60             
7796: 10 A0      STOP    $A0             
7798: 18 70      JR      $780A           
779A: 10 B0      STOP    $B0             
779C: 10 60      STOP    $60             
779E: 10 B0      STOP    $B0             
77A0: 18 70      JR      $7812           
77A2: 10 00      STOP    $00             
77A4: 00         NOP                     
77A5: 32         LD      (HLD),A         
77A6: 10 00      STOP    $00             
77A8: 08 34 10   LD      ($1034),SP      
77AB: 00         NOP                     
77AC: 10 36      STOP    $36             
77AE: 10 00      STOP    $00             
77B0: 18 36      JR      $77E8           
77B2: 30 00      JR      NC,$77B4        
77B4: 20 34      JR      NZ,$77EA        
77B6: 30 00      JR      NC,$77B8        
77B8: 28 32      JR      Z,$77EC         
77BA: 30 10      JR      NC,$77CC        
77BC: 00         NOP                     
77BD: 38 10      JR      C,$77CF         
77BF: 10 08      STOP    $08             
77C1: 3A         LD      A,(HLD)         
77C2: 10 10      STOP    $10             
77C4: 10 3C      STOP    $3C             
77C6: 10 10      STOP    $10             
77C8: 18 3C      JR      $7806           
77CA: 30 10      JR      NC,$77DC        
77CC: 20 3A      JR      NZ,$7808        
77CE: 30 10      JR      NC,$77E0        
77D0: 28 38      JR      Z,$780A         
77D2: 30 20      JR      NC,$77F4        
77D4: 10 52      STOP    $52             
77D6: 10 20      STOP    $20             
77D8: 18 62      JR      $783C           
77DA: 10 30      STOP    $30             
77DC: 10 52      STOP    $52             
77DE: 10 30      STOP    $30             
77E0: 18 62      JR      $7844           
77E2: 10 40      STOP    $40             
77E4: 10 52      STOP    $52             
77E6: 10 40      STOP    $40             
77E8: 18 62      JR      $784C           
77EA: 10 50      STOP    $50             
77EC: 10 52      STOP    $52             
77EE: 10 50      STOP    $50             
77F0: 18 62      JR      $7854           
77F2: 10 60      STOP    $60             
77F4: 10 52      STOP    $52             
77F6: 10 60      STOP    $60             
77F8: 18 62      JR      $785C           
77FA: 10 70      STOP    $70             
77FC: 10 52      STOP    $52             
77FE: 10 70      STOP    $70             
7800: 18 62      JR      $7864           
7802: 10 80      STOP    $80             
7804: 10 52      STOP    $52             
7806: 10 80      STOP    $80             
7808: 18 62      JR      $786C           
780A: 10 90      STOP    $90             
780C: 10 52      STOP    $52             
780E: 10 90      STOP    $90             
7810: 18 62      JR      $7874           
7812: 10 A0      STOP    $A0             
7814: 10 52      STOP    $52             
7816: 10 A0      STOP    $A0             
7818: 18 62      JR      $787C           
781A: 10 B0      STOP    $B0             
781C: 10 52      STOP    $52             
781E: 10 B0      STOP    $B0             
7820: 18 62      JR      $7884           
7822: 10 00      STOP    $00             
7824: 00         NOP                     
7825: 42         LD      B,D             
7826: 10 00      STOP    $00             
7828: 08 44 10   LD      ($1044),SP      
782B: 00         NOP                     
782C: 10 46      STOP    $46             
782E: 10 00      STOP    $00             
7830: 18 46      JR      $7878           
7832: 30 00      JR      NC,$7834        
7834: 20 44      JR      NZ,$787A        
7836: 30 00      JR      NC,$7838        
7838: 28 42      JR      Z,$787C         
783A: 30 10      JR      NC,$784C        
783C: 00         NOP                     
783D: 48         LD      C,B             
783E: 10 10      STOP    $10             
7840: 08 4A 10   LD      ($104A),SP      
7843: 10 10      STOP    $10             
7845: 4C         LD      C,H             
7846: 10 10      STOP    $10             
7848: 18 4C      JR      $7896           
784A: 30 10      JR      NC,$785C        
784C: 20 4A      JR      NZ,$7898        
784E: 30 10      JR      NC,$7860        
7850: 28 08      JR      Z,$785A         
7852: 30 20      JR      NC,$7874        
7854: 10 56      STOP    $56             
7856: 10 20      STOP    $20             
7858: 18 66      JR      $78C0           
785A: 10 30      STOP    $30             
785C: 10 56      STOP    $56             
785E: 10 30      STOP    $30             
7860: 18 66      JR      $78C8           
7862: 10 40      STOP    $40             
7864: 10 56      STOP    $56             
7866: 10 40      STOP    $40             
7868: 18 66      JR      $78D0           
786A: 10 50      STOP    $50             
786C: 10 56      STOP    $56             
786E: 10 50      STOP    $50             
7870: 18 66      JR      $78D8           
7872: 10 60      STOP    $60             
7874: 10 56      STOP    $56             
7876: 10 60      STOP    $60             
7878: 18 66      JR      $78E0           
787A: 10 70      STOP    $70             
787C: 10 56      STOP    $56             
787E: 10 70      STOP    $70             
7880: 18 66      JR      $78E8           
7882: 10 80      STOP    $80             
7884: 10 56      STOP    $56             
7886: 10 80      STOP    $80             
7888: 18 66      JR      $78F0           
788A: 10 90      STOP    $90             
788C: 10 56      STOP    $56             
788E: 10 90      STOP    $90             
7890: 18 66      JR      $78F8           
7892: 10 A0      STOP    $A0             
7894: 10 56      STOP    $56             
7896: 10 A0      STOP    $A0             
7898: 18 66      JR      $7900           
789A: 10 B0      STOP    $B0             
789C: 10 56      STOP    $56             
789E: 10 B0      STOP    $B0             
78A0: 18 66      JR      $7908           
78A2: 10 70      STOP    $70             
78A4: 68         LD      L,B             
78A5: 60         LD      H,B             
78A6: 58         LD      E,B             
78A7: 50         LD      D,B             
78A8: 48         LD      C,B             
78A9: 40         LD      B,B             
78AA: 38 30      JR      C,$78DC         
78AC: 30 30      JR      NC,$78DE        
78AE: 30 30      JR      NC,$78E0        
78B0: 30 80      JR      NC,$7832        
78B2: 78         LD      A,B             
78B3: C5         PUSH    BC              
78B4: F0 EC      LD      A,($EC)         
78B6: CB 37      SET     1,E             
78B8: E6 0F      AND     $0F             
78BA: 5F         LD      E,A             
78BB: 50         LD      D,B             
78BC: 21 A3 78   LD      HL,$78A3        
78BF: 19         ADD     HL,DE           
78C0: 46         LD      B,(HL)          
78C1: 21 23 76   LD      HL,$7623        
78C4: F0 F1      LD      A,($F1)         
78C6: FE 05      CP      $05             
78C8: 28 40      JR      Z,$790A         
78CA: A7         AND     A               
78CB: 28 15      JR      Z,$78E2         
78CD: 21 A3 76   LD      HL,$76A3        
78D0: 3D         DEC     A               
78D1: 28 0F      JR      Z,$78E2         
78D3: 21 23 77   LD      HL,$7723        
78D6: 3D         DEC     A               
78D7: 28 09      JR      Z,$78E2         
78D9: 21 A3 77   LD      HL,$77A3        
78DC: 3D         DEC     A               
78DD: 28 03      JR      Z,$78E2         
78DF: 21 23 78   LD      HL,$7823        
78E2: 11 0C C0   LD      DE,$C00C        
78E5: 0E 00      LD      C,$00           
78E7: 79         LD      A,C             
78E8: E6 03      AND     $03             
78EA: FE 00      CP      $00             
78EC: 20 04      JR      NZ,$78F2        
78EE: F0 EC      LD      A,($EC)         
78F0: 18 0C      JR      $78FE           
78F2: FE 01      CP      $01             
78F4: 20 0B      JR      NZ,$7901        
78F6: E5         PUSH    HL              
78F7: 21 55 C1   LD      HL,$C155        
78FA: F0 EE      LD      A,($EE)         
78FC: 96         SUB     (HL)            
78FD: E1         POP     HL              
78FE: 86         ADD     A,(HL)          
78FF: 18 01      JR      $7902           
7901: 7E         LD      A,(HL)          
7902: 12         LD      (DE),A          
7903: 23         INC     HL              
7904: 13         INC     DE              
7905: 0C         INC     C               
7906: 79         LD      A,C             
7907: B8         CP      B               
7908: 20 DD      JR      NZ,$78E7        
790A: C1         POP     BC              
790B: C9         RET                     
790C: CD 38 79   CALL    $7938           
790F: C9         RET                     
7910: 20 40      JR      NZ,$7952        
7912: 60         LD      H,B             
7913: 78         LD      A,B             
7914: 10 48      STOP    $48             
7916: 68         LD      L,B             
7917: 90         SUB     B               
7918: 30 50      JR      NC,$796A        
791A: 80         ADD     A,B             
791B: 90         SUB     B               
791C: 18 38      JR      $7956           
791E: 68         LD      L,B             
791F: 78         LD      A,B             
7920: 28 08      JR      Z,$792A         
7922: 28 00      JR      Z,$7924         
7924: 48         LD      C,B             
7925: 40         LD      B,B             
7926: 4C         LD      C,H             
7927: 38 68      JR      C,$7991         
7929: 70         LD      (HL),B          
792A: 58         LD      E,B             
792B: 68         LD      L,B             
792C: 78         LD      A,B             
792D: 88         ADC     A,B             
792E: 98         SBC     B               
792F: 80         ADD     A,B             
7930: 1E 1E      LD      E,$1E           
7932: 1E 2E      LD      E,$2E           
7934: 2E 3E      LD      L,$3E           
7936: 2E 2E      LD      L,$2E           
7938: 11 90 C0   LD      DE,$C090        
793B: C5         PUSH    BC              
793C: F0 E7      LD      A,($E7)         
793E: E6 01      AND     $01             
7940: 4F         LD      C,A             
7941: 21 20 79   LD      HL,$7920        
7944: 09         ADD     HL,BC           
7945: F0 EC      LD      A,($EC)         
7947: 86         ADD     A,(HL)          
7948: FE 98      CP      $98             
794A: 38 02      JR      C,$794E         
794C: D6 88      SUB     $88             
794E: 12         LD      (DE),A          
794F: 13         INC     DE              
7950: 21 10 79   LD      HL,$7910        
7953: 09         ADD     HL,BC           
7954: 7E         LD      A,(HL)          
7955: 12         LD      (DE),A          
7956: 13         INC     DE              
7957: C5         PUSH    BC              
7958: F0 E7      LD      A,($E7)         
795A: 1F         RRA                     
795B: 1F         RRA                     
795C: 1F         RRA                     
795D: 1F         RRA                     
795E: 00         NOP                     
795F: A9         XOR     C               
7960: E6 07      AND     $07             
7962: 4F         LD      C,A             
7963: 06 00      LD      B,$00           
7965: 21 30 79   LD      HL,$7930        
7968: 09         ADD     HL,BC           
7969: 7E         LD      A,(HL)          
796A: 12         LD      (DE),A          
796B: 13         INC     DE              
796C: C1         POP     BC              
796D: 3E 90      LD      A,$90           
796F: 12         LD      (DE),A          
7970: 13         INC     DE              
7971: 0C         INC     C               
7972: 0C         INC     C               
7973: 79         LD      A,C             
7974: FE 10      CP      $10             
7976: 38 C9      JR      C,$7941         
7978: C1         POP     BC              
7979: C9         RET                     
797A: 00         NOP                     
797B: F8 58      LDHL    SP,$58          
797D: 00         NOP                     
797E: 00         NOP                     
797F: 00         NOP                     
7980: 68         LD      L,B             
7981: 00         NOP                     
7982: 00         NOP                     
7983: 08 68 20   LD      ($2068),SP      
7986: 00         NOP                     
7987: 10 58      STOP    $58             
7989: 20 00      JR      NZ,$798B        
798B: F8 5A      LDHL    SP,$5A          
798D: 00         NOP                     
798E: 00         NOP                     
798F: 00         NOP                     
7990: 6A         LD      L,D             
7991: 00         NOP                     
7992: 00         NOP                     
7993: 08 6A 20   LD      ($206A),SP      
7996: 00         NOP                     
7997: 10 5A      STOP    $5A             
7999: 20 00      JR      NZ,$799B        
799B: F8 5C      LDHL    SP,$5C          
799D: 00         NOP                     
799E: 00         NOP                     
799F: 00         NOP                     
79A0: 6C         LD      L,H             
79A1: 00         NOP                     
79A2: 00         NOP                     
79A3: 08 6C 20   LD      ($206C),SP      
79A6: 00         NOP                     
79A7: 10 5C      STOP    $5C             
79A9: 20 00      JR      NZ,$79AB        
79AB: F8 5E      LDHL    SP,$5E          
79AD: 00         NOP                     
79AE: 00         NOP                     
79AF: 00         NOP                     
79B0: 6E         LD      L,(HL)          
79B1: 00         NOP                     
79B2: 00         NOP                     
79B3: 08 6E 20   LD      ($206E),SP      
79B6: 00         NOP                     
79B7: 10 5E      STOP    $5E             
79B9: 20 3E      JR      NZ,$79F9        
79BB: 50         LD      D,B             
79BC: EA C0 C3   LD      ($C3C0),A       
79BF: 21 7A 79   LD      HL,$797A        
79C2: F0 F1      LD      A,($F1)         
79C4: 17         RLA                     
79C5: 17         RLA                     
79C6: 17         RLA                     
79C7: 17         RLA                     
79C8: E6 F0      AND     $F0             
79CA: 5F         LD      E,A             
79CB: 50         LD      D,B             
79CC: 19         ADD     HL,DE           
79CD: 0E 04      LD      C,$04           
79CF: CD 26 3D   CALL    $3D26           
79D2: 3E 04      LD      A,$04           
79D4: CD D0 3D   CALL    $3DD0           
79D7: F0 E7      LD      A,($E7)         
79D9: 1F         RRA                     
79DA: 1F         RRA                     
79DB: 1F         RRA                     
79DC: E6 03      AND     $03             
79DE: CD 87 3B   CALL    $3B87           
79E1: F0 F0      LD      A,($F0)         
79E3: C7         RST     0X00            
79E4: EC         ???                     
79E5: 79         LD      A,C             
79E6: 1A         LD      A,(DE)          
79E7: 7A         LD      A,D             
79E8: 44         LD      B,H             
79E9: 7A         LD      A,D             
79EA: 56         LD      D,(HL)          
79EB: 7A         LD      A,D             
79EC: CD 91 08   CALL    $0891           
79EF: 20 18      JR      NZ,$7A09        
79F1: CD BB 7B   CALL    $7BBB           
79F4: F0 E7      LD      A,($E7)         
79F6: E6 03      AND     $03             
79F8: 20 0F      JR      NZ,$7A09        
79FA: 21 50 C2   LD      HL,$C250        
79FD: 09         ADD     HL,BC           
79FE: 35         DEC     (HL)            
79FF: 20 08      JR      NZ,$7A09        
7A01: CD 91 08   CALL    $0891           
7A04: 36 80      LD      (HL),$80        
7A06: CD 8D 3B   CALL    $3B8D           
7A09: C9         RET                     
7A0A: 00         NOP                     
7A0B: 00         NOP                     
7A0C: 00         NOP                     
7A0D: 01 01 02   LD      BC,$0201        
7A10: 03         INC     BC              
7A11: 03         INC     BC              
7A12: 04         INC     B               
7A13: 04         INC     B               
7A14: 04         INC     B               
7A15: 03         INC     BC              
7A16: 03         INC     BC              
7A17: 02         LD      (BC),A          
7A18: 01 01 CD   LD      BC,$CD01        
7A1B: 91         SUB     C               
7A1C: 08 20 0D   LD      ($0D20),SP      
7A1F: 3E CF      LD      A,$CF           
7A21: CD 8F 7A   CALL    $7A8F           
7A24: 3E 19      LD      A,$19           
7A26: EA AB C5   LD      ($C5AB),A       
7A29: CD 8D 3B   CALL    $3B8D           
7A2C: 21 D0 C3   LD      HL,$C3D0        
7A2F: 09         ADD     HL,BC           
7A30: 7E         LD      A,(HL)          
7A31: 7E         LD      A,(HL)          
7A32: 34         INC     (HL)            
7A33: 1F         RRA                     
7A34: 1F         RRA                     
7A35: E6 0F      AND     $0F             
7A37: 5F         LD      E,A             
7A38: 50         LD      D,B             
7A39: 21 0A 7A   LD      HL,$7A0A        
7A3C: 19         ADD     HL,DE           
7A3D: 7E         LD      A,(HL)          
7A3E: 21 10 C3   LD      HL,$C310        
7A41: 09         ADD     HL,BC           
7A42: 77         LD      (HL),A          
7A43: C9         RET                     
7A44: CD 2C 7A   CALL    $7A2C           
7A47: FA 9F C1   LD      A,($C19F)       
7A4A: A7         AND     A               
7A4B: 20 08      JR      NZ,$7A55        
7A4D: CD 91 08   CALL    $0891           
7A50: 36 FF      LD      (HL),$FF        
7A52: CD 8D 3B   CALL    $3B8D           
7A55: C9         RET                     
7A56: CD 2C 7A   CALL    $7A2C           
7A59: CD 91 08   CALL    $0891           
7A5C: 20 09      JR      NZ,$7A67        
7A5E: CD 2B 4A   CALL    $4A2B           
7A61: 21 80 C2   LD      HL,$C280        
7A64: 09         ADD     HL,BC           
7A65: 70         LD      (HL),B          
7A66: C9         RET                     
7A67: FE E0      CP      $E0             
7A69: 30 23      JR      NC,$7A8E        
7A6B: FE DF      CP      $DF             
7A6D: 20 04      JR      NZ,$7A73        
7A6F: 3E 26      LD      A,$26           
7A71: E0 F2      LDFF00  ($F2),A         
7A73: 21 D0 C2   LD      HL,$C2D0        
7A76: 09         ADD     HL,BC           
7A77: 5E         LD      E,(HL)          
7A78: 7E         LD      A,(HL)          
7A79: FE FC      CP      $FC             
7A7B: 30 E1      JR      NC,$7A5E        
7A7D: C6 02      ADD     $02             
7A7F: 77         LD      (HL),A          
7A80: 21 40 C4   LD      HL,$C440        
7A83: 09         ADD     HL,BC           
7A84: 7E         LD      A,(HL)          
7A85: 83         ADD     A,E             
7A86: 77         LD      (HL),A          
7A87: 30 05      JR      NC,$7A8E        
7A89: 3E FF      LD      A,$FF           
7A8B: CD 87 3B   CALL    $3B87           
7A8E: C9         RET                     
7A8F: 5F         LD      E,A             
7A90: F0 99      LD      A,($99)         
7A92: F5         PUSH    AF              
7A93: 3E 10      LD      A,$10           
7A95: E0 99      LDFF00  ($99),A         
7A97: 7B         LD      A,E             
7A98: CD 97 21   CALL    $2197           
7A9B: F1         POP     AF              
7A9C: E0 99      LDFF00  ($99),A         
7A9E: C9         RET                     
7A9F: 00         NOP                     
7AA0: 00         NOP                     
7AA1: 02         LD      (BC),A          
7AA2: 00         NOP                     
7AA3: 02         LD      (BC),A          
7AA4: 20 00      JR      NZ,$7AA6        
7AA6: 20 44      JR      NZ,$7AEC        
7AA8: 00         NOP                     
7AA9: 46         LD      B,(HL)          
7AAA: 00         NOP                     
7AAB: 48         LD      C,B             
7AAC: 00         NOP                     
7AAD: 4A         LD      C,D             
7AAE: 00         NOP                     
7AAF: 4C         LD      C,H             
7AB0: 00         NOP                     
7AB1: 4C         LD      C,H             
7AB2: 20 D8      JR      NZ,$7A8C        
7AB4: 20 D6      JR      NZ,$7A8C        
7AB6: 20 D4      JR      NZ,$7A8C        
7AB8: 00         NOP                     
7AB9: D4 20 D6   CALL    NC,$D620        
7ABC: 00         NOP                     
7ABD: D8         RET     C               
7ABE: 00         NOP                     
7ABF: DA 00 DC   JP      C,$DC00         
7AC2: 00         NOP                     
7AC3: DE 00      SBC     $00             
7AC5: E0 00      LDFF00  ($00),A         
7AC7: E2         LDFF00  (C),A           
7AC8: 00         NOP                     
7AC9: E2         LDFF00  (C),A           
7ACA: 20 E0      JR      NZ,$7AAC        
7ACC: 20 DE      JR      NZ,$7AAC        
7ACE: 20 DC      JR      NZ,$7AAC        
7AD0: 20 DA      JR      NZ,$7AAC        
7AD2: 20 F0      JR      NZ,$7AC4        
7AD4: 9D         SBC     L               
7AD5: 17         RLA                     
7AD6: 17         RLA                     
7AD7: E6 FC      AND     $FC             
7AD9: 5F         LD      E,A             
7ADA: 16 00      LD      D,$00           
7ADC: 21 9F 7A   LD      HL,$7A9F        
7ADF: 19         ADD     HL,DE           
7AE0: E5         PUSH    HL              
7AE1: D1         POP     DE              
7AE2: 21 04 C0   LD      HL,$C004        
7AE5: F0 99      LD      A,($99)         
7AE7: 22         LD      (HLI),A         
7AE8: FA 55 C1   LD      A,($C155)       
7AEB: 4F         LD      C,A             
7AEC: F0 98      LD      A,($98)         
7AEE: 91         SUB     C               
7AEF: 22         LD      (HLI),A         
7AF0: 1A         LD      A,(DE)          
7AF1: 13         INC     DE              
7AF2: 22         LD      (HLI),A         
7AF3: 1A         LD      A,(DE)          
7AF4: 13         INC     DE              
7AF5: 22         LD      (HLI),A         
7AF6: F0 99      LD      A,($99)         
7AF8: 22         LD      (HLI),A         
7AF9: F0 98      LD      A,($98)         
7AFB: 91         SUB     C               
7AFC: C6 08      ADD     $08             
7AFE: 22         LD      (HLI),A         
7AFF: 1A         LD      A,(DE)          
7B00: 13         INC     DE              
7B01: 22         LD      (HLI),A         
7B02: 1A         LD      A,(DE)          
7B03: 77         LD      (HL),A          
7B04: C9         RET                     
7B05: 37         SCF                     
7B06: 7F         LD      A,A             
7B07: F0 E7      LD      A,($E7)         
7B09: E6 10      AND     $10             
7B0B: C0         RET     NZ              
7B0C: 1E 00      LD      E,$00           
7B0E: FA 9F C1   LD      A,($C19F)       
7B11: E6 80      AND     $80             
7B13: 28 01      JR      Z,$7B16         
7B15: 1C         INC     E               
7B16: 16 00      LD      D,$00           
7B18: FA 95 DB   LD      A,($DB95)       
7B1B: FE 01      CP      $01             
7B1D: 28 18      JR      Z,$7B37         
7B1F: 21 05 7B   LD      HL,$7B05        
7B22: 19         ADD     HL,DE           
7B23: 7E         LD      A,(HL)          
7B24: EA 18 C0   LD      ($C018),A       
7B27: 3E 97      LD      A,$97           
7B29: EA 19 C0   LD      ($C019),A       
7B2C: 3E A2      LD      A,$A2           
7B2E: EA 1A C0   LD      ($C01A),A       
7B31: 3E 40      LD      A,$40           
7B33: EA 1B C0   LD      ($C01B),A       
7B36: C9         RET                     
7B37: 21 05 7B   LD      HL,$7B05        
7B3A: 19         ADD     HL,DE           
7B3B: 7E         LD      A,(HL)          
7B3C: 21 97 FF   LD      HL,$FF97        
7B3F: 96         SUB     (HL)            
7B40: EA 00 C0   LD      ($C000),A       
7B43: 3E 97      LD      A,$97           
7B45: EA 01 C0   LD      ($C001),A       
7B48: 3E FE      LD      A,$FE           
7B4A: EA 02 C0   LD      ($C002),A       
7B4D: 3E 40      LD      A,$40           
7B4F: EA 03 C0   LD      ($C003),A       
7B52: C9         RET                     
7B53: 30 78      JR      NC,$7BCD        
7B55: 30 58      JR      NC,$7BAF        
7B57: 1E 00      LD      E,$00           
7B59: FA 9F C1   LD      A,($C19F)       
7B5C: E6 80      AND     $80             
7B5E: 28 01      JR      Z,$7B61         
7B60: 1C         INC     E               
7B61: 16 00      LD      D,$00           
7B63: FA 95 DB   LD      A,($DB95)       
7B66: FE 01      CP      $01             
7B68: 28 25      JR      Z,$7B8F         
7B6A: 21 53 7B   LD      HL,$7B53        
7B6D: 19         ADD     HL,DE           
7B6E: 7E         LD      A,(HL)          
7B6F: EA 18 C0   LD      ($C018),A       
7B72: 1E 00      LD      E,$00           
7B74: FA 77 C1   LD      A,($C177)       
7B77: E6 01      AND     $01             
7B79: 28 01      JR      Z,$7B7C         
7B7B: 1C         INC     E               
7B7C: 21 55 7B   LD      HL,$7B55        
7B7F: 19         ADD     HL,DE           
7B80: 7E         LD      A,(HL)          
7B81: EA 19 C0   LD      ($C019),A       
7B84: 3E 3E      LD      A,$3E           
7B86: EA 1A C0   LD      ($C01A),A       
7B89: 3E 00      LD      A,$00           
7B8B: EA 1B C0   LD      ($C01B),A       
7B8E: C9         RET                     
7B8F: 21 53 7B   LD      HL,$7B53        
7B92: 19         ADD     HL,DE           
7B93: 7E         LD      A,(HL)          
7B94: 21 97 FF   LD      HL,$FF97        
7B97: 96         SUB     (HL)            
7B98: EA 00 C0   LD      ($C000),A       
7B9B: 1E 00      LD      E,$00           
7B9D: FA 77 C1   LD      A,($C177)       
7BA0: E6 01      AND     $01             
7BA2: 28 01      JR      Z,$7BA5         
7BA4: 1C         INC     E               
7BA5: 21 55 7B   LD      HL,$7B55        
7BA8: 19         ADD     HL,DE           
7BA9: 7E         LD      A,(HL)          
7BAA: EA 01 C0   LD      ($C001),A       
7BAD: 3E 9E      LD      A,$9E           
7BAF: EA 02 C0   LD      ($C002),A       
7BB2: 3E 00      LD      A,$00           
7BB4: EA 03 C0   LD      ($C003),A       
7BB7: C9         RET                     
7BB8: CD C5 7B   CALL    $7BC5           
7BBB: C5         PUSH    BC              
7BBC: 79         LD      A,C             
7BBD: C6 10      ADD     $10             
7BBF: 4F         LD      C,A             
7BC0: CD C5 7B   CALL    $7BC5           
7BC3: C1         POP     BC              
7BC4: C9         RET                     
7BC5: 21 40 C2   LD      HL,$C240        
7BC8: 09         ADD     HL,BC           
7BC9: 7E         LD      A,(HL)          
7BCA: A7         AND     A               
7BCB: 28 23      JR      Z,$7BF0         
7BCD: F5         PUSH    AF              
7BCE: CB 37      SET     1,E             
7BD0: E6 F0      AND     $F0             
7BD2: 21 60 C2   LD      HL,$C260        
7BD5: 09         ADD     HL,BC           
7BD6: 86         ADD     A,(HL)          
7BD7: 77         LD      (HL),A          
7BD8: CB 12      SET     1,E             
7BDA: 21 00 C2   LD      HL,$C200        
7BDD: 09         ADD     HL,BC           
7BDE: F1         POP     AF              
7BDF: 1E 00      LD      E,$00           
7BE1: CB 7F      SET     1,E             
7BE3: 28 02      JR      Z,$7BE7         
7BE5: 1E F0      LD      E,$F0           
7BE7: CB 37      SET     1,E             
7BE9: E6 0F      AND     $0F             
7BEB: B3         OR      E               
7BEC: CB 1A      SET     1,E             
7BEE: 8E         ADC     A,(HL)          
7BEF: 77         LD      (HL),A          
7BF0: C9         RET                     
7BF1: 21 20 C3   LD      HL,$C320        
7BF4: 09         ADD     HL,BC           
7BF5: 7E         LD      A,(HL)          
7BF6: A7         AND     A               
7BF7: 28 F7      JR      Z,$7BF0         
7BF9: F5         PUSH    AF              
7BFA: CB 37      SET     1,E             
7BFC: E6 F0      AND     $F0             
7BFE: 21 30 C3   LD      HL,$C330        
7C01: 09         ADD     HL,BC           
7C02: 86         ADD     A,(HL)          
7C03: 77         LD      (HL),A          
7C04: CB 12      SET     1,E             
7C06: 21 10 C3   LD      HL,$C310        
7C09: 18 D2      JR      $7BDD           
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
