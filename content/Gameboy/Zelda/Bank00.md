![Bank 00](GBZelda.jpg)

# Bank 00

>>> cpu Z80GB

>>> binary 0000:roms/zelda.gb[0000:4000]

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

```code
; TODO:
; Problems in disassembly. Fix and write REDIS program.
; - CB instructions are jacked. CB87 should be RES 0,A and does something else
; - ": F0" should be LDFF00 -- not LD
;
; Proper way to document a function
; Document RAM addresses correctly
; JavaScript to show tiles/sprites
; What's up with Horiz/Veritcal implulse. Looks likes the code is doing 2 different.       

0000: C3 72 28   JP      $2872           ; RST 0 rerouted to table-jumper
0003: 00         NOP
0004: 00         NOP
                   
0005: FF FF FF FF FF FF FF FF FF FF FF           
0010: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF      
0020: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
0030: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF      
    
0040: C3 25 05   JP           $0525
0043: FF FF FF FF FF
           
0048: C3 E2 03   JP           $03E2
004B: FF FF FF FF FF
            
0050: D9         RETI
0051: FF FF FF FF FF FF FF
           
0058: D9         RETI
0059: FF FF FF FF FF FF FF
            
0060: D9         RETI
0061: FF
           
0062: 21 00 69   LD           HL,$6900
0065: 11 A0 89   LD           DE,$89A0 ; ?Character RAM
0068: 18 16      JR           $80

006A: 21 30 69   LD           HL,$6930
006D: 11 D0 89   LD           DE,$89D0 ; ?Character RAM
0070: 18 0E      JR           $80
       
0072: 21 D0 49   LD           HL,$49D0
0075: 11 D0 89   LD           DE,$89D0 ; ?Character RAM
0078: 18 06      JR           $80
        
007A: 21 A0 49   LD           HL,$49A0
007D: 11 A0 89   LD           DE,$89A0 ; ?Character RAM
;        
0080: 01 30 00   LD           BC,$0030 ; 48 bytes (3 tile maps) to copy
0083: CD C5 28   CALL       $28C5 ; Copy HL to DE
0086: AF         XOR         A ; 0 ...
0087: E0 90      LDFF00   ($90),A ; ?In high ram
0089: E0 92      LDFF00   ($92),A ; 
008B: 3E 0C      LD           A,$0C ; Bank switch to ...
008D: EA 00 21   LD           ($2100),A ; ... Bank 0C
0090: C9         RET ; Done

0091: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
00A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
00B0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
00C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
00D0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
00E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
00F0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
  
; Gameboy boot ROM transfers control here    
0100: 00         NOP
0101: C3 50 01   JP           $0150 ; Start game
       
; Nintendo characters
0104: CE ED 66 66 CC 0D 00 0B 03 73 00 83            
0110: 00 0C 00 0D 00 08 11 1F 88 89 00 0E DC CC 6E E6         
0120: DD DD D9 99 BB BB 67 63 6E 0E EC CC DD DC 99 9F             
0130: BB B9 33 3E
 
;     Z  E  L  D  A
0134: 5A 45 4C 44 41 00 00 00 00 00 00 00 00 00 00 00
                    
0144: 00 00 ; Extended manufacturer code (none here)
0146: 00    ; Not used
0147: 03    ; Cartridge type (ROM+MBC1+RAM+BATTERY)
0148: 04    ; ROM Size (512K -- 32 banks)
0149: 02    ; RAM Size (8K   --  1 bank)
014A: 01    ; Language (English)
014B: 01    ; Manufacturer code
014C: 00    ; Version number
014D: 6C    ; Complement check
014E: 47 B7 ; Checksum

; Code starts here
Startup:
0150: CD 81 28   CALL       $2881 ; Turn off LCD
0153: 31 FF DF   LD           SP,$DFFF ; Stack in internal RAM ?DF00-DFFF
0156: AF         XOR         A ; Clear out ...
0157: E0 47      LDFF00   ($47),A ; ... Background palette ...
0159: E0 48      LDFF00   ($48),A ; ... Sprite palette #0 ...
015B: E0 49      LDFF00   ($49),A ; ... Sprite palette #1
015D: 21 00 80   LD           HL,$8000 ; Clear ...
0160: 01 00 18   LD           BC,$1800 ; ... 8000-97FF ...
0163: CD 99 29   CALL       $2999 ; ... Tile Pattern Tables
0166: CD A8 28   CALL       $28A8 ; Fill Background Tile Table with 7Fs
0169: CD 8A 29   CALL       $298A ; Clear RAM and HRAM
016C: 3E 01      LD           A,$01 ; Switch in ...
016E: EA 00 21   LD           ($2100),A ; ... bank 01
0171: CD 19 7D   CALL       $7D19 ; Copy ?routine to HRAM at FFC0
0174: CD C0 FF   CALL       $FFC0 ; Call ?routine
0177: CD CE 40   CALL       $40CE ; ?window and lcd
017A: CD 6B 2B   CALL       $2B6B ; ?lots of tile pattern work
017D: 3E 44      LD           A,$44 ; 0100 0100 
017F: E0 41      LDFF00   ($41),A ; LCDSTAT= ?Horiz blanking impulse, interrupt on coincidence
0181: 3E 4F      LD           A,$4F ; Scanline 79
0183: E0 45      LDFF00   ($45),A ; Scanline compare = 79
0185: 3E 01      LD           A,$01 ; Currently in ...
0187: EA AF DB   LD           ($DBAF),A ; ... bank 01
018A: 3E 01      LD           A,$01 ; Enable ...
018C: E0 FF      LDFF00   ($FF),A ; ... vertical blanking impulse
018E: 3E 01      LD           A,$01 ; Switch in ...
0190: EA 00 21   LD           ($2100),A ; ... bank 01
0193: CD 0F 46   CALL       $460F
0196: 3E 1F      LD           A,$1F ; Switch in ...
0198: EA 00 21   LD           ($2100),A ; ... bank 1F
019B: CD 00 40   CALL       $4000
019E: 3E 18      LD           A,$18
01A0: E0 B5      LDFF00   ($B5),A
01A2: FB         EI ; Enable interrupts
01A3: C3 BD 03   JP           $03BD

01A6: 3E 01      LD           A,$01
01A8: E0 FD      LDFF00   ($FD),A
01AA: FA 00 C5   LD           A,($C500)
01AD: A7         AND         A
01AE: 28 0E      JR           Z,$1BE
01B0: FA 95 DB   LD           A,($DB95)
01B3: FE 0B      CP           $0B
01B5: 20 07      JR           NZ,$1BE
01B7: F0 E7      LD           A,($E7)
01B9: 0F         RRCA
01BA: E6 80      AND         $80
01BC: 18 06      JR           $1C4
01BE: 21 56 C1   LD           HL,$C156
01C1: F0 97      LD           A,($97)
01C3: 86         ADD         A,(HL)
01C4: E0 42      LDFF00   ($42),A
01C6: F0 96      LD           A,($96)
01C8: 21 55 C1   LD           HL,$C155
01CB: 86         ADD         A,(HL)
01CC: 21 BF C1   LD           HL,$C1BF
01CF: 86         ADD         A,(HL)
01D0: E0 43      LDFF00   ($43),A
01D2: FA FE D6   LD           A,($D6FE)
01D5: A7         AND         A
01D6: 20 07      JR           NZ,$1DF
01D8: FA FF D6   LD           A,($D6FF)
01DB: FE 00      CP           $00
01DD: 28 2A      JR           Z,$209
01DF: FA 95 DB   LD           A,($DB95)
01E2: FE 09      CP           $09
01E4: 28 0F      JR           Z,$1F5
01E6: FE 06      CP           $06
01E8: 38 0B      JR           C,$1F5
01EA: FE 0B      CP           $0B
01EC: 20 0D      JR           NZ,$1FB
01EE: FA 96 DB   LD           A,($DB96)
01F1: FE 07      CP           $07
01F3: 30 06      JR           NC,$1FB
01F5: CD 44 08   CALL       $0844
01F8: CD 44 08   CALL       $0844
01FB: F3         DI
01FC: CD A1 04   CALL       $04A1
01FF: FB         EI
0200: CD 44 08   CALL       $0844
0203: CD 44 08   CALL       $0844
0206: C3 BD 03   JP           $03BD
0209: FA FD D6   LD           A,($D6FD)
020C: E6 7F      AND         $7F
020E: 5F         LD           E,A
020F: F0 40      LD           A,($40)
0211: E6 80      AND         $80
0213: B3         OR           E
0214: E0 40      LDFF00   ($40),A
0216: 21 E7 FF   LD           HL,$FFE7
0219: 34         INC         (HL)
021A: FA 95 DB   LD           A,($DB95)
021D: FE 00      CP           $00
021F: 20 0F      JR           NZ,$230
0221: FA 96 DB   LD           A,($DB96)
0224: FE 08      CP           $08
0226: 38 08      JR           C,$230
0228: 3E 01      LD           A,$01
022A: EA 00 21   LD           ($2100),A
022D: CD B7 6D   CALL       $6DB7
0230: FA 7F C1   LD           A,($C17F)
0233: A7         AND         A
0234: CA 52 03   JP           Z,$0352
0237: 3C         INC         A
0238: 20 0B      JR           NZ,$245
023A: 3E 17      LD           A,$17
023C: EA 00 21   LD           ($2100),A
023F: CD A6 46   CALL       $46A6
0242: C3 52 03   JP           $0352
0245: 3C         INC         A
0246: 28 F2      JR           Z,$23A
0248: 3E 14      LD           A,$14
024A: EA 00 21   LD           ($2100),A
024D: FA 80 C1   LD           A,($C180)
0250: 3C         INC         A
0251: EA 80 C1   LD           ($C180),A
0254: FE C0      CP           $C0
0256: 20 14      JR           NZ,$26C
0258: FA 7F C1   LD           A,($C17F)
025B: FE 02      CP           $02
025D: 20 03      JR           NZ,$262
025F: CD 1B 54   CALL       $541B
0262: AF         XOR         A
0263: EA 7F C1   LD           ($C17F),A
0266: EA CA C3   LD           ($C3CA),A
0269: C3 52 03   JP           $0352
026C: FE 60      CP           $60
026E: 38 4C      JR           C,$2BC
0270: F5         PUSH       AF
0271: E6 07      AND         $07
0273: 20 0B      JR           NZ,$280
0275: FA CA C3   LD           A,($C3CA)
0278: FE 0C      CP           $0C
027A: 28 3F      JR           Z,$2BB
027C: 3C         INC         A
027D: EA CA C3   LD           ($C3CA),A
0280: FA CA C3   LD           A,($C3CA)
0283: 5F         LD           E,A
0284: F0 E7      LD           A,($E7)
0286: E6 03      AND         $03
0288: 83         ADD         A,E
0289: 5F         LD           E,A
028A: 16 00      LD           D,$00
028C: FA 7F C1   LD           A,($C17F)
028F: FE 03      CP           $03
0291: 28 15      JR           Z,$2A8
0293: 21 6A 54   LD           HL,$546A
0296: 19         ADD         HL,DE
0297: 7E         LD           A,(HL)
0298: EA 97 DB   LD           ($DB97),A
029B: EA 99 DB   LD           ($DB99),A
029E: 21 7A 54   LD           HL,$547A
02A1: 19         ADD         HL,DE
02A2: 7E         LD           A,(HL)
02A3: EA 98 DB   LD           ($DB98),A
02A6: 18 13      JR           $2BB
02A8: 21 8A 54   LD           HL,$548A
02AB: 19         ADD         HL,DE
02AC: 7E         LD           A,(HL)
02AD: EA 97 DB   LD           ($DB97),A
02B0: EA 99 DB   LD           ($DB99),A
02B3: 21 9A 54   LD           HL,$549A
02B6: 19         ADD         HL,DE
02B7: 7E         LD           A,(HL)
02B8: EA 98 DB   LD           ($DB98),A
02BB: F1         POP         AF
02BC: CB 3F      SRL         A
02BE: CB 3F      SRL         A
02C0: E0 D7      LDFF00   ($D7),A
02C2: FA 80 C1   LD           A,($C180)
02C5: 00         NOP
02C6: E6 E0      AND         $E0
02C8: 5F         LD           E,A
02C9: FA 7F C1   LD           A,($C17F)
02CC: FE 03      CP           $03
02CE: 20 04      JR           NZ,$2D4
02D0: 7B         LD           A,E
02D1: EE E0      XOR         $E0
02D3: 5F         LD           E,A
02D4: 7B         LD           A,E
02D5: E0 D8      LDFF00   ($D8),A
02D7: 21 7C C1   LD           HL,$C17C
02DA: AF         XOR         A
02DB: 22         LD           (HLI),A
02DC: 22         LD           (HLI),A
02DD: 22         LD           (HLI),A
02DE: F0 41      LD           A,($41)
02E0: E6 03      AND         $03
02E2: 20 FA      JR           NZ,$2DE
02E4: 16 00      LD           D,$00
02E6: FA 7E C1   LD           A,($C17E)
02E9: 3C         INC         A
02EA: EA 7E C1   LD           ($C17E),A
02ED: E6 01      AND         $01
02EF: 20 F5      JR           NZ,$2E6
02F1: FA 7C C1   LD           A,($C17C)
02F4: C6 01      ADD         $01
02F6: EA 7C C1   LD           ($C17C),A
02F9: FA 7D C1   LD           A,($C17D)
02FC: CE 00      ADC         $00
02FE: EA 7D C1   LD           ($C17D),A
0301: FA 7C C1   LD           A,($C17C)
0304: FE 58      CP           $58
0306: CA 3E 03   JP           Z,$033E
0309: 0E 00      LD           C,$00
030B: FA 7F C1   LD           A,($C17F)
030E: FE 01      CP           $01
0310: 28 01      JR           Z,$313
0312: 0C         INC         C
0313: 21 7C C1   LD           HL,$C17C
0316: F0 D7      LD           A,($D7)
0318: 86         ADD         A,(HL)
0319: E6 1F      AND         $1F
031B: 21 D8 FF   LD           HL,$FFD8
031E: B6         OR           (HL)
031F: 5F         LD           E,A
0320: 21 AA 54   LD           HL,$54AA
0323: 19         ADD         HL,DE
0324: FA 80 C1   LD           A,($C180)
0327: A1         AND         C
0328: 7E         LD           A,(HL)
0329: 28 02      JR           Z,$32D
032B: 2F         CPL
032C: 3C         INC         A
032D: F5         PUSH       AF
032E: 21 96 FF   LD           HL,$FF96
0331: 86         ADD         A,(HL)
0332: E0 43      LDFF00   ($43),A
0334: F1         POP         AF
0335: 21 97 FF   LD           HL,$FF97
0338: 86         ADD         A,(HL)
0339: E0 42      LDFF00   ($42),A
033B: C3 DE 02   JP           $02DE
033E: CD 44 08   CALL       $0844
0341: FA 97 DB   LD           A,($DB97)
0344: E0 47      LDFF00   ($47),A
0346: FA 98 DB   LD           A,($DB98)
0349: E0 48      LDFF00   ($48),A
034B: FA 99 DB   LD           A,($DB99)
034E: E0 49      LDFF00   ($49),A
0350: 18 6B      JR           $3BD
0352: FA 9A DB   LD           A,($DB9A)
0355: E0 4A      LDFF00   ($4A),A
0357: FA 97 DB   LD           A,($DB97)
035A: E0 47      LDFF00   ($47),A
035C: FA 98 DB   LD           A,($DB98)
035F: E0 48      LDFF00   ($48),A
0361: FA 99 DB   LD           A,($DB99)
0364: E0 49      LDFF00   ($49),A
0366: CD 44 08   CALL       $0844
0369: CD FE 27   CALL       $27FE
036C: F0 90      LD           A,($90)
036E: 21 91 FF   LD           HL,$FF91
0371: B6         OR           (HL)
0372: 21 0E C1   LD           HL,$C10E
0375: B6         OR           (HL)
0376: 20 45      JR           NZ,$3BD
0378: FA 03 00   LD           A,($0003)
037B: A7         AND         A
037C: 28 2C      JR           Z,$3AA
037E: FA FC D6   LD           A,($D6FC)
0381: A7         AND         A
0382: 20 06      JR           NZ,$38A
0384: F0 CB      LD           A,($CB)
0386: E6 0F      AND         $0F
0388: 28 1A      JR           Z,$3A4
038A: F0 CC      LD           A,($CC)
038C: E6 40      AND         $40
038E: 28 14      JR           Z,$3A4
0390: FA FC D6   LD           A,($D6FC)
0393: EE 01      XOR         $01
0395: EA FC D6   LD           ($D6FC),A
0398: 20 23      JR           NZ,$3BD
039A: FA 7B C1   LD           A,($C17B)
039D: EE 10      XOR         $10
039F: EA 7B C1   LD           ($C17B),A
03A2: 18 19      JR           $3BD
03A4: FA FC D6   LD           A,($D6FC)
03A7: A7         AND         A
03A8: 20 13      JR           NZ,$3BD
03AA: 3E 01      LD           A,$01
03AC: CD B9 07   CALL       $07B9
03AF: CD F0 5C   CALL       $5CF0
03B2: CD 90 0A   CALL       $0A90
03B5: 3E 01      LD           A,$01
03B7: EA 00 21   LD           ($2100),A
03BA: CD 03 5D   CALL       $5D03
03BD: 3E 1F      LD           A,$1F
03BF: EA 00 21   LD           ($2100),A
03C2: CD 80 7F   CALL       $7F80
03C5: 3E 0C      LD           A,$0C
03C7: EA 00 21   LD           ($2100),A
03CA: AF         XOR         A
03CB: E0 FD      LDFF00   ($FD),A
03CD: 76         HALT
03CE: F0 D1      LD           A,($D1)
03D0: A7         AND         A
03D1: 28 FB      JR           Z,$3CE
03D3: AF         XOR         A
03D4: E0 D1      LDFF00   ($D1),A
03D6: C3 A6 01   JP           $01A6
03D9: 20 30      JR           NZ,$40B
03DB: 40         LD           B,B
03DC: 60         LD           H,B
03DD: 00         NOP
03DE: 30 56      JR           NC,$436
03E0: 68         LD           L,B
03E1: 00         NOP
03E2: F3         DI
03E3: F5         PUSH       AF
03E4: E5         PUSH       HL
03E5: D5         PUSH       DE
03E6: FA 95 DB   LD           A,($DB95)
03E9: FE 01      CP           $01
03EB: 20 13      JR           NZ,$400
03ED: FA 96 DB   LD           A,($DB96)
03F0: FE 05      CP           $05
03F2: 20 05      JR           NZ,$3F9
03F4: FA 00 D0   LD           A,($D000)
03F7: 18 02      JR           $3FB
03F9: F0 97      LD           A,($97)
03FB: E0 42      LDFF00   ($42),A
03FD: C3 52 04   JP           $0452
0400: FE 00      CP           $00
0402: 20 4B      JR           NZ,$44F
0404: FA 05 C1   LD           A,($C105)
0407: 5F         LD           E,A
0408: 16 00      LD           D,$00
040A: 21 00 C1   LD           HL,$C100
040D: 19         ADD         HL,DE
040E: 7E         LD           A,(HL)
040F: 21 96 FF   LD           HL,$FF96
0412: 86         ADD         A,(HL)
0413: E0 43      LDFF00   ($43),A
0415: FA 96 DB   LD           A,($DB96)
0418: FE 06      CP           $06
041A: 38 10      JR           C,$42C
041C: 21 DE 03   LD           HL,$03DE
041F: 19         ADD         HL,DE
0420: 7E         LD           A,(HL)
0421: E0 45      LDFF00   ($45),A
0423: 7B         LD           A,E
0424: 3C         INC         A
0425: E6 03      AND         $03
0427: EA 05 C1   LD           ($C105),A
042A: 18 26      JR           $452
042C: 21 D9 03   LD           HL,$03D9
042F: 19         ADD         HL,DE
0430: 7E         LD           A,(HL)
0431: E0 45      LDFF00   ($45),A
0433: 7B         LD           A,E
0434: 3C         INC         A
0435: FE 05      CP           $05
0437: 20 01      JR           NZ,$43A
0439: AF         XOR         A
043A: EA 05 C1   LD           ($C105),A
043D: 00         NOP
043E: FE 04      CP           $04
0440: 20 0B      JR           NZ,$44D
0442: FA 06 C1   LD           A,($C106)
0445: E0 42      LDFF00   ($42),A
0447: 2F         CPL
0448: 3C         INC         A
0449: C6 60      ADD         $60
044B: E0 45      LDFF00   ($45),A
044D: 18 03      JR           $452
044F: AF         XOR         A
0450: E0 43      LDFF00   ($43),A
0452: D1         POP         DE
0453: E1         POP         HL
0454: F1         POP         AF
0455: FB         EI
0456: D9         RETI
0457: 00         NOP
0458: 00         NOP
0459: A5         AND         L
045A: 62         LD           H,D
045B: 13         INC         DE
045C: 73         LD           (HL),E
045D: 0F         RRCA
045E: 6F         LD           L,A
045F: 01 6F 1E   LD           BC,$1E6F
0462: 70         LD           (HL),B
0463: 54         LD           D,H
0464: 71         LD           (HL),C
0465: 51         LD           D,C
0466: D6 C2      SUB         $C2
0468: 6E         LD           L,(HL)
0469: 93         SUB         E
046A: 73         LD           (HL),E
046B: 59         LD           E,C
046C: 75         LD           (HL),L
046D: C0         RET         NZ
046E: 74         LD           (HL),H
046F: 2B         DEC         HL
0470: 72         LD           (HL),D
0471: 37         SCF
0472: 76         HALT
0473: B7         OR           A
0474: 76         HALT
0475: 00         NOP
0476: 78         LD           A,B
0477: 0B         DEC         BC
0478: 7A         LD           A,D
0479: 8A         ADC         A,D
047A: 7B         LD           A,E
047B: AF         XOR         A
047C: 54         LD           D,H
047D: 70         LD           (HL),B
047E: 56         LD           D,(HL)
047F: 81         ADD         A,C
0480: 6E         LD           L,(HL)
0481: 10 53      STOP       $53
0483: 65         LD           H,L
0484: 63         LD           H,E
0485: CE 66      ADC         $66
0487: A1         AND         C
0488: 67         LD           H,A
0489: E5         PUSH       HL
048A: 68         LD           L,B
048B: 34         INC         (HL)
048C: 6A         LD           L,D
048D: 20 6B      JR           NZ,$4FA
048F: DD                              
0490: 6B         LD           L,E
0491: DD                              
0492: 6B         LD           L,E
0493: 73         LD           (HL),E
0494: 5A         LD           E,D
0495: 29         ADD         HL,HL
0496: 5C         LD           E,H
0497: C8         RET         Z
0498: 5D         LD           E,L
0499: 67         LD           H,A
049A: 5F         LD           E,A
049B: 06 61      LD           B,$61
049D: 0E 58      LD           C,$58
049F: AD         XOR         L
04A0: 59         LD           E,C
04A1: FA FE D6   LD           A,($D6FE)
04A4: A7         AND         A
04A5: 28 4E      JR           Z,$4F5
04A7: F5         PUSH       AF
04A8: CD 81 28   CALL       $2881
04AB: F1         POP         AF
04AC: CD B1 04   CALL       $04B1
04AF: 18 65      JR           $516
04B1: 3D         DEC         A
04B2: C7         RST         0X00
04B3: 6C         LD           L,H
04B4: 2E A8      LD           L,$A8
04B6: 28 6B      JR           Z,$523
04B8: 2B         DEC         HL
04B9: 9F         SBC         A
04BA: 2B         DEC         HL
04BB: 7E         LD           A,(HL)
04BC: 2C         INC         L
04BD: C4 2B 7E   CALL       NZ,$7E2B
04C0: 2C         INC         L
04C1: A1         AND         C
04C2: 28 88      JR           Z,$44C
04C4: 2D         DEC         L
04C5: 22         LD           (HLI),A
04C6: 05         DEC         B
04C7: 01 2D 22   LD           BC,$222D
04CA: 05         DEC         B
04CB: 73         LD           (HL),E
04CC: 2D         DEC         L
04CD: DB                              
04CE: 37         SCF
04CF: 98         SBC         B
04D0: 28 C2      JR           Z,$494
04D2: 2C         INC         L
04D3: F0 2C      LD           A,($2C)
04D5: 28 2D      JR           Z,$504
04D7: 56         LD           D,(HL)
04D8: 2D         DEC         L
04D9: 1E 2D      LD           E,$2D
04DB: 26 2A      LD           H,$2A
04DD: A2         AND         D
04DE: 2A         LD           A,(HLI)
04DF: 9D         SBC         L
04E0: 2A         LD           A,(HLI)
04E1: 98         SBC         B
04E2: 2A         LD           A,(HLI)
04E3: F7         RST         0X30
04E4: 2A         LD           A,(HLI)
04E5: F2                              
04E6: 2A         LD           A,(HLI)
04E7: BF         CP           A
04E8: 2A         LD           A,(HLI)
04E9: F2                              
04EA: 2A         LD           A,(HLI)
04EB: 65         LD           H,L
04EC: 2A         LD           A,(HLI)
04ED: FA 29 17   LD           A,($1729)
04F0: 2A         LD           A,(HLI)
04F1: 23         INC         HL
04F2: 2D         DEC         L
04F3: 39         ADD         HL,SP
04F4: 2D         DEC         L
04F5: CD 81 28   CALL       $2881
04F8: 21 57 04   LD           HL,$0457
04FB: 06 00      LD           B,$00
04FD: FA FF D6   LD           A,($D6FF)
0500: CB 27      SLA         A
0502: 4F         LD           C,A
0503: 09         ADD         HL,BC
0504: 7E         LD           A,(HL)
0505: 5F         LD           E,A
0506: 23         INC         HL
0507: 7E         LD           A,(HL)
0508: 57         LD           D,A
0509: 3E 08      LD           A,$08
050B: EA 00 21   LD           ($2100),A
050E: CD DE 28   CALL       $28DE
0511: 3E 0C      LD           A,$0C
0513: EA 00 21   LD           ($2100),A
0516: AF         XOR         A
0517: EA FF D6   LD           ($D6FF),A
051A: EA FE D6   LD           ($D6FE),A
051D: FA FD D6   LD           A,($D6FD)
0520: E0 40      LDFF00   ($40),A
0522: C9         RET
0523: 07         RLCA
0524: 09         ADD         HL,BC
0525: F5         PUSH       AF
0526: C5         PUSH       BC
0527: D5         PUSH       DE
0528: E5         PUSH       HL
0529: F3         DI
052A: F0 FD      LD           A,($FD)
052C: A7         AND         A
052D: C2 B6 05   JP           NZ,$05B6
0530: FA 9F C1   LD           A,($C19F)
0533: E6 7F      AND         $7F
0535: 28 2F      JR           Z,$566
0537: FE 01      CP           $01
0539: 28 2B      JR           Z,$566
053B: FE 05      CP           $05
053D: 30 09      JR           NC,$548
053F: CD DF 21   CALL       $21DF
0542: 21 9F C1   LD           HL,$C19F
0545: 34         INC         (HL)
0546: 18 6E      JR           $5B6
0548: FE 0A      CP           $0A
054A: 20 05      JR           NZ,$551
054C: CD A5 25   CALL       $25A5
054F: 18 65      JR           $5B6
0551: FE 0B      CP           $0B
0553: 20 11      JR           NZ,$566
0555: FA 72 C1   LD           A,($C172)
0558: A7         AND         A
0559: 28 06      JR           Z,$561
055B: 3D         DEC         A
055C: EA 72 C1   LD           ($C172),A
055F: 18 05      JR           $566
0561: CD F9 25   CALL       $25F9
0564: 18 50      JR           $5B6
0566: FA FE D6   LD           A,($D6FE)
0569: A7         AND         A
056A: 20 4A      JR           NZ,$5B6
056C: F0 90      LD           A,($90)
056E: E0 E8      LDFF00   ($E8),A
0570: 21 91 FF   LD           HL,$FF91
0573: B6         OR           (HL)
0574: 21 0E C1   LD           HL,$C10E
0577: B6         OR           (HL)
0578: 28 11      JR           Z,$58B
057A: CD C0 05   CALL       $05C0
057D: F0 E8      LD           A,($E8)
057F: FE 08      CP           $08
0581: 30 03      JR           NC,$586
0583: CD CC 1C   CALL       $1CCC
0586: CD C0 FF   CALL       $FFC0
0589: 18 2B      JR           $5B6
058B: F0 BB      LD           A,($BB)
058D: A7         AND         A
058E: 28 13      JR           Z,$5A3
0590: 3D         DEC         A
0591: E0 BB      LDFF00   ($BB),A
0593: 5F         LD           E,A
0594: 16 00      LD           D,$00
0596: 21 23 05   LD           HL,$0523
0599: 19         ADD         HL,DE
059A: 7E         LD           A,(HL)
059B: EA F8 D6   LD           ($D6F8),A
059E: CD EE 1D   CALL       $1DEE
05A1: 18 E0      JR           $583
05A3: CD A9 1A   CALL       $1AA9
05A6: 11 01 D6   LD           DE,$D601
05A9: CD D8 28   CALL       $28D8
05AC: AF         XOR         A
05AD: EA 00 D6   LD           ($D600),A
05B0: EA 01 D6   LD           ($D601),A
05B3: CD C0 FF   CALL       $FFC0
05B6: FB         EI
05B7: E1         POP         HL
05B8: D1         POP         DE
05B9: C1         POP         BC
05BA: 3E 01      LD           A,$01
05BC: E0 D1      LDFF00   ($D1),A
05BE: F1         POP         AF
05BF: D9         RETI
05C0: F0 90      LD           A,($90)
05C2: A7         AND         A
05C3: CA 88 06   JP           Z,$0688
05C6: FE 07      CP           $07
05C8: CA 60 07   JP           Z,$0760
05CB: FE 03      CP           $03
05CD: CA 62 00   JP           Z,$0062
05D0: FE 04      CP           $04
05D2: CA 6A 00   JP           Z,$006A
05D5: FE 05      CP           $05
05D7: CA 72 00   JP           Z,$0072
05DA: FE 06      CP           $06
05DC: CA 7A 00   JP           Z,$007A
05DF: FE 08      CP           $08
05E1: D2 83 07   JP           NC,$0783
05E4: FA A5 DB   LD           A,($DBA5)
05E7: A7         AND         A
05E8: 28 59      JR           Z,$643
05EA: F0 90      LD           A,($90)
05EC: FE 02      CP           $02
05EE: CA C9 07   JP           Z,$07C9
05F1: 3E 0D      LD           A,$0D
05F3: EA 00 21   LD           ($2100),A
05F6: F0 92      LD           A,($92)
05F8: 4F         LD           C,A
05F9: 06 00      LD           B,$00
05FB: CB 21      SLA         C
05FD: CB 10      RL           B
05FF: CB 21      SLA         C
0601: CB 10      RL           B
0603: CB 21      SLA         C
0605: CB 10      RL           B
0607: CB 21      SLA         C
0609: CB 10      RL           B
060B: CB 21      SLA         C
060D: CB 10      RL           B
060F: CB 21      SLA         C
0611: CB 10      RL           B
0613: 21 00 90   LD           HL,$9000
0616: 09         ADD         HL,BC
0617: E5         PUSH       HL
0618: D1         POP         DE
0619: 21 00 50   LD           HL,$5000
061C: F0 94      LD           A,($94)
061E: C6 50      ADD         $50
0620: 67         LD           H,A
0621: 09         ADD         HL,BC
0622: F0 BB      LD           A,($BB)
0624: A7         AND         A
0625: 28 07      JR           Z,$62E
0627: F0 92      LD           A,($92)
0629: 3D         DEC         A
062A: FE 02      CP           $02
062C: 38 06      JR           C,$634
062E: 01 40 00   LD           BC,$0040
0631: CD C5 28   CALL       $28C5
0634: F0 92      LD           A,($92)
0636: 3C         INC         A
0637: E0 92      LDFF00   ($92),A
0639: FE 04      CP           $04
063B: 20 05      JR           NZ,$642
063D: AF         XOR         A
063E: E0 90      LDFF00   ($90),A
0640: E0 92      LDFF00   ($92),A
0642: C9         RET
0643: 21 00 21   LD           HL,$2100
0646: 36 0F      LD           (HL),$0F
0648: F0 92      LD           A,($92)
064A: 4F         LD           C,A
064B: 06 00      LD           B,$00
064D: CB 21      SLA         C
064F: CB 10      RL           B
0651: CB 21      SLA         C
0653: CB 10      RL           B
0655: CB 21      SLA         C
0657: CB 10      RL           B
0659: CB 21      SLA         C
065B: CB 10      RL           B
065D: CB 21      SLA         C
065F: CB 10      RL           B
0661: CB 21      SLA         C
0663: CB 10      RL           B
0665: 21 00 90   LD           HL,$9000
0668: 09         ADD         HL,BC
0669: E5         PUSH       HL
066A: D1         POP         DE
066B: F0 94      LD           A,($94)
066D: C6 40      ADD         $40
066F: 67         LD           H,A
0670: 2E 00      LD           L,$00
0672: 09         ADD         HL,BC
0673: 01 40 00   LD           BC,$0040
0676: CD C5 28   CALL       $28C5
0679: F0 92      LD           A,($92)
067B: 3C         INC         A
067C: E0 92      LDFF00   ($92),A
067E: FE 08      CP           $08
0680: 20 05      JR           NZ,$687
0682: AF         XOR         A
0683: E0 90      LDFF00   ($90),A
0685: E0 92      LDFF00   ($92),A
0687: C9         RET
0688: F0 91      LD           A,($91)
068A: A7         AND         A
068B: 28 67      JR           Z,$6F4
068D: FA 97 C1   LD           A,($C197)
0690: 5F         LD           E,A
0691: 16 00      LD           D,$00
0693: 21 93 C1   LD           HL,$C193
0696: 19         ADD         HL,DE
0697: 7E         LD           A,(HL)
0698: F5         PUSH       AF
0699: E6 3F      AND         $3F
069B: 57         LD           D,A
069C: 1E 00      LD           E,$00
069E: F1         POP         AF
069F: CB 37      SWAP       A
06A1: 1F         RRA
06A2: 1F         RRA
06A3: E6 03      AND         $03
06A5: 4F         LD           C,A
06A6: 06 00      LD           B,$00
06A8: 21 84 2D   LD           HL,$2D84
06AB: 09         ADD         HL,BC
06AC: 7E         LD           A,(HL)
06AD: EA 00 21   LD           ($2100),A
06B0: F0 93      LD           A,($93)
06B2: 4F         LD           C,A
06B3: 06 00      LD           B,$00
06B5: CB 21      SLA         C
06B7: CB 10      RL           B
06B9: CB 21      SLA         C
06BB: CB 10      RL           B
06BD: CB 21      SLA         C
06BF: CB 10      RL           B
06C1: CB 21      SLA         C
06C3: CB 10      RL           B
06C5: CB 21      SLA         C
06C7: CB 10      RL           B
06C9: CB 21      SLA         C
06CB: CB 10      RL           B
06CD: 21 00 40   LD           HL,$4000
06D0: 09         ADD         HL,BC
06D1: 19         ADD         HL,DE
06D2: E5         PUSH       HL
06D3: FA 97 C1   LD           A,($C197)
06D6: 57         LD           D,A
06D7: 21 00 84   LD           HL,$8400
06DA: 09         ADD         HL,BC
06DB: 19         ADD         HL,DE
06DC: E5         PUSH       HL
06DD: D1         POP         DE
06DE: E1         POP         HL
06DF: 01 40 00   LD           BC,$0040
06E2: CD C5 28   CALL       $28C5
06E5: F0 93      LD           A,($93)
06E7: 3C         INC         A
06E8: E0 93      LDFF00   ($93),A
06EA: FE 04      CP           $04
06EC: 20 05      JR           NZ,$6F3
06EE: AF         XOR         A
06EF: E0 91      LDFF00   ($91),A
06F1: E0 93      LDFF00   ($93),A
06F3: C9         RET
06F4: FA 0D C1   LD           A,($C10D)
06F7: 5F         LD           E,A
06F8: 16 00      LD           D,$00
06FA: 21 93 C1   LD           HL,$C193
06FD: 19         ADD         HL,DE
06FE: 7E         LD           A,(HL)
06FF: F5         PUSH       AF
0700: E6 3F      AND         $3F
0702: 57         LD           D,A
0703: 1E 00      LD           E,$00
0705: F1         POP         AF
0706: CB 37      SWAP       A
0708: 1F         RRA
0709: 1F         RRA
070A: E6 03      AND         $03
070C: 4F         LD           C,A
070D: 06 00      LD           B,$00
070F: 21 84 2D   LD           HL,$2D84
0712: 09         ADD         HL,BC
0713: 7E         LD           A,(HL)
0714: EA 00 21   LD           ($2100),A
0717: FA 0F C1   LD           A,($C10F)
071A: 4F         LD           C,A
071B: 06 00      LD           B,$00
071D: CB 21      SLA         C
071F: CB 10      RL           B
0721: CB 21      SLA         C
0723: CB 10      RL           B
0725: CB 21      SLA         C
0727: CB 10      RL           B
0729: CB 21      SLA         C
072B: CB 10      RL           B
072D: CB 21      SLA         C
072F: CB 10      RL           B
0731: CB 21      SLA         C
0733: CB 10      RL           B
0735: 21 00 40   LD           HL,$4000
0738: 09         ADD         HL,BC
0739: 19         ADD         HL,DE
073A: E5         PUSH       HL
073B: FA 0D C1   LD           A,($C10D)
073E: 57         LD           D,A
073F: 21 00 84   LD           HL,$8400
0742: 09         ADD         HL,BC
0743: 19         ADD         HL,DE
0744: E5         PUSH       HL
0745: D1         POP         DE
0746: E1         POP         HL
0747: 01 40 00   LD           BC,$0040
074A: CD C5 28   CALL       $28C5
074D: FA 0F C1   LD           A,($C10F)
0750: 3C         INC         A
0751: EA 0F C1   LD           ($C10F),A
0754: FE 04      CP           $04
0756: 20 07      JR           NZ,$75F
0758: AF         XOR         A
0759: EA 0E C1   LD           ($C10E),A
075C: EA 0F C1   LD           ($C10F),A
075F: C9         RET
0760: 3E 01      LD           A,$01
0762: EA 00 21   LD           ($2100),A
0765: CD C5 7B   CALL       $7BC5
0768: C3 8B 00   JP           $008B
076B: 60         LD           H,B
076C: 69         LD           L,C
076D: A0         AND         B
076E: 69         LD           L,C
076F: C0         RET         NZ
0770: 69         LD           L,C
0771: 00         NOP
0772: 42         LD           B,D
0773: 40         LD           B,B
0774: 42         LD           B,D
0775: 60         LD           H,B
0776: 42         LD           B,D
0777: 00         NOP
0778: 82         ADD         A,D
0779: 40         LD           B,B
077A: 82         ADD         A,D
077B: 60         LD           H,B
077C: 82         ADD         A,D
077D: 00         NOP
077E: 82         ADD         A,D
077F: 40         LD           B,B
0780: 82         ADD         A,D
0781: 60         LD           H,B
0782: 82         ADD         A,D
0783: D6 08      SUB         $08
0785: CB 27      SLA         A
0787: 5F         LD           E,A
0788: 16 00      LD           D,$00
078A: 21 6B 07   LD           HL,$076B
078D: 19         ADD         HL,DE
078E: E5         PUSH       HL
078F: 21 77 07   LD           HL,$0777
0792: 19         ADD         HL,DE
0793: 5E         LD           E,(HL)
0794: 23         INC         HL
0795: 56         LD           D,(HL)
0796: E1         POP         HL
0797: 2A         LD           A,(HLI)
0798: 66         LD           H,(HL)
0799: 6F         LD           L,A
079A: 3E 0C      LD           A,$0C
079C: EA 00 21   LD           ($2100),A
079F: 01 40 00   LD           BC,$0040
07A2: CD C5 28   CALL       $28C5
07A5: F0 90      LD           A,($90)
07A7: FE 0A      CP           $0A
07A9: 28 0A      JR           Z,$7B5
07AB: FE 0D      CP           $0D
07AD: 28 06      JR           Z,$7B5
07AF: F0 90      LD           A,($90)
07B1: 3C         INC         A
07B2: E0 90      LDFF00   ($90),A
07B4: C9         RET
07B5: AF         XOR         A
07B6: E0 90      LDFF00   ($90),A
07B8: C9         RET

; Switch to bank A (remember bank number)
SwitchBank:
07B9: EA 00 21   LD           ($2100),A ; Switch to bank A
07BC: EA AF DB   LD           ($DBAF),A ; Remember what bank we are in
07BF: C9         RET ; Back

SwitchBankSave:
07C0: F5         PUSH       AF
07C1: FA AF DB   LD           A,($DBAF)
07C4: EA 00 21   LD           ($2100),A
07C7: F1         POP         AF
07C8: C9         RET
     
07C9: 3E 12      LD           A,$12
07CB: EA 00 21   LD           ($2100),A
07CE: F0 92      LD           A,($92)
07D0: FE 08      CP           $08
07D2: 38 3F      JR           C,$813
07D4: 20 0D      JR           NZ,$7E3
07D6: 3E 02      LD           A,$02
07D8: EA 00 21   LD           ($2100),A
07DB: CD B8 6B   CALL       $6BB8
07DE: 21 92 FF   LD           HL,$FF92
07E1: 34         INC         (HL)
07E2: C9         RET
07E3: FE 09      CP           $09
07E5: 20 0D      JR           NZ,$7F4
07E7: 3E 02      LD           A,$02
07E9: EA 00 21   LD           ($2100),A
07EC: CD 92 6B   CALL       $6B92
07EF: 21 92 FF   LD           HL,$FF92
07F2: 34         INC         (HL)
07F3: C9         RET
07F4: FE 0A      CP           $0A
07F6: 20 0D      JR           NZ,$805
07F8: 3E 02      LD           A,$02
07FA: EA 00 21   LD           ($2100),A
07FD: CD 6C 6B   CALL       $6B6C
0800: 21 92 FF   LD           HL,$FF92
0803: 34         INC         (HL)
0804: C9         RET
0805: 3E 02      LD           A,$02
0807: EA 00 21   LD           ($2100),A
080A: CD 46 6B   CALL       $6B46
080D: AF         XOR         A
080E: E0 90      LDFF00   ($90),A
0810: E0 92      LDFF00   ($92),A
0812: C9         RET
0813: 4F         LD           C,A
0814: 06 00      LD           B,$00
0816: CB 21      SLA         C
0818: CB 10      RL           B
081A: CB 21      SLA         C
081C: CB 10      RL           B
081E: CB 21      SLA         C
0820: CB 10      RL           B
0822: CB 21      SLA         C
0824: CB 10      RL           B
0826: CB 21      SLA         C
0828: CB 10      RL           B
082A: CB 21      SLA         C
082C: CB 10      RL           B
082E: 21 00 8D   LD           HL,$8D00
0831: 09         ADD         HL,BC
0832: E5         PUSH       HL
0833: D1         POP         DE
0834: 21 00 7E   LD           HL,$7E00
0837: 09         ADD         HL,BC
0838: 01 40 00   LD           BC,$0040
083B: CD C5 28   CALL       $28C5
083E: F0 92      LD           A,($92)
0840: 3C         INC         A
0841: E0 92      LDFF00   ($92),A
0843: C9         RET
0844: 3E 1F      LD           A,$1F
0846: EA 00 21   LD           ($2100),A
0849: CD 06 40   CALL       $4006
084C: F0 F3      LD           A,($F3)
084E: A7         AND         A
084F: 20 25      JR           NZ,$876
0851: FA 0B C1   LD           A,($C10B)
0854: A7         AND         A
0855: 28 0F      JR           Z,$866
0857: FE 02      CP           $02
0859: 20 08      JR           NZ,$863
085B: F0 E7      LD           A,($E7)
085D: E6 01      AND         $01
085F: 20 15      JR           NZ,$876
0861: 18 03      JR           $866
0863: CD 66 08   CALL       $0866
0866: 3E 1B      LD           A,$1B
0868: EA 00 21   LD           ($2100),A
086B: CD 06 40   CALL       $4006
086E: 3E 1E      LD           A,$1E
0870: EA 00 21   LD           ($2100),A
0873: CD 06 40   CALL       $4006
0876: C9         RET
0877: FF         RST         0X38
0878: FF         RST         0X38
0879: FF         RST         0X38
087A: FF         RST         0X38
087B: FF         RST         0X38
087C: 3E 02      LD           A,$02
087E: EA 00 21   LD           ($2100),A
0881: CD EF 19   CALL       $19EF
0884: C3 C0 07   JP           $07C0
0887: 21 50 C4   LD           HL,$C450
088A: 18 08      JR           $894
088C: 21 F0 C2   LD           HL,$C2F0
088F: 18 03      JR           $894
0891: 21 E0 C2   LD           HL,$C2E0
0894: 09         ADD         HL,BC
0895: 7E         LD           A,(HL)
0896: A7         AND         A
0897: C9         RET
0898: 3E AF      LD           A,$AF
089A: CD 01 3C   CALL       $3C01
089D: F0 98      LD           A,($98)
089F: 21 00 C2   LD           HL,$C200
08A2: 19         ADD         HL,DE
08A3: 77         LD           (HL),A
08A4: F0 99      LD           A,($99)
08A6: 21 10 C2   LD           HL,$C210
08A9: 19         ADD         HL,DE
08AA: 77         LD           (HL),A
08AB: C9         RET
08AC: 3E 1D      LD           A,$1D
08AE: E0 F2      LDFF00   ($F2),A
08B0: C9         RET
08B1: 21 E1 45   LD           HL,$45E1
08B4: 18 03      JR           $8B9
08B6: 21 E1 46   LD           HL,$46E1
08B9: 3E 1C      LD           A,$1C
08BB: EA 00 21   LD           ($2100),A
08BE: 09         ADD         HL,BC
08BF: 7E         LD           A,(HL)
08C0: 21 00 21   LD           HL,$2100
08C3: 36 01      LD           (HL),$01
08C5: C9         RET
08C6: 3E 0C      LD           A,$0C
08C8: EA 00 21   LD           ($2100),A
08CB: 01 40 00   LD           BC,$0040
08CE: CD C5 28   CALL       $28C5
08D1: 3E 01      LD           A,$01
08D3: EA 00 21   LD           ($2100),A
08D6: C9         RET
08D7: 21 F4 FF   LD           HL,$FFF4
08DA: 36 0C      LD           (HL),$0C
08DC: 21 02 C5   LD           HL,$C502
08DF: 36 04      LD           (HL),$04
08E1: C9         RET
08E2: 21 10 C4   LD           HL,$C410
08E5: 09         ADD         HL,BC
08E6: 7E         LD           A,(HL)
08E7: A7         AND         A
08E8: 28 01      JR           Z,$8EB
08EA: 35         DEC         (HL)
08EB: C9         RET
08EC: F5         PUSH       AF
08ED: FA 8F C1   LD           A,($C18F)
08F0: A7         AND         A
08F1: 20 14      JR           NZ,$907
08F3: EA CF C1   LD           ($C1CF),A
08F6: 3C         INC         A
08F7: EA 8F C1   LD           ($C18F),A
08FA: EA A6 C5   LD           ($C5A6),A
08FD: FA 9D C1   LD           A,($C19D)
0900: A7         AND         A
0901: 20 04      JR           NZ,$907
0903: 3E 02      LD           A,$02
0905: E0 F2      LDFF00   ($F2),A
0907: F1         POP         AF
0908: C9         RET
0909: 3E 30      LD           A,$30
090B: E0 A8      LDFF00   ($A8),A
090D: 18 17      JR           $926
090F: 3E 30      LD           A,$30
0911: E0 A8      LDFF00   ($A8),A
0913: 18 15      JR           $92A
0915: FA 01 D4   LD           A,($D401)
0918: FE 01      CP           $01
091A: 20 ED      JR           NZ,$909
091C: FA A5 DB   LD           A,($DBA5)
091F: A7         AND         A
0920: 28 E7      JR           Z,$909
0922: 3E 01      LD           A,$01
0924: E0 BC      LDFF00   ($BC),A
0926: 3E 06      LD           A,$06
0928: E0 F4      LDFF00   ($F4),A
092A: 3E 03      LD           A,$03
092C: EA 1C C1   LD           ($C11C),A
092F: AF         XOR         A
0930: EA 6B C1   LD           ($C16B),A
0933: EA 6C C1   LD           ($C16C),A
0936: EA 78 D4   LD           ($D478),A
0939: A7         AND         A
093A: C9         RET
093B: AF         XOR         A
093C: EA 21 C1   LD           ($C121),A
093F: EA 22 C1   LD           ($C122),A
0942: AF         XOR         A
0943: EA 4B C1   LD           ($C14B),A
0946: EA 4A C1   LD           ($C14A),A
0949: C9         RET
094A: F0 9F      LD           A,($9F)
094C: E0 98      LDFF00   ($98),A
094E: F0 A0      LD           A,($A0)
0950: E0 99      LDFF00   ($99),A
0952: C9         RET
0953: F5         PUSH       AF
0954: 1E 0F      LD           E,$0F
0956: 16 00      LD           D,$00
0958: 21 10 C5   LD           HL,$C510
095B: 19         ADD         HL,DE
095C: 7E         LD           A,(HL)
095D: A7         AND         A
095E: 28 18      JR           Z,$978
0960: 1D         DEC         E
0961: 7B         LD           A,E
0962: FE FF      CP           $FF
0964: 20 F2      JR           NZ,$958
0966: 21 C0 C5   LD           HL,$C5C0
0969: 35         DEC         (HL)
096A: 7E         LD           A,(HL)
096B: FE FF      CP           $FF
096D: 20 05      JR           NZ,$974
096F: 3E 0F      LD           A,$0F
0971: EA C0 C5   LD           ($C5C0),A
0974: FA C0 C5   LD           A,($C5C0)
0977: 5F         LD           E,A
0978: F1         POP         AF
0979: 21 10 C5   LD           HL,$C510
097C: 19         ADD         HL,DE
097D: 77         LD           (HL),A
097E: F0 D8      LD           A,($D8)
0980: 21 40 C5   LD           HL,$C540
0983: 19         ADD         HL,DE
0984: 77         LD           (HL),A
0985: F0 D7      LD           A,($D7)
0987: 21 30 C5   LD           HL,$C530
098A: 19         ADD         HL,DE
098B: 77         LD           (HL),A
098C: 21 20 C5   LD           HL,$C520
098F: 19         ADD         HL,DE
0990: 36 0F      LD           (HL),$0F
0992: C9         RET
0993: FA 40 C1   LD           A,($C140)
0996: D6 08      SUB         $08
0998: E0 D7      LDFF00   ($D7),A
099A: FA 42 C1   LD           A,($C142)
099D: D6 08      SUB         $08
099F: E0 D8      LDFF00   ($D8),A
09A1: 3E 07      LD           A,$07
09A3: E0 F2      LDFF00   ($F2),A
09A5: 3E 05      LD           A,$05
09A7: C3 53 09   JP           $0953
09AA: 3E 08      LD           A,$08
09AC: EA 00 21   LD           ($2100),A
09AF: FA A5 DB   LD           A,($DBA5)
09B2: A7         AND         A
09B3: 28 27      JR           Z,$9DC
09B5: F0 F6      LD           A,($F6)
09B7: 5F         LD           E,A
09B8: 16 00      LD           D,$00
09BA: 21 40 40   LD           HL,$4040
09BD: F0 F7      LD           A,($F7)
09BF: FE 1A      CP           $1A
09C1: 30 05      JR           NC,$9C8
09C3: FE 06      CP           $06
09C5: 38 01      JR           C,$9C8
09C7: 24         INC         H
09C8: 19         ADD         HL,DE
09C9: F0 94      LD           A,($94)
09CB: 5F         LD           E,A
09CC: 7E         LD           A,(HL)
09CD: BB         CP           E
09CE: 28 0A      JR           Z,$9DA
09D0: E0 94      LDFF00   ($94),A
09D2: FE FF      CP           $FF
09D4: 28 04      JR           Z,$9DA
09D6: 3E 01      LD           A,$01
09D8: E0 90      LDFF00   ($90),A
09DA: 18 2D      JR           $A09
09DC: F0 F6      LD           A,($F6)
09DE: FE 07      CP           $07
09E0: 20 01      JR           NZ,$9E3
09E2: 3C         INC         A
09E3: 57         LD           D,A
09E4: CB 3F      SRL         A
09E6: CB 3F      SRL         A
09E8: E6 F8      AND         $F8
09EA: 5F         LD           E,A
09EB: 7A         LD           A,D
09EC: CB 3F      SRL         A
09EE: E6 07      AND         $07
09F0: B3         OR           E
09F1: 5F         LD           E,A
09F2: 16 00      LD           D,$00
09F4: 21 00 40   LD           HL,$4000
09F7: 19         ADD         HL,DE
09F8: F0 94      LD           A,($94)
09FA: 5F         LD           E,A
09FB: 7E         LD           A,(HL)
09FC: BB         CP           E
09FD: 28 0A      JR           Z,$A09
09FF: FE 0F      CP           $0F
0A01: 28 06      JR           Z,$A09
0A03: E0 94      LDFF00   ($94),A
0A05: 3E 01      LD           A,$01
0A07: E0 90      LDFF00   ($90),A
0A09: AF         XOR         A
0A0A: E0 D7      LDFF00   ($D7),A
0A0C: F0 F6      LD           A,($F6)
0A0E: 5F         LD           E,A
0A0F: 16 00      LD           D,$00
0A11: 21 40 42   LD           HL,$4240
0A14: FA A5 DB   LD           A,($DBA5)
0A17: 57         LD           D,A
0A18: F0 F7      LD           A,($F7)
0A1A: FE 1A      CP           $1A
0A1C: 30 05      JR           NC,$A23
0A1E: FE 06      CP           $06
0A20: 38 01      JR           C,$A23
0A22: 14         INC         D
0A23: 19         ADD         HL,DE
0A24: 5E         LD           E,(HL)
0A25: 7A         LD           A,D
0A26: A7         AND         A
0A27: 20 1A      JR           NZ,$A43
0A29: 7B         LD           A,E
0A2A: FE 23      CP           $23
0A2C: 20 08      JR           NZ,$A36
0A2E: FA C9 D8   LD           A,($D8C9)
0A31: E6 20      AND         $20
0A33: 28 01      JR           Z,$A36
0A35: 1C         INC         E
0A36: 7B         LD           A,E
0A37: FE 21      CP           $21
0A39: 20 08      JR           NZ,$A43
0A3B: FA FD D8   LD           A,($D8FD)
0A3E: E6 20      AND         $20
0A40: 28 01      JR           Z,$A43
0A42: 1C         INC         E
0A43: 16 00      LD           D,$00
0A45: CB 23      SLA         E
0A47: CB 12      RL           D
0A49: CB 23      SLA         E
0A4B: CB 12      RL           D
0A4D: 21 40 45   LD           HL,$4540
0A50: FA A5 DB   LD           A,($DBA5)
0A53: A7         AND         A
0A54: 28 03      JR           Z,$A59
0A56: 21 88 47   LD           HL,$4788
0A59: 19         ADD         HL,DE
0A5A: 16 00      LD           D,$00
0A5C: 01 93 C1   LD           BC,$C193
0A5F: 5E         LD           E,(HL)
0A60: 0A         LD           A,(BC)
0A61: BB         CP           E
0A62: 28 21      JR           Z,$A85
0A64: 7B         LD           A,E
0A65: FE FF      CP           $FF
0A67: 28 1C      JR           Z,$A85
0A69: 02         LD           (BC),A
0A6A: F0 D7      LD           A,($D7)
0A6C: A7         AND         A
0A6D: 28 0B      JR           Z,$A7A
0A6F: 7A         LD           A,D
0A70: EA 0D C1   LD           ($C10D),A
0A73: 3E 01      LD           A,$01
0A75: EA 0E C1   LD           ($C10E),A
0A78: 18 0B      JR           $A85
0A7A: 3C         INC         A
0A7B: E0 D7      LDFF00   ($D7),A
0A7D: 7A         LD           A,D
0A7E: EA 97 C1   LD           ($C197),A
0A81: 3E 01      LD           A,$01
0A83: E0 91      LDFF00   ($91),A
0A85: 23         INC         HL
0A86: 03         INC         BC
0A87: 14         INC         D
0A88: 7A         LD           A,D
0A89: FE 04      CP           $04
0A8B: 20 D2      JR           NZ,$A5F
0A8D: C3 C0 07   JP           $07C0
0A90: FA 95 DB   LD           A,($DB95)
0A93: FE 07      CP           $07
0A95: 38 37      JR           C,$ACE
0A97: FE 0B      CP           $0B
0A99: 20 07      JR           NZ,$AA2
0A9B: FA 96 DB   LD           A,($DB96)
0A9E: FE 07      CP           $07
0AA0: 20 2C      JR           NZ,$ACE
0AA2: FA 6B C1   LD           A,($C16B)
0AA5: FE 04      CP           $04
0AA7: 20 25      JR           NZ,$ACE
0AA9: FA 9F C1   LD           A,($C19F)
0AAC: 21 67 C1   LD           HL,$C167
0AAF: B6         OR           (HL)
0AB0: 21 24 C1   LD           HL,$C124
0AB3: B6         OR           (HL)
0AB4: 20 18      JR           NZ,$ACE
0AB6: F0 CB      LD           A,($CB)
0AB8: FE F0      CP           $F0
0ABA: 20 12      JR           NZ,$ACE
0ABC: AF         XOR         A
0ABD: EA 6B C1   LD           ($C16B),A
0AC0: EA 6C C1   LD           ($C16C),A
0AC3: EA 9F C1   LD           ($C19F),A
0AC6: EA 96 DB   LD           ($DB96),A
0AC9: 3E 06      LD           A,$06
0ACB: EA 95 DB   LD           ($DB95),A
0ACE: FA 95 DB   LD           A,($DB95)
0AD1: C7         RST         0X00
0AD2: 05         DEC         B
0AD3: 0B         DEC         BC
0AD4: 08 0B 34   LD           ($340B),SP
0AD7: 0B         DEC         BC
0AD8: 37         SCF
0AD9: 0B         DEC         BC
0ADA: 3A         LD           A,(HLD)
0ADB: 0B         DEC         BC
0ADC: 3D         DEC         A
0ADD: 0B         DEC         BC
0ADE: 02         LD           (BC),A
0ADF: 0B         DEC         BC
0AE0: FC                              
0AE1: 0A         LD           A,(BC)
0AE2: F0 0A      LD           A,($0A)
0AE4: F6 0A      OR           $0A
0AE6: EA 0A 40   LD           ($400A),A
0AE9: 0B         DEC         BC
0AEA: CD BC 67   CALL       $67BC
0AED: C3 32 0C   JP           $0C32
0AF0: CD 4C 65   CALL       $654C
0AF3: C3 32 0C   JP           $0C32
0AF6: CD BB 5F   CALL       $5FBB
0AF9: C3 32 0C   JP           $0C32
0AFC: CD 6E 54   CALL       $546E
0AFF: C3 32 0C   JP           $0C32
0B02: C3 00 40   JP           $4000
0B05: C3 3E 6E   JP           $6E3E
0B08: 3E 17      LD           A,$17
0B0A: CD B9 07   CALL       $07B9
0B0D: CD 2A 48   CALL       $482A
0B10: C3 32 0C   JP           $0C32
0B13: 3E 03      LD           A,$03
0B15: EA 00 21   LD           ($2100),A
0B18: 3E 17      LD           A,$17
0B1A: F5         PUSH       AF
0B1B: CD 43 38   CALL       $3843
0B1E: F1         POP         AF
0B1F: C3 B9 07   JP           $07B9
0B22: 3E 03      LD           A,$03
0B24: EA 00 21   LD           ($2100),A
0B27: 3E 01      LD           A,$01
0B29: 18 EF      JR           $B1A
0B2B: 3E 03      LD           A,$03
0B2D: EA 00 21   LD           ($2100),A
0B30: 3E 02      LD           A,$02
0B32: 18 E6      JR           $B1A
0B34: C3 11 47   JP           $4711
0B37: C3 4B 49   JP           $494B
0B3A: C3 E6 4B   JP           $4BE6
0B3D: C3 34 4E   JP           $4E34
0B40: 3E 14      LD           A,$14
0B42: EA 00 21   LD           ($2100),A
0B45: CD 26 53   CALL       $5326
0B48: CD 3C 52   CALL       $523C
0B4B: 3E 01      LD           A,$01
0B4D: CD B9 07   CALL       $07B9
0B50: C3 1E 43   JP           $431E
0B53: 3E 02      LD           A,$02
0B55: CD B9 07   CALL       $07B9
0B58: FA 9F C1   LD           A,($C19F)
0B5B: A7         AND         A
0B5C: 20 3C      JR           NZ,$B9A
0B5E: 21 B4 FF   LD           HL,$FFB4
0B61: 7E         LD           A,(HL)
0B62: A7         AND         A
0B63: 28 1B      JR           Z,$B80
0B65: FA 9A DB   LD           A,($DB9A)
0B68: FE 80      CP           $80
0B6A: 20 14      JR           NZ,$B80
0B6C: FA 4F C1   LD           A,($C14F)
0B6F: A7         AND         A
0B70: 20 0E      JR           NZ,$B80
0B72: 35         DEC         (HL)
0B73: 20 0B      JR           NZ,$B80
0B75: 3E 01      LD           A,$01
0B77: EA 00 21   LD           ($2100),A
0B7A: CD A6 5F   CALL       $5FA6
0B7D: CD C0 07   CALL       $07C0
0B80: FA 9F C1   LD           A,($C19F)
0B83: A7         AND         A
0B84: 20 14      JR           NZ,$B9A
0B86: FA BC C1   LD           A,($C1BC)
0B89: A7         AND         A
0B8A: 28 0E      JR           Z,$B9A
0B8C: 21 A1 FF   LD           HL,$FFA1
0B8F: 36 02      LD           (HL),$02
0B91: 3D         DEC         A
0B92: EA BC C1   LD           ($C1BC),A
0B95: 20 03      JR           NZ,$B9A
0B97: C3 09 09   JP           $0909
0B9A: 21 C7 DB   LD           HL,$DBC7
0B9D: 7E         LD           A,(HL)
0B9E: A7         AND         A
0B9F: 28 01      JR           Z,$BA2
0BA1: 35         DEC         (HL)
0BA2: F0 98      LD           A,($98)
0BA4: E0 9F      LDFF00   ($9F),A
0BA6: F0 99      LD           A,($99)
0BA8: E0 A0      LDFF00   ($A0),A
0BAA: 21 A2 FF   LD           HL,$FFA2
0BAD: 96         SUB         (HL)
0BAE: E0 B3      LDFF00   ($B3),A
0BB0: CD D5 5D   CALL       $5DD5
0BB3: AF         XOR         A
0BB4: EA 40 C1   LD           ($C140),A
0BB7: EA 3C C1   LD           ($C13C),A
0BBA: EA 3B C1   LD           ($C13B),A
0BBD: 21 1D C1   LD           HL,$C11D
0BC0: CB BE      RES         7,(HL)
0BC2: 21 1E C1   LD           HL,$C11E
0BC5: CB BE      RES         7,(HL)
0BC7: CD 31 57   CALL       $5731
0BCA: 3E 02      LD           A,$02
0BCC: CD B9 07   CALL       $07B9
0BCF: CD 55 26   CALL       $2655
0BD2: CD 40 0C   CALL       $0C40
0BD5: FA 5C C1   LD           A,($C15C)
0BD8: EA CF C3   LD           ($C3CF),A
0BDB: AF         XOR         A
0BDC: EA 4E C1   LD           ($C14E),A
0BDF: EA 4D C1   LD           ($C14D),A
0BE2: EA A4 C1   LD           ($C1A4),A
0BE5: EA 5C C1   LD           ($C15C),A
0BE8: EA AE C1   LD           ($C1AE),A
0BEB: FA 44 C1   LD           A,($C144)
0BEE: A7         AND         A
0BEF: 28 04      JR           Z,$BF5
0BF1: 3D         DEC         A
0BF2: EA 44 C1   LD           ($C144),A
0BF5: 3E 19      LD           A,$19
0BF7: CD B9 07   CALL       $07B9
0BFA: CD 97 76   CALL       $7697
0BFD: CD 43 38   CALL       $3843
0C00: 3E 02      LD           A,$02
0C02: CD B9 07   CALL       $07B9
0C05: CD 9A 52   CALL       $529A
0C08: 21 01 D6   LD           HL,$D601
0C0B: F0 E7      LD           A,($E7)
0C0D: E6 03      AND         $03
0C0F: B6         OR           (HL)
0C10: 20 18      JR           NZ,$C2A
0C12: FA 1C C1   LD           A,($C11C)
0C15: FE 02      CP           $02
0C17: 30 11      JR           NC,$C2A
0C19: 0E 01      LD           C,$01
0C1B: 06 00      LD           B,$00
0C1D: 1E 00      LD           E,$00
0C1F: F0 E7      LD           A,($E7)
0C21: E6 04      AND         $04
0C23: 28 02      JR           Z,$C27
0C25: 0D         DEC         C
0C26: 1D         DEC         E
0C27: CD ED 61   CALL       $61ED
0C2A: 3E 14      LD           A,$14
0C2C: CD B9 07   CALL       $07B9
0C2F: CD B0 59   CALL       $59B0
0C32: 3E 0F      LD           A,$0F
0C34: CD B9 07   CALL       $07B9
0C37: CD 33 21   CALL       $2133
0C3A: C9         RET
0C3B: 08 0E 99   LD           ($990E),SP
0C3E: 28 EC      JR           Z,$C2C
0C40: F0 99      LD           A,($99)
0C42: 21 A2 FF   LD           HL,$FFA2
0C45: 96         SUB         (HL)
0C46: EA 45 C1   LD           ($C145),A
0C49: FA A9 C1   LD           A,($C1A9)
0C4C: A7         AND         A
0C4D: 28 3D      JR           Z,$C8C
0C4F: FA 9F C1   LD           A,($C19F)
0C52: A7         AND         A
0C53: 20 25      JR           NZ,$C7A
0C55: 21 AA C1   LD           HL,$C1AA
0C58: 35         DEC         (HL)
0C59: 7E         LD           A,(HL)
0C5A: FE 02      CP           $02
0C5C: 20 10      JR           NZ,$C6E
0C5E: FA A9 C1   LD           A,($C1A9)
0C61: 5F         LD           E,A
0C62: 16 00      LD           D,$00
0C64: 21 3A 0C   LD           HL,$0C3A
0C67: 19         ADD         HL,DE
0C68: 7E         LD           A,(HL)
0C69: CD 97 21   CALL       $2197
0C6C: 3E 01      LD           A,$01
0C6E: A7         AND         A
0C6F: 20 09      JR           NZ,$C7A
0C71: AF         XOR         A
0C72: EA A9 C1   LD           ($C1A9),A
0C75: EA A8 C1   LD           ($C1A8),A
0C78: 18 12      JR           $C8C
0C7A: FA A9 C1   LD           A,($C1A9)
0C7D: EA A8 C1   LD           ($C1A8),A
0C80: 3D         DEC         A
0C81: C7         RST         0X00
0C82: 18 50      JR           $CD4
0C84: 23         INC         HL
0C85: 50         LD           D,B
0C86: 23         INC         HL
0C87: 50         LD           D,B
0C88: 23         INC         HL
0C89: 50         LD           D,B
0C8A: 18 50      JR           $CDC
0C8C: F0 CB      LD           A,($CB)
0C8E: E6 B0      AND         $B0
0C90: 20 4C      JR           NZ,$CDE
0C92: F0 CB      LD           A,($CB)
0C94: E6 40      AND         $40
0C96: 28 46      JR           Z,$CDE
0C98: FA 5F D4   LD           A,($D45F)
0C9B: 3C         INC         A
0C9C: EA 5F D4   LD           ($D45F),A
0C9F: FE 04      CP           $04
0CA1: 38 3F      JR           C,$CE2
0CA3: F0 A1      LD           A,($A1)
0CA5: FE 02      CP           $02
0CA7: 28 35      JR           Z,$CDE
0CA9: F0 9D      LD           A,($9D)
0CAB: FE FF      CP           $FF
0CAD: 28 2F      JR           Z,$CDE
0CAF: FA 1C C1   LD           A,($C11C)
0CB2: FE 02      CP           $02
0CB4: 30 28      JR           NC,$CDE
0CB6: 21 67 C1   LD           HL,$C167
0CB9: FA 9F C1   LD           A,($C19F)
0CBC: B6         OR           (HL)
0CBD: 20 1F      JR           NZ,$CDE
0CBF: AF         XOR         A
0CC0: EA 6B C1   LD           ($C16B),A
0CC3: EA 6C C1   LD           ($C16C),A
0CC6: EA 96 DB   LD           ($DB96),A
0CC9: 3E 07      LD           A,$07
0CCB: EA 95 DB   LD           ($DB95),A
0CCE: 3E 02      LD           A,$02
0CD0: EA 00 21   LD           ($2100),A
0CD3: CD 1B 78   CALL       $781B
0CD6: CD CC 1C   CALL       $1CCC
0CD9: CD 43 38   CALL       $3843
0CDC: F1         POP         AF
0CDD: C9         RET
0CDE: AF         XOR         A
0CDF: EA 5F D4   LD           ($D45F),A
0CE2: F0 B7      LD           A,($B7)
0CE4: A7         AND         A
0CE5: 28 03      JR           Z,$CEA
0CE7: 3D         DEC         A
0CE8: E0 B7      LDFF00   ($B7),A
0CEA: F0 B6      LD           A,($B6)
0CEC: A7         AND         A
0CED: 28 03      JR           Z,$CF2
0CEF: 3D         DEC         A
0CF0: E0 B6      LDFF00   ($B6),A
0CF2: FA 9F C1   LD           A,($C19F)
0CF5: A7         AND         A
0CF6: C2 9B 14   JP           NZ,$149B
0CF9: FA 24 C1   LD           A,($C124)
0CFC: A7         AND         A
0CFD: C2 49 0D   JP           NZ,$0D49
0D00: FA 1C C1   LD           A,($C11C)
0D03: FE 07      CP           $07
0D05: 28 2B      JR           Z,$D32
0D07: FA 5A DB   LD           A,($DB5A)
0D0A: 21 0A C5   LD           HL,$C50A
0D0D: B6         OR           (HL)
0D0E: 21 4F C1   LD           HL,$C14F
0D11: B6         OR           (HL)
0D12: 20 1B      JR           NZ,$D2F
0D14: 3E 07      LD           A,$07
0D16: EA 1C C1   LD           ($C11C),A
0D19: 3E BF      LD           A,$BF
0D1B: E0 B7      LDFF00   ($B7),A
0D1D: 3E 10      LD           A,$10
0D1F: EA CC C3   LD           ($C3CC),A
0D22: AF         XOR         A
0D23: EA C7 DB   LD           ($DBC7),A
0D26: E0 9C      LDFF00   ($9C),A
0D28: CD D2 27   CALL       $27D2
0D2B: 3E 08      LD           A,$08
0D2D: E0 F3      LDFF00   ($F3),A
0D2F: FA 1C C1   LD           A,($C11C)
0D32: C7         RST         0X00
0D33: 5F         LD           E,A
0D34: 0D         DEC         C
0D35: 92         SUB         D
0D36: 4D         LD           C,L
0D37: 0E 49      LD           C,$49
0D39: B3         OR           E
0D3A: 15         DEC         D
0D3B: 32         LD           (HLD),A
0D3C: 17         RLA
0D3D: 00         NOP
0D3E: 4D         LD           C,L
0D3F: 30 4F      JR           NC,$D90
0D41: 57         LD           D,A
0D42: 0D         DEC         C
0D43: A2         AND         D
0D44: 50         LD           D,B
0D45: 4F         LD           C,A
0D46: 0D         DEC         C
0D47: FF         RST         0X38
0D48: 4E         LD           C,(HL)
0D49: CD 9B 14   CALL       $149B
0D4C: C3 CC 1C   JP           $1CCC
0D4F: 3E 19      LD           A,$19
0D51: CD B9 07   CALL       $07B9
0D54: C3 A9 5C   JP           $5CA9
0D57: 3E 01      LD           A,$01
0D59: CD B9 07   CALL       $07B9
0D5C: C3 84 41   JP           $4184
0D5F: 3E 02      LD           A,$02
0D61: CD B9 07   CALL       $07B9
0D64: CD 6E 42   CALL       $426E
0D67: C9         RET
0D68: FA 0A C5   LD           A,($C50A)
0D6B: 21 67 C1   LD           HL,$C167
0D6E: B6         OR           (HL)
0D6F: 21 A4 C1   LD           HL,$C1A4
0D72: B6         OR           (HL)
0D73: C0         RET         NZ
0D74: FA 4A C1   LD           A,($C14A)
0D77: A7         AND         A
0D78: 28 33      JR           Z,$DAD
0D7A: FA 01 DB   LD           A,($DB01)
0D7D: FE 01      CP           $01
0D7F: 28 1A      JR           Z,$D9B
0D81: FA 00 DB   LD           A,($DB00)
0D84: FE 01      CP           $01
0D86: 28 13      JR           Z,$D9B
0D88: FA 01 DB   LD           A,($DB01)
0D8B: FE 04      CP           $04
0D8D: 28 07      JR           Z,$D96
0D8F: FA 00 DB   LD           A,($DB00)
0D92: FE 04      CP           $04
0D94: 20 15      JR           NZ,$DAB
0D96: CD 34 0F   CALL       $0F34
0D99: 18 10      JR           $DAB
0D9B: FA 37 C1   LD           A,($C137)
0D9E: 3D         DEC         A
0D9F: FE 04      CP           $04
0DA1: 38 08      JR           C,$DAB
0DA3: 3E 05      LD           A,$05
0DA5: EA 37 C1   LD           ($C137),A
0DA8: EA 6A C1   LD           ($C16A),A
0DAB: 18 07      JR           $DB4
0DAD: AF         XOR         A
0DAE: EA 5B C1   LD           ($C15B),A
0DB1: EA 5A C1   LD           ($C15A),A
0DB4: FA 17 C1   LD           A,($C117)
0DB7: A7         AND         A
0DB8: C2 D0 0E   JP           NZ,$0ED0
0DBB: FA 5C C1   LD           A,($C15C)
0DBE: A7         AND         A
0DBF: C2 D0 0E   JP           NZ,$0ED0
0DC2: FA 37 C1   LD           A,($C137)
0DC5: A7         AND         A
0DC6: 28 0B      JR           Z,$DD3
0DC8: FE 03      CP           $03
0DCA: 20 07      JR           NZ,$DD3
0DCC: FA 38 C1   LD           A,($C138)
0DCF: FE 03      CP           $03
0DD1: 30 06      JR           NC,$DD9
0DD3: F0 A1      LD           A,($A1)
0DD5: A7         AND         A
0DD6: C2 D0 0E   JP           NZ,$0ED0
0DD9: FA 00 DB   LD           A,($DB00)
0DDC: FE 08      CP           $08
0DDE: 20 0F      JR           NZ,$DEF
0DE0: F0 CB      LD           A,($CB)
0DE2: E6 20      AND         $20
0DE4: 28 05      JR           Z,$DEB
0DE6: CD 0C 14   CALL       $140C
0DE9: 18 04      JR           $DEF
0DEB: AF         XOR         A
0DEC: EA 4B C1   LD           ($C14B),A
0DEF: FA 01 DB   LD           A,($DB01)
0DF2: FE 08      CP           $08
0DF4: 20 0F      JR           NZ,$E05
0DF6: F0 CB      LD           A,($CB)
0DF8: E6 10      AND         $10
0DFA: 28 05      JR           Z,$E01
0DFC: CD 0C 14   CALL       $140C
0DFF: 18 04      JR           $E05
0E01: AF         XOR         A
0E02: EA 4B C1   LD           ($C14B),A
0E05: FA 01 DB   LD           A,($DB01)
0E08: FE 04      CP           $04
0E0A: 20 1A      JR           NZ,$E26
0E0C: FA 44 DB   LD           A,($DB44)
0E0F: EA 5A C1   LD           ($C15A),A
0E12: F0 CB      LD           A,($CB)
0E14: E6 10      AND         $10
0E16: 28 0E      JR           Z,$E26
0E18: FA AD C1   LD           A,($C1AD)
0E1B: FE 01      CP           $01
0E1D: 28 07      JR           Z,$E26
0E1F: FE 02      CP           $02
0E21: 28 03      JR           Z,$E26
0E23: CD 34 0F   CALL       $0F34
0E26: FA 00 DB   LD           A,($DB00)
0E29: FE 04      CP           $04
0E2B: 20 0F      JR           NZ,$E3C
0E2D: FA 44 DB   LD           A,($DB44)
0E30: EA 5A C1   LD           ($C15A),A
0E33: F0 CB      LD           A,($CB)
0E35: E6 20      AND         $20
0E37: 28 03      JR           Z,$E3C
0E39: CD 34 0F   CALL       $0F34
0E3C: F0 CC      LD           A,($CC)
0E3E: E6 20      AND         $20
0E40: 28 0D      JR           Z,$E4F
0E42: FA AD C1   LD           A,($C1AD)
0E45: FE 02      CP           $02
0E47: 28 06      JR           Z,$E4F
0E49: FA 00 DB   LD           A,($DB00)
0E4C: CD 7F 0E   CALL       $0E7F
0E4F: F0 CC      LD           A,($CC)
0E51: E6 10      AND         $10
0E53: 28 11      JR           Z,$E66
0E55: FA AD C1   LD           A,($C1AD)
0E58: FE 01      CP           $01
0E5A: 28 0A      JR           Z,$E66
0E5C: FE 02      CP           $02
0E5E: 28 06      JR           Z,$E66
0E60: FA 01 DB   LD           A,($DB01)
0E63: CD 7F 0E   CALL       $0E7F
0E66: F0 CB      LD           A,($CB)
0E68: E6 20      AND         $20
0E6A: 28 06      JR           Z,$E72
0E6C: FA 00 DB   LD           A,($DB00)
0E6F: CD 05 0F   CALL       $0F05
0E72: F0 CB      LD           A,($CB)
0E74: E6 10      AND         $10
0E76: 28 06      JR           Z,$E7E
0E78: FA 01 DB   LD           A,($DB01)
0E7B: CD 05 0F   CALL       $0F05
0E7E: C9         RET
0E7F: 4F         LD           C,A
0E80: FE 01      CP           $01
0E82: CA 2F 12   JP           Z,$122F
0E85: FE 04      CP           $04
0E87: CA D1 0E   JP           Z,$0ED1
0E8A: FE 02      CP           $02
0E8C: CA 76 0F   JP           Z,$0F76
0E8F: FE 03      CP           $03
0E91: CA 07 10   JP           Z,$1007
0E94: FE 05      CP           $05
0E96: CA 79 10   JP           Z,$1079
0E99: FE 0D      CP           $0D
0E9B: CA 0E 10   JP           Z,$100E
0E9E: FE 06      CP           $06
0EA0: CA FC 0E   JP           Z,$0EFC
0EA3: FE 0A      CP           $0A
0EA5: CA D1 11   JP           Z,$11D1
0EA8: FE 09      CP           $09
0EAA: CA E6 41   JP           Z,$41E6
0EAD: FE 0C      CP           $0C
0EAF: CA 51 11   JP           Z,$1151
0EB2: FE 0B      CP           $0B
0EB4: CA DB 0E   JP           Z,$0EDB
0EB7: FE 07      CP           $07
0EB9: 20 15      JR           NZ,$ED0
0EBB: 21 37 C1   LD           HL,$C137
0EBE: FA 9B C1   LD           A,($C19B)
0EC1: B6         OR           (HL)
0EC2: 20 0C      JR           NZ,$ED0
0EC4: FA 4D C1   LD           A,($C14D)
0EC7: FE 02      CP           $02
0EC9: 30 05      JR           NC,$ED0
0ECB: 3E 8E      LD           A,$8E
0ECD: EA 9B C1   LD           ($C19B),A
0ED0: C9         RET
0ED1: FA 44 C1   LD           A,($C144)
0ED4: A7         AND         A
0ED5: C0         RET         NZ
0ED6: 3E 16      LD           A,$16
0ED8: E0 F4      LDFF00   ($F4),A
0EDA: C9         RET
0EDB: FA C7 C1   LD           A,($C1C7)
0EDE: 21 46 C1   LD           HL,$C146
0EE1: B6         OR           (HL)
0EE2: C0         RET         NZ
0EE3: CD 35 4C   CALL       $4C35
0EE6: 30 06      JR           NC,$EEE
0EE8: 3E 07      LD           A,$07
0EEA: E0 F2      LDFF00   ($F2),A
0EEC: 18 04      JR           $EF2
0EEE: 3E 0E      LD           A,$0E
0EF0: E0 F4      LDFF00   ($F4),A
0EF2: 3E 01      LD           A,$01
0EF4: EA C7 C1   LD           ($C1C7),A
0EF7: AF         XOR         A
0EF8: EA C8 C1   LD           ($C1C8),A
0EFB: C9         RET
0EFC: FA A4 C1   LD           A,($C1A4)
0EFF: A7         AND         A
0F00: C0         RET         NZ
0F01: CD 3B 42   CALL       $423B
0F04: C9         RET
0F05: FE 01      CP           $01
0F07: C0         RET         NZ
0F08: 21 37 C1   LD           HL,$C137
0F0B: FA AD C1   LD           A,($C1AD)
0F0E: E6 03      AND         $03
0F10: B6         OR           (HL)
0F11: C0         RET         NZ
0F12: FA 60 C1   LD           A,($C160)
0F15: A7         AND         A
0F16: C0         RET         NZ
0F17: AF         XOR         A
0F18: EA AC C1   LD           ($C1AC),A
0F1B: 3E 05      LD           A,$05
0F1D: EA 37 C1   LD           ($C137),A
0F20: EA B0 C5   LD           ($C5B0),A
0F23: C9         RET
0F24: 10 00      STOP       $00
0F26: 08 08 03   LD           ($0308),SP
0F29: 03         INC         BC
0F2A: 08 08 08   LD           ($0808),SP
0F2D: 08 00 0D   LD           ($0D00),SP
0F30: 08 08 03   LD           ($0308),SP
0F33: 04         INC         B
0F34: 3E 01      LD           A,$01
0F36: EA 5B C1   LD           ($C15B),A
0F39: FA 44 DB   LD           A,($DB44)
0F3C: EA 5A C1   LD           ($C15A),A
0F3F: F0 9E      LD           A,($9E)
0F41: 5F         LD           E,A
0F42: 16 00      LD           D,$00
0F44: 21 24 0F   LD           HL,$0F24
0F47: 19         ADD         HL,DE
0F48: F0 98      LD           A,($98)
0F4A: 86         ADD         A,(HL)
0F4B: EA 40 C1   LD           ($C140),A
0F4E: 21 28 0F   LD           HL,$0F28
0F51: 19         ADD         HL,DE
0F52: 7E         LD           A,(HL)
0F53: EA 41 C1   LD           ($C141),A
0F56: 21 2C 0F   LD           HL,$0F2C
0F59: 19         ADD         HL,DE
0F5A: FA 45 C1   LD           A,($C145)
0F5D: 86         ADD         A,(HL)
0F5E: EA 42 C1   LD           ($C142),A
0F61: 21 30 0F   LD           HL,$0F30
0F64: 19         ADD         HL,DE
0F65: 7E         LD           A,(HL)
0F66: EA 43 C1   LD           ($C143),A
0F69: AF         XOR         A
0F6A: EA B0 C5   LD           ($C5B0),A
0F6D: C9         RET
0F6E: 08 F8 00   LD           ($00F8),SP
0F71: 00         NOP
0F72: 00         NOP
0F73: 00         NOP
0F74: FD                              
0F75: 04         INC         B
0F76: FA 4E C1   LD           A,($C14E)
0F79: FE 01      CP           $01
0F7B: D0         RET         NC
0F7C: FA 4D DB   LD           A,($DB4D)
0F7F: A7         AND         A
0F80: CA AC 08   JP           Z,$08AC
0F83: D6 01      SUB         $01
0F85: 27         DAA
0F86: EA 4D DB   LD           ($DB4D),A
0F89: 3E 02      LD           A,$02
0F8B: CD EB 10   CALL       $10EB
0F8E: D8         RET         C
0F8F: 21 F0 C2   LD           HL,$C2F0
0F92: 19         ADD         HL,DE
0F93: 36 10      LD           (HL),$10
0F95: FA C0 C1   LD           A,($C1C0)
0F98: A7         AND         A
0F99: CA AC 0F   JP           Z,$0FAC
0F9C: AF         XOR         A
0F9D: EA C0 C1   LD           ($C1C0),A
0FA0: FA C2 C1   LD           A,($C1C2)
0FA3: 4F         LD           C,A
0FA4: 42         LD           B,D
0FA5: 21 90 C2   LD           HL,$C290
0FA8: 09         ADD         HL,BC
0FA9: 36 01      LD           (HL),$01
0FAB: C9         RET
0FAC: 3E 06      LD           A,$06
0FAE: EA C0 C1   LD           ($C1C0),A
0FB1: 7B         LD           A,E
0FB2: EA C1 C1   LD           ($C1C1),A
0FB5: 3E 0C      LD           A,$0C
0FB7: EA 9B C1   LD           ($C19B),A
0FBA: 21 E0 C2   LD           HL,$C2E0
0FBD: 19         ADD         HL,DE
0FBE: 36 A0      LD           (HL),$A0
0FC0: 21 B0 C3   LD           HL,$C3B0
0FC3: 19         ADD         HL,DE
0FC4: 72         LD           (HL),D
0FC5: 21 80 C4   LD           HL,$C480
0FC8: 19         ADD         HL,DE
0FC9: 36 03      LD           (HL),$03
0FCB: F0 F9      LD           A,($F9)
0FCD: A7         AND         A
0FCE: 20 06      JR           NZ,$FD6
0FD0: 3E 09      LD           A,$09
0FD2: E0 F2      LDFF00   ($F2),A
0FD4: 18 05      JR           $FDB
0FD6: 21 10 C3   LD           HL,$C310
0FD9: 19         ADD         HL,DE
0FDA: 72         LD           (HL),D
0FDB: 21 40 C2   LD           HL,$C240
0FDE: 19         ADD         HL,DE
0FDF: 72         LD           (HL),D
0FE0: 21 50 C2   LD           HL,$C250
0FE3: 19         ADD         HL,DE
0FE4: 72         LD           (HL),D
0FE5: 21 20 C3   LD           HL,$C320
0FE8: 19         ADD         HL,DE
0FE9: 72         LD           (HL),D
0FEA: F0 9E      LD           A,($9E)
0FEC: 4F         LD           C,A
0FED: 42         LD           B,D
0FEE: 21 6E 0F   LD           HL,$0F6E
0FF1: 09         ADD         HL,BC
0FF2: F0 98      LD           A,($98)
0FF4: 86         ADD         A,(HL)
0FF5: 21 00 C2   LD           HL,$C200
0FF8: 19         ADD         HL,DE
0FF9: 77         LD           (HL),A
0FFA: 21 72 0F   LD           HL,$0F72
0FFD: 09         ADD         HL,BC
0FFE: F0 99      LD           A,($99)
1000: 86         ADD         A,(HL)
1001: 21 10 C2   LD           HL,$C210
1004: 19         ADD         HL,DE
1005: 77         LD           (HL),A
1006: C9         RET
1007: C9         RET
1008: 18 E8      JR           $FF2
100A: 00         NOP
100B: E8 18      ADD         SP,$18
100D: 00         NOP
100E: FA 4D C1   LD           A,($C14D)
1011: A7         AND         A
1012: C0         RET         NZ
1013: 3E 01      LD           A,$01
1015: CD EB 10   CALL       $10EB
1018: D8         RET         C
1019: 21 E0 C2   LD           HL,$C2E0
101C: 19         ADD         HL,DE
101D: 36 28      LD           (HL),$28
101F: 0E 04      LD           C,$04
1021: 06 00      LD           B,$00
1023: F0 CB      LD           A,($CB)
1025: CB 3F      SRL         A
1027: 30 01      JR           NC,$102A
1029: 04         INC         B
102A: 0D         DEC         C
102B: 20 F8      JR           NZ,$1025
102D: 78         LD           A,B
102E: FE 02      CP           $02
1030: 38 26      JR           C,$1058
1032: F0 CB      LD           A,($CB)
1034: E6 03      AND         $03
1036: 4F         LD           C,A
1037: 06 00      LD           B,$00
1039: 21 07 10   LD           HL,$1007
103C: 09         ADD         HL,BC
103D: 7E         LD           A,(HL)
103E: 21 40 C2   LD           HL,$C240
1041: 19         ADD         HL,DE
1042: 77         LD           (HL),A
1043: F0 CB      LD           A,($CB)
1045: CB 3F      SRL         A
1047: CB 3F      SRL         A
1049: E6 03      AND         $03
104B: 4F         LD           C,A
104C: 06 00      LD           B,$00
104E: 21 0A 10   LD           HL,$100A
1051: 09         ADD         HL,BC
1052: 7E         LD           A,(HL)
1053: 21 50 C2   LD           HL,$C250
1056: 19         ADD         HL,DE
1057: 77         LD           (HL),A
1058: C9         RET
1059: 00         NOP
105A: 00         NOP
105B: 00         NOP
105C: 00         NOP
105D: 00         NOP
105E: 00         NOP
105F: 00         NOP
1060: 00         NOP
1061: 20 E0      JR           NZ,$1043
1063: 00         NOP
1064: 00         NOP
1065: 00         NOP
1066: 00         NOP
1067: E0 20      LDFF00   ($20),A
1069: 30 D0      JR           NC,$103B
106B: 00         NOP
106C: 00         NOP
106D: 40         LD           B,B
106E: C0         RET         NZ
106F: 00         NOP
1070: 00         NOP
1071: 00         NOP
1072: 00         NOP
1073: D0         RET         NC
1074: 30 00      JR           NC,$1076
1076: 00         NOP
1077: C0         RET         NZ
1078: 40         LD           B,B
1079: FA 4C C1   LD           A,($C14C)
107C: A7         AND         A
107D: C0         RET         NZ
107E: FA 4D C1   LD           A,($C14D)
1081: FE 02      CP           $02
1083: 30 65      JR           NC,$10EA
1085: 3E 10      LD           A,$10
1087: EA 4C C1   LD           ($C14C),A
108A: FA 45 DB   LD           A,($DB45)
108D: A7         AND         A
108E: CA AC 08   JP           Z,$08AC
1091: D6 01      SUB         $01
1093: 27         DAA
1094: EA 45 DB   LD           ($DB45),A
1097: CD 83 12   CALL       $1283
109A: 3E 00      LD           A,$00
109C: CD EB 10   CALL       $10EB
109F: D8         RET         C
10A0: 7B         LD           A,E
10A1: EA C2 C1   LD           ($C1C2),A
10A4: FA C0 C1   LD           A,($C1C0)
10A7: A7         AND         A
10A8: 28 13      JR           Z,$10BD
10AA: FA C1 C1   LD           A,($C1C1)
10AD: 4F         LD           C,A
10AE: 42         LD           B,D
10AF: 21 80 C2   LD           HL,$C280
10B2: 09         ADD         HL,BC
10B3: 70         LD           (HL),B
10B4: 21 90 C2   LD           HL,$C290
10B7: 19         ADD         HL,DE
10B8: 36 01      LD           (HL),$01
10BA: AF         XOR         A
10BB: 18 06      JR           $10C3
10BD: 3E 0A      LD           A,$0A
10BF: E0 F4      LDFF00   ($F4),A
10C1: 3E 06      LD           A,$06
10C3: EA C0 C1   LD           ($C1C0),A
10C6: F0 9E      LD           A,($9E)
10C8: 4F         LD           C,A
10C9: 06 00      LD           B,$00
10CB: FA 7C D4   LD           A,($D47C)
10CE: FE 01      CP           $01
10D0: 20 04      JR           NZ,$10D6
10D2: 79         LD           A,C
10D3: C6 04      ADD         $04
10D5: 4F         LD           C,A
10D6: 21 69 10   LD           HL,$1069
10D9: 09         ADD         HL,BC
10DA: 7E         LD           A,(HL)
10DB: 21 40 C2   LD           HL,$C240
10DE: 19         ADD         HL,DE
10DF: 77         LD           (HL),A
10E0: 21 71 10   LD           HL,$1071
10E3: 09         ADD         HL,BC
10E4: 7E         LD           A,(HL)
10E5: 21 50 C2   LD           HL,$C250
10E8: 19         ADD         HL,DE
10E9: 77         LD           (HL),A
10EA: C9         RET
10EB: CD 01 3C   CALL       $3C01
10EE: D8         RET         C
10EF: 3E 0C      LD           A,$0C
10F1: EA 9B C1   LD           ($C19B),A
10F4: C5         PUSH       BC
10F5: F0 9E      LD           A,($9E)
10F7: 4F         LD           C,A
10F8: 06 00      LD           B,$00
10FA: 21 59 10   LD           HL,$1059
10FD: 09         ADD         HL,BC
10FE: F0 98      LD           A,($98)
1100: 86         ADD         A,(HL)
1101: 21 00 C2   LD           HL,$C200
1104: 19         ADD         HL,DE
1105: 77         LD           (HL),A
1106: 21 5D 10   LD           HL,$105D
1109: 09         ADD         HL,BC
110A: F0 99      LD           A,($99)
110C: 86         ADD         A,(HL)
110D: 21 10 C2   LD           HL,$C210
1110: 19         ADD         HL,DE
1111: 77         LD           (HL),A
1112: F0 A2      LD           A,($A2)
1114: 3C         INC         A
1115: 21 10 C3   LD           HL,$C310
1118: 19         ADD         HL,DE
1119: 77         LD           (HL),A
111A: 21 61 10   LD           HL,$1061
111D: 09         ADD         HL,BC
111E: 7E         LD           A,(HL)
111F: 21 40 C2   LD           HL,$C240
1122: 19         ADD         HL,DE
1123: 77         LD           (HL),A
1124: 21 65 10   LD           HL,$1065
1127: 09         ADD         HL,BC
1128: 7E         LD           A,(HL)
1129: 21 50 C2   LD           HL,$C250
112C: 19         ADD         HL,DE
112D: 77         LD           (HL),A
112E: F0 9E      LD           A,($9E)
1130: 21 B0 C3   LD           HL,$C3B0
1133: 19         ADD         HL,DE
1134: 77         LD           (HL),A
1135: 21 80 C3   LD           HL,$C380
1138: 19         ADD         HL,DE
1139: 77         LD           (HL),A
113A: 21 D0 C5   LD           HL,$C5D0
113D: 19         ADD         HL,DE
113E: 77         LD           (HL),A
113F: 21 F0 C4   LD           HL,$C4F0
1142: 19         ADD         HL,DE
1143: 36 01      LD           (HL),$01
1145: C1         POP         BC
1146: 37         SCF
1147: 3F         CCF
1148: C9         RET
1149: 0E F2      LD           C,$F2
114B: 00         NOP
114C: 00         NOP
114D: 00         NOP
114E: 00         NOP
114F: F4                              
1150: 0C         INC         C
1151: FA 9B C1   LD           A,($C19B)
1154: A7         AND         A
1155: C0         RET         NZ
1156: FA 4B DB   LD           A,($DB4B)
1159: A7         AND         A
115A: 28 0F      JR           Z,$116B
115C: F0 A2      LD           A,($A2)
115E: A7         AND         A
115F: C0         RET         NZ
1160: 3E 02      LD           A,$02
1162: EA A9 C1   LD           ($C1A9),A
1165: 3E 2A      LD           A,$2A
1167: EA AA C1   LD           ($C1AA),A
116A: C9         RET
116B: FA 4C DB   LD           A,($DB4C)
116E: A7         AND         A
116F: CA AC 08   JP           Z,$08AC
1172: 3E 08      LD           A,$08
1174: CD 01 3C   CALL       $3C01
1177: D8         RET         C
1178: 3E 05      LD           A,$05
117A: E0 F2      LDFF00   ($F2),A
117C: 3E 0E      LD           A,$0E
117E: EA 9B C1   LD           ($C19B),A
1181: FA 4C DB   LD           A,($DB4C)
1184: D6 01      SUB         $01
1186: 27         DAA
1187: EA 4C DB   LD           ($DB4C),A
118A: 20 12      JR           NZ,$119E
118C: 21 00 DB   LD           HL,$DB00
118F: 7E         LD           A,(HL)
1190: FE 0C      CP           $0C
1192: 20 02      JR           NZ,$1196
1194: 36 00      LD           (HL),$00
1196: 23         INC         HL
1197: 7E         LD           A,(HL)
1198: FE 0C      CP           $0C
119A: 20 02      JR           NZ,$119E
119C: 36 00      LD           (HL),$00
119E: C5         PUSH       BC
119F: F0 9E      LD           A,($9E)
11A1: 4F         LD           C,A
11A2: 21 49 11   LD           HL,$1149
11A5: 09         ADD         HL,BC
11A6: F0 98      LD           A,($98)
11A8: 86         ADD         A,(HL)
11A9: 21 00 C2   LD           HL,$C200
11AC: 19         ADD         HL,DE
11AD: 77         LD           (HL),A
11AE: 21 4D 11   LD           HL,$114D
11B1: 09         ADD         HL,BC
11B2: F0 99      LD           A,($99)
11B4: 86         ADD         A,(HL)
11B5: 21 10 C2   LD           HL,$C210
11B8: 19         ADD         HL,DE
11B9: 77         LD           (HL),A
11BA: F0 A2      LD           A,($A2)
11BC: 21 10 C3   LD           HL,$C310
11BF: 19         ADD         HL,DE
11C0: 77         LD           (HL),A
11C1: 21 E0 C2   LD           HL,$C2E0
11C4: 19         ADD         HL,DE
11C5: 36 17      LD           (HL),$17
11C7: C1         POP         BC
11C8: C9         RET
11C9: 1C         INC         E
11CA: E4                              
11CB: 00         NOP
11CC: 00         NOP
11CD: 00         NOP
11CE: 00         NOP
11CF: E4                              
11D0: 1C         INC         E
11D1: FA 30 C1   LD           A,($C130)
11D4: FE 07      CP           $07
11D6: C8         RET         Z
11D7: FA 46 C1   LD           A,($C146)
11DA: A7         AND         A
11DB: C0         RET         NZ
11DC: 3E 01      LD           A,$01
11DE: EA 46 C1   LD           ($C146),A
11E1: AF         XOR         A
11E2: EA 52 C1   LD           ($C152),A
11E5: EA 53 C1   LD           ($C153),A
11E8: 3E 0D      LD           A,$0D
11EA: E0 F2      LDFF00   ($F2),A
11EC: F0 F9      LD           A,($F9)
11EE: A7         AND         A
11EF: 28 1E      JR           Z,$120F
11F1: CD 0F 12   CALL       $120F
11F4: F0 CB      LD           A,($CB)
11F6: E6 03      AND         $03
11F8: 3E EA      LD           A,$EA
11FA: 28 02      JR           Z,$11FE
11FC: 3E E8      LD           A,$E8
11FE: E0 9B      LDFF00   ($9B),A
1200: AF         XOR         A
1201: E0 A3      LDFF00   ($A3),A
1203: CD D6 20   CALL       $20D6
1206: 3E 02      LD           A,$02
1208: CD B9 07   CALL       $07B9
120B: CD B1 6F   CALL       $6FB1
120E: C9         RET
120F: 3E 20      LD           A,$20
1211: E0 A3      LDFF00   ($A3),A
1213: FA 4A C1   LD           A,($C14A)
1216: A7         AND         A
1217: C8         RET         Z
1218: F0 9E      LD           A,($9E)
121A: 5F         LD           E,A
121B: 50         LD           D,B
121C: 21 C9 11   LD           HL,$11C9
121F: 19         ADD         HL,DE
1220: 7E         LD           A,(HL)
1221: E0 9A      LDFF00   ($9A),A
1223: 21 CD 11   LD           HL,$11CD
1226: 19         ADD         HL,DE
1227: 7E         LD           A,(HL)
1228: E0 9B      LDFF00   ($9B),A
122A: C9         RET
122B: 02         LD           (BC),A
122C: 14         INC         D
122D: 15         DEC         D
122E: 18 FA      JR           $122A
1230: 6D         LD           L,L
1231: C1         POP         BC
1232: 21 21 C1   LD           HL,$C121
1235: B6         OR           (HL)
1236: C0         RET         NZ
1237: 3E 03      LD           A,$03
1239: EA 38 C1   LD           ($C138),A
123C: 3E 01      LD           A,$01
123E: EA 37 C1   LD           ($C137),A
1241: EA B0 C5   LD           ($C5B0),A
1244: AF         XOR         A
1245: EA 60 C1   LD           ($C160),A
1248: EA AC C1   LD           ($C1AC),A
124B: CD ED 27   CALL       $27ED
124E: E6 03      AND         $03
1250: 5F         LD           E,A
1251: 16 00      LD           D,$00
1253: 21 2B 12   LD           HL,$122B
1256: 19         ADD         HL,DE
1257: 7E         LD           A,(HL)
1258: E0 F4      LDFF00   ($F4),A
125A: CD 83 12   CALL       $1283
125D: FA 46 C1   LD           A,($C146)
1260: A7         AND         A
1261: 20 06      JR           NZ,$1269
1263: CD 3B 09   CALL       $093B
1266: CD 95 14   CALL       $1495
1269: FA 4D C1   LD           A,($C14D)
126C: A7         AND         A
126D: C0         RET         NZ
126E: FA A9 C5   LD           A,($C5A9)
1271: A7         AND         A
1272: C8         RET         Z
1273: FA 4E DB   LD           A,($DB4E)
1276: FE 02      CP           $02
1278: C0         RET         NZ
1279: 3E DF      LD           A,$DF
127B: CD EB 10   CALL       $10EB
127E: AF         XOR         A
127F: EA 9B C1   LD           ($C19B),A
1282: C9         RET
1283: F0 CB      LD           A,($CB)
1285: E6 0F      AND         $0F
1287: 5F         LD           E,A
1288: 16 00      LD           D,$00
128A: 21 B3 48   LD           HL,$48B3
128D: 19         ADD         HL,DE
128E: 7E         LD           A,(HL)
128F: FE 0F      CP           $0F
1291: 28 02      JR           Z,$1295
1293: E0 9E      LDFF00   ($9E),A
1295: C9         RET
1296: 16 FA      LD           D,$FA
1298: 08 08 16   LD           ($1608),SP
129B: 16 08      LD           D,$08
129D: FA FA FA   LD           A,($FAFA)
12A0: 08 16 08   LD           ($0816),SP
12A3: 08 FA 16   LD           ($16FA),SP
12A6: 08 16 16   LD           ($1616),SP
12A9: 16 08      LD           D,$08
12AB: FA FA FA   LD           A,($FAFA)
12AE: CD B6 12   CALL       $12B6
12B1: 3E 02      LD           A,$02
12B3: C3 B9 07   JP           $07B9
12B6: FA C4 C1   LD           A,($C1C4)
12B9: A7         AND         A
12BA: C0         RET         NZ
12BB: FA 4A C1   LD           A,($C14A)
12BE: A7         AND         A
12BF: 20 06      JR           NZ,$12C7
12C1: FA 6A C1   LD           A,($C16A)
12C4: FE 05      CP           $05
12C6: C8         RET         Z
12C7: FA 21 C1   LD           A,($C121)
12CA: A7         AND         A
12CB: 28 07      JR           Z,$12D4
12CD: FA 36 C1   LD           A,($C136)
12D0: C6 04      ADD         $04
12D2: 18 02      JR           $12D6
12D4: F0 9E      LD           A,($9E)
12D6: 5F         LD           E,A
12D7: 16 00      LD           D,$00
12D9: 21 96 12   LD           HL,$1296
12DC: 19         ADD         HL,DE
12DD: F0 98      LD           A,($98)
12DF: 86         ADD         A,(HL)
12E0: D6 08      SUB         $08
12E2: E6 F0      AND         $F0
12E4: E0 CE      LDFF00   ($CE),A
12E6: CB 37      SWAP       A
12E8: 4F         LD           C,A
12E9: 21 A2 12   LD           HL,$12A2
12EC: 19         ADD         HL,DE
12ED: F0 99      LD           A,($99)
12EF: 86         ADD         A,(HL)
12F0: D6 10      SUB         $10
12F2: E6 F0      AND         $F0
12F4: E0 CD      LDFF00   ($CD),A
12F6: B1         OR           C
12F7: 5F         LD           E,A
12F8: 21 11 D7   LD           HL,$D711
12FB: 19         ADD         HL,DE
12FC: 7C         LD           A,H
12FD: FE D7      CP           $D7
12FF: C0         RET         NZ
1300: D5         PUSH       DE
1301: 7E         LD           A,(HL)
1302: E0 AF      LDFF00   ($AF),A
1304: 5F         LD           E,A
1305: FA A5 DB   LD           A,($DBA5)
1308: 57         LD           D,A
1309: CD DB 29   CALL       $29DB
130C: D1         POP         DE
130D: FE D0      CP           $D0
130F: DA 17 13   JP           C,$1317
1312: FE D4      CP           $D4
1314: DA C9 13   JP           C,$13C9
1317: FE 90      CP           $90
1319: D2 C9 13   JP           NC,$13C9
131C: FE 01      CP           $01
131E: CA C9 13   JP           Z,$13C9
1321: 0E 00      LD           C,$00
1323: FA A5 DB   LD           A,($DBA5)
1326: A7         AND         A
1327: F0 AF      LD           A,($AF)
1329: 28 05      JR           Z,$1330
132B: FE DD      CP           $DD
132D: 28 0F      JR           Z,$133E
132F: C9         RET
1330: 0C         INC         C
1331: FE D3      CP           $D3
1333: 28 09      JR           Z,$133E
1335: FE 5C      CP           $5C
1337: 28 05      JR           Z,$133E
1339: FE 0A      CP           $0A
133B: C0         RET         NZ
133C: 0E FF      LD           C,$FF
133E: 79         LD           A,C
133F: E0 F1      LDFF00   ($F1),A
1341: CD A6 20   CALL       $20A6
1344: FA 4A C1   LD           A,($C14A)
1347: A7         AND         A
1348: 20 10      JR           NZ,$135A
134A: FA 6A C1   LD           A,($C16A)
134D: FE 05      CP           $05
134F: 20 09      JR           NZ,$135A
1351: AF         XOR         A
1352: EA 22 C1   LD           ($C122),A
1355: 3E 0C      LD           A,$0C
1357: EA 6D C1   LD           ($C16D),A
135A: 3E 05      LD           A,$05
135C: CD EB 10   CALL       $10EB
135F: 38 22      JR           C,$1383
1361: AF         XOR         A
1362: EA 9B C1   LD           ($C19B),A
1365: 21 00 C2   LD           HL,$C200
1368: 19         ADD         HL,DE
1369: F0 CE      LD           A,($CE)
136B: C6 08      ADD         $08
136D: 77         LD           (HL),A
136E: 21 10 C2   LD           HL,$C210
1371: 19         ADD         HL,DE
1372: F0 CD      LD           A,($CD)
1374: C6 10      ADD         $10
1376: 77         LD           (HL),A
1377: 21 B0 C3   LD           HL,$C3B0
137A: 19         ADD         HL,DE
137B: F0 F1      LD           A,($F1)
137D: 77         LD           (HL),A
137E: D5         PUSH       DE
137F: C1         POP         BC
1380: CD 03 38   CALL       $3803
1383: CD ED 27   CALL       $27ED
1386: E6 07      AND         $07
1388: C0         RET         NZ
1389: F0 AF      LD           A,($AF)
138B: FE D3      CP           $D3
138D: C8         RET         Z
138E: CD ED 27   CALL       $27ED
1391: 1F         RRA
1392: 3E 2E      LD           A,$2E
1394: 30 02      JR           NC,$1398
1396: 3E 2D      LD           A,$2D
1398: CD 01 3C   CALL       $3C01
139B: D8         RET         C
139C: 21 00 C2   LD           HL,$C200
139F: 19         ADD         HL,DE
13A0: F0 CE      LD           A,($CE)
13A2: C6 08      ADD         $08
13A4: 77         LD           (HL),A
13A5: 21 10 C2   LD           HL,$C210
13A8: 19         ADD         HL,DE
13A9: F0 CD      LD           A,($CD)
13AB: C6 10      ADD         $10
13AD: 77         LD           (HL),A
13AE: 21 50 C4   LD           HL,$C450
13B1: 19         ADD         HL,DE
13B2: 36 80      LD           (HL),$80
13B4: 21 F0 C2   LD           HL,$C2F0
13B7: 19         ADD         HL,DE
13B8: 36 18      LD           (HL),$18
13BA: 21 20 C3   LD           HL,$C320
13BD: 19         ADD         HL,DE
13BE: 36 10      LD           (HL),$10
13C0: C9         RET
13C1: 12         LD           (DE),A
13C2: EE FC      XOR         $FC
13C4: 04         INC         B
13C5: 04         INC         B
13C6: 04         INC         B
13C7: EE 12      XOR         $12
13C9: 4F         LD           C,A
13CA: FA 6D C1   LD           A,($C16D)
13CD: A7         AND         A
13CE: C8         RET         Z
13CF: F0 9E      LD           A,($9E)
13D1: 5F         LD           E,A
13D2: 16 00      LD           D,$00
13D4: 21 C1 13   LD           HL,$13C1
13D7: 19         ADD         HL,DE
13D8: F0 98      LD           A,($98)
13DA: 86         ADD         A,(HL)
13DB: E0 D7      LDFF00   ($D7),A
13DD: 21 C5 13   LD           HL,$13C5
13E0: 19         ADD         HL,DE
13E1: F0 99      LD           A,($99)
13E3: 86         ADD         A,(HL)
13E4: E0 D8      LDFF00   ($D8),A
13E6: 3E 04      LD           A,$04
13E8: EA 02 C5   LD           ($C502),A
13EB: CD A1 09   CALL       $09A1
13EE: 3E 10      LD           A,$10
13F0: EA C4 C1   LD           ($C1C4),A
13F3: 79         LD           A,C
13F4: E6 F0      AND         $F0
13F6: FE 90      CP           $90
13F8: 28 05      JR           Z,$13FF
13FA: 3E 07      LD           A,$07
13FC: E0 F2      LDFF00   ($F2),A
13FE: C9         RET
13FF: 3E 17      LD           A,$17
1401: E0 F4      LDFF00   ($F4),A
1403: C9         RET
1404: 20 E0      JR           NZ,$13E6
1406: 00         NOP
1407: 00         NOP
1408: 00         NOP
1409: 00         NOP
140A: E0 20      LDFF00   ($20),A
140C: F0 F9      LD           A,($F9)
140E: A7         AND         A
140F: 28 09      JR           Z,$141A
1411: F0 9C      LD           A,($9C)
1413: A7         AND         A
1414: C0         RET         NZ
1415: F0 9E      LD           A,($9E)
1417: E6 02      AND         $02
1419: C0         RET         NZ
141A: FA 4A C1   LD           A,($C14A)
141D: A7         AND         A
141E: C0         RET         NZ
141F: F0 A2      LD           A,($A2)
1421: 21 46 C1   LD           HL,$C146
1424: B6         OR           (HL)
1425: C0         RET         NZ
1426: FA 20 C1   LD           A,($C120)
1429: C6 02      ADD         $02
142B: EA 20 C1   LD           ($C120),A
142E: CD 5D 14   CALL       $145D
1431: FA 4B C1   LD           A,($C14B)
1434: 3C         INC         A
1435: EA 4B C1   LD           ($C14B),A
1438: FE 20      CP           $20
143A: C0         RET         NZ
143B: EA 4A C1   LD           ($C14A),A
143E: AF         XOR         A
143F: EA 21 C1   LD           ($C121),A
1442: EA 22 C1   LD           ($C122),A
1445: F0 9E      LD           A,($9E)
1447: 5F         LD           E,A
1448: 16 00      LD           D,$00
144A: 21 04 14   LD           HL,$1404
144D: 19         ADD         HL,DE
144E: 7E         LD           A,(HL)
144F: E0 9A      LDFF00   ($9A),A
1451: 21 08 14   LD           HL,$1408
1454: 19         ADD         HL,DE
1455: 7E         LD           A,(HL)
1456: E0 9B      LDFF00   ($9B),A
1458: AF         XOR         A
1459: EA AC C1   LD           ($C1AC),A
145C: C9         RET
145D: F0 E7      LD           A,($E7)
145F: E6 07      AND         $07
1461: 21 A2 FF   LD           HL,$FFA2
1464: B6         OR           (HL)
1465: 21 A1 FF   LD           HL,$FFA1
1468: B6         OR           (HL)
1469: 21 46 C1   LD           HL,$C146
146C: B6         OR           (HL)
146D: C0         RET         NZ
146E: F0 98      LD           A,($98)
1470: E0 D7      LDFF00   ($D7),A
1472: FA 81 C1   LD           A,($C181)
1475: FE 05      CP           $05
1477: 28 0F      JR           Z,$1488
1479: 3E 07      LD           A,$07
147B: E0 F4      LDFF00   ($F4),A
147D: F0 99      LD           A,($99)
147F: C6 06      ADD         $06
1481: E0 D8      LDFF00   ($D8),A
1483: 3E 0B      LD           A,$0B
1485: C3 53 09   JP           $0953
1488: F0 99      LD           A,($99)
148A: E0 D8      LDFF00   ($D8),A
148C: 3E 0E      LD           A,$0E
148E: E0 F2      LDFF00   ($F2),A
1490: 3E 0C      LD           A,$0C
1492: C3 53 09   JP           $0953
1495: AF         XOR         A
1496: E0 9A      LDFF00   ($9A),A
1498: E0 9B      LDFF00   ($9B),A
149A: C9         RET
149B: CD FA 77   CALL       $77FA
149E: FA 1C C1   LD           A,($C11C)
14A1: FE 01      CP           $01
14A3: C8         RET         Z
14A4: FA 6A C1   LD           A,($C16A)
14A7: A7         AND         A
14A8: 28 38      JR           Z,$14E2
14AA: 01 10 C0   LD           BC,$C010
14AD: FA 45 C1   LD           A,($C145)
14B0: 21 3B C1   LD           HL,$C13B
14B3: 86         ADD         A,(HL)
14B4: E0 D7      LDFF00   ($D7),A
14B6: F0 98      LD           A,($98)
14B8: E0 D8      LDFF00   ($D8),A
14BA: 21 DA FF   LD           HL,$FFDA
14BD: 36 00      LD           (HL),$00
14BF: FA 22 C1   LD           A,($C122)
14C2: FE 28      CP           $28
14C4: 38 07      JR           C,$14CD
14C6: F0 E7      LD           A,($E7)
14C8: 17         RLA
14C9: 17         RLA
14CA: E6 10      AND         $10
14CC: 77         LD           (HL),A
14CD: FA 39 C1   LD           A,($C139)
14D0: 67         LD           H,A
14D1: FA 3A C1   LD           A,($C13A)
14D4: 6F         LD           L,A
14D5: FA 36 C1   LD           A,($C136)
14D8: E0 D9      LDFF00   ($D9),A
14DA: F0 99      LD           A,($99)
14DC: FE 88      CP           $88
14DE: D0         RET         NC
14DF: C3 40 15   JP           $1540
14E2: FA 9B C1   LD           A,($C19B)
14E5: F5         PUSH       AF
14E6: CB 7F      BIT         7,A
14E8: CA 1B 15   JP           Z,$151B
14EB: 3E 02      LD           A,$02
14ED: CD B9 07   CALL       $07B9
14F0: CD 4B 51   CALL       $514B
14F3: FA 9B C1   LD           A,($C19B)
14F6: E6 7F      AND         $7F
14F8: FE 0C      CP           $0C
14FA: 20 1F      JR           NZ,$151B
14FC: 21 9F C1   LD           HL,$C19F
14FF: FA 24 C1   LD           A,($C124)
1502: B6         OR           (HL)
1503: 20 16      JR           NZ,$151B
1505: CD 83 12   CALL       $1283
1508: 3E 04      LD           A,$04
150A: CD EB 10   CALL       $10EB
150D: 38 0C      JR           C,$151B
150F: 3E 0D      LD           A,$0D
1511: E0 F4      LDFF00   ($F4),A
1513: 3E 02      LD           A,$02
1515: CD B9 07   CALL       $07B9
1518: CD C6 51   CALL       $51C6
151B: F1         POP         AF
151C: EA 9B C1   LD           ($C19B),A
151F: C9         RET
1520: 08 06 0C   LD           ($0C06),SP
1523: 0A         LD           A,(BC)
1524: FF         RST         0X38
1525: 04         INC         B
1526: 0A         LD           A,(BC)
1527: 0C         INC         C
1528: 06 08      LD           B,$08
152A: 0A         LD           A,(BC)
152B: 0C         INC         C
152C: FF         RST         0X38
152D: 04         INC         B
152E: 0C         INC         C
152F: 0A         LD           A,(BC)
1530: 20 20      JR           NZ,$1552
1532: 60         LD           H,B
1533: 60         LD           H,B
1534: 00         NOP
1535: 00         NOP
1536: 40         LD           B,B
1537: 40         LD           B,B
1538: 00         NOP
1539: 00         NOP
153A: 00         NOP
153B: 00         NOP
153C: 40         LD           B,B
153D: 40         LD           B,B
153E: 20 20      JR           NZ,$1560
1540: E5         PUSH       HL
1541: F0 D7      LD           A,($D7)
1543: 84         ADD         A,H
1544: 02         LD           (BC),A
1545: 03         INC         BC
1546: F0 D8      LD           A,($D8)
1548: 85         ADD         A,L
1549: 02         LD           (BC),A
154A: 03         INC         BC
154B: 21 20 15   LD           HL,$1520
154E: F0 D9      LD           A,($D9)
1550: CB 27      SLA         A
1552: 5F         LD           E,A
1553: 16 00      LD           D,$00
1555: 19         ADD         HL,DE
1556: 7E         LD           A,(HL)
1557: 02         LD           (BC),A
1558: FE FF      CP           $FF
155A: 20 05      JR           NZ,$1561
155C: 0B         DEC         BC
155D: 3E F0      LD           A,$F0
155F: 02         LD           (BC),A
1560: 03         INC         BC
1561: 03         INC         BC
1562: 21 30 15   LD           HL,$1530
1565: 19         ADD         HL,DE
1566: 7E         LD           A,(HL)
1567: 21 DA FF   LD           HL,$FFDA
156A: B6         OR           (HL)
156B: 02         LD           (BC),A
156C: 03         INC         BC
156D: E1         POP         HL
156E: F0 D7      LD           A,($D7)
1570: 84         ADD         A,H
1571: 02         LD           (BC),A
1572: 03         INC         BC
1573: F0 D8      LD           A,($D8)
1575: 85         ADD         A,L
1576: C6 08      ADD         $08
1578: 02         LD           (BC),A
1579: 03         INC         BC
157A: 21 21 15   LD           HL,$1521
157D: 19         ADD         HL,DE
157E: 7E         LD           A,(HL)
157F: 02         LD           (BC),A
1580: 03         INC         BC
1581: 21 31 15   LD           HL,$1531
1584: 19         ADD         HL,DE
1585: 7E         LD           A,(HL)
1586: 21 DA FF   LD           HL,$FFDA
1589: B6         OR           (HL)
158A: 02         LD           (BC),A
158B: C9         RET
158C: 10 F0      STOP       $F0
158E: 08 08 0C   LD           ($0C08),SP
1591: 0C         INC         C
1592: F0 10      LD           A,($10)
1594: F0 9E      LD           A,($9E)
1596: 5F         LD           E,A
1597: 16 00      LD           D,$00
1599: 21 8C 15   LD           HL,$158C
159C: 19         ADD         HL,DE
159D: F0 98      LD           A,($98)
159F: 86         ADD         A,(HL)
15A0: EA 79 C1   LD           ($C179),A
15A3: 21 90 15   LD           HL,$1590
15A6: 19         ADD         HL,DE
15A7: F0 99      LD           A,($99)
15A9: 86         ADD         A,(HL)
15AA: EA 7A C1   LD           ($C17A),A
15AD: 3E 02      LD           A,$02
15AF: EA 78 C1   LD           ($C178),A
15B2: C9         RET
15B3: CD 0F 78   CALL       $780F
15B6: FA C9 C3   LD           A,($C3C9)
15B9: A7         AND         A
15BA: 28 07      JR           Z,$15C3
15BC: AF         XOR         A
15BD: EA C9 C3   LD           ($C3C9),A
15C0: C3 09 09   JP           $0909
15C3: CD 76 17   CALL       $1776
15C6: AF         XOR         A
15C7: EA 57 C1   LD           ($C157),A
15CA: 3C         INC         A
15CB: EA A8 C1   LD           ($C1A8),A
15CE: FA 6B C1   LD           A,($C16B)
15D1: FE 04      CP           $04
15D3: C2 2D 17   JP           NZ,$172D
15D6: AF         XOR         A
15D7: E0 96      LDFF00   ($96),A
15D9: E0 97      LDFF00   ($97),A
15DB: E0 B4      LDFF00   ($B4),A
15DD: 1E 10      LD           E,$10
15DF: 21 80 C2   LD           HL,$C280
15E2: 22         LD           (HLI),A
15E3: 1D         DEC         E
15E4: 20 FC      JR           NZ,$15E2
15E6: FA 09 C5   LD           A,($C509)
15E9: A7         AND         A
15EA: 28 1A      JR           Z,$1606
15EC: F5         PUSH       AF
15ED: 3E 04      LD           A,$04
15EF: CD B9 07   CALL       $07B9
15F2: F1         POP         AF
15F3: CD E3 79   CALL       $79E3
15F6: 21 6E DB   LD           HL,$DB6E
15F9: 34         INC         (HL)
15FA: 21 46 DB   LD           HL,$DB46
15FD: 34         INC         (HL)
15FE: 3E 01      LD           A,$01
1600: EA 7E D4   LD           ($D47E),A
1603: AF         XOR         A
1604: E0 9D      LDFF00   ($9D),A
1606: F0 F9      LD           A,($F9)
1608: E0 E4      LDFF00   ($E4),A
160A: 3E 0B      LD           A,$0B
160C: EA 95 DB   LD           ($DB95),A
160F: AF         XOR         A
1610: EA 96 DB   LD           ($DB96),A
1613: EA CB C3   LD           ($C3CB),A
1616: E0 F9      LDFF00   ($F9),A
1618: 21 01 D4   LD           HL,$D401
161B: FA A5 DB   LD           A,($DBA5)
161E: E0 E6      LDFF00   ($E6),A
1620: A7         AND         A
1621: 20 2A      JR           NZ,$164D
1623: 21 16 D4   LD           HL,$D416
1626: 0E 00      LD           C,$00
1628: F0 98      LD           A,($98)
162A: CB 37      SWAP       A
162C: E6 0F      AND         $0F
162E: 5F         LD           E,A
162F: F0 99      LD           A,($99)
1631: D6 08      SUB         $08
1633: E6 F0      AND         $F0
1635: B3         OR           E
1636: BE         CP           (HL)
1637: 28 07      JR           Z,$1640
1639: 23         INC         HL
163A: 0C         INC         C
163B: 79         LD           A,C
163C: FE 04      CP           $04
163E: 20 E8      JR           NZ,$1628
1640: 79         LD           A,C
1641: CB 27      SLA         A
1643: CB 27      SLA         A
1645: 81         ADD         A,C
1646: 5F         LD           E,A
1647: 16 00      LD           D,$00
1649: 21 01 D4   LD           HL,$D401
164C: 19         ADD         HL,DE
164D: E5         PUSH       HL
164E: 2A         LD           A,(HLI)
164F: EA A5 DB   LD           ($DBA5),A
1652: FE 02      CP           $02
1654: 20 0A      JR           NZ,$1660
1656: E0 F9      LDFF00   ($F9),A
1658: 3D         DEC         A
1659: EA A5 DB   LD           ($DBA5),A
165C: 3E 01      LD           A,$01
165E: E0 9C      LDFF00   ($9C),A
1660: 2A         LD           A,(HLI)
1661: E0 F7      LDFF00   ($F7),A
1663: FA A5 DB   LD           A,($DBA5)
1666: A7         AND         A
1667: 2A         LD           A,(HLI)
1668: E0 F6      LDFF00   ($F6),A
166A: 20 0B      JR           NZ,$1677
166C: F0 E6      LD           A,($E6)
166E: A7         AND         A
166F: 28 04      JR           Z,$1675
1671: AF         XOR         A
1672: EA 7C D4   LD           ($D47C),A
1675: 18 5D      JR           $16D4
1677: 4F         LD           C,A
1678: 3E 14      LD           A,$14
167A: CD B9 07   CALL       $07B9
167D: E5         PUSH       HL
167E: F0 F7      LD           A,($F7)
1680: CB 37      SWAP       A
1682: 5F         LD           E,A
1683: 16 00      LD           D,$00
1685: CB 23      SLA         E
1687: CB 12      RL           D
1689: CB 23      SLA         E
168B: CB 12      RL           D
168D: 21 00 42   LD           HL,$4200
1690: 19         ADD         HL,DE
1691: F0 F7      LD           A,($F7)
1693: FE 06      CP           $06
1695: 20 0A      JR           NZ,$16A1
1697: FA 6B DB   LD           A,($DB6B)
169A: E6 04      AND         $04
169C: 28 03      JR           Z,$16A1
169E: 21 C0 44   LD           HL,$44C0
16A1: 1E 00      LD           E,$00
16A3: 2A         LD           A,(HLI)
16A4: B9         CP           C
16A5: 28 06      JR           Z,$16AD
16A7: 1C         INC         E
16A8: 7B         LD           A,E
16A9: FE 40      CP           $40
16AB: 20 F6      JR           NZ,$16A3
16AD: 7B         LD           A,E
16AE: EA AE DB   LD           ($DBAE),A
16B1: F0 E6      LD           A,($E6)
16B3: A7         AND         A
16B4: 20 1D      JR           NZ,$16D3
16B6: AF         XOR         A
16B7: EA 7C D4   LD           ($D47C),A
16BA: F0 F7      LD           A,($F7)
16BC: FE 0A      CP           $0A
16BE: 30 13      JR           NC,$16D3
16C0: 3E 02      LD           A,$02
16C2: CD B9 07   CALL       $07B9
16C5: CD 9B 6A   CALL       $6A9B
16C8: 3E 30      LD           A,$30
16CA: E0 B4      LDFF00   ($B4),A
16CC: AF         XOR         A
16CD: EA FB D6   LD           ($D6FB),A
16D0: EA F8 D6   LD           ($D6F8),A
16D3: E1         POP         HL
16D4: 2A         LD           A,(HLI)
16D5: EA 9D DB   LD           ($DB9D),A
16D8: 7E         LD           A,(HL)
16D9: EA 9E DB   LD           ($DB9E),A
16DC: E1         POP         HL
16DD: F0 F9      LD           A,($F9)
16DF: A7         AND         A
16E0: 20 4C      JR           NZ,$172E
16E2: F0 E4      LD           A,($E4)
16E4: A7         AND         A
16E5: 20 46      JR           NZ,$172D
16E7: FA A5 DB   LD           A,($DBA5)
16EA: A7         AND         A
16EB: 28 29      JR           Z,$1716
16ED: F0 F7      LD           A,($F7)
16EF: FE 0A      CP           $0A
16F1: 30 23      JR           NC,$1716
16F3: 5F         LD           E,A
16F4: CB 27      SLA         A
16F6: CB 27      SLA         A
16F8: 83         ADD         A,E
16F9: 5F         LD           E,A
16FA: 16 00      LD           D,$00
16FC: 21 E5 53   LD           HL,$53E5
16FF: 19         ADD         HL,DE
1700: 3E 14      LD           A,$14
1702: EA 00 21   LD           ($2100),A
1705: CD 16 17   CALL       $1716
1708: D5         PUSH       DE
1709: F0 F7      LD           A,($F7)
170B: 5F         LD           E,A
170C: 16 00      LD           D,$00
170E: 21 12 54   LD           HL,$5412
1711: 19         ADD         HL,DE
1712: 7E         LD           A,(HL)
1713: D1         POP         DE
1714: 12         LD           (DE),A
1715: C9         RET
1716: 3E 00      LD           A,$00
1718: E0 D7      LDFF00   ($D7),A
171A: 11 5F DB   LD           DE,$DB5F
171D: 2A         LD           A,(HLI)
171E: 12         LD           (DE),A
171F: 13         INC         DE
1720: F0 D7      LD           A,($D7)
1722: 3C         INC         A
1723: E0 D7      LDFF00   ($D7),A
1725: FE 05      CP           $05
1727: 20 F4      JR           NZ,$171D
1729: FA AE DB   LD           A,($DBAE)
172C: 12         LD           (DE),A
172D: C9         RET
172E: AF         XOR         A
172F: E0 9E      LDFF00   ($9E),A
1731: C9         RET
1732: CD 0F 78   CALL       $780F
1735: FA 74 D4   LD           A,($D474)
1738: A7         AND         A
1739: 28 15      JR           Z,$1750
173B: AF         XOR         A
173C: EA 74 D4   LD           ($D474),A
173F: 3E 30      LD           A,$30
1741: EA 80 C1   LD           ($C180),A
1744: 3E 03      LD           A,$03
1746: EA 7F C1   LD           ($C17F),A
1749: 3E 04      LD           A,$04
174B: EA 6B C1   LD           ($C16B),A
174E: 18 0A      JR           $175A
1750: CD C3 17   CALL       $17C3
1753: FA 6B C1   LD           A,($C16B)
1756: FE 04      CP           $04
1758: 20 1B      JR           NZ,$1775
175A: FA 63 D4   LD           A,($D463)
175D: FE 01      CP           $01
175F: 28 02      JR           Z,$1763
1761: 3E 00      LD           A,$00
1763: EA 1C C1   LD           ($C11C),A
1766: FA 7E D4   LD           A,($D47E)
1769: A7         AND         A
176A: 28 09      JR           Z,$1775
176C: AF         XOR         A
176D: EA 7E D4   LD           ($D47E),A
1770: 3E 36      LD           A,$36
1772: CD 97 21   CALL       $2197
1775: C9         RET
1776: 21 6C C1   LD           HL,$C16C
1779: 34         INC         (HL)
177A: FA 6C C1   LD           A,($C16C)
177D: E6 03      AND         $03
177F: 20 35      JR           NZ,$17B6
1781: 21 6B C1   LD           HL,$C16B
1784: 7E         LD           A,(HL)
1785: FE 04      CP           $04
1787: 28 2D      JR           Z,$17B6
1789: 34         INC         (HL)
178A: AF         XOR         A
178B: E0 D7      LDFF00   ($D7),A
178D: F0 D7      LD           A,($D7)
178F: FE 03      CP           $03
1791: 28 23      JR           Z,$17B6
1793: 21 97 DB   LD           HL,$DB97
1796: 5F         LD           E,A
1797: 16 00      LD           D,$00
1799: 19         ADD         HL,DE
179A: 7E         LD           A,(HL)
179B: 4F         LD           C,A
179C: 06 00      LD           B,$00
179E: 79         LD           A,C
179F: E6 03      AND         $03
17A1: 28 01      JR           Z,$17A4
17A3: 0D         DEC         C
17A4: CB 09      RRC         C
17A6: CB 09      RRC         C
17A8: 04         INC         B
17A9: 78         LD           A,B
17AA: FE 04      CP           $04
17AC: 20 F0      JR           NZ,$179E
17AE: 79         LD           A,C
17AF: 77         LD           (HL),A
17B0: 21 D7 FF   LD           HL,$FFD7
17B3: 34         INC         (HL)
17B4: 18 D7      JR           $178D
17B6: C9         RET
17B7: 00         NOP
17B8: 01 02 03   LD           BC,$0302
17BB: 00         NOP
17BC: 03         INC         BC
17BD: 01 00 00   LD           BC,$0000
17C0: 01 02 03   LD           BC,$0302
17C3: 21 6C C1   LD           HL,$C16C
17C6: 34         INC         (HL)
17C7: FA 6C C1   LD           A,($C16C)
17CA: E6 03      AND         $03
17CC: 20 44      JR           NZ,$1812
17CE: 21 6B C1   LD           HL,$C16B
17D1: 7E         LD           A,(HL)
17D2: 34         INC         (HL)
17D3: FE 04      CP           $04
17D5: 28 DF      JR           Z,$17B6
17D7: AF         XOR         A
17D8: E0 D7      LDFF00   ($D7),A
17DA: F0 D7      LD           A,($D7)
17DC: FE 03      CP           $03
17DE: 28 32      JR           Z,$1812
17E0: 21 97 DB   LD           HL,$DB97
17E3: 5F         LD           E,A
17E4: 16 00      LD           D,$00
17E6: 19         ADD         HL,DE
17E7: 7E         LD           A,(HL)
17E8: E5         PUSH       HL
17E9: 4F         LD           C,A
17EA: 06 00      LD           B,$00
17EC: F0 D7      LD           A,($D7)
17EE: CB 27      SLA         A
17F0: CB 27      SLA         A
17F2: B0         OR           B
17F3: 5F         LD           E,A
17F4: 21 B7 17   LD           HL,$17B7
17F7: 19         ADD         HL,DE
17F8: 79         LD           A,C
17F9: E6 03      AND         $03
17FB: BE         CP           (HL)
17FC: 28 01      JR           Z,$17FF
17FE: 0C         INC         C
17FF: CB 09      RRC         C
1801: CB 09      RRC         C
1803: 04         INC         B
1804: 78         LD           A,B
1805: FE 04      CP           $04
1807: 20 E3      JR           NZ,$17EC
1809: 79         LD           A,C
180A: E1         POP         HL
180B: 77         LD           (HL),A
180C: 21 D7 FF   LD           HL,$FFD7
180F: 34         INC         (HL)
1810: 18 C8      JR           $17DA
1812: C9         RET
1813: 00         NOP
1814: 02         LD           (BC),A
1815: 02         LD           (BC),A
1816: 00         NOP
1817: 10 02      STOP       $02
1819: 12         LD           (DE),A
181A: 00         NOP
181B: 04         INC         B
181C: 06 06      LD           B,$06
181E: 04         INC         B
181F: 08 0A 0C   LD           ($0C0A),SP
1822: 0E 18      LD           C,$18
1824: 0A         LD           A,(BC)
1825: 1C         INC         E
1826: 0E 0A      LD           C,$0A
1828: 08 0E 0C   LD           ($0C0E),SP
182B: 0A         LD           A,(BC)
182C: 18 0E      JR           $183C
182E: 1C         INC         E
182F: 20 22      JR           NZ,$1853
1831: 24         INC         H
1832: 26 28      LD           H,$28
1834: 2A         LD           A,(HLI)
1835: 2A         LD           A,(HLI)
1836: 28 30      JR           Z,$1868
1838: 32         LD           (HLD),A
1839: 20 22      JR           NZ,$185D
183B: 34         INC         (HL)
183C: 36 24      LD           (HL),$24
183E: 26 38      LD           H,$38
1840: 3A         LD           A,(HLD)
1841: 28 2A      JR           Z,$186D
1843: 3A         LD           A,(HLD)
1844: 38 2A      JR           C,$1870
1846: 28 40      JR           Z,$1888
1848: 40         LD           B,B
1849: 42         LD           B,D
184A: 42         LD           B,D
184B: 44         LD           B,H
184C: 46         LD           B,(HL)
184D: 48         LD           C,B
184E: 4A         LD           C,D
184F: 4C         LD           C,H
1850: 4E         LD           C,(HL)
1851: 50         LD           D,B
1852: 52         LD           D,D
1853: 4E         LD           C,(HL)
1854: 4C         LD           C,H
1855: 52         LD           D,D
1856: 50         LD           D,B
1857: 80         ADD         A,B
1858: 02         LD           (BC),A
1859: 82         ADD         A,D
185A: 00         NOP
185B: 84         ADD         A,H
185C: 86         ADD         A,(HL)
185D: 88         ADC         A,B
185E: 8A         ADC         A,D
185F: 8C         ADC         A,H
1860: 8E         ADC         A,(HL)
1861: 90         SUB         B
1862: 92         SUB         D
1863: 94         SUB         H
1864: 96         SUB         (HL)
1865: 98         SBC         B
1866: 9A         SBC         D
1867: 9C         SBC         H
1868: 9E         SBC         (HL)
1869: 9A         SBC         D
186A: A2         AND         D
186B: A4         AND         H
186C: 08 A6 0C   LD           ($0CA6),SP
186F: A8         XOR         B
1870: AA         XOR         D
1871: AC         XOR         H
1872: AE         XOR         (HL)
1873: B0         OR           B
1874: B2         OR           D
1875: B4         OR           H
1876: B6         OR           (HL)
1877: B0         OR           B
1878: B2         OR           D
1879: B4         OR           H
187A: B6         OR           (HL)
187B: 04         INC         B
187C: C0         RET         NZ
187D: 06 C2      LD           B,$C2
187F: 5A         LD           E,D
1880: 58         LD           E,B
1881: 5E         LD           E,(HL)
1882: 5C         LD           E,H
1883: 58         LD           E,B
1884: 5A         LD           E,D
1885: 5C         LD           E,H
1886: 5E         LD           E,(HL)
1887: 44         LD           B,H
1888: 46         LD           B,(HL)
1889: 6E         LD           L,(HL)
188A: 6E         LD           L,(HL)
188B: 40         LD           B,B
188C: 40         LD           B,B
188D: 56         LD           D,(HL)
188E: 56         LD           D,(HL)
188F: 7A         LD           A,D
1890: 78         LD           A,B
1891: 7E         LD           A,(HL)
1892: 7C         LD           A,H
1893: 78         LD           A,B
1894: 7A         LD           A,D
1895: 7C         LD           A,H
1896: 7E         LD           A,(HL)
1897: 74         LD           (HL),H
1898: 76         HALT
1899: 76         HALT
189A: 74         LD           (HL),H
189B: 70         LD           (HL),B
189C: 72         LD           (HL),D
189D: 72         LD           (HL),D
189E: 70         LD           (HL),B
189F: CA C8 D6   JP           Z,$D6C8
18A2: D4 C8 CA   CALL       NC,$CAC8
18A5: D4 D6 CC   CALL       NC,$CCD6
18A8: CE D8      ADC         $D8
18AA: DA C4 C4   JP           C,$C4C4
18AD: C6 C6      ADD         $C6
18AF: DC DC DE   CALL       C,$DEDC
18B2: DE EA      SBC         $EA
18B4: EC                              
18B5: EE F0      XOR         $F0
18B7: F2                              
18B8: F4                              
18B9: F6 F6      OR           $F6
18BB: F8 FA      LDHL       SP,$FA
18BD: E0 E2      LDFF00   ($E2),A
18BF: E4                              
18C0: E6 E8      AND         $E8
18C2: E8 10      ADD         SP,$10
18C4: 12         LD           (DE),A
18C5: 14         INC         D
18C6: 16 18      LD           D,$18
18C8: 1C         INC         E
18C9: 12         LD           (DE),A
18CA: 10 16      STOP       $16
18CC: 14         INC         D
18CD: 1C         INC         E
18CE: 18 66      JR           $1936
18D0: 68         LD           L,B
18D1: 6A         LD           L,D
18D2: 6C         LD           L,H
18D3: 68         LD           L,B
18D4: 66         LD           H,(HL)
18D5: 68         LD           L,B
18D6: 66         LD           H,(HL)
18D7: 6C         LD           L,H
18D8: 6A         LD           L,D
18D9: 66         LD           H,(HL)
18DA: 68         LD           L,B
18DB: 60         LD           H,B
18DC: 60         LD           H,B
18DD: 62         LD           H,D
18DE: 62         LD           H,D
18DF: 64         LD           H,H
18E0: 64         LD           H,H
18E1: 62         LD           H,D
18E2: 62         LD           H,D
18E3: 64         LD           H,H
18E4: 64         LD           H,H
18E5: 60         LD           H,B
18E6: 60         LD           H,B
18E7: 54         LD           D,H
18E8: 54         LD           D,H
18E9: 3C         INC         A
18EA: 3E FE      LD           A,$FE
18EC: FE 18      CP           $18
18EE: 1A         LD           A,(DE)
18EF: 1C         INC         E
18F0: 1E 2C      LD           E,$2C
18F2: 2E B8      LD           L,$B8
18F4: BA         CP           D
18F5: 2E 2C      LD           L,$2C
18F7: BA         CP           D
18F8: B8         CP           B
18F9: BC         CP           H
18FA: BE         CP           (HL)
18FB: D0         RET         NC
18FC: D2 A0 FC   JP           NC,$FCA0
18FF: FC                              
1900: A0         AND         B
1901: 00         NOP
1902: 00         NOP
1903: 20 20      JR           NZ,$1925
1905: 00         NOP
1906: 00         NOP
1907: 00         NOP
1908: 20 00      JR           NZ,$190A
190A: 00         NOP
190B: 20 20      JR           NZ,$192D
190D: 00         NOP
190E: 00         NOP
190F: 00         NOP
1910: 00         NOP
1911: 00         NOP
1912: 00         NOP
1913: 00         NOP
1914: 00         NOP
1915: 20 20      JR           NZ,$1937
1917: 20 20      JR           NZ,$1939
1919: 20 20      JR           NZ,$193B
191B: 20 20      JR           NZ,$193D
191D: 00         NOP
191E: 00         NOP
191F: 00         NOP
1920: 00         NOP
1921: 00         NOP
1922: 00         NOP
1923: 20 20      JR           NZ,$1945
1925: 00         NOP
1926: 00         NOP
1927: 00         NOP
1928: 00         NOP
1929: 00         NOP
192A: 00         NOP
192B: 00         NOP
192C: 00         NOP
192D: 00         NOP
192E: 00         NOP
192F: 00         NOP
1930: 00         NOP
1931: 20 20      JR           NZ,$1953
1933: 20 20      JR           NZ,$1955
1935: 00         NOP
1936: 20 00      JR           NZ,$1938
1938: 20 00      JR           NZ,$193A
193A: 00         NOP
193B: 00         NOP
193C: 00         NOP
193D: 00         NOP
193E: 00         NOP
193F: 00         NOP
1940: 00         NOP
1941: 20 20      JR           NZ,$1963
1943: 20 20      JR           NZ,$1965
1945: 00         NOP
1946: 00         NOP
1947: 00         NOP
1948: 20 00      JR           NZ,$194A
194A: 00         NOP
194B: 00         NOP
194C: 00         NOP
194D: 00         NOP
194E: 00         NOP
194F: 00         NOP
1950: 00         NOP
1951: 00         NOP
1952: 00         NOP
1953: 00         NOP
1954: 00         NOP
1955: 00         NOP
1956: 00         NOP
1957: 20 00      JR           NZ,$1959
1959: 00         NOP
195A: 20 00      JR           NZ,$195C
195C: 20 00      JR           NZ,$195E
195E: 00         NOP
195F: 00         NOP
1960: 00         NOP
1961: 00         NOP
1962: 00         NOP
1963: 00         NOP
1964: 00         NOP
1965: 00         NOP
1966: 00         NOP
1967: 00         NOP
1968: 00         NOP
1969: 00         NOP
196A: 00         NOP
196B: 20 00      JR           NZ,$196D
196D: 20 20      JR           NZ,$198F
196F: 20 20      JR           NZ,$1991
1971: 00         NOP
1972: 00         NOP
1973: 00         NOP
1974: 00         NOP
1975: 00         NOP
1976: 00         NOP
1977: 00         NOP
1978: 20 00      JR           NZ,$197A
197A: 20 00      JR           NZ,$197C
197C: 20 20      JR           NZ,$199E
197E: 20 20      JR           NZ,$19A0
1980: 20 00      JR           NZ,$1982
1982: 00         NOP
1983: 00         NOP
1984: 00         NOP
1985: 00         NOP
1986: 00         NOP
1987: 20 20      JR           NZ,$19A9
1989: 00         NOP
198A: 00         NOP
198B: 20 20      JR           NZ,$19AD
198D: 20 20      JR           NZ,$19AF
198F: 20 20      JR           NZ,$19B1
1991: 00         NOP
1992: 00         NOP
1993: 00         NOP
1994: 00         NOP
1995: 00         NOP
1996: 00         NOP
1997: 00         NOP
1998: 00         NOP
1999: 00         NOP
199A: 20 00      JR           NZ,$199C
199C: 20 00      JR           NZ,$199E
199E: 20 00      JR           NZ,$19A0
19A0: 20 00      JR           NZ,$19A2
19A2: 00         NOP
19A3: 00         NOP
19A4: 00         NOP
19A5: 00         NOP
19A6: 00         NOP
19A7: 00         NOP
19A8: 20 00      JR           NZ,$19AA
19AA: 00         NOP
19AB: 00         NOP
19AC: 00         NOP
19AD: 00         NOP
19AE: 00         NOP
19AF: 00         NOP
19B0: 20 00      JR           NZ,$19B2
19B2: 00         NOP
19B3: 00         NOP
19B4: 00         NOP
19B5: 00         NOP
19B6: 00         NOP
19B7: 20 20      JR           NZ,$19D9
19B9: 20 20      JR           NZ,$19DB
19BB: 20 20      JR           NZ,$19DD
19BD: 00         NOP
19BE: 00         NOP
19BF: 00         NOP
19C0: 00         NOP
19C1: 60         LD           H,B
19C2: 60         LD           H,B
19C3: 20 20      JR           NZ,$19E5
19C5: 20 20      JR           NZ,$19E7
19C7: 40         LD           B,B
19C8: 40         LD           B,B
19C9: 00         NOP
19CA: 20 00      JR           NZ,$19CC
19CC: 20 00      JR           NZ,$19CE
19CE: 20 40      JR           NZ,$1A10
19D0: 60         LD           H,B
19D1: 40         LD           B,B
19D2: 60         LD           H,B
19D3: 40         LD           B,B
19D4: 60         LD           H,B
19D5: 00         NOP
19D6: 20 00      JR           NZ,$19D8
19D8: 00         NOP
19D9: 00         NOP
19DA: 20 00      JR           NZ,$19DC
19DC: 00         NOP
19DD: 00         NOP
19DE: 00         NOP
19DF: 00         NOP
19E0: 00         NOP
19E1: 00         NOP
19E2: 00         NOP
19E3: 20 20      JR           NZ,$1A05
19E5: 20 20      JR           NZ,$1A07
19E7: 00         NOP
19E8: 00         NOP
19E9: 00         NOP
19EA: 00         NOP
19EB: 00         NOP
19EC: 00         NOP
19ED: 20 20      JR           NZ,$1A0F
19EF: FA 20 C1   LD           A,($C120)
19F2: CB 2F      SRA         A
19F4: CB 2F      SRA         A
19F6: CB 2F      SRA         A
19F8: E6 01      AND         $01
19FA: 57         LD           D,A
19FB: F0 9E      LD           A,($9E)
19FD: CB 27      SLA         A
19FF: B2         OR           D
1A00: 4F         LD           C,A
1A01: 06 00      LD           B,$00
1A03: 21 F6 48   LD           HL,$48F6
1A06: FA 1C C1   LD           A,($C11C)
1A09: FE 01      CP           $01
1A0B: 20 0A      JR           NZ,$1A17
1A0D: F0 9C      LD           A,($9C)
1A0F: A7         AND         A
1A10: 28 03      JR           Z,$1A15
1A12: 21 FE 48   LD           HL,$48FE
1A15: 18 4F      JR           $1A66
1A17: F0 F9      LD           A,($F9)
1A19: A7         AND         A
1A1A: 28 0B      JR           Z,$1A27
1A1C: F0 9C      LD           A,($9C)
1A1E: FE 02      CP           $02
1A20: 20 05      JR           NZ,$1A27
1A22: 21 06 49   LD           HL,$4906
1A25: 18 3F      JR           $1A66
1A27: FA 5C C1   LD           A,($C15C)
1A2A: FE 01      CP           $01
1A2C: 28 35      JR           Z,$1A63
1A2E: F0 B2      LD           A,($B2)
1A30: A7         AND         A
1A31: 20 06      JR           NZ,$1A39
1A33: FA 44 C1   LD           A,($C144)
1A36: A7         AND         A
1A37: 20 25      JR           NZ,$1A5E
1A39: FA 5A C1   LD           A,($C15A)
1A3C: A7         AND         A
1A3D: 20 05      JR           NZ,$1A44
1A3F: 21 BE 48   LD           HL,$48BE
1A42: 18 22      JR           $1A66
1A44: 21 C6 48   LD           HL,$48C6
1A47: FE 02      CP           $02
1A49: 20 03      JR           NZ,$1A4E
1A4B: 21 D6 48   LD           HL,$48D6
1A4E: FA 5B C1   LD           A,($C15B)
1A51: A7         AND         A
1A52: 28 08      JR           Z,$1A5C
1A54: 7D         LD           A,L
1A55: C6 08      ADD         $08
1A57: 6F         LD           L,A
1A58: 7C         LD           A,H
1A59: CE 00      ADC         $00
1A5B: 67         LD           H,A
1A5C: 18 08      JR           $1A66
1A5E: 21 E6 48   LD           HL,$48E6
1A61: 18 03      JR           $1A66
1A63: 21 EE 48   LD           HL,$48EE
1A66: 09         ADD         HL,BC
1A67: 7E         LD           A,(HL)
1A68: E0 9D      LDFF00   ($9D),A
1A6A: C9         RET
1A6B: FA 01 D6   LD           A,($D601)
1A6E: A7         AND         A
1A6F: C0         RET         NZ
1A70: 3E 10      LD           A,$10
1A72: EA 00 21   LD           ($2100),A
1A75: 21 00 65   LD           HL,$6500
1A78: 11 00 95   LD           DE,$9500
1A7B: F0 E7      LD           A,($E7)
1A7D: E6 0F      AND         $0F
1A7F: 28 06      JR           Z,$1A87
1A81: FE 08      CP           $08
1A83: C0         RET         NZ
1A84: 2E 40      LD           L,$40
1A86: 5D         LD           E,L
1A87: F0 E7      LD           A,($E7)
1A89: E6 30      AND         $30
1A8B: 4F         LD           C,A
1A8C: 06 00      LD           B,$00
1A8E: CB 21      SLA         C
1A90: CB 10      RL           B
1A92: CB 21      SLA         C
1A94: CB 10      RL           B
1A96: CB 21      SLA         C
1A98: CB 10      RL           B
1A9A: 09         ADD         HL,BC
1A9B: 01 40 00   LD           BC,$0040
1A9E: C3 C5 28   JP           $28C5
1AA1: 20 60      JR           NZ,$1B03
1AA3: A0         AND         B
1AA4: E0 E0      LDFF00   ($E0),A
1AA6: E0 A0      LDFF00   ($A0),A
1AA8: 60         LD           H,B
1AA9: FA 95 DB   LD           A,($DB95)
1AAC: FE 09      CP           $09
1AAE: 28 BB      JR           Z,$1A6B
1AB0: FE 00      CP           $00
1AB2: 20 2B      JR           NZ,$1ADF
1AB4: FA 01 D6   LD           A,($D601)
1AB7: A7         AND         A
1AB8: C2 DE 1A   JP           NZ,$1ADE
1ABB: F0 E7      LD           A,($E7)
1ABD: E6 0F      AND         $0F
1ABF: FE 04      CP           $04
1AC1: 38 1B      JR           C,$1ADE
1AC3: 3E 10      LD           A,$10
1AC5: EA 00 21   LD           ($2100),A
1AC8: FA 06 D0   LD           A,($D006)
1ACB: 6F         LD           L,A
1ACC: FA 07 D0   LD           A,($D007)
1ACF: 67         LD           H,A
1AD0: FA 08 D0   LD           A,($D008)
1AD3: 5F         LD           E,A
1AD4: FA 09 D0   LD           A,($D009)
1AD7: 57         LD           D,A
1AD8: 01 20 00   LD           BC,$0020
1ADB: CD C5 28   CALL       $28C5
1ADE: C9         RET
1ADF: FA 95 DB   LD           A,($DB95)
1AE2: FE 01      CP           $01
1AE4: 20 06      JR           NZ,$1AEC
1AE6: F0 A5      LD           A,($A5)
1AE8: A7         AND         A
1AE9: 20 30      JR           NZ,$1B1B
1AEB: C9         RET
1AEC: FE 0B      CP           $0B
1AEE: DA 14 1D   JP           C,$1D14
1AF1: FA 9A DB   LD           A,($DB9A)
1AF4: FE 80      CP           $80
1AF6: C2 14 1D   JP           NZ,$1D14
1AF9: FA 4F C1   LD           A,($C14F)
1AFC: A7         AND         A
1AFD: C2 CC 1C   JP           NZ,$1CCC
1B00: 21 24 C1   LD           HL,$C124
1B03: FA 01 D6   LD           A,($D601)
1B06: B6         OR           (HL)
1B07: C2 CC 1C   JP           NZ,$1CCC
1B0A: FA F8 D6   LD           A,($D6F8)
1B0D: A7         AND         A
1B0E: 28 06      JR           Z,$1B16
1B10: CD EE 1D   CALL       $1DEE
1B13: C3 CC 1C   JP           $1CCC
1B16: F0 A5      LD           A,($A5)
1B18: A7         AND         A
1B19: 28 4B      JR           Z,$1B66
1B1B: FE 01      CP           $01
1B1D: CA BD 3F   JP           Z,$3FBD
1B20: FE 02      CP           $02
1B22: CA D3 3F   JP           Z,$3FD3
1B25: FE 03      CP           $03
1B27: CA CF 1D   JP           Z,$1DCF
1B2A: FE 04      CP           $04
1B2C: CA D6 1D   JP           Z,$1DD6
1B2F: FE 08      CP           $08
1B31: CA 8C 1D   JP           Z,$1D8C
1B34: FE 09      CP           $09
1B36: CA BE 1D   JP           Z,$1DBE
1B39: FE 0A      CP           $0A
1B3B: CA 54 1D   JP           Z,$1D54
1B3E: FE 0B      CP           $0B
1B40: CA AD 1D   JP           Z,$1DAD
1B43: FE 0C      CP           $0C
1B45: CA 5C 1D   JP           Z,$1D5C
1B48: FE 0D      CP           $0D
1B4A: CA 2D 1D   JP           Z,$1D2D
1B4D: FE 0E      CP           $0E
1B4F: 28 0D      JR           Z,$1B5E
1B51: FE 0F      CP           $0F
1B53: CA 1C 1D   JP           Z,$1D1C
1B56: FE 10      CP           $10
1B58: CA 15 1D   JP           Z,$1D15
1B5B: C3 CC 1C   JP           $1CCC
1B5E: 3E 17      LD           A,$17
1B60: EA 00 21   LD           ($2100),A
1B63: C3 60 40   JP           $4060
1B66: F0 A6      LD           A,($A6)
1B68: 3C         INC         A
1B69: E0 A6      LDFF00   ($A6),A
1B6B: F0 A4      LD           A,($A4)
1B6D: C7         RST         0X00
1B6E: 5A         LD           E,D
1B6F: 1C         INC         E
1B70: 90         SUB         B
1B71: 1B         DEC         DE
1B72: AA         XOR         D
1B73: 1B         DEC         DE
1B74: AE         XOR         (HL)
1B75: 1B         DEC         DE
1B76: CD 1B F1   CALL       $F11B
1B79: 1B         DEC         DE
1B7A: F5         PUSH       AF
1B7B: 1B         DEC         DE
1B7C: 10 1C      STOP       $1C
1B7E: 21 1C 30   LD           HL,$301C
1B81: 1C         INC         E
1B82: 3F         CCF
1B83: 1C         INC         E
1B84: B6         OR           (HL)
1B85: 1B         DEC         DE
1B86: B2         OR           D
1B87: 1B         DEC         DE
1B88: 4A         LD           C,D
1B89: 1C         INC         E
1B8A: 56         LD           D,(HL)
1B8B: 1C         INC         E
1B8C: 4E         LD           C,(HL)
1B8D: 1C         INC         E
1B8E: 52         LD           D,D
1B8F: 1C         INC         E
1B90: F0 A6      LD           A,($A6)
1B92: E6 07      AND         $07
1B94: C2 5A 1C   JP           NZ,$1C5A
1B97: 3E 01      LD           A,$01
1B99: EA 00 21   LD           ($2100),A
1B9C: CD 62 5F   CALL       $5F62
1B9F: 3E 0C      LD           A,$0C
1BA1: EA 00 21   LD           ($2100),A
1BA4: C3 CC 1C   JP           $1CCC
1BA7: 6F         LD           L,A
1BA8: 18 3B      JR           $1BE5
1BAA: 26 6B      LD           H,$6B
1BAC: 18 0A      JR           $1BB8
1BAE: 26 6C      LD           H,$6C
1BB0: 18 06      JR           $1BB8
1BB2: 26 73      LD           H,$73
1BB4: 18 02      JR           $1BB8
1BB6: 26 6A      LD           H,$6A
1BB8: F0 A6      LD           A,($A6)
1BBA: E6 0F      AND         $0F
1BBC: C2 5A 1C   JP           NZ,$1C5A
1BBF: CD 43 1C   CALL       $1C43
1BC2: C3 A7 1B   JP           $1BA7
1BC5: 00         NOP
1BC6: 40         LD           B,B
1BC7: 80         ADD         A,B
1BC8: C0         RET         NZ
1BC9: C0         RET         NZ
1BCA: C0         RET         NZ
1BCB: 80         ADD         A,B
1BCC: 40         LD           B,B
1BCD: F0 A6      LD           A,($A6)
1BCF: E6 07      AND         $07
1BD1: C2 5A 1C   JP           NZ,$1C5A
1BD4: F0 A6      LD           A,($A6)
1BD6: 1F         RRA
1BD7: 1F         RRA
1BD8: 1F         RRA
1BD9: E6 07      AND         $07
1BDB: 5F         LD           E,A
1BDC: 16 00      LD           D,$00
1BDE: 21 C5 1B   LD           HL,$1BC5
1BE1: 19         ADD         HL,DE
1BE2: 6E         LD           L,(HL)
1BE3: 26 6D      LD           H,$6D
1BE5: 11 C0 96   LD           DE,$96C0
1BE8: 01 40 00   LD           BC,$0040
1BEB: CD C5 28   CALL       $28C5
1BEE: C3 CC 1C   JP           $1CCC
1BF1: 26 6E      LD           H,$6E
1BF3: 18 C3      JR           $1BB8
1BF5: F0 A6      LD           A,($A6)
1BF7: E6 07      AND         $07
1BF9: C2 5A 1C   JP           NZ,$1C5A
1BFC: F0 A6      LD           A,($A6)
1BFE: 1F         RRA
1BFF: 1F         RRA
1C00: 1F         RRA
1C01: E6 07      AND         $07
1C03: 5F         LD           E,A
1C04: 16 00      LD           D,$00
1C06: 21 C5 1B   LD           HL,$1BC5
1C09: 19         ADD         HL,DE
1C0A: 6E         LD           L,(HL)
1C0B: 26 6F      LD           H,$6F
1C0D: C3 E5 1B   JP           $1BE5
1C10: F0 A6      LD           A,($A6)
1C12: 3C         INC         A
1C13: E6 03      AND         $03
1C15: C2 CD 1B   JP           NZ,$1BCD
1C18: 21 C0 DC   LD           HL,$DCC0
1C1B: 11 C0 90   LD           DE,$90C0
1C1E: C3 E8 1B   JP           $1BE8
1C21: 26 70      LD           H,$70
1C23: F0 A6      LD           A,($A6)
1C25: E6 07      AND         $07
1C27: C2 5A 1C   JP           NZ,$1C5A
1C2A: CD 43 1C   CALL       $1C43
1C2D: C3 A7 1B   JP           $1BA7
1C30: 26 71      LD           H,$71
1C32: F0 A6      LD           A,($A6)
1C34: E6 03      AND         $03
1C36: C2 5A 1C   JP           NZ,$1C5A
1C39: CD 43 1C   CALL       $1C43
1C3C: C3 A7 1B   JP           $1BA7
1C3F: 26 72      LD           H,$72
1C41: 18 EF      JR           $1C32
1C43: F0 A7      LD           A,($A7)
1C45: C6 40      ADD         $40
1C47: E0 A7      LDFF00   ($A7),A
1C49: C9         RET
1C4A: 26 75      LD           H,$75
1C4C: 18 E4      JR           $1C32
1C4E: 26 74      LD           H,$74
1C50: 18 D1      JR           $1C23
1C52: 26 77      LD           H,$77
1C54: 18 CD      JR           $1C23
1C56: 26 76      LD           H,$76
1C58: 18 C9      JR           $1C23
1C5A: F0 9D      LD           A,($9D)
1C5C: FE FF      CP           $FF
1C5E: CA CC 1C   JP           Z,$1CCC
1C61: 21 13 18   LD           HL,$1813
1C64: CB 27      SLA         A
1C66: 4F         LD           C,A
1C67: 06 00      LD           B,$00
1C69: 09         ADD         HL,BC
1C6A: 5E         LD           E,(HL)
1C6B: E5         PUSH       HL
1C6C: 21 01 19   LD           HL,$1901
1C6F: 09         ADD         HL,BC
1C70: FA 1D C1   LD           A,($C11D)
1C73: E6 9F      AND         $9F
1C75: B6         OR           (HL)
1C76: EA 1D C1   LD           ($C11D),A
1C79: 23         INC         HL
1C7A: FA 1E C1   LD           A,($C11E)
1C7D: E6 9F      AND         $9F
1C7F: B6         OR           (HL)
1C80: EA 1E C1   LD           ($C11E),A
1C83: 16 00      LD           D,$00
1C85: CB 23      SLA         E
1C87: CB 12      RL           D
1C89: CB 23      SLA         E
1C8B: CB 12      RL           D
1C8D: CB 23      SLA         E
1C8F: CB 12      RL           D
1C91: CB 23      SLA         E
1C93: CB 12      RL           D
1C95: 21 00 58   LD           HL,$5800
1C98: 19         ADD         HL,DE
1C99: E5         PUSH       HL
1C9A: C1         POP         BC
1C9B: 21 00 80   LD           HL,$8000
1C9E: 16 20      LD           D,$20
1CA0: 0A         LD           A,(BC)
1CA1: 03         INC         BC
1CA2: 22         LD           (HLI),A
1CA3: 15         DEC         D
1CA4: 20 FA      JR           NZ,$1CA0
1CA6: E1         POP         HL
1CA7: 23         INC         HL
1CA8: 5E         LD           E,(HL)
1CA9: 16 00      LD           D,$00
1CAB: CB 23      SLA         E
1CAD: CB 12      RL           D
1CAF: CB 23      SLA         E
1CB1: CB 12      RL           D
1CB3: CB 23      SLA         E
1CB5: CB 12      RL           D
1CB7: CB 23      SLA         E
1CB9: CB 12      RL           D
1CBB: 21 00 58   LD           HL,$5800
1CBE: 19         ADD         HL,DE
1CBF: E5         PUSH       HL
1CC0: C1         POP         BC
1CC1: 21 20 80   LD           HL,$8020
1CC4: 16 20      LD           D,$20
1CC6: 0A         LD           A,(BC)
1CC7: 03         INC         BC
1CC8: 22         LD           (HLI),A
1CC9: 15         DEC         D
1CCA: 20 FA      JR           NZ,$1CC6
1CCC: F0 9D      LD           A,($9D)
1CCE: 3C         INC         A
1CCF: 28 43      JR           Z,$1D14
1CD1: FA C7 DB   LD           A,($DBC7)
1CD4: 17         RLA
1CD5: 17         RLA
1CD6: E6 10      AND         $10
1CD8: EA 35 C1   LD           ($C135),A
1CDB: 21 08 C0   LD           HL,$C008
1CDE: FA 3B C1   LD           A,($C13B)
1CE1: 4F         LD           C,A
1CE2: FA 45 C1   LD           A,($C145)
1CE5: 81         ADD         A,C
1CE6: FE 88      CP           $88
1CE8: 30 2A      JR           NC,$1D14
1CEA: F5         PUSH       AF
1CEB: 22         LD           (HLI),A
1CEC: FA 3C C1   LD           A,($C13C)
1CEF: 4F         LD           C,A
1CF0: F0 98      LD           A,($98)
1CF2: 81         ADD         A,C
1CF3: 22         LD           (HLI),A
1CF4: 3E 00      LD           A,$00
1CF6: 22         LD           (HLI),A
1CF7: FA 35 C1   LD           A,($C135)
1CFA: 57         LD           D,A
1CFB: FA 1D C1   LD           A,($C11D)
1CFE: B2         OR           D
1CFF: 22         LD           (HLI),A
1D00: F1         POP         AF
1D01: 22         LD           (HLI),A
1D02: F0 98      LD           A,($98)
1D04: 81         ADD         A,C
1D05: C6 08      ADD         $08
1D07: 22         LD           (HLI),A
1D08: 3E 02      LD           A,$02
1D0A: 22         LD           (HLI),A
1D0B: FA 35 C1   LD           A,($C135)
1D0E: 57         LD           D,A
1D0F: FA 1E C1   LD           A,($C11E)
1D12: B2         OR           D
1D13: 22         LD           (HLI),A
1D14: C9         RET
1D15: 21 00 4F   LD           HL,$4F00
1D18: 3E 0E      LD           A,$0E
1D1A: 18 05      JR           $1D21
1D1C: 3E 12      LD           A,$12
1D1E: 21 80 60   LD           HL,$6080
1D21: EA 00 21   LD           ($2100),A
1D24: 11 00 84   LD           DE,$8400
1D27: 01 40 00   LD           BC,$0040
1D2A: C3 4D 1E   JP           $1E4D
1D2D: FA 0E DB   LD           A,($DB0E)
1D30: FE 02      CP           $02
1D32: DA 50 1E   JP           C,$1E50
1D35: D6 02      SUB         $02
1D37: 57         LD           D,A
1D38: 1E 00      LD           E,$00
1D3A: CB 2A      SRA         D
1D3C: CB 1B      RR           E
1D3E: CB 2A      SRA         D
1D40: CB 1B      RR           E
1D42: 21 00 44   LD           HL,$4400
1D45: 19         ADD         HL,DE
1D46: 11 A0 89   LD           DE,$89A0
1D49: 01 40 00   LD           BC,$0040
1D4C: 3E 0C      LD           A,$0C
1D4E: EA 00 21   LD           ($2100),A
1D51: C3 4D 1E   JP           $1E4D
1D54: 21 C0 68   LD           HL,$68C0
1D57: 11 E0 88   LD           DE,$88E0
1D5A: 18 68      JR           $1DC4
1D5C: 3E 11      LD           A,$11
1D5E: EA 00 21   LD           ($2100),A
1D61: FA 00 D0   LD           A,($D000)
1D64: CB 37      SWAP       A
1D66: E6 F0      AND         $F0
1D68: 5F         LD           E,A
1D69: 16 00      LD           D,$00
1D6B: CB 23      SLA         E
1D6D: CB 12      RL           D
1D6F: CB 23      SLA         E
1D71: CB 12      RL           D
1D73: 21 00 8D   LD           HL,$8D00
1D76: 19         ADD         HL,DE
1D77: E5         PUSH       HL
1D78: 21 00 50   LD           HL,$5000
1D7B: 19         ADD         HL,DE
1D7C: D1         POP         DE
1D7D: 01 40 00   LD           BC,$0040
1D80: CD C5 28   CALL       $28C5
1D83: AF         XOR         A
1D84: E0 A5      LDFF00   ($A5),A
1D86: 3E 0C      LD           A,$0C
1D88: EA 00 21   LD           ($2100),A
1D8B: C9         RET
1D8C: 3E 13      LD           A,$13
1D8E: EA 00 21   LD           ($2100),A
1D91: FA 00 D0   LD           A,($D000)
1D94: CB 37      SWAP       A
1D96: E6 F0      AND         $F0
1D98: 5F         LD           E,A
1D99: 16 00      LD           D,$00
1D9B: CB 23      SLA         E
1D9D: CB 12      RL           D
1D9F: CB 23      SLA         E
1DA1: CB 12      RL           D
1DA3: 21 00 8D   LD           HL,$8D00
1DA6: 19         ADD         HL,DE
1DA7: E5         PUSH       HL
1DA8: 21 00 4D   LD           HL,$4D00
1DAB: 18 CE      JR           $1D7B
1DAD: 21 E0 48   LD           HL,$48E0
1DB0: 11 E0 88   LD           DE,$88E0
1DB3: 3E 0C      LD           A,$0C
1DB5: EA 00 21   LD           ($2100),A
1DB8: 01 20 00   LD           BC,$0020
1DBB: C3 4D 1E   JP           $1E4D
1DBE: 21 E0 68   LD           HL,$68E0
1DC1: 11 A0 8C   LD           DE,$8CA0
1DC4: 3E 0C      LD           A,$0C
1DC6: EA 00 21   LD           ($2100),A
1DC9: 01 20 00   LD           BC,$0020
1DCC: C3 4D 1E   JP           $1E4D
1DCF: 21 00 7F   LD           HL,$7F00
1DD2: 3E 12      LD           A,$12
1DD4: 18 05      JR           $1DDB
1DD6: 21 40 4C   LD           HL,$4C40
1DD9: 3E 0D      LD           A,$0D
1DDB: EA 00 21   LD           ($2100),A
1DDE: 11 40 91   LD           DE,$9140
1DE1: C3 4A 1E   JP           $1E4A
1DE4: 40         LD           B,B
1DE5: 68         LD           L,B
1DE6: 40         LD           B,B
1DE7: 68         LD           L,B
1DE8: 00         NOP
1DE9: 68         LD           L,B
1DEA: 80         ADD         A,B
1DEB: 68         LD           L,B
1DEC: 00         NOP
1DED: 68         LD           L,B
1DEE: 21 00 21   LD           HL,$2100
1DF1: 36 0C      LD           (HL),$0C
1DF3: 21 A1 FF   LD           HL,$FFA1
1DF6: 36 01      LD           (HL),$01
1DF8: 21 FB D6   LD           HL,$D6FB
1DFB: 5E         LD           E,(HL)
1DFC: 16 00      LD           D,$00
1DFE: 3C         INC         A
1DFF: FE 03      CP           $03
1E01: 20 0A      JR           NZ,$1E0D
1E03: F5         PUSH       AF
1E04: FA FB D6   LD           A,($D6FB)
1E07: EE 02      XOR         $02
1E09: EA FB D6   LD           ($D6FB),A
1E0C: F1         POP         AF
1E0D: EA F8 D6   LD           ($D6F8),A
1E10: FE 04      CP           $04
1E12: 20 05      JR           NZ,$1E19
1E14: 21 E4 1D   LD           HL,$1DE4
1E17: 18 07      JR           $1E20
1E19: FE 08      CP           $08
1E1B: 20 09      JR           NZ,$1E26
1E1D: 21 E8 1D   LD           HL,$1DE8
1E20: 19         ADD         HL,DE
1E21: 11 40 90   LD           DE,$9040
1E24: 18 18      JR           $1E3E
1E26: FE 06      CP           $06
1E28: 20 05      JR           NZ,$1E2F
1E2A: 21 E4 1D   LD           HL,$1DE4
1E2D: 18 0B      JR           $1E3A
1E2F: FE 0A      CP           $0A
1E31: 20 14      JR           NZ,$1E47
1E33: AF         XOR         A
1E34: EA F8 D6   LD           ($D6F8),A
1E37: 21 EA 1D   LD           HL,$1DEA
1E3A: 19         ADD         HL,DE
1E3B: 11 80 90   LD           DE,$9080
1E3E: 01 40 00   LD           BC,$0040
1E41: 2A         LD           A,(HLI)
1E42: 66         LD           H,(HL)
1E43: 6F         LD           L,A
1E44: C3 C5 28   JP           $28C5
1E47: C3 CC 1C   JP           $1CCC
1E4A: 01 40 00   LD           BC,$0040
1E4D: CD C5 28   CALL       $28C5
1E50: AF         XOR         A
1E51: E0 A5      LDFF00   ($A5),A
1E53: 3E 0C      LD           A,$0C
1E55: EA 00 21   LD           ($2100),A
1E58: C3 CC 1C   JP           $1CCC
1E5B: 0C         INC         C
1E5C: 03         INC         BC
1E5D: 08 08 0A   LD           ($0A08),SP
1E60: 0A         LD           A,(BC)
1E61: 05         DEC         B
1E62: 10 36      STOP       $36
1E64: 38 3A      JR           C,$1EA0
1E66: 3C         INC         A
1E67: 02         LD           (BC),A
1E68: 01 08 04   LD           BC,$0408
1E6B: FC                              
1E6C: 04         INC         B
1E6D: 00         NOP
1E6E: 00         NOP
1E6F: 00         NOP
1E70: 00         NOP
1E71: 04         INC         B
1E72: 00         NOP
1E73: CD 7B 1E   CALL       $1E7B
1E76: 3E 02      LD           A,$02
1E78: C3 B9 07   JP           $07B9
1E7B: 21 4A C1   LD           HL,$C14A
1E7E: FA 5C C1   LD           A,($C15C)
1E81: B6         OR           (HL)
1E82: 21 A2 FF   LD           HL,$FFA2
1E85: B6         OR           (HL)
1E86: 21 1C C1   LD           HL,$C11C
1E89: B6         OR           (HL)
1E8A: C2 A5 20   JP           NZ,$20A5
1E8D: F0 9E      LD           A,($9E)
1E8F: 5F         LD           E,A
1E90: 16 00      LD           D,$00
1E92: 21 5B 1E   LD           HL,$1E5B
1E95: 19         ADD         HL,DE
1E96: F0 98      LD           A,($98)
1E98: 86         ADD         A,(HL)
1E99: D6 08      SUB         $08
1E9B: E6 F0      AND         $F0
1E9D: E0 CE      LDFF00   ($CE),A
1E9F: CB 37      SWAP       A
1EA1: 4F         LD           C,A
1EA2: 21 5F 1E   LD           HL,$1E5F
1EA5: 19         ADD         HL,DE
1EA6: F0 99      LD           A,($99)
1EA8: 86         ADD         A,(HL)
1EA9: D6 10      SUB         $10
1EAB: E6 F0      AND         $F0
1EAD: E0 CD      LDFF00   ($CD),A
1EAF: B1         OR           C
1EB0: 5F         LD           E,A
1EB1: E0 D8      LDFF00   ($D8),A
1EB3: 21 11 D7   LD           HL,$D711
1EB6: 19         ADD         HL,DE
1EB7: 7C         LD           A,H
1EB8: FE D7      CP           $D7
1EBA: C2 7C 20   JP           NZ,$207C
1EBD: 7E         LD           A,(HL)
1EBE: E0 D7      LDFF00   ($D7),A
1EC0: 5F         LD           E,A
1EC1: FA A5 DB   LD           A,($DBA5)
1EC4: 57         LD           D,A
1EC5: CD DB 29   CALL       $29DB
1EC8: E0 DC      LDFF00   ($DC),A
1ECA: F0 D7      LD           A,($D7)
1ECC: FE 9A      CP           $9A
1ECE: 28 40      JR           Z,$1F10
1ED0: F0 DC      LD           A,($DC)
1ED2: FE 00      CP           $00
1ED4: CA 7C 20   JP           Z,$207C
1ED7: FE 01      CP           $01
1ED9: 28 1D      JR           Z,$1EF8
1EDB: FE 50      CP           $50
1EDD: CA 7C 20   JP           Z,$207C
1EE0: FE 51      CP           $51
1EE2: CA 7C 20   JP           Z,$207C
1EE5: FE 11      CP           $11
1EE7: DA 7C 20   JP           C,$207C
1EEA: FE D4      CP           $D4
1EEC: D2 7C 20   JP           NC,$207C
1EEF: FE D0      CP           $D0
1EF1: 30 05      JR           NC,$1EF8
1EF3: FE 7C      CP           $7C
1EF5: D2 7C 20   JP           NC,$207C
1EF8: F0 D7      LD           A,($D7)
1EFA: 5F         LD           E,A
1EFB: FE 6F      CP           $6F
1EFD: 28 09      JR           Z,$1F08
1EFF: FE 5E      CP           $5E
1F01: 28 05      JR           Z,$1F08
1F03: FE D4      CP           $D4
1F05: C2 A1 1F   JP           NZ,$1FA1
1F08: FA A5 DB   LD           A,($DBA5)
1F0B: A7         AND         A
1F0C: 7B         LD           A,E
1F0D: C2 A1 1F   JP           NZ,$1FA1
1F10: 5F         LD           E,A
1F11: F0 9E      LD           A,($9E)
1F13: FE 02      CP           $02
1F15: C2 FD 1F   JP           NZ,$1FFD
1F18: 3E 02      LD           A,$02
1F1A: EA AD C1   LD           ($C1AD),A
1F1D: F0 CC      LD           A,($CC)
1F1F: E6 30      AND         $30
1F21: CA FD 1F   JP           Z,$1FFD
1F24: 7B         LD           A,E
1F25: FE 5E      CP           $5E
1F27: 3E 8E      LD           A,$8E
1F29: 28 6B      JR           Z,$1F96
1F2B: 7B         LD           A,E
1F2C: FE 6F      CP           $6F
1F2E: 28 2B      JR           Z,$1F5B
1F30: FE D4      CP           $D4
1F32: 28 27      JR           Z,$1F5B
1F34: FA 73 DB   LD           A,($DB73)
1F37: A7         AND         A
1F38: 28 08      JR           Z,$1F42
1F3A: 3E 78      LD           A,$78
1F3C: CD 8E 21   CALL       $218E
1F3F: C3 FD 1F   JP           $1FFD
1F42: FA 4E DB   LD           A,($DB4E)
1F45: A7         AND         A
1F46: F0 F6      LD           A,($F6)
1F48: 20 06      JR           NZ,$1F50
1F4A: 1E FF      LD           E,$FF
1F4C: FE A3      CP           $A3
1F4E: 28 08      JR           Z,$1F58
1F50: 1E FC      LD           E,$FC
1F52: FE FA      CP           $FA
1F54: 28 02      JR           Z,$1F58
1F56: 1E FD      LD           E,$FD
1F58: 7B         LD           A,E
1F59: 18 41      JR           $1F9C
1F5B: F0 F6      LD           A,($F6)
1F5D: 5F         LD           E,A
1F5E: 16 00      LD           D,$00
1F60: 3E 14      LD           A,$14
1F62: EA 00 21   LD           ($2100),A
1F65: 21 FF 55   LD           HL,$55FF
1F68: 19         ADD         HL,DE
1F69: FA 49 DB   LD           A,($DB49)
1F6C: 5F         LD           E,A
1F6D: 7E         LD           A,(HL)
1F6E: FE A9      CP           $A9
1F70: 20 06      JR           NZ,$1F78
1F72: CB 43      BIT         0,E
1F74: 28 02      JR           Z,$1F78
1F76: 3E AF      LD           A,$AF
1F78: FE AF      CP           $AF
1F7A: 20 16      JR           NZ,$1F92
1F7C: CB 43      BIT         0,E
1F7E: 20 12      JR           NZ,$1F92
1F80: F0 CE      LD           A,($CE)
1F82: CB 37      SWAP       A
1F84: E6 0F      AND         $0F
1F86: 5F         LD           E,A
1F87: F0 CD      LD           A,($CD)
1F89: E6 F0      AND         $F0
1F8B: B3         OR           E
1F8C: EA 73 D4   LD           ($D473),A
1F8F: C3 FD 1F   JP           $1FFD
1F92: FE 83      CP           $83
1F94: 28 06      JR           Z,$1F9C
1F96: CD 85 21   CALL       $2185
1F99: C3 FD 1F   JP           $1FFD
1F9C: CD 97 21   CALL       $2197
1F9F: 18 5C      JR           $1FFD
1FA1: FE A0      CP           $A0
1FA3: 20 58      JR           NZ,$1FFD
1FA5: FA 8E C1   LD           A,($C18E)
1FA8: E6 1F      AND         $1F
1FAA: FE 0D      CP           $0D
1FAC: 28 4F      JR           Z,$1FFD
1FAE: F0 9E      LD           A,($9E)
1FB0: FE 02      CP           $02
1FB2: 20 49      JR           NZ,$1FFD
1FB4: EA AD C1   LD           ($C1AD),A
1FB7: F0 CC      LD           A,($CC)
1FB9: E6 30      AND         $30
1FBB: 28 40      JR           Z,$1FFD
1FBD: F0 F9      LD           A,($F9)
1FBF: A7         AND         A
1FC0: 20 06      JR           NZ,$1FC8
1FC2: F0 9E      LD           A,($9E)
1FC4: FE 02      CP           $02
1FC6: 20 35      JR           NZ,$1FFD
1FC8: 3E 14      LD           A,$14
1FCA: EA 00 21   LD           ($2100),A
1FCD: F0 F6      LD           A,($F6)
1FCF: 5F         LD           E,A
1FD0: FA A5 DB   LD           A,($DBA5)
1FD3: 57         LD           D,A
1FD4: F0 F7      LD           A,($F7)
1FD6: FE 1A      CP           $1A
1FD8: 30 05      JR           NC,$1FDF
1FDA: FE 06      CP           $06
1FDC: 38 01      JR           C,$1FDF
1FDE: 14         INC         D
1FDF: 21 00 45   LD           HL,$4500
1FE2: 19         ADD         HL,DE
1FE3: 7E         LD           A,(HL)
1FE4: FE 20      CP           $20
1FE6: 20 0B      JR           NZ,$1FF3
1FE8: FA 4E DB   LD           A,($DB4E)
1FEB: FE 02      CP           $02
1FED: 3E 20      LD           A,$20
1FEF: 38 02      JR           C,$1FF3
1FF1: 3E 1C      LD           A,$1C
1FF3: E0 DF      LDFF00   ($DF),A
1FF5: 3E 02      LD           A,$02
1FF7: EA 00 21   LD           ($2100),A
1FFA: CD BA 41   CALL       $41BA
1FFD: FA 00 DB   LD           A,($DB00)
2000: FE 03      CP           $03
2002: 20 07      JR           NZ,$200B
2004: F0 CB      LD           A,($CB)
2006: E6 20      AND         $20
2008: 20 10      JR           NZ,$201A
200A: C9         RET
200B: FA 01 DB   LD           A,($DB01)
200E: FE 03      CP           $03
2010: C2 A5 20   JP           NZ,$20A5
2013: F0 CB      LD           A,($CB)
2015: E6 10      AND         $10
2017: CA A5 20   JP           Z,$20A5
201A: 3E 02      LD           A,$02
201C: EA 00 21   LD           ($2100),A
201F: CD 5E 48   CALL       $485E
2022: 3E 01      LD           A,$01
2024: E0 A1      LDFF00   ($A1),A
2026: F0 9E      LD           A,($9E)
2028: 5F         LD           E,A
2029: 16 00      LD           D,$00
202B: 21 63 1E   LD           HL,$1E63
202E: 19         ADD         HL,DE
202F: 7E         LD           A,(HL)
2030: E0 9D      LDFF00   ($9D),A
2032: 21 67 1E   LD           HL,$1E67
2035: 19         ADD         HL,DE
2036: F0 CB      LD           A,($CB)
2038: A6         AND         (HL)
2039: 28 41      JR           Z,$207C
203B: 21 6B 1E   LD           HL,$1E6B
203E: 19         ADD         HL,DE
203F: 7E         LD           A,(HL)
2040: EA 3C C1   LD           ($C13C),A
2043: 21 6F 1E   LD           HL,$1E6F
2046: 19         ADD         HL,DE
2047: 7E         LD           A,(HL)
2048: EA 3B C1   LD           ($C13B),A
204B: 21 9D FF   LD           HL,$FF9D
204E: 34         INC         (HL)
204F: 1E 08      LD           E,$08
2051: FA 7C D4   LD           A,($D47C)
2054: FE 01      CP           $01
2056: 20 02      JR           NZ,$205A
2058: 1E 03      LD           E,$03
205A: 21 5F C1   LD           HL,$C15F
205D: 34         INC         (HL)
205E: 7E         LD           A,(HL)
205F: BB         CP           E
2060: 38 19      JR           C,$207B
2062: AF         XOR         A
2063: E0 E5      LDFF00   ($E5),A
2065: F0 D7      LD           A,($D7)
2067: FE 8E      CP           $8E
2069: 28 16      JR           Z,$2081
206B: FE 20      CP           $20
206D: 28 12      JR           Z,$2081
206F: FA A5 DB   LD           A,($DBA5)
2072: A7         AND         A
2073: 20 06      JR           NZ,$207B
2075: F0 D7      LD           A,($D7)
2077: FE 5C      CP           $5C
2079: 28 14      JR           Z,$208F
207B: C9         RET
207C: AF         XOR         A
207D: EA 5F C1   LD           ($C15F),A
2080: C9         RET
2081: CD 93 20   CALL       $2093
2084: 3E 14      LD           A,$14
2086: EA 00 21   LD           ($2100),A
2089: CD AA 55   CALL       $55AA
208C: C3 C0 07   JP           $07C0
208F: 3E 01      LD           A,$01
2091: E0 E5      LDFF00   ($E5),A
2093: F0 D8      LD           A,($D8)
2095: 5F         LD           E,A
2096: F0 D7      LD           A,($D7)
2098: E0 AF      LDFF00   ($AF),A
209A: CD A6 20   CALL       $20A6
209D: F0 9E      LD           A,($9E)
209F: EA 5D C1   LD           ($C15D),A
20A2: CD B1 20   CALL       $20B1
20A5: C9         RET
20A6: 3E 14      LD           A,$14
20A8: EA 00 21   LD           ($2100),A
20AB: CD DE 59   CALL       $59DE
20AE: C3 C0 07   JP           $07C0
20B1: 3E 05      LD           A,$05
20B3: CD EB 10   CALL       $10EB
20B6: 38 1D      JR           C,$20D5
20B8: 3E 02      LD           A,$02
20BA: E0 F3      LDFF00   ($F3),A
20BC: 21 80 C2   LD           HL,$C280
20BF: 19         ADD         HL,DE
20C0: 36 07      LD           (HL),$07
20C2: 21 B0 C3   LD           HL,$C3B0
20C5: 19         ADD         HL,DE
20C6: F0 E5      LD           A,($E5)
20C8: 77         LD           (HL),A
20C9: D5         PUSH       DE
20CA: C1         POP         BC
20CB: 1E 01      LD           E,$01
20CD: 3E 03      LD           A,$03
20CF: CD B9 07   CALL       $07B9
20D2: CD EF 57   CALL       $57EF
20D5: C9         RET
20D6: FA 4F C1   LD           A,($C14F)
20D9: A7         AND         A
20DA: C0         RET         NZ
20DB: 0E 01      LD           C,$01
20DD: CD E4 20   CALL       $20E4
20E0: 0E 00      LD           C,$00
20E2: E0 D7      LDFF00   ($D7),A
20E4: 06 00      LD           B,$00
20E6: 21 9A FF   LD           HL,$FF9A
20E9: 09         ADD         HL,BC
20EA: 7E         LD           A,(HL)
20EB: F5         PUSH       AF
20EC: CB 37      SWAP       A
20EE: E6 F0      AND         $F0
20F0: 21 1A C1   LD           HL,$C11A
20F3: 09         ADD         HL,BC
20F4: 86         ADD         A,(HL)
20F5: 77         LD           (HL),A
20F6: CB 12      RL           D
20F8: 21 98 FF   LD           HL,$FF98
20FB: 09         ADD         HL,BC
20FC: F1         POP         AF
20FD: 1E 00      LD           E,$00
20FF: CB 7F      BIT         7,A
2101: 28 02      JR           Z,$2105
2103: 1E F0      LD           E,$F0
2105: CB 37      SWAP       A
2107: E6 0F      AND         $0F
2109: B3         OR           E
210A: CB 1A      RR           D
210C: 8E         ADC         A,(HL)
210D: 77         LD           (HL),A
210E: C9         RET
210F: F0 A3      LD           A,($A3)
2111: F5         PUSH       AF
2112: CB 37      SWAP       A
2114: E6 F0      AND         $F0
2116: 21 49 C1   LD           HL,$C149
2119: 86         ADD         A,(HL)
211A: 77         LD           (HL),A
211B: CB 12      RL           D
211D: 21 A2 FF   LD           HL,$FFA2
2120: F1         POP         AF
2121: 1E 00      LD           E,$00
2123: CB 7F      BIT         7,A
2125: 28 02      JR           Z,$2129
2127: 1E F0      LD           E,$F0
2129: CB 37      SWAP       A
212B: E6 0F      AND         $0F
212D: B3         OR           E
212E: CB 1A      RR           D
2130: 8E         ADC         A,(HL)
2131: 77         LD           (HL),A
2132: C9         RET
2133: FA 9F C1   LD           A,($C19F)
2136: A7         AND         A
2137: C8         RET         Z
2138: 5F         LD           E,A
2139: FA 95 DB   LD           A,($DB95)
213C: FE 01      CP           $01
213E: 3E 7E      LD           A,$7E
2140: 20 02      JR           NZ,$2144
2142: 3E 7F      LD           A,$7F
2144: E0 E8      LDFF00   ($E8),A
2146: FA 64 C1   LD           A,($C164)
2149: A7         AND         A
214A: FA 70 C1   LD           A,($C170)
214D: 20 04      JR           NZ,$2153
214F: FE 20      CP           $20
2151: 38 04      JR           C,$2157
2153: E6 0F      AND         $0F
2155: F6 10      OR           $10
2157: EA 71 C1   LD           ($C171),A
215A: 7B         LD           A,E
215B: E6 7F      AND         $7F
215D: 3D         DEC         A
215E: C7         RST         0X00
215F: 7D         LD           A,L
2160: 21 C2 21   LD           HL,$21C2
2163: C2 21 C2   JP           NZ,$C221
2166: 21 53 22   LD           HL,$2253
2169: 20 23      JR           NZ,$218E
216B: 59         LD           E,C
216C: 23         INC         HL
216D: B5         OR           L
216E: 23         INC         HL
216F: 21 25 A0   LD           HL,$A025
2172: 25         DEC         H
2173: F4                              
2174: 25         DEC         H
2175: 95         SUB         L
2176: 22         LD           (HLI),A
2177: 1F         RRA
2178: 26 CE      LD           H,$CE
217A: 22         LD           (HLI),A
217B: C3 21 3E   JP           $3E21
217E: 14         INC         D
217F: EA 00 21   LD           ($2100),A
2182: C3 24 59   JP           $5924
2185: CD 97 21   CALL       $2197
2188: 3E 01      LD           A,$01
218A: EA 12 C1   LD           ($C112),A
218D: C9         RET
218E: CD 97 21   CALL       $2197
2191: 3E 02      LD           A,$02
2193: EA 12 C1   LD           ($C112),A
2196: C9         RET
2197: F5         PUSH       AF
2198: AF         XOR         A
2199: EA 77 C1   LD           ($C177),A
219C: F1         POP         AF
219D: EA 73 C1   LD           ($C173),A
21A0: AF         XOR         A
21A1: EA 6F C1   LD           ($C16F),A
21A4: EA 70 C1   LD           ($C170),A
21A7: EA 64 C1   LD           ($C164),A
21AA: EA 08 C1   LD           ($C108),A
21AD: EA 12 C1   LD           ($C112),A
21B0: 3E 0F      LD           A,$0F
21B2: EA AB C5   LD           ($C5AB),A
21B5: F0 99      LD           A,($99)
21B7: FE 48      CP           $48
21B9: 1F         RRA
21BA: E6 80      AND         $80
21BC: F6 01      OR           $01
21BE: EA 9F C1   LD           ($C19F),A
21C1: C9         RET
21C2: C9         RET
21C3: AF         XOR         A
21C4: EA 9F C1   LD           ($C19F),A
21C7: 3E 18      LD           A,$18
21C9: EA 34 C1   LD           ($C134),A
21CC: C9         RET
21CD: 00         NOP
21CE: 24         INC         H
21CF: 48         LD           C,B
21D0: 00         NOP
21D1: 24         INC         H
21D2: 48         LD           C,B
21D3: 98         SBC         B
21D4: 98         SBC         B
21D5: 98         SBC         B
21D6: 99         SBC         C
21D7: 99         SBC         C
21D8: 99         SBC         C
21D9: 21 61 A1   LD           HL,$A161
21DC: 41         LD           B,C
21DD: 81         ADD         A,C
21DE: C1         POP         BC
21DF: FA 9F C1   LD           A,($C19F)
21E2: CB 7F      BIT         7,A
21E4: 28 04      JR           Z,$21EA
21E6: E6 7F      AND         $7F
21E8: C6 03      ADD         $03
21EA: 5F         LD           E,A
21EB: 16 00      LD           D,$00
21ED: 21 CB 21   LD           HL,$21CB
21F0: 19         ADD         HL,DE
21F1: 7E         LD           A,(HL)
21F2: 4F         LD           C,A
21F3: 06 00      LD           B,$00
21F5: 21 00 D5   LD           HL,$D500
21F8: 09         ADD         HL,BC
21F9: E5         PUSH       HL
21FA: C1         POP         BC
21FB: 21 D7 21   LD           HL,$21D7
21FE: 19         ADD         HL,DE
21FF: FA 2F C1   LD           A,($C12F)
2202: 86         ADD         A,(HL)
2203: 6F         LD           L,A
2204: E0 D7      LDFF00   ($D7),A
2206: 21 D1 21   LD           HL,$21D1
2209: 19         ADD         HL,DE
220A: FA 2E C1   LD           A,($C12E)
220D: 86         ADD         A,(HL)
220E: 67         LD           H,A
220F: F0 D7      LD           A,($D7)
2211: 6F         LD           L,A
2212: AF         XOR         A
2213: 5F         LD           E,A
2214: 57         LD           D,A
2215: 7E         LD           A,(HL)
2216: 02         LD           (BC),A
2217: 03         INC         BC
2218: 7D         LD           A,L
2219: C6 01      ADD         $01
221B: E6 1F      AND         $1F
221D: 20 06      JR           NZ,$2225
221F: 7D         LD           A,L
2220: E6 E0      AND         $E0
2222: 6F         LD           L,A
2223: 18 01      JR           $2226
2225: 2C         INC         L
2226: 1C         INC         E
2227: 7B         LD           A,E
2228: FE 12      CP           $12
222A: 20 E9      JR           NZ,$2215
222C: 1E 00      LD           E,$00
222E: F0 D7      LD           A,($D7)
2230: C6 20      ADD         $20
2232: E0 D7      LDFF00   ($D7),A
2234: 30 01      JR           NC,$2237
2236: 24         INC         H
2237: 6F         LD           L,A
2238: 14         INC         D
2239: 7A         LD           A,D
223A: FE 02      CP           $02
223C: 20 D7      JR           NZ,$2215
223E: C9         RET
223F: 61         LD           H,C
2240: 41         LD           B,C
2241: 81         ADD         A,C
2242: 21 A1 81   LD           HL,$81A1
2245: 61         LD           H,C
2246: A1         AND         C
2247: 41         LD           B,C
2248: C1         POP         BC
2249: 98         SBC         B
224A: 98         SBC         B
224B: 98         SBC         B
224C: 98         SBC         B
224D: 98         SBC         B
224E: 99         SBC         C
224F: 99         SBC         C
2250: 99         SBC         C
2251: 99         SBC         C
2252: 99         SBC         C
2253: FA 9F C1   LD           A,($C19F)
2256: 4F         LD           C,A
2257: FA 6F C1   LD           A,($C16F)
225A: FE 05      CP           $05
225C: 28 32      JR           Z,$2290
225E: CB 79      BIT         7,C
2260: 28 02      JR           Z,$2264
2262: C6 05      ADD         $05
2264: 4F         LD           C,A
2265: 06 00      LD           B,$00
2267: 1E 01      LD           E,$01
2269: 16 00      LD           D,$00
226B: FA 2E C1   LD           A,($C12E)
226E: 21 49 22   LD           HL,$2249
2271: 09         ADD         HL,BC
2272: 86         ADD         A,(HL)
2273: 21 00 D6   LD           HL,$D600
2276: 19         ADD         HL,DE
2277: 22         LD           (HLI),A
2278: E5         PUSH       HL
2279: FA 2F C1   LD           A,($C12F)
227C: 21 3F 22   LD           HL,$223F
227F: 09         ADD         HL,BC
2280: 86         ADD         A,(HL)
2281: E1         POP         HL
2282: 22         LD           (HLI),A
2283: 3E 51      LD           A,$51
2285: 22         LD           (HLI),A
2286: F0 E8      LD           A,($E8)
2288: 22         LD           (HLI),A
2289: 36 00      LD           (HL),$00
228B: 21 6F C1   LD           HL,$C16F
228E: 34         INC         (HL)
228F: C9         RET
2290: 21 9F C1   LD           HL,$C19F
2293: 34         INC         (HL)
2294: C9         RET
2295: FA AB C1   LD           A,($C1AB)
2298: A7         AND         A
2299: 20 14      JR           NZ,$22AF
229B: F0 CC      LD           A,($CC)
229D: E6 30      AND         $30
229F: 28 0E      JR           Z,$22AF
22A1: AF         XOR         A
22A2: EA 6F C1   LD           ($C16F),A
22A5: FA 9F C1   LD           A,($C19F)
22A8: E6 F0      AND         $F0
22AA: F6 0E      OR           $0E
22AC: EA 9F C1   LD           ($C19F),A
22AF: C9         RET
22B0: A1         AND         C
22B1: 21 81 41   LD           HL,$4181
22B4: 61         LD           H,C
22B5: C1         POP         BC
22B6: 41         LD           B,C
22B7: A1         AND         C
22B8: 61         LD           H,C
22B9: 81         ADD         A,C
22BA: 98         SBC         B
22BB: 98         SBC         B
22BC: 98         SBC         B
22BD: 98         SBC         B
22BE: 98         SBC         B
22BF: 99         SBC         C
22C0: 99         SBC         C
22C1: 99         SBC         C
22C2: 99         SBC         C
22C3: 99         SBC         C
22C4: 48         LD           C,B
22C5: 00         NOP
22C6: 36 12      LD           (HL),$12
22C8: 24         INC         H
22C9: 48         LD           C,B
22CA: 00         NOP
22CB: 36 12      LD           (HL),$12
22CD: 24         INC         H
22CE: FA 9F C1   LD           A,($C19F)
22D1: 4F         LD           C,A
22D2: FA 6F C1   LD           A,($C16F)
22D5: FE 05      CP           $05
22D7: 28 B7      JR           Z,$2290
22D9: CB 79      BIT         7,C
22DB: 28 02      JR           Z,$22DF
22DD: C6 05      ADD         $05
22DF: 4F         LD           C,A
22E0: 06 00      LD           B,$00
22E2: 1E 01      LD           E,$01
22E4: 16 00      LD           D,$00
22E6: FA 2E C1   LD           A,($C12E)
22E9: 21 BA 22   LD           HL,$22BA
22EC: 09         ADD         HL,BC
22ED: 86         ADD         A,(HL)
22EE: 21 00 D6   LD           HL,$D600
22F1: 19         ADD         HL,DE
22F2: 22         LD           (HLI),A
22F3: E5         PUSH       HL
22F4: FA 2F C1   LD           A,($C12F)
22F7: 21 B0 22   LD           HL,$22B0
22FA: 09         ADD         HL,BC
22FB: 86         ADD         A,(HL)
22FC: E1         POP         HL
22FD: 22         LD           (HLI),A
22FE: 3E 11      LD           A,$11
2300: 22         LD           (HLI),A
2301: E5         PUSH       HL
2302: 21 C4 22   LD           HL,$22C4
2305: 09         ADD         HL,BC
2306: 7E         LD           A,(HL)
2307: 4F         LD           C,A
2308: 06 00      LD           B,$00
230A: 21 00 D5   LD           HL,$D500
230D: 09         ADD         HL,BC
230E: E5         PUSH       HL
230F: C1         POP         BC
2310: E1         POP         HL
2311: 1E 12      LD           E,$12
2313: 0A         LD           A,(BC)
2314: 03         INC         BC
2315: 22         LD           (HLI),A
2316: 1D         DEC         E
2317: 20 FA      JR           NZ,$2313
2319: 36 00      LD           (HL),$00
231B: 21 6F C1   LD           HL,$C16F
231E: 34         INC         (HL)
231F: C9         RET
2320: 3E 1C      LD           A,$1C
2322: EA 00 21   LD           ($2100),A
2325: FA 72 C1   LD           A,($C172)
2328: A7         AND         A
2329: 28 05      JR           Z,$2330
232B: 3D         DEC         A
232C: EA 72 C1   LD           ($C172),A
232F: C9         RET
2330: FA 70 C1   LD           A,($C170)
2333: E6 1F      AND         $1F
2335: 5F         LD           E,A
2336: 16 00      LD           D,$00
2338: 0E 01      LD           C,$01
233A: 06 00      LD           B,$00
233C: 21 21 45   LD           HL,$4521
233F: 19         ADD         HL,DE
2340: 7E         LD           A,(HL)
2341: 21 00 D6   LD           HL,$D600
2344: 09         ADD         HL,BC
2345: 22         LD           (HLI),A
2346: E5         PUSH       HL
2347: 21 01 45   LD           HL,$4501
234A: 19         ADD         HL,DE
234B: 7E         LD           A,(HL)
234C: E1         POP         HL
234D: 22         LD           (HLI),A
234E: 3E 4F      LD           A,$4F
2350: 22         LD           (HLI),A
2351: 3E FF      LD           A,$FF
2353: 22         LD           (HLI),A
2354: 36 00      LD           (HL),$00
2356: C3 90 22   JP           $2290
2359: 3E 1C      LD           A,$1C
235B: EA 00 21   LD           ($2100),A
235E: FA 9F C1   LD           A,($C19F)
2361: 4F         LD           C,A
2362: FA 71 C1   LD           A,($C171)
2365: CB 79      BIT         7,C
2367: 28 02      JR           Z,$236B
2369: C6 20      ADD         $20
236B: 4F         LD           C,A
236C: 06 00      LD           B,$00
236E: 1E 01      LD           E,$01
2370: 16 00      LD           D,$00
2372: FA 2E C1   LD           A,($C12E)
2375: 21 61 45   LD           HL,$4561
2378: 09         ADD         HL,BC
2379: 86         ADD         A,(HL)
237A: 21 00 D6   LD           HL,$D600
237D: 19         ADD         HL,DE
237E: 22         LD           (HLI),A
237F: EA 75 C1   LD           ($C175),A
2382: E5         PUSH       HL
2383: 21 A1 45   LD           HL,$45A1
2386: 09         ADD         HL,BC
2387: 7E         LD           A,(HL)
2388: E6 E0      AND         $E0
238A: C6 20      ADD         $20
238C: 5F         LD           E,A
238D: FA 2F C1   LD           A,($C12F)
2390: 86         ADD         A,(HL)
2391: 57         LD           D,A
2392: BB         CP           E
2393: 38 04      JR           C,$2399
2395: 7A         LD           A,D
2396: D6 20      SUB         $20
2398: 57         LD           D,A
2399: 7A         LD           A,D
239A: EA 76 C1   LD           ($C176),A
239D: E1         POP         HL
239E: 22         LD           (HLI),A
239F: AF         XOR         A
23A0: 22         LD           (HLI),A
23A1: E5         PUSH       HL
23A2: FA 70 C1   LD           A,($C170)
23A5: E6 1F      AND         $1F
23A7: 4F         LD           C,A
23A8: 21 41 45   LD           HL,$4541
23AB: 09         ADD         HL,BC
23AC: 7E         LD           A,(HL)
23AD: E1         POP         HL
23AE: 22         LD           (HLI),A
23AF: CD 90 22   CALL       $2290
23B2: C3 B5 23   JP           $23B5
23B5: 3E 1C      LD           A,$1C
23B7: EA 00 21   LD           ($2100),A
23BA: FA 70 C1   LD           A,($C170)
23BD: E6 1F      AND         $1F
23BF: 4F         LD           C,A
23C0: 06 00      LD           B,$00
23C2: 1E 05      LD           E,$05
23C4: 16 00      LD           D,$00
23C6: 21 21 45   LD           HL,$4521
23C9: 09         ADD         HL,BC
23CA: 7E         LD           A,(HL)
23CB: 21 00 D6   LD           HL,$D600
23CE: 19         ADD         HL,DE
23CF: 22         LD           (HLI),A
23D0: E5         PUSH       HL
23D1: 21 01 45   LD           HL,$4501
23D4: 09         ADD         HL,BC
23D5: 7E         LD           A,(HL)
23D6: E1         POP         HL
23D7: 22         LD           (HLI),A
23D8: 3E 0F      LD           A,$0F
23DA: 22         LD           (HLI),A
23DB: E5         PUSH       HL
23DC: FA 12 C1   LD           A,($C112)
23DF: 57         LD           D,A
23E0: FA 73 C1   LD           A,($C173)
23E3: 5F         LD           E,A
23E4: CB 23      SLA         E
23E6: CB 12      RL           D
23E8: 21 01 40   LD           HL,$4001
23EB: 19         ADD         HL,DE
23EC: 2A         LD           A,(HLI)
23ED: 5F         LD           E,A
23EE: 56         LD           D,(HL)
23EF: D5         PUSH       DE
23F0: FA 73 C1   LD           A,($C173)
23F3: 5F         LD           E,A
23F4: FA 12 C1   LD           A,($C112)
23F7: 57         LD           D,A
23F8: 21 E1 46   LD           HL,$46E1
23FB: 19         ADD         HL,DE
23FC: 7E         LD           A,(HL)
23FD: E6 1F      AND         $1F
23FF: EA 00 21   LD           ($2100),A
2402: E1         POP         HL
2403: FA 70 C1   LD           A,($C170)
2406: 5F         LD           E,A
2407: FA 64 C1   LD           A,($C164)
240A: 57         LD           D,A
240B: 19         ADD         HL,DE
240C: 2A         LD           A,(HLI)
240D: 5F         LD           E,A
240E: 7E         LD           A,(HL)
240F: EA C3 C3   LD           ($C3C3),A
2412: CD C0 07   CALL       $07C0
2415: 7B         LD           A,E
2416: E0 D7      LDFF00   ($D7),A
2418: FE FE      CP           $FE
241A: 20 14      JR           NZ,$2430
241C: E1         POP         HL
241D: AF         XOR         A
241E: EA 01 D6   LD           ($D601),A
2421: FA 9F C1   LD           A,($C19F)
2424: E6 F0      AND         $F0
2426: F6 0D      OR           $0D
2428: EA 9F C1   LD           ($C19F),A
242B: 3E 15      LD           A,$15
242D: E0 F2      LDFF00   ($F2),A
242F: C9         RET
2430: FE FF      CP           $FF
2432: 20 15      JR           NZ,$2449
2434: E1         POP         HL
2435: AF         XOR         A
2436: EA 01 D6   LD           ($D601),A
2439: FA 9F C1   LD           A,($C19F)
243C: E6 F0      AND         $F0
243E: F6 0C      OR           $0C
2440: EA 9F C1   LD           ($C19F),A
2443: C9         RET
2444: 55         LD           D,L
2445: 49         LD           C,C
2446: 4A         LD           C,D
2447: 46         LD           B,(HL)
2448: 47         LD           B,A
2449: FE 20      CP           $20
244B: 28 1F      JR           Z,$246C
244D: F5         PUSH       AF
244E: FA AB C5   LD           A,($C5AB)
2451: 57         LD           D,A
2452: 1E 01      LD           E,$01
2454: FE 0F      CP           $0F
2456: 28 08      JR           Z,$2460
2458: 1E 07      LD           E,$07
245A: FE 19      CP           $19
245C: 28 02      JR           Z,$2460
245E: 1E 03      LD           E,$03
2460: FA 70 C1   LD           A,($C170)
2463: C6 04      ADD         $04
2465: A3         AND         E
2466: 20 03      JR           NZ,$246B
2468: 7A         LD           A,D
2469: E0 F3      LDFF00   ($F3),A
246B: F1         POP         AF
246C: 16 00      LD           D,$00
246E: FE 23      CP           $23
2470: 20 22      JR           NZ,$2494
2472: FA 08 C1   LD           A,($C108)
2475: 5F         LD           E,A
2476: 3C         INC         A
2477: FE 05      CP           $05
2479: 20 01      JR           NZ,$247C
247B: AF         XOR         A
247C: EA 08 C1   LD           ($C108),A
247F: 21 4F DB   LD           HL,$DB4F
2482: FA 6E DB   LD           A,($DB6E)
2485: A7         AND         A
2486: 28 03      JR           Z,$248B
2488: 21 44 24   LD           HL,$2444
248B: 19         ADD         HL,DE
248C: 7E         LD           A,(HL)
248D: 3D         DEC         A
248E: FE FF      CP           $FF
2490: 20 02      JR           NZ,$2494
2492: 3E 20      LD           A,$20
2494: E0 D8      LDFF00   ($D8),A
2496: 5F         LD           E,A
2497: 3E 1C      LD           A,$1C
2499: EA 00 21   LD           ($2100),A
249C: 21 E1 45   LD           HL,$45E1
249F: 19         ADD         HL,DE
24A0: 5E         LD           E,(HL)
24A1: 16 00      LD           D,$00
24A3: CB 23      SLA         E
24A5: CB 12      RL           D
24A7: CB 23      SLA         E
24A9: CB 12      RL           D
24AB: CB 23      SLA         E
24AD: CB 12      RL           D
24AF: CB 23      SLA         E
24B1: CB 12      RL           D
24B3: CD C0 07   CALL       $07C0
24B6: 21 00 50   LD           HL,$5000
24B9: 19         ADD         HL,DE
24BA: E5         PUSH       HL
24BB: C1         POP         BC
24BC: E1         POP         HL
24BD: 1E 10      LD           E,$10
24BF: 0A         LD           A,(BC)
24C0: 22         LD           (HLI),A
24C1: 03         INC         BC
24C2: 1D         DEC         E
24C3: 20 FA      JR           NZ,$24BF
24C5: 36 00      LD           (HL),$00
24C7: E5         PUSH       HL
24C8: 3E 1C      LD           A,$1C
24CA: EA 00 21   LD           ($2100),A
24CD: F0 D8      LD           A,($D8)
24CF: 5F         LD           E,A
24D0: 16 00      LD           D,$00
24D2: AF         XOR         A
24D3: E1         POP         HL
24D4: A7         AND         A
24D5: 28 18      JR           Z,$24EF
24D7: 5F         LD           E,A
24D8: FA 75 C1   LD           A,($C175)
24DB: 22         LD           (HLI),A
24DC: FA 76 C1   LD           A,($C176)
24DF: D6 20      SUB         $20
24E1: 22         LD           (HLI),A
24E2: 3E 00      LD           A,$00
24E4: 22         LD           (HLI),A
24E5: 3E C9      LD           A,$C9
24E7: CB 1B      RR           E
24E9: 38 01      JR           C,$24EC
24EB: 3D         DEC         A
24EC: 22         LD           (HLI),A
24ED: 36 00      LD           (HL),$00
24EF: FA 70 C1   LD           A,($C170)
24F2: C6 01      ADD         $01
24F4: EA 70 C1   LD           ($C170),A
24F7: FA 64 C1   LD           A,($C164)
24FA: CE 00      ADC         $00
24FC: EA 64 C1   LD           ($C164),A
24FF: AF         XOR         A
2500: EA CC C1   LD           ($C1CC),A
2503: FA 71 C1   LD           A,($C171)
2506: FE 1F      CP           $1F
2508: 28 10      JR           Z,$251A
250A: FA 9F C1   LD           A,($C19F)
250D: E6 F0      AND         $F0
250F: F6 06      OR           $06
2511: EA 9F C1   LD           ($C19F),A
2514: 3E 00      LD           A,$00
2516: EA 72 C1   LD           ($C172),A
2519: C9         RET
251A: C3 90 22   JP           $2290
251D: 22         LD           (HLI),A
251E: 42         LD           B,D
251F: 98         SBC         B
2520: 99         SBC         C
2521: FA 70 C1   LD           A,($C170)
2524: E6 1F      AND         $1F
2526: 20 45      JR           NZ,$256D
2528: FA C3 C3   LD           A,($C3C3)
252B: FE FF      CP           $FF
252D: CA 39 24   JP           Z,$2439
2530: FE FE      CP           $FE
2532: CA 21 24   JP           Z,$2421
2535: FA CC C1   LD           A,($C1CC)
2538: A7         AND         A
2539: 20 07      JR           NZ,$2542
253B: 3C         INC         A
253C: EA CC C1   LD           ($C1CC),A
253F: CD 2B 24   CALL       $242B
2542: CD 4D 26   CALL       $264D
2545: F0 CC      LD           A,($CC)
2547: CB 67      BIT         4,A
2549: 20 22      JR           NZ,$256D
254B: CB 6F      BIT         5,A
254D: 28 51      JR           Z,$25A0
254F: 3E 1C      LD           A,$1C
2551: EA 00 21   LD           ($2100),A
2554: FA 95 DB   LD           A,($DB95)
2557: FE 07      CP           $07
2559: CA 17 26   JP           Z,$2617
255C: FA 73 C1   LD           A,($C173)
255F: 5F         LD           E,A
2560: FA 12 C1   LD           A,($C112)
2563: 57         LD           D,A
2564: 21 E1 46   LD           HL,$46E1
2567: 19         ADD         HL,DE
2568: CB 7E      BIT         7,(HL)
256A: CA 17 26   JP           Z,$2617
256D: 1E 00      LD           E,$00
256F: FA 9F C1   LD           A,($C19F)
2572: E6 80      AND         $80
2574: 28 01      JR           Z,$2577
2576: 1C         INC         E
2577: 16 00      LD           D,$00
2579: 21 1F 25   LD           HL,$251F
257C: 19         ADD         HL,DE
257D: FA 2E C1   LD           A,($C12E)
2580: 86         ADD         A,(HL)
2581: EA 01 D6   LD           ($D601),A
2584: 21 1D 25   LD           HL,$251D
2587: 19         ADD         HL,DE
2588: FA 2F C1   LD           A,($C12F)
258B: 86         ADD         A,(HL)
258C: EA 02 D6   LD           ($D602),A
258F: 3E 4F      LD           A,$4F
2591: EA 03 D6   LD           ($D603),A
2594: F0 E8      LD           A,($E8)
2596: EA 04 D6   LD           ($D604),A
2599: AF         XOR         A
259A: EA 05 D6   LD           ($D605),A
259D: CD 90 22   CALL       $2290
25A0: C9         RET
25A1: 62         LD           H,D
25A2: 82         ADD         A,D
25A3: 98         SBC         B
25A4: 99         SBC         C
25A5: 1E 00      LD           E,$00
25A7: FA 9F C1   LD           A,($C19F)
25AA: E6 80      AND         $80
25AC: 28 01      JR           Z,$25AF
25AE: 1C         INC         E
25AF: 16 00      LD           D,$00
25B1: 21 A3 25   LD           HL,$25A3
25B4: 19         ADD         HL,DE
25B5: FA 2E C1   LD           A,($C12E)
25B8: 86         ADD         A,(HL)
25B9: 47         LD           B,A
25BA: 21 A1 25   LD           HL,$25A1
25BD: 19         ADD         HL,DE
25BE: FA 2F C1   LD           A,($C12F)
25C1: 86         ADD         A,(HL)
25C2: 4F         LD           C,A
25C3: 1E 10      LD           E,$10
25C5: 79         LD           A,C
25C6: D6 20      SUB         $20
25C8: 6F         LD           L,A
25C9: 60         LD           H,B
25CA: 0A         LD           A,(BC)
25CB: 77         LD           (HL),A
25CC: C5         PUSH       BC
25CD: 79         LD           A,C
25CE: C6 20      ADD         $20
25D0: 4F         LD           C,A
25D1: 7D         LD           A,L
25D2: C6 20      ADD         $20
25D4: 6F         LD           L,A
25D5: 0A         LD           A,(BC)
25D6: 77         LD           (HL),A
25D7: 7D         LD           A,L
25D8: C6 20      ADD         $20
25DA: 6F         LD           L,A
25DB: F0 E8      LD           A,($E8)
25DD: 77         LD           (HL),A
25DE: C1         POP         BC
25DF: 03         INC         BC
25E0: 79         LD           A,C
25E1: E6 1F      AND         $1F
25E3: 20 04      JR           NZ,$25E9
25E5: 79         LD           A,C
25E6: D6 20      SUB         $20
25E8: 4F         LD           C,A
25E9: 1D         DEC         E
25EA: 20 D9      JR           NZ,$25C5
25EC: 3E 08      LD           A,$08
25EE: EA 72 C1   LD           ($C172),A
25F1: C3 90 22   JP           $2290
25F4: C9         RET
25F5: 42         LD           B,D
25F6: 62         LD           H,D
25F7: 98         SBC         B
25F8: 99         SBC         C
25F9: 1E 00      LD           E,$00
25FB: FA 9F C1   LD           A,($C19F)
25FE: E6 80      AND         $80
2600: 28 01      JR           Z,$2603
2602: 1C         INC         E
2603: 16 00      LD           D,$00
2605: 21 F7 25   LD           HL,$25F7
2608: 19         ADD         HL,DE
2609: FA 2E C1   LD           A,($C12E)
260C: 86         ADD         A,(HL)
260D: 47         LD           B,A
260E: 21 F5 25   LD           HL,$25F5
2611: CD BD 25   CALL       $25BD
2614: C3 0A 25   JP           $250A
2617: 3E 02      LD           A,$02
2619: EA 77 C1   LD           ($C177),A
261C: C3 A1 22   JP           $22A1
261F: F0 CC      LD           A,($CC)
2621: CB 6F      BIT         5,A
2623: 20 F2      JR           NZ,$2617
2625: E6 10      AND         $10
2627: C2 49 26   JP           NZ,$2649
262A: F0 CC      LD           A,($CC)
262C: E6 43      AND         $43
262E: 28 0C      JR           Z,$263C
2630: 21 77 C1   LD           HL,$C177
2633: 7E         LD           A,(HL)
2634: 3C         INC         A
2635: E6 01      AND         $01
2637: 77         LD           (HL),A
2638: 3E 0A      LD           A,$0A
263A: E0 F2      LDFF00   ($F2),A
263C: F0 E7      LD           A,($E7)
263E: E6 10      AND         $10
2640: C8         RET         Z
2641: 3E 17      LD           A,$17
2643: EA 00 21   LD           ($2100),A
2646: C3 57 7B   JP           $7B57
2649: CD A1 22   CALL       $22A1
264C: C9         RET
264D: 3E 17      LD           A,$17
264F: EA 00 21   LD           ($2100),A
2652: C3 07 7B   JP           $7B07
2655: 3E 02      LD           A,$02
2657: CD B9 07   CALL       $07B9
265A: CD 74 7B   CALL       $7B74
265D: C9         RET
265E: 01 01 20   LD           BC,$2001
2661: 20 93      JR           NZ,$25F6
2663: 93         SUB         E
2664: 13         INC         DE
2665: 13         INC         DE
2666: 10 10      STOP       $10
2668: 01 01 08   LD           BC,$0801
266B: 08 0A 0A   LD           ($0A0A),SP
266E: 01 FF F0   LD           BC,$F0FF
2671: 10 00      STOP       $00
2673: 00         NOP
2674: 03         INC         BC
2675: 00         NOP
2676: 02         LD           (BC),A
2677: 1E C0      LD           E,$C0
2679: 40         LD           B,B
267A: 3E 08      LD           A,$08
267C: EA 00 21   LD           ($2100),A
267F: CD 86 26   CALL       $2686
2682: CD C0 07   CALL       $07C0
2685: C9         RET
2686: FA 2B C1   LD           A,($C12B)
2689: FE 00      CP           $00
268B: 28 05      JR           Z,$2692
268D: 3D         DEC         A
268E: EA 2B C1   LD           ($C12B),A
2691: C9         RET
2692: FA 25 C1   LD           A,($C125)
2695: 4F         LD           C,A
2696: 06 00      LD           B,$00
2698: 3E 01      LD           A,$01
269A: EA 2B C1   LD           ($C12B),A
269D: FA 2A C1   LD           A,($C12A)
26A0: E0 D9      LDFF00   ($D9),A
26A2: 21 5E 26   LD           HL,$265E
26A5: 09         ADD         HL,BC
26A6: FA 27 C1   LD           A,($C127)
26A9: EA 02 D6   LD           ($D602),A
26AC: 86         ADD         A,(HL)
26AD: CB 12      RL           D
26AF: EA 19 D6   LD           ($D619),A
26B2: FA 26 C1   LD           A,($C126)
26B5: F6 98      OR           $98
26B7: EA 01 D6   LD           ($D601),A
26BA: CB 1A      RR           D
26BC: CE 00      ADC         $00
26BE: EA 18 D6   LD           ($D618),A
26C1: 21 62 26   LD           HL,$2662
26C4: 09         ADD         HL,BC
26C5: 7E         LD           A,(HL)
26C6: EA 03 D6   LD           ($D603),A
26C9: EA 1A D6   LD           ($D61A),A
26CC: 3E 00      LD           A,$00
26CE: EA 2F D6   LD           ($D62F),A
26D1: 3E EE      LD           A,$EE
26D3: EA 14 D6   LD           ($D614),A
26D6: EA 15 D6   LD           ($D615),A
26D9: EA 16 D6   LD           ($D616),A
26DC: EA 17 D6   LD           ($D617),A
26DF: EA 2B D6   LD           ($D62B),A
26E2: EA 2C D6   LD           ($D62C),A
26E5: EA 2D D6   LD           ($D62D),A
26E8: EA 2E D6   LD           ($D62E),A
26EB: 06 D6      LD           B,$D6
26ED: 0E 04      LD           C,$04
26EF: 16 D6      LD           D,$D6
26F1: 1E 1B      LD           E,$1B
26F3: C5         PUSH       BC
26F4: D5         PUSH       DE
26F5: F0 D9      LD           A,($D9)
26F7: 4F         LD           C,A
26F8: 06 00      LD           B,$00
26FA: 21 11 D7   LD           HL,$D711
26FD: 09         ADD         HL,BC
26FE: 06 00      LD           B,$00
2700: 4E         LD           C,(HL)
2701: CB 21      SLA         C
2703: CB 10      RL           B
2705: CB 21      SLA         C
2707: CB 10      RL           B
2709: 21 8C 49   LD           HL,$498C
270C: FA A5 DB   LD           A,($DBA5)
270F: A7         AND         A
2710: 28 03      JR           Z,$2715
2712: 21 60 4D   LD           HL,$4D60
2715: 09         ADD         HL,BC
2716: D1         POP         DE
2717: C1         POP         BC
2718: FA 25 C1   LD           A,($C125)
271B: E6 02      AND         $02
271D: 28 0E      JR           Z,$272D
271F: 2A         LD           A,(HLI)
2720: 02         LD           (BC),A
2721: 03         INC         BC
2722: 2A         LD           A,(HLI)
2723: 02         LD           (BC),A
2724: 03         INC         BC
2725: 2A         LD           A,(HLI)
2726: 12         LD           (DE),A
2727: 13         INC         DE
2728: 7E         LD           A,(HL)
2729: 12         LD           (DE),A
272A: 13         INC         DE
272B: 18 0C      JR           $2739
272D: 2A         LD           A,(HLI)
272E: 02         LD           (BC),A
272F: 2A         LD           A,(HLI)
2730: 12         LD           (DE),A
2731: 03         INC         BC
2732: 13         INC         DE
2733: 2A         LD           A,(HLI)
2734: 02         LD           (BC),A
2735: 7E         LD           A,(HL)
2736: 12         LD           (DE),A
2737: 03         INC         BC
2738: 13         INC         DE
2739: C5         PUSH       BC
273A: FA 25 C1   LD           A,($C125)
273D: 4F         LD           C,A
273E: 06 00      LD           B,$00
2740: 21 66 26   LD           HL,$2666
2743: 09         ADD         HL,BC
2744: F0 D9      LD           A,($D9)
2746: 86         ADD         A,(HL)
2747: E0 D9      LDFF00   ($D9),A
2749: C1         POP         BC
274A: FA 28 C1   LD           A,($C128)
274D: 3D         DEC         A
274E: EA 28 C1   LD           ($C128),A
2751: 20 A0      JR           NZ,$26F3
2753: FA 25 C1   LD           A,($C125)
2756: 4F         LD           C,A
2757: 06 00      LD           B,$00
2759: 21 6A 26   LD           HL,$266A
275C: 09         ADD         HL,BC
275D: 7E         LD           A,(HL)
275E: EA 28 C1   LD           ($C128),A
2761: 21 6E 26   LD           HL,$266E
2764: 09         ADD         HL,BC
2765: FA 2A C1   LD           A,($C12A)
2768: 86         ADD         A,(HL)
2769: EA 2A C1   LD           ($C12A),A
276C: 21 76 26   LD           HL,$2676
276F: 09         ADD         HL,BC
2770: FA 27 C1   LD           A,($C127)
2773: 86         ADD         A,(HL)
2774: CB 1A      RR           D
2776: E6 DF      AND         $DF
2778: EA 27 C1   LD           ($C127),A
277B: 21 72 26   LD           HL,$2672
277E: 09         ADD         HL,BC
277F: FA 26 C1   LD           A,($C126)
2782: CB 12      RL           D
2784: 8E         ADC         A,(HL)
2785: E6 03      AND         $03
2787: EA 26 C1   LD           ($C126),A
278A: FA 29 C1   LD           A,($C129)
278D: 3D         DEC         A
278E: EA 29 C1   LD           ($C129),A
2791: 20 03      JR           NZ,$2796
2793: C3 97 27   JP           $2797
2796: C9         RET
2797: FA 24 C1   LD           A,($C124)
279A: 3C         INC         A
279B: EA 24 C1   LD           ($C124),A
279E: C9         RET
279F: FF         RST         0X38
27A0: FF         RST         0X38
27A1: FF         RST         0X38
27A2: FF         RST         0X38
27A3: FF         RST         0X38
27A4: FF         RST         0X38
27A5: FF         RST         0X38
27A6: FF         RST         0X38
27A7: FF         RST         0X38
27A8: EA 68 D3   LD           ($D368),A
27AB: E0 BF      LDFF00   ($BF),A
27AD: 3E 38      LD           A,$38
27AF: E0 AB      LDFF00   ($AB),A
27B1: AF         XOR         A
27B2: E0 A8      LDFF00   ($A8),A
27B4: C9         RET
27B5: E5         PUSH       HL
27B6: 21 00 00   LD           HL,$0000
27B9: 36 0A      LD           (HL),$0A
27BB: E1         POP         HL
27BC: C9         RET
27BD: 3E 02      LD           A,$02
27BF: EA 00 21   LD           ($2100),A
27C2: C5         PUSH       BC
27C3: CD 46 41   CALL       $4146
27C6: C1         POP         BC
27C7: C3 C0 07   JP           $07C0
27CA: 3E 38      LD           A,$38
27CC: E0 A8      LDFF00   ($A8),A
27CE: AF         XOR         A
27CF: E0 AB      LDFF00   ($AB),A
27D1: C9         RET
27D2: F0 BC      LD           A,($BC)
27D4: A7         AND         A
27D5: 20 08      JR           NZ,$27DF
27D7: 3E 1F      LD           A,$1F
27D9: EA 00 21   LD           ($2100),A
27DC: CD 03 40   CALL       $4003
27DF: C3 C0 07   JP           $07C0
27E2: 3E 01      LD           A,$01
27E4: EA 00 21   LD           ($2100),A
27E7: CD CF 5B   CALL       $5BCF
27EA: C3 C0 07   JP           $07C0
27ED: E5         PUSH       HL
27EE: F0 E7      LD           A,($E7)
27F0: 21 3D C1   LD           HL,$C13D
27F3: 86         ADD         A,(HL)
27F4: 21 44 FF   LD           HL,$FF44
27F7: 86         ADD         A,(HL)
27F8: 0F         RRCA
27F9: EA 3D C1   LD           ($C13D),A
27FC: E1         POP         HL
27FD: C9         RET
27FE: FA 24 C1   LD           A,($C124)
2801: A7         AND         A
2802: 20 34      JR           NZ,$2838
2804: 3E 20      LD           A,$20
2806: E0 00      LDFF00   ($00),A
2808: F0 00      LD           A,($00)
280A: F0 00      LD           A,($00)
280C: 2F         CPL
280D: E6 0F      AND         $0F
280F: 47         LD           B,A
2810: 3E 10      LD           A,$10
2812: E0 00      LDFF00   ($00),A
2814: F0 00      LD           A,($00)
2816: F0 00      LD           A,($00)
2818: F0 00      LD           A,($00)
281A: F0 00      LD           A,($00)
281C: F0 00      LD           A,($00)
281E: F0 00      LD           A,($00)
2820: F0 00      LD           A,($00)
2822: F0 00      LD           A,($00)
2824: CB 37      SWAP       A
2826: 2F         CPL
2827: E6 F0      AND         $F0
2829: B0         OR           B
282A: 4F         LD           C,A
282B: F0 CB      LD           A,($CB)
282D: A9         XOR         C
282E: A1         AND         C
282F: E0 CC      LDFF00   ($CC),A
2831: 79         LD           A,C
2832: E0 CB      LDFF00   ($CB),A
2834: 3E 30      LD           A,$30
2836: E0 00      LDFF00   ($00),A
2838: C9         RET
2839: C5         PUSH       BC
283A: F0 CD      LD           A,($CD)
283C: 21 97 FF   LD           HL,$FF97
283F: 86         ADD         A,(HL)
2840: E6 F8      AND         $F8
2842: CB 3F      SRL         A
2844: CB 3F      SRL         A
2846: CB 3F      SRL         A
2848: 11 00 00   LD           DE,$0000
284B: 5F         LD           E,A
284C: 21 00 98   LD           HL,$9800
284F: 06 20      LD           B,$20
2851: 19         ADD         HL,DE
2852: 05         DEC         B
2853: 20 FC      JR           NZ,$2851
2855: E5         PUSH       HL
2856: F0 CE      LD           A,($CE)
2858: 21 96 FF   LD           HL,$FF96
285B: 86         ADD         A,(HL)
285C: E1         POP         HL
285D: E6 F8      AND         $F8
285F: CB 3F      SRL         A
2861: CB 3F      SRL         A
2863: CB 3F      SRL         A
2865: 11 00 00   LD           DE,$0000
2868: 5F         LD           E,A
2869: 19         ADD         HL,DE
286A: 7C         LD           A,H
286B: E0 CF      LDFF00   ($CF),A
286D: 7D         LD           A,L
286E: E0 D0      LDFF00   ($D0),A
2870: C1         POP         BC
2871: C9         RET

; Normally RST 0 (reset) would come here. But boot rom gets reset.
; Instead, this is used as a table-jumper.
;
; Jump table follows RST 0 instruction. A has table entry.
; Look up address and jump to it
TableJump:
2872: 5F         LD           E,A ; A*2 ...
2873: 16 00      LD           D,$00 ; ... to ..
2875: CB 23      SLA         E ; ...
2877: CB 12      RL           D ; DE
2879: E1         POP         HL ; Next byte in caller
287A: 19         ADD         HL,DE ; Offset into table
287B: 5E         LD           E,(HL) ; Get LSB from table
287C: 23         INC         HL ; Next byte
287D: 56         LD           D,(HL) ; Get MSB from table
287E: D5         PUSH       DE ; Jump address ...
287F: E1         POP         HL ; ... to HL
2880: E9         JP           (HL) ; Jump to routine

; Turn off LCD at next vertical blanking
LCDOff:
2881: F0 FF      LD       A,($FF) ; Current interrupt register
2883: E0 D2      LDFF00   ($D2),A ; Hold it in RAM
2885: CB 87      RES         0,A ; ??
2887: F0 44      LD       A,($44) ; Wait for ...
2889: FE 91      CP           $91 ; ... line 145 ...
288B: 20 FA      JR           NZ,$2887 ; ... Vertical Blanking
288D: F0 40      LD           A,($40) ; LCD control
288F: E6 7F      AND         $7F ; Turn ...
2891: E0 40      LDFF00   ($40),A ; ... LCD off
2893: F0 D2      LD           A,($D2) ; Old interrupt value
2895: E0 FF      LDFF00   ($FF),A ; Restore interrupts
2897: C9         RET ; Done

2898: 3E 01      LD           A,$01
289A: CD B9 07   CALL       $07B9
289D: CD F3 7C   CALL       $7CF3
28A0: C9         RET
28A1: 3E 7E      LD           A,$7E
28A3: 01 00 04   LD           BC,$0400
28A6: 18 05      JR           $28AD
       
; Fill Background Tile Table with all 7Fs
ClearMap:
28A8: 3E 7F      LD           A,$7F ; Blank background tile number
28AA: 01 00 08   LD           BC,$0800 ; 800 bytes
28AD: 57         LD           D,A ; Pattern to D (we'll mutilate A shortly)
28AE: 21 00 98   LD           HL,$9800 ; Background Tile Table
28B1: 7A         LD           A,D ; Tile number
28B2: 22         LD           (HLI),A ; Store in table and HL++
28B3: 0B         DEC         BC ; Count down
28B4: 78         LD           A,B ; All ...
28B5: B1         OR           C ; ... done?
28B6: 20 F9      JR           NZ,$28B1 ; No ... keep going
28B8: C9         RET ; OUT

; Switch to bank A, copy HL to DE (BC bytes), switch to bank 1
BankCopyHLtoDE:
28B9: EA 00 21   LD           ($2100),A
28BC: CD C5 28   CALL       $28C5
28BF: 3E 01      LD           A,$01
28C1: EA 00 21   LD           ($2100),A
28C4: C9         RET

; From HL to DE ... count BC
CopyHLtoDE:
28C5: 2A         LD           A,(HLI) ; From (HL++)
28C6: 12         LD           (DE),A ; To (DE)
28C7: 13         INC         DE ; Bump destination pointer
28C8: 0B         DEC         BC ; Decrement count
28C9: 78         LD           A,B ; Reached ...
28CA: B1         OR           C ; ... zero?
28CB: 20 F8      JR           NZ,$28C5 ; No ... keep copying
28CD: C9         RET ; Done

28CE: 13         INC         DE
28CF: 67         LD           H,A
28D0: 1A         LD           A,(DE)
28D1: 6F         LD           L,A
28D2: 13         INC         DE
28D3: 1A         LD           A,(DE)
28D4: 13         INC         DE
28D5: CD F2 28   CALL       $28F2
28D8: FA 24 C1   LD           A,($C124)
28DB: A7         AND         A
28DC: 20 0F      JR           NZ,$28ED
28DE: 1A         LD           A,(DE)
28DF: A7         AND         A
28E0: 20 EC      JR           NZ,$28CE
28E2: C9         RET
28E3: 13         INC         DE
28E4: 67         LD           H,A
28E5: 1A         LD           A,(DE)
28E6: 6F         LD           L,A
28E7: 13         INC         DE
28E8: 1A         LD           A,(DE)
28E9: 13         INC         DE
28EA: CD 48 29   CALL       $2948
28ED: 1A         LD           A,(DE)
28EE: A7         AND         A
28EF: 20 F2      JR           NZ,$28E3
28F1: C9         RET
28F2: F5         PUSH       AF
28F3: E6 3F      AND         $3F
28F5: 47         LD           B,A
28F6: 04         INC         B
28F7: F1         POP         AF
28F8: 07         RLCA
28F9: 07         RLCA
28FA: E6 03      AND         $03
28FC: 28 08      JR           Z,$2906
28FE: 3D         DEC         A
28FF: 28 19      JR           Z,$291A
2901: 3D         DEC         A
2902: 28 2A      JR           Z,$292E
2904: 18 35      JR           $293B
2906: 1A         LD           A,(DE)
2907: 22         LD           (HLI),A
2908: 7D         LD           A,L
2909: E6 1F      AND         $1F
290B: 20 08      JR           NZ,$2915
290D: 7D         LD           A,L
290E: D6 20      SUB         $20
2910: 6F         LD           L,A
2911: 7C         LD           A,H
2912: DE 00      SBC         $00
2914: 67         LD           H,A
2915: 13         INC         DE
2916: 05         DEC         B
2917: 20 ED      JR           NZ,$2906
2919: C9         RET
291A: 1A         LD           A,(DE)
291B: 22         LD           (HLI),A
291C: 7D         LD           A,L
291D: E6 1F      AND         $1F
291F: 20 08      JR           NZ,$2929
2921: 7D         LD           A,L
2922: D6 20      SUB         $20
2924: 6F         LD           L,A
2925: 7C         LD           A,H
2926: DE 00      SBC         $00
2928: 67         LD           H,A
2929: 05         DEC         B
292A: 20 EE      JR           NZ,$291A
292C: 13         INC         DE
292D: C9         RET
292E: 1A         LD           A,(DE)
292F: 77         LD           (HL),A
2930: 13         INC         DE
2931: 78         LD           A,B
2932: 01 20 00   LD           BC,$0020
2935: 09         ADD         HL,BC
2936: 47         LD           B,A
2937: 05         DEC         B
2938: 20 F4      JR           NZ,$292E
293A: C9         RET
293B: 1A         LD           A,(DE)
293C: 77         LD           (HL),A
293D: 78         LD           A,B
293E: 01 20 00   LD           BC,$0020
2941: 09         ADD         HL,BC
2942: 47         LD           B,A
2943: 05         DEC         B
2944: 20 F5      JR           NZ,$293B
2946: 13         INC         DE
2947: C9         RET
2948: F5         PUSH       AF
2949: E6 3F      AND         $3F
294B: 47         LD           B,A
294C: 04         INC         B
294D: F1         POP         AF
294E: E6 80      AND         $80
2950: 20 18      JR           NZ,$296A
2952: 1A         LD           A,(DE)
2953: FE EE      CP           $EE
2955: 28 0E      JR           Z,$2965
2957: 22         LD           (HLI),A
2958: 7D         LD           A,L
2959: E6 1F      AND         $1F
295B: 20 08      JR           NZ,$2965
295D: 7D         LD           A,L
295E: D6 20      SUB         $20
2960: 6F         LD           L,A
2961: 7C         LD           A,H
2962: DE 00      SBC         $00
2964: 67         LD           H,A
2965: 13         INC         DE
2966: 05         DEC         B
2967: 20 E9      JR           NZ,$2952
2969: C9         RET
296A: 1A         LD           A,(DE)
296B: FE EE      CP           $EE
296D: 28 01      JR           Z,$2970
296F: 77         LD           (HL),A
2970: 13         INC         DE
2971: 78         LD           A,B
2972: 01 20 00   LD           BC,$0020
2975: 09         ADD         HL,BC
2976: 47         LD           B,A
2977: 05         DEC         B
2978: 20 F0      JR           NZ,$296A
297A: C9         RET
297B: 01 00 16   LD           BC,$1600
297E: 18 16      JR           $2996
2980: 01 00 13   LD           BC,$1300
2983: 18 11      JR           $2996
2985: 01 2F 00   LD           BC,$002F
2988: 18 03      JR           $298D

; Clear HRAM and RAM
ClearRAM:
298A: 01 6D 00   LD           BC,$006D ; ?Is this all we use in HRAM
298D: 21 90 FF   LD           HL,$FF90
2990: CD 99 29   CALL       $2999
2993: 01 00 1F   LD           BC,$1F00 ; Clear RAM ...
2996: 21 00 C0   LD           HL,$C000 ; ... C000 - DF00 (all but stack)

; clear BC bytes of memory at HL
ClearRAMHL:
2999: AF         XOR         A ; A = 0
299A: 22         LD           (HLI),A ; Clear (HL++)
299B: 0B         DEC         BC ; Decrement count
299C: 78         LD           A,B ; All ...
299D: B1         OR           C ; ... done?
299E: 20 F9      JR           NZ,$2999 ; No... keep clearing
29A0: C9         RET ; Out

29A1: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF           
29B0: FF FF FF FF FF FF FF FF    
        
29B8: 3E 14      LD           A,$14 ; Switch in ...
29BA: EA 00 21   LD           ($2100),A ; ... bank 14
29BD: 21 00 45   LD           HL,$4500
29C0: 19         ADD         HL,DE
29C1: 7E         LD           A,(HL)
29C2: C3 C0 07   JP           $07C0
29C5: FA AC C5   LD           A,($C5AC)
29C8: A7         AND         A
29C9: 20 04      JR           NZ,$29CF
29CB: 3E 2D      LD           A,$2D
29CD: E0 F4      LDFF00   ($F4),A
29CF: C9         RET
29D0: 3E 01      LD           A,$01
29D2: EA 00 21   LD           ($2100),A
29D5: CD 07 58   CALL       $5807
29D8: C3 C0 07   JP           $07C0
29DB: 3E 08      LD           A,$08
29DD: EA 00 21   LD           ($2100),A
29E0: 21 10 51   LD           HL,$5110
29E3: 19         ADD         HL,DE
29E4: 7E         LD           A,(HL)
29E5: C3 C0 07   JP           $07C0
29E8: 3E 08      LD           A,$08
29EA: EA 00 21   LD           ($2100),A
29ED: 21 10 51   LD           HL,$5110
29F0: 19         ADD         HL,DE
29F1: 7E         LD           A,(HL)
29F2: F5         PUSH       AF
29F3: 3E 03      LD           A,$03
29F5: EA 00 21   LD           ($2100),A
29F8: F1         POP         AF
29F9: C9         RET
29FA: 3E 13      LD           A,$13
29FC: EA 00 21   LD           ($2100),A
29FF: 21 00 68   LD           HL,$6800
2A02: 11 00 90   LD           DE,$9000
2A05: 01 00 08   LD           BC,$0800
2A08: CD C5 28   CALL       $28C5
2A0B: 21 00 70   LD           HL,$7000
2A0E: 11 00 88   LD           DE,$8800
2A11: 01 00 08   LD           BC,$0800
2A14: C3 C5 28   JP           $28C5
2A17: CD 26 2A   CALL       $2A26
2A1A: 11 00 84   LD           DE,$8400
2A1D: 21 00 76   LD           HL,$7600
2A20: 01 00 01   LD           BC,$0100
2A23: C3 C5 28   JP           $28C5
2A26: 3E 13      LD           A,$13
2A28: EA 00 21   LD           ($2100),A
2A2B: 21 00 40   LD           HL,$4000
2A2E: 11 00 80   LD           DE,$8000
2A31: 01 00 18   LD           BC,$1800
2A34: CD C5 28   CALL       $28C5
2A37: 3E 0C      LD           A,$0C
2A39: EA 00 21   LD           ($2100),A
2A3C: 21 E0 57   LD           HL,$57E0
2A3F: 11 F0 97   LD           DE,$97F0
2A42: 01 10 00   LD           BC,$0010
2A45: CD C5 28   CALL       $28C5
2A48: 3E 12      LD           A,$12
2A4A: EA 00 21   LD           ($2100),A
2A4D: 21 00 75   LD           HL,$7500
2A50: 11 00 80   LD           DE,$8000
2A53: 01 40 00   LD           BC,$0040
2A56: CD C5 28   CALL       $28C5
2A59: 11 00 8D   LD           DE,$8D00
2A5C: 21 00 75   LD           HL,$7500
2A5F: 01 00 02   LD           BC,$0200
2A62: C3 C5 28   JP           $28C5
2A65: 3E 0C      LD           A,$0C
2A67: EA 00 21   LD           ($2100),A
2A6A: 21 00 50   LD           HL,$5000
2A6D: 11 00 90   LD           DE,$9000
2A70: 01 00 08   LD           BC,$0800
2A73: CD C5 28   CALL       $28C5
2A76: 3E 12      LD           A,$12
2A78: EA 00 21   LD           ($2100),A
2A7B: 21 00 60   LD           HL,$6000
2A7E: 11 00 80   LD           DE,$8000
2A81: 01 00 08   LD           BC,$0800
2A84: CD C5 28   CALL       $28C5
2A87: 3E 0F      LD           A,$0F
2A89: EA 00 21   LD           ($2100),A
2A8C: 21 00 60   LD           HL,$6000
2A8F: 11 00 88   LD           DE,$8800
2A92: 01 00 08   LD           BC,$0800
2A95: C3 C5 28   JP           $28C5
2A98: 21 00 40   LD           HL,$4000
2A9B: 18 08      JR           $2AA5
2A9D: 21 00 48   LD           HL,$4800
2AA0: 18 03      JR           $2AA5
2AA2: 21 00 60   LD           HL,$6000
2AA5: 3E 13      LD           A,$13
2AA7: EA 00 21   LD           ($2100),A
2AAA: 11 00 80   LD           DE,$8000
2AAD: 01 00 08   LD           BC,$0800
2AB0: CD C5 28   CALL       $28C5
2AB3: 21 00 58   LD           HL,$5800
2AB6: 11 00 88   LD           DE,$8800
2AB9: 01 00 10   LD           BC,$1000
2ABC: C3 C5 28   JP           $28C5
2ABF: CD 44 08   CALL       $0844
2AC2: 21 00 68   LD           HL,$6800
2AC5: 3E 10      LD           A,$10
2AC7: CD FC 2A   CALL       $2AFC
2ACA: CD 44 08   CALL       $0844
2ACD: 3E 12      LD           A,$12
2ACF: EA 00 21   LD           ($2100),A
2AD2: 21 00 66   LD           HL,$6600
2AD5: 11 00 80   LD           DE,$8000
2AD8: 01 80 00   LD           BC,$0080
2ADB: CD C5 28   CALL       $28C5
2ADE: CD 44 08   CALL       $0844
2AE1: 3E 0C      LD           A,$0C
2AE3: EA 00 21   LD           ($2100),A
2AE6: 21 20 42   LD           HL,$4220
2AE9: 11 00 81   LD           DE,$8100
2AEC: 01 20 00   LD           BC,$0020
2AEF: C3 C5 28   JP           $28C5
2AF2: 21 00 78   LD           HL,$7800
2AF5: 18 03      JR           $2AFA
2AF7: 21 00 48   LD           HL,$4800
2AFA: 3E 13      LD           A,$13
2AFC: EA 00 21   LD           ($2100),A
2AFF: 11 00 80   LD           DE,$8000
2B02: 01 00 08   LD           BC,$0800
2B05: CD C5 28   CALL       $28C5
2B08: 3E 13      LD           A,$13
2B0A: EA 00 21   LD           ($2100),A
2B0D: 21 00 70   LD           HL,$7000
2B10: 11 00 88   LD           DE,$8800
2B13: 01 00 08   LD           BC,$0800
2B16: CD C5 28   CALL       $28C5
2B19: 21 00 68   LD           HL,$6800
2B1C: 11 00 90   LD           DE,$9000
2B1F: 01 00 08   LD           BC,$0800
2B22: C3 C5 28   JP           $28C5
2B25: C5         PUSH       BC
2B26: 3E 14      LD           A,$14
2B28: EA 00 21   LD           ($2100),A
2B2B: 21 00 42   LD           HL,$4200
2B2E: F0 F7      LD           A,($F7)
2B30: FE 0B      CP           $0B
2B32: 30 32      JR           NC,$2B66
2B34: CB 37      SWAP       A
2B36: 4F         LD           C,A
2B37: 06 00      LD           B,$00
2B39: CB 21      SLA         C
2B3B: CB 10      RL           B
2B3D: CB 21      SLA         C
2B3F: CB 10      RL           B
2B41: 09         ADD         HL,BC
2B42: F0 F7      LD           A,($F7)
2B44: FE 06      CP           $06
2B46: 20 0A      JR           NZ,$2B52
2B48: FA 6B DB   LD           A,($DB6B)
2B4B: E6 04      AND         $04
2B4D: 28 03      JR           Z,$2B52
2B4F: 21 C0 44   LD           HL,$44C0
2B52: 19         ADD         HL,DE
2B53: 7E         LD           A,(HL)
2B54: 5F         LD           E,A
2B55: 16 00      LD           D,$00
2B57: F0 F7      LD           A,($F7)
2B59: FE 1A      CP           $1A
2B5B: 30 05      JR           NC,$2B62
2B5D: FE 06      CP           $06
2B5F: 38 01      JR           C,$2B62
2B61: 14         INC         D
2B62: 21 00 D9   LD           HL,$D900
2B65: 19         ADD         HL,DE
2B66: CD C0 07   CALL       $07C0
2B69: C1         POP         BC
2B6A: C9         RET

; Lots of copy to tile pattern
2B6B: 3E 0C      LD           A,$0C ; Switch in ...
2B6D: CD B9 07   CALL       $07B9 ; ... bank 0C
2B70: 21 00 40   LD           HL,$4000
2B73: 11 00 80   LD           DE,$8000
2B76: 01 00 04   LD           BC,$0400
2B79: CD C5 28   CALL       $28C5
;
2B7C: 3E 0C      LD           A,$0C ; Switch in ...
2B7E: CD B9 07   CALL       $07B9 ; ... bank 0C
2B81: 21 00 48   LD           HL,$4800
2B84: 11 00 88   LD           DE,$8800
2B87: 01 00 10   LD           BC,$1000
2B8A: CD C5 28   CALL       $28C5
;
2B8D: 21 A0 47   LD           HL,$47A0
2B90: 11 00 8E   LD           DE,$8E00
2B93: 01 20 00   LD           BC,$0020
2B96: CD C5 28   CALL       $28C5
;           
2B99: 3E 01      LD           A,$01 ; Switch in ...
2B9B: CD B9 07   CALL       $07B9 ; ... bank 01
2B9E: C9         RET ; Out

2B9F: CD 6B 2B   CALL       $2B6B
2BA2: 3E 0F      LD           A,$0F
2BA4: CD B9 07   CALL       $07B9
2BA7: 21 00 40   LD           HL,$4000
2BAA: 11 00 88   LD           DE,$8800
2BAD: 01 00 04   LD           BC,$0400
2BB0: CD C5 28   CALL       $28C5
2BB3: 3E 0F      LD           A,$0F
2BB5: CD B9 07   CALL       $07B9
2BB8: 21 00 50   LD           HL,$5000
2BBB: 11 00 90   LD           DE,$9000
2BBE: 01 00 08   LD           BC,$0800
2BC1: C3 C5 28   JP           $28C5
2BC4: 3E 01      LD           A,$01
2BC6: CD B9 07   CALL       $07B9
2BC9: F0 F7      LD           A,($F7)
2BCB: 5F         LD           E,A
2BCC: 16 00      LD           D,$00
2BCE: D5         PUSH       DE
2BCF: 21 64 7F   LD           HL,$7F64
2BD2: 19         ADD         HL,DE
2BD3: 66         LD           H,(HL)
2BD4: 2E 00      LD           L,$00
2BD6: 3E 0D      LD           A,$0D
2BD8: CD B9 07   CALL       $07B9
2BDB: 11 00 91   LD           DE,$9100
2BDE: 01 00 01   LD           BC,$0100
2BE1: CD C5 28   CALL       $28C5
2BE4: 21 00 40   LD           HL,$4000
2BE7: 11 00 92   LD           DE,$9200
2BEA: 01 00 06   LD           BC,$0600
2BED: CD C5 28   CALL       $28C5
2BF0: 3E 01      LD           A,$01
2BF2: EA 00 21   LD           ($2100),A
2BF5: D1         POP         DE
2BF6: D5         PUSH       DE
2BF7: 21 84 7F   LD           HL,$7F84
2BFA: 19         ADD         HL,DE
2BFB: 66         LD           H,(HL)
2BFC: 2E 00      LD           L,$00
2BFE: CD C0 07   CALL       $07C0
2C01: 11 00 92   LD           DE,$9200
2C04: 01 00 02   LD           BC,$0200
2C07: CD C5 28   CALL       $28C5
2C0A: 3E 0C      LD           A,$0C
2C0C: EA 00 21   LD           ($2100),A
2C0F: 21 C0 47   LD           HL,$47C0
2C12: 11 C0 DC   LD           DE,$DCC0
2C15: 01 40 00   LD           BC,$0040
2C18: CD C5 28   CALL       $28C5
2C1B: CD A1 2C   CALL       $2CA1
2C1E: 3E 01      LD           A,$01
2C20: EA 00 21   LD           ($2100),A
2C23: D1         POP         DE
2C24: 21 A4 7F   LD           HL,$7FA4
2C27: 19         ADD         HL,DE
2C28: 66         LD           H,(HL)
2C29: 2E 00      LD           L,$00
2C2B: 3E 12      LD           A,$12
2C2D: CD B9 07   CALL       $07B9
2C30: 11 00 8F   LD           DE,$8F00
2C33: 01 00 01   LD           BC,$0100
2C36: CD C5 28   CALL       $28C5
2C39: 21 00 7D   LD           HL,$7D00
2C3C: F0 F7      LD           A,($F7)
2C3E: FE 0A      CP           $0A
2C40: 38 08      JR           C,$2C4A
2C42: 3E 0C      LD           A,$0C
2C44: CD B9 07   CALL       $07B9
2C47: 21 00 4C   LD           HL,$4C00
2C4A: 11 00 8C   LD           DE,$8C00
2C4D: 01 00 03   LD           BC,$0300
2C50: CD C5 28   CALL       $28C5
2C53: FA 4B DB   LD           A,($DB4B)
2C56: A7         AND         A
2C57: 28 03      JR           Z,$2C5C
2C59: CD 54 1D   CALL       $1D54
2C5C: FA A5 DB   LD           A,($DBA5)
2C5F: A7         AND         A
2C60: 28 06      JR           Z,$2C68
2C62: F0 F7      LD           A,($F7)
2C64: FE 0A      CP           $0A
2C66: 38 0A      JR           C,$2C72
2C68: FA 15 DB   LD           A,($DB15)
2C6B: FE 06      CP           $06
2C6D: 38 03      JR           C,$2C72
2C6F: CD BE 1D   CALL       $1DBE
2C72: FA 0E DB   LD           A,($DB0E)
2C75: FE 02      CP           $02
2C77: 38 04      JR           C,$2C7D
2C79: 3E 0D      LD           A,$0D
2C7B: E0 A5      LDFF00   ($A5),A
2C7D: C9         RET
2C7E: 3E 0C      LD           A,$0C
2C80: CD B9 07   CALL       $07B9
2C83: 21 00 52   LD           HL,$5200
2C86: 11 00 92   LD           DE,$9200
2C89: 01 00 06   LD           BC,$0600
2C8C: CD C5 28   CALL       $28C5
2C8F: 21 00 4C   LD           HL,$4C00
2C92: 11 00 8C   LD           DE,$8C00
2C95: 01 00 04   LD           BC,$0400
2C98: CD C5 28   CALL       $28C5
2C9B: CD A1 2C   CALL       $2CA1
2C9E: C3 53 2C   JP           $2C53
2CA1: AF         XOR         A
2CA2: E0 A6      LDFF00   ($A6),A
2CA4: E0 A7      LDFF00   ($A7),A
2CA6: CD 6B 1B   CALL       $1B6B
2CA9: 21 00 48   LD           HL,$4800
2CAC: 11 00 88   LD           DE,$8800
2CAF: 01 00 08   LD           BC,$0800
2CB2: CD C5 28   CALL       $28C5
2CB5: 21 00 42   LD           HL,$4200
2CB8: 11 00 82   LD           DE,$8200
2CBB: 01 00 01   LD           BC,$0100
2CBE: CD C5 28   CALL       $28C5
2CC1: C9         RET
2CC2: 3E 01      LD           A,$01
2CC4: CD B9 07   CALL       $07B9
2CC7: 21 31 7D   LD           HL,$7D31
2CCA: 11 00 87   LD           DE,$8700
2CCD: 01 80 00   LD           BC,$0080
2CD0: CD C5 28   CALL       $28C5
2CD3: 3E 10      LD           A,$10
2CD5: CD B9 07   CALL       $07B9
2CD8: 21 00 54   LD           HL,$5400
2CDB: 11 00 80   LD           DE,$8000
2CDE: 01 00 06   LD           BC,$0600
2CE1: CD C5 28   CALL       $28C5
2CE4: 21 00 40   LD           HL,$4000
2CE7: 11 00 88   LD           DE,$8800
2CEA: 01 00 10   LD           BC,$1000
2CED: C3 C5 28   JP           $28C5
2CF0: 3E 0F      LD           A,$0F
2CF2: CD B9 07   CALL       $07B9
2CF5: 21 00 49   LD           HL,$4900
2CF8: 11 00 88   LD           DE,$8800
2CFB: 01 00 07   LD           BC,$0700
2CFE: C3 C5 28   JP           $28C5
2D01: 3E 0C      LD           A,$0C
2D03: CD B9 07   CALL       $07B9
2D06: 21 00 78   LD           HL,$7800
2D09: 11 00 8F   LD           DE,$8F00
2D0C: 01 00 08   LD           BC,$0800
2D0F: CD C5 28   CALL       $28C5
2D12: 21 00 50   LD           HL,$5000
2D15: 11 00 82   LD           DE,$8200
2D18: 01 00 01   LD           BC,$0100
2D1B: C3 C5 28   JP           $28C5
2D1E: 21 00 70   LD           HL,$7000
2D21: 18 08      JR           $2D2B
2D23: 21 00 78   LD           HL,$7800
2D26: 18 03      JR           $2D2B
2D28: 21 00 58   LD           HL,$5800
2D2B: 3E 10      LD           A,$10
2D2D: CD B9 07   CALL       $07B9
2D30: 11 00 90   LD           DE,$9000
2D33: 01 00 08   LD           BC,$0800
2D36: C3 C5 28   JP           $28C5
2D39: 3E 13      LD           A,$13
2D3B: EA 00 21   LD           ($2100),A
2D3E: 21 00 7C   LD           HL,$7C00
2D41: 11 00 8C   LD           DE,$8C00
2D44: 01 00 04   LD           BC,$0400
2D47: CD C5 28   CALL       $28C5
2D4A: 21 00 68   LD           HL,$6800
2D4D: 11 00 90   LD           DE,$9000
2D50: 01 00 04   LD           BC,$0400
2D53: C3 C5 28   JP           $28C5
2D56: 3E 10      LD           A,$10
2D58: CD B9 07   CALL       $07B9
2D5B: 21 00 67   LD           HL,$6700
2D5E: 11 00 84   LD           DE,$8400
2D61: 01 00 04   LD           BC,$0400
2D64: CD C5 28   CALL       $28C5
2D67: 21 00 60   LD           HL,$6000
2D6A: 11 00 90   LD           DE,$9000
2D6D: 01 00 06   LD           BC,$0600
2D70: C3 C5 28   JP           $28C5
2D73: 3E 0F      LD           A,$0F
2D75: CD B9 07   CALL       $07B9
2D78: 21 00 44   LD           HL,$4400
2D7B: 11 00 88   LD           DE,$8800
2D7E: 01 00 05   LD           BC,$0500
2D81: C3 C5 28   JP           $28C5
2D84: 00         NOP
2D85: 11 0E 12   LD           DE,$120E
2D88: AF         XOR         A
2D89: E0 D7      LDFF00   ($D7),A
2D8B: 21 93 C1   LD           HL,$C193
2D8E: 5F         LD           E,A
2D8F: 16 00      LD           D,$00
2D91: 19         ADD         HL,DE
2D92: A7         AND         A
2D93: 20 42      JR           NZ,$2DD7
2D95: FA A5 DB   LD           A,($DBA5)
2D98: A7         AND         A
2D99: 28 19      JR           Z,$2DB4
2D9B: F0 F9      LD           A,($F9)
2D9D: A7         AND         A
2D9E: 20 37      JR           NZ,$2DD7
2DA0: F0 F7      LD           A,($F7)
2DA2: FE 14      CP           $14
2DA4: 28 31      JR           Z,$2DD7
2DA6: FE 0A      CP           $0A
2DA8: 38 2D      JR           C,$2DD7
2DAA: F0 F6      LD           A,($F6)
2DAC: FE FD      CP           $FD
2DAE: 28 27      JR           Z,$2DD7
2DB0: FE B1      CP           $B1
2DB2: 28 23      JR           Z,$2DD7
2DB4: FA 56 DB   LD           A,($DB56)
2DB7: FE 01      CP           $01
2DB9: 3E A4      LD           A,$A4
2DBB: 28 18      JR           Z,$2DD5
2DBD: FA 79 DB   LD           A,($DB79)
2DC0: A7         AND         A
2DC1: 3E D8      LD           A,$D8
2DC3: 20 10      JR           NZ,$2DD5
2DC5: FA 7B DB   LD           A,($DB7B)
2DC8: A7         AND         A
2DC9: 3E DD      LD           A,$DD
2DCB: 20 08      JR           NZ,$2DD5
2DCD: FA 73 DB   LD           A,($DB73)
2DD0: A7         AND         A
2DD1: 28 04      JR           Z,$2DD7
2DD3: 3E 8F      LD           A,$8F
2DD5: 18 01      JR           $2DD8
2DD7: 7E         LD           A,(HL)
2DD8: F5         PUSH       AF
2DD9: E6 3F      AND         $3F
2DDB: 47         LD           B,A
2DDC: 0E 00      LD           C,$00
2DDE: F1         POP         AF
2DDF: CB 37      SWAP       A
2DE1: 1F         RRA
2DE2: 1F         RRA
2DE3: E6 03      AND         $03
2DE5: 5F         LD           E,A
2DE6: 16 00      LD           D,$00
2DE8: 21 84 2D   LD           HL,$2D84
2DEB: 19         ADD         HL,DE
2DEC: 7E         LD           A,(HL)
2DED: EA 00 21   LD           ($2100),A
2DF0: F0 D7      LD           A,($D7)
2DF2: 57         LD           D,A
2DF3: 1E 00      LD           E,$00
2DF5: 21 00 84   LD           HL,$8400
2DF8: 19         ADD         HL,DE
2DF9: E5         PUSH       HL
2DFA: D1         POP         DE
2DFB: 21 00 40   LD           HL,$4000
2DFE: 09         ADD         HL,BC
2DFF: 01 00 01   LD           BC,$0100
2E02: CD C5 28   CALL       $28C5
2E05: F0 D7      LD           A,($D7)
2E07: 3C         INC         A
2E08: FE 04      CP           $04
2E0A: C2 89 2D   JP           NZ,$2D89
2E0D: 11 00 90   LD           DE,$9000
2E10: FA A5 DB   LD           A,($DBA5)
2E13: A7         AND         A
2E14: 28 3F      JR           Z,$2E55
2E16: 3E 0D      LD           A,$0D
2E18: EA 00 21   LD           ($2100),A
2E1B: F0 F9      LD           A,($F9)
2E1D: A7         AND         A
2E1E: 28 22      JR           Z,$2E42
2E20: 21 00 70   LD           HL,$7000
2E23: F0 F7      LD           A,($F7)
2E25: FE 06      CP           $06
2E27: 28 0F      JR           Z,$2E38
2E29: FE 0A      CP           $0A
2E2B: 30 05      JR           NC,$2E32
2E2D: 21 00 78   LD           HL,$7800
2E30: 18 06      JR           $2E38
2E32: F0 F6      LD           A,($F6)
2E34: FE E9      CP           $E9
2E36: 28 F5      JR           Z,$2E2D
2E38: 11 00 90   LD           DE,$9000
2E3B: 01 00 08   LD           BC,$0800
2E3E: CD C5 28   CALL       $28C5
2E41: C9         RET
2E42: 21 00 50   LD           HL,$5000
2E45: F0 94      LD           A,($94)
2E47: FE FF      CP           $FF
2E49: 28 09      JR           Z,$2E54
2E4B: C6 50      ADD         $50
2E4D: 67         LD           H,A
2E4E: 01 00 01   LD           BC,$0100
2E51: CD C5 28   CALL       $28C5
2E54: C9         RET
2E55: 3E 0F      LD           A,$0F
2E57: EA 00 21   LD           ($2100),A
2E5A: F0 94      LD           A,($94)
2E5C: FE 0F      CP           $0F
2E5E: 28 0B      JR           Z,$2E6B
2E60: C6 40      ADD         $40
2E62: 67         LD           H,A
2E63: 2E 00      LD           L,$00
2E65: 01 00 02   LD           BC,$0200
2E68: CD C5 28   CALL       $28C5
2E6B: C9         RET
2E6C: 3E 08      LD           A,$08
2E6E: CD B9 07   CALL       $07B9
2E71: 11 00 98   LD           DE,$9800
2E74: 21 11 D7   LD           HL,$D711
2E77: 0E 80      LD           C,$80
2E79: D5         PUSH       DE
2E7A: E5         PUSH       HL
2E7B: C5         PUSH       BC
2E7C: 7E         LD           A,(HL)
2E7D: 4F         LD           C,A
2E7E: 06 00      LD           B,$00
2E80: CB 21      SLA         C
2E82: CB 10      RL           B
2E84: CB 21      SLA         C
2E86: CB 10      RL           B
2E88: 21 8C 49   LD           HL,$498C
2E8B: FA A5 DB   LD           A,($DBA5)
2E8E: A7         AND         A
2E8F: 28 03      JR           Z,$2E94
2E91: 21 60 4D   LD           HL,$4D60
2E94: 09         ADD         HL,BC
2E95: 2A         LD           A,(HLI)
2E96: 12         LD           (DE),A
2E97: 13         INC         DE
2E98: 2A         LD           A,(HLI)
2E99: 12         LD           (DE),A
2E9A: 7B         LD           A,E
2E9B: C6 1F      ADD         $1F
2E9D: 5F         LD           E,A
2E9E: 7A         LD           A,D
2E9F: CE 00      ADC         $00
2EA1: 57         LD           D,A
2EA2: 2A         LD           A,(HLI)
2EA3: 12         LD           (DE),A
2EA4: 13         INC         DE
2EA5: 7E         LD           A,(HL)
2EA6: 12         LD           (DE),A
2EA7: C1         POP         BC
2EA8: E1         POP         HL
2EA9: D1         POP         DE
2EAA: 23         INC         HL
2EAB: 7D         LD           A,L
2EAC: E6 0F      AND         $0F
2EAE: FE 0B      CP           $0B
2EB0: 20 06      JR           NZ,$2EB8
2EB2: 7D         LD           A,L
2EB3: E6 F0      AND         $F0
2EB5: C6 11      ADD         $11
2EB7: 6F         LD           L,A
2EB8: 7B         LD           A,E
2EB9: C6 02      ADD         $02
2EBB: 5F         LD           E,A
2EBC: E6 1F      AND         $1F
2EBE: FE 14      CP           $14
2EC0: 20 0A      JR           NZ,$2ECC
2EC2: 7B         LD           A,E
2EC3: E6 E0      AND         $E0
2EC5: C6 40      ADD         $40
2EC7: 5F         LD           E,A
2EC8: 7A         LD           A,D
2EC9: CE 00      ADC         $00
2ECB: 57         LD           D,A
2ECC: 0D         DEC         C
2ECD: 20 AA      JR           NZ,$2E79
2ECF: 3E 01      LD           A,$01
2ED1: EA 00 21   LD           ($2100),A
2ED4: C3 C1 7D   JP           $7DC1
2ED7: 3E 01      LD           A,$01
2ED9: E0 FF      LDFF00   ($FF),A
2EDB: 21 7F D4   LD           HL,$D47F
2EDE: 34         INC         (HL)
2EDF: 3E 09      LD           A,$09
2EE1: EA 00 21   LD           ($2100),A
2EE4: AF         XOR         A
2EE5: E0 E6      LDFF00   ($E6),A
2EE7: EA 9C C1   LD           ($C19C),A
2EEA: EA 04 C5   LD           ($C504),A
2EED: EA C8 DB   LD           ($DBC8),A
2EF0: EA C9 DB   LD           ($DBC9),A
2EF3: EA A2 C1   LD           ($C1A2),A
2EF6: EA C6 C1   LD           ($C1C6),A
2EF9: EA FA D6   LD           ($D6FA),A
2EFC: EA 0A C5   LD           ($C50A),A
2EFF: E0 AC      LDFF00   ($AC),A
2F01: EA 13 C1   LD           ($C113),A
2F04: EA 60 D4   LD           ($D460),A
2F07: EA BE C1   LD           ($C1BE),A
2F0A: EA 0E C5   LD           ($C50E),A
2F0D: EA C8 C3   LD           ($C3C8),A
2F10: EA A6 C5   LD           ($C5A6),A
2F13: EA 62 D4   LD           ($D462),A
2F16: EA CD C3   LD           ($C3CD),A
2F19: 3E FF      LD           A,$FF
2F1B: EA 01 D4   LD           ($D401),A
2F1E: EA 0F C5   LD           ($C50F),A
2F21: FA A5 DB   LD           A,($DBA5)
2F24: A7         AND         A
2F25: 28 69      JR           Z,$2F90
2F27: 3E 14      LD           A,$14
2F29: EA 00 21   LD           ($2100),A
2F2C: E0 E8      LDFF00   ($E8),A
2F2E: F0 F7      LD           A,($F7)
2F30: FE 0B      CP           $0B
2F32: 30 2B      JR           NC,$2F5F
2F34: 21 00 42   LD           HL,$4200
2F37: CB 37      SWAP       A
2F39: 5F         LD           E,A
2F3A: 16 00      LD           D,$00
2F3C: CB 23      SLA         E
2F3E: CB 12      RL           D
2F40: CB 23      SLA         E
2F42: CB 12      RL           D
2F44: 19         ADD         HL,DE
2F45: F0 F7      LD           A,($F7)
2F47: FE 06      CP           $06
2F49: 20 0A      JR           NZ,$2F55
2F4B: FA 6B DB   LD           A,($DB6B)
2F4E: E6 04      AND         $04
2F50: 28 03      JR           Z,$2F55
2F52: 21 C0 44   LD           HL,$44C0
2F55: FA AE DB   LD           A,($DBAE)
2F58: 5F         LD           E,A
2F59: 16 00      LD           D,$00
2F5B: 19         ADD         HL,DE
2F5C: 7E         LD           A,(HL)
2F5D: E0 F6      LDFF00   ($F6),A
2F5F: F0 F6      LD           A,($F6)
2F61: 4F         LD           C,A
2F62: 06 00      LD           B,$00
2F64: F0 F7      LD           A,($F7)
2F66: FE 1A      CP           $1A
2F68: 30 05      JR           NC,$2F6F
2F6A: FE 06      CP           $06
2F6C: 38 01      JR           C,$2F6F
2F6E: 04         INC         B
2F6F: 21 00 40   LD           HL,$4000
2F72: 09         ADD         HL,BC
2F73: 7E         LD           A,(HL)
2F74: EA 8E C1   LD           ($C18E),A
2F77: AF         XOR         A
2F78: EA 8A C1   LD           ($C18A),A
2F7B: EA 8B C1   LD           ($C18B),A
2F7E: EA 90 C1   LD           ($C190),A
2F81: EA 8F C1   LD           ($C18F),A
2F84: 5F         LD           E,A
2F85: 21 B5 DB   LD           HL,$DBB5
2F88: AF         XOR         A
2F89: 22         LD           (HLI),A
2F8A: 1C         INC         E
2F8B: 7B         LD           A,E
2F8C: FE 11      CP           $11
2F8E: 20 F8      JR           NZ,$2F88
2F90: F0 F6      LD           A,($F6)
2F92: 5F         LD           E,A
2F93: 16 00      LD           D,$00
2F95: 21 00 D8   LD           HL,$D800
2F98: FA A5 DB   LD           A,($DBA5)
2F9B: A7         AND         A
2F9C: 28 10      JR           Z,$2FAE
2F9E: 21 00 D9   LD           HL,$D900
2FA1: F0 F7      LD           A,($F7)
2FA3: FE 1A      CP           $1A
2FA5: 30 07      JR           NC,$2FAE
2FA7: FE 06      CP           $06
2FA9: 38 03      JR           C,$2FAE
2FAB: 21 00 DA   LD           HL,$DA00
2FAE: 19         ADD         HL,DE
2FAF: F0 F9      LD           A,($F9)
2FB1: A7         AND         A
2FB2: 7E         LD           A,(HL)
2FB3: 20 03      JR           NZ,$2FB8
2FB5: F6 80      OR           $80
2FB7: 77         LD           (HL),A
2FB8: E0 F8      LDFF00   ($F8),A
2FBA: F0 F6      LD           A,($F6)
2FBC: 4F         LD           C,A
2FBD: 06 00      LD           B,$00
2FBF: CB 21      SLA         C
2FC1: CB 10      RL           B
2FC3: FA A5 DB   LD           A,($DBA5)
2FC6: A7         AND         A
2FC7: 28 39      JR           Z,$3002
2FC9: 3E 0A      LD           A,$0A
2FCB: EA 00 21   LD           ($2100),A
2FCE: E0 E8      LDFF00   ($E8),A
2FD0: F0 F7      LD           A,($F7)
2FD2: FE 1F      CP           $1F
2FD4: 20 13      JR           NZ,$2FE9
2FD6: F0 F6      LD           A,($F6)
2FD8: FE F5      CP           $F5
2FDA: 20 0D      JR           NZ,$2FE9
2FDC: FA 0E DB   LD           A,($DB0E)
2FDF: FE 0E      CP           $0E
2FE1: 20 06      JR           NZ,$2FE9
2FE3: 01 53 78   LD           BC,$7853
2FE6: C3 7D 30   JP           $307D
2FE9: 21 00 40   LD           HL,$4000
2FEC: F0 F7      LD           A,($F7)
2FEE: FE 1A      CP           $1A
2FF0: 30 75      JR           NC,$3067
2FF2: FE 06      CP           $06
2FF4: 38 71      JR           C,$3067
2FF6: 3E 0B      LD           A,$0B
2FF8: EA 00 21   LD           ($2100),A
2FFB: E0 E8      LDFF00   ($E8),A
2FFD: 21 00 40   LD           HL,$4000
3000: 18 65      JR           $3067
3002: F0 F6      LD           A,($F6)
3004: FE 0E      CP           $0E
3006: 20 0C      JR           NZ,$3014
3008: FA 0E D8   LD           A,($D80E)
300B: E6 10      AND         $10
300D: 28 55      JR           Z,$3064
300F: 01 F0 47   LD           BC,$47F0
3012: 18 5E      JR           $3072
3014: FE 8C      CP           $8C
3016: 20 0C      JR           NZ,$3024
3018: FA 8C D8   LD           A,($D88C)
301B: E6 10      AND         $10
301D: 28 45      JR           Z,$3064
301F: 01 56 43   LD           BC,$4356
3022: 18 4E      JR           $3072
3024: FE 79      CP           $79
3026: 20 0C      JR           NZ,$3034
3028: FA 79 D8   LD           A,($D879)
302B: E6 10      AND         $10
302D: 28 35      JR           Z,$3064
302F: 01 FD 64   LD           BC,$64FD
3032: 18 3E      JR           $3072
3034: FE 06      CP           $06
3036: 20 0C      JR           NZ,$3044
3038: FA 06 D8   LD           A,($D806)
303B: E6 10      AND         $10
303D: 28 25      JR           Z,$3064
303F: 01 96 44   LD           BC,$4496
3042: 18 2E      JR           $3072
3044: FE 1B      CP           $1B
3046: 20 0C      JR           NZ,$3054
3048: FA 2B D8   LD           A,($D82B)
304B: E6 10      AND         $10
304D: 28 15      JR           Z,$3064
304F: 01 13 4C   LD           BC,$4C13
3052: 18 1E      JR           $3072
3054: FE 2B      CP           $2B
3056: 20 0C      JR           NZ,$3064
3058: FA 2B D8   LD           A,($D82B)
305B: E6 10      AND         $10
305D: 28 05      JR           Z,$3064
305F: 01 AC 50   LD           BC,$50AC
3062: 18 0E      JR           $3072
3064: 21 00 40   LD           HL,$4000
3067: 09         ADD         HL,BC
3068: 2A         LD           A,(HLI)
3069: 4F         LD           C,A
306A: 7E         LD           A,(HL)
306B: 47         LD           B,A
306C: FA A5 DB   LD           A,($DBA5)
306F: A7         AND         A
3070: 20 0B      JR           NZ,$307D
3072: F0 F6      LD           A,($F6)
3074: FE 80      CP           $80
3076: 38 05      JR           C,$307D
3078: 3E 1A      LD           A,$1A
307A: EA 00 21   LD           ($2100),A
307D: 0A         LD           A,(BC)
307E: FE FE      CP           $FE
3080: 28 4F      JR           Z,$30D1
3082: E0 A4      LDFF00   ($A4),A
3084: 03         INC         BC
3085: FA A5 DB   LD           A,($DBA5)
3088: A7         AND         A
3089: 28 10      JR           Z,$309B
308B: 0A         LD           A,(BC)
308C: E6 0F      AND         $0F
308E: CD CF 36   CALL       $36CF
3091: 0A         LD           A,(BC)
3092: CB 37      SWAP       A
3094: E6 0F      AND         $0F
3096: CD C9 37   CALL       $37C9
3099: 18 04      JR           $309F
309B: 0A         LD           A,(BC)
309C: CD CF 36   CALL       $36CF
309F: 03         INC         BC
30A0: 0A         LD           A,(BC)
30A1: E6 FC      AND         $FC
30A3: FE E0      CP           $E0
30A5: 20 20      JR           NZ,$30C7
30A7: F0 E6      LD           A,($E6)
30A9: 5F         LD           E,A
30AA: 16 00      LD           D,$00
30AC: 21 01 D4   LD           HL,$D401
30AF: 19         ADD         HL,DE
30B0: 0A         LD           A,(BC)
30B1: E6 03      AND         $03
30B3: 22         LD           (HLI),A
30B4: 03         INC         BC
30B5: 0A         LD           A,(BC)
30B6: 22         LD           (HLI),A
30B7: 03         INC         BC
30B8: 0A         LD           A,(BC)
30B9: 22         LD           (HLI),A
30BA: 03         INC         BC
30BB: 0A         LD           A,(BC)
30BC: 22         LD           (HLI),A
30BD: 03         INC         BC
30BE: 0A         LD           A,(BC)
30BF: 22         LD           (HLI),A
30C0: 7B         LD           A,E
30C1: C6 05      ADD         $05
30C3: E0 E6      LDFF00   ($E6),A
30C5: 18 D8      JR           $309F
30C7: 0A         LD           A,(BC)
30C8: FE FE      CP           $FE
30CA: 28 05      JR           Z,$30D1
30CC: CD DC 30   CALL       $30DC
30CF: 18 CE      JR           $309F
30D1: 3E 01      LD           A,$01
30D3: EA 00 21   LD           ($2100),A
30D6: CD DE 7C   CALL       $7CDE
30D9: C3 C0 07   JP           $07C0
30DC: AF         XOR         A
30DD: E0 D7      LDFF00   ($D7),A
30DF: 0A         LD           A,(BC)
30E0: CB 7F      BIT         7,A
30E2: 28 07      JR           Z,$30EB
30E4: CB 67      BIT         4,A
30E6: 20 03      JR           NZ,$30EB
30E8: E0 D7      LDFF00   ($D7),A
30EA: 03         INC         BC
30EB: 03         INC         BC
30EC: F0 F8      LD           A,($F8)
30EE: 5F         LD           E,A
30EF: FA A5 DB   LD           A,($DBA5)
30F2: A7         AND         A
30F3: 20 18      JR           NZ,$310D
30F5: 0A         LD           A,(BC)
30F6: D6 F5      SUB         $F5
30F8: 38 3E      JR           C,$3138
30FA: C7         RST         0X00
30FB: 38 33      JR           C,$3130
30FD: 25         DEC         H
30FE: 34         INC         (HL)
30FF: 45         LD           B,L
3100: 34         INC         (HL)
3101: EF         RST         0X28
3102: 33         INC         SP
3103: 5F         LD           E,A
3104: 34         INC         (HL)
3105: 79         LD           A,C
3106: 34         INC         (HL)
3107: 98         SBC         B
3108: 34         INC         (HL)
3109: C2 34 DC   JP           NZ,$DC34
310C: 34         INC         (HL)
310D: 0A         LD           A,(BC)
310E: D6 EC      SUB         $EC
3110: DA FD 31   JP           C,$31FD
3113: C7         RST         0X00
3114: EB                              
3115: 34         INC         (HL)
3116: 06 35      LD           B,$35
3118: 21 35 3C   LD           HL,$3C35
311B: 35         DEC         (HL)
311C: 55         LD           D,L
311D: 35         DEC         (HL)
311E: 68         LD           L,B
311F: 35         DEC         (HL)
3120: 7B         LD           A,E
3121: 35         DEC         (HL)
3122: 8E         ADC         A,(HL)
3123: 35         DEC         (HL)
3124: A3         AND         E
3125: 35         DEC         (HL)
3126: D2 35 E6   JP           NC,$E635
3129: 35         DEC         (HL)
312A: FA 35 0E   LD           A,($0E35)
312D: 36 46      LD           (HL),$46
312F: 36 55      LD           (HL),$55
3131: 36 64      LD           (HL),$64
3133: 36 8A      LD           (HL),$8A
3135: 36 9E      LD           (HL),$9E
3137: 36 C6      LD           (HL),$C6
3139: F5         PUSH       AF
313A: F5         PUSH       AF
313B: 57         LD           D,A
313C: FE E9      CP           $E9
313E: 20 03      JR           NZ,$3143
3140: EA 0E C5   LD           ($C50E),A
3143: FE 5E      CP           $5E
3145: 20 04      JR           NZ,$314B
3147: CB 6B      BIT         5,E
3149: 20 65      JR           NZ,$31B0
314B: FE 91      CP           $91
314D: 20 09      JR           NZ,$3158
314F: CB 6B      BIT         5,E
3151: 28 05      JR           Z,$3158
3153: F1         POP         AF
3154: 3E 5E      LD           A,$5E
3156: 57         LD           D,A
3157: F5         PUSH       AF
3158: FE DC      CP           $DC
315A: 20 09      JR           NZ,$3165
315C: CB 6B      BIT         5,E
315E: 28 05      JR           Z,$3165
3160: F1         POP         AF
3161: 3E 91      LD           A,$91
3163: 57         LD           D,A
3164: F5         PUSH       AF
3165: FE D8      CP           $D8
3167: 28 08      JR           Z,$3171
3169: FE D9      CP           $D9
316B: 28 04      JR           Z,$3171
316D: FE DA      CP           $DA
316F: 20 09      JR           NZ,$317A
3171: CB 63      BIT         4,E
3173: 28 05      JR           Z,$317A
3175: F1         POP         AF
3176: 3E DB      LD           A,$DB
3178: 57         LD           D,A
3179: F5         PUSH       AF
317A: FE C2      CP           $C2
317C: 20 09      JR           NZ,$3187
317E: CB 63      BIT         4,E
3180: 28 05      JR           Z,$3187
3182: F1         POP         AF
3183: 3E E3      LD           A,$E3
3185: 57         LD           D,A
3186: F5         PUSH       AF
3187: 7A         LD           A,D
3188: FE BA      CP           $BA
318A: 20 09      JR           NZ,$3195
318C: CB 53      BIT         2,E
318E: 28 05      JR           Z,$3195
3190: F1         POP         AF
3191: 3E E1      LD           A,$E1
3193: 57         LD           D,A
3194: F5         PUSH       AF
3195: 7A         LD           A,D
3196: FE D3      CP           $D3
3198: 20 1B      JR           NZ,$31B5
319A: CB 63      BIT         4,E
319C: 28 17      JR           Z,$31B5
319E: F0 F6      LD           A,($F6)
31A0: FE 75      CP           $75
31A2: 28 0C      JR           Z,$31B0
31A4: FE 07      CP           $07
31A6: 28 08      JR           Z,$31B0
31A8: FE AA      CP           $AA
31AA: 28 04      JR           Z,$31B0
31AC: FE 4A      CP           $4A
31AE: 20 05      JR           NZ,$31B5
31B0: F1         POP         AF
31B1: 3E C6      LD           A,$C6
31B3: 57         LD           D,A
31B4: F5         PUSH       AF
31B5: 7A         LD           A,D
31B6: E0 E0      LDFF00   ($E0),A
31B8: FE C2      CP           $C2
31BA: 28 20      JR           Z,$31DC
31BC: FE E1      CP           $E1
31BE: 28 1C      JR           Z,$31DC
31C0: FE CB      CP           $CB
31C2: 28 18      JR           Z,$31DC
31C4: FE BA      CP           $BA
31C6: 28 14      JR           Z,$31DC
31C8: FE 61      CP           $61
31CA: 28 10      JR           Z,$31DC
31CC: FE C6      CP           $C6
31CE: 28 0C      JR           Z,$31DC
31D0: FE C5      CP           $C5
31D2: 28 08      JR           Z,$31DC
31D4: FE E2      CP           $E2
31D6: 28 04      JR           Z,$31DC
31D8: FE E3      CP           $E3
31DA: 20 12      JR           NZ,$31EE
31DC: FA 9C C1   LD           A,($C19C)
31DF: 5F         LD           E,A
31E0: 3C         INC         A
31E1: EA 9C C1   LD           ($C19C),A
31E4: 16 00      LD           D,$00
31E6: 21 16 D4   LD           HL,$D416
31E9: 19         ADD         HL,DE
31EA: 0B         DEC         BC
31EB: 0A         LD           A,(BC)
31EC: 77         LD           (HL),A
31ED: 03         INC         BC
31EE: F0 E0      LD           A,($E0)
31F0: FE C5      CP           $C5
31F2: CA AA 32   JP           Z,$32AA
31F5: FE C6      CP           $C6
31F7: CA AA 32   JP           Z,$32AA
31FA: C3 FB 32   JP           $32FB
31FD: C6 EC      ADD         $EC
31FF: E0 E0      LDFF00   ($E0),A
3201: F5         PUSH       AF
3202: FE CF      CP           $CF
3204: 38 08      JR           C,$320E
3206: FE D3      CP           $D3
3208: 30 04      JR           NC,$320E
320A: 21 A5 C1   LD           HL,$C1A5
320D: 34         INC         (HL)
320E: FE AB      CP           $AB
3210: 20 22      JR           NZ,$3234
3212: AF         XOR         A
3213: EA CB C3   LD           ($C3CB),A
3216: F0 F6      LD           A,($F6)
3218: FE C4      CP           $C4
321A: F0 E0      LD           A,($E0)
321C: 28 16      JR           Z,$3234
321E: 21 C9 DB   LD           HL,$DBC9
3221: 34         INC         (HL)
3222: EA CB C3   LD           ($C3CB),A
3225: F5         PUSH       AF
3226: FA CD C3   LD           A,($C3CD)
3229: C6 04      ADD         $04
322B: EA CD C3   LD           ($C3CD),A
322E: 3E 04      LD           A,$04
3230: EA 6B C1   LD           ($C16B),A
3233: F1         POP         AF
3234: FE 8E      CP           $8E
3236: 28 13      JR           Z,$324B
3238: FE AA      CP           $AA
323A: 28 0F      JR           Z,$324B
323C: FE DC      CP           $DC
323E: 28 04      JR           Z,$3244
3240: FE DB      CP           $DB
3242: 20 0C      JR           NZ,$3250
3244: 21 FA D6   LD           HL,$D6FA
3247: 36 02      LD           (HL),$02
3249: 18 05      JR           $3250
324B: 21 FA D6   LD           HL,$D6FA
324E: 36 01      LD           (HL),$01
3250: FE 3F      CP           $3F
3252: 28 04      JR           Z,$3258
3254: FE 47      CP           $47
3256: 20 04      JR           NZ,$325C
3258: CB 53      BIT         2,E
325A: 20 0C      JR           NZ,$3268
325C: FE 40      CP           $40
325E: 28 04      JR           Z,$3264
3260: FE 48      CP           $48
3262: 20 08      JR           NZ,$326C
3264: CB 5B      BIT         3,E
3266: 28 04      JR           Z,$326C
3268: F1         POP         AF
3269: 3E 3D      LD           A,$3D
326B: F5         PUSH       AF
326C: FE 41      CP           $41
326E: 28 04      JR           Z,$3274
3270: FE 49      CP           $49
3272: 20 04      JR           NZ,$3278
3274: CB 4B      BIT         1,E
3276: 20 0C      JR           NZ,$3284
3278: FE 42      CP           $42
327A: 28 04      JR           Z,$3280
327C: FE 4A      CP           $4A
327E: 20 08      JR           NZ,$3288
3280: CB 43      BIT         0,E
3282: 28 04      JR           Z,$3288
3284: F1         POP         AF
3285: 3E 3E      LD           A,$3E
3287: F5         PUSH       AF
3288: FE A1      CP           $A1
328A: 20 08      JR           NZ,$3294
328C: CB 63      BIT         4,E
328E: 20 04      JR           NZ,$3294
3290: F1         POP         AF
3291: F0 E9      LD           A,($E9)
3293: F5         PUSH       AF
3294: FE BF      CP           $BF
3296: 20 06      JR           NZ,$329E
3298: CB 63      BIT         4,E
329A: 20 02      JR           NZ,$329E
329C: F1         POP         AF
329D: C9         RET
329E: FE BE      CP           $BE
32A0: 28 08      JR           Z,$32AA
32A2: FE BF      CP           $BF
32A4: 28 04      JR           Z,$32AA
32A6: FE CB      CP           $CB
32A8: 20 19      JR           NZ,$32C3
32AA: 0B         DEC         BC
32AB: 3E 01      LD           A,$01
32AD: E0 AC      LDFF00   ($AC),A
32AF: 0A         LD           A,(BC)
32B0: E6 F0      AND         $F0
32B2: C6 10      ADD         $10
32B4: E0 AE      LDFF00   ($AE),A
32B6: 0A         LD           A,(BC)
32B7: CB 37      SWAP       A
32B9: E6 F0      AND         $F0
32BB: C6 08      ADD         $08
32BD: E0 AD      LDFF00   ($AD),A
32BF: 03         INC         BC
32C0: C3 FB 32   JP           $32FB
32C3: FE D6      CP           $D6
32C5: 28 04      JR           Z,$32CB
32C7: FE D5      CP           $D5
32C9: 20 08      JR           NZ,$32D3
32CB: CB 63      BIT         4,E
32CD: 20 04      JR           NZ,$32D3
32CF: F1         POP         AF
32D0: 3E 21      LD           A,$21
32D2: F5         PUSH       AF
32D3: FE D7      CP           $D7
32D5: 28 04      JR           Z,$32DB
32D7: FE D8      CP           $D8
32D9: 20 08      JR           NZ,$32E3
32DB: CB 63      BIT         4,E
32DD: 20 04      JR           NZ,$32E3
32DF: F1         POP         AF
32E0: 3E 22      LD           A,$22
32E2: F5         PUSH       AF
32E3: F0 F7      LD           A,($F7)
32E5: FE 0A      CP           $0A
32E7: F0 E0      LD           A,($E0)
32E9: 38 04      JR           C,$32EF
32EB: FE A9      CP           $A9
32ED: 28 04      JR           Z,$32F3
32EF: FE DE      CP           $DE
32F1: 20 08      JR           NZ,$32FB
32F3: CB 73      BIT         6,E
32F5: 28 04      JR           Z,$32FB
32F7: F1         POP         AF
32F8: 3E 0D      LD           A,$0D
32FA: F5         PUSH       AF
32FB: FE A0      CP           $A0
32FD: 20 08      JR           NZ,$3307
32FF: CB 63      BIT         4,E
3301: 28 04      JR           Z,$3307
3303: F1         POP         AF
3304: 3E A1      LD           A,$A1
3306: F5         PUSH       AF
3307: 16 00      LD           D,$00
3309: F0 D7      LD           A,($D7)
330B: A7         AND         A
330C: 28 1F      JR           Z,$332D
330E: 0B         DEC         BC
330F: 0A         LD           A,(BC)
3310: 5F         LD           E,A
3311: 21 11 D7   LD           HL,$D711
3314: 19         ADD         HL,DE
3315: F0 D7      LD           A,($D7)
3317: E6 0F      AND         $0F
3319: 5F         LD           E,A
331A: F1         POP         AF
331B: 57         LD           D,A
331C: 7A         LD           A,D
331D: 22         LD           (HLI),A
331E: F0 D7      LD           A,($D7)
3320: E6 40      AND         $40
3322: 28 04      JR           Z,$3328
3324: 7D         LD           A,L
3325: C6 0F      ADD         $0F
3327: 6F         LD           L,A
3328: 1D         DEC         E
3329: 20 F1      JR           NZ,$331C
332B: 03         INC         BC
332C: C9         RET
332D: 0B         DEC         BC
332E: 0A         LD           A,(BC)
332F: 5F         LD           E,A
3330: 21 11 D7   LD           HL,$D711
3333: 19         ADD         HL,DE
3334: F1         POP         AF
3335: 77         LD           (HL),A
3336: 03         INC         BC
3337: C9         RET
3338: 0B         DEC         BC
3339: 0A         LD           A,(BC)
333A: C6 11      ADD         $11
333C: 5F         LD           E,A
333D: E6 0F      AND         $0F
333F: 20 04      JR           NZ,$3345
3341: 7B         LD           A,E
3342: D6 10      SUB         $10
3344: 5F         LD           E,A
3345: 16 00      LD           D,$00
3347: 21 00 D7   LD           HL,$D700
334A: 19         ADD         HL,DE
334B: F0 D7      LD           A,($D7)
334D: A7         AND         A
334E: 28 19      JR           Z,$3369
3350: E6 0F      AND         $0F
3352: 5F         LD           E,A
3353: CD 69 33   CALL       $3369
3356: 0B         DEC         BC
3357: F0 D7      LD           A,($D7)
3359: E6 40      AND         $40
335B: 16 F1      LD           D,$F1
335D: 28 02      JR           Z,$3361
335F: 16 0F      LD           D,$0F
3361: 7D         LD           A,L
3362: 82         ADD         A,D
3363: 6F         LD           L,A
3364: 1D         DEC         E
3365: 20 EC      JR           NZ,$3353
3367: 03         INC         BC
3368: C9         RET
3369: 7E         LD           A,(HL)
336A: FE 10      CP           $10
336C: 3E 25      LD           A,$25
336E: 38 02      JR           C,$3372
3370: C6 04      ADD         $04
3372: 22         LD           (HLI),A
3373: 7E         LD           A,(HL)
3374: FE 10      CP           $10
3376: 3E 26      LD           A,$26
3378: 38 02      JR           C,$337C
337A: C6 04      ADD         $04
337C: 32         LD           (HLD),A
337D: 7D         LD           A,L
337E: C6 10      ADD         $10
3380: 6F         LD           L,A
3381: 7E         LD           A,(HL)
3382: FE 8A      CP           $8A
3384: 30 0A      JR           NC,$3390
3386: FE 10      CP           $10
3388: 3E 27      LD           A,$27
338A: 38 06      JR           C,$3392
338C: 3E 2A      LD           A,$2A
338E: 18 02      JR           $3392
3390: 3E 82      LD           A,$82
3392: 22         LD           (HLI),A
3393: 7E         LD           A,(HL)
3394: FE 8A      CP           $8A
3396: 30 0A      JR           NC,$33A2
3398: FE 10      CP           $10
339A: 3E 28      LD           A,$28
339C: 38 06      JR           C,$33A4
339E: 3E 29      LD           A,$29
33A0: 18 02      JR           $33A4
33A2: 3E 83      LD           A,$83
33A4: 77         LD           (HL),A
33A5: 03         INC         BC
33A6: C9         RET
33A7: E5         PUSH       HL
33A8: D5         PUSH       DE
33A9: 0A         LD           A,(BC)
33AA: 5F         LD           E,A
33AB: 16 00      LD           D,$00
33AD: 19         ADD         HL,DE
33AE: D1         POP         DE
33AF: 1A         LD           A,(DE)
33B0: FE E1      CP           $E1
33B2: 28 08      JR           Z,$33BC
33B4: FE E2      CP           $E2
33B6: 28 04      JR           Z,$33BC
33B8: FE E3      CP           $E3
33BA: 20 1A      JR           NZ,$33D6
33BC: F5         PUSH       AF
33BD: E5         PUSH       HL
33BE: D5         PUSH       DE
33BF: 7D         LD           A,L
33C0: D6 11      SUB         $11
33C2: F5         PUSH       AF
33C3: FA 9C C1   LD           A,($C19C)
33C6: 5F         LD           E,A
33C7: 3C         INC         A
33C8: EA 9C C1   LD           ($C19C),A
33CB: 16 00      LD           D,$00
33CD: 21 16 D4   LD           HL,$D416
33D0: 19         ADD         HL,DE
33D1: F1         POP         AF
33D2: 77         LD           (HL),A
33D3: D1         POP         DE
33D4: E1         POP         HL
33D5: F1         POP         AF
33D6: 77         LD           (HL),A
33D7: 13         INC         DE
33D8: 03         INC         BC
33D9: E1         POP         HL
33DA: 0A         LD           A,(BC)
33DB: A7         AND         A
33DC: FE FF      CP           $FF
33DE: 20 C7      JR           NZ,$33A7
33E0: C1         POP         BC
33E1: C9         RET
33E2: 00         NOP
33E3: 01 02 10   LD           BC,$1002
33E6: 11 12 FF   LD           DE,$FF12
33E9: B6         OR           (HL)
33EA: B7         OR           A
33EB: 66         LD           H,(HL)
33EC: 67         LD           H,A
33ED: E3                              
33EE: 68         LD           L,B
33EF: C5         PUSH       BC
33F0: CD FC 33   CALL       $33FC
33F3: 01 E2 33   LD           BC,$33E2
33F6: 11 E9 33   LD           DE,$33E9
33F9: C3 A7 33   JP           $33A7
33FC: 0B         DEC         BC
33FD: 0A         LD           A,(BC)
33FE: 5F         LD           E,A
33FF: 16 00      LD           D,$00
3401: 21 11 D7   LD           HL,$D711
3404: 19         ADD         HL,DE
3405: C9         RET
3406: 00         NOP
3407: 01 02 03   LD           BC,$0302
340A: 04         INC         B
340B: 10 11      STOP       $11
340D: 12         LD           (DE),A
340E: 13         INC         DE
340F: 14         INC         D
3410: 20 21      JR           NZ,$3433
3412: 22         LD           (HLI),A
3413: 23         INC         HL
3414: 24         INC         H
3415: FF         RST         0X38
3416: 55         LD           D,L
3417: 5A         LD           E,D
3418: 5A         LD           E,D
3419: 5A         LD           E,D
341A: 56         LD           D,(HL)
341B: 57         LD           D,A
341C: 59         LD           E,C
341D: 59         LD           E,C
341E: 59         LD           E,C
341F: 58         LD           E,B
3420: 5B         LD           E,E
3421: E2         LDFF00   (C),A
3422: 5B         LD           E,E
3423: E2         LDFF00   (C),A
3424: 5B         LD           E,E
3425: C5         PUSH       BC
3426: CD FC 33   CALL       $33FC
3429: 01 06 34   LD           BC,$3406
342C: 11 16 34   LD           DE,$3416
342F: C3 A7 33   JP           $33A7
3432: 00         NOP
3433: 01 02 10   LD           BC,$1002
3436: 11 12 20   LD           DE,$2012
3439: 21 22 FF   LD           HL,$FF22
343C: 55         LD           D,L
343D: 5A         LD           E,D
343E: 56         LD           D,(HL)
343F: 57         LD           D,A
3440: 59         LD           E,C
3441: 58         LD           E,B
3442: 5B         LD           E,E
3443: E2         LDFF00   (C),A
3444: 5B         LD           E,E
3445: C5         PUSH       BC
3446: CD FC 33   CALL       $33FC
3449: 01 32 34   LD           BC,$3432
344C: 11 3C 34   LD           DE,$343C
344F: C3 A7 33   JP           $33A7
3452: 00         NOP
3453: 01 02 10   LD           BC,$1002
3456: 11 12 FF   LD           DE,$FF12
3459: A4         AND         H
345A: A5         AND         L
345B: A6         AND         (HL)
345C: A7         AND         A
345D: E3                              
345E: A8         XOR         B
345F: C5         PUSH       BC
3460: CD FC 33   CALL       $33FC
3463: 01 52 34   LD           BC,$3452
3466: 11 59 34   LD           DE,$3459
3469: C3 A7 33   JP           $33A7
346C: 00         NOP
346D: 01 10 11   LD           BC,$1110
3470: FF         RST         0X38
3471: BB         CP           E
3472: BC         CP           H
3473: BD         CP           L
3474: BE         CP           (HL)
3475: 09         ADD         HL,BC
3476: 09         ADD         HL,BC
3477: 09         ADD         HL,BC
3478: 09         ADD         HL,BC
3479: C5         PUSH       BC
347A: CD FC 33   CALL       $33FC
347D: 01 6C 34   LD           BC,$346C
3480: 11 71 34   LD           DE,$3471
3483: F0 F8      LD           A,($F8)
3485: E6 04      AND         $04
3487: 28 03      JR           Z,$348C
3489: 11 75 34   LD           DE,$3475
348C: C3 A7 33   JP           $33A7
348F: 00         NOP
3490: 01 10 11   LD           BC,$1110
3493: FF         RST         0X38
3494: B6         OR           (HL)
3495: B7         OR           A
3496: CD CE C5   CALL       $C5CE
3499: CD FC 33   CALL       $33FC
349C: 01 8F 34   LD           BC,$348F
349F: 11 94 34   LD           DE,$3494
34A2: C3 A7 33   JP           $33A7
34A5: 00         NOP
34A6: 01 02 10   LD           BC,$1002
34A9: 11 12 1F   LD           DE,$1F12
34AC: 20 21      JR           NZ,$34CF
34AE: 22         LD           (HLI),A
34AF: 23         INC         HL
34B0: 30 31      JR           NC,$34E3
34B2: 32         LD           (HLD),A
34B3: FF         RST         0X38
34B4: 2B         DEC         HL
34B5: 2C         INC         L
34B6: 2D         DEC         L
34B7: 37         SCF
34B8: E8 38      ADD         SP,$38
34BA: 0A         LD           A,(BC)
34BB: 33         INC         SP
34BC: 2F         CPL
34BD: 34         INC         (HL)
34BE: 0A         LD           A,(BC)
34BF: 0A         LD           A,(BC)
34C0: 0A         LD           A,(BC)
34C1: 0A         LD           A,(BC)
34C2: C5         PUSH       BC
34C3: CD FC 33   CALL       $33FC
34C6: 01 A5 34   LD           BC,$34A5
34C9: 11 B4 34   LD           DE,$34B4
34CC: C3 A7 33   JP           $33A7
34CF: 00         NOP
34D0: 01 02 10   LD           BC,$1002
34D3: 11 12 FF   LD           DE,$FF12
34D6: 52         LD           D,D
34D7: 52         LD           D,D
34D8: 52         LD           D,D
34D9: 5B         LD           E,E
34DA: E2         LDFF00   (C),A
34DB: 5B         LD           E,E
34DC: C5         PUSH       BC
34DD: CD FC 33   CALL       $33FC
34E0: 01 CF 34   LD           BC,$34CF
34E3: 11 D6 34   LD           DE,$34D6
34E6: C3 A7 33   JP           $33A7
34E9: 2D         DEC         L
34EA: 2E 1E      LD           L,$1E
34EC: 00         NOP
34ED: CD 27 36   CALL       $3627
34F0: F0 F8      LD           A,($F8)
34F2: E6 04      AND         $04
34F4: C2 A3 35   JP           NZ,$35A3
34F7: C5         PUSH       BC
34F8: CD FC 33   CALL       $33FC
34FB: 01 C9 36   LD           BC,$36C9
34FE: 11 E9 34   LD           DE,$34E9
3501: C3 A7 33   JP           $33A7
3504: 2F         CPL
3505: 30 1E      JR           NC,$3525
3507: 01 CD 27   LD           BC,$27CD
350A: 36 F0      LD           (HL),$F0
350C: F8 E6      LDHL       SP,$E6
350E: 08 C2 D2   LD           ($D2C2),SP
3511: 35         DEC         (HL)
3512: C5         PUSH       BC
3513: CD FC 33   CALL       $33FC
3516: 01 C9 36   LD           BC,$36C9
3519: 11 04 35   LD           DE,$3504
351C: C3 A7 33   JP           $33A7
351F: 31 32 1E   LD           SP,$1E32
3522: 02         LD           (BC),A
3523: CD 27 36   CALL       $3627
3526: F0 F8      LD           A,($F8)
3528: E6 02      AND         $02
352A: C2 E6 35   JP           NZ,$35E6
352D: C5         PUSH       BC
352E: CD FC 33   CALL       $33FC
3531: 01 CC 36   LD           BC,$36CC
3534: 11 1F 35   LD           DE,$351F
3537: C3 A7 33   JP           $33A7
353A: 33         INC         SP
353B: 34         INC         (HL)
353C: 1E 03      LD           E,$03
353E: CD 27 36   CALL       $3627
3541: F0 F8      LD           A,($F8)
3543: E6 01      AND         $01
3545: C2 FA 35   JP           NZ,$35FA
3548: C5         PUSH       BC
3549: CD FC 33   CALL       $33FC
354C: 01 CC 36   LD           BC,$36CC
354F: 11 3A 35   LD           DE,$353A
3552: C3 A7 33   JP           $33A7
3555: 1E 04      LD           E,$04
3557: CD 27 36   CALL       $3627
355A: FA 8A C1   LD           A,($C18A)
355D: F6 01      OR           $01
355F: EA 8A C1   LD           ($C18A),A
3562: EA 8B C1   LD           ($C18B),A
3565: C3 A3 35   JP           $35A3
3568: 1E 05      LD           E,$05
356A: CD 27 36   CALL       $3627
356D: FA 8A C1   LD           A,($C18A)
3570: F6 02      OR           $02
3572: EA 8A C1   LD           ($C18A),A
3575: EA 8B C1   LD           ($C18B),A
3578: C3 D2 35   JP           $35D2
357B: 1E 06      LD           E,$06
357D: CD 27 36   CALL       $3627
3580: FA 8A C1   LD           A,($C18A)
3583: F6 04      OR           $04
3585: EA 8A C1   LD           ($C18A),A
3588: EA 8B C1   LD           ($C18B),A
358B: C3 E6 35   JP           $35E6
358E: 1E 07      LD           E,$07
3590: CD 27 36   CALL       $3627
3593: FA 8A C1   LD           A,($C18A)
3596: F6 08      OR           $08
3598: EA 8A C1   LD           ($C18A),A
359B: EA 8B C1   LD           ($C18B),A
359E: C3 FA 35   JP           $35FA
35A1: 43         LD           B,E
35A2: 44         LD           B,H
35A3: 3E 04      LD           A,$04
35A5: CD B5 35   CALL       $35B5
35A8: C5         PUSH       BC
35A9: CD FC 33   CALL       $33FC
35AC: 01 C9 36   LD           BC,$36C9
35AF: 11 A1 35   LD           DE,$35A1
35B2: C3 A7 33   JP           $33A7
35B5: F5         PUSH       AF
35B6: F0 F6      LD           A,($F6)
35B8: 5F         LD           E,A
35B9: 16 00      LD           D,$00
35BB: F0 F7      LD           A,($F7)
35BD: FE 1A      CP           $1A
35BF: 30 05      JR           NC,$35C6
35C1: FE 06      CP           $06
35C3: 38 01      JR           C,$35C6
35C5: 14         INC         D
35C6: 21 00 D9   LD           HL,$D900
35C9: 19         ADD         HL,DE
35CA: F1         POP         AF
35CB: B6         OR           (HL)
35CC: 77         LD           (HL),A
35CD: E0 F8      LDFF00   ($F8),A
35CF: C9         RET
35D0: 8C         ADC         A,H
35D1: 08 3E 08   LD           ($083E),SP
35D4: CD B5 35   CALL       $35B5
35D7: C5         PUSH       BC
35D8: CD FC 33   CALL       $33FC
35DB: 01 C9 36   LD           BC,$36C9
35DE: 11 D0 35   LD           DE,$35D0
35E1: C3 A7 33   JP           $33A7
35E4: 09         ADD         HL,BC
35E5: 0A         LD           A,(BC)
35E6: 3E 02      LD           A,$02
35E8: CD B5 35   CALL       $35B5
35EB: C5         PUSH       BC
35EC: CD FC 33   CALL       $33FC
35EF: 01 CC 36   LD           BC,$36CC
35F2: 11 E4 35   LD           DE,$35E4
35F5: C3 A7 33   JP           $33A7
35F8: 0B         DEC         BC
35F9: 0C         INC         C
35FA: 3E 01      LD           A,$01
35FC: CD B5 35   CALL       $35B5
35FF: C5         PUSH       BC
3600: CD FC 33   CALL       $33FC
3603: 01 CC 36   LD           BC,$36CC
3606: 11 F8 35   LD           DE,$35F8
3609: C3 A7 33   JP           $33A7
360C: A4         AND         H
360D: A5         AND         L
360E: 1E 08      LD           E,$08
3610: CD 27 36   CALL       $3627
3613: F0 F8      LD           A,($F8)
3615: E6 04      AND         $04
3617: C2 A3 35   JP           NZ,$35A3
361A: C5         PUSH       BC
361B: CD FC 33   CALL       $33FC
361E: 01 C9 36   LD           BC,$36C9
3621: 11 0C 36   LD           DE,$360C
3624: C3 A7 33   JP           $33A7
3627: 16 00      LD           D,$00
3629: 21 F0 C1   LD           HL,$C1F0
362C: 19         ADD         HL,DE
362D: 0B         DEC         BC
362E: 0A         LD           A,(BC)
362F: 77         LD           (HL),A
3630: F5         PUSH       AF
3631: E6 F0      AND         $F0
3633: 21 E0 C1   LD           HL,$C1E0
3636: 19         ADD         HL,DE
3637: 77         LD           (HL),A
3638: F1         POP         AF
3639: CB 37      SWAP       A
363B: E6 F0      AND         $F0
363D: 21 D0 C1   LD           HL,$C1D0
3640: 19         ADD         HL,DE
3641: 77         LD           (HL),A
3642: 03         INC         BC
3643: C9         RET
3644: AF         XOR         A
3645: B0         OR           B
3646: C5         PUSH       BC
3647: CD FC 33   CALL       $33FC
364A: 01 CC 36   LD           BC,$36CC
364D: 11 44 36   LD           DE,$3644
3650: C3 A7 33   JP           $33A7
3653: B1         OR           C
3654: B2         OR           D
3655: C5         PUSH       BC
3656: CD FC 33   CALL       $33FC
3659: 01 C9 36   LD           BC,$36C9
365C: 11 53 36   LD           DE,$3653
365F: C3 A7 33   JP           $33A7
3662: 45         LD           B,L
3663: 46         LD           B,(HL)
3664: C5         PUSH       BC
3665: CD FC 33   CALL       $33FC
3668: 01 C9 36   LD           BC,$36C9
366B: 11 62 36   LD           DE,$3662
366E: C3 A7 33   JP           $33A7
3671: 00         NOP
3672: 01 02 03   LD           BC,$0302
3675: 10 11      STOP       $11
3677: 12         LD           (DE),A
3678: 13         INC         DE
3679: 20 21      JR           NZ,$369C
367B: 22         LD           (HLI),A
367C: 23         INC         HL
367D: FF         RST         0X38
367E: B3         OR           E
367F: B4         OR           H
3680: B4         OR           H
3681: B5         OR           L
3682: B6         OR           (HL)
3683: B7         OR           A
3684: B8         CP           B
3685: B9         CP           C
3686: BA         CP           D
3687: BB         CP           E
3688: BC         CP           H
3689: BD         CP           L
368A: 3E 08      LD           A,$08
368C: CD B5 35   CALL       $35B5
368F: C5         PUSH       BC
3690: CD FC 33   CALL       $33FC
3693: 01 71 36   LD           BC,$3671
3696: 11 7E 36   LD           DE,$367E
3699: C3 A7 33   JP           $33A7
369C: C1         POP         BC
369D: C2 F0 F7   JP           NZ,$F7F0
36A0: FE 1A      CP           $1A
36A2: 30 13      JR           NC,$36B7
36A4: FE 06      CP           $06
36A6: 38 0F      JR           C,$36B7
36A8: F0 F6      LD           A,($F6)
36AA: FE D3      CP           $D3
36AC: 20 09      JR           NZ,$36B7
36AE: FA 46 DB   LD           A,($DB46)
36B1: A7         AND         A
36B2: 28 03      JR           Z,$36B7
36B4: C3 68 35   JP           $3568
36B7: 3E 01      LD           A,$01
36B9: CD B5 35   CALL       $35B5
36BC: C5         PUSH       BC
36BD: CD FC 33   CALL       $33FC
36C0: 01 C9 36   LD           BC,$36C9
36C3: 11 9C 36   LD           DE,$369C
36C6: C3 A7 33   JP           $33A7
36C9: 00         NOP
36CA: 01 FF 00   LD           BC,$00FF
36CD: 10 FF      STOP       $FF
36CF: E0 E9      LDFF00   ($E9),A
36D1: 16 80      LD           D,$80
36D3: 21 11 D7   LD           HL,$D711
36D6: 5F         LD           E,A
36D7: 7D         LD           A,L
36D8: E6 0F      AND         $0F
36DA: 28 05      JR           Z,$36E1
36DC: FE 0B      CP           $0B
36DE: 30 01      JR           NC,$36E1
36E0: 73         LD           (HL),E
36E1: 23         INC         HL
36E2: 15         DEC         D
36E3: 20 F2      JR           NZ,$36D7
36E5: C9         RET
36E6: 3E 01      LD           A,$01
36E8: EA 00 21   LD           ($2100),A
36EB: CD 61 5C   CALL       $5C61
36EE: 3E 16      LD           A,$16
36F0: EA 00 21   LD           ($2100),A
36F3: AF         XOR         A
36F4: E0 E4      LDFF00   ($E4),A
36F6: F0 F6      LD           A,($F6)
36F8: 4F         LD           C,A
36F9: 06 00      LD           B,$00
36FB: CB 21      SLA         C
36FD: CB 10      RL           B
36FF: 21 00 40   LD           HL,$4000
3702: FA A5 DB   LD           A,($DBA5)
3705: A7         AND         A
3706: 28 3F      JR           Z,$3747
3708: F0 F7      LD           A,($F7)
370A: FE 06      CP           $06
370C: 20 2A      JR           NZ,$3738
370E: FA 6F DB   LD           A,($DB6F)
3711: 21 F6 FF   LD           HL,$FFF6
3714: BE         CP           (HL)
3715: 20 21      JR           NZ,$3738
3717: 3E A8      LD           A,$A8
3719: CD 01 3C   CALL       $3C01
371C: FA 70 DB   LD           A,($DB70)
371F: 21 00 C2   LD           HL,$C200
3722: 19         ADD         HL,DE
3723: 77         LD           (HL),A
3724: FA 71 DB   LD           A,($DB71)
3727: 21 10 C2   LD           HL,$C210
372A: 19         ADD         HL,DE
372B: 77         LD           (HL),A
372C: CD B3 37   CALL       $37B3
372F: 21 60 C4   LD           HL,$C460
3732: 19         ADD         HL,DE
3733: 36 FF      LD           (HL),$FF
3735: AF         XOR         A
3736: E0 E4      LDFF00   ($E4),A
3738: 21 00 42   LD           HL,$4200
373B: F0 F7      LD           A,($F7)
373D: FE 1A      CP           $1A
373F: 30 06      JR           NC,$3747
3741: FE 06      CP           $06
3743: 38 02      JR           C,$3747
3745: 24         INC         H
3746: 24         INC         H
3747: 09         ADD         HL,BC
3748: 2A         LD           A,(HLI)
3749: 4F         LD           C,A
374A: 7E         LD           A,(HL)
374B: 47         LD           B,A
374C: 0A         LD           A,(BC)
374D: FE FF      CP           $FF
374F: 28 05      JR           Z,$3756
3751: CD 62 37   CALL       $3762
3754: 18 F6      JR           $374C
3756: CD C0 07   CALL       $07C0
3759: C9         RET
375A: 01 02 04   LD           BC,$0402
375D: 08 10 20   LD           ($2010),SP
3760: 40         LD           B,B
3761: 80         ADD         A,B
3762: F0 E4      LD           A,($E4)
3764: FE 08      CP           $08
3766: 30 12      JR           NC,$377A
3768: 5F         LD           E,A
3769: 16 00      LD           D,$00
376B: 21 5A 37   LD           HL,$375A
376E: 19         ADD         HL,DE
376F: F0 F6      LD           A,($F6)
3771: 5F         LD           E,A
3772: 7E         LD           A,(HL)
3773: 21 00 CF   LD           HL,$CF00
3776: 19         ADD         HL,DE
3777: A6         AND         (HL)
3778: 20 12      JR           NZ,$378C
377A: 1E 00      LD           E,$00
377C: 53         LD           D,E
377D: 21 80 C2   LD           HL,$C280
3780: 19         ADD         HL,DE
3781: 7E         LD           A,(HL)
3782: FE 00      CP           $00
3784: 28 0D      JR           Z,$3793
3786: 1C         INC         E
3787: 7B         LD           A,E
3788: FE 10      CP           $10
378A: 20 F1      JR           NZ,$377D
378C: 21 E4 FF   LD           HL,$FFE4
378F: 34         INC         (HL)
3790: 03         INC         BC
3791: 03         INC         BC
3792: C9         RET
3793: 36 04      LD           (HL),$04
3795: 0A         LD           A,(BC)
3796: E6 F0      AND         $F0
3798: 21 10 C2   LD           HL,$C210
379B: 19         ADD         HL,DE
379C: C6 10      ADD         $10
379E: 77         LD           (HL),A
379F: 0A         LD           A,(BC)
37A0: 03         INC         BC
37A1: CB 37      SWAP       A
37A3: E6 F0      AND         $F0
37A5: 21 00 C2   LD           HL,$C200
37A8: 19         ADD         HL,DE
37A9: C6 08      ADD         $08
37AB: 77         LD           (HL),A
37AC: 21 A0 C3   LD           HL,$C3A0
37AF: 19         ADD         HL,DE
37B0: 0A         LD           A,(BC)
37B1: 03         INC         BC
37B2: 77         LD           (HL),A
37B3: 3E 03      LD           A,$03
37B5: EA 00 21   LD           ($2100),A
37B8: CD 52 65   CALL       $6552
37BB: 3E 01      LD           A,$01
37BD: EA 00 21   LD           ($2100),A
37C0: CD 0A 5C   CALL       $5C0A
37C3: 3E 16      LD           A,$16
37C5: EA 00 21   LD           ($2100),A
37C8: C9         RET
37C9: 5F         LD           E,A
37CA: 3E 14      LD           A,$14
37CC: EA 00 21   LD           ($2100),A
37CF: 7B         LD           A,E
37D0: C5         PUSH       BC
37D1: CD 00 50   CALL       $5000
37D4: C1         POP         BC
37D5: F0 E8      LD           A,($E8)
37D7: EA 00 21   LD           ($2100),A
37DA: C9         RET
37DB: 3E 01      LD           A,$01
37DD: EA 00 21   LD           ($2100),A
37E0: CD E8 7E   CALL       $7EE8
37E3: C9         RET
37E4: FF         RST         0X38
37E5: FF         RST         0X38
37E6: 3E 14      LD           A,$14
37E8: EA 00 21   LD           ($2100),A
37EB: 21 FF 56   LD           HL,$56FF
37EE: 19         ADD         HL,DE
37EF: 7E         LD           A,(HL)
37F0: 21 00 21   LD           HL,$2100
37F3: 36 05      LD           (HL),$05
37F5: C9         RET
37F6: 3E 19      LD           A,$19
37F8: CD B9 07   CALL       $07B9
37FB: CD C2 77   CALL       $77C2
37FE: 3E 03      LD           A,$03
3800: C3 B9 07   JP           $07B9
3803: 3E 03      LD           A,$03
3805: EA 00 21   LD           ($2100),A
3808: CD 41 54   CALL       $5441
380B: C3 C0 07   JP           $07C0
380E: 3E 14      LD           A,$14
3810: EA 00 21   LD           ($2100),A
3813: CD 64 59   CALL       $5964
3816: C3 C0 07   JP           $07C0
3819: 3E 01      LD           A,$01
381B: CD B9 07   CALL       $07B9
381E: CD 6B 5D   CALL       $5D6B
3821: 3E 02      LD           A,$02
3823: C3 B9 07   JP           $07B9
3826: 3E 03      LD           A,$03
3828: EA 00 21   LD           ($2100),A
382B: CD B0 48   CALL       $48B0
382E: C3 C0 07   JP           $07C0
3831: 3E 14      LD           A,$14
3833: EA 00 21   LD           ($2100),A
3836: CD 22 58   CALL       $5822
3839: 3E 03      LD           A,$03
383B: EA 00 21   LD           ($2100),A
383E: C9         RET
383F: 00         NOP
3840: 08 10 18   LD           ($1810),SP
3843: 21 A7 C5   LD           HL,$C5A7
3846: 7E         LD           A,(HL)
3847: A7         AND         A
3848: 28 07      JR           Z,$3851
384A: 35         DEC         (HL)
384B: 20 04      JR           NZ,$3851
384D: 3E 10      LD           A,$10
384F: E0 F3      LDFF00   ($F3),A
3851: FA 9F C1   LD           A,($C19F)
3854: A7         AND         A
3855: 20 0D      JR           NZ,$3864
3857: FA 11 C1   LD           A,($C111)
385A: EA A8 C1   LD           ($C1A8),A
385D: A7         AND         A
385E: 28 04      JR           Z,$3864
3860: 3D         DEC         A
3861: EA 11 C1   LD           ($C111),A
3864: FA 1C C1   LD           A,($C11C)
3867: FE 07      CP           $07
3869: C8         RET         Z
386A: AF         XOR         A
386B: EA C1 C3   LD           ($C3C1),A
386E: F0 F7      LD           A,($F7)
3870: FE 0A      CP           $0A
3872: F0 E7      LD           A,($E7)
3874: 38 01      JR           C,$3877
3876: AF         XOR         A
3877: E6 03      AND         $03
3879: 5F         LD           E,A
387A: 16 00      LD           D,$00
387C: 21 3F 38   LD           HL,$383F
387F: 19         ADD         HL,DE
3880: 7E         LD           A,(HL)
3881: EA C0 C3   LD           ($C3C0),A
3884: FA A0 C5   LD           A,($C5A0)
3887: EA A1 C5   LD           ($C5A1),A
388A: AF         XOR         A
388B: EA A0 C5   LD           ($C5A0),A
388E: EA 0C C1   LD           ($C10C),A
3891: E0 B2      LDFF00   ($B2),A
3893: EA 17 C1   LD           ($C117),A
3896: EA 9D C1   LD           ($C19D),A
3899: EA 47 C1   LD           ($C147),A
389C: EA A8 C5   LD           ($C5A8),A
389F: EA 5E D4   LD           ($D45E),A
38A2: FA 9F C1   LD           A,($C19F)
38A5: A7         AND         A
38A6: 20 03      JR           NZ,$38AB
38A8: EA AD C1   LD           ($C1AD),A
38AB: 3E 02      LD           A,$02
38AD: CD B9 07   CALL       $07B9
38B0: CD E6 63   CALL       $63E6
38B3: 06 00      LD           B,$00
38B5: 0E 0F      LD           C,$0F
38B7: 79         LD           A,C
38B8: EA 23 C1   LD           ($C123),A
38BB: 21 80 C2   LD           HL,$C280
38BE: 09         ADD         HL,BC
38BF: 7E         LD           A,(HL)
38C0: A7         AND         A
38C1: 28 05      JR           Z,$38C8
38C3: E0 EA      LDFF00   ($EA),A
38C5: CD DD 38   CALL       $38DD
38C8: 0D         DEC         C
38C9: 79         LD           A,C
38CA: FE FF      CP           $FF
38CC: 20 E9      JR           NZ,$38B7
38CE: C9         RET
38CF: 3E 15      LD           A,$15
38D1: EA 00 21   LD           ($2100),A
38D4: CD 00 40   CALL       $4000
38D7: 3E 03      LD           A,$03
38D9: EA 00 21   LD           ($2100),A
38DC: C9         RET
38DD: 21 A0 C3   LD           HL,$C3A0
38E0: 09         ADD         HL,BC
38E1: 7E         LD           A,(HL)
38E2: E0 EB      LDFF00   ($EB),A
38E4: 21 90 C2   LD           HL,$C290
38E7: 09         ADD         HL,BC
38E8: 7E         LD           A,(HL)
38E9: E0 F0      LDFF00   ($F0),A
38EB: 21 B0 C3   LD           HL,$C3B0
38EE: 09         ADD         HL,BC
38EF: 7E         LD           A,(HL)
38F0: E0 F1      LDFF00   ($F1),A
38F2: 3E 19      LD           A,$19
38F4: CD B9 07   CALL       $07B9
38F7: F0 EB      LD           A,($EB)
38F9: FE 6A      CP           $6A
38FB: 20 05      JR           NZ,$3902
38FD: F0 B2      LD           A,($B2)
38FF: A7         AND         A
3900: 20 06      JR           NZ,$3908
3902: F0 EA      LD           A,($EA)
3904: FE 07      CP           $07
3906: 20 08      JR           NZ,$3910
3908: CD 5F 75   CALL       $755F
390B: CD BA 3D   CALL       $3DBA
390E: 18 06      JR           $3916
3910: CD BA 3D   CALL       $3DBA
3913: CD 5F 75   CALL       $755F
3916: 3E 14      LD           A,$14
3918: CD B9 07   CALL       $07B9
391B: CD 88 53   CALL       $5388
391E: 3E 03      LD           A,$03
3920: CD B9 07   CALL       $07B9
3923: F0 EA      LD           A,($EA)
3925: FE 05      CP           $05
3927: CA 45 39   JP           Z,$3945
392A: C7         RST         0X00
392B: CE 38      ADC         $38
392D: 7E         LD           A,(HL)
392E: 55         LD           D,L
392F: 90         SUB         B
3930: 4D         LD           C,L
3931: 26 4D      LD           H,$4D
3933: 0A         LD           A,(BC)
3934: 49         LD           C,C
3935: 45         LD           B,L
3936: 39         ADD         HL,SP
3937: BC         CP           H
3938: 4E         LD           C,(HL)
3939: 92         SUB         D
393A: 57         LD           D,A
393B: 49         LD           C,C
393C: 4E         LD           C,(HL)
393D: CD 45 39   CALL       $3945
3940: 3E 03      LD           A,$03
3942: C3 B9 07   JP           $07B9
3945: F0 EB      LD           A,($EB)
3947: 5F         LD           E,A
3948: 50         LD           D,B
3949: 21 00 40   LD           HL,$4000
394C: 19         ADD         HL,DE
394D: 7E         LD           A,(HL)
394E: CD B9 07   CALL       $07B9
3951: 7B         LD           A,E
3952: C7         RST         0X00
3953: 4B         LD           C,E
3954: 6A         LD           L,D
3955: 61         LD           H,C
3956: 44         LD           B,H
3957: BF         CP           A
3958: 66         LD           H,(HL)
3959: 61         LD           H,C
395A: 7B         LD           A,E
395B: C9         RET
395C: 69         LD           L,C
395D: 97         SUB         A
395E: 53         LD           D,E
395F: BE         CP           (HL)
3960: 52         LD           D,D
3961: E3                              
3962: 7A         LD           A,D
3963: 30 79      JR           NC,$39DE
3965: 44         LD           B,H
3966: 58         LD           E,B
3967: 3D         DEC         A
3968: 6A         LD           L,D
3969: 82         ADD         A,D
396A: 58         LD           E,B
396B: E7         RST         0X20
396C: 6A         LD           L,D
396D: CD 79 6B   CALL       $6B79
3970: 7E         LD           A,(HL)
3971: 47         LD           B,A
3972: 75         LD           (HL),L
3973: 04         INC         B
3974: 5C         LD           E,H
3975: FF         RST         0X38
3976: 5B         LD           E,E
3977: 04         INC         B
3978: 5C         LD           E,H
3979: 35         DEC         (HL)
397A: 5A         LD           E,D
397B: 5E         LD           E,(HL)
397C: 78         LD           A,B
397D: 7B         LD           A,E
397E: 79         LD           A,C
397F: 41         LD           B,C
3980: 66         LD           H,(HL)
3981: 41         LD           B,C
3982: 66         LD           H,(HL)
3983: 70         LD           (HL),B
3984: 74         LD           (HL),H
3985: 3C         INC         A
3986: 67         LD           H,A
3987: CE 4A      ADC         $4A
3989: FC                              
398A: 7C         LD           A,H
398B: D0         RET         NC
398C: 7C         LD           A,H
398D: 00         NOP
398E: 00         NOP
398F: AB         XOR         E
3990: 4E         LD           C,(HL)
3991: 5F         LD           E,A
3992: 7F         LD           A,A
3993: 5D         LD           E,L
3994: 4F         LD           C,A
3995: 27         DAA
3996: 77         LD           (HL),A
3997: FB         EI
3998: 65         LD           H,L
3999: B5         OR           L
399A: 7E         LD           A,(HL)
399B: B4         OR           H
399C: 50         LD           D,B
399D: 1E 4D      LD           E,$4D
399F: 1E 4D      LD           E,$4D
39A1: 0B         DEC         BC
39A2: 76         HALT
39A3: 65         LD           H,L
39A4: 67         LD           H,A
39A5: 8B         ADC         A,E
39A6: 5A         LD           E,D
39A7: 2B         DEC         HL
39A8: 6C         LD           L,H
39A9: E5         PUSH       HL
39AA: 75         LD           (HL),L
39AB: BC         CP           H
39AC: 76         HALT
39AD: 7F         LD           A,A
39AE: 5D         LD           E,L
39AF: C0         RET         NZ
39B0: 60         LD           H,B
39B1: 7D         LD           A,L
39B2: 61         LD           H,C
39B3: D0         RET         NC
39B4: 5C         LD           E,H
39B5: DC 5B CB   CALL       C,$CB5B
39B8: 5B         LD           E,E
39B9: B0         OR           B
39BA: 5B         LD           E,E
39BB: A0         AND         B
39BC: 5B         LD           E,E
39BD: 9C         SBC         H
39BE: 5A         LD           E,D
39BF: 39         ADD         HL,SP
39C0: 5A         LD           E,D
39C1: 9D         SBC         L
39C2: 60         LD           H,B
39C3: EE 5F      XOR         $5F
39C5: DA 5D 92   JP           C,$925D
39C8: 5D         LD           E,L
39C9: 83         ADD         A,E
39CA: 60         LD           H,B
39CB: 29         ADD         HL,HL
39CC: 60         LD           H,B
39CD: FF         RST         0X38
39CE: 5F         LD           E,A
39CF: E5         PUSH       HL
39D0: 4D         LD           C,L
39D1: 15         DEC         D
39D2: 49         LD           C,C
39D3: E1         POP         HL
39D4: 47         LD           B,A
39D5: 01 68 68   LD           BC,$6868
39D8: 5E         LD           E,(HL)
39D9: 94         SUB         H
39DA: 44         LD           B,H
39DB: 3F         CCF
39DC: 44         LD           B,H
39DD: 65         LD           H,L
39DE: 43         LD           B,E
39DF: FD                              
39E0: 40         LD           B,B
39E1: C7         RST         0X00
39E2: 41         LD           B,C
39E3: 3A         LD           A,(HLD)
39E4: 42         LD           B,D
39E5: AD         XOR         L
39E6: 42         LD           B,D
39E7: 00         NOP
39E8: 00         NOP
39E9: 95         SUB         L
39EA: 53         LD           D,E
39EB: 00         NOP
39EC: 00         NOP
39ED: 79         LD           A,C
39EE: 76         HALT
39EF: 2B         DEC         HL
39F0: 76         HALT
39F1: 46         LD           B,(HL)
39F2: 6E         LD           L,(HL)
39F3: B3         OR           E
39F4: 7A         LD           A,D
39F5: 71         LD           (HL),C
39F6: 69         LD           L,C
39F7: E6 67      AND         $67
39F9: E6 67      AND         $67
39FB: 59         LD           E,C
39FC: 5F         LD           E,A
39FD: 80         ADD         A,B
39FE: 7D         LD           A,L
39FF: 90         SUB         B
3A00: 7C         LD           A,H
3A01: E9         JP           (HL)
3A02: 5D         LD           E,L
3A03: F7         RST         0X30
3A04: 5E         LD           E,(HL)
3A05: 9D         SBC         L
3A06: 56         LD           D,(HL)
3A07: 72         LD           (HL),D
3A08: 50         LD           D,B
3A09: C1         POP         BC
3A0A: 49         LD           C,C
3A0B: 09         ADD         HL,BC
3A0C: 40         LD           B,B
3A0D: 41         LD           B,C
3A0E: 6C         LD           L,H
3A0F: 05         DEC         B
3A10: 7B         LD           A,E
3A11: 4D         LD           C,L
3A12: 69         LD           L,C
3A13: CD 67 16   CALL       $1667
3A16: 42         LD           B,D
3A17: 61         LD           H,C
3A18: 62         LD           H,D
3A19: BB         CP           E
3A1A: 59         LD           E,C
3A1B: EF         RST         0X28
3A1C: 5D         LD           E,L
3A1D: AA         XOR         D
3A1E: 54         LD           D,H
3A1F: 24         INC         H
3A20: 43         LD           B,E
3A21: 9F         SBC         A
3A22: 54         LD           D,H
3A23: 58         LD           E,B
3A24: 74         LD           (HL),H
3A25: C2 53 9E   JP           NZ,$9E53
3A28: 52         LD           D,D
3A29: 8B         ADC         A,E
3A2A: 5D         LD           E,L
3A2B: 2E 45      LD           L,$45
3A2D: 38 40      JR           C,$3A6F
3A2F: B4         OR           H
3A30: 6B         LD           L,E
3A31: 94         SUB         H
3A32: 48         LD           C,B
3A33: 48         LD           C,B
3A34: 62         LD           H,D
3A35: C3 60 C3   JP           $C360
3A38: 60         LD           H,B
3A39: 48         LD           C,B
3A3A: 62         LD           H,D
3A3B: BF         CP           A
3A3C: 4D         LD           C,L
3A3D: A4         AND         H
3A3E: 4C         LD           C,H
3A3F: 33         INC         SP
3A40: 4B         LD           C,E
3A41: E8 5C      ADD         SP,$5C
3A43: BE         CP           (HL)
3A44: 5A         LD           E,D
3A45: 4E         LD           C,(HL)
3A46: 5C         LD           E,H
3A47: 5C         LD           E,H
3A48: 5D         LD           E,L
3A49: FD                              
3A4A: 5E         LD           E,(HL)
3A4B: DE 62      SBC         $62
3A4D: CD 63 2A   CALL       $2A63
3A50: 64         LD           H,H
3A51: C6 72      ADD         $72
3A53: 88         ADC         A,B
3A54: 6A         LD           L,D
3A55: 58         LD           E,B
3A56: 6C         LD           L,H
3A57: D4 6E 66   CALL       NC,$666E
3A5A: 70         LD           (HL),B
3A5B: C9         RET
3A5C: 71         LD           (HL),C
3A5D: 39         ADD         HL,SP
3A5E: 73         LD           (HL),E
3A5F: 19         ADD         HL,DE
3A60: 7C         LD           A,H
3A61: B5         OR           L
3A62: 56         LD           D,(HL)
3A63: A1         AND         C
3A64: 53         LD           D,E
3A65: 07         RLCA
3A66: 51         LD           D,C
3A67: 49         LD           C,C
3A68: 50         LD           D,B
3A69: 49         LD           C,C
3A6A: 50         LD           D,B
3A6B: BF         CP           A
3A6C: 4E         LD           C,(HL)
3A6D: 36 4F      LD           (HL),$4F
3A6F: 92         SUB         D
3A70: 4B         LD           C,E
3A71: 77         LD           (HL),A
3A72: 47         LD           B,A
3A73: 49         LD           C,C
3A74: 49         LD           C,C
3A75: 47         LD           B,A
3A76: 42         LD           B,D
3A77: 1B         DEC         DE
3A78: 45         LD           B,L
3A79: 50         LD           D,B
3A7A: 41         LD           B,C
3A7B: AD         XOR         L
3A7C: 70         LD           (HL),B
3A7D: 20 40      JR           NZ,$3ABF
3A7F: FD                              
3A80: 5A         LD           E,D
3A81: 05         DEC         B
3A82: 48         LD           C,B
3A83: 03         INC         BC
3A84: 75         LD           (HL),L
3A85: 44         LD           B,H
3A86: 74         LD           (HL),H
3A87: 14         INC         D
3A88: 73         LD           (HL),E
3A89: B4         OR           H
3A8A: 71         LD           (HL),C
3A8B: 5E         LD           E,(HL)
3A8C: 71         LD           (HL),C
3A8D: 22         LD           (HLI),A
3A8E: 40         LD           B,B
3A8F: 31 70 F1   LD           SP,$F170
3A92: 63         LD           H,E
3A93: 25         DEC         H
3A94: 65         LD           H,L
3A95: 6D         LD           L,L
3A96: 66         LD           H,(HL)
3A97: FB         EI
3A98: 61         LD           H,C
3A99: BD         CP           L
3A9A: 60         LD           H,B
3A9B: BD         CP           L
3A9C: 60         LD           H,B
3A9D: 98         SBC         B
3A9E: 61         LD           H,C
3A9F: 54         LD           D,H
3AA0: 5F         LD           E,A
3AA1: 47         LD           B,A
3AA2: 5B         LD           E,E
3AA3: 87         ADD         A,A
3AA4: 5D         LD           E,L
3AA5: 7C         LD           A,H
3AA6: 59         LD           E,C
3AA7: 0A         LD           A,(BC)
3AA8: 68         LD           L,B
3AA9: 0A         LD           A,(BC)
3AAA: 68         LD           L,B
3AAB: 7E         LD           A,(HL)
3AAC: 68         LD           L,B
3AAD: D5         PUSH       DE
3AAE: 55         LD           D,L
3AAF: DC 53 C6   CALL       C,$C653
3AB2: 52         LD           D,D
3AB3: 09         ADD         HL,BC
3AB4: 51         LD           D,C
3AB5: 03         INC         BC
3AB6: 4F         LD           C,A
3AB7: 1C         INC         E
3AB8: 75         LD           (HL),L
3AB9: 88         ADC         A,B
3ABA: 4A         LD           C,D
3ABB: A8         XOR         B
3ABC: 4C         LD           C,H
3ABD: A3         AND         E
3ABE: 49         LD           C,C
3ABF: 0D         DEC         C
3AC0: 48         LD           C,B
3AC1: D3                              
3AC2: 44         LD           B,H
3AC3: 72         LD           (HL),D
3AC4: 42         LD           B,D
3AC5: 2B         DEC         HL
3AC6: 77         LD           (HL),A
3AC7: EA 77 15   LD           ($1577),A
3ACA: 40         LD           B,B
3ACB: A8         XOR         B
3ACC: 6F         LD           L,A
3ACD: C7         RST         0X00
3ACE: 69         LD           L,C
3ACF: A7         AND         A
3AD0: 64         LD           H,H
3AD1: 62         LD           H,D
3AD2: 63         LD           H,E
3AD3: 7D         LD           A,L
3AD4: 62         LD           H,D
3AD5: 76         HALT
3AD6: 61         LD           H,C
3AD7: B6         OR           (HL)
3AD8: 5E         LD           E,(HL)
3AD9: 00         NOP
3ADA: 40         LD           B,B
3ADB: F7         RST         0X30
3ADC: 54         LD           D,H
3ADD: C9         RET
3ADE: 73         LD           (HL),E
3ADF: 4E         LD           C,(HL)
3AE0: 73         LD           (HL),E
3AE1: 1D         DEC         E
3AE2: 45         LD           B,L
3AE3: 98         SBC         B
3AE4: 52         LD           D,D
3AE5: FC                              
3AE6: 50         LD           D,B
3AE7: 40         LD           B,B
3AE8: 4E         LD           C,(HL)
3AE9: F5         PUSH       AF
3AEA: 49         LD           C,C
3AEB: BD         CP           L
3AEC: 44         LD           B,H
3AED: 97         SUB         A
3AEE: 6B         LD           L,E
3AEF: 57         LD           D,A
3AF0: 49         LD           C,C
3AF1: 13         INC         DE
3AF2: 6E         LD           L,(HL)
3AF3: 32         LD           (HLD),A
3AF4: 51         LD           D,C
3AF5: 80         ADD         A,B
3AF6: 51         LD           D,C
3AF7: 5D         LD           E,L
3AF8: 52         LD           D,D
3AF9: CA 51 58   JP           Z,$5851
3AFC: 5D         LD           E,L
3AFD: 18 59      JR           $3B58
3AFF: 17         RLA
3B00: 58         LD           E,B
3B01: F3         DI
3B02: 55         LD           D,L
3B03: E8 56      ADD         SP,$56
3B05: C1         POP         BC
3B06: 54         LD           D,H
3B07: 44         LD           B,H
3B08: 53         LD           D,E
3B09: E4                              
3B0A: 52         LD           D,D
3B0B: 8A         ADC         A,D
3B0C: 51         LD           D,C
3B0D: 9A         SBC         D
3B0E: 4C         LD           C,H
3B0F: 1C         INC         E
3B10: 4A         LD           C,D
3B11: 27         DAA
3B12: 45         LD           B,L
3B13: 8A         ADC         A,D
3B14: 76         HALT
3B15: AC         XOR         H
3B16: 78         LD           A,B
3B17: 58         LD           E,B
3B18: 4D         LD           C,L
3B19: F5         PUSH       AF
3B1A: 4B         LD           C,E
3B1B: BE         CP           (HL)
3B1C: 46         LD           B,(HL)
3B1D: 19         ADD         HL,DE
3B1E: 7C         LD           A,H
3B1F: 96         SUB         (HL)
3B20: 50         LD           D,B
3B21: 9A         SBC         D
3B22: 40         LD           B,B
3B23: 47         LD           B,A
3B24: 75         LD           (HL),L
3B25: 08 05 08   LD           ($0805),SP
3B28: 05         DEC         B
3B29: 08 0A 08   LD           ($080A),SP
3B2C: 0A         LD           A,(BC)
3B2D: 08 0A 08   LD           ($080A),SP
3B30: 0A         LD           A,(BC)
3B31: 08 10 04   LD           ($0410),SP
3B34: 0A         LD           A,(BC)
3B35: 08 02 08   LD           ($0802),SP
3B38: 02         LD           (BC),A
3B39: 08 13 08   LD           ($0813),SP
3B3C: 13         INC         DE
3B3D: 08 06 06   LD           ($0606),SP
3B40: 08 08 07   LD           ($0708),SP
3B43: 06 0A      LD           B,$0A
3B45: 08 06 10   LD           ($1006),SP
3B48: 30 08      JR           NC,$3B52
3B4A: 07         RLCA
3B4B: 04         INC         B
3B4C: 0A         LD           A,(BC)
3B4D: 0C         INC         C
3B4E: 07         RLCA
3B4F: FC                              
3B50: 04         INC         B
3B51: 10 10      STOP       $10
3B53: 0C         INC         C
3B54: 12         LD           (DE),A
3B55: 08 08 02   LD           ($0208),SP
3B58: 08 10 0C   LD           ($0C10),SP
3B5B: 08 10 08   LD           ($0810),SP
3B5E: 07         RLCA
3B5F: 0C         INC         C
3B60: 08 08 08   LD           ($0808),SP
3B63: 02         LD           (BC),A
3B64: 08 21 50   LD           ($5021),SP
3B67: C3 09 7E   JP           $7E09
3B6A: E6 7C      AND         $7C
3B6C: 5F         LD           E,A
3B6D: 50         LD           D,B
3B6E: 21 25 3B   LD           HL,$3B25
3B71: 19         ADD         HL,DE
3B72: E5         PUSH       HL
3B73: D1         POP         DE
3B74: C5         PUSH       BC
3B75: CB 21      SLA         C
3B77: CB 21      SLA         C
3B79: 21 80 D5   LD           HL,$D580
3B7C: 09         ADD         HL,BC
3B7D: 0E 04      LD           C,$04
3B7F: 1A         LD           A,(DE)
3B80: 13         INC         DE
3B81: 22         LD           (HLI),A
3B82: 0D         DEC         C
3B83: 20 FA      JR           NZ,$3B7F
3B85: C1         POP         BC
3B86: C9         RET
3B87: 21 B0 C3   LD           HL,$C3B0
3B8A: 09         ADD         HL,BC
3B8B: 77         LD           (HL),A
3B8C: C9         RET
3B8D: 21 90 C2   LD           HL,$C290
3B90: 09         ADD         HL,BC
3B91: 34         INC         (HL)
3B92: C9         RET
3B93: 3E 02      LD           A,$02
3B95: EA 00 21   LD           ($2100),A
3B98: CD B5 78   CALL       $78B5
3B9B: C3 C0 07   JP           $07C0
3B9E: 3E 03      LD           A,$03
3BA0: EA 00 21   LD           ($2100),A
3BA3: CD 92 78   CALL       $7892
3BA6: C3 C0 07   JP           $07C0
3BA9: 3E 03      LD           A,$03
3BAB: EA 00 21   LD           ($2100),A
3BAE: CD AA 7C   CALL       $7CAA
3BB1: C3 C0 07   JP           $07C0
3BB4: 3E 03      LD           A,$03
3BB6: EA 00 21   LD           ($2100),A
3BB9: CD 3D 6E   CALL       $6E3D
3BBC: C3 C0 07   JP           $07C0
3BBF: 3E 03      LD           A,$03
3BC1: EA 00 21   LD           ($2100),A
3BC4: CD 87 6C   CALL       $6C87
3BC7: C3 C0 07   JP           $07C0
3BCA: 3E 03      LD           A,$03
3BCC: EA 00 21   LD           ($2100),A
3BCF: CD F9 6B   CALL       $6BF9
3BD2: C3 C0 07   JP           $07C0
3BD5: 3E 03      LD           A,$03
3BD7: EA 00 21   LD           ($2100),A
3BDA: CD 93 6C   CALL       $6C93
3BDD: C3 C0 07   JP           $07C0
3BE0: 3E 03      LD           A,$03
3BE2: EA 00 21   LD           ($2100),A
3BE5: CD EF 73   CALL       $73EF
3BE8: C3 C0 07   JP           $07C0
3BEB: 3E 03      LD           A,$03
3BED: EA 00 21   LD           ($2100),A
3BF0: CD 40 6E   CALL       $6E40
3BF3: C3 C0 07   JP           $07C0
3BF6: 3E 03      LD           A,$03
3BF8: EA 00 21   LD           ($2100),A
3BFB: CD A6 75   CALL       $75A6
3BFE: C3 C0 07   JP           $07C0
3C01: F5         PUSH       AF
3C02: 3E 03      LD           A,$03
3C04: EA 00 21   LD           ($2100),A
3C07: F1         POP         AF
3C08: CD F8 64   CALL       $64F8
3C0B: CB 1D      RR           L
3C0D: CD C0 07   CALL       $07C0
3C10: CB 15      RL           L
3C12: C9         RET
3C13: F5         PUSH       AF
3C14: 3E 03      LD           A,$03
3C16: EA 00 21   LD           ($2100),A
3C19: F1         POP         AF
3C1A: CD FA 64   CALL       $64FA
3C1D: CB 1D      RR           L
3C1F: CD C0 07   CALL       $07C0
3C22: CB 15      RL           L
3C24: C9         RET
3C25: 21 00 21   LD           HL,$2100
3C28: 36 03      LD           (HL),$03
3C2A: CD 99 7E   CALL       $7E99
3C2D: C3 C0 07   JP           $07C0
3C30: 21 00 21   LD           HL,$2100
3C33: 36 03      LD           (HL),$03
3C35: CD 17 7E   CALL       $7E17
3C38: C3 C0 07   JP           $07C0
3C3B: F0 F1      LD           A,($F1)
3C3D: 3C         INC         A
3C3E: C8         RET         Z
3C3F: CD 87 3D   CALL       $3D87
3C42: D5         PUSH       DE
3C43: FA C0 C3   LD           A,($C3C0)
3C46: 5F         LD           E,A
3C47: 50         LD           D,B
3C48: 21 30 C0   LD           HL,$C030
3C4B: 19         ADD         HL,DE
3C4C: E5         PUSH       HL
3C4D: D1         POP         DE
3C4E: F0 EC      LD           A,($EC)
3C50: 12         LD           (DE),A
3C51: 13         INC         DE
3C52: FA 55 C1   LD           A,($C155)
3C55: 4F         LD           C,A
3C56: F0 ED      LD           A,($ED)
3C58: E6 20      AND         $20
3C5A: 1F         RRA
3C5B: 1F         RRA
3C5C: 21 EE FF   LD           HL,$FFEE
3C5F: 86         ADD         A,(HL)
3C60: 91         SUB         C
3C61: 12         LD           (DE),A
3C62: 13         INC         DE
3C63: F0 F1      LD           A,($F1)
3C65: 4F         LD           C,A
3C66: 06 00      LD           B,$00
3C68: CB 21      SLA         C
3C6A: CB 10      RL           B
3C6C: CB 21      SLA         C
3C6E: CB 10      RL           B
3C70: E1         POP         HL
3C71: 09         ADD         HL,BC
3C72: F0 F5      LD           A,($F5)
3C74: 4F         LD           C,A
3C75: 2A         LD           A,(HLI)
3C76: 81         ADD         A,C
3C77: 12         LD           (DE),A
3C78: E6 0F      AND         $0F
3C7A: FE 0F      CP           $0F
3C7C: 20 05      JR           NZ,$3C83
3C7E: 1B         DEC         DE
3C7F: 3E F0      LD           A,$F0
3C81: 12         LD           (DE),A
3C82: 13         INC         DE
3C83: 13         INC         DE
3C84: 2A         LD           A,(HLI)
3C85: E5         PUSH       HL
3C86: 21 ED FF   LD           HL,$FFED
3C89: AE         XOR         (HL)
3C8A: 12         LD           (DE),A
3C8B: 13         INC         DE
3C8C: F0 EC      LD           A,($EC)
3C8E: 12         LD           (DE),A
3C8F: 13         INC         DE
3C90: FA 55 C1   LD           A,($C155)
3C93: 4F         LD           C,A
3C94: F0 ED      LD           A,($ED)
3C96: E6 20      AND         $20
3C98: EE 20      XOR         $20
3C9A: 1F         RRA
3C9B: 1F         RRA
3C9C: 21 EE FF   LD           HL,$FFEE
3C9F: 91         SUB         C
3CA0: 86         ADD         A,(HL)
3CA1: 12         LD           (DE),A
3CA2: 13         INC         DE
3CA3: E1         POP         HL
3CA4: F0 F5      LD           A,($F5)
3CA6: 4F         LD           C,A
3CA7: 2A         LD           A,(HLI)
3CA8: 81         ADD         A,C
3CA9: 12         LD           (DE),A
3CAA: E6 0F      AND         $0F
3CAC: FE 0F      CP           $0F
3CAE: 20 05      JR           NZ,$3CB5
3CB0: 1B         DEC         DE
3CB1: 3E F0      LD           A,$F0
3CB3: 12         LD           (DE),A
3CB4: 13         INC         DE
3CB5: 13         INC         DE
3CB6: 7E         LD           A,(HL)
3CB7: 21 ED FF   LD           HL,$FFED
3CBA: AE         XOR         (HL)
3CBB: 12         LD           (DE),A
3CBC: FA 23 C1   LD           A,($C123)
3CBF: 4F         LD           C,A
3CC0: 06 00      LD           B,$00
3CC2: 3E 15      LD           A,$15
3CC4: EA 00 21   LD           ($2100),A
3CC7: CD 6D 79   CALL       $796D
3CCA: CD A5 79   CALL       $79A5
3CCD: C3 C0 07   JP           $07C0
3CD0: F0 F1      LD           A,($F1)
3CD2: 3C         INC         A
3CD3: C8         RET         Z
3CD4: CD 87 3D   CALL       $3D87
3CD7: D5         PUSH       DE
3CD8: FA C0 C3   LD           A,($C3C0)
3CDB: 6F         LD           L,A
3CDC: 26 00      LD           H,$00
3CDE: 01 30 C0   LD           BC,$C030
3CE1: 09         ADD         HL,BC
3CE2: E5         PUSH       HL
3CE3: D1         POP         DE
3CE4: FA 23 C1   LD           A,($C123)
3CE7: 4F         LD           C,A
3CE8: 06 00      LD           B,$00
3CEA: F0 F9      LD           A,($F9)
3CEC: A7         AND         A
3CED: F0 EC      LD           A,($EC)
3CEF: 28 04      JR           Z,$3CF5
3CF1: D6 04      SUB         $04
3CF3: E0 EC      LDFF00   ($EC),A
3CF5: 12         LD           (DE),A
3CF6: 13         INC         DE
3CF7: FA 55 C1   LD           A,($C155)
3CFA: 67         LD           H,A
3CFB: F0 EE      LD           A,($EE)
3CFD: C6 04      ADD         $04
3CFF: 94         SUB         H
3D00: 12         LD           (DE),A
3D01: 13         INC         DE
3D02: F0 F1      LD           A,($F1)
3D04: 4F         LD           C,A
3D05: 06 00      LD           B,$00
3D07: CB 21      SLA         C
3D09: CB 10      RL           B
3D0B: E1         POP         HL
3D0C: 09         ADD         HL,BC
3D0D: 2A         LD           A,(HLI)
3D0E: 12         LD           (DE),A
3D0F: 13         INC         DE
3D10: 2A         LD           A,(HLI)
3D11: 21 ED FF   LD           HL,$FFED
3D14: AE         XOR         (HL)
3D15: 12         LD           (DE),A
3D16: 13         INC         DE
3D17: 18 A3      JR           $3CBC
3D19: 3E 15      LD           A,$15
3D1B: EA 00 21   LD           ($2100),A
3D1E: 18 AA      JR           $3CCA
3D20: E5         PUSH       HL
3D21: 21 00 C0   LD           HL,$C000
3D24: 18 10      JR           $3D36
3D26: F0 F1      LD           A,($F1)
3D28: 3C         INC         A
3D29: 28 57      JR           Z,$3D82
3D2B: E5         PUSH       HL
3D2C: FA C0 C3   LD           A,($C3C0)
3D2F: 5F         LD           E,A
3D30: 16 00      LD           D,$00
3D32: 21 30 C0   LD           HL,$C030
3D35: 19         ADD         HL,DE
3D36: E5         PUSH       HL
3D37: D1         POP         DE
3D38: E1         POP         HL
3D39: 79         LD           A,C
3D3A: E0 D7      LDFF00   ($D7),A
3D3C: FA 23 C1   LD           A,($C123)
3D3F: 4F         LD           C,A
3D40: CD 87 3D   CALL       $3D87
3D43: F0 D7      LD           A,($D7)
3D45: 4F         LD           C,A
3D46: F0 EC      LD           A,($EC)
3D48: 86         ADD         A,(HL)
3D49: 12         LD           (DE),A
3D4A: 23         INC         HL
3D4B: 13         INC         DE
3D4C: C5         PUSH       BC
3D4D: FA 55 C1   LD           A,($C155)
3D50: 4F         LD           C,A
3D51: F0 EE      LD           A,($EE)
3D53: 86         ADD         A,(HL)
3D54: 91         SUB         C
3D55: 12         LD           (DE),A
3D56: 23         INC         HL
3D57: 13         INC         DE
3D58: F0 F5      LD           A,($F5)
3D5A: 4F         LD           C,A
3D5B: 2A         LD           A,(HLI)
3D5C: F5         PUSH       AF
3D5D: 81         ADD         A,C
3D5E: 12         LD           (DE),A
3D5F: F1         POP         AF
3D60: FE FF      CP           $FF
3D62: 20 04      JR           NZ,$3D68
3D64: 1B         DEC         DE
3D65: AF         XOR         A
3D66: 12         LD           (DE),A
3D67: 13         INC         DE
3D68: C1         POP         BC
3D69: 13         INC         DE
3D6A: F0 ED      LD           A,($ED)
3D6C: AE         XOR         (HL)
3D6D: 23         INC         HL
3D6E: 12         LD           (DE),A
3D6F: 13         INC         DE
3D70: 0D         DEC         C
3D71: 20 D3      JR           NZ,$3D46
3D73: FA 23 C1   LD           A,($C123)
3D76: 4F         LD           C,A
3D77: 3E 15      LD           A,$15
3D79: EA 00 21   LD           ($2100),A
3D7C: CD 6D 79   CALL       $796D
3D7F: C3 C0 07   JP           $07C0
3D82: FA 23 C1   LD           A,($C123)
3D85: 4F         LD           C,A
3D86: C9         RET
3D87: E5         PUSH       HL
3D88: FA 24 C1   LD           A,($C124)
3D8B: A7         AND         A
3D8C: 28 1F      JR           Z,$3DAD
3D8E: F0 EE      LD           A,($EE)
3D90: 3D         DEC         A
3D91: FE C0      CP           $C0
3D93: 30 17      JR           NC,$3DAC
3D95: F0 EC      LD           A,($EC)
3D97: 3D         DEC         A
3D98: FE 88      CP           $88
3D9A: 30 10      JR           NC,$3DAC
3D9C: 21 20 C2   LD           HL,$C220
3D9F: 09         ADD         HL,BC
3DA0: 7E         LD           A,(HL)
3DA1: A7         AND         A
3DA2: 20 08      JR           NZ,$3DAC
3DA4: 21 30 C2   LD           HL,$C230
3DA7: 09         ADD         HL,BC
3DA8: 7E         LD           A,(HL)
3DA9: A7         AND         A
3DAA: 28 01      JR           Z,$3DAD
3DAC: F1         POP         AF
3DAD: E1         POP         HL
3DAE: C9         RET
3DAF: 21 40 C2   LD           HL,$C240
3DB2: 09         ADD         HL,BC
3DB3: 70         LD           (HL),B
3DB4: 21 50 C2   LD           HL,$C250
3DB7: 09         ADD         HL,BC
3DB8: 70         LD           (HL),B
3DB9: C9         RET
3DBA: 21 00 C2   LD           HL,$C200
3DBD: 09         ADD         HL,BC
3DBE: 7E         LD           A,(HL)
3DBF: E0 EE      LDFF00   ($EE),A
3DC1: 21 10 C2   LD           HL,$C210
3DC4: 09         ADD         HL,BC
3DC5: 7E         LD           A,(HL)
3DC6: E0 EF      LDFF00   ($EF),A
3DC8: 21 10 C3   LD           HL,$C310
3DCB: 09         ADD         HL,BC
3DCC: 96         SUB         (HL)
3DCD: E0 EC      LDFF00   ($EC),A
3DCF: C9         RET
3DD0: 21 00 21   LD           HL,$2100
3DD3: 36 15      LD           (HL),$15
3DD5: CD 74 79   CALL       $7974
3DD8: C3 C0 07   JP           $07C0
3DDB: 21 00 21   LD           HL,$2100
3DDE: 36 04      LD           (HL),$04
3DE0: CD 10 5A   CALL       $5A10
3DE3: C3 C0 07   JP           $07C0
3DE6: 21 00 21   LD           HL,$2100
3DE9: 36 04      LD           (HL),$04
3DEB: CD 80 56   CALL       $5680
3DEE: C3 C0 07   JP           $07C0
3DF1: 21 00 21   LD           HL,$2100
3DF4: 36 04      LD           (HL),$04
3DF6: CD 4D 50   CALL       $504D
3DF9: C3 C0 07   JP           $07C0
3DFC: 21 00 21   LD           HL,$2100
3DFF: 36 04      LD           (HL),$04
3E01: CD B5 49   CALL       $49B5
3E04: C3 C0 07   JP           $07C0
3E07: 21 00 21   LD           HL,$2100
3E0A: 36 04      LD           (HL),$04
3E0C: CD 00 40   CALL       $4000
3E0F: C3 C0 07   JP           $07C0
3E12: 21 00 21   LD           HL,$2100
3E15: 36 05      LD           (HL),$05
3E17: CD 2B 6C   CALL       $6C2B
3E1A: C3 C0 07   JP           $07C0
3E1D: 21 00 21   LD           HL,$2100
3E20: 36 05      LD           (HL),$05
3E22: CD 76 67   CALL       $6776
3E25: C3 C0 07   JP           $07C0
3E28: 21 00 21   LD           HL,$2100
3E2B: 36 05      LD           (HL),$05
3E2D: CD 4F 62   CALL       $624F
3E30: C3 C0 07   JP           $07C0
3E33: 21 00 21   LD           HL,$2100
3E36: 36 05      LD           (HL),$05
3E38: CD 59 59   CALL       $5959
3E3B: C3 C0 07   JP           $07C0
3E3E: 21 00 21   LD           HL,$2100
3E41: 36 05      LD           (HL),$05
3E43: CD 9F 54   CALL       $549F
3E46: C3 C0 07   JP           $07C0
3E49: FA AF DB   LD           A,($DBAF)
3E4C: F5         PUSH       AF
3E4D: 3E 02      LD           A,$02
3E4F: CD B9 07   CALL       $07B9
3E52: CD B1 6F   CALL       $6FB1
3E55: F1         POP         AF
3E56: C3 B9 07   JP           $07B9
3E59: 21 00 21   LD           HL,$2100
3E5C: 36 04      LD           (HL),$04
3E5E: CD 5A 5C   CALL       $5C5A
3E61: C3 C0 07   JP           $07C0
3E64: 21 00 21   LD           HL,$2100
3E67: 36 03      LD           (HL),$03
3E69: CD 64 54   CALL       $5464
3E6C: C3 C0 07   JP           $07C0
3E6F: 21 00 21   LD           HL,$2100
3E72: 36 02      LD           (HL),$02
3E74: CD D1 5F   CALL       $5FD1
3E77: CD 17 61   CALL       $6117
3E7A: C3 C0 07   JP           $07C0
3E7D: 3E 02      LD           A,$02
3E7F: CD B9 07   CALL       $07B9
3E82: CD BA 41   CALL       $41BA
3E85: 3E 03      LD           A,$03
3E87: C3 B9 07   JP           $07B9
3E8A: 21 00 21   LD           HL,$2100
3E8D: 36 02      LD           (HL),$02
3E8F: CD E7 61   CALL       $61E7
3E92: C3 C0 07   JP           $07C0
3E95: 21 00 21   LD           HL,$2100
3E98: 36 03      LD           (HL),$03
3E9A: CD 97 64   CALL       $6497
3E9D: C3 C0 07   JP           $07C0
3EA0: 3E 06      LD           A,$06
3EA2: CD B9 07   CALL       $07B9
3EA5: CD 40 79   CALL       $7940
3EA8: 3E 03      LD           A,$03
3EAA: C3 B9 07   JP           $07B9
3EAD: 1E 10      LD           E,$10
3EAF: 21 80 C2   LD           HL,$C280
3EB2: AF         XOR         A
3EB3: 22         LD           (HLI),A
3EB4: 1D         DEC         E
3EB5: 20 FB      JR           NZ,$3EB2
3EB7: C9         RET
3EB8: 21 A0 C4   LD           HL,$C4A0
3EBB: 09         ADD         HL,BC
3EBC: 7E         LD           A,(HL)
3EBD: A7         AND         A
3EBE: C8         RET         Z
3EBF: F0 E7      LD           A,($E7)
3EC1: A9         XOR         C
3EC2: E6 03      AND         $03
3EC4: C0         RET         NZ
3EC5: F0 EE      LD           A,($EE)
3EC7: E0 D7      LDFF00   ($D7),A
3EC9: F0 EC      LD           A,($EC)
3ECB: E0 D8      LDFF00   ($D8),A
3ECD: 3E 08      LD           A,$08
3ECF: CD 53 09   CALL       $0953
3ED2: 21 20 C5   LD           HL,$C520
3ED5: 19         ADD         HL,DE
3ED6: 36 0F      LD           (HL),$0F
3ED8: C9         RET
3ED9: 21 F0 C3   LD           HL,$C3F0
3EDC: 09         ADD         HL,BC
3EDD: 7E         LD           A,(HL)
3EDE: CB 7F      BIT         7,A
3EE0: 28 02      JR           Z,$3EE4
3EE2: 2F         CPL
3EE3: 3C         INC         A
3EE4: E0 D7      LDFF00   ($D7),A
3EE6: 21 00 C4   LD           HL,$C400
3EE9: 09         ADD         HL,BC
3EEA: 7E         LD           A,(HL)
3EEB: CB 7F      BIT         7,A
3EED: 28 02      JR           Z,$3EF1
3EEF: 2F         CPL
3EF0: 3C         INC         A
3EF1: 1E 03      LD           E,$03
3EF3: 21 D7 FF   LD           HL,$FFD7
3EF6: BE         CP           (HL)
3EF7: 38 02      JR           C,$3EFB
3EF9: 1E 0C      LD           E,$0C
3EFB: 7B         LD           A,E
3EFC: 21 A0 C2   LD           HL,$C2A0
3EFF: 09         ADD         HL,BC
3F00: A6         AND         (HL)
3F01: 28 05      JR           Z,$3F08
3F03: 21 10 C4   LD           HL,$C410
3F06: 09         ADD         HL,BC
3F07: 70         LD           (HL),B
3F08: C9         RET
3F09: B0         OR           B
3F0A: B4         OR           H
3F0B: B1         OR           C
3F0C: B2         OR           D
3F0D: B3         OR           E
3F0E: B6         OR           (HL)
3F0F: BA         CP           D
3F10: BC         CP           H
3F11: B8         CP           B
3F12: 21 4F C1   LD           HL,$C14F
3F15: FA 24 C1   LD           A,($C124)
3F18: B6         OR           (HL)
3F19: C0         RET         NZ
3F1A: FA 65 C1   LD           A,($C165)
3F1D: A7         AND         A
3F1E: 28 05      JR           Z,$3F25
3F20: 3D         DEC         A
3F21: EA 65 C1   LD           ($C165),A
3F24: C9         RET
3F25: FA BD C1   LD           A,($C1BD)
3F28: A7         AND         A
3F29: C0         RET         NZ
3F2A: 3C         INC         A
3F2B: EA BD C1   LD           ($C1BD),A
3F2E: 21 30 C4   LD           HL,$C430
3F31: 09         ADD         HL,BC
3F32: 7E         LD           A,(HL)
3F33: E6 04      AND         $04
3F35: 3E 19      LD           A,$19
3F37: 28 02      JR           Z,$3F3B
3F39: 3E 50      LD           A,$50
3F3B: EA 68 D3   LD           ($D368),A
3F3E: E0 BD      LDFF00   ($BD),A
3F40: FA 6B C1   LD           A,($C16B)
3F43: FE 04      CP           $04
3F45: C0         RET         NZ
3F46: F0 EB      LD           A,($EB)
3F48: FE 87      CP           $87
3F4A: 20 04      JR           NZ,$3F50
3F4C: 3E DA      LD           A,$DA
3F4E: 18 1E      JR           $3F6E
3F50: FE BC      CP           $BC
3F52: 20 04      JR           NZ,$3F58
3F54: 3E 26      LD           A,$26
3F56: 18 16      JR           $3F6E
3F58: 21 30 C4   LD           HL,$C430
3F5B: 09         ADD         HL,BC
3F5C: 7E         LD           A,(HL)
3F5D: E6 04      AND         $04
3F5F: 20 10      JR           NZ,$3F71
3F61: F0 F7      LD           A,($F7)
3F63: FE 05      CP           $05
3F65: 28 0A      JR           Z,$3F71
3F67: 5F         LD           E,A
3F68: 50         LD           D,B
3F69: 21 09 3F   LD           HL,$3F09
3F6C: 19         ADD         HL,DE
3F6D: 7E         LD           A,(HL)
3F6E: CD 97 21   CALL       $2197
3F71: C9         RET
3F72: 01 02 04   LD           BC,$0402
3F75: 08 10 20   LD           ($2010),SP
3F78: 40         LD           B,B
3F79: 80         ADD         A,B
3F7A: 3E 03      LD           A,$03
3F7C: EA 13 C1   LD           ($C113),A
3F7F: EA 00 21   LD           ($2100),A
3F82: CD 2F 56   CALL       $562F
3F85: CD C0 07   CALL       $07C0
3F88: 21 60 C4   LD           HL,$C460
3F8B: 09         ADD         HL,BC
3F8C: 7E         LD           A,(HL)
3F8D: FE FF      CP           $FF
3F8F: 28 26      JR           Z,$3FB7
3F91: F5         PUSH       AF
3F92: FA B5 DB   LD           A,($DBB5)
3F95: 5F         LD           E,A
3F96: 50         LD           D,B
3F97: 3C         INC         A
3F98: EA B5 DB   LD           ($DBB5),A
3F9B: 7E         LD           A,(HL)
3F9C: 21 B6 DB   LD           HL,$DBB6
3F9F: 19         ADD         HL,DE
3FA0: 77         LD           (HL),A
3FA1: F1         POP         AF
3FA2: FE 08      CP           $08
3FA4: 30 11      JR           NC,$3FB7
3FA6: 5F         LD           E,A
3FA7: 50         LD           D,B
3FA8: 21 72 3F   LD           HL,$3F72
3FAB: 19         ADD         HL,DE
3FAC: F0 F6      LD           A,($F6)
3FAE: 5F         LD           E,A
3FAF: 50         LD           D,B
3FB0: 7E         LD           A,(HL)
3FB1: 21 00 CF   LD           HL,$CF00
3FB4: 19         ADD         HL,DE
3FB5: B6         OR           (HL)
3FB6: 77         LD           (HL),A
3FB7: 21 80 C2   LD           HL,$C280
3FBA: 09         ADD         HL,BC
3FBB: 70         LD           (HL),B
3FBC: C9         RET
3FBD: 3E 05      LD           A,$05
3FBF: EA 00 21   LD           ($2100),A
3FC2: 21 19 59   LD           HL,$5919
3FC5: 11 60 84   LD           DE,$8460
3FC8: 01 10 00   LD           BC,$0010
3FCB: CD C5 28   CALL       $28C5
3FCE: 21 29 59   LD           HL,$5929
3FD1: 18 14      JR           $3FE7
3FD3: 3E 05      LD           A,$05
3FD5: EA 00 21   LD           ($2100),A
3FD8: 21 39 59   LD           HL,$5939
3FDB: 11 60 84   LD           DE,$8460
3FDE: 01 10 00   LD           BC,$0010
3FE1: CD C5 28   CALL       $28C5
3FE4: 21 49 59   LD           HL,$5949
3FE7: 11 80 84   LD           DE,$8480
3FEA: 01 10 00   LD           BC,$0010
3FED: CD C5 28   CALL       $28C5
3FF0: AF         XOR         A
3FF1: E0 A5      LDFF00   ($A5),A
3FF3: 3E 0C      LD           A,$0C
3FF5: EA 00 21   LD           ($2100),A
3FF8: C3 CC 1C   JP           $1CCC
3FFB: FF         RST         0X38
3FFC: FF         RST         0X38
3FFD: FF         RST         0X38
3FFE: FF         RST         0X38
3FFF: FF         RST         0X38
```
