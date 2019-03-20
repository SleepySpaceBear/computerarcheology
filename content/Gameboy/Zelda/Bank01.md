![Bank 01](GBZelda.jpg)

# Bank 01

>>> cpu Z80GB

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

```code
4000: FA 96 DB   LD      A,($DB96)       
4003: C7         RST     0X00            
4004: 10 40      STOP    $40             
4006: 41         LD      B,C             
4007: 40         LD      B,B             
4008: 4D         LD      C,L             
4009: 40         LD      B,B             
400A: 65         LD      H,L             
400B: 40         LD      B,B             
400C: 73         LD      (HL),E          
400D: 40         LD      B,B             
400E: FD                              
400F: 55         LD      D,L             
4010: CD CC 1C   CALL    $1CCC           
4013: CD 22 0B   CALL    $0B22           
4016: CD 76 17   CALL    $1776           
4019: FA 6B C1   LD      A,($C16B)       
401C: FE 04      CP      $04             
401E: 20 20      JR      NZ,$4040        
4020: 3E 03      LD      A,$03           
4022: E0 A9      LDFF00  ($A9),A         
4024: 3E 30      LD      A,$30           
4026: E0 AA      LDFF00  ($AA),A         
4028: CD 45 44   CALL    $4445           
402B: AF         XOR     A               
402C: EA BF C1   LD      ($C1BF),A       
402F: EA 4F C1   LD      ($C14F),A       
4032: EA B8 C1   LD      ($C1B8),A       
4035: EA B9 C1   LD      ($C1B9),A       
4038: EA B5 C1   LD      ($C1B5),A       
403B: 3E 0F      LD      A,$0F           
403D: EA FE D6   LD      ($D6FE),A       
4040: C9         RET                     
4041: 3E 0D      LD      A,$0D           
4043: EA FE D6   LD      ($D6FE),A       
4046: AF         XOR     A               
4047: EA 3F C1   LD      ($C13F),A       
404A: C3 45 44   JP      $4445           
404D: 3E 0D      LD      A,$0D           
404F: EA FF D6   LD      ($D6FF),A       
4052: 3E FF      LD      A,$FF           
4054: EA 9A DB   LD      ($DB9A),A       
4057: AF         XOR     A               
4058: E0 96      LDFF00  ($96),A         
405A: E0 97      LDFF00  ($97),A         
405C: EA 6B C1   LD      ($C16B),A       
405F: EA 6C C1   LD      ($C16C),A       
4062: C3 45 44   JP      $4445           
4065: CD C3 17   CALL    $17C3           
4068: FA 6B C1   LD      A,($C16B)       
406B: FE 04      CP      $04             
406D: 20 03      JR      NZ,$4072        
406F: CD 45 44   CALL    $4445           
4072: C9         RET                     
4073: CD EB 40   CALL    $40EB           
4076: F0 CC      LD      A,($CC)         
4078: E6 B0      AND     $B0             
407A: 28 6C      JR      Z,$40E8         
407C: 3E 13      LD      A,$13           
407E: E0 F2      LDFF00  ($F2),A         
4080: FA 3F C1   LD      A,($C13F)       
4083: FE 01      CP      $01             
4085: 28 3B      JR      Z,$40C2         
4087: CD 45 44   CALL    $4445           
408A: AF         XOR     A               
408B: EA 6B C1   LD      ($C16B),A       
408E: EA 6C C1   LD      ($C16C),A       
4091: FA A5 DB   LD      A,($DBA5)       
4094: A7         AND     A               
4095: 28 07      JR      Z,$409E         
4097: AF         XOR     A               
4098: EA 0A C5   LD      ($C50A),A       
409B: EA 16 C1   LD      ($C116),A       
409E: C9         RET                     
409F: AF         XOR     A               
40A0: EA 98 DB   LD      ($DB98),A       
40A3: EA 99 DB   LD      ($DB99),A       
40A6: E0 48      LDFF00  ($48),A         
40A8: E0 49      LDFF00  ($49),A         
40AA: EA 97 DB   LD      ($DB97),A       
40AD: E0 47      LDFF00  ($47),A         
40AF: F0 98      LD      A,($98)         
40B1: EA 9D DB   LD      ($DB9D),A       
40B4: F0 99      LD      A,($99)         
40B6: EA 9E DB   LD      ($DB9E),A       
40B9: CD 2A 51   CALL    $512A           
40BC: 3E 80      LD      A,$80           
40BE: EA C7 DB   LD      ($DBC7),A       
40C1: C9         RET                     
40C2: CD D2 27   CALL    $27D2           
40C5: CD 94 5B   CALL    $5B94           
40C8: CD 85 29   CALL    $2985           
40CB: CD 1A 5F   CALL    $5F1A         
;  
40CE: 3E C7      LD      A,$C7           ; 1100 0111
40D0: E0 40      LDFF00  ($40),A         ; LDCCONT
40D2: EA FD D6   LD      ($D6FD),A       ; ?control mirror?
40D5: 3E 07      LD      A,$07           
40D7: E0 4B      LDFF00  ($4B),A         ; WNDPOSX
40D9: 3E 80      LD      A,$80           
40DB: EA 9A DB   LD      ($DB9A),A       
40DE: E0 4A      LDFF00  ($4A),A         ; WNDPOSY
40E0: 3E 07      LD      A,$07           
40E2: E0 A9      LDFF00  ($A9),A         
40E4: 3E 70      LD      A,$70           
40E6: E0 AA      LDFF00  ($AA),A         
40E8: C9         RET
                     
40E9: 48         LD      C,B             
40EA: 58         LD      E,B             
40EB: 21 3F C1   LD      HL,$C13F        
40EE: CD 2D 6E   CALL    $6E2D           
40F1: F0 CC      LD      A,($CC)         
40F3: E6 4C      AND     $4C             
40F5: 28 05      JR      Z,$40FC         
40F7: 7E         LD      A,(HL)          
40F8: 3C         INC     A               
40F9: E6 01      AND     $01             
40FB: 77         LD      (HL),A          
40FC: 5E         LD      E,(HL)          
40FD: 16 00      LD      D,$00           
40FF: 21 E9 40   LD      HL,$40E9        
4102: 19         ADD     HL,DE           
4103: 7E         LD      A,(HL)          
4104: 21 18 C0   LD      HL,$C018        
4107: 22         LD      (HLI),A         
4108: 3E 24      LD      A,$24           
410A: 22         LD      (HLI),A         
410B: 3E BE      LD      A,$BE           
410D: 22         LD      (HLI),A         
410E: 36 00      LD      (HL),$00        
4110: C9         RET                     
4111: F0 B7      LD      A,($B7)         
4113: A7         AND     A               
4114: C2 7D 41   JP      NZ,$417D        
4117: 1E 70      LD      E,$70           
4119: 3E 00      LD      A,$00           
411B: E0 47      LDFF00  ($47),A         
411D: 00         NOP                     
411E: 00         NOP                     
411F: 00         NOP                     
4120: 00         NOP                     
4121: 00         NOP                     
4122: 00         NOP                     
4123: 00         NOP                     
4124: 00         NOP                     
4125: 00         NOP                     
4126: 00         NOP                     
4127: 00         NOP                     
4128: 00         NOP                     
4129: 00         NOP                     
412A: 00         NOP                     
412B: 00         NOP                     
412C: 00         NOP                     
412D: 00         NOP                     
412E: 00         NOP                     
412F: 00         NOP                     
4130: 00         NOP                     
4131: 00         NOP                     
4132: 00         NOP                     
4133: 00         NOP                     
4134: 00         NOP                     
4135: 00         NOP                     
4136: 00         NOP                     
4137: 00         NOP                     
4138: 00         NOP                     
4139: 00         NOP                     
413A: 00         NOP                     
413B: 1D         DEC     E               
413C: 20 DB      JR      NZ,$4119        
413E: 1E 30      LD      E,$30           
4140: 3E 40      LD      A,$40           
4142: E0 47      LDFF00  ($47),A         
4144: 1D         DEC     E               
4145: 20 F9      JR      NZ,$4140        
4147: 1E 30      LD      E,$30           
4149: 3E 80      LD      A,$80           
414B: E0 47      LDFF00  ($47),A         
414D: 1D         DEC     E               
414E: 20 F9      JR      NZ,$4149        
4150: 1E FF      LD      E,$FF           
4152: 3E C0      LD      A,$C0           
4154: E0 47      LDFF00  ($47),A         
4156: 00         NOP                     
4157: 00         NOP                     
4158: 00         NOP                     
4159: 00         NOP                     
415A: 00         NOP                     
415B: 00         NOP                     
415C: 00         NOP                     
415D: 00         NOP                     
415E: 00         NOP                     
415F: 00         NOP                     
4160: 00         NOP                     
4161: 00         NOP                     
4162: 00         NOP                     
4163: 00         NOP                     
4164: 00         NOP                     
4165: 00         NOP                     
4166: 00         NOP                     
4167: 00         NOP                     
4168: 1D         DEC     E               
4169: 20 E7      JR      NZ,$4152        
416B: 1E 30      LD      E,$30           
416D: 3E 80      LD      A,$80           
416F: E0 47      LDFF00  ($47),A         
4171: 1D         DEC     E               
4172: 20 F9      JR      NZ,$416D        
4174: 1E 30      LD      E,$30           
4176: 3E 40      LD      A,$40           
4178: E0 47      LDFF00  ($47),A         
417A: 1D         DEC     E               
417B: 20 F9      JR      NZ,$4176        
417D: AF         XOR     A               
417E: EA 97 DB   LD      ($DB97),A       
4181: E0 47      LDFF00  ($47),A         
4183: C9         RET                     
4184: F0 9C      LD      A,($9C)         
4186: C7         RST     0X00            
4187: C5         PUSH    BC              
4188: 41         LD      B,C             
4189: 49         LD      C,C             
418A: 42         LD      B,D             
418B: 53         LD      D,E             
418C: 42         LD      B,D             
418D: 7F         LD      A,A             
418E: 42         LD      B,D             
418F: 8E         ADC     A,(HL)          
4190: 42         LD      B,D             
4191: 6A         LD      L,D             
4192: 6A         LD      L,D             
4193: 6A         LD      L,D             
4194: 6A         LD      L,D             
4195: 6A         LD      L,D             
4196: 6A         LD      L,D             
4197: 6A         LD      L,D             
4198: 6A         LD      L,D             
4199: 6A         LD      L,D             
419A: 6A         LD      L,D             
419B: 00         NOP                     
419C: 00         NOP                     
419D: 00         NOP                     
419E: 0A         LD      A,(BC)          
419F: 04         INC     B               
41A0: 06 00      LD      B,$00           
41A2: 0A         LD      A,(BC)          
41A3: 04         INC     B               
41A4: 06 00      LD      B,$00           
41A6: 0A         LD      A,(BC)          
41A7: 04         INC     B               
41A8: 06 1C      LD      B,$1C           
41AA: 1C         INC     E               
41AB: 1C         INC     E               
41AC: 1C         INC     E               
41AD: 1C         INC     E               
41AE: 1C         INC     E               
41AF: 1C         INC     E               
41B0: 1C         INC     E               
41B1: 1C         INC     E               
41B2: 1C         INC     E               
41B3: 1B         DEC     DE              
41B4: 1A         LD      A,(DE)          
41B5: 19         ADD     HL,DE           
41B6: 18 17      JR      $41CF           
41B8: 16 15      LD      D,$15           
41BA: 14         INC     D               
41BB: 13         INC     DE              
41BC: 12         LD      (DE),A          
41BD: 11 10 10   LD      DE,$1010        
41C0: 10 10      STOP    $10             
41C2: 10 10      STOP    $10             
41C4: 10 AF      STOP    $AF             
41C6: EA 55 C1   LD      ($C155),A       
41C9: EA 56 C1   LD      ($C156),A       
41CC: F0 B7      LD      A,($B7)         
41CE: A7         AND     A               
41CF: 20 48      JR      NZ,$4219        
41D1: 3E 10      LD      A,$10           
41D3: E0 B7      LDFF00  ($B7),A         
41D5: 3E 01      LD      A,$01           
41D7: E0 9C      LDFF00  ($9C),A         
41D9: 3E 0F      LD      A,$0F           
41DB: EA FE D6   LD      ($D6FE),A       
41DE: 3E FF      LD      A,$FF           
41E0: E0 9D      LDFF00  ($9D),A         
41E2: FA 57 DB   LD      A,($DB57)       
41E5: C6 01      ADD     $01             
41E7: 27         DAA                     
41E8: EA 57 DB   LD      ($DB57),A       
41EB: FA 58 DB   LD      A,($DB58)       
41EE: CE 00      ADC     $00             
41F0: 27         DAA                     
41F1: EA 58 DB   LD      ($DB58),A       
41F4: FE 10      CP      $10             
41F6: 38 0A      JR      C,$4202         
41F8: 3E 99      LD      A,$99           
41FA: EA 57 DB   LD      ($DB57),A       
41FD: 3E 09      LD      A,$09           
41FF: EA 58 DB   LD      ($DB58),A       
4202: AF         XOR     A               
4203: EA BF C1   LD      ($C1BF),A       
4206: EA 15 D4   LD      ($D415),A       
4209: EA 7C D4   LD      ($D47C),A       
420C: EA 7A D4   LD      ($D47A),A       
420F: EA CB C3   LD      ($C3CB),A       
4212: EA CC C3   LD      ($C3CC),A       
4215: EA CD C3   LD      ($C3CD),A       
4218: C9         RET                     
4219: 1F         RRA                     
421A: 1F         RRA                     
421B: 1F         RRA                     
421C: E6 3F      AND     $3F             
421E: 5F         LD      E,A             
421F: 16 00      LD      D,$00           
4221: 21 91 41   LD      HL,$4191        
4224: 19         ADD     HL,DE           
4225: 7E         LD      A,(HL)          
4226: E0 9D      LDFF00  ($9D),A         
4228: F0 B7      LD      A,($B7)         
422A: 1F         RRA                     
422B: 1F         RRA                     
422C: 1F         RRA                     
422D: E6 1F      AND     $1F             
422F: 5F         LD      E,A             
4230: 21 A9 41   LD      HL,$41A9        
4233: 19         ADD     HL,DE           
4234: 7E         LD      A,(HL)          
4235: EA CD C3   LD      ($C3CD),A       
4238: 3E 01      LD      A,$01           
423A: EA CB C3   LD      ($C3CB),A       
423D: 3E 1C      LD      A,$1C           
423F: EA 98 DB   LD      ($DB98),A       
4242: FA 97 DB   LD      A,($DB97)       
4245: EA 99 DB   LD      ($DB99),A       
4248: C9         RET                     
4249: 3E 0D      LD      A,$0D           
424B: EA FE D6   LD      ($D6FE),A       
424E: 21 9C FF   LD      HL,$FF9C        
4251: 34         INC     (HL)            
4252: C9         RET                     
4253: 3E E4      LD      A,$E4           
4255: EA 97 DB   LD      ($DB97),A       
4258: 3E 0A      LD      A,$0A           
425A: EA FF D6   LD      ($D6FF),A       
425D: 3E FF      LD      A,$FF           
425F: EA 9A DB   LD      ($DB9A),A       
4262: AF         XOR     A               
4263: E0 96      LDFF00  ($96),A         
4265: E0 97      LDFF00  ($97),A         
4267: 21 9C FF   LD      HL,$FF9C        
426A: 34         INC     (HL)            
426B: CD E2 27   CALL    $27E2           
426E: C9         RET                     
426F: 00         NOP                     
4270: FE FD      CP      $FD             
4272: FE 00      CP      $00             
4274: 02         LD      (BC),A          
4275: 03         INC     BC              
4276: 02         LD      (BC),A          
4277: 00         NOP                     
4278: 04         INC     B               
4279: 08 0C 10   LD      ($100C),SP      
427C: 0C         INC     C               
427D: 08 04 F0   LD      ($F004),SP      
4280: B7         OR      A               
4281: A7         AND     A               
4282: 20 09      JR      NZ,$428D        
4284: 21 9C FF   LD      HL,$FF9C        
4287: 34         INC     (HL)            
4288: 3E 03      LD      A,$03           
428A: EA 68 D3   LD      ($D368),A       
428D: C9         RET                     
428E: CD E6 42   CALL    $42E6           
4291: F0 CC      LD      A,($CC)         
4293: E6 B0      AND     $B0             
4295: 28 4B      JR      Z,$42E2         
4297: FA 3F C1   LD      A,($C13F)       
429A: FE 01      CP      $01             
429C: 28 3E      JR      Z,$42DC         
429E: FE 00      CP      $00             
42A0: 28 05      JR      Z,$42A7         
42A2: EA D1 DB   LD      ($DBD1),A       
42A5: 18 03      JR      $42AA           
42A7: CD 94 5B   CALL    $5B94           
42AA: AF         XOR     A               
42AB: 21 80 C2   LD      HL,$C280        
42AE: 1E 10      LD      E,$10           
42B0: 22         LD      (HLI),A         
42B1: 1D         DEC     E               
42B2: 20 FC      JR      NZ,$42B0        
42B4: EA 98 DB   LD      ($DB98),A       
42B7: EA 99 DB   LD      ($DB99),A       
42BA: E0 48      LDFF00  ($48),A         
42BC: E0 49      LDFF00  ($49),A         
42BE: EA 97 DB   LD      ($DB97),A       
42C1: E0 47      LDFF00  ($47),A         
42C3: EA FB D6   LD      ($D6FB),A       
42C6: EA 75 D4   LD      ($D475),A       
42C9: F0 98      LD      A,($98)         
42CB: EA 9D DB   LD      ($DB9D),A       
42CE: F0 99      LD      A,($99)         
42D0: EA 9E DB   LD      ($DB9E),A       
42D3: CD 2A 51   CALL    $512A           
42D6: 3E 80      LD      A,$80           
42D8: EA C7 DB   LD      ($DBC7),A       
42DB: C9         RET                     
42DC: CD 94 5B   CALL    $5B94           
42DF: CD 1A 5F   CALL    $5F1A           
42E2: C9         RET                     
42E3: 50         LD      D,B             
42E4: 60         LD      H,B             
42E5: 70         LD      (HL),B          
42E6: 21 3F C1   LD      HL,$C13F        
42E9: CD 2D 6E   CALL    $6E2D           
42EC: F0 CC      LD      A,($CC)         
42EE: E6 48      AND     $48             
42F0: 28 08      JR      Z,$42FA         
42F2: 7E         LD      A,(HL)          
42F3: 3C         INC     A               
42F4: FE 03      CP      $03             
42F6: 20 01      JR      NZ,$42F9        
42F8: AF         XOR     A               
42F9: 77         LD      (HL),A          
42FA: F0 CC      LD      A,($CC)         
42FC: E6 04      AND     $04             
42FE: 28 09      JR      Z,$4309         
4300: 7E         LD      A,(HL)          
4301: 3D         DEC     A               
4302: FE FF      CP      $FF             
4304: 20 02      JR      NZ,$4308        
4306: 3E 02      LD      A,$02           
4308: 77         LD      (HL),A          
4309: 5E         LD      E,(HL)          
430A: 16 00      LD      D,$00           
430C: 21 E3 42   LD      HL,$42E3        
430F: 19         ADD     HL,DE           
4310: 7E         LD      A,(HL)          
4311: 21 18 C0   LD      HL,$C018        
4314: 22         LD      (HLI),A         
4315: 3E 24      LD      A,$24           
4317: 22         LD      (HLI),A         
4318: 3E BE      LD      A,$BE           
431A: 22         LD      (HLI),A         
431B: 36 00      LD      (HL),$00        
431D: C9         RET                     
431E: FA 96 DB   LD      A,($DB96)       
4321: C7         RST     0X00            
4322: 3F         CCF                     
4323: 43         LD      B,E             
4324: B3         OR      E               
4325: 43         LD      B,E             
4326: 34         INC     (HL)            
4327: 44         LD      B,H             
4328: 4A         LD      C,D             
4329: 44         LD      B,H             
432A: 68         LD      L,B             
432B: 44         LD      B,H             
432C: 6F         LD      L,A             
432D: 44         LD      B,H             
432E: 76         HALT                    
432F: 44         LD      B,H             
4330: 53         LD      D,E             
4331: 0B         DEC     BC              
4332: 00         NOP                     
4333: 00         NOP                     
4334: 00         NOP                     
4335: 00         NOP                     
4336: 00         NOP                     
4337: 00         NOP                     
4338: 30 00      JR      NC,$433A        
433A: 00         NOP                     
433B: 00         NOP                     
433C: 00         NOP                     
433D: 00         NOP                     
433E: 00         NOP                     
433F: CD D2 27   CALL    $27D2           
4342: CD 45 44   CALL    $4445           
4345: FA A5 DB   LD      A,($DBA5)       
4348: A7         AND     A               
4349: 28 51      JR      Z,$439C         
434B: F0 F7      LD      A,($F7)         
434D: 5F         LD      E,A             
434E: CB 27      SET     1,E             
4350: CB 27      SET     1,E             
4352: 83         ADD     A,E             
4353: 5F         LD      E,A             
4354: 16 00      LD      D,$00           
4356: 21 16 DB   LD      HL,$DB16        
4359: 19         ADD     HL,DE           
435A: 11 CC DB   LD      DE,$DBCC        
435D: 0E 05      LD      C,$05           
435F: F0 F7      LD      A,($F7)         
4361: FE 0A      CP      $0A             
4363: F0 F7      LD      A,($F7)         
4365: FE 08      CP      $08             
4367: 28 02      JR      Z,$436B         
4369: 38 03      JR      C,$436E         
436B: AF         XOR     A               
436C: 28 01      JR      Z,$436F         
436E: 2A         LD      A,(HLI)         
436F: 12         LD      (DE),A          
4370: 13         INC     DE              
4371: 0D         DEC     C               
4372: 20 EB      JR      NZ,$435F        
4374: F0 F7      LD      A,($F7)         
4376: 5F         LD      E,A             
4377: 16 00      LD      D,$00           
4379: 21 32 43   LD      HL,$4332        
437C: 19         ADD     HL,DE           
437D: 7E         LD      A,(HL)          
437E: EA B0 DB   LD      ($DBB0),A       
4381: 7B         LD      A,E             
4382: FE 08      CP      $08             
4384: 28 27      JR      Z,$43AD         
4386: FE 0A      CP      $0A             
4388: 30 23      JR      NC,$43AD        
438A: FE 06      CP      $06             
438C: 20 05      JR      NZ,$4393        
438E: F0 F9      LD      A,($F9)         
4390: A7         AND     A               
4391: 20 1A      JR      NZ,$43AD        
4393: CD 57 53   CALL    $5357           
4396: 3E 07      LD      A,$07           
4398: EA FF D6   LD      ($D6FF),A       
439B: C9         RET                     
439C: 3E 02      LD      A,$02           
439E: EA FF D6   LD      ($D6FF),A       
43A1: CD ED 27   CALL    $27ED           
43A4: 21 E7 FF   LD      HL,$FFE7        
43A7: B6         OR      (HL)            
43A8: E6 03      AND     $03             
43AA: E0 B9      LDFF00  ($B9),A         
43AC: C9         RET                     
43AD: 3E 09      LD      A,$09           
43AF: EA FF D6   LD      ($D6FF),A       
43B2: C9         RET                     
43B3: CD 80 29   CALL    $2980           
43B6: AF         XOR     A               
43B7: EA 1C C1   LD      ($C11C),A       
43BA: CD 45 44   CALL    $4445           
43BD: FA 9D DB   LD      A,($DB9D)       
43C0: E0 98      LDFF00  ($98),A         
43C2: EA B1 DB   LD      ($DBB1),A       
43C5: FA 9E DB   LD      A,($DB9E)       
43C8: E0 99      LDFF00  ($99),A         
43CA: EA B2 DB   LD      ($DBB2),A       
43CD: FA C8 DB   LD      A,($DBC8)       
43D0: E0 A2      LDFF00  ($A2),A         
43D2: A7         AND     A               
43D3: 28 05      JR      Z,$43DA         
43D5: 3E 02      LD      A,$02           
43D7: EA 46 C1   LD      ($C146),A       
43DA: 3E 04      LD      A,$04           
43DC: EA 25 C1   LD      ($C125),A       
43DF: CD D7 2E   CALL    $2ED7           
43E2: CD E6 36   CALL    $36E6           
43E5: CD 6B 5D   CALL    $5D6B           
43E8: 3E FF      LD      A,$FF           
43EA: E0 A6      LDFF00  ($A6),A         
43EC: FA A5 DB   LD      A,($DBA5)       
43EF: A7         AND     A               
43F0: 28 34      JR      Z,$4426         
43F2: 57         LD      D,A             
43F3: F0 F7      LD      A,($F7)         
43F5: FE 1A      CP      $1A             
43F7: 30 05      JR      NC,$43FE        
43F9: FE 06      CP      $06             
43FB: 38 01      JR      C,$43FE         
43FD: 14         INC     D               
43FE: F0 F6      LD      A,($F6)         
4400: 5F         LD      E,A             
4401: CD B8 29   CALL    $29B8           
4404: FE 1A      CP      $1A             
4406: 28 0D      JR      Z,$4415         
4408: FE 19      CP      $19             
440A: 28 09      JR      Z,$4415         
440C: FA 8E C1   LD      A,($C18E)       
440F: E6 E0      AND     $E0             
4411: FE 80      CP      $80             
4413: 20 11      JR      NZ,$4426        
4415: FA CD DB   LD      A,($DBCD)       
4418: A7         AND     A               
4419: 28 0B      JR      Z,$4426         
441B: F0 F8      LD      A,($F8)         
441D: E6 10      AND     $10             
441F: 20 05      JR      NZ,$4426        
4421: 3E 0C      LD      A,$0C           
4423: EA 62 D4   LD      ($D462),A       
4426: FA A5 DB   LD      A,($DBA5)       
4429: A7         AND     A               
442A: 3E 06      LD      A,$06           
442C: 20 02      JR      NZ,$4430        
442E: 3E 07      LD      A,$07           
4430: EA FE D6   LD      ($D6FE),A       
4433: C9         RET                     
4434: 3E 0F      LD      A,$0F           
4436: E0 94      LDFF00  ($94),A         
4438: CD AA 09   CALL    $09AA           
443B: AF         XOR     A               
443C: E0 90      LDFF00  ($90),A         
443E: E0 91      LDFF00  ($91),A         
4440: 3E 09      LD      A,$09           
4442: EA FE D6   LD      ($D6FE),A       
4445: 21 96 DB   LD      HL,$DB96        
4448: 34         INC     (HL)            
4449: C9         RET                     
444A: 3E 01      LD      A,$01           
444C: EA FE D6   LD      ($D6FE),A       
444F: FA FA D6   LD      A,($D6FA)       
4452: A7         AND     A               
4453: 28 0F      JR      Z,$4464         
4455: 3E 05      LD      A,$05           
4457: EA F8 D6   LD      ($D6F8),A       
445A: FA CB C1   LD      A,($C1CB)       
445D: A7         AND     A               
445E: 28 04      JR      Z,$4464         
4460: 3E 03      LD      A,$03           
4462: E0 A5      LDFF00  ($A5),A         
4464: CD 45 44   CALL    $4445           
4467: C9         RET                     
4468: CD 6F 3E   CALL    $3E6F           
446B: CD 45 44   CALL    $4445           
446E: C9         RET                     
446F: CD 8A 3E   CALL    $3E8A           
4472: CD 45 44   CALL    $4445           
4475: C9         RET                     
4476: CD 43 56   CALL    $5643           
4479: F0 40      LD      A,($40)         
447B: F6 20      OR      $20             
447D: EA FD D6   LD      ($D6FD),A       
4480: E0 40      LDFF00  ($40),A         
4482: CD 45 44   CALL    $4445           
4485: FA 1C C1   LD      A,($C11C)       
4488: EA 63 D4   LD      ($D463),A       
448B: 3E 04      LD      A,$04           
448D: EA 1C C1   LD      ($C11C),A       
4490: AF         XOR     A               
4491: EA 6B C1   LD      ($C16B),A       
4494: EA 6C C1   LD      ($C16C),A       
4497: FA CB C3   LD      A,($C3CB)       
449A: A7         AND     A               
449B: 28 15      JR      Z,$44B2         
449D: FA AD C5   LD      A,($C5AD)       
44A0: EA 97 DB   LD      ($DB97),A       
44A3: 3E 1C      LD      A,$1C           
44A5: EA 98 DB   LD      ($DB98),A       
44A8: 3E E4      LD      A,$E4           
44AA: EA 99 DB   LD      ($DB99),A       
44AD: 3E 04      LD      A,$04           
44AF: EA 6B C1   LD      ($C16B),A       
44B2: C3 BD 27   JP      $27BD           
44B5: F0 CC      LD      A,($CC)         
44B7: E6 90      AND     $90             
44B9: CA CB 45   JP      Z,$45CB         
44BC: EA 7B D4   LD      ($D47B),A       
44BF: CD B5 27   CALL    $27B5           
44C2: FA 54 A4   LD      A,($A454)       
44C5: EA 80 DB   LD      ($DB80),A       
44C8: CD B5 27   CALL    $27B5           
44CB: FA 55 A4   LD      A,($A455)       
44CE: EA 81 DB   LD      ($DB81),A       
44D1: CD B5 27   CALL    $27B5           
44D4: FA 56 A4   LD      A,($A456)       
44D7: EA 82 DB   LD      ($DB82),A       
44DA: CD B5 27   CALL    $27B5           
44DD: FA 57 A4   LD      A,($A457)       
44E0: EA 83 DB   LD      ($DB83),A       
44E3: CD B5 27   CALL    $27B5           
44E6: FA 58 A4   LD      A,($A458)       
44E9: EA 84 DB   LD      ($DB84),A       
44EC: CD B5 27   CALL    $27B5           
44EF: FA 5F A4   LD      A,($A45F)       
44F2: EA 06 DC   LD      ($DC06),A       
44F5: CD B5 27   CALL    $27B5           
44F8: FA 60 A4   LD      A,($A460)       
44FB: EA 09 DC   LD      ($DC09),A       
44FE: CD B5 27   CALL    $27B5           
4501: FA 5C A4   LD      A,($A45C)       
4504: EA 00 DC   LD      ($DC00),A       
4507: CD B5 27   CALL    $27B5           
450A: FA 5D A4   LD      A,($A45D)       
450D: EA 01 DC   LD      ($DC01),A       
4510: CD B5 27   CALL    $27B5           
4513: FA D9 A7   LD      A,($A7D9)       
4516: EA 85 DB   LD      ($DB85),A       
4519: CD B5 27   CALL    $27B5           
451C: FA DA A7   LD      A,($A7DA)       
451F: EA 86 DB   LD      ($DB86),A       
4522: CD B5 27   CALL    $27B5           
4525: FA DB A7   LD      A,($A7DB)       
4528: EA 87 DB   LD      ($DB87),A       
452B: CD B5 27   CALL    $27B5           
452E: FA DC A7   LD      A,($A7DC)       
4531: EA 88 DB   LD      ($DB88),A       
4534: CD B5 27   CALL    $27B5           
4537: FA DD A7   LD      A,($A7DD)       
453A: EA 89 DB   LD      ($DB89),A       
453D: CD B5 27   CALL    $27B5           
4540: FA E4 A7   LD      A,($A7E4)       
4543: EA 07 DC   LD      ($DC07),A       
4546: CD B5 27   CALL    $27B5           
4549: FA E5 A7   LD      A,($A7E5)       
454C: EA 0A DC   LD      ($DC0A),A       
454F: CD B5 27   CALL    $27B5           
4552: FA E1 A7   LD      A,($A7E1)       
4555: EA 02 DC   LD      ($DC02),A       
4558: CD B5 27   CALL    $27B5           
455B: FA E2 A7   LD      A,($A7E2)       
455E: EA 03 DC   LD      ($DC03),A       
4561: CD B5 27   CALL    $27B5           
4564: FA 5E AB   LD      A,($AB5E)       
4567: EA 8A DB   LD      ($DB8A),A       
456A: CD B5 27   CALL    $27B5           
456D: FA 5F AB   LD      A,($AB5F)       
4570: EA 8B DB   LD      ($DB8B),A       
4573: CD B5 27   CALL    $27B5           
4576: FA 60 AB   LD      A,($AB60)       
4579: EA 8C DB   LD      ($DB8C),A       
457C: CD B5 27   CALL    $27B5           
457F: FA 61 AB   LD      A,($AB61)       
4582: EA 8D DB   LD      ($DB8D),A       
4585: CD B5 27   CALL    $27B5           
4588: FA 62 AB   LD      A,($AB62)       
458B: EA 8E DB   LD      ($DB8E),A       
458E: CD B5 27   CALL    $27B5           
4591: FA 69 AB   LD      A,($AB69)       
4594: EA 08 DC   LD      ($DC08),A       
4597: CD B5 27   CALL    $27B5           
459A: FA 6A AB   LD      A,($AB6A)       
459D: EA 0B DC   LD      ($DC0B),A       
45A0: CD B5 27   CALL    $27B5           
45A3: FA 66 AB   LD      A,($AB66)       
45A6: EA 04 DC   LD      ($DC04),A       
45A9: CD B5 27   CALL    $27B5           
45AC: FA 67 AB   LD      A,($AB67)       
45AF: EA 05 DC   LD      ($DC05),A       
45B2: 3E 02      LD      A,$02           
45B4: EA 95 DB   LD      ($DB95),A       
45B7: AF         XOR     A               
45B8: EA 96 DB   LD      ($DB96),A       
45BB: AF         XOR     A               
45BC: E0 97      LDFF00  ($97),A         
45BE: E0 96      LDFF00  ($96),A         
45C0: 3E 00      LD      A,$00           
45C2: EA 97 DB   LD      ($DB97),A       
45C5: EA 98 DB   LD      ($DB98),A       
45C8: EA 99 DB   LD      ($DB99),A       
45CB: C9         RET                     
45CC: 01 02 03   LD      BC,$0302        
45CF: 04         INC     B               
45D0: 05         DEC     B               
45D1: 06 07      LD      B,$07           
45D3: 08 09 0A   LD      ($0A09),SP      
45D6: 0B         DEC     BC              
45D7: 0C         INC     C               
45D8: 01 01 01   LD      BC,$0101        
45DB: 01 00 01   LD      BC,$0100        
45DE: 01 01 01   LD      BC,$0101        
45E1: 00         NOP                     
45E2: 01 01 01   LD      BC,$0101        
45E5: 01 01 01   LD      BC,$0101        
45E8: 01 01 01   LD      BC,$0101        
45EB: 02         LD      (BC),A          
45EC: 01 01 01   LD      BC,$0101        
45EF: 01 03 01   LD      BC,$0103        
45F2: 01 01 01   LD      BC,$0101        
45F5: 04         INC     B               
45F6: 01 01 01   LD      BC,$0101        
45F9: 01 05 01   LD      BC,$0105        
45FC: 01 01 01   LD      BC,$0101        
45FF: 06 01      LD      B,$01           
4601: 01 01 01   LD      BC,$0101        
4604: 07         RLCA                    
4605: 01 01 01   LD      BC,$0101        
4608: 01 08 01   LD      BC,$0108        
460B: 01 01 01   LD      BC,$0101        
460E: 09         ADD     HL,BC           

460F: 11 00 00   LD      DE,$0000        
4612: CD DD 46   CALL    $46DD           
4615: 11 85 03   LD      DE,$0385        
4618: CD DD 46   CALL    $46DD           
461B: 11 0A 07   LD      DE,$070A        
461E: CD DD 46   CALL    $46DD           
4621: FA 03 00   LD      A,($0003)       
4624: A7         AND     A               
4625: CA DC 46   JP      Z,$46DC         
4628: 1E 00      LD      E,$00           
462A: 16 00      LD      D,$00           
462C: 01 05 A4   LD      BC,$A405        
462F: 21 CC 45   LD      HL,$45CC        
4632: 19         ADD     HL,DE           
4633: 2A         LD      A,(HLI)         
4634: 02         LD      (BC),A          
4635: 03         INC     BC              
4636: 1C         INC     E               
4637: 7B         LD      A,E             
4638: FE 43      CP      $43             
463A: 20 F3      JR      NZ,$462F        
463C: 3E 01      LD      A,$01           
463E: EA 53 A4   LD      ($A453),A       
4641: 3E 01      LD      A,$01           
4643: EA 49 A4   LD      ($A449),A       
4646: 3E 02      LD      A,$02           
4648: EA 48 A4   LD      ($A448),A       
464B: 21 6A A4   LD      HL,$A46A        
464E: 1E 09      LD      E,$09           
4650: 3E 02      LD      A,$02           
4652: 22         LD      (HLI),A         
4653: 1D         DEC     E               
4654: 20 FC      JR      NZ,$4652        
4656: 3E 60      LD      A,$60           
4658: EA 52 A4   LD      ($A452),A       
465B: EA 7D A4   LD      ($A47D),A       
465E: EA 7C A4   LD      ($A47C),A       
4661: EA 4A A4   LD      ($A44A),A       
4664: 3E 40      LD      A,$40           
4666: EA 7B A4   LD      ($A47B),A       
4669: EA 51 A4   LD      ($A451),A       
466C: 3E 89      LD      A,$89           
466E: EA 4C A4   LD      ($A44C),A       
4671: 3E 00      LD      A,$00           
4673: EA 14 A4   LD      ($A414),A       
4676: 3E 07      LD      A,$07           
4678: EA 4E A4   LD      ($A44E),A       
467B: 3E 05      LD      A,$05           
467D: EA 62 A4   LD      ($A462),A       
4680: 3E 09      LD      A,$09           
4682: EA 63 A4   LD      ($A463),A       
4685: 3E 01      LD      A,$01           
4687: EA 4D A4   LD      ($A44D),A       
468A: 3E 50      LD      A,$50           
468C: EA 5F A4   LD      ($A45F),A       
468F: 3E 0A      LD      A,$0A           
4691: EA 60 A4   LD      ($A460),A       
4694: 3E 5B      LD      A,$5B           
4696: EA 54 A4   LD      ($A454),A       
4699: 3E 46      LD      A,$46           
469B: EA 55 A4   LD      ($A455),A       
469E: 3E 4D      LD      A,$4D           
46A0: EA 56 A4   LD      ($A456),A       
46A3: 3E 45      LD      A,$45           
46A5: EA 57 A4   LD      ($A457),A       
46A8: 3E 42      LD      A,$42           
46AA: EA 58 A4   LD      ($A458),A       
46AD: 3E 00      LD      A,$00           
46AF: EA 5C A4   LD      ($A45C),A       
46B2: EA 5D A4   LD      ($A45D),A       
46B5: 3E 00      LD      A,$00           
46B7: EA 5B A4   LD      ($A45B),A       
46BA: EA 64 A4   LD      ($A464),A       
46BD: 3E 00      LD      A,$00           
46BF: EA 65 A4   LD      ($A465),A       
46C2: 3E 92      LD      A,$92           
46C4: EA 66 A4   LD      ($A466),A       
46C7: 3E 48      LD      A,$48           
46C9: EA 67 A4   LD      ($A467),A       
46CC: 3E 62      LD      A,$62           
46CE: EA 68 A4   LD      ($A468),A       
46D1: 21 05 A1   LD      HL,$A105        
46D4: 3E 80      LD      A,$80           
46D6: 1E 00      LD      E,$00           
46D8: 22         LD      (HLI),A         
46D9: 1D         DEC     E               
46DA: 20 FC      JR      NZ,$46D8        
46DC: C9         RET                     

46DD: 0E 01      LD      C,$01           
46DF: 06 05      LD      B,$05           
46E1: 21 00 A1   LD      HL,$A100        
46E4: 19         ADD     HL,DE           
46E5: CD B5 27   CALL    $27B5           
46E8: 2A         LD      A,(HLI)         
46E9: B9         CP      C               
46EA: 20 07      JR      NZ,$46F3        
46EC: 0C         INC     C               
46ED: 0C         INC     C               
46EE: 05         DEC     B               
46EF: 20 F4      JR      NZ,$46E5        
46F1: 18 1D      JR      $4710           ; Out

46F3: 21 00 A1   LD      HL,$A100        
46F6: 19         ADD     HL,DE           
46F7: 3E 01      LD      A,$01           
46F9: CD B5 27   CALL    $27B5           
46FC: 22         LD      (HLI),A         
46FD: 3C         INC     A               
46FE: 3C         INC     A               
46FF: FE 0B      CP      $0B             
4701: 38 F6      JR      C,$46F9         
4703: 11 80 03   LD      DE,$0380        
4706: CD B5 27   CALL    $27B5           
4709: AF         XOR     A               
470A: 22         LD      (HLI),A         
470B: 1B         DEC     DE              
470C: 7B         LD      A,E             
470D: B2         OR      D               
470E: 20 F6      JR      NZ,$4706        
4710: C9         RET                     

4711: CD 6E 5B   CALL    $5B6E           
4714: FA 96 DB   LD      A,($DB96)       
4717: C7         RST     0X00            
4718: 2C         INC     L               
4719: 47         LD      B,A             
471A: 38 47      JR      C,$4763         
471C: 40         LD      B,B             
471D: 47         LD      B,A             
471E: 49         LD      C,C             
471F: 47         LD      B,A             
4720: 4F         LD      C,A             
4721: 47         LD      B,A             
4722: 92         SUB     D               
4723: 47         LD      B,A             
4724: F6 47      OR      $47             
4726: 28 48      JR      Z,$4770         
4728: DE 48      SBC     $48             
472A: 48         LD      C,B             
472B: 49         LD      C,C             
472C: 3E 04      LD      A,$04           
472E: EA FE D6   LD      ($D6FE),A       
4731: AF         XOR     A               
4732: EA 00 D0   LD      ($D000),A       
4735: C3 45 44   JP      $4445           
4738: 3E 08      LD      A,$08           
473A: EA FE D6   LD      ($D6FE),A       
473D: C3 45 44   JP      $4445           
4740: CD 4D 4C   CALL    $4C4D           
4743: CD 66 4C   CALL    $4C66           
4746: C3 45 44   JP      $4445           
4749: CD 7E 4C   CALL    $4C7E           
474C: C3 45 44   JP      $4445           
474F: FA A7 DB   LD      A,($DBA7)       
4752: E6 01      AND     $01             
4754: 28 0E      JR      Z,$4764         
4756: FA 00 DC   LD      A,($DC00)       
4759: 67         LD      H,A             
475A: FA 01 DC   LD      A,($DC01)       
475D: 6F         LD      L,A             
475E: 11 E7 98   LD      DE,$98E7        
4761: CD ED 4D   CALL    $4DED           
4764: FA A7 DB   LD      A,($DBA7)       
4767: E6 02      AND     $02             
4769: 28 0E      JR      Z,$4779         
476B: FA 02 DC   LD      A,($DC02)       
476E: 67         LD      H,A             
476F: FA 03 DC   LD      A,($DC03)       
4772: 6F         LD      L,A             
4773: 11 47 99   LD      DE,$9947        
4776: CD ED 4D   CALL    $4DED           
4779: FA A7 DB   LD      A,($DBA7)       
477C: E6 04      AND     $04             
477E: 28 0E      JR      Z,$478E         
4780: FA 04 DC   LD      A,($DC04)       
4783: 67         LD      H,A             
4784: FA 05 DC   LD      A,($DC05)       
4787: 6F         LD      L,A             
4788: 11 A7 99   LD      DE,$99A7        
478B: CD ED 4D   CALL    $4DED           
478E: C3 45 44   JP      $4445           
4791: C9         RET                     
4792: C3 14 4C   JP      $4C14           
4795: D5         PUSH    DE              
4796: FA 00 D6   LD      A,($D600)       
4799: 5F         LD      E,A             
479A: 16 00      LD      D,$00           
479C: 21 01 D6   LD      HL,$D601        
479F: 19         ADD     HL,DE           
47A0: C6 10      ADD     $10             
47A2: EA 00 D6   LD      ($D600),A       
47A5: 78         LD      A,B             
47A6: 22         LD      (HLI),A         
47A7: 79         LD      A,C             
47A8: 22         LD      (HLI),A         
47A9: 3E 04      LD      A,$04           
47AB: 22         LD      (HLI),A         
47AC: D1         POP     DE              
47AD: D5         PUSH    DE              
47AE: 3E 05      LD      A,$05           
47B0: E0 D7      LDFF00  ($D7),A         
47B2: 1A         LD      A,(DE)          
47B3: A7         AND     A               
47B4: 3E 7E      LD      A,$7E           
47B6: 28 0C      JR      Z,$47C4         
47B8: 1A         LD      A,(DE)          
47B9: 3D         DEC     A               
47BA: C5         PUSH    BC              
47BB: E5         PUSH    HL              
47BC: 4F         LD      C,A             
47BD: 06 00      LD      B,$00           
47BF: CD B1 08   CALL    $08B1           
47C2: E1         POP     HL              
47C3: C1         POP     BC              
47C4: 22         LD      (HLI),A         
47C5: 13         INC     DE              
47C6: F0 D7      LD      A,($D7)         
47C8: 3D         DEC     A               
47C9: 20 E5      JR      NZ,$47B0        
47CB: 78         LD      A,B             
47CC: 22         LD      (HLI),A         
47CD: 79         LD      A,C             
47CE: D6 20      SUB     $20             
47D0: 22         LD      (HLI),A         
47D1: 3E 04      LD      A,$04           
47D3: 22         LD      (HLI),A         
47D4: D1         POP     DE              
47D5: 3E 05      LD      A,$05           
47D7: E0 D7      LDFF00  ($D7),A         
47D9: 1A         LD      A,(DE)          
47DA: A7         AND     A               
47DB: 18 03      JR      $47E0           
47DD: 3D         DEC     A               
47DE: E6 C0      AND     $C0             
47E0: 3E 7E      LD      A,$7E           
47E2: 18 08      JR      $47EC           
47E4: 1A         LD      A,(DE)          
47E5: E6 80      AND     $80             
47E7: 3E C8      LD      A,$C8           
47E9: 28 01      JR      Z,$47EC         
47EB: 3C         INC     A               
47EC: 22         LD      (HLI),A         
47ED: 13         INC     DE              
47EE: F0 D7      LD      A,($D7)         
47F0: 3D         DEC     A               
47F1: 20 E4      JR      NZ,$47D7        
47F3: AF         XOR     A               
47F4: 77         LD      (HL),A          
47F5: C9         RET                     
47F6: FA 7B D4   LD      A,($D47B)       
47F9: A7         AND     A               
47FA: 28 09      JR      Z,$4805         
47FC: AF         XOR     A               
47FD: EA 7B D4   LD      ($D47B),A       
4800: 3E 11      LD      A,$11           
4802: EA 68 D3   LD      ($D368),A       
4805: FA A7 DB   LD      A,($DBA7)       
4808: A7         AND     A               
4809: 3E 03      LD      A,$03           
480B: 28 02      JR      Z,$480F         
480D: 3E 04      LD      A,$04           
480F: EA FF D6   LD      ($D6FF),A       
4812: 3E E4      LD      A,$E4           
4814: EA 97 DB   LD      ($DB97),A       
4817: 3E 1C      LD      A,$1C           
4819: EA 98 DB   LD      ($DB98),A       
481C: 3E E4      LD      A,$E4           
481E: EA 99 DB   LD      ($DB99),A       
4821: C3 45 44   JP      $4445           
4824: 3B         DEC     SP              
4825: 53         LD      D,E             
4826: 6B         LD      L,E             
4827: 83         ADD     A,E             
4828: CD 2D 6E   CALL    $6E2D           
482B: F0 CC      LD      A,($CC)         
482D: E6 90      AND     $90             
482F: 28 03      JR      Z,$4834         
4831: C3 45 44   JP      $4445           
4834: F0 CC      LD      A,($CC)         
4836: E6 4C      AND     $4C             
4838: 28 2A      JR      Z,$4864         
483A: 0E 02      LD      C,$02           
483C: FA A7 DB   LD      A,($DBA7)       
483F: A7         AND     A               
4840: 28 01      JR      Z,$4843         
4842: 0C         INC     C               
4843: F0 CC      LD      A,($CC)         
4845: CB 77      SET     1,E             
4847: 20 04      JR      NZ,$484D        
4849: CB 57      SET     1,E             
484B: 20 0C      JR      NZ,$4859        
484D: FA A6 DB   LD      A,($DBA6)       
4850: C6 01      ADD     $01             
4852: 0C         INC     C               
4853: B9         CP      C               
4854: 38 0B      JR      C,$4861         
4856: AF         XOR     A               
4857: 18 08      JR      $4861           
4859: FA A6 DB   LD      A,($DBA6)       
485C: D6 01      SUB     $01             
485E: 30 01      JR      NC,$4861        
4860: 79         LD      A,C             
4861: EA A6 DB   LD      ($DBA6),A       
4864: FA A6 DB   LD      A,($DBA6)       
4867: FE 03      CP      $03             
4869: 20 2D      JR      NZ,$4898        
486B: F0 CC      LD      A,($CC)         
486D: E6 03      AND     $03             
486F: 28 0B      JR      Z,$487C         
4871: CD 33 6E   CALL    $6E33           
4874: FA 00 D0   LD      A,($D000)       
4877: EE 01      XOR     $01             
4879: EA 00 D0   LD      ($D000),A       
487C: F0 E7      LD      A,($E7)         
487E: E6 10      AND     $10             
4880: 20 16      JR      NZ,$4898        
4882: FA 00 D0   LD      A,($D000)       
4885: A7         AND     A               
4886: 3E 2C      LD      A,$2C           
4888: 28 02      JR      Z,$488C         
488A: 3E 64      LD      A,$64           
488C: 21 08 C0   LD      HL,$C008        
488F: 36 88      LD      (HL),$88        
4891: 23         INC     HL              
4892: 22         LD      (HLI),A         
4893: 3E BE      LD      A,$BE           
4895: 22         LD      (HLI),A         
4896: AF         XOR     A               
4897: 77         LD      (HL),A          
4898: FA A6 DB   LD      A,($DBA6)       
489B: 5F         LD      E,A             
489C: 16 00      LD      D,$00           
489E: 21 24 48   LD      HL,$4824        
48A1: 19         ADD     HL,DE           
48A2: F0 E7      LD      A,($E7)         
48A4: E6 08      AND     $08             
48A6: 28 1B      JR      Z,$48C3         
48A8: 7E         LD      A,(HL)          
48A9: 21 00 C0   LD      HL,$C000        
48AC: F5         PUSH    AF              
48AD: 22         LD      (HLI),A         
48AE: 3E 18      LD      A,$18           
48B0: 22         LD      (HLI),A         
48B1: 3E 00      LD      A,$00           
48B3: 22         LD      (HLI),A         
48B4: 3E 00      LD      A,$00           
48B6: 22         LD      (HLI),A         
48B7: F1         POP     AF              
48B8: 22         LD      (HLI),A         
48B9: 3E 20      LD      A,$20           
48BB: 22         LD      (HLI),A         
48BC: 3E 02      LD      A,$02           
48BE: 22         LD      (HLI),A         
48BF: 3E 00      LD      A,$00           
48C1: 77         LD      (HL),A          
48C2: C9         RET                     
48C3: 7E         LD      A,(HL)          
48C4: 21 00 C0   LD      HL,$C000        
48C7: F5         PUSH    AF              
48C8: 22         LD      (HLI),A         
48C9: 3E 18      LD      A,$18           
48CB: 22         LD      (HLI),A         
48CC: 3E 02      LD      A,$02           
48CE: 22         LD      (HLI),A         
48CF: 3E 20      LD      A,$20           
48D1: 22         LD      (HLI),A         
48D2: F1         POP     AF              
48D3: 22         LD      (HLI),A         
48D4: 3E 20      LD      A,$20           
48D6: 22         LD      (HLI),A         
48D7: 3E 00      LD      A,$00           
48D9: 22         LD      (HLI),A         
48DA: 3E 20      LD      A,$20           
48DC: 77         LD      (HL),A          
48DD: C9         RET                     
48DE: FA A6 DB   LD      A,($DBA6)       
48E1: FE 03      CP      $03             
48E3: 28 3D      JR      Z,$4922         
48E5: FA A6 DB   LD      A,($DBA6)       
48E8: 5F         LD      E,A             
48E9: CB 27      SET     1,E             
48EB: CB 27      SET     1,E             
48ED: 83         ADD     A,E             
48EE: 5F         LD      E,A             
48EF: 16 00      LD      D,$00           
48F1: 0E 05      LD      C,$05           
48F3: 21 80 DB   LD      HL,$DB80        
48F6: 19         ADD     HL,DE           
48F7: 2A         LD      A,(HLI)         
48F8: A7         AND     A               
48F9: 20 11      JR      NZ,$490C        
48FB: 0D         DEC     C               
48FC: 20 F9      JR      NZ,$48F7        
48FE: AF         XOR     A               
48FF: EA 

4890: 96 DB      ; 10010110
                 ; 11011011
4902: 3E 03      ; 00111110
                 ; 00000011      
4904: EA 95 
4906: DB 3E 
4908: 13 E0 
490A: F2 C9                        
490C: CD 07 
490E: 49 3E 

4910: 00      LD      A,$00           
4911: EA 97 DB   LD      ($DB97),A       
4914: EA 98 DB   LD      ($DB98),A       
4917: EA 99 DB   LD      ($DB99),A       
491A: 3E 05      LD      A,$05           
491C: EA FE D6   LD      ($D6FE),A       
491F: C3 45 44   JP      $4445           
4922: AF         XOR     A               
4923: EA 96 DB   LD      ($DB96),A       
4926: FA 00 D0   LD      A,($D000)       
4929: A7         AND     A               
492A: 3E 04      LD      A,$04           
492C: 28 02      JR      Z,$4930         
492E: 3E 05      LD      A,$05           
4930: EA 95 DB   LD      ($DB95),A       
4933: C3 07 49   JP      $4907           
4936: 05         DEC     B               
4937: A4         AND     H               
4938: 8A         ADC     A,D             
4939: A7         AND     A               
493A: 0F         RRCA                    
493B: AB         XOR     E               
493C: 05         DEC     B               
493D: A1         AND     C               
493E: 8A         ADC     A,D             
493F: A4         AND     H               
4940: 0F         RRCA                    
4941: A8         XOR     B               
4942: 00         NOP                     
4943: A1         AND     C               
4944: 85         ADD     A,L             
4945: A4         AND     H               
4946: 0A         LD      A,(BC)          
4947: A8         XOR     B               
4948: C3 2A 51   JP      $512A           
494B: FA 96 DB   LD      A,($DB96)       
494E: C7         RST     0X00            
494F: 55         LD      D,L             
4950: 49         LD      C,C             
4951: 68         LD      L,B             
4952: 49         LD      C,C             
4953: 86         ADD     A,(HL)          
4954: 49         LD      C,C             
4955: CD 45 44   CALL    $4445           
4958: 3E 08      LD      A,$08           
495A: EA FE D6   LD      ($D6FE),A       
495D: AF         XOR     A               
495E: EA A8 DB   LD      ($DBA8),A       
4961: EA A9 DB   LD      ($DBA9),A       
4964: EA AA DB   LD      ($DBAA),A       
4967: C9         RET                     
4968: 3E 05      LD      A,$05           
496A: EA FF D6   LD      ($D6FF),A       
496D: 21 01 D6   LD      HL,$D601        
4970: 3E 98      LD      A,$98           
4972: 22         LD      (HLI),A         
4973: 3E 48      LD      A,$48           
4975: 22         LD      (HLI),A         
4976: AF         XOR     A               
4977: 22         LD      (HLI),A         
4978: FA A6 DB   LD      A,($DBA6)       
497B: C6 AB      ADD     $AB             
497D: 22         LD      (HLI),A         
497E: AF         XOR     A               
497F: 77         LD      (HL),A          
4980: C3 45 44   JP      $4445           
4983: 00         NOP                     
4984: 05         DEC     B               
4985: 0A         LD      A,(BC)          
4986: FA A6 DB   LD      A,($DBA6)       
4989: 5F         LD      E,A             
498A: 16 00      LD      D,$00           
498C: 21 83 49   LD      HL,$4983        
498F: 19         ADD     HL,DE           
4990: 5E         LD      E,(HL)          
4991: 21 80 DB   LD      HL,$DB80        
4994: 19         ADD     HL,DE           
4995: E5         PUSH    HL              
4996: D1         POP     DE              
4997: 01 49 98   LD      BC,$9849        
499A: CD 95 47   CALL    $4795           
499D: F0 CC      LD      A,($CC)         
499F: E6
 
49A0: 80            
49A1: 28 71      JR      Z,$4A14         
49A3: CD 07 49   CALL    $4907           
49A6: FA A6 DB   LD      A,($DBA6)       
49A9: CB 27      SET     1,E             
49AB: 5F         LD      E,A             
49AC: 16 00      LD      D,$00           
49AE: 21 36 

49B0: 49        
49B1: 19         ADD     HL,DE           
49B2: 2A         LD      A,(HLI)         
49B3: 66         LD      H,(HL)          
49B4: 6F         LD      L,A             
49B5: E5         PUSH    HL              
49B6: 11 4F 00   LD      DE,$004F        
49B9: 19         ADD     HL,DE           
49BA: E5         PUSH    HL              
49BB: FA A6 DB   LD      A,($DBA6)       
49BE: 5F         LD      E,A             
49BF: CB 

49C0: 27             
49C1: CB 27      SET     1,E             
49C3: 83         ADD     A,E             
49C4: 5F         LD      E,A             
49C5: 16 00      LD      D,$00           
49C7: 21 80 DB   LD      HL,$DB80        
49CA: 19         ADD     HL,DE           
49CB: 2A         LD      A,(HLI)         
49CC: FE 5B      CP      $5B             
49CE: 20 19      JR      NZ,$49E9    
    
49D0: 2A         LD      A,(HLI)         
49D1: FE 46      CP      $46             
49D3: 20 14      JR      NZ,$49E9        
49D5: 2A         LD      A,(HLI)         
49D6: FE 4D      CP      $4D             
49D8: 20 0F      JR      NZ,$49E9        
49DA: 2A         LD      A,(HLI)         
49DB: FE 45      CP      $45             
49DD: 20 0A      JR      NZ,$49E9        
49DF: 2A         LD      A,(HLI)         
49E0: FE 42      CP      $42             
49E2: 20 05      JR      NZ,$49E9        
49E4: 3E 60      LD      A,$60           
49E6: EA 68 D3   LD      ($D368),A       
49E9: 21 80 DB   LD      HL,$DB80        
49EC: 19         ADD     HL,DE           
49ED: C1         POP     BC              
49EE: 1E 05      LD      E,$05           
49F0: CD B5 27   CALL    $27B5           
49F3: 2A         LD      A,(HLI)         
49F4: 02         LD      (BC),A          
49F5: 03         INC     BC              
49F6: 1D         DEC     E               
49F7: 20 F7      JR      NZ,$49F0        
49F9: E1         POP     HL              
49FA: E5         PUSH    HL              
49FB: 11 5A 00   LD      DE,$005A        
49FE: 19         ADD     HL,DE           
49FF: 36 18      LD      (HL),$18        
4A01: E1         POP     HL              
4A02: E5         PUSH    HL              
4A03: 11 5B 00   LD      DE,$005B        
4A06: 19         ADD     HL,DE           
4A07: 36 03      LD      (HL),$03        
4A09: E1         POP     HL              
4A0A: 11 57 00   LD      DE,$0057        
4A0D: 19         ADD     HL,DE           
4A0E: AF         XOR     A               
4A0F: 22         LD      (HLI),A         
4A10: 77         LD      (HL),A          
4A11: C3 BF 44   JP      $44BF           
4A14: CD E0 4A   CALL    $4AE0           
4A17: CD 75 4B   CALL    $4B75           
4A1A: C9         RET                     
4A1B: 38 38      JR      C,$4A55         
4A1D: 38 38      JR      C,$4A57         
4A1F: 38 38      JR      C,$4A59         
4A21: 38 38      JR      C,$4A5B         
4A23: 38 38      JR      C,$4A5D         
4A25: 38 38      JR      C,$4A5F         
4A27: 38 38      JR      C,$4A61         
4A29: 38 38      JR      C,$4A63         
4A2B: 48         LD      C,B             
4A2C: 48         LD      C,B             
4A2D: 48         LD      C,B             
4A2E: 48         LD      C,B             
4A2F: 48         LD      C,B             
4A30: 48         LD      C,B             
4A31: 48         LD      C,B             
4A32: 48         LD      C,B             
4A33: 48         LD      C,B             
4A34: 48         LD      C,B             
4A35: 48         LD      C,B             
4A36: 48         LD      C,B             
4A37: 48         LD      C,B             
4A38: 48         LD      C,B             
4A39: 48         LD      C,B             
4A3A: 48         LD      C,B             
4A3B: 58         LD      E,B             
4A3C: 58         LD      E,B             
4A3D: 58         LD      E,B             
4A3E: 58         LD      E,B             
4A3F: 58         LD      E,B             
4A40: 58         LD      E,B             
4A41: 58         LD      E,B             
4A42: 58         LD      E,B             
4A43: 58         LD      E,B             
4A44: 58         LD      E,B             
4A45: 58         LD      E,B             
4A46: 58         LD      E,B             
4A47: 58         LD      E,B             
4A48: 58         LD      E,B             
4A49: 58         LD      E,B             
4A4A: 58         LD      E,B             
4A4B: 68         LD      L,B             
4A4C: 68         LD      L,B             
4A4D: 68         LD      L,B             
4A4E: 68         LD      L,B             
4A4F: 68         LD      L,B             
4A50: 68         LD      L,B             
4A51: 68         LD      L,B             
4A52: 68         LD      L,B             
4A53: 68         LD      L,B             
4A54: 68         LD      L,B             
4A55: 68         LD      L,B             
4A56: 68         LD      L,B             
4A57: 68         LD      L,B             
4A58: 68         LD      L,B             
4A59: 68         LD      L,B             
4A5A: 68         LD      L,B             
4A5B: 14         INC     D               
4A5C: 1C         INC     E               
4A5D: 24         INC     H               
4A5E: 2C         INC     L               
4A5F: 34         INC     (HL)            
4A60: 3C         INC     A               
4A61: 44         LD      B,H             
4A62: 4C         LD      C,H             
4A63: 54         LD      D,H             
4A64: 5C         LD      E,H             
4A65: 64         LD      H,H             
4A66: 6C         LD      L,H             
4A67: 74         LD      (HL),H          
4A68: 7C         LD      A,H             
4A69: 84         ADD     A,H             
4A6A: 8C         ADC     A,H             
4A6B: 14         INC     D               
4A6C: 1C         INC     E               
4A6D: 24         INC     H               
4A6E: 2C         INC     L               
4A6F: 34         INC     (HL)            
4A70: 3C         INC     A               
4A71: 44         LD      B,H             
4A72: 4C         LD      C,H             
4A73: 54         LD      D,H             
4A74: 5C         LD      E,H             
4A75: 64         LD      H,H             
4A76: 6C         LD      L,H             
4A77: 74         LD      (HL),H          
4A78: 7C         LD      A,H             
4A79: 84         ADD     A,H             
4A7A: 8C         ADC     A,H             
4A7B: 14         INC     D               
4A7C: 1C         INC     E               
4A7D: 24         INC     H               
4A7E: 2C         INC     L               
4A7F: 34         INC     (HL)            
4A80: 3C         INC     A               
4A81: 44         LD      B,H             
4A82: 4C         LD      C,H             
4A83: 54         LD      D,H             
4A84: 5C         LD      E,H             
4A85: 64         LD      H,H             
4A86: 6C         LD      L,H             
4A87: 74         LD      (HL),H          
4A88: 7C         LD      A,H             
4A89: 84         ADD     A,H             
4A8A: 8C         ADC     A,H             
4A8B: 14         INC     D               
4A8C: 1C         INC     E               
4A8D: 24         INC     H               
4A8E: 2C         INC     L               
4A8F: 34         INC     (HL)            
4A90: 3C         INC     A               
4A91: 44         LD      B,H             
4A92: 4C         LD      C,H             
4A93: 54         LD      D,H             
4A94: 5C         LD      E,H             
4A95: 64         LD      H,H             
4A96: 6C         LD      L,H             
4A97: 74         LD      (HL),H          
4A98: 7C         LD      A,H             
4A99: 84         ADD     A,H             
4A9A: 8C         ADC     A,H             
4A9B: 4C         LD      C,H             
4A9C: 54         LD      D,H             
4A9D: 5C         LD      E,H             
4A9E: 64         LD      H,H             
4A9F: 6C         LD      L,H             
4AA0: 42         LD      B,D             
4AA1: 43         LD      B,E             
4AA2: 44         LD      B,H             
4AA3: 45         LD      B,L             
4AA4: 46         LD      B,(HL)          
4AA5: 47         LD      B,A             
4AA6: 48         LD      C,B             
4AA7: 00         NOP                     
4AA8: 00         NOP                     
4AA9: 62         LD      H,D             
4AAA: 63         LD      H,E             
4AAB: 64         LD      H,H             
4AAC: 65         LD      H,L             
4AAD: 66         LD      H,(HL)          
4AAE: 67         LD      H,A             
4AAF: 68         LD      L,B             
4AB0: 49         LD      C,C             
4AB1: 4A         LD      C,D             
4AB2: 4B         LD      C,E             
4AB3: 4C         LD      C,H             
4AB4: 4D         LD      C,L             
4AB5: 4E         LD      C,(HL)          
4AB6: 4F         LD      C,A             
4AB7: 00         NOP                     
4AB8: 00         NOP                     
4AB9: 69         LD      L,C             
4ABA: 6A         LD      L,D             
4ABB: 6B         LD      L,E             
4ABC: 6C         LD      L,H             
4ABD: 6D         LD      L,L             
4ABE: 6E         LD      L,(HL)          
4ABF: 6F         LD      L,A             
4AC0: 50         LD      D,B             
4AC1: 51         LD      D,C             
4AC2: 52         LD      D,D             
4AC3: 53         LD      D,E             
4AC4: 54         LD      D,H             
4AC5: 55         LD      D,L             
4AC6: 56         LD      D,(HL)          
4AC7: 00         NOP                     
4AC8: 00         NOP                     
4AC9: 70         LD      (HL),B          
4ACA: 71         LD      (HL),C          
4ACB: 72         LD      (HL),D          
4ACC: 73         LD      (HL),E          
4ACD: 74         LD      (HL),H          
4ACE: 75         LD      (HL),L          
4ACF: 76         HALT                    
4AD0: 57         LD      D,A             
4AD1: 58         LD      E,B             
4AD2: 59         LD      E,C             
4AD3: 5A         LD      E,D             
4AD4: 5B         LD      E,E             
4AD5: 00         NOP                     
4AD6: 00         NOP                     
4AD7: 00         NOP                     
4AD8: 00         NOP                     
4AD9: 77         LD      (HL),A          
4ADA: 78         LD      A,B             
4ADB: 79         LD      A,C             
4ADC: 7A         LD      A,D             
4ADD: 7B         LD      A,E             
4ADE: 00         NOP                     
4ADF: 00         NOP                     
4AE0: F0 CC      LD      A,($CC)         
4AE2: E0 D7      LDFF00  ($D7),A         
4AE4: F0 D7      LD      A,($D7)         
4AE6: E6 0C      AND     $0C             
4AE8: 20 42      JR      NZ,$4B2C        
4AEA: F0 D7      LD      A,($D7)         
4AEC: E6 03      AND     $03             
4AEE: 20 1C      JR      NZ,$4B0C        
4AF0: F0 CB      LD      A,($CB)         
4AF2: 21 82 C1   LD      HL,$C182        
4AF5: E6 0F      AND     $0F             
4AF7: 20 04      JR      NZ,$4AFD        
4AF9: AF         XOR     A               
4AFA: 77         LD      (HL),A          
4AFB: 18 0D      JR      $4B0A           
4AFD: 7E         LD      A,(HL)          
4AFE: 3C         INC     A               
4AFF: 77         LD      (HL),A          
4B00: FE 18      CP      $18             
4B02: 20 06      JR      NZ,$4B0A        
4B04: 36 15      LD      (HL),$15        
4B06: F0 CB      LD      A,($CB)         
4B08: 18 D8      JR      $4AE2           
4B0A: 18 42      JR      $4B4E           
4B0C: CD 33 6E   CALL    $6E33           
4B0F: CB 4F      SET     1,E             
4B11: 20 0C      JR      NZ,$4B1F        
4B13: FA A9 DB   LD      A,($DBA9)       
4B16: C6 01      ADD     $01             
4B18: FE 40      CP      $40             
4B1A: 38 2D      JR      C,$4B49         
4B1C: AF         XOR     A               
4B1D: 18 2A      JR      $4B49           
4B1F: FA A9 DB   LD      A,($DBA9)       
4B22: D6 01      SUB     $01             
4B24: FE FF      CP      $FF             
4B26: 20 21      JR      NZ,$4B49        
4B28: 3E 3F      LD      A,$3F           
4B2A: 18 1D      JR      $4B49           
4B2C: CD 33 6E   CALL    $6E33           
4B2F: CB 57      SET     1,E             
4B31: 28 0B      JR      Z,$4B3E         
4B33: FA A9 DB   LD      A,($DBA9)       
4B36: D6 10      SUB     $10             
4B38: 30 0F      JR      NC,$4B49        
4B3A: C6 40      ADD     $40             
4B3C: 18 0B      JR      $4B49           
4B3E: FA A9 DB   LD      A,($DBA9)       
4B41: C6 10      ADD     $10             
4B43: FE 40      CP      $40             
4B45: 38 02      JR      C,$4B49         
4B47: D6 40      SUB     $40             
4B49: EA A9 DB   LD      ($DBA9),A       
4B4C: 18 00      JR      $4B4E           
4B4E: FA A9 DB   LD      A,($DBA9)       
4B51: 21 5B 4A   LD      HL,$4A5B        
4B54: 4F         LD      C,A             
4B55: 06 00      LD      B,$00           
4B57: 09         ADD     HL,BC           
4B58: 5E         LD      E,(HL)          
4B59: FA A9 DB   LD      A,($DBA9)       
4B5C: 21 1B 4A   LD      HL,$4A1B        
4B5F: 4F         LD      C,A             
4B60: 06 00      LD      B,$00           
4B62: 09         ADD     HL,BC           
4B63: 56         LD      D,(HL)          
4B64: 21 00 C0   LD      HL,$C000        
4B67: 7A         LD      A,D             
4B68: C6 0B      ADD     $0B             
4B6A: 22         LD      (HLI),A         
4B6B: 7B         LD      A,E             
4B6C: C6 04      ADD     $04             
4B6E: 22         LD      (HLI),A         
4B6F: 3E E0      LD      A,$E0           
4B71: 22         LD      (HLI),A         
4B72: AF         XOR     A               
4B73: 77         LD      (HL),A          
4B74: C9         RET                     
4B75: F0 CC      LD      A,($CC)         
4B77: E6 30      AND     $30             
4B79: 28 27      JR      Z,$4BA2         
4B7B: CB 6F      SET     1,E             
4B7D: 20 13      JR      NZ,$4B92        
4B7F: CD 07 49   CALL    $4907           
4B82: CD C5 4B   CALL    $4BC5           
4B85: FA AA DB   LD      A,($DBAA)       
4B88: C6 01      ADD     $01             
4B8A: FE 05      CP      $05             
4B8C: 38 11      JR      C,$4B9F         
4B8E: 3E 04      LD      A,$04           
4B90: 18 0D      JR      $4B9F           
4B92: CD 07 49   CALL    $4907           
4B95: FA AA DB   LD      A,($DBAA)       
4B98: D6 01      SUB     $01             
4B9A: FE FF      CP      $FF             
4B9C: 20 01      JR      NZ,$4B9F        
4B9E: AF         XOR     A               
4B9F: EA AA DB   LD      ($DBAA),A       
4BA2: FA AA DB   LD      A,($DBAA)       
4BA5: 21 9B 4A   LD      HL,$4A9B        
4BA8: 4F         LD      C,A             
4BA9: 06 00      LD      B,$00           
4BAB: 09         ADD     HL,BC           
4BAC: 5E         LD      E,(HL)          
4BAD: F0 E7      LD      A,($E7)         
4BAF: E6 10      AND     $10             
4BB1: 28 11      JR      Z,$4BC4         
4BB3: 21 04 C0   LD      HL,$C004        
4BB6: 3E 18      LD      A,$18           
4BB8: C6 0B      ADD     $0B             
4BBA: 22         LD      (HLI),A         
4BBB: 7B         LD      A,E             
4BBC: C6 04      ADD     $04             
4BBE: 22         LD      (HLI),A         
4BBF: 3E E0      LD      A,$E0           
4BC1: 22         LD      (HLI),A         
4BC2: AF         XOR     A               
4BC3: 77         LD      (HL),A          
4BC4: C9         RET                     
4BC5: FA A9 DB   LD      A,($DBA9)       
4BC8: 4F         LD      C,A             
4BC9: 06 00      LD      B,$00           
4BCB: 21 A0 4A   LD      HL,$4AA0        
4BCE: 09         ADD     HL,BC           
4BCF: 7E         LD      A,(HL)          
4BD0: 5F         LD      E,A             
4BD1: FA A6 DB   LD      A,($DBA6)       
4BD4: 4F         LD      C,A             
4BD5: CB 27      SET     1,E             
4BD7: CB 27      SET     1,E             
4BD9: 81         ADD     A,C             
4BDA: 4F         LD      C,A             
4BDB: 21 80 DB   LD      HL,$DB80        
4BDE: 09         ADD     HL,BC           
4BDF: FA AA DB   LD      A,($DBAA)       
4BE2: 4F         LD      C,A             
4BE3: 09         ADD     HL,BC           
4BE4: 73         LD      (HL),E          
4BE5: C9         RET                     
4BE6: CD 6E 5B   CALL    $5B6E           
4BE9: FA 96 DB   LD      A,($DB96)       
4BEC: C7         RST     0X00            
4BED: FD                              
4BEE: 4B         LD      C,E             
4BEF: 0C         INC     C               
4BF0: 4C         LD      C,H             
4BF1: 14         INC     D               
4BF2: 4C         LD      C,H             
4BF3: 20 4C      JR      NZ,$4C41        
4BF5: 29         ADD     HL,HL           
4BF6: 4C         LD      C,H             
4BF7: 2F         CPL                     
4BF8: 4C         LD      C,H             
4BF9: AE         XOR     (HL)            
4BFA: 4C         LD      C,H             
4BFB: 13         INC     DE              
4BFC: 4D         LD      C,L             
4BFD: 3E 08      LD      A,$08           
4BFF: EA FE D6   LD      ($D6FE),A       
4C02: AF         XOR     A               
4C03: EA A6 DB   LD      ($DBA6),A       
4C06: EA 00 D0   LD      ($D000),A       
4C09: C3 45 44   JP      $4445           
4C0C: 3E 06      LD      A,$06           
4C0E: EA FF D6   LD      ($D6FF),A       
4C11: C3 45 44   JP      $4445           
4C14: CD 32 4C   CALL    $4C32           
4C17: CD 3B 4C   CALL    $4C3B           
4C1A: CD 44 4C   CALL    $4C44           
4C1D: C3 45 44   JP      $4445           
4C20: CD 4D 4C   CALL    $4C4D           
4C23: CD 66 4C   CALL    $4C66           
4C26: C3 45 44   JP      $4445           
4C29: CD 7E 4C   CALL    $4C7E           
4C2C: C3 45 44   JP      $4445           
4C2F: C3 4F 47   JP      $474F           
4C32: 01 C5 98   LD      BC,$98C5        
4C35: 11 80 DB   LD      DE,$DB80        
4C38: C3 95 47   JP      $4795           
4C3B: 01 25 99   LD      BC,$9925        
4C3E: 11 85 DB   LD      DE,$DB85        
4C41: C3 95 47   JP      $4795           
4C44: 01 85 99   LD      BC,$9985        
4C47: 11 8A DB   LD      DE,$DB8A        
4C4A: C3 95 47   JP      $4795           
4C4D: FA A7 DB   LD      A,($DBA7)       
4C50: E6 01      AND     $01             
4C52: 28 11      JR      Z,$4C65         
4C54: 3E 00      LD      A,$00           
4C56: E0 DB      LDFF00  ($DB),A         
4C58: FA 06 DC   LD      A,($DC06)       
4C5B: E0 D9      LDFF00  ($D9),A         
4C5D: FA 09 DC   LD      A,($DC09)       
4C60: E0 DA      LDFF00  ($DA),A         
4C62: C3 01 5B   JP      $5B01           
4C65: C9         RET                     
4C66: FA A7 DB   LD      A,($DBA7)       
4C69: E6 02      AND     $02             
4C6B: 28 F8      JR      Z,$4C65         
4C6D: 3E 01      LD      A,$01           
4C6F: E0 DB      LDFF00  ($DB),A         
4C71: FA 07 DC   LD      A,($DC07)       
4C74: E0 D9      LDFF00  ($D9),A         
4C76: FA 0A DC   LD      A,($DC0A)       
4C79: E0 DA      LDFF00  ($DA),A         
4C7B: C3 01 5B   JP      $5B01           
4C7E: FA A7 DB   LD      A,($DBA7)       
4C81: E6 04      AND     $04             
4C83: 28 E0      JR      Z,$4C65         
4C85: 3E 02      LD      A,$02           
4C87: E0 DB      LDFF00  ($DB),A         
4C89: FA 08 DC   LD      A,($DC08)       
4C8C: E0 D9      LDFF00  ($D9),A         
4C8E: FA 0B DC   LD      A,($DC0B)       
4C91: E0 DA      LDFF00  ($DA),A         
4C93: C3 01 5B   JP      $5B01           
4C96: 98         SBC     B               
4C97: A5         AND     L               
4C98: 44         LD      B,H             
4C99: 7E         LD      A,(HL)          
4C9A: 98         SBC     B               
4C9B: C5         PUSH    BC              
4C9C: 44         LD      B,H             
4C9D: 7E         LD      A,(HL)          
4C9E: 99         SBC     C               
4C9F: 05         DEC     B               
4CA0: 44         LD      B,H             
4CA1: 7E         LD      A,(HL)          
4CA2: 99         SBC     C               
4CA3: 25         DEC     H               
4CA4: 44         LD      B,H             
4CA5: 7E         LD      A,(HL)          
4CA6: 99         SBC     C               
4CA7: 65         LD      H,L             
4CA8: 44         LD      B,H             
4CA9: 7E         LD      A,(HL)          
4CAA: 99         SBC     C               
4CAB: 85         ADD     A,L             
4CAC: 44         LD      B,H             
4CAD: 7E         LD      A,(HL)          
4CAE: CD 2D 6E   CALL    $6E2D           
4CB1: F0 CC      LD      A,($CC)         
4CB3: E6 48      AND     $48             
4CB5: 28 09      JR      Z,$4CC0         
4CB7: FA A6 DB   LD      A,($DBA6)       
4CBA: 3C         INC     A               
4CBB: E6 03      AND     $03             
4CBD: EA A6 DB   LD      ($DBA6),A       
4CC0: F0 CC      LD      A,($CC)         
4CC2: E6 04      AND     $04             
4CC4: 28 0D      JR      Z,$4CD3         
4CC6: FA A6 DB   LD      A,($DBA6)       
4CC9: 3D         DEC     A               
4CCA: FE FF      CP      $FF             
4CCC: 20 02      JR      NZ,$4CD0        
4CCE: 3E 03      LD      A,$03           
4CD0: EA A6 DB   LD      ($DBA6),A       
4CD3: F0 CC      LD      A,($CC)         
4CD5: E6 90      AND     $90             
4CD7: 28 36      JR      Z,$4D0F         
4CD9: FA A6 DB   LD      A,($DBA6)       
4CDC: FE 03      CP      $03             
4CDE: 20 03      JR      NZ,$4CE3        
4CE0: C3 BF 44   JP      $44BF           
4CE3: CD 07 49   CALL    $4907           
4CE6: CD 45 44   CALL    $4445           
4CE9: 18 12      JR      $4CFD           
4CEB: 99         SBC     C               
4CEC: E4                              
4CED: 0D         DEC     C               
4CEE: 7E         LD      A,(HL)          
4CEF: 7E         LD      A,(HL)          
4CF0: 10 14      STOP    $14             
4CF2: 08 13 7E   LD      ($7E13),SP      
4CF5: 7E         LD      A,(HL)          
4CF6: 7E         LD      A,(HL)          
4CF7: 7E         LD      A,(HL)          
4CF8: 0E 0A      LD      C,$0A           
4CFA: 7E         LD      A,(HL)          
4CFB: 7E         LD      A,(HL)          
4CFC: 00         NOP                     
4CFD: 21 01 D6   LD      HL,$D601        
4D00: 11 EB 4C   LD      DE,$4CEB        
4D03: 0E 11      LD      C,$11           
4D05: 1A         LD      A,(DE)          
4D06: 13         INC     DE              
4D07: 22         LD      (HLI),A         
4D08: 0D         DEC     C               
4D09: 79         LD      A,C             
4D0A: FE FF      CP      $FF             
4D0C: 20 F7      JR      NZ,$4D05        
4D0E: C9         RET                     
4D0F: CD 98 48   CALL    $4898           
4D12: C9         RET                     
4D13: F0 CC      LD      A,($CC)         
4D15: CB 6F      SET     1,E             
4D17: 20 2D      JR      NZ,$4D46        
4D19: E6 90      AND     $90             
4D1B: 28 64      JR      Z,$4D81         
4D1D: FA 00 D0   LD      A,($D000)       
4D20: A7         AND     A               
4D21: CA BF 44   JP      Z,$44BF         
4D24: CD 07 49   CALL    $4907           
4D27: FA A6 DB   LD      A,($DBA6)       
4D2A: CB 27      SET     1,E             
4D2C: 5F         LD      E,A             
4D2D: 16 00      LD      D,$00           
4D2F: 21 3C 49   LD      HL,$493C        
4D32: 19         ADD     HL,DE           
4D33: 2A         LD      A,(HLI)         
4D34: 66         LD      H,(HL)          
4D35: 6F         LD      L,A             
4D36: 11 80 03   LD      DE,$0380        
4D39: CD B5 27   CALL    $27B5           
4D3C: AF         XOR     A               
4D3D: 22         LD      (HLI),A         
4D3E: 1B         DEC     DE              
4D3F: 7B         LD      A,E             
4D40: B2         OR      D               
4D41: 20 F6      JR      NZ,$4D39        
4D43: C3 BF 44   JP      $44BF           
4D46: CD 8D 4D   CALL    $4D8D           
4D49: CD 63 4D   CALL    $4D63           
4D4C: 21 96 DB   LD      HL,$DB96        
4D4F: 35         DEC     (HL)            
4D50: C9         RET                     
4D51: 99         SBC     C               
4D52: E4                              
4D53: 0D         DEC     C               
4D54: 11 04 13   LD      DE,$1304        
4D57: 14         INC     D               
4D58: 11 0D 7E   LD      DE,$7E0D        
4D5B: 13         INC     DE              
4D5C: 0E 7E      LD      C,$7E           
4D5E: 0C         INC     C               
4D5F: 04         INC     B               
4D60: 0D         DEC     C               
4D61: 14         INC     D               
4D62: 00         NOP                     
4D63: FA 00 D6   LD      A,($D600)       
4D66: 5F         LD      E,A             
4D67: C6 11      ADD     $11             
4D69: EA 00 D6   LD      ($D600),A       
4D6C: 16 00      LD      D,$00           
4D6E: 21 01 D6   LD      HL,$D601        
4D71: 19         ADD     HL,DE           
4D72: 11 51 4D   LD      DE,$4D51        
4D75: 0E 11      LD      C,$11           
4D77: 1A         LD      A,(DE)          
4D78: 13         INC     DE              
4D79: 22         LD      (HLI),A         
4D7A: 0D         DEC     C               
4D7B: 79         LD      A,C             
4D7C: FE FF      CP      $FF             
4D7E: 20 F7      JR      NZ,$4D77        
4D80: C9         RET                     
4D81: CD B4 4D   CALL    $4DB4           
4D84: CD 98 48   CALL    $4898           
4D87: F0 E7      LD      A,($E7)         
4D89: E6 10      AND     $10             
4D8B: 28 0A      JR      Z,$4D97         
4D8D: FA A6 DB   LD      A,($DBA6)       
4D90: C7         RST     0X00            
4D91: 32         LD      (HLD),A         
4D92: 4C         LD      C,H             
4D93: 3B         DEC     SP              
4D94: 4C         LD      C,H             
4D95: 44         LD      B,H             
4D96: 4C         LD      C,H             
4D97: FA A6 DB   LD      A,($DBA6)       
4D9A: 17         RLA                     
4D9B: 17         RLA                     
4D9C: 17         RLA                     
4D9D: E6 F8      AND     $F8             
4D9F: 5F         LD      E,A             
4DA0: 16 00      LD      D,$00           
4DA2: 21 96 4C   LD      HL,$4C96        
4DA5: 19         ADD     HL,DE           
4DA6: 11 01 D6   LD      DE,$D601        
4DA9: 0E 08      LD      C,$08           
4DAB: 2A         LD      A,(HLI)         
4DAC: 12         LD      (DE),A          
4DAD: 13         INC     DE              
4DAE: 0D         DEC     C               
4DAF: 20 FA      JR      NZ,$4DAB        
4DB1: AF         XOR     A               
4DB2: 12         LD      (DE),A          
4DB3: C9         RET                     
4DB4: F0 CC      LD      A,($CC)         
4DB6: E6 43      AND     $43             
4DB8: 28 0B      JR      Z,$4DC5         
4DBA: CD 33 6E   CALL    $6E33           
4DBD: FA 00 D0   LD      A,($D000)       
4DC0: EE 01      XOR     $01             
4DC2: EA 00 D0   LD      ($D000),A       
4DC5: F0 E7      LD      A,($E7)         
4DC7: E6 10      AND     $10             
4DC9: 20 17      JR      NZ,$4DE2        
4DCB: FA 00 D0   LD      A,($D000)       
4DCE: 5F         LD      E,A             
4DCF: 3E 28      LD      A,$28           
4DD1: 1D         DEC     E               
4DD2: 20 02      JR      NZ,$4DD6        
4DD4: 3E 6C      LD      A,$6C           
4DD6: 21 0C C0   LD      HL,$C00C        
4DD9: 36 88      LD      (HL),$88        
4DDB: 23         INC     HL              
4DDC: 22         LD      (HLI),A         
4DDD: 3E BE      LD      A,$BE           
4DDF: 22         LD      (HLI),A         
4DE0: AF         XOR     A               
4DE1: 77         LD      (HL),A          
4DE2: C9         RET                     
4DE3: B0         OR      B               
4DE4: B1         OR      C               
4DE5: B2         OR      D               
4DE6: B3         OR      E               
4DE7: B4         OR      H               
4DE8: B5         OR      L               
4DE9: B6         OR      (HL)            
4DEA: B7         OR      A               
4DEB: B8         CP      B               
4DEC: B9         CP      C               
4DED: E5         PUSH    HL              
4DEE: FA 00 D6   LD      A,($D600)       
4DF1: 4F         LD      C,A             
4DF2: C6 06      ADD     $06             
4DF4: EA 00 D6   LD      ($D600),A       
4DF7: 06 00      LD      B,$00           
4DF9: 21 01 D6   LD      HL,$D601        
4DFC: 09         ADD     HL,BC           
4DFD: 7A         LD      A,D             
4DFE: 22         LD      (HLI),A         
4DFF: 7B         LD      A,E             
4E00: 22         LD      (HLI),A         
4E01: 3E 02      LD      A,$02           
4E03: 22         LD      (HLI),A         
4E04: C1         POP     BC              
4E05: E5         PUSH    HL              
4E06: 79         LD      A,C             
4E07: E6 0F      AND     $0F             
4E09: 5F         LD      E,A             
4E0A: 16 00      LD      D,$00           
4E0C: 21 E3 4D   LD      HL,$4DE3        
4E0F: 19         ADD     HL,DE           
4E10: 7E         LD      A,(HL)          
4E11: E1         POP     HL              
4E12: 22         LD      (HLI),A         
4E13: E5         PUSH    HL              
4E14: 78         LD      A,B             
4E15: E6 F0      AND     $F0             
4E17: CB 37      SET     1,E             
4E19: 5F         LD      E,A             
4E1A: 16 00      LD      D,$00           
4E1C: 21 E3 4D   LD      HL,$4DE3        
4E1F: 19         ADD     HL,DE           
4E20: 7E         LD      A,(HL)          
4E21: E1         POP     HL              
4E22: 22         LD      (HLI),A         
4E23: E5         PUSH    HL              
4E24: 78         LD      A,B             
4E25: E6 0F      AND     $0F             
4E27: 5F         LD      E,A             
4E28: 16 00      LD      D,$00           
4E2A: 21 E3 4D   LD      HL,$4DE3        
4E2D: 19         ADD     HL,DE           
4E2E: 7E         LD      A,(HL)          
4E2F: E1         POP     HL              
4E30: 22         LD      (HLI),A         
4E31: AF         XOR     A               
4E32: 77         LD      (HL),A          
4E33: C9         RET                     
4E34: FA 96 DB   LD      A,($DB96)       
4E37: C7         RST     0X00            
4E38: 46         LD      B,(HL)          
4E39: 4E         LD      C,(HL)          
4E3A: 5B         LD      E,E             
4E3B: 4E         LD      C,(HL)          
4E3C: 63         LD      H,E             
4E3D: 4E         LD      C,(HL)          
4E3E: 81         ADD     A,C             
4E3F: 4E         LD      C,(HL)          
4E40: 9F         SBC     A               
4E41: 4E         LD      C,(HL)          
4E42: 65         LD      H,L             
4E43: 4F         LD      C,A             
4E44: 6F         LD      L,A             
4E45: 50         LD      D,B             
4E46: 3E 08      LD      A,$08           
4E48: EA FE D6   LD      ($D6FE),A       
4E4B: AF         XOR     A               
4E4C: EA A6 DB   LD      ($DBA6),A       
4E4F: EA 00 D0   LD      ($D000),A       
4E52: EA 01 D0   LD      ($D001),A       
4E55: EA 02 D0   LD      ($D002),A       
4E58: C3 45 44   JP      $4445           
4E5B: 3E 0C      LD      A,$0C           
4E5D: EA FF D6   LD      ($D6FF),A       
4E60: C3 45 44   JP      $4445           
4E63: 01 C4 98   LD      BC,$98C4        
4E66: 11 80 DB   LD      DE,$DB80        
4E69: CD 95 47   CALL    $4795           
4E6C: 01 24 99   LD      BC,$9924        
4E6F: 11 85 DB   LD      DE,$DB85        
4E72: CD 95 47   CALL    $4795           
4E75: 01 84 99   LD      BC,$9984        
4E78: 11 8A DB   LD      DE,$DB8A        
4E7B: CD 95 47   CALL    $4795           
4E7E: C3 45 44   JP      $4445           
4E81: 01 CD 98   LD      BC,$98CD        
4E84: 11 80 DB   LD      DE,$DB80        
4E87: CD 95 47   CALL    $4795           
4E8A: 01 2D 99   LD      BC,$992D        
4E8D: 11 85 DB   LD      DE,$DB85        
4E90: CD 95 47   CALL    $4795           
4E93: 01 8D 99   LD      BC,$998D        
4E96: 11 8A DB   LD      DE,$DB8A        
4E99: CD 95 47   CALL    $4795           
4E9C: C3 45 44   JP      $4445           
4E9F: CD 2D 6E   CALL    $6E2D           
4EA2: F0 CC      LD      A,($CC)         
4EA4: E6 48      AND     $48             
4EA6: 28 09      JR      Z,$4EB1         
4EA8: FA 01 D0   LD      A,($D001)       
4EAB: 3C         INC     A               
4EAC: E6 03      AND     $03             
4EAE: EA 01 D0   LD      ($D001),A       
4EB1: F0 CC      LD      A,($CC)         
4EB3: E6 04      AND     $04             
4EB5: 28 0D      JR      Z,$4EC4         
4EB7: FA 01 D0   LD      A,($D001)       
4EBA: 3D         DEC     A               
4EBB: FE FF      CP      $FF             
4EBD: 20 02      JR      NZ,$4EC1        
4EBF: 3E 03      LD      A,$03           
4EC1: EA 01 D0   LD      ($D001),A       
4EC4: F0 CC      LD      A,($CC)         
4EC6: E6 90      AND     $90             
4EC8: 28 0E      JR      Z,$4ED8         
4ECA: FA 01 D0   LD      A,($D001)       
4ECD: FE 03      CP      $03             
4ECF: CA BF 44   JP      Z,$44BF         
4ED2: CD 45 44   CALL    $4445           
4ED5: CD 07 49   CALL    $4907           
4ED8: FA 01 D0   LD      A,($D001)       
4EDB: 5F         LD      E,A             
4EDC: 16 00      LD      D,$00           
4EDE: 21 24 48   LD      HL,$4824        
4EE1: 19         ADD     HL,DE           
4EE2: F0 E7      LD      A,($E7)         
4EE4: E6 08      AND     $08             
4EE6: 7E         LD      A,(HL)          
4EE7: 21 00 C0   LD      HL,$C000        
4EEA: 28 17      JR      Z,$4F03         
4EEC: F5         PUSH    AF              
4EED: 22         LD      (HLI),A         
4EEE: 3E 10      LD      A,$10           
4EF0: 22         LD      (HLI),A         
4EF1: 3E 00      LD      A,$00           
4EF3: 22         LD      (HLI),A         
4EF4: 3E 00      LD      A,$00           
4EF6: 22         LD      (HLI),A         
4EF7: F1         POP     AF              
4EF8: 22         LD      (HLI),A         
4EF9: 3E 18      LD      A,$18           
4EFB: 22         LD      (HLI),A         
4EFC: 3E 02      LD      A,$02           
4EFE: 22         LD      (HLI),A         
4EFF: 3E 00      LD      A,$00           
4F01: 77         LD      (HL),A          
4F02: C9         RET                     
4F03: F5         PUSH    AF              
4F04: 22         LD      (HLI),A         
4F05: 3E 10      LD      A,$10           
4F07: 22         LD      (HLI),A         
4F08: 3E 02      LD      A,$02           
4F0A: 22         LD      (HLI),A         
4F0B: 3E 20      LD      A,$20           
4F0D: 22         LD      (HLI),A         
4F0E: F1         POP     AF              
4F0F: 22         LD      (HLI),A         
4F10: 3E 18      LD      A,$18           
4F12: 22         LD      (HLI),A         
4F13: 3E 00      LD      A,$00           
4F15: 22         LD      (HLI),A         
4F16: 3E 20      LD      A,$20           
4F18: 77         LD      (HL),A          
4F19: C9         RET                     
4F1A: FA 01 D0   LD      A,($D001)       
4F1D: 5F         LD      E,A             
4F1E: 16 00      LD      D,$00           
4F20: 21 24 48   LD      HL,$4824        
4F23: 19         ADD     HL,DE           
4F24: 7E         LD      A,(HL)          
4F25: 21 00 C0   LD      HL,$C000        
4F28: C6 05      ADD     $05             
4F2A: 22         LD      (HLI),A         
4F2B: 3E 14      LD      A,$14           
4F2D: 22         LD      (HLI),A         
4F2E: 3E BE      LD      A,$BE           
4F30: 22         LD      (HLI),A         
4F31: 3E 00      LD      A,$00           
4F33: 77         LD      (HL),A          
4F34: C9         RET                     
4F35: 98         SBC     B               
4F36: A4         AND     H               
4F37: 44         LD      B,H             
4F38: 7E         LD      A,(HL)          
4F39: 98         SBC     B               
4F3A: C4 44 7E   CALL    NZ,$7E44        
4F3D: 99         SBC     C               
4F3E: 04         INC     B               
4F3F: 44         LD      B,H             
4F40: 7E         LD      A,(HL)          
4F41: 99         SBC     C               
4F42: 24         INC     H               
4F43: 44         LD      B,H             
4F44: 7E         LD      A,(HL)          
4F45: 99         SBC     C               
4F46: 64         LD      H,H             
4F47: 44         LD      B,H             
4F48: 7E         LD      A,(HL)          
4F49: 99         SBC     C               
4F4A: 84         ADD     A,H             
4F4B: 44         LD      B,H             
4F4C: 7E         LD      A,(HL)          
4F4D: 98         SBC     B               
4F4E: AD         XOR     L               
4F4F: 44         LD      B,H             
4F50: 7E         LD      A,(HL)          
4F51: 98         SBC     B               
4F52: CD 44 7E   CALL    $7E44           
4F55: 99         SBC     C               
4F56: 0D         DEC     C               
4F57: 44         LD      B,H             
4F58: 7E         LD      A,(HL)          
4F59: 99         SBC     C               
4F5A: 2D         DEC     L               
4F5B: 44         LD      B,H             
4F5C: 7E         LD      A,(HL)          
4F5D: 99         SBC     C               
4F5E: 6D         LD      L,L             
4F5F: 44         LD      B,H             
4F60: 7E         LD      A,(HL)          
4F61: 99         SBC     C               
4F62: 8D         ADC     A,L             
4F63: 44         LD      B,H             
4F64: 7E         LD      A,(HL)          
4F65: CD 2D 6E   CALL    $6E2D           
4F68: F0 CC      LD      A,($CC)         
4F6A: E6 48      AND     $48             
4F6C: 28 09      JR      Z,$4F77         
4F6E: FA 02 D0   LD      A,($D002)       
4F71: 3C         INC     A               
4F72: E6 03      AND     $03             
4F74: EA 02 D0   LD      ($D002),A       
4F77: F0 CC      LD      A,($CC)         
4F79: E6 04      AND     $04             
4F7B: 28 0D      JR      Z,$4F8A         
4F7D: FA 02 D0   LD      A,($D002)       
4F80: 3D         DEC     A               
4F81: FE FF      CP      $FF             
4F83: 20 02      JR      NZ,$4F87        
4F85: 3E 03      LD      A,$03           
4F87: EA 02 D0   LD      ($D002),A       
4F8A: CD 1A 4F   CALL    $4F1A           
4F8D: F0 CC      LD      A,($CC)         
4F8F: CB 6F      SET     1,E             
4F91: 28 07      JR      Z,$4F9A         
4F93: 21 96 DB   LD      HL,$DB96        
4F96: 35         DEC     (HL)            
4F97: C3 D5 4F   JP      $4FD5           
4F9A: E6 90      AND     $90             
4F9C: 28 11      JR      Z,$4FAF         
4F9E: FA 02 D0   LD      A,($D002)       
4FA1: FE 03      CP      $03             
4FA3: CA BF 44   JP      Z,$44BF         
4FA6: CD 07 49   CALL    $4907           
4FA9: CD 45 44   CALL    $4445           
4FAC: C3 FD 4C   JP      $4CFD           
4FAF: CD FB 4F   CALL    $4FFB           
4FB2: F0 E7      LD      A,($E7)         
4FB4: E6 10      AND     $10             
4FB6: 28 1D      JR      Z,$4FD5         
4FB8: FA 01 D0   LD      A,($D001)       
4FBB: 17         RLA                     
4FBC: 17         RLA                     
4FBD: 17         RLA                     
4FBE: E6 F8      AND     $F8             
4FC0: 5F         LD      E,A             
4FC1: 16 00      LD      D,$00           
4FC3: 21 35 4F   LD      HL,$4F35        
4FC6: 19         ADD     HL,DE           
4FC7: 11 01 D6   LD      DE,$D601        
4FCA: 0E 08      LD      C,$08           
4FCC: 2A         LD      A,(HLI)         
4FCD: 12         LD      (DE),A          
4FCE: 13         INC     DE              
4FCF: 0D         DEC     C               
4FD0: 20 FA      JR      NZ,$4FCC        
4FD2: AF         XOR     A               
4FD3: 12         LD      (DE),A          
4FD4: C9         RET                     
4FD5: FA 01 D0   LD      A,($D001)       
4FD8: FE 01      CP      $01             
4FDA: 28 0D      JR      Z,$4FE9         
4FDC: FE 02      CP      $02             
4FDE: 28 12      JR      Z,$4FF2         
4FE0: 01 C4 98   LD      BC,$98C4        
4FE3: 11 80 DB   LD      DE,$DB80        
4FE6: C3 95 47   JP      $4795           
4FE9: 01 24 99   LD      BC,$9924        
4FEC: 11 85 DB   LD      DE,$DB85        
4FEF: C3 95 47   JP      $4795           
4FF2: 01 84 99   LD      BC,$9984        
4FF5: 11 8A DB   LD      DE,$DB8A        
4FF8: C3 95 47   JP      $4795           
4FFB: FA 02 D0   LD      A,($D002)       
4FFE: 5F         LD      E,A             
4FFF: 16 00      LD      D,$00           
5001: 21 24 48   LD      HL,$4824        
5004: 19         ADD     HL,DE           
5005: FA 02 D0   LD      A,($D002)       
5008: FE 03      CP      $03             
500A: CA 49 50   JP      Z,$5049         
500D: F0 E7      LD      A,($E7)         
500F: E6 08      AND     $08             
5011: 28 1B      JR      Z,$502E         
5013: 7E         LD      A,(HL)          
5014: 21 08 C0   LD      HL,$C008        
5017: F5         PUSH    AF              
5018: 22         LD      (HLI),A         
5019: 3E 58      LD      A,$58           
501B: 22         LD      (HLI),A         
501C: 3E 00      LD      A,$00           
501E: 22         LD      (HLI),A         
501F: 3E 00      LD      A,$00           
5021: 22         LD      (HLI),A         
5022: F1         POP     AF              
5023: 22         LD      (HLI),A         
5024: 3E 60      LD      A,$60           
5026: 22         LD      (HLI),A         
5027: 3E 02      LD      A,$02           
5029: 22         LD      (HLI),A         
502A: 3E 00      LD      A,$00           
502C: 77         LD      (HL),A          
502D: C9         RET                     
502E: 7E         LD      A,(HL)          
502F: 21 08 C0   LD      HL,$C008        
5032: F5         PUSH    AF              
5033: 22         LD      (HLI),A         
5034: 3E 58      LD      A,$58           
5036: 22         LD      (HLI),A         
5037: 3E 02      LD      A,$02           
5039: 22         LD      (HLI),A         
503A: 3E 20      LD      A,$20           
503C: 22         LD      (HLI),A         
503D: F1         POP     AF              
503E: 22         LD      (HLI),A         
503F: 3E 60      LD      A,$60           
5041: 22         LD      (HLI),A         
5042: 3E 00      LD      A,$00           
5044: 22         LD      (HLI),A         
5045: 3E 20      LD      A,$20           
5047: 77         LD      (HL),A          
5048: C9         RET                     
5049: F0 E7      LD      A,($E7)         
504B: E6 08      AND     $08             
504D: 7E         LD      A,(HL)          
504E: 21 08 C0   LD      HL,$C008        
5051: C3 EA 4E   JP      $4EEA           
5054: FA 02 D0   LD      A,($D002)       
5057: 5F         LD      E,A             
5058: 16 00      LD      D,$00           
505A: 21 24 48   LD      HL,$4824        
505D: 19         ADD     HL,DE           
505E: 7E         LD      A,(HL)          
505F: 21 08 C0   LD      HL,$C008        
5062: C6 05      ADD     $05             
5064: 22         LD      (HLI),A         
5065: 3E 5C      LD      A,$5C           
5067: 22         LD      (HLI),A         
5068: 3E BE      LD      A,$BE           
506A: 22         LD      (HLI),A         
506B: 3E 00      LD      A,$00           
506D: 77         LD      (HL),A          
506E: C9         RET                     
506F: CD 1A 4F   CALL    $4F1A           
5072: CD 54 50   CALL    $5054           
5075: CD B4 4D   CALL    $4DB4           
5078: F0 CC      LD      A,($CC)         
507A: E6 90      AND     $90             
507C: 28 3D      JR      Z,$50BB         
507E: FA 00 D0   LD      A,($D000)       
5081: A7         AND     A               
5082: CA BF 44   JP      Z,$44BF         
5085: CD 07 49   CALL    $4907           
5088: FA 01 D0   LD      A,($D001)       
508B: CB 27      SET     1,E             
508D: 5F         LD      E,A             
508E: 16 00      LD      D,$00           
5090: 21 42 49   LD      HL,$4942        
5093: 19         ADD     HL,DE           
5094: 4E         LD      C,(HL)          
5095: 23         INC     HL              
5096: 46         LD      B,(HL)          
5097: FA 02 D0   LD      A,($D002)       
509A: CB 27      SET     1,E             
509C: 5F         LD      E,A             
509D: 16 00      LD      D,$00           
509F: 21 42 49   LD      HL,$4942        
50A2: 19         ADD     HL,DE           
50A3: 7E         LD      A,(HL)          
50A4: 23         INC     HL              
50A5: 66         LD      H,(HL)          
50A6: 6F         LD      L,A             
50A7: 11 85 03   LD      DE,$0385        
50AA: CD B5 27   CALL    $27B5           
50AD: 0A         LD      A,(BC)          
50AE: 03         INC     BC              
50AF: CD B5 27   CALL    $27B5           
50B2: 22         LD      (HLI),A         
50B3: 1B         DEC     DE              
50B4: 7B         LD      A,E             
50B5: B2         OR      D               
50B6: 20 F2      JR      NZ,$50AA        
50B8: C3 BF 44   JP      $44BF           
50BB: F0 CC      LD      A,($CC)         
50BD: CB 6F      SET     1,E             
50BF: 28 0E      JR      Z,$50CF         
50C1: 21 96 DB   LD      HL,$DB96        
50C4: 35         DEC     (HL)            
50C5: AF         XOR     A               
50C6: EA 00 D0   LD      ($D000),A       
50C9: CD 63 4D   CALL    $4D63           
50CC: C3 F5 50   JP      $50F5           
50CF: CD B2 4F   CALL    $4FB2           
50D2: F0 E7      LD      A,($E7)         
50D4: E6 10      AND     $10             
50D6: 28 1D      JR      Z,$50F5         
50D8: FA 02 D0   LD      A,($D002)       
50DB: 17         RLA                     
50DC: 17         RLA                     
50DD: 17         RLA                     
50DE: E6 F8      AND     $F8             
50E0: 5F         LD      E,A             
50E1: 16 00      LD      D,$00           
50E3: 21 4D 4F   LD      HL,$4F4D        
50E6: 19         ADD     HL,DE           
50E7: 11 09 D6   LD      DE,$D609        
50EA: 0E 08      LD      C,$08           
50EC: 2A         LD      A,(HLI)         
50ED: 12         LD      (DE),A          
50EE: 13         INC     DE              
50EF: 0D         DEC     C               
50F0: 20 FA      JR      NZ,$50EC        
50F2: AF         XOR     A               
50F3: 12         LD      (DE),A          
50F4: C9         RET                     
50F5: FA 02 D0   LD      A,($D002)       
50F8: FE 01      CP      $01             
50FA: 28 0D      JR      Z,$5109         
50FC: FE 02      CP      $02             
50FE: 28 12      JR      Z,$5112         
5100: 01 CD 98   LD      BC,$98CD        
5103: 11 80 DB   LD      DE,$DB80        
5106: C3 95 47   JP      $4795           
5109: 01 2D 99   LD      BC,$992D        
510C: 11 85 DB   LD      DE,$DB85        
510F: C3 95 47   JP      $4795           
5112: 01 8D 99   LD      BC,$998D        
5115: 11 8A DB   LD      DE,$DB8A        
5118: C3 95 47   JP      $4795           
511B: 18 18      JR      $5135           
511D: 18 18      JR      $5137           
511F: 18 18      JR      $5139           
5121: 28 28      JR      Z,$514B         
5123: 28 28      JR      Z,$514D         
5125: 38 38      JR      C,$515F         
5127: 38 38      JR      C,$5161         
5129: 50         LD      D,B             
512A: AF         XOR     A               
512B: E0 F9      LDFF00  ($F9),A         
512D: FA 5A DB   LD      A,($DB5A)       
5130: A7         AND     A               
5131: 20 0E      JR      NZ,$5141        
5133: FA 5B DB   LD      A,($DB5B)       
5136: 5F         LD      E,A             
5137: 16 00      LD      D,$00           
5139: 21 1B 51   LD      HL,$511B        
513C: 19         ADD     HL,DE           
513D: 7E         LD      A,(HL)          
513E: EA 5A DB   LD      ($DB5A),A       
5141: 21 D1 DB   LD      HL,$DBD1        
5144: 7E         LD      A,(HL)          
5145: 36 00      LD      (HL),$00        
5147: A7         AND     A               
5148: 20 20      JR      NZ,$516A        
514A: FA A6 DB   LD      A,($DBA6)       
514D: CB 27      SET     1,E             
514F: 5F         LD      E,A             
5150: 16 00      LD      D,$00           
5152: 21 3C 49   LD      HL,$493C        
5155: 19         ADD     HL,DE           
5156: 4E         LD      C,(HL)          
5157: 23         INC     HL              
5158: 46         LD      B,(HL)          
5159: 21 00 D8   LD      HL,$D800        
515C: 11 80 03   LD      DE,$0380        
515F: CD B5 27   CALL    $27B5           
5162: 0A         LD      A,(BC)          
5163: 03         INC     BC              
5164: 22         LD      (HLI),A         
5165: 1B         DEC     DE              
5166: 7B         LD      A,E             
5167: B2         OR      D               
5168: 20 F5      JR      NZ,$515F        
516A: 3E 0B      LD      A,$0B           
516C: EA 95 DB   LD      ($DB95),A       
516F: AF         XOR     A               
5170: EA 96 DB   LD      ($DB96),A       
5173: AF         XOR     A               
5174: EA 1C C1   LD      ($C11C),A       
5177: E0 9C      LDFF00  ($9C),A         
5179: EA 93 DB   LD      ($DB93),A       
517C: EA 94 DB   LD      ($DB94),A       
517F: EA 90 DB   LD      ($DB90),A       
5182: EA 8F DB   LD      ($DB8F),A       
5185: EA 92 DB   LD      ($DB92),A       
5188: EA 91 DB   LD      ($DB91),A       
518B: FA 6F DB   LD      A,($DB6F)       
518E: A7         AND     A               
518F: 20 0F      JR      NZ,$51A0        
5191: 3E 16      LD      A,$16           
5193: EA 6F DB   LD      ($DB6F),A       
5196: 3E 50      LD      A,$50           
5198: EA 70 DB   LD      ($DB70),A       
519B: 3E 27      LD      A,$27           
519D: EA 71 DB   LD      ($DB71),A       
51A0: FA 62 DB   LD      A,($DB62)       
51A3: A7         AND     A               
51A4: 28 37      JR      Z,$51DD         
51A6: EA 9D DB   LD      ($DB9D),A       
51A9: FA 63 DB   LD      A,($DB63)       
51AC: EA 9E DB   LD      ($DB9E),A       
51AF: FA 61 DB   LD      A,($DB61)       
51B2: E0 F6      LDFF00  ($F6),A         
51B4: EA 9C DB   LD      ($DB9C),A       
51B7: FA 60 DB   LD      A,($DB60)       
51BA: E0 F7      LDFF00  ($F7),A         
51BC: FA 64 DB   LD      A,($DB64)       
51BF: EA AE DB   LD      ($DBAE),A       
51C2: AF         XOR     A               
51C3: E0 F9      LDFF00  ($F9),A         
51C5: FA 5F DB   LD      A,($DB5F)       
51C8: E6 01      AND     $01             
51CA: EA A5 DB   LD      ($DBA5),A       
51CD: 28 08      JR      Z,$51D7         
51CF: 3E 04      LD      A,$04           
51D1: E0 9D      LDFF00  ($9D),A         
51D3: 3E 02      LD      A,$02           
51D5: E0 9E      LDFF00  ($9E),A         
51D7: 3E 02      LD      A,$02           
51D9: EA FF D6   LD      ($D6FF),A       
51DC: C9         RET                     
51DD: 3E 30      LD      A,$30           
51DF: EA 78 DB   LD      ($DB78),A       
51E2: 3E 30      LD      A,$30           
51E4: EA 77 DB   LD      ($DB77),A       
51E7: 3E 20      LD      A,$20           
51E9: EA 76 DB   LD      ($DB76),A       
51EC: 3E A3      LD      A,$A3           
51EE: EA 9C DB   LD      ($DB9C),A       
51F1: E0 F6      LDFF00  ($F6),A         
51F3: 3E 01      LD      A,$01           
51F5: EA A5 DB   LD      ($DBA5),A       
51F8: 3E 10      LD      A,$10           
51FA: E0 F7      LDFF00  ($F7),A         
51FC: 3E 50      LD      A,$50           
51FE: EA 9D DB   LD      ($DB9D),A       
5201: 3E 60      LD      A,$60           
5203: EA 9E DB   LD      ($DB9E),A       
5206: AF         XOR     A               
5207: E0 9D      LDFF00  ($9D),A         
5209: 3E 03      LD      A,$03           
520B: E0 9E      LDFF00  ($9E),A         
520D: 3E 16      LD      A,$16           
520F: EA 6F DB   LD      ($DB6F),A       
5212: 3E 50      LD      A,$50           
5214: EA 70 DB   LD      ($DB70),A       
5217: 3E 27      LD      A,$27           
5219: EA 71 DB   LD      ($DB71),A       
521C: 18 B9      JR      $51D7           
521E: 9D         SBC     L               
521F: 9D         SBC     L               
5220: 9D         SBC     L               
5221: FF         RST     0X38            
5222: 9D         SBC     L               
5223: 9D         SBC     L               
5224: 9D         SBC     L               
5225: FF         RST     0X38            
5226: 9D         SBC     L               
5227: 9D         SBC     L               
5228: 9C         SBC     H               
5229: FF         RST     0X38            
522A: 9D         SBC     L               
522B: 9D         SBC     L               
522C: 9C         SBC     H               
522D: FF         RST     0X38            
522E: 32         LD      (HLD),A         
522F: 32         LD      (HLD),A         
5230: 09         ADD     HL,BC           
5231: FF         RST     0X38            
5232: 2E 2E      LD      L,$2E           
5234: 09         ADD     HL,BC           
5235: FF         RST     0X38            
5236: 8A         ADC     A,D             
5237: 32         LD      (HLD),A         
5238: E9         JP      (HL)            
5239: FF         RST     0X38            
523A: 8A         ADC     A,D             
523B: 2E E9      LD      L,$E9           
523D: FF         RST     0X38            
523E: C8         RET     Z               
523F: C8         RET     Z               
5240: 00         NOP                     
5241: FF         RST     0X38            
5242: C8         RET     Z               
5243: C8         RET     Z               
5244: 00         NOP                     
5245: FF         RST     0X38            
5246: 48         LD      C,B             
5247: C8         RET     Z               
5248: 00         NOP                     
5249: FF         RST     0X38            
524A: 48         LD      C,B             
524B: C8         RET     Z               
524C: 00         NOP                     
524D: FF         RST     0X38            
524E: 7F         LD      A,A             
524F: 7F         LD      A,A             
5250: BA         CP      D               
5251: FF         RST     0X38            
5252: 7F         LD      A,A             
5253: 7F         LD      A,A             
5254: BA         CP      D               
5255: FF         RST     0X38            
5256: 7F         LD      A,A             
5257: 7F         LD      A,A             
5258: BA         CP      D               
5259: FF         RST     0X38            
525A: 7F         LD      A,A             
525B: 7F         LD      A,A             
525C: BA         CP      D               
525D: FF         RST     0X38            
525E: 00         NOP                     
525F: 00         NOP                     
5260: 00         NOP                     
5261: FF         RST     0X38            
5262: 00         NOP                     
5263: 00         NOP                     
5264: 00         NOP                     
5265: FF         RST     0X38            
5266: 9D         SBC     L               
5267: 9D         SBC     L               
5268: FF         RST     0X38            
5269: 00         NOP                     
526A: 9D         SBC     L               
526B: 9D         SBC     L               
526C: 9D         SBC     L               
526D: FF         RST     0X38            
526E: 9D         SBC     L               
526F: 9C         SBC     H               
5270: FF         RST     0X38            
5271: 00         NOP                     
5272: 9D         SBC     L               
5273: 9C         SBC     H               
5274: 9C         SBC     H               
5275: FF         RST     0X38            
5276: 9D         SBC     L               
5277: 9D         SBC     L               
5278: 9C         SBC     H               
5279: 9C         SBC     H               
527A: FF         RST     0X38            
527B: 00         NOP                     
527C: 00         NOP                     
527D: 00         NOP                     
527E: 00         NOP                     
527F: 00         NOP                     
5280: 00         NOP                     
5281: 9D         SBC     L               
5282: 9D         SBC     L               
5283: 9C         SBC     H               
5284: 9C         SBC     H               
5285: 9C         SBC     H               
5286: 9C         SBC     H               
5287: FF         RST     0X38            
5288: 00         NOP                     
5289: 00         NOP                     
528A: 00         NOP                     
528B: 00         NOP                     
528C: 9D         SBC     L               
528D: 9D         SBC     L               
528E: 9C         SBC     H               
528F: 9C         SBC     H               
5290: 9D         SBC     L               
5291: 9D         SBC     L               
5292: 9C         SBC     H               
5293: 9C         SBC     H               
5294: FF         RST     0X38            
5295: 00         NOP                     
5296: 00         NOP                     
5297: 9D         SBC     L               
5298: 9D         SBC     L               
5299: 9C         SBC     H               
529A: 9C         SBC     H               
529B: 9D         SBC     L               
529C: 9D         SBC     L               
529D: 9C         SBC     H               
529E: 9C         SBC     H               
529F: 9C         SBC     H               
52A0: 9C         SBC     H               
52A1: FF         RST     0X38            
52A2: 00         NOP                     
52A3: 00         NOP                     
52A4: 00         NOP                     
52A5: FF         RST     0X38            
52A6: 00         NOP                     
52A7: 00         NOP                     
52A8: 00         NOP                     
52A9: FF         RST     0X38            
52AA: 0D         DEC     C               
52AB: 12         LD      (DE),A          
52AC: FF         RST     0X38            
52AD: 00         NOP                     
52AE: 0D         DEC     C               
52AF: 11 12 FF   LD      DE,$FF12        
52B2: 92         SUB     D               
52B3: F2                              
52B4: FF         RST     0X38            
52B5: 00         NOP                     
52B6: 92         SUB     D               
52B7: F1         POP     AF              
52B8: F2                              
52B9: FF         RST     0X38            
52BA: 8D         ADC     A,L             
52BB: 92         SUB     D               
52BC: ED                              
52BD: F2                              
52BE: FF         RST     0X38            
52BF: 00         NOP                     
52C0: 00         NOP                     
52C1: 00         NOP                     
52C2: 00         NOP                     
52C3: 00         NOP                     
52C4: 00         NOP                     
52C5: 8D         ADC     A,L             
52C6: 92         SUB     D               
52C7: ED                              
52C8: F2                              
52C9: F1         POP     AF              
52CA: F2                              
52CB: FF         RST     0X38            
52CC: 00         NOP                     
52CD: 00         NOP                     
52CE: 00         NOP                     
52CF: 00         NOP                     
52D0: 8D         ADC     A,L             
52D1: 92         SUB     D               
52D2: ED                              
52D3: F2                              
52D4: 91         SUB     C               
52D5: 92         SUB     D               
52D6: F1         POP     AF              
52D7: F2                              
52D8: FF         RST     0X38            
52D9: 00         NOP                     
52DA: 00         NOP                     
52DB: 8D         ADC     A,L             
52DC: 92         SUB     D               
52DD: ED                              
52DE: F2                              
52DF: 91         SUB     C               
52E0: 92         SUB     D               
52E1: EC                              
52E2: ED                              
52E3: F1         POP     AF              
52E4: F2                              
52E5: FF         RST     0X38            
52E6: 00         NOP                     
52E7: 00         NOP                     
52E8: 00         NOP                     
52E9: FF         RST     0X38            
52EA: 00         NOP                     
52EB: 00         NOP                     
52EC: 00         NOP                     
52ED: FF         RST     0X38            
52EE: E8 E9      ADD     SP,$E9          
52F0: FF         RST     0X38            
52F1: 00         NOP                     
52F2: E8 EC      ADD     SP,$EC          
52F4: E8 FF      ADD     SP,$FF          
52F6: E8 E9      ADD     SP,$E9          
52F8: FF         RST     0X38            
52F9: 00         NOP                     
52FA: E8 EC      ADD     SP,$EC          
52FC: E8 FF      ADD     SP,$FF          
52FE: E8 EA      ADD     SP,$EA          
5300: E9         JP      (HL)            
5301: EB                              
5302: FF         RST     0X38            
5303: 00         NOP                     
5304: 00         NOP                     
5305: 00         NOP                     
5306: 00         NOP                     
5307: 00         NOP                     
5308: 00         NOP                     
5309: E8 EA      ADD     SP,$EA          
530B: E9         JP      (HL)            
530C: EB                              
530D: EC                              
530E: E8 FF      ADD     SP,$FF          
5310: 00         NOP                     
5311: 00         NOP                     
5312: 00         NOP                     
5313: 00         NOP                     
5314: E8 EA      ADD     SP,$EA          
5316: E9         JP      (HL)            
5317: EB                              
5318: EC                              
5319: E8 EC      ADD     SP,$EC          
531B: E9         JP      (HL)            
531C: FF         RST     0X38            
531D: 00         NOP                     
531E: 00         NOP                     
531F: E8 EA      ADD     SP,$EA          
5321: E9         JP      (HL)            
5322: EB                              
5323: EC                              
5324: E8 EC      ADD     SP,$EC          
5326: EA EC E9   LD      ($E9EC),A       
5329: FF         RST     0X38            
532A: 9D         SBC     L               
532B: 9C         SBC     H               
532C: 0A         LD      A,(BC)          
532D: EA 9C E9   LD      ($E99C),A       
5330: 49         LD      C,C             
5331: 7F         LD      A,A             
5332: 9D         SBC     L               
5333: 09         ADD     HL,BC           
5334: 49         LD      C,C             
5335: 7F         LD      A,A             
5336: 9D         SBC     L               
5337: 29         ADD     HL,HL           
5338: 49         LD      C,C             
5339: 7F         LD      A,A             
533A: 9D         SBC     L               
533B: 49         LD      C,C             
533C: 49         LD      C,C             
533D: 7F         LD      A,A             
533E: 9D         SBC     L               
533F: 69         LD      L,C             
5340: 49         LD      C,C             
5341: 7F         LD      A,A             
5342: 9D         SBC     L               
5343: 89         ADC     A,C             
5344: 49         LD      C,C             
5345: 7F         LD      A,A             
5346: 9D         SBC     L               
5347: A9         XOR     C               
5348: 49         LD      C,C             
5349: 7F         LD      A,A             
534A: 9D         SBC     L               
534B: C9         RET                     
534C: 49         LD      C,C             
534D: 7F         LD      A,A             
534E: 9D         SBC     L               
534F: E9         JP      (HL)            
5350: 49         LD      C,C             
5351: 7F         LD      A,A             
5352: 9E         SBC     (HL)            
5353: 09         ADD     HL,BC           
5354: 49         LD      C,C             
5355: 7F         LD      A,A             
5356: 00         NOP                     
5357: 21 2E 53   LD      HL,$532E        
535A: 11 50 D6   LD      DE,$D650        
535D: 0E 29      LD      C,$29           
535F: 2A         LD      A,(HLI)         
5360: 13         INC     DE              
5361: 12         LD      (DE),A          
5362: 0D         DEC     C               
5363: 20 FA      JR      NZ,$535F        
5365: D5         PUSH    DE              
5366: AF         XOR     A               
5367: E0 D7      LDFF00  ($D7),A         
5369: E0 D8      LDFF00  ($D8),A         
536B: E0 D9      LDFF00  ($D9),A         
536D: E0 DA      LDFF00  ($DA),A         
536F: 4F         LD      C,A             
5370: 47         LD      B,A             
5371: 5F         LD      E,A             
5372: 57         LD      D,A             
5373: FA B0 DB   LD      A,($DBB0)       
5376: CB 37      SET     1,E             
5378: E6 03      AND     $03             
537A: 5F         LD      E,A             
537B: A7         AND     A               
537C: 28 0B      JR      Z,$5389         
537E: 79         LD      A,C             
537F: C6 04      ADD     $04             
5381: 4F         LD      C,A             
5382: 1D         DEC     E               
5383: 7B         LD      A,E             
5384: A7         AND     A               
5385: 20 F7      JR      NZ,$537E        
5387: 06 00      LD      B,$00           
5389: E1         POP     HL              
538A: E5         PUSH    HL              
538B: 21 1E 52   LD      HL,$521E        
538E: 09         ADD     HL,BC           
538F: 7E         LD      A,(HL)          
5390: E0 D7      LDFF00  ($D7),A         
5392: 21 2E 52   LD      HL,$522E        
5395: 09         ADD     HL,BC           
5396: 7E         LD      A,(HL)          
5397: E0 D8      LDFF00  ($D8),A         
5399: 21 3E 52   LD      HL,$523E        
539C: 09         ADD     HL,BC           
539D: 7E         LD      A,(HL)          
539E: E0 D9      LDFF00  ($D9),A         
53A0: 21 4E 52   LD      HL,$524E        
53A3: 09         ADD     HL,BC           
53A4: 7E         LD      A,(HL)          
53A5: E0 DA      LDFF00  ($DA),A         
53A7: E1         POP     HL              
53A8: CD 61 54   CALL    $5461           
53AB: E5         PUSH    HL              
53AC: 21 1E 52   LD      HL,$521E        
53AF: 03         INC     BC              
53B0: 09         ADD     HL,BC           
53B1: 7E         LD      A,(HL)          
53B2: E1         POP     HL              
53B3: 23         INC     HL              
53B4: FE FF      CP      $FF             
53B6: 20 D2      JR      NZ,$538A        
53B8: AF         XOR     A               
53B9: 77         LD      (HL),A          
53BA: AF         XOR     A               
53BB: E0 D7      LDFF00  ($D7),A         
53BD: E0 D8      LDFF00  ($D8),A         
53BF: E0 D9      LDFF00  ($D9),A         
53C1: E0 DA      LDFF00  ($DA),A         
53C3: 4F         LD      C,A             
53C4: 47         LD      B,A             
53C5: 5F         LD      E,A             
53C6: 57         LD      D,A             
53C7: FA B0 DB   LD      A,($DBB0)       
53CA: CB 37      SET     1,E             
53CC: E6 03      AND     $03             
53CE: 5F         LD      E,A             
53CF: A7         AND     A               
53D0: 28 5E      JR      Z,$5430         
53D2: 06 00      LD      B,$00           
53D4: 79         LD      A,C             
53D5: C6 08      ADD     $08             
53D7: 4F         LD      C,A             
53D8: 1D         DEC     E               
53D9: 7B         LD      A,E             
53DA: A7         AND     A               
53DB: 20 F5      JR      NZ,$53D2        
53DD: FA B0 DB   LD      A,($DBB0)       
53E0: E6 03      AND     $03             
53E2: 28 22      JR      Z,$5406         
53E4: FA B0 DB   LD      A,($DBB0)       
53E7: E6 30      AND     $30             
53E9: FE 30      CP      $30             
53EB: 28 08      JR      Z,$53F5         
53ED: 79         LD      A,C             
53EE: C6 04      ADD     $04             
53F0: 4F         LD      C,A             
53F1: 06 00      LD      B,$00           
53F3: 18 11      JR      $5406           
53F5: FA B0 DB   LD      A,($DBB0)       
53F8: E6 03      AND     $03             
53FA: 5F         LD      E,A             
53FB: 06 00      LD      B,$00           
53FD: 79         LD      A,C             
53FE: C6 0B      ADD     $0B             
5400: 4F         LD      C,A             
5401: 1D         DEC     E               
5402: 7B         LD      A,E             
5403: A7         AND     A               
5404: 20 F5      JR      NZ,$53FB        
5406: E5         PUSH    HL              
5407: 21 5E 52   LD      HL,$525E        
540A: 09         ADD     HL,BC           
540B: 7E         LD      A,(HL)          
540C: E0 D7      LDFF00  ($D7),A         
540E: 21 A2 52   LD      HL,$52A2        
5411: 09         ADD     HL,BC           
5412: 7E         LD      A,(HL)          
5413: E0 D8      LDFF00  ($D8),A         
5415: AF         XOR     A               
5416: E0 D9      LDFF00  ($D9),A         
5418: 21 E6 52   LD      HL,$52E6        
541B: 09         ADD     HL,BC           
541C: 7E         LD      A,(HL)          
541D: E0 DA      LDFF00  ($DA),A         
541F: E1         POP     HL              
5420: CD 61 54   CALL    $5461           
5423: E5         PUSH    HL              
5424: 21 5E 52   LD      HL,$525E        
5427: 03         INC     BC              
5428: 09         ADD     HL,BC           
5429: 7E         LD      A,(HL)          
542A: E1         POP     HL              
542B: 23         INC     HL              
542C: FE FF      CP      $FF             
542E: 20 D6      JR      NZ,$5406        
5430: AF         XOR     A               
5431: 47         LD      B,A             
5432: 4F         LD      C,A             
5433: FA B0 DB   LD      A,($DBB0)       
5436: CB 6F      SET     1,E             
5438: 28 01      JR      Z,$543B         
543A: 03         INC     BC              
543B: E5         PUSH    HL              
543C: 21 2A 53   LD      HL,$532A        
543F: 09         ADD     HL,BC           
5440: 7E         LD      A,(HL)          
5441: E0 D7      LDFF00  ($D7),A         
5443: 21 2C 53   LD      HL,$532C        
5446: 09         ADD     HL,BC           
5447: 7E         LD      A,(HL)          
5448: E0 D8      LDFF00  ($D8),A         
544A: 3E 01      LD      A,$01           
544C: E0 D9      LDFF00  ($D9),A         
544E: F0 F7      LD      A,($F7)         
5450: C6 B1      ADD     $B1             
5452: E0 DA      LDFF00  ($DA),A         
5454: E1         POP     HL              
5455: CD 61 54   CALL    $5461           
5458: E5         PUSH    HL              
5459: E1         POP     HL              
545A: 23         INC     HL              
545B: 3E 7F      LD      A,$7F           
545D: 22         LD      (HLI),A         
545E: AF         XOR     A               
545F: 77         LD      (HL),A          
5460: C9         RET                     
5461: F0 D7      LD      A,($D7)         
5463: 22         LD      (HLI),A         
5464: F0 D8      LD      A,($D8)         
5466: 22         LD      (HLI),A         
5467: F0 D9      LD      A,($D9)         
5469: 22         LD      (HLI),A         
546A: F0 DA      LD      A,($DA)         
546C: 77         LD      (HL),A          
546D: C9         RET                     
546E: AF         XOR     A               
546F: EA C0 C3   LD      ($C3C0),A       
5472: FA 96 DB   LD      A,($DB96)       
5475: C7         RST     0X00            
5476: 82         ADD     A,D             
5477: 54         LD      D,H             
5478: FE 54      CP      $54             
547A: 07         RLCA                    
547B: 55         LD      D,L             
547C: 10 55      STOP    $55             
547E: 21 55 FD   LD      HL,$FD55        
5481: 55         LD      D,L             
5482: CD CC 1C   CALL    $1CCC           
5485: CD 22 0B   CALL    $0B22           
5488: CD 76 17   CALL    $1776           
548B: FA 6B C1   LD      A,($C16B)       
548E: FE 04      CP      $04             
5490: 20 6B      JR      NZ,$54FD        
5492: 3E 03      LD      A,$03           
5494: E0 A9      LDFF00  ($A9),A         
5496: 3E 30      LD      A,$30           
5498: E0 AA      LDFF00  ($AA),A         
549A: CD 45 44   CALL    $4445           
549D: AF         XOR     A               
549E: EA 6B C1   LD      ($C16B),A       
54A1: EA 6C C1   LD      ($C16C),A       
54A4: E0 96      LDFF00  ($96),A         
54A6: EA BF C1   LD      ($C1BF),A       
54A9: E0 97      LDFF00  ($97),A         
54AB: EA 4F C1   LD      ($C14F),A       
54AE: EA B2 C1   LD      ($C1B2),A       
54B1: EA B3 C1   LD      ($C1B3),A       
54B4: FA 54 DB   LD      A,($DB54)       
54B7: EA B4 DB   LD      ($DBB4),A       
54BA: 5F         LD      E,A             
54BB: 16 00      LD      D,$00           
54BD: 21 07 57   LD      HL,$5707        
54C0: 19         ADD     HL,DE           
54C1: 7E         LD      A,(HL)          
54C2: A7         AND     A               
54C3: 28 1E      JR      Z,$54E3         
54C5: CB 37      SET     1,E             
54C7: E6 07      AND     $07             
54C9: 3C         INC     A               
54CA: FE 01      CP      $01             
54CC: 20 15      JR      NZ,$54E3        
54CE: FA A2 C5   LD      A,($C5A2)       
54D1: A7         AND     A               
54D2: 3E 00      LD      A,$00           
54D4: 20 0D      JR      NZ,$54E3        
54D6: 21 00 D8   LD      HL,$D800        
54D9: 19         ADD     HL,DE           
54DA: 7E         LD      A,(HL)          
54DB: E6 20      AND     $20             
54DD: 3E 00      LD      A,$00           
54DF: 28 02      JR      Z,$54E3         
54E1: 3E 01      LD      A,$01           
54E3: EA B1 C1   LD      ($C1B1),A       
54E6: FA B4 DB   LD      A,($DBB4)       
54E9: EA B4 C1   LD      ($C1B4),A       
54EC: F0 40      LD      A,($40)         
54EE: E6 DF      AND     $DF             
54F0: EA FD D6   LD      ($D6FD),A       
54F3: E0 40      LDFF00  ($40),A         
54F5: CD 36 56   CALL    $5636           
54F8: 3E 08      LD      A,$08           
54FA: EA FF D6   LD      ($D6FF),A       
54FD: C9         RET                     
54FE: 3E 0B      LD      A,$0B           
5500: EA FE D6   LD      ($D6FE),A       
5503: CD 45 44   CALL    $4445           
5506: C9         RET                     
5507: 3E 0E      LD      A,$0E           
5509: EA FE D6   LD      ($D6FE),A       
550C: CD 45 44   CALL    $4445           
550F: C9         RET                     
5510: CD C3 17   CALL    $17C3           
5513: FA 6B C1   LD      A,($C16B)       
5516: FE 04      CP      $04             
5518: 20 06      JR      NZ,$5520        
551A: CD 45 44   CALL    $4445           
551D: CD 07 49   CALL    $4907           
5520: C9         RET                     
5521: FA 9F C1   LD      A,($C19F)       
5524: A7         AND     A               
5525: C2 F0 55   JP      NZ,$55F0        
5528: F0 CC      LD      A,($CC)         
552A: E6 10      AND     $10             
552C: 28 66      JR      Z,$5594         
552E: FA B4 DB   LD      A,($DBB4)       
5531: 5F         LD      E,A             
5532: 16 00      LD      D,$00           
5534: 21 07 57   LD      HL,$5707        
5537: 19         ADD     HL,DE           
5538: 7E         LD      A,(HL)          
5539: A7         AND     A               
553A: 28 23      JR      Z,$555F         
553C: 5F         LD      E,A             
553D: E6 F0      AND     $F0             
553F: 20 15      JR      NZ,$5556        
5541: FA A2 C5   LD      A,($C5A2)       
5544: A7         AND     A               
5545: 20 18      JR      NZ,$555F        
5547: D5         PUSH    DE              
5548: FA B4 DB   LD      A,($DBB4)       
554B: 5F         LD      E,A             
554C: 21 00 D8   LD      HL,$D800        
554F: 19         ADD     HL,DE           
5550: D1         POP     DE              
5551: 7E         LD      A,(HL)          
5552: E6 20      AND     $20             
5554: 28 09      JR      Z,$555F         
5556: 16 00      LD      D,$00           
5558: 21 B7 56   LD      HL,$56B7        
555B: 19         ADD     HL,DE           
555C: 7E         LD      A,(HL)          
555D: 18 23      JR      $5582           
555F: FA B4 DB   LD      A,($DBB4)       
5562: FE 24      CP      $24             
5564: 28 04      JR      Z,$556A         
5566: FE 34      CP      $34             
5568: 20 04      JR      NZ,$556E        
556A: 3E 76      LD      A,$76           
556C: 18 14      JR      $5582           
556E: 1F         RRA                     
556F: E6 07      AND     $07             
5571: 5F         LD      E,A             
5572: FA B4 DB   LD      A,($DBB4)       
5575: 1F         RRA                     
5576: 1F         RRA                     
5577: E6 38      AND     $38             
5579: B3         OR      E               
557A: 5F         LD      E,A             
557B: 16 00      LD      D,$00           
557D: 21 77 56   LD      HL,$5677        
5580: 19         ADD     HL,DE           
5581: 7E         LD      A,(HL)          
5582: CD 97 21   CALL    $2197           
5585: FA B4 DB   LD      A,($DBB4)       
5588: FE 70      CP      $70             
558A: 3E 01      LD      A,$01           
558C: 30 02      JR      NC,$5590        
558E: 3E 81      LD      A,$81           
5590: EA 9F C1   LD      ($C19F),A       
5593: C9         RET                     
5594: FA 03 00   LD      A,($0003)       
5597: A7         AND     A               
5598: 28 3D      JR      Z,$55D7         
559A: F0 CB      LD      A,($CB)         
559C: FE 60      CP      $60             
559E: 20 37      JR      NZ,$55D7        
55A0: 3E 0B      LD      A,$0B           
55A2: EA 95 DB   LD      ($DB95),A       
55A5: CD 09 09   CALL    $0909           
55A8: 3E 00      LD      A,$00           
55AA: EA 01 D4   LD      ($D401),A       
55AD: EA 02 D4   LD      ($D402),A       
55B0: FA B4 DB   LD      A,($DBB4)       
55B3: EA 03 D4   LD      ($D403),A       
55B6: 3E 48      LD      A,$48           
55B8: EA 04 D4   LD      ($D404),A       
55BB: 3E 52      LD      A,$52           
55BD: EA 05 D4   LD      ($D405),A       
55C0: F0 98      LD      A,($98)         
55C2: CB 37      SET     1,E             
55C4: E6 0F      AND     $0F             
55C6: 5F         LD      E,A             
55C7: F0 99      LD      A,($99)         
55C9: D6 08      SUB     $08             
55CB: E6 F0      AND     $F0             
55CD: B3         OR      E               
55CE: EA 16 D4   LD      ($D416),A       
55D1: 3E 07      LD      A,$07           
55D3: EA 96 DB   LD      ($DB96),A       
55D6: C9         RET                     
55D7: 1E 40      LD      E,$40           
55D9: FA 03 00   LD      A,($0003)       
55DC: A7         AND     A               
55DD: 20 02      JR      NZ,$55E1        
55DF: 1E 60      LD      E,$60           
55E1: F0 CC      LD      A,($CC)         
55E3: A3         AND     E               
55E4: 28 0A      JR      Z,$55F0         
55E6: AF         XOR     A               
55E7: EA 6B C1   LD      ($C16B),A       
55EA: EA 6C C1   LD      ($C16C),A       
55ED: CD 45 44   CALL    $4445           
55F0: CD 56 56   CALL    $5656           
55F3: CD 1F 58   CALL    $581F           
55F6: CD F7 59   CALL    $59F7           
55F9: C9         RET                     
55FA: CD 50 67   CALL    $6750           
55FD: CD 76 17   CALL    $1776           
5600: FA 6B C1   LD      A,($C16B)       
5603: FE 04      CP      $04             
5605: 20 4E      JR      NZ,$5655        
5607: AF         XOR     A               
5608: EA 0A C5   LD      ($C50A),A       
560B: EA 16 C1   LD      ($C116),A       
560E: E0 96      LDFF00  ($96),A         
5610: E0 97      LDFF00  ($97),A         
5612: EA 67 C1   LD      ($C167),A       
5615: 3E 07      LD      A,$07           
5617: E0 A9      LDFF00  ($A9),A         
5619: 3E 70      LD      A,$70           
561B: E0 AA      LDFF00  ($AA),A         
561D: 3E 0B      LD      A,$0B           
561F: EA 95 DB   LD      ($DB95),A       
5622: E0 BC      LDFF00  ($BC),A         
5624: 3E 02      LD      A,$02           
5626: EA 96 DB   LD      ($DB96),A       
5629: FA A5 DB   LD      A,($DBA5)       
562C: A7         AND     A               
562D: 3E 06      LD      A,$06           
562F: 20 02      JR      NZ,$5633        
5631: 3E 07      LD      A,$07           
5633: EA FE D6   LD      ($D6FE),A       
5636: 21 24 C1   LD      HL,$C124        
5639: 1E 00      LD      E,$00           
563B: AF         XOR     A               
563C: 22         LD      (HLI),A         
563D: 1C         INC     E               
563E: 7B         LD      A,E             
563F: FE 0C      CP      $0C             
5641: 20 F8      JR      NZ,$563B        
5643: 3E 80      LD      A,$80           
5645: EA 9A DB   LD      ($DB9A),A       
5648: 3E 06      LD      A,$06           
564A: E0 4B      LDFF00  ($4B),A         
564C: 3E 08      LD      A,$08           
564E: EA 50 C1   LD      ($C150),A       
5651: AF         XOR     A               
5652: EA 4F C1   LD      ($C14F),A       
5655: C9         RET                     
5656: 21 9C C0   LD      HL,$C09C        
5659: FA 54 DB   LD      A,($DB54)       
565C: 1F         RRA                     
565D: E6 78      AND     $78             
565F: C6 18      ADD     $18             
5661: 22         LD      (HLI),A         
5662: FA 54 DB   LD      A,($DB54)       
5665: CB 37      SET     1,E             
5667: 1F         RRA                     
5668: E6 78      AND     $78             
566A: C6 18      ADD     $18             
566C: 22         LD      (HLI),A         
566D: 36 3E      LD      (HL),$3E        
566F: 23         INC     HL              
5670: F0 E7      LD      A,($E7)         
5672: 17         RLA                     
5673: E6 10      AND     $10             
5675: 77         LD      (HL),A          
5676: C9         RET                     
5677: 6C         LD      L,H             
5678: 6C         LD      L,H             
5679: 6C         LD      L,H             
567A: 6B         LD      L,E             
567B: 6C         LD      L,H             
567C: 6C         LD      L,H             
567D: 6C         LD      L,H             
567E: 6C         LD      L,H             
567F: 76         HALT                    
5680: 76         HALT                    
5681: 79         LD      A,C             
5682: 79         LD      A,C             
5683: 79         LD      A,C             
5684: 79         LD      A,C             
5685: 79         LD      A,C             
5686: 79         LD      A,C             
5687: 6A         LD      L,D             
5688: 6A         LD      L,D             
5689: 72         LD      (HL),D          
568A: 7A         LD      A,D             
568B: 78         LD      A,B             
568C: 78         LD      A,B             
568D: 71         LD      (HL),C          
568E: 71         LD      (HL),C          
568F: 6A         LD      L,D             
5690: 6A         LD      L,D             
5691: 72         LD      (HL),D          
5692: 70         LD      (HL),B          
5693: 78         LD      A,B             
5694: 78         LD      A,B             
5695: 71         LD      (HL),C          
5696: 71         LD      (HL),C          
5697: 6A         LD      L,D             
5698: 6E         LD      L,(HL)          
5699: 69         LD      L,C             
569A: 69         LD      L,C             
569B: 69         LD      L,C             
569C: 69         LD      L,C             
569D: 77         LD      (HL),A          
569E: 71         LD      (HL),C          
569F: 6E         LD      L,(HL)          
56A0: 6E         LD      L,(HL)          
56A1: 69         LD      L,C             
56A2: 69         LD      L,C             
56A3: 69         LD      L,C             
56A4: 69         LD      L,C             
56A5: 77         LD      (HL),A          
56A6: 77         LD      (HL),A          
56A7: 7B         LD      A,E             
56A8: 7B         LD      A,E             
56A9: 6D         LD      L,L             
56AA: 62         LD      H,D             
56AB: 74         LD      (HL),H          
56AC: 74         LD      (HL),H          
56AD: 6F         LD      L,A             
56AE: 68         LD      L,B             
56AF: 73         LD      (HL),E          
56B0: 73         LD      (HL),E          
56B1: 73         LD      (HL),E          
56B2: 74         LD      (HL),H          
56B3: 74         LD      (HL),H          
56B4: 74         LD      (HL),H          
56B5: 75         LD      (HL),L          
56B6: 68         LD      L,B             
56B7: 00         NOP                     
56B8: D9         RETI                    
56B9: C0         RET     NZ              
56BA: C1         POP     BC              
56BB: C2 C3 C4   JP      NZ,$C4C3        
56BE: C5         PUSH    BC              
56BF: C6 C7      ADD     $C7             
56C1: C8         RET     Z               
56C2: C9         RET                     
56C3: CA CB CC   JP      Z,$CCCB         
56C6: CD 00 56   CALL    $5600           
56C9: 57         LD      D,A             
56CA: 58         LD      E,B             
56CB: 59         LD      E,C             
56CC: 5A         LD      E,D             
56CD: 5B         LD      E,E             
56CE: 5C         LD      E,H             
56CF: 5D         LD      E,L             
56D0: 00         NOP                     
56D1: 00         NOP                     
56D2: 00         NOP                     
56D3: 00         NOP                     
56D4: 00         NOP                     
56D5: 00         NOP                     
56D6: 00         NOP                     
56D7: 00         NOP                     
56D8: 7C         LD      A,H             
56D9: 67         LD      H,A             
56DA: 00         NOP                     
56DB: 00         NOP                     
56DC: 80         ADD     A,B             
56DD: 65         LD      H,L             
56DE: 00         NOP                     
56DF: 64         LD      H,H             
56E0: 88         ADC     A,B             
56E1: 00         NOP                     
56E2: 00         NOP                     
56E3: 00         NOP                     
56E4: 00         NOP                     
56E5: 00         NOP                     
56E6: 00         NOP                     
56E7: 00         NOP                     
56E8: 5E         LD      E,(HL)          
56E9: 5F         LD      E,A             
56EA: 7F         LD      A,A             
56EB: 7E         LD      A,(HL)          
56EC: 7D         LD      A,L             
56ED: 82         ADD     A,D             
56EE: 84         ADD     A,H             
56EF: 85         ADD     A,L             
56F0: 86         ADD     A,(HL)          
56F1: 87         ADD     A,A             
56F2: 81         ADD     A,C             
56F3: 66         LD      H,(HL)          
56F4: 83         ADD     A,E             
56F5: 5E         LD      E,(HL)          
56F6: 63         LD      H,E             
56F7: 00         NOP                     
56F8: 61         LD      H,C             
56F9: 00         NOP                     
56FA: 00         NOP                     
56FB: 00         NOP                     
56FC: 00         NOP                     
56FD: 00         NOP                     
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
5708: 00         NOP                     
5709: 00         NOP                     
570A: 00         NOP                     
570B: 00         NOP                     
570C: 00         NOP                     
570D: 3E 00      LD      A,$00           
570F: 0E 00      LD      C,$00           
5711: 39         ADD     HL,SP           
5712: 00         NOP                     
5713: 00         NOP                     
5714: 00         NOP                     
5715: 17         RLA                     
5716: 00         NOP                     
5717: 18 3D      JR      $5756           
5719: 00         NOP                     
571A: 00         NOP                     
571B: 00         NOP                     
571C: 00         NOP                     
571D: 06 0C      LD      B,$0C           
571F: 00         NOP                     
5720: 00         NOP                     
5721: 00         NOP                     
5722: 00         NOP                     
5723: 00         NOP                     
5724: 00         NOP                     
5725: 00         NOP                     
5726: 00         NOP                     
5727: 00         NOP                     
5728: 00         NOP                     
5729: 00         NOP                     
572A: 00         NOP                     
572B: 12         LD      (DE),A          
572C: 00         NOP                     
572D: 00         NOP                     
572E: 00         NOP                     
572F: 07         RLCA                    
5730: 00         NOP                     
5731: 00         NOP                     
5732: 14         INC     D               
5733: 00         NOP                     
5734: 00         NOP                     
5735: 00         NOP                     
5736: 00         NOP                     
5737: 33         INC     SP              
5738: 3D         DEC     A               
5739: 00         NOP                     
573A: 00         NOP                     
573B: 00         NOP                     
573C: 00         NOP                     
573D: 05         DEC     B               
573E: 00         NOP                     
573F: 00         NOP                     
5740: 00         NOP                     
5741: 00         NOP                     
5742: 00         NOP                     
5743: 00         NOP                     
5744: 00         NOP                     
5745: 00         NOP                     
5746: 29         ADD     HL,HL           
5747: 00         NOP                     
5748: 03         INC     BC              
5749: 00         NOP                     
574A: 00         NOP                     
574B: 00         NOP                     
574C: 25         DEC     H               
574D: 00         NOP                     
574E: 00         NOP                     
574F: 00         NOP                     
5750: 00         NOP                     
5751: 00         NOP                     
5752: 3D         DEC     A               
5753: 00         NOP                     
5754: 00         NOP                     
5755: 00         NOP                     
5756: 00         NOP                     
5757: 00         NOP                     
5758: 00         NOP                     
5759: 00         NOP                     
575A: 00         NOP                     
575B: 00         NOP                     
575C: 00         NOP                     
575D: 00         NOP                     
575E: 00         NOP                     
575F: 00         NOP                     
5760: 00         NOP                     
5761: 00         NOP                     
5762: 00         NOP                     
5763: 00         NOP                     
5764: 00         NOP                     
5765: 00         NOP                     
5766: 00         NOP                     
5767: 00         NOP                     
5768: 00         NOP                     
5769: 00         NOP                     
576A: 00         NOP                     
576B: 0D         DEC     C               
576C: 22         LD      (HLI),A         
576D: 00         NOP                     
576E: 00         NOP                     
576F: 00         NOP                     
5770: 00         NOP                     
5771: 00         NOP                     
5772: 00         NOP                     
5773: 00         NOP                     
5774: 00         NOP                     
5775: 00         NOP                     
5776: 00         NOP                     
5777: 00         NOP                     
5778: 00         NOP                     
5779: 00         NOP                     
577A: 00         NOP                     
577B: 00         NOP                     
577C: 00         NOP                     
577D: 00         NOP                     
577E: 00         NOP                     
577F: 00         NOP                     
5780: 00         NOP                     
5781: 00         NOP                     
5782: 00         NOP                     
5783: 00         NOP                     
5784: 00         NOP                     
5785: 00         NOP                     
5786: 00         NOP                     
5787: 02         LD      (BC),A          
5788: 21 3B 36   LD      HL,$363B        
578B: 00         NOP                     
578C: 00         NOP                     
578D: 00         NOP                     
578E: 00         NOP                     
578F: 3D         DEC     A               
5790: 00         NOP                     
5791: 37         SCF                     
5792: 00         NOP                     
5793: 16 00      LD      D,$00           
5795: 00         NOP                     
5796: 00         NOP                     
5797: 00         NOP                     
5798: 00         NOP                     
5799: 00         NOP                     
579A: 26 00      LD      H,$00           
579C: 00         NOP                     
579D: 00         NOP                     
579E: 00         NOP                     
579F: 00         NOP                     
57A0: 00         NOP                     
57A1: 00         NOP                     
57A2: 09         ADD     HL,BC           
57A3: 0B         DEC     BC              
57A4: 09         ADD     HL,BC           
57A5: 00         NOP                     
57A6: 00         NOP                     
57A7: 00         NOP                     
57A8: 35         DEC     (HL)            
57A9: 3C         INC     A               
57AA: 00         NOP                     
57AB: 3D         DEC     A               
57AC: 00         NOP                     
57AD: 00         NOP                     
57AE: 00         NOP                     
57AF: 00         NOP                     
57B0: 00         NOP                     
57B1: 00         NOP                     
57B2: 00         NOP                     
57B3: 0A         LD      A,(BC)          
57B4: 00         NOP                     
57B5: 00         NOP                     
57B6: 00         NOP                     
57B7: 3A         LD      A,(HLD)         
57B8: 34         INC     (HL)            
57B9: 3D         DEC     A               
57BA: 28 00      JR      Z,$57BC         
57BC: 13         INC     DE              
57BD: 07         RLCA                    
57BE: 00         NOP                     
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
57D4: 00         NOP                     
57D5: 00         NOP                     
57D6: 00         NOP                     
57D7: 00         NOP                     
57D8: 00         NOP                     
57D9: 04         INC     B               
57DA: 11 00 00   LD      DE,$0000        
57DD: 38 00      JR      C,$57DF         
57DF: 00         NOP                     
57E0: 15         DEC     D               
57E1: 00         NOP                     
57E2: 3D         DEC     A               
57E3: 00         NOP                     
57E4: 00         NOP                     
57E5: 00         NOP                     
57E6: 00         NOP                     
57E7: 00         NOP                     
57E8: 00         NOP                     
57E9: 00         NOP                     
57EA: 41         LD      B,C             
57EB: 00         NOP                     
57EC: 00         NOP                     
57ED: 00         NOP                     
57EE: 00         NOP                     
57EF: 3D         DEC     A               
57F0: 00         NOP                     
57F1: 00         NOP                     
57F2: 00         NOP                     
57F3: 00         NOP                     
57F4: 00         NOP                     
57F5: 08 00 00   LD      ($0000),SP      
57F8: 00         NOP                     
57F9: 01 00 00   LD      BC,$0000        
57FC: 00         NOP                     
57FD: 3F         CCF                     
57FE: 00         NOP                     
57FF: 00         NOP                     
5800: 00         NOP                     
5801: 00         NOP                     
5802: 00         NOP                     
5803: 00         NOP                     
5804: 00         NOP                     
5805: 00         NOP                     
5806: 00         NOP                     
5807: F0 F6      LD      A,($F6)         
5809: 5F         LD      E,A             
580A: 16 00      LD      D,$00           
580C: 21 07 57   LD      HL,$5707        
580F: 19         ADD     HL,DE           
5810: 5E         LD      E,(HL)          
5811: 21 B7 56   LD      HL,$56B7        
5814: 19         ADD     HL,DE           
5815: 7E         LD      A,(HL)          
5816: C3 97 21   JP      $2197           
5819: 00         NOP                     
581A: 01 FF 00   LD      BC,$00FF        
581D: F0 10      LD      A,($10)         
581F: FA B4 DB   LD      A,($DBB4)       
5822: E0 D7      LDFF00  ($D7),A         
5824: FA B3 C1   LD      A,($C1B3)       
5827: 21 B2 C1   LD      HL,$C1B2        
582A: B6         OR      (HL)            
582B: 21 9F C1   LD      HL,$C19F        
582E: B6         OR      (HL)            
582F: C2 ED 58   JP      NZ,$58ED        
5832: F0 CB      LD      A,($CB)         
5834: 4F         LD      C,A             
5835: 21 82 C1   LD      HL,$C182        
5838: E6 0F      AND     $0F             
583A: 20 04      JR      NZ,$5840        
583C: AF         XOR     A               
583D: 77         LD      (HL),A          
583E: 18 0B      JR      $584B           
5840: 7E         LD      A,(HL)          
5841: 3C         INC     A               
5842: 77         LD      (HL),A          
5843: FE 18      CP      $18             
5845: 20 04      JR      NZ,$584B        
5847: 36 15      LD      (HL),$15        
5849: 18 03      JR      $584E           
584B: F0 CC      LD      A,($CC)         
584D: 4F         LD      C,A             
584E: 79         LD      A,C             
584F: E6 03      AND     $03             
5851: 5F         LD      E,A             
5852: 16 00      LD      D,$00           
5854: 21 19 58   LD      HL,$5819        
5857: 19         ADD     HL,DE           
5858: FA B4 DB   LD      A,($DBB4)       
585B: 57         LD      D,A             
585C: E6 F0      AND     $F0             
585E: 5F         LD      E,A             
585F: 7A         LD      A,D             
5860: 86         ADD     A,(HL)          
5861: E6 0F      AND     $0F             
5863: B3         OR      E               
5864: EA B4 DB   LD      ($DBB4),A       
5867: 79         LD      A,C             
5868: 1F         RRA                     
5869: 1F         RRA                     
586A: E6 03      AND     $03             
586C: 5F         LD      E,A             
586D: 16 00      LD      D,$00           
586F: 21 1C 58   LD      HL,$581C        
5872: 19         ADD     HL,DE           
5873: FA B4 DB   LD      A,($DBB4)       
5876: 86         ADD     A,(HL)          
5877: 21 D7 FF   LD      HL,$FFD7        
587A: EA B4 DB   LD      ($DBB4),A       
587D: BE         CP      (HL)            
587E: 28 6D      JR      Z,$58ED         
5880: 5F         LD      E,A             
5881: 16 00      LD      D,$00           
5883: 21 00 D8   LD      HL,$D800        
5886: 19         ADD     HL,DE           
5887: FA A2 C5   LD      A,($C5A2)       
588A: A7         AND     A               
588B: 20 16      JR      NZ,$58A3        
588D: 7E         LD      A,(HL)          
588E: E6 FF      AND     $FF             
5890: 20 11      JR      NZ,$58A3        
5892: FA 7B C1   LD      A,($C17B)       
5895: A7         AND     A               
5896: 20 0B      JR      NZ,$58A3        
5898: 3E 09      LD      A,$09           
589A: E0 F2      LDFF00  ($F2),A         
589C: F0 D7      LD      A,($D7)         
589E: EA B4 DB   LD      ($DBB4),A       
58A1: 18 4A      JR      $58ED           
58A3: CD 33 6E   CALL    $6E33           
58A6: 21 07 57   LD      HL,$5707        
58A9: 19         ADD     HL,DE           
58AA: 7E         LD      A,(HL)          
58AB: A7         AND     A               
58AC: 28 30      JR      Z,$58DE         
58AE: CB 37      SET     1,E             
58B0: E6 07      AND     $07             
58B2: 3C         INC     A               
58B3: 4F         LD      C,A             
58B4: FE 01      CP      $01             
58B6: 20 0F      JR      NZ,$58C7        
58B8: FA A2 C5   LD      A,($C5A2)       
58BB: A7         AND     A               
58BC: 20 20      JR      NZ,$58DE        
58BE: 21 00 D8   LD      HL,$D800        
58C1: 19         ADD     HL,DE           
58C2: 7E         LD      A,(HL)          
58C3: E6 20      AND     $20             
58C5: 28 17      JR      Z,$58DE         
58C7: FA B1 C1   LD      A,($C1B1)       
58CA: A7         AND     A               
58CB: 20 05      JR      NZ,$58D2        
58CD: 3E 10      LD      A,$10           
58CF: EA B2 C1   LD      ($C1B2),A       
58D2: 79         LD      A,C             
58D3: EA B1 C1   LD      ($C1B1),A       
58D6: FA B4 DB   LD      A,($DBB4)       
58D9: EA B4 C1   LD      ($C1B4),A       
58DC: 18 0F      JR      $58ED           
58DE: FA B1 C1   LD      A,($C1B1)       
58E1: A7         AND     A               
58E2: 28 09      JR      Z,$58ED         
58E4: AF         XOR     A               
58E5: EA B1 C1   LD      ($C1B1),A       
58E8: 3E 10      LD      A,$10           
58EA: EA B3 C1   LD      ($C1B3),A       
58ED: 21 80 C0   LD      HL,$C080        
58F0: FA B4 DB   LD      A,($DBB4)       
58F3: 1F         RRA                     
58F4: E6 78      AND     $78             
58F6: C6 14      ADD     $14             
58F8: 5F         LD      E,A             
58F9: FA B4 DB   LD      A,($DBB4)       
58FC: CB 37      SET     1,E             
58FE: 1F         RRA                     
58FF: E6 78      AND     $78             
5901: C6 14      ADD     $14             
5903: 57         LD      D,A             
5904: 7B         LD      A,E             
5905: 22         LD      (HLI),A         
5906: 7A         LD      A,D             
5907: 22         LD      (HLI),A         
5908: 36 F0      LD      (HL),$F0        
590A: 23         INC     HL              
590B: 36 00      LD      (HL),$00        
590D: 23         INC     HL              
590E: 7B         LD      A,E             
590F: 22         LD      (HLI),A         
5910: 7A         LD      A,D             
5911: C6 08      ADD     $08             
5913: 22         LD      (HLI),A         
5914: 36 F0      LD      (HL),$F0        
5916: 23         INC     HL              
5917: 36 20      LD      (HL),$20        
5919: F0 E7      LD      A,($E7)         
591B: E6 10      AND     $10             
591D: 20 3B      JR      NZ,$595A        
591F: 21 88 C0   LD      HL,$C088        
5922: 7B         LD      A,E             
5923: C6 04      ADD     $04             
5925: 22         LD      (HLI),A         
5926: 7A         LD      A,D             
5927: C6 F6      ADD     $F6             
5929: 22         LD      (HLI),A         
592A: 3E F6      LD      A,$F6           
592C: 22         LD      (HLI),A         
592D: 3E 00      LD      A,$00           
592F: 22         LD      (HLI),A         
5930: 7B         LD      A,E             
5931: C6 04      ADD     $04             
5933: 22         LD      (HLI),A         
5934: 7A         LD      A,D             
5935: C6 13      ADD     $13             
5937: 22         LD      (HLI),A         
5938: 3E F6      LD      A,$F6           
593A: 22         LD      (HLI),A         
593B: 3E 20      LD      A,$20           
593D: 22         LD      (HLI),A         
593E: 7B         LD      A,E             
593F: C6 F6      ADD     $F6             
5941: 22         LD      (HLI),A         
5942: 7A         LD      A,D             
5943: C6 04      ADD     $04             
5945: 22         LD      (HLI),A         
5946: 3E F8      LD      A,$F8           
5948: 22         LD      (HLI),A         
5949: 3E 00      LD      A,$00           
594B: 22         LD      (HLI),A         
594C: 7B         LD      A,E             
594D: C6 0B      ADD     $0B             
594F: 22         LD      (HLI),A         
5950: 7A         LD      A,D             
5951: C6 04      ADD     $04             
5953: 22         LD      (HLI),A         
5954: 3E F8      LD      A,$F8           
5956: 22         LD      (HLI),A         
5957: 3E 40      LD      A,$40           
5959: 22         LD      (HLI),A         
595A: C9         RET                     
595B: F8 F8      LDHL    SP,$F8          
595D: F2                              
595E: 00         NOP                     
595F: F8 00      LDHL    SP,$00          
5961: F4                              
5962: 00         NOP                     
5963: F8 08      LDHL    SP,$08          
5965: F4                              
5966: 20 F8      JR      NZ,$5960        
5968: 10 F2      STOP    $F2             
596A: 20 08      JR      NZ,$5974        
596C: F8 F2      LDHL    SP,$F2          
596E: 40         LD      B,B             
596F: 08 00 F4   LD      ($F400),SP      
5972: 40         LD      B,B             
5973: 08 08 F4   LD      ($F408),SP      
5976: 60         LD      H,B             
5977: 08 10 F2   LD      ($F210),SP      
597A: 60         LD      H,B             
597B: FA FA F2   LD      A,($F2FA)       
597E: 00         NOP                     
597F: FA 02 F4   LD      A,($F402)       
5982: 00         NOP                     
5983: FA 06 F4   LD      A,($F406)       
5986: 20 FA      JR      NZ,$5982        
5988: 0E F2      LD      C,$F2           
598A: 20 06      JR      NZ,$5992        
598C: FA F2 40   LD      A,($40F2)       
598F: 06 02      LD      B,$02           
5991: F4                              
5992: 40         LD      B,B             
5993: 06 06      LD      B,$06           
5995: F4                              
5996: 60         LD      H,B             
5997: 06 0E      LD      B,$0E           
5999: F2                              
599A: 60         LD      H,B             
599B: FC                              
599C: FC                              
599D: F2                              
599E: 00         NOP                     
599F: FC                              
59A0: 04         INC     B               
59A1: F4                              
59A2: 00         NOP                     
59A3: FC                              
59A4: 04         INC     B               
59A5: F4                              
59A6: 20 FC      JR      NZ,$59A4        
59A8: 0C         INC     C               
59A9: F2                              
59AA: 20 04      JR      NZ,$59B0        
59AC: FC                              
59AD: F2                              
59AE: 40         LD      B,B             
59AF: 04         INC     B               
59B0: 04         INC     B               
59B1: F4                              
59B2: 40         LD      B,B             
59B3: 04         INC     B               
59B4: 04         INC     B               
59B5: F4                              
59B6: 60         LD      H,B             
59B7: 04         INC     B               
59B8: 0C         INC     C               
59B9: F2                              
59BA: 60         LD      H,B             
59BB: FE FE      CP      $FE             
59BD: F2                              
59BE: 00         NOP                     
59BF: FE 04      CP      $04             
59C1: F4                              
59C2: 00         NOP                     
59C3: FE 04      CP      $04             
59C5: F4                              
59C6: 20 FE      JR      NZ,$59C6        
59C8: 0A         LD      A,(BC)          
59C9: F2                              
59CA: 20 02      JR      NZ,$59CE        
59CC: FE F2      CP      $F2             
59CE: 40         LD      B,B             
59CF: 02         LD      (BC),A          
59D0: 04         INC     B               
59D1: F4                              
59D2: 40         LD      B,B             
59D3: 02         LD      (BC),A          
59D4: 04         INC     B               
59D5: F4                              
59D6: 60         LD      H,B             
59D7: 02         LD      (BC),A          
59D8: 0A         LD      A,(BC)          
59D9: F2                              
59DA: 60         LD      H,B             
59DB: 20 00      JR      NZ,$59DD        
59DD: 22         LD      (HLI),A         
59DE: 00         NOP                     
59DF: 24         INC     H               
59E0: 00         NOP                     
59E1: 26 00      LD      H,$00           
59E3: 28 00      JR      Z,$59E5         
59E5: 2A         LD      A,(HLI)         
59E6: 00         NOP                     
59E7: 2C         INC     L               
59E8: 00         NOP                     
59E9: 2E 00      LD      L,$00           
59EB: 2C         INC     L               
59EC: 00         NOP                     
59ED: 2E 00      LD      L,$00           
59EF: 28 78      JR      Z,$5A69         
59F1: 28 78      JR      Z,$5A6B         
59F3: 28 28      JR      Z,$5A1D         
59F5: 78         LD      A,B             
59F6: 78         LD      A,B             
59F7: FA 40 C3   LD      A,($C340)       
59FA: F5         PUSH    AF              
59FB: CD 03 5A   CALL    $5A03           
59FE: F1         POP     AF              
59FF: EA 40 C3   LD      ($C340),A       
5A02: C9         RET                     
5A03: FA B3 C1   LD      A,($C1B3)       
5A06: A7         AND     A               
5A07: 28 07      JR      Z,$5A10         
5A09: 3D         DEC     A               
5A0A: EA B3 C1   LD      ($C1B3),A       
5A0D: 2F         CPL                     
5A0E: 18 0A      JR      $5A1A           
5A10: FA B2 C1   LD      A,($C1B2)       
5A13: A7         AND     A               
5A14: 28 0A      JR      Z,$5A20         
5A16: 3D         DEC     A               
5A17: EA B2 C1   LD      ($C1B2),A       
5A1A: 1F         RRA                     
5A1B: 1F         RRA                     
5A1C: E6 03      AND     $03             
5A1E: 18 09      JR      $5A29           
5A20: FA B1 C1   LD      A,($C1B1)       
5A23: A7         AND     A               
5A24: CA C1 5A   JP      Z,$5AC1         
5A27: 3E 00      LD      A,$00           
5A29: EA B0 C1   LD      ($C1B0),A       
5A2C: E0 F1      LDFF00  ($F1),A         
5A2E: 3E 00      LD      A,$00           
5A30: EA C0 C3   LD      ($C3C0),A       
5A33: 3E 08      LD      A,$08           
5A35: EA 40 C3   LD      ($C340),A       
5A38: 3E 00      LD      A,$00           
5A3A: EA 23 C1   LD      ($C123),A       
5A3D: E0 ED      LDFF00  ($ED),A         
5A3F: 1E 00      LD      E,$00           
5A41: FA B4 C1   LD      A,($C1B4)       
5A44: FE 70      CP      $70             
5A46: 38 02      JR      C,$5A4A         
5A48: 1E 02      LD      E,$02           
5A4A: E6 0F      AND     $0F             
5A4C: FE 08      CP      $08             
5A4E: 30 01      JR      NC,$5A51        
5A50: 1C         INC     E               
5A51: 16 00      LD      D,$00           
5A53: 21 EF 59   LD      HL,$59EF        
5A56: 19         ADD     HL,DE           
5A57: 7E         LD      A,(HL)          
5A58: E0 EE      LDFF00  ($EE),A         
5A5A: 21 F3 59   LD      HL,$59F3        
5A5D: 19         ADD     HL,DE           
5A5E: 7E         LD      A,(HL)          
5A5F: E0 EC      LDFF00  ($EC),A         
5A61: FA B0 C1   LD      A,($C1B0)       
5A64: 17         RLA                     
5A65: 17         RLA                     
5A66: 17         RLA                     
5A67: 17         RLA                     
5A68: 17         RLA                     
5A69: E6 E0      AND     $E0             
5A6B: 5F         LD      E,A             
5A6C: 16 00      LD      D,$00           
5A6E: 21 5B 59   LD      HL,$595B        
5A71: 19         ADD     HL,DE           
5A72: 3E 08      LD      A,$08           
5A74: EA C0 C3   LD      ($C3C0),A       
5A77: AF         XOR     A               
5A78: E0 F5      LDFF00  ($F5),A         
5A7A: 0E 08      LD      C,$08           
5A7C: CD 26 3D   CALL    $3D26           
5A7F: FA B0 C1   LD      A,($C1B0)       
5A82: FE 00      CP      $00             
5A84: 20 3B      JR      NZ,$5AC1        
5A86: FA B1 C1   LD      A,($C1B1)       
5A89: 3D         DEC     A               
5A8A: FE 80      CP      $80             
5A8C: 30 33      JR      NC,$5AC1        
5A8E: E0 F1      LDFF00  ($F1),A         
5A90: 11 30 C0   LD      DE,$C030        
5A93: F0 EC      LD      A,($EC)         
5A95: 12         LD      (DE),A          
5A96: 13         INC     DE              
5A97: F0 EE      LD      A,($EE)         
5A99: 12         LD      (DE),A          
5A9A: 13         INC     DE              
5A9B: F0 F1      LD      A,($F1)         
5A9D: 4F         LD      C,A             
5A9E: 06 00      LD      B,$00           
5AA0: CB 21      SET     1,E             
5AA2: CB 10      SET     1,E             
5AA4: CB 21      SET     1,E             
5AA6: CB 10      SET     1,E             
5AA8: 21 DB 59   LD      HL,$59DB        
5AAB: 09         ADD     HL,BC           
5AAC: 2A         LD      A,(HLI)         
5AAD: 12         LD      (DE),A          
5AAE: 13         INC     DE              
5AAF: 2A         LD      A,(HLI)         
5AB0: 12         LD      (DE),A          
5AB1: 13         INC     DE              
5AB2: F0 EC      LD      A,($EC)         
5AB4: 12         LD      (DE),A          
5AB5: 13         INC     DE              
5AB6: F0 EE      LD      A,($EE)         
5AB8: C6 08      ADD     $08             
5ABA: 12         LD      (DE),A          
5ABB: 13         INC     DE              
5ABC: 2A         LD      A,(HLI)         
5ABD: 12         LD      (DE),A          
5ABE: 13         INC     DE              
5ABF: 7E         LD      A,(HL)          
5AC0: 12         LD      (DE),A          
5AC1: C9         RET                     
5AC2: 98         SBC     B               
5AC3: CB 06      SET     1,E             
5AC5: 7E         LD      A,(HL)          
5AC6: 7E         LD      A,(HL)          
5AC7: 7E         LD      A,(HL)          
5AC8: 7E         LD      A,(HL)          
5AC9: 7E         LD      A,(HL)          
5ACA: 7E         LD      A,(HL)          
5ACB: 7E         LD      A,(HL)          
5ACC: 98         SBC     B               
5ACD: EB                              
5ACE: 06 7E      LD      B,$7E           
5AD0: 7E         LD      A,(HL)          
5AD1: 7E         LD      A,(HL)          
5AD2: 7E         LD      A,(HL)          
5AD3: 7E         LD      A,(HL)          
5AD4: 7E         LD      A,(HL)          
5AD5: 7E         LD      A,(HL)          
5AD6: 00         NOP                     
5AD7: 99         SBC     C               
5AD8: 2B         DEC     HL              
5AD9: 06 7E      LD      B,$7E           
5ADB: 7E         LD      A,(HL)          
5ADC: 7E         LD      A,(HL)          
5ADD: 7E         LD      A,(HL)          
5ADE: 7E         LD      A,(HL)          
5ADF: 7E         LD      A,(HL)          
5AE0: 7E         LD      A,(HL)          
5AE1: 99         SBC     C               
5AE2: 4B         LD      C,E             
5AE3: 06 7E      LD      B,$7E           
5AE5: 7E         LD      A,(HL)          
5AE6: 7E         LD      A,(HL)          
5AE7: 7E         LD      A,(HL)          
5AE8: 7E         LD      A,(HL)          
5AE9: 7E         LD      A,(HL)          
5AEA: 7E         LD      A,(HL)          
5AEB: 00         NOP                     
5AEC: 99         SBC     C               
5AED: 8B         ADC     A,E             
5AEE: 06 7E      LD      B,$7E           
5AF0: 7E         LD      A,(HL)          
5AF1: 7E         LD      A,(HL)          
5AF2: 7E         LD      A,(HL)          
5AF3: 7E         LD      A,(HL)          
5AF4: 7E         LD      A,(HL)          
5AF5: 7E         LD      A,(HL)          
5AF6: 99         SBC     C               
5AF7: AB         XOR     E               
5AF8: 06 7E      LD      B,$7E           
5AFA: 7E         LD      A,(HL)          
5AFB: 7E         LD      A,(HL)          
5AFC: 7E         LD      A,(HL)          
5AFD: 7E         LD      A,(HL)          
5AFE: 7E         LD      A,(HL)          
5AFF: 7E         LD      A,(HL)          
5B00: 00         NOP                     
5B01: FA 00 D6   LD      A,($D600)       
5B04: 5F         LD      E,A             
5B05: 16 00      LD      D,$00           
5B07: C6 14      ADD     $14             
5B09: EA 00 D6   LD      ($D600),A       
5B0C: 21 01 D6   LD      HL,$D601        
5B0F: 19         ADD     HL,DE           
5B10: D5         PUSH    DE              
5B11: 01 C2 5A   LD      BC,$5AC2        
5B14: F0 DB      LD      A,($DB)         
5B16: A7         AND     A               
5B17: 28 0A      JR      Z,$5B23         
5B19: 01 D7 5A   LD      BC,$5AD7        
5B1C: FE 01      CP      $01             
5B1E: 28 03      JR      Z,$5B23         
5B20: 01 EC 5A   LD      BC,$5AEC        
5B23: 1E 15      LD      E,$15           
5B25: 0A         LD      A,(BC)          
5B26: 03         INC     BC              
5B27: 22         LD      (HLI),A         
5B28: 1D         DEC     E               
5B29: 20 FA      JR      NZ,$5B25        
5B2B: D1         POP     DE              
5B2C: 21 04 D6   LD      HL,$D604        
5B2F: 19         ADD     HL,DE           
5B30: 0E 00      LD      C,$00           
5B32: F0 D9      LD      A,($D9)         
5B34: A7         AND     A               
5B35: 28 22      JR      Z,$5B59         
5B37: E0 D7      LDFF00  ($D7),A         
5B39: F0 D7      LD      A,($D7)         
5B3B: D6 08      SUB     $08             
5B3D: E0 D7      LDFF00  ($D7),A         
5B3F: 38 0F      JR      C,$5B50         
5B41: 3E AE      LD      A,$AE           
5B43: 22         LD      (HLI),A         
5B44: 0C         INC     C               
5B45: 79         LD      A,C             
5B46: FE 07      CP      $07             
5B48: 20 04      JR      NZ,$5B4E        
5B4A: 7D         LD      A,L             
5B4B: C6 03      ADD     $03             
5B4D: 6F         LD      L,A             
5B4E: 18 E9      JR      $5B39           
5B50: C6 08      ADD     $08             
5B52: 28 05      JR      Z,$5B59         
5B54: 3E AE      LD      A,$AE           
5B56: 22         LD      (HLI),A         
5B57: 18 08      JR      $5B61           
5B59: F0 DA      LD      A,($DA)         
5B5B: B9         CP      C               
5B5C: 28 0F      JR      Z,$5B6D         
5B5E: 3E AE      LD      A,$AE           
5B60: 22         LD      (HLI),A         
5B61: 0C         INC     C               
5B62: 79         LD      A,C             
5B63: FE 07      CP      $07             
5B65: 20 04      JR      NZ,$5B6B        
5B67: 7D         LD      A,L             
5B68: C6 03      ADD     $03             
5B6A: 6F         LD      L,A             
5B6B: 18 EC      JR      $5B59           
5B6D: C9         RET                     
5B6E: AF         XOR     A               
5B6F: 11 A7 DB   LD      DE,$DBA7        
5B72: 12         LD      (DE),A          
5B73: 06 01      LD      B,$01           
5B75: 0E 00      LD      C,$00           
5B77: 21 80 DB   LD      HL,$DB80        
5B7A: 2A         LD      A,(HLI)         
5B7B: A7         AND     A               
5B7C: 28 03      JR      Z,$5B81         
5B7E: 1A         LD      A,(DE)          
5B7F: B0         OR      B               
5B80: 12         LD      (DE),A          
5B81: 0C         INC     C               
5B82: 79         LD      A,C             
5B83: FE 05      CP      $05             
5B85: 20 02      JR      NZ,$5B89        
5B87: 06 02      LD      B,$02           
5B89: FE 0A      CP      $0A             
5B8B: 20 02      JR      NZ,$5B8F        
5B8D: 06 04      LD      B,$04           
5B8F: FE 0F      CP      $0F             
5B91: 20 E7      JR      NZ,$5B7A        
5B93: C9         RET                     
5B94: FA 5A DB   LD      A,($DB5A)       
5B97: A7         AND     A               
5B98: 20 0E      JR      NZ,$5BA8        
5B9A: FA 5B DB   LD      A,($DB5B)       
5B9D: 5F         LD      E,A             
5B9E: 16 00      LD      D,$00           
5BA0: 21 1B 51   LD      HL,$511B        
5BA3: 19         ADD     HL,DE           
5BA4: 7E         LD      A,(HL)          
5BA5: EA 5A DB   LD      ($DB5A),A       
5BA8: CD E2 27   CALL    $27E2           
5BAB: FA A6 DB   LD      A,($DBA6)       
5BAE: CB 27      SET     1,E             
5BB0: 5F         LD      E,A             
5BB1: 16 00      LD      D,$00           
5BB3: 21 3C 49   LD      HL,$493C        
5BB6: 19         ADD     HL,DE           
5BB7: 2A         LD      A,(HLI)         
5BB8: 66         LD      H,(HL)          
5BB9: 6F         LD      L,A             
5BBA: 01 00 D8   LD      BC,$D800        
5BBD: 11 80 03   LD      DE,$0380        
5BC0: CD B5 27   CALL    $27B5           
5BC3: 0A         LD      A,(BC)          
5BC4: 03         INC     BC              
5BC5: CD B5 27   CALL    $27B5           
5BC8: 22         LD      (HLI),A         
5BC9: 1B         DEC     DE              
5BCA: 7B         LD      A,E             
5BCB: B2         OR      D               
5BCC: 20 F2      JR      NZ,$5BC0        
5BCE: C9         RET                     
5BCF: C5         PUSH    BC              
5BD0: FA A5 DB   LD      A,($DBA5)       
5BD3: A7         AND     A               
5BD4: 28 1E      JR      Z,$5BF4         
5BD6: F0 F7      LD      A,($F7)         
5BD8: FE 0A      CP      $0A             
5BDA: 30 18      JR      NC,$5BF4        
5BDC: 5F         LD      E,A             
5BDD: CB 27      SET     1,E             
5BDF: CB 27      SET     1,E             
5BE1: 83         ADD     A,E             
5BE2: 5F         LD      E,A             
5BE3: 16 00      LD      D,$00           
5BE5: 21 16 DB   LD      HL,$DB16        
5BE8: 19         ADD     HL,DE           
5BE9: 11 CC DB   LD      DE,$DBCC        
5BEC: 0E 05      LD      C,$05           
5BEE: 1A         LD      A,(DE)          
5BEF: 13         INC     DE              
5BF0: 22         LD      (HLI),A         
5BF1: 0D         DEC     C               
5BF2: 20 FA      JR      NZ,$5BEE        
5BF4: C1         POP     BC              
5BF5: C9         RET                     
5BF6: A0         AND     B               
5BF7: 60         LD      H,B             
5BF8: 00         NOP                     
5BF9: 00         NOP                     
5BFA: 00         NOP                     
5BFB: 00         NOP                     
5BFC: FF         RST     0X38            
5BFD: 00         NOP                     
5BFE: 00         NOP                     
5BFF: 00         NOP                     
5C00: 00         NOP                     
5C01: 00         NOP                     
5C02: 80         ADD     A,B             
5C03: 80         ADD     A,B             
5C04: 00         NOP                     
5C05: 00         NOP                     
5C06: 00         NOP                     
5C07: FF         RST     0X38            
5C08: 00         NOP                     
5C09: 00         NOP                     
5C0A: 21 60 C4   LD      HL,$C460        
5C0D: 19         ADD     HL,DE           
5C0E: F0 E4      LD      A,($E4)         
5C10: 77         LD      (HL),A          
5C11: 3C         INC     A               
5C12: E0 E4      LDFF00  ($E4),A         
5C14: C5         PUSH    BC              
5C15: FA 25 C1   LD      A,($C125)       
5C18: 4F         LD      C,A             
5C19: 06 00      LD      B,$00           
5C1B: 21 F6 5B   LD      HL,$5BF6        
5C1E: 09         ADD     HL,BC           
5C1F: 7E         LD      A,(HL)          
5C20: E0 D7      LDFF00  ($D7),A         
5C22: 21 FB 5B   LD      HL,$5BFB        
5C25: 09         ADD     HL,BC           
5C26: 7E         LD      A,(HL)          
5C27: E0 D8      LDFF00  ($D8),A         
5C29: 21 00 5C   LD      HL,$5C00        
5C2C: 09         ADD     HL,BC           
5C2D: 7E         LD      A,(HL)          
5C2E: E0 D9      LDFF00  ($D9),A         
5C30: 21 05 5C   LD      HL,$5C05        
5C33: 09         ADD     HL,BC           
5C34: 7E         LD      A,(HL)          
5C35: E0 DA      LDFF00  ($DA),A         
5C37: 21 00 C2   LD      HL,$C200        
5C3A: 19         ADD     HL,DE           
5C3B: F0 D7      LD      A,($D7)         
5C3D: 86         ADD     A,(HL)          
5C3E: 77         LD      (HL),A          
5C3F: CB 19      SET     1,E             
5C41: 21 20 C2   LD      HL,$C220        
5C44: 19         ADD     HL,DE           
5C45: F0 D8      LD      A,($D8)         
5C47: CB 11      SET     1,E             
5C49: 8E         ADC     A,(HL)          
5C4A: 77         LD      (HL),A          
5C4B: 21 10 C2   LD      HL,$C210        
5C4E: 19         ADD     HL,DE           
5C4F: F0 D9      LD      A,($D9)         
5C51: 86         ADD     A,(HL)          
5C52: 77         LD      (HL),A          
5C53: CB 19      SET     1,E             
5C55: 21 30 C2   LD      HL,$C230        
5C58: 19         ADD     HL,DE           
5C59: F0 DA      LD      A,($DA)         
5C5B: CB 11      SET     1,E             
5C5D: 8E         ADC     A,(HL)          
5C5E: 77         LD      (HL),A          
5C5F: C1         POP     BC              
5C60: C9         RET                     
5C61: 0E 06      LD      C,$06           
5C63: F0 F6      LD      A,($F6)         
5C65: 21 81 CE   LD      HL,$CE81        
5C68: BE         CP      (HL)            
5C69: 28 21      JR      Z,$5C8C         
5C6B: 23         INC     HL              
5C6C: 0D         DEC     C               
5C6D: 20 F9      JR      NZ,$5C68        
5C6F: FA 80 CE   LD      A,($CE80)       
5C72: 3C         INC     A               
5C73: FE 06      CP      $06             
5C75: 20 01      JR      NZ,$5C78        
5C77: AF         XOR     A               
5C78: EA 80 CE   LD      ($CE80),A       
5C7B: 5F         LD      E,A             
5C7C: 16 00      LD      D,$00           
5C7E: 21 81 CE   LD      HL,$CE81        
5C81: 19         ADD     HL,DE           
5C82: 5E         LD      E,(HL)          
5C83: F0 F6      LD      A,($F6)         
5C85: 77         LD      (HL),A          
5C86: 21 00 CF   LD      HL,$CF00        
5C89: 19         ADD     HL,DE           
5C8A: 36 00      LD      (HL),$00        
5C8C: C9         RET                     
5C8D: FF         RST     0X38            
5C8E: FF         RST     0X38            
5C8F: FF         RST     0X38            
5C90: FF         RST     0X38            
5C91: FF         RST     0X38            
5C92: FF         RST     0X38            
5C93: FF         RST     0X38            
5C94: FF         RST     0X38            
5C95: FF         RST     0X38            
5C96: FF         RST     0X38            
5C97: FF         RST     0X38            
5C98: FF         RST     0X38            
5C99: FF         RST     0X38            
5C9A: FF         RST     0X38            
5C9B: FF         RST     0X38            
5C9C: FF         RST     0X38            
5C9D: FF         RST     0X38            
5C9E: FF         RST     0X38            
5C9F: FF         RST     0X38            
5CA0: FF         RST     0X38            
5CA1: FF         RST     0X38            
5CA2: FF         RST     0X38            
5CA3: FF         RST     0X38            
5CA4: FF         RST     0X38            
5CA5: FF         RST     0X38            
5CA6: FF         RST     0X38            
5CA7: FF         RST     0X38            
5CA8: FF         RST     0X38            
5CA9: FF         RST     0X38            
5CAA: FF         RST     0X38            
5CAB: FF         RST     0X38            
5CAC: FF         RST     0X38            
5CAD: FF         RST     0X38            
5CAE: FF         RST     0X38            
5CAF: FF         RST     0X38            
5CB0: FF         RST     0X38            
5CB1: FF         RST     0X38            
5CB2: FF         RST     0X38            
5CB3: FF         RST     0X38            
5CB4: FF         RST     0X38            
5CB5: FF         RST     0X38            
5CB6: FF         RST     0X38            
5CB7: FF         RST     0X38            
5CB8: FF         RST     0X38            
5CB9: FF         RST     0X38            
5CBA: FF         RST     0X38            
5CBB: FF         RST     0X38            
5CBC: FF         RST     0X38            
5CBD: FF         RST     0X38            
5CBE: FF         RST     0X38            
5CBF: FF         RST     0X38            
5CC0: FF         RST     0X38            
5CC1: FF         RST     0X38            
5CC2: FF         RST     0X38            
5CC3: FF         RST     0X38            
5CC4: FF         RST     0X38            
5CC5: FF         RST     0X38            
5CC6: FF         RST     0X38            
5CC7: FF         RST     0X38            
5CC8: FF         RST     0X38            
5CC9: FF         RST     0X38            
5CCA: FF         RST     0X38            
5CCB: FF         RST     0X38            
5CCC: FF         RST     0X38            
5CCD: FF         RST     0X38            
5CCE: FF         RST     0X38            
5CCF: FF         RST     0X38            
5CD0: FF         RST     0X38            
5CD1: FF         RST     0X38            
5CD2: FF         RST     0X38            
5CD3: FF         RST     0X38            
5CD4: FF         RST     0X38            
5CD5: FF         RST     0X38            
5CD6: FF         RST     0X38            
5CD7: FF         RST     0X38            
5CD8: FF         RST     0X38            
5CD9: FF         RST     0X38            
5CDA: FF         RST     0X38            
5CDB: FF         RST     0X38            
5CDC: FF         RST     0X38            
5CDD: FF         RST     0X38            
5CDE: FF         RST     0X38            
5CDF: FF         RST     0X38            
5CE0: FF         RST     0X38            
5CE1: FF         RST     0X38            
5CE2: FF         RST     0X38            
5CE3: FF         RST     0X38            
5CE4: FF         RST     0X38            
5CE5: FF         RST     0X38            
5CE6: FF         RST     0X38            
5CE7: FF         RST     0X38            
5CE8: FF         RST     0X38            
5CE9: FF         RST     0X38            
5CEA: FF         RST     0X38            
5CEB: FF         RST     0X38            
5CEC: FF         RST     0X38            
5CED: FF         RST     0X38            
5CEE: FF         RST     0X38            
5CEF: FF         RST     0X38            
5CF0: 21 00 00   LD      HL,$0000        
5CF3: 36 FF      LD      (HL),$FF        
5CF5: 06 28      LD      B,$28           
5CF7: AF         XOR     A               
5CF8: 21 00 C0   LD      HL,$C000        
5CFB: 22         LD      (HLI),A         
5CFC: 23         INC     HL              
5CFD: 23         INC     HL              
5CFE: 23         INC     HL              
5CFF: 05         DEC     B               
5D00: 20 F9      JR      NZ,$5CFB        
5D02: C9         RET                     
5D03: FA 4F C1   LD      A,($C14F)       
5D06: A7         AND     A               
5D07: 28 19      JR      Z,$5D22         
5D09: 21 00 C0   LD      HL,$C000        
5D0C: FA 9A DB   LD      A,($DB9A)       
5D0F: C6 08      ADD     $08             
5D11: 57         LD      D,A             
5D12: 1E 28      LD      E,$28           
5D14: 7E         LD      A,(HL)          
5D15: BA         CP      D               
5D16: 38 02      JR      C,$5D1A         
5D18: 36 00      LD      (HL),$00        
5D1A: 23         INC     HL              
5D1B: 23         INC     HL              
5D1C: 23         INC     HL              
5D1D: 23         INC     HL              
5D1E: 1D         DEC     E               
5D1F: 20 F3      JR      NZ,$5D14        
5D21: C9         RET                     
5D22: FA 9A DB   LD      A,($DB9A)       
5D25: A7         AND     A               
5D26: C8         RET     Z               
5D27: FA 9F C1   LD      A,($C19F)       
5D2A: A7         AND     A               
5D2B: C8         RET     Z               
5D2C: 16 3E      LD      D,$3E           
5D2E: FA 9F C1   LD      A,($C19F)       
5D31: E6 80      AND     $80             
5D33: 28 02      JR      Z,$5D37         
5D35: 16 58      LD      D,$58           
5D37: 1E 1F      LD      E,$1F           
5D39: 21 24 C0   LD      HL,$C024        
5D3C: 7E         LD      A,(HL)          
5D3D: BA         CP      D               
5D3E: FA 9F C1   LD      A,($C19F)       
5D41: CB 7F      SET     1,E             
5D43: 20 01      JR      NZ,$5D46        
5D45: 3F         CCF                     
5D46: 38 1B      JR      C,$5D63         
5D48: FA 73 C1   LD      A,($C173)       
5D4B: FE 4F      CP      $4F             
5D4D: 20 12      JR      NZ,$5D61        
5D4F: FA 12 C1   LD      A,($C112)       
5D52: A7         AND     A               
5D53: 20 0C      JR      NZ,$5D61        
5D55: 23         INC     HL              
5D56: 23         INC     HL              
5D57: 3A         LD      A,(HLD)         
5D58: 2B         DEC     HL              
5D59: FE 9A      CP      $9A             
5D5B: 38 04      JR      C,$5D61         
5D5D: FE A0      CP      $A0             
5D5F: 38 02      JR      C,$5D63         
5D61: 36 00      LD      (HL),$00        
5D63: 23         INC     HL              
5D64: 23         INC     HL              
5D65: 23         INC     HL              
5D66: 23         INC     HL              
5D67: 1D         DEC     E               
5D68: 20 D2      JR      NZ,$5D3C        
5D6A: C9         RET                     
5D6B: FA A5 DB   LD      A,($DBA5)       
5D6E: A7         AND     A               
5D6F: 28 1A      JR      Z,$5D8B         
5D71: F0 F9      LD      A,($F9)         
5D73: A7         AND     A               
5D74: C0         RET     NZ              
5D75: F0 F7      LD      A,($F7)         
5D77: FE 16      CP      $16             
5D79: C8         RET     Z               
5D7A: FE 14      CP      $14             
5D7C: C8         RET     Z               
5D7D: FE 13      CP      $13             
5D7F: C8         RET     Z               
5D80: FE 0A      CP      $0A             
5D82: D8         RET     C               
5D83: F0 F6      LD      A,($F6)         
5D85: FE FD      CP      $FD             
5D87: C8         RET     Z               
5D88: FE B1      CP      $B1             
5D8A: C8         RET     Z               
5D8B: FA 7B DB   LD      A,($DB7B)       
5D8E: FE 01      CP      $01             
5D90: 20 3A      JR      NZ,$5DCC        
5D92: 1E 0F      LD      E,$0F           
5D94: 16 00      LD      D,$00           
5D96: 21 A0 C3   LD      HL,$C3A0        
5D99: 19         ADD     HL,DE           
5D9A: 7E         LD      A,(HL)          
5D9B: FE D5      CP      $D5             
5D9D: 20 09      JR      NZ,$5DA8        
5D9F: 21 80 C2   LD      HL,$C280        
5DA2: 19         ADD     HL,DE           
5DA3: 7E         LD      A,(HL)          
5DA4: A7         AND     A               
5DA5: 28 01      JR      Z,$5DA8         
5DA7: 72         LD      (HL),D          
5DA8: 1D         DEC     E               
5DA9: 7B         LD      A,E             
5DAA: FE FF      CP      $FF             
5DAC: 20 E8      JR      NZ,$5D96        
5DAE: 3E D5      LD      A,$D5           
5DB0: CD 01 3C   CALL    $3C01           
5DB3: F0 98      LD      A,($98)         
5DB5: 21 00 C2   LD      HL,$C200        
5DB8: 19         ADD     HL,DE           
5DB9: 77         LD      (HL),A          
5DBA: F0 A2      LD      A,($A2)         
5DBC: 21 10 C3   LD      HL,$C310        
5DBF: 19         ADD     HL,DE           
5DC0: 77         LD      (HL),A          
5DC1: F0 99      LD      A,($99)         
5DC3: 21 3B C1   LD      HL,$C13B        
5DC6: 86         ADD     A,(HL)          
5DC7: 21 10 C2   LD      HL,$C210        
5DCA: 19         ADD     HL,DE           
5DCB: 77         LD      (HL),A          
5DCC: FA 79 DB   LD      A,($DB79)       
5DCF: FE 01      CP      $01             
5DD1: 28 28      JR      Z,$5DFB         
5DD3: FE 02      CP      $02             
5DD5: 20 60      JR      NZ,$5E37        
5DD7: FA A5 DB   LD      A,($DBA5)       
5DDA: A7         AND     A               
5DDB: 20 5A      JR      NZ,$5E37        
5DDD: F0 F6      LD      A,($F6)         
5DDF: FE 40      CP      $40             
5DE1: 38 54      JR      C,$5E37         
5DE3: FA 68 DB   LD      A,($DB68)       
5DE6: E6 02      AND     $02             
5DE8: 28 4D      JR      Z,$5E37         
5DEA: FA 43 DB   LD      A,($DB43)       
5DED: FE 02      CP      $02             
5DEF: 38 03      JR      C,$5DF4         
5DF1: AF         XOR     A               
5DF2: 18 02      JR      $5DF6           
5DF4: 3E 01      LD      A,$01           
5DF6: EA 79 DB   LD      ($DB79),A       
5DF9: 18 3C      JR      $5E37           
5DFB: 1E 0F      LD      E,$0F           
5DFD: 16 00      LD      D,$00           
5DFF: 21 A0 C3   LD      HL,$C3A0        
5E02: 19         ADD     HL,DE           
5E03: 7E         LD      A,(HL)          
5E04: FE D4      CP      $D4             
5E06: 20 09      JR      NZ,$5E11        
5E08: 21 80 C2   LD      HL,$C280        
5E0B: 19         ADD     HL,DE           
5E0C: 7E         LD      A,(HL)          
5E0D: A7         AND     A               
5E0E: 28 01      JR      Z,$5E11         
5E10: 72         LD      (HL),D          
5E11: 1D         DEC     E               
5E12: 7B         LD      A,E             
5E13: FE FF      CP      $FF             
5E15: 20 E8      JR      NZ,$5DFF        
5E17: 3E D4      LD      A,$D4           
5E19: CD 01 3C   CALL    $3C01           
5E1C: F0 98      LD      A,($98)         
5E1E: 21 00 C2   LD      HL,$C200        
5E21: 19         ADD     HL,DE           
5E22: 77         LD      (HL),A          
5E23: F0 99      LD      A,($99)         
5E25: 21 3B C1   LD      HL,$C13B        
5E28: 86         ADD     A,(HL)          
5E29: 21 10 C2   LD      HL,$C210        
5E2C: 19         ADD     HL,DE           
5E2D: 77         LD      (HL),A          
5E2E: 21 B0 C2   LD      HL,$C2B0        
5E31: 19         ADD     HL,DE           
5E32: 34         INC     (HL)            
5E33: 3E 2D      LD      A,$2D           
5E35: E0 F2      LDFF00  ($F2),A         
5E37: FA 73 DB   LD      A,($DB73)       
5E3A: A7         AND     A               
5E3B: CA D7 5E   JP      Z,$5ED7         
5E3E: 1E 0F      LD      E,$0F           
5E40: 16 00      LD      D,$00           
5E42: 21 A0 C3   LD      HL,$C3A0        
5E45: 19         ADD     HL,DE           
5E46: 7E         LD      A,(HL)          
5E47: FE C1      CP      $C1             
5E49: 20 09      JR      NZ,$5E54        
5E4B: 21 80 C2   LD      HL,$C280        
5E4E: 19         ADD     HL,DE           
5E4F: 7E         LD      A,(HL)          
5E50: A7         AND     A               
5E51: 28 01      JR      Z,$5E54         
5E53: 72         LD      (HL),D          
5E54: 1D         DEC     E               
5E55: 7B         LD      A,E             
5E56: FE FF      CP      $FF             
5E58: 20 E8      JR      NZ,$5E42        
5E5A: 3E C1      LD      A,$C1           
5E5C: CD 01 3C   CALL    $3C01           
5E5F: F0 98      LD      A,($98)         
5E61: 21 00 C2   LD      HL,$C200        
5E64: 19         ADD     HL,DE           
5E65: 77         LD      (HL),A          
5E66: 21 55 D1   LD      HL,$D155        
5E69: CD D0 5E   CALL    $5ED0           
5E6C: F0 99      LD      A,($99)         
5E6E: 21 3B C1   LD      HL,$C13B        
5E71: 86         ADD     A,(HL)          
5E72: 21 10 C2   LD      HL,$C210        
5E75: 19         ADD     HL,DE           
5E76: 77         LD      (HL),A          
5E77: 21 75 D1   LD      HL,$D175        
5E7A: CD D0 5E   CALL    $5ED0           
5E7D: F0 A2      LD      A,($A2)         
5E7F: 21 10 C3   LD      HL,$C310        
5E82: 19         ADD     HL,DE           
5E83: 77         LD      (HL),A          
5E84: 21 95 D1   LD      HL,$D195        
5E87: CD D0 5E   CALL    $5ED0           
5E8A: 21 40 C4   LD      HL,$C440        
5E8D: 19         ADD     HL,DE           
5E8E: 36 01      LD      (HL),$01        
5E90: 21 F0 C2   LD      HL,$C2F0        
5E93: 19         ADD     HL,DE           
5E94: 36 0C      LD      (HL),$0C        
5E96: F0 F6      LD      A,($F6)         
5E98: FE A4      CP      $A4             
5E9A: 20 13      JR      NZ,$5EAF        
5E9C: F0 F7      LD      A,($F7)         
5E9E: FE 11      CP      $11             
5EA0: 20 0D      JR      NZ,$5EAF        
5EA2: 3E 08      LD      A,$08           
5EA4: E0 F2      LDFF00  ($F2),A         
5EA6: EA 67 C1   LD      ($C167),A       
5EA9: 21 00 C3   LD      HL,$C300        
5EAC: 19         ADD     HL,DE           
5EAD: 36 79      LD      (HL),$79        
5EAF: F0 9E      LD      A,($9E)         
5EB1: 21 B5 D1   LD      HL,$D1B5        
5EB4: CD D0 5E   CALL    $5ED0           
5EB7: FA 10 DB   LD      A,($DB10)       
5EBA: A7         AND     A               
5EBB: 28 12      JR      Z,$5ECF         
5EBD: F0 98      LD      A,($98)         
5EBF: 21 00 C2   LD      HL,$C200        
5EC2: 19         ADD     HL,DE           
5EC3: C6 20      ADD     $20             
5EC5: 77         LD      (HL),A          
5EC6: F0 99      LD      A,($99)         
5EC8: 21 10 C2   LD      HL,$C210        
5ECB: 19         ADD     HL,DE           
5ECC: C6 10      ADD     $10             
5ECE: 77         LD      (HL),A          
5ECF: C9         RET                     
5ED0: 0E 10      LD      C,$10           
5ED2: 22         LD      (HLI),A         
5ED3: 0D         DEC     C               
5ED4: 20 FC      JR      NZ,$5ED2        
5ED6: C9         RET                     
5ED7: F0 F6      LD      A,($F6)         
5ED9: FE A7      CP      $A7             
5EDB: C8         RET     Z               
5EDC: FA 56 DB   LD      A,($DB56)       
5EDF: FE 01      CP      $01             
5EE1: 20 36      JR      NZ,$5F19        
5EE3: 1E 0F      LD      E,$0F           
5EE5: 16 00      LD      D,$00           
5EE7: 21 A0 C3   LD      HL,$C3A0        
5EEA: 19         ADD     HL,DE           
5EEB: 7E         LD      A,(HL)          
5EEC: FE 6D      CP      $6D             
5EEE: 20 09      JR      NZ,$5EF9        
5EF0: 21 80 C2   LD      HL,$C280        
5EF3: 19         ADD     HL,DE           
5EF4: 7E         LD      A,(HL)          
5EF5: A7         AND     A               
5EF6: 28 01      JR      Z,$5EF9         
5EF8: 72         LD      (HL),D          
5EF9: 1D         DEC     E               
5EFA: 7B         LD      A,E             
5EFB: FE FF      CP      $FF             
5EFD: 20 E8      JR      NZ,$5EE7        
5EFF: 3E 6D      LD      A,$6D           
5F01: CD 01 3C   CALL    $3C01           
5F04: F0 98      LD      A,($98)         
5F06: 21 00 C2   LD      HL,$C200        
5F09: 19         ADD     HL,DE           
5F0A: 77         LD      (HL),A          
5F0B: F0 99      LD      A,($99)         
5F0D: 21 10 C2   LD      HL,$C210        
5F10: 19         ADD     HL,DE           
5F11: 77         LD      (HL),A          
5F12: F0 A2      LD      A,($A2)         
5F14: 21 10 C3   LD      HL,$C310        
5F17: 19         ADD     HL,DE           
5F18: 77         LD      (HL),A          
5F19: C9         RET                     
5F1A: CD D2 27   CALL    $27D2           
5F1D: AF         XOR     A               
5F1E: EA 95 DB   LD      ($DB95),A       
5F21: EA 96 DB   LD      ($DB96),A       
5F24: EA 98 DB   LD      ($DB98),A       
5F27: EA 99 DB   LD      ($DB99),A       
5F2A: EA 97 DB   LD      ($DB97),A       
5F2D: E0 47      LDFF00  ($47),A         
5F2F: E0 48      LDFF00  ($48),A         
5F31: E0 49      LDFF00  ($49),A         
5F33: E0 97      LDFF00  ($97),A         
5F35: E0 96      LDFF00  ($96),A         
5F37: EA FB D6   LD      ($D6FB),A       
5F3A: EA F8 D6   LD      ($D6F8),A       
5F3D: 3E 18      LD      A,$18           
5F3F: E0 B5      LDFF00  ($B5),A         
5F41: C9         RET                     
5F42: 00         NOP                     
5F43: 57         LD      D,A             
5F44: 10 57      STOP    $57             
5F46: 20 57      JR      NZ,$5F9F        
5F48: 30 57      JR      NC,$5FA1        
5F4A: 40         LD      B,B             
5F4B: 57         LD      D,A             
5F4C: 50         LD      D,B             
5F4D: 57         LD      D,A             
5F4E: 60         LD      H,B             
5F4F: 57         LD      D,A             
5F50: 70         LD      (HL),B          
5F51: 57         LD      D,A             
5F52: 80         ADD     A,B             
5F53: 57         LD      D,A             
5F54: 90         SUB     B               
5F55: 57         LD      D,A             
5F56: 00         NOP                     
5F57: 58         LD      E,B             
5F58: 10 58      STOP    $58             
5F5A: 20 58      JR      NZ,$5FB4        
5F5C: 30 58      JR      NC,$5FB6        
5F5E: 40         LD      B,B             
5F5F: 58         LD      E,B             
5F60: 50         LD      D,B             
5F61: 58         LD      E,B             
5F62: FA 09 C1   LD      A,($C109)       
5F65: E6 0F      AND     $0F             
5F67: CB 27      SET     1,E             
5F69: 5F         LD      E,A             
5F6A: 16 00      LD      D,$00           
5F6C: 21 42 5F   LD      HL,$5F42        
5F6F: 19         ADD     HL,DE           
5F70: 2A         LD      A,(HLI)         
5F71: 66         LD      H,(HL)          
5F72: 6F         LD      L,A             
5F73: 11 D0 96   LD      DE,$96D0        
5F76: 01 10 00   LD      BC,$0010        
5F79: 3E 0F      LD      A,$0F           
5F7B: CD B9 28   CALL    $28B9           
5F7E: FA 09 C1   LD      A,($C109)       
5F81: CB 37      SET     1,E             
5F83: E6 0F      AND     $0F             
5F85: CB 27      SET     1,E             
5F87: 5F         LD      E,A             
5F88: 16 00      LD      D,$00           
5F8A: 21 42 5F   LD      HL,$5F42        
5F8D: 19         ADD     HL,DE           
5F8E: 2A         LD      A,(HLI)         
5F8F: 66         LD      H,(HL)          
5F90: 6F         LD      L,A             
5F91: 11 C0 96   LD      DE,$96C0        
5F94: 01 10 00   LD      BC,$0010        
5F97: 3E 0F      LD      A,$0F           
5F99: CD B9 28   CALL    $28B9           
5F9C: 3E 6C      LD      A,$6C           
5F9E: EA 09 99   LD      ($9909),A       
5FA1: 3C         INC     A               
5FA2: EA 0A 99   LD      ($990A),A       
5FA5: C9         RET                     
5FA6: FA 1C C1   LD      A,($C11C)       
5FA9: FE 00      CP      $00             
5FAB: 20 0D      JR      NZ,$5FBA        
5FAD: FA 7B C1   LD      A,($C17B)       
5FB0: A7         AND     A               
5FB1: 20 07      JR      NZ,$5FBA        
5FB3: F0 F7      LD      A,($F7)         
5FB5: C6 56      ADD     $56             
5FB7: CD 97 21   CALL    $2197           
5FBA: C9         RET                     
5FBB: FA 9F C1   LD      A,($C19F)       
5FBE: A7         AND     A               
5FBF: 20 0A      JR      NZ,$5FCB        
5FC1: FA C7 C3   LD      A,($C3C7)       
5FC4: A7         AND     A               
5FC5: 28 04      JR      Z,$5FCB         
5FC7: 3D         DEC     A               
5FC8: EA C7 C3   LD      ($C3C7),A       
5FCB: FA C4 C3   LD      A,($C3C4)       
5FCE: A7         AND     A               
5FCF: 28 04      JR      Z,$5FD5         
5FD1: 3D         DEC     A               
5FD2: EA C4 C3   LD      ($C3C4),A       
5FD5: FA 96 DB   LD      A,($DB96)       
5FD8: C7         RST     0X00            
5FD9: F5         PUSH    AF              
5FDA: 5F         LD      E,A             
5FDB: 17         RLA                     
5FDC: 60         LD      H,B             
5FDD: 23         INC     HL              
5FDE: 60         LD      H,B             
5FDF: 5A         LD      E,D             
5FE0: 61         LD      H,C             
5FE1: 8D         ADC     A,L             
5FE2: 61         LD      H,C             
5FE3: A8         XOR     B               
5FE4: 61         LD      H,C             
5FE5: C6 61      ADD     $61             
5FE7: DD                              
5FE8: 61         LD      H,C             
5FE9: EF         RST     0X28            
5FEA: 61         LD      H,C             
5FEB: 06 62      LD      B,$62           
5FED: 18 62      JR      $6051           
5FEF: 46         LD      B,(HL)          
5FF0: 62         LD      H,D             
5FF1: 5D         LD      E,L             
5FF2: 62         LD      H,D             
5FF3: FD                              
5FF4: 55         LD      D,L             
5FF5: 3E 01      LD      A,$01           
5FF7: EA 67 C1   LD      ($C167),A       
5FFA: CD 76 17   CALL    $1776           
5FFD: FA 6B C1   LD      A,($C16B)       
6000: FE 04      CP      $04             
6002: 20 12      JR      NZ,$6016        
6004: CD 45 44   CALL    $4445           
6007: AF         XOR     A               
6008: EA BF C1   LD      ($C1BF),A       
600B: CD 36 56   CALL    $5636           
600E: CD 75 62   CALL    $6275           
6011: 3E 0F      LD      A,$0F           
6013: EA FE D6   LD      ($D6FE),A       
6016: C9         RET                     
6017: 3E 13      LD      A,$13           
6019: EA FE D6   LD      ($D6FE),A       
601C: AF         XOR     A               
601D: EA 3F C1   LD      ($C13F),A       
6020: C3 45 44   JP      $4445           
6023: 3E 13      LD      A,$13           
6025: EA FF D6   LD      ($D6FF),A       
6028: 3E FF      LD      A,$FF           
602A: EA 9A DB   LD      ($DB9A),A       
602D: AF         XOR     A               
602E: E0 96      LDFF00  ($96),A         
6030: EA 6B C1   LD      ($C16B),A       
6033: EA 6C C1   LD      ($C16C),A       
6036: 3E 90      LD      A,$90           
6038: E0 97      LDFF00  ($97),A         
603A: 3E 40      LD      A,$40           
603C: EA 14 C1   LD      ($C114),A       
603F: 3E A0      LD      A,$A0           
6041: EA 66 D4   LD      ($D466),A       
6044: 3E E0      LD      A,$E0           
6046: EA 40 C5   LD      ($C540),A       
6049: 3E 00      LD      A,$00           
604B: EA 30 C5   LD      ($C530),A       
604E: 3E 01      LD      A,$01           
6050: EA 10 C5   LD      ($C510),A       
6053: 3E 0C      LD      A,$0C           
6055: EA 60 C5   LD      ($C560),A       
6058: 3E 08      LD      A,$08           
605A: EA 50 C5   LD      ($C550),A       
605D: 3E 00      LD      A,$00           
605F: EA 20 C5   LD      ($C520),A       
6062: EA 00 D2   LD      ($D200),A       
6065: 3E 20      LD      A,$20           
6067: EA 41 C5   LD      ($C541),A       
606A: 3E A0      LD      A,$A0           
606C: EA 31 C5   LD      ($C531),A       
606F: 3E 01      LD      A,$01           
6071: EA 11 C5   LD      ($C511),A       
6074: 3E 08      LD      A,$08           
6076: EA 61 C5   LD      ($C561),A       
6079: 3E F8      LD      A,$F8           
607B: EA 51 C5   LD      ($C551),A       
607E: 3E 40      LD      A,$40           
6080: EA 21 C5   LD      ($C521),A       
6083: 3E 24      LD      A,$24           
6085: EA 01 D2   LD      ($D201),A       
6088: 3E 48      LD      A,$48           
608A: EA 42 C5   LD      ($C542),A       
608D: 3E 30      LD      A,$30           
608F: EA 32 C5   LD      ($C532),A       
6092: 3E 02      LD      A,$02           
6094: EA 12 C5   LD      ($C512),A       
6097: 3E 00      LD      A,$00           
6099: EA 62 C5   LD      ($C562),A       
609C: 3E 00      LD      A,$00           
609E: EA 52 C5   LD      ($C552),A       
60A1: 3E 00      LD      A,$00           
60A3: EA 22 C5   LD      ($C522),A       
60A6: 3E 02      LD      A,$02           
60A8: EA 02 D2   LD      ($D202),A       
60AB: 3E 3C      LD      A,$3C           
60AD: EA 43 C5   LD      ($C543),A       
60B0: 3E 40      LD      A,$40           
60B2: EA 33 C5   LD      ($C533),A       
60B5: 3E 02      LD      A,$02           
60B7: EA 13 C5   LD      ($C513),A       
60BA: 3E 00      LD      A,$00           
60BC: EA 63 C5   LD      ($C563),A       
60BF: 3E 00      LD      A,$00           
60C1: EA 53 C5   LD      ($C553),A       
60C4: 3E 00      LD      A,$00           
60C6: EA 23 C5   LD      ($C523),A       
60C9: 3E 00      LD      A,$00           
60CB: EA 03 D2   LD      ($D203),A       
60CE: 3E 40      LD      A,$40           
60D0: EA 44 C5   LD      ($C544),A       
60D3: 3E 50      LD      A,$50           
60D5: EA 34 C5   LD      ($C534),A       
60D8: 3E 02      LD      A,$02           
60DA: EA 14 C5   LD      ($C514),A       
60DD: 3E 00      LD      A,$00           
60DF: EA 64 C5   LD      ($C564),A       
60E2: 3E 00      LD      A,$00           
60E4: EA 54 C5   LD      ($C554),A       
60E7: 3E 00      LD      A,$00           
60E9: EA 24 C5   LD      ($C524),A       
60EC: 3E 00      LD      A,$00           
60EE: EA 04 D2   LD      ($D204),A       
60F1: 3E 3C      LD      A,$3C           
60F3: EA 45 C5   LD      ($C545),A       
60F6: 3E 60      LD      A,$60           
60F8: EA 35 C5   LD      ($C535),A       
60FB: 3E 02      LD      A,$02           
60FD: EA 15 C5   LD      ($C515),A       
6100: 3E 00      LD      A,$00           
6102: EA 65 C5   LD      ($C565),A       
6105: 3E 00      LD      A,$00           
6107: EA 55 C5   LD      ($C555),A       
610A: 3E 00      LD      A,$00           
610C: EA 25 C5   LD      ($C525),A       
610F: 3E 00      LD      A,$00           
6111: EA 05 D2   LD      ($D205),A       
6114: 3E 44      LD      A,$44           
6116: EA 46 C5   LD      ($C546),A       
6119: 3E 68      LD      A,$68           
611B: EA 36 C5   LD      ($C536),A       
611E: 3E 02      LD      A,$02           
6120: EA 16 C5   LD      ($C516),A       
6123: 3E 00      LD      A,$00           
6125: EA 66 C5   LD      ($C566),A       
6128: 3E 00      LD      A,$00           
612A: EA 56 C5   LD      ($C556),A       
612D: 3E 00      LD      A,$00           
612F: EA 26 C5   LD      ($C526),A       
6132: 3E 00      LD      A,$00           
6134: EA 06 D2   LD      ($D206),A       
6137: C3 45 44   JP      $4445           
613A: 00         NOP                     
613B: 00         NOP                     
613C: 00         NOP                     
613D: 00         NOP                     
613E: 40         LD      B,B             
613F: 40         LD      B,B             
6140: 40         LD      B,B             
6141: 40         LD      B,B             
6142: 94         SUB     H               
6143: 94         SUB     H               
6144: 94         SUB     H               
6145: 94         SUB     H               
6146: E4                              
6147: E4                              
6148: E4                              
6149: E4                              
614A: 00         NOP                     
614B: 00         NOP                     
614C: 00         NOP                     
614D: 00         NOP                     
614E: 04         INC     B               
614F: 04         INC     B               
6150: 04         INC     B               
6151: 04         INC     B               
6152: 18 18      JR      $616C           
6154: 18 18      JR      $616E           
6156: 1C         INC     E               
6157: 1C         INC     E               
6158: 1C         INC     E               
6159: 1C         INC     E               
615A: F0 E7      LD      A,($E7)         
615C: E6 07      AND     $07             
615E: 20 0E      JR      NZ,$616E        
6160: FA C5 C3   LD      A,($C3C5)       
6163: 3C         INC     A               
6164: EA C5 C3   LD      ($C3C5),A       
6167: FE 0C      CP      $0C             
6169: 20 03      JR      NZ,$616E        
616B: CD 45 44   CALL    $4445           
616E: F0 E7      LD      A,($E7)         
6170: E6 03      AND     $03             
6172: 5F         LD      E,A             
6173: FA C5 C3   LD      A,($C3C5)       
6176: 83         ADD     A,E             
6177: 5F         LD      E,A             
6178: 16 00      LD      D,$00           
617A: 21 3A 61   LD      HL,$613A        
617D: 19         ADD     HL,DE           
617E: 7E         LD      A,(HL)          
617F: EA 97 DB   LD      ($DB97),A       
6182: EA 99 DB   LD      ($DB99),A       
6185: 21 4A 61   LD      HL,$614A        
6188: 19         ADD     HL,DE           
6189: 7E         LD      A,(HL)          
618A: EA 98 DB   LD      ($DB98),A       
618D: F0 E7      LD      A,($E7)         
618F: E6 03      AND     $03             
6191: 20 11      JR      NZ,$61A4        
6193: F0 97      LD      A,($97)         
6195: 3C         INC     A               
6196: E0 97      LDFF00  ($97),A         
6198: FE 00      CP      $00             
619A: 20 08      JR      NZ,$61A4        
619C: 3E 80      LD      A,$80           
619E: EA C7 C3   LD      ($C3C7),A       
61A1: CD 45 44   CALL    $4445           
61A4: CD 8C 62   CALL    $628C           
61A7: C9         RET                     
61A8: CD 8C 62   CALL    $628C           
61AB: FA 9F C1   LD      A,($C19F)       
61AE: A7         AND     A               
61AF: 20 0F      JR      NZ,$61C0        
61B1: FA C7 C3   LD      A,($C3C7)       
61B4: A7         AND     A               
61B5: 20 08      JR      NZ,$61BF        
61B7: 3E D8      LD      A,$D8           
61B9: CD 3C 65   CALL    $653C           
61BC: CD 45 44   CALL    $4445           
61BF: C9         RET                     
61C0: 3E 02      LD      A,$02           
61C2: EA C4 C3   LD      ($C3C4),A       
61C5: C9         RET                     
61C6: CD 8C 62   CALL    $628C           
61C9: FA 9F C1   LD      A,($C19F)       
61CC: A7         AND     A               
61CD: 20 0D      JR      NZ,$61DC        
61CF: 3E 80      LD      A,$80           
61D1: EA C4 C3   LD      ($C3C4),A       
61D4: 3E C0      LD      A,$C0           
61D6: EA C7 C3   LD      ($C3C7),A       
61D9: CD 45 44   CALL    $4445           
61DC: C9         RET                     
61DD: CD 8C 62   CALL    $628C           
61E0: FA C7 C3   LD      A,($C3C7)       
61E3: A7         AND     A               
61E4: 20 08      JR      NZ,$61EE        
61E6: 3E D9      LD      A,$D9           
61E8: CD 3C 65   CALL    $653C           
61EB: C3 45 44   JP      $4445           
61EE: C9         RET                     
61EF: CD 8C 62   CALL    $628C           
61F2: FA 9F C1   LD      A,($C19F)       
61F5: A7         AND     A               
61F6: 20 0D      JR      NZ,$6205        
61F8: 3E 80      LD      A,$80           
61FA: EA C4 C3   LD      ($C3C4),A       
61FD: 3E C0      LD      A,$C0           
61FF: EA C7 C3   LD      ($C3C7),A       
6202: CD 45 44   CALL    $4445           
6205: C9         RET                     
6206: CD 8C 62   CALL    $628C           
6209: FA C7 C3   LD      A,($C3C7)       
620C: A7         AND     A               
620D: 20 08      JR      NZ,$6217        
620F: 3E DA      LD      A,$DA           
6211: CD 3C 65   CALL    $653C           
6214: C3 45 44   JP      $4445           
6217: C9         RET                     
6218: CD 8C 62   CALL    $628C           
621B: FA 9F C1   LD      A,($C19F)       
621E: A7         AND     A               
621F: 20 1F      JR      NZ,$6240        
6221: FA 77 C1   LD      A,($C177)       
6224: A7         AND     A               
6225: 20 09      JR      NZ,$6230        
6227: 3E DB      LD      A,$DB           
6229: CD 3C 65   CALL    $653C           
622C: CD 45 44   CALL    $4445           
622F: C9         RET                     
6230: 3E DE      LD      A,$DE           
6232: CD 3C 65   CALL    $653C           
6235: 3E 05      LD      A,$05           
6237: EA 96 DB   LD      ($DB96),A       
623A: 3E 05      LD      A,$05           
623C: EA C7 C3   LD      ($C3C7),A       
623F: C9         RET                     
6240: 3E 02      LD      A,$02           
6242: EA C4 C3   LD      ($C3C4),A       
6245: C9         RET                     
6246: CD 8C 62   CALL    $628C           
6249: FA 9F C1   LD      A,($C19F)       
624C: A7         AND     A               
624D: 20 0D      JR      NZ,$625C        
624F: 3E DC      LD      A,$DC           
6251: CD 3C 65   CALL    $653C           
6254: 3E 30      LD      A,$30           
6256: EA C7 C3   LD      ($C3C7),A       
6259: CD 45 44   CALL    $4445           
625C: C9         RET                     
625D: CD 8C 62   CALL    $628C           
6260: 3E 02      LD      A,$02           
6262: EA C4 C3   LD      ($C3C4),A       
6265: FA C7 C3   LD      A,($C3C7)       
6268: A7         AND     A               
6269: C0         RET     NZ              
626A: CD D2 27   CALL    $27D2           
626D: CD 0F 66   CALL    $660F           
6270: 3E 01      LD      A,$01           
6272: EA 73 DB   LD      ($DB73),A       
6275: 1E 10      LD      E,$10           
6277: 21 10 C5   LD      HL,$C510        
627A: AF         XOR     A               
627B: 22         LD      (HLI),A         
627C: 1D         DEC     E               
627D: 20 FC      JR      NZ,$627B        
627F: C9         RET                     
6280: 40         LD      B,B             
6281: 00         NOP                     
6282: 40         LD      B,B             
6283: 20 46      JR      NZ,$62CB        
6285: 00         NOP                     
6286: 48         LD      C,B             
6287: 00         NOP                     
6288: 42         LD      B,D             
6289: 00         NOP                     
628A: 44         LD      B,H             
628B: 00         NOP                     
628C: CD 0C 63   CALL    $630C           
628F: FA 14 C1   LD      A,($C114)       
6292: 3C         INC     A               
6293: FE A0      CP      $A0             
6295: 20 05      JR      NZ,$629C        
6297: 3E 0F      LD      A,$0F           
6299: E0 F4      LDFF00  ($F4),A         
629B: AF         XOR     A               
629C: EA 14 C1   LD      ($C114),A       
629F: FA 66 D4   LD      A,($D466)       
62A2: A7         AND     A               
62A3: 20 0E      JR      NZ,$62B3        
62A5: 3E 21      LD      A,$21           
62A7: E0 F2      LDFF00  ($F2),A         
62A9: CD ED 27   CALL    $27ED           
62AC: E6 7F      AND     $7F             
62AE: C6 60      ADD     $60             
62B0: EA 66 D4   LD      ($D466),A       
62B3: 3D         DEC     A               
62B4: EA 66 D4   LD      ($D466),A       
62B7: F0 97      LD      A,($97)         
62B9: 3D         DEC     A               
62BA: FE C0      CP      $C0             
62BC: D8         RET     C               
62BD: 11 80 62   LD      DE,$6280        
62C0: FA C4 C3   LD      A,($C3C4)       
62C3: A7         AND     A               
62C4: 28 07      JR      Z,$62CD         
62C6: FE 60      CP      $60             
62C8: 30 03      JR      NC,$62CD        
62CA: 11 84 62   LD      DE,$6284        
62CD: 3E 7C      LD      A,$7C           
62CF: E0 EC      LDFF00  ($EC),A         
62D1: 3E 58      LD      A,$58           
62D3: E0 EE      LDFF00  ($EE),A         
62D5: 21 30 C0   LD      HL,$C030        
62D8: CD E9 62   CALL    $62E9           
62DB: 3E 48      LD      A,$48           
62DD: E0 EE      LDFF00  ($EE),A         
62DF: 11 88 62   LD      DE,$6288        
62E2: 21 38 C0   LD      HL,$C038        
62E5: CD E9 62   CALL    $62E9           
62E8: C9         RET                     
62E9: C5         PUSH    BC              
62EA: F0 97      LD      A,($97)         
62EC: 4F         LD      C,A             
62ED: F0 EC      LD      A,($EC)         
62EF: 91         SUB     C               
62F0: E0 E8      LDFF00  ($E8),A         
62F2: 22         LD      (HLI),A         
62F3: F0 EE      LD      A,($EE)         
62F5: 22         LD      (HLI),A         
62F6: 1A         LD      A,(DE)          
62F7: 13         INC     DE              
62F8: 22         LD      (HLI),A         
62F9: 1A         LD      A,(DE)          
62FA: 13         INC     DE              
62FB: 22         LD      (HLI),A         
62FC: F0 EC      LD      A,($EC)         
62FE: 91         SUB     C               
62FF: 22         LD      (HLI),A         
6300: F0 EE      LD      A,($EE)         
6302: C6 08      ADD     $08             
6304: 22         LD      (HLI),A         
6305: 1A         LD      A,(DE)          
6306: 13         INC     DE              
6307: 22         LD      (HLI),A         
6308: 1A         LD      A,(DE)          
6309: 77         LD      (HL),A          
630A: C1         POP     BC              
630B: C9         RET                     
630C: 0E 08      LD      C,$08           
630E: 06 00      LD      B,$00           
6310: 21 10 C5   LD      HL,$C510        
6313: 09         ADD     HL,BC           
6314: 7E         LD      A,(HL)          
6315: A7         AND     A               
6316: 28 1C      JR      Z,$6334         
6318: F5         PUSH    AF              
6319: 21 30 C5   LD      HL,$C530        
631C: 09         ADD     HL,BC           
631D: 7E         LD      A,(HL)          
631E: E0 EE      LDFF00  ($EE),A         
6320: 21 40 C5   LD      HL,$C540        
6323: 09         ADD     HL,BC           
6324: 7E         LD      A,(HL)          
6325: E0 EC      LDFF00  ($EC),A         
6327: 21 20 C5   LD      HL,$C520        
632A: 09         ADD     HL,BC           
632B: 7E         LD      A,(HL)          
632C: A7         AND     A               
632D: 28 01      JR      Z,$6330         
632F: 35         DEC     (HL)            
6330: F1         POP     AF              
6331: CD 3B 63   CALL    $633B           
6334: 0D         DEC     C               
6335: 79         LD      A,C             
6336: FE FF      CP      $FF             
6338: 20 D6      JR      NZ,$6310        
633A: C9         RET                     
633B: 3D         DEC     A               
633C: C7         RST     0X00            
633D: D1         POP     DE              
633E: 63         LD      H,E             
633F: 5B         LD      E,E             
6340: 64         LD      H,H             
6341: 4D         LD      C,L             
6342: 63         LD      H,E             
6343: 51         LD      D,C             
6344: 63         LD      H,E             
6345: 55         LD      D,L             
6346: 63         LD      H,E             
6347: 59         LD      E,C             
6348: 63         LD      H,E             
6349: 5D         LD      E,L             
634A: 63         LD      H,E             
634B: 61         LD      H,C             
634C: 63         LD      H,E             
634D: 50         LD      D,B             
634E: 00         NOP                     
634F: 50         LD      D,B             
6350: 20 52      JR      NZ,$63A4        
6352: 00         NOP                     
6353: 52         LD      D,D             
6354: 20 54      JR      NZ,$63AA        
6356: 00         NOP                     
6357: 54         LD      D,H             
6358: 20 56      JR      NZ,$63B0        
635A: 00         NOP                     
635B: 56         LD      D,(HL)          
635C: 20 58      JR      NZ,$63B6        
635E: 00         NOP                     
635F: 58         LD      E,B             
6360: 20 5A      JR      NZ,$63BC        
6362: 00         NOP                     
6363: 5A         LD      E,D             
6364: 20 03      JR      NZ,$6369        
6366: 03         INC     BC              
6367: 03         INC     BC              
6368: 03         INC     BC              
6369: 03         INC     BC              
636A: 03         INC     BC              
636B: 03         INC     BC              
636C: 03         INC     BC              
636D: 03         INC     BC              
636E: 03         INC     BC              
636F: 04         INC     B               
6370: 05         DEC     B               
6371: 00         NOP                     
6372: 01 02 03   LD      BC,$0302        
6375: 04         INC     B               
6376: 05         DEC     B               
6377: 00         NOP                     
6378: 01 02 03   LD      BC,$0302        
637B: 04         INC     B               
637C: 05         DEC     B               
637D: 00         NOP                     
637E: 01 02 03   LD      BC,$0302        
6381: 04         INC     B               
6382: 05         DEC     B               
6383: 00         NOP                     
6384: 01 02 03   LD      BC,$0302        
6387: 04         INC     B               
6388: 05         DEC     B               
6389: 00         NOP                     
638A: 01 02 03   LD      BC,$0302        
638D: 04         INC     B               
638E: 05         DEC     B               
638F: 00         NOP                     
6390: 01 02 03   LD      BC,$0302        
6393: 03         INC     BC              
6394: 03         INC     BC              
6395: 03         INC     BC              
6396: 03         INC     BC              
6397: 03         INC     BC              
6398: 03         INC     BC              
6399: 03         INC     BC              
639A: 03         INC     BC              
639B: 03         INC     BC              
639C: 03         INC     BC              
639D: 03         INC     BC              
639E: 03         INC     BC              
639F: 03         INC     BC              
63A0: 03         INC     BC              
63A1: 03         INC     BC              
63A2: 03         INC     BC              
63A3: 03         INC     BC              
63A4: 03         INC     BC              
63A5: 04         INC     B               
63A6: 05         DEC     B               
63A7: 00         NOP                     
63A8: 01 02 03   LD      BC,$0302        
63AB: 04         INC     B               
63AC: 05         DEC     B               
63AD: 00         NOP                     
63AE: 01 02 03   LD      BC,$0302        
63B1: 04         INC     B               
63B2: 05         DEC     B               
63B3: 00         NOP                     
63B4: 01 02 03   LD      BC,$0302        
63B7: 04         INC     B               
63B8: 05         DEC     B               
63B9: 00         NOP                     
63BA: 01 02 03   LD      BC,$0302        
63BD: 04         INC     B               
63BE: 05         DEC     B               
63BF: 00         NOP                     
63C0: 01 02 03   LD      BC,$0302        
63C3: 04         INC     B               
63C4: 05         DEC     B               
63C5: 00         NOP                     
63C6: 01 02 03   LD      BC,$0302        
63C9: 04         INC     B               
63CA: 05         DEC     B               
63CB: 00         NOP                     
63CC: 01 02 03   LD      BC,$0302        
63CF: 04         INC     B               
63D0: 05         DEC     B               
63D1: 21 20 C5   LD      HL,$C520        
63D4: 09         ADD     HL,BC           
63D5: 7E         LD      A,(HL)          
63D6: A7         AND     A               
63D7: C0         RET     NZ              
63D8: 21 10 D2   LD      HL,$D210        
63DB: 09         ADD     HL,BC           
63DC: 7E         LD      A,(HL)          
63DD: 3C         INC     A               
63DE: 77         LD      (HL),A          
63DF: FE 06      CP      $06             
63E1: 38 06      JR      C,$63E9         
63E3: 70         LD      (HL),B          
63E4: 21 00 D2   LD      HL,$D200        
63E7: 09         ADD     HL,BC           
63E8: 34         INC     (HL)            
63E9: 21 00 D2   LD      HL,$D200        
63EC: 09         ADD     HL,BC           
63ED: 5E         LD      E,(HL)          
63EE: 50         LD      D,B             
63EF: 21 65 63   LD      HL,$6365        
63F2: 19         ADD     HL,DE           
63F3: 5E         LD      E,(HL)          
63F4: CB 23      SET     1,E             
63F6: 50         LD      D,B             
63F7: 21 41 63   LD      HL,$6341        
63FA: 19         ADD     HL,DE           
63FB: 2A         LD      A,(HLI)         
63FC: 56         LD      D,(HL)          
63FD: 5F         LD      E,A             
63FE: D5         PUSH    DE              
63FF: 21 40 C0   LD      HL,$C040        
6402: 79         LD      A,C             
6403: 17         RLA                     
6404: 17         RLA                     
6405: 17         RLA                     
6406: E6 78      AND     $78             
6408: 5F         LD      E,A             
6409: 50         LD      D,B             
640A: 19         ADD     HL,DE           
640B: D1         POP     DE              
640C: CD E9 62   CALL    $62E9           
640F: CD 06 65   CALL    $6506           
6412: F0 E7      LD      A,($E7)         
6414: E6 07      AND     $07             
6416: 20 0A      JR      NZ,$6422        
6418: 21 60 C5   LD      HL,$C560        
641B: 09         ADD     HL,BC           
641C: 7E         LD      A,(HL)          
641D: FE FB      CP      $FB             
641F: 28 01      JR      Z,$6422         
6421: 35         DEC     (HL)            
6422: F0 E8      LD      A,($E8)         
6424: FE F0      CP      $F0             
6426: 38 0D      JR      C,$6435         
6428: 21 60 C5   LD      HL,$C560        
642B: 09         ADD     HL,BC           
642C: 7E         LD      A,(HL)          
642D: E6 80      AND     $80             
642F: C8         RET     Z               
6430: 21 10 C5   LD      HL,$C510        
6433: 09         ADD     HL,BC           
6434: 70         LD      (HL),B          
6435: C9         RET                     
6436: 3E 64      LD      A,$64           
6438: 42         LD      B,D             
6439: 64         LD      H,H             
643A: 46         LD      B,(HL)          
643B: 64         LD      H,H             
643C: 4A         LD      C,D             
643D: 64         LD      H,H             
643E: 4C         LD      C,H             
643F: 00         NOP                     
6440: 4C         LD      C,H             
6441: 20 4E      JR      NZ,$6491        
6443: 00         NOP                     
6444: 4E         LD      C,(HL)          
6445: 20 5C      JR      NZ,$64A3        
6447: 00         NOP                     
6448: 5C         LD      E,H             
6449: 20 5E      JR      NZ,$64A9        
644B: 00         NOP                     
644C: 5E         LD      E,(HL)          
644D: 20 01      JR      NZ,$6450        
644F: FF         RST     0X38            
6450: 01 FF FE   LD      BC,$FEFF        
6453: 02         LD      (BC),A          
6454: 01 FF 4C   LD      BC,$4CFF        
6457: 52         LD      D,D             
6458: 58         LD      E,B             
6459: 5C         LD      E,H             
645A: 60         LD      H,B             
645B: 21 60 C5   LD      HL,$C560        
645E: 09         ADD     HL,BC           
645F: 7E         LD      A,(HL)          
6460: 1E 03      LD      E,$03           
6462: E6 80      AND     $80             
6464: 28 10      JR      Z,$6476         
6466: 21 00 D2   LD      HL,$D200        
6469: 09         ADD     HL,BC           
646A: F0 E7      LD      A,($E7)         
646C: E6 07      AND     $07             
646E: 20 05      JR      NZ,$6475        
6470: 7E         LD      A,(HL)          
6471: 3C         INC     A               
6472: E6 03      AND     $03             
6474: 77         LD      (HL),A          
6475: 5E         LD      E,(HL)          
6476: CB 23      SET     1,E             
6478: 50         LD      D,B             
6479: 21 36 64   LD      HL,$6436        
647C: 19         ADD     HL,DE           
647D: 2A         LD      A,(HLI)         
647E: 56         LD      D,(HL)          
647F: 5F         LD      E,A             
6480: D5         PUSH    DE              
6481: 21 40 C0   LD      HL,$C040        
6484: 79         LD      A,C             
6485: 17         RLA                     
6486: 17         RLA                     
6487: 17         RLA                     
6488: E6 78      AND     $78             
648A: 5F         LD      E,A             
648B: 50         LD      D,B             
648C: 19         ADD     HL,DE           
648D: D1         POP     DE              
648E: CD E9 62   CALL    $62E9           
6491: CD 06 65   CALL    $6506           
6494: 79         LD      A,C             
6495: CB 27      SET     1,E             
6497: CB 27      SET     1,E             
6499: CB 27      SET     1,E             
649B: CB 27      SET     1,E             
649D: 5F         LD      E,A             
649E: F0 E7      LD      A,($E7)         
64A0: 83         ADD     A,E             
64A1: E0 E9      LDFF00  ($E9),A         
64A3: E6 3F      AND     $3F             
64A5: 20 11      JR      NZ,$64B8        
64A7: CD ED 27   CALL    $27ED           
64AA: E6 07      AND     $07             
64AC: 5F         LD      E,A             
64AD: 50         LD      D,B             
64AE: 21 4E 64   LD      HL,$644E        
64B1: 19         ADD     HL,DE           
64B2: 7E         LD      A,(HL)          
64B3: 21 50 C5   LD      HL,$C550        
64B6: 09         ADD     HL,BC           
64B7: 77         LD      (HL),A          
64B8: F0 E9      LD      A,($E9)         
64BA: C6 40      ADD     $40             
64BC: E6 3F      AND     $3F             
64BE: 20 11      JR      NZ,$64D1        
64C0: CD ED 27   CALL    $27ED           
64C3: E6 07      AND     $07             
64C5: 5F         LD      E,A             
64C6: 50         LD      D,B             
64C7: 21 4E 64   LD      HL,$644E        
64CA: 19         ADD     HL,DE           
64CB: 7E         LD      A,(HL)          
64CC: 21 60 C5   LD      HL,$C560        
64CF: 09         ADD     HL,BC           
64D0: 77         LD      (HL),A          
64D1: 21 90 C5   LD      HL,$C590        
64D4: 09         ADD     HL,BC           
64D5: 7E         LD      A,(HL)          
64D6: 3C         INC     A               
64D7: 77         LD      (HL),A          
64D8: FE 13      CP      $13             
64DA: 38 29      JR      C,$6505         
64DC: 70         LD      (HL),B          
64DD: 21 54 64   LD      HL,$6454        
64E0: 09         ADD     HL,BC           
64E1: 56         LD      D,(HL)          
64E2: 21 30 C5   LD      HL,$C530        
64E5: 09         ADD     HL,BC           
64E6: 7E         LD      A,(HL)          
64E7: 92         SUB     D               
64E8: 1E 01      LD      E,$01           
64EA: E6 80      AND     $80             
64EC: 20 02      JR      NZ,$64F0        
64EE: 1E FF      LD      E,$FF           
64F0: 7E         LD      A,(HL)          
64F1: 83         ADD     A,E             
64F2: 77         LD      (HL),A          
64F3: 21 40 C5   LD      HL,$C540        
64F6: 09         ADD     HL,BC           
64F7: 7E         LD      A,(HL)          
64F8: D6 48      SUB     $48             
64FA: 1E 01      LD      E,$01           
64FC: E6 80      AND     $80             
64FE: 20 02      JR      NZ,$6502        
6500: 1E FF      LD      E,$FF           
6502: 7E         LD      A,(HL)          
6503: 83         ADD     A,E             
6504: 77         LD      (HL),A          
6505: C9         RET                     
6506: CD 13 65   CALL    $6513           
6509: C5         PUSH    BC              
650A: 79         LD      A,C             
650B: C6 10      ADD     $10             
650D: 4F         LD      C,A             
650E: CD 13 65   CALL    $6513           
6511: C1         POP     BC              
6512: C9         RET                     
6513: 21 50 C5   LD      HL,$C550        
6516: 09         ADD     HL,BC           
6517: 7E         LD      A,(HL)          
6518: F5         PUSH    AF              
6519: CB 37      SET     1,E             
651B: E6 F0      AND     $F0             
651D: 21 70 C5   LD      HL,$C570        
6520: 09         ADD     HL,BC           
6521: 86         ADD     A,(HL)          
6522: 77         LD      (HL),A          
6523: CB 12      SET     1,E             
6525: 21 30 C5   LD      HL,$C530        
6528: 09         ADD     HL,BC           
6529: F1         POP     AF              
652A: 1E 00      LD      E,$00           
652C: CB 7F      SET     1,E             
652E: 28 02      JR      Z,$6532         
6530: 1E F0      LD      E,$F0           
6532: CB 37      SET     1,E             
6534: E6 0F      AND     $0F             
6536: B3         OR      E               
6537: CB 1A      SET     1,E             
6539: 8E         ADC     A,(HL)          
653A: 77         LD      (HL),A          
653B: C9         RET                     
653C: 5F         LD      E,A             
653D: F0 99      LD      A,($99)         
653F: F5         PUSH    AF              
6540: 3E 60      LD      A,$60           
6542: E0 99      LDFF00  ($99),A         
6544: 7B         LD      A,E             
6545: CD 85 21   CALL    $2185           
6548: F1         POP     AF              
6549: E0 99      LDFF00  ($99),A         
654B: C9         RET                     
654C: FA 96 DB   LD      A,($DB96)       
654F: C7         RST     0X00            
6550: 64         LD      H,H             
6551: 65         LD      H,L             
6552: 91         SUB     C               
6553: 65         LD      H,L             
6554: AE         XOR     (HL)            
6555: 65         LD      H,L             
6556: E0 65      LDFF00  ($65),A         
6558: F6 65      OR      $65             
655A: FD                              
655B: 55         LD      D,L             
655C: 1A         LD      A,(DE)          
655D: 66         LD      H,(HL)          
655E: 3E 66      LD      A,$66           
6560: 7B         LD      A,E             
6561: 66         LD      H,(HL)          
6562: FA 55 3E   LD      A,($3E55)       
6565: 01 EA 67   LD      BC,$67EA        
6568: C1         POP     BC              
6569: CD 76 17   CALL    $1776           
656C: FA 6B C1   LD      A,($C16B)       
656F: FE 04      CP      $04             
6571: 20 1D      JR      NZ,$6590        
6573: CD 36 56   CALL    $5636           
6576: F0 F7      LD      A,($F7)         
6578: FE 06      CP      $06             
657A: 28 08      JR      Z,$6584         
657C: 3E 03      LD      A,$03           
657E: E0 A9      LDFF00  ($A9),A         
6580: 3E 30      LD      A,$30           
6582: E0 AA      LDFF00  ($AA),A         
6584: CD 45 44   CALL    $4445           
6587: AF         XOR     A               
6588: EA BF C1   LD      ($C1BF),A       
658B: 3E 0F      LD      A,$0F           
658D: EA FE D6   LD      ($D6FE),A       
6590: C9         RET                     
6591: 1E 21      LD      E,$21           
6593: F0 F7      LD      A,($F7)         
6595: FE 06      CP      $06             
6597: 28 0A      JR      Z,$65A3         
6599: F0 F6      LD      A,($F6)         
659B: FE DD      CP      $DD             
659D: 1E 12      LD      E,$12           
659F: 20 02      JR      NZ,$65A3        
65A1: 1E 20      LD      E,$20           
65A3: 7B         LD      A,E             
65A4: EA FE D6   LD      ($D6FE),A       
65A7: AF         XOR     A               
65A8: EA 3F C1   LD      ($C13F),A       
65AB: C3 45 44   JP      $4445           
65AE: 1E 24      LD      E,$24           
65B0: F0 F7      LD      A,($F7)         
65B2: FE 06      CP      $06             
65B4: 28 0A      JR      Z,$65C0         
65B6: F0 F6      LD      A,($F6)         
65B8: FE DD      CP      $DD             
65BA: 1E 12      LD      E,$12           
65BC: 20 02      JR      NZ,$65C0        
65BE: 1E 23      LD      E,$23           
65C0: 7B         LD      A,E             
65C1: EA FF D6   LD      ($D6FF),A       
65C4: 3E FF      LD      A,$FF           
65C6: EA 9A DB   LD      ($DB9A),A       
65C9: AF         XOR     A               
65CA: E0 96      LDFF00  ($96),A         
65CC: E0 97      LDFF00  ($97),A         
65CE: EA 6B C1   LD      ($C16B),A       
65D1: EA 6C C1   LD      ($C16C),A       
65D4: 1E 08      LD      E,$08           
65D6: 21 10 D2   LD      HL,$D210        
65D9: 22         LD      (HLI),A         
65DA: 1D         DEC     E               
65DB: 20 FC      JR      NZ,$65D9        
65DD: C3 45 44   JP      $4445           
65E0: CD 50 67   CALL    $6750           
65E3: CD C3 17   CALL    $17C3           
65E6: FA 6B C1   LD      A,($C16B)       
65E9: FE 04      CP      $04             
65EB: 20 08      JR      NZ,$65F5        
65ED: CD 45 44   CALL    $4445           
65F0: 3E 80      LD      A,$80           
65F2: EA 10 D2   LD      ($D210),A       
65F5: C9         RET                     
65F6: F0 F7      LD      A,($F7)         
65F8: FE 06      CP      $06             
65FA: 20 09      JR      NZ,$6605        
65FC: CD 50 67   CALL    $6750           
65FF: 3E 06      LD      A,$06           
6601: EA 96 DB   LD      ($DB96),A       
6604: C9         RET                     
6605: F0 CC      LD      A,($CC)         
6607: E6 B0      AND     $B0             
6609: 28 0E      JR      Z,$6619         
660B: 3E 13      LD      A,$13           
660D: E0 F2      LDFF00  ($F2),A         
660F: CD 45 44   CALL    $4445           
6612: AF         XOR     A               
6613: EA 6B C1   LD      ($C16B),A       
6616: EA 6C C1   LD      ($C16C),A       
6619: C9         RET                     
661A: CD 50 67   CALL    $6750           
661D: FA 10 D2   LD      A,($D210)       
6620: 3D         DEC     A               
6621: EA 10 D2   LD      ($D210),A       
6624: 20 0B      JR      NZ,$6631        
6626: EA 56 C1   LD      ($C156),A       
6629: 3E 20      LD      A,$20           
662B: EA 10 D2   LD      ($D210),A       
662E: C3 45 44   JP      $4445           
6631: 1E 00      LD      E,$00           
6633: E6 04      AND     $04             
6635: 28 02      JR      Z,$6639         
6637: 1E FE      LD      E,$FE           
6639: 7B         LD      A,E             
663A: EA 56 C1   LD      ($C156),A       
663D: C9         RET                     
663E: CD 50 67   CALL    $6750           
6641: CD 91 66   CALL    $6691           
6644: FA 10 D2   LD      A,($D210)       
6647: 3D         DEC     A               
6648: EA 10 D2   LD      ($D210),A       
664B: 20 2D      JR      NZ,$667A        
664D: CD D7 08   CALL    $08D7           
6650: 3E 30      LD      A,$30           
6652: EA 10 D2   LD      ($D210),A       
6655: 3E 30      LD      A,$30           
6657: EA 14 D2   LD      ($D214),A       
665A: 3E 18      LD      A,$18           
665C: EA 15 D2   LD      ($D215),A       
665F: FA 11 D2   LD      A,($D211)       
6662: C6 08      ADD     $08             
6664: EA 11 D2   LD      ($D211),A       
6667: FA 13 D2   LD      A,($D213)       
666A: 3C         INC     A               
666B: EA 13 D2   LD      ($D213),A       
666E: FE 04      CP      $04             
6670: 20 08      JR      NZ,$667A        
6672: 3E 80      LD      A,$80           
6674: EA 10 D2   LD      ($D210),A       
6677: CD 45 44   CALL    $4445           
667A: C9         RET                     
667B: CD 50 67   CALL    $6750           
667E: CD 91 66   CALL    $6691           
6681: 21 10 D2   LD      HL,$D210        
6684: 35         DEC     (HL)            
6685: C0         RET     NZ              
6686: CD 45 44   CALL    $4445           
6689: AF         XOR     A               
668A: EA 6B C1   LD      ($C16B),A       
668D: EA 6C C1   LD      ($C16C),A       
6690: C9         RET                     
6691: AF         XOR     A               
6692: EA 56 C1   LD      ($C156),A       
6695: FA 15 D2   LD      A,($D215)       
6698: A7         AND     A               
6699: 28 10      JR      Z,$66AB         
669B: 3D         DEC     A               
669C: EA 15 D2   LD      ($D215),A       
669F: 1E FE      LD      E,$FE           
66A1: E6 04      AND     $04             
66A3: 28 02      JR      Z,$66A7         
66A5: 1E 00      LD      E,$00           
66A7: 7B         LD      A,E             
66A8: EA 56 C1   LD      ($C156),A       
66AB: C9         RET                     
66AC: 14         INC     D               
66AD: 14         INC     D               
66AE: 10 10      STOP    $10             
66B0: 0C         INC     C               
66B1: 0C         INC     C               
66B2: 00         NOP                     
66B3: 00         NOP                     
66B4: CC 10 00   CALL    Z,$0010         
66B7: 08 CE 10   LD      ($10CE),SP      
66BA: 00         NOP                     
66BB: 10 DC      STOP    $DC             
66BD: 10 00      STOP    $00             
66BF: 18 CC      JR      $668D           
66C1: 30 10      JR      NC,$66D3        
66C3: 00         NOP                     
66C4: DE 10      SBC     $10             
66C6: 10 08      STOP    $08             
66C8: E0 10      LDFF00  ($10),A         
66CA: 10 10      STOP    $10             
66CC: E2         LDFF00  (C),A           
66CD: 10 10      STOP    $10             
66CF: 18 DE      JR      $66AF           
66D1: 30 20      JR      NC,$66F3        
66D3: 00         NOP                     
66D4: E4                              
66D5: 10 20      STOP    $20             
66D7: 08 E6 10   LD      ($10E6),SP      
66DA: 20 10      JR      NZ,$66EC        
66DC: E8 10      ADD     SP,$10          
66DE: 20 18      JR      NZ,$66F8        
66E0: E4                              
66E1: 30 30      JR      NC,$6713        
66E3: 00         NOP                     
66E4: DE 10      SBC     $10             
66E6: 30 08      JR      NC,$66F0        
66E8: E0 10      LDFF00  ($10),A         
66EA: 30 10      JR      NC,$66FC        
66EC: E0 30      LDFF00  ($30),A         
66EE: 30 18      JR      NC,$6708        
66F0: DE 30      SBC     $30             
66F2: 40         LD      B,B             
66F3: 00         NOP                     
66F4: DE 10      SBC     $10             
66F6: 40         LD      B,B             
66F7: 08 E0 10   LD      ($10E0),SP      
66FA: 40         LD      B,B             
66FB: 10 E0      STOP    $E0             
66FD: 30 40      JR      NC,$673F        
66FF: 18 DE      JR      $66DF           
6701: 30 48      JR      NC,$674B        
6703: 08 F0 00   LD      ($00F0),SP      
6706: 48         LD      C,B             
6707: 10 F2      STOP    $F2             
6709: 00         NOP                     
670A: 48         LD      C,B             
670B: 18 F4      JR      $6701           
670D: 00         NOP                     
670E: 48         LD      C,B             
670F: 20 F4      JR      NZ,$6705        
6711: 20 48      JR      NZ,$675B        
6713: 28 F2      JR      Z,$6707         
6715: 20 48      JR      NZ,$675F        
6717: 30 F0      JR      NC,$6709        
6719: 20 48      JR      NZ,$6763        
671B: 08 F6 00   LD      ($00F6),SP      
671E: 48         LD      C,B             
671F: 10 F8      STOP    $F8             
6721: 00         NOP                     
6722: 48         LD      C,B             
6723: 18 FA      JR      $671F           
6725: 00         NOP                     
6726: 48         LD      C,B             
6727: 20 FA      JR      NZ,$6723        
6729: 20 48      JR      NZ,$6773        
672B: 28 F8      JR      Z,$6725         
672D: 20 48      JR      NZ,$6777        
672F: 30 F6      JR      NC,$6727        
6731: 20 48      JR      NZ,$677B        
6733: 08 FC 00   LD      ($00FC),SP      
6736: 48         LD      C,B             
6737: 10 FE      STOP    $FE             
6739: 00         NOP                     
673A: 48         LD      C,B             
673B: 18 EE      JR      $672B           
673D: 00         NOP                     
673E: 48         LD      C,B             
673F: 20 EE      JR      NZ,$672F        
6741: 20 48      JR      NZ,$678B        
6743: 28 FE      JR      Z,$6743         
6745: 20 48      JR      NZ,$678F        
6747: 30 FC      JR      NC,$6745        
6749: 20 02      JR      NZ,$674D        
674B: 67         LD      H,A             
674C: 1A         LD      A,(DE)          
674D: 67         LD      H,A             
674E: 32         LD      (HLD),A         
674F: 67         LD      H,A             
6750: F0 F7      LD      A,($F7)         
6752: FE 06      CP      $06             
6754: C0         RET     NZ              
6755: AF         XOR     A               
6756: E0 F1      LDFF00  ($F1),A         
6758: E0 ED      LDFF00  ($ED),A         
675A: E0 F5      LDFF00  ($F5),A         
675C: 3E 38      LD      A,$38           
675E: E0 EE      LDFF00  ($EE),A         
6760: FA 56 C1   LD      A,($C156)       
6763: 5F         LD      E,A             
6764: 3E 20      LD      A,$20           
6766: 93         SUB     E               
6767: E0 EC      LDFF00  ($EC),A         
6769: FA 14 D2   LD      A,($D214)       
676C: A7         AND     A               
676D: 28 27      JR      Z,$6796         
676F: 3D         DEC     A               
6770: EA 14 D2   LD      ($D214),A       
6773: F0 E7      LD      A,($E7)         
6775: E6 07      AND     $07             
6777: FA 12 D2   LD      A,($D212)       
677A: 20 06      JR      NZ,$6782        
677C: 3C         INC     A               
677D: FE 03      CP      $03             
677F: 20 01      JR      NZ,$6782        
6781: AF         XOR     A               
6782: EA 12 D2   LD      ($D212),A       
6785: 17         RLA                     
6786: E6 06      AND     $06             
6788: 5F         LD      E,A             
6789: 50         LD      D,B             
678A: 21 4A 67   LD      HL,$674A        
678D: 19         ADD     HL,DE           
678E: 2A         LD      A,(HLI)         
678F: 66         LD      H,(HL)          
6790: 6F         LD      L,A             
6791: 0E 06      LD      C,$06           
6793: CD 20 3D   CALL    $3D20           
6796: 3E 48      LD      A,$48           
6798: E0 EE      LDFF00  ($EE),A         
679A: FA 56 C1   LD      A,($C156)       
679D: 5F         LD      E,A             
679E: FA 11 D2   LD      A,($D211)       
67A1: C6 20      ADD     $20             
67A3: 93         SUB     E               
67A4: E0 EC      LDFF00  ($EC),A         
67A6: FA 13 D2   LD      A,($D213)       
67A9: 5F         LD      E,A             
67AA: 16 00      LD      D,$00           
67AC: 21 AC 66   LD      HL,$66AC        
67AF: 19         ADD     HL,DE           
67B0: 4E         LD      C,(HL)          
67B1: AF         XOR     A               
67B2: EA C0 C3   LD      ($C3C0),A       
67B5: 21 B2 66   LD      HL,$66B2        
67B8: CD 26 3D   CALL    $3D26           
67BB: C9         RET                     
67BC: FA 96 DB   LD      A,($DB96)       
67BF: C7         RST     0X00            
67C0: CC 67 F3   CALL    Z,$F367         
67C3: 67         LD      H,A             
67C4: 0B         DEC     BC              
67C5: 68         LD      L,B             
67C6: 1D         DEC     E               
67C7: 68         LD      L,B             
67C8: 36 68      LD      (HL),$68        
67CA: FD                              
67CB: 55         LD      D,L             
67CC: 3E 01      LD      A,$01           
67CE: EA 67 C1   LD      ($C167),A       
67D1: CD 76 17   CALL    $1776           
67D4: FA 6B C1   LD      A,($C16B)       
67D7: FE 04      CP      $04             
67D9: 20 17      JR      NZ,$67F2        
67DB: CD 36 56   CALL    $5636           
67DE: 3E 03      LD      A,$03           
67E0: E0 A9      LDFF00  ($A9),A         
67E2: 3E 30      LD      A,$30           
67E4: E0 AA      LDFF00  ($AA),A         
67E6: CD 45 44   CALL    $4445           
67E9: AF         XOR     A               
67EA: EA BF C1   LD      ($C1BF),A       
67ED: 3E 14      LD      A,$14           
67EF: EA FE D6   LD      ($D6FE),A       
67F2: C9         RET                     
67F3: 3E 15      LD      A,$15           
67F5: EA FF D6   LD      ($D6FF),A       
67F8: 3E FF      LD      A,$FF           
67FA: EA 9A DB   LD      ($DB9A),A       
67FD: AF         XOR     A               
67FE: E0 96      LDFF00  ($96),A         
6800: E0 97      LDFF00  ($97),A         
6802: EA 6B C1   LD      ($C16B),A       
6805: EA 6C C1   LD      ($C16C),A       
6808: C3 45 44   JP      $4445           
680B: CD C3 17   CALL    $17C3           
680E: FA 6B C1   LD      A,($C16B)       
6811: FE 04      CP      $04             
6813: 20 07      JR      NZ,$681C        
6815: CD 45 44   CALL    $4445           
6818: AF         XOR     A               
6819: EA C4 C3   LD      ($C3C4),A       
681C: C9         RET                     
681D: FA 9F C1   LD      A,($C19F)       
6820: A7         AND     A               
6821: C0         RET     NZ              
6822: FA C4 C3   LD      A,($C3C4)       
6825: 3C         INC     A               
6826: EA C4 C3   LD      ($C3C4),A       
6829: CA 45 44   JP      Z,$4445         
682C: FE 80      CP      $80             
682E: 20 05      JR      NZ,$6835        
6830: 3E E7      LD      A,$E7           
6832: CD 97 21   CALL    $2197           
6835: C9         RET                     
6836: F0 CC      LD      A,($CC)         
6838: E6 B0      AND     $B0             
683A: 28 07      JR      Z,$6843         
683C: 3E 13      LD      A,$13           
683E: E0 F2      LDFF00  ($F2),A         
6840: CD 0F 66   CALL    $660F           
6843: C9         RET                     
6844: 00         NOP                     
6845: 00         NOP                     
6846: 00         NOP                     
6847: 00         NOP                     
6848: 00         NOP                     
6849: 00         NOP                     
684A: 00         NOP                     
684B: 00         NOP                     
684C: 00         NOP                     
684D: 00         NOP                     
684E: 00         NOP                     
684F: 00         NOP                     
6850: 00         NOP                     
6851: 00         NOP                     
6852: 00         NOP                     
6853: 00         NOP                     
6854: 00         NOP                     
6855: 00         NOP                     
6856: 00         NOP                     
6857: 00         NOP                     
6858: 00         NOP                     
6859: 00         NOP                     
685A: 00         NOP                     
685B: 00         NOP                     
685C: 00         NOP                     
685D: 00         NOP                     
685E: 00         NOP                     
685F: 00         NOP                     
6860: 00         NOP                     
6861: 00         NOP                     
6862: 00         NOP                     
6863: 00         NOP                     
6864: 00         NOP                     
6865: 00         NOP                     
6866: 00         NOP                     
6867: 00         NOP                     
6868: 00         NOP                     
6869: 00         NOP                     
686A: 00         NOP                     
686B: 00         NOP                     
686C: 00         NOP                     
686D: 00         NOP                     
686E: 00         NOP                     
686F: 00         NOP                     
6870: 00         NOP                     
6871: 00         NOP                     
6872: 00         NOP                     
6873: 00         NOP                     
6874: 00         NOP                     
6875: 00         NOP                     
6876: 00         NOP                     
6877: 00         NOP                     
6878: 00         NOP                     
6879: 00         NOP                     
687A: 00         NOP                     
687B: 00         NOP                     
687C: 00         NOP                     
687D: 00         NOP                     
687E: 00         NOP                     
687F: 00         NOP                     
6880: 00         NOP                     
6881: 00         NOP                     
6882: 00         NOP                     
6883: 00         NOP                     
6884: F0 F0      LD      A,($F0)         
6886: F0 F0      LD      A,($F0)         
6888: F0 F0      LD      A,($F0)         
688A: F0 F0      LD      A,($F0)         
688C: F0 F0      LD      A,($F0)         
688E: F0 F0      LD      A,($F0)         
6890: F0 F0      LD      A,($F0)         
6892: F0 F0      LD      A,($F0)         
6894: E0 E0      LDFF00  ($E0),A         
6896: E0 E0      LDFF00  ($E0),A         
6898: E0 E2      LDFF00  ($E2),A         
689A: E5         PUSH    HL              
689B: E8 EB      ADD     SP,$EB          
689D: EE F1      XOR     $F1             
689F: F4                              
68A0: F7         RST     0X30            
68A1: FA FD 00   LD      A,($00FD)       
68A4: 03         INC     BC              
68A5: 06 09      LD      B,$09           
68A7: 0C         INC     C               
68A8: 0F         RRCA                    
68A9: 12         LD      (DE),A          
68AA: 15         DEC     D               
68AB: 18 1B      JR      $68C8           
68AD: 1E 21      LD      E,$21           
68AF: 24         INC     H               
68B0: 27         DAA                     
68B1: 2A         LD      A,(HLI)         
68B2: 2D         DEC     L               
68B3: 30 33      JR      NC,$68E8        
68B5: 36 39      LD      (HL),$39        
68B7: 3C         INC     A               
68B8: 3F         CCF                     
68B9: 42         LD      B,D             
68BA: 45         LD      B,L             
68BB: 48         LD      C,B             
68BC: 33         INC     SP              
68BD: 36 39      LD      (HL),$39        
68BF: 3C         INC     A               
68C0: 3F         CCF                     
68C1: 42         LD      B,D             
68C2: 45         LD      B,L             
68C3: 48         LD      C,B             
68C4: F0 F0      LD      A,($F0)         
68C6: F0 F0      LD      A,($F0)         
68C8: F0 F0      LD      A,($F0)         
68CA: F0 F0      LD      A,($F0)         
68CC: F0 F0      LD      A,($F0)         
68CE: F0 F0      LD      A,($F0)         
68D0: F0 F0      LD      A,($F0)         
68D2: F0 E0      LD      A,($E0)         
68D4: E2         LDFF00  (C),A           
68D5: E4                              
68D6: E6 E8      AND     $E8             
68D8: EA EC EE   LD      ($EEEC),A       
68DB: F0 F2      LD      A,($F2)         
68DD: F4                              
68DE: F6 F8      OR      $F8             
68E0: FA FC FE   LD      A,($FEFC)       
68E3: 00         NOP                     
68E4: 02         LD      (BC),A          
68E5: 04         INC     B               
68E6: 06 08      LD      B,$08           
68E8: 0A         LD      A,(BC)          
68E9: 0C         INC     C               
68EA: 0E 10      LD      C,$10           
68EC: 12         LD      (DE),A          
68ED: 14         INC     D               
68EE: 16 18      LD      D,$18           
68F0: 1A         LD      A,(DE)          
68F1: 1C         INC     E               
68F2: 1D         DEC     E               
68F3: 1E 20      LD      E,$20           
68F5: 22         LD      (HLI),A         
68F6: 24         INC     H               
68F7: 26 28      LD      H,$28           
68F9: 2A         LD      A,(HLI)         
68FA: 2C         INC     L               
68FB: 2E 20      LD      L,$20           
68FD: 22         LD      (HLI),A         
68FE: 24         INC     H               
68FF: 26 

6900: 28          
6901: 2A         LD      A,(HLI)         
6902: 2C         INC     L               
6903: 2E F0      LD      L,$F0           
6905: F0 F0      LD      A,($F0)         
6907: F0 F0      LD      A,($F0)         
6909: F0 F0      LD      A,($F0)         
690B: F0 F0      LD      A,($F0)         
690D: DF         RST     0X18            
690E: E0 E2      LDFF00  ($E2),A  
       
6910: E3                              
6911: E5         PUSH    HL              
6912: E6 E8      AND     $E8             
6914: E9         JP      (HL)            
6915: EB                              
6916: EC                              
6917: EE EF      XOR     $EF             
6919: F1         POP     AF              
691A: F2                              
691B: F4                              
691C: F5         PUSH    AF              
691D: F7         RST     0X30            
691E: F8 FA      LDHL    SP,$FA   
       
6920: FB         EI                      
6921: FD                              
6922: FE 00      CP      $00             
6924: 01 03 04   LD      BC,$0403        
6927: 06 07      LD      B,$07           
6929: 09         ADD     HL,BC           
692A: 0A         LD      A,(BC)          
692B: 0C         INC     C               
692C: 0D         DEC     C               
692D: 0F         RRCA                    
692E: 10 12      STOP    $12     
        
6930: 13         INC     DE              
6931: 15         DEC     D               
6932: 16 18      LD      D,$18           
6934: 19         ADD     HL,DE           
6935: 1B         DEC     DE              
6936: 1C         INC     E               
6937: 1E 1F      LD      E,$1F           
6939: 21 22 24   LD      HL,$2422        
693C: 19         ADD     HL,DE           
693D: 1B         DEC     DE              
693E: 1C         INC     E               
693F: 1E 1F      LD      E,$1F           
6941: 21 22 24   LD      HL,$2422        
6944: F0 F0      LD      A,($F0)         
6946: F0 F0      LD      A,($F0)         
6948: F0 F0      LD      A,($F0)         
694A: F0 F0      LD      A,($F0)         
694C: F0 F0      LD      A,($F0)         
694E: E2         LDFF00  (C),A           
694F: E3                              
6950: E5         PUSH    HL              
6951: E6 E8      AND     $E8             
6953: E9         JP      (HL)            
6954: EB                              
6955: EC                              
6956: EE F0      XOR     $F0             
6958: F2                              
6959: F3         DI                      
695A: F6 F7      OR      $F7             
695C: F8 F9      LDHL    SP,$F9          
695E: FA FC FD   LD      A,($FDFC)       
6961: FE FF      CP      $FF             
6963: 00         NOP                     
6964: 01 03 04   LD      BC,$0403        
6967: 06 07      LD      B,$07           
6969: 09         ADD     HL,BC           
696A: 0A         LD      A,(BC)          
696B: 0C         INC     C               
696C: 0D         DEC     C               
696D: 0F         RRCA                    
696E: 10 12      STOP    $12             
6970: 13         INC     DE              
6971: 15         DEC     D               
6972: 16 18      LD      D,$18           
6974: 19         ADD     HL,DE           
6975: 1B         DEC     DE              
6976: 1C         INC     E               
6977: 1E 1F      LD      E,$1F           
6979: 21 22 22   LD      HL,$2222        
697C: 24         INC     H               
697D: 25         DEC     H               
697E: 27         DAA                     
697F: 29         ADD     HL,HL           
6980: 2B         DEC     HL              
6981: 2C         INC     L               
6982: 2E 2F      LD      L,$2F           
6984: F0 F0      LD      A,($F0)         
6986: F0 F0      LD      A,($F0)         
6988: F0 F0      LD      A,($F0)         
698A: F0 F0      LD      A,($F0)         
698C: E1         POP     HL              
698D: E2         LDFF00  (C),A           
698E: E4                              
698F: E5         PUSH    HL              
6990: E6 E8      AND     $E8             
6992: E9         JP      (HL)            
6993: EA EC ED   LD      ($EDEC),A       
6996: EE F0      XOR     $F0             
6998: F1         POP     AF              
6999: F2                              
699A: F4                              
699B: F5         PUSH    AF              
699C: F6 F8      OR      $F8             
699E: F9         LD      SP,HL           
699F: FA FC FE   LD      A,($FEFC)       
69A2: FF         RST     0X38            
69A3: 00         NOP                     
69A4: 01 02 04   LD      BC,$0402        
69A7: 05         DEC     B               
69A8: 06 08      LD      B,$08           
69AA: 09         ADD     HL,BC           
69AB: 0A         LD      A,(BC)          
69AC: 0C         INC     C               
69AD: 0D         DEC     C               
69AE: 0E 10      LD      C,$10           
69B0: 11 12 14   LD      DE,$1412        
69B3: 15         DEC     D               
69B4: 16 18      LD      D,$18           
69B6: 19         ADD     HL,DE           
69B7: 1A         LD      A,(DE)          
69B8: 1C         INC     E               
69B9: 1D         DEC     E               
69BA: 1E 20      LD      E,$20           
69BC: 22         LD      (HLI),A         
69BD: 23         INC     HL              
69BE: 24         INC     H               
69BF: 25         DEC     H               
69C0: 27         DAA                     
69C1: 28 2A      JR      Z,$69ED         
69C3: 2B         DEC     HL              
69C4: F0 F0      LD      A,($F0)         
69C6: F0 F0      LD      A,($F0)         
69C8: F0 F0      LD      A,($F0)         
69CA: F0 E2      LD      A,($E2)         
69CC: E3                              
69CD: E4                              
69CE: E5         PUSH    HL              
69CF: E6 E8      AND     $E8             
69D1: E9         JP      (HL)            
69D2: EA EC ED   LD      ($EDEC),A       
69D5: EE EF      XOR     $EF             
69D7: F1         POP     AF              
69D8: F2                              
69D9: F3         DI                      
69DA: F5         PUSH    AF              
69DB: F6 F8      OR      $F8             
69DD: F9         LD      SP,HL           
69DE: FA FB FD   LD      A,($FDFB)       
69E1: FE FF      CP      $FF             
69E3: 00         NOP                     
69E4: 01 02 03   LD      BC,$0302        
69E7: 05         DEC     B               
69E8: 06 07      LD      B,$07           
69EA: 08 0A 0B   LD      ($0B0A),SP      
69ED: 0C         INC     C               
69EE: 0D         DEC     C               
69EF: 0F         RRCA                    
69F0: 10 11      STOP    $11             
69F2: 12         LD      (DE),A          
69F3: 14         INC     D               
69F4: 15         DEC     D               
69F5: 16 17      LD      D,$17           
69F7: 19         ADD     HL,DE           
69F8: 1A         LD      A,(DE)          
69F9: 1B         DEC     DE              
69FA: 1D         DEC     E               
69FB: 1E 20      LD      E,$20           
69FD: 21 22 23   LD      HL,$2322        
6A00: 25         DEC     H               
6A01: 26 27      LD      H,$27           
6A03: 28 F0      JR      Z,$69F5         
6A05: F0 F0      LD      A,($F0)         
6A07: F0 F0      LD      A,($F0)         
6A09: F0 E3      LD      A,($E3)         
6A0B: E4                              
6A0C: E5         PUSH    HL              
6A0D: E6 E7      AND     $E7             
6A0F: E8 E9      ADD     SP,$E9          
6A11: EB                              
6A12: EC                              
6A13: ED                              
6A14: EE F0      XOR     $F0             
6A16: F1         POP     AF              
6A17: F2                              
6A18: F3         DI                      
6A19: F4                              
6A1A: F6 F7      OR      $F7             
6A1C: F8 F9      LDHL    SP,$F9          
6A1E: FB         EI                      
6A1F: FC                              
6A20: FD                              
6A21: FE FF      CP      $FF             
6A23: 00         NOP                     
6A24: 01 02 03   LD      BC,$0302        
6A27: 04         INC     B               
6A28: 06 07      LD      B,$07           
6A2A: 08 09 0A   LD      ($0A09),SP      
6A2D: 0B         DEC     BC              
6A2E: 0C         INC     C               
6A2F: 0E 10      LD      C,$10           
6A31: 11 12 13   LD      DE,$1312        
6A34: 14         INC     D               
6A35: 15         DEC     D               
6A36: 16 18      LD      D,$18           
6A38: 19         ADD     HL,DE           
6A39: 1A         LD      A,(DE)          
6A3A: 1B         DEC     DE              
6A3B: 1C         INC     E               
6A3C: 1D         DEC     E               
6A3D: 1F         RRA                     
6A3E: 20 21      JR      NZ,$6A61        
6A40: 22         LD      (HLI),A         
6A41: 23         INC     HL              
6A42: 24         INC     H               
6A43: 25         DEC     H               
6A44: F0 F0      LD      A,($F0)         
6A46: F0 F0      LD      A,($F0)         
6A48: F0 E4      LD      A,($E4)         
6A4A: E5         PUSH    HL              
6A4B: E6 E7      AND     $E7             
6A4D: E8 E9      ADD     SP,$E9          
6A4F: EA EB EC   LD      ($ECEB),A       
6A52: EE EF      XOR     $EF             
6A54: F0 F1      LD      A,($F1)         
6A56: F2                              
6A57: F3         DI                      
6A58: F4                              
6A59: F5         PUSH    AF              
6A5A: F6 F8      OR      $F8             
6A5C: F9         LD      SP,HL           
6A5D: FA FB FC   LD      A,($FCFB)       
6A60: FD                              
6A61: FE FF      CP      $FF             
6A63: 00         NOP                     
6A64: 01 02 03   LD      BC,$0302        
6A67: 04         INC     B               
6A68: 05         DEC     B               
6A69: 06 07      LD      B,$07           
6A6B: 08 09 0A   LD      ($0A09),SP      
6A6E: 0C         INC     C               
6A6F: 0D         DEC     C               
6A70: 0E 0F      LD      C,$0F           
6A72: 10 11      STOP    $11             
6A74: 12         LD      (DE),A          
6A75: 13         INC     DE              
6A76: 15         DEC     D               
6A77: 16 17      LD      D,$17           
6A79: 18 19      JR      $6A94           
6A7B: 1A         LD      A,(DE)          
6A7C: 1B         DEC     DE              
6A7D: 1C         INC     E               
6A7E: 1D         DEC     E               
6A7F: 1E 1F      LD      E,$1F           
6A81: 21 22 23   LD      HL,$2322        
6A84: F0 F0      LD      A,($F0)         
6A86: F0 F0      LD      A,($F0)         
6A88: E5         PUSH    HL              
6A89: E6 E7      AND     $E7             
6A8B: E8 E9      ADD     SP,$E9          
6A8D: EA EB EC   LD      ($ECEB),A       
6A90: ED                              
6A91: EE EF      XOR     $EF             
6A93: F0 F1      LD      A,($F1)         
6A95: F2                              
6A96: F3         DI                      
6A97: F4                              
6A98: F5         PUSH    AF              
6A99: F6 F7      OR      $F7             
6A9B: F8 F9      LDHL    SP,$F9          
6A9D: FA FB FC   LD      A,($FCFB)       
6AA0: FD                              
6AA1: FE FF      CP      $FF             
6AA3: 00         NOP                     
6AA4: 01 02 03   LD      BC,$0302        
6AA7: 04         INC     B               
6AA8: 05         DEC     B               
6AA9: 06 07      LD      B,$07           
6AAB: 08 09 0A   LD      ($0A09),SP      
6AAE: 0B         DEC     BC              
6AAF: 0C         INC     C               
6AB0: 0D         DEC     C               
6AB1: 0E 0F      LD      C,$0F           
6AB3: 10 11      STOP    $11             
6AB5: 12         LD      (DE),A          
6AB6: 13         INC     DE              
6AB7: 14         INC     D               
6AB8: 15         DEC     D               
6AB9: 16 17      LD      D,$17           
6ABB: 18 19      JR      $6AD6           
6ABD: 1A         LD      A,(DE)          
6ABE: 1B         DEC     DE              
6ABF: 1C         INC     E               
6AC0: 1D         DEC     E               
6AC1: 1E 1F      LD      E,$1F           
6AC3: 20 F0      JR      NZ,$6AB5        
6AC5: F0 F0      LD      A,($F0)         
6AC7: E6 E7      AND     $E7             
6AC9: E8 E8      ADD     SP,$E8          
6ACB: E9         JP      (HL)            
6ACC: EA EB EC   LD      ($ECEB),A       
6ACF: ED                              
6AD0: EE EF      XOR     $EF             
6AD2: F0 F0      LD      A,($F0)         
6AD4: F1         POP     AF              
6AD5: F2                              
6AD6: F3         DI                      
6AD7: F4                              
6AD8: F5         PUSH    AF              
6AD9: F6 F7      OR      $F7             
6ADB: F8 F8      LDHL    SP,$F8          
6ADD: F9         LD      SP,HL           
6ADE: FA FB FC   LD      A,($FCFB)       
6AE1: FD                              
6AE2: FE FF      CP      $FF             
6AE4: 00         NOP                     
6AE5: 01 02 03   LD      BC,$0302        
6AE8: 04         INC     B               
6AE9: 05         DEC     B               
6AEA: 06 07      LD      B,$07           
6AEC: 07         RLCA                    
6AED: 08 09 0A   LD      ($0A09),SP      
6AF0: 0B         DEC     BC              
6AF1: 0C         INC     C               
6AF2: 0D         DEC     C               
6AF3: 0E 0F      LD      C,$0F           
6AF5: 10 11      STOP    $11             
6AF7: 12         LD      (DE),A          
6AF8: 13         INC     DE              
6AF9: 14         INC     D               
6AFA: 15         DEC     D               
6AFB: 16 17      LD      D,$17           
6AFD: 18 19      JR      $6B18           
6AFF: 1A         LD      A,(DE)          
6B00: 1A         LD      A,(DE)          
6B01: 1B         DEC     DE              
6B02: 1C         INC     E               
6B03: 1D         DEC     E               
6B04: F0 F0      LD      A,($F0)         
6B06: E7         RST     0X20            
6B07: E8 E9      ADD     SP,$E9          
6B09: EA EB EC   LD      ($ECEB),A       
6B0C: EC                              
6B0D: EC                              
6B0E: ED                              
6B0F: EE EF      XOR     $EF             
6B11: F0 F1      LD      A,($F1)         
6B13: F2                              
6B14: F2                              
6B15: F3         DI                      
6B16: F4                              
6B17: F5         PUSH    AF              
6B18: F6 F7      OR      $F7             
6B1A: F7         RST     0X30            
6B1B: F8 F9      LDHL    SP,$F9          
6B1D: FA FB FC   LD      A,($FCFB)       
6B20: FC                              
6B21: FD                              
6B22: FE FF      CP      $FF             
6B24: 00         NOP                     
6B25: 01 02 03   LD      BC,$0302        
6B28: 04         INC     B               
6B29: 04         INC     B               
6B2A: 05         DEC     B               
6B2B: 06 07      LD      B,$07           
6B2D: 08 09 09   LD      ($0909),SP      
6B30: 0A         LD      A,(BC)          
6B31: 0B         DEC     BC              
6B32: 0C         INC     C               
6B33: 0D         DEC     C               
6B34: 0E 0E      LD      C,$0E           
6B36: 0F         RRCA                    
6B37: 10 11      STOP    $11             
6B39: 12         LD      (DE),A          
6B3A: 13         INC     DE              
6B3B: 14         INC     D               
6B3C: 15         DEC     D               
6B3D: 16 16      LD      D,$16           
6B3F: 17         RLA                     
6B40: 18 19      JR      $6B5B           
6B42: 1A         LD      A,(DE)          
6B43: 1B         DEC     DE              
6B44: F0 E9      LD      A,($E9)         
6B46: E9         JP      (HL)            
6B47: EA EB EB   LD      ($EBEB),A       
6B4A: EC                              
6B4B: ED                              
6B4C: EE EE      XOR     $EE             
6B4E: EF         RST     0X28            
6B4F: F0 F0      LD      A,($F0)         
6B51: F1         POP     AF              
6B52: F2                              
6B53: F3         DI                      
6B54: F4                              
6B55: F4                              
6B56: F5         PUSH    AF              
6B57: F6 F7      OR      $F7             
6B59: F8 F8      LDHL    SP,$F8          
6B5B: F9         LD      SP,HL           
6B5C: FA FB FC   LD      A,($FCFB)       
6B5F: FC                              
6B60: FD                              
6B61: FE FF      CP      $FF             
6B63: 00         NOP                     
6B64: 00         NOP                     
6B65: 01 02 03   LD      BC,$0302        
6B68: 03         INC     BC              
6B69: 04         INC     B               
6B6A: 05         DEC     B               
6B6B: 06 06      LD      B,$06           
6B6D: 07         RLCA                    
6B6E: 08 09 0A   LD      ($0A09),SP      
6B71: 0A         LD      A,(BC)          
6B72: 0B         DEC     BC              
6B73: 0C         INC     C               
6B74: 0C         INC     C               
6B75: 0D         DEC     C               
6B76: 0E 0E      LD      C,$0E           
6B78: 10 11      STOP    $11             
6B7A: 12         LD      (DE),A          
6B7B: 12         LD      (DE),A          
6B7C: 13         INC     DE              
6B7D: 14         INC     D               
6B7E: 15         DEC     D               
6B7F: 15         DEC     D               
6B80: 16 17      LD      D,$17           
6B82: 18 18      JR      $6B9C           
6B84: EB                              
6B85: EC                              
6B86: EC                              
6B87: ED                              
6B88: EE EE      XOR     $EE             
6B8A: EF         RST     0X28            
6B8B: F0 F0      LD      A,($F0)         
6B8D: F1         POP     AF              
6B8E: F2                              
6B8F: F2                              
6B90: F3         DI                      
6B91: F4                              
6B92: F4                              
6B93: F5         PUSH    AF              
6B94: F6 F6      OR      $F6             
6B96: F7         RST     0X30            
6B97: F8 F8      LDHL    SP,$F8          
6B99: F9         LD      SP,HL           
6B9A: FA FA FB   LD      A,($FBFA)       
6B9D: FC                              
6B9E: FC                              
6B9F: FD                              
6BA0: FE FE      CP      $FE             
6BA2: FF         RST     0X38            
6BA3: 00         NOP                     
6BA4: 00         NOP                     
6BA5: 01 02 02   LD      BC,$0202        
6BA8: 03         INC     BC              
6BA9: 04         INC     B               
6BAA: 04         INC     B               
6BAB: 05         DEC     B               
6BAC: 06 06      LD      B,$06           
6BAE: 07         RLCA                    
6BAF: 08 08 09   LD      ($0908),SP      
6BB2: 0A         LD      A,(BC)          
6BB3: 0A         LD      A,(BC)          
6BB4: 0B         DEC     BC              
6BB5: 0C         INC     C               
6BB6: 0C         INC     C               
6BB7: 0D         DEC     C               
6BB8: 0E 0E      LD      C,$0E           
6BBA: 0F         RRCA                    
6BBB: 10 10      STOP    $10             
6BBD: 11 12 12   LD      DE,$1212        
6BC0: 13         INC     DE              
6BC1: 14         INC     D               
6BC2: 14         INC     D               
6BC3: 15         DEC     D               
6BC4: ED                              
6BC5: EE EE      XOR     $EE             
6BC7: EF         RST     0X28            
6BC8: F0 F0      LD      A,($F0)         
6BCA: F1         POP     AF              
6BCB: F1         POP     AF              
6BCC: F2                              
6BCD: F2                              
6BCE: F3         DI                      
6BCF: F3         DI                      
6BD0: F3         DI                      
6BD1: F4                              
6BD2: F5         PUSH    AF              
6BD3: F5         PUSH    AF              
6BD4: F6 F6      OR      $F6             
6BD6: F7         RST     0X30            
6BD7: F8 F8      LDHL    SP,$F8          
6BD9: F9         LD      SP,HL           
6BDA: F9         LD      SP,HL           
6BDB: FA FB FB   LD      A,($FBFB)       
6BDE: FC                              
6BDF: FC                              
6BE0: FE FF      CP      $FF             
6BE2: FF         RST     0X38            
6BE3: 00         NOP                     
6BE4: 00         NOP                     
6BE5: 01 01 02   LD      BC,$0201        
6BE8: 03         INC     BC              
6BE9: 03         INC     BC              
6BEA: 04         INC     B               
6BEB: 04         INC     B               
6BEC: 05         DEC     B               
6BED: 06 06      LD      B,$06           
6BEF: 07         RLCA                    
6BF0: 07         RLCA                    
6BF1: 08 09 09   LD      ($0909),SP      
6BF4: 0A         LD      A,(BC)          
6BF5: 0A         LD      A,(BC)          
6BF6: 0B         DEC     BC              
6BF7: 0C         INC     C               
6BF8: 0C         INC     C               
6BF9: 0D         DEC     C               
6BFA: 0D         DEC     C               
6BFB: 0E 0F      LD      C,$0F           
6BFD: 0F         RRCA                    
6BFE: 10 10      STOP    $10             
6C00: 11 12 12   LD      DE,$1212        
6C03: 13         INC     DE              
6C04: F0 F1      LD      A,($F1)         
6C06: F1         POP     AF              
6C07: F2                              
6C08: F2                              
6C09: F3         DI                      
6C0A: F3         DI                      
6C0B: F4                              
6C0C: F4                              
6C0D: F5         PUSH    AF              
6C0E: F5         PUSH    AF              
6C0F: F6 F6      OR      $F6             
6C11: F7         RST     0X30            
6C12: F7         RST     0X30            
6C13: F8 F8      LDHL    SP,$F8          
6C15: F9         LD      SP,HL           
6C16: F9         LD      SP,HL           
6C17: FA FA FB   LD      A,($FBFA)       
6C1A: FB         EI                      
6C1B: FC                              
6C1C: FC                              
6C1D: FD                              
6C1E: FD                              
6C1F: FE FE      CP      $FE             
6C21: FF         RST     0X38            
6C22: FF         RST     0X38            
6C23: 00         NOP                     
6C24: 00         NOP                     
6C25: 01 01 02   LD      BC,$0201        
6C28: 02         LD      (BC),A          
6C29: 03         INC     BC              
6C2A: 03         INC     BC              
6C2B: 04         INC     B               
6C2C: 04         INC     B               
6C2D: 05         DEC     B               
6C2E: 05         DEC     B               
6C2F: 06 06      LD      B,$06           
6C31: 07         RLCA                    
6C32: 07         RLCA                    
6C33: 08 08 09   LD      ($0908),SP      
6C36: 09         ADD     HL,BC           
6C37: 0A         LD      A,(BC)          
6C38: 0A         LD      A,(BC)          
6C39: 0B         DEC     BC              
6C3A: 0B         DEC     BC              
6C3B: 0C         INC     C               
6C3C: 0C         INC     C               
6C3D: 0D         DEC     C               
6C3E: 0D         DEC     C               
6C3F: 0E 0E      LD      C,$0E           
6C41: 0F         RRCA                    
6C42: 0F         RRCA                    
6C43: 10 F3      STOP    $F3             
6C45: F4                              
6C46: F4                              
6C47: F4                              
6C48: F5         PUSH    AF              
6C49: F5         PUSH    AF              
6C4A: F6 F6      OR      $F6             
6C4C: F6 F7      OR      $F7             
6C4E: F7         RST     0X30            
6C4F: F8 F8      LDHL    SP,$F8          
6C51: F8 F9      LDHL    SP,$F9          
6C53: F9         LD      SP,HL           
6C54: FA FA FA   LD      A,($FAFA)       
6C57: FB         EI                      
6C58: FB         EI                      
6C59: FC                              
6C5A: FC                              
6C5B: FC                              
6C5C: FD                              
6C5D: FD                              
6C5E: FE FE      CP      $FE             
6C60: FF         RST     0X38            
6C61: FF         RST     0X38            
6C62: 00         NOP                     
6C63: 00         NOP                     
6C64: 00         NOP                     
6C65: 01 01 02   LD      BC,$0201        
6C68: 02         LD      (BC),A          
6C69: 03         INC     BC              
6C6A: 03         INC     BC              
6C6B: 03         INC     BC              
6C6C: 04         INC     B               
6C6D: 04         INC     B               
6C6E: 05         DEC     B               
6C6F: 05         DEC     B               
6C70: 05         DEC     B               
6C71: 06 06      LD      B,$06           
6C73: 07         RLCA                    
6C74: 07         RLCA                    
6C75: 07         RLCA                    
6C76: 08 08 09   LD      ($0908),SP      
6C79: 09         ADD     HL,BC           
6C7A: 09         ADD     HL,BC           
6C7B: 0A         LD      A,(BC)          
6C7C: 0A         LD      A,(BC)          
6C7D: 0B         DEC     BC              
6C7E: 0B         DEC     BC              
6C7F: 0B         DEC     BC              
6C80: 0C         INC     C               
6C81: 0C         INC     C               
6C82: 0D         DEC     C               
6C83: 0D         DEC     C               
6C84: F5         PUSH    AF              
6C85: F6 F6      OR      $F6             
6C87: F6 F7      OR      $F7             
6C89: F7         RST     0X30            
6C8A: F7         RST     0X30            
6C8B: F8 F8      LDHL    SP,$F8          
6C8D: F8 F9      LDHL    SP,$F9          
6C8F: F9         LD      SP,HL           
6C90: F9         LD      SP,HL           
6C91: FA FA FA   LD      A,($FAFA)       
6C94: FB         EI                      
6C95: FB         EI                      
6C96: FB         EI                      
6C97: FC                              
6C98: FC                              
6C99: FC                              
6C9A: FD                              
6C9B: FD                              
6C9C: FD                              
6C9D: FE FE      CP      $FE             
6C9F: FE FF      CP      $FF             
6CA1: FF         RST     0X38            
6CA2: FF         RST     0X38            
6CA3: 00         NOP                     
6CA4: 00         NOP                     
6CA5: 01 01 01   LD      BC,$0101        
6CA8: 02         LD      (BC),A          
6CA9: 02         LD      (BC),A          
6CAA: 02         LD      (BC),A          
6CAB: 03         INC     BC              
6CAC: 03         INC     BC              
6CAD: 03         INC     BC              
6CAE: 04         INC     B               
6CAF: 04         INC     B               
6CB0: 04         INC     B               
6CB1: 05         DEC     B               
6CB2: 05         DEC     B               
6CB3: 05         DEC     B               
6CB4: 06 06      LD      B,$06           
6CB6: 06 07      LD      B,$07           
6CB8: 07         RLCA                    
6CB9: 07         RLCA                    
6CBA: 08 08 08   LD      ($0808),SP      
6CBD: 09         ADD     HL,BC           
6CBE: 09         ADD     HL,BC           
6CBF: 09         ADD     HL,BC           
6CC0: 0A         LD      A,(BC)          
6CC1: 0A         LD      A,(BC)          
6CC2: 0A         LD      A,(BC)          
6CC3: 0B         DEC     BC              
6CC4: FC                              
6CC5: FC                              
6CC6: FB         EI                      
6CC7: FB         EI                      
6CC8: FB         EI                      
6CC9: FB         EI                      
6CCA: FA FA FA   LD      A,($FAFA)       
6CCD: FA FB FB   LD      A,($FBFB)       
6CD0: FB         EI                      
6CD1: FB         EI                      
6CD2: FC                              
6CD3: FC                              
6CD4: FC                              
6CD5: FC                              
6CD6: FD                              
6CD7: FD                              
6CD8: FD                              
6CD9: FD                              
6CDA: FE FE      CP      $FE             
6CDC: FE FE      CP      $FE             
6CDE: FF         RST     0X38            
6CDF: FF         RST     0X38            
6CE0: FF         RST     0X38            
6CE1: FF         RST     0X38            
6CE2: 00         NOP                     
6CE3: 00         NOP                     
6CE4: 00         NOP                     
6CE5: 00         NOP                     
6CE6: 01 01 01   LD      BC,$0101        
6CE9: 01 02 02   LD      BC,$0202        
6CEC: 02         LD      (BC),A          
6CED: 02         LD      (BC),A          
6CEE: 03         INC     BC              
6CEF: 03         INC     BC              
6CF0: 03         INC     BC              
6CF1: 03         INC     BC              
6CF2: 04         INC     B               
6CF3: 04         INC     B               
6CF4: 04         INC     B               
6CF5: 04         INC     B               
6CF6: 05         DEC     B               
6CF7: 05         DEC     B               
6CF8: 05         DEC     B               
6CF9: 05         DEC     B               
6CFA: 06 06      LD      B,$06           
6CFC: 06 06      LD      B,$06           
6CFE: 07         RLCA                    
6CFF: 07         RLCA                    
6D00: 07         RLCA                    
6D01: 07         RLCA                    
6D02: 08 08 FB   LD      ($FB08),SP      
6D05: FB         EI                      
6D06: FB         EI                      
6D07: FB         EI                      
6D08: FB         EI                      
6D09: FC                              
6D0A: FC                              
6D0B: FC                              
6D0C: FC                              
6D0D: FC                              
6D0E: FC                              
6D0F: FD                              
6D10: FD                              
6D11: FD                              
6D12: FD                              
6D13: FD                              
6D14: FE FE      CP      $FE             
6D16: FE FE      CP      $FE             
6D18: FE FE      CP      $FE             
6D1A: FF         RST     0X38            
6D1B: FF         RST     0X38            
6D1C: FF         RST     0X38            
6D1D: FF         RST     0X38            
6D1E: FF         RST     0X38            
6D1F: FF         RST     0X38            
6D20: 00         NOP                     
6D21: 00         NOP                     
6D22: 00         NOP                     
6D23: 00         NOP                     
6D24: 00         NOP                     
6D25: 00         NOP                     
6D26: 01 01 01   LD      BC,$0101        
6D29: 01 01 01   LD      BC,$0101        
6D2C: 02         LD      (BC),A          
6D2D: 02         LD      (BC),A          
6D2E: 02         LD      (BC),A          
6D2F: 02         LD      (BC),A          
6D30: 02         LD      (BC),A          
6D31: 02         LD      (BC),A          
6D32: 03         INC     BC              
6D33: 03         INC     BC              
6D34: 03         INC     BC              
6D35: 03         INC     BC              
6D36: 03         INC     BC              
6D37: 03         INC     BC              
6D38: 04         INC     B               
6D39: 04         INC     B               
6D3A: 04         INC     B               
6D3B: 04         INC     B               
6D3C: 04         INC     B               
6D3D: 04         INC     B               
6D3E: 05         DEC     B               
6D3F: 05         DEC     B               
6D40: 05         DEC     B               
6D41: 05         DEC     B               
6D42: 05         DEC     B               
6D43: 05         DEC     B               
6D44: FD                              
6D45: FD                              
6D46: FD                              
6D47: FD                              
6D48: FD                              
6D49: FD                              
6D4A: FD                              
6D4B: FD                              
6D4C: FE FE      CP      $FE             
6D4E: FE FE      CP      $FE             
6D50: FE FE      CP      $FE             
6D52: FE FE      CP      $FE             
6D54: FE FE      CP      $FE             
6D56: FF         RST     0X38            
6D57: FE FF      CP      $FF             
6D59: FF         RST     0X38            
6D5A: FF         RST     0X38            
6D5B: FF         RST     0X38            
6D5C: FF         RST     0X38            
6D5D: FF         RST     0X38            
6D5E: FF         RST     0X38            
6D5F: 00         NOP                     
6D60: 00         NOP                     
6D61: 00         NOP                     
6D62: 00         NOP                     
6D63: 00         NOP                     
6D64: 00         NOP                     
6D65: 00         NOP                     
6D66: 00         NOP                     
6D67: 00         NOP                     
6D68: 00         NOP                     
6D69: 01 01 01   LD      BC,$0101        
6D6C: 01 01 01   LD      BC,$0101        
6D6F: 01 01 01   LD      BC,$0101        
6D72: 01 02 02   LD      BC,$0202        
6D75: 02         LD      (BC),A          
6D76: 02         LD      (BC),A          
6D77: 02         LD      (BC),A          
6D78: 02         LD      (BC),A          
6D79: 02         LD      (BC),A          
6D7A: 02         LD      (BC),A          
6D7B: 02         LD      (BC),A          
6D7C: 02         LD      (BC),A          
6D7D: 03         INC     BC              
6D7E: 03         INC     BC              
6D7F: 03         INC     BC              
6D80: 03         INC     BC              
6D81: 03         INC     BC              
6D82: 03         INC     BC              
6D83: 03         INC     BC              
6D84: 84         ADD     A,H             
6D85: 68         LD      L,B             
6D86: C4 68 04   CALL    NZ,$0468        
6D89: 69         LD      L,C             
6D8A: 84         ADD     A,H             
6D8B: 69         LD      L,C             
6D8C: 04         INC     B               
6D8D: 6A         LD      L,D             
6D8E: 44         LD      B,H             
6D8F: 6A         LD      L,D             
6D90: C4 6A 04   CALL    NZ,$046A        
6D93: 6B         LD      L,E             
6D94: 44         LD      B,H             
6D95: 6B         LD      L,E             
6D96: C4 6B 04   CALL    NZ,$046B        
6D99: 6C         LD      L,H             
6D9A: 44         LD      B,H             
6D9B: 6C         LD      L,H             
6D9C: 84         ADD     A,H             
6D9D: 6C         LD      L,H             
6D9E: C4 6C 04   CALL    NZ,$046C        
6DA1: 6D         LD      L,L             
6DA2: 44         LD      B,H             
6DA3: 6D         LD      L,L             
6DA4: 44         LD      B,H             
6DA5: 68         LD      L,B             
6DA6: 28 2A      JR      Z,$6DD2         
6DA8: 2C         INC     L               
6DA9: 2C         INC     L               
6DAA: 2E 2E      LD      L,$2E           
6DAC: 30 30      JR      NC,$6DDE        
6DAE: 31 33 33   LD      SP,$3333        
6DB1: 34         INC     (HL)            
6DB2: 35         DEC     (HL)            
6DB3: 36 38      LD      (HL),$38        
6DB5: 3A         LD      A,(HLD)         
6DB6: 3A         LD      A,(HLD)         
6DB7: 21 7C C1   LD      HL,$C17C        
6DBA: AF         XOR     A               
6DBB: 22         LD      (HLI),A         
6DBC: 22         LD      (HLI),A         
6DBD: 16 00      LD      D,$00           
6DBF: F0 E7      LD      A,($E7)         
6DC1: E6 01      AND     $01             
6DC3: 20 0D      JR      NZ,$6DD2        
6DC5: FA 7E C1   LD      A,($C17E)       
6DC8: 3C         INC     A               
6DC9: FE 10      CP      $10             
6DCB: 38 02      JR      C,$6DCF         
6DCD: 3E 10      LD      A,$10           
6DCF: EA 7E C1   LD      ($C17E),A       
6DD2: FA 7E C1   LD      A,($C17E)       
6DD5: 5F         LD      E,A             
6DD6: 21 A6 6D   LD      HL,$6DA6        
6DD9: 19         ADD     HL,DE           
6DDA: 7E         LD      A,(HL)          
6DDB: E0 D7      LDFF00  ($D7),A         
6DDD: CB 23      SET     1,E             
6DDF: 21 84 6D   LD      HL,$6D84        
6DE2: 19         ADD     HL,DE           
6DE3: 2A         LD      A,(HLI)         
6DE4: 46         LD      B,(HL)          
6DE5: 4F         LD      C,A             
6DE6: F0 44      LD      A,($44)         
6DE8: FE 10      CP      $10             
6DEA: 20 FA      JR      NZ,$6DE6        
6DEC: F0 41      LD      A,($41)         
6DEE: E6 03      AND     $03             
6DF0: 20 FA      JR      NZ,$6DEC        
6DF2: FA 7D C1   LD      A,($C17D)       
6DF5: 3C         INC     A               
6DF6: EA 7D C1   LD      ($C17D),A       
6DF9: E6 01      AND     $01             
6DFB: 20 F5      JR      NZ,$6DF2        
6DFD: F0 D7      LD      A,($D7)         
6DFF: 6F         LD      L,A             
6E00: FA 7C C1   LD      A,($C17C)       
6E03: 5F         LD      E,A             
6E04: 3C         INC     A               
6E05: EA 7C C1   LD      ($C17C),A       
6E08: FE 3A      CP      $3A             
6E0A: 28 17      JR      Z,$6E23         
6E0C: BD         CP      L               
6E0D: 38 06      JR      C,$6E15         
6E0F: 3E 55      LD      A,$55           
6E11: E0 47      LDFF00  ($47),A         
6E13: 18 D7      JR      $6DEC           
6E15: 21 00 00   LD      HL,$0000        
6E18: 19         ADD     HL,DE           
6E19: 09         ADD     HL,BC           
6E1A: 7E         LD      A,(HL)          
6E1B: 21 97 FF   LD      HL,$FF97        
6E1E: 86         ADD     A,(HL)          
6E1F: E0 42      LDFF00  ($42),A         
6E21: 18 C9      JR      $6DEC           
6E23: F0 97      LD      A,($97)         
6E25: E0 42      LDFF00  ($42),A         
6E27: FA 97 DB   LD      A,($DB97)       
6E2A: E0 47      LDFF00  ($47),A         
6E2C: C9         RET                     
6E2D: F0 CC      LD      A,($CC)         
6E2F: E6 4C      AND     $4C             
6E31: 28 06      JR      Z,$6E39         
6E33: F5         PUSH    AF              
6E34: 3E 0A      LD      A,$0A           
6E36: E0 F2      LDFF00  ($F2),A         
6E38: F1         POP     AF              
6E39: C9         RET                     
6E3A: C6 C2      ADD     $C2             
6E3C: C0         RET     NZ              
6E3D: C2 F0 B5   JP      NZ,$B5F0        
6E40: A7         AND     A               
6E41: 28 05      JR      Z,$6E48         
6E43: 3D         DEC     A               
6E44: E0 B5      LDFF00  ($B5),A         
6E46: 18 65      JR      $6EAD           
6E48: F0 CC      LD      A,($CC)         
6E4A: E6 80      AND     $80             
6E4C: 28 5F      JR      Z,$6EAD         
6E4E: CD D2 27   CALL    $27D2           
6E51: FA 96 DB   LD      A,($DB96)       
6E54: FE 0B      CP      $0B             
6E56: 28 38      JR      Z,$6E90         
6E58: 3E 28      LD      A,$28           
6E5A: E0 B5      LDFF00  ($B5),A         
6E5C: 3E 11      LD      A,$11           
6E5E: EA FF D6   LD      ($D6FF),A       
6E61: 3E 0D      LD      A,$0D           
6E63: EA 96 DB   LD      ($DB96),A       
6E66: AF         XOR     A               
6E67: EA 80 C2   LD      ($C280),A       
6E6A: EA 81 C2   LD      ($C281),A       
6E6D: EA 82 C2   LD      ($C282),A       
6E70: EA 83 C2   LD      ($C283),A       
6E73: EA 84 C2   LD      ($C284),A       
6E76: E0 47      LDFF00  ($47),A         
6E78: EA 97 DB   LD      ($DB97),A       
6E7B: 3E 10      LD      A,$10           
6E7D: EA 7E C1   LD      ($C17E),A       
6E80: CD 7D 72   CALL    $727D           
6E83: 3E 0D      LD      A,$0D           
6E85: EA 68 D3   LD      ($D368),A       
6E88: EA 0F D0   LD      ($D00F),A       
6E8B: CD 11 7B   CALL    $7B11           
6E8E: 18 14      JR      $6EA4           
6E90: C3 BC 44   JP      $44BC           
6E93: AF         XOR     A               
6E94: EA 96 DB   LD      ($DB96),A       
6E97: E0 96      LDFF00  ($96),A         
6E99: E0 97      LDFF00  ($97),A         
6E9B: E0 47      LDFF00  ($47),A         
6E9D: EA 97 DB   LD      ($DB97),A       
6EA0: 21 95 DB   LD      HL,$DB95        
6EA3: 34         INC     (HL)            
6EA4: 3E 01      LD      A,$01           
6EA6: E0 FF      LDFF00  ($FF),A         
6EA8: 3E 4F      LD      A,$4F           
6EAA: E0 45      LDFF00  ($45),A         
6EAC: C9         RET                     
6EAD: FA 96 DB   LD      A,($DB96)       
6EB0: FE 05      CP      $05             
6EB2: 30 19      JR      NC,$6ECD        
6EB4: FA 00 D0   LD      A,($D000)       
6EB7: A7         AND     A               
6EB8: 28 04      JR      Z,$6EBE         
6EBA: 3D         DEC     A               
6EBB: EA 00 D0   LD      ($D000),A       
6EBE: 1F         RRA                     
6EBF: 00         NOP                     
6EC0: E6 03      AND     $03             
6EC2: 5F         LD      E,A             
6EC3: 16 00      LD      D,$00           
6EC5: 21 3A 6E   LD      HL,$6E3A        
6EC8: 19         ADD     HL,DE           
6EC9: 7E         LD      A,(HL)          
6ECA: EA 97 DB   LD      ($DB97),A       
6ECD: FA 96 DB   LD      A,($DB96)       
6ED0: C7         RST     0X00            
6ED1: ED                              
6ED2: 6E         LD      L,(HL)          
6ED3: 11 6F 19   LD      DE,$196F        
6ED6: 6F         LD      L,A             
6ED7: 84         ADD     A,H             
6ED8: 6F         LD      L,A             
6ED9: 8A         ADC     A,D             
6EDA: 70         LD      (HL),B          
6EDB: D4 70 0D   CALL    NC,$0D70        
6EDE: 71         LD      (HL),C          
6EDF: 75         LD      (HL),L          
6EE0: 71         LD      (HL),C          
6EE1: 24         INC     H               
6EE2: 72         LD      (HL),D          
6EE3: 4F         LD      C,A             
6EE4: 72         LD      (HL),D          
6EE5: 6C         LD      L,H             
6EE6: 72         LD      (HL),D          
6EE7: 9C         SBC     H               
6EE8: 72         LD      (HL),D          
6EE9: 03         INC     BC              
6EEA: 73         LD      (HL),E          
6EEB: 11 73 CD   LD      DE,$CD73        
6EEE: 7B         LD      A,E             
6EEF: 29         ADD     HL,HL           
6EF0: CD D2 27   CALL    $27D2           
6EF3: 3E 1A      LD      A,$1A           
6EF5: CD A8 27   CALL    $27A8           
6EF8: 3E 02      LD      A,$02           
6EFA: EA FE D6   LD      ($D6FE),A       
6EFD: AF         XOR     A               
6EFE: E0 E7      LDFF00  ($E7),A         
6F00: 3E A2      LD      A,$A2           
6F02: EA 3D C1   LD      ($C13D),A       
6F05: F0 40      LD      A,($40)         
6F07: E6 DF      AND     $DF             
6F09: EA FD D6   LD      ($D6FD),A       
6F0C: E0 40      LDFF00  ($40),A         
6F0E: C3 45 44   JP      $4445           
6F11: 3E 10      LD      A,$10           
6F13: EA FE D6   LD      ($D6FE),A       
6F16: C3 45 44   JP      $4445           
6F19: CD C4 7A   CALL    $7AC4           
6F1C: 3E 0E      LD      A,$0E           
6F1E: EA FF D6   LD      ($D6FF),A       
6F21: 3E C6      LD      A,$C6           
6F23: EA 97 DB   LD      ($DB97),A       
6F26: 3E 1C      LD      A,$1C           
6F28: EA 98 DB   LD      ($DB98),A       
6F2B: 3E E0      LD      A,$E0           
6F2D: EA 99 DB   LD      ($DB99),A       
6F30: 3E 03      LD      A,$03           
6F32: E0 FF      LDFF00  ($FF),A         
6F34: 3E 00      LD      A,$00           
6F36: E0 45      LDFF00  ($45),A         
6F38: 1E 11      LD      E,$11           
6F3A: 21 00 D0   LD      HL,$D000        
6F3D: AF         XOR     A               
6F3E: 22         LD      (HLI),A         
6F3F: 1D         DEC     E               
6F40: 20 FC      JR      NZ,$6F3E        
6F42: EA 80 C2   LD      ($C280),A       
6F45: EA 81 C2   LD      ($C281),A       
6F48: EA B0 C3   LD      ($C3B0),A       
6F4B: EA B1 C3   LD      ($C3B1),A       
6F4E: EA B2 C3   LD      ($C3B2),A       
6F51: E0 ED      LDFF00  ($ED),A         
6F53: 3E 05      LD      A,$05           
6F55: EA 82 C2   LD      ($C282),A       
6F58: 3E C0      LD      A,$C0           
6F5A: EA 02 C2   LD      ($C202),A       
6F5D: 3E 4E      LD      A,$4E           
6F5F: EA 12 C2   LD      ($C212),A       
6F62: AF         XOR     A               
6F63: EA 40 C3   LD      ($C340),A       
6F66: EA 41 C3   LD      ($C341),A       
6F69: EA 42 C3   LD      ($C342),A       
6F6C: EA 43 C3   LD      ($C343),A       
6F6F: C3 45 44   JP      $4445           
6F72: 81         ADD     A,C             
6F73: 40         LD      B,B             
6F74: 00         NOP                     
6F75: 00         NOP                     
6F76: 00         NOP                     
6F77: 00         NOP                     
6F78: 00         NOP                     
6F79: 00         NOP                     
6F7A: 00         NOP                     
6F7B: 08 08 08   LD      ($0808),SP      
6F7E: 04         INC     B               
6F7F: 00         NOP                     
6F80: 00         NOP                     
6F81: 00         NOP                     
6F82: 00         NOP                     
6F83: 00         NOP                     
6F84: CD 2B 73   CALL    $732B           
6F87: CD 9B 73   CALL    $739B           
6F8A: FA 02 D0   LD      A,($D002)       
6F8D: A7         AND     A               
6F8E: 28 60      JR      Z,$6FF0         
6F90: 3C         INC     A               
6F91: EA 02 D0   LD      ($D002),A       
6F94: FE 18      CP      $18             
6F96: 38 57      JR      C,$6FEF         
6F98: D6 18      SUB     $18             
6F9A: 1F         RRA                     
6F9B: 1F         RRA                     
6F9C: 1F         RRA                     
6F9D: E6 0F      AND     $0F             
6F9F: 5F         LD      E,A             
6FA0: 16 00      LD      D,$00           
6FA2: 21 72 6F   LD      HL,$6F72        
6FA5: 19         ADD     HL,DE           
6FA6: 7E         LD      A,(HL)          
6FA7: EA 97 DB   LD      ($DB97),A       
6FAA: 21 7B 6F   LD      HL,$6F7B        
6FAD: 19         ADD     HL,DE           
6FAE: 7E         LD      A,(HL)          
6FAF: EA 98 DB   LD      ($DB98),A       
6FB2: 7B         LD      A,E             
6FB3: FE 08      CP      $08             
6FB5: C2 EF 6F   JP      NZ,$6FEF        
6FB8: AF         XOR     A               
6FB9: EA 80 C2   LD      ($C280),A       
6FBC: EA 81 C2   LD      ($C281),A       
6FBF: EA 82 C2   LD      ($C282),A       
6FC2: EA 90 C2   LD      ($C290),A       
6FC5: 3E 05      LD      A,$05           
6FC7: EA 96 DB   LD      ($DB96),A       
6FCA: EA 0F D0   LD      ($D00F),A       
6FCD: CD 11 7B   CALL    $7B11           
6FD0: 3E 11      LD      A,$11           
6FD2: EA FE D6   LD      ($D6FE),A       
6FD5: 3E FF      LD      A,$FF           
6FD7: EA 01 D0   LD      ($D001),A       
6FDA: AF         XOR     A               
6FDB: E0 96      LDFF00  ($96),A         
6FDD: EA 00 C1   LD      ($C100),A       
6FE0: EA 02 C1   LD      ($C102),A       
6FE3: EA 03 C1   LD      ($C103),A       
6FE6: 3E 92      LD      A,$92           
6FE8: EA 01 C1   LD      ($C101),A       
6FEB: 3E 03      LD      A,$03           
6FED: E0 FF      LDFF00  ($FF),A         
6FEF: C9         RET                     
6FF0: FA 02 C2   LD      A,($C202)       
6FF3: FE 50      CP      $50             
6FF5: 20 12      JR      NZ,$7009        
6FF7: 3E 04      LD      A,$04           
6FF9: EA 96 DB   LD      ($DB96),A       
6FFC: 3E 0F      LD      A,$0F           
6FFE: EA FF D6   LD      ($D6FF),A       
7001: 3E 01      LD      A,$01           
7003: E0 FF      LDFF00  ($FF),A         
7005: AF         XOR     A               
7006: E0 96      LDFF00  ($96),A         
7008: C9         RET                     
7009: CD C4 7A   CALL    $7AC4           
700C: F0 E7      LD      A,($E7)         
700E: E6 07      AND     $07             
7010: C2 89 70   JP      NZ,$7089        
7013: 21 96 FF   LD      HL,$FF96        
7016: 34         INC     (HL)            
7017: 21 00 C2   LD      HL,$C200        
701A: 35         DEC     (HL)            
701B: 23         INC     HL              
701C: 35         DEC     (HL)            
701D: 23         INC     HL              
701E: 35         DEC     (HL)            
701F: 0E 00      LD      C,$00           
7021: F0 96      LD      A,($96)         
7023: FE 10      CP      $10             
7025: 28 19      JR      Z,$7040         
7027: 0C         INC     C               
7028: FE 30      CP      $30             
702A: 28 14      JR      Z,$7040         
702C: 0C         INC     C               
702D: FE 38      CP      $38             
702F: 28 0F      JR      Z,$7040         
7031: 0C         INC     C               
7032: FE 58      CP      $58             
7034: 28 0A      JR      Z,$7040         
7036: 0C         INC     C               
7037: FE 5A      CP      $5A             
7039: 28 05      JR      Z,$7040         
703B: 0C         INC     C               
703C: FE 69      CP      $69             
703E: 20 49      JR      NZ,$7089        
7040: 1E 01      LD      E,$01           
7042: 16 00      LD      D,$00           
7044: 21 80 C2   LD      HL,$C280        
7047: 19         ADD     HL,DE           
7048: 7E         LD      A,(HL)          
7049: A7         AND     A               
704A: 28 13      JR      Z,$705F         
704C: 1D         DEC     E               
704D: 7B         LD      A,E             
704E: FE FF      CP      $FF             
7050: 20 F2      JR      NZ,$7044        
7052: C9         RET                     
7053: 28 78      JR      Z,$70CD         
7055: 60         LD      H,B             
7056: 38 68      JR      C,$70C0         
7058: 58         LD      E,B             
7059: 04         INC     B               
705A: 02         LD      (BC),A          
705B: 01 04 03   LD      BC,$0304        
705E: 01 06 00   LD      BC,$0006        
7061: 21 59 70   LD      HL,$7059        
7064: 09         ADD     HL,BC           
7065: 7E         LD      A,(HL)          
7066: 21 80 C2   LD      HL,$C280        
7069: 19         ADD     HL,DE           
706A: 77         LD      (HL),A          
706B: 21 53 70   LD      HL,$7053        
706E: 09         ADD     HL,BC           
706F: 7E         LD      A,(HL)          
7070: 21 00 C2   LD      HL,$C200        
7073: 19         ADD     HL,DE           
7074: 77         LD      (HL),A          
7075: 21 10 C2   LD      HL,$C210        
7078: 19         ADD     HL,DE           
7079: 36 30      LD      (HL),$30        
707B: 21 E0 C2   LD      HL,$C2E0        
707E: 19         ADD     HL,DE           
707F: 36 20      LD      (HL),$20        
7081: 3E 1C      LD      A,$1C           
7083: EA 00 D0   LD      ($D000),A       
7086: CD D7 08   CALL    $08D7           
7089: C9         RET                     
708A: CD 2B 73   CALL    $732B           
708D: FA 01 D0   LD      A,($D001)       
7090: 3C         INC     A               
7091: EA 01 D0   LD      ($D001),A       
7094: FE 80      CP      $80             
7096: 20 05      JR      NZ,$709D        
7098: F5         PUSH    AF              
7099: CD 8C 73   CALL    $738C           
709C: F1         POP     AF              
709D: FE 90      CP      $90             
709F: 20 03      JR      NZ,$70A4        
70A1: CD 81 70   CALL    $7081           
70A4: FE A0      CP      $A0             
70A6: 20 1B      JR      NZ,$70C3        
70A8: 3E 03      LD      A,$03           
70AA: EA 96 DB   LD      ($DB96),A       
70AD: 3E 0E      LD      A,$0E           
70AF: EA FF D6   LD      ($D6FF),A       
70B2: 3E 03      LD      A,$03           
70B4: E0 FF      LDFF00  ($FF),A         
70B6: AF         XOR     A               
70B7: EA 80 C2   LD      ($C280),A       
70BA: EA 81 C2   LD      ($C281),A       
70BD: 3E 01      LD      A,$01           
70BF: EA 02 D0   LD      ($D002),A       
70C2: C9         RET                     
70C3: F0 E7      LD      A,($E7)         
70C5: E6 7F      AND     $7F             
70C7: 20 0A      JR      NZ,$70D3        
70C9: CD ED 27   CALL    $27ED           
70CC: E6 00      AND     $00             
70CE: 20 03      JR      NZ,$70D3        
70D0: CD 81 70   CALL    $7081           
70D3: C9         RET                     
70D4: 3E 10      LD      A,$10           
70D6: EA FF D6   LD      ($D6FF),A       
70D9: CD 45 44   CALL    $4445           
70DC: C9         RET                     
70DD: 00         NOP                     
70DE: 00         NOP                     
70DF: 00         NOP                     
70E0: 00         NOP                     
70E1: 40         LD      B,B             
70E2: 40         LD      B,B             
70E3: 40         LD      B,B             
70E4: 80         ADD     A,B             
70E5: 85         ADD     A,L             
70E6: 85         ADD     A,L             
70E7: 85         ADD     A,L             
70E8: C5         PUSH    BC              
70E9: C9         RET                     
70EA: C9         RET                     
70EB: C9         RET                     
70EC: C9         RET                     
70ED: 00         NOP                     
70EE: 00         NOP                     
70EF: 00         NOP                     
70F0: 00         NOP                     
70F1: 04         INC     B               
70F2: 04         INC     B               
70F3: 04         INC     B               
70F4: 04         INC     B               
70F5: 18 18      JR      $710F           
70F7: 18 18      JR      $7111           
70F9: 1C         INC     E               
70FA: 1C         INC     E               
70FB: 1C         INC     E               
70FC: 1C         INC     E               
70FD: 00         NOP                     
70FE: 00         NOP                     
70FF: 00         NOP                     
7100: 00         NOP                     
7101: 40         LD      B,B             
7102: 40         LD      B,B             
7103: 40         LD      B,B             
7104: 40         LD      B,B             
7105: 90         SUB     B               
7106: 90         SUB     B               
7107: 90         SUB     B               
7108: 90         SUB     B               
7109: E0 E0      LDFF00  ($E0),A         
710B: E0 E0      LDFF00  ($E0),A         
710D: CD 79 71   CALL    $7179           
7110: FA 01 D0   LD      A,($D001)       
7113: FE A0      CP      $A0             
7115: 20 06      JR      NZ,$711D        
7117: F5         PUSH    AF              
7118: 3E 02      LD      A,$02           
711A: E0 45      LDFF00  ($45),A         
711C: F1         POP     AF              
711D: 3D         DEC     A               
711E: EA 01 D0   LD      ($D001),A       
7121: 20 1A      JR      NZ,$713D        
7123: 3E 07      LD      A,$07           
7125: EA 96 DB   LD      ($DB96),A       
7128: 3E 06      LD      A,$06           
712A: EA 80 C2   LD      ($C280),A       
712D: 3E B0      LD      A,$B0           
712F: EA 00 C2   LD      ($C200),A       
7132: 3E 68      LD      A,$68           
7134: EA 10 C2   LD      ($C210),A       
7137: 3E 01      LD      A,$01           
7139: EA D0 C3   LD      ($C3D0),A       
713C: C9         RET                     
713D: FE 34      CP      $34             
713F: 30 33      JR      NC,$7174        
7141: E6 03      AND     $03             
7143: 20 0B      JR      NZ,$7150        
7145: FA 10 D0   LD      A,($D010)       
7148: FE 0C      CP      $0C             
714A: 28 04      JR      Z,$7150         
714C: 3C         INC     A               
714D: EA 10 D0   LD      ($D010),A       
7150: F0 E7      LD      A,($E7)         
7152: E6 03      AND     $03             
7154: 5F         LD      E,A             
7155: FA 10 D0   LD      A,($D010)       
7158: 83         ADD     A,E             
7159: 5F         LD      E,A             
715A: 16 00      LD      D,$00           
715C: 21 DD 70   LD      HL,$70DD        
715F: 19         ADD     HL,DE           
7160: 7E         LD      A,(HL)          
7161: EA 97 DB   LD      ($DB97),A       
7164: 21 ED 70   LD      HL,$70ED        
7167: 19         ADD     HL,DE           
7168: 7E         LD      A,(HL)          
7169: EA 98 DB   LD      ($DB98),A       
716C: 21 FD 70   LD      HL,$70FD        
716F: 19         ADD     HL,DE           
7170: 7E         LD      A,(HL)          
7171: EA 99 DB   LD      ($DB99),A       
7174: C9         RET                     
7175: CD 9B 73   CALL    $739B           
7178: C9         RET                     
7179: FA 91 C2   LD      A,($C291)       
717C: FE 02      CP      $02             
717E: 30 10      JR      NC,$7190        
7180: FA 14 C1   LD      A,($C114)       
7183: 3C         INC     A               
7184: FE A0      CP      $A0             
7186: 20 05      JR      NZ,$718D        
7188: 3E 0F      LD      A,$0F           
718A: E0 F4      LDFF00  ($F4),A         
718C: AF         XOR     A               
718D: EA 14 C1   LD      ($C114),A       
7190: C9         RET                     
7191: 9A         SBC     D               
7192: 16 0F      LD      D,$0F           
7194: 80         ADD     A,B             
7195: 81         ADD     A,C             
7196: 82         ADD     A,D             
7197: 83         ADD     A,E             
7198: 84         ADD     A,H             
7199: 85         ADD     A,L             
719A: 86         ADD     A,(HL)          
719B: 87         ADD     A,A             
719C: 88         ADC     A,B             
719D: 89         ADC     A,C             
719E: 8A         ADC     A,D             
719F: 8B         ADC     A,E             
71A0: 8C         ADC     A,H             
71A1: 8D         ADC     A,L             
71A2: 8E         ADC     A,(HL)          
71A3: 8F         ADC     A,A             
71A4: 9A         SBC     D               
71A5: 36 0F      LD      (HL),$0F        
71A7: 90         SUB     B               
71A8: 91         SUB     C               
71A9: 92         SUB     D               
71AA: 93         SUB     E               
71AB: 94         SUB     H               
71AC: 95         SUB     L               
71AD: 96         SUB     (HL)            
71AE: 97         SUB     A               
71AF: 98         SBC     B               
71B0: 99         SBC     C               
71B1: 9A         SBC     D               
71B2: 9B         SBC     E               
71B3: 9C         SBC     H               
71B4: 9D         SBC     L               
71B5: 9E         SBC     (HL)            
71B6: 9F         SBC     A               
71B7: 9A         SBC     D               
71B8: 56         LD      D,(HL)          
71B9: 0F         RRCA                    
71BA: A0         AND     B               
71BB: A1         AND     C               
71BC: A2         AND     D               
71BD: A3         AND     E               
71BE: A4         AND     H               
71BF: A5         AND     L               
71C0: A6         AND     (HL)            
71C1: A7         AND     A               
71C2: A8         XOR     B               
71C3: A9         XOR     C               
71C4: AA         XOR     D               
71C5: AB         XOR     E               
71C6: AC         XOR     H               
71C7: AD         XOR     L               
71C8: AE         XOR     (HL)            
71C9: AF         XOR     A               
71CA: 9A         SBC     D               
71CB: 76         HALT                    
71CC: 0F         RRCA                    
71CD: B0         OR      B               
71CE: B1         OR      C               
71CF: B2         OR      D               
71D0: B3         OR      E               
71D1: B4         OR      H               
71D2: B5         OR      L               
71D3: B6         OR      (HL)            
71D4: B7         OR      A               
71D5: B8         CP      B               
71D6: B9         CP      C               
71D7: BA         CP      D               
71D8: BB         CP      E               
71D9: BC         CP      H               
71DA: BD         CP      L               
71DB: BE         CP      (HL)            
71DC: BF         CP      A               
71DD: 9A         SBC     D               
71DE: 96         SUB     (HL)            
71DF: 0F         RRCA                    
71E0: C0         RET     NZ              
71E1: C1         POP     BC              
71E2: C2 C3 C4   JP      NZ,$C4C3        
71E5: C5         PUSH    BC              
71E6: C6 C7      ADD     $C7             
71E8: C8         RET     Z               
71E9: C9         RET                     
71EA: CA CB CC   JP      Z,$CCCB         
71ED: CD CE CF   CALL    $CFCE           
71F0: 9A         SBC     D               
71F1: B6         OR      (HL)            
71F2: 0F         RRCA                    
71F3: D0         RET     NC              
71F4: D1         POP     DE              
71F5: D2 D3 D4   JP      NC,$D4D3        
71F8: D5         PUSH    DE              
71F9: D6 D7      SUB     $D7             
71FB: D8         RET     C               
71FC: D9         RETI                    
71FD: DA DB DC   JP      C,$DCDB         
7200: DD                              
7201: DE DF      SBC     $DF             
7203: 9A         SBC     D               
7204: D6 0F      SUB     $0F             
7206: E0 E1      LDFF00  ($E1),A         
7208: E2         LDFF00  (C),A           
7209: E3                              
720A: E4                              
720B: E5         PUSH    HL              
720C: E6 E7      AND     $E7             
720E: E8 E9      ADD     SP,$E9          
7210: EA EB EC   LD      ($ECEB),A       
7213: ED                              
7214: EE EF      XOR     $EF             
7216: CA 71 B7   JP      Z,$B771         
7219: 71         LD      (HL),C          
721A: DD                              
721B: 71         LD      (HL),C          
721C: A4         AND     H               
721D: 71         LD      (HL),C          
721E: F0 71      LD      A,($71)         
7220: 91         SUB     C               
7221: 71         LD      (HL),C          
7222: 03         INC     BC              
7223: 72         LD      (HL),D          
7224: FA 02 D0   LD      A,($D002)       
7227: CB 27      SET     1,E             
7229: 5F         LD      E,A             
722A: 16 00      LD      D,$00           
722C: 21 16 72   LD      HL,$7216        
722F: 19         ADD     HL,DE           
7230: 2A         LD      A,(HLI)         
7231: 56         LD      D,(HL)          
7232: 5F         LD      E,A             
7233: 21 01 D6   LD      HL,$D601        
7236: 0E 13      LD      C,$13           
7238: 1A         LD      A,(DE)          
7239: 13         INC     DE              
723A: 22         LD      (HLI),A         
723B: 0D         DEC     C               
723C: 20 FA      JR      NZ,$7238        
723E: 36 00      LD      (HL),$00        
7240: FA 02 D0   LD      A,($D002)       
7243: 3C         INC     A               
7244: EA 02 D0   LD      ($D002),A       
7247: FE 07      CP      $07             
7249: 20 03      JR      NZ,$724E        
724B: CD 45 44   CALL    $4445           
724E: C9         RET                     
724F: FA 7E C1   LD      A,($C17E)       
7252: FE 10      CP      $10             
7254: 38 07      JR      C,$725D         
7256: 3E 19      LD      A,$19           
7258: E0 F4      LDFF00  ($F4),A         
725A: CD 45 44   CALL    $4445           
725D: C9         RET                     
725E: 9B         SBC     E               
725F: B9         CP      C               
7260: 09         ADD     HL,BC           
7261: 65         LD      H,L             
7262: 66         LD      H,(HL)          
7263: 67         LD      H,A             
7264: 68         LD      L,B             
7265: 69         LD      L,C             
7266: 6A         LD      L,D             
7267: 6B         LD      L,E             
7268: 6C         LD      L,H             
7269: 6D         LD      L,L             
726A: 6E         LD      L,(HL)          
726B: 00         NOP                     
726C: 11 5E 72   LD      DE,$725E        
726F: 21 01 D6   LD      HL,$D601        
7272: 0E 0E      LD      C,$0E           
7274: 1A         LD      A,(DE)          
7275: 13         INC     DE              
7276: 22         LD      (HLI),A         
7277: 0D         DEC     C               
7278: 20 FA      JR      NZ,$7274        
727A: CD 45 44   CALL    $4445           
727D: 3E A0      LD      A,$A0           
727F: EA 01 D0   LD      ($D001),A       
7282: AF         XOR     A               
7283: EA 02 D0   LD      ($D002),A       
7286: 3E FF      LD      A,$FF           
7288: EA 03 D0   LD      ($D003),A       
728B: C9         RET                     
728C: 18 18      JR      $72A6           
728E: 38 40      JR      C,$72D0         
7290: 58         LD      E,B             
7291: 60         LD      H,B             
7292: 80         ADD     A,B             
7293: 88         ADC     A,B             
7294: 20 48      JR      NZ,$72DE        
7296: 44         LD      B,H             
7297: 28 44      JR      Z,$72DD         
7299: 28 28      JR      Z,$72C3         
729B: 40         LD      B,B             
729C: CD 9B 73   CALL    $739B           
729F: F0 E7      LD      A,($E7)         
72A1: E6 3F      AND     $3F             
72A3: 20 3C      JR      NZ,$72E1        
72A5: 1E 01      LD      E,$01           
72A7: 16 00      LD      D,$00           
72A9: 21 80 C2   LD      HL,$C280        
72AC: 19         ADD     HL,DE           
72AD: 7E         LD      A,(HL)          
72AE: A7         AND     A               
72AF: 28 08      JR      Z,$72B9         
72B1: 1D         DEC     E               
72B2: 7B         LD      A,E             
72B3: FE FF      CP      $FF             
72B5: 20 F2      JR      NZ,$72A9        
72B7: 18 28      JR      $72E1           
72B9: 36 08      LD      (HL),$08        
72BB: 21 E0 C2   LD      HL,$C2E0        
72BE: 19         ADD     HL,DE           
72BF: 36 3F      LD      (HL),$3F        
72C1: FA 03 D0   LD      A,($D003)       
72C4: 3C         INC     A               
72C5: EA 03 D0   LD      ($D003),A       
72C8: E6 07      AND     $07             
72CA: 4F         LD      C,A             
72CB: 06 00      LD      B,$00           
72CD: 21 8C 72   LD      HL,$728C        
72D0: 09         ADD     HL,BC           
72D1: 7E         LD      A,(HL)          
72D2: 21 00 C2   LD      HL,$C200        
72D5: 19         ADD     HL,DE           
72D6: 77         LD      (HL),A          
72D7: 21 94 72   LD      HL,$7294        
72DA: 09         ADD     HL,BC           
72DB: 7E         LD      A,(HL)          
72DC: 21 10 C2   LD      HL,$C210        
72DF: 19         ADD     HL,DE           
72E0: 77         LD      (HL),A          
72E1: FA 02 D0   LD      A,($D002)       
72E4: 3C         INC     A               
72E5: EA 02 D0   LD      ($D002),A       
72E8: E6 0F      AND     $0F             
72EA: 20 16      JR      NZ,$7302        
72EC: FA 01 D0   LD      A,($D001)       
72EF: 3D         DEC     A               
72F0: EA 01 D0   LD      ($D001),A       
72F3: 20 0D      JR      NZ,$7302        
72F5: CD 45 44   CALL    $4445           
72F8: AF         XOR     A               
72F9: EA 6B C1   LD      ($C16B),A       
72FC: EA 6C C1   LD      ($C16C),A       
72FF: CD CA 27   CALL    $27CA           
7302: C9         RET                     
7303: CD 76 17   CALL    $1776           
7306: FA 6B C1   LD      A,($C16B)       
7309: FE 04      CP      $04             
730B: 20 03      JR      NZ,$7310        
730D: C3 1A 5F   JP      $5F1A           
7310: C9         RET                     
7311: 3E 11      LD      A,$11           
7313: EA FE D6   LD      ($D6FE),A       
7316: 3E 0B      LD      A,$0B           
7318: EA 96 DB   LD      ($DB96),A       
731B: 3E C9      LD      A,$C9           
731D: EA 97 DB   LD      ($DB97),A       
7320: 3E 1C      LD      A,$1C           
7322: EA 98 DB   LD      ($DB98),A       
7325: AF         XOR     A               
7326: E0 96      LDFF00  ($96),A         
7328: E0 97      LDFF00  ($97),A         
732A: C9         RET                     
732B: CD ED 27   CALL    $27ED           
732E: E6 18      AND     $18             
7330: C6 10      ADD     $10             
7332: E0 D8      LDFF00  ($D8),A         
7334: CD ED 27   CALL    $27ED           
7337: E6 18      AND     $18             
7339: C6 10      ADD     $10             
733B: E0 D7      LDFF00  ($D7),A         
733D: 21 4C C0   LD      HL,$C04C        
7340: 0E 10      LD      C,$10           
7342: FA 96 DB   LD      A,($DB96)       
7345: FE 04      CP      $04             
7347: 20 02      JR      NZ,$734B        
7349: 0E 15      LD      C,$15           
734B: F0 D8      LD      A,($D8)         
734D: 22         LD      (HLI),A         
734E: F0 D7      LD      A,($D7)         
7350: 22         LD      (HLI),A         
7351: CD ED 27   CALL    $27ED           
7354: E6 01      AND     $01             
7356: 3E 28      LD      A,$28           
7358: 28 07      JR      Z,$7361         
735A: CD ED 27   CALL    $27ED           
735D: E6 06      AND     $06             
735F: C6 70      ADD     $70             
7361: 22         LD      (HLI),A         
7362: 3E 00      LD      A,$00           
7364: 22         LD      (HLI),A         
7365: F0 D7      LD      A,($D7)         
7367: C6 1C      ADD     $1C             
7369: E0 D7      LDFF00  ($D7),A         
736B: FE A0      CP      $A0             
736D: 38 0A      JR      C,$7379         
736F: D6 98      SUB     $98             
7371: E0 D7      LDFF00  ($D7),A         
7373: F0 D8      LD      A,($D8)         
7375: C6 25      ADD     $25             
7377: E0 D8      LDFF00  ($D8),A         
7379: 0D         DEC     C               
737A: 20 CF      JR      NZ,$734B        
737C: C9         RET                     
737D: 99         SBC     C               
737E: 2B         DEC     HL              
737F: 83         ADD     A,E             
7380: 1E 20      LD      E,$20           
7382: 22         LD      (HLI),A         
7383: 24         INC     H               
7384: 99         SBC     C               
7385: 2C         INC     L               
7386: 83         ADD     A,E             
7387: 1F         RRA                     
7388: 21 23 25   LD      HL,$2523        
738B: 00         NOP                     
738C: 11 01 D6   LD      DE,$D601        
738F: 21 7D 73   LD      HL,$737D        
7392: 0E 0F      LD      C,$0F           
7394: 2A         LD      A,(HLI)         
7395: 12         LD      (DE),A          
7396: 13         INC     DE              
7397: 0D         DEC     C               
7398: 20 FA      JR      NZ,$7394        
739A: C9         RET                     
739B: AF         XOR     A               
739C: EA C0 C3   LD      ($C3C0),A       
739F: 0E 02      LD      C,$02           
73A1: 06 00      LD      B,$00           
73A3: 79         LD      A,C             
73A4: EA 23 C1   LD      ($C123),A       
73A7: 21 80 C2   LD      HL,$C280        
73AA: 09         ADD     HL,BC           
73AB: 7E         LD      A,(HL)          
73AC: A7         AND     A               
73AD: 28 1F      JR      Z,$73CE         
73AF: 21 00 C2   LD      HL,$C200        
73B2: 09         ADD     HL,BC           
73B3: 7E         LD      A,(HL)          
73B4: E0 EE      LDFF00  ($EE),A         
73B6: 21 10 C2   LD      HL,$C210        
73B9: 09         ADD     HL,BC           
73BA: 7E         LD      A,(HL)          
73BB: E0 EC      LDFF00  ($EC),A         
73BD: 21 B0 C3   LD      HL,$C3B0        
73C0: 09         ADD     HL,BC           
73C1: 7E         LD      A,(HL)          
73C2: E0 F1      LDFF00  ($F1),A         
73C4: 21 90 C2   LD      HL,$C290        
73C7: 09         ADD     HL,BC           
73C8: 7E         LD      A,(HL)          
73C9: E0 F0      LDFF00  ($F0),A         
73CB: CD D5 73   CALL    $73D5           
73CE: 0D         DEC     C               
73CF: 79         LD      A,C             
73D0: FE FF      CP      $FF             
73D2: 20 CF      JR      NZ,$73A3        
73D4: C9         RET                     
73D5: 21 80 C2   LD      HL,$C280        
73D8: 09         ADD     HL,BC           
73D9: 7E         LD      A,(HL)          
73DA: FE 05      CP      $05             
73DC: 28 4F      JR      Z,$742D         
73DE: FE 06      CP      $06             
73E0: CA 24 75   JP      Z,$7524         
73E3: FE 07      CP      $07             
73E5: CA 0C 77   JP      Z,$770C         
73E8: FE 08      CP      $08             
73EA: CA A2 76   JP      Z,$76A2         
73ED: CD 91 08   CALL    $0891           
73F0: 20 06      JR      NZ,$73F8        
73F2: 21 80 C2   LD      HL,$C280        
73F5: 09         ADD     HL,BC           
73F6: 70         LD      (HL),B          
73F7: C9         RET                     
73F8: 35         DEC     (HL)            
73F9: CD F0 74   CALL    $74F0           
73FC: C9         RET                     
73FD: 00         NOP                     
73FE: 00         NOP                     
73FF: 1C         INC     E               
7400: 00         NOP                     
7401: 00         NOP                     
7402: 08 1E 00   LD      ($001E),SP      
7405: 10 F8      STOP    $F8             
7407: 20 00      JR      NZ,$7409        
7409: 10 00      STOP    $00             
740B: 22         LD      (HLI),A         
740C: 00         NOP                     
740D: 10 08      STOP    $08             
740F: 24         INC     H               
7410: 00         NOP                     
7411: 10 10      STOP    $10             
7413: 26 00      LD      H,$00           
7415: F8 04      LDHL    SP,$04          
7417: 32         LD      (HLD),A         
7418: 00         NOP                     
7419: E8 04      ADD     SP,$04          
741B: 32         LD      (HLD),A         
741C: 00         NOP                     
741D: D8         RET     C               
741E: 04         INC     B               
741F: 32         LD      (HLD),A         
7420: 00         NOP                     
7421: C8         RET     Z               
7422: 04         INC     B               
7423: 32         LD      (HLD),A         
7424: 00         NOP                     
7425: 02         LD      (BC),A          
7426: 01 00 00   LD      BC,$0000        
7429: 00         NOP                     
742A: 01 02 02   LD      BC,$0202        
742D: FA 02 D0   LD      A,($D002)       
7430: A7         AND     A               
7431: 3E 00      LD      A,$00           
7433: 20 0A      JR      NZ,$743F        
7435: F0 E7      LD      A,($E7)         
7437: C6 D0      ADD     $D0             
7439: 1F         RRA                     
743A: 1F         RRA                     
743B: 1F         RRA                     
743C: 1F         RRA                     
743D: E6 07      AND     $07             
743F: 5F         LD      E,A             
7440: 16 00      LD      D,$00           
7442: 21 25 74   LD      HL,$7425        
7445: 19         ADD     HL,DE           
7446: 7E         LD      A,(HL)          
7447: 21 EC FF   LD      HL,$FFEC        
744A: 86         ADD     A,(HL)          
744B: 77         LD      (HL),A          
744C: 21 FD 73   LD      HL,$73FD        
744F: 11 00 C0   LD      DE,$C000        
7452: C5         PUSH    BC              
7453: 0E 06      LD      C,$06           
7455: F0 EC      LD      A,($EC)         
7457: 86         ADD     A,(HL)          
7458: 23         INC     HL              
7459: 12         LD      (DE),A          
745A: 13         INC     DE              
745B: F0 EE      LD      A,($EE)         
745D: 86         ADD     A,(HL)          
745E: 23         INC     HL              
745F: 12         LD      (DE),A          
7460: 13         INC     DE              
7461: 2A         LD      A,(HLI)         
7462: 12         LD      (DE),A          
7463: 13         INC     DE              
7464: 2A         LD      A,(HLI)         
7465: 12         LD      (DE),A          
7466: 13         INC     DE              
7467: 0D         DEC     C               
7468: 20 EB      JR      NZ,$7455        
746A: FA 02 D0   LD      A,($D002)       
746D: FE 10      CP      $10             
746F: 38 1D      JR      C,$748E         
7471: 21 15 74   LD      HL,$7415        
7474: 11 18 C0   LD      DE,$C018        
7477: 0E 04      LD      C,$04           
7479: F0 EC      LD      A,($EC)         
747B: 86         ADD     A,(HL)          
747C: 23         INC     HL              
747D: 12         LD      (DE),A          
747E: 13         INC     DE              
747F: F0 EE      LD      A,($EE)         
7481: 86         ADD     A,(HL)          
7482: 23         INC     HL              
7483: 12         LD      (DE),A          
7484: 13         INC     DE              
7485: 2A         LD      A,(HLI)         
7486: 12         LD      (DE),A          
7487: 13         INC     DE              
7488: 2A         LD      A,(HLI)         
7489: 12         LD      (DE),A          
748A: 13         INC     DE              
748B: 0D         DEC     C               
748C: 20 EB      JR      NZ,$7479        
748E: C1         POP     BC              
748F: C9         RET                     
7490: 00         NOP                     
7491: 00         NOP                     
7492: 34         INC     (HL)            
7493: 00         NOP                     
7494: 00         NOP                     
7495: 08 36 00   LD      ($0036),SP      
7498: 10 00      STOP    $00             
749A: 2C         INC     L               
749B: 00         NOP                     
749C: 20 F8      JR      NZ,$7496        
749E: 2C         INC     L               
749F: 00         NOP                     
74A0: 28 00      JR      Z,$74A2         
74A2: 2E 20      LD      L,$20           
74A4: 30 F0      JR      NC,$7496        
74A6: 2E 00      LD      L,$00           
74A8: 08 00 36   LD      ($3600),SP      
74AB: 20 08      JR      NZ,$74B5        
74AD: 08 34 20   LD      ($2034),SP      
74B0: 18 00      JR      $74B2           
74B2: 30 00      JR      NC,$74B4        
74B4: 18 08      JR      $74BE           
74B6: 2C         INC     L               
74B7: 20 28      JR      NZ,$74E1        
74B9: 10 2E      STOP    $2E             
74BB: 20 28      JR      NZ,$74E5        
74BD: 10 2E      STOP    $2E             
74BF: 20 00      JR      NZ,$74C1        
74C1: 08 34 20   LD      ($2034),SP      
74C4: 00         NOP                     
74C5: 00         NOP                     
74C6: 36 20      LD      (HL),$20        
74C8: 10 08      STOP    $08             
74CA: 2C         INC     L               
74CB: 20 20      JR      NZ,$74ED        
74CD: 10 2C      STOP    $2C             
74CF: 20 28      JR      NZ,$74F9        
74D1: 08 2E 00   LD      ($002E),SP      
74D4: 30 18      JR      NC,$74EE        
74D6: 2E 20      LD      L,$20           
74D8: 08 08 36   LD      ($3608),SP      
74DB: 00         NOP                     
74DC: 08 00 34   LD      ($3400),SP      
74DF: 00         NOP                     
74E0: 18 08      JR      $74EA           
74E2: 30 20      JR      NC,$7504        
74E4: 18 00      JR      $74E6           
74E6: 2C         INC     L               
74E7: 00         NOP                     
74E8: 28 F8      JR      Z,$74E2         
74EA: 2E 00      LD      L,$00           
74EC: 28 F8      JR      Z,$74E6         
74EE: 2E 00      LD      L,$00           
74F0: 21 80 C2   LD      HL,$C280        
74F3: 09         ADD     HL,BC           
74F4: 7E         LD      A,(HL)          
74F5: 3D         DEC     A               
74F6: CB 27      SET     1,E             
74F8: CB 27      SET     1,E             
74FA: CB 27      SET     1,E             
74FC: 5F         LD      E,A             
74FD: CB 27      SET     1,E             
74FF: 83         ADD     A,E             
7500: 5F         LD      E,A             
7501: 50         LD      D,B             
7502: 21 90 74   LD      HL,$7490        
7505: 19         ADD     HL,DE           
7506: 0E 06      LD      C,$06           
7508: CD 26 3D   CALL    $3D26           
750B: FA C0 C3   LD      A,($C3C0)       
750E: C6 18      ADD     $18             
7510: EA C0 C3   LD      ($C3C0),A       
7513: C9         RET                     
7514: 00         NOP                     
7515: 00         NOP                     
7516: 02         LD      (BC),A          
7517: 00         NOP                     
7518: 04         INC     B               
7519: 00         NOP                     
751A: 06 00      LD      B,$00           
751C: 08 00 0A   LD      ($0A00),SP      
751F: 00         NOP                     
7520: 0C         INC     C               
7521: 00         NOP                     
7522: 0E 00      LD      C,$00           
7524: CD 79 71   CALL    $7179           
7527: AF         XOR     A               
7528: EA 40 C3   LD      ($C340),A       
752B: 11 14 75   LD      DE,$7514        
752E: CD 3B 3C   CALL    $3C3B           
7531: FA C0 C3   LD      A,($C3C0)       
7534: C6 08      ADD     $08             
7536: EA C0 C3   LD      ($C3C0),A       
7539: F0 F0      LD      A,($F0)         
753B: C7         RST     0X00            
753C: 46         LD      B,(HL)          
753D: 75         LD      (HL),L          
753E: 70         LD      (HL),B          
753F: 75         LD      (HL),L          
7540: 9B         SBC     E               
7541: 75         LD      (HL),L          
7542: D6 75      SUB     $75             
7544: 46         LD      B,(HL)          
7545: 76         HALT                    
7546: CD 5F 7B   CALL    $7B5F           
7549: F0 E7      LD      A,($E7)         
754B: 1F         RRA                     
754C: 1F         RRA                     
754D: 1F         RRA                     
754E: E6 01      AND     $01             
7550: CD 87 3B   CALL    $3B87           
7553: F0 EE      LD      A,($EE)         
7555: FE 48      CP      $48             
7557: 30 08      JR      NC,$7561        
7559: CD 91 08   CALL    $0891           
755C: 36 40      LD      (HL),$40        
755E: CD 8D 3B   CALL    $3B8D           
7561: 21 D0 C3   LD      HL,$C3D0        
7564: 09         ADD     HL,BC           
7565: 35         DEC     (HL)            
7566: 20 07      JR      NZ,$756F        
7568: 36 04      LD      (HL),$04        
756A: 21 00 C2   LD      HL,$C200        
756D: 09         ADD     HL,BC           
756E: 35         DEC     (HL)            
756F: C9         RET                     
7570: CD 09 7B   CALL    $7B09           
7573: 3E 01      LD      A,$01           
7575: CD 87 3B   CALL    $3B87           
7578: CD 91 08   CALL    $0891           
757B: 20 1C      JR      NZ,$7599        
757D: CD 8D 3B   CALL    $3B8D           
7580: 3E 07      LD      A,$07           
7582: EA 81 C2   LD      ($C281),A       
7585: 3E FE      LD      A,$FE           
7587: EA 01 C2   LD      ($C201),A       
758A: 3E 6E      LD      A,$6E           
758C: EA 11 C2   LD      ($C211),A       
758F: AF         XOR     A               
7590: EA 91 C2   LD      ($C291),A       
7593: EA E1 C2   LD      ($C2E1),A       
7596: E0 E7      LDFF00  ($E7),A         
7598: C9         RET                     
7599: 35         DEC     (HL)            
759A: C9         RET                     
759B: CD 5F 7B   CALL    $7B5F           
759E: FA 01 C2   LD      A,($C201)       
75A1: 3D         DEC     A               
75A2: EA 01 C2   LD      ($C201),A       
75A5: F0 E7      LD      A,($E7)         
75A7: E6 01      AND     $01             
75A9: 20 21      JR      NZ,$75CC        
75AB: 21 96 FF   LD      HL,$FF96        
75AE: 34         INC     (HL)            
75AF: 7E         LD      A,(HL)          
75B0: FE 30      CP      $30             
75B2: 20 08      JR      NZ,$75BC        
75B4: CD 91 08   CALL    $0891           
75B7: 36 40      LD      (HL),$40        
75B9: C3 8D 3B   JP      $3B8D           
75BC: FE 20      CP      $20             
75BE: 20 04      JR      NZ,$75C4        
75C0: CD F3 76   CALL    $76F3           
75C3: AF         XOR     A               
75C4: FE 22      CP      $22             
75C6: 20 04      JR      NZ,$75CC        
75C8: CD EE 76   CALL    $76EE           
75CB: AF         XOR     A               
75CC: F0 E7      LD      A,($E7)         
75CE: 1F         RRA                     
75CF: 1F         RRA                     
75D0: E6 01      AND     $01             
75D2: CD 87 3B   CALL    $3B87           
75D5: C9         RET                     
75D6: CD 91 08   CALL    $0891           
75D9: 20 62      JR      NZ,$763D        
75DB: CD 92 7B   CALL    $7B92           
75DE: F0 E7      LD      A,($E7)         
75E0: E6 01      AND     $01             
75E2: 20 4D      JR      NZ,$7631        
75E4: FA 01 C2   LD      A,($C201)       
75E7: 3D         DEC     A               
75E8: EA 01 C2   LD      ($C201),A       
75EB: F0 E7      LD      A,($E7)         
75ED: E6 03      AND     $03             
75EF: 20 40      JR      NZ,$7631        
75F1: 21 96 FF   LD      HL,$FF96        
75F4: 34         INC     (HL)            
75F5: 7E         LD      A,(HL)          
75F6: FE 40      CP      $40             
75F8: 28 0B      JR      Z,$7605         
75FA: FE 3A      CP      $3A             
75FC: 20 0C      JR      NZ,$760A        
75FE: CD 91 08   CALL    $0891           
7601: 36 30      LD      (HL),$30        
7603: 18 05      JR      $760A           
7605: CD 91 08   CALL    $0891           
7608: 36 50      LD      (HL),$50        
760A: F0 96      LD      A,($96)         
760C: FE 56      CP      $56             
760E: 20 11      JR      NZ,$7621        
7610: 3E A0      LD      A,$A0           
7612: 77         LD      (HL),A          
7613: E0 43      LDFF00  ($43),A         
7615: 3E 01      LD      A,$01           
7617: E0 FF      LDFF00  ($FF),A         
7619: CD 91 08   CALL    $0891           
761C: 36 E0      LD      (HL),$E0        
761E: C3 8D 3B   JP      $3B8D           
7621: FE 20      CP      $20             
7623: 20 04      JR      NZ,$7629        
7625: CD F3 76   CALL    $76F3           
7628: AF         XOR     A               
7629: FE 22      CP      $22             
762B: 20 04      JR      NZ,$7631        
762D: CD EE 76   CALL    $76EE           
7630: AF         XOR     A               
7631: F0 E7      LD      A,($E7)         
7633: 1F         RRA                     
7634: 1F         RRA                     
7635: 1F         RRA                     
7636: 1F         RRA                     
7637: E6 01      AND     $01             
7639: CD 87 3B   CALL    $3B87           
763C: C9         RET                     
763D: 35         DEC     (HL)            
763E: CD 09 7B   CALL    $7B09           
7641: 3E 01      LD      A,$01           
7643: C3 87 3B   JP      $3B87           
7646: CD 09 7B   CALL    $7B09           
7649: F0 E7      LD      A,($E7)         
764B: E6 01      AND     $01             
764D: 20 32      JR      NZ,$7681        
764F: 3E 02      LD      A,$02           
7651: CD 87 3B   CALL    $3B87           
7654: 3E 00      LD      A,$00           
7656: EA B1 C3   LD      ($C3B1),A       
7659: CD 91 08   CALL    $0891           
765C: 28 01      JR      Z,$765F         
765E: 35         DEC     (HL)            
765F: FE A0      CP      $A0             
7661: 30 1E      JR      NC,$7681        
7663: FE 90      CP      $90             
7665: 30 10      JR      NC,$7677        
7667: FE 50      CP      $50             
7669: 30 16      JR      NC,$7681        
766B: FE 4A      CP      $4A             
766D: 30 08      JR      NC,$7677        
766F: FE 3C      CP      $3C             
7671: 30 0E      JR      NC,$7681        
7673: FE 36      CP      $36             
7675: 38 0A      JR      C,$7681         
7677: 3E 03      LD      A,$03           
7679: CD 87 3B   CALL    $3B87           
767C: 3E 01      LD      A,$01           
767E: EA B1 C3   LD      ($C3B1),A       
7681: C9         RET                     
7682: 38 00      JR      C,$7684         
7684: 38 20      JR      C,$76A6         
7686: 3A         LD      A,(HLD)         
7687: 00         NOP                     
7688: 3A         LD      A,(HLD)         
7689: 20 3A      JR      NZ,$76C5        
768B: 00         NOP                     
768C: 3A         LD      A,(HLD)         
768D: 20 3C      JR      NZ,$76CB        
768F: 00         NOP                     
7690: 3E 00      LD      A,$00           
7692: 3C         INC     A               
7693: 00         NOP                     
7694: 3E 00      LD      A,$00           
7696: 3A         LD      A,(HLD)         
7697: 00         NOP                     
7698: 3A         LD      A,(HLD)         
7699: 20 3A      JR      NZ,$76D5        
769B: 00         NOP                     
769C: 3A         LD      A,(HLD)         
769D: 20 38      JR      NZ,$76D7        
769F: 00         NOP                     
76A0: 38 20      JR      C,$76C2         
76A2: CD 91 08   CALL    $0891           
76A5: 35         DEC     (HL)            
76A6: 20 06      JR      NZ,$76AE        
76A8: 21 80 C2   LD      HL,$C280        
76AB: 09         ADD     HL,BC           
76AC: 70         LD      (HL),B          
76AD: C9         RET                     
76AE: 7E         LD      A,(HL)          
76AF: 1F         RRA                     
76B0: 1F         RRA                     
76B1: 1F         RRA                     
76B2: E6 07      AND     $07             
76B4: E0 F1      LDFF00  ($F1),A         
76B6: AF         XOR     A               
76B7: EA 40 C3   LD      ($C340),A       
76BA: 11 82 76   LD      DE,$7682        
76BD: CD 3B 3C   CALL    $3C3B           
76C0: FA C0 C3   LD      A,($C3C0)       
76C3: C6 08      ADD     $08             
76C5: EA C0 C3   LD      ($C3C0),A       
76C8: C9         RET                     
76C9: 98         SBC     B               
76CA: 00         NOP                     
76CB: 43         LD      B,E             
76CC: 7D         LD      A,L             
76CD: 98         SBC     B               
76CE: 20 43      JR      NZ,$7713        
76D0: 7D         LD      A,L             
76D1: 98         SBC     B               
76D2: 40         LD      B,B             
76D3: 43         LD      B,E             
76D4: 7D         LD      A,L             
76D5: 98         SBC     B               
76D6: 60         LD      H,B             
76D7: 43         LD      B,E             
76D8: 7D         LD      A,L             
76D9: 00         NOP                     
76DA: 98         SBC     B               
76DB: 04         INC     B               
76DC: 03         INC     BC              
76DD: 7D         LD      A,L             
76DE: 7D         LD      A,L             
76DF: 4C         LD      C,H             
76E0: 4D         LD      C,L             
76E1: 98         SBC     B               
76E2: 24         INC     H               
76E3: 43         LD      B,E             
76E4: 7D         LD      A,L             
76E5: 98         SBC     B               
76E6: 44         LD      B,H             
76E7: 43         LD      B,E             
76E8: 7D         LD      A,L             
76E9: 98         SBC     B               
76EA: 64         LD      H,H             
76EB: 43         LD      B,E             
76EC: 7D         LD      A,L             
76ED: 00         NOP                     
76EE: 21 DA 76   LD      HL,$76DA        
76F1: 18 03      JR      $76F6           
76F3: 21 C9 76   LD      HL,$76C9        
76F6: 11 01 D6   LD      DE,$D601        
76F9: C5         PUSH    BC              
76FA: 0E 18      LD      C,$18           
76FC: 2A         LD      A,(HLI)         
76FD: 12         LD      (DE),A          
76FE: 13         INC     DE              
76FF: 0D         DEC     C               
7700: 20 FA      JR      NZ,$76FC        
7702: C1         POP     BC              
7703: C9         RET                     
7704: 10 00      STOP    $00             
7706: 12         LD      (DE),A          
7707: 00         NOP                     
7708: 14         INC     D               
7709: 00         NOP                     
770A: 16 00      LD      D,$00           
770C: F0 EE      LD      A,($EE)         
770E: FE F0      CP      $F0             
7710: 30 12      JR      NC,$7724        
7712: AF         XOR     A               
7713: EA 40 C3   LD      ($C340),A       
7716: 11 04 77   LD      DE,$7704        
7719: CD 3B 3C   CALL    $3C3B           
771C: FA C0 C3   LD      A,($C3C0)       
771F: C6 08      ADD     $08             
7721: EA C0 C3   LD      ($C3C0),A       
7724: F0 F0      LD      A,($F0)         
7726: C7         RST     0X00            
7727: 2F         CPL                     
7728: 77         LD      (HL),A          
7729: 3B         DEC     SP              
772A: 77         LD      (HL),A          
772B: 4B         LD      C,E             
772C: 77         LD      (HL),A          
772D: A1         AND     C               
772E: 77         LD      (HL),A          
772F: CD 91 08   CALL    $0891           
7732: 35         DEC     (HL)            
7733: 20 05      JR      NZ,$773A        
7735: 36 90      LD      (HL),$90        
7737: CD 8D 3B   CALL    $3B8D           
773A: C9         RET                     
773B: F0 E7      LD      A,($E7)         
773D: E6 03      AND     $03             
773F: 20 06      JR      NZ,$7747        
7741: CD 91 08   CALL    $0891           
7744: 35         DEC     (HL)            
7745: 28 01      JR      Z,$7748         
7747: C9         RET                     
7748: C3 8D 3B   JP      $3B8D           
774B: FA 0A D0   LD      A,($D00A)       
774E: FE 13      CP      $13             
7750: 28 3E      JR      Z,$7790         
7752: FA 0E D0   LD      A,($D00E)       
7755: 3C         INC     A               
7756: EA 0E D0   LD      ($D00E),A       
7759: E6 03      AND     $03             
775B: 20 32      JR      NZ,$778F        
775D: FA 10 C2   LD      A,($C210)       
7760: FE A0      CP      $A0             
7762: 30 04      JR      NC,$7768        
7764: 3C         INC     A               
7765: EA 10 C2   LD      ($C210),A       
7768: FA 11 C2   LD      A,($C211)       
776B: FE A0      CP      $A0             
776D: 30 04      JR      NC,$7773        
776F: 3C         INC     A               
7770: EA 11 C2   LD      ($C211),A       
7773: F0 97      LD      A,($97)         
7775: F5         PUSH    AF              
7776: 3D         DEC     A               
7777: E0 97      LDFF00  ($97),A         
7779: F1         POP     AF              
777A: E6 07      AND     $07             
777C: 20 11      JR      NZ,$778F        
777E: C5         PUSH    BC              
777F: CD 41 7A   CALL    $7A41           
7782: C1         POP     BC              
7783: FA 0A D0   LD      A,($D00A)       
7786: FE 0B      CP      $0B             
7788: 20 05      JR      NZ,$778F        
778A: 3E 01      LD      A,$01           
778C: EA 68 D3   LD      ($D368),A       
778F: C9         RET                     
7790: CD 8D 3B   CALL    $3B8D           
7793: CD 91 08   CALL    $0891           
7796: 36 17      LD      (HL),$17        
7798: 3E 07      LD      A,$07           
779A: E0 A9      LDFF00  ($A9),A         
779C: 3E 70      LD      A,$70           
779E: E0 AA      LDFF00  ($AA),A         
77A0: C9         RET                     
77A1: F0 E7      LD      A,($E7)         
77A3: E6 03      AND     $03             
77A5: 20 19      JR      NZ,$77C0        
77A7: CD 91 08   CALL    $0891           
77AA: 35         DEC     (HL)            
77AB: 20 13      JR      NZ,$77C0        
77AD: CD 45 44   CALL    $4445           
77B0: AF         XOR     A               
77B1: EA 02 D0   LD      ($D002),A       
77B4: EA 03 D0   LD      ($D003),A       
77B7: EA 04 D0   LD      ($D004),A       
77BA: EA 80 C2   LD      ($C280),A       
77BD: EA 81 C2   LD      ($C281),A       
77C0: C9         RET                     
77C1: 7C         LD      A,H             
77C2: 7C         LD      A,H             
77C3: 44         LD      B,H             
77C4: 45         LD      B,L             
77C5: 7D         LD      A,L             
77C6: 7D         LD      A,L             
77C7: 7D         LD      A,L             
77C8: 7D         LD      A,L             
77C9: 7D         LD      A,L             
77CA: 7D         LD      A,L             
77CB: 7D         LD      A,L             
77CC: 7D         LD      A,L             
77CD: 7D         LD      A,L             
77CE: 7D         LD      A,L             
77CF: 7D         LD      A,L             
77D0: 7D         LD      A,L             
77D1: 4C         LD      C,H             
77D2: 4D         LD      C,L             
77D3: 7C         LD      A,H             
77D4: 7C         LD      A,H             
77D5: 7C         LD      A,H             
77D6: 7C         LD      A,H             
77D7: 7C         LD      A,H             
77D8: 7C         LD      A,H             
77D9: 44         LD      B,H             
77DA: 45         LD      B,L             
77DB: 7D         LD      A,L             
77DC: 7D         LD      A,L             
77DD: 7D         LD      A,L             
77DE: 7D         LD      A,L             
77DF: 7D         LD      A,L             
77E0: 7D         LD      A,L             
77E1: 7D         LD      A,L             
77E2: 7D         LD      A,L             
77E3: 4C         LD      C,H             
77E4: 4D         LD      C,L             
77E5: 7C         LD      A,H             
77E6: 7C         LD      A,H             
77E7: 7C         LD      A,H             
77E8: 7C         LD      A,H             
77E9: 7C         LD      A,H             
77EA: 7C         LD      A,H             
77EB: 7C         LD      A,H             
77EC: 7C         LD      A,H             
77ED: 7C         LD      A,H             
77EE: 70         LD      (HL),B          
77EF: 71         LD      (HL),C          
77F0: 72         LD      (HL),D          
77F1: 73         LD      (HL),E          
77F2: 74         LD      (HL),H          
77F3: 75         LD      (HL),L          
77F4: 76         HALT                    
77F5: 77         LD      (HL),A          
77F6: 78         LD      A,B             
77F7: 79         LD      A,C             
77F8: 7C         LD      A,H             
77F9: 7C         LD      A,H             
77FA: 7C         LD      A,H             
77FB: 7C         LD      A,H             
77FC: 7C         LD      A,H             
77FD: 7C         LD      A,H             
77FE: 7C         LD      A,H             
77FF: 7C         LD      A,H             
7800: 7C         LD      A,H             
7801: 7C         LD      A,H             
7802: 7C         LD      A,H             
7803: 7C         LD      A,H             
7804: 46         LD      B,(HL)          
7805: 7D         LD      A,L             
7806: 7D         LD      A,L             
7807: 7D         LD      A,L             
7808: 7D         LD      A,L             
7809: 4B         LD      C,E             
780A: 7C         LD      A,H             
780B: 7C         LD      A,H             
780C: 7C         LD      A,H             
780D: 7C         LD      A,H             
780E: 7C         LD      A,H             
780F: 7C         LD      A,H             
7810: 7C         LD      A,H             
7811: 7C         LD      A,H             
7812: 7C         LD      A,H             
7813: 7C         LD      A,H             
7814: 7C         LD      A,H             
7815: 7C         LD      A,H             
7816: 7C         LD      A,H             
7817: 7C         LD      A,H             
7818: 7C         LD      A,H             
7819: 5C         LD      E,H             
781A: 5D         LD      E,L             
781B: 5E         LD      E,(HL)          
781C: 5F         LD      E,A             
781D: 7C         LD      A,H             
781E: 7C         LD      A,H             
781F: 7C         LD      A,H             
7820: 7C         LD      A,H             
7821: 7C         LD      A,H             
7822: 7C         LD      A,H             
7823: 7C         LD      A,H             
7824: 7C         LD      A,H             
7825: 7C         LD      A,H             
7826: 7C         LD      A,H             
7827: 7C         LD      A,H             
7828: 7C         LD      A,H             
7829: 7C         LD      A,H             
782A: 7C         LD      A,H             
782B: 7C         LD      A,H             
782C: 7C         LD      A,H             
782D: 58         LD      E,B             
782E: 59         LD      E,C             
782F: 5A         LD      E,D             
7830: 5B         LD      E,E             
7831: 7C         LD      A,H             
7832: 7C         LD      A,H             
7833: 7C         LD      A,H             
7834: 7C         LD      A,H             
7835: 7C         LD      A,H             
7836: 7C         LD      A,H             
7837: 7C         LD      A,H             
7838: 7C         LD      A,H             
7839: 7C         LD      A,H             
783A: 7C         LD      A,H             
783B: 7C         LD      A,H             
783C: 7C         LD      A,H             
783D: 7C         LD      A,H             
783E: 7C         LD      A,H             
783F: 7C         LD      A,H             
7840: 7C         LD      A,H             
7841: 54         LD      D,H             
7842: 55         LD      D,L             
7843: 56         LD      D,(HL)          
7844: 57         LD      D,A             
7845: 7C         LD      A,H             
7846: 7C         LD      A,H             
7847: 7C         LD      A,H             
7848: 7C         LD      A,H             
7849: 7C         LD      A,H             
784A: 7C         LD      A,H             
784B: 7C         LD      A,H             
784C: 7C         LD      A,H             
784D: 7C         LD      A,H             
784E: 7C         LD      A,H             
784F: 7C         LD      A,H             
7850: 7C         LD      A,H             
7851: 7C         LD      A,H             
7852: 7C         LD      A,H             
7853: 7C         LD      A,H             
7854: 7C         LD      A,H             
7855: 50         LD      D,B             
7856: 51         LD      D,C             
7857: 52         LD      D,D             
7858: 53         LD      D,E             
7859: 7C         LD      A,H             
785A: 7C         LD      A,H             
785B: 7C         LD      A,H             
785C: 7C         LD      A,H             
785D: 7C         LD      A,H             
785E: 7C         LD      A,H             
785F: 7C         LD      A,H             
7860: 7C         LD      A,H             
7861: 7C         LD      A,H             
7862: 7C         LD      A,H             
7863: 7C         LD      A,H             
7864: 7C         LD      A,H             
7865: 7C         LD      A,H             
7866: 7C         LD      A,H             
7867: 7C         LD      A,H             
7868: 7C         LD      A,H             
7869: 7C         LD      A,H             
786A: 2B         DEC     HL              
786B: 2C         INC     L               
786C: 7C         LD      A,H             
786D: 7C         LD      A,H             
786E: 7C         LD      A,H             
786F: 7C         LD      A,H             
7870: 7C         LD      A,H             
7871: 7C         LD      A,H             
7872: 7C         LD      A,H             
7873: 7C         LD      A,H             
7874: 7C         LD      A,H             
7875: 7C         LD      A,H             
7876: 7C         LD      A,H             
7877: 7C         LD      A,H             
7878: 7C         LD      A,H             
7879: 7C         LD      A,H             
787A: 7C         LD      A,H             
787B: 7C         LD      A,H             
787C: 7C         LD      A,H             
787D: 7C         LD      A,H             
787E: 7C         LD      A,H             
787F: 7C         LD      A,H             
7880: 7C         LD      A,H             
7881: 7C         LD      A,H             
7882: 7C         LD      A,H             
7883: 7C         LD      A,H             
7884: 7C         LD      A,H             
7885: 7C         LD      A,H             
7886: 7C         LD      A,H             
7887: 7C         LD      A,H             
7888: 7C         LD      A,H             
7889: 7C         LD      A,H             
788A: 7C         LD      A,H             
788B: 7C         LD      A,H             
788C: 7C         LD      A,H             
788D: 7C         LD      A,H             
788E: 7C         LD      A,H             
788F: 7C         LD      A,H             
7890: 7C         LD      A,H             
7891: 7C         LD      A,H             
7892: 7C         LD      A,H             
7893: 7C         LD      A,H             
7894: 7C         LD      A,H             
7895: 7C         LD      A,H             
7896: 7C         LD      A,H             
7897: 7C         LD      A,H             
7898: 7C         LD      A,H             
7899: 7C         LD      A,H             
789A: 7C         LD      A,H             
789B: 7C         LD      A,H             
789C: 7C         LD      A,H             
789D: 7C         LD      A,H             
789E: 7C         LD      A,H             
789F: 7C         LD      A,H             
78A0: 7C         LD      A,H             
78A1: 7C         LD      A,H             
78A2: 7C         LD      A,H             
78A3: 7C         LD      A,H             
78A4: 7C         LD      A,H             
78A5: 7C         LD      A,H             
78A6: 7C         LD      A,H             
78A7: 7C         LD      A,H             
78A8: 7C         LD      A,H             
78A9: 7C         LD      A,H             
78AA: 7C         LD      A,H             
78AB: 7C         LD      A,H             
78AC: 7C         LD      A,H             
78AD: 7C         LD      A,H             
78AE: 7C         LD      A,H             
78AF: 7C         LD      A,H             
78B0: 7C         LD      A,H             
78B1: 7C         LD      A,H             
78B2: 7C         LD      A,H             
78B3: 7C         LD      A,H             
78B4: 7C         LD      A,H             
78B5: 7C         LD      A,H             
78B6: 7C         LD      A,H             
78B7: 7C         LD      A,H             
78B8: 7C         LD      A,H             
78B9: 7C         LD      A,H             
78BA: 7C         LD      A,H             
78BB: 7C         LD      A,H             
78BC: 7C         LD      A,H             
78BD: 7C         LD      A,H             
78BE: 7C         LD      A,H             
78BF: 7C         LD      A,H             
78C0: 7C         LD      A,H             
78C1: 7C         LD      A,H             
78C2: 7C         LD      A,H             
78C3: 7C         LD      A,H             
78C4: 7C         LD      A,H             
78C5: 7C         LD      A,H             
78C6: 7C         LD      A,H             
78C7: 7C         LD      A,H             
78C8: 7C         LD      A,H             
78C9: 7C         LD      A,H             
78CA: 7C         LD      A,H             
78CB: 7C         LD      A,H             
78CC: 7C         LD      A,H             
78CD: 7C         LD      A,H             
78CE: 7C         LD      A,H             
78CF: 7C         LD      A,H             
78D0: 7C         LD      A,H             
78D1: 7C         LD      A,H             
78D2: 7C         LD      A,H             
78D3: 7C         LD      A,H             
78D4: 7C         LD      A,H             
78D5: 7C         LD      A,H             
78D6: 7C         LD      A,H             
78D7: 7C         LD      A,H             
78D8: 7C         LD      A,H             
78D9: 7C         LD      A,H             
78DA: 7C         LD      A,H             
78DB: 7C         LD      A,H             
78DC: 7C         LD      A,H             
78DD: 7C         LD      A,H             
78DE: 7C         LD      A,H             
78DF: 7C         LD      A,H             
78E0: 7C         LD      A,H             
78E1: 7C         LD      A,H             
78E2: 7C         LD      A,H             
78E3: 7C         LD      A,H             
78E4: 7C         LD      A,H             
78E5: 7C         LD      A,H             
78E6: 7C         LD      A,H             
78E7: 7C         LD      A,H             
78E8: 7C         LD      A,H             
78E9: 7C         LD      A,H             
78EA: 7C         LD      A,H             
78EB: 7C         LD      A,H             
78EC: 7C         LD      A,H             
78ED: 7C         LD      A,H             
78EE: 7C         LD      A,H             
78EF: 7C         LD      A,H             
78F0: 7C         LD      A,H             
78F1: 7C         LD      A,H             
78F2: 7C         LD      A,H             
78F3: 7C         LD      A,H             
78F4: 7C         LD      A,H             
78F5: 7C         LD      A,H             
78F6: 7C         LD      A,H             
78F7: 7C         LD      A,H             
78F8: 7C         LD      A,H             
78F9: 7C         LD      A,H             
78FA: 7C         LD      A,H             
78FB: 7C         LD      A,H             
78FC: 7C         LD      A,H             
78FD: 7C         LD      A,H             
78FE: 7C         LD      A,H             
78FF: 7C         LD      A,H             
7900: 7C         LD      A,H             
7901: 7C         LD      A,H             
7902: 7C         LD      A,H             
7903: 7C         LD      A,H             
7904: 7C         LD      A,H             
7905: 7C         LD      A,H             
7906: 7C         LD      A,H             
7907: 7C         LD      A,H             
7908: 7C         LD      A,H             
7909: 7C         LD      A,H             
790A: 7C         LD      A,H             
790B: 7C         LD      A,H             
790C: 7C         LD      A,H             
790D: 7C         LD      A,H             
790E: 7C         LD      A,H             
790F: 7C         LD      A,H             
7910: 7C         LD      A,H             
7911: 7C         LD      A,H             
7912: 7C         LD      A,H             
7913: 7C         LD      A,H             
7914: 7C         LD      A,H             
7915: 7C         LD      A,H             
7916: 7C         LD      A,H             
7917: 7C         LD      A,H             
7918: 7C         LD      A,H             
7919: 7C         LD      A,H             
791A: 7C         LD      A,H             
791B: 7C         LD      A,H             
791C: 7C         LD      A,H             
791D: 7C         LD      A,H             
791E: 7C         LD      A,H             
791F: 7C         LD      A,H             
7920: 7C         LD      A,H             
7921: 7C         LD      A,H             
7922: 7C         LD      A,H             
7923: 7C         LD      A,H             
7924: 7C         LD      A,H             
7925: 7C         LD      A,H             
7926: 7C         LD      A,H             
7927: 7C         LD      A,H             
7928: 7C         LD      A,H             
7929: 7C         LD      A,H             
792A: 7C         LD      A,H             
792B: 7C         LD      A,H             
792C: 7C         LD      A,H             
792D: 7C         LD      A,H             
792E: 7C         LD      A,H             
792F: 7C         LD      A,H             
7930: 7C         LD      A,H             
7931: 7C         LD      A,H             
7932: 7C         LD      A,H             
7933: 7C         LD      A,H             
7934: 7C         LD      A,H             
7935: 7C         LD      A,H             
7936: 7C         LD      A,H             
7937: 7C         LD      A,H             
7938: 7C         LD      A,H             
7939: 7C         LD      A,H             
793A: 7C         LD      A,H             
793B: 7C         LD      A,H             
793C: 7C         LD      A,H             
793D: 7C         LD      A,H             
793E: 7C         LD      A,H             
793F: 7C         LD      A,H             
7940: 7C         LD      A,H             
7941: 7C         LD      A,H             
7942: 7C         LD      A,H             
7943: 7C         LD      A,H             
7944: 7C         LD      A,H             
7945: 7C         LD      A,H             
7946: 7C         LD      A,H             
7947: 7C         LD      A,H             
7948: 7C         LD      A,H             
7949: 7C         LD      A,H             
794A: 7C         LD      A,H             
794B: 7C         LD      A,H             
794C: 7C         LD      A,H             
794D: 7C         LD      A,H             
794E: 7C         LD      A,H             
794F: 7C         LD      A,H             
7950: 7C         LD      A,H             
7951: 7C         LD      A,H             
7952: 7C         LD      A,H             
7953: 7C         LD      A,H             
7954: 7C         LD      A,H             
7955: 7C         LD      A,H             
7956: 7C         LD      A,H             
7957: 7C         LD      A,H             
7958: 7C         LD      A,H             
7959: 7C         LD      A,H             
795A: 7C         LD      A,H             
795B: 7C         LD      A,H             
795C: 7C         LD      A,H             
795D: 7C         LD      A,H             
795E: 7C         LD      A,H             
795F: 7C         LD      A,H             
7960: 7C         LD      A,H             
7961: 7C         LD      A,H             
7962: 7C         LD      A,H             
7963: 7C         LD      A,H             
7964: 7C         LD      A,H             
7965: 7C         LD      A,H             
7966: 7C         LD      A,H             
7967: 7C         LD      A,H             
7968: 7C         LD      A,H             
7969: 7C         LD      A,H             
796A: 7C         LD      A,H             
796B: 7C         LD      A,H             
796C: 7C         LD      A,H             
796D: 7C         LD      A,H             
796E: 7C         LD      A,H             
796F: 7C         LD      A,H             
7970: 7C         LD      A,H             
7971: 7C         LD      A,H             
7972: 7C         LD      A,H             
7973: 7C         LD      A,H             
7974: 7C         LD      A,H             
7975: 7C         LD      A,H             
7976: 7C         LD      A,H             
7977: 7C         LD      A,H             
7978: 7C         LD      A,H             
7979: 7C         LD      A,H             
797A: 7C         LD      A,H             
797B: 7C         LD      A,H             
797C: 7C         LD      A,H             
797D: 7C         LD      A,H             
797E: 7C         LD      A,H             
797F: 7C         LD      A,H             
7980: 7C         LD      A,H             
7981: 7C         LD      A,H             
7982: 7C         LD      A,H             
7983: 7C         LD      A,H             
7984: 7C         LD      A,H             
7985: 7C         LD      A,H             
7986: 7C         LD      A,H             
7987: 7C         LD      A,H             
7988: 7C         LD      A,H             
7989: 7C         LD      A,H             
798A: 7C         LD      A,H             
798B: 7C         LD      A,H             
798C: 7C         LD      A,H             
798D: 7C         LD      A,H             
798E: 7C         LD      A,H             
798F: 7C         LD      A,H             
7990: 7C         LD      A,H             
7991: 7C         LD      A,H             
7992: 7C         LD      A,H             
7993: 7C         LD      A,H             
7994: 7C         LD      A,H             
7995: 7C         LD      A,H             
7996: 7C         LD      A,H             
7997: 7C         LD      A,H             
7998: 7C         LD      A,H             
7999: 7C         LD      A,H             
799A: 7C         LD      A,H             
799B: 7C         LD      A,H             
799C: 7C         LD      A,H             
799D: 7C         LD      A,H             
799E: 7C         LD      A,H             
799F: 7C         LD      A,H             
79A0: 7C         LD      A,H             
79A1: 7C         LD      A,H             
79A2: 7C         LD      A,H             
79A3: 7C         LD      A,H             
79A4: 7C         LD      A,H             
79A5: 7C         LD      A,H             
79A6: 7C         LD      A,H             
79A7: 7C         LD      A,H             
79A8: 7C         LD      A,H             
79A9: 7C         LD      A,H             
79AA: 7C         LD      A,H             
79AB: 7C         LD      A,H             
79AC: 7C         LD      A,H             
79AD: 7C         LD      A,H             
79AE: 7C         LD      A,H             
79AF: 7C         LD      A,H             
79B0: 7C         LD      A,H             
79B1: 7C         LD      A,H             
79B2: 7C         LD      A,H             
79B3: 7C         LD      A,H             
79B4: 7C         LD      A,H             
79B5: 7C         LD      A,H             
79B6: 7C         LD      A,H             
79B7: 7C         LD      A,H             
79B8: 7C         LD      A,H             
79B9: 7C         LD      A,H             
79BA: 7C         LD      A,H             
79BB: 7C         LD      A,H             
79BC: 7C         LD      A,H             
79BD: 7C         LD      A,H             
79BE: 7C         LD      A,H             
79BF: 7C         LD      A,H             
79C0: 7C         LD      A,H             
79C1: 7C         LD      A,H             
79C2: 7C         LD      A,H             
79C3: 7C         LD      A,H             
79C4: 7C         LD      A,H             
79C5: 7C         LD      A,H             
79C6: 7C         LD      A,H             
79C7: 7C         LD      A,H             
79C8: 7C         LD      A,H             
79C9: 7C         LD      A,H             
79CA: 7C         LD      A,H             
79CB: 7C         LD      A,H             
79CC: 7C         LD      A,H             
79CD: 7C         LD      A,H             
79CE: 7C         LD      A,H             
79CF: 7C         LD      A,H             
79D0: 7C         LD      A,H             
79D1: 7C         LD      A,H             
79D2: 7C         LD      A,H             
79D3: 7C         LD      A,H             
79D4: 7C         LD      A,H             
79D5: 7C         LD      A,H             
79D6: 7C         LD      A,H             
79D7: 7C         LD      A,H             
79D8: 7C         LD      A,H             
79D9: 7C         LD      A,H             
79DA: 7C         LD      A,H             
79DB: 7C         LD      A,H             
79DC: 7C         LD      A,H             
79DD: 7C         LD      A,H             
79DE: 7C         LD      A,H             
79DF: 7C         LD      A,H             
79E0: 7C         LD      A,H             
79E1: 7C         LD      A,H             
79E2: 7C         LD      A,H             
79E3: 7C         LD      A,H             
79E4: 7C         LD      A,H             
79E5: 7C         LD      A,H             
79E6: 7C         LD      A,H             
79E7: 7C         LD      A,H             
79E8: 7C         LD      A,H             
79E9: 7C         LD      A,H             
79EA: 7C         LD      A,H             
79EB: 7C         LD      A,H             
79EC: 7C         LD      A,H             
79ED: 7C         LD      A,H             
79EE: 7C         LD      A,H             
79EF: 7C         LD      A,H             
79F0: 7C         LD      A,H             
79F1: 7C         LD      A,H             
79F2: 7C         LD      A,H             
79F3: 7C         LD      A,H             
79F4: 7C         LD      A,H             
79F5: 7C         LD      A,H             
79F6: 7C         LD      A,H             
79F7: 7C         LD      A,H             
79F8: 7C         LD      A,H             
79F9: 7C         LD      A,H             
79FA: 7C         LD      A,H             
79FB: 7C         LD      A,H             
79FC: 7C         LD      A,H             
79FD: 7C         LD      A,H             
79FE: 7C         LD      A,H             
79FF: 7C         LD      A,H             
7A00: 7C         LD      A,H             
7A01: 7C         LD      A,H             
7A02: 7C         LD      A,H             
7A03: 7C         LD      A,H             
7A04: 7C         LD      A,H             
7A05: 7C         LD      A,H             
7A06: 7C         LD      A,H             
7A07: 7C         LD      A,H             
7A08: 7C         LD      A,H             
7A09: 7C         LD      A,H             
7A0A: 7C         LD      A,H             
7A0B: 7C         LD      A,H             
7A0C: 7C         LD      A,H             
7A0D: 7C         LD      A,H             
7A0E: 7C         LD      A,H             
7A0F: 7C         LD      A,H             
7A10: 7C         LD      A,H             
7A11: 7C         LD      A,H             
7A12: 7C         LD      A,H             
7A13: 7C         LD      A,H             
7A14: 7C         LD      A,H             
7A15: 7C         LD      A,H             
7A16: 7C         LD      A,H             
7A17: 7C         LD      A,H             
7A18: 7C         LD      A,H             
7A19: 7C         LD      A,H             
7A1A: 7C         LD      A,H             
7A1B: 7C         LD      A,H             
7A1C: 7C         LD      A,H             
7A1D: 7C         LD      A,H             
7A1E: 7C         LD      A,H             
7A1F: 7C         LD      A,H             
7A20: 7C         LD      A,H             
7A21: 7C         LD      A,H             
7A22: 7C         LD      A,H             
7A23: 7C         LD      A,H             
7A24: 7C         LD      A,H             
7A25: 7C         LD      A,H             
7A26: 7C         LD      A,H             
7A27: 7C         LD      A,H             
7A28: 7C         LD      A,H             
7A29: 7C         LD      A,H             
7A2A: 7C         LD      A,H             
7A2B: 7C         LD      A,H             
7A2C: 7C         LD      A,H             
7A2D: 7C         LD      A,H             
7A2E: 7C         LD      A,H             
7A2F: 7C         LD      A,H             
7A30: 7C         LD      A,H             
7A31: 7C         LD      A,H             
7A32: 7C         LD      A,H             
7A33: 7C         LD      A,H             
7A34: 7C         LD      A,H             
7A35: 7C         LD      A,H             
7A36: 7C         LD      A,H             
7A37: 7C         LD      A,H             
7A38: 7C         LD      A,H             
7A39: 7C         LD      A,H             
7A3A: 7C         LD      A,H             
7A3B: 7C         LD      A,H             
7A3C: 7C         LD      A,H             
7A3D: 7C         LD      A,H             
7A3E: 7C         LD      A,H             
7A3F: 7C         LD      A,H             
7A40: 7C         LD      A,H             
7A41: FA 0A D0   LD      A,($D00A)       
7A44: A7         AND     A               
7A45: 20 0A      JR      NZ,$7A51        
7A47: 3E F4      LD      A,$F4           
7A49: EA 0B D0   LD      ($D00B),A       
7A4C: 3E 9B      LD      A,$9B           
7A4E: EA 0C D0   LD      ($D00C),A       
7A51: FA 0A D0   LD      A,($D00A)       
7A54: 5F         LD      E,A             
7A55: 16 00      LD      D,$00           
7A57: CB 23      SET     1,E             
7A59: CB 12      SET     1,E             
7A5B: CB 23      SET     1,E             
7A5D: CB 12      SET     1,E             
7A5F: 7B         LD      A,E             
7A60: CB 23      SET     1,E             
7A62: CB 12      SET     1,E             
7A64: CB 23      SET     1,E             
7A66: CB 12      SET     1,E             
7A68: 83         ADD     A,E             
7A69: 5F         LD      E,A             
7A6A: 7A         LD      A,D             
7A6B: CE 00      ADC     $00             
7A6D: 57         LD      D,A             
7A6E: 0E 00      LD      C,$00           
7A70: 21 01 D6   LD      HL,$D601        
7A73: FA 0C D0   LD      A,($D00C)       
7A76: 22         LD      (HLI),A         
7A77: FA 0B D0   LD      A,($D00B)       
7A7A: 22         LD      (HLI),A         
7A7B: 3E 13      LD      A,$13           
7A7D: 22         LD      (HLI),A         
7A7E: E5         PUSH    HL              
7A7F: 21 C1 77   LD      HL,$77C1        
7A82: 19         ADD     HL,DE           
7A83: 7E         LD      A,(HL)          
7A84: E1         POP     HL              
7A85: 22         LD      (HLI),A         
7A86: 13         INC     DE              
7A87: 0C         INC     C               
7A88: 79         LD      A,C             
7A89: FE 14      CP      $14             
7A8B: 20 F1      JR      NZ,$7A7E        
7A8D: 36 00      LD      (HL),$00        
7A8F: 21 0A D0   LD      HL,$D00A        
7A92: 34         INC     (HL)            
7A93: FA 0B D0   LD      A,($D00B)       
7A96: D6 20      SUB     $20             
7A98: EA 0B D0   LD      ($D00B),A       
7A9B: FA 0C D0   LD      A,($D00C)       
7A9E: DE 00      SBC     $00             
7AA0: EA 0C D0   LD      ($D00C),A       
7AA3: C9         RET                     
7AA4: 00         NOP                     
7AA5: 50         LD      D,B             
7AA6: 80         ADD     A,B             
7AA7: 50         LD      D,B             
7AA8: 00         NOP                     
7AA9: 51         LD      D,C             
7AAA: 80         ADD     A,B             
7AAB: 51         LD      D,C             
7AAC: 00         NOP                     
7AAD: 52         LD      D,D             
7AAE: 80         ADD     A,B             
7AAF: 52         LD      D,D             
7AB0: 00         NOP                     
7AB1: 53         LD      D,E             
7AB2: 80         ADD     A,B             
7AB3: 53         LD      D,E             
7AB4: 00         NOP                     
7AB5: 02         LD      (BC),A          
7AB6: 04         INC     B               
7AB7: 06 06      LD      B,$06           
7AB9: 04         INC     B               
7ABA: 02         LD      (BC),A          
7ABB: 00         NOP                     
7ABC: 03         INC     BC              
7ABD: 02         LD      (BC),A          
7ABE: 01 00 00   LD      BC,$0000        
7AC1: 01 02 03   LD      BC,$0302        
7AC4: 21 00 C1   LD      HL,$C100        
7AC7: F0 E7      LD      A,($E7)         
7AC9: E6 07      AND     $07             
7ACB: 20 01      JR      NZ,$7ACE        
7ACD: 34         INC     (HL)            
7ACE: 23         INC     HL              
7ACF: F0 E7      LD      A,($E7)         
7AD1: E6 0F      AND     $0F             
7AD3: 20 01      JR      NZ,$7AD6        
7AD5: 34         INC     (HL)            
7AD6: 23         INC     HL              
7AD7: F0 E7      LD      A,($E7)         
7AD9: E6 1F      AND     $1F             
7ADB: 20 01      JR      NZ,$7ADE        
7ADD: 34         INC     (HL)            
7ADE: 23         INC     HL              
7ADF: F0 E7      LD      A,($E7)         
7AE1: E6 0F      AND     $0F             
7AE3: 20 01      JR      NZ,$7AE6        
7AE5: 34         INC     (HL)            
7AE6: 23         INC     HL              
7AE7: FA 04 D0   LD      A,($D004)       
7AEA: C6 28      ADD     $28             
7AEC: EA 04 D0   LD      ($D004),A       
7AEF: 30 01      JR      NC,$7AF2        
7AF1: 34         INC     (HL)            
7AF2: F0 E7      LD      A,($E7)         
7AF4: C6 FC      ADD     $FC             
7AF6: 1F         RRA                     
7AF7: 1F         RRA                     
7AF8: 1F         RRA                     
7AF9: 1F         RRA                     
7AFA: E6 07      AND     $07             
7AFC: 5F         LD      E,A             
7AFD: 16 00      LD      D,$00           
7AFF: 21 BC 7A   LD      HL,$7ABC        
7B02: 19         ADD     HL,DE           
7B03: 3E 00      LD      A,$00           
7B05: 96         SUB     (HL)            
7B06: EA 06 C1   LD      ($C106),A       
7B09: F0 E7      LD      A,($E7)         
7B0B: E6 0F      AND     $0F             
7B0D: FE 04      CP      $04             
7B0F: 38 4D      JR      C,$7B5E         
7B11: F0 E7      LD      A,($E7)         
7B13: 1F         RRA                     
7B14: 1F         RRA                     
7B15: 1F         RRA                     
7B16: 1F         RRA                     
7B17: E6 07      AND     $07             
7B19: 5F         LD      E,A             
7B1A: 16 00      LD      D,$00           
7B1C: 21 B4 7A   LD      HL,$7AB4        
7B1F: 19         ADD     HL,DE           
7B20: 5E         LD      E,(HL)          
7B21: 21 A4 7A   LD      HL,$7AA4        
7B24: FA 0F D0   LD      A,($D00F)       
7B27: A7         AND     A               
7B28: 28 03      JR      Z,$7B2D         
7B2A: 21 AC 7A   LD      HL,$7AAC        
7B2D: 19         ADD     HL,DE           
7B2E: 2A         LD      A,(HLI)         
7B2F: 66         LD      H,(HL)          
7B30: 6F         LD      L,A             
7B31: 11 00 89   LD      DE,$8900        
7B34: FA 0F D0   LD      A,($D00F)       
7B37: A7         AND     A               
7B38: 28 03      JR      Z,$7B3D         
7B3A: 11 00 93   LD      DE,$9300        
7B3D: F0 E7      LD      A,($E7)         
7B3F: E6 03      AND     $03             
7B41: CB 27      SET     1,E             
7B43: CB 27      SET     1,E             
7B45: CB 27      SET     1,E             
7B47: CB 27      SET     1,E             
7B49: CB 27      SET     1,E             
7B4B: 5F         LD      E,A             
7B4C: 85         ADD     A,L             
7B4D: 6F         LD      L,A             
7B4E: 7D         LD      A,L             
7B4F: EA 06 D0   LD      ($D006),A       
7B52: 7C         LD      A,H             
7B53: EA 07 D0   LD      ($D007),A       
7B56: 7B         LD      A,E             
7B57: EA 08 D0   LD      ($D008),A       
7B5A: 7A         LD      A,D             
7B5B: EA 09 D0   LD      ($D009),A       
7B5E: C9         RET                     
7B5F: 21 00 C1   LD      HL,$C100        
7B62: F0 E7      LD      A,($E7)         
7B64: E6 07      AND     $07             
7B66: 20 01      JR      NZ,$7B69        
7B68: 34         INC     (HL)            
7B69: 21 01 C1   LD      HL,$C101        
7B6C: FA 04 D0   LD      A,($D004)       
7B6F: C6 50      ADD     $50             
7B71: EA 04 D0   LD      ($D004),A       
7B74: 30 01      JR      NC,$7B77        
7B76: 34         INC     (HL)            
7B77: 23         INC     HL              
7B78: FA 05 D0   LD      A,($D005)       
7B7B: C6 58      ADD     $58             
7B7D: EA 05 D0   LD      ($D005),A       
7B80: 30 01      JR      NC,$7B83        
7B82: 34         INC     (HL)            
7B83: 23         INC     HL              
7B84: FA 0D D0   LD      A,($D00D)       
7B87: C6 B0      ADD     $B0             
7B89: EA 0D D0   LD      ($D00D),A       
7B8C: 30 01      JR      NC,$7B8F        
7B8E: 34         INC     (HL)            
7B8F: C3 09 7B   JP      $7B09           
7B92: 21 00 C1   LD      HL,$C100        
7B95: F0 E7      LD      A,($E7)         
7B97: E6 0F      AND     $0F             
7B99: 20 01      JR      NZ,$7B9C        
7B9B: 34         INC     (HL)            
7B9C: 21 01 C1   LD      HL,$C101        
7B9F: FA 04 D0   LD      A,($D004)       
7BA2: C6 28      ADD     $28             
7BA4: EA 04 D0   LD      ($D004),A       
7BA7: 30 01      JR      NC,$7BAA        
7BA9: 34         INC     (HL)            
7BAA: 23         INC     HL              
7BAB: FA 05 D0   LD      A,($D005)       
7BAE: C6 2C      ADD     $2C             
7BB0: EA 05 D0   LD      ($D005),A       
7BB3: 30 01      JR      NC,$7BB6        
7BB5: 34         INC     (HL)            
7BB6: 23         INC     HL              
7BB7: FA 0D D0   LD      A,($D00D)       
7BBA: C6 58      ADD     $58             
7BBC: EA 0D D0   LD      ($D00D),A       
7BBF: 30 01      JR      NC,$7BC2        
7BC1: 34         INC     (HL)            
7BC2: C3 09 7B   JP      $7B09           
7BC5: F0 92      LD      A,($92)         
7BC7: FE 08      CP      $08             
7BC9: DA 87 7C   JP      C,$7C87         
7BCC: 20 08      JR      NZ,$7BD6        
7BCE: CD 00 7C   CALL    $7C00           
7BD1: 21 92 FF   LD      HL,$FF92        
7BD4: 34         INC     (HL)            
7BD5: C9         RET                     
7BD6: CD FA 7B   CALL    $7BFA           
7BD9: AF         XOR     A               
7BDA: E0 90      LDFF00  ($90),A         
7BDC: E0 92      LDFF00  ($92),A         
7BDE: C9         RET                     
7BDF: 0F         RRCA                    
7BE0: 51         LD      D,C             
7BE1: B1         OR      C               
7BE2: EF         RST     0X28            
7BE3: EC                              
7BE4: AA         XOR     D               
7BE5: 4A         LD      C,D             
7BE6: 0C         INC     C               
7BE7: B1         OR      C               
7BE8: B2         OR      D               
7BE9: B3         OR      E               
7BEA: B4         OR      H               
7BEB: B5         OR      L               
7BEC: B6         OR      (HL)            
7BED: B7         OR      A               
7BEE: B8         CP      B               
7BEF: D0         RET     NC              
7BF0: D2 D4 D6   JP      NC,$D6D4        
7BF3: D8         RET     C               
7BF4: DA DC DE   JP      C,$DEDC         
7BF7: 01 1F 01   LD      BC,$011F        
7BFA: 0E 08      LD      C,$08           
7BFC: 1E 04      LD      E,$04           
7BFE: 18 04      JR      $7C04           
7C00: 0E 04      LD      C,$04           
7C02: 1E 00      LD      E,$00           
7C04: 79         LD      A,C             
7C05: E0 E0      LDFF00  ($E0),A         
7C07: 16 00      LD      D,$00           
7C09: AF         XOR     A               
7C0A: E0 D7      LDFF00  ($D7),A         
7C0C: E0 D8      LDFF00  ($D8),A         
7C0E: E0 D9      LDFF00  ($D9),A         
7C10: E0 DA      LDFF00  ($DA),A         
7C12: 21 65 DB   LD      HL,$DB65        
7C15: 19         ADD     HL,DE           
7C16: 7E         LD      A,(HL)          
7C17: CB 4F      SET     1,E             
7C19: C2 3A 7C   JP      NZ,$7C3A        
7C1C: 0E 00      LD      C,$00           
7C1E: 41         LD      B,C             
7C1F: 21 DF 7B   LD      HL,$7BDF        
7C22: 19         ADD     HL,DE           
7C23: 7E         LD      A,(HL)          
7C24: 6F         LD      L,A             
7C25: 26 9D      LD      H,$9D           
7C27: E5         PUSH    HL              
7C28: 3E 7C      LD      A,$7C           
7C2A: E0 D7      LDFF00  ($D7),A         
7C2C: E0 D8      LDFF00  ($D8),A         
7C2E: E0 D9      LDFF00  ($D9),A         
7C30: 21 E7 7B   LD      HL,$7BE7        
7C33: 19         ADD     HL,DE           
7C34: 7E         LD      A,(HL)          
7C35: E0 DA      LDFF00  ($DA),A         
7C37: E1         POP     HL              
7C38: 18 1E      JR      $7C58           
7C3A: 0E 00      LD      C,$00           
7C3C: 41         LD      B,C             
7C3D: 21 DF 7B   LD      HL,$7BDF        
7C40: 19         ADD     HL,DE           
7C41: 7E         LD      A,(HL)          
7C42: 6F         LD      L,A             
7C43: 26 9D      LD      H,$9D           
7C45: E5         PUSH    HL              
7C46: 21 EF 7B   LD      HL,$7BEF        
7C49: 19         ADD     HL,DE           
7C4A: 7E         LD      A,(HL)          
7C4B: E0 D7      LDFF00  ($D7),A         
7C4D: 3C         INC     A               
7C4E: E0 D8      LDFF00  ($D8),A         
7C50: C6 0F      ADD     $0F             
7C52: E0 D9      LDFF00  ($D9),A         
7C54: 3C         INC     A               
7C55: E0 DA      LDFF00  ($DA),A         
7C57: E1         POP     HL              
7C58: F0 D7      LD      A,($D7)         
7C5A: 77         LD      (HL),A          
7C5B: CD 79 7C   CALL    $7C79           
7C5E: F0 D8      LD      A,($D8)         
7C60: 77         LD      (HL),A          
7C61: 0C         INC     C               
7C62: CD 79 7C   CALL    $7C79           
7C65: F0 D9      LD      A,($D9)         
7C67: 77         LD      (HL),A          
7C68: 0C         INC     C               
7C69: CD 79 7C   CALL    $7C79           
7C6C: F0 DA      LD      A,($DA)         
7C6E: 77         LD      (HL),A          
7C6F: 1C         INC     E               
7C70: 7B         LD      A,E             
7C71: 21 E0 FF   LD      HL,$FFE0        
7C74: BE         CP      (HL)            
7C75: C2 09 7C   JP      NZ,$7C09        
7C78: C9         RET                     
7C79: E5         PUSH    HL              
7C7A: 21 F7 7B   LD      HL,$7BF7        
7C7D: 09         ADD     HL,BC           
7C7E: 7E         LD      A,(HL)          
7C7F: E1         POP     HL              
7C80: 85         ADD     A,L             
7C81: 6F         LD      L,A             
7C82: 7C         LD      A,H             
7C83: CE 00      ADC     $00             
7C85: 67         LD      H,A             
7C86: C9         RET                     
7C87: 4F         LD      C,A             
7C88: 06 00      LD      B,$00           
7C8A: CB 21      SET     1,E             
7C8C: CB 10      SET     1,E             
7C8E: CB 21      SET     1,E             
7C90: CB 10      SET     1,E             
7C92: CB 21      SET     1,E             
7C94: CB 10      SET     1,E             
7C96: CB 21      SET     1,E             
7C98: CB 10      SET     1,E             
7C9A: CB 21      SET     1,E             
7C9C: CB 10      SET     1,E             
7C9E: CB 21      SET     1,E             
7CA0: CB 10      SET     1,E             
7CA2: 21 00 8D   LD      HL,$8D00        
7CA5: 09         ADD     HL,BC           
7CA6: E5         PUSH    HL              
7CA7: D1         POP     DE              
7CA8: 21 00 4D   LD      HL,$4D00        
7CAB: 09         ADD     HL,BC           
7CAC: CD C6 08   CALL    $08C6           
7CAF: F0 92      LD      A,($92)         
7CB1: 3C         INC     A               
7CB2: E0 92      LDFF00  ($92),A         
7CB4: C9         RET                     
7CB5: 00         NOP                     
7CB6: 01 02 03   LD      BC,$0302        
7CB9: 04         INC     B               
7CBA: 05         DEC     B               
7CBB: 06 07      LD      B,$07           
7CBD: 08 09 0A   LD      ($0A09),SP      
7CC0: 0B         DEC     BC              
7CC1: 10 1B      STOP    $1B             
7CC3: 20 2B      JR      NZ,$7CF0        
7CC5: 30 3B      JR      NC,$7D02        
7CC7: 40         LD      B,B             
7CC8: 4B         LD      C,E             
7CC9: 50         LD      D,B             
7CCA: 5B         LD      E,E             
7CCB: 60         LD      H,B             
7CCC: 6B         LD      L,E             
7CCD: 70         LD      (HL),B          
7CCE: 7B         LD      A,E             
7CCF: 80         ADD     A,B             
7CD0: 8B         ADC     A,E             
7CD1: 90         SUB     B               
7CD2: 91         SUB     C               
7CD3: 92         SUB     D               
7CD4: 93         SUB     E               
7CD5: 94         SUB     H               
7CD6: 95         SUB     L               
7CD7: 96         SUB     (HL)            
7CD8: 97         SUB     A               
7CD9: 98         SBC     B               
7CDA: 99         SBC     C               
7CDB: 9A         SBC     D               
7CDC: 9B         SBC     E               
7CDD: FF         RST     0X38            
7CDE: 01 B5 7C   LD      BC,$7CB5        
7CE1: 0A         LD      A,(BC)          
7CE2: FE FF      CP      $FF             
7CE4: 28 0C      JR      Z,$7CF2         
7CE6: 5F         LD      E,A             
7CE7: 16 00      LD      D,$00           
7CE9: 21 00 D7   LD      HL,$D700        
7CEC: 19         ADD     HL,DE           
7CED: 36 FF      LD      (HL),$FF        
7CEF: 03         INC     BC              
7CF0: 18 EF      JR      $7CE1           
7CF2: C9         RET                     
7CF3: 01 00 04   LD      BC,$0400        
7CF6: 21 00 98   LD      HL,$9800        
7CF9: 1E 00      LD      E,$00           
7CFB: 7D         LD      A,L             
7CFC: E6 20      AND     $20             
7CFE: 28 01      JR      Z,$7D01         
7D00: 1C         INC     E               
7D01: 16 AE      LD      D,$AE           
7D03: 7D         LD      A,L             
7D04: E6 01      AND     $01             
7D06: AB         XOR     E               
7D07: 28 01      JR      Z,$7D0A         
7D09: 14         INC     D               
7D0A: 7D         LD      A,L             
7D0B: E6 1F      AND     $1F             
7D0D: FE 14      CP      $14             
7D0F: 30 01      JR      NC,$7D12        
7D11: 72         LD      (HL),D          
7D12: 23         INC     HL              
7D13: 0B         DEC     BC              
7D14: 78         LD      A,B             
7D15: B1         OR      C               
7D16: 20 E1      JR      NZ,$7CF9        
7D18: C9         RET                     

; Copy ? routine to HRAM at FFC0
7D19: 0E C0      LD      C,$C0           ; HRAM FFC0
7D1B: 06 0A      LD      B,$0A           ; 10 bytes in routine at 7D27
7D1D: 21 27 7D   LD      HL,$7D27        ; Start of routine to copy
7D20: 2A         LD      A,(HLI)         ; Copy ...
7D21: E2         LDFF00  (C),A           ; ... ? ...
7D22: 0C         INC     C               ; ... routine ...
7D23: 05         DEC     B               ; ... to ...
7D24: 20 FA      JR      NZ,$7D20        ; ... HRAM ...
7D26: C9         RET                     ; Out

; This routine is copied to FFC0..
; It loads FF46 with C0 and delays in a short loop
; ?What does this do?
7D27: 3E C0      LD      A,$C0           
7D29: E0 46      LDFF00  ($46),A         
7D2B: 3E 28      LD      A,$28           
7D2D: 3D         DEC     A               
7D2E: 20 FD      JR      NZ,$7D2D        
7D30: C9         RET                     

7D31: 80         ADD     A,B             
7D32: 80         ADD     A,B             
7D33: 40         LD      B,B             
7D34: 40         LD      B,B             
7D35: 20 20      JR      NZ,$7D57        
7D37: 10 10      STOP    $10             
7D39: 08 08 04   LD      ($0408),SP      
7D3C: 04         INC     B               
7D3D: 02         LD      (BC),A          
7D3E: 02         LD      (BC),A          
7D3F: 01 01 00   LD      BC,$0001        
7D42: 00         NOP                     
7D43: 00         NOP                     
7D44: 00         NOP                     
7D45: 00         NOP                     
7D46: 00         NOP                     
7D47: 00         NOP                     
7D48: 00         NOP                     
7D49: 00         NOP                     
7D4A: 00         NOP                     
7D4B: 00         NOP                     
7D4C: 00         NOP                     
7D4D: 00         NOP                     
7D4E: 00         NOP                     
7D4F: 00         NOP                     
7D50: 00         NOP                     
7D51: 80         ADD     A,B             
7D52: 80         ADD     A,B             
7D53: 40         LD      B,B             
7D54: 40         LD      B,B             
7D55: 20 20      JR      NZ,$7D77        
7D57: 10 10      STOP    $10             
7D59: 08 08 04   LD      ($0408),SP      
7D5C: 04         INC     B               
7D5D: 00         NOP                     
7D5E: 00         NOP                     
7D5F: 00         NOP                     
7D60: 00         NOP                     
7D61: 00         NOP                     
7D62: 00         NOP                     
7D63: 00         NOP                     
7D64: 00         NOP                     
7D65: 00         NOP                     
7D66: 00         NOP                     
7D67: 00         NOP                     
7D68: 00         NOP                     
7D69: 00         NOP                     
7D6A: 00         NOP                     
7D6B: 00         NOP                     
7D6C: 00         NOP                     
7D6D: 00         NOP                     
7D6E: 00         NOP                     
7D6F: 00         NOP                     
7D70: 00         NOP                     
7D71: 80         ADD     A,B             
7D72: 80         ADD     A,B             
7D73: 40         LD      B,B             
7D74: 40         LD      B,B             
7D75: 20 20      JR      NZ,$7D97        
7D77: 10 10      STOP    $10             
7D79: 00         NOP                     
7D7A: 00         NOP                     
7D7B: 00         NOP                     
7D7C: 00         NOP                     
7D7D: 00         NOP                     
7D7E: 00         NOP                     
7D7F: 00         NOP                     
7D80: 00         NOP                     
7D81: 00         NOP                     
7D82: 00         NOP                     
7D83: 00         NOP                     
7D84: 00         NOP                     
7D85: 00         NOP                     
7D86: 00         NOP                     
7D87: 00         NOP                     
7D88: 00         NOP                     
7D89: 00         NOP                     
7D8A: 00         NOP                     
7D8B: 00         NOP                     
7D8C: 00         NOP                     
7D8D: 00         NOP                     
7D8E: 00         NOP                     
7D8F: 00         NOP                     
7D90: 00         NOP                     
7D91: 80         ADD     A,B             
7D92: 80         ADD     A,B             
7D93: 40         LD      B,B             
7D94: 40         LD      B,B             
7D95: 20 20      JR      NZ,$7DB7        
7D97: 10 10      STOP    $10             
7D99: 08 08 04   LD      ($0408),SP      
7D9C: 04         INC     B               
7D9D: 02         LD      (BC),A          
7D9E: 02         LD      (BC),A          
7D9F: 01 01 00   LD      BC,$0001        
7DA2: 00         NOP                     
7DA3: 00         NOP                     
7DA4: 00         NOP                     
7DA5: 00         NOP                     
7DA6: 00         NOP                     
7DA7: 00         NOP                     
7DA8: 00         NOP                     
7DA9: 00         NOP                     
7DAA: 00         NOP                     
7DAB: 00         NOP                     
7DAC: 00         NOP                     
7DAD: 00         NOP                     
7DAE: 00         NOP                     
7DAF: 00         NOP                     
7DB0: 00         NOP                     
7DB1: 2D         DEC     L               
7DB2: 9E         SBC     (HL)            
7DB3: 2C         INC     L               
7DB4: 9E         SBC     (HL)            
7DB5: 2B         DEC     HL              
7DB6: 9E         SBC     (HL)            
7DB7: 2D         DEC     L               
7DB8: 9E         SBC     (HL)            
7DB9: 31 9E 2D   LD      SP,$2D9E        
7DBC: 9E         SBC     (HL)            
7DBD: 2B         DEC     HL              
7DBE: 9E         SBC     (HL)            
7DBF: 2D         DEC     L               
7DC0: 9E         SBC     (HL)            
7DC1: FA 04 00   LD      A,($0004)       
7DC4: A7         AND     A               
7DC5: C0         RET     NZ              
7DC6: FA A5 DB   LD      A,($DBA5)       
7DC9: A7         AND     A               
7DCA: 28 1B      JR      Z,$7DE7         
7DCC: F0 F7      LD      A,($F7)         
7DCE: FE 08      CP      $08             
7DD0: 30 15      JR      NC,$7DE7        
7DD2: CB 27      SET     1,E             
7DD4: 5F         LD      E,A             
7DD5: 16 00      LD      D,$00           
7DD7: 21 B1 7D   LD      HL,$7DB1        
7DDA: 19         ADD     HL,DE           
7DDB: 2A         LD      A,(HLI)         
7DDC: 66         LD      H,(HL)          
7DDD: 6F         LD      L,A             
7DDE: 36 A3      LD      (HL),$A3        
7DE0: F0 F9      LD      A,($F9)         
7DE2: A7         AND     A               
7DE3: 28 02      JR      Z,$7DE7         
7DE5: 36 7F      LD      (HL),$7F        
7DE7: C9         RET                     
7DE8: 27         DAA                     
7DE9: 6A         LD      L,D             
7DEA: 6C         LD      L,H             
7DEB: 21 22 23   LD      HL,$2322        
7DEE: 24         INC     H               
7DEF: 25         DEC     H               
7DF0: 26 6A      LD      H,$6A           
7DF2: FF         RST     0X38            
7DF3: 6C         LD      L,H             
7DF4: 6A         LD      L,D             
7DF5: 6C         LD      L,H             
7DF6: 6A         LD      L,D             
7DF7: 6C         LD      L,H             
7DF8: 65         LD      H,L             
7DF9: 65         LD      H,L             
7DFA: 66         LD      H,(HL)          
7DFB: 31 32 33   LD      SP,$3332        
7DFE: 34         INC     (HL)            
7DFF: 35         DEC     (HL)            
7E00: 36 67      LD      (HL),$67        
7E02: 68         LD      L,B             
7E03: 64         LD      H,H             
7E04: 67         LD      H,A             
7E05: 69         LD      L,C             
7E06: 65         LD      H,L             
7E07: 66         LD      H,(HL)          
7E08: 40         LD      B,B             
7E09: 40         LD      B,B             
7E0A: 41         LD      B,C             
7E0B: 42         LD      B,D             
7E0C: 43         LD      B,E             
7E0D: 44         LD      B,H             
7E0E: FA FA 63   LD      A,($63FA)       
7E11: 40         LD      B,B             
7E12: 40         LD      B,B             
7E13: 40         LD      B,B             
7E14: 40         LD      B,B             
7E15: 40         LD      B,B             
7E16: 40         LD      B,B             
7E17: 60         LD      H,B             
7E18: FF         RST     0X38            
7E19: FA 48 49   LD      A,($4948)       
7E1C: 4A         LD      C,D             
7E1D: FA FA FA   LD      A,($FAFA)       
7E20: 62         LD      H,D             
7E21: 6D         LD      L,L             
7E22: 6D         LD      L,L             
7E23: 6D         LD      L,L             
7E24: 6D         LD      L,L             
7E25: 6D         LD      L,L             
7E26: 6D         LD      L,L             
7E27: FF         RST     0X38            
7E28: 00         NOP                     
7E29: 01 00 01   LD      BC,$0100        
7E2C: FA FF 5E   LD      A,($5EFF)       
7E2F: 5F         LD      E,A             
7E30: 04         INC     B               
7E31: 05         DEC     B               
7E32: 06 07      LD      B,$07           
7E34: 28 29      JR      Z,$7E5F         
7E36: 29         ADD     HL,HL           
7E37: 2A         LD      A,(HLI)         
7E38: 10 11      STOP    $11             
7E3A: 10 11      STOP    $11             
7E3C: FA FA 6E   LD      A,($6EFA)       
7E3F: 6F         LD      L,A             
7E40: 14         INC     D               
7E41: 15         DEC     D               
7E42: 16 17      LD      D,$17           
7E44: 38 20      JR      C,$7E66         
7E46: 20 3A      JR      NZ,$7E82        
7E48: 00         NOP                     
7E49: 01 00 01   LD      BC,$0100        
7E4C: FB         EI                      
7E4D: FF         RST     0X38            
7E4E: FE FE      CP      $FE             
7E50: 08 09 0A   LD      ($0A09),SP      
7E53: 0B         DEC     BC              
7E54: 38 20      JR      C,$7E76         
7E56: 20 3A      JR      NZ,$7E92        
7E58: 10 11      STOP    $11             
7E5A: 10 11      STOP    $11             
7E5C: FB         EI                      
7E5D: FB         EI                      
7E5E: FE FE      CP      $FE             
7E60: 18 19      JR      $7E7B           
7E62: 1A         LD      A,(DE)          
7E63: 1B         DEC     DE              
7E64: 48         LD      C,B             
7E65: 49         LD      C,C             
7E66: 49         LD      C,C             
7E67: 4A         LD      C,D             
7E68: FB         EI                      
7E69: FF         RST     0X38            
7E6A: 0C         INC     C               
7E6B: 0D         DEC     C               
7E6C: 40         LD      B,B             
7E6D: 40         LD      B,B             
7E6E: 40         LD      B,B             
7E6F: 40         LD      B,B             
7E70: FA FA FF   LD      A,($FFFA)       
7E73: 58         LD      E,B             
7E74: 0E 0F      LD      C,$0F           
7E76: FA FA FB   LD      A,($FBFA)       
7E79: FB         EI                      
7E7A: 1C         INC     E               
7E7B: 1D         DEC     E               
7E7C: FA FA FA   LD      A,($FAFA)       
7E7F: FA FA FA   LD      A,($FAFA)       
7E82: FA 5D 1E   LD      A,($1E5D)       
7E85: 1F         RRA                     
7E86: FA FA 0C   LD      A,($0CFA)       
7E89: 0D         DEC     C               
7E8A: 0C         INC     C               
7E8B: 0D         DEC     C               
7E8C: FB         EI                      
7E8D: FB         EI                      
7E8E: 28 2A      JR      Z,$7EBA         
7E90: FA FA FA   LD      A,($FAFA)       
7E93: 58         LD      E,B             
7E94: 2D         DEC     L               
7E95: 2E 2E      LD      L,$2E           
7E97: 2F         CPL                     
7E98: 1C         INC     E               
7E99: 1D         DEC     E               
7E9A: 1C         INC     E               
7E9B: 1D         DEC     E               
7E9C: FB         EI                      
7E9D: 56         LD      D,(HL)          
7E9E: 61         LD      H,C             
7E9F: 4A         LD      C,D             
7EA0: FA FA 59   LD      A,($59FA)       
7EA3: 5A         LD      E,D             
7EA4: 3D         DEC     A               
7EA5: 3E 3E      LD      A,$3E           
7EA7: 3F         CCF                     
7EA8: FD                              
7EA9: FD                              
7EAA: FD                              
7EAB: FD                              
7EAC: FB         EI                      
7EAD: FB         EI                      
7EAE: FB         EI                      
7EAF: FB         EI                      
7EB0: 28 29      JR      Z,$7EDB         
7EB2: 5B         LD      E,E             
7EB3: FA FF FF   LD      A,($FFFF)       
7EB6: 54         LD      D,H             
7EB7: 54         LD      D,H             
7EB8: FD                              
7EB9: FD                              
7EBA: FD                              
7EBB: FD                              
7EBC: FB         EI                      
7EBD: FB         EI                      
7EBE: FF         RST     0X38            
7EBF: FB         EI                      
7EC0: 38 30      JR      C,$7EF2         
7EC2: 3A         LD      A,(HLD)         
7EC3: FA FF FF   LD      A,($FFFF)       
7EC6: 54         LD      D,H             
7EC7: 54         LD      D,H             
7EC8: FD                              
7EC9: FD                              
7ECA: FD                              
7ECB: FF         RST     0X38            
7ECC: FD                              
7ECD: FD                              
7ECE: FB         EI                      
7ECF: FB         EI                      
7ED0: 48         LD      C,B             
7ED1: FE 4A      CP      $4A             
7ED3: FA 56 57   LD      A,($5756)       
7ED6: 54         LD      D,H             
7ED7: 54         LD      D,H             
7ED8: 03         INC     BC              
7ED9: 12         LD      (DE),A          
7EDA: 13         INC     DE              
7EDB: 12         LD      (DE),A          
7EDC: 13         INC     DE              
7EDD: 02         LD      (BC),A          
7EDE: FF         RST     0X38            
7EDF: FB         EI                      
7EE0: 5C         LD      E,H             
7EE1: 2B         DEC     HL              
7EE2: FA FA FA   LD      A,($FAFA)       
7EE5: FA 54 54   LD      A,($5454)       
7EE8: 11 22 98   LD      DE,$9822        
7EEB: 01 00 00   LD      BC,$0000        
7EEE: FA A2 C5   LD      A,($C5A2)       
7EF1: A7         AND     A               
7EF2: 20 12      JR      NZ,$7F06        
7EF4: FA 95 DB   LD      A,($DB95)       
7EF7: FE 01      CP      $01             
7EF9: 28 0B      JR      Z,$7F06         
7EFB: 21 00 D8   LD      HL,$D800        
7EFE: 09         ADD     HL,BC           
7EFF: 7E         LD      A,(HL)          
7F00: E6 80      AND     $80             
7F02: 3E 2C      LD      A,$2C           
7F04: 28 05      JR      Z,$7F0B         
7F06: 21 E8 7D   LD      HL,$7DE8        
7F09: 09         ADD     HL,BC           
7F0A: 7E         LD      A,(HL)          
7F0B: 12         LD      (DE),A          
7F0C: 0C         INC     C               
7F0D: 28 14      JR      Z,$7F23         
7F0F: 1C         INC     E               
7F10: 7B         LD      A,E             
7F11: E6 1F      AND     $1F             
7F13: FE 12      CP      $12             
7F15: 20 0A      JR      NZ,$7F21        
7F17: 7B         LD      A,E             
7F18: E6 E0      AND     $E0             
7F1A: C6 22      ADD     $22             
7F1C: 5F         LD      E,A             
7F1D: 7A         LD      A,D             
7F1E: CE 00      ADC     $00             
7F20: 57         LD      D,A             
7F21: 18 CB      JR      $7EEE           
7F23: C9         RET                     
7F24: 0F         RRCA                    
7F25: 00         NOP                     
7F26: 1F         RRA                     
7F27: 00         NOP                     
7F28: 3F         CCF                     
7F29: 00         NOP                     
7F2A: 3F         CCF                     
7F2B: 11 3F 1F   LD      DE,$1F3F        
7F2E: 3F         CCF                     
7F2F: 1F         RRA                     
7F30: 3F         CCF                     
7F31: 19         ADD     HL,DE           
7F32: 3F         CCF                     
7F33: 11 3F 03   LD      DE,$033F        
7F36: FF         RST     0X38            
7F37: 1F         RRA                     
7F38: FF         RST     0X38            
7F39: 40         LD      B,B             
7F3A: FF         RST     0X38            
7F3B: 4A         LD      C,D             
7F3C: FF         RST     0X38            
7F3D: 51         LD      D,C             
7F3E: FF         RST     0X38            
7F3F: 5F         LD      E,A             
7F40: FE 5F      CP      $5F             
7F42: 7E         LD      A,(HL)          
7F43: 1F         RRA                     
7F44: 3E 1F      LD      A,$1F           
7F46: 3C         INC     A               
7F47: 1F         RRA                     
7F48: 3F         CCF                     
7F49: 1F         RRA                     
7F4A: 3F         CCF                     
7F4B: 1F         RRA                     
7F4C: 3F         CCF                     
7F4D: 1F         RRA                     
7F4E: 3F         CCF                     
7F4F: 1F         RRA                     
7F50: 3A         LD      A,(HLD)         
7F51: 1D         DEC     E               
7F52: 39         ADD     HL,SP           
7F53: 17         RLA                     
7F54: 33         INC     SP              
7F55: 1F         RRA                     
7F56: 3B         DEC     SP              
7F57: 16 39      LD      D,$39           
7F59: 1F         RRA                     
7F5A: 1C         INC     E               
7F5B: 0B         DEC     BC              
7F5C: 0F         RRCA                    
7F5D: 05         DEC     B               
7F5E: 07         RLCA                    
7F5F: 03         INC     BC              
7F60: 03         INC     BC              
7F61: 00         NOP                     
7F62: 00         NOP                     
7F63: 00         NOP                     
7F64: 4C         LD      C,H             
7F65: 62         LD      H,D             
7F66: 63         LD      H,E             
7F67: 66         LD      H,(HL)          
7F68: 6B         LD      L,E             
7F69: 63         LD      H,E             
7F6A: 65         LD      H,L             
7F6B: 64         LD      H,H             
7F6C: 60         LD      H,B             
7F6D: 4C         LD      C,H             
7F6E: 4D         LD      C,L             
7F6F: 4C         LD      C,H             
7F70: 4C         LD      C,H             
7F71: 4C         LD      C,H             
7F72: 4E         LD      C,(HL)          
7F73: 4E         LD      C,(HL)          
7F74: 4E         LD      C,(HL)          
7F75: 4D         LD      C,L             
7F76: 4D         LD      C,L             
7F77: 4F         LD      C,A             
7F78: 61         LD      H,C             
7F79: 63         LD      H,E             
7F7A: 63         LD      H,E             
7F7B: 00         NOP                     
7F7C: 00         NOP                     
7F7D: 00         NOP                     
7F7E: 00         NOP                     
7F7F: 00         NOP                     
7F80: 00         NOP                     
7F81: 4E         LD      C,(HL)          
7F82: 4E         LD      C,(HL)          
7F83: 4D         LD      C,L             
7F84: 40         LD      B,B             
7F85: 40         LD      B,B             
7F86: 6C         LD      L,H             
7F87: 40         LD      B,B             
7F88: 40         LD      B,B             
7F89: 6C         LD      L,H             
7F8A: 40         LD      B,B             
7F8B: 6E         LD      L,(HL)          
7F8C: 4A         LD      C,D             
7F8D: 40         LD      B,B             
7F8E: 46         LD      B,(HL)          
7F8F: 40         LD      B,B             
7F90: 40         LD      B,B             
7F91: 40         LD      B,B             
7F92: 48         LD      C,B             
7F93: 48         LD      C,B             
7F94: 48         LD      C,B             
7F95: 46         LD      B,(HL)          
7F96: 48         LD      C,B             
7F97: 4A         LD      C,D             
7F98: 40         LD      B,B             
7F99: 46         LD      B,(HL)          
7F9A: 6C         LD      L,H             
7F9B: 00         NOP                     
7F9C: 00         NOP                     
7F9D: 00         NOP                     
7F9E: 00         NOP                     
7F9F: 00         NOP                     
7FA0: 00         NOP                     
7FA1: 48         LD      C,B             
7FA2: 48         LD      C,B             
7FA3: 46         LD      B,(HL)          
7FA4: 79         LD      A,C             
7FA5: 79         LD      A,C             
7FA6: 77         LD      (HL),A          
7FA7: 79         LD      A,C             
7FA8: 79         LD      A,C             
7FA9: 77         LD      (HL),A          
7FAA: 78         LD      A,B             
7FAB: 79         LD      A,C             
7FAC: 79         LD      A,C             
7FAD: 63         LD      H,E             
7FAE: 7A         LD      A,D             
7FAF: 00         NOP                     
7FB0: 00         NOP                     
7FB1: 00         NOP                     
7FB2: 7B         LD      A,E             
7FB3: 7B         LD      A,E             
7FB4: 7B         LD      A,E             
7FB5: 7A         LD      A,D             
7FB6: 7B         LD      A,E             
7FB7: 79         LD      A,C             
7FB8: 7C         LD      A,H             
7FB9: 7A         LD      A,D             
7FBA: 77         LD      (HL),A          
7FBB: 00         NOP                     
7FBC: 00         NOP                     
7FBD: 00         NOP                     
7FBE: 00         NOP                     
7FBF: 00         NOP                     
7FC0: 00         NOP                     
7FC1: 7C         LD      A,H             
7FC2: 7B         LD      A,E             
7FC3: 7A         LD      A,D             
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
