![Bank 11](GBZelda.jpg)

# Bank 11

>>> cpu Z80GB

>>> binary 4000:roms/zelda.gb[44000:48000]

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

```code
4000: 00         NOP
4001: 00         NOP
4002: 00         NOP
4003: 00         NOP
4004: 00         NOP
4005: 00         NOP
4006: 00         NOP
4007: 00         NOP
4008: 01 00 01   LD           BC,$0100
400B: 00         NOP
400C: 3F         CCF
400D: 00         NOP
400E: 59         LD           E,C
400F: 3E AE      LD           A,$AE
4011: 71         LD           (HL),C
4012: A7         AND         A
4013: 78         LD           A,B
4014: 51         LD           D,C
4015: 3E 61      LD           A,$61
4017: 1E 72      LD           E,$72
4019: 2D         DEC         L
401A: FF         RST         0X38
401B: 61         LD           H,C
401C: FF         RST         0X38
401D: 01 E2 DD   LD           BC,$DDE2
4020: 00         NOP
4021: 00         NOP
4022: 00         NOP
4023: 00         NOP
4024: 73         LD           (HL),E
4025: 00         NOP
4026: 9F         SBC         A
4027: 63         LD           H,E
4028: 1F         RRA
4029: EC                              
402A: 3B         DEC         SP
402B: DC BB 5C   CALL       C,$5CBB
402E: FF         RST         0X38
402F: 1C         INC         E
4030: EE 1B      XOR         $1B
4032: B7         OR           A
4033: 6B         LD           L,E
4034: 75         LD           (HL),L
4035: FB         EI
4036: 9A         SBC         D
4037: FD                              
4038: 9B         SBC         E
4039: FD                              
403A: F7         RST         0X30
403B: FB         EI
403C: FF         RST         0X38
403D: F7         RST         0X30
403E: 6E         LD           L,(HL)
403F: F7         RST         0X30
4040: 52         LD           D,D
4041: 3D         DEC         A
4042: 6E         LD           L,(HL)
4043: 31 D3 6C   LD           SP,$6CD3
4046: E1         POP         HL
4047: 5E         LD           E,(HL)
4048: C9         RET
4049: 7E         LD           A,(HL)
404A: B3         OR           E
404B: 7C         LD           A,H
404C: 7E         LD           A,(HL)
404D: 01 3D 03   LD           BC,$033D
4050: 26 1B      LD           H,$1B
4052: 76         HALT
4053: 3B         DEC         SP
4054: 6E         LD           L,(HL)
4055: 33         INC         SP
4056: 7E         LD           A,(HL)
4057: 43         LD           B,E
4058: 76         HALT
4059: 7B         LD           A,E
405A: 07         RLCA
405B: 01 03 00   LD           BC,$0003
405E: 01 00 7E   LD           BC,$7E00
4061: EF         RST         0X28
4062: 7F         LD           A,A
4063: EF         RST         0X28
4064: 19         ADD         HL,DE
4065: EF         RST         0X28
4066: 99         SBC         C
4067: 6F         LD           L,A
4068: FF         RST         0X38
4069: 0F         RRCA
406A: 76         HALT
406B: 8F         ADC         A,A
406C: 3A         LD           A,(HLD)
406D: C7         RST         0X00
406E: 4C         LD           C,H
406F: B3         OR           E
4070: 87         ADD         A,A
4071: 78         LD           A,B
4072: 82         ADD         A,D
4073: 7D         LD           A,L
4074: 0B         DEC         BC
4075: FD                              
4076: 35         DEC         (HL)
4077: FB         EI
4078: 5D         LD           E,L
4079: E3                              
407A: BE         CP           (HL)
407B: C1         POP         BC
407C: F7         RST         0X30
407D: 06 C3      LD           B,$C3
407F: 03         INC         BC
4080: 00         NOP
4081: 00         NOP
4082: 00         NOP
4083: 00         NOP
4084: 00         NOP
4085: 00         NOP
4086: 00         NOP
4087: 00         NOP
4088: 01 00 01   LD           BC,$0100
408B: 00         NOP
408C: 3F         CCF
408D: 00         NOP
408E: 59         LD           E,C
408F: 3E AF      LD           A,$AF
4091: 70         LD           (HL),B
4092: 9F         SBC         A
4093: 67         LD           H,A
4094: 78         LD           A,B
4095: 0F         RRCA
4096: 77         LD           (HL),A
4097: 38 CF      JR           C,$4068
4099: 70         LD           (HL),B
409A: DF         RST         0X18
409B: 60         LD           H,B
409C: BF         CP           A
409D: 70         LD           (HL),B
409E: 4F         LD           C,A
409F: 38 03      JR           C,$40A4
40A1: 00         NOP
40A2: 07         RLCA
40A3: 03         INC         BC
40A4: 7C         LD           A,H
40A5: 07         RLCA
40A6: 9D         SBC         L
40A7: 66         LD           H,(HL)
40A8: 1B         DEC         DE
40A9: E6 3F      AND         $3F
40AB: CE 73      ADC         $73
40AD: 9C         SBC         H
40AE: EF         RST         0X28
40AF: 30 FF      JR           NC,$40B0
40B1: 20 FF      JR           NZ,$40B2
40B3: 20 DF      JR           NZ,$4094
40B5: B0         OR           B
40B6: 7F         LD           A,A
40B7: D0         RET         NC
40B8: BF         CP           A
40B9: 69         LD           L,C
40BA: DF         RST         0X18
40BB: 39         ADD         HL,SP
40BC: E6 19      AND         $19
40BE: FD                              
40BF: 02         LD           (BC),A
40C0: 7F         LD           A,A
40C1: 08 7D 0E   LD           ($0E7D),SP
40C4: D7         RST         0X10
40C5: 6F         LD           L,A
40C6: D9         RETI
40C7: 67         LD           H,A
40C8: CC 73 A7   CALL       Z,$A773
40CB: 78         LD           A,B
40CC: 7F         LD           A,A
40CD: 00         NOP
40CE: 3C         INC         A
40CF: 03         INC         BC
40D0: 26 1B      LD           H,$1B
40D2: 76         HALT
40D3: 3B         DEC         SP
40D4: 6E         LD           L,(HL)
40D5: 33         INC         SP
40D6: 7E         LD           A,(HL)
40D7: 43         LD           B,E
40D8: 76         HALT
40D9: 7B         LD           A,E
40DA: 07         RLCA
40DB: 01 03 00   LD           BC,$0003
40DE: 01 00 FD   LD           BC,$FD00
40E1: 03         INC         BC
40E2: EE 19      XOR         $19
40E4: FF         RST         0X38
40E5: F4                              
40E6: FB         EI
40E7: EC                              
40E8: 37         SCF
40E9: D8         RET         C
40EA: FF         RST         0X38
40EB: 10 FF      STOP       $FF
40ED: 10 FF      STOP       $FF
40EF: 10 FF      STOP       $FF
40F1: 10 AF      STOP       $AF
40F3: 58         LD           E,B
40F4: 37         SCF
40F5: CE 13      ADC         $13
40F7: EE 5D      XOR         $5D
40F9: E6 BD      AND         $BD
40FB: C6 FF      ADD         $FF
40FD: 03         INC         BC
40FE: C7         RST         0X00
40FF: 00         NOP
4100: 00         NOP
4101: 00         NOP
4102: 03         INC         BC
4103: 00         NOP
4104: 0C         INC         C
4105: 03         INC         BC
4106: 14         INC         D
4107: 0B         DEC         BC
4108: 20 1F      JR           NZ,$4129
410A: 20 1F      JR           NZ,$412B
410C: 24         INC         H
410D: 1B         DEC         DE
410E: 2A         LD           A,(HLI)
410F: 1D         DEC         E
4110: 2E 1D      LD           L,$1D
4112: 1E 0D      LD           E,$0D
4114: 16 0D      LD           D,$0D
4116: 0A         LD           A,(BC)
4117: 05         DEC         B
4118: 06 01      LD           B,$01
411A: 02         LD           (BC),A
411B: 01 01 00   LD           BC,$0001
411E: 01 00 F3   LD           BC,$F300
4121: 00         NOP
4122: 0C         INC         C
4123: F3         DI
4124: 03         INC         BC
4125: FC                              
4126: 60         LD           H,B
4127: 9F         SBC         A
4128: 85         ADD         A,L
4129: 7B         LD           A,E
412A: 82         ADD         A,D
412B: 7D         LD           A,L
412C: 89         ADC         A,C
412D: 7E         LD           A,(HL)
412E: E4                              
412F: 1F         RRA
4130: D2 2F BA   JP           NC,$BA2F
4133: 77         LD           (HL),A
4134: BE         CP           (HL)
4135: 7B         LD           A,E
4136: BC         CP           H
4137: 63         LD           H,E
4138: 95         SUB         L
4139: 6A         LD           L,D
413A: 5F         LD           E,A
413B: A1         AND         C
413C: 3D         DEC         A
413D: C3 89 77   JP           $7789
4140: E5         PUSH       HL
4141: 1B         DEC         DE
4142: A4         AND         H
4143: 5B         LD           E,E
4144: A9         XOR         C
4145: 57         LD           D,A
4146: 69         LD           L,C
4147: 17         RLA
4148: 49         LD           C,C
4149: 37         SCF
414A: 84         ADD         A,H
414B: 7B         LD           A,E
414C: 84         ADD         A,H
414D: 7B         LD           A,E
414E: 81         ADD         A,C
414F: 7F         LD           A,A
4150: 45         LD           B,L
4151: 3B         DEC         SP
4152: 26 19      LD           H,$19
4154: 22         LD           (HLI),A
4155: 1D         DEC         E
4156: 22         LD           (HLI),A
4157: 1D         DEC         E
4158: 21 1F 10   LD           HL,$101F
415B: 0F         RRCA
415C: 0C         INC         C
415D: 03         INC         BC
415E: 03         INC         BC
415F: 00         NOP
4160: 07         RLCA
4161: 00         NOP
4162: 08 07 30   LD           ($3007),SP
4165: 0F         RRCA
4166: 51         LD           D,C
4167: 2E B3      LD           L,$B3
4169: 6D         LD           L,L
416A: B6         OR           (HL)
416B: 49         LD           C,C
416C: F7         RST         0X30
416D: 28 B7      JR           Z,$4126
416F: 68         LD           L,B
4170: B3         OR           E
4171: 6C         LD           L,H
4172: B0         OR           B
4173: 4F         LD           C,A
4174: F0 2F      LD           A,($2F)
4176: B8         CP           B
4177: 77         LD           (HL),A
4178: 9F         SBC         A
4179: 78         LD           A,B
417A: 4F         LD           C,A
417B: 3F         CCF
417C: 20 1F      JR           NZ,$419D
417E: 1F         RRA
417F: 00         NOP
4180: F3         DI
4181: 00         NOP
4182: 0C         INC         C
4183: F3         DI
4184: 03         INC         BC
4185: FC                              
4186: 60         LD           H,B
4187: 9F         SBC         A
4188: 85         ADD         A,L
4189: 7B         LD           A,E
418A: 82         ADD         A,D
418B: 7D         LD           A,L
418C: 89         ADC         A,C
418D: 7E         LD           A,(HL)
418E: E4                              
418F: 1F         RRA
4190: 72         LD           (HL),D
4191: 8F         ADC         A,A
4192: DA 27 CE   JP           C,$CE27
4195: 33         INC         SP
4196: A4         AND         H
4197: 5B         LD           E,E
4198: 95         SUB         L
4199: 6A         LD           L,D
419A: 4F         LD           C,A
419B: B1         OR           C
419C: 3D         DEC         A
419D: C3 89 77   JP           $7789
41A0: 01 01 03   LD           BC,$0301
41A3: 02         LD           (BC),A
41A4: 07         RLCA
41A5: 04         INC         B
41A6: 0F         RRCA
41A7: 0C         INC         C
41A8: 1F         RRA
41A9: 14         INC         D
41AA: 17         RLA
41AB: 1A         LD           A,(DE)
41AC: 23         INC         HL
41AD: 3D         DEC         A
41AE: 23         INC         HL
41AF: 3E 27      LD           A,$27
41B1: 3C         INC         A
41B2: 2F         CPL
41B3: 3C         INC         A
41B4: 37         SCF
41B5: 3C         INC         A
41B6: 37         SCF
41B7: 1C         INC         E
41B8: 17         RLA
41B9: 1E 15      LD           E,$15
41BB: 1F         RRA
41BC: 1C         INC         E
41BD: 0F         RRCA
41BE: 07         RLCA
41BF: 03         INC         BC
41C0: FF         RST         0X38
41C1: FF         RST         0X38
41C2: FF         RST         0X38
41C3: 20 FF      JR           NZ,$41C4
41C5: 20 FF      JR           NZ,$41C6
41C7: 58         LD           E,B
41C8: FF         RST         0X38
41C9: 86         ADD         A,(HL)
41CA: FF         RST         0X38
41CB: 81         ADD         A,C
41CC: FF         RST         0X38
41CD: 81         ADD         A,C
41CE: EF         RST         0X28
41CF: F1         POP         AF
41D0: F7         RST         0X30
41D1: 99         SBC         C
41D2: F9         LD           SP,HL
41D3: CF         RST         0X08
41D4: BD         CP           L
41D5: E7         RST         0X20
41D6: 9D         SBC         L
41D7: F7         RST         0X30
41D8: CF         RST         0X08
41D9: FE FF      CP           $FF
41DB: 3C         INC         A
41DC: FF         RST         0X38
41DD: 88         ADC         A,B
41DE: 7F         LD           A,A
41DF: C8         RET         Z
41E0: FF         RST         0X38
41E1: F8 DF      LDHL       SP,$DF
41E3: 70         LD           (HL),B
41E4: DF         RST         0X18
41E5: 73         LD           (HL),E
41E6: FF         RST         0X38
41E7: 74         LD           (HL),H
41E8: CF         RST         0X08
41E9: 78         LD           A,B
41EA: 8F         ADC         A,A
41EB: F8 87      LDHL       SP,$87
41ED: FC                              
41EE: 87         ADD         A,A
41EF: FF         RST         0X38
41F0: 9F         SBC         A
41F1: FC                              
41F2: EF         RST         0X28
41F3: 74         LD           (HL),H
41F4: E7         RST         0X20
41F5: 3A         LD           A,(HLD)
41F6: E7         RST         0X20
41F7: 3B         DEC         SP
41F8: 67         LD           H,A
41F9: 3C         INC         A
41FA: 7F         LD           A,A
41FB: 18 3F      JR           $423C
41FD: 08 1F 07   LD           ($071F),SP
4200: 03         INC         BC
4201: 00         NOP
4202: 0F         RRCA
4203: 00         NOP
4204: 1F         RRA
4205: 00         NOP
4206: 3F         CCF
4207: 03         INC         BC
4208: 3F         CCF
4209: 01 3F 06   LD           BC,$063F
420C: 57         LD           D,A
420D: 38 73      JR           C,$4282
420F: 3C         INC         A
4210: 7B         LD           A,E
4211: 34         INC         (HL)
4212: 63         LD           H,E
4213: 3C         INC         A
4214: 67         LD           H,A
4215: 38 47      JR           C,$425E
4217: 38 49      JR           C,$4262
4219: 30 33      JR           NC,$424E
421B: 01 07 02   LD           BC,$0207
421E: 07         RLCA
421F: 00         NOP
4220: 80         ADD         A,B
4221: 00         NOP
4222: C0         RET         NZ
4223: 00         NOP
4224: E0 00      LDFF00   ($00),A
4226: F0 00      LD           A,($00)
4228: F0 00      LD           A,($00)
422A: F8 00      LDHL       SP,$00
422C: B8         CP           B
422D: 40         LD           B,B
422E: BC         CP           H
422F: 40         LD           B,B
4230: BC         CP           H
4231: 40         LD           B,B
4232: DC 20 EC   CALL       C,$EC20
4235: 10 F8      STOP       $F8
4237: 00         NOP
4238: DC 20 CC   CALL       C,$CC20
423B: 70         LD           (HL),B
423C: A8         XOR         B
423D: D0         RET         NC
423E: F8 00      LDHL       SP,$00
4240: 38 00      JR           C,$4242
4242: 2F         CPL
4243: 10 3F      STOP       $3F
4245: 00         NOP
4246: 3F         CCF
4247: 00         NOP
4248: 7F         LD           A,A
4249: 06 7F      LD           B,$7F
424B: 02         LD           (BC),A
424C: 7F         LD           A,A
424D: 0C         INC         C
424E: AF         XOR         A
424F: 70         LD           (HL),B
4250: E7         RST         0X20
4251: 78         LD           A,B
4252: F7         RST         0X30
4253: 68         LD           L,B
4254: C7         RST         0X00
4255: 78         LD           A,B
4256: CF         RST         0X08
4257: 70         LD           (HL),B
4258: 8F         ADC         A,A
4259: 70         LD           (HL),B
425A: 93         SUB         E
425B: 61         LD           H,C
425C: 67         LD           H,A
425D: 02         LD           (BC),A
425E: 07         RLCA
425F: 00         NOP
4260: 0F         RRCA
4261: 00         NOP
4262: 17         RLA
4263: 08 AE 10   LD           ($10AE),SP
4266: FC                              
4267: 00         NOP
4268: FF         RST         0X38
4269: 00         NOP
426A: F7         RST         0X30
426B: 08 FE 00   LD           ($00FE),SP
426E: FC                              
426F: 00         NOP
4270: F8 00      LDHL       SP,$00
4272: F0 00      LD           A,($00)
4274: FC                              
4275: 00         NOP
4276: FE 00      CP           $00
4278: DC 20 C8   CALL       C,$C820
427B: 70         LD           (HL),B
427C: A8         XOR         B
427D: D0         RET         NC
427E: F8 00      LDHL       SP,$00
4280: 07         RLCA
4281: 00         NOP
4282: 0F         RRCA
4283: 07         RLCA
4284: 3F         CCF
4285: 0C         INC         C
4286: 7C         LD           A,H
4287: 2B         DEC         HL
4288: FF         RST         0X38
4289: 68         LD           L,B
428A: FF         RST         0X38
428B: 4F         LD           C,A
428C: 7F         LD           A,A
428D: 10 3A      STOP       $3A
428F: 15         DEC         D
4290: 38 17      JR           C,$42A9
4292: 3F         CCF
4293: 18 3F      JR           $42D4
4295: 1F         RRA
4296: 1F         RRA
4297: 0F         RRCA
4298: 0F         RRCA
4299: 07         RLCA
429A: 07         RLCA
429B: 00         NOP
429C: 00         NOP
429D: 00         NOP
429E: 00         NOP
429F: 00         NOP
42A0: C0         RET         NZ
42A1: 00         NOP
42A2: E0 C0      LDFF00   ($C0),A
42A4: F0 E0      LD           A,($E0)
42A6: FC                              
42A7: 60         LD           H,B
42A8: FE 7C      CP           $7C
42AA: FF         RST         0X38
42AB: DE FE      SBC         $FE
42AD: 10 38      STOP       $38
42AF: D0         RET         NC
42B0: 7C         LD           A,H
42B1: B0         OR           B
42B2: FE 64      CP           $64
42B4: FF         RST         0X38
42B5: DE FF      SBC         $FF
42B7: F2                              
42B8: F2                              
42B9: E0 E0      LDFF00   ($E0),A
42BB: 00         NOP
42BC: 00         NOP
42BD: 00         NOP
42BE: 00         NOP
42BF: 00         NOP
42C0: 00         NOP
42C1: 00         NOP
42C2: 07         RLCA
42C3: 00         NOP
42C4: CF         RST         0X08
42C5: 07         RLCA
42C6: FF         RST         0X38
42C7: 4C         LD           C,H
42C8: FC                              
42C9: 6B         LD           L,E
42CA: 7F         LD           A,A
42CB: 28 3F      JR           Z,$430C
42CD: 0F         RRCA
42CE: 3F         CCF
42CF: 10 3A      STOP       $3A
42D1: 15         DEC         D
42D2: 3A         LD           A,(HLD)
42D3: 15         DEC         D
42D4: 3A         LD           A,(HLD)
42D5: 15         DEC         D
42D6: 38 17      JR           C,$42EF
42D8: 1F         RRA
42D9: 08 0F 07   LD           ($070F),SP
42DC: 07         RLCA
42DD: 00         NOP
42DE: 00         NOP
42DF: 00         NOP
42E0: 00         NOP
42E1: 00         NOP
42E2: C0         RET         NZ
42E3: 00         NOP
42E4: E7         RST         0X20
42E5: C0         RET         NZ
42E6: FF         RST         0X38
42E7: E6 FE      AND         $FE
42E9: 6C         LD           L,H
42EA: FC                              
42EB: 78         LD           A,B
42EC: F8 D0      LDHL       SP,$D0
42EE: F8 10      LDHL       SP,$10
42F0: 3A         LD           A,(HLD)
42F1: D0         RET         NC
42F2: 7F         LD           A,A
42F3: B2         OR           D
42F4: 7F         LD           A,A
42F5: A6         AND         (HL)
42F6: 7E         LD           A,(HL)
42F7: BC         CP           H
42F8: FC                              
42F9: 70         LD           (HL),B
42FA: F0 E0      LD           A,($E0)
42FC: E0 00      LDFF00   ($00),A
42FE: 00         NOP
42FF: 00         NOP
4300: 0F         RRCA
4301: 00         NOP
4302: 3F         CCF
4303: 0F         RRCA
4304: 7F         LD           A,A
4305: 33         INC         SP
4306: 7F         LD           A,A
4307: 2D         DEC         L
4308: 7F         LD           A,A
4309: 2D         DEC         L
430A: 3F         CCF
430B: 0D         DEC         C
430C: 3F         CCF
430D: 0E 3F      LD           C,$3F
430F: 1A         LD           A,(DE)
4310: 3F         CCF
4311: 1F         RRA
4312: 1F         RRA
4313: 0C         INC         C
4314: 0F         RRCA
4315: 03         INC         BC
4316: 1F         RRA
4317: 0B         DEC         BC
4318: 3F         CCF
4319: 0C         INC         C
431A: EF         RST         0X28
431B: 30 CF      JR           NC,$42EC
431D: 70         LD           (HL),B
431E: 70         LD           (HL),B
431F: 00         NOP
4320: C0         RET         NZ
4321: 00         NOP
4322: EC                              
4323: C0         RET         NZ
4324: FE EC      CP           $EC
4326: FF         RST         0X38
4327: EE FF      XOR         $FF
4329: F6 FF      OR           $FF
432B: F6 F9      OR           $F9
432D: F6 FE      OR           $FE
432F: F0 F0      LD           A,($F0)
4331: 20 60      JR           NZ,$4393
4333: 80         ADD         A,B
4334: F0 00      LD           A,($00)
4336: D0         RET         NC
4337: 20 30      JR           NZ,$4369
4339: C0         RET         NZ
433A: F8 00      LDHL       SP,$00
433C: F8 00      LDHL       SP,$00
433E: 00         NOP
433F: 00         NOP
4340: 1F         RRA
4341: 00         NOP
4342: 3F         CCF
4343: 1F         RRA
4344: 7F         LD           A,A
4345: 30 7F      JR           NC,$43C6
4347: 36 FF      LD           (HL),$FF
4349: 6F         LD           L,A
434A: FF         RST         0X38
434B: 5F         LD           E,A
434C: FF         RST         0X38
434D: 5F         LD           E,A
434E: 7F         LD           A,A
434F: 16 3F      LD           D,$3F
4351: 1F         RRA
4352: 1F         RRA
4353: 0E 0F      LD           C,$0F
4355: 01 1F 01   LD           BC,$011F
4358: 17         RLA
4359: 08 3F 06   LD           ($063F),SP
435C: 3D         DEC         A
435D: 0E 1F      LD           C,$1F
435F: 00         NOP
4360: 80         ADD         A,B
4361: 00         NOP
4362: F8 80      LDHL       SP,$80
4364: FC                              
4365: D8         RET         C
4366: FE EC      CP           $EC
4368: FE 74      CP           $74
436A: FA 74 FC   LD           A,($FC74)
436D: B0         OR           B
436E: F8 C0      LDHL       SP,$C0
4370: E8 90      ADD         SP,$90
4372: F0 60      LD           A,($60)
4374: F0 60      LD           A,($60)
4376: E0 80      LDFF00   ($80),A
4378: 90         SUB         B
4379: 60         LD           H,B
437A: F8 00      LDHL       SP,$00
437C: F8 00      LDHL       SP,$00
437E: 00         NOP
437F: 00         NOP
4380: 1F         RRA
4381: 00         NOP
4382: 3F         CCF
4383: 1F         RRA
4384: 7F         LD           A,A
4385: 30 7F      JR           NC,$4406
4387: 36 FF      LD           (HL),$FF
4389: 6F         LD           L,A
438A: FF         RST         0X38
438B: 5F         LD           E,A
438C: FF         RST         0X38
438D: 5F         LD           E,A
438E: 7F         LD           A,A
438F: 16 3F      LD           D,$3F
4391: 1F         RRA
4392: 1F         RRA
4393: 06 3F      LD           B,$3F
4395: 19         ADD         HL,DE
4396: 3F         CCF
4397: 19         ADD         HL,DE
4398: 1F         RRA
4399: 00         NOP
439A: 30 0F      JR           NC,$43AB
439C: 3F         CCF
439D: 00         NOP
439E: 00         NOP
439F: 00         NOP
43A0: 80         ADD         A,B
43A1: 00         NOP
43A2: F8 80      LDHL       SP,$80
43A4: FC                              
43A5: D8         RET         C
43A6: FE EC      CP           $EC
43A8: FE 74      CP           $74
43AA: FA 74 FC   LD           A,($FC74)
43AD: B0         OR           B
43AE: F8 D0      LDHL       SP,$D0
43B0: F0 A0      LD           A,($A0)
43B2: E0 00      LDFF00   ($00),A
43B4: E0 80      LDFF00   ($80),A
43B6: E0 80      LDFF00   ($80),A
43B8: 90         SUB         B
43B9: 60         LD           H,B
43BA: 78         LD           A,B
43BB: 80         ADD         A,B
43BC: F8 00      LDHL       SP,$00
43BE: 00         NOP
43BF: 00         NOP
43C0: 07         RLCA
43C1: 00         NOP
43C2: 6F         LD           L,A
43C3: 04         INC         B
43C4: FF         RST         0X38
43C5: 6B         LD           L,E
43C6: FF         RST         0X38
43C7: 67         LD           H,A
43C8: 7F         LD           A,A
43C9: 0B         DEC         BC
43CA: 7F         LD           A,A
43CB: 0F         RRCA
43CC: 7F         LD           A,A
43CD: 0D         DEC         C
43CE: 3F         CCF
43CF: 0D         DEC         C
43D0: 37         SCF
43D1: 0D         DEC         C
43D2: 1B         DEC         DE
43D3: 07         RLCA
43D4: 1F         RRA
43D5: 00         NOP
43D6: 0F         RRCA
43D7: 00         NOP
43D8: 1B         DEC         DE
43D9: 04         INC         B
43DA: 3C         INC         A
43DB: 03         INC         BC
43DC: 77         LD           (HL),A
43DD: 38 7F      JR           C,$445E
43DF: 00         NOP
43E0: C0         RET         NZ
43E1: 00         NOP
43E2: F0 C0      LD           A,($C0)
43E4: F8 70      LDHL       SP,$70
43E6: FC                              
43E7: B8         CP           B
43E8: FE 38      CP           $38
43EA: FF         RST         0X38
43EB: CA FF F6   JP           Z,$F6FF
43EE: FF         RST         0X38
43EF: E6 D6      AND         $D6
43F1: EC                              
43F2: BC         CP           H
43F3: C0         RET         NZ
43F4: F8 00      LDHL       SP,$00
43F6: FC                              
43F7: 00         NOP
43F8: FC                              
43F9: 30 7C      JR           NC,$4477
43FB: B0         OR           B
43FC: F8 00      LDHL       SP,$00
43FE: FC                              
43FF: 00         NOP
4400: 0F         RRCA
4401: 00         NOP
4402: 3F         CCF
4403: 00         NOP
4404: 47         LD           B,A
4405: 38 9B      JR           C,$43A2
4407: 7C         LD           A,H
4408: BD         CP           L
4409: 7E         LD           A,(HL)
440A: FF         RST         0X38
440B: 06 07      LD           B,$07
440D: 02         LD           (BC),A
440E: 03         INC         BC
440F: 00         NOP
4410: 01 00 00   LD           BC,$0000
4413: 00         NOP
4414: 01 00 03   LD           BC,$0300
4417: 01 02 01   LD           BC,$0102
441A: 03         INC         BC
441B: 00         NOP
441C: 07         RLCA
441D: 03         INC         BC
441E: 07         RLCA
441F: 00         NOP
4420: 81         ADD         A,C
4421: 00         NOP
4422: C7         RST         0X00
4423: 00         NOP
4424: FF         RST         0X38
4425: C7         RST         0X00
4426: FF         RST         0X38
4427: 4C         LD           C,H
4428: FD                              
4429: 7E         LD           A,(HL)
442A: FE A7      CP           $A7
442C: FE A7      CP           $A7
442E: FD                              
442F: AE         XOR         (HL)
4430: FB         EI
4431: FC                              
4432: FF         RST         0X38
4433: 70         LD           (HL),B
4434: FC                              
4435: 53         LD           D,E
4436: FC                              
4437: 73         LD           (HL),E
4438: 7E         LD           A,(HL)
4439: 81         ADD         A,C
443A: 24         INC         H
443B: C3 42 81   JP           $8142
443E: 81         ADD         A,C
443F: 00         NOP
4440: 01 00 01   LD           BC,$0100
4443: 00         NOP
4444: 00         NOP
4445: 00         NOP
4446: 01 00 03   LD           BC,$0300
4449: 00         NOP
444A: 07         RLCA
444B: 00         NOP
444C: 07         RLCA
444D: 00         NOP
444E: 0D         DEC         C
444F: 02         LD           (BC),A
4450: 0B         DEC         BC
4451: 06 0F      LD           B,$0F
4453: 06 0F      LD           B,$0F
4455: 06 0B      LD           B,$0B
4457: 06 07      LD           B,$07
4459: 02         LD           (BC),A
445A: 05         DEC         B
445B: 02         LD           (BC),A
445C: 03         INC         BC
445D: 00         NOP
445E: 01 00 C7   LD           BC,$C700
4461: 00         NOP
4462: EF         RST         0X28
4463: C7         RST         0X00
4464: FF         RST         0X38
4465: 4C         LD           C,H
4466: FD                              
4467: 7E         LD           A,(HL)
4468: FE A7      CP           $A7
446A: FE A7      CP           $A7
446C: FD                              
446D: AE         XOR         (HL)
446E: FB         EI
446F: FC                              
4470: FF         RST         0X38
4471: 70         LD           (HL),B
4472: FF         RST         0X38
4473: 50         LD           D,B
4474: FF         RST         0X38
4475: 70         LD           (HL),B
4476: 7E         LD           A,(HL)
4477: 81         ADD         A,C
4478: 99         SBC         C
4479: E7         RST         0X20
447A: DB                              
447B: 24         INC         H
447C: A5         AND         L
447D: C3 C3 00   JP           $00C3
4480: 03         INC         BC
4481: 00         NOP
4482: 3C         INC         A
4483: 03         INC         BC
4484: 79         LD           A,C
4485: 37         SCF
4486: DB                              
4487: 75         LD           (HL),L
4488: BB         CP           E
4489: 54         LD           D,H
448A: F9         LD           SP,HL
448B: 46         LD           B,(HL)
448C: AC         XOR         H
448D: 43         LD           B,E
448E: E7         RST         0X20
448F: 40         LD           B,B
4490: A7         AND         A
4491: 42         LD           B,D
4492: E7         RST         0X20
4493: 42         LD           B,D
4494: A2         AND         D
4495: 40         LD           B,B
4496: E0 40      LDFF00   ($40),A
4498: A0         AND         B
4499: 40         LD           B,B
449A: E0 40      LDFF00   ($40),A
449C: 90         SUB         B
449D: 60         LD           H,B
449E: 70         LD           (HL),B
449F: 00         NOP
44A0: 00         NOP
44A1: 00         NOP
44A2: 00         NOP
44A3: 00         NOP
44A4: 00         NOP
44A5: 00         NOP
44A6: 00         NOP
44A7: 00         NOP
44A8: 00         NOP
44A9: 00         NOP
44AA: 30 00      JR           NC,$44AC
44AC: 7B         LD           A,E
44AD: 30 DC      JR           NC,$448B
44AF: 73         LD           (HL),E
44B0: B9         CP           C
44B1: 57         LD           D,A
44B2: EB                              
44B3: 55         LD           D,L
44B4: AB         XOR         E
44B5: 54         LD           D,H
44B6: E9         JP           (HL)
44B7: 56         LD           D,(HL)
44B8: BC         CP           H
44B9: 43         LD           B,E
44BA: E7         RST         0X20
44BB: 40         LD           B,B
44BC: 97         SUB         A
44BD: 62         LD           H,D
44BE: 73         LD           (HL),E
44BF: 00         NOP
44C0: 01 00 0E   LD           BC,$0E00
44C3: 01 33 0D   LD           BC,$0D33
44C6: 5F         LD           E,A
44C7: 21 9F 6C   LD           HL,$6C9F
44CA: FF         RST         0X38
44CB: 1D         DEC         E
44CC: BF         CP           A
44CD: 5D         LD           E,L
44CE: BF         CP           A
44CF: 5E         LD           E,(HL)
44D0: BF         CP           A
44D1: 5D         LD           E,L
44D2: BF         CP           A
44D3: 43         LD           B,E
44D4: 7F         LD           A,A
44D5: 1B         DEC         DE
44D6: 4F         LD           C,A
44D7: 3D         DEC         A
44D8: 47         LD           B,A
44D9: 3E 21      LD           A,$21
44DB: 1E 19      LD           E,$19
44DD: 06 07      LD           B,$07
44DF: 00         NOP
44E0: E0 00      LDFF00   ($00),A
44E2: 10 E0      STOP       $E0
44E4: DC E0 F2   CALL       C,$F2E0
44E7: EC                              
44E8: F9         LD           SP,HL
44E9: 16 FD      LD           D,$FD
44EB: DA FD 9A   JP           C,$9AFD
44EE: FD                              
44EF: 6A         LD           L,D
44F0: FF         RST         0X38
44F1: E0 FD      LDFF00   ($FD),A
44F3: EE FD      XOR         $FD
44F5: DE F9      SBC         $F9
44F7: DE F2      SBC         $F2
44F9: 1C         INC         E
44FA: F4                              
44FB: E8 18      ADD         SP,$18
44FD: E0 E0      LDFF00   ($E0),A
44FF: 00         NOP
4500: 00         NOP
4501: 00         NOP
4502: 00         NOP
4503: 00         NOP
4504: 00         NOP
4505: 00         NOP
4506: 00         NOP
4507: 00         NOP
4508: 01 00 02   LD           BC,$0200
450B: 01 05 03   LD           BC,$0305
450E: 07         RLCA
450F: 02         LD           (BC),A
4510: 05         DEC         B
4511: 02         LD           (BC),A
4512: 07         RLCA
4513: 02         LD           (BC),A
4514: 05         DEC         B
4515: 02         LD           (BC),A
4516: 03         INC         BC
4517: 00         NOP
4518: 03         INC         BC
4519: 01 02 01   LD           BC,$0102
451C: 01 00 00   LD           BC,$0000
451F: 00         NOP
4520: 07         RLCA
4521: 00         NOP
4522: 0F         RRCA
4523: 00         NOP
4524: 0F         RRCA
4525: 01 3F 01   LD           BC,$013F
4528: FF         RST         0X38
4529: 07         RLCA
452A: BF         CP           A
452B: ED                              
452C: FF         RST         0X38
452D: 0D         DEC         C
452E: 7F         LD           A,A
452F: F7         RST         0X30
4530: FF         RST         0X38
4531: AB         XOR         E
4532: FF         RST         0X38
4533: FA 75 CB   LD           A,($CB75)
4536: FF         RST         0X38
4537: 00         NOP
4538: DB                              
4539: BD         CP           L
453A: CF         RST         0X08
453B: BB         CP           E
453C: C6 3B      ADD         $3B
453E: 3F         CCF
453F: 00         NOP
4540: F0 00      LD           A,($00)
4542: F8 00      LDHL       SP,$00
4544: F8 00      LDHL       SP,$00
4546: FE 00      CP           $00
4548: FF         RST         0X38
4549: C0         RET         NZ
454A: FF         RST         0X38
454B: 6C         LD           L,H
454C: FE 7C      CP           $7C
454E: FF         RST         0X38
454F: FC                              
4550: FF         RST         0X38
4551: F0 EE      LD           A,($EE)
4553: 70         LD           (HL),B
4554: D8         RET         C
4555: E0 F0      LDFF00   ($F0),A
4557: 00         NOP
4558: 60         LD           H,B
4559: 80         ADD         A,B
455A: 50         LD           D,B
455B: A0         AND         B
455C: F0 00      LD           A,($00)
455E: F0 00      LD           A,($00)
4560: 00         NOP
4561: 00         NOP
4562: 00         NOP
4563: 00         NOP
4564: 00         NOP
4565: 00         NOP
4566: 01 00 02   LD           BC,$0200
4569: 01 05 03   LD           BC,$0305
456C: 07         RLCA
456D: 02         LD           (BC),A
456E: 05         DEC         B
456F: 02         LD           (BC),A
4570: 07         RLCA
4571: 02         LD           (BC),A
4572: 05         DEC         B
4573: 02         LD           (BC),A
4574: 03         INC         BC
4575: 00         NOP
4576: 03         INC         BC
4577: 01 02 01   LD           BC,$0102
457A: 01 00 00   LD           BC,$0000
457D: 00         NOP
457E: 00         NOP
457F: 00         NOP
4580: 07         RLCA
4581: 00         NOP
4582: 0F         RRCA
4583: 00         NOP
4584: 1F         RRA
4585: 04         INC         B
4586: FF         RST         0X38
4587: 04         INC         B
4588: AF         XOR         A
4589: F7         RST         0X30
458A: FF         RST         0X38
458B: 05         DEC         B
458C: 7F         LD           A,A
458D: F5         PUSH       AF
458E: FF         RST         0X38
458F: AF         XOR         A
4590: FF         RST         0X38
4591: EF         RST         0X28
4592: 7F         LD           A,A
4593: CB FF      SET         1,E
4595: 07         RLCA
4596: F7         RST         0X30
4597: B8         CP           B
4598: D7         RST         0X10
4599: BB         CP           E
459A: 8F         ADC         A,A
459B: 77         LD           (HL),A
459C: 7F         LD           A,A
459D: 06 1F      LD           B,$1F
459F: 00         NOP
45A0: E0 00      LDFF00   ($00),A
45A2: F0 00      LD           A,($00)
45A4: F0 00      LD           A,($00)
45A6: F8 00      LDHL       SP,$00
45A8: FC                              
45A9: 00         NOP
45AA: FE B0      CP           $B0
45AC: FE B0      CP           $B0
45AE: FC                              
45AF: F0 DE      LD           A,($DE)
45B1: E0 BE      LDFF00   ($BE),A
45B3: C0         RET         NZ
45B4: 7C         LD           A,H
45B5: 80         ADD         A,B
45B6: E0 00      LDFF00   ($00),A
45B8: E0 00      LDFF00   ($00),A
45BA: 90         SUB         B
45BB: 60         LD           H,B
45BC: F0 00      LD           A,($00)
45BE: F0 00      LD           A,($00)
45C0: 0F         RRCA
45C1: 00         NOP
45C2: 1F         RRA
45C3: 00         NOP
45C4: 1F         RRA
45C5: 06 1F      LD           B,$1F
45C7: 07         RLCA
45C8: 0F         RRCA
45C9: 05         DEC         B
45CA: 1F         RRA
45CB: 05         DEC         B
45CC: 3F         CCF
45CD: 17         RLA
45CE: 3F         CCF
45CF: 1F         RRA
45D0: 3F         CCF
45D1: 1F         RRA
45D2: 1F         RRA
45D3: 04         INC         B
45D4: 1F         RRA
45D5: 07         RLCA
45D6: 3F         CCF
45D7: 1B         DEC         DE
45D8: 3F         CCF
45D9: 18 1F      JR           $45FA
45DB: 00         NOP
45DC: 39         ADD         HL,SP
45DD: 1E 3F      LD           E,$3F
45DF: 00         NOP
45E0: 78         LD           A,B
45E1: 00         NOP
45E2: FC                              
45E3: 00         NOP
45E4: FC                              
45E5: C0         RET         NZ
45E6: FC                              
45E7: C0         RET         NZ
45E8: F0 40      LD           A,($40)
45EA: F8 40      LDHL       SP,$40
45EC: FC                              
45ED: D8         RET         C
45EE: FC                              
45EF: F8 F8      LDHL       SP,$F8
45F1: F0 F0      LD           A,($F0)
45F3: C0         RET         NZ
45F4: F8 B0      LDHL       SP,$B0
45F6: F8 30      LDHL       SP,$30
45F8: F8 00      LDHL       SP,$00
45FA: F8 00      LDHL       SP,$00
45FC: BC         CP           H
45FD: 78         LD           A,B
45FE: FC                              
45FF: 00         NOP
4600: 00         NOP
4601: 00         NOP
4602: 00         NOP
4603: 00         NOP
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
4610: 00         NOP
4611: 00         NOP
4612: 00         NOP
4613: 00         NOP
4614: 00         NOP
4615: 00         NOP
4616: 07         RLCA
4617: 00         NOP
4618: 0F         RRCA
4619: 07         RLCA
461A: 1F         RRA
461B: 0F         RRCA
461C: 1F         RRA
461D: 0F         RRCA
461E: 7F         LD           A,A
461F: 0A         LD           A,(BC)
4620: 00         NOP
4621: 00         NOP
4622: 00         NOP
4623: 00         NOP
4624: 00         NOP
4625: 00         NOP
4626: 00         NOP
4627: 00         NOP
4628: 00         NOP
4629: 00         NOP
462A: 00         NOP
462B: 00         NOP
462C: 00         NOP
462D: 00         NOP
462E: 00         NOP
462F: 00         NOP
4630: 00         NOP
4631: 00         NOP
4632: 00         NOP
4633: 00         NOP
4634: 00         NOP
4635: 00         NOP
4636: 80         ADD         A,B
4637: 00         NOP
4638: C0         RET         NZ
4639: 80         ADD         A,B
463A: F0 C0      LD           A,($C0)
463C: F8 F0      LDHL       SP,$F0
463E: F8 D0      LDHL       SP,$D0
4640: 7F         LD           A,A
4641: 22         LD           (HLI),A
4642: EC                              
4643: 5F         LD           E,A
4644: E0 5F      LDFF00   ($5F),A
4646: FF         RST         0X38
4647: 60         LD           H,B
4648: FF         RST         0X38
4649: 7F         LD           A,A
464A: 77         LD           (HL),A
464B: 18 3F      JR           $468C
464D: 00         NOP
464E: 7F         LD           A,A
464F: 1B         DEC         DE
4650: 7F         LD           A,A
4651: 00         NOP
4652: FF         RST         0X38
4653: 66         LD           H,(HL)
4654: 88         ADC         A,B
4655: 77         LD           (HL),A
4656: 7F         LD           A,A
4657: 00         NOP
4658: EF         RST         0X28
4659: 73         LD           (HL),E
465A: 42         LD           B,D
465B: 3D         DEC         A
465C: 3F         CCF
465D: 00         NOP
465E: 00         NOP
465F: 00         NOP
4660: F0 A0      LD           A,($A0)
4662: F8 70      LDHL       SP,$70
4664: F8 70      LDHL       SP,$70
4666: F8 E0      LDHL       SP,$E0
4668: FC                              
4669: F0 FC      LD           A,($FC)
466B: E8 FC      ADD         SP,$FC
466D: 08 7C 88   LD           ($887C),SP
4670: 7C         LD           A,H
4671: 88         ADC         A,B
4672: FC                              
4673: 18 F6      JR           $466B
4675: 78         LD           A,B
4676: F2                              
4677: 6C         LD           L,H
4678: 56         LD           D,(HL)
4679: A8         XOR         B
467A: 0C         INC         C
467B: F0 F8      LD           A,($F8)
467D: 00         NOP
467E: 00         NOP
467F: 00         NOP
4680: 00         NOP
4681: 00         NOP
4682: 00         NOP
4683: 00         NOP
4684: 00         NOP
4685: 00         NOP
4686: 00         NOP
4687: 00         NOP
4688: 00         NOP
4689: 00         NOP
468A: 00         NOP
468B: 00         NOP
468C: 00         NOP
468D: 00         NOP
468E: 00         NOP
468F: 00         NOP
4690: 00         NOP
4691: 00         NOP
4692: 00         NOP
4693: 00         NOP
4694: 00         NOP
4695: 00         NOP
4696: 01 00 03   LD           BC,$0300
4699: 01 07 03   LD           BC,$0307
469C: 1F         RRA
469D: 02         LD           (BC),A
469E: 3F         CCF
469F: 18 00      JR           $46A1
46A1: 00         NOP
46A2: 00         NOP
46A3: 00         NOP
46A4: 00         NOP
46A5: 00         NOP
46A6: 00         NOP
46A7: 00         NOP
46A8: 00         NOP
46A9: 00         NOP
46AA: 00         NOP
46AB: 00         NOP
46AC: 00         NOP
46AD: 00         NOP
46AE: 00         NOP
46AF: 00         NOP
46B0: 00         NOP
46B1: 00         NOP
46B2: 00         NOP
46B3: 00         NOP
46B4: 00         NOP
46B5: 00         NOP
46B6: E0 00      LDFF00   ($00),A
46B8: F0 E0      LD           A,($E0)
46BA: FC                              
46BB: F0 FE      LD           A,($FE)
46BD: BC         CP           H
46BE: FE A4      CP           $A4
46C0: 3B         DEC         SP
46C1: 17         RLA
46C2: 78         LD           A,B
46C3: 37         SCF
46C4: 7F         LD           A,A
46C5: 38 7F      JR           C,$4746
46C7: 3F         CCF
46C8: 3B         DEC         SP
46C9: 0C         INC         C
46CA: 1F         RRA
46CB: 00         NOP
46CC: 3F         CCF
46CD: 0C         INC         C
46CE: 3F         CCF
46CF: 00         NOP
46D0: 7F         LD           A,A
46D1: 33         INC         SP
46D2: 44         LD           B,H
46D3: 3B         DEC         SP
46D4: 3F         CCF
46D5: 00         NOP
46D6: 7F         LD           A,A
46D7: 31 46 39   LD           SP,$3946
46DA: 21 1E 1F   LD           HL,$1F1E
46DD: 00         NOP
46DE: 00         NOP
46DF: 00         NOP
46E0: 3C         INC         A
46E1: D8         RET         C
46E2: 3E DC      LD           A,$DC
46E4: FE 38      CP           $38
46E6: FE FC      CP           $FC
46E8: FF         RST         0X38
46E9: 78         LD           A,B
46EA: FF         RST         0X38
46EB: 02         LD           (BC),A
46EC: DF         RST         0X18
46ED: E2         LDFF00   (C),A
46EE: DF         RST         0X18
46EF: 22         LD           (HLI),A
46F0: FF         RST         0X38
46F1: 02         LD           (BC),A
46F2: 7F         LD           A,A
46F3: BE         CP           (HL)
46F4: FF         RST         0X38
46F5: 3E EA      LD           A,$EA
46F7: 94         SUB         H
46F8: 29         ADD         HL,HL
46F9: D6 03      SUB         $03
46FB: FC                              
46FC: FE 00      CP           $00
46FE: 00         NOP
46FF: 00         NOP
4700: 07         RLCA
4701: 00         NOP
4702: 3F         CCF
4703: 00         NOP
4704: 7F         LD           A,A
4705: 02         LD           (BC),A
4706: FF         RST         0X38
4707: 07         RLCA
4708: FF         RST         0X38
4709: 0F         RRCA
470A: FF         RST         0X38
470B: 2B         DEC         HL
470C: FF         RST         0X38
470D: 3B         DEC         SP
470E: D3                              
470F: 3F         CCF
4710: 7F         LD           A,A
4711: 1F         RRA
4712: 2F         CPL
4713: 1E 37      LD           E,$37
4715: 0F         RRCA
4716: 2C         INC         L
4717: 13         INC         DE
4718: 7F         LD           A,A
4719: 34         INC         (HL)
471A: 73         LD           (HL),E
471B: 2F         CPL
471C: 30 0F      JR           NC,$472D
471E: 3F         CCF
471F: 00         NOP
4720: E0 00      LDFF00   ($00),A
4722: FC                              
4723: 00         NOP
4724: FE 80      CP           $80
4726: FF         RST         0X38
4727: C0         RET         NZ
4728: FF         RST         0X38
4729: E0 FF      LDFF00   ($FF),A
472B: AC         XOR         H
472C: FF         RST         0X38
472D: BC         CP           H
472E: 9A         SBC         D
472F: FC                              
4730: FF         RST         0X38
4731: FA F5 FA   LD           A,($FAF5)
4734: EE F0      XOR         $F0
4736: 77         LD           (HL),A
4737: 88         ADC         A,B
4738: FF         RST         0X38
4739: 58         LD           E,B
473A: BE         CP           (HL)
473B: D8         RET         C
473C: 1C         INC         E
473D: E0 FC      LDFF00   ($FC),A
473F: 00         NOP
4740: 07         RLCA
4741: 00         NOP
4742: 3F         CCF
4743: 00         NOP
4744: 7F         LD           A,A
4745: 00         NOP
4746: FF         RST         0X38
4747: 00         NOP
4748: FF         RST         0X38
4749: 00         NOP
474A: FF         RST         0X38
474B: 00         NOP
474C: FF         RST         0X38
474D: 00         NOP
474E: 7F         LD           A,A
474F: 01 7E 03   LD           BC,$037E
4752: 3D         DEC         A
4753: 02         LD           (BC),A
4754: 3F         CCF
4755: 00         NOP
4756: 7F         LD           A,A
4757: 20 77      JR           NZ,$47D0
4759: 28 23      JR           Z,$477E
475B: 1C         INC         E
475C: 23         INC         HL
475D: 1F         RRA
475E: 3F         CCF
475F: 00         NOP
4760: E0 00      LDFF00   ($00),A
4762: 7C         LD           A,H
4763: 80         ADD         A,B
4764: 7E         LD           A,(HL)
4765: 80         ADD         A,B
4766: FF         RST         0X38
4767: 00         NOP
4768: FF         RST         0X38
4769: 00         NOP
476A: FF         RST         0X38
476B: 00         NOP
476C: FF         RST         0X38
476D: 00         NOP
476E: FE C0      CP           $C0
4770: 1E E0      LD           E,$E0
4772: FC                              
4773: 00         NOP
4774: 38 C0      JR           C,$4736
4776: FC                              
4777: 08 FC 08   LD           ($08FC),SP
477A: EC                              
477B: 10 E4      STOP       $E4
477D: F8 FC      LDHL       SP,$FC
477F: 00         NOP
4780: 1F         RRA
4781: 00         NOP
4782: 3F         CCF
4783: 00         NOP
4784: 3F         CCF
4785: 0C         INC         C
4786: 3F         CCF
4787: 1E 3F      LD           E,$3F
4789: 1F         RRA
478A: 3F         CCF
478B: 17         RLA
478C: 7F         LD           A,A
478D: 37         SCF
478E: 73         LD           (HL),E
478F: 3F         CCF
4790: 7F         LD           A,A
4791: 3F         CCF
4792: 7F         LD           A,A
4793: 3F         CCF
4794: 3F         CCF
4795: 1F         RRA
4796: 11 0E 0F   LD           DE,$0F0E
4799: 01 1F 0B   LD           BC,$0B1F
479C: 16 0B      LD           D,$0B
479E: 0F         RRCA
479F: 00         NOP
47A0: C0         RET         NZ
47A1: 00         NOP
47A2: F8 00      LDHL       SP,$00
47A4: FC                              
47A5: 00         NOP
47A6: FE 00      CP           $00
47A8: AE         XOR         (HL)
47A9: 70         LD           (HL),B
47AA: FE 70      CP           $70
47AC: DE F0      SBC         $F0
47AE: EC                              
47AF: F0 BE      LD           A,($BE)
47B1: C4 B7 C8   CALL       NZ,$C8B7
47B4: 7F         LD           A,A
47B5: 80         ADD         A,B
47B6: DF         RST         0X18
47B7: 20 5E      JR           NZ,$4817
47B9: A0         AND         B
47BA: 48         LD           C,B
47BB: B0         OR           B
47BC: 84         ADD         A,H
47BD: 78         LD           A,B
47BE: FC                              
47BF: 00         NOP
47C0: 0F         RRCA
47C1: 00         NOP
47C2: 3F         CCF
47C3: 00         NOP
47C4: 7F         LD           A,A
47C5: 0A         LD           A,(BC)
47C6: 7F         LD           A,A
47C7: 1F         RRA
47C8: 7F         LD           A,A
47C9: 1F         RRA
47CA: 3F         CCF
47CB: 1B         DEC         DE
47CC: 7F         LD           A,A
47CD: 3B         DEC         SP
47CE: 79         LD           A,C
47CF: 3F         CCF
47D0: 7F         LD           A,A
47D1: 3F         CCF
47D2: 7F         LD           A,A
47D3: 1F         RRA
47D4: 2F         CPL
47D5: 1F         RRA
47D6: 10 0F      STOP       $0F
47D8: 0F         RRCA
47D9: 00         NOP
47DA: 1D         DEC         E
47DB: 0E 11      LD           C,$11
47DD: 0E 0F      LD           C,$0F
47DF: 00         NOP
47E0: E0 00      LDFF00   ($00),A
47E2: FC                              
47E3: 00         NOP
47E4: FE 00      CP           $00
47E6: FF         RST         0X38
47E7: 00         NOP
47E8: D7         RST         0X10
47E9: B8         CP           B
47EA: FF         RST         0X38
47EB: B8         CP           B
47EC: EF         RST         0X28
47ED: F8 F6      LDHL       SP,$F6
47EF: F8 DC      LDHL       SP,$DC
47F1: E0 DE      LDFF00   ($DE),A
47F3: E4                              
47F4: B6         OR           (HL)
47F5: C8         RET         Z
47F6: FE 00      CP           $00
47F8: BC         CP           H
47F9: C0         RET         NZ
47FA: E8 D0      ADD         SP,$D0
47FC: 64         LD           H,H
47FD: D8         RET         C
47FE: FC                              
47FF: 00         NOP
4800: 00         NOP
4801: 00         NOP
4802: 00         NOP
4803: 00         NOP
4804: 00         NOP
4805: 00         NOP
4806: 00         NOP
4807: 00         NOP
4808: 00         NOP
4809: 00         NOP
480A: 03         INC         BC
480B: 04         INC         B
480C: 0F         RRCA
480D: 00         NOP
480E: 0F         RRCA
480F: 10 1F      STOP       $1F
4811: 00         NOP
4812: 1F         RRA
4813: 00         NOP
4814: 1F         RRA
4815: 08 1B 0E   LD           ($0E1B),SP
4818: 1E 03      LD           E,$03
481A: 0F         RRCA
481B: 00         NOP
481C: 03         INC         BC
481D: 04         INC         B
481E: 00         NOP
481F: 00         NOP
4820: 00         NOP
4821: 00         NOP
4822: 00         NOP
4823: 00         NOP
4824: 00         NOP
4825: 00         NOP
4826: 00         NOP
4827: 00         NOP
4828: 00         NOP
4829: 00         NOP
482A: C0         RET         NZ
482B: 20 70      JR           NZ,$489D
482D: 80         ADD         A,B
482E: F0 08      LD           A,($08)
4830: 58         LD           E,B
4831: E0 F8      LDFF00   ($F8),A
4833: A0         AND         B
4834: 58         LD           E,B
4835: E0 F8      LDFF00   ($F8),A
4837: 00         NOP
4838: F0 08      LD           A,($08)
483A: F0 00      LD           A,($00)
483C: C0         RET         NZ
483D: 20 00      JR           NZ,$483F
483F: 00         NOP
4840: 00         NOP
4841: 00         NOP
4842: 00         NOP
4843: 00         NOP
4844: 00         NOP
4845: 00         NOP
4846: 00         NOP
4847: 00         NOP
4848: 00         NOP
4849: 00         NOP
484A: 03         INC         BC
484B: 04         INC         B
484C: 0F         RRCA
484D: 00         NOP
484E: 0F         RRCA
484F: 10 1F      STOP       $1F
4851: 0C         INC         C
4852: 1F         RRA
4853: 0B         DEC         BC
4854: 0F         RRCA
4855: 02         LD           (BC),A
4856: 17         RLA
4857: 08 10 0F   LD           ($0F10),SP
485A: 0F         RRCA
485B: 00         NOP
485C: 03         INC         BC
485D: 04         INC         B
485E: 00         NOP
485F: 00         NOP
4860: 00         NOP
4861: 00         NOP
4862: 00         NOP
4863: 00         NOP
4864: 00         NOP
4865: 00         NOP
4866: 00         NOP
4867: 00         NOP
4868: 00         NOP
4869: 00         NOP
486A: C0         RET         NZ
486B: 20 70      JR           NZ,$48DD
486D: 80         ADD         A,B
486E: F0 08      LD           A,($08)
4870: A8         XOR         B
4871: 70         LD           (HL),B
4872: F8 50      LDHL       SP,$50
4874: A8         XOR         B
4875: F0 78      LD           A,($78)
4877: 80         ADD         A,B
4878: F0 08      LD           A,($08)
487A: F0 00      LD           A,($00)
487C: C0         RET         NZ
487D: 20 00      JR           NZ,$487F
487F: 00         NOP
4880: 00         NOP
4881: 00         NOP
4882: 01 00 01   LD           BC,$0100
4885: 00         NOP
4886: 03         INC         BC
4887: 01 03 01   LD           BC,$0103
488A: 0F         RRCA
488B: 00         NOP
488C: 1E 01      LD           E,$01
488E: 1F         RRA
488F: 20 3E      JR           NZ,$48CF
4891: 01 3F 01   LD           BC,$013F
4894: 3E 11      LD           A,$11
4896: 37         SCF
4897: 1C         INC         E
4898: 3D         DEC         A
4899: 06 1F      LD           B,$1F
489B: 00         NOP
489C: 07         RLCA
489D: 08 00 00   LD           ($0000),SP
48A0: C0         RET         NZ
48A1: 00         NOP
48A2: E6 C0      AND         $C0
48A4: EF         RST         0X28
48A5: C6 FF      ADD         $FF
48A7: 8E         ADC         A,(HL)
48A8: DF         RST         0X18
48A9: 6E         LD           L,(HL)
48AA: 9F         SBC         A
48AB: 66         LD           H,(HL)
48AC: FF         RST         0X38
48AD: 0E FF      LD           C,$FF
48AF: 0E BF      LD           C,$BF
48B1: C6 F6      ADD         $F6
48B3: 40         LD           B,B
48B4: B0         OR           B
48B5: C0         RET         NZ
48B6: F0 00      LD           A,($00)
48B8: E0 10      LDFF00   ($10),A
48BA: E0 00      LDFF00   ($00),A
48BC: 80         ADD         A,B
48BD: 40         LD           B,B
48BE: 00         NOP
48BF: 00         NOP
48C0: 00         NOP
48C1: 00         NOP
48C2: 00         NOP
48C3: 00         NOP
48C4: 01 00 01   LD           BC,$0100
48C7: 00         NOP
48C8: 03         INC         BC
48C9: 01 0F 00   LD           BC,$000F
48CC: 1E 01      LD           E,$01
48CE: 1F         RRA
48CF: 20 3F      JR           NZ,$4910
48D1: 18 3F      JR           $4912
48D3: 16 1F      LD           D,$1F
48D5: 05         DEC         B
48D6: 2E 11      LD           L,$11
48D8: 21 1E 1F   LD           HL,$1F1E
48DB: 00         NOP
48DC: 07         RLCA
48DD: 08 00 00   LD           ($0000),SP
48E0: 00         NOP
48E1: 00         NOP
48E2: C0         RET         NZ
48E3: 00         NOP
48E4: E6 C0      AND         $C0
48E6: EF         RST         0X28
48E7: C6 FF      ADD         $FF
48E9: 8E         ADC         A,(HL)
48EA: DF         RST         0X18
48EB: 6E         LD           L,(HL)
48EC: DF         RST         0X18
48ED: 26 FF      LD           H,$FF
48EF: 0E 5F      LD           C,$5F
48F1: EE FF      XOR         $FF
48F3: A6         AND         (HL)
48F4: 56         LD           D,(HL)
48F5: E0 F0      LDFF00   ($F0),A
48F7: 00         NOP
48F8: E0 10      LDFF00   ($10),A
48FA: E0 00      LDFF00   ($00),A
48FC: 80         ADD         A,B
48FD: 40         LD           B,B
48FE: 00         NOP
48FF: 00         NOP
4900: 3C         INC         A
4901: 00         NOP
4902: 3E 1C      LD           A,$1C
4904: 3F         CCF
4905: 16 3F      LD           D,$3F
4907: 18 3F      JR           $4948
4909: 10 17      STOP       $17
490B: 08 1F 00   LD           ($001F),SP
490E: 7F         LD           A,A
490F: 01 BF 41   LD           BC,$41BF
4912: FF         RST         0X38
4913: 01 FF 03   LD           BC,$03FF
4916: 7F         LD           A,A
4917: 0B         DEC         BC
4918: 3F         CCF
4919: 0F         RRCA
491A: 7F         LD           A,A
491B: 07         RLCA
491C: FF         RST         0X38
491D: 13         INC         DE
491E: FF         RST         0X38
491F: 00         NOP
4920: 1F         RRA
4921: 00         NOP
4922: 3F         CCF
4923: 1E FF      LD           E,$FF
4925: 26 FF      LD           H,$FF
4927: 9E         SBC         (HL)
4928: DE 3C      SBC         $3C
492A: EE 1C      XOR         $1C
492C: 7C         LD           A,H
492D: 80         ADD         A,B
492E: FC                              
492F: 80         ADD         A,B
4930: FE 80      CP           $80
4932: FF         RST         0X38
4933: 80         ADD         A,B
4934: FF         RST         0X38
4935: 50         LD           D,B
4936: FF         RST         0X38
4937: 70         LD           (HL),B
4938: EE F0      XOR         $F0
493A: FC                              
493B: C0         RET         NZ
493C: FE 88      CP           $88
493E: FF         RST         0X38
493F: 00         NOP
4940: 0E 00      LD           C,$00
4942: 0F         RRCA
4943: 06 0F      LD           B,$0F
4945: 04         INC         B
4946: 0F         RRCA
4947: 01 1F 00   LD           BC,$001F
494A: 2F         CPL
494B: 10 3B      STOP       $3B
494D: 04         INC         B
494E: 3F         CCF
494F: 04         INC         B
4950: 7F         LD           A,A
4951: 04         INC         B
4952: 7F         LD           A,A
4953: 06 7F      LD           B,$7F
4955: 05         DEC         B
4956: 3F         CCF
4957: 0D         DEC         C
4958: 3F         CCF
4959: 0F         RRCA
495A: 3F         CCF
495B: 0F         RRCA
495C: 7F         LD           A,A
495D: 07         RLCA
495E: FF         RST         0X38
495F: 00         NOP
4960: 78         LD           A,B
4961: 00         NOP
4962: FC                              
4963: 78         LD           A,B
4964: FC                              
4965: 48         LD           C,B
4966: FC                              
4967: 38 F8      JR           C,$4961
4969: 70         LD           (HL),B
496A: F8 30      LDHL       SP,$30
496C: FC                              
496D: 00         NOP
496E: FE 00      CP           $00
4970: FF         RST         0X38
4971: 00         NOP
4972: FF         RST         0X38
4973: 00         NOP
4974: BF         CP           A
4975: 60         LD           H,B
4976: FE E0      CP           $E0
4978: DC E0 FE   CALL       C,$FEE0
497B: 80         ADD         A,B
497C: FF         RST         0X38
497D: 20 FF      JR           NZ,$497E
497F: 00         NOP
4980: FC                              
4981: 0B         DEC         BC
4982: 77         LD           (HL),A
4983: 18 3F      JR           $49C4
4985: 13         INC         DE
4986: 1F         RRA
4987: 05         DEC         B
4988: 0F         RRCA
4989: 06 0F      LD           B,$0F
498B: 04         INC         B
498C: 0E 00      LD           C,$00
498E: 00         NOP
498F: 00         NOP
4990: 00         NOP
4991: 00         NOP
4992: 00         NOP
4993: 00         NOP
4994: 00         NOP
4995: 00         NOP
4996: 00         NOP
4997: 00         NOP
4998: 00         NOP
4999: 00         NOP
499A: 00         NOP
499B: 00         NOP
499C: 00         NOP
499D: 00         NOP
499E: 00         NOP
499F: 00         NOP
49A0: FF         RST         0X38
49A1: 40         LD           B,B
49A2: BE         CP           (HL)
49A3: 60         LD           H,B
49A4: D8         RET         C
49A5: 30 F0      JR           NC,$4997
49A7: 80         ADD         A,B
49A8: E0 C0      LDFF00   ($C0),A
49AA: C0         RET         NZ
49AB: 00         NOP
49AC: 00         NOP
49AD: 00         NOP
49AE: 00         NOP
49AF: 00         NOP
49B0: 00         NOP
49B1: 00         NOP
49B2: 00         NOP
49B3: 00         NOP
49B4: 00         NOP
49B5: 00         NOP
49B6: 00         NOP
49B7: 00         NOP
49B8: 00         NOP
49B9: 00         NOP
49BA: 00         NOP
49BB: 00         NOP
49BC: 00         NOP
49BD: 00         NOP
49BE: 00         NOP
49BF: 00         NOP
49C0: 00         NOP
49C1: FF         RST         0X38
49C2: 00         NOP
49C3: FF         RST         0X38
49C4: 24         INC         H
49C5: FF         RST         0X38
49C6: 18 FF      JR           $49C7
49C8: 18 FF      JR           $49C9
49CA: 24         INC         H
49CB: FF         RST         0X38
49CC: 00         NOP
49CD: FF         RST         0X38
49CE: 00         NOP
49CF: FF         RST         0X38
49D0: 00         NOP
49D1: FF         RST         0X38
49D2: 00         NOP
49D3: FF         RST         0X38
49D4: 24         INC         H
49D5: FF         RST         0X38
49D6: 18 FF      JR           $49D7
49D8: 18 FF      JR           $49D9
49DA: 24         INC         H
49DB: FF         RST         0X38
49DC: 00         NOP
49DD: FF         RST         0X38
49DE: 00         NOP
49DF: FF         RST         0X38
49E0: 00         NOP
49E1: FF         RST         0X38
49E2: 00         NOP
49E3: FF         RST         0X38
49E4: 24         INC         H
49E5: FF         RST         0X38
49E6: 18 FF      JR           $49E7
49E8: 18 FF      JR           $49E9
49EA: 24         INC         H
49EB: FF         RST         0X38
49EC: 00         NOP
49ED: FF         RST         0X38
49EE: 00         NOP
49EF: FF         RST         0X38
49F0: 00         NOP
49F1: FF         RST         0X38
49F2: 00         NOP
49F3: FF         RST         0X38
49F4: 24         INC         H
49F5: FF         RST         0X38
49F6: 18 FF      JR           $49F7
49F8: 18 FF      JR           $49F9
49FA: 24         INC         H
49FB: FF         RST         0X38
49FC: 00         NOP
49FD: FF         RST         0X38
49FE: 00         NOP
49FF: FF         RST         0X38
4A00: 00         NOP
4A01: 00         NOP
4A02: 01 00 07   LD           BC,$0700
4A05: 01 0F 06   LD           BC,$060F
4A08: 1F         RRA
4A09: 0E 1F      LD           C,$1F
4A0B: 0D         DEC         C
4A0C: 3F         CCF
4A0D: 1B         DEC         DE
4A0E: 2F         CPL
4A0F: 1B         DEC         DE
4A10: 37         SCF
4A11: 0B         DEC         BC
4A12: 7D         LD           A,L
4A13: 43         LD           B,E
4A14: 74         LD           (HL),H
4A15: 4B         LD           C,E
4A16: 77         LD           (HL),A
4A17: 68         LD           L,B
4A18: 3E 21      LD           A,$21
4A1A: 3E 31      LD           A,$31
4A1C: 1F         RRA
4A1D: 1C         INC         E
4A1E: 07         RLCA
4A1F: 07         RLCA
4A20: 0E 00      LD           C,$00
4A22: 1F         RRA
4A23: 0E 7F      LD           C,$7F
4A25: 0D         DEC         C
4A26: FF         RST         0X38
4A27: 75         LD           (HL),L
4A28: FD                              
4A29: 7B         LD           A,E
4A2A: FC                              
4A2B: 7B         LD           A,E
4A2C: FE 21      CP           $21
4A2E: 7F         LD           A,A
4A2F: 1C         INC         E
4A30: 7F         LD           A,A
4A31: 3D         DEC         A
4A32: FF         RST         0X38
4A33: BB         CP           E
4A34: FF         RST         0X38
4A35: 83         ADD         A,E
4A36: F7         RST         0X30
4A37: C9         RET
4A38: 7F         LD           A,A
4A39: 60         LD           H,B
4A3A: 3E 31      LD           A,$31
4A3C: 1F         RRA
4A3D: 1C         INC         E
4A3E: 07         RLCA
4A3F: 07         RLCA
4A40: 07         RLCA
4A41: 00         NOP
4A42: 3F         CCF
4A43: 01 7F 12   LD           BC,$127F
4A46: 7F         LD           A,A
4A47: 3A         LD           A,(HLD)
4A48: 7F         LD           A,A
4A49: 09         ADD         HL,BC
4A4A: 3F         CCF
4A4B: 18 3F      JR           $4A8C
4A4D: 08 7F 08   LD           ($087F),SP
4A50: FF         RST         0X38
4A51: 19         ADD         HL,DE
4A52: FB         EI
4A53: 77         LD           (HL),A
4A54: F3         DI
4A55: 6F         LD           L,A
4A56: 6F         LD           L,A
4A57: 1B         DEC         DE
4A58: 2F         CPL
4A59: 1C         INC         E
4A5A: 17         RLA
4A5B: 0F         RRCA
4A5C: 0F         RRCA
4A5D: 00         NOP
4A5E: 00         NOP
4A5F: 00         NOP
4A60: FC                              
4A61: 00         NOP
4A62: E2         LDFF00   (C),A
4A63: 9C         SBC         H
4A64: FD                              
4A65: 42         LD           B,D
4A66: FF         RST         0X38
4A67: 40         LD           B,B
4A68: DF         RST         0X18
4A69: A0         AND         B
4A6A: E8 10      ADD         SP,$10
4A6C: E8 10      ADD         SP,$10
4A6E: F8 00      LDHL       SP,$00
4A70: FF         RST         0X38
4A71: C0         RET         NZ
4A72: FF         RST         0X38
4A73: C6 FF      ADD         $FF
4A75: 86         ADD         A,(HL)
4A76: 9E         SBC         (HL)
4A77: 6C         LD           L,H
4A78: BC         CP           H
4A79: D8         RET         C
4A7A: 7C         LD           A,H
4A7B: 98         SBC         B
4A7C: 9C         SBC         H
4A7D: 08 0C 00   LD           ($000C),SP
4A80: 38 00      JR           C,$4A82
4A82: 58         LD           E,B
4A83: 20 B8      JR           NZ,$4A3D
4A85: 40         LD           B,B
4A86: BF         CP           A
4A87: 40         LD           B,B
4A88: B9         CP           C
4A89: 46         LD           B,(HL)
4A8A: F7         RST         0X30
4A8B: 08 FF 30   LD           ($30FF),SP
4A8E: FF         RST         0X38
4A8F: 48         LD           C,B
4A90: FF         RST         0X38
4A91: 48         LD           C,B
4A92: FF         RST         0X38
4A93: 30 FF      JR           NC,$4A94
4A95: 00         NOP
4A96: 7F         LD           A,A
4A97: 1F         RRA
4A98: 7F         LD           A,A
4A99: 35         DEC         (HL)
4A9A: 7F         LD           A,A
4A9B: 13         INC         DE
4A9C: 3E 03      LD           A,$03
4A9E: 03         INC         BC
4A9F: 00         NOP
4AA0: E0 00      LDFF00   ($00),A
4AA2: F0 60      LD           A,($60)
4AA4: FF         RST         0X38
4AA5: 70         LD           (HL),B
4AA6: FF         RST         0X38
4AA7: 1E FE      LD           E,$FE
4AA9: 0C         INC         C
4AAA: EC                              
4AAB: 10 E4      STOP       $E4
4AAD: D8         RET         C
4AAE: FA EC FE   LD           A,($FEEC)
4AB1: F4                              
4AB2: FE 74      CP           $74
4AB4: 9E         SBC         (HL)
4AB5: 6C         LD           L,H
4AB6: DA 3C D4   JP           C,$D43C
4AB9: B8         CP           B
4ABA: 48         LD           C,B
4ABB: B0         OR           B
4ABC: F0 00      LD           A,($00)
4ABE: 80         ADD         A,B
4ABF: 00         NOP
4AC0: 00         NOP
4AC1: 00         NOP
4AC2: 00         NOP
4AC3: 00         NOP
4AC4: 00         NOP
4AC5: 00         NOP
4AC6: 00         NOP
4AC7: 00         NOP
4AC8: 00         NOP
4AC9: 00         NOP
4ACA: 00         NOP
4ACB: 00         NOP
4ACC: 00         NOP
4ACD: 00         NOP
4ACE: 0E 00      LD           C,$00
4AD0: 12         LD           (DE),A
4AD1: 0C         INC         C
4AD2: 2E 10      LD           L,$10
4AD4: 2E 10      LD           L,$10
4AD6: 5E         LD           E,(HL)
4AD7: 20 5E      JR           NZ,$4B37
4AD9: 20 FF      JR           NZ,$4ADA
4ADB: 81         ADD         A,C
4ADC: FF         RST         0X38
4ADD: C3 7E 7E   JP           $7E7E
4AE0: 00         NOP
4AE1: 00         NOP
4AE2: 00         NOP
4AE3: 00         NOP
4AE4: 00         NOP
4AE5: 00         NOP
4AE6: 00         NOP
4AE7: 00         NOP
4AE8: 00         NOP
4AE9: 00         NOP
4AEA: 00         NOP
4AEB: 00         NOP
4AEC: 00         NOP
4AED: 00         NOP
4AEE: 18 00      JR           $4AF0
4AF0: 2C         INC         L
4AF1: 10 2C      STOP       $2C
4AF3: 10 2C      STOP       $2C
4AF5: 10 6E      STOP       $6E
4AF7: 52         LD           D,D
4AF8: EF         RST         0X28
4AF9: 91         SUB         C
4AFA: FF         RST         0X38
4AFB: 81         ADD         A,C
4AFC: FF         RST         0X38
4AFD: C3 7E 7E   JP           $7E7E
4B00: 0E 00      LD           C,$00
4B02: 1D         DEC         E
4B03: 0E 20      LD           C,$20
4B05: 1F         RRA
4B06: 20 1F      JR           NZ,$4B27
4B08: 25         DEC         H
4B09: 1A         LD           A,(DE)
4B0A: 1F         RRA
4B0B: 05         DEC         B
4B0C: 1F         RRA
4B0D: 0F         RRCA
4B0E: 1F         RRA
4B0F: 02         LD           (BC),A
4B10: 7F         LD           A,A
4B11: 1D         DEC         E
4B12: BF         CP           A
4B13: 55         LD           D,L
4B14: BF         CP           A
4B15: 5D         LD           E,L
4B16: 9F         SBC         A
4B17: 62         LD           H,D
4B18: BF         CP           A
4B19: 48         LD           C,B
4B1A: B7         OR           A
4B1B: 4F         LD           C,A
4B1C: AF         XOR         A
4B1D: 50         LD           D,B
4B1E: EF         RST         0X28
4B1F: 1C         INC         E
4B20: F8 00      LDHL       SP,$00
4B22: 64         LD           H,H
4B23: F8 02      LDHL       SP,$02
4B25: FC                              
4B26: 02         LD           (BC),A
4B27: FC                              
4B28: 82         ADD         A,D
4B29: 7C         LD           A,H
4B2A: C4 B8 E8   CALL       NZ,$E8B8
4B2D: D0         RET         NC
4B2E: FC                              
4B2F: 20 FE      JR           NZ,$4B2F
4B31: C8         RET         Z
4B32: FD                              
4B33: 5A         LD           E,D
4B34: F5         PUSH       AF
4B35: DA F9 26   JP           C,$26F9
4B38: DD                              
4B39: E2         LDFF00   (C),A
4B3A: BD         CP           L
4B3B: C2 E5 1A   JP           NZ,$1AE5
4B3E: F7         RST         0X30
4B3F: 38 7F      JR           C,$4BC0
4B41: 0C         INC         C
4B42: 6F         LD           L,A
4B43: 33         INC         SP
4B44: 7F         LD           A,A
4B45: 3F         CCF
4B46: 7F         LD           A,A
4B47: 29         ADD         HL,HL
4B48: 7F         LD           A,A
4B49: 3F         CCF
4B4A: 7F         LD           A,A
4B4B: 22         LD           (HLI),A
4B4C: 7F         LD           A,A
4B4D: 3F         CCF
4B4E: 7F         LD           A,A
4B4F: 25         DEC         H
4B50: 7F         LD           A,A
4B51: 3F         CCF
4B52: 7F         LD           A,A
4B53: 00         NOP
4B54: 00         NOP
4B55: 00         NOP
4B56: 00         NOP
4B57: 00         NOP
4B58: 00         NOP
4B59: 00         NOP
4B5A: 00         NOP
4B5B: 00         NOP
4B5C: 00         NOP
4B5D: 00         NOP
4B5E: 00         NOP
4B5F: 00         NOP
4B60: 07         RLCA
4B61: 00         NOP
4B62: 0C         INC         C
4B63: 07         RLCA
4B64: 11 0E 10   LD           DE,$100E
4B67: 0F         RRCA
4B68: 16 09      LD           D,$09
4B6A: 1F         RRA
4B6B: 06 1F      LD           B,$1F
4B6D: 0F         RRCA
4B6E: 3F         CCF
4B6F: 03         INC         BC
4B70: 7F         LD           A,A
4B71: 2C         INC         L
4B72: FF         RST         0X38
4B73: 2D         DEC         L
4B74: BF         CP           A
4B75: 4D         LD           C,L
4B76: BF         CP           A
4B77: 53         LD           D,E
4B78: BF         CP           A
4B79: 47         LD           B,A
4B7A: B7         OR           A
4B7B: 4F         LD           C,A
4B7C: AF         XOR         A
4B7D: 50         LD           D,B
4B7E: EF         RST         0X28
4B7F: 1C         INC         E
4B80: 7C         LD           A,H
4B81: 00         NOP
4B82: A2         AND         D
4B83: 7C         LD           A,H
4B84: 41         LD           B,C
4B85: FE 01      CP           $01
4B87: FE 01      CP           $01
4B89: FE 01      CP           $01
4B8B: FE 82      CP           $82
4B8D: 7C         LD           A,H
4B8E: B4         OR           H
4B8F: 48         LD           C,B
4B90: FE 30      CP           $30
4B92: F9         LD           SP,HL
4B93: B6         OR           (HL)
4B94: E9         JP           (HL)
4B95: F6 F9      OR           $F9
4B97: C6 BD      ADD         $BD
4B99: C2 7D 82   JP           NZ,$827D
4B9C: E5         PUSH       HL
4B9D: 1A         LD           A,(DE)
4B9E: F7         RST         0X30
4B9F: 38 0E      JR           C,$4BAF
4BA1: 00         NOP
4BA2: 0A         LD           A,(BC)
4BA3: 04         INC         B
4BA4: 0E 00      LD           C,$00
4BA6: 0A         LD           A,(BC)
4BA7: 04         INC         B
4BA8: 0A         LD           A,(BC)
4BA9: 04         INC         B
4BAA: 0E 00      LD           C,$00
4BAC: 0A         LD           A,(BC)
4BAD: 04         INC         B
4BAE: 11 0E 15   LD           DE,$150E
4BB1: 0E 1F      LD           C,$1F
4BB3: 00         NOP
4BB4: 15         DEC         D
4BB5: 0E 25      LD           C,$25
4BB7: 1E 2D      LD           E,$2D
4BB9: 1E 4D      LD           E,$4D
4BBB: 3E 5D      LD           A,$5D
4BBD: 2A         LD           A,(HLI)
4BBE: 7F         LD           A,A
4BBF: 00         NOP
4BC0: 00         NOP
4BC1: FF         RST         0X38
4BC2: 00         NOP
4BC3: FF         RST         0X38
4BC4: 24         INC         H
4BC5: FF         RST         0X38
4BC6: 18 FF      JR           $4BC7
4BC8: 18 FF      JR           $4BC9
4BCA: 24         INC         H
4BCB: FF         RST         0X38
4BCC: 00         NOP
4BCD: FF         RST         0X38
4BCE: 00         NOP
4BCF: FF         RST         0X38
4BD0: 00         NOP
4BD1: FF         RST         0X38
4BD2: 00         NOP
4BD3: FF         RST         0X38
4BD4: 24         INC         H
4BD5: FF         RST         0X38
4BD6: 18 FF      JR           $4BD7
4BD8: 18 FF      JR           $4BD9
4BDA: 24         INC         H
4BDB: FF         RST         0X38
4BDC: 00         NOP
4BDD: FF         RST         0X38
4BDE: 00         NOP
4BDF: FF         RST         0X38
4BE0: 00         NOP
4BE1: FF         RST         0X38
4BE2: 00         NOP
4BE3: FF         RST         0X38
4BE4: 24         INC         H
4BE5: FF         RST         0X38
4BE6: 18 FF      JR           $4BE7
4BE8: 18 FF      JR           $4BE9
4BEA: 24         INC         H
4BEB: FF         RST         0X38
4BEC: 00         NOP
4BED: FF         RST         0X38
4BEE: 00         NOP
4BEF: FF         RST         0X38
4BF0: 00         NOP
4BF1: FF         RST         0X38
4BF2: 00         NOP
4BF3: FF         RST         0X38
4BF4: 24         INC         H
4BF5: FF         RST         0X38
4BF6: 18 FF      JR           $4BF7
4BF8: 18 FF      JR           $4BF9
4BFA: 24         INC         H
4BFB: FF         RST         0X38
4BFC: 00         NOP
4BFD: FF         RST         0X38
4BFE: 00         NOP
4BFF: FF         RST         0X38
4C00: 38 00      JR           C,$4C02
4C02: 5F         LD           E,A
4C03: 20 BF      JR           NZ,$4BC4
4C05: 40         LD           B,B
4C06: FC                              
4C07: 03         INC         BC
4C08: B7         OR           A
4C09: 78         LD           A,B
4C0A: FF         RST         0X38
4C0B: 03         INC         BC
4C0C: 1F         RRA
4C0D: 07         RLCA
4C0E: 3F         CCF
4C0F: 0E 3E      LD           C,$3E
4C11: 0D         DEC         C
4C12: 7E         LD           A,(HL)
4C13: 0D         DEC         C
4C14: 7F         LD           A,A
4C15: 0E BF      LD           C,$BF
4C17: 47         LD           B,A
4C18: FF         RST         0X38
4C19: 43         LD           B,E
4C1A: BF         CP           A
4C1B: 60         LD           H,B
4C1C: 5F         LD           E,A
4C1D: 3F         CCF
4C1E: 3F         CCF
4C1F: 00         NOP
4C20: 1C         INC         E
4C21: 00         NOP
4C22: F2                              
4C23: 0C         INC         C
4C24: FD                              
4C25: 02         LD           (BC),A
4C26: 3F         CCF
4C27: C0         RET         NZ
4C28: ED                              
4C29: 1E FF      LD           E,$FF
4C2B: C0         RET         NZ
4C2C: F8 E0      LDHL       SP,$E0
4C2E: FC                              
4C2F: 70         LD           (HL),B
4C30: 7C         LD           A,H
4C31: B0         OR           B
4C32: 7E         LD           A,(HL)
4C33: 90         SUB         B
4C34: 9E         SBC         (HL)
4C35: 60         LD           H,B
4C36: CD B2 FF   CALL       $FFB2
4C39: 82         ADD         A,D
4C3A: FD                              
4C3B: 06 FA      LD           B,$FA
4C3D: FC                              
4C3E: FC                              
4C3F: 00         NOP
4C40: 00         NOP
4C41: 00         NOP
4C42: 00         NOP
4C43: 00         NOP
4C44: 1E 00      LD           E,$00
4C46: 21 1E 47   LD           HL,$471E
4C49: 3F         CCF
4C4A: 77         LD           (HL),A
4C4B: 0D         DEC         C
4C4C: EF         RST         0X28
4C4D: 77         LD           (HL),A
4C4E: E8 17      ADD         SP,$17
4C50: F0 6F      LD           A,($6F)
4C52: FC                              
4C53: 5F         LD           E,A
4C54: FF         RST         0X38
4C55: 3E 7F      LD           A,$7F
4C57: 3E 5E      LD           A,$5E
4C59: 3F         CCF
4C5A: 2D         DEC         L
4C5B: 1E 1F      LD           E,$1F
4C5D: 01 1F 00   LD           BC,$001F
4C60: 00         NOP
4C61: 00         NOP
4C62: 00         NOP
4C63: 00         NOP
4C64: 00         NOP
4C65: 00         NOP
4C66: 00         NOP
4C67: 00         NOP
4C68: 80         ADD         A,B
4C69: 00         NOP
4C6A: 80         ADD         A,B
4C6B: 00         NOP
4C6C: 60         LD           H,B
4C6D: 80         ADD         A,B
4C6E: 1E E0      LD           E,$E0
4C70: 1D         DEC         E
4C71: E2         LDFF00   (C),A
4C72: 39         ADD         HL,SP
4C73: C6 1A      ADD         $1A
4C75: E4                              
4C76: 14         INC         D
4C77: E8 F8      ADD         SP,$F8
4C79: 00         NOP
4C7A: F0 40      LD           A,($40)
4C7C: D0         RET         NC
4C7D: E0 F0      LDFF00   ($F0),A
4C7F: 00         NOP
4C80: 00         NOP
4C81: 00         NOP
4C82: 0F         RRCA
4C83: 00         NOP
4C84: 10 0F      STOP       $0F
4C86: 23         INC         HL
4C87: 1F         RRA
4C88: 3B         DEC         SP
4C89: 06 77      LD           B,$77
4C8B: 3B         DEC         SP
4C8C: 74         LD           (HL),H
4C8D: 0B         DEC         BC
4C8E: 78         LD           A,B
4C8F: 37         SCF
4C90: 7E         LD           A,(HL)
4C91: 2F         CPL
4C92: 3F         CCF
4C93: 1E 3F      LD           E,$3F
4C95: 1E 3F      LD           E,$3F
4C97: 1F         RRA
4C98: 2F         CPL
4C99: 1F         RRA
4C9A: 11 0E 0F   LD           DE,$0F0E
4C9D: 01 1F 00   LD           BC,$001F
4CA0: 00         NOP
4CA1: 00         NOP
4CA2: 00         NOP
4CA3: 00         NOP
4CA4: 80         ADD         A,B
4CA5: 00         NOP
4CA6: C0         RET         NZ
4CA7: 80         ADD         A,B
4CA8: C0         RET         NZ
4CA9: 80         ADD         A,B
4CAA: E0 80      LDFF00   ($80),A
4CAC: 1E E0      LD           E,$E0
4CAE: 1D         DEC         E
4CAF: E2         LDFF00   (C),A
4CB0: 39         ADD         HL,SP
4CB1: C6 1A      ADD         $1A
4CB3: E4                              
4CB4: 14         INC         D
4CB5: E8 E8      ADD         SP,$E8
4CB7: 10 70      STOP       $70
4CB9: 80         ADD         A,B
4CBA: E0 40      LDFF00   ($40),A
4CBC: D0         RET         NC
4CBD: E0 F0      LDFF00   ($F0),A
4CBF: 00         NOP
4CC0: E0 00      LDFF00   ($00),A
4CC2: F0 00      LD           A,($00)
4CC4: 9E         SBC         (HL)
4CC5: 60         LD           H,B
4CC6: 61         LD           H,C
4CC7: 1E 47      LD           E,$47
4CC9: 3F         CCF
4CCA: 77         LD           (HL),A
4CCB: 0D         DEC         C
4CCC: EF         RST         0X28
4CCD: 77         LD           (HL),A
4CCE: E8 17      ADD         SP,$17
4CD0: F0 6F      LD           A,($6F)
4CD2: FC                              
4CD3: 5F         LD           E,A
4CD4: FE 3F      CP           $3F
4CD6: 7E         LD           A,(HL)
4CD7: 3F         CCF
4CD8: 5E         LD           E,(HL)
4CD9: 3F         CCF
4CDA: 2D         DEC         L
4CDB: 1E 1F      LD           E,$1F
4CDD: 01 1F 00   LD           BC,$001F
4CE0: 07         RLCA
4CE1: 00         NOP
4CE2: 1F         RRA
4CE3: 00         NOP
4CE4: 2F         CPL
4CE5: 10 4F      STOP       $4F
4CE7: 30 83      JR           NC,$4C6C
4CE9: 7C         LD           A,H
4CEA: 82         ADD         A,D
4CEB: 7C         LD           A,H
4CEC: 02         LD           (BC),A
4CED: FC                              
4CEE: 06 F8      LD           B,$F8
4CF0: 09         ADD         HL,BC
4CF1: F6 31      OR           $31
4CF3: CE 02      ADC         $02
4CF5: FC                              
4CF6: 04         INC         B
4CF7: F8 78      LDHL       SP,$78
4CF9: 80         ADD         A,B
4CFA: F0 40      LD           A,($40)
4CFC: D0         RET         NC
4CFD: E0 F0      LDFF00   ($F0),A
4CFF: 00         NOP
4D00: 00         NOP
4D01: 00         NOP
4D02: 00         NOP
4D03: 00         NOP
4D04: 00         NOP
4D05: 00         NOP
4D06: 00         NOP
4D07: 00         NOP
4D08: 00         NOP
4D09: 00         NOP
4D0A: 00         NOP
4D0B: 00         NOP
4D0C: 00         NOP
4D0D: 00         NOP
4D0E: 00         NOP
4D0F: 00         NOP
4D10: 0E 00      LD           C,$00
4D12: 1F         RRA
4D13: 0E 0F      LD           C,$0F
4D15: 01 01 00   LD           BC,$0001
4D18: 00         NOP
4D19: 00         NOP
4D1A: 06 00      LD           B,$00
4D1C: 0F         RRCA
4D1D: 00         NOP
4D1E: 0D         DEC         C
4D1F: 02         LD           (BC),A
4D20: 00         NOP
4D21: 00         NOP
4D22: 00         NOP
4D23: 00         NOP
4D24: 00         NOP
4D25: 00         NOP
4D26: 00         NOP
4D27: 00         NOP
4D28: 00         NOP
4D29: 00         NOP
4D2A: 00         NOP
4D2B: 00         NOP
4D2C: 00         NOP
4D2D: 00         NOP
4D2E: 70         LD           (HL),B
4D2F: 00         NOP
4D30: 79         LD           A,C
4D31: 30 3B      JR           NC,$4D6E
4D33: 10 9F      STOP       $9F
4D35: 08 FE 8B   LD           ($8BFE),SP
4D38: B6         OR           (HL)
4D39: 49         LD           C,C
4D3A: FF         RST         0X38
4D3B: 00         NOP
4D3C: FF         RST         0X38
4D3D: 00         NOP
4D3E: FF         RST         0X38
4D3F: 00         NOP
4D40: 00         NOP
4D41: 00         NOP
4D42: 00         NOP
4D43: 00         NOP
4D44: 00         NOP
4D45: 00         NOP
4D46: 00         NOP
4D47: 00         NOP
4D48: 00         NOP
4D49: 00         NOP
4D4A: 00         NOP
4D4B: 00         NOP
4D4C: 00         NOP
4D4D: 00         NOP
4D4E: 00         NOP
4D4F: 00         NOP
4D50: F0 00      LD           A,($00)
4D52: 38 C0      JR           C,$4D14
4D54: F8 00      LDHL       SP,$00
4D56: FC                              
4D57: 00         NOP
4D58: FC                              
4D59: 00         NOP
4D5A: FC                              
4D5B: 00         NOP
4D5C: BC         CP           H
4D5D: 00         NOP
4D5E: D8         RET         C
4D5F: 00         NOP
4D60: 0F         RRCA
4D61: 00         NOP
4D62: 0F         RRCA
4D63: 00         NOP
4D64: 1F         RRA
4D65: 00         NOP
4D66: 1F         RRA
4D67: 08 17 0C   LD           ($0C17),SP
4D6A: 0F         RRCA
4D6B: 06 07      LD           B,$07
4D6D: 03         INC         BC
4D6E: 03         INC         BC
4D6F: 01 01 00   LD           BC,$0001
4D72: 00         NOP
4D73: 00         NOP
4D74: 01 00 03   LD           BC,$0300
4D77: 01 03 00   LD           BC,$0003
4D7A: 00         NOP
4D7B: 00         NOP
4D7C: 00         NOP
4D7D: 00         NOP
4D7E: 00         NOP
4D7F: 00         NOP
4D80: FF         RST         0X38
4D81: 18 FF      JR           $4D82
4D83: 18 FF      JR           $4D84
4D85: 18 FF      JR           $4D86
4D87: 35         DEC         (HL)
4D88: FF         RST         0X38
4D89: B7         OR           A
4D8A: FE FF      CP           $FF
4D8C: FF         RST         0X38
4D8D: 7C         LD           A,H
4D8E: 7F         LD           A,A
4D8F: B8         CP           B
4D90: 7F         LD           A,A
4D91: 82         ADD         A,D
4D92: E7         RST         0X20
4D93: 5B         LD           E,E
4D94: FB         EI
4D95: C5         PUSH       BC
4D96: D1         POP         DE
4D97: 8E         ADC         A,(HL)
4D98: 9F         SBC         A
4D99: 00         NOP
4D9A: 1E 0B      LD           E,$0B
4D9C: 1F         RRA
4D9D: 0A         LD           A,(BC)
4D9E: 1E 00      LD           E,$00
4DA0: C7         RST         0X00
4DA1: 00         NOP
4DA2: CF         RST         0X08
4DA3: 06 DD      LD           B,$DD
4DA5: 0E FE      LD           C,$FE
4DA7: 1C         INC         E
4DA8: FA 3C FC   LD           A,($FC3C)
4DAB: 78         LD           A,B
4DAC: 68         LD           L,B
4DAD: F0 30      LD           A,($30)
4DAF: C0         RET         NZ
4DB0: C0         RET         NZ
4DB1: 00         NOP
4DB2: 80         ADD         A,B
4DB3: 00         NOP
4DB4: C0         RET         NZ
4DB5: 80         ADD         A,B
4DB6: C0         RET         NZ
4DB7: 00         NOP
4DB8: 80         ADD         A,B
4DB9: 00         NOP
4DBA: 80         ADD         A,B
4DBB: 00         NOP
4DBC: 00         NOP
4DBD: 00         NOP
4DBE: 00         NOP
4DBF: 00         NOP
4DC0: 0F         RRCA
4DC1: 00         NOP
4DC2: 0F         RRCA
4DC3: 00         NOP
4DC4: 0F         RRCA
4DC5: 00         NOP
4DC6: 07         RLCA
4DC7: 00         NOP
4DC8: 03         INC         BC
4DC9: 00         NOP
4DCA: 01 00 00   LD           BC,$0000
4DCD: 00         NOP
4DCE: 01 00 02   LD           BC,$0200
4DD1: 01 07 03   LD           BC,$0307
4DD4: 0F         RRCA
4DD5: 06 1F      LD           B,$1F
4DD7: 0D         DEC         C
4DD8: 3F         CCF
4DD9: 18 18      JR           $4DF3
4DDB: 00         NOP
4DDC: 00         NOP
4DDD: 00         NOP
4DDE: 00         NOP
4DDF: 00         NOP
4DE0: C0         RET         NZ
4DE1: 00         NOP
4DE2: C0         RET         NZ
4DE3: 00         NOP
4DE4: C0         RET         NZ
4DE5: 00         NOP
4DE6: C0         RET         NZ
4DE7: 00         NOP
4DE8: 80         ADD         A,B
4DE9: 00         NOP
4DEA: 80         ADD         A,B
4DEB: 00         NOP
4DEC: 80         ADD         A,B
4DED: 00         NOP
4DEE: 40         LD           B,B
4DEF: 80         ADD         A,B
4DF0: F0 C0      LD           A,($C0)
4DF2: F8 70      LDHL       SP,$70
4DF4: FC                              
4DF5: B8         CP           B
4DF6: FE 1C      CP           $1C
4DF8: 9F         SBC         A
4DF9: 06 87      LD           B,$87
4DFB: 00         NOP
4DFC: 00         NOP
4DFD: 00         NOP
4DFE: 00         NOP
4DFF: 00         NOP
4E00: 0F         RRCA
4E01: 00         NOP
4E02: 1F         RRA
4E03: 0C         INC         C
4E04: FF         RST         0X38
4E05: 00         NOP
4E06: F9         LD           SP,HL
4E07: 7E         LD           A,(HL)
4E08: 7F         LD           A,A
4E09: 00         NOP
4E0A: 1F         RRA
4E0B: 0D         DEC         C
4E0C: 1F         RRA
4E0D: 05         DEC         B
4E0E: 7F         LD           A,A
4E0F: 1F         RRA
4E10: BF         CP           A
4E11: 5E         LD           E,(HL)
4E12: 9E         SBC         (HL)
4E13: 61         LD           H,C
4E14: C0         RET         NZ
4E15: 3F         CCF
4E16: FF         RST         0X38
4E17: 40         LD           B,B
4E18: FC                              
4E19: 5B         LD           E,E
4E1A: 7F         LD           A,A
4E1B: 18 1B      JR           $4E38
4E1D: 07         RLCA
4E1E: 3F         CCF
4E1F: 00         NOP
4E20: F8 00      LDHL       SP,$00
4E22: B4         OR           H
4E23: 78         LD           A,B
4E24: 7A         LD           A,D
4E25: FC                              
4E26: 6A         LD           L,D
4E27: FC                              
4E28: 02         LD           (BC),A
4E29: FC                              
4E2A: FC                              
4E2B: 00         NOP
4E2C: E4                              
4E2D: D8         RET         C
4E2E: E8 10      ADD         SP,$10
4E30: 30 C0      JR           NC,$4DF2
4E32: 18 E0      JR           $4E14
4E34: 78         LD           A,B
4E35: 80         ADD         A,B
4E36: 98         SBC         B
4E37: 60         LD           H,B
4E38: 38 C0      JR           C,$4DFA
4E3A: F8 00      LDHL       SP,$00
4E3C: 20 C0      JR           NZ,$4DFE
4E3E: F0 00      LD           A,($00)
4E40: 3F         CCF
4E41: 00         NOP
4E42: 5B         LD           E,E
4E43: 3C         INC         A
4E44: BD         CP           L
4E45: 7E         LD           A,(HL)
4E46: AD         XOR         L
4E47: 7E         LD           A,(HL)
4E48: 81         ADD         A,C
4E49: 7E         LD           A,(HL)
4E4A: 7F         LD           A,A
4E4B: 01 4F 37   LD           BC,$374F
4E4E: 6F         LD           L,A
4E4F: 11 31 0E   LD           DE,$0E31
4E52: A0         AND         B
4E53: 1F         RRA
4E54: F0 0F      LD           A,($0F)
4E56: FF         RST         0X38
4E57: 60         LD           H,B
4E58: FC                              
4E59: 5B         LD           E,E
4E5A: 7F         LD           A,A
4E5B: 18 1B      JR           $4E78
4E5D: 07         RLCA
4E5E: 3F         CCF
4E5F: 00         NOP
4E60: E0 00      LDFF00   ($00),A
4E62: F0 60      LD           A,($60)
4E64: FE 00      CP           $00
4E66: 3E FC      LD           A,$FC
4E68: FC                              
4E69: 00         NOP
4E6A: F0 60      LD           A,($60)
4E6C: F8 40      LDHL       SP,$40
4E6E: FC                              
4E6F: F0 FA      LD           A,($FA)
4E71: F4                              
4E72: F2                              
4E73: 0C         INC         C
4E74: 04         INC         B
4E75: F8 F8      LDHL       SP,$F8
4E77: 00         NOP
4E78: 38 C0      JR           C,$4E3A
4E7A: F8 00      LDHL       SP,$00
4E7C: 20 C0      JR           NZ,$4E3E
4E7E: F0 00      LD           A,($00)
4E80: 00         NOP
4E81: 00         NOP
4E82: 00         NOP
4E83: 00         NOP
4E84: 00         NOP
4E85: 00         NOP
4E86: 00         NOP
4E87: 00         NOP
4E88: 00         NOP
4E89: 00         NOP
4E8A: 00         NOP
4E8B: 00         NOP
4E8C: 00         NOP
4E8D: 00         NOP
4E8E: 3F         CCF
4E8F: 00         NOP
4E90: 7F         LD           A,A
4E91: 3F         CCF
4E92: 3F         CCF
4E93: 00         NOP
4E94: 00         NOP
4E95: 00         NOP
4E96: 00         NOP
4E97: 00         NOP
4E98: 00         NOP
4E99: 00         NOP
4E9A: 00         NOP
4E9B: 00         NOP
4E9C: 00         NOP
4E9D: 00         NOP
4E9E: 00         NOP
4E9F: 00         NOP
4EA0: 00         NOP
4EA1: 00         NOP
4EA2: 00         NOP
4EA3: 00         NOP
4EA4: 00         NOP
4EA5: 00         NOP
4EA6: 00         NOP
4EA7: 00         NOP
4EA8: 00         NOP
4EA9: 00         NOP
4EAA: 00         NOP
4EAB: 00         NOP
4EAC: 00         NOP
4EAD: 00         NOP
4EAE: C0         RET         NZ
4EAF: 00         NOP
4EB0: BC         CP           H
4EB1: C0         RET         NZ
4EB2: 7B         LD           A,E
4EB3: FC                              
4EB4: F6 0F      OR           $0F
4EB6: 0D         DEC         C
4EB7: 03         INC         BC
4EB8: 03         INC         BC
4EB9: 00         NOP
4EBA: 00         NOP
4EBB: 00         NOP
4EBC: 00         NOP
4EBD: 00         NOP
4EBE: 00         NOP
4EBF: 00         NOP
4EC0: 00         NOP
4EC1: 00         NOP
4EC2: 00         NOP
4EC3: 00         NOP
4EC4: 1C         INC         E
4EC5: 00         NOP
4EC6: 3F         CCF
4EC7: 1C         INC         E
4EC8: 1F         RRA
4EC9: 03         INC         BC
4ECA: 03         INC         BC
4ECB: 00         NOP
4ECC: 00         NOP
4ECD: 00         NOP
4ECE: 00         NOP
4ECF: 00         NOP
4ED0: 00         NOP
4ED1: 00         NOP
4ED2: 00         NOP
4ED3: 00         NOP
4ED4: 00         NOP
4ED5: 00         NOP
4ED6: 00         NOP
4ED7: 00         NOP
4ED8: 00         NOP
4ED9: 00         NOP
4EDA: 00         NOP
4EDB: 00         NOP
4EDC: 00         NOP
4EDD: 00         NOP
4EDE: 00         NOP
4EDF: 00         NOP
4EE0: 00         NOP
4EE1: 00         NOP
4EE2: 00         NOP
4EE3: 00         NOP
4EE4: 00         NOP
4EE5: 00         NOP
4EE6: 80         ADD         A,B
4EE7: 00         NOP
4EE8: E0 80      LDFF00   ($80),A
4EEA: 78         LD           A,B
4EEB: E0 DC      LDFF00   ($DC),A
4EED: 38 2E      JR           C,$4F1D
4EEF: 1C         INC         E
4EF0: 17         RLA
4EF1: 0E 0B      LD           C,$0B
4EF3: 07         RLCA
4EF4: 05         DEC         B
4EF5: 03         INC         BC
4EF6: 02         LD           (BC),A
4EF7: 01 01 00   LD           BC,$0001
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
4F07: 00         NOP
4F08: 0F         RRCA
4F09: 00         NOP
4F0A: 37         SCF
4F0B: 0F         RRCA
4F0C: 5F         LD           E,A
4F0D: 3F         CCF
4F0E: BF         CP           A
4F0F: 7F         LD           A,A
4F10: BF         CP           A
4F11: 7F         LD           A,A
4F12: 5F         LD           E,A
4F13: 3F         CCF
4F14: 37         SCF
4F15: 0F         RRCA
4F16: 0F         RRCA
4F17: 00         NOP
4F18: 00         NOP
4F19: 00         NOP
4F1A: 00         NOP
4F1B: 00         NOP
4F1C: 00         NOP
4F1D: 00         NOP
4F1E: 00         NOP
4F1F: 00         NOP
4F20: 01 00 02   LD           BC,$0200
4F23: 01 05 03   LD           BC,$0305
4F26: 07         RLCA
4F27: 03         INC         BC
4F28: 0B         DEC         BC
4F29: 07         RLCA
4F2A: 0F         RRCA
4F2B: 07         RLCA
4F2C: 0F         RRCA
4F2D: 07         RLCA
4F2E: 0F         RRCA
4F2F: 07         RLCA
4F30: 0F         RRCA
4F31: 07         RLCA
4F32: 0F         RRCA
4F33: 07         RLCA
4F34: 0F         RRCA
4F35: 07         RLCA
4F36: 0B         DEC         BC
4F37: 07         RLCA
4F38: 07         RLCA
4F39: 03         INC         BC
4F3A: 05         DEC         B
4F3B: 03         INC         BC
4F3C: 02         LD           (BC),A
4F3D: 01 01 00   LD           BC,$0001
4F40: 00         NOP
4F41: 00         NOP
4F42: 00         NOP
4F43: 00         NOP
4F44: 00         NOP
4F45: 00         NOP
4F46: 00         NOP
4F47: 00         NOP
4F48: 00         NOP
4F49: 00         NOP
4F4A: 1F         RRA
4F4B: 00         NOP
4F4C: 6F         LD           L,A
4F4D: 1F         RRA
4F4E: BF         CP           A
4F4F: 7F         LD           A,A
4F50: BF         CP           A
4F51: 7F         LD           A,A
4F52: 6F         LD           L,A
4F53: 1F         RRA
4F54: 1F         RRA
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
4F60: 01 00 02   LD           BC,$0200
4F63: 01 03 01   LD           BC,$0103
4F66: 05         DEC         B
4F67: 03         INC         BC
4F68: 07         RLCA
4F69: 03         INC         BC
4F6A: 07         RLCA
4F6B: 03         INC         BC
4F6C: 07         RLCA
4F6D: 03         INC         BC
4F6E: 07         RLCA
4F6F: 03         INC         BC
4F70: 07         RLCA
4F71: 03         INC         BC
4F72: 07         RLCA
4F73: 03         INC         BC
4F74: 07         RLCA
4F75: 03         INC         BC
4F76: 07         RLCA
4F77: 03         INC         BC
4F78: 05         DEC         B
4F79: 03         INC         BC
4F7A: 03         INC         BC
4F7B: 01 02 01   LD           BC,$0102
4F7E: 01 00 00   LD           BC,$0000
4F81: 00         NOP
4F82: 00         NOP
4F83: 00         NOP
4F84: 1F         RRA
4F85: 00         NOP
4F86: 2E 1F      LD           L,$1F
4F88: 3F         CCF
4F89: 1F         RRA
4F8A: 3F         CCF
4F8B: 1F         RRA
4F8C: 3F         CCF
4F8D: 1F         RRA
4F8E: 2F         CPL
4F8F: 1F         RRA
4F90: 1F         RRA
4F91: 0F         RRCA
4F92: 17         RLA
4F93: 0F         RRCA
4F94: 0F         RRCA
4F95: 07         RLCA
4F96: 05         DEC         B
4F97: 03         INC         BC
4F98: 03         INC         BC
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
4FA4: 18 00      JR           $4FA6
4FA6: 26 18      LD           H,$18
4FA8: 2D         DEC         L
4FA9: 1E 1F      LD           E,$1F
4FAB: 0F         RRCA
4FAC: 17         RLA
4FAD: 0F         RRCA
4FAE: 0F         RRCA
4FAF: 07         RLCA
4FB0: 07         RLCA
4FB1: 03         INC         BC
4FB2: 03         INC         BC
4FB3: 01 01 00   LD           BC,$0001
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
4FC4: 01 00 01   LD           BC,$0100
4FC7: 00         NOP
4FC8: 01 00 01   LD           BC,$0100
4FCB: 00         NOP
4FCC: 01 00 01   LD           BC,$0100
4FCF: 00         NOP
4FD0: 01 00 01   LD           BC,$0100
4FD3: 00         NOP
4FD4: 1F         RRA
4FD5: 00         NOP
4FD6: 3F         CCF
4FD7: 00         NOP
4FD8: 3E 00      LD           A,$00
4FDA: 1C         INC         E
4FDB: 00         NOP
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
4FE6: 80         ADD         A,B
4FE7: 00         NOP
4FE8: C0         RET         NZ
4FE9: 00         NOP
4FEA: 60         LD           H,B
4FEB: 00         NOP
4FEC: 70         LD           (HL),B
4FED: 00         NOP
4FEE: 30 00      JR           NC,$4FF0
4FF0: 30 00      JR           NC,$4FF2
4FF2: 20 00      JR           NZ,$4FF4
4FF4: 40         LD           B,B
4FF5: 00         NOP
4FF6: 00         NOP
4FF7: 00         NOP
4FF8: 00         NOP
4FF9: 00         NOP
4FFA: 00         NOP
4FFB: 00         NOP
4FFC: 00         NOP
4FFD: 00         NOP
4FFE: 00         NOP
4FFF: 00         NOP
5000: 00         NOP
5001: 00         NOP
5002: 00         NOP
5003: 00         NOP
5004: 00         NOP
5005: 00         NOP
5006: 03         INC         BC
5007: 00         NOP
5008: 07         RLCA
5009: 03         INC         BC
500A: 3F         CCF
500B: 02         LD           (BC),A
500C: 7E         LD           A,(HL)
500D: 3D         DEC         A
500E: FD                              
500F: 6A         LD           L,D
5010: FA 45 FC   LD           A,($FC45)
5013: 53         LD           D,E
5014: F0 7F      LD           A,($7F)
5016: E3                              
5017: 7C         LD           A,H
5018: C4 3B 60   CALL       NZ,$603B
501B: 1F         RRA
501C: 7F         LD           A,A
501D: 00         NOP
501E: 9F         SBC         A
501F: 00         NOP
5020: 1E 00      LD           E,$00
5022: 19         ADD         HL,DE
5023: 0E 25      LD           C,$25
5025: 1A         LD           A,(DE)
5026: DF         RST         0X18
5027: 20 B0      JR           NZ,$4FD9
5029: 40         LD           B,B
502A: 50         LD           D,B
502B: A0         AND         B
502C: 98         SBC         B
502D: 60         LD           H,B
502E: 18 E0      JR           $5010
5030: 78         LD           A,B
5031: 80         ADD         A,B
5032: 30 C0      JR           NC,$4FF4
5034: 20 C0      JR           NZ,$4FF6
5036: 20 C0      JR           NZ,$4FF8
5038: 20 C0      JR           NZ,$4FFA
503A: 60         LD           H,B
503B: 80         ADD         A,B
503C: C0         RET         NZ
503D: 00         NOP
503E: 80         ADD         A,B
503F: 00         NOP
5040: 00         NOP
5041: 00         NOP
5042: 07         RLCA
5043: 00         NOP
5044: 1D         DEC         E
5045: 07         RLCA
5046: 38 1F      JR           C,$5067
5048: 22         LD           (HLI),A
5049: 1D         DEC         E
504A: 67         LD           H,A
504B: 39         ADD         HL,SP
504C: 66         LD           H,(HL)
504D: 3B         DEC         SP
504E: CD 76 FA   CALL       $FA76
5051: 7D         LD           A,L
5052: 7D         LD           A,L
5053: 02         LD           (BC),A
5054: 1C         INC         E
5055: 03         INC         BC
5056: 1E 01      LD           E,$01
5058: 0F         RRCA
5059: 00         NOP
505A: 0F         RRCA
505B: 00         NOP
505C: 07         RLCA
505D: 00         NOP
505E: 00         NOP
505F: 00         NOP
5060: 00         NOP
5061: 00         NOP
5062: 00         NOP
5063: 00         NOP
5064: 80         ADD         A,B
5065: 00         NOP
5066: C0         RET         NZ
5067: 80         ADD         A,B
5068: E0 80      LDFF00   ($80),A
506A: 70         LD           (HL),B
506B: A0         AND         B
506C: B8         CP           B
506D: 60         LD           H,B
506E: 9C         SBC         H
506F: 68         LD           L,B
5070: 7F         LD           A,A
5071: 88         ADC         A,B
5072: 15         DEC         D
5073: EA F7 08   LD           ($08F7),A
5076: 34         INC         (HL)
5077: C8         RET         Z
5078: F8 00      LDHL       SP,$00
507A: C0         RET         NZ
507B: 00         NOP
507C: 80         ADD         A,B
507D: 00         NOP
507E: 00         NOP
507F: 00         NOP
5080: 00         NOP
5081: 00         NOP
5082: 00         NOP
5083: 00         NOP
5084: 00         NOP
5085: 00         NOP
5086: 03         INC         BC
5087: 00         NOP
5088: 1D         DEC         E
5089: 03         INC         BC
508A: 27         DAA
508B: 1F         RRA
508C: 5E         LD           E,(HL)
508D: 21 BF 40   LD           HL,$40BF
5090: BF         CP           A
5091: 43         LD           B,E
5092: BF         CP           A
5093: 43         LD           B,E
5094: BC         CP           H
5095: 43         LD           B,E
5096: 5F         LD           E,A
5097: 20 5F      JR           NZ,$50F8
5099: 20 27      JR           NZ,$50C2
509B: 18 18      JR           $50B5
509D: 07         RLCA
509E: 07         RLCA
509F: 00         NOP
50A0: 00         NOP
50A1: 00         NOP
50A2: 0C         INC         C
50A3: 00         NOP
50A4: FE 0C      CP           $0C
50A6: 7A         LD           A,D
50A7: E4                              
50A8: 8C         ADC         A,H
50A9: F0 04      LD           A,($04)
50AB: F8 C4      LDHL       SP,$C4
50AD: F8 44      LDHL       SP,$44
50AF: F8 88      LDHL       SP,$88
50B1: 70         LD           (HL),B
50B2: 48         LD           C,B
50B3: B0         OR           B
50B4: 50         LD           D,B
50B5: A0         AND         B
50B6: D0         RET         NC
50B7: 20 D0      JR           NZ,$5089
50B9: 20 A0      JR           NZ,$505B
50BB: 40         LD           B,B
50BC: 40         LD           B,B
50BD: 80         ADD         A,B
50BE: 80         ADD         A,B
50BF: 00         NOP
50C0: 3C         INC         A
50C1: 00         NOP
50C2: 7C         LD           A,H
50C3: 38 6F      JR           C,$5134
50C5: 30 5E      JR           NC,$5125
50C7: 3F         CCF
50C8: 27         DAA
50C9: 18 1A      JR           $50E5
50CB: 00         NOP
50CC: 0A         LD           A,(BC)
50CD: 00         NOP
50CE: 0A         LD           A,(BC)
50CF: 00         NOP
50D0: 0A         LD           A,(BC)
50D1: 00         NOP
50D2: 0A         LD           A,(BC)
50D3: 00         NOP
50D4: 0A         LD           A,(BC)
50D5: 00         NOP
50D6: 0A         LD           A,(BC)
50D7: 00         NOP
50D8: 3F         CCF
50D9: 00         NOP
50DA: 60         LD           H,B
50DB: 3F         CCF
50DC: 4F         LD           C,A
50DD: 30 70      JR           NC,$514F
50DF: 00         NOP
50E0: 00         NOP
50E1: 00         NOP
50E2: 00         NOP
50E3: 00         NOP
50E4: 80         ADD         A,B
50E5: 00         NOP
50E6: 40         LD           B,B
50E7: 80         ADD         A,B
50E8: 20 C0      JR           NZ,$50AA
50EA: 90         SUB         B
50EB: 60         LD           H,B
50EC: C8         RET         Z
50ED: 30 A4      JR           NC,$5093
50EF: 18 B2      JR           $50A3
50F1: 0C         INC         C
50F2: AA         XOR         D
50F3: 04         INC         B
50F4: A5         AND         L
50F5: 02         LD           (BC),A
50F6: A5         AND         L
50F7: 02         LD           (BC),A
50F8: A5         AND         L
50F9: 02         LD           (BC),A
50FA: 79         LD           A,C
50FB: 86         ADD         A,(HL)
50FC: 02         LD           (BC),A
50FD: FC                              
50FE: FC                              
50FF: 00         NOP
5100: 01 00 02   LD           BC,$0200
5103: 01 06 01   LD           BC,$0106
5106: 09         ADD         HL,BC
5107: 06 18      LD           B,$18
5109: 07         RLCA
510A: 24         INC         H
510B: 1B         DEC         DE
510C: 62         LD           H,D
510D: 1D         DEC         E
510E: 91         SUB         C
510F: 6E         LD           L,(HL)
5110: 89         ADC         A,C
5111: 76         HALT
5112: 4F         LD           C,A
5113: 31 BF 4C   LD           SP,$4CBF
5116: 9F         SBC         A
5117: 61         LD           H,C
5118: BA         CP           D
5119: 7D         LD           A,L
511A: 47         LD           B,A
511B: 38 38      JR           C,$5155
511D: 00         NOP
511E: 00         NOP
511F: 00         NOP
5120: 80         ADD         A,B
5121: 00         NOP
5122: 40         LD           B,B
5123: 80         ADD         A,B
5124: 20 C0      JR           NZ,$50E6
5126: 10 E0      STOP       $E0
5128: 88         ADC         A,B
5129: 70         LD           (HL),B
512A: 44         LD           B,H
512B: B8         CP           B
512C: 26 D8      LD           H,$D8
512E: 3F         CCF
512F: C6 FF      ADD         $FF
5131: 30 FF      JR           NC,$5132
5133: 86         ADD         A,(HL)
5134: F9         LD           SP,HL
5135: 36 CE      LD           (HL),$CE
5137: B0         OR           B
5138: 70         LD           (HL),B
5139: 80         ADD         A,B
513A: 80         ADD         A,B
513B: 00         NOP
513C: 00         NOP
513D: 00         NOP
513E: 00         NOP
513F: 00         NOP
5140: 06 00      LD           B,$00
5142: 07         RLCA
5143: 02         LD           (BC),A
5144: 04         INC         B
5145: 03         INC         BC
5146: 02         LD           (BC),A
5147: 01 02 01   LD           BC,$0102
514A: 05         DEC         B
514B: 02         LD           (BC),A
514C: 05         DEC         B
514D: 02         LD           (BC),A
514E: 0A         LD           A,(BC)
514F: 04         INC         B
5150: 0A         LD           A,(BC)
5151: 04         INC         B
5152: 14         INC         D
5153: 08 14 08   LD           ($0814),SP
5156: 28 10      JR           Z,$5168
5158: 2F         CPL
5159: 10 60      STOP       $60
515B: 3F         CCF
515C: 7F         LD           A,A
515D: 00         NOP
515E: 00         NOP
515F: 00         NOP
5160: B0         OR           B
5161: 00         NOP
5162: FC                              
5163: A0         AND         B
5164: 12         LD           (DE),A
5165: E0 A9      LDFF00   ($A9),A
5167: 40         LD           B,B
5168: 25         DEC         H
5169: C0         RET         NZ
516A: D3                              
516B: 20 50      JR           NZ,$51BD
516D: 20 28      JR           NZ,$5197
516F: 10 28      STOP       $28
5171: 10 14      STOP       $14
5173: 08 14 08   LD           ($0814),SP
5176: 08 00 FE   LD           ($FE00),SP
5179: 00         NOP
517A: 02         LD           (BC),A
517B: FC                              
517C: FE 00      CP           $00
517E: 00         NOP
517F: 00         NOP
5180: 00         NOP
5181: 00         NOP
5182: 07         RLCA
5183: 00         NOP
5184: 0B         DEC         BC
5185: 07         RLCA
5186: 10 0F      STOP       $0F
5188: 21 1F 43   LD           HL,$431F
518B: 3E 47      LD           A,$47
518D: 3C         INC         A
518E: 4F         LD           C,A
518F: 38 5F      JR           C,$51F0
5191: 30 7F      JR           NC,$5212
5193: 22         LD           (HLI),A
5194: 7F         LD           A,A
5195: 01 7F 19   LD           BC,$197F
5198: 5F         LD           E,A
5199: 2E 2F      LD           L,$2F
519B: 17         RLA
519C: 17         RLA
519D: 08 0F 00   LD           ($000F),SP
51A0: 00         NOP
51A1: 00         NOP
51A2: F0 00      LD           A,($00)
51A4: F8 C0      LDHL       SP,$C0
51A6: FC                              
51A7: 88         ADC         A,B
51A8: FE 04      CP           $04
51AA: FF         RST         0X38
51AB: 26 FF      LD           H,$FF
51AD: 1A         LD           A,(DE)
51AE: FF         RST         0X38
51AF: 9C         SBC         H
51B0: FD                              
51B1: 6A         LD           L,D
51B2: FA 74 F4   LD           A,($F474)
51B5: A8         XOR         B
51B6: E8 D0      ADD         SP,$D0
51B8: D0         RET         NC
51B9: A0         AND         B
51BA: A0         AND         B
51BB: 40         LD           B,B
51BC: 40         LD           B,B
51BD: 80         ADD         A,B
51BE: 80         ADD         A,B
51BF: 00         NOP
51C0: 00         NOP
51C1: 00         NOP
51C2: 07         RLCA
51C3: 00         NOP
51C4: 1F         RRA
51C5: 07         RLCA
51C6: 38 1F      JR           C,$51E7
51C8: 61         LD           H,C
51C9: 3E 63      LD           A,$63
51CB: 3D         DEC         A
51CC: 63         LD           H,E
51CD: 3C         INC         A
51CE: 79         LD           A,C
51CF: 1E 7F      LD           E,$7F
51D1: 27         DAA
51D2: 7F         LD           A,A
51D3: 18 7F      JR           $5254
51D5: 27         DAA
51D6: 7F         LD           A,A
51D7: 30 7D      JR           NC,$5256
51D9: 26 3B      LD           H,$3B
51DB: 0C         INC         C
51DC: 1A         LD           A,(DE)
51DD: 05         DEC         B
51DE: 07         RLCA
51DF: 00         NOP
51E0: 1C         INC         E
51E1: 00         NOP
51E2: FE 14      CP           $14
51E4: FA AC F4   LD           A,($F4AC)
51E7: 58         LD           E,B
51E8: EC                              
51E9: B0         OR           B
51EA: D6 6C      SUB         $6C
51EC: A6         AND         (HL)
51ED: DC DE 38   CALL       C,$38DE
51F0: FE E4      CP           $E4
51F2: FE 18      CP           $18
51F4: FA E4 F2   LD           A,($F2E4)
51F7: 0C         INC         C
51F8: 36 C8      LD           (HL),$C8
51FA: 24         INC         H
51FB: D8         RET         C
51FC: 78         LD           A,B
51FD: 80         ADD         A,B
51FE: E0 00      LDFF00   ($00),A
5200: 07         RLCA
5201: 00         NOP
5202: 18 07      JR           $520B
5204: 23         INC         HL
5205: 1F         RRA
5206: 2F         CPL
5207: 10 5F      STOP       $5F
5209: 20 7E      JR           NZ,$5289
520B: 01 4D 33   LD           BC,$334D
520E: B5         OR           L
520F: 7B         LD           A,E
5210: BF         CP           A
5211: 79         LD           A,C
5212: BA         CP           D
5213: 6D         LD           L,L
5214: FF         RST         0X38
5215: 2C         INC         L
5216: 5E         LD           E,(HL)
5217: 35         DEC         (HL)
5218: 62         LD           H,D
5219: 1D         DEC         E
521A: 3E 01      LD           A,$01
521C: 17         RLA
521D: 0C         INC         C
521E: 0E 00      LD           C,$00
5220: 03         INC         BC
5221: 00         NOP
5222: 0C         INC         C
5223: 03         INC         BC
5224: 17         RLA
5225: 0F         RRCA
5226: 2F         CPL
5227: 1C         INC         E
5228: 6D         LD           L,L
5229: 13         INC         DE
522A: FB         EI
522B: 47         LD           B,A
522C: E8 17      ADD         SP,$17
522E: 4F         LD           C,A
522F: 30 5F      JR           NC,$5290
5231: 20 EF      JR           NZ,$5222
5233: 1F         RRA
5234: EF         RST         0X28
5235: 57         LD           D,A
5236: AF         XOR         A
5237: 59         LD           E,C
5238: 57         LD           D,A
5239: 2F         CPL
523A: 38 07      JR           C,$5243
523C: 1F         RRA
523D: 00         NOP
523E: 07         RLCA
523F: 00         NOP
5240: 80         ADD         A,B
5241: 00         NOP
5242: 60         LD           H,B
5243: 80         ADD         A,B
5244: B8         CP           B
5245: C0         RET         NZ
5246: FC                              
5247: 00         NOP
5248: 7A         LD           A,D
5249: 84         ADD         A,H
524A: 7D         LD           A,L
524B: 86         ADD         A,(HL)
524C: FD                              
524D: 06 FD      LD           B,$FD
524F: 06 FD      LD           B,$FD
5251: 06 7D      LD           B,$7D
5253: 86         ADD         A,(HL)
5254: B9         CP           C
5255: C6 BA      ADD         $BA
5257: C4 B2 CC   CALL       NZ,$CCB2
525A: 64         LD           H,H
525B: 98         SBC         B
525C: F8 00      LDHL       SP,$00
525E: C0         RET         NZ
525F: 00         NOP
5260: 00         NOP
5261: 00         NOP
5262: 03         INC         BC
5263: 00         NOP
5264: 0F         RRCA
5265: 00         NOP
5266: 1E 01      LD           E,$01
5268: 3D         DEC         A
5269: 03         INC         BC
526A: 3D         DEC         A
526B: 03         INC         BC
526C: 5E         LD           E,(HL)
526D: 21 5F 20   LD           HL,$205F
5270: 5F         LD           E,A
5271: 20 4F      JR           NZ,$52C2
5273: 30 27      JR           NC,$529C
5275: 18 25      JR           $529C
5277: 1B         DEC         DE
5278: 14         INC         D
5279: 0B         DEC         BC
527A: 0C         INC         C
527B: 03         INC         BC
527C: 03         INC         BC
527D: 00         NOP
527E: 00         NOP
527F: 00         NOP
5280: 06 00      LD           B,$00
5282: 09         ADD         HL,BC
5283: 06 15      LD           B,$15
5285: 0E 1B      LD           C,$1B
5287: 0C         INC         C
5288: 1F         RRA
5289: 08 17 08   LD           ($0817),SP
528C: 1E 01      LD           E,$01
528E: 1D         DEC         E
528F: 03         INC         BC
5290: 7D         LD           A,L
5291: 03         INC         BC
5292: 9E         SBC         (HL)
5293: 61         LD           H,C
5294: AF         XOR         A
5295: 70         LD           (HL),B
5296: 5B         LD           E,E
5297: 3C         INC         A
5298: 3F         CCF
5299: 00         NOP
529A: 00         NOP
529B: 00         NOP
529C: 00         NOP
529D: 00         NOP
529E: 00         NOP
529F: 00         NOP
52A0: 00         NOP
52A1: 00         NOP
52A2: 00         NOP
52A3: 00         NOP
52A4: 07         RLCA
52A5: 00         NOP
52A6: 18 07      JR           $52AF
52A8: 26 1F      LD           H,$1F
52AA: 73         LD           (HL),E
52AB: 0C         INC         C
52AC: 8C         ADC         A,H
52AD: 73         LD           (HL),E
52AE: A9         XOR         C
52AF: 77         LD           (HL),A
52B0: 9D         SBC         L
52B1: 63         LD           H,E
52B2: 6F         LD           L,A
52B3: 1C         INC         E
52B4: 2D         DEC         L
52B5: 1E 21      LD           E,$21
52B7: 1E 13      LD           E,$13
52B9: 0C         INC         C
52BA: 0C         INC         C
52BB: 00         NOP
52BC: 00         NOP
52BD: 00         NOP
52BE: 00         NOP
52BF: 00         NOP
52C0: 18 00      JR           $52C2
52C2: 3C         INC         A
52C3: 18 3A      JR           $52FF
52C5: 1C         INC         E
52C6: 12         LD           (DE),A
52C7: 0C         INC         C
52C8: 1E 00      LD           E,$00
52CA: 15         DEC         D
52CB: 0E 7F      LD           C,$7F
52CD: 06 EF      LD           B,$EF
52CF: 71         LD           (HL),C
52D0: FE 6D      CP           $6D
52D2: 7D         LD           A,L
52D3: 0E 09      LD           C,$09
52D5: 06 07      LD           B,$07
52D7: 00         NOP
52D8: 0B         DEC         BC
52D9: 06 05      LD           B,$05
52DB: 02         LD           (BC),A
52DC: 02         LD           (BC),A
52DD: 00         NOP
52DE: 00         NOP
52DF: 00         NOP
52E0: 00         NOP
52E1: 00         NOP
52E2: 00         NOP
52E3: 00         NOP
52E4: 00         NOP
52E5: 00         NOP
52E6: 00         NOP
52E7: 00         NOP
52E8: 00         NOP
52E9: 00         NOP
52EA: 06 00      LD           B,$00
52EC: 7F         LD           A,A
52ED: 06 E9      LD           B,$E9
52EF: 76         HALT
52F0: 9E         SBC         (HL)
52F1: 60         LD           H,B
52F2: 74         LD           (HL),H
52F3: 18 3E      JR           $5333
52F5: 00         NOP
52F6: 7E         LD           A,(HL)
52F7: 0C         INC         C
52F8: B4         OR           H
52F9: 68         LD           L,B
52FA: CC 70 90   CALL       Z,$9070
52FD: 60         LD           H,B
52FE: 60         LD           H,B
52FF: 00         NOP
5300: 04         INC         B
5301: 00         NOP
5302: 0E 04      LD           C,$04
5304: 0E 04      LD           C,$04
5306: 0E 04      LD           C,$04
5308: 0F         RRCA
5309: 06 0F      LD           B,$0F
530B: 07         RLCA
530C: 1F         RRA
530D: 07         RLCA
530E: 3B         DEC         SP
530F: 17         RLA
5310: 6D         LD           L,L
5311: 33         INC         SP
5312: 5E         LD           E,(HL)
5313: 21 FF 00   LD           HL,$00FF
5316: FE 01      CP           $01
5318: FC                              
5319: 03         INC         BC
531A: BC         CP           H
531B: 43         LD           B,E
531C: BE         CP           (HL)
531D: 61         LD           H,C
531E: 5B         LD           E,E
531F: 3C         INC         A
5320: 00         NOP
5321: 00         NOP
5322: 03         INC         BC
5323: 00         NOP
5324: 04         INC         B
5325: 03         INC         BC
5326: 09         ADD         HL,BC
5327: 07         RLCA
5328: 13         INC         DE
5329: 0F         RRCA
532A: F3         DI
532B: 0F         RRCA
532C: F1         POP         AF
532D: EE F3      XOR         $F3
532F: ED                              
5330: D3                              
5331: ED                              
5332: 23         INC         HL
5333: DD                              
5334: C1         POP         BC
5335: 3E 30      LD           A,$30
5337: CF         RST         0X08
5338: F9         LD           SP,HL
5339: D7         RST         0X10
533A: DD                              
533B: EB                              
533C: 2D         DEC         L
533D: F3         DI
533E: 81         ADD         A,C
533F: 7E         LD           A,(HL)
5340: 7F         LD           A,A
5341: 00         NOP
5342: F7         RST         0X30
5343: 38 9B      JR           C,$52E0
5345: 7D         LD           A,L
5346: 8F         ADC         A,A
5347: 7B         LD           A,E
5348: 8F         ADC         A,A
5349: 75         LD           (HL),L
534A: 4F         LD           C,A
534B: 35         DEC         (HL)
534C: 3B         DEC         SP
534D: 05         DEC         B
534E: 0C         INC         C
534F: 03         INC         BC
5350: 17         RLA
5351: 08 20 1F   LD           ($1F20),SP
5354: 2F         CPL
5355: 10 3F      STOP       $3F
5357: 00         NOP
5358: 27         DAA
5359: 18 4F      JR           $53AA
535B: 30 7F      JR           NC,$53DC
535D: 00         NOP
535E: 3F         CCF
535F: 00         NOP
5360: E3                              
5361: 1D         DEC         E
5362: F3         DI
5363: 0C         INC         C
5364: DB                              
5365: A5         AND         L
5366: CF         RST         0X08
5367: 30 E3      JR           NC,$534C
5369: DF         RST         0X18
536A: F1         POP         AF
536B: 8F         ADC         A,A
536C: BF         CP           A
536D: D0         RET         NC
536E: 6F         LD           L,A
536F: 9B         SBC         E
5370: B1         OR           C
5371: 4F         LD           C,A
5372: 0F         RRCA
5373: F0 04      LD           A,($04)
5375: FB         EI
5376: 87         ADD         A,A
5377: 78         LD           A,B
5378: CF         RST         0X08
5379: 30 FF      JR           NC,$537A
537B: 00         NOP
537C: F8 00      LDHL       SP,$00
537E: E0 00      LDFF00   ($00),A
5380: 00         NOP
5381: 00         NOP
5382: 00         NOP
5383: 00         NOP
5384: 00         NOP
5385: 00         NOP
5386: 03         INC         BC
5387: 00         NOP
5388: 05         DEC         B
5389: 03         INC         BC
538A: FB         EI
538B: 07         RLCA
538C: F3         DI
538D: EF         RST         0X28
538E: F3         DI
538F: EE D1      XOR         $D1
5391: EE 21      XOR         $21
5393: DE C1      SBC         $C1
5395: 3E 00      LD           A,$00
5397: FF         RST         0X38
5398: F8 E7      LDHL       SP,$E7
539A: 6D         LD           L,L
539B: F3         DI
539C: 15         DEC         D
539D: FB         EI
539E: 81         ADD         A,C
539F: 7E         LD           A,(HL)
53A0: FF         RST         0X38
53A1: 80         ADD         A,B
53A2: DF         RST         0X18
53A3: 3F         CCF
53A4: BF         CP           A
53A5: 7F         LD           A,A
53A6: 9F         SBC         A
53A7: 60         LD           H,B
53A8: BE         CP           (HL)
53A9: 41         LD           B,C
53AA: B7         OR           A
53AB: 48         LD           C,B
53AC: B1         OR           C
53AD: 4E         LD           C,(HL)
53AE: B4         OR           H
53AF: 4B         LD           C,E
53B0: BF         CP           A
53B1: 40         LD           B,B
53B2: B7         OR           A
53B3: 49         LD           C,C
53B4: B2         OR           D
53B5: 4D         LD           C,L
53B6: 9B         SBC         E
53B7: 64         LD           H,H
53B8: 8F         ADC         A,A
53B9: 70         LD           (HL),B
53BA: E4                              
53BB: 1B         DEC         DE
53BC: 31 0E 1F   LD           SP,$1F0E
53BF: 00         NOP
53C0: 00         NOP
53C1: 00         NOP
53C2: 00         NOP
53C3: 00         NOP
53C4: 00         NOP
53C5: 00         NOP
53C6: 00         NOP
53C7: 00         NOP
53C8: 00         NOP
53C9: 00         NOP
53CA: 00         NOP
53CB: 00         NOP
53CC: 1E 00      LD           E,$00
53CE: 3F         CCF
53CF: 10 6F      STOP       $6F
53D1: 31 5F 21   LD           SP,$215F
53D4: FF         RST         0X38
53D5: 00         NOP
53D6: FF         RST         0X38
53D7: 01 FD 03   LD           BC,$03FD
53DA: BC         CP           H
53DB: 43         LD           B,E
53DC: BE         CP           (HL)
53DD: 61         LD           H,C
53DE: 5B         LD           E,E
53DF: 3C         INC         A
53E0: 00         NOP
53E1: 00         NOP
53E2: 00         NOP
53E3: 00         NOP
53E4: 03         INC         BC
53E5: 00         NOP
53E6: 75         LD           (HL),L
53E7: 03         INC         BC
53E8: E9         JP           (HL)
53E9: 76         HALT
53EA: BB         CP           E
53EB: 44         LD           B,H
53EC: FF         RST         0X38
53ED: 00         NOP
53EE: FF         RST         0X38
53EF: 80         ADD         A,B
53F0: FF         RST         0X38
53F1: 00         NOP
53F2: E3                              
53F3: 1C         INC         E
53F4: DD                              
53F5: 3E DF      LD           A,$DF
53F7: 3E EF      LD           A,$EF
53F9: 1A         LD           A,(DE)
53FA: D1         POP         DE
53FB: EE 3F      XOR         $3F
53FD: E0 9F      LDFF00   ($9F),A
53FF: 6C         LD           L,H
5400: 00         NOP
5401: 00         NOP
5402: 00         NOP
5403: 00         NOP
5404: 03         INC         BC
5405: 00         NOP
5406: 02         LD           (BC),A
5407: 01 02 01   LD           BC,$0102
540A: 02         LD           (BC),A
540B: 01 0F 00   LD           BC,$000F
540E: 13         INC         DE
540F: 0C         INC         C
5410: 2D         DEC         L
5411: 1E 40      LD           E,$40
5413: 3F         CCF
5414: 70         LD           (HL),B
5415: 0F         RRCA
5416: 5D         LD           E,L
5417: 3E 9D      LD           A,$9D
5419: 7E         LD           A,(HL)
541A: 9B         SBC         E
541B: 7C         LD           A,H
541C: 85         ADD         A,L
541D: 7B         LD           A,E
541E: C8         RET         Z
541F: 37         SCF
5420: 07         RLCA
5421: 00         NOP
5422: 0D         DEC         C
5423: 02         LD           (BC),A
5424: CF         RST         0X08
5425: 00         NOP
5426: E9         JP           (HL)
5427: 87         ADD         A,A
5428: 72         LD           (HL),D
5429: CF         RST         0X08
542A: B1         OR           C
542B: 6E         LD           L,(HL)
542C: 42         LD           B,D
542D: BD         CP           L
542E: 25         DEC         H
542F: DB                              
5430: A5         AND         L
5431: 5B         LD           E,E
5432: CD 33 9A   CALL       $9A33
5435: 7D         LD           A,L
5436: 81         ADD         A,C
5437: 7E         LD           A,(HL)
5438: 9C         SBC         H
5439: 63         LD           H,E
543A: DF         RST         0X18
543B: 24         INC         H
543C: 7B         LD           A,E
543D: 86         ADD         A,(HL)
543E: BF         CP           A
543F: C0         RET         NZ
5440: 80         ADD         A,B
5441: 00         NOP
5442: 4E         LD           C,(HL)
5443: 80         ADD         A,B
5444: DE 04      SBC         $04
5446: FB         EI
5447: CC 33 EC   CALL       Z,$EC33
544A: CA 35 E7   JP           Z,$E735
544D: D9         RETI
544E: F5         PUSH       AF
544F: EB                              
5450: F4                              
5451: 2B         DEC         HL
5452: F6 29      OR           $29
5454: FB         EI
5455: DC C1 3E   CALL       C,$3EC1
5458: 1D         DEC         E
5459: E2         LDFF00   (C),A
545A: FD                              
545B: 12         LD           (DE),A
545C: E9         JP           (HL)
545D: 36 F1      LD           (HL),$F1
545F: 0E 38      LD           C,$38
5461: 00         NOP
5462: 7E         LD           A,(HL)
5463: 38 A7      JR           C,$540C
5465: 7A         LD           A,D
5466: 9F         SBC         A
5467: 62         LD           H,D
5468: 89         ADC         A,C
5469: 76         HALT
546A: E7         RST         0X20
546B: 98         SBC         B
546C: 85         ADD         A,L
546D: FA 12 EC   LD           A,($EC12)
5470: 0C         INC         C
5471: F0 84      LD           A,($84)
5473: 78         LD           A,B
5474: 04         INC         B
5475: F8 04      LDHL       SP,$04
5477: F8 38      LDHL       SP,$38
5479: C0         RET         NZ
547A: 10 E0      STOP       $E0
547C: B0         OR           B
547D: 40         LD           B,B
547E: F0 00      LD           A,($00)
5480: 83         ADD         A,E
5481: 7C         LD           A,H
5482: 80         ADD         A,B
5483: 7F         LD           A,A
5484: 66         LD           H,(HL)
5485: 1F         RRA
5486: 23         INC         HL
5487: 1F         RRA
5488: 30 0F      JR           NC,$5499
548A: 18 07      JR           $5493
548C: 1F         RRA
548D: 00         NOP
548E: 13         INC         DE
548F: 0C         INC         C
5490: 0C         INC         C
5491: 03         INC         BC
5492: 08 07 1E   LD           ($1E07),SP
5495: 01 2A 1F   LD           BC,$1F2A
5498: 24         INC         H
5499: 1B         DEC         DE
549A: 3F         CCF
549B: 00         NOP
549C: 00         NOP
549D: 03         INC         BC
549E: 00         NOP
549F: 00         NOP
54A0: 3E D9      LD           A,$D9
54A2: BD         CP           L
54A3: 72         LD           (HL),D
54A4: 3D         DEC         A
54A5: FE 3B      CP           $3B
54A7: FC                              
54A8: 15         DEC         D
54A9: FA 81 7E   LD           A,($7E81)
54AC: C3 3C 7F   JP           $7F3C
54AF: 80         ADD         A,B
54B0: 6F         LD           L,A
54B1: 90         SUB         B
54B2: 0D         DEC         C
54B3: F0 04      LD           A,($04)
54B5: F8 4C      LDHL       SP,$4C
54B7: F3         DI
54B8: 98         SBC         B
54B9: 67         LD           H,A
54BA: F0 0F      LD           A,($0F)
54BC: 00         NOP
54BD: FF         RST         0X38
54BE: 00         NOP
54BF: FF         RST         0X38
54C0: 03         INC         BC
54C1: FC                              
54C2: 1F         RRA
54C3: E0 FE      LDFF00   ($FE),A
54C5: 01 F9 06   LD           BC,$06F9
54C8: E3                              
54C9: 1C         INC         E
54CA: 0E F1      LD           C,$F1
54CC: FC                              
54CD: 03         INC         BC
54CE: FC                              
54CF: 03         INC         BC
54D0: FC                              
54D1: 03         INC         BC
54D2: DA 05 10   JP           C,$1005
54D5: 0F         RRCA
54D6: 20 DF      JR           NZ,$54B7
54D8: 20 DF      JR           NZ,$54B9
54DA: 39         ADD         HL,SP
54DB: C7         RST         0X00
54DC: 0C         INC         C
54DD: F3         DI
54DE: 07         RLCA
54DF: F8 E0      LDHL       SP,$E0
54E1: 00         NOP
54E2: A0         AND         B
54E3: 40         LD           B,B
54E4: 70         LD           (HL),B
54E5: 80         ADD         A,B
54E6: F8 00      LDHL       SP,$00
54E8: 6C         LD           L,H
54E9: F0 74      LD           A,($74)
54EB: F8 0A      LDHL       SP,$0A
54ED: FC                              
54EE: 1A         LD           A,(DE)
54EF: FC                              
54F0: 42         LD           B,D
54F1: BC         CP           H
54F2: 3C         INC         A
54F3: C0         RET         NZ
54F4: 08 F0 78   LD           ($78F0),SP
54F7: 80         ADD         A,B
54F8: 0C         INC         C
54F9: F2                              
54FA: 2A         LD           A,(HLI)
54FB: FD                              
54FC: 92         SUB         D
54FD: 6D         LD           L,L
54FE: FE 00      CP           $00
5500: 00         NOP
5501: 00         NOP
5502: 00         NOP
5503: 00         NOP
5504: 07         RLCA
5505: 00         NOP
5506: 1F         RRA
5507: 07         RLCA
5508: 3F         CCF
5509: 1F         RRA
550A: 7F         LD           A,A
550B: 3F         CCF
550C: 7F         LD           A,A
550D: 2E FF      LD           L,$FF
550F: 6E         LD           L,(HL)
5510: FF         RST         0X38
5511: 7F         LD           A,A
5512: FF         RST         0X38
5513: 7F         LD           A,A
5514: FF         RST         0X38
5515: 6E         LD           L,(HL)
5516: BF         CP           A
5517: 71         LD           (HL),C
5518: 5F         LD           E,A
5519: 3F         CCF
551A: 6F         LD           L,A
551B: 1F         RRA
551C: F8 67      LDHL       SP,$67
551E: FF         RST         0X38
551F: 00         NOP
5520: 00         NOP
5521: 00         NOP
5522: 00         NOP
5523: 00         NOP
5524: E0 00      LDFF00   ($00),A
5526: F8 E0      LDHL       SP,$E0
5528: FC                              
5529: F8 FE      LDHL       SP,$FE
552B: FC                              
552C: FE FC      CP           $FC
552E: FF         RST         0X38
552F: FE F7      CP           $F7
5531: EE F9      XOR         $F9
5533: F6 FF      OR           $FF
5535: F8 F9      LDHL       SP,$F9
5537: FE F2      CP           $F2
5539: FC                              
553A: DC E0 2E   CALL       C,$2EE0
553D: DC FE 00   CALL       C,$00FE
5540: 00         NOP
5541: 00         NOP
5542: 00         NOP
5543: 00         NOP
5544: 07         RLCA
5545: 00         NOP
5546: 1F         RRA
5547: 07         RLCA
5548: 3F         CCF
5549: 1F         RRA
554A: 7F         LD           A,A
554B: 3F         CCF
554C: 7F         LD           A,A
554D: 2F         CPL
554E: FF         RST         0X38
554F: 6F         LD           L,A
5550: FF         RST         0X38
5551: 7F         LD           A,A
5552: FF         RST         0X38
5553: 7F         LD           A,A
5554: FF         RST         0X38
5555: 77         LD           (HL),A
5556: BF         CP           A
5557: 78         LD           A,B
5558: 5F         LD           E,A
5559: 3F         CCF
555A: 6F         LD           L,A
555B: 1F         RRA
555C: F8 67      LDHL       SP,$67
555E: FF         RST         0X38
555F: 00         NOP
5560: 33         INC         SP
5561: 00         NOP
5562: 7F         LD           A,A
5563: 33         INC         SP
5564: 7F         LD           A,A
5565: 27         DAA
5566: 7F         LD           A,A
5567: 16 7F      LD           D,$7F
5569: 3F         CCF
556A: 7F         LD           A,A
556B: 3F         CCF
556C: FF         RST         0X38
556D: 60         LD           H,B
556E: FF         RST         0X38
556F: 40         LD           B,B
5570: FF         RST         0X38
5571: 40         LD           B,B
5572: FF         RST         0X38
5573: 40         LD           B,B
5574: FF         RST         0X38
5575: 40         LD           B,B
5576: BF         CP           A
5577: 60         LD           H,B
5578: 5F         LD           E,A
5579: 3F         CCF
557A: 6F         LD           L,A
557B: 1F         RRA
557C: F8 67      LDHL       SP,$67
557E: FF         RST         0X38
557F: 00         NOP
5580: C6 00      ADD         $00
5582: FF         RST         0X38
5583: C6 FF      ADD         $FF
5585: 6E         LD           L,(HL)
5586: FD                              
5587: DE F9      SBC         $F9
5589: FE F2      CP           $F2
558B: FC                              
558C: FD                              
558D: FA F9 7E   LD           A,($7EF9)
5590: F9         LD           SP,HL
5591: 3E F9      LD           A,$F9
5593: 3E F9      LD           A,$F9
5595: 2E F9      LD           L,$F9
5597: 6E         LD           L,(HL)
5598: F2                              
5599: DC DC E0   CALL       C,$E0DC
559C: 2E DC      LD           L,$DC
559E: FE 00      CP           $00
55A0: 00         NOP
55A1: 00         NOP
55A2: FF         RST         0X38
55A3: 00         NOP
55A4: FF         RST         0X38
55A5: FF         RST         0X38
55A6: FF         RST         0X38
55A7: FF         RST         0X38
55A8: FF         RST         0X38
55A9: FF         RST         0X38
55AA: FF         RST         0X38
55AB: FF         RST         0X38
55AC: FF         RST         0X38
55AD: FB         EI
55AE: FF         RST         0X38
55AF: FB         EI
55B0: FF         RST         0X38
55B1: FF         RST         0X38
55B2: FF         RST         0X38
55B3: FF         RST         0X38
55B4: FF         RST         0X38
55B5: F7         RST         0X30
55B6: FF         RST         0X38
55B7: 0F         RRCA
55B8: FF         RST         0X38
55B9: FF         RST         0X38
55BA: FF         RST         0X38
55BB: FF         RST         0X38
55BC: 00         NOP
55BD: FF         RST         0X38
55BE: FF         RST         0X38
55BF: 00         NOP
55C0: 00         NOP
55C1: 00         NOP
55C2: 30 00      JR           NC,$55C4
55C4: 7F         LD           A,A
55C5: 30 7F      JR           NC,$5646
55C7: 27         DAA
55C8: 7F         LD           A,A
55C9: 1F         RRA
55CA: 7F         LD           A,A
55CB: 2E 7F      LD           L,$7F
55CD: 2E FF      LD           L,$FF
55CF: 7F         LD           A,A
55D0: FF         RST         0X38
55D1: 7F         LD           A,A
55D2: FF         RST         0X38
55D3: 77         LD           (HL),A
55D4: FF         RST         0X38
55D5: 77         LD           (HL),A
55D6: BF         CP           A
55D7: 77         LD           (HL),A
55D8: 5F         LD           E,A
55D9: 3F         CCF
55DA: 6F         LD           L,A
55DB: 1F         RRA
55DC: F8 67      LDHL       SP,$67
55DE: FF         RST         0X38
55DF: 00         NOP
55E0: 00         NOP
55E1: 00         NOP
55E2: 06 00      LD           B,$00
55E4: EF         RST         0X28
55E5: 06 FF      LD           B,$FF
55E7: EE FD      XOR         $FD
55E9: FE F9      CP           $F9
55EB: FE F2      CP           $F2
55ED: FC                              
55EE: FD                              
55EF: FA F9 FE   LD           A,($FEF9)
55F2: F9         LD           SP,HL
55F3: FE F9      CP           $F9
55F5: FE F9      CP           $F9
55F7: FE F2      CP           $F2
55F9: FC                              
55FA: DC E0 2E   CALL       C,$2EE0
55FD: DC FE 00   CALL       C,$00FE
5600: 00         NOP
5601: 00         NOP
5602: 00         NOP
5603: 00         NOP
5604: 00         NOP
5605: 00         NOP
5606: 01 01 03   LD           BC,$0301
5609: 03         INC         BC
560A: 06 07      LD           B,$07
560C: 0D         DEC         C
560D: 0E 1B      LD           C,$1B
560F: 1C         INC         E
5610: 1E 19      LD           E,$19
5612: 14         INC         D
5613: 1B         DEC         DE
5614: 3C         INC         A
5615: 33         INC         SP
5616: 28 37      JR           Z,$564F
5618: 38 27      JR           C,$5641
561A: 38 27      JR           C,$5643
561C: 38 27      JR           C,$5645
561E: 38 27      JR           C,$5647
5620: 00         NOP
5621: 00         NOP
5622: 00         NOP
5623: 00         NOP
5624: 3F         CCF
5625: 3F         CCF
5626: EF         RST         0X28
5627: F0 3F      LD           A,($3F)
5629: C0         RET         NZ
562A: E0 1F      LDFF00   ($1F),A
562C: 80         ADD         A,B
562D: 7F         LD           A,A
562E: 00         NOP
562F: FF         RST         0X38
5630: 00         NOP
5631: FF         RST         0X38
5632: 07         RLCA
5633: FF         RST         0X38
5634: 1F         RRA
5635: FF         RST         0X38
5636: 3F         CCF
5637: FF         RST         0X38
5638: 3F         CCF
5639: FF         RST         0X38
563A: 7F         LD           A,A
563B: FF         RST         0X38
563C: 7F         LD           A,A
563D: FF         RST         0X38
563E: 7F         LD           A,A
563F: FF         RST         0X38
5640: 38 27      JR           C,$5669
5642: 78         LD           A,B
5643: 67         LD           H,A
5644: 78         LD           A,B
5645: 47         LD           B,A
5646: E4                              
5647: 9B         SBC         E
5648: CF         RST         0X08
5649: B0         OR           B
564A: DF         RST         0X18
564B: B0         OR           B
564C: DF         RST         0X18
564D: B0         OR           B
564E: D7         RST         0X10
564F: B8         CP           B
5650: 6F         LD           L,A
5651: 58         LD           E,B
5652: 77         LD           (HL),A
5653: 4C         LD           C,H
5654: 39         ADD         HL,SP
5655: 26 1F      LD           H,$1F
5657: 10 0F      STOP       $0F
5659: 0A         LD           A,(BC)
565A: 0D         DEC         C
565B: 0B         DEC         BC
565C: 0E 09      LD           C,$09
565E: 07         RLCA
565F: 04         INC         B
5660: 3F         CCF
5661: FF         RST         0X38
5662: 03         INC         BC
5663: FF         RST         0X38
5664: 7D         LD           A,L
5665: 83         ADD         A,E
5666: DE 39      SBC         $39
5668: 87         ADD         A,A
5669: 7C         LD           A,H
566A: FB         EI
566B: 06 B5      LD           B,$B5
566D: 7B         LD           A,E
566E: 7B         LD           A,E
566F: FD                              
5670: 7F         LD           A,A
5671: FD                              
5672: 7E         LD           A,(HL)
5673: FD                              
5674: 7E         LD           A,(HL)
5675: E5         PUSH       HL
5676: BF         CP           A
5677: 64         LD           H,H
5678: C6 39      ADD         $39
567A: FC                              
567B: 03         INC         BC
567C: F1         POP         AF
567D: 0E FF      LD           C,$FF
567F: 61         LD           H,C
5680: 00         NOP
5681: 00         NOP
5682: 03         INC         BC
5683: 03         INC         BC
5684: 07         RLCA
5685: 04         INC         B
5686: 0E 09      LD           C,$09
5688: 7D         LD           A,L
5689: 73         LD           (HL),E
568A: FB         EI
568B: 86         ADD         A,(HL)
568C: DB                              
568D: 34         INC         (HL)
568E: BF         CP           A
568F: 60         LD           H,B
5690: F8 07      LDHL       SP,$07
5692: F7         RST         0X30
5693: 8F         ADC         A,A
5694: EF         RST         0X28
5695: 9F         SBC         A
5696: EF         RST         0X28
5697: 13         INC         DE
5698: AF         XOR         A
5699: 53         LD           D,E
569A: BF         CP           A
569B: 4F         LD           C,A
569C: 9F         SBC         A
569D: 60         LD           H,B
569E: C9         RET
569F: B7         OR           A
56A0: F8 F8      LDHL       SP,$F8
56A2: FE 06      CP           $06
56A4: 8F         ADC         A,A
56A5: 73         LD           (HL),E
56A6: 3F         CCF
56A7: C0         RET         NZ
56A8: FF         RST         0X38
56A9: 00         NOP
56AA: F0 0F      LD           A,($0F)
56AC: E0 1F      LDFF00   ($1F),A
56AE: E0 1F      LDFF00   ($1F),A
56B0: 70         LD           (HL),B
56B1: 8F         ADC         A,A
56B2: A9         XOR         C
56B3: D7         RST         0X10
56B4: E5         PUSH       HL
56B5: DB                              
56B6: ED                              
56B7: DB                              
56B8: AD         XOR         L
56B9: DB                              
56BA: 5D         LD           E,L
56BB: B3         OR           E
56BC: BB         CP           E
56BD: 67         LD           H,A
56BE: F7         RST         0X30
56BF: CF         RST         0X08
56C0: 00         NOP
56C1: 00         NOP
56C2: 04         INC         B
56C3: 04         INC         B
56C4: 00         NOP
56C5: 00         NOP
56C6: 18 18      JR           $56E0
56C8: 18 18      JR           $56E2
56CA: 06 06      LD           B,$06
56CC: 46         LD           B,(HL)
56CD: 46         LD           B,(HL)
56CE: 00         NOP
56CF: 00         NOP
56D0: 18 18      JR           $56EA
56D2: 1D         DEC         E
56D3: 1D         DEC         E
56D4: 0D         DEC         C
56D5: 0D         DEC         C
56D6: 01 01 47   LD           BC,$4701
56D9: 47         LD           B,A
56DA: 06 06      LD           B,$06
56DC: 00         NOP
56DD: 00         NOP
56DE: 00         NOP
56DF: 00         NOP
56E0: 00         NOP
56E1: 00         NOP
56E2: 10 10      STOP       $10
56E4: 00         NOP
56E5: 00         NOP
56E6: C0         RET         NZ
56E7: C0         RET         NZ
56E8: E0 E0      LDFF00   ($E0),A
56EA: 6C         LD           L,H
56EB: 6C         LD           L,H
56EC: 0C         INC         C
56ED: 0C         INC         C
56EE: 78         LD           A,B
56EF: 78         LD           A,B
56F0: 78         LD           A,B
56F1: 78         LD           A,B
56F2: 98         SBC         B
56F3: 98         SBC         B
56F4: 9C         SBC         H
56F5: 9C         SBC         H
56F6: FC                              
56F7: FC                              
56F8: FE FE      CP           $FE
56FA: 3E 3E      LD           A,$3E
56FC: 0E 0E      LD           C,$0E
56FE: 00         NOP
56FF: 00         NOP
5700: 00         NOP
5701: 00         NOP
5702: 00         NOP
5703: 00         NOP
5704: 00         NOP
5705: 00         NOP
5706: 00         NOP
5707: 00         NOP
5708: 01 00 07   LD           BC,$0700
570B: 00         NOP
570C: 0F         RRCA
570D: 00         NOP
570E: 1F         RRA
570F: 00         NOP
5710: 3F         CCF
5711: 00         NOP
5712: 3F         CCF
5713: 01 5F 21   LD           BC,$215F
5716: 6E         LD           L,(HL)
5717: 31 57 38   LD           SP,$3857
571A: 2D         DEC         L
571B: 1E 1B      LD           E,$1B
571D: 07         RLCA
571E: 07         RLCA
571F: 00         NOP
5720: 00         NOP
5721: 00         NOP
5722: 00         NOP
5723: 00         NOP
5724: 00         NOP
5725: 00         NOP
5726: 3F         CCF
5727: 00         NOP
5728: FF         RST         0X38
5729: 00         NOP
572A: FF         RST         0X38
572B: 00         NOP
572C: FF         RST         0X38
572D: 00         NOP
572E: FF         RST         0X38
572F: 00         NOP
5730: FF         RST         0X38
5731: E0 FF      LDFF00   ($FF),A
5733: 30 FF      JR           NC,$5734
5735: 30 EF      JR           NC,$5726
5737: F0 1F      LD           A,($1F)
5739: E0 FD      LDFF00   ($FD),A
573B: 03         INC         BC
573C: FF         RST         0X38
573D: FF         RST         0X38
573E: FF         RST         0X38
573F: 00         NOP
5740: 20 00      JR           NZ,$5742
5742: 20 00      JR           NZ,$5744
5744: 60         LD           H,B
5745: 00         NOP
5746: E0 00      LDFF00   ($00),A
5748: F0 00      LD           A,($00)
574A: F8 00      LDHL       SP,$00
574C: FC                              
574D: 00         NOP
574E: FE 00      CP           $00
5750: FE 00      CP           $00
5752: D7         RST         0X10
5753: 38 FB      JR           C,$5750
5755: 2C         INC         L
5756: BD         CP           L
5757: 76         HALT
5758: 77         LD           (HL),A
5759: F8 E4      LDHL       SP,$E4
575B: F8 98      LDHL       SP,$98
575D: E0 E0      LDFF00   ($E0),A
575F: 00         NOP
5760: 03         INC         BC
5761: 00         NOP
5762: 06 03      LD           B,$03
5764: 0D         DEC         C
5765: 06 0B      LD           B,$0B
5767: 04         INC         B
5768: 1F         RRA
5769: 00         NOP
576A: 1F         RRA
576B: 01 1F 01   LD           BC,$011F
576E: 2E 11      LD           L,$11
5770: 3F         CCF
5771: 10 37      STOP       $37
5773: 18 3B      JR           $57B0
5775: 1C         INC         E
5776: 2E 1F      LD           L,$1F
5778: 17         RLA
5779: 0F         RRCA
577A: 0B         DEC         BC
577B: 07         RLCA
577C: 06 01      LD           B,$01
577E: 01 00 81   LD           BC,$8100
5781: 00         NOP
5782: FD                              
5783: 00         NOP
5784: FF         RST         0X38
5785: 00         NOP
5786: FF         RST         0X38
5787: 00         NOP
5788: FF         RST         0X38
5789: E0 FF      LDFF00   ($FF),A
578B: 30 FF      JR           NC,$578C
578D: 30 EF      JR           NC,$577E
578F: F0 1F      LD           A,($1F)
5791: E0 FF      LDFF00   ($FF),A
5793: 00         NOP
5794: FE 01      CP           $01
5796: FB         EI
5797: 07         RLCA
5798: FF         RST         0X38
5799: FF         RST         0X38
579A: FF         RST         0X38
579B: FF         RST         0X38
579C: 00         NOP
579D: FF         RST         0X38
579E: FF         RST         0X38
579F: 00         NOP
57A0: CC 00 B8   CALL       Z,$B800
57A3: C0         RET         NZ
57A4: F0 C0      LD           A,($C0)
57A6: 50         LD           D,B
57A7: E0 F0      LDFF00   ($F0),A
57A9: 60         LD           H,B
57AA: A8         XOR         B
57AB: 70         LD           (HL),B
57AC: F8 30      LDHL       SP,$30
57AE: F4                              
57AF: 38 BC      JR           C,$576D
57B1: 78         LD           A,B
57B2: 7C         LD           A,H
57B3: F8 F4      LDHL       SP,$F4
57B5: F8 E4      LDHL       SP,$E4
57B7: F8 C8      LDHL       SP,$C8
57B9: F0 10      LD           A,($10)
57BB: E0 60      LDFF00   ($60),A
57BD: 80         ADD         A,B
57BE: 80         ADD         A,B
57BF: 00         NOP
57C0: 00         NOP
57C1: 00         NOP
57C2: 00         NOP
57C3: 00         NOP
57C4: 00         NOP
57C5: 00         NOP
57C6: 00         NOP
57C7: 00         NOP
57C8: 00         NOP
57C9: 00         NOP
57CA: 00         NOP
57CB: 00         NOP
57CC: 00         NOP
57CD: 00         NOP
57CE: 00         NOP
57CF: 00         NOP
57D0: 00         NOP
57D1: 00         NOP
57D2: 00         NOP
57D3: 00         NOP
57D4: 70         LD           (HL),B
57D5: 00         NOP
57D6: D8         RET         C
57D7: 20 F8      JR           NZ,$57D1
57D9: 00         NOP
57DA: F8 00      LDHL       SP,$00
57DC: 70         LD           (HL),B
57DD: 00         NOP
57DE: 20 00      JR           NZ,$57E0
57E0: 07         RLCA
57E1: 00         NOP
57E2: 1F         RRA
57E3: 00         NOP
57E4: 3E 01      LD           A,$01
57E6: 7D         LD           A,L
57E7: 03         INC         BC
57E8: 7D         LD           A,L
57E9: 03         INC         BC
57EA: FE 01      CP           $01
57EC: FF         RST         0X38
57ED: 00         NOP
57EE: FF         RST         0X38
57EF: 00         NOP
57F0: BF         CP           A
57F1: 40         LD           B,B
57F2: BF         CP           A
57F3: 40         LD           B,B
57F4: 9F         SBC         A
57F5: 60         LD           H,B
57F6: 47         LD           B,A
57F7: 38 40      JR           C,$5839
57F9: 3F         CCF
57FA: 20 1F      JR           NZ,$581B
57FC: 18 07      JR           $5805
57FE: 07         RLCA
57FF: 00         NOP
5800: 0F         RRCA
5801: 00         NOP
5802: 1B         DEC         DE
5803: 07         RLCA
5804: 2F         CPL
5805: 1F         RRA
5806: 3F         CCF
5807: 1F         RRA
5808: 5F         LD           E,A
5809: 33         INC         SP
580A: 7F         LD           A,A
580B: 33         INC         SP
580C: 7F         LD           A,A
580D: 33         INC         SP
580E: 7F         LD           A,A
580F: 3F         CCF
5810: 5F         LD           E,A
5811: 3C         INC         A
5812: 7F         LD           A,A
5813: 1C         INC         E
5814: EF         RST         0X28
5815: 5F         LD           E,A
5816: D8         RET         C
5817: 67         LD           H,A
5818: 97         SUB         A
5819: 68         LD           L,B
581A: 78         LD           A,B
581B: 07         RLCA
581C: 7C         LD           A,H
581D: 3B         DEC         SP
581E: 7F         LD           A,A
581F: 00         NOP
5820: F0 00      LD           A,($00)
5822: 68         LD           L,B
5823: 90         SUB         B
5824: D4 E8 F2   CALL       NC,$F2E8
5827: EC                              
5828: EA 34 F9   LD           ($F934),A
582B: 36 F9      LD           (HL),$F9
582D: 36 FE      LD           (HL),$FE
582F: F0 EA      LD           A,($EA)
5831: F4                              
5832: D1         POP         DE
5833: EE A9      XOR         $A9
5835: DE 75      SBC         $75
5837: 9A         SBC         D
5838: A5         AND         L
5839: 5A         LD           E,D
583A: 19         ADD         HL,DE
583B: E6 06      AND         $06
583D: F8 FC      LDHL       SP,$FC
583F: 00         NOP
5840: 03         INC         BC
5841: 00         NOP
5842: 0C         INC         C
5843: 03         INC         BC
5844: 13         INC         DE
5845: 0F         RRCA
5846: 26 1F      LD           H,$1F
5848: 24         INC         H
5849: 1F         RRA
584A: 20 1F      JR           NZ,$586B
584C: 30 0F      JR           NC,$585D
584E: 30 0F      JR           NC,$585F
5850: 28 17      JR           Z,$5869
5852: 47         LD           B,A
5853: 38 40      JR           C,$5895
5855: 3F         CCF
5856: 40         LD           B,B
5857: 3F         CCF
5858: 60         LD           H,B
5859: 1F         RRA
585A: 40         LD           B,B
585B: 3F         CCF
585C: 20 1F      JR           NZ,$587D
585E: 1F         RRA
585F: 00         NOP
5860: E0 00      LDFF00   ($00),A
5862: 18 E0      JR           $5844
5864: 04         INC         B
5865: F8 04      LDHL       SP,$04
5867: F8 02      LDHL       SP,$02
5869: FC                              
586A: 02         LD           (BC),A
586B: FC                              
586C: 22         LD           (HLI),A
586D: DC 3A C4   CALL       C,$C43A
5870: C6 38      ADD         $38
5872: 03         INC         BC
5873: FC                              
5874: 01 FE 41   LD           BC,$41FE
5877: BE         CP           (HL)
5878: 89         ADC         A,C
5879: 76         HALT
587A: 3E C0      LD           A,$C0
587C: 7C         LD           A,H
587D: B8         CP           B
587E: FC                              
587F: 00         NOP
5880: 3F         CCF
5881: 00         NOP
5882: 56         LD           D,(HL)
5883: 39         ADD         HL,SP
5884: 7B         LD           A,E
5885: 3C         INC         A
5886: BF         CP           A
5887: 7C         LD           A,H
5888: FD                              
5889: 26 FF      LD           H,$FF
588B: 26 FF      LD           H,$FF
588D: 26 BF      LD           H,$BF
588F: 7E         LD           A,(HL)
5890: BD         CP           L
5891: 5E         LD           E,(HL)
5892: BB         CP           E
5893: 5C         LD           E,H
5894: 75         LD           (HL),L
5895: 3B         DEC         SP
5896: 4A         LD           C,D
5897: 37         SCF
5898: 79         LD           A,C
5899: 06 3E      LD           B,$3E
589B: 01 7B 3C   LD           BC,$3C7B
589E: 7F         LD           A,A
589F: 00         NOP
58A0: F0 00      LD           A,($00)
58A2: CC F0 02   CALL       Z,$02F0
58A5: FC                              
58A6: 01 FE 81   LD           BC,$81FE
58A9: 7E         LD           A,(HL)
58AA: 91         SUB         C
58AB: 6E         LD           L,(HL)
58AC: FD                              
58AD: 02         LD           (BC),A
58AE: 8B         ADC         A,E
58AF: 70         LD           (HL),B
58B0: 08 F0 8C   LD           ($8CF0),SP
58B3: 70         LD           (HL),B
58B4: 12         LD           (DE),A
58B5: EC                              
58B6: 81         ADD         A,C
58B7: 7E         LD           A,(HL)
58B8: 07         RLCA
58B9: F8 1F      LDHL       SP,$1F
58BB: E2         LDFF00   (C),A
58BC: FF         RST         0X38
58BD: 1C         INC         E
58BE: FE 00      CP           $00
58C0: 3F         CCF
58C1: 00         NOP
58C2: 5B         LD           E,E
58C3: 3C         INC         A
58C4: 7D         LD           A,L
58C5: 3E BF      LD           A,$BF
58C7: 7E         LD           A,(HL)
58C8: FE 53      CP           $53
58CA: FF         RST         0X38
58CB: 53         LD           D,E
58CC: FF         RST         0X38
58CD: 53         LD           D,E
58CE: FF         RST         0X38
58CF: 7F         LD           A,A
58D0: FE 6F      CP           $6F
58D2: BD         CP           L
58D3: 6E         LD           L,(HL)
58D4: 7A         LD           A,D
58D5: 3D         DEC         A
58D6: C5         PUSH       BC
58D7: 3B         DEC         SP
58D8: BC         CP           H
58D9: 43         LD           B,E
58DA: FF         RST         0X38
58DB: 00         NOP
58DC: 1F         RRA
58DD: 07         RLCA
58DE: 3F         CCF
58DF: 00         NOP
58E0: E0 00      LDFF00   ($00),A
58E2: 58         LD           E,B
58E3: E0 84      LDFF00   ($84),A
58E5: 78         LD           A,B
58E6: 82         ADD         A,D
58E7: 7C         LD           A,H
58E8: C2 3C D2   JP           NZ,$D23C
58EB: 2C         INC         L
58EC: FA 04 CE   LD           A,($CE04)
58EF: 30 88      JR           NC,$5879
58F1: 70         LD           (HL),B
58F2: C8         RET         Z
58F3: 30 8C      JR           NC,$5881
58F5: F0 42      LD           A,($42)
58F7: BC         CP           H
58F8: 81         ADD         A,C
58F9: 7E         LD           A,(HL)
58FA: C1         POP         BC
58FB: 3E FF      LD           A,$FF
58FD: C0         RET         NZ
58FE: FC                              
58FF: 00         NOP
5900: 07         RLCA
5901: 00         NOP
5902: 1F         RRA
5903: 02         LD           (BC),A
5904: 3F         CCF
5905: 03         INC         BC
5906: 7F         LD           A,A
5907: 00         NOP
5908: 7B         LD           A,E
5909: 07         RLCA
590A: F7         RST         0X30
590B: 0F         RRCA
590C: EF         RST         0X28
590D: 1E FE      LD           E,$FE
590F: 1D         DEC         E
5910: FC                              
5911: 1B         DEC         DE
5912: FC                              
5913: 1B         DEC         DE
5914: FE 1D      CP           $1D
5916: 6F         LD           L,A
5917: 1E 77      LD           E,$77
5919: 0F         RRCA
591A: BB         CP           E
591B: 67         LD           H,A
591C: 8F         ADC         A,A
591D: 70         LD           (HL),B
591E: 7C         LD           A,H
591F: 00         NOP
5920: F0 00      LD           A,($00)
5922: FC                              
5923: 20 FE      JR           NZ,$5923
5925: 60         LD           H,B
5926: FE 00      CP           $00
5928: EF         RST         0X28
5929: F0 F7      LD           A,($F7)
592B: 78         LD           A,B
592C: 7B         LD           A,E
592D: BC         CP           H
592E: 3F         CCF
592F: DC 1F EC   CALL       C,$EC1F
5932: 1F         RRA
5933: EC                              
5934: 3E DC      LD           A,$DC
5936: 7A         LD           A,D
5937: BC         CP           H
5938: F5         PUSH       AF
5939: 7A         LD           A,D
593A: ED                              
593B: F2                              
593C: FE 00      CP           $00
593E: 00         NOP
593F: 00         NOP
5940: 07         RLCA
5941: 00         NOP
5942: 1F         RRA
5943: 02         LD           (BC),A
5944: 3F         CCF
5945: 03         INC         BC
5946: 7F         LD           A,A
5947: 00         NOP
5948: 7B         LD           A,E
5949: 07         RLCA
594A: F7         RST         0X30
594B: 0F         RRCA
594C: EF         RST         0X28
594D: 1C         INC         E
594E: FC                              
594F: 1B         DEC         DE
5950: FC                              
5951: 1B         DEC         DE
5952: FC                              
5953: 1B         DEC         DE
5954: FE 1D      CP           $1D
5956: 6F         LD           L,A
5957: 1E 77      LD           E,$77
5959: 0F         RRCA
595A: BB         CP           E
595B: 67         LD           H,A
595C: 8F         ADC         A,A
595D: 70         LD           (HL),B
595E: 7C         LD           A,H
595F: 00         NOP
5960: F0 00      LD           A,($00)
5962: FC                              
5963: 20 FE      JR           NZ,$5963
5965: 60         LD           H,B
5966: FE 00      CP           $00
5968: EF         RST         0X28
5969: F0 F7      LD           A,($F7)
596B: F8 FB      LDHL       SP,$FB
596D: 9C         SBC         H
596E: 9F         SBC         A
596F: 6C         LD           L,H
5970: 1F         RRA
5971: EC                              
5972: 1F         RRA
5973: EC                              
5974: 3E DC      LD           A,$DC
5976: 7A         LD           A,D
5977: BC         CP           H
5978: F5         PUSH       AF
5979: 7A         LD           A,D
597A: ED                              
597B: F2                              
597C: FE 00      CP           $00
597E: 00         NOP
597F: 00         NOP
5980: 07         RLCA
5981: 00         NOP
5982: 1F         RRA
5983: 02         LD           (BC),A
5984: 3F         CCF
5985: 03         INC         BC
5986: 7F         LD           A,A
5987: 00         NOP
5988: 7B         LD           A,E
5989: 07         RLCA
598A: F7         RST         0X30
598B: 0F         RRCA
598C: EF         RST         0X28
598D: 1E FF      LD           E,$FF
598F: 1C         INC         E
5990: FF         RST         0X38
5991: 18 FF      JR           $5992
5993: 18 FF      JR           $5994
5995: 18 6E      JR           $5A05
5997: 1F         RRA
5998: 77         LD           (HL),A
5999: 0E BB      LD           C,$BB
599B: 67         LD           H,A
599C: 8F         ADC         A,A
599D: 70         LD           (HL),B
599E: 7C         LD           A,H
599F: 00         NOP
59A0: F0 00      LD           A,($00)
59A2: FC                              
59A3: 20 FE      JR           NZ,$59A3
59A5: 60         LD           H,B
59A6: FE 00      CP           $00
59A8: EF         RST         0X28
59A9: F0 F7      LD           A,($F7)
59AB: 78         LD           A,B
59AC: FB         EI
59AD: 3C         INC         A
59AE: FF         RST         0X38
59AF: 1C         INC         E
59B0: FF         RST         0X38
59B1: 0C         INC         C
59B2: FF         RST         0X38
59B3: 0C         INC         C
59B4: FE 0C      CP           $0C
59B6: BA         CP           D
59B7: 7C         LD           A,H
59B8: F5         PUSH       AF
59B9: 3A         LD           A,(HLD)
59BA: ED                              
59BB: F2                              
59BC: FE 00      CP           $00
59BE: 00         NOP
59BF: 00         NOP
59C0: 07         RLCA
59C1: 00         NOP
59C2: 1F         RRA
59C3: 02         LD           (BC),A
59C4: 3F         CCF
59C5: 03         INC         BC
59C6: 7F         LD           A,A
59C7: 00         NOP
59C8: 7B         LD           A,E
59C9: 07         RLCA
59CA: F7         RST         0X30
59CB: 0F         RRCA
59CC: EF         RST         0X28
59CD: 1E FF      LD           E,$FF
59CF: 1E FF      LD           E,$FF
59D1: 19         ADD         HL,DE
59D2: FF         RST         0X38
59D3: 10 FF      STOP       $FF
59D5: 10 6F      STOP       $6F
59D7: 19         ADD         HL,DE
59D8: 77         LD           (HL),A
59D9: 0F         RRCA
59DA: BB         CP           E
59DB: 67         LD           H,A
59DC: 8F         ADC         A,A
59DD: 70         LD           (HL),B
59DE: 7C         LD           A,H
59DF: 00         NOP
59E0: F0 00      LD           A,($00)
59E2: FC                              
59E3: 20 FE      JR           NZ,$59E3
59E5: 60         LD           H,B
59E6: FE 00      CP           $00
59E8: EF         RST         0X28
59E9: F0 F7      LD           A,($F7)
59EB: 78         LD           A,B
59EC: FB         EI
59ED: 3C         INC         A
59EE: FF         RST         0X38
59EF: 3C         INC         A
59F0: FF         RST         0X38
59F1: 4C         LD           C,H
59F2: FF         RST         0X38
59F3: 04         INC         B
59F4: FE 04      CP           $04
59F6: FA 4C F5   LD           A,($F54C)
59F9: 7A         LD           A,D
59FA: ED                              
59FB: F2                              
59FC: FE 00      CP           $00
59FE: 00         NOP
59FF: 00         NOP
5A00: 00         NOP
5A01: 00         NOP
5A02: 00         NOP
5A03: 00         NOP
5A04: 00         NOP
5A05: 00         NOP
5A06: 00         NOP
5A07: 00         NOP
5A08: 00         NOP
5A09: 00         NOP
5A0A: 00         NOP
5A0B: 00         NOP
5A0C: 00         NOP
5A0D: 00         NOP
5A0E: 00         NOP
5A0F: 00         NOP
5A10: 30 00      JR           NC,$5A12
5A12: 7B         LD           A,E
5A13: 30 FF      JR           NC,$5A14
5A15: 3A         LD           A,(HLD)
5A16: DF         RST         0X18
5A17: 76         HALT
5A18: B7         OR           A
5A19: 7E         LD           A,(HL)
5A1A: 5D         LD           E,L
5A1B: 3E 23      LD           A,$23
5A1D: 1C         INC         E
5A1E: 3C         INC         A
5A1F: 00         NOP
5A20: 00         NOP
5A21: 00         NOP
5A22: 00         NOP
5A23: 00         NOP
5A24: 00         NOP
5A25: 00         NOP
5A26: 00         NOP
5A27: 00         NOP
5A28: 60         LD           H,B
5A29: 00         NOP
5A2A: 70         LD           (HL),B
5A2B: 20 5F      JR           NZ,$5A8C
5A2D: 30 2B      JR           NC,$5A5A
5A2F: 17         RLA
5A30: 31 0F 27   LD           SP,$270F
5A33: 18 27      JR           $5A5C
5A35: 1A         LD           A,(DE)
5A36: 3F         CCF
5A37: 00         NOP
5A38: 2D         DEC         L
5A39: 1E 5B      LD           E,$5B
5A3B: 3E 45      LD           A,$45
5A3D: 3A         LD           A,(HLD)
5A3E: 3E 00      LD           A,$00
5A40: 30 00      JR           NC,$5A42
5A42: 38 10      JR           C,$5A54
5A44: 3F         CCF
5A45: 10 37      STOP       $37
5A47: 0F         RRCA
5A48: 23         INC         HL
5A49: 1F         RRA
5A4A: 2F         CPL
5A4B: 10 2F      STOP       $2F
5A4D: 14         INC         D
5A4E: 2F         CPL
5A4F: 10 22      STOP       $22
5A51: 1D         DEC         E
5A52: 62         LD           H,D
5A53: 1D         DEC         E
5A54: 90         SUB         B
5A55: 6F         LD           L,A
5A56: 9F         SBC         A
5A57: 60         LD           H,B
5A58: AD         XOR         L
5A59: 5E         LD           E,(HL)
5A5A: 5B         LD           E,E
5A5B: 3E 45      LD           A,$45
5A5D: 3A         LD           A,(HLD)
5A5E: 3E 00      LD           A,$00
5A60: 06 00      LD           B,$00
5A62: 0E 04      LD           C,$04
5A64: FA 0C B4   LD           A,($B40C)
5A67: D8         RET         C
5A68: 18 E0      JR           $5A4A
5A6A: E4                              
5A6B: 18 E4      JR           $5A51
5A6D: 98         SBC         B
5A6E: E4                              
5A6F: 18 04      JR           $5A75
5A71: F8 1A      LDHL       SP,$1A
5A73: E4                              
5A74: 35         DEC         (HL)
5A75: CE F9      ADC         $F9
5A77: 06 B5      LD           B,$B5
5A79: 7A         LD           A,D
5A7A: DA 7C A2   JP           C,$A27C
5A7D: 5C         LD           E,H
5A7E: 7C         LD           A,H
5A7F: 00         NOP
5A80: 00         NOP
5A81: FF         RST         0X38
5A82: 00         NOP
5A83: FF         RST         0X38
5A84: 24         INC         H
5A85: FF         RST         0X38
5A86: 18 FF      JR           $5A87
5A88: 18 FF      JR           $5A89
5A8A: 24         INC         H
5A8B: FF         RST         0X38
5A8C: 00         NOP
5A8D: FF         RST         0X38
5A8E: 00         NOP
5A8F: FF         RST         0X38
5A90: 00         NOP
5A91: FF         RST         0X38
5A92: 00         NOP
5A93: FF         RST         0X38
5A94: 24         INC         H
5A95: FF         RST         0X38
5A96: 18 FF      JR           $5A97
5A98: 18 FF      JR           $5A99
5A9A: 24         INC         H
5A9B: FF         RST         0X38
5A9C: 00         NOP
5A9D: FF         RST         0X38
5A9E: 00         NOP
5A9F: FF         RST         0X38
5AA0: 00         NOP
5AA1: FF         RST         0X38
5AA2: 00         NOP
5AA3: FF         RST         0X38
5AA4: 24         INC         H
5AA5: FF         RST         0X38
5AA6: 18 FF      JR           $5AA7
5AA8: 18 FF      JR           $5AA9
5AAA: 24         INC         H
5AAB: FF         RST         0X38
5AAC: 00         NOP
5AAD: FF         RST         0X38
5AAE: 00         NOP
5AAF: FF         RST         0X38
5AB0: 00         NOP
5AB1: FF         RST         0X38
5AB2: 00         NOP
5AB3: FF         RST         0X38
5AB4: 24         INC         H
5AB5: FF         RST         0X38
5AB6: 18 FF      JR           $5AB7
5AB8: 18 FF      JR           $5AB9
5ABA: 24         INC         H
5ABB: FF         RST         0X38
5ABC: 00         NOP
5ABD: FF         RST         0X38
5ABE: 00         NOP
5ABF: FF         RST         0X38
5AC0: 00         NOP
5AC1: FF         RST         0X38
5AC2: 00         NOP
5AC3: FF         RST         0X38
5AC4: 24         INC         H
5AC5: FF         RST         0X38
5AC6: 18 FF      JR           $5AC7
5AC8: 18 FF      JR           $5AC9
5ACA: 24         INC         H
5ACB: FF         RST         0X38
5ACC: 00         NOP
5ACD: FF         RST         0X38
5ACE: 00         NOP
5ACF: FF         RST         0X38
5AD0: 00         NOP
5AD1: FF         RST         0X38
5AD2: 00         NOP
5AD3: FF         RST         0X38
5AD4: 24         INC         H
5AD5: FF         RST         0X38
5AD6: 18 FF      JR           $5AD7
5AD8: 18 FF      JR           $5AD9
5ADA: 24         INC         H
5ADB: FF         RST         0X38
5ADC: 00         NOP
5ADD: FF         RST         0X38
5ADE: 00         NOP
5ADF: FF         RST         0X38
5AE0: 00         NOP
5AE1: FF         RST         0X38
5AE2: 00         NOP
5AE3: FF         RST         0X38
5AE4: 24         INC         H
5AE5: FF         RST         0X38
5AE6: 18 FF      JR           $5AE7
5AE8: 18 FF      JR           $5AE9
5AEA: 24         INC         H
5AEB: FF         RST         0X38
5AEC: 00         NOP
5AED: FF         RST         0X38
5AEE: 00         NOP
5AEF: FF         RST         0X38
5AF0: 00         NOP
5AF1: FF         RST         0X38
5AF2: 00         NOP
5AF3: FF         RST         0X38
5AF4: 24         INC         H
5AF5: FF         RST         0X38
5AF6: 18 FF      JR           $5AF7
5AF8: 18 FF      JR           $5AF9
5AFA: 24         INC         H
5AFB: FF         RST         0X38
5AFC: 00         NOP
5AFD: FF         RST         0X38
5AFE: 00         NOP
5AFF: FF         RST         0X38
5B00: 39         ADD         HL,SP
5B01: 00         NOP
5B02: 73         LD           (HL),E
5B03: 00         NOP
5B04: 7F         LD           A,A
5B05: 00         NOP
5B06: 7F         LD           A,A
5B07: 00         NOP
5B08: 7F         LD           A,A
5B09: 00         NOP
5B0A: 3F         CCF
5B0B: 00         NOP
5B0C: 3F         CCF
5B0D: 1D         DEC         E
5B0E: 17         RLA
5B0F: 0D         DEC         C
5B10: 0B         DEC         BC
5B11: 07         RLCA
5B12: 1F         RRA
5B13: 00         NOP
5B14: 3D         DEC         A
5B15: 1A         LD           A,(DE)
5B16: 3E 1B      LD           A,$1B
5B18: 79         LD           A,C
5B19: 07         RLCA
5B1A: 78         LD           A,B
5B1B: 07         RLCA
5B1C: 7F         LD           A,A
5B1D: 00         NOP
5B1E: 4F         LD           C,A
5B1F: 00         NOP
5B20: E0 00      LDFF00   ($00),A
5B22: F8 00      LDHL       SP,$00
5B24: FC                              
5B25: 00         NOP
5B26: FC                              
5B27: 00         NOP
5B28: FE 00      CP           $00
5B2A: FE 6C      CP           $6C
5B2C: FA BC EC   LD           A,($ECBC)
5B2F: B0         OR           B
5B30: D8         RET         C
5B31: E0 FC      LDFF00   ($FC),A
5B33: 00         NOP
5B34: DE 20      SBC         $20
5B36: 3E EC      LD           A,$EC
5B38: DF         RST         0X18
5B39: EC                              
5B3A: 7F         LD           A,A
5B3B: 80         ADD         A,B
5B3C: BD         CP           L
5B3D: 78         LD           A,B
5B3E: F8 00      LDHL       SP,$00
5B40: 73         LD           (HL),E
5B41: 00         NOP
5B42: E7         RST         0X20
5B43: 00         NOP
5B44: FF         RST         0X38
5B45: 00         NOP
5B46: FF         RST         0X38
5B47: 00         NOP
5B48: FF         RST         0X38
5B49: 00         NOP
5B4A: 7F         LD           A,A
5B4B: 00         NOP
5B4C: 7F         LD           A,A
5B4D: 3B         DEC         SP
5B4E: 2F         CPL
5B4F: 1B         DEC         DE
5B50: 17         RLA
5B51: 0F         RRCA
5B52: 3F         CCF
5B53: 00         NOP
5B54: 7B         LD           A,E
5B55: 04         INC         B
5B56: 7C         LD           A,H
5B57: 37         SCF
5B58: FB         EI
5B59: 37         SCF
5B5A: FE 01      CP           $01
5B5C: BD         CP           L
5B5D: 1E 1F      LD           E,$1F
5B5F: 00         NOP
5B60: C0         RET         NZ
5B61: 00         NOP
5B62: F0 00      LD           A,($00)
5B64: F8 00      LDHL       SP,$00
5B66: F8 00      LDHL       SP,$00
5B68: FC                              
5B69: 00         NOP
5B6A: FC                              
5B6B: D8         RET         C
5B6C: F4                              
5B6D: 78         LD           A,B
5B6E: D8         RET         C
5B6F: 60         LD           H,B
5B70: B0         OR           B
5B71: C0         RET         NZ
5B72: F8 00      LDHL       SP,$00
5B74: BC         CP           H
5B75: 58         LD           E,B
5B76: 7C         LD           A,H
5B77: D8         RET         C
5B78: 9E         SBC         (HL)
5B79: E0 1E      LDFF00   ($1E),A
5B7B: E0 FE      LDFF00   ($FE),A
5B7D: 00         NOP
5B7E: F2                              
5B7F: 00         NOP
5B80: 73         LD           (HL),E
5B81: 00         NOP
5B82: E7         RST         0X20
5B83: 00         NOP
5B84: FF         RST         0X38
5B85: 00         NOP
5B86: FF         RST         0X38
5B87: 00         NOP
5B88: 7F         LD           A,A
5B89: 00         NOP
5B8A: 1F         RRA
5B8B: 00         NOP
5B8C: 3F         CCF
5B8D: 0B         DEC         BC
5B8E: 3F         CCF
5B8F: 1B         DEC         DE
5B90: 1F         RRA
5B91: 0F         RRCA
5B92: 0F         RRCA
5B93: 00         NOP
5B94: 0F         RRCA
5B95: 06 0F      LD           B,$0F
5B97: 06 06      LD           B,$06
5B99: 01 03 00   LD           BC,$0003
5B9C: 07         RLCA
5B9D: 03         INC         BC
5B9E: 07         RLCA
5B9F: 00         NOP
5BA0: E0 00      LDFF00   ($00),A
5BA2: F8 00      LDHL       SP,$00
5BA4: FC                              
5BA5: 00         NOP
5BA6: FC                              
5BA7: 00         NOP
5BA8: FC                              
5BA9: 00         NOP
5BAA: FC                              
5BAB: 60         LD           H,B
5BAC: F8 60      LDHL       SP,$60
5BAE: F0 C0      LD           A,($C0)
5BB0: F0 80      LD           A,($80)
5BB2: F8 00      LDHL       SP,$00
5BB4: 7C         LD           A,H
5BB5: 80         ADD         A,B
5BB6: 3C         INC         A
5BB7: C0         RET         NZ
5BB8: 3E C0      LD           A,$C0
5BBA: FE 00      CP           $00
5BBC: DE E0      SBC         $E0
5BBE: F8 00      LDHL       SP,$00
5BC0: 00         NOP
5BC1: 00         NOP
5BC2: 73         LD           (HL),E
5BC3: 00         NOP
5BC4: E7         RST         0X20
5BC5: 00         NOP
5BC6: FF         RST         0X38
5BC7: 00         NOP
5BC8: FF         RST         0X38
5BC9: 00         NOP
5BCA: 7F         LD           A,A
5BCB: 00         NOP
5BCC: 1F         RRA
5BCD: 00         NOP
5BCE: 3F         CCF
5BCF: 0B         DEC         BC
5BD0: 3F         CCF
5BD1: 1B         DEC         DE
5BD2: 1F         RRA
5BD3: 0F         RRCA
5BD4: 0F         RRCA
5BD5: 00         NOP
5BD6: 07         RLCA
5BD7: 03         INC         BC
5BD8: 07         RLCA
5BD9: 03         INC         BC
5BDA: 0F         RRCA
5BDB: 00         NOP
5BDC: 1F         RRA
5BDD: 0C         INC         C
5BDE: 1F         RRA
5BDF: 00         NOP
5BE0: 00         NOP
5BE1: 00         NOP
5BE2: E0 00      LDFF00   ($00),A
5BE4: F8 00      LDHL       SP,$00
5BE6: FC                              
5BE7: 00         NOP
5BE8: FC                              
5BE9: 00         NOP
5BEA: FC                              
5BEB: 00         NOP
5BEC: FC                              
5BED: 60         LD           H,B
5BEE: F8 60      LDHL       SP,$60
5BF0: F0 C0      LD           A,($C0)
5BF2: FE 80      CP           $80
5BF4: BF         CP           A
5BF5: 40         LD           B,B
5BF6: 9F         SBC         A
5BF7: 60         LD           H,B
5BF8: 9F         SBC         A
5BF9: 60         LD           H,B
5BFA: 3F         CCF
5BFB: C8         RET         Z
5BFC: FC                              
5BFD: 38 FC      JR           C,$5BFB
5BFF: 00         NOP
5C00: 00         NOP
5C01: 00         NOP
5C02: 00         NOP
5C03: 00         NOP
5C04: 00         NOP
5C05: 00         NOP
5C06: 00         NOP
5C07: 00         NOP
5C08: 06 00      LD           B,$00
5C0A: 0F         RRCA
5C0B: 06 0E      LD           B,$0E
5C0D: 05         DEC         B
5C0E: 16 0D      LD           D,$0D
5C10: 10 0F      STOP       $0F
5C12: 1C         INC         E
5C13: 0B         DEC         BC
5C14: 17         RLA
5C15: 0C         INC         C
5C16: 3F         CCF
5C17: 17         RLA
5C18: 2B         DEC         HL
5C19: 17         RLA
5C1A: 3A         LD           A,(HLD)
5C1B: 05         DEC         B
5C1C: 4F         LD           C,A
5C1D: 34         INC         (HL)
5C1E: 7F         LD           A,A
5C1F: 00         NOP
5C20: 06 00      LD           B,$00
5C22: 0F         RRCA
5C23: 06 0E      LD           B,$0E
5C25: 05         DEC         B
5C26: 16 0D      LD           D,$0D
5C28: 10 0F      STOP       $0F
5C2A: 1F         RRA
5C2B: 08 1F 0C   LD           ($0C1F),SP
5C2E: 17         RLA
5C2F: 0F         RRCA
5C30: 0B         DEC         BC
5C31: 07         RLCA
5C32: 09         ADD         HL,BC
5C33: 07         RLCA
5C34: 0A         LD           A,(BC)
5C35: 05         DEC         B
5C36: 0F         RRCA
5C37: 04         INC         B
5C38: 0D         DEC         C
5C39: 02         LD           (BC),A
5C3A: 09         ADD         HL,BC
5C3B: 06 12      LD           B,$12
5C3D: 0C         INC         C
5C3E: 1C         INC         E
5C3F: 00         NOP
5C40: 00         NOP
5C41: 00         NOP
5C42: 00         NOP
5C43: 00         NOP
5C44: 00         NOP
5C45: 00         NOP
5C46: 00         NOP
5C47: 00         NOP
5C48: 06 00      LD           B,$00
5C4A: 0D         DEC         C
5C4B: 06 08      LD           B,$08
5C4D: 07         RLCA
5C4E: 11 0F 11   LD           DE,$110F
5C51: 0F         RRCA
5C52: 10 0F      STOP       $0F
5C54: 1A         LD           A,(DE)
5C55: 05         DEC         B
5C56: 3A         LD           A,(HLD)
5C57: 15         DEC         D
5C58: 24         INC         H
5C59: 1B         DEC         DE
5C5A: 30 0F      JR           NC,$5C6B
5C5C: 4C         LD           C,H
5C5D: 33         INC         SP
5C5E: 7F         LD           A,A
5C5F: 00         NOP
5C60: 06 00      LD           B,$00
5C62: 0D         DEC         C
5C63: 06 08      LD           B,$08
5C65: 07         RLCA
5C66: 11 0F 11   LD           DE,$110F
5C69: 0F         RRCA
5C6A: 10 0F      STOP       $0F
5C6C: 12         LD           (DE),A
5C6D: 0D         DEC         C
5C6E: 1A         LD           A,(DE)
5C6F: 05         DEC         B
5C70: 14         INC         D
5C71: 0B         DEC         BC
5C72: 14         INC         D
5C73: 0B         DEC         BC
5C74: 0D         DEC         C
5C75: 02         LD           (BC),A
5C76: 05         DEC         B
5C77: 02         LD           (BC),A
5C78: 05         DEC         B
5C79: 02         LD           (BC),A
5C7A: 09         ADD         HL,BC
5C7B: 06 12      LD           B,$12
5C7D: 0C         INC         C
5C7E: 1C         INC         E
5C7F: 00         NOP
5C80: 00         NOP
5C81: 00         NOP
5C82: 00         NOP
5C83: 00         NOP
5C84: 00         NOP
5C85: 00         NOP
5C86: 00         NOP
5C87: 00         NOP
5C88: 07         RLCA
5C89: 00         NOP
5C8A: 0E 07      LD           C,$07
5C8C: 0E 03      LD           C,$03
5C8E: 1E 03      LD           E,$03
5C90: 21 1F 21   LD           HL,$211F
5C93: 1F         RRA
5C94: 3C         INC         A
5C95: 03         INC         BC
5C96: 1F         RRA
5C97: 0E 0A      LD           C,$0A
5C99: 05         DEC         B
5C9A: 04         INC         B
5C9B: 03         INC         BC
5C9C: 09         ADD         HL,BC
5C9D: 06 0F      LD           B,$0F
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
5CA9: 00         NOP
5CAA: 80         ADD         A,B
5CAB: 00         NOP
5CAC: 40         LD           B,B
5CAD: 80         ADD         A,B
5CAE: 30 C0      JR           NC,$5C70
5CB0: 88         ADC         A,B
5CB1: F0 84      LD           A,($84)
5CB3: F8 E4      LDHL       SP,$E4
5CB5: 18 D2      JR           $5C89
5CB7: 6C         LD           L,H
5CB8: 8A         ADC         A,D
5CB9: 74         LD           (HL),H
5CBA: E6 18      AND         $18
5CBC: 86         ADD         A,(HL)
5CBD: 78         LD           A,B
5CBE: FC                              
5CBF: 00         NOP
5CC0: 1C         INC         E
5CC1: 00         NOP
5CC2: 3A         LD           A,(HLD)
5CC3: 1C         INC         E
5CC4: 39         ADD         HL,SP
5CC5: 0E 79      LD           C,$79
5CC7: 0E 86      LD           C,$86
5CC9: 7F         LD           A,A
5CCA: C6 3F      ADD         $3F
5CCC: 20 1F      JR           NZ,$5CED
5CCE: 70         LD           (HL),B
5CCF: 0F         RRCA
5CD0: 7E         LD           A,(HL)
5CD1: 3D         DEC         A
5CD2: 32         LD           (HLD),A
5CD3: 0D         DEC         C
5CD4: 0E 01      LD           C,$01
5CD6: 04         INC         B
5CD7: 03         INC         BC
5CD8: 07         RLCA
5CD9: 00         NOP
5CDA: 00         NOP
5CDB: 00         NOP
5CDC: 00         NOP
5CDD: 00         NOP
5CDE: 00         NOP
5CDF: 00         NOP
5CE0: 00         NOP
5CE1: 00         NOP
5CE2: 00         NOP
5CE3: 00         NOP
5CE4: 00         NOP
5CE5: 00         NOP
5CE6: 00         NOP
5CE7: 00         NOP
5CE8: C0         RET         NZ
5CE9: 00         NOP
5CEA: 20 C0      JR           NZ,$5CAC
5CEC: 10 E0      STOP       $E0
5CEE: 08 F0 88   LD           ($88F0),SP
5CF1: 70         LD           (HL),B
5CF2: E8 50      ADD         SP,$50
5CF4: E8 10      ADD         SP,$10
5CF6: A6         AND         (HL)
5CF7: 18 21      JR           $5D1A
5CF9: 1E 1D      LD           E,$1D
5CFB: 02         LD           (BC),A
5CFC: 05         DEC         B
5CFD: 02         LD           (BC),A
5CFE: 06 00      LD           B,$00
5D00: 03         INC         BC
5D01: 00         NOP
5D02: 07         RLCA
5D03: 03         INC         BC
5D04: 0F         RRCA
5D05: 06 1F      LD           B,$1F
5D07: 0C         INC         C
5D08: 3F         CCF
5D09: 00         NOP
5D0A: 3F         CCF
5D0B: 18 3F      JR           $5D4C
5D0D: 1C         INC         E
5D0E: 3F         CCF
5D0F: 1E 1F      LD           E,$1F
5D11: 0C         INC         C
5D12: 7F         LD           A,A
5D13: 03         INC         BC
5D14: F7         RST         0X30
5D15: 6F         LD           L,A
5D16: F7         RST         0X30
5D17: 6F         LD           L,A
5D18: F3         DI
5D19: 6F         LD           L,A
5D1A: F9         LD           SP,HL
5D1B: 67         LD           H,A
5D1C: 64         LD           H,H
5D1D: 03         INC         BC
5D1E: 03         INC         BC
5D1F: 00         NOP
5D20: C0         RET         NZ
5D21: 00         NOP
5D22: E0 C0      LDFF00   ($C0),A
5D24: F8 00      LDHL       SP,$00
5D26: FC                              
5D27: 68         LD           L,B
5D28: FE FC      CP           $FC
5D2A: FE D4      CP           $D4
5D2C: FE D4      CP           $D4
5D2E: FE FC      CP           $FC
5D30: FE 60      CP           $60
5D32: FE 1C      CP           $1C
5D34: FF         RST         0X38
5D35: BE         CP           (HL)
5D36: FF         RST         0X38
5D37: B2         OR           D
5D38: DF         RST         0X18
5D39: BE         CP           (HL)
5D3A: AA         XOR         D
5D3B: DC 1C E0   CALL       C,$E01C
5D3E: E0 00      LDFF00   ($00),A
5D40: 03         INC         BC
5D41: 00         NOP
5D42: 07         RLCA
5D43: 03         INC         BC
5D44: 0F         RRCA
5D45: 06 1F      LD           B,$1F
5D47: 0C         INC         C
5D48: 3F         CCF
5D49: 18 3F      JR           $5D8A
5D4B: 10 2F      STOP       $2F
5D4D: 10 3F      STOP       $3F
5D4F: 00         NOP
5D50: 7F         LD           A,A
5D51: 3E 7F      LD           A,$7F
5D53: 3E FF      LD           A,$FF
5D55: 5D         LD           E,L
5D56: FF         RST         0X38
5D57: 63         LD           H,E
5D58: F3         DI
5D59: 6F         LD           L,A
5D5A: F9         LD           SP,HL
5D5B: 67         LD           H,A
5D5C: 64         LD           H,H
5D5D: 03         INC         BC
5D5E: 03         INC         BC
5D5F: 00         NOP
5D60: C0         RET         NZ
5D61: 00         NOP
5D62: E0 C0      LDFF00   ($C0),A
5D64: F8 00      LDHL       SP,$00
5D66: FC                              
5D67: 68         LD           L,B
5D68: FE FC      CP           $FC
5D6A: FE D4      CP           $D4
5D6C: FE D4      CP           $D4
5D6E: FE FC      CP           $FC
5D70: FE 60      CP           $60
5D72: FE 1C      CP           $1C
5D74: FF         RST         0X38
5D75: BE         CP           (HL)
5D76: FF         RST         0X38
5D77: B2         OR           D
5D78: FF         RST         0X38
5D79: B2         OR           D
5D7A: DD                              
5D7B: BE         CP           (HL)
5D7C: 2A         LD           A,(HLI)
5D7D: DC FC 00   CALL       C,$00FC
5D80: 03         INC         BC
5D81: 00         NOP
5D82: 0F         RRCA
5D83: 03         INC         BC
5D84: 3F         CCF
5D85: 0F         RRCA
5D86: 7F         LD           A,A
5D87: 3F         CCF
5D88: FF         RST         0X38
5D89: 70         LD           (HL),B
5D8A: FF         RST         0X38
5D8B: 6C         LD           L,H
5D8C: 7F         LD           A,A
5D8D: 12         LD           (DE),A
5D8E: 3F         CCF
5D8F: 12         LD           (DE),A
5D90: 3F         CCF
5D91: 0C         INC         C
5D92: 3F         CCF
5D93: 11 7F 3F   LD           DE,$3F7F
5D96: 7F         LD           A,A
5D97: 37         SCF
5D98: 7F         LD           A,A
5D99: 36 5B      LD           (HL),$5B
5D9B: 36 2D      LD           (HL),$2D
5D9D: 12         LD           (DE),A
5D9E: 16 00      LD           D,$00
5DA0: 00         NOP
5DA1: 00         NOP
5DA2: 03         INC         BC
5DA3: 00         NOP
5DA4: 0F         RRCA
5DA5: 03         INC         BC
5DA6: 3F         CCF
5DA7: 0F         RRCA
5DA8: 7F         LD           A,A
5DA9: 3F         CCF
5DAA: FF         RST         0X38
5DAB: 70         LD           (HL),B
5DAC: FF         RST         0X38
5DAD: 6C         LD           L,H
5DAE: 7F         LD           A,A
5DAF: 12         LD           (DE),A
5DB0: 7F         LD           A,A
5DB1: 12         LD           (DE),A
5DB2: FF         RST         0X38
5DB3: 6D         LD           L,L
5DB4: FF         RST         0X38
5DB5: 73         LD           (HL),E
5DB6: BF         CP           A
5DB7: 6E         LD           L,(HL)
5DB8: 57         LD           D,A
5DB9: 2C         INC         L
5DBA: 2A         LD           A,(HLI)
5DBB: 04         INC         B
5DBC: 06 00      LD           B,$00
5DBE: 00         NOP
5DBF: 00         NOP
5DC0: 00         NOP
5DC1: FF         RST         0X38
5DC2: 00         NOP
5DC3: FF         RST         0X38
5DC4: 24         INC         H
5DC5: FF         RST         0X38
5DC6: 18 FF      JR           $5DC7
5DC8: 18 FF      JR           $5DC9
5DCA: 24         INC         H
5DCB: FF         RST         0X38
5DCC: 00         NOP
5DCD: FF         RST         0X38
5DCE: 00         NOP
5DCF: FF         RST         0X38
5DD0: 00         NOP
5DD1: FF         RST         0X38
5DD2: 00         NOP
5DD3: FF         RST         0X38
5DD4: 24         INC         H
5DD5: FF         RST         0X38
5DD6: 18 FF      JR           $5DD7
5DD8: 18 FF      JR           $5DD9
5DDA: 24         INC         H
5DDB: FF         RST         0X38
5DDC: 00         NOP
5DDD: FF         RST         0X38
5DDE: 00         NOP
5DDF: FF         RST         0X38
5DE0: 00         NOP
5DE1: FF         RST         0X38
5DE2: 00         NOP
5DE3: FF         RST         0X38
5DE4: 24         INC         H
5DE5: FF         RST         0X38
5DE6: 18 FF      JR           $5DE7
5DE8: 18 FF      JR           $5DE9
5DEA: 24         INC         H
5DEB: FF         RST         0X38
5DEC: 00         NOP
5DED: FF         RST         0X38
5DEE: 00         NOP
5DEF: FF         RST         0X38
5DF0: 00         NOP
5DF1: FF         RST         0X38
5DF2: 00         NOP
5DF3: FF         RST         0X38
5DF4: 24         INC         H
5DF5: FF         RST         0X38
5DF6: 18 FF      JR           $5DF7
5DF8: 18 FF      JR           $5DF9
5DFA: 24         INC         H
5DFB: FF         RST         0X38
5DFC: 00         NOP
5DFD: FF         RST         0X38
5DFE: 00         NOP
5DFF: FF         RST         0X38
5E00: 03         INC         BC
5E01: 00         NOP
5E02: 03         INC         BC
5E03: 01 03 00   LD           BC,$0003
5E06: 07         RLCA
5E07: 03         INC         BC
5E08: 7F         LD           A,A
5E09: 07         RLCA
5E0A: FF         RST         0X38
5E0B: 7E         LD           A,(HL)
5E0C: FF         RST         0X38
5E0D: 5F         LD           E,A
5E0E: BF         CP           A
5E0F: 7F         LD           A,A
5E10: 4F         LD           C,A
5E11: 33         INC         SP
5E12: 36 0F      LD           (HL),$0F
5E14: 0F         RRCA
5E15: 00         NOP
5E16: 04         INC         B
5E17: 03         INC         BC
5E18: 0A         LD           A,(BC)
5E19: 05         DEC         B
5E1A: 09         ADD         HL,BC
5E1B: 06 0C      LD           B,$0C
5E1D: 03         INC         BC
5E1E: 07         RLCA
5E1F: 00         NOP
5E20: 60         LD           H,B
5E21: 00         NOP
5E22: F0 60      LD           A,($60)
5E24: F8 B0      LDHL       SP,$B0
5E26: FC                              
5E27: D0         RET         NC
5E28: FE F4      CP           $F4
5E2A: FE F8      CP           $F8
5E2C: FF         RST         0X38
5E2D: FA BF F8   LD           A,($F8BF)
5E30: 7F         LD           A,A
5E31: BA         CP           D
5E32: BE         CP           (HL)
5E33: 78         LD           A,B
5E34: 34         INC         (HL)
5E35: F8 74      LDHL       SP,$74
5E37: F8 EA      LDHL       SP,$EA
5E39: F4                              
5E3A: F2                              
5E3B: 0C         INC         C
5E3C: C6 F8      ADD         $F8
5E3E: FC                              
5E3F: 00         NOP
5E40: 07         RLCA
5E41: 00         NOP
5E42: 0F         RRCA
5E43: 03         INC         BC
5E44: 1F         RRA
5E45: 0D         DEC         C
5E46: 1F         RRA
5E47: 0F         RRCA
5E48: 17         RLA
5E49: 0F         RRCA
5E4A: 0B         DEC         BC
5E4B: 07         RLCA
5E4C: 05         DEC         B
5E4D: 02         LD           (BC),A
5E4E: 0F         RRCA
5E4F: 00         NOP
5E50: 17         RLA
5E51: 0F         RRCA
5E52: 20 1F      JR           NZ,$5E73
5E54: 2E 11      LD           L,$11
5E56: 2F         CPL
5E57: 10 2F      STOP       $2F
5E59: 10 17      STOP       $17
5E5B: 08 08 07   LD           ($0708),SP
5E5E: 07         RLCA
5E5F: 00         NOP
5E60: 00         NOP
5E61: 00         NOP
5E62: 80         ADD         A,B
5E63: 00         NOP
5E64: F0 80      LD           A,($80)
5E66: FF         RST         0X38
5E67: D0         RET         NC
5E68: FF         RST         0X38
5E69: FA FF FE   LD           A,($FEFF)
5E6C: BE         CP           (HL)
5E6D: 7C         LD           A,H
5E6E: 7B         LD           A,E
5E6F: FC                              
5E70: FF         RST         0X38
5E71: 7A         LD           A,D
5E72: F7         RST         0X30
5E73: B8         CP           B
5E74: 67         LD           H,A
5E75: DA 6E D0   JP           C,$D06E
5E78: 3E C4      LD           A,$C4
5E7A: 2C         INC         L
5E7B: C0         RET         NZ
5E7C: 40         LD           B,B
5E7D: 80         ADD         A,B
5E7E: 80         ADD         A,B
5E7F: 00         NOP
5E80: 00         NOP
5E81: FF         RST         0X38
5E82: 00         NOP
5E83: FF         RST         0X38
5E84: 24         INC         H
5E85: FF         RST         0X38
5E86: 18 FF      JR           $5E87
5E88: 18 FF      JR           $5E89
5E8A: 24         INC         H
5E8B: FF         RST         0X38
5E8C: 00         NOP
5E8D: FF         RST         0X38
5E8E: 00         NOP
5E8F: FF         RST         0X38
5E90: 00         NOP
5E91: FF         RST         0X38
5E92: 00         NOP
5E93: FF         RST         0X38
5E94: 24         INC         H
5E95: FF         RST         0X38
5E96: 18 FF      JR           $5E97
5E98: 18 FF      JR           $5E99
5E9A: 24         INC         H
5E9B: FF         RST         0X38
5E9C: 00         NOP
5E9D: FF         RST         0X38
5E9E: 00         NOP
5E9F: FF         RST         0X38
5EA0: 00         NOP
5EA1: FF         RST         0X38
5EA2: 00         NOP
5EA3: FF         RST         0X38
5EA4: 24         INC         H
5EA5: FF         RST         0X38
5EA6: 18 FF      JR           $5EA7
5EA8: 18 FF      JR           $5EA9
5EAA: 24         INC         H
5EAB: FF         RST         0X38
5EAC: 00         NOP
5EAD: FF         RST         0X38
5EAE: 00         NOP
5EAF: FF         RST         0X38
5EB0: 00         NOP
5EB1: FF         RST         0X38
5EB2: 00         NOP
5EB3: FF         RST         0X38
5EB4: 24         INC         H
5EB5: FF         RST         0X38
5EB6: 18 FF      JR           $5EB7
5EB8: 18 FF      JR           $5EB9
5EBA: 24         INC         H
5EBB: FF         RST         0X38
5EBC: 00         NOP
5EBD: FF         RST         0X38
5EBE: 00         NOP
5EBF: FF         RST         0X38
5EC0: 00         NOP
5EC1: FF         RST         0X38
5EC2: 00         NOP
5EC3: FF         RST         0X38
5EC4: 24         INC         H
5EC5: FF         RST         0X38
5EC6: 18 FF      JR           $5EC7
5EC8: 18 FF      JR           $5EC9
5ECA: 24         INC         H
5ECB: FF         RST         0X38
5ECC: 00         NOP
5ECD: FF         RST         0X38
5ECE: 00         NOP
5ECF: FF         RST         0X38
5ED0: 00         NOP
5ED1: FF         RST         0X38
5ED2: 00         NOP
5ED3: FF         RST         0X38
5ED4: 24         INC         H
5ED5: FF         RST         0X38
5ED6: 18 FF      JR           $5ED7
5ED8: 18 FF      JR           $5ED9
5EDA: 24         INC         H
5EDB: FF         RST         0X38
5EDC: 00         NOP
5EDD: FF         RST         0X38
5EDE: 00         NOP
5EDF: FF         RST         0X38
5EE0: 00         NOP
5EE1: FF         RST         0X38
5EE2: 00         NOP
5EE3: FF         RST         0X38
5EE4: 24         INC         H
5EE5: FF         RST         0X38
5EE6: 18 FF      JR           $5EE7
5EE8: 18 FF      JR           $5EE9
5EEA: 24         INC         H
5EEB: FF         RST         0X38
5EEC: 00         NOP
5EED: FF         RST         0X38
5EEE: 00         NOP
5EEF: FF         RST         0X38
5EF0: 00         NOP
5EF1: FF         RST         0X38
5EF2: 00         NOP
5EF3: FF         RST         0X38
5EF4: 24         INC         H
5EF5: FF         RST         0X38
5EF6: 18 FF      JR           $5EF7
5EF8: 18 FF      JR           $5EF9
5EFA: 24         INC         H
5EFB: FF         RST         0X38
5EFC: 00         NOP
5EFD: FF         RST         0X38
5EFE: 00         NOP
5EFF: FF         RST         0X38
5F00: 1C         INC         E
5F01: 00         NOP
5F02: 3E 1C      LD           A,$1C
5F04: 7F         LD           A,A
5F05: 3E 73      LD           A,$73
5F07: 3E 33      LD           A,$33
5F09: 1D         DEC         E
5F0A: 1D         DEC         E
5F0B: 03         INC         BC
5F0C: 3C         INC         A
5F0D: 1B         DEC         DE
5F0E: 73         LD           (HL),E
5F0F: 3C         INC         A
5F10: 73         LD           (HL),E
5F11: 3E 7F      LD           A,$7F
5F13: 3E 3F      LD           A,$3F
5F15: 1C         INC         E
5F16: 1F         RRA
5F17: 00         NOP
5F18: 13         INC         DE
5F19: 0C         INC         C
5F1A: 19         ADD         HL,DE
5F1B: 07         RLCA
5F1C: 0C         INC         C
5F1D: 03         INC         BC
5F1E: 07         RLCA
5F1F: 00         NOP
5F20: 03         INC         BC
5F21: 00         NOP
5F22: 07         RLCA
5F23: 03         INC         BC
5F24: 06 03      LD           B,$03
5F26: 75         LD           (HL),L
5F27: 02         LD           (BC),A
5F28: FF         RST         0X38
5F29: 71         LD           (HL),C
5F2A: E5         PUSH       HL
5F2B: 7B         LD           A,E
5F2C: E4                              
5F2D: 7B         LD           A,E
5F2E: FF         RST         0X38
5F2F: 70         LD           (HL),B
5F30: 7E         LD           A,(HL)
5F31: 03         INC         BC
5F32: 0E 07      LD           C,$07
5F34: 0F         RRCA
5F35: 07         RLCA
5F36: 17         RLA
5F37: 0B         DEC         BC
5F38: 13         INC         DE
5F39: 0C         INC         C
5F3A: 19         ADD         HL,DE
5F3B: 07         RLCA
5F3C: 0C         INC         C
5F3D: 03         INC         BC
5F3E: 07         RLCA
5F3F: 00         NOP
5F40: 1F         RRA
5F41: 00         NOP
5F42: 3E 1F      LD           A,$1F
5F44: 7E         LD           A,(HL)
5F45: 2B         DEC         HL
5F46: 7E         LD           A,(HL)
5F47: 2B         DEC         HL
5F48: B6         OR           (HL)
5F49: 7F         LD           A,A
5F4A: 80         ADD         A,B
5F4B: 7F         LD           A,A
5F4C: 81         ADD         A,C
5F4D: 7E         LD           A,(HL)
5F4E: FE 01      CP           $01
5F50: 7E         LD           A,(HL)
5F51: 3F         CCF
5F52: 3C         INC         A
5F53: 03         INC         BC
5F54: 1C         INC         E
5F55: 0F         RRCA
5F56: 39         ADD         HL,SP
5F57: 1E 38      LD           E,$38
5F59: 1F         RRA
5F5A: 2D         DEC         L
5F5B: 1F         RRA
5F5C: 17         RLA
5F5D: 0F         RRCA
5F5E: 3F         CCF
5F5F: 00         NOP
5F60: 80         ADD         A,B
5F61: 00         NOP
5F62: 40         LD           B,B
5F63: 80         ADD         A,B
5F64: 20 C0      JR           NZ,$5F26
5F66: 10 E0      STOP       $E0
5F68: D0         RET         NC
5F69: 20 90      JR           NZ,$5EFB
5F6B: 60         LD           H,B
5F6C: 10 E0      STOP       $E0
5F6E: 20 C0      JR           NZ,$5F30
5F70: 23         INC         HL
5F71: C0         RET         NZ
5F72: 45         LD           B,L
5F73: 82         ADD         A,D
5F74: F5         PUSH       AF
5F75: 02         LD           (BC),A
5F76: 09         ADD         HL,BC
5F77: F6 01      OR           $01
5F79: FE F1      CP           $F1
5F7B: FE 6A      CP           $6A
5F7D: 9C         SBC         H
5F7E: FC                              
5F7F: 00         NOP
5F80: 80         ADD         A,B
5F81: 00         NOP
5F82: 40         LD           B,B
5F83: 80         ADD         A,B
5F84: 20 C0      JR           NZ,$5F46
5F86: 10 E0      STOP       $E0
5F88: D0         RET         NC
5F89: 20 90      JR           NZ,$5F1B
5F8B: 60         LD           H,B
5F8C: 10 E0      STOP       $E0
5F8E: 20 C0      JR           NZ,$5F50
5F90: 20 C0      JR           NZ,$5F52
5F92: 46         LD           B,(HL)
5F93: 80         ADD         A,B
5F94: EA 04 12   LD           ($1204),A
5F97: EC                              
5F98: 04         INC         B
5F99: F8 CC      LDHL       SP,$CC
5F9B: F8 F8      LDHL       SP,$F8
5F9D: 70         LD           (HL),B
5F9E: FC                              
5F9F: 00         NOP
5FA0: 03         INC         BC
5FA1: 00         NOP
5FA2: 1C         INC         E
5FA3: 03         INC         BC
5FA4: 3E 01      LD           A,$01
5FA6: 0F         RRCA
5FA7: 04         INC         B
5FA8: 1F         RRA
5FA9: 0F         RRCA
5FAA: 2F         CPL
5FAB: 1B         DEC         DE
5FAC: 4F         LD           C,A
5FAD: 3B         DEC         SP
5FAE: 40         LD           B,B
5FAF: 3F         CCF
5FB0: 50         LD           D,B
5FB1: 2F         CPL
5FB2: 4F         LD           C,A
5FB3: 30 20      JR           NC,$5FD5
5FB5: 1F         RRA
5FB6: 1F         RRA
5FB7: 00         NOP
5FB8: 0B         DEC         BC
5FB9: 07         RLCA
5FBA: 3D         DEC         A
5FBB: 03         INC         BC
5FBC: 77         LD           (HL),A
5FBD: 38 7E      JR           C,$603D
5FBF: 00         NOP
5FC0: C0         RET         NZ
5FC1: 00         NOP
5FC2: 7C         LD           A,H
5FC3: 80         ADD         A,B
5FC4: FE 00      CP           $00
5FC6: F0 60      LD           A,($60)
5FC8: E8 F0      ADD         SP,$F0
5FCA: E4                              
5FCB: B8         CP           B
5FCC: E2         LDFF00   (C),A
5FCD: BC         CP           H
5FCE: 02         LD           (BC),A
5FCF: FC                              
5FD0: 12         LD           (DE),A
5FD1: EC                              
5FD2: E2         LDFF00   (C),A
5FD3: 1C         INC         E
5FD4: 04         INC         B
5FD5: F8 F8      LDHL       SP,$F8
5FD7: 00         NOP
5FD8: D8         RET         C
5FD9: E0 AC      LDFF00   ($AC),A
5FDB: D8         RET         C
5FDC: FC                              
5FDD: 00         NOP
5FDE: 00         NOP
5FDF: 00         NOP
5FE0: 00         NOP
5FE1: 00         NOP
5FE2: 00         NOP
5FE3: 00         NOP
5FE4: 00         NOP
5FE5: 00         NOP
5FE6: 00         NOP
5FE7: 00         NOP
5FE8: 00         NOP
5FE9: 00         NOP
5FEA: 00         NOP
5FEB: 00         NOP
5FEC: 00         NOP
5FED: 00         NOP
5FEE: 00         NOP
5FEF: 00         NOP
5FF0: F3         DI
5FF1: 00         NOP
5FF2: 3C         INC         A
5FF3: 03         INC         BC
5FF4: 4E         LD           C,(HL)
5FF5: 31 87 78   LD           SP,$7887
5FF8: BF         CP           A
5FF9: 76         HALT
5FFA: 7F         LD           A,A
5FFB: 00         NOP
5FFC: F2                              
5FFD: 7D         LD           A,L
5FFE: 7F         LD           A,A
5FFF: 00         NOP
6000: 00         NOP
6001: 00         NOP
6002: 1B         DEC         DE
6003: 00         NOP
6004: 3D         DEC         A
6005: 1B         DEC         DE
6006: 69         LD           L,C
6007: 37         SCF
6008: FB         EI
6009: A4         AND         H
600A: FD                              
600B: 93         SUB         E
600C: FF         RST         0X38
600D: F2                              
600E: 1F         RRA
600F: 02         LD           (BC),A
6010: 3D         DEC         A
6011: 1B         DEC         DE
6012: 77         LD           (HL),A
6013: 3C         INC         A
6014: 69         LD           L,C
6015: 36 76      LD           (HL),$76
6017: 20 70      JR           NZ,$6089
6019: 20 F8      JR           NZ,$6013
601B: A8         XOR         B
601C: F8 98      LDHL       SP,$98
601E: 70         LD           (HL),B
601F: 70         LD           (HL),B
6020: 00         NOP
6021: 00         NOP
6022: 00         NOP
6023: 00         NOP
6024: 1B         DEC         DE
6025: 00         NOP
6026: 3D         DEC         A
6027: 1B         DEC         DE
6028: 69         LD           L,C
6029: 37         SCF
602A: DB                              
602B: 64         LD           H,H
602C: FD                              
602D: 13         INC         DE
602E: EF         RST         0X28
602F: E2         LDFF00   (C),A
6030: 1F         RRA
6031: 02         LD           (BC),A
6032: 3D         DEC         A
6033: 1B         DEC         DE
6034: 67         LD           H,A
6035: 3C         INC         A
6036: D9         RETI
6037: 66         LD           H,(HL)
6038: F6 40      OR           $40
603A: E0 40      LDFF00   ($40),A
603C: E0 20      LDFF00   ($20),A
603E: E0 E0      LDFF00   ($E0),A
6040: 00         NOP
6041: 00         NOP
6042: 00         NOP
6043: 00         NOP
6044: E3                              
6045: 00         NOP
6046: F6 61      OR           $61
6048: FF         RST         0X38
6049: 70         LD           (HL),B
604A: BF         CP           A
604B: 72         LD           (HL),D
604C: 5F         LD           E,A
604D: 32         LD           (HLD),A
604E: 3F         CCF
604F: 10 3F      STOP       $3F
6051: 18 3F      JR           $6092
6053: 1C         INC         E
6054: 3F         CCF
6055: 1F         RRA
6056: 3B         DEC         SP
6057: 1C         INC         E
6058: 74         LD           (HL),H
6059: 38 4F      JR           C,$60AA
605B: 30 3F      JR           NC,$609C
605D: 00         NOP
605E: 00         NOP
605F: 00         NOP
6060: 00         NOP
6061: 00         NOP
6062: 30 00      JR           NC,$6064
6064: 7B         LD           A,E
6065: 30 7E      JR           NC,$60E5
6067: 39         ADD         HL,SP
6068: 5F         LD           E,A
6069: 34         INC         (HL)
606A: 3F         CCF
606B: 15         DEC         D
606C: 3F         CCF
606D: 11 2F 10   LD           DE,$102F
6070: 1F         RRA
6071: 08 1F 0C   LD           ($0C1F),SP
6074: 1F         RRA
6075: 0F         RRCA
6076: 3B         DEC         SP
6077: 1C         INC         E
6078: 24         INC         H
6079: 18 1F      JR           $609A
607B: 00         NOP
607C: 03         INC         BC
607D: 04         INC         B
607E: 00         NOP
607F: 00         NOP
6080: 00         NOP
6081: 00         NOP
6082: 00         NOP
6083: 00         NOP
6084: C0         RET         NZ
6085: 00         NOP
6086: 6E         LD           L,(HL)
6087: 80         ADD         A,B
6088: FE 0C      CP           $0C
608A: FE 1C      CP           $1C
608C: FA 3C F4   LD           A,($F43C)
608F: 38 E8      JR           C,$6079
6091: 30 E8      JR           NC,$607B
6093: 70         LD           (HL),B
6094: E8 F0      ADD         SP,$F0
6096: 78         LD           A,B
6097: F0 BC      LD           A,($BC)
6099: 78         LD           A,B
609A: DC 38 F8   CALL       C,$F838
609D: 00         NOP
609E: 00         NOP
609F: 00         NOP
60A0: 01 00 03   LD           BC,$0300
60A3: 01 03 00   LD           BC,$0003
60A6: 06 01      LD           B,$01
60A8: 0F         RRCA
60A9: 00         NOP
60AA: 0F         RRCA
60AB: 01 0D 03   LD           BC,$030D
60AE: 0D         DEC         C
60AF: 03         INC         BC
60B0: 04         INC         B
60B1: 03         INC         BC
60B2: 04         INC         B
60B3: 03         INC         BC
60B4: 05         DEC         B
60B5: 03         INC         BC
60B6: 05         DEC         B
60B7: 03         INC         BC
60B8: 05         DEC         B
60B9: 03         INC         BC
60BA: 07         RLCA
60BB: 01 06 01   LD           BC,$0106
60BE: 03         INC         BC
60BF: 00         NOP
60C0: 00         NOP
60C1: 00         NOP
60C2: 00         NOP
60C3: 00         NOP
60C4: 00         NOP
60C5: 00         NOP
60C6: 03         INC         BC
60C7: 00         NOP
60C8: 06 01      LD           B,$01
60CA: 0F         RRCA
60CB: 00         NOP
60CC: 0F         RRCA
60CD: 00         NOP
60CE: 0F         RRCA
60CF: 04         INC         B
60D0: 0F         RRCA
60D1: 00         NOP
60D2: 1F         RRA
60D3: 03         INC         BC
60D4: 35         DEC         (HL)
60D5: 1B         DEC         DE
60D6: 26 19      LD           H,$19
60D8: 1D         DEC         E
60D9: 02         LD           (BC),A
60DA: 04         INC         B
60DB: 03         INC         BC
60DC: 03         INC         BC
60DD: 00         NOP
60DE: 00         NOP
60DF: 00         NOP
60E0: 00         NOP
60E1: 00         NOP
60E2: 00         NOP
60E3: 00         NOP
60E4: 00         NOP
60E5: 00         NOP
60E6: C0         RET         NZ
60E7: 00         NOP
60E8: 60         LD           H,B
60E9: 80         ADD         A,B
60EA: F0 00      LD           A,($00)
60EC: F0 00      LD           A,($00)
60EE: F0 C0      LD           A,($C0)
60F0: F0 00      LD           A,($00)
60F2: 78         LD           A,B
60F3: 90         SUB         B
60F4: FF         RST         0X38
60F5: F0 FF      LD           A,($FF)
60F7: F6 ED      OR           $ED
60F9: 7E         LD           A,(HL)
60FA: BA         CP           D
60FB: 7C         LD           A,H
60FC: C4 38 F8   CALL       NZ,$F838
60FF: 00         NOP
6100: 00         NOP
6101: FF         RST         0X38
6102: 00         NOP
6103: FF         RST         0X38
6104: 24         INC         H
6105: FF         RST         0X38
6106: 18 FF      JR           $6107
6108: 18 FF      JR           $6109
610A: 24         INC         H
610B: FF         RST         0X38
610C: 00         NOP
610D: FF         RST         0X38
610E: 00         NOP
610F: FF         RST         0X38
6110: 00         NOP
6111: FF         RST         0X38
6112: 00         NOP
6113: FF         RST         0X38
6114: 24         INC         H
6115: FF         RST         0X38
6116: 18 FF      JR           $6117
6118: 18 FF      JR           $6119
611A: 24         INC         H
611B: FF         RST         0X38
611C: 00         NOP
611D: FF         RST         0X38
611E: 00         NOP
611F: FF         RST         0X38
6120: 00         NOP
6121: 00         NOP
6122: 01 00 03   LD           BC,$0300
6125: 01 E3 01   LD           BC,$01E3
6128: F7         RST         0X30
6129: 60         LD           H,B
612A: FF         RST         0X38
612B: 74         LD           (HL),H
612C: 7D         LD           A,L
612D: 2B         DEC         HL
612E: 78         LD           A,B
612F: 27         DAA
6130: F3         DI
6131: 6C         LD           L,H
6132: F7         RST         0X30
6133: 69         LD           L,C
6134: 77         LD           (HL),A
6135: 28 F7      JR           Z,$612E
6137: 68         LD           L,B
6138: F3         DI
6139: 8C         ADC         A,H
613A: F8 E7      LDHL       SP,$E7
613C: 77         LD           (HL),A
613D: 78         LD           A,B
613E: 0F         RRCA
613F: 0F         RRCA
6140: 00         NOP
6141: 00         NOP
6142: 07         RLCA
6143: 07         RLCA
6144: 1F         RRA
6145: 1C         INC         E
6146: 3F         CCF
6147: 31 7F 67   LD           SP,$677F
614A: 7F         LD           A,A
614B: 6E         LD           L,(HL)
614C: FF         RST         0X38
614D: CC FF CD   CALL       Z,$CDFF
6150: FF         RST         0X38
6151: 67         LD           H,A
6152: FF         RST         0X38
6153: 73         LD           (HL),E
6154: FF         RST         0X38
6155: B8         CP           B
6156: FF         RST         0X38
6157: 9F         SBC         A
6158: 7F         LD           A,A
6159: 47         LD           B,A
615A: 3F         CCF
615B: 30 0F      JR           NC,$616C
615D: 0F         RRCA
615E: 00         NOP
615F: 00         NOP
6160: 01 00 03   LD           BC,$0300
6163: 01 E3 01   LD           BC,$01E3
6166: F7         RST         0X30
6167: 60         LD           H,B
6168: FF         RST         0X38
6169: 70         LD           (HL),B
616A: 7F         LD           A,A
616B: 2C         INC         L
616C: 7F         LD           A,A
616D: 2E FF      LD           L,$FF
616F: 6B         LD           L,E
6170: FF         RST         0X38
6171: 68         LD           L,B
6172: 79         LD           A,C
6173: 27         DAA
6174: F3         DI
6175: 6C         LD           L,H
6176: F4                              
6177: 4B         LD           C,E
6178: F1         POP         AF
6179: 8E         ADC         A,(HL)
617A: FF         RST         0X38
617B: F1         POP         AF
617C: 3F         CCF
617D: 3F         CCF
617E: 07         RLCA
617F: 07         RLCA
6180: 00         NOP
6181: FF         RST         0X38
6182: 00         NOP
6183: FF         RST         0X38
6184: 24         INC         H
6185: FF         RST         0X38
6186: 18 FF      JR           $6187
6188: 18 FF      JR           $6189
618A: 24         INC         H
618B: FF         RST         0X38
618C: 00         NOP
618D: FF         RST         0X38
618E: 00         NOP
618F: FF         RST         0X38
6190: 00         NOP
6191: FF         RST         0X38
6192: 00         NOP
6193: FF         RST         0X38
6194: 24         INC         H
6195: FF         RST         0X38
6196: 18 FF      JR           $6197
6198: 18 FF      JR           $6199
619A: 24         INC         H
619B: FF         RST         0X38
619C: 00         NOP
619D: FF         RST         0X38
619E: 00         NOP
619F: FF         RST         0X38
61A0: 00         NOP
61A1: FF         RST         0X38
61A2: 00         NOP
61A3: FF         RST         0X38
61A4: 24         INC         H
61A5: FF         RST         0X38
61A6: 18 FF      JR           $61A7
61A8: 18 FF      JR           $61A9
61AA: 24         INC         H
61AB: FF         RST         0X38
61AC: 00         NOP
61AD: FF         RST         0X38
61AE: 00         NOP
61AF: FF         RST         0X38
61B0: 00         NOP
61B1: FF         RST         0X38
61B2: 00         NOP
61B3: FF         RST         0X38
61B4: 24         INC         H
61B5: FF         RST         0X38
61B6: 18 FF      JR           $61B7
61B8: 18 FF      JR           $61B9
61BA: 24         INC         H
61BB: FF         RST         0X38
61BC: 00         NOP
61BD: FF         RST         0X38
61BE: 00         NOP
61BF: FF         RST         0X38
61C0: 00         NOP
61C1: FF         RST         0X38
61C2: 00         NOP
61C3: FF         RST         0X38
61C4: 24         INC         H
61C5: FF         RST         0X38
61C6: 18 FF      JR           $61C7
61C8: 18 FF      JR           $61C9
61CA: 24         INC         H
61CB: FF         RST         0X38
61CC: 00         NOP
61CD: FF         RST         0X38
61CE: 00         NOP
61CF: FF         RST         0X38
61D0: 00         NOP
61D1: FF         RST         0X38
61D2: 00         NOP
61D3: FF         RST         0X38
61D4: 24         INC         H
61D5: FF         RST         0X38
61D6: 18 FF      JR           $61D7
61D8: 18 FF      JR           $61D9
61DA: 24         INC         H
61DB: FF         RST         0X38
61DC: 00         NOP
61DD: FF         RST         0X38
61DE: 00         NOP
61DF: FF         RST         0X38
61E0: 00         NOP
61E1: FF         RST         0X38
61E2: 00         NOP
61E3: FF         RST         0X38
61E4: 24         INC         H
61E5: FF         RST         0X38
61E6: 18 FF      JR           $61E7
61E8: 18 FF      JR           $61E9
61EA: 24         INC         H
61EB: FF         RST         0X38
61EC: 00         NOP
61ED: FF         RST         0X38
61EE: 00         NOP
61EF: FF         RST         0X38
61F0: 00         NOP
61F1: FF         RST         0X38
61F2: 00         NOP
61F3: FF         RST         0X38
61F4: 24         INC         H
61F5: FF         RST         0X38
61F6: 18 FF      JR           $61F7
61F8: 18 FF      JR           $61F9
61FA: 24         INC         H
61FB: FF         RST         0X38
61FC: 00         NOP
61FD: FF         RST         0X38
61FE: 00         NOP
61FF: FF         RST         0X38
6200: 00         NOP
6201: 00         NOP
6202: 00         NOP
6203: 00         NOP
6204: 00         NOP
6205: 00         NOP
6206: 07         RLCA
6207: 00         NOP
6208: 0F         RRCA
6209: 07         RLCA
620A: 17         RLA
620B: 08 17 08   LD           ($0817),SP
620E: 17         RLA
620F: 08 0C 03   LD           ($030C),SP
6212: 0B         DEC         BC
6213: 07         RLCA
6214: 09         ADD         HL,BC
6215: 07         RLCA
6216: 07         RLCA
6217: 03         INC         BC
6218: 07         RLCA
6219: 03         INC         BC
621A: 05         DEC         B
621B: 03         INC         BC
621C: 02         LD           (BC),A
621D: 01 01 00   LD           BC,$0001
6220: 07         RLCA
6221: 00         NOP
6222: 0F         RRCA
6223: 07         RLCA
6224: 1F         RRA
6225: 0F         RRCA
6226: DF         RST         0X18
6227: 0F         RRCA
6228: FB         EI
6229: 8E         ADC         A,(HL)
622A: F7         RST         0X30
622B: CA FF 63   JP           Z,$63FF
622E: FF         RST         0X38
622F: 21 7F B0   LD           HL,$B07F
6232: 5F         LD           E,A
6233: BC         CP           H
6234: EF         RST         0X28
6235: 1C         INC         E
6236: BE         CP           (HL)
6237: 43         LD           B,E
6238: 9F         SBC         A
6239: 7C         LD           A,H
623A: 7F         LD           A,A
623B: 81         ADD         A,C
623C: 5E         LD           E,(HL)
623D: BF         CP           A
623E: FF         RST         0X38
623F: 00         NOP
6240: F8 00      LDHL       SP,$00
6242: FD                              
6243: F8 FF      LDHL       SP,$FF
6245: FC                              
6246: FF         RST         0X38
6247: FE B7      CP           $B7
6249: 7A         LD           A,D
624A: FF         RST         0X38
624B: 32         LD           (HLD),A
624C: FF         RST         0X38
624D: 36 FF      LD           (HL),$FF
624F: FE FF      CP           $FF
6251: CC FF F8   CALL       Z,$F8FF
6254: FF         RST         0X38
6255: 4A         LD           C,D
6256: FD                              
6257: 06 BB      LD           B,$BB
6259: EC                              
625A: 5F         LD           E,A
625B: B0         OR           B
625C: E2         LDFF00   (C),A
625D: 1C         INC         E
625E: FC                              
625F: 00         NOP
6260: F0 00      LD           A,($00)
6262: E8 70      ADD         SP,$70
6264: F4                              
6265: 18 3C      JR           $62A3
6267: C8         RET         Z
6268: FC                              
6269: 08 FC 08   LD           ($08FC),SP
626C: F4                              
626D: 18 68      JR           $62D7
626F: B0         OR           B
6270: 50         LD           D,B
6271: E0 F0      LDFF00   ($F0),A
6273: 00         NOP
6274: 60         LD           H,B
6275: C0         RET         NZ
6276: 60         LD           H,B
6277: C0         RET         NZ
6278: 60         LD           H,B
6279: C0         RET         NZ
627A: A0         AND         B
627B: 40         LD           B,B
627C: C0         RET         NZ
627D: 00         NOP
627E: 00         NOP
627F: 00         NOP
6280: 07         RLCA
6281: 00         NOP
6282: 0E 07      LD           C,$07
6284: 0F         RRCA
6285: 07         RLCA
6286: 0F         RRCA
6287: 07         RLCA
6288: 08 07 04   LD           ($0407),SP
628B: 03         INC         BC
628C: 03         INC         BC
628D: 00         NOP
628E: 03         INC         BC
628F: 00         NOP
6290: 07         RLCA
6291: 00         NOP
6292: 0F         RRCA
6293: 07         RLCA
6294: 1E 09      LD           E,$09
6296: 17         RLA
6297: 08 1F 05   LD           ($051F),SP
629A: 3E 0B      LD           A,$0B
629C: 7E         LD           A,(HL)
629D: 37         SCF
629E: 7F         LD           A,A
629F: 00         NOP
62A0: 3C         INC         A
62A1: 03         INC         BC
62A2: DC 3B 57   CALL       C,$573B
62A5: BC         CP           H
62A6: 5B         LD           E,E
62A7: B7         OR           A
62A8: 4D         LD           C,L
62A9: BB         CP           E
62AA: F7         RST         0X30
62AB: 0D         DEC         C
62AC: CB 07      RLC         1,E
62AE: C7         RST         0X00
62AF: 00         NOP
62B0: E0 00      LDFF00   ($00),A
62B2: F0 00      LD           A,($00)
62B4: F0 80      LD           A,($80)
62B6: 78         LD           A,B
62B7: C0         RET         NZ
62B8: F8 40      LDHL       SP,$40
62BA: B4         OR           H
62BB: 48         LD           C,B
62BC: 4C         LD           C,H
62BD: B0         OR           B
62BE: F8 00      LDHL       SP,$00
62C0: F0 00      LD           A,($00)
62C2: FF         RST         0X38
62C3: 70         LD           (HL),B
62C4: BF         CP           A
62C5: D6 7D      SUB         $7D
62C7: B6         OR           (HL)
62C8: F7         RST         0X30
62C9: 68         LD           L,B
62CA: F9         LD           SP,HL
62CB: 40         LD           B,B
62CC: C3 80 8F   JP           $8F80
62CF: 00         NOP
62D0: 1F         RRA
62D1: 01 1E 03   LD           BC,$031E
62D4: 37         SCF
62D5: 0A         LD           A,(BC)
62D6: 39         ADD         HL,SP
62D7: 06 1E      LD           B,$1E
62D9: 01 07 00   LD           BC,$0007
62DC: 00         NOP
62DD: 00         NOP
62DE: 00         NOP
62DF: 00         NOP
62E0: 70         LD           (HL),B
62E1: 00         NOP
62E2: B8         CP           B
62E3: 70         LD           (HL),B
62E4: 78         LD           A,B
62E5: F0 78      LD           A,($78)
62E7: F0 08      LD           A,($08)
62E9: F0 90      LD           A,($90)
62EB: 60         LD           H,B
62EC: E0 00      LDFF00   ($00),A
62EE: E0 00      LDFF00   ($00),A
62F0: D0         RET         NC
62F1: E0 E8      LDFF00   ($E8),A
62F3: 10 F8      STOP       $F8
62F5: A0         AND         B
62F6: FC                              
62F7: D0         RET         NC
62F8: 7E         LD           A,(HL)
62F9: EC                              
62FA: FE 00      CP           $00
62FC: 00         NOP
62FD: 00         NOP
62FE: 00         NOP
62FF: 00         NOP
6300: 0F         RRCA
6301: 00         NOP
6302: 37         SCF
6303: 0F         RRCA
6304: 5F         LD           E,A
6305: 3F         CCF
6306: 7F         LD           A,A
6307: 30 BF      JR           NC,$62C8
6309: 67         LD           H,A
630A: BF         CP           A
630B: 69         LD           L,C
630C: BF         CP           A
630D: 69         LD           L,C
630E: B7         OR           A
630F: 6D         LD           L,L
6310: BB         CP           E
6311: 66         LD           H,(HL)
6312: BE         CP           (HL)
6313: 63         LD           H,E
6314: BF         CP           A
6315: 63         LD           H,E
6316: 7F         LD           A,A
6317: 32         LD           (HLD),A
6318: 5F         LD           E,A
6319: 38 2F      JR           C,$634A
631B: 1F         RRA
631C: 10 0F      STOP       $0F
631E: 0F         RRCA
631F: 00         NOP
6320: 01 00 01   LD           BC,$0100
6323: 00         NOP
6324: 02         LD           (BC),A
6325: 01 03 01   LD           BC,$0103
6328: 05         DEC         B
6329: 03         INC         BC
632A: 07         RLCA
632B: 03         INC         BC
632C: 1B         DEC         DE
632D: 07         RLCA
632E: 2E 17      LD           L,$17
6330: 2D         DEC         L
6331: 16 6F      LD           D,$6F
6333: 18 B1      JR           $62E6
6335: 6E         LD           L,(HL)
6336: DE 30      SBC         $30
6338: FA 5C BA   LD           A,($BA5C)
633B: 7C         LD           A,H
633C: 44         LD           B,H
633D: 38 38      JR           C,$6377
633F: 00         NOP
6340: 0E 00      LD           C,$00
6342: 1E 0C      LD           E,$0C
6344: 2E 1C      LD           L,$1C
6346: 3A         LD           A,(HLD)
6347: 1C         INC         E
6348: 5C         LD           E,H
6349: 38 74      JR           C,$63BF
634B: 38 B8      JR           C,$6305
634D: 70         LD           (HL),B
634E: E8 70      ADD         SP,$70
6350: 70         LD           (HL),B
6351: E0 D0      LDFF00   ($D0),A
6353: E0 E0      LDFF00   ($E0),A
6355: C0         RET         NZ
6356: A0         AND         B
6357: C0         RET         NZ
6358: C0         RET         NZ
6359: 80         ADD         A,B
635A: 40         LD           B,B
635B: 80         ADD         A,B
635C: 80         ADD         A,B
635D: 00         NOP
635E: 80         ADD         A,B
635F: 00         NOP
6360: 0E 00      LD           C,$00
6362: 35         DEC         (HL)
6363: 0E 5E      LD           C,$5E
6365: 3F         CCF
6366: 7F         LD           A,A
6367: 3F         CCF
6368: BF         CP           A
6369: 7F         LD           A,A
636A: FF         RST         0X38
636B: 7F         LD           A,A
636C: FF         RST         0X38
636D: 7F         LD           A,A
636E: BF         CP           A
636F: 7F         LD           A,A
6370: BF         CP           A
6371: 7F         LD           A,A
6372: 7F         LD           A,A
6373: 3F         CCF
6374: 5F         LD           E,A
6375: 3F         CCF
6376: 2F         CPL
6377: 1F         RRA
6378: 1B         DEC         DE
6379: 07         RLCA
637A: 07         RLCA
637B: 00         NOP
637C: 00         NOP
637D: 00         NOP
637E: 00         NOP
637F: 00         NOP
6380: 00         NOP
6381: 00         NOP
6382: 00         NOP
6383: 00         NOP
6384: 80         ADD         A,B
6385: 00         NOP
6386: 40         LD           B,B
6387: 80         ADD         A,B
6388: A0         AND         B
6389: C0         RET         NZ
638A: D8         RET         C
638B: E0 F7      LDFF00   ($F7),A
638D: F8 FF      LDHL       SP,$FF
638F: FF         RST         0X38
6390: FF         RST         0X38
6391: FF         RST         0X38
6392: FF         RST         0X38
6393: FF         RST         0X38
6394: FF         RST         0X38
6395: FF         RST         0X38
6396: FF         RST         0X38
6397: FF         RST         0X38
6398: FF         RST         0X38
6399: FF         RST         0X38
639A: 7D         LD           A,L
639B: FE FE      CP           $FE
639D: 00         NOP
639E: 00         NOP
639F: 00         NOP
63A0: 01 00 01   LD           BC,$0100
63A3: 00         NOP
63A4: 02         LD           (BC),A
63A5: 01 05 03   LD           BC,$0305
63A8: 0B         DEC         BC
63A9: 07         RLCA
63AA: 37         SCF
63AB: 0F         RRCA
63AC: DF         RST         0X18
63AD: 3F         CCF
63AE: FE FF      CP           $FF
63B0: FD                              
63B1: FE FA      CP           $FA
63B3: FC                              
63B4: F4                              
63B5: F8 D8      LDHL       SP,$D8
63B7: E0 60      LDFF00   ($60),A
63B9: 80         ADD         A,B
63BA: 80         ADD         A,B
63BB: 00         NOP
63BC: 00         NOP
63BD: 00         NOP
63BE: 00         NOP
63BF: 00         NOP
63C0: 56         LD           D,(HL)
63C1: 3C         INC         A
63C2: 76         HALT
63C3: 3C         INC         A
63C4: 6E         LD           L,(HL)
63C5: 3C         INC         A
63C6: 6A         LD           L,D
63C7: 3C         INC         A
63C8: 6C         LD           L,H
63C9: 38 BC      JR           C,$6387
63CB: 78         LD           A,B
63CC: FC                              
63CD: 78         LD           A,B
63CE: F4                              
63CF: 78         LD           A,B
63D0: 78         LD           A,B
63D1: F0 E8      LD           A,($E8)
63D3: F0 F0      LD           A,($F0)
63D5: E0 D0      LDFF00   ($D0),A
63D7: E0 E0      LDFF00   ($E0),A
63D9: C0         RET         NZ
63DA: A0         AND         B
63DB: C0         RET         NZ
63DC: 40         LD           B,B
63DD: 80         ADD         A,B
63DE: 80         ADD         A,B
63DF: 00         NOP
63E0: 00         NOP
63E1: 01 00 01   LD           BC,$0100
63E4: 01 00 01   LD           BC,$0100
63E7: 04         INC         B
63E8: 03         INC         BC
63E9: 06 07      LD           B,$07
63EB: 12         LD           (DE),A
63EC: 07         RLCA
63ED: 12         LD           (DE),A
63EE: 1F         RRA
63EF: 0A         LD           A,(BC)
63F0: 1F         RRA
63F1: 0A         LD           A,(BC)
63F2: 1F         RRA
63F3: 0A         LD           A,(BC)
63F4: 1F         RRA
63F5: 0A         LD           A,(BC)
63F6: 2F         CPL
63F7: 1A         LD           A,(DE)
63F8: 3F         CCF
63F9: 1A         LD           A,(DE)
63FA: 3B         DEC         SP
63FB: 16 3F      LD           D,$3F
63FD: 16 3D      LD           D,$3D
63FF: 16 06      LD           D,$06
6401: 00         NOP
6402: 0F         RRCA
6403: 06 0F      LD           B,$0F
6405: 06 1F      LD           B,$1F
6407: 06 2F      LD           B,$2F
6409: 16 2F      LD           D,$2F
640B: 16 4F      LD           D,$4F
640D: 36 4B      LD           (HL),$4B
640F: 36 77      LD           (HL),$77
6411: 3B         DEC         SP
6412: 75         LD           (HL),L
6413: 3B         DEC         SP
6414: 43         LD           B,E
6415: 3C         INC         A
6416: 21 1F 39   LD           HL,$391F
6419: 1F         RRA
641A: 18 0F      JR           $642B
641C: 0C         INC         C
641D: 03         INC         BC
641E: 03         INC         BC
641F: 00         NOP
6420: 02         LD           (BC),A
6421: 01 3A 01   LD           BC,$013A
6424: 46         LD           B,(HL)
6425: 39         ADD         HL,SP
6426: 9E         SBC         (HL)
6427: 61         LD           H,C
6428: A2         AND         D
6429: 5D         LD           E,L
642A: 8E         ADC         A,(HL)
642B: 71         LD           (HL),C
642C: 92         SUB         D
642D: 61         LD           H,C
642E: 62         LD           H,D
642F: 01 02 01   LD           BC,$0102
6432: 3A         LD           A,(HLD)
6433: 01 46 39   LD           BC,$3946
6436: 9E         SBC         (HL)
6437: 61         LD           H,C
6438: A2         AND         D
6439: 5D         LD           E,L
643A: 8E         ADC         A,(HL)
643B: 71         LD           (HL),C
643C: 92         SUB         D
643D: 61         LD           H,C
643E: 62         LD           H,D
643F: 01 00 00   LD           BC,$0000
6442: 00         NOP
6443: 00         NOP
6444: 00         NOP
6445: 00         NOP
6446: 00         NOP
6447: 00         NOP
6448: 00         NOP
6449: 00         NOP
644A: 00         NOP
644B: 00         NOP
644C: 00         NOP
644D: 00         NOP
644E: 00         NOP
644F: 00         NOP
6450: 06 00      LD           B,$00
6452: 0F         RRCA
6453: 06 0F      LD           B,$0F
6455: 06 1F      LD           B,$1F
6457: 06 2F      LD           B,$2F
6459: 16 2F      LD           D,$2F
645B: 16 4F      LD           D,$4F
645D: 36 4B      LD           (HL),$4B
645F: 36 77      LD           (HL),$77
6461: 3B         DEC         SP
6462: 75         LD           (HL),L
6463: 3B         DEC         SP
6464: 43         LD           B,E
6465: 3C         INC         A
6466: 21 1F 39   LD           HL,$391F
6469: 1F         RRA
646A: 18 0F      JR           $647B
646C: 0C         INC         C
646D: 03         INC         BC
646E: 03         INC         BC
646F: 00         NOP
6470: 02         LD           (BC),A
6471: 01 3A 01   LD           BC,$013A
6474: 46         LD           B,(HL)
6475: 39         ADD         HL,SP
6476: 9E         SBC         (HL)
6477: 61         LD           H,C
6478: A2         AND         D
6479: 5D         LD           E,L
647A: 8E         ADC         A,(HL)
647B: 71         LD           (HL),C
647C: 92         SUB         D
647D: 61         LD           H,C
647E: 62         LD           H,D
647F: 01 00 00   LD           BC,$0000
6482: 00         NOP
6483: 00         NOP
6484: 70         LD           (HL),B
6485: 00         NOP
6486: E8 70      ADD         SP,$70
6488: BC         CP           H
6489: 78         LD           A,B
648A: EE 1C      XOR         $1C
648C: 97         SUB         A
648D: 6E         LD           L,(HL)
648E: 8B         ADC         A,E
648F: 76         HALT
6490: 77         LD           (HL),A
6491: 3B         DEC         SP
6492: 75         LD           (HL),L
6493: 3B         DEC         SP
6494: 43         LD           B,E
6495: 3C         INC         A
6496: 21 1F 39   LD           HL,$391F
6499: 1F         RRA
649A: 18 0F      JR           $64AB
649C: 0C         INC         C
649D: 03         INC         BC
649E: 03         INC         BC
649F: 00         NOP
64A0: 03         INC         BC
64A1: 03         INC         BC
64A2: 3E 3F      LD           A,$3F
64A4: 65         LD           H,L
64A5: 7E         LD           A,(HL)
64A6: 5B         LD           E,E
64A7: 64         LD           H,H
64A8: AE         XOR         (HL)
64A9: D1         POP         DE
64AA: A5         AND         L
64AB: DB                              
64AC: CB BF      RES         1,E
64AE: DF         RST         0X18
64AF: BB         CP           E
64B0: DF         RST         0X18
64B1: B9         CP           C
64B2: CF         RST         0X08
64B3: B9         CP           C
64B4: A7         AND         A
64B5: DD                              
64B6: B3         OR           E
64B7: CF         RST         0X08
64B8: 5C         LD           E,H
64B9: 63         LD           H,E
64BA: 67         LD           H,A
64BB: 78         LD           A,B
64BC: 38 3F      JR           C,$64FD
64BE: 0F         RRCA
64BF: 0F         RRCA
64C0: 00         NOP
64C1: 00         NOP
64C2: 00         NOP
64C3: 00         NOP
64C4: 00         NOP
64C5: 00         NOP
64C6: 0D         DEC         C
64C7: 0D         DEC         C
64C8: 1A         LD           A,(DE)
64C9: 1F         RRA
64CA: 15         DEC         D
64CB: 1A         LD           A,(DE)
64CC: 36 39      LD           (HL),$39
64CE: 29         ADD         HL,HL
64CF: 37         SCF
64D0: 2B         DEC         HL
64D1: 37         SCF
64D2: 2B         DEC         HL
64D3: 37         SCF
64D4: 29         ADD         HL,HL
64D5: 37         SCF
64D6: 36 39      LD           (HL),$39
64D8: 19         ADD         HL,DE
64D9: 1E 0E      LD           E,$0E
64DB: 0F         RRCA
64DC: 03         INC         BC
64DD: 03         INC         BC
64DE: 00         NOP
64DF: 00         NOP
64E0: 00         NOP
64E1: 00         NOP
64E2: 00         NOP
64E3: 00         NOP
64E4: 00         NOP
64E5: 00         NOP
64E6: 00         NOP
64E7: 00         NOP
64E8: 00         NOP
64E9: 00         NOP
64EA: 03         INC         BC
64EB: 03         INC         BC
64EC: 06 07      LD           B,$07
64EE: 05         DEC         B
64EF: 06 0A      LD           B,$0A
64F1: 0D         DEC         C
64F2: 0A         LD           A,(BC)
64F3: 0D         DEC         C
64F4: 0D         DEC         C
64F5: 0E 06      LD           C,$06
64F7: 07         RLCA
64F8: 03         INC         BC
64F9: 03         INC         BC
64FA: 00         NOP
64FB: 00         NOP
64FC: 00         NOP
64FD: 00         NOP
64FE: 00         NOP
64FF: 00         NOP
6500: FF         RST         0X38
6501: 00         NOP
6502: FF         RST         0X38
6503: 7F         LD           A,A
6504: C0         RET         NZ
6505: 7F         LD           A,A
6506: C0         RET         NZ
6507: 7F         LD           A,A
6508: 86         ADD         A,(HL)
6509: 79         LD           A,C
650A: FF         RST         0X38
650B: 00         NOP
650C: C0         RET         NZ
650D: 3F         CCF
650E: F3         DI
650F: 3F         CCF
6510: EC                              
6511: 3F         CCF
6512: E0 3F      LDFF00   ($3F),A
6514: C0         RET         NZ
6515: 3F         CCF
6516: C0         RET         NZ
6517: 3F         CCF
6518: 64         LD           H,H
6519: 1B         DEC         DE
651A: 34         INC         (HL)
651B: 0F         RRCA
651C: 18 07      JR           $6525
651E: 0F         RRCA
651F: 00         NOP
6520: FF         RST         0X38
6521: 00         NOP
6522: CF         RST         0X08
6523: FF         RST         0X38
6524: 30 FF      JR           NC,$6525
6526: 00         NOP
6527: FF         RST         0X38
6528: 00         NOP
6529: FF         RST         0X38
652A: FF         RST         0X38
652B: 00         NOP
652C: 00         NOP
652D: FF         RST         0X38
652E: F1         POP         AF
652F: FF         RST         0X38
6530: 0E FF      LD           C,$FF
6532: 00         NOP
6533: FF         RST         0X38
6534: C0         RET         NZ
6535: 3F         CCF
6536: C0         RET         NZ
6537: FF         RST         0X38
6538: 00         NOP
6539: FF         RST         0X38
653A: 00         NOP
653B: FF         RST         0X38
653C: 8C         ADC         A,H
653D: 73         LD           (HL),E
653E: FF         RST         0X38
653F: 00         NOP
6540: FF         RST         0X38
6541: 00         NOP
6542: FF         RST         0X38
6543: 7F         LD           A,A
6544: C0         RET         NZ
6545: 7F         LD           A,A
6546: C0         RET         NZ
6547: 7F         LD           A,A
6548: 87         ADD         A,A
6549: 78         LD           A,B
654A: FD                              
654B: 03         INC         BC
654C: C2 3F F3   JP           NZ,$F33F
654F: 3E EC      LD           A,$EC
6551: 3F         CCF
6552: E0 3F      LDFF00   ($3F),A
6554: C0         RET         NZ
6555: 3F         CCF
6556: C0         RET         NZ
6557: 3F         CCF
6558: 64         LD           H,H
6559: 1B         DEC         DE
655A: 34         INC         (HL)
655B: 0B         DEC         BC
655C: 1A         LD           A,(DE)
655D: 05         DEC         B
655E: 0F         RRCA
655F: 00         NOP
6560: FF         RST         0X38
6561: 00         NOP
6562: CF         RST         0X08
6563: FF         RST         0X38
6564: 70         LD           (HL),B
6565: FF         RST         0X38
6566: F8 07      LDHL       SP,$07
6568: 76         HALT
6569: F9         LD           SP,HL
656A: 8D         ADC         A,L
656B: FE F2      CP           $F2
656D: 0F         RRCA
656E: FD                              
656F: 03         INC         BC
6570: 1E E1      LD           E,$E1
6572: 00         NOP
6573: FF         RST         0X38
6574: 3F         CCF
6575: C0         RET         NZ
6576: 7F         LD           A,A
6577: B6         OR           (HL)
6578: FF         RST         0X38
6579: 20 E0      JR           NZ,$655B
657B: 1F         RRA
657C: 0C         INC         C
657D: F3         DI
657E: FF         RST         0X38
657F: 00         NOP
6580: FF         RST         0X38
6581: 00         NOP
6582: FF         RST         0X38
6583: 66         LD           H,(HL)
6584: F6 69      OR           $69
6586: E0 1F      LDFF00   ($1F),A
6588: C0         RET         NZ
6589: 3F         CCF
658A: ED                              
658B: 53         LD           D,E
658C: EF         RST         0X28
658D: 54         LD           D,H
658E: CF         RST         0X08
658F: 37         SCF
6590: CB 36      SWAP      4,(HL)
6592: E7         RST         0X20
6593: 58         LD           E,B
6594: E0 5F      LDFF00   ($5F),A
6596: C3 3C E0   JP           $E03C
6599: 1F         RRA
659A: F6 69      OR           $69
659C: FF         RST         0X38
659D: 66         LD           H,(HL)
659E: FF         RST         0X38
659F: 00         NOP
65A0: FF         RST         0X38
65A1: 00         NOP
65A2: FF         RST         0X38
65A3: 66         LD           H,(HL)
65A4: F6 69      OR           $69
65A6: E0 1F      LDFF00   ($1F),A
65A8: C3 3C E5   JP           $E53C
65AB: 5B         LD           E,E
65AC: E7         RST         0X20
65AD: 5B         LD           E,E
65AE: C7         RST         0X00
65AF: 3A         LD           A,(HLD)
65B0: C5         PUSH       BC
65B1: 3A         LD           A,(HLD)
65B2: E3                              
65B3: 5C         LD           E,H
65B4: E0 5F      LDFF00   ($5F),A
65B6: C1         POP         BC
65B7: 3E E0      LD           A,$E0
65B9: 1F         RRA
65BA: F6 69      OR           $69
65BC: FF         RST         0X38
65BD: 66         LD           H,(HL)
65BE: FF         RST         0X38
65BF: 00         NOP
65C0: 0F         RRCA
65C1: 09         ADD         HL,BC
65C2: 3F         CCF
65C3: 18 7F      JR           $6644
65C5: 03         INC         BC
65C6: 7F         LD           A,A
65C7: 4F         LD           C,A
65C8: FF         RST         0X38
65C9: D3                              
65CA: FF         RST         0X38
65CB: 19         ADD         HL,DE
65CC: FF         RST         0X38
65CD: 3D         DEC         A
65CE: FF         RST         0X38
65CF: AF         XOR         A
65D0: FF         RST         0X38
65D1: A7         AND         A
65D2: FF         RST         0X38
65D3: 39         ADD         HL,SP
65D4: FF         RST         0X38
65D5: 1C         INC         E
65D6: FF         RST         0X38
65D7: DE 7F      SBC         $7F
65D9: 4F         LD           C,A
65DA: 7F         LD           A,A
65DB: 03         INC         BC
65DC: 3F         CCF
65DD: 18 0F      JR           $65EE
65DF: 09         ADD         HL,BC
65E0: 7F         LD           A,A
65E1: 00         NOP
65E2: 4F         LD           C,A
65E3: 3F         CCF
65E4: 47         LD           B,A
65E5: 3F         CCF
65E6: 20 1F      JR           NZ,$6607
65E8: 1F         RRA
65E9: 00         NOP
65EA: 20 1F      JR           NZ,$660B
65EC: 43         LD           B,E
65ED: 3F         CCF
65EE: 43         LD           B,E
65EF: 3F         CCF
65F0: 81         ADD         A,C
65F1: 7F         LD           A,A
65F2: 80         ADD         A,B
65F3: 7F         LD           A,A
65F4: A3         AND         E
65F5: 5C         LD           E,H
65F6: D2 2D 9E   JP           NC,$9E2D
65F9: 61         LD           H,C
65FA: 40         LD           B,B
65FB: 3F         CCF
65FC: 20 1F      JR           NZ,$661D
65FE: 1F         RRA
65FF: 00         NOP
6600: 00         NOP
6601: 00         NOP
6602: 3F         CCF
6603: 00         NOP
6604: 21 1F 21   LD           HL,$211F
6607: 1F         RRA
6608: 21 1F 21   LD           HL,$211F
660B: 1F         RRA
660C: 3F         CCF
660D: 1F         RRA
660E: 3F         CCF
660F: 1F         RRA
6610: 21 1F 21   LD           HL,$211F
6613: 1F         RRA
6614: 21 1F 21   LD           HL,$211F
6617: 1F         RRA
6618: 3F         CCF
6619: 00         NOP
661A: 3F         CCF
661B: 00         NOP
661C: 00         NOP
661D: 00         NOP
661E: 00         NOP
661F: 00         NOP
6620: 01 00 02   LD           BC,$0200
6623: 01 04 03   LD           BC,$0304
6626: 08 07 1C   LD           ($1C07),SP
6629: 0F         RRCA
662A: 26 1F      LD           H,$1F
662C: 43         LD           B,E
662D: 3F         CCF
662E: 81         ADD         A,C
662F: 7F         LD           A,A
6630: C3 3F 66   JP           $663F
6633: 1F         RRA
6634: 3C         INC         A
6635: 0F         RRCA
6636: 1C         INC         E
6637: 07         RLCA
6638: 0C         INC         C
6639: 03         INC         BC
663A: 06 01      LD           B,$01
663C: 03         INC         BC
663D: 00         NOP
663E: 01 00 03   LD           BC,$0300
6641: 00         NOP
6642: 02         LD           (BC),A
6643: 01 03 00   LD           BC,$0003
6646: 02         LD           (BC),A
6647: 01 0F 01   LD           BC,$010F
664A: 1B         DEC         DE
664B: 0D         DEC         C
664C: 2E 11      LD           L,$11
664E: 5A         LD           E,D
664F: 21 B2 41   LD           HL,$41B2
6652: A2         AND         D
6653: 41         LD           B,C
6654: A2         AND         D
6655: 41         LD           B,C
6656: A2         AND         D
6657: 41         LD           B,C
6658: BE         CP           (HL)
6659: 41         LD           B,C
665A: 87         ADD         A,A
665B: 7D         LD           A,L
665C: FE 01      CP           $01
665E: 7F         LD           A,A
665F: 00         NOP
6660: 02         LD           (BC),A
6661: 01 02 01   LD           BC,$0102
6664: 02         LD           (BC),A
6665: 01 02 01   LD           BC,$0102
6668: 02         LD           (BC),A
6669: 01 02 01   LD           BC,$0102
666C: 02         LD           (BC),A
666D: 01 02 01   LD           BC,$0102
6670: 02         LD           (BC),A
6671: 01 02 01   LD           BC,$0102
6674: 02         LD           (BC),A
6675: 01 02 01   LD           BC,$0102
6678: 02         LD           (BC),A
6679: 01 02 01   LD           BC,$0102
667C: 02         LD           (BC),A
667D: 01 02 01   LD           BC,$0102
6680: 3F         CCF
6681: 00         NOP
6682: 7F         LD           A,A
6683: 3F         CCF
6684: EF         RST         0X28
6685: 70         LD           (HL),B
6686: D0         RET         NC
6687: 6F         LD           L,A
6688: E0 5F      LDFF00   ($5F),A
668A: E0 5F      LDFF00   ($5F),A
668C: E0 5F      LDFF00   ($5F),A
668E: D0         RET         NC
668F: 6F         LD           L,A
6690: EF         RST         0X28
6691: 70         LD           (HL),B
6692: BF         CP           A
6693: 7F         LD           A,A
6694: 9F         SBC         A
6695: 7F         LD           A,A
6696: C0         RET         NZ
6697: 3F         CCF
6698: 60         LD           H,B
6699: 1F         RRA
669A: 3F         CCF
669B: 00         NOP
669C: 23         INC         HL
669D: 1F         RRA
669E: 27         DAA
669F: 1F         RRA
66A0: 27         DAA
66A1: 1F         RRA
66A2: 23         INC         HL
66A3: 1F         RRA
66A4: 33         INC         SP
66A5: 0F         RRCA
66A6: 2C         INC         L
66A7: 13         INC         DE
66A8: 2B         DEC         HL
66A9: 1C         INC         E
66AA: 27         DAA
66AB: 1F         RRA
66AC: 23         INC         HL
66AD: 1F         RRA
66AE: 27         DAA
66AF: 1F         RRA
66B0: 27         DAA
66B1: 1F         RRA
66B2: 23         INC         HL
66B3: 1F         RRA
66B4: 33         INC         SP
66B5: 0F         RRCA
66B6: 2C         INC         L
66B7: 13         INC         DE
66B8: 2B         DEC         HL
66B9: 1C         INC         E
66BA: 27         DAA
66BB: 1F         RRA
66BC: 23         INC         HL
66BD: 1F         RRA
66BE: 27         DAA
66BF: 1F         RRA
66C0: 27         DAA
66C1: 1F         RRA
66C2: 23         INC         HL
66C3: 1F         RRA
66C4: 33         INC         SP
66C5: 0F         RRCA
66C6: 2C         INC         L
66C7: 13         INC         DE
66C8: 27         DAA
66C9: 1C         INC         E
66CA: 63         LD           H,E
66CB: 1F         RRA
66CC: A3         AND         E
66CD: 5F         LD           E,A
66CE: A7         AND         A
66CF: 5F         LD           E,A
66D0: A7         AND         A
66D1: 5F         LD           E,A
66D2: B3         OR           E
66D3: 6F         LD           L,A
66D4: BC         CP           H
66D5: 73         LD           (HL),E
66D6: 9B         SBC         E
66D7: 7C         LD           A,H
66D8: 8F         ADC         A,A
66D9: 7F         LD           A,A
66DA: C0         RET         NZ
66DB: 3F         CCF
66DC: 60         LD           H,B
66DD: 1F         RRA
66DE: 3F         CCF
66DF: 00         NOP
66E0: 03         INC         BC
66E1: 00         NOP
66E2: 0F         RRCA
66E3: 00         NOP
66E4: 1F         RRA
66E5: 00         NOP
66E6: 3E 01      LD           A,$01
66E8: 3D         DEC         A
66E9: 03         INC         BC
66EA: 7D         LD           A,L
66EB: 03         INC         BC
66EC: 7E         LD           A,(HL)
66ED: 01 5F 20   LD           BC,$205F
66F0: 5F         LD           E,A
66F1: 20 4F      JR           NZ,$6742
66F3: 30 23      JR           NC,$6718
66F5: 1C         INC         E
66F6: 20 1F      JR           NZ,$6717
66F8: 10 0F      STOP       $0F
66FA: 0C         INC         C
66FB: 03         INC         BC
66FC: 03         INC         BC
66FD: 00         NOP
66FE: 00         NOP
66FF: 00         NOP
6700: 00         NOP
6701: 00         NOP
6702: 01 00 07   LD           BC,$0700
6705: 00         NOP
6706: 0F         RRCA
6707: 00         NOP
6708: 1F         RRA
6709: 0D         DEC         C
670A: 1F         RRA
670B: 0F         RRCA
670C: 3F         CCF
670D: 0A         LD           A,(BC)
670E: 3F         CCF
670F: 1F         RRA
6710: 7F         LD           A,A
6711: 3B         DEC         SP
6712: 7F         LD           A,A
6713: 04         INC         B
6714: 3F         CCF
6715: 1F         RRA
6716: 1F         RRA
6717: 00         NOP
6718: 1F         RRA
6719: 04         INC         B
671A: 3F         CCF
671B: 16 3F      LD           D,$3F
671D: 06 07      LD           B,$07
671F: 00         NOP
6720: 00         NOP
6721: 00         NOP
6722: E0 00      LDFF00   ($00),A
6724: F0 00      LD           A,($00)
6726: F8 10      LDHL       SP,$10
6728: F8 90      LDHL       SP,$90
672A: F8 C0      LDHL       SP,$C0
672C: FC                              
672D: C0         RET         NZ
672E: FE C0      CP           $C0
6730: DE E0      SBC         $E0
6732: D6 68      SUB         $68
6734: B6         OR           (HL)
6735: C8         RET         Z
6736: EC                              
6737: 10 FC      STOP       $FC
6739: 40         LD           B,B
673A: EE DC      XOR         $DC
673C: FE C0      CP           $C0
673E: C0         RET         NZ
673F: 00         NOP
6740: 00         NOP
6741: 00         NOP
6742: 03         INC         BC
6743: 00         NOP
6744: 07         RLCA
6745: 00         NOP
6746: 0F         RRCA
6747: 02         LD           (BC),A
6748: 0F         RRCA
6749: 02         LD           (BC),A
674A: 3F         CCF
674B: 08 7F 30   LD           ($307F),SP
674E: 7F         LD           A,A
674F: 30 4F      JR           NC,$67A0
6751: 30 3F      JR           NC,$6792
6753: 00         NOP
6754: 3F         CCF
6755: 00         NOP
6756: 6F         LD           L,A
6757: 30 7F      JR           NC,$67D8
6759: 20 7F      JR           NZ,$67DA
675B: 34         INC         (HL)
675C: 3B         DEC         SP
675D: 07         RLCA
675E: 07         RLCA
675F: 00         NOP
6760: 00         NOP
6761: 00         NOP
6762: C0         RET         NZ
6763: 00         NOP
6764: E0 00      LDFF00   ($00),A
6766: F0 00      LD           A,($00)
6768: F0 00      LD           A,($00)
676A: F0 00      LD           A,($00)
676C: F0 00      LD           A,($00)
676E: F8 00      LDHL       SP,$00
6770: FC                              
6771: 00         NOP
6772: 3A         LD           A,(HLD)
6773: C4 12 EC   CALL       NZ,$EC12
6776: 96         SUB         (HL)
6777: 68         LD           L,B
6778: FC                              
6779: 00         NOP
677A: FC                              
677B: 00         NOP
677C: FC                              
677D: 98         SBC         B
677E: FC                              
677F: 00         NOP
6780: 0E 00      LD           C,$00
6782: 1F         RRA
6783: 0E 3F      LD           C,$3F
6785: 06 3F      LD           B,$3F
6787: 00         NOP
6788: 7F         LD           A,A
6789: 0D         DEC         C
678A: 7F         LD           A,A
678B: 0F         RRCA
678C: 7F         LD           A,A
678D: 0A         LD           A,(BC)
678E: 3F         CCF
678F: 1F         RRA
6790: 7F         LD           A,A
6791: 3B         DEC         SP
6792: 7F         LD           A,A
6793: 04         INC         B
6794: 3F         CCF
6795: 1F         RRA
6796: 1F         RRA
6797: 00         NOP
6798: 1F         RRA
6799: 00         NOP
679A: 37         SCF
679B: 18 3F      JR           $67DC
679D: 00         NOP
679E: 01 00 1C   LD           BC,$1C00
67A1: 00         NOP
67A2: 3E 1C      LD           A,$1C
67A4: 7F         LD           A,A
67A5: 0C         INC         C
67A6: FF         RST         0X38
67A7: 00         NOP
67A8: FF         RST         0X38
67A9: 0D         DEC         C
67AA: FF         RST         0X38
67AB: 0F         RRCA
67AC: 7F         LD           A,A
67AD: 0A         LD           A,(BC)
67AE: 3F         CCF
67AF: 1F         RRA
67B0: 7F         LD           A,A
67B1: 3B         DEC         SP
67B2: 7F         LD           A,A
67B3: 04         INC         B
67B4: 3F         CCF
67B5: 1F         RRA
67B6: 1F         RRA
67B7: 00         NOP
67B8: 1F         RRA
67B9: 00         NOP
67BA: 37         SCF
67BB: 18 3F      JR           $67FC
67BD: 00         NOP
67BE: 01 00 03   LD           BC,$0300
67C1: 00         NOP
67C2: 6F         LD           L,A
67C3: 00         NOP
67C4: FF         RST         0X38
67C5: 6D         LD           L,L
67C6: FF         RST         0X38
67C7: 4A         LD           C,D
67C8: FF         RST         0X38
67C9: 5F         LD           E,A
67CA: FF         RST         0X38
67CB: 3B         DEC         SP
67CC: 7F         LD           A,A
67CD: 04         INC         B
67CE: 5F         LD           E,A
67CF: 3F         CCF
67D0: 2F         CPL
67D1: 1F         RRA
67D2: 1F         RRA
67D3: 00         NOP
67D4: 13         INC         DE
67D5: 0C         INC         C
67D6: 18 07      JR           $67DF
67D8: 0F         RRCA
67D9: 00         NOP
67DA: 07         RLCA
67DB: 00         NOP
67DC: 03         INC         BC
67DD: 01 01 00   LD           BC,$0001
67E0: C0         RET         NZ
67E1: 00         NOP
67E2: F8 00      LDHL       SP,$00
67E4: FC                              
67E5: B8         CP           B
67E6: FE B8      CP           $B8
67E8: FE 88      CP           $88
67EA: FE C0      CP           $C0
67EC: FE 60      CP           $60
67EE: DE E0      SBC         $E0
67F0: FC                              
67F1: 80         ADD         A,B
67F2: FC                              
67F3: 00         NOP
67F4: 1E E0      LD           E,$E0
67F6: 1E E0      LD           E,$E0
67F8: FF         RST         0X38
67F9: 04         INC         B
67FA: FF         RST         0X38
67FB: 0E CF      LD           C,$CF
67FD: 86         ADD         A,(HL)
67FE: C6 00      ADD         $00
6800: 1C         INC         E
6801: 00         NOP
6802: 3E 1C      LD           A,$1C
6804: 7F         LD           A,A
6805: 3E 73      LD           A,$73
6807: 3E 33      LD           A,$33
6809: 1D         DEC         E
680A: 1D         DEC         E
680B: 03         INC         BC
680C: 3C         INC         A
680D: 1B         DEC         DE
680E: 73         LD           (HL),E
680F: 3C         INC         A
6810: 73         LD           (HL),E
6811: 3E 7F      LD           A,$7F
6813: 3E 3F      LD           A,$3F
6815: 1C         INC         E
6816: 1F         RRA
6817: 00         NOP
6818: 13         INC         DE
6819: 0C         INC         C
681A: 19         ADD         HL,DE
681B: 07         RLCA
681C: 0C         INC         C
681D: 03         INC         BC
681E: 07         RLCA
681F: 00         NOP
6820: 03         INC         BC
6821: 00         NOP
6822: 07         RLCA
6823: 03         INC         BC
6824: 06 03      LD           B,$03
6826: 75         LD           (HL),L
6827: 02         LD           (BC),A
6828: FF         RST         0X38
6829: 71         LD           (HL),C
682A: E5         PUSH       HL
682B: 7B         LD           A,E
682C: E4                              
682D: 7B         LD           A,E
682E: FF         RST         0X38
682F: 70         LD           (HL),B
6830: 7E         LD           A,(HL)
6831: 03         INC         BC
6832: 0E 07      LD           C,$07
6834: 0F         RRCA
6835: 07         RLCA
6836: 17         RLA
6837: 0B         DEC         BC
6838: 13         INC         DE
6839: 0C         INC         C
683A: 19         ADD         HL,DE
683B: 07         RLCA
683C: 0C         INC         C
683D: 03         INC         BC
683E: 07         RLCA
683F: 00         NOP
6840: 03         INC         BC
6841: 00         NOP
6842: 02         LD           (BC),A
6843: 01 03 00   LD           BC,$0003
6846: 02         LD           (BC),A
6847: 01 0F 01   LD           BC,$010F
684A: 1B         DEC         DE
684B: 0D         DEC         C
684C: 2E 11      LD           L,$11
684E: 5A         LD           E,D
684F: 21 B2 41   LD           HL,$41B2
6852: A2         AND         D
6853: 41         LD           B,C
6854: A2         AND         D
6855: 41         LD           B,C
6856: A2         AND         D
6857: 41         LD           B,C
6858: BE         CP           (HL)
6859: 41         LD           B,C
685A: 87         ADD         A,A
685B: 7D         LD           A,L
685C: FE 01      CP           $01
685E: 7F         LD           A,A
685F: 00         NOP
6860: 02         LD           (BC),A
6861: 01 02 01   LD           BC,$0102
6864: 02         LD           (BC),A
6865: 01 02 01   LD           BC,$0102
6868: 02         LD           (BC),A
6869: 01 02 01   LD           BC,$0102
686C: 02         LD           (BC),A
686D: 01 02 01   LD           BC,$0102
6870: 02         LD           (BC),A
6871: 01 02 01   LD           BC,$0102
6874: 02         LD           (BC),A
6875: 01 02 01   LD           BC,$0102
6878: 02         LD           (BC),A
6879: 01 02 01   LD           BC,$0102
687C: 02         LD           (BC),A
687D: 01 02 01   LD           BC,$0102
6880: 00         NOP
6881: FF         RST         0X38
6882: 00         NOP
6883: FF         RST         0X38
6884: 24         INC         H
6885: FF         RST         0X38
6886: 18 FF      JR           $6887
6888: 18 FF      JR           $6889
688A: 24         INC         H
688B: FF         RST         0X38
688C: 00         NOP
688D: FF         RST         0X38
688E: 00         NOP
688F: FF         RST         0X38
6890: 00         NOP
6891: FF         RST         0X38
6892: 00         NOP
6893: FF         RST         0X38
6894: 24         INC         H
6895: FF         RST         0X38
6896: 18 FF      JR           $6897
6898: 18 FF      JR           $6899
689A: 24         INC         H
689B: FF         RST         0X38
689C: 00         NOP
689D: FF         RST         0X38
689E: 00         NOP
689F: FF         RST         0X38
68A0: 03         INC         BC
68A1: 00         NOP
68A2: 1C         INC         E
68A3: 03         INC         BC
68A4: 3E 01      LD           A,$01
68A6: 0F         RRCA
68A7: 04         INC         B
68A8: 1F         RRA
68A9: 0F         RRCA
68AA: 2F         CPL
68AB: 1B         DEC         DE
68AC: 4F         LD           C,A
68AD: 3B         DEC         SP
68AE: 40         LD           B,B
68AF: 3F         CCF
68B0: 50         LD           D,B
68B1: 2F         CPL
68B2: 4F         LD           C,A
68B3: 30 20      JR           NC,$68D5
68B5: 1F         RRA
68B6: 1F         RRA
68B7: 00         NOP
68B8: 0B         DEC         BC
68B9: 07         RLCA
68BA: 3D         DEC         A
68BB: 03         INC         BC
68BC: 77         LD           (HL),A
68BD: 38 7E      JR           C,$693D
68BF: 00         NOP
68C0: C0         RET         NZ
68C1: 00         NOP
68C2: 7C         LD           A,H
68C3: 80         ADD         A,B
68C4: FE 00      CP           $00
68C6: F0 60      LD           A,($60)
68C8: E8 F0      ADD         SP,$F0
68CA: E4                              
68CB: B8         CP           B
68CC: E2         LDFF00   (C),A
68CD: BC         CP           H
68CE: 02         LD           (BC),A
68CF: FC                              
68D0: 12         LD           (DE),A
68D1: EC                              
68D2: E2         LDFF00   (C),A
68D3: 1C         INC         E
68D4: 04         INC         B
68D5: F8 F8      LDHL       SP,$F8
68D7: 00         NOP
68D8: D8         RET         C
68D9: E0 AC      LDFF00   ($AC),A
68DB: D8         RET         C
68DC: FC                              
68DD: 00         NOP
68DE: 00         NOP
68DF: 00         NOP
68E0: 00         NOP
68E1: 00         NOP
68E2: 00         NOP
68E3: 00         NOP
68E4: 00         NOP
68E5: 00         NOP
68E6: 00         NOP
68E7: 00         NOP
68E8: 00         NOP
68E9: 00         NOP
68EA: 00         NOP
68EB: 00         NOP
68EC: 00         NOP
68ED: 00         NOP
68EE: 00         NOP
68EF: 00         NOP
68F0: F3         DI
68F1: 00         NOP
68F2: 3C         INC         A
68F3: 03         INC         BC
68F4: 4E         LD           C,(HL)
68F5: 31 87 78   LD           SP,$7887
68F8: BF         CP           A
68F9: 76         HALT
68FA: 7F         LD           A,A
68FB: 00         NOP
68FC: F2                              
68FD: 7D         LD           A,L
68FE: 7F         LD           A,A
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
6916: 01 00 03   LD           BC,$0300
6919: 00         NOP
691A: 07         RLCA
691B: 00         NOP
691C: 07         RLCA
691D: 00         NOP
691E: 0F         RRCA
691F: 00         NOP
6920: 07         RLCA
6921: 00         NOP
6922: 0F         RRCA
6923: 07         RLCA
6924: 0D         DEC         C
6925: 03         INC         BC
6926: 0F         RRCA
6927: 07         RLCA
6928: 1F         RRA
6929: 03         INC         BC
692A: 1F         RRA
692B: 08 1F 00   LD           ($001F),SP
692E: 3F         CCF
692F: 10 3F      STOP       $3F
6931: 0E 7F      LD           C,$7F
6933: 1F         RRA
6934: FF         RST         0X38
6935: 1F         RRA
6936: FF         RST         0X38
6937: 23         INC         HL
6938: FF         RST         0X38
6939: 37         SCF
693A: FF         RST         0X38
693B: 36 FF      LD           (HL),$FF
693D: 01 FF 5F   LD           BC,$5FFF
6940: F8 00      LDHL       SP,$00
6942: FC                              
6943: F8 BE      LDHL       SP,$BE
6945: CC FE F4   CALL       Z,$F4FE
6948: FE 84      CP           $84
694A: FE 34      CP           $34
694C: FC                              
694D: 10 F8      STOP       $F8
694F: C0         RET         NZ
6950: FC                              
6951: 40         LD           B,B
6952: FE 00      CP           $00
6954: FF         RST         0X38
6955: 80         ADD         A,B
6956: FF         RST         0X38
6957: C3 FF C6   JP           $C6FF
695A: FF         RST         0X38
695B: C6 FF      ADD         $FF
695D: 86         ADD         A,(HL)
695E: FF         RST         0X38
695F: 06 0F      LD           B,$0F
6961: 00         NOP
6962: 1F         RRA
6963: 00         NOP
6964: 1F         RRA
6965: 00         NOP
6966: 1F         RRA
6967: 0C         INC         C
6968: 1F         RRA
6969: 0E 1F      LD           C,$1F
696B: 0C         INC         C
696C: 1F         RRA
696D: 0E 0F      LD           C,$0F
696F: 06 07      LD           B,$07
6971: 00         NOP
6972: 03         INC         BC
6973: 00         NOP
6974: 0F         RRCA
6975: 00         NOP
6976: 1F         RRA
6977: 0F         RRCA
6978: 3F         CCF
6979: 1F         RRA
697A: 3F         CCF
697B: 15         DEC         D
697C: 3F         CCF
697D: 00         NOP
697E: 00         NOP
697F: 00         NOP
6980: FF         RST         0X38
6981: 60         LD           H,B
6982: FF         RST         0X38
6983: 60         LD           H,B
6984: FF         RST         0X38
6985: FF         RST         0X38
6986: FF         RST         0X38
6987: 8F         ADC         A,A
6988: D3                              
6989: AF         XOR         A
698A: FC                              
698B: 8F         ADC         A,A
698C: BF         CP           A
698D: FF         RST         0X38
698E: BF         CP           A
698F: FF         RST         0X38
6990: BF         CP           A
6991: FF         RST         0X38
6992: DF         RST         0X18
6993: 7F         LD           A,A
6994: CF         RST         0X08
6995: 7F         LD           A,A
6996: 70         LD           (HL),B
6997: BF         CP           A
6998: BF         CP           A
6999: DF         RST         0X18
699A: DF         RST         0X18
699B: E0 FF      LDFF00   ($FF),A
699D: 00         NOP
699E: 00         NOP
699F: 00         NOP
69A0: 73         LD           (HL),E
69A1: 00         NOP
69A2: 5F         LD           E,A
69A3: 33         INC         SP
69A4: 2C         INC         L
69A5: 1B         DEC         DE
69A6: 37         SCF
69A7: 0C         INC         C
69A8: 6B         LD           L,E
69A9: 36 7D      LD           (HL),$7D
69AB: 23         INC         HL
69AC: 76         HALT
69AD: 29         ADD         HL,HL
69AE: 5F         LD           E,A
69AF: 30 6F      JR           NC,$6A20
69B1: 1C         INC         E
69B2: 5B         LD           E,E
69B3: 27         DAA
69B4: 4F         LD           C,A
69B5: 38 4F      JR           C,$6A06
69B7: 3F         CCF
69B8: 4F         LD           C,A
69B9: 3F         CCF
69BA: 27         DAA
69BB: 1F         RRA
69BC: 18 07      JR           $69C5
69BE: 07         RLCA
69BF: 00         NOP
69C0: C0         RET         NZ
69C1: 00         NOP
69C2: F0 C0      LD           A,($C0)
69C4: 38 F0      JR           C,$69B6
69C6: EC                              
69C7: 18 76      JR           $6A3F
69C9: 8C         ADC         A,H
69CA: BE         CP           (HL)
69CB: 44         LD           B,H
69CC: BE         CP           (HL)
69CD: 44         LD           B,H
69CE: FA 0C F6   LD           A,($F60C)
69D1: 38 DA      JR           C,$69AD
69D3: E4                              
69D4: FA 14 FA   LD           A,($FA14)
69D7: C4 F2 FC   CALL       NZ,$FCF2
69DA: E4                              
69DB: F8 18      LDHL       SP,$18
69DD: E0 E0      LDFF00   ($E0),A
69DF: 00         NOP
69E0: 3C         INC         A
69E1: 00         NOP
69E2: FF         RST         0X38
69E3: 18 BD      JR           $69A2
69E5: 66         LD           H,(HL)
69E6: 99         SBC         C
69E7: 6E         LD           L,(HL)
69E8: 52         LD           D,D
69E9: 2C         INC         L
69EA: 24         INC         H
69EB: 18 3C      JR           $6A29
69ED: 00         NOP
69EE: 42         LD           B,D
69EF: 3C         INC         A
69F0: 99         SBC         C
69F1: 7E         LD           A,(HL)
69F2: DB                              
69F3: 24         INC         H
69F4: BD         CP           L
69F5: 5A         LD           E,D
69F6: 99         SBC         C
69F7: 7E         LD           A,(HL)
69F8: DB                              
69F9: 24         INC         H
69FA: A5         AND         L
69FB: 5A         LD           E,D
69FC: 42         LD           B,D
69FD: 3C         INC         A
69FE: 3C         INC         A
69FF: 00         NOP
6A00: 00         NOP
6A01: 00         NOP
6A02: 00         NOP
6A03: 00         NOP
6A04: 1E 00      LD           E,$00
6A06: 21 1E 5E   LD           HL,$5E1E
6A09: 21 5E 21   LD           HL,$215E
6A0C: 5E         LD           E,(HL)
6A0D: 21 6D 1E   LD           HL,$1E6D
6A10: 7F         LD           A,A
6A11: 00         NOP
6A12: 5E         LD           E,(HL)
6A13: 21 4C 3F   LD           HL,$3F4C
6A16: 6D         LD           L,L
6A17: 1E 7F      LD           E,$7F
6A19: 00         NOP
6A1A: 5E         LD           E,(HL)
6A1B: 21 2D 1E   LD           HL,$1E2D
6A1E: 1E 00      LD           E,$00
6A20: 3C         INC         A
6A21: 00         NOP
6A22: 7E         LD           A,(HL)
6A23: 3C         INC         A
6A24: C7         RST         0X00
6A25: 7E         LD           A,(HL)
6A26: C3 FE C3   JP           $C3FE
6A29: FE FE      CP           $FE
6A2B: 3C         INC         A
6A2C: BC         CP           H
6A2D: 00         NOP
6A2E: 80         ADD         A,B
6A2F: 00         NOP
6A30: 80         ADD         A,B
6A31: 00         NOP
6A32: 80         ADD         A,B
6A33: 00         NOP
6A34: 80         ADD         A,B
6A35: 00         NOP
6A36: 80         ADD         A,B
6A37: 00         NOP
6A38: 80         ADD         A,B
6A39: 00         NOP
6A3A: 80         ADD         A,B
6A3B: 00         NOP
6A3C: 00         NOP
6A3D: 00         NOP
6A3E: 00         NOP
6A3F: 00         NOP
6A40: 00         NOP
6A41: 00         NOP
6A42: 00         NOP
6A43: 00         NOP
6A44: 38 00      JR           C,$6A46
6A46: 2C         INC         L
6A47: 18 2F      JR           $6A78
6A49: 1C         INC         E
6A4A: E7         RST         0X20
6A4B: 1F         RRA
6A4C: B8         CP           B
6A4D: 67         LD           H,A
6A4E: BF         CP           A
6A4F: 78         LD           A,B
6A50: 5F         LD           E,A
6A51: 3F         CCF
6A52: 2E 1F      LD           L,$1F
6A54: FF         RST         0X38
6A55: 00         NOP
6A56: BF         CP           A
6A57: 7F         LD           A,A
6A58: 9F         SBC         A
6A59: 7F         LD           A,A
6A5A: 40         LD           B,B
6A5B: 3F         CCF
6A5C: 30 0F      JR           NC,$6A6D
6A5E: 0F         RRCA
6A5F: 00         NOP
6A60: 1C         INC         E
6A61: 00         NOP
6A62: 3E 1C      LD           A,$1C
6A64: 37         SCF
6A65: 0E 1F      LD           C,$1F
6A67: 06 EF      LD           B,$EF
6A69: 10 AA      STOP       $AA
6A6B: D4 EA 34   CALL       NC,$34EA
6A6E: DE EC      SBC         $EC
6A70: BA         CP           D
6A71: DC FA 3C   CALL       C,$3CFA
6A74: F4                              
6A75: F8 E4      LDHL       SP,$E4
6A77: F8 88      LDHL       SP,$88
6A79: F0 10      LD           A,($10)
6A7B: E0 60      LDFF00   ($60),A
6A7D: 80         ADD         A,B
6A7E: 80         ADD         A,B
6A7F: 00         NOP
6A80: 7C         LD           A,H
6A81: 7C         LD           A,H
6A82: FE 82      CP           $82
6A84: 7E         LD           A,(HL)
6A85: 7A         LD           A,D
6A86: 1C         INC         E
6A87: 14         INC         D
6A88: 38 28      JR           C,$6AB2
6A8A: 7C         LD           A,H
6A8B: 5C         LD           E,H
6A8C: FE 82      CP           $82
6A8E: 7C         LD           A,H
6A8F: 7C         LD           A,H
6A90: 00         NOP
6A91: 00         NOP
6A92: 00         NOP
6A93: 00         NOP
6A94: 00         NOP
6A95: 00         NOP
6A96: 00         NOP
6A97: 00         NOP
6A98: 00         NOP
6A99: 00         NOP
6A9A: 00         NOP
6A9B: 00         NOP
6A9C: 00         NOP
6A9D: 00         NOP
6A9E: 00         NOP
6A9F: 00         NOP
6AA0: 00         NOP
6AA1: FF         RST         0X38
6AA2: 00         NOP
6AA3: FF         RST         0X38
6AA4: 24         INC         H
6AA5: FF         RST         0X38
6AA6: 18 FF      JR           $6AA7
6AA8: 18 FF      JR           $6AA9
6AAA: 24         INC         H
6AAB: FF         RST         0X38
6AAC: 00         NOP
6AAD: FF         RST         0X38
6AAE: 00         NOP
6AAF: FF         RST         0X38
6AB0: 00         NOP
6AB1: FF         RST         0X38
6AB2: 00         NOP
6AB3: FF         RST         0X38
6AB4: 24         INC         H
6AB5: FF         RST         0X38
6AB6: 18 FF      JR           $6AB7
6AB8: 18 FF      JR           $6AB9
6ABA: 24         INC         H
6ABB: FF         RST         0X38
6ABC: 00         NOP
6ABD: FF         RST         0X38
6ABE: 00         NOP
6ABF: FF         RST         0X38
6AC0: 00         NOP
6AC1: FF         RST         0X38
6AC2: 00         NOP
6AC3: FF         RST         0X38
6AC4: 24         INC         H
6AC5: FF         RST         0X38
6AC6: 18 FF      JR           $6AC7
6AC8: 18 FF      JR           $6AC9
6ACA: 24         INC         H
6ACB: FF         RST         0X38
6ACC: 00         NOP
6ACD: FF         RST         0X38
6ACE: 00         NOP
6ACF: FF         RST         0X38
6AD0: 00         NOP
6AD1: FF         RST         0X38
6AD2: 00         NOP
6AD3: FF         RST         0X38
6AD4: 24         INC         H
6AD5: FF         RST         0X38
6AD6: 18 FF      JR           $6AD7
6AD8: 18 FF      JR           $6AD9
6ADA: 24         INC         H
6ADB: FF         RST         0X38
6ADC: 00         NOP
6ADD: FF         RST         0X38
6ADE: 00         NOP
6ADF: FF         RST         0X38
6AE0: 00         NOP
6AE1: FF         RST         0X38
6AE2: 00         NOP
6AE3: FF         RST         0X38
6AE4: 24         INC         H
6AE5: FF         RST         0X38
6AE6: 18 FF      JR           $6AE7
6AE8: 18 FF      JR           $6AE9
6AEA: 24         INC         H
6AEB: FF         RST         0X38
6AEC: 00         NOP
6AED: FF         RST         0X38
6AEE: 00         NOP
6AEF: FF         RST         0X38
6AF0: 00         NOP
6AF1: FF         RST         0X38
6AF2: 00         NOP
6AF3: FF         RST         0X38
6AF4: 24         INC         H
6AF5: FF         RST         0X38
6AF6: 18 FF      JR           $6AF7
6AF8: 18 FF      JR           $6AF9
6AFA: 24         INC         H
6AFB: FF         RST         0X38
6AFC: 00         NOP
6AFD: FF         RST         0X38
6AFE: 00         NOP
6AFF: FF         RST         0X38
6B00: 03         INC         BC
6B01: 00         NOP
6B02: 05         DEC         B
6B03: 03         INC         BC
6B04: 05         DEC         B
6B05: 02         LD           (BC),A
6B06: 03         INC         BC
6B07: 00         NOP
6B08: 0C         INC         C
6B09: 03         INC         BC
6B0A: 11 0F 2F   LD           DE,$2F0F
6B0D: 15         DEC         D
6B0E: 5F         LD           E,A
6B0F: 2D         DEC         L
6B10: 7F         LD           A,A
6B11: 2D         DEC         L
6B12: BF         CP           A
6B13: 60         LD           H,B
6B14: B1         OR           C
6B15: 4E         LD           C,(HL)
6B16: ED                              
6B17: 12         LD           (DE),A
6B18: 8C         ADC         A,H
6B19: 73         LD           (HL),E
6B1A: E1         POP         HL
6B1B: 1E 6D      LD           E,$6D
6B1D: 12         LD           (DE),A
6B1E: 3F         CCF
6B1F: 00         NOP
6B20: 00         NOP
6B21: 00         NOP
6B22: 00         NOP
6B23: 00         NOP
6B24: 00         NOP
6B25: 00         NOP
6B26: 00         NOP
6B27: 00         NOP
6B28: C6 00      ADD         $00
6B2A: EE 44      XOR         $44
6B2C: FE 6C      CP           $6C
6B2E: 7C         LD           A,H
6B2F: 28 38      JR           Z,$6B69
6B31: 00         NOP
6B32: 00         NOP
6B33: 00         NOP
6B34: 00         NOP
6B35: 00         NOP
6B36: 00         NOP
6B37: 00         NOP
6B38: 00         NOP
6B39: 00         NOP
6B3A: 00         NOP
6B3B: 00         NOP
6B3C: 00         NOP
6B3D: 00         NOP
6B3E: 00         NOP
6B3F: 00         NOP
6B40: 73         LD           (HL),E
6B41: 00         NOP
6B42: FF         RST         0X38
6B43: 70         LD           (HL),B
6B44: FF         RST         0X38
6B45: 75         LD           (HL),L
6B46: FF         RST         0X38
6B47: 60         LD           H,B
6B48: FB         EI
6B49: 07         RLCA
6B4A: 98         SBC         B
6B4B: 67         LD           H,A
6B4C: 9F         SBC         A
6B4D: 60         LD           H,B
6B4E: 4F         LD           C,A
6B4F: 30 4F      JR           NC,$6BA0
6B51: 36 2B      LD           (HL),$2B
6B53: 16 15      LD           D,$15
6B55: 0B         DEC         BC
6B56: 1B         DEC         DE
6B57: 0C         INC         C
6B58: 27         DAA
6B59: 1F         RRA
6B5A: 78         LD           A,B
6B5B: 07         RLCA
6B5C: F7         RST         0X30
6B5D: 78         LD           A,B
6B5E: FF         RST         0X38
6B5F: 00         NOP
6B60: E0 00      LDFF00   ($00),A
6B62: F8 00      LDHL       SP,$00
6B64: FC                              
6B65: A0         AND         B
6B66: FC                              
6B67: A0         AND         B
6B68: 7E         LD           A,(HL)
6B69: F0 7E      LD           A,($7E)
6B6B: 94         SUB         H
6B6C: FE 1C      CP           $1C
6B6E: FA 3C FC   LD           A,($FC3C)
6B71: 78         LD           A,B
6B72: FA 74 B9   LD           A,($B974)
6B75: C6 FD      ADD         $FD
6B77: 1A         LD           A,(DE)
6B78: BE         CP           (HL)
6B79: D8         RET         C
6B7A: 1E E0      LD           E,$E0
6B7C: EF         RST         0X28
6B7D: 1E FF      LD           E,$FF
6B7F: 00         NOP
6B80: 30 00      JR           NC,$6B82
6B82: 48         LD           C,B
6B83: 30 48      JR           NC,$6BCD
6B85: 30 4C      JR           NC,$6BD3
6B87: 30 52      JR           NC,$6BDB
6B89: 2C         INC         L
6B8A: 52         LD           D,D
6B8B: 2C         INC         L
6B8C: 42         LD           B,D
6B8D: 3C         INC         A
6B8E: 44         LD           B,H
6B8F: 38 48      JR           C,$6BD9
6B91: 30 48      JR           NC,$6BDB
6B93: 30 48      JR           NC,$6BDD
6B95: 30 48      JR           NC,$6BDF
6B97: 30 48      JR           NC,$6BE1
6B99: 30 48      JR           NC,$6BE3
6B9B: 30 48      JR           NC,$6BE5
6B9D: 30 30      JR           NC,$6BCF
6B9F: 00         NOP
6BA0: 00         NOP
6BA1: 00         NOP
6BA2: 00         NOP
6BA3: 00         NOP
6BA4: 00         NOP
6BA5: 00         NOP
6BA6: 0C         INC         C
6BA7: 00         NOP
6BA8: 12         LD           (DE),A
6BA9: 0C         INC         C
6BAA: 11 0E 0C   LD           DE,$0C0E
6BAD: 03         INC         BC
6BAE: 12         LD           (DE),A
6BAF: 0D         DEC         C
6BB0: 10 0F      STOP       $0F
6BB2: 0F         RRCA
6BB3: 00         NOP
6BB4: 00         NOP
6BB5: 00         NOP
6BB6: 00         NOP
6BB7: 00         NOP
6BB8: 00         NOP
6BB9: 00         NOP
6BBA: 00         NOP
6BBB: 00         NOP
6BBC: 00         NOP
6BBD: 00         NOP
6BBE: 00         NOP
6BBF: 00         NOP
6BC0: 00         NOP
6BC1: 00         NOP
6BC2: 00         NOP
6BC3: 00         NOP
6BC4: 00         NOP
6BC5: 00         NOP
6BC6: 00         NOP
6BC7: 00         NOP
6BC8: 00         NOP
6BC9: 00         NOP
6BCA: 00         NOP
6BCB: 00         NOP
6BCC: 80         ADD         A,B
6BCD: 00         NOP
6BCE: 40         LD           B,B
6BCF: 80         ADD         A,B
6BD0: 20 C0      JR           NZ,$6B92
6BD2: 10 E0      STOP       $E0
6BD4: 88         ADC         A,B
6BD5: 70         LD           (HL),B
6BD6: 44         LD           B,H
6BD7: 38 22      JR           C,$6BFB
6BD9: 1C         INC         E
6BDA: 12         LD           (DE),A
6BDB: 0C         INC         C
6BDC: 0C         INC         C
6BDD: 00         NOP
6BDE: 00         NOP
6BDF: 00         NOP
6BE0: 00         NOP
6BE1: FF         RST         0X38
6BE2: 00         NOP
6BE3: FF         RST         0X38
6BE4: 24         INC         H
6BE5: FF         RST         0X38
6BE6: 18 FF      JR           $6BE7
6BE8: 18 FF      JR           $6BE9
6BEA: 24         INC         H
6BEB: FF         RST         0X38
6BEC: 00         NOP
6BED: FF         RST         0X38
6BEE: 00         NOP
6BEF: FF         RST         0X38
6BF0: 00         NOP
6BF1: FF         RST         0X38
6BF2: 00         NOP
6BF3: FF         RST         0X38
6BF4: 24         INC         H
6BF5: FF         RST         0X38
6BF6: 18 FF      JR           $6BF7
6BF8: 18 FF      JR           $6BF9
6BFA: 24         INC         H
6BFB: FF         RST         0X38
6BFC: 00         NOP
6BFD: FF         RST         0X38
6BFE: 00         NOP
6BFF: FF         RST         0X38
6C00: 15         DEC         D
6C01: 00         NOP
6C02: 1F         RRA
6C03: 00         NOP
6C04: 1F         RRA
6C05: 00         NOP
6C06: 3F         CCF
6C07: 07         RLCA
6C08: 7F         LD           A,A
6C09: 2D         DEC         L
6C0A: 7F         LD           A,A
6C0B: 28 5B      JR           Z,$6C68
6C0D: 37         SCF
6C0E: 38 17      JR           C,$6C27
6C10: 3F         CCF
6C11: 10 3F      STOP       $3F
6C13: 08 7F 27   LD           ($277F),SP
6C16: 77         LD           (HL),A
6C17: 28 33      JR           Z,$6C4C
6C19: 0F         RRCA
6C1A: 1E 01      LD           E,$01
6C1C: 3D         DEC         A
6C1D: 1E 1F      LD           E,$1F
6C1F: 00         NOP
6C20: E0 00      LDFF00   ($00),A
6C22: F8 00      LDHL       SP,$00
6C24: FC                              
6C25: 00         NOP
6C26: FC                              
6C27: E0 FE      LDFF00   ($FE),A
6C29: B4         OR           H
6C2A: FE B4      CP           $B4
6C2C: 3A         LD           A,(HLD)
6C2D: FC                              
6C2E: 3C         INC         A
6C2F: C8         RET         Z
6C30: FC                              
6C31: 18 FA      JR           $6C2D
6C33: 34         INC         (HL)
6C34: F2                              
6C35: CC FA 34   CALL       Z,$34FA
6C38: FC                              
6C39: B0         OR           B
6C3A: 38 C0      JR           C,$6BFC
6C3C: FC                              
6C3D: 00         NOP
6C3E: F0 00      LD           A,($00)
6C40: 07         RLCA
6C41: 00         NOP
6C42: 1F         RRA
6C43: 00         NOP
6C44: 3F         CCF
6C45: 00         NOP
6C46: 3F         CCF
6C47: 00         NOP
6C48: 7F         LD           A,A
6C49: 20 7F      JR           NZ,$6CCA
6C4B: 20 5F      JR           NZ,$6CAC
6C4D: 20 3F      JR           NZ,$6C8E
6C4F: 10 2F      STOP       $2F
6C51: 18 7F      JR           $6CD2
6C53: 2C         INC         L
6C54: 7F         LD           A,A
6C55: 23         INC         HL
6C56: 33         INC         SP
6C57: 0C         INC         C
6C58: 16 0F      LD           D,$0F
6C5A: 3F         CCF
6C5B: 01 3F 0E   LD           BC,$0E3F
6C5E: 1F         RRA
6C5F: 00         NOP
6C60: B0         OR           B
6C61: 00         NOP
6C62: F8 00      LDHL       SP,$00
6C64: FC                              
6C65: 00         NOP
6C66: FC                              
6C67: 00         NOP
6C68: FE 04      CP           $04
6C6A: FE 04      CP           $04
6C6C: FA 04 FC   LD           A,($FC04)
6C6F: 08 F4 18   LD           ($18F4),SP
6C72: E8 30      ADD         SP,$30
6C74: FC                              
6C75: C0         RET         NZ
6C76: CE 34      ADC         $34
6C78: 2E F4      LD           L,$F4
6C7A: DC E0 FC   CALL       C,$FCE0
6C7D: 00         NOP
6C7E: F8 00      LDHL       SP,$00
6C80: 2B         DEC         HL
6C81: 00         NOP
6C82: 3F         CCF
6C83: 00         NOP
6C84: 3F         CCF
6C85: 00         NOP
6C86: 1F         RRA
6C87: 0F         RRCA
6C88: 3F         CCF
6C89: 15         DEC         D
6C8A: 3F         CCF
6C8B: 05         DEC         B
6C8C: 5B         LD           E,E
6C8D: 3F         CCF
6C8E: 43         LD           B,E
6C8F: 3C         INC         A
6C90: 7F         LD           A,A
6C91: 00         NOP
6C92: 3F         CCF
6C93: 01 17 0F   LD           BC,$0F17
6C96: 0F         RRCA
6C97: 00         NOP
6C98: 11 0E 1F   LD           DE,$1F0E
6C9B: 00         NOP
6C9C: 0B         DEC         BC
6C9D: 07         RLCA
6C9E: 1F         RRA
6C9F: 00         NOP
6CA0: C0         RET         NZ
6CA1: 00         NOP
6CA2: F0 00      LD           A,($00)
6CA4: F8 00      LDHL       SP,$00
6CA6: FC                              
6CA7: 00         NOP
6CA8: FC                              
6CA9: D8         RET         C
6CAA: FC                              
6CAB: D8         RET         C
6CAC: F4                              
6CAD: F8 F8      LDHL       SP,$F8
6CAF: 70         LD           (HL),B
6CB0: F8 F0      LDHL       SP,$F0
6CB2: F8 E0      LDHL       SP,$E0
6CB4: E4                              
6CB5: 18 E4      JR           $6C9B
6CB7: D8         RET         C
6CB8: E4                              
6CB9: D8         RET         C
6CBA: F8 00      LDHL       SP,$00
6CBC: D0         RET         NC
6CBD: E0 F8      LDFF00   ($F8),A
6CBF: 00         NOP
6CC0: 00         NOP
6CC1: 00         NOP
6CC2: 2B         DEC         HL
6CC3: 00         NOP
6CC4: 3F         CCF
6CC5: 00         NOP
6CC6: 3F         CCF
6CC7: 00         NOP
6CC8: 1F         RRA
6CC9: 0F         RRCA
6CCA: 3F         CCF
6CCB: 15         DEC         D
6CCC: 3F         CCF
6CCD: 05         DEC         B
6CCE: 5B         LD           E,E
6CCF: 3F         CCF
6CD0: 43         LD           B,E
6CD1: 3C         INC         A
6CD2: 7F         LD           A,A
6CD3: 00         NOP
6CD4: 3F         CCF
6CD5: 00         NOP
6CD6: 17         RLA
6CD7: 0D         DEC         C
6CD8: 0F         RRCA
6CD9: 01 1F 00   LD           BC,$001F
6CDC: 3D         DEC         A
6CDD: 1E 3F      LD           E,$3F
6CDF: 00         NOP
6CE0: 00         NOP
6CE1: 00         NOP
6CE2: C0         RET         NZ
6CE3: 00         NOP
6CE4: F0 00      LD           A,($00)
6CE6: F8 00      LDHL       SP,$00
6CE8: FC                              
6CE9: 00         NOP
6CEA: FC                              
6CEB: D8         RET         C
6CEC: FC                              
6CED: D8         RET         C
6CEE: F4                              
6CEF: F8 F8      LDHL       SP,$F8
6CF1: 70         LD           (HL),B
6CF2: F8 E0      LDHL       SP,$E0
6CF4: E4                              
6CF5: 18 C4      JR           $6CBB
6CF7: B8         CP           B
6CF8: C4 B8 FE   CALL       NZ,$FEB8
6CFB: 04         INC         B
6CFC: FE 7C      CP           $7C
6CFE: FE 00      CP           $00
6D00: 07         RLCA
6D01: 00         NOP
6D02: 0F         RRCA
6D03: 00         NOP
6D04: 0F         RRCA
6D05: 06 1F      LD           B,$1F
6D07: 0E 1F      LD           C,$1F
6D09: 0C         INC         C
6D0A: 1D         DEC         E
6D0B: 02         LD           (BC),A
6D0C: 1F         RRA
6D0D: 03         INC         BC
6D0E: 1F         RRA
6D0F: 03         INC         BC
6D10: 1F         RRA
6D11: 03         INC         BC
6D12: 1F         RRA
6D13: 02         LD           (BC),A
6D14: 1F         RRA
6D15: 03         INC         BC
6D16: 3F         CCF
6D17: 01 7F 30   LD           BC,$307F
6D1A: 5C         LD           E,H
6D1B: 3B         DEC         SP
6D1C: 6F         LD           L,A
6D1D: 18 3C      JR           $6D5B
6D1F: 00         NOP
6D20: BC         CP           H
6D21: 00         NOP
6D22: FE 00      CP           $00
6D24: FE 60      CP           $60
6D26: FE E0      CP           $E0
6D28: F8 A0      LDHL       SP,$A0
6D2A: FC                              
6D2B: A0         AND         B
6D2C: FE EC      CP           $EC
6D2E: FE FC      CP           $FC
6D30: FC                              
6D31: F8 FE      LDHL       SP,$FE
6D33: 60         LD           H,B
6D34: FF         RST         0X38
6D35: C6 FF      ADD         $FF
6D37: 82         ADD         A,D
6D38: FE 0C      CP           $0C
6D3A: 3A         LD           A,(HLD)
6D3B: DC F6 18   CALL       C,$18F6
6D3E: 3C         INC         A
6D3F: 00         NOP
6D40: 07         RLCA
6D41: 00         NOP
6D42: 0F         RRCA
6D43: 00         NOP
6D44: CF         RST         0X08
6D45: 03         INC         BC
6D46: E7         RST         0X20
6D47: 43         LD           B,E
6D48: F7         RST         0X30
6D49: 62         LD           H,D
6D4A: FF         RST         0X38
6D4B: 62         LD           H,D
6D4C: 7F         LD           A,A
6D4D: 0B         DEC         BC
6D4E: 7F         LD           A,A
6D4F: 0E 3F      LD           C,$3F
6D51: 06 1F      LD           B,$1F
6D53: 02         LD           (BC),A
6D54: 1F         RRA
6D55: 02         LD           (BC),A
6D56: 3F         CCF
6D57: 01 7F 30   LD           BC,$307F
6D5A: 5C         LD           E,H
6D5B: 3B         DEC         SP
6D5C: 6F         LD           L,A
6D5D: 18 3C      JR           $6D9B
6D5F: 00         NOP
6D60: BC         CP           H
6D61: 00         NOP
6D62: FE 00      CP           $00
6D64: FE 60      CP           $60
6D66: FE E0      CP           $E0
6D68: F8 A0      LDHL       SP,$A0
6D6A: FC                              
6D6B: A0         AND         B
6D6C: FE EC      CP           $EC
6D6E: FE FC      CP           $FC
6D70: FC                              
6D71: 78         LD           A,B
6D72: FE 60      CP           $60
6D74: F7         RST         0X30
6D75: 4E         LD           C,(HL)
6D76: FF         RST         0X38
6D77: 82         ADD         A,D
6D78: FE 0C      CP           $0C
6D7A: 3A         LD           A,(HLD)
6D7B: DC F6 18   CALL       C,$18F6
6D7E: 3C         INC         A
6D7F: 00         NOP
6D80: 0E 00      LD           C,$00
6D82: 1F         RRA
6D83: 00         NOP
6D84: 3F         CCF
6D85: 00         NOP
6D86: 3F         CCF
6D87: 00         NOP
6D88: 1F         RRA
6D89: 0D         DEC         C
6D8A: 3F         CCF
6D8B: 0F         RRCA
6D8C: 3F         CCF
6D8D: 1A         LD           A,(DE)
6D8E: 3F         CCF
6D8F: 1A         LD           A,(DE)
6D90: 1F         RRA
6D91: 08 3E 07   LD           ($073E),SP
6D94: 7C         LD           A,H
6D95: 37         SCF
6D96: 7E         LD           A,(HL)
6D97: 2F         CPL
6D98: 78         LD           A,B
6D99: 0F         RRCA
6D9A: 5D         LD           E,L
6D9B: 2E 6F      LD           L,$6F
6D9D: 10 38      STOP       $38
6D9F: 00         NOP
6DA0: F0 00      LD           A,($00)
6DA2: F8 00      LDHL       SP,$00
6DA4: F8 00      LDHL       SP,$00
6DA6: F8 00      LDHL       SP,$00
6DA8: E0 80      LDFF00   ($80),A
6DAA: F0 80      LD           A,($80)
6DAC: F8 B0      LDHL       SP,$B0
6DAE: F8 F0      LDHL       SP,$F0
6DB0: F0 C0      LD           A,($C0)
6DB2: F8 40      LDHL       SP,$40
6DB4: F8 00      LDHL       SP,$00
6DB6: FC                              
6DB7: 60         LD           H,B
6DB8: FE 6C      CP           $6C
6DBA: 7A         LD           A,D
6DBB: 9C         SBC         H
6DBC: F6 18      OR           $18
6DBE: 3C         INC         A
6DBF: 00         NOP
6DC0: 07         RLCA
6DC1: 00         NOP
6DC2: 0F         RRCA
6DC3: 00         NOP
6DC4: 0F         RRCA
6DC5: 03         INC         BC
6DC6: 07         RLCA
6DC7: 03         INC         BC
6DC8: 07         RLCA
6DC9: 02         LD           (BC),A
6DCA: 0F         RRCA
6DCB: 02         LD           (BC),A
6DCC: 1F         RRA
6DCD: 0B         DEC         BC
6DCE: 1F         RRA
6DCF: 0E 0F      LD           C,$0F
6DD1: 04         INC         B
6DD2: 0F         RRCA
6DD3: 00         NOP
6DD4: 7D         LD           A,L
6DD5: 0E F9      LD           C,$F9
6DD7: 6E         LD           L,(HL)
6DD8: FD                              
6DD9: 5E         LD           E,(HL)
6DDA: F1         POP         AF
6DDB: 1E 7B      LD           E,$7B
6DDD: 1C         INC         E
6DDE: 3E 00      LD           A,$00
6DE0: 03         INC         BC
6DE1: 00         NOP
6DE2: 07         RLCA
6DE3: 03         INC         BC
6DE4: 0E 05      LD           C,$05
6DE6: 0F         RRCA
6DE7: 04         INC         B
6DE8: 07         RLCA
6DE9: 03         INC         BC
6DEA: 0F         RRCA
6DEB: 00         NOP
6DEC: 17         RLA
6DED: 0D         DEC         C
6DEE: 2B         DEC         HL
6DEF: 1C         INC         E
6DF0: 2D         DEC         L
6DF1: 1B         DEC         DE
6DF2: 41         LD           B,C
6DF3: 3F         CCF
6DF4: 41         LD           B,C
6DF5: 3F         CCF
6DF6: 40         LD           B,B
6DF7: 3F         CCF
6DF8: 48         LD           C,B
6DF9: 37         SCF
6DFA: 28 17      JR           Z,$6E13
6DFC: 1C         INC         E
6DFD: 03         INC         BC
6DFE: 07         RLCA
6DFF: 00         NOP
6E00: 00         NOP
6E01: 00         NOP
6E02: 00         NOP
6E03: 00         NOP
6E04: 00         NOP
6E05: 00         NOP
6E06: 00         NOP
6E07: 00         NOP
6E08: 00         NOP
6E09: 00         NOP
6E0A: 01 00 02   LD           BC,$0200
6E0D: 01 03 00   LD           BC,$0003
6E10: 0D         DEC         C
6E11: 03         INC         BC
6E12: 1F         RRA
6E13: 0F         RRCA
6E14: 3C         INC         A
6E15: 1F         RRA
6E16: 50         LD           D,B
6E17: 3F         CCF
6E18: 4C         LD           C,H
6E19: 33         INC         SP
6E1A: C8         RET         Z
6E1B: 37         SCF
6E1C: 82         ADD         A,D
6E1D: 7D         LD           A,L
6E1E: 81         ADD         A,C
6E1F: 7E         LD           A,(HL)
6E20: 00         NOP
6E21: 00         NOP
6E22: 00         NOP
6E23: 00         NOP
6E24: 1F         RRA
6E25: 00         NOP
6E26: 6F         LD           L,A
6E27: 1F         RRA
6E28: BF         CP           A
6E29: 7F         LD           A,A
6E2A: 63         LD           H,E
6E2B: FF         RST         0X38
6E2C: 01 FF F0   LD           BC,$F0FF
6E2F: 0F         RRCA
6E30: C8         RET         Z
6E31: F7         RST         0X30
6E32: 00         NOP
6E33: FF         RST         0X38
6E34: 30 CF      JR           NC,$6E05
6E36: 40         LD           B,B
6E37: BF         CP           A
6E38: 40         LD           B,B
6E39: BF         CP           A
6E3A: 70         LD           (HL),B
6E3B: 8F         ADC         A,A
6E3C: 38 FF      JR           C,$6E3D
6E3E: 0C         INC         C
6E3F: FF         RST         0X38
6E40: 00         NOP
6E41: 00         NOP
6E42: 00         NOP
6E43: 00         NOP
6E44: F0 00      LD           A,($00)
6E46: EC                              
6E47: F0 FA      LD           A,($FA)
6E49: FC                              
6E4A: 6D         LD           L,L
6E4B: FE 26      CP           $26
6E4D: FF         RST         0X38
6E4E: 03         INC         BC
6E4F: FF         RST         0X38
6E50: 01 FF 00   LD           BC,$00FF
6E53: FF         RST         0X38
6E54: 00         NOP
6E55: FF         RST         0X38
6E56: 00         NOP
6E57: FF         RST         0X38
6E58: 00         NOP
6E59: FF         RST         0X38
6E5A: 00         NOP
6E5B: FF         RST         0X38
6E5C: 00         NOP
6E5D: FF         RST         0X38
6E5E: 00         NOP
6E5F: FF         RST         0X38
6E60: 00         NOP
6E61: 00         NOP
6E62: 00         NOP
6E63: 00         NOP
6E64: 00         NOP
6E65: 00         NOP
6E66: 00         NOP
6E67: 00         NOP
6E68: 00         NOP
6E69: 00         NOP
6E6A: 00         NOP
6E6B: 00         NOP
6E6C: 80         ADD         A,B
6E6D: 00         NOP
6E6E: 80         ADD         A,B
6E6F: 00         NOP
6E70: 40         LD           B,B
6E71: 80         ADD         A,B
6E72: 40         LD           B,B
6E73: 80         ADD         A,B
6E74: 20 C0      JR           NZ,$6E36
6E76: 20 C0      JR           NZ,$6E38
6E78: 20 C0      JR           NZ,$6E3A
6E7A: 10 E0      STOP       $E0
6E7C: 1C         INC         E
6E7D: E0 12      LDFF00   ($12),A
6E7F: EC                              
6E80: A1         AND         C
6E81: 5E         LD           E,(HL)
6E82: E3                              
6E83: 1C         INC         E
6E84: FD                              
6E85: 42         LD           B,D
6E86: FD                              
6E87: 6E         LD           L,(HL)
6E88: FD                              
6E89: 6E         LD           L,(HL)
6E8A: B7         OR           A
6E8B: 6E         LD           L,(HL)
6E8C: 7F         LD           A,A
6E8D: 26 5B      LD           H,$5B
6E8F: 26 3F      LD           H,$3F
6E91: 02         LD           (BC),A
6E92: 16 09      LD           D,$09
6E94: 3B         DEC         SP
6E95: 1C         INC         E
6E96: 70         LD           (HL),B
6E97: 3F         CCF
6E98: 7F         LD           A,A
6E99: 00         NOP
6E9A: 00         NOP
6E9B: 00         NOP
6E9C: 00         NOP
6E9D: 00         NOP
6E9E: 00         NOP
6E9F: 00         NOP
6EA0: 00         NOP
6EA1: FF         RST         0X38
6EA2: 00         NOP
6EA3: FF         RST         0X38
6EA4: 00         NOP
6EA5: FF         RST         0X38
6EA6: 03         INC         BC
6EA7: FC                              
6EA8: 05         DEC         B
6EA9: FB         EI
6EAA: 07         RLCA
6EAB: FB         EI
6EAC: 02         LD           (BC),A
6EAD: FF         RST         0X38
6EAE: 00         NOP
6EAF: FF         RST         0X38
6EB0: 01 FE 09   LD           BC,$09FE
6EB3: F6 09      OR           $09
6EB5: F6 FC      OR           $FC
6EB7: 03         INC         BC
6EB8: FF         RST         0X38
6EB9: 00         NOP
6EBA: 00         NOP
6EBB: 00         NOP
6EBC: 00         NOP
6EBD: 00         NOP
6EBE: 00         NOP
6EBF: 00         NOP
6EC0: 00         NOP
6EC1: FF         RST         0X38
6EC2: 00         NOP
6EC3: FF         RST         0X38
6EC4: 00         NOP
6EC5: FF         RST         0X38
6EC6: 80         ADD         A,B
6EC7: 7F         LD           A,A
6EC8: C0         RET         NZ
6EC9: FF         RST         0X38
6ECA: 00         NOP
6ECB: FF         RST         0X38
6ECC: 30 CF      JR           NC,$6E9D
6ECE: 0C         INC         C
6ECF: F3         DI
6ED0: 32         LD           (HLD),A
6ED1: FD                              
6ED2: 3D         DEC         A
6ED3: FE 1F      CP           $1F
6ED5: FF         RST         0X38
6ED6: 87         ADD         A,A
6ED7: 7F         LD           A,A
6ED8: C0         RET         NZ
6ED9: 3F         CCF
6EDA: 3F         CCF
6EDB: 00         NOP
6EDC: 00         NOP
6EDD: 00         NOP
6EDE: 00         NOP
6EDF: 00         NOP
6EE0: 12         LD           (DE),A
6EE1: EC                              
6EE2: 04         INC         B
6EE3: F8 0A      LDHL       SP,$0A
6EE5: FC                              
6EE6: 0D         DEC         C
6EE7: FE 05      CP           $05
6EE9: FE 01      CP           $01
6EEB: FE 11      CP           $11
6EED: EE 11      XOR         $11
6EEF: EE 39      XOR         $39
6EF1: C6 C6      ADD         $C6
6EF3: 00         NOP
6EF4: 80         ADD         A,B
6EF5: 00         NOP
6EF6: 40         LD           B,B
6EF7: 80         ADD         A,B
6EF8: 40         LD           B,B
6EF9: 80         ADD         A,B
6EFA: C0         RET         NZ
6EFB: 00         NOP
6EFC: 00         NOP
6EFD: 00         NOP
6EFE: 00         NOP
6EFF: 00         NOP
6F00: 00         NOP
6F01: 00         NOP
6F02: 00         NOP
6F03: 00         NOP
6F04: 1F         RRA
6F05: 00         NOP
6F06: 6F         LD           L,A
6F07: 1F         RRA
6F08: BF         CP           A
6F09: 7F         LD           A,A
6F0A: 63         LD           H,E
6F0B: FF         RST         0X38
6F0C: 01 FF F0   LD           BC,$F0FF
6F0F: 0F         RRCA
6F10: C8         RET         Z
6F11: F7         RST         0X30
6F12: 20 DF      JR           NZ,$6EF3
6F14: 70         LD           (HL),B
6F15: 8F         ADC         A,A
6F16: 78         LD           A,B
6F17: B7         OR           A
6F18: 78         LD           A,B
6F19: 97         SUB         A
6F1A: 28 D7      JR           Z,$6EF3
6F1C: 38 FF      JR           C,$6F1D
6F1E: 0C         INC         C
6F1F: FF         RST         0X38
6F20: 03         INC         BC
6F21: 00         NOP
6F22: 0D         DEC         C
6F23: 03         INC         BC
6F24: 1F         RRA
6F25: 0F         RRCA
6F26: 3C         INC         A
6F27: 1F         RRA
6F28: 50         LD           D,B
6F29: 3F         CCF
6F2A: 4C         LD           C,H
6F2B: 33         INC         SP
6F2C: C8         RET         Z
6F2D: 37         SCF
6F2E: 82         ADD         A,D
6F2F: 7D         LD           A,L
6F30: 81         ADD         A,C
6F31: 7E         LD           A,(HL)
6F32: A1         AND         C
6F33: 5E         LD           E,(HL)
6F34: E3                              
6F35: 1C         INC         E
6F36: FD                              
6F37: 42         LD           B,D
6F38: FD                              
6F39: 6E         LD           L,(HL)
6F3A: FD                              
6F3B: 6E         LD           L,(HL)
6F3C: B7         OR           A
6F3D: 6E         LD           L,(HL)
6F3E: 7F         LD           A,A
6F3F: 26 F0      LD           H,$F0
6F41: 00         NOP
6F42: CC F0 23   CALL       Z,$23F0
6F45: DC 71 8E   CALL       C,$8E71
6F48: 78         LD           A,B
6F49: B7         OR           A
6F4A: 78         LD           A,B
6F4B: 97         SUB         A
6F4C: 28 D7      JR           Z,$6F25
6F4E: 38 FF      JR           C,$6F4F
6F50: 0C         INC         C
6F51: FF         RST         0X38
6F52: 00         NOP
6F53: FF         RST         0X38
6F54: 00         NOP
6F55: FF         RST         0X38
6F56: 00         NOP
6F57: FF         RST         0X38
6F58: 00         NOP
6F59: FF         RST         0X38
6F5A: 00         NOP
6F5B: FF         RST         0X38
6F5C: 00         NOP
6F5D: FF         RST         0X38
6F5E: 00         NOP
6F5F: FF         RST         0X38
6F60: 5B         LD           E,E
6F61: 26 35      LD           H,$35
6F63: 0A         LD           A,(BC)
6F64: 13         INC         DE
6F65: 0C         INC         C
6F66: 10 0F      STOP       $0F
6F68: 08 07 08   LD           ($0807),SP
6F6B: 07         RLCA
6F6C: 04         INC         B
6F6D: 03         INC         BC
6F6E: 04         INC         B
6F6F: 03         INC         BC
6F70: 0E 01      LD           C,$01
6F72: 12         LD           (DE),A
6F73: 0D         DEC         C
6F74: 39         ADD         HL,SP
6F75: 1E 70      LD           E,$70
6F77: 3F         CCF
6F78: 7F         LD           A,A
6F79: 00         NOP
6F7A: 00         NOP
6F7B: 00         NOP
6F7C: 00         NOP
6F7D: 00         NOP
6F7E: 00         NOP
6F7F: 00         NOP
6F80: 00         NOP
6F81: 00         NOP
6F82: 00         NOP
6F83: 00         NOP
6F84: 00         NOP
6F85: 00         NOP
6F86: 00         NOP
6F87: 00         NOP
6F88: 00         NOP
6F89: 00         NOP
6F8A: 00         NOP
6F8B: 00         NOP
6F8C: 00         NOP
6F8D: 00         NOP
6F8E: 01 00 02   LD           BC,$0200
6F91: 01 04 03   LD           BC,$0304
6F94: 0E 01      LD           C,$01
6F96: 38 07      JR           C,$6F9F
6F98: 78         LD           A,B
6F99: 37         SCF
6F9A: F1         POP         AF
6F9B: 6E         LD           L,(HL)
6F9C: 93         SUB         E
6F9D: 6C         LD           L,H
6F9E: 78         LD           A,B
6F9F: 07         RLCA
6FA0: 01 00 06   LD           BC,$0600
6FA3: 01 08 07   LD           BC,$0708
6FA6: 13         INC         DE
6FA7: 0F         RRCA
6FA8: 18 07      JR           $6FB1
6FAA: 60         LD           H,B
6FAB: 1F         RRA
6FAC: 80         ADD         A,B
6FAD: 7F         LD           A,A
6FAE: E0 1F      LDFF00   ($1F),A
6FB0: 00         NOP
6FB1: FF         RST         0X38
6FB2: 00         NOP
6FB3: FF         RST         0X38
6FB4: 60         LD           H,B
6FB5: FF         RST         0X38
6FB6: D4 EB 3C   CALL       NC,$3CEB
6FB9: DB                              
6FBA: 7C         LD           A,H
6FBB: 8B         ADC         A,E
6FBC: 39         ADD         HL,SP
6FBD: C7         RST         0X00
6FBE: 03         INC         BC
6FBF: FF         RST         0X38
6FC0: F8 00      LDHL       SP,$00
6FC2: E4                              
6FC3: F8 08      LDHL       SP,$08
6FC5: F0 90      LD           A,($90)
6FC7: 60         LD           H,B
6FC8: 78         LD           A,B
6FC9: 80         ADD         A,B
6FCA: 06 F8      LD           B,$F8
6FCC: 01 FE 00   LD           BC,$00FE
6FCF: FF         RST         0X38
6FD0: 00         NOP
6FD1: FF         RST         0X38
6FD2: 00         NOP
6FD3: FF         RST         0X38
6FD4: 00         NOP
6FD5: FF         RST         0X38
6FD6: 40         LD           B,B
6FD7: BF         CP           A
6FD8: 29         ADD         HL,HL
6FD9: DF         RST         0X18
6FDA: 2D         DEC         L
6FDB: DF         RST         0X18
6FDC: 97         SUB         A
6FDD: EF         RST         0X28
6FDE: D7         RST         0X10
6FDF: EF         RST         0X28
6FE0: 00         NOP
6FE1: 00         NOP
6FE2: 00         NOP
6FE3: 00         NOP
6FE4: 00         NOP
6FE5: 00         NOP
6FE6: 00         NOP
6FE7: 00         NOP
6FE8: 00         NOP
6FE9: 00         NOP
6FEA: 00         NOP
6FEB: 00         NOP
6FEC: 80         ADD         A,B
6FED: 00         NOP
6FEE: 40         LD           B,B
6FEF: 80         ADD         A,B
6FF0: 20 C0      JR           NZ,$6FB2
6FF2: 10 E0      STOP       $E0
6FF4: 17         RLA
6FF5: E0 09      LDFF00   ($09),A
6FF7: F6 09      OR           $09
6FF9: F6 21      OR           $21
6FFB: FE A1      CP           $A1
6FFD: FE F2      CP           $F2
6FFF: FC                              
7000: 00         NOP
7001: 00         NOP
7002: 00         NOP
7003: 00         NOP
7004: 00         NOP
7005: 00         NOP
7006: 00         NOP
7007: 00         NOP
7008: 00         NOP
7009: 00         NOP
700A: 00         NOP
700B: 00         NOP
700C: 00         NOP
700D: 00         NOP
700E: 00         NOP
700F: 00         NOP
7010: 00         NOP
7011: 00         NOP
7012: 00         NOP
7013: 00         NOP
7014: 00         NOP
7015: 00         NOP
7016: 00         NOP
7017: 00         NOP
7018: 03         INC         BC
7019: 00         NOP
701A: 0D         DEC         C
701B: 03         INC         BC
701C: 1F         RRA
701D: 0F         RRCA
701E: 3C         INC         A
701F: 1F         RRA
7020: 00         NOP
7021: 00         NOP
7022: 00         NOP
7023: 00         NOP
7024: 00         NOP
7025: 00         NOP
7026: 00         NOP
7027: 00         NOP
7028: 00         NOP
7029: 00         NOP
702A: 00         NOP
702B: 00         NOP
702C: 00         NOP
702D: 00         NOP
702E: 00         NOP
702F: 00         NOP
7030: 00         NOP
7031: 00         NOP
7032: 00         NOP
7033: 00         NOP
7034: 00         NOP
7035: 00         NOP
7036: 00         NOP
7037: 00         NOP
7038: F0 00      LD           A,($00)
703A: CC F0 22   CALL       Z,$22F0
703D: DC 73 8E   CALL       C,$8E73
7040: 50         LD           D,B
7041: 3F         CCF
7042: 4C         LD           C,H
7043: 33         INC         SP
7044: C8         RET         Z
7045: 37         SCF
7046: 82         ADD         A,D
7047: 7D         LD           A,L
7048: 81         ADD         A,C
7049: 7E         LD           A,(HL)
704A: A1         AND         C
704B: 5E         LD           E,(HL)
704C: E3                              
704D: 1C         INC         E
704E: FD                              
704F: 42         LD           B,D
7050: FD                              
7051: 6E         LD           L,(HL)
7052: FD                              
7053: 6E         LD           L,(HL)
7054: B7         OR           A
7055: 6E         LD           L,(HL)
7056: FF         RST         0X38
7057: A6         AND         (HL)
7058: DB                              
7059: A6         AND         (HL)
705A: FF         RST         0X38
705B: C2 7F 78   JP           NZ,$787F
705E: 1F         RRA
705F: 1F         RRA
7060: 79         LD           A,C
7061: B7         OR           A
7062: 78         LD           A,B
7063: 97         SUB         A
7064: 28 D7      JR           Z,$703D
7066: 38 FF      JR           C,$7067
7068: 0C         INC         C
7069: FF         RST         0X38
706A: 00         NOP
706B: FF         RST         0X38
706C: 00         NOP
706D: FF         RST         0X38
706E: 00         NOP
706F: FF         RST         0X38
7070: 00         NOP
7071: FF         RST         0X38
7072: 00         NOP
7073: FF         RST         0X38
7074: 00         NOP
7075: FF         RST         0X38
7076: 00         NOP
7077: FF         RST         0X38
7078: 00         NOP
7079: FF         RST         0X38
707A: 00         NOP
707B: FF         RST         0X38
707C: FF         RST         0X38
707D: 00         NOP
707E: FF         RST         0X38
707F: FF         RST         0X38
7080: 80         ADD         A,B
7081: 00         NOP
7082: C0         RET         NZ
7083: 80         ADD         A,B
7084: A0         AND         B
7085: C0         RET         NZ
7086: 10 E0      STOP       $E0
7088: 10 E0      STOP       $E0
708A: 08 F0 08   LD           ($08F0),SP
708D: F0 04      LD           A,($04)
708F: F8 04      LDHL       SP,$04
7091: F8 04      LDHL       SP,$04
7093: F8 02      LDHL       SP,$02
7095: FC                              
7096: 03         INC         BC
7097: FD                              
7098: 03         INC         BC
7099: FD                              
709A: 0F         RRCA
709B: F3         DI
709C: FE 0E      CP           $0E
709E: FC                              
709F: FC                              
70A0: 01 00 06   LD           BC,$0600
70A3: 01 0F 07   LD           BC,$070F
70A6: 1E 0F      LD           E,$0F
70A8: 28 1F      JR           Z,$70C9
70AA: 26 19      LD           H,$19
70AC: 64         LD           H,H
70AD: 1B         DEC         DE
70AE: 41         LD           B,C
70AF: 3E 40      LD           A,$40
70B1: 3F         CCF
70B2: D0         RET         NC
70B3: AF         XOR         A
70B4: F1         POP         AF
70B5: 8E         ADC         A,(HL)
70B6: FE A1      CP           $A1
70B8: FE B7      CP           $B7
70BA: FE 87      CP           $87
70BC: 7F         LD           A,A
70BD: 70         LD           (HL),B
70BE: 1F         RRA
70BF: 1F         RRA
70C0: F8 00      LDHL       SP,$00
70C2: E6 F8      AND         $F8
70C4: 93         SUB         E
70C5: EE 39      XOR         $39
70C7: C7         RST         0X00
70C8: 3C         INC         A
70C9: DB                              
70CA: 3C         INC         A
70CB: CB 14      RL          1,E
70CD: EB                              
70CE: 1C         INC         E
70CF: FF         RST         0X38
70D0: 86         ADD         A,(HL)
70D1: 7F         LD           A,A
70D2: 80         ADD         A,B
70D3: 7F         LD           A,A
70D4: 80         ADD         A,B
70D5: 7F         LD           A,A
70D6: 80         ADD         A,B
70D7: 7F         LD           A,A
70D8: 80         ADD         A,B
70D9: 7F         LD           A,A
70DA: 80         ADD         A,B
70DB: 7F         LD           A,A
70DC: FF         RST         0X38
70DD: 00         NOP
70DE: FF         RST         0X38
70DF: FF         RST         0X38
70E0: 00         NOP
70E1: 00         NOP
70E2: 00         NOP
70E3: 00         NOP
70E4: 80         ADD         A,B
70E5: 00         NOP
70E6: 40         LD           B,B
70E7: 80         ADD         A,B
70E8: A0         AND         B
70E9: C0         RET         NZ
70EA: 10 E0      STOP       $E0
70EC: 10 E0      STOP       $E0
70EE: 08 F0 08   LD           ($08F0),SP
70F1: F0 06      LD           A,($06)
70F3: FA 06 FA   LD           A,($FA06)
70F6: 06 FA      LD           B,$FA
70F8: 06 FA      LD           B,$FA
70FA: 1E E6      LD           E,$E6
70FC: FC                              
70FD: 1C         INC         E
70FE: F8 F8      LDHL       SP,$F8
7100: 00         NOP
7101: 00         NOP
7102: 00         NOP
7103: 00         NOP
7104: 00         NOP
7105: 00         NOP
7106: 0F         RRCA
7107: 00         NOP
7108: 1F         RRA
7109: 00         NOP
710A: 3F         CCF
710B: 02         LD           (BC),A
710C: 3F         CCF
710D: 06 3F      LD           B,$3F
710F: 06 1F      LD           B,$1F
7111: 07         RLCA
7112: 3F         CCF
7113: 0B         DEC         BC
7114: 7C         LD           A,H
7115: 0B         DEC         BC
7116: 77         LD           (HL),A
7117: 0F         RRCA
7118: 7B         LD           A,E
7119: 07         RLCA
711A: 1F         RRA
711B: 00         NOP
711C: 00         NOP
711D: 00         NOP
711E: 00         NOP
711F: 00         NOP
7120: 38 00      JR           C,$7122
7122: 76         HALT
7123: 38 EF      JR           C,$7114
7125: 16 DA      LD           D,$DA
7127: 6C         LD           L,H
7128: FD                              
7129: 62         LD           H,D
712A: F7         RST         0X30
712B: 5A         LD           E,D
712C: FE 18      CP           $18
712E: FC                              
712F: 00         NOP
7130: F8 80      LDHL       SP,$80
7132: FC                              
7133: 50         LD           D,B
7134: EE 70      XOR         $70
7136: BE         CP           (HL)
7137: C0         RET         NZ
7138: 7E         LD           A,(HL)
7139: 80         ADD         A,B
713A: F8 00      LDHL       SP,$00
713C: 00         NOP
713D: 00         NOP
713E: 00         NOP
713F: 00         NOP
7140: 00         NOP
7141: 00         NOP
7142: 00         NOP
7143: 00         NOP
7144: 00         NOP
7145: 00         NOP
7146: C0         RET         NZ
7147: 80         ADD         A,B
7148: F8 C0      LDHL       SP,$C0
714A: 7F         LD           A,A
714B: F8 1F      LDHL       SP,$1F
714D: 7F         LD           A,A
714E: 00         NOP
714F: 1F         RRA
7150: 00         NOP
7151: 00         NOP
7152: 00         NOP
7153: 00         NOP
7154: 00         NOP
7155: 00         NOP
7156: 00         NOP
7157: 00         NOP
7158: 00         NOP
7159: 00         NOP
715A: 00         NOP
715B: 00         NOP
715C: 00         NOP
715D: 00         NOP
715E: 00         NOP
715F: 00         NOP
7160: 0F         RRCA
7161: 00         NOP
7162: 13         INC         DE
7163: 0F         RRCA
7164: 09         ADD         HL,BC
7165: 07         RLCA
7166: 09         ADD         HL,BC
7167: 07         RLCA
7168: 05         DEC         B
7169: 03         INC         BC
716A: 04         INC         B
716B: 03         INC         BC
716C: 02         LD           (BC),A
716D: 01 06 03   LD           BC,$0306
7170: 0E 07      LD           C,$07
7172: 15         DEC         D
7173: 0E 11      LD           C,$11
7175: 0E 21      LD           C,$21
7177: 1E 21      LD           E,$21
7179: 1E 60      LD           E,$60
717B: 5F         LD           E,A
717C: 70         LD           (HL),B
717D: 6F         LD           L,A
717E: 3F         CCF
717F: 3F         CCF
7180: 00         NOP
7181: 00         NOP
7182: 80         ADD         A,B
7183: 00         NOP
7184: C0         RET         NZ
7185: 80         ADD         A,B
7186: C0         RET         NZ
7187: 80         ADD         A,B
7188: F8 80      LDHL       SP,$80
718A: FC                              
718B: F8 7E      LDHL       SP,$7E
718D: FC                              
718E: 0E FC      LD           C,$FC
7190: C1         POP         BC
7191: 3E 3F      LD           A,$3F
7193: 00         NOP
7194: 00         NOP
7195: 00         NOP
7196: 00         NOP
7197: 00         NOP
7198: 00         NOP
7199: 00         NOP
719A: C0         RET         NZ
719B: 40         LD           B,B
719C: C0         RET         NZ
719D: 40         LD           B,B
719E: 80         ADD         A,B
719F: 80         ADD         A,B
71A0: 2F         CPL
71A1: 00         NOP
71A2: 7F         LD           A,A
71A3: 00         NOP
71A4: 7F         LD           A,A
71A5: 00         NOP
71A6: FF         RST         0X38
71A7: 00         NOP
71A8: FF         RST         0X38
71A9: 00         NOP
71AA: FF         RST         0X38
71AB: 00         NOP
71AC: FF         RST         0X38
71AD: 07         RLCA
71AE: 7F         LD           A,A
71AF: 0F         RRCA
71B0: 7F         LD           A,A
71B1: 1F         RRA
71B2: 3F         CCF
71B3: 1B         DEC         DE
71B4: 1F         RRA
71B5: 0B         DEC         BC
71B6: 17         RLA
71B7: 0F         RRCA
71B8: 1B         DEC         DE
71B9: 07         RLCA
71BA: 1F         RRA
71BB: 08 1E 0C   LD           ($0C1E),SP
71BE: 0E 00      LD           C,$00
71C0: DC 00 FF   CALL       C,$FF00
71C3: D8         RET         C
71C4: FF         RST         0X38
71C5: 10 FF      STOP       $FF
71C7: 6C         LD           L,H
71C8: FF         RST         0X38
71C9: 34         INC         (HL)
71CA: FE 01      CP           $01
71CC: FB         EI
71CD: 06 FD      LD           B,$FD
71CF: 86         ADD         A,(HL)
71D0: FF         RST         0X38
71D1: D4 FA 74   CALL       NC,$74FA
71D4: DC 68 BD   CALL       C,$BD68
71D7: D8         RET         C
71D8: 75         LD           (HL),L
71D9: 98         SBC         B
71DA: F9         LD           SP,HL
71DB: 30 71      JR           NC,$724E
71DD: 20 60      JR           NZ,$723F
71DF: 00         NOP
71E0: 00         NOP
71E1: 00         NOP
71E2: 00         NOP
71E3: 00         NOP
71E4: 80         ADD         A,B
71E5: 00         NOP
71E6: 40         LD           B,B
71E7: 80         ADD         A,B
71E8: A0         AND         B
71E9: C0         RET         NZ
71EA: 60         LD           H,B
71EB: C0         RET         NZ
71EC: 10 E0      STOP       $E0
71EE: 90         SUB         B
71EF: 60         LD           H,B
71F0: 10 E0      STOP       $E0
71F2: 88         ADC         A,B
71F3: 70         LD           (HL),B
71F4: A4         AND         H
71F5: 78         LD           A,B
71F6: 74         LD           (HL),H
71F7: F8 7A      LDHL       SP,$7A
71F9: DC DE 8C   CALL       C,$8CDE
71FC: CE 84      ADC         $84
71FE: C6 00      ADD         $00
7200: 00         NOP
7201: 00         NOP
7202: 00         NOP
7203: 00         NOP
7204: 00         NOP
7205: 00         NOP
7206: 00         NOP
7207: 00         NOP
7208: 0F         RRCA
7209: 00         NOP
720A: 1F         RRA
720B: 00         NOP
720C: 3F         CCF
720D: 02         LD           (BC),A
720E: 3F         CCF
720F: 06 3F      LD           B,$3F
7211: 06 1F      LD           B,$1F
7213: 07         RLCA
7214: 3F         CCF
7215: 0B         DEC         BC
7216: 7F         LD           A,A
7217: 0B         DEC         BC
7218: F7         RST         0X30
7219: 0F         RRCA
721A: FB         EI
721B: 07         RLCA
721C: 77         LD           (HL),A
721D: 08 FF 0B   LD           ($0BFF),SP
7220: 00         NOP
7221: 00         NOP
7222: 38 00      JR           C,$7224
7224: 76         HALT
7225: 38 EF      JR           C,$7216
7227: 16 DA      LD           D,$DA
7229: 6C         LD           L,H
722A: FD                              
722B: 62         LD           H,D
722C: F7         RST         0X30
722D: 5A         LD           E,D
722E: FE 18      CP           $18
7230: FC                              
7231: 00         NOP
7232: FC                              
7233: 80         ADD         A,B
7234: FE 50      CP           $50
7236: EF         RST         0X28
7237: 70         LD           (HL),B
7238: BF         CP           A
7239: C0         RET         NZ
723A: 7E         LD           A,(HL)
723B: 80         ADD         A,B
723C: FF         RST         0X38
723D: 40         LD           B,B
723E: FF         RST         0X38
723F: 40         LD           B,B
7240: FF         RST         0X38
7241: 08 EF 18   LD           ($18EF),SP
7244: 7F         LD           A,A
7245: 17         RLA
7246: 3C         INC         A
7247: 0F         RRCA
7248: 21 1E 20   LD           HL,$201E
724B: 1F         RRA
724C: 10 0F      STOP       $0F
724E: 0C         INC         C
724F: 03         INC         BC
7250: 03         INC         BC
7251: 00         NOP
7252: 01 00 01   LD           BC,$0100
7255: 00         NOP
7256: 01 00 01   LD           BC,$0100
7259: 00         NOP
725A: 00         NOP
725B: 00         NOP
725C: 00         NOP
725D: 00         NOP
725E: 00         NOP
725F: 00         NOP
7260: FF         RST         0X38
7261: 20 EF      JR           NZ,$7252
7263: 30 7E      JR           NC,$72E3
7265: 98         SBC         B
7266: 38 C0      JR           C,$7228
7268: 20 C0      JR           NZ,$722A
726A: A0         AND         B
726B: 40         LD           B,B
726C: 7E         LD           A,(HL)
726D: 80         ADD         A,B
726E: 0E FC      LD           C,$FC
7270: 3C         INC         A
7271: F8 78      LDHL       SP,$78
7273: E0 60      LDFF00   ($60),A
7275: C0         RET         NZ
7276: 60         LD           H,B
7277: C0         RET         NZ
7278: E0 C0      LDFF00   ($C0),A
727A: E0 40      LDFF00   ($40),A
727C: 40         LD           B,B
727D: 00         NOP
727E: 00         NOP
727F: 00         NOP
7280: FF         RST         0X38
7281: 08 EF 18   LD           ($18EF),SP
7284: 7F         LD           A,A
7285: 17         RLA
7286: 3C         INC         A
7287: 0F         RRCA
7288: 20 1F      JR           NZ,$72A9
728A: 21 1E 23   LD           HL,$231E
728D: 1C         INC         E
728E: 24         INC         H
728F: 18 22      JR           $72B3
7291: 1C         INC         E
7292: 49         LD           C,C
7293: 3E 5D      LD           A,$5D
7295: 3E BE      LD           A,$BE
7297: 77         LD           (HL),A
7298: F7         RST         0X30
7299: 63         LD           H,E
729A: E3                              
729B: 41         LD           B,C
729C: 41         LD           B,C
729D: 00         NOP
729E: 00         NOP
729F: 00         NOP
72A0: FF         RST         0X38
72A1: 20 EF      JR           NZ,$7292
72A3: 30 7E      JR           NC,$7323
72A5: 98         SBC         B
72A6: 38 C0      JR           C,$7268
72A8: 20 C0      JR           NZ,$726A
72AA: 20 C0      JR           NZ,$726C
72AC: C0         RET         NZ
72AD: 00         NOP
72AE: 00         NOP
72AF: 00         NOP
72B0: 00         NOP
72B1: 00         NOP
72B2: 00         NOP
72B3: 00         NOP
72B4: 00         NOP
72B5: 00         NOP
72B6: 80         ADD         A,B
72B7: 00         NOP
72B8: 80         ADD         A,B
72B9: 00         NOP
72BA: 80         ADD         A,B
72BB: 00         NOP
72BC: 80         ADD         A,B
72BD: 00         NOP
72BE: 00         NOP
72BF: 00         NOP
72C0: 00         NOP
72C1: FF         RST         0X38
72C2: 00         NOP
72C3: FF         RST         0X38
72C4: 24         INC         H
72C5: FF         RST         0X38
72C6: 18 FF      JR           $72C7
72C8: 18 FF      JR           $72C9
72CA: 24         INC         H
72CB: FF         RST         0X38
72CC: 00         NOP
72CD: FF         RST         0X38
72CE: 00         NOP
72CF: FF         RST         0X38
72D0: 00         NOP
72D1: FF         RST         0X38
72D2: 00         NOP
72D3: FF         RST         0X38
72D4: 24         INC         H
72D5: FF         RST         0X38
72D6: 18 FF      JR           $72D7
72D8: 18 FF      JR           $72D9
72DA: 24         INC         H
72DB: FF         RST         0X38
72DC: 00         NOP
72DD: FF         RST         0X38
72DE: 00         NOP
72DF: FF         RST         0X38
72E0: 00         NOP
72E1: FF         RST         0X38
72E2: 00         NOP
72E3: FF         RST         0X38
72E4: 24         INC         H
72E5: FF         RST         0X38
72E6: 18 FF      JR           $72E7
72E8: 18 FF      JR           $72E9
72EA: 24         INC         H
72EB: FF         RST         0X38
72EC: 00         NOP
72ED: FF         RST         0X38
72EE: 00         NOP
72EF: FF         RST         0X38
72F0: 00         NOP
72F1: FF         RST         0X38
72F2: 00         NOP
72F3: FF         RST         0X38
72F4: 24         INC         H
72F5: FF         RST         0X38
72F6: 18 FF      JR           $72F7
72F8: 18 FF      JR           $72F9
72FA: 24         INC         H
72FB: FF         RST         0X38
72FC: 00         NOP
72FD: FF         RST         0X38
72FE: 00         NOP
72FF: FF         RST         0X38
7300: 00         NOP
7301: 00         NOP
7302: 01 00 06   LD           BC,$0600
7305: 01 0C 07   LD           BC,$070C
7308: 1A         LD           A,(DE)
7309: 0D         DEC         C
730A: 16 09      LD           D,$09
730C: 0E 05      LD           C,$05
730E: 0E 05      LD           C,$05
7310: 19         ADD         HL,DE
7311: 0E 30      LD           C,$30
7313: 0F         RRCA
7314: 68         LD           L,B
7315: 37         SCF
7316: AE         XOR         (HL)
7317: 71         LD           (HL),C
7318: C6 7B      ADD         $7B
731A: 8F         ADC         A,A
731B: 76         HALT
731C: 49         LD           C,C
731D: 36 5D      LD           (HL),$5D
731F: 22         LD           (HLI),A
7320: 00         NOP
7321: 00         NOP
7322: E0 00      LDFF00   ($00),A
7324: D0         RET         NC
7325: E0 28      LDFF00   ($28),A
7327: F0 18      LD           A,($18)
7329: F0 14      LD           A,($14)
732B: F8 04      LDHL       SP,$04
732D: F8 C4      LDHL       SP,$C4
732F: 38 CA      JR           C,$72FB
7331: BC         CP           H
7332: 45         LD           B,L
7333: BE         CP           (HL)
7334: 85         ADD         A,L
7335: 7E         LD           A,(HL)
7336: C9         RET
7337: BE         CP           (HL)
7338: 4A         LD           C,D
7339: BC         CP           H
733A: 44         LD           B,H
733B: B8         CP           B
733C: 42         LD           B,D
733D: BC         CP           H
733E: 22         LD           (HLI),A
733F: DC 2C 1F   CALL       C,$1F2C
7342: 58         LD           E,B
7343: 3F         CCF
7344: 43         LD           B,E
7345: 3C         INC         A
7346: 45         LD           B,L
7347: 3E 62      LD           A,$62
7349: 1F         RRA
734A: 78         LD           A,B
734B: 27         DAA
734C: B6         OR           (HL)
734D: 69         LD           L,C
734E: BB         CP           E
734F: 5C         LD           E,H
7350: DD                              
7351: 3E AF      LD           A,$AF
7353: 5C         LD           E,H
7354: 9F         SBC         A
7355: 60         LD           H,B
7356: 89         ADC         A,C
7357: 76         HALT
7358: 88         ADC         A,B
7359: 77         LD           (HL),A
735A: 50         LD           D,B
735B: 2F         CPL
735C: 30 0F      JR           NC,$736D
735E: 1F         RRA
735F: 00         NOP
7360: 92         SUB         D
7361: 6C         LD           L,H
7362: 7C         LD           A,H
7363: 80         ADD         A,B
7364: FC                              
7365: 18 FE      JR           $7365
7367: 3C         INC         A
7368: FE 04      CP           $04
736A: 6F         LD           L,A
736B: F6 1F      OR           $1F
736D: EE 3D      XOR         $3D
736F: DE 3B      SBC         $3B
7371: DC 2D D2   CALL       C,$D22D
7374: 79         LD           A,C
7375: 86         ADD         A,(HL)
7376: C5         PUSH       BC
7377: 3A         LD           A,(HLD)
7378: 46         LD           B,(HL)
7379: B8         CP           B
737A: 44         LD           B,H
737B: B8         CP           B
737C: 48         LD           C,B
737D: B0         OR           B
737E: F0 00      LD           A,($00)
7380: 00         NOP
7381: FF         RST         0X38
7382: 00         NOP
7383: FF         RST         0X38
7384: 24         INC         H
7385: FF         RST         0X38
7386: 18 FF      JR           $7387
7388: 18 FF      JR           $7389
738A: 24         INC         H
738B: FF         RST         0X38
738C: 00         NOP
738D: FF         RST         0X38
738E: 00         NOP
738F: FF         RST         0X38
7390: 00         NOP
7391: FF         RST         0X38
7392: 00         NOP
7393: FF         RST         0X38
7394: 24         INC         H
7395: FF         RST         0X38
7396: 18 FF      JR           $7397
7398: 18 FF      JR           $7399
739A: 24         INC         H
739B: FF         RST         0X38
739C: 00         NOP
739D: FF         RST         0X38
739E: 00         NOP
739F: FF         RST         0X38
73A0: 00         NOP
73A1: FF         RST         0X38
73A2: 00         NOP
73A3: FF         RST         0X38
73A4: 24         INC         H
73A5: FF         RST         0X38
73A6: 18 FF      JR           $73A7
73A8: 18 FF      JR           $73A9
73AA: 24         INC         H
73AB: FF         RST         0X38
73AC: 00         NOP
73AD: FF         RST         0X38
73AE: 00         NOP
73AF: FF         RST         0X38
73B0: 00         NOP
73B1: FF         RST         0X38
73B2: 00         NOP
73B3: FF         RST         0X38
73B4: 24         INC         H
73B5: FF         RST         0X38
73B6: 18 FF      JR           $73B7
73B8: 18 FF      JR           $73B9
73BA: 24         INC         H
73BB: FF         RST         0X38
73BC: 00         NOP
73BD: FF         RST         0X38
73BE: 00         NOP
73BF: FF         RST         0X38
73C0: 00         NOP
73C1: FF         RST         0X38
73C2: 00         NOP
73C3: FF         RST         0X38
73C4: 24         INC         H
73C5: FF         RST         0X38
73C6: 18 FF      JR           $73C7
73C8: 18 FF      JR           $73C9
73CA: 24         INC         H
73CB: FF         RST         0X38
73CC: 00         NOP
73CD: FF         RST         0X38
73CE: 00         NOP
73CF: FF         RST         0X38
73D0: 00         NOP
73D1: FF         RST         0X38
73D2: 00         NOP
73D3: FF         RST         0X38
73D4: 24         INC         H
73D5: FF         RST         0X38
73D6: 18 FF      JR           $73D7
73D8: 18 FF      JR           $73D9
73DA: 24         INC         H
73DB: FF         RST         0X38
73DC: 00         NOP
73DD: FF         RST         0X38
73DE: 00         NOP
73DF: FF         RST         0X38
73E0: 00         NOP
73E1: FF         RST         0X38
73E2: 00         NOP
73E3: FF         RST         0X38
73E4: 24         INC         H
73E5: FF         RST         0X38
73E6: 18 FF      JR           $73E7
73E8: 18 FF      JR           $73E9
73EA: 24         INC         H
73EB: FF         RST         0X38
73EC: 00         NOP
73ED: FF         RST         0X38
73EE: 00         NOP
73EF: FF         RST         0X38
73F0: 00         NOP
73F1: FF         RST         0X38
73F2: 00         NOP
73F3: FF         RST         0X38
73F4: 24         INC         H
73F5: FF         RST         0X38
73F6: 18 FF      JR           $73F7
73F8: 18 FF      JR           $73F9
73FA: 24         INC         H
73FB: FF         RST         0X38
73FC: 00         NOP
73FD: FF         RST         0X38
73FE: 00         NOP
73FF: FF         RST         0X38
7400: 38 00      JR           C,$7402
7402: 4C         LD           C,H
7403: 38 46      JR           C,$744B
7405: 3C         INC         A
7406: 4B         LD           C,E
7407: 34         INC         (HL)
7408: 5C         LD           E,H
7409: 2B         DEC         HL
740A: 5F         LD           E,A
740B: 28 7F      JR           Z,$748C
740D: 07         RLCA
740E: FF         RST         0X38
740F: 7F         LD           A,A
7410: FF         RST         0X38
7411: 4A         LD           C,D
7412: 7F         LD           A,A
7413: 2A         LD           A,(HLI)
7414: 3F         CCF
7415: 0F         RRCA
7416: 3F         CCF
7417: 1F         RRA
7418: 3F         CCF
7419: 11 7F 1B   LD           DE,$1B7F
741C: FF         RST         0X38
741D: 5F         LD           E,A
741E: FF         RST         0X38
741F: 6B         LD           L,E
7420: 1E 00      LD           E,$00
7422: 39         ADD         HL,SP
7423: 1E 61      LD           E,$61
7425: 3E E1      LD           A,$E1
7427: 1E E2      LD           E,$E2
7429: 5C         LD           E,H
742A: E2         LDFF00   (C),A
742B: 5C         LD           E,H
742C: FE 00      CP           $00
742E: FF         RST         0X38
742F: FE FB      CP           $FB
7431: 66         LD           H,(HL)
7432: FE EC      CP           $EC
7434: FC                              
7435: E0 F8      LDFF00   ($F8),A
7437: E0 FC      LDFF00   ($FC),A
7439: D8         RET         C
743A: FE BC      CP           $BC
743C: FD                              
743D: BE         CP           (HL)
743E: 9F         SBC         A
743F: 6E         LD           L,(HL)
7440: FF         RST         0X38
7441: 70         LD           (HL),B
7442: BF         CP           A
7443: 7C         LD           A,H
7444: 5F         LD           E,A
7445: 3D         DEC         A
7446: 7F         LD           A,A
7447: 15         DEC         D
7448: 7F         LD           A,A
7449: 23         INC         HL
744A: 7F         LD           A,A
744B: 3F         CCF
744C: 7F         LD           A,A
744D: 29         ADD         HL,HL
744E: 7F         LD           A,A
744F: 3F         CCF
7450: 7F         LD           A,A
7451: 22         LD           (HLI),A
7452: 7F         LD           A,A
7453: 3F         CCF
7454: 7F         LD           A,A
7455: 25         DEC         H
7456: 7F         LD           A,A
7457: 3F         CCF
7458: 7F         LD           A,A
7459: 00         NOP
745A: 00         NOP
745B: 00         NOP
745C: 00         NOP
745D: 00         NOP
745E: 00         NOP
745F: 00         NOP
7460: 0C         INC         C
7461: 00         NOP
7462: 16 0C      LD           D,$0C
7464: 13         INC         DE
7465: 0E 15      LD           C,$15
7467: 0A         LD           A,(BC)
7468: 1E 05      LD           E,$05
746A: 1F         RRA
746B: 08 7F 07   LD           ($077F),SP
746E: 7F         LD           A,A
746F: 2F         CPL
7470: 6F         LD           L,A
7471: 1C         INC         E
7472: 7F         LD           A,A
7473: 3D         DEC         A
7474: FF         RST         0X38
7475: 7F         LD           A,A
7476: FF         RST         0X38
7477: 0F         RRCA
7478: FF         RST         0X38
7479: 5F         LD           E,A
747A: FF         RST         0X38
747B: 7C         LD           A,H
747C: 7C         LD           A,H
747D: 3B         DEC         SP
747E: F8 47      LDHL       SP,$47
7480: 38 00      JR           C,$7482
7482: 64         LD           H,H
7483: 38 C4      JR           C,$7449
7485: 78         LD           A,B
7486: 64         LD           H,H
7487: 98         SBC         B
7488: D4 68 A4   CALL       NC,$A468
748B: D8         RET         C
748C: F8 00      LDHL       SP,$00
748E: FC                              
748F: F8 EC      LDHL       SP,$EC
7491: 98         SBC         B
7492: F8 F0      LDHL       SP,$F0
7494: F0 80      LD           A,($80)
7496: F8 B0      LDHL       SP,$B0
7498: FC                              
7499: F8 FE      LDHL       SP,$FE
749B: FC                              
749C: 7D         LD           A,L
749D: FE 3F      CP           $3F
749F: EE 0F      XOR         $0F
74A1: 00         NOP
74A2: 18 07      JR           $74AB
74A4: 1F         RRA
74A5: 0A         LD           A,(BC)
74A6: 3F         CCF
74A7: 04         INC         B
74A8: 3F         CCF
74A9: 1A         LD           A,(DE)
74AA: 5F         LD           E,A
74AB: 38 4F      JR           C,$74FC
74AD: 33         INC         SP
74AE: 6B         LD           L,E
74AF: 17         RLA
74B0: 38 07      JR           C,$74B9
74B2: 07         RLCA
74B3: 00         NOP
74B4: 05         DEC         B
74B5: 02         LD           (BC),A
74B6: 05         DEC         B
74B7: 03         INC         BC
74B8: 0B         DEC         BC
74B9: 04         INC         B
74BA: 09         ADD         HL,BC
74BB: 07         RLCA
74BC: 08 07 07   LD           ($0707),SP
74BF: 00         NOP
74C0: 00         NOP
74C1: 00         NOP
74C2: F0 00      LD           A,($00)
74C4: 88         ADC         A,B
74C5: 70         LD           (HL),B
74C6: C8         RET         Z
74C7: F0 C8      LD           A,($C8)
74C9: F0 C8      LD           A,($C8)
74CB: 30 F0      JR           NC,$74BD
74CD: 80         ADD         A,B
74CE: 20 C0      JR           NZ,$7490
74D0: 20 C0      JR           NZ,$7492
74D2: C0         RET         NZ
74D3: 00         NOP
74D4: A0         AND         B
74D5: 40         LD           B,B
74D6: A0         AND         B
74D7: C0         RET         NZ
74D8: D0         RET         NC
74D9: 20 90      JR           NZ,$746B
74DB: E0 10      LDFF00   ($10),A
74DD: E0 E0      LDFF00   ($E0),A
74DF: 00         NOP
74E0: 00         NOP
74E1: 00         NOP
74E2: 00         NOP
74E3: 00         NOP
74E4: 00         NOP
74E5: 00         NOP
74E6: 00         NOP
74E7: 00         NOP
74E8: 00         NOP
74E9: 00         NOP
74EA: 00         NOP
74EB: 00         NOP
74EC: 00         NOP
74ED: 00         NOP
74EE: 00         NOP
74EF: 00         NOP
74F0: 03         INC         BC
74F1: 00         NOP
74F2: 04         INC         B
74F3: 03         INC         BC
74F4: 05         DEC         B
74F5: 02         LD           (BC),A
74F6: 05         DEC         B
74F7: 03         INC         BC
74F8: 0B         DEC         BC
74F9: 04         INC         B
74FA: 09         ADD         HL,BC
74FB: 07         RLCA
74FC: 08 07 07   LD           ($0707),SP
74FF: 00         NOP
7500: 1C         INC         E
7501: 00         NOP
7502: 1F         RRA
7503: 0C         INC         C
7504: 0F         RRCA
7505: 06 1F      LD           B,$1F
7507: 03         INC         BC
7508: 3F         CCF
7509: 18 3F      JR           $754A
750B: 1E 7F      LD           E,$7F
750D: 0C         INC         C
750E: CF         RST         0X08
750F: 37         SCF
7510: E7         RST         0X20
7511: 5B         LD           E,E
7512: F3         DI
7513: 6C         LD           L,H
7514: F8 07      LDHL       SP,$07
7516: 7F         LD           A,A
7517: 30 78      JR           NC,$7591
7519: 37         SCF
751A: FF         RST         0X38
751B: 00         NOP
751C: B3         OR           E
751D: 7C         LD           A,H
751E: FF         RST         0X38
751F: 00         NOP
7520: F0 00      LD           A,($00)
7522: F8 00      LDHL       SP,$00
7524: 74         LD           (HL),H
7525: C8         RET         Z
7526: BE         CP           (HL)
7527: 5C         LD           E,H
7528: DD                              
7529: BE         CP           (HL)
752A: E3                              
752B: 1E F5      LD           E,$F5
752D: CE F9      ADC         $F9
752F: E6 F6      AND         $F6
7531: 28 24      JR           Z,$7557
7533: D8         RET         C
7534: 38 C0      JR           C,$74F6
7536: F0 00      LD           A,($00)
7538: 70         LD           (HL),B
7539: 80         ADD         A,B
753A: F0 00      LD           A,($00)
753C: 68         LD           L,B
753D: F0 F8      LD           A,($F8)
753F: 00         NOP
7540: 00         NOP
7541: 00         NOP
7542: 00         NOP
7543: 00         NOP
7544: 03         INC         BC
7545: 00         NOP
7546: 07         RLCA
7547: 03         INC         BC
7548: 0D         DEC         C
7549: 06 1A      LD           B,$1A
754B: 0C         INC         C
754C: 14         INC         D
754D: 08 18 00   LD           ($0018),SP
7550: 00         NOP
7551: 00         NOP
7552: 00         NOP
7553: 00         NOP
7554: 00         NOP
7555: 00         NOP
7556: 00         NOP
7557: 00         NOP
7558: 00         NOP
7559: 00         NOP
755A: 00         NOP
755B: 00         NOP
755C: 00         NOP
755D: 00         NOP
755E: 00         NOP
755F: 00         NOP
7560: 00         NOP
7561: 00         NOP
7562: 00         NOP
7563: 00         NOP
7564: E0 00      LDFF00   ($00),A
7566: D0         RET         NC
7567: E0 F8      LDFF00   ($F8),A
7569: 70         LD           (HL),B
756A: 5C         LD           E,H
756B: 38 2C      JR           C,$7599
756D: 18 1E      JR           $758D
756F: 0C         INC         C
7570: 16 0C      LD           D,$0C
7572: 0F         RRCA
7573: 06 0B      LD           B,$0B
7575: 06 0B      LD           B,$0B
7577: 07         RLCA
7578: 07         RLCA
7579: 03         INC         BC
757A: 05         DEC         B
757B: 03         INC         BC
757C: 05         DEC         B
757D: 03         INC         BC
757E: 03         INC         BC
757F: 00         NOP
7580: FF         RST         0X38
7581: 00         NOP
7582: FF         RST         0X38
7583: 7F         LD           A,A
7584: FF         RST         0X38
7585: 00         NOP
7586: 40         LD           B,B
7587: 3F         CCF
7588: 47         LD           B,A
7589: 3F         CCF
758A: 6B         LD           L,E
758B: 17         RLA
758C: 24         INC         H
758D: 1B         DEC         DE
758E: 33         INC         SP
758F: 0C         INC         C
7590: 10 0F      STOP       $0F
7592: 18 07      JR           $759B
7594: 0C         INC         C
7595: 03         INC         BC
7596: 06 01      LD           B,$01
7598: 03         INC         BC
7599: 00         NOP
759A: 01 00 00   LD           BC,$0000
759D: 00         NOP
759E: 00         NOP
759F: 00         NOP
75A0: FF         RST         0X38
75A1: 00         NOP
75A2: FF         RST         0X38
75A3: FF         RST         0X38
75A4: FF         RST         0X38
75A5: 00         NOP
75A6: 00         NOP
75A7: FF         RST         0X38
75A8: FF         RST         0X38
75A9: FF         RST         0X38
75AA: FF         RST         0X38
75AB: FF         RST         0X38
75AC: FF         RST         0X38
75AD: FF         RST         0X38
75AE: 00         NOP
75AF: FF         RST         0X38
75B0: FF         RST         0X38
75B1: 00         NOP
75B2: 00         NOP
75B3: FF         RST         0X38
75B4: 00         NOP
75B5: FF         RST         0X38
75B6: 00         NOP
75B7: FF         RST         0X38
75B8: FF         RST         0X38
75B9: 00         NOP
75BA: FF         RST         0X38
75BB: 00         NOP
75BC: 00         NOP
75BD: 00         NOP
75BE: 00         NOP
75BF: 00         NOP
75C0: FF         RST         0X38
75C1: 00         NOP
75C2: FF         RST         0X38
75C3: FE FF      CP           $FF
75C5: 00         NOP
75C6: 0E F0      LD           C,$F0
75C8: E8 F0      ADD         SP,$F0
75CA: E8 F0      ADD         SP,$F0
75CC: D8         RET         C
75CD: E0 34      LDFF00   ($34),A
75CF: C8         RET         Z
75D0: F4                              
75D1: 08 36 C8   LD           ($C836),SP
75D4: 33         INC         SP
75D5: CC 71 8E   CALL       Z,$8E71
75D8: F1         POP         AF
75D9: 0E E9      LD           C,$E9
75DB: 06 0F      LD           B,$0F
75DD: 00         NOP
75DE: 00         NOP
75DF: 00         NOP
75E0: 18 00      JR           $75E2
75E2: 24         INC         H
75E3: 18 42      JR           $7627
75E5: 3C         INC         A
75E6: 43         LD           B,E
75E7: 3C         INC         A
75E8: 3D         DEC         A
75E9: 00         NOP
75EA: 39         ADD         HL,SP
75EB: 10 38      STOP       $38
75ED: 00         NOP
75EE: 44         LD           B,H
75EF: 38 82      JR           C,$7573
75F1: 7C         LD           A,H
75F2: 82         ADD         A,D
75F3: 7C         LD           A,H
75F4: 84         ADD         A,H
75F5: 78         LD           A,B
75F6: 48         LD           C,B
75F7: 30 31      JR           NC,$762A
75F9: 00         NOP
75FA: 31 00 1A   LD           SP,$1A00
75FD: 00         NOP
75FE: 0C         INC         C
75FF: 00         NOP
7600: 1C         INC         E
7601: 00         NOP
7602: 3A         LD           A,(HLD)
7603: 1C         INC         E
7604: 29         ADD         HL,HL
7605: 1E 11      LD           E,$11
7607: 0E 39      LD           C,$39
7609: 1E 1B      LD           E,$1B
760B: 0C         INC         C
760C: 17         RLA
760D: 08 1F 00   LD           ($001F),SP
7610: 0B         DEC         BC
7611: 04         INC         B
7612: 08 07 04   LD           ($0407),SP
7615: 03         INC         BC
7616: 07         RLCA
7617: 00         NOP
7618: 07         RLCA
7619: 00         NOP
761A: 0D         DEC         C
761B: 06 0B      LD           B,$0B
761D: 04         INC         B
761E: 0F         RRCA
761F: 00         NOP
7620: 3C         INC         A
7621: 00         NOP
7622: 42         LD           B,D
7623: 3C         INC         A
7624: 99         SBC         C
7625: 66         LD           H,(HL)
7626: BD         CP           L
7627: 42         LD           B,D
7628: 3C         INC         A
7629: C3 18 E7   JP           $E718
762C: 81         ADD         A,C
762D: 7E         LD           A,(HL)
762E: 81         ADD         A,C
762F: 7E         LD           A,(HL)
7630: 00         NOP
7631: FF         RST         0X38
7632: 42         LD           B,D
7633: BD         CP           L
7634: FF         RST         0X38
7635: 42         LD           B,D
7636: FF         RST         0X38
7637: 3C         INC         A
7638: BD         CP           L
7639: 7E         LD           A,(HL)
763A: DB                              
763B: 3C         INC         A
763C: BD         CP           L
763D: 00         NOP
763E: 00         NOP
763F: 00         NOP
7640: 00         NOP
7641: 00         NOP
7642: 30 00      JR           NC,$7644
7644: 78         LD           A,B
7645: 30 5C      JR           NC,$76A3
7647: 38 EB      JR           C,$7634
7649: 5C         LD           E,H
764A: BB         CP           E
764B: 7C         LD           A,H
764C: 57         LD           D,A
764D: 38 EF      JR           C,$763E
764F: 50         LD           D,B
7650: BB         CP           E
7651: 74         LD           (HL),H
7652: 48         LD           C,B
7653: 37         SCF
7654: 24         INC         H
7655: 1B         DEC         DE
7656: 1F         RRA
7657: 00         NOP
7658: 07         RLCA
7659: 00         NOP
765A: 0D         DEC         C
765B: 06 0B      LD           B,$0B
765D: 04         INC         B
765E: 0F         RRCA
765F: 00         NOP
7660: 00         NOP
7661: 00         NOP
7662: 00         NOP
7663: 00         NOP
7664: 00         NOP
7665: 00         NOP
7666: 00         NOP
7667: 00         NOP
7668: 0D         DEC         C
7669: 00         NOP
766A: 1F         RRA
766B: 0C         INC         C
766C: 3F         CCF
766D: 18 37      JR           $76A6
766F: 18 73      JR           $76E4
7671: 1C         INC         E
7672: 72         LD           (HL),D
7673: 2D         DEC         L
7674: 72         LD           (HL),D
7675: 1D         DEC         E
7676: 57         LD           D,A
7677: 28 25      JR           Z,$769E
7679: 1A         LD           A,(DE)
767A: 17         RLA
767B: 08 0F 00   LD           ($000F),SP
767E: 00         NOP
767F: 00         NOP
7680: 00         NOP
7681: FF         RST         0X38
7682: 00         NOP
7683: FF         RST         0X38
7684: 24         INC         H
7685: FF         RST         0X38
7686: 18 FF      JR           $7687
7688: 18 FF      JR           $7689
768A: 24         INC         H
768B: FF         RST         0X38
768C: 00         NOP
768D: FF         RST         0X38
768E: 00         NOP
768F: FF         RST         0X38
7690: 00         NOP
7691: FF         RST         0X38
7692: 00         NOP
7693: FF         RST         0X38
7694: 24         INC         H
7695: FF         RST         0X38
7696: 18 FF      JR           $7697
7698: 18 FF      JR           $7699
769A: 24         INC         H
769B: FF         RST         0X38
769C: 00         NOP
769D: FF         RST         0X38
769E: 00         NOP
769F: FF         RST         0X38
76A0: 00         NOP
76A1: FF         RST         0X38
76A2: 00         NOP
76A3: FF         RST         0X38
76A4: 24         INC         H
76A5: FF         RST         0X38
76A6: 18 FF      JR           $76A7
76A8: 18 FF      JR           $76A9
76AA: 24         INC         H
76AB: FF         RST         0X38
76AC: 00         NOP
76AD: FF         RST         0X38
76AE: 00         NOP
76AF: FF         RST         0X38
76B0: 00         NOP
76B1: FF         RST         0X38
76B2: 00         NOP
76B3: FF         RST         0X38
76B4: 24         INC         H
76B5: FF         RST         0X38
76B6: 18 FF      JR           $76B7
76B8: 18 FF      JR           $76B9
76BA: 24         INC         H
76BB: FF         RST         0X38
76BC: 00         NOP
76BD: FF         RST         0X38
76BE: 00         NOP
76BF: FF         RST         0X38
76C0: 00         NOP
76C1: 00         NOP
76C2: 00         NOP
76C3: 00         NOP
76C4: 00         NOP
76C5: 00         NOP
76C6: 03         INC         BC
76C7: 00         NOP
76C8: 04         INC         B
76C9: 03         INC         BC
76CA: 1B         DEC         DE
76CB: 07         RLCA
76CC: 34         INC         (HL)
76CD: 0F         RRCA
76CE: 58         LD           E,B
76CF: 2F         CPL
76D0: A3         AND         E
76D1: 5F         LD           E,A
76D2: E7         RST         0X20
76D3: 1C         INC         E
76D4: BC         CP           H
76D5: 5B         LD           E,E
76D6: 9E         SBC         (HL)
76D7: 61         LD           H,C
76D8: EA 45 44   LD           ($4445),A
76DB: 03         INC         BC
76DC: 03         INC         BC
76DD: 00         NOP
76DE: 00         NOP
76DF: 00         NOP
76E0: 00         NOP
76E1: 00         NOP
76E2: 00         NOP
76E3: 00         NOP
76E4: 00         NOP
76E5: 00         NOP
76E6: C0         RET         NZ
76E7: 00         NOP
76E8: 38 C0      JR           C,$76AA
76EA: D4 E8 2A   CALL       NC,$2AE8
76ED: F4                              
76EE: 1A         LD           A,(DE)
76EF: F4                              
76F0: C6 F8      ADD         $F8
76F2: E4                              
76F3: 38 3C      JR           C,$7731
76F5: D8         RET         C
76F6: 7A         LD           A,D
76F7: 84         ADD         A,H
76F8: 52         LD           D,D
76F9: AC         XOR         H
76FA: 2E C4      LD           L,$C4
76FC: CE 04      ADC         $04
76FE: 04         INC         B
76FF: 00         NOP
7700: 00         NOP
7701: 00         NOP
7702: 00         NOP
7703: 00         NOP
7704: 7F         LD           A,A
7705: 00         NOP
7706: FD                              
7707: 7B         LD           A,E
7708: FB         EI
7709: 77         LD           (HL),A
770A: 8B         ADC         A,E
770B: 77         LD           (HL),A
770C: F9         LD           SP,HL
770D: 77         LD           (HL),A
770E: 8C         ADC         A,H
770F: 73         LD           (HL),E
7710: F7         RST         0X30
7711: 78         LD           A,B
7712: FB         EI
7713: 7F         LD           A,A
7714: 84         ADD         A,H
7715: 7B         LD           A,E
7716: FF         RST         0X38
7717: 00         NOP
7718: B1         OR           C
7719: 4E         LD           C,(HL)
771A: BF         CP           A
771B: 40         LD           B,B
771C: 80         ADD         A,B
771D: 7F         LD           A,A
771E: 7F         LD           A,A
771F: 00         NOP
7720: 3F         CCF
7721: 00         NOP
7722: 7F         LD           A,A
7723: 38 7F      JR           C,$77A4
7725: 31 4F 30   LD           SP,$304F
7728: 7B         LD           A,E
7729: 34         INC         (HL)
772A: 79         LD           A,C
772B: 36 4C      LD           (HL),$4C
772D: 33         INC         SP
772E: 77         LD           (HL),A
772F: 38 7B      JR           C,$77AC
7731: 3F         CCF
7732: 7B         LD           A,E
7733: 3F         CCF
7734: 44         LD           B,H
7735: 3B         DEC         SP
7736: 7F         LD           A,A
7737: 00         NOP
7738: 59         LD           E,C
7739: 26 5F      LD           H,$5F
773B: 20 40      JR           NZ,$777D
773D: 3F         CCF
773E: 3F         CCF
773F: 00         NOP
7740: 0F         RRCA
7741: 00         NOP
7742: 73         LD           (HL),E
7743: 0F         RRCA
7744: F7         RST         0X30
7745: 6F         LD           L,A
7746: 9F         SBC         A
7747: 64         LD           H,H
7748: FF         RST         0X38
7749: 60         LD           H,B
774A: 9F         SBC         A
774B: 6F         LD           L,A
774C: F3         DI
774D: 6F         LD           L,A
774E: 96         SUB         (HL)
774F: 6F         LD           L,A
7750: BB         CP           E
7751: 77         LD           (HL),A
7752: 57         LD           D,A
7753: 38 20      JR           C,$7775
7755: 1F         RRA
7756: 7F         LD           A,A
7757: 3F         CCF
7758: 43         LD           B,E
7759: 3C         INC         A
775A: FF         RST         0X38
775B: 78         LD           A,B
775C: FF         RST         0X38
775D: 00         NOP
775E: 7F         LD           A,A
775F: 00         NOP
7760: E0 00      LDFF00   ($00),A
7762: 90         SUB         B
7763: E0 E8      LDFF00   ($E8),A
7765: F0 EC      LD           A,($EC)
7767: B0         OR           B
7768: EE 34      XOR         $34
776A: 0F         RRCA
776B: F6 EB      OR           $EB
776D: F6 7D      OR           $7D
776F: 8E         ADC         A,(HL)
7770: ED                              
7771: 7E         LD           A,(HL)
7772: EA 7C 7E   LD           ($7E7C),A
7775: 80         ADD         A,B
7776: 82         ADD         A,D
7777: FC                              
7778: BE         CP           (HL)
7779: 7C         LD           A,H
777A: C3 3C FF   JP           $FF3C
777D: 3E FF      LD           A,$FF
777F: 00         NOP
7780: 00         NOP
7781: 00         NOP
7782: 00         NOP
7783: 00         NOP
7784: 00         NOP
7785: 00         NOP
7786: 0E 00      LD           C,$00
7788: 1E 04      LD           E,$04
778A: 1D         DEC         E
778B: 0E 1A      LD           C,$1A
778D: 07         RLCA
778E: 05         DEC         B
778F: 03         INC         BC
7790: 02         LD           (BC),A
7791: 01 01 00   LD           BC,$0001
7794: 00         NOP
7795: 00         NOP
7796: 00         NOP
7797: 00         NOP
7798: 00         NOP
7799: 00         NOP
779A: 00         NOP
779B: 00         NOP
779C: 00         NOP
779D: 00         NOP
779E: 00         NOP
779F: 00         NOP
77A0: 03         INC         BC
77A1: 00         NOP
77A2: 07         RLCA
77A3: 03         INC         BC
77A4: 0F         RRCA
77A5: 07         RLCA
77A6: 0F         RRCA
77A7: 04         INC         B
77A8: 7F         LD           A,A
77A9: 05         DEC         B
77AA: 7B         LD           A,E
77AB: 37         SCF
77AC: 7F         LD           A,A
77AD: 31 3F 1D   LD           SP,$1D3F
77B0: 5F         LD           E,A
77B1: 2C         INC         L
77B2: 7C         LD           A,H
77B3: 03         INC         BC
77B4: 7B         LD           A,E
77B5: 34         INC         (HL)
77B6: 7C         LD           A,H
77B7: 33         INC         SP
77B8: 3F         CCF
77B9: 00         NOP
77BA: 0F         RRCA
77BB: 06 1F      LD           B,$1F
77BD: 0E 1F      LD           C,$1F
77BF: 00         NOP
77C0: F0 00      LD           A,($00)
77C2: F8 F0      LDHL       SP,$F0
77C4: 7C         LD           A,H
77C5: F8 3C      LDHL       SP,$3C
77C7: C8         RET         Z
77C8: FF         RST         0X38
77C9: E8 F7      ADD         SP,$F7
77CB: 3A         LD           A,(HLD)
77CC: FF         RST         0X38
77CD: E6 FE      AND         $FE
77CF: 2C         INC         L
77D0: FD                              
77D1: 0A         LD           A,(BC)
77D2: CD 32 37   CALL       $3732
77D5: C8         RET         Z
77D6: CF         RST         0X08
77D7: 36 FF      LD           (HL),$FF
77D9: 06 CE      LD           B,$CE
77DB: 30 F8      JR           NC,$77D5
77DD: 00         NOP
77DE: 00         NOP
77DF: 00         NOP
77E0: E7         RST         0X20
77E1: 00         NOP
77E2: FF         RST         0X38
77E3: 67         LD           H,A
77E4: FE 6F      CP           $6F
77E6: 7E         LD           A,(HL)
77E7: 29         ADD         HL,HL
77E8: FF         RST         0X38
77E9: 0B         DEC         BC
77EA: FF         RST         0X38
77EB: 66         LD           H,(HL)
77EC: FF         RST         0X38
77ED: 6B         LD           L,E
77EE: FF         RST         0X38
77EF: 02         LD           (BC),A
77F0: 27         DAA
77F1: 18 7F      JR           $7872
77F3: 20 F8      JR           NZ,$77ED
77F5: 70         LD           (HL),B
77F6: 78         LD           A,B
77F7: 30 70      JR           NC,$7869
77F9: 20 20      JR           NZ,$781B
77FB: 00         NOP
77FC: 00         NOP
77FD: 00         NOP
77FE: 00         NOP
77FF: 00         NOP
7800: 3B         DEC         SP
7801: 00         NOP
7802: 25         DEC         H
7803: 1B         DEC         DE
7804: 19         ADD         HL,DE
7805: 06 0B      LD           B,$0B
7807: 04         INC         B
7808: 1B         DEC         DE
7809: 04         INC         B
780A: FF         RST         0X38
780B: 00         NOP
780C: FA 7D FB   LD           A,($FB7D)
780F: 54         LD           D,H
7810: FA 7D FB   LD           A,($FB7D)
7813: 7C         LD           A,H
7814: FB         EI
7815: 54         LD           D,H
7816: FB         EI
7817: 7C         LD           A,H
7818: FA 7D FB   LD           A,($FB7D)
781B: 54         LD           D,H
781C: 83         ADD         A,E
781D: 7C         LD           A,H
781E: FF         RST         0X38
781F: 00         NOP
7820: DC 00 A4   CALL       C,$A400
7823: D8         RET         C
7824: 9E         SBC         (HL)
7825: 60         LD           H,B
7826: D7         RST         0X10
7827: 22         LD           (HLI),A
7828: D7         RST         0X10
7829: 22         LD           (HLI),A
782A: 9F         SBC         A
782B: 62         LD           H,D
782C: 37         SCF
782D: CA CF 30   JP           Z,$30CF
7830: 2F         CPL
7831: F6 8B      OR           $8B
7833: 76         HALT
7834: FF         RST         0X38
7835: 06 8F      LD           B,$8F
7837: 70         LD           (HL),B
7838: 07         RLCA
7839: FA FF 02   LD           A,($02FF)
783C: 86         ADD         A,(HL)
783D: 78         LD           A,B
783E: FC                              
783F: 00         NOP
7840: 3B         DEC         SP
7841: 00         NOP
7842: 25         DEC         H
7843: 1B         DEC         DE
7844: 19         ADD         HL,DE
7845: 06 0B      LD           B,$0B
7847: 05         DEC         B
7848: FF         RST         0X38
7849: 01 FB 7C   LD           BC,$7CFB
784C: FA 55 FB   LD           A,($FB55)
784F: 7C         LD           A,H
7850: FA 7D FB   LD           A,($FB7D)
7853: 54         LD           D,H
7854: FB         EI
7855: 7C         LD           A,H
7856: FB         EI
7857: 7C         LD           A,H
7858: FA 55 83   LD           A,($8355)
785B: 7C         LD           A,H
785C: 7F         LD           A,A
785D: 00         NOP
785E: FF         RST         0X38
785F: 00         NOP
7860: DC 00 A4   CALL       C,$A400
7863: D8         RET         C
7864: 98         SBC         B
7865: 60         LD           H,B
7866: D2 A0 D7   JP           NC,$D7A0
7869: A2         AND         D
786A: 9F         SBC         A
786B: 62         LD           H,D
786C: 37         SCF
786D: CA C7 3A   JP           Z,$3AC7
7870: 2F         CPL
7871: F0 8F      LD           A,($8F)
7873: 76         HALT
7874: FB         EI
7875: 06 8F      LD           B,$8F
7877: 76         HALT
7878: 77         LD           (HL),A
7879: 88         ADC         A,B
787A: FF         RST         0X38
787B: 72         LD           (HL),D
787C: FF         RST         0X38
787D: 7A         LD           A,D
787E: FE 00      CP           $00
7880: 00         NOP
7881: FF         RST         0X38
7882: 00         NOP
7883: FF         RST         0X38
7884: 24         INC         H
7885: FF         RST         0X38
7886: 18 FF      JR           $7887
7888: 18 FF      JR           $7889
788A: 24         INC         H
788B: FF         RST         0X38
788C: 00         NOP
788D: FF         RST         0X38
788E: 00         NOP
788F: FF         RST         0X38
7890: 00         NOP
7891: FF         RST         0X38
7892: 00         NOP
7893: FF         RST         0X38
7894: 24         INC         H
7895: FF         RST         0X38
7896: 18 FF      JR           $7897
7898: 18 FF      JR           $7899
789A: 24         INC         H
789B: FF         RST         0X38
789C: 00         NOP
789D: FF         RST         0X38
789E: 00         NOP
789F: FF         RST         0X38
78A0: 00         NOP
78A1: FF         RST         0X38
78A2: 00         NOP
78A3: FF         RST         0X38
78A4: 24         INC         H
78A5: FF         RST         0X38
78A6: 18 FF      JR           $78A7
78A8: 18 FF      JR           $78A9
78AA: 24         INC         H
78AB: FF         RST         0X38
78AC: 00         NOP
78AD: FF         RST         0X38
78AE: 00         NOP
78AF: FF         RST         0X38
78B0: 00         NOP
78B1: FF         RST         0X38
78B2: 00         NOP
78B3: FF         RST         0X38
78B4: 24         INC         H
78B5: FF         RST         0X38
78B6: 18 FF      JR           $78B7
78B8: 18 FF      JR           $78B9
78BA: 24         INC         H
78BB: FF         RST         0X38
78BC: 00         NOP
78BD: FF         RST         0X38
78BE: 00         NOP
78BF: FF         RST         0X38
78C0: 00         NOP
78C1: FF         RST         0X38
78C2: 00         NOP
78C3: FF         RST         0X38
78C4: 24         INC         H
78C5: FF         RST         0X38
78C6: 18 FF      JR           $78C7
78C8: 18 FF      JR           $78C9
78CA: 24         INC         H
78CB: FF         RST         0X38
78CC: 00         NOP
78CD: FF         RST         0X38
78CE: 00         NOP
78CF: FF         RST         0X38
78D0: 00         NOP
78D1: FF         RST         0X38
78D2: 00         NOP
78D3: FF         RST         0X38
78D4: 24         INC         H
78D5: FF         RST         0X38
78D6: 18 FF      JR           $78D7
78D8: 18 FF      JR           $78D9
78DA: 24         INC         H
78DB: FF         RST         0X38
78DC: 00         NOP
78DD: FF         RST         0X38
78DE: 00         NOP
78DF: FF         RST         0X38
78E0: 00         NOP
78E1: FF         RST         0X38
78E2: 00         NOP
78E3: FF         RST         0X38
78E4: 24         INC         H
78E5: FF         RST         0X38
78E6: 18 FF      JR           $78E7
78E8: 18 FF      JR           $78E9
78EA: 24         INC         H
78EB: FF         RST         0X38
78EC: 00         NOP
78ED: FF         RST         0X38
78EE: 00         NOP
78EF: FF         RST         0X38
78F0: 00         NOP
78F1: FF         RST         0X38
78F2: 00         NOP
78F3: FF         RST         0X38
78F4: 24         INC         H
78F5: FF         RST         0X38
78F6: 18 FF      JR           $78F7
78F8: 18 FF      JR           $78F9
78FA: 24         INC         H
78FB: FF         RST         0X38
78FC: 00         NOP
78FD: FF         RST         0X38
78FE: 00         NOP
78FF: FF         RST         0X38
7900: 03         INC         BC
7901: 00         NOP
7902: 04         INC         B
7903: 03         INC         BC
7904: 09         ADD         HL,BC
7905: 07         RLCA
7906: 0B         DEC         BC
7907: 07         RLCA
7908: 0B         DEC         BC
7909: 05         DEC         B
790A: 0B         DEC         BC
790B: 05         DEC         B
790C: 0B         DEC         BC
790D: 05         DEC         B
790E: 0B         DEC         BC
790F: 07         RLCA
7910: 0B         DEC         BC
7911: 07         RLCA
7912: 0B         DEC         BC
7913: 07         RLCA
7914: 05         DEC         B
7915: 03         INC         BC
7916: 04         INC         B
7917: 03         INC         BC
7918: 1C         INC         E
7919: 07         RLCA
791A: 38 1F      JR           C,$793B
791C: 23         INC         HL
791D: 1C         INC         E
791E: 3C         INC         A
791F: 00         NOP
7920: 00         NOP
7921: 00         NOP
7922: 00         NOP
7923: 00         NOP
7924: 07         RLCA
7925: 00         NOP
7926: 08 07 13   LD           ($1307),SP
7929: 0F         RRCA
792A: 13         INC         DE
792B: 0F         RRCA
792C: 13         INC         DE
792D: 0E 09      LD           C,$09
792F: 07         RLCA
7930: 09         ADD         HL,BC
7931: 07         RLCA
7932: 04         INC         B
7933: 03         INC         BC
7934: 1C         INC         E
7935: 03         INC         BC
7936: 2E 19      LD           L,$19
7938: 74         LD           (HL),H
7939: 0F         RRCA
793A: 70         LD           (HL),B
793B: 0F         RRCA
793C: 3F         CCF
793D: 00         NOP
793E: 38 00      JR           C,$7940
7940: 00         NOP
7941: 00         NOP
7942: 00         NOP
7943: 00         NOP
7944: 80         ADD         A,B
7945: 00         NOP
7946: 60         LD           H,B
7947: 80         ADD         A,B
7948: 90         SUB         B
7949: E0 D0      LDFF00   ($D0),A
794B: E0 C8      LDFF00   ($C8),A
794D: B0         OR           B
794E: E8 50      ADD         SP,$50
7950: E8 50      ADD         SP,$50
7952: E8 F0      ADD         SP,$F0
7954: 48         LD           C,B
7955: F0 10      LD           A,($10)
7957: E0 30      LDFF00   ($30),A
7959: C0         RET         NZ
795A: 18 F0      JR           $794C
795C: 8C         ADC         A,H
795D: 78         LD           A,B
795E: 78         LD           A,B
795F: 00         NOP
7960: 20 00      JR           NZ,$7962
7962: 47         LD           B,A
7963: 00         NOP
7964: 48         LD           C,B
7965: 07         RLCA
7966: 11 0F 13   LD           DE,$130F
7969: 0F         RRCA
796A: 13         INC         DE
796B: 0D         DEC         C
796C: 53         LD           D,E
796D: 0D         DEC         C
796E: 2B         DEC         HL
796F: 07         RLCA
7970: 09         ADD         HL,BC
7971: 07         RLCA
7972: 29         ADD         HL,HL
7973: 07         RLCA
7974: 74         LD           (HL),H
7975: 03         INC         BC
7976: 04         INC         B
7977: 03         INC         BC
7978: 1C         INC         E
7979: 07         RLCA
797A: 38 1F      JR           C,$799B
797C: 23         INC         HL
797D: 1C         INC         E
797E: 3C         INC         A
797F: 00         NOP
7980: 80         ADD         A,B
7981: 00         NOP
7982: 40         LD           B,B
7983: 00         NOP
7984: 80         ADD         A,B
7985: 00         NOP
7986: 5C         LD           E,H
7987: 80         ADD         A,B
7988: C8         RET         Z
7989: 80         ADD         A,B
798A: A8         XOR         B
798B: 40         LD           B,B
798C: A0         AND         B
798D: 40         LD           B,B
798E: A0         AND         B
798F: C0         RET         NZ
7990: A0         AND         B
7991: C0         RET         NZ
7992: A4         AND         H
7993: C0         RET         NZ
7994: 28 C0      JR           Z,$7956
7996: 24         INC         H
7997: C0         RET         NZ
7998: 38 E0      JR           C,$797A
799A: 1C         INC         E
799B: F8 C4      LDHL       SP,$C4
799D: 38 3C      JR           C,$79DB
799F: 00         NOP
79A0: 03         INC         BC
79A1: 00         NOP
79A2: 05         DEC         B
79A3: 03         INC         BC
79A4: 05         DEC         B
79A5: 03         INC         BC
79A6: 3E 01      LD           A,$01
79A8: 5D         LD           E,L
79A9: 3E 7F      LD           A,$7F
79AB: 36 5D      LD           (HL),$5D
79AD: 3E 3E      LD           A,$3E
79AF: 01 04 03   LD           BC,$0304
79B2: 04         INC         B
79B3: 03         INC         BC
79B4: 04         INC         B
79B5: 03         INC         BC
79B6: 04         INC         B
79B7: 03         INC         BC
79B8: 18 07      JR           $79C1
79BA: 29         ADD         HL,HL
79BB: 1E 23      LD           E,$23
79BD: 1C         INC         E
79BE: 1E 00      LD           E,$00
79C0: 1E 00      LD           E,$00
79C2: 2D         DEC         L
79C3: 1E 2C      LD           E,$2C
79C5: 1F         RRA
79C6: 20 1F      JR           NZ,$79E7
79C8: 10 0F      STOP       $0F
79CA: 1F         RRA
79CB: 00         NOP
79CC: 3F         CCF
79CD: 1E 7D      LD           E,$7D
79CF: 36 5A      LD           (HL),$5A
79D1: 3D         DEC         A
79D2: 3E 01      LD           A,$01
79D4: 04         INC         B
79D5: 03         INC         BC
79D6: 04         INC         B
79D7: 03         INC         BC
79D8: 18 07      JR           $79E1
79DA: 29         ADD         HL,HL
79DB: 1E 23      LD           E,$23
79DD: 1C         INC         E
79DE: 1E 00      LD           E,$00
79E0: 00         NOP
79E1: 00         NOP
79E2: 38 00      JR           C,$79E4
79E4: F4                              
79E5: 38 F4      JR           C,$79DB
79E7: 58         LD           E,B
79E8: E8 70      ADD         SP,$70
79EA: 90         SUB         B
79EB: 60         LD           H,B
79EC: E0 00      LDFF00   ($00),A
79EE: 20 C0      JR           NZ,$79B0
79F0: 20 C0      JR           NZ,$79B2
79F2: 20 C0      JR           NZ,$79B4
79F4: 20 C0      JR           NZ,$79B6
79F6: 18 E0      JR           $79D8
79F8: 14         INC         D
79F9: F8 C4      LDHL       SP,$C4
79FB: 38 FC      JR           C,$79F9
79FD: 00         NOP
79FE: 38 00      JR           C,$7A00
7A00: 07         RLCA
7A01: 00         NOP
7A02: 18 07      JR           $7A0B
7A04: 0E 01      LD           C,$01
7A06: 0F         RRCA
7A07: 00         NOP
7A08: 1B         DEC         DE
7A09: 0C         INC         C
7A0A: 32         LD           (HLD),A
7A0B: 1D         DEC         E
7A0C: 2A         LD           A,(HLI)
7A0D: 15         DEC         D
7A0E: 4F         LD           C,A
7A0F: 30 58      JR           NC,$7A69
7A11: 27         DAA
7A12: 92         SUB         D
7A13: 6F         LD           L,A
7A14: A7         AND         A
7A15: 5A         LD           E,D
7A16: AE         XOR         (HL)
7A17: 59         LD           E,C
7A18: BC         CP           H
7A19: 43         LD           B,E
7A1A: 65         LD           H,L
7A1B: 03         INC         BC
7A1C: 03         INC         BC
7A1D: 00         NOP
7A1E: 00         NOP
7A1F: 00         NOP
7A20: 81         ADD         A,C
7A21: 00         NOP
7A22: 7E         LD           A,(HL)
7A23: 81         ADD         A,C
7A24: 3C         INC         A
7A25: FF         RST         0X38
7A26: 99         SBC         C
7A27: 7E         LD           A,(HL)
7A28: 5A         LD           E,D
7A29: BD         CP           L
7A2A: 66         LD           H,(HL)
7A2B: DB                              
7A2C: 66         LD           H,(HL)
7A2D: FF         RST         0X38
7A2E: 00         NOP
7A2F: FF         RST         0X38
7A30: FF         RST         0X38
7A31: 42         LD           B,D
7A32: E7         RST         0X20
7A33: 5A         LD           E,D
7A34: C3 BD 7E   JP           $7EBD
7A37: FF         RST         0X38
7A38: 3C         INC         A
7A39: FF         RST         0X38
7A3A: BD         CP           L
7A3B: C3 C3 00   JP           $00C3
7A3E: 00         NOP
7A3F: 00         NOP
7A40: 0E 00      LD           C,$00
7A42: 3F         CCF
7A43: 08 58 37   LD           ($3758),SP
7A46: BE         CP           (HL)
7A47: 41         LD           B,C
7A48: 7F         LD           A,A
7A49: 00         NOP
7A4A: 1F         RRA
7A4B: 00         NOP
7A4C: 06 01      LD           B,$01
7A4E: 02         LD           (BC),A
7A4F: 01 07 00   LD           BC,$0007
7A52: 08 07 12   LD           ($1207),SP
7A55: 0F         RRCA
7A56: 27         DAA
7A57: 1A         LD           A,(DE)
7A58: 2E 19      LD           L,$19
7A5A: 1C         INC         E
7A5B: 03         INC         BC
7A5C: 05         DEC         B
7A5D: 03         INC         BC
7A5E: 03         INC         BC
7A5F: 00         NOP
7A60: 00         NOP
7A61: 00         NOP
7A62: 81         ADD         A,C
7A63: 00         NOP
7A64: 7E         LD           A,(HL)
7A65: 81         ADD         A,C
7A66: 3C         INC         A
7A67: FF         RST         0X38
7A68: 99         SBC         C
7A69: 7E         LD           A,(HL)
7A6A: 5A         LD           E,D
7A6B: BD         CP           L
7A6C: 66         LD           H,(HL)
7A6D: DB                              
7A6E: 66         LD           H,(HL)
7A6F: FF         RST         0X38
7A70: 00         NOP
7A71: FF         RST         0X38
7A72: FF         RST         0X38
7A73: 42         LD           B,D
7A74: E7         RST         0X20
7A75: 5A         LD           E,D
7A76: C3 BD 7E   JP           $7EBD
7A79: FF         RST         0X38
7A7A: 3C         INC         A
7A7B: FF         RST         0X38
7A7C: BD         CP           L
7A7D: C3 C3 00   JP           $00C3
7A80: 03         INC         BC
7A81: 00         NOP
7A82: 04         INC         B
7A83: 03         INC         BC
7A84: 09         ADD         HL,BC
7A85: 06 17      LD           B,$17
7A87: 00         NOP
7A88: 3F         CCF
7A89: 00         NOP
7A8A: 76         HALT
7A8B: 39         ADD         HL,SP
7A8C: 62         LD           H,D
7A8D: 3D         DEC         A
7A8E: 22         LD           (HLI),A
7A8F: 1D         DEC         E
7A90: 11 0E 3D   LD           DE,$3D0E
7A93: 16 27      LD           D,$27
7A95: 1A         LD           A,(DE)
7A96: 2C         INC         L
7A97: 13         INC         DE
7A98: 2E 11      LD           L,$11
7A9A: 2C         INC         L
7A9B: 13         INC         DE
7A9C: 1D         DEC         E
7A9D: 03         INC         BC
7A9E: 13         INC         DE
7A9F: 00         NOP
7AA0: 81         ADD         A,C
7AA1: 00         NOP
7AA2: 7E         LD           A,(HL)
7AA3: 81         ADD         A,C
7AA4: 3C         INC         A
7AA5: FF         RST         0X38
7AA6: DB                              
7AA7: 3C         INC         A
7AA8: 66         LD           H,(HL)
7AA9: DB                              
7AAA: 66         LD           H,(HL)
7AAB: FF         RST         0X38
7AAC: 3C         INC         A
7AAD: C3 FF 42   JP           $42FF
7AB0: FF         RST         0X38
7AB1: 42         LD           B,D
7AB2: 7E         LD           A,(HL)
7AB3: 81         ADD         A,C
7AB4: 66         LD           H,(HL)
7AB5: 99         SBC         C
7AB6: BD         CP           L
7AB7: 42         LD           B,D
7AB8: 42         LD           B,D
7AB9: BD         CP           L
7ABA: 3C         INC         A
7ABB: C3 BD C3   JP           $C3BD
7ABE: C3 00 00   JP           $0000
7AC1: 00         NOP
7AC2: 00         NOP
7AC3: 00         NOP
7AC4: 08 00 18   LD           ($1800),SP
7AC7: 00         NOP
7AC8: 3E 00      LD           A,$00
7ACA: 7F         LD           A,A
7ACB: 06 6F      LD           B,$6F
7ACD: 12         LD           (DE),A
7ACE: CB 37      SWAP        1,E
7AD0: BF         CP           A
7AD1: 75         LD           (HL),L
7AD2: FF         RST         0X38
7AD3: 75         LD           (HL),L
7AD4: FB         EI
7AD5: 67         LD           H,A
7AD6: E7         RST         0X20
7AD7: 42         LD           B,D
7AD8: C7         RST         0X00
7AD9: 02         LD           (BC),A
7ADA: 83         ADD         A,E
7ADB: 00         NOP
7ADC: 00         NOP
7ADD: 00         NOP
7ADE: 00         NOP
7ADF: 00         NOP
7AE0: 00         NOP
7AE1: 00         NOP
7AE2: 02         LD           (BC),A
7AE3: 00         NOP
7AE4: 06 00      LD           B,$00
7AE6: 0E 00      LD           C,$00
7AE8: 0F         RRCA
7AE9: 06 1F      LD           B,$1F
7AEB: 02         LD           (BC),A
7AEC: 1B         DEC         DE
7AED: 07         RLCA
7AEE: 1F         RRA
7AEF: 05         DEC         B
7AF0: 1F         RRA
7AF1: 05         DEC         B
7AF2: 1B         DEC         DE
7AF3: 07         RLCA
7AF4: 1F         RRA
7AF5: 02         LD           (BC),A
7AF6: 1F         RRA
7AF7: 02         LD           (BC),A
7AF8: 0B         DEC         BC
7AF9: 00         NOP
7AFA: 08 00 00   LD           ($0000),SP
7AFD: 00         NOP
7AFE: 00         NOP
7AFF: 00         NOP
7B00: 00         NOP
7B01: 00         NOP
7B02: 00         NOP
7B03: 00         NOP
7B04: 7F         LD           A,A
7B05: 00         NOP
7B06: FD                              
7B07: 7B         LD           A,E
7B08: FB         EI
7B09: 77         LD           (HL),A
7B0A: 8B         ADC         A,E
7B0B: 77         LD           (HL),A
7B0C: F9         LD           SP,HL
7B0D: 77         LD           (HL),A
7B0E: 8C         ADC         A,H
7B0F: 73         LD           (HL),E
7B10: F7         RST         0X30
7B11: 78         LD           A,B
7B12: FB         EI
7B13: 7F         LD           A,A
7B14: 84         ADD         A,H
7B15: 7B         LD           A,E
7B16: FF         RST         0X38
7B17: 00         NOP
7B18: B1         OR           C
7B19: 4E         LD           C,(HL)
7B1A: BF         CP           A
7B1B: 40         LD           B,B
7B1C: 80         ADD         A,B
7B1D: 7F         LD           A,A
7B1E: 7F         LD           A,A
7B1F: 00         NOP
7B20: 3F         CCF
7B21: 00         NOP
7B22: 7F         LD           A,A
7B23: 38 7F      JR           C,$7BA4
7B25: 31 4F 30   LD           SP,$304F
7B28: 7B         LD           A,E
7B29: 34         INC         (HL)
7B2A: 79         LD           A,C
7B2B: 36 4C      LD           (HL),$4C
7B2D: 33         INC         SP
7B2E: 77         LD           (HL),A
7B2F: 38 7B      JR           C,$7BAC
7B31: 3F         CCF
7B32: 7B         LD           A,E
7B33: 3F         CCF
7B34: 44         LD           B,H
7B35: 3B         DEC         SP
7B36: 7F         LD           A,A
7B37: 00         NOP
7B38: 59         LD           E,C
7B39: 26 5F      LD           H,$5F
7B3B: 20 40      JR           NZ,$7B7D
7B3D: 3F         CCF
7B3E: 3F         CCF
7B3F: 00         NOP
7B40: 1F         RRA
7B41: 00         NOP
7B42: 3E 1F      LD           A,$1F
7B44: 7E         LD           A,(HL)
7B45: 2B         DEC         HL
7B46: 7E         LD           A,(HL)
7B47: 2B         DEC         HL
7B48: B6         OR           (HL)
7B49: 7F         LD           A,A
7B4A: 80         ADD         A,B
7B4B: 7F         LD           A,A
7B4C: 81         ADD         A,C
7B4D: 7E         LD           A,(HL)
7B4E: FE 01      CP           $01
7B50: 7E         LD           A,(HL)
7B51: 3F         CCF
7B52: 3C         INC         A
7B53: 03         INC         BC
7B54: 1C         INC         E
7B55: 0F         RRCA
7B56: 39         ADD         HL,SP
7B57: 1E 38      LD           E,$38
7B59: 1F         RRA
7B5A: 2D         DEC         L
7B5B: 1F         RRA
7B5C: 17         RLA
7B5D: 0F         RRCA
7B5E: 3F         CCF
7B5F: 00         NOP
7B60: 80         ADD         A,B
7B61: 00         NOP
7B62: 40         LD           B,B
7B63: 80         ADD         A,B
7B64: 20 C0      JR           NZ,$7B26
7B66: 10 E0      STOP       $E0
7B68: D0         RET         NC
7B69: 20 90      JR           NZ,$7AFB
7B6B: 60         LD           H,B
7B6C: 10 E0      STOP       $E0
7B6E: 20 C0      JR           NZ,$7B30
7B70: 23         INC         HL
7B71: C0         RET         NZ
7B72: 45         LD           B,L
7B73: 82         ADD         A,D
7B74: F5         PUSH       AF
7B75: 02         LD           (BC),A
7B76: 09         ADD         HL,BC
7B77: F6 01      OR           $01
7B79: FE F1      CP           $F1
7B7B: FE 6A      CP           $6A
7B7D: 9C         SBC         H
7B7E: FC                              
7B7F: 00         NOP
7B80: 80         ADD         A,B
7B81: 00         NOP
7B82: 40         LD           B,B
7B83: 80         ADD         A,B
7B84: 20 C0      JR           NZ,$7B46
7B86: 10 E0      STOP       $E0
7B88: D0         RET         NC
7B89: 20 90      JR           NZ,$7B1B
7B8B: 60         LD           H,B
7B8C: 10 E0      STOP       $E0
7B8E: 20 C0      JR           NZ,$7B50
7B90: 20 C0      JR           NZ,$7B52
7B92: 46         LD           B,(HL)
7B93: 80         ADD         A,B
7B94: EA 04 12   LD           ($1204),A
7B97: EC                              
7B98: 04         INC         B
7B99: F8 CC      LDHL       SP,$CC
7B9B: F8 F8      LDHL       SP,$F8
7B9D: 70         LD           (HL),B
7B9E: FC                              
7B9F: 00         NOP
7BA0: 00         NOP
7BA1: FF         RST         0X38
7BA2: 00         NOP
7BA3: FF         RST         0X38
7BA4: 24         INC         H
7BA5: FF         RST         0X38
7BA6: 18 FF      JR           $7BA7
7BA8: 18 FF      JR           $7BA9
7BAA: 24         INC         H
7BAB: FF         RST         0X38
7BAC: 00         NOP
7BAD: FF         RST         0X38
7BAE: 00         NOP
7BAF: FF         RST         0X38
7BB0: 00         NOP
7BB1: FF         RST         0X38
7BB2: 00         NOP
7BB3: FF         RST         0X38
7BB4: 24         INC         H
7BB5: FF         RST         0X38
7BB6: 18 FF      JR           $7BB7
7BB8: 18 FF      JR           $7BB9
7BBA: 24         INC         H
7BBB: FF         RST         0X38
7BBC: 00         NOP
7BBD: FF         RST         0X38
7BBE: 00         NOP
7BBF: FF         RST         0X38
7BC0: 03         INC         BC
7BC1: 03         INC         BC
7BC2: 0C         INC         C
7BC3: 0F         RRCA
7BC4: 13         INC         DE
7BC5: 1C         INC         E
7BC6: 2F         CPL
7BC7: 30 2F      JR           NC,$7BF8
7BC9: 30 5C      JR           NC,$7C27
7BCB: 63         LD           H,E
7BCC: 59         LD           E,C
7BCD: 67         LD           H,A
7BCE: 59         LD           E,C
7BCF: 67         LD           H,A
7BD0: 59         LD           E,C
7BD1: 66         LD           H,(HL)
7BD2: 59         LD           E,C
7BD3: 66         LD           H,(HL)
7BD4: 2C         INC         L
7BD5: 33         INC         SP
7BD6: 2F         CPL
7BD7: 30 13      JR           NC,$7BEC
7BD9: 1C         INC         E
7BDA: 0C         INC         C
7BDB: 0F         RRCA
7BDC: 03         INC         BC
7BDD: 03         INC         BC
7BDE: 00         NOP
7BDF: 00         NOP
7BE0: 00         NOP
7BE1: 0C         INC         C
7BE2: 45         LD           B,L
7BE3: 0B         DEC         BC
7BE4: 16 19      LD           D,$19
7BE6: 37         SCF
7BE7: 38 0F      JR           C,$7BF8
7BE9: F0 7C      LD           A,($7C)
7BEB: 83         ADD         A,E
7BEC: 39         ADD         HL,SP
7BED: 47         LD           B,A
7BEE: 59         LD           E,C
7BEF: 67         LD           H,A
7BF0: D9         RETI
7BF1: 66         LD           H,(HL)
7BF2: 59         LD           E,C
7BF3: 66         LD           H,(HL)
7BF4: 3C         INC         A
7BF5: 43         LD           B,E
7BF6: 7F         LD           A,A
7BF7: 80         ADD         A,B
7BF8: 0F         RRCA
7BF9: F0 36      LD           A,($36)
7BFB: 39         ADD         HL,SP
7BFC: 55         LD           D,L
7BFD: 1B         DEC         DE
7BFE: 00         NOP
7BFF: 0C         INC         C
7C00: F3         DI
7C01: 00         NOP
7C02: 8C         ADC         A,H
7C03: 73         LD           (HL),E
7C04: 54         LD           D,H
7C05: 2B         DEC         HL
7C06: 37         SCF
7C07: 0C         INC         C
7C08: 52         LD           D,D
7C09: 2D         DEC         L
7C0A: F8 07      LDHL       SP,$07
7C0C: FF         RST         0X38
7C0D: 68         LD           L,B
7C0E: DD                              
7C0F: 6B         LD           L,E
7C10: 9B         SBC         E
7C11: 66         LD           H,(HL)
7C12: 77         LD           (HL),A
7C13: 0F         RRCA
7C14: 7D         LD           A,L
7C15: 03         INC         BC
7C16: 73         LD           (HL),E
7C17: 0C         INC         C
7C18: 7F         LD           A,A
7C19: 03         INC         BC
7C1A: 23         INC         HL
7C1B: 1C         INC         E
7C1C: 77         LD           (HL),A
7C1D: 3E 7F      LD           A,$7F
7C1F: 00         NOP
7C20: CF         RST         0X08
7C21: 00         NOP
7C22: 31 CE 2A   LD           SP,$2ACE
7C25: D4 EC 30   CALL       NC,$30EC
7C28: 4A         LD           C,D
7C29: B4         OR           H
7C2A: 19         ADD         HL,DE
7C2B: E6 FD      AND         $FD
7C2D: 12         LD           (DE),A
7C2E: BF         CP           A
7C2F: D0         RET         NC
7C30: DF         RST         0X18
7C31: 66         LD           H,(HL)
7C32: EB                              
7C33: F6 B9      OR           $B9
7C35: C6 EE      ADD         $EE
7C37: 10 FC      STOP       $FC
7C39: E0 F0      LDFF00   ($F0),A
7C3B: 00         NOP
7C3C: F8 00      LDHL       SP,$00
7C3E: C0         RET         NZ
7C3F: 00         NOP
7C40: F3         DI
7C41: 00         NOP
7C42: 8C         ADC         A,H
7C43: 73         LD           (HL),E
7C44: 4F         LD           C,A
7C45: 30 3F      JR           NC,$7C86
7C47: 0F         RRCA
7C48: 3F         CCF
7C49: 10 7F      STOP       $7F
7C4B: 00         NOP
7C4C: BF         CP           A
7C4D: 40         LD           B,B
7C4E: BF         CP           A
7C4F: 40         LD           B,B
7C50: AF         XOR         A
7C51: 50         LD           D,B
7C52: 60         LD           H,B
7C53: 1F         RRA
7C54: 30 0F      JR           NC,$7C65
7C56: 3F         CCF
7C57: 00         NOP
7C58: 3F         CCF
7C59: 00         NOP
7C5A: 23         INC         HL
7C5B: 1C         INC         E
7C5C: 41         LD           B,C
7C5D: 3E 7F      LD           A,$7F
7C5F: 00         NOP
7C60: CF         RST         0X08
7C61: 00         NOP
7C62: 31 CE E2   LD           SP,$E2CE
7C65: 1C         INC         E
7C66: F4                              
7C67: E8 FE      ADD         SP,$FE
7C69: 14         INC         D
7C6A: FF         RST         0X38
7C6B: 06 FB      LD           B,$FB
7C6D: 06 F9      LD           B,$F9
7C6F: 06 E9      LD           B,$E9
7C71: 16 0F      LD           D,$0F
7C73: F0 1C      LD           A,($1C)
7C75: E0 FC      LDFF00   ($FC),A
7C77: 00         NOP
7C78: FC                              
7C79: 00         NOP
7C7A: F8 00      LDHL       SP,$00
7C7C: FC                              
7C7D: 00         NOP
7C7E: 00         NOP
7C7F: 00         NOP
7C80: 0F         RRCA
7C81: 00         NOP
7C82: F0 0F      LD           A,($0F)
7C84: D6 29      SUB         $29
7C86: 8E         ADC         A,(HL)
7C87: 73         LD           (HL),E
7C88: 81         ADD         A,C
7C89: 7E         LD           A,(HL)
7C8A: 83         ADD         A,E
7C8B: 7D         LD           A,L
7C8C: 77         LD           (HL),A
7C8D: 0B         DEC         BC
7C8E: 7F         LD           A,A
7C8F: 32         LD           (HLD),A
7C90: 5F         LD           E,A
7C91: 38 37      JR           C,$7CCA
7C93: 08 1E 07   LD           ($071E),SP
7C96: 1C         INC         E
7C97: 07         RLCA
7C98: 08 07 07   LD           ($0707),SP
7C9B: 00         NOP
7C9C: 03         INC         BC
7C9D: 01 07 00   LD           BC,$0007
7CA0: E0 00      LDFF00   ($00),A
7CA2: 10 E0      STOP       $E0
7CA4: 68         LD           L,B
7CA5: 90         SUB         B
7CA6: 1C         INC         E
7CA7: E0 8E      LDFF00   ($8E),A
7CA9: 74         LD           (HL),H
7CAA: BE         CP           (HL)
7CAB: 48         LD           C,B
7CAC: FF         RST         0X38
7CAD: 30 FF      JR           NC,$7CAE
7CAF: 00         NOP
7CB0: EF         RST         0X28
7CB1: 70         LD           (HL),B
7CB2: 07         RLCA
7CB3: FA 87 7A   LD           A,($7A87)
7CB6: 07         RLCA
7CB7: F8 8F      LDHL       SP,$8F
7CB9: 70         LD           (HL),B
7CBA: FC                              
7CBB: 00         NOP
7CBC: 86         ADD         A,(HL)
7CBD: F8 FE      LDHL       SP,$FE
7CBF: 00         NOP
7CC0: 00         NOP
7CC1: 00         NOP
7CC2: 0F         RRCA
7CC3: 00         NOP
7CC4: F0 0F      LD           A,($0F)
7CC6: D6 29      SUB         $29
7CC8: 8E         ADC         A,(HL)
7CC9: 73         LD           (HL),E
7CCA: 81         ADD         A,C
7CCB: 7E         LD           A,(HL)
7CCC: 83         ADD         A,E
7CCD: 7D         LD           A,L
7CCE: 77         LD           (HL),A
7CCF: 0B         DEC         BC
7CD0: 7F         LD           A,A
7CD1: 32         LD           (HLD),A
7CD2: 5F         LD           E,A
7CD3: 38 37      JR           C,$7D0C
7CD5: 0B         DEC         BC
7CD6: 1E 03      LD           E,$03
7CD8: 1C         INC         E
7CD9: 03         INC         BC
7CDA: 0F         RRCA
7CDB: 00         NOP
7CDC: 1C         INC         E
7CDD: 0F         RRCA
7CDE: 1F         RRA
7CDF: 00         NOP
7CE0: 00         NOP
7CE1: 00         NOP
7CE2: E0 00      LDFF00   ($00),A
7CE4: 10 E0      STOP       $E0
7CE6: 68         LD           L,B
7CE7: 90         SUB         B
7CE8: 1C         INC         E
7CE9: E0 8E      LDFF00   ($8E),A
7CEB: 74         LD           (HL),H
7CEC: FE 08      CP           $08
7CEE: FF         RST         0X38
7CEF: 30 FF      JR           NC,$7CF0
7CF1: 00         NOP
7CF2: BF         CP           A
7CF3: 70         LD           (HL),B
7CF4: 47         LD           B,A
7CF5: BA         CP           D
7CF6: 07         RLCA
7CF7: FA 4F B0   LD           A,($B04F)
7CFA: F9         LD           SP,HL
7CFB: 06 79      LD           B,$79
7CFD: 9E         SBC         (HL)
7CFE: FE 00      CP           $00
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
7D14: 0D         DEC         C
7D15: 00         NOP
7D16: 7F         LD           A,A
7D17: 05         DEC         B
7D18: B7         OR           A
7D19: 78         LD           A,B
7D1A: B1         OR           C
7D1B: 4E         LD           C,(HL)
7D1C: B8         CP           B
7D1D: 47         LD           B,A
7D1E: 7C         LD           A,H
7D1F: 03         INC         BC
7D20: 00         NOP
7D21: 00         NOP
7D22: 00         NOP
7D23: 00         NOP
7D24: 00         NOP
7D25: 00         NOP
7D26: 00         NOP
7D27: 00         NOP
7D28: 00         NOP
7D29: 00         NOP
7D2A: 00         NOP
7D2B: 00         NOP
7D2C: 00         NOP
7D2D: 00         NOP
7D2E: 00         NOP
7D2F: 00         NOP
7D30: 00         NOP
7D31: 00         NOP
7D32: 00         NOP
7D33: 00         NOP
7D34: C0         RET         NZ
7D35: 00         NOP
7D36: E0 C0      LDFF00   ($C0),A
7D38: E0 40      LDFF00   ($40),A
7D3A: E0 C0      LDFF00   ($C0),A
7D3C: D0         RET         NC
7D3D: 20 10      JR           NZ,$7D4F
7D3F: E0 7E      LDFF00   ($7E),A
7D41: 01 3E 01   LD           BC,$013E
7D44: 3F         CCF
7D45: 00         NOP
7D46: 3F         CCF
7D47: 00         NOP
7D48: 3F         CCF
7D49: 00         NOP
7D4A: 3F         CCF
7D4B: 00         NOP
7D4C: 3F         CCF
7D4D: 01 5E 23   LD           BC,$235E
7D50: 7D         LD           A,L
7D51: 26 5B      LD           H,$5B
7D53: 3D         DEC         A
7D54: FF         RST         0X38
7D55: 43         LD           B,E
7D56: AF         XOR         A
7D57: 57         LD           D,A
7D58: 78         LD           A,B
7D59: 17         RLA
7D5A: 75         LD           (HL),L
7D5B: 1A         LD           A,(DE)
7D5C: FF         RST         0X38
7D5D: 6D         LD           L,L
7D5E: FF         RST         0X38
7D5F: 00         NOP
7D60: 68         LD           L,B
7D61: 90         SUB         B
7D62: 68         LD           L,B
7D63: 90         SUB         B
7D64: 08 F0 04   LD           ($04F0),SP
7D67: F8 04      LDHL       SP,$04
7D69: F8 04      LDHL       SP,$04
7D6B: F8 02      LDHL       SP,$02
7D6D: FC                              
7D6E: 8A         ADC         A,D
7D6F: 74         LD           (HL),H
7D70: 8A         ADC         A,D
7D71: F4                              
7D72: CE F0      ADC         $F0
7D74: CB F6      SET         1,E
7D76: D1         POP         DE
7D77: 6E         LD           L,(HL)
7D78: D2 6C FE   JP           NC,$FE6C
7D7B: C8         RET         Z
7D7C: FF         RST         0X38
7D7D: 8E         ADC         A,(HL)
7D7E: FF         RST         0X38
7D7F: 00         NOP
7D80: 0E 00      LD           C,$00
7D82: 1F         RRA
7D83: 0E 1F      LD           C,$1F
7D85: 0A         LD           A,(BC)
7D86: 1E 0D      LD           E,$0D
7D88: 2C         INC         L
7D89: 13         INC         DE
7D8A: 40         LD           B,B
7D8B: 3F         CCF
7D8C: 51         LD           D,C
7D8D: 2F         CPL
7D8E: 78         LD           A,B
7D8F: 17         RLA
7D90: 3F         CCF
7D91: 08 5F 27   LD           ($275F),SP
7D94: D7         RST         0X10
7D95: 68         LD           L,B
7D96: 93         SUB         E
7D97: 6D         LD           L,L
7D98: 5B         LD           E,E
7D99: 2D         DEC         L
7D9A: 7A         LD           A,D
7D9B: 0D         DEC         C
7D9C: EF         RST         0X28
7D9D: 76         HALT
7D9E: FF         RST         0X38
7D9F: 00         NOP
7DA0: 0E 00      LD           C,$00
7DA2: 1F         RRA
7DA3: 0E 1F      LD           C,$1F
7DA5: 0A         LD           A,(BC)
7DA6: 1E 0D      LD           E,$0D
7DA8: 2C         INC         L
7DA9: 13         INC         DE
7DAA: 40         LD           B,B
7DAB: 3F         CCF
7DAC: 51         LD           D,C
7DAD: 2F         CPL
7DAE: 58         LD           E,B
7DAF: 37         SCF
7DB0: 3F         CCF
7DB1: 18 6F      JR           $7E22
7DB3: 1F         RRA
7DB4: D7         RST         0X10
7DB5: 6F         LD           L,A
7DB6: 98         SBC         B
7DB7: 67         LD           H,A
7DB8: 5F         LD           E,A
7DB9: 28 7A      JR           Z,$7E35
7DBB: 0D         DEC         C
7DBC: EF         RST         0X28
7DBD: 76         HALT
7DBE: FF         RST         0X38
7DBF: 00         NOP
7DC0: 1B         DEC         DE
7DC1: 00         NOP
7DC2: 3F         CCF
7DC3: 1B         DEC         DE
7DC4: 3F         CCF
7DC5: 09         ADD         HL,BC
7DC6: 3F         CCF
7DC7: 1B         DEC         DE
7DC8: 5B         LD           E,E
7DC9: 24         INC         H
7DCA: 80         ADD         A,B
7DCB: 7F         LD           A,A
7DCC: 98         SBC         B
7DCD: 7F         LD           A,A
7DCE: 81         ADD         A,C
7DCF: 7E         LD           A,(HL)
7DD0: 7E         LD           A,(HL)
7DD1: 01 7F 3F   LD           BC,$3F7F
7DD4: FF         RST         0X38
7DD5: 41         LD           B,C
7DD6: A7         AND         A
7DD7: 5B         LD           E,E
7DD8: 77         LD           (HL),A
7DD9: 1B         DEC         DE
7DDA: 74         LD           (HL),H
7DDB: 1B         DEC         DE
7DDC: FF         RST         0X38
7DDD: 6C         LD           L,H
7DDE: FF         RST         0X38
7DDF: 00         NOP
7DE0: 80         ADD         A,B
7DE1: 00         NOP
7DE2: E0 80      LDFF00   ($80),A
7DE4: D0         RET         NC
7DE5: A0         AND         B
7DE6: D8         RET         C
7DE7: A0         AND         B
7DE8: 84         ADD         A,H
7DE9: 78         LD           A,B
7DEA: 34         INC         (HL)
7DEB: C8         RET         Z
7DEC: 34         INC         (HL)
7DED: C8         RET         Z
7DEE: 84         ADD         A,H
7DEF: 78         LD           A,B
7DF0: CC F0 D2   CALL       Z,$D2F0
7DF3: EC                              
7DF4: 93         SUB         E
7DF5: 6E         LD           L,(HL)
7DF6: 91         SUB         C
7DF7: 6E         LD           L,(HL)
7DF8: B2         OR           D
7DF9: 6C         LD           L,H
7DFA: B6         OR           (HL)
7DFB: 68         LD           L,B
7DFC: F7         RST         0X30
7DFD: CE FF      ADC         $FF
7DFF: 00         NOP
7E00: 00         NOP
7E01: 00         NOP
7E02: 00         NOP
7E03: 00         NOP
7E04: 00         NOP
7E05: 00         NOP
7E06: 00         NOP
7E07: 00         NOP
7E08: 00         NOP
7E09: 00         NOP
7E0A: 00         NOP
7E0B: 00         NOP
7E0C: 01 00 02   LD           BC,$0200
7E0F: 01 0D 03   LD           BC,$030D
7E12: 14         INC         D
7E13: 0F         RRCA
7E14: 29         ADD         HL,HL
7E15: 1E 21      LD           E,$21
7E17: 1E 20      LD           E,$20
7E19: 1F         RRA
7E1A: 13         INC         DE
7E1B: 0C         INC         C
7E1C: 0C         INC         C
7E1D: 03         INC         BC
7E1E: 05         DEC         B
7E1F: 03         INC         BC
7E20: 00         NOP
7E21: 00         NOP
7E22: 00         NOP
7E23: 00         NOP
7E24: 18 00      JR           $7E26
7E26: 3D         DEC         A
7E27: 18 7F      JR           $7EA8
7E29: 2D         DEC         L
7E2A: 7F         LD           A,A
7E2B: 35         DEC         (HL)
7E2C: FF         RST         0X38
7E2D: 39         ADD         HL,SP
7E2E: 39         ADD         HL,SP
7E2F: C6 80      ADD         $80
7E31: FF         RST         0X38
7E32: 00         NOP
7E33: FF         RST         0X38
7E34: 60         LD           H,B
7E35: 9F         SBC         A
7E36: 40         LD           B,B
7E37: BF         CP           A
7E38: 00         NOP
7E39: FF         RST         0X38
7E3A: 80         ADD         A,B
7E3B: 7F         LD           A,A
7E3C: 63         LD           H,E
7E3D: 9C         SBC         H
7E3E: DD                              
7E3F: E3                              
7E40: 07         RLCA
7E41: 00         NOP
7E42: 0F         RRCA
7E43: 06 FE      LD           B,$FE
7E45: 05         DEC         B
7E46: FF         RST         0X38
7E47: E1         POP         HL
7E48: FD                              
7E49: D6 FA      SUB         $FA
7E4B: B7         OR           A
7E4C: F8 67      LDHL       SP,$67
7E4E: EC                              
7E4F: DF         RST         0X18
7E50: D8         RET         C
7E51: 3F         CCF
7E52: 00         NOP
7E53: FF         RST         0X38
7E54: 1C         INC         E
7E55: E3                              
7E56: 2A         LD           A,(HLI)
7E57: D5         PUSH       DE
7E58: 7E         LD           A,(HL)
7E59: 95         SUB         L
7E5A: BC         CP           H
7E5B: 53         LD           D,E
7E5C: F6 0F      OR           $0F
7E5E: FD                              
7E5F: FE 00      CP           $00
7E61: 00         NOP
7E62: F0 00      LD           A,($00)
7E64: F0 E0      LD           A,($E0)
7E66: F0 E0      LD           A,($E0)
7E68: D8         RET         C
7E69: E0 B8      LDFF00   ($B8),A
7E6B: 50         LD           D,B
7E6C: 8C         ADC         A,H
7E6D: 70         LD           (HL),B
7E6E: 76         HALT
7E6F: 8C         ADC         A,H
7E70: 33         INC         SP
7E71: CE 3B      ADC         $3B
7E73: C6 3B      ADD         $3B
7E75: C6 37      ADD         $37
7E77: CE 7D      ADC         $7D
7E79: 9E         SBC         (HL)
7E7A: 76         HALT
7E7B: B8         CP           B
7E7C: DC 60 B8   CALL       C,$B860
7E7F: C0         RET         NZ
7E80: 06 01      LD           B,$01
7E82: 1F         RRA
7E83: 00         NOP
7E84: 27         DAA
7E85: 1C         INC         E
7E86: 4B         LD           C,E
7E87: 36 4F      LD           (HL),$4F
7E89: 30 4F      JR           NC,$7EDA
7E8B: 3C         INC         A
7E8C: 4E         LD           C,(HL)
7E8D: 31 2F 1D   LD           SP,$1D2F
7E90: 3D         DEC         A
7E91: 03         INC         BC
7E92: 25         DEC         H
7E93: 1B         DEC         DE
7E94: 23         INC         HL
7E95: 1D         DEC         E
7E96: 12         LD           (DE),A
7E97: 0D         DEC         C
7E98: 1F         RRA
7E99: 00         NOP
7E9A: 3F         CCF
7E9B: 16 7C      LD           D,$7C
7E9D: 2F         CPL
7E9E: 7F         LD           A,A
7E9F: 00         NOP
7EA0: FF         RST         0X38
7EA1: FF         RST         0X38
7EA2: 7F         LD           A,A
7EA3: FF         RST         0X38
7EA4: BF         CP           A
7EA5: 7F         LD           A,A
7EA6: E0 1F      LDFF00   ($1F),A
7EA8: 7F         LD           A,A
7EA9: C0         RET         NZ
7EAA: 3F         CCF
7EAB: DC FF 3E   CALL       C,$3EFF
7EAE: 7F         LD           A,A
7EAF: BE         CP           (HL)
7EB0: FF         RST         0X38
7EB1: BE         CP           (HL)
7EB2: FE DD      CP           $DD
7EB4: FD                              
7EB5: E3                              
7EB6: FF         RST         0X38
7EB7: FF         RST         0X38
7EB8: 7F         LD           A,A
7EB9: FF         RST         0X38
7EBA: 9E         SBC         (HL)
7EBB: 7F         LD           A,A
7EBC: FF         RST         0X38
7EBD: 00         NOP
7EBE: FF         RST         0X38
7EBF: 00         NOP
7EC0: FB         EI
7EC1: FD                              
7EC2: EF         RST         0X28
7EC3: F1         POP         AF
7EC4: 37         SCF
7EC5: C8         RET         Z
7EC6: E6 1B      AND         $1B
7EC8: BE         CP           (HL)
7EC9: C7         RST         0X00
7ECA: 3E C1      LD           A,$C1
7ECC: DC 2B 5C   CALL       C,$5C2B
7ECF: EF         RST         0X28
7ED0: 6E         LD           L,(HL)
7ED1: F1         POP         AF
7ED2: EE F7      XOR         $F7
7ED4: EF         RST         0X28
7ED5: F0 C8      LD           A,($C8)
7ED7: F7         RST         0X30
7ED8: 97         SUB         A
7ED9: E8 2F      ADD         SP,$2F
7EDB: D6 F3      SUB         $F3
7EDD: 0F         RRCA
7EDE: FF         RST         0X38
7EDF: 00         NOP
7EE0: 7C         LD           A,H
7EE1: 80         ADD         A,B
7EE2: 4C         LD           C,H
7EE3: B0         OR           B
7EE4: 9C         SBC         H
7EE5: 78         LD           A,B
7EE6: CA 3C 42   JP           Z,$423C
7EE9: BC         CP           H
7EEA: 02         LD           (BC),A
7EEB: FC                              
7EEC: 02         LD           (BC),A
7EED: FC                              
7EEE: 26 D8      LD           H,$D8
7EF0: 3E C0      LD           A,$C0
7EF2: 7C         LD           A,H
7EF3: 80         ADD         A,B
7EF4: FC                              
7EF5: 40         LD           B,B
7EF6: FF         RST         0X38
7EF7: 60         LD           H,B
7EF8: BD         CP           L
7EF9: 72         LD           (HL),D
7EFA: DF         RST         0X18
7EFB: BA         CP           D
7EFC: EF         RST         0X28
7EFD: 5E         LD           E,(HL)
7EFE: FE 00      CP           $00
7F00: 00         NOP
7F01: 00         NOP
7F02: 00         NOP
7F03: 00         NOP
7F04: 00         NOP
7F05: 00         NOP
7F06: 00         NOP
7F07: 00         NOP
7F08: 00         NOP
7F09: 00         NOP
7F0A: 03         INC         BC
7F0B: 00         NOP
7F0C: 0D         DEC         C
7F0D: 03         INC         BC
7F0E: 3A         LD           A,(HLD)
7F0F: 0D         DEC         C
7F10: 52         LD           D,D
7F11: 3D         DEC         A
7F12: 40         LD           B,B
7F13: 3F         CCF
7F14: 43         LD           B,E
7F15: 3C         INC         A
7F16: 24         INC         H
7F17: 1B         DEC         DE
7F18: 17         RLA
7F19: 0B         DEC         BC
7F1A: 0F         RRCA
7F1B: 03         INC         BC
7F1C: 07         RLCA
7F1D: 00         NOP
7F1E: 04         INC         B
7F1F: 03         INC         BC
7F20: 00         NOP
7F21: 00         NOP
7F22: 18 00      JR           $7F24
7F24: 3D         DEC         A
7F25: 18 7F      JR           $7FA6
7F27: 2D         DEC         L
7F28: 7F         LD           A,A
7F29: 35         DEC         (HL)
7F2A: FF         RST         0X38
7F2B: 09         ADD         HL,BC
7F2C: E9         JP           (HL)
7F2D: F6 60      OR           $60
7F2F: 9F         SBC         A
7F30: 40         LD           B,B
7F31: BF         CP           A
7F32: 00         NOP
7F33: FF         RST         0X38
7F34: E0 1F      LDFF00   ($1F),A
7F36: 9C         SBC         H
7F37: 63         LD           H,E
7F38: FA 6D FD   LD           A,($FD6D)
7F3B: 6E         LD           L,(HL)
7F3C: FF         RST         0X38
7F3D: 00         NOP
7F3E: FE FF      CP           $FF
7F40: 07         RLCA
7F41: 00         NOP
7F42: FF         RST         0X38
7F43: 06 FE      LD           B,$FE
7F45: E5         PUSH       HL
7F46: FF         RST         0X38
7F47: D1         POP         DE
7F48: F9         LD           SP,HL
7F49: B6         OR           (HL)
7F4A: FC                              
7F4B: 6F         LD           L,A
7F4C: FC                              
7F4D: DF         RST         0X18
7F4E: D0         RET         NC
7F4F: 3F         CCF
7F50: 06 F9      LD           B,$F9
7F52: 04         INC         B
7F53: FB         EI
7F54: 02         LD           (BC),A
7F55: FD                              
7F56: 02         LD           (BC),A
7F57: FD                              
7F58: 02         LD           (BC),A
7F59: FD                              
7F5A: 04         INC         B
7F5B: FB         EI
7F5C: 8E         ADC         A,(HL)
7F5D: 73         LD           (HL),E
7F5E: FD                              
7F5F: 0E 00      LD           C,$00
7F61: 00         NOP
7F62: F0 00      LD           A,($00)
7F64: F0 E0      LD           A,($E0)
7F66: F0 E0      LD           A,($E0)
7F68: D8         RET         C
7F69: E0 B8      LDFF00   ($B8),A
7F6B: 50         LD           D,B
7F6C: 8C         ADC         A,H
7F6D: 70         LD           (HL),B
7F6E: 76         HALT
7F6F: 8C         ADC         A,H
7F70: 33         INC         SP
7F71: CE 3B      ADC         $3B
7F73: C6 3B      ADD         $3B
7F75: C6 37      ADD         $37
7F77: CE 7D      ADC         $7D
7F79: 9E         SBC         (HL)
7F7A: 76         HALT
7F7B: B8         CP           B
7F7C: DC 60 B8   CALL       C,$B860
7F7F: C0         RET         NZ
7F80: 07         RLCA
7F81: 00         NOP
7F82: 08 07 16   LD           ($1607),SP
7F85: 0F         RRCA
7F86: 10 0F      STOP       $0F
7F88: 10 0F      STOP       $0F
7F8A: 10 0F      STOP       $0F
7F8C: 09         ADD         HL,BC
7F8D: 06 07      LD           B,$07
7F8F: 01 05 02   LD           BC,$0205
7F92: 02         LD           (BC),A
7F93: 01 02 01   LD           BC,$0102
7F96: 02         LD           (BC),A
7F97: 01 02 01   LD           BC,$0102
7F9A: 05         DEC         B
7F9B: 03         INC         BC
7F9C: 07         RLCA
7F9D: 03         INC         BC
7F9E: 05         DEC         B
7F9F: 03         INC         BC
7FA0: 0E 00      LD           C,$00
7FA2: DF         RST         0X18
7FA3: 0E 3F      LD           C,$3F
7FA5: C8         RET         Z
7FA6: 09         ADD         HL,BC
7FA7: F6 00      OR           $00
7FA9: FF         RST         0X38
7FAA: E0 1F      LDFF00   ($1F),A
7FAC: F0 AF      LD           A,($AF)
7FAE: FC                              
7FAF: B3         OR           E
7FB0: FF         RST         0X38
7FB1: 00         NOP
7FB2: FF         RST         0X38
7FB3: 00         NOP
7FB4: FF         RST         0X38
7FB5: 00         NOP
7FB6: C4 3B B7   CALL       NZ,$B73B
7FB9: 7F         LD           A,A
7FBA: A6         AND         (HL)
7FBB: 7F         LD           A,A
7FBC: 90         SUB         B
7FBD: 6F         LD           L,A
7FBE: FF         RST         0X38
7FBF: 80         ADD         A,B
7FC0: 78         LD           A,B
7FC1: 00         NOP
7FC2: FC                              
7FC3: 78         LD           A,B
7FC4: FF         RST         0X38
7FC5: C4 FD BA   CALL       NZ,$BAFD
7FC8: FE 67      CP           $67
7FCA: 6C         LD           L,H
7FCB: 9F         SBC         A
7FCC: 00         NOP
7FCD: FF         RST         0X38
7FCE: 00         NOP
7FCF: FF         RST         0X38
7FD0: E0 1F      LDFF00   ($1F),A
7FD2: F8 07      LDHL       SP,$07
7FD4: FC                              
7FD5: 03         INC         BC
7FD6: 7C         LD           A,H
7FD7: 83         ADD         A,E
7FD8: 3C         INC         A
7FD9: C3 1C E3   JP           $E31C
7FDC: 76         HALT
7FDD: 8F         ADC         A,A
7FDE: BD         CP           L
7FDF: 7E         LD           A,(HL)
7FE0: 00         NOP
7FE1: 00         NOP
7FE2: E0 00      LDFF00   ($00),A
7FE4: 60         LD           H,B
7FE5: C0         RET         NZ
7FE6: FC                              
7FE7: C0         RET         NZ
7FE8: FC                              
7FE9: 38 FC      JR           C,$7FE7
7FEB: 78         LD           A,B
7FEC: FE 30      CP           $30
7FEE: 5E         LD           E,(HL)
7FEF: AC         XOR         H
7FF0: 22         LD           (HLI),A
7FF1: DC 3F C0   CALL       C,$C03F
7FF4: 1F         RRA
7FF5: E2         LDFF00   (C),A
7FF6: 1B         DEC         DE
7FF7: E6 1B      AND         $1B
7FF9: E6 35      AND         $35
7FFB: CE DA      ADC         $DA
7FFD: 3C         INC         A
7FFE: F4                              
7FFF: F8
```
