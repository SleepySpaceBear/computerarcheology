![Bank 04](GBZelda.jpg)

# Bank 04

>>> cpu Z80GB

>>> binary 4000:zelda.gb[10000:14000]

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

```code
4000: 21 00 C2   LD           HL,$C200
4003: 09         ADD         HL,BC
4004: 7E         LD           A,(HL)
4005: C6 08      ADD         $08
4007: 77         LD           (HL),A
4008: C9         RET
4009: CD 0E 38   CALL       $380E
400C: CD 12 3F   CALL       $3F12
400F: 21 B0 C2   LD           HL,$C2B0
4012: 09         ADD         HL,BC
4013: 7E         LD           A,(HL)
4014: C7         RST         0X00
4015: 1F         RRA
4016: 40         LD           B,B
4017: D2 42 33   JP           NC,$3342
401A: 48         LD           C,B
401B: D0         RET         NC
401C: 48         LD           C,B
401D: 36 49      LD           (HL),$49
401F: 21 40 C4   LD           HL,$C440
4022: 09         ADD         HL,BC
4023: 7E         LD           A,(HL)
4024: FE 03      CP           $03
4026: 38 2F      JR           C,$4057
4028: 3E 5C      LD           A,$5C
402A: CD 01 3C   CALL       $3C01
402D: F0 D7      LD           A,($D7)
402F: 21 00 C2   LD           HL,$C200
4032: 19         ADD         HL,DE
4033: 77         LD           (HL),A
4034: F0 D8      LD           A,($D8)
4036: 21 10 C2   LD           HL,$C210
4039: 19         ADD         HL,DE
403A: D6 18      SUB         $18
403C: 77         LD           (HL),A
403D: 21 B0 C2   LD           HL,$C2B0
4040: 19         ADD         HL,DE
4041: 36 02      LD           (HL),$02
4043: 21 E0 C2   LD           HL,$C2E0
4046: 19         ADD         HL,DE
4047: 36 27      LD           (HL),$27
4049: 21 60 C3   LD           HL,$C360
404C: 19         ADD         HL,DE
404D: 36 08      LD           (HL),$08
404F: CD 64 3E   CALL       $3E64
4052: 3E 29      LD           A,$29
4054: E0 F4      LDFF00   ($F4),A
4056: C9         RET
4057: 21 60 C3   LD           HL,$C360
405A: 09         ADD         HL,BC
405B: 36 20      LD           (HL),$20
405D: 79         LD           A,C
405E: EA 02 D0   LD           ($D002),A
4061: CD 9C 42   CALL       $429C
4064: CD 1F 7F   CALL       $7F1F
4067: 21 40 C3   LD           HL,$C340
406A: 09         ADD         HL,BC
406B: 36 81      LD           (HL),$81
406D: 21 50 C3   LD           HL,$C350
4070: 09         ADD         HL,BC
4071: 36 80      LD           (HL),$80
4073: CD CD 6D   CALL       $6DCD
4076: 21 20 C3   LD           HL,$C320
4079: 09         ADD         HL,BC
407A: 35         DEC         (HL)
407B: 35         DEC         (HL)
407C: 21 10 C3   LD           HL,$C310
407F: 09         ADD         HL,BC
4080: 7E         LD           A,(HL)
4081: E0 E8      LDFF00   ($E8),A
4083: E6 80      AND         $80
4085: 28 07      JR           Z,$408E
4087: AF         XOR         A
4088: 77         LD           (HL),A
4089: 21 20 C3   LD           HL,$C320
408C: 09         ADD         HL,BC
408D: 70         LD           (HL),B
408E: F0 F0      LD           A,($F0)
4090: C7         RST         0X00
4091: 99         SBC         C
4092: 40         LD           B,B
4093: AC         XOR         H
4094: 40         LD           B,B
4095: 5F         LD           E,A
4096: 41         LD           B,C
4097: FD                              
4098: 41         LD           B,C
4099: F0 99      LD           A,($99)
409B: FE 70      CP           $70
409D: 30 08      JR           NC,$40A7
409F: CD 8D 3B   CALL       $3B8D
40A2: CD 91 08   CALL       $0891
40A5: 36 FF      LD           (HL),$FF
40A7: C9         RET
40A8: 00         NOP
40A9: 01 00 02   LD           BC,$0200
40AC: CD E2 08   CALL       $08E2
40AF: CD EB 3B   CALL       $3BEB
40B2: CD BF 3B   CALL       $3BBF
40B5: 30 19      JR           NC,$40D0
40B7: CD 42 09   CALL       $0942
40BA: 3E 09      LD           A,$09
40BC: E0 F2      LDFF00   ($F2),A
40BE: 3E 10      LD           A,$10
40C0: EA 3E C1   LD           ($C13E),A
40C3: 3E 14      LD           A,$14
40C5: CD 30 3C   CALL       $3C30
40C8: F0 D7      LD           A,($D7)
40CA: E0 9B      LDFF00   ($9B),A
40CC: F0 D8      LD           A,($D8)
40CE: E0 9A      LDFF00   ($9A),A
40D0: 21 D0 C2   LD           HL,$C2D0
40D3: 09         ADD         HL,BC
40D4: 7E         LD           A,(HL)
40D5: A7         AND         A
40D6: 20 49      JR           NZ,$4121
40D8: F0 E8      LD           A,($E8)
40DA: E6 80      AND         $80
40DC: 28 0A      JR           Z,$40E8
40DE: 21 20 C3   LD           HL,$C320
40E1: 09         ADD         HL,BC
40E2: 36 10      LD           (HL),$10
40E4: 3E 20      LD           A,$20
40E6: E0 F2      LDFF00   ($F2),A
40E8: F0 98      LD           A,($98)
40EA: F5         PUSH       AF
40EB: 3E 50      LD           A,$50
40ED: E0 98      LDFF00   ($98),A
40EF: F0 99      LD           A,($99)
40F1: F5         PUSH       AF
40F2: 3E 48      LD           A,$48
40F4: E0 99      LDFF00   ($99),A
40F6: 3E 08      LD           A,$08
40F8: CD 25 3C   CALL       $3C25
40FB: F0 EE      LD           A,($EE)
40FD: 21 98 FF   LD           HL,$FF98
4100: 96         SUB         (HL)
4101: C6 02      ADD         $02
4103: FE 04      CP           $04
4105: 30 11      JR           NC,$4118
4107: F0 EF      LD           A,($EF)
4109: 21 99 FF   LD           HL,$FF99
410C: 96         SUB         (HL)
410D: C6 02      ADD         $02
410F: FE 04      CP           $04
4111: 30 05      JR           NC,$4118
4113: 21 D0 C2   LD           HL,$C2D0
4116: 09         ADD         HL,BC
4117: 34         INC         (HL)
4118: F1         POP         AF
4119: E0 99      LDFF00   ($99),A
411B: F1         POP         AF
411C: E0 98      LDFF00   ($98),A
411E: CD 94 6D   CALL       $6D94
4121: CD 91 08   CALL       $0891
4124: FE 01      CP           $01
4126: 20 25      JR           NZ,$414D
4128: 3E 5C      LD           A,$5C
412A: CD 01 3C   CALL       $3C01
412D: F0 D7      LD           A,($D7)
412F: 21 00 C2   LD           HL,$C200
4132: 19         ADD         HL,DE
4133: 77         LD           (HL),A
4134: F0 D8      LD           A,($D8)
4136: 21 10 C2   LD           HL,$C210
4139: 19         ADD         HL,DE
413A: D6 26      SUB         $26
413C: 77         LD           (HL),A
413D: 21 B0 C2   LD           HL,$C2B0
4140: 19         ADD         HL,DE
4141: 36 02      LD           (HL),$02
4143: 21 E0 C2   LD           HL,$C2E0
4146: 19         ADD         HL,DE
4147: 36 47      LD           (HL),$47
4149: 3E 06      LD           A,$06
414B: E0 F2      LDFF00   ($F2),A
414D: F0 E7      LD           A,($E7)
414F: 1F         RRA
4150: 1F         RRA
4151: 1F         RRA
4152: E6 03      AND         $03
4154: 5F         LD           E,A
4155: 50         LD           D,B
4156: 21 A8 40   LD           HL,$40A8
4159: 19         ADD         HL,DE
415A: 7E         LD           A,(HL)
415B: CD 87 3B   CALL       $3B87
415E: C9         RET
415F: CD 91 08   CALL       $0891
4162: 28 30      JR           Z,$4194
4164: 3D         DEC         A
4165: 20 06      JR           NZ,$416D
4167: CD 8D 3B   CALL       $3B8D
416A: 36 03      LD           (HL),$03
416C: C9         RET
416D: 21 10 C3   LD           HL,$C310
4170: 09         ADD         HL,BC
4171: 7E         LD           A,(HL)
4172: A7         AND         A
4173: 20 19      JR           NZ,$418E
4175: CD AF 3D   CALL       $3DAF
4178: CD 91 08   CALL       $0891
417B: FE 28      CP           $28
417D: 30 12      JR           NC,$4191
417F: 1E 08      LD           E,$08
4181: F0 E7      LD           A,($E7)
4183: E6 04      AND         $04
4185: 28 02      JR           Z,$4189
4187: 1E F8      LD           E,$F8
4189: 21 40 C2   LD           HL,$C240
418C: 09         ADD         HL,BC
418D: 73         LD           (HL),E
418E: CD 94 6D   CALL       $6D94
4191: CD 9E 3B   CALL       $3B9E
4194: CD E2 08   CALL       $08E2
4197: CD EB 3B   CALL       $3BEB
419A: CD 54 7B   CALL       $7B54
419D: F0 EE      LD           A,($EE)
419F: 21 98 FF   LD           HL,$FF98
41A2: 96         SUB         (HL)
41A3: C6 10      ADD         $10
41A5: FE 20      CP           $20
41A7: 30 4F      JR           NC,$41F8
41A9: F0 EC      LD           A,($EC)
41AB: 21 99 FF   LD           HL,$FF99
41AE: 96         SUB         (HL)
41AF: C6 10      ADD         $10
41B1: FE 20      CP           $20
41B3: 30 43      JR           NC,$41F8
41B5: CD 42 09   CALL       $0942
41B8: FA 00 DB   LD           A,($DB00)
41BB: FE 03      CP           $03
41BD: 20 08      JR           NZ,$41C7
41BF: F0 CB      LD           A,($CB)
41C1: E6 20      AND         $20
41C3: 20 0F      JR           NZ,$41D4
41C5: 18 31      JR           $41F8
41C7: FA 01 DB   LD           A,($DB01)
41CA: FE 03      CP           $03
41CC: 20 2A      JR           NZ,$41F8
41CE: F0 CB      LD           A,($CB)
41D0: E6 10      AND         $10
41D2: 28 24      JR           Z,$41F8
41D4: FA CF C3   LD           A,($C3CF)
41D7: A7         AND         A
41D8: 20 1E      JR           NZ,$41F8
41DA: 3C         INC         A
41DB: EA CF C3   LD           ($C3CF),A
41DE: 21 80 C2   LD           HL,$C280
41E1: 09         ADD         HL,BC
41E2: 36 07      LD           (HL),$07
41E4: 21 90 C4   LD           HL,$C490
41E7: 09         ADD         HL,BC
41E8: 70         LD           (HL),B
41E9: F0 9E      LD           A,($9E)
41EB: EA 5D C1   LD           ($C15D),A
41EE: 21 F3 FF   LD           HL,$FFF3
41F1: 36 02      LD           (HL),$02
41F3: CD 91 08   CALL       $0891
41F6: 36 08      LD           (HL),$08
41F8: AF         XOR         A
41F9: CD 87 3B   CALL       $3B87
41FC: C9         RET
41FD: 21 20 C4   LD           HL,$C420
4200: 09         ADD         HL,BC
4201: 7E         LD           A,(HL)
4202: A7         AND         A
4203: 28 29      JR           Z,$422E
4205: 70         LD           (HL),B
4206: CD 8D 3B   CALL       $3B8D
4209: 36 02      LD           (HL),$02
420B: 21 20 C3   LD           HL,$C320
420E: 09         ADD         HL,BC
420F: 36 20      LD           (HL),$20
4211: 3E 08      LD           A,$08
4213: CD 30 3C   CALL       $3C30
4216: F0 D7      LD           A,($D7)
4218: 2F         CPL
4219: 3C         INC         A
421A: 21 50 C2   LD           HL,$C250
421D: 09         ADD         HL,BC
421E: 77         LD           (HL),A
421F: F0 D8      LD           A,($D8)
4221: 2F         CPL
4222: 3C         INC         A
4223: 21 40 C2   LD           HL,$C240
4226: 09         ADD         HL,BC
4227: 77         LD           (HL),A
4228: CD 91 08   CALL       $0891
422B: 36 C0      LD           (HL),$C0
422D: C9         RET
422E: CD 4A 6D   CALL       $6D4A
4231: 21 40 C3   LD           HL,$C340
4234: 09         ADD         HL,BC
4235: 36 01      LD           (HL),$01
4237: 21 50 C3   LD           HL,$C350
423A: 09         ADD         HL,BC
423B: 36 00      LD           (HL),$00
423D: 21 30 C4   LD           HL,$C430
4240: 09         ADD         HL,BC
4241: 36 00      LD           (HL),$00
4243: CD B4 3B   CALL       $3BB4
4246: 21 30 C4   LD           HL,$C430
4249: 09         ADD         HL,BC
424A: 36 D0      LD           (HL),$D0
424C: F0 E8      LD           A,($E8)
424E: E6 80      AND         $80
4250: 28 0F      JR           Z,$4261
4252: 21 20 C3   LD           HL,$C320
4255: 09         ADD         HL,BC
4256: 36 10      LD           (HL),$10
4258: 3E 20      LD           A,$20
425A: E0 F2      LDFF00   ($F2),A
425C: 3E 0C      LD           A,$0C
425E: CD 25 3C   CALL       $3C25
4261: CD 94 6D   CALL       $6D94
4264: CD 9E 3B   CALL       $3B9E
4267: C3 4D 41   JP           $414D
426A: F0 00      LD           A,($00)
426C: 76         HALT
426D: 00         NOP
426E: F0 08      LD           A,($08)
4270: 76         HALT
4271: 20 00      JR           NZ,$4273
4273: 00         NOP
4274: 78         LD           A,B
4275: 00         NOP
4276: 00         NOP
4277: 08 78 20   LD           ($2078),SP
427A: F0 00      LD           A,($00)
427C: 7A         LD           A,D
427D: 00         NOP
427E: F0 08      LD           A,($08)
4280: 7C         LD           A,H
4281: 00         NOP
4282: 00         NOP
4283: 00         NOP
4284: 7E         LD           A,(HL)
4285: 00         NOP
4286: 00         NOP
4287: 08 7E 20   LD           ($207E),SP
428A: F0 00      LD           A,($00)
428C: 7C         LD           A,H
428D: 20 F0      JR           NZ,$427F
428F: 08 7A 20   LD           ($207A),SP
4292: 00         NOP
4293: 00         NOP
4294: 7E         LD           A,(HL)
4295: 00         NOP
4296: 00         NOP
4297: 08 7E 20   LD           ($207E),SP
429A: 26 00      LD           H,$00
429C: 21 B0 C3   LD           HL,$C3B0
429F: 09         ADD         HL,BC
42A0: 7E         LD           A,(HL)
42A1: 17         RLA
42A2: 17         RLA
42A3: 17         RLA
42A4: 17         RLA
42A5: E6 F0      AND         $F0
42A7: 5F         LD           E,A
42A8: 50         LD           D,B
42A9: 21 6A 42   LD           HL,$426A
42AC: 19         ADD         HL,DE
42AD: 0E 04      LD           C,$04
42AF: CD 26 3D   CALL       $3D26
42B2: 3E 04      LD           A,$04
42B4: CD D0 3D   CALL       $3DD0
42B7: 21 10 C3   LD           HL,$C310
42BA: 09         ADD         HL,BC
42BB: 7E         LD           A,(HL)
42BC: A7         AND         A
42BD: 28 12      JR           Z,$42D1
42BF: F0 EF      LD           A,($EF)
42C1: C6 0A      ADD         $0A
42C3: E0 EC      LDFF00   ($EC),A
42C5: AF         XOR         A
42C6: E0 F1      LDFF00   ($F1),A
42C8: 11 9A 42   LD           DE,$429A
42CB: CD D0 3C   CALL       $3CD0
42CE: CD BA 3D   CALL       $3DBA
42D1: C9         RET
42D2: CD EC 46   CALL       $46EC
42D5: F0 EA      LD           A,($EA)
42D7: FE 05      CP           $05
42D9: 28 2E      JR           Z,$4309
42DB: 21 20 C4   LD           HL,$C420
42DE: 09         ADD         HL,BC
42DF: F0 E7      LD           A,($E7)
42E1: 77         LD           (HL),A
42E2: F0 F0      LD           A,($F0)
42E4: C7         RST         0X00
42E5: EB                              
42E6: 42         LD           B,D
42E7: F4                              
42E8: 42         LD           B,D
42E9: FF         RST         0X38
42EA: 42         LD           B,D
42EB: CD 91 08   CALL       $0891
42EE: 36 40      LD           (HL),$40
42F0: CD 8D 3B   CALL       $3B8D
42F3: C9         RET
42F4: CD 91 08   CALL       $0891
42F7: 20 05      JR           NZ,$42FE
42F9: 36 A0      LD           (HL),$A0
42FB: CD 8D 3B   CALL       $3B8D
42FE: C9         RET
42FF: CD 91 08   CALL       $0891
4302: CA 46 57   JP           Z,$5746
4305: CD F3 50   CALL       $50F3
4308: C9         RET
4309: CD 1F 7F   CALL       $7F1F
430C: 21 40 C2   LD           HL,$C240
430F: 09         ADD         HL,BC
4310: 7E         LD           A,(HL)
4311: EA 00 D0   LD           ($D000),A
4314: 21 50 C2   LD           HL,$C250
4317: 09         ADD         HL,BC
4318: 7E         LD           A,(HL)
4319: EA 01 D0   LD           ($D001),A
431C: F0 F0      LD           A,($F0)
431E: FE 05      CP           $05
4320: 28 03      JR           Z,$4325
4322: CD BF 3B   CALL       $3BBF
4325: F0 F0      LD           A,($F0)
4327: C7         RST         0X00
4328: 34         INC         (HL)
4329: 43         LD           B,E
432A: 71         LD           (HL),C
432B: 43         LD           B,E
432C: 92         SUB         D
432D: 44         LD           B,H
432E: DC 44 0A   CALL       C,$0A44
4331: 45         LD           B,L
4332: 68         LD           L,B
4333: 45         LD           B,L
4334: CD 91 08   CALL       $0891
4337: 20 27      JR           NZ,$4360
4339: CD 8D 3B   CALL       $3B8D
433C: CD 8C 08   CALL       $088C
433F: 36 FF      LD           (HL),$FF
4341: FA 02 D0   LD           A,($D002)
4344: 5F         LD           E,A
4345: 50         LD           D,B
4346: 21 80 C2   LD           HL,$C280
4349: 19         ADD         HL,DE
434A: 7E         LD           A,(HL)
434B: A7         AND         A
434C: 3E 52      LD           A,$52
434E: 20 0D      JR           NZ,$435D
4350: CD 8D 3B   CALL       $3B8D
4353: 36 04      LD           (HL),$04
4355: 21 60 C3   LD           HL,$C360
4358: 09         ADD         HL,BC
4359: 36 08      LD           (HL),$08
435B: 3E 53      LD           A,$53
435D: CD 97 21   CALL       $2197
4360: C9         RET
4361: 10 14      STOP       $14
4363: 18 20      JR           $4385
4365: 28 30      JR           Z,$4397
4367: 38 40      JR           C,$43A9
4369: FF         RST         0X38
436A: FF         RST         0X38
436B: 60         LD           H,B
436C: 40         LD           B,B
436D: 01 FF 08   LD           BC,$08FF
4370: F8 CD      LDHL       SP,$CD
4372: 94         SUB         H
4373: 6D         LD           L,L
4374: 21 80 C3   LD           HL,$C380
4377: 09         ADD         HL,BC
4378: 5E         LD           E,(HL)
4379: 50         LD           D,B
437A: F0 E7      LD           A,($E7)
437C: E6 07      AND         $07
437E: 20 17      JR           NZ,$4397
4380: 21 40 C2   LD           HL,$C240
4383: 09         ADD         HL,BC
4384: 7E         LD           A,(HL)
4385: 21 6F 43   LD           HL,$436F
4388: 19         ADD         HL,DE
4389: BE         CP           (HL)
438A: 28 0B      JR           Z,$4397
438C: 21 6D 43   LD           HL,$436D
438F: 19         ADD         HL,DE
4390: 7E         LD           A,(HL)
4391: 21 40 C2   LD           HL,$C240
4394: 09         ADD         HL,BC
4395: 86         ADD         A,(HL)
4396: 77         LD           (HL),A
4397: 21 6B 43   LD           HL,$436B
439A: 19         ADD         HL,DE
439B: F0 EE      LD           A,($EE)
439D: BE         CP           (HL)
439E: 20 08      JR           NZ,$43A8
43A0: 21 80 C3   LD           HL,$C380
43A3: 09         ADD         HL,BC
43A4: 7E         LD           A,(HL)
43A5: EE 01      XOR         $01
43A7: 77         LD           (HL),A
43A8: F0 E7      LD           A,($E7)
43AA: E6 01      AND         $01
43AC: 20 20      JR           NZ,$43CE
43AE: 21 C0 C2   LD           HL,$C2C0
43B1: 09         ADD         HL,BC
43B2: 5E         LD           E,(HL)
43B3: 50         LD           D,B
43B4: 21 6D 43   LD           HL,$436D
43B7: 19         ADD         HL,DE
43B8: 7E         LD           A,(HL)
43B9: 21 50 C2   LD           HL,$C250
43BC: 09         ADD         HL,BC
43BD: 86         ADD         A,(HL)
43BE: 77         LD           (HL),A
43BF: 21 6F 43   LD           HL,$436F
43C2: 19         ADD         HL,DE
43C3: BE         CP           (HL)
43C4: 20 08      JR           NZ,$43CE
43C6: 21 C0 C2   LD           HL,$C2C0
43C9: 09         ADD         HL,BC
43CA: 7E         LD           A,(HL)
43CB: EE 01      XOR         $01
43CD: 77         LD           (HL),A
43CE: F0 E7      LD           A,($E7)
43D0: 1F         RRA
43D1: 1F         RRA
43D2: 1F         RRA
43D3: 1F         RRA
43D4: E6 01      AND         $01
43D6: CD 87 3B   CALL       $3B87
43D9: CD 91 08   CALL       $0891
43DC: 20 4B      JR           NZ,$4429
43DE: E5         PUSH       HL
43DF: 21 D0 C3   LD           HL,$C3D0
43E2: 09         ADD         HL,BC
43E3: 7E         LD           A,(HL)
43E4: 5F         LD           E,A
43E5: FE 08      CP           $08
43E7: 38 07      JR           C,$43F0
43E9: CD 8D 3B   CALL       $3B8D
43EC: E1         POP         HL
43ED: 36 30      LD           (HL),$30
43EF: C9         RET
43F0: 50         LD           D,B
43F1: 21 61 43   LD           HL,$4361
43F4: 19         ADD         HL,DE
43F5: 7E         LD           A,(HL)
43F6: E1         POP         HL
43F7: 77         LD           (HL),A
43F8: 3E 5C      LD           A,$5C
43FA: CD 01 3C   CALL       $3C01
43FD: 38 2A      JR           C,$4429
43FF: F0 D7      LD           A,($D7)
4401: D6 0C      SUB         $0C
4403: 21 00 C2   LD           HL,$C200
4406: 19         ADD         HL,DE
4407: 77         LD           (HL),A
4408: F0 D8      LD           A,($D8)
440A: D6 14      SUB         $14
440C: 21 10 C2   LD           HL,$C210
440F: 19         ADD         HL,DE
4410: 77         LD           (HL),A
4411: 21 B0 C2   LD           HL,$C2B0
4414: 19         ADD         HL,DE
4415: 36 03      LD           (HL),$03
4417: 21 20 C3   LD           HL,$C320
441A: 19         ADD         HL,DE
441B: 36 20      LD           (HL),$20
441D: 21 40 C2   LD           HL,$C240
4420: 19         ADD         HL,DE
4421: 36 0C      LD           (HL),$0C
4423: 21 40 C3   LD           HL,$C340
4426: 19         ADD         HL,DE
4427: 36 42      LD           (HL),$42
4429: CD 8C 08   CALL       $088C
442C: 20 4A      JR           NZ,$4478
442E: 36 20      LD           (HL),$20
4430: 3E 5C      LD           A,$5C
4432: CD 01 3C   CALL       $3C01
4435: 38 41      JR           C,$4478
4437: C5         PUSH       BC
4438: 21 D0 C3   LD           HL,$C3D0
443B: 09         ADD         HL,BC
443C: 7E         LD           A,(HL)
443D: 34         INC         (HL)
443E: E6 01      AND         $01
4440: 4F         LD           C,A
4441: 21 90 44   LD           HL,$4490
4444: 09         ADD         HL,BC
4445: F0 D7      LD           A,($D7)
4447: 86         ADD         A,(HL)
4448: 21 00 C2   LD           HL,$C200
444B: 19         ADD         HL,DE
444C: 77         LD           (HL),A
444D: F0 D8      LD           A,($D8)
444F: 21 10 C2   LD           HL,$C210
4452: 19         ADD         HL,DE
4453: 77         LD           (HL),A
4454: 21 20 C3   LD           HL,$C320
4457: 19         ADD         HL,DE
4458: 36 24      LD           (HL),$24
445A: 21 B0 C2   LD           HL,$C2B0
445D: 19         ADD         HL,DE
445E: 36 04      LD           (HL),$04
4460: 21 40 C3   LD           HL,$C340
4463: 19         ADD         HL,DE
4464: 36 12      LD           (HL),$12
4466: D5         PUSH       DE
4467: C1         POP         BC
4468: 3E 1F      LD           A,$1F
446A: CD 25 3C   CALL       $3C25
446D: C1         POP         BC
446E: 21 00 C3   LD           HL,$C300
4471: 09         ADD         HL,BC
4472: 36 10      LD           (HL),$10
4474: 3E 28      LD           A,$28
4476: E0 F4      LDFF00   ($F4),A
4478: 21 00 C3   LD           HL,$C300
447B: 09         ADD         HL,BC
447C: 7E         LD           A,(HL)
447D: A7         AND         A
447E: 28 0F      JR           Z,$448F
4480: 21 D0 C3   LD           HL,$C3D0
4483: 09         ADD         HL,BC
4484: 7E         LD           A,(HL)
4485: E6 01      AND         $01
4487: 3E 02      LD           A,$02
4489: 28 01      JR           Z,$448C
448B: 3C         INC         A
448C: CD 87 3B   CALL       $3B87
448F: C9         RET
4490: F4                              
4491: 0C         INC         C
4492: FA 02 D0   LD           A,($D002)
4495: 5F         LD           E,A
4496: 50         LD           D,B
4497: F0 98      LD           A,($98)
4499: F5         PUSH       AF
449A: 21 00 C2   LD           HL,$C200
449D: 19         ADD         HL,DE
449E: 7E         LD           A,(HL)
449F: E0 98      LDFF00   ($98),A
44A1: F0 99      LD           A,($99)
44A3: F5         PUSH       AF
44A4: 21 10 C2   LD           HL,$C210
44A7: 19         ADD         HL,DE
44A8: 7E         LD           A,(HL)
44A9: D6 20      SUB         $20
44AB: E0 99      LDFF00   ($99),A
44AD: 3E 10      LD           A,$10
44AF: CD 25 3C   CALL       $3C25
44B2: CD 94 6D   CALL       $6D94
44B5: 21 98 FF   LD           HL,$FF98
44B8: F0 EE      LD           A,($EE)
44BA: 96         SUB         (HL)
44BB: C6 03      ADD         $03
44BD: FE 06      CP           $06
44BF: 30 14      JR           NC,$44D5
44C1: 21 99 FF   LD           HL,$FF99
44C4: F0 EC      LD           A,($EC)
44C6: 96         SUB         (HL)
44C7: C6 03      ADD         $03
44C9: FE 06      CP           $06
44CB: 30 08      JR           NC,$44D5
44CD: CD 91 08   CALL       $0891
44D0: 36 10      LD           (HL),$10
44D2: CD 8D 3B   CALL       $3B8D
44D5: F1         POP         AF
44D6: E0 99      LDFF00   ($99),A
44D8: F1         POP         AF
44D9: E0 98      LDFF00   ($98),A
44DB: C9         RET
44DC: CD 91 08   CALL       $0891
44DF: CA 44 6D   JP           Z,$6D44
44E2: FE 04      CP           $04
44E4: 20 23      JR           NZ,$4509
44E6: 3E 5C      LD           A,$5C
44E8: CD 01 3C   CALL       $3C01
44EB: F0 D7      LD           A,($D7)
44ED: 21 00 C2   LD           HL,$C200
44F0: 19         ADD         HL,DE
44F1: 77         LD           (HL),A
44F2: F0 D8      LD           A,($D8)
44F4: 21 10 C2   LD           HL,$C210
44F7: 19         ADD         HL,DE
44F8: 77         LD           (HL),A
44F9: 21 B0 C2   LD           HL,$C2B0
44FC: 19         ADD         HL,DE
44FD: 36 02      LD           (HL),$02
44FF: 21 E0 C2   LD           HL,$C2E0
4502: 19         ADD         HL,DE
4503: 36 C7      LD           (HL),$C7
4505: 3E 1F      LD           A,$1F
4507: E0 F2      LDFF00   ($F2),A
4509: C9         RET
450A: 21 50 C3   LD           HL,$C350
450D: 09         ADD         HL,BC
450E: 36 0C      LD           (HL),$0C
4510: 21 30 C4   LD           HL,$C430
4513: 09         ADD         HL,BC
4514: 36 81      LD           (HL),$81
4516: 21 20 C4   LD           HL,$C420
4519: 09         ADD         HL,BC
451A: 7E         LD           A,(HL)
451B: FE 02      CP           $02
451D: 20 09      JR           NZ,$4528
451F: CD 8D 3B   CALL       $3B8D
4522: CD 91 08   CALL       $0891
4525: 36 80      LD           (HL),$80
4527: C9         RET
4528: CD 4A 6D   CALL       $6D4A
452B: CD EB 3B   CALL       $3BEB
452E: CD 94 6D   CALL       $6D94
4531: CD 9E 3B   CALL       $3B9E
4534: F0 E7      LD           A,($E7)
4536: E6 03      AND         $03
4538: 20 21      JR           NZ,$455B
453A: 3E 10      LD           A,$10
453C: CD 30 3C   CALL       $3C30
453F: 21 40 C2   LD           HL,$C240
4542: 09         ADD         HL,BC
4543: F0 D8      LD           A,($D8)
4545: 96         SUB         (HL)
4546: E6 80      AND         $80
4548: 28 02      JR           Z,$454C
454A: 35         DEC         (HL)
454B: 35         DEC         (HL)
454C: 34         INC         (HL)
454D: 21 50 C2   LD           HL,$C250
4550: 09         ADD         HL,BC
4551: F0 D7      LD           A,($D7)
4553: 96         SUB         (HL)
4554: E6 80      AND         $80
4556: 28 02      JR           Z,$455A
4558: 35         DEC         (HL)
4559: 35         DEC         (HL)
455A: 34         INC         (HL)
455B: F0 E7      LD           A,($E7)
455D: 1F         RRA
455E: 1F         RRA
455F: 1F         RRA
4560: 1F         RRA
4561: E6 01      AND         $01
4563: C6 02      ADD         $02
4565: C3 87 3B   JP           $3B87
4568: 21 40 C3   LD           HL,$C340
456B: 09         ADD         HL,BC
456C: 36 41      LD           (HL),$41
456E: CD 91 08   CALL       $0891
4571: 20 71      JR           NZ,$45E4
4573: CD 8D 3B   CALL       $3B8D
4576: 36 04      LD           (HL),$04
4578: 21 40 C3   LD           HL,$C340
457B: 09         ADD         HL,BC
457C: 36 01      LD           (HL),$01
457E: CD ED 27   CALL       $27ED
4581: E6 01      AND         $01
4583: 20 14      JR           NZ,$4599
4585: 21 D0 C2   LD           HL,$C2D0
4588: 09         ADD         HL,BC
4589: 7E         LD           A,(HL)
458A: 21 10 C2   LD           HL,$C210
458D: 09         ADD         HL,BC
458E: 77         LD           (HL),A
458F: 21 40 C4   LD           HL,$C440
4592: 09         ADD         HL,BC
4593: 7E         LD           A,(HL)
4594: 21 00 C2   LD           HL,$C200
4597: 09         ADD         HL,BC
4598: 77         LD           (HL),A
4599: CD AF 3D   CALL       $3DAF
459C: 21 10 C4   LD           HL,$C410
459F: 09         ADD         HL,BC
45A0: 70         LD           (HL),B
45A1: 3E 5C      LD           A,$5C
45A3: CD 01 3C   CALL       $3C01
45A6: 38 3B      JR           C,$45E3
45A8: C5         PUSH       BC
45A9: 21 D0 C3   LD           HL,$C3D0
45AC: 09         ADD         HL,BC
45AD: 7E         LD           A,(HL)
45AE: 34         INC         (HL)
45AF: E6 01      AND         $01
45B1: 4F         LD           C,A
45B2: 21 90 44   LD           HL,$4490
45B5: 09         ADD         HL,BC
45B6: F0 D7      LD           A,($D7)
45B8: 86         ADD         A,(HL)
45B9: 21 00 C2   LD           HL,$C200
45BC: 19         ADD         HL,DE
45BD: 77         LD           (HL),A
45BE: F0 D8      LD           A,($D8)
45C0: 21 10 C2   LD           HL,$C210
45C3: 19         ADD         HL,DE
45C4: 77         LD           (HL),A
45C5: 21 20 C3   LD           HL,$C320
45C8: 19         ADD         HL,DE
45C9: 36 24      LD           (HL),$24
45CB: 21 B0 C2   LD           HL,$C2B0
45CE: 19         ADD         HL,DE
45CF: 36 04      LD           (HL),$04
45D1: 21 40 C3   LD           HL,$C340
45D4: 19         ADD         HL,DE
45D5: 36 12      LD           (HL),$12
45D7: D5         PUSH       DE
45D8: C1         POP         BC
45D9: 3E 1F      LD           A,$1F
45DB: CD 25 3C   CALL       $3C25
45DE: C1         POP         BC
45DF: 3E 28      LD           A,$28
45E1: E0 F4      LDFF00   ($F4),A
45E3: C9         RET
45E4: F0 98      LD           A,($98)
45E6: F5         PUSH       AF
45E7: 3E 50      LD           A,$50
45E9: E0 98      LDFF00   ($98),A
45EB: F0 99      LD           A,($99)
45ED: F5         PUSH       AF
45EE: 3E 48      LD           A,$48
45F0: E0 99      LDFF00   ($99),A
45F2: 3E 20      LD           A,$20
45F4: CD 30 3C   CALL       $3C30
45F7: F0 D8      LD           A,($D8)
45F9: 2F         CPL
45FA: 3C         INC         A
45FB: F5         PUSH       AF
45FC: F0 D7      LD           A,($D7)
45FE: F5         PUSH       AF
45FF: 3E 04      LD           A,$04
4601: CD 30 3C   CALL       $3C30
4604: 21 D8 FF   LD           HL,$FFD8
4607: F1         POP         AF
4608: 86         ADD         A,(HL)
4609: 21 40 C2   LD           HL,$C240
460C: 09         ADD         HL,BC
460D: 77         LD           (HL),A
460E: 21 D7 FF   LD           HL,$FFD7
4611: F1         POP         AF
4612: 86         ADD         A,(HL)
4613: 21 50 C2   LD           HL,$C250
4616: 09         ADD         HL,BC
4617: 77         LD           (HL),A
4618: F1         POP         AF
4619: E0 99      LDFF00   ($99),A
461B: F1         POP         AF
461C: E0 98      LDFF00   ($98),A
461E: CD 94 6D   CALL       $6D94
4621: CD 27 46   CALL       $4627
4624: C3 5B 45   JP           $455B
4627: 21 10 C2   LD           HL,$C210
462A: 09         ADD         HL,BC
462B: 7E         LD           A,(HL)
462C: D6 48      SUB         $48
462E: 5F         LD           E,A
462F: 3E 48      LD           A,$48
4631: 93         SUB         E
4632: 21 D0 C2   LD           HL,$C2D0
4635: 09         ADD         HL,BC
4636: 77         LD           (HL),A
4637: 21 00 C2   LD           HL,$C200
463A: 09         ADD         HL,BC
463B: 7E         LD           A,(HL)
463C: D6 50      SUB         $50
463E: 5F         LD           E,A
463F: 3E 50      LD           A,$50
4641: 93         SUB         E
4642: 21 40 C4   LD           HL,$C440
4645: 09         ADD         HL,BC
4646: 77         LD           (HL),A
4647: C9         RET
4648: F0 F4      LD           A,($F4)
464A: 60         LD           H,B
464B: 00         NOP
464C: F0 FC      LD           A,($FC)
464E: 62         LD           H,D
464F: 00         NOP
4650: F0 04      LD           A,($04)
4652: 64         LD           H,H
4653: 00         NOP
4654: F0 0C      LD           A,($0C)
4656: 62         LD           H,D
4657: 20 F0      JR           NZ,$4649
4659: 14         INC         D
465A: 60         LD           H,B
465B: 20 00      JR           NZ,$465D
465D: F4                              
465E: 66         LD           H,(HL)
465F: 00         NOP
4660: 00         NOP
4661: FC                              
4662: 68         LD           L,B
4663: 00         NOP
4664: 00         NOP
4665: 04         INC         B
4666: 6A         LD           L,D
4667: 00         NOP
4668: 00         NOP
4669: 0C         INC         C
466A: 68         LD           L,B
466B: 20 00      JR           NZ,$466D
466D: 14         INC         D
466E: 66         LD           H,(HL)
466F: 20 F0      JR           NZ,$4661
4671: F4                              
4672: 60         LD           H,B
4673: 00         NOP
4674: F0 FC      LD           A,($FC)
4676: 62         LD           H,D
4677: 00         NOP
4678: F0 04      LD           A,($04)
467A: 64         LD           H,H
467B: 20 F0      JR           NZ,$466D
467D: 0C         INC         C
467E: 62         LD           H,D
467F: 20 F0      JR           NZ,$4671
4681: 14         INC         D
4682: 60         LD           H,B
4683: 20 00      JR           NZ,$4685
4685: F4                              
4686: 66         LD           H,(HL)
4687: 00         NOP
4688: 00         NOP
4689: FC                              
468A: 68         LD           L,B
468B: 00         NOP
468C: 00         NOP
468D: 04         INC         B
468E: 6A         LD           L,D
468F: 20 00      JR           NZ,$4691
4691: 0C         INC         C
4692: 68         LD           L,B
4693: 20 00      JR           NZ,$4695
4695: 14         INC         D
4696: 66         LD           H,(HL)
4697: 20 F0      JR           NZ,$4689
4699: F4                              
469A: 60         LD           H,B
469B: 00         NOP
469C: F0 FC      LD           A,($FC)
469E: 62         LD           H,D
469F: 00         NOP
46A0: F0 04      LD           A,($04)
46A2: 64         LD           H,H
46A3: 00         NOP
46A4: F0 0C      LD           A,($0C)
46A6: 6C         LD           L,H
46A7: 00         NOP
46A8: F0 14      LD           A,($14)
46AA: 6E         LD           L,(HL)
46AB: 00         NOP
46AC: 00         NOP
46AD: F4                              
46AE: 66         LD           H,(HL)
46AF: 00         NOP
46B0: 00         NOP
46B1: FC                              
46B2: 68         LD           L,B
46B3: 00         NOP
46B4: 00         NOP
46B5: 04         INC         B
46B6: 6A         LD           L,D
46B7: 00         NOP
46B8: 00         NOP
46B9: 0C         INC         C
46BA: 70         LD           (HL),B
46BB: 00         NOP
46BC: 00         NOP
46BD: 14         INC         D
46BE: 72         LD           (HL),D
46BF: 00         NOP
46C0: F0 F4      LD           A,($F4)
46C2: 6E         LD           L,(HL)
46C3: 20 F0      JR           NZ,$46B5
46C5: FC                              
46C6: 6C         LD           L,H
46C7: 20 F0      JR           NZ,$46B9
46C9: 04         INC         B
46CA: 64         LD           H,H
46CB: 20 F0      JR           NZ,$46BD
46CD: 0C         INC         C
46CE: 62         LD           H,D
46CF: 20 F0      JR           NZ,$46C1
46D1: 14         INC         D
46D2: 60         LD           H,B
46D3: 20 00      JR           NZ,$46D5
46D5: F4                              
46D6: 72         LD           (HL),D
46D7: 20 00      JR           NZ,$46D9
46D9: FC                              
46DA: 70         LD           (HL),B
46DB: 20 00      JR           NZ,$46DD
46DD: 04         INC         B
46DE: 6A         LD           L,D
46DF: 20 00      JR           NZ,$46E1
46E1: 0C         INC         C
46E2: 68         LD           L,B
46E3: 20 00      JR           NZ,$46E5
46E5: 14         INC         D
46E6: 66         LD           H,(HL)
46E7: 20 74      JR           NZ,$475D
46E9: 00         NOP
46EA: 74         LD           (HL),H
46EB: 20 F0      JR           NZ,$46DD
46ED: F0 FE      LD           A,($FE)
46EF: 05         DEC         B
46F0: 20 14      JR           NZ,$4706
46F2: F0 E7      LD           A,($E7)
46F4: E6 01      AND         $01
46F6: 20 0E      JR           NZ,$4706
46F8: 21 D0 C2   LD           HL,$C2D0
46FB: 09         ADD         HL,BC
46FC: 7E         LD           A,(HL)
46FD: E0 EC      LDFF00   ($EC),A
46FF: 21 40 C4   LD           HL,$C440
4702: 09         ADD         HL,BC
4703: 7E         LD           A,(HL)
4704: E0 EE      LDFF00   ($EE),A
4706: 21 B0 C3   LD           HL,$C3B0
4709: 09         ADD         HL,BC
470A: 7E         LD           A,(HL)
470B: 5F         LD           E,A
470C: 50         LD           D,B
470D: CB 23      SLA         1,E
470F: CB 23      SLA         1,E
4711: CB 23      SLA         1,E
4713: 7B         LD           A,E
4714: CB 23      SLA         1,E
4716: CB 23      SLA         1,E
4718: 83         ADD         A,E
4719: 5F         LD           E,A
471A: 21 48 46   LD           HL,$4648
471D: 19         ADD         HL,DE
471E: 0E 0A      LD           C,$0A
4720: CD 26 3D   CALL       $3D26
4723: 3E 0A      LD           A,$0A
4725: CD D0 3D   CALL       $3DD0
4728: F0 EC      LD           A,($EC)
472A: C6 10      ADD         $10
472C: E0 EC      LDFF00   ($EC),A
472E: F0 E7      LD           A,($E7)
4730: 1F         RRA
4731: 1F         RRA
4732: 1F         RRA
4733: E6 01      AND         $01
4735: E0 F1      LDFF00   ($F1),A
4737: 11 E8 46   LD           DE,$46E8
473A: CD D0 3C   CALL       $3CD0
473D: CD BA 3D   CALL       $3DBA
4740: C9         RET
4741: 10 00      STOP       $00
4743: 1E 00      LD           E,$00
4745: 10 08      STOP       $08
4747: 1E 60      LD           E,$60
4749: 10 00      STOP       $00
474B: 1E 00      LD           E,$00
474D: 10 08      STOP       $08
474F: 1E 60      LD           E,$60
4751: 10 00      STOP       $00
4753: 1E 00      LD           E,$00
4755: 10 08      STOP       $08
4757: 1E 60      LD           E,$60
4759: 10 00      STOP       $00
475B: 1E 00      LD           E,$00
475D: 10 08      STOP       $08
475F: 1E 60      LD           E,$60
4761: 08 00 30   LD           ($3000),SP
4764: 00         NOP
4765: 08 08 30   LD           ($3008),SP
4768: 60         LD           H,B
4769: 08 00 30   LD           ($3000),SP
476C: 00         NOP
476D: 08 08 30   LD           ($3008),SP
4770: 60         LD           H,B
4771: 08 00 30   LD           ($3000),SP
4774: 00         NOP
4775: 08 08 30   LD           ($3008),SP
4778: 60         LD           H,B
4779: 08 00 30   LD           ($3000),SP
477C: 00         NOP
477D: 08 08 30   LD           ($3008),SP
4780: 60         LD           H,B
4781: 04         INC         B
4782: 00         NOP
4783: 30 00      JR           NC,$4785
4785: 04         INC         B
4786: 08 30 60   LD           ($6030),SP
4789: 14         INC         D
478A: 00         NOP
478B: 1E 00      LD           E,$00
478D: 14         INC         D
478E: 08 1E 60   LD           ($601E),SP
4791: 14         INC         D
4792: 00         NOP
4793: 1E 00      LD           E,$00
4795: 14         INC         D
4796: 08 1E 60   LD           ($601E),SP
4799: 14         INC         D
479A: 00         NOP
479B: 1E 00      LD           E,$00
479D: 14         INC         D
479E: 08 1E 60   LD           ($601E),SP
47A1: 00         NOP
47A2: 00         NOP
47A3: 30 00      JR           NC,$47A5
47A5: 00         NOP
47A6: 08 30 60   LD           ($6030),SP
47A9: 10 00      STOP       $00
47AB: 1E 00      LD           E,$00
47AD: 10 08      STOP       $08
47AF: 1E 60      LD           E,$60
47B1: 10 00      STOP       $00
47B3: 1E 00      LD           E,$00
47B5: 10 08      STOP       $08
47B7: 1E 60      LD           E,$60
47B9: 10 00      STOP       $00
47BB: 1E 00      LD           E,$00
47BD: 10 08      STOP       $08
47BF: 1E 60      LD           E,$60
47C1: F2                              
47C2: FA 30 00   LD           A,($0030)
47C5: F2                              
47C6: 02         LD           (BC),A
47C7: 30 60      JR           NC,$4829
47C9: F2                              
47CA: 06 30      LD           B,$30
47CC: 00         NOP
47CD: F2                              
47CE: 0E 30      LD           C,$30
47D0: 60         LD           H,B
47D1: FE FA      CP           $FA
47D3: 30 00      JR           NC,$47D5
47D5: FE 02      CP           $02
47D7: 30 60      JR           NC,$4839
47D9: FE 06      CP           $06
47DB: 30 00      JR           NC,$47DD
47DD: FE 0E      CP           $0E
47DF: 30 60      JR           NC,$4841
47E1: F0 F8      LD           A,($F8)
47E3: 30 40      JR           NC,$4825
47E5: F0 00      LD           A,($00)
47E7: 30 20      JR           NC,$4809
47E9: F0 08      LD           A,($08)
47EB: 30 40      JR           NC,$482D
47ED: F0 10      LD           A,($10)
47EF: 30 20      JR           NC,$4811
47F1: 00         NOP
47F2: F8 30      LDHL       SP,$30
47F4: 40         LD           B,B
47F5: 00         NOP
47F6: 00         NOP
47F7: 30 20      JR           NC,$4819
47F9: 00         NOP
47FA: 08 30 40   LD           ($4030),SP
47FD: 00         NOP
47FE: 10 30      STOP       $30
4800: 20 F0      JR           NZ,$47F2
4802: F8 32      LDHL       SP,$32
4804: 00         NOP
4805: F0 00      LD           A,($00)
4807: 32         LD           (HLD),A
4808: 60         LD           H,B
4809: F0 08      LD           A,($08)
480B: 32         LD           (HLD),A
480C: 00         NOP
480D: F0 10      LD           A,($10)
480F: 32         LD           (HLD),A
4810: 60         LD           H,B
4811: 00         NOP
4812: F8 32      LDHL       SP,$32
4814: 00         NOP
4815: 00         NOP
4816: 00         NOP
4817: 32         LD           (HLD),A
4818: 60         LD           H,B
4819: 00         NOP
481A: 08 32 00   LD           ($0032),SP
481D: 00         NOP
481E: 10 32      STOP       $32
4820: 60         LD           H,B
4821: 06 05      LD           B,$05
4823: 04         INC         B
4824: 05         DEC         B
4825: 04         INC         B
4826: 03         INC         BC
4827: 02         LD           (BC),A
4828: 01 00 00   LD           BC,$0000
482B: 01 02 03   LD           BC,$0302
482E: 04         INC         B
482F: 05         DEC         B
4830: 04         INC         B
4831: 05         DEC         B
4832: 06 CD      LD           B,$CD
4834: AE         XOR         (HL)
4835: 48         LD           C,B
4836: CD 1F 7F   CALL       $7F1F
4839: CD 91 08   CALL       $0891
483C: CB 7F      BIT         1,E
483E: 28 22      JR           Z,$4862
4840: E6 7F      AND         $7F
4842: 20 0E      JR           NZ,$4852
4844: FA 02 D0   LD           A,($D002)
4847: 5F         LD           E,A
4848: 50         LD           D,B
4849: 21 90 C2   LD           HL,$C290
484C: 19         ADD         HL,DE
484D: 36 03      LD           (HL),$03
484F: C3 44 6D   JP           $6D44
4852: 1F         RRA
4853: 1F         RRA
4854: 1F         RRA
4855: E6 0F      AND         $0F
4857: 5F         LD           E,A
4858: 50         LD           D,B
4859: 21 2A 48   LD           HL,$482A
485C: 19         ADD         HL,DE
485D: 7E         LD           A,(HL)
485E: CD 87 3B   CALL       $3B87
4861: C9         RET
4862: A7         AND         A
4863: CA 44 6D   JP           Z,$6D44
4866: FE 06      CP           $06
4868: 20 31      JR           NZ,$489B
486A: 3E 5C      LD           A,$5C
486C: CD 01 3C   CALL       $3C01
486F: F0 D7      LD           A,($D7)
4871: 21 00 C2   LD           HL,$C200
4874: 19         ADD         HL,DE
4875: 77         LD           (HL),A
4876: F0 D8      LD           A,($D8)
4878: FE 14      CP           $14
487A: 30 02      JR           NC,$487E
487C: 3E 14      LD           A,$14
487E: 21 10 C2   LD           HL,$C210
4881: 19         ADD         HL,DE
4882: 77         LD           (HL),A
4883: 21 B0 C2   LD           HL,$C2B0
4886: 19         ADD         HL,DE
4887: 36 01      LD           (HL),$01
4889: 21 E0 C2   LD           HL,$C2E0
488C: 19         ADD         HL,DE
488D: 36 40      LD           (HL),$40
488F: 21 40 C3   LD           HL,$C340
4892: 19         ADD         HL,DE
4893: 36 01      LD           (HL),$01
4895: 21 50 C3   LD           HL,$C350
4898: 19         ADD         HL,DE
4899: 36 8C      LD           (HL),$8C
489B: CD 91 08   CALL       $0891
489E: 1F         RRA
489F: 1F         RRA
48A0: 1F         RRA
48A1: E6 0F      AND         $0F
48A3: 5F         LD           E,A
48A4: 50         LD           D,B
48A5: 21 21 48   LD           HL,$4821
48A8: 19         ADD         HL,DE
48A9: 7E         LD           A,(HL)
48AA: CD 87 3B   CALL       $3B87
48AD: C9         RET
48AE: F0 F1      LD           A,($F1)
48B0: 17         RLA
48B1: 17         RLA
48B2: 17         RLA
48B3: 17         RLA
48B4: 17         RLA
48B5: E6 E0      AND         $E0
48B7: 5F         LD           E,A
48B8: 50         LD           D,B
48B9: 21 41 47   LD           HL,$4741
48BC: 19         ADD         HL,DE
48BD: 0E 08      LD           C,$08
48BF: CD 26 3D   CALL       $3D26
48C2: 3E 08      LD           A,$08
48C4: CD D0 3D   CALL       $3DD0
48C7: C9         RET
48C8: 34         INC         (HL)
48C9: 00         NOP
48CA: 34         INC         (HL)
48CB: 20 34      JR           NZ,$4901
48CD: 10 34      STOP       $34
48CF: 30 11      JR           NC,$48E2
48D1: C8         RET         Z
48D2: 48         LD           C,B
48D3: CD 3B 3C   CALL       $3C3B
48D6: CD 1F 7F   CALL       $7F1F
48D9: F0 E7      LD           A,($E7)
48DB: 1F         RRA
48DC: 1F         RRA
48DD: 1F         RRA
48DE: E6 01      AND         $01
48E0: CD 87 3B   CALL       $3B87
48E3: 21 40 C2   LD           HL,$C240
48E6: 09         ADD         HL,BC
48E7: 7E         LD           A,(HL)
48E8: F5         PUSH       AF
48E9: FA 00 D0   LD           A,($D000)
48EC: 86         ADD         A,(HL)
48ED: 77         LD           (HL),A
48EE: 21 50 C2   LD           HL,$C250
48F1: 09         ADD         HL,BC
48F2: 7E         LD           A,(HL)
48F3: F5         PUSH       AF
48F4: FA 01 D0   LD           A,($D001)
48F7: 86         ADD         A,(HL)
48F8: 77         LD           (HL),A
48F9: CD 94 6D   CALL       $6D94
48FC: F1         POP         AF
48FD: 21 50 C2   LD           HL,$C250
4900: 09         ADD         HL,BC
4901: 77         LD           (HL),A
4902: F1         POP         AF
4903: 21 40 C2   LD           HL,$C240
4906: 09         ADD         HL,BC
4907: 77         LD           (HL),A
4908: F0 F0      LD           A,($F0)
490A: A7         AND         A
490B: 20 22      JR           NZ,$492F
490D: CD CD 6D   CALL       $6DCD
4910: 21 20 C3   LD           HL,$C320
4913: 09         ADD         HL,BC
4914: 35         DEC         (HL)
4915: 35         DEC         (HL)
4916: 21 10 C3   LD           HL,$C310
4919: 09         ADD         HL,BC
491A: 7E         LD           A,(HL)
491B: E6 80      AND         $80
491D: 28 0F      JR           Z,$492E
491F: 70         LD           (HL),B
4920: CD 8D 3B   CALL       $3B8D
4923: CD 91 08   CALL       $0891
4926: 36 08      LD           (HL),$08
4928: 21 40 C2   LD           HL,$C240
492B: 09         ADD         HL,BC
492C: 36 E0      LD           (HL),$E0
492E: C9         RET
492F: CD 91 08   CALL       $0891
4932: CC 44 6D   CALL       Z,$6D44
4935: C9         RET
4936: 11 C8 48   LD           DE,$48C8
4939: CD 3B 3C   CALL       $3C3B
493C: CD 1F 7F   CALL       $7F1F
493F: F0 E7      LD           A,($E7)
4941: 1F         RRA
4942: 1F         RRA
4943: 1F         RRA
4944: E6 01      AND         $01
4946: CD 87 3B   CALL       $3B87
4949: CD BF 3B   CALL       $3BBF
494C: CD 94 6D   CALL       $6D94
494F: CD CD 6D   CALL       $6DCD
4952: 21 20 C3   LD           HL,$C320
4955: 09         ADD         HL,BC
4956: 35         DEC         (HL)
4957: 35         DEC         (HL)
4958: 21 10 C3   LD           HL,$C310
495B: 09         ADD         HL,BC
495C: 7E         LD           A,(HL)
495D: E6 80      AND         $80
495F: C2 44 6D   JP           NZ,$6D44
4962: C9         RET
4963: EE 12      XOR         $12
4965: F8 08      LDHL       SP,$08
4967: AF         XOR         A
4968: E0 E8      LDFF00   ($E8),A
496A: 3E 5B      LD           A,$5B
496C: CD 01 3C   CALL       $3C01
496F: 21 90 C3   LD           HL,$C390
4972: 19         ADD         HL,DE
4973: 36 01      LD           (HL),$01
4975: C5         PUSH       BC
4976: F0 E8      LD           A,($E8)
4978: 4F         LD           C,A
4979: 21 63 49   LD           HL,$4963
497C: 09         ADD         HL,BC
497D: F0 D7      LD           A,($D7)
497F: 86         ADD         A,(HL)
4980: 21 00 C2   LD           HL,$C200
4983: 19         ADD         HL,DE
4984: 77         LD           (HL),A
4985: 21 65 49   LD           HL,$4965
4988: 09         ADD         HL,BC
4989: 7E         LD           A,(HL)
498A: 21 40 C2   LD           HL,$C240
498D: 19         ADD         HL,DE
498E: 77         LD           (HL),A
498F: 21 20 C3   LD           HL,$C320
4992: 19         ADD         HL,DE
4993: 36 10      LD           (HL),$10
4995: 21 90 C2   LD           HL,$C290
4998: 19         ADD         HL,DE
4999: 36 01      LD           (HL),$01
499B: F0 D8      LD           A,($D8)
499D: 21 10 C2   LD           HL,$C210
49A0: 19         ADD         HL,DE
49A1: 77         LD           (HL),A
49A2: 21 60 C3   LD           HL,$C360
49A5: 19         ADD         HL,DE
49A6: 36 05      LD           (HL),$05
49A8: C1         POP         BC
49A9: F0 E8      LD           A,($E8)
49AB: 3C         INC         A
49AC: E0 E8      LDFF00   ($E8),A
49AE: FE 02      CP           $02
49B0: 20 B8      JR           NZ,$496A
49B2: C3 44 6D   JP           $6D44
49B5: 21 10 C3   LD           HL,$C310
49B8: 09         ADD         HL,BC
49B9: 36 7E      LD           (HL),$7E
49BB: CD 91 08   CALL       $0891
49BE: 36 A0      LD           (HL),$A0
49C0: C9         RET
49C1: CD 0E 38   CALL       $380E
49C4: CD 12 3F   CALL       $3F12
49C7: CD 52 4E   CALL       $4E52
49CA: 21 90 C3   LD           HL,$C390
49CD: 09         ADD         HL,BC
49CE: 7E         LD           A,(HL)
49CF: C7         RST         0X00
49D0: D4 49 F9   CALL       NC,$F949
49D3: 4D         LD           C,L
49D4: 21 60 C3   LD           HL,$C360
49D7: 09         ADD         HL,BC
49D8: 36 50      LD           (HL),$50
49DA: F0 F0      LD           A,($F0)
49DC: C7         RST         0X00
49DD: E5         PUSH       HL
49DE: 49         LD           C,C
49DF: 25         DEC         H
49E0: 4A         LD           C,D
49E1: 64         LD           H,H
49E2: 4A         LD           C,D
49E3: 78         LD           A,B
49E4: 4A         LD           C,D
49E5: FA 57 C1   LD           A,($C157)
49E8: FE 05      CP           $05
49EA: 20 07      JR           NZ,$49F3
49EC: CD 8D 3B   CALL       $3B8D
49EF: 3E 08      LD           A,$08
49F1: E0 F2      LDFF00   ($F2),A
49F3: CD 91 08   CALL       $0891
49F6: 20 2C      JR           NZ,$4A24
49F8: 36 50      LD           (HL),$50
49FA: FA AE C1   LD           A,($C1AE)
49FD: FE 02      CP           $02
49FF: 30 23      JR           NC,$4A24
4A01: 3E 1B      LD           A,$1B
4A03: CD 01 3C   CALL       $3C01
4A06: CD ED 27   CALL       $27ED
4A09: E6 3F      AND         $3F
4A0B: C6 40      ADD         $40
4A0D: 21 00 C2   LD           HL,$C200
4A10: 19         ADD         HL,DE
4A11: 77         LD           (HL),A
4A12: CD ED 27   CALL       $27ED
4A15: E6 3F      AND         $3F
4A17: C6 30      ADD         $30
4A19: 21 10 C2   LD           HL,$C210
4A1C: 19         ADD         HL,DE
4A1D: 77         LD           (HL),A
4A1E: 21 10 C3   LD           HL,$C310
4A21: 19         ADD         HL,DE
4A22: 36 70      LD           (HL),$70
4A24: C9         RET
4A25: CD B1 4D   CALL       $4DB1
4A28: CD 1F 7F   CALL       $7F1F
4A2B: CD CD 6D   CALL       $6DCD
4A2E: 21 20 C3   LD           HL,$C320
4A31: 09         ADD         HL,BC
4A32: 7E         LD           A,(HL)
4A33: FE A0      CP           $A0
4A35: 28 02      JR           Z,$4A39
4A37: 35         DEC         (HL)
4A38: 35         DEC         (HL)
4A39: 21 10 C3   LD           HL,$C310
4A3C: 09         ADD         HL,BC
4A3D: 7E         LD           A,(HL)
4A3E: E6 80      AND         $80
4A40: 28 21      JR           Z,$4A63
4A42: 70         LD           (HL),B
4A43: 3E 50      LD           A,$50
4A45: EA 57 C1   LD           ($C157),A
4A48: 3E 04      LD           A,$04
4A4A: EA 58 C1   LD           ($C158),A
4A4D: CD 91 08   CALL       $0891
4A50: 36 40      LD           (HL),$40
4A52: CD D7 08   CALL       $08D7
4A55: FA 46 C1   LD           A,($C146)
4A58: A7         AND         A
4A59: 20 05      JR           NZ,$4A60
4A5B: CD 87 08   CALL       $0887
4A5E: 36 14      LD           (HL),$14
4A60: CD 8D 3B   CALL       $3B8D
4A63: C9         RET
4A64: CD B1 4D   CALL       $4DB1
4A67: CD 1F 7F   CALL       $7F1F
4A6A: CD 91 08   CALL       $0891
4A6D: 20 03      JR           NZ,$4A72
4A6F: CD 8D 3B   CALL       $3B8D
4A72: CD 28 4B   CALL       $4B28
4A75: C3 BF 3B   JP           $3BBF
4A78: CD B1 4D   CALL       $4DB1
4A7B: CD 1F 7F   CALL       $7F1F
4A7E: CD E2 08   CALL       $08E2
4A81: 21 00 C3   LD           HL,$C300
4A84: 09         ADD         HL,BC
4A85: 7E         LD           A,(HL)
4A86: A7         AND         A
4A87: 28 16      JR           Z,$4A9F
4A89: FE 01      CP           $01
4A8B: CA 67 49   JP           Z,$4967
4A8E: E0 A1      LDFF00   ($A1),A
4A90: F0 E7      LD           A,($E7)
4A92: E6 01      AND         $01
4A94: 20 04      JR           NZ,$4A9A
4A96: 21 99 FF   LD           HL,$FF99
4A99: 35         DEC         (HL)
4A9A: 3E 06      LD           A,$06
4A9C: C3 87 3B   JP           $3B87
4A9F: CD 4C 4B   CALL       $4B4C
4AA2: F0 E7      LD           A,($E7)
4AA4: 1F         RRA
4AA5: 1F         RRA
4AA6: 1F         RRA
4AA7: 1F         RRA
4AA8: E6 01      AND         $01
4AAA: CD 87 3B   CALL       $3B87
4AAD: 21 B0 C2   LD           HL,$C2B0
4AB0: 09         ADD         HL,BC
4AB1: 7E         LD           A,(HL)
4AB2: A7         AND         A
4AB3: 28 10      JR           Z,$4AC5
4AB5: 3C         INC         A
4AB6: CD 87 3B   CALL       $3B87
4AB9: CD 8C 08   CALL       $088C
4ABC: 20 07      JR           NZ,$4AC5
4ABE: 36 28      LD           (HL),$28
4AC0: 21 B0 C2   LD           HL,$C2B0
4AC3: 09         ADD         HL,BC
4AC4: 35         DEC         (HL)
4AC5: AF         XOR         A
4AC6: E0 E8      LDFF00   ($E8),A
4AC8: 3E 14      LD           A,$14
4ACA: CD 31 4B   CALL       $4B31
4ACD: CD EB 3B   CALL       $3BEB
4AD0: 21 20 C4   LD           HL,$C420
4AD3: 09         ADD         HL,BC
4AD4: 7E         LD           A,(HL)
4AD5: 21 00 C3   LD           HL,$C300
4AD8: 09         ADD         HL,BC
4AD9: B6         OR           (HL)
4ADA: 20 0D      JR           NZ,$4AE9
4ADC: CD 28 4B   CALL       $4B28
4ADF: CD BF 3B   CALL       $3BBF
4AE2: 3E 01      LD           A,$01
4AE4: E0 E8      LDFF00   ($E8),A
4AE6: CD EB 3B   CALL       $3BEB
4AE9: 3E 14      LD           A,$14
4AEB: CD 31 4B   CALL       $4B31
4AEE: 21 20 C4   LD           HL,$C420
4AF1: 09         ADD         HL,BC
4AF2: 7E         LD           A,(HL)
4AF3: A7         AND         A
4AF4: 28 15      JR           Z,$4B0B
4AF6: F0 E7      LD           A,($E7)
4AF8: E6 1F      AND         $1F
4AFA: 20 0F      JR           NZ,$4B0B
4AFC: CD 8C 08   CALL       $088C
4AFF: 36 50      LD           (HL),$50
4B01: 21 B0 C2   LD           HL,$C2B0
4B04: 09         ADD         HL,BC
4B05: 7E         LD           A,(HL)
4B06: FE 04      CP           $04
4B08: 28 01      JR           Z,$4B0B
4B0A: 34         INC         (HL)
4B0B: C9         RET
4B0C: 08 14 00   LD           ($0014),SP
4B0F: 0C         INC         C
4B10: 08 15 00   LD           ($0015),SP
4B13: 0B         DEC         BC
4B14: 08 16 00   LD           ($0016),SP
4B17: 08 08 17   LD           ($1708),SP
4B1A: 00         NOP
4B1B: 06 08      LD           B,$08
4B1D: 18 00      JR           $4B1F
4B1F: 04         INC         B
4B20: 08 03 08   LD           ($0803),SP
4B23: 03         INC         BC
4B24: 08 0C 02   LD           ($020C),SP
4B27: 0C         INC         C
4B28: 21 B0 C2   LD           HL,$C2B0
4B2B: 09         ADD         HL,BC
4B2C: 7E         LD           A,(HL)
4B2D: CB 27      SLA         1,E
4B2F: CB 27      SLA         1,E
4B31: 5F         LD           E,A
4B32: 50         LD           D,B
4B33: 21 0C 4B   LD           HL,$4B0C
4B36: 19         ADD         HL,DE
4B37: E5         PUSH       HL
4B38: D1         POP         DE
4B39: C5         PUSH       BC
4B3A: CB 21      SLA         1,E
4B3C: CB 21      SLA         1,E
4B3E: 21 80 D5   LD           HL,$D580
4B41: 09         ADD         HL,BC
4B42: 0E 04      LD           C,$04
4B44: 1A         LD           A,(DE)
4B45: 13         INC         DE
4B46: 22         LD           (HLI),A
4B47: 0D         DEC         C
4B48: 20 FA      JR           NZ,$4B44
4B4A: C1         POP         BC
4B4B: C9         RET
4B4C: 21 D0 C2   LD           HL,$C2D0
4B4F: 09         ADD         HL,BC
4B50: 7E         LD           A,(HL)
4B51: C7         RST         0X00
4B52: 76         HALT
4B53: 4B         LD           C,E
4B54: C1         POP         BC
4B55: 4B         LD           C,E
4B56: 10 0C      STOP       $0C
4B58: 06 02      LD           B,$02
4B5A: F0 F4      LD           A,($F4)
4B5C: FA FE 10   LD           A,($10FE)
4B5F: 0C         INC         C
4B60: 06 02      LD           B,$02
4B62: F0 F4      LD           A,($F4)
4B64: FA FE 02   LD           A,($02FE)
4B67: 06 0C      LD           B,$0C
4B69: 10 02      STOP       $02
4B6B: 06 0C      LD           B,$0C
4B6D: 10 FE      STOP       $FE
4B6F: FA F4 F0   LD           A,($F0F4)
4B72: FE FA      CP           $FA
4B74: F4                              
4B75: F0 CD      LD           A,($CD)
4B77: 91         SUB         C
4B78: 08 A7 20   LD           ($20A7),SP
4B7B: 44         LD           B,H
4B7C: CD ED 27   CALL       $27ED
4B7F: E6 1F      AND         $1F
4B81: C6 10      ADD         $10
4B83: 77         LD           (HL),A
4B84: 21 D0 C2   LD           HL,$C2D0
4B87: 09         ADD         HL,BC
4B88: 34         INC         (HL)
4B89: 1E 00      LD           E,$00
4B8B: F0 EE      LD           A,($EE)
4B8D: FE 50      CP           $50
4B8F: 38 01      JR           C,$4B92
4B91: 1C         INC         E
4B92: 16 00      LD           D,$00
4B94: F0 EC      LD           A,($EC)
4B96: FE 48      CP           $48
4B98: 38 02      JR           C,$4B9C
4B9A: 14         INC         D
4B9B: 14         INC         D
4B9C: 7A         LD           A,D
4B9D: B3         OR           E
4B9E: CB 27      SLA         1,E
4BA0: CB 27      SLA         1,E
4BA2: F5         PUSH       AF
4BA3: CD ED 27   CALL       $27ED
4BA6: E6 03      AND         $03
4BA8: D1         POP         DE
4BA9: B2         OR           D
4BAA: 5F         LD           E,A
4BAB: 50         LD           D,B
4BAC: 21 56 4B   LD           HL,$4B56
4BAF: 19         ADD         HL,DE
4BB0: 7E         LD           A,(HL)
4BB1: 21 40 C2   LD           HL,$C240
4BB4: 09         ADD         HL,BC
4BB5: 77         LD           (HL),A
4BB6: 21 66 4B   LD           HL,$4B66
4BB9: 19         ADD         HL,DE
4BBA: 7E         LD           A,(HL)
4BBB: 21 50 C2   LD           HL,$C250
4BBE: 09         ADD         HL,BC
4BBF: 77         LD           (HL),A
4BC0: C9         RET
4BC1: CD 91 08   CALL       $0891
4BC4: 28 0B      JR           Z,$4BD1
4BC6: E6 0E      AND         $0E
4BC8: 20 06      JR           NZ,$4BD0
4BCA: CD 94 6D   CALL       $6D94
4BCD: CD 9E 3B   CALL       $3B9E
4BD0: C9         RET
4BD1: 36 30      LD           (HL),$30
4BD3: 21 D0 C2   LD           HL,$C2D0
4BD6: 09         ADD         HL,BC
4BD7: 70         LD           (HL),B
4BD8: C9         RET
4BD9: F0 F0      LD           A,($F0)
4BDB: 60         LD           H,B
4BDC: 00         NOP
4BDD: F0 F8      LD           A,($F8)
4BDF: 62         LD           H,D
4BE0: 00         NOP
4BE1: F0 00      LD           A,($00)
4BE3: 70         LD           (HL),B
4BE4: 00         NOP
4BE5: F0 08      LD           A,($08)
4BE7: 70         LD           (HL),B
4BE8: 20 F0      JR           NZ,$4BDA
4BEA: 10 62      STOP       $62
4BEC: 20 F0      JR           NZ,$4BDE
4BEE: 18 60      JR           $4C50
4BF0: 20 00      JR           NZ,$4BF2
4BF2: F0 64      LD           A,($64)
4BF4: 00         NOP
4BF5: 00         NOP
4BF6: F8 6E      LDHL       SP,$6E
4BF8: 00         NOP
4BF9: 00         NOP
4BFA: 00         NOP
4BFB: 72         LD           (HL),D
4BFC: 00         NOP
4BFD: 00         NOP
4BFE: 08 72 20   LD           ($2072),SP
4C01: 00         NOP
4C02: 10 6E      STOP       $6E
4C04: 20 00      JR           NZ,$4C06
4C06: 18 64      JR           $4C6C
4C08: 20 00      JR           NZ,$4C0A
4C0A: 00         NOP
4C0B: FF         RST         0X38
4C0C: 00         NOP
4C0D: 00         NOP
4C0E: 00         NOP
4C0F: FF         RST         0X38
4C10: 00         NOP
4C11: 00         NOP
4C12: 00         NOP
4C13: FF         RST         0X38
4C14: 00         NOP
4C15: 00         NOP
4C16: 00         NOP
4C17: FF         RST         0X38
4C18: 00         NOP
4C19: F0 F0      LD           A,($F0)
4C1B: 68         LD           L,B
4C1C: 00         NOP
4C1D: F0 F8      LD           A,($F8)
4C1F: 6A         LD           L,D
4C20: 00         NOP
4C21: F0 00      LD           A,($00)
4C23: 7E         LD           A,(HL)
4C24: 00         NOP
4C25: F0 08      LD           A,($08)
4C27: 7E         LD           A,(HL)
4C28: 20 F0      JR           NZ,$4C1A
4C2A: 10 6A      STOP       $6A
4C2C: 20 F0      JR           NZ,$4C1E
4C2E: 18 68      JR           $4C98
4C30: 20 00      JR           NZ,$4C32
4C32: F0 6C      LD           A,($6C)
4C34: 00         NOP
4C35: 00         NOP
4C36: F8 6E      LDHL       SP,$6E
4C38: 00         NOP
4C39: 00         NOP
4C3A: 00         NOP
4C3B: 72         LD           (HL),D
4C3C: 00         NOP
4C3D: 00         NOP
4C3E: 08 72 20   LD           ($2072),SP
4C41: 00         NOP
4C42: 10 6E      STOP       $6E
4C44: 20 00      JR           NZ,$4C46
4C46: 18 6C      JR           $4CB4
4C48: 20 00      JR           NZ,$4C4A
4C4A: 00         NOP
4C4B: FF         RST         0X38
4C4C: 00         NOP
4C4D: 00         NOP
4C4E: 00         NOP
4C4F: FF         RST         0X38
4C50: 00         NOP
4C51: 00         NOP
4C52: 00         NOP
4C53: FF         RST         0X38
4C54: 00         NOP
4C55: 00         NOP
4C56: 00         NOP
4C57: FF         RST         0X38
4C58: 00         NOP
4C59: F0 F0      LD           A,($F0)
4C5B: 60         LD           H,B
4C5C: 00         NOP
4C5D: F0 F8      LD           A,($F8)
4C5F: 62         LD           H,D
4C60: 00         NOP
4C61: F0 00      LD           A,($00)
4C63: 62         LD           H,D
4C64: 20 F0      JR           NZ,$4C56
4C66: 08 62 00   LD           ($0062),SP
4C69: F0 10      LD           A,($10)
4C6B: 62         LD           H,D
4C6C: 20 F0      JR           NZ,$4C5E
4C6E: 18 60      JR           $4CD0
4C70: 20 00      JR           NZ,$4C72
4C72: F0 64      LD           A,($64)
4C74: 00         NOP
4C75: 00         NOP
4C76: F8 66      LDHL       SP,$66
4C78: 00         NOP
4C79: 00         NOP
4C7A: 00         NOP
4C7B: 66         LD           H,(HL)
4C7C: 20 00      JR           NZ,$4C7E
4C7E: 08 66 00   LD           ($0066),SP
4C81: 00         NOP
4C82: 10 66      STOP       $66
4C84: 20 00      JR           NZ,$4C86
4C86: 18 64      JR           $4CEC
4C88: 20 00      JR           NZ,$4C8A
4C8A: 00         NOP
4C8B: FF         RST         0X38
4C8C: 00         NOP
4C8D: 00         NOP
4C8E: 00         NOP
4C8F: FF         RST         0X38
4C90: 00         NOP
4C91: 00         NOP
4C92: 00         NOP
4C93: FF         RST         0X38
4C94: 00         NOP
4C95: 00         NOP
4C96: 00         NOP
4C97: FF         RST         0X38
4C98: 00         NOP
4C99: F0 EC      LD           A,($EC)
4C9B: 60         LD           H,B
4C9C: 00         NOP
4C9D: F0 F4      LD           A,($F4)
4C9F: 62         LD           H,D
4CA0: 00         NOP
4CA1: F0 FC      LD           A,($FC)
4CA3: 62         LD           H,D
4CA4: 20 F0      JR           NZ,$4C96
4CA6: 04         INC         B
4CA7: 74         LD           (HL),H
4CA8: 00         NOP
4CA9: F0 0C      LD           A,($0C)
4CAB: 62         LD           H,D
4CAC: 00         NOP
4CAD: F0 14      LD           A,($14)
4CAF: 62         LD           H,D
4CB0: 20 F0      JR           NZ,$4CA2
4CB2: 1C         INC         E
4CB3: 60         LD           H,B
4CB4: 20 00      JR           NZ,$4CB6
4CB6: EC                              
4CB7: 64         LD           H,H
4CB8: 00         NOP
4CB9: 00         NOP
4CBA: F4                              
4CBB: 66         LD           H,(HL)
4CBC: 00         NOP
4CBD: 00         NOP
4CBE: FC                              
4CBF: 66         LD           H,(HL)
4CC0: 20 00      JR           NZ,$4CC2
4CC2: 04         INC         B
4CC3: 76         HALT
4CC4: 00         NOP
4CC5: 00         NOP
4CC6: 0C         INC         C
4CC7: 66         LD           H,(HL)
4CC8: 00         NOP
4CC9: 00         NOP
4CCA: 14         INC         D
4CCB: 66         LD           H,(HL)
4CCC: 20 00      JR           NZ,$4CCE
4CCE: 1C         INC         E
4CCF: 64         LD           H,H
4CD0: 20 00      JR           NZ,$4CD2
4CD2: 00         NOP
4CD3: FF         RST         0X38
4CD4: 00         NOP
4CD5: 00         NOP
4CD6: 00         NOP
4CD7: FF         RST         0X38
4CD8: 00         NOP
4CD9: F0 E8      LD           A,($E8)
4CDB: 60         LD           H,B
4CDC: 00         NOP
4CDD: F0 F0      LD           A,($F0)
4CDF: 62         LD           H,D
4CE0: 00         NOP
4CE1: F0 F8      LD           A,($F8)
4CE3: 62         LD           H,D
4CE4: 20 F0      JR           NZ,$4CD6
4CE6: 00         NOP
4CE7: 78         LD           A,B
4CE8: 00         NOP
4CE9: F0 08      LD           A,($08)
4CEB: 78         LD           A,B
4CEC: 20 F0      JR           NZ,$4CDE
4CEE: 10 62      STOP       $62
4CF0: 00         NOP
4CF1: F0 18      LD           A,($18)
4CF3: 62         LD           H,D
4CF4: 20 F0      JR           NZ,$4CE6
4CF6: 20 60      JR           NZ,$4D58
4CF8: 20 00      JR           NZ,$4CFA
4CFA: E8 64      ADD         SP,$64
4CFC: 00         NOP
4CFD: 00         NOP
4CFE: F0 66      LD           A,($66)
4D00: 00         NOP
4D01: 00         NOP
4D02: F8 66      LDHL       SP,$66
4D04: 20 00      JR           NZ,$4D06
4D06: 00         NOP
4D07: 7A         LD           A,D
4D08: 00         NOP
4D09: 00         NOP
4D0A: 08 7A 20   LD           ($207A),SP
4D0D: 00         NOP
4D0E: 10 66      STOP       $66
4D10: 00         NOP
4D11: 00         NOP
4D12: 18 66      JR           $4D7A
4D14: 20 00      JR           NZ,$4D16
4D16: 20 64      JR           NZ,$4D7C
4D18: 20 F0      JR           NZ,$4D0A
4D1A: E8 60      ADD         SP,$60
4D1C: 00         NOP
4D1D: F0 F0      LD           A,($F0)
4D1F: 62         LD           H,D
4D20: 00         NOP
4D21: F0 F8      LD           A,($F8)
4D23: 62         LD           H,D
4D24: 20 F0      JR           NZ,$4D16
4D26: 00         NOP
4D27: 78         LD           A,B
4D28: 00         NOP
4D29: F0 08      LD           A,($08)
4D2B: 78         LD           A,B
4D2C: 20 F0      JR           NZ,$4D1E
4D2E: 10 62      STOP       $62
4D30: 00         NOP
4D31: F0 18      LD           A,($18)
4D33: 62         LD           H,D
4D34: 20 F0      JR           NZ,$4D26
4D36: 20 60      JR           NZ,$4D98
4D38: 20 00      JR           NZ,$4D3A
4D3A: E8 64      ADD         SP,$64
4D3C: 00         NOP
4D3D: 00         NOP
4D3E: F0 66      LD           A,($66)
4D40: 00         NOP
4D41: 00         NOP
4D42: F8 66      LDHL       SP,$66
4D44: 20 00      JR           NZ,$4D46
4D46: 00         NOP
4D47: 7C         LD           A,H
4D48: 00         NOP
4D49: 00         NOP
4D4A: 08 7C 20   LD           ($207C),SP
4D4D: 00         NOP
4D4E: 10 66      STOP       $66
4D50: 00         NOP
4D51: 00         NOP
4D52: 18 66      JR           $4DBA
4D54: 20 00      JR           NZ,$4D56
4D56: 20 64      JR           NZ,$4DBC
4D58: 20 F0      JR           NZ,$4D4A
4D5A: E6 60      AND         $60
4D5C: 00         NOP
4D5D: F0 EE      LD           A,($EE)
4D5F: 62         LD           H,D
4D60: 00         NOP
4D61: F0 F6      LD           A,($F6)
4D63: 62         LD           H,D
4D64: 20 F0      JR           NZ,$4D56
4D66: FE 78      CP           $78
4D68: 00         NOP
4D69: F0 0A      LD           A,($0A)
4D6B: 78         LD           A,B
4D6C: 20 F0      JR           NZ,$4D5E
4D6E: 12         LD           (DE),A
4D6F: 62         LD           H,D
4D70: 00         NOP
4D71: F0 1A      LD           A,($1A)
4D73: 62         LD           H,D
4D74: 20 F0      JR           NZ,$4D66
4D76: 22         LD           (HLI),A
4D77: 60         LD           H,B
4D78: 20 00      JR           NZ,$4D7A
4D7A: E6 64      AND         $64
4D7C: 00         NOP
4D7D: 00         NOP
4D7E: EE 66      XOR         $66
4D80: 00         NOP
4D81: 00         NOP
4D82: F6 66      OR           $66
4D84: 20 00      JR           NZ,$4D86
4D86: FE 7C      CP           $7C
4D88: 00         NOP
4D89: 00         NOP
4D8A: 0A         LD           A,(BC)
4D8B: 7C         LD           A,H
4D8C: 20 00      JR           NZ,$4D8E
4D8E: 12         LD           (DE),A
4D8F: 66         LD           H,(HL)
4D90: 00         NOP
4D91: 00         NOP
4D92: 1A         LD           A,(DE)
4D93: 66         LD           H,(HL)
4D94: 20 00      JR           NZ,$4D96
4D96: 22         LD           (HLI),A
4D97: 64         LD           H,H
4D98: 20 0C      JR           NZ,$4DA6
4D9A: F5         PUSH       AF
4D9B: 26 00      LD           H,$00
4D9D: 0C         INC         C
4D9E: FB         EI
4D9F: 26 00      LD           H,$00
4DA1: 0C         INC         C
4DA2: 01 26 00   LD           BC,$0026
4DA5: 0C         INC         C
4DA6: 07         RLCA
4DA7: 26 00      LD           H,$00
4DA9: 0C         INC         C
4DAA: 0D         DEC         C
4DAB: 26 00      LD           H,$00
4DAD: 0C         INC         C
4DAE: 13         INC         DE
4DAF: 26 00      LD           H,$00
4DB1: 21 B0 C3   LD           HL,$C3B0
4DB4: 09         ADD         HL,BC
4DB5: 7E         LD           A,(HL)
4DB6: 50         LD           D,B
4DB7: 17         RLA
4DB8: CB 12      RL          1,E
4DBA: 17         RLA
4DBB: CB 12      RL          1,E
4DBD: 17         RLA
4DBE: CB 12      RL          1,E
4DC0: 17         RLA
4DC1: CB 12      RL          1,E
4DC3: 17         RLA
4DC4: CB 12      RL          1,E
4DC6: 17         RLA
4DC7: CB 12      RL          1,E
4DC9: E6 C0      AND         $C0
4DCB: 5F         LD           E,A
4DCC: 21 D9 4B   LD           HL,$4BD9
4DCF: 19         ADD         HL,DE
4DD0: 0E 10      LD           C,$10
4DD2: CD 26 3D   CALL       $3D26
4DD5: 3E 10      LD           A,$10
4DD7: CD D0 3D   CALL       $3DD0
4DDA: 21 10 C3   LD           HL,$C310
4DDD: 09         ADD         HL,BC
4DDE: 7E         LD           A,(HL)
4DDF: A7         AND         A
4DE0: 28 16      JR           Z,$4DF8
4DE2: F0 EF      LD           A,($EF)
4DE4: D6 08      SUB         $08
4DE6: E0 EC      LDFF00   ($EC),A
4DE8: 21 99 4D   LD           HL,$4D99
4DEB: 0E 06      LD           C,$06
4DED: CD 26 3D   CALL       $3D26
4DF0: 3E 06      LD           A,$06
4DF2: CD D0 3D   CALL       $3DD0
4DF5: CD BA 3D   CALL       $3DBA
4DF8: C9         RET
4DF9: CD 00 50   CALL       $5000
4DFC: F0 EA      LD           A,($EA)
4DFE: FE 05      CP           $05
4E00: CA 60 4E   JP           Z,$4E60
4E03: 21 20 C4   LD           HL,$C420
4E06: 09         ADD         HL,BC
4E07: F0 E7      LD           A,($E7)
4E09: 77         LD           (HL),A
4E0A: F0 F0      LD           A,($F0)
4E0C: C7         RST         0X00
4E0D: 13         INC         DE
4E0E: 4E         LD           C,(HL)
4E0F: 1B         DEC         DE
4E10: 4E         LD           C,(HL)
4E11: 26 4E      LD           H,$4E
4E13: CD 91 08   CALL       $0891
4E16: 36 40      LD           (HL),$40
4E18: C3 8D 3B   JP           $3B8D
4E1B: CD 91 08   CALL       $0891
4E1E: 20 05      JR           NZ,$4E25
4E20: 36 A0      LD           (HL),$A0
4E22: CD 8D 3B   CALL       $3B8D
4E25: C9         RET
4E26: CD 91 08   CALL       $0891
4E29: 20 24      JR           NZ,$4E4F
4E2B: 1E 0F      LD           E,$0F
4E2D: 50         LD           D,B
4E2E: 79         LD           A,C
4E2F: BB         CP           E
4E30: 28 11      JR           Z,$4E43
4E32: 21 80 C2   LD           HL,$C280
4E35: 19         ADD         HL,DE
4E36: 7E         LD           A,(HL)
4E37: A7         AND         A
4E38: 28 09      JR           Z,$4E43
4E3A: 21 A0 C3   LD           HL,$C3A0
4E3D: 19         ADD         HL,DE
4E3E: 7E         LD           A,(HL)
4E3F: FE 5B      CP           $5B
4E41: 28 09      JR           Z,$4E4C
4E43: 1D         DEC         E
4E44: 7B         LD           A,E
4E45: FE FF      CP           $FF
4E47: 20 E5      JR           NZ,$4E2E
4E49: C3 46 57   JP           $5746
4E4C: C3 44 6D   JP           $6D44
4E4F: C3 F3 50   JP           $50F3
4E52: CD 87 08   CALL       $0887
4E55: 28 08      JR           Z,$4E5F
4E57: 3E 02      LD           A,$02
4E59: E0 A1      LDFF00   ($A1),A
4E5B: 3E 6A      LD           A,$6A
4E5D: E0 9D      LDFF00   ($9D),A
4E5F: C9         RET
4E60: CD 1F 7F   CALL       $7F1F
4E63: 21 10 C4   LD           HL,$C410
4E66: 09         ADD         HL,BC
4E67: 7E         LD           A,(HL)
4E68: FE 02      CP           $02
4E6A: 20 17      JR           NZ,$4E83
4E6C: 21 B0 C2   LD           HL,$C2B0
4E6F: 09         ADD         HL,BC
4E70: 7E         LD           A,(HL)
4E71: A7         AND         A
4E72: 28 0E      JR           Z,$4E82
4E74: CD 8D 3B   CALL       $3B8D
4E77: 36 02      LD           (HL),$02
4E79: 3E 24      LD           A,$24
4E7B: E0 F2      LDFF00   ($F2),A
4E7D: CD AF 3D   CALL       $3DAF
4E80: 18 01      JR           $4E83
4E82: 34         INC         (HL)
4E83: CD 4A 6D   CALL       $6D4A
4E86: AF         XOR         A
4E87: E0 E8      LDFF00   ($E8),A
4E89: F0 F0      LD           A,($F0)
4E8B: C7         RST         0X00
4E8C: A4         AND         H
4E8D: 4E         LD           C,(HL)
4E8E: EB                              
4E8F: 4E         LD           C,(HL)
4E90: 65         LD           H,L
4E91: 4F         LD           C,A
4E92: 80         ADD         A,B
4E93: 4F         LD           C,A
4E94: 10 0C      STOP       $0C
4E96: 00         NOP
4E97: F4                              
4E98: F0 F4      LD           A,($F4)
4E9A: 00         NOP
4E9B: 0C         INC         C
4E9C: 00         NOP
4E9D: 0C         INC         C
4E9E: 10 0C      STOP       $0C
4EA0: 00         NOP
4EA1: F4                              
4EA2: F0 F4      LD           A,($F4)
4EA4: 3E 18      LD           A,$18
4EA6: CD 31 4B   CALL       $4B31
4EA9: CD B4 3B   CALL       $3BB4
4EAC: CD 91 08   CALL       $0891
4EAF: 20 36      JR           NZ,$4EE7
4EB1: CD ED 27   CALL       $27ED
4EB4: E6 07      AND         $07
4EB6: 5F         LD           E,A
4EB7: 50         LD           D,B
4EB8: 21 94 4E   LD           HL,$4E94
4EBB: 19         ADD         HL,DE
4EBC: 7E         LD           A,(HL)
4EBD: 21 40 C2   LD           HL,$C240
4EC0: 09         ADD         HL,BC
4EC1: 77         LD           (HL),A
4EC2: 21 9C 4E   LD           HL,$4E9C
4EC5: 19         ADD         HL,DE
4EC6: 7E         LD           A,(HL)
4EC7: 21 50 C2   LD           HL,$C250
4ECA: 09         ADD         HL,BC
4ECB: 77         LD           (HL),A
4ECC: CD ED 27   CALL       $27ED
4ECF: E6 03      AND         $03
4ED1: 20 05      JR           NZ,$4ED8
4ED3: 3E 18      LD           A,$18
4ED5: CD 25 3C   CALL       $3C25
4ED8: CD ED 27   CALL       $27ED
4EDB: E6 0F      AND         $0F
4EDD: 21 20 C3   LD           HL,$C320
4EE0: 09         ADD         HL,BC
4EE1: C6 08      ADD         $08
4EE3: 77         LD           (HL),A
4EE4: CD 8D 3B   CALL       $3B8D
4EE7: 78         LD           A,B
4EE8: C3 87 3B   JP           $3B87
4EEB: CD 91 08   CALL       $0891
4EEE: A7         AND         A
4EEF: 20 6F      JR           NZ,$4F60
4EF1: CD 94 6D   CALL       $6D94
4EF4: CD 9E 3B   CALL       $3B9E
4EF7: CD CD 6D   CALL       $6DCD
4EFA: 21 20 C3   LD           HL,$C320
4EFD: 09         ADD         HL,BC
4EFE: 35         DEC         (HL)
4EFF: 35         DEC         (HL)
4F00: 3E 18      LD           A,$18
4F02: CD 31 4B   CALL       $4B31
4F05: CD BF 3B   CALL       $3BBF
4F08: 21 40 C4   LD           HL,$C440
4F0B: 09         ADD         HL,BC
4F0C: 7E         LD           A,(HL)
4F0D: A7         AND         A
4F0E: 20 04      JR           NZ,$4F14
4F10: CD EB 3B   CALL       $3BEB
4F13: AF         XOR         A
4F14: 21 10 C3   LD           HL,$C310
4F17: 09         ADD         HL,BC
4F18: 7E         LD           A,(HL)
4F19: E6 80      AND         $80
4F1B: 28 43      JR           Z,$4F60
4F1D: 70         LD           (HL),B
4F1E: 21 40 C4   LD           HL,$C440
4F21: 09         ADD         HL,BC
4F22: 70         LD           (HL),B
4F23: 21 20 C3   LD           HL,$C320
4F26: 09         ADD         HL,BC
4F27: 7E         LD           A,(HL)
4F28: D6 E0      SUB         $E0
4F2A: E6 80      AND         $80
4F2C: 28 1B      JR           Z,$4F49
4F2E: 3E 18      LD           A,$18
4F30: EA 57 C1   LD           ($C157),A
4F33: 3E 0B      LD           A,$0B
4F35: E0 F2      LDFF00   ($F2),A
4F37: FA 46 C1   LD           A,($C146)
4F3A: A7         AND         A
4F3B: 20 0C      JR           NZ,$4F49
4F3D: CD 87 08   CALL       $0887
4F40: 36 0E      LD           (HL),$0E
4F42: 21 20 C3   LD           HL,$C320
4F45: 09         ADD         HL,BC
4F46: 70         LD           (HL),B
4F47: 18 0E      JR           $4F57
4F49: 21 20 C3   LD           HL,$C320
4F4C: 09         ADD         HL,BC
4F4D: 7E         LD           A,(HL)
4F4E: 70         LD           (HL),B
4F4F: FE F2      CP           $F2
4F51: 30 04      JR           NC,$4F57
4F53: 3E 20      LD           A,$20
4F55: E0 F2      LDFF00   ($F2),A
4F57: CD 8D 3B   CALL       $3B8D
4F5A: 70         LD           (HL),B
4F5B: CD 91 08   CALL       $0891
4F5E: 36 20      LD           (HL),$20
4F60: 3E 01      LD           A,$01
4F62: C3 87 3B   JP           $3B87
4F65: 21 20 C3   LD           HL,$C320
4F68: 09         ADD         HL,BC
4F69: 36 60      LD           (HL),$60
4F6B: CD CD 6D   CALL       $6DCD
4F6E: 21 10 C3   LD           HL,$C310
4F71: 09         ADD         HL,BC
4F72: 7E         LD           A,(HL)
4F73: FE 70      CP           $70
4F75: 38 08      JR           C,$4F7F
4F77: CD 91 08   CALL       $0891
4F7A: 36 30      LD           (HL),$30
4F7C: CD 8D 3B   CALL       $3B8D
4F7F: C9         RET
4F80: 3E FF      LD           A,$FF
4F82: CD 87 3B   CALL       $3B87
4F85: CD 91 08   CALL       $0891
4F88: 20 25      JR           NZ,$4FAF
4F8A: 36 18      LD           (HL),$18
4F8C: 21 40 C4   LD           HL,$C440
4F8F: 09         ADD         HL,BC
4F90: 36 01      LD           (HL),$01
4F92: CD 8D 3B   CALL       $3B8D
4F95: 36 01      LD           (HL),$01
4F97: 21 20 C3   LD           HL,$C320
4F9A: 09         ADD         HL,BC
4F9B: 36 C0      LD           (HL),$C0
4F9D: F0 98      LD           A,($98)
4F9F: 21 00 C2   LD           HL,$C200
4FA2: 09         ADD         HL,BC
4FA3: 77         LD           (HL),A
4FA4: F0 99      LD           A,($99)
4FA6: 21 10 C2   LD           HL,$C210
4FA9: 09         ADD         HL,BC
4FAA: 77         LD           (HL),A
4FAB: 3E 08      LD           A,$08
4FAD: E0 F2      LDFF00   ($F2),A
4FAF: C9         RET
4FB0: F0 F8      LD           A,($F8)
4FB2: 60         LD           H,B
4FB3: 00         NOP
4FB4: F0 00      LD           A,($00)
4FB6: 62         LD           H,D
4FB7: 00         NOP
4FB8: F0 08      LD           A,($08)
4FBA: 62         LD           H,D
4FBB: 20 F0      JR           NZ,$4FAD
4FBD: 10 60      STOP       $60
4FBF: 20 00      JR           NZ,$4FC1
4FC1: F8 64      LDHL       SP,$64
4FC3: 00         NOP
4FC4: 00         NOP
4FC5: 00         NOP
4FC6: 66         LD           H,(HL)
4FC7: 00         NOP
4FC8: 00         NOP
4FC9: 08 66 20   LD           ($2066),SP
4FCC: 00         NOP
4FCD: 10 64      STOP       $64
4FCF: 20 F0      JR           NZ,$4FC1
4FD1: F8 68      LDHL       SP,$68
4FD3: 00         NOP
4FD4: F0 00      LD           A,($00)
4FD6: 6A         LD           L,D
4FD7: 00         NOP
4FD8: F0 08      LD           A,($08)
4FDA: 6A         LD           L,D
4FDB: 20 F0      JR           NZ,$4FCD
4FDD: 10 68      STOP       $68
4FDF: 20 00      JR           NZ,$4FE1
4FE1: F8 6C      LDHL       SP,$6C
4FE3: 00         NOP
4FE4: 00         NOP
4FE5: 00         NOP
4FE6: 66         LD           H,(HL)
4FE7: 00         NOP
4FE8: 00         NOP
4FE9: 08 66 20   LD           ($2066),SP
4FEC: 00         NOP
4FED: 10 6C      STOP       $6C
4FEF: 20 0C      JR           NZ,$4FFD
4FF1: FB         EI
4FF2: 26 00      LD           H,$00
4FF4: 0C         INC         C
4FF5: 01 26 00   LD           BC,$0026
4FF8: 0C         INC         C
4FF9: 07         RLCA
4FFA: 26 00      LD           H,$00
4FFC: 0C         INC         C
4FFD: 0D         DEC         C
4FFE: 26 00      LD           H,$00
5000: 21 B0 C3   LD           HL,$C3B0
5003: 09         ADD         HL,BC
5004: 7E         LD           A,(HL)
5005: 50         LD           D,B
5006: 17         RLA
5007: CB 12      RL          1,E
5009: 17         RLA
500A: CB 12      RL          1,E
500C: 17         RLA
500D: CB 12      RL          1,E
500F: 17         RLA
5010: CB 12      RL          1,E
5012: 17         RLA
5013: CB 12      RL          1,E
5015: E6 E0      AND         $E0
5017: 5F         LD           E,A
5018: 21 B0 4F   LD           HL,$4FB0
501B: 19         ADD         HL,DE
501C: 0E 08      LD           C,$08
501E: CD 26 3D   CALL       $3D26
5021: 3E 08      LD           A,$08
5023: CD D0 3D   CALL       $3DD0
5026: 21 B0 C3   LD           HL,$C3B0
5029: 09         ADD         HL,BC
502A: 7E         LD           A,(HL)
502B: FE FF      CP           $FF
502D: 28 1B      JR           Z,$504A
502F: 21 10 C3   LD           HL,$C310
5032: 09         ADD         HL,BC
5033: 7E         LD           A,(HL)
5034: A7         AND         A
5035: 28 13      JR           Z,$504A
5037: F0 EF      LD           A,($EF)
5039: D6 02      SUB         $02
503B: E0 EC      LDFF00   ($EC),A
503D: 21 F0 4F   LD           HL,$4FF0
5040: 0E 04      LD           C,$04
5042: CD 26 3D   CALL       $3D26
5045: 3E 04      LD           A,$04
5047: CD D0 3D   CALL       $3DD0
504A: C3 BA 3D   JP           $3DBA
504D: CD 91 08   CALL       $0891
5050: 36 FF      LD           (HL),$FF
5052: 21 10 C4   LD           HL,$C410
5055: 09         ADD         HL,BC
5056: 36 08      LD           (HL),$08
5058: 21 60 C3   LD           HL,$C360
505B: 09         ADD         HL,BC
505C: 36 12      LD           (HL),$12
505E: 21 00 C2   LD           HL,$C200
5061: 09         ADD         HL,BC
5062: CD 69 50   CALL       $5069
5065: 21 10 C2   LD           HL,$C210
5068: 09         ADD         HL,BC
5069: 7E         LD           A,(HL)
506A: C6 08      ADD         $08
506C: 77         LD           (HL),A
506D: 3E FF      LD           A,$FF
506F: C3 87 3B   JP           $3B87
5072: 21 B0 C2   LD           HL,$C2B0
5075: 09         ADD         HL,BC
5076: 7E         LD           A,(HL)
5077: C7         RST         0X00
5078: 80         ADD         A,B
5079: 50         LD           D,B
507A: 70         LD           (HL),B
507B: 54         LD           D,H
507C: 0B         DEC         BC
507D: 55         LD           D,L
507E: 9C         SBC         H
507F: 55         LD           D,L
5080: AF         XOR         A
5081: EA 55 C1   LD           ($C155),A
5084: CD 12 3F   CALL       $3F12
5087: CD 0E 38   CALL       $380E
508A: CD 38 54   CALL       $5438
508D: F0 EA      LD           A,($EA)
508F: FE 05      CP           $05
5091: CA 15 51   JP           Z,$5115
5094: 21 20 C4   LD           HL,$C420
5097: 09         ADD         HL,BC
5098: F0 E7      LD           A,($E7)
509A: 77         LD           (HL),A
509B: 21 40 C4   LD           HL,$C440
509E: 09         ADD         HL,BC
509F: 7E         LD           A,(HL)
50A0: C7         RST         0X00
50A1: A7         AND         A
50A2: 50         LD           D,B
50A3: E3                              
50A4: 50         LD           D,B
50A5: ED                              
50A6: 50         LD           D,B
50A7: CD 91 08   CALL       $0891
50AA: 36 80      LD           (HL),$80
50AC: 1E 0F      LD           E,$0F
50AE: 50         LD           D,B
50AF: 79         LD           A,C
50B0: BB         CP           E
50B1: 28 24      JR           Z,$50D7
50B3: 21 40 C3   LD           HL,$C340
50B6: 19         ADD         HL,DE
50B7: 7E         LD           A,(HL)
50B8: E6 80      AND         $80
50BA: 20 1B      JR           NZ,$50D7
50BC: 21 80 C2   LD           HL,$C280
50BF: 19         ADD         HL,DE
50C0: 7E         LD           A,(HL)
50C1: FE 05      CP           $05
50C3: 38 12      JR           C,$50D7
50C5: 36 01      LD           (HL),$01
50C7: 21 80 C4   LD           HL,$C480
50CA: 19         ADD         HL,DE
50CB: 36 1F      LD           (HL),$1F
50CD: 21 40 C3   LD           HL,$C340
50D0: 19         ADD         HL,DE
50D1: 7E         LD           A,(HL)
50D2: E6 F0      AND         $F0
50D4: F6 02      OR           $02
50D6: 77         LD           (HL),A
50D7: 1D         DEC         E
50D8: 7B         LD           A,E
50D9: FE FF      CP           $FF
50DB: 20 D2      JR           NZ,$50AF
50DD: 21 40 C4   LD           HL,$C440
50E0: 09         ADD         HL,BC
50E1: 34         INC         (HL)
50E2: C9         RET
50E3: CD 91 08   CALL       $0891
50E6: 20 04      JR           NZ,$50EC
50E8: 36 FF      LD           (HL),$FF
50EA: 18 F1      JR           $50DD
50EC: C9         RET
50ED: CD 91 08   CALL       $0891
50F0: CA 46 57   JP           Z,$5746
50F3: E6 07      AND         $07
50F5: 20 1D      JR           NZ,$5114
50F7: CD ED 27   CALL       $27ED
50FA: E6 1F      AND         $1F
50FC: D6 10      SUB         $10
50FE: 5F         LD           E,A
50FF: 21 EE FF   LD           HL,$FFEE
5102: 86         ADD         A,(HL)
5103: 77         LD           (HL),A
5104: CD ED 27   CALL       $27ED
5107: E6 1F      AND         $1F
5109: D6 10      SUB         $10
510B: 5F         LD           E,A
510C: 21 EC FF   LD           HL,$FFEC
510F: 86         ADD         A,(HL)
5110: 77         LD           (HL),A
5111: CD FB 59   CALL       $59FB
5114: C9         RET
5115: CD 1F 7F   CALL       $7F1F
5118: 21 20 C4   LD           HL,$C420
511B: 09         ADD         HL,BC
511C: 7E         LD           A,(HL)
511D: A7         AND         A
511E: 28 06      JR           Z,$5126
5120: 21 90 C3   LD           HL,$C390
5123: 09         ADD         HL,BC
5124: 36 FF      LD           (HL),$FF
5126: 21 40 C3   LD           HL,$C340
5129: 09         ADD         HL,BC
512A: 36 08      LD           (HL),$08
512C: F0 F0      LD           A,($F0)
512E: C7         RST         0X00
512F: 35         DEC         (HL)
5130: 51         LD           D,C
5131: 60         LD           H,B
5132: 51         LD           D,C
5133: F1         POP         AF
5134: 51         LD           D,C
5135: CD 91 08   CALL       $0891
5138: 20 05      JR           NZ,$513F
513A: 36 FF      LD           (HL),$FF
513C: CD 8D 3B   CALL       $3B8D
513F: C9         RET
5140: 03         INC         BC
5141: 03         INC         BC
5142: 03         INC         BC
5143: 03         INC         BC
5144: 03         INC         BC
5145: 02         LD           (BC),A
5146: 01 00 01   LD           BC,$0100
5149: 00         NOP
514A: 01 01 01   LD           BC,$0101
514D: 01 01 01   LD           BC,$0101
5150: 01 01 01   LD           BC,$0101
5153: 01 01 01   LD           BC,$0101
5156: 01 00 00   LD           BC,$0000
5159: 00         NOP
515A: 00         NOP
515B: 00         NOP
515C: 00         NOP
515D: 00         NOP
515E: 00         NOP
515F: 00         NOP
5160: CD 91 08   CALL       $0891
5163: 28 0F      JR           Z,$5174
5165: 1F         RRA
5166: 1F         RRA
5167: 1F         RRA
5168: E6 1F      AND         $1F
516A: 5F         LD           E,A
516B: 50         LD           D,B
516C: 21 40 51   LD           HL,$5140
516F: 19         ADD         HL,DE
5170: 7E         LD           A,(HL)
5171: C3 87 3B   JP           $3B87
5174: CD 8D 3B   CALL       $3B8D
5177: CD 8C 08   CALL       $088C
517A: 36 A0      LD           (HL),$A0
517C: CD 87 08   CALL       $0887
517F: 36 FF      LD           (HL),$FF
5181: 3E B6      LD           A,$B6
5183: CD 97 21   CALL       $2197
5186: C9         RET
5187: 03         INC         BC
5188: 02         LD           (BC),A
5189: 04         INC         B
518A: 02         LD           (BC),A
518B: 28 38      JR           Z,$51C5
518D: 48         LD           C,B
518E: 58         LD           E,B
518F: 68         LD           L,B
5190: 78         LD           A,B
5191: 28 78      JR           Z,$520B
5193: 28 78      JR           Z,$520D
5195: 28 38      JR           Z,$51CF
5197: 48         LD           C,B
5198: 58         LD           E,B
5199: 68         LD           L,B
519A: 78         LD           A,B
519B: 30 30      JR           NC,$51CD
519D: 30 30      JR           NC,$51CF
519F: 30 30      JR           NC,$51D1
51A1: 40         LD           B,B
51A2: 40         LD           B,B
51A3: 50         LD           D,B
51A4: 50         LD           D,B
51A5: 60         LD           H,B
51A6: 60         LD           H,B
51A7: 60         LD           H,B
51A8: 60         LD           H,B
51A9: 60         LD           H,B
51AA: 60         LD           H,B
51AB: 28 38      JR           Z,$51E5
51AD: 48         LD           C,B
51AE: 58         LD           E,B
51AF: 68         LD           L,B
51B0: 78         LD           A,B
51B1: 18 88      JR           $513B
51B3: 18 88      JR           $513D
51B5: 18 88      JR           $513F
51B7: 18 88      JR           $5141
51B9: 28 38      JR           Z,$51F3
51BB: 48         LD           C,B
51BC: 58         LD           E,B
51BD: 68         LD           L,B
51BE: 78         LD           A,B
51BF: 20 20      JR           NZ,$51E1
51C1: 20 20      JR           NZ,$51E3
51C3: 20 20      JR           NZ,$51E5
51C5: 30 30      JR           NC,$51F7
51C7: 40         LD           B,B
51C8: 40         LD           B,B
51C9: 50         LD           D,B
51CA: 50         LD           D,B
51CB: 60         LD           H,B
51CC: 60         LD           H,B
51CD: 70         LD           (HL),B
51CE: 70         LD           (HL),B
51CF: 70         LD           (HL),B
51D0: 70         LD           (HL),B
51D1: 70         LD           (HL),B
51D2: 70         LD           (HL),B
51D3: 00         NOP
51D4: 13         INC         DE
51D5: 01 12 02   LD           BC,$0212
51D8: 11 03 10   LD           DE,$1003
51DB: 04         INC         B
51DC: 0F         RRCA
51DD: 05         DEC         B
51DE: 0E 06      LD           C,$06
51E0: 0D         DEC         C
51E1: 07         RLCA
51E2: 0C         INC         C
51E3: 08 0B 09   LD           ($090B),SP
51E6: 0A         LD           A,(BC)
51E7: 18 88      JR           $5171
51E9: 18 88      JR           $5173
51EB: 20 70      JR           NZ,$525D
51ED: 70         LD           (HL),B
51EE: 20 00      JR           NZ,$51F0
51F0: FF         RST         0X38
51F1: F0 E7      LD           A,($E7)
51F3: E6 3F      AND         $3F
51F5: 20 0C      JR           NZ,$5203
51F7: CD ED 27   CALL       $27ED
51FA: E6 01      AND         $01
51FC: 20 05      JR           NZ,$5203
51FE: CD 91 08   CALL       $0891
5201: 36 1F      LD           (HL),$1F
5203: F0 E7      LD           A,($E7)
5205: 1F         RRA
5206: 1F         RRA
5207: 1F         RRA
5208: E6 01      AND         $01
520A: 5F         LD           E,A
520B: 50         LD           D,B
520C: 21 EF 51   LD           HL,$51EF
520F: 19         ADD         HL,DE
5210: 7E         LD           A,(HL)
5211: EA 55 C1   LD           ($C155),A
5214: CD 87 08   CALL       $0887
5217: 20 63      JR           NZ,$527C
5219: CD ED 27   CALL       $27ED
521C: E6 0F      AND         $0F
521E: C6 18      ADD         $18
5220: 77         LD           (HL),A
5221: 21 D0 C3   LD           HL,$C3D0
5224: 09         ADD         HL,BC
5225: 7E         LD           A,(HL)
5226: FE 14      CP           $14
5228: 38 52      JR           C,$527C
522A: 21 D0 C2   LD           HL,$C2D0
522D: 09         ADD         HL,BC
522E: 7E         LD           A,(HL)
522F: FE 04      CP           $04
5231: 38 49      JR           C,$527C
5233: 3E 5A      LD           A,$5A
5235: CD 01 3C   CALL       $3C01
5238: 38 42      JR           C,$527C
523A: 21 B0 C2   LD           HL,$C2B0
523D: 19         ADD         HL,DE
523E: 36 01      LD           (HL),$01
5240: CD ED 27   CALL       $27ED
5243: E6 0F      AND         $0F
5245: 21 C0 C2   LD           HL,$C2C0
5248: 09         ADD         HL,BC
5249: BE         CP           (HL)
524A: 28 F4      JR           Z,$5240
524C: 77         LD           (HL),A
524D: C5         PUSH       BC
524E: 4F         LD           C,A
524F: 21 8B 51   LD           HL,$518B
5252: 09         ADD         HL,BC
5253: 7E         LD           A,(HL)
5254: 21 00 C2   LD           HL,$C200
5257: 19         ADD         HL,DE
5258: 77         LD           (HL),A
5259: 21 9B 51   LD           HL,$519B
525C: 09         ADD         HL,BC
525D: 7E         LD           A,(HL)
525E: 21 10 C2   LD           HL,$C210
5261: 19         ADD         HL,DE
5262: 77         LD           (HL),A
5263: 21 E0 C2   LD           HL,$C2E0
5266: 19         ADD         HL,DE
5267: 36 7F      LD           (HL),$7F
5269: 21 40 C3   LD           HL,$C340
526C: 19         ADD         HL,DE
526D: 36 C2      LD           (HL),$C2
526F: 21 50 C3   LD           HL,$C350
5272: 19         ADD         HL,DE
5273: 36 00      LD           (HL),$00
5275: 21 30 C4   LD           HL,$C430
5278: 19         ADD         HL,DE
5279: 36 00      LD           (HL),$00
527B: C1         POP         BC
527C: CD 8C 08   CALL       $088C
527F: 20 51      JR           NZ,$52D2
5281: 36 40      LD           (HL),$40
5283: 21 D0 C3   LD           HL,$C3D0
5286: 09         ADD         HL,BC
5287: 7E         LD           A,(HL)
5288: FE 14      CP           $14
528A: 30 46      JR           NC,$52D2
528C: 3E 5A      LD           A,$5A
528E: CD 01 3C   CALL       $3C01
5291: 38 3F      JR           C,$52D2
5293: 21 B0 C2   LD           HL,$C2B0
5296: 19         ADD         HL,DE
5297: 36 02      LD           (HL),$02
5299: C5         PUSH       BC
529A: 21 D0 C3   LD           HL,$C3D0
529D: 09         ADD         HL,BC
529E: 4E         LD           C,(HL)
529F: 34         INC         (HL)
52A0: 21 D3 51   LD           HL,$51D3
52A3: 09         ADD         HL,BC
52A4: 4E         LD           C,(HL)
52A5: 21 AB 51   LD           HL,$51AB
52A8: 09         ADD         HL,BC
52A9: 7E         LD           A,(HL)
52AA: 21 00 C2   LD           HL,$C200
52AD: 19         ADD         HL,DE
52AE: 77         LD           (HL),A
52AF: 21 BF 51   LD           HL,$51BF
52B2: 09         ADD         HL,BC
52B3: 7E         LD           A,(HL)
52B4: 21 10 C2   LD           HL,$C210
52B7: 19         ADD         HL,DE
52B8: 77         LD           (HL),A
52B9: 21 40 C3   LD           HL,$C340
52BC: 19         ADD         HL,DE
52BD: 36 12      LD           (HL),$12
52BF: 21 50 C3   LD           HL,$C350
52C2: 19         ADD         HL,DE
52C3: 36 00      LD           (HL),$00
52C5: 21 30 C4   LD           HL,$C430
52C8: 19         ADD         HL,DE
52C9: 36 00      LD           (HL),$00
52CB: 21 D0 C4   LD           HL,$C4D0
52CE: 19         ADD         HL,DE
52CF: 36 02      LD           (HL),$02
52D1: C1         POP         BC
52D2: 21 00 C3   LD           HL,$C300
52D5: 09         ADD         HL,BC
52D6: 7E         LD           A,(HL)
52D7: A7         AND         A
52D8: 20 6F      JR           NZ,$5349
52DA: 36 40      LD           (HL),$40
52DC: 21 D0 C2   LD           HL,$C2D0
52DF: 09         ADD         HL,BC
52E0: 7E         LD           A,(HL)
52E1: FE 04      CP           $04
52E3: 30 64      JR           NC,$5349
52E5: 21 D0 C3   LD           HL,$C3D0
52E8: 09         ADD         HL,BC
52E9: 7E         LD           A,(HL)
52EA: FE 12      CP           $12
52EC: 38 5B      JR           C,$5349
52EE: 3E 5A      LD           A,$5A
52F0: CD 01 3C   CALL       $3C01
52F3: 38 54      JR           C,$5349
52F5: 21 B0 C2   LD           HL,$C2B0
52F8: 19         ADD         HL,DE
52F9: 36 03      LD           (HL),$03
52FB: C5         PUSH       BC
52FC: 21 D0 C2   LD           HL,$C2D0
52FF: 09         ADD         HL,BC
5300: 4E         LD           C,(HL)
5301: 34         INC         (HL)
5302: 21 E7 51   LD           HL,$51E7
5305: 09         ADD         HL,BC
5306: 7E         LD           A,(HL)
5307: 21 00 C2   LD           HL,$C200
530A: 19         ADD         HL,DE
530B: 77         LD           (HL),A
530C: E0 EE      LDFF00   ($EE),A
530E: 21 EB 51   LD           HL,$51EB
5311: 09         ADD         HL,BC
5312: 7E         LD           A,(HL)
5313: 21 10 C2   LD           HL,$C210
5316: 19         ADD         HL,DE
5317: 77         LD           (HL),A
5318: E0 EF      LDFF00   ($EF),A
531A: 21 40 C3   LD           HL,$C340
531D: 19         ADD         HL,DE
531E: 36 12      LD           (HL),$12
5320: 21 50 C3   LD           HL,$C350
5323: 19         ADD         HL,DE
5324: 36 00      LD           (HL),$00
5326: 21 30 C4   LD           HL,$C430
5329: 19         ADD         HL,DE
532A: 36 00      LD           (HL),$00
532C: 21 D0 C4   LD           HL,$C4D0
532F: 19         ADD         HL,DE
5330: 36 1B      LD           (HL),$1B
5332: D5         PUSH       DE
5333: C1         POP         BC
5334: 21 40 C2   LD           HL,$C240
5337: 09         ADD         HL,BC
5338: 36 01      LD           (HL),$01
533A: CD 9E 3B   CALL       $3B9E
533D: 21 A0 C2   LD           HL,$C2A0
5340: 09         ADD         HL,BC
5341: 7E         LD           A,(HL)
5342: A7         AND         A
5343: 20 03      JR           NZ,$5348
5345: CD 44 6D   CALL       $6D44
5348: C1         POP         BC
5349: CD 91 08   CALL       $0891
534C: 1F         RRA
534D: 1F         RRA
534E: 1F         RRA
534F: E6 03      AND         $03
5351: 5F         LD           E,A
5352: 50         LD           D,B
5353: 21 87 51   LD           HL,$5187
5356: 19         ADD         HL,DE
5357: 7E         LD           A,(HL)
5358: CD 87 3B   CALL       $3B87
535B: 21 20 C4   LD           HL,$C420
535E: 09         ADD         HL,BC
535F: 7E         LD           A,(HL)
5360: A7         AND         A
5361: 28 05      JR           Z,$5368
5363: 3E 02      LD           A,$02
5365: CD 87 3B   CALL       $3B87
5368: 21 90 C3   LD           HL,$C390
536B: 09         ADD         HL,BC
536C: 7E         LD           A,(HL)
536D: A7         AND         A
536E: 28 17      JR           Z,$5387
5370: 35         DEC         (HL)
5371: 1F         RRA
5372: 1F         RRA
5373: 1F         RRA
5374: 1F         RRA
5375: E6 0F      AND         $0F
5377: 5F         LD           E,A
5378: 50         LD           D,B
5379: 21 88 53   LD           HL,$5388
537C: 19         ADD         HL,DE
537D: 7E         LD           A,(HL)
537E: CD 87 3B   CALL       $3B87
5381: 21 40 C3   LD           HL,$C340
5384: 09         ADD         HL,BC
5385: 36 48      LD           (HL),$48
5387: C9         RET
5388: 02         LD           (BC),A
5389: 01 00 FF   LD           BC,$FF00
538C: FF         RST         0X38
538D: FF         RST         0X38
538E: FF         RST         0X38
538F: FF         RST         0X38
5390: FF         RST         0X38
5391: FF         RST         0X38
5392: FF         RST         0X38
5393: FF         RST         0X38
5394: FF         RST         0X38
5395: 00         NOP
5396: 01 02 F8   LD           BC,$F802
5399: F0 70      LD           A,($70)
539B: 00         NOP
539C: F8 F8      LDHL       SP,$F8
539E: 72         LD           (HL),D
539F: 00         NOP
53A0: F8 10      LDHL       SP,$10
53A2: 72         LD           (HL),D
53A3: 20 F8      JR           NZ,$539D
53A5: 18 70      JR           $5417
53A7: 20 08      JR           NZ,$53B1
53A9: F8 7C      LDHL       SP,$7C
53AB: 00         NOP
53AC: 08 00 7E   LD           ($7E00),SP
53AF: 00         NOP
53B0: 08 08 7E   LD           ($7E08),SP
53B3: 20 08      JR           NZ,$53BD
53B5: 10 7C      STOP       $7C
53B7: 20 F8      JR           NZ,$53B1
53B9: F0 74      LD           A,($74)
53BB: 00         NOP
53BC: F8 F8      LDHL       SP,$F8
53BE: 76         HALT
53BF: 00         NOP
53C0: F8 10      LDHL       SP,$10
53C2: 76         HALT
53C3: 20 F8      JR           NZ,$53BD
53C5: 18 74      JR           $543B
53C7: 20 08      JR           NZ,$53D1
53C9: F8 7C      LDHL       SP,$7C
53CB: 00         NOP
53CC: 08 00 7E   LD           ($7E00),SP
53CF: 00         NOP
53D0: 08 08 7E   LD           ($7E08),SP
53D3: 20 08      JR           NZ,$53DD
53D5: 10 7C      STOP       $7C
53D7: 20 F8      JR           NZ,$53D1
53D9: F0 74      LD           A,($74)
53DB: 00         NOP
53DC: F8 F8      LDHL       SP,$F8
53DE: 76         HALT
53DF: 00         NOP
53E0: F8 10      LDHL       SP,$10
53E2: 76         HALT
53E3: 20 F8      JR           NZ,$53DD
53E5: 18 74      JR           $545B
53E7: 20 08      JR           NZ,$53F1
53E9: F8 60      LDHL       SP,$60
53EB: 00         NOP
53EC: 08 00 62   LD           ($6200),SP
53EF: 00         NOP
53F0: 08 08 62   LD           ($6208),SP
53F3: 20 08      JR           NZ,$53FD
53F5: 10 60      STOP       $60
53F7: 20 F8      JR           NZ,$53F1
53F9: F0 78      LD           A,($78)
53FB: 00         NOP
53FC: F8 F8      LDHL       SP,$F8
53FE: 7A         LD           A,D
53FF: 00         NOP
5400: F8 10      LDHL       SP,$10
5402: 7A         LD           A,D
5403: 20 F8      JR           NZ,$53FD
5405: 18 78      JR           $547F
5407: 20 08      JR           NZ,$5411
5409: F8 60      LDHL       SP,$60
540B: 00         NOP
540C: 08 00 62   LD           ($6200),SP
540F: 00         NOP
5410: 08 08 62   LD           ($6208),SP
5413: 20 08      JR           NZ,$541D
5415: 10 60      STOP       $60
5417: 20 F8      JR           NZ,$5411
5419: F0 70      LD           A,($70)
541B: 00         NOP
541C: F8 F8      LDHL       SP,$F8
541E: 72         LD           (HL),D
541F: 00         NOP
5420: F8 10      LDHL       SP,$10
5422: 72         LD           (HL),D
5423: 20 F8      JR           NZ,$541D
5425: 18 70      JR           $5497
5427: 20 08      JR           NZ,$5431
5429: F8 60      LDHL       SP,$60
542B: 00         NOP
542C: 08 00 62   LD           ($6200),SP
542F: 00         NOP
5430: 08 08 62   LD           ($6208),SP
5433: 20 08      JR           NZ,$543D
5435: 10 60      STOP       $60
5437: 20 21      JR           NZ,$545A
5439: B0         OR           B
543A: C3 09 7E   JP           $7E09
543D: 17         RLA
543E: 17         RLA
543F: 17         RLA
5440: 17         RLA
5441: 17         RLA
5442: E6 E0      AND         $E0
5444: 5F         LD           E,A
5445: 50         LD           D,B
5446: 21 98 53   LD           HL,$5398
5449: 19         ADD         HL,DE
544A: 0E 08      LD           C,$08
544C: CD 26 3D   CALL       $3D26
544F: C9         RET
5450: 68         LD           L,B
5451: 00         NOP
5452: 68         LD           L,B
5453: 20 6A      JR           NZ,$54BF
5455: 00         NOP
5456: 6A         LD           L,D
5457: 20 6C      JR           NZ,$54C5
5459: 00         NOP
545A: 6C         LD           L,H
545B: 20 6E      JR           NZ,$54CB
545D: 00         NOP
545E: 6E         LD           L,(HL)
545F: 20 00      JR           NZ,$5461
5461: 01 02 03   LD           BC,$0302
5464: 03         INC         BC
5465: 03         INC         BC
5466: 03         INC         BC
5467: 03         INC         BC
5468: 03         INC         BC
5469: 02         LD           (BC),A
546A: 01 00 00   LD           BC,$0000
546D: 00         NOP
546E: 00         NOP
546F: 00         NOP
5470: 11 50 54   LD           DE,$5450
5473: CD 3B 3C   CALL       $3C3B
5476: CD 1F 7F   CALL       $7F1F
5479: CD 91 08   CALL       $0891
547C: CA 44 6D   JP           Z,$6D44
547F: FE 50      CP           $50
5481: 20 05      JR           NZ,$5488
5483: 21 F2 FF   LD           HL,$FFF2
5486: 36 40      LD           (HL),$40
5488: 1F         RRA
5489: 1F         RRA
548A: 1F         RRA
548B: E6 0F      AND         $0F
548D: 5F         LD           E,A
548E: 50         LD           D,B
548F: 21 60 54   LD           HL,$5460
5492: 19         ADD         HL,DE
5493: 7E         LD           A,(HL)
5494: CD 87 3B   CALL       $3B87
5497: FE 03      CP           $03
5499: 20 5F      JR           NZ,$54FA
549B: FA 1C C1   LD           A,($C11C)
549E: FE 06      CP           $06
54A0: 28 58      JR           Z,$54FA
54A2: F0 A2      LD           A,($A2)
54A4: A7         AND         A
54A5: 20 53      JR           NZ,$54FA
54A7: CD FF 6D   CALL       $6DFF
54AA: C6 08      ADD         $08
54AC: FE 10      CP           $10
54AE: 30 4A      JR           NC,$54FA
54B0: CD 0F 6E   CALL       $6E0F
54B3: C6 08      ADD         $08
54B5: FE 10      CP           $10
54B7: 30 41      JR           NC,$54FA
54B9: 3E 0C      LD           A,$0C
54BB: CD 30 3C   CALL       $3C30
54BE: F0 D7      LD           A,($D7)
54C0: 2F         CPL
54C1: 3C         INC         A
54C2: E0 9B      LDFF00   ($9B),A
54C4: F0 D8      LD           A,($D8)
54C6: 2F         CPL
54C7: 3C         INC         A
54C8: E0 9A      LDFF00   ($9A),A
54CA: C5         PUSH       BC
54CB: CD D6 20   CALL       $20D6
54CE: C1         POP         BC
54CF: CD FF 6D   CALL       $6DFF
54D2: C6 03      ADD         $03
54D4: FE 06      CP           $06
54D6: 30 22      JR           NC,$54FA
54D8: CD 0F 6E   CALL       $6E0F
54DB: C6 03      ADD         $03
54DD: FE 06      CP           $06
54DF: 30 19      JR           NC,$54FA
54E1: F0 EE      LD           A,($EE)
54E3: E0 98      LDFF00   ($98),A
54E5: 3E 06      LD           A,$06
54E7: EA 1C C1   LD           ($C11C),A
54EA: CD 3B 09   CALL       $093B
54ED: EA 98 C1   LD           ($C198),A
54F0: CD 91 08   CALL       $0891
54F3: 36 40      LD           (HL),$40
54F5: 3E 50      LD           A,$50
54F7: EA CB DB   LD           ($DBCB),A
54FA: C9         RET
54FB: 40         LD           B,B
54FC: 00         NOP
54FD: 40         LD           B,B
54FE: 20 42      JR           NZ,$5542
5500: 00         NOP
5501: 42         LD           B,D
5502: 20 70      JR           NZ,$5574
5504: 00         NOP
5505: 70         LD           (HL),B
5506: 20 72      JR           NZ,$557A
5508: 00         NOP
5509: 72         LD           (HL),D
550A: 20 11      JR           NZ,$551D
550C: FB         EI
550D: 54         LD           D,H
550E: F0 F7      LD           A,($F7)
5510: FE 01      CP           $01
5512: 20 03      JR           NZ,$5517
5514: 11 03 55   LD           DE,$5503
5517: CD 3B 3C   CALL       $3C3B
551A: CD E2 08   CALL       $08E2
551D: 21 20 C4   LD           HL,$C420
5520: 09         ADD         HL,BC
5521: 7E         LD           A,(HL)
5522: A7         AND         A
5523: 20 6F      JR           NZ,$5594
5525: CD 1F 7F   CALL       $7F1F
5528: F0 E7      LD           A,($E7)
552A: 1F         RRA
552B: 1F         RRA
552C: 1F         RRA
552D: E6 01      AND         $01
552F: CD 87 3B   CALL       $3B87
5532: F0 E7      LD           A,($E7)
5534: E6 07      AND         $07
5536: 20 04      JR           NZ,$553C
5538: 3E 3F      LD           A,$3F
553A: E0 F2      LDFF00   ($F2),A
553C: F0 F0      LD           A,($F0)
553E: C7         RST         0X00
553F: 45         LD           B,L
5540: 55         LD           D,L
5541: 64         LD           H,H
5542: 55         LD           D,L
5543: 83         ADD         A,E
5544: 55         LD           D,L
5545: CD 91 08   CALL       $0891
5548: 36 60      LD           (HL),$60
554A: CD 8D 3B   CALL       $3B8D
554D: 21 40 C4   LD           HL,$C440
5550: 09         ADD         HL,BC
5551: 7E         LD           A,(HL)
5552: FE 01      CP           $01
5554: CA 08 56   JP           Z,$5608
5557: FE 10      CP           $10
5559: CA 16 56   JP           Z,$5616
555C: FE 20      CP           $20
555E: CA 0F 56   JP           Z,$560F
5561: C3 24 56   JP           $5624
5564: CD EB 3B   CALL       $3BEB
5567: CD 91 08   CALL       $0891
556A: 28 0E      JR           Z,$557A
556C: FE 30      CP           $30
556E: 38 12      JR           C,$5582
5570: E6 03      AND         $03
5572: 20 05      JR           NZ,$5579
5574: 21 10 C3   LD           HL,$C310
5577: 09         ADD         HL,BC
5578: 34         INC         (HL)
5579: C9         RET
557A: CD 8D 3B   CALL       $3B8D
557D: 3E 18      LD           A,$18
557F: CD 25 3C   CALL       $3C25
5582: C9         RET
5583: CD 94 6D   CALL       $6D94
5586: CD 9E 3B   CALL       $3B9E
5589: CD B4 3B   CALL       $3BB4
558C: 21 A0 C2   LD           HL,$C2A0
558F: 09         ADD         HL,BC
5590: 7E         LD           A,(HL)
5591: A7         AND         A
5592: 28 03      JR           Z,$5597
5594: CD 64 3E   CALL       $3E64
5597: C9         RET
5598: F0 10      LD           A,($10)
559A: F0 30      LD           A,($30)
559C: 11 98 55   LD           DE,$5598
559F: CD 3B 3C   CALL       $3C3B
55A2: 21 20 C4   LD           HL,$C420
55A5: 09         ADD         HL,BC
55A6: 7E         LD           A,(HL)
55A7: A7         AND         A
55A8: 20 EA      JR           NZ,$5594
55AA: CD 1F 7F   CALL       $7F1F
55AD: F0 F0      LD           A,($F0)
55AF: C7         RST         0X00
55B0: B6         OR           (HL)
55B1: 55         LD           D,L
55B2: C2 55 E1   JP           NZ,$E155
55B5: 55         LD           D,L
55B6: CD 1D 56   CALL       $561D
55B9: CD 8D 3B   CALL       $3B8D
55BC: CD 91 08   CALL       $0891
55BF: 36 60      LD           (HL),$60
55C1: C9         RET
55C2: CD EB 3B   CALL       $3BEB
55C5: CD 91 08   CALL       $0891
55C8: 28 0E      JR           Z,$55D8
55CA: FE 30      CP           $30
55CC: 38 12      JR           C,$55E0
55CE: E6 03      AND         $03
55D0: 20 05      JR           NZ,$55D7
55D2: 21 10 C3   LD           HL,$C310
55D5: 09         ADD         HL,BC
55D6: 34         INC         (HL)
55D7: C9         RET
55D8: CD 8D 3B   CALL       $3B8D
55DB: 3E 18      LD           A,$18
55DD: CD 25 3C   CALL       $3C25
55E0: C9         RET
55E1: CD 94 6D   CALL       $6D94
55E4: CD 9E 3B   CALL       $3B9E
55E7: CD B4 3B   CALL       $3BB4
55EA: 21 A0 C2   LD           HL,$C2A0
55ED: 09         ADD         HL,BC
55EE: 7E         LD           A,(HL)
55EF: A7         AND         A
55F0: C2 94 55   JP           NZ,$5594
55F3: C9         RET
55F4: 10 12      STOP       $12
55F6: 11 13 10   LD           DE,$1013
55F9: 12         LD           (DE),A
55FA: 11 13 14   LD           DE,$1413
55FD: 16 15      LD           D,$15
55FF: 17         RLA
5600: 76         HALT
5601: 77         LD           (HL),A
5602: 76         HALT
5603: 77         LD           (HL),A
5604: 76         HALT
5605: 49         LD           C,C
5606: 76         HALT
5607: 49         LD           C,C
5608: 11 FC 55   LD           DE,$55FC
560B: 3E AA      LD           A,$AA
560D: 18 1A      JR           $5629
560F: 11 00 56   LD           DE,$5600
5612: 3E AE      LD           A,$AE
5614: 18 13      JR           $5629
5616: 11 04 56   LD           DE,$5604
5619: 3E 1D      LD           A,$1D
561B: 18 0C      JR           $5629
561D: 11 F8 55   LD           DE,$55F8
5620: 3E 0D      LD           A,$0D
5622: 18 05      JR           $5629
5624: 11 F4 55   LD           DE,$55F4
5627: 3E 0D      LD           A,$0D
5629: E0 D7      LDFF00   ($D7),A
562B: D5         PUSH       DE
562C: F0 EF      LD           A,($EF)
562E: D6 0F      SUB         $0F
5630: E0 CD      LDFF00   ($CD),A
5632: F0 EE      LD           A,($EE)
5634: D6 07      SUB         $07
5636: E0 CE      LDFF00   ($CE),A
5638: CB 37      SWAP        1,E
563A: E6 0F      AND         $0F
563C: 5F         LD           E,A
563D: F0 CD      LD           A,($CD)
563F: E6 F0      AND         $F0
5641: B3         OR           E
5642: 5F         LD           E,A
5643: 16 00      LD           D,$00
5645: 21 11 D7   LD           HL,$D711
5648: 19         ADD         HL,DE
5649: F0 D7      LD           A,($D7)
564B: 77         LD           (HL),A
564C: CD 39 28   CALL       $2839
564F: FA 00 D6   LD           A,($D600)
5652: 5F         LD           E,A
5653: 16 00      LD           D,$00
5655: 21 01 D6   LD           HL,$D601
5658: 19         ADD         HL,DE
5659: C6 0A      ADD         $0A
565B: EA 00 D6   LD           ($D600),A
565E: D1         POP         DE
565F: F0 CF      LD           A,($CF)
5661: 22         LD           (HLI),A
5662: F0 D0      LD           A,($D0)
5664: 22         LD           (HLI),A
5665: 3E 81      LD           A,$81
5667: 22         LD           (HLI),A
5668: 1A         LD           A,(DE)
5669: 13         INC         DE
566A: 22         LD           (HLI),A
566B: 1A         LD           A,(DE)
566C: 13         INC         DE
566D: 22         LD           (HLI),A
566E: F0 CF      LD           A,($CF)
5670: 22         LD           (HLI),A
5671: F0 D0      LD           A,($D0)
5673: 3C         INC         A
5674: 22         LD           (HLI),A
5675: 3E 81      LD           A,$81
5677: 22         LD           (HLI),A
5678: 1A         LD           A,(DE)
5679: 13         INC         DE
567A: 22         LD           (HLI),A
567B: 1A         LD           A,(DE)
567C: 22         LD           (HLI),A
567D: AF         XOR         A
567E: 77         LD           (HL),A
567F: C9         RET
5680: AF         XOR         A
5681: EA 01 D2   LD           ($D201),A
5684: 1E 80      LD           E,$80
5686: 21 00 D1   LD           HL,$D100
5689: AF         XOR         A
568A: 22         LD           (HLI),A
568B: 1D         DEC         E
568C: 20 FB      JR           NZ,$5689
568E: C9         RET
568F: 06 07      LD           B,$07
5691: 00         NOP
5692: 01 02 03   LD           BC,$0302
5695: 04         INC         B
5696: 05         DEC         B
5697: CD 1F 7F   CALL       $7F1F
569A: C3 B4 3B   JP           $3BB4
569D: CD 0E 38   CALL       $380E
56A0: CD 97 56   CALL       $5697
56A3: CD F8 58   CALL       $58F8
56A6: CD E2 08   CALL       $08E2
56A9: FA 24 C1   LD           A,($C124)
56AC: A7         AND         A
56AD: C2 80 56   JP           NZ,$5680
56B0: CD 12 3F   CALL       $3F12
56B3: F0 EA      LD           A,($EA)
56B5: FE 05      CP           $05
56B7: CA 86 57   JP           Z,$5786
56BA: F0 F0      LD           A,($F0)
56BC: C7         RST         0X00
56BD: C5         PUSH       BC
56BE: 56         LD           D,(HL)
56BF: D4 56 E5   CALL       NC,$E556
56C2: 56         LD           D,(HL)
56C3: 12         LD           (DE),A
56C4: 57         LD           D,A
56C5: CD 91 08   CALL       $0891
56C8: 36 60      LD           (HL),$60
56CA: 21 20 C4   LD           HL,$C420
56CD: 09         ADD         HL,BC
56CE: 36 FF      LD           (HL),$FF
56D0: CD 8D 3B   CALL       $3B8D
56D3: C9         RET
56D4: CD 91 08   CALL       $0891
56D7: 20 0B      JR           NZ,$56E4
56D9: 36 FF      LD           (HL),$FF
56DB: 21 20 C4   LD           HL,$C420
56DE: 09         ADD         HL,BC
56DF: 36 FF      LD           (HL),$FF
56E1: CD 8D 3B   CALL       $3B8D
56E4: C9         RET
56E5: CD 91 08   CALL       $0891
56E8: E6 1F      AND         $1F
56EA: 20 0D      JR           NZ,$56F9
56EC: 21 D0 C2   LD           HL,$C2D0
56EF: 09         ADD         HL,BC
56F0: 7E         LD           A,(HL)
56F1: FE 04      CP           $04
56F3: 28 05      JR           Z,$56FA
56F5: 34         INC         (HL)
56F6: CD FB 59   CALL       $59FB
56F9: C9         RET
56FA: CD 91 08   CALL       $0891
56FD: 36 30      LD           (HL),$30
56FF: C3 8D 3B   JP           $3B8D
5702: 00         NOP
5703: 06 08      LD           B,$08
5705: 06 00      LD           B,$00
5707: FA F8 FA   LD           A,($FAF8)
570A: F8 FA      LDHL       SP,$FA
570C: 00         NOP
570D: 06 08      LD           B,$08
570F: 06 00      LD           B,$00
5711: FA CD 91   LD           A,($91CD)
5714: 08 CA 46   LD           ($46CA),SP
5717: 57         LD           D,A
5718: E6 03      AND         $03
571A: 20 29      JR           NZ,$5745
571C: 7E         LD           A,(HL)
571D: 1F         RRA
571E: 1F         RRA
571F: E6 07      AND         $07
5721: 5F         LD           E,A
5722: 50         LD           D,B
5723: 21 02 57   LD           HL,$5702
5726: 19         ADD         HL,DE
5727: F0 EE      LD           A,($EE)
5729: 86         ADD         A,(HL)
572A: E0 EE      LDFF00   ($EE),A
572C: 21 0A 57   LD           HL,$570A
572F: 19         ADD         HL,DE
5730: F0 EC      LD           A,($EC)
5732: 86         ADD         A,(HL)
5733: E0 EC      LDFF00   ($EC),A
5735: CD FB 59   CALL       $59FB
5738: CD 91 08   CALL       $0891
573B: FE 10      CP           $10
573D: 20 06      JR           NZ,$5745
573F: 21 D0 C2   LD           HL,$C2D0
5742: 09         ADD         HL,BC
5743: 36 05      LD           (HL),$05
5745: C9         RET
5746: 3E 36      LD           A,$36
5748: CD 01 3C   CALL       $3C01
574B: F0 D7      LD           A,($D7)
574D: FE 88      CP           $88
574F: 38 02      JR           C,$5753
5751: 3E 88      LD           A,$88
5753: FE 18      CP           $18
5755: 30 02      JR           NC,$5759
5757: 3E 18      LD           A,$18
5759: 21 00 C2   LD           HL,$C200
575C: 19         ADD         HL,DE
575D: 77         LD           (HL),A
575E: F0 D8      LD           A,($D8)
5760: FE 70      CP           $70
5762: 38 02      JR           C,$5766
5764: 3E 70      LD           A,$70
5766: FE 20      CP           $20
5768: 30 02      JR           NC,$576C
576A: 3E 20      LD           A,$20
576C: 21 10 C2   LD           HL,$C210
576F: 19         ADD         HL,DE
5770: 77         LD           (HL),A
5771: 21 20 C3   LD           HL,$C320
5774: 19         ADD         HL,DE
5775: 36 10      LD           (HL),$10
5777: F0 DA      LD           A,($DA)
5779: 21 10 C3   LD           HL,$C310
577C: 19         ADD         HL,DE
577D: 77         LD           (HL),A
577E: 21 F4 FF   LD           HL,$FFF4
5781: 36 1A      LD           (HL),$1A
5783: C3 44 6D   JP           $6D44
5786: CD BA 3D   CALL       $3DBA
5789: CD 1F 7F   CALL       $7F1F
578C: AF         XOR         A
578D: EA D6 D3   LD           ($D3D6),A
5790: 1E 10      LD           E,$10
5792: 21 60 C3   LD           HL,$C360
5795: 09         ADD         HL,BC
5796: 7E         LD           A,(HL)
5797: FE 02      CP           $02
5799: 38 08      JR           C,$57A3
579B: 21 00 C3   LD           HL,$C300
579E: 09         ADD         HL,BC
579F: 7E         LD           A,(HL)
57A0: A7         AND         A
57A1: 28 0A      JR           Z,$57AD
57A3: CD BB 57   CALL       $57BB
57A6: 3E 01      LD           A,$01
57A8: EA D6 D3   LD           ($D3D6),A
57AB: 1E 0B      LD           E,$0B
57AD: 21 01 D2   LD           HL,$D201
57B0: 7E         LD           A,(HL)
57B1: 3C         INC         A
57B2: 77         LD           (HL),A
57B3: BB         CP           E
57B4: 38 05      JR           C,$57BB
57B6: 70         LD           (HL),B
57B7: 3E 1B      LD           A,$1B
57B9: E0 F4      LDFF00   ($F4),A
57BB: 21 D0 C3   LD           HL,$C3D0
57BE: 09         ADD         HL,BC
57BF: 7E         LD           A,(HL)
57C0: 3C         INC         A
57C1: E6 7F      AND         $7F
57C3: 77         LD           (HL),A
57C4: 5F         LD           E,A
57C5: 50         LD           D,B
57C6: 21 00 D0   LD           HL,$D000
57C9: 19         ADD         HL,DE
57CA: F0 EE      LD           A,($EE)
57CC: 77         LD           (HL),A
57CD: 21 00 D1   LD           HL,$D100
57D0: 19         ADD         HL,DE
57D1: F0 EC      LD           A,($EC)
57D3: 77         LD           (HL),A
57D4: CD DC 5A   CALL       $5ADC
57D7: 21 B0 C2   LD           HL,$C2B0
57DA: 09         ADD         HL,BC
57DB: 5E         LD           E,(HL)
57DC: CB 3B      SRL         1,E
57DE: 50         LD           D,B
57DF: 21 8F 56   LD           HL,$568F
57E2: 19         ADD         HL,DE
57E3: 7E         LD           A,(HL)
57E4: CD 87 3B   CALL       $3B87
57E7: C9         RET
57E8: F8 F8      LDHL       SP,$F8
57EA: 60         LD           H,B
57EB: 00         NOP
57EC: F8 00      LDHL       SP,$00
57EE: 62         LD           H,D
57EF: 00         NOP
57F0: F8 08      LDHL       SP,$08
57F2: 62         LD           H,D
57F3: 20 F8      JR           NZ,$57ED
57F5: 10 60      STOP       $60
57F7: 20 08      JR           NZ,$5801
57F9: F8 64      LDHL       SP,$64
57FB: 00         NOP
57FC: 08 00 66   LD           ($6600),SP
57FF: 00         NOP
5800: 08 08 66   LD           ($6608),SP
5803: 20 08      JR           NZ,$580D
5805: 10 64      STOP       $64
5807: 20 F8      JR           NZ,$5801
5809: F8 60      LDHL       SP,$60
580B: 00         NOP
580C: F8 00      LDHL       SP,$00
580E: 62         LD           H,D
580F: 00         NOP
5810: F8 08      LDHL       SP,$08
5812: 62         LD           H,D
5813: 20 F8      JR           NZ,$580D
5815: 10 60      STOP       $60
5817: 20 08      JR           NZ,$5821
5819: F8 6C      LDHL       SP,$6C
581B: 00         NOP
581C: 08 00 6E   LD           ($6E00),SP
581F: 00         NOP
5820: 08 08 62   LD           ($6208),SP
5823: 60         LD           H,B
5824: 08 10 60   LD           ($6010),SP
5827: 60         LD           H,B
5828: F8 F8      LDHL       SP,$F8
582A: 68         LD           L,B
582B: 00         NOP
582C: F8 00      LDHL       SP,$00
582E: 6A         LD           L,D
582F: 00         NOP
5830: F8 08      LDHL       SP,$08
5832: 62         LD           H,D
5833: 20 F8      JR           NZ,$582D
5835: 10 60      STOP       $60
5837: 20 08      JR           NZ,$5841
5839: F8 68      LDHL       SP,$68
583B: 40         LD           B,B
583C: 08 00 6A   LD           ($6A00),SP
583F: 40         LD           B,B
5840: 08 08 62   LD           ($6208),SP
5843: 60         LD           H,B
5844: 08 10 60   LD           ($6010),SP
5847: 60         LD           H,B
5848: F8 F8      LDHL       SP,$F8
584A: 6C         LD           L,H
584B: 40         LD           B,B
584C: F8 00      LDHL       SP,$00
584E: 6E         LD           L,(HL)
584F: 40         LD           B,B
5850: F8 08      LDHL       SP,$08
5852: 62         LD           H,D
5853: 20 F8      JR           NZ,$584D
5855: 10 60      STOP       $60
5857: 20 08      JR           NZ,$5861
5859: F8 60      LDHL       SP,$60
585B: 40         LD           B,B
585C: 08 00 62   LD           ($6200),SP
585F: 40         LD           B,B
5860: 08 08 62   LD           ($6208),SP
5863: 60         LD           H,B
5864: 08 10 60   LD           ($6010),SP
5867: 60         LD           H,B
5868: F8 F8      LDHL       SP,$F8
586A: 64         LD           H,H
586B: 40         LD           B,B
586C: F8 00      LDHL       SP,$00
586E: 66         LD           H,(HL)
586F: 40         LD           B,B
5870: F8 08      LDHL       SP,$08
5872: 66         LD           H,(HL)
5873: 60         LD           H,B
5874: F8 10      LDHL       SP,$10
5876: 64         LD           H,H
5877: 60         LD           H,B
5878: 08 F8 60   LD           ($60F8),SP
587B: 40         LD           B,B
587C: 08 00 62   LD           ($6200),SP
587F: 40         LD           B,B
5880: 08 08 62   LD           ($6208),SP
5883: 60         LD           H,B
5884: 08 10 60   LD           ($6010),SP
5887: 60         LD           H,B
5888: F8 F8      LDHL       SP,$F8
588A: 60         LD           H,B
588B: 00         NOP
588C: F8 00      LDHL       SP,$00
588E: 62         LD           H,D
588F: 00         NOP
5890: F8 08      LDHL       SP,$08
5892: 6E         LD           L,(HL)
5893: 60         LD           H,B
5894: F8 10      LDHL       SP,$10
5896: 6C         LD           L,H
5897: 60         LD           H,B
5898: 08 F8 60   LD           ($60F8),SP
589B: 40         LD           B,B
589C: 08 00 62   LD           ($6200),SP
589F: 40         LD           B,B
58A0: 08 08 62   LD           ($6208),SP
58A3: 60         LD           H,B
58A4: 08 10 60   LD           ($6010),SP
58A7: 60         LD           H,B
58A8: F8 F8      LDHL       SP,$F8
58AA: 60         LD           H,B
58AB: 00         NOP
58AC: F8 00      LDHL       SP,$00
58AE: 62         LD           H,D
58AF: 00         NOP
58B0: F8 08      LDHL       SP,$08
58B2: 6A         LD           L,D
58B3: 20 F8      JR           NZ,$58AD
58B5: 10 68      STOP       $68
58B7: 20 08      JR           NZ,$58C1
58B9: F8 60      LDHL       SP,$60
58BB: 40         LD           B,B
58BC: 08 00 62   LD           ($6200),SP
58BF: 40         LD           B,B
58C0: 08 08 6A   LD           ($6A08),SP
58C3: 60         LD           H,B
58C4: 08 10 68   LD           ($6810),SP
58C7: 60         LD           H,B
58C8: F8 F8      LDHL       SP,$F8
58CA: 60         LD           H,B
58CB: 00         NOP
58CC: F8 00      LDHL       SP,$00
58CE: 62         LD           H,D
58CF: 00         NOP
58D0: F8 08      LDHL       SP,$08
58D2: 62         LD           H,D
58D3: 20 F8      JR           NZ,$58CD
58D5: 10 60      STOP       $60
58D7: 20 08      JR           NZ,$58E1
58D9: F8 60      LDHL       SP,$60
58DB: 40         LD           B,B
58DC: 08 00 62   LD           ($6200),SP
58DF: 40         LD           B,B
58E0: 08 08 6E   LD           ($6E08),SP
58E3: 20 08      JR           NZ,$58ED
58E5: 10 6C      STOP       $6C
58E7: 20 70      JR           NZ,$5959
58E9: 00         NOP
58EA: 70         LD           (HL),B
58EB: 20 72      JR           NZ,$595F
58ED: 00         NOP
58EE: 72         LD           (HL),D
58EF: 20 74      JR           NZ,$5965
58F1: 00         NOP
58F2: 74         LD           (HL),H
58F3: 20 76      JR           NZ,$596B
58F5: 00         NOP
58F6: 76         HALT
58F7: 20 21      JR           NZ,$591A
58F9: D0         RET         NC
58FA: C2 09 7E   JP           NZ,$7E09
58FD: FE 05      CP           $05
58FF: D2 FA 59   JP           NC,$59FA
5902: 21 40 C3   LD           HL,$C340
5905: 09         ADD         HL,BC
5906: 36 08      LD           (HL),$08
5908: 21 B0 C3   LD           HL,$C3B0
590B: 09         ADD         HL,BC
590C: 7E         LD           A,(HL)
590D: 17         RLA
590E: 17         RLA
590F: 17         RLA
5910: 17         RLA
5911: 17         RLA
5912: E6 E0      AND         $E0
5914: 5F         LD           E,A
5915: 50         LD           D,B
5916: 21 E8 57   LD           HL,$57E8
5919: 19         ADD         HL,DE
591A: 0E 08      LD           C,$08
591C: CD 26 3D   CALL       $3D26
591F: 21 40 C3   LD           HL,$C340
5922: 09         ADD         HL,BC
5923: 36 02      LD           (HL),$02
5925: 21 D0 C3   LD           HL,$C3D0
5928: 09         ADD         HL,BC
5929: 7E         LD           A,(HL)
592A: E0 D7      LDFF00   ($D7),A
592C: 21 D0 C2   LD           HL,$C2D0
592F: 09         ADD         HL,BC
5930: 7E         LD           A,(HL)
5931: FE 04      CP           $04
5933: D2 FA 59   JP           NC,$59FA
5936: F0 D7      LD           A,($D7)
5938: D6 0C      SUB         $0C
593A: E6 7F      AND         $7F
593C: 5F         LD           E,A
593D: 50         LD           D,B
593E: 21 00 D0   LD           HL,$D000
5941: 19         ADD         HL,DE
5942: 7E         LD           A,(HL)
5943: E0 EE      LDFF00   ($EE),A
5945: 21 00 D1   LD           HL,$D100
5948: 19         ADD         HL,DE
5949: 7E         LD           A,(HL)
594A: E0 EC      LDFF00   ($EC),A
594C: 3E 00      LD           A,$00
594E: E0 F1      LDFF00   ($F1),A
5950: 11 E8 58   LD           DE,$58E8
5953: CD 3B 3C   CALL       $3C3B
5956: 21 D0 C2   LD           HL,$C2D0
5959: 09         ADD         HL,BC
595A: 7E         LD           A,(HL)
595B: FE 03      CP           $03
595D: D2 FA 59   JP           NC,$59FA
5960: F0 D7      LD           A,($D7)
5962: D6 18      SUB         $18
5964: E6 7F      AND         $7F
5966: 5F         LD           E,A
5967: 50         LD           D,B
5968: 21 00 D0   LD           HL,$D000
596B: 19         ADD         HL,DE
596C: 7E         LD           A,(HL)
596D: E0 EE      LDFF00   ($EE),A
596F: 21 00 D1   LD           HL,$D100
5972: 19         ADD         HL,DE
5973: 7E         LD           A,(HL)
5974: E0 EC      LDFF00   ($EC),A
5976: 3E 00      LD           A,$00
5978: E0 F1      LDFF00   ($F1),A
597A: 11 E8 58   LD           DE,$58E8
597D: CD 3B 3C   CALL       $3C3B
5980: 21 D0 C2   LD           HL,$C2D0
5983: 09         ADD         HL,BC
5984: 7E         LD           A,(HL)
5985: FE 02      CP           $02
5987: 30 71      JR           NC,$59FA
5989: F0 D7      LD           A,($D7)
598B: D6 24      SUB         $24
598D: E6 7F      AND         $7F
598F: 5F         LD           E,A
5990: 50         LD           D,B
5991: 21 00 D0   LD           HL,$D000
5994: 19         ADD         HL,DE
5995: 7E         LD           A,(HL)
5996: E0 EE      LDFF00   ($EE),A
5998: 21 00 D1   LD           HL,$D100
599B: 19         ADD         HL,DE
599C: 7E         LD           A,(HL)
599D: E0 EC      LDFF00   ($EC),A
599F: 3E 01      LD           A,$01
59A1: E0 F1      LDFF00   ($F1),A
59A3: 11 E8 58   LD           DE,$58E8
59A6: CD 3B 3C   CALL       $3C3B
59A9: 21 D0 C2   LD           HL,$C2D0
59AC: 09         ADD         HL,BC
59AD: 7E         LD           A,(HL)
59AE: A7         AND         A
59AF: 20 49      JR           NZ,$59FA
59B1: F0 D7      LD           A,($D7)
59B3: D6 2E      SUB         $2E
59B5: E6 7F      AND         $7F
59B7: 5F         LD           E,A
59B8: 50         LD           D,B
59B9: 21 00 D0   LD           HL,$D000
59BC: 19         ADD         HL,DE
59BD: 7E         LD           A,(HL)
59BE: E0 EE      LDFF00   ($EE),A
59C0: 21 00 D1   LD           HL,$D100
59C3: 19         ADD         HL,DE
59C4: 7E         LD           A,(HL)
59C5: E0 EC      LDFF00   ($EC),A
59C7: F0 E7      LD           A,($E7)
59C9: 1F         RRA
59CA: 1F         RRA
59CB: 1F         RRA
59CC: E6 01      AND         $01
59CE: C6 02      ADD         $02
59D0: E0 F1      LDFF00   ($F1),A
59D2: F0 E7      LD           A,($E7)
59D4: 17         RLA
59D5: 17         RLA
59D6: E6 10      AND         $10
59D8: 21 ED FF   LD           HL,$FFED
59DB: AE         XOR         (HL)
59DC: 77         LD           (HL),A
59DD: 11 E8 58   LD           DE,$58E8
59E0: CD 3B 3C   CALL       $3C3B
59E3: 21 20 C4   LD           HL,$C420
59E6: 09         ADD         HL,BC
59E7: 7E         LD           A,(HL)
59E8: A7         AND         A
59E9: 20 0F      JR           NZ,$59FA
59EB: 21 30 C4   LD           HL,$C430
59EE: 09         ADD         HL,BC
59EF: 36 90      LD           (HL),$90
59F1: CD EB 3B   CALL       $3BEB
59F4: 21 30 C4   LD           HL,$C430
59F7: 09         ADD         HL,BC
59F8: 36 D0      LD           (HL),$D0
59FA: C9         RET
59FB: CD 25 7F   CALL       $7F25
59FE: F0 EE      LD           A,($EE)
5A00: E0 D7      LDFF00   ($D7),A
5A02: F0 EC      LD           A,($EC)
5A04: E0 D8      LDFF00   ($D8),A
5A06: 3E 02      LD           A,$02
5A08: CD 53 09   CALL       $0953
5A0B: 3E 13      LD           A,$13
5A0D: E0 F4      LDFF00   ($F4),A
5A0F: C9         RET
5A10: 21 60 C4   LD           HL,$C460
5A13: 09         ADD         HL,BC
5A14: 5E         LD           E,(HL)
5A15: CB 23      SLA         1,E
5A17: CB 23      SLA         1,E
5A19: CB 23      SLA         1,E
5A1B: CB 23      SLA         1,E
5A1D: CB 23      SLA         1,E
5A1F: 50         LD           D,B
5A20: 21 00 D0   LD           HL,$D000
5A23: 19         ADD         HL,DE
5A24: D5         PUSH       DE
5A25: 1E 20      LD           E,$20
5A27: AF         XOR         A
5A28: 22         LD           (HLI),A
5A29: 1D         DEC         E
5A2A: 7B         LD           A,E
5A2B: FE 00      CP           $00
5A2D: 20 F8      JR           NZ,$5A27
5A2F: D1         POP         DE
5A30: 21 00 D1   LD           HL,$D100
5A33: 19         ADD         HL,DE
5A34: 1E 20      LD           E,$20
5A36: AF         XOR         A
5A37: 22         LD           (HLI),A
5A38: 1D         DEC         E
5A39: 7B         LD           A,E
5A3A: FE 00      CP           $00
5A3C: 20 F8      JR           NZ,$5A36
5A3E: C9         RET
5A3F: 70         LD           (HL),B
5A40: 00         NOP
5A41: 70         LD           (HL),B
5A42: 20 70      JR           NZ,$5AB4
5A44: 40         LD           B,B
5A45: 70         LD           (HL),B
5A46: 60         LD           H,B
5A47: 72         LD           (HL),D
5A48: 00         NOP
5A49: 74         LD           (HL),H
5A4A: 00         NOP
5A4B: 74         LD           (HL),H
5A4C: 20 72      JR           NZ,$5AC0
5A4E: 20 76      JR           NZ,$5AC6
5A50: 00         NOP
5A51: 78         LD           A,B
5A52: 00         NOP
5A53: 78         LD           A,B
5A54: 20 76      JR           NZ,$5ACC
5A56: 20 76      JR           NZ,$5ACE
5A58: 40         LD           B,B
5A59: 78         LD           A,B
5A5A: 40         LD           B,B
5A5B: 78         LD           A,B
5A5C: 60         LD           H,B
5A5D: 76         HALT
5A5E: 60         LD           H,B
5A5F: 7A         LD           A,D
5A60: 00         NOP
5A61: 7A         LD           A,D
5A62: 20 7C      JR           NZ,$5AE0
5A64: 00         NOP
5A65: 7C         LD           A,H
5A66: 20 03      JR           NZ,$5A6B
5A68: 03         INC         BC
5A69: 05         DEC         B
5A6A: 05         DEC         B
5A6B: 00         NOP
5A6C: 00         NOP
5A6D: 04         INC         B
5A6E: 04         INC         B
5A6F: 02         LD           (BC),A
5A70: 02         LD           (BC),A
5A71: 06 06      LD           B,$06
5A73: 01 01 07   LD           BC,$0701
5A76: 07         RLCA
5A77: 00         NOP
5A78: 06 0C      LD           B,$0C
5A7A: 0E 10      LD           C,$10
5A7C: 0E 0C      LD           C,$0C
5A7E: 06 00      LD           B,$00
5A80: FA F4 F2   LD           A,($F2F4)
5A83: F0 F2      LD           A,($F2)
5A85: F4                              
5A86: FA 00 06   LD           A,($0600)
5A89: 0C         INC         C
5A8A: 0E CD      LD           C,$CD
5A8C: 75         LD           (HL),L
5A8D: 5B         LD           E,E
5A8E: FA 24 C1   LD           A,($C124)
5A91: A7         AND         A
5A92: 20 08      JR           NZ,$5A9C
5A94: 21 10 C4   LD           HL,$C410
5A97: 09         ADD         HL,BC
5A98: 7E         LD           A,(HL)
5A99: A7         AND         A
5A9A: 28 03      JR           Z,$5A9F
5A9C: CD 10 5A   CALL       $5A10
5A9F: CD 1F 7F   CALL       $7F1F
5AA2: 21 D0 C3   LD           HL,$C3D0
5AA5: 09         ADD         HL,BC
5AA6: 7E         LD           A,(HL)
5AA7: 3C         INC         A
5AA8: E6 1F      AND         $1F
5AAA: 77         LD           (HL),A
5AAB: E0 D7      LDFF00   ($D7),A
5AAD: 21 60 C4   LD           HL,$C460
5AB0: 09         ADD         HL,BC
5AB1: 5E         LD           E,(HL)
5AB2: CB 23      SLA         1,E
5AB4: CB 23      SLA         1,E
5AB6: CB 23      SLA         1,E
5AB8: CB 23      SLA         1,E
5ABA: CB 23      SLA         1,E
5ABC: 16 00      LD           D,$00
5ABE: D5         PUSH       DE
5ABF: 21 00 D0   LD           HL,$D000
5AC2: 19         ADD         HL,DE
5AC3: F0 D7      LD           A,($D7)
5AC5: 5F         LD           E,A
5AC6: 19         ADD         HL,DE
5AC7: F0 EE      LD           A,($EE)
5AC9: 77         LD           (HL),A
5ACA: D1         POP         DE
5ACB: 21 00 D1   LD           HL,$D100
5ACE: 19         ADD         HL,DE
5ACF: F0 D7      LD           A,($D7)
5AD1: 5F         LD           E,A
5AD2: 19         ADD         HL,DE
5AD3: F0 EC      LD           A,($EC)
5AD5: 77         LD           (HL),A
5AD6: CD 4A 6D   CALL       $6D4A
5AD9: CD B4 3B   CALL       $3BB4
5ADC: 21 20 C4   LD           HL,$C420
5ADF: 09         ADD         HL,BC
5AE0: 7E         LD           A,(HL)
5AE1: A7         AND         A
5AE2: 20 03      JR           NZ,$5AE7
5AE4: CD 94 6D   CALL       $6D94
5AE7: CD 9E 3B   CALL       $3B9E
5AEA: 21 A0 C2   LD           HL,$C2A0
5AED: 09         ADD         HL,BC
5AEE: 7E         LD           A,(HL)
5AEF: A7         AND         A
5AF0: 28 2C      JR           Z,$5B1E
5AF2: 1E 08      LD           E,$08
5AF4: CB 47      BIT         1,E
5AF6: 20 0E      JR           NZ,$5B06
5AF8: 1E 00      LD           E,$00
5AFA: CB 4F      BIT         1,E
5AFC: 20 08      JR           NZ,$5B06
5AFE: 1E 04      LD           E,$04
5B00: CB 57      BIT         1,E
5B02: 20 02      JR           NZ,$5B06
5B04: 1E 0C      LD           E,$0C
5B06: 21 B0 C2   LD           HL,$C2B0
5B09: 09         ADD         HL,BC
5B0A: 73         LD           (HL),E
5B0B: CD ED 27   CALL       $27ED
5B0E: 1F         RRA
5B0F: 38 08      JR           C,$5B19
5B11: 21 C0 C2   LD           HL,$C2C0
5B14: 09         ADD         HL,BC
5B15: 7E         LD           A,(HL)
5B16: 2F         CPL
5B17: 3C         INC         A
5B18: 77         LD           (HL),A
5B19: CD 91 08   CALL       $0891
5B1C: 36 10      LD           (HL),$10
5B1E: CD 8C 08   CALL       $088C
5B21: 20 39      JR           NZ,$5B5C
5B23: 36 04      LD           (HL),$04
5B25: F0 EB      LD           A,($EB)
5B27: FE 59      CP           $59
5B29: 20 02      JR           NZ,$5B2D
5B2B: 36 06      LD           (HL),$06
5B2D: 21 C0 C2   LD           HL,$C2C0
5B30: 09         ADD         HL,BC
5B31: 7E         LD           A,(HL)
5B32: 21 B0 C2   LD           HL,$C2B0
5B35: 09         ADD         HL,BC
5B36: 86         ADD         A,(HL)
5B37: E6 0F      AND         $0F
5B39: 77         LD           (HL),A
5B3A: 21 B0 C2   LD           HL,$C2B0
5B3D: 09         ADD         HL,BC
5B3E: 5E         LD           E,(HL)
5B3F: 50         LD           D,B
5B40: 21 67 5A   LD           HL,$5A67
5B43: 19         ADD         HL,DE
5B44: 7E         LD           A,(HL)
5B45: CD 87 3B   CALL       $3B87
5B48: 21 77 5A   LD           HL,$5A77
5B4B: 19         ADD         HL,DE
5B4C: 7E         LD           A,(HL)
5B4D: 21 50 C2   LD           HL,$C250
5B50: 09         ADD         HL,BC
5B51: 77         LD           (HL),A
5B52: 21 7B 5A   LD           HL,$5A7B
5B55: 19         ADD         HL,DE
5B56: 7E         LD           A,(HL)
5B57: 21 40 C2   LD           HL,$C240
5B5A: 09         ADD         HL,BC
5B5B: 77         LD           (HL),A
5B5C: CD 91 08   CALL       $0891
5B5F: 20 13      JR           NZ,$5B74
5B61: CD ED 27   CALL       $27ED
5B64: E6 1F      AND         $1F
5B66: C6 10      ADD         $10
5B68: 77         LD           (HL),A
5B69: CD ED 27   CALL       $27ED
5B6C: E6 02      AND         $02
5B6E: 3D         DEC         A
5B6F: 21 C0 C2   LD           HL,$C2C0
5B72: 09         ADD         HL,BC
5B73: 77         LD           (HL),A
5B74: C9         RET
5B75: 11 3F 5A   LD           DE,$5A3F
5B78: CD 3B 3C   CALL       $3C3B
5B7B: CD 1F 7F   CALL       $7F1F
5B7E: 21 D0 C3   LD           HL,$C3D0
5B81: 09         ADD         HL,BC
5B82: 7E         LD           A,(HL)
5B83: E0 D7      LDFF00   ($D7),A
5B85: 21 60 C4   LD           HL,$C460
5B88: 09         ADD         HL,BC
5B89: 5E         LD           E,(HL)
5B8A: CB 23      SLA         1,E
5B8C: CB 23      SLA         1,E
5B8E: CB 23      SLA         1,E
5B90: CB 23      SLA         1,E
5B92: CB 23      SLA         1,E
5B94: 50         LD           D,B
5B95: D5         PUSH       DE
5B96: D5         PUSH       DE
5B97: 21 00 D0   LD           HL,$D000
5B9A: 19         ADD         HL,DE
5B9B: F0 D7      LD           A,($D7)
5B9D: D6 09      SUB         $09
5B9F: E6 1F      AND         $1F
5BA1: 5F         LD           E,A
5BA2: 50         LD           D,B
5BA3: 19         ADD         HL,DE
5BA4: 7E         LD           A,(HL)
5BA5: E0 EE      LDFF00   ($EE),A
5BA7: D1         POP         DE
5BA8: 21 00 D1   LD           HL,$D100
5BAB: 19         ADD         HL,DE
5BAC: F0 D7      LD           A,($D7)
5BAE: D6 09      SUB         $09
5BB0: E6 1F      AND         $1F
5BB2: 5F         LD           E,A
5BB3: 50         LD           D,B
5BB4: 19         ADD         HL,DE
5BB5: 7E         LD           A,(HL)
5BB6: E0 EC      LDFF00   ($EC),A
5BB8: 3E 08      LD           A,$08
5BBA: E0 F1      LDFF00   ($F1),A
5BBC: 11 3F 5A   LD           DE,$5A3F
5BBF: CD 3B 3C   CALL       $3C3B
5BC2: D1         POP         DE
5BC3: D5         PUSH       DE
5BC4: 21 00 D0   LD           HL,$D000
5BC7: 19         ADD         HL,DE
5BC8: F0 D7      LD           A,($D7)
5BCA: D6 10      SUB         $10
5BCC: E6 1F      AND         $1F
5BCE: 5F         LD           E,A
5BCF: 50         LD           D,B
5BD0: 19         ADD         HL,DE
5BD1: 7E         LD           A,(HL)
5BD2: E0 EE      LDFF00   ($EE),A
5BD4: D1         POP         DE
5BD5: 21 00 D1   LD           HL,$D100
5BD8: 19         ADD         HL,DE
5BD9: F0 D7      LD           A,($D7)
5BDB: D6 10      SUB         $10
5BDD: E6 1F      AND         $1F
5BDF: 5F         LD           E,A
5BE0: 50         LD           D,B
5BE1: 19         ADD         HL,DE
5BE2: 7E         LD           A,(HL)
5BE3: E0 EC      LDFF00   ($EC),A
5BE5: 3E 09      LD           A,$09
5BE7: E0 F1      LDFF00   ($F1),A
5BE9: 11 3F 5A   LD           DE,$5A3F
5BEC: CD 3B 3C   CALL       $3C3B
5BEF: CD BA 3D   CALL       $3DBA
5BF2: C9         RET
5BF3: 58         LD           E,B
5BF4: 00         NOP
5BF5: 5A         LD           E,D
5BF6: 00         NOP
5BF7: 5C         LD           E,H
5BF8: 00         NOP
5BF9: 5E         LD           E,(HL)
5BFA: 00         NOP
5BFB: 0C         INC         C
5BFC: F4                              
5BFD: 08 F8 CD   LD           ($CDF8),SP
5C00: 9D         SBC         L
5C01: 5D         LD           E,L
5C02: 18 09      JR           $5C0D
5C04: CD 0C 7F   CALL       $7F0C
5C07: 11 F3 5B   LD           DE,$5BF3
5C0A: CD 3B 3C   CALL       $3C3B
5C0D: F0 F0      LD           A,($F0)
5C0F: A7         AND         A
5C10: 28 28      JR           Z,$5C3A
5C12: 3E FF      LD           A,$FF
5C14: CD 87 3B   CALL       $3B87
5C17: CD FF 6D   CALL       $6DFF
5C1A: C6 10      ADD         $10
5C1C: FE 20      CP           $20
5C1E: 30 19      JR           NC,$5C39
5C20: CD 0F 6E   CALL       $6E0F
5C23: C6 10      ADD         $10
5C25: FE 20      CP           $20
5C27: 30 10      JR           NC,$5C39
5C29: FA 33 C1   LD           A,($C133)
5C2C: A7         AND         A
5C2D: 28 0A      JR           Z,$5C39
5C2F: CD 8D 3B   CALL       $3B8D
5C32: 70         LD           (HL),B
5C33: 21 00 C3   LD           HL,$C300
5C36: 09         ADD         HL,BC
5C37: 36 30      LD           (HL),$30
5C39: C9         RET
5C3A: F0 E7      LD           A,($E7)
5C3C: 1F         RRA
5C3D: 1F         RRA
5C3E: 1F         RRA
5C3F: 1F         RRA
5C40: A9         XOR         C
5C41: E6 01      AND         $01
5C43: CD 87 3B   CALL       $3B87
5C46: F0 E7      LD           A,($E7)
5C48: E6 00      AND         $00
5C4A: 28 05      JR           Z,$5C51
5C4C: 3E FF      LD           A,$FF
5C4E: CD 87 3B   CALL       $3B87
5C51: CD 1F 7F   CALL       $7F1F
5C54: CD 4A 6D   CALL       $6D4A
5C57: CD EB 3B   CALL       $3BEB
5C5A: CD 94 6D   CALL       $6D94
5C5D: CD CD 6D   CALL       $6DCD
5C60: CD FF 5C   CALL       $5CFF
5C63: 21 00 C3   LD           HL,$C300
5C66: 09         ADD         HL,BC
5C67: 7E         LD           A,(HL)
5C68: A7         AND         A
5C69: C2 FE 5C   JP           NZ,$5CFE
5C6C: CD BF 3B   CALL       $3BBF
5C6F: CD 91 08   CALL       $0891
5C72: 20 0F      JR           NZ,$5C83
5C74: CD ED 27   CALL       $27ED
5C77: E6 1F      AND         $1F
5C79: C6 20      ADD         $20
5C7B: 77         LD           (HL),A
5C7C: E6 01      AND         $01
5C7E: 21 B0 C2   LD           HL,$C2B0
5C81: 09         ADD         HL,BC
5C82: 77         LD           (HL),A
5C83: CD 8C 08   CALL       $088C
5C86: 20 0F      JR           NZ,$5C97
5C88: CD ED 27   CALL       $27ED
5C8B: E6 0F      AND         $0F
5C8D: C6 18      ADD         $18
5C8F: 77         LD           (HL),A
5C90: E6 01      AND         $01
5C92: 21 C0 C2   LD           HL,$C2C0
5C95: 09         ADD         HL,BC
5C96: 77         LD           (HL),A
5C97: F0 E7      LD           A,($E7)
5C99: A9         XOR         C
5C9A: E6 03      AND         $03
5C9C: 20 60      JR           NZ,$5CFE
5C9E: 21 B0 C2   LD           HL,$C2B0
5CA1: 09         ADD         HL,BC
5CA2: F0 EE      LD           A,($EE)
5CA4: FE 28      CP           $28
5CA6: 30 04      JR           NC,$5CAC
5CA8: 36 00      LD           (HL),$00
5CAA: 18 06      JR           $5CB2
5CAC: FE 78      CP           $78
5CAE: 38 07      JR           C,$5CB7
5CB0: 36 01      LD           (HL),$01
5CB2: CD 91 08   CALL       $0891
5CB5: 36 20      LD           (HL),$20
5CB7: 21 C0 C2   LD           HL,$C2C0
5CBA: 09         ADD         HL,BC
5CBB: F0 EC      LD           A,($EC)
5CBD: FE 28      CP           $28
5CBF: 30 04      JR           NC,$5CC5
5CC1: 36 00      LD           (HL),$00
5CC3: 18 06      JR           $5CCB
5CC5: FE 60      CP           $60
5CC7: 38 07      JR           C,$5CD0
5CC9: 36 01      LD           (HL),$01
5CCB: CD 8C 08   CALL       $088C
5CCE: 36 20      LD           (HL),$20
5CD0: 21 B0 C2   LD           HL,$C2B0
5CD3: 09         ADD         HL,BC
5CD4: 5E         LD           E,(HL)
5CD5: 50         LD           D,B
5CD6: 21 FB 5B   LD           HL,$5BFB
5CD9: 19         ADD         HL,DE
5CDA: 7E         LD           A,(HL)
5CDB: 21 40 C2   LD           HL,$C240
5CDE: 09         ADD         HL,BC
5CDF: 96         SUB         (HL)
5CE0: E6 80      AND         $80
5CE2: 20 02      JR           NZ,$5CE6
5CE4: 34         INC         (HL)
5CE5: 34         INC         (HL)
5CE6: 35         DEC         (HL)
5CE7: 21 C0 C2   LD           HL,$C2C0
5CEA: 09         ADD         HL,BC
5CEB: 5E         LD           E,(HL)
5CEC: 50         LD           D,B
5CED: 21 FD 5B   LD           HL,$5BFD
5CF0: 19         ADD         HL,DE
5CF1: 7E         LD           A,(HL)
5CF2: 21 50 C2   LD           HL,$C250
5CF5: 09         ADD         HL,BC
5CF6: 96         SUB         (HL)
5CF7: E6 80      AND         $80
5CF9: 20 02      JR           NZ,$5CFD
5CFB: 34         INC         (HL)
5CFC: 34         INC         (HL)
5CFD: 35         DEC         (HL)
5CFE: C9         RET
5CFF: F0 E7      LD           A,($E7)
5D01: E6 03      AND         $03
5D03: 20 17      JR           NZ,$5D1C
5D05: 21 10 C3   LD           HL,$C310
5D08: 09         ADD         HL,BC
5D09: 7E         LD           A,(HL)
5D0A: FE 10      CP           $10
5D0C: 28 0E      JR           Z,$5D1C
5D0E: CB 7F      BIT         1,E
5D10: 28 03      JR           Z,$5D15
5D12: 34         INC         (HL)
5D13: 18 07      JR           $5D1C
5D15: FE 10      CP           $10
5D17: 30 02      JR           NC,$5D1B
5D19: 34         INC         (HL)
5D1A: C9         RET
5D1B: 35         DEC         (HL)
5D1C: C9         RET
5D1D: F8 F8      LDHL       SP,$F8
5D1F: 60         LD           H,B
5D20: 00         NOP
5D21: F8 00      LDHL       SP,$00
5D23: 62         LD           H,D
5D24: 00         NOP
5D25: F8 08      LDHL       SP,$08
5D27: 62         LD           H,D
5D28: 20 F8      JR           NZ,$5D22
5D2A: 10 60      STOP       $60
5D2C: 20 08      JR           NZ,$5D36
5D2E: F8 64      LDHL       SP,$64
5D30: 00         NOP
5D31: 08 00 66   LD           ($6600),SP
5D34: 00         NOP
5D35: 08 08 68   LD           ($6808),SP
5D38: 00         NOP
5D39: 08 10 6A   LD           ($6A10),SP
5D3C: 00         NOP
5D3D: F8 F8      LDHL       SP,$F8
5D3F: 60         LD           H,B
5D40: 00         NOP
5D41: F8 00      LDHL       SP,$00
5D43: 62         LD           H,D
5D44: 00         NOP
5D45: F8 08      LDHL       SP,$08
5D47: 62         LD           H,D
5D48: 20 F8      JR           NZ,$5D42
5D4A: 10 60      STOP       $60
5D4C: 20 08      JR           NZ,$5D56
5D4E: F8 64      LDHL       SP,$64
5D50: 00         NOP
5D51: 08 00 6C   LD           ($6C00),SP
5D54: 00         NOP
5D55: 08 08 6E   LD           ($6E08),SP
5D58: 00         NOP
5D59: 08 10 6A   LD           ($6A10),SP
5D5C: 00         NOP
5D5D: F8 F8      LDHL       SP,$F8
5D5F: 60         LD           H,B
5D60: 00         NOP
5D61: F8 00      LDHL       SP,$00
5D63: 62         LD           H,D
5D64: 00         NOP
5D65: F8 08      LDHL       SP,$08
5D67: 62         LD           H,D
5D68: 20 F8      JR           NZ,$5D62
5D6A: 10 60      STOP       $60
5D6C: 20 08      JR           NZ,$5D76
5D6E: F8 6A      LDHL       SP,$6A
5D70: 20 08      JR           NZ,$5D7A
5D72: 00         NOP
5D73: 68         LD           L,B
5D74: 20 08      JR           NZ,$5D7E
5D76: 08 66 20   LD           ($2066),SP
5D79: 08 10 64   LD           ($6410),SP
5D7C: 20 F8      JR           NZ,$5D76
5D7E: F8 60      LDHL       SP,$60
5D80: 00         NOP
5D81: F8 00      LDHL       SP,$00
5D83: 62         LD           H,D
5D84: 00         NOP
5D85: F8 08      LDHL       SP,$08
5D87: 62         LD           H,D
5D88: 20 F8      JR           NZ,$5D82
5D8A: 10 60      STOP       $60
5D8C: 20 08      JR           NZ,$5D96
5D8E: F8 6A      LDHL       SP,$6A
5D90: 20 08      JR           NZ,$5D9A
5D92: 00         NOP
5D93: 6E         LD           L,(HL)
5D94: 20 08      JR           NZ,$5D9E
5D96: 08 6C 20   LD           ($206C),SP
5D99: 08 10 64   LD           ($6410),SP
5D9C: 20 CD      JR           NZ,$5D6B
5D9E: 0C         INC         C
5D9F: 7F         LD           A,A
5DA0: F0 ED      LD           A,($ED)
5DA2: F5         PUSH       AF
5DA3: 17         RLA
5DA4: E6 40      AND         $40
5DA6: E0 D7      LDFF00   ($D7),A
5DA8: F1         POP         AF
5DA9: E6 0F      AND         $0F
5DAB: E0 ED      LDFF00   ($ED),A
5DAD: 21 B0 C3   LD           HL,$C3B0
5DB0: 09         ADD         HL,BC
5DB1: 7E         LD           A,(HL)
5DB2: 17         RLA
5DB3: 17         RLA
5DB4: 17         RLA
5DB5: 17         RLA
5DB6: 17         RLA
5DB7: E6 E0      AND         $E0
5DB9: 21 D7 FF   LD           HL,$FFD7
5DBC: 86         ADD         A,(HL)
5DBD: 5F         LD           E,A
5DBE: 50         LD           D,B
5DBF: 21 1D 5D   LD           HL,$5D1D
5DC2: 19         ADD         HL,DE
5DC3: 0E 08      LD           C,$08
5DC5: CD 26 3D   CALL       $3D26
5DC8: C9         RET
5DC9: 70         LD           (HL),B
5DCA: 00         NOP
5DCB: 72         LD           (HL),D
5DCC: 00         NOP
5DCD: 72         LD           (HL),D
5DCE: 20 70      JR           NZ,$5E40
5DD0: 20 74      JR           NZ,$5E46
5DD2: 00         NOP
5DD3: 74         LD           (HL),H
5DD4: 20 00      JR           NZ,$5DD6
5DD6: 00         NOP
5DD7: 00         NOP
5DD8: 00         NOP
5DD9: 7A         LD           A,D
5DDA: 00         NOP
5DDB: 7A         LD           A,D
5DDC: 20 FF      JR           NZ,$5DDD
5DDE: 00         NOP
5DDF: FF         RST         0X38
5DE0: 00         NOP
5DE1: 76         HALT
5DE2: 00         NOP
5DE3: 78         LD           A,B
5DE4: 00         NOP
5DE5: 78         LD           A,B
5DE6: 20 76      JR           NZ,$5E5E
5DE8: 20 F0      JR           NZ,$5DDA
5DEA: F1         POP         AF
5DEB: FE 03      CP           $03
5DED: 20 25      JR           NZ,$5E14
5DEF: F0 EE      LD           A,($EE)
5DF1: D6 08      SUB         $08
5DF3: E0 EE      LDFF00   ($EE),A
5DF5: 3E 06      LD           A,$06
5DF7: E0 F1      LDFF00   ($F1),A
5DF9: 11 C9 5D   LD           DE,$5DC9
5DFC: CD 3B 3C   CALL       $3C3B
5DFF: F0 EE      LD           A,($EE)
5E01: C6 10      ADD         $10
5E03: E0 EE      LDFF00   ($EE),A
5E05: 3E 07      LD           A,$07
5E07: E0 F1      LDFF00   ($F1),A
5E09: 11 C9 5D   LD           DE,$5DC9
5E0C: CD 3B 3C   CALL       $3C3B
5E0F: CD BA 3D   CALL       $3DBA
5E12: 18 06      JR           $5E1A
5E14: 11 C9 5D   LD           DE,$5DC9
5E17: CD 3B 3C   CALL       $3C3B
5E1A: CD 1F 7F   CALL       $7F1F
5E1D: CD 4A 6D   CALL       $6D4A
5E20: F0 F0      LD           A,($F0)
5E22: C7         RST         0X00
5E23: 29         ADD         HL,HL
5E24: 5E         LD           E,(HL)
5E25: 6E         LD           L,(HL)
5E26: 5E         LD           E,(HL)
5E27: AF         XOR         A
5E28: 5E         LD           E,(HL)
5E29: CD B4 3B   CALL       $3BB4
5E2C: F0 E7      LD           A,($E7)
5E2E: 1F         RRA
5E2F: 1F         RRA
5E30: 1F         RRA
5E31: 1F         RRA
5E32: E6 01      AND         $01
5E34: CD 87 3B   CALL       $3B87
5E37: CD 91 08   CALL       $0891
5E3A: FE 18      CP           $18
5E3C: 20 04      JR           NZ,$5E42
5E3E: CD C0 5E   CALL       $5EC0
5E41: A7         AND         A
5E42: 30 26      JR           NC,$5E6A
5E44: CD FF 6D   CALL       $6DFF
5E47: C6 20      ADD         $20
5E49: FE 40      CP           $40
5E4B: 30 1D      JR           NC,$5E6A
5E4D: CD 0F 6E   CALL       $6E0F
5E50: C6 20      ADD         $20
5E52: FE 40      CP           $40
5E54: 30 14      JR           NC,$5E6A
5E56: 21 20 C4   LD           HL,$C420
5E59: 09         ADD         HL,BC
5E5A: 7E         LD           A,(HL)
5E5B: A7         AND         A
5E5C: 20 0C      JR           NZ,$5E6A
5E5E: CD 91 08   CALL       $0891
5E61: 36 20      LD           (HL),$20
5E63: CD 8D 3B   CALL       $3B8D
5E66: 3E 3C      LD           A,$3C
5E68: E0 F2      LDFF00   ($F2),A
5E6A: C9         RET
5E6B: 04         INC         B
5E6C: 03         INC         BC
5E6D: 02         LD           (BC),A
5E6E: CD 91 08   CALL       $0891
5E71: FE 18      CP           $18
5E73: D2 B4 3B   JP           NC,$3BB4
5E76: A7         AND         A
5E77: 20 23      JR           NZ,$5E9C
5E79: 36 40      LD           (HL),$40
5E7B: CD 8D 3B   CALL       $3B8D
5E7E: 3E FF      LD           A,$FF
5E80: CD 87 3B   CALL       $3B87
5E83: 21 10 C2   LD           HL,$C210
5E86: 09         ADD         HL,BC
5E87: 7E         LD           A,(HL)
5E88: D6 48      SUB         $48
5E8A: 5F         LD           E,A
5E8B: 3E 48      LD           A,$48
5E8D: 93         SUB         E
5E8E: 77         LD           (HL),A
5E8F: 21 00 C2   LD           HL,$C200
5E92: 09         ADD         HL,BC
5E93: 7E         LD           A,(HL)
5E94: D6 50      SUB         $50
5E96: 5F         LD           E,A
5E97: 3E 50      LD           A,$50
5E99: 93         SUB         E
5E9A: 77         LD           (HL),A
5E9B: C9         RET
5E9C: 1F         RRA
5E9D: 1F         RRA
5E9E: 1F         RRA
5E9F: E6 03      AND         $03
5EA1: 5F         LD           E,A
5EA2: 50         LD           D,B
5EA3: 21 6B 5E   LD           HL,$5E6B
5EA6: 19         ADD         HL,DE
5EA7: 7E         LD           A,(HL)
5EA8: CD 87 3B   CALL       $3B87
5EAB: C9         RET
5EAC: 02         LD           (BC),A
5EAD: 03         INC         BC
5EAE: 04         INC         B
5EAF: CD 91 08   CALL       $0891
5EB2: FE 18      CP           $18
5EB4: 30 38      JR           NC,$5EEE
5EB6: A7         AND         A
5EB7: 20 26      JR           NZ,$5EDF
5EB9: 36 30      LD           (HL),$30
5EBB: CD 8D 3B   CALL       $3B8D
5EBE: 70         LD           (HL),B
5EBF: C9         RET
5EC0: 3E 58      LD           A,$58
5EC2: CD 01 3C   CALL       $3C01
5EC5: 38 17      JR           C,$5EDE
5EC7: 21 00 C2   LD           HL,$C200
5ECA: 19         ADD         HL,DE
5ECB: F0 D7      LD           A,($D7)
5ECD: 77         LD           (HL),A
5ECE: 21 10 C2   LD           HL,$C210
5ED1: 19         ADD         HL,DE
5ED2: F0 D8      LD           A,($D8)
5ED4: 77         LD           (HL),A
5ED5: C5         PUSH       BC
5ED6: D5         PUSH       DE
5ED7: C1         POP         BC
5ED8: 3E 18      LD           A,$18
5EDA: CD 25 3C   CALL       $3C25
5EDD: C1         POP         BC
5EDE: C9         RET
5EDF: 1F         RRA
5EE0: 1F         RRA
5EE1: 1F         RRA
5EE2: E6 03      AND         $03
5EE4: 5F         LD           E,A
5EE5: 50         LD           D,B
5EE6: 21 AC 5E   LD           HL,$5EAC
5EE9: 19         ADD         HL,DE
5EEA: 7E         LD           A,(HL)
5EEB: CD 87 3B   CALL       $3B87
5EEE: C9         RET
5EEF: 7C         LD           A,H
5EF0: 00         NOP
5EF1: 7C         LD           A,H
5EF2: 20 7E      JR           NZ,$5F72
5EF4: 00         NOP
5EF5: 7E         LD           A,(HL)
5EF6: 20 11      JR           NZ,$5F09
5EF8: EF         RST         0X28
5EF9: 5E         LD           E,(HL)
5EFA: CD 3B 3C   CALL       $3C3B
5EFD: CD 1F 7F   CALL       $7F1F
5F00: F0 E7      LD           A,($E7)
5F02: 1F         RRA
5F03: 1F         RRA
5F04: 1F         RRA
5F05: E6 01      AND         $01
5F07: CD 87 3B   CALL       $3B87
5F0A: CD 94 6D   CALL       $6D94
5F0D: CD A9 3B   CALL       $3BA9
5F10: CD CA 3B   CALL       $3BCA
5F13: CD EB 3B   CALL       $3BEB
5F16: 21 A0 C2   LD           HL,$C2A0
5F19: 09         ADD         HL,BC
5F1A: 7E         LD           A,(HL)
5F1B: A7         AND         A
5F1C: 28 06      JR           Z,$5F24
5F1E: CD 44 6D   CALL       $6D44
5F21: CD E9 6B   CALL       $6BE9
5F24: C9         RET
5F25: 00         NOP
5F26: F0 78      LD           A,($78)
5F28: 00         NOP
5F29: 00         NOP
5F2A: F8 7A      LDHL       SP,$7A
5F2C: 00         NOP
5F2D: 00         NOP
5F2E: 00         NOP
5F2F: 70         LD           (HL),B
5F30: 00         NOP
5F31: 00         NOP
5F32: 08 72 00   LD           ($0072),SP
5F35: 00         NOP
5F36: F0 7C      LD           A,($7C)
5F38: 00         NOP
5F39: 00         NOP
5F3A: F8 7E      LDHL       SP,$7E
5F3C: 00         NOP
5F3D: 00         NOP
5F3E: 00         NOP
5F3F: 70         LD           (HL),B
5F40: 00         NOP
5F41: 00         NOP
5F42: 08 72 00   LD           ($0072),SP
5F45: 00         NOP
5F46: F0 78      LD           A,($78)
5F48: 00         NOP
5F49: 00         NOP
5F4A: F8 7A      LDHL       SP,$7A
5F4C: 00         NOP
5F4D: 00         NOP
5F4E: 00         NOP
5F4F: 74         LD           (HL),H
5F50: 00         NOP
5F51: 00         NOP
5F52: 08 76 00   LD           ($0076),SP
5F55: 9A         SBC         D
5F56: 10 9C      STOP       $9C
5F58: 10 21      STOP       $21
5F5A: 40         LD           B,B
5F5B: C4 09 7E   CALL       NZ,$7E09
5F5E: A7         AND         A
5F5F: 28 32      JR           Z,$5F93
5F61: F0 EC      LD           A,($EC)
5F63: C6 04      ADD         $04
5F65: E0 EC      LDFF00   ($EC),A
5F67: 11 55 5F   LD           DE,$5F55
5F6A: CD 3B 3C   CALL       $3C3B
5F6D: CD 94 6D   CALL       $6D94
5F70: CD CD 6D   CALL       $6DCD
5F73: 21 20 C3   LD           HL,$C320
5F76: 09         ADD         HL,BC
5F77: 35         DEC         (HL)
5F78: 21 10 C3   LD           HL,$C310
5F7B: 09         ADD         HL,BC
5F7C: 7E         LD           A,(HL)
5F7D: E6 80      AND         $80
5F7F: 28 0D      JR           Z,$5F8E
5F81: CD 44 6D   CALL       $6D44
5F84: AF         XOR         A
5F85: EA 7F DB   LD           ($DB7F),A
5F88: EA 67 C1   LD           ($C167),A
5F8B: C3 98 08   JP           $0898
5F8E: 3E 02      LD           A,$02
5F90: E0 A1      LDFF00   ($A1),A
5F92: C9         RET
5F93: F0 F9      LD           A,($F9)
5F95: A7         AND         A
5F96: C2 7B 60   JP           NZ,$607B
5F99: 21 40 C3   LD           HL,$C340
5F9C: 09         ADD         HL,BC
5F9D: 36 84      LD           (HL),$84
5F9F: 21 90 C3   LD           HL,$C390
5FA2: 09         ADD         HL,BC
5FA3: 7E         LD           A,(HL)
5FA4: E0 E8      LDFF00   ($E8),A
5FA6: FA 9F C1   LD           A,($C19F)
5FA9: A7         AND         A
5FAA: 21 45 5F   LD           HL,$5F45
5FAD: 20 10      JR           NZ,$5FBF
5FAF: 21 D0 C3   LD           HL,$C3D0
5FB2: 09         ADD         HL,BC
5FB3: 7E         LD           A,(HL)
5FB4: 34         INC         (HL)
5FB5: 21 25 5F   LD           HL,$5F25
5FB8: E6 30      AND         $30
5FBA: 28 03      JR           Z,$5FBF
5FBC: 21 35 5F   LD           HL,$5F35
5FBF: 0E 04      LD           C,$04
5FC1: CD 26 3D   CALL       $3D26
5FC4: 3E 04      LD           A,$04
5FC6: CD D0 3D   CALL       $3DD0
5FC9: CD 54 7B   CALL       $7B54
5FCC: F0 F0      LD           A,($F0)
5FCE: C7         RST         0X00
5FCF: D5         PUSH       DE
5FD0: 5F         LD           E,A
5FD1: E3                              
5FD2: 5F         LD           E,A
5FD3: 16 60      LD           D,$60
5FD5: CD BC 7B   CALL       $7BBC
5FD8: 30 08      JR           NC,$5FE2
5FDA: 3E 45      LD           A,$45
5FDC: CD 97 21   CALL       $2197
5FDF: CD 8D 3B   CALL       $3B8D
5FE2: C9         RET
5FE3: FA 9F C1   LD           A,($C19F)
5FE6: A7         AND         A
5FE7: 20 25      JR           NZ,$600E
5FE9: CD 8D 3B   CALL       $3B8D
5FEC: FA 77 C1   LD           A,($C177)
5FEF: A7         AND         A
5FF0: 28 06      JR           Z,$5FF8
5FF2: 70         LD           (HL),B
5FF3: 3E 46      LD           A,$46
5FF5: C3 97 21   JP           $2197
5FF8: FA 5E DB   LD           A,($DB5E)
5FFB: D6 10      SUB         $10
5FFD: FA 5D DB   LD           A,($DB5D)
6000: DE 00      SBC         $00
6002: 38 0B      JR           C,$600F
6004: 3E 0A      LD           A,$0A
6006: EA 92 DB   LD           ($DB92),A
6009: 3E 47      LD           A,$47
600B: CD 97 21   CALL       $2197
600E: C9         RET
600F: 70         LD           (HL),B
6010: 3E 4E      LD           A,$4E
6012: CD 97 21   CALL       $2197
6015: C9         RET
6016: FA 9F C1   LD           A,($C19F)
6019: A7         AND         A
601A: 20 06      JR           NZ,$6022
601C: CD AD 3E   CALL       $3EAD
601F: CD C1 67   CALL       $67C1
6022: C9         RET
6023: 58         LD           E,B
6024: 00         NOP
6025: 5A         LD           E,D
6026: 00         NOP
6027: 56         LD           D,(HL)
6028: 20 FF      JR           NZ,$6029
602A: 00         NOP
602B: 5C         LD           E,H
602C: 00         NOP
602D: 5E         LD           E,(HL)
602E: 00         NOP
602F: 58         LD           E,B
6030: 00         NOP
6031: 5A         LD           E,D
6032: 00         NOP
6033: 58         LD           E,B
6034: 00         NOP
6035: 5A         LD           E,D
6036: 00         NOP
6037: 5C         LD           E,H
6038: 00         NOP
6039: 5E         LD           E,(HL)
603A: 00         NOP
603B: 5C         LD           E,H
603C: 00         NOP
603D: 5E         LD           E,(HL)
603E: 00         NOP
603F: 56         LD           D,(HL)
6040: 00         NOP
6041: FF         RST         0X38
6042: 00         NOP
6043: 5E         LD           E,(HL)
6044: 20 5C      JR           NZ,$60A2
6046: 20 58      JR           NZ,$60A0
6048: 00         NOP
6049: 5A         LD           E,D
604A: 00         NOP
604B: 06 16      LD           B,$16
604D: 10 10      STOP       $10
604F: 38 38      JR           C,$6089
6051: 39         ADD         HL,SP
6052: 39         ADD         HL,SP
6053: 16 38      LD           D,$38
6055: F6 00      OR           $00
6057: F1         POP         AF
6058: F0 F0      LD           A,($F0)
605A: F0 F0      LD           A,($F0)
605C: FE 04      CP           $04
605E: F2                              
605F: 00         NOP
6060: F0 FA      LD           A,($FA)
6062: 00         NOP
6063: 00         NOP
6064: F8 F8      LDHL       SP,$F8
6066: F8 F2      LDHL       SP,$F2
6068: FE E8      CP           $E8
606A: 00         NOP
606B: E0 E8      LDFF00   ($E8),A
606D: 00         NOP
606E: 00         NOP
606F: 00         NOP
6070: 00         NOP
6071: 14         INC         D
6072: 10 E0      STOP       $E0
6074: F8 10      LDHL       SP,$10
6076: 00         NOP
6077: 00         NOP
6078: 00         NOP
6079: 00         NOP
607A: F0 21      LD           A,($21)
607C: B0         OR           B
607D: C2 09 7E   JP           NZ,$7E09
6080: C7         RST         0X00
6081: A2         AND         D
6082: 60         LD           H,B
6083: 41         LD           B,C
6084: 62         LD           H,D
6085: FC                              
6086: 63         LD           H,E
6087: E7         RST         0X20
6088: 66         LD           H,(HL)
6089: 18 58      JR           $60E3
608B: 60         LD           H,B
608C: 18 88      JR           $6016
608E: 40         LD           B,B
608F: 4C         LD           C,H
6090: 34         INC         (HL)
6091: 68         LD           L,B
6092: 50         LD           D,B
6093: 01 00 00   LD           BC,$0000
6096: 01 00 02   LD           BC,$0200
6099: 02         LD           (BC),A
609A: 02         LD           (BC),A
609B: 03         INC         BC
609C: 03         INC         BC
609D: 00         NOP
609E: 3E 1E      LD           A,$1E
60A0: 10 30      STOP       $30
60A2: 3E 02      LD           A,$02
60A4: E0 A1      LDFF00   ($A1),A
60A6: 21 C0 C2   LD           HL,$C2C0
60A9: 09         ADD         HL,BC
60AA: 7E         LD           A,(HL)
60AB: A7         AND         A
60AC: 20 44      JR           NZ,$60F2
60AE: 34         INC         (HL)
60AF: C5         PUSH       BC
60B0: 0E 05      LD           C,$05
60B2: 3E 54      LD           A,$54
60B4: CD 01 3C   CALL       $3C01
60B7: 21 88 60   LD           HL,$6088
60BA: 09         ADD         HL,BC
60BB: 7E         LD           A,(HL)
60BC: 21 00 C2   LD           HL,$C200
60BF: 19         ADD         HL,DE
60C0: 77         LD           (HL),A
60C1: 21 8D 60   LD           HL,$608D
60C4: 09         ADD         HL,BC
60C5: 7E         LD           A,(HL)
60C6: 21 10 C2   LD           HL,$C210
60C9: 19         ADD         HL,DE
60CA: 77         LD           (HL),A
60CB: 21 92 60   LD           HL,$6092
60CE: 09         ADD         HL,BC
60CF: 7E         LD           A,(HL)
60D0: 21 80 C3   LD           HL,$C380
60D3: 19         ADD         HL,DE
60D4: 77         LD           (HL),A
60D5: 21 97 60   LD           HL,$6097
60D8: 09         ADD         HL,BC
60D9: 7E         LD           A,(HL)
60DA: 21 B0 C2   LD           HL,$C2B0
60DD: 19         ADD         HL,DE
60DE: 77         LD           (HL),A
60DF: 21 9C 60   LD           HL,$609C
60E2: 09         ADD         HL,BC
60E3: 7E         LD           A,(HL)
60E4: 21 E0 C2   LD           HL,$C2E0
60E7: 19         ADD         HL,DE
60E8: 77         LD           (HL),A
60E9: 0D         DEC         C
60EA: 20 C6      JR           NZ,$60B2
60EC: AF         XOR         A
60ED: EA 04 D0   LD           ($D004),A
60F0: C1         POP         BC
60F1: C9         RET
60F2: F0 F1      LD           A,($F1)
60F4: 5F         LD           E,A
60F5: 50         LD           D,B
60F6: 21 4B 60   LD           HL,$604B
60F9: 19         ADD         HL,DE
60FA: 7E         LD           A,(HL)
60FB: E0 9D      LDFF00   ($9D),A
60FD: 21 55 60   LD           HL,$6055
6100: 19         ADD         HL,DE
6101: F0 98      LD           A,($98)
6103: 86         ADD         A,(HL)
6104: E0 EE      LDFF00   ($EE),A
6106: 21 5F 60   LD           HL,$605F
6109: 19         ADD         HL,DE
610A: F0 99      LD           A,($99)
610C: 86         ADD         A,(HL)
610D: E0 EC      LDFF00   ($EC),A
610F: 11 23 60   LD           DE,$6023
6112: CD 3B 3C   CALL       $3C3B
6115: F0 F0      LD           A,($F0)
6117: C7         RST         0X00
6118: 26 61      LD           H,$61
611A: 4E         LD           C,(HL)
611B: 61         LD           H,C
611C: B7         OR           A
611D: 61         LD           H,C
611E: B8         CP           B
611F: 61         LD           H,C
6120: 02         LD           (BC),A
6121: 62         LD           H,D
6122: 0F         RRCA
6123: 62         LD           H,D
6124: 2C         INC         L
6125: 62         LD           H,D
6126: FA 9F C1   LD           A,($C19F)
6129: A7         AND         A
612A: 20 12      JR           NZ,$613E
612C: F0 CC      LD           A,($CC)
612E: E6 30      AND         $30
6130: 28 0C      JR           Z,$613E
6132: CD 8D 3B   CALL       $3B8D
6135: CD 91 08   CALL       $0891
6138: 36 23      LD           (HL),$23
613A: AF         XOR         A
613B: EA 02 D0   LD           ($D002),A
613E: 3E 09      LD           A,$09
6140: CD 8D 61   CALL       $618D
6143: C9         RET
6144: 01 08 08   LD           BC,$0808
6147: 08 08 08   LD           ($0808),SP
614A: 01 02 03   LD           BC,$0302
614D: 00         NOP
614E: CD 91 08   CALL       $0891
6151: 20 36      JR           NZ,$6189
6153: CD 8D 3B   CALL       $3B8D
6156: 3E 02      LD           A,$02
6158: EA B0 C3   LD           ($C3B0),A
615B: 3E 54      LD           A,$54
615D: CD 01 3C   CALL       $3C01
6160: 21 00 C2   LD           HL,$C200
6163: 19         ADD         HL,DE
6164: 36 78      LD           (HL),$78
6166: 21 10 C2   LD           HL,$C210
6169: 19         ADD         HL,DE
616A: 36 18      LD           (HL),$18
616C: 21 40 C2   LD           HL,$C240
616F: 19         ADD         HL,DE
6170: 36 E2      LD           (HL),$E2
6172: 21 50 C2   LD           HL,$C250
6175: 19         ADD         HL,DE
6176: 36 FA      LD           (HL),$FA
6178: 21 B0 C2   LD           HL,$C2B0
617B: 19         ADD         HL,DE
617C: 36 01      LD           (HL),$01
617E: 21 E0 C2   LD           HL,$C2E0
6181: 19         ADD         HL,DE
6182: 36 14      LD           (HL),$14
6184: 3E 08      LD           A,$08
6186: E0 F2      LDFF00   ($F2),A
6188: C9         RET
6189: 1F         RRA
618A: 1F         RRA
618B: E6 1F      AND         $1F
618D: 5F         LD           E,A
618E: 50         LD           D,B
618F: 21 44 61   LD           HL,$6144
6192: 19         ADD         HL,DE
6193: 7E         LD           A,(HL)
6194: EA B0 C3   LD           ($C3B0),A
6197: 5F         LD           E,A
6198: 50         LD           D,B
6199: 21 69 60   LD           HL,$6069
619C: 19         ADD         HL,DE
619D: F0 98      LD           A,($98)
619F: 86         ADD         A,(HL)
61A0: E0 EE      LDFF00   ($EE),A
61A2: 21 72 60   LD           HL,$6072
61A5: 19         ADD         HL,DE
61A6: F0 99      LD           A,($99)
61A8: 86         ADD         A,(HL)
61A9: E0 EC      LDFF00   ($EC),A
61AB: AF         XOR         A
61AC: E0 F1      LDFF00   ($F1),A
61AE: 11 2D 62   LD           DE,$622D
61B1: CD 3B 3C   CALL       $3C3B
61B4: C3 BA 3D   JP           $3DBA
61B7: C9         RET
61B8: FA 9F C1   LD           A,($C19F)
61BB: A7         AND         A
61BC: 20 3B      JR           NZ,$61F9
61BE: FA 77 C1   LD           A,($C177)
61C1: A7         AND         A
61C2: 20 2D      JR           NZ,$61F1
61C4: FA 04 D0   LD           A,($D004)
61C7: FE 05      CP           $05
61C9: 38 0B      JR           C,$61D6
61CB: 3E 4B      LD           A,$4B
61CD: CD 97 21   CALL       $2197
61D0: CD 8D 3B   CALL       $3B8D
61D3: 36 05      LD           (HL),$05
61D5: C9         RET
61D6: FA 5E DB   LD           A,($DB5E)
61D9: D6 10      SUB         $10
61DB: FA 5D DB   LD           A,($DB5D)
61DE: DE 00      SBC         $00
61E0: 38 18      JR           C,$61FA
61E2: 3E 0A      LD           A,$0A
61E4: EA 92 DB   LD           ($DB92),A
61E7: 3E 47      LD           A,$47
61E9: CD 97 21   CALL       $2197
61EC: CD 8D 3B   CALL       $3B8D
61EF: 70         LD           (HL),B
61F0: C9         RET
61F1: 3E 46      LD           A,$46
61F3: CD 97 21   CALL       $2197
61F6: CD 8D 3B   CALL       $3B8D
61F9: C9         RET
61FA: 3E 4E      LD           A,$4E
61FC: CD 97 21   CALL       $2197
61FF: C3 8D 3B   JP           $3B8D
6202: FA 9F C1   LD           A,($C19F)
6205: A7         AND         A
6206: 20 06      JR           NZ,$620E
6208: CD AD 3E   CALL       $3EAD
620B: CD C1 67   CALL       $67C1
620E: C9         RET
620F: FA 9F C1   LD           A,($C19F)
6212: A7         AND         A
6213: 20 16      JR           NZ,$622B
6215: CD 8D 3B   CALL       $3B8D
6218: 36 04      LD           (HL),$04
621A: FA 77 C1   LD           A,($C177)
621D: A7         AND         A
621E: 20 06      JR           NZ,$6226
6220: 3E 4C      LD           A,$4C
6222: CD 97 21   CALL       $2197
6225: C9         RET
6226: 3E 46      LD           A,$46
6228: CD 97 21   CALL       $2197
622B: C9         RET
622C: C9         RET
622D: 50         LD           D,B
622E: 00         NOP
622F: 54         LD           D,H
6230: 00         NOP
6231: 50         LD           D,B
6232: 00         NOP
6233: 52         LD           D,D
6234: 00         NOP
6235: 50         LD           D,B
6236: 40         LD           B,B
6237: 54         LD           D,H
6238: 00         NOP
6239: 54         LD           D,H
623A: 40         LD           B,B
623B: 50         LD           D,B
623C: 40         LD           B,B
623D: 54         LD           D,H
623E: 60         LD           H,B
623F: 50         LD           D,B
6240: 60         LD           H,B
6241: 79         LD           A,C
6242: EA 03 D0   LD           ($D003),A
6245: 11 2D 62   LD           DE,$622D
6248: CD 3B 3C   CALL       $3C3B
624B: F0 EE      LD           A,($EE)
624D: EA 00 D0   LD           ($D000),A
6250: F0 EF      LD           A,($EF)
6252: EA 01 D0   LD           ($D001),A
6255: CD 1F 7F   CALL       $7F1F
6258: F0 F0      LD           A,($F0)
625A: C7         RST         0X00
625B: 5F         LD           E,A
625C: 62         LD           H,D
625D: C8         RET         Z
625E: 62         LD           H,D
625F: CD A1 6D   CALL       $6DA1
6262: CD 97 6D   CALL       $6D97
6265: F0 CB      LD           A,($CB)
6267: E6 01      AND         $01
6269: 28 11      JR           Z,$627C
626B: F0 E7      LD           A,($E7)
626D: E6 01      AND         $01
626F: 20 0B      JR           NZ,$627C
6271: 21 40 C2   LD           HL,$C240
6274: 09         ADD         HL,BC
6275: 7E         LD           A,(HL)
6276: A7         AND         A
6277: 28 03      JR           Z,$627C
6279: 34         INC         (HL)
627A: 18 05      JR           $6281
627C: CD 91 08   CALL       $0891
627F: 20 26      JR           NZ,$62A7
6281: F0 E7      LD           A,($E7)
6283: E6 01      AND         $01
6285: 20 0A      JR           NZ,$6291
6287: 21 50 C2   LD           HL,$C250
628A: 09         ADD         HL,BC
628B: 7E         LD           A,(HL)
628C: FE 20      CP           $20
628E: 28 01      JR           Z,$6291
6290: 34         INC         (HL)
6291: 21 D0 C3   LD           HL,$C3D0
6294: 09         ADD         HL,BC
6295: 7E         LD           A,(HL)
6296: 3C         INC         A
6297: FE 03      CP           $03
6299: 77         LD           (HL),A
629A: 20 0B      JR           NZ,$62A7
629C: AF         XOR         A
629D: 77         LD           (HL),A
629E: 21 40 C2   LD           HL,$C240
62A1: 09         ADD         HL,BC
62A2: 7E         LD           A,(HL)
62A3: A7         AND         A
62A4: 28 01      JR           Z,$62A7
62A6: 34         INC         (HL)
62A7: 21 10 C2   LD           HL,$C210
62AA: 09         ADD         HL,BC
62AB: 7E         LD           A,(HL)
62AC: FE 2A      CP           $2A
62AE: 38 17      JR           C,$62C7
62B0: CD AF 3D   CALL       $3DAF
62B3: CD 8D 3B   CALL       $3B8D
62B6: F0 EC      LD           A,($EC)
62B8: E0 D8      LDFF00   ($D8),A
62BA: F0 EE      LD           A,($EE)
62BC: E0 D7      LDFF00   ($D7),A
62BE: 3E 01      LD           A,$01
62C0: CD 53 09   CALL       $0953
62C3: 3E 0E      LD           A,$0E
62C5: E0 F2      LDFF00   ($F2),A
62C7: C9         RET
62C8: 21 B0 C3   LD           HL,$C3B0
62CB: 36 00      LD           (HL),$00
62CD: CD 91 08   CALL       $0891
62D0: 28 05      JR           Z,$62D7
62D2: 21 B0 C3   LD           HL,$C3B0
62D5: 36 04      LD           (HL),$04
62D7: CD 8C 08   CALL       $088C
62DA: 28 05      JR           Z,$62E1
62DC: 21 B0 C3   LD           HL,$C3B0
62DF: 36 05      LD           (HL),$05
62E1: F0 E7      LD           A,($E7)
62E3: 1F         RRA
62E4: 1F         RRA
62E5: 1F         RRA
62E6: 1F         RRA
62E7: E6 01      AND         $01
62E9: CD 87 3B   CALL       $3B87
62EC: CD 94 6D   CALL       $6D94
62EF: F0 E7      LD           A,($E7)
62F1: E6 07      AND         $07
62F3: 20 1F      JR           NZ,$6314
62F5: 21 50 C2   LD           HL,$C250
62F8: 09         ADD         HL,BC
62F9: 7E         LD           A,(HL)
62FA: D6 04      SUB         $04
62FC: 28 07      JR           Z,$6305
62FE: E6 80      AND         $80
6300: 28 02      JR           Z,$6304
6302: 34         INC         (HL)
6303: 34         INC         (HL)
6304: 35         DEC         (HL)
6305: 21 40 C2   LD           HL,$C240
6308: 09         ADD         HL,BC
6309: 7E         LD           A,(HL)
630A: A7         AND         A
630B: 28 07      JR           Z,$6314
630D: E6 80      AND         $80
630F: 28 02      JR           Z,$6313
6311: 34         INC         (HL)
6312: 34         INC         (HL)
6313: 35         DEC         (HL)
6314: F0 CC      LD           A,($CC)
6316: E6 30      AND         $30
6318: 28 5F      JR           Z,$6379
631A: CD 91 08   CALL       $0891
631D: 36 08      LD           (HL),$08
631F: F0 98      LD           A,($98)
6321: F5         PUSH       AF
6322: D6 17      SUB         $17
6324: E0 98      LDFF00   ($98),A
6326: 3E 04      LD           A,$04
6328: CD 25 3C   CALL       $3C25
632B: F1         POP         AF
632C: E0 98      LDFF00   ($98),A
632E: F0 EC      LD           A,($EC)
6330: FE 25      CP           $25
6332: 30 39      JR           NC,$636D
6334: F0 EE      LD           A,($EE)
6336: FE 70      CP           $70
6338: 38 33      JR           C,$636D
633A: 21 90 C2   LD           HL,$C290
633D: 36 03      LD           (HL),$03
633F: 3E 48      LD           A,$48
6341: CD 97 21   CALL       $2197
6344: CD 44 6D   CALL       $6D44
6347: 1E 0F      LD           E,$0F
6349: 50         LD           D,B
634A: 21 80 C2   LD           HL,$C280
634D: 19         ADD         HL,DE
634E: 7E         LD           A,(HL)
634F: A7         AND         A
6350: 28 15      JR           Z,$6367
6352: 21 B0 C2   LD           HL,$C2B0
6355: 19         ADD         HL,DE
6356: 7E         LD           A,(HL)
6357: FE 02      CP           $02
6359: 38 0C      JR           C,$6367
635B: 21 90 C2   LD           HL,$C290
635E: 19         ADD         HL,DE
635F: 7E         LD           A,(HL)
6360: FE 02      CP           $02
6362: 38 03      JR           C,$6367
6364: E6 01      AND         $01
6366: 77         LD           (HL),A
6367: 1D         DEC         E
6368: 7B         LD           A,E
6369: FE FF      CP           $FF
636B: 20 DD      JR           NZ,$634A
636D: F0 E7      LD           A,($E7)
636F: 1F         RRA
6370: 1F         RRA
6371: 1F         RRA
6372: E6 01      AND         $01
6374: CD 87 3B   CALL       $3B87
6377: 18 25      JR           $639E
6379: F0 CC      LD           A,($CC)
637B: E6 05      AND         $05
637D: 28 1F      JR           Z,$639E
637F: F0 EC      LD           A,($EC)
6381: FE 30      CP           $30
6383: 38 19      JR           C,$639E
6385: 21 00 C3   LD           HL,$C300
6388: 09         ADD         HL,BC
6389: 7E         LD           A,(HL)
638A: A7         AND         A
638B: 20 11      JR           NZ,$639E
638D: 21 50 C2   LD           HL,$C250
6390: 09         ADD         HL,BC
6391: 36 FA      LD           (HL),$FA
6393: 21 00 C3   LD           HL,$C300
6396: 09         ADD         HL,BC
6397: 36 50      LD           (HL),$50
6399: CD 8C 08   CALL       $088C
639C: 36 10      LD           (HL),$10
639E: F0 EE      LD           A,($EE)
63A0: 21 00 C2   LD           HL,$C200
63A3: 09         ADD         HL,BC
63A4: BE         CP           (HL)
63A5: 20 09      JR           NZ,$63B0
63A7: F0 EF      LD           A,($EF)
63A9: 21 10 C2   LD           HL,$C210
63AC: 09         ADD         HL,BC
63AD: BE         CP           (HL)
63AE: 28 12      JR           Z,$63C2
63B0: 21 50 C2   LD           HL,$C250
63B3: 09         ADD         HL,BC
63B4: 7E         LD           A,(HL)
63B5: F5         PUSH       AF
63B6: E5         PUSH       HL
63B7: E6 80      AND         $80
63B9: 28 01      JR           Z,$63BC
63BB: 70         LD           (HL),B
63BC: CD 9E 3B   CALL       $3B9E
63BF: E1         POP         HL
63C0: F1         POP         AF
63C1: 77         LD           (HL),A
63C2: 21 A0 C2   LD           HL,$C2A0
63C5: 09         ADD         HL,BC
63C6: 7E         LD           A,(HL)
63C7: A7         AND         A
63C8: 28 04      JR           Z,$63CE
63CA: AF         XOR         A
63CB: CD 87 3B   CALL       $3B87
63CE: 21 50 C2   LD           HL,$C250
63D1: 09         ADD         HL,BC
63D2: 7E         LD           A,(HL)
63D3: 17         RLA
63D4: 38 05      JR           C,$63DB
63D6: 3E 02      LD           A,$02
63D8: CD 87 3B   CALL       $3B87
63DB: C9         RET
63DC: 4C         LD           C,H
63DD: 00         NOP
63DE: 4A         LD           C,D
63DF: 00         NOP
63E0: 4C         LD           C,H
63E1: 00         NOP
63E2: 4E         LD           C,(HL)
63E3: 00         NOP
63E4: 48         LD           C,B
63E5: 00         NOP
63E6: 4A         LD           C,D
63E7: 00         NOP
63E8: 48         LD           C,B
63E9: 00         NOP
63EA: 4E         LD           C,(HL)
63EB: 00         NOP
63EC: 4A         LD           C,D
63ED: 20 4C      JR           NZ,$643B
63EF: 20 4E      JR           NZ,$643F
63F1: 20 4C      JR           NZ,$643F
63F3: 20 4A      JR           NZ,$643F
63F5: 20 48      JR           NZ,$643F
63F7: 20 4E      JR           NZ,$6447
63F9: 20 48      JR           NZ,$6443
63FB: 20 21      JR           NZ,$641E
63FD: 80         ADD         A,B
63FE: C3 09 7E   JP           $7E09
6401: A7         AND         A
6402: 20 06      JR           NZ,$640A
6404: F0 F1      LD           A,($F1)
6406: C6 04      ADD         $04
6408: E0 F1      LDFF00   ($F1),A
640A: 11 DC 63   LD           DE,$63DC
640D: CD 3B 3C   CALL       $3C3B
6410: CD 1F 7F   CALL       $7F1F
6413: CD 94 6D   CALL       $6D94
6416: F0 F0      LD           A,($F0)
6418: C7         RST         0X00
6419: 25         DEC         H
641A: 64         LD           H,H
641B: 5D         LD           E,L
641C: 64         LD           H,H
641D: B4         OR           H
641E: 64         LD           H,H
641F: EF         RST         0X28
6420: 64         LD           H,H
6421: 3C         INC         A
6422: 65         LD           H,L
6423: 4D         LD           C,L
6424: 66         LD           H,(HL)
6425: CD 61 67   CALL       $6761
6428: 21 B0 C2   LD           HL,$C2B0
642B: 09         ADD         HL,BC
642C: 7E         LD           A,(HL)
642D: FE 03      CP           $03
642F: CA FE 66   JP           Z,$66FE
6432: CD 91 08   CALL       $0891
6435: 20 0D      JR           NZ,$6444
6437: 36 30      LD           (HL),$30
6439: 21 80 C3   LD           HL,$C380
643C: 09         ADD         HL,BC
643D: 7E         LD           A,(HL)
643E: EE 01      XOR         $01
6440: 77         LD           (HL),A
6441: CD 8D 3B   CALL       $3B8D
6444: F0 E7      LD           A,($E7)
6446: E6 03      AND         $03
6448: 20 0F      JR           NZ,$6459
644A: 21 40 C2   LD           HL,$C240
644D: 09         ADD         HL,BC
644E: 7E         LD           A,(HL)
644F: A7         AND         A
6450: 28 07      JR           Z,$6459
6452: E6 80      AND         $80
6454: 28 02      JR           Z,$6458
6456: 34         INC         (HL)
6457: 34         INC         (HL)
6458: 35         DEC         (HL)
6459: 18 47      JR           $64A2
645B: 10 F0      STOP       $F0
645D: CD 61 67   CALL       $6761
6460: 21 B0 C2   LD           HL,$C2B0
6463: 09         ADD         HL,BC
6464: 7E         LD           A,(HL)
6465: FE 03      CP           $03
6467: CA 28 67   JP           Z,$6728
646A: CD 91 08   CALL       $0891
646D: 20 06      JR           NZ,$6475
646F: 36 50      LD           (HL),$50
6471: CD 8D 3B   CALL       $3B8D
6474: 70         LD           (HL),B
6475: F0 E7      LD           A,($E7)
6477: 1F         RRA
6478: 1F         RRA
6479: 1F         RRA
647A: E6 01      AND         $01
647C: CD 87 3B   CALL       $3B87
647F: F0 E7      LD           A,($E7)
6481: E6 03      AND         $03
6483: 20 1D      JR           NZ,$64A2
6485: 21 40 C2   LD           HL,$C240
6488: 09         ADD         HL,BC
6489: 7E         LD           A,(HL)
648A: E5         PUSH       HL
648B: 21 80 C3   LD           HL,$C380
648E: 09         ADD         HL,BC
648F: 5E         LD           E,(HL)
6490: 16 00      LD           D,$00
6492: 21 5B 64   LD           HL,$645B
6495: 19         ADD         HL,DE
6496: 96         SUB         (HL)
6497: E1         POP         HL
6498: A7         AND         A
6499: 28 07      JR           Z,$64A2
649B: E6 80      AND         $80
649D: 28 02      JR           Z,$64A1
649F: 34         INC         (HL)
64A0: 34         INC         (HL)
64A1: 35         DEC         (HL)
64A2: 21 10 C2   LD           HL,$C210
64A5: 09         ADD         HL,BC
64A6: 7E         LD           A,(HL)
64A7: FE 34      CP           $34
64A9: 30 06      JR           NC,$64B1
64AB: 34         INC         (HL)
64AC: 21 50 C2   LD           HL,$C250
64AF: 09         ADD         HL,BC
64B0: 70         LD           (HL),B
64B1: C9         RET
64B2: F2                              
64B3: 14         INC         D
64B4: F0 E7      LD           A,($E7)
64B6: 1F         RRA
64B7: 1F         RRA
64B8: 1F         RRA
64B9: E6 01      AND         $01
64BB: CD 87 3B   CALL       $3B87
64BE: CD 91 08   CALL       $0891
64C1: 20 03      JR           NZ,$64C6
64C3: CD 8D 3B   CALL       $3B8D
64C6: F0 98      LD           A,($98)
64C8: F5         PUSH       AF
64C9: F0 99      LD           A,($99)
64CB: F5         PUSH       AF
64CC: 21 80 C3   LD           HL,$C380
64CF: 09         ADD         HL,BC
64D0: 5E         LD           E,(HL)
64D1: 50         LD           D,B
64D2: 21 B2 64   LD           HL,$64B2
64D5: 19         ADD         HL,DE
64D6: FA 00 D0   LD           A,($D000)
64D9: 86         ADD         A,(HL)
64DA: E0 98      LDFF00   ($98),A
64DC: FA 01 D0   LD           A,($D001)
64DF: E0 99      LDFF00   ($99),A
64E1: 3E 04      LD           A,$04
64E3: CD 25 3C   CALL       $3C25
64E6: F1         POP         AF
64E7: E0 99      LDFF00   ($99),A
64E9: F1         POP         AF
64EA: E0 98      LDFF00   ($98),A
64EC: C3 94 6D   JP           $6D94
64EF: F0 E7      LD           A,($E7)
64F1: 1F         RRA
64F2: 1F         RRA
64F3: E6 01      AND         $01
64F5: C6 02      ADD         $02
64F7: CD 87 3B   CALL       $3B87
64FA: F0 98      LD           A,($98)
64FC: F5         PUSH       AF
64FD: F0 99      LD           A,($99)
64FF: F5         PUSH       AF
6500: FA 00 D0   LD           A,($D000)
6503: C6 04      ADD         $04
6505: E0 98      LDFF00   ($98),A
6507: FA 01 D0   LD           A,($D001)
650A: E0 99      LDFF00   ($99),A
650C: 3E 10      LD           A,$10
650E: CD 25 3C   CALL       $3C25
6511: F1         POP         AF
6512: E0 99      LDFF00   ($99),A
6514: F1         POP         AF
6515: E0 98      LDFF00   ($98),A
6517: CD 94 6D   CALL       $6D94
651A: FA 00 D0   LD           A,($D000)
651D: 21 EE FF   LD           HL,$FFEE
6520: 96         SUB         (HL)
6521: C6 08      ADD         $08
6523: FE 10      CP           $10
6525: 30 10      JR           NC,$6537
6527: CD AF 3D   CALL       $3DAF
652A: CD 8D 3B   CALL       $3B8D
652D: FA 03 D0   LD           A,($D003)
6530: 5F         LD           E,A
6531: 50         LD           D,B
6532: 21 80 C2   LD           HL,$C280
6535: 19         ADD         HL,DE
6536: 70         LD           (HL),B
6537: C9         RET
6538: 54         LD           D,H
6539: 00         NOP
653A: 08 F8 21   LD           ($21F8),SP
653D: 80         ADD         A,B
653E: C3 09 5E   JP           $5E09
6541: 50         LD           D,B
6542: 21 3A 65   LD           HL,$653A
6545: 19         ADD         HL,DE
6546: F0 EE      LD           A,($EE)
6548: 86         ADD         A,(HL)
6549: E0 EE      LDFF00   ($EE),A
654B: 21 F1 FF   LD           HL,$FFF1
654E: 70         LD           (HL),B
654F: 11 38 65   LD           DE,$6538
6552: CD D0 3C   CALL       $3CD0
6555: CD BA 3D   CALL       $3DBA
6558: F0 E7      LD           A,($E7)
655A: 1F         RRA
655B: 1F         RRA
655C: 1F         RRA
655D: E6 01      AND         $01
655F: CD 87 3B   CALL       $3B87
6562: F0 E7      LD           A,($E7)
6564: E6 07      AND         $07
6566: 20 35      JR           NZ,$659D
6568: F0 98      LD           A,($98)
656A: F5         PUSH       AF
656B: F0 99      LD           A,($99)
656D: F5         PUSH       AF
656E: 3E 00      LD           A,$00
6570: E0 98      LDFF00   ($98),A
6572: 3E 59      LD           A,$59
6574: E0 99      LDFF00   ($99),A
6576: 3E 08      LD           A,$08
6578: CD 30 3C   CALL       $3C30
657B: F0 D7      LD           A,($D7)
657D: 21 50 C2   LD           HL,$C250
6580: 09         ADD         HL,BC
6581: 96         SUB         (HL)
6582: 34         INC         (HL)
6583: E6 80      AND         $80
6585: 28 02      JR           Z,$6589
6587: 35         DEC         (HL)
6588: 35         DEC         (HL)
6589: F0 D8      LD           A,($D8)
658B: 21 40 C2   LD           HL,$C240
658E: 09         ADD         HL,BC
658F: 96         SUB         (HL)
6590: 34         INC         (HL)
6591: E6 80      AND         $80
6593: 28 02      JR           Z,$6597
6595: 35         DEC         (HL)
6596: 35         DEC         (HL)
6597: F1         POP         AF
6598: E0 99      LDFF00   ($99),A
659A: F1         POP         AF
659B: E0 98      LDFF00   ($98),A
659D: F0 CC      LD           A,($CC)
659F: E6 30      AND         $30
65A1: 28 50      JR           Z,$65F3
65A3: 21 B0 C2   LD           HL,$C2B0
65A6: 09         ADD         HL,BC
65A7: 7E         LD           A,(HL)
65A8: FE 03      CP           $03
65AA: 20 07      JR           NZ,$65B3
65AC: CD ED 27   CALL       $27ED
65AF: E6 03      AND         $03
65B1: 28 40      JR           Z,$65F3
65B3: F0 98      LD           A,($98)
65B5: F5         PUSH       AF
65B6: D6 14      SUB         $14
65B8: E0 98      LDFF00   ($98),A
65BA: F0 99      LD           A,($99)
65BC: F5         PUSH       AF
65BD: C6 08      ADD         $08
65BF: E0 99      LDFF00   ($99),A
65C1: 3E 03      LD           A,$03
65C3: CD 30 3C   CALL       $3C30
65C6: F0 D7      LD           A,($D7)
65C8: 21 50 C2   LD           HL,$C250
65CB: 09         ADD         HL,BC
65CC: 96         SUB         (HL)
65CD: 34         INC         (HL)
65CE: 34         INC         (HL)
65CF: E6 80      AND         $80
65D1: 28 04      JR           Z,$65D7
65D3: 35         DEC         (HL)
65D4: 35         DEC         (HL)
65D5: 35         DEC         (HL)
65D6: 35         DEC         (HL)
65D7: F0 D8      LD           A,($D8)
65D9: 21 40 C2   LD           HL,$C240
65DC: 09         ADD         HL,BC
65DD: 96         SUB         (HL)
65DE: 34         INC         (HL)
65DF: 34         INC         (HL)
65E0: E6 80      AND         $80
65E2: 28 04      JR           Z,$65E8
65E4: 35         DEC         (HL)
65E5: 35         DEC         (HL)
65E6: 35         DEC         (HL)
65E7: 35         DEC         (HL)
65E8: F1         POP         AF
65E9: E0 99      LDFF00   ($99),A
65EB: F1         POP         AF
65EC: E0 98      LDFF00   ($98),A
65EE: CD 91 08   CALL       $0891
65F1: 36 10      LD           (HL),$10
65F3: CD 94 6D   CALL       $6D94
65F6: 21 40 C2   LD           HL,$C240
65F9: 09         ADD         HL,BC
65FA: 7E         LD           A,(HL)
65FB: A7         AND         A
65FC: 28 08      JR           Z,$6606
65FE: 07         RLCA
65FF: E6 01      AND         $01
6601: 21 80 C3   LD           HL,$C380
6604: 09         ADD         HL,BC
6605: 77         LD           (HL),A
6606: 21 B0 C3   LD           HL,$C3B0
6609: 36 05      LD           (HL),$05
660B: CD 91 08   CALL       $0891
660E: 28 0B      JR           Z,$661B
6610: F0 E7      LD           A,($E7)
6612: E6 30      AND         $30
6614: 28 05      JR           Z,$661B
6616: 21 B0 C3   LD           HL,$C3B0
6619: 36 07      LD           (HL),$07
661B: F0 EC      LD           A,($EC)
661D: FE 2C      CP           $2C
661F: 30 18      JR           NC,$6639
6621: F0 EE      LD           A,($EE)
6623: FE 74      CP           $74
6625: 38 12      JR           C,$6639
6627: CD 8D 3B   CALL       $3B8D
662A: 21 40 C2   LD           HL,$C240
662D: 09         ADD         HL,BC
662E: 36 05      LD           (HL),$05
6630: 21 50 C2   LD           HL,$C250
6633: 09         ADD         HL,BC
6634: 36 F0      LD           (HL),$F0
6636: C3 B6 62   JP           $62B6
6639: F0 EE      LD           A,($EE)
663B: FE 03      CP           $03
663D: 30 0D      JR           NC,$664C
663F: 21 90 C2   LD           HL,$C290
6642: 36 03      LD           (HL),$03
6644: 3E 49      LD           A,$49
6646: CD 97 21   CALL       $2197
6649: C3 44 6D   JP           $6D44
664C: C9         RET
664D: 21 B0 C3   LD           HL,$C3B0
6650: 36 01      LD           (HL),$01
6652: CD 94 6D   CALL       $6D94
6655: 21 50 C2   LD           HL,$C250
6658: 09         ADD         HL,BC
6659: 34         INC         (HL)
665A: 00         NOP
665B: 7E         LD           A,(HL)
665C: FE 0C      CP           $0C
665E: 20 66      JR           NZ,$66C6
6660: 21 90 C2   LD           HL,$C290
6663: 36 03      LD           (HL),$03
6665: 79         LD           A,C
6666: FE 0F      CP           $0F
6668: 20 41      JR           NZ,$66AB
666A: F0 F8      LD           A,($F8)
666C: E6 10      AND         $10
666E: 20 3B      JR           NZ,$66AB
6670: 3E 01      LD           A,$01
6672: E0 F2      LDFF00   ($F2),A
6674: F0 F6      LD           A,($F6)
6676: 5F         LD           E,A
6677: 16 01      LD           D,$01
6679: 21 00 D9   LD           HL,$D900
667C: 19         ADD         HL,DE
667D: 7E         LD           A,(HL)
667E: F6 10      OR           $10
6680: 77         LD           (HL),A
6681: E0 F8      LDFF00   ($F8),A
6683: FA 5C DB   LD           A,($DB5C)
6686: 3C         INC         A
6687: EA 5C DB   LD           ($DB5C),A
668A: FE 04      CP           $04
668C: 20 11      JR           NZ,$669F
668E: AF         XOR         A
668F: EA 5C DB   LD           ($DB5C),A
6692: 21 93 DB   LD           HL,$DB93
6695: 36 40      LD           (HL),$40
6697: 21 5B DB   LD           HL,$DB5B
669A: 34         INC         (HL)
669B: 3E FF      LD           A,$FF
669D: 18 02      JR           $66A1
669F: 3E FE      LD           A,$FE
66A1: CD 85 21   CALL       $2185
66A4: 21 90 DB   LD           HL,$DB90
66A7: 36 20      LD           (HL),$20
66A9: 18 18      JR           $66C3
66AB: 21 B0 C2   LD           HL,$C2B0
66AE: 09         ADD         HL,BC
66AF: 7E         LD           A,(HL)
66B0: FE 03      CP           $03
66B2: 1E 14      LD           E,$14
66B4: 3E 4A      LD           A,$4A
66B6: 28 04      JR           Z,$66BC
66B8: 1E 05      LD           E,$05
66BA: 3E 4D      LD           A,$4D
66BC: 21 90 DB   LD           HL,$DB90
66BF: 73         LD           (HL),E
66C0: CD 97 21   CALL       $2197
66C3: CD 44 6D   CALL       $6D44
66C6: C9         RET
66C7: 44         LD           B,H
66C8: 00         NOP
66C9: 42         LD           B,D
66CA: 00         NOP
66CB: 44         LD           B,H
66CC: 00         NOP
66CD: 46         LD           B,(HL)
66CE: 00         NOP
66CF: 40         LD           B,B
66D0: 00         NOP
66D1: 42         LD           B,D
66D2: 00         NOP
66D3: 40         LD           B,B
66D4: 00         NOP
66D5: 46         LD           B,(HL)
66D6: 00         NOP
66D7: 42         LD           B,D
66D8: 20 44      JR           NZ,$671E
66DA: 20 46      JR           NZ,$6722
66DC: 20 44      JR           NZ,$6722
66DE: 20 42      JR           NZ,$6722
66E0: 20 40      JR           NZ,$6722
66E2: 20 46      JR           NZ,$672A
66E4: 20 40      JR           NZ,$6726
66E6: 20 21      JR           NZ,$6709
66E8: 80         ADD         A,B
66E9: C3 09 7E   JP           $7E09
66EC: A7         AND         A
66ED: 20 06      JR           NZ,$66F5
66EF: F0 F1      LD           A,($F1)
66F1: C6 04      ADD         $04
66F3: E0 F1      LDFF00   ($F1),A
66F5: 11 C7 66   LD           DE,$66C7
66F8: CD 3B 3C   CALL       $3C3B
66FB: C3 10 64   JP           $6410
66FE: CD 91 08   CALL       $0891
6701: 20 0D      JR           NZ,$6710
6703: 36 18      LD           (HL),$18
6705: 21 80 C3   LD           HL,$C380
6708: 09         ADD         HL,BC
6709: 7E         LD           A,(HL)
670A: EE 01      XOR         $01
670C: 77         LD           (HL),A
670D: CD 8D 3B   CALL       $3B8D
6710: F0 E7      LD           A,($E7)
6712: E6 03      AND         $03
6714: 20 0F      JR           NZ,$6725
6716: 21 40 C2   LD           HL,$C240
6719: 09         ADD         HL,BC
671A: 7E         LD           A,(HL)
671B: A7         AND         A
671C: 28 07      JR           Z,$6725
671E: E6 80      AND         $80
6720: 28 02      JR           Z,$6724
6722: 34         INC         (HL)
6723: 34         INC         (HL)
6724: 35         DEC         (HL)
6725: C9         RET
6726: 08 F8 CD   LD           ($CDF8),SP
6729: 91         SUB         C
672A: 08 20 06   LD           ($0620),SP
672D: 36 50      LD           (HL),$50
672F: CD 8D 3B   CALL       $3B8D
6732: 70         LD           (HL),B
6733: F0 E7      LD           A,($E7)
6735: 1F         RRA
6736: 1F         RRA
6737: 1F         RRA
6738: E6 01      AND         $01
673A: CD 87 3B   CALL       $3B87
673D: F0 E7      LD           A,($E7)
673F: E6 03      AND         $03
6741: 20 1D      JR           NZ,$6760
6743: 21 40 C2   LD           HL,$C240
6746: 09         ADD         HL,BC
6747: 7E         LD           A,(HL)
6748: E5         PUSH       HL
6749: 21 80 C3   LD           HL,$C380
674C: 09         ADD         HL,BC
674D: 5E         LD           E,(HL)
674E: 16 00      LD           D,$00
6750: 21 26 67   LD           HL,$6726
6753: 19         ADD         HL,DE
6754: 96         SUB         (HL)
6755: E1         POP         HL
6756: A7         AND         A
6757: 28 07      JR           Z,$6760
6759: E6 80      AND         $80
675B: 28 02      JR           Z,$675F
675D: 34         INC         (HL)
675E: 34         INC         (HL)
675F: 35         DEC         (HL)
6760: C9         RET
6761: FA 02 D0   LD           A,($D002)
6764: A7         AND         A
6765: 20 59      JR           NZ,$67C0
6767: FA 03 D0   LD           A,($D003)
676A: 5F         LD           E,A
676B: 50         LD           D,B
676C: 21 80 C2   LD           HL,$C280
676F: 19         ADD         HL,DE
6770: 7E         LD           A,(HL)
6771: A7         AND         A
6772: 28 4C      JR           Z,$67C0
6774: 21 90 C2   LD           HL,$C290
6777: 19         ADD         HL,DE
6778: 7E         LD           A,(HL)
6779: A7         AND         A
677A: 28 44      JR           Z,$67C0
677C: FA 00 D0   LD           A,($D000)
677F: 21 EE FF   LD           HL,$FFEE
6782: 96         SUB         (HL)
6783: 07         RLCA
6784: 07         RLCA
6785: E6 01      AND         $01
6787: 21 80 C3   LD           HL,$C380
678A: 09         ADD         HL,BC
678B: BE         CP           (HL)
678C: 20 32      JR           NZ,$67C0
678E: FA 00 D0   LD           A,($D000)
6791: 21 EE FF   LD           HL,$FFEE
6794: 96         SUB         (HL)
6795: C6 18      ADD         $18
6797: FE 30      CP           $30
6799: 30 25      JR           NC,$67C0
679B: FA 01 D0   LD           A,($D001)
679E: 21 EF FF   LD           HL,$FFEF
67A1: 96         SUB         (HL)
67A2: C6 10      ADD         $10
67A4: FE 20      CP           $20
67A6: 30 18      JR           NC,$67C0
67A8: CD 8D 3B   CALL       $3B8D
67AB: 36 02      LD           (HL),$02
67AD: 21 02 D0   LD           HL,$D002
67B0: 34         INC         (HL)
67B1: 21 04 D0   LD           HL,$D004
67B4: 34         INC         (HL)
67B5: CD 91 08   CALL       $0891
67B8: CD ED 27   CALL       $27ED
67BB: E6 3F      AND         $3F
67BD: C6 30      ADD         $30
67BF: 77         LD           (HL),A
67C0: C9         RET
67C1: CD 0F 09   CALL       $090F
67C4: F0 98      LD           A,($98)
67C6: CB 37      SWAP        1,E
67C8: E6 0F      AND         $0F
67CA: 5F         LD           E,A
67CB: F0 99      LD           A,($99)
67CD: D6 08      SUB         $08
67CF: E6 F0      AND         $F0
67D1: B3         OR           E
67D2: EA 16 D4   LD           ($D416),A
67D5: C9         RET
67D6: 4C         LD           C,H
67D7: 00         NOP
67D8: 4C         LD           C,H
67D9: 20 4E      JR           NZ,$6829
67DB: 00         NOP
67DC: 4E         LD           C,(HL)
67DD: 20 7C      JR           NZ,$685B
67DF: 00         NOP
67E0: 7C         LD           A,H
67E1: 20 7E      JR           NZ,$6861
67E3: 00         NOP
67E4: 7E         LD           A,(HL)
67E5: 20 21      JR           NZ,$6808
67E7: 5E         LD           E,(HL)
67E8: D4 34 11   CALL       NC,$1134
67EB: D6 67      SUB         $67
67ED: F0 F7      LD           A,($F7)
67EF: FE 01      CP           $01
67F1: 20 03      JR           NZ,$67F6
67F3: 11 DE 67   LD           DE,$67DE
67F6: CD 3B 3C   CALL       $3C3B
67F9: CD 1F 7F   CALL       $7F1F
67FC: CD EB 3B   CALL       $3BEB
67FF: F0 F0      LD           A,($F0)
6801: C7         RST         0X00
6802: 0A         LD           A,(BC)
6803: 68         LD           L,B
6804: C0         RET         NZ
6805: 68         LD           L,B
6806: 00         NOP
6807: 03         INC         BC
6808: 01 02 CD   LD           BC,$CD02
680B: 87         ADD         A,A
680C: 08 20 06   LD           ($0620),SP
680F: 36 10      LD           (HL),$10
6811: CD 8D 3B   CALL       $3B8D
6814: C9         RET
6815: FA 1C C1   LD           A,($C11C)
6818: FE 00      CP           $00
681A: C2 A7 68   JP           NZ,$68A7
681D: F0 9A      LD           A,($9A)
681F: F5         PUSH       AF
6820: F0 9B      LD           A,($9B)
6822: F5         PUSH       AF
6823: 1E 00      LD           E,$00
6825: F0 EB      LD           A,($EB)
6827: FE 52      CP           $52
6829: 3E 14      LD           A,$14
682B: 20 03      JR           NZ,$6830
682D: 1C         INC         E
682E: 3E 08      LD           A,$08
6830: D5         PUSH       DE
6831: CD 30 3C   CALL       $3C30
6834: D1         POP         DE
6835: F0 D7      LD           A,($D7)
6837: CB 43      BIT         1,E
6839: 28 02      JR           Z,$683D
683B: 2F         CPL
683C: 3C         INC         A
683D: E0 9B      LDFF00   ($9B),A
683F: F0 D8      LD           A,($D8)
6841: CB 43      BIT         1,E
6843: 28 02      JR           Z,$6847
6845: 2F         CPL
6846: 3C         INC         A
6847: E0 9A      LDFF00   ($9A),A
6849: C5         PUSH       BC
684A: CD D6 20   CALL       $20D6
684D: CD 49 3E   CALL       $3E49
6850: C1         POP         BC
6851: F1         POP         AF
6852: E0 9B      LDFF00   ($9B),A
6854: F1         POP         AF
6855: E0 9A      LDFF00   ($9A),A
6857: AF         XOR         A
6858: EA 44 C1   LD           ($C144),A
685B: F0 EB      LD           A,($EB)
685D: FE 52      CP           $52
685F: C2 A7 68   JP           NZ,$68A7
6862: FA 46 C1   LD           A,($C146)
6865: A7         AND         A
6866: 20 2F      JR           NZ,$6897
6868: CD FF 6D   CALL       $6DFF
686B: C6 04      ADD         $04
686D: FE 08      CP           $08
686F: 30 26      JR           NC,$6897
6871: CD 0F 6E   CALL       $6E0F
6874: C6 04      ADD         $04
6876: FE 08      CP           $08
6878: 30 1D      JR           NC,$6897
687A: F0 EE      LD           A,($EE)
687C: E0 98      LDFF00   ($98),A
687E: F0 EC      LD           A,($EC)
6880: E0 99      LDFF00   ($99),A
6882: 3E 06      LD           A,$06
6884: EA 1C C1   LD           ($C11C),A
6887: CD 3B 09   CALL       $093B
688A: EA 98 C1   LD           ($C198),A
688D: 3E FF      LD           A,$FF
688F: EA CB DB   LD           ($DBCB),A
6892: 3E 0C      LD           A,$0C
6894: E0 F3      LDFF00   ($F3),A
6896: C9         RET
6897: F0 E7      LD           A,($E7)
6899: 1F         RRA
689A: 1F         RRA
689B: 1F         RRA
689C: E6 03      AND         $03
689E: 5F         LD           E,A
689F: 50         LD           D,B
68A0: 21 06 68   LD           HL,$6806
68A3: 19         ADD         HL,DE
68A4: 7E         LD           A,(HL)
68A5: E0 9E      LDFF00   ($9E),A
68A7: CD D0 68   CALL       $68D0
68AA: F0 E7      LD           A,($E7)
68AC: 1F         RRA
68AD: 1F         RRA
68AE: 1F         RRA
68AF: 1F         RRA
68B0: E6 01      AND         $01
68B2: CD 87 3B   CALL       $3B87
68B5: F0 E7      LD           A,($E7)
68B7: E6 1F      AND         $1F
68B9: 20 04      JR           NZ,$68BF
68BB: 3E 1F      LD           A,$1F
68BD: E0 F4      LDFF00   ($F4),A
68BF: C9         RET
68C0: CD 87 08   CALL       $0887
68C3: 20 06      JR           NZ,$68CB
68C5: 36 40      LD           (HL),$40
68C7: CD 8D 3B   CALL       $3B8D
68CA: 70         LD           (HL),B
68CB: 3E 00      LD           A,$00
68CD: C3 87 3B   JP           $3B87
68D0: 1E 0F      LD           E,$0F
68D2: 50         LD           D,B
68D3: D5         PUSH       DE
68D4: 7B         LD           A,E
68D5: B9         CP           C
68D6: CA 68 69   JP           Z,$6968
68D9: 21 80 C2   LD           HL,$C280
68DC: 19         ADD         HL,DE
68DD: 7E         LD           A,(HL)
68DE: A7         AND         A
68DF: CA 68 69   JP           Z,$6968
68E2: CD BA 3D   CALL       $3DBA
68E5: C5         PUSH       BC
68E6: D5         PUSH       DE
68E7: C1         POP         BC
68E8: F0 E7      LD           A,($E7)
68EA: A9         XOR         C
68EB: E6 01      AND         $01
68ED: 20 78      JR           NZ,$6967
68EF: F0 98      LD           A,($98)
68F1: F5         PUSH       AF
68F2: F0 99      LD           A,($99)
68F4: F5         PUSH       AF
68F5: F0 EE      LD           A,($EE)
68F7: E0 98      LDFF00   ($98),A
68F9: F0 EF      LD           A,($EF)
68FB: E0 99      LDFF00   ($99),A
68FD: 21 40 C2   LD           HL,$C240
6900: 09         ADD         HL,BC
6901: 7E         LD           A,(HL)
6902: F5         PUSH       AF
6903: 21 50 C2   LD           HL,$C250
6906: 09         ADD         HL,BC
6907: 7E         LD           A,(HL)
6908: F5         PUSH       AF
6909: 3E 10      LD           A,$10
690B: CD 30 3C   CALL       $3C30
690E: 1E 00      LD           E,$00
6910: F0 EB      LD           A,($EB)
6912: FE 52      CP           $52
6914: 20 01      JR           NZ,$6917
6916: 1C         INC         E
6917: F0 D7      LD           A,($D7)
6919: CB 43      BIT         1,E
691B: 20 02      JR           NZ,$691F
691D: 2F         CPL
691E: 3C         INC         A
691F: 21 50 C2   LD           HL,$C250
6922: 09         ADD         HL,BC
6923: 77         LD           (HL),A
6924: F0 D8      LD           A,($D8)
6926: CB 43      BIT         1,E
6928: 20 02      JR           NZ,$692C
692A: 2F         CPL
692B: 3C         INC         A
692C: 21 40 C2   LD           HL,$C240
692F: 09         ADD         HL,BC
6930: 77         LD           (HL),A
6931: CD BA 3D   CALL       $3DBA
6934: CD 94 6D   CALL       $6D94
6937: CD 9E 3B   CALL       $3B9E
693A: F0 EE      LD           A,($EE)
693C: 21 98 FF   LD           HL,$FF98
693F: 96         SUB         (HL)
6940: C6 02      ADD         $02
6942: FE 04      CP           $04
6944: 30 0F      JR           NC,$6955
6946: F0 EC      LD           A,($EC)
6948: 21 99 FF   LD           HL,$FF99
694B: 96         SUB         (HL)
694C: C6 02      ADD         $02
694E: FE 04      CP           $04
6950: 30 03      JR           NC,$6955
6952: CD 44 6D   CALL       $6D44
6955: F1         POP         AF
6956: 21 50 C2   LD           HL,$C250
6959: 09         ADD         HL,BC
695A: 77         LD           (HL),A
695B: F1         POP         AF
695C: 21 40 C2   LD           HL,$C240
695F: 09         ADD         HL,BC
6960: 77         LD           (HL),A
6961: F1         POP         AF
6962: E0 99      LDFF00   ($99),A
6964: F1         POP         AF
6965: E0 98      LDFF00   ($98),A
6967: C1         POP         BC
6968: D1         POP         DE
6969: 1D         DEC         E
696A: 7B         LD           A,E
696B: FE FF      CP           $FF
696D: C2 D3 68   JP           NZ,$68D3
6970: C9         RET
6971: F0 F7      LD           A,($F7)
6973: FE 14      CP           $14
6975: 38 15      JR           C,$698C
6977: F0 F8      LD           A,($F8)
6979: E6 10      AND         $10
697B: C2 44 6D   JP           NZ,$6D44
697E: 21 60 C4   LD           HL,$C460
6981: 09         ADD         HL,BC
6982: 36 FF      LD           (HL),$FF
6984: 21 E0 C4   LD           HL,$C4E0
6987: 09         ADD         HL,BC
6988: 36 3C      LD           (HL),$3C
698A: 18 0C      JR           $6998
698C: 5F         LD           E,A
698D: 50         LD           D,B
698E: 21 65 DB   LD           HL,$DB65
6991: 19         ADD         HL,DE
6992: 7E         LD           A,(HL)
6993: E6 01      AND         $01
6995: C2 44 6D   JP           NZ,$6D44
6998: CD 8B 6A   CALL       $6A8B
699B: CD BA 3D   CALL       $3DBA
699E: CD 1F 7F   CALL       $7F1F
69A1: CD 4A 6D   CALL       $6D4A
69A4: 21 30 C4   LD           HL,$C430
69A7: 09         ADD         HL,BC
69A8: 36 00      LD           (HL),$00
69AA: CD B4 3B   CALL       $3BB4
69AD: F0 F0      LD           A,($F0)
69AF: C7         RST         0X00
69B0: B6         OR           (HL)
69B1: 69         LD           L,C
69B2: 01 6A 2E   LD           BC,$2E6A
69B5: 6A         LD           L,D
69B6: CD 91 08   CALL       $0891
69B9: 20 2D      JR           NZ,$69E8
69BB: F0 E7      LD           A,($E7)
69BD: A9         XOR         C
69BE: E6 07      AND         $07
69C0: 20 05      JR           NZ,$69C7
69C2: 3E 04      LD           A,$04
69C4: CD 25 3C   CALL       $3C25
69C7: CD 94 6D   CALL       $6D94
69CA: CD 9E 3B   CALL       $3B9E
69CD: CD FF 6D   CALL       $6DFF
69D0: C6 30      ADD         $30
69D2: FE 60      CP           $60
69D4: 30 12      JR           NC,$69E8
69D6: CD 0F 6E   CALL       $6E0F
69D9: C6 30      ADD         $30
69DB: FE 60      CP           $60
69DD: 30 09      JR           NC,$69E8
69DF: CD 91 08   CALL       $0891
69E2: 36 28      LD           (HL),$28
69E4: CD 8D 3B   CALL       $3B8D
69E7: C9         RET
69E8: F0 E7      LD           A,($E7)
69EA: E6 01      AND         $01
69EC: 20 F9      JR           NZ,$69E7
69EE: 21 D0 C3   LD           HL,$C3D0
69F1: 09         ADD         HL,BC
69F2: 34         INC         (HL)
69F3: 7E         LD           A,(HL)
69F4: 1F         RRA
69F5: 1F         RRA
69F6: 1F         RRA
69F7: E6 01      AND         $01
69F9: CD 87 3B   CALL       $3B87
69FC: C9         RET
69FD: 04         INC         B
69FE: 0C         INC         C
69FF: 00         NOP
6A00: 08 CD 91   LD           ($91CD),SP
6A03: 08 20 25   LD           ($2520),SP
6A06: CD 1F 6E   CALL       $6E1F
6A09: 21 80 C3   LD           HL,$C380
6A0C: 09         ADD         HL,BC
6A0D: 73         LD           (HL),E
6A0E: 50         LD           D,B
6A0F: 21 D0 C3   LD           HL,$C3D0
6A12: 09         ADD         HL,BC
6A13: 7E         LD           A,(HL)
6A14: E6 0F      AND         $0F
6A16: 21 FD 69   LD           HL,$69FD
6A19: 19         ADD         HL,DE
6A1A: BE         CP           (HL)
6A1B: 20 0E      JR           NZ,$6A2B
6A1D: 21 B0 C2   LD           HL,$C2B0
6A20: 09         ADD         HL,BC
6A21: 36 38      LD           (HL),$38
6A23: 21 40 C4   LD           HL,$C440
6A26: 09         ADD         HL,BC
6A27: 70         LD           (HL),B
6A28: CD 8D 3B   CALL       $3B8D
6A2B: C3 EE 69   JP           $69EE
6A2E: CD E7 6D   CALL       $6DE7
6A31: 21 B0 C2   LD           HL,$C2B0
6A34: 09         ADD         HL,BC
6A35: 35         DEC         (HL)
6A36: 35         DEC         (HL)
6A37: F0 E7      LD           A,($E7)
6A39: E6 03      AND         $03
6A3B: 20 05      JR           NZ,$6A42
6A3D: 21 40 C4   LD           HL,$C440
6A40: 09         ADD         HL,BC
6A41: 34         INC         (HL)
6A42: 21 D0 C2   LD           HL,$C2D0
6A45: 09         ADD         HL,BC
6A46: 7E         LD           A,(HL)
6A47: A7         AND         A
6A48: 28 04      JR           Z,$6A4E
6A4A: E6 80      AND         $80
6A4C: 28 1C      JR           Z,$6A6A
6A4E: 70         LD           (HL),B
6A4F: CD 8D 3B   CALL       $3B8D
6A52: 70         LD           (HL),B
6A53: CD 91 08   CALL       $0891
6A56: 36 10      LD           (HL),$10
6A58: 21 80 C3   LD           HL,$C380
6A5B: 09         ADD         HL,BC
6A5C: 5E         LD           E,(HL)
6A5D: 50         LD           D,B
6A5E: 21 FD 69   LD           HL,$69FD
6A61: 19         ADD         HL,DE
6A62: 7E         LD           A,(HL)
6A63: C6 08      ADD         $08
6A65: 21 D0 C3   LD           HL,$C3D0
6A68: 09         ADD         HL,BC
6A69: 77         LD           (HL),A
6A6A: C9         RET
6A6B: 70         LD           (HL),B
6A6C: 00         NOP
6A6D: 72         LD           (HL),D
6A6E: 00         NOP
6A6F: 74         LD           (HL),H
6A70: 00         NOP
6A71: 76         HALT
6A72: 00         NOP
6A73: 78         LD           A,B
6A74: 00         NOP
6A75: 78         LD           A,B
6A76: 20 0A      JR           NZ,$6A82
6A78: 06 03      LD           B,$03
6A7A: 01 00 01   LD           BC,$0100
6A7D: 03         INC         BC
6A7E: 06 0A      LD           B,$0A
6A80: 0E 11      LD           C,$11
6A82: 13         INC         DE
6A83: 14         INC         D
6A84: 13         INC         DE
6A85: 11 0E 0A   LD           DE,$0A0E
6A88: 06 03      LD           B,$03
6A8A: 01 11 6B   LD           BC,$6B11
6A8D: 6A         LD           L,D
6A8E: CD 3B 3C   CALL       $3C3B
6A91: 21 D0 C2   LD           HL,$C2D0
6A94: 09         ADD         HL,BC
6A95: 7E         LD           A,(HL)
6A96: A7         AND         A
6A97: 28 5C      JR           Z,$6AF5
6A99: AF         XOR         A
6A9A: E0 D7      LDFF00   ($D7),A
6A9C: 21 80 C3   LD           HL,$C380
6A9F: 09         ADD         HL,BC
6AA0: 7E         LD           A,(HL)
6AA1: 21 D0 C2   LD           HL,$C2D0
6AA4: 09         ADD         HL,BC
6AA5: CB 4F      BIT         1,E
6AA7: 20 26      JR           NZ,$6ACF
6AA9: FE 01      CP           $01
6AAB: 7E         LD           A,(HL)
6AAC: 20 06      JR           NZ,$6AB4
6AAE: 21 D7 FF   LD           HL,$FFD7
6AB1: 34         INC         (HL)
6AB2: 2F         CPL
6AB3: 3C         INC         A
6AB4: 21 EE FF   LD           HL,$FFEE
6AB7: 86         ADD         A,(HL)
6AB8: 77         LD           (HL),A
6AB9: 21 40 C4   LD           HL,$C440
6ABC: 09         ADD         HL,BC
6ABD: F0 D7      LD           A,($D7)
6ABF: A7         AND         A
6AC0: 7E         LD           A,(HL)
6AC1: 28 03      JR           Z,$6AC6
6AC3: 2F         CPL
6AC4: E6 0F      AND         $0F
6AC6: 21 EC FF   LD           HL,$FFEC
6AC9: 86         ADD         A,(HL)
6ACA: C6 F3      ADD         $F3
6ACC: 77         LD           (HL),A
6ACD: 18 46      JR           $6B15
6ACF: FE 02      CP           $02
6AD1: 7E         LD           A,(HL)
6AD2: 20 06      JR           NZ,$6ADA
6AD4: 21 D7 FF   LD           HL,$FFD7
6AD7: 34         INC         (HL)
6AD8: 2F         CPL
6AD9: 3C         INC         A
6ADA: 21 EC FF   LD           HL,$FFEC
6ADD: 86         ADD         A,(HL)
6ADE: 77         LD           (HL),A
6ADF: 21 40 C4   LD           HL,$C440
6AE2: 09         ADD         HL,BC
6AE3: F0 D7      LD           A,($D7)
6AE5: A7         AND         A
6AE6: 7E         LD           A,(HL)
6AE7: 20 03      JR           NZ,$6AEC
6AE9: 2F         CPL
6AEA: E6 0F      AND         $0F
6AEC: 21 EE FF   LD           HL,$FFEE
6AEF: 86         ADD         A,(HL)
6AF0: C6 F8      ADD         $F8
6AF2: 77         LD           (HL),A
6AF3: 18 20      JR           $6B15
6AF5: 21 D0 C3   LD           HL,$C3D0
6AF8: 09         ADD         HL,BC
6AF9: 7E         LD           A,(HL)
6AFA: E6 0F      AND         $0F
6AFC: 5F         LD           E,A
6AFD: 16 00      LD           D,$00
6AFF: 21 77 6A   LD           HL,$6A77
6B02: 19         ADD         HL,DE
6B03: F0 EC      LD           A,($EC)
6B05: 86         ADD         A,(HL)
6B06: C6 F0      ADD         $F0
6B08: E0 EC      LDFF00   ($EC),A
6B0A: 21 7B 6A   LD           HL,$6A7B
6B0D: 19         ADD         HL,DE
6B0E: F0 EE      LD           A,($EE)
6B10: 86         ADD         A,(HL)
6B11: C6 F3      ADD         $F3
6B13: E0 EE      LDFF00   ($EE),A
6B15: 3E 02      LD           A,$02
6B17: E0 F1      LDFF00   ($F1),A
6B19: 11 6B 6A   LD           DE,$6A6B
6B1C: CD 3B 3C   CALL       $3C3B
6B1F: 21 40 C4   LD           HL,$C440
6B22: 09         ADD         HL,BC
6B23: 7E         LD           A,(HL)
6B24: A7         AND         A
6B25: CA A7 6B   JP           Z,$6BA7
6B28: 21 B0 C2   LD           HL,$C2B0
6B2B: 09         ADD         HL,BC
6B2C: 7E         LD           A,(HL)
6B2D: E6 80      AND         $80
6B2F: 20 11      JR           NZ,$6B42
6B31: CD 8C 08   CALL       $088C
6B34: 20 0C      JR           NZ,$6B42
6B36: 21 30 C4   LD           HL,$C430
6B39: 09         ADD         HL,BC
6B3A: 36 40      LD           (HL),$40
6B3C: CD B4 3B   CALL       $3BB4
6B3F: CD A8 6B   CALL       $6BA8
6B42: F0 EE      LD           A,($EE)
6B44: C6 04      ADD         $04
6B46: 21 00 C2   LD           HL,$C200
6B49: 09         ADD         HL,BC
6B4A: 96         SUB         (HL)
6B4B: CB 2F      SRA         1,E
6B4D: CB 2F      SRA         1,E
6B4F: E0 D7      LDFF00   ($D7),A
6B51: E0 D9      LDFF00   ($D9),A
6B53: F0 EC      LD           A,($EC)
6B55: 21 10 C2   LD           HL,$C210
6B58: 09         ADD         HL,BC
6B59: 96         SUB         (HL)
6B5A: CB 2F      SRA         1,E
6B5C: CB 2F      SRA         1,E
6B5E: E0 D8      LDFF00   ($D8),A
6B60: E0 DA      LDFF00   ($DA),A
6B62: FA C0 C3   LD           A,($C3C0)
6B65: 5F         LD           E,A
6B66: 16 00      LD           D,$00
6B68: 21 30 C0   LD           HL,$C030
6B6B: 19         ADD         HL,DE
6B6C: E5         PUSH       HL
6B6D: D1         POP         DE
6B6E: CD BA 3D   CALL       $3DBA
6B71: 3E 03      LD           A,$03
6B73: E0 DB      LDFF00   ($DB),A
6B75: F0 EC      LD           A,($EC)
6B77: 21 D8 FF   LD           HL,$FFD8
6B7A: 86         ADD         A,(HL)
6B7B: 12         LD           (DE),A
6B7C: 13         INC         DE
6B7D: F0 EE      LD           A,($EE)
6B7F: 21 D7 FF   LD           HL,$FFD7
6B82: 86         ADD         A,(HL)
6B83: 12         LD           (DE),A
6B84: 13         INC         DE
6B85: 3E 24      LD           A,$24
6B87: 12         LD           (DE),A
6B88: 13         INC         DE
6B89: 3E 00      LD           A,$00
6B8B: 12         LD           (DE),A
6B8C: 13         INC         DE
6B8D: F0 D7      LD           A,($D7)
6B8F: 21 D9 FF   LD           HL,$FFD9
6B92: 86         ADD         A,(HL)
6B93: E0 D7      LDFF00   ($D7),A
6B95: F0 D8      LD           A,($D8)
6B97: 21 DA FF   LD           HL,$FFDA
6B9A: 86         ADD         A,(HL)
6B9B: E0 D8      LDFF00   ($D8),A
6B9D: F0 DB      LD           A,($DB)
6B9F: 3D         DEC         A
6BA0: 20 D1      JR           NZ,$6B73
6BA2: 3E 03      LD           A,$03
6BA4: CD D0 3D   CALL       $3DD0
6BA7: C9         RET
6BA8: F0 EE      LD           A,($EE)
6BAA: E0 DB      LDFF00   ($DB),A
6BAC: CB 37      SWAP        1,E
6BAE: E6 0F      AND         $0F
6BB0: 5F         LD           E,A
6BB1: F0 EC      LD           A,($EC)
6BB3: D6 10      SUB         $10
6BB5: C6 04      ADD         $04
6BB7: E0 DC      LDFF00   ($DC),A
6BB9: E6 F0      AND         $F0
6BBB: B3         OR           E
6BBC: 5F         LD           E,A
6BBD: 16 00      LD           D,$00
6BBF: 21 11 D7   LD           HL,$D711
6BC2: 7C         LD           A,H
6BC3: 19         ADD         HL,DE
6BC4: 67         LD           H,A
6BC5: 7E         LD           A,(HL)
6BC6: E0 AF      LDFF00   ($AF),A
6BC8: 5F         LD           E,A
6BC9: FA A5 DB   LD           A,($DBA5)
6BCC: 57         LD           D,A
6BCD: CD DB 29   CALL       $29DB
6BD0: FE 00      CP           $00
6BD2: 28 22      JR           Z,$6BF6
6BD4: FE 01      CP           $01
6BD6: 20 1E      JR           NZ,$6BF6
6BD8: 21 B0 C2   LD           HL,$C2B0
6BDB: 09         ADD         HL,BC
6BDC: 7E         LD           A,(HL)
6BDD: 2F         CPL
6BDE: 3C         INC         A
6BDF: 77         LD           (HL),A
6BE0: CD 8C 08   CALL       $088C
6BE3: 36 08      LD           (HL),$08
6BE5: 3E 07      LD           A,$07
6BE7: E0 F2      LDFF00   ($F2),A
6BE9: F0 EE      LD           A,($EE)
6BEB: E0 D7      LDFF00   ($D7),A
6BED: F0 EC      LD           A,($EC)
6BEF: E0 D8      LDFF00   ($D8),A
6BF1: 3E 05      LD           A,$05
6BF3: CD 53 09   CALL       $0953
6BF6: C9         RET
6BF7: 70         LD           (HL),B
6BF8: 00         NOP
6BF9: 70         LD           (HL),B
6BFA: 20 78      JR           NZ,$6C74
6BFC: 00         NOP
6BFD: 7A         LD           A,D
6BFE: 00         NOP
6BFF: 74         LD           (HL),H
6C00: 00         NOP
6C01: 76         HALT
6C02: 00         NOP
6C03: 7C         LD           A,H
6C04: 00         NOP
6C05: 7E         LD           A,(HL)
6C06: 00         NOP
6C07: 72         LD           (HL),D
6C08: 00         NOP
6C09: 72         LD           (HL),D
6C0A: 20 7E      JR           NZ,$6C8A
6C0C: 20 7C      JR           NZ,$6C8A
6C0E: 20 76      JR           NZ,$6C86
6C10: 20 74      JR           NZ,$6C86
6C12: 20 7A      JR           NZ,$6C8E
6C14: 20 78      JR           NZ,$6C8E
6C16: 20 10      JR           NZ,$6C28
6C18: 0E 0C      LD           C,$0C
6C1A: 06 00      LD           B,$00
6C1C: FA F4 F2   LD           A,($F2F4)
6C1F: F0 F2      LD           A,($F2)
6C21: F4                              
6C22: FA 00 06   LD           A,($0600)
6C25: 0C         INC         C
6C26: 0E 10      LD           C,$10
6C28: 0E 0C      LD           C,$0C
6C2A: 06 F0      LD           B,$F0
6C2C: F0 A7      LD           A,($A7)
6C2E: C2 D9 6C   JP           NZ,$6CD9
6C31: 11 F7 6B   LD           DE,$6BF7
6C34: CD 3B 3C   CALL       $3C3B
6C37: CD 1F 7F   CALL       $7F1F
6C3A: CD BF 3B   CALL       $3BBF
6C3D: CD 9E 3B   CALL       $3B9E
6C40: CD 91 08   CALL       $0891
6C43: 28 39      JR           Z,$6C7E
6C45: FE 10      CP           $10
6C47: 20 34      JR           NZ,$6C7D
6C49: 3E 2B      LD           A,$2B
6C4B: CD 01 3C   CALL       $3C01
6C4E: 38 2D      JR           C,$6C7D
6C50: 3E 08      LD           A,$08
6C52: E0 F4      LDFF00   ($F4),A
6C54: F0 D7      LD           A,($D7)
6C56: 21 00 C2   LD           HL,$C200
6C59: 19         ADD         HL,DE
6C5A: 77         LD           (HL),A
6C5B: F0 D8      LD           A,($D8)
6C5D: 21 10 C2   LD           HL,$C210
6C60: 19         ADD         HL,DE
6C61: 77         LD           (HL),A
6C62: F0 D9      LD           A,($D9)
6C64: 21 80 C3   LD           HL,$C380
6C67: 19         ADD         HL,DE
6C68: 77         LD           (HL),A
6C69: 21 40 C2   LD           HL,$C240
6C6C: 09         ADD         HL,BC
6C6D: 7E         LD           A,(HL)
6C6E: 21 40 C2   LD           HL,$C240
6C71: 19         ADD         HL,DE
6C72: 77         LD           (HL),A
6C73: 21 50 C2   LD           HL,$C250
6C76: 09         ADD         HL,BC
6C77: 7E         LD           A,(HL)
6C78: 21 50 C2   LD           HL,$C250
6C7B: 19         ADD         HL,DE
6C7C: 77         LD           (HL),A
6C7D: C9         RET
6C7E: 21 D0 C3   LD           HL,$C3D0
6C81: 09         ADD         HL,BC
6C82: 7E         LD           A,(HL)
6C83: 3C         INC         A
6C84: 77         LD           (HL),A
6C85: E6 07      AND         $07
6C87: 20 4F      JR           NZ,$6CD8
6C89: 21 80 C3   LD           HL,$C380
6C8C: 09         ADD         HL,BC
6C8D: 7E         LD           A,(HL)
6C8E: 3C         INC         A
6C8F: E6 0F      AND         $0F
6C91: 77         LD           (HL),A
6C92: CB 3F      SRL         1,E
6C94: 21 B0 C3   LD           HL,$C3B0
6C97: 09         ADD         HL,BC
6C98: 77         LD           (HL),A
6C99: 3E 2A      LD           A,$2A
6C9B: CD 01 3C   CALL       $3C01
6C9E: 38 38      JR           C,$6CD8
6CA0: F0 D7      LD           A,($D7)
6CA2: 21 00 C2   LD           HL,$C200
6CA5: 19         ADD         HL,DE
6CA6: 77         LD           (HL),A
6CA7: F0 D8      LD           A,($D8)
6CA9: 21 10 C2   LD           HL,$C210
6CAC: 19         ADD         HL,DE
6CAD: 77         LD           (HL),A
6CAE: 21 90 C2   LD           HL,$C290
6CB1: 19         ADD         HL,DE
6CB2: 36 01      LD           (HL),$01
6CB4: 21 B0 C2   LD           HL,$C2B0
6CB7: 19         ADD         HL,DE
6CB8: 71         LD           (HL),C
6CB9: 21 40 C3   LD           HL,$C340
6CBC: 19         ADD         HL,DE
6CBD: 36 C0      LD           (HL),$C0
6CBF: C5         PUSH       BC
6CC0: F0 D9      LD           A,($D9)
6CC2: 4F         LD           C,A
6CC3: 21 1B 6C   LD           HL,$6C1B
6CC6: 09         ADD         HL,BC
6CC7: 7E         LD           A,(HL)
6CC8: 21 40 C2   LD           HL,$C240
6CCB: 19         ADD         HL,DE
6CCC: 77         LD           (HL),A
6CCD: 21 17 6C   LD           HL,$6C17
6CD0: 09         ADD         HL,BC
6CD1: 7E         LD           A,(HL)
6CD2: 21 50 C2   LD           HL,$C250
6CD5: 19         ADD         HL,DE
6CD6: 77         LD           (HL),A
6CD7: C1         POP         BC
6CD8: C9         RET
6CD9: CD A9 3B   CALL       $3BA9
6CDC: 21 A0 C2   LD           HL,$C2A0
6CDF: 09         ADD         HL,BC
6CE0: 7E         LD           A,(HL)
6CE1: A7         AND         A
6CE2: C2 44 6D   JP           NZ,$6D44
6CE5: F0 EE      LD           A,($EE)
6CE7: 21 98 FF   LD           HL,$FF98
6CEA: 96         SUB         (HL)
6CEB: C6 10      ADD         $10
6CED: FE 20      CP           $20
6CEF: 30 35      JR           NC,$6D26
6CF1: F0 EF      LD           A,($EF)
6CF3: 21 99 FF   LD           HL,$FF99
6CF6: 96         SUB         (HL)
6CF7: C6 10      ADD         $10
6CF9: FE 20      CP           $20
6CFB: 30 29      JR           NC,$6D26
6CFD: CD 44 6D   CALL       $6D44
6D00: FA C7 DB   LD           A,($DBC7)
6D03: A7         AND         A
6D04: 20 20      JR           NZ,$6D26
6D06: 21 B0 C2   LD           HL,$C2B0
6D09: 09         ADD         HL,BC
6D0A: 5E         LD           E,(HL)
6D0B: 50         LD           D,B
6D0C: 21 E0 C2   LD           HL,$C2E0
6D0F: 19         ADD         HL,DE
6D10: 7E         LD           A,(HL)
6D11: A7         AND         A
6D12: 20 12      JR           NZ,$6D26
6D14: 36 20      LD           (HL),$20
6D16: 21 20 C4   LD           HL,$C420
6D19: 19         ADD         HL,DE
6D1A: 36 10      LD           (HL),$10
6D1C: C5         PUSH       BC
6D1D: D5         PUSH       DE
6D1E: C1         POP         BC
6D1F: 3E 40      LD           A,$40
6D21: CD 25 3C   CALL       $3C25
6D24: C1         POP         BC
6D25: C9         RET
6D26: 21 40 C2   LD           HL,$C240
6D29: 09         ADD         HL,BC
6D2A: 7E         LD           A,(HL)
6D2B: 21 00 C2   LD           HL,$C200
6D2E: 09         ADD         HL,BC
6D2F: 86         ADD         A,(HL)
6D30: 77         LD           (HL),A
6D31: FE 9C      CP           $9C
6D33: D2 44 6D   JP           NC,$6D44
6D36: 21 50 C2   LD           HL,$C250
6D39: 09         ADD         HL,BC
6D3A: 7E         LD           A,(HL)
6D3B: 21 10 C2   LD           HL,$C210
6D3E: 09         ADD         HL,BC
6D3F: 86         ADD         A,(HL)
6D40: 77         LD           (HL),A
6D41: FE 78      CP           $78
6D43: D8         RET         C
6D44: 21 80 C2   LD           HL,$C280
6D47: 09         ADD         HL,BC
6D48: 70         LD           (HL),B
6D49: C9         RET
6D4A: 21 10 C4   LD           HL,$C410
6D4D: 09         ADD         HL,BC
6D4E: 7E         LD           A,(HL)
6D4F: A7         AND         A
6D50: 28 41      JR           Z,$6D93
6D52: 3D         DEC         A
6D53: 77         LD           (HL),A
6D54: CD B8 3E   CALL       $3EB8
6D57: 21 40 C2   LD           HL,$C240
6D5A: 09         ADD         HL,BC
6D5B: 7E         LD           A,(HL)
6D5C: F5         PUSH       AF
6D5D: 21 50 C2   LD           HL,$C250
6D60: 09         ADD         HL,BC
6D61: 7E         LD           A,(HL)
6D62: F5         PUSH       AF
6D63: 21 F0 C3   LD           HL,$C3F0
6D66: 09         ADD         HL,BC
6D67: 7E         LD           A,(HL)
6D68: 21 40 C2   LD           HL,$C240
6D6B: 09         ADD         HL,BC
6D6C: 77         LD           (HL),A
6D6D: 21 00 C4   LD           HL,$C400
6D70: 09         ADD         HL,BC
6D71: 7E         LD           A,(HL)
6D72: 21 50 C2   LD           HL,$C250
6D75: 09         ADD         HL,BC
6D76: 77         LD           (HL),A
6D77: CD 94 6D   CALL       $6D94
6D7A: 21 30 C4   LD           HL,$C430
6D7D: 09         ADD         HL,BC
6D7E: 7E         LD           A,(HL)
6D7F: E6 20      AND         $20
6D81: 20 03      JR           NZ,$6D86
6D83: CD 9E 3B   CALL       $3B9E
6D86: 21 50 C2   LD           HL,$C250
6D89: 09         ADD         HL,BC
6D8A: F1         POP         AF
6D8B: 77         LD           (HL),A
6D8C: 21 40 C2   LD           HL,$C240
6D8F: 09         ADD         HL,BC
6D90: F1         POP         AF
6D91: 77         LD           (HL),A
6D92: F1         POP         AF
6D93: C9         RET
6D94: CD A1 6D   CALL       $6DA1
6D97: C5         PUSH       BC
6D98: 79         LD           A,C
6D99: C6 10      ADD         $10
6D9B: 4F         LD           C,A
6D9C: CD A1 6D   CALL       $6DA1
6D9F: C1         POP         BC
6DA0: C9         RET
6DA1: 21 40 C2   LD           HL,$C240
6DA4: 09         ADD         HL,BC
6DA5: 7E         LD           A,(HL)
6DA6: A7         AND         A
6DA7: 28 23      JR           Z,$6DCC
6DA9: F5         PUSH       AF
6DAA: CB 37      SWAP        1,E
6DAC: E6 F0      AND         $F0
6DAE: 21 60 C2   LD           HL,$C260
6DB1: 09         ADD         HL,BC
6DB2: 86         ADD         A,(HL)
6DB3: 77         LD           (HL),A
6DB4: CB 12      RL          1,E
6DB6: 21 00 C2   LD           HL,$C200
6DB9: 09         ADD         HL,BC
6DBA: F1         POP         AF
6DBB: 1E 00      LD           E,$00
6DBD: CB 7F      BIT         1,E
6DBF: 28 02      JR           Z,$6DC3
6DC1: 1E F0      LD           E,$F0
6DC3: CB 37      SWAP        1,E
6DC5: E6 0F      AND         $0F
6DC7: B3         OR           E
6DC8: CB 1A      RR          1,E
6DCA: 8E         ADC         A,(HL)
6DCB: 77         LD           (HL),A
6DCC: C9         RET
6DCD: 21 20 C3   LD           HL,$C320
6DD0: 09         ADD         HL,BC
6DD1: 7E         LD           A,(HL)
6DD2: A7         AND         A
6DD3: 28 F7      JR           Z,$6DCC
6DD5: F5         PUSH       AF
6DD6: CB 37      SWAP        1,E
6DD8: E6 F0      AND         $F0
6DDA: 21 30 C3   LD           HL,$C330
6DDD: 09         ADD         HL,BC
6DDE: 86         ADD         A,(HL)
6DDF: 77         LD           (HL),A
6DE0: CB 12      RL          1,E
6DE2: 21 10 C3   LD           HL,$C310
6DE5: 18 D2      JR           $6DB9
6DE7: 21 B0 C2   LD           HL,$C2B0
6DEA: 09         ADD         HL,BC
6DEB: 7E         LD           A,(HL)
6DEC: F5         PUSH       AF
6DED: CB 37      SWAP        1,E
6DEF: E6 F0      AND         $F0
6DF1: 21 C0 C2   LD           HL,$C2C0
6DF4: 09         ADD         HL,BC
6DF5: 86         ADD         A,(HL)
6DF6: 77         LD           (HL),A
6DF7: CB 12      RL          1,E
6DF9: 21 D0 C2   LD           HL,$C2D0
6DFC: C3 B9 6D   JP           $6DB9
6DFF: 1E 00      LD           E,$00
6E01: F0 98      LD           A,($98)
6E03: 21 00 C2   LD           HL,$C200
6E06: 09         ADD         HL,BC
6E07: 96         SUB         (HL)
6E08: CB 7F      BIT         1,E
6E0A: 28 01      JR           Z,$6E0D
6E0C: 1C         INC         E
6E0D: 57         LD           D,A
6E0E: C9         RET
6E0F: 1E 02      LD           E,$02
6E11: F0 99      LD           A,($99)
6E13: 21 10 C2   LD           HL,$C210
6E16: 09         ADD         HL,BC
6E17: 96         SUB         (HL)
6E18: CB 7F      BIT         1,E
6E1A: 20 01      JR           NZ,$6E1D
6E1C: 1C         INC         E
6E1D: 57         LD           D,A
6E1E: C9         RET
6E1F: CD FF 6D   CALL       $6DFF
6E22: 7B         LD           A,E
6E23: E0 D7      LDFF00   ($D7),A
6E25: 7A         LD           A,D
6E26: CB 7F      BIT         1,E
6E28: 28 02      JR           Z,$6E2C
6E2A: 2F         CPL
6E2B: 3C         INC         A
6E2C: F5         PUSH       AF
6E2D: CD 0F 6E   CALL       $6E0F
6E30: 7B         LD           A,E
6E31: E0 D8      LDFF00   ($D8),A
6E33: 7A         LD           A,D
6E34: CB 7F      BIT         1,E
6E36: 28 02      JR           Z,$6E3A
6E38: 2F         CPL
6E39: 3C         INC         A
6E3A: D1         POP         DE
6E3B: BA         CP           D
6E3C: 30 04      JR           NC,$6E42
6E3E: F0 D7      LD           A,($D7)
6E40: 18 02      JR           $6E44
6E42: F0 D8      LD           A,($D8)
6E44: 5F         LD           E,A
6E45: C9         RET
6E46: FA 73 DB   LD           A,($DB73)
6E49: F5         PUSH       AF
6E4A: F0 F8      LD           A,($F8)
6E4C: E6 10      AND         $10
6E4E: 28 04      JR           Z,$6E54
6E50: AF         XOR         A
6E51: EA 73 DB   LD           ($DB73),A
6E54: CD 5C 6E   CALL       $6E5C
6E57: F1         POP         AF
6E58: EA 73 DB   LD           ($DB73),A
6E5B: C9         RET
6E5C: 21 B0 C2   LD           HL,$C2B0
6E5F: 09         ADD         HL,BC
6E60: 7E         LD           A,(HL)
6E61: A7         AND         A
6E62: C2 37 74   JP           NZ,$7437
6E65: 79         LD           A,C
6E66: EA 10 D2   LD           ($D210),A
6E69: 3E 02      LD           A,$02
6E6B: EA 0A C5   LD           ($C50A),A
6E6E: CD 8C 08   CALL       $088C
6E71: 3D         DEC         A
6E72: 20 04      JR           NZ,$6E78
6E74: 3E 19      LD           A,$19
6E76: E0 F2      LDFF00   ($F2),A
6E78: F0 F1      LD           A,($F1)
6E7A: 3C         INC         A
6E7B: 28 17      JR           Z,$6E94
6E7D: F0 E7      LD           A,($E7)
6E7F: E6 1F      AND         $1F
6E81: 20 08      JR           NZ,$6E8B
6E83: CD 1F 6E   CALL       $6E1F
6E86: 21 80 C3   LD           HL,$C380
6E89: 09         ADD         HL,BC
6E8A: 73         LD           (HL),E
6E8B: CD 09 7C   CALL       $7C09
6E8E: 11 59 76   LD           DE,$7659
6E91: CD 3B 3C   CALL       $3C3B
6E94: CD 6E 73   CALL       $736E
6E97: CD BA 3D   CALL       $3DBA
6E9A: CD 54 7B   CALL       $7B54
6E9D: CD 27 73   CALL       $7327
6EA0: F0 F0      LD           A,($F0)
6EA2: FE 03      CP           $03
6EA4: 38 0D      JR           C,$6EB3
6EA6: FA 73 DB   LD           A,($DB73)
6EA9: A7         AND         A
6EAA: 28 07      JR           Z,$6EB3
6EAC: 3E 02      LD           A,$02
6EAE: E0 A1      LDFF00   ($A1),A
6EB0: EA 67 C1   LD           ($C167),A
6EB3: F0 F0      LD           A,($F0)
6EB5: C7         RST         0X00
6EB6: EE 6E      XOR         $6E
6EB8: 69         LD           L,C
6EB9: 6F         LD           L,A
6EBA: C6 6F      ADD         $6F
6EBC: 26 70      LD           H,$70
6EBE: A4         AND         H
6EBF: 70         LD           (HL),B
6EC0: FE 70      CP           $70
6EC2: 24         INC         H
6EC3: 71         LD           (HL),C
6EC4: 63         LD           H,E
6EC5: 71         LD           (HL),C
6EC6: AD         XOR         L
6EC7: 71         LD           (HL),C
6EC8: E3                              
6EC9: 71         LD           (HL),C
6ECA: 00         NOP
6ECB: 72         LD           (HL),D
6ECC: 5C         LD           E,H
6ECD: 72         LD           (HL),D
6ECE: 9E         SBC         (HL)
6ECF: 72         LD           (HL),D
6ED0: 38 58      JR           C,$6F2A
6ED2: 78         LD           A,B
6ED3: 58         LD           E,B
6ED4: 40         LD           B,B
6ED5: 70         LD           (HL),B
6ED6: 2E 2E      LD           L,$2E
6ED8: 2E 3E      LD           L,$3E
6EDA: 4E         LD           C,(HL)
6EDB: 4E         LD           C,(HL)
6EDC: 00         NOP
6EDD: 00         NOP
6EDE: 00         NOP
6EDF: 04         INC         B
6EE0: 01 02 05   LD           BC,$0502
6EE3: 02         LD           (BC),A
6EE4: 02         LD           (BC),A
6EE5: 00         NOP
6EE6: 03         INC         BC
6EE7: 04         INC         B
6EE8: 81         ADD         A,C
6EE9: 81         ADD         A,C
6EEA: 81         ADD         A,C
6EEB: 82         ADD         A,D
6EEC: 81         ADD         A,C
6EED: 81         ADD         A,C
6EEE: 1E 06      LD           E,$06
6EF0: 16 00      LD           D,$00
6EF2: D5         PUSH       DE
6EF3: 3E 4F      LD           A,$4F
6EF5: 1E 0E      LD           E,$0E
6EF7: CD 13 3C   CALL       $3C13
6EFA: 21 B0 C2   LD           HL,$C2B0
6EFD: 19         ADD         HL,DE
6EFE: 36 01      LD           (HL),$01
6F00: 21 C7 6E   LD           HL,$6EC7
6F03: 19         ADD         HL,DE
6F04: 7E         LD           A,(HL)
6F05: 21 00 C2   LD           HL,$C200
6F08: 19         ADD         HL,DE
6F09: 77         LD           (HL),A
6F0A: 21 CD 6E   LD           HL,$6ECD
6F0D: 19         ADD         HL,DE
6F0E: 7E         LD           A,(HL)
6F0F: 21 10 C2   LD           HL,$C210
6F12: 19         ADD         HL,DE
6F13: 77         LD           (HL),A
6F14: 21 D9 6E   LD           HL,$6ED9
6F17: 19         ADD         HL,DE
6F18: 7E         LD           A,(HL)
6F19: 21 B0 C3   LD           HL,$C3B0
6F1C: 19         ADD         HL,DE
6F1D: 77         LD           (HL),A
6F1E: 21 DF 6E   LD           HL,$6EDF
6F21: 19         ADD         HL,DE
6F22: 7E         LD           A,(HL)
6F23: 21 40 C3   LD           HL,$C340
6F26: 19         ADD         HL,DE
6F27: 77         LD           (HL),A
6F28: 21 D3 6E   LD           HL,$6ED3
6F2B: 19         ADD         HL,DE
6F2C: 7E         LD           A,(HL)
6F2D: 21 80 C3   LD           HL,$C380
6F30: 19         ADD         HL,DE
6F31: 77         LD           (HL),A
6F32: C5         PUSH       BC
6F33: D5         PUSH       DE
6F34: C1         POP         BC
6F35: CD 14 76   CALL       $7614
6F38: C1         POP         BC
6F39: D1         POP         DE
6F3A: 1D         DEC         E
6F3B: 20 B5      JR           NZ,$6EF2
6F3D: AF         XOR         A
6F3E: EA 06 D2   LD           ($D206),A
6F41: 3E 10      LD           A,$10
6F43: EA 02 D2   LD           ($D202),A
6F46: EA 03 D2   LD           ($D203),A
6F49: 3E 16      LD           A,$16
6F4B: EA 05 D2   LD           ($D205),A
6F4E: 3E 18      LD           A,$18
6F50: EA 04 D2   LD           ($D204),A
6F53: 3E 00      LD           A,$00
6F55: EA 00 D2   LD           ($D200),A
6F58: 3E 04      LD           A,$04
6F5A: EA 01 D2   LD           ($D201),A
6F5D: CD 8D 3B   CALL       $3B8D
6F60: FA 0E DB   LD           A,($DB0E)
6F63: 21 90 C3   LD           HL,$C390
6F66: 09         ADD         HL,BC
6F67: 77         LD           (HL),A
6F68: C9         RET
6F69: FA 67 C1   LD           A,($C167)
6F6C: A7         AND         A
6F6D: C0         RET         NZ
6F6E: FA 73 DB   LD           A,($DB73)
6F71: A7         AND         A
6F72: 28 11      JR           Z,$6F85
6F74: F0 98      LD           A,($98)
6F76: FE 6C      CP           $6C
6F78: 38 0B      JR           C,$6F85
6F7A: 21 A0 DA   LD           HL,$DAA0
6F7D: CB E6      SET         1,E
6F7F: 3E 6B      LD           A,$6B
6F81: E0 98      LDFF00   ($98),A
6F83: 18 05      JR           $6F8A
6F85: CD 77 7B   CALL       $7B77
6F88: 30 3B      JR           NC,$6FC5
6F8A: AF         XOR         A
6F8B: EA 20 C1   LD           ($C120),A
6F8E: E0 9A      LDFF00   ($9A),A
6F90: 1E 06      LD           E,$06
6F92: 21 90 C3   LD           HL,$C390
6F95: 09         ADD         HL,BC
6F96: 7E         LD           A,(HL)
6F97: A7         AND         A
6F98: 28 01      JR           Z,$6F9B
6F9A: 1D         DEC         E
6F9B: 21 40 C4   LD           HL,$C440
6F9E: 09         ADD         HL,BC
6F9F: 7E         LD           A,(HL)
6FA0: BB         CP           E
6FA1: 38 06      JR           C,$6FA9
6FA3: 3E 40      LD           A,$40
6FA5: CD 97 21   CALL       $2197
6FA8: C9         RET
6FA9: FA 73 DB   LD           A,($DB73)
6FAC: A7         AND         A
6FAD: 28 04      JR           Z,$6FB3
6FAF: 3E F7      LD           A,$F7
6FB1: 18 0C      JR           $6FBF
6FB3: 21 D0 C2   LD           HL,$C2D0
6FB6: 09         ADD         HL,BC
6FB7: 7E         LD           A,(HL)
6FB8: A7         AND         A
6FB9: 3E 3B      LD           A,$3B
6FBB: 28 02      JR           Z,$6FBF
6FBD: 3E 3E      LD           A,$3E
6FBF: CD 97 21   CALL       $2197
6FC2: CD 8D 3B   CALL       $3B8D
6FC5: C9         RET
6FC6: 3E 02      LD           A,$02
6FC8: E0 A1      LDFF00   ($A1),A
6FCA: FA 9F C1   LD           A,($C19F)
6FCD: A7         AND         A
6FCE: 20 32      JR           NZ,$7002
6FD0: FA 73 C1   LD           A,($C173)
6FD3: FE F8      CP           $F8
6FD5: 28 07      JR           Z,$6FDE
6FD7: FA 77 C1   LD           A,($C177)
6FDA: FE 01      CP           $01
6FDC: 30 13      JR           NC,$6FF1
6FDE: FA 5E DB   LD           A,($DB5E)
6FE1: D6 10      SUB         $10
6FE3: FA 5D DB   LD           A,($DB5D)
6FE6: DE 00      SBC         $00
6FE8: 30 19      JR           NC,$7003
6FEA: 3E 34      LD           A,$34
6FEC: CD 97 21   CALL       $2197
6FEF: 18 0B      JR           $6FFC
6FF1: FA 73 DB   LD           A,($DB73)
6FF4: A7         AND         A
6FF5: 28 05      JR           Z,$6FFC
6FF7: 3E F8      LD           A,$F8
6FF9: C3 97 21   JP           $2197
6FFC: 21 90 C2   LD           HL,$C290
6FFF: 09         ADD         HL,BC
7000: 36 01      LD           (HL),$01
7002: C9         RET
7003: FA 73 DB   LD           A,($DB73)
7006: A7         AND         A
7007: 28 03      JR           Z,$700C
7009: EA 74 DB   LD           ($DB74),A
700C: 21 D0 C2   LD           HL,$C2D0
700F: 09         ADD         HL,BC
7010: 7E         LD           A,(HL)
7011: 36 01      LD           (HL),$01
7013: A7         AND         A
7014: 3E 3C      LD           A,$3C
7016: 28 02      JR           Z,$701A
7018: 3E 3F      LD           A,$3F
701A: CD 97 21   CALL       $2197
701D: 3E 0A      LD           A,$0A
701F: EA 92 DB   LD           ($DB92),A
7022: CD 8D 3B   CALL       $3B8D
7025: C9         RET
7026: F0 E7      LD           A,($E7)
7028: 1F         RRA
7029: 1F         RRA
702A: 1F         RRA
702B: 1F         RRA
702C: E6 01      AND         $01
702E: EA 00 D2   LD           ($D200),A
7031: 3E 10      LD           A,$10
7033: EA 03 D2   LD           ($D203),A
7036: F0 E7      LD           A,($E7)
7038: E6 10      AND         $10
703A: EA 02 D2   LD           ($D202),A
703D: FA 73 DB   LD           A,($DB73)
7040: A7         AND         A
7041: 28 49      JR           Z,$708C
7043: CD 87 08   CALL       $0887
7046: 28 07      JR           Z,$704F
7048: 3D         DEC         A
7049: 20 03      JR           NZ,$704E
704B: CD 9C 70   CALL       $709C
704E: C9         RET
704F: CD 1F 7F   CALL       $7F1F
7052: C5         PUSH       BC
7053: FA 0F C5   LD           A,($C50F)
7056: 4F         LD           C,A
7057: F0 E7      LD           A,($E7)
7059: E6 10      AND         $10
705B: 3E 04      LD           A,$04
705D: 28 01      JR           Z,$7060
705F: 3C         INC         A
7060: CD 87 3B   CALL       $3B87
7063: 21 40 C2   LD           HL,$C240
7066: 09         ADD         HL,BC
7067: 36 F8      LD           (HL),$F8
7069: CD A1 6D   CALL       $6DA1
706C: 21 00 C2   LD           HL,$C200
706F: 09         ADD         HL,BC
7070: C1         POP         BC
7071: 7E         LD           A,(HL)
7072: FE 28      CP           $28
7074: 20 15      JR           NZ,$708B
7076: CD 87 08   CALL       $0887
7079: 36 18      LD           (HL),$18
707B: FA 0F C5   LD           A,($C50F)
707E: 5F         LD           E,A
707F: 50         LD           D,B
7080: 21 B0 C3   LD           HL,$C3B0
7083: 19         ADD         HL,DE
7084: 36 02      LD           (HL),$02
7086: 1E 01      LD           E,$01
7088: CD 9F 71   CALL       $719F
708B: C9         RET
708C: F0 CB      LD           A,($CB)
708E: E6 20      AND         $20
7090: 28 11      JR           Z,$70A3
7092: F0 98      LD           A,($98)
7094: FE 20      CP           $20
7096: 38 0B      JR           C,$70A3
7098: FE 30      CP           $30
709A: 30 07      JR           NC,$70A3
709C: CD 8D 3B   CALL       $3B8D
709F: 3E 20      LD           A,$20
70A1: E0 F4      LDFF00   ($F4),A
70A3: C9         RET
70A4: CD EA 70   CALL       $70EA
70A7: 3E 10      LD           A,$10
70A9: EA 03 D2   LD           ($D203),A
70AC: F0 E7      LD           A,($E7)
70AE: E6 10      AND         $10
70B0: EA 02 D2   LD           ($D202),A
70B3: FA 73 DB   LD           A,($DB73)
70B6: A7         AND         A
70B7: 28 07      JR           Z,$70C0
70B9: 1E 02      LD           E,$02
70BB: CD 9F 71   CALL       $719F
70BE: 18 06      JR           $70C6
70C0: F0 CB      LD           A,($CB)
70C2: E6 20      AND         $20
70C4: 28 11      JR           Z,$70D7
70C6: F0 E7      LD           A,($E7)
70C8: E6 03      AND         $03
70CA: 20 1D      JR           NZ,$70E9
70CC: FA 04 D2   LD           A,($D204)
70CF: 3C         INC         A
70D0: EA 04 D2   LD           ($D204),A
70D3: FE 88      CP           $88
70D5: 38 12      JR           C,$70E9
70D7: CD 8D 3B   CALL       $3B8D
70DA: FA 73 DB   LD           A,($DB73)
70DD: A7         AND         A
70DE: 28 05      JR           Z,$70E5
70E0: CD 87 08   CALL       $0887
70E3: 36 10      LD           (HL),$10
70E5: 3E 21      LD           A,$21
70E7: E0 F4      LDFF00   ($F4),A
70E9: C9         RET
70EA: F0 E7      LD           A,($E7)
70EC: 1F         RRA
70ED: 1F         RRA
70EE: 1F         RRA
70EF: 1F         RRA
70F0: E6 01      AND         $01
70F2: EA 00 D2   LD           ($D200),A
70F5: 3E 01      LD           A,$01
70F7: E0 A1      LDFF00   ($A1),A
70F9: 3E 02      LD           A,$02
70FB: E0 9E      LDFF00   ($9E),A
70FD: C9         RET
70FE: CD EA 70   CALL       $70EA
7101: 3E 10      LD           A,$10
7103: EA 02 D2   LD           ($D202),A
7106: F0 E7      LD           A,($E7)
7108: E6 10      AND         $10
710A: EA 03 D2   LD           ($D203),A
710D: CD 87 08   CALL       $0887
7110: C0         RET         NZ
7111: FA 73 DB   LD           A,($DB73)
7114: A7         AND         A
7115: 20 06      JR           NZ,$711D
7117: F0 CB      LD           A,($CB)
7119: E6 10      AND         $10
711B: 28 06      JR           Z,$7123
711D: CD 9F 70   CALL       $709F
7120: CD 8D 3B   CALL       $3B8D
7123: C9         RET
7124: CD EA 70   CALL       $70EA
7127: 3E 10      LD           A,$10
7129: EA 02 D2   LD           ($D202),A
712C: F0 E7      LD           A,($E7)
712E: E6 10      AND         $10
7130: EA 03 D2   LD           ($D203),A
7133: FA 73 DB   LD           A,($DB73)
7136: A7         AND         A
7137: 28 02      JR           Z,$713B
7139: 18 06      JR           $7141
713B: F0 CB      LD           A,($CB)
713D: E6 10      AND         $10
713F: 28 11      JR           Z,$7152
7141: F0 E7      LD           A,($E7)
7143: E6 03      AND         $03
7145: 20 1B      JR           NZ,$7162
7147: FA 05 D2   LD           A,($D205)
714A: 3C         INC         A
714B: EA 05 D2   LD           ($D205),A
714E: FE 55      CP           $55
7150: 38 10      JR           C,$7162
7152: CD 8D 3B   CALL       $3B8D
7155: CD E5 70   CALL       $70E5
7158: CD 91 08   CALL       $0891
715B: 36 60      LD           (HL),$60
715D: 1E 00      LD           E,$00
715F: CD 9F 71   CALL       $719F
7162: C9         RET
7163: F0 E7      LD           A,($E7)
7165: 1F         RRA
7166: 1F         RRA
7167: 1F         RRA
7168: E6 01      AND         $01
716A: EA 00 D2   LD           ($D200),A
716D: 3E 10      LD           A,$10
716F: EA 02 D2   LD           ($D202),A
7172: EA 03 D2   LD           ($D203),A
7175: CD 91 08   CALL       $0891
7178: FE 30      CP           $30
717A: 30 05      JR           NC,$7181
717C: 21 01 D2   LD           HL,$D201
717F: 36 02      LD           (HL),$02
7181: A7         AND         A
7182: 20 28      JR           NZ,$71AC
7184: F0 E7      LD           A,($E7)
7186: E6 03      AND         $03
7188: 20 22      JR           NZ,$71AC
718A: FA 06 D2   LD           A,($D206)
718D: 3C         INC         A
718E: EA 06 D2   LD           ($D206),A
7191: FE 0F      CP           $0F
7193: 20 17      JR           NZ,$71AC
7195: CD 91 08   CALL       $0891
7198: 36 FF      LD           (HL),$FF
719A: CD 8D 3B   CALL       $3B8D
719D: 1E 00      LD           E,$00
719F: FA 73 DB   LD           A,($DB73)
71A2: A7         AND         A
71A3: C8         RET         Z
71A4: 7B         LD           A,E
71A5: E0 9E      LDFF00   ($9E),A
71A7: C5         PUSH       BC
71A8: CD 7C 08   CALL       $087C
71AB: C1         POP         BC
71AC: C9         RET
71AD: F0 E7      LD           A,($E7)
71AF: 1F         RRA
71B0: 1F         RRA
71B1: 1F         RRA
71B2: E6 01      AND         $01
71B4: EA 00 D2   LD           ($D200),A
71B7: CD 91 08   CALL       $0891
71BA: FE C8      CP           $C8
71BC: 20 05      JR           NZ,$71C3
71BE: 21 06 D2   LD           HL,$D206
71C1: 36 10      LD           (HL),$10
71C3: FE A0      CP           $A0
71C5: 20 05      JR           NZ,$71CC
71C7: 21 01 D2   LD           HL,$D201
71CA: 36 03      LD           (HL),$03
71CC: FE 50      CP           $50
71CE: 20 09      JR           NZ,$71D9
71D0: 21 01 D2   LD           HL,$D201
71D3: 36 04      LD           (HL),$04
71D5: CD A2 72   CALL       $72A2
71D8: C9         RET
71D9: A7         AND         A
71DA: 20 06      JR           NZ,$71E2
71DC: CD 8D 3B   CALL       $3B8D
71DF: CD 9F 70   CALL       $709F
71E2: C9         RET
71E3: F0 E7      LD           A,($E7)
71E5: 1F         RRA
71E6: 1F         RRA
71E7: 1F         RRA
71E8: E6 01      AND         $01
71EA: EA 00 D2   LD           ($D200),A
71ED: F0 E7      LD           A,($E7)
71EF: E6 03      AND         $03
71F1: 20 0C      JR           NZ,$71FF
71F3: FA 06 D2   LD           A,($D206)
71F6: 3D         DEC         A
71F7: EA 06 D2   LD           ($D206),A
71FA: 20 03      JR           NZ,$71FF
71FC: CD 8D 3B   CALL       $3B8D
71FF: C9         RET
7200: F0 E7      LD           A,($E7)
7202: 1F         RRA
7203: 1F         RRA
7204: 1F         RRA
7205: E6 01      AND         $01
7207: EA 00 D2   LD           ($D200),A
720A: F0 98      LD           A,($98)
720C: F5         PUSH       AF
720D: F0 99      LD           A,($99)
720F: F5         PUSH       AF
7210: 3E 16      LD           A,$16
7212: E0 99      LDFF00   ($99),A
7214: 3E 18      LD           A,$18
7216: E0 98      LDFF00   ($98),A
7218: FA 04 D2   LD           A,($D204)
721B: EA 01 C2   LD           ($C201),A
721E: FA 05 D2   LD           A,($D205)
7221: EA 11 C2   LD           ($C211),A
7224: C5         PUSH       BC
7225: 0E 01      LD           C,$01
7227: 3E 04      LD           A,$04
7229: CD 25 3C   CALL       $3C25
722C: CD 94 6D   CALL       $6D94
722F: FA 01 C2   LD           A,($C201)
7232: EA 04 D2   LD           ($D204),A
7235: FA 11 C2   LD           A,($C211)
7238: EA 05 D2   LD           ($D205),A
723B: C1         POP         BC
723C: F1         POP         AF
723D: E0 99      LDFF00   ($99),A
723F: F1         POP         AF
7240: E0 98      LDFF00   ($98),A
7242: FA 04 D2   LD           A,($D204)
7245: FE 18      CP           $18
7247: 20 12      JR           NZ,$725B
7249: FA 05 D2   LD           A,($D205)
724C: FE 16      CP           $16
724E: 20 0B      JR           NZ,$725B
7250: CD 91 08   CALL       $0891
7253: 36 C0      LD           (HL),$C0
7255: CD 8D 3B   CALL       $3B8D
7258: CD E5 70   CALL       $70E5
725B: C9         RET
725C: F0 E7      LD           A,($E7)
725E: 1F         RRA
725F: 1F         RRA
7260: 1F         RRA
7261: E6 01      AND         $01
7263: EA 00 D2   LD           ($D200),A
7266: CD 91 08   CALL       $0891
7269: FE 60      CP           $60
726B: 20 25      JR           NZ,$7292
726D: 21 01 D2   LD           HL,$D201
7270: 36 02      LD           (HL),$02
7272: 21 C0 C2   LD           HL,$C2C0
7275: 09         ADD         HL,BC
7276: 7E         LD           A,(HL)
7277: A7         AND         A
7278: 28 17      JR           Z,$7291
727A: 36 00      LD           (HL),$00
727C: 3D         DEC         A
727D: 5F         LD           E,A
727E: 50         LD           D,B
727F: 21 90 C2   LD           HL,$C290
7282: 19         ADD         HL,DE
7283: 36 02      LD           (HL),$02
7285: FA 73 DB   LD           A,($DB73)
7288: A7         AND         A
7289: 28 06      JR           Z,$7291
728B: 21 B0 C3   LD           HL,$C3B0
728E: 19         ADD         HL,DE
728F: 36 07      LD           (HL),$07
7291: C9         RET
7292: A7         AND         A
7293: 20 08      JR           NZ,$729D
7295: 21 01 D2   LD           HL,$D201
7298: 36 04      LD           (HL),$04
729A: CD 8D 3B   CALL       $3B8D
729D: C9         RET
729E: CD FC 6F   CALL       $6FFC
72A1: C9         RET
72A2: FA 73 DB   LD           A,($DB73)
72A5: A7         AND         A
72A6: 28 27      JR           Z,$72CF
72A8: 3E FF      LD           A,$FF
72AA: CD 87 3B   CALL       $3B87
72AD: 3E 4F      LD           A,$4F
72AF: CD 01 3C   CALL       $3C01
72B2: FA 04 D2   LD           A,($D204)
72B5: 21 00 C2   LD           HL,$C200
72B8: 19         ADD         HL,DE
72B9: 77         LD           (HL),A
72BA: FA 05 D2   LD           A,($D205)
72BD: C6 18      ADD         $18
72BF: 21 10 C2   LD           HL,$C210
72C2: 19         ADD         HL,DE
72C3: 77         LD           (HL),A
72C4: 21 B0 C3   LD           HL,$C3B0
72C7: 19         ADD         HL,DE
72C8: 36 06      LD           (HL),$06
72CA: 21 B0 C2   LD           HL,$C2B0
72CD: 19         ADD         HL,DE
72CE: 34         INC         (HL)
72CF: 1E 0F      LD           E,$0F
72D1: 50         LD           D,B
72D2: 21 80 C2   LD           HL,$C280
72D5: 19         ADD         HL,DE
72D6: 7E         LD           A,(HL)
72D7: A7         AND         A
72D8: 28 46      JR           Z,$7320
72DA: 21 90 C2   LD           HL,$C290
72DD: 19         ADD         HL,DE
72DE: 7E         LD           A,(HL)
72DF: A7         AND         A
72E0: 20 3E      JR           NZ,$7320
72E2: 21 A0 C3   LD           HL,$C3A0
72E5: 19         ADD         HL,DE
72E6: 7E         LD           A,(HL)
72E7: FE 4F      CP           $4F
72E9: 20 35      JR           NZ,$7320
72EB: 21 00 C2   LD           HL,$C200
72EE: 19         ADD         HL,DE
72EF: FA 04 D2   LD           A,($D204)
72F2: 96         SUB         (HL)
72F3: C6 04      ADD         $04
72F5: FE 08      CP           $08
72F7: 30 27      JR           NC,$7320
72F9: 21 10 C2   LD           HL,$C210
72FC: 19         ADD         HL,DE
72FD: FA 05 D2   LD           A,($D205)
7300: C6 18      ADD         $18
7302: 96         SUB         (HL)
7303: C6 06      ADD         $06
7305: FE 0C      CP           $0C
7307: 30 17      JR           NC,$7320
7309: 21 90 C2   LD           HL,$C290
730C: 19         ADD         HL,DE
730D: 36 01      LD           (HL),$01
730F: 7B         LD           A,E
7310: 3C         INC         A
7311: 21 C0 C2   LD           HL,$C2C0
7314: 09         ADD         HL,BC
7315: 77         LD           (HL),A
7316: CD 8C 08   CALL       $088C
7319: 36 10      LD           (HL),$10
731B: 21 40 C4   LD           HL,$C440
731E: 34         INC         (HL)
731F: C9         RET
7320: 1D         DEC         E
7321: 7B         LD           A,E
7322: FE FF      CP           $FF
7324: 20 AC      JR           NZ,$72D2
7326: C9         RET
7327: 21 C0 C2   LD           HL,$C2C0
732A: 09         ADD         HL,BC
732B: 7E         LD           A,(HL)
732C: A7         AND         A
732D: 28 22      JR           Z,$7351
732F: 3D         DEC         A
7330: 5F         LD           E,A
7331: 50         LD           D,B
7332: FA 04 D2   LD           A,($D204)
7335: 21 00 C2   LD           HL,$C200
7338: 19         ADD         HL,DE
7339: 77         LD           (HL),A
733A: FA 05 D2   LD           A,($D205)
733D: C6 18      ADD         $18
733F: 21 10 C2   LD           HL,$C210
7342: 19         ADD         HL,DE
7343: 77         LD           (HL),A
7344: 3E 10      LD           A,$10
7346: 21 06 D2   LD           HL,$D206
7349: 96         SUB         (HL)
734A: C6 FE      ADD         $FE
734C: 21 10 C3   LD           HL,$C310
734F: 19         ADD         HL,DE
7350: 77         LD           (HL),A
7351: C9         RET
7352: 76         HALT
7353: 00         NOP
7354: 78         LD           A,B
7355: 00         NOP
7356: 78         LD           A,B
7357: 20 76      JR           NZ,$73CF
7359: 20 70      JR           NZ,$73CB
735B: 00         NOP
735C: 70         LD           (HL),B
735D: 20 72      JR           NZ,$73D1
735F: 00         NOP
7360: 70         LD           (HL),B
7361: 20 72      JR           NZ,$73D5
7363: 00         NOP
7364: 72         LD           (HL),D
7365: 20 7E      JR           NZ,$73E5
7367: 00         NOP
7368: 7E         LD           A,(HL)
7369: 20 26      JR           NZ,$7391
736B: 00         NOP
736C: 26 00      LD           H,$00
736E: FA 04 D2   LD           A,($D204)
7371: E0 EE      LDFF00   ($EE),A
7373: FA 05 D2   LD           A,($D205)
7376: 21 06 D2   LD           HL,$D206
7379: 86         ADD         A,(HL)
737A: C6 08      ADD         $08
737C: E0 EC      LDFF00   ($EC),A
737E: FA 01 D2   LD           A,($D201)
7381: E0 F1      LDFF00   ($F1),A
7383: 11 52 73   LD           DE,$7352
7386: CD 3B 3C   CALL       $3C3B
7389: FA 04 D2   LD           A,($D204)
738C: E0 EE      LDFF00   ($EE),A
738E: FA 05 D2   LD           A,($D205)
7391: E0 EC      LDFF00   ($EC),A
7393: FA 00 D2   LD           A,($D200)
7396: E0 F1      LDFF00   ($F1),A
7398: 11 52 73   LD           DE,$7352
739B: CD 3B 3C   CALL       $3C3B
739E: FA 06 D2   LD           A,($D206)
73A1: FE 08      CP           $08
73A3: 38 16      JR           C,$73BB
73A5: FA 04 D2   LD           A,($D204)
73A8: E0 EE      LDFF00   ($EE),A
73AA: FA 05 D2   LD           A,($D205)
73AD: C6 10      ADD         $10
73AF: E0 EC      LDFF00   ($EC),A
73B1: 3E 05      LD           A,$05
73B3: E0 F1      LDFF00   ($F1),A
73B5: 11 52 73   LD           DE,$7352
73B8: CD 3B 3C   CALL       $3C3B
73BB: F0 E7      LD           A,($E7)
73BD: E6 01      AND         $01
73BF: 20 26      JR           NZ,$73E7
73C1: FA 04 D2   LD           A,($D204)
73C4: E0 EE      LDFF00   ($EE),A
73C6: FA 05 D2   LD           A,($D205)
73C9: C6 20      ADD         $20
73CB: E0 EC      LDFF00   ($EC),A
73CD: AF         XOR         A
73CE: E0 F1      LDFF00   ($F1),A
73D0: 11 6A 73   LD           DE,$736A
73D3: FA C0 C3   LD           A,($C3C0)
73D6: F5         PUSH       AF
73D7: CD 3B 3C   CALL       $3C3B
73DA: F1         POP         AF
73DB: 5F         LD           E,A
73DC: 50         LD           D,B
73DD: 21 31 C0   LD           HL,$C031
73E0: 19         ADD         HL,DE
73E1: 34         INC         (HL)
73E2: 23         INC         HL
73E3: 23         INC         HL
73E4: 23         INC         HL
73E5: 23         INC         HL
73E6: 35         DEC         (HL)
73E7: 21 20 C0   LD           HL,$C020
73EA: 3E 50      LD           A,$50
73EC: 22         LD           (HLI),A
73ED: 3E 28      LD           A,$28
73EF: 22         LD           (HLI),A
73F0: 3E 7A      LD           A,$7A
73F2: 22         LD           (HLI),A
73F3: FA 02 D2   LD           A,($D202)
73F6: 22         LD           (HLI),A
73F7: 3E 60      LD           A,$60
73F9: 22         LD           (HLI),A
73FA: 3E 28      LD           A,$28
73FC: 22         LD           (HLI),A
73FD: 3E 3E      LD           A,$3E
73FF: 22         LD           (HLI),A
7400: FA 02 D2   LD           A,($D202)
7403: 22         LD           (HLI),A
7404: 3E 50      LD           A,$50
7406: 22         LD           (HLI),A
7407: 3E 30      LD           A,$30
7409: 22         LD           (HLI),A
740A: 3E 7C      LD           A,$7C
740C: 22         LD           (HLI),A
740D: FA 03 D2   LD           A,($D203)
7410: 22         LD           (HLI),A
7411: 3E 60      LD           A,$60
7413: 22         LD           (HLI),A
7414: 3E 30      LD           A,$30
7416: 22         LD           (HLI),A
7417: 3E 3E      LD           A,$3E
7419: 22         LD           (HLI),A
741A: FA 03 D2   LD           A,($D203)
741D: 22         LD           (HLI),A
741E: C9         RET
741F: FF         RST         0X38
7420: FF         RST         0X38
7421: 9E         SBC         (HL)
7422: 10 A6      STOP       $A6
7424: 10 8E      STOP       $8E
7426: 10 86      STOP       $86
7428: 10 A8      STOP       $A8
742A: 10 9A      STOP       $9A
742C: 10 9C      STOP       $9C
742E: 10 6C      STOP       $6C
7430: 00         NOP
7431: 6E         LD           L,(HL)
7432: 00         NOP
7433: 6E         LD           L,(HL)
7434: 20 6C      JR           NZ,$74A2
7436: 20 F0      JR           NZ,$7428
7438: F1         POP         AF
7439: FE 06      CP           $06
743B: 38 12      JR           C,$744F
743D: 11 17 74   LD           DE,$7417
7440: FE 07      CP           $07
7442: 28 09      JR           Z,$744D
7444: F0 E7      LD           A,($E7)
7446: E6 10      AND         $10
7448: 20 03      JR           NZ,$744D
744A: 11 1B 74   LD           DE,$741B
744D: 18 1B      JR           $746A
744F: FE 03      CP           $03
7451: 20 09      JR           NZ,$745C
7453: FA 4B DB   LD           A,($DB4B)
7456: A7         AND         A
7457: C2 44 6D   JP           NZ,$6D44
745A: 18 13      JR           $746F
745C: FE 00      CP           $00
745E: 20 0F      JR           NZ,$746F
7460: FA 0E DB   LD           A,($DB0E)
7463: A7         AND         A
7464: C2 44 6D   JP           NZ,$6D44
7467: 11 2B 74   LD           DE,$742B
746A: CD 3B 3C   CALL       $3C3B
746D: 18 06      JR           $7475
746F: 11 1F 74   LD           DE,$741F
7472: CD D0 3C   CALL       $3CD0
7475: CD 1F 7F   CALL       $7F1F
7478: F0 F0      LD           A,($F0)
747A: C7         RST         0X00
747B: 87         ADD         A,A
747C: 74         LD           (HL),H
747D: BA         CP           D
747E: 74         LD           (HL),H
747F: C5         PUSH       BC
7480: 74         LD           (HL),H
7481: 1C         INC         E
7482: 75         LD           (HL),L
7483: E2         LDFF00   (C),A
7484: 75         LD           (HL),L
7485: F9         LD           SP,HL
7486: 75         LD           (HL),L
7487: CD 94 6D   CALL       $6D94
748A: 21 80 C3   LD           HL,$C380
748D: 09         ADD         HL,BC
748E: 7E         LD           A,(HL)
748F: C7         RST         0X00
7490: 9A         SBC         D
7491: 74         LD           (HL),H
7492: A2         AND         D
7493: 74         LD           (HL),H
7494: AA         XOR         D
7495: 74         LD           (HL),H
7496: B2         OR           D
7497: 74         LD           (HL),H
7498: A1         AND         C
7499: 74         LD           (HL),H
749A: F0 EE      LD           A,($EE)
749C: FE 3A      CP           $3A
749E: DA 0B 76   JP           C,$760B
74A1: C9         RET
74A2: F0 EC      LD           A,($EC)
74A4: FE 4E      CP           $4E
74A6: D2 0B 76   JP           NC,$760B
74A9: C9         RET
74AA: F0 EE      LD           A,($EE)
74AC: FE 78      CP           $78
74AE: D2 0B 76   JP           NC,$760B
74B1: C9         RET
74B2: F0 EC      LD           A,($EC)
74B4: FE 2E      CP           $2E
74B6: DA 0B 76   JP           C,$760B
74B9: C9         RET
74BA: CD 1F 6E   CALL       $6E1F
74BD: 7B         LD           A,E
74BE: EE 01      XOR         $01
74C0: 5F         LD           E,A
74C1: CD 9F 71   CALL       $719F
74C4: C9         RET
74C5: FA 73 DB   LD           A,($DB73)
74C8: A7         AND         A
74C9: 28 04      JR           Z,$74CF
74CB: 3E 02      LD           A,$02
74CD: E0 A1      LDFF00   ($A1),A
74CF: CD CD 6D   CALL       $6DCD
74D2: 21 20 C3   LD           HL,$C320
74D5: 09         ADD         HL,BC
74D6: 35         DEC         (HL)
74D7: 35         DEC         (HL)
74D8: 21 10 C3   LD           HL,$C310
74DB: 09         ADD         HL,BC
74DC: 7E         LD           A,(HL)
74DD: E6 80      AND         $80
74DF: 28 16      JR           Z,$74F7
74E1: AF         XOR         A
74E2: 77         LD           (HL),A
74E3: 21 20 C3   LD           HL,$C320
74E6: 09         ADD         HL,BC
74E7: 7E         LD           A,(HL)
74E8: CB 2F      SRA         1,E
74EA: 2F         CPL
74EB: 77         LD           (HL),A
74EC: FE 07      CP           $07
74EE: 30 03      JR           NC,$74F3
74F0: 70         LD           (HL),B
74F1: 18 04      JR           $74F7
74F3: 3E 09      LD           A,$09
74F5: E0 F2      LDFF00   ($F2),A
74F7: F0 E7      LD           A,($E7)
74F9: E6 03      AND         $03
74FB: 20 0B      JR           NZ,$7508
74FD: 21 10 C2   LD           HL,$C210
7500: 09         ADD         HL,BC
7501: 7E         LD           A,(HL)
7502: FE 56      CP           $56
7504: 28 03      JR           Z,$7509
7506: 3C         INC         A
7507: 77         LD           (HL),A
7508: C9         RET
7509: C6 0A      ADD         $0A
750B: 77         LD           (HL),A
750C: 21 10 C3   LD           HL,$C310
750F: 09         ADD         HL,BC
7510: 36 0A      LD           (HL),$0A
7512: CD 8D 3B   CALL       $3B8D
7515: C9         RET
7516: 44         LD           B,H
7517: 43         LD           B,E
7518: 42         LD           B,D
7519: 41         LD           B,C
751A: 3D         DEC         A
751B: 2A         LD           A,(HLI)
751C: FA 73 DB   LD           A,($DB73)
751F: A7         AND         A
7520: 28 04      JR           Z,$7526
7522: 3E 02      LD           A,$02
7524: E0 A1      LDFF00   ($A1),A
7526: CD CD 6D   CALL       $6DCD
7529: 21 20 C3   LD           HL,$C320
752C: 09         ADD         HL,BC
752D: 35         DEC         (HL)
752E: 35         DEC         (HL)
752F: 21 10 C3   LD           HL,$C310
7532: 09         ADD         HL,BC
7533: 7E         LD           A,(HL)
7534: E6 80      AND         $80
7536: CA E1 75   JP           Z,$75E1
7539: AF         XOR         A
753A: 77         LD           (HL),A
753B: 21 20 C3   LD           HL,$C320
753E: 09         ADD         HL,BC
753F: 7E         LD           A,(HL)
7540: CB 2F      SRA         1,E
7542: 2F         CPL
7543: 77         LD           (HL),A
7544: FE 07      CP           $07
7546: 30 02      JR           NC,$754A
7548: AF         XOR         A
7549: 77         LD           (HL),A
754A: F0 F1      LD           A,($F1)
754C: FE 06      CP           $06
754E: 38 08      JR           C,$7558
7550: 3E F9      LD           A,$F9
7552: CD 97 21   CALL       $2197
7555: C3 8D 3B   JP           $3B8D
7558: F0 EE      LD           A,($EE)
755A: 21 98 FF   LD           HL,$FF98
755D: 96         SUB         (HL)
755E: C6 07      ADD         $07
7560: FE 0E      CP           $0E
7562: D0         RET         NC
7563: F0 EC      LD           A,($EC)
7565: 21 99 FF   LD           HL,$FF99
7568: 96         SUB         (HL)
7569: C6 05      ADD         $05
756B: FE 0A      CP           $0A
756D: D0         RET         NC
756E: FA 10 D2   LD           A,($D210)
7571: 5F         LD           E,A
7572: 50         LD           D,B
7573: 21 80 C4   LD           HL,$C480
7576: 19         ADD         HL,DE
7577: 7E         LD           A,(HL)
7578: A7         AND         A
7579: C0         RET         NZ
757A: 36 18      LD           (HL),$18
757C: F0 F1      LD           A,($F1)
757E: FE 00      CP           $00
7580: 20 0B      JR           NZ,$758D
7582: 3E 01      LD           A,$01
7584: EA 0E DB   LD           ($DB0E),A
7587: CD 98 08   CALL       $0898
758A: C3 44 6D   JP           $6D44
758D: CD 44 6D   CALL       $6D44
7590: 21 F3 FF   LD           HL,$FFF3
7593: 36 01      LD           (HL),$01
7595: F0 F1      LD           A,($F1)
7597: 5F         LD           E,A
7598: 50         LD           D,B
7599: 21 16 75   LD           HL,$7516
759C: 19         ADD         HL,DE
759D: 7E         LD           A,(HL)
759E: CD 97 21   CALL       $2197
75A1: F0 F1      LD           A,($F1)
75A3: 3D         DEC         A
75A4: 20 01      JR           NZ,$75A7
75A6: C9         RET
75A7: 3D         DEC         A
75A8: 20 09      JR           NZ,$75B3
75AA: FA 90 DB   LD           A,($DB90)
75AD: C6 1E      ADD         $1E
75AF: EA 90 DB   LD           ($DB90),A
75B2: C9         RET
75B3: 3D         DEC         A
75B4: 20 1D      JR           NZ,$75D3
75B6: 21 76 DB   LD           HL,$DB76
75B9: FA 4C DB   LD           A,($DB4C)
75BC: BE         CP           (HL)
75BD: 30 07      JR           NC,$75C6
75BF: C6 10      ADD         $10
75C1: 27         DAA
75C2: BE         CP           (HL)
75C3: 38 01      JR           C,$75C6
75C5: 7E         LD           A,(HL)
75C6: EA 4C DB   LD           ($DB4C),A
75C9: 16 0C      LD           D,$0C
75CB: CD 95 3E   CALL       $3E95
75CE: 3E 0B      LD           A,$0B
75D0: E0 A5      LDFF00   ($A5),A
75D2: C9         RET
75D3: 3D         DEC         A
75D4: 20 06      JR           NZ,$75DC
75D6: 16 04      LD           D,$04
75D8: CD 95 3E   CALL       $3E95
75DB: C9         RET
75DC: 3E FF      LD           A,$FF
75DE: EA 93 DB   LD           ($DB93),A
75E1: C9         RET
75E2: 3E 02      LD           A,$02
75E4: E0 A1      LDFF00   ($A1),A
75E6: EA 67 C1   LD           ($C167),A
75E9: FA AD C1   LD           A,($C1AD)
75EC: A7         AND         A
75ED: C0         RET         NZ
75EE: EA 74 DB   LD           ($DB74),A
75F1: 3E 18      LD           A,$18
75F3: EA BC C1   LD           ($C1BC),A
75F6: C3 8D 3B   JP           $3B8D
75F9: 3E 02      LD           A,$02
75FB: E0 A1      LDFF00   ($A1),A
75FD: EA 67 C1   LD           ($C167),A
7600: C9         RET
7601: FC                              
7602: 00         NOP
7603: 04         INC         B
7604: 00         NOP
7605: 00         NOP
7606: 00         NOP
7607: 04         INC         B
7608: 00         NOP
7609: FC                              
760A: 00         NOP
760B: 21 80 C3   LD           HL,$C380
760E: 09         ADD         HL,BC
760F: 7E         LD           A,(HL)
7610: 3C         INC         A
7611: E6 03      AND         $03
7613: 77         LD           (HL),A
7614: 5F         LD           E,A
7615: 50         LD           D,B
7616: 21 01 76   LD           HL,$7601
7619: 19         ADD         HL,DE
761A: 7E         LD           A,(HL)
761B: 21 40 C2   LD           HL,$C240
761E: 09         ADD         HL,BC
761F: 77         LD           (HL),A
7620: 21 06 76   LD           HL,$7606
7623: 19         ADD         HL,DE
7624: 7E         LD           A,(HL)
7625: 21 50 C2   LD           HL,$C250
7628: 09         ADD         HL,BC
7629: 77         LD           (HL),A
762A: C9         RET
762B: F0 E7      LD           A,($E7)
762D: E6 1F      AND         $1F
762F: 20 09      JR           NZ,$763A
7631: CD 1F 6E   CALL       $6E1F
7634: 7B         LD           A,E
7635: 21 80 C3   LD           HL,$C380
7638: 09         ADD         HL,BC
7639: 77         LD           (HL),A
763A: CD 09 7C   CALL       $7C09
763D: 11 59 76   LD           DE,$7659
7640: CD 3B 3C   CALL       $3C3B
7643: CD 54 7B   CALL       $7B54
7646: CD BC 7B   CALL       $7BBC
7649: 30 0D      JR           NC,$7658
764B: FA 7F D4   LD           A,($D47F)
764E: FE 03      CP           $03
7650: 3E 39      LD           A,$39
7652: 38 01      JR           C,$7655
7654: 3C         INC         A
7655: CD 97 21   CALL       $2197
7658: C9         RET
7659: 60         LD           H,B
765A: 00         NOP
765B: 62         LD           H,D
765C: 00         NOP
765D: 62         LD           H,D
765E: 20 60      JR           NZ,$76C0
7660: 20 64      JR           NZ,$76C6
7662: 00         NOP
7663: 66         LD           H,(HL)
7664: 00         NOP
7665: 66         LD           H,(HL)
7666: 20 64      JR           NZ,$76CC
7668: 20 68      JR           NZ,$76D2
766A: 00         NOP
766B: 6A         LD           L,D
766C: 00         NOP
766D: 6C         LD           L,H
766E: 00         NOP
766F: 6E         LD           L,(HL)
7670: 00         NOP
7671: 6A         LD           L,D
7672: 20 68      JR           NZ,$76DC
7674: 20 6E      JR           NZ,$76E4
7676: 20 6C      JR           NZ,$76E4
7678: 20 FA      JR           NZ,$7674
767A: 0A         LD           A,(BC)
767B: C5         PUSH       BC
767C: A7         AND         A
767D: 20 08      JR           NZ,$7687
767F: 3E 01      LD           A,$01
7681: EA 0A C5   LD           ($C50A),A
7684: CD 0F 78   CALL       $780F
7687: FA 4E DB   LD           A,($DB4E)
768A: A7         AND         A
768B: 28 06      JR           Z,$7693
768D: F0 E7      LD           A,($E7)
768F: E6 5F      AND         $5F
7691: 20 09      JR           NZ,$769C
7693: CD 1F 6E   CALL       $6E1F
7696: 7B         LD           A,E
7697: 21 80 C3   LD           HL,$C380
769A: 09         ADD         HL,BC
769B: 77         LD           (HL),A
769C: CD 09 7C   CALL       $7C09
769F: 11 59 76   LD           DE,$7659
76A2: CD 3B 3C   CALL       $3C3B
76A5: CD DE 7A   CALL       $7ADE
76A8: F0 F0      LD           A,($F0)
76AA: FE 04      CP           $04
76AC: 30 03      JR           NC,$76B1
76AE: CD 54 7B   CALL       $7B54
76B1: F0 F0      LD           A,($F0)
76B3: C7         RST         0X00
76B4: 86         ADD         A,(HL)
76B5: 77         LD           (HL),A
76B6: 30 78      JR           NC,$7730
76B8: E1         POP         HL
76B9: 78         LD           A,B
76BA: 66         LD           H,(HL)
76BB: 7A         LD           A,D
76BC: 70         LD           (HL),B
76BD: 7A         LD           A,D
76BE: AB         XOR         E
76BF: 7A         LD           A,D
76C0: 98         SBC         B
76C1: 63         LD           H,E
76C2: 02         LD           (BC),A
76C3: B2         OR           D
76C4: B0         OR           B
76C5: B0         OR           B
76C6: 98         SBC         B
76C7: A4         AND         H
76C8: 01 7F 7F   LD           BC,$7F7F
76CB: 98         SBC         B
76CC: 67         LD           H,A
76CD: 02         LD           (BC),A
76CE: B1         OR           C
76CF: B0         OR           B
76D0: 7F         LD           A,A
76D1: 98         SBC         B
76D2: A8         XOR         B
76D3: 01 0A B3   LD           BC,$B30A
76D6: 98         SBC         B
76D7: 6A         LD           L,D
76D8: 02         LD           (BC),A
76D9: 7F         LD           A,A
76DA: B2         OR           D
76DB: B0         OR           B
76DC: 98         SBC         B
76DD: AC         XOR         H
76DE: 01 BA B1   LD           BC,$B1BA
76E1: 98         SBC         B
76E2: 6E         LD           L,(HL)
76E3: 02         LD           (BC),A
76E4: B1         OR           C
76E5: B0         OR           B
76E6: 7F         LD           A,A
76E7: 98         SBC         B
76E8: B0         OR           B
76E9: 01 0A 09   LD           BC,$090A
76EC: 98         SBC         B
76ED: 63         LD           H,E
76EE: 02         LD           (BC),A
76EF: B9         CP           C
76F0: B8         CP           B
76F1: B0         OR           B
76F2: 98         SBC         B
76F3: A4         AND         H
76F4: 01 7F 7F   LD           BC,$7F7F
76F7: 98         SBC         B
76F8: 63         LD           H,E
76F9: 02         LD           (BC),A
76FA: B1         OR           C
76FB: B0         OR           B
76FC: 7F         LD           A,A
76FD: 98         SBC         B
76FE: A4         AND         H
76FF: 01 0A 09   LD           BC,$090A
7702: 00         NOP
7703: 98         SBC         B
7704: 62         LD           H,D
7705: 43         LD           B,E
7706: 7F         LD           A,A
7707: 98         SBC         B
7708: 83         ADD         A,E
7709: 42         LD           B,D
770A: 7F         LD           A,A
770B: 98         SBC         B
770C: A3         AND         E
770D: 42         LD           B,D
770E: 7F         LD           A,A
770F: 00         NOP
7710: 00         NOP
7711: 00         NOP
7712: 00         NOP
7713: 98         SBC         B
7714: 66         LD           H,(HL)
7715: 43         LD           B,E
7716: 7F         LD           A,A
7717: 98         SBC         B
7718: 87         ADD         A,A
7719: 42         LD           B,D
771A: 7F         LD           A,A
771B: 98         SBC         B
771C: A7         AND         A
771D: 42         LD           B,D
771E: 7F         LD           A,A
771F: 00         NOP
7720: 00         NOP
7721: 00         NOP
7722: 00         NOP
7723: 98         SBC         B
7724: 6A         LD           L,D
7725: 43         LD           B,E
7726: 7F         LD           A,A
7727: 98         SBC         B
7728: 8B         ADC         A,E
7729: 42         LD           B,D
772A: 7F         LD           A,A
772B: 98         SBC         B
772C: AB         XOR         E
772D: 42         LD           B,D
772E: 7F         LD           A,A
772F: 00         NOP
7730: 00         NOP
7731: 00         NOP
7732: 00         NOP
7733: 98         SBC         B
7734: 6E         LD           L,(HL)
7735: 43         LD           B,E
7736: 7F         LD           A,A
7737: 98         SBC         B
7738: 8F         ADC         A,A
7739: 42         LD           B,D
773A: 7F         LD           A,A
773B: 98         SBC         B
773C: AF         XOR         A
773D: 42         LD           B,D
773E: 7F         LD           A,A
773F: 00         NOP
7740: 00         NOP
7741: 00         NOP
7742: 00         NOP
7743: 01 02 03   LD           BC,$0302
7746: 00         NOP
7747: 01 02 03   LD           BC,$0302
774A: 04         INC         B
774B: 05         DEC         B
774C: 02         LD           (BC),A
774D: 03         INC         BC
774E: 04         INC         B
774F: 06 02      LD           B,$02
7751: 03         INC         BC
7752: 04         INC         B
7753: 07         RLCA
7754: 08 09 0A   LD           ($0A09),SP
7757: 30 31      JR           NC,$778A
7759: 32         LD           (HLD),A
775A: 33         INC         SP
775B: 2C         INC         L
775C: 2D         DEC         L
775D: 39         ADD         HL,SP
775E: 00         NOP
775F: 00         NOP
7760: 00         NOP
7761: 00         NOP
7762: 02         LD           (BC),A
7763: 00         NOP
7764: 00         NOP
7765: 00         NOP
7766: 09         ADD         HL,BC
7767: 00         NOP
7768: 00         NOP
7769: 00         NOP
776A: 00         NOP
776B: 00         NOP
776C: 10 20      STOP       $20
776E: 10 80      STOP       $80
7770: 10 00      STOP       $00
7772: 00         NOP
7773: 00         NOP
7774: 00         NOP
7775: 00         NOP
7776: 00         NOP
7777: 00         NOP
7778: 03         INC         BC
7779: 00         NOP
777A: 00         NOP
777B: 00         NOP
777C: 00         NOP
777D: C8         RET         Z
777E: 0A         LD           A,(BC)
777F: 14         INC         D
7780: 0A         LD           A,(BC)
7781: D4 0A 00   CALL       NC,$000A
7784: 00         NOP
7785: 00         NOP
7786: FA 46 DB   LD           A,($DB46)
7789: A7         AND         A
778A: 28 3B      JR           Z,$77C7
778C: 21 10 C2   LD           HL,$C210
778F: 09         ADD         HL,BC
7790: 36 40      LD           (HL),$40
7792: 21 00 C2   LD           HL,$C200
7795: 09         ADD         HL,BC
7796: 36 50      LD           (HL),$50
7798: 21 80 C3   LD           HL,$C380
779B: 09         ADD         HL,BC
779C: 36 03      LD           (HL),$03
779E: 3E 02      LD           A,$02
77A0: E0 A1      LDFF00   ($A1),A
77A2: EA 67 C1   LD           ($C167),A
77A5: FA 6B C1   LD           A,($C16B)
77A8: FE 04      CP           $04
77AA: 20 1A      JR           NZ,$77C6
77AC: F0 99      LD           A,($99)
77AE: D6 01      SUB         $01
77B0: E0 99      LDFF00   ($99),A
77B2: FE 74      CP           $74
77B4: 20 10      JR           NZ,$77C6
77B6: 3E 38      LD           A,$38
77B8: CD 97 21   CALL       $2197
77BB: 21 90 C2   LD           HL,$C290
77BE: 09         ADD         HL,BC
77BF: 36 04      LD           (HL),$04
77C1: 3E 19      LD           A,$19
77C3: EA 68 D3   LD           ($D368),A
77C6: C9         RET
77C7: 1E 00      LD           E,$00
77C9: 50         LD           D,B
77CA: FA 66 DB   LD           A,($DB66)
77CD: E6 02      AND         $02
77CF: 28 02      JR           Z,$77D3
77D1: 1E 04      LD           E,$04
77D3: C5         PUSH       BC
77D4: 21 00 DB   LD           HL,$DB00
77D7: 0E 0B      LD           C,$0B
77D9: 2A         LD           A,(HLI)
77DA: FE 0B      CP           $0B
77DC: 20 02      JR           NZ,$77E0
77DE: 1E 08      LD           E,$08
77E0: 0D         DEC         C
77E1: 79         LD           A,C
77E2: FE FF      CP           $FF
77E4: 20 F3      JR           NZ,$77D9
77E6: 21 00 DB   LD           HL,$DB00
77E9: 0E 0B      LD           C,$0B
77EB: 2A         LD           A,(HLI)
77EC: FE 05      CP           $05
77EE: 20 02      JR           NZ,$77F2
77F0: 1E 0C      LD           E,$0C
77F2: 0D         DEC         C
77F3: 79         LD           A,C
77F4: FE FF      CP           $FF
77F6: 20 F3      JR           NZ,$77EB
77F8: 21 43 77   LD           HL,$7743
77FB: 19         ADD         HL,DE
77FC: 11 05 C5   LD           DE,$C505
77FF: 0E 04      LD           C,$04
7801: 2A         LD           A,(HLI)
7802: 12         LD           (DE),A
7803: 13         INC         DE
7804: 0D         DEC         C
7805: 20 FA      JR           NZ,$7801
7807: C1         POP         BC
7808: CD 8D 3B   CALL       $3B8D
780B: CD 0F 78   CALL       $780F
780E: C9         RET
780F: 11 01 D6   LD           DE,$D601
7812: C5         PUSH       BC
7813: 21 05 C5   LD           HL,$C505
7816: 0E 04      LD           C,$04
7818: 2A         LD           A,(HLI)
7819: A7         AND         A
781A: 28 05      JR           Z,$7821
781C: E5         PUSH       HL
781D: CD 0F 79   CALL       $790F
7820: E1         POP         HL
7821: 0D         DEC         C
7822: 20 F4      JR           NZ,$7818
7824: C1         POP         BC
7825: C9         RET
7826: 00         NOP
7827: 00         NOP
7828: 00         NOP
7829: 01 01 02   LD           BC,$0201
782C: 02         LD           (BC),A
782D: 03         INC         BC
782E: 03         INC         BC
782F: 03         INC         BC
7830: FA 09 C5   LD           A,($C509)
7833: A7         AND         A
7834: 28 1F      JR           Z,$7855
7836: 21 80 C3   LD           HL,$C380
7839: 09         ADD         HL,BC
783A: 7E         LD           A,(HL)
783B: E6 01      AND         $01
783D: 28 16      JR           Z,$7855
783F: FA 1C C1   LD           A,($C11C)
7842: FE 00      CP           $00
7844: 20 0F      JR           NZ,$7855
7846: F0 99      LD           A,($99)
7848: FE 7B      CP           $7B
784A: 38 09      JR           C,$7855
784C: D6 02      SUB         $02
784E: E0 99      LDFF00   ($99),A
7850: 3E 2F      LD           A,$2F
7852: C3 97 21   JP           $2197
7855: F0 99      LD           A,($99)
7857: FE 48      CP           $48
7859: 30 66      JR           NC,$78C1
785B: F0 9E      LD           A,($9E)
785D: FE 02      CP           $02
785F: 20 60      JR           NZ,$78C1
7861: F0 CC      LD           A,($CC)
7863: E6 30      AND         $30
7865: 28 5A      JR           Z,$78C1
7867: FA 09 C5   LD           A,($C509)
786A: A7         AND         A
786B: 28 1B      JR           Z,$7888
786D: F0 98      LD           A,($98)
786F: C6 00      ADD         $00
7871: CB 37      SWAP        1,E
7873: E6 0F      AND         $0F
7875: 5F         LD           E,A
7876: 50         LD           D,B
7877: 21 26 78   LD           HL,$7826
787A: 19         ADD         HL,DE
787B: FA 0B C5   LD           A,($C50B)
787E: BE         CP           (HL)
787F: 20 40      JR           NZ,$78C1
7881: 3E 13      LD           A,$13
7883: E0 F2      LDFF00   ($F2),A
7885: C3 F1 78   JP           $78F1
7888: F0 98      LD           A,($98)
788A: C6 00      ADD         $00
788C: CB 37      SWAP        1,E
788E: E6 0F      AND         $0F
7890: 5F         LD           E,A
7891: 50         LD           D,B
7892: 21 26 78   LD           HL,$7826
7895: 19         ADD         HL,DE
7896: 7E         LD           A,(HL)
7897: EA 0B C5   LD           ($C50B),A
789A: 5F         LD           E,A
789B: 50         LD           D,B
789C: 21 05 C5   LD           HL,$C505
789F: 19         ADD         HL,DE
78A0: 7E         LD           A,(HL)
78A1: EA 09 C5   LD           ($C509),A
78A4: 70         LD           (HL),B
78A5: A7         AND         A
78A6: 28 04      JR           Z,$78AC
78A8: 3E 13      LD           A,$13
78AA: E0 F2      LDFF00   ($F2),A
78AC: C5         PUSH       BC
78AD: 7B         LD           A,E
78AE: CB 37      SWAP        1,E
78B0: 5F         LD           E,A
78B1: 21 03 77   LD           HL,$7703
78B4: 19         ADD         HL,DE
78B5: 11 01 D6   LD           DE,$D601
78B8: 0E 0D      LD           C,$0D
78BA: 2A         LD           A,(HLI)
78BB: 12         LD           (DE),A
78BC: 13         INC         DE
78BD: 0D         DEC         C
78BE: 20 FA      JR           NZ,$78BA
78C0: C1         POP         BC
78C1: CD 77 7B   CALL       $7B77
78C4: 30 1A      JR           NC,$78E0
78C6: FA 09 C5   LD           A,($C509)
78C9: A7         AND         A
78CA: 28 0F      JR           Z,$78DB
78CC: 3D         DEC         A
78CD: 5F         LD           E,A
78CE: 50         LD           D,B
78CF: 21 57 77   LD           HL,$7757
78D2: 19         ADD         HL,DE
78D3: 7E         LD           A,(HL)
78D4: CD 97 21   CALL       $2197
78D7: CD 8D 3B   CALL       $3B8D
78DA: C9         RET
78DB: 3E 2E      LD           A,$2E
78DD: CD 97 21   CALL       $2197
78E0: C9         RET
78E1: FA 9F C1   LD           A,($C19F)
78E4: A7         AND         A
78E5: C0         RET         NZ
78E6: FA 77 C1   LD           A,($C177)
78E9: FE 00      CP           $00
78EB: 28 42      JR           Z,$792F
78ED: FE 02      CP           $02
78EF: 28 17      JR           Z,$7908
78F1: FA 0B C5   LD           A,($C50B)
78F4: 5F         LD           E,A
78F5: 50         LD           D,B
78F6: 21 05 C5   LD           HL,$C505
78F9: 19         ADD         HL,DE
78FA: FA 09 C5   LD           A,($C509)
78FD: 77         LD           (HL),A
78FE: 11 01 D6   LD           DE,$D601
7901: CD 0F 79   CALL       $790F
7904: AF         XOR         A
7905: EA 09 C5   LD           ($C509),A
7908: 21 90 C2   LD           HL,$C290
790B: 09         ADD         HL,BC
790C: 36 01      LD           (HL),$01
790E: C9         RET
790F: D5         PUSH       DE
7910: 3D         DEC         A
7911: 57         LD           D,A
7912: CB 27      SLA         1,E
7914: 5F         LD           E,A
7915: CB 27      SLA         1,E
7917: CB 27      SLA         1,E
7919: 83         ADD         A,E
791A: 82         ADD         A,D
791B: 5F         LD           E,A
791C: 50         LD           D,B
791D: 21 C0 76   LD           HL,$76C0
7920: 19         ADD         HL,DE
7921: D1         POP         DE
7922: C5         PUSH       BC
7923: 0E 0B      LD           C,$0B
7925: 2A         LD           A,(HLI)
7926: 12         LD           (DE),A
7927: 13         INC         DE
7928: 0D         DEC         C
7929: 20 FA      JR           NZ,$7925
792B: AF         XOR         A
792C: 12         LD           (DE),A
792D: C1         POP         BC
792E: C9         RET
792F: FA 09 C5   LD           A,($C509)
7932: 5F         LD           E,A
7933: FE 02      CP           $02
7935: 20 08      JR           NZ,$793F
7937: FA A9 C5   LD           A,($C5A9)
793A: A7         AND         A
793B: 20 4C      JR           NZ,$7989
793D: 18 51      JR           $7990
793F: FE 04      CP           $04
7941: 20 1A      JR           NZ,$795D
7943: 21 00 DB   LD           HL,$DB00
7946: 16 0C      LD           D,$0C
7948: 2A         LD           A,(HLI)
7949: FE 02      CP           $02
794B: 28 05      JR           Z,$7952
794D: 15         DEC         D
794E: 20 F8      JR           NZ,$7948
7950: 18 3E      JR           $7990
7952: FA 4D DB   LD           A,($DB4D)
7955: 21 77 DB   LD           HL,$DB77
7958: BE         CP           (HL)
7959: 30 2E      JR           NC,$7989
795B: 18 33      JR           $7990
795D: FE 06      CP           $06
795F: 20 1A      JR           NZ,$797B
7961: 21 00 DB   LD           HL,$DB00
7964: 16 0C      LD           D,$0C
7966: 2A         LD           A,(HLI)
7967: FE 05      CP           $05
7969: 28 05      JR           Z,$7970
796B: 15         DEC         D
796C: 20 F8      JR           NZ,$7966
796E: 18 20      JR           $7990
7970: FA 45 DB   LD           A,($DB45)
7973: 21 78 DB   LD           HL,$DB78
7976: BE         CP           (HL)
7977: 30 10      JR           NC,$7989
7979: 18 15      JR           $7990
797B: FE 03      CP           $03
797D: 20 11      JR           NZ,$7990
797F: 21 00 DB   LD           HL,$DB00
7982: 16 0C      LD           D,$0C
7984: 2A         LD           A,(HLI)
7985: FE 04      CP           $04
7987: 20 04      JR           NZ,$798D
7989: 3E 29      LD           A,$29
798B: 18 1B      JR           $79A8
798D: 15         DEC         D
798E: 20 F4      JR           NZ,$7984
7990: 50         LD           D,B
7991: 21 61 77   LD           HL,$7761
7994: 19         ADD         HL,DE
7995: 7E         LD           A,(HL)
7996: 21 6A 77   LD           HL,$776A
7999: 19         ADD         HL,DE
799A: 5E         LD           E,(HL)
799B: 57         LD           D,A
799C: FA 5E DB   LD           A,($DB5E)
799F: 93         SUB         E
79A0: FA 5D DB   LD           A,($DB5D)
79A3: 9A         SBC         D
79A4: 30 0C      JR           NC,$79B2
79A6: 3E 34      LD           A,$34
79A8: CD 97 21   CALL       $2197
79AB: 21 90 C2   LD           HL,$C290
79AE: 09         ADD         HL,BC
79AF: 36 03      LD           (HL),$03
79B1: C9         RET
79B2: 21 09 C5   LD           HL,$C509
79B5: 7E         LD           A,(HL)
79B6: F5         PUSH       AF
79B7: 36 00      LD           (HL),$00
79B9: 5F         LD           E,A
79BA: 50         LD           D,B
79BB: 21 7C 77   LD           HL,$777C
79BE: 19         ADD         HL,DE
79BF: FA 92 DB   LD           A,($DB92)
79C2: 86         ADD         A,(HL)
79C3: EA 92 DB   LD           ($DB92),A
79C6: CB 17      RL          1,E
79C8: 21 73 77   LD           HL,$7773
79CB: 19         ADD         HL,DE
79CC: CB 1F      RR          1,E
79CE: FA 91 DB   LD           A,($DB91)
79D1: 8E         ADC         A,(HL)
79D2: EA 91 DB   LD           ($DB91),A
79D5: 21 90 C2   LD           HL,$C290
79D8: 09         ADD         HL,BC
79D9: 36 01      LD           (HL),$01
79DB: F1         POP         AF
79DC: F5         PUSH       AF
79DD: 3E 35      LD           A,$35
79DF: CD 97 21   CALL       $2197
79E2: F1         POP         AF
79E3: 3D         DEC         A
79E4: C7         RST         0X00
79E5: 2E 7A      LD           L,$7A
79E7: 5A         LD           E,D
79E8: 7A         LD           A,D
79E9: 60         LD           H,B
79EA: 7A         LD           A,D
79EB: 34         INC         (HL)
79EC: 7A         LD           A,D
79ED: F7         RST         0X30
79EE: 79         LD           A,C
79EF: 02         LD           (BC),A
79F0: 7A         LD           A,D
79F1: 10 7A      STOP       $7A
79F3: 16 7A      LD           D,$7A
79F5: 24         INC         H
79F6: 7A         LD           A,D
79F7: 16 05      LD           D,$05
79F9: CD 95 3E   CALL       $3E95
79FC: 3E 20      LD           A,$20
79FE: EA 45 DB   LD           ($DB45),A
7A01: C9         RET
7A02: FA 45 DB   LD           A,($DB45)
7A05: C6 0A      ADD         $0A
7A07: 27         DAA
7A08: 30 02      JR           NC,$7A0C
7A0A: 3E 99      LD           A,$99
7A0C: EA 45 DB   LD           ($DB45),A
7A0F: C9         RET
7A10: 16 09      LD           D,$09
7A12: CD 95 3E   CALL       $3E95
7A15: C9         RET
7A16: FA 47 DB   LD           A,($DB47)
7A19: C6 0A      ADD         $0A
7A1B: 27         DAA
7A1C: 30 02      JR           NC,$7A20
7A1E: 3E 99      LD           A,$99
7A20: EA 47 DB   LD           ($DB47),A
7A23: C9         RET
7A24: FA 0D DB   LD           A,($DB0D)
7A27: C6 01      ADD         $01
7A29: 27         DAA
7A2A: EA 0D DB   LD           ($DB0D),A
7A2D: C9         RET
7A2E: 16 0B      LD           D,$0B
7A30: CD 95 3E   CALL       $3E95
7A33: C9         RET
7A34: FA 4D DB   LD           A,($DB4D)
7A37: C6 0A      ADD         $0A
7A39: 27         DAA
7A3A: 30 02      JR           NC,$7A3E
7A3C: 3E 99      LD           A,$99
7A3E: EA 4D DB   LD           ($DB4D),A
7A41: 16 02      LD           D,$02
7A43: CD 95 3E   CALL       $3E95
7A46: C9         RET
7A47: FA 45 DB   LD           A,($DB45)
7A4A: C6 0A      ADD         $0A
7A4C: 27         DAA
7A4D: 30 02      JR           NC,$7A51
7A4F: 3E 99      LD           A,$99
7A51: EA 45 DB   LD           ($DB45),A
7A54: 16 0C      LD           D,$0C
7A56: CD 95 3E   CALL       $3E95
7A59: C9         RET
7A5A: 3E 18      LD           A,$18
7A5C: EA 93 DB   LD           ($DB93),A
7A5F: C9         RET
7A60: 16 04      LD           D,$04
7A62: CD 95 3E   CALL       $3E95
7A65: C9         RET
7A66: FA 9F C1   LD           A,($C19F)
7A69: A7         AND         A
7A6A: 20 03      JR           NZ,$7A6F
7A6C: CD F1 78   CALL       $78F1
7A6F: C9         RET
7A70: FA 9F C1   LD           A,($C19F)
7A73: A7         AND         A
7A74: 20 34      JR           NZ,$7AAA
7A76: 3E CA      LD           A,$CA
7A78: CD 01 3C   CALL       $3C01
7A7B: 3E 26      LD           A,$26
7A7D: E0 F4      LDFF00   ($F4),A
7A7F: F0 D7      LD           A,($D7)
7A81: 21 00 C2   LD           HL,$C200
7A84: 19         ADD         HL,DE
7A85: 77         LD           (HL),A
7A86: F0 D8      LD           A,($D8)
7A88: 21 10 C2   LD           HL,$C210
7A8B: 19         ADD         HL,DE
7A8C: 77         LD           (HL),A
7A8D: 21 D0 C2   LD           HL,$C2D0
7A90: 19         ADD         HL,DE
7A91: 36 01      LD           (HL),$01
7A93: 21 E0 C2   LD           HL,$C2E0
7A96: 19         ADD         HL,DE
7A97: 36 C0      LD           (HL),$C0
7A99: CD 91 08   CALL       $0891
7A9C: 36 C0      LD           (HL),$C0
7A9E: CD 8D 3B   CALL       $3B8D
7AA1: AF         XOR         A
7AA2: EA 0D DB   LD           ($DB0D),A
7AA5: 3E FF      LD           A,$FF
7AA7: EA 94 DB   LD           ($DB94),A
7AAA: C9         RET
7AAB: 3E 02      LD           A,$02
7AAD: E0 A1      LDFF00   ($A1),A
7AAF: CD 91 08   CALL       $0891
7AB2: 20 0F      JR           NZ,$7AC3
7AB4: FA 5A DB   LD           A,($DB5A)
7AB7: A7         AND         A
7AB8: 20 09      JR           NZ,$7AC3
7ABA: EA 46 DB   LD           ($DB46),A
7ABD: EA 0A C5   LD           ($C50A),A
7AC0: C3 44 6D   JP           $6D44
7AC3: C9         RET
7AC4: 1D         DEC         E
7AC5: 3D         DEC         A
7AC6: 5D         LD           E,L
7AC7: 7D         LD           A,L
7AC8: 96         SUB         (HL)
7AC9: 10 A8      STOP       $A8
7ACB: 10 86      STOP       $86
7ACD: 10 80      STOP       $80
7ACF: 10 88      STOP       $88
7AD1: 10 FF      STOP       $FF
7AD3: FF         RST         0X38
7AD4: 90         SUB         B
7AD5: 10 AE      STOP       $AE
7AD7: 10 A0      STOP       $A0
7AD9: 10 2A      STOP       $2A
7ADB: 40         LD           B,B
7ADC: 2A         LD           A,(HLI)
7ADD: 60         LD           H,B
7ADE: 3E 04      LD           A,$04
7AE0: E0 E6      LDFF00   ($E6),A
7AE2: 5F         LD           E,A
7AE3: 50         LD           D,B
7AE4: 21 04 C5   LD           HL,$C504
7AE7: 19         ADD         HL,DE
7AE8: 7E         LD           A,(HL)
7AE9: A7         AND         A
7AEA: 28 2E      JR           Z,$7B1A
7AEC: 3D         DEC         A
7AED: E0 F1      LDFF00   ($F1),A
7AEF: 21 C3 7A   LD           HL,$7AC3
7AF2: F0 E6      LD           A,($E6)
7AF4: 5F         LD           E,A
7AF5: 19         ADD         HL,DE
7AF6: 7E         LD           A,(HL)
7AF7: E0 EE      LDFF00   ($EE),A
7AF9: 3E 32      LD           A,$32
7AFB: E0 EC      LDFF00   ($EC),A
7AFD: F0 F1      LD           A,($F1)
7AFF: FE 01      CP           $01
7B01: 20 05      JR           NZ,$7B08
7B03: 21 EC FF   LD           HL,$FFEC
7B06: 36 2F      LD           (HL),$2F
7B08: FE 05      CP           $05
7B0A: 20 08      JR           NZ,$7B14
7B0C: 11 C6 7A   LD           DE,$7AC6
7B0F: CD 3B 3C   CALL       $3C3B
7B12: 18 06      JR           $7B1A
7B14: 11 C8 7A   LD           DE,$7AC8
7B17: CD D0 3C   CALL       $3CD0
7B1A: F0 E6      LD           A,($E6)
7B1C: 3D         DEC         A
7B1D: 20 C1      JR           NZ,$7AE0
7B1F: CD 26 7B   CALL       $7B26
7B22: CD BA 3D   CALL       $3DBA
7B25: C9         RET
7B26: FA 09 C5   LD           A,($C509)
7B29: A7         AND         A
7B2A: 28 27      JR           Z,$7B53
7B2C: 3D         DEC         A
7B2D: E0 F1      LDFF00   ($F1),A
7B2F: 3E 01      LD           A,$01
7B31: EA 5C C1   LD           ($C15C),A
7B34: CD 3B 09   CALL       $093B
7B37: F0 98      LD           A,($98)
7B39: E0 EE      LDFF00   ($EE),A
7B3B: F0 99      LD           A,($99)
7B3D: D6 0E      SUB         $0E
7B3F: E0 EC      LDFF00   ($EC),A
7B41: F0 F1      LD           A,($F1)
7B43: FE 05      CP           $05
7B45: 20 06      JR           NZ,$7B4D
7B47: 11 C6 7A   LD           DE,$7AC6
7B4A: C3 3B 3C   JP           $3C3B
7B4D: 11 C8 7A   LD           DE,$7AC8
7B50: CD D0 3C   CALL       $3CD0
7B53: C9         RET
7B54: CD D5 3B   CALL       $3BD5
7B57: 30 1D      JR           NC,$7B76
7B59: CD 4A 09   CALL       $094A
7B5C: CD 42 09   CALL       $0942
7B5F: FA A6 C1   LD           A,($C1A6)
7B62: A7         AND         A
7B63: 28 11      JR           Z,$7B76
7B65: 5F         LD           E,A
7B66: 50         LD           D,B
7B67: 21 9F C3   LD           HL,$C39F
7B6A: 19         ADD         HL,DE
7B6B: 7E         LD           A,(HL)
7B6C: FE 03      CP           $03
7B6E: 20 06      JR           NZ,$7B76
7B70: 21 8F C2   LD           HL,$C28F
7B73: 19         ADD         HL,DE
7B74: 36 00      LD           (HL),$00
7B76: C9         RET
7B77: F0 98      LD           A,($98)
7B79: 21 EE FF   LD           HL,$FFEE
7B7C: 96         SUB         (HL)
7B7D: C6 20      ADD         $20
7B7F: FE 30      CP           $30
7B81: 30 37      JR           NC,$7BBA
7B83: F0 99      LD           A,($99)
7B85: 21 EF FF   LD           HL,$FFEF
7B88: 96         SUB         (HL)
7B89: C6 10      ADD         $10
7B8B: FE 20      CP           $20
7B8D: 30 2B      JR           NC,$7BBA
7B8F: CD 1F 6E   CALL       $6E1F
7B92: F0 9E      LD           A,($9E)
7B94: EE 01      XOR         $01
7B96: BB         CP           E
7B97: 20 21      JR           NZ,$7BBA
7B99: 21 AD C1   LD           HL,$C1AD
7B9C: 36 01      LD           (HL),$01
7B9E: FA 9F C1   LD           A,($C19F)
7BA1: 21 4F C1   LD           HL,$C14F
7BA4: B6         OR           (HL)
7BA5: 21 34 C1   LD           HL,$C134
7BA8: B6         OR           (HL)
7BA9: 20 0F      JR           NZ,$7BBA
7BAB: FA 9A DB   LD           A,($DB9A)
7BAE: FE 80      CP           $80
7BB0: 20 08      JR           NZ,$7BBA
7BB2: F0 CC      LD           A,($CC)
7BB4: E6 10      AND         $10
7BB6: 28 02      JR           Z,$7BBA
7BB8: 37         SCF
7BB9: C9         RET
7BBA: A7         AND         A
7BBB: C9         RET
7BBC: FA 9F C1   LD           A,($C19F)
7BBF: 21 4F C1   LD           HL,$C14F
7BC2: B6         OR           (HL)
7BC3: 21 46 C1   LD           HL,$C146
7BC6: B6         OR           (HL)
7BC7: 21 34 C1   LD           HL,$C134
7BCA: B6         OR           (HL)
7BCB: 20 36      JR           NZ,$7C03
7BCD: FA 9A DB   LD           A,($DB9A)
7BD0: FE 80      CP           $80
7BD2: 20 2F      JR           NZ,$7C03
7BD4: F0 98      LD           A,($98)
7BD6: 21 EE FF   LD           HL,$FFEE
7BD9: 96         SUB         (HL)
7BDA: C6 10      ADD         $10
7BDC: FE 20      CP           $20
7BDE: 30 23      JR           NC,$7C03
7BE0: F0 99      LD           A,($99)
7BE2: 21 EF FF   LD           HL,$FFEF
7BE5: 96         SUB         (HL)
7BE6: C6 14      ADD         $14
7BE8: FE 28      CP           $28
7BEA: 30 17      JR           NC,$7C03
7BEC: CD 1F 6E   CALL       $6E1F
7BEF: F0 9E      LD           A,($9E)
7BF1: EE 01      XOR         $01
7BF3: BB         CP           E
7BF4: 20 0D      JR           NZ,$7C03
7BF6: 21 AD C1   LD           HL,$C1AD
7BF9: 36 01      LD           (HL),$01
7BFB: F0 CC      LD           A,($CC)
7BFD: E6 10      AND         $10
7BFF: 28 02      JR           Z,$7C03
7C01: 37         SCF
7C02: C9         RET
7C03: A7         AND         A
7C04: C9         RET
7C05: 06 04      LD           B,$04
7C07: 02         LD           (BC),A
7C08: 00         NOP
7C09: 21 80 C3   LD           HL,$C380
7C0C: 09         ADD         HL,BC
7C0D: 5E         LD           E,(HL)
7C0E: 50         LD           D,B
7C0F: 21 05 7C   LD           HL,$7C05
7C12: 19         ADD         HL,DE
7C13: E5         PUSH       HL
7C14: 21 D0 C3   LD           HL,$C3D0
7C17: 09         ADD         HL,BC
7C18: 34         INC         (HL)
7C19: 7E         LD           A,(HL)
7C1A: 1F         RRA
7C1B: 1F         RRA
7C1C: 1F         RRA
7C1D: E1         POP         HL
7C1E: E6 01      AND         $01
7C20: B6         OR           (HL)
7C21: C3 87 3B   JP           $3B87
7C24: 21 40 C2   LD           HL,$C240
7C27: 09         ADD         HL,BC
7C28: 7E         LD           A,(HL)
7C29: F5         PUSH       AF
7C2A: 36 01      LD           (HL),$01
7C2C: 21 50 C2   LD           HL,$C250
7C2F: 09         ADD         HL,BC
7C30: 7E         LD           A,(HL)
7C31: F5         PUSH       AF
7C32: 36 01      LD           (HL),$01
7C34: CD 9E 3B   CALL       $3B9E
7C37: 21 A0 C2   LD           HL,$C2A0
7C3A: 09         ADD         HL,BC
7C3B: 7E         LD           A,(HL)
7C3C: F5         PUSH       AF
7C3D: 21 40 C2   LD           HL,$C240
7C40: 09         ADD         HL,BC
7C41: 36 FF      LD           (HL),$FF
7C43: 21 50 C2   LD           HL,$C250
7C46: 09         ADD         HL,BC
7C47: 36 FF      LD           (HL),$FF
7C49: CD 9E 3B   CALL       $3B9E
7C4C: 21 A0 C2   LD           HL,$C2A0
7C4F: 09         ADD         HL,BC
7C50: F1         POP         AF
7C51: B6         OR           (HL)
7C52: 77         LD           (HL),A
7C53: F1         POP         AF
7C54: 21 50 C2   LD           HL,$C250
7C57: 09         ADD         HL,BC
7C58: 77         LD           (HL),A
7C59: F1         POP         AF
7C5A: 21 40 C2   LD           HL,$C240
7C5D: 09         ADD         HL,BC
7C5E: 77         LD           (HL),A
7C5F: C9         RET
7C60: 7A         LD           A,D
7C61: 20 78      JR           NZ,$7CDB
7C63: 20 78      JR           NZ,$7CDD
7C65: 00         NOP
7C66: 7A         LD           A,D
7C67: 00         NOP
7C68: 7E         LD           A,(HL)
7C69: 00         NOP
7C6A: 7E         LD           A,(HL)
7C6B: 20 70      JR           NZ,$7CDD
7C6D: 00         NOP
7C6E: 72         LD           (HL),D
7C6F: 00         NOP
7C70: 74         LD           (HL),H
7C71: 00         NOP
7C72: 76         HALT
7C73: 00         NOP
7C74: 7C         LD           A,H
7C75: 00         NOP
7C76: 7C         LD           A,H
7C77: 20 6A      JR           NZ,$7CE3
7C79: 20 68      JR           NZ,$7CE3
7C7B: 20 68      JR           NZ,$7CE5
7C7D: 00         NOP
7C7E: 6A         LD           L,D
7C7F: 00         NOP
7C80: 6E         LD           L,(HL)
7C81: 00         NOP
7C82: 6E         LD           L,(HL)
7C83: 20 60      JR           NZ,$7CE5
7C85: 00         NOP
7C86: 62         LD           H,D
7C87: 00         NOP
7C88: 64         LD           H,H
7C89: 00         NOP
7C8A: 66         LD           H,(HL)
7C8B: 00         NOP
7C8C: 6C         LD           L,H
7C8D: 00         NOP
7C8E: 6C         LD           L,H
7C8F: 20 11      JR           NZ,$7CA2
7C91: 60         LD           H,B
7C92: 7C         LD           A,H
7C93: F0 F7      LD           A,($F7)
7C95: FE 07      CP           $07
7C97: 20 03      JR           NZ,$7C9C
7C99: 11 78 7C   LD           DE,$7C78
7C9C: CD 8C 08   CALL       $088C
7C9F: 17         RLA
7CA0: 17         RLA
7CA1: 17         RLA
7CA2: E6 10      AND         $10
7CA4: E0 ED      LDFF00   ($ED),A
7CA6: CD 3B 3C   CALL       $3C3B
7CA9: CD 1F 7F   CALL       $7F1F
7CAC: 21 10 C4   LD           HL,$C410
7CAF: 09         ADD         HL,BC
7CB0: 7E         LD           A,(HL)
7CB1: FE 08      CP           $08
7CB3: 20 0D      JR           NZ,$7CC2
7CB5: F0 F0      LD           A,($F0)
7CB7: A7         AND         A
7CB8: 20 08      JR           NZ,$7CC2
7CBA: CD 8D 3B   CALL       $3B8D
7CBD: CD 87 08   CALL       $0887
7CC0: 36 6F      LD           (HL),$6F
7CC2: CD 4A 6D   CALL       $6D4A
7CC5: CD 94 6D   CALL       $6D94
7CC8: CD 9E 3B   CALL       $3B9E
7CCB: F0 F0      LD           A,($F0)
7CCD: C7         RST         0X00
7CCE: DA 7C 15   JP           C,$157C
7CD1: 7D         LD           A,L
7CD2: 08 F8 00   LD           ($00F8),SP
7CD5: 00         NOP
7CD6: 00         NOP
7CD7: 00         NOP
7CD8: F8 00      LDHL       SP,$00
7CDA: CD B4 3B   CALL       $3BB4
7CDD: CD 91 08   CALL       $0891
7CE0: 20 20      JR           NZ,$7D02
7CE2: CD ED 27   CALL       $27ED
7CE5: E6 1F      AND         $1F
7CE7: C6 30      ADD         $30
7CE9: 77         LD           (HL),A
7CEA: E6 03      AND         $03
7CEC: 5F         LD           E,A
7CED: 50         LD           D,B
7CEE: 21 D2 7C   LD           HL,$7CD2
7CF1: 19         ADD         HL,DE
7CF2: 7E         LD           A,(HL)
7CF3: 21 40 C2   LD           HL,$C240
7CF6: 09         ADD         HL,BC
7CF7: 77         LD           (HL),A
7CF8: 21 D6 7C   LD           HL,$7CD6
7CFB: 19         ADD         HL,DE
7CFC: 7E         LD           A,(HL)
7CFD: 21 50 C2   LD           HL,$C250
7D00: 09         ADD         HL,BC
7D01: 77         LD           (HL),A
7D02: F0 E7      LD           A,($E7)
7D04: 1F         RRA
7D05: 1F         RRA
7D06: 1F         RRA
7D07: 1F         RRA
7D08: E6 01      AND         $01
7D0A: CD 87 3B   CALL       $3B87
7D0D: C9         RET
7D0E: 05         DEC         B
7D0F: 05         DEC         B
7D10: 04         INC         B
7D11: 03         INC         BC
7D12: 02         LD           (BC),A
7D13: 02         LD           (BC),A
7D14: 02         LD           (BC),A
7D15: FA 4A C1   LD           A,($C14A)
7D18: A7         AND         A
7D19: 28 05      JR           Z,$7D20
7D1B: CD 8D 3B   CALL       $3B8D
7D1E: 70         LD           (HL),B
7D1F: C9         RET
7D20: CD EB 3B   CALL       $3BEB
7D23: CD FF 6D   CALL       $6DFF
7D26: C6 12      ADD         $12
7D28: FE 24      CP           $24
7D2A: 30 09      JR           NC,$7D35
7D2C: CD 0F 6E   CALL       $6E0F
7D2F: C6 12      ADD         $12
7D31: FE 24      CP           $24
7D33: 38 0E      JR           C,$7D43
7D35: F0 E7      LD           A,($E7)
7D37: A9         XOR         C
7D38: E6 03      AND         $03
7D3A: 20 05      JR           NZ,$7D41
7D3C: 3E 0E      LD           A,$0E
7D3E: CD 25 3C   CALL       $3C25
7D41: 18 03      JR           $7D46
7D43: CD AF 3D   CALL       $3DAF
7D46: CD 87 08   CALL       $0887
7D49: CA 2F 7E   JP           Z,$7E2F
7D4C: FE 18      CP           $18
7D4E: 20 07      JR           NZ,$7D57
7D50: 36 0A      LD           (HL),$0A
7D52: CD 8C 08   CALL       $088C
7D55: 36 30      LD           (HL),$30
7D57: 1F         RRA
7D58: 1F         RRA
7D59: 1F         RRA
7D5A: 1F         RRA
7D5B: E6 07      AND         $07
7D5D: 5F         LD           E,A
7D5E: 50         LD           D,B
7D5F: 21 0E 7D   LD           HL,$7D0E
7D62: 19         ADD         HL,DE
7D63: 7E         LD           A,(HL)
7D64: CD 87 3B   CALL       $3B87
7D67: C9         RET
7D68: 7A         LD           A,D
7D69: 20 78      JR           NZ,$7DE3
7D6B: 20 78      JR           NZ,$7DE5
7D6D: 00         NOP
7D6E: 7A         LD           A,D
7D6F: 00         NOP
7D70: 6A         LD           L,D
7D71: 20 68      JR           NZ,$7DDB
7D73: 20 68      JR           NZ,$7DDD
7D75: 00         NOP
7D76: 6A         LD           L,D
7D77: 00         NOP
7D78: 08 F8 00   LD           ($00F8),SP
7D7B: 00         NOP
7D7C: 00         NOP
7D7D: 00         NOP
7D7E: F8 08      LDHL       SP,$08
7D80: 11 68 7D   LD           DE,$7D68
7D83: F0 F7      LD           A,($F7)
7D85: FE 07      CP           $07
7D87: 20 03      JR           NZ,$7D8C
7D89: 11 70 7D   LD           DE,$7D70
7D8C: CD 3B 3C   CALL       $3C3B
7D8F: CD 1F 7F   CALL       $7F1F
7D92: CD 4A 6D   CALL       $6D4A
7D95: CD 8C 08   CALL       $088C
7D98: 20 03      JR           NZ,$7D9D
7D9A: CD B4 3B   CALL       $3BB4
7D9D: CD 94 6D   CALL       $6D94
7DA0: CD 9E 3B   CALL       $3B9E
7DA3: F0 F0      LD           A,($F0)
7DA5: C7         RST         0X00
7DA6: AC         XOR         H
7DA7: 7D         LD           A,L
7DA8: C0         RET         NZ
7DA9: 7D         LD           A,L
7DAA: F7         RST         0X30
7DAB: 7D         LD           A,L
7DAC: CD 91 08   CALL       $0891
7DAF: 20 03      JR           NZ,$7DB4
7DB1: CD 8D 3B   CALL       $3B8D
7DB4: F0 E7      LD           A,($E7)
7DB6: 1F         RRA
7DB7: 1F         RRA
7DB8: 1F         RRA
7DB9: 1F         RRA
7DBA: E6 01      AND         $01
7DBC: CD 87 3B   CALL       $3B87
7DBF: C9         RET
7DC0: CD ED 27   CALL       $27ED
7DC3: E6 03      AND         $03
7DC5: 28 07      JR           Z,$7DCE
7DC7: CD ED 27   CALL       $27ED
7DCA: E6 03      AND         $03
7DCC: 18 03      JR           $7DD1
7DCE: CD 1F 6E   CALL       $6E1F
7DD1: 5F         LD           E,A
7DD2: 50         LD           D,B
7DD3: 21 78 7D   LD           HL,$7D78
7DD6: 19         ADD         HL,DE
7DD7: 7E         LD           A,(HL)
7DD8: 21 40 C2   LD           HL,$C240
7DDB: 09         ADD         HL,BC
7DDC: 77         LD           (HL),A
7DDD: 21 7C 7D   LD           HL,$7D7C
7DE0: 19         ADD         HL,DE
7DE1: 7E         LD           A,(HL)
7DE2: 21 50 C2   LD           HL,$C250
7DE5: 09         ADD         HL,BC
7DE6: 77         LD           (HL),A
7DE7: CD 91 08   CALL       $0891
7DEA: CD ED 27   CALL       $27ED
7DED: E6 0F      AND         $0F
7DEF: C6 20      ADD         $20
7DF1: 77         LD           (HL),A
7DF2: CD 8D 3B   CALL       $3B8D
7DF5: 70         LD           (HL),B
7DF6: C9         RET
7DF7: CD F6 3B   CALL       $3BF6
7DFA: CD 91 08   CALL       $0891
7DFD: 28 30      JR           Z,$7E2F
7DFF: 21 A0 C2   LD           HL,$C2A0
7E02: 09         ADD         HL,BC
7E03: 7E         LD           A,(HL)
7E04: E6 03      AND         $03
7E06: 20 07      JR           NZ,$7E0F
7E08: 7E         LD           A,(HL)
7E09: E6 0C      AND         $0C
7E0B: 20 0C      JR           NZ,$7E19
7E0D: 18 16      JR           $7E25
7E0F: 21 40 C2   LD           HL,$C240
7E12: 09         ADD         HL,BC
7E13: 7E         LD           A,(HL)
7E14: 2F         CPL
7E15: 3C         INC         A
7E16: 77         LD           (HL),A
7E17: 18 08      JR           $7E21
7E19: 21 50 C2   LD           HL,$C250
7E1C: 09         ADD         HL,BC
7E1D: 7E         LD           A,(HL)
7E1E: 2F         CPL
7E1F: 3C         INC         A
7E20: 77         LD           (HL),A
7E21: 3E 09      LD           A,$09
7E23: E0 F2      LDFF00   ($F2),A
7E25: F0 E7      LD           A,($E7)
7E27: 1F         RRA
7E28: 1F         RRA
7E29: E6 01      AND         $01
7E2B: CD 87 3B   CALL       $3B87
7E2E: C9         RET
7E2F: CD 36 7E   CALL       $7E36
7E32: CD 44 6D   CALL       $6D44
7E35: C9         RET
7E36: 3E 02      LD           A,$02
7E38: CD 01 3C   CALL       $3C01
7E3B: 38 1D      JR           C,$7E5A
7E3D: CD D7 08   CALL       $08D7
7E40: F0 D7      LD           A,($D7)
7E42: 21 00 C2   LD           HL,$C200
7E45: 19         ADD         HL,DE
7E46: 77         LD           (HL),A
7E47: F0 D8      LD           A,($D8)
7E49: 21 10 C2   LD           HL,$C210
7E4C: 19         ADD         HL,DE
7E4D: 77         LD           (HL),A
7E4E: 21 E0 C2   LD           HL,$C2E0
7E51: 19         ADD         HL,DE
7E52: 36 17      LD           (HL),$17
7E54: 21 40 C4   LD           HL,$C440
7E57: 19         ADD         HL,DE
7E58: 36 01      LD           (HL),$01
7E5A: C9         RET
7E5B: 56         LD           D,(HL)
7E5C: 00         NOP
7E5D: 56         LD           D,(HL)
7E5E: 20 54      JR           NZ,$7EB4
7E60: 00         NOP
7E61: 54         LD           D,H
7E62: 20 52      JR           NZ,$7EB6
7E64: 00         NOP
7E65: 52         LD           D,D
7E66: 20 50      JR           NZ,$7EB8
7E68: 00         NOP
7E69: 50         LD           D,B
7E6A: 20 11      JR           NZ,$7E7D
7E6C: 5B         LD           E,E
7E6D: 7E         LD           A,(HL)
7E6E: CD 3B 3C   CALL       $3C3B
7E71: CD 1F 7F   CALL       $7F1F
7E74: CD 4A 6D   CALL       $6D4A
7E77: CD 94 6D   CALL       $6D94
7E7A: CD 9E 3B   CALL       $3B9E
7E7D: F0 F0      LD           A,($F0)
7E7F: E6 03      AND         $03
7E81: C7         RST         0X00
7E82: 8A         ADC         A,D
7E83: 7E         LD           A,(HL)
7E84: 9F         SBC         A
7E85: 7E         LD           A,(HL)
7E86: C3 7E F0   JP           $F07E
7E89: 7E         LD           A,(HL)
7E8A: 3E FF      LD           A,$FF
7E8C: CD 87 3B   CALL       $3B87
7E8F: CD 91 08   CALL       $0891
7E92: 20 08      JR           NZ,$7E9C
7E94: 36 1F      LD           (HL),$1F
7E96: CD 8D 3B   CALL       $3B8D
7E99: CD AF 3D   CALL       $3DAF
7E9C: C9         RET
7E9D: 01 00 CD   LD           BC,$CD00
7EA0: 91         SUB         C
7EA1: 08 20 0C   LD           ($0C20),SP
7EA4: CD ED 27   CALL       $27ED
7EA7: E6 3F      AND         $3F
7EA9: C6 70      ADD         $70
7EAB: 77         LD           (HL),A
7EAC: CD 8D 3B   CALL       $3B8D
7EAF: C9         RET
7EB0: 21 9D 7E   LD           HL,$7E9D
7EB3: CB 3F      SRL         1,E
7EB5: CB 3F      SRL         1,E
7EB7: CB 3F      SRL         1,E
7EB9: CB 3F      SRL         1,E
7EBB: 5F         LD           E,A
7EBC: 50         LD           D,B
7EBD: 19         ADD         HL,DE
7EBE: 7E         LD           A,(HL)
7EBF: CD 87 3B   CALL       $3B87
7EC2: C9         RET
7EC3: CD B4 3B   CALL       $3BB4
7EC6: CD 91 08   CALL       $0891
7EC9: 20 09      JR           NZ,$7ED4
7ECB: 36 1F      LD           (HL),$1F
7ECD: CD 8D 3B   CALL       $3B8D
7ED0: CD AF 3D   CALL       $3DAF
7ED3: C9         RET
7ED4: F0 E7      LD           A,($E7)
7ED6: A9         XOR         C
7ED7: F5         PUSH       AF
7ED8: E6 0F      AND         $0F
7EDA: 20 05      JR           NZ,$7EE1
7EDC: 3E 08      LD           A,$08
7EDE: CD 25 3C   CALL       $3C25
7EE1: F1         POP         AF
7EE2: CB 3F      SRL         1,E
7EE4: CB 3F      SRL         1,E
7EE6: E6 01      AND         $01
7EE8: CD 87 3B   CALL       $3B87
7EEB: 34         INC         (HL)
7EEC: 34         INC         (HL)
7EED: C9         RET
7EEE: 00         NOP
7EEF: 01 CD 91   LD           BC,$91CD
7EF2: 08 20 11   LD           ($1120),SP
7EF5: CD ED 27   CALL       $27ED
7EF8: E6 1F      AND         $1F
7EFA: C6 30      ADD         $30
7EFC: 77         LD           (HL),A
7EFD: CD 8D 3B   CALL       $3B8D
7F00: 3E 08      LD           A,$08
7F02: CD 25 3C   CALL       $3C25
7F05: C9         RET
7F06: 21 EE 7E   LD           HL,$7EEE
7F09: C3 B3 7E   JP           $7EB3
7F0C: 21 40 C2   LD           HL,$C240
7F0F: 09         ADD         HL,BC
7F10: 7E         LD           A,(HL)
7F11: CB 17      RL          1,E
7F13: 3E 00      LD           A,$00
7F15: 38 02      JR           C,$7F19
7F17: 3E 20      LD           A,$20
7F19: 21 ED FF   LD           HL,$FFED
7F1C: AE         XOR         (HL)
7F1D: 77         LD           (HL),A
7F1E: C9         RET
7F1F: F0 EA      LD           A,($EA)
7F21: FE 05      CP           $05
7F23: 20 1A      JR           NZ,$7F3F
7F25: FA 95 DB   LD           A,($DB95)
7F28: FE 07      CP           $07
7F2A: 28 13      JR           Z,$7F3F
7F2C: 21 A8 C1   LD           HL,$C1A8
7F2F: FA 9F C1   LD           A,($C19F)
7F32: B6         OR           (HL)
7F33: 21 4F C1   LD           HL,$C14F
7F36: B6         OR           (HL)
7F37: 20 06      JR           NZ,$7F3F
7F39: FA 24 C1   LD           A,($C124)
7F3C: A7         AND         A
7F3D: 28 01      JR           Z,$7F40
7F3F: F1         POP         AF
7F40: C9         RET
7F41: FF         RST         0X38
7F42: FF         RST         0X38
7F43: FF         RST         0X38
7F44: FF         RST         0X38
7F45: FF         RST         0X38
7F46: FF         RST         0X38
7F47: FF         RST         0X38
7F48: FF         RST         0X38
7F49: FF         RST         0X38
7F4A: FF         RST         0X38
7F4B: FF         RST         0X38
7F4C: FF         RST         0X38
7F4D: FF         RST         0X38
7F4E: FF         RST         0X38
7F4F: FF         RST         0X38
7F50: FF         RST         0X38
7F51: FF         RST         0X38
7F52: FF         RST         0X38
7F53: FF         RST         0X38
7F54: FF         RST         0X38
7F55: FF         RST         0X38
7F56: FF         RST         0X38
7F57: FF         RST         0X38
7F58: FF         RST         0X38
7F59: FF         RST         0X38
7F5A: FF         RST         0X38
7F5B: FF         RST         0X38
7F5C: FF         RST         0X38
7F5D: FF         RST         0X38
7F5E: FF         RST         0X38
7F5F: FF         RST         0X38
7F60: FF         RST         0X38
7F61: FF         RST         0X38
7F62: FF         RST         0X38
7F63: FF         RST         0X38
7F64: FF         RST         0X38
7F65: FF         RST         0X38
7F66: FF         RST         0X38
7F67: FF         RST         0X38
7F68: FF         RST         0X38
7F69: FF         RST         0X38
7F6A: FF         RST         0X38
7F6B: FF         RST         0X38
7F6C: FF         RST         0X38
7F6D: FF         RST         0X38
7F6E: FF         RST         0X38
7F6F: FF         RST         0X38
7F70: FF         RST         0X38
7F71: FF         RST         0X38
7F72: FF         RST         0X38
7F73: FF         RST         0X38
7F74: FF         RST         0X38
7F75: FF         RST         0X38
7F76: FF         RST         0X38
7F77: FF         RST         0X38
7F78: FF         RST         0X38
7F79: FF         RST         0X38
7F7A: FF         RST         0X38
7F7B: FF         RST         0X38
7F7C: FF         RST         0X38
7F7D: FF         RST         0X38
7F7E: FF         RST         0X38
7F7F: FF         RST         0X38
7F80: FF         RST         0X38
7F81: FF         RST         0X38
7F82: FF         RST         0X38
7F83: FF         RST         0X38
7F84: FF         RST         0X38
7F85: FF         RST         0X38
7F86: FF         RST         0X38
7F87: FF         RST         0X38
7F88: FF         RST         0X38
7F89: FF         RST         0X38
7F8A: FF         RST         0X38
7F8B: FF         RST         0X38
7F8C: FF         RST         0X38
7F8D: FF         RST         0X38
7F8E: FF         RST         0X38
7F8F: FF         RST         0X38
7F90: FF         RST         0X38
7F91: FF         RST         0X38
7F92: FF         RST         0X38
7F93: FF         RST         0X38
7F94: FF         RST         0X38
7F95: FF         RST         0X38
7F96: FF         RST         0X38
7F97: FF         RST         0X38
7F98: FF         RST         0X38
7F99: FF         RST         0X38
7F9A: FF         RST         0X38
7F9B: FF         RST         0X38
7F9C: FF         RST         0X38
7F9D: FF         RST         0X38
7F9E: FF         RST         0X38
7F9F: FF         RST         0X38
7FA0: FF         RST         0X38
7FA1: FF         RST         0X38
7FA2: FF         RST         0X38
7FA3: FF         RST         0X38
7FA4: FF         RST         0X38
7FA5: FF         RST         0X38
7FA6: FF         RST         0X38
7FA7: FF         RST         0X38
7FA8: FF         RST         0X38
7FA9: FF         RST         0X38
7FAA: FF         RST         0X38
7FAB: FF         RST         0X38
7FAC: FF         RST         0X38
7FAD: FF         RST         0X38
7FAE: FF         RST         0X38
7FAF: FF         RST         0X38
7FB0: FF         RST         0X38
7FB1: FF         RST         0X38
7FB2: FF         RST         0X38
7FB3: FF         RST         0X38
7FB4: FF         RST         0X38
7FB5: FF         RST         0X38
7FB6: FF         RST         0X38
7FB7: FF         RST         0X38
7FB8: FF         RST         0X38
7FB9: FF         RST         0X38
7FBA: FF         RST         0X38
7FBB: FF         RST         0X38
7FBC: FF         RST         0X38
7FBD: FF         RST         0X38
7FBE: FF         RST         0X38
7FBF: FF         RST         0X38
7FC0: FF         RST         0X38
7FC1: FF         RST         0X38
7FC2: FF         RST         0X38
7FC3: FF         RST         0X38
7FC4: FF         RST         0X38
7FC5: FF         RST         0X38
7FC6: FF         RST         0X38
7FC7: FF         RST         0X38
7FC8: FF         RST         0X38
7FC9: FF         RST         0X38
7FCA: FF         RST         0X38
7FCB: FF         RST         0X38
7FCC: FF         RST         0X38
7FCD: FF         RST         0X38
7FCE: FF         RST         0X38
7FCF: FF         RST         0X38
7FD0: FF         RST         0X38
7FD1: FF         RST         0X38
7FD2: FF         RST         0X38
7FD3: FF         RST         0X38
7FD4: FF         RST         0X38
7FD5: FF         RST         0X38
7FD6: FF         RST         0X38
7FD7: FF         RST         0X38
7FD8: FF         RST         0X38
7FD9: FF         RST         0X38
7FDA: FF         RST         0X38
7FDB: FF         RST         0X38
7FDC: FF         RST         0X38
7FDD: FF         RST         0X38
7FDE: FF         RST         0X38
7FDF: FF         RST         0X38
7FE0: FF         RST         0X38
7FE1: FF         RST         0X38
7FE2: FF         RST         0X38
7FE3: FF         RST         0X38
7FE4: FF         RST         0X38
7FE5: FF         RST         0X38
7FE6: FF         RST         0X38
7FE7: FF         RST         0X38
7FE8: FF         RST         0X38
7FE9: FF         RST         0X38
7FEA: FF         RST         0X38
7FEB: FF         RST         0X38
7FEC: FF         RST         0X38
7FED: FF         RST         0X38
7FEE: FF         RST         0X38
7FEF: FF         RST         0X38
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
