![Bank 16](GBZelda.jpg)

# Bank 16

>>> cpu Z80GB

>>> binary 4000:zelda.gb[58000:5C000]

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

```code
4000: 20 51      JR           NZ,$4053
4002: 27         DAA
4003: 51         LD           D,C
4004: 2C         INC         L
4005: 51         LD           D,C
4006: 2F         CPL
4007: 51         LD           D,C
4008: 32         LD           (HLD),A
4009: 51         LD           D,C
400A: 35         DEC         (HL)
400B: 51         LD           D,C
400C: 38 51      JR           C,$405F
400E: 3D         DEC         A
400F: 51         LD           D,C
4010: 3E 51      LD           A,$51
4012: 43         LD           B,E
4013: 51         LD           D,C
4014: 44         LD           B,H
4015: 51         LD           D,C
4016: 49         LD           C,C
4017: 51         LD           D,C
4018: 4E         LD           C,(HL)
4019: 51         LD           D,C
401A: 53         LD           D,E
401B: 51         LD           D,C
401C: 56         LD           D,(HL)
401D: 51         LD           D,C
401E: 57         LD           D,A
401F: 51         LD           D,C
4020: 5C         LD           E,H
4021: 51         LD           D,C
4022: 63         LD           H,E
4023: 51         LD           D,C
4024: 66         LD           H,(HL)
4025: 51         LD           D,C
4026: 6D         LD           L,L
4027: 51         LD           D,C
4028: 72         LD           (HL),D
4029: 51         LD           D,C
402A: 77         LD           (HL),A
402B: 51         LD           D,C
402C: 7A         LD           A,D
402D: 51         LD           D,C
402E: 7D         LD           A,L
402F: 51         LD           D,C
4030: 80         ADD         A,B
4031: 51         LD           D,C
4032: 81         ADD         A,C
4033: 51         LD           D,C
4034: 84         ADD         A,H
4035: 51         LD           D,C
4036: 85         ADD         A,L
4037: 51         LD           D,C
4038: 86         ADD         A,(HL)
4039: 51         LD           D,C
403A: 87         ADD         A,A
403B: 51         LD           D,C
403C: 8A         ADC         A,D
403D: 51         LD           D,C
403E: 8D         ADC         A,L
403F: 51         LD           D,C
4040: 90         SUB         B
4041: 51         LD           D,C
4042: 97         SUB         A
4043: 51         LD           D,C
4044: 9E         SBC         (HL)
4045: 51         LD           D,C
4046: A5         AND         L
4047: 51         LD           D,C
4048: AA         XOR         D
4049: 51         LD           D,C
404A: B5         OR           L
404B: 51         LD           D,C
404C: BA         CP           D
404D: 51         LD           D,C
404E: BB         CP           E
404F: 51         LD           D,C
4050: BC         CP           H
4051: 51         LD           D,C
4052: C1         POP         BC
4053: 51         LD           D,C
4054: C4 51 C9   CALL       NZ,$C951
4057: 51         LD           D,C
4058: CA 51 CF   JP           Z,$CF51
405B: 51         LD           D,C
405C: D2 51 D5   JP           NC,$D551
405F: 51         LD           D,C
4060: DA 51 DD   JP           C,$DD51
4063: 51         LD           D,C
4064: E4                              
4065: 51         LD           D,C
4066: E7         RST         0X20
4067: 51         LD           D,C
4068: EE 51      XOR         $51
406A: F1         POP         AF
406B: 51         LD           D,C
406C: F2                              
406D: 51         LD           D,C
406E: F5         PUSH       AF
406F: 51         LD           D,C
4070: F8 51      LDHL       SP,$51
4072: FB         EI
4073: 51         LD           D,C
4074: 00         NOP
4075: 52         LD           D,D
4076: 05         DEC         B
4077: 52         LD           D,D
4078: 08 52 0D   LD           ($0D52),SP
407B: 52         LD           D,D
407C: 10 52      STOP       $52
407E: 15         DEC         D
407F: 52         LD           D,D
4080: 18 52      JR           $40D4
4082: 1D         DEC         E
4083: 52         LD           D,D
4084: 20 52      JR           NZ,$40D8
4086: 27         DAA
4087: 52         LD           D,D
4088: 2C         INC         L
4089: 52         LD           D,D
408A: 2F         CPL
408B: 52         LD           D,D
408C: 30 52      JR           NC,$40E0
408E: 35         DEC         (HL)
408F: 52         LD           D,D
4090: 3A         LD           A,(HLD)
4091: 52         LD           D,D
4092: 3D         DEC         A
4093: 52         LD           D,D
4094: 3E 52      LD           A,$52
4096: 41         LD           B,C
4097: 52         LD           D,D
4098: 42         LD           B,D
4099: 52         LD           D,D
409A: 45         LD           B,L
409B: 52         LD           D,D
409C: 48         LD           C,B
409D: 52         LD           D,D
409E: 4B         LD           C,E
409F: 52         LD           D,D
40A0: 52         LD           D,D
40A1: 52         LD           D,D
40A2: 55         LD           D,L
40A3: 52         LD           D,D
40A4: 58         LD           E,B
40A5: 52         LD           D,D
40A6: 5D         LD           E,L
40A7: 52         LD           D,D
40A8: 60         LD           H,B
40A9: 52         LD           D,D
40AA: 65         LD           H,L
40AB: 52         LD           D,D
40AC: 66         LD           H,(HL)
40AD: 52         LD           D,D
40AE: 6B         LD           L,E
40AF: 52         LD           D,D
40B0: 70         LD           (HL),B
40B1: 52         LD           D,D
40B2: 75         LD           (HL),L
40B3: 52         LD           D,D
40B4: 76         HALT
40B5: 52         LD           D,D
40B6: 79         LD           A,C
40B7: 52         LD           D,D
40B8: 7A         LD           A,D
40B9: 52         LD           D,D
40BA: 81         ADD         A,C
40BB: 52         LD           D,D
40BC: 86         ADD         A,(HL)
40BD: 52         LD           D,D
40BE: 8B         ADC         A,E
40BF: 52         LD           D,D
40C0: 90         SUB         B
40C1: 52         LD           D,D
40C2: 95         SUB         L
40C3: 52         LD           D,D
40C4: 9A         SBC         D
40C5: 52         LD           D,D
40C6: 9D         SBC         L
40C7: 52         LD           D,D
40C8: A0         AND         B
40C9: 52         LD           D,D
40CA: A5         AND         L
40CB: 52         LD           D,D
40CC: A8         XOR         B
40CD: 52         LD           D,D
40CE: B1         OR           C
40CF: 52         LD           D,D
40D0: BA         CP           D
40D1: 52         LD           D,D
40D2: BD         CP           L
40D3: 52         LD           D,D
40D4: BE         CP           (HL)
40D5: 52         LD           D,D
40D6: C5         PUSH       BC
40D7: 52         LD           D,D
40D8: C6 52      ADD         $52
40DA: C9         RET
40DB: 52         LD           D,D
40DC: D2 52 D5   JP           NC,$D552
40DF: 52         LD           D,D
40E0: E0 52      LDFF00   ($52),A
40E2: E5         PUSH       HL
40E3: 52         LD           D,D
40E4: EC                              
40E5: 52         LD           D,D
40E6: F3         DI
40E7: 52         LD           D,D
40E8: FA 52 FF   LD           A,($FF52)
40EB: 52         LD           D,D
40EC: 02         LD           (BC),A
40ED: 53         LD           D,E
40EE: 0D         DEC         C
40EF: 53         LD           D,E
40F0: 16 53      LD           D,$53
40F2: 17         RLA
40F3: 53         LD           D,E
40F4: 18 53      JR           $4149
40F6: 19         ADD         HL,DE
40F7: 53         LD           D,E
40F8: 1E 53      LD           E,$53
40FA: 25         DEC         H
40FB: 53         LD           D,E
40FC: 2A         LD           A,(HLI)
40FD: 53         LD           D,E
40FE: 31 53 3A   LD           SP,$3A53
4101: 53         LD           D,E
4102: 3D         DEC         A
4103: 53         LD           D,E
4104: 40         LD           B,B
4105: 53         LD           D,E
4106: 47         LD           B,A
4107: 53         LD           D,E
4108: 4E         LD           C,(HL)
4109: 53         LD           D,E
410A: 53         LD           D,E
410B: 53         LD           D,E
410C: 54         LD           D,H
410D: 53         LD           D,E
410E: 5B         LD           E,E
410F: 53         LD           D,E
4110: 60         LD           H,B
4111: 53         LD           D,E
4112: 65         LD           H,L
4113: 53         LD           D,E
4114: 6A         LD           L,D
4115: 53         LD           D,E
4116: 73         LD           (HL),E
4117: 53         LD           D,E
4118: 78         LD           A,B
4119: 53         LD           D,E
411A: 79         LD           A,C
411B: 53         LD           D,E
411C: 7A         LD           A,D
411D: 53         LD           D,E
411E: 7F         LD           A,A
411F: 53         LD           D,E
4120: 82         ADD         A,D
4121: 53         LD           D,E
4122: 83         ADD         A,E
4123: 53         LD           D,E
4124: 8C         ADC         A,H
4125: 53         LD           D,E
4126: 9B         SBC         E
4127: 53         LD           D,E
4128: A0         AND         B
4129: 53         LD           D,E
412A: A1         AND         C
412B: 53         LD           D,E
412C: A8         XOR         B
412D: 53         LD           D,E
412E: AD         XOR         L
412F: 53         LD           D,E
4130: B0         OR           B
4131: 53         LD           D,E
4132: B7         OR           A
4133: 53         LD           D,E
4134: BC         CP           H
4135: 53         LD           D,E
4136: C3 53 C8   JP           $C853
4139: 53         LD           D,E
413A: CB 53      BIT         1,E
413C: D2 53 D7   JP           NC,$D753
413F: 53         LD           D,E
4140: DC 53 E9   CALL       C,$E953
4143: 53         LD           D,E
4144: F2                              
4145: 53         LD           D,E
4146: F7         RST         0X30
4147: 53         LD           D,E
4148: 00         NOP
4149: 54         LD           D,H
414A: 07         RLCA
414B: 54         LD           D,H
414C: 0E 54      LD           C,$54
414E: 11 54 12   LD           DE,$1254
4151: 54         LD           D,H
4152: 19         ADD         HL,DE
4153: 54         LD           D,H
4154: 20 54      JR           NZ,$41AA
4156: 21 54 28   LD           HL,$2854
4159: 54         LD           D,H
415A: 2F         CPL
415B: 54         LD           D,H
415C: 3C         INC         A
415D: 54         LD           D,H
415E: 45         LD           B,L
415F: 54         LD           D,H
4160: 46         LD           B,(HL)
4161: 54         LD           D,H
4162: 4F         LD           C,A
4163: 54         LD           D,H
4164: 54         LD           D,H
4165: 54         LD           D,H
4166: 59         LD           E,C
4167: 54         LD           D,H
4168: 64         LD           H,H
4169: 54         LD           D,H
416A: 69         LD           L,C
416B: 54         LD           D,H
416C: 6A         LD           L,D
416D: 54         LD           D,H
416E: 6D         LD           L,L
416F: 54         LD           D,H
4170: 6E         LD           L,(HL)
4171: 54         LD           D,H
4172: 73         LD           (HL),E
4173: 54         LD           D,H
4174: 7C         LD           A,H
4175: 54         LD           D,H
4176: 81         ADD         A,C
4177: 54         LD           D,H
4178: 86         ADD         A,(HL)
4179: 54         LD           D,H
417A: 91         SUB         C
417B: 54         LD           D,H
417C: 9E         SBC         (HL)
417D: 54         LD           D,H
417E: AB         XOR         E
417F: 54         LD           D,H
4180: B6         OR           (HL)
4181: 54         LD           D,H
4182: B7         OR           A
4183: 54         LD           D,H
4184: BC         CP           H
4185: 54         LD           D,H
4186: C3 54 CA   JP           $CA54
4189: 54         LD           D,H
418A: D3                              
418B: 54         LD           D,H
418C: DA 54 DD   JP           C,$DD54
418F: 54         LD           D,H
4190: DE 54      SBC         $54
4192: E3                              
4193: 54         LD           D,H
4194: E6 54      AND         $54
4196: ED                              
4197: 54         LD           D,H
4198: F4                              
4199: 54         LD           D,H
419A: FD                              
419B: 54         LD           D,H
419C: 06 55      LD           B,$55
419E: 0B         DEC         BC
419F: 55         LD           D,L
41A0: 10 55      STOP       $55
41A2: 13         INC         DE
41A3: 55         LD           D,L
41A4: 18 55      JR           $41FB
41A6: 1D         DEC         E
41A7: 55         LD           D,L
41A8: 1E 55      LD           E,$55
41AA: 25         DEC         H
41AB: 55         LD           D,L
41AC: 30 55      JR           NC,$4203
41AE: 31 55 32   LD           SP,$3255
41B1: 55         LD           D,L
41B2: 37         SCF
41B3: 55         LD           D,L
41B4: 3C         INC         A
41B5: 55         LD           D,L
41B6: 43         LD           B,E
41B7: 55         LD           D,L
41B8: 4A         LD           C,D
41B9: 55         LD           D,L
41BA: 59         LD           E,C
41BB: 55         LD           D,L
41BC: 62         LD           H,D
41BD: 55         LD           D,L
41BE: 69         LD           L,C
41BF: 55         LD           D,L
41C0: 74         LD           (HL),H
41C1: 55         LD           D,L
41C2: 79         LD           A,C
41C3: 55         LD           D,L
41C4: 80         ADD         A,B
41C5: 55         LD           D,L
41C6: 89         ADC         A,C
41C7: 55         LD           D,L
41C8: 92         SUB         D
41C9: 55         LD           D,L
41CA: 95         SUB         L
41CB: 55         LD           D,L
41CC: 96         SUB         (HL)
41CD: 55         LD           D,L
41CE: 97         SUB         A
41CF: 55         LD           D,L
41D0: 9A         SBC         D
41D1: 55         LD           D,L
41D2: 9F         SBC         A
41D3: 55         LD           D,L
41D4: A4         AND         H
41D5: 55         LD           D,L
41D6: A9         XOR         C
41D7: 55         LD           D,L
41D8: B0         OR           B
41D9: 55         LD           D,L
41DA: B3         OR           E
41DB: 55         LD           D,L
41DC: B4         OR           H
41DD: 55         LD           D,L
41DE: B7         OR           A
41DF: 55         LD           D,L
41E0: BC         CP           H
41E1: 55         LD           D,L
41E2: C3 55 CA   JP           $CA55
41E5: 55         LD           D,L
41E6: D1         POP         DE
41E7: 55         LD           D,L
41E8: D6 55      SUB         $55
41EA: DD                              
41EB: 55         LD           D,L
41EC: E0 55      LDFF00   ($55),A
41EE: E1         POP         HL
41EF: 55         LD           D,L
41F0: E2         LDFF00   (C),A
41F1: 55         LD           D,L
41F2: E7         RST         0X20
41F3: 55         LD           D,L
41F4: E8 55      ADD         SP,$55
41F6: ED                              
41F7: 55         LD           D,L
41F8: F2                              
41F9: 55         LD           D,L
41FA: F3         DI
41FB: 55         LD           D,L
41FC: F6 55      OR           $55
41FE: F7         RST         0X30
41FF: 55         LD           D,L
4200: 00         NOP
4201: 46         LD           B,(HL)
4202: 01 46 02   LD           BC,$0246
4205: 46         LD           B,(HL)
4206: 05         DEC         B
4207: 46         LD           B,(HL)
4208: 0C         INC         C
4209: 46         LD           B,(HL)
420A: 0F         RRCA
420B: 46         LD           B,(HL)
420C: 18 46      JR           $4254
420E: 1B         DEC         DE
420F: 46         LD           B,(HL)
4210: 20 46      JR           NZ,$4258
4212: 21 46 24   LD           HL,$2446
4215: 46         LD           B,(HL)
4216: 2D         DEC         L
4217: 46         LD           B,(HL)
4218: 36 46      LD           (HL),$46
421A: 37         SCF
421B: 46         LD           B,(HL)
421C: 3A         LD           A,(HLD)
421D: 46         LD           B,(HL)
421E: 41         LD           B,C
421F: 46         LD           B,(HL)
4220: 48         LD           C,B
4221: 46         LD           B,(HL)
4222: 4F         LD           C,A
4223: 46         LD           B,(HL)
4224: 56         LD           D,(HL)
4225: 46         LD           B,(HL)
4226: 5F         LD           E,A
4227: 46         LD           B,(HL)
4228: 66         LD           H,(HL)
4229: 46         LD           B,(HL)
422A: 6F         LD           L,A
422B: 46         LD           B,(HL)
422C: 7C         LD           A,H
422D: 46         LD           B,(HL)
422E: 81         ADD         A,C
422F: 46         LD           B,(HL)
4230: 84         ADD         A,H
4231: 46         LD           B,(HL)
4232: 87         ADD         A,A
4233: 46         LD           B,(HL)
4234: 8C         ADC         A,H
4235: 46         LD           B,(HL)
4236: 8D         ADC         A,L
4237: 46         LD           B,(HL)
4238: 8E         ADC         A,(HL)
4239: 46         LD           B,(HL)
423A: 91         SUB         C
423B: 46         LD           B,(HL)
423C: 96         SUB         (HL)
423D: 46         LD           B,(HL)
423E: 99         SBC         C
423F: 46         LD           B,(HL)
4240: 9C         SBC         H
4241: 46         LD           B,(HL)
4242: A1         AND         C
4243: 46         LD           B,(HL)
4244: AE         XOR         (HL)
4245: 46         LD           B,(HL)
4246: B9         CP           C
4247: 46         LD           B,(HL)
4248: C0         RET         NZ
4249: 46         LD           B,(HL)
424A: CD 46 D8   CALL       $D846
424D: 46         LD           B,(HL)
424E: E1         POP         HL
424F: 46         LD           B,(HL)
4250: E8 46      ADD         SP,$46
4252: ED                              
4253: 46         LD           B,(HL)
4254: F8 46      LDHL       SP,$46
4256: FB         EI
4257: 46         LD           B,(HL)
4258: FE 46      CP           $46
425A: 05         DEC         B
425B: 47         LD           B,A
425C: 06 47      LD           B,$47
425E: 09         ADD         HL,BC
425F: 47         LD           B,A
4260: 14         INC         D
4261: 47         LD           B,A
4262: 21 47 24   LD           HL,$2447
4265: 47         LD           B,A
4266: 29         ADD         HL,HL
4267: 47         LD           B,A
4268: 2E 47      LD           L,$47
426A: 35         DEC         (HL)
426B: 47         LD           B,A
426C: 3A         LD           A,(HLD)
426D: 47         LD           B,A
426E: 45         LD           B,L
426F: 47         LD           B,A
4270: 4C         LD           C,H
4271: 47         LD           B,A
4272: 51         LD           D,C
4273: 47         LD           B,A
4274: 5A         LD           E,D
4275: 47         LD           B,A
4276: 5F         LD           E,A
4277: 47         LD           B,A
4278: 66         LD           H,(HL)
4279: 47         LD           B,A
427A: 6D         LD           L,L
427B: 47         LD           B,A
427C: 72         LD           (HL),D
427D: 47         LD           B,A
427E: 75         LD           (HL),L
427F: 47         LD           B,A
4280: 78         LD           A,B
4281: 47         LD           B,A
4282: 81         ADD         A,C
4283: 47         LD           B,A
4284: 8A         ADC         A,D
4285: 47         LD           B,A
4286: 93         SUB         E
4287: 47         LD           B,A
4288: 9E         SBC         (HL)
4289: 47         LD           B,A
428A: A5         AND         L
428B: 47         LD           B,A
428C: AC         XOR         H
428D: 47         LD           B,A
428E: AF         XOR         A
428F: 47         LD           B,A
4290: B6         OR           (HL)
4291: 47         LD           B,A
4292: BF         CP           A
4293: 47         LD           B,A
4294: CA 47 D3   JP           Z,$D347
4297: 47         LD           B,A
4298: DC 47 E5   CALL       C,$E547
429B: 47         LD           B,A
429C: F0 47      LD           A,($47)
429E: F7         RST         0X30
429F: 47         LD           B,A
42A0: 00         NOP
42A1: 48         LD           C,B
42A2: 07         RLCA
42A3: 48         LD           C,B
42A4: 10 48      STOP       $48
42A6: 13         INC         DE
42A7: 48         LD           C,B
42A8: 16 48      LD           D,$48
42AA: 21 48 2C   LD           HL,$2C48
42AD: 48         LD           C,B
42AE: 37         SCF
42AF: 48         LD           C,B
42B0: 3E 48      LD           A,$48
42B2: 4D         LD           C,L
42B3: 48         LD           C,B
42B4: 50         LD           D,B
42B5: 48         LD           C,B
42B6: 53         LD           D,E
42B7: 48         LD           C,B
42B8: 5E         LD           E,(HL)
42B9: 48         LD           C,B
42BA: 67         LD           H,A
42BB: 48         LD           C,B
42BC: 68         LD           L,B
42BD: 48         LD           C,B
42BE: 6D         LD           L,L
42BF: 48         LD           C,B
42C0: 72         LD           (HL),D
42C1: 48         LD           C,B
42C2: 7B         LD           A,E
42C3: 48         LD           C,B
42C4: 88         ADC         A,B
42C5: 48         LD           C,B
42C6: 8B         ADC         A,E
42C7: 48         LD           C,B
42C8: 96         SUB         (HL)
42C9: 48         LD           C,B
42CA: 9B         SBC         E
42CB: 48         LD           C,B
42CC: A4         AND         H
42CD: 48         LD           C,B
42CE: A5         AND         L
42CF: 48         LD           C,B
42D0: AE         XOR         (HL)
42D1: 48         LD           C,B
42D2: B9         CP           C
42D3: 48         LD           C,B
42D4: C2 48 CB   JP           NZ,$CB48
42D7: 48         LD           C,B
42D8: D6 48      SUB         $48
42DA: DF         RST         0X18
42DB: 48         LD           C,B
42DC: E8 48      ADD         SP,$48
42DE: EF         RST         0X28
42DF: 48         LD           C,B
42E0: FA 48 FF   LD           A,($FF48)
42E3: 48         LD           C,B
42E4: 0A         LD           A,(BC)
42E5: 49         LD           C,C
42E6: 11 49 18   LD           DE,$1849
42E9: 49         LD           C,C
42EA: 1F         RRA
42EB: 49         LD           C,C
42EC: 2A         LD           A,(HLI)
42ED: 49         LD           C,C
42EE: 33         INC         SP
42EF: 49         LD           C,C
42F0: 3A         LD           A,(HLD)
42F1: 49         LD           C,C
42F2: 43         LD           B,E
42F3: 49         LD           C,C
42F4: 4A         LD           C,D
42F5: 49         LD           C,C
42F6: 4D         LD           C,L
42F7: 49         LD           C,C
42F8: 56         LD           D,(HL)
42F9: 49         LD           C,C
42FA: 59         LD           E,C
42FB: 49         LD           C,C
42FC: 5C         LD           E,H
42FD: 49         LD           C,C
42FE: 5D         LD           E,L
42FF: 49         LD           C,C
4300: 5E         LD           E,(HL)
4301: 49         LD           C,C
4302: 61         LD           H,C
4303: 49         LD           C,C
4304: 6A         LD           L,D
4305: 49         LD           C,C
4306: 6D         LD           L,L
4307: 49         LD           C,C
4308: 76         HALT
4309: 49         LD           C,C
430A: 79         LD           A,C
430B: 49         LD           C,C
430C: 7C         LD           A,H
430D: 49         LD           C,C
430E: 7D         LD           A,L
430F: 49         LD           C,C
4310: 8A         ADC         A,D
4311: 49         LD           C,C
4312: 95         SUB         L
4313: 49         LD           C,C
4314: A4         AND         H
4315: 49         LD           C,C
4316: AF         XOR         A
4317: 49         LD           C,C
4318: B2         OR           D
4319: 49         LD           C,C
431A: B3         OR           E
431B: 49         LD           C,C
431C: BC         CP           H
431D: 49         LD           C,C
431E: C5         PUSH       BC
431F: 49         LD           C,C
4320: CE 49      ADC         $49
4322: DB                              
4323: 49         LD           C,C
4324: E0 49      LDFF00   ($49),A
4326: E3                              
4327: 49         LD           C,C
4328: EA 49 F5   LD           ($F549),A
432B: 49         LD           C,C
432C: F8 49      LDHL       SP,$49
432E: 05         DEC         B
432F: 4A         LD           C,D
4330: 10 4A      STOP       $4A
4332: 1D         DEC         E
4333: 4A         LD           C,D
4334: 28 4A      JR           Z,$4380
4336: 2F         CPL
4337: 4A         LD           C,D
4338: 38 4A      JR           C,$4384
433A: 45         LD           B,L
433B: 4A         LD           C,D
433C: 4C         LD           C,H
433D: 4A         LD           C,D
433E: 53         LD           D,E
433F: 4A         LD           C,D
4340: 5E         LD           E,(HL)
4341: 4A         LD           C,D
4342: 65         LD           H,L
4343: 4A         LD           C,D
4344: 68         LD           L,B
4345: 4A         LD           C,D
4346: 6F         LD           L,A
4347: 4A         LD           C,D
4348: 74         LD           (HL),H
4349: 4A         LD           C,D
434A: 77         LD           (HL),A
434B: 4A         LD           C,D
434C: 7C         LD           A,H
434D: 4A         LD           C,D
434E: 81         ADD         A,C
434F: 4A         LD           C,D
4350: 86         ADD         A,(HL)
4351: 4A         LD           C,D
4352: 8F         ADC         A,A
4353: 4A         LD           C,D
4354: 94         SUB         H
4355: 4A         LD           C,D
4356: 97         SUB         A
4357: 4A         LD           C,D
4358: 9A         SBC         D
4359: 4A         LD           C,D
435A: 9D         SBC         L
435B: 4A         LD           C,D
435C: 9E         SBC         (HL)
435D: 4A         LD           C,D
435E: 9F         SBC         A
435F: 4A         LD           C,D
4360: A0         AND         B
4361: 4A         LD           C,D
4362: A9         XOR         C
4363: 4A         LD           C,D
4364: B4         OR           H
4365: 4A         LD           C,D
4366: BD         CP           L
4367: 4A         LD           C,D
4368: C4 4A CB   CALL       NZ,$CB4A
436B: 4A         LD           C,D
436C: CE 4A      ADC         $4A
436E: D1         POP         DE
436F: 4A         LD           C,D
4370: DC 4A E9   CALL       C,$E94A
4373: 4A         LD           C,D
4374: EC                              
4375: 4A         LD           C,D
4376: F5         PUSH       AF
4377: 4A         LD           C,D
4378: 00         NOP
4379: 4B         LD           C,E
437A: 03         INC         BC
437B: 4B         LD           C,E
437C: 08 4B 13   LD           ($134B),SP
437F: 4B         LD           C,E
4380: 1C         INC         E
4381: 4B         LD           C,E
4382: 27         DAA
4383: 4B         LD           C,E
4384: 32         LD           (HLD),A
4385: 4B         LD           C,E
4386: 3D         DEC         A
4387: 4B         LD           C,E
4388: 40         LD           B,B
4389: 4B         LD           C,E
438A: 45         LD           B,L
438B: 4B         LD           C,E
438C: 4A         LD           C,D
438D: 4B         LD           C,E
438E: 4B         LD           C,E
438F: 4B         LD           C,E
4390: 50         LD           D,B
4391: 4B         LD           C,E
4392: 57         LD           D,A
4393: 4B         LD           C,E
4394: 5C         LD           E,H
4395: 4B         LD           C,E
4396: 67         LD           H,A
4397: 4B         LD           C,E
4398: 6C         LD           L,H
4399: 4B         LD           C,E
439A: 79         LD           A,C
439B: 4B         LD           C,E
439C: 86         ADD         A,(HL)
439D: 4B         LD           C,E
439E: 8D         ADC         A,L
439F: 4B         LD           C,E
43A0: 94         SUB         H
43A1: 4B         LD           C,E
43A2: 9D         SBC         L
43A3: 4B         LD           C,E
43A4: A8         XOR         B
43A5: 4B         LD           C,E
43A6: AF         XOR         A
43A7: 4B         LD           C,E
43A8: B6         OR           (HL)
43A9: 4B         LD           C,E
43AA: B9         CP           C
43AB: 4B         LD           C,E
43AC: C2 4B C5   JP           NZ,$C54B
43AF: 4B         LD           C,E
43B0: CE 4B      ADC         $4B
43B2: D5         PUSH       DE
43B3: 4B         LD           C,E
43B4: DA 4B DB   JP           C,$DB4B
43B7: 4B         LD           C,E
43B8: E2         LDFF00   (C),A
43B9: 4B         LD           C,E
43BA: EB                              
43BB: 4B         LD           C,E
43BC: F2                              
43BD: 4B         LD           C,E
43BE: F3         DI
43BF: 4B         LD           C,E
43C0: F4                              
43C1: 4B         LD           C,E
43C2: F4                              
43C3: 4B         LD           C,E
43C4: F4                              
43C5: 4B         LD           C,E
43C6: F7         RST         0X30
43C7: 4B         LD           C,E
43C8: FA 4B FD   LD           A,($FD4B)
43CB: 4B         LD           C,E
43CC: 00         NOP
43CD: 4C         LD           C,H
43CE: 03         INC         BC
43CF: 4C         LD           C,H
43D0: 04         INC         B
43D1: 4C         LD           C,H
43D2: 07         RLCA
43D3: 4C         LD           C,H
43D4: 08 4C 09   LD           ($094C),SP
43D7: 4C         LD           C,H
43D8: 0A         LD           A,(BC)
43D9: 4C         LD           C,H
43DA: 0F         RRCA
43DB: 4C         LD           C,H
43DC: 10 4C      STOP       $4C
43DE: 13         INC         DE
43DF: 4C         LD           C,H
43E0: 14         INC         D
43E1: 4C         LD           C,H
43E2: 15         DEC         D
43E3: 4C         LD           C,H
43E4: 1A         LD           A,(DE)
43E5: 4C         LD           C,H
43E6: 1B         DEC         DE
43E7: 4C         LD           C,H
43E8: 1E 4C      LD           E,$4C
43EA: 1F         RRA
43EB: 4C         LD           C,H
43EC: 22         LD           (HLI),A
43ED: 4C         LD           C,H
43EE: 25         DEC         H
43EF: 4C         LD           C,H
43F0: 26 4C      LD           H,$4C
43F2: 2F         CPL
43F3: 4C         LD           C,H
43F4: 30 4C      JR           NC,$4442
43F6: 41         LD           B,C
43F7: 4C         LD           C,H
43F8: 44         LD           B,H
43F9: 4C         LD           C,H
43FA: 4B         LD           C,E
43FB: 4C         LD           C,H
43FC: 4C         LD           C,H
43FD: 4C         LD           C,H
43FE: 4D         LD           C,L
43FF: 4C         LD           C,H
4400: 50         LD           D,B
4401: 4C         LD           C,H
4402: 51         LD           D,C
4403: 4C         LD           C,H
4404: 56         LD           D,(HL)
4405: 4C         LD           C,H
4406: 5D         LD           E,L
4407: 4C         LD           C,H
4408: 64         LD           H,H
4409: 4C         LD           C,H
440A: 6B         LD           L,E
440B: 4C         LD           C,H
440C: 6C         LD           L,H
440D: 4C         LD           C,H
440E: 6F         LD           L,A
440F: 4C         LD           C,H
4410: 76         HALT
4411: 4C         LD           C,H
4412: 7B         LD           A,E
4413: 4C         LD           C,H
4414: 7C         LD           A,H
4415: 4C         LD           C,H
4416: 83         ADD         A,E
4417: 4C         LD           C,H
4418: 84         ADD         A,H
4419: 4C         LD           C,H
441A: 8B         ADC         A,E
441B: 4C         LD           C,H
441C: 92         SUB         D
441D: 4C         LD           C,H
441E: 95         SUB         L
441F: 4C         LD           C,H
4420: 9A         SBC         D
4421: 4C         LD           C,H
4422: A3         AND         E
4423: 4C         LD           C,H
4424: AA         XOR         D
4425: 4C         LD           C,H
4426: B1         OR           C
4427: 4C         LD           C,H
4428: B6         OR           (HL)
4429: 4C         LD           C,H
442A: B9         CP           C
442B: 4C         LD           C,H
442C: C2 4C CB   JP           NZ,$CB4C
442F: 4C         LD           C,H
4430: D4 4C DB   CALL       NC,$DB4C
4433: 4C         LD           C,H
4434: E2         LDFF00   (C),A
4435: 4C         LD           C,H
4436: E5         PUSH       HL
4437: 4C         LD           C,H
4438: EC                              
4439: 4C         LD           C,H
443A: F3         DI
443B: 4C         LD           C,H
443C: FA 4C FD   LD           A,($FD4C)
443F: 4C         LD           C,H
4440: 08 4D 11   LD           ($114D),SP
4443: 4D         LD           C,L
4444: 1A         LD           A,(DE)
4445: 4D         LD           C,L
4446: 1B         DEC         DE
4447: 4D         LD           C,L
4448: 1C         INC         E
4449: 4D         LD           C,L
444A: 25         DEC         H
444B: 4D         LD           C,L
444C: 2E 4D      LD           L,$4D
444E: 2F         CPL
444F: 4D         LD           C,L
4450: 30 4D      JR           NC,$449F
4452: 35         DEC         (HL)
4453: 4D         LD           C,L
4454: 3E 4D      LD           A,$4D
4456: 47         LD           B,A
4457: 4D         LD           C,L
4458: 4E         LD           C,(HL)
4459: 4D         LD           C,L
445A: 51         LD           D,C
445B: 4D         LD           C,L
445C: 5A         LD           E,D
445D: 4D         LD           C,L
445E: 5B         LD           E,E
445F: 4D         LD           C,L
4460: 5C         LD           E,H
4461: 4D         LD           C,L
4462: 5F         LD           E,A
4463: 4D         LD           C,L
4464: 60         LD           H,B
4465: 4D         LD           C,L
4466: 63         LD           H,E
4467: 4D         LD           C,L
4468: 64         LD           H,H
4469: 4D         LD           C,L
446A: 67         LD           H,A
446B: 4D         LD           C,L
446C: 70         LD           (HL),B
446D: 4D         LD           C,L
446E: 71         LD           (HL),C
446F: 4D         LD           C,L
4470: 72         LD           (HL),D
4471: 4D         LD           C,L
4472: 75         LD           (HL),L
4473: 4D         LD           C,L
4474: 76         HALT
4475: 4D         LD           C,L
4476: 83         ADD         A,E
4477: 4D         LD           C,L
4478: 86         ADD         A,(HL)
4479: 4D         LD           C,L
447A: 8F         ADC         A,A
447B: 4D         LD           C,L
447C: 94         SUB         H
447D: 4D         LD           C,L
447E: 9D         SBC         L
447F: 4D         LD           C,L
4480: A2         AND         D
4481: 4D         LD           C,L
4482: A5         AND         L
4483: 4D         LD           C,L
4484: AA         XOR         D
4485: 4D         LD           C,L
4486: B1         OR           C
4487: 4D         LD           C,L
4488: B4         OR           H
4489: 4D         LD           C,L
448A: BD         CP           L
448B: 4D         LD           C,L
448C: C8         RET         Z
448D: 4D         LD           C,L
448E: CD 4D D4   CALL       $D44D
4491: 4D         LD           C,L
4492: DB                              
4493: 4D         LD           C,L
4494: DC 4D E1   CALL       C,$E14D
4497: 4D         LD           C,L
4498: EC                              
4499: 4D         LD           C,L
449A: F1         POP         AF
449B: 4D         LD           C,L
449C: F4                              
449D: 4D         LD           C,L
449E: F7         RST         0X30
449F: 4D         LD           C,L
44A0: FC                              
44A1: 4D         LD           C,L
44A2: FF         RST         0X38
44A3: 4D         LD           C,L
44A4: 02         LD           (BC),A
44A5: 4E         LD           C,(HL)
44A6: 05         DEC         B
44A7: 4E         LD           C,(HL)
44A8: 0E 4E      LD           C,$4E
44AA: 13         INC         DE
44AB: 4E         LD           C,(HL)
44AC: 1A         LD           A,(DE)
44AD: 4E         LD           C,(HL)
44AE: 23         INC         HL
44AF: 4E         LD           C,(HL)
44B0: 26 4E      LD           H,$4E
44B2: 2F         CPL
44B3: 4E         LD           C,(HL)
44B4: 30 4E      JR           NC,$4504
44B6: 39         ADD         HL,SP
44B7: 4E         LD           C,(HL)
44B8: 3C         INC         A
44B9: 4E         LD           C,(HL)
44BA: 45         LD           B,L
44BB: 4E         LD           C,(HL)
44BC: 48         LD           C,B
44BD: 4E         LD           C,(HL)
44BE: 51         LD           D,C
44BF: 4E         LD           C,(HL)
44C0: 5A         LD           E,D
44C1: 4E         LD           C,(HL)
44C2: 5F         LD           E,A
44C3: 4E         LD           C,(HL)
44C4: 64         LD           H,H
44C5: 4E         LD           C,(HL)
44C6: 65         LD           H,L
44C7: 4E         LD           C,(HL)
44C8: 68         LD           L,B
44C9: 4E         LD           C,(HL)
44CA: 6F         LD           L,A
44CB: 4E         LD           C,(HL)
44CC: 78         LD           A,B
44CD: 4E         LD           C,(HL)
44CE: 7D         LD           A,L
44CF: 4E         LD           C,(HL)
44D0: 82         ADD         A,D
44D1: 4E         LD           C,(HL)
44D2: 89         ADC         A,C
44D3: 4E         LD           C,(HL)
44D4: 8E         ADC         A,(HL)
44D5: 4E         LD           C,(HL)
44D6: 95         SUB         L
44D7: 4E         LD           C,(HL)
44D8: 9A         SBC         D
44D9: 4E         LD           C,(HL)
44DA: 9B         SBC         E
44DB: 4E         LD           C,(HL)
44DC: 9C         SBC         H
44DD: 4E         LD           C,(HL)
44DE: 9D         SBC         L
44DF: 4E         LD           C,(HL)
44E0: A0         AND         B
44E1: 4E         LD           C,(HL)
44E2: A1         AND         C
44E3: 4E         LD           C,(HL)
44E4: A2         AND         D
44E5: 4E         LD           C,(HL)
44E6: A3         AND         E
44E7: 4E         LD           C,(HL)
44E8: A4         AND         H
44E9: 4E         LD           C,(HL)
44EA: A7         AND         A
44EB: 4E         LD           C,(HL)
44EC: A8         XOR         B
44ED: 4E         LD           C,(HL)
44EE: A9         XOR         C
44EF: 4E         LD           C,(HL)
44F0: AA         XOR         D
44F1: 4E         LD           C,(HL)
44F2: AB         XOR         E
44F3: 4E         LD           C,(HL)
44F4: AC         XOR         H
44F5: 4E         LD           C,(HL)
44F6: AF         XOR         A
44F7: 4E         LD           C,(HL)
44F8: B0         OR           B
44F9: 4E         LD           C,(HL)
44FA: B1         OR           C
44FB: 4E         LD           C,(HL)
44FC: B2         OR           D
44FD: 4E         LD           C,(HL)
44FE: B3         OR           E
44FF: 4E         LD           C,(HL)
4500: B6         OR           (HL)
4501: 4E         LD           C,(HL)
4502: BF         CP           A
4503: 4E         LD           C,(HL)
4504: C6 4E      ADD         $4E
4506: CF         RST         0X08
4507: 4E         LD           C,(HL)
4508: D0         RET         NC
4509: 4E         LD           C,(HL)
450A: D1         POP         DE
450B: 4E         LD           C,(HL)
450C: D4 4E DD   CALL       NC,$DD4E
450F: 4E         LD           C,(HL)
4510: E2         LDFF00   (C),A
4511: 4E         LD           C,(HL)
4512: EB                              
4513: 4E         LD           C,(HL)
4514: F0 4E      LD           A,($4E)
4516: F1         POP         AF
4517: 4E         LD           C,(HL)
4518: FA 4E FF   LD           A,($FF4E)
451B: 4E         LD           C,(HL)
451C: 00         NOP
451D: 4F         LD           C,A
451E: 09         ADD         HL,BC
451F: 4F         LD           C,A
4520: 0E 4F      LD           C,$4F
4522: 0F         RRCA
4523: 4F         LD           C,A
4524: 18 4F      JR           $4575
4526: 1D         DEC         E
4527: 4F         LD           C,A
4528: 26 4F      LD           H,$4F
452A: 29         ADD         HL,HL
452B: 4F         LD           C,A
452C: 30 4F      JR           NC,$457D
452E: 33         INC         SP
452F: 4F         LD           C,A
4530: 42         LD           B,D
4531: 4F         LD           C,A
4532: 4D         LD           C,L
4533: 4F         LD           C,A
4534: 50         LD           D,B
4535: 4F         LD           C,A
4536: 53         LD           D,E
4537: 4F         LD           C,A
4538: 56         LD           D,(HL)
4539: 4F         LD           C,A
453A: 59         LD           E,C
453B: 4F         LD           C,A
453C: 5C         LD           E,H
453D: 4F         LD           C,A
453E: 5D         LD           E,L
453F: 4F         LD           C,A
4540: 66         LD           H,(HL)
4541: 4F         LD           C,A
4542: 69         LD           L,C
4543: 4F         LD           C,A
4544: 6C         LD           L,H
4545: 4F         LD           C,A
4546: 7D         LD           A,L
4547: 4F         LD           C,A
4548: 86         ADD         A,(HL)
4549: 4F         LD           C,A
454A: 89         ADC         A,C
454B: 4F         LD           C,A
454C: 8C         ADC         A,H
454D: 4F         LD           C,A
454E: 91         SUB         C
454F: 4F         LD           C,A
4550: 96         SUB         (HL)
4551: 4F         LD           C,A
4552: 9B         SBC         E
4553: 4F         LD           C,A
4554: A0         AND         B
4555: 4F         LD           C,A
4556: A3         AND         E
4557: 4F         LD           C,A
4558: A6         AND         (HL)
4559: 4F         LD           C,A
455A: AB         XOR         E
455B: 4F         LD           C,A
455C: B2         OR           D
455D: 4F         LD           C,A
455E: B7         OR           A
455F: 4F         LD           C,A
4560: BE         CP           (HL)
4561: 4F         LD           C,A
4562: C1         POP         BC
4563: 4F         LD           C,A
4564: C4 4F C9   CALL       NZ,$C94F
4567: 4F         LD           C,A
4568: CA 4F CD   JP           Z,$CD4F
456B: 4F         LD           C,A
456C: CE 4F      ADC         $4F
456E: D7         RST         0X10
456F: 4F         LD           C,A
4570: DE 4F      SBC         $4F
4572: E5         PUSH       HL
4573: 4F         LD           C,A
4574: EC                              
4575: 4F         LD           C,A
4576: EF         RST         0X28
4577: 4F         LD           C,A
4578: F4                              
4579: 4F         LD           C,A
457A: FB         EI
457B: 4F         LD           C,A
457C: 04         INC         B
457D: 50         LD           D,B
457E: 0D         DEC         C
457F: 50         LD           D,B
4580: 18 50      JR           $45D2
4582: 19         ADD         HL,DE
4583: 50         LD           D,B
4584: 1A         LD           A,(DE)
4585: 50         LD           D,B
4586: 1F         RRA
4587: 50         LD           D,B
4588: 26 50      LD           H,$50
458A: 27         DAA
458B: 50         LD           D,B
458C: 2E 50      LD           L,$50
458E: 31 50 3C   LD           SP,$3C50
4591: 50         LD           D,B
4592: 41         LD           B,C
4593: 50         LD           D,B
4594: 44         LD           B,H
4595: 50         LD           D,B
4596: 4B         LD           C,E
4597: 50         LD           D,B
4598: 4E         LD           C,(HL)
4599: 50         LD           D,B
459A: 51         LD           D,C
459B: 50         LD           D,B
459C: 5A         LD           E,D
459D: 50         LD           D,B
459E: 5D         LD           E,L
459F: 50         LD           D,B
45A0: 66         LD           H,(HL)
45A1: 50         LD           D,B
45A2: 69         LD           L,C
45A3: 50         LD           D,B
45A4: 6E         LD           L,(HL)
45A5: 50         LD           D,B
45A6: 77         LD           (HL),A
45A7: 50         LD           D,B
45A8: 78         LD           A,B
45A9: 50         LD           D,B
45AA: 79         LD           A,C
45AB: 50         LD           D,B
45AC: 7A         LD           A,D
45AD: 50         LD           D,B
45AE: 7F         LD           A,A
45AF: 50         LD           D,B
45B0: 82         ADD         A,D
45B1: 50         LD           D,B
45B2: 87         ADD         A,A
45B3: 50         LD           D,B
45B4: 8C         ADC         A,H
45B5: 50         LD           D,B
45B6: 8D         ADC         A,L
45B7: 50         LD           D,B
45B8: 8E         ADC         A,(HL)
45B9: 50         LD           D,B
45BA: 91         SUB         C
45BB: 50         LD           D,B
45BC: 94         SUB         H
45BD: 50         LD           D,B
45BE: 9B         SBC         E
45BF: 50         LD           D,B
45C0: A0         AND         B
45C1: 50         LD           D,B
45C2: A9         XOR         C
45C3: 50         LD           D,B
45C4: AC         XOR         H
45C5: 50         LD           D,B
45C6: AF         XOR         A
45C7: 50         LD           D,B
45C8: B2         OR           D
45C9: 50         LD           D,B
45CA: B5         OR           L
45CB: 50         LD           D,B
45CC: B8         CP           B
45CD: 50         LD           D,B
45CE: C1         POP         BC
45CF: 50         LD           D,B
45D0: C8         RET         Z
45D1: 50         LD           D,B
45D2: CB 50      BIT         1,E
45D4: CE 50      ADC         $50
45D6: D3                              
45D7: 50         LD           D,B
45D8: D4 50 D5   CALL       NC,$D550
45DB: 50         LD           D,B
45DC: D6 50      SUB         $50
45DE: DD                              
45DF: 50         LD           D,B
45E0: E6 50      AND         $50
45E2: E9         JP           (HL)
45E3: 50         LD           D,B
45E4: EE 50      XOR         $50
45E6: EF         RST         0X28
45E7: 50         LD           D,B
45E8: F0 50      LD           A,($50)
45EA: F3         DI
45EB: 50         LD           D,B
45EC: F6 50      OR           $50
45EE: FB         EI
45EF: 50         LD           D,B
45F0: FE 50      CP           $50
45F2: FF         RST         0X38
45F3: 50         LD           D,B
45F4: 04         INC         B
45F5: 51         LD           D,C
45F6: 0B         DEC         BC
45F7: 51         LD           D,C
45F8: 12         LD           (DE),A
45F9: 51         LD           D,C
45FA: 13         INC         DE
45FB: 51         LD           D,C
45FC: 1A         LD           A,(DE)
45FD: 51         LD           D,C
45FE: 1D         DEC         E
45FF: 51         LD           D,C
4600: FF         RST         0X38
4601: FF         RST         0X38
4602: 24         INC         H
4603: 39         ADD         HL,SP
4604: FF         RST         0X38
4605: 05         DEC         B
4606: 42         LD           B,D
4607: 32         LD           (HLD),A
4608: 2C         INC         L
4609: 55         LD           D,L
460A: 2C         INC         L
460B: FF         RST         0X38
460C: 14         INC         D
460D: 17         RLA
460E: FF         RST         0X38
460F: 13         INC         DE
4610: 17         RLA
4611: 66         LD           H,(HL)
4612: 16 15      LD           D,$15
4614: 1C         INC         E
4615: 33         INC         SP
4616: 1C         INC         E
4617: FF         RST         0X38
4618: 23         INC         HL
4619: 59         LD           E,C
461A: FF         RST         0X38
461B: 31 27 45   LD           SP,$4527
461E: 19         ADD         HL,DE
461F: FF         RST         0X38
4620: FF         RST         0X38
4621: 27         DAA
4622: 20 FF      JR           NZ,$4623
4624: 22         LD           (HLI),A
4625: 90         SUB         B
4626: 27         DAA
4627: 90         SUB         B
4628: 34         INC         (HL)
4629: 90         SUB         B
462A: 05         DEC         B
462B: 42         LD           B,D
462C: FF         RST         0X38
462D: 11 27 18   LD           DE,$1827
4630: 27         DAA
4631: 61         LD           H,C
4632: 27         DAA
4633: 68         LD           L,B
4634: 27         DAA
4635: FF         RST         0X38
4636: FF         RST         0X38
4637: 24         INC         H
4638: 29         ADD         HL,HL
4639: FF         RST         0X38
463A: 35         DEC         (HL)
463B: 29         ADD         HL,HL
463C: 14         INC         D
463D: 17         RLA
463E: 67         LD           H,A
463F: 16 FF      LD           D,$FF
4641: 44         LD           B,H
4642: 1E 26      LD           E,$26
4644: 19         ADD         HL,DE
4645: 35         DEC         (HL)
4646: 19         ADD         HL,DE
4647: FF         RST         0X38
4648: 67         LD           H,A
4649: 17         RLA
464A: 55         LD           D,L
464B: 16 23      LD           D,$23
464D: 1E FF      LD           E,$FF
464F: 34         INC         (HL)
4650: 61         LD           H,C
4651: 38 81      JR           C,$45D4
4653: 36 82      LD           (HL),$82
4655: FF         RST         0X38
4656: 34         INC         (HL)
4657: 19         ADD         HL,DE
4658: 35         DEC         (HL)
4659: 19         ADD         HL,DE
465A: 44         LD           B,H
465B: 19         ADD         HL,DE
465C: 45         LD           B,L
465D: 19         ADD         HL,DE
465E: FF         RST         0X38
465F: 14         INC         D
4660: 20 52      JR           NZ,$46B4
4662: 1C         INC         E
4663: 57         LD           D,A
4664: 1C         INC         E
4665: FF         RST         0X38
4666: 43         LD           B,E
4667: 1E 46      LD           E,$46
4669: 1E 54      LD           E,$54
466B: 19         ADD         HL,DE
466C: 55         LD           D,L
466D: 19         ADD         HL,DE
466E: FF         RST         0X38
466F: 42         LD           B,D
4670: 9B         SBC         E
4671: 32         LD           (HLD),A
4672: 9B         SBC         E
4673: 34         INC         (HL)
4674: 9B         SBC         E
4675: 44         LD           B,H
4676: 9B         SBC         E
4677: 11 9E 15   LD           DE,$159E
467A: 9E         SBC         (HL)
467B: FF         RST         0X38
467C: 23         INC         HL
467D: 20 26      JR           NZ,$46A5
467F: 20 FF      JR           NZ,$4680
4681: 34         INC         (HL)
4682: 61         LD           H,C
4683: FF         RST         0X38
4684: 65         LD           H,L
4685: 9F         SBC         A
4686: FF         RST         0X38
4687: 62         LD           H,D
4688: 9F         SBC         A
4689: 65         LD           H,L
468A: 9F         SBC         A
468B: FF         RST         0X38
468C: FF         RST         0X38
468D: FF         RST         0X38
468E: 44         LD           B,H
468F: E5         PUSH       HL
4690: FF         RST         0X38
4691: 51         LD           D,C
4692: 27         DAA
4693: 58         LD           E,B
4694: 27         DAA
4695: FF         RST         0X38
4696: 25         DEC         H
4697: D8         RET         C
4698: FF         RST         0X38
4699: 14         INC         D
469A: D8         RET         C
469B: FF         RST         0X38
469C: 24         INC         H
469D: 50         LD           D,B
469E: 45         LD           B,L
469F: 50         LD           D,B
46A0: FF         RST         0X38
46A1: 32         LD           (HLD),A
46A2: 19         ADD         HL,DE
46A3: 37         SCF
46A4: 19         ADD         HL,DE
46A5: 18 2D      JR           $46D4
46A7: 24         INC         H
46A8: 2E 57      LD           L,$57
46AA: 2E 25      LD           L,$25
46AC: 86         ADD         A,(HL)
46AD: FF         RST         0X38
46AE: 24         INC         H
46AF: 66         LD           H,(HL)
46B0: 53         LD           D,E
46B1: 2D         DEC         L
46B2: 54         LD           D,H
46B3: 2D         DEC         L
46B4: 55         LD           D,L
46B5: 2D         DEC         L
46B6: 56         LD           D,(HL)
46B7: 2D         DEC         L
46B8: FF         RST         0X38
46B9: 17         RLA
46BA: 20 23      JR           NZ,$46DF
46BC: 1C         INC         E
46BD: 64         LD           H,H
46BE: 19         ADD         HL,DE
46BF: FF         RST         0X38
46C0: 23         INC         HL
46C1: 19         ADD         HL,DE
46C2: 25         DEC         H
46C3: 19         ADD         HL,DE
46C4: 43         LD           B,E
46C5: 19         ADD         HL,DE
46C6: 45         LD           B,L
46C7: 19         ADD         HL,DE
46C8: 34         INC         (HL)
46C9: 66         LD           H,(HL)
46CA: 18 1A      JR           $46E6
46CC: FF         RST         0X38
46CD: 44         LD           B,H
46CE: 18 67      JR           $4737
46D0: 18 46      JR           $4718
46D2: 1B         DEC         DE
46D3: 55         LD           D,L
46D4: 2E 63      LD           L,$63
46D6: 2F         CPL
46D7: FF         RST         0X38
46D8: 61         LD           H,C
46D9: 52         LD           D,D
46DA: 24         INC         H
46DB: 19         ADD         HL,DE
46DC: 35         DEC         (HL)
46DD: 19         ADD         HL,DE
46DE: 46         LD           B,(HL)
46DF: 19         ADD         HL,DE
46E0: FF         RST         0X38
46E1: 64         LD           H,H
46E2: 18 67      JR           $474B
46E4: 19         ADD         HL,DE
46E5: 33         INC         SP
46E6: 0B         DEC         BC
46E7: FF         RST         0X38
46E8: 25         DEC         H
46E9: 89         ADC         A,C
46EA: 34         INC         (HL)
46EB: 61         LD           H,C
46EC: FF         RST         0X38
46ED: 22         LD           (HLI),A
46EE: 19         ADD         HL,DE
46EF: 57         LD           D,A
46F0: 19         ADD         HL,DE
46F1: 05         DEC         B
46F2: 42         LD           B,D
46F3: 32         LD           (HLD),A
46F4: 2D         DEC         L
46F5: 66         LD           H,(HL)
46F6: E5         PUSH       HL
46F7: FF         RST         0X38
46F8: 24         INC         H
46F9: 39         ADD         HL,SP
46FA: FF         RST         0X38
46FB: 24         INC         H
46FC: 5C         LD           E,H
46FD: FF         RST         0X38
46FE: 22         LD           (HLI),A
46FF: 19         ADD         HL,DE
4700: 21 16 44   LD           HL,$4416
4703: E5         PUSH       HL
4704: FF         RST         0X38
4705: FF         RST         0X38
4706: 15         DEC         D
4707: 20 FF      JR           NZ,$4708
4709: 24         INC         H
470A: 19         ADD         HL,DE
470B: 54         LD           D,H
470C: 19         ADD         HL,DE
470D: 62         LD           H,D
470E: 17         RLA
470F: 24         INC         H
4710: 2D         DEC         L
4711: 65         LD           H,L
4712: 2D         DEC         L
4713: FF         RST         0X38
4714: 11 27 18   LD           DE,$1827
4717: 27         DAA
4718: 61         LD           H,C
4719: 27         DAA
471A: 68         LD           L,B
471B: 27         DAA
471C: 33         INC         SP
471D: 19         ADD         HL,DE
471E: 36 19      LD           (HL),$19
4720: FF         RST         0X38
4721: 12         LD           (DE),A
4722: 16 FF      LD           D,$FF
4724: 34         INC         (HL)
4725: 1E 35      LD           E,$35
4727: 1A         LD           A,(DE)
4728: FF         RST         0X38
4729: 35         DEC         (HL)
472A: 66         LD           H,(HL)
472B: 12         LD           (DE),A
472C: 16 FF      LD           D,$FF
472E: 35         DEC         (HL)
472F: 8F         ADC         A,A
4730: 36 8F      LD           (HL),$8F
4732: 68         LD           L,B
4733: 2E FF      LD           L,$FF
4735: 25         DEC         H
4736: 2C         INC         L
4737: 68         LD           L,B
4738: 2C         INC         L
4739: FF         RST         0X38
473A: 34         INC         (HL)
473B: 61         LD           H,C
473C: 17         RLA
473D: 2D         DEC         L
473E: 18 2D      JR           $476D
4740: 27         DAA
4741: 2D         DEC         L
4742: 28 2D      JR           Z,$4771
4744: FF         RST         0X38
4745: 54         LD           D,H
4746: 8F         ADC         A,A
4747: 44         LD           B,H
4748: 2E 46      LD           L,$46
474A: 2E FF      LD           L,$FF
474C: 62         LD           H,D
474D: 14         INC         D
474E: 45         LD           B,L
474F: 66         LD           H,(HL)
4750: FF         RST         0X38
4751: 68         LD           L,B
4752: 66         LD           H,(HL)
4753: 11 2D 21   LD           DE,$212D
4756: 2D         DEC         L
4757: 45         LD           B,L
4758: 86         ADD         A,(HL)
4759: FF         RST         0X38
475A: 43         LD           B,E
475B: A5         AND         L
475C: 66         LD           H,(HL)
475D: D6 FF      SUB         $FF
475F: 43         LD           B,E
4760: A5         AND         L
4761: 66         LD           H,(HL)
4762: D6 67      SUB         $67
4764: D6 FF      SUB         $FF
4766: 53         LD           D,E
4767: A2         AND         D
4768: 57         LD           D,A
4769: A2         AND         D
476A: 55         LD           D,L
476B: 9F         SBC         A
476C: FF         RST         0X38
476D: 54         LD           D,H
476E: A2         AND         D
476F: 62         LD           H,D
4770: 9F         SBC         A
4771: FF         RST         0X38
4772: 33         INC         SP
4773: A4         AND         H
4774: FF         RST         0X38
4775: 63         LD           H,E
4776: A3         AND         E
4777: FF         RST         0X38
4778: 15         DEC         D
4779: 55         LD           D,L
477A: 42         LD           B,D
477B: 55         LD           D,L
477C: 37         SCF
477D: 14         INC         D
477E: 34         INC         (HL)
477F: 86         ADD         A,(HL)
4780: FF         RST         0X38
4781: 18 55      JR           $47D8
4783: 41         LD           B,C
4784: 55         LD           D,L
4785: 43         LD           B,E
4786: 55         LD           D,L
4787: 44         LD           B,H
4788: 2F         CPL
4789: FF         RST         0X38
478A: 23         INC         HL
478B: 9B         SBC         E
478C: 32         LD           (HLD),A
478D: 0B         DEC         BC
478E: 35         DEC         (HL)
478F: 9B         SBC         E
4790: 46         LD           B,(HL)
4791: 9B         SBC         E
4792: FF         RST         0X38
4793: 12         LD           (DE),A
4794: 56         LD           D,(HL)
4795: 26 56      LD           H,$56
4797: 47         LD           B,A
4798: 56         LD           D,(HL)
4799: 33         INC         SP
479A: 9B         SBC         E
479B: 37         SCF
479C: 9B         SBC         E
479D: FF         RST         0X38
479E: 23         INC         HL
479F: 1A         LD           A,(DE)
47A0: 35         DEC         (HL)
47A1: 1B         DEC         DE
47A2: 42         LD           B,D
47A3: 1B         DEC         DE
47A4: FF         RST         0X38
47A5: 23         INC         HL
47A6: 60         LD           H,B
47A7: 25         DEC         H
47A8: 60         LD           H,B
47A9: 34         INC         (HL)
47AA: 61         LD           H,C
47AB: FF         RST         0X38
47AC: 64         LD           H,H
47AD: E5         PUSH       HL
47AE: FF         RST         0X38
47AF: 13         INC         DE
47B0: 1A         LD           A,(DE)
47B1: 46         LD           B,(HL)
47B2: 1A         LD           A,(DE)
47B3: 32         LD           (HLD),A
47B4: 9B         SBC         E
47B5: FF         RST         0X38
47B6: 22         LD           (HLI),A
47B7: 57         LD           D,A
47B8: 56         LD           D,(HL)
47B9: 57         LD           D,A
47BA: 33         INC         SP
47BB: 9B         SBC         E
47BC: 36 9B      LD           (HL),$9B
47BE: FF         RST         0X38
47BF: 34         INC         (HL)
47C0: 1C         INC         E
47C1: 43         LD           B,E
47C2: 1C         INC         E
47C3: 45         LD           B,L
47C4: 1C         INC         E
47C5: 54         LD           D,H
47C6: 1C         INC         E
47C7: 44         LD           B,H
47C8: 1B         DEC         DE
47C9: FF         RST         0X38
47CA: 24         INC         H
47CB: 0B         DEC         BC
47CC: 47         LD           B,A
47CD: 0B         DEC         BC
47CE: 67         LD           H,A
47CF: 2D         DEC         L
47D0: 68         LD           L,B
47D1: 38 FF      JR           C,$47D2
47D3: 62         LD           H,D
47D4: 0B         DEC         BC
47D5: 64         LD           H,H
47D6: 0B         DEC         BC
47D7: 66         LD           H,(HL)
47D8: 2D         DEC         L
47D9: 67         LD           H,A
47DA: 2D         DEC         L
47DB: FF         RST         0X38
47DC: 25         DEC         H
47DD: 9B         SBC         E
47DE: 27         DAA
47DF: 9B         SBC         E
47E0: 45         LD           B,L
47E1: 9B         SBC         E
47E2: 47         LD           B,A
47E3: 9B         SBC         E
47E4: FF         RST         0X38
47E5: 12         LD           (DE),A
47E6: 9B         SBC         E
47E7: 21 9B 26   LD           HL,$269B
47EA: 9B         SBC         E
47EB: 28 9B      JR           Z,$4788
47ED: 68         LD           L,B
47EE: 9B         SBC         E
47EF: FF         RST         0X38
47F0: 31 1C 35   LD           SP,$351C
47F3: 1E 45      LD           E,$45
47F5: 1E FF      LD           E,$FF
47F7: 36 9B      LD           (HL),$9B
47F9: 46         LD           B,(HL)
47FA: 9B         SBC         E
47FB: 37         SCF
47FC: 9B         SBC         E
47FD: 47         LD           B,A
47FE: 9B         SBC         E
47FF: FF         RST         0X38
4800: 32         LD           (HLD),A
4801: 19         ADD         HL,DE
4802: 61         LD           H,C
4803: 19         ADD         HL,DE
4804: 46         LD           B,(HL)
4805: 14         INC         D
4806: FF         RST         0X38
4807: 31 1C 41   LD           SP,$411C
480A: 55         LD           D,L
480B: 48         LD           C,B
480C: 55         LD           D,L
480D: 35         DEC         (HL)
480E: 14         INC         D
480F: FF         RST         0X38
4810: 34         INC         (HL)
4811: 61         LD           H,C
4812: FF         RST         0X38
4813: 37         SCF
4814: 53         LD           D,E
4815: FF         RST         0X38
4816: 33         INC         SP
4817: 42         LD           B,D
4818: 36 66      LD           (HL),$66
481A: 41         LD           B,C
481B: 0B         DEC         BC
481C: 48         LD           C,B
481D: 1A         LD           A,(DE)
481E: 21 2D FF   LD           HL,$FF2D
4821: 27         DAA
4822: 57         LD           D,A
4823: 36 9B      LD           (HL),$9B
4825: 41         LD           B,C
4826: 9B         SBC         E
4827: 57         LD           D,A
4828: 57         LD           D,A
4829: 42         LD           B,D
482A: E5         PUSH       HL
482B: FF         RST         0X38
482C: 25         DEC         H
482D: 9B         SBC         E
482E: 45         LD           B,L
482F: 9B         SBC         E
4830: 27         DAA
4831: 9B         SBC         E
4832: 47         LD           B,A
4833: 9B         SBC         E
4834: 32         LD           (HLD),A
4835: 1C         INC         E
4836: FF         RST         0X38
4837: 26 57      LD           H,$57
4839: 33         INC         SP
483A: 19         ADD         HL,DE
483B: 57         LD           D,A
483C: 19         ADD         HL,DE
483D: FF         RST         0X38
483E: 34         INC         (HL)
483F: 9B         SBC         E
4840: 41         LD           B,C
4841: 9B         SBC         E
4842: 56         LD           D,(HL)
4843: 9B         SBC         E
4844: 36 57      LD           (HL),$57
4846: 52         LD           D,D
4847: 0B         DEC         BC
4848: 54         LD           D,H
4849: 38 55      JR           C,$48A0
484B: 38 FF      JR           C,$484C
484D: 24         INC         H
484E: 39         ADD         HL,SP
484F: FF         RST         0X38
4850: 34         INC         (HL)
4851: 5B         LD           E,E
4852: FF         RST         0X38
4853: 13         INC         DE
4854: 19         ADD         HL,DE
4855: 25         DEC         H
4856: 19         ADD         HL,DE
4857: 42         LD           B,D
4858: 19         ADD         HL,DE
4859: 55         LD           D,L
485A: 19         ADD         HL,DE
485B: 67         LD           H,A
485C: 19         ADD         HL,DE
485D: FF         RST         0X38
485E: 15         DEC         D
485F: 57         LD           D,A
4860: 32         LD           (HLD),A
4861: 57         LD           D,A
4862: 67         LD           H,A
4863: 57         LD           D,A
4864: 34         INC         (HL)
4865: E5         PUSH       HL
4866: FF         RST         0X38
4867: FF         RST         0X38
4868: 37         SCF
4869: AB         XOR         E
486A: 53         LD           D,E
486B: AA         XOR         D
486C: FF         RST         0X38
486D: 34         INC         (HL)
486E: AB         XOR         E
486F: 62         LD           H,D
4870: AA         XOR         D
4871: FF         RST         0X38
4872: 03         INC         BC
4873: 9E         SBC         (HL)
4874: 05         DEC         B
4875: 9E         SBC         (HL)
4876: 53         LD           D,E
4877: 1B         DEC         DE
4878: 55         LD           D,L
4879: 1B         DEC         DE
487A: FF         RST         0X38
487B: 07         RLCA
487C: 69         LD           L,C
487D: 53         LD           D,E
487E: 16 21      LD           D,$21
4880: 46         LD           B,(HL)
4881: 51         LD           D,C
4882: 47         LD           B,A
4883: 63         LD           H,E
4884: 48         LD           C,B
4885: 66         LD           H,(HL)
4886: 49         LD           C,C
4887: FF         RST         0X38
4888: 24         INC         H
4889: 39         ADD         HL,SP
488A: FF         RST         0X38
488B: 34         INC         (HL)
488C: 8A         ADC         A,D
488D: 33         INC         SP
488E: 24         INC         H
488F: 36 24      LD           (HL),$24
4891: 45         LD           B,L
4892: 1B         DEC         DE
4893: 44         LD           B,H
4894: E5         PUSH       HL
4895: FF         RST         0X38
4896: 11 8E 14   LD           DE,$148E
4899: 61         LD           H,C
489A: FF         RST         0X38
489B: 13         INC         DE
489C: 15         DEC         D
489D: 17         RLA
489E: 15         DEC         D
489F: 35         DEC         (HL)
48A0: 99         SBC         C
48A1: 32         LD           (HLD),A
48A2: E5         PUSH       HL
48A3: FF         RST         0X38
48A4: FF         RST         0X38
48A5: 34         INC         (HL)
48A6: 8B         ADC         A,E
48A7: 23         INC         HL
48A8: 99         SBC         C
48A9: 36 99      LD           (HL),$99
48AB: 55         LD           D,L
48AC: 99         SBC         C
48AD: FF         RST         0X38
48AE: 04         INC         B
48AF: 9E         SBC         (HL)
48B0: 05         DEC         B
48B1: 9E         SBC         (HL)
48B2: 37         SCF
48B3: 9B         SBC         E
48B4: 58         LD           E,B
48B5: 9B         SBC         E
48B6: 61         LD           H,C
48B7: 17         RLA
48B8: FF         RST         0X38
48B9: 44         LD           B,H
48BA: 1B         DEC         DE
48BB: 45         LD           B,L
48BC: 1B         DEC         DE
48BD: 67         LD           H,A
48BE: 2E 68      LD           L,$68
48C0: 2D         DEC         L
48C1: FF         RST         0X38
48C2: 13         INC         DE
48C3: 9C         SBC         H
48C4: 24         INC         H
48C5: 9B         SBC         E
48C6: 32         LD           (HLD),A
48C7: 14         INC         D
48C8: 58         LD           E,B
48C9: 1B         DEC         DE
48CA: FF         RST         0X38
48CB: 28 99      JR           Z,$4866
48CD: 35         DEC         (HL)
48CE: A0         AND         B
48CF: 43         LD           B,E
48D0: 99         SBC         C
48D1: 57         LD           D,A
48D2: A0         AND         B
48D3: 58         LD           E,B
48D4: 38 FF      JR           C,$48D5
48D6: 23         INC         HL
48D7: 1B         DEC         DE
48D8: 53         LD           D,E
48D9: 1B         DEC         DE
48DA: 56         LD           D,(HL)
48DB: 1B         DEC         DE
48DC: 54         LD           D,H
48DD: 2D         DEC         L
48DE: FF         RST         0X38
48DF: 37         SCF
48E0: 14         INC         D
48E1: 48         LD           C,B
48E2: 1B         DEC         DE
48E3: 55         LD           D,L
48E4: 0B         DEC         BC
48E5: 18 2D      JR           $4914
48E7: FF         RST         0X38
48E8: 37         SCF
48E9: 99         SBC         C
48EA: 46         LD           B,(HL)
48EB: 99         SBC         C
48EC: 52         LD           D,D
48ED: E5         PUSH       HL
48EE: FF         RST         0X38
48EF: 43         LD           B,E
48F0: 42         LD           B,D
48F1: 33         INC         SP
48F2: 9B         SBC         E
48F3: 36 2C      LD           (HL),$2C
48F5: 42         LD           B,D
48F6: 2C         INC         L
48F7: 25         DEC         H
48F8: 2F         CPL
48F9: FF         RST         0X38
48FA: 55         LD           D,L
48FB: 1B         DEC         DE
48FC: 58         LD           E,B
48FD: 1B         DEC         DE
48FE: FF         RST         0X38
48FF: 35         DEC         (HL)
4900: 15         DEC         D
4901: 43         LD           B,E
4902: 99         SBC         C
4903: 58         LD           E,B
4904: A0         AND         B
4905: 51         LD           D,C
4906: 2E 61      LD           L,$61
4908: 2E FF      LD           L,$FF
490A: 13         INC         DE
490B: A0         AND         B
490C: 28 A0      JR           Z,$48AE
490E: 36 A0      LD           (HL),$A0
4910: FF         RST         0X38
4911: 22         LD           (HLI),A
4912: 99         SBC         C
4913: 26 99      LD           H,$99
4915: 34         INC         (HL)
4916: 99         SBC         C
4917: FF         RST         0X38
4918: 22         LD           (HLI),A
4919: 99         SBC         C
491A: 35         DEC         (HL)
491B: A0         AND         B
491C: 44         LD           B,H
491D: 99         SBC         C
491E: FF         RST         0X38
491F: 25         DEC         H
4920: 99         SBC         C
4921: 28 99      JR           Z,$48BC
4923: 42         LD           B,D
4924: A0         AND         B
4925: 47         LD           B,A
4926: 99         SBC         C
4927: 21 2F FF   LD           HL,$FF2F
492A: 51         LD           D,C
492B: 2D         DEC         L
492C: 61         LD           H,C
492D: 2D         DEC         L
492E: 65         LD           H,L
492F: 99         SBC         C
4930: 36 86      LD           (HL),$86
4932: FF         RST         0X38
4933: 42         LD           B,D
4934: 2C         INC         L
4935: 46         LD           B,(HL)
4936: 2C         INC         L
4937: 55         LD           D,L
4938: 1B         DEC         DE
4939: FF         RST         0X38
493A: 35         DEC         (HL)
493B: 2C         INC         L
493C: 53         LD           D,E
493D: 16 56      LD           D,$56
493F: 1B         DEC         DE
4940: 62         LD           H,D
4941: 2C         INC         L
4942: FF         RST         0X38
4943: 36 99      LD           (HL),$99
4945: 48         LD           C,B
4946: 99         SBC         C
4947: 54         LD           D,H
4948: 99         SBC         C
4949: FF         RST         0X38
494A: 34         INC         (HL)
494B: 61         LD           H,C
494C: FF         RST         0X38
494D: 21 99 28   LD           HL,$2899
4950: 99         SBC         C
4951: 52         LD           D,D
4952: 99         SBC         C
4953: 68         LD           L,B
4954: 99         SBC         C
4955: FF         RST         0X38
4956: 23         INC         HL
4957: 30 FF      JR           NC,$4958
4959: 32         LD           (HLD),A
495A: A3         AND         E
495B: FF         RST         0X38
495C: FF         RST         0X38
495D: FF         RST         0X38
495E: 34         INC         (HL)
495F: 5F         LD           E,A
4960: FF         RST         0X38
4961: 13         INC         DE
4962: 1E 51      LD           E,$51
4964: 1E 18      LD           E,$18
4966: 1A         LD           A,(DE)
4967: 65         LD           H,L
4968: 1A         LD           A,(DE)
4969: FF         RST         0X38
496A: 24         INC         H
496B: 39         ADD         HL,SP
496C: FF         RST         0X38
496D: 33         INC         SP
496E: 1E 34      LD           E,$34
4970: 1A         LD           A,(DE)
4971: 35         DEC         (HL)
4972: 1E 54      LD           E,$54
4974: E5         PUSH       HL
4975: FF         RST         0X38
4976: 34         INC         (HL)
4977: 5F         LD           E,A
4978: FF         RST         0X38
4979: 34         INC         (HL)
497A: 5D         LD           E,L
497B: FF         RST         0X38
497C: FF         RST         0X38
497D: 16 16      LD           D,$16
497F: 25         DEC         H
4980: 9B         SBC         E
4981: 37         SCF
4982: 9B         SBC         E
4983: 42         LD           B,D
4984: 9B         SBC         E
4985: 18 2D      JR           $49B4
4987: 61         LD           H,C
4988: 2D         DEC         L
4989: FF         RST         0X38
498A: 32         LD           (HLD),A
498B: 14         INC         D
498C: 44         LD           B,H
498D: 9C         SBC         H
498E: 62         LD           H,D
498F: 2E 64      LD           L,$64
4991: 2E 58      LD           L,$58
4993: E5         PUSH       HL
4994: FF         RST         0X38
4995: 41         LD           B,C
4996: 9E         SBC         (HL)
4997: 48         LD           C,B
4998: 9E         SBC         (HL)
4999: 26 0B      LD           H,$0B
499B: 56         LD           D,(HL)
499C: 14         INC         D
499D: 18 2D      JR           $49CC
499F: 61         LD           H,C
49A0: 2E 62      LD           L,$62
49A2: 2E FF      LD           L,$FF
49A4: 05         DEC         B
49A5: 42         LD           B,D
49A6: 24         INC         H
49A7: 9C         SBC         H
49A8: 26 15      LD           H,$15
49AA: 64         LD           H,H
49AB: 9C         SBC         H
49AC: 66         LD           H,(HL)
49AD: 9C         SBC         H
49AE: FF         RST         0X38
49AF: 65         LD           H,L
49B0: 17         RLA
49B1: FF         RST         0X38
49B2: FF         RST         0X38
49B3: 15         DEC         D
49B4: 99         SBC         C
49B5: 41         LD           B,C
49B6: 99         SBC         C
49B7: 48         LD           C,B
49B8: 99         SBC         C
49B9: 65         LD           H,L
49BA: 99         SBC         C
49BB: FF         RST         0X38
49BC: 22         LD           (HLI),A
49BD: 0B         DEC         BC
49BE: 35         DEC         (HL)
49BF: 0B         DEC         BC
49C0: 43         LD           B,E
49C1: 9C         SBC         H
49C2: 13         INC         DE
49C3: 2E FF      LD           L,$FF
49C5: 42         LD           B,D
49C6: 16 64      LD           D,$64
49C8: 1B         DEC         DE
49C9: 66         LD           H,(HL)
49CA: 14         INC         D
49CB: 54         LD           D,H
49CC: 86         ADD         A,(HL)
49CD: FF         RST         0X38
49CE: 11 27 18   LD           DE,$1827
49D1: 27         DAA
49D2: 61         LD           H,C
49D3: 27         DAA
49D4: 68         LD           L,B
49D5: 27         DAA
49D6: 23         INC         HL
49D7: 9C         SBC         H
49D8: 42         LD           B,D
49D9: 14         INC         D
49DA: FF         RST         0X38
49DB: 31 16 57   LD           SP,$5716
49DE: 17         RLA
49DF: FF         RST         0X38
49E0: 34         INC         (HL)
49E1: 5F         LD           E,A
49E2: FF         RST         0X38
49E3: 12         LD           (DE),A
49E4: 5E         LD           E,(HL)
49E5: 42         LD           B,D
49E6: 5E         LD           E,(HL)
49E7: 34         INC         (HL)
49E8: 61         LD           H,C
49E9: FF         RST         0X38
49EA: 24         INC         H
49EB: 1B         DEC         DE
49EC: 43         LD           B,E
49ED: 1B         DEC         DE
49EE: 55         LD           D,L
49EF: 15         DEC         D
49F0: 34         INC         (HL)
49F1: 2D         DEC         L
49F2: 35         DEC         (HL)
49F3: 37         SCF
49F4: FF         RST         0X38
49F5: 34         INC         (HL)
49F6: 5F         LD           E,A
49F7: FF         RST         0X38
49F8: 24         INC         H
49F9: 9B         SBC         E
49FA: 32         LD           (HLD),A
49FB: 9B         SBC         E
49FC: 44         LD           B,H
49FD: 9B         SBC         E
49FE: 25         DEC         H
49FF: 38 26      JR           C,$4A27
4A01: 38 36      JR           C,$4A39
4A03: 2D         DEC         L
4A04: FF         RST         0X38
4A05: 42         LD           B,D
4A06: 24         INC         H
4A07: 53         LD           D,E
4A08: 24         INC         H
4A09: 66         LD           H,(HL)
4A0A: 24         INC         H
4A0B: 21 2D 53   LD           HL,$532D
4A0E: E5         PUSH       HL
4A0F: FF         RST         0X38
4A10: 14         INC         D
4A11: 27         DAA
4A12: 16 27      LD           D,$27
4A14: 64         LD           H,H
4A15: 27         DAA
4A16: 66         LD           H,(HL)
4A17: 27         DAA
4A18: 22         LD           (HLI),A
4A19: 9B         SBC         E
4A1A: 52         LD           D,D
4A1B: 9B         SBC         E
4A1C: FF         RST         0X38
4A1D: 15         DEC         D
4A1E: 9E         SBC         (HL)
4A1F: 32         LD           (HLD),A
4A20: 1B         DEC         DE
4A21: 34         INC         (HL)
4A22: 1B         DEC         DE
4A23: 37         SCF
4A24: 2F         CPL
4A25: 43         LD           B,E
4A26: E5         PUSH       HL
4A27: FF         RST         0X38
4A28: 12         LD           (DE),A
4A29: 1A         LD           A,(DE)
4A2A: 17         RLA
4A2B: 1A         LD           A,(DE)
4A2C: 46         LD           B,(HL)
4A2D: 1E FF      LD           E,$FF
4A2F: 24         INC         H
4A30: 16 33      LD           D,$33
4A32: 24         INC         H
4A33: 55         LD           D,L
4A34: 24         INC         H
4A35: 54         LD           D,H
4A36: 86         ADD         A,(HL)
4A37: FF         RST         0X38
4A38: 11 27 18   LD           DE,$1827
4A3B: 27         DAA
4A3C: 61         LD           H,C
4A3D: 27         DAA
4A3E: 68         LD           L,B
4A3F: 27         DAA
4A40: 55         LD           D,L
4A41: 24         INC         H
4A42: 33         INC         SP
4A43: 24         INC         H
4A44: FF         RST         0X38
4A45: 26 1A      LD           H,$1A
4A47: 32         LD           (HLD),A
4A48: 24         INC         H
4A49: 53         LD           D,E
4A4A: 1E FF      LD           E,$FF
4A4C: 34         INC         (HL)
4A4D: 16 35      LD           D,$35
4A4F: 24         INC         H
4A50: 44         LD           B,H
4A51: 24         INC         H
4A52: FF         RST         0X38
4A53: 23         INC         HL
4A54: 19         ADD         HL,DE
4A55: 26 19      LD           H,$19
4A57: 43         LD           B,E
4A58: 19         ADD         HL,DE
4A59: 46         LD           B,(HL)
4A5A: 19         ADD         HL,DE
4A5B: 34         INC         (HL)
4A5C: 24         INC         H
4A5D: FF         RST         0X38
4A5E: 44         LD           B,H
4A5F: 24         INC         H
4A60: 45         LD           B,L
4A61: 16 55      LD           D,$55
4A63: 1B         DEC         DE
4A64: FF         RST         0X38
4A65: 34         INC         (HL)
4A66: 61         LD           H,C
4A67: FF         RST         0X38
4A68: 33         INC         SP
4A69: A9         XOR         C
4A6A: 34         INC         (HL)
4A6B: A9         XOR         C
4A6C: 37         SCF
4A6D: 9F         SBC         A
4A6E: FF         RST         0X38
4A6F: 42         LD           B,D
4A70: A9         XOR         C
4A71: 52         LD           D,D
4A72: A9         XOR         C
4A73: FF         RST         0X38
4A74: 51         LD           D,C
4A75: 9F         SBC         A
4A76: FF         RST         0X38
4A77: 32         LD           (HLD),A
4A78: 9F         SBC         A
4A79: 34         INC         (HL)
4A7A: 9F         SBC         A
4A7B: FF         RST         0X38
4A7C: 53         LD           D,E
4A7D: AC         XOR         H
4A7E: 56         LD           D,(HL)
4A7F: AC         XOR         H
4A80: FF         RST         0X38
4A81: 52         LD           D,D
4A82: AC         XOR         H
4A83: 56         LD           D,(HL)
4A84: AC         XOR         H
4A85: FF         RST         0X38
4A86: 52         LD           D,D
4A87: A6         AND         (HL)
4A88: 36 A6      LD           (HL),$A6
4A8A: 54         LD           D,H
4A8B: A6         AND         (HL)
4A8C: 38 A6      JR           C,$4A34
4A8E: FF         RST         0X38
4A8F: 54         LD           D,H
4A90: A6         AND         (HL)
4A91: 36 A6      LD           (HL),$A6
4A93: FF         RST         0X38
4A94: 15         DEC         D
4A95: D9         RETI
4A96: FF         RST         0X38
4A97: 37         SCF
4A98: A2         AND         D
4A99: FF         RST         0X38
4A9A: 24         INC         H
4A9B: 84         ADD         A,H
4A9C: FF         RST         0X38
4A9D: FF         RST         0X38
4A9E: FF         RST         0X38
4A9F: FF         RST         0X38
4AA0: 53         LD           D,E
4AA1: 98         SBC         B
4AA2: 56         LD           D,(HL)
4AA3: 98         SBC         B
4AA4: 22         LD           (HLI),A
4AA5: 66         LD           H,(HL)
4AA6: 21 9C FF   LD           HL,$FF9C
4AA9: 53         LD           D,E
4AAA: 98         SBC         B
4AAB: 56         LD           D,(HL)
4AAC: 98         SBC         B
4AAD: 27         DAA
4AAE: 66         LD           H,(HL)
4AAF: 28 9C      JR           Z,$4A4D
4AB1: 64         LD           H,H
4AB2: E5         PUSH       HL
4AB3: FF         RST         0X38
4AB4: 15         DEC         D
4AB5: 16 32      LD           D,$32
4AB7: 9D         SBC         L
4AB8: 34         INC         (HL)
4AB9: 9D         SBC         L
4ABA: 42         LD           B,D
4ABB: 17         RLA
4ABC: FF         RST         0X38
4ABD: 00         NOP
4ABE: 66         LD           H,(HL)
4ABF: 35         DEC         (HL)
4AC0: 9C         SBC         H
4AC1: 38 86      JR           C,$4A49
4AC3: FF         RST         0X38
4AC4: 14         INC         D
4AC5: 15         DEC         D
4AC6: 33         INC         SP
4AC7: 21 36 21   LD           HL,$2136
4ACA: FF         RST         0X38
4ACB: 24         INC         H
4ACC: 39         ADD         HL,SP
4ACD: FF         RST         0X38
4ACE: 26 66      LD           H,$66
4AD0: FF         RST         0X38
4AD1: 31 17 48   LD           SP,$4817
4AD4: 16 34      LD           D,$34
4AD6: 86         ADD         A,(HL)
4AD7: 23         INC         HL
4AD8: 37         SCF
4AD9: 28 2D      JR           Z,$4B08
4ADB: FF         RST         0X38
4ADC: 57         LD           D,A
4ADD: 38 58      JR           C,$4B37
4ADF: 38 25      JR           C,$4B06
4AE1: 9B         SBC         E
4AE2: 32         LD           (HLD),A
4AE3: 9B         SBC         E
4AE4: 34         INC         (HL)
4AE5: 9B         SBC         E
4AE6: 32         LD           (HLD),A
4AE7: E5         PUSH       HL
4AE8: FF         RST         0X38
4AE9: 17         RLA
4AEA: 9E         SBC         (HL)
4AEB: FF         RST         0X38
4AEC: 34         INC         (HL)
4AED: 98         SBC         B
4AEE: 45         LD           B,L
4AEF: 98         SBC         B
4AF0: 36 2D      LD           (HL),$2D
4AF2: 43         LD           B,E
4AF3: 2D         DEC         L
4AF4: FF         RST         0X38
4AF5: 55         LD           D,L
4AF6: 42         LD           B,D
4AF7: 38 86      JR           C,$4A7F
4AF9: 14         INC         D
4AFA: 9D         SBC         L
4AFB: 32         LD           (HLD),A
4AFC: 16 42      LD           D,$42
4AFE: 17         RLA
4AFF: FF         RST         0X38
4B00: 34         INC         (HL)
4B01: 5A         LD           E,D
4B02: FF         RST         0X38
4B03: 32         LD           (HLD),A
4B04: 9D         SBC         L
4B05: 37         SCF
4B06: 9D         SBC         L
4B07: FF         RST         0X38
4B08: 25         DEC         H
4B09: 99         SBC         C
4B0A: 27         DAA
4B0B: 99         SBC         C
4B0C: 46         LD           B,(HL)
4B0D: 99         SBC         C
4B0E: 31 9C 63   LD           SP,$639C
4B11: 2D         DEC         L
4B12: FF         RST         0X38
4B13: 31 18 34   LD           SP,$3418
4B16: 18 52      JR           $4B6A
4B18: 18 11      JR           $4B2B
4B1A: 38 FF      JR           C,$4B1B
4B1C: 61         LD           H,C
4B1D: 66         LD           H,(HL)
4B1E: 27         DAA
4B1F: 21 34 21   LD           HL,$2134
4B22: 52         LD           D,D
4B23: 21 33 E5   LD           HL,$E533
4B26: FF         RST         0X38
4B27: 46         LD           B,(HL)
4B28: 9B         SBC         E
4B29: 53         LD           D,E
4B2A: 9B         SBC         E
4B2B: 11 2D 25   LD           DE,$252D
4B2E: 38 61      JR           C,$4B91
4B30: 37         SCF
4B31: FF         RST         0X38
4B32: 23         INC         HL
4B33: 9B         SBC         E
4B34: 25         DEC         H
4B35: 9B         SBC         E
4B36: 45         LD           B,L
4B37: 9B         SBC         E
4B38: 53         LD           D,E
4B39: 9B         SBC         E
4B3A: 34         INC         (HL)
4B3B: 9D         SBC         L
4B3C: FF         RST         0X38
4B3D: 22         LD           (HLI),A
4B3E: 9A         SBC         D
4B3F: FF         RST         0X38
4B40: 22         LD           (HLI),A
4B41: 17         RLA
4B42: 26 17      LD           H,$17
4B44: FF         RST         0X38
4B45: 35         DEC         (HL)
4B46: 92         SUB         D
4B47: 34         INC         (HL)
4B48: 61         LD           H,C
4B49: FF         RST         0X38
4B4A: FF         RST         0X38
4B4B: 25         DEC         H
4B4C: 60         LD           H,B
4B4D: 54         LD           D,H
4B4E: 60         LD           H,B
4B4F: FF         RST         0X38
4B50: 34         INC         (HL)
4B51: 66         LD           H,(HL)
4B52: 25         DEC         H
4B53: 8F         ADC         A,A
4B54: 54         LD           D,H
4B55: 9D         SBC         L
4B56: FF         RST         0X38
4B57: 14         INC         D
4B58: 9D         SBC         L
4B59: 22         LD           (HLI),A
4B5A: E5         PUSH       HL
4B5B: FF         RST         0X38
4B5C: 44         LD           B,H
4B5D: 52         LD           D,D
4B5E: 24         INC         H
4B5F: 9B         SBC         E
4B60: 51         LD           D,C
4B61: 9B         SBC         E
4B62: 46         LD           B,(HL)
4B63: 9B         SBC         E
4B64: 64         LD           H,H
4B65: 9B         SBC         E
4B66: FF         RST         0X38
4B67: 35         DEC         (HL)
4B68: 21 68 2A   LD           HL,$2A68
4B6B: FF         RST         0X38
4B6C: 11 9E 18   LD           DE,$189E
4B6F: 9E         SBC         (HL)
4B70: 34         INC         (HL)
4B71: 1B         DEC         DE
4B72: 35         DEC         (HL)
4B73: 1B         DEC         DE
4B74: 37         SCF
4B75: 2D         DEC         L
4B76: 42         LD           B,D
4B77: 38 FF      JR           C,$4B78
4B79: 27         DAA
4B7A: 16 22      LD           D,$22
4B7C: 99         SBC         C
4B7D: 53         LD           D,E
4B7E: 99         SBC         C
4B7F: 38 9C      JR           C,$4B1D
4B81: 17         RLA
4B82: 38 18      JR           C,$4B9C
4B84: 37         SCF
4B85: FF         RST         0X38
4B86: 34         INC         (HL)
4B87: 9D         SBC         L
4B88: 35         DEC         (HL)
4B89: 9D         SBC         L
4B8A: 18 2F      JR           $4BBB
4B8C: FF         RST         0X38
4B8D: 23         INC         HL
4B8E: 29         ADD         HL,HL
4B8F: 38 9D      JR           C,$4B2E
4B91: 63         LD           H,E
4B92: 17         RLA
4B93: FF         RST         0X38
4B94: 13         INC         DE
4B95: 9E         SBC         (HL)
4B96: 16 9E      LD           D,$9E
4B98: 43         LD           B,E
4B99: 9D         SBC         L
4B9A: 46         LD           B,(HL)
4B9B: 9D         SBC         L
4B9C: FF         RST         0X38
4B9D: 23         INC         HL
4B9E: 21 34 21   LD           HL,$2134
4BA1: 45         LD           B,L
4BA2: 21 56 21   LD           HL,$2156
4BA5: 25         DEC         H
4BA6: E5         PUSH       HL
4BA7: FF         RST         0X38
4BA8: 48         LD           C,B
4BA9: 29         ADD         HL,HL
4BAA: 38 21      JR           C,$4BCD
4BAC: 58         LD           E,B
4BAD: 21 FF 24   LD           HL,$24FF
4BB0: 21 43 21   LD           HL,$2143
4BB3: 45         LD           B,L
4BB4: 21 FF 34   LD           HL,$34FF
4BB7: 61         LD           H,C
4BB8: FF         RST         0X38
4BB9: 43         LD           B,E
4BBA: 9D         SBC         L
4BBB: 46         LD           B,(HL)
4BBC: 9D         SBC         L
4BBD: 13         INC         DE
4BBE: 27         DAA
4BBF: 16 27      LD           D,$27
4BC1: FF         RST         0X38
4BC2: 00         NOP
4BC3: 9A         SBC         D
4BC4: FF         RST         0X38
4BC5: 32         LD           (HLD),A
4BC6: 9C         SBC         H
4BC7: 36 9C      LD           (HL),$9C
4BC9: 68         LD           L,B
4BCA: 27         DAA
4BCB: 11 2D FF   LD           DE,$FF2D
4BCE: 25         DEC         H
4BCF: DB                              
4BD0: 64         LD           H,H
4BD1: 9F         SBC         A
4BD2: 66         LD           H,(HL)
4BD3: 9F         SBC         A
4BD4: FF         RST         0X38
4BD5: 12         LD           (DE),A
4BD6: DB                              
4BD7: 64         LD           H,H
4BD8: 9F         SBC         A
4BD9: FF         RST         0X38
4BDA: FF         RST         0X38
4BDB: 25         DEC         H
4BDC: 17         RLA
4BDD: 53         LD           D,E
4BDE: 16 66      LD           D,$66
4BE0: 9F         SBC         A
4BE1: FF         RST         0X38
4BE2: 24         INC         H
4BE3: D7         RST         0X10
4BE4: 25         DEC         H
4BE5: D7         RST         0X10
4BE6: 26 D7      LD           H,$D7
4BE8: 27         DAA
4BE9: D7         RST         0X10
4BEA: FF         RST         0X38
4BEB: 22         LD           (HLI),A
4BEC: D7         RST         0X10
4BED: 24         INC         H
4BEE: D7         RST         0X10
4BEF: 33         INC         SP
4BF0: D7         RST         0X10
4BF1: FF         RST         0X38
4BF2: FF         RST         0X38
4BF3: FF         RST         0X38
4BF4: 34         INC         (HL)
4BF5: CA FF 68   JP           Z,$68FF
4BF8: 3D         DEC         A
4BF9: FF         RST         0X38
4BFA: 34         INC         (HL)
4BFB: DC FF 55   CALL       C,$55FF
4BFE: CC FF 53   CALL       Z,$53FF
4C01: CC FF FF   CALL       Z,$FFFF
4C04: 14         INC         D
4C05: 35         DEC         (HL)
4C06: FF         RST         0X38
4C07: FF         RST         0X38
4C08: FF         RST         0X38
4C09: FF         RST         0X38
4C0A: 62         LD           H,D
4C0B: 9F         SBC         A
4C0C: 64         LD           H,H
4C0D: 9F         SBC         A
4C0E: FF         RST         0X38
4C0F: FF         RST         0X38
4C10: 08 E2 FF   LD           ($FFE2),SP
4C13: FF         RST         0X38
4C14: FF         RST         0X38
4C15: 53         LD           D,E
4C16: CC 64 CC   CALL       Z,$CC64
4C19: FF         RST         0X38
4C1A: FF         RST         0X38
4C1B: 24         INC         H
4C1C: 84         ADD         A,H
4C1D: FF         RST         0X38
4C1E: FF         RST         0X38
4C1F: 14         INC         D
4C20: 8F         ADC         A,A
4C21: FF         RST         0X38
4C22: 15         DEC         D
4C23: CC FF FF   CALL       Z,$FFFF
4C26: 34         INC         (HL)
4C27: 30 38      JR           NC,$4C61
4C29: B0         OR           B
4C2A: 42         LD           B,D
4C2B: B0         OR           B
4C2C: 62         LD           H,D
4C2D: B0         OR           B
4C2E: FF         RST         0X38
4C2F: FF         RST         0X38
4C30: 21 DD 23   LD           HL,$23DD
4C33: DD                              
4C34: 26 DD      LD           H,$DD
4C36: 28 DD      JR           Z,$4C15
4C38: 51         LD           D,C
4C39: DD                              
4C3A: 53         LD           D,E
4C3B: DD                              
4C3C: 56         LD           D,(HL)
4C3D: DD                              
4C3E: 58         LD           E,B
4C3F: DD                              
4C40: FF         RST         0X38
4C41: 24         INC         H
4C42: 84         ADD         A,H
4C43: FF         RST         0X38
4C44: 14         INC         D
4C45: 14         INC         D
4C46: 23         INC         HL
4C47: 0B         DEC         BC
4C48: 26 0B      LD           H,$0B
4C4A: FF         RST         0X38
4C4B: FF         RST         0X38
4C4C: FF         RST         0X38
4C4D: 26 65      LD           H,$65
4C4F: FF         RST         0X38
4C50: FF         RST         0X38
4C51: 33         INC         SP
4C52: 91         SUB         C
4C53: 57         LD           D,A
4C54: 9F         SBC         A
4C55: FF         RST         0X38
4C56: 55         LD           D,L
4C57: 29         ADD         HL,HL
4C58: 43         LD           B,E
4C59: A0         AND         B
4C5A: 58         LD           E,B
4C5B: A0         AND         B
4C5C: FF         RST         0X38
4C5D: 41         LD           B,C
4C5E: A0         AND         B
4C5F: 47         LD           B,A
4C60: A0         AND         B
4C61: 54         LD           D,H
4C62: 2A         LD           A,(HLI)
4C63: FF         RST         0X38
4C64: 51         LD           D,C
4C65: 91         SUB         C
4C66: 44         LD           B,H
4C67: 2A         LD           A,(HLI)
4C68: 36 16      LD           (HL),$16
4C6A: FF         RST         0X38
4C6B: FF         RST         0X38
4C6C: 22         LD           (HLI),A
4C6D: E5         PUSH       HL
4C6E: FF         RST         0X38
4C6F: 45         LD           B,L
4C70: 1E 26      LD           E,$26
4C72: 23         INC         HL
4C73: 42         LD           B,D
4C74: 23         INC         HL
4C75: FF         RST         0X38
4C76: 04         INC         B
4C77: 9E         SBC         (HL)
4C78: 54         LD           D,H
4C79: 66         LD           H,(HL)
4C7A: FF         RST         0X38
4C7B: FF         RST         0X38
4C7C: 47         LD           B,A
4C7D: 1F         RRA
4C7E: 25         DEC         H
4C7F: 1F         RRA
4C80: 65         LD           H,L
4C81: 17         RLA
4C82: FF         RST         0X38
4C83: FF         RST         0X38
4C84: 11 27 61   LD           DE,$6127
4C87: 27         DAA
4C88: 33         INC         SP
4C89: 1F         RRA
4C8A: FF         RST         0X38
4C8B: 45         LD           B,L
4C8C: 21 25 38   LD           HL,$3825
4C8F: 36 38      LD           (HL),$38
4C91: FF         RST         0X38
4C92: 34         INC         (HL)
4C93: 61         LD           H,C
4C94: FF         RST         0X38
4C95: 11 27 18   LD           DE,$1827
4C98: 27         DAA
4C99: FF         RST         0X38
4C9A: 00         NOP
4C9B: 9E         SBC         (HL)
4C9C: 23         INC         HL
4C9D: 23         INC         HL
4C9E: 35         DEC         (HL)
4C9F: 15         DEC         D
4CA0: 46         LD           B,(HL)
4CA1: 23         INC         HL
4CA2: FF         RST         0X38
4CA3: 31 90 48   LD           SP,$4890
4CA6: 90         SUB         B
4CA7: 65         LD           H,L
4CA8: 90         SUB         B
4CA9: FF         RST         0X38
4CAA: 42         LD           B,D
4CAB: 98         SBC         B
4CAC: 47         LD           B,A
4CAD: 98         SBC         B
4CAE: 65         LD           H,L
4CAF: 15         DEC         D
4CB0: FF         RST         0X38
4CB1: 11 9A 16   LD           DE,$169A
4CB4: 15         DEC         D
4CB5: FF         RST         0X38
4CB6: 35         DEC         (HL)
4CB7: A7         AND         A
4CB8: FF         RST         0X38
4CB9: 22         LD           (HLI),A
4CBA: 9B         SBC         E
4CBB: 34         INC         (HL)
4CBC: A7         AND         A
4CBD: 45         LD           B,L
4CBE: 9B         SBC         E
4CBF: 17         RLA
4CC0: 1B         DEC         DE
4CC1: FF         RST         0X38
4CC2: 08 69 01   LD           ($0169),SP
4CC5: 42         LD           B,D
4CC6: 21 46 51   LD           HL,$5146
4CC9: 47         LD           B,A
4CCA: FF         RST         0X38
4CCB: 12         LD           (DE),A
4CCC: 16 25      LD           D,$25
4CCE: 17         RLA
4CCF: 33         INC         SP
4CD0: 9B         SBC         E
4CD1: 57         LD           D,A
4CD2: 9B         SBC         E
4CD3: FF         RST         0X38
4CD4: 45         LD           B,L
4CD5: A7         AND         A
4CD6: 37         SCF
4CD7: 9B         SBC         E
4CD8: 54         LD           D,H
4CD9: 9B         SBC         E
4CDA: FF         RST         0X38
4CDB: 44         LD           B,H
4CDC: A7         AND         A
4CDD: 52         LD           D,D
4CDE: 9B         SBC         E
4CDF: 56         LD           D,(HL)
4CE0: E5         PUSH       HL
4CE1: FF         RST         0X38
4CE2: 68         LD           L,B
4CE3: 66         LD           H,(HL)
4CE4: FF         RST         0X38
4CE5: 61         LD           H,C
4CE6: 9E         SBC         (HL)
4CE7: 68         LD           L,B
4CE8: 9E         SBC         (HL)
4CE9: 34         INC         (HL)
4CEA: 89         ADC         A,C
4CEB: FF         RST         0X38
4CEC: 52         LD           D,D
4CED: 90         SUB         B
4CEE: 56         LD           D,(HL)
4CEF: 90         SUB         B
4CF0: 64         LD           H,H
4CF1: 90         SUB         B
4CF2: FF         RST         0X38
4CF3: 24         INC         H
4CF4: 66         LD           H,(HL)
4CF5: 37         SCF
4CF6: 9B         SBC         E
4CF7: 63         LD           H,E
4CF8: 9B         SBC         E
4CF9: FF         RST         0X38
4CFA: 56         LD           D,(HL)
4CFB: 15         DEC         D
4CFC: FF         RST         0X38
4CFD: 22         LD           (HLI),A
4CFE: A0         AND         B
4CFF: 27         DAA
4D00: A0         AND         B
4D01: 34         INC         (HL)
4D02: 2A         LD           A,(HLI)
4D03: 51         LD           D,C
4D04: 27         DAA
4D05: 58         LD           E,B
4D06: 27         DAA
4D07: FF         RST         0X38
4D08: 15         DEC         D
4D09: 98         SBC         B
4D0A: 23         INC         HL
4D0B: 98         SBC         B
4D0C: 45         LD           B,L
4D0D: 1B         DEC         DE
4D0E: 57         LD           D,A
4D0F: 2A         LD           A,(HLI)
4D10: FF         RST         0X38
4D11: 22         LD           (HLI),A
4D12: 9F         SBC         A
4D13: 15         DEC         D
4D14: 16 34      LD           D,$34
4D16: 2A         LD           A,(HLI)
4D17: 47         LD           B,A
4D18: A0         AND         B
4D19: FF         RST         0X38
4D1A: FF         RST         0X38
4D1B: FF         RST         0X38
4D1C: 21 66 26   LD           HL,$2666
4D1F: 17         RLA
4D20: 51         LD           D,C
4D21: 17         RLA
4D22: 58         LD           E,B
4D23: 17         RLA
4D24: FF         RST         0X38
4D25: 15         DEC         D
4D26: 21 35 21   LD           HL,$2135
4D29: 43         LD           B,E
4D2A: 2A         LD           A,(HLI)
4D2B: 66         LD           H,(HL)
4D2C: 15         DEC         D
4D2D: FF         RST         0X38
4D2E: FF         RST         0X38
4D2F: FF         RST         0X38
4D30: 04         INC         B
4D31: BC         CP           H
4D32: 34         INC         (HL)
4D33: 61         LD           H,C
4D34: FF         RST         0X38
4D35: 34         INC         (HL)
4D36: A0         AND         B
4D37: 51         LD           D,C
4D38: A0         AND         B
4D39: 63         LD           H,E
4D3A: 15         DEC         D
4D3B: 56         LD           D,(HL)
4D3C: A1         AND         C
4D3D: FF         RST         0X38
4D3E: 23         INC         HL
4D3F: A0         AND         B
4D40: 47         LD           B,A
4D41: 24         INC         H
4D42: 64         LD           H,H
4D43: 24         INC         H
4D44: 34         INC         (HL)
4D45: 86         ADD         A,(HL)
4D46: FF         RST         0X38
4D47: 25         DEC         H
4D48: 9F         SBC         A
4D49: 48         LD           C,B
4D4A: 9F         SBC         A
4D4B: 54         LD           D,H
4D4C: 9F         SBC         A
4D4D: FF         RST         0X38
4D4E: 24         INC         H
4D4F: 39         ADD         HL,SP
4D50: FF         RST         0X38
4D51: 25         DEC         H
4D52: 9F         SBC         A
4D53: 47         LD           B,A
4D54: 9F         SBC         A
4D55: 52         LD           D,D
4D56: 9F         SBC         A
4D57: 57         LD           D,A
4D58: 9F         SBC         A
4D59: FF         RST         0X38
4D5A: FF         RST         0X38
4D5B: FF         RST         0X38
4D5C: 24         INC         H
4D5D: 39         ADD         HL,SP
4D5E: FF         RST         0X38
4D5F: FF         RST         0X38
4D60: 52         LD           D,D
4D61: B1         OR           C
4D62: FF         RST         0X38
4D63: FF         RST         0X38
4D64: 34         INC         (HL)
4D65: 62         LD           H,D
4D66: FF         RST         0X38
4D67: 47         LD           B,A
4D68: E5         PUSH       HL
4D69: 56         LD           D,(HL)
4D6A: E5         PUSH       HL
4D6B: 27         DAA
4D6C: 86         ADD         A,(HL)
4D6D: 36 86      LD           (HL),$86
4D6F: FF         RST         0X38
4D70: FF         RST         0X38
4D71: FF         RST         0X38
4D72: 11 8E FF   LD           DE,$FF8E
4D75: FF         RST         0X38
4D76: 32         LD           (HLD),A
4D77: BD         CP           L
4D78: 33         INC         SP
4D79: A1         AND         C
4D7A: 54         LD           D,H
4D7B: A1         AND         C
4D7C: 62         LD           H,D
4D7D: 37         SCF
4D7E: 65         LD           H,L
4D7F: 2F         CPL
4D80: 66         LD           H,(HL)
4D81: 37         SCF
4D82: FF         RST         0X38
4D83: 31 E5 FF   LD           SP,$FFE5
4D86: 11 9B 21   LD           DE,$219B
4D89: 9B         SBC         E
4D8A: 23         INC         HL
4D8B: 9B         SBC         E
4D8C: 34         INC         (HL)
4D8D: 9B         SBC         E
4D8E: FF         RST         0X38
4D8F: 32         LD           (HLD),A
4D90: 60         LD           H,B
4D91: 55         LD           D,L
4D92: 60         LD           H,B
4D93: FF         RST         0X38
4D94: 16 E5      LD           D,$E5
4D96: 34         INC         (HL)
4D97: 1F         RRA
4D98: 36 1F      LD           (HL),$1F
4D9A: 25         DEC         H
4D9B: 86         ADD         A,(HL)
4D9C: FF         RST         0X38
4D9D: 35         DEC         (HL)
4D9E: BE         CP           (HL)
4D9F: 34         INC         (HL)
4DA0: 61         LD           H,C
4DA1: FF         RST         0X38
4DA2: 63         LD           H,E
4DA3: 2A         LD           A,(HLI)
4DA4: FF         RST         0X38
4DA5: 33         INC         SP
4DA6: 17         RLA
4DA7: 36 17      LD           (HL),$17
4DA9: FF         RST         0X38
4DAA: 14         INC         D
4DAB: A1         AND         C
4DAC: 34         INC         (HL)
4DAD: A0         AND         B
4DAE: 56         LD           D,(HL)
4DAF: A1         AND         C
4DB0: FF         RST         0X38
4DB1: 34         INC         (HL)
4DB2: A1         AND         C
4DB3: FF         RST         0X38
4DB4: 16 16      LD           D,$16
4DB6: 17         RLA
4DB7: 16 42      LD           D,$42
4DB9: 9B         SBC         E
4DBA: 52         LD           D,D
4DBB: 9B         SBC         E
4DBC: FF         RST         0X38
4DBD: 23         INC         HL
4DBE: 9B         SBC         E
4DBF: 26 9B      LD           H,$9B
4DC1: 53         LD           D,E
4DC2: 9B         SBC         E
4DC3: 56         LD           D,(HL)
4DC4: 9B         SBC         E
4DC5: 38 86      JR           C,$4D4D
4DC7: FF         RST         0X38
4DC8: 31 A1 38   LD           SP,$38A1
4DCB: A1         AND         C
4DCC: FF         RST         0X38
4DCD: 32         LD           (HLD),A
4DCE: 86         ADD         A,(HL)
4DCF: 43         LD           B,E
4DD0: E5         PUSH       HL
4DD1: 52         LD           D,D
4DD2: E5         PUSH       HL
4DD3: FF         RST         0X38
4DD4: 23         INC         HL
4DD5: A0         AND         B
4DD6: 45         LD           B,L
4DD7: A0         AND         B
4DD8: 27         DAA
4DD9: A0         AND         B
4DDA: FF         RST         0X38
4DDB: FF         RST         0X38
4DDC: 23         INC         HL
4DDD: BD         CP           L
4DDE: 36 E5      LD           (HL),$E5
4DE0: FF         RST         0X38
4DE1: 11 27 18   LD           DE,$1827
4DE4: 27         DAA
4DE5: 61         LD           H,C
4DE6: 27         DAA
4DE7: 68         LD           L,B
4DE8: 27         DAA
4DE9: 47         LD           B,A
4DEA: 1E FF      LD           E,$FF
4DEC: 16 16      LD           D,$16
4DEE: 34         INC         (HL)
4DEF: BD         CP           L
4DF0: FF         RST         0X38
4DF1: 36 B1      LD           (HL),$B1
4DF3: FF         RST         0X38
4DF4: 34         INC         (HL)
4DF5: 89         ADC         A,C
4DF6: FF         RST         0X38
4DF7: 22         LD           (HLI),A
4DF8: 9B         SBC         E
4DF9: 24         INC         H
4DFA: 9B         SBC         E
4DFB: FF         RST         0X38
4DFC: 53         LD           D,E
4DFD: B1         OR           C
4DFE: FF         RST         0X38
4DFF: 68         LD           L,B
4E00: E5         PUSH       HL
4E01: FF         RST         0X38
4E02: 34         INC         (HL)
4E03: 66         LD           H,(HL)
4E04: FF         RST         0X38
4E05: 51         LD           D,C
4E06: 42         LD           B,D
4E07: 18 2A      JR           $4E33
4E09: 34         INC         (HL)
4E0A: 9B         SBC         E
4E0B: 55         LD           D,L
4E0C: 9B         SBC         E
4E0D: FF         RST         0X38
4E0E: 31 81 33   LD           SP,$3381
4E11: 82         ADD         A,D
4E12: FF         RST         0X38
4E13: 46         LD           B,(HL)
4E14: 17         RLA
4E15: 47         LD           B,A
4E16: 16 62      LD           D,$62
4E18: E5         PUSH       HL
4E19: FF         RST         0X38
4E1A: 22         LD           (HLI),A
4E1B: A1         AND         C
4E1C: 41         LD           B,C
4E1D: A1         AND         C
4E1E: 45         LD           B,L
4E1F: A1         AND         C
4E20: 54         LD           D,H
4E21: 2A         LD           A,(HLI)
4E22: FF         RST         0X38
4E23: 44         LD           B,H
4E24: BD         CP           L
4E25: FF         RST         0X38
4E26: 13         INC         DE
4E27: 16 46      LD           D,$46
4E29: 16 45      LD           D,$45
4E2B: 86         ADD         A,(HL)
4E2C: 68         LD           L,B
4E2D: 2F         CPL
4E2E: FF         RST         0X38
4E2F: FF         RST         0X38
4E30: 47         LD           B,A
4E31: B1         OR           C
4E32: 42         LD           B,D
4E33: 9B         SBC         E
4E34: 53         LD           D,E
4E35: 9B         SBC         E
4E36: 34         INC         (HL)
4E37: E5         PUSH       HL
4E38: FF         RST         0X38
4E39: 34         INC         (HL)
4E3A: 92         SUB         D
4E3B: FF         RST         0X38
4E3C: 33         INC         SP
4E3D: 9B         SBC         E
4E3E: 35         DEC         (HL)
4E3F: 9B         SBC         E
4E40: 44         LD           B,H
4E41: 9B         SBC         E
4E42: 67         LD           H,A
4E43: 52         LD           D,D
4E44: FF         RST         0X38
4E45: 34         INC         (HL)
4E46: 61         LD           H,C
4E47: FF         RST         0X38
4E48: 26 28      LD           H,$28
4E4A: 53         LD           D,E
4E4B: 28 61      JR           Z,$4EAE
4E4D: 9E         SBC         (HL)
4E4E: 68         LD           L,B
4E4F: 9E         SBC         (HL)
4E50: FF         RST         0X38
4E51: 15         DEC         D
4E52: A1         AND         C
4E53: 33         INC         SP
4E54: A1         AND         C
4E55: 37         SCF
4E56: A1         AND         C
4E57: 45         LD           B,L
4E58: A1         AND         C
4E59: FF         RST         0X38
4E5A: 13         INC         DE
4E5B: 9F         SBC         A
4E5C: 16 9F      LD           D,$9F
4E5E: FF         RST         0X38
4E5F: 43         LD           B,E
4E60: 9F         SBC         A
4E61: 45         LD           B,L
4E62: 9F         SBC         A
4E63: FF         RST         0X38
4E64: FF         RST         0X38
4E65: 53         LD           D,E
4E66: 9F         SBC         A
4E67: FF         RST         0X38
4E68: 43         LD           B,E
4E69: A3         AND         E
4E6A: 64         LD           H,H
4E6B: DA 67 DA   JP           C,$DA67
4E6E: FF         RST         0X38
4E6F: 32         LD           (HLD),A
4E70: A4         AND         H
4E71: 55         LD           D,L
4E72: A4         AND         H
4E73: 64         LD           H,H
4E74: DA 67 DA   JP           C,$DA67
4E77: FF         RST         0X38
4E78: 33         INC         SP
4E79: 9F         SBC         A
4E7A: 65         LD           H,L
4E7B: 9F         SBC         A
4E7C: FF         RST         0X38
4E7D: 63         LD           H,E
4E7E: DA 65 DA   JP           C,$DA65
4E81: FF         RST         0X38
4E82: 33         INC         SP
4E83: A4         AND         H
4E84: 26 17      LD           H,$17
4E86: 67         LD           H,A
4E87: 9F         SBC         A
4E88: FF         RST         0X38
4E89: 53         LD           D,E
4E8A: A3         AND         E
4E8B: 57         LD           D,A
4E8C: 9F         SBC         A
4E8D: FF         RST         0X38
4E8E: 63         LD           H,E
4E8F: DA 65 DA   JP           C,$DA65
4E92: 67         LD           H,A
4E93: DA FF 63   JP           C,$63FF
4E96: DA 65 DA   JP           C,$DA65
4E99: FF         RST         0X38
4E9A: FF         RST         0X38
4E9B: FF         RST         0X38
4E9C: FF         RST         0X38
4E9D: 04         INC         B
4E9E: 42         LD           B,D
4E9F: FF         RST         0X38
4EA0: FF         RST         0X38
4EA1: FF         RST         0X38
4EA2: FF         RST         0X38
4EA3: FF         RST         0X38
4EA4: 34         INC         (HL)
4EA5: E6 FF      AND         $FF
4EA7: FF         RST         0X38
4EA8: FF         RST         0X38
4EA9: FF         RST         0X38
4EAA: FF         RST         0X38
4EAB: FF         RST         0X38
4EAC: 24         INC         H
4EAD: 30 FF      JR           NC,$4EAE
4EAF: FF         RST         0X38
4EB0: FF         RST         0X38
4EB1: FF         RST         0X38
4EB2: FF         RST         0X38
4EB3: 34         INC         (HL)
4EB4: 88         ADC         A,B
4EB5: FF         RST         0X38
4EB6: 05         DEC         B
4EB7: 19         ADD         HL,DE
4EB8: 13         INC         DE
4EB9: 19         ADD         HL,DE
4EBA: 22         LD           (HLI),A
4EBB: 19         ADD         HL,DE
4EBC: 34         INC         (HL)
4EBD: 19         ADD         HL,DE
4EBE: FF         RST         0X38
4EBF: 13         INC         DE
4EC0: 9B         SBC         E
4EC1: 14         INC         D
4EC2: 9B         SBC         E
4EC3: 15         DEC         D
4EC4: 9B         SBC         E
4EC5: FF         RST         0X38
4EC6: 04         INC         B
4EC7: 19         ADD         HL,DE
4EC8: 16 19      LD           D,$19
4ECA: 34         INC         (HL)
4ECB: 19         ADD         HL,DE
4ECC: 37         SCF
4ECD: 19         ADD         HL,DE
4ECE: FF         RST         0X38
4ECF: FF         RST         0X38
4ED0: FF         RST         0X38
4ED1: 48         LD           C,B
4ED2: 9B         SBC         E
4ED3: FF         RST         0X38
4ED4: 36 20      LD           (HL),$20
4ED6: 34         INC         (HL)
4ED7: 9B         SBC         E
4ED8: 47         LD           B,A
4ED9: 9B         SBC         E
4EDA: 42         LD           B,D
4EDB: 20 FF      JR           NZ,$4EDC
4EDD: 41         LD           B,C
4EDE: 9B         SBC         E
4EDF: 51         LD           D,C
4EE0: 9B         SBC         E
4EE1: FF         RST         0X38
4EE2: 25         DEC         H
4EE3: 9B         SBC         E
4EE4: 27         DAA
4EE5: 9B         SBC         E
4EE6: 45         LD           B,L
4EE7: 9B         SBC         E
4EE8: 47         LD           B,A
4EE9: 9B         SBC         E
4EEA: FF         RST         0X38
4EEB: 33         INC         SP
4EEC: 19         ADD         HL,DE
4EED: 35         DEC         (HL)
4EEE: 9B         SBC         E
4EEF: FF         RST         0X38
4EF0: FF         RST         0X38
4EF1: 23         INC         HL
4EF2: 19         ADD         HL,DE
4EF3: 26 19      LD           H,$19
4EF5: 43         LD           B,E
4EF6: 19         ADD         HL,DE
4EF7: 46         LD           B,(HL)
4EF8: 19         ADD         HL,DE
4EF9: FF         RST         0X38
4EFA: 44         LD           B,H
4EFB: 9B         SBC         E
4EFC: 45         LD           B,L
4EFD: 9B         SBC         E
4EFE: FF         RST         0X38
4EFF: FF         RST         0X38
4F00: 17         RLA
4F01: BB         CP           E
4F02: 42         LD           B,D
4F03: 20 36      JR           NZ,$4F3B
4F05: 19         ADD         HL,DE
4F06: 38 19      JR           C,$4F21
4F08: FF         RST         0X38
4F09: 43         LD           B,E
4F0A: 37         SCF
4F0B: 46         LD           B,(HL)
4F0C: 37         SCF
4F0D: FF         RST         0X38
4F0E: FF         RST         0X38
4F0F: 16 19      LD           D,$19
4F11: 25         DEC         H
4F12: BB         CP           E
4F13: 53         LD           D,E
4F14: BB         CP           E
4F15: 66         LD           H,(HL)
4F16: 9B         SBC         E
4F17: FF         RST         0X38
4F18: 32         LD           (HLD),A
4F19: 9B         SBC         E
4F1A: 45         LD           B,L
4F1B: BB         CP           E
4F1C: FF         RST         0X38
4F1D: 21 BB 24   LD           HL,$24BB
4F20: 9B         SBC         E
4F21: 37         SCF
4F22: BB         CP           E
4F23: 43         LD           B,E
4F24: 9B         SBC         E
4F25: FF         RST         0X38
4F26: 27         DAA
4F27: 9B         SBC         E
4F28: FF         RST         0X38
4F29: 15         DEC         D
4F2A: 9B         SBC         E
4F2B: 45         LD           B,L
4F2C: 9B         SBC         E
4F2D: 52         LD           D,D
4F2E: 9B         SBC         E
4F2F: FF         RST         0X38
4F30: 52         LD           D,D
4F31: 9B         SBC         E
4F32: FF         RST         0X38
4F33: 14         INC         D
4F34: AF         XOR         A
4F35: 11 2D 21   LD           DE,$212D
4F38: 2D         DEC         L
4F39: 31 2D 18   LD           SP,$182D
4F3C: 2D         DEC         L
4F3D: 28 2D      JR           Z,$4F6C
4F3F: 38 2D      JR           C,$4F6E
4F41: FF         RST         0X38
4F42: 22         LD           (HLI),A
4F43: 1B         DEC         DE
4F44: 48         LD           C,B
4F45: 1B         DEC         DE
4F46: 53         LD           D,E
4F47: 1B         DEC         DE
4F48: 25         DEC         H
4F49: 28 41      JR           Z,$4F8C
4F4B: 28 FF      JR           Z,$4F4C
4F4D: 55         LD           D,L
4F4E: 80         ADD         A,B
4F4F: FF         RST         0X38
4F50: 21 20 FF   LD           HL,$FF20
4F53: 55         LD           D,L
4F54: 80         ADD         A,B
4F55: FF         RST         0X38
4F56: 55         LD           D,L
4F57: 80         ADD         A,B
4F58: FF         RST         0X38
4F59: 55         LD           D,L
4F5A: 80         ADD         A,B
4F5B: FF         RST         0X38
4F5C: FF         RST         0X38
4F5D: 26 DC      LD           H,$DC
4F5F: 17         RLA
4F60: 6C         LD           L,H
4F61: 36 6C      LD           (HL),$6C
4F63: 44         LD           B,H
4F64: 6C         LD           L,H
4F65: FF         RST         0X38
4F66: 68         LD           L,B
4F67: 4F         LD           C,A
4F68: FF         RST         0X38
4F69: 57         LD           D,A
4F6A: 4D         LD           C,L
4F6B: FF         RST         0X38
4F6C: 44         LD           B,H
4F6D: 40         LD           B,B
4F6E: 17         RLA
4F6F: 2D         DEC         L
4F70: 21 2D 23   LD           HL,$232D
4F73: 2D         DEC         L
4F74: 61         LD           H,C
4F75: 2D         DEC         L
4F76: 32         LD           (HLD),A
4F77: 3B         DEC         SP
4F78: 37         SCF
4F79: 3B         DEC         SP
4F7A: 24         INC         H
4F7B: E1         POP         HL
4F7C: FF         RST         0X38
4F7D: 35         DEC         (HL)
4F7E: 3E 47      LD           A,$47
4F80: 3F         CCF
4F81: 61         LD           H,C
4F82: 2D         DEC         L
4F83: 62         LD           H,D
4F84: 2D         DEC         L
4F85: FF         RST         0X38
4F86: 44         LD           B,H
4F87: 35         DEC         (HL)
4F88: FF         RST         0X38
4F89: 23         INC         HL
4F8A: 2E FF      LD           L,$FF
4F8C: 32         LD           (HLD),A
4F8D: 74         LD           (HL),H
4F8E: 24         INC         H
4F8F: B6         OR           (HL)
4F90: FF         RST         0X38
4F91: 22         LD           (HLI),A
4F92: 78         LD           A,B
4F93: 34         INC         (HL)
4F94: 79         LD           A,C
4F95: FF         RST         0X38
4F96: 34         INC         (HL)
4F97: 76         HALT
4F98: 26 85      LD           H,$85
4F9A: FF         RST         0X38
4F9B: 22         LD           (HLI),A
4F9C: 80         ADD         A,B
4F9D: 44         LD           B,H
4F9E: 77         LD           (HL),A
4F9F: FF         RST         0X38
4FA0: 35         DEC         (HL)
4FA1: 83         ADD         A,E
4FA2: FF         RST         0X38
4FA3: 33         INC         SP
4FA4: 35         DEC         (HL)
4FA5: FF         RST         0X38
4FA6: 33         INC         SP
4FA7: 9B         SBC         E
4FA8: 44         LD           B,H
4FA9: 9B         SBC         E
4FAA: FF         RST         0X38
4FAB: 24         INC         H
4FAC: 7B         LD           A,E
4FAD: 36 E1      LD           (HL),$E1
4FAF: 52         LD           D,D
4FB0: E1         POP         HL
4FB1: FF         RST         0X38
4FB2: 31 9B 53   LD           SP,$539B
4FB5: 9B         SBC         E
4FB6: FF         RST         0X38
4FB7: 54         LD           D,H
4FB8: 9B         SBC         E
4FB9: 55         LD           D,L
4FBA: 9B         SBC         E
4FBB: 56         LD           D,(HL)
4FBC: 9B         SBC         E
4FBD: FF         RST         0X38
4FBE: 58         LD           E,B
4FBF: 6A         LD           L,D
4FC0: FF         RST         0X38
4FC1: 37         SCF
4FC2: 54         LD           D,H
4FC3: FF         RST         0X38
4FC4: 44         LD           B,H
4FC5: 78         LD           A,B
4FC6: 66         LD           H,(HL)
4FC7: 3D         DEC         A
4FC8: FF         RST         0X38
4FC9: FF         RST         0X38
4FCA: 55         LD           D,L
4FCB: 80         ADD         A,B
4FCC: FF         RST         0X38
4FCD: FF         RST         0X38
4FCE: 27         DAA
4FCF: 19         ADD         HL,DE
4FD0: 34         INC         (HL)
4FD1: 19         ADD         HL,DE
4FD2: 35         DEC         (HL)
4FD3: 20 58      JR           NZ,$502D
4FD5: 19         ADD         HL,DE
4FD6: FF         RST         0X38
4FD7: 14         INC         D
4FD8: 9B         SBC         E
4FD9: 20 9E      JR           NZ,$4F79
4FDB: 55         LD           D,L
4FDC: 9B         SBC         E
4FDD: FF         RST         0X38
4FDE: 26 19      LD           H,$19
4FE0: 27         DAA
4FE1: 19         ADD         HL,DE
4FE2: 46         LD           B,(HL)
4FE3: 9B         SBC         E
4FE4: FF         RST         0X38
4FE5: 22         LD           (HLI),A
4FE6: 19         ADD         HL,DE
4FE7: 24         INC         H
4FE8: 19         ADD         HL,DE
4FE9: 33         INC         SP
4FEA: 9B         SBC         E
4FEB: FF         RST         0X38
4FEC: 33         INC         SP
4FED: 35         DEC         (HL)
4FEE: FF         RST         0X38
4FEF: 37         SCF
4FF0: 9B         SBC         E
4FF1: 42         LD           B,D
4FF2: 9B         SBC         E
4FF3: FF         RST         0X38
4FF4: 37         SCF
4FF5: 9B         SBC         E
4FF6: 45         LD           B,L
4FF7: 9B         SBC         E
4FF8: 68         LD           L,B
4FF9: 9B         SBC         E
4FFA: FF         RST         0X38
4FFB: 25         DEC         H
4FFC: 19         ADD         HL,DE
4FFD: 26 19      LD           H,$19
4FFF: 22         LD           (HLI),A
5000: 19         ADD         HL,DE
5001: 52         LD           D,D
5002: 19         ADD         HL,DE
5003: FF         RST         0X38
5004: 14         INC         D
5005: 28 17      JR           Z,$501E
5007: 28 31      JR           Z,$503A
5009: 28 51      JR           Z,$505C
500B: 28 FF      JR           Z,$500C
500D: 13         INC         DE
500E: 28 14      JR           Z,$5024
5010: 28 15      JR           Z,$5027
5012: 28 28      JR           Z,$503C
5014: 28 48      JR           Z,$505E
5016: 28 FF      JR           Z,$5017
5018: FF         RST         0X38
5019: FF         RST         0X38
501A: 53         LD           D,E
501B: 0B         DEC         BC
501C: 66         LD           H,(HL)
501D: 14         INC         D
501E: FF         RST         0X38
501F: 00         NOP
5020: E7         RST         0X20
5021: 56         LD           D,(HL)
5022: 0B         DEC         BC
5023: 64         LD           H,H
5024: 19         ADD         HL,DE
5025: FF         RST         0X38
5026: FF         RST         0X38
5027: 32         LD           (HLD),A
5028: 94         SUB         H
5029: 37         SCF
502A: 94         SUB         H
502B: 64         LD           H,H
502C: 17         RLA
502D: FF         RST         0X38
502E: 26 51      LD           H,$51
5030: FF         RST         0X38
5031: 16 95      LD           D,$95
5033: 62         LD           H,D
5034: 96         SUB         (HL)
5035: 43         LD           B,E
5036: 96         SUB         (HL)
5037: 56         LD           D,(HL)
5038: 96         SUB         (HL)
5039: 48         LD           C,B
503A: 96         SUB         (HL)
503B: FF         RST         0X38
503C: 32         LD           (HLD),A
503D: 9B         SBC         E
503E: 37         SCF
503F: 9B         SBC         E
5040: FF         RST         0X38
5041: 33         INC         SP
5042: 9B         SBC         E
5043: FF         RST         0X38
5044: 45         LD           B,L
5045: BB         CP           E
5046: 62         LD           H,D
5047: 9B         SBC         E
5048: 64         LD           H,H
5049: 9B         SBC         E
504A: FF         RST         0X38
504B: 55         LD           D,L
504C: 80         ADD         A,B
504D: FF         RST         0X38
504E: 55         LD           D,L
504F: 80         ADD         A,B
5050: FF         RST         0X38
5051: 21 9B 27   LD           HL,$279B
5054: 9B         SBC         E
5055: 43         LD           B,E
5056: 9B         SBC         E
5057: 48         LD           C,B
5058: 9B         SBC         E
5059: FF         RST         0X38
505A: 41         LD           B,C
505B: 28 FF      JR           Z,$505C
505D: 18 28      JR           $5087
505F: 28 28      JR           Z,$5089
5061: 38 28      JR           C,$508B
5063: 48         LD           C,B
5064: 28 FF      JR           Z,$5065
5066: 46         LD           B,(HL)
5067: CC FF 34   CALL       Z,$34FF
506A: CC 55 CC   CALL       Z,$CC55
506D: FF         RST         0X38
506E: 13         INC         DE
506F: 0B         DEC         BC
5070: 16 0B      LD           D,$0B
5072: 32         LD           (HLD),A
5073: 1B         DEC         DE
5074: 37         SCF
5075: 15         DEC         D
5076: FF         RST         0X38
5077: FF         RST         0X38
5078: FF         RST         0X38
5079: FF         RST         0X38
507A: 31 38 48   LD           SP,$4838
507D: 2D         DEC         L
507E: FF         RST         0X38
507F: 25         DEC         H
5080: B5         OR           L
5081: FF         RST         0X38
5082: 13         INC         DE
5083: 9B         SBC         E
5084: 26 9B      LD           H,$9B
5086: FF         RST         0X38
5087: 46         LD           B,(HL)
5088: 76         HALT
5089: 26 85      LD           H,$85
508B: FF         RST         0X38
508C: FF         RST         0X38
508D: FF         RST         0X38
508E: 35         DEC         (HL)
508F: D3                              
5090: FF         RST         0X38
5091: 45         LD           B,L
5092: CD FF 26   CALL       $26FF
5095: 19         ADD         HL,DE
5096: 51         LD           D,C
5097: 19         ADD         HL,DE
5098: 56         LD           D,(HL)
5099: 20 FF      JR           NZ,$509A
509B: 16 35      LD           D,$35
509D: 35         DEC         (HL)
509E: 19         ADD         HL,DE
509F: FF         RST         0X38
50A0: 14         INC         D
50A1: 0B         DEC         BC
50A2: 22         LD           (HLI),A
50A3: 0B         DEC         BC
50A4: 26 0B      LD           H,$0B
50A6: 48         LD           C,B
50A7: 0B         DEC         BC
50A8: FF         RST         0X38
50A9: 55         LD           D,L
50AA: E4                              
50AB: FF         RST         0X38
50AC: 37         SCF
50AD: 6D         LD           L,L
50AE: FF         RST         0X38
50AF: 55         LD           D,L
50B0: 80         ADD         A,B
50B1: FF         RST         0X38
50B2: 13         INC         DE
50B3: 16 FF      LD           D,$FF
50B5: 45         LD           B,L
50B6: 35         DEC         (HL)
50B7: FF         RST         0X38
50B8: 13         INC         DE
50B9: 35         DEC         (HL)
50BA: 34         INC         (HL)
50BB: 9B         SBC         E
50BC: 35         DEC         (HL)
50BD: 9B         SBC         E
50BE: 36 9B      LD           (HL),$9B
50C0: FF         RST         0X38
50C1: 22         LD           (HLI),A
50C2: 19         ADD         HL,DE
50C3: 35         DEC         (HL)
50C4: 19         ADD         HL,DE
50C5: 43         LD           B,E
50C6: 19         ADD         HL,DE
50C7: FF         RST         0X38
50C8: 43         LD           B,E
50C9: 63         LD           H,E
50CA: FF         RST         0X38
50CB: 00         NOP
50CC: CF         RST         0X08
50CD: FF         RST         0X38
50CE: 36 19      LD           (HL),$19
50D0: 44         LD           B,H
50D1: 19         ADD         HL,DE
50D2: FF         RST         0X38
50D3: FF         RST         0X38
50D4: FF         RST         0X38
50D5: FF         RST         0X38
50D6: 13         INC         DE
50D7: BB         CP           E
50D8: 42         LD           B,D
50D9: 19         ADD         HL,DE
50DA: 55         LD           D,L
50DB: 19         ADD         HL,DE
50DC: FF         RST         0X38
50DD: 31 BB 35   LD           SP,$35BB
50E0: 9B         SBC         E
50E1: 55         LD           D,L
50E2: BB         CP           E
50E3: 53         LD           D,E
50E4: 9B         SBC         E
50E5: FF         RST         0X38
50E6: 36 14      LD           (HL),$14
50E8: FF         RST         0X38
50E9: 37         SCF
50EA: CC 54 CC   CALL       Z,$CC54
50ED: FF         RST         0X38
50EE: FF         RST         0X38
50EF: FF         RST         0X38
50F0: 51         LD           D,C
50F1: 16 FF      LD           D,$FF
50F3: 24         INC         H
50F4: B8         CP           B
50F5: FF         RST         0X38
50F6: 13         INC         DE
50F7: 20 43      JR           NZ,$513C
50F9: 16 FF      LD           D,$FF
50FB: 23         INC         HL
50FC: 20 FF      JR           NZ,$50FD
50FE: FF         RST         0X38
50FF: 22         LD           (HLI),A
5100: 19         ADD         HL,DE
5101: 25         DEC         H
5102: CC FF 25   CALL       Z,$25FF
5105: BB         CP           E
5106: 16 19      LD           D,$19
5108: 44         LD           B,H
5109: 19         ADD         HL,DE
510A: FF         RST         0X38
510B: 14         INC         D
510C: C3 42 C3   JP           $C342
510F: 47         LD           B,A
5110: C3 FF FF   JP           $FFFF
5113: 35         DEC         (HL)
5114: C7         RST         0X00
5115: 63         LD           H,E
5116: C7         RST         0X00
5117: 66         LD           H,(HL)
5118: C7         RST         0X00
5119: FF         RST         0X38
511A: 37         SCF
511B: CD FF 34   CALL       $34FF
511E: 6A         LD           L,D
511F: FF         RST         0X38
5120: 67         LD           H,A
5121: 29         ADD         HL,HL
5122: 24         INC         H
5123: 35         DEC         (HL)
5124: 26 7A      LD           H,$7A
5126: FF         RST         0X38
5127: 46         LD           B,(HL)
5128: 61         LD           H,C
5129: 53         LD           D,E
512A: 7A         LD           A,D
512B: FF         RST         0X38
512C: 64         LD           H,H
512D: 0B         DEC         BC
512E: FF         RST         0X38
512F: 63         LD           H,E
5130: 0E FF      LD           C,$FF
5132: 53         LD           D,E
5133: 29         ADD         HL,HL
5134: FF         RST         0X38
5135: 45         LD           B,L
5136: 29         ADD         HL,HL
5137: FF         RST         0X38
5138: 00         NOP
5139: DE F0      SBC         $F0
513B: 41         LD           B,C
513C: FF         RST         0X38
513D: FF         RST         0X38
513E: 00         NOP
513F: 41         LD           B,C
5140: 24         INC         H
5141: C2 FF FF   JP           NZ,$FFFF
5144: 32         LD           (HLD),A
5145: 0D         DEC         C
5146: 36 0D      LD           (HL),$0D
5148: FF         RST         0X38
5149: 12         LD           (DE),A
514A: 0D         DEC         C
514B: 56         LD           D,(HL)
514C: 0D         DEC         C
514D: FF         RST         0X38
514E: 28 3D      JR           Z,$518D
5150: 37         SCF
5151: BB         CP           E
5152: FF         RST         0X38
5153: 46         LD           B,(HL)
5154: BB         CP           E
5155: FF         RST         0X38
5156: FF         RST         0X38
5157: 52         LD           D,D
5158: 0D         DEC         C
5159: 57         LD           D,A
515A: 0D         DEC         C
515B: FF         RST         0X38
515C: 15         DEC         D
515D: 7F         LD           A,A
515E: 13         INC         DE
515F: 7A         LD           A,D
5160: 17         RLA
5161: 7A         LD           A,D
5162: FF         RST         0X38
5163: 33         INC         SP
5164: 0B         DEC         BC
5165: FF         RST         0X38
5166: 13         INC         DE
5167: 0E 25      LD           C,$25
5169: 23         INC         HL
516A: 32         LD           (HLD),A
516B: 0E FF      LD           C,$FF
516D: 44         LD           B,H
516E: 0B         DEC         BC
516F: 55         LD           D,L
5170: 23         INC         HL
5171: FF         RST         0X38
5172: 53         LD           D,E
5173: 29         ADD         HL,HL
5174: 00         NOP
5175: 45         LD           B,L
5176: FF         RST         0X38
5177: 00         NOP
5178: 45         LD           B,L
5179: FF         RST         0X38
517A: 35         DEC         (HL)
517B: 41         LD           B,C
517C: FF         RST         0X38
517D: 00         NOP
517E: 41         LD           B,C
517F: FF         RST         0X38
5180: FF         RST         0X38
5181: 26 B6      LD           H,$B6
5183: FF         RST         0X38
5184: FF         RST         0X38
5185: FF         RST         0X38
5186: FF         RST         0X38
5187: 23         INC         HL
5188: 0D         DEC         C
5189: FF         RST         0X38
518A: 56         LD           D,(HL)
518B: 0D         DEC         C
518C: FF         RST         0X38
518D: 57         LD           D,A
518E: 0D         DEC         C
518F: FF         RST         0X38
5190: 25         DEC         H
5191: 0B         DEC         BC
5192: 32         LD           (HLD),A
5193: 23         INC         HL
5194: 45         LD           B,L
5195: 23         INC         HL
5196: FF         RST         0X38
5197: 36 23      LD           (HL),$23
5199: 53         LD           D,E
519A: 0B         DEC         BC
519B: 56         LD           D,(HL)
519C: 0B         DEC         BC
519D: FF         RST         0X38
519E: 38 7E      JR           C,$521E
51A0: 67         LD           H,A
51A1: 7E         LD           A,(HL)
51A2: 53         LD           D,E
51A3: CC FF 35   CALL       Z,$35FF
51A6: 7C         LD           A,H
51A7: 54         LD           D,H
51A8: CC FF 22   CALL       Z,$22FF
51AB: 7E         LD           A,(HL)
51AC: 24         INC         H
51AD: 7E         LD           A,(HL)
51AE: 32         LD           (HLD),A
51AF: 7E         LD           A,(HL)
51B0: 34         INC         (HL)
51B1: 7E         LD           A,(HL)
51B2: 43         LD           B,E
51B3: 7E         LD           A,(HL)
51B4: FF         RST         0X38
51B5: 43         LD           B,E
51B6: 0B         DEC         BC
51B7: 55         LD           D,L
51B8: 0B         DEC         BC
51B9: FF         RST         0X38
51BA: FF         RST         0X38
51BB: FF         RST         0X38
51BC: 33         INC         SP
51BD: 0B         DEC         BC
51BE: 53         LD           D,E
51BF: 0B         DEC         BC
51C0: FF         RST         0X38
51C1: 55         LD           D,L
51C2: 0B         DEC         BC
51C3: FF         RST         0X38
51C4: 64         LD           H,H
51C5: 0D         DEC         C
51C6: 67         LD           H,A
51C7: 0D         DEC         C
51C8: FF         RST         0X38
51C9: FF         RST         0X38
51CA: 46         LD           B,(HL)
51CB: 61         LD           H,C
51CC: 54         LD           D,H
51CD: 0D         DEC         C
51CE: FF         RST         0X38
51CF: 53         LD           D,E
51D0: 23         INC         HL
51D1: FF         RST         0X38
51D2: 47         LD           B,A
51D3: 23         INC         HL
51D4: FF         RST         0X38
51D5: 43         LD           B,E
51D6: 09         ADD         HL,BC
51D7: 54         LD           D,H
51D8: 09         ADD         HL,BC
51D9: FF         RST         0X38
51DA: 43         LD           B,E
51DB: 0B         DEC         BC
51DC: FF         RST         0X38
51DD: 22         LD           (HLI),A
51DE: 0B         DEC         BC
51DF: 52         LD           D,D
51E0: 23         INC         HL
51E1: 63         LD           H,E
51E2: 0B         DEC         BC
51E3: FF         RST         0X38
51E4: 27         DAA
51E5: CC FF 17   CALL       Z,$17FF
51E8: 7C         LD           A,H
51E9: 25         DEC         H
51EA: 7E         LD           A,(HL)
51EB: 32         LD           (HLD),A
51EC: CC FF 15   CALL       Z,$15FF
51EF: CC FF FF   CALL       Z,$FFFF
51F2: 45         LD           B,L
51F3: 41         LD           B,C
51F4: FF         RST         0X38
51F5: 24         INC         H
51F6: 14         INC         D
51F7: FF         RST         0X38
51F8: 42         LD           B,D
51F9: 0B         DEC         BC
51FA: FF         RST         0X38
51FB: 35         DEC         (HL)
51FC: 0B         DEC         BC
51FD: 46         LD           B,(HL)
51FE: 0B         DEC         BC
51FF: FF         RST         0X38
5200: 24         INC         H
5201: 0B         DEC         BC
5202: 44         LD           B,H
5203: 0D         DEC         C
5204: FF         RST         0X38
5205: 37         SCF
5206: BA         CP           D
5207: FF         RST         0X38
5208: 24         INC         H
5209: 0D         DEC         C
520A: 36 0D      LD           (HL),$0D
520C: FF         RST         0X38
520D: 36 0D      LD           (HL),$0D
520F: FF         RST         0X38
5210: 26 23      LD           H,$23
5212: 37         SCF
5213: 23         INC         HL
5214: FF         RST         0X38
5215: 54         LD           D,H
5216: 6A         LD           L,D
5217: FF         RST         0X38
5218: 24         INC         H
5219: 0B         DEC         BC
521A: 56         LD           D,(HL)
521B: 0B         DEC         BC
521C: FF         RST         0X38
521D: 00         NOP
521E: 41         LD           B,C
521F: FF         RST         0X38
5220: 45         LD           B,L
5221: 1B         DEC         DE
5222: 54         LD           D,H
5223: 1B         DEC         DE
5224: 47         LD           B,A
5225: 0B         DEC         BC
5226: FF         RST         0X38
5227: 33         INC         SP
5228: 0B         DEC         BC
5229: 55         LD           D,L
522A: 0B         DEC         BC
522B: FF         RST         0X38
522C: 44         LD           B,H
522D: 35         DEC         (HL)
522E: FF         RST         0X38
522F: FF         RST         0X38
5230: 37         SCF
5231: 7A         LD           A,D
5232: 54         LD           D,H
5233: 7A         LD           A,D
5234: FF         RST         0X38
5235: 26 7A      LD           H,$7A
5237: 53         LD           D,E
5238: 7A         LD           A,D
5239: FF         RST         0X38
523A: 36 0B      LD           (HL),$0B
523C: FF         RST         0X38
523D: FF         RST         0X38
523E: 35         DEC         (HL)
523F: 14         INC         D
5240: FF         RST         0X38
5241: FF         RST         0X38
5242: 44         LD           B,H
5243: 86         ADD         A,(HL)
5244: FF         RST         0X38
5245: 35         DEC         (HL)
5246: 86         ADD         A,(HL)
5247: FF         RST         0X38
5248: 66         LD           H,(HL)
5249: 86         ADD         A,(HL)
524A: FF         RST         0X38
524B: 26 86      LD           H,$86
524D: 35         DEC         (HL)
524E: 86         ADD         A,(HL)
524F: 48         LD           C,B
5250: 86         ADD         A,(HL)
5251: FF         RST         0X38
5252: 32         LD           (HLD),A
5253: 3A         LD           A,(HLD)
5254: FF         RST         0X38
5255: 37         SCF
5256: 3F         CCF
5257: FF         RST         0X38
5258: 42         LD           B,D
5259: 14         INC         D
525A: 45         LD           B,L
525B: 0B         DEC         BC
525C: FF         RST         0X38
525D: 34         INC         (HL)
525E: 84         ADD         A,H
525F: FF         RST         0X38
5260: 37         SCF
5261: B9         CP           C
5262: 43         LD           B,E
5263: CB FF      SET         1,E
5265: FF         RST         0X38
5266: 23         INC         HL
5267: 7A         LD           A,D
5268: 35         DEC         (HL)
5269: 7A         LD           A,D
526A: FF         RST         0X38
526B: 23         INC         HL
526C: 7A         LD           A,D
526D: 46         LD           B,(HL)
526E: 7A         LD           A,D
526F: FF         RST         0X38
5270: 14         INC         D
5271: 7A         LD           A,D
5272: 47         LD           B,A
5273: 14         INC         D
5274: FF         RST         0X38
5275: FF         RST         0X38
5276: 34         INC         (HL)
5277: 93         SUB         E
5278: FF         RST         0X38
5279: FF         RST         0X38
527A: 31 E5 41   LD           SP,$41E5
527D: 86         ADD         A,(HL)
527E: 52         LD           D,D
527F: 86         ADD         A,(HL)
5280: FF         RST         0X38
5281: 67         LD           H,A
5282: 86         ADD         A,(HL)
5283: 54         LD           D,H
5284: E5         PUSH       HL
5285: FF         RST         0X38
5286: 16 86      LD           D,$86
5288: 55         LD           D,L
5289: E5         PUSH       HL
528A: FF         RST         0X38
528B: 48         LD           C,B
528C: 86         ADD         A,(HL)
528D: 62         LD           H,D
528E: E5         PUSH       HL
528F: FF         RST         0X38
5290: 35         DEC         (HL)
5291: 0B         DEC         BC
5292: 55         LD           D,L
5293: 0B         DEC         BC
5294: FF         RST         0X38
5295: 23         INC         HL
5296: 0B         DEC         BC
5297: 34         INC         (HL)
5298: 0B         DEC         BC
5299: FF         RST         0X38
529A: 65         LD           H,L
529B: 0B         DEC         BC
529C: FF         RST         0X38
529D: 37         SCF
529E: 0B         DEC         BC
529F: FF         RST         0X38
52A0: 2D         DEC         L
52A1: 41         LD           B,C
52A2: 52         LD           D,D
52A3: 44         LD           B,H
52A4: FF         RST         0X38
52A5: 19         ADD         HL,DE
52A6: 2F         CPL
52A7: FF         RST         0X38
52A8: 37         SCF
52A9: 10 53      STOP       $53
52AB: 10 57      STOP       $57
52AD: 10 45      STOP       $45
52AF: 12         LD           (DE),A
52B0: FF         RST         0X38
52B1: 33         INC         SP
52B2: 10 53      STOP       $53
52B4: 10 45      STOP       $45
52B6: 12         LD           (DE),A
52B7: 57         LD           D,A
52B8: 11 FF 64   LD           DE,$64FF
52BB: 14         INC         D
52BC: FF         RST         0X38
52BD: FF         RST         0X38
52BE: 32         LD           (HLD),A
52BF: 14         INC         D
52C0: 66         LD           H,(HL)
52C1: 14         INC         D
52C2: 12         LD           (DE),A
52C3: 2F         CPL
52C4: FF         RST         0X38
52C5: FF         RST         0X38
52C6: 66         LD           H,(HL)
52C7: 86         ADD         A,(HL)
52C8: FF         RST         0X38
52C9: 57         LD           D,A
52CA: E5         PUSH       HL
52CB: 58         LD           E,B
52CC: E5         PUSH       HL
52CD: 67         LD           H,A
52CE: 86         ADD         A,(HL)
52CF: 68         LD           L,B
52D0: 86         ADD         A,(HL)
52D1: FF         RST         0X38
52D2: 24         INC         H
52D3: 86         ADD         A,(HL)
52D4: FF         RST         0X38
52D5: 26 86      LD           H,$86
52D7: 28 86      JR           Z,$525F
52D9: 48         LD           C,B
52DA: 86         ADD         A,(HL)
52DB: 51         LD           D,C
52DC: 86         ADD         A,(HL)
52DD: 68         LD           L,B
52DE: 86         ADD         A,(HL)
52DF: FF         RST         0X38
52E0: 27         DAA
52E1: 0B         DEC         BC
52E2: 36 0B      LD           (HL),$0B
52E4: FF         RST         0X38
52E5: 42         LD           B,D
52E6: 1B         DEC         DE
52E7: 66         LD           H,(HL)
52E8: 1B         DEC         DE
52E9: 22         LD           (HLI),A
52EA: 0B         DEC         BC
52EB: FF         RST         0X38
52EC: 42         LD           B,D
52ED: 0B         DEC         BC
52EE: 46         LD           B,(HL)
52EF: 0B         DEC         BC
52F0: 32         LD           (HLD),A
52F1: 1B         DEC         DE
52F2: FF         RST         0X38
52F3: 24         INC         H
52F4: 0B         DEC         BC
52F5: 35         DEC         (HL)
52F6: 0B         DEC         BC
52F7: 57         LD           D,A
52F8: 1B         DEC         DE
52F9: FF         RST         0X38
52FA: 36 3D      LD           (HL),$3D
52FC: 00         NOP
52FD: BF         CP           A
52FE: FF         RST         0X38
52FF: 00         NOP
5300: BF         CP           A
5301: FF         RST         0X38
5302: 00         NOP
5303: BF         CP           A
5304: 14         INC         D
5305: 10 16      STOP       $16
5307: 10 34      STOP       $34
5309: 10 25      STOP       $25
530B: 12         LD           (DE),A
530C: FF         RST         0X38
530D: 13         INC         DE
530E: 10 17      STOP       $17
5310: 10 35      STOP       $35
5312: 10 24      STOP       $24
5314: 12         LD           (DE),A
5315: FF         RST         0X38
5316: FF         RST         0X38
5317: FF         RST         0X38
5318: FF         RST         0X38
5319: 24         INC         H
531A: AF         XOR         A
531B: 54         LD           D,H
531C: AD         XOR         L
531D: FF         RST         0X38
531E: 21 E5 28   LD           HL,$28E5
5321: 86         ADD         A,(HL)
5322: 31 86 FF   LD           SP,$FF86
5325: 24         INC         H
5326: 86         ADD         A,(HL)
5327: 48         LD           C,B
5328: 86         ADD         A,(HL)
5329: FF         RST         0X38
532A: 22         LD           (HLI),A
532B: 86         ADD         A,(HL)
532C: 24         INC         H
532D: 86         ADD         A,(HL)
532E: 26 86      LD           H,$86
5330: FF         RST         0X38
5331: 22         LD           (HLI),A
5332: 86         ADD         A,(HL)
5333: 34         INC         (HL)
5334: 86         ADD         A,(HL)
5335: 43         LD           B,E
5336: E5         PUSH       HL
5337: 45         LD           B,L
5338: 86         ADD         A,(HL)
5339: FF         RST         0X38
533A: 11 41 FF   LD           DE,$FF41
533D: 46         LD           B,(HL)
533E: 54         LD           D,H
533F: FF         RST         0X38
5340: 26 6E      LD           H,$6E
5342: 32         LD           (HLD),A
5343: 6E         LD           L,(HL)
5344: 55         LD           D,L
5345: 6E         LD           L,(HL)
5346: FF         RST         0X38
5347: 25         DEC         H
5348: 70         LD           (HL),B
5349: 22         LD           (HLI),A
534A: 6E         LD           L,(HL)
534B: 56         LD           D,(HL)
534C: 6E         LD           L,(HL)
534D: FF         RST         0X38
534E: 23         INC         HL
534F: 6E         LD           L,(HL)
5350: 41         LD           B,C
5351: 6E         LD           L,(HL)
5352: FF         RST         0X38
5353: FF         RST         0X38
5354: 27         DAA
5355: B0         OR           B
5356: 34         INC         (HL)
5357: B0         OR           B
5358: 54         LD           D,H
5359: B0         OR           B
535A: FF         RST         0X38
535B: 24         INC         H
535C: B3         OR           E
535D: 45         LD           B,L
535E: B4         OR           H
535F: FF         RST         0X38
5360: 27         DAA
5361: AE         XOR         (HL)
5362: 32         LD           (HLD),A
5363: AE         XOR         (HL)
5364: FF         RST         0X38
5365: 34         INC         (HL)
5366: B0         OR           B
5367: 56         LD           D,(HL)
5368: B2         OR           D
5369: FF         RST         0X38
536A: 54         LD           D,H
536B: 0B         DEC         BC
536C: 56         LD           D,(HL)
536D: 0B         DEC         BC
536E: 52         LD           D,D
536F: 43         LD           B,E
5370: 57         LD           D,A
5371: 43         LD           B,E
5372: FF         RST         0X38
5373: 44         LD           B,H
5374: 3D         DEC         A
5375: 38 CB      JR           C,$5342
5377: FF         RST         0X38
5378: FF         RST         0X38
5379: FF         RST         0X38
537A: 25         DEC         H
537B: BA         CP           D
537C: 43         LD           B,E
537D: BA         CP           D
537E: FF         RST         0X38
537F: 26 2F      LD           H,$2F
5381: FF         RST         0X38
5382: FF         RST         0X38
5383: 22         LD           (HLI),A
5384: 38 44      JR           C,$53CA
5386: 6C         LD           L,H
5387: 26 6E      LD           H,$6E
5389: 32         LD           (HLD),A
538A: 6E         LD           L,(HL)
538B: FF         RST         0X38
538C: 57         LD           D,A
538D: 73         LD           (HL),E
538E: 42         LD           B,D
538F: 3E 63      LD           A,$63
5391: 6F         LD           L,A
5392: 11 6E 17   LD           DE,$176E
5395: 6E         LD           L,(HL)
5396: 23         INC         HL
5397: 6E         LD           L,(HL)
5398: 45         LD           B,L
5399: DC FF 22   CALL       C,$22FF
539C: 6C         LD           L,H
539D: 46         LD           B,(HL)
539E: 6E         LD           L,(HL)
539F: FF         RST         0X38
53A0: FF         RST         0X38
53A1: 46         LD           B,(HL)
53A2: 61         LD           H,C
53A3: 25         DEC         H
53A4: AE         XOR         (HL)
53A5: 23         INC         HL
53A6: 2F         CPL
53A7: FF         RST         0X38
53A8: 23         INC         HL
53A9: B0         OR           B
53AA: 56         LD           D,(HL)
53AB: B0         OR           B
53AC: FF         RST         0X38
53AD: 22         LD           (HLI),A
53AE: B0         OR           B
53AF: FF         RST         0X38
53B0: 12         LD           (DE),A
53B1: AE         XOR         (HL)
53B2: 35         DEC         (HL)
53B3: AE         XOR         (HL)
53B4: 58         LD           E,B
53B5: BA         CP           D
53B6: FF         RST         0X38
53B7: 33         INC         SP
53B8: AE         XOR         (HL)
53B9: 56         LD           D,(HL)
53BA: AE         XOR         (HL)
53BB: FF         RST         0X38
53BC: 46         LD           B,(HL)
53BD: 0B         DEC         BC
53BE: 54         LD           D,H
53BF: 14         INC         D
53C0: 57         LD           D,A
53C1: 0B         DEC         BC
53C2: FF         RST         0X38
53C3: 44         LD           B,H
53C4: BA         CP           D
53C5: 38 CB      JR           C,$5392
53C7: FF         RST         0X38
53C8: F0 41      LD           A,($41)
53CA: FF         RST         0X38
53CB: 0F         RRCA
53CC: 41         LD           B,C
53CD: 22         LD           (HLI),A
53CE: 0F         RRCA
53CF: 64         LD           H,H
53D0: BA         CP           D
53D1: FF         RST         0X38
53D2: 43         LD           B,E
53D3: 0D         DEC         C
53D4: 56         LD           D,(HL)
53D5: 0D         DEC         C
53D6: FF         RST         0X38
53D7: 44         LD           B,H
53D8: BA         CP           D
53D9: 37         SCF
53DA: 0D         DEC         C
53DB: FF         RST         0X38
53DC: 13         INC         DE
53DD: 6E         LD           L,(HL)
53DE: 26 6E      LD           H,$6E
53E0: 52         LD           D,D
53E1: 6E         LD           L,(HL)
53E2: 24         INC         H
53E3: 2D         DEC         L
53E4: 25         DEC         H
53E5: 2D         DEC         L
53E6: 26 2D      LD           H,$2D
53E8: FF         RST         0X38
53E9: 17         RLA
53EA: 6F         LD           L,A
53EB: 23         INC         HL
53EC: 6E         LD           L,(HL)
53ED: 58         LD           E,B
53EE: 6E         LD           L,(HL)
53EF: 44         LD           B,H
53F0: 6D         LD           L,L
53F1: FF         RST         0X38
53F2: 27         DAA
53F3: 2F         CPL
53F4: 53         LD           D,E
53F5: 6C         LD           L,H
53F6: FF         RST         0X38
53F7: 35         DEC         (HL)
53F8: 3D         DEC         A
53F9: 13         INC         DE
53FA: 6E         LD           L,(HL)
53FB: 32         LD           (HLD),A
53FC: 6E         LD           L,(HL)
53FD: 57         LD           D,A
53FE: 6E         LD           L,(HL)
53FF: FF         RST         0X38
5400: 26 3D      LD           H,$3D
5402: 51         LD           D,C
5403: AE         XOR         (HL)
5404: 46         LD           B,(HL)
5405: AE         XOR         (HL)
5406: FF         RST         0X38
5407: 34         INC         (HL)
5408: AE         XOR         (HL)
5409: 65         LD           H,L
540A: AE         XOR         (HL)
540B: 45         LD           B,L
540C: 3D         DEC         A
540D: FF         RST         0X38
540E: 46         LD           B,(HL)
540F: 3D         DEC         A
5410: FF         RST         0X38
5411: FF         RST         0X38
5412: 53         LD           D,E
5413: 3D         DEC         A
5414: 46         LD           B,(HL)
5415: AE         XOR         (HL)
5416: 64         LD           H,H
5417: AE         XOR         (HL)
5418: FF         RST         0X38
5419: 33         INC         SP
541A: 0B         DEC         BC
541B: 46         LD           B,(HL)
541C: 0B         DEC         BC
541D: 54         LD           D,H
541E: 0B         DEC         BC
541F: FF         RST         0X38
5420: FF         RST         0X38
5421: 28 B9      JR           Z,$53DC
5423: 34         INC         (HL)
5424: BA         CP           D
5425: 42         LD           B,D
5426: B9         CP           C
5427: FF         RST         0X38
5428: 41         LD           B,C
5429: 41         LD           B,C
542A: 63         LD           H,E
542B: 0F         RRCA
542C: 67         LD           H,A
542D: 0F         RRCA
542E: FF         RST         0X38
542F: 23         INC         HL
5430: 0F         RRCA
5431: 27         DAA
5432: 0F         RRCA
5433: 24         INC         H
5434: 9B         SBC         E
5435: 26 9B      LD           H,$9B
5437: 44         LD           B,H
5438: 9B         SBC         E
5439: 46         LD           B,(HL)
543A: 9B         SBC         E
543B: FF         RST         0X38
543C: 34         INC         (HL)
543D: 0F         RRCA
543E: 36 0F      LD           (HL),$0F
5440: 54         LD           D,H
5441: 0F         RRCA
5442: 56         LD           D,(HL)
5443: 0F         RRCA
5444: FF         RST         0X38
5445: FF         RST         0X38
5446: 44         LD           B,H
5447: 71         LD           (HL),C
5448: 47         LD           B,A
5449: 72         LD           (HL),D
544A: 15         DEC         D
544B: 6E         LD           L,(HL)
544C: 17         RLA
544D: 6E         LD           L,(HL)
544E: FF         RST         0X38
544F: 03         INC         BC
5450: 6C         LD           L,H
5451: 57         LD           D,A
5452: 75         LD           (HL),L
5453: FF         RST         0X38
5454: 23         INC         HL
5455: 6E         LD           L,(HL)
5456: 27         DAA
5457: 6C         LD           L,H
5458: FF         RST         0X38
5459: 26 6E      LD           H,$6E
545B: 33         INC         SP
545C: 6E         LD           L,(HL)
545D: 47         LD           B,A
545E: 6E         LD           L,(HL)
545F: 22         LD           (HLI),A
5460: 6F         LD           L,A
5461: 52         LD           D,D
5462: 73         LD           (HL),E
5463: FF         RST         0X38
5464: 00         NOP
5465: C0         RET         NZ
5466: 42         LD           B,D
5467: 14         INC         D
5468: FF         RST         0X38
5469: FF         RST         0X38
546A: F1         POP         AF
546B: 41         LD           B,C
546C: FF         RST         0X38
546D: FF         RST         0X38
546E: 37         SCF
546F: BA         CP           D
5470: 42         LD           B,D
5471: BA         CP           D
5472: FF         RST         0X38
5473: 34         INC         (HL)
5474: 3D         DEC         A
5475: 22         LD           (HLI),A
5476: 0B         DEC         BC
5477: 26 0B      LD           H,$0B
5479: 42         LD           B,D
547A: 0B         DEC         BC
547B: FF         RST         0X38
547C: 22         LD           (HLI),A
547D: BA         CP           D
547E: 55         LD           D,L
547F: CB FF      SET         1,E
5481: 46         LD           B,(HL)
5482: B9         CP           C
5483: 53         LD           D,E
5484: B9         CP           C
5485: FF         RST         0X38
5486: 12         LD           (DE),A
5487: 0F         RRCA
5488: 64         LD           H,H
5489: 0F         RRCA
548A: 13         INC         DE
548B: 9B         SBC         E
548C: 42         LD           B,D
548D: 9B         SBC         E
548E: 66         LD           H,(HL)
548F: 9B         SBC         E
5490: FF         RST         0X38
5491: 22         LD           (HLI),A
5492: 0F         RRCA
5493: 26 0F      LD           H,$0F
5495: 44         LD           B,H
5496: 0F         RRCA
5497: 57         LD           D,A
5498: 0F         RRCA
5499: 25         DEC         H
549A: 9B         SBC         E
549B: 32         LD           (HLD),A
549C: 9B         SBC         E
549D: FF         RST         0X38
549E: 12         LD           (DE),A
549F: 0F         RRCA
54A0: 14         INC         D
54A1: 0F         RRCA
54A2: 46         LD           B,(HL)
54A3: 0F         RRCA
54A4: 41         LD           B,C
54A5: 9B         SBC         E
54A6: 53         LD           D,E
54A7: 9B         SBC         E
54A8: 56         LD           D,(HL)
54A9: 9B         SBC         E
54AA: FF         RST         0X38
54AB: 31 0F 35   LD           SP,$350F
54AE: 0F         RRCA
54AF: 53         LD           D,E
54B0: 0F         RRCA
54B1: 23         INC         HL
54B2: 1B         DEC         DE
54B3: 26 9B      LD           H,$9B
54B5: FF         RST         0X38
54B6: FF         RST         0X38
54B7: 33         INC         SP
54B8: 09         ADD         HL,BC
54B9: 54         LD           D,H
54BA: 09         ADD         HL,BC
54BB: FF         RST         0X38
54BC: 13         INC         DE
54BD: 09         ADD         HL,BC
54BE: 26 09      LD           H,$09
54C0: 56         LD           D,(HL)
54C1: 09         ADD         HL,BC
54C2: FF         RST         0X38
54C3: 24         INC         H
54C4: 09         ADD         HL,BC
54C5: 47         LD           B,A
54C6: 09         ADD         HL,BC
54C7: 52         LD           D,D
54C8: 09         ADD         HL,BC
54C9: FF         RST         0X38
54CA: 00         NOP
54CB: C0         RET         NZ
54CC: 23         INC         HL
54CD: 9B         SBC         E
54CE: 44         LD           B,H
54CF: 9B         SBC         E
54D0: 56         LD           D,(HL)
54D1: 1B         DEC         DE
54D2: FF         RST         0X38
54D3: 00         NOP
54D4: C0         RET         NZ
54D5: 43         LD           B,E
54D6: 9B         SBC         E
54D7: 58         LD           E,B
54D8: 9B         SBC         E
54D9: FF         RST         0X38
54DA: 27         DAA
54DB: 3C         INC         A
54DC: FF         RST         0X38
54DD: FF         RST         0X38
54DE: 35         DEC         (HL)
54DF: 0B         DEC         BC
54E0: 44         LD           B,H
54E1: 0B         DEC         BC
54E2: FF         RST         0X38
54E3: 47         LD           B,A
54E4: B7         OR           A
54E5: FF         RST         0X38
54E6: 22         LD           (HLI),A
54E7: CB 36      SWAP        1,E
54E9: CB 54      BIT         1,E
54EB: CB FF      SET         1,E
54ED: 22         LD           (HLI),A
54EE: 6E         LD           L,(HL)
54EF: 37         SCF
54F0: 6E         LD           L,(HL)
54F1: 54         LD           D,H
54F2: 6E         LD           L,(HL)
54F3: FF         RST         0X38
54F4: 54         LD           D,H
54F5: D3                              
54F6: 22         LD           (HLI),A
54F7: 6E         LD           L,(HL)
54F8: 43         LD           B,E
54F9: 6E         LD           L,(HL)
54FA: 58         LD           E,B
54FB: 6E         LD           L,(HL)
54FC: FF         RST         0X38
54FD: 53         LD           D,E
54FE: D3                              
54FF: 56         LD           D,(HL)
5500: 75         LD           (HL),L
5501: 54         LD           D,H
5502: 6E         LD           L,(HL)
5503: 62         LD           H,D
5504: 6E         LD           L,(HL)
5505: FF         RST         0X38
5506: 43         LD           B,E
5507: 87         ADD         A,A
5508: 00         NOP
5509: 61         LD           H,C
550A: FF         RST         0X38
550B: 25         DEC         H
550C: 0E 33      LD           C,$33
550E: 0E FF      LD           C,$FF
5510: 17         RLA
5511: 09         ADD         HL,BC
5512: FF         RST         0X38
5513: 37         SCF
5514: 09         ADD         HL,BC
5515: 43         LD           B,E
5516: 09         ADD         HL,BC
5517: FF         RST         0X38
5518: 45         LD           B,L
5519: 41         LD           B,C
551A: 43         LD           B,E
551B: 3D         DEC         A
551C: FF         RST         0X38
551D: FF         RST         0X38
551E: 00         NOP
551F: C0         RET         NZ
5520: 22         LD           (HLI),A
5521: 9B         SBC         E
5522: 36 BB      LD           (HL),$BB
5524: FF         RST         0X38
5525: 00         NOP
5526: C0         RET         NZ
5527: 24         INC         H
5528: 9B         SBC         E
5529: 33         INC         SP
552A: 9B         SBC         E
552B: 47         LD           B,A
552C: 9B         SBC         E
552D: 64         LD           H,H
552E: BB         CP           E
552F: FF         RST         0X38
5530: FF         RST         0X38
5531: FF         RST         0X38
5532: 32         LD           (HLD),A
5533: BA         CP           D
5534: 38 CB      JR           C,$5501
5536: FF         RST         0X38
5537: 52         LD           D,D
5538: 97         SUB         A
5539: 54         LD           D,H
553A: 97         SUB         A
553B: FF         RST         0X38
553C: 33         INC         SP
553D: 3D         DEC         A
553E: 26 CB      LD           H,$CB
5540: 62         LD           H,D
5541: CB FF      SET         1,E
5543: 32         LD           (HLD),A
5544: BA         CP           D
5545: 34         INC         (HL)
5546: BB         CP           E
5547: 55         LD           D,L
5548: BB         CP           E
5549: FF         RST         0X38
554A: 35         DEC         (HL)
554B: 3E 38      LD           A,$38
554D: 6E         LD           L,(HL)
554E: 26 D0      LD           H,$D0
5550: 23         INC         HL
5551: D2 53 D0   JP           NC,$D053
5554: 57         LD           D,A
5555: D1         POP         DE
5556: 65         LD           H,L
5557: D0         RET         NC
5558: FF         RST         0X38
5559: 42         LD           B,D
555A: D3                              
555B: 18 6E      JR           $55CB
555D: 33         INC         SP
555E: 6E         LD           L,(HL)
555F: 47         LD           B,A
5560: 6E         LD           L,(HL)
5561: FF         RST         0X38
5562: 27         DAA
5563: 0E 34      LD           C,$34
5565: 0E 57      LD           C,$57
5567: 0E FF      LD           C,$FF
5569: 37         SCF
556A: E3                              
556B: 63         LD           H,E
556C: E3                              
556D: 32         LD           (HLD),A
556E: 0E 65      LD           C,$65
5570: 0E 66      LD           C,$66
5572: 44         LD           B,H
5573: FF         RST         0X38
5574: 14         INC         D
5575: 09         ADD         HL,BC
5576: 42         LD           B,D
5577: 09         ADD         HL,BC
5578: FF         RST         0X38
5579: 23         INC         HL
557A: C5         PUSH       BC
557B: 46         LD           B,(HL)
557C: C5         PUSH       BC
557D: 47         LD           B,A
557E: C5         PUSH       BC
557F: FF         RST         0X38
5580: 26 09      LD           H,$09
5582: 55         LD           D,L
5583: 09         ADD         HL,BC
5584: 52         LD           D,D
5585: C5         PUSH       BC
5586: 62         LD           H,D
5587: C5         PUSH       BC
5588: FF         RST         0X38
5589: 10 CD      STOP       $CD
558B: 16 CD      LD           D,$CD
558D: 50         LD           D,B
558E: CD 56 CD   CALL       $CD56
5591: FF         RST         0X38
5592: 14         INC         D
5593: E0 FF      LDFF00   ($FF),A
5595: FF         RST         0X38
5596: FF         RST         0X38
5597: 34         INC         (HL)
5598: B9         CP           C
5599: FF         RST         0X38
559A: 33         INC         SP
559B: B9         CP           C
559C: 46         LD           B,(HL)
559D: B9         CP           C
559E: FF         RST         0X38
559F: 26 CE      LD           H,$CE
55A1: 62         LD           H,D
55A2: 3D         DEC         A
55A3: FF         RST         0X38
55A4: 26 97      LD           H,$97
55A6: 66         LD           H,(HL)
55A7: B9         CP           C
55A8: FF         RST         0X38
55A9: 32         LD           (HLD),A
55AA: B9         CP           C
55AB: 33         INC         SP
55AC: BA         CP           D
55AD: 46         LD           B,(HL)
55AE: B9         CP           C
55AF: FF         RST         0X38
55B0: 46         LD           B,(HL)
55B1: 61         LD           H,C
55B2: FF         RST         0X38
55B3: FF         RST         0X38
55B4: 01 41 FF   LD           BC,$FF41
55B7: 46         LD           B,(HL)
55B8: E3                              
55B9: 53         LD           D,E
55BA: E3                              
55BB: FF         RST         0X38
55BC: 44         LD           B,H
55BD: 0E 47      LD           C,$47
55BF: 0E 22      LD           C,$22
55C1: 09         ADD         HL,BC
55C2: FF         RST         0X38
55C3: 13         INC         DE
55C4: 09         ADD         HL,BC
55C5: 23         INC         HL
55C6: 0E 45      LD           C,$45
55C8: 0E FF      LD           C,$FF
55CA: 00         NOP
55CB: 41         LD           B,C
55CC: 55         LD           D,L
55CD: 31 32 C5   LD           SP,$C532
55D0: FF         RST         0X38
55D1: 32         LD           (HLD),A
55D2: C6 46      ADD         $46
55D4: C6 FF      ADD         $FF
55D6: 24         INC         H
55D7: 0E 26      LD           C,$26
55D9: 0E 28      LD           C,$28
55DB: C6 FF      ADD         $FF
55DD: 45         LD           B,L
55DE: C1         POP         BC
55DF: FF         RST         0X38
55E0: FF         RST         0X38
55E1: FF         RST         0X38
55E2: 44         LD           B,H
55E3: 3D         DEC         A
55E4: 21 CB FF   LD           HL,$FFCB
55E7: FF         RST         0X38
55E8: 22         LD           (HLI),A
55E9: B9         CP           C
55EA: 51         LD           D,C
55EB: CB FF      SET         1,E
55ED: 24         INC         H
55EE: B9         CP           C
55EF: 22         LD           (HLI),A
55F0: BB         CP           E
55F1: FF         RST         0X38
55F2: FF         RST         0X38
55F3: 38 C4      JR           C,$55B9
55F5: FF         RST         0X38
55F6: FF         RST         0X38
55F7: 45         LD           B,L
55F8: 3D         DEC         A
55F9: 23         INC         HL
55FA: 0E 42      LD           C,$42
55FC: 0E FF      LD           C,$FF
55FE: FF         RST         0X38
55FF: FF         RST         0X38
5600: FF         RST         0X38
5601: FF         RST         0X38
5602: FF         RST         0X38
5603: FF         RST         0X38
5604: FF         RST         0X38
5605: FF         RST         0X38
5606: FF         RST         0X38
5607: FF         RST         0X38
5608: FF         RST         0X38
5609: FF         RST         0X38
560A: FF         RST         0X38
560B: FF         RST         0X38
560C: FF         RST         0X38
560D: FF         RST         0X38
560E: FF         RST         0X38
560F: FF         RST         0X38
5610: FF         RST         0X38
5611: FF         RST         0X38
5612: FF         RST         0X38
5613: FF         RST         0X38
5614: FF         RST         0X38
5615: FF         RST         0X38
5616: FF         RST         0X38
5617: FF         RST         0X38
5618: FF         RST         0X38
5619: FF         RST         0X38
561A: FF         RST         0X38
561B: FF         RST         0X38
561C: FF         RST         0X38
561D: FF         RST         0X38
561E: FF         RST         0X38
561F: FF         RST         0X38
5620: FF         RST         0X38
5621: FF         RST         0X38
5622: FF         RST         0X38
5623: FF         RST         0X38
5624: FF         RST         0X38
5625: FF         RST         0X38
5626: FF         RST         0X38
5627: FF         RST         0X38
5628: FF         RST         0X38
5629: FF         RST         0X38
562A: FF         RST         0X38
562B: FF         RST         0X38
562C: FF         RST         0X38
562D: FF         RST         0X38
562E: FF         RST         0X38
562F: FF         RST         0X38
5630: FF         RST         0X38
5631: FF         RST         0X38
5632: FF         RST         0X38
5633: FF         RST         0X38
5634: FF         RST         0X38
5635: FF         RST         0X38
5636: FF         RST         0X38
5637: FF         RST         0X38
5638: FF         RST         0X38
5639: FF         RST         0X38
563A: FF         RST         0X38
563B: FF         RST         0X38
563C: FF         RST         0X38
563D: FF         RST         0X38
563E: FF         RST         0X38
563F: FF         RST         0X38
5640: FF         RST         0X38
5641: FF         RST         0X38
5642: FF         RST         0X38
5643: FF         RST         0X38
5644: FF         RST         0X38
5645: FF         RST         0X38
5646: FF         RST         0X38
5647: FF         RST         0X38
5648: FF         RST         0X38
5649: FF         RST         0X38
564A: FF         RST         0X38
564B: FF         RST         0X38
564C: FF         RST         0X38
564D: FF         RST         0X38
564E: FF         RST         0X38
564F: FF         RST         0X38
5650: FF         RST         0X38
5651: FF         RST         0X38
5652: FF         RST         0X38
5653: FF         RST         0X38
5654: FF         RST         0X38
5655: FF         RST         0X38
5656: FF         RST         0X38
5657: FF         RST         0X38
5658: FF         RST         0X38
5659: FF         RST         0X38
565A: FF         RST         0X38
565B: FF         RST         0X38
565C: FF         RST         0X38
565D: FF         RST         0X38
565E: FF         RST         0X38
565F: FF         RST         0X38
5660: FF         RST         0X38
5661: FF         RST         0X38
5662: FF         RST         0X38
5663: FF         RST         0X38
5664: FF         RST         0X38
5665: FF         RST         0X38
5666: FF         RST         0X38
5667: FF         RST         0X38
5668: FF         RST         0X38
5669: FF         RST         0X38
566A: FF         RST         0X38
566B: FF         RST         0X38
566C: FF         RST         0X38
566D: FF         RST         0X38
566E: FF         RST         0X38
566F: FF         RST         0X38
5670: FF         RST         0X38
5671: FF         RST         0X38
5672: FF         RST         0X38
5673: FF         RST         0X38
5674: FF         RST         0X38
5675: FF         RST         0X38
5676: FF         RST         0X38
5677: FF         RST         0X38
5678: FF         RST         0X38
5679: FF         RST         0X38
567A: FF         RST         0X38
567B: FF         RST         0X38
567C: FF         RST         0X38
567D: FF         RST         0X38
567E: FF         RST         0X38
567F: FF         RST         0X38
5680: FF         RST         0X38
5681: FF         RST         0X38
5682: FF         RST         0X38
5683: FF         RST         0X38
5684: FF         RST         0X38
5685: FF         RST         0X38
5686: FF         RST         0X38
5687: FF         RST         0X38
5688: FF         RST         0X38
5689: FF         RST         0X38
568A: FF         RST         0X38
568B: FF         RST         0X38
568C: FF         RST         0X38
568D: FF         RST         0X38
568E: FF         RST         0X38
568F: FF         RST         0X38
5690: FF         RST         0X38
5691: FF         RST         0X38
5692: FF         RST         0X38
5693: FF         RST         0X38
5694: FF         RST         0X38
5695: FF         RST         0X38
5696: FF         RST         0X38
5697: FF         RST         0X38
5698: FF         RST         0X38
5699: FF         RST         0X38
569A: FF         RST         0X38
569B: FF         RST         0X38
569C: FF         RST         0X38
569D: FF         RST         0X38
569E: FF         RST         0X38
569F: FF         RST         0X38
56A0: FF         RST         0X38
56A1: FF         RST         0X38
56A2: FF         RST         0X38
56A3: FF         RST         0X38
56A4: FF         RST         0X38
56A5: FF         RST         0X38
56A6: FF         RST         0X38
56A7: FF         RST         0X38
56A8: FF         RST         0X38
56A9: FF         RST         0X38
56AA: FF         RST         0X38
56AB: FF         RST         0X38
56AC: FF         RST         0X38
56AD: FF         RST         0X38
56AE: FF         RST         0X38
56AF: FF         RST         0X38
56B0: FF         RST         0X38
56B1: FF         RST         0X38
56B2: FF         RST         0X38
56B3: FF         RST         0X38
56B4: FF         RST         0X38
56B5: FF         RST         0X38
56B6: FF         RST         0X38
56B7: FF         RST         0X38
56B8: FF         RST         0X38
56B9: FF         RST         0X38
56BA: FF         RST         0X38
56BB: FF         RST         0X38
56BC: FF         RST         0X38
56BD: FF         RST         0X38
56BE: FF         RST         0X38
56BF: FF         RST         0X38
56C0: FF         RST         0X38
56C1: FF         RST         0X38
56C2: FF         RST         0X38
56C3: FF         RST         0X38
56C4: FF         RST         0X38
56C5: FF         RST         0X38
56C6: FF         RST         0X38
56C7: FF         RST         0X38
56C8: FF         RST         0X38
56C9: FF         RST         0X38
56CA: FF         RST         0X38
56CB: FF         RST         0X38
56CC: FF         RST         0X38
56CD: FF         RST         0X38
56CE: FF         RST         0X38
56CF: FF         RST         0X38
56D0: FF         RST         0X38
56D1: FF         RST         0X38
56D2: FF         RST         0X38
56D3: FF         RST         0X38
56D4: FF         RST         0X38
56D5: FF         RST         0X38
56D6: FF         RST         0X38
56D7: FF         RST         0X38
56D8: FF         RST         0X38
56D9: FF         RST         0X38
56DA: FF         RST         0X38
56DB: FF         RST         0X38
56DC: FF         RST         0X38
56DD: FF         RST         0X38
56DE: FF         RST         0X38
56DF: FF         RST         0X38
56E0: FF         RST         0X38
56E1: FF         RST         0X38
56E2: FF         RST         0X38
56E3: FF         RST         0X38
56E4: FF         RST         0X38
56E5: FF         RST         0X38
56E6: FF         RST         0X38
56E7: FF         RST         0X38
56E8: FF         RST         0X38
56E9: FF         RST         0X38
56EA: FF         RST         0X38
56EB: FF         RST         0X38
56EC: FF         RST         0X38
56ED: FF         RST         0X38
56EE: FF         RST         0X38
56EF: FF         RST         0X38
56F0: FF         RST         0X38
56F1: FF         RST         0X38
56F2: FF         RST         0X38
56F3: FF         RST         0X38
56F4: FF         RST         0X38
56F5: FF         RST         0X38
56F6: FF         RST         0X38
56F7: FF         RST         0X38
56F8: FF         RST         0X38
56F9: FF         RST         0X38
56FA: FF         RST         0X38
56FB: FF         RST         0X38
56FC: FF         RST         0X38
56FD: FF         RST         0X38
56FE: FF         RST         0X38
56FF: FF         RST         0X38
5700: 20 43      JR           NZ,$5745
5702: 72         LD           (HL),D
5703: 61         LD           H,C
5704: 7A         LD           A,D
5705: 79         LD           A,C
5706: 20 54      JR           NZ,$575C
5708: 72         LD           (HL),D
5709: 61         LD           H,C
570A: 63         LD           H,E
570B: 79         LD           A,C
570C: 5E         LD           E,(HL)
570D: 73         LD           (HL),E
570E: 20 20      JR           NZ,$5730
5710: 20 20      JR           NZ,$5732
5712: 48         LD           C,B
5713: 65         LD           H,L
5714: 61         LD           H,C
5715: 6C         LD           L,H
5716: 74         LD           (HL),H
5717: 68         LD           L,B
5718: 20 53      JR           NZ,$576D
571A: 70         LD           (HL),B
571B: 61         LD           H,C
571C: FF         RST         0X38
571D: 51         LD           D,C
571E: 75         LD           (HL),L
571F: 61         LD           H,C
5720: 64         LD           H,H
5721: 72         LD           (HL),D
5722: 75         LD           (HL),L
5723: 70         LD           (HL),B
5724: 6C         LD           L,H
5725: 65         LD           H,L
5726: 74         LD           (HL),H
5727: 5E         LD           E,(HL)
5728: 73         LD           (HL),E
5729: 20 20      JR           NZ,$574B
572B: 20 20      JR           NZ,$574D
572D: 20 20      JR           NZ,$574F
572F: 20 20      JR           NZ,$5751
5731: 20 20      JR           NZ,$5753
5733: 48         LD           C,B
5734: 6F         LD           L,A
5735: 75         LD           (HL),L
5736: 73         LD           (HL),E
5737: 65         LD           H,L
5738: FF         RST         0X38
5739: 20 20      JR           NZ,$575B
573B: 44         LD           B,H
573C: 72         LD           (HL),D
573D: 65         LD           H,L
573E: 61         LD           H,C
573F: 6D         LD           L,L
5740: 20 53      JR           NZ,$5795
5742: 68         LD           L,B
5743: 72         LD           (HL),D
5744: 69         LD           L,C
5745: 6E         LD           L,(HL)
5746: 65         LD           H,L
5747: 20 20      JR           NZ,$5769
5749: FF         RST         0X38
574A: 54         LD           D,H
574B: 65         LD           H,L
574C: 6C         LD           L,H
574D: 65         LD           H,L
574E: 70         LD           (HL),B
574F: 68         LD           L,B
5750: 6F         LD           L,A
5751: 6E         LD           L,(HL)
5752: 65         LD           H,L
5753: 20 42      JR           NZ,$5797
5755: 6F         LD           L,A
5756: 6F         LD           L,A
5757: 74         LD           (HL),H
5758: 68         LD           L,B
5759: 20 FF      JR           NZ,$575A
575B: 53         LD           D,E
575C: 65         LD           H,L
575D: 61         LD           H,C
575E: 73         LD           (HL),E
575F: 68         LD           L,B
5760: 65         LD           H,L
5761: 6C         LD           L,H
5762: 6C         LD           L,H
5763: 20 4D      JR           NZ,$57B2
5765: 61         LD           H,C
5766: 6E         LD           L,(HL)
5767: 73         LD           (HL),E
5768: 69         LD           L,C
5769: 6F         LD           L,A
576A: 6E         LD           L,(HL)
576B: FF         RST         0X38
576C: 52         LD           D,D
576D: 69         LD           L,C
576E: 63         LD           H,E
576F: 68         LD           L,B
5770: 61         LD           H,C
5771: 72         LD           (HL),D
5772: 64         LD           H,H
5773: 5E         LD           E,(HL)
5774: 73         LD           (HL),E
5775: 20 56      JR           NZ,$57CD
5777: 69         LD           L,C
5778: 6C         LD           L,H
5779: 6C         LD           L,H
577A: 61         LD           H,C
577B: 20 FF      JR           NZ,$577C
577D: 20 20      JR           NZ,$579F
577F: 20 20      JR           NZ,$57A1
5781: 20 48      JR           NZ,$57CB
5783: 65         LD           H,L
5784: 6E         LD           L,(HL)
5785: 20 48      JR           NZ,$57CF
5787: 6F         LD           L,A
5788: 75         LD           (HL),L
5789: 73         LD           (HL),E
578A: 65         LD           H,L
578B: 20 20      JR           NZ,$57AD
578D: FF         RST         0X38
578E: 56         LD           D,(HL)
578F: 69         LD           L,C
5790: 6C         LD           L,H
5791: 6C         LD           L,H
5792: 61         LD           H,C
5793: 67         LD           H,A
5794: 65         LD           H,L
5795: 20 4C      JR           NZ,$57E3
5797: 69         LD           L,C
5798: 62         LD           H,D
5799: 72         LD           (HL),D
579A: 61         LD           H,C
579B: 72         LD           (HL),D
579C: 79         LD           A,C
579D: 20 FF      JR           NZ,$579E
579F: 20 20      JR           NZ,$57C1
57A1: 20 20      JR           NZ,$57C3
57A3: 52         LD           D,D
57A4: 61         LD           H,C
57A5: 66         LD           H,(HL)
57A6: 74         LD           (HL),H
57A7: 20 53      JR           NZ,$57FC
57A9: 68         LD           L,B
57AA: 6F         LD           L,A
57AB: 70         LD           (HL),B
57AC: 20 20      JR           NZ,$57CE
57AE: 20 FF      JR           NZ,$57AF
57B0: 20 20      JR           NZ,$57D2
57B2: 20 20      JR           NZ,$57D4
57B4: 57         LD           D,A
57B5: 61         LD           H,C
57B6: 72         LD           (HL),D
57B7: 70         LD           (HL),B
57B8: 20 48      JR           NZ,$5802
57BA: 6F         LD           L,A
57BB: 6C         LD           L,H
57BC: 65         LD           H,L
57BD: 20 20      JR           NZ,$57DF
57BF: 20 FF      JR           NZ,$57C0
57C1: 54         LD           D,H
57C2: 68         LD           L,B
57C3: 69         LD           L,C
57C4: 73         LD           (HL),E
57C5: 20 72      JR           NZ,$5839
57C7: 6F         LD           L,A
57C8: 63         LD           H,E
57C9: 6B         LD           L,E
57CA: 20 68      JR           NZ,$5834
57CC: 61         LD           H,C
57CD: 73         LD           (HL),E
57CE: 20 20      JR           NZ,$57F0
57D0: 20 6D      JR           NZ,$583F
57D2: 61         LD           H,C
57D3: 6E         LD           L,(HL)
57D4: 79         LD           A,C
57D5: 20 63      JR           NZ,$583A
57D7: 72         LD           (HL),D
57D8: 61         LD           H,C
57D9: 63         LD           H,E
57DA: 6B         LD           L,E
57DB: 73         LD           (HL),E
57DC: 2E 2E      LD           L,$2E
57DE: 2E 20      LD           L,$20
57E0: 20 54      JR           NZ,$5836
57E2: 68         LD           L,B
57E3: 65         LD           H,L
57E4: 72         LD           (HL),D
57E5: 65         LD           H,L
57E6: 20 6D      JR           NZ,$5855
57E8: 75         LD           (HL),L
57E9: 73         LD           (HL),E
57EA: 74         LD           (HL),H
57EB: 20 62      JR           NZ,$584F
57ED: 65         LD           H,L
57EE: 20 20      JR           NZ,$5810
57F0: 20 73      JR           NZ,$5865
57F2: 6F         LD           L,A
57F3: 6D         LD           L,L
57F4: 65         LD           H,L
57F5: 20 77      JR           NZ,$586E
57F7: 61         LD           H,C
57F8: 79         LD           A,C
57F9: 20 74      JR           NZ,$586F
57FB: 6F         LD           L,A
57FC: 20 20      JR           NZ,$581E
57FE: 20 20      JR           NZ,$5820
5800: 20 73      JR           NZ,$5875
5802: 68         LD           L,B
5803: 61         LD           H,C
5804: 74         LD           (HL),H
5805: 74         LD           (HL),H
5806: 65         LD           H,L
5807: 72         LD           (HL),D
5808: 20 69      JR           NZ,$5873
580A: 74         LD           (HL),H
580B: 2E 2E      LD           L,$2E
580D: 2E FF      LD           L,$FF
580F: 4F         LD           C,A
5810: 68         LD           L,B
5811: 3F         CCF
5812: 20 57      JR           NZ,$586B
5814: 68         LD           L,B
5815: 61         LD           H,C
5816: 74         LD           (HL),H
5817: 20 61      JR           NZ,$587A
5819: 20 77      JR           NZ,$5892
581B: 65         LD           H,L
581C: 69         LD           L,C
581D: 72         LD           (HL),D
581E: 64         LD           H,H
581F: 6F         LD           L,A
5820: 62         LD           H,D
5821: 6A         LD           L,D
5822: 65         LD           H,L
5823: 63         LD           H,E
5824: 74         LD           (HL),H
5825: 21 20 20   LD           HL,$2020
5828: 54         LD           D,H
5829: 68         LD           L,B
582A: 65         LD           H,L
582B: 72         LD           (HL),D
582C: 65         LD           H,L
582D: 20 20      JR           NZ,$584F
582F: 6D         LD           L,L
5830: 75         LD           (HL),L
5831: 73         LD           (HL),E
5832: 74         LD           (HL),H
5833: 20 62      JR           NZ,$5897
5835: 65         LD           H,L
5836: 20 73      JR           NZ,$58AB
5838: 6F         LD           L,A
5839: 6D         LD           L,L
583A: 65         LD           H,L
583B: 20 77      JR           NZ,$58B4
583D: 61         LD           H,C
583E: 79         LD           A,C
583F: 74         LD           (HL),H
5840: 6F         LD           L,A
5841: 20 74      JR           NZ,$58B7
5843: 61         LD           H,C
5844: 63         LD           H,E
5845: 6B         LD           L,E
5846: 6C         LD           L,H
5847: 65         LD           H,L
5848: 20 74      JR           NZ,$58BE
584A: 68         LD           L,B
584B: 69         LD           L,C
584C: 73         LD           (HL),E
584D: 20 20      JR           NZ,$586F
584F: 6F         LD           L,A
5850: 62         LD           H,D
5851: 73         LD           (HL),E
5852: 74         LD           (HL),H
5853: 61         LD           H,C
5854: 63         LD           H,E
5855: 6C         LD           L,H
5856: 65         LD           H,L
5857: 2E FF      LD           L,$FF
5859: 48         LD           C,B
585A: 75         LD           (HL),L
585B: 6E         LD           L,(HL)
585C: 68         LD           L,B
585D: 3F         CCF
585E: 20 20      JR           NZ,$5880
5860: 54         LD           D,H
5861: 68         LD           L,B
5862: 69         LD           L,C
5863: 73         LD           (HL),E
5864: 20 72      JR           NZ,$58D8
5866: 6F         LD           L,A
5867: 63         LD           H,E
5868: 6B         LD           L,E
5869: 68         LD           L,B
586A: 61         LD           H,C
586B: 73         LD           (HL),E
586C: 20 61      JR           NZ,$58CF
586E: 20 6B      JR           NZ,$58DB
5870: 65         LD           H,L
5871: 79         LD           A,C
5872: 20 68      JR           NZ,$58DC
5874: 6F         LD           L,A
5875: 6C         LD           L,H
5876: 65         LD           H,L
5877: 21 20 59   LD           HL,$5920
587A: 6F         LD           L,A
587B: 75         LD           (HL),L
587C: 20 73      JR           NZ,$58F1
587E: 68         LD           L,B
587F: 6F         LD           L,A
5880: 75         LD           (HL),L
5881: 6C         LD           L,H
5882: 64         LD           H,H
5883: 20 63      JR           NZ,$58E8
5885: 6F         LD           L,A
5886: 6D         LD           L,L
5887: 65         LD           H,L
5888: 20 62      JR           NZ,$58EC
588A: 61         LD           H,C
588B: 63         LD           H,E
588C: 6B         LD           L,E
588D: 20 77      JR           NZ,$5906
588F: 69         LD           L,C
5890: 74         LD           (HL),H
5891: 68         LD           L,B
5892: 20 61      JR           NZ,$58F5
5894: 20 6B      JR           NZ,$5901
5896: 65         LD           H,L
5897: 79         LD           A,C
5898: 21 FF 57   LD           HL,$57FF
589B: 6F         LD           L,A
589C: 77         LD           (HL),A
589D: 21 20 20   LD           HL,$2020
58A0: 54         LD           D,H
58A1: 68         LD           L,B
58A2: 69         LD           L,C
58A3: 73         LD           (HL),E
58A4: 20 6C      JR           NZ,$5912
58A6: 6F         LD           L,A
58A7: 6F         LD           L,A
58A8: 6B         LD           L,E
58A9: 73         LD           (HL),E
58AA: 70         LD           (HL),B
58AB: 72         LD           (HL),D
58AC: 65         LD           H,L
58AD: 74         LD           (HL),H
58AE: 74         LD           (HL),H
58AF: 79         LD           A,C
58B0: 20 68      JR           NZ,$591A
58B2: 65         LD           H,L
58B3: 61         LD           H,C
58B4: 76         HALT
58B5: 79         LD           A,C
58B6: 21 20 20   LD           HL,$2020
58B9: 20 59      JR           NZ,$5914
58BB: 6F         LD           L,A
58BC: 75         LD           (HL),L
58BD: 20 77      JR           NZ,$5936
58BF: 6F         LD           L,A
58C0: 6E         LD           L,(HL)
58C1: 5E         LD           E,(HL)
58C2: 74         LD           (HL),H
58C3: 20 62      JR           NZ,$5927
58C5: 65         LD           H,L
58C6: 20 20      JR           NZ,$58E8
58C8: 20 20      JR           NZ,$58EA
58CA: 61         LD           H,C
58CB: 62         LD           H,D
58CC: 6C         LD           L,H
58CD: 65         LD           H,L
58CE: 20 74      JR           NZ,$5944
58D0: 6F         LD           L,A
58D1: 20 6C      JR           NZ,$593F
58D3: 69         LD           L,C
58D4: 66         LD           H,(HL)
58D5: 74         LD           (HL),H
58D6: 20 69      JR           NZ,$5941
58D8: 74         LD           (HL),H
58D9: 20 77      JR           NZ,$5952
58DB: 69         LD           L,C
58DC: 74         LD           (HL),H
58DD: 68         LD           L,B
58DE: 20 6A      JR           NZ,$594A
58E0: 75         LD           (HL),L
58E1: 73         LD           (HL),E
58E2: 74         LD           (HL),H
58E3: 20 79      JR           NZ,$595E
58E5: 6F         LD           L,A
58E6: 75         LD           (HL),L
58E7: 72         LD           (HL),D
58E8: 20 20      JR           NZ,$590A
58EA: 62         LD           H,D
58EB: 61         LD           H,C
58EC: 72         LD           (HL),D
58ED: 65         LD           H,L
58EE: 20 68      JR           NZ,$5958
58F0: 61         LD           H,C
58F1: 6E         LD           L,(HL)
58F2: 64         LD           H,H
58F3: 73         LD           (HL),E
58F4: 2E 2E      LD           L,$2E
58F6: 2E FF      LD           L,$FF
58F8: 57         LD           D,A
58F9: 65         LD           H,L
58FA: 6C         LD           L,H
58FB: 6C         LD           L,H
58FC: 2C         INC         L
58FD: 20 69      JR           NZ,$5968
58FF: 74         LD           (HL),H
5900: 5E         LD           E,(HL)
5901: 73         LD           (HL),E
5902: 20 61      JR           NZ,$5965
5904: 6E         LD           L,(HL)
5905: 20 20      JR           NZ,$5927
5907: 20 4F      JR           NZ,$5958
5909: 63         LD           H,E
590A: 61         LD           H,C
590B: 72         LD           (HL),D
590C: 69         LD           L,C
590D: 6E         LD           L,(HL)
590E: 61         LD           H,C
590F: 2C         INC         L
5910: 20 62      JR           NZ,$5974
5912: 75         LD           (HL),L
5913: 74         LD           (HL),H
5914: 20 79      JR           NZ,$598F
5916: 6F         LD           L,A
5917: 75         LD           (HL),L
5918: 64         LD           H,H
5919: 6F         LD           L,A
591A: 6E         LD           L,(HL)
591B: 5E         LD           E,(HL)
591C: 74         LD           (HL),H
591D: 20 6B      JR           NZ,$598A
591F: 6E         LD           L,(HL)
5920: 6F         LD           L,A
5921: 77         LD           (HL),A
5922: 20 68      JR           NZ,$598C
5924: 6F         LD           L,A
5925: 77         LD           (HL),A
5926: 20 20      JR           NZ,$5948
5928: 74         LD           (HL),H
5929: 6F         LD           L,A
592A: 20 70      JR           NZ,$599C
592C: 6C         LD           L,H
592D: 61         LD           H,C
592E: 79         LD           A,C
592F: 20 69      JR           NZ,$599A
5931: 74         LD           (HL),H
5932: 2E 2E      LD           L,$2E
5934: 2E FF      LD           L,$FF
5936: 4E         LD           C,(HL)
5937: 6F         LD           L,A
5938: 21 20 20   LD           HL,$2020
593B: 4E         LD           C,(HL)
593C: 6F         LD           L,A
593D: 21 20 20   LD           HL,$2020
5940: 50         LD           D,B
5941: 6F         LD           L,A
5942: 6F         LD           L,A
5943: 72         LD           (HL),D
5944: 20 20      JR           NZ,$5966
5946: 68         LD           L,B
5947: 65         LD           H,L
5948: 6E         LD           L,(HL)
5949: 21 20 20   LD           HL,$2020
594C: 53         LD           D,E
594D: 74         LD           (HL),H
594E: 6F         LD           L,A
594F: 70         LD           (HL),B
5950: 20 74      JR           NZ,$59C6
5952: 68         LD           L,B
5953: 61         LD           H,C
5954: 74         LD           (HL),H
5955: 21 FF 59   LD           HL,$59FF
5958: 6F         LD           L,A
5959: 75         LD           (HL),L
595A: 20 66      JR           NZ,$59C2
595C: 6F         LD           L,A
595D: 75         LD           (HL),L
595E: 6E         LD           L,(HL)
595F: 64         LD           H,H
5960: 20 74      JR           NZ,$59D6
5962: 68         LD           L,B
5963: 65         LD           H,L
5964: 20 20      JR           NZ,$5986
5966: 20 50      JR           NZ,$59B8
5968: 6F         LD           L,A
5969: 77         LD           (HL),A
596A: 65         LD           H,L
596B: 72         LD           (HL),D
596C: 20 42      JR           NZ,$59B0
596E: 72         LD           (HL),D
596F: 61         LD           H,C
5970: 63         LD           H,E
5971: 65         LD           H,L
5972: 6C         LD           L,H
5973: 65         LD           H,L
5974: 74         LD           (HL),H
5975: 21 20 41   LD           HL,$4120
5978: 74         LD           (HL),H
5979: 20 6C      JR           NZ,$59E7
597B: 61         LD           H,C
597C: 73         LD           (HL),E
597D: 74         LD           (HL),H
597E: 2C         INC         L
597F: 20 79      JR           NZ,$59FA
5981: 6F         LD           L,A
5982: 75         LD           (HL),L
5983: 20 63      JR           NZ,$59E8
5985: 61         LD           H,C
5986: 6E         LD           L,(HL)
5987: 70         LD           (HL),B
5988: 69         LD           L,C
5989: 63         LD           H,E
598A: 6B         LD           L,E
598B: 20 75      JR           NZ,$5A02
598D: 70         LD           (HL),B
598E: 20 70      JR           NZ,$5A00
5990: 6F         LD           L,A
5991: 74         LD           (HL),H
5992: 73         LD           (HL),E
5993: 20 61      JR           NZ,$59F6
5995: 6E         LD           L,(HL)
5996: 64         LD           H,H
5997: 73         LD           (HL),E
5998: 74         LD           (HL),H
5999: 6F         LD           L,A
599A: 6E         LD           L,(HL)
599B: 65         LD           H,L
599C: 73         LD           (HL),E
599D: 21 FF 59   LD           HL,$59FF
59A0: 6F         LD           L,A
59A1: 75         LD           (HL),L
59A2: 20 67      JR           NZ,$5A0B
59A4: 6F         LD           L,A
59A5: 74         LD           (HL),H
59A6: 20 79      JR           NZ,$5A21
59A8: 6F         LD           L,A
59A9: 75         LD           (HL),L
59AA: 72         LD           (HL),D
59AB: 20 20      JR           NZ,$59CD
59AD: 20 20      JR           NZ,$59CF
59AF: 53         LD           D,E
59B0: 68         LD           L,B
59B1: 69         LD           L,C
59B2: 65         LD           H,L
59B3: 6C         LD           L,H
59B4: 64         LD           H,H
59B5: 20 62      JR           NZ,$5A19
59B7: 61         LD           H,C
59B8: 63         LD           H,E
59B9: 6B         LD           L,E
59BA: 21 20 20   LD           HL,$2020
59BD: 20 20      JR           NZ,$59DF
59BF: 59         LD           E,C
59C0: 6F         LD           L,A
59C1: 75         LD           (HL),L
59C2: 20 63      JR           NZ,$5A27
59C4: 61         LD           H,C
59C5: 6E         LD           L,(HL)
59C6: 20 75      JR           NZ,$5A3D
59C8: 73         LD           (HL),E
59C9: 65         LD           H,L
59CA: 20 69      JR           NZ,$5A35
59CC: 74         LD           (HL),H
59CD: 20 20      JR           NZ,$59EF
59CF: 74         LD           (HL),H
59D0: 6F         LD           L,A
59D1: 20 66      JR           NZ,$5A39
59D3: 6C         LD           L,H
59D4: 69         LD           L,C
59D5: 70         LD           (HL),B
59D6: 20 65      JR           NZ,$5A3D
59D8: 6E         LD           L,(HL)
59D9: 65         LD           H,L
59DA: 6D         LD           L,L
59DB: 69         LD           L,C
59DC: 65         LD           H,L
59DD: 73         LD           (HL),E
59DE: 21 FF 41   LD           HL,$41FF
59E1: 68         LD           L,B
59E2: 68         LD           L,B
59E3: 68         LD           L,B
59E4: 2E 2E      LD           L,$2E
59E6: 2E 20      LD           L,$20
59E8: 59         LD           E,C
59E9: 65         LD           H,L
59EA: 73         LD           (HL),E
59EB: 73         LD           (HL),E
59EC: 2E 2E      LD           L,$2E
59EE: 2E 20      LD           L,$20
59F0: 54         LD           D,H
59F1: 68         LD           L,B
59F2: 61         LD           H,C
59F3: 74         LD           (HL),H
59F4: 20 64      JR           NZ,$5A5A
59F6: 75         LD           (HL),L
59F7: 73         LD           (HL),E
59F8: 74         LD           (HL),H
59F9: 20 77      JR           NZ,$5A72
59FB: 61         LD           H,C
59FC: 73         LD           (HL),E
59FD: 20 73      JR           NZ,$5A72
59FF: 6F         LD           L,A
5A00: 72         LD           (HL),D
5A01: 65         LD           H,L
5A02: 66         LD           H,(HL)
5A03: 72         LD           (HL),D
5A04: 65         LD           H,L
5A05: 73         LD           (HL),E
5A06: 68         LD           L,B
5A07: 69         LD           L,C
5A08: 6E         LD           L,(HL)
5A09: 67         LD           H,A
5A0A: 2E 2E      LD           L,$2E
5A0C: 2E 20      LD           L,$20
5A0E: 20 20      JR           NZ,$5A30
5A10: 46         LD           B,(HL)
5A11: 6F         LD           L,A
5A12: 72         LD           (HL),D
5A13: 20 74      JR           NZ,$5A89
5A15: 68         LD           L,B
5A16: 61         LD           H,C
5A17: 74         LD           (HL),H
5A18: 2C         INC         L
5A19: 20 49      JR           NZ,$5A64
5A1B: 5E         LD           E,(HL)
5A1C: 6C         LD           L,H
5A1D: 6C         LD           L,H
5A1E: 20 20      JR           NZ,$5A40
5A20: 74         LD           (HL),H
5A21: 65         LD           H,L
5A22: 6C         LD           L,H
5A23: 6C         LD           L,H
5A24: 20 79      JR           NZ,$5A9F
5A26: 6F         LD           L,A
5A27: 75         LD           (HL),L
5A28: 20 61      JR           NZ,$5A8B
5A2A: 20 68      JR           NZ,$5A94
5A2C: 69         LD           L,C
5A2D: 6E         LD           L,(HL)
5A2E: 74         LD           (HL),H
5A2F: 21 55 73   LD           HL,$7355
5A32: 65         LD           H,L
5A33: 20 61      JR           NZ,$5A96
5A35: 20 42      JR           NZ,$5A79
5A37: 6F         LD           L,A
5A38: 6D         LD           L,L
5A39: 62         LD           H,D
5A3A: 20 69      JR           NZ,$5AA5
5A3C: 6E         LD           L,(HL)
5A3D: 20 61      JR           NZ,$5AA0
5A3F: 20 70      JR           NZ,$5AB1
5A41: 6C         LD           L,H
5A42: 61         LD           H,C
5A43: 63         LD           H,E
5A44: 65         LD           H,L
5A45: 20 77      JR           NZ,$5ABE
5A47: 68         LD           L,B
5A48: 65         LD           H,L
5A49: 72         LD           (HL),D
5A4A: 65         LD           H,L
5A4B: 20 74      JR           NZ,$5AC1
5A4D: 68         LD           L,B
5A4E: 65         LD           H,L
5A4F: 20 73      JR           NZ,$5AC4
5A51: 61         LD           H,C
5A52: 6E         LD           L,(HL)
5A53: 64         LD           H,H
5A54: 20 73      JR           NZ,$5AC9
5A56: 77         LD           (HL),A
5A57: 61         LD           H,C
5A58: 6C         LD           L,H
5A59: 6C         LD           L,H
5A5A: 6F         LD           L,A
5A5B: 77         LD           (HL),A
5A5C: 73         LD           (HL),E
5A5D: 20 20      JR           NZ,$5A7F
5A5F: 20 79      JR           NZ,$5ADA
5A61: 6F         LD           L,A
5A62: 75         LD           (HL),L
5A63: 2E 2E      LD           L,$2E
5A65: 2E 20      LD           L,$20
5A67: 54         LD           D,H
5A68: 68         LD           L,B
5A69: 65         LD           H,L
5A6A: 72         LD           (HL),D
5A6B: 65         LD           H,L
5A6C: 20 69      JR           NZ,$5AD7
5A6E: 73         LD           (HL),E
5A6F: 20 61      JR           NZ,$5AD2
5A71: 20 74      JR           NZ,$5AE7
5A73: 72         LD           (HL),D
5A74: 65         LD           H,L
5A75: 61         LD           H,C
5A76: 74         LD           (HL),H
5A77: 20 6F      JR           NZ,$5AE8
5A79: 6E         LD           L,(HL)
5A7A: 20 74      JR           NZ,$5AF0
5A7C: 68         LD           L,B
5A7D: 65         LD           H,L
5A7E: 20 20      JR           NZ,$5AA0
5A80: 6F         LD           L,A
5A81: 74         LD           (HL),H
5A82: 68         LD           L,B
5A83: 65         LD           H,L
5A84: 72         LD           (HL),D
5A85: 20 73      JR           NZ,$5AFA
5A87: 69         LD           L,C
5A88: 64         LD           H,H
5A89: 65         LD           H,L
5A8A: 20 6F      JR           NZ,$5AFB
5A8C: 66         LD           H,(HL)
5A8D: 20 20      JR           NZ,$5AAF
5A8F: 20 74      JR           NZ,$5B05
5A91: 68         LD           L,B
5A92: 65         LD           H,L
5A93: 20 77      JR           NZ,$5B0C
5A95: 61         LD           H,C
5A96: 6C         LD           L,H
5A97: 6C         LD           L,H
5A98: 2E 2E      LD           L,$2E
5A9A: 2E 20      LD           L,$20
5A9C: 42         LD           B,D
5A9D: 79         LD           A,C
5A9E: 65         LD           H,L
5A9F: 21 FF 59   LD           HL,$59FF
5AA2: 6F         LD           L,A
5AA3: 75         LD           (HL),L
5AA4: 5E         LD           E,(HL)
5AA5: 76         HALT
5AA6: 65         LD           H,L
5AA7: 20 67      JR           NZ,$5B10
5AA9: 6F         LD           L,A
5AAA: 74         LD           (HL),H
5AAB: 20 74      JR           NZ,$5B21
5AAD: 68         LD           L,B
5AAE: 65         LD           H,L
5AAF: 20 20      JR           NZ,$5AD1
5AB1: 48         LD           C,B
5AB2: 6F         LD           L,A
5AB3: 6F         LD           L,A
5AB4: 6B         LD           L,E
5AB5: 20 53      JR           NZ,$5B0A
5AB7: 68         LD           L,B
5AB8: 6F         LD           L,A
5AB9: 74         LD           (HL),H
5ABA: 21 20 20   LD           HL,$2020
5ABD: 49         LD           C,C
5ABE: 74         LD           (HL),H
5ABF: 73         LD           (HL),E
5AC0: 20 63      JR           NZ,$5B25
5AC2: 68         LD           L,B
5AC3: 61         LD           H,C
5AC4: 69         LD           L,C
5AC5: 6E         LD           L,(HL)
5AC6: 20 73      JR           NZ,$5B3B
5AC8: 74         LD           (HL),H
5AC9: 72         LD           (HL),D
5ACA: 65         LD           H,L
5ACB: 74         LD           (HL),H
5ACC: 63         LD           H,E
5ACD: 68         LD           L,B
5ACE: 65         LD           H,L
5ACF: 73         LD           (HL),E
5AD0: 20 6C      JR           NZ,$5B3E
5AD2: 6F         LD           L,A
5AD3: 6E         LD           L,(HL)
5AD4: 67         LD           H,A
5AD5: 20 77      JR           NZ,$5B4E
5AD7: 68         LD           L,B
5AD8: 65         LD           H,L
5AD9: 6E         LD           L,(HL)
5ADA: 20 79      JR           NZ,$5B55
5ADC: 6F         LD           L,A
5ADD: 75         LD           (HL),L
5ADE: 20 20      JR           NZ,$5B00
5AE0: 20 75      JR           NZ,$5B57
5AE2: 73         LD           (HL),E
5AE3: 65         LD           H,L
5AE4: 20 69      JR           NZ,$5B4F
5AE6: 74         LD           (HL),H
5AE7: 21 FF 59   LD           HL,$59FF
5AEA: 6F         LD           L,A
5AEB: 75         LD           (HL),L
5AEC: 5E         LD           E,(HL)
5AED: 76         HALT
5AEE: 65         LD           H,L
5AEF: 20 67      JR           NZ,$5B58
5AF1: 6F         LD           L,A
5AF2: 74         LD           (HL),H
5AF3: 20 74      JR           NZ,$5B69
5AF5: 68         LD           L,B
5AF6: 65         LD           H,L
5AF7: 20 20      JR           NZ,$5B19
5AF9: 4D         LD           C,L
5AFA: 61         LD           H,C
5AFB: 67         LD           H,A
5AFC: 69         LD           L,C
5AFD: 63         LD           H,E
5AFE: 20 52      JR           NZ,$5B52
5B00: 6F         LD           L,A
5B01: 64         LD           H,H
5B02: 21 20 20   LD           HL,$2020
5B05: 4E         LD           C,(HL)
5B06: 6F         LD           L,A
5B07: 77         LD           (HL),A
5B08: 20 79      JR           NZ,$5B83
5B0A: 6F         LD           L,A
5B0B: 75         LD           (HL),L
5B0C: 20 63      JR           NZ,$5B71
5B0E: 61         LD           H,C
5B0F: 6E         LD           L,(HL)
5B10: 20 62      JR           NZ,$5B74
5B12: 75         LD           (HL),L
5B13: 72         LD           (HL),D
5B14: 6E         LD           L,(HL)
5B15: 20 20      JR           NZ,$5B37
5B17: 20 20      JR           NZ,$5B39
5B19: 74         LD           (HL),H
5B1A: 68         LD           L,B
5B1B: 69         LD           L,C
5B1C: 6E         LD           L,(HL)
5B1D: 67         LD           H,A
5B1E: 73         LD           (HL),E
5B1F: 21 20 42   LD           HL,$4220
5B22: 75         LD           (HL),L
5B23: 72         LD           (HL),D
5B24: 6E         LD           L,(HL)
5B25: 20 69      JR           NZ,$5B90
5B27: 74         LD           (HL),H
5B28: 21 42 75   LD           HL,$7542
5B2B: 72         LD           (HL),D
5B2C: 6E         LD           L,(HL)
5B2D: 2C         INC         L
5B2E: 20 62      JR           NZ,$5B92
5B30: 61         LD           H,C
5B31: 62         LD           H,D
5B32: 79         LD           A,C
5B33: 20 62      JR           NZ,$5B97
5B35: 75         LD           (HL),L
5B36: 72         LD           (HL),D
5B37: 6E         LD           L,(HL)
5B38: 21 FF 59   LD           HL,$59FF
5B3B: 6F         LD           L,A
5B3C: 75         LD           (HL),L
5B3D: 5E         LD           E,(HL)
5B3E: 76         HALT
5B3F: 65         LD           H,L
5B40: 20 67      JR           NZ,$5BA9
5B42: 6F         LD           L,A
5B43: 74         LD           (HL),H
5B44: 20 74      JR           NZ,$5BBA
5B46: 68         LD           L,B
5B47: 65         LD           H,L
5B48: 20 20      JR           NZ,$5B6A
5B4A: 50         LD           D,B
5B4B: 65         LD           H,L
5B4C: 67         LD           H,A
5B4D: 61         LD           H,C
5B4E: 73         LD           (HL),E
5B4F: 75         LD           (HL),L
5B50: 73         LD           (HL),E
5B51: 20 42      JR           NZ,$5B95
5B53: 6F         LD           L,A
5B54: 6F         LD           L,A
5B55: 74         LD           (HL),H
5B56: 73         LD           (HL),E
5B57: 21 20 20   LD           HL,$2020
5B5A: 49         LD           C,C
5B5B: 66         LD           H,(HL)
5B5C: 20 79      JR           NZ,$5BD7
5B5E: 6F         LD           L,A
5B5F: 75         LD           (HL),L
5B60: 20 68      JR           NZ,$5BCA
5B62: 6F         LD           L,A
5B63: 6C         LD           L,H
5B64: 64         LD           H,H
5B65: 20 64      JR           NZ,$5BCB
5B67: 6F         LD           L,A
5B68: 77         LD           (HL),A
5B69: 6E         LD           L,(HL)
5B6A: 74         LD           (HL),H
5B6B: 68         LD           L,B
5B6C: 65         LD           H,L
5B6D: 20 42      JR           NZ,$5BB1
5B6F: 75         LD           (HL),L
5B70: 74         LD           (HL),H
5B71: 74         LD           (HL),H
5B72: 6F         LD           L,A
5B73: 6E         LD           L,(HL)
5B74: 2C         INC         L
5B75: 20 79      JR           NZ,$5BF0
5B77: 6F         LD           L,A
5B78: 75         LD           (HL),L
5B79: 20 63      JR           NZ,$5BDE
5B7B: 61         LD           H,C
5B7C: 6E         LD           L,(HL)
5B7D: 20 64      JR           NZ,$5BE3
5B7F: 61         LD           H,C
5B80: 73         LD           (HL),E
5B81: 68         LD           L,B
5B82: 21 FF 59   LD           HL,$59FF
5B85: 6F         LD           L,A
5B86: 75         LD           (HL),L
5B87: 5E         LD           E,(HL)
5B88: 76         HALT
5B89: 65         LD           H,L
5B8A: 20 67      JR           NZ,$5BF3
5B8C: 6F         LD           L,A
5B8D: 74         LD           (HL),H
5B8E: 20 74      JR           NZ,$5C04
5B90: 68         LD           L,B
5B91: 65         LD           H,L
5B92: 20 20      JR           NZ,$5BB4
5B94: 4F         LD           C,A
5B95: 63         LD           H,E
5B96: 61         LD           H,C
5B97: 72         LD           (HL),D
5B98: 69         LD           L,C
5B99: 6E         LD           L,(HL)
5B9A: 61         LD           H,C
5B9B: 21 20 20   LD           HL,$2020
5B9E: 59         LD           E,C
5B9F: 6F         LD           L,A
5BA0: 75         LD           (HL),L
5BA1: 20 20      JR           NZ,$5BC3
5BA3: 20 73      JR           NZ,$5C18
5BA5: 68         LD           L,B
5BA6: 6F         LD           L,A
5BA7: 75         LD           (HL),L
5BA8: 6C         LD           L,H
5BA9: 64         LD           H,H
5BAA: 20 6C      JR           NZ,$5C18
5BAC: 65         LD           H,L
5BAD: 61         LD           H,C
5BAE: 72         LD           (HL),D
5BAF: 6E         LD           L,(HL)
5BB0: 20 74      JR           NZ,$5C26
5BB2: 6F         LD           L,A
5BB3: 20 70      JR           NZ,$5C25
5BB5: 6C         LD           L,H
5BB6: 61         LD           H,C
5BB7: 79         LD           A,C
5BB8: 20 6D      JR           NZ,$5C27
5BBA: 61         LD           H,C
5BBB: 6E         LD           L,(HL)
5BBC: 79         LD           A,C
5BBD: 20 73      JR           NZ,$5C32
5BBF: 6F         LD           L,A
5BC0: 6E         LD           L,(HL)
5BC1: 67         LD           H,A
5BC2: 73         LD           (HL),E
5BC3: 21 FF 59   LD           HL,$59FF
5BC6: 6F         LD           L,A
5BC7: 75         LD           (HL),L
5BC8: 5E         LD           E,(HL)
5BC9: 76         HALT
5BCA: 65         LD           H,L
5BCB: 20 67      JR           NZ,$5C34
5BCD: 6F         LD           L,A
5BCE: 74         LD           (HL),H
5BCF: 20 74      JR           NZ,$5C45
5BD1: 68         LD           L,B
5BD2: 65         LD           H,L
5BD3: 20 20      JR           NZ,$5BF5
5BD5: 52         LD           D,D
5BD6: 6F         LD           L,A
5BD7: 63         LD           H,E
5BD8: 5E         LD           E,(HL)
5BD9: 73         LD           (HL),E
5BDA: 20 46      JR           NZ,$5C22
5BDC: 65         LD           H,L
5BDD: 61         LD           H,C
5BDE: 74         LD           (HL),H
5BDF: 68         LD           L,B
5BE0: 65         LD           H,L
5BE1: 72         LD           (HL),D
5BE2: 21 20 20   LD           HL,$2020
5BE5: 49         LD           C,C
5BE6: 74         LD           (HL),H
5BE7: 20 66      JR           NZ,$5C4F
5BE9: 65         LD           H,L
5BEA: 65         LD           H,L
5BEB: 6C         LD           L,H
5BEC: 73         LD           (HL),E
5BED: 20 6C      JR           NZ,$5C5B
5BEF: 69         LD           L,C
5BF0: 6B         LD           L,E
5BF1: 65         LD           H,L
5BF2: 20 20      JR           NZ,$5C14
5BF4: 20 79      JR           NZ,$5C6F
5BF6: 6F         LD           L,A
5BF7: 75         LD           (HL),L
5BF8: 72         LD           (HL),D
5BF9: 20 62      JR           NZ,$5C5D
5BFB: 6F         LD           L,A
5BFC: 64         LD           H,H
5BFD: 79         LD           A,C
5BFE: 20 69      JR           NZ,$5C69
5C00: 73         LD           (HL),E
5C01: 20 61      JR           NZ,$5C64
5C03: 20 20      JR           NZ,$5C25
5C05: 6C         LD           L,H
5C06: 6F         LD           L,A
5C07: 74         LD           (HL),H
5C08: 20 6C      JR           NZ,$5C76
5C0A: 69         LD           L,C
5C0B: 67         LD           H,A
5C0C: 68         LD           L,B
5C0D: 74         LD           (HL),H
5C0E: 65         LD           H,L
5C0F: 72         LD           (HL),D
5C10: 21 FF 59   LD           HL,$59FF
5C13: 6F         LD           L,A
5C14: 75         LD           (HL),L
5C15: 5E         LD           E,(HL)
5C16: 76         HALT
5C17: 65         LD           H,L
5C18: 20 67      JR           NZ,$5C81
5C1A: 6F         LD           L,A
5C1B: 74         LD           (HL),H
5C1C: 20 61      JR           NZ,$5C7F
5C1E: 20 20      JR           NZ,$5C40
5C20: 20 20      JR           NZ,$5C42
5C22: 53         LD           D,E
5C23: 68         LD           L,B
5C24: 6F         LD           L,A
5C25: 76         HALT
5C26: 65         LD           H,L
5C27: 6C         LD           L,H
5C28: 21 20 20   LD           HL,$2020
5C2B: 4E         LD           C,(HL)
5C2C: 6F         LD           L,A
5C2D: 77         LD           (HL),A
5C2E: 20 79      JR           NZ,$5CA9
5C30: 6F         LD           L,A
5C31: 75         LD           (HL),L
5C32: 63         LD           H,E
5C33: 61         LD           H,C
5C34: 6E         LD           L,(HL)
5C35: 20 66      JR           NZ,$5C9D
5C37: 65         LD           H,L
5C38: 65         LD           H,L
5C39: 6C         LD           L,H
5C3A: 20 74      JR           NZ,$5CB0
5C3C: 68         LD           L,B
5C3D: 65         LD           H,L
5C3E: 20 6A      JR           NZ,$5CAA
5C40: 6F         LD           L,A
5C41: 79         LD           A,C
5C42: 6F         LD           L,A
5C43: 66         LD           H,(HL)
5C44: 20 64      JR           NZ,$5CAA
5C46: 69         LD           L,C
5C47: 67         LD           H,A
5C48: 67         LD           H,A
5C49: 69         LD           L,C
5C4A: 6E         LD           L,(HL)
5C4B: 67         LD           H,A
5C4C: 21 FF 59   LD           HL,$59FF
5C4F: 6F         LD           L,A
5C50: 75         LD           (HL),L
5C51: 5E         LD           E,(HL)
5C52: 76         HALT
5C53: 65         LD           H,L
5C54: 20 67      JR           NZ,$5CBD
5C56: 6F         LD           L,A
5C57: 74         LD           (HL),H
5C58: 20 73      JR           NZ,$5CCD
5C5A: 6F         LD           L,A
5C5B: 6D         LD           L,L
5C5C: 65         LD           H,L
5C5D: 20 4D      JR           NZ,$5CAC
5C5F: 61         LD           H,C
5C60: 67         LD           H,A
5C61: 69         LD           L,C
5C62: 63         LD           H,E
5C63: 20 50      JR           NZ,$5CB5
5C65: 6F         LD           L,A
5C66: 77         LD           (HL),A
5C67: 64         LD           H,H
5C68: 65         LD           H,L
5C69: 72         LD           (HL),D
5C6A: 21 20 20   LD           HL,$2020
5C6D: 20 54      JR           NZ,$5CC3
5C6F: 72         LD           (HL),D
5C70: 79         LD           A,C
5C71: 20 73      JR           NZ,$5CE6
5C73: 70         LD           (HL),B
5C74: 72         LD           (HL),D
5C75: 69         LD           L,C
5C76: 6E         LD           L,(HL)
5C77: 6B         LD           L,E
5C78: 6C         LD           L,H
5C79: 69         LD           L,C
5C7A: 6E         LD           L,(HL)
5C7B: 67         LD           H,A
5C7C: 20 20      JR           NZ,$5C9E
5C7E: 69         LD           L,C
5C7F: 74         LD           (HL),H
5C80: 20 6F      JR           NZ,$5CF1
5C82: 6E         LD           L,(HL)
5C83: 20 61      JR           NZ,$5CE6
5C85: 20 76      JR           NZ,$5CFD
5C87: 61         LD           H,C
5C88: 72         LD           (HL),D
5C89: 69         LD           L,C
5C8A: 65         LD           H,L
5C8B: 74         LD           (HL),H
5C8C: 79         LD           A,C
5C8D: 20 6F      JR           NZ,$5CFE
5C8F: 66         LD           H,(HL)
5C90: 20 74      JR           NZ,$5D06
5C92: 68         LD           L,B
5C93: 69         LD           L,C
5C94: 6E         LD           L,(HL)
5C95: 67         LD           H,A
5C96: 73         LD           (HL),E
5C97: 21 FF 59   LD           HL,$59FF
5C9A: 6F         LD           L,A
5C9B: 75         LD           (HL),L
5C9C: 20 66      JR           NZ,$5D04
5C9E: 6F         LD           L,A
5C9F: 75         LD           (HL),L
5CA0: 6E         LD           L,(HL)
5CA1: 64         LD           H,H
5CA2: 20 79      JR           NZ,$5D1D
5CA4: 6F         LD           L,A
5CA5: 75         LD           (HL),L
5CA6: 72         LD           (HL),D
5CA7: 20 20      JR           NZ,$5CC9
5CA9: 53         LD           D,E
5CAA: 77         LD           (HL),A
5CAB: 6F         LD           L,A
5CAC: 72         LD           (HL),D
5CAD: 64         LD           H,H
5CAE: 21 20 20   LD           HL,$2020
5CB1: 49         LD           C,C
5CB2: 74         LD           (HL),H
5CB3: 20 6D      JR           NZ,$5D22
5CB5: 75         LD           (HL),L
5CB6: 73         LD           (HL),E
5CB7: 74         LD           (HL),H
5CB8: 20 62      JR           NZ,$5D1C
5CBA: 65         LD           H,L
5CBB: 20 79      JR           NZ,$5D36
5CBD: 6F         LD           L,A
5CBE: 75         LD           (HL),L
5CBF: 72         LD           (HL),D
5CC0: 73         LD           (HL),E
5CC1: 20 62      JR           NZ,$5D25
5CC3: 65         LD           H,L
5CC4: 63         LD           H,E
5CC5: 61         LD           H,C
5CC6: 75         LD           (HL),L
5CC7: 73         LD           (HL),E
5CC8: 65         LD           H,L
5CC9: 69         LD           L,C
5CCA: 74         LD           (HL),H
5CCB: 20 68      JR           NZ,$5D35
5CCD: 61         LD           H,C
5CCE: 73         LD           (HL),E
5CCF: 20 79      JR           NZ,$5D4A
5CD1: 6F         LD           L,A
5CD2: 75         LD           (HL),L
5CD3: 72         LD           (HL),D
5CD4: 20 6E      JR           NZ,$5D44
5CD6: 61         LD           H,C
5CD7: 6D         LD           L,L
5CD8: 65         LD           H,L
5CD9: 65         LD           H,L
5CDA: 6E         LD           L,(HL)
5CDB: 67         LD           H,A
5CDC: 72         LD           (HL),D
5CDD: 61         LD           H,C
5CDE: 76         HALT
5CDF: 65         LD           H,L
5CE0: 64         LD           H,H
5CE1: 20 6F      JR           NZ,$5D52
5CE3: 6E         LD           L,(HL)
5CE4: 20 69      JR           NZ,$5D4F
5CE6: 74         LD           (HL),H
5CE7: 21 FF 59   LD           HL,$59FF
5CEA: 6F         LD           L,A
5CEB: 75         LD           (HL),L
5CEC: 5E         LD           E,(HL)
5CED: 76         HALT
5CEE: 65         LD           H,L
5CEF: 20 67      JR           NZ,$5D58
5CF1: 6F         LD           L,A
5CF2: 74         LD           (HL),H
5CF3: 20 74      JR           NZ,$5D69
5CF5: 68         LD           L,B
5CF6: 65         LD           H,L
5CF7: 20 20      JR           NZ,$5D19
5CF9: 46         LD           B,(HL)
5CFA: 6C         LD           L,H
5CFB: 69         LD           L,C
5CFC: 70         LD           (HL),B
5CFD: 70         LD           (HL),B
5CFE: 65         LD           H,L
5CFF: 72         LD           (HL),D
5D00: 73         LD           (HL),E
5D01: 21 20 49   LD           HL,$4920
5D04: 66         LD           H,(HL)
5D05: 20 79      JR           NZ,$5D80
5D07: 6F         LD           L,A
5D08: 75         LD           (HL),L
5D09: 70         LD           (HL),B
5D0A: 72         LD           (HL),D
5D0B: 65         LD           H,L
5D0C: 73         LD           (HL),E
5D0D: 73         LD           (HL),E
5D0E: 20 74      JR           NZ,$5D84
5D10: 68         LD           L,B
5D11: 65         LD           H,L
5D12: 20 42      JR           NZ,$5D56
5D14: 20 20      JR           NZ,$5D36
5D16: 20 20      JR           NZ,$5D38
5D18: 20 42      JR           NZ,$5D5C
5D1A: 75         LD           (HL),L
5D1B: 74         LD           (HL),H
5D1C: 74         LD           (HL),H
5D1D: 6F         LD           L,A
5D1E: 6E         LD           L,(HL)
5D1F: 20 77      JR           NZ,$5D98
5D21: 68         LD           L,B
5D22: 69         LD           L,C
5D23: 6C         LD           L,H
5D24: 65         LD           H,L
5D25: 20 79      JR           NZ,$5DA0
5D27: 6F         LD           L,A
5D28: 75         LD           (HL),L
5D29: 73         LD           (HL),E
5D2A: 77         LD           (HL),A
5D2B: 69         LD           L,C
5D2C: 6D         LD           L,L
5D2D: 2C         INC         L
5D2E: 20 79      JR           NZ,$5DA9
5D30: 6F         LD           L,A
5D31: 75         LD           (HL),L
5D32: 20 63      JR           NZ,$5D97
5D34: 61         LD           H,C
5D35: 6E         LD           L,(HL)
5D36: 20 20      JR           NZ,$5D58
5D38: 20 64      JR           NZ,$5D9E
5D3A: 69         LD           L,C
5D3B: 76         HALT
5D3C: 65         LD           H,L
5D3D: 20 75      JR           NZ,$5DB4
5D3F: 6E         LD           L,(HL)
5D40: 64         LD           H,H
5D41: 65         LD           H,L
5D42: 72         LD           (HL),D
5D43: 77         LD           (HL),A
5D44: 61         LD           H,C
5D45: 74         LD           (HL),H
5D46: 65         LD           H,L
5D47: 72         LD           (HL),D
5D48: 21 FF 59   LD           HL,$59FF
5D4B: 6F         LD           L,A
5D4C: 75         LD           (HL),L
5D4D: 5E         LD           E,(HL)
5D4E: 76         HALT
5D4F: 65         LD           H,L
5D50: 20 67      JR           NZ,$5DB9
5D52: 6F         LD           L,A
5D53: 74         LD           (HL),H
5D54: 20 74      JR           NZ,$5DCA
5D56: 68         LD           L,B
5D57: 65         LD           H,L
5D58: 20 20      JR           NZ,$5D7A
5D5A: 4D         LD           C,L
5D5B: 61         LD           H,C
5D5C: 67         LD           H,A
5D5D: 6E         LD           L,(HL)
5D5E: 69         LD           L,C
5D5F: 66         LD           H,(HL)
5D60: 79         LD           A,C
5D61: 69         LD           L,C
5D62: 6E         LD           L,(HL)
5D63: 67         LD           H,A
5D64: 20 4C      JR           NZ,$5DB2
5D66: 65         LD           H,L
5D67: 6E         LD           L,(HL)
5D68: 73         LD           (HL),E
5D69: 21 54 68   LD           HL,$6854
5D6C: 69         LD           L,C
5D6D: 73         LD           (HL),E
5D6E: 20 77      JR           NZ,$5DE7
5D70: 69         LD           L,C
5D71: 6C         LD           L,H
5D72: 6C         LD           L,H
5D73: 20 72      JR           NZ,$5DE7
5D75: 65         LD           H,L
5D76: 76         HALT
5D77: 65         LD           H,L
5D78: 61         LD           H,C
5D79: 6C         LD           L,H
5D7A: 6D         LD           L,L
5D7B: 61         LD           H,C
5D7C: 6E         LD           L,(HL)
5D7D: 79         LD           A,C
5D7E: 20 74      JR           NZ,$5DF4
5D80: 68         LD           L,B
5D81: 69         LD           L,C
5D82: 6E         LD           L,(HL)
5D83: 67         LD           H,A
5D84: 73         LD           (HL),E
5D85: 20 79      JR           NZ,$5E00
5D87: 6F         LD           L,A
5D88: 75         LD           (HL),L
5D89: 20 63      JR           NZ,$5DEE
5D8B: 6F         LD           L,A
5D8C: 75         LD           (HL),L
5D8D: 6C         LD           L,H
5D8E: 64         LD           H,H
5D8F: 6E         LD           L,(HL)
5D90: 5E         LD           E,(HL)
5D91: 74         LD           (HL),H
5D92: 20 73      JR           NZ,$5E07
5D94: 65         LD           H,L
5D95: 65         LD           H,L
5D96: 20 20      JR           NZ,$5DB8
5D98: 20 20      JR           NZ,$5DBA
5D9A: 62         LD           H,D
5D9B: 65         LD           H,L
5D9C: 66         LD           H,(HL)
5D9D: 6F         LD           L,A
5D9E: 72         LD           (HL),D
5D9F: 65         LD           H,L
5DA0: 21 FF 59   LD           HL,$59FF
5DA3: 6F         LD           L,A
5DA4: 75         LD           (HL),L
5DA5: 5E         LD           E,(HL)
5DA6: 76         HALT
5DA7: 65         LD           H,L
5DA8: 20 67      JR           NZ,$5E11
5DAA: 6F         LD           L,A
5DAB: 74         LD           (HL),H
5DAC: 20 61      JR           NZ,$5E0F
5DAE: 20 20      JR           NZ,$5DD0
5DB0: 20 20      JR           NZ,$5DD2
5DB2: 6E         LD           L,(HL)
5DB3: 65         LD           H,L
5DB4: 77         LD           (HL),A
5DB5: 20 53      JR           NZ,$5E0A
5DB7: 77         LD           (HL),A
5DB8: 6F         LD           L,A
5DB9: 72         LD           (HL),D
5DBA: 64         LD           H,H
5DBB: 21 20 20   LD           HL,$2020
5DBE: 59         LD           E,C
5DBF: 6F         LD           L,A
5DC0: 75         LD           (HL),L
5DC1: 20 73      JR           NZ,$5E36
5DC3: 68         LD           L,B
5DC4: 6F         LD           L,A
5DC5: 75         LD           (HL),L
5DC6: 6C         LD           L,H
5DC7: 64         LD           H,H
5DC8: 20 70      JR           NZ,$5E3A
5DCA: 75         LD           (HL),L
5DCB: 74         LD           (HL),H
5DCC: 20 79      JR           NZ,$5E47
5DCE: 6F         LD           L,A
5DCF: 75         LD           (HL),L
5DD0: 72         LD           (HL),D
5DD1: 20 6E      JR           NZ,$5E41
5DD3: 61         LD           H,C
5DD4: 6D         LD           L,L
5DD5: 65         LD           H,L
5DD6: 20 6F      JR           NZ,$5E47
5DD8: 6E         LD           L,(HL)
5DD9: 20 69      JR           NZ,$5E44
5DDB: 74         LD           (HL),H
5DDC: 20 72      JR           NZ,$5E50
5DDE: 69         LD           L,C
5DDF: 67         LD           H,A
5DE0: 68         LD           L,B
5DE1: 74         LD           (HL),H
5DE2: 61         LD           H,C
5DE3: 77         LD           (HL),A
5DE4: 61         LD           H,C
5DE5: 79         LD           A,C
5DE6: 21 FF 59   LD           HL,$59FF
5DE9: 6F         LD           L,A
5DEA: 75         LD           (HL),L
5DEB: 5E         LD           E,(HL)
5DEC: 76         HALT
5DED: 65         LD           H,L
5DEE: 20 67      JR           NZ,$5E57
5DF0: 6F         LD           L,A
5DF1: 74         LD           (HL),H
5DF2: 20 74      JR           NZ,$5E68
5DF4: 68         LD           L,B
5DF5: 65         LD           H,L
5DF6: 20 20      JR           NZ,$5E18
5DF8: 54         LD           D,H
5DF9: 61         LD           H,C
5DFA: 69         LD           L,C
5DFB: 6C         LD           L,H
5DFC: 20 4B      JR           NZ,$5E49
5DFE: 65         LD           H,L
5DFF: 79         LD           A,C
5E00: 21 20 20   LD           HL,$2020
5E03: 4E         LD           C,(HL)
5E04: 6F         LD           L,A
5E05: 77         LD           (HL),A
5E06: 20 20      JR           NZ,$5E28
5E08: 79         LD           A,C
5E09: 6F         LD           L,A
5E0A: 75         LD           (HL),L
5E0B: 20 63      JR           NZ,$5E70
5E0D: 61         LD           H,C
5E0E: 6E         LD           L,(HL)
5E0F: 20 6F      JR           NZ,$5E80
5E11: 70         LD           (HL),B
5E12: 65         LD           H,L
5E13: 6E         LD           L,(HL)
5E14: 20 74      JR           NZ,$5E8A
5E16: 68         LD           L,B
5E17: 65         LD           H,L
5E18: 54         LD           D,H
5E19: 61         LD           H,C
5E1A: 69         LD           L,C
5E1B: 6C         LD           L,H
5E1C: 20 43      JR           NZ,$5E61
5E1E: 61         LD           H,C
5E1F: 76         HALT
5E20: 65         LD           H,L
5E21: 20 67      JR           NZ,$5E8A
5E23: 61         LD           H,C
5E24: 74         LD           (HL),H
5E25: 65         LD           H,L
5E26: 21 FF 59   LD           HL,$59FF
5E29: 6F         LD           L,A
5E2A: 75         LD           (HL),L
5E2B: 5E         LD           E,(HL)
5E2C: 76         HALT
5E2D: 65         LD           H,L
5E2E: 20 67      JR           NZ,$5E97
5E30: 6F         LD           L,A
5E31: 74         LD           (HL),H
5E32: 20 74      JR           NZ,$5EA8
5E34: 68         LD           L,B
5E35: 65         LD           H,L
5E36: 20 20      JR           NZ,$5E58
5E38: 53         LD           D,E
5E39: 6C         LD           L,H
5E3A: 69         LD           L,C
5E3B: 6D         LD           L,L
5E3C: 65         LD           H,L
5E3D: 20 4B      JR           NZ,$5E8A
5E3F: 65         LD           H,L
5E40: 79         LD           A,C
5E41: 21 20 20   LD           HL,$2020
5E44: 4E         LD           C,(HL)
5E45: 6F         LD           L,A
5E46: 77         LD           (HL),A
5E47: 20 79      JR           NZ,$5EC2
5E49: 6F         LD           L,A
5E4A: 75         LD           (HL),L
5E4B: 20 63      JR           NZ,$5EB0
5E4D: 61         LD           H,C
5E4E: 6E         LD           L,(HL)
5E4F: 20 6F      JR           NZ,$5EC0
5E51: 70         LD           (HL),B
5E52: 65         LD           H,L
5E53: 6E         LD           L,(HL)
5E54: 20 74      JR           NZ,$5ECA
5E56: 68         LD           L,B
5E57: 65         LD           H,L
5E58: 67         LD           H,A
5E59: 61         LD           H,C
5E5A: 74         LD           (HL),H
5E5B: 65         LD           H,L
5E5C: 20 69      JR           NZ,$5EC7
5E5E: 6E         LD           L,(HL)
5E5F: 20 55      JR           NZ,$5EB6
5E61: 6B         LD           L,E
5E62: 75         LD           (HL),L
5E63: 6B         LD           L,E
5E64: 75         LD           (HL),L
5E65: 20 20      JR           NZ,$5E87
5E67: 20 50      JR           NZ,$5EB9
5E69: 72         LD           (HL),D
5E6A: 61         LD           H,C
5E6B: 69         LD           L,C
5E6C: 72         LD           (HL),D
5E6D: 69         LD           L,C
5E6E: 65         LD           H,L
5E6F: 21 FF 59   LD           HL,$59FF
5E72: 6F         LD           L,A
5E73: 75         LD           (HL),L
5E74: 5E         LD           E,(HL)
5E75: 76         HALT
5E76: 65         LD           H,L
5E77: 20 67      JR           NZ,$5EE0
5E79: 6F         LD           L,A
5E7A: 74         LD           (HL),H
5E7B: 20 74      JR           NZ,$5EF1
5E7D: 68         LD           L,B
5E7E: 65         LD           H,L
5E7F: 20 20      JR           NZ,$5EA1
5E81: 41         LD           B,C
5E82: 6E         LD           L,(HL)
5E83: 67         LD           H,A
5E84: 6C         LD           L,H
5E85: 65         LD           H,L
5E86: 72         LD           (HL),D
5E87: 20 4B      JR           NZ,$5ED4
5E89: 65         LD           H,L
5E8A: 79         LD           A,C
5E8B: 21 FF 59   LD           HL,$59FF
5E8E: 6F         LD           L,A
5E8F: 75         LD           (HL),L
5E90: 5E         LD           E,(HL)
5E91: 76         HALT
5E92: 65         LD           H,L
5E93: 20 67      JR           NZ,$5EFC
5E95: 6F         LD           L,A
5E96: 74         LD           (HL),H
5E97: 20 74      JR           NZ,$5F0D
5E99: 68         LD           L,B
5E9A: 65         LD           H,L
5E9B: 20 20      JR           NZ,$5EBD
5E9D: 46         LD           B,(HL)
5E9E: 61         LD           H,C
5E9F: 63         LD           H,E
5EA0: 65         LD           H,L
5EA1: 20 4B      JR           NZ,$5EEE
5EA3: 65         LD           H,L
5EA4: 79         LD           A,C
5EA5: 21 FF 59   LD           HL,$59FF
5EA8: 6F         LD           L,A
5EA9: 75         LD           (HL),L
5EAA: 5E         LD           E,(HL)
5EAB: 76         HALT
5EAC: 65         LD           H,L
5EAD: 20 67      JR           NZ,$5F16
5EAF: 6F         LD           L,A
5EB0: 74         LD           (HL),H
5EB1: 20 74      JR           NZ,$5F27
5EB3: 68         LD           L,B
5EB4: 65         LD           H,L
5EB5: 20 20      JR           NZ,$5ED7
5EB7: 42         LD           B,D
5EB8: 69         LD           L,C
5EB9: 72         LD           (HL),D
5EBA: 64         LD           H,H
5EBB: 20 4B      JR           NZ,$5F08
5EBD: 65         LD           H,L
5EBE: 79         LD           A,C
5EBF: 21 FF 41   LD           HL,$41FF
5EC2: 74         LD           (HL),H
5EC3: 20 6C      JR           NZ,$5F31
5EC5: 61         LD           H,C
5EC6: 73         LD           (HL),E
5EC7: 74         LD           (HL),H
5EC8: 2C         INC         L
5EC9: 20 79      JR           NZ,$5F44
5ECB: 6F         LD           L,A
5ECC: 75         LD           (HL),L
5ECD: 20 67      JR           NZ,$5F36
5ECF: 6F         LD           L,A
5ED0: 74         LD           (HL),H
5ED1: 61         LD           H,C
5ED2: 20 4D      JR           NZ,$5F21
5ED4: 61         LD           H,C
5ED5: 70         LD           (HL),B
5ED6: 21 20 20   LD           HL,$2020
5ED9: 50         LD           D,B
5EDA: 72         LD           (HL),D
5EDB: 65         LD           H,L
5EDC: 73         LD           (HL),E
5EDD: 73         LD           (HL),E
5EDE: 20 20      JR           NZ,$5F00
5EE0: 20 74      JR           NZ,$5F56
5EE2: 68         LD           L,B
5EE3: 65         LD           H,L
5EE4: 20 53      JR           NZ,$5F39
5EE6: 54         LD           D,H
5EE7: 41         LD           B,C
5EE8: 52         LD           D,D
5EE9: 54         LD           D,H
5EEA: 20 42      JR           NZ,$5F2E
5EEC: 75         LD           (HL),L
5EED: 74         LD           (HL),H
5EEE: 74         LD           (HL),H
5EEF: 6F         LD           L,A
5EF0: 6E         LD           L,(HL)
5EF1: 74         LD           (HL),H
5EF2: 6F         LD           L,A
5EF3: 20 6C      JR           NZ,$5F61
5EF5: 6F         LD           L,A
5EF6: 6F         LD           L,A
5EF7: 6B         LD           L,E
5EF8: 20 61      JR           NZ,$5F5B
5EFA: 74         LD           (HL),H
5EFB: 20 69      JR           NZ,$5F66
5EFD: 74         LD           (HL),H
5EFE: 21 FF 59   LD           HL,$59FF
5F01: 6F         LD           L,A
5F02: 75         LD           (HL),L
5F03: 5E         LD           E,(HL)
5F04: 76         HALT
5F05: 65         LD           H,L
5F06: 20 67      JR           NZ,$5F6F
5F08: 6F         LD           L,A
5F09: 74         LD           (HL),H
5F0A: 20 74      JR           NZ,$5F80
5F0C: 68         LD           L,B
5F0D: 65         LD           H,L
5F0E: 20 20      JR           NZ,$5F30
5F10: 43         LD           B,E
5F11: 6F         LD           L,A
5F12: 6D         LD           L,L
5F13: 70         LD           (HL),B
5F14: 61         LD           H,C
5F15: 73         LD           (HL),E
5F16: 73         LD           (HL),E
5F17: 21 20 20   LD           HL,$2020
5F1A: 4E         LD           C,(HL)
5F1B: 6F         LD           L,A
5F1C: 77         LD           (HL),A
5F1D: 2C         INC         L
5F1E: 20 20      JR           NZ,$5F40
5F20: 79         LD           A,C
5F21: 6F         LD           L,A
5F22: 75         LD           (HL),L
5F23: 20 63      JR           NZ,$5F88
5F25: 61         LD           H,C
5F26: 6E         LD           L,(HL)
5F27: 20 73      JR           NZ,$5F9C
5F29: 65         LD           H,L
5F2A: 65         LD           H,L
5F2B: 20 20      JR           NZ,$5F4D
5F2D: 20 20      JR           NZ,$5F4F
5F2F: 20 77      JR           NZ,$5FA8
5F31: 68         LD           L,B
5F32: 65         LD           H,L
5F33: 72         LD           (HL),D
5F34: 65         LD           H,L
5F35: 20 74      JR           NZ,$5FAB
5F37: 68         LD           L,B
5F38: 65         LD           H,L
5F39: 20 63      JR           NZ,$5F9E
5F3B: 68         LD           L,B
5F3C: 65         LD           H,L
5F3D: 73         LD           (HL),E
5F3E: 74         LD           (HL),H
5F3F: 73         LD           (HL),E
5F40: 61         LD           H,C
5F41: 6E         LD           L,(HL)
5F42: 64         LD           H,H
5F43: 20 4E      JR           NZ,$5F93
5F45: 69         LD           L,C
5F46: 67         LD           H,A
5F47: 68         LD           L,B
5F48: 74         LD           (HL),H
5F49: 6D         LD           L,L
5F4A: 61         LD           H,C
5F4B: 72         LD           (HL),D
5F4C: 65         LD           H,L
5F4D: 20 20      JR           NZ,$5F6F
5F4F: 20 61      JR           NZ,$5FB2
5F51: 72         LD           (HL),D
5F52: 65         LD           H,L
5F53: 20 68      JR           NZ,$5FBD
5F55: 69         LD           L,C
5F56: 64         LD           H,H
5F57: 64         LD           H,H
5F58: 65         LD           H,L
5F59: 6E         LD           L,(HL)
5F5A: 21 20 54   LD           HL,$5420
5F5D: 68         LD           L,B
5F5E: 69         LD           L,C
5F5F: 73         LD           (HL),E
5F60: 43         LD           B,E
5F61: 6F         LD           L,A
5F62: 6D         LD           L,L
5F63: 70         LD           (HL),B
5F64: 61         LD           H,C
5F65: 73         LD           (HL),E
5F66: 73         LD           (HL),E
5F67: 20 68      JR           NZ,$5FD1
5F69: 61         LD           H,C
5F6A: 73         LD           (HL),E
5F6B: 20 61      JR           NZ,$5FCE
5F6D: 20 20      JR           NZ,$5F8F
5F6F: 20 6E      JR           NZ,$5FDF
5F71: 65         LD           H,L
5F72: 77         LD           (HL),A
5F73: 20 66      JR           NZ,$5FDB
5F75: 65         LD           H,L
5F76: 61         LD           H,C
5F77: 74         LD           (HL),H
5F78: 75         LD           (HL),L
5F79: 72         LD           (HL),D
5F7A: 65         LD           H,L
5F7B: 2D         DEC         L
5F7C: 2D         DEC         L
5F7D: 20 61      JR           NZ,$5FE0
5F7F: 20 74      JR           NZ,$5FF5
5F81: 6F         LD           L,A
5F82: 6E         LD           L,(HL)
5F83: 65         LD           H,L
5F84: 20 77      JR           NZ,$5FFD
5F86: 69         LD           L,C
5F87: 6C         LD           L,H
5F88: 6C         LD           L,H
5F89: 20 74      JR           NZ,$5FFF
5F8B: 65         LD           H,L
5F8C: 6C         LD           L,H
5F8D: 6C         LD           L,H
5F8E: 20 20      JR           NZ,$5FB0
5F90: 79         LD           A,C
5F91: 6F         LD           L,A
5F92: 75         LD           (HL),L
5F93: 20 69      JR           NZ,$5FFE
5F95: 66         LD           H,(HL)
5F96: 20 61      JR           NZ,$5FF9
5F98: 20 6B      JR           NZ,$6005
5F9A: 65         LD           H,L
5F9B: 79         LD           A,C
5F9C: 20 69      JR           NZ,$6007
5F9E: 73         LD           (HL),E
5F9F: 20 68      JR           NZ,$6009
5FA1: 69         LD           L,C
5FA2: 64         LD           H,H
5FA3: 64         LD           H,H
5FA4: 65         LD           H,L
5FA5: 6E         LD           L,(HL)
5FA6: 20 69      JR           NZ,$6011
5FA8: 6E         LD           L,(HL)
5FA9: 20 61      JR           NZ,$600C
5FAB: 20 72      JR           NZ,$601F
5FAD: 6F         LD           L,A
5FAE: 6F         LD           L,A
5FAF: 6D         LD           L,L
5FB0: 77         LD           (HL),A
5FB1: 68         LD           L,B
5FB2: 65         LD           H,L
5FB3: 6E         LD           L,(HL)
5FB4: 20 79      JR           NZ,$602F
5FB6: 6F         LD           L,A
5FB7: 75         LD           (HL),L
5FB8: 20 65      JR           NZ,$601F
5FBA: 6E         LD           L,(HL)
5FBB: 74         LD           (HL),H
5FBC: 65         LD           H,L
5FBD: 72         LD           (HL),D
5FBE: 21 20 FF   LD           HL,$FF20
5FC1: 59         LD           E,C
5FC2: 6F         LD           L,A
5FC3: 75         LD           (HL),L
5FC4: 20 66      JR           NZ,$602C
5FC6: 6F         LD           L,A
5FC7: 75         LD           (HL),L
5FC8: 6E         LD           L,(HL)
5FC9: 64         LD           H,H
5FCA: 20 61      JR           NZ,$602D
5FCC: 20 20      JR           NZ,$5FEE
5FCE: 20 20      JR           NZ,$5FF0
5FD0: 20 66      JR           NZ,$6038
5FD2: 72         LD           (HL),D
5FD3: 61         LD           H,C
5FD4: 67         LD           H,A
5FD5: 6D         LD           L,L
5FD6: 65         LD           H,L
5FD7: 6E         LD           L,(HL)
5FD8: 74         LD           (HL),H
5FD9: 20 6F      JR           NZ,$604A
5FDB: 66         LD           H,(HL)
5FDC: 20 61      JR           NZ,$603F
5FDE: 20 20      JR           NZ,$6000
5FE0: 20 53      JR           NZ,$6035
5FE2: 74         LD           (HL),H
5FE3: 6F         LD           L,A
5FE4: 6E         LD           L,(HL)
5FE5: 65         LD           H,L
5FE6: 20 53      JR           NZ,$603B
5FE8: 6C         LD           L,H
5FE9: 61         LD           H,C
5FEA: 62         LD           H,D
5FEB: 21 20 20   LD           HL,$2020
5FEE: 4E         LD           C,(HL)
5FEF: 6F         LD           L,A
5FF0: 77         LD           (HL),A
5FF1: 79         LD           A,C
5FF2: 6F         LD           L,A
5FF3: 75         LD           (HL),L
5FF4: 20 63      JR           NZ,$6059
5FF6: 61         LD           H,C
5FF7: 6E         LD           L,(HL)
5FF8: 20 72      JR           NZ,$606C
5FFA: 65         LD           H,L
5FFB: 61         LD           H,C
5FFC: 64         LD           H,H
5FFD: 20 74      JR           NZ,$6073
5FFF: 68         LD           L,B
6000: 65         LD           H,L
6001: 6D         LD           L,L
6002: 65         LD           H,L
6003: 73         LD           (HL),E
6004: 73         LD           (HL),E
6005: 61         LD           H,C
6006: 67         LD           H,A
6007: 65         LD           H,L
6008: 20 6F      JR           NZ,$6079
600A: 6E         LD           L,(HL)
600B: 20 74      JR           NZ,$6081
600D: 68         LD           L,B
600E: 65         LD           H,L
600F: 20 20      JR           NZ,$6031
6011: 77         LD           (HL),A
6012: 61         LD           H,C
6013: 6C         LD           L,H
6014: 6C         LD           L,H
6015: 21 FF 59   LD           HL,$59FF
6018: 6F         LD           L,A
6019: 75         LD           (HL),L
601A: 5E         LD           E,(HL)
601B: 76         HALT
601C: 65         LD           H,L
601D: 20 67      JR           NZ,$6086
601F: 6F         LD           L,A
6020: 74         LD           (HL),H
6021: 20 74      JR           NZ,$6097
6023: 68         LD           L,B
6024: 65         LD           H,L
6025: 20 20      JR           NZ,$6047
6027: 4E         LD           C,(HL)
6028: 69         LD           L,C
6029: 67         LD           H,A
602A: 68         LD           L,B
602B: 74         LD           (HL),H
602C: 6D         LD           L,L
602D: 61         LD           H,C
602E: 72         LD           (HL),D
602F: 65         LD           H,L
6030: 5E         LD           E,(HL)
6031: 73         LD           (HL),E
6032: 20 4B      JR           NZ,$607F
6034: 65         LD           H,L
6035: 79         LD           A,C
6036: 21 4E 6F   LD           HL,$6F4E
6039: 77         LD           (HL),A
603A: 20 79      JR           NZ,$60B5
603C: 6F         LD           L,A
603D: 75         LD           (HL),L
603E: 20 63      JR           NZ,$60A3
6040: 61         LD           H,C
6041: 6E         LD           L,(HL)
6042: 20 6F      JR           NZ,$60B3
6044: 70         LD           (HL),B
6045: 65         LD           H,L
6046: 6E         LD           L,(HL)
6047: 74         LD           (HL),H
6048: 68         LD           L,B
6049: 65         LD           H,L
604A: 20 64      JR           NZ,$60B0
604C: 6F         LD           L,A
604D: 6F         LD           L,A
604E: 72         LD           (HL),D
604F: 20 74      JR           NZ,$60C5
6051: 6F         LD           L,A
6052: 20 74      JR           NZ,$60C8
6054: 68         LD           L,B
6055: 65         LD           H,L
6056: 20 4E      JR           NZ,$60A6
6058: 69         LD           L,C
6059: 67         LD           H,A
605A: 68         LD           L,B
605B: 74         LD           (HL),H
605C: 6D         LD           L,L
605D: 61         LD           H,C
605E: 72         LD           (HL),D
605F: 65         LD           H,L
6060: 5E         LD           E,(HL)
6061: 73         LD           (HL),E
6062: 20 20      JR           NZ,$6084
6064: 20 20      JR           NZ,$6086
6066: 20 4C      JR           NZ,$60B4
6068: 61         LD           H,C
6069: 69         LD           L,C
606A: 72         LD           (HL),D
606B: 21 FF 59   LD           HL,$59FF
606E: 6F         LD           L,A
606F: 75         LD           (HL),L
6070: 20 67      JR           NZ,$60D9
6072: 6F         LD           L,A
6073: 74         LD           (HL),H
6074: 20 61      JR           NZ,$60D7
6076: 20 53      JR           NZ,$60CB
6078: 6D         LD           L,L
6079: 61         LD           H,C
607A: 6C         LD           L,H
607B: 6C         LD           L,H
607C: 20 4B      JR           NZ,$60C9
607E: 65         LD           H,L
607F: 79         LD           A,C
6080: 21 20 20   LD           HL,$2020
6083: 59         LD           E,C
6084: 6F         LD           L,A
6085: 75         LD           (HL),L
6086: 20 63      JR           NZ,$60EB
6088: 61         LD           H,C
6089: 6E         LD           L,(HL)
608A: 20 20      JR           NZ,$60AC
608C: 20 6F      JR           NZ,$60FD
608E: 70         LD           (HL),B
608F: 65         LD           H,L
6090: 6E         LD           L,(HL)
6091: 20 61      JR           NZ,$60F4
6093: 20 6C      JR           NZ,$6101
6095: 6F         LD           L,A
6096: 63         LD           H,E
6097: 6B         LD           L,E
6098: 65         LD           H,L
6099: 64         LD           H,H
609A: 20 20      JR           NZ,$60BC
609C: 20 64      JR           NZ,$6102
609E: 6F         LD           L,A
609F: 6F         LD           L,A
60A0: 72         LD           (HL),D
60A1: 2E FF      LD           L,$FF
60A3: 20 20      JR           NZ,$60C5
60A5: 20 59      JR           NZ,$6100
60A7: 6F         LD           L,A
60A8: 75         LD           (HL),L
60A9: 20 67      JR           NZ,$6112
60AB: 6F         LD           L,A
60AC: 74         LD           (HL),H
60AD: 20 32      JR           NZ,$60E1
60AF: 30 20      JR           NC,$60D1
60B1: 20 20      JR           NZ,$60D3
60B3: 20 20      JR           NZ,$60D5
60B5: 20 20      JR           NZ,$60D7
60B7: 20 52      JR           NZ,$610B
60B9: 75         LD           (HL),L
60BA: 70         LD           (HL),B
60BB: 65         LD           H,L
60BC: 65         LD           H,L
60BD: 73         LD           (HL),E
60BE: 21 20 20   LD           HL,$2020
60C1: 20 20      JR           NZ,$60E3
60C3: 20 20      JR           NZ,$60E5
60C5: 20 20      JR           NZ,$60E7
60C7: 20 20      JR           NZ,$60E9
60C9: 4A         LD           C,D
60CA: 4F         LD           C,A
60CB: 59         LD           E,C
60CC: 21 FF 20   LD           HL,$20FF
60CF: 20 20      JR           NZ,$60F1
60D1: 20 59      JR           NZ,$612C
60D3: 6F         LD           L,A
60D4: 75         LD           (HL),L
60D5: 20 67      JR           NZ,$613E
60D7: 6F         LD           L,A
60D8: 74         LD           (HL),H
60D9: 20 35      JR           NZ,$6110
60DB: 30 20      JR           NC,$60FD
60DD: 20 20      JR           NZ,$60FF
60DF: 20 20      JR           NZ,$6101
60E1: 20 20      JR           NZ,$6103
60E3: 20 52      JR           NZ,$6137
60E5: 75         LD           (HL),L
60E6: 70         LD           (HL),B
60E7: 65         LD           H,L
60E8: 65         LD           H,L
60E9: 73         LD           (HL),E
60EA: 21 20 20   LD           HL,$2020
60ED: 20 20      JR           NZ,$610F
60EF: 20 20      JR           NZ,$6111
60F1: 20 56      JR           NZ,$6149
60F3: 65         LD           H,L
60F4: 72         LD           (HL),D
60F5: 79         LD           A,C
60F6: 20 4E      JR           NZ,$6146
60F8: 69         LD           L,C
60F9: 63         LD           H,E
60FA: 65         LD           H,L
60FB: 21 FF 20   LD           HL,$20FF
60FE: 20 20      JR           NZ,$6120
6100: 59         LD           E,C
6101: 6F         LD           L,A
6102: 75         LD           (HL),L
6103: 20 67      JR           NZ,$616C
6105: 6F         LD           L,A
6106: 74         LD           (HL),H
6107: 20 31      JR           NZ,$613A
6109: 30 30      JR           NC,$613B
610B: 20 20      JR           NZ,$612D
610D: 20 20      JR           NZ,$612F
610F: 20 20      JR           NZ,$6131
6111: 20 52      JR           NZ,$6165
6113: 75         LD           (HL),L
6114: 70         LD           (HL),B
6115: 65         LD           H,L
6116: 65         LD           H,L
6117: 73         LD           (HL),E
6118: 21 20 20   LD           HL,$2020
611B: 20 20      JR           NZ,$613D
611D: 20 20      JR           NZ,$613F
611F: 59         LD           E,C
6120: 6F         LD           L,A
6121: 75         LD           (HL),L
6122: 5E         LD           E,(HL)
6123: 72         LD           (HL),D
6124: 65         LD           H,L
6125: 20 48      JR           NZ,$616F
6127: 61         LD           H,C
6128: 70         LD           (HL),B
6129: 70         LD           (HL),B
612A: 79         LD           A,C
612B: 21 FF 20   LD           HL,$20FF
612E: 20 20      JR           NZ,$6150
6130: 59         LD           E,C
6131: 6F         LD           L,A
6132: 75         LD           (HL),L
6133: 20 67      JR           NZ,$619C
6135: 6F         LD           L,A
6136: 74         LD           (HL),H
6137: 20 32      JR           NZ,$616B
6139: 30 30      JR           NC,$616B
613B: 20 20      JR           NZ,$615D
613D: 20 20      JR           NZ,$615F
613F: 20 20      JR           NZ,$6161
6141: 20 52      JR           NZ,$6195
6143: 75         LD           (HL),L
6144: 70         LD           (HL),B
6145: 65         LD           H,L
6146: 65         LD           H,L
6147: 73         LD           (HL),E
6148: 21 20 20   LD           HL,$2020
614B: 20 20      JR           NZ,$616D
614D: 59         LD           E,C
614E: 6F         LD           L,A
614F: 75         LD           (HL),L
6150: 5E         LD           E,(HL)
6151: 72         LD           (HL),D
6152: 65         LD           H,L
6153: 20 45      JR           NZ,$619A
6155: 63         LD           H,E
6156: 73         LD           (HL),E
6157: 74         LD           (HL),H
6158: 61         LD           H,C
6159: 74         LD           (HL),H
615A: 69         LD           L,C
615B: 63         LD           H,E
615C: 21 FF 4C   LD           HL,$4CFF
615F: 65         LD           H,L
6160: 61         LD           H,C
6161: 76         HALT
6162: 65         LD           H,L
6163: 20 6D      JR           NZ,$61D2
6165: 65         LD           H,L
6166: 20 61      JR           NZ,$61C9
6168: 6C         LD           L,H
6169: 6F         LD           L,A
616A: 6E         LD           L,(HL)
616B: 65         LD           H,L
616C: 21 20 49   LD           HL,$4920
616F: 5E         LD           E,(HL)
6170: 6D         LD           L,L
6171: 20 74      JR           NZ,$61E7
6173: 72         LD           (HL),D
6174: 79         LD           A,C
6175: 69         LD           L,C
6176: 6E         LD           L,(HL)
6177: 67         LD           H,A
6178: 20 74      JR           NZ,$61EE
617A: 6F         LD           L,A
617B: 20 20      JR           NZ,$619D
617D: 20 73      JR           NZ,$61F2
617F: 69         LD           L,C
6180: 74         LD           (HL),H
6181: 20 73      JR           NZ,$61F6
6183: 74         LD           (HL),H
6184: 69         LD           L,C
6185: 6C         LD           L,H
6186: 6C         LD           L,H
6187: 20 73      JR           NZ,$61FC
6189: 6F         LD           L,A
618A: 20 20      JR           NZ,$61AC
618C: 20 20      JR           NZ,$61AE
618E: 53         LD           D,E
618F: 63         LD           H,E
6190: 68         LD           L,B
6191: 75         LD           (HL),L
6192: 6C         LD           L,H
6193: 65         LD           H,L
6194: 20 63      JR           NZ,$61F9
6196: 61         LD           H,C
6197: 6E         LD           L,(HL)
6198: 20 70      JR           NZ,$620A
619A: 61         LD           H,C
619B: 69         LD           L,C
619C: 6E         LD           L,(HL)
619D: 74         LD           (HL),H
619E: 6D         LD           L,L
619F: 79         LD           A,C
61A0: 20 70      JR           NZ,$6212
61A2: 6F         LD           L,A
61A3: 72         LD           (HL),D
61A4: 74         LD           (HL),H
61A5: 72         LD           (HL),D
61A6: 61         LD           H,C
61A7: 69         LD           L,C
61A8: 74         LD           (HL),H
61A9: 21 FF 42   LD           HL,$42FF
61AC: 55         LD           D,L
61AD: 5A         LD           E,D
61AE: 5A         LD           E,D
61AF: 5A         LD           E,D
61B0: 5A         LD           E,D
61B1: 5A         LD           E,D
61B2: 21 20 42   LD           HL,$4220
61B5: 55         LD           D,L
61B6: 5A         LD           E,D
61B7: 5A         LD           E,D
61B8: 5A         LD           E,D
61B9: 5A         LD           E,D
61BA: 21 20 20   LD           HL,$2020
61BD: 20 4F      JR           NZ,$620E
61BF: 55         LD           D,L
61C0: 54         LD           D,H
61C1: 5A         LD           E,D
61C2: 5A         LD           E,D
61C3: 5A         LD           E,D
61C4: 49         LD           C,C
61C5: 44         LD           B,H
61C6: 45         LD           B,L
61C7: 52         LD           D,D
61C8: 21 20 20   LD           HL,$2020
61CB: FF         RST         0X38
61CC: 4E         LD           C,(HL)
61CD: 45         LD           B,L
61CE: 45         LD           B,L
61CF: 4E         LD           C,(HL)
61D0: 45         LD           B,L
61D1: 52         LD           D,D
61D2: 20 4E      JR           NZ,$6222
61D4: 45         LD           B,L
61D5: 45         LD           B,L
61D6: 4E         LD           C,(HL)
61D7: 45         LD           B,L
61D8: 52         LD           D,D
61D9: 21 20 20   LD           HL,$2020
61DC: 59         LD           E,C
61DD: 6F         LD           L,A
61DE: 75         LD           (HL),L
61DF: 20 63      JR           NZ,$6244
61E1: 61         LD           H,C
61E2: 6E         LD           L,(HL)
61E3: 5E         LD           E,(HL)
61E4: 74         LD           (HL),H
61E5: 20 66      JR           NZ,$624D
61E7: 69         LD           L,C
61E8: 6E         LD           L,(HL)
61E9: 64         LD           H,H
61EA: 20 20      JR           NZ,$620C
61EC: 6D         LD           L,L
61ED: 65         LD           H,L
61EE: 21 20 20   LD           HL,$2020
61F1: 4E         LD           C,(HL)
61F2: 59         LD           E,C
61F3: 41         LD           B,C
61F4: 48         LD           C,B
61F5: 20 4E      JR           NZ,$6245
61F7: 59         LD           E,C
61F8: 41         LD           B,C
61F9: 48         LD           C,B
61FA: 21 FF 42   LD           HL,$42FF
61FD: 4C         LD           C,H
61FE: 4F         LD           C,A
61FF: 4F         LD           C,A
6200: 4F         LD           C,A
6201: 50         LD           D,B
6202: 21 20 42   LD           HL,$4220
6205: 4C         LD           C,H
6206: 4F         LD           C,A
6207: 4F         LD           C,A
6208: 4F         LD           C,A
6209: 50         LD           D,B
620A: 21 20 20   LD           HL,$2020
620D: 20 47      JR           NZ,$6256
620F: 4C         LD           C,H
6210: 55         LD           D,L
6211: 42         LD           B,D
6212: 21 20 20   LD           HL,$2020
6215: 47         LD           B,A
6216: 4C         LD           C,H
6217: 55         LD           D,L
6218: 42         LD           B,D
6219: 21 20 20   LD           HL,$2020
621C: 4F         LD           C,A
621D: 47         LD           B,A
621E: 47         LD           B,A
621F: 47         LD           B,A
6220: 48         LD           C,B
6221: 21 20 20   LD           HL,$2020
6224: 46         LD           B,(HL)
6225: 4F         LD           C,A
6226: 4F         LD           C,A
6227: 4F         LD           C,A
6228: 4F         LD           C,A
6229: 44         LD           B,H
622A: 21 20 42   LD           HL,$4220
622D: 4C         LD           C,H
622E: 4F         LD           C,A
622F: 4F         LD           C,A
6230: 4F         LD           C,A
6231: 4F         LD           C,A
6232: 50         LD           D,B
6233: 21 20 20   LD           HL,$2020
6236: 47         LD           B,A
6237: 4C         LD           C,H
6238: 55         LD           D,L
6239: 42         LD           B,D
623A: 21 FF 53   LD           HL,$53FF
623D: 73         LD           (HL),E
623E: 73         LD           (HL),E
623F: 6F         LD           L,A
6240: 2E 2E      LD           L,$2E
6242: 2E 79      LD           L,$79
6244: 6F         LD           L,A
6245: 75         LD           (HL),L
6246: 20 61      JR           NZ,$62A9
6248: 72         LD           (HL),D
6249: 65         LD           H,L
624A: 20 20      JR           NZ,$626C
624C: 74         LD           (HL),H
624D: 68         LD           L,B
624E: 65         LD           H,L
624F: 20 6F      JR           NZ,$62C0
6251: 75         LD           (HL),L
6252: 74         LD           (HL),H
6253: 73         LD           (HL),E
6254: 73         LD           (HL),E
6255: 73         LD           (HL),E
6256: 69         LD           L,C
6257: 64         LD           H,H
6258: 65         LD           H,L
6259: 72         LD           (HL),D
625A: 2C         INC         L
625B: 20 63      JR           NZ,$62C0
625D: 6F         LD           L,A
625E: 6D         LD           L,L
625F: 65         LD           H,L
6260: 20 74      JR           NZ,$62D6
6262: 6F         LD           L,A
6263: 20 77      JR           NZ,$62DC
6265: 61         LD           H,C
6266: 6B         LD           L,E
6267: 65         LD           H,L
6268: 20 74      JR           NZ,$62DE
626A: 68         LD           L,B
626B: 65         LD           H,L
626C: 57         LD           D,A
626D: 69         LD           L,C
626E: 6E         LD           L,(HL)
626F: 64         LD           H,H
6270: 20 46      JR           NZ,$62B8
6272: 69         LD           L,C
6273: 73         LD           (HL),E
6274: 73         LD           (HL),E
6275: 73         LD           (HL),E
6276: 68         LD           L,B
6277: 2E 2E      LD           L,$2E
6279: 2E 20      LD           L,$20
627B: 20 4B      JR           NZ,$62C8
627D: 45         LD           B,L
627E: 45         LD           B,L
627F: 45         LD           B,L
6280: 2D         DEC         L
6281: 48         LD           C,B
6282: 45         LD           B,L
6283: 45         LD           B,L
6284: 2D         DEC         L
6285: 48         LD           C,B
6286: 45         LD           B,L
6287: 45         LD           B,L
6288: 45         LD           B,L
6289: 48         LD           C,B
628A: 21 20 49   LD           HL,$4920
628D: 20 73      JR           NZ,$6302
628F: 68         LD           L,B
6290: 61         LD           H,C
6291: 6C         LD           L,H
6292: 6C         LD           L,H
6293: 20 65      JR           NZ,$62FA
6295: 61         LD           H,C
6296: 74         LD           (HL),H
6297: 20 79      JR           NZ,$6312
6299: 6F         LD           L,A
629A: 75         LD           (HL),L
629B: 21 FF 48   LD           HL,$48FF
629E: 4F         LD           C,A
629F: 20 48      JR           NZ,$62E9
62A1: 4F         LD           C,A
62A2: 20 48      JR           NZ,$62EC
62A4: 4F         LD           C,A
62A5: 21 20 20   LD           HL,$2020
62A8: 20 20      JR           NZ,$62CA
62AA: 20 20      JR           NZ,$62CC
62AC: 20 49      JR           NZ,$62F7
62AE: 5E         LD           E,(HL)
62AF: 6D         LD           L,L
62B0: 20 79      JR           NZ,$632B
62B2: 6F         LD           L,A
62B3: 75         LD           (HL),L
62B4: 72         LD           (HL),D
62B5: 20 62      JR           NZ,$6319
62B7: 61         LD           H,C
62B8: 64         LD           H,H
62B9: 20 67      JR           NZ,$6322
62BB: 75         LD           (HL),L
62BC: 79         LD           A,C
62BD: 74         LD           (HL),H
62BE: 68         LD           L,B
62BF: 69         LD           L,C
62C0: 73         LD           (HL),E
62C1: 20 74      JR           NZ,$6337
62C3: 69         LD           L,C
62C4: 6D         LD           L,L
62C5: 65         LD           H,L
62C6: 21 21 20   LD           HL,$2021
62C9: 20 20      JR           NZ,$62EB
62CB: 20 20      JR           NZ,$62ED
62CD: 48         LD           C,B
62CE: 4F         LD           C,A
62CF: 20 48      JR           NZ,$6319
62D1: 4F         LD           C,A
62D2: 20 48      JR           NZ,$631C
62D4: 4F         LD           C,A
62D5: 21 FF 54   LD           HL,$54FF
62D8: 53         LD           D,E
62D9: 53         LD           D,E
62DA: 53         LD           D,E
62DB: 4B         LD           C,E
62DC: 2C         INC         L
62DD: 20 54      JR           NZ,$6333
62DF: 53         LD           D,E
62E0: 53         LD           D,E
62E1: 53         LD           D,E
62E2: 4B         LD           C,E
62E3: 21 20 20   LD           HL,$2020
62E6: 20 59      JR           NZ,$6341
62E8: 6F         LD           L,A
62E9: 75         LD           (HL),L
62EA: 20 64      JR           NZ,$6350
62EC: 6F         LD           L,A
62ED: 6E         LD           L,(HL)
62EE: 5E         LD           E,(HL)
62EF: 74         LD           (HL),H
62F0: 20 73      JR           NZ,$6365
62F2: 73         LD           (HL),E
62F3: 73         LD           (HL),E
62F4: 65         LD           H,L
62F5: 65         LD           H,L
62F6: 6D         LD           L,L
62F7: 74         LD           (HL),H
62F8: 6F         LD           L,A
62F9: 20 6B      JR           NZ,$6366
62FB: 6E         LD           L,(HL)
62FC: 6F         LD           L,A
62FD: 77         LD           (HL),A
62FE: 20 77      JR           NZ,$6377
6300: 68         LD           L,B
6301: 61         LD           H,C
6302: 74         LD           (HL),H
6303: 20 20      JR           NZ,$6325
6305: 20 20      JR           NZ,$6327
6307: 6B         LD           L,E
6308: 69         LD           L,C
6309: 6E         LD           L,(HL)
630A: 64         LD           H,H
630B: 20 6F      JR           NZ,$637C
630D: 66         LD           H,(HL)
630E: 20 69      JR           NZ,$6379
6310: 73         LD           (HL),E
6311: 6C         LD           L,H
6312: 61         LD           H,C
6313: 6E         LD           L,(HL)
6314: 64         LD           H,H
6315: 20 20      JR           NZ,$6337
6317: 74         LD           (HL),H
6318: 68         LD           L,B
6319: 69         LD           L,C
631A: 73         LD           (HL),E
631B: 73         LD           (HL),E
631C: 73         LD           (HL),E
631D: 20 69      JR           NZ,$6388
631F: 73         LD           (HL),E
6320: 73         LD           (HL),E
6321: 2E 2E      LD           L,$2E
6323: 2E 20      LD           L,$20
6325: 20 20      JR           NZ,$6347
6327: 4B         LD           C,E
6328: 45         LD           B,L
6329: 45         LD           B,L
632A: 45         LD           B,L
632B: 2D         DEC         L
632C: 48         LD           C,B
632D: 45         LD           B,L
632E: 45         LD           B,L
632F: 45         LD           B,L
6330: 2D         DEC         L
6331: 48         LD           C,B
6332: 45         LD           B,L
6333: 45         LD           B,L
6334: 45         LD           B,L
6335: 21 20 57   LD           HL,$5720
6338: 68         LD           L,B
6339: 61         LD           H,C
633A: 74         LD           (HL),H
633B: 20 61      JR           NZ,$639E
633D: 20 66      JR           NZ,$63A5
633F: 6F         LD           L,A
6340: 6F         LD           L,A
6341: 6C         LD           L,H
6342: 2E 2E      LD           L,$2E
6344: 2E 20      LD           L,$20
6346: 20 4B      JR           NZ,$6393
6348: 45         LD           B,L
6349: 45         LD           B,L
634A: 2D         DEC         L
634B: 48         LD           C,B
634C: 45         LD           B,L
634D: 45         LD           B,L
634E: 2D         DEC         L
634F: 48         LD           C,B
6350: 45         LD           B,L
6351: 48         LD           C,B
6352: 21 21 FF   LD           HL,$FF21
6355: 48         LD           C,B
6356: 65         LD           H,L
6357: 79         LD           A,C
6358: 20 64      JR           NZ,$63BE
635A: 75         LD           (HL),L
635B: 6D         LD           L,L
635C: 6D         LD           L,L
635D: 79         LD           A,C
635E: 21 20 4E   LD           HL,$4E20
6361: 65         LD           H,L
6362: 65         LD           H,L
6363: 64         LD           H,H
6364: 20 61      JR           NZ,$63C7
6366: 20 68      JR           NZ,$63D0
6368: 69         LD           L,C
6369: 6E         LD           L,(HL)
636A: 74         LD           (HL),H
636B: 3F         CCF
636C: 20 20      JR           NZ,$638E
636E: 4D         LD           C,L
636F: 79         LD           A,C
6370: 20 77      JR           NZ,$63E9
6372: 65         LD           H,L
6373: 61         LD           H,C
6374: 6B         LD           L,E
6375: 70         LD           (HL),B
6376: 6F         LD           L,A
6377: 69         LD           L,C
6378: 6E         LD           L,(HL)
6379: 74         LD           (HL),H
637A: 20 69      JR           NZ,$63E5
637C: 73         LD           (HL),E
637D: 2E 2E      LD           L,$2E
637F: 2E 20      LD           L,$20
6381: 21 21 20   LD           HL,$2021
6384: 20 57      JR           NZ,$63DD
6386: 68         LD           L,B
6387: 6F         LD           L,A
6388: 6F         LD           L,A
6389: 70         LD           (HL),B
638A: 73         LD           (HL),E
638B: 21 20 20   LD           HL,$2020
638E: 54         LD           D,H
638F: 68         LD           L,B
6390: 65         LD           H,L
6391: 72         LD           (HL),D
6392: 65         LD           H,L
6393: 20 49      JR           NZ,$63DE
6395: 67         LD           H,A
6396: 6F         LD           L,A
6397: 2C         INC         L
6398: 20 74      JR           NZ,$640E
639A: 61         LD           H,C
639B: 6C         LD           L,H
639C: 6B         LD           L,E
639D: 69         LD           L,C
639E: 6E         LD           L,(HL)
639F: 67         LD           H,A
63A0: 20 74      JR           NZ,$6416
63A2: 6F         LD           L,A
63A3: 6F         LD           L,A
63A4: 20 6D      JR           NZ,$6413
63A6: 75         LD           (HL),L
63A7: 63         LD           H,E
63A8: 68         LD           L,B
63A9: 20 61      JR           NZ,$640C
63AB: 67         LD           H,A
63AC: 61         LD           H,C
63AD: 69         LD           L,C
63AE: 6E         LD           L,(HL)
63AF: 2E 2E      LD           L,$2E
63B1: 2E FF      LD           L,$FF
63B3: 4F         LD           C,A
63B4: 6B         LD           L,E
63B5: 61         LD           H,C
63B6: 79         LD           A,C
63B7: 2C         INC         L
63B8: 20 6C      JR           NZ,$6426
63BA: 69         LD           L,C
63BB: 73         LD           (HL),E
63BC: 74         LD           (HL),H
63BD: 65         LD           H,L
63BE: 6E         LD           L,(HL)
63BF: 20 75      JR           NZ,$6436
63C1: 70         LD           (HL),B
63C2: 21 49 66   LD           HL,$6649
63C5: 20 74      JR           NZ,$643B
63C7: 68         LD           L,B
63C8: 65         LD           H,L
63C9: 20 57      JR           NZ,$6422
63CB: 69         LD           L,C
63CC: 6E         LD           L,(HL)
63CD: 64         LD           H,H
63CE: 20 46      JR           NZ,$6416
63D0: 69         LD           L,C
63D1: 73         LD           (HL),E
63D2: 68         LD           L,B
63D3: 77         LD           (HL),A
63D4: 61         LD           H,C
63D5: 6B         LD           L,E
63D6: 65         LD           H,L
63D7: 73         LD           (HL),E
63D8: 20 75      JR           NZ,$644F
63DA: 70         LD           (HL),B
63DB: 2C         INC         L
63DC: 20 65      JR           NZ,$6443
63DE: 76         HALT
63DF: 65         LD           H,L
63E0: 72         LD           (HL),D
63E1: 79         LD           A,C
63E2: 2D         DEC         L
63E3: 74         LD           (HL),H
63E4: 68         LD           L,B
63E5: 69         LD           L,C
63E6: 6E         LD           L,(HL)
63E7: 67         LD           H,A
63E8: 20 6F      JR           NZ,$6459
63EA: 6E         LD           L,(HL)
63EB: 20 74      JR           NZ,$6461
63ED: 68         LD           L,B
63EE: 69         LD           L,C
63EF: 73         LD           (HL),E
63F0: 20 20      JR           NZ,$6412
63F2: 20 69      JR           NZ,$645D
63F4: 73         LD           (HL),E
63F5: 6C         LD           L,H
63F6: 61         LD           H,C
63F7: 6E         LD           L,(HL)
63F8: 64         LD           H,H
63F9: 20 77      JR           NZ,$6472
63FB: 69         LD           L,C
63FC: 6C         LD           L,H
63FD: 6C         LD           L,H
63FE: 20 62      JR           NZ,$6462
6400: 65         LD           H,L
6401: 20 20      JR           NZ,$6423
6403: 67         LD           H,A
6404: 6F         LD           L,A
6405: 6E         LD           L,(HL)
6406: 65         LD           H,L
6407: 20 66      JR           NZ,$646F
6409: 6F         LD           L,A
640A: 72         LD           (HL),D
640B: 65         LD           H,L
640C: 76         HALT
640D: 65         LD           H,L
640E: 72         LD           (HL),D
640F: 21 20 20   LD           HL,$2020
6412: 20 41      JR           NZ,$6455
6414: 6E         LD           L,(HL)
6415: 64         LD           H,H
6416: 20 49      JR           NZ,$6461
6418: 20 64      JR           NZ,$647E
641A: 6F         LD           L,A
641B: 20 6D      JR           NZ,$648A
641D: 65         LD           H,L
641E: 61         LD           H,C
641F: 6E         LD           L,(HL)
6420: 2E 2E      LD           L,$2E
6422: 2E 45      LD           L,$45
6424: 56         LD           D,(HL)
6425: 45         LD           B,L
6426: 52         LD           D,D
6427: 59         LD           E,C
6428: 54         LD           D,H
6429: 48         LD           C,B
642A: 49         LD           C,C
642B: 4E         LD           C,(HL)
642C: 47         LD           B,A
642D: 21 FF 4D   LD           HL,$4DFF
6430: 79         LD           A,C
6431: 20 65      JR           NZ,$6498
6433: 6E         LD           L,(HL)
6434: 65         LD           H,L
6435: 72         LD           (HL),D
6436: 67         LD           H,A
6437: 79         LD           A,C
6438: 2E 2E      LD           L,$2E
643A: 2E 20      LD           L,$20
643C: 20 20      JR           NZ,$645E
643E: 20 67      JR           NZ,$64A7
6440: 6F         LD           L,A
6441: 6E         LD           L,(HL)
6442: 65         LD           H,L
6443: 2E 2E      LD           L,$2E
6445: 2E 49      LD           L,$49
6447: 2E 2E      LD           L,$2E
6449: 2E 6C      LD           L,$6C
644B: 6F         LD           L,A
644C: 73         LD           (HL),E
644D: 74         LD           (HL),H
644E: 21 42 75   LD           HL,$7542
6451: 74         LD           (HL),H
6452: 20 79      JR           NZ,$64CD
6454: 6F         LD           L,A
6455: 75         LD           (HL),L
6456: 20 77      JR           NZ,$64CF
6458: 69         LD           L,C
6459: 6C         LD           L,H
645A: 6C         LD           L,H
645B: 20 62      JR           NZ,$64BF
645D: 65         LD           H,L
645E: 20 6C      JR           NZ,$64CC
6460: 6F         LD           L,A
6461: 73         LD           (HL),E
6462: 74         LD           (HL),H
6463: 20 74      JR           NZ,$64D9
6465: 6F         LD           L,A
6466: 6F         LD           L,A
6467: 2C         INC         L
6468: 20 69      JR           NZ,$64D3
646A: 66         LD           H,(HL)
646B: 20 74      JR           NZ,$64E1
646D: 68         LD           L,B
646E: 65         LD           H,L
646F: 57         LD           D,A
6470: 69         LD           L,C
6471: 6E         LD           L,(HL)
6472: 64         LD           H,H
6473: 20 46      JR           NZ,$64BB
6475: 69         LD           L,C
6476: 73         LD           (HL),E
6477: 68         LD           L,B
6478: 20 77      JR           NZ,$64F1
647A: 61         LD           H,C
647B: 6B         LD           L,E
647C: 65         LD           H,L
647D: 73         LD           (HL),E
647E: 21 53 61   LD           HL,$6153
6481: 6D         LD           L,L
6482: 65         LD           H,L
6483: 20 61      JR           NZ,$64E6
6485: 73         LD           (HL),E
6486: 20 6D      JR           NZ,$64F5
6488: 65         LD           H,L
6489: 2E 2E      LD           L,$2E
648B: 2E 79      LD           L,$79
648D: 6F         LD           L,A
648E: 75         LD           (HL),L
648F: 2E 2E      LD           L,$2E
6491: 2E 61      LD           L,$61
6493: 72         LD           (HL),D
6494: 65         LD           H,L
6495: 2E 2E      LD           L,$2E
6497: 2E 69      LD           L,$69
6499: 6E         LD           L,(HL)
649A: 2E 2E      LD           L,$2E
649C: 2E 20      LD           L,$20
649E: 20 68      JR           NZ,$6508
64A0: 69         LD           L,C
64A1: 73         LD           (HL),E
64A2: 2E 2E      LD           L,$2E
64A4: 2E 64      LD           L,$64
64A6: 72         LD           (HL),D
64A7: 65         LD           H,L
64A8: 61         LD           H,C
64A9: 6D         LD           L,L
64AA: 2E 2E      LD           L,$2E
64AC: 2E FF      LD           L,$FF
64AE: 42         LD           B,D
64AF: 41         LD           B,C
64B0: 48         LD           C,B
64B1: 21 20 20   LD           HL,$2020
64B4: 49         LD           C,C
64B5: 5E         LD           E,(HL)
64B6: 6D         LD           L,L
64B7: 20 6E      JR           NZ,$6527
64B9: 6F         LD           L,A
64BA: 74         LD           (HL),H
64BB: 20 20      JR           NZ,$64DD
64BD: 20 67      JR           NZ,$6526
64BF: 6F         LD           L,A
64C0: 69         LD           L,C
64C1: 6E         LD           L,(HL)
64C2: 67         LD           H,A
64C3: 20 74      JR           NZ,$6539
64C5: 6F         LD           L,A
64C6: 20 68      JR           NZ,$6530
64C8: 6F         LD           L,A
64C9: 6C         LD           L,H
64CA: 64         LD           H,H
64CB: 20 20      JR           NZ,$64ED
64CD: 20 62      JR           NZ,$6531
64CF: 61         LD           H,C
64D0: 63         LD           H,E
64D1: 6B         LD           L,E
64D2: 21 20 20   LD           HL,$2020
64D5: 49         LD           C,C
64D6: 5E         LD           E,(HL)
64D7: 6D         LD           L,L
64D8: 20 67      JR           NZ,$6541
64DA: 6F         LD           L,A
64DB: 69         LD           L,C
64DC: 6E         LD           L,(HL)
64DD: 67         LD           H,A
64DE: 74         LD           (HL),H
64DF: 6F         LD           L,A
64E0: 20 6D      JR           NZ,$654F
64E2: 61         LD           H,C
64E3: 6B         LD           L,E
64E4: 65         LD           H,L
64E5: 20 79      JR           NZ,$6560
64E7: 6F         LD           L,A
64E8: 75         LD           (HL),L
64E9: 20 77      JR           NZ,$6562
64EB: 69         LD           L,C
64EC: 73         LD           (HL),E
64ED: 68         LD           L,B
64EE: 79         LD           A,C
64EF: 6F         LD           L,A
64F0: 75         LD           (HL),L
64F1: 20 77      JR           NZ,$656A
64F3: 65         LD           H,L
64F4: 72         LD           (HL),D
64F5: 65         LD           H,L
64F6: 20 6E      JR           NZ,$6566
64F8: 65         LD           H,L
64F9: 76         HALT
64FA: 65         LD           H,L
64FB: 72         LD           (HL),D
64FC: 20 20      JR           NZ,$651E
64FE: 62         LD           H,D
64FF: 6F         LD           L,A
6500: 72         LD           (HL),D
6501: 6E         LD           L,(HL)
6502: 21 21 FF   LD           HL,$FF21
6505: 43         LD           B,E
6506: 52         LD           D,D
6507: 41         LD           B,C
6508: 43         LD           B,E
6509: 4B         LD           C,E
650A: 4C         LD           C,H
650B: 45         LD           B,L
650C: 2D         DEC         L
650D: 46         LD           B,(HL)
650E: 57         LD           D,A
650F: 4F         LD           C,A
6510: 4F         LD           C,A
6511: 4F         LD           C,A
6512: 53         LD           D,E
6513: 48         LD           C,B
6514: 21 59 6F   LD           HL,$6F59
6517: 75         LD           (HL),L
6518: 5E         LD           E,(HL)
6519: 72         LD           (HL),D
651A: 65         LD           H,L
651B: 20 66      JR           NZ,$6583
651D: 69         LD           L,C
651E: 6E         LD           L,(HL)
651F: 69         LD           L,C
6520: 73         LD           (HL),E
6521: 68         LD           L,B
6522: 65         LD           H,L
6523: 64         LD           H,H
6524: 21 49 20   LD           HL,$2049
6527: 77         LD           (HL),A
6528: 69         LD           L,C
6529: 6C         LD           L,H
652A: 6C         LD           L,H
652B: 20 6E      JR           NZ,$659B
652D: 65         LD           H,L
652E: 76         HALT
652F: 65         LD           H,L
6530: 72         LD           (HL),D
6531: 20 6C      JR           NZ,$659F
6533: 65         LD           H,L
6534: 74         LD           (HL),H
6535: 79         LD           A,C
6536: 6F         LD           L,A
6537: 75         LD           (HL),L
6538: 20 70      JR           NZ,$65AA
653A: 6C         LD           L,H
653B: 61         LD           H,C
653C: 79         LD           A,C
653D: 20 74      JR           NZ,$65B3
653F: 68         LD           L,B
6540: 65         LD           H,L
6541: 20 20      JR           NZ,$6563
6543: 20 20      JR           NZ,$6565
6545: 49         LD           C,C
6546: 6E         LD           L,(HL)
6547: 73         LD           (HL),E
6548: 74         LD           (HL),H
6549: 72         LD           (HL),D
654A: 75         LD           (HL),L
654B: 6D         LD           L,L
654C: 65         LD           H,L
654D: 6E         LD           L,(HL)
654E: 74         LD           (HL),H
654F: 73         LD           (HL),E
6550: 20 6F      JR           NZ,$65C1
6552: 66         LD           H,(HL)
6553: 20 20      JR           NZ,$6575
6555: 74         LD           (HL),H
6556: 68         LD           L,B
6557: 65         LD           H,L
6558: 20 53      JR           NZ,$65AD
655A: 69         LD           L,C
655B: 72         LD           (HL),D
655C: 65         LD           H,L
655D: 6E         LD           L,(HL)
655E: 73         LD           (HL),E
655F: 21 21 FF   LD           HL,$FF21
6562: 43         LD           B,E
6563: 2D         DEC         L
6564: 43         LD           B,E
6565: 2D         DEC         L
6566: 43         LD           B,E
6567: 52         LD           D,D
6568: 41         LD           B,C
6569: 43         LD           B,E
656A: 4B         LD           C,E
656B: 4C         LD           C,H
656C: 45         LD           B,L
656D: 21 20 20   LD           HL,$2020
6570: 20 20      JR           NZ,$6592
6572: 57         LD           D,A
6573: 68         LD           L,B
6574: 79         LD           A,C
6575: 20 64      JR           NZ,$65DB
6577: 69         LD           L,C
6578: 64         LD           H,H
6579: 20 79      JR           NZ,$65F4
657B: 6F         LD           L,A
657C: 75         LD           (HL),L
657D: 20 63      JR           NZ,$65E2
657F: 6F         LD           L,A
6580: 6D         LD           L,L
6581: 65         LD           H,L
6582: 68         LD           L,B
6583: 65         LD           H,L
6584: 72         LD           (HL),D
6585: 65         LD           H,L
6586: 3F         CCF
6587: 20 20      JR           NZ,$65A9
6589: 49         LD           C,C
658A: 66         LD           H,(HL)
658B: 20 69      JR           NZ,$65F6
658D: 74         LD           (HL),H
658E: 20 20      JR           NZ,$65B0
6590: 20 20      JR           NZ,$65B2
6592: 77         LD           (HL),A
6593: 65         LD           H,L
6594: 72         LD           (HL),D
6595: 65         LD           H,L
6596: 6E         LD           L,(HL)
6597: 5E         LD           E,(HL)
6598: 74         LD           (HL),H
6599: 20 66      JR           NZ,$6601
659B: 6F         LD           L,A
659C: 72         LD           (HL),D
659D: 20 79      JR           NZ,$6618
659F: 6F         LD           L,A
65A0: 75         LD           (HL),L
65A1: 2C         INC         L
65A2: 6E         LD           L,(HL)
65A3: 6F         LD           L,A
65A4: 74         LD           (HL),H
65A5: 68         LD           L,B
65A6: 69         LD           L,C
65A7: 6E         LD           L,(HL)
65A8: 67         LD           H,A
65A9: 20 77      JR           NZ,$6622
65AB: 6F         LD           L,A
65AC: 75         LD           (HL),L
65AD: 6C         LD           L,H
65AE: 64         LD           H,H
65AF: 20 20      JR           NZ,$65D1
65B1: 20 68      JR           NZ,$661B
65B3: 61         LD           H,C
65B4: 76         HALT
65B5: 65         LD           H,L
65B6: 20 74      JR           NZ,$662C
65B8: 6F         LD           L,A
65B9: 20 63      JR           NZ,$661E
65BB: 68         LD           L,B
65BC: 61         LD           H,C
65BD: 6E         LD           L,(HL)
65BE: 67         LD           H,A
65BF: 65         LD           H,L
65C0: 21 20 59   LD           HL,$5920
65C3: 6F         LD           L,A
65C4: 75         LD           (HL),L
65C5: 20 63      JR           NZ,$662A
65C7: 61         LD           H,C
65C8: 6E         LD           L,(HL)
65C9: 6E         LD           L,(HL)
65CA: 6F         LD           L,A
65CB: 74         LD           (HL),H
65CC: 20 77      JR           NZ,$6645
65CE: 61         LD           H,C
65CF: 6B         LD           L,E
65D0: 65         LD           H,L
65D1: 20 74      JR           NZ,$6647
65D3: 68         LD           L,B
65D4: 65         LD           H,L
65D5: 20 57      JR           NZ,$662E
65D7: 69         LD           L,C
65D8: 6E         LD           L,(HL)
65D9: 64         LD           H,H
65DA: 20 46      JR           NZ,$6622
65DC: 69         LD           L,C
65DD: 73         LD           (HL),E
65DE: 68         LD           L,B
65DF: 21 20 20   LD           HL,$2020
65E2: 52         LD           D,D
65E3: 65         LD           H,L
65E4: 6D         LD           L,L
65E5: 65         LD           H,L
65E6: 6D         LD           L,L
65E7: 62         LD           H,D
65E8: 65         LD           H,L
65E9: 72         LD           (HL),D
65EA: 2C         INC         L
65EB: 20 79      JR           NZ,$6666
65ED: 6F         LD           L,A
65EE: 75         LD           (HL),L
65EF: 2E 2E      LD           L,$2E
65F1: 2E 74      LD           L,$74
65F3: 6F         LD           L,A
65F4: 6F         LD           L,A
65F5: 2E 2E      LD           L,$2E
65F7: 2E 61      LD           L,$61
65F9: 72         LD           (HL),D
65FA: 65         LD           H,L
65FB: 20 69      JR           NZ,$6666
65FD: 6E         LD           L,(HL)
65FE: 2E 2E      LD           L,$2E
6600: 2E 20      LD           L,$20
6602: 2E 2E      LD           L,$2E
6604: 2E 74      LD           L,$74
6606: 68         LD           L,B
6607: 65         LD           H,L
6608: 20 64      JR           NZ,$666E
660A: 72         LD           (HL),D
660B: 65         LD           H,L
660C: 61         LD           H,C
660D: 6D         LD           L,L
660E: 2E 2E      LD           L,$2E
6610: 2E FF      LD           L,$FF
6612: 48         LD           C,B
6613: 6F         LD           L,A
6614: 6F         LD           L,A
6615: 74         LD           (HL),H
6616: 21 20 20   LD           HL,$2020
6619: 48         LD           C,B
661A: 6F         LD           L,A
661B: 2C         INC         L
661C: 20 62      JR           NZ,$6680
661E: 72         LD           (HL),D
661F: 61         LD           H,C
6620: 76         HALT
6621: 65         LD           H,L
6622: 6C         LD           L,H
6623: 61         LD           H,C
6624: 64         LD           H,H
6625: 2C         INC         L
6626: 20 6F      JR           NZ,$6697
6628: 6E         LD           L,(HL)
6629: 20 79      JR           NZ,$66A4
662B: 6F         LD           L,A
662C: 75         LD           (HL),L
662D: 72         LD           (HL),D
662E: 20 20      JR           NZ,$6650
6630: 20 20      JR           NZ,$6652
6632: 71         LD           (HL),C
6633: 75         LD           (HL),L
6634: 65         LD           H,L
6635: 73         LD           (HL),E
6636: 74         LD           (HL),H
6637: 20 74      JR           NZ,$66AD
6639: 6F         LD           L,A
663A: 20 77      JR           NZ,$66B3
663C: 61         LD           H,C
663D: 6B         LD           L,E
663E: 65         LD           H,L
663F: 20 20      JR           NZ,$6661
6641: 20 74      JR           NZ,$66B7
6643: 68         LD           L,B
6644: 65         LD           H,L
6645: 20 64      JR           NZ,$66AB
6647: 72         LD           (HL),D
6648: 65         LD           H,L
6649: 61         LD           H,C
664A: 6D         LD           L,L
664B: 65         LD           H,L
664C: 72         LD           (HL),D
664D: 21 20 20   LD           HL,$2020
6650: 20 20      JR           NZ,$6672
6652: 57         LD           D,A
6653: 65         LD           H,L
6654: 6C         LD           L,H
6655: 63         LD           H,E
6656: 6F         LD           L,A
6657: 6D         LD           L,L
6658: 65         LD           H,L
6659: 20 74      JR           NZ,$66CF
665B: 6F         LD           L,A
665C: 20 74      JR           NZ,$66D2
665E: 68         LD           L,B
665F: 65         LD           H,L
6660: 20 20      JR           NZ,$6682
6662: 4D         LD           C,L
6663: 79         LD           A,C
6664: 73         LD           (HL),E
6665: 74         LD           (HL),H
6666: 65         LD           H,L
6667: 72         LD           (HL),D
6668: 69         LD           L,C
6669: 6F         LD           L,A
666A: 75         LD           (HL),L
666B: 73         LD           (HL),E
666C: 20 57      JR           NZ,$66C5
666E: 6F         LD           L,A
666F: 6F         LD           L,A
6670: 64         LD           H,H
6671: 21 4D 75   LD           HL,$754D
6674: 63         LD           H,E
6675: 68         LD           L,B
6676: 20 6F      JR           NZ,$66E7
6678: 66         LD           H,(HL)
6679: 20 6D      JR           NZ,$66E8
667B: 79         LD           A,C
667C: 73         LD           (HL),E
667D: 74         LD           (HL),H
667E: 65         LD           H,L
667F: 72         LD           (HL),D
6680: 79         LD           A,C
6681: 20 79      JR           NZ,$66FC
6683: 6F         LD           L,A
6684: 75         LD           (HL),L
6685: 20 77      JR           NZ,$66FE
6687: 69         LD           L,C
6688: 6C         LD           L,H
6689: 6C         LD           L,H
668A: 20 66      JR           NZ,$66F2
668C: 69         LD           L,C
668D: 6E         LD           L,(HL)
668E: 64         LD           H,H
668F: 20 6F      JR           NZ,$6700
6691: 6E         LD           L,(HL)
6692: 74         LD           (HL),H
6693: 68         LD           L,B
6694: 69         LD           L,C
6695: 73         LD           (HL),E
6696: 20 75      JR           NZ,$670D
6698: 6E         LD           L,(HL)
6699: 63         LD           H,E
669A: 68         LD           L,B
669B: 61         LD           H,C
669C: 72         LD           (HL),D
669D: 74         LD           (HL),H
669E: 65         LD           H,L
669F: 64         LD           H,H
66A0: 20 20      JR           NZ,$66C2
66A2: 4B         LD           C,E
66A3: 6F         LD           L,A
66A4: 68         LD           L,B
66A5: 6F         LD           L,A
66A6: 6C         LD           L,H
66A7: 69         LD           L,C
66A8: 6E         LD           L,(HL)
66A9: 74         LD           (HL),H
66AA: 20 69      JR           NZ,$6715
66AC: 73         LD           (HL),E
66AD: 6C         LD           L,H
66AE: 61         LD           H,C
66AF: 6E         LD           L,(HL)
66B0: 64         LD           H,H
66B1: 21 49 5E   LD           HL,$5E49
66B4: 6D         LD           L,L
66B5: 20 61      JR           NZ,$6718
66B7: 66         LD           H,(HL)
66B8: 72         LD           (HL),D
66B9: 61         LD           H,C
66BA: 69         LD           L,C
66BB: 64         LD           H,H
66BC: 20 79      JR           NZ,$6737
66BE: 6F         LD           L,A
66BF: 75         LD           (HL),L
66C0: 20 20      JR           NZ,$66E2
66C2: 6D         LD           L,L
66C3: 61         LD           H,C
66C4: 79         LD           A,C
66C5: 20 66      JR           NZ,$672D
66C7: 69         LD           L,C
66C8: 6E         LD           L,(HL)
66C9: 64         LD           H,H
66CA: 20 69      JR           NZ,$6735
66CC: 74         LD           (HL),H
66CD: 20 61      JR           NZ,$6730
66CF: 20 20      JR           NZ,$66F1
66D1: 20 74      JR           NZ,$6747
66D3: 72         LD           (HL),D
66D4: 69         LD           L,C
66D5: 66         LD           H,(HL)
66D6: 6C         LD           L,H
66D7: 65         LD           H,L
66D8: 20 64      JR           NZ,$673E
66DA: 69         LD           L,C
66DB: 66         LD           H,(HL)
66DC: 66         LD           H,(HL)
66DD: 69         LD           L,C
66DE: 63         LD           H,E
66DF: 75         LD           (HL),L
66E0: 6C         LD           L,H
66E1: 74         LD           (HL),H
66E2: 74         LD           (HL),H
66E3: 6F         LD           L,A
66E4: 20 6C      JR           NZ,$6752
66E6: 65         LD           H,L
66E7: 61         LD           H,C
66E8: 76         HALT
66E9: 65         LD           H,L
66EA: 20 74      JR           NZ,$6760
66EC: 68         LD           L,B
66ED: 65         LD           H,L
66EE: 20 20      JR           NZ,$6710
66F0: 20 20      JR           NZ,$6712
66F2: 69         LD           L,C
66F3: 73         LD           (HL),E
66F4: 6C         LD           L,H
66F5: 61         LD           H,C
66F6: 6E         LD           L,(HL)
66F7: 64         LD           H,H
66F8: 20 77      JR           NZ,$6771
66FA: 68         LD           L,B
66FB: 69         LD           L,C
66FC: 6C         LD           L,H
66FD: 65         LD           H,L
66FE: 20 74      JR           NZ,$6774
6700: 68         LD           L,B
6701: 65         LD           H,L
6702: 57         LD           D,A
6703: 69         LD           L,C
6704: 6E         LD           L,(HL)
6705: 64         LD           H,H
6706: 20 46      JR           NZ,$674E
6708: 69         LD           L,C
6709: 73         LD           (HL),E
670A: 68         LD           L,B
670B: 20 6E      JR           NZ,$677B
670D: 61         LD           H,C
670E: 70         LD           (HL),B
670F: 73         LD           (HL),E
6710: 2E 20      LD           L,$20
6712: 2E 2E      LD           L,$2E
6714: 2E 42      LD           L,$42
6716: 79         LD           A,C
6717: 20 74      JR           NZ,$678D
6719: 68         LD           L,B
671A: 65         LD           H,L
671B: 20 62      JR           NZ,$677F
671D: 79         LD           A,C
671E: 2C         INC         L
671F: 20 20      JR           NZ,$6741
6721: 20 68      JR           NZ,$678B
6723: 61         LD           H,C
6724: 76         HALT
6725: 65         LD           H,L
6726: 20 79      JR           NZ,$67A1
6728: 6F         LD           L,A
6729: 75         LD           (HL),L
672A: 20 65      JR           NZ,$6791
672C: 76         HALT
672D: 65         LD           H,L
672E: 72         LD           (HL),D
672F: 20 20      JR           NZ,$6751
6731: 20 76      JR           NZ,$67A9
6733: 69         LD           L,C
6734: 73         LD           (HL),E
6735: 69         LD           L,C
6736: 74         LD           (HL),H
6737: 65         LD           H,L
6738: 64         LD           H,H
6739: 20 74      JR           NZ,$67AF
673B: 68         LD           L,B
673C: 65         LD           H,L
673D: 20 54      JR           NZ,$6793
673F: 61         LD           H,C
6740: 69         LD           L,C
6741: 6C         LD           L,H
6742: 43         LD           B,E
6743: 61         LD           H,C
6744: 76         HALT
6745: 65         LD           H,L
6746: 2C         INC         L
6747: 20 77      JR           NZ,$67C0
6749: 68         LD           L,B
674A: 69         LD           L,C
674B: 63         LD           H,E
674C: 68         LD           L,B
674D: 20 69      JR           NZ,$67B8
674F: 73         LD           (HL),E
6750: 20 20      JR           NZ,$6772
6752: 73         LD           (HL),E
6753: 6F         LD           L,A
6754: 75         LD           (HL),L
6755: 74         LD           (HL),H
6756: 68         LD           L,B
6757: 20 6F      JR           NZ,$67C8
6759: 66         LD           H,(HL)
675A: 20 74      JR           NZ,$67D0
675C: 68         LD           L,B
675D: 65         LD           H,L
675E: 20 20      JR           NZ,$6780
6760: 20 20      JR           NZ,$6782
6762: 76         HALT
6763: 69         LD           L,C
6764: 6C         LD           L,H
6765: 6C         LD           L,H
6766: 61         LD           H,C
6767: 67         LD           H,A
6768: 65         LD           H,L
6769: 3F         CCF
676A: 20 20      JR           NZ,$678C
676C: 47         LD           B,A
676D: 6F         LD           L,A
676E: 20 20      JR           NZ,$6790
6770: 20 20      JR           NZ,$6792
6772: 74         LD           (HL),H
6773: 68         LD           L,B
6774: 65         LD           H,L
6775: 72         LD           (HL),D
6776: 65         LD           H,L
6777: 20 77      JR           NZ,$67F0
6779: 69         LD           L,C
677A: 74         LD           (HL),H
677B: 68         LD           L,B
677C: 20 74      JR           NZ,$67F2
677E: 68         LD           L,B
677F: 65         LD           H,L
6780: 20 20      JR           NZ,$67A2
6782: 6B         LD           L,E
6783: 65         LD           H,L
6784: 79         LD           A,C
6785: 20 79      JR           NZ,$6800
6787: 6F         LD           L,A
6788: 75         LD           (HL),L
6789: 20 66      JR           NZ,$67F1
678B: 69         LD           L,C
678C: 6E         LD           L,(HL)
678D: 64         LD           H,H
678E: 20 69      JR           NZ,$67F9
6790: 6E         LD           L,(HL)
6791: 20 74      JR           NZ,$6807
6793: 68         LD           L,B
6794: 69         LD           L,C
6795: 73         LD           (HL),E
6796: 20 66      JR           NZ,$67FE
6798: 6F         LD           L,A
6799: 72         LD           (HL),D
679A: 65         LD           H,L
679B: 73         LD           (HL),E
679C: 74         LD           (HL),H
679D: 2E 2E      LD           L,$2E
679F: 2E 20      LD           L,$20
67A1: 20 54      JR           NZ,$67F7
67A3: 68         LD           L,B
67A4: 65         LD           H,L
67A5: 20 57      JR           NZ,$67FE
67A7: 69         LD           L,C
67A8: 6E         LD           L,(HL)
67A9: 64         LD           H,H
67AA: 20 46      JR           NZ,$67F2
67AC: 69         LD           L,C
67AD: 73         LD           (HL),E
67AE: 68         LD           L,B
67AF: 20 69      JR           NZ,$681A
67B1: 73         LD           (HL),E
67B2: 77         LD           (HL),A
67B3: 61         LD           H,C
67B4: 74         LD           (HL),H
67B5: 63         LD           H,E
67B6: 68         LD           L,B
67B7: 69         LD           L,C
67B8: 6E         LD           L,(HL)
67B9: 67         LD           H,A
67BA: 2E 2E      LD           L,$2E
67BC: 2E 48      LD           L,$48
67BE: 6F         LD           L,A
67BF: 6F         LD           L,A
67C0: 74         LD           (HL),H
67C1: 21 FF 48   LD           HL,$48FF
67C4: 6F         LD           L,A
67C5: 6F         LD           L,A
67C6: 74         LD           (HL),H
67C7: 21 20 20   LD           HL,$2020
67CA: 54         LD           D,H
67CB: 61         LD           H,C
67CC: 6B         LD           L,E
67CD: 65         LD           H,L
67CE: 20 74      JR           NZ,$6844
67D0: 68         LD           L,B
67D1: 65         LD           H,L
67D2: 20 6B      JR           NZ,$683F
67D4: 65         LD           H,L
67D5: 79         LD           A,C
67D6: 20 61      JR           NZ,$6839
67D8: 6E         LD           L,(HL)
67D9: 64         LD           H,H
67DA: 20 67      JR           NZ,$6843
67DC: 6F         LD           L,A
67DD: 20 74      JR           NZ,$6853
67DF: 6F         LD           L,A
67E0: 20 20      JR           NZ,$6802
67E2: 20 74      JR           NZ,$6858
67E4: 68         LD           L,B
67E5: 65         LD           H,L
67E6: 20 54      JR           NZ,$683C
67E8: 61         LD           H,C
67E9: 69         LD           L,C
67EA: 6C         LD           L,H
67EB: 20 43      JR           NZ,$6830
67ED: 61         LD           H,C
67EE: 76         HALT
67EF: 65         LD           H,L
67F0: 2E 20      LD           L,$20
67F2: 20 52      JR           NZ,$6846
67F4: 65         LD           H,L
67F5: 74         LD           (HL),H
67F6: 72         LD           (HL),D
67F7: 69         LD           L,C
67F8: 65         LD           H,L
67F9: 76         HALT
67FA: 65         LD           H,L
67FB: 20 74      JR           NZ,$6871
67FD: 68         LD           L,B
67FE: 65         LD           H,L
67FF: 20 20      JR           NZ,$6821
6801: 20 20      JR           NZ,$6823
6803: 49         LD           C,C
6804: 6E         LD           L,(HL)
6805: 73         LD           (HL),E
6806: 74         LD           (HL),H
6807: 72         LD           (HL),D
6808: 75         LD           (HL),L
6809: 6D         LD           L,L
680A: 65         LD           H,L
680B: 6E         LD           L,(HL)
680C: 74         LD           (HL),H
680D: 20 74      JR           NZ,$6883
680F: 68         LD           L,B
6810: 61         LD           H,C
6811: 74         LD           (HL),H
6812: 20 69      JR           NZ,$687D
6814: 73         LD           (HL),E
6815: 20 68      JR           NZ,$687F
6817: 69         LD           L,C
6818: 64         LD           H,H
6819: 64         LD           H,H
681A: 65         LD           H,L
681B: 6E         LD           L,(HL)
681C: 20 74      JR           NZ,$6892
681E: 68         LD           L,B
681F: 65         LD           H,L
6820: 72         LD           (HL),D
6821: 65         LD           H,L
6822: 21 47 6F   LD           HL,$6F47
6825: 20 6E      JR           NZ,$6895
6827: 6F         LD           L,A
6828: 77         LD           (HL),A
6829: 21 20 20   LD           HL,$2020
682C: 54         LD           D,H
682D: 68         LD           L,B
682E: 65         LD           H,L
682F: 20 20      JR           NZ,$6851
6831: 20 20      JR           NZ,$6853
6833: 57         LD           D,A
6834: 69         LD           L,C
6835: 6E         LD           L,(HL)
6836: 64         LD           H,H
6837: 20 46      JR           NZ,$687F
6839: 69         LD           L,C
683A: 73         LD           (HL),E
683B: 68         LD           L,B
683C: 20 69      JR           NZ,$68A7
683E: 73         LD           (HL),E
683F: 20 20      JR           NZ,$6861
6841: 20 20      JR           NZ,$6863
6843: 77         LD           (HL),A
6844: 61         LD           H,C
6845: 69         LD           L,C
6846: 74         LD           (HL),H
6847: 69         LD           L,C
6848: 6E         LD           L,(HL)
6849: 67         LD           H,A
684A: 21 20 20   LD           HL,$2020
684D: 48         LD           C,B
684E: 6F         LD           L,A
684F: 6F         LD           L,A
6850: 6F         LD           L,A
6851: 74         LD           (HL),H
6852: 21 FF 48   LD           HL,$48FF
6855: 6F         LD           L,A
6856: 6F         LD           L,A
6857: 6F         LD           L,A
6858: 6F         LD           L,A
6859: 74         LD           (HL),H
685A: 21 20 20   LD           HL,$2020
685D: 54         LD           D,H
685E: 68         LD           L,B
685F: 61         LD           H,C
6860: 74         LD           (HL),H
6861: 20 69      JR           NZ,$68CC
6863: 73         LD           (HL),E
6864: 61         LD           H,C
6865: 6E         LD           L,(HL)
6866: 20 5E      JR           NZ,$68C6
6868: 49         LD           C,C
6869: 6E         LD           L,(HL)
686A: 73         LD           (HL),E
686B: 74         LD           (HL),H
686C: 72         LD           (HL),D
686D: 75         LD           (HL),L
686E: 6D         LD           L,L
686F: 65         LD           H,L
6870: 6E         LD           L,(HL)
6871: 74         LD           (HL),H
6872: 20 20      JR           NZ,$6894
6874: 6F         LD           L,A
6875: 66         LD           H,(HL)
6876: 20 74      JR           NZ,$68EC
6878: 68         LD           L,B
6879: 65         LD           H,L
687A: 20 53      JR           NZ,$68CF
687C: 69         LD           L,C
687D: 72         LD           (HL),D
687E: 65         LD           H,L
687F: 6E         LD           L,(HL)
6880: 73         LD           (HL),E
6881: 21 5E 20   LD           HL,$205E
6884: 49         LD           C,C
6885: 20 68      JR           NZ,$68EF
6887: 61         LD           H,C
6888: 76         HALT
6889: 65         LD           H,L
688A: 20 74      JR           NZ,$6900
688C: 6F         LD           L,A
688D: 20 61      JR           NZ,$68F0
688F: 64         LD           H,H
6890: 6D         LD           L,L
6891: 69         LD           L,C
6892: 74         LD           (HL),H
6893: 2C         INC         L
6894: 61         LD           H,C
6895: 74         LD           (HL),H
6896: 20 66      JR           NZ,$68FE
6898: 69         LD           L,C
6899: 72         LD           (HL),D
689A: 73         LD           (HL),E
689B: 74         LD           (HL),H
689C: 20 49      JR           NZ,$68E7
689E: 20 64      JR           NZ,$6904
68A0: 69         LD           L,C
68A1: 64         LD           H,H
68A2: 20 20      JR           NZ,$68C4
68A4: 6E         LD           L,(HL)
68A5: 6F         LD           L,A
68A6: 74         LD           (HL),H
68A7: 20 62      JR           NZ,$690B
68A9: 65         LD           H,L
68AA: 6C         LD           L,H
68AB: 69         LD           L,C
68AC: 65         LD           H,L
68AD: 76         HALT
68AE: 65         LD           H,L
68AF: 20 79      JR           NZ,$692A
68B1: 6F         LD           L,A
68B2: 75         LD           (HL),L
68B3: 20 77      JR           NZ,$692C
68B5: 65         LD           H,L
68B6: 72         LD           (HL),D
68B7: 65         LD           H,L
68B8: 20 72      JR           NZ,$692C
68BA: 65         LD           H,L
68BB: 61         LD           H,C
68BC: 6C         LD           L,H
68BD: 2E 2E      LD           L,$2E
68BF: 2E 20      LD           L,$20
68C1: 20 20      JR           NZ,$68E3
68C3: 20 54      JR           NZ,$6919
68C5: 68         LD           L,B
68C6: 61         LD           H,C
68C7: 74         LD           (HL),H
68C8: 20 49      JR           NZ,$6913
68CA: 6E         LD           L,(HL)
68CB: 73         LD           (HL),E
68CC: 74         LD           (HL),H
68CD: 72         LD           (HL),D
68CE: 75         LD           (HL),L
68CF: 6D         LD           L,L
68D0: 65         LD           H,L
68D1: 6E         LD           L,(HL)
68D2: 74         LD           (HL),H
68D3: 2C         INC         L
68D4: 61         LD           H,C
68D5: 6C         LD           L,H
68D6: 6F         LD           L,A
68D7: 6E         LD           L,(HL)
68D8: 67         LD           H,A
68D9: 20 77      JR           NZ,$6952
68DB: 69         LD           L,C
68DC: 74         LD           (HL),H
68DD: 68         LD           L,B
68DE: 20 74      JR           NZ,$6954
68E0: 68         LD           L,B
68E1: 65         LD           H,L
68E2: 20 20      JR           NZ,$6904
68E4: 73         LD           (HL),E
68E5: 65         LD           H,L
68E6: 76         HALT
68E7: 65         LD           H,L
68E8: 6E         LD           L,(HL)
68E9: 20 6F      JR           NZ,$695A
68EB: 74         LD           (HL),H
68EC: 68         LD           L,B
68ED: 65         LD           H,L
68EE: 72         LD           (HL),D
68EF: 73         LD           (HL),E
68F0: 20 69      JR           NZ,$695B
68F2: 6E         LD           L,(HL)
68F3: 20 74      JR           NZ,$6969
68F5: 68         LD           L,B
68F6: 65         LD           H,L
68F7: 20 73      JR           NZ,$696C
68F9: 65         LD           H,L
68FA: 74         LD           (HL),H
68FB: 2C         INC         L
68FC: 20 68      JR           NZ,$6966
68FE: 61         LD           H,C
68FF: 73         LD           (HL),E
6900: 20 74      JR           NZ,$6976
6902: 68         LD           L,B
6903: 65         LD           H,L
6904: 70         LD           (HL),B
6905: 6F         LD           L,A
6906: 77         LD           (HL),A
6907: 65         LD           H,L
6908: 72         LD           (HL),D
6909: 20 74      JR           NZ,$697F
690B: 6F         LD           L,A
690C: 20 77      JR           NZ,$6985
690E: 61         LD           H,C
690F: 6B         LD           L,E
6910: 65         LD           H,L
6911: 20 20      JR           NZ,$6933
6913: 20 74      JR           NZ,$6989
6915: 68         LD           L,B
6916: 65         LD           H,L
6917: 20 57      JR           NZ,$6970
6919: 69         LD           L,C
691A: 6E         LD           L,(HL)
691B: 64         LD           H,H
691C: 20 46      JR           NZ,$6964
691E: 69         LD           L,C
691F: 73         LD           (HL),E
6920: 68         LD           L,B
6921: 21 20 20   LD           HL,$2020
6924: 59         LD           E,C
6925: 6F         LD           L,A
6926: 75         LD           (HL),L
6927: 20 6D      JR           NZ,$6996
6929: 75         LD           (HL),L
692A: 73         LD           (HL),E
692B: 74         LD           (HL),H
692C: 20 63      JR           NZ,$6991
692E: 6F         LD           L,A
692F: 6C         LD           L,H
6930: 6C         LD           L,H
6931: 65         LD           H,L
6932: 63         LD           H,E
6933: 74         LD           (HL),H
6934: 74         LD           (HL),H
6935: 68         LD           L,B
6936: 65         LD           H,L
6937: 6D         LD           L,L
6938: 20 61      JR           NZ,$699B
693A: 6C         LD           L,H
693B: 6C         LD           L,H
693C: 21 20 20   LD           HL,$2020
693F: 49         LD           C,C
6940: 20 77      JR           NZ,$69B9
6942: 61         LD           H,C
6943: 73         LD           (HL),E
6944: 69         LD           L,C
6945: 6E         LD           L,(HL)
6946: 73         LD           (HL),E
6947: 74         LD           (HL),H
6948: 72         LD           (HL),D
6949: 75         LD           (HL),L
694A: 63         LD           H,E
694B: 74         LD           (HL),H
694C: 65         LD           H,L
694D: 64         LD           H,H
694E: 20 74      JR           NZ,$69C4
6950: 6F         LD           L,A
6951: 20 20      JR           NZ,$6973
6953: 20 67      JR           NZ,$69BC
6955: 69         LD           L,C
6956: 76         HALT
6957: 65         LD           H,L
6958: 20 79      JR           NZ,$69D3
695A: 6F         LD           L,A
695B: 75         LD           (HL),L
695C: 20 64      JR           NZ,$69C2
695E: 69         LD           L,C
695F: 72         LD           (HL),D
6960: 65         LD           H,L
6961: 63         LD           H,E
6962: 2D         DEC         L
6963: 20 74      JR           NZ,$69D9
6965: 69         LD           L,C
6966: 6F         LD           L,A
6967: 6E         LD           L,(HL)
6968: 73         LD           (HL),E
6969: 2E 2E      LD           L,$2E
696B: 2E 20      LD           L,$20
696D: 20 59      JR           NZ,$69C8
696F: 6F         LD           L,A
6970: 75         LD           (HL),L
6971: 72         LD           (HL),D
6972: 20 20      JR           NZ,$6994
6974: 6E         LD           L,(HL)
6975: 65         LD           H,L
6976: 78         LD           A,B
6977: 74         LD           (HL),H
6978: 20 67      JR           NZ,$69E1
697A: 6F         LD           L,A
697B: 61         LD           H,C
697C: 6C         LD           L,H
697D: 20 69      JR           NZ,$69E8
697F: 73         LD           (HL),E
6980: 20 20      JR           NZ,$69A2
6982: 20 20      JR           NZ,$69A4
6984: 6E         LD           L,(HL)
6985: 6F         LD           L,A
6986: 72         LD           (HL),D
6987: 74         LD           (HL),H
6988: 68         LD           L,B
6989: 2C         INC         L
698A: 20 69      JR           NZ,$69F5
698C: 6E         LD           L,(HL)
698D: 20 20      JR           NZ,$69AF
698F: 20 20      JR           NZ,$69B1
6991: 20 20      JR           NZ,$69B3
6993: 20 47      JR           NZ,$69DC
6995: 6F         LD           L,A
6996: 70         LD           (HL),B
6997: 6F         LD           L,A
6998: 6E         LD           L,(HL)
6999: 67         LD           H,A
699A: 61         LD           H,C
699B: 20 53      JR           NZ,$69F0
699D: 77         LD           (HL),A
699E: 61         LD           H,C
699F: 6D         LD           L,L
69A0: 70         LD           (HL),B
69A1: 21 21 20   LD           HL,$2021
69A4: 48         LD           C,B
69A5: 6F         LD           L,A
69A6: 6F         LD           L,A
69A7: 74         LD           (HL),H
69A8: 2C         INC         L
69A9: 20 69      JR           NZ,$6A14
69AB: 6E         LD           L,(HL)
69AC: 64         LD           H,H
69AD: 65         LD           H,L
69AE: 65         LD           H,L
69AF: 64         LD           H,H
69B0: 21 FF 48   LD           HL,$48FF
69B3: 6F         LD           L,A
69B4: 6F         LD           L,A
69B5: 74         LD           (HL),H
69B6: 21 20 20   LD           HL,$2020
69B9: 54         LD           D,H
69BA: 68         LD           L,B
69BB: 61         LD           H,C
69BC: 74         LD           (HL),H
69BD: 20 69      JR           NZ,$6A28
69BF: 73         LD           (HL),E
69C0: 20 61      JR           NZ,$6A23
69C2: 66         LD           H,(HL)
69C3: 65         LD           H,L
69C4: 61         LD           H,C
69C5: 72         LD           (HL),D
69C6: 73         LD           (HL),E
69C7: 6F         LD           L,A
69C8: 6D         LD           L,L
69C9: 65         LD           H,L
69CA: 20 6C      JR           NZ,$6A38
69CC: 6F         LD           L,A
69CD: 6F         LD           L,A
69CE: 6B         LD           L,E
69CF: 69         LD           L,C
69D0: 6E         LD           L,(HL)
69D1: 67         LD           H,A
69D2: 61         LD           H,C
69D3: 6E         LD           L,(HL)
69D4: 69         LD           L,C
69D5: 6D         LD           L,L
69D6: 61         LD           H,C
69D7: 6C         LD           L,H
69D8: 20 79      JR           NZ,$6A53
69DA: 6F         LD           L,A
69DB: 75         LD           (HL),L
69DC: 20 68      JR           NZ,$6A46
69DE: 61         LD           H,C
69DF: 76         HALT
69E0: 65         LD           H,L
69E1: 20 74      JR           NZ,$6A57
69E3: 68         LD           L,B
69E4: 65         LD           H,L
69E5: 72         LD           (HL),D
69E6: 65         LD           H,L
69E7: 21 20 20   LD           HL,$2020
69EA: 44         LD           B,H
69EB: 6F         LD           L,A
69EC: 20 6E      JR           NZ,$6A5C
69EE: 6F         LD           L,A
69EF: 74         LD           (HL),H
69F0: 20 20      JR           NZ,$6A12
69F2: 66         LD           H,(HL)
69F3: 6F         LD           L,A
69F4: 72         LD           (HL),D
69F5: 67         LD           H,A
69F6: 65         LD           H,L
69F7: 74         LD           (HL),H
69F8: 2C         INC         L
69F9: 20 74      JR           NZ,$6A6F
69FB: 68         LD           L,B
69FC: 65         LD           H,L
69FD: 20 6E      JR           NZ,$6A6D
69FF: 65         LD           H,L
6A00: 78         LD           A,B
6A01: 74         LD           (HL),H
6A02: 49         LD           C,C
6A03: 6E         LD           L,(HL)
6A04: 73         LD           (HL),E
6A05: 74         LD           (HL),H
6A06: 72         LD           (HL),D
6A07: 75         LD           (HL),L
6A08: 6D         LD           L,L
6A09: 65         LD           H,L
6A0A: 6E         LD           L,(HL)
6A0B: 74         LD           (HL),H
6A0C: 20 69      JR           NZ,$6A77
6A0E: 73         LD           (HL),E
6A0F: 20 69      JR           NZ,$6A7A
6A11: 6E         LD           L,(HL)
6A12: 47         LD           B,A
6A13: 6F         LD           L,A
6A14: 70         LD           (HL),B
6A15: 6F         LD           L,A
6A16: 6E         LD           L,(HL)
6A17: 67         LD           H,A
6A18: 61         LD           H,C
6A19: 20 53      JR           NZ,$6A6E
6A1B: 77         LD           (HL),A
6A1C: 61         LD           H,C
6A1D: 6D         LD           L,L
6A1E: 70         LD           (HL),B
6A1F: 21 FF 48   LD           HL,$48FF
6A22: 6F         LD           L,A
6A23: 6F         LD           L,A
6A24: 6F         LD           L,A
6A25: 6F         LD           L,A
6A26: 74         LD           (HL),H
6A27: 21 20 54   LD           HL,$5420
6A2A: 68         LD           L,B
6A2B: 65         LD           H,L
6A2C: 20 57      JR           NZ,$6A85
6A2E: 69         LD           L,C
6A2F: 6E         LD           L,(HL)
6A30: 64         LD           H,H
6A31: 46         LD           B,(HL)
6A32: 69         LD           L,C
6A33: 73         LD           (HL),E
6A34: 68         LD           L,B
6A35: 20 73      JR           NZ,$6AAA
6A37: 6C         LD           L,H
6A38: 65         LD           H,L
6A39: 65         LD           H,L
6A3A: 70         LD           (HL),B
6A3B: 73         LD           (HL),E
6A3C: 20 6C      JR           NZ,$6AAA
6A3E: 6F         LD           L,A
6A3F: 6E         LD           L,(HL)
6A40: 67         LD           H,A
6A41: 61         LD           H,C
6A42: 6E         LD           L,(HL)
6A43: 64         LD           H,H
6A44: 20 64      JR           NZ,$6AAA
6A46: 72         LD           (HL),D
6A47: 65         LD           H,L
6A48: 61         LD           H,C
6A49: 6D         LD           L,L
6A4A: 69         LD           L,C
6A4B: 6C         LD           L,H
6A4C: 79         LD           A,C
6A4D: 20 69      JR           NZ,$6AB8
6A4F: 6E         LD           L,(HL)
6A50: 20 74      JR           NZ,$6AC6
6A52: 68         LD           L,B
6A53: 65         LD           H,L
6A54: 20 45      JR           NZ,$6A9B
6A56: 67         LD           H,A
6A57: 67         LD           H,A
6A58: 20 61      JR           NZ,$6ABB
6A5A: 62         LD           H,D
6A5B: 6F         LD           L,A
6A5C: 76         HALT
6A5D: 65         LD           H,L
6A5E: 2E 2E      LD           L,$2E
6A60: 2E 57      LD           L,$57
6A62: 68         LD           L,B
6A63: 65         LD           H,L
6A64: 6E         LD           L,(HL)
6A65: 20 79      JR           NZ,$6AE0
6A67: 6F         LD           L,A
6A68: 75         LD           (HL),L
6A69: 20 70      JR           NZ,$6ADB
6A6B: 6C         LD           L,H
6A6C: 61         LD           H,C
6A6D: 79         LD           A,C
6A6E: 20 20      JR           NZ,$6A90
6A70: 20 74      JR           NZ,$6AE6
6A72: 68         LD           L,B
6A73: 65         LD           H,L
6A74: 20 65      JR           NZ,$6ADB
6A76: 69         LD           L,C
6A77: 67         LD           H,A
6A78: 68         LD           L,B
6A79: 74         LD           (HL),H
6A7A: 20 53      JR           NZ,$6ACF
6A7C: 69         LD           L,C
6A7D: 72         LD           (HL),D
6A7E: 65         LD           H,L
6A7F: 6E         LD           L,(HL)
6A80: 20 49      JR           NZ,$6ACB
6A82: 6E         LD           L,(HL)
6A83: 73         LD           (HL),E
6A84: 74         LD           (HL),H
6A85: 72         LD           (HL),D
6A86: 75         LD           (HL),L
6A87: 6D         LD           L,L
6A88: 65         LD           H,L
6A89: 6E         LD           L,(HL)
6A8A: 74         LD           (HL),H
6A8B: 73         LD           (HL),E
6A8C: 20 69      JR           NZ,$6AF7
6A8E: 6E         LD           L,(HL)
6A8F: 20 20      JR           NZ,$6AB1
6A91: 66         LD           H,(HL)
6A92: 72         LD           (HL),D
6A93: 6F         LD           L,A
6A94: 6E         LD           L,(HL)
6A95: 74         LD           (HL),H
6A96: 20 6F      JR           NZ,$6B07
6A98: 66         LD           H,(HL)
6A99: 20 74      JR           NZ,$6B0F
6A9B: 68         LD           L,B
6A9C: 65         LD           H,L
6A9D: 20 45      JR           NZ,$6AE4
6A9F: 67         LD           H,A
6AA0: 67         LD           H,A
6AA1: 68         LD           L,B
6AA2: 65         LD           H,L
6AA3: 20 77      JR           NZ,$6B1C
6AA5: 69         LD           L,C
6AA6: 6C         LD           L,H
6AA7: 6C         LD           L,H
6AA8: 20 61      JR           NZ,$6B0B
6AAA: 77         LD           (HL),A
6AAB: 61         LD           H,C
6AAC: 6B         LD           L,E
6AAD: 65         LD           H,L
6AAE: 6E         LD           L,(HL)
6AAF: 2E 20      LD           L,$20
6AB1: 54         LD           D,H
6AB2: 68         LD           L,B
6AB3: 69         LD           L,C
6AB4: 73         LD           (HL),E
6AB5: 2C         INC         L
6AB6: 20 6D      JR           NZ,$6B25
6AB8: 79         LD           A,C
6AB9: 20 66      JR           NZ,$6B21
6ABB: 72         LD           (HL),D
6ABC: 69         LD           L,C
6ABD: 65         LD           H,L
6ABE: 6E         LD           L,(HL)
6ABF: 64         LD           H,H
6AC0: 2C         INC         L
6AC1: 69         LD           L,C
6AC2: 73         LD           (HL),E
6AC3: 20 74      JR           NZ,$6B39
6AC5: 68         LD           L,B
6AC6: 65         LD           H,L
6AC7: 20 6F      JR           NZ,$6B38
6AC9: 6E         LD           L,(HL)
6ACA: 6C         LD           L,H
6ACB: 79         LD           A,C
6ACC: 20 77      JR           NZ,$6B45
6ACE: 61         LD           H,C
6ACF: 79         LD           A,C
6AD0: 20 66      JR           NZ,$6B38
6AD2: 6F         LD           L,A
6AD3: 72         LD           (HL),D
6AD4: 20 79      JR           NZ,$6B4F
6AD6: 6F         LD           L,A
6AD7: 75         LD           (HL),L
6AD8: 20 74      JR           NZ,$6B4E
6ADA: 6F         LD           L,A
6ADB: 20 6C      JR           NZ,$6B49
6ADD: 65         LD           H,L
6ADE: 61         LD           H,C
6ADF: 76         HALT
6AE0: 65         LD           H,L
6AE1: 74         LD           (HL),H
6AE2: 68         LD           L,B
6AE3: 65         LD           H,L
6AE4: 20 69      JR           NZ,$6B4F
6AE6: 73         LD           (HL),E
6AE7: 6C         LD           L,H
6AE8: 61         LD           H,C
6AE9: 6E         LD           L,(HL)
6AEA: 64         LD           H,H
6AEB: 21 20 48   LD           HL,$4820
6AEE: 6F         LD           L,A
6AEF: 6F         LD           L,A
6AF0: 21 FF 48   LD           HL,$48FF
6AF3: 6F         LD           L,A
6AF4: 6F         LD           L,A
6AF5: 74         LD           (HL),H
6AF6: 21 20 20   LD           HL,$2020
6AF9: 48         LD           C,B
6AFA: 6F         LD           L,A
6AFB: 77         LD           (HL),A
6AFC: 20 6D      JR           NZ,$6B6B
6AFE: 61         LD           H,C
6AFF: 6E         LD           L,(HL)
6B00: 79         LD           A,C
6B01: 20 49      JR           NZ,$6B4C
6B03: 6E         LD           L,(HL)
6B04: 73         LD           (HL),E
6B05: 74         LD           (HL),H
6B06: 72         LD           (HL),D
6B07: 75         LD           (HL),L
6B08: 6D         LD           L,L
6B09: 65         LD           H,L
6B0A: 6E         LD           L,(HL)
6B0B: 74         LD           (HL),H
6B0C: 73         LD           (HL),E
6B0D: 20 20      JR           NZ,$6B2F
6B0F: 20 20      JR           NZ,$6B31
6B11: 20 68      JR           NZ,$6B7B
6B13: 61         LD           H,C
6B14: 76         HALT
6B15: 65         LD           H,L
6B16: 20 79      JR           NZ,$6B91
6B18: 6F         LD           L,A
6B19: 75         LD           (HL),L
6B1A: 20 67      JR           NZ,$6B83
6B1C: 6F         LD           L,A
6B1D: 74         LD           (HL),H
6B1E: 74         LD           (HL),H
6B1F: 65         LD           H,L
6B20: 6E         LD           L,(HL)
6B21: 20 73      JR           NZ,$6B96
6B23: 6F         LD           L,A
6B24: 20 66      JR           NZ,$6B8C
6B26: 61         LD           H,C
6B27: 72         LD           (HL),D
6B28: 3F         CCF
6B29: 20 20      JR           NZ,$6B4B
6B2B: 57         LD           D,A
6B2C: 68         LD           L,B
6B2D: 65         LD           H,L
6B2E: 6E         LD           L,(HL)
6B2F: 20 20      JR           NZ,$6B51
6B31: 20 79      JR           NZ,$6BAC
6B33: 6F         LD           L,A
6B34: 75         LD           (HL),L
6B35: 20 70      JR           NZ,$6BA7
6B37: 6C         LD           L,H
6B38: 61         LD           H,C
6B39: 79         LD           A,C
6B3A: 20 74      JR           NZ,$6BB0
6B3C: 68         LD           L,B
6B3D: 65         LD           H,L
6B3E: 20 20      JR           NZ,$6B60
6B40: 20 20      JR           NZ,$6B62
6B42: 49         LD           C,C
6B43: 6E         LD           L,(HL)
6B44: 73         LD           (HL),E
6B45: 74         LD           (HL),H
6B46: 72         LD           (HL),D
6B47: 75         LD           (HL),L
6B48: 6D         LD           L,L
6B49: 65         LD           H,L
6B4A: 6E         LD           L,(HL)
6B4B: 74         LD           (HL),H
6B4C: 73         LD           (HL),E
6B4D: 20 69      JR           NZ,$6BB8
6B4F: 6E         LD           L,(HL)
6B50: 20 20      JR           NZ,$6B72
6B52: 66         LD           H,(HL)
6B53: 72         LD           (HL),D
6B54: 6F         LD           L,A
6B55: 6E         LD           L,(HL)
6B56: 74         LD           (HL),H
6B57: 20 6F      JR           NZ,$6BC8
6B59: 66         LD           H,(HL)
6B5A: 20 74      JR           NZ,$6BD0
6B5C: 68         LD           L,B
6B5D: 65         LD           H,L
6B5E: 20 20      JR           NZ,$6B80
6B60: 20 20      JR           NZ,$6B82
6B62: 45         LD           B,L
6B63: 67         LD           H,A
6B64: 67         LD           H,A
6B65: 2C         INC         L
6B66: 20 74      JR           NZ,$6BDC
6B68: 68         LD           L,B
6B69: 65         LD           H,L
6B6A: 20 57      JR           NZ,$6BC3
6B6C: 69         LD           L,C
6B6D: 6E         LD           L,(HL)
6B6E: 64         LD           H,H
6B6F: 20 20      JR           NZ,$6B91
6B71: 20 46      JR           NZ,$6BB9
6B73: 69         LD           L,C
6B74: 73         LD           (HL),E
6B75: 68         LD           L,B
6B76: 20 77      JR           NZ,$6BEF
6B78: 69         LD           L,C
6B79: 6C         LD           L,H
6B7A: 6C         LD           L,H
6B7B: 20 77      JR           NZ,$6BF4
6B7D: 61         LD           H,C
6B7E: 6B         LD           L,E
6B7F: 65         LD           H,L
6B80: 20 20      JR           NZ,$6BA2
6B82: 61         LD           H,C
6B83: 6E         LD           L,(HL)
6B84: 64         LD           H,H
6B85: 20 79      JR           NZ,$6C00
6B87: 6F         LD           L,A
6B88: 75         LD           (HL),L
6B89: 20 77      JR           NZ,$6C02
6B8B: 69         LD           L,C
6B8C: 6C         LD           L,H
6B8D: 6C         LD           L,H
6B8E: 20 20      JR           NZ,$6BB0
6B90: 20 20      JR           NZ,$6BB2
6B92: 6C         LD           L,H
6B93: 65         LD           H,L
6B94: 61         LD           H,C
6B95: 76         HALT
6B96: 65         LD           H,L
6B97: 20 74      JR           NZ,$6C0D
6B99: 68         LD           L,B
6B9A: 69         LD           L,C
6B9B: 73         LD           (HL),E
6B9C: 20 20      JR           NZ,$6BBE
6B9E: 20 20      JR           NZ,$6BC0
6BA0: 20 20      JR           NZ,$6BC2
6BA2: 69         LD           L,C
6BA3: 73         LD           (HL),E
6BA4: 6C         LD           L,H
6BA5: 61         LD           H,C
6BA6: 6E         LD           L,(HL)
6BA7: 64         LD           H,H
6BA8: 2E 20      LD           L,$20
6BAA: 20 4E      JR           NZ,$6BFA
6BAC: 6F         LD           L,A
6BAD: 77         LD           (HL),A
6BAE: 2C         INC         L
6BAF: 20 20      JR           NZ,$6BD1
6BB1: 20 79      JR           NZ,$6C2C
6BB3: 6F         LD           L,A
6BB4: 75         LD           (HL),L
6BB5: 20 6D      JR           NZ,$6C24
6BB7: 75         LD           (HL),L
6BB8: 73         LD           (HL),E
6BB9: 74         LD           (HL),H
6BBA: 20 68      JR           NZ,$6C24
6BBC: 61         LD           H,C
6BBD: 73         LD           (HL),E
6BBE: 74         LD           (HL),H
6BBF: 65         LD           H,L
6BC0: 6E         LD           L,(HL)
6BC1: 20 74      JR           NZ,$6C37
6BC3: 6F         LD           L,A
6BC4: 20 74      JR           NZ,$6C3A
6BC6: 68         LD           L,B
6BC7: 65         LD           H,L
6BC8: 20 59      JR           NZ,$6C23
6BCA: 61         LD           H,C
6BCB: 72         LD           (HL),D
6BCC: 6E         LD           L,(HL)
6BCD: 61         LD           H,C
6BCE: 20 20      JR           NZ,$6BF0
6BD0: 20 20      JR           NZ,$6BF2
6BD2: 44         LD           B,H
6BD3: 65         LD           H,L
6BD4: 73         LD           (HL),E
6BD5: 65         LD           H,L
6BD6: 72         LD           (HL),D
6BD7: 74         LD           (HL),H
6BD8: 21 20 20   LD           HL,$2020
6BDB: 54         LD           D,H
6BDC: 68         LD           L,B
6BDD: 65         LD           H,L
6BDE: 20 20      JR           NZ,$6C00
6BE0: 20 20      JR           NZ,$6C02
6BE2: 64         LD           H,H
6BE3: 61         LD           H,C
6BE4: 72         LD           (HL),D
6BE5: 6B         LD           L,E
6BE6: 2C         INC         L
6BE7: 20 6D      JR           NZ,$6C56
6BE9: 6F         LD           L,A
6BEA: 6E         LD           L,(HL)
6BEB: 73         LD           (HL),E
6BEC: 74         LD           (HL),H
6BED: 72         LD           (HL),D
6BEE: 6F         LD           L,A
6BEF: 75         LD           (HL),L
6BF0: 73         LD           (HL),E
6BF1: 20 69      JR           NZ,$6C5C
6BF3: 6E         LD           L,(HL)
6BF4: 68         LD           L,B
6BF5: 61         LD           H,C
6BF6: 62         LD           H,D
6BF7: 69         LD           L,C
6BF8: 74         LD           (HL),H
6BF9: 61         LD           H,C
6BFA: 6E         LD           L,(HL)
6BFB: 74         LD           (HL),H
6BFC: 73         LD           (HL),E
6BFD: 20 6F      JR           NZ,$6C6E
6BFF: 66         LD           H,(HL)
6C00: 20 20      JR           NZ,$6C22
6C02: 74         LD           (HL),H
6C03: 68         LD           L,B
6C04: 65         LD           H,L
6C05: 20 73      JR           NZ,$6C7A
6C07: 61         LD           H,C
6C08: 6E         LD           L,(HL)
6C09: 64         LD           H,H
6C0A: 20 77      JR           NZ,$6C83
6C0C: 69         LD           L,C
6C0D: 6C         LD           L,H
6C0E: 6C         LD           L,H
6C0F: 20 20      JR           NZ,$6C31
6C11: 20 73      JR           NZ,$6C86
6C13: 68         LD           L,B
6C14: 6F         LD           L,A
6C15: 77         LD           (HL),A
6C16: 20 79      JR           NZ,$6C91
6C18: 6F         LD           L,A
6C19: 75         LD           (HL),L
6C1A: 20 74      JR           NZ,$6C90
6C1C: 68         LD           L,B
6C1D: 65         LD           H,L
6C1E: 20 20      JR           NZ,$6C40
6C20: 20 20      JR           NZ,$6C42
6C22: 77         LD           (HL),A
6C23: 61         LD           H,C
6C24: 79         LD           A,C
6C25: 21 20 48   LD           HL,$4820
6C28: 6F         LD           L,A
6C29: 6F         LD           L,A
6C2A: 74         LD           (HL),H
6C2B: 20 48      JR           NZ,$6C75
6C2D: 6F         LD           L,A
6C2E: 6F         LD           L,A
6C2F: 74         LD           (HL),H
6C30: 21 FF 48   LD           HL,$48FF
6C33: 6F         LD           L,A
6C34: 6F         LD           L,A
6C35: 74         LD           (HL),H
6C36: 21 20 20   LD           HL,$2020
6C39: 54         LD           D,H
6C3A: 68         LD           L,B
6C3B: 65         LD           H,L
6C3C: 20 73      JR           NZ,$6CB1
6C3E: 68         LD           L,B
6C3F: 61         LD           H,C
6C40: 70         LD           (HL),B
6C41: 65         LD           H,L
6C42: 6F         LD           L,A
6C43: 66         LD           H,(HL)
6C44: 20 74      JR           NZ,$6CBA
6C46: 68         LD           L,B
6C47: 65         LD           H,L
6C48: 20 6B      JR           NZ,$6CB5
6C4A: 65         LD           H,L
6C4B: 79         LD           A,C
6C4C: 20 73      JR           NZ,$6CC1
6C4E: 68         LD           L,B
6C4F: 6F         LD           L,A
6C50: 77         LD           (HL),A
6C51: 73         LD           (HL),E
6C52: 61         LD           H,C
6C53: 20 66      JR           NZ,$6CBB
6C55: 69         LD           L,C
6C56: 73         LD           (HL),E
6C57: 68         LD           L,B
6C58: 2C         INC         L
6C59: 20 73      JR           NZ,$6CCE
6C5B: 77         LD           (HL),A
6C5C: 69         LD           L,C
6C5D: 6D         LD           L,L
6C5E: 6D         LD           L,L
6C5F: 69         LD           L,C
6C60: 6E         LD           L,(HL)
6C61: 67         LD           H,A
6C62: 75         LD           (HL),L
6C63: 70         LD           (HL),B
6C64: 20 61      JR           NZ,$6CC7
6C66: 20 63      JR           NZ,$6CCB
6C68: 61         LD           H,C
6C69: 73         LD           (HL),E
6C6A: 63         LD           H,E
6C6B: 61         LD           H,C
6C6C: 64         LD           H,H
6C6D: 65         LD           H,L
6C6E: 20 6F      JR           NZ,$6CDF
6C70: 66         LD           H,(HL)
6C71: 20 77      JR           NZ,$6CEA
6C73: 61         LD           H,C
6C74: 74         LD           (HL),H
6C75: 65         LD           H,L
6C76: 72         LD           (HL),D
6C77: 21 20 20   LD           HL,$2020
6C7A: 47         LD           B,A
6C7B: 6F         LD           L,A
6C7C: 20 6E      JR           NZ,$6CEC
6C7E: 6F         LD           L,A
6C7F: 77         LD           (HL),A
6C80: 20 20      JR           NZ,$6CA2
6C82: 74         LD           (HL),H
6C83: 6F         LD           L,A
6C84: 20 74      JR           NZ,$6CFA
6C86: 68         LD           L,B
6C87: 65         LD           H,L
6C88: 20 6D      JR           NZ,$6CF7
6C8A: 6F         LD           L,A
6C8B: 75         LD           (HL),L
6C8C: 6E         LD           L,(HL)
6C8D: 74         LD           (HL),H
6C8E: 61         LD           H,C
6C8F: 69         LD           L,C
6C90: 6E         LD           L,(HL)
6C91: 20 77      JR           NZ,$6D0A
6C93: 61         LD           H,C
6C94: 74         LD           (HL),H
6C95: 65         LD           H,L
6C96: 72         LD           (HL),D
6C97: 66         LD           H,(HL)
6C98: 61         LD           H,C
6C99: 6C         LD           L,H
6C9A: 6C         LD           L,H
6C9B: 21 20 20   LD           HL,$2020
6C9E: 41         LD           B,C
6C9F: 20 20      JR           NZ,$6CC1
6CA1: 20 6C      JR           NZ,$6D0F
6CA3: 65         LD           H,L
6CA4: 61         LD           H,C
6CA5: 70         LD           (HL),B
6CA6: 20 66      JR           NZ,$6D0E
6CA8: 72         LD           (HL),D
6CA9: 6F         LD           L,A
6CAA: 6D         LD           L,L
6CAB: 20 74      JR           NZ,$6D21
6CAD: 68         LD           L,B
6CAE: 65         LD           H,L
6CAF: 20 20      JR           NZ,$6CD1
6CB1: 20 74      JR           NZ,$6D27
6CB3: 6F         LD           L,A
6CB4: 70         LD           (HL),B
6CB5: 20 61      JR           NZ,$6D18
6CB7: 6E         LD           L,(HL)
6CB8: 64         LD           H,H
6CB9: 20 79      JR           NZ,$6D34
6CBB: 6F         LD           L,A
6CBC: 75         LD           (HL),L
6CBD: 20 77      JR           NZ,$6D36
6CBF: 69         LD           L,C
6CC0: 6C         LD           L,H
6CC1: 6C         LD           L,H
6CC2: 72         LD           (HL),D
6CC3: 65         LD           H,L
6CC4: 61         LD           H,C
6CC5: 63         LD           H,E
6CC6: 68         LD           L,B
6CC7: 20 79      JR           NZ,$6D42
6CC9: 6F         LD           L,A
6CCA: 75         LD           (HL),L
6CCB: 72         LD           (HL),D
6CCC: 20 67      JR           NZ,$6D35
6CCE: 6F         LD           L,A
6CCF: 61         LD           H,C
6CD0: 6C         LD           L,H
6CD1: 21 FF 48   LD           HL,$48FF
6CD4: 6F         LD           L,A
6CD5: 6F         LD           L,A
6CD6: 74         LD           (HL),H
6CD7: 21 20 20   LD           HL,$2020
6CDA: 54         LD           D,H
6CDB: 68         LD           L,B
6CDC: 65         LD           H,L
6CDD: 72         LD           (HL),D
6CDE: 65         LD           H,L
6CDF: 20 61      JR           NZ,$6D42
6CE1: 72         LD           (HL),D
6CE2: 65         LD           H,L
6CE3: 74         LD           (HL),H
6CE4: 77         LD           (HL),A
6CE5: 6F         LD           L,A
6CE6: 20 73      JR           NZ,$6D5B
6CE8: 68         LD           L,B
6CE9: 72         LD           (HL),D
6CEA: 69         LD           L,C
6CEB: 6E         LD           L,(HL)
6CEC: 65         LD           H,L
6CED: 73         LD           (HL),E
6CEE: 2C         INC         L
6CEF: 20 6F      JR           NZ,$6D60
6CF1: 6E         LD           L,(HL)
6CF2: 65         LD           H,L
6CF3: 74         LD           (HL),H
6CF4: 6F         LD           L,A
6CF5: 20 74      JR           NZ,$6D6B
6CF7: 68         LD           L,B
6CF8: 65         LD           H,L
6CF9: 20 6E      JR           NZ,$6D69
6CFB: 6F         LD           L,A
6CFC: 72         LD           (HL),D
6CFD: 74         LD           (HL),H
6CFE: 68         LD           L,B
6CFF: 2C         INC         L
6D00: 20 20      JR           NZ,$6D22
6D02: 20 74      JR           NZ,$6D78
6D04: 68         LD           L,B
6D05: 65         LD           H,L
6D06: 20 6F      JR           NZ,$6D77
6D08: 74         LD           (HL),H
6D09: 68         LD           L,B
6D0A: 65         LD           H,L
6D0B: 72         LD           (HL),D
6D0C: 20 74      JR           NZ,$6D82
6D0E: 6F         LD           L,A
6D0F: 20 74      JR           NZ,$6D85
6D11: 68         LD           L,B
6D12: 65         LD           H,L
6D13: 73         LD           (HL),E
6D14: 6F         LD           L,A
6D15: 75         LD           (HL),L
6D16: 74         LD           (HL),H
6D17: 68         LD           L,B
6D18: 2E 20      LD           L,$20
6D1A: 20 46      JR           NZ,$6D62
6D1C: 69         LD           L,C
6D1D: 72         LD           (HL),D
6D1E: 73         LD           (HL),E
6D1F: 74         LD           (HL),H
6D20: 2C         INC         L
6D21: 20 20      JR           NZ,$6D43
6D23: 68         LD           L,B
6D24: 65         LD           H,L
6D25: 61         LD           H,C
6D26: 64         LD           H,H
6D27: 20 73      JR           NZ,$6D9C
6D29: 6F         LD           L,A
6D2A: 75         LD           (HL),L
6D2B: 74         LD           (HL),H
6D2C: 68         LD           L,B
6D2D: 2C         INC         L
6D2E: 20 20      JR           NZ,$6D50
6D30: 20 20      JR           NZ,$6D52
6D32: 20 77      JR           NZ,$6DAB
6D34: 68         LD           L,B
6D35: 65         LD           H,L
6D36: 72         LD           (HL),D
6D37: 65         LD           H,L
6D38: 20 61      JR           NZ,$6D9B
6D3A: 6E         LD           L,(HL)
6D3B: 63         LD           H,E
6D3C: 69         LD           L,C
6D3D: 65         LD           H,L
6D3E: 6E         LD           L,(HL)
6D3F: 74         LD           (HL),H
6D40: 20 20      JR           NZ,$6D62
6D42: 20 72      JR           NZ,$6DB6
6D44: 75         LD           (HL),L
6D45: 69         LD           L,C
6D46: 6E         LD           L,(HL)
6D47: 73         LD           (HL),E
6D48: 20 73      JR           NZ,$6DBD
6D4A: 70         LD           (HL),B
6D4B: 65         LD           H,L
6D4C: 61         LD           H,C
6D4D: 6B         LD           L,E
6D4E: 20 6F      JR           NZ,$6DBF
6D50: 66         LD           H,(HL)
6D51: 20 20      JR           NZ,$6D73
6D53: 74         LD           (HL),H
6D54: 68         LD           L,B
6D55: 65         LD           H,L
6D56: 20 57      JR           NZ,$6DAF
6D58: 69         LD           L,C
6D59: 6E         LD           L,(HL)
6D5A: 64         LD           H,H
6D5B: 20 46      JR           NZ,$6DA3
6D5D: 69         LD           L,C
6D5E: 73         LD           (HL),E
6D5F: 68         LD           L,B
6D60: 2E 2E      LD           L,$2E
6D62: 2E 59      LD           L,$59
6D64: 6F         LD           L,A
6D65: 75         LD           (HL),L
6D66: 20 77      JR           NZ,$6DDF
6D68: 69         LD           L,C
6D69: 6C         LD           L,H
6D6A: 6C         LD           L,H
6D6B: 20 6C      JR           NZ,$6DD9
6D6D: 65         LD           H,L
6D6E: 61         LD           H,C
6D6F: 72         LD           (HL),D
6D70: 6E         LD           L,(HL)
6D71: 20 20      JR           NZ,$6D93
6D73: 6D         LD           L,L
6D74: 75         LD           (HL),L
6D75: 63         LD           H,E
6D76: 68         LD           L,B
6D77: 20 74      JR           NZ,$6DED
6D79: 68         LD           L,B
6D7A: 65         LD           H,L
6D7B: 72         LD           (HL),D
6D7C: 65         LD           H,L
6D7D: 2E 2E      LD           L,$2E
6D7F: 2E FF      LD           L,$FF
6D81: 48         LD           C,B
6D82: 6F         LD           L,A
6D83: 6F         LD           L,A
6D84: 74         LD           (HL),H
6D85: 21 20 20   LD           HL,$2020
6D88: 49         LD           C,C
6D89: 20 73      JR           NZ,$6DFE
6D8B: 65         LD           H,L
6D8C: 65         LD           H,L
6D8D: 20 79      JR           NZ,$6E08
6D8F: 6F         LD           L,A
6D90: 75         LD           (HL),L
6D91: 68         LD           L,B
6D92: 61         LD           H,C
6D93: 76         HALT
6D94: 65         LD           H,L
6D95: 20 72      JR           NZ,$6E09
6D97: 65         LD           H,L
6D98: 61         LD           H,C
6D99: 64         LD           H,H
6D9A: 20 74      JR           NZ,$6E10
6D9C: 68         LD           L,B
6D9D: 65         LD           H,L
6D9E: 20 20      JR           NZ,$6DC0
6DA0: 20 72      JR           NZ,$6E14
6DA2: 65         LD           H,L
6DA3: 6C         LD           L,H
6DA4: 69         LD           L,C
6DA5: 65         LD           H,L
6DA6: 66         LD           H,(HL)
6DA7: 2E 2E      LD           L,$2E
6DA9: 2E 20      LD           L,$20
6DAB: 20 57      JR           NZ,$6E04
6DAD: 68         LD           L,B
6DAE: 69         LD           L,C
6DAF: 6C         LD           L,H
6DB0: 65         LD           H,L
6DB1: 69         LD           L,C
6DB2: 74         LD           (HL),H
6DB3: 20 64      JR           NZ,$6E19
6DB5: 6F         LD           L,A
6DB6: 65         LD           H,L
6DB7: 73         LD           (HL),E
6DB8: 20 73      JR           NZ,$6E2D
6DBA: 61         LD           H,C
6DBB: 79         LD           A,C
6DBC: 20 74      JR           NZ,$6E32
6DBE: 68         LD           L,B
6DBF: 65         LD           H,L
6DC0: 20 69      JR           NZ,$6E2B
6DC2: 73         LD           (HL),E
6DC3: 6C         LD           L,H
6DC4: 61         LD           H,C
6DC5: 6E         LD           L,(HL)
6DC6: 64         LD           H,H
6DC7: 20 69      JR           NZ,$6E32
6DC9: 73         LD           (HL),E
6DCA: 20 62      JR           NZ,$6E2E
6DCC: 75         LD           (HL),L
6DCD: 74         LD           (HL),H
6DCE: 20 61      JR           NZ,$6E31
6DD0: 20 64      JR           NZ,$6E36
6DD2: 72         LD           (HL),D
6DD3: 65         LD           H,L
6DD4: 61         LD           H,C
6DD5: 6D         LD           L,L
6DD6: 20 6F      JR           NZ,$6E47
6DD8: 66         LD           H,(HL)
6DD9: 20 74      JR           NZ,$6E4F
6DDB: 68         LD           L,B
6DDC: 65         LD           H,L
6DDD: 20 20      JR           NZ,$6DFF
6DDF: 20 20      JR           NZ,$6E01
6DE1: 57         LD           D,A
6DE2: 69         LD           L,C
6DE3: 6E         LD           L,(HL)
6DE4: 64         LD           H,H
6DE5: 20 46      JR           NZ,$6E2D
6DE7: 69         LD           L,C
6DE8: 73         LD           (HL),E
6DE9: 68         LD           L,B
6DEA: 2C         INC         L
6DEB: 20 6E      JR           NZ,$6E5B
6DED: 6F         LD           L,A
6DEE: 20 20      JR           NZ,$6E10
6DF0: 20 6F      JR           NZ,$6E61
6DF2: 6E         LD           L,(HL)
6DF3: 65         LD           H,L
6DF4: 20 69      JR           NZ,$6E5F
6DF6: 73         LD           (HL),E
6DF7: 20 72      JR           NZ,$6E6B
6DF9: 65         LD           H,L
6DFA: 61         LD           H,C
6DFB: 6C         LD           L,H
6DFC: 6C         LD           L,H
6DFD: 79         LD           A,C
6DFE: 20 20      JR           NZ,$6E20
6E00: 20 73      JR           NZ,$6E75
6E02: 75         LD           (HL),L
6E03: 72         LD           (HL),D
6E04: 65         LD           H,L
6E05: 2E 2E      LD           L,$2E
6E07: 2E 20      LD           L,$20
6E09: 20 4A      JR           NZ,$6E55
6E0B: 75         LD           (HL),L
6E0C: 73         LD           (HL),E
6E0D: 74         LD           (HL),H
6E0E: 20 61      JR           NZ,$6E71
6E10: 73         LD           (HL),E
6E11: 79         LD           A,C
6E12: 6F         LD           L,A
6E13: 75         LD           (HL),L
6E14: 20 63      JR           NZ,$6E79
6E16: 61         LD           H,C
6E17: 6E         LD           L,(HL)
6E18: 6E         LD           L,(HL)
6E19: 6F         LD           L,A
6E1A: 74         LD           (HL),H
6E1B: 20 6B      JR           NZ,$6E88
6E1D: 6E         LD           L,(HL)
6E1E: 6F         LD           L,A
6E1F: 77         LD           (HL),A
6E20: 20 69      JR           NZ,$6E8B
6E22: 66         LD           H,(HL)
6E23: 20 61      JR           NZ,$6E86
6E25: 20 63      JR           NZ,$6E8A
6E27: 68         LD           L,B
6E28: 65         LD           H,L
6E29: 73         LD           (HL),E
6E2A: 74         LD           (HL),H
6E2B: 20 68      JR           NZ,$6E95
6E2D: 6F         LD           L,A
6E2E: 6C         LD           L,H
6E2F: 64         LD           H,H
6E30: 73         LD           (HL),E
6E31: 74         LD           (HL),H
6E32: 72         LD           (HL),D
6E33: 65         LD           H,L
6E34: 61         LD           H,C
6E35: 73         LD           (HL),E
6E36: 75         LD           (HL),L
6E37: 72         LD           (HL),D
6E38: 65         LD           H,L
6E39: 20 75      JR           NZ,$6EB0
6E3B: 6E         LD           L,(HL)
6E3C: 74         LD           (HL),H
6E3D: 69         LD           L,C
6E3E: 6C         LD           L,H
6E3F: 20 20      JR           NZ,$6E61
6E41: 79         LD           A,C
6E42: 6F         LD           L,A
6E43: 75         LD           (HL),L
6E44: 20 6F      JR           NZ,$6EB5
6E46: 70         LD           (HL),B
6E47: 65         LD           H,L
6E48: 6E         LD           L,(HL)
6E49: 20 69      JR           NZ,$6EB4
6E4B: 74         LD           (HL),H
6E4C: 2C         INC         L
6E4D: 20 73      JR           NZ,$6EC2
6E4F: 6F         LD           L,A
6E50: 20 79      JR           NZ,$6ECB
6E52: 6F         LD           L,A
6E53: 75         LD           (HL),L
6E54: 20 63      JR           NZ,$6EB9
6E56: 61         LD           H,C
6E57: 6E         LD           L,(HL)
6E58: 6E         LD           L,(HL)
6E59: 6F         LD           L,A
6E5A: 74         LD           (HL),H
6E5B: 20 74      JR           NZ,$6ED1
6E5D: 65         LD           H,L
6E5E: 6C         LD           L,H
6E5F: 6C         LD           L,H
6E60: 20 69      JR           NZ,$6ECB
6E62: 66         LD           H,(HL)
6E63: 20 74      JR           NZ,$6ED9
6E65: 68         LD           L,B
6E66: 69         LD           L,C
6E67: 73         LD           (HL),E
6E68: 20 69      JR           NZ,$6ED3
6E6A: 73         LD           (HL),E
6E6B: 20 61      JR           NZ,$6ECE
6E6D: 20 20      JR           NZ,$6E8F
6E6F: 20 20      JR           NZ,$6E91
6E71: 64         LD           H,H
6E72: 72         LD           (HL),D
6E73: 65         LD           H,L
6E74: 61         LD           H,C
6E75: 6D         LD           L,L
6E76: 20 75      JR           NZ,$6EED
6E78: 6E         LD           L,(HL)
6E79: 74         LD           (HL),H
6E7A: 69         LD           L,C
6E7B: 6C         LD           L,H
6E7C: 20 79      JR           NZ,$6EF7
6E7E: 6F         LD           L,A
6E7F: 75         LD           (HL),L
6E80: 20 61      JR           NZ,$6EE3
6E82: 77         LD           (HL),A
6E83: 61         LD           H,C
6E84: 6B         LD           L,E
6E85: 65         LD           H,L
6E86: 6E         LD           L,(HL)
6E87: 2E 2E      LD           L,$2E
6E89: 2E 20      LD           L,$20
6E8B: 20 54      JR           NZ,$6EE1
6E8D: 68         LD           L,B
6E8E: 65         LD           H,L
6E8F: 20 20      JR           NZ,$6EB1
6E91: 6F         LD           L,A
6E92: 6E         LD           L,(HL)
6E93: 6C         LD           L,H
6E94: 79         LD           A,C
6E95: 20 6F      JR           NZ,$6F06
6E97: 6E         LD           L,(HL)
6E98: 65         LD           H,L
6E99: 20 77      JR           NZ,$6F12
6E9B: 68         LD           L,B
6E9C: 6F         LD           L,A
6E9D: 20 20      JR           NZ,$6EBF
6E9F: 20 20      JR           NZ,$6EC1
6EA1: 6B         LD           L,E
6EA2: 6E         LD           L,(HL)
6EA3: 6F         LD           L,A
6EA4: 77         LD           (HL),A
6EA5: 73         LD           (HL),E
6EA6: 20 66      JR           NZ,$6F0E
6EA8: 6F         LD           L,A
6EA9: 72         LD           (HL),D
6EAA: 20 73      JR           NZ,$6F1F
6EAC: 75         LD           (HL),L
6EAD: 72         LD           (HL),D
6EAE: 65         LD           H,L
6EAF: 20 20      JR           NZ,$6ED1
6EB1: 69         LD           L,C
6EB2: 73         LD           (HL),E
6EB3: 20 74      JR           NZ,$6F29
6EB5: 68         LD           L,B
6EB6: 65         LD           H,L
6EB7: 20 57      JR           NZ,$6F10
6EB9: 69         LD           L,C
6EBA: 6E         LD           L,(HL)
6EBB: 64         LD           H,H
6EBC: 20 20      JR           NZ,$6EDE
6EBE: 20 20      JR           NZ,$6EE0
6EC0: 20 46      JR           NZ,$6F08
6EC2: 69         LD           L,C
6EC3: 73         LD           (HL),E
6EC4: 68         LD           L,B
6EC5: 2E 2E      LD           L,$2E
6EC7: 2E 20      LD           L,$20
6EC9: 20 54      JR           NZ,$6F1F
6ECB: 72         LD           (HL),D
6ECC: 75         LD           (HL),L
6ECD: 73         LD           (HL),E
6ECE: 74         LD           (HL),H
6ECF: 20 20      JR           NZ,$6EF1
6ED1: 79         LD           A,C
6ED2: 6F         LD           L,A
6ED3: 75         LD           (HL),L
6ED4: 72         LD           (HL),D
6ED5: 20 66      JR           NZ,$6F3D
6ED7: 65         LD           H,L
6ED8: 65         LD           H,L
6ED9: 6C         LD           L,H
6EDA: 69         LD           L,C
6EDB: 6E         LD           L,(HL)
6EDC: 67         LD           H,A
6EDD: 73         LD           (HL),E
6EDE: 2E 2E      LD           L,$2E
6EE0: 2E 53      LD           L,$53
6EE2: 6F         LD           L,A
6EE3: 6D         LD           L,L
6EE4: 65         LD           H,L
6EE5: 64         LD           H,H
6EE6: 61         LD           H,C
6EE7: 79         LD           A,C
6EE8: 20 79      JR           NZ,$6F63
6EEA: 6F         LD           L,A
6EEB: 75         LD           (HL),L
6EEC: 20 77      JR           NZ,$6F65
6EEE: 69         LD           L,C
6EEF: 6C         LD           L,H
6EF0: 6C         LD           L,H
6EF1: 6B         LD           L,E
6EF2: 6E         LD           L,(HL)
6EF3: 6F         LD           L,A
6EF4: 77         LD           (HL),A
6EF5: 20 66      JR           NZ,$6F5D
6EF7: 6F         LD           L,A
6EF8: 72         LD           (HL),D
6EF9: 20 73      JR           NZ,$6F6E
6EFB: 75         LD           (HL),L
6EFC: 72         LD           (HL),D
6EFD: 65         LD           H,L
6EFE: 2E 2E      LD           L,$2E
6F00: 2E FF      LD           L,$FF
6F02: 48         LD           C,B
6F03: 6F         LD           L,A
6F04: 6F         LD           L,A
6F05: 74         LD           (HL),H
6F06: 21 20 20   LD           HL,$2020
6F09: 54         LD           D,H
6F0A: 68         LD           L,B
6F0B: 65         LD           H,L
6F0C: 20 6D      JR           NZ,$6F7B
6F0E: 61         LD           H,C
6F0F: 6E         LD           L,(HL)
6F10: 79         LD           A,C
6F11: 20 6D      JR           NZ,$6F80
6F13: 6F         LD           L,A
6F14: 6E         LD           L,(HL)
6F15: 73         LD           (HL),E
6F16: 74         LD           (HL),H
6F17: 65         LD           H,L
6F18: 72         LD           (HL),D
6F19: 73         LD           (HL),E
6F1A: 20 6F      JR           NZ,$6F8B
6F1C: 66         LD           H,(HL)
6F1D: 20 74      JR           NZ,$6F93
6F1F: 68         LD           L,B
6F20: 69         LD           L,C
6F21: 73         LD           (HL),E
6F22: 69         LD           L,C
6F23: 73         LD           (HL),E
6F24: 6C         LD           L,H
6F25: 61         LD           H,C
6F26: 6E         LD           L,(HL)
6F27: 64         LD           H,H
6F28: 20 66      JR           NZ,$6F90
6F2A: 65         LD           H,L
6F2B: 61         LD           H,C
6F2C: 72         LD           (HL),D
6F2D: 20 74      JR           NZ,$6FA3
6F2F: 68         LD           L,B
6F30: 61         LD           H,C
6F31: 74         LD           (HL),H
6F32: 74         LD           (HL),H
6F33: 68         LD           L,B
6F34: 65         LD           H,L
6F35: 20 57      JR           NZ,$6F8E
6F37: 69         LD           L,C
6F38: 6E         LD           L,(HL)
6F39: 64         LD           H,H
6F3A: 20 46      JR           NZ,$6F82
6F3C: 69         LD           L,C
6F3D: 73         LD           (HL),E
6F3E: 68         LD           L,B
6F3F: 20 69      JR           NZ,$6FAA
6F41: 73         LD           (HL),E
6F42: 61         LD           H,C
6F43: 62         LD           H,D
6F44: 6F         LD           L,A
6F45: 75         LD           (HL),L
6F46: 74         LD           (HL),H
6F47: 20 74      JR           NZ,$6FBD
6F49: 6F         LD           L,A
6F4A: 20 61      JR           NZ,$6FAD
6F4C: 77         LD           (HL),A
6F4D: 61         LD           H,C
6F4E: 6B         LD           L,E
6F4F: 65         LD           H,L
6F50: 6E         LD           L,(HL)
6F51: 21 54 68   LD           HL,$6854
6F54: 65         LD           H,L
6F55: 20 6D      JR           NZ,$6FC4
6F57: 6F         LD           L,A
6F58: 6E         LD           L,(HL)
6F59: 73         LD           (HL),E
6F5A: 74         LD           (HL),H
6F5B: 65         LD           H,L
6F5C: 72         LD           (HL),D
6F5D: 73         LD           (HL),E
6F5E: 5E         LD           E,(HL)
6F5F: 20 20      JR           NZ,$6F81
6F61: 20 70      JR           NZ,$6FD3
6F63: 6F         LD           L,A
6F64: 77         LD           (HL),A
6F65: 65         LD           H,L
6F66: 72         LD           (HL),D
6F67: 20 69      JR           NZ,$6FD2
6F69: 73         LD           (HL),E
6F6A: 20 72      JR           NZ,$6FDE
6F6C: 65         LD           H,L
6F6D: 61         LD           H,C
6F6E: 6C         LD           L,H
6F6F: 21 20 20   LD           HL,$2020
6F72: 54         LD           D,H
6F73: 68         LD           L,B
6F74: 65         LD           H,L
6F75: 79         LD           A,C
6F76: 20 6D      JR           NZ,$6FE5
6F78: 61         LD           H,C
6F79: 79         LD           A,C
6F7A: 20 63      JR           NZ,$6FDF
6F7C: 6F         LD           L,A
6F7D: 6E         LD           L,(HL)
6F7E: 71         LD           (HL),C
6F7F: 75         LD           (HL),L
6F80: 65         LD           H,L
6F81: 72         LD           (HL),D
6F82: 74         LD           (HL),H
6F83: 68         LD           L,B
6F84: 65         LD           H,L
6F85: 20 69      JR           NZ,$6FF0
6F87: 73         LD           (HL),E
6F88: 6C         LD           L,H
6F89: 61         LD           H,C
6F8A: 6E         LD           L,(HL)
6F8B: 64         LD           H,H
6F8C: 20 61      JR           NZ,$6FEF
6F8E: 6E         LD           L,(HL)
6F8F: 64         LD           H,H
6F90: 20 20      JR           NZ,$6FB2
6F92: 64         LD           H,H
6F93: 65         LD           H,L
6F94: 73         LD           (HL),E
6F95: 74         LD           (HL),H
6F96: 72         LD           (HL),D
6F97: 6F         LD           L,A
6F98: 79         LD           A,C
6F99: 20 74      JR           NZ,$700F
6F9B: 68         LD           L,B
6F9C: 65         LD           H,L
6F9D: 69         LD           L,C
6F9E: 72         LD           (HL),D
6F9F: 20 20      JR           NZ,$6FC1
6FA1: 20 66      JR           NZ,$7009
6FA3: 6F         LD           L,A
6FA4: 65         LD           H,L
6FA5: 73         LD           (HL),E
6FA6: 21 20 20   LD           HL,$2020
6FA9: 54         LD           D,H
6FAA: 68         LD           L,B
6FAB: 61         LD           H,C
6FAC: 74         LD           (HL),H
6FAD: 20 64      JR           NZ,$7013
6FAF: 61         LD           H,C
6FB0: 79         LD           A,C
6FB1: 20 6D      JR           NZ,$7020
6FB3: 61         LD           H,C
6FB4: 79         LD           A,C
6FB5: 20 63      JR           NZ,$701A
6FB7: 6F         LD           L,A
6FB8: 6D         LD           L,L
6FB9: 65         LD           H,L
6FBA: 20 73      JR           NZ,$702F
6FBC: 6F         LD           L,A
6FBD: 6F         LD           L,A
6FBE: 6E         LD           L,(HL)
6FBF: 21 20 20   LD           HL,$2020
6FC2: 4E         LD           C,(HL)
6FC3: 6F         LD           L,A
6FC4: 77         LD           (HL),A
6FC5: 2C         INC         L
6FC6: 20 67      JR           NZ,$702F
6FC8: 6F         LD           L,A
6FC9: 20 74      JR           NZ,$703F
6FCB: 6F         LD           L,A
6FCC: 20 74      JR           NZ,$7042
6FCE: 68         LD           L,B
6FCF: 65         LD           H,L
6FD0: 20 20      JR           NZ,$6FF2
6FD2: 6D         LD           L,L
6FD3: 6F         LD           L,A
6FD4: 75         LD           (HL),L
6FD5: 6E         LD           L,(HL)
6FD6: 74         LD           (HL),H
6FD7: 61         LD           H,C
6FD8: 69         LD           L,C
6FD9: 6E         LD           L,(HL)
6FDA: 20 74      JR           NZ,$7050
6FDC: 6F         LD           L,A
6FDD: 77         LD           (HL),A
6FDE: 65         LD           H,L
6FDF: 72         LD           (HL),D
6FE0: 21 20 46   LD           HL,$4620
6FE3: 6C         LD           L,H
6FE4: 79         LD           A,C
6FE5: 20 6C      JR           NZ,$7053
6FE7: 69         LD           L,C
6FE8: 6B         LD           L,E
6FE9: 65         LD           H,L
6FEA: 20 61      JR           NZ,$704D
6FEC: 20 62      JR           NZ,$7050
6FEE: 69         LD           L,C
6FEF: 72         LD           (HL),D
6FF0: 64         LD           H,H
6FF1: 21 48 6F   LD           HL,$6F48
6FF4: 6F         LD           L,A
6FF5: 74         LD           (HL),H
6FF6: 21 20 48   LD           HL,$4820
6FF9: 6F         LD           L,A
6FFA: 6F         LD           L,A
6FFB: 74         LD           (HL),H
6FFC: 21 FF 54   LD           HL,$54FF
6FFF: 68         LD           L,B
7000: 65         LD           H,L
7001: 20 67      JR           NZ,$706A
7003: 6F         LD           L,A
7004: 69         LD           L,C
7005: 6E         LD           L,(HL)
7006: 67         LD           H,A
7007: 20 69      JR           NZ,$7072
7009: 73         LD           (HL),E
700A: 20 20      JR           NZ,$702C
700C: 20 20      JR           NZ,$702E
700E: 6D         LD           L,L
700F: 75         LD           (HL),L
7010: 63         LD           H,E
7011: 68         LD           L,B
7012: 20 6D      JR           NZ,$7081
7014: 6F         LD           L,A
7015: 72         LD           (HL),D
7016: 65         LD           H,L
7017: 20 74      JR           NZ,$708D
7019: 72         LD           (HL),D
701A: 79         LD           A,C
701B: 69         LD           L,C
701C: 6E         LD           L,(HL)
701D: 67         LD           H,A
701E: 66         LD           H,(HL)
701F: 72         LD           (HL),D
7020: 6F         LD           L,A
7021: 6D         LD           L,L
7022: 20 74      JR           NZ,$7098
7024: 68         LD           L,B
7025: 69         LD           L,C
7026: 73         LD           (HL),E
7027: 20 70      JR           NZ,$7099
7029: 6F         LD           L,A
702A: 69         LD           L,C
702B: 6E         LD           L,(HL)
702C: 74         LD           (HL),H
702D: 21 59 6F   LD           HL,$6F59
7030: 75         LD           (HL),L
7031: 20 68      JR           NZ,$709B
7033: 61         LD           H,C
7034: 76         HALT
7035: 65         LD           H,L
7036: 20 6F      JR           NZ,$70A7
7038: 6E         LD           L,(HL)
7039: 6C         LD           L,H
703A: 79         LD           A,C
703B: 20 20      JR           NZ,$705D
703D: 20 74      JR           NZ,$70B3
703F: 77         LD           (HL),A
7040: 6F         LD           L,A
7041: 20 6D      JR           NZ,$70B0
7043: 6F         LD           L,A
7044: 72         LD           (HL),D
7045: 65         LD           H,L
7046: 20 74      JR           NZ,$70BC
7048: 61         LD           H,C
7049: 73         LD           (HL),E
704A: 6B         LD           L,E
704B: 73         LD           (HL),E
704C: 20 20      JR           NZ,$706E
704E: 74         LD           (HL),H
704F: 6F         LD           L,A
7050: 20 61      JR           NZ,$70B3
7052: 63         LD           H,E
7053: 63         LD           H,E
7054: 6F         LD           L,A
7055: 6D         LD           L,L
7056: 70         LD           (HL),B
7057: 6C         LD           L,H
7058: 69         LD           L,C
7059: 73         LD           (HL),E
705A: 68         LD           L,B
705B: 21 20 20   LD           HL,$2020
705E: 54         LD           D,H
705F: 68         LD           L,B
7060: 65         LD           H,L
7061: 20 66      JR           NZ,$70C9
7063: 69         LD           L,C
7064: 72         LD           (HL),D
7065: 73         LD           (HL),E
7066: 74         LD           (HL),H
7067: 20 69      JR           NZ,$70D2
7069: 73         LD           (HL),E
706A: 20 69      JR           NZ,$70D5
706C: 6E         LD           L,(HL)
706D: 20 74      JR           NZ,$70E3
706F: 68         LD           L,B
7070: 65         LD           H,L
7071: 20 65      JR           NZ,$70D8
7073: 61         LD           H,C
7074: 73         LD           (HL),E
7075: 74         LD           (HL),H
7076: 20 70      JR           NZ,$70E8
7078: 61         LD           H,C
7079: 72         LD           (HL),D
707A: 74         LD           (HL),H
707B: 20 6F      JR           NZ,$70EC
707D: 66         LD           H,(HL)
707E: 74         LD           (HL),H
707F: 68         LD           L,B
7080: 65         LD           H,L
7081: 20 6D      JR           NZ,$70F0
7083: 6F         LD           L,A
7084: 75         LD           (HL),L
7085: 6E         LD           L,(HL)
7086: 74         LD           (HL),H
7087: 61         LD           H,C
7088: 69         LD           L,C
7089: 6E         LD           L,(HL)
708A: 73         LD           (HL),E
708B: 2C         INC         L
708C: 20 20      JR           NZ,$70AE
708E: 74         LD           (HL),H
708F: 68         LD           L,B
7090: 65         LD           H,L
7091: 20 73      JR           NZ,$7106
7093: 65         LD           H,L
7094: 63         LD           H,E
7095: 6F         LD           L,A
7096: 6E         LD           L,(HL)
7097: 64         LD           H,H
7098: 20 69      JR           NZ,$7103
709A: 6E         LD           L,(HL)
709B: 20 20      JR           NZ,$70BD
709D: 20 74      JR           NZ,$7113
709F: 68         LD           L,B
70A0: 65         LD           H,L
70A1: 20 77      JR           NZ,$711A
70A3: 65         LD           H,L
70A4: 73         LD           (HL),E
70A5: 74         LD           (HL),H
70A6: 2E 20      LD           L,$20
70A8: 20 47      JR           NZ,$70F1
70AA: 6F         LD           L,A
70AB: 21 20 20   LD           HL,$2020
70AE: 54         LD           D,H
70AF: 68         LD           L,B
70B0: 65         LD           H,L
70B1: 20 57      JR           NZ,$710A
70B3: 69         LD           L,C
70B4: 6E         LD           L,(HL)
70B5: 64         LD           H,H
70B6: 20 46      JR           NZ,$70FE
70B8: 69         LD           L,C
70B9: 73         LD           (HL),E
70BA: 68         LD           L,B
70BB: 20 20      JR           NZ,$70DD
70BD: 20 67      JR           NZ,$7126
70BF: 72         LD           (HL),D
70C0: 6F         LD           L,A
70C1: 77         LD           (HL),A
70C2: 73         LD           (HL),E
70C3: 20 72      JR           NZ,$7137
70C5: 65         LD           H,L
70C6: 73         LD           (HL),E
70C7: 74         LD           (HL),H
70C8: 6C         LD           L,H
70C9: 65         LD           H,L
70CA: 73         LD           (HL),E
70CB: 73         LD           (HL),E
70CC: 21 FF 48   LD           HL,$48FF
70CF: 6F         LD           L,A
70D0: 6F         LD           L,A
70D1: 74         LD           (HL),H
70D2: 21 20 20   LD           HL,$2020
70D5: 49         LD           C,C
70D6: 74         LD           (HL),H
70D7: 20 68      JR           NZ,$7141
70D9: 61         LD           H,C
70DA: 73         LD           (HL),E
70DB: 20 20      JR           NZ,$70FD
70DD: 20 62      JR           NZ,$7141
70DF: 65         LD           H,L
70E0: 65         LD           H,L
70E1: 6E         LD           L,(HL)
70E2: 20 73      JR           NZ,$7157
70E4: 6F         LD           L,A
70E5: 6D         LD           L,L
70E6: 65         LD           H,L
70E7: 20 74      JR           NZ,$715D
70E9: 69         LD           L,C
70EA: 6D         LD           L,L
70EB: 65         LD           H,L
70EC: 20 20      JR           NZ,$710E
70EE: 73         LD           (HL),E
70EF: 69         LD           L,C
70F0: 6E         LD           L,(HL)
70F1: 63         LD           H,E
70F2: 65         LD           H,L
70F3: 20 6F      JR           NZ,$7164
70F5: 75         LD           (HL),L
70F6: 72         LD           (HL),D
70F7: 20 70      JR           NZ,$7169
70F9: 61         LD           H,C
70FA: 74         LD           (HL),H
70FB: 68         LD           L,B
70FC: 73         LD           (HL),E
70FD: 20 63      JR           NZ,$7162
70FF: 72         LD           (HL),D
7100: 6F         LD           L,A
7101: 73         LD           (HL),E
7102: 73         LD           (HL),E
7103: 65         LD           H,L
7104: 64         LD           H,H
7105: 2C         INC         L
7106: 20 6C      JR           NZ,$7174
7108: 61         LD           H,C
7109: 64         LD           H,H
710A: 2E 20      LD           L,$20
710C: 20 20      JR           NZ,$712E
710E: 59         LD           E,C
710F: 6F         LD           L,A
7110: 75         LD           (HL),L
7111: 20 6D      JR           NZ,$7180
7113: 75         LD           (HL),L
7114: 73         LD           (HL),E
7115: 74         LD           (HL),H
7116: 20 64      JR           NZ,$717C
7118: 69         LD           L,C
7119: 76         HALT
711A: 65         LD           H,L
711B: 20 20      JR           NZ,$713D
711D: 20 69      JR           NZ,$7188
711F: 6E         LD           L,(HL)
7120: 74         LD           (HL),H
7121: 6F         LD           L,A
7122: 20 74      JR           NZ,$7198
7124: 68         LD           L,B
7125: 65         LD           H,L
7126: 20 77      JR           NZ,$719F
7128: 61         LD           H,C
7129: 74         LD           (HL),H
712A: 65         LD           H,L
712B: 72         LD           (HL),D
712C: 73         LD           (HL),E
712D: 20 6F      JR           NZ,$719E
712F: 66         LD           H,(HL)
7130: 20 4D      JR           NZ,$717F
7132: 61         LD           H,C
7133: 72         LD           (HL),D
7134: 74         LD           (HL),H
7135: 68         LD           L,B
7136: 61         LD           H,C
7137: 5E         LD           E,(HL)
7138: 73         LD           (HL),E
7139: 20 42      JR           NZ,$717D
713B: 61         LD           H,C
713C: 79         LD           A,C
713D: 20 74      JR           NZ,$71B3
713F: 6F         LD           L,A
7140: 20 65      JR           NZ,$71A7
7142: 6E         LD           L,(HL)
7143: 74         LD           (HL),H
7144: 65         LD           H,L
7145: 72         LD           (HL),D
7146: 20 74      JR           NZ,$71BC
7148: 68         LD           L,B
7149: 65         LD           H,L
714A: 20 20      JR           NZ,$716C
714C: 20 20      JR           NZ,$716E
714E: 43         LD           B,E
714F: 61         LD           H,C
7150: 74         LD           (HL),H
7151: 66         LD           H,(HL)
7152: 69         LD           L,C
7153: 73         LD           (HL),E
7154: 68         LD           L,B
7155: 5E         LD           E,(HL)
7156: 73         LD           (HL),E
7157: 20 4D      JR           NZ,$71A6
7159: 61         LD           H,C
715A: 77         LD           (HL),A
715B: 2E 2E      LD           L,$2E
715D: 2E 54      LD           L,$54
715F: 68         LD           L,B
7160: 65         LD           H,L
7161: 20 63      JR           NZ,$71C6
7163: 6C         LD           L,H
7164: 6F         LD           L,A
7165: 73         LD           (HL),E
7166: 65         LD           H,L
7167: 72         LD           (HL),D
7168: 20 79      JR           NZ,$71E3
716A: 6F         LD           L,A
716B: 75         LD           (HL),L
716C: 20 20      JR           NZ,$718E
716E: 67         LD           H,A
716F: 65         LD           H,L
7170: 74         LD           (HL),H
7171: 20 74      JR           NZ,$71E7
7173: 6F         LD           L,A
7174: 20 74      JR           NZ,$71EA
7176: 68         LD           L,B
7177: 65         LD           H,L
7178: 20 57      JR           NZ,$71D1
717A: 69         LD           L,C
717B: 6E         LD           L,(HL)
717C: 64         LD           H,H
717D: 20 46      JR           NZ,$71C5
717F: 69         LD           L,C
7180: 73         LD           (HL),E
7181: 68         LD           L,B
7182: 2C         INC         L
7183: 20 74      JR           NZ,$71F9
7185: 68         LD           L,B
7186: 65         LD           H,L
7187: 20 6D      JR           NZ,$71F6
7189: 6F         LD           L,A
718A: 72         LD           (HL),D
718B: 65         LD           H,L
718C: 20 20      JR           NZ,$71AE
718E: 72         LD           (HL),D
718F: 65         LD           H,L
7190: 73         LD           (HL),E
7191: 74         LD           (HL),H
7192: 6C         LD           L,H
7193: 65         LD           H,L
7194: 73         LD           (HL),E
7195: 73         LD           (HL),E
7196: 20 68      JR           NZ,$7200
7198: 65         LD           H,L
7199: 20 20      JR           NZ,$71BB
719B: 20 20      JR           NZ,$71BD
719D: 20 73      JR           NZ,$7212
719F: 6C         LD           L,H
71A0: 65         LD           H,L
71A1: 65         LD           H,L
71A2: 70         LD           (HL),B
71A3: 73         LD           (HL),E
71A4: 2E 20      LD           L,$20
71A6: 20 43      JR           NZ,$71EB
71A8: 61         LD           H,C
71A9: 72         LD           (HL),D
71AA: 72         LD           (HL),D
71AB: 79         LD           A,C
71AC: 20 20      JR           NZ,$71CE
71AE: 6F         LD           L,A
71AF: 6E         LD           L,(HL)
71B0: 77         LD           (HL),A
71B1: 61         LD           H,C
71B2: 72         LD           (HL),D
71B3: 64         LD           H,H
71B4: 21 20 20   LD           HL,$2020
71B7: 48         LD           C,B
71B8: 6F         LD           L,A
71B9: 6F         LD           L,A
71BA: 74         LD           (HL),H
71BB: 21 FF 48   LD           HL,$48FF
71BE: 6F         LD           L,A
71BF: 6F         LD           L,A
71C0: 74         LD           (HL),H
71C1: 21 20 20   LD           HL,$2020
71C4: 54         LD           D,H
71C5: 68         LD           L,B
71C6: 61         LD           H,C
71C7: 74         LD           (HL),H
71C8: 20 67      JR           NZ,$7231
71CA: 69         LD           L,C
71CB: 72         LD           (HL),D
71CC: 6C         LD           L,H
71CD: 73         LD           (HL),E
71CE: 61         LD           H,C
71CF: 6E         LD           L,(HL)
71D0: 67         LD           H,A
71D1: 20 68      JR           NZ,$723B
71D3: 65         LD           H,L
71D4: 72         LD           (HL),D
71D5: 20 73      JR           NZ,$724A
71D7: 6F         LD           L,A
71D8: 6E         LD           L,(HL)
71D9: 67         LD           H,A
71DA: 20 69      JR           NZ,$7245
71DC: 6E         LD           L,(HL)
71DD: 66         LD           H,(HL)
71DE: 72         LD           (HL),D
71DF: 6F         LD           L,A
71E0: 6E         LD           L,(HL)
71E1: 74         LD           (HL),H
71E2: 20 6F      JR           NZ,$7253
71E4: 66         LD           H,(HL)
71E5: 20 74      JR           NZ,$725B
71E7: 68         LD           L,B
71E8: 65         LD           H,L
71E9: 20 20      JR           NZ,$720B
71EB: 20 20      JR           NZ,$720D
71ED: 45         LD           B,L
71EE: 67         LD           H,A
71EF: 67         LD           H,A
71F0: 21 20 48   LD           HL,$4820
71F3: 65         LD           H,L
71F4: 72         LD           (HL),D
71F5: 20 5E      JR           NZ,$7255
71F7: 42         LD           B,D
71F8: 61         LD           H,C
71F9: 6C         LD           L,H
71FA: 6C         LD           L,H
71FB: 61         LD           H,C
71FC: 64         LD           H,H
71FD: 6F         LD           L,A
71FE: 66         LD           H,(HL)
71FF: 20 74      JR           NZ,$7275
7201: 68         LD           L,B
7202: 65         LD           H,L
7203: 20 57      JR           NZ,$725C
7205: 69         LD           L,C
7206: 6E         LD           L,(HL)
7207: 64         LD           H,H
7208: 20 20      JR           NZ,$722A
720A: 20 20      JR           NZ,$722C
720C: 20 46      JR           NZ,$7254
720E: 69         LD           L,C
720F: 73         LD           (HL),E
7210: 68         LD           L,B
7211: 5E         LD           E,(HL)
7212: 20 69      JR           NZ,$727D
7214: 73         LD           (HL),E
7215: 20 61      JR           NZ,$7278
7217: 20 73      JR           NZ,$728C
7219: 6F         LD           L,A
721A: 6E         LD           L,(HL)
721B: 67         LD           H,A
721C: 20 6F      JR           NZ,$728D
721E: 66         LD           H,(HL)
721F: 20 61      JR           NZ,$7282
7221: 77         LD           (HL),A
7222: 61         LD           H,C
7223: 6B         LD           L,E
7224: 65         LD           H,L
7225: 6E         LD           L,(HL)
7226: 69         LD           L,C
7227: 6E         LD           L,(HL)
7228: 67         LD           H,A
7229: 21 20 20   LD           HL,$2020
722C: 20 44      JR           NZ,$7272
722E: 69         LD           L,C
722F: 64         LD           H,H
7230: 20 73      JR           NZ,$72A5
7232: 68         LD           L,B
7233: 65         LD           H,L
7234: 20 61      JR           NZ,$7297
7236: 63         LD           H,E
7237: 74         LD           (HL),H
7238: 75         LD           (HL),L
7239: 61         LD           H,C
723A: 6C         LD           L,H
723B: 6C         LD           L,H
723C: 79         LD           A,C
723D: 69         LD           L,C
723E: 6E         LD           L,(HL)
723F: 74         LD           (HL),H
7240: 65         LD           H,L
7241: 6E         LD           L,(HL)
7242: 64         LD           H,H
7243: 20 74      JR           NZ,$72B9
7245: 6F         LD           L,A
7246: 20 77      JR           NZ,$72BF
7248: 61         LD           H,C
7249: 6B         LD           L,E
724A: 65         LD           H,L
724B: 20 20      JR           NZ,$726D
724D: 74         LD           (HL),H
724E: 68         LD           L,B
724F: 65         LD           H,L
7250: 20 57      JR           NZ,$72A9
7252: 69         LD           L,C
7253: 6E         LD           L,(HL)
7254: 64         LD           H,H
7255: 20 46      JR           NZ,$729D
7257: 69         LD           L,C
7258: 73         LD           (HL),E
7259: 68         LD           L,B
725A: 3F         CCF
725B: 21 20 54   LD           HL,$5420
725E: 68         LD           L,B
725F: 65         LD           H,L
7260: 20 6E      JR           NZ,$72D0
7262: 65         LD           H,L
7263: 78         LD           A,B
7264: 74         LD           (HL),H
7265: 20 53      JR           NZ,$72BA
7267: 69         LD           L,C
7268: 72         LD           (HL),D
7269: 65         LD           H,L
726A: 6E         LD           L,(HL)
726B: 73         LD           (HL),E
726C: 5E         LD           E,(HL)
726D: 49         LD           C,C
726E: 6E         LD           L,(HL)
726F: 73         LD           (HL),E
7270: 74         LD           (HL),H
7271: 72         LD           (HL),D
7272: 75         LD           (HL),L
7273: 6D         LD           L,L
7274: 65         LD           H,L
7275: 6E         LD           L,(HL)
7276: 74         LD           (HL),H
7277: 20 69      JR           NZ,$72E2
7279: 73         LD           (HL),E
727A: 20 69      JR           NZ,$72E5
727C: 6E         LD           L,(HL)
727D: 74         LD           (HL),H
727E: 68         LD           L,B
727F: 65         LD           H,L
7280: 20 77      JR           NZ,$72F9
7282: 65         LD           H,L
7283: 73         LD           (HL),E
7284: 74         LD           (HL),H
7285: 2E 20      LD           L,$20
7287: 20 50      JR           NZ,$72D9
7289: 6C         LD           L,H
728A: 61         LD           H,C
728B: 79         LD           A,C
728C: 20 79      JR           NZ,$7307
728E: 6F         LD           L,A
728F: 75         LD           (HL),L
7290: 72         LD           (HL),D
7291: 20 6D      JR           NZ,$7300
7293: 65         LD           H,L
7294: 6C         LD           L,H
7295: 6F         LD           L,A
7296: 64         LD           H,H
7297: 69         LD           L,C
7298: 65         LD           H,L
7299: 73         LD           (HL),E
729A: 20 73      JR           NZ,$730F
729C: 6F         LD           L,A
729D: 74         LD           (HL),H
729E: 68         LD           L,B
729F: 65         LD           H,L
72A0: 20 75      JR           NZ,$7317
72A2: 6E         LD           L,(HL)
72A3: 6C         LD           L,H
72A4: 69         LD           L,C
72A5: 76         HALT
72A6: 69         LD           L,C
72A7: 6E         LD           L,(HL)
72A8: 67         LD           H,A
72A9: 20 20      JR           NZ,$72CB
72AB: 20 20      JR           NZ,$72CD
72AD: 73         LD           (HL),E
72AE: 74         LD           (HL),H
72AF: 6F         LD           L,A
72B0: 6E         LD           L,(HL)
72B1: 65         LD           H,L
72B2: 73         LD           (HL),E
72B3: 20 6D      JR           NZ,$7322
72B5: 69         LD           L,C
72B6: 67         LD           H,A
72B7: 68         LD           L,B
72B8: 74         LD           (HL),H
72B9: 20 20      JR           NZ,$72DB
72BB: 20 20      JR           NZ,$72DD
72BD: 68         LD           L,B
72BE: 65         LD           H,L
72BF: 61         LD           H,C
72C0: 72         LD           (HL),D
72C1: 21 20 20   LD           HL,$2020
72C4: 53         LD           D,E
72C5: 68         LD           L,B
72C6: 6F         LD           L,A
72C7: 77         LD           (HL),A
72C8: 20 79      JR           NZ,$7343
72CA: 6F         LD           L,A
72CB: 75         LD           (HL),L
72CC: 72         LD           (HL),D
72CD: 63         LD           H,E
72CE: 6F         LD           L,A
72CF: 75         LD           (HL),L
72D0: 72         LD           (HL),D
72D1: 61         LD           H,C
72D2: 67         LD           H,A
72D3: 65         LD           H,L
72D4: 21 20 20   LD           HL,$2020
72D7: 54         LD           D,H
72D8: 68         LD           L,B
72D9: 65         LD           H,L
72DA: 20 20      JR           NZ,$72FC
72DC: 20 57      JR           NZ,$7335
72DE: 69         LD           L,C
72DF: 6E         LD           L,(HL)
72E0: 64         LD           H,H
72E1: 20 46      JR           NZ,$7329
72E3: 69         LD           L,C
72E4: 73         LD           (HL),E
72E5: 68         LD           L,B
72E6: 20 77      JR           NZ,$735F
72E8: 61         LD           H,C
72E9: 69         LD           L,C
72EA: 74         LD           (HL),H
72EB: 73         LD           (HL),E
72EC: 20 66      JR           NZ,$7354
72EE: 6F         LD           L,A
72EF: 72         LD           (HL),D
72F0: 20 79      JR           NZ,$736B
72F2: 6F         LD           L,A
72F3: 75         LD           (HL),L
72F4: 21 20 20   LD           HL,$2020
72F7: 48         LD           C,B
72F8: 6F         LD           L,A
72F9: 6F         LD           L,A
72FA: 74         LD           (HL),H
72FB: 21 FF 54   LD           HL,$54FF
72FE: 68         LD           L,B
72FF: 65         LD           H,L
7300: 20 74      JR           NZ,$7376
7302: 69         LD           L,C
7303: 6D         LD           L,L
7304: 65         LD           H,L
7305: 20 68      JR           NZ,$736F
7307: 61         LD           H,C
7308: 73         LD           (HL),E
7309: 20 20      JR           NZ,$732B
730B: 20 20      JR           NZ,$732D
730D: 63         LD           H,E
730E: 6F         LD           L,A
730F: 6D         LD           L,L
7310: 65         LD           H,L
7311: 2E 2E      LD           L,$2E
7313: 2E 20      LD           L,$20
7315: 54         LD           D,H
7316: 68         LD           L,B
7317: 65         LD           H,L
7318: 20 57      JR           NZ,$7371
731A: 69         LD           L,C
731B: 6E         LD           L,(HL)
731C: 64         LD           H,H
731D: 46         LD           B,(HL)
731E: 69         LD           L,C
731F: 73         LD           (HL),E
7320: 68         LD           L,B
7321: 20 61      JR           NZ,$7384
7323: 77         LD           (HL),A
7324: 61         LD           H,C
7325: 69         LD           L,C
7326: 74         LD           (HL),H
7327: 73         LD           (HL),E
7328: 2E 2E      LD           L,$2E
732A: 2E 20      LD           L,$20
732C: 20 45      JR           NZ,$7373
732E: 6E         LD           L,(HL)
732F: 74         LD           (HL),H
7330: 65         LD           H,L
7331: 72         LD           (HL),D
7332: 20 74      JR           NZ,$73A8
7334: 68         LD           L,B
7335: 65         LD           H,L
7336: 20 45      JR           NZ,$737D
7338: 67         LD           H,A
7339: 67         LD           H,A
733A: 2E 2E      LD           L,$2E
733C: 2E 48      LD           L,$48
733E: 6F         LD           L,A
733F: 6F         LD           L,A
7340: 74         LD           (HL),H
7341: 21 20 48   LD           HL,$4820
7344: 6F         LD           L,A
7345: 6F         LD           L,A
7346: 74         LD           (HL),H
7347: 21 FF 48   LD           HL,$48FF
734A: 6F         LD           L,A
734B: 6F         LD           L,A
734C: 74         LD           (HL),H
734D: 21 20 59   LD           HL,$5920
7350: 6F         LD           L,A
7351: 75         LD           (HL),L
7352: 6E         LD           L,(HL)
7353: 67         LD           H,A
7354: 20 6C      JR           NZ,$73C2
7356: 61         LD           H,C
7357: 64         LD           H,H
7358: 2C         INC         L
7359: 49         LD           C,C
735A: 20 6D      JR           NZ,$73C9
735C: 65         LD           H,L
735D: 61         LD           H,C
735E: 6E         LD           L,(HL)
735F: 2E 2E      LD           L,$2E
7361: 2E 20      LD           L,$20
7363: 23         INC         HL
7364: 23         INC         HL
7365: 23         INC         HL
7366: 23         INC         HL
7367: 23         INC         HL
7368: 2C         INC         L
7369: 74         LD           (HL),H
736A: 68         LD           L,B
736B: 65         LD           H,L
736C: 20 68      JR           NZ,$73D6
736E: 65         LD           H,L
736F: 72         LD           (HL),D
7370: 6F         LD           L,A
7371: 21 20 20   LD           HL,$2020
7374: 59         LD           E,C
7375: 6F         LD           L,A
7376: 75         LD           (HL),L
7377: 20 20      JR           NZ,$7399
7379: 68         LD           L,B
737A: 61         LD           H,C
737B: 76         HALT
737C: 65         LD           H,L
737D: 20 64      JR           NZ,$73E3
737F: 65         LD           H,L
7380: 66         LD           H,(HL)
7381: 65         LD           H,L
7382: 61         LD           H,C
7383: 74         LD           (HL),H
7384: 65         LD           H,L
7385: 64         LD           H,H
7386: 20 20      JR           NZ,$73A8
7388: 20 74      JR           NZ,$73FE
738A: 68         LD           L,B
738B: 65         LD           H,L
738C: 20 4E      JR           NZ,$73DC
738E: 69         LD           L,C
738F: 67         LD           H,A
7390: 68         LD           L,B
7391: 74         LD           (HL),H
7392: 6D         LD           L,L
7393: 61         LD           H,C
7394: 72         LD           (HL),D
7395: 65         LD           H,L
7396: 73         LD           (HL),E
7397: 21 20 59   LD           HL,$5920
739A: 6F         LD           L,A
739B: 75         LD           (HL),L
739C: 20 68      JR           NZ,$7406
739E: 61         LD           H,C
739F: 76         HALT
73A0: 65         LD           H,L
73A1: 20 70      JR           NZ,$7413
73A3: 72         LD           (HL),D
73A4: 6F         LD           L,A
73A5: 76         HALT
73A6: 65         LD           H,L
73A7: 6E         LD           L,(HL)
73A8: 20 79      JR           NZ,$7423
73AA: 6F         LD           L,A
73AB: 75         LD           (HL),L
73AC: 72         LD           (HL),D
73AD: 20 77      JR           NZ,$7426
73AF: 69         LD           L,C
73B0: 73         LD           (HL),E
73B1: 64         LD           H,H
73B2: 6F         LD           L,A
73B3: 6D         LD           L,L
73B4: 2C         INC         L
73B5: 20 20      JR           NZ,$73D7
73B7: 20 20      JR           NZ,$73D9
73B9: 63         LD           H,E
73BA: 6F         LD           L,A
73BB: 75         LD           (HL),L
73BC: 72         LD           (HL),D
73BD: 61         LD           H,C
73BE: 67         LD           H,A
73BF: 65         LD           H,L
73C0: 20 61      JR           NZ,$7423
73C2: 6E         LD           L,(HL)
73C3: 64         LD           H,H
73C4: 20 20      JR           NZ,$73E6
73C6: 20 20      JR           NZ,$73E8
73C8: 20 70      JR           NZ,$743A
73CA: 6F         LD           L,A
73CB: 77         LD           (HL),A
73CC: 65         LD           H,L
73CD: 72         LD           (HL),D
73CE: 21 20 20   LD           HL,$2020
73D1: 20 20      JR           NZ,$73F3
73D3: 20 20      JR           NZ,$73F5
73D5: 20 20      JR           NZ,$73F7
73D7: 20 20      JR           NZ,$73F9
73D9: 2E 2E      LD           L,$2E
73DB: 2E 20      LD           L,$20
73DD: 2E 2E      LD           L,$2E
73DF: 2E 20      LD           L,$20
73E1: 2E 2E      LD           L,$2E
73E3: 2E 20      LD           L,$20
73E5: 2E 2E      LD           L,$2E
73E7: 2E 20      LD           L,$20
73E9: 41         LD           B,C
73EA: 73         LD           (HL),E
73EB: 20 70      JR           NZ,$745D
73ED: 61         LD           H,C
73EE: 72         LD           (HL),D
73EF: 74         LD           (HL),H
73F0: 20 6F      JR           NZ,$7461
73F2: 66         LD           H,(HL)
73F3: 20 74      JR           NZ,$7469
73F5: 68         LD           L,B
73F6: 65         LD           H,L
73F7: 20 20      JR           NZ,$7419
73F9: 57         LD           D,A
73FA: 69         LD           L,C
73FB: 6E         LD           L,(HL)
73FC: 64         LD           H,H
73FD: 20 46      JR           NZ,$7445
73FF: 69         LD           L,C
7400: 73         LD           (HL),E
7401: 68         LD           L,B
7402: 5E         LD           E,(HL)
7403: 73         LD           (HL),E
7404: 20 20      JR           NZ,$7426
7406: 20 20      JR           NZ,$7428
7408: 20 73      JR           NZ,$747D
740A: 70         LD           (HL),B
740B: 69         LD           L,C
740C: 72         LD           (HL),D
740D: 69         LD           L,C
740E: 74         LD           (HL),H
740F: 2C         INC         L
7410: 20 49      JR           NZ,$745B
7412: 20 61      JR           NZ,$7475
7414: 6D         LD           L,L
7415: 20 74      JR           NZ,$748B
7417: 68         LD           L,B
7418: 65         LD           H,L
7419: 67         LD           H,A
741A: 75         LD           (HL),L
741B: 61         LD           H,C
741C: 72         LD           (HL),D
741D: 64         LD           H,H
741E: 69         LD           L,C
741F: 61         LD           H,C
7420: 6E         LD           L,(HL)
7421: 20 6F      JR           NZ,$7492
7423: 66         LD           H,(HL)
7424: 20 68      JR           NZ,$748E
7426: 69         LD           L,C
7427: 73         LD           (HL),E
7428: 20 64      JR           NZ,$748E
742A: 72         LD           (HL),D
742B: 65         LD           H,L
742C: 61         LD           H,C
742D: 6D         LD           L,L
742E: 20 77      JR           NZ,$74A7
7430: 6F         LD           L,A
7431: 72         LD           (HL),D
7432: 6C         LD           L,H
7433: 64         LD           H,H
7434: 2E 2E      LD           L,$2E
7436: 2E 20      LD           L,$20
7438: 20 42      JR           NZ,$747C
743A: 75         LD           (HL),L
743B: 74         LD           (HL),H
743C: 20 6F      JR           NZ,$74AD
743E: 6E         LD           L,(HL)
743F: 65         LD           H,L
7440: 20 64      JR           NZ,$74A6
7442: 61         LD           H,C
7443: 79         LD           A,C
7444: 2C         INC         L
7445: 20 74      JR           NZ,$74BB
7447: 68         LD           L,B
7448: 65         LD           H,L
7449: 4E         LD           C,(HL)
744A: 69         LD           L,C
744B: 67         LD           H,A
744C: 68         LD           L,B
744D: 74         LD           (HL),H
744E: 6D         LD           L,L
744F: 61         LD           H,C
7450: 72         LD           (HL),D
7451: 65         LD           H,L
7452: 73         LD           (HL),E
7453: 20 20      JR           NZ,$7475
7455: 20 20      JR           NZ,$7477
7457: 20 20      JR           NZ,$7479
7459: 65         LD           H,L
745A: 6E         LD           L,(HL)
745B: 74         LD           (HL),H
745C: 65         LD           H,L
745D: 72         LD           (HL),D
745E: 65         LD           H,L
745F: 64         LD           H,H
7460: 20 74      JR           NZ,$74D6
7462: 68         LD           L,B
7463: 65         LD           H,L
7464: 20 20      JR           NZ,$7486
7466: 20 20      JR           NZ,$7488
7468: 20 64      JR           NZ,$74CE
746A: 72         LD           (HL),D
746B: 65         LD           H,L
746C: 61         LD           H,C
746D: 6D         LD           L,L
746E: 20 61      JR           NZ,$74D1
7470: 6E         LD           L,(HL)
7471: 64         LD           H,H
7472: 20 62      JR           NZ,$74D6
7474: 65         LD           H,L
7475: 67         LD           H,A
7476: 61         LD           H,C
7477: 6E         LD           L,(HL)
7478: 20 77      JR           NZ,$74F1
747A: 72         LD           (HL),D
747B: 65         LD           H,L
747C: 61         LD           H,C
747D: 6B         LD           L,E
747E: 69         LD           L,C
747F: 6E         LD           L,(HL)
7480: 67         LD           H,A
7481: 20 68      JR           NZ,$74EB
7483: 61         LD           H,C
7484: 76         HALT
7485: 6F         LD           L,A
7486: 63         LD           H,E
7487: 2E 20      LD           L,$20
7489: 54         LD           D,H
748A: 68         LD           L,B
748B: 65         LD           H,L
748C: 6E         LD           L,(HL)
748D: 20 79      JR           NZ,$7508
748F: 6F         LD           L,A
7490: 75         LD           (HL),L
7491: 2C         INC         L
7492: 20 23      JR           NZ,$74B7
7494: 23         INC         HL
7495: 23         INC         HL
7496: 23         INC         HL
7497: 23         INC         HL
7498: 2C         INC         L
7499: 63         LD           H,E
749A: 61         LD           H,C
749B: 6D         LD           L,L
749C: 65         LD           H,L
749D: 20 74      JR           NZ,$7513
749F: 6F         LD           L,A
74A0: 20 72      JR           NZ,$7514
74A2: 65         LD           H,L
74A3: 73         LD           (HL),E
74A4: 63         LD           H,E
74A5: 75         LD           (HL),L
74A6: 65         LD           H,L
74A7: 20 20      JR           NZ,$74C9
74A9: 74         LD           (HL),H
74AA: 68         LD           L,B
74AB: 65         LD           H,L
74AC: 20 69      JR           NZ,$7517
74AE: 73         LD           (HL),E
74AF: 6C         LD           L,H
74B0: 61         LD           H,C
74B1: 6E         LD           L,(HL)
74B2: 64         LD           H,H
74B3: 2E 2E      LD           L,$2E
74B5: 2E 20      LD           L,$20
74B7: 20 20      JR           NZ,$74D9
74B9: 49         LD           C,C
74BA: 20 68      JR           NZ,$7524
74BC: 61         LD           H,C
74BD: 76         HALT
74BE: 65         LD           H,L
74BF: 20 61      JR           NZ,$7522
74C1: 6C         LD           L,H
74C2: 77         LD           (HL),A
74C3: 61         LD           H,C
74C4: 79         LD           A,C
74C5: 73         LD           (HL),E
74C6: 20 20      JR           NZ,$74E8
74C8: 20 74      JR           NZ,$753E
74CA: 72         LD           (HL),D
74CB: 75         LD           (HL),L
74CC: 73         LD           (HL),E
74CD: 74         LD           (HL),H
74CE: 65         LD           H,L
74CF: 64         LD           H,H
74D0: 20 69      JR           NZ,$753B
74D2: 6E         LD           L,(HL)
74D3: 20 79      JR           NZ,$754E
74D5: 6F         LD           L,A
74D6: 75         LD           (HL),L
74D7: 72         LD           (HL),D
74D8: 20 63      JR           NZ,$753D
74DA: 6F         LD           L,A
74DB: 75         LD           (HL),L
74DC: 72         LD           (HL),D
74DD: 61         LD           H,C
74DE: 67         LD           H,A
74DF: 65         LD           H,L
74E0: 20 74      JR           NZ,$7556
74E2: 6F         LD           L,A
74E3: 20 74      JR           NZ,$7559
74E5: 75         LD           (HL),L
74E6: 72         LD           (HL),D
74E7: 6E         LD           L,(HL)
74E8: 20 62      JR           NZ,$754C
74EA: 61         LD           H,C
74EB: 63         LD           H,E
74EC: 6B         LD           L,E
74ED: 20 74      JR           NZ,$7563
74EF: 68         LD           L,B
74F0: 65         LD           H,L
74F1: 20 4E      JR           NZ,$7541
74F3: 69         LD           L,C
74F4: 67         LD           H,A
74F5: 68         LD           L,B
74F6: 74         LD           (HL),H
74F7: 2D         DEC         L
74F8: 20 6D      JR           NZ,$7567
74FA: 61         LD           H,C
74FB: 72         LD           (HL),D
74FC: 65         LD           H,L
74FD: 73         LD           (HL),E
74FE: 2E 20      LD           L,$20
7500: 20 54      JR           NZ,$7556
7502: 68         LD           L,B
7503: 61         LD           H,C
7504: 6E         LD           L,(HL)
7505: 6B         LD           L,E
7506: 20 20      JR           NZ,$7528
7508: 20 79      JR           NZ,$7583
750A: 6F         LD           L,A
750B: 75         LD           (HL),L
750C: 2C         INC         L
750D: 20 23      JR           NZ,$7532
750F: 23         INC         HL
7510: 23         INC         HL
7511: 23         INC         HL
7512: 23         INC         HL
7513: 2E 2E      LD           L,$2E
7515: 2E 20      LD           L,$20
7517: 4D         LD           C,L
7518: 79         LD           A,C
7519: 77         LD           (HL),A
751A: 6F         LD           L,A
751B: 72         LD           (HL),D
751C: 6B         LD           L,E
751D: 20 69      JR           NZ,$7588
751F: 73         LD           (HL),E
7520: 20 64      JR           NZ,$7586
7522: 6F         LD           L,A
7523: 6E         LD           L,(HL)
7524: 65         LD           H,L
7525: 2E 2E      LD           L,$2E
7527: 2E 20      LD           L,$20
7529: 54         LD           D,H
752A: 68         LD           L,B
752B: 65         LD           H,L
752C: 20 57      JR           NZ,$7585
752E: 69         LD           L,C
752F: 6E         LD           L,(HL)
7530: 64         LD           H,H
7531: 20 46      JR           NZ,$7579
7533: 69         LD           L,C
7534: 73         LD           (HL),E
7535: 68         LD           L,B
7536: 20 20      JR           NZ,$7558
7538: 20 77      JR           NZ,$75B1
753A: 69         LD           L,C
753B: 6C         LD           L,H
753C: 6C         LD           L,H
753D: 20 77      JR           NZ,$75B6
753F: 61         LD           H,C
7540: 6B         LD           L,E
7541: 65         LD           H,L
7542: 20 73      JR           NZ,$75B7
7544: 6F         LD           L,A
7545: 6F         LD           L,A
7546: 6E         LD           L,(HL)
7547: 2E 20      LD           L,$20
7549: 47         LD           B,A
754A: 6F         LD           L,A
754B: 6F         LD           L,A
754C: 64         LD           H,H
754D: 20 62      JR           NZ,$75B1
754F: 79         LD           A,C
7550: 65         LD           H,L
7551: 2E 2E      LD           L,$2E
7553: 2E 48      LD           L,$48
7555: 6F         LD           L,A
7556: 6F         LD           L,A
7557: 74         LD           (HL),H
7558: 21 FF 2E   LD           HL,$2EFF
755B: 2E 2E      LD           L,$2E
755D: 20 2E      JR           NZ,$758D
755F: 2E 2E      LD           L,$2E
7561: 20 2E      JR           NZ,$7591
7563: 2E 2E      LD           L,$2E
7565: 20 2E      JR           NZ,$7595
7567: 2E 2E      LD           L,$2E
7569: 20 20      JR           NZ,$758B
756B: 2E 2E      LD           L,$2E
756D: 2E 20      LD           L,$20
756F: 2E 2E      LD           L,$2E
7571: 2E 20      LD           L,$20
7573: 2E 2E      LD           L,$2E
7575: 2E 20      LD           L,$20
7577: 2E 2E      LD           L,$2E
7579: 2E 20      LD           L,$20
757B: 49         LD           C,C
757C: 20 41      JR           NZ,$75BF
757E: 4D         LD           C,L
757F: 20 54      JR           NZ,$75D5
7581: 48         LD           C,B
7582: 45         LD           B,L
7583: 20 57      JR           NZ,$75DC
7585: 49         LD           C,C
7586: 4E         LD           C,(HL)
7587: 44         LD           B,H
7588: 20 20      JR           NZ,$75AA
758A: 20 20      JR           NZ,$75AC
758C: 20 20      JR           NZ,$75AE
758E: 20 20      JR           NZ,$75B0
7590: 46         LD           B,(HL)
7591: 49         LD           C,C
7592: 53         LD           D,E
7593: 48         LD           C,B
7594: 2E 2E      LD           L,$2E
7596: 2E 20      LD           L,$20
7598: 20 20      JR           NZ,$75BA
759A: 20 4C      JR           NZ,$75E8
759C: 4F         LD           C,A
759D: 4E         LD           C,(HL)
759E: 47         LD           B,A
759F: 20 48      JR           NZ,$75E9
75A1: 41         LD           B,C
75A2: 53         LD           D,E
75A3: 20 42      JR           NZ,$75E7
75A5: 45         LD           B,L
75A6: 45         LD           B,L
75A7: 4E         LD           C,(HL)
75A8: 20 20      JR           NZ,$75CA
75AA: 20 20      JR           NZ,$75CC
75AC: 4D         LD           C,L
75AD: 59         LD           E,C
75AE: 20 53      JR           NZ,$7603
75B0: 4C         LD           C,H
75B1: 55         LD           D,L
75B2: 4D         LD           C,L
75B3: 42         LD           B,D
75B4: 45         LD           B,L
75B5: 52         LD           D,D
75B6: 2E 2E      LD           L,$2E
75B8: 2E 20      LD           L,$20
75BA: 20 49      JR           NZ,$7605
75BC: 4E         LD           C,(HL)
75BD: 20 4D      JR           NZ,$760C
75BF: 59         LD           E,C
75C0: 20 44      JR           NZ,$7606
75C2: 52         LD           D,D
75C3: 45         LD           B,L
75C4: 41         LD           B,C
75C5: 4D         LD           C,L
75C6: 53         LD           D,E
75C7: 2E 2E      LD           L,$2E
75C9: 2E 20      LD           L,$20
75CB: 41         LD           B,C
75CC: 4E         LD           C,(HL)
75CD: 20 45      JR           NZ,$7614
75CF: 47         LD           B,A
75D0: 47         LD           B,A
75D1: 20 41      JR           NZ,$7614
75D3: 50         LD           D,B
75D4: 50         LD           D,B
75D5: 45         LD           B,L
75D6: 41         LD           B,C
75D7: 52         LD           D,D
75D8: 45         LD           B,L
75D9: 44         LD           B,H
75DA: 20 20      JR           NZ,$75FC
75DC: 20 20      JR           NZ,$75FE
75DE: 20 41      JR           NZ,$7621
75E0: 4E         LD           C,(HL)
75E1: 44         LD           B,H
75E2: 20 57      JR           NZ,$763B
75E4: 41         LD           B,C
75E5: 53         LD           D,E
75E6: 20 20      JR           NZ,$7608
75E8: 20 20      JR           NZ,$760A
75EA: 53         LD           D,E
75EB: 55         LD           D,L
75EC: 52         LD           D,D
75ED: 52         LD           D,D
75EE: 4F         LD           C,A
75EF: 55         LD           D,L
75F0: 4E         LD           C,(HL)
75F1: 44         LD           B,H
75F2: 45         LD           B,L
75F3: 44         LD           B,H
75F4: 20 42      JR           NZ,$7638
75F6: 59         LD           E,C
75F7: 20 41      JR           NZ,$763A
75F9: 4E         LD           C,(HL)
75FA: 20 20      JR           NZ,$761C
75FC: 49         LD           C,C
75FD: 53         LD           D,E
75FE: 4C         LD           C,H
75FF: 41         LD           B,C
7600: 4E         LD           C,(HL)
7601: 44         LD           B,H
7602: 2C         INC         L
7603: 20 57      JR           NZ,$765C
7605: 49         LD           C,C
7606: 54         LD           D,H
7607: 48         LD           C,B
7608: 20 20      JR           NZ,$762A
760A: 50         LD           D,B
760B: 45         LD           B,L
760C: 4F         LD           C,A
760D: 50         LD           D,B
760E: 4C         LD           C,H
760F: 45         LD           B,L
7610: 2C         INC         L
7611: 20 41      JR           NZ,$7654
7613: 4E         LD           C,(HL)
7614: 49         LD           C,C
7615: 4D         LD           C,L
7616: 41         LD           B,C
7617: 4C         LD           C,H
7618: 53         LD           D,E
7619: 2C         INC         L
761A: 41         LD           B,C
761B: 4E         LD           C,(HL)
761C: 20 45      JR           NZ,$7663
761E: 4E         LD           C,(HL)
761F: 54         LD           D,H
7620: 49         LD           C,C
7621: 52         LD           D,D
7622: 45         LD           B,L
7623: 20 57      JR           NZ,$767C
7625: 4F         LD           C,A
7626: 52         LD           D,D
7627: 4C         LD           C,H
7628: 44         LD           B,H
7629: 21 2E 2E   LD           HL,$2E2E
762C: 2E 20      LD           L,$20
762E: 2E 2E      LD           L,$2E
7630: 2E 20      LD           L,$20
7632: 2E 2E      LD           L,$2E
7634: 2E 20      LD           L,$20
7636: 2E 2E      LD           L,$2E
7638: 2E 20      LD           L,$20
763A: 20 20      JR           NZ,$765C
763C: 42         LD           B,D
763D: 55         LD           D,L
763E: 54         LD           D,H
763F: 2C         INC         L
7640: 20 56      JR           NZ,$7698
7642: 45         LD           B,L
7643: 52         LD           D,D
7644: 49         LD           C,C
7645: 4C         LD           C,H
7646: 59         LD           E,C
7647: 2C         INC         L
7648: 20 20      JR           NZ,$766A
764A: 49         LD           C,C
764B: 54         LD           D,H
764C: 20 42      JR           NZ,$7690
764E: 45         LD           B,L
764F: 20 54      JR           NZ,$76A5
7651: 48         LD           C,B
7652: 45         LD           B,L
7653: 20 4E      JR           NZ,$76A3
7655: 41         LD           B,C
7656: 54         LD           D,H
7657: 55         LD           D,L
7658: 52         LD           D,D
7659: 45         LD           B,L
765A: 20 20      JR           NZ,$767C
765C: 4F         LD           C,A
765D: 46         LD           B,(HL)
765E: 20 44      JR           NZ,$76A4
7660: 52         LD           D,D
7661: 45         LD           B,L
7662: 41         LD           B,C
7663: 4D         LD           C,L
7664: 53         LD           D,E
7665: 20 54      JR           NZ,$76BB
7667: 4F         LD           C,A
7668: 20 20      JR           NZ,$768A
766A: 45         LD           B,L
766B: 4E         LD           C,(HL)
766C: 44         LD           B,H
766D: 21 20 57   LD           HL,$5720
7670: 48         LD           C,B
7671: 45         LD           B,L
7672: 4E         LD           C,(HL)
7673: 20 49      JR           NZ,$76BE
7675: 20 44      JR           NZ,$76BB
7677: 4F         LD           C,A
7678: 53         LD           D,E
7679: 54         LD           D,H
767A: 41         LD           B,C
767B: 57         LD           D,A
767C: 41         LD           B,C
767D: 4B         LD           C,E
767E: 45         LD           B,L
767F: 4E         LD           C,(HL)
7680: 2C         INC         L
7681: 20 4B      JR           NZ,$76CE
7683: 4F         LD           C,A
7684: 48         LD           C,B
7685: 4F         LD           C,A
7686: 4C         LD           C,H
7687: 49         LD           C,C
7688: 4E         LD           C,(HL)
7689: 54         LD           D,H
768A: 20 57      JR           NZ,$76E3
768C: 49         LD           C,C
768D: 4C         LD           C,H
768E: 4C         LD           C,H
768F: 20 42      JR           NZ,$76D3
7691: 45         LD           B,L
7692: 20 47      JR           NZ,$76DB
7694: 4F         LD           C,A
7695: 4E         LD           C,(HL)
7696: 45         LD           B,L
7697: 2E 2E      LD           L,$2E
7699: 2E 4F      LD           L,$4F
769B: 4E         LD           C,(HL)
769C: 4C         LD           C,H
769D: 59         LD           E,C
769E: 20 54      JR           NZ,$76F4
76A0: 48         LD           C,B
76A1: 45         LD           B,L
76A2: 20 4D      JR           NZ,$76F1
76A4: 45         LD           B,L
76A5: 4D         LD           C,L
76A6: 4F         LD           C,A
76A7: 52         LD           D,D
76A8: 59         LD           E,C
76A9: 20 20      JR           NZ,$76CB
76AB: 4F         LD           C,A
76AC: 46         LD           B,(HL)
76AD: 20 54      JR           NZ,$7703
76AF: 48         LD           C,B
76B0: 49         LD           C,C
76B1: 53         LD           D,E
76B2: 20 44      JR           NZ,$76F8
76B4: 52         LD           D,D
76B5: 45         LD           B,L
76B6: 41         LD           B,C
76B7: 4D         LD           C,L
76B8: 20 20      JR           NZ,$76DA
76BA: 4C         LD           C,H
76BB: 41         LD           B,C
76BC: 4E         LD           C,(HL)
76BD: 44         LD           B,H
76BE: 20 57      JR           NZ,$7717
76C0: 49         LD           C,C
76C1: 4C         LD           C,H
76C2: 4C         LD           C,H
76C3: 20 45      JR           NZ,$770A
76C5: 58         LD           E,B
76C6: 49         LD           C,C
76C7: 53         LD           D,E
76C8: 54         LD           D,H
76C9: 20 20      JR           NZ,$76EB
76CB: 20 49      JR           NZ,$7716
76CD: 4E         LD           C,(HL)
76CE: 20 54      JR           NZ,$7724
76D0: 48         LD           C,B
76D1: 45         LD           B,L
76D2: 20 57      JR           NZ,$772B
76D4: 41         LD           B,C
76D5: 4B         LD           C,E
76D6: 49         LD           C,C
76D7: 4E         LD           C,(HL)
76D8: 47         LD           B,A
76D9: 20 20      JR           NZ,$76FB
76DB: 20 20      JR           NZ,$76FD
76DD: 20 20      JR           NZ,$76FF
76DF: 20 57      JR           NZ,$7738
76E1: 4F         LD           C,A
76E2: 52         LD           D,D
76E3: 4C         LD           C,H
76E4: 44         LD           B,H
76E5: 2E 2E      LD           L,$2E
76E7: 2E 20      LD           L,$20
76E9: 20 20      JR           NZ,$770B
76EB: 53         LD           D,E
76EC: 4F         LD           C,A
76ED: 4D         LD           C,L
76EE: 45         LD           B,L
76EF: 44         LD           B,H
76F0: 41         LD           B,C
76F1: 59         LD           E,C
76F2: 2C         INC         L
76F3: 20 54      JR           NZ,$7749
76F5: 48         LD           C,B
76F6: 4F         LD           C,A
76F7: 55         LD           D,L
76F8: 20 20      JR           NZ,$771A
76FA: 4D         LD           C,L
76FB: 41         LD           B,C
76FC: 59         LD           E,C
76FD: 20 52      JR           NZ,$7751
76FF: 45         LD           B,L
7700: 43         LD           B,E
7701: 41         LD           B,C
7702: 4C         LD           C,H
7703: 4C         LD           C,H
7704: 20 54      JR           NZ,$775A
7706: 48         LD           C,B
7707: 49         LD           C,C
7708: 53         LD           D,E
7709: 20 20      JR           NZ,$772B
770B: 49         LD           C,C
770C: 53         LD           D,E
770D: 4C         LD           C,H
770E: 41         LD           B,C
770F: 4E         LD           C,(HL)
7710: 44         LD           B,H
7711: 2E 2E      LD           L,$2E
7713: 2E 20      LD           L,$20
7715: 20 54      JR           NZ,$776B
7717: 48         LD           C,B
7718: 41         LD           B,C
7719: 54         LD           D,H
771A: 20 4D      JR           NZ,$7769
771C: 45         LD           B,L
771D: 4D         LD           C,L
771E: 4F         LD           C,A
771F: 52         LD           D,D
7720: 59         LD           E,C
7721: 20 4D      JR           NZ,$7770
7723: 55         LD           D,L
7724: 53         LD           D,E
7725: 54         LD           D,H
7726: 20 42      JR           NZ,$776A
7728: 45         LD           B,L
7729: 20 20      JR           NZ,$774B
772B: 54         LD           D,H
772C: 48         LD           C,B
772D: 45         LD           B,L
772E: 20 52      JR           NZ,$7782
7730: 45         LD           B,L
7731: 41         LD           B,C
7732: 4C         LD           C,H
7733: 20 44      JR           NZ,$7779
7735: 52         LD           D,D
7736: 45         LD           B,L
7737: 41         LD           B,C
7738: 4D         LD           C,L
7739: 20 20      JR           NZ,$775B
773B: 20 20      JR           NZ,$775D
773D: 20 20      JR           NZ,$775F
773F: 57         LD           D,A
7740: 4F         LD           C,A
7741: 52         LD           D,D
7742: 4C         LD           C,H
7743: 44         LD           B,H
7744: 2E 2E      LD           L,$2E
7746: 2E 20      LD           L,$20
7748: 20 20      JR           NZ,$776A
774A: 2E 2E      LD           L,$2E
774C: 2E 20      LD           L,$20
774E: 2E 2E      LD           L,$2E
7750: 2E 20      LD           L,$20
7752: 2E 2E      LD           L,$2E
7754: 2E 20      LD           L,$20
7756: 2E 2E      LD           L,$2E
7758: 2E 20      LD           L,$20
775A: 20 43      JR           NZ,$779F
775C: 4F         LD           C,A
775D: 4D         LD           C,L
775E: 45         LD           B,L
775F: 2C         INC         L
7760: 20 23      JR           NZ,$7785
7762: 23         INC         HL
7763: 23         INC         HL
7764: 23         INC         HL
7765: 23         INC         HL
7766: 2E 2E      LD           L,$2E
7768: 2E 20      LD           L,$20
776A: 4C         LD           C,H
776B: 45         LD           B,L
776C: 54         LD           D,H
776D: 20 55      JR           NZ,$77C4
776F: 53         LD           D,E
7770: 20 41      JR           NZ,$77B3
7772: 57         LD           D,A
7773: 41         LD           B,C
7774: 4B         LD           C,E
7775: 45         LD           B,L
7776: 4E         LD           C,(HL)
7777: 2E 2E      LD           L,$2E
7779: 2E 20      LD           L,$20
777B: 20 20      JR           NZ,$779D
777D: 54         LD           D,H
777E: 4F         LD           C,A
777F: 47         LD           B,A
7780: 45         LD           B,L
7781: 54         LD           D,H
7782: 48         LD           C,B
7783: 45         LD           B,L
7784: 52         LD           D,D
7785: 21 21 FF   LD           HL,$FF21
7788: 20 50      JR           NZ,$77DA
778A: 4C         LD           C,H
778B: 41         LD           B,C
778C: 59         LD           E,C
778D: 20 54      JR           NZ,$77E3
778F: 48         LD           C,B
7790: 45         LD           B,L
7791: 20 45      JR           NZ,$77D8
7793: 49         LD           C,C
7794: 47         LD           B,A
7795: 48         LD           C,B
7796: 54         LD           D,H
7797: 20 20      JR           NZ,$77B9
7799: 20 49      JR           NZ,$77E4
779B: 4E         LD           C,(HL)
779C: 53         LD           D,E
779D: 54         LD           D,H
779E: 52         LD           D,D
779F: 55         LD           D,L
77A0: 4D         LD           C,L
77A1: 45         LD           B,L
77A2: 4E         LD           C,(HL)
77A3: 54         LD           D,H
77A4: 53         LD           D,E
77A5: 21 20 20   LD           HL,$2020
77A8: 50         LD           D,B
77A9: 4C         LD           C,H
77AA: 41         LD           B,C
77AB: 59         LD           E,C
77AC: 20 54      JR           NZ,$7802
77AE: 48         LD           C,B
77AF: 45         LD           B,L
77B0: 20 53      JR           NZ,$7805
77B2: 4F         LD           C,A
77B3: 4E         LD           C,(HL)
77B4: 47         LD           B,A
77B5: 20 4F      JR           NZ,$7806
77B7: 46         LD           B,(HL)
77B8: 20 20      JR           NZ,$77DA
77BA: 20 41      JR           NZ,$77FD
77BC: 57         LD           D,A
77BD: 41         LD           B,C
77BE: 4B         LD           C,E
77BF: 45         LD           B,L
77C0: 4E         LD           C,(HL)
77C1: 49         LD           C,C
77C2: 4E         LD           C,(HL)
77C3: 47         LD           B,A
77C4: 21 21 FF   LD           HL,$FF21
77C7: 4D         LD           C,L
77C8: 65         LD           H,L
77C9: 72         LD           (HL),D
77CA: 6D         LD           L,L
77CB: 61         LD           H,C
77CC: 69         LD           L,C
77CD: 64         LD           H,H
77CE: 20 53      JR           NZ,$7823
77D0: 74         LD           (HL),H
77D1: 61         LD           H,C
77D2: 74         LD           (HL),H
77D3: 75         LD           (HL),L
77D4: 65         LD           H,L
77D5: 20 20      JR           NZ,$77F7
77D7: FF         RST         0X38
77D8: 2E 2E      LD           L,$2E
77DA: 2E 23      LD           L,$23
77DC: 23         INC         HL
77DD: 23         INC         HL
77DE: 23         INC         HL
77DF: 23         INC         HL
77E0: 2C         INC         L
77E1: 20 79      JR           NZ,$785C
77E3: 6F         LD           L,A
77E4: 75         LD           (HL),L
77E5: 20 20      JR           NZ,$7807
77E7: 20 68      JR           NZ,$7851
77E9: 61         LD           H,C
77EA: 76         HALT
77EB: 65         LD           H,L
77EC: 20 62      JR           NZ,$7850
77EE: 65         LD           H,L
77EF: 61         LD           H,C
77F0: 74         LD           (HL),H
77F1: 65         LD           H,L
77F2: 6E         LD           L,(HL)
77F3: 20 61      JR           NZ,$7856
77F5: 6C         LD           L,H
77F6: 6C         LD           L,H
77F7: 20 74      JR           NZ,$786D
77F9: 68         LD           L,B
77FA: 65         LD           H,L
77FB: 20 4E      JR           NZ,$784B
77FD: 69         LD           L,C
77FE: 67         LD           H,A
77FF: 68         LD           L,B
7800: 74         LD           (HL),H
7801: 6D         LD           L,L
7802: 61         LD           H,C
7803: 72         LD           (HL),D
7804: 65         LD           H,L
7805: 73         LD           (HL),E
7806: 21 20 43   LD           HL,$4320
7809: 6C         LD           L,H
780A: 69         LD           L,C
780B: 6D         LD           L,L
780C: 62         LD           H,D
780D: 20 74      JR           NZ,$7883
780F: 68         LD           L,B
7810: 65         LD           H,L
7811: 20 73      JR           NZ,$7886
7813: 74         LD           (HL),H
7814: 61         LD           H,C
7815: 69         LD           L,C
7816: 72         LD           (HL),D
7817: 73         LD           (HL),E
7818: 62         LD           H,D
7819: 65         LD           H,L
781A: 66         LD           H,(HL)
781B: 6F         LD           L,A
781C: 72         LD           (HL),D
781D: 65         LD           H,L
781E: 20 79      JR           NZ,$7899
7820: 6F         LD           L,A
7821: 75         LD           (HL),L
7822: 21 FF 41   LD           HL,$41FF
7825: 63         LD           H,E
7826: 68         LD           L,B
7827: 21 20 56   LD           HL,$5620
782A: 61         LD           H,C
782B: 74         LD           (HL),H
782C: 20 61      JR           NZ,$788F
782E: 72         LD           (HL),D
782F: 65         LD           H,L
7830: 20 79      JR           NZ,$78AB
7832: 6F         LD           L,A
7833: 75         LD           (HL),L
7834: 6C         LD           L,H
7835: 6F         LD           L,A
7836: 6F         LD           L,A
7837: 6B         LD           L,E
7838: 69         LD           L,C
7839: 6E         LD           L,(HL)
783A: 67         LD           H,A
783B: 20 61      JR           NZ,$789E
783D: 74         LD           (HL),H
783E: 20 76      JR           NZ,$78B6
7840: 69         LD           L,C
7841: 74         LD           (HL),H
7842: 68         LD           L,B
7843: 20 7A      JR           NZ,$78BF
7845: 61         LD           H,C
7846: 74         LD           (HL),H
7847: 20 6D      JR           NZ,$78B6
7849: 61         LD           H,C
784A: 67         LD           H,A
784B: 6E         LD           L,(HL)
784C: 69         LD           L,C
784D: 66         LD           H,(HL)
784E: 79         LD           A,C
784F: 69         LD           L,C
7850: 6E         LD           L,(HL)
7851: 67         LD           H,A
7852: 20 20      JR           NZ,$7874
7854: 6C         LD           L,H
7855: 65         LD           H,L
7856: 6E         LD           L,(HL)
7857: 73         LD           (HL),E
7858: 3F         CCF
7859: 20 20      JR           NZ,$787B
785B: 53         LD           D,E
785C: 74         LD           (HL),H
785D: 6F         LD           L,A
785E: 70         LD           (HL),B
785F: 20 69      JR           NZ,$78CA
7861: 74         LD           (HL),H
7862: 20 20      JR           NZ,$7884
7864: 61         LD           H,C
7865: 74         LD           (HL),H
7866: 20 76      JR           NZ,$78DE
7868: 6F         LD           L,A
7869: 6E         LD           L,(HL)
786A: 63         LD           H,E
786B: 65         LD           H,L
786C: 21 FF 20   LD           HL,$20FF
786F: 20 48      JR           NZ,$78B9
7871: 6F         LD           L,A
7872: 6F         LD           L,A
7873: 74         LD           (HL),H
7874: 21 20 20   LD           HL,$2020
7877: 48         LD           C,B
7878: 6F         LD           L,A
7879: 6F         LD           L,A
787A: 74         LD           (HL),H
787B: 21 20 20   LD           HL,$2020
787E: 53         LD           D,E
787F: 6F         LD           L,A
7880: 20 79      JR           NZ,$78FB
7882: 6F         LD           L,A
7883: 75         LD           (HL),L
7884: 20 61      JR           NZ,$78E7
7886: 72         LD           (HL),D
7887: 65         LD           H,L
7888: 20 74      JR           NZ,$78FE
788A: 68         LD           L,B
788B: 65         LD           H,L
788C: 20 20      JR           NZ,$78AE
788E: 6C         LD           L,H
788F: 61         LD           H,C
7890: 64         LD           H,H
7891: 20 77      JR           NZ,$790A
7893: 68         LD           L,B
7894: 6F         LD           L,A
7895: 20 6F      JR           NZ,$7906
7897: 77         LD           (HL),A
7898: 6E         LD           L,(HL)
7899: 73         LD           (HL),E
789A: 20 74      JR           NZ,$7910
789C: 68         LD           L,B
789D: 65         LD           H,L
789E: 73         LD           (HL),E
789F: 77         LD           (HL),A
78A0: 6F         LD           L,A
78A1: 72         LD           (HL),D
78A2: 64         LD           H,H
78A3: 2E 2E      LD           L,$2E
78A5: 2E 20      LD           L,$20
78A7: 20 4E      JR           NZ,$78F7
78A9: 6F         LD           L,A
78AA: 77         LD           (HL),A
78AB: 20 49      JR           NZ,$78F6
78AD: 20 75      JR           NZ,$7924
78AF: 6E         LD           L,(HL)
78B0: 64         LD           H,H
78B1: 65         LD           H,L
78B2: 72         LD           (HL),D
78B3: 73         LD           (HL),E
78B4: 74         LD           (HL),H
78B5: 61         LD           H,C
78B6: 6E         LD           L,(HL)
78B7: 64         LD           H,H
78B8: 20 77      JR           NZ,$7931
78BA: 68         LD           L,B
78BB: 79         LD           A,C
78BC: 20 20      JR           NZ,$78DE
78BE: 74         LD           (HL),H
78BF: 68         LD           L,B
78C0: 65         LD           H,L
78C1: 20 6D      JR           NZ,$7930
78C3: 6F         LD           L,A
78C4: 6E         LD           L,(HL)
78C5: 73         LD           (HL),E
78C6: 74         LD           (HL),H
78C7: 65         LD           H,L
78C8: 72         LD           (HL),D
78C9: 73         LD           (HL),E
78CA: 20 61      JR           NZ,$792D
78CC: 72         LD           (HL),D
78CD: 65         LD           H,L
78CE: 73         LD           (HL),E
78CF: 74         LD           (HL),H
78D0: 61         LD           H,C
78D1: 72         LD           (HL),D
78D2: 74         LD           (HL),H
78D3: 69         LD           L,C
78D4: 6E         LD           L,(HL)
78D5: 67         LD           H,A
78D6: 20 74      JR           NZ,$794C
78D8: 6F         LD           L,A
78D9: 20 61      JR           NZ,$793C
78DB: 63         LD           H,E
78DC: 74         LD           (HL),H
78DD: 20 73      JR           NZ,$7952
78DF: 6F         LD           L,A
78E0: 20 76      JR           NZ,$7958
78E2: 69         LD           L,C
78E3: 6F         LD           L,A
78E4: 6C         LD           L,H
78E5: 65         LD           H,L
78E6: 6E         LD           L,(HL)
78E7: 74         LD           (HL),H
78E8: 6C         LD           L,H
78E9: 79         LD           A,C
78EA: 2E 2E      LD           L,$2E
78EC: 2E 20      LD           L,$20
78EE: 41         LD           B,C
78EF: 20 63      JR           NZ,$7954
78F1: 6F         LD           L,A
78F2: 75         LD           (HL),L
78F3: 72         LD           (HL),D
78F4: 61         LD           H,C
78F5: 67         LD           H,A
78F6: 65         LD           H,L
78F7: 6F         LD           L,A
78F8: 75         LD           (HL),L
78F9: 73         LD           (HL),E
78FA: 20 6C      JR           NZ,$7968
78FC: 61         LD           H,C
78FD: 64         LD           H,H
78FE: 68         LD           L,B
78FF: 61         LD           H,C
7900: 73         LD           (HL),E
7901: 20 63      JR           NZ,$7966
7903: 6F         LD           L,A
7904: 6D         LD           L,L
7905: 65         LD           H,L
7906: 20 74      JR           NZ,$797C
7908: 6F         LD           L,A
7909: 20 77      JR           NZ,$7982
790B: 61         LD           H,C
790C: 6B         LD           L,E
790D: 65         LD           H,L
790E: 74         LD           (HL),H
790F: 68         LD           L,B
7910: 65         LD           H,L
7911: 20 57      JR           NZ,$796A
7913: 69         LD           L,C
7914: 6E         LD           L,(HL)
7915: 64         LD           H,H
7916: 20 46      JR           NZ,$795E
7918: 69         LD           L,C
7919: 73         LD           (HL),E
791A: 68         LD           L,B
791B: 2E 2E      LD           L,$2E
791D: 2E 49      LD           L,$49
791F: 74         LD           (HL),H
7920: 20 69      JR           NZ,$798B
7922: 73         LD           (HL),E
7923: 20 73      JR           NZ,$7998
7925: 61         LD           H,C
7926: 69         LD           L,C
7927: 64         LD           H,H
7928: 20 74      JR           NZ,$799E
792A: 68         LD           L,B
792B: 61         LD           H,C
792C: 74         LD           (HL),H
792D: 20 79      JR           NZ,$79A8
792F: 6F         LD           L,A
7930: 75         LD           (HL),L
7931: 20 63      JR           NZ,$7996
7933: 61         LD           H,C
7934: 6E         LD           L,(HL)
7935: 6E         LD           L,(HL)
7936: 6F         LD           L,A
7937: 74         LD           (HL),H
7938: 20 6C      JR           NZ,$79A6
793A: 65         LD           H,L
793B: 61         LD           H,C
793C: 76         HALT
793D: 65         LD           H,L
793E: 74         LD           (HL),H
793F: 68         LD           L,B
7940: 65         LD           H,L
7941: 20 69      JR           NZ,$79AC
7943: 73         LD           (HL),E
7944: 6C         LD           L,H
7945: 61         LD           H,C
7946: 6E         LD           L,(HL)
7947: 64         LD           H,H
7948: 20 20      JR           NZ,$796A
794A: 20 20      JR           NZ,$796C
794C: 20 20      JR           NZ,$796E
794E: 75         LD           (HL),L
794F: 6E         LD           L,(HL)
7950: 6C         LD           L,H
7951: 65         LD           H,L
7952: 73         LD           (HL),E
7953: 73         LD           (HL),E
7954: 20 79      JR           NZ,$79CF
7956: 6F         LD           L,A
7957: 75         LD           (HL),L
7958: 20 77      JR           NZ,$79D1
795A: 61         LD           H,C
795B: 6B         LD           L,E
795C: 65         LD           H,L
795D: 20 74      JR           NZ,$79D3
795F: 68         LD           L,B
7960: 65         LD           H,L
7961: 20 57      JR           NZ,$79BA
7963: 69         LD           L,C
7964: 6E         LD           L,(HL)
7965: 64         LD           H,H
7966: 20 46      JR           NZ,$79AE
7968: 69         LD           L,C
7969: 73         LD           (HL),E
796A: 68         LD           L,B
796B: 2E 2E      LD           L,$2E
796D: 2E 59      LD           L,$59
796F: 6F         LD           L,A
7970: 75         LD           (HL),L
7971: 20 73      JR           NZ,$79E6
7973: 68         LD           L,B
7974: 6F         LD           L,A
7975: 75         LD           (HL),L
7976: 6C         LD           L,H
7977: 64         LD           H,H
7978: 20 6E      JR           NZ,$79E8
797A: 6F         LD           L,A
797B: 77         LD           (HL),A
797C: 20 20      JR           NZ,$799E
797E: 67         LD           H,A
797F: 6F         LD           L,A
7980: 20 6E      JR           NZ,$79F0
7982: 6F         LD           L,A
7983: 72         LD           (HL),D
7984: 74         LD           (HL),H
7985: 68         LD           L,B
7986: 2C         INC         L
7987: 20 74      JR           NZ,$79FD
7989: 6F         LD           L,A
798A: 20 74      JR           NZ,$7A00
798C: 68         LD           L,B
798D: 65         LD           H,L
798E: 4D         LD           C,L
798F: 79         LD           A,C
7990: 73         LD           (HL),E
7991: 74         LD           (HL),H
7992: 65         LD           H,L
7993: 72         LD           (HL),D
7994: 69         LD           L,C
7995: 6F         LD           L,A
7996: 75         LD           (HL),L
7997: 73         LD           (HL),E
7998: 20 20      JR           NZ,$79BA
799A: 20 20      JR           NZ,$79BC
799C: 20 20      JR           NZ,$79BE
799E: 46         LD           B,(HL)
799F: 6F         LD           L,A
79A0: 72         LD           (HL),D
79A1: 65         LD           H,L
79A2: 73         LD           (HL),E
79A3: 74         LD           (HL),H
79A4: 2E 20      LD           L,$20
79A6: 20 49      JR           NZ,$79F1
79A8: 20 77      JR           NZ,$7A21
79AA: 69         LD           L,C
79AB: 6C         LD           L,H
79AC: 6C         LD           L,H
79AD: 20 77      JR           NZ,$7A26
79AF: 61         LD           H,C
79B0: 69         LD           L,C
79B1: 74         LD           (HL),H
79B2: 20 66      JR           NZ,$7A1A
79B4: 6F         LD           L,A
79B5: 72         LD           (HL),D
79B6: 20 79      JR           NZ,$7A31
79B8: 6F         LD           L,A
79B9: 75         LD           (HL),L
79BA: 20 20      JR           NZ,$79DC
79BC: 20 20      JR           NZ,$79DE
79BE: 74         LD           (HL),H
79BF: 68         LD           L,B
79C0: 65         LD           H,L
79C1: 72         LD           (HL),D
79C2: 65         LD           H,L
79C3: 21 20 20   LD           HL,$2020
79C6: 48         LD           C,B
79C7: 6F         LD           L,A
79C8: 6F         LD           L,A
79C9: 74         LD           (HL),H
79CA: 21 FF 41   LD           HL,$41FF
79CD: 6E         LD           L,(HL)
79CE: 6E         LD           L,(HL)
79CF: 6F         LD           L,A
79D0: 79         LD           A,C
79D1: 61         LD           H,C
79D2: 6E         LD           L,(HL)
79D3: 63         LD           H,E
79D4: 65         LD           H,L
79D5: 21 20 20   LD           HL,$2020
79D8: 59         LD           E,C
79D9: 6F         LD           L,A
79DA: 75         LD           (HL),L
79DB: 20 61      JR           NZ,$7A3E
79DD: 72         LD           (HL),D
79DE: 65         LD           H,L
79DF: 20 6F      JR           NZ,$7A50
79E1: 6E         LD           L,(HL)
79E2: 6C         LD           L,H
79E3: 79         LD           A,C
79E4: 20 67      JR           NZ,$7A4D
79E6: 65         LD           H,L
79E7: 74         LD           (HL),H
79E8: 74         LD           (HL),H
79E9: 69         LD           L,C
79EA: 6E         LD           L,(HL)
79EB: 67         LD           H,A
79EC: 69         LD           L,C
79ED: 6E         LD           L,(HL)
79EE: 20 74      JR           NZ,$7A64
79F0: 68         LD           L,B
79F1: 65         LD           H,L
79F2: 20 77      JR           NZ,$7A6B
79F4: 61         LD           H,C
79F5: 79         LD           A,C
79F6: 21 FF 52   LD           HL,$52FF
79F9: 69         LD           L,C
79FA: 62         LD           H,D
79FB: 62         LD           H,D
79FC: 69         LD           L,C
79FD: 74         LD           (HL),H
79FE: 21 20 20   LD           HL,$2020
7A01: 52         LD           D,D
7A02: 69         LD           L,C
7A03: 62         LD           H,D
7A04: 62         LD           H,D
7A05: 69         LD           L,C
7A06: 74         LD           (HL),H
7A07: 21 48 65   LD           HL,$6548
7A0A: 79         LD           A,C
7A0B: 2C         INC         L
7A0C: 20 6D      JR           NZ,$7A7B
7A0E: 61         LD           H,C
7A0F: 6E         LD           L,(HL)
7A10: 2C         INC         L
7A11: 20 49      JR           NZ,$7A5C
7A13: 5E         LD           E,(HL)
7A14: 6D         LD           L,L
7A15: 20 20      JR           NZ,$7A37
7A17: 20 4D      JR           NZ,$7A66
7A19: 61         LD           H,C
7A1A: 6D         LD           L,L
7A1B: 75         LD           (HL),L
7A1C: 2C         INC         L
7A1D: 20 6F      JR           NZ,$7A8E
7A1F: 6E         LD           L,(HL)
7A20: 20 76      JR           NZ,$7A98
7A22: 6F         LD           L,A
7A23: 63         LD           H,E
7A24: 61         LD           H,C
7A25: 6C         LD           L,H
7A26: 73         LD           (HL),E
7A27: 21 42 72   LD           HL,$7242
7A2A: 6F         LD           L,A
7A2B: 74         LD           (HL),H
7A2C: 68         LD           L,B
7A2D: 65         LD           H,L
7A2E: 72         LD           (HL),D
7A2F: 2C         INC         L
7A30: 20 79      JR           NZ,$7AAB
7A32: 6F         LD           L,A
7A33: 75         LD           (HL),L
7A34: 20 20      JR           NZ,$7A56
7A36: 20 20      JR           NZ,$7A58
7A38: 6C         LD           L,H
7A39: 6F         LD           L,A
7A3A: 6F         LD           L,A
7A3B: 6B         LD           L,E
7A3C: 20 6C      JR           NZ,$7AAA
7A3E: 69         LD           L,C
7A3F: 6B         LD           L,E
7A40: 65         LD           H,L
7A41: 20 79      JR           NZ,$7ABC
7A43: 6F         LD           L,A
7A44: 75         LD           (HL),L
7A45: 20 20      JR           NZ,$7A67
7A47: 20 64      JR           NZ,$7AAD
7A49: 6F         LD           L,A
7A4A: 6E         LD           L,(HL)
7A4B: 5E         LD           E,(HL)
7A4C: 74         LD           (HL),H
7A4D: 20 6B      JR           NZ,$7ABA
7A4F: 6E         LD           L,(HL)
7A50: 6F         LD           L,A
7A51: 77         LD           (HL),A
7A52: 20 20      JR           NZ,$7A74
7A54: 20 20      JR           NZ,$7A76
7A56: 20 20      JR           NZ,$7A78
7A58: 73         LD           (HL),E
7A59: 71         LD           (HL),C
7A5A: 75         LD           (HL),L
7A5B: 61         LD           H,C
7A5C: 74         LD           (HL),H
7A5D: 20 61      JR           NZ,$7AC0
7A5F: 62         LD           H,D
7A60: 6F         LD           L,A
7A61: 75         LD           (HL),L
7A62: 74         LD           (HL),H
7A63: 20 20      JR           NZ,$7A85
7A65: 20 20      JR           NZ,$7A87
7A67: 20 6D      JR           NZ,$7AD6
7A69: 75         LD           (HL),L
7A6A: 73         LD           (HL),E
7A6B: 69         LD           L,C
7A6C: 63         LD           H,E
7A6D: 21 20 20   LD           HL,$2020
7A70: 52         LD           D,D
7A71: 69         LD           L,C
7A72: 62         LD           H,D
7A73: 62         LD           H,D
7A74: 69         LD           L,C
7A75: 74         LD           (HL),H
7A76: 21 FF 52   LD           HL,$52FF
7A79: 69         LD           L,C
7A7A: 62         LD           H,D
7A7B: 62         LD           H,D
7A7C: 69         LD           L,C
7A7D: 74         LD           (HL),H
7A7E: 21 20 20   LD           HL,$2020
7A81: 52         LD           D,D
7A82: 69         LD           L,C
7A83: 62         LD           H,D
7A84: 62         LD           H,D
7A85: 69         LD           L,C
7A86: 74         LD           (HL),H
7A87: 21 49 5E   LD           HL,$5E49
7A8A: 6D         LD           L,L
7A8B: 20 4D      JR           NZ,$7ADA
7A8D: 61         LD           H,C
7A8E: 6D         LD           L,L
7A8F: 75         LD           (HL),L
7A90: 2C         INC         L
7A91: 20 6F      JR           NZ,$7B02
7A93: 6E         LD           L,(HL)
7A94: 20 20      JR           NZ,$7AB6
7A96: 20 20      JR           NZ,$7AB8
7A98: 76         HALT
7A99: 6F         LD           L,A
7A9A: 63         LD           H,E
7A9B: 61         LD           H,C
7A9C: 6C         LD           L,H
7A9D: 73         LD           (HL),E
7A9E: 21 20 20   LD           HL,$2020
7AA1: 42         LD           B,D
7AA2: 75         LD           (HL),L
7AA3: 74         LD           (HL),H
7AA4: 20 49      JR           NZ,$7AEF
7AA6: 20 20      JR           NZ,$7AC8
7AA8: 64         LD           H,H
7AA9: 6F         LD           L,A
7AAA: 6E         LD           L,(HL)
7AAB: 5E         LD           E,(HL)
7AAC: 74         LD           (HL),H
7AAD: 20 6E      JR           NZ,$7B1D
7AAF: 65         LD           H,L
7AB0: 65         LD           H,L
7AB1: 64         LD           H,H
7AB2: 20 74      JR           NZ,$7B28
7AB4: 6F         LD           L,A
7AB5: 20 20      JR           NZ,$7AD7
7AB7: 20 74      JR           NZ,$7B2D
7AB9: 65         LD           H,L
7ABA: 6C         LD           L,H
7ABB: 6C         LD           L,H
7ABC: 20 79      JR           NZ,$7B37
7ABE: 6F         LD           L,A
7ABF: 75         LD           (HL),L
7AC0: 20 74      JR           NZ,$7B36
7AC2: 68         LD           L,B
7AC3: 61         LD           H,C
7AC4: 74         LD           (HL),H
7AC5: 2C         INC         L
7AC6: 20 20      JR           NZ,$7AE8
7AC8: 64         LD           H,H
7AC9: 6F         LD           L,A
7ACA: 20 49      JR           NZ,$7B15
7ACC: 3F         CCF
7ACD: 20 20      JR           NZ,$7AEF
7ACF: 45         LD           B,L
7AD0: 76         HALT
7AD1: 65         LD           H,L
7AD2: 72         LD           (HL),D
7AD3: 79         LD           A,C
7AD4: 62         LD           H,D
7AD5: 6F         LD           L,A
7AD6: 64         LD           H,H
7AD7: 79         LD           A,C
7AD8: 6B         LD           L,E
7AD9: 6E         LD           L,(HL)
7ADA: 6F         LD           L,A
7ADB: 77         LD           (HL),A
7ADC: 73         LD           (HL),E
7ADD: 20 6D      JR           NZ,$7B4C
7ADF: 65         LD           H,L
7AE0: 21 20 20   LD           HL,$2020
7AE3: 57         LD           D,A
7AE4: 61         LD           H,C
7AE5: 6E         LD           L,(HL)
7AE6: 74         LD           (HL),H
7AE7: 20 74      JR           NZ,$7B5D
7AE9: 6F         LD           L,A
7AEA: 20 68      JR           NZ,$7B54
7AEC: 61         LD           H,C
7AED: 6E         LD           L,(HL)
7AEE: 67         LD           H,A
7AEF: 20 6F      JR           NZ,$7B60
7AF1: 75         LD           (HL),L
7AF2: 74         LD           (HL),H
7AF3: 20 61      JR           NZ,$7B56
7AF5: 6E         LD           L,(HL)
7AF6: 64         LD           H,H
7AF7: 20 6C      JR           NZ,$7B65
7AF9: 69         LD           L,C
7AFA: 73         LD           (HL),E
7AFB: 74         LD           (HL),H
7AFC: 65         LD           H,L
7AFD: 6E         LD           L,(HL)
7AFE: 20 74      JR           NZ,$7B74
7B00: 6F         LD           L,A
7B01: 20 75      JR           NZ,$7B78
7B03: 73         LD           (HL),E
7B04: 20 20      JR           NZ,$7B26
7B06: 20 20      JR           NZ,$7B28
7B08: 6A         LD           L,D
7B09: 61         LD           H,C
7B0A: 6D         LD           L,L
7B0B: 3F         CCF
7B0C: 20 20      JR           NZ,$7B2E
7B0E: 46         LD           B,(HL)
7B0F: 6F         LD           L,A
7B10: 72         LD           (HL),D
7B11: 20 33      JR           NZ,$7B46
7B13: 30 30      JR           NC,$7B45
7B15: 20 20      JR           NZ,$7B37
7B17: 20 52      JR           NZ,$7B6B
7B19: 75         LD           (HL),L
7B1A: 70         LD           (HL),B
7B1B: 65         LD           H,L
7B1C: 65         LD           H,L
7B1D: 73         LD           (HL),E
7B1E: 2C         INC         L
7B1F: 20 77      JR           NZ,$7B98
7B21: 65         LD           H,L
7B22: 5E         LD           E,(HL)
7B23: 6C         LD           L,H
7B24: 6C         LD           L,H
7B25: 20 20      JR           NZ,$7B47
7B27: 20 6C      JR           NZ,$7B95
7B29: 65         LD           H,L
7B2A: 74         LD           (HL),H
7B2B: 20 79      JR           NZ,$7BA6
7B2D: 6F         LD           L,A
7B2E: 75         LD           (HL),L
7B2F: 20 6C      JR           NZ,$7B9D
7B31: 69         LD           L,C
7B32: 73         LD           (HL),E
7B33: 74         LD           (HL),H
7B34: 65         LD           H,L
7B35: 6E         LD           L,(HL)
7B36: 20 20      JR           NZ,$7B58
7B38: 74         LD           (HL),H
7B39: 6F         LD           L,A
7B3A: 20 61      JR           NZ,$7B9D
7B3C: 20 70      JR           NZ,$7BAE
7B3E: 72         LD           (HL),D
7B3F: 65         LD           H,L
7B40: 76         HALT
7B41: 69         LD           L,C
7B42: 6F         LD           L,A
7B43: 75         LD           (HL),L
7B44: 73         LD           (HL),E
7B45: 6C         LD           L,H
7B46: 79         LD           A,C
7B47: 20 75      JR           NZ,$7BBE
7B49: 6E         LD           L,(HL)
7B4A: 72         LD           (HL),D
7B4B: 65         LD           H,L
7B4C: 6C         LD           L,H
7B4D: 65         LD           H,L
7B4E: 61         LD           H,C
7B4F: 73         LD           (HL),E
7B50: 65         LD           H,L
7B51: 64         LD           H,H
7B52: 20 63      JR           NZ,$7BB7
7B54: 75         LD           (HL),L
7B55: 74         LD           (HL),H
7B56: 21 20 57   LD           HL,$5720
7B59: 68         LD           L,B
7B5A: 61         LD           H,C
7B5B: 74         LD           (HL),H
7B5C: 20 64      JR           NZ,$7BC2
7B5E: 6F         LD           L,A
7B5F: 20 79      JR           NZ,$7BDA
7B61: 6F         LD           L,A
7B62: 75         LD           (HL),L
7B63: 20 64      JR           NZ,$7BC9
7B65: 6F         LD           L,A
7B66: 3F         CCF
7B67: 20 20      JR           NZ,$7B89
7B69: 20 20      JR           NZ,$7B8B
7B6B: 20 50      JR           NZ,$7BBD
7B6D: 61         LD           H,C
7B6E: 79         LD           A,C
7B6F: 20 20      JR           NZ,$7B91
7B71: 4C         LD           C,H
7B72: 65         LD           H,L
7B73: 61         LD           H,C
7B74: 76         HALT
7B75: 65         LD           H,L
7B76: FE 54      CP           $54
7B78: 68         LD           L,B
7B79: 61         LD           H,C
7B7A: 6E         LD           L,(HL)
7B7B: 6B         LD           L,E
7B7C: 20 79      JR           NZ,$7BF7
7B7E: 6F         LD           L,A
7B7F: 75         LD           (HL),L
7B80: 2E 2E      LD           L,$2E
7B82: 2E 20      LD           L,$20
7B84: 20 20      JR           NZ,$7BA6
7B86: 20 54      JR           NZ,$7BDC
7B88: 68         LD           L,B
7B89: 61         LD           H,C
7B8A: 6E         LD           L,(HL)
7B8B: 6B         LD           L,E
7B8C: 20 79      JR           NZ,$7C07
7B8E: 6F         LD           L,A
7B8F: 75         LD           (HL),L
7B90: 20 76      JR           NZ,$7C08
7B92: 65         LD           H,L
7B93: 72         LD           (HL),D
7B94: 79         LD           A,C
7B95: 20 20      JR           NZ,$7BB7
7B97: 6D         LD           L,L
7B98: 75         LD           (HL),L
7B99: 63         LD           H,E
7B9A: 68         LD           L,B
7B9B: 2E 2E      LD           L,$2E
7B9D: 2E 20      LD           L,$20
7B9F: 43         LD           B,E
7BA0: 72         LD           (HL),D
7BA1: 6F         LD           L,A
7BA2: 61         LD           H,C
7BA3: 6B         LD           L,E
7BA4: 21 FF 57   LD           HL,$57FF
7BA7: 65         LD           H,L
7BA8: 6C         LD           L,H
7BA9: 6C         LD           L,H
7BAA: 2C         INC         L
7BAB: 20 74      JR           NZ,$7C21
7BAD: 68         LD           L,B
7BAE: 61         LD           H,C
7BAF: 74         LD           (HL),H
7BB0: 5E         LD           E,(HL)
7BB1: 73         LD           (HL),E
7BB2: 20 61      JR           NZ,$7C15
7BB4: 20 20      JR           NZ,$7BD6
7BB6: 73         LD           (HL),E
7BB7: 68         LD           L,B
7BB8: 61         LD           H,C
7BB9: 6D         LD           L,L
7BBA: 65         LD           H,L
7BBB: 2C         INC         L
7BBC: 20 62      JR           NZ,$7C20
7BBE: 75         LD           (HL),L
7BBF: 74         LD           (HL),H
7BC0: 20 77      JR           NZ,$7C39
7BC2: 65         LD           H,L
7BC3: 20 20      JR           NZ,$7BE5
7BC5: 20 64      JR           NZ,$7C2B
7BC7: 6F         LD           L,A
7BC8: 6E         LD           L,(HL)
7BC9: 5E         LD           E,(HL)
7BCA: 74         LD           (HL),H
7BCB: 20 70      JR           NZ,$7C3D
7BCD: 6C         LD           L,H
7BCE: 61         LD           H,C
7BCF: 79         LD           A,C
7BD0: 20 66      JR           NZ,$7C38
7BD2: 6F         LD           L,A
7BD3: 72         LD           (HL),D
7BD4: 20 20      JR           NZ,$7BF6
7BD6: 66         LD           H,(HL)
7BD7: 72         LD           (HL),D
7BD8: 65         LD           H,L
7BD9: 65         LD           H,L
7BDA: 21 FF 59   LD           HL,$59FF
7BDD: 6F         LD           L,A
7BDE: 75         LD           (HL),L
7BDF: 5E         LD           E,(HL)
7BE0: 76         HALT
7BE1: 65         LD           H,L
7BE2: 20 6C      JR           NZ,$7C50
7BE4: 65         LD           H,L
7BE5: 61         LD           H,C
7BE6: 72         LD           (HL),D
7BE7: 6E         LD           L,(HL)
7BE8: 65         LD           H,L
7BE9: 64         LD           H,H
7BEA: 20 20      JR           NZ,$7C0C
7BEC: 54         LD           D,H
7BED: 68         LD           L,B
7BEE: 65         LD           H,L
7BEF: 20 46      JR           NZ,$7C37
7BF1: 72         LD           (HL),D
7BF2: 6F         LD           L,A
7BF3: 67         LD           H,A
7BF4: 5E         LD           E,(HL)
7BF5: 73         LD           (HL),E
7BF6: 20 53      JR           NZ,$7C4B
7BF8: 6F         LD           L,A
7BF9: 6E         LD           L,(HL)
7BFA: 67         LD           H,A
7BFB: 20 6F      JR           NZ,$7C6C
7BFD: 66         LD           H,(HL)
7BFE: 20 53      JR           NZ,$7C53
7C00: 6F         LD           L,A
7C01: 75         LD           (HL),L
7C02: 6C         LD           L,H
7C03: 21 20 20   LD           HL,$2020
7C06: 49         LD           C,C
7C07: 74         LD           (HL),H
7C08: 5E         LD           E,(HL)
7C09: 73         LD           (HL),E
7C0A: 20 61      JR           NZ,$7C6D
7C0C: 76         HALT
7C0D: 65         LD           H,L
7C0E: 72         LD           (HL),D
7C0F: 79         LD           A,C
7C10: 20 6D      JR           NZ,$7C7F
7C12: 6F         LD           L,A
7C13: 76         HALT
7C14: 69         LD           L,C
7C15: 6E         LD           L,(HL)
7C16: 67         LD           H,A
7C17: 20 20      JR           NZ,$7C39
7C19: 20 20      JR           NZ,$7C3B
7C1B: 20 74      JR           NZ,$7C91
7C1D: 75         LD           (HL),L
7C1E: 6E         LD           L,(HL)
7C1F: 65         LD           H,L
7C20: 2E 2E      LD           L,$2E
7C22: 2E 20      LD           L,$20
7C24: 49         LD           C,C
7C25: 74         LD           (HL),H
7C26: 20 63      JR           NZ,$7C8B
7C28: 61         LD           H,C
7C29: 6E         LD           L,(HL)
7C2A: 20 20      JR           NZ,$7C4C
7C2C: 65         LD           H,L
7C2D: 76         HALT
7C2E: 65         LD           H,L
7C2F: 6E         LD           L,(HL)
7C30: 20 6C      JR           NZ,$7C9E
7C32: 69         LD           L,C
7C33: 76         HALT
7C34: 65         LD           H,L
7C35: 6E         LD           L,(HL)
7C36: 20 75      JR           NZ,$7CAD
7C38: 70         LD           (HL),B
7C39: 20 20      JR           NZ,$7C5B
7C3B: 20 75      JR           NZ,$7CB2
7C3D: 6E         LD           L,(HL)
7C3E: 6C         LD           L,H
7C3F: 69         LD           L,C
7C40: 76         HALT
7C41: 69         LD           L,C
7C42: 6E         LD           L,(HL)
7C43: 67         LD           H,A
7C44: 20 74      JR           NZ,$7CBA
7C46: 68         LD           L,B
7C47: 69         LD           L,C
7C48: 6E         LD           L,(HL)
7C49: 67         LD           H,A
7C4A: 73         LD           (HL),E
7C4B: 21 FF 49   LD           HL,$49FF
7C4E: 66         LD           H,(HL)
7C4F: 20 79      JR           NZ,$7CCA
7C51: 6F         LD           L,A
7C52: 75         LD           (HL),L
7C53: 20 70      JR           NZ,$7CC5
7C55: 6C         LD           L,H
7C56: 61         LD           H,C
7C57: 79         LD           A,C
7C58: 20 74      JR           NZ,$7CCE
7C5A: 68         LD           L,B
7C5B: 69         LD           L,C
7C5C: 73         LD           (HL),E
7C5D: 73         LD           (HL),E
7C5E: 6F         LD           L,A
7C5F: 6E         LD           L,(HL)
7C60: 67         LD           H,A
7C61: 2C         INC         L
7C62: 20 79      JR           NZ,$7CDD
7C64: 6F         LD           L,A
7C65: 75         LD           (HL),L
7C66: 5E         LD           E,(HL)
7C67: 6C         LD           L,H
7C68: 6C         LD           L,H
7C69: 20 20      JR           NZ,$7C8B
7C6B: 20 20      JR           NZ,$7C8D
7C6D: 6D         LD           L,L
7C6E: 61         LD           H,C
7C6F: 6B         LD           L,E
7C70: 65         LD           H,L
7C71: 20 65      JR           NZ,$7CD8
7C73: 76         HALT
7C74: 65         LD           H,L
7C75: 72         LD           (HL),D
7C76: 79         LD           A,C
7C77: 74         LD           (HL),H
7C78: 68         LD           L,B
7C79: 69         LD           L,C
7C7A: 6E         LD           L,(HL)
7C7B: 67         LD           H,A
7C7C: 20 61      JR           NZ,$7CDF
7C7E: 72         LD           (HL),D
7C7F: 6F         LD           L,A
7C80: 75         LD           (HL),L
7C81: 6E         LD           L,(HL)
7C82: 64         LD           H,H
7C83: 20 79      JR           NZ,$7CFE
7C85: 6F         LD           L,A
7C86: 75         LD           (HL),L
7C87: 20 66      JR           NZ,$7CEF
7C89: 65         LD           H,L
7C8A: 65         LD           H,L
7C8B: 6C         LD           L,H
7C8C: 20 6D      JR           NZ,$7CFB
7C8E: 6F         LD           L,A
7C8F: 72         LD           (HL),D
7C90: 65         LD           H,L
7C91: 20 61      JR           NZ,$7CF4
7C93: 6C         LD           L,H
7C94: 69         LD           L,C
7C95: 76         HALT
7C96: 65         LD           H,L
7C97: 21 FF 48   LD           HL,$48FF
7C9A: 65         LD           H,L
7C9B: 79         LD           A,C
7C9C: 2C         INC         L
7C9D: 20 4B      JR           NZ,$7CEA
7C9F: 69         LD           L,C
7CA0: 64         LD           H,H
7CA1: 21 20 20   LD           HL,$2020
7CA4: 59         LD           E,C
7CA5: 6F         LD           L,A
7CA6: 75         LD           (HL),L
7CA7: 20 20      JR           NZ,$7CC9
7CA9: 77         LD           (HL),A
7CAA: 6F         LD           L,A
7CAB: 6B         LD           L,E
7CAC: 65         LD           H,L
7CAD: 20 6D      JR           NZ,$7D1C
7CAF: 65         LD           H,L
7CB0: 20 75      JR           NZ,$7D27
7CB2: 70         LD           (HL),B
7CB3: 20 66      JR           NZ,$7D1B
7CB5: 72         LD           (HL),D
7CB6: 6F         LD           L,A
7CB7: 6D         LD           L,L
7CB8: 20 61      JR           NZ,$7D1B
7CBA: 20 66      JR           NZ,$7D22
7CBC: 69         LD           L,C
7CBD: 6E         LD           L,(HL)
7CBE: 65         LD           H,L
7CBF: 20 6E      JR           NZ,$7D2F
7CC1: 61         LD           H,C
7CC2: 70         LD           (HL),B
7CC3: 21 21 20   LD           HL,$2021
7CC6: 20 20      JR           NZ,$7CE8
7CC8: 20 2E      JR           NZ,$7CF8
7CCA: 2E 2E      LD           L,$2E
7CCC: 54         LD           D,H
7CCD: 68         LD           L,B
7CCE: 61         LD           H,C
7CCF: 6E         LD           L,(HL)
7CD0: 6B         LD           L,E
7CD1: 73         LD           (HL),E
7CD2: 20 61      JR           NZ,$7D35
7CD4: 20 6C      JR           NZ,$7D42
7CD6: 6F         LD           L,A
7CD7: 74         LD           (HL),H
7CD8: 21 42 75   LD           HL,$7542
7CDB: 74         LD           (HL),H
7CDC: 20 6E      JR           NZ,$7D4C
7CDE: 6F         LD           L,A
7CDF: 77         LD           (HL),A
7CE0: 2C         INC         L
7CE1: 20 49      JR           NZ,$7D2C
7CE3: 5E         LD           E,(HL)
7CE4: 6C         LD           L,H
7CE5: 6C         LD           L,H
7CE6: 20 20      JR           NZ,$7D08
7CE8: 20 67      JR           NZ,$7D51
7CEA: 65         LD           H,L
7CEB: 74         LD           (HL),H
7CEC: 20 6D      JR           NZ,$7D5B
7CEE: 79         LD           A,C
7CEF: 20 72      JR           NZ,$7D63
7CF1: 65         LD           H,L
7CF2: 76         HALT
7CF3: 65         LD           H,L
7CF4: 6E         LD           L,(HL)
7CF5: 67         LD           H,A
7CF6: 65         LD           H,L
7CF7: 21 20 41   LD           HL,$4120
7CFA: 72         LD           (HL),D
7CFB: 65         LD           H,L
7CFC: 20 79      JR           NZ,$7D77
7CFE: 6F         LD           L,A
7CFF: 75         LD           (HL),L
7D00: 20 72      JR           NZ,$7D74
7D02: 65         LD           H,L
7D03: 61         LD           H,C
7D04: 64         LD           H,H
7D05: 79         LD           A,C
7D06: 3F         CCF
7D07: 21 20 20   LD           HL,$2020
7D0A: 20 20      JR           NZ,$7D2C
7D0C: 20 59      JR           NZ,$7D67
7D0E: 65         LD           H,L
7D0F: 73         LD           (HL),E
7D10: 20 20      JR           NZ,$7D32
7D12: 4E         LD           C,(HL)
7D13: 2D         DEC         L
7D14: 4E         LD           C,(HL)
7D15: 6F         LD           L,A
7D16: FE 49      CP           $49
7D18: 5E         LD           E,(HL)
7D19: 6C         LD           L,H
7D1A: 6C         LD           L,H
7D1B: 20 6C      JR           NZ,$7D89
7D1D: 65         LD           H,L
7D1E: 74         LD           (HL),H
7D1F: 20 79      JR           NZ,$7D9A
7D21: 6F         LD           L,A
7D22: 75         LD           (HL),L
7D23: 20 20      JR           NZ,$7D45
7D25: 20 20      JR           NZ,$7D47
7D27: 63         LD           H,E
7D28: 61         LD           H,C
7D29: 72         LD           (HL),D
7D2A: 72         LD           (HL),D
7D2B: 79         LD           A,C
7D2C: 20 6D      JR           NZ,$7D9B
7D2E: 6F         LD           L,A
7D2F: 72         LD           (HL),D
7D30: 65         LD           H,L
7D31: 20 4D      JR           NZ,$7D80
7D33: 61         LD           H,C
7D34: 67         LD           H,A
7D35: 69         LD           L,C
7D36: 63         LD           H,E
7D37: 50         LD           D,B
7D38: 6F         LD           L,A
7D39: 77         LD           (HL),A
7D3A: 64         LD           H,H
7D3B: 65         LD           H,L
7D3C: 72         LD           (HL),D
7D3D: 21 20 20   LD           HL,$2020
7D40: 48         LD           C,B
7D41: 65         LD           H,L
7D42: 20 48      JR           NZ,$7D8C
7D44: 65         LD           H,L
7D45: 21 20 41   LD           HL,$4120
7D48: 72         LD           (HL),D
7D49: 65         LD           H,L
7D4A: 20 79      JR           NZ,$7DC5
7D4C: 6F         LD           L,A
7D4D: 75         LD           (HL),L
7D4E: 20 72      JR           NZ,$7DC2
7D50: 65         LD           H,L
7D51: 61         LD           H,C
7D52: 64         LD           H,H
7D53: 79         LD           A,C
7D54: 3F         CCF
7D55: 21 20 20   LD           HL,$2020
7D58: 20 20      JR           NZ,$7D7A
7D5A: 20 59      JR           NZ,$7DB5
7D5C: 65         LD           H,L
7D5D: 73         LD           (HL),E
7D5E: 20 20      JR           NZ,$7D80
7D60: 4E         LD           C,(HL)
7D61: 2D         DEC         L
7D62: 4E         LD           C,(HL)
7D63: 6F         LD           L,A
7D64: FE 4F      CP           $4F
7D66: 6B         LD           L,E
7D67: 61         LD           H,C
7D68: 79         LD           A,C
7D69: 2C         INC         L
7D6A: 20 49      JR           NZ,$7DB5
7D6C: 5E         LD           E,(HL)
7D6D: 6C         LD           L,H
7D6E: 6C         LD           L,H
7D6F: 20 6C      JR           NZ,$7DDD
7D71: 65         LD           H,L
7D72: 74         LD           (HL),H
7D73: 20 20      JR           NZ,$7D95
7D75: 79         LD           A,C
7D76: 6F         LD           L,A
7D77: 75         LD           (HL),L
7D78: 20 63      JR           NZ,$7DDD
7D7A: 61         LD           H,C
7D7B: 72         LD           (HL),D
7D7C: 72         LD           (HL),D
7D7D: 79         LD           A,C
7D7E: 20 6D      JR           NZ,$7DED
7D80: 6F         LD           L,A
7D81: 72         LD           (HL),D
7D82: 65         LD           H,L
7D83: 20 20      JR           NZ,$7DA5
7D85: 42         LD           B,D
7D86: 6F         LD           L,A
7D87: 6D         LD           L,L
7D88: 62         LD           H,D
7D89: 73         LD           (HL),E
7D8A: 21 20 48   LD           HL,$4820
7D8D: 65         LD           H,L
7D8E: 20 48      JR           NZ,$7DD8
7D90: 65         LD           H,L
7D91: 20 48      JR           NZ,$7DDB
7D93: 65         LD           H,L
7D94: 21 41 72   LD           HL,$7241
7D97: 65         LD           H,L
7D98: 20 79      JR           NZ,$7E13
7D9A: 6F         LD           L,A
7D9B: 75         LD           (HL),L
7D9C: 20 72      JR           NZ,$7E10
7D9E: 65         LD           H,L
7D9F: 61         LD           H,C
7DA0: 64         LD           H,H
7DA1: 79         LD           A,C
7DA2: 3F         CCF
7DA3: 21 20 20   LD           HL,$2020
7DA6: 20 20      JR           NZ,$7DC8
7DA8: 20 59      JR           NZ,$7E03
7DAA: 65         LD           H,L
7DAB: 73         LD           (HL),E
7DAC: 20 20      JR           NZ,$7DCE
7DAE: 4E         LD           C,(HL)
7DAF: 2D         DEC         L
7DB0: 4E         LD           C,(HL)
7DB1: 6F         LD           L,A
7DB2: FE 46      CP           $46
7DB4: 69         LD           L,C
7DB5: 6E         LD           L,(HL)
7DB6: 65         LD           H,L
7DB7: 2C         INC         L
7DB8: 20 49      JR           NZ,$7E03
7DBA: 5E         LD           E,(HL)
7DBB: 6C         LD           L,H
7DBC: 6C         LD           L,H
7DBD: 20 6C      JR           NZ,$7E2B
7DBF: 65         LD           H,L
7DC0: 74         LD           (HL),H
7DC1: 20 20      JR           NZ,$7DE3
7DC3: 79         LD           A,C
7DC4: 6F         LD           L,A
7DC5: 75         LD           (HL),L
7DC6: 20 68      JR           NZ,$7E30
7DC8: 61         LD           H,C
7DC9: 76         HALT
7DCA: 65         LD           H,L
7DCB: 20 6D      JR           NZ,$7E3A
7DCD: 6F         LD           L,A
7DCE: 72         LD           (HL),D
7DCF: 65         LD           H,L
7DD0: 20 20      JR           NZ,$7DF2
7DD2: 20 61      JR           NZ,$7E35
7DD4: 72         LD           (HL),D
7DD5: 72         LD           (HL),D
7DD6: 6F         LD           L,A
7DD7: 77         LD           (HL),A
7DD8: 73         LD           (HL),E
7DD9: 21 20 48   LD           HL,$4820
7DDC: 65         LD           H,L
7DDD: 68         LD           L,B
7DDE: 20 48      JR           NZ,$7E28
7DE0: 65         LD           H,L
7DE1: 68         LD           L,B
7DE2: 21 41 72   LD           HL,$7241
7DE5: 65         LD           H,L
7DE6: 20 79      JR           NZ,$7E61
7DE8: 6F         LD           L,A
7DE9: 75         LD           (HL),L
7DEA: 20 72      JR           NZ,$7E5E
7DEC: 65         LD           H,L
7DED: 61         LD           H,C
7DEE: 64         LD           H,H
7DEF: 79         LD           A,C
7DF0: 3F         CCF
7DF1: 21 20 20   LD           HL,$2020
7DF4: 20 20      JR           NZ,$7E16
7DF6: 20 59      JR           NZ,$7E51
7DF8: 65         LD           H,L
7DF9: 73         LD           (HL),E
7DFA: 20 20      JR           NZ,$7E1C
7DFC: 4E         LD           C,(HL)
7DFD: 2D         DEC         L
7DFE: 4E         LD           C,(HL)
7DFF: 6F         LD           L,A
7E00: FE 48      CP           $48
7E02: 65         LD           H,L
7E03: 68         LD           L,B
7E04: 20 48      JR           NZ,$7E4E
7E06: 65         LD           H,L
7E07: 68         LD           L,B
7E08: 20 48      JR           NZ,$7E52
7E0A: 65         LD           H,L
7E0B: 68         LD           L,B
7E0C: 21 20 20   LD           HL,$2020
7E0F: 20 20      JR           NZ,$7E31
7E11: 59         LD           E,C
7E12: 6F         LD           L,A
7E13: 75         LD           (HL),L
7E14: 20 64      JR           NZ,$7E7A
7E16: 65         LD           H,L
7E17: 73         LD           (HL),E
7E18: 65         LD           H,L
7E19: 72         LD           (HL),D
7E1A: 76         HALT
7E1B: 65         LD           H,L
7E1C: 20 69      JR           NZ,$7E87
7E1E: 74         LD           (HL),H
7E1F: 21 20 4E   LD           HL,$4E20
7E22: 6F         LD           L,A
7E23: 77         LD           (HL),A
7E24: 20 6C      JR           NZ,$7E92
7E26: 6F         LD           L,A
7E27: 6F         LD           L,A
7E28: 6B         LD           L,E
7E29: 20 61      JR           NZ,$7E8C
7E2B: 74         LD           (HL),H
7E2C: 20 61      JR           NZ,$7E8F
7E2E: 6C         LD           L,H
7E2F: 6C         LD           L,H
7E30: 20 74      JR           NZ,$7EA6
7E32: 68         LD           L,B
7E33: 61         LD           H,C
7E34: 74         LD           (HL),H
7E35: 20 6A      JR           NZ,$7EA1
7E37: 75         LD           (HL),L
7E38: 6E         LD           L,(HL)
7E39: 6B         LD           L,E
7E3A: 20 79      JR           NZ,$7EB5
7E3C: 6F         LD           L,A
7E3D: 75         LD           (HL),L
7E3E: 20 20      JR           NZ,$7E60
7E40: 20 68      JR           NZ,$7EAA
7E42: 61         LD           H,C
7E43: 76         HALT
7E44: 65         LD           H,L
7E45: 20 74      JR           NZ,$7EBB
7E47: 6F         LD           L,A
7E48: 20 63      JR           NZ,$7EAD
7E4A: 61         LD           H,C
7E4B: 72         LD           (HL),D
7E4C: 72         LD           (HL),D
7E4D: 79         LD           A,C
7E4E: 21 20 20   LD           HL,$2020
7E51: 48         LD           C,B
7E52: 61         LD           H,C
7E53: 68         LD           L,B
7E54: 21 20 20   LD           HL,$2020
7E57: 54         LD           D,H
7E58: 61         LD           H,C
7E59: 6B         LD           L,E
7E5A: 65         LD           H,L
7E5B: 20 63      JR           NZ,$7EC0
7E5D: 61         LD           H,C
7E5E: 72         LD           (HL),D
7E5F: 65         LD           H,L
7E60: 21 53 65   LD           HL,$6553
7E63: 65         LD           H,L
7E64: 20 79      JR           NZ,$7EDF
7E66: 6F         LD           L,A
7E67: 75         LD           (HL),L
7E68: 20 61      JR           NZ,$7ECB
7E6A: 67         LD           H,A
7E6B: 61         LD           H,C
7E6C: 69         LD           L,C
7E6D: 6E         LD           L,(HL)
7E6E: 21 FF 3F   LD           HL,$3FFF
7E71: 3F         CCF
7E72: 20 20      JR           NZ,$7E94
7E74: 54         LD           D,H
7E75: 68         LD           L,B
7E76: 65         LD           H,L
7E77: 72         LD           (HL),D
7E78: 65         LD           H,L
7E79: 20 69      JR           NZ,$7EE4
7E7B: 73         LD           (HL),E
7E7C: 20 61      JR           NZ,$7EDF
7E7E: 20 20      JR           NZ,$7EA0
7E80: 70         LD           (HL),B
7E81: 69         LD           L,C
7E82: 63         LD           H,E
7E83: 74         LD           (HL),H
7E84: 75         LD           (HL),L
7E85: 72         LD           (HL),D
7E86: 65         LD           H,L
7E87: 20 63      JR           NZ,$7EEC
7E89: 61         LD           H,C
7E8A: 72         LD           (HL),D
7E8B: 76         HALT
7E8C: 65         LD           H,L
7E8D: 64         LD           H,H
7E8E: 20 20      JR           NZ,$7EB0
7E90: 6F         LD           L,A
7E91: 6E         LD           L,(HL)
7E92: 20 74      JR           NZ,$7F08
7E94: 68         LD           L,B
7E95: 65         LD           H,L
7E96: 20 77      JR           NZ,$7F0F
7E98: 61         LD           H,C
7E99: 6C         LD           L,H
7E9A: 6C         LD           L,H
7E9B: 2C         INC         L
7E9C: 20 62      JR           NZ,$7F00
7E9E: 75         LD           (HL),L
7E9F: 74         LD           (HL),H
7EA0: 79         LD           A,C
7EA1: 6F         LD           L,A
7EA2: 75         LD           (HL),L
7EA3: 20 63      JR           NZ,$7F08
7EA5: 61         LD           H,C
7EA6: 6E         LD           L,(HL)
7EA7: 5E         LD           E,(HL)
7EA8: 74         LD           (HL),H
7EA9: 20 73      JR           NZ,$7F1E
7EAB: 65         LD           H,L
7EAC: 65         LD           H,L
7EAD: 20 69      JR           NZ,$7F18
7EAF: 74         LD           (HL),H
7EB0: 62         LD           H,D
7EB1: 65         LD           H,L
7EB2: 63         LD           H,E
7EB3: 61         LD           H,C
7EB4: 75         LD           (HL),L
7EB5: 73         LD           (HL),E
7EB6: 65         LD           H,L
7EB7: 20 69      JR           NZ,$7F22
7EB9: 74         LD           (HL),H
7EBA: 5E         LD           E,(HL)
7EBB: 73         LD           (HL),E
7EBC: 20 74      JR           NZ,$7F32
7EBE: 6F         LD           L,A
7EBF: 6F         LD           L,A
7EC0: 64         LD           H,H
7EC1: 61         LD           H,C
7EC2: 72         LD           (HL),D
7EC3: 6B         LD           L,E
7EC4: 20 69      JR           NZ,$7F2F
7EC6: 6E         LD           L,(HL)
7EC7: 20 68      JR           NZ,$7F31
7EC9: 65         LD           H,L
7ECA: 72         LD           (HL),D
7ECB: 65         LD           H,L
7ECC: 2E 2E      LD           L,$2E
7ECE: 2E FF      LD           L,$FF
7ED0: 54         LD           D,H
7ED1: 4F         LD           C,A
7ED2: 20 54      JR           NZ,$7F28
7ED4: 48         LD           C,B
7ED5: 45         LD           B,L
7ED6: 20 46      JR           NZ,$7F1E
7ED8: 49         LD           C,C
7ED9: 4E         LD           C,(HL)
7EDA: 44         LD           B,H
7EDB: 45         LD           B,L
7EDC: 52         LD           D,D
7EDD: 2E 2E      LD           L,$2E
7EDF: 2E 20      LD           L,$20
7EE1: 20 54      JR           NZ,$7F37
7EE3: 48         LD           C,B
7EE4: 45         LD           B,L
7EE5: 20 49      JR           NZ,$7F30
7EE7: 53         LD           D,E
7EE8: 4C         LD           C,H
7EE9: 45         LD           B,L
7EEA: 20 4F      JR           NZ,$7F3B
7EEC: 46         LD           B,(HL)
7EED: 20 20      JR           NZ,$7F0F
7EEF: 20 4B      JR           NZ,$7F3C
7EF1: 4F         LD           C,A
7EF2: 48         LD           C,B
7EF3: 4F         LD           C,A
7EF4: 4C         LD           C,H
7EF5: 49         LD           C,C
7EF6: 4E         LD           C,(HL)
7EF7: 54         LD           D,H
7EF8: 2C         INC         L
7EF9: 20 49      JR           NZ,$7F44
7EFB: 53         LD           D,E
7EFC: 20 42      JR           NZ,$7F40
7EFE: 55         LD           D,L
7EFF: 54         LD           D,H
7F00: 20 20      JR           NZ,$7F22
7F02: 41         LD           B,C
7F03: 4E         LD           C,(HL)
7F04: 20 49      JR           NZ,$7F4F
7F06: 4C         LD           C,H
7F07: 4C         LD           C,H
7F08: 55         LD           D,L
7F09: 53         LD           D,E
7F0A: 49         LD           C,C
7F0B: 4F         LD           C,A
7F0C: 4E         LD           C,(HL)
7F0D: 2E 2E      LD           L,$2E
7F0F: 2E 20      LD           L,$20
7F11: 48         LD           C,B
7F12: 55         LD           D,L
7F13: 4D         LD           C,L
7F14: 41         LD           B,C
7F15: 4E         LD           C,(HL)
7F16: 2C         INC         L
7F17: 20 4D      JR           NZ,$7F66
7F19: 4F         LD           C,A
7F1A: 4E         LD           C,(HL)
7F1B: 53         LD           D,E
7F1C: 54         LD           D,H
7F1D: 45         LD           B,L
7F1E: 52         LD           D,D
7F1F: 2C         INC         L
7F20: 20 53      JR           NZ,$7F75
7F22: 45         LD           B,L
7F23: 41         LD           B,C
7F24: 2C         INC         L
7F25: 20 53      JR           NZ,$7F7A
7F27: 4B         LD           C,E
7F28: 59         LD           E,C
7F29: 2E 2E      LD           L,$2E
7F2B: 2E 20      LD           L,$20
7F2D: 41         LD           B,C
7F2E: 20 20      JR           NZ,$7F50
7F30: 53         LD           D,E
7F31: 43         LD           B,E
7F32: 45         LD           B,L
7F33: 4E         LD           C,(HL)
7F34: 45         LD           B,L
7F35: 20 4F      JR           NZ,$7F86
7F37: 4E         LD           C,(HL)
7F38: 20 54      JR           NZ,$7F8E
7F3A: 48         LD           C,B
7F3B: 45         LD           B,L
7F3C: 20 4C      JR           NZ,$7F8A
7F3E: 49         LD           C,C
7F3F: 44         LD           B,H
7F40: 20 4F      JR           NZ,$7F91
7F42: 46         LD           B,(HL)
7F43: 20 41      JR           NZ,$7F86
7F45: 20 53      JR           NZ,$7F9A
7F47: 4C         LD           C,H
7F48: 45         LD           B,L
7F49: 45         LD           B,L
7F4A: 50         LD           D,B
7F4B: 45         LD           B,L
7F4C: 52         LD           D,D
7F4D: 5E         LD           E,(HL)
7F4E: 53         LD           D,E
7F4F: 20 20      JR           NZ,$7F71
7F51: 20 45      JR           NZ,$7F98
7F53: 59         LD           E,C
7F54: 45         LD           B,L
7F55: 2E 2E      LD           L,$2E
7F57: 2E 20      LD           L,$20
7F59: 20 41      JR           NZ,$7F9C
7F5B: 57         LD           D,A
7F5C: 41         LD           B,C
7F5D: 4B         LD           C,E
7F5E: 45         LD           B,L
7F5F: 20 54      JR           NZ,$7FB5
7F61: 48         LD           C,B
7F62: 45         LD           B,L
7F63: 20 44      JR           NZ,$7FA9
7F65: 52         LD           D,D
7F66: 45         LD           B,L
7F67: 41         LD           B,C
7F68: 4D         LD           C,L
7F69: 45         LD           B,L
7F6A: 52         LD           D,D
7F6B: 2C         INC         L
7F6C: 20 41      JR           NZ,$7FAF
7F6E: 4E         LD           C,(HL)
7F6F: 44         LD           B,H
7F70: 20 20      JR           NZ,$7F92
7F72: 4B         LD           C,E
7F73: 4F         LD           C,A
7F74: 48         LD           C,B
7F75: 4F         LD           C,A
7F76: 4C         LD           C,H
7F77: 49         LD           C,C
7F78: 4E         LD           C,(HL)
7F79: 54         LD           D,H
7F7A: 20 57      JR           NZ,$7FD3
7F7C: 49         LD           C,C
7F7D: 4C         LD           C,H
7F7E: 4C         LD           C,H
7F7F: 20 56      JR           NZ,$7FD7
7F81: 41         LD           B,C
7F82: 4E         LD           C,(HL)
7F83: 49         LD           C,C
7F84: 53         LD           D,E
7F85: 48         LD           C,B
7F86: 20 4D      JR           NZ,$7FD5
7F88: 55         LD           D,L
7F89: 43         LD           B,E
7F8A: 48         LD           C,B
7F8B: 20 4C      JR           NZ,$7FD9
7F8D: 49         LD           C,C
7F8E: 4B         LD           C,E
7F8F: 45         LD           B,L
7F90: 20 20      JR           NZ,$7FB2
7F92: 41         LD           B,C
7F93: 20 42      JR           NZ,$7FD7
7F95: 55         LD           D,L
7F96: 42         LD           B,D
7F97: 42         LD           B,D
7F98: 4C         LD           C,H
7F99: 45         LD           B,L
7F9A: 20 4F      JR           NZ,$7FEB
7F9C: 4E         LD           C,(HL)
7F9D: 20 41      JR           NZ,$7FE0
7F9F: 20 4E      JR           NZ,$7FEF
7FA1: 45         LD           B,L
7FA2: 45         LD           B,L
7FA3: 44         LD           B,H
7FA4: 4C         LD           C,H
7FA5: 45         LD           B,L
7FA6: 2E 2E      LD           L,$2E
7FA8: 2E 20      LD           L,$20
7FAA: 43         LD           B,E
7FAB: 41         LD           B,C
7FAC: 53         LD           D,E
7FAD: 54         LD           D,H
7FAE: 2D         DEC         L
7FAF: 20 41      JR           NZ,$7FF2
7FB1: 57         LD           D,A
7FB2: 41         LD           B,C
7FB3: 59         LD           E,C
7FB4: 2C         INC         L
7FB5: 20 59      JR           NZ,$8010
7FB7: 4F         LD           C,A
7FB8: 55         LD           D,L
7FB9: 20 53      JR           NZ,$800E
7FBB: 48         LD           C,B
7FBC: 4F         LD           C,A
7FBD: 55         LD           D,L
7FBE: 4C         LD           C,H
7FBF: 44         LD           B,H
7FC0: 4B         LD           C,E
7FC1: 4E         LD           C,(HL)
7FC2: 4F         LD           C,A
7FC3: 57         LD           D,A
7FC4: 20 54      JR           NZ,$801A
7FC6: 48         LD           C,B
7FC7: 45         LD           B,L
7FC8: 20 54      JR           NZ,$801E
7FCA: 52         LD           D,D
7FCB: 55         LD           D,L
7FCC: 54         LD           D,H
7FCD: 48         LD           C,B
7FCE: 21 20 2E   LD           HL,$2E20
7FD1: 2E 2E      LD           L,$2E
7FD3: 20 2E      JR           NZ,$8003
7FD5: 2E 2E      LD           L,$2E
7FD7: 20 2E      JR           NZ,$8007
7FD9: 2E 2E      LD           L,$2E
7FDB: 20 2E      JR           NZ,$800B
7FDD: 2E 2E      LD           L,$2E
7FDF: 20 57      JR           NZ,$8038
7FE1: 68         LD           L,B
7FE2: 61         LD           H,C
7FE3: 74         LD           (HL),H
7FE4: 3F         CCF
7FE5: 20 20      JR           NZ,$8007
7FE7: 49         LD           C,C
7FE8: 6C         LD           L,H
7FE9: 6C         LD           L,H
7FEA: 75         LD           (HL),L
7FEB: 73         LD           (HL),E
7FEC: 69         LD           L,C
7FED: 6F         LD           L,A
7FEE: 6E         LD           L,(HL)
7FEF: 3F         CCF
7FF0: FF         RST         0X38
7FF1: FF         RST         0X38
7FF2: FF         RST         0X38
7FF3: FF         RST         0X38
7FF4: FF         RST         0X38
7FF5: FF         RST         0X38
7FF6: FF         RST         0X38
7FF7: FF         RST         0X38
7FF8: FF         RST         0X38
7FF9: FF         RST         0X38
7FFA: FF         RST         0X38
7FFB: FF         RST         0X38
7FFC: FF         RST         0X38
7FFD: FF         RST         0X38
7FFE: FF         RST         0X38
7FFF: FF         RST         0X38
```
